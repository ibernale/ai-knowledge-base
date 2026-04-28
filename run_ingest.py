"""AI Knowledge Base ingest pipeline.

Daily cron: identifies new high-value AI items via Claude+web_search,
downloads each item, converts to clean Markdown, and writes:
  - knowledge/<type>/YYYY-MM-DD-<slug>.md      (short note)
  - knowledge/<type>/YYYY-MM-DD-<slug>.full.md (full content)

Then updates knowledge/_index/ingested.json with the canonical URL of
each ingested item, so subsequent runs can dedupe.

Usage:
    python run_ingest.py
"""

from __future__ import annotations

import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import anthropic
import httpx

# Optional dependencies, used inside try-blocks so partial install still works.
try:
    import fitz  # pymupdf
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

try:
    import trafilatura
    HAS_TRAFILATURA = True
except ImportError:
    HAS_TRAFILATURA = False


# --- Configuration -----------------------------------------------------------

MODEL = "claude-opus-4-5"
MAX_TOKENS = 8000          # JSON list output is far smaller than a full brief
MAX_WEB_SEARCHES = 25      # enough for tier-by-tier sweep

PROMPT_PATH = Path("master_prompt_ingest.md")
KNOWLEDGE_DIR = Path("knowledge")
INDEX_DIR = KNOWLEDGE_DIR / "_index"
INDEX_FILE = INDEX_DIR / "ingested.json"

KNOWLEDGE_DIR.mkdir(exist_ok=True)
INDEX_DIR.mkdir(exist_ok=True)
for sub in ("papers", "blog-posts", "reports"):
    (KNOWLEDGE_DIR / sub).mkdir(exist_ok=True)

USER_AGENT = "ai-kb-ingest/1.0 (+https://github.com)"
HTTP_TIMEOUT = 30.0


# --- Index of already-ingested URLs -----------------------------------------

def load_index() -> dict[str, Any]:
    """Load the dedup index. Schema: {"items": [{"url":..., "ingested":...}, ...]}."""
    if not INDEX_FILE.exists():
        return {"items": []}
    try:
        return json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print("WARNING: index file unreadable, starting fresh", file=sys.stderr)
        return {"items": []}


def save_index(index: dict[str, Any]) -> None:
    INDEX_FILE.write_text(
        json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def normalise_url(url: str) -> str:
    """Strip tracking params and trailing slashes for stable comparison."""
    url = url.strip().rstrip("/")
    # Strip common tracking query params
    url = re.sub(r"\?utm_[^&]+(&utm_[^&]+)*$", "", url)
    url = re.sub(r"&utm_[^&]+", "", url)
    # Normalize arXiv: always abs/, never pdf/, no version suffix
    m = re.match(r"https?://arxiv\.org/(abs|pdf)/(\d+\.\d+)(v\d+)?(\.pdf)?", url)
    if m:
        return f"https://arxiv.org/abs/{m.group(2)}"
    return url


# --- Claude: identify candidates --------------------------------------------

def identify_candidates(prior_urls: list[str]) -> list[dict[str, Any]]:
    """Ask Claude to return a JSON list of items to ingest today."""
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    already_block = "\n".join(f"- {u}" for u in prior_urls[-300:])  # last 300 is plenty
    user_message = (
        f"Today's date is {today}.\n\n"
        f"<already_ingested>\n{already_block}\n</already_ingested>\n\n"
        "Identify items to ingest now. Return ONLY the JSON array."
    )

    client = anthropic.Anthropic()
    print(f"Calling {MODEL} to identify candidates...", flush=True)

    text_chunks: list[str] = []
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": MAX_WEB_SEARCHES,
        }],
    ) as stream:
        for text in stream.text_stream:
            text_chunks.append(text)

    raw = "".join(text_chunks).strip()

    # Extract the JSON array. Claude usually returns clean JSON but defend
    # against the occasional ```json fence or leading prose.
    fenced = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", raw, re.DOTALL)
    if fenced:
        raw = fenced.group(1)
    else:
        # Find the first '[' and last ']'
        start = raw.find("[")
        end = raw.rfind("]")
        if start != -1 and end > start:
            raw = raw[start:end + 1]

    try:
        items = json.loads(raw)
        if not isinstance(items, list):
            raise ValueError("Top-level JSON is not a list")
        return items
    except (json.JSONDecodeError, ValueError) as e:
        print(f"ERROR parsing Claude's JSON: {e}", file=sys.stderr)
        print(f"Raw output (first 500 chars): {raw[:500]}", file=sys.stderr)
        return []


# --- Content download and conversion ----------------------------------------

@dataclass
class Fetched:
    """Result of trying to download and convert an item to Markdown."""
    markdown: str | None
    note: str  # "ok", "abstract-only", "fetch-failed", etc.


def fetch_arxiv(arxiv_url: str) -> Fetched:
    """Try ar5iv first (clean HTML), fall back to PDF text extraction."""
    m = re.match(r"https?://arxiv\.org/abs/(\d+\.\d+)", arxiv_url)
    if not m:
        return Fetched(None, "bad-arxiv-url")
    paper_id = m.group(1)

    # Attempt 1: ar5iv
    ar5iv_url = f"https://ar5iv.labs.arxiv.org/html/{paper_id}"
    try:
        with httpx.Client(timeout=HTTP_TIMEOUT, follow_redirects=True,
                          headers={"User-Agent": USER_AGENT}) as client:
            resp = client.get(ar5iv_url)
        if resp.status_code == 200 and HAS_TRAFILATURA:
            md = trafilatura.extract(
                resp.text,
                output_format="markdown",
                include_links=True,
                include_tables=True,
            )
            if md and len(md) > 1000:
                return Fetched(md, "ar5iv")
    except (httpx.HTTPError, Exception) as e:
        print(f"  ar5iv failed: {e}", file=sys.stderr)

    # Attempt 2: PDF
    if not HAS_FITZ:
        return Fetched(None, "no-fitz")
    pdf_url = f"https://arxiv.org/pdf/{paper_id}"
    try:
        with httpx.Client(timeout=HTTP_TIMEOUT, follow_redirects=True,
                          headers={"User-Agent": USER_AGENT}) as client:
            resp = client.get(pdf_url)
        if resp.status_code != 200:
            return Fetched(None, f"pdf-status-{resp.status_code}")
        doc = fitz.open(stream=resp.content, filetype="pdf")
        pages = []
        for page in doc:
            pages.append(page.get_text())
        doc.close()
        text = "\n\n".join(pages)
        # Light cleanup
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        return Fetched(f"# Full text\n\n{text}", "pdf-extracted")
    except Exception as e:
        return Fetched(None, f"pdf-failed-{type(e).__name__}")


def fetch_html(url: str) -> Fetched:
    """Generic HTML fetch + extract for blogs and most reports."""
    if not HAS_TRAFILATURA:
        return Fetched(None, "no-trafilatura")
    try:
        with httpx.Client(timeout=HTTP_TIMEOUT, follow_redirects=True,
                          headers={"User-Agent": USER_AGENT}) as client:
            resp = client.get(url)
        if resp.status_code != 200:
            return Fetched(None, f"html-status-{resp.status_code}")
        md = trafilatura.extract(
            resp.text,
            output_format="markdown",
            include_links=True,
            include_tables=True,
            include_images=False,
        )
        if not md or len(md) < 200:
            return Fetched(None, "html-too-short")
        return Fetched(md, "html-extracted")
    except Exception as e:
        return Fetched(None, f"html-failed-{type(e).__name__}")


def fetch_full_content(item: dict[str, Any]) -> Fetched:
    """Dispatch to arxiv or html fetcher based on item source."""
    url = item.get("url", "")
    if "arxiv.org" in url:
        return fetch_arxiv(url)
    return fetch_html(url)


# --- Note writing ------------------------------------------------------------

def slugify(text: str, max_length: int = 60) -> str:
    """Filesystem-safe slug from a title."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:max_length].rstrip("-") or "untitled"


def folder_for_type(item_type: str) -> Path:
    mapping = {
        "paper": KNOWLEDGE_DIR / "papers",
        "blog-post": KNOWLEDGE_DIR / "blog-posts",
        "report": KNOWLEDGE_DIR / "reports",
    }
    return mapping.get(item_type, KNOWLEDGE_DIR / "blog-posts")


def write_note(item: dict[str, Any], full_content: Fetched) -> tuple[Path, Path | None]:
    """Write the short note and (if available) the full-content companion.

    Returns (short_note_path, full_note_path_or_None).
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slug = slugify(item.get("title", "untitled"))
    folder = folder_for_type(item.get("type", "blog-post"))

    short_path = folder / f"{today}-{slug}.md"
    full_path: Path | None = None

    # Frontmatter
    fm_lines = ["---"]
    fm_lines.append(f"title: {json.dumps(item.get('title', ''))}")
    fm_lines.append(f"url: {item.get('url', '')}")
    fm_lines.append(f"source: {item.get('source', 'other')}")
    fm_lines.append(f"type: {item.get('type', 'blog-post')}")
    authors = item.get("authors") or []
    fm_lines.append(f"authors: {json.dumps(authors, ensure_ascii=False)}")
    fm_lines.append(f"published: {item.get('published_date', '')}")
    fm_lines.append(f"ingested: {today}")
    tags = item.get("tags") or []
    fm_lines.append(f"tags: {json.dumps(tags)}")
    fm_lines.append("---\n")
    frontmatter = "\n".join(fm_lines)

    # If we have a full-content companion, write it first so we can wikilink to it.
    if full_content.markdown:
        full_path = folder / f"{today}-{slug}.full.md"
        full_fm = (
            "---\n"
            f"title: {json.dumps(item.get('title', '') + ' (full text)')}\n"
            f"url: {item.get('url', '')}\n"
            f"source: {item.get('source', 'other')}\n"
            f"type: full-text\n"
            f"parent: \"[[{short_path.stem}]]\"\n"
            f"ingested: {today}\n"
            f"extraction: {full_content.note}\n"
            "---\n\n"
        )
        full_path.write_text(full_fm + full_content.markdown, encoding="utf-8")

    # Build the short note body
    body = [frontmatter, f"# {item.get('title', 'Untitled')}\n"]

    body.append("## Why it matters")
    body.append(item.get("why_it_matters", "_Not provided_"))
    body.append("")

    abstract = item.get("abstract_or_lede")
    if abstract:
        label = "Abstract" if item.get("type") == "paper" else "Lede"
        body.append(f"## {label} (original)")
        body.append(abstract)
        body.append("")

    body.append("## Source")
    body.append(f"[{item.get('url', '')}]({item.get('url', '')})")
    body.append("")

    if full_path is not None:
        body.append("## Full text")
        body.append(f"[[{full_path.stem}]] (extracted: {full_content.note})")
    else:
        body.append("## Full text")
        body.append(f"_Not extracted: {full_content.note}_")

    short_path.write_text("\n".join(body), encoding="utf-8")
    return short_path, full_path


# --- Main --------------------------------------------------------------------

def main() -> int:
    if not PROMPT_PATH.exists():
        print(f"ERROR: prompt file not found: {PROMPT_PATH}", file=sys.stderr)
        return 1

    if not HAS_TRAFILATURA:
        print("ERROR: trafilatura is required (pip install trafilatura)", file=sys.stderr)
        return 1

    index = load_index()
    prior_urls = {normalise_url(item["url"]) for item in index.get("items", [])}
    print(f"Index loaded: {len(prior_urls)} prior URLs.")

    candidates = identify_candidates(sorted(prior_urls))
    print(f"Claude returned {len(candidates)} candidates.")

    if not candidates:
        print("Nothing to ingest today.")
        return 0

    ingested_today = 0
    for item in candidates:
        url = normalise_url(item.get("url", ""))
        if not url:
            print("SKIP: missing url")
            continue
        if url in prior_urls:
            print(f"SKIP (already in index): {url}")
            continue

        print(f"\nIngesting: {item.get('title', '?')[:80]}")
        print(f"  URL: {url}")
        try:
            fetched = fetch_full_content({**item, "url": url})
        except Exception as e:
            fetched = Fetched(None, f"unhandled-{type(e).__name__}")

        try:
            short_path, full_path = write_note({**item, "url": url}, fetched)
            print(f"  Wrote: {short_path}")
            if full_path:
                print(f"  Wrote: {full_path}")
        except Exception as e:
            print(f"  ERROR writing note: {e}", file=sys.stderr)
            continue

        # Record in the index, even if full extraction failed — short note is enough.
        index["items"].append({
            "url": url,
            "title": item.get("title", ""),
            "ingested": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "extraction": fetched.note,
        })
        prior_urls.add(url)
        ingested_today += 1

    save_index(index)
    print(f"\nIngested {ingested_today} new items today.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

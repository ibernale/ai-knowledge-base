"""AI Knowledge Base ingest pipeline (v2, sources-driven).

Daily cron: identifies new high-value AI items via Claude+web_search,
downloads each item, converts to clean Markdown, and writes:
  - knowledge/<type>/YYYY-MM-DD-<slug>.md      (short note)
  - knowledge/<type>/YYYY-MM-DD-<slug>.full.md (full content)

Then updates knowledge/_index/ingested.json with the canonical URL of
each ingested item, so subsequent runs can dedupe.

v2 changes:
- Loads sources.md and injects it in the user message as a sources catalog.
- Higher max_tokens and max_web_searches to support 8-15 items/day target.

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

try:
    import fitz
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

try:
    import trafilatura
    HAS_TRAFILATURA = True
except ImportError:
    HAS_TRAFILATURA = False


MODEL = "claude-opus-4-5"
MAX_TOKENS = 12000
MAX_WEB_SEARCHES = 40

PROMPT_PATH = Path("master_prompt_ingest.md")
SOURCES_PATH = Path("sources.md")
KNOWLEDGE_DIR = Path("knowledge")
INDEX_DIR = KNOWLEDGE_DIR / "_index"
INDEX_FILE = INDEX_DIR / "ingested.json"

KNOWLEDGE_DIR.mkdir(exist_ok=True)
INDEX_DIR.mkdir(exist_ok=True)
for sub in ("papers", "blog-posts", "reports"):
    (KNOWLEDGE_DIR / sub).mkdir(exist_ok=True)

USER_AGENT = "ai-kb-ingest/2.0 (+https://github.com)"
HTTP_TIMEOUT = 30.0


def load_index() -> dict[str, Any]:
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
    url = url.strip().rstrip("/")
    url = re.sub(r"\?utm_[^&]+(&utm_[^&]+)*$", "", url)
    url = re.sub(r"&utm_[^&]+", "", url)
    m = re.match(r"https?://arxiv\.org/(abs|pdf)/(\d+\.\d+)(v\d+)?(\.pdf)?", url)
    if m:
        return f"https://arxiv.org/abs/{m.group(2)}"
    return url


def identify_candidates(prior_urls: list[str]) -> list[dict[str, Any]]:
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")
    sources_catalog = SOURCES_PATH.read_text(encoding="utf-8") if SOURCES_PATH.exists() else ""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    already_block = "\n".join(f"- {u}" for u in prior_urls[-500:])

    user_message = (
        f"Today's date is {today}.\n\n"
        f"<already_ingested>\n{already_block}\n</already_ingested>\n\n"
        f"<sources_catalog>\n{sources_catalog}\n</sources_catalog>\n\n"
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

    fenced = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", raw, re.DOTALL)
    if fenced:
        raw = fenced.group(1)
    else:
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


@dataclass
class Fetched:
    markdown: str | None
    note: str


def fetch_arxiv(arxiv_url: str) -> Fetched:
    m = re.match(r"https?://arxiv\.org/abs/(\d+\.\d+)", arxiv_url)
    if not m:
        return Fetched(None, "bad-arxiv-url")
    paper_id = m.group(1)

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
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        return Fetched(f"# Full text\n\n{text}", "pdf-extracted")
    except Exception as e:
        return Fetched(None, f"pdf-failed-{type(e).__name__}")


def fetch_html(url: str) -> Fetched:
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
    url = item.get("url", "")
    if "arxiv.org" in url:
        return fetch_arxiv(url)
    return fetch_html(url)


def slugify(text: str, max_length: int = 60) -> str:
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
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slug = slugify(item.get("title", "untitled"))
    folder = folder_for_type(item.get("type", "blog-post"))

    short_path = folder / f"{today}-{slug}.md"
    full_path: Path | None = None

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


def main() -> int:
    if not PROMPT_PATH.exists():
        print(f"ERROR: prompt file not found: {PROMPT_PATH}", file=sys.stderr)
        return 1
    if not SOURCES_PATH.exists():
        print(f"WARNING: sources catalog not found: {SOURCES_PATH}", file=sys.stderr)
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

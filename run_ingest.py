"""AI Knowledge Base ingest pipeline (v3).

v3 changes vs v2:
- Hardened HTML/PDF fetching: better headers, smarter wrapper-page detection,
  and graceful handling of scanned PDFs.
- Two-pass extraction for consultancy pages: if the landing HTML looks like
  a wrapper that links to a PDF, follow the link and extract the PDF instead.
- Higher token budget (model needs to fit ~15 items with 80-120 word why_it_matters).

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
from urllib.parse import urljoin, urlparse

import anthropic
import httpx

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


MODEL = "claude-opus-4-5"
MAX_TOKENS = 16000        # bumped from 12000 — 15 items with longer why_it_matters
MAX_WEB_SEARCHES = 50     # bumped from 40 to support the explicit author checklist

PROMPT_PATH = Path("master_prompt_ingest.md")
SOURCES_PATH = Path("sources.md")
KNOWLEDGE_DIR = Path("knowledge")
INDEX_DIR = KNOWLEDGE_DIR / "_index"
INDEX_FILE = INDEX_DIR / "ingested.json"

KNOWLEDGE_DIR.mkdir(exist_ok=True)
INDEX_DIR.mkdir(exist_ok=True)
for sub in ("papers", "blog-posts", "reports"):
    (KNOWLEDGE_DIR / sub).mkdir(exist_ok=True)

# Realistic browser-like headers improve fetch success on consultancy and
# corporate sites that 403 anything that smells like a script.
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/pdf,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
}
HTTP_TIMEOUT = 45.0
MIN_PDF_TEXT = 500          # pymupdf < this many chars => probably scanned
MIN_HTML_MD_LEN = 200       # below this, treat html extraction as failed


# --- Index of already-ingested URLs -----------------------------------------

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


# --- Claude: identify candidates --------------------------------------------

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


# --- Content download and conversion ----------------------------------------

@dataclass
class Fetched:
    markdown: str | None
    note: str


def http_get(url: str, *, accept: str | None = None) -> httpx.Response:
    """Single shared HTTP getter with browser-like headers."""
    headers = dict(DEFAULT_HEADERS)
    if accept:
        headers["Accept"] = accept
    with httpx.Client(timeout=HTTP_TIMEOUT, follow_redirects=True, headers=headers) as client:
        return client.get(url)


def extract_pdf_text(pdf_bytes: bytes) -> tuple[str | None, str]:
    """Returns (text, note). text is None if extraction failed or too short."""
    if not HAS_FITZ:
        return None, "no-fitz"
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        pages = [page.get_text() for page in doc]
        doc.close()
        text = re.sub(r"\n{3,}", "\n\n", "\n\n".join(pages)).strip()
        if len(text) < MIN_PDF_TEXT:
            return None, "scanned-or-empty-pdf"
        return text, "pdf-extracted"
    except Exception as e:
        return None, f"pdf-failed-{type(e).__name__}"


def extract_html_markdown(html: str) -> tuple[str | None, str]:
    """Returns (markdown, note). markdown is None if extraction failed."""
    if not HAS_TRAFILATURA:
        return None, "no-trafilatura"
    md = trafilatura.extract(
        html,
        output_format="markdown",
        include_links=True,
        include_tables=True,
        include_images=False,
    )
    if not md or len(md) < MIN_HTML_MD_LEN:
        return None, "html-too-short"
    return md, "html-extracted"


def find_pdf_link_in_html(html: str, base_url: str) -> str | None:
    """For consultancy pages: find a link to a PDF if the page is a wrapper.

    Looks for the first plausible PDF link near the top of the page or in
    common 'download' anchors.
    """
    # Direct .pdf links
    pdf_match = re.search(
        r'href=["\']([^"\']+\.pdf(?:\?[^"\']*)?)["\']',
        html,
        re.IGNORECASE,
    )
    if pdf_match:
        return urljoin(base_url, pdf_match.group(1))

    # "download report" / "view PDF" anchors with non-.pdf URLs (some sites obfuscate)
    dl_match = re.search(
        r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>\s*(?:download|view)\s+(?:full\s+)?(?:report|pdf|the\s+report)',
        html,
        re.IGNORECASE,
    )
    if dl_match:
        return urljoin(base_url, dl_match.group(1))

    return None


def fetch_arxiv(arxiv_url: str) -> Fetched:
    """ar5iv first, then PDF fallback."""
    m = re.match(r"https?://arxiv\.org/abs/(\d+\.\d+)", arxiv_url)
    if not m:
        return Fetched(None, "bad-arxiv-url")
    paper_id = m.group(1)

    # Attempt 1: ar5iv HTML
    try:
        resp = http_get(f"https://ar5iv.labs.arxiv.org/html/{paper_id}")
        if resp.status_code == 200:
            md, note = extract_html_markdown(resp.text)
            if md:
                return Fetched(md, "ar5iv")
    except Exception as e:
        print(f"  ar5iv failed: {type(e).__name__}: {e}", file=sys.stderr)

    # Attempt 2: PDF
    try:
        resp = http_get(f"https://arxiv.org/pdf/{paper_id}", accept="application/pdf")
        if resp.status_code != 200:
            return Fetched(None, f"pdf-status-{resp.status_code}")
        text, note = extract_pdf_text(resp.content)
        if text:
            return Fetched(f"# Full text\n\n{text}", note)
        return Fetched(None, note)
    except Exception as e:
        return Fetched(None, f"pdf-failed-{type(e).__name__}")


def fetch_html_or_wrapped_pdf(url: str) -> Fetched:
    """For non-arXiv URLs.

    Logic:
    1. Fetch the URL.
    2. If response is a PDF, extract text from it.
    3. If response is HTML, try markdown extraction.
    4. If markdown extraction yields too little, look inside the HTML for a
       PDF link (consultancy wrapper case) and try that PDF.
    """
    try:
        resp = http_get(url)
    except Exception as e:
        return Fetched(None, f"http-failed-{type(e).__name__}")

    if resp.status_code != 200:
        return Fetched(None, f"http-status-{resp.status_code}")

    content_type = resp.headers.get("content-type", "").lower()

    # Case 1: response IS a PDF
    if "application/pdf" in content_type or url.lower().endswith(".pdf"):
        text, note = extract_pdf_text(resp.content)
        if text:
            return Fetched(f"# Full text\n\n{text}", note)
        return Fetched(None, note)

    # Case 2: HTML — try direct markdown extraction
    md, note = extract_html_markdown(resp.text)
    if md:
        return Fetched(md, "html-extracted")

    # Case 3: HTML extraction too short — likely a wrapper page. Look for a PDF.
    pdf_link = find_pdf_link_in_html(resp.text, url)
    if pdf_link:
        print(f"  HTML wrapper detected — trying {pdf_link}")
        try:
            pdf_resp = http_get(pdf_link, accept="application/pdf")
            if pdf_resp.status_code == 200:
                text, pdf_note = extract_pdf_text(pdf_resp.content)
                if text:
                    return Fetched(f"# Full text\n\n{text}", "wrapped-pdf-extracted")
                return Fetched(None, pdf_note)
        except Exception as e:
            return Fetched(None, f"wrapped-pdf-failed-{type(e).__name__}")

    return Fetched(None, note)  # html-too-short, no wrapped PDF found


def fetch_full_content(item: dict[str, Any]) -> Fetched:
    url = item.get("url", "")
    if "arxiv.org" in url:
        return fetch_arxiv(url)
    return fetch_html_or_wrapped_pdf(url)


# --- Note writing ------------------------------------------------------------

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


# Tags the LLM is allowed to emit (research/* + governance/*).
# Mirrors _spine/tag-vocabulary.md and master_prompt_ingest.md.
ALLOWED_LLM_TAGS = {
    "research/agents", "research/rag", "research/evals", "research/alignment",
    "research/safety", "research/interpretability", "research/moe",
    "research/long-context", "research/reasoning", "research/multimodal",
    "research/robotics", "research/distillation", "research/pretraining",
    "research/posttraining", "research/inference", "research/hardware",
    "research/benchmarks", "research/agentic-coding", "research/tool-use",
    "research/economics", "research/industry", "research/regulation",
    "research/model-release",
    "governance/eu-ai-act", "governance/dora", "governance/gdpr",
    "governance/eba", "governance/nis2",
}

# Legacy flat tags → hierarchical equivalents. Belt-and-suspenders for the
# transition period in case the LLM regresses.
FLAT_TO_HIER = {
    "policy": "research/regulation",
    "economics": "research/economics",
    "industry": "research/industry",
    "model-release": "research/model-release",
    **{t: f"research/{t}" for t in (
        "agents", "rag", "evals", "alignment", "safety", "interpretability",
        "moe", "long-context", "reasoning", "multimodal", "robotics",
        "distillation", "pretraining", "posttraining", "inference",
        "hardware", "benchmarks", "agentic-coding", "tool-use", "regulation",
    )},
}

ITEM_TYPE_TO_TAG = {
    "paper": "type/paper",
    "blog-post": "type/blog",
    "report": "type/report",
}


def normalise_tags(raw_tags: list[str], item_type: str) -> list[str]:
    """Coerce LLM tags into the hierarchical vocabulary, then add the
    structural tags (type/* and access/*) that the pipeline owns."""
    out: list[str] = []
    seen: set[str] = set()
    for tag in raw_tags or []:
        if not isinstance(tag, str):
            continue
        t = tag.strip().lower()
        if "/" not in t:
            t = FLAT_TO_HIER.get(t, t)
        if t in ALLOWED_LLM_TAGS and t not in seen:
            out.append(t)
            seen.add(t)
    type_tag = ITEM_TYPE_TO_TAG.get(item_type, "type/blog")
    if type_tag not in seen:
        out.append(type_tag)
    out.append("access/public")
    return out


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
    tags = normalise_tags(item.get("tags") or [], item.get("type", "blog-post"))
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


# --- Main --------------------------------------------------------------------

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
    extraction_summary: dict[str, int] = {}
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
                print(f"  Wrote: {full_path} (extraction: {fetched.note})")
            else:
                print(f"  No full content — extraction: {fetched.note}")
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
        extraction_summary[fetched.note] = extraction_summary.get(fetched.note, 0) + 1
        ingested_today += 1

    save_index(index)
    print(f"\n=== Ingested {ingested_today} new items today ===")
    if extraction_summary:
        print("Extraction breakdown:")
        for note, count in sorted(extraction_summary.items()):
            print(f"  {note}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

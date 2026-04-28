# AI Knowledge Base

Self-updating personal knowledge base of high-value AI research, blog posts and reports. New items are ingested daily via GitHub Actions and synced into Obsidian.

## How it works

Every day at 06:30 UTC, a GitHub Action runs `run_ingest.py`, which:
1. Asks Claude (with web search) to identify items worth ingesting in the last 24-36 hours.
2. Skips anything whose URL already lives in `knowledge/_index/ingested.json`.
3. For each new item, downloads the full content (HTML for blogs, ar5iv/PDF for arXiv).
4. Writes two files per item:
   - A **short note** with metadata, "Why it matters", abstract/lede, and a wikilink.
   - A **full-content companion** (`.full.md`) with the extracted body.
5. Appends the canonical URL to the dedup index.
6. Commits the new notes back to the repo.

## Repo layout

```
ai-knowledge-base/
├── master_prompt_ingest.md   # the system prompt for Claude
├── run_ingest.py             # the ingest pipeline
├── requirements.txt
├── README.md
├── .github/workflows/
│   └── ingest.yml
└── knowledge/                # this is the Obsidian vault content
    ├── papers/               # .md notes for arXiv papers
    ├── blog-posts/           # .md notes for lab/Substack posts
    ├── reports/              # .md notes for analyst/consultancy reports
    └── _index/
        └── ingested.json     # canonical-URL log for dedup
```

## Using it from Obsidian

Clone the repo locally and either:
- Open the repo root as a vault (you'll see prompt, script, and the knowledge/ tree).
- Or open just `knowledge/` as a vault for a cleaner experience.

Install the **Obsidian Git** community plugin and configure:
- Auto pull interval: 60 minutes
- Auto pull on startup: yes
- Disable push: yes (the source of truth is GitHub Actions, not your laptop)

## Tag vocabulary

Closed list — see `master_prompt_ingest.md` for the canonical set. Examples:
`agents` `rag` `evals` `alignment` `interpretability` `moe` `long-context`
`reasoning` `multimodal` `agentic-coding` `tool-use` `policy` `benchmarks`.

## Manual run

From the Actions tab → "Daily AI Knowledge Ingest" → "Run workflow".

## Cost

Roughly $1.50–3.00 per run depending on how many items get ingested.
At 30 runs/month, expect $50–90/month maximum.

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
├── CLAUDE.md                 # context for Claude Code
├── master_prompt_ingest.md   # the system prompt for Claude
├── run_ingest.py             # the ingest pipeline
├── requirements.txt
├── README.md
├── _spine/                   # git submodule → kb-spine (schemas, lint, templates, tag vocab)
├── .github/workflows/
│   └── ingest.yml            # daily run, with lint + PII gate
└── knowledge/                # the Obsidian vault content
    ├── papers/               # .md notes for arXiv papers (raw, ingested)
    ├── blog-posts/           # .md notes for lab/Substack posts (raw, ingested)
    ├── reports/              # .md notes for analyst/consultancy reports (raw, ingested)
    ├── wiki/                 # human prose, evergreen
    ├── entities/             # human-curated: people, orgs, labs, models, products
    ├── concepts/             # curated concepts (and _candidates/ auto-drafted)
    ├── daily/                # daily notes (and _weekly/ exec digests)
    ├── auto/                 # pipeline-only, never edit by hand
    └── _index/
        └── ingested.json     # canonical-URL log for dedup
```

The `_spine/` submodule is the **single source of truth** for schemas, the closed tag vocabulary, lint scripts, and templates — shared across all four KB vaults (research, santander, saas, tech). See `_spine/docs/conventions.md`.

## Using it from Obsidian

Clone the repo locally and either:
- Open the repo root as a vault (you'll see prompt, script, and the knowledge/ tree).
- Or open just `knowledge/` as a vault for a cleaner experience.

Install the **Obsidian Git** community plugin and configure:
- Auto pull interval: 60 minutes
- Auto pull on startup: yes
- Disable push: yes (the source of truth is GitHub Actions, not your laptop)

## Tag vocabulary

Closed, hierarchical list. Single source of truth: `_spine/tag-vocabulary.md`.
Examples: `research/agents`, `research/rag`, `governance/eu-ai-act`, `type/paper`, `access/public`.

Every note carries exactly one `type/*` and one `access/*` tag — the pipeline injects these for ingested items.

## Manual run

From the Actions tab → "Daily AI Knowledge Ingest" → "Run workflow".

## Cost

Roughly $1.50–3.00 per run depending on how many items get ingested.
At 30 runs/month, expect $50–90/month maximum.

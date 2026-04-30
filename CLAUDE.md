# ai-knowledge-base — context for Claude Code

This file is loaded automatically when this repository is opened. Read it before doing anything.

## What this is

Personal AI research second brain, ingested daily by `run_ingest.py` (run via GitHub Actions). Public GitHub repo, private. Owned by Ignacio Bernal.

This vault is **one of four** in a coordinated knowledge-base system. Shared scaffolding (tag vocabulary, schemas, lint, templates) lives in the sibling `kb-spine` repo, mounted here as a git submodule under `_spine/`.

## The single invariant

**Pipeline writes only to `auto/` and to the raw folders (`knowledge/papers/`, `knowledge/blog-posts/`, `knowledge/reports/`, `knowledge/daily/`, `knowledge/daily/_weekly/`, `knowledge/concepts/_candidates/`).**

**Humans (and Claude when invoked from this repo) write everywhere else.**

If you ever feel the urge to edit something under `auto/`, you are doing it wrong: edit the corresponding hand-written sibling instead. Hand-written notes transclude their auto companion with `![[auto/.../<slug>]]`.

This invariant is non-negotiable. It is the entire reason the architecture works.

## Folder model

```
knowledge/
├── papers/                 ← raw, ingested by pipeline
├── blog-posts/             ← raw, ingested
├── reports/                ← raw, ingested
├── wiki/                   ← human prose, evergreen
├── entities/               ← human-curated entity notes
│   ├── people/
│   ├── orgs/
│   ├── labs/
│   ├── models/
│   └── products/
├── concepts/
│   └── _candidates/        ← LLM-drafted concept candidates (you promote or delete weekly)
├── daily/
│   └── _weekly/            ← exec digests, auto-generated Sundays
├── auto/                   ← pipeline-only territory. NEVER edit here.
└── _index/
    └── ingested.json       ← URL dedup ledger
```

## Conventions (single source of truth: `_spine/docs/conventions.md`)

- **Frontmatter**: every Markdown file (except `.full.md` raw companions) carries YAML frontmatter validated against a JSON Schema in `_spine/schemas/`.
- **Tag vocabulary**: closed, hierarchical. Lives in `_spine/tag-vocabulary.md`. Lint rejects anything else. Every note carries exactly one `type/*` and one `access/*` tag (the pipeline injects these for ingested items).
- **Wikilinks**: prefer bare basenames `[[andrej-karpathy]]`. Use path-style only for `auto/` transclusions: `![[auto/entities/people/andrej-karpathy]]`.
- **File naming**: `YYYY-MM-DD-<slug>.md` for ingested items, `<slug>.md` everywhere else. Slug regex: `^[a-z0-9][a-z0-9-]*$`.

## Language

The vault content is in English (research and exec deliverables). Conversation with the user is in Spanish unless they say otherwise.

## When the user asks you to write a wiki / entity / concept note

1. Read `_spine/docs/conventions.md` and `_spine/tag-vocabulary.md`.
2. Use the appropriate template under `_spine/templates/` as the structural starting point.
3. Save to the right folder under `knowledge/`. **Never** to `auto/`.
4. Run `python _spine/lint/lint_vault.py knowledge --only-files <new-file>` before declaring done.

## When something is contradictory

If a note in `wiki/`, `entities/`, or `concepts/` contradicts a paper in `papers/`, the wiki is the human source of truth and the raw is just material — but flag the contradiction openly to the user before committing.

## Pipeline ownership

The pipeline (`run_ingest.py`) is owned by you (Claude) when explicitly asked to modify it. Do **not** modify it as a side effect of other work. The GitHub Action runs daily at 06:30 UTC; a broken pipeline costs the user a day of ingestion.

## Plugins (Obsidian)

- `obsidian-git` — required for sync.
- `obsidian-local-rest-api` — required for MCP integration.
- `templater-obsidian` — for note creation from `_spine/templates/`.
- `dataview` — for vault-wide queries on entity / concept tags.

Do not propose installing AI plugins inside Obsidian — LLM work should go through Claude Code, not embedded plugins, so vault scope is auditable.

## Commit style

Conventional commits in English: `feat(spine): ...`, `fix(pipeline): ...`, `docs(conventions): ...`, `chore(scaffolding): ...`.

## When in doubt

Ask. A clarifying question is cheaper than a wrong write to a vault that gets committed and pushed.

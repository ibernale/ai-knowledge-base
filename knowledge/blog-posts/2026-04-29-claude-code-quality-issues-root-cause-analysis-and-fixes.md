---
title: "Claude Code Quality Issues: Root Cause Analysis and Fixes"
url: "https://www.anthropic.com/engineering/claude-code-quality-fixes"
source: "anthropic"
type: "blog-post"
authors: ["Anthropic Engineering"]
published: "2026-04-20"
ingested: "2026-04-29"
tags: ["research/agentic-coding", "research/posttraining", "type/blog", "access/public"]
---
# Claude Code Quality Issues: Root Cause Analysis and Fixes

## Why it matters
Detailed post-mortem on three bugs that degraded Claude Code quality: a caching bug dropping thinking history, a verbosity prompt change hurting coding quality, and context management issues at the API intersection. Notable that Opus 4.7 caught the bug in back-testing while Opus 4.6 missed it. Anthropic is adding support for additional repositories as context for code reviews. Transparency on production AI system failures is rare and valuable.

## Lede (original)
We traced recent reports of Claude Code quality issues to three separate changes that affected Claude Code, the Claude Agent SDK, and Claude Cowork. The API was not impacted. All three issues have now been resolved as of April 20 (v2.1.116). In this post, we explain what we found, what we fixed, and what we'll do differently to ensure similar issues are much less likely to happen again.

## Source
[https://www.anthropic.com/engineering/claude-code-quality-fixes](https://www.anthropic.com/engineering/claude-code-quality-fixes)

## Full text
_Not extracted: html-status-404_
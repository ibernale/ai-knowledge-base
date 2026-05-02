---
title: "Simon Willison: Codex CLI 0.128.0 adds /goal and GPT-5.5 cyber evaluation coverage"
url: https://simonwillison.net/2026/May/1
source: substack
type: blog-post
authors: ["Simon Willison"]
published: "2026-05-01"
ingested: "2026-05-02"
tags: ["research/agentic-coding", "research/agents", "research/safety", "type/blog", "access/public"]
---

# Simon Willison: Codex CLI 0.128.0 adds /goal and GPT-5.5 cyber evaluation coverage

## Why it matters
Simon Willison covers two significant developments: (1) OpenAI's Codex CLI 0.128.0 adds a /goal command implementing their version of the 'Ralph loop' for autonomous goal-directed coding with token budget limits; (2) The UK AISI's GPT-5.5 cyber evaluation showing it matches Mythos but is generally available now. Willison notes the system prompts implementing goal continuation are injected via goals/continuation.md and goals/budget_limit.md files. This is key documentation of evolving agentic coding patterns from a leading practitioner voice.

## Lede (original)
The latest version of OpenAI's Codex CLI coding agent adds their own version of the Ralph loop: you can now set a /goal and Codex will keep on looping until it evaluates that the goal has been completed... or the configured token budget has been exhausted. The UK's AI Security Institute previously evaluated Claude Mythos: now they've evaluated GPT-5.5 for finding security vulnerabilities and found it to be comparable to Mythos, but unlike Mythos it's generally available right now.

## Source
[https://simonwillison.net/2026/May/1](https://simonwillison.net/2026/May/1)

## Full text
_Not extracted: html-too-short_
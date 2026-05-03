---
type: wiki
title: "LLM Evals and Benchmarks"
slug: llm-evals
status: draft
tags: [type/wiki, access/public, research/evals, research/benchmarks]
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# LLM Evals and Benchmarks

_Working synthesis on evaluation methodology. Hand-written; the live item list is auto-generated and transcluded from `auto/concepts/research-evals`._

## My take

The most under-rated lever in shipping LLM applications is **a small, well-curated eval set with rubric-based grading run on every prompt change.** Vibes-check is not a strategy. The teams that move fast at quality have a regression test for their prompts.

Tensions I'm tracking:

- LLM-as-judge calibration: how often does the judge agree with humans, and how do you eval the judge?
- Eval-set drift: when input distribution shifts, does the eval still measure what we want?
- Cost / latency of running the full set on every release.

## Live: items tagged `research/evals` (auto)

![[auto/concepts/research-evals]]

## Live: items tagged `research/benchmarks` (auto)

![[auto/concepts/research-benchmarks]]

## See also

- [[agentic-systems]]
- Hamel Husain's blog (auto rollup): `![[auto/entities/people/hamel-husain]]`

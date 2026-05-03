---
type: wiki
title: "Agentic Systems"
slug: agentic-systems
status: draft
tags: [type/wiki, access/public, research/agents]
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# Agentic Systems

_Working synthesis on the agentic-AI track. Hand-written prose; the live item lists below are auto-generated rollups transcluded from `auto/concepts/`._

## My take

The interesting line in agentic AI today isn't "can the model decide" — it's **what control-flow primitives let a debate / multi-tool / long-horizon plan stay legible to a human reviewer**. LangGraph state machines + interrupts (HITL) are the closest production-grade answer; everything else either re-invents that or pretends it doesn't matter.

Open threads I'm tracking:

- Eval discipline for multi-agent debates (the "investment committee" pattern in `[[twincore]]`).
- How prompt-version drift interacts with traditional model-risk-management.
- MCP as the cross-product tool surface ([[mcp-tooling-pattern]] in `tech-kb`).

## Live: items tagged `research/agents` (auto)

![[auto/concepts/research-agents]]

## Live: items tagged `research/agentic-coding` (auto)

![[auto/concepts/research-agentic-coding]]

## Live: items tagged `research/tool-use` (auto)

![[auto/concepts/research-tool-use]]

## Related entities (auto rollups)

The pipeline auto-generates per-person rollups under `auto/entities/people/` and per-org under `auto/entities/orgs/`. Useful to follow:

- `![[auto/entities/people/jack-clark]]` (Jack Clark / Import AI)
- `![[auto/entities/orgs/anthropic]]`
- `![[auto/entities/orgs/openai]]`
- `![[auto/entities/orgs/deepmind]]`

## See also

- [[llm-evals]]
- [[inference-cost]]

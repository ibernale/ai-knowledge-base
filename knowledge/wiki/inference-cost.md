---
type: wiki
title: "Inference Cost and Efficiency"
slug: inference-cost
status: draft
tags: [type/wiki, access/public, research/inference, research/hardware]
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# Inference Cost and Efficiency

_Working synthesis on serving cost. Hand-written; live items transcluded from `auto/concepts/`._

## My take

Token cost is dropping fast — but per-task cost isn't, because the field keeps adding latency-multiplicative tricks (extended thinking, multi-agent debate, tool loops). The real lever for cost reduction in production is **provider abstraction with a smart router**: cheap model for the easy 80%, frontier model for the hard 20%, with an eval gate deciding which is which.

Watch:

- Specialized inference engines (vLLM, SGLang, llama.cpp).
- Serving providers race-to-bottom (Together, Fireworks, Groq).
- Hardware: H100/H200 → B200/B300, TPU v5p, MI300X.

## Live: items tagged `research/inference` (auto)

![[auto/concepts/research-inference]]

## Live: items tagged `research/hardware` (auto)

![[auto/concepts/research-hardware]]

## See also

- [[agentic-systems]]
- [[llm-evals]]

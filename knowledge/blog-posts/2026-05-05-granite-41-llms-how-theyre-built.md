---
title: "Granite 4.1 LLMs: How They're Built"
url: https://huggingface.co/blog/ibm-granite/granite-4-1
source: huggingface
type: blog-post
authors: ["Granite Team", "IBM"]
published: "2026-04-29"
ingested: "2026-05-05"
tags: ["research/pretraining", "research/posttraining", "research/model-release", "type/blog", "access/public"]
---

# Granite 4.1 LLMs: How They're Built

## Why it matters
IBM's technical deep-dive on the Granite 4.1 training pipeline reveals how they achieved competitive small-model performance through rigorous data curation and a five-phase pre-training strategy covering 15T+ tokens. Key innovations include multi-stage reinforcement learning via on-policy GRPO with DAPO loss and long-context extension to 512K tokens. The 8B instruct model notably matches or surpasses the previous 32B MoE model, demonstrating that dense architectures can match MoE efficiency at smaller scales with the right training recipe. All models Apache 2.0 licensed.

## Lede (original)
TL;DR — Granite 4.1 is a family of dense, decoder‑only LLMs (3B, 8B, and 30B) trained on ~15T tokens using a multi‑stage pre‑training pipeline, including long‑context extension of up to 512K tokens.

## Source
[https://huggingface.co/blog/ibm-granite/granite-4-1](https://huggingface.co/blog/ibm-granite/granite-4-1)

## Full text
[[2026-05-05-granite-41-llms-how-theyre-built.full]] (extracted: html-extracted)
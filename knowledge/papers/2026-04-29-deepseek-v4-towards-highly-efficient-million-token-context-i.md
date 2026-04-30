---
title: "DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence"
url: "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
source: "deepseek"
type: "paper"
authors: ["DeepSeek-AI"]
published: "2026-04-24"
ingested: "2026-04-29"
tags: ["research/model-release", "research/long-context", "research/moe", "research/inference", "research/reasoning", "type/paper", "access/public"]
---
# DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

## Why it matters
DeepSeek-V4 represents a major leap in efficient long-context intelligence with 1.6T parameters (49B active) and native 1M token context. The hybrid Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) architecture reduces single-token inference FLOPs to 27% and KV cache to 10% compared to V3.2 at 1M tokens. The Engram conditional memory module introduces a new sparsity axis for O(1) knowledge retrieval. Released under MIT license, it's the strongest open-source model for agentic coding, though DeepSeek acknowledges it trails US frontier models by 3-6 months.

## Abstract (original)
We present a preview version of DeepSeek-V4 series, including two strong Mixture-of-Experts (MoE) language models — DeepSeek-V4-Pro with 1.6T parameters (49B activated) and DeepSeek-V4-Flash with 284B parameters (13B activated) — both supporting a context length of one million tokens. DeepSeek-V4 series incorporate several key upgrades in architecture and optimization: Hybrid Attention Architecture combining Compressed Sparse Attention and Heavily Compressed Attention, Manifold-Constrained Hyper-Connections for training stability, and native FP4/FP8 mixed precision training.

## Source
[https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

## Full text
[[2026-04-29-deepseek-v4-towards-highly-efficient-million-token-context-i.full]] (extracted: html-extracted)
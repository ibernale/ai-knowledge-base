---
title: "DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence"
url: https://arxiv.org/abs/2604.17800
source: arxiv
type: paper
authors: ["DeepSeek-AI"]
published: 2026-04-24
ingested: 2026-04-29
tags: ["long-context", "inference", "moe", "model-release"]
---

# DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

## Why it matters
DeepSeek-V4 introduces a hybrid attention architecture (Compressed Sparse Attention + Heavily Compressed Attention) that reduces inference FLOPs to 27% and KV cache to 10% of V3.2 at 1M context. The 1.6T-parameter Pro model (49B active) and 284B Flash model (13B active) are open-sourced under MIT license. Architectural innovations include Manifold-Constrained Hyper-Connections and FP4+FP8 mixed precision training. Performance trails GPT-5.4 and Gemini-3.1-Pro by 3-6 months per DeepSeek's own assessment, but dominates open-source benchmarks. First major model validated on Huawei Ascend NPUs alongside NVIDIA GPUs.

## Abstract (original)
We present a preview version of DeepSeek-V4 series, including two strong Mixture-of-Experts (MoE) language models — DeepSeek-V4-Pro with 1.6T parameters (49B activated) and DeepSeek-V4-Flash with 284B parameters (13B activated) — both supporting a context length of one million tokens. DeepSeek-V4 series incorporate several key upgrades in architecture and optimization: Hybrid Attention Architecture combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) to dramatically improve long-context efficiency. In the 1M-token context setting, DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2.

## Source
[https://arxiv.org/abs/2604.17800](https://arxiv.org/abs/2604.17800)

## Full text
[[2026-04-29-deepseek-v4-towards-highly-efficient-million-token-context-i.full]] (extracted: ar5iv)
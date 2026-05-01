---
title: "Kwai Summary Attention: Efficient Long-Context Processing for LLMs"
url: https://arxiv.org/abs/2604.26800
source: arxiv
type: paper
authors: ["Chenglong Chu", "Guorui Zhou", "Guowang Zhang", "Kuaishou OneRec Team"]
published: "2026-04-27"
ingested: "2026-05-01"
tags: ["research/long-context", "research/inference", "type/paper", "access/public"]
---

# Kwai Summary Attention: Efficient Long-Context Processing for LLMs

## Why it matters
Kuaishou's OneRec team introduces Kwai Summary Attention (KSA), a hybrid attention mechanism that compresses historical context into learnable summary tokens. Achieves 5.81-point gain over full attention on RULER-128K benchmark while reducing KV cache cost to O(N/k) and decreasing KV cache memory by 2.5x at 128K context length. A practical solution for production recommendation systems needing efficient long-context retrieval—directly applicable to real-world LLM serving infrastructure.

## Abstract (original)
Kwai Summary Attention (KSA) is a hybrid attention mechanism that compresses historical context into learnable summary tokens to enable efficient processing of long input sequences in Large Language Models. This approach reduces KV cache cost to O(N/k) and enhances long-context retrieval, achieving a 5.81-point gain over full attention on RULER-128K and decreasing KV cache memory by 2.5 times at 128K context length.

## Source
[https://arxiv.org/abs/2604.26800](https://arxiv.org/abs/2604.26800)

## Full text
[[2026-05-01-kwai-summary-attention-efficient-long-context-processing-for.full]] (extracted: ar5iv)
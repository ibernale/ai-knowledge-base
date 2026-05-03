---
title: "Learning Rate Transfer in Normalized Transformers (\u03bdGPT)"
url: https://arxiv.org/abs/2604.27077
source: arxiv
type: paper
authors: ["Boris Shigida", "Boris Hanin", "Andrey Gromov"]
published: "2026-04-29"
ingested: "2026-05-03"
tags: ["research/pretraining", "research/inference", "type/paper", "access/public"]
---

# Learning Rate Transfer in Normalized Transformers (νGPT)

## Why it matters
This paper introduces νGPT, a novel parameterization for Normalized Transformers (nGPT) that enables robust learning rate transfer across model width, depth, and token horizon. While nGPT promised training speedups of 4-20x, it lacked hyperparameter transfer capabilities. νGPT addresses this by using alignment exponents to modify μP-style hyperparameter scaling, significantly reducing the computational burden of hyperparameter tuning for large-scale models. For practitioners training transformers at scale, this provides principled guidance for scaling experiments without expensive hyperparameter searches.

## Abstract (original)
The Normalized Transformer, or nGPT achieves impressive training speedups and does not require weight decay or learning rate warmup. However, despite having hyperparameters that explicitly scale with model size, we observe that nGPT does not exhibit learning rate transfer across model dimension and token horizon. To rectify this, we combine numerical experiments with a principled use of alignment exponents to revisit and modify the μP approach to hyperparameter transfer.

## Source
[https://arxiv.org/abs/2604.27077](https://arxiv.org/abs/2604.27077)

## Full text
[[2026-05-03-learning-rate-transfer-in-normalized-transformers-gpt.full]] (extracted: ar5iv)
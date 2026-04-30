---
title: "SFT Bug Invalidates Multiple Mixed-Policy Optimization Papers"
url: "https://arxiv.org/abs/2604.18500"
source: "arxiv"
type: "paper"
authors: ["Alexis Limozin", "Eduard Durech", "Torsten Hoefler"]
published: "2026-04-26"
ingested: "2026-04-29"
tags: ["research/posttraining", "research/reasoning", "research/evals", "type/paper", "access/public"]
---
# SFT Bug Invalidates Multiple Mixed-Policy Optimization Papers

## Why it matters
This paper identifies critical bugs in DeepSpeed's CPU-offloaded optimizer and OpenRLHF's loss aggregation that suppressed SFT performance in multiple downstream frameworks (TRL, Llama-Factory). Once corrected, standard SFT-then-RL pipeline surpasses every published mixed-policy method by +3.8 points on math benchmarks (Qwen2.5-Math-7B) and +22.2 points in other settings. A significant methodological finding that invalidates baselines in numerous recent papers on LLM reasoning training.

## Abstract (original)
Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline. We show that numerous recently published research papers rely on a faulty baseline caused by two distinct bugs: a CPU-offloaded optimizer bug in DeepSpeed that silently drops intermediate micro-batches during gradient accumulation, and a loss aggregation bug in OpenRLHF that incorrectly weights per-mini-batch losses.

## Source
[https://arxiv.org/abs/2604.18500](https://arxiv.org/abs/2604.18500)

## Full text
[[2026-04-29-sft-bug-invalidates-multiple-mixed-policy-optimization-paper.full]] (extracted: ar5iv)
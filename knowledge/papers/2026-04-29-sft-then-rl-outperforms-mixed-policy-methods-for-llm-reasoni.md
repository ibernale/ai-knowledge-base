---
title: "SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning"
url: "https://arxiv.org/abs/2604.23747"
source: "arxiv"
type: "paper"
authors: ["Alexis Limozin", "Eduard Durech", "Torsten Hoefler"]
published: "2026-04-26"
ingested: "2026-04-29"
tags: ["research/posttraining", "research/reasoning", "research/benchmarks", "type/paper", "access/public"]
---
# SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning

## Why it matters
This paper identifies critical bugs in two widely-used RLHF frameworks (DeepSpeed and OpenRLHF) that have suppressed SFT baseline performance in numerous published papers. The CPU-offloaded optimizer bug in DeepSpeed silently drops micro-batches during gradient accumulation, affecting TRL, OpenRLHF, and Llama-Factory. Once corrected, standard SFT-then-RL outperforms all published mixed-policy methods by +3.8 points on math benchmarks with Qwen2.5-Math-7B and +22.2 points with Llama-3.1-8B. This is a significant methodological finding that may invalidate conclusions from multiple recent papers.

## Abstract (original)
Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline. We show that numerous recently published research papers rely on a faulty baseline caused by two distinct bugs: a CPU-offloaded optimizer bug in DeepSpeed that silently drops intermediate micro-batches during gradient accumulation (affecting multiple downstream frameworks including TRL, OpenRLHF and Llama-Factory), and a loss aggregation bug in OpenRLHF that incorrectly weights per-mini-batch losses.

## Source
[https://arxiv.org/abs/2604.23747](https://arxiv.org/abs/2604.23747)

## Full text
[[2026-04-29-sft-then-rl-outperforms-mixed-policy-methods-for-llm-reasoni.full]] (extracted: ar5iv)
---
title: "SFT-then-RL Pipeline Bugs: DeepSpeed Optimizer Bug and OpenRLHF Loss Aggregation Bug"
url: "https://www.alphaxiv.org"
source: "arxiv"
type: "paper"
authors: ["Alexis Limozin", "Eduard Durech", "Torsten Hoefler"]
published: "2026-04-26"
ingested: "2026-04-29"
tags: ["research/posttraining", "research/reasoning", "research/benchmarks", "type/paper", "access/public"]
---
# SFT-then-RL Pipeline Bugs: DeepSpeed Optimizer Bug and OpenRLHF Loss Aggregation Bug

## Why it matters
This paper reveals that numerous published mixed-policy optimization methods for LLM reasoning rely on faulty baselines due to two bugs: a DeepSpeed CPU-offloaded optimizer bug that drops micro-batches during gradient accumulation (affecting TRL, OpenRLHF, Llama-Factory), and an OpenRLHF loss aggregation bug. Once corrected, the standard SFT-then-RL pipeline surpasses published mixed-policy methods by +3.8 points on math benchmarks with Qwen2.5-Math-7B. Critical for anyone doing RLHF/post-training work.

## Abstract (original)
Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline. We show that numerous recently published research papers rely on a faulty baseline caused by two distinct bugs: a CPU-offloaded optimizer bug in DeepSpeed that silently drops intermediate micro-batches during gradient accumulation, and a loss aggregation bug in OpenRLHF.

## Source
[https://www.alphaxiv.org](https://www.alphaxiv.org)

## Full text
[[2026-04-29-sft-then-rl-pipeline-bugs-deepspeed-optimizer-bug-and-openrl.full]] (extracted: html-extracted)
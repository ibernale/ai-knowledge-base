---
title: "Decoupled DiLoCo: Resilient, Distributed AI Training at Scale"
url: "https://deepmind.google/blog/decoupled-diloco"
source: "deepmind"
type: "paper"
authors: ["Arthur Douillard", "Keith Rush", "Yani Donchev", "Zachary Charles", "et al."]
published: "2026-04-23"
ingested: "2026-04-28"
tags: ["research/pretraining", "research/hardware", "type/paper", "access/public"]
---
# Decoupled DiLoCo: Resilient, Distributed AI Training at Scale

## Why it matters
Google DeepMind introduces Decoupled DiLoCo, a distributed training architecture that enables LLM training across distant data centers with lower bandwidth and more hardware resiliency. By dividing training runs across decoupled compute islands with asynchronous data flow, the approach can mix different hardware generations (TPU v6e and v5p) in a single training run while matching ML performance of single-chip-type runs. This has major implications for training efficiency and infrastructure utilization at scale.

## Abstract (original)
Our new distributed architecture helps to train LLMs across distant data centers - with lower bandwidth and more hardware resiliency. Training a frontier AI model traditionally depends on a large, tightly coupled system in which identical chips must stay in near-perfect synchronization. This approach is highly effective for today's state-of-the-art models, but as we look toward future generations of scale, maintaining this level of synchronization across thousands of chips becomes a significant logistical challenge.

## Source
[https://deepmind.google/blog/decoupled-diloco](https://deepmind.google/blog/decoupled-diloco)

## Full text
[[2026-04-28-decoupled-diloco-resilient-distributed-ai-training-at-scale.full]] (extracted: html-extracted)
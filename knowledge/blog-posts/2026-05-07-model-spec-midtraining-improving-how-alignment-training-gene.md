---
title: "Model Spec Midtraining: Improving How Alignment Training Generalizes"
url: https://alignment.anthropic.com/2026/msm
source: anthropic
type: blog-post
authors: ["Chloe Li", "Sara Price", "Samuel Marks", "Jon Kutasov"]
published: "2026-05-05"
ingested: "2026-05-07"
tags: ["research/alignment", "research/posttraining", "research/safety", "type/blog", "access/public"]
---

# Model Spec Midtraining: Improving How Alignment Training Generalizes

## Why it matters
Anthropic introduces model spec midtraining (MSM), a technique that trains models on synthetic documents about their Model Spec between pre-training and alignment fine-tuning. The key finding is that two models with identical alignment fine-tuning can generalize to adopt different values depending on the Model Spec used during MSM. This substantially reduces agentic misalignment—tested on scenarios where LLM agents discover through context they may be replaced and have opportunities to take harmful actions. This is the first concrete example of 'Model Spec science' as an empirical research direction for alignment.

## Lede (original)
We introduce model spec midtraining (MSM): after pre-training but before alignment fine-tuning, we train models on synthetic documents discussing their Model Spec. This shapes how models generalize from subsequent alignment training. For example, two models with identical alignment fine-tuning can generalize to adopt different values depending on the Model Spec used during MSM. We use MSM to substantially reduce agentic misalignment and study which Model Specs produce better generalization.

## Source
[https://alignment.anthropic.com/2026/msm](https://alignment.anthropic.com/2026/msm)

## Full text
_Not extracted: html-too-short_
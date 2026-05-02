---
title: "Thinking with Visual Primitives"
url: https://github.com/deepseek-ai/Thinking-with-Visual-Primitives
source: other
type: paper
authors: ["DeepSeek-AI", "Peking University", "Tsinghua University"]
published: "2026-04-30"
ingested: "2026-05-02"
tags: ["research/multimodal", "research/reasoning", "type/paper", "access/public"]
---

# Thinking with Visual Primitives

## Why it matters
DeepSeek introduces a framework that addresses the 'Reference Gap' in multimodal reasoning by integrating visual primitives (points and bounding boxes) directly into the chain-of-thought. Built on DeepSeek-V4-Flash (284B params, 13B active), it achieves extreme visual token efficiency—only ~90 KV cache entries for 800x800 images vs ~870 for Claude Sonnet 4.6. Despite smaller size and fewer tokens, it matches or exceeds GPT-5.4, Claude-Sonnet-4.6, and Gemini-3-Flash on visual QA benchmarks. This demonstrates that precise spatial grounding can compensate for reduced visual token budgets.

## Abstract (original)
MLLMs frequently suffer from logical collapse in tasks involving complex spatial layouts or dense object interactions. We identify this failure as the Reference Gap: the inherent inability of language to precisely reference visual elements during reasoning. By interleaving spatial markers directly into the reasoning trajectory as minimal units of thought, we anchor abstract linguistic concepts to concrete physical coordinates.

## Source
[https://github.com/deepseek-ai/Thinking-with-Visual-Primitives](https://github.com/deepseek-ai/Thinking-with-Visual-Primitives)

## Full text
_Not extracted: http-status-404_
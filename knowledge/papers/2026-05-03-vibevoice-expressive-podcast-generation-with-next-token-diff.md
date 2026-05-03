---
title: "VibeVoice: Expressive Podcast Generation with Next-Token Diffusion"
url: https://arxiv.org/abs/2508.19205
source: microsoft
type: paper
authors: ["Li Dong", "et al."]
published: "2026-05-01"
ingested: "2026-05-03"
tags: ["research/multimodal", "research/inference", "type/paper", "access/public"]
---

# VibeVoice: Expressive Podcast Generation with Next-Token Diffusion

## Why it matters
VibeVoice represents a breakthrough in long-form, multi-speaker speech synthesis. The system uses a novel continuous speech tokenizer operating at 7.5 Hz (80x more efficient than Encodec) combined with next-token diffusion to synthesize up to 90 minutes of conversational audio with 4 distinct speakers. Accepted as an Oral at ICLR 2026, this addresses key TTS pain points around speaker consistency, natural turn-taking, and scalability. Microsoft has open-sourced both TTS and ASR models (VibeVoice-ASR handles 60-minute audio in a single pass), making this immediately usable for podcast generation, audiobook production, and conversational AI applications.

## Abstract (original)
Generating long-form, multi-speaker conversational audio like podcasts poses significant challenges for traditional Text-to-Speech (TTS) systems, particularly in scalability, speaker consistency, and natural turn-taking. We present VibeVoice, a novel model designed to synthesize expressive, long-form speech with multiple speakers in a zero-shot manner. A core component of our approach is the continuous speech tokenizers operating at an ultra-low frame rate of 7.5. This tokenizer effectively preserves audio fidelity while significantly boosting computational efficiency for processing long sequences.

## Source
[https://arxiv.org/abs/2508.19205](https://arxiv.org/abs/2508.19205)

## Full text
[[2026-05-03-vibevoice-expressive-podcast-generation-with-next-token-diff.full]] (extracted: pdf-extracted)
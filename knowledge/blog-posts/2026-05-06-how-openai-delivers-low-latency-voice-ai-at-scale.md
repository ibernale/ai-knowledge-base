---
title: "How OpenAI delivers low-latency voice AI at scale"
url: https://openai.com/index/delivering-low-latency-voice-ai-at-scale
source: openai
type: blog-post
authors: ["Yi Zhang", "William McDonald"]
published: "2026-05-04"
ingested: "2026-05-06"
tags: ["research/inference", "research/multimodal", "type/blog", "access/public"]
---

# How OpenAI delivers low-latency voice AI at scale

## Why it matters
OpenAI's engineering team reveals how they rebuilt their WebRTC stack to serve 900+ million weekly active users with real-time voice AI. The split relay-plus-transceiver architecture addresses three constraints that collide at scale: one-port-per-session media termination, stateful ICE/DTLS session ownership, and first-hop latency. This is infrastructure engineering at frontier scale, showing the gap between 'model works' and 'product feels natural.' Practitioners building voice agents will find the architectural decisions—choosing WebRTC termination points, handling session state, and routing packets to inference—directly applicable.

## Lede (original)
Voice AI only feels natural if conversation moves at the speed of speech. When the network gets in the way, people hear it immediately as awkward pauses, clipped interruptions, or delayed barge-in. At OpenAI's scale, that translates into three concrete requirements: global reach, fast connection setup, and low and stable media round-trip time.

## Source
[https://openai.com/index/delivering-low-latency-voice-ai-at-scale](https://openai.com/index/delivering-low-latency-voice-ai-at-scale)

## Full text
_Not extracted: http-status-403_
---
title: "Introducing Dynamic Workflows: durable execution that follows the tenant"
url: https://blog.cloudflare.com/dynamic-workflows
source: other
type: blog-post
authors: ["Dan Lapid", "Luís Duarte"]
published: "2026-05-01"
ingested: "2026-05-04"
tags: ["research/agents", "research/inference", "type/blog", "access/public"]
---

# Introducing Dynamic Workflows: durable execution that follows the tenant

## Why it matters
Cloudflare's Dynamic Workflows enables AI platforms to route durable execution to tenant-provided code at runtime, critical for multi-tenant agentic systems. Built on Dynamic Workers (V8 isolates with ~100x faster startup than containers), it allows agents to generate and execute multi-step plans that survive restarts and await human approval. The library unlocks patterns where SaaS platforms let each customer define their own automation with near-zero idle cost—a significant infrastructure primitive for production agent deployment.

## Lede (original)
Dynamic Workflows is a library that lets you route durable execution to tenant-provided code on the fly. Built on Dynamic Workers, it enables platforms to serve millions of unique workflows at near-zero idle cost. This unlocks patterns where the Workflow code itself is dynamic—SaaS platforms where each tenant defines their own automation, AI agent frameworks where agents generate and execute multi-step plans at runtime.

## Source
[https://blog.cloudflare.com/dynamic-workflows](https://blog.cloudflare.com/dynamic-workflows)

## Full text
_Not extracted: html-too-short_
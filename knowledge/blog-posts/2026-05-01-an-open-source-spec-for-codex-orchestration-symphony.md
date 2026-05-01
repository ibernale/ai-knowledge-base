---
title: "An open-source spec for Codex orchestration: Symphony"
url: https://openai.com/index/open-source-codex-orchestration-symphony
source: openai
type: blog-post
authors: ["OpenAI Engineering"]
published: "2026-04-27"
ingested: "2026-05-01"
tags: ["research/agents", "research/agentic-coding", "research/tool-use", "type/blog", "access/public"]
---

# An open-source spec for Codex orchestration: Symphony

## Why it matters
OpenAI open-sources Symphony, an agent orchestrator spec (Apache 2.0) that turns Linear-style issue trackers into control planes for Codex coding agents. Every open task spawns a dedicated agent workspace; Symphony monitors, restarts on stalls, and lands approved PRs automatically. Internal teams report 500% increases in landed PRs. The release signals OpenAI's vision for scaling agentic development: decoupling work from interactive sessions and making engineers managers of outcomes rather than supervisors of agents. Competes directly with Anthropic's Claude Code and GitHub Copilot's Jira integration.

## Lede (original)
Symphony is an agent orchestrator that turns a project-management board like Linear into a control plane for coding agents. Every open task gets an agent, agents run continuously, and humans review the results. This post explains how we created Symphony—resulting in a 500% increase in landed pull requests on some teams—and how to use it to turn your own issue tracker into an always-on agent orchestrator.

## Source
[https://openai.com/index/open-source-codex-orchestration-symphony](https://openai.com/index/open-source-codex-orchestration-symphony)

## Full text
_Not extracted: http-status-403_
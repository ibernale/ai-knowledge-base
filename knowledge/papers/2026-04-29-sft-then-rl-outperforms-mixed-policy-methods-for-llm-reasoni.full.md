---
title: "SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning (full text)"
url: https://arxiv.org/abs/2604.23747
source: arxiv
type: full-text
parent: "[[2026-04-29-sft-then-rl-outperforms-mixed-policy-methods-for-llm-reasoni]]"
ingested: 2026-04-29
extraction: ar5iv
---

# Computer Science > Machine Learning

[Submitted on 26 Apr 2026]

# Title:SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning

[View PDF](/pdf/2604.23747)

[HTML (experimental)](https://arxiv.org/html/2604.23747v1)

Abstract:Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline. We show that numerous recently published research papers rely on a faulty baseline caused by two distinct bugs: a CPU-offloaded optimizer bug in DeepSpeed that silently drops intermediate micro-batches during gradient accumulation (affecting multiple downstream frameworks including TRL, OpenRLHF and Llama-Factory), and a loss aggregation bug in OpenRLHF that incorrectly weights per-mini-batch losses. Together they suppress SFT performance, with the optimizer bug accounting for most of the gap and the loss aggregation bug contributing a smaller additional effect. Once corrected, the standard SFT-then-RL pipeline surpasses every published mixed-policy method we evaluate by +3.8 points on math benchmarks with Qwen2.5-Math-7B and by +22.2 points with Llama-3.1-8B. Even a truncated variant with just 50 RL steps outperforms mixed-policy methods on math benchmarks while using fewer FLOPs.

### Current browse context:

cs.LG

### References & Citations

Loading...

# Bibliographic and Citation Tools

Bibliographic Explorer

*(*[What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))
Connected Papers

*(*[What is Connected Papers?](https://www.connectedpapers.com/about))
Litmaps

*(*[What is Litmaps?](https://www.litmaps.co/))
scite Smart Citations

*(*[What are Smart Citations?](https://www.scite.ai/))# Code, Data and Media Associated with this Article

alphaXiv

*(*[What is alphaXiv?](https://alphaxiv.org/))
CatalyzeX Code Finder for Papers

*(*[What is CatalyzeX?](https://www.catalyzex.com))
DagsHub

*(*[What is DagsHub?](https://dagshub.com/))
Gotit.pub

*(*[What is GotitPub?](http://gotit.pub/faq))
Hugging Face

*(*[What is Huggingface?](https://huggingface.co/huggingface))
ScienceCast

*(*[What is ScienceCast?](https://sciencecast.org/welcome))# Demos

# Recommenders and Search Tools

Influence Flower

*(*[What are Influence Flowers?](https://influencemap.cmlab.dev/))
CORE Recommender

*(*[What is CORE?](https://core.ac.uk/services/recommender))
IArxiv Recommender

*(*[What is IArxiv?](https://iarxiv.org/about))# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [ Learn more about arXivLabs](https://info.arxiv.org/labs/index.html).
---
title: "SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection (full text)"
url: https://arxiv.org/abs/2605.02888
source: arxiv
type: full-text
parent: "[[2026-05-06-speckv-adaptive-speculative-decoding-with-compression-aware]]"
ingested: 2026-05-06
extraction: ar5iv
---

# Computer Science > Machine Learning

[Submitted on 4 May 2026 (

[v1](https://arxiv.org/abs/2605.02888v1)), last revised 5 May 2026 (this version, v2)]# Title:SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection

[View PDF](/pdf/2605.02888)

[HTML (experimental)](https://arxiv.org/html/2605.02888v2)

Abstract:Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length $\gamma$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed $\gamma$ (typically 4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present SpecKV, a lightweight adaptive controller that selects $\gamma$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4 task categories, 4 speculation lengths, and 3 compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal $\gamma$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation $\approx$ 0.56). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0% improvement over the fixed-$\gamma=4$ baseline with only 0.34 ms overhead per decision (<0.5% of step time). The improvement is statistically significant (p < 0.001, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.

## Submission history

From: Shikhar Shukla [[view email](/show-email/70edfa99/2605.02888)]

**Mon, 4 May 2026 17:55:05 UTC (640 KB)**

[[v1]](/abs/2605.02888v1)**[v2]**Tue, 5 May 2026 12:57:37 UTC (640 KB)

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
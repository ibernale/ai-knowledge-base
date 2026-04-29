---
title: "Context Engineering for AI Agents in Open-Source Software (full text)"
url: https://arxiv.org/abs/2604.18200
source: arxiv
type: full-text
parent: "[[2026-04-29-context-engineering-for-ai-agents-in-open-source-software]]"
ingested: 2026-04-29
extraction: ar5iv
---

# Computer Science > Information Retrieval

[Submitted on 20 Apr 2026]

# Title:Multi-LLM Token Filtering and Routing for Sequential Recommendation

[View PDF](/pdf/2604.18200)

[HTML (experimental)](https://arxiv.org/html/2604.18200v1)

Abstract:Large language models (LLMs) have recently shown promise in recommendation by providing rich semantic knowledge. While most existing approaches rely on external textual corpora to align LLMs with recommender systems, we revisit a more fundamental yet underexplored question: Can recommendation benefit from LLM token embeddings alone without textual input? Through a systematic empirical study, we show that directly injecting token embeddings from a single LLM into sequential recommenders leads to unstable or limited gains, due to semantic misalignment, insufficient task adaptation, and the restricted coverage of individual LLMs. To address these challenges, we propose MLTFR, a Multi-LLM Token Filtering and Routing framework for corpus-free sequential recommendation. MLTFR follows an interaction-guided LLM knowledge integration paradigm, where task-relevant token embeddings are selected via user-guided token filtering to suppress noisy and irrelevant vocabulary signals. To overcome the limitations of single-LLM representations, MLTFR integrates multiple LLM token spaces through a Mixture-of-Experts architecture, with a Fisher-weighted semantic consensus expert to balance heterogeneous experts and prevent domination during training. By jointly filtering informative tokens and aggregating complementary semantic knowledge across multiple LLMs, MLTFR enables stable and effective utilization of LLM token embeddings without textual inputs or backbone modification. Extensive experiments demonstrate that MLTFR consistently outperforms state-of-the-art sequential recommendation baselines and existing alignment methods. Our code is available at:[this https URL].

### Additional Features

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

*(*[What is CORE?](https://core.ac.uk/services/recommender))# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [ Learn more about arXivLabs](https://info.arxiv.org/labs/index.html).
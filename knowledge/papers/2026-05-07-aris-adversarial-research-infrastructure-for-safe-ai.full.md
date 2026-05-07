---
title: "ARIS: Adversarial Research Infrastructure for Safe AI (full text)"
url: https://arxiv.org/abs/2605.04000
source: arxiv
type: full-text
parent: "[[2026-05-07-aris-adversarial-research-infrastructure-for-safe-ai]]"
ingested: 2026-05-07
extraction: ar5iv
---

# Computer Science > Software Engineering

[Submitted on 5 May 2026 (

[v1](https://arxiv.org/abs/2605.04000v1)), last revised 6 May 2026 (this version, v2)]# Title:Mitigating False Positives in Static Memory Safety Analysis of Rust Programs via Reinforcement Learning

[View PDF](/pdf/2605.04000)

[HTML (experimental)](https://arxiv.org/html/2605.04000v2)

Abstract:Static analysis tools are essential for ensuring memory safety in Rust programs, particularly as Rust gains adoption in safety-critical domains. However, existing tools such as Rudra and MirChecker suffer from high false positive rates, which diminish developer trust, increase manual review effort, and may obscure genuine vulnerabilities. This paper presents a novel reinforcement learning (RL)-based approach for automatically classifying and suppressing spurious warnings in static memory safety analysis for Rust. To achieve this, we design an RL agent that learns a warning suppression policy by extracting contextual features from Rust's Mid-level Intermediate Representation (MIR) and optimizing its decisions through interaction with static analysis outputs. To improve decision quality, we integrate dynamic validation via cargo-fuzz as an auxiliary feedback mechanism, allowing the agent to selectively validate suspicious warnings through targeted fuzz testing. Our evaluation shows that the proposed approach significantly outperforms state-of-the-art LLM-based baselines, achieving 65.2% accuracy and an F1 score of 0.659, an improvement of 17.1% over the best LLM baseline. With a recall of 74.6%, our method successfully identifies nearly three-quarters of true bugs while substantially reducing false positives, improving precision from 25.6% in raw Rudra output to 59.0%. Incorporating dynamic fuzzing further boosts performance, yielding additional improvements of 10.7 percentage points in accuracy and 8.6 percentage points in F1 score over the RL-only variant. Overall, our work demonstrates that combining reinforcement learning with hybrid static-dynamic analysis can substantially reduce false positives and improve the practical usability of memory safety verification tools for Rust.

## Submission history

From: Akilesh P [[view email](/show-email/8b5ea07a/2605.04000)]

**Tue, 5 May 2026 17:21:40 UTC (428 KB)**

[[v1]](/abs/2605.04000v1)**[v2]**Wed, 6 May 2026 04:54:08 UTC (428 KB)

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
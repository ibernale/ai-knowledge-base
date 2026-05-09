---
title: "Agent Context Files: First Large-Scale Empirical Study of 2,303 Files from 1,925 Repositories (full text)"
url: https://arxiv.org/abs/2605.05000
source: arxiv
type: full-text
parent: "[[2026-05-09-agent-context-files-first-large-scale-empirical-study-of-230]]"
ingested: 2026-05-09
extraction: ar5iv
---

# Computer Science > Cryptography and Security

[Submitted on 6 May 2026]

# Title:Agentic Vulnerability Reasoning on Windows COM Binaries

[View PDF](/pdf/2605.05000)

[HTML (experimental)](https://arxiv.org/html/2605.05000v1)

Abstract:Windows Component Object Model (COM) services run with elevated privileges and are widely accessible to authenticated users, making race conditions in these binaries a critical surface for local privilege escalation. We present SLYP, an end-to-end agentic pipeline that discovers race condition vulnerabilities in COM binaries and generates debugger-verified proof-of-concept (PoC) code. SLYP exposes binary exploration, COM inspection, and dynamic debugging as reusable tool interfaces, giving agents the static context, COM activation metadata, and debugger feedback needed to move from vulnerability discovery to verified PoC generation. On a benchmark of 20 COM objects covering 40 vulnerability cases, SLYP achieves 0.973 F1, outperforming production coding agents by up to 0.208 F1 and the state-of-the-art static analyzer by 3.3x in bug discovery. For PoC generation, production coding agents in their default setup (without our COM inspection and dynamic debugging tools) verify essentially no cases on either frontier model, whereas SLYP's interactive toolsets enable it to autonomously synthesize working PoCs for 67.5% of cases on the strongest configuration. Deployed on production Windows services, SLYP discovers 28 previously unknown vulnerabilities across nine COM services, all confirmed by the Microsoft Security Response Center (MSRC) with 16 CVEs assigned and $140,000 in bounties. Furthermore, SLYP is designed with generalizable binary analysis and debugging interfaces, making it readily applicable to other commercial off-the-shelf (COTS) binaries beyond Windows COM services.

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
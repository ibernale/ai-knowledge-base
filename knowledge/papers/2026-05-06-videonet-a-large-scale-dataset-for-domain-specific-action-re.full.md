---
title: "VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition (full text)"
url: https://arxiv.org/abs/2605.02834
source: arxiv
type: full-text
parent: "[[2026-05-06-videonet-a-large-scale-dataset-for-domain-specific-action-re]]"
ingested: 2026-05-06
extraction: ar5iv
---

# Computer Science > Computer Vision and Pattern Recognition

[Submitted on 4 May 2026 (

[v1](https://arxiv.org/abs/2605.02834v1)), last revised 5 May 2026 (this version, v2)]# Title:VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition

[View PDF](/pdf/2605.02834)

[HTML (experimental)](https://arxiv.org/html/2605.02834v2)

Abstract:Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.

## Submission history

From: Tanush Yadav [[view email](/show-email/8d699da9/2605.02834)]

**Mon, 4 May 2026 17:11:16 UTC (28,315 KB)**

[[v1]](/abs/2605.02834v1)**[v2]**Tue, 5 May 2026 09:59:53 UTC (28,314 KB)

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
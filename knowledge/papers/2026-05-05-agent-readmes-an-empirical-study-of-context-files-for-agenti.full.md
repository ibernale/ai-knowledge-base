---
title: "Agent READMEs: An Empirical Study of Context Files for Agentic Coding (full text)"
url: https://arxiv.org/abs/2605.01234
source: arxiv
type: full-text
parent: "[[2026-05-05-agent-readmes-an-empirical-study-of-context-files-for-agenti]]"
ingested: 2026-05-05
extraction: ar5iv
---

# Computer Science > Computer Vision and Pattern Recognition

[Submitted on 2 May 2026]

# Title:TT4D: A Pipeline and Dataset for Table Tennis 4D Reconstruction From Monocular Videos

[View PDF](/pdf/2605.01234)

[HTML (experimental)](https://arxiv.org/html/2605.01234v1)

Abstract:We present TT4D, a large-scale, high-fidelity table tennis dataset. It provides $140+$ hours of reconstructed singles and doubles gameplay from monocular broadcast videos, featuring multimodal annotations like high-quality camera calibrations, precise 3D ball positions, ball spin, time segmentation, and 3D human meshes over time. This rich data provides a new foundation for virtual replay, in-depth player analysis, and robot learning. The dataset's combination of scale and precision is achieved through a novel reconstruction pipeline. Prior methods first partition a game sequence into individual shot segments based on the 2D ball track, and only then attempt reconstruction. However, 2D-based time segmentation collapses under occlusion and varied camera viewpoints, preventing reliable reconstruction. We invert this paradigm by first lifting the entire unsegmented 2D ball track to 3D through a learned lifting network. This 3D trajectory then allows us to reliably perform time segmentation. The learned lifting network also infers the ball's spin, handles unreliable ball detections, and successfully reconstructs the ball trajectory in cases of high occlusion. This lift-first design is necessary, as our pipeline is the only method capable of reconstructing table tennis gameplay from general-view broadcast monocular videos. We demonstrate the dataset's fidelity through two downstream tasks: estimating the racket's pose \& velocity at impact, and training a generative model of competitive rallies.

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
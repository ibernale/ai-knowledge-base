---
title: "AlphaEvolve: Gemini-powered coding agent scaling impact across fields (full text)"
url: https://deepmind.google/blog/alphaevolve-impact
source: deepmind
type: full-text
parent: "[[2026-05-09-alphaevolve-gemini-powered-coding-agent-scaling-impact-acros]]"
ingested: 2026-05-09
extraction: html-extracted
---

## Improving AI infrastructure

AlphaEvolve has graduated from pilot testing to becoming a core component of our infrastructure. AlphaEvolve has been used as a regular tool to optimize the design of the next generation of [TPUs](https://cloud.google.com/tpu?e=48754805). It also helped discover more efficient [cache replacement policies](https://arxiv.org/abs/2602.22425), achieving in two days what previously required a concerted, human-intensive effort spanning months.

“*AlphaEvolve began optimizing the lowest levels of hardware powering our AI stacks. It proposed a circuit design so counterintuitive yet efficient that it was integrated directly into the silicon of our next-generation TPUs. This is the latest example of TPU brains helping design next-generation TPU bodies.*” — Jeff Dean, Chief Scientist, Google DeepMind and Google Research

AlphaEvolve improved the efficiency of [Google Spanner](https://cloud.google.com/spanner) by refining its [Log-Structured Merge-tree](https://en.wikipedia.org/wiki/Log-structured_merge-tree) compaction heuristics. This optimization reduced 'write amplification'—the ratio of data written to storage versus the original request—by 20%. It also provided insights for [new compiler optimization strategies](https://arxiv.org/abs/2601.21096) that reduced the storage footprint of software by nearly 9%.

## Scaling commercial applications

[Together with Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-on-google-cloud?e=48754805), we are now bringing the power of AlphaEvolve to a variety of commercial enterprises across industries.

- In financial services,
[Klarna](https://engineering.klarna.com/beyond-prompting-how-algorithmic-evolution-doubled-our-training-speed-8f874af3080d) used the system to optimize one of its largest transformer models — doubling its training speed whilst improving model quality. - In semiconductor manufacturing,
[Substrate](https://substrate.com/information-to-atoms) applied AlphaEvolve to its computational lithography framework, achieving a multi-fold increase in runtime speed, enabling them to run significantly larger simulations of advanced semiconductors. - In logistics,
[FM Logistic](https://cloud.google.com/blog/products/ai-machine-learning/how-fm-logistic-tackled-the-traveling-salesman-problem-at-warehouse-scale-with-alphaevolve?e=48754805) used the technology to optimize complex routing challenges like the Traveling Salesman Problem, finding 10.4% improvement in routing efficiency over the previous heavily optimized solutions — saving over 15,000 kilometers of distance travelled annually. - In advertising and marketing,
[WPP](https://thelab.wppresolve.com/blog/cracking-the-code-of-campaign-success-with-googles-alphaevolve-agent) used AlphaEvolve to refine AI model components, navigating complex, high-dimensional campaign data and achieving 10% accuracy gains over their competitive manual model optimizations. - In computational material and life sciences,
[Schrödinger](https://www.schrodinger.com/company/about/?_gl=1*ius61h*_up*MQ..*_gs*MQ..&gclid=Cj0KCQjwkYLPBhC3ARIsAIyHi3Rm2kCs3x5O0g-fhVotOLr0BJ07wW4PlIYjQx79xY_sGz1si0Uyd2QaAhv8EALw_wcB&gbraid=0AAAAAoiC9DPuTTJLOACkELqcLzvfQOPqG) applied AlphaEvolve to achieve a roughly 4x speedup in both Machine Learned Force Fields (MLFF) training and inference.

*“AlphaEvolve allows us to explore larger chemical spaces faster and more efficiently than ever before. Faster MLFF inference carries real business impact, shortening R&D cycles in drug discovery, catalyst design, and materials development, and enabling companies to screen molecular candidates in days rather than months.”* — Gabriel Marques, Technical Lead of Machine Learning at Schrödinger.

## The future of AlphaEvolve

The past year shows how AlphaEvolve is rapidly becoming a versatile, general-purpose system. It is demonstrating that the next breakthroughs will be driven by algorithms that can learn, evolve and optimize themselves. As we look ahead, we are excited to expand these capabilities, and bring the power of this technology to an even broader set of external challenges.

## Acknowledgements

AlphaEvolve was developed by Matej Balog, Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, and Pushmeet Kohli. This research was developed as part of a broader initiative focused on using AI for algorithm discovery. Following the initial development, Alexey Cherepanov, Anindya Basu, Becky Evangelakos, Jamie Smith, and Mario Pinto joined the team to scale AlphaEvolve’s impact.

Adam Connors, Alex Bäuerle, Anna Trostanetski, Fernanda Viegas, Gabi Cardoso, Jonathan Caton, Lucas Dixon, Mariana Felix, Martin Wattenberg, Matin Akhlaghinia, Richard Green, Yosuke Ushigome, and Yunhan Xu collaborated with our team to develop the AlphaEvolve UI, with support from many others.

Anant Nawalgaria, Diego Ballesteros, Gemma Jennings, Jakob Oesinghaus, Kartik Sanu, Laurynas Tamulevičius, Nicolas Stroppa, Nishta Dhawan, Oliver Hilsenbeck, Reah Miyara, Skander Hannachi, Tom Beyer, and Vishal Agarwal collaborated with our team to develop the AlphaEvolve API and engage with Google Cloud customers, with support from many others.

We gratefully acknowledge our collaborators for leading applications of AlphaEvolve on critical problems and contributing to this report: Aaron Wenger, Abhradeep Guha Thakurta, Akanksha Jain, Alex Vitvitskyi, Amir Yazdan Bakhsh, Andrew Carroll, Aranyak Mehta, Arthur Conmy, Ansh Nagda, Davide Paglieri, Eric Perim Martins, Hassler Thurston, Hongzheng Chen, Jack Mason, János Kramár, Jeremy Ratcliff, Jessica Sapick, Johannes Bausch, Jonathan Katz, Kevin Miller, Kim Stachenfeld, Mark Kurzeja, Mircea Trofin, Myriam Khan, Nero Geng, Pablo Samuel Castro, Petar Veličković, Pi-Chuan Chang, Prabhakar Raghavan, Raghav Gupta, Rohin Shah, Sasha Vezhnevets, Sébastien Lahaie, Sergio Guadarrama, Shravya Shetty, Shruthi Gorantala, Terence Tao, Todd Lipcon, Tom O'Brien, Vinod Nair, Ziyue Wang, Zun Li, among many other users of AlphaEvolve.

Finally, we thank our leadership for their guidance and support: Amin Vahdat, Ankur Jain, Demis Hassabis, Jeff Dean, Parthasarathy Ranganathan, Pushmeet Kohli, Saurabh Tiwary, and Sundar Pichai. We also extend our gratitude to our partner teams across Google DeepMind, Google Cloud, Google Labs, Google Research, and other product areas for enabling the applications and products powered by AlphaEvolve.
---
title: "Decoupled DiLoCo: Resilient, Distributed AI Training at Scale (full text)"
url: https://deepmind.google/blog/decoupled-diloco
source: deepmind
type: full-text
parent: "[[2026-04-28-decoupled-diloco-resilient-distributed-ai-training-at-scale]]"
ingested: 2026-04-28
extraction: html-extracted
---

# Decoupled DiLoCo: A new frontier for resilient, distributed AI training

Our new distributed architecture helps to train LLMs across distant data centers - with lower bandwidth and more hardware resiliency.

Training a frontier AI model traditionally depends on a large, tightly coupled system in which identical chips must stay in near-perfect synchronization. This approach is highly effective for today’s state-of-the-art models, but as we look toward future generations of scale, maintaining this level of synchronization across thousands of chips becomes a significant logistical challenge.

Today, in a [new paper](https://arxiv.org/abs/2604.21428v1) we are excited to share a new approach to this problem, called Decoupled DiLoCo (Distributed Low-Communication). By dividing large training runs across decoupled “islands” of compute, with asynchronous data flowing between them, this architecture isolates local disruptions so that other parts of the system can keep learning efficiently.

The result is a more resilient and flexible way to train advanced models across globally distributed data centers. And crucially, Decoupled DiLoCo does not suffer the communication delays that made previous distributed methods like Data-Parallel impractical at global scale.

As frontier models continue to grow in scale and complexity, we’re exploring diverse approaches to train models across more compute, locations and varied hardware.

## Developing more fault-tolerant asynchronous training at scale

Decoupled DiLoCo builds on two earlier advances: [Pathways](https://blog.google/innovation-and-ai/products/introducing-pathways-next-generation-ai-architecture/), which introduced a distributed AI system based on asynchronous data flow, and [DiLoCo](https://arxiv.org/abs/2311.08105), which dramatically reduced the bandwidth required between distributed data centers, making it practical to train large language models across distant locations.

Decoupled DiLoCo brings those ideas together to train AI models more flexibly at scale. Built on top of Pathways, it enables asynchronous training across separate islands of compute (known as learner units) so that a chip failure in one area doesn’t interrupt the progress of the others.

This infrastructure is also self-healing. In testing, we used a method called “chaos engineering” to introduce artificial hardware failures during training runs. Decoupled DiLoCo continued the training process after the loss of entire learner units, and then seamlessly reintegrated them when they came back online.

Testing Decoupled DiLoCo with Gemma 4 models demonstrated that, when hardware fails, the system maintains greater availability of learning clusters than more traditional training methods — while ultimately delivering the same benchmarked level of machine learning (ML) performance.

Decoupled DiLoCo is not only more resilient to failures, but is also practical for executing production-level, fully distributed pre-training. We successfully trained a 12 billion parameter model across four separate U.S. regions using 2-5 Gbps of wide-area networking (a level relatively achievable using existing internet connectivity between datacenter facilities, rather than requiring new custom network infrastructure between facilities). Notably, the system achieved this training result more than 20 times faster than conventional synchronization methods. This is because our system incorporates required communication into longer periods of computation, avoiding the "blocking" bottlenecks where one part of the system must wait for another.

## Driving the evolution of AI training infrastructure

At Google, we take a full-stack approach to AI training, spanning hardware, software infrastructure and research. Increasingly, gains are coming from rethinking how these layers fit together.

Decoupled DiLoCo is one example. By enabling training jobs at internet-scale bandwidth, it can tap any unused compute wherever it sits, turning stranded resources into useful capacity.

Beyond efficiency and resilience, this training paradigm also unlocks the ability to mix different hardware generations, such as TPU v6e and TPU v5p, in a single training run. This approach not only extends the useful life of existing hardware, but also increases the total compute available for model training. In our experiments, chips from different generations running at different speeds still matched the ML performance of single-chip-type training runs, ensuring that even older hardware can meaningfully accelerate AI training.

What’s more, because new generations of hardware don’t arrive everywhere all at once, being able to train across generations can alleviate recurring logistical and capacity bottlenecks.

As we push the frontiers of AI infrastructure today, we’re continuing to explore approaches to resilient systems needed to unlock the next generation of AI.

## Acknowledgements

This work was done by a team of members across Google DeepMind and Google Research.

The leads and core contributors behind Decoupled DiLoCo are Arthur Douillard, Keith Rush, Yani Donchev, Zachary Charles, Ayush Dubey, Blake Woodworth, Ionel Gog, Josef Dean, Nova Fallen, Zachary Garrett. Operational support was done by Nate Keating and Jenny Bishop.

We are also grateful for the additional support and advising from Jeff Dean, Marc’Aurelio Ranzato, Raia Hadsell, Arthur Szlam, Edouard Yvinec, Henry Prior, Paul Barham, Michael Isard, Daniel Ramage, Brendan McMahan, Chase Hensel, and Zoltan Egyed.
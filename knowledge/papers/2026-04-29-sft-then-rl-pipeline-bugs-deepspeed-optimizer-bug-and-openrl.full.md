---
title: "SFT-then-RL Pipeline Bugs: DeepSpeed Optimizer Bug and OpenRLHF Loss Aggregation Bug (full text)"
url: https://www.alphaxiv.org
source: arxiv
type: full-text
parent: "[[2026-04-29-sft-then-rl-pipeline-bugs-deepspeed-optimizer-bug-and-openrl]]"
ingested: 2026-04-29
extraction: html-extracted
---

What are the most popular benchmarks for math reasoning?

A collaborative group of researchers presents a synthetic argument for the emergence of 'learning mechanics,' a scientific theory of deep learning that aims to explain and predict neural network behavior through mathematical, first-principles calculations. It consolidates diverse theoretical and empirical evidence, suggesting a path toward a unified understanding of phenomena like scaling laws, training dynamics, and universal representations.

DeepSeek-V4 introduces models that efficiently process contexts up to one million tokens through a hybrid attention architecture and optimized infrastructure, reducing single-token inference FLOPs by up to 73% and KV cache usage by up to 90% compared to its predecessor. The models achieve competitive performance across reasoning, coding, and long-context tasks, establishing new open-source benchmarks.

Meta AI researchers introduced Tuna-2, a unified multimodal model that performs visual understanding and generation directly from pixel embeddings, eliminating the need for pretrained vision encoders. This encoder-free architecture achieved competitive performance across nine VQA benchmarks and state-of-the-art results among native UMMs for image generation and editing tasks.

Researchers at IBM Research AI developed Abstract Chain-of-Thought (Abstract-CoT), a post-training framework that replaces lengthy verbalized rationales with a short sequence of discrete, abstract tokens. This method achieves comparable or improved performance over traditional Chain-of-Thought while reducing reasoning token usage by up to 12 times across various benchmarks and language models.

Researchers from Zhejiang University and Microsoft Research developed World-R1, a reinforcement learning framework that imbues existing text-to-video foundation models with robust 3D geometric consistency without architectural modifications. This approach led to a PSNR improvement of up to 10.23dB over baseline models and a 92% user preference for geometric consistency in generated videos.

This research introduces a "levels × laws" taxonomy for agentic world modeling, categorizing capabilities into Predictor, Simulator, and Evolver levels and world types into physical, digital, social, and scientific regimes. The framework unifies disparate research efforts, providing criteria for decision-usable simulation and autonomous model revision, and highlights the shift from passive prediction to active, adaptable environmental understanding for AI agents.

Kuaishou's OneRec Team developed Kwai Summary Attention (KSA), a hybrid attention mechanism that compresses historical context into learnable summary tokens to enable efficient processing of long input sequences in Large Language Models. This approach reduces KV cache cost to O(N/k) and enhances long-context retrieval, achieving a 5.81-point gain over full attention on RULER-128K and decreasing KV cache memory by 2.5 times at 128K context length.

Joy Future Academy introduced EgoLive, an extensive open-source egocentric dataset featuring 1,680 hours of high-resolution stereo video and multi-modal annotations from 65,866 real-world human task episodes. This dataset provides 6-DoF motion tracking, semantic segmentation, 3D scene reconstruction, and hierarchical language descriptions to foster generalizable robot manipulation models, demonstrating broader semantic coverage and more accurate depth estimation compared to prior work.

ClawMark is presented as a benchmark designed to evaluate language model agents functioning as persistent coworkers across multi-day, multi-turn workflows in dynamic environments requiring raw multimodal evidence. Evaluation of frontier models on ClawMark revealed that while partial progress is achievable, strict task success rates remain low, with models struggling particularly with detecting unannounced environmental changes and committing backend writebacks.

Google's Vision Banana model, created by instruction-tuning a pretrained image generator, demonstrates that generative models can achieve state-of-the-art performance in both visual understanding and generation. It surpasses existing specialized models on tasks like semantic segmentation and metric depth estimation while maintaining high-quality image generation capabilities.

The Massachusetts Institute of Technology developed Hyperloop Transformers, an architecture integrating looped Transformers with strategic hyper-connections to achieve parameter efficiency. This approach yielded approximately 50% fewer parameters than depth-matched baselines while achieving lower perplexity, improved downstream task performance, and strong robustness to INT4 quantization.

This research introduces MMEB-V3, a comprehensive benchmark spanning text, image, video, and audio modalities, and OmniSET, a diagnostic framework designed to evaluate omni-modality embedding models' ability to interpret and enforce explicit modality constraints. Experiments demonstrate that current models frequently fail to reliably retrieve content in the instructed target modality, often exhibiting strong modality biases and insufficient, misaligned instruction-induced embedding shifts.

This research re-evaluates mixed-policy optimization methods for large language model (LLM) reasoning by identifying and correcting bugs in widely used supervised fine-tuning (SFT) training frameworks. It demonstrates that a correctly implemented SFT-then-reinforcement learning (RL) pipeline consistently outperforms current mixed-policy approaches on mathematical reasoning benchmarks, often with greater computational efficiency.

Researchers from Alibaba Group and The Chinese University of Hong Kong introduced Temporal Curriculum On-Policy Distillation (TCOD), a framework designed to stabilize on-policy distillation for multi-turn autonomous agents by controlling trajectory depth. TCOD improved success rates by up to 15.71 points over vanilla OPD on ALFWorld and reduced total training time by nearly 32%.

Omni, a unified multimodal model, introduces "Context Unrolling" as an emergent capability for explicit reasoning across heterogeneous modal representations. This mechanism dynamically constructs and composes task-relevant contexts, leading to improved fidelity across multimodal understanding, generation, and 3D geometry tasks.

Alibaba Group researchers developed AgenticQwen, a series of smaller language models, for industrial-scale tool use by integrating multi-round reinforcement learning with dual data flywheels for continuous, diverse data generation. These models exhibit enhanced agentic capabilities, achieving performance comparable to larger models while offering improved cost-performance efficiency for real-world applications.

The GazeVLA framework introduces a Vision-Language-Intention-Action (VLIA) model that learns human intention, specifically through gaze, to enhance robotic manipulation capabilities. This model achieved a 22% relative improvement over prior methods in out-of-distribution simulated tasks and doubled success rates in real-world fine-grained manipulation by effectively transferring human intention.

M-VLA, an architectural paradigm, enables generalized Vision-Language Models to serve as robust backbones for robotic manipulation by freezing their core parameters, thereby preserving semantic understanding and avoiding catastrophic forgetting. It introduces Mixture of Layers (MoL) for feature extraction and a Meta Skill Module (MSM) for efficient trajectory learning, achieving an average 95.3% success rate in simulation and superior generalization to novel instructions and objects in real-world tasks with significantly fewer parameters (0.3B) than fine-tuned alternatives.

Researchers formalized Maryna Viazovska's solution to the 8-dimensional sphere packing problem within the Lean Theorem Prover, completing a "sorry-free" proof with substantial assistance from the 'Gauss' autoformalization model. This effort provided a machine-checked verification of the E₈ lattice packing's optimality and insights into human-AI collaboration in advanced mathematics.

A Meta-CoT framework for image editing uses hierarchical Chain-of-Thought decomposition and a consistency reward to enhance understanding granularity and generalization. It improved performance by 13.1% on a 21-task benchmark and 19.7% on the ImgEdit benchmark compared to a Bagel baseline.
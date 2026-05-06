---
title: "RF-DETR: Neural Architecture Search for Real-Time Detection Transformers (full text)"
url: https://arxiv.org/abs/2511.09554
source: arxiv
type: full-text
parent: "[[2026-05-06-rf-detr-neural-architecture-search-for-real-time-detection-t]]"
ingested: 2026-05-06
extraction: ar5iv
---

# RF-DETR: Neural Architecture Search for Real-Time Detection Transformers

###### Abstract

Open-vocabulary detectors achieve impressive performance on COCO, but often fail to generalize to real-world datasets with out-of-distribution classes not typically found in their pre-training. Rather than simply fine-tuning a heavy-weight vision-language model (VLM) for new domains, we introduce RF-DETR, a light-weight specialist detection transformer that discovers accuracy-latency Pareto curves for any target dataset with weight-sharing neural architecture search (NAS). Our approach fine-tunes a pre-trained base network on a target dataset and evaluates thousands of network configurations with different accuracy-latency tradeoffs without re-training. Further, we revisit the “tunable knobs” for NAS to improve the transferability of DETRs to diverse target domains. Notably, RF-DETR significantly improves on prior state-of-the-art real-time methods on COCO and Roboflow100-VL. RF-DETR (nano) achieves 48.0 AP on COCO, beating D-FINE (nano) by 5.3 AP at similar latency, and RF-DETR (2x-large) outperforms GroundingDINO (tiny) by 1.2 AP on Roboflow100-VL while running as fast. To the best of our knowledge, RF-DETR (2x-large) is the first real-time detector to surpass 60 AP on COCO. Our code is available on [GitHub](https://github.com/roboflow/rf-detr).

## 1 Introduction

Object detection is a fundamental problem in computer vision that has matured in recent years (felzenszwalb2009object; lin2014coco; ren2015faster). Open-vocabulary detectors like GroundingDINO (liu2023grounding) and YOLO-World (Cheng2024YOLOWorld) achieve remarkable zero-shot performance on common categories like car, truck, and pedestrian. However, state-of-the-art vision-language models (VLMs) still struggle to generalize to out-of-distribution classes, tasks and imaging modalities not typically found in their pre-training (robicheaux2025roboflow100vl). Fine-tuning VLMs on a target dataset significantly improves in-domain performance at the cost of runtime efficiency (due to heavy-weight text encoders) and open-vocabulary generalization. In contrast, specialist (i.e., closed-vocabulary) object detectors like D-FINE (peng2024dfine) and RT-DETR (zhao2024rtdetr) achieve real-time inference, but underperform fined-tuned VLMs like GroundingDINO. In this paper, we modernize specialist detectors by combining internet-scale pre-training with real-time architectures to achieve state-of-the-art performance and fast inference.

Are Specialist Detectors Over-Optimized for COCO? Sustained progress in object detection can be largely attributed to standardized benchmarks like PASCAL VOC (pascalvoc) and COCO (lin2014coco). However, we find that recent specialist detectors implicitly overfit to COCO at the cost of real-world performance using bespoke model architectures, learning rate schedulers, and augmentation schedulers. Notably, state-of-the-art object detectors like YOLOv8 (yolov8) generalize poorly to real-world datasets with significantly different data distributions from COCO (e.g., number of objects per image, number of classes, and dataset size). To address these limitations, we present RF-DETR, a scheduler-free approach that leverages internet-scale pre-training to generalize to real-world data distributions. To better specialize our model for diverse hardware platforms and dataset characteristics, we revisit neural architecture search (NAS) in the context of end-to-end object detection and segmentation.

Rethinking Neural Architecture Search (NAS) for DETRs. NAS discovers accuracy-latency tradeoffs by exploring architectural variants within a pre-defined search space. NAS has been previously studied in the context of image classification (tan2019efficientnet; cai2019ofa) and for model sub-components like detector backbones tan2020efficientdet and FPNs ghiasi2019fpn. Unlike prior work, we explore end-to-end weight-sharing NAS for object detection and segmentation. Our key insight, inspired by OFA (cai2019ofa), is that we can vary model inputs like image resolution, and architectural components like patch size during training. Further, weight-sharing NAS allows us to modify inference configurations like the number of decoder layers and query tokens to specialize our strong base model without fine-tuning. We evaluate all model configurations with grid search on a validation set. Importantly, our approach does not evaluate the search space until the base model has been fully-trained on the target dataset. As a result, all possible sub-nets (i.e., model configurations within the search space) achieve strong performance without further fine-tuning, significantly reducing the computational cost of optimizing for new hardware. Interestingly, we find that sub-nets not explicitly seen during training still achieve high performance, suggesting that RF-DETR can generalize to unseen architectures (cf. [H](#A8)). Extending RF-DETR for segmentation is also relatively straightforward and only requires adding a lightweight instance segmentation head. We denote this model as RF-DETR-Seg. Notably, this allows us to also leverage end-to-end weight-sharing NAS to discover Pareto optimal architectures for real-time instance segmentation.

Standardizing Latency Evaluation. We evaluate our approach on COCO (lin2014coco) and Roboflow100-VL (RF100-VL) (robicheaux2025roboflow100vl) and achieve state-of-the-art performance among real-time detectors. RF-DETR (nano) outperforms D-FINE (nano) by 5% AP on COCO at comparable run-times, and RF-DETR (2x-lage) beats GroundingDINO (tiny) on RF100-VL at a fraction of the runtime. RF-DETR-Seg (nano) outperforms YOLOv11-Seg (x-large) on COCO while running 4 as fast. However, comparing RF-DETR’s latency with prior work remains challenging because reported latency evaluation varies significantly between papers. Notably, each new model re-benchmarks the latency of prior work for fair comparison on their hardware. For example, D-FINE’s reported latency evaluation of LW-DETR (chen2024lw) is 25% faster than originally reported. We identify that this lack of reproducibility can be primarily attributed to GPU power throttling during inference. We find that buffering between forward passes limits power over-draw and standardizes latency evaluation (cf. Table [1](#S4.T1)).

Contributions. We present three major contributions. First, we introduce RF-DETR, a family of scheduler-free NAS-based detection and segmentation models that outperform prior state-of-the-art on RF100-VL (robicheaux2025roboflow100vl) and real-time methods with latencies 40 ms on COCO (lin2014coco)(cf. Fig. [1](#S1.F1)). To the best of our knowledge, RF-DETR is the first real-time detector to exceed 60 mAP on COCO. Next, we explore the “tunable-knobs” for weight-sharing NAS to improve accuracy-latency tradeoffs for end-to-end object detection (cf. Fig. [3](#S3.F3)). Notably, our use of a weight-sharing NAS allows us to leverage large-scale pre-training and effectively transfer to small datasets (cf. Tab. [4](#S4.T4)). Lastly, we revisit current benchmarking protocols for measuring latency and propose a simple standardized procedure to improve reproducibility.

## 2 Related Works

Neural Architecture Search (NAS) automatically identifies families of model architectures with different accuracy-latency tradeoffs (zoph2016neural; zoph2018learning; real2019regularized; cai2018efficient). Early NAS approaches (zoph2016neural; real2019regularized) focused primarily on maximizing accuracy, with little consideration for efficiency. As a result, discovered architectures (e.g., NASNet and AmoebaNet) were often computationally expensive. More recent hardware-aware NAS methods (cai2018proxylessnas; tan2019mnasnet; wu2019fbnet) address this limitation by incorporating hardware feedback directly into the search process. However, these methods must repeat the search and training process for each new hardware platform. In contrast, OFA (cai2019ofa) proposes a weight-sharing NAS that decouples training and search by simultaneously optimizing thousands of sub-nets with different accuracy-latency tradeoffs. Contemporary methods typically evaluate NAS for object detection by simply replacing standard backbones with NAS backbones in existing detection frameworks. Unlike prior work, we directly optimize end-to-end object detection accuracy to find Pareto optimal accuracy-latency tradeoffs for any target dataset.

Real-Time Object Detectors are of significant interest for safety-critical and interactive applications. Historically, two-stage detectors like Mask-RCNN (he2017mask) and Hybrid Task Cascade (chen2019hybrid) achieved state-of-the-art performance at the cost of latency, while single-stage detectors like YOLO (redmon2016you) and SSD (liu2016ssd) traded accuracy for state-of-the-art runtime. However, modern detectors (zhao2024rtdetr) reexamine this accuracy-latency tradeoff, simultaneously improving on both axes. Recent YOLO variants innovate on architecture, data augmentation, and training techniques (redmon2016you; wang2023yolov7; wang2024yolov9; yolov8; yolov11) to improve performance while maintaining fast inference. Despite their efficiency, most YOLO models rely on non-maximum suppression (NMS), which introduces additional latency. In contrast, DETR (carion2020end) removes hand-crafted components like NMS and anchor boxes. However, early DETR variants (zhu2020deformable; zhang2022dino; meng2021conditional; liu2022dab) achieved strong accuracy at the cost of runtime, limiting their use in real-time applications. Recent works such as RT-DETR (zhao2024rtdetr) and LW-DETR (chen2024lw) have successfully adapted high performance DETRs for real-time applications.

Vision-Language Models are trained on large-scale, weakly supervised image-text pairs from the web. Such internet-scale pre-training is a key enabler for open-vocabulary object detection (liu2023grounding; Cheng2024YOLOWorld). GLIP (li2021grounded) frames detection as phrase grounding with a single text query, while Detic (zhou2022detecting) boosts long-tail detection using ImageNet-level supervision (russakovsky2015imagenet). MQ-Det (xu2024multi) extends GLIP with a learnable module that enables multi-modal prompting. Recent VLMs demonstrate strong zero-shot performance and are often applied as “black-box” models in diverse downstream tasks (ma2023long; pmlr-v205-peri23a; khurana2024shelf; sal2024eccv; takmaz2025cal). However, robicheaux2025roboflow100vl find that such models perform poorly when evaluated on categories not typically found in their pre-training, requiring further fine-tuning. In addition, many vision-language models are prohibitively slow, making them difficult to use for real-time tasks. In contrast, RF-DETR combines the fast inference of real-time detectors with the internet-scale priors of VLMs to achieve state-of-the-art performance on RF100-VL and at all latencies 40 ms on COCO.

## 3 RF-DETR: Weight-Sharing NAS With Foundation Models

In this section, we describe the architecture of our base model (cf. Fig. [2](#S3.F2)) and present the “tunable knobs” of our weight-sharing NAS (cf. Fig. [3](#S3.F3)). Further, we highlight the limitations of hand-designed learning-rate and augmentation schedulers, and advocate for a scheduler-free approach.

Incorporating Internet-Scale Priors. RF-DETR modernizes LW-DETR (chen2024lw) by simplifying its architecture and training procedure to improve generalization to diverse target domains. First, we replace LW-DETR’s CAEv2 (zhang2022cae) backbone with DINOv2 (oquab2023dinov2). We find that initializing our backbone with DINOv2’s pre-trained weights significantly improves detection accuracy on small datasets. Notably, CAEv2’s encoder has 10 layers with a patch size of 16, while DINOv2’s encoder has 12 layers. Our DINOv2 backbone has more layers and is slower than CAEv2, but we make up for this latency using NAS (discussed next). Lastly, we facilitate training on consumer-grade GPUs via gradient accumulation by using layer norm instead of batch norm in the multi-scale projector.

Real-Time Instance Segmentation. Inspired by li2023maskdino, we add a lightweight instance segmentation head to jointly predict high quality segmentation masks. Our segmentation head bilinearly interpolates the output of the encoder and learns a lightweight projector to generate a pixel embedding map. Specifically, we upsample the same low-resolution feature map for the detection and segmentation heads to ensure that it contains relevant spatial information. Unlike MaskDINO (li2023maskdino), we do not incorporate multi-scale backbone features in our segmentation head to minimize latency. Lastly, we compute the dot product of all projected query token embeddings (at the output of each decoder layer transformed by a FFN) with the pixel embedding map to generate segmentation masks. Interestingly, we can interpret these pixel embeddings as segmentation prototypes bolya2019yolact. Motivated by LW-DETR’s observation that pre-training improves DETRs, we pre-train RF-DETR-Seg on Objects-365 (objects365) psuedo-labeled with SAM2 (ravi2024sam2) instance masks.

End-to-End Neural Architecture Search. Our weight-sharing NAS evaluates thousands of model configurations with different input image resolutions, patch sizes, window attention blocks, decoder layers, and query tokens. At every training iteration, we uniformly sample a random model configuration and perform a gradient update. This allows our model to efficiently train thousands of sub-nets in parallel, similar to ensemble learning with dropout (dropout). We find that this weight-sharing NAS approach also serves as a regularizer during training, effectively performing “architecture augmentation”. To the best of our knowledge, RF-DETR is the first end-to-end weight-sharing NAS applied to object detection and segmentation. We describe each component below.

-
•
Patch Size. Smaller patches lead to higher accuracy at greater computational cost. We adopt a FlexiVIT-style (beyer2023flexivit) transformation to interpolate between patch sizes during training.

-
•
Number of Decoder Layers. Similar to recent DETRs (peng2024dfine; zhao2024rtdetr), we apply a regression loss to the output of all decoder layers during training. Therefore, we can drop any (or all) decoder blocks during inference. Interestingly, removing the entire decoder during inference effectively turns RF-DETR into a single-stage detector. Notably, truncating the decoder also shrinks the size of the segmentation branch, allowing for greater control over segmentation latency.

-
•
Number of Query Tokens. Query tokens learn spatial priors for bounding box regression and segmentation. We drop query tokens (ordered by the maximum sigmoid of the corresponding class logit per token at the output of the encoder, see appendix

[B](#A2)) at test time to vary the maximum number of detections and reduce inference latency. The Pareto optimal number of query tokens implicitly encodes dataset statistics about the average number of objects per image in a target dataset. -
•
Image Resolution. Higher resolution improves small object detection performance, while lower resolution improves runtime. We pre-allocate positional embeddings corresponding to the largest image resolution divided by the smallest patch size and interpolate these embeddings for smaller resolutions or larger patch sizes.

-
•
Number of Windows per Windowed Attention Block. Window attention restricts self-attention to only process a fixed number of neighboring tokens. We can add or remove windows per block to balance accuracy, global information mixing, and computational efficiency.


At inference time, we pick a specific model configuration to select an operating point on the accuracy-latency Pareto curve. Importantly, different model configurations may have similar parameter counts but significantly different latencies. Similar to cai2019ofa, we see little benefit from fine-tuning the NAS-mined models on COCO (Appendix [F](#A6)), but note modest improvements from fine-tuning NAS-mined models on RF100-VL. We posit that RF-DETR on RF100-VL benefits from additional fine-tuning because the “architecture augmentation” regularization requires more than 100 epochs to converge on small datasets. Notably, prior weight-sharing NAS methods (cai2019ofa) train in stages and use a different learning-rate scheduler per-stage. However, such schedulers make strict assumptions about model convergence, which may not hold across diverse datasets.

Training Schedulers and Augmentations Bias Model Performance. State-of-the-art detectors often require careful hyper-parameter tuning to maximize performance on standard benchmarks. However, such bespoke training procedures implicitly bias the model towards certain dataset characteristics (e.g. number of images). Concurrent with DINOv3 (simeoni2025dinov3), we observe that cosine schedules assume a known (fixed) optimization horizon, which is impractical for diverse target datasets like those in RF100-VL. Data augmentations introduce similar biases by presuming prior knowledge of dataset properties. For example, prior work leverages aggressive data augmentation (e.g., VerticalFlip, RandomFlip, RandomResize, RandomCrop, YOLOXHSVRandomAug, and CachedMixUp) to increase effective dataset size. However, certain augmentations like VerticalFlip may negatively bias model predictions in safety-critical domains. For example, a person detector in a self-driving vehicle should not be trained with VerticalFlip to avoid false positive detections from reflections in puddles. Therefore, we limit augmentations to horizontal flips and random crops. Lastly, LW-DETR applies a per-image random resize augmentation, where each image is padded to match the largest image in the batch. As a result, most images have significant padding, which introduces window artifacts, and wastes computation on padded regions. In contrast, we resize images at the batch level to minimize the number of padded pixels per-batch and to ensure that all positional encoding resolutions are equally likely to be seen at train time.

## 4 Experiments

We evaluate RF-DETR on COCO and RF100-VL and demonstrate that our approach achieves state-of-the-art accuracy among all real-time methods. In addition, we identify inconsistencies in standard benchmarking protocols and present a simple standardized procedure to improve reproducibility. Following LW-DETR (chen2024lw), we group models of similar latency into the same size bucket rather than grouping based on parameter count.

Datasets and Metrics. We evaluate RF-DETR on COCO for fair comparison with prior work and on RF100-VL to evaluate generalization to real-world datasets with significantly different data distributions. Due to the diversity of RF100-VL’s 100 datasets, we posit that overall performance on this benchmark is a proxy for transferability to any target domain. We use pycocotools to report standard metrics like mean average precision (mAP) and provide breakdown analysis for AP50, AP75, APSmall, APMedium, and APLarge. Further, we evaluate efficiency by measuring GFLOPs, number of parameters, and inference latency on an NVIDIA T4 GPU with Tensor-RT 10.4 and CUDA 12.4.

[A](#A1)for more details.

| Method | Reported | Buffering (FP-32) | Buffering (FP-16) | |||
|---|---|---|---|---|---|---|
AP50:95 |
Latency (ms) | AP50:95 |
Latency (ms) | AP50:95 |
Latency (ms) | |
| YOLOv8 (M) | 50.2 | 5.86 | 49.3 | 14.8 | 47.3 | 5.4 |
| YOLOv11 (M) | 51.5 | 4.7 | 49.7 | 18.7 | 48.3 | 5.2 |
| RT-DETR (R18) | 49.0 | 4.61 | 49.0 | 12.2 | 49.0 | 4.4 |
| LW-DETR (M) | 52.5 | 5.6 | 52.6 | 26.8 | 52.6 | 4.4 |
| D-FINE (M) | 55.1 | 5.62 | 55.1 | 13.9 | 55.0 (0.5∗) |
5.4 |
| RF-DETR (M) | - | - | 54.8 | 20.5 | 54.7 | 4.4 |

Standardizing Latency Benchmarking. Despite its maturity, benchmarking object detectors remains inconsistent across prior work. For example, YOLO-based models often omit non-maximal suppression (NMS) when computing latency, leading to unfair comparisons with end-to-end detectors. Additionally, YOLO-based segmentation models measure the latency of generating prototype predictions instead of directly usable per-object masks (yolov11), leading to biased runtime measurements. Further, D-FINE’s reported latency evaluation of LW-DETR is 25% faster than reported by chen2024lwdetr. We observe that such differences can be attributed to detectable power throttling events, particularly when the GPU overheats (cf. Table [1](#S4.T1)). In contrast, simply pausing for 200ms between consecutive forward passes largely mitigates power throttling, yielding more stable latency measurements. Lastly, we find that prior work often reports latency using FP16 quantized models, but evaluates accuracy with FP32 models. However, naive quantization can significantly degrade performance (in some cases dropping performance to near 0 AP). To ensure fair comparison, we advocate reporting accuracy and latency with the same model artifact. We release our stand-alone benchmarking tool on [GitHub](https://github.com/roboflow/single_artifact_benchmarking).

[E](#A5)for L, XL, and Max variants of RF-DETR on COCO.

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| Real-Time Object Detection w/ NMS | ||||||||||
| YOLOv8 (yolov8) | N | 3.2M | 8.7 | 2.1 | 35.2 | 49.2 | 38.3 | 15.8 | 38.8 | 51.3 |
| YOLOv11 (yolov11) | N | 2.6M | 6.5 | 2.2 | 37.1 | 51.6 | 40.4 | 17.3 | 40.7 | 55.6 |
| YOLOv8 (yolov8) | S | 11.2M | 28.6 | 2.9 | 42.4 | 57.6 | 46.0 | 22.2 | 47.1 | 59.6 |
| YOLOv11 (yolov11) | S | 9.4M | 21.5 | 3.2 | 44.1 | 59.3 | 47.9 | 26.1 | 48.5 | 62.6 |
| YOLOv8 (yolov8) | M | 25.9M | 78.9 | 5.4 | 47.3 | 62.5 | 51.5 | 27.5 | 52.9 | 65.1 |
| YOLOv11 (yolov11) | M | 20.1M | 68.0 | 5.1 | 48.3 | 63.6 | 52.5 | 29.1 | 53.8 | 66.3 |
| Open-Vocabulary Object Detection (Fully-Supervised Fine-Tuning) | ||||||||||
| GroundingDINO (liu2023grounding) | T | 173.0M | 1008.3 | 427.6* | 58.2 | - | - | - | - | - |
| End-to-End Real-Time Object Detection | ||||||||||
| LW-DETR (chen2024lw) | T | 12.1M | 21.4 | 1.9 | 42.9 | 60.7 | 45.9 | 22.7 | 47.3 | 60.0 |
| D-FINE (peng2024dfine) | N | 3.8M | 7.3 | 2.1 | 42.7 | 60.2 | 45.4 | 22.9 | 46.6 | 62.1 |
| RF-DETR (Ours) | N | 30.5M | 31.9 | 2.3 | 48.0 | 67.0 | 51.4 | 25.2 | 53.5 | 70.0 |
| LW-DETR (chen2024lw) | S | 14.6M | 31.8 | 2.6 | 48.0 | 66.8 | 51.6 | 26.7 | 52.5 | 65.6 |
| D-FINE (peng2024dfine) | S | 10.2M | 25.2 | 3.5 | 50.6 | 67.6 | 55.0 | 32.6 | 54.6 | 66.6 |
| RF-DETR (Ours) | S | 32.1M | 59.8 | 3.5 | 52.9 | 71.9 | 57.0 | 32.0 | 58.3 | 73.0 |
| RT-DETR (zhao2024rtdetr) | R18 | 36.0M | 100.0 | 4.4 | 49.0 | 66.6 | 53.3 | 32.8 | 52.1 | 65.0 |
| LW-DETR (chen2024lw) | M | 28.2M | 83.9 | 4.4 | 52.6 | 72.0 | 56.6 | 32.5 | 57.6 | 70.5 |
| D-FINE (peng2024dfine) | M | 19.2M | 56.6 | 5.4 | 55.0 | 72.6 | 59.7 | 37.6 | 59.4 | 71.7 |
| RF-DETR (Ours) | M | 33.7M | 78.8 | 4.4 | 54.7 | 73.5 | 59.2 | 36.1 | 59.7 | 73.8 |
| RF-DETR (Ours) | 2XL | 126.9M | 438.4 | 17.2 | 60.1 | 78.5 | 65.5 | 43.2 | 64.9 | 76.2 |

Evaluating RF-DETR and RF-DETR-Seg on COCO. COCO (lin2014coco) is a flagship benchmark for object detection and instance segmentation. In Table [2](#S4.T2), we compare RF-DETR with leading real-time and open-vocabulary detectors. RF-DETR (nano) beats both D-FINE (nano) and LW-DETR (nano) by more than 5 AP. We see similar trends for small and medium sizes as well. Notably, RF-DETR also significantly outperforms YOLOv8 and YOLOv11. RF-DETR (nano) matches the performance of YOLOv8 and YOLOv11 (medium). We use mmdetection’s implementation of GroundingDINO and include their reported AP since they do not release a model artifact for GroundingDINO fine-tuned on COCO. We benchmark mmGroundingDINO’s parameter count, GFLOPS, and latency using the released open-vocabulary model. In Table [3](#S4.T3), we compare RF-DETR-Seg with real-time instance segmentation models. RF-DETR-Seg (nano) outperforms YOLOv8 and YOLOv11 at all sizes. Furthermore, RF-DETR-Seg (nano) beats FastInst by 5.4% while running almost ten times faster. Similarly, RF-DETR (x-large) surpasses GroundingDINO (tiny), and RF-DETR-Seg (large) outperforms MaskDINO (R50), at a fraction of their runtime.

[E](#A5)for L, XL, and Max variants of RF-DETR-Seg on COCO.

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| Real-Time Instance Segmentation w/ NMS | ||||||||||
| YOLOv8 (yolov8) | N | 3.4M | 12.6 | 3.5 | 28.3 | 45.6 | 29.8 | 9.3 | 31.3 | 44.3 |
| YOLOv11 (yolov11) | N | 2.9M | 10.4 | 3.6 | 30.0 | 47.8 | 31.5 | 10.0 | 33.4 | 47.7 |
| YOLOv8 (yolov8) | S | 11.8M | 42.6 | 4.2 | 34.0 | 53.8 | 36.0 | 13.6 | 38.5 | 52.2 |
| YOLOv11 (yolov11) | S | 10.1M | 35.5 | 4.6 | 35.0 | 55.4 | 37.1 | 15.3 | 39.7 | 53.9 |
| YOLOv8 (yolov8) | M | 27.3M | 110.2 | 7.0 | 37.3 | 58.2 | 39.9 | 16.7 | 43.0 | 56.1 |
| YOLOv11 (yolov11) | M | 22.4M | 123.3 | 6.9 | 38.5 | 60.0 | 40.9 | 18.0 | 44.3 | 57.6 |
| End-to-End Instance Segmentation | ||||||||||
| RF-DETR-Seg. (Ours) | N | 33.6M | 50.0 | 3.4 | 40.3 | 63.0 | 42.6 | 16.3 | 45.3 | 63.6 |
| RF-DETR-Seg. (Ours) | S | 33.7M | 70.6 | 4.4 | 43.1 | 66.2 | 45.9 | 21.9 | 48.5 | 64.1 |
| FastInst (he2023fastinst) | R50 | 29.7M | 99.7 | 39.6∗
|
34.9 | 56.0 | 36.2 | 13.3 | 38.0 | 56.8 |
| MaskDINO (li2023maskdino) | R50 | 52.1M | 586 | 242∗
|
46.3 | 69.0 | 50.7 | 26.1 | 49.3 | 66.1 |
| RF-DETR-Seg. (Ours) | M | 35.7M | 102.0 | 5.9 | 45.3 | 68.4 | 48.8 | 25.5 | 50.4 | 65.3 |
| RF-DETR (Ours) | 2XL | 38.6M | 435.3 | 21.8 | 49.9 | 73.1 | 54.5 | 33.9 | 54.1 | 65.7 |

Evaluating RF-DETR on RF100-VL. RF100-VL is a challenging detection benchmark composed of 100 diverse datasets. We report latencies, FLOPs, and accuracy averaged over all 100 datasets in Table [4](#S4.T4). Our results show that RF-DETR (2x-large) outperforms GroundingDINO and LLMDet while requiring only a fraction of their runtime. Interestingly, RT-DETR outperforms D-FINE (which is built on RT-DETR) at mAP50, indicating that D-FINE’s hyperparameters are potentially overoptimized for COCO. We note that RF-DETR benefits from scaling to larger backbone sizes (Appendix [E](#A5)). In contrast, YOLOv8 and YOLOv11 consistently underperform DETR-based detectors, and scaling these model families to larger sizes does not improve their performance on RF100-VL.

[E](#A5)for L, XL, and Max variants of RF-DETR on RF100-VL.

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| Real-Time Object Detectors w/ NMS | ||||||||||
| YOLOv8 (yolov8) | N | 3.2M | 8.7 | 2.6 | 55.0 | 81.1 | 59.5 | 4.8 | 44.1 | 48.0 |
| YOLOv11 (yolov11) | N | 2.6M | 6.5 | 3.0 | 55.5 | 81.3 | 60.3 | 4.7 | 44.4 | 49.2 |
| YOLOv8 (yolov8) | S | 11.2M | 28.6 | 3.1 | 56.3 | 82.0 | 60.9 | 6.1 | 45.6 | 48.6 |
| YOLOv11 (yolov11) | S | 9.4M | 21.5 | 3.3 | 56.4 | 82.5 | 61.3 | 6.5 | 45.5 | 48.5 |
| YOLOv8 (yolov8) | M | 25.9M | 78.9 | 5.4 | 56.5 | 82.3 | 60.9 | 6.4 | 45.7 | 48.6 |
| YOLOv11 (yolov11) | M | 20.1M | 68.0 | 5.1 | 57.0 | 82.5 | 61.9 | 7.3 | 46.1 | 48.6 |
| Open-Vocabulary Object-Detectors (Fully-Supervised Fine-Tuning) | ||||||||||
| GroundingDINO (liu2023grounding) | T | 173.0M | 1008.3 | 309.9∗
|
62.3 | 88.8 | 67.8 | 39.2 | 57.7 | 69.5 |
| LLMDet (fu2025llmdet) | T | 173.0M | 1008.3 | 308.4∗
|
62.3 | 88.3 | 67.8 | 39.1 | 57.6 | 70.3 |
| End-to-End Real-Time Object Detectors | ||||||||||
| LW-DETR (chen2024lw) | N | 12.1M | 21.4 | 1.9 | 57.1 | 84.7 | 61.5 | 31.2 | 51.8 | 65.8 |
| D-FINE (peng2024dfine) | N | 3.8M | 7.3 | 2.0 | 58.2 | 84.4 | 62.5 | 32.4 | 52.9 | 65.8 |
| RF-DETR (Ours) | N | 31.2M | 34.5 | 2.5 | 57.6 | 84.9 | 62.1 | 30.7 | 52.2 | 66.8 |
| RF-DETR w/ Fine-Tuning (Ours) | N | 31.2M | 34.5 | 2.5 | 58.7 | 85.6 | 63.5 | 32.4 | 52.7 | 67.0 |
| LW-DETR (chen2024lw) | S | 14.6M | 31.8 | 2.6 | 57.4 | 85.0 | 62.0 | 32.1 | 52.1 | 65.8 |
| D-FINE (peng2024dfine) | S | 10.2M | 25.2 | 3.5 | 60.3 | 85.3 | 65.4 | 36.6 | 56.0 | 68.4 |
| RF-DETR (Ours) | S | 33.5M | 62.4 | 3.7 | 60.7 | 87.0 | 66.0 | 35.4 | 55.4 | 69.6 |
| RF-DETR w/ Fine-Tuning (Ours) | S | 33.5M | 62.4 | 3.7 | 61.0 | 87.2 | 66.4 | 35.3 | 55.9 | 69.8 |
| RT-DETR (zhao2024rtdetr) | M | 36.0M | 100.0 | 4.3 | 59.6 | 85.7 | 64.6 | 36.4 | 54.6 | 67.3 |
| LW-DETR (chen2024lw) | M | 28.2M | 83.9 | 4.3 | 59.8 | 86.8 | 64.9 | 34.0 | 54.4 | 68.9 |
| D-FINE (peng2024dfine) | M | 19.2M | 56.6 | 5.6 | 60.6 | 85.5 | 65.8 | 36.0 | 56.6 | 67.5 |
| RF-DETR (Ours) | M | 33.5M | 86.7 | 4.6 | 61.5 | 87.7 | 67.0 | 36.44 | 56.5 | 69.8 |
| RF-DETR w/ Fine-Tuning (Ours) | M | 33.5M | 86.7 | 4.6 | 61.9 | 87.9 | 67.3 | 36.4 | 56.6 | 70.1 |
| RF-DETR (Ours) | 2XL | 123.5M | 410.2 | 15.6 | 63.3 | 88.9 | 69.0 | 38.7 | 58.2 | 71.6 |
| RF-DETR (Ours) w/ Fine-Tuning | 2XL | 123.5M | 410.2 | 15.6 | 63.5 | 89.0 | 69.2 | 38.9 | 58.3 | 71.7 |

Impact of Neural Architecture Search. We ablate the impact of weight-sharing NAS in Table [3](#S3.F3). We find that adopting a gentler set of hyperparameters compared to LW-DETR (e.g. larger batch size, lower learning rate, and replacing batch normalization with layer normalization) reduces performance over LW-DETR by 1.0%. Notably, replacing batch normalization with layer normalization hurts performance, but is necessary to train on consumer hardware. However, replacing LW-DETR’s CAEv2 backbone with DINOv2 improves performance by 2%. The lower learning rate, in particular, helps preserve DINOv2’s pre-trained knowledge, while additional epochs of Objects-365 pre-training further compensate for the slower optimization. Our final model with weight-sharing NAS improves over LW-DETR by 2% without increasing latency.

| Model | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
|---|---|---|---|---|---|---|---|---|---|
| LW-DETR (M) | 28.2M | 83.7 | 4.4 | 52.6 | 72.0 | 56.6 | 32.5 | 57.6 | 70.5 |
| + Gentler Hyperparameters | 28.2M | 83.7 | 4.4 | 51.6 | 71.1 | 55.5 | 31.7 | 56.4 | 69.4 |
| + DINOv2 Backbone | 32.3M | 78.2 | 4.7 | 53.6 | 72.7 | 58.0 | 34.3 | 58.3 | 72.4 |
| + Additional O365 Pre-Training | 32.3M | 78.2 | 4.7 | 54.3 | 73.4 | 58.8 | 35.8 | 59.2 | 72.3 |
| + Weight Sharing NAS | 32.3M | 78.2 | 4.7 | 54.6 | 73.4 | 59.3 | 36.3 | 59.3 | 72.1 |
| + Patch Size 1416, Res 560640 | 32.3M | 78.5 | 4.7 | 54.4 | 73.2 | 59.1 | 35.9 | 59.2 | 72.1 |
| + Image Resolution 640576 | 32.2M | 64.2 | 4.0 | 53.6 | 72.4 | 58.2 | 34.8 | 58.6 | 72.0 |
| + # Windows per Block 42 | 32.2M | 63.7 | 4.3 | 54.3 | 73.3 | 58.8 | 35.6 | 59.4 | 73.2 |
| + # Decoder Layers 34 | 33.7M | 64.8 | 4.4 | 54.6 | 73.5 | 59.1 | 36.0 | 59.8 | 73.7 |
| + # Query Tokens 300300 | 33.7M | 64.8 | 4.4 | 54.6 | 73.5 | 59.1 | 36.0 | 59.8 | 73.7 |

Impact of Backbone Architecture and Pre-Training. We study the impact of different backbone architectures in RF-DETR. We find that DINOv2 achieves the best performance, outperforming CAEv2 by 2%. Interestingly, despite having fewer parameters than SigLIPv2, SAM2’s Hiera-S backbone is considerably slower. This is in contrast with the Hiera-S claim that it is meaningfully faster than equivalently performant ViTs. However, Hiera does not explore latency in the context of kernels such as Flash Attention, which are highly optimized in compilers such as TensorRT. Additionally, existing foundation model families typically do not release lightweight ViT variants such as ViT-S or ViT-T, making it difficult to repurpose such models for real-time applications.

| LW-DETR (M) + Gentler Hyperparameters | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
|---|---|---|---|---|---|---|---|---|---|
| w/ CAEv2 ViT/S-16-Truncated Backbone | 28.3M | 83.7 | 4.4 | 52.3 | 71.4 | 56.3 | 32.3 | 56.4 | 70.0 |
| w/ DINOv2 ViT/S-14 Backbone | 32.3M | 78.2 | 4.7 | 54.3 | 73.4 | 58.8 | 35.8 | 59.2 | 72.3 |
w/ SigLIPv2 ViT/B-32 Backbone∗
|
105.1M | 81.6 | 4.8 | 50.4 | 70.4 | 53.7 | 28.0 | 55.3 | 73.0 |
w/ SAM2 Hiera-S Backbone∗
|
44.0M | 109.1 | 11.2 | 53.6 | 72.4 | 57.9 | 33.3 | 58.3 | 71.0 |

Rethinking Standard Accuracy Benchmarking Practices. Following prior work, we report all COCO results on the validation set. However, relying solely on the validation for both model selection and evaluation can lead to overfitting. For example, D-FINE (which builds on RT-DETR) conducts an extensive hyperparameter sweep on COCO’s validation set and reports its best model. However, evaluating this configuration on RF100-VL shows that D-FINE underperforms RT-DETR on the test set. In contrast, our method achieves state-of-the-art performance among all real-time detectors on RF100-VL and COCO, demonstrating the robustness of our weight-sharing NAS. In addition to evaluating on COCO, we advocate that future detectors should also evaluate on datasets with public validation and test splits like RF100-VL.

Limitations. Despite controlling for power throttling and GPU overheating during inference, our latency measurements still have a variance of up to 0.1ms due to the non-deterministic behavior of TensorRT during compilation. Specifically, TensorRT can introduce power throttling, which in turn affects the resulting engine and leads to random fluctuations in latency. Although the measurement of a given TensorRT engine is generally consistent, recompiling the same ONNX artifact can produce different latency results. Therefore, we only report latencies with one digit of precision after the decimal place.

## 5 Conclusion

In this paper, we introduce RF-DETR, a state-of-the-art NAS-based method for fine-tuning specialist end-to-end object detectors for target datasets and hardware platforms. Our approach outperforms prior state-of-the-art real-time methods on COCO and RF100-VL, improving upon D-FINE (nano) by 5% AP on COCO. Moreover, we highlight that current architectures, learning rate schedulers and augmentation schedulers are tailored to maximize performance on COCO, suggesting that the community should benchmark models on diverse, large-scale datasets to prevent implicit overfitting. Lastly, we highlight the high variance in latency benchmarking due to power throttling and propose a standardized protocol to improve reproducibility.

## Appendix A Implementation Details

Training Hyperparamters. RF-DETR extends LW-DETR (chen2024lw) for Neural Architecture Search. We highlight key differences in our training procedure below. First, we pseudo-label Objects365 (objects365) with SAM2 (ravi2024sam2) to allow us to pre-train the segmentation and detection heads on the same data. We use a learning rate of 1e-4 (LW-DETR uses 4e-4), and a batch size of 128 (LW-DETR uses the same). Similar to DINOv3 (simeoni2025dinov3), we use an EMA scheduler since this is necessary for EMA’s proper function. However, unlike DINOv3, we omit learning-rate warm-up. We clip all gradients greater than 0.1 and apply a per-layer multiplicative decay of 0.8 to preserve information (especially the earlier layers) in the DINOv2 backbone. We place our window attention blocks between layers {0, 1, 3, 4, 6, 7, 9, 10}, while LW-DETR places their window attention blocks between layers {0, 1, 3, 6, 7, 9}. Although we have the same number of windows, contiguous windowed blocks don’t require an additional reshape operation, making our implementation slightly more efficient. Further, we train with more multi-scale resolutions (0.5 to 1.5 scale) than LW-DETR (0.7 to 1.4 scale) to ensure that the augmentation is symmetric around the default scale. Notably, we add resolution as a “tunable knob” in our NAS search space, while LW-DETR uses it as a form of data augmentation. Our model training and inference code is available on [GitHub](https://github.com/roboflow/rf-detr).

Latency Evaluation. We ensure fair evaluation between models by measuring detection accuracy and latency using the same artifact. To further standardize inference, we employ CUDA graphs in TensorRT, which pre-queue all kernels rather than requiring the CPU to launch them serially during execution. This optimization can accelerate some networks depending on the number and type of kernels used by the model. We observe that RT-DETR, LW-DETR, and RF-DETR benefit from this optimization. Further, CUDA graphs place LW-DETR on the same latency-accuracy curve as D-FINE, since CUDA graphs speed up LW-DETR but do not benefit D-FINE. We release our stand-alone latency benchmarking tool on [GitHub](https://github.com/roboflow/single_artifact_benchmarking).

Pareto-Optimal Model Configurations on COCO. We present the Pareto-Optimal RF-DETR and RF-DETR-Seg configs in Tables [7](#A1.T7) and [8](#A1.T8). We highlight notable trends about RF-DETR’s Pareto-Optimal architectures in Appendix [H](#A8).

| Model Size | Resolution | Patch Size | Windows | Decoder Layers | Queries | Backbone |
|---|---|---|---|---|---|---|
| N | 384 | 16 | 2 | 2 | 300 | DINOv2-S |
| S | 512 | 16 | 2 | 3 | 300 | DINOv2-S |
| M | 576 | 16 | 2 | 4 | 300 | DINOv2-S |
| L | 704 | 16 | 2 | 4 | 300 | DINOv2-S |
| XL | 700 | 20 | 1 | 5 | 300 | DINOv2-B |
| 2XL | 880 | 20 | 2 | 5 | 300 | DINOv2-B |
| Max | 828 | 12 | 1 | 6 | 300 | DINOv2-B |

| Model Size | Resolution | Patch Size | Windows | Decoder Layers | Queries | Backbone |
|---|---|---|---|---|---|---|
| N | 312 | 12 | 1 | 4 | 100 | DINOv2-S |
| S | 384 | 12 | 2 | 4 | 100 | DINOv2-S |
| M | 432 | 12 | 2 | 5 | 200 | DINOv2-S |
| L | 504 | 12 | 2 | 5 | 300 | DINOv2-S |
| XL | 624 | 12 | 2 | 6 | 300 | DINOv2-S |
| 2XL | 768 | 12 | 2 | 6 | 300 | DINOv2-S |
| Max | 890 | 10 | 1 | 6 | 300 | DINOv2-S |

## Appendix B Ablation on Query Tokens and Decoder Layers

We train RF-DETR (nano) with 300 object queries, following standard practice for real-time DETR-based object detectors. However, many datasets contain fewer than 300 objects per image. Therefore, processing all 300 queries can be computationally wasteful. LW-DETR (tiny) demonstrates that training with fewer queries can improve the latency-accuracy tradeoff. Rather than deciding on the optimal number of queries apriori, we find that we can drop queries at test time without retraining by discarding the lowest-confidence queries ordered by the confidence of the corresponding token at the output of the encoder. As shown in Figure [4](#A2.F4), this yields meaningful latency-accuracy tradeoffs. In addition, prior work (zhao2024rtdetr) demonstrates that decoder layers can be pruned at test time, since each layer is supervised independently during training. We find that it is possible to remove *all* decoder layers, relying solely on the initial query proposals from the two-stage DETR pipeline. In this case, there is no cross-attention to the encoder states or self-attention between queries, leading to a substantial runtime reduction. The resulting model resembles a single-stage YOLO-style architecture without NMS. As shown in Figure [4](#A2.F4), eliminating the final decoder layer reduces latency by 10% with only a 2 mAP drop in performance.

## Appendix C Benchmarking FLOPs

We benchmark FLOPs for RF-DETR GroundingDINO, and YOLO-E with PyTorch’s [FlopCounterMode](https://github.com/pytorch/pytorch/blob/baee623691a38433d10843d5bb9bc0ef6a0feeef/torch/utils/flop_counter.py#L596). We find that FlopCounterMode closely reproduces FLOPs counts obtained with custom benchmarking tools for YOLOv11, D-FINE, and LW-DETR. In practice, we also find that it provides more reliable results than CalFLOPs (calflops). Notably, LW-DETR’s FLOPs count is roughly twice that of the originally reported result (cf. Table [9](#A3.T9)). We posit that this discrepancy can be attributed to LW-DETR reporting MACs instead of FLOPs. We rely on the officially reported FLOPs counts from YOLOv11, YOLOv8, D-FINE, and RT-DETR.

| Model | Size | Reported | CalFLOPs | FlopCounterMode |
|---|---|---|---|---|
| D-FINE | S | 25.2 M | 25.2 M | 25.5 M |
| LW-DETR | S | 16.6 M | 22.9 M | 31.8 M |
| YOLO11 | S | 21.5 M | 23.9 M | 21.6 M |

## Appendix D Impact of Class-Names on Open-Vocabulary Detectors

We evaluate the impact of fine-tuning open-vocabulary detectors like GroundingDINO with class names on RF100-VL in Table [10](#A4.T10). Intuitively, GroundingDINO’s vision-language pre-training is more useful when we prompt with class names (e.g. car, truck, bus) instead of class indices (e.g. 0, 1, 2). Using class names at finetune time therefore provides more information to the VLM about the underlying data than is available to non-VLM detectors, potentially leading to better downstream performance. However, we find that fine-tuning GroundingDINO on RF100-VL yields nearly identical performance in both cases, suggesting that naively fine-tuning the end-to-end model mitigates the benefits of open-vocabulary pre-training. Future should investigate ways of effectively fine-tuning VLMs to preserve foundational pre-training.

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
|---|---|---|---|---|---|---|---|---|---|---|
| RF100-VL | ||||||||||
| GroundingDINO (liu2023grounding) w/ Standard Class Names | T | 173.0M | 1008.3 | 309.9∗
|
62.3 | 88.8 | 67.8 | 39.2 | 57.7 | 69.5 |
| GroundingDINO (liu2023grounding) w/ Class Index Names | T | 173.0M | 1008.3 | 309.9∗
|
62.5 | 88.2 | 68.3 | 40.0 | 58.4 | 70.3 |

## Appendix E Benchmarking Larger Model Variants

Detectors like LW-DETR (chen2024lw) and D-FINE (peng2024dfine) hand-design larger variants to scale up a model family. In contrast, NAS-based architectures like RF-DETR automatically discover scaling strategies through grid-based search. We analyze two families of RF-DETR models derived from distinct scaling strategies: one based on a DINOv2-S backbone and another based on a DINOv2-B backbone. To evaluate how well each family scales, we compare their NAS-generated Pareto curves against those of D-FINE. Specifically, at each D-FINE size, we identify the RF-DETR variant with the same backbone that maximizes performance at a comparable latency. For example, when comparing to D-FINE (small), we select the RF-DETR model that offers the best accuracy without exceeding D-FINE (small)’s latency.

As shown in Table [11](#A5.T11), the DINOv2-S backbone family initially surpasses D-FINE in mAP@50:95 but fails to maintain this advantage at larger model sizes, suggesting that its scaling strategy is less effective than D-FINE’s manual design. In contrast, the DINOv2-B backbone family shows the opposite trend, where the performance gap between D-FINE and RF-DETR narrows as latency increases. This implies that at higher latencies, the DINOv2-B based RF-DETR models could surpass D-FINE (and indeed RF-DETR (2x-large) outperforms D-FINE on mAP 50:95). Importantly, expanding the D-FINE model family would require substantial additional engineering effort, whereas extending the RF-DETR model family is straightforward; higher-latency variants can be sampled directly from the same NAS search without re-training. We present the COCO and RF100-VL of our larger variants in Tables [12](#A5.T12), [13](#A5.T13), and [14](#A5.T14). We also include an RF-DETR Max variant on each dataset to show our method’s maximum performance with latency less than 100ms, a scale other model families don’t reach.

| Method (Backbone) | S | M | L | XL |
|---|---|---|---|---|
| RF-DETR (DINOv2-S) | +2.3 | +0.9 | -0.4 | -1.1 |
| RF-DETR (DINOv2-B) | -3.1 | -1.3 | -1.2 | -0.7 |

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| Real-Time Object Detection w/ NMS | ||||||||||
| YOLOv8 (yolov8) | L | 43.7M | 165.2 | 8.0 | 49.5 | 64.7 | 54.0 | 30.2 | 55.1 | 68.5 |
| YOLOv11 (yolov11) | L | 25.3M | 86.9 | 6.5 | 49.9 | 64.9 | 54.5 | 30.4 | 55.9 | 68.1 |
| YOLOv8 (yolov8) | XL | 68.2M | 257.8 | 11.3 | 50.5 | 65.6 | 55.1 | 30.0 | 56.2 | 69.5 |
| YOLOv11 (yolov11) | XL | 56.9M | 194.9 | 10.5 | 50.9 | 66.1 | 55.4 | 31.5 | 56.6 | 68.7 |
| End-to-End Real-Time Object Detection | ||||||||||
| RT-DETR (zhao2024rtdetr) | R50 | 42M | 136 | 8.5 | 55.0 | 73.3 | 59.8 | 37.9 | 59.7 | 71.6 |
| LW-DETR (chen2024lw) | L | 46.8M | 137.5 | 6.9 | 56.1 | 74.6 | 61.0 | 37.1 | 60.4 | 73.0 |
| D-FINE (peng2024dfine) | L | 31M | 91 | 7.5 | 57.2 | 74.9 | 62.2 | 40.6 | 61.4 | 73.7 |
| RF-DETR (Ours) | L | 33.9M | 125.6 | 6.8 | 56.5 | 75.1 | 61.3 | 39.0 | 61.0 | 73.9 |
| RT-DETR (zhao2024rtdetr) | R101 | 76M | 259 | 12.0 | 56.1 | 74.5 | 61.1 | 38.1 | 60.4 | 73.4 |
| LW-DETR (chen2024lw) | XL | 118.0M | 342.5 | 13.0 | 58.3 | 76.9 | 63.3 | 40.2 | 63.3 | 74.7 |
| D-FINE (peng2024dfine) | XL | 62M | 202 | 11.5 | 59.3 | 76.8 | 64.6 | 42.1 | 64.2 | 76.3 |
| RF-DETR (Ours) | XL | 126.4M | 299.3 | 11.5 | 58.6 | 77.4 | 63.8 | 40.3 | 63.9 | 76.2 |
| RF-DETR (Ours) | 2XL | 126.9M | 438.4 | 17.2 | 60.1 | 78.5 | 65.5 | 43.2 | 64.9 | 76.2 |
| RF-DETR (Ours) | Max | 132.4M | 1742.5 | 98.0 | 61.8 | 79.7 | 67.7 | 47.5 | 66.1 | 76.0 |

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| Real-Time Instance Segmentation w/ NMS | ||||||||||
| YOLOv8 (yolov8) | L | 46.0M | 220.5 | 9.7 | 39.0 | 60.5 | 41.7 | 18.0 | 44.7 | 57.8 |
| YOLOv11 (yolov11) | L | 27.6M | 132.2 | 8.3 | 39.5 | 61.5 | 42.1 | 18.6 | 45.5 | 59.4 |
| YOLOv8 (yolov8) | XL | 71.8M | 344.1 | 14.0 | 39.5 | 61.3 | 42.1 | 18.9 | 45.6 | 58.8 |
| YOLOv11 (yolov11) | XL | 62.1M | 296.4 | 13.7 | 40.1 | 62.4 | 42.6 | 18.8 | 46.4 | 60.1 |
| End-to-End Real-Time Instance Segmentation | ||||||||||
| RF-DETR (Ours) | L | 36.2M | 151.1 | 8.8 | 47.1 | 70.5 | 50.9 | 28.4 | 52.1 | 65.6 |
| RF-DETR (Ours) | XL | 38.1M | 260.0 | 13.5 | 48.8 | 72.2 | 53.1 | 30.6 | 53.3 | 65.9 |
| RF-DETR (Ours) | 2XL | 38.6M | 435.3 | 21.8 | 49.9 | 73.1 | 54.5 | 33.9 | 54.1 | 65.7 |
| RF-DETR (Ours) | Max | 40.1M | 1668.2 | 95.6 | 50.5 | 74.0 | 55.4 | 34.6 | 54.2 | 65.4 |

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| Real-Time Object Detection w/ NMS | ||||||||||
| YOLOv8 (yolov8) | L | 43.7M | 165.2 | 7.9 | 56.5 | 82.1 | 61.1 | 7.1 | 46.0 | 48.9 |
| YOLOv11 (yolov11) | L | 25.3M | 86.9 | 6.4 | 56.5 | 82.2 | 61.0 | 6.4 | 45.5 | 49.0 |
| YOLOv8 (yolov8) | XL | 68.2M | 257.8 | 11.2 | 56.5 | 82.3 | 61.0 | 6.6 | 45.7 | 47.9 |
| YOLOv11 (yolov11) | XL | 56.9M | 194.9 | 10.3 | 56.2 | 81.7 | 60.8 | 6.1 | 45.9 | 48.1 |
| End-to-End Real-Time Object Detection | ||||||||||
| RT-DETR (zhao2024rtdetr) | R50 | 42M | 136 | 8.4 | 61.7 | 87.7 | 66.9 | 38.1 | 57.1 | 69.4 |
| LW-DETR (chen2024lw) | L | 46.8M | 137.5 | 6.8 | 61.5 | 87.4 | 67.0 | 37.1 | 56.4 | 69.0 |
| D-FINE (peng2024dfine) | L | 31M | 91 | 7.5 | 61.6 | 86.4 | 67.2 | 37.8 | 56.5 | 70.1 |
| RF-DETR (Ours) | L | 34.1M | 119.1 | 6.3 | 62.3 | 88.2 | 68.0 | 36.4 | 57.3 | 70.6 |
| RF-DETR (Ours) w/ Fine-Tuning | L | 34.1M | 119.1 | 6.3 | 62.6 | 88.4 | 68.2 | 37.0 | 57.5 | 70.5 |
| RT-DETR (zhao2024rtdetr) | R101 | 76M | 259 | 11.9 | 61.0 | 87.4 | 66.2 | 36.6 | 56.3 | 68.2 |
| LW-DETR (chen2024lw) | XL | 118.0M | 342.5 | 13.0 | 62.1 | 87.9 | 67.6 | 37.4 | 57.1 | 70.2 |
| D-FINE (peng2024dfine) | XL | 59.3 | 76.8 | 11.4 | 62.2 | 86.9 | 68.0 | 37.6 | 57.4 | 69.7 |
| RF-DETR (Ours) | XL | 35.0M | 199.0 | 9.8 | 62.7 | 88.5 | 68.5 | 39.3 | 58.4 | 70.4 |
| RF-DETR (Ours) w/ Fine-Tuning | XL | 35.0M | 199.0 | 9.8 | 63.1 | 88.6 | 69.0 | 39.6 | 58.5 | 70.8 |
| RF-DETR (Ours) | 2XL | 123.5M | 410.2 | 15.6 | 63.3 | 88.9 | 69.0 | 38.7 | 58.2 | 71.6 |
| RF-DETR (Ours) w/ Fine-Tuning | 2XL | 123.5M | 410.2 | 15.6 | 63.5 | 89.0 | 69.2 | 38.9 | 58.3 | 71.7 |

## Appendix F Impact on NAS Fine-Tuning on COCO

We find that fine-tuning after NAS provides limited benefit for COCO. We posit that the NAS “architecture augmentation” acts as a strong regularizer, and additional training without this regularization leads to degraded performance. Specifically, when models are pre-trained with strong regularization, removing the regularization during fine-tuning leads to overfitting. As shown in Tables [15](#A6.T15) and [16](#A6.T16), this trend is consistent across both detection and segmentation tasks. Interestingly, models trained on RF100-VL benefit more from fine-tuning, likely because they require more than 100 epochs to converge. In such cases, we posit that reducing the total number of NAS configurations during training, or training for more than 100 epochs with weight-sharing NAS can improve performance.

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| End-to-End Real-Time Object Detectors | ||||||||||
| RF-DETR (Ours) | N | 30.5M | 31.9 | 2.3 | 48.0 | 67.0 | 51.4 | 25.2 | 53.5 | 70.0 |
| RF-DETR (Ours) w/ Fine-Tuning | N | 30.5M | 31.9 | 2.3 | +0.4 | +0.6 | +0.3 | +0.1 | +0.1 | +1.3 |
| RF-DETR (Ours) | S | 32.1M | 59.8 | 3.5 | 52.9 | 71.9 | 57.0 | 32.0 | 58.3 | 73.0 |
| RF-DETR (Ours) w/ Fine-Tuning | S | 32.1M | 59.8 | 3.5 | +0.1 | +0.2 | +0.2 | -0.2 | +0.2 | +0.1 |
| RF-DETR (Ours) | M | 33.7M | 78.8 | 4.4 | 54.7 | 73.5 | 59.2 | 36.1 | 59.7 | 73.8 |
| RF-DETR (Ours) w/ Fine-Tuning | M | 33.7M | 78.8 | 4.4 | +0.0 | +0.1 | +0.0 | -0.1 | +0.1 | -0.1 |
| RF-DETR (Ours) | L | 33.9M | 125.6 | 6.8 | 56.5 | 75.1 | 61.3 | 39.0 | 61.0 | 73.9 |
| RF-DETR (Ours) w/ Fine-Tuning | L | 33.9M | 125.6 | 6.8 | +0.0 | +0.0 | +0.0 | -0.1 | +0.1 | +0.1 |
| RF-DETR (Ours) | XL | 126.4M | 299.3 | 11.5 | 58.6 | 77.4 | 63.8 | 40.3 | 63.9 | 76.2 |
| RF-DETR (Ours) w/ Fine-Tuning | XL | 126.4M | 299.3 | 11.5 | +0.3 | +0.1 | +0.2 | +0.5 | +0.4 | +0.1 |
| RF-DETR (Ours) | 2XL | 126.9M | 438.4 | 17.2 | 60.1 | 78.5 | 65.5 | 43.2 | 64.9 | 76.2 |
| RF-DETR (Ours) w/ Fine-Tuning | 2XL | 126.9M | 438.4 | 17.2 | +0.1 | +0.0 | +0.3 | +0.5 | +0.2 | +0.1 |

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| End-to-End Real-Time Object Detectors | ||||||||||
| RF-DETR-Seg. (Ours) | N | 33.6M | 50.0 | 3.4 | 40.3 | 63.0 | 42.6 | 16.3 | 45.3 | 63.6 |
| RF-DETR-Seg. w/ Fine-Tuning (Ours) | N | 33.6M | 50.0 | 3.4 | +0.1 | +0.4 | +0.0 | -0.5 | +0.2 | +0.7 |
| RF-DETR-Seg. (Ours) | S | 33.7M | 70.6 | 4.4 | 43.1 | 66.2 | 45.9 | 21.9 | 48.5 | 64.1 |
| RF-DETR w/ Fine-Tuning (Ours) | S | Did | Not | Improve | - | - | - | - | - | - |
| RF-DETR-Seg. (Ours) | M | 35.7M | 102.0 | 5.9 | 45.3 | 68.4 | 48.8 | 25.5 | 50.4 | 65.3 |
| RF-DETR w/ Fine-Tuning (Ours) | M | Did | Not | Improve | - | - | - | - | - | - |
| RF-DETR (Ours) | L | 36.2M | 151.1 | 8.8 | 47.1 | 70.5 | 50.9 | 28.4 | 52.1 | 65.6 |
| RF-DETR (Ours) w/ Fine-Tuning | L | Did | Not | Improve | - | - | - | - | - | - |
| RF-DETR (Ours) | XL | 38.1M | 260.0 | 13.5 | 48.8 | 72.2 | 53.1 | 30.6 | 53.3 | 65.9 |
| RF-DETR (Ours) w/ Fine-Tuning | XL | Did | Not | Improve | - | - | - | - | - | - |
| RF-DETR (Ours) | 2XL | 38.6M | 435.3 | 21.8 | 49.9 | 73.1 | 54.5 | 33.9 | 54.1 | 65.7 |
| RF-DETR (Ours) w/ Fine-Tuning | 2XL | Did | Not | Improve | - | - | - | - | - | - |

## Appendix G Impact of Fixed Architecture on RF100-VL

We evaluate the impact of transferring a NAS architecture optimized for COCO to RF100-VL in Table [17](#A7.T17). We find that these fixed architecture models perform remarkably well without further dataset-specific NAS. Specifically, RF-DETR (large) model with a fixed architecture achieves the best performance among all prior real-time models on COCO. However, dataset-specific NAS yields significant additional gains. Notably, the improvement from LW-DETR to the fixed architecture is comparable to the improvement from the fixed architecture to the NAS-optimized model on the target dataset for N, S, and M scale models.

| Model | Size | # Params. | GFLOPS | Latency (ms) | AP | AP50 |
AP75 |
APS |
APM |
APL |
| End-to-End Real-Time Object Detectors | ||||||||||
| RF-DETR (Ours) Fixed Architecture | N | 30.5M | 31.9 | 2.3 | 57.7 | 85.0 | 61.9 | 30.8 | 51.5 | 67.4 |
| RF-DETR (Ours) | N | 30.8M | 36.3 | 2.5 | 57.6 | 84.9 | 62.1 | 30.7 | 52.2 | 66.8 |
| RF-DETR w/ Fine-Tuning (Ours) | N | 30.8M | 36.3 | 2.5 | 58.7 | 85.6 | 63.5 | 32.4 | 52.7 | 67.0 |
| RF-DETR (Ours) Fixed Architecture | S | 32.1M | 59.8 | 3.5 | 60.2 | 86.7 | 65.0 | 34.2 | 54.4 | 68.9 |
| RF-DETR (Ours) | S | 33.3M | 65.5 | 3.7 | 60.7 | 87.0 | 66.0 | 35.4 | 55.4 | 69.6 |
| RF-DETR w/ Fine-Tuning (Ours) | S | 33.3M | 65.5 | 3.7 | 61.0 | 87.2 | 66.4 | 35.3 | 55.9 | 69.8 |
| RF-DETR (Ours) Fixed Architecture | M | 33.7M | 78.8 | 4.4 | 61.2 | 87.4 | 66.4 | 35.8 | 56.1 | 69.8 |
| RF-DETR (Ours) | M | 33.6M | 91.0 | 4.6 | 61.5 | 87.7 | 67.0 | 36.44 | 56.5 | 69.8 |
| RF-DETR w/ Fine-Tuning (Ours) | M | 33.6M | 91.0 | 4.6 | 61.9 | 87.9 | 67.3 | 36.4 | 56.6 | 70.1 |
| RF-DETR (Ours) w/ Fixed Architecture | L | 33.9M | 125.6 | 6.8 | 62.2 | 88.2 | 67.8 | 37.7 | 57.0 | 70.5 |
| RF-DETR (Ours) | L | 34.1M | 119.1 | 6.3 | 62.3 | 88.2 | 68.0 | 36.4 | 57.3 | 70.6 |
| RF-DETR (Ours) w/ Fine-Tuning | L | 34.1M | 119.1 | 6.3 | 62.6 | 88.4 | 68.2 | 37.0 | 57.5 | 70.5 |
| RF-DETR (Ours, DINOv2-Base) w/ Fixed Architecture | XL | 126.4M | 299.3 | 11.5 | 62.9 | 88.5 | 68.6 | 37.0 | 57.5 | 71.3 |
| RF-DETR (Ours) | XL | 35.0M | 199.0 | 9.8 | 62.7 | 88.5 | 68.5 | 39.3 | 58.4 | 70.4 |
| RF-DETR (Ours) w/ Fine-Tuning | XL | 35.0M | 199.0 | 9.8 | 63.1 | 88.6 | 69.0 | 39.6 | 58.5 | 70.8 |
| RF-DETR (Ours, DINOv2-Base) w/ Fixed Architecture | 2XL | 126.9M | 438.4 | 17.1 | 63.2 | 89.0 | 69.3 | 38.4 | 58.4 | 71.5 |
| RF-DETR (Ours, DINOv2-Base) | 2XL | 123.5M | 410.2 | 15.6 | 63.3 | 88.9 | 69.0 | 38.7 | 58.2 | 71.6 |
| RF-DETR (Ours, DINOv2-Base) w/ Fine-Tuning | 2XL | 123.5M | 410.2 | 15.6 | 63.5 | 89.0 | 69.2 | 38.9 | 58.3 | 71.7 |

## Appendix H Discussion on Notable Discovered Architectures

All “tunable” knobs are used when defining the Pareto-optimal model families, validating our choice of search space. This suggests that expanding the search space may additionally improve downstream performance.

The Pareto optimal models tend to use the same patch size, excluding the Max variants which are just chosen as the highest accuracy running at less than 100ms. For example, the optimal patch size for RF-DETR with a DINOv2-S backbone converges to a size of 16, whereas the DINOv2-B backbone converges to a patch size of 20. The optimal patch size for RF-DETR-Seg with a DINOv2-S backbone is 12. All Pareto-optimal model families simultaneously scale the compute in both the encoder and the decoder. Changing patch size, number of windows, and resolution impacts the encoder, and changing number of decoder layers and number of queries impacts the decoder. For RF-DETR-Seg, scaling resolution also impacts the segmentation head. We find that using 2 windows is typically optimal in the encoder and resolution scales within a family as we increase latency. For the decoder, on COCO the detector model keeps queries constant and scales decoder layers only, while for the segmentation model both are scaled simultaneously. This may be because the depth of the segmentation head is tied to the number of decoder layers, and there may be a certain minimum number of layers in the segmentation head that produce viable masks, so even the lowest latency model uses at least that number of layers. To compensate for the additional latency of those decoder layers, the segmentation model trades off the number of queries it uses to get lower latency for smaller model sizes, which effectively reduces the width of the decoder. While the object detector evaluated on COCO prefers a wide and shallow decoder, the segmentation model prefers a thin and deep decoder.

We find that RF-DETR’s performance depends on the number of spatial locations (e.g. resolution divided by patch size) rather than resolution or patch size individually. Scaling resolution while fixing patch size yields similar results to scaling patch size while fixing resolution, since vision transformers are agnostic to absolute input resolution after the patchify-and-project stage. To verify this, we constructed an alternative family with fixed resolution () and varied patch sizes to preserve the number of spatial locations. Specifically, we evaluate RF-DETR (nano) with a patch size of , RF-DETR (small) with a patch size of , and RF-DETR (medium) with a patch size of , achieving results nearly identical to the Pareto-optimal family. Notably, patch sizes of and were unseen during training, demonstrating RF-DETR’s strong generalization to novel patch sizes.

However, we find that this trend does not hold for RF-DETR-Seg. The segmentation head features are always upsampled to run at 1/4 scale of the input image resolution. Therefore, scaling resolution affects both the number of spatial locations and the segmentation head resolution. Specifically, RF-DETR-Seg (nano) uses a resolution of and a patch size of , yielding a segmentation head resolution of with spatial locations; RF-DETR-Seg (small) uses a resolution of and a patch size of , yielding a segmentation head resolution with spatial locations; and RF-DETR-Seg (medium) uses a resolution of and a patch size of , yielding a segmentation head resolution of with spatial locations. In contrast, scaling patch size alone (e.g., a patch size of at a resolution of ) can keep spatial locations fixed while increasing head resolution (to ). This is a more nuanced interaction between patch size and resolution than is observed in RF-DETR object detection. RF-DETR(medium) uses spatial locations, while RF-DETR-Seg (medium) uses spatial locations, but at a lower resolution, showing that the additional tying of the segmentation mask resolution changes the Pareto-optimal resolution even if the optimal number of spatial locations is the same for a given latency range.

Dataset characteristics influence optimal discovered architectures. We find that when running NAS on RF100-VL datasets, the optimal lower latency models tend to use fewer queries than the COCO models of equivalent latency, which always uses 300. This may be because RF100-VL datasets tend to have fewer objects per image than COCO, so fewer queries are required to find all the objects, as each query is able to find a single object.

Most Pareto-optimal RF-DETRmodels perform best with 2 windows, whereas LW-DETR achieves the best performance with 4 windows. We attribute this difference to how each architecture handles class tokens. LW-DETR’s CAEv2 backbone omits the class token, while RF-DETR’s DINOv2 backbone relies on it as a key part of pre-training. To make windowed attention compatible with class tokens, we duplicate the class token for each window. During global attention, window-level class tokens attend to one another, while all other tokens attend to all class tokens. In practice, RF-DETR (nano), RF-DETR (small), and RF-DETR (medium) all use 2 windows, since duplicating class tokens for additional windows reduces runtime efficiency. As a result, unlike LW-DETR, RF-DETR does not benefit from scaling to 4 windows.

To generate our model based on DINOv2-B, we follow the scaling strategy from ViT-S to ViT-B and just double the width of all layers in the model. We find that this is sufficient to gain strong and differentiated performance when we allow NAS to explore the axis of variation we’ve defined. Notably, different from LW-DETR’s larger variants, we don’t use higher resolution feature maps from the backbone.

## Appendix I Visualizing Model Predictions

We visualize model predictions from RF-DETR (nano) and compare them with comparable detection and segmentation baselines in Figure [6](#A9.F6). We find that RF-DETR (nano) predicts fewer false positives (e..g mistaking sign post for person). Similarly, RF-DETR-Seg. (nano) predicts more precise object boundaries.
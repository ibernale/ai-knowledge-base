---
title: "RF-DETR: Neural Architecture Search for Real-Time Detection Transformers"
url: https://arxiv.org/abs/2511.09554
source: arxiv
type: paper
authors: ["Isaac Robinson", "Peter Robicheaux", "Fedor Popov", "Deva Ramanan", "Neehar Peri"]
published: "2026-02-03"
ingested: "2026-05-06"
tags: ["research/multimodal", "research/inference", "type/paper", "access/public"]
---

# RF-DETR: Neural Architecture Search for Real-Time Detection Transformers

## Why it matters
RF-DETR is the first real-time object detector to surpass 60 AP on COCO, accepted at ICLR 2026. Using weight-sharing NAS on a DINOv2 vision transformer backbone, it discovers accuracy-latency Pareto curves for any target dataset without re-training. RF-DETR-nano beats D-FINE-nano by 5.3 AP at similar latency; RF-DETR-2x-large outperforms GroundingDINO-tiny by 1.2 AP while running 20× faster. Apache 2.0 licensed core models. This is now trending on Hugging Face with 187 upvotes and represents the CV community's shift from YOLO to transformer-based real-time detection.

## Abstract (original)
Open-vocabulary detectors achieve impressive performance on COCO, but often fail to generalize to real-world datasets. Rather than fine-tuning a heavy-weight VLM, we introduce RF-DETR, a light-weight specialist detection transformer that discovers accuracy-latency Pareto curves with weight-sharing neural architecture search.

## Source
[https://arxiv.org/abs/2511.09554](https://arxiv.org/abs/2511.09554)

## Full text
[[2026-05-06-rf-detr-neural-architecture-search-for-real-time-detection-t.full]] (extracted: ar5iv)
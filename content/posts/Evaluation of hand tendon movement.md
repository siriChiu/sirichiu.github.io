---
title: 手指肌腱位移評估技術
slug: Evaluation of hand tendon movement
date: 2022-04-22
categories:
- 研究生專題
tags:
- MATLAB
- Ultrasound
- Vector Doppler Imaging
- Tendon Displacement
- Medical Imaging

thumbnailImagePosition: left
thumbnailImage: /postImg/EvaluationOfHandTendonMovement/0.png
katex: true
---
向量都卜勒成像 (Vector Doppler Imaging) 可用來估算目標在不同方向上的運動變化。除了血液流速分析外，本專案也嘗試將此方法應用於手指肌腱滑動評估，提供較量化的位移資訊作為復健評估參考。
<!--more-->


## 摘要

本研究以人類手指肌腱為觀測目標，透過高通濾波降低自然顫動造成的干擾，再以視覺化演算法呈現肌腱移動過程中的速度與位移變化。目標是探索超音波量化肌腱位移距離的可行性，作為後續復健評估工具的基礎。

![手指肌腱 Vector Doppler 位移評估流程](/postImg/EvaluationOfHandTendonMovement/vector-doppler-workflow.svg)

## 方法
基於不同超音波發射角度相關的超音波都卜勒公式如下:

$$v = \begin{bmatrix}v_z \\\ v_x\end{bmatrix} = (A^TA)^{-1}A^Tu$$

得到這一連串的縱向與橫向速度，就能繪製出肌腱滑動行進的動畫。

## 結果


|Longitudinal View|Transverse View|
| --- | --- |
|{{< video src="/videos/humanTendonVectorDopplerTVB.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="400" height="300">}}|{{< video src="/videos/humanTendonVectorDopplerLVB.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="400" height="300">}}|







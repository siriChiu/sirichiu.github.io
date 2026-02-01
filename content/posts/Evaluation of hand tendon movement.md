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
向量都卜勒成像(Vector Doppler Imaging)能夠觀測更多的目標運動變化，除了應用在血液流速的估算外，也可以應用在肌腱上評估肌腱的滑動性，進而提供肌腱的位移資訊給予醫師更多評估的信息。
<!--more-->


## 摘要
Evaluation of hand tendon movement

提出一種臨床評估上手部復健程度的新方法，這裡的目標物也是人類的手指肌腱，透過高通濾波器將人體自然顫動去除，並透過視覺化的演算法顯現出手指肌腱再移動過程中的變化，這個研究希望透過超音波量化病人的肌腱位移距離作為評估患者受傷程度的工具。

## 方法
基於不同超音波發射角度相關的超音波都卜勒公式如下:

$$v = \begin{bmatrix}v_z \\\ v_x\end{bmatrix} = (A^TA)^{-1}A^Tu$$

得到這一連串的縱向與橫向速度，就能繪製出肌腱滑動行進的動畫。

## 結果


|Longitudinal View|Transverse View|
| --- | --- |
|{{< video src="/videos/humanTendonVectorDopplerTVB.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="400" height="300">}}|{{< video src="/videos/humanTendonVectorDopplerLVB.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="400" height="300">}}|







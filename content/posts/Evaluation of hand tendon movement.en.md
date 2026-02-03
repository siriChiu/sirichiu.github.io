---
title: "Hand Tendon Displacement Evaluation Technology"
slug: Evaluation of hand tendon movement
date: 2022-04-22
categories:
- Graduate Project
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
Vector Doppler Imaging can observe more target motion changes. Besides blood flow velocity estimation, it can also be applied to tendons to evaluate tendon gliding, providing physicians with displacement information for more comprehensive assessment.
<!--more-->


## Abstract
Evaluation of hand tendon movement

This research proposes a new clinical method for evaluating hand rehabilitation progress. The target is human finger tendons. By using high-pass filters to remove natural tremors and visualization algorithms to display changes during finger tendon movement, this study aims to quantify tendon displacement using ultrasound as a tool for assessing patient injury severity.

## Method
The ultrasound Doppler formula related to different ultrasound emission angles is as follows:

$$v = \begin{bmatrix}v_z \\\ v_x\end{bmatrix} = (A^TA)^{-1}A^Tu$$

By obtaining this series of longitudinal and transverse velocities, we can create animations of tendon gliding movement.

## Results


|Longitudinal View|Transverse View|
| --- | --- |
|{{< video src="/videos/humanTendonVectorDopplerTVB.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="400" height="300">}}|{{< video src="/videos/humanTendonVectorDopplerLVB.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="400" height="300">}}|





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
Vector Doppler Imaging can estimate motion components in different directions. Besides blood-flow analysis, this project applies the method to hand tendon movement evaluation, providing more quantitative displacement information for rehabilitation assessment research.
<!--more-->


## Abstract

This study uses human finger tendons as the observation target. A high-pass filter reduces interference from natural hand tremor, and visualization algorithms present velocity and displacement changes during tendon movement. The goal is to explore whether ultrasound can quantify tendon displacement for later rehabilitation assessment workflows.

![Hand tendon Vector Doppler displacement workflow](/postImg/EvaluationOfHandTendonMovement/vector-doppler-workflow.svg)

## Method
The ultrasound Doppler formula related to different ultrasound emission angles is as follows:

$$v = \begin{bmatrix}v_z \\\ v_x\end{bmatrix} = (A^TA)^{-1}A^Tu$$

By obtaining this series of longitudinal and transverse velocities, we can create animations of tendon gliding movement.

## Results


|Longitudinal View|Transverse View|
| --- | --- |
|{{< video src="/videos/humanTendonVectorDopplerTVB.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="400" height="300">}}|{{< video src="/videos/humanTendonVectorDopplerLVB.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="400" height="300">}}|





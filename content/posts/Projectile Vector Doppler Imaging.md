---
title:  射流向量多普勒成像技術在靜脈瓣膜血流分析中的應用
slug: Projectile Vector Doppler Imaging
date: 2022-04-23
categories:
- 研究生專題
tags:
- MATLAB
- Ultrasound
- Vector Doppler
- Signal Processing
- Medical Imaging

thumbnailImagePosition: left
thumbnailImage: /postImg/ProjectileVectorDopplerImaging/0.png
katex: true
---
<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

動態向量都卜勒(Projectile Vector Doppler Imaging) 比傳統都卜勒影像提供更多樣的血液資訊，如流速、流動，擾流情況等，給予醫師更多診斷資訊。

<!--more-->

## 摘要

都卜勒成像(Doppler Imaging)是醫療超音波中儀器常見的模式，透過超音波都卜勒的公式能夠估算出血液的速度，而其中向量都卜勒成像(Vector Doppler Imaging)，能夠估算出其中更詳細資訊，如相位與速度資訊。

## 方法

Projectile Vector Doppler Imaging

超音波向量都卜勒公式是由不同的超音波發射角度與一般的超音波都卜勒公式所推導而來的，如下圖。
![Untitled](/postImg/ProjectileVectorDopplerImaging/1.png)

其中θ, φ為超音波發射角與接收角， α為超音波探頭與目標的角度。

套用都卜勒公式後可推導出與發射及接收角度相關的向量都卜勒公式:

$$
f_d≅{2\times cos⁡(θ-α)+2\times v\times cos⁡(φ-α)\over c }\times f_0
$$

整理此式可得:

$$
v_y (cosθ_m+cosφ_n )+v_x (sinθ_m+sinφ_n )={c\over f_0}\times f_d
$$

通過不同角度的超音波資訊，再以最小平方法推算，推導出各方向的速度與不同超音波發射的角度資訊關係式。

$$
Av=u⇒\begin{bmatrix} cos⁡ θ_1 + cos⁡ φ_1 & sin⁡ θ_1 + sin φ_1 \\\⋮&⋮\\\ cos⁡ θ_M + cos⁡ φ_N & sin⁡ θ_M + sin φ_N 
\end{bmatrix}
\begin{bmatrix}v_z \\\ v_x\end{bmatrix} = 
\begin{bmatrix}u_{11} \\\ ⋮ \\\ u_{MN}\end{bmatrix}
$$

$$v = \begin{bmatrix}v_z \\\ v_x\end{bmatrix} = (A^TA)^{-1}A^Tu$$

## 結果

**人類膕靜脈(popliteal vein)瓣膜的Projectile Vector Doppler 影像**
可以清楚看見紅血球在經過靜脈瓣膜的時候因為壓力改變而有噴發的現象，這技術在臨床上可以看見血管健康程度，假設該患部有血栓或靜脈區張，透過此技術可以輕易的看出血流的變化趨勢。

{{< video src="/videos/ProjectileVectorDoppler.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="600" height="500">}}

## 參考
[Vector Projectile Imaging: Time-Resolved Dynamic Visualization of Complex Flow Patterns - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0301562914001628?casa_token=tl9X1qyiT3YAAAAA:DzDVDOpl_INb7eAkYlDe52KAaP4rMb6lGrP7WEfn3GwJoPFkWEpEhnNqMSPeFmwPrcXCYFynOP0)




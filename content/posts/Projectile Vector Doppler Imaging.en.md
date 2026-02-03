---
title: "Projectile Vector Doppler Imaging for Venous Valve Blood Flow Analysis"
slug: Projectile Vector Doppler Imaging
date: 2022-04-23
categories:
- Graduate Project
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

Projectile Vector Doppler Imaging provides more diverse blood information than traditional Doppler imaging, such as flow velocity, flow direction, and turbulence conditions, giving physicians more diagnostic information.

<!--more-->

## Abstract

Doppler Imaging is a common mode in medical ultrasound equipment. Blood velocity can be estimated through the ultrasound Doppler formula. Among these, Vector Doppler Imaging can estimate more detailed information such as phase and velocity data.

## Method

Projectile Vector Doppler Imaging

The ultrasound vector Doppler formula is derived from different ultrasound emission angles and the general ultrasound Doppler formula, as shown below.
![Untitled](/postImg/ProjectileVectorDopplerImaging/1.png)

Where θ, φ are ultrasound emission and reception angles, α is the angle between ultrasound probe and target.

After applying the Doppler formula, a vector Doppler formula related to emission and reception angles can be derived:

$$
f_d≅{2\times cos⁡(θ-α)+2\times v\times cos⁡(φ-α)\over c }\times f_0
$$

Rearranging this equation:

$$
v_y (cosθ_m+cosφ_n )+v_x (sinθ_m+sinφ_n )={c\over f_0}\times f_d
$$

Using ultrasound information from different angles and the least squares method, the velocity-to-emission-angle relationship in each direction is derived.

$$
Av=u⇒\begin{bmatrix} cos⁡ θ_1 + cos⁡ φ_1 & sin⁡ θ_1 + sin φ_1 \\\⋮&⋮\\\ cos⁡ θ_M + cos⁡ φ_N & sin⁡ θ_M + sin φ_N 
\end{bmatrix}
\begin{bmatrix}v_z \\\ v_x\end{bmatrix} = 
\begin{bmatrix}u_{11} \\\ ⋮ \\\ u_{MN}\end{bmatrix}
$$

$$v = \begin{bmatrix}v_z \\\ v_x\end{bmatrix} = (A^TA)^{-1}A^Tu$$

## Results

**Projectile Vector Doppler Image of Human Popliteal Vein Valve**
You can clearly see the ejection phenomenon of red blood cells as they pass through the venous valve due to pressure changes. Clinically, this technique can visualize vascular health. If the patient has a blood clot or varicose veins, this technique can easily reveal blood flow change trends.

{{< video src="/videos/ProjectileVectorDoppler.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="600" height="500">}}

## Reference
[Vector Projectile Imaging: Time-Resolved Dynamic Visualization of Complex Flow Patterns - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0301562914001628?casa_token=tl9X1qyiT3YAAAAA:DzDVDOpl_INb7eAkYlDe52KAaP4rMb6lGrP7WEfn3GwJoPFkWEpEhnNqMSPeFmwPrcXCYFynOP0)



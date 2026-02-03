---
title: "Mechanism Synthesis Optimization: MATLAB-Based Numerical Path Generator for Four-Bar Linkage"
slug: 4-Bar linkage
date: 2022-04-22
categories:
- Graduate Project
tags:
- MATLAB
- Mechanism Synthesis
- Kinematics
- Optimization
- Numerical Analysis
- Deep Learning & Machine Learning

thumbnailImagePosition: left
thumbnailImage: /postImg/4-Bar Linkage/1.png
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
This project explores a classic problem in mechanism design—"Path Generation." The goal is to design a four-bar linkage whose coupler curve precisely passes through 9 specified target points in space.
<!--more-->


---

## 📋 Abstract

Unlike traditional graphical or trial-and-error methods, this project employs a **numerical optimization** strategy. Using **MATLAB**, I built a kinematic model based on the Vector Loop Equation and utilized the `fminsearch` algorithm for multi-variable iterative solving of link lengths and initial angles. The result successfully identified optimal mechanism parameters with minimal error while satisfying Grashof's theorem (full rotation condition).

---

## 🛑 The Problem

In a course project, we were given 9 fixed spatial coordinate points. The task was to design a four-bar linkage such that when the driving link rotates one full revolution, a specific point on the coupler traces a path that closely matches these 9 points.

This is a typical **nonlinear optimization problem** facing the following challenges:
1.  **Multi-variable Coupling:** Changing any single link length dramatically alters the entire trajectory shape.
2.  **Geometric Constraints:** The mechanism must perform a full 360-degree rotation (Crank-Rocker) without locking.
3.  **Mathematical Complexity:** The nonlinear position equations of the coupler cannot be solved analytically and require numerical methods.

---

## 🛠️ Technical Deep Dive

The core of this project lies in transforming a physical mechanism into a mathematical model and defining an objective function that the computer can "score."

### 1. Mathematical Modeling: Vector Loop Method

To calculate the mechanism's position at any angle, I used the Complex Numbers Method. As shown in the figure, the four-bar linkage is viewed as a closed vector loop:

$$\vec{r_2} + \vec{r_3} = \vec{r_1} + \vec{r_4}$$

Using Euler's formula ($e^{i\theta} = \cos\theta + i\sin\theta$), this expands into real and imaginary parts:

$$r_2 e^{i\theta_2} + r_3 e^{i\theta_3} - r_4 e^{i\theta_4} - r_1 = 0$$

Through this equation, for each input driving angle $\theta_2$, we can derive the follower angle $\theta_4$ and coupler angle $\theta_3$ using geometric relationships, thereby calculating the precise coordinates $(x, y)$ of trajectory point $P$.

![Untitled](/postImg/4-Bar linkage/1.png)

### 2. Optimization Strategy

I chose MATLAB's `fminsearch` (based on Nelder-Mead simplex method) as the solver.

* **Design Variables:**
    Parameters to be adjusted include the lengths of 4 links ($L_1, L_2, L_3, L_4$) and the initial angle of the driving link ($\theta_{start}$).

* **Cost Function:**
    To define "optimal," I adopted the **Least Squares** concept. Calculate the sum of **Euclidean distances** between corresponding trajectory points and the 9 target points:

    $$Error = \sum_{i=1}^{9} \sqrt{(x_{target,i} - x_{calc,i})^2 + (y_{target,i} - y_{calc,i})^2}$$

    The algorithm's goal is to find a parameter set that minimizes this $Error$ value.

### 3. Constraint Handling

Not all length combinations can form a rotatable mechanism. To ensure the mechanism operates smoothly through one full rotation without locking, it must satisfy **Grashof's Law**:

$$S + L \le P + Q$$

*(Where $S$ is the shortest link, $L$ is the longest link, and $P, Q$ are the remaining two links)*

In implementation, I used the **Penalty Function** technique: before calculating the error, check whether current parameters satisfy the Grashof condition. If not (e.g., mechanism cannot complete full rotation), immediately return an extremely large error value (like `Infinity`), forcing the `fminsearch` algorithm away from that parameter region to find a feasible solution.

---

## 📊 Results & Conclusion

Through hundreds of iterations, the program converged to an optimal set of link length parameters. When plotted, the resulting coupler curve successfully passed through the 9 target points (or with acceptable error margin), and the mechanism operated smoothly without dead points.

This project gave me a deep appreciation for:
1.  **Mathematics is the Language of Engineering:** Through Euler's formula and vector methods, complex mechanical motions can be precisely quantified.
2.  **The Power of Numerical Methods:** When analytical solutions are difficult to obtain, properly setting objective functions and constraints allows algorithms to effectively solve engineering optimization problems.

## Results

{{< video src="/videos/4bar-linkage.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="720" height="720">}}





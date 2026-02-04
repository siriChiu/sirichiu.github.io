---
title: "Server Cooling Control Algorithm: Automated PID Parameter Generation System Based on Steady-State Thermal Profiles"
slug: new-pid-for-server
date: 2025-11-10
categories:
- Professional Technology
tags:
- Server Cooling
- PID Algorithm
- Thermal Management
- Automation
- Data Center
- Energy Efficiency
- Golang
- Python
- Grafana
- IPMI
- Linux
- Server BMC
- CI/CD

thumbnailImagePosition: left
thumbnailImage: /postImg/ice_algo/0.jpg
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

This project aims to solve the dual challenges of "low R&D efficiency" and "energy loss" in data center server cooling control. To address the over-design caused by traditional open-loop control and the high time cost of manual PID tuning, I developed an **"Automated Thermal Characteristic Identification System."**

<!--more-->

Unlike traditional tools that only passively execute scripts, this system introduces **physical characteristic modeling** technology. It establishes exclusive mathematical models for components such as CPU (linear growth) and Memory/Ethernet (anti-exponential saturation), enabling reverse derivation and precise locking of target stress environments. In terms of data analysis, the system innovatively designs a **Grafana 4D Heatmap** that integrates temperature, RPM, wattage, and time-frequency, and connects to an **AI vision model** for automated chart interpretation. This solution successfully transforms the system verification process from manual operation to a data-driven intelligent decision-making mode, significantly improving test coverage and risk identification efficiency.

The core technology of this project includes two major breakthroughs:

1. **Physical Characteristic Predictive Modeling**: Established interpretable mathematical models for the heterogeneous power consumption characteristics of components like CPU (linear growth) and Memory/Ethernet (inverse exponential saturation). Precise control of system wattage and stress is achieved through linear fitting and algorithm reverse derivation.

2. **AI-Driven 4D Visualization**: Innovatively designed a Grafana 4D heatmap integrating temperature, RPM, wattage, and time-frequency. It connects to visual AI models for automated chart interpretation, identifying potential cooling risks and performance bottlenecks in real-time. This system successfully transforms the hardware verification process from passive execution to proactive data-driven decision-making.

## 📋 Executive Summary

This system integrates **Golang** and **Python** automation scripts to autonomously build a server's **Steady-state Thermal Profile** through chamber testing. It uses an original parameter correlation model to automatically derive optimized PID parameters. Additionally, a "Non-zero Integral Reset" mechanism was introduced for scenarios with sudden load changes (Load Dump). This achieved R&D process standardization and significantly improved the server's Power Usage Effectiveness (PUE) and component reliability.

---

## 🛑 Industry Context & Challenges

In the field of server cooling, current mainstream practices face several technical bottlenecks:

### 1. Over-design in Open-loop Control
Traditional "Lookup Table" methods rely solely on fixed RPMs corresponding to temperature ranges. To ensure safety, the industry standard is to set a single cooling curve based on the **Maximum Configuration** supported by the chassis and the **Worst-case Scenario**.
*   **Consequence**: For low-to-mid-range servers, fans operate in an unnecessary "over-speeding" state for long periods, leading to serious energy waste and high-frequency noise.

### 2. Manual Tuning Inefficiency of Traditional PID
Even with closed-loop PID control, parameter settings ($K_p, K_i, K_d$) depend heavily on the experience of senior engineers through trial and error.
*   **Consequence**: Lack of standardized system identification processes leads to weeks of tuning and an inability to accurately adapt to minor hardware differences between individual servers (Lack of Reproducibility).

### 3. Integral Windup & Instability
In Load Dump scenarios, traditional PID is prone to accumulating excessive error in the integral term, causing fan speed to drop too sharply (Undershoot) or even oscillate, affecting cooling stability.

---

## 🛠️ Technical Solution

This invention proposes an **"Automated Control Parameter Generation Method Based on Steady-State Thermal Profile Data Structures,"** transforming cooling control from "experience-driven" to "data-driven."

### ■ System Architecture

We constructed a Hardware-in-the-Loop automation test loop, integrating hardware and software resources:

*   **Host Controller**: Core logic written in **Golang**, utilizing its high concurrency for managing connections to multiple Systems Under Test (SUT). Low-level commands are encapsulated with **Shell Scripts** and **Python** for data cleaning and plotting.
*   **System Under Test (SUT)**: Receives RPM commands and returns sensor data via the BMC interface.
*   **Environmental Chamber**: Provides stable ambient temperature variables.

### ■ Core Methodology

#### 1. Automated Thermal Profiling
During the engineering verification stage (EVT/DVT), automation scripts control the server to traverse multiple computational load points $L_i$ from Idle to Full Load. At each load point, fan speed $\omega$ is scanned step-wise.

When the system detects a temperature change rate $\frac{dT}{dt} \approx 0$, it determines that **Thermal Equilibrium** has been reached and records the data, building a **"Steady-state Thermal Characteristic Profile"** describing the server's physical cooling limits.

#### 2. Parameter Derivation and Modeling
The system parses the profile data, calculates system gain and response slope, and first determines the primary control gain (proportional term $K_p$). 
Next, using a predefined **Parameter Correlation Model**, the integral ($K_i$) and derivative ($K_d$) terms are derived as functions of $K_p$.

Let $\mathcal{M}$ be the transformation model based on thermal time constants and system damping ratios; the PID parameters are derived as follows:

$$K_p = f(\text{Slope}_{profile}, \text{Gain}_{system})$$

$$K_i, K_d = \mathcal{M}(K_p)$$

This ensures that the three parameters have strong physical coupling rather than being random numbers, achieving stability in closed-loop control.

#### 3. Runtime Control with Non-zero Reset
During the BMC runtime phase, I designed a special integral weight management module for rapid temperature drops caused by Load Dumps.
When the error $e(t)$ changes drastically, the integral term $I_{term}$ does not reset to zero as in traditional Anti-windup; instead, it resets to a dynamically calculated base value $I_{base}$:

$$I_{new} = \begin{cases} 0 & \text{Traditional Approach (Risky)} \\ I_{base} & \text{Proposed Approach (Stable)} \end{cases}$$

Where $I_{base} \neq 0$, ensuring the fan can smoothly transition to the safe speed required by the low load, eliminating Undershoot risk.

---

## 📊 Impact & Benefits

### 1. Efficiency & Standardization
*   Shortened the manual tuning process from **weeks** to a fully automated procedure taking only **hours**.
*   Achieved "reproducibility" in parameter generation, ensuring optimized parameters across different server batches and shortening Time-to-Market.

### 2. Energy Optimization & ESG
*   Through precise PID temperature tracking, the system automatically maintains the **minimum required fan speed**, eliminating ineffective over-cooling.
*   Significantly reduced data center Power Usage Effectiveness (PUE) and carbon emissions, aligning with green computing trends.

### 3. Hardware Reliability
*   Smooth RPM control and the "Non-zero Reset" mechanism effectively prevent violent fan speed oscillations.
*   Reduced **thermal cycling stress** on electronic components, extending the life of fan bearings and chip packaging.

### Step-by-Step Flowchart
![alt text](/postImg/ice_algo/1.jpg)

### Process Flow Diagram
![alt text](/postImg/ice_algo/2.jpg)

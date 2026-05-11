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
thumbnailImage: /postImg/ice_algo/thumbnail.png
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

This project addresses two common issues in server cooling control: conservative open-loop fan curves and the time cost of manual PID tuning. I developed an **Automated Thermal Characteristic Identification System** to make thermal testing and parameter derivation more repeatable.

<!--more-->

The system combines automation scripts, chamber tests, and steady-state thermal profiling. Instead of tuning PID coefficients only by experience, it records thermal equilibrium points across load and fan-speed conditions, then derives a set of control parameters from the measured profile.

The main technical focus is:

1. **Thermal Profile Construction**: Build a repeatable profile from load, fan-speed, and temperature data collected during chamber tests.

2. **PID Parameter Derivation**: Use a parameter correlation model and a non-zero integral reset strategy to reduce undershoot and oscillation during sudden load changes.

## 📋 Executive Summary

This system integrates **Golang** and **Python** automation scripts to build a server's **Steady-state Thermal Profile** through chamber testing. It uses a parameter correlation model to derive PID parameters. A "Non-zero Integral Reset" mechanism is added for sudden load changes (Load Dump), reducing the risk of fan-speed undershoot and oscillation.

---

## 🛑 Industry Context & Challenges

In the field of server cooling, current mainstream practices face several technical bottlenecks:

### 1. Over-design in Open-loop Control
Traditional "Lookup Table" methods rely solely on fixed RPMs corresponding to temperature ranges. To ensure safety, the industry standard is to set a single cooling curve based on the **Maximum Configuration** supported by the chassis and the **Worst-case Scenario**.
*   **Consequence**: For low-to-mid-range servers, fans may operate in an unnecessary "over-speeding" state for long periods, causing extra energy use and noise.

### 2. Manual Tuning Inefficiency of Traditional PID
Even with closed-loop PID control, parameter settings ($K_p, K_i, K_d$) depend heavily on the experience of senior engineers through trial and error.
*   **Consequence**: Lack of standardized system identification processes can lead to weeks of tuning and lower reproducibility across server units.

### 3. Integral Windup & Instability
In Load Dump scenarios, traditional PID is prone to accumulating excessive error in the integral term, causing fan speed to drop too sharply (Undershoot) or even oscillate, affecting cooling stability.

---

## 🛠️ Technical Solution

This method proposes an **Automated Control Parameter Generation Flow Based on Steady-State Thermal Profile Data Structures**, moving cooling control from pure experience-based tuning toward data-assisted parameter derivation.

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
*   Improved reproducibility in parameter generation, making it easier to apply a consistent derivation process across server batches.

### 2. Energy Optimization & ESG
*   Through PID temperature tracking, the system can aim for fan speeds closer to actual thermal demand, reducing unnecessary over-cooling.
*   Helps reduce avoidable fan power consumption and supports later energy-efficiency optimization.

### 3. Hardware Reliability
*   Smooth RPM control and the "Non-zero Reset" mechanism effectively prevent violent fan speed oscillations.
*   Reduced **thermal cycling stress** on electronic components, extending the life of fan bearings and chip packaging.

### Step-by-Step Flowchart
![PID control test result diagram](/postImg/ice_algo/1.jpg)

### Process Flow Diagram
![PID control parameter analysis diagram](/postImg/ice_algo/2.jpg)

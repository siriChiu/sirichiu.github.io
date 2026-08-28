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
- Golang
- Python
- IPMI
- Linux
- Server BMC
thumbnailImagePosition: left
thumbnailImage: /postImg/ice_algo/thumbnail-v2.png
katex: true
---

This project connects an environmental chamber, server BMC, and automation controller in a test loop. It first builds a steady-state thermal profile, then derives PID parameters from profile slope and system gain. The method addresses both time-consuming manual tuning and integral-state behavior that can cause RPM undershoot or oscillation after a load dump.

<!--more-->

> This case study is part of my [Advantech software-engineering portfolio](/en/job_exp_advantech/). It presents the method and data flow while excluding coefficients, equipment configurations, thresholds, and internal test data.

## Problem Context

A single open-loop lookup table is commonly based on a chassis’s maximum configuration and worst-case environment. Lower configurations can therefore run fans above their immediate thermal demand. Moving to closed-loop PID does not by itself solve repeatability if `Kp`, `Ki`, and `Kd` still depend on repeated trial and error.

A second risk appears after a load dump. As workload and temperature fall rapidly, accumulated integral state can drive fan RPM too low or introduce oscillation. The project therefore separates **offline thermal identification** from **BMC runtime control**.

![Thermal identification, parameter derivation, and BMC runtime control loop](/postImg/ice_algo/thermal-control-loop.svg)

## Architecture and My Contribution

- **Host controller:** Golang orchestration coordinates SUT connections, workload points, and fan sweeps; Shell/Python support low-level commands, data cleaning, and plotting.
- **SUT / BMC:** The BMC accepts RPM commands and returns temperature, fan, and other sensor data.
- **Environmental chamber:** Controls ambient context so measurement points can be compared under known conditions.
- **Method design:** Steady-state profile construction, control-parameter derivation, and a non-zero integral-reset path for load dumps.

![Conceptual host, BMC/SUT, and chamber architecture](/postImg/ice_algo/0.jpg)
*Conceptual architecture, not a measurement screenshot.*

## Offline Identification: Building the Thermal Profile

Automation selects multiple load points `Li` from idle to full load and steps fan speed `ω` at each point. When it observes:

$$\frac{dT}{dt} \approx 0$$

it treats the state as thermal equilibrium and records workload, fan speed/RPM, temperature, ambient temperature, and temperature rate. Repeating the sweep produces a steady-state thermal characteristic profile from which response slope and system gain can be calculated.

![Automated thermal-characterization test flow](/postImg/ice_algo/1.jpg)
*Existing process diagram from test conditions through equilibrium detection and data recording; it is not a PID result curve.*

The public description does not disclose equilibrium tolerance, observation window, sampling cadence, load grid, or fan steps. `dT/dt ≈ 0` is therefore a method condition, not an unrestricted accuracy guarantee.

## Parameter Derivation and Deployment

The system determines proportional gain from profile slope and system gain, then applies a defined parameter-correlation model to derive the integral and derivative terms:

$$K_p = f(\text{Slope}_{profile}, \text{Gain}_{system})$$

$$K_i, K_d = \mathcal{M}(K_p)$$

The actual `f` and `M` formulas are not public. The design keeps all three parameters tied to one thermal-characterization context; it does not prove a globally optimal result for every server configuration. Generated values proceed through engineering validation before being handed to BMC firmware.

![PID parameter generation and BMC deployment flow](/postImg/ice_algo/2.jpg)
*Existing diagram showing profile input, parameter generation, and firmware handoff.*

## Runtime: Non-Zero Integral Reset

When load-dump behavior produces a sharp error change, the controller resets the integral term to a dynamically calculated non-zero base rather than zero:

$$I_{new}=I_{base},\quad I_{base}\neq0$$

The design intent is to retain the safe fan speed still required at lower load and reduce undershoot and oscillation risk. No public comparison curve or lifetime study supports claiming complete elimination of undershoot or longer fan-bearing/chip-package life.

## Validation, Impact, and Limits

In the originally described internal tuning context, automation reduced a manual process that could take **weeks** to **hours**. That figure applies to the stated workflow, not a cross-platform benchmark. The profile and derivation steps also make the procedure more consistent, although reproducibility across units still depends on configuration, environment, and statistical validation.

PID temperature tracking can be used to pursue less unnecessary over-cooling. This is a control objective, not a publicly validated fixed energy-saving percentage. Safe deployment still requires temperature and RPM bounds, sensor-fault handling, chamber-failure handling, and rollback behavior; confidential implementation details are omitted.

## Stack

**Golang · Python · Shell · BMC/IPMI · Environmental chamber · Thermal profiling · PID control**

---
title: Digital Signal Processing & Firmware Engineer
slug: job_exp_sentos
date: 2021-10-01
categories:
- Personal Experience
tags:
- C#
- C++
- MATLAB
- Automation
- UI/UX
- Optimization
- Numerical Analysis
- Ultrasound
thumbnailImagePosition: left
thumbnailImage: /postImg/job_sentos/thumbnail-v2.png
katex: true
---

At Sentons Taiwan, I worked on ultrasound touch-signal analysis, calibration tooling, and C++ firmware implementation, while supporting customer-requested features and issues during validation and mass-production stages. The central engineering path was to turn measured waveforms into reviewable parameters and deliver them safely to firmware.

<!--more-->

## Role and Scope

**Sentons Taiwan Branch | Digital Signal Processing & Firmware Engineer | 2021/10 – 2022/09**

My responsibilities spanned MATLAB signal research, C# WPF tooling, device communication, and C++ firmware. This article describes my contribution to that workflow without disclosing customers, product models, production yield, or quantitative outcomes.

![Engineering flow from ultrasound signal through waveform analysis to C++ firmware](/postImg/job_sentos/signal-to-firmware-flow.svg)

## Problem: Calibration Depends on Context

Ultrasound touch parameters can vary with material, hardware, and environmental conditions. Editing configuration files directly creates a cumbersome workflow and makes it harder to review the gesture, captured waveform, and final parameter choice in one context.

My work established a clearer signal-to-firmware path: capture a guided gesture, visualize and analyze its waveform, identify candidate filter bands, and hand validated parameters or features to firmware.

## C# WPF Calibration and Device Tooling

I developed a graphical tool and SDK with **C# WPF**, integrating device communication, ultrasound-signal display, and parameter configuration. The interaction guided a user through gestures such as left/right swipes, analyzed the captured waveform, and proposed a candidate filter frequency. This reduced the need to edit complex configuration files directly.

The tool assisted engineering and validation workflows; it was not a claim that one click produced a universal optimum across every material and environment. No public timing, accuracy, or production-line comparison is available, so the outcome is framed as a workflow contribution rather than a measured improvement.

## From DSP Analysis to Firmware

- **MATLAB / DSP:** Time- and frequency-domain analysis, ultrasound simulation, linear and nonlinear filtering, and touch-algorithm research.
- **Parameter validation:** Compare gesture waveforms and candidate settings, then prepare usable parameters for handoff.
- **C++ firmware:** Implement validated parameters and customer-requested features such as virtual-button triggers.
- **Tooling layer:** Connect signals, device communication, visualization, and configuration through the C# GUI/SDK.

## Productization Support and Collaboration

I contributed to requested software and firmware features and supported issue reproduction, evidence gathering, firmware fixes, and escalation during validation and mass-production stages. I also aligned technical details with US colleagues and management through English writing and meetings. These were team activities; I do not claim sole ownership of a product integration or production outcome.

## Signal-Calibration and Filtering Illustrations

![Calibration-flow illustration for finding a candidate filter frequency from a guided swipe](/postImg/job_sentos/1.jpg)
*Concept illustration: places a guided gesture, waveform, and candidate filter frequency in one interaction context. It is not an actual measurement screenshot or accuracy evidence.*

![Illustration of a raw signal passing through a custom filter into a trigger signal](/postImg/job_sentos/2.jpg)
*Concept illustration: shows the engineering relationship among the raw signal, filter, and clean trigger signal. Actual parameters still require device- and environment-specific validation.*

## Validation Boundary and Lessons

This role taught me that DSP productization is not only about choosing an algorithm. It also requires a reproducible handoff from measurement and analysis through parameter review and firmware deployment. Tooling should preserve waveform and configuration context, and changes in material, hardware, or environment still require revalidation rather than extrapolation from one case.

| Layer | Technology | Output |
| --- | --- | --- |
| Signal research | MATLAB, time/frequency analysis, filtering | Waveform analysis and candidate parameters |
| Engineering tool | C#, WPF, SDK, device communication | Graphical calibration and test workflow |
| Product implementation | C/C++, firmware | Validated parameters and features |
| Collaboration | English technical communication, issue analysis | Reproducible evidence and fix handoff |

---
title: Software Engineer
slug: job_exp_advantech
date: 2026-02-01
categories:
- Personal Experience
tags:
- Golang
- Python
- React
- Docker
- Drone CI
- IPMI
- Server Thermal Algorithm
- FastAPI
- Mathematical Regression
- Automation
- Grafana
- Prometheus
- SNMP
- AI Agent
- SWQA
- Hermes
- BDD
thumbnailImagePosition: left
thumbnailImage: /postImg/job_advantech/thumbnail-v2.png
katex: true
---

At Advantech, my software engineering work spans server thermal control, repeatable stress testing, rack observability, and quality tooling with explicit evidence and write gates. Across these projects, I turn fragmented hardware signals and manual procedures into workflows that can be traced and inspected.

<!--more-->

## Role and Scope

**Advantech | Software Engineer | 2022/11 – Present**

My contributions include Golang/Python automation, BMC/IPMI and SNMP integration, Prometheus/Grafana data pipelines, and AI-assisted quality and development workflows. This work also gave me patent-application experience related to server thermal control; this public article does not disclose filing scope or legal status. The map below presents complementary portfolio themes; it does not imply that every system is integrated into one product.

![Advantech engineering portfolio map covering server systems, automation, and quality engineering](/postImg/job_advantech/engineering-portfolio-map.svg)

## Server-System Case Studies

### 1. PID Parameters from Steady-State Thermal Profiles

A Golang host controller coordinates the SUT/BMC, workload, fan duty, and environmental chamber. It records equilibrium points when `dT/dt ≈ 0`, builds a steady-state thermal profile, and derives control parameters from profile slope and system gain. A non-zero integral reset path is used after load dumps to reduce the risk of RPM undershoot and oscillation.

For the stated internal workflow, this moved a manual tuning process that could take weeks into an automated procedure taking hours. Public material does not disclose tolerances, coefficients, or cross-platform statistics, so I do not generalize this into a universal performance or energy-saving percentage.

→ [Read the server cooling case study](/en/new-pid-for-server/)

### 2. Target-Wattage Stress Testing

I developed a distributed Golang agent/controller flow for scheduling SUTs, executing tests, and returning status and logs. Pre-tests characterize approximately linear CPU power response and saturating Memory/Ethernet response, then estimate a mix of CPU, GPU, RAM, FIO, and Ethernet workload intensities for a target wattage. Grafana charts support long-duration review of thermal, fan, and power behavior. AI-based chart review is an assistive module; no public accuracy result supports autonomous diagnosis.

→ [Read the smart stress-testing case study](/en/smart-stress-testing/)

### 3. Observability across Heterogeneous Rack Equipment

The monitoring agent reads server BMC sensors through IPMI and implements SNMP collectors for Netgear/Cisco switches and Raritan PDUs from their MIBs. It normalizes telemetry into Prometheus metrics for Grafana dashboards and threshold alerts. PDU power switching is a separate control capability, not an action performed by the read-only Prometheus/Grafana path.

→ [Read the rack-monitoring case study](/en/rack-monitor/)

## Quality and Productivity Tooling

### AI Quality Pilot

[AI Quality Pilot](/en/ai-quality-pilot/) is a deterministic-first AI software quality assurance system I designed and developed during my work at Advantech. Hermes provides the conversational entry point, while a Python deterministic engine owns contracts, four-axis test truth, evidence, and remote-write gates. The architecture connects Redmine/Gitea MCP, Pytest/BDD, a Task Graph, and a Knowledge Graph.

The public version generalizes the architecture and excludes internal hosts, accounts, test data, customer information, and lab topology. Its capability matrix is explicitly Supported, Partial, and Planned: this is an evolving gated loop, not a system that delegates every decision and write to an LLM.

### OpenAI-Assisted Review and Email Processing

I also connected Drone CI, Gitea webhooks, and the OpenAI API for automated code-review assistance that flags potential syntax problems in a defined workflow. Another workflow extracts and routes key email content with an LLM. Since no public sample, measurement period, or baseline is available, I do not claim a fixed time-saving percentage.

### Redmine Smart Companion

[Redmine Smart Companion](/en/redmine-tracker/) is a desktop time-entry workflow built with Electron/React/TypeScript and a local FastAPI service. It brings Plan, Track, and Log into one interface and uses PyInstaller plus electron-builder for Windows packaging. History-based prediction remains a roadmap item, not a current AI feature.

## Stack and Engineering Trade-offs

| Area | Technology | Design focus |
| --- | --- | --- |
| Automation and services | Golang, Python, Shell, FastAPI | Replace manual steps with repeatable workflows |
| Server and equipment | BMC, IPMI, SNMP | Normalize heterogeneous device interfaces |
| Observability | Prometheus, Grafana | Separate collection, storage, visualization, and control |
| Quality and DevOps | Hermes, Pytest/BDD, Gitea, Redmine, Drone CI | AI interprets context; deterministic code owns truth and writes |
| Desktop UX | Electron, React, TypeScript | Shorten an existing workflow without overstating roadmap AI |

![Conceptual server thermal-control architecture, not a measurement screenshot](/postImg/ice_algo/0.jpg)
*Conceptual view of the host, BMC/SUT, and environmental-chamber test loop.*

![Grafana stress-test result view](/postImg/smartfan/4D_graph.png)
*Result view used to review power, fan, and temperature variables; the visible chart labels remain the authority for its encodings.*

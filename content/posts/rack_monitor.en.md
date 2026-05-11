---
title: Rack Monitoring System Development
slug: rack-monitor
date: 2026-02-05
categories:
- Professional Technology
tags:
- Golang
- IPMI
- SNMP
- Prometheus
- Grafana
- Netgear
- Cisco
- Raritan
- Network Automation
- Data Visualization

thumbnailImagePosition: left
thumbnailImage: /postImg/rack_monitor/thumbnail.png
katex: true
---

Responsible for the design and implementation of a Rack Monitoring System. The system uses a Golang agent to collect server, switch, and PDU data through IPMI and SNMP, then integrates Prometheus and Grafana to provide real-time visibility into rack equipment status.

<!--more-->

# Software Engineer
**Advantech** | 2022/11 – Present

![Rack monitoring system architecture](/postImg/rack_monitor/architecture.svg)

### 🚀 Core Skills & Expertise
*   ✅ **Protocol Integration**: In-depth research and implementation of IPMI and SNMP (MIB) protocols, customizing data collection for different brand devices.
*   ✅ **Monitoring System Development**: Developed high-performance Agents using Golang, integrating Prometheus time-series database.
*   ✅ **Data Visualization**: Designed Grafana dashboards to transform complex data center metrics into intuitive real-time charts.

### 💼 Key Projects & Contributions

#### Rack Monitoring System Development

1.  **Monitoring Agent Design & Data Collection**
    *   `#Golang`, `#IPMI`, `#SNMP`, `#ipmitool`, `#gosnmp`, `#pysnmp`
    *   **Server Monitoring**: Developed a **Golang** monitoring Agent to communicate directly with BMC via the **IPMI (`ipmitool`)** protocol, capturing server health status and sensor data in real-time.
    *   **Network & Power Monitoring**: Conducted in-depth research on **SNMP MIB (Management Information Base)** files to implement data collectors for specific brands (Switch: **Netgear, Cisco**; PDU: **Raritan**). Utilized `gosnmp` and `pysnmp` packages to ensure cross-platform and cross-device compatibility.
    *   **Comprehensive Metrics**:
        *   **Switch**: Collected Network Traffic, Port On/Off Speed, Stacking Status, Max Speed, Health Status, Temperature, and Fan Speed.
        *   **PDU**: Monitored environmental sensor data (Humidity, Temperature, Vibration, etc.) and Power Control (On/Off).

2.  **Data Pipeline & Storage**
    *   `#Prometheus`, `#TimeSeriesDB`
    *   **Prometheus Integration**: Formatted collected heterogeneous data into unified Prometheus Metrics, establishing a high-efficiency **Time-series Pipeline** to support high-frequency data ingestion and querying.

3.  **Grafana Real-time Monitoring Dashboard**
    *   `#Grafana`, `#Dashboard`, `#Visualization`
    *   **Grafana Dashboard**: Designed multi-dimensional dashboards to show the operational status of rack equipment in one place.
    *   **Anomaly Alerting**: Implemented threshold-based alerting. Visual indicators and notifications help operations personnel locate anomalies faster when overheating, fan failures, or network congestion occurs.

### 🛠️ Tech Stack
*   **Languages**: Golang, Python.
*   **Protocols**: IPMI (ipmitool), SNMP (v2c/v3).
*   **Hardware**: Netgear Switch, Cisco Switch, Raritan PDU.
*   **Observability**: Prometheus, Grafana.

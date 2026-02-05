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
thumbnailImage: /postImg/rack_monitor/1.jpg
katex: true
---

Responsible for the full-stack design and implementation of the Rack Monitoring System. Developed a Golang Agent to collect data from servers, switches, and PDUs via IPMI and SNMP protocols, integrating Prometheus and Grafana to achieve real-time visual monitoring and ensure equipment stability in the data center.

<!--more-->

# Software Engineer
**Advantech** | 2022/11 – Present

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
    *   **War-Room Level Dashboard**: Designed multi-dimensional **Grafana Dashboards** to display the real-time operational status of all equipment within the rack.
    *   **Anomaly Alerting**: implemented threshold-based alerting. Visual indicators (color changes) and notifications allow the operations team to react immediately to critical events like overheating, fan failures, or network congestion.

### 🛠️ Tech Stack
*   **Languages**: Golang, Python.
*   **Protocols**: IPMI (ipmitool), SNMP (v2c/v3).
*   **Hardware**: Netgear Switch, Cisco Switch, Raritan PDU.
*   **Observability**: Prometheus, Grafana.

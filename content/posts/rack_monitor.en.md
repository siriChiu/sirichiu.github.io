---
title: Rack Monitoring System Development
slug: rack-monitor
date: 2025-12-05
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
thumbnailImage: /postImg/rack_monitor/thumbnail-v2.png
katex: true
---

This rack-monitoring system handles the protocol and vendor-MIB differences among server BMCs, switches, and PDUs. A Golang collector gathers data through IPMI/SNMP, normalizes it into Prometheus metrics, and gives Grafana a unified source for equipment status and threshold alerts.

<!--more-->

> This case study belongs to my [Advantech software-engineering portfolio](/en/job_exp_advantech/). Its focus is heterogeneous-device observability, not predictive control.

## Problem: Each Equipment Class Speaks Differently

Servers, network switches, and PDUs expose different fields and may use different protocols, SNMP versions, MIBs, and naming conventions. If each device is visible only through its own interface, engineers cannot easily compare health, network, environmental, and power context in one view.

The central design decision was to keep protocol adaptation and metric normalization in the collector layer, so the time-series backend and dashboards do not need to understand every vendor’s raw format.

![Observability pipeline from IPMI/SNMP equipment to Prometheus and Grafana](/postImg/rack_monitor/observability-pipeline-v2.svg)

## Architecture and Data Flow

1. **Server / BMC adapter:** A Golang agent invokes IPMI/`ipmitool` to read health and sensor data.
2. **Switch adapters:** Collectors implement fields from Netgear and Cisco SNMP MIBs with `gosnmp`/`pysnmp`.
3. **PDU adapter:** A Raritan MIB provides environmental telemetry; the public description separately lists power on/off control.
4. **Normalization:** The collector maps heterogeneous values into consistent Prometheus metrics.
5. **Observe:** Prometheus stores time series, Grafana presents dashboards, and threshold rules support alerts for overheating, fan anomalies, and network congestion.

![Existing rack-monitoring architecture diagram](/postImg/rack_monitor/architecture.svg)
*Architecture diagram of the read-only telemetry path through device adapters, collector, Prometheus, and Grafana.*

## Described Telemetry Scope

| Equipment | Protocol | Publicly described fields |
| --- | --- | --- |
| Server / BMC | IPMI | Health status and sensor data |
| Netgear / Cisco switch | SNMP | Traffic, port state/speed, stacking, maximum speed, health, temperature, fan speed |
| Raritan PDU | SNMP | Humidity, temperature, vibration, and other environmental sensors |

Supported SNMP versions are **v2c/v3**. Fields from different devices are not inherently equivalent; normalization should retain device class and source so similarly named values with different semantics are not mixed.

## Safety Boundary between Control and Observability

The public description mentions PDU power on/off, while the existing architecture only establishes a one-way metrics path. Power switching should be treated as a separate control path with authentication, authorization, confirmation, and audit—not as an action performed directly by Grafana or Prometheus.

Likewise, “real time” here means a continuously updated monitoring view. No polling interval, latency, or retention data is public, so the project does not claim a particular real-time SLA or deployment scale.

## Validation and Limitations

The supported implementation story is: research the MIBs for named vendors, implement collectors with Golang/Python SNMP libraries, expose Prometheus metrics, and integrate Grafana views and threshold-based alerts. Public material does not include metric names, labels, cardinality, supported models/firmware, alert thresholds, notification channels, or a dashboard screenshot.

This case therefore does not claim universal device compatibility or call threshold alerting a predictive model. Deployment still requires validation of credential storage, SNMPv3 configuration, network isolation, polling failure, stale data, and control authorization.

## Stack

**Golang · Python · IPMI (`ipmitool`) · SNMP v2c/v3 · `gosnmp` · `pysnmp` · Prometheus · Grafana**

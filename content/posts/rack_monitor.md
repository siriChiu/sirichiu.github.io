---
title: 機櫃監控系統開發 | Rack Monitoring System Development
slug: rack-monitor
date: 2025-12-05
categories:
- 專業技術
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

負責機櫃監控系統 (Rack Monitoring System) 的設計與實作。系統以 Golang Agent 透過 IPMI 與 SNMP 採集伺服器、Switch 與 PDU 數據，並整合 Prometheus 與 Grafana 建立即時監控視圖，協助掌握機房設備狀態。

<!--more-->


# 軟體工程師 | Software Engineer
**研華科技 (Advantech)** | 2022/11 – Present

![機櫃監控系統架構](/postImg/rack_monitor/architecture.svg)

### 🚀 核心技能 (Core Skills & Expertise)
*   ✅ **協定整合與數據採集 (Protocol Integration)**：深入研究與實作 IPMI 與 SNMP (MIB) 協定，針對不同品牌設備進行客製化數據抓取。
*   ✅ **監控系統開發 (Monitoring System Dev)**：以 Golang 開發高效能 Agent，並整合 Prometheus 時序資料庫。
*   ✅ **資料可視化 (Data Visualization)**：設計 Grafana 儀表板，將複雜的機房數據轉化為直觀的即時圖表。

### 💼 關鍵專案與貢獻 (Key Projects & Contributions)

#### 機櫃監控系統開發 (Rack Monitoring System)

1.  **監控 Agent 設計與數據採集**
    *   `#Golang`, `#IPMI`, `#SNMP`, `#ipmitool`, `#gosnmp`, `#pysnmp`
    *   **伺服器監控**：利用 **Golang** 開發監控 Agent，透過 **IPMI (`ipmitool`)** 協定直接與 BMC 溝通，即時抓取伺服器健康狀態與感測器數據。
    *   **網路設備與電源監控**：深入研究 **SNMP MIB (Management Information Base)** 檔案，針對不同品牌設備（Switch: **Netgear, Cisco**; PDU: **Raritan**）實作數據採集器。使用 `gosnmp` 與 `pysnmp` 套件確保跨平台與跨設備的兼容性。
    *   **全面性指標**：
        *   **Switch**：採集網路流量 (Network Data)、埠口開關速度 (On/Off Speed)、堆疊狀態 (Stacking)、最大傳輸速度 (Max Speed)、健康狀態 (Healthy)、溫度 (Temp) 與風扇轉速 (Fan Speed)。
        *   **PDU**：監控環境感測器數據（濕度 Humidity、溫度 Temp、震動 Vibration 等）以及電源開關控制 (Control On/Off)。

2.  **數據管線與儲存 (Data Pipeline & Storage)**
    *   `#Prometheus`, `#TimeSeriesDB`
    *   **Prometheus 整合**：將採集到的異質數據統一格式化為 Prometheus Metrics，建立高效率的時序數據管線 (Time-series Pipeline)，支援高頻率的數據寫入與查詢。

3.  **Grafana 即時監控儀表板**
    *   `#Grafana`, `#Dashboard`, `#Visualization`
    *   **Grafana Dashboard**：設計多維度儀表板，集中顯示機櫃內設備的運作狀態。
    *   **異常告警**：結合數據閾值設定，當溫度過高、風扇異常或網路流量壅塞時，透過圖表顏色變化與告警通知，讓運維人員能更快定位異常。


### 🛠️ 技術棧 (Tech Stack)
*   **Languages**: Golang, Python.
*   **Protocols**: IPMI (ipmitool), SNMP (v2c/v3).
*   **Hardware**: Netgear Switch, Cisco Switch, Raritan PDU.
*   **Observability**: Prometheus, Grafana.


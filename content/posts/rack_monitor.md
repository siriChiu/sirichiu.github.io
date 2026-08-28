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
thumbnailImage: /postImg/rack_monitor/thumbnail-v2.png
katex: true
---

這套機櫃監控系統處理伺服器 BMC、switch 與 PDU 之間不同的協定和 vendor MIB。Golang collector 透過 IPMI/SNMP 採集資料、正規化為 Prometheus metrics，再由 Grafana 集中呈現設備狀態與門檻告警。

<!--more-->

> 此案例屬於我的[研華軟體工程作品集](/job_exp_advantech/)，重點是異質設備可觀測性，而不是預測控制。

## 問題：每類設備說不同的語言

機櫃中的 server、network switch 與 PDU 不只資料欄位不同，也可能使用不同協定、SNMP version、MIB 與命名方式。若每台設備只能在各自介面查看，工程人員很難用一致視角比較健康狀態、網路、環境與電力資訊。

本專案的核心工作，是把 protocol adaptation 與 metric normalization 放在 collector 層，讓後端時序資料與 dashboard 不必理解每個 vendor 的原始格式。

![從 IPMI/SNMP 設備到 Prometheus 與 Grafana 的可觀測性管線](/postImg/rack_monitor/observability-pipeline-v2.svg)

## 架構與資料流

1. **Server / BMC adapter：** Golang agent 呼叫 IPMI／`ipmitool` 讀取健康狀態與 sensor data。
2. **Switch adapter：** 依 Netgear、Cisco 的 SNMP MIB，以 `gosnmp`／`pysnmp` 實作設備欄位採集。
3. **PDU adapter：** 依 Raritan MIB 取得環境感測資訊；公開描述另包含 power on/off 控制能力。
4. **Normalization：** collector 將異質資料映射為一致的 Prometheus metrics。
5. **Observe：** Prometheus 儲存 time series，Grafana 呈現 dashboard，門檻規則用於過熱、風扇異常或網路壅塞等告警。

![既有機櫃監控架構圖](/postImg/rack_monitor/architecture.svg)
*架構圖：device adapter、collector、Prometheus 與 Grafana 的唯讀 telemetry 路徑。*

## 支援的遙測範圍

| 設備 | 協定 | 公開描述的欄位 |
| --- | --- | --- |
| Server / BMC | IPMI | health status、sensor data |
| Netgear / Cisco switch | SNMP | traffic、port state/speed、stacking、maximum speed、health、temperature、fan speed |
| Raritan PDU | SNMP | humidity、temperature、vibration 等環境 sensor |

SNMP 支援版本為 **v2c/v3**。不同設備的欄位不是天然等價；normalization 必須保留 device class 與來源，避免把相同名稱但不同語意的值混在一起。

## 控制與可觀測性的安全邊界

公開內容提到 PDU power on/off，但既有架構圖只證明單向 metrics pipeline。電源切換應視為獨立 control path，需要身份驗證、授權、確認與稽核，不應暗示 Grafana 或 Prometheus 會直接執行控制。

同樣地，「即時」在這裡表示持續更新的監看視圖；因為未公開 polling interval、延遲與 retention，不宣稱特定 real-time SLA 或規模。

## 驗證與限制

可驗證的成果是：針對指定品牌研究 MIB、以 Golang/Python SNMP library 實作 collector、輸出 Prometheus metrics，並以 Grafana 整合檢視與 threshold-based alerting。公開資料未包含 metric names、labels、cardinality、支援型號／firmware、alert threshold、notification channel 或 dashboard screenshot。

因此，這篇案例不宣稱跨所有設備的普遍相容性，也不把 threshold alert 描述成預測模型。實際部署仍應驗證認證資料保管、SNMPv3 設定、網路隔離、poll failure、stale data 與控制權限。

## 技術棧

**Golang · Python · IPMI (`ipmitool`) · SNMP v2c/v3 · `gosnmp` · `pysnmp` · Prometheus · Grafana**

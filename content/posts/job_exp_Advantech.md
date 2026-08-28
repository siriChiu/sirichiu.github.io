---
title: 軟體工程師 | Software Engineer
slug: job_exp_advantech
date: 2026-02-01
categories:
- 個人經歷
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

我在研華科技擔任軟體工程師，工作橫跨伺服器熱控制、可重複的壓力測試、機櫃可觀測性，以及具證據與寫入閘門的品質工程工具。這些專案的共同重點，是把分散的硬體訊號與人工流程轉換成可追蹤、可檢查的工程工作流。

<!--more-->

## 角色與範圍

**研華科技（Advantech）｜軟體工程師｜2022/11 – Present**

我的主要貢獻包括 Golang/Python 自動化、BMC/IPMI 與 SNMP 協定整合、Prometheus/Grafana 資料管線，以及 AI 輔助的品質與開發流程；這段工作也累積了伺服器熱控制相關的專利申請經驗。本文不揭露申請內容或法律狀態。下圖是作品集層級的關係圖；它呈現互補的工程問題，不代表所有系統已整合成單一產品。

![研華工程作品集地圖：伺服器系統、自動化與品質工程](/postImg/job_advantech/engineering-portfolio-map.svg)

## 伺服器系統案例

### 1. 以穩態熱特徵推導 PID 參數

在環境測試室中，由 Golang host controller 協調 SUT/BMC、負載與風扇轉速，於 `dT/dt ≈ 0` 時記錄平衡點，建立穩態熱特徵資料。系統再依 profile slope 與 system gain 推導控制參數，並在 load dump 路徑加入非零積分重置，以降低轉速下探與震盪風險。

這項方法把原本可能耗時數週的人工反覆調校，轉成特定內部測試流程中可於數小時完成的自動化程序；公開資料未包含容差、係數與跨平台統計，因此不把它延伸解讀為通用效能或節能百分比。

→ [閱讀伺服器散熱控制案例](/new-pid-for-server/)

### 2. 目標瓦數壓力測試

我開發分散式 Golang agent/controller 流程，讓多台 SUT 能被排程、執行測試並回傳狀態與 log。前測試用來描述 CPU 的近似線性功耗，以及 Memory/Ethernet 的飽和型反應，再依目標瓦數推估 CPU、GPU、RAM、FIO 與 Ethernet 等 workload 的組合強度。Grafana 圖表協助回顧溫度、風扇與功率的長時間變化；AI 圖表判讀屬輔助模組，沒有公開準確率或自主診斷證據。

→ [閱讀智慧型自動化壓力測試案例](/smart-stress-testing/)

### 3. 異質機櫃設備的可觀測性

監控 agent 透過 IPMI 讀取伺服器 BMC 感測資料，並依 Netgear/Cisco switch 與 Raritan PDU 的 SNMP MIB 實作採集器。資料正規化為 Prometheus metrics，再由 Grafana 提供儀表板與門檻告警。PDU 電源開關是獨立控制能力，不由 Prometheus/Grafana 的唯讀管線執行。

→ [閱讀機櫃監控案例](/rack-monitor/)

## 品質與生產力工具

### AI Quality Pilot

[AI Quality Pilot](/ai-quality-pilot/) 是我在研華任職期間設計與開發的 deterministic-first AI 軟體品質保證系統。Hermes 提供對話入口；Python deterministic engine 掌管 contract、四軸測試真實狀態、evidence 與 remote-write gate，並連接 Redmine/Gitea MCP、Pytest/BDD、Task Graph 與 Knowledge Graph。

公開版本是去除公司內部 host、帳號、測試資料、客戶資訊與實驗室拓樸後的通用架構。目前能力包含 Supported、Partial 與 Planned 層級，因此它是逐步完成的受控閉環，而不是把所有判斷與寫入都交給 LLM。

### OpenAI 輔助程式碼審查與郵件處理

我也曾以 Drone CI、Gitea webhook 與 OpenAI API 串接自動化程式碼審查，協助在既定流程中提示潛在語法問題；另以 LLM 萃取郵件重點並推送資訊。由於公開資料沒有樣本、期間與基準，這裡不宣稱固定的節省比例。

### Redmine Smart Companion

[Redmine Smart Companion](/redmine-tracker/) 是 Electron/React/TypeScript 與本機 FastAPI 組成的桌面工時流程工具，將 Plan、Track、Log 整理成單一介面，並以 PyInstaller 與 electron-builder 完成 Windows 封裝。歷史資料預測仍是 roadmap，不視為目前功能。

## 技術棧與工程取捨

| 領域 | 技術 | 取捨重點 |
| --- | --- | --- |
| 自動化與服務 | Golang、Python、Shell、FastAPI | 以可重複流程取代人工步驟 |
| 伺服器與設備 | BMC、IPMI、SNMP | 將異質協定轉成一致資料 |
| 可觀測性 | Prometheus、Grafana | 分開採集、儲存、檢視與控制邊界 |
| 品質與 DevOps | Hermes、Pytest/BDD、Gitea、Redmine、Drone CI | AI 輔助理解，規則引擎擁有真實狀態與寫入權 |
| 桌面體驗 | Electron、React、TypeScript | 縮短既有工作流，不誇大未實作的 AI 功能 |

![伺服器熱控制概念架構；此圖為示意而非量測截圖](/postImg/ice_algo/0.jpg)
*概念圖：host、BMC/SUT 與環境測試室之間的熱控制測試迴路。*

![壓力測試 Grafana 結果畫面](/postImg/smartfan/4D_graph.png)
*結果畫面：以多變數圖表回顧功率、風扇與溫度狀態；圖中編碼以實際畫面標示為準。*

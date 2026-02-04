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
- Deep Learning & Machine Learning
- Automation
- UI/UX
- Grafana
- Streamlit
- Prometheus
- Ansible

thumbnailImagePosition: left
thumbnailImage: /postImg/ice_algo/0.jpg
katex: true
---

專精於 全端自動化開發 (Full-Stack Automation)、伺服器熱流演算法 (已申請專利) 與 AI 自動化落地。研發伺服器降溫演算法、開發預測性燒機模組與 OpenAI 代碼審查機器人 (節省 30% Review 時間)，擅長 Golang/Python 全端開發與 DevOps 流程整合

<!--more-->


---
# 軟體工程師 | Software Engineer
**研華科技 (Advantech)** | 2022/11 – Present

### 🚀 核心技能 (Core Skills & Expertise)
*   ✅ **伺服器熱流演算法 (Server Thermal Algorithm)**：專精於溫度控制策略，具備專利申請經驗。
*   ✅ **AI/ML 落地應用 (AI Implementation)**：整合 OpenAI API 於 DevOps 流程，並運用數學回歸模型進行壓力預測。
*   ✅ **全端自動化開發 (Full-Stack Automation)**：熟稔 Python/Golang 後端與 Electron/React 現代化前端架構。
*   ✅ **基礎設施即程式碼 (IaC & DevOps)**：熟悉 Docker, Drone CI, Gitea Webhook 與 BMC/IPMI 協定。

---

### 💼 關鍵專案與貢獻 (Key Projects & Contributions)

#### 工業/AI伺服器之風扇控制相關工具開發

1.  **最佳化風扇曲線演算法開發、數據進行蒐集與演算法導入**
    *   `#Golang`, `#BashScript`, `#Algorithm`, `#Fancurve`, `#PIDalgorighm`, `#ipmitool`, `#BMC`
    *   **創新研發**：透過前測試 (Pre-test) 分析伺服器耐力極限，自動化生成最適化的溫控演算法。
    *   **量化成效**：經實測驗證，新演算法相較於傳統 Openloop 控制策略，**效能提升約 20%~40%**，有效優化散熱效率與節能表現（專利申請中）。

2.  **自動化伺服器壓力測試工具開發**
    *   `#Golang`, `#BashScript`, `#Algorithm`
    *   **智慧燒機預測**：針對燒機測試 (Burn-in)，建立 **數學回歸模型 (Mathematical Regression Model)**。將各類壓力腳本（CPU, GPU, RAM, FIO, ETH）作為輸入變數，精準預測並組合出目標負載（如精確控制在 50% 或 100% Loading）。
    *   **解決痛點**：解決了傳統測試難以精確控制負載的問題，為風流評估提供高可信度的測試環境。

3.  **即時感測器數據資料繪製與保存**
    *   `#Python`, `#Golang`, `#MySQL`, `#Grafana`
    *   **多機同步監控**：開發自動化控制工具，實現**一對多（1-to-5）**伺服器的即時同步監控。
    *   **可視化儀表板**：整合 Grafana 與 MySQL，即時繪製並保存感測器數據，提供研發人員直觀的效能分析視圖。

4.  **遠端/本機端伺服器測試工具開發**
    *   `#Golang`, `#Python`, `#Linux`, `#BashScript`
    *   **混合架構設計**：結合 Golang 的高併發特性與 Python 的豐富生態，構建高效率的遠端/本機測試載具。
    *   **跨平台支援**：確保工具在不同 Linux 發行版與硬體架構下的相容性與穩定性。

#### GenAI 與公司工作效率提升之創造

1.  **基於 OpenAI API，Gitea Action 實現自動化代碼審查工具**
    *   `#AI`, `#LLM`, `#automatic`, `#workflow`, `#codereview`, `#restfulapi`, `#CI/CD`
    *   **DevOps 整合**：利用 Drone CI 與 Gitea Webhook 建立觸發事件，整合 **OpenAI API** 開發自動化審查機器人。
    *   **流程優化**：成功攔截潛在語法錯誤，並 **減少資深工程師約 30% 的 Code Review 時間**，顯著提升開發團隊的交付效率。

2.  **GenAI 電子郵件內容萃取與自動推送**
    *   `#AI`, `#LLM`, `#workflow`, `#CI`
    *   **自動化流程**：利用 LLM 技術自動分析並萃取關鍵電子郵件內容，實現智慧化的資訊分發與推送，減少人工篩選的時間成本。

---

### 🛠️ 技術棧 (Tech Stack)
*   **Languages**: Golang, Python, JavaScript/TypeScript (React).
*   **AI/ML**: Mathematical Regression, OpenAI API, Deep Learning Basics.
*   **Infrastructure**: Docker, Drone CI, IPMI, Server BMC.
*   **Frameworks**: FastAPI, Electron.

---

### 🖼️ 專案示意圖 (Reference Images)

**Image 1: 伺服器降溫演算法與專利**
![alt text](/postImg/ice_algo/0.jpg)

**Image 2: 智慧燒機預測系統**
![alt text](/postImg/smartfan/4D_graph.png)

**Image 3: 混合架構生產力工具**
![alt text](/postImg/Redmine-tracker/main.jpg)
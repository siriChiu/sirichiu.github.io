---
title: Redmine Smart Companion：重塑工時管理的桌面自動化工具
date: 2025-01-27
categories:
- 專業技術
tags:
- Vibe Coding
- Deep Learning/Machine Learning
- Redmine
- Python
- React
- Electron
- FastAPI
- Automation
- CI/CD

thumbnailImagePosition: left
thumbnailImage: /postImg/Redmine-tracker/main.jpg
---

本專案開發了一款跨平台的桌面應用程式，旨在解決工程師在使用 Redmine 系統記錄工時面臨的「操作繁瑣」與「流程斷裂」問題。

<!--more-->

---

## 📋 專案摘要 (Abstract)

> **這是一款結合現代化 UI 與 Python 強大後端的桌面生產力工具。**

透過結合 **Electron (React)** 的現代化前端與 **Python FastAPI** 的強大後端，我打造了一個 **「混合架構 (Hybrid Architecture)」**
解決方案。

此工具將原本需 10 個步驟的網頁操作簡化為「一鍵完成」，並引入視覺化儀表板與智慧排程功能。這不僅消除了記錄工時的作業感，更為未來導入 AI 工時預測功能預留了架構彈性，成功將被動的行政工作轉化為高效率的生產力管理體驗。

---

## 🛑 問題與背景 (The Problem)

在軟體開發流程中，Redmine 是強大的專案管理工具，但其「工時記錄 (Time Logging)」體驗卻相當過時且不人性化：

* **⏳ 高昂的時間成本：** 記錄一筆工時平均需要點擊與跳轉約 10 次，工程師每天需花費約 30 分鐘處理此類行政瑣事。
* **💔 流程斷裂 (Context Switch)：** 為了記錄工時，開發者必須中斷心流 (Flow)，切換瀏覽器分頁，導致工作效率下降。
* **📉 缺乏反饋：** 原生介面缺乏即時的數據可視化，使用者難以掌握當週工時狀態，容易造成漏記或超時。

---

## 💡 解決方案與體驗設計 (Solution & UX Design)

為了徹底解決上述痛點，我設計了一套 **"Plan ➝ Track ➝ Log"** 的閉環工作流，並採用 **Glassmorphism (毛玻璃特效)** 風格的深色模式 UI，打造沈浸式的桌面體驗。

### 1. 核心工作流 (The "Focus First" Workflow)
* **Plan (規劃):** 透過 **Smart Daily Planner** 與 **Intelligent Profiles** 功能，使用者可預先載入常用的任務模板（如 Daily Standup），一鍵建立每日待辦。
* **Track (追蹤):** 支援拖拉式 (Drag-and-drop) 行事曆介面。系統即時監控工時，並透過視覺化圖表自動標示空檔（如午休時間）。
* **Log (記錄):** 提供 **Automated Workflows**，當任務完成或下班時間一到，系統自動將本地數據推送至 Redmine API，實現「無感記錄」。

![calender](/postImg/Redmine-Tracker/calender.jpg)

### 2. 可視化儀表板 (Interactive Dashboard)
* 提供 **Weekly Overview** 長條圖，讓使用者一眼掌握本週工時分佈。
* 整合 **Project Deep Dive** 視圖，無須打開瀏覽器即可查看 Issue 的狀態、優先級與歷史討論串。

![main](/postImg/Redmine-Tracker/main.jpg)

---

## 🛠️ 技術深度剖析 (Technical Case Study)

### 1. 創新的混合式架構 (Hybrid Architecture)

不同於傳統 Electron App 僅依賴 Node.js，本專案採用了 **React (Frontend) + Python FastAPI (Backend)** 的並發架構 (Concurrent Architecture)。

* **Frontend:** 使用 **Vite + React + TypeScript** 構建，確保極致的渲染效能與型別安全。
* **Backend:** 使用 **Python FastAPI** 作為本地伺服器，處理與 Redmine API 的交互及資料邏輯。

#### 🤔 為什麼選擇這種架構？ (Why Python Backend?)
1.  **既有資產整合 (Legacy Integration):** 能夠直接封裝並重用我先前編寫的高效 Python 自動化腳本，大幅縮短開發週期。
2.  **AI 擴充性 (AI Readiness):** 為了未來的 Roadmap 做準備。Python 擁有最豐富的 AI/ML 生態系，這層架構讓我未來能輕鬆導入 `Scikit-learn` 或 `Pandas`，實現「基於歷史數據的工時智慧預測」功能，而不必重構整個後端。



### 2. 桌面端封裝與發布 (Packaging & Distribution)

將 Python 環境打包進 Electron 是一大技術挑戰。我建立了一套自動化的 Build Pipeline：

* **後端編譯:** 使用 **PyInstaller** 將 Python FastAPI 環境與依賴庫編譯為單一執行檔 (`backend.exe`)，解決了使用者無需安裝 Python 環境的問題。
* **跨進程通訊:** Electron Main Process 負責管理 Python 子進程的生命週期（啟動與優雅關閉），並處理 Port 8000 的佔用衝突 (Errno 10048)。
* **安裝包製作:** 最終透過 **electron-builder** 將 React 前端與 Python 執行檔打包為標準的 Windows 安裝程式 (`.exe`)。

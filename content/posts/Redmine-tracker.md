---
title: Redmine Smart Companion：以桌面工作流重新設計工時記錄體驗
slug: redmine-tracker
date: 2025-01-27
categories:
- 專業技術
tags:
- Redmine
- Python
- FastAPI
- React
- TypeScript
- Electron
- PyInstaller
- Desktop App
- Automation
- UI/UX
- CI/CD
thumbnailImagePosition: left
thumbnailImage: /postImg/Redmine-Tracker/thumbnail-v2.png
---

Redmine Smart Companion 是一套以 **Electron／React／TypeScript** 前端搭配本機 **Python FastAPI** 後端的桌面工時工具。我把原本分散在瀏覽器頁面中的規劃、追蹤與登錄步驟，整理成「Plan → Track → Review → Log」工作流，並以 Windows 安裝包交付。

<!--more-->

## 問題脈絡：工時登錄打斷工程工作流

Redmine 能管理 issue 與工時，但在我觀察的既有流程中，建立一筆紀錄可能涉及約十次點擊與頁面跳轉；「每天約 30 分鐘」是當時使用情境的經驗值，不是跨版本、跨團隊的正式 benchmark。

真正的問題不只在點擊次數，而是資訊散落：工程師先在其他地方安排工作，再回到 Redmine 選 project、issue、日期、時數與備註，最後還要另外確認本週是否漏記。每次切換都會中斷目前的開發脈絡。

![Redmine Smart Companion 的 Plan、Track、Review 與 Log 桌面工作流](/postImg/Redmine-Tracker/plan-track-log-flow.svg)

## 體驗設計：Plan → Track → Review → Log

1. **Plan：** 以 daily planner 與常用 profile 建立工作項目，減少重複輸入。
2. **Track：** 透過週曆與拖放式排程整理工作區段，並保留午休或未分配時段。
3. **Review：** 由 weekly overview 檢查每日與每週時數分布，回到 issue 脈絡確認內容。
4. **Log：** 將本機整理的資料送往 Redmine API，完成工時登錄。

![Redmine Smart Companion 週曆排程畫面](/postImg/Redmine-Tracker/calender.jpg)
*實際介面畫面：以週曆呈現工作區段與空檔；截圖能證明 UI surface，但不單獨證明遠端寫入結果。*

![Redmine Smart Companion 儀表板](/postImg/Redmine-Tracker/main.jpg)
*實際介面畫面：顯示當日／每週摘要與 issue 分布，用來協助登錄前後的人工檢查。*

## 混合式桌面架構

系統刻意把桌面體驗與既有 Python 自動化資產分開：

| 層次 | 技術 | 責任 |
| --- | --- | --- |
| Renderer | Vite、React、TypeScript | Calendar、dashboard、profiles 與使用者互動 |
| Desktop shell | Electron main process | 視窗、應用程式生命週期與 Python 子程序管理 |
| Local service | FastAPI、Python | Redmine API 封裝、資料邏輯與既有腳本整合 |
| Remote system | Redmine REST API | Issue context 與工時資料的系統來源 |

選擇 Python backend 的主要理由，是可以重用既有自動化程式，並讓 UI 不必直接承擔 Redmine 資料邏輯。這也保留未來使用 Pandas／Scikit-learn 分析歷史工時的可能性；**歷史工時預測仍是 roadmap，不是目前已驗證的 AI 功能。**

## Windows 封裝與程序生命週期

我使用 **PyInstaller** 將 FastAPI 與 Python 依賴封裝成 `backend.exe`，由 Electron main process 負責啟動與結束本機服務，再以 **electron-builder** 產生 Windows 安裝程式。這個流程讓使用者不必另外安裝 Python，也需要處理 backend 啟動失敗、graceful shutdown 與 port 8000 衝突（例如 `Errno 10048`）。

原始文章曾以「跨平台」描述桌面架構，但目前公開證據只涵蓋 Windows 執行檔與安裝包；因此這篇文章只宣稱 **Windows desktop packaging**，不把架構可攜性等同於已完成 macOS／Linux 發布。

## 遠端寫入與安全邊界

工時登錄會改變 Redmine 的正式資料，因此不能只以「無感自動化」描述。公開內容尚未交代 API key 儲存、renderer 與 localhost backend 的認證、TLS、log redaction、送出前預覽、重試去重與錯誤回復等細節。若要正式部署，至少應具備：

- 明確顯示 project、issue、日期、時數與 comment，再由使用者確認。
- 避免重試造成重複工時，並保留 Redmine 回應與錯誤狀態。
- 限制本機服務 bind address，保護 credential，且不把 token 寫入 log。
- 將「本機草稿」與「已成功寫入 Redmine」分成不同狀態。

這些是遠端寫入的必要工程邊界；在缺少程式碼與測試證據時，我不把它們宣稱為目前版本全部完成的能力。

## 可驗證成果與限制

目前可由公開內容支持的成果，是桌面 planner/calendar/dashboard 的介面、React + Electron + FastAPI 的混合式設計，以及 Windows backend／installer 封裝流程。公開資料未提供 build log、release artifact、API integration test、操作時間對照或使用者研究，因此不宣稱固定的生產力提升比例。

若要量化下一版成效，我會追蹤每筆工時的 median interactions／elapsed time、重複或失敗率、sync 成功率、啟動時間，以及人工修正次數。

## 技術棧

**Electron · Vite · React · TypeScript · Python · FastAPI · PyInstaller · electron-builder · Redmine REST API**

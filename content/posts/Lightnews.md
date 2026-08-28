---
title: 全自動化技術資訊聚合平台：基於 n8n 與本地 LLM 的內容工作流
slug: lightnews
date: 2025-08-15
categories:
- 專業技術
tags:
- Automation
- n8n
- Ollama
- Deep Learning & Machine Learning
- Web Scraping
- RSS
- WordPress
thumbnailImagePosition: left
thumbnailImage: /postImg/lightnews/thumbnail-v2.png
---

Lightnews 是一套架設於 Linux 的技術內容工作流：n8n 監看 RSS、清理網頁、呼叫 Ollama 本地模型完成摘要與繁體中文翻譯，再經圖片檢索與 WordPress REST API 產生可審閱的文章。它把重複性處理自動化，但保留編輯判斷。

<!--more-->

## 專案脈絡

人工整理國際技術文章需要在來源追蹤、摘要、翻譯、分類、配圖與 CMS 之間來回切換。原文章把「數天到數週」視為可能的資訊延遲；這是工作流觀察，不是正式量測的服務指標。

本專案的目標是先產生結構一致的繁體中文草稿，讓人工把時間放在來源、技術語意、授權與發布判斷，而不是重複搬運欄位。

![Lightnews 信任邊界與編輯管線：外部來源、本機推論、CMS 草稿與人工審閱](/postImg/lightnews/editorial-pipeline-v2.svg)

## 架構與資料流

1. **RSS 監看與內容擷取：** n8n 監看選定來源；發現新文章後抓取頁面並移除廣告與無關 HTML。
2. **本地文字推論：** 清理後的文字交給 Ollama 上的 `gpt-oss`，產生摘要、繁體中文翻譯、技術分類與視覺關鍵字。
3. **外部圖片檢索：** 以視覺關鍵字呼叫 Unsplash API，再依下載量與相關度訊號排序／選擇候選圖。
4. **CMS 交付：** n8n 整理標題、內文、標籤與圖片連結，透過 WordPress REST API 建立草稿或依流程發布。
5. **編輯閘門：** 草稿仍需檢查來源語意、翻譯、圖片授權／標示與是否適合公開。

這裡的「本地」只指文字推論在自管 Linux host 上執行，降低對外部 LLM API 的依賴。RSS/原始網頁、Unsplash 與 WordPress 仍跨越外部服務邊界，因此不是完全離線或全私有的系統。

![既有 Lightnews 自動化處理流程圖](/postImg/lightnews/pipeline.svg)
*架構圖：RSS、清理、本地 LLM、圖片選擇與 WordPress 草稿的主要節點。*

## 技術決策

### 為什麼使用 n8n

n8n 讓 API 節點、條件分支與失敗路徑能在同一個 orchestration surface 中閱讀，適合這種整合型流程。它取代零散 crontab 腳本的角色，但不代表節點本身免除重試、驗證與監控需求。

### 為什麼使用本地 LLM

摘要、翻譯與分類會處理大量文字，本地 Ollama 可降低文字送往第三方 LLM API 的需求，也保留模型與部署控制權。這個選擇不等於翻譯必然準確；公開資料沒有基準集或人工評分，因此輸出仍是待審草稿。

### 圖片與發布邊界

Unsplash 的下載量與相關度只能作為候選排序訊號，不能證明圖片是「最佳」或已自動滿足每個授權／標示條件。WordPress API 具備建立草稿與發布能力，但較安全的預設敘事是先建立可審閱輸出。

## 可見成果與限制

以下畫面證明已有可瀏覽的繁體中文網站介面；它不代表 uptime、吞吐量、翻譯品質或編輯錯誤率已被量化。

![Lightnews 繁體中文技術新聞網站畫面](/postImg/lightnews/1.jpg)
*實際網站畫面：可見文章、分類與發佈時間等閱讀介面。*

目前公開內容未提供 n8n workflow export、錯誤重試策略、更新頻率、內容品質評估或授權稽核紀錄。後續若要把系統成效量化，應追蹤每篇人工審閱時間、翻譯修訂率、來源與圖片授權完整度，以及工作流失敗／重試率。

## 技術棧

**Linux · n8n · Ollama (`gpt-oss`) · RSS · Web extraction · Unsplash API · WordPress REST API**

## 線上網站

> **外部內容提醒：** 下方 iframe 會載入 `lightnews.tw` 的外部內容，可能受網站可用性、Cookie 或瀏覽器安全設定影響。

若無法顯示嵌入頁面，請使用可見的備援連結：[前往 Lightnews 科技輕鬆報](https://lightnews.tw/)。

<iframe src="https://lightnews.tw/" title="Lightnews 科技輕鬆報外部網站" width="100%" height="500" loading="lazy" style="border:0;max-width:100%;"></iframe>

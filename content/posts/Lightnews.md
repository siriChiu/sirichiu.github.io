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
thumbnailImage: /postImg/lightnews/1.jpg
---

本專案構建了一套端到端 (End-to-End) 的自動化內容發布系統，旨在解決繁體中文圈與國際技術社群之間的「資訊落差」。

<!--more-->


## 📋 專案摘要 (Abstract)

傳統的技術新知傳播依賴人工翻譯與搬運，往往存在數天甚至數週的時間延遲。為了解決此問題，我利用 Linux 伺服器架設 **n8n** 自動化流程，並整合 **Ollama 本地大型語言模型 (gpt-oss)**，實現了從 RSS 監聽、內容擷取、AI 摘要翻譯、智慧配圖到最終 WordPress 發布的全無人值守工作流。此系統能即時將國外第一手技術資訊轉化為高品質的中文內容，大幅提升了資訊獲取的效率與廣度。

---

## 🛠️ 技術深度剖析 (Technical Case Study)

### 1. 系統架構與基礎設施 (Infrastructure)

為了確保系統的穩定性與隱私安全性，本專案採用全私有化部署方案：

* **Linux Server:** 作為運算與服務託管的基礎環境。
* **Workflow Orchestration (n8n):** 使用 n8n 作為自動化中樞，負責串接各個 API 節點與邏輯判斷，取代傳統繁瑣的 Python Crontab 腳本。
* **Local LLM Inference (Ollama):** 部署 Ollama 框架運行 `gpt-oss` 模型，讓大量文本處理無需依賴昂貴且有隱私疑慮的外部 API。

### 2. 核心技術：AI 驅動的內容處理管線 (AI-Driven Content Pipeline)

本系統的核心在於將非結構化的網頁內容，透過 AI 轉化為結構化的發布格式。

#### 2.1 智慧擷取與認知處理 (Ingestion & Cognitive Processing)
流程始於對特定技術領域的 RSS 監控。一旦發現新文章，系統即觸發以下處理鏈：

1.  **內容清洗:** 自動爬取原始網頁，去除廣告與無關 HTML 標籤。
2.  **本地 LLM 推論:** 將清洗後的文本輸入至 Ollama (`gpt-oss`) 進行多維度處理：
    * **摘要生成 (Summarization):** 提煉文章核心技術點。
    * **跨語言翻譯 (Translation):** 將英文技術術語準確轉換為繁體中文。
    * **自動分類 (Auto-Tagging):** 根據內文語意，自動判斷文章所屬的技術領域（如：DevOps, AI, Security）並生成對應標籤。



#### 2.2 上下文感知的媒體檢索 (Context-Aware Media Retrieval)
為了讓文章圖文並茂，我設計了一套「文轉圖」的檢索邏輯，而非單純使用隨機圖片。

1.  **視覺意圖識別:** 透過 LLM 分析文章內文，生成一組精準的英文「視覺關鍵字 (Visual Keywords)」。
2.  **API 媒合:** 系統自動呼叫圖庫 API (Unsplash)，利用上述關鍵字進行檢索。
3.  **最佳化篩選:** 根據圖片的下載量與相關度評分，自動選取最合適的一張作為文章封面圖 (Featured Image)。

### 3. 自動化交付 (Automated Delivery)

最後階段，n8n 將處理好的標題、內文、標籤與圖片連結，透過 **WordPress REST API** 自動建立草稿或直接發布。這不僅標準化了文章格式，更實現了 24 小時不間斷的資訊更新。

---

### 總結 (Conclusion)

這個專案展示了如何利用 **Low-Code 工具 (n8n)** 與 **Local LLM** 技術，快速構建具備商業價值的自動化系統。它不僅解決了資訊時效性的問題，更證明了在低成本硬體上運行複雜 AI 工作流的可行性。


<iframe src="https://lightnews.tw/" width="100%" height="500px" style="border:none;"></iframe>

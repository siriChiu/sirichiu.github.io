---
title: "Fully Automated Tech Information Aggregation Platform: Content Workflow Based on n8n and Local LLM"
slug: lightnews
date: 2025-08-15
categories:
- Professional Technology
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

This project built an end-to-end automated content publishing system, aimed at solving the "information gap" between the Traditional Chinese community and international tech communities.

<!--more-->


## 📋 Abstract

Traditional technical knowledge dissemination relies on manual translation and transfer, often resulting in delays of days or even weeks. To solve this problem, I set up **n8n** automation workflow on a Linux server and integrated **Ollama local large language model (gpt-oss)** to achieve a fully unattended workflow from RSS monitoring, content extraction, AI summary translation, smart image selection, to final WordPress publishing. This system can instantly transform first-hand international technical information into high-quality Chinese content, significantly improving the efficiency and breadth of information acquisition.

---

## 🛠️ Technical Case Study

### 1. System Architecture & Infrastructure

To ensure system stability and privacy security, this project adopted a fully privatized deployment solution:

* **Linux Server:** Serves as the foundational environment for computing and service hosting.
* **Workflow Orchestration (n8n):** Uses n8n as the automation hub, responsible for connecting various API nodes and logical judgments, replacing traditional cumbersome Python Crontab scripts.
* **Local LLM Inference (Ollama):** Deploys Ollama framework running `gpt-oss` model, enabling large-scale text processing without relying on expensive external APIs with privacy concerns.

### 2. Core Technology: AI-Driven Content Pipeline

The core of this system lies in transforming unstructured web content into structured publishing format through AI.

#### 2.1 Ingestion & Cognitive Processing
The workflow begins with RSS monitoring of specific technical domains. Once new articles are discovered, the system triggers the following processing chain:

1.  **Content Cleaning:** Automatically crawls original web pages, removing ads and irrelevant HTML tags.
2.  **Local LLM Inference:** Feeds cleaned text to Ollama (`gpt-oss`) for multi-dimensional processing:
    * **Summarization:** Extracts core technical points from articles.
    * **Translation:** Accurately converts English technical terminology to Traditional Chinese.
    * **Auto-Tagging:** Based on semantic context, automatically determines the technical domain (e.g., DevOps, AI, Security) and generates corresponding tags.



#### 2.2 Context-Aware Media Retrieval
To make articles visually engaging, I designed a "text-to-image" retrieval logic rather than simply using random images.

1.  **Visual Intent Recognition:** LLM analyzes article content to generate a set of precise English "Visual Keywords."
2.  **API Matching:** System automatically calls image library API (Unsplash) using these keywords for search.
3.  **Optimized Selection:** Based on download count and relevance scores, automatically selects the most suitable image as the article's Featured Image.

### 3. Automated Delivery

In the final stage, n8n creates drafts or directly publishes through the **WordPress REST API** using processed titles, content, tags, and image links. This not only standardizes article format but also achieves 24/7 uninterrupted information updates.

---

### Conclusion

This project demonstrates how to use **Low-Code tools (n8n)** and **Local LLM** technology to rapidly build automated systems with commercial value. It not only solves the timeliness of information but also proves the feasibility of running complex AI workflows on low-cost hardware.


<iframe src="https://lightnews.tw/" width="100%" height="500px" style="border:none;"></iframe>

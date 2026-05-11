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
thumbnailImage: /postImg/lightnews/thumbnail.png
---

This project builds an end-to-end automated content publishing workflow to reduce the time gap between international technical sources and Traditional Chinese readers.

<!--more-->


## 📋 Abstract

Technical news curation often depends on manual translation and reposting, which can introduce delays of days or weeks. To reduce that cost, I set up an **n8n** workflow on a Linux server and integrated **Ollama local large language model (gpt-oss)** for RSS monitoring, content extraction, summarization, translation, image retrieval, and WordPress publishing. The system is designed to produce reviewable drafts first, leaving final judgment to a human editor when needed.

---

## 🛠️ Technical Case Study

### 1. System Architecture & Infrastructure

To ensure system stability and privacy security, this project adopted a fully privatized deployment solution:

* **Linux Server:** Serves as the foundational environment for computing and service hosting.
* **Workflow Orchestration (n8n):** Uses n8n as the automation hub, responsible for connecting various API nodes and logical judgments, replacing traditional cumbersome Python Crontab scripts.
* **Local LLM Inference (Ollama):** Runs the `gpt-oss` model through Ollama, reducing dependence on external APIs for large-volume text processing.

![Lightnews automated content pipeline](/postImg/lightnews/pipeline.svg)

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

1.  **Visual Intent Recognition:** LLM analyzes article content to generate searchable English "Visual Keywords."
2.  **API Matching:** System automatically calls image library API (Unsplash) using these keywords for search.
3.  **Optimized Selection:** Based on download count and relevance scores, selects a relevant image as the article's Featured Image.

### 3. Automated Delivery

In the final stage, n8n sends processed titles, content, tags, and image links to the **WordPress REST API** to create drafts or publish posts. This keeps article formatting consistent and supports a steadier update rhythm.

---

### Conclusion

This project demonstrates how **Low-Code tools (n8n)** and **Local LLMs** can support a practical content workflow. The goal is not to replace editorial judgment, but to automate repetitive extraction, summarization, and pre-publishing work so human review can focus on quality control.


<iframe src="https://lightnews.tw/" width="100%" height="500px" style="border:none;"></iframe>

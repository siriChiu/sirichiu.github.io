---
title: 基於 MobileNet 與雲端協同運算的姿態辨識應用
slug: pose detection
date: 2022-04-22
categories:
- 研究生專題
tags: 
- Python
- OpenPose
- MobileNet
- WebSocket
- Cloud Computing
- Deep Learning/Machine Learning
thumbnailImagePosition: left
thumbnailImage: /postImg/pose-detection/1.jpg
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

本專案旨在解決高齡化社會中，長輩缺乏運動動機與數位落差的問題。我們開發了一套基於 AI 肢體辨識的互動遊戲系統，包含「記憶翻牌」與「瑜珈引導」，讓長輩在家中即可透過簡單的設備進行復健與運動。

<!--more-->


---

在技術實作上，針對 OpenPose 模型在一般消費級筆電上運行緩慢（低 FPS）的痛點，本專案提出了一種**「雲端協同運算架構 (Cloud-Edge Collaboration)」**。前端設備僅負責影像採集與渲染，繁重的 AI 推論則透過 **WebSocket** 即時傳輸至 **Google Cloud Platform (GCP)** 上的 **MobileNet + OpenPose** 模型進行處理。此架構成功突破了地端硬體的算力限制，實現了跨平台的低延遲、高幀率即時互動體驗。

---

## 🛑 問題與挑戰 (The Problem)

在開發初期，我們面臨了兩個主要的技術挑戰：

1.  **算力瓶頸 (Hardware Limitation):**
    OpenPose 雖然準確度高，但運算成本極大。在一般的非電競筆電（無獨立 GPU）上運行時，即便使用了輕量化的 MobileNet 作為骨幹，FPS 仍僅有個位數。這導致遊戲畫面嚴重延遲，極易造成使用者的「3D 暈」或操作挫折感。

2.  **即時性需求 (Real-time Requirement):**
    體感遊戲需要即時反饋（例如：手舉起來，畫面中的卡片就要馬上翻開）。若延遲 (Latency) 過高，遊戲的可玩性將趨近於零。

---

## 🛠️ 技術深度剖析 (Technical Deep Dive)

為了兼顧準確度與流暢度，我們將架構由「地端運算」轉型為「雲端串流運算」。

### 1. 核心模型：MobileNet + OpenPose

我們採用 **MobileNet** 作為 OpenPose 的特徵提取器 (Backbone)。MobileNet 的核心優勢在於使用了 **深度可分離卷積 (Depthwise Separable Convolution)**，大幅減少了參數與運算量。

假設輸入特徵圖大小為 $D_F \times D_F \times M$，卷積核大小為 $D_K \times D_K$，輸出通道數為 $N$。

* **標準卷積運算量 (Standard Convolution):**
    $$C_{std} = D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F$$

* **深度可分離卷積運算量 (Depthwise Separable Convolution):**
    $$C_{depthwise} = D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F$$

透過此公式可看出，MobileNet 將運算量降低了約 8~9 倍，這是在雲端能快速處理大量 Frame 的基礎。

### 2. 系統架構：雲端協同與 WebSocket (System Architecture)

為了解決地端算力不足，我設計了 Client-Server 分離架構：

* **Client 端 (地端筆電):**
    * 角色：**Thin Client (瘦客戶端)**。
    * 任務：使用 OpenCV 讀取 Webcam 影像，將每一幀畫面壓縮（JPEG）並編碼，透過網路傳送。接收回傳的骨架資訊並繪製在畫面上。
* **Server 端 (Google Cloud Platform):**
    * 角色：**Inference Engine (推論引擎)**。
    * 任務：接收影像流，執行 MobileNet + OpenPose 推論，計算人體 18 個關鍵點 (Keypoints) 的座標 $(x, y)$。
* **通訊協定 (WebSocket):**
    * 為了達到 Real-time，HTTP 的三向交握 (Handshake) 開銷太大。
    * 我們採用 **WebSocket** 全雙工通訊協定，建立一條持久連線 (Persistent Connection)，確保影像封包能以毫秒級的速度往返。

### 3. 遊戲邏輯與互動設計 (Game Logic)

透過 AI 識別出的骨架座標，我們將其映射到遊戲邏輯中：

* **翻牌記憶遊戲 (Memory Card):**
    偵測「手腕 (Wrist)」節點的座標。當手腕座標停留在虛擬卡片區域超過 1 秒（Hover），即觸發「翻牌」事件。


* **瑜珈模仿遊戲 (Yoga):**
    計算肢體角度的餘弦相似度 (Cosine Similarity)。例如計算「手肘-肩膀-臀部」的向量夾角，比對使用者與標準動作的差異，並給予評分。

---

## 📊 成果展示 (Results)

透過雲端運算的導入，我們成功將遊戲幀率 (FPS) 提升至流暢的可玩水準，並實現了跨平台支援。

### 1. 翻牌遊戲實測

![Untitled](/postImg/pose-detection/1.jpg)
*Figure 1: 使用者透過手部動作隔空控制虛擬卡片。系統精確捕捉手腕位置，實現無接觸式互動。*

### 2. 瑜珈遊戲實測

![Untitled](/postImg/pose-detection/2.jpg)
*Figure 2: 系統即時比對使用者姿勢（黃色骨架）與標準動作（右上角圖示），並給予即時分數回饋。*

### 結論 (Conclusion)

本專案證明了在硬體資源受限的場景下，透過合理的**架構設計 (Architecture Design)**——即將繁重的 AI 運算轉移至雲端，並利用 WebSocket 優化傳輸——能夠有效解決效能瓶頸。這不僅降低了使用者的硬體門檻（不需購買昂貴電腦），也為銀髮族提供了一種更易取得的居家運動方案。
---
title: Deep Q-Network 實戰：基於 TensorFlow 的四層神經網路貪食蛇代理
slug: DQNsnakegame
date: 2022-04-22
categories:
- 研究生專題
tags: 
- Python
- TensorFlow
- Reinforcement Learning
- Deep Q-Network
- Deep Learning & Machine Learning

thumbnailImagePosition: left
thumbnailImage: /postImg/DQNsnakegame/1.png
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

本專案將深度強化學習 (Deep Reinforcement Learning) 應用於經典的貪食蛇遊戲中。為了讓代理 (Agent) 能在動態環境中做出最佳決策，我使用 **TensorFlow** 框架設計了一個**客製化的四層全連接神經網路 (4-Layer Fully Connected Network)** 作為核心的 Q-Network。

<!--more-->


---

透過設計 11 維的環境特徵向量作為輸入，並配合 Bellman Equation 進行 Q 值迭代更新，該模型成功學會了避障、路徑規劃以及長期生存策略。此專案展示了從環境建置、模型架構設計到獎勵函數優化的完整 AI 開發流程。

---

## 🛑 動機與挑戰 (Motivation & Challenge)

在強化學習中，如何設計一個「夠深但不過擬合 (Overfitting)」的網路架構來處理狀態空間，是成功的關鍵。

1.  **狀態特徵提取：** 貪食蛇的決策依賴於相對位置（食物在哪？身旁有無危險？），而非絕對座標。
2.  **稀疏獎勵 (Sparse Reward)：** 蛇只有在吃到食物時才有正回饋，其餘時間都在移動。若網路架構過於簡單，難以捕捉「移動」與「未來獎勵」的關聯；若過於複雜，則訓練收斂速度太慢。

---

## 🛠️ 技術深度剖析 (Technical Deep Dive)

### 1. 狀態空間設計 (State Representation)

為了降低輸入維度並加速收斂，我捨棄了原始圖像輸入 (CNN)，改採特徵工程方式，將當前局勢濃縮為一個 **11 維的布林向量 (Boolean Vector)** $S_t$：

> *[圖片佔位符：建議放入一張示意圖，顯示蛇頭周圍的 11 個感測數值定義]* 

* **危險感知 (3):** [前方有危險, 右方有危險, 左方有危險]
* **移動方向 (4):** [左, 右, 上, 下] (One-hot encoding)
* **食物方位 (4):** [食物在左, 食物在右, 食物在上, 食物在下]

### 2. 模型架構設計 (Model Architecture)

這是本專案的核心。為了捕捉狀態特徵之間的非線性關係（例如：「食物在左」且「左方有危險」$\rightarrow$ 應採取「向上或向下」），我利用 TensorFlow/Keras 建構了一個**四層 Dense 網路**。

數學表示如下：

$$f(x) = W_4 \cdot \sigma(W_3 \cdot \sigma(W_2 \cdot \sigma(W_1 \cdot x + b_1) + b_2) + b_3) + b_4$$

* **Input Layer:** 接收 11 維狀態向量。
* **Hidden Layer 1 & 2 (Dense):** 透過兩層隱藏層（配合 ReLU 激活函數 $\sigma$）進行特徵交叉與提取，增加模型的表達能力，使其能理解複雜的死路結構。
* **Output Layer:** 輸出 3 個 Q 值，分別對應 [直走, 右轉, 左轉] 的預期獎勵。

> *[圖片佔位符：建議放入神經網路架構圖，顯示 Input(11) -> Dense -> Dense -> Output(3) 的層級結構]* 

### 3. DQN 演算法與優化 (DQN Algorithm)

利用 TensorFlow 的自動微分能力，我實作了 DQN 的訓練迴圈：

* **預測 (Prediction):** 使用 `model.predict(state)` 獲取當前動作的 Q 值。
* **目標 Q 值 (Target Q):** 根據 Bellman Equation 計算：
    $$Q_{target} = R + \gamma \cdot \max(Q_{next\_state})$$
* **訓練 (Training):** 使用 `model.fit()` 最小化損失函數 (Loss Function)，採用均方誤差 (MSE) 來讓預測值逼近目標值。

### 4. 獎勵塑形 (Reward Shaping)

為了引導蛇更有效率地學習，我設計了細緻的獎勵機制：

* **生存與進食:** 吃到食物 $+10$，死亡 $-10$。
* **引導策略:** 若動作使蛇頭與食物的距離**縮短**，給予微小獎勵；若**變遠**，給予微小懲罰。這解決了初期蛇在原地打轉的問題。
* **時間懲罰:** 每一步固定扣除 $-0.1$，迫使模型尋找最短路徑。

![Untitled](/postImg/DQNsnakegame/1.png)

---

## 📊 成果與反思 (Results & Reflection)


經過多次訓練迭代 (Epochs)，觀察到 Agent 的行為進化：

1.  **隨機階段:** 模型尚未收斂，蛇經常撞牆。
2.  **避障階段:** 隱藏層學會了識別「危險特徵」，蛇能長時間存活但在場地繞圈。
3.  **目標導向:** 四層架構成功融合了「食物方位」與「路徑規劃」，蛇展現出明確的捕食行為。

### 結論 (Conclusion)

透過 TensorFlow 實作這個自定義的四層 DQN 模型，我驗證了**深度神經網路 (DNN)** 在處理決策問題上的強大能力。這個專案不僅讓我熟悉了 TensorFlow 的模型建構 API，更讓我深刻體會到網路深度 (Depth) 與獎勵函數設計對強化學習效能的決定性影響。


{{< video src="/videos/DQNsnakegame.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="720" height="480">}}

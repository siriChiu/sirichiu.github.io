---
title: 智慧醫療輔助診斷：基於 ResNet50 的胸腔 X 光肺炎分類器
slug: covid19-chestXray
date: 2022-04-22
categories:
- 研究生專題
tags:
- MATLAB
- Deep Learning/Machine Learning
- Medical Imaging
- Classification

thumbnailImagePosition: left
thumbnailImage: /postImg/covid19-chastXray/4.png
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

本專案旨在開發一套基於深度學習的自動化輔助診斷系統，協助醫療人員快速判讀胸腔 X 光影像 (CXR)。

<!--more-->

---

## 📋 專案摘要 (Abstract)

本專案旨在開發一套基於深度學習的自動化輔助診斷系統，協助醫療人員快速判讀胸腔 X 光影像 (CXR)。

針對 COVID-19 與肺炎特徵在 X 光片上難以肉眼區分的挑戰，本專案選用 **MATLAB** 作為開發環境，並導入深層殘差網路 **ResNet50** 進行二元分類任務（Normal vs. Pneumonia/COVID-19）。透過殘差學習 (Residual Learning) 機制解決深層網路的退化問題，最終模型在測試集上展現了良好的召回率 (Recall)，能有效篩檢出潛在的肺炎患者，降低漏診風險。

---

## 🛑 問題與挑戰 (The Problem)

在疫情高峰期或醫療資源匱乏地區，放射科醫師面臨巨大的閱片壓力。傳統的人工判讀存在以下痛點：

1.  **判讀耗時：** 醫師需要長時間專注查看細微的肺部浸潤特徵。
2.  **特徵模糊：** 早期肺炎或 COVID-19 的毛玻璃狀病變 (Ground-glass opacity) 與一般肺部紋理極為相似，容易造成誤判。
3.  **疲勞誤差：** 長時間工作導致的視覺疲勞可能增加漏診率。

---

## 🛠️ 技術深度剖析 (Technical Deep Dive)

### 1. 資料前處理 (Data Preprocessing)

資料集包含兩類胸腔 X 光影像：

* **Normal (正常):** 肺野清晰，無明顯異常陰影。
* **Pneumonia (肺炎/COVID-19):** 肺部呈現斑片狀陰影或實變。

為了提升模型的泛化能力 (Generalization)，我對原始影像進行了標準化處理，並調整至 ResNet50 所需的輸入尺寸 ($224 \times 224$ pixels)。

![正常胸腔 X 光](/postImg/covid19-chastXray/1.jpg)
*Figure 1: 正常的胸腔 X 光影像 (Normal)，肺野清晰。*

![肺炎胸腔 X 光](/postImg/covid19-chastXray/2.jpg)
*Figure 2: 患有肺炎的胸腔 X 光影像 (Pneumonia)，可見肺部有模糊陰影。*

### 2. 核心架構：ResNet50 與殘差學習 (Residual Learning)

傳統卷積神經網路 (CNN) 在層數加深時，容易遇到梯度消失 (Vanishing Gradient) 或梯度爆炸問題，導致訓練效果反而下降。

為了訓練高達 50 層的深層網路，我採用了 **ResNet (Residual Network)** 架構。其核心創新在於引入了 **「捷徑連接 (Shortcut Connection)」**。

假設神經網路某一層的輸入為 $x$，期望學習到的特徵映射為 $H(x)$。ResNet 不直接學習 $H(x)$，而是學習殘差函數 $F(x) = H(x) - x$。最終輸出為：

$$y = F(x, \{W_i\}) + x$$

* $F(x, \{W_i\})$：殘差映射 (Residual Mapping)，即網路層需要學習的變化量。
* $x$：恆等映射 (Identity Mapping)，直接將輸入訊息傳遞到輸出。

這種 $y = F(x) + x$ 的結構確保了即使在網路極深的情況下，梯度也能透過 $x$ 這條「高速公路」直接回傳，讓模型能有效捕捉 X 光影像中極其細微的病徵特徵。



### 3. 訓練策略 (Training Strategy)

使用 MATLAB 的 Deep Learning Toolbox 進行訓練。

* **優化器 (Optimizer):** SGDM (Stochastic Gradient Descent with Momentum)
* **損失函數 (Loss Function):** Cross Entropy Loss (二元交叉熵)

---

## 📊 成果與數據分析 (Results & Analysis)

根據測試集的混淆矩陣（Confusion Matrix），我們對模型的效能進行了量化評估：

![混淆矩陣結果](/postImg/covid19-chastXray/3.png)
*Figure 3: 測試集的混淆矩陣 (Confusion Matrix)。*

### 1. 混淆矩陣數據解讀

測試集總樣本數：$N = 591$ 張

* **True Positive (TP, 成功預測肺炎):** 308 張
* **True Negative (TN, 成功預測正常):** 150 張
* **False Positive (FP, 誤判為肺炎):** 84 張
* **False Negative (FN, 漏診肺炎):** 49 張

### 2. 關鍵指標計算

* **準確率 (Accuracy):**
    $$Accuracy = \frac{TP + TN}{Total} = \frac{308 + 150}{591} \approx 77.5\%$$
    模型整體判斷正確的比例約為七成八。

* **召回率 / 靈敏度 (Recall / Sensitivity):**
    $$Recall = \frac{TP}{TP + FN} = \frac{308}{308 + 49} \approx 86.3\%$$
    **這是醫療診斷最重要的指標。** 結果顯示，在所有實際患有肺炎的病人中，模型成功抓出了 **86.3%** 的案例。這意味著模型作為「第一道篩檢防線」是非常稱職的，能有效減少漏診。

* **精確率 (Precision):**
    $$Precision = \frac{TP}{TP + FP} = \frac{308}{308 + 84} \approx 78.6\%$$
    在模型判斷為肺炎的案例中，有 78.6% 是確診的。雖然有部分正常人被誤判為肺炎（偽陽性 84 例），但在醫療篩檢的情境下，**「寧可誤判 (False Positive) 也不要漏診 (False Negative)」** 是可接受的權衡。

### 結論 (Conclusion)

本專案成功利用 ResNet50 架構實現了胸腔 X 光的自動化分類。實驗數據證明，透過殘差學習機制，模型能有效提取肺部病變特徵，並達到 **86.3% 的高靈敏度**。這套系統具備成為放射科醫師輔助工具的潛力，能在短時間內處理大量影像，標示出高風險案例供醫師優先複查。



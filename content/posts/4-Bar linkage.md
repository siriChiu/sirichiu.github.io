---
title: 機構合成的最佳化：基於 MATLAB 數值分析的四連桿路徑生成器
slug: 4-Bar linkage
date: 2022-04-22
categories:
- 研究生專題
tags:
- MATLAB
- Mechanism Synthesis
- Kinematics
- Optimization
- Numerical Analysis
- Deep Learning & Machine Learning

thumbnailImagePosition: left
thumbnailImage: /postImg/4-Bar Linkage/1.png
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
本專案探討了機構學中的經典難題——「路徑生成 (Path Generation)」。目標是設計一組四連桿機構 (4-Bar Linkage)，使其連桿曲線 (Coupler Curve) 能精確通過空間中指定的 9 個目標點。
<!--more-->


---

## 📋 專案摘要 (Abstract)



不同於傳統的圖解法或試誤法，本專案採用**數值最佳化**策略。透過 **MATLAB** 建立基於向量迴路法 (Vector Loop Equation) 的運動學模型，並利用 `fminsearch` 演算法針對桿長與起始角度進行多變數迭代求解。最終成功在滿足 Grashof 定理 (全迴轉條件) 的前提下，找出了誤差最小的最佳機構尺寸參數。

---

## 🛑 問題與挑戰 (The Problem)

在課堂專題中，我們被給予了 9 個固定高度的空間座標點。任務是設計一個四連桿機構，當主動桿旋轉一圈時，其連結桿 (Coupler) 上的特定點軌跡必須盡可能貼合這 9 個點。

這是一個典型的**非線性最佳化問題**，面臨以下挑戰：
1.  **多變數耦合：** 改變任意一根桿長，整條軌跡的形狀都會劇烈變化。
2.  **幾何限制：** 機構必須能進行 360 度全迴轉 (Crank-Rocker)，否則會卡死。
3.  **數學複雜度：** 連桿的非線性位置方程式難以直接求出解析解，必須依賴數值方法。

---

## 🛠️ 技術深度剖析 (Technical Deep Dive)

本專案的核心在於將物理機構轉化為數學模型，並定義出讓電腦可以「評分」的目標函數。

### 1. 數學建模：向量迴路法 (Vector Loop Modeling)

為了計算機構在任意角度下的位置，我使用了複數向量法 (Complex Numbers Method)。如圖所示，將四連桿視為一個閉合的向量迴路：

$$\vec{r_2} + \vec{r_3} = \vec{r_1} + \vec{r_4}$$

利用尤拉公式 ($e^{i\theta} = \cos\theta + i\sin\theta$) 將其展開為實部與虛部：

$$r_2 e^{i\theta_2} + r_3 e^{i\theta_3} - r_4 e^{i\theta_4} - r_1 = 0$$

透過此方程式，對於每一個輸入的主動桿角度 $\theta_2$，我們可以利用幾何關係推導出從動桿角度 $\theta_4$ 與連結桿角度 $\theta_3$，進而計算出軌跡點 $P$ 的精確座標 $(x, y)$。

![Untitled](/postImg/4-Bar linkage/1.png)

### 2. 最佳化策略 (Optimization Strategy)

我選擇 MATLAB 的 `fminsearch` (基於 Nelder-Mead 單純形法) 作為求解器。

* **優化變數 (Design Variables):**
    系統需要調整的參數包含 4 根桿子的長度 ($L_1, L_2, L_3, L_4$) 以及主動桿的起始角度 ($\theta_{start}$)。

* **目標函數 (Cost Function):**
    為了定義「最佳」，我採用**最小平方法 (Least Squares)** 的概念。計算軌跡上對應點與 9 個目標點之間的**歐幾里得距離 (Euclidean Distance)** 總和：

    $$Error = \sum_{i=1}^{9} \sqrt{(x_{target,i} - x_{calc,i})^2 + (y_{target,i} - y_{calc,i})^2}$$

    演算法的目標即是找到一組參數，使此 $Error$ 值最小化。

### 3. 機構限制處理 (Constraint Handling)

並非所有長度組合都能形成可旋轉的機構。為了確保機構能順利運轉一圈而不卡死，必須滿足 **Grashof 定理 (Grashof's Law)**：

$$S + L \le P + Q$$

*(其中 $S$ 為最短桿，$L$ 為最長桿，$P, Q$ 為其餘兩桿)*

在程式實作上，我採用了**懲罰函數 (Penalty Function)** 的技巧：在計算誤差前，先檢查當前參數是否滿足 Grashof 條件。若不滿足（例如機構無法全迴轉），則直接回傳一個極大的誤差值 (如 `Infinity`)，強制 `fminsearch` 演算法遠離該參數區域，重新尋找可行解。

---

## 📊 成果與結論 (Results & Conclusion)

透過數百次的迭代運算，程式最終收斂出一組最佳桿長參數。將此參數代入繪圖後，產生的連桿曲線成功穿過了目標的 9 個點（或誤差在可接受範圍內），且機構運轉順暢無死點。

這個專案讓我深刻體會到：
1.  **數學是工程的語言：** 透過尤拉公式與向量法，能將複雜的機械動作精準量化。
2.  **數值方法的威力：** 當解析解難以求得時，正確設定目標函數與限制條件，利用演算法能有效解決工程上的最佳化難題。

## 結果

{{< video src="/videos/4bar-linkage.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="720" height="720">}}






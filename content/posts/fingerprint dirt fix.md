---
title: 形態學指紋特徵提取：基於 Bowler-Hat 變換的雜訊抑制與結構增強
slug: fingerprint-dirt-fix
date: 2022-04-22
categories:
- 研究生專題
tags: 
- MATLAB
- Image Processing
- Mathematical Morphology
- Feature Extraction
- Noise Reduction
- Fingerprint Recognition

thumbnailImagePosition: left
thumbnailImage: /postImg/fingerprint-dirt-fix/1.jpg
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
本專案利用 **MATLAB** 實作了進階的數學形態學處理流程。透過 **Top-Hat 運算**濾除背景污漬，並引入 **Bowler-Hat 變換 (Bowler-Hat Transform)** 進行結構增強。實驗結果證實，此演算法能有效還原受汙損指紋的脊線特徵，同時也驗證了該演算法在不同領域影像處理上的通用性。

<!--more-->


---

指紋影像與超音波血管影像在拓樸結構上具有高度相似性（均為管狀/線狀結構），但也同樣面臨背景雜訊（污漬）與對比度不足的問題。

---

## 🛑 問題與挑戰 (The Problem)

在指紋辨識的前處理階段，我們常面臨以下挑戰：

1.  **背景雜訊 (Background Noise):** 採集過程中的污漬、油墨不均或感測器髒汙，會在影像上形成不規則的塊狀雜訊（如圖左所示的大面積污漬）。
2.  **結構模糊 (Weak Structure):** 指紋脊線 (Ridges) 與谷線 (Valleys) 的對比度低，導致傳統的二值化方法（如 Otsu's method）容易產生斷裂或沾黏。

我們的目標是在保留指紋細節的前提下，移除低頻背景雜訊並強化高頻紋理。

---

## 🛠️ 技術深度剖析 (Technical Deep Dive)

本專案的核心概念是將指紋視為一種「地貌」，脊線是山峰，谷線是山谷，而污漬則是平緩的斜坡。我們利用數學形態學 (Mathematical Morphology) 來分離這些特徵。

### 1. 形態學基礎與結構元素 (Structuring Element)
使用 **MATLAB** 的 Image Processing Toolbox，我首先定義了結構元素 (Structuring Element, $B$)。為了配合指紋的物理特性，$B$ 的大小被設計為略大於一般脊線的寬度，以確保能正確捕捉紋理。

### 2. 雜訊移除：Top-Hat 運算 (Top-Hat Operations)
為了移除大面積的背景污漬（低頻雜訊），我使用了 Top-Hat 運算。

* **White Top-Hat (WTH):** 用於提取比周圍亮且小於結構元素的特徵（即亮細節/脊線）。
    $$WTH(f) = f - (f \circ B)$$
    *(其中 $\circ$ 代表 Opening 運算)*

* **Black Top-Hat (BTH):** 用於提取比周圍暗且小於結構元素的特徵（即暗細節/谷線）。
    $$BTH(f) = (f \bullet B) - f$$
    *(其中 $\bullet$ 代表 Closing 運算)*

透過這兩個運算，我們能將局部的亮點與暗點從不均勻的背景中「剝離」出來。

### 3. 結構增強：Bowler-Hat 變換 (Bowler-Hat Transform)
單純的 Top-Hat 往往只保留了部分訊息。為了同時強化脊線（亮）與谷線（暗），並最大化兩者間的對比度，我實作了 **Bowler-Hat Transform (BHT)**。

參考文獻 *Meftah et al. (2018)*，BHT 的標準定義為將 White Top-Hat 減去 Black Top-Hat：

$$BHT(f) = WTH(f) - BTH(f)$$

將其展開可表示為：

$$BHT(f) = [f - (f \circ B)] - [(f \bullet B) - f]$$

**物理意義：**
* $WTH(f)$ 貢獻了影像中的「正向特徵」（脊線）。
* $BTH(f)$ 貢獻了影像中的「負向特徵」（谷線）。
* 相減的操作 ($WTH - BTH$) 能夠在數學上極大化局部對比度，同時抵消掉背景中的緩慢變化（即移除了污漬），從而獲得純淨且高對比的紋理結構。

---

## 📊 成果與驗證 (Results & Validation)

下圖展示了演算法的處理成果：

![指紋處理前後對比圖](/postImg/fingerprint-dirt-fix/1.jpg)
*Figure 1: 指紋強化前後對比。左圖：帶有嚴重污漬與雜訊的原始影像；右圖：經過 Bowler-Hat 變換與二值化後的結果。*

**分析結果：**
* **去噪效果 (Noise Reduction):** 原始影像左上角及邊緣的大面積模糊污漬被成功移除。這是因為該污漬的幾何尺度大於我們設定的結構元素 $B$，因此在 Top-Hat 運算中被視為背景而被濾除。
* **特徵強化 (Structure Enhancement):** 指紋中心的螺旋結構（Whorl）變得清晰可見，脊線的連續性與分離度得到顯著改善，證明了 BHT 在增強管狀結構上的有效性。

### 結論 (Conclusion)
本專案成功利用形態學技術解決了指紋提取中的雜訊干擾問題。更重要的是，它作為一個驗證集 (Validation Set)，證明了我所開發的**血管強化演算法**具備強大的強健性 (Robustness) 與跨領域應用潛力，能有效處理各類具備「管狀結構」特徵的生物醫學影像。

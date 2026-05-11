---
title: 伺服器散熱控制演算法：基於穩態熱特徵的自動化 PID 參數生成系統
slug: new-pid-for-server
date: 2025-11-10
categories:
- 專業技術
tags:
- Server Cooling
- PID Algorithm
- Thermal Management
- Automation
- Data Center
- Energy Efficiency
- Golang
- Python
- Grafana
- IPMI
- Linux
- Server BMC
- CI/CD


thumbnailImagePosition: left
thumbnailImage: /postImg/ice_algo/thumbnail.png
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

本專案針對資料中心伺服器散熱控制中的兩個常見問題：開迴路控制造成的過度保守，以及人工調校 PID 所需的時間成本。我開發了一套**自動化熱特徵識別系統**，用來建立較一致的測試流程與控制參數推導方式。

<!--more-->

該系統整合 **Golang** 與 **Python** 自動化腳本，透過環境測試室（Chamber）建立伺服器的穩態熱特徵資料結構（Steady-state Thermal Profile），再透過參數關聯模型推導 PID 參數。此外，針對運算負載劇變（Load Dump）場景，引入「非零積分重置（Non-zero Integral Reset）」機制，降低風扇轉速過度下探與震盪風險。

<!-- --- -->


## 🛑 產業背景與痛點 (Industry Context & Challenges)

在伺服器散熱領域，現行的主流作法面臨以下技術瓶頸：

### 1. 開迴路控制的過度設計 (Over-design in Open-loop Control)
傳統的「查表法（Lookup Table）」僅依賴溫度區間對應固定轉速。為了確保系統安全性，業界慣例是基於該機箱支援的**最高階硬體配置 (Maximum Configuration)** 與 **最嚴苛環境條件 (Worst-case Scenario)** 來設定單一散熱曲線。
* **後果：** 對於中低階配置的伺服器，風扇可能長期處於非必要的「過轉（Over-speeding）」狀態，造成額外能源消耗與噪音。

### 2. 傳統 PID 的人工調校瓶頸 (Manual Tuning Inefficiency)
即便採用閉迴路控制（Closed-loop PID），參數 ($K_p, K_i, K_d$) 的設定往往高度依賴資深工程師的經驗法則（Rule of Thumb）進行反覆試誤（Trial and Error）。
* **後果：** 缺乏標準化的系統識別（System Identification）流程，調校可能耗時數週，且不容易重現到不同伺服器個體。

### 3. 積分飽和與系統不穩 (Integral Windup & Instability)
在負載瞬間卸除（Load Dump）的情境下，傳統 PID 容易因積分項累積過多誤差，導致風扇轉速驟降（Undershoot）甚至發生震盪（Oscillation），影響散熱穩定性。

---

## 🛠️ 技術解決方案 (Technical Solution)

本方法提出一種**基於穩態熱特徵資料結構的自動化控制參數生成流程**，讓散熱控制從單純經驗調校，逐步轉向資料輔助的參數推導。

### ■ 系統架構 (System Architecture)

我們建構了一套自動化測試迴路 (Hardware-in-the-Loop)，整合軟硬體資源：

* **自動化控制單元 (Host Controller):** 使用 **Golang** 編寫核心控制邏輯，利用其高併發特性處理多台待測機 (SUT) 的連線管理；底層指令封裝則結合 **Shell Script** 與 **Python** 進行數據清洗與圖表繪製。
* **待測伺服器 (SUT):** 透過 BMC 介面接收轉速指令並回傳感測器數據。
* **環境測試室 (Chamber):** 提供穩定的環境溫度變因。



### ■ 核心演算法流程 (Core Methodology)

#### 1. 自動化熱特性掃描 (Automated Thermal Profiling)
於工程驗證階段 (EVT/DVT)，自動化腳本控制伺服器遍歷從空載 (Idle) 到滿載 (Full Load) 的複數個運算負載點 $L_i$。在每個負載點下，控制風扇轉速 $\omega$ 進行階梯式掃描。

當系統偵測到溫度變化率 $\frac{dT}{dt} \approx 0$ 時，判定進入**熱平衡狀態 (Thermal Equilibrium)**，並記錄該點的數據，建立描述該伺服器物理散熱極限的**「穩態熱特徵資料結構 (Thermal Characteristic Profile)」**。



#### 2. 參數推導與模型化 (Parameter Derivation)
系統解析上述資料結構，計算系統增益 (System Gain) 與響應斜率，首先決定第一控制增益（比例項 $K_p$）。
接著，透過預設的**參數關聯模型 (Parameter Correlation Model)**，將積分 ($K_i$) 與微分 ($K_d$) 項視為 $K_p$ 的函數進行推導。

令 $\mathcal{M}$ 為基於熱時間常數與系統阻尼比所建立的轉換模型，則 PID 參數推導如下：

$$K_p = f(\text{Slope}_{profile}, \text{Gain}_{system})$$

$$K_i, K_d = \mathcal{M}(K_p)$$

這確保了三項參數具備物理意義上的強耦合性，而非隨機湊數，實現了閉迴路控制的穩定性。

#### 3. 動態運行控制：非零重置機制 (Runtime Control with Non-zero Reset)
在 BMC 運行階段，針對 Load Dump 造成的溫度急降，我設計了特殊的積分權重管理模組。
當誤差 $e(t)$ 急劇變化時，積分項 $I_{term}$ 不會像傳統 Anti-windup 直接歸零，而是重置為一個動態計算的基準值 $I_{base}$：

$$I_{new} = \begin{cases} 0 & \text{Traditional Approach (Risky)} \\ I_{base} & \text{Proposed Approach (Stable)} \end{cases}$$

其中 $I_{base} \neq 0$，確保風扇能平滑過渡至低負載所需的安全轉速，消除 Undershoot 風險。



---

## 📊 專案成效 (Impact & Benefits)

### 1. 研發效率與標準化 (Efficiency & Standardization)
* 將原本耗時 **數週** 的人工調校流程，縮短為 **數小時** 的全自動化程序。
* 提升參數生成的「可重現性」，讓不同批次的伺服器更容易沿用一致的控制參數推導流程。

### 2. 極大化熱餘裕與節能 (Energy Optimization & ESG)
* 透過 PID 溫度追隨，系統可嘗試維持接近需求的風扇轉速，減少無效過冷。
* 有助於降低不必要的風扇功耗，支援後續能效最佳化。

### 3. 提升硬體可靠度 (Reliability)
* 平滑的轉速控制與「非零重置」機制，有效避免了風扇轉速劇烈震盪。
* 減少了電子元件承受的**熱循環應力 (Thermal Stress)**，延長了風扇軸承與晶片封裝的使用壽命。


### 步驟流程圖 (Control Flow Diagram) 
![PID 控制測試結果圖](/postImg/ice_algo/1.jpg)

### 控制流程圖 (Process Flow Diagram)
![PID 控制參數分析圖](/postImg/ice_algo/2.jpg)

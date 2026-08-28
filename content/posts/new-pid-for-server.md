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
- Golang
- Python
- IPMI
- Linux
- Server BMC
thumbnailImagePosition: left
thumbnailImage: /postImg/ice_algo/thumbnail-v2.png
katex: true
---

本專案把環境測試室、伺服器 BMC 與自動化 controller 串成閉環，先建立伺服器的穩態熱特徵，再由 profile slope 與 system gain 推導 PID 參數。它同時處理兩個問題：人工調校耗時，以及 load dump 後的積分狀態可能造成轉速下探與震盪。

<!--more-->

> 此案例屬於我的[研華軟體工程作品集](/job_exp_advantech/)。公開內容保留方法與資料流，但不揭露實際係數、設備組態、門檻或內部測試資料。

## 問題脈絡

單一 open-loop lookup table 通常以最高配置與最嚴苛環境為基準。對中低配置而言，這可能造成風扇長時間高於實際散熱需求。改用 closed-loop PID 後，`Kp`、`Ki`、`Kd` 若仍依賴反覆試誤，調校流程便難以標準化與重現。

另一個風險出現在 load dump：負載突然卸除、溫度快速下降時，累積積分狀態可能讓風扇轉速下探或震盪。本專案因此把**離線熱特徵識別**與**BMC runtime 控制**分開設計。

![熱特徵識別、參數推導與 BMC 執行期控制迴路](/postImg/ice_algo/thermal-control-loop.svg)

## 系統架構與我的貢獻

- **Host controller：** 以 Golang 編寫 orchestration，協調多台 SUT 的連線、負載與風扇掃描；Shell/Python 支援底層命令、資料清理與繪圖。
- **SUT / BMC：** BMC 接收 RPM 指令並回傳溫度、轉速與其他感測資料。
- **Environmental chamber：** 固定或調整 ambient condition，讓不同測試點具可比較的環境脈絡。
- **方法設計：** 建立 steady-state profile、控制參數推導，以及 load dump 的 non-zero integral reset 路徑。

![Host、BMC/SUT 與 chamber 的概念架構](/postImg/ice_algo/0.jpg)
*概念圖，不是量測結果截圖。*

## 離線識別：建立穩態熱特徵

自動化流程在 idle 到 full load 之間選擇多個負載點 `Li`，並於每個點階梯式調整風扇轉速 `ω`。當觀測到：

$$\frac{dT}{dt} \approx 0$$

系統把該狀態視為 thermal equilibrium，記錄負載、fan speed/RPM、temperature、ambient temperature 與溫度變化率。重複掃描後形成 steady-state thermal characteristic profile，供後續計算 response slope 與 system gain。

![自動化熱特徵測試流程](/postImg/ice_algo/1.jpg)
*既有流程圖：從測試條件、平衡判定到資料紀錄；它不是 PID 結果曲線。*

公開資料沒有揭露平衡容差、觀測窗、sampling cadence、負載 grid 或 fan step，因此 `dT/dt ≈ 0` 是方法條件，不應解讀為未限定的精度保證。

## 參數推導與部署

系統先從 profile slope 與 system gain 決定比例增益，再由既定參數關聯模型推導積分與微分項：

$$K_p = f(\text{Slope}_{profile}, \text{Gain}_{system})$$

$$K_i, K_d = \mathcal{M}(K_p)$$

`f` 與 `M` 的實際公式未公開。這個設計的價值是讓三個參數來自同一套熱特徵脈絡，而不是證明它在所有 server configuration 上都具最佳控制結果。產生的參數經工程驗證後，才交付 BMC firmware。

![PID 參數生成與 BMC 部署流程](/postImg/ice_algo/2.jpg)
*既有流程圖：profile 輸入、參數生成與韌體交付。*

## Runtime：非零積分重置

偵測到 load dump 對應的誤差急變時，控制器不是把積分項直接歸零，而是重置到動態計算的非零基準：

$$I_{new}=I_{base},\quad I_{base}\neq0$$

設計意圖是讓風扇保留低負載仍需要的安全轉速，降低過度下探與震盪風險。公開內容沒有比較曲線或可靠度壽命研究，因此不宣稱完全消除 undershoot，亦不推論風扇軸承或晶片封裝壽命延長。

## 驗證、成效與限制

在原先描述的內部調校情境中，這套自動化程序把可能耗時**數週**的人工流程縮短為**數小時**。這個數字只適用於該工作流，不是跨機種 benchmark。profile 與推導流程也讓測試步驟更一致，但跨批次可重現性仍需由配置、環境與統計驗證支持。

PID 追隨溫度需求可用來嘗試減少不必要的 over-cooling；這是控制目標，不是已公開驗證的固定節能比例。安全部署仍需要溫度上限、RPM 邊界、sensor fault、chamber 異常與 rollback 等保護措施，細節因保密未列出。

## 技術棧

**Golang · Python · Shell · BMC/IPMI · Environmental chamber · Thermal profiling · PID control**

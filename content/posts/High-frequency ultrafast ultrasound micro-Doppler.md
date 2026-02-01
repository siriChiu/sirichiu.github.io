---
title: 高頻超音波微多普勒成像技術在手指肌腱新生血管評估中的應用
slug: High-frequency ultrafast ultrasound micro-Doppler imaging for estimating finger tendon neovascularity based on curvilinear structure enhancement
date: 2022-04-24
categories:
- 研究所論文
tags:
- MATLAB
- Ultrasound
- Micro-Doppler
- Neovascularization
- Medical Imaging
- Signal Processing

thumbnailImagePosition: left
thumbnailImage: /postImg/HFUDCEI/00.png
coverImage: 
---

我提出一種微血管成像演算法，能夠清楚的看見老鼠腎臟的血管樹狀結構以及手指受傷肌腱的新生血管資訊，最高解析度可達直徑35um。

<!--more-->


## Abstract

High-frequency ultrafast ultrasound micro-Doppler imaging for estimating finger tendon neovascularity based on curvilinear structure enhancement

我提出一種演算法他能夠清楚的看見老鼠腎臟以及手指受傷肌腱的血管變化。
這裡的超音波影像是老鼠的腎臟以及脾臟，腎臟的大小大約在9mmX5mm左右，脾臟大約在6mmX3mm左右，這兩個器官在解剖學上具有標準的血管樹狀結構，向這樣的大小在臨床儀器中是不可能看到其中血流的變化的。但是透過我們的儀器以及我提出的演算法可以很輕易地看見其中血流分布的資訊。

![Untitled](/postImg/HFUDCEI/0.png)

---

# 研究內容

## Introduction

### 手部受損

人類不管哪個部位受傷時基本上都會瘀青，瘀青就是新生血管的一種呈現，受傷部位必須通過血液攜帶養分才能夠進行修復。

手部的受傷在急診室相當常見，比例大約占10-15%，
手部受傷後的特性變化，對於評估患者恢復情況是很重要的。

手部修復過程分為三個階段，第一個是發炎期，在來是增生期，最後是修復期。

在發炎期與增生期生所產生的新生血管，在手指上已經有研究指出是位於手指兩側的動脈。
手指在受傷的時候旁邊兩條動脈會感應受傷的部位而新生血管進行修復。

![Untitled](/postImg/HFUDCEI/1.png)

## Flow Diagram

![Untitled](/postImg/HFUDCEI/2.png)

## Clutter filter-(Block-wise SVD)

奇異值分解是很強大的數學工具，常常用來進行特徵的提取，在這裡我對整個超音波序列資料進行SVD分解可以得到三個矩陣U, 𝜟, V， U是左奇異向量矩陣，在這裡代表超音波的空間資訊，V代表時間資訊，𝜟表示資料中的權重分布。

![Untitled](/postImg/HFUDCEI/3.png)

每個U𝜟V 在超音波所代表的意義可以用這張小鼠的腎臟圖表示，權重越高的可以理解為空間貢獻度最大，時間上最無變化的資訊也就是組織訊號，反之則為雜訊，將所不要的組織訊號濾除，最後重組的結果就是濾波後的資料。

![Untitled](/postImg/HFUDCEI/4.png)

## Background Suppression

可以發現濾波後的影像中的有一層漸層的背景雜訊。

這個背景雜訊在2017年的時候以由Song等人研究證實與超音波TGC增益有關。

目前常見的文獻中通常都使用TopHat轉換進行背景濾除來獲得更高清晰度的血管影像。上圖是侵襲性乳管癌第二型的影像，下圖的人類肝臟影像。

![Untitled](/postImg/HFUDCEI/5.png)

這裡以一維的方式簡單介紹一下Tophat轉換。
圖A表示在未經抑制的血管與背景雜訊資訊，在來經過形態學的侵蝕與膨脹處理，用這個方法將背景訊號挑出來，最後將原始影像A減去經過形態學處理得到的底躁C 就會得到僅剩血管的影像D

![Untitled](/postImg/HFUDCEI/6.png)

## Vessel enhance filter (VEF) Hessian based Vesselness

即使經過背景抑制的演算法，血管影像依然看起來粗糙，在這裡我就使用Frangi等人提出，並由Bayat引進至超音波領域中的血管增強濾波器，來提升血管的視覺化效果。

![Untitled](/postImg/HFUDCEI/7.png)

血管特徵提取，這個方法一開始是在MRA(腦部磁振造影血管攝影)、CTA(電腦斷層血管攝影)這些領域使用的。

在Vesselness公式中的H表示二次微分的二維黑森矩陣，黑森矩陣在影像處理中的意義中是邊緣提取的意思，Hs表示在不同尺度下所看到的影像資料。
之後透過此公式的會得到黑森矩陣的兩個特徵值 𝜆1, 𝜆2
𝜆1為垂直於血管的特徵，𝜆2為平行於血管的特徵，通過清除非平行於血管的特徵值，就能夠得到最後的血管影像。

![Untitled](/postImg/HFUDCEI/8.png)

不同的𝜆1與𝜆2表示影像中的不同結構，比方說像是𝜆2>>𝜆1表示曲線狀的結構等

## Results

### Animal Study

為了驗證HFUDCEI演算法的精確度及可靠性，我以小鼠的腎臟及脾臟的樹狀血管結構為參考，比較了各種血管成像技術得到的影像。
我總共掃描四隻老鼠的腎臟影像，而這是其中一張老鼠左腎的照片，在BMODE影像中可以看到腎臟以及脾臟的位置，中間這排分別是經過SVD濾波 SVD+TH、SVD+BH、SVD+TH+VEF，最下面這排分別是經過BWSVD、BWSVD+TH背景抑制、BWSVD+BH背景抑制與BWSVD+BH+VEF也就是HFUDCEI

直接從影像上可以看出，在未經過背景抑制之前的影像都能看出有一層背景雜訊，

在背景抑制的程序中，與TH相比，BH轉換可以更有效的將背景訊號濾除，
假如今天當對雜訊的濾除不夠完全就將進行VEF血管增強處理的話，就很有可能導致許多雜訊因此被跟著強化。

![Untitled](/postImg/HFUDCEI/9.png)

為了量化各個演算法的結果，我比較了各個演算法下的影像品質。

我的對比度與信噪比是根據這個公式計算的，並以人工圈選的方式選擇要比較的血管區域，這裡白色實線表示，
要比較的雜訊區域，以虛線表示，這裡的結果是由四隻小鼠作來統計的，可以看到BWSVD+BH+VEF獲得了最高的 CNR 及SNR 分別為 20.76 與 71.98 分貝，

而在血管解析度中，1和2的血管分布分別為35um與48um左右直徑的大小。在血管分布3中可以看出我提出的演算法的峰對谷比是最高的，

總結來說HFUDCEI對血管的敏感度、以及抗雜訊能力都很優秀，因此是很有能力作為新生血管量測的工具的。

![Untitled](/postImg/HFUDCEI/10.png)

### Human Study

這裡是人類實驗的結果
這是一個典型的EDC肌腱斷裂個案的超音波影像，掃描的位置在左手小拇指，在B-Mode上可以看出EDC肌腱中中間有明顯斷點，並且肌腱附近組織分布相當雜亂，
透過我的演算法(左上方)，可以看出新生血管從組織處生長進肌腱內部的過程，

值得一提的是，左上方第二張圖中用白色虛線框出的區域的影像，這經過分析後其實並不是血流訊號，而是因為雜訊濾除以及背景雜訊抑制不完全，所導致的。這樣的結果會對診斷以及後續的評估產生極大的誤差，這也是我們所不樂見的，

這也就是為甚麼我的演算法的處理過程都採取更嚴謹的方式將雜訊濾除。

![Untitled](/postImg/HFUDCEI/11.png)

### Subject evaluation

這裡我對兩組個案進行追蹤評估，第一組是復健周期較點的病人。

右邊紅色的手表示個案的受傷手，黑色框框表示健康手指與受傷手指的掃描區域

左邊第一列的超音波影像 為個案的正常手
第二列及第三列分別為第一次以及第二次收集的其中一個切面的超音波資料

而在統計結果中可以看到兩名個案受傷手的新生血管密度都大於5%，而受傷手的新生血管密度平均皆有變少的趨勢並且在Ttest統計上均具有顯著差異(P<0.05)。
依據這個結果可以說明個案們因受傷產生的新生血管正在慢慢減少中。

![Untitled](/postImg/HFUDCEI/12.png)

這是受傷後經過一年多時間的個案他的新生血管密度估計結果
右邊紅色的手表示個案的受傷手，黑色框框表示健康手指與受傷手指的掃描區域

第一列到第三列分別是正常手、第一次量測、第二次量測後的超音波影像
可以發現個案3的血管密度都不大於3%，並且正常手與57周量測的新生血管密度無顯著差異，
可以推測個案3經過一年的恢復治療後，新生血管密度已經趨近於正常手了。

![Untitled](/postImg/HFUDCEI/13.png)

## Conclusion

本研究提出了一種基於曲線結構增強技術的高頻超音波快速成像技術，並用於人類手指肌腱新生血管密度估計。

為了驗證HFUDCEI，我比較了不同微血管成像演算法，在小鼠腎臟與脾臟上面，結果說明我的演算法的影像品質都是更優秀的，CNR為20.76分貝，SNR為71.98分貝，以及最小血管直徑為35um

HFUDCEI在統計結果的顯示上有者與手部受傷相關論文相似的趨勢。

新生血管與肌腱撕裂傷的相關性在人體上幾乎沒有研究的，但是根據我們的研究結果顯示新生血管的變少與患者的恢復程度似乎有相關性，更具體的相關變化必須參考更多個案才能夠說明。



**更詳細的研究內容請參閱我的 Journal paper**

[Estimating the neovascularity of human finger tendon through high frequency ultrasound micro-Doppler imaging | IEEE Journals & Magazine | IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/9718199?casa_token=buwbNQLtrg8AAAAA:zO9amKBw2vI5zLsmVyoLL2bBUh75ZkP_GAhBtWWWxDe3hsgnBPYZ68rtzULKRDZXK5YDXqAWpg)
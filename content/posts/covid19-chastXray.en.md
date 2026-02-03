---
title: "Smart Medical Diagnostic Aid: ResNet50-Based Chest X-Ray Pneumonia Classifier"
slug: covid19-chestXray
date: 2022-04-22
categories:
- Graduate Project
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

This project aims to develop a deep learning-based automated diagnostic assistance system to help medical professionals quickly interpret chest X-ray images (CXR).

<!--more-->

---

## 📋 Abstract

This project aims to develop a deep learning-based automated diagnostic assistance system to help medical professionals quickly interpret chest X-ray images (CXR).

Addressing the challenge that COVID-19 and pneumonia features are difficult to distinguish visually on X-rays, this project uses **MATLAB** as the development environment and implements **ResNet50** for binary classification tasks (Normal vs. Pneumonia/COVID-19). Through the Residual Learning mechanism that solves the degradation problem of deep networks, the final model demonstrated excellent Recall on the test set, effectively screening potential pneumonia patients and reducing missed diagnosis risk.

---

## 🛑 The Problem

During pandemic peaks or in resource-limited regions, radiologists face enormous reading pressure. Traditional manual interpretation has the following pain points:

1.  **Time-Consuming:** Physicians need to focus for extended periods examining subtle pulmonary infiltration features.
2.  **Ambiguous Features:** Early pneumonia or COVID-19 ground-glass opacities closely resemble normal lung textures, easily causing misdiagnosis.
3.  **Fatigue Errors:** Visual fatigue from prolonged work may increase missed diagnosis rates.

---

## 🛠️ Technical Deep Dive

### 1. Data Preprocessing

The dataset contains two classes of chest X-ray images:

* **Normal:** Clear lung fields with no significant abnormal shadows.
* **Pneumonia (Pneumonia/COVID-19):** Lungs showing patchy shadows or consolidation.

To improve model generalization, I standardized the original images and resized them to ResNet50's required input dimensions ($224 \times 224$ pixels).

![Normal Chest X-Ray](/postImg/covid19-chastXray/1.jpg)
*Figure 1: Normal chest X-ray image with clear lung fields.*

![Pneumonia Chest X-Ray](/postImg/covid19-chastXray/2.jpg)
*Figure 2: Chest X-ray image showing pneumonia with visible fuzzy shadows in the lungs.*

### 2. Core Architecture: ResNet50 and Residual Learning

Traditional Convolutional Neural Networks (CNN) often encounter vanishing gradient or gradient explosion problems when layers deepen, causing training performance to actually decrease.

To train a network as deep as 50 layers, I adopted the **ResNet (Residual Network)** architecture. Its core innovation is introducing **"Shortcut Connections"**.

Assuming the input to a neural network layer is $x$ and the desired feature mapping is $H(x)$. ResNet doesn't directly learn $H(x)$, but learns the residual function $F(x) = H(x) - x$. The final output is:

$$y = F(x, \{W_i\}) + x$$

* $F(x, \{W_i\})$: Residual Mapping, the change the network layers need to learn.
* $x$: Identity Mapping, directly passing input information to output.

This $y = F(x) + x$ structure ensures that even in extremely deep networks, gradients can flow back directly through this "highway" of $x$, allowing the model to effectively capture extremely subtle pathological features in X-ray images.



### 3. Training Strategy

Training was performed using MATLAB's Deep Learning Toolbox.

* **Optimizer:** SGDM (Stochastic Gradient Descent with Momentum)
* **Loss Function:** Cross Entropy Loss (Binary Cross Entropy)

---

## 📊 Results & Analysis

Based on the test set Confusion Matrix, we quantitatively evaluated the model's performance:

![Confusion Matrix Results](/postImg/covid19-chastXray/3.png)
*Figure 3: Test set Confusion Matrix.*

### 1. Confusion Matrix Data Interpretation

Total test set samples: $N = 591$ images

* **True Positive (TP, Successfully predicted pneumonia):** 308 images
* **True Negative (TN, Successfully predicted normal):** 150 images
* **False Positive (FP, Incorrectly classified as pneumonia):** 84 images
* **False Negative (FN, Missed pneumonia):** 49 images

### 2. Key Metrics Calculation

* **Accuracy:**
    $$Accuracy = \frac{TP + TN}{Total} = \frac{308 + 150}{591} \approx 77.5\%$$
    The model's overall correct judgment rate is approximately 77.5%.

* **Recall / Sensitivity:**
    $$Recall = \frac{TP}{TP + FN} = \frac{308}{308 + 49} \approx 86.3\%$$
    **This is the most important metric in medical diagnosis.** Results show that among all actual pneumonia patients, the model successfully identified **86.3%** of cases. This means the model serves excellently as a "first-line screening defense," effectively reducing missed diagnoses.

* **Precision:**
    $$Precision = \frac{TP}{TP + FP} = \frac{308}{308 + 84} \approx 78.6\%$$
    Among cases the model classified as pneumonia, 78.6% were confirmed. Although some normal individuals were misclassified as pneumonia (84 false positive cases), in medical screening contexts, **"better to over-diagnose (False Positive) than to miss (False Negative)"** is an acceptable trade-off.

### Conclusion

This project successfully implemented automated chest X-ray classification using the ResNet50 architecture. Experimental data proves that through the residual learning mechanism, the model can effectively extract pulmonary lesion features and achieve **86.3% high sensitivity**. This system has the potential to become a radiologist's assistive tool, capable of processing large volumes of images in short time and flagging high-risk cases for priority physician review.



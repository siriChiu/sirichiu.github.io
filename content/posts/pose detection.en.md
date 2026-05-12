---
title: "MobileNet and Cloud-Collaborative Pose Recognition Application"
slug: pose detection
date: 2022-04-22
categories:
- Graduate Project
tags: 
- Python
- OpenPose
- MobileNet
- WebSocket
- Cloud Computing
- Deep Learning & Machine Learning
thumbnailImagePosition: left
thumbnailImage: /postImg/pose-detection/1.jpg
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

This project aims to address the lack of exercise motivation and digital divide among elderly people in an aging society. We developed an interactive game system based on AI body recognition, including "Memory Card Flip" and "Yoga Guidance," allowing seniors to exercise and rehabilitate at home using simple equipment.

<!--more-->


---

In implementation, this project addresses the low FPS of OpenPose on consumer-grade laptops with a **Cloud-Edge Collaboration Architecture**. The front-end device handles image capture and rendering, while AI inference is sent via **WebSocket** to **MobileNet + OpenPose** running on **Google Cloud Platform (GCP)**. This reduces the local hardware burden and improves interaction smoothness.

---

## 🛑 The Problem

During early development, we faced two main technical challenges:

1.  **Hardware Limitation:**
    OpenPose has high accuracy but extremely high computational cost. On regular non-gaming laptops (without dedicated GPU), even with lightweight MobileNet as the backbone, FPS was only single digits. This caused severe game latency, easily causing "3D sickness" or operational frustration for users.

2.  **Real-time Requirement:**
    Motion-sensing games need real-time feedback (e.g., raise your hand, the on-screen card flips immediately). If latency is too high, game playability approaches zero.

---

## 🛠️ Technical Deep Dive

To balance accuracy and fluidity, we transformed the architecture from "local computing" to "cloud streaming computing."

### 1. Core Model: MobileNet + OpenPose

We adopted **MobileNet** as OpenPose's feature extractor (Backbone). MobileNet uses **Depthwise Separable Convolution** to reduce parameters and computation.

Assuming input feature map size is $D_F \times D_F \times M$, kernel size is $D_K \times D_K$, output channel count is $N$.

* **Standard Convolution Computation:**
    $$C_{std} = D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F$$

* **Depthwise Separable Convolution Computation:**
    $$C_{depthwise} = D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F$$

This formula shows MobileNet reduces computation by approximately 8-9 times, which is the foundation for quickly processing large numbers of frames in the cloud.

### 2. System Architecture: Cloud Collaboration & WebSocket

To address insufficient local computing power, I designed a Client-Server separation architecture:

* **Client Side (Local Laptop):**
    * Role: **Thin Client**.
    * Tasks: Use OpenCV to read Webcam images, compress each frame (JPEG) and encode, transmit via network. Receive returned skeleton information and render on screen.
* **Server Side (Google Cloud Platform):**
    * Role: **Inference Engine**.
    * Tasks: Receive image stream, execute MobileNet + OpenPose inference, calculate coordinates $(x, y)$ of 18 human keypoints.
* **Communication Protocol (WebSocket):**
    * For Real-time, HTTP's three-way handshake overhead is too large.
    * We adopted **WebSocket** full-duplex communication protocol, establishing a persistent connection to ensure image packets can travel round-trip at millisecond speeds.

### 3. Game Logic & Interaction Design

By mapping AI-recognized skeleton coordinates to game logic:

* **Memory Card Game:**
    Detect "Wrist" node coordinates. When wrist coordinates hover over a virtual card area for more than 1 second (Hover), trigger the "flip card" event.


* **Yoga Imitation Game:**
    Calculate limb angle cosine similarity. For example, calculate the vector angle of "elbow-shoulder-hip," compare differences between user and standard poses, and provide scores.

---

## 📊 Results

Through cloud computing integration, the game frame rate (FPS) improved to a smoother playable level, with cross-platform support.

### 1. Card Flip Game Demo

![Pose detection card-control demo](/postImg/pose-detection/1.jpg)
*Figure 1: User controls virtual cards remotely using hand movements. The system uses wrist position to trigger contactless interaction.*

### 2. Yoga Game Demo

![Pose detection interaction result](/postImg/pose-detection/2.jpg)
*Figure 2: System compares user pose (yellow skeleton) with standard movement (upper right icon) in real-time, providing instant score feedback.*

### Conclusion

This project shows that, in hardware-limited scenarios, **Architecture Design** can move heavier AI computation to the cloud and use WebSocket to reduce transmission overhead. This lowers the user hardware barrier and provides a more accessible home-exercise interaction pattern for seniors.

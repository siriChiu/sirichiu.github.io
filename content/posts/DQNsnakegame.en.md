---
title: "Deep Q-Network in Practice: A TensorFlow-Based Four-Layer Neural Network Snake Agent"
slug: DQNsnakegame
date: 2022-04-22
categories:
- Graduate Project
tags: 
- Python
- TensorFlow
- Reinforcement Learning
- Deep Q-Network
- Deep Learning/Machine Learning

thumbnailImagePosition: left
thumbnailImage: /postImg/DQNsnakegame/1.png
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

This project applies Deep Reinforcement Learning to the classic Snake game. To enable the Agent to make optimal decisions in a dynamic environment, I designed a **custom four-layer fully connected network** using the **TensorFlow** framework as the core Q-Network.

<!--more-->


---

By designing an 11-dimensional environment feature vector as input and combining it with Bellman Equation for Q-value iterative updates, the model successfully learned obstacle avoidance, path planning, and long-term survival strategies. This project demonstrates the complete AI development process from environment setup, model architecture design, to reward function optimization.

---

## 🛑 Motivation & Challenge

In reinforcement learning, designing a network architecture that is "deep enough but not overfitting" to handle the state space is the key to success.

1.  **State Feature Extraction:** Snake's decisions depend on relative positions (Where is the food? Is there danger nearby?) rather than absolute coordinates.
2.  **Sparse Reward:** The snake only receives positive feedback when eating food; the rest of the time it's just moving. If the network architecture is too simple, it's difficult to capture the relationship between "movement" and "future rewards"; if too complex, training convergence is too slow.

---

## 🛠️ Technical Deep Dive

### 1. State Representation

To reduce input dimensions and accelerate convergence, I abandoned raw image input (CNN) and instead adopted feature engineering, condensing the current situation into an **11-dimensional Boolean Vector** $S_t$:

> *[Image placeholder: Recommend inserting a diagram showing the 11 sensor value definitions around the snake head]* 

* **Danger Perception (3):** [Danger ahead, Danger to the right, Danger to the left]
* **Movement Direction (4):** [Left, Right, Up, Down] (One-hot encoding)
* **Food Direction (4):** [Food to the left, Food to the right, Food above, Food below]

### 2. Model Architecture Design

This is the core of the project. To capture nonlinear relationships between state features (e.g., "food is to the left" AND "danger on the left" $\rightarrow$ should "go up or down"), I built a **four-layer Dense network** using TensorFlow/Keras.

Mathematical representation:

$$f(x) = W_4 \cdot \sigma(W_3 \cdot \sigma(W_2 \cdot \sigma(W_1 \cdot x + b_1) + b_2) + b_3) + b_4$$

* **Input Layer:** Receives the 11-dimensional state vector.
* **Hidden Layer 1 & 2 (Dense):** Through two hidden layers (with ReLU activation function $\sigma$) for feature crossing and extraction, increasing the model's expressive power to understand complex dead-end structures.
* **Output Layer:** Outputs 3 Q-values corresponding to expected rewards for [Go straight, Turn right, Turn left].

> *[Image placeholder: Recommend inserting neural network architecture diagram showing Input(11) -> Dense -> Dense -> Output(3) layer structure]* 

### 3. DQN Algorithm & Optimization

Using TensorFlow's automatic differentiation capability, I implemented the DQN training loop:

* **Prediction:** Use `model.predict(state)` to get Q-values for current actions.
* **Target Q:** Calculate according to Bellman Equation:
    $$Q_{target} = R + \gamma \cdot \max(Q_{next\_state})$$
* **Training:** Use `model.fit()` to minimize the loss function, using Mean Squared Error (MSE) to make predictions approach target values.

### 4. Reward Shaping

To guide the snake to learn more efficiently, I designed a refined reward mechanism:

* **Survival & Eating:** Food eaten $+10$, Death $-10$.
* **Guidance Strategy:** If an action **shortens** the distance between snake head and food, give a small reward; if it **increases** the distance, give a small penalty. This solved the problem of the snake spinning in place during early training.
* **Time Penalty:** Deduct $-0.1$ per step, forcing the model to find the shortest path.

![Untitled](/postImg/DQNsnakegame/1.png)

---

## 📊 Results & Reflection


After multiple training iterations (Epochs), the Agent's behavioral evolution was observed:

1.  **Random Phase:** Model hasn't converged yet, snake frequently hits walls.
2.  **Obstacle Avoidance Phase:** Hidden layers learned to recognize "danger features," snake can survive for long periods but circles the field.
3.  **Goal-Oriented:** The four-layer architecture successfully integrated "food direction" with "path planning," snake exhibits clear hunting behavior.

### Conclusion

By implementing this custom four-layer DQN model with TensorFlow, I validated the powerful capability of **Deep Neural Networks (DNN)** in handling decision problems. This project not only familiarized me with TensorFlow's model construction API but also gave me a deep appreciation for the decisive impact of network depth and reward function design on reinforcement learning performance.


{{< video src="/videos/DQNsnakegame.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="720" height="480">}}

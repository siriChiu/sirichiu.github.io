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
- Deep Learning & Machine Learning

thumbnailImagePosition: left
thumbnailImage: /postImg/DQNsnakegame/1.png
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

This project applies Deep Reinforcement Learning to the classic Snake game. To help the agent choose reasonable actions from changing game states, I designed a four-layer fully connected network in **TensorFlow** as the core Q-Network.

<!--more-->


---

By using an 11-dimensional environment feature vector and Bellman Equation updates, the model gradually learned obstacle avoidance, food-seeking behavior, and longer survival. This project documents a reinforcement learning implementation from environment setup and model design to reward-function tuning.

---

## 🛑 Motivation & Challenge

In reinforcement learning, designing a network architecture that is "deep enough but not overfitting" to handle the state space is the key to success.

1.  **State Feature Extraction:** Snake's decisions depend on relative positions (Where is the food? Is there danger nearby?) rather than absolute coordinates.
2.  **Sparse Reward:** The snake only receives positive feedback when eating food; the rest of the time it's just moving. If the network architecture is too simple, it's difficult to capture the relationship between "movement" and "future rewards"; if too complex, training convergence is too slow.

---

## 🛠️ Technical Deep Dive

### 1. State Representation

To reduce input dimensions and accelerate convergence, I abandoned raw image input (CNN) and instead adopted feature engineering, condensing the current situation into an **11-dimensional Boolean Vector** $S_t$:

![DQN Snake 11-dimensional state vector design](/postImg/DQNsnakegame/state-vector.svg)

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

![DQN four-layer Q-Network architecture](/postImg/DQNsnakegame/q-network.svg)

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

![Snake agent training result screen](/postImg/DQNsnakegame/1.png)

---

## 📊 Results & Reflection


After multiple training iterations (Epochs), the Agent's behavioral evolution was observed:

1.  **Random Phase:** Model hasn't converged yet, snake frequently hits walls.
2.  **Obstacle Avoidance Phase:** Hidden layers learned to recognize "danger features," snake can survive for long periods but circles the field.
3.  **Goal-Oriented:** The four-layer architecture uses both food-direction and danger-perception features, and the snake gradually shows goal-directed behavior.

### Conclusion

By implementing this four-layer DQN model with TensorFlow, I learned how state design, network depth, and reward shaping jointly affect reinforcement learning convergence. The project also helped me practice TensorFlow model construction APIs and training-loop implementation.


{{< video src="/videos/DQNsnakegame.mp4" type="video/mp4" preload="auto" autoplay="true" loop="true" width="720" height="480">}}

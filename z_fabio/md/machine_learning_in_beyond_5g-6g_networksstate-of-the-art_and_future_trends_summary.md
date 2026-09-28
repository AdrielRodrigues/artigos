---
index_terms:
  - 6G wireless networks
  - machine learning
  - reinforcement learning
  - intelligent reflecting surfaces
  - network optimization
  - beamforming
  - resource allocation
---

# Machine Learning in Beyond 5G/6G Networks—State-of-the-Art and Future Trends

## 1. Introduction
As commercial 5G deployments struggle to meet the demands of skyrocketing traffic and real-time service requirements, research is shifting toward sixth-generation (6G) systems. Machine Learning (ML), as a subset of Artificial Intelligence (AI), is positioned as a critical tool for 6G due to its ability to make data-driven decisions and estimate parameters without relying on conventional mathematical models. This paper reviews the state-of-the-art ML methods—supervised, unsupervised, and reinforcement learning—and their applications in optimizing wireless communication systems.

## 2. 6G Network Requirements and Challenges
6G must handle a projected global mobile traffic volume of 5016 exabytes per month by 2030. To address these loads, 6G focuses on creating "smart radio environments" using Intelligent Reflecting Surfaces (IRS) to control signal reflection via induced phase changes, as well as operating in higher frequency bands (mm-wave and THz).

Key performance requirements for 6G compared to 5G include:
*   **Data Rates:** Peak rates of 1 Tbps (10–100x greater than 5G).
*   **Latency:** Reduction from 10 ms down to less than 1 ms.
*   **Spectrum:** Expansion up to 1000 GHz.
*   **Mobility:** Support for speeds up to 1000 km/h.
*   **Reliability:** Improvement to 99.99999%.
*   **Services:** Integration of Extended Reality (XR), the Internet of Everything (IoE), and holographic-type communication.

## 3. Machine Learning
ML models learn system features that are too complex for traditional mathematical modeling. They are categorized into three primary types:

### 3.1. Supervised Learning
Trained on labeled datasets where both input and desired output are known. Key algorithms include:
*   **Artificial Neural Networks (ANNs) & Deep Learning (DNNs):** Used for resource allocation and cell association; Autoencoders can be used for unsupervised pre-training.
*   **k-Nearest Neighbor (kNN):** A distance-based classifier effective for multi-class problems but computationally expensive for large datasets.
*   **Naive Bayes:** A probabilistic model based on Bayes' theorem, efficient for high-dimensional data assuming feature independence.
*   **Decision Trees & Random Forests:** Tree-based structures that maximize information gain; Random Forests reduce overfitting by aggregating multiple trees.
*   **Convolutional Neural Networks (CNNs):** Optimized for pattern recognition and image classification via convolutional and pooling layers.
*   **Recurrent Neural Networks (RNNs) & LSTM:** Designed for sequential/time-series data; LSTMs specifically address the vanishing gradient problem.

### 3.2. Unsupervised Learning
Trained on unlabeled data to find hidden patterns or clusters. Key algorithms include:
*   **K-means:** Clusters data based on distance to centroids; performance is highly dependent on the choice of $k$.
*   **Self-Organizing Maps (SOM):** Uses competitive learning for dimensionality reduction and clustering.
*   **Autoencoders:** Neural networks that learn efficient data codings by attempting to reconstruct the input at the output.
*   **Principal Component Analysis (PCA):** Reduces dimensionality by projecting data onto orthogonal axes of maximum variance.
*   **Hidden Markov Models (HMM) & Restricted Boltzmann Machines (RBM):** Used for sequence modeling and encoding probability distributions, respectively.

### 3.3. Reinforcement Learning
An agent-based trial-and-error process where a model learns an optimal policy by maximizing a reward signal from its environment. 
*   **Value-Based:** Includes Q-learning (off-policy greedy approach) and SARSA (on-policy).
*   **Policy-Based:** Includes Policy Gradient (PG), Proximal Policy Optimization (PPO), and Actor-Critic (A2C) models, which learn both a policy (actor) and a value function (critic).
*   **Deep Reinforcement Learning (DRL):** Integrates deep learning to enable RL to operate in high-dimensional state and action spaces.

## 4. Beyond 5G/6G Applications and Machine Learning

### 4.1. Supervised Learning
#### 4.1.1. Optimization Problems
Supervised methods are used for predicting path loss (Random Forest, kNN), joint user association and power allocation (semi-supervised GRL/SRL), and dynamic bandwidth allocation (ANN). DNNs are employed to predict UAV network requirements, while RNNs help in intelligent load balancing (APRIL model). Other applications include Cooperative Spectrum Sensing (ANN, SVM), data rate prediction (Random Forest), and MISO beamforming (DNN).

#### 4.1.2. Fault/Anomaly Management
Extended Support Vector Machines (Support Tucker Machine) are used for outlier detection in big sensor data within IoT systems to improve accuracy.

#### 4.1.3. Channel Estimation/Allocation
DNN estimators provide more accurate channel predictions than conventional algorithms. Deep supervised learning is also applied to adaptive bit allocation in heterogeneous networks to reduce feedback overhead.

#### 4.1.4. Beam Selection
In mm-wave communications, kNN and SVC are used for multi-class beam selection. DNNs and Gated Recurrent Units (GRU) help reduce beam overhead and predict serving base stations for drones based on trajectory.

#### 4.1.5. Caching/Computing
ANNs and DNNs optimize code caching and IoT system caching to approach optimal performance levels of conventional methods.

#### 4.1.6. Security
Decision trees combined with eXplainable AI (XAI) improve trust in intrusion detection systems. LSTMs (using the Nadam optimizer) and CNNs are used for high-accuracy malware traffic classification and detection.

#### 4.1.7. MIMO
Massive MIMO CSI prediction utilizes combinations of CNNs with Autoregressive Networks (ARN) and RNNs to handle channel aging. Deep supervised mapping reduces training and feedback overhead in space-frequency domain mapping.

#### 4.1.8. UAV
Supervised DL combines clustering with CNNs for joint caching and trajectory optimization. ANNs and SVMs are used to detect GPS spoofing, jamming, and intrusion attacks, while ensemble methods predict Received Signal Strength (RSS).

### 4.2. Unsupervised Learning
#### 4.2.1. Optimization Problems
K-means is applied to user selection and power allocation in NOMA systems. LSTMs and CNNs are used for modulation recognition and unsupervised cell event detection/classification.

#### 4.2.2. Fault Management
SOMs have been found to outperform Fuzzy C-means and K-means in predicting faults. "K-Aware K-means" self-optimizes the $k$ value to detect anomalies with high accuracy (99.7%).

#### 4.2.3. Channel Estimation
Unsupervised DL models, such as DetNet and LSTMs, are used for channel detection in molecular communication, specifically addressing inter-symbol interference.

#### 4.2.4. User Mobility Estimation
Discrete-time Markov chains and HMMs predict user trajectories and locations by treating the network as a state-transition graph. Unsupervised UE association algorithms optimize data rates at RF and THz frequencies.

#### 4.2.5. Security
Non-parametric Bayesian methods assist in IoT authentication. GMMs enhance Physical Layer security, while combinations of CNN and Stacked Encoders (SAE) are used for intrusion detection.

#### 4.2.6. UAV Networks
K-means is used to cluster users spatially before deploying a UAV as a base station; MLP and LSTM models predict optimal UAV locations to maximize throughput.

#### 4.2.7. MIMO
Unsupervised DNNs are used for fast beamforming design in single BS MIMO systems, maximizing the sum-rate while increasing computational speed.

#### 4.2.8. Visible Light Communications (VLC)
VLC provides high data rates and security for indoor and V2X communications. Unsupervised methods like K-means and CAPD are used to reduce non-linearity in VLC systems and serve as pre-distorters.

### 4.3. Reinforcement Learning
#### 4.3.1. Optimization Problems
RL is extensively used for spectrum allocation (NAAC for D2D, GAN-DDQN for network slicing) and resource allocation (Q-learning to minimize outage probability). Deep RL optimizes power allocation using delayed CSI and maximizes SNR in IRS communications.

#### 4.3.2. Caching/Computing
DRL (MDP-based) and Actor-Critic models optimize caching in MEC networks by maximizing cache hit rates and reducing transmission delay. Multi-Agent Multi-Armed Bandit (MAMAB) approaches allow online learning of caching strategies.

#### 4.3.3. Channel Estimation/Allocation
RL based on auction theory and MDPs are used for channel allocation in LTE, 5G, and dense WLANs to enhance throughput.

#### 4.3.4. Energy Consumption/Harvesting
Q-learning and DRL reduce energy consumption in cooperative networks. Hybrid Actor-Critic (Hybrid-AC) algorithms optimize dynamic computation offloading by balancing time and energy costs.

#### 4.3.5. Handover
Offline RL reduces excess handovers, while DRL utilizing camera images enables proactive handover timing in mm-wave systems by predicting data rate drops before they occur.

#### 4.3.6. V2V
DRL maps observations to optimal resource allocation to minimize interference and satisfy latency constraints on V2V links.

#### 4.3.7. UAV
Two-stage DRL optimizes offline content placement and online user tracking (via DDQN) while adhering to energy constraints.

#### 4.3.8. Security
DRL provides robustness against jamming attacks. Multi-agent RL (MARL) enables collaborative spectrum sharing for defense, and specialized RL models boost secrecy rates in IRS-aided environments using prioritized experience replay.

#### 4.3.9. Visible Light Communication
Multi-agent DQN and Q-learning optimize power allocation in hybrid RF/VLC networks, improving convergence rates over typical Q-learning.

#### 4.3.10. Fault/Anomaly Management
Deep Q-learning is applied to fault detection and diagnosis, achieving high accuracy with fewer required features.

## 5. Open Issues
The authors identify several unresolved challenges:
*   **Time Convergence:** Long convergence times in ML can hinder performance in highly dynamic wireless environments.
*   **Resource Allocation for e-Health:** Harmonizing network resources across diverse technologies for wearable sensors is an ongoing challenge.
*   **QoS and QoE Balancing:** Creating cross-layer ML protocols that can balance conflicting requirements (e.g., high throughput for video vs. high security for payments).
*   **UAVs as Intelligent Service (UaaIS):** The need for energy-efficient training and inference given the limited battery life of UAVs acting as edge trainers.
*   **CSI Acquisition in IRS:** High training overhead and the passive nature of IRS make accurate CSI acquisition difficult, requiring ML to move beyond linear correlations.

## 6. Future Trends

### 6.1. Model Agnostic Meta Learning (MAML)
Meta-learning aims for "learning to learn." MAML allows for fast adaptation to new tasks with very few samples by finding a sensitive parameter initialization. Potential applications include reducing the sample size needed for DNN training in wireless channels and improving IoT demodulation via online meta-learning.

### 6.2. Generative Adversarial Networks (GANs)
GANs utilize a minimax game between a Generator and a Discriminator to create realistic data samples. In 6G, GANs can pre-train DRL frameworks for URLLC resource allocation or optimize UAV trajectories and power settings with high convergence speeds.

## 7. Conclusions
The paper concludes that ML is indispensable for realizing the capabilities of 6G. By summarizing supervised, unsupervised, and RL applications across beamforming, security, caching, and energy management, the authors demonstrate how data-driven models overcome traditional mathematical limitations in wireless communication.
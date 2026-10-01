---
index_terms:
  - vertical federated learning
  - cloud radio access network
  - over-the-air computation
  - convergence analysis
  - system optimization
  - fronthaul quantization
---

# Vertical Federated Learning Over Cloud-RAN: Convergence Analysis and System Optimization

## I. Introduction
Vertical Federated Learning (VFL) allows devices to collaboratively train a model using feature-partitioned datasets (shared samples, different features). Unlike horizontal FL, VFL requires full device participation because each participant holds a unique sub-model of the global model. This creates a communication bottleneck as the volume of intermediate outputs is proportional to the number of training samples.

To address these challenges, the authors propose a Cloud Radio Access Network (Cloud-RAN) architecture utilizing Over-the-Air Computation (AirComp). AirComp enables efficient aggregation via waveform superposition in the wireless medium, reducing latency and radio resource consumption. The Cloud-RAN structure—consisting of distributed remote radio heads (RRHs/edge servers) coordinated by a central baseband unit (BBU) pool—alleviates the "straggler" problem (devices with poor channel conditions) by shortening the communication distance between devices and edge servers.

The paper specifically focuses on mitigating two sources of error: AirComp aggregation errors and quantization errors stemming from limited fronthaul capacity between RRHs and the BBU. The core contributions include a convergence analysis characterizing the impact of these errors and a system optimization framework for joint transceiver and quantization design.

## II. System Model

### A. Vertical Federated Learning
The VFL goal is to minimize an empirical risk function $F(\boldsymbol{w})$ consisting of a sample-wise loss and regularization terms. The global model $\boldsymbol{w}$ is split into local sub-models $\boldsymbol{w}_k$. Training involves a cyclical process: 
1. Devices compute local predictions $g_k$ based on their features.
2. These are aggregated by the central server to produce a final prediction via a non-linear transformation $\sigma(\cdot)$.
3. The central server computes an auxiliary function $G_i$ and broadcasts it back to devices.
4. Devices use $G_i$ and local gradients of $g_k$ to update their sub-models using gradient descent (GD).

### B. Over-the-Air Computation Based Cloud Radio Access Network
The proposed architecture consists of $K$ single-antenna devices, $N$ edge servers with $M$ antennas each, and one central server. The system uses digital fronthaul links with a total capacity constraint $C$.

#### 1) Uplink Transmission Model
Devices transmit local predictions simultaneously using AirComp. Edge servers receive these superposed signals, quantize them to fit limited fronthaul capacity (modeled via rate-distortion theory as Gaussian quantization noise), and forward them to the central server. The central server uses a receive beamforming vector $\boldsymbol{m}^{(t)}$ and a power control factor $\eta^{(t)}$ to estimate the aggregated signal $\hat{s}^{(t)}(i)$, introducing effective uplink noise $n_{\text{UL}}^{(t)}(i)$.

#### 2) Downlink Transmission Model
The central server computes the auxiliary result $G_i(\hat{s}^{(t)}(i))$, beamforms it via $\boldsymbol{u}_n^{(t)}$, and sends it to edge servers over quantized fronthaul links. Edge servers broadcast these signals to devices. Devices scale the received signal with a receive scalar $b_{\text{DL},k}^{(t)}$ to estimate $\hat{G}_{i,k}$. This process introduces effective downlink noise $n_{\text{DL},k}^{(t)}(i)$.

## III. Convergence Analysis

### A. Zero-Forcing Precoding
To eliminate channel fading distortion, the authors employ zero-forcing precoding by designing transmit and receive scalars to invert the channel effects. While this ensures unbiased estimations of the aggregated signals (under the assumption that noise amplitude is small), communication noises $n_{\text{UL}}^{(t)}$ and $n_{\text{DL},k}^{(t)}$ still persist and degrade performance.

### B. Convergence Result
Assuming $\alpha$-strong convexity and $\beta$-smoothness of the objective function, Theorem 1 proves that the expected optimality gap between the trained model and the optimal solution is upper-bounded by a term $B(T)$. This gap depends on the contraction rate $\rho$ and a weighted sum of uplink and downlink noise variances ($\sigma_{\mathrm{UL}}^{2}$ and $\sigma_{\mathrm{DL},k}^{2}$). This result establishes that communication noise creates a non-zero optimality gap, motivating the need for system optimization to minimize $B(T)$.

## IV. System Optimization

### A. Problem Formulation
The objective is to minimize the optimality gap $B(T)$ subject to total fronthaul capacity constraints and maximum transmit power constraints. The problem is decomposed into two independent sub-problems: one for uplink (optimizing $\boldsymbol{m}^{(t)}$ and $\boldsymbol{Q}_{\mathrm{UL}}^{(t)}$) and one for downlink (optimizing $\boldsymbol{u}^{(t)}$ and $\boldsymbol{Q}_{\mathrm{DL}}^{(t)}$).

### B. Optimization Framework

#### 1) Uplink Optimization
The uplink problem is solved via alternating optimization:
*   **Beamforming ($\boldsymbol{m}$):** Formulated as a min-max problem to minimize the worst-case noise across devices. It is solved using Successive Convex Approximation (SCA) by converting complex variables to the real domain and linearizing concave functions.
*   **Quantization ($\boldsymbol{Q}_{\mathrm{UL}}$):** With fixed beamforming, the problem becomes convex and is solved using CVX.

#### 2) Downlink Optimization
The downlink problem involves a non-convex capacity constraint. The authors use a lemma to approximate this as a convex constraint (linearizing the log-determinant). The resulting problem is solved via an Alternate Convex Search (ACS) approach, alternating between updating the quantization covariance $\boldsymbol{Q}_{\mathrm{DL}}$, the transmit beamforming vector $\boldsymbol{u}$, and an auxiliary variable $\boldsymbol{\Sigma}$.

## V. Numerical Results

### A. Simulation Settings
The authors tested a regularized logistic regression model on the Fashion-MNIST dataset with 49 devices. The communication setup included $N=8$ edge servers in a circular area of radius 500m.

### B. Convergence of the Proposed Algorithm
Simulations show that the proposed algorithm achieves linear convergence of the optimality gap. Higher downlink power constraints lead to smaller gaps due to improved SNR.

### C. Impact of Key System Parameters
Joint optimization of beamforming and quantization significantly outperforms baselines using uniform settings. At low fronthaul capacity, quantization optimization provides the most gain. As capacity increases, optimized beamforming becomes more critical. Increasing the number of antennas $M$ at edge servers improves performance up to a point of saturation (approximately $M=10$).

### D. Cloud-RAN Versus Massive MIMO
Comparing a distributed system (Cloud-RAN) with a centralized one (Massive MIMO) for the same total antenna count shows that Cloud-RAN is superior when $N \ge 2$. This is because distributing antennas across multiple RRHs mitigates the straggler issue by ensuring devices are closer to at least one server, improving overall channel conditions.

## VI. Conclusion
The paper demonstrates that a Cloud-RAN architecture using AirComp can support communication-efficient VFL. By characterizing the convergence behavior and jointly optimizing transceiver beamforming and fronthaul quantization, the authors successfully minimized the optimality gap caused by wireless noise and limited capacity. Numerical results validate that distributed antenna systems are more effective than centralized ones for VFL in large-scale IoT scenarios.
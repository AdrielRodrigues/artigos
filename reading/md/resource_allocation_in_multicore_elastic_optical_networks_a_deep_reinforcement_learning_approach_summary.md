---
index_terms:
  - Multicore Fiber Elastic Optical Networks
  - Deep Reinforcement Learning
  - Resource Allocation
  - RMSCA Problem
  - Blocking Probability
  - Intercore Crosstalk
---

# Resource Allocation in Multicore Elastic Optical Networks: A Deep Reinforcement Learning Approach

## 1. Introduction
The rapid increase in global Internet traffic, driven by high-consumption applications and the rollout of 5G, threatens to exceed the capacity of current core optical networks. To address this "capacity crunch," two primary technologies are proposed: Elastic Optical Networks (EONs), which enhance spectral efficiency using frequency slot units (FSUs), and multicore fiber (MCF), which increases total capacity by providing multiple transmission cores within a single cladding. The combination of these, termed dynamic MCF-EONs, is essential for future 6G services like tactile Internet and high-definition 3D streaming.

The primary technical challenge in dynamic MCF-EONs is the Routing, Modulation, Spectrum, and Core Allocation (RMSCA) problem. While traditional rule-based heuristics are computationally efficient, they rely heavily on expert design and often miss non-obvious optimal policies. Deep Reinforcement Learning (DRL) offers a potential alternative by allowing an agent to learn resource allocation strategies through experience.

### 1.1 Related Work
Previous DRL applications in EONs have focused on routing, modulation, and spectrum assignment (RMSA) in single-domain, multidomain, multiband, and survivable networks. However, prior work on MCF has been limited to fixed-grid networks or supervised machine learning used only as an auxiliary tool for predicting traffic or crosstalk (XT), rather than for direct decision-making.

### 1.2 Paper Contribution
This paper introduces the first application of DRL to solve the RMSCA problem in dynamic MCF-EONs. The authors develop a new simulation environment and train four different DRL agents, comparing their blocking performance against three established baseline heuristics.

## 2. DRL for Dynamic MCF-EONs
The resource allocation problem is modeled as a Markov Decision Process (MDP) defined by the tuple $\{S, A, T, R, s_0, \gamma\}$.
*   **States ($S$):** Represented by link spectrum utilization per core on candidate routes, source and destination nodes, holding time, and bitrate.
*   **Actions ($A$):** Defined as a triplet $(k, c, j)$ consisting of the selected route, the specific fiber core, and the contiguous block of slots.
*   **Transition Probability ($\mathcal{T}$):** The likelihood of moving to a new state given an action and a connection request.
*   **Reward ($R$):** A binary reward system where successful allocations receive 1 and rejections receive -1.
*   **Initial State ($s_0$):** An empty network with all spectrum slots available across all cores.
*   **Discount Factor ($\gamma$):** Adjusts the weight of future versus immediate rewards.

The state is numerically represented as a 1D array including one-hot encoded node identifiers and specific metrics for each route/core combination, such as block size, first slot index, FSUs required (based on modulation), average available FSUs, and total available FSUs.

### 2.1 Stage 1: Environment Design and Implementation
The authors extended the `Optical RL-Gym` toolkit to create `DeepRMSCAEnv`, which consists of a dynamic MCF-EON simulator and a feature engineering module.

**Dynamic MCF-EON Simulator components:**
*   **Network Information & Utilization:** Stores graph topology, capacity, precomputed routes, modulation formats, and the current status (used/available) of every slot in every core.
*   **Traffic Generator:** Randomly generates connection establishment and release requests.
*   **Request Processor:** Determines required slots based on the most efficient modulation format that meets Quality of Transmission (QoT) requirements. It verifies resource availability and crosstalk feasibility via the XT Calculator.
*   **XT Calculator:** Computes intercore crosstalk (XT). For triangular/hexagonal core arrangements, it uses an approximation formula to calculate mean XT affecting a connection based on coupling coefficients and link length. If XT exceeds predefined thresholds for the selected modulation format, the request is rejected.

**Feature Engineering Module components:**
*   **Reward Generator:** Assigns rewards based on whether the Request Processor accepted the connection or rejected it due to spectrum lack, XT thresholds, or optical reach limits.
*   **Routes Utilization:** Consolidates slot utilization data for $K$ candidate routes into a 1D vector for the agent.
*   **Experience Data Generator:** Populates an experience buffer with $(a_t, s_t, r_t, s_{t+1})$ tuples for training.

### 2.2 Stage 2: Agent Training
The agent's goal is to maximize long-term cumulative rewards by optimizing its policy—the mapping of network states to resource allocation actions (route, core, and slot). Each request requires a specific number of slots based on the modulation format, plus one slot as a guard band.

#### 2.2.1 Policy
The policy determines the action most likely to avoid blocking. An example provided shows that an agent must consider not only spectral availability but also potential crosstalk; choosing a route with available slots may still result in failure if intercore XT exceeds acceptable thresholds.

#### 2.2.2 Learning Algorithm
Because the action space is multi-discrete (selecting from multiple discrete sets of routes, cores, and slots), four algorithms from the `Stable Baselines` library were tested:
1.  **A2C & ACKTR:** Actor-Critic methods using two neural networks (one for policy and one for value estimation). ACKTR uses a Kronecker-factored approximation to speed up gradient updates.
2.  **PPO2 & TRPO:** Policy gradient methods using a single network. TRPO employs a trust region (Kullback–Leibler restriction) to prevent drastic, unstable updates to neural network weights, while PPO2 optimizes the descent curve without such strict limits.

## 3. Performance Evaluation
Experiments used NSFNet and COST239 topologies with 3 cores per link (triangular geometry), 100 FSUs, and modulation formats ranging from BPSK to 16-QAM. Traffic is modeled as a Poisson process with exponentially distributed holding times and bitrates between 25–100 Gbps. Agents were trained over 160,000 connection requests.

### 3.1 Preliminary Training Results
Training results indicate that A2C and TRPO agents are the most effective, achieving rewards close to the maximum of 50 per episode. PPO2 and ACKTR performed poorly with default parameters, often getting stuck in local optima or behaving randomly. TRPO showed the most monotonic improvement. When compared to the kSP-FF-FCA baseline heuristic, A2C and TRPO achieved significant reductions in blocking probability during steady-state operation.

### 3.2 TRPO Training Results
The TRPO agent was tested across traffic loads from 500 to 3000 Erlang. The blocking probability increased linearly with load as expected. Convergence to a steady state occurred after approximately 130,000 to 150,000 timesteps regardless of the specific load level.

### 3.3 TRPO Agent VS. Heuristic: Blocking Performance
The trained TRPO agent was compared against three heuristics: KSP-FF-FCA (First Fit), KSP-RF-RCA (Random), and KSP-SCMA XT/demand-aware. In the C-band (320 FSUs), the TRPO agent significantly outperformed all heuristics. On average, at loads above 2000 Erlang, the TRPO agent reduced blocking probability by a factor of four compared to the best heuristic (KSP-SCMA).

The results suggest that DRL agents can generalize across different traffic loads and spectrum resources. However, they do not generalize across topologies; an agent trained on NSFNet does not perform well on COST239, and vice versa.

## 4. Conclusion
The study demonstrates that a DRL approach to the RMSCA problem in dynamic MCF-EONs provides a substantial performance advantage over traditional rule-based heuristics. Future work should investigate hyperparameter tuning, Graph Neural Networks (GNNs) for topology generalization, larger core counts, and differentiated reward schemes based on specific blocking causes (e.g., fragmentation vs. crosstalk). The authors also propose using explainability techniques to derive better human-designed heuristics from the agent's learned policies.
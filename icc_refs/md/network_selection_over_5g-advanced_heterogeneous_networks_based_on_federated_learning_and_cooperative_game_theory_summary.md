---
index_terms:
  - 5G-Advanced
  - Federated Learning
  - Double Deep Q-Network
  - Cooperative Game Theory
  - Network Slicing
  - O-RAN
  - Load Balancing
---

# Network Selection Over 5G-Advanced Heterogeneous Networks Based on Federated Learning and Cooperative Game Theory

## I. Introduction
Future wireless networks (5G-Advanced and Beyond) aim to create a 3D ecosystem integrating terrestrial networks (TN) and non-terrestrial networks (NTN)—such as UAVs, HAPs, and satellites—to ensure seamless coverage and capacity for high-demand applications (e.g., XR, cloud gaming). These environments utilize high-frequency bands (mmWave/THz) and network slicing to manage differentiated traffic via logical partitions of physical resources.

The paper proposes the enhanced Dynamic Radio Access Network Selection (**eDRANS**) algorithm within the O-RAN architecture. eDRANS utilizes **Federated Double Deep Q-Network (F-DDQN)** for base station (BS) selection and **Cooperative Game Theory (CGT)** for load balancing during overload. The goal is to optimize Quality of Service (QoS) and slice utilization while accommodating users with different priorities, mobility patterns, and service requirements.

## II. Related Works
### A. Network Selection and Slicing Resource Allocation
Traditional heuristic methods like Multi-Attribute Decision-Making (MADM) suffer from high computational complexity in massive, dynamic environments. While Deep Reinforcement Learning (DRL) offers a trial-and-error approach to solve complex state spaces, centralized schemes lack scalability, and distributed schemes are suboptimal as they ignore peer data. Federated Learning combined with DRL (F-DRL) is identified as a superior alternative because it enables collaborative training while preserving data privacy and reducing communication overhead.

### B. Load Balancing
Load balancing is critical during network saturation to accept new users without abruptly degrading the experience of active ones. Most existing works either use fixed resource allocation or simple redistribution. eDRANS differs by employing CGT to dynamically adjust resources among active users based on service performance and Service Level Agreements (SLA).

## III. Overview of the Proposed Solution
### A. The O-RAN Framework
The proposal is integrated into the O-RAN architecture:
*   **Non-RT RIC:** Acts as a Service Management and Orchestration framework that trains/updates the **ML Global Model** via rApps and distributes policies (A1) to the Near-RT RIC.
*   **Near-RT RIC:** Executes optimization actions through xApps in control loops (10ms–1s). It hosts multiple **ML Local Models** (one per BS) and a **Selector Module**.
*   **Workflow:** ML Local Models provide preference statements based on local data; the Selector Module makes the final decision based on these outputs. Model parameters are periodically aggregated in the Non-RT RIC using Federated Averaging (FedAvg), ensuring privacy as raw user data is never transmitted.

### B. System Model
The system serves users ($\mathbb{U}$) with two priority levels: high (premium) and low (regular). BSs ($\mathbb{B}$) consist of terrestrial ($\mathbb{T}$) and non-terrestrial ($\mathbb{N}$) nodes. Services ($\mathbb{L}$), including Video (VI), Virtual Reality (VR), and IIoT, are mapped to Network Slices (NSs).
*   **QoS Metrics:** Throughput ($Th$), Delay ($D$), and Energy Consumption ($Ec$) are defined. These are normalized using upward/downward utility functions.
*   **Score Function ($SF$):** A dimensionless metric $\in [0,1]$ used to evaluate BS suitability. It considers:
    *   $S_{b,m}^u$: Score when resources are sufficient (based on weighted QoS).
    *   $C_{b,m}^u$: Score during overload (based on potential releaseable Resource Blocks ($P_{RB}$) and average throughput satisfaction).

### C. eDRANS Overview
The algorithm operates at each Transmission Time Interval (TTI), detecting events such as new requests or channel quality changes. The Selector Module chooses the BS with the highest $SF$. If resources are insufficient, a load-balancing process is triggered. The problem is formulated as maximizing the long-term sum of $SF$ subject to constraints on minimum/maximum throughput, delay, energy consumption, and slice accessibility.

## IV. Network Selection Process
eDRANS uses F-DDQN to find an optimal policy $\pi^*$ for BS selection. 

### MDP Formulation
*   **State Space ($S_b$):** Includes user priority, service request, historical association, slice availability, resource blocks, and current QoS metrics.
*   **Action Space ($\mathcal{A}$):** $\{0, 1, 2\}$, where $0=$ reject, $1=$ attend with sufficient resources, $2=$ attend via load balancing.
*   **Reward Function:** Rewards are granted for correct decisions (matching $SF$ values) and penalties (-1) for incorrect decisions (e.g., choosing to serve a user when the BS is overloaded).

### F-DDQN Mechanism
To prevent overestimation of Q-values, two neural networks are used: one for action selection and one for reward evaluation. The agents use an $\varepsilon$-greedy strategy for exploration and experience replay buffers for training stability. The Non-RT RIC aggregates local model parameters using FedAvg to update the Global Model.

### Complexity Analysis
The computational complexity is dominated by the DDQN training process. F-DDQN is significantly more scalable than centralized or heuristic models because the state space per agent remains constant regardless of the total number of BSs in the network.

## V. Load Balancing Process
When a BS is overloaded, CGT is used to release the minimum necessary resources ($RB_{req}$) for a new user. 

### Coalition Formation
The "players" in this weighted voting game are the resource blocks of active users. Priority-based scheduling determines the order of resource release:
1.  Low-priority users first.
2.  Users with maximum throughput before those with medium throughput.
3.  IIoT users contribute less when the request is for high-bandwidth services (VI/VR).

### Winning Coalition
A coalition $C$ is formed from a subset of players $\mathbb{P}^*$. The characteristic function $\nu(C)$ balances two factors: the number of affected users ($U_{aff}$) and the residual resources ($\xi$). The winning coalition $C_{\min}$ is the one that maximizes $\nu(C)$, thereby minimizing both the impact on existing users and resource waste.

## VI. Results and Discussion
Simulations were conducted using a heterogeneous environment (Macro-BS, Micro-BS, and UAV-BS) with up to 150 users.

### A. Training
Loss function analysis showed that the Adam optimizer with $\alpha=0.01$ and mini-batch size $64$ provided the fastest convergence. Reward averages for F-DDQN were comparable to centralized DDQN but outperformed distributed ML, which lacked inter-agent knowledge sharing.

### B. Validation
eDRANS was compared against Max-SINR, a heuristic (DASA), and centralized/distributed ML:
*   **Throughput & Data Rate:** eDRANS performed similarly to the heuristic DASA and significantly better than Max-SINR and distributed ML in terms of average throughput satisfaction ($Th_{sat}$) and Aggregated Data Rate (ADR).
*   **Energy & Delay:** eDRANS achieved lower cumulative energy consumption and lower average delay during overload situations compared to all benchmarks except the heuristic.
*   **SLA Satisfaction:** Using the SLA indicator ($I$), eDRANS maintained 100% satisfaction for a larger number of users than models with fixed resources or those without load balancing. Premium users were successfully prioritized, maintaining higher $Th_{sat}$ during saturation.

## VII. Conclusion
eDRANS effectively integrates F-DDQN and CGT within the O-RAN architecture to solve network selection and resource allocation in 3D heterogeneous networks. It matches heuristic performance while ensuring data privacy and scalability. The results demonstrate that dynamic slicing adjustment via CGT is essential for maintaining SLA satisfaction and QoS in high-density, multi-priority environments. Future work will incorporate more detailed physical variables (e.g., BS type, propagation losses) into the ML models.
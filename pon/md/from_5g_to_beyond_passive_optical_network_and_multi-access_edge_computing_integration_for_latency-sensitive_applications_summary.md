---
index_terms:
  - Passive Optical Networks
  - Multi-access Edge Computing
  - Federated Reinforcement Learning
  - H2M/R Communications
  - Dynamic Bandwidth Allocation
  - 5G-and-Beyond Networks
  - Latency-sensitive applications
---

# From 5G to beyond: Passive optical network and multi-access edge computing integration for latency-sensitive applications

## 1. Introduction
The emergence of 6G, the Tactile Internet, and Human-to-Machine/Robot (H2M/R) communications has created a demand for millisecond-range latency and high reliability to support applications like telesurgery, industrial automation, and AR/VR. Traditional centralized cloud computing is insufficient due to propagation delays caused by distance between users and data centers. Multi-access Edge Computing (MEC) addresses this by placing computational resources at the network edge. This paper argues that integrating MEC with Passive Optical Networks (PONs)—which offer high capacity and low delay—is a viable solution for the x-haul requirements of 5G-and-beyond (5GB). The authors propose a federated reinforcement learning (FedRL) framework to optimize bandwidth allocation, thereby further reducing end-to-end latency.

## 2. Background: Passive optical networks and multi access edge computing

### 2.1. PON overview
PONs utilize a point-to-multipoint (P2MP) topology consisting of an Optical Line Terminal (OLT) at the central office, a passive splitter, and multiple Optical Network Units (ONUs). This architecture is cost-effective as it shares a single feeder fiber among $N$ subscribers. Bandwidth is managed via Time Division Multiplexing (TDM) downstream and Time Division Multiple Access (TDMA) upstream. The paper notes the evolution of PON standards from GPON/EPON to 10G, NG-PON2, and 50G-capable PONs to support increasing data demands.

### 2.2. MEC overview
MEC evolved from Mobile Cloud Computing (MCC) to eliminate the need for data to traverse core networks, which causes congestion and latency. Managed by ETSI standards, MEC places servers at the radio access network (RAN) edge (e.g., base stations or cell aggregation points). Unlike MCC, MEC is designed to serve both wired and wireless networks, providing local computation, storage, and caching.

## 3. PON-MEC integration

### 3.1. Network architecture
An integrated PON-MEC network connects the OLT to a centralized cloud while simultaneously linking ONUs—which co-exist with mobile base stations—to MEC servers at the RAN edge. This configuration allows MEC servers to provide low-latency processing for both wireless mobile users and wired customers. The authors highlight that this integration enables optimal resource coordination across heterogeneous network segments.

### 3.2. Use cases

#### 3.2.1. X-hauling 5GB wireless networks
6G targets peak data rates of 100 Gb/s and latency under 1 ms. To support this, the paper discusses "functional splits" (splitting BBU functions into Centralized Units, Distributed Units, and Remote Units) to manage the massive fronthaul traffic that makes traditional CPRI impractical. PON is identified as a cost-effective x-haul solution for functional split options above 7.2 (e.g., O-RAN). However, challenges remain regarding scalability and the impact of "discovery windows" in PONs on network latency.

#### 3.2.2. e-Health
Remote healthcare, specifically wearable IoT surveillance and remote surgery, requires extreme reliability ($99.999\%$) and ultra-low latency ($<1$ ms). Integration allows high-bandwidth PON links to transport data while MEC servers perform heavy ML/DL analysis locally, avoiding the delays of a centralized cloud.

#### 3.2.3. Industry 4.0
Smart factories rely on Human–Agent–Robot Teamwork (HART) and predictive maintenance. These applications require latencies between 10–25 ms and very low packet loss rates ($\leq 10^{-9}$). MEC servers in this context provide the necessary computation for task selection between resource-constrained robots and resource-rich cloud agents.

#### 3.2.4. Augmented Reality/Virtual Reality
AR, VR, and XR used in medical training or robotic surgery require high precision, which necessitates the processing of massive amounts of video and audio data with minimal delay. The PON-MEC architecture provides the necessary bandwidth and edge-processing power to maintain immersive experiences.

## 4. Federated PON-MECs for H2M/R communications

### 4.1. Motivation
H2M/R interactions require millisecond round-trip times for haptic feedback. By utilizing ML-based traffic prediction at the MEC, haptic feedback can be expedited and the volume of data traversing the network reduced.

### 4.2. Bandwidth allocation in PON-MECs
Uplink bandwidth is managed via a REPORT-GRANT process. In conservative schemes, COs grant only what is requested, leading to packet waiting times of $\sim 1.5$ polling cycles. To optimize this, the authors introduce a "bonus" bandwidth ($\text{BW}_{\text{bonus}}$) added to the request:
$$\text{BW}_{\text{GRANT}} = \min\{\text{BW}_{\text{REQ}} + \text{BW}_{\text{BONUS}}, \text{BW}_{\text{MAX}}\}$$
The goal is to set $\text{BW}_{\text{bonus}}$ such that waiting time is reduced to $0.5$ polling cycles without causing bandwidth inefficiency via over-granting.

### 4.3. Reinforcement learning-based bandwidth allocation in federated PON-MECs
The authors propose a Federated Reinforcement Learning (FedRL) framework combining RL for decision optimization and Federated Learning (FL) for experience sharing between multiple PON-MEC systems.

#### 4.3.1. Q-learning in local PON-MEC
Each local PON-MEC uses Q-learning where the reward is defined as negative latency. The CO updates a local value function $Q_{net}$ based on the Bellman optimality equation and employs a greedy policy to select the optimal $\text{BW}_{\text{bonus}}$ from a discretized set of values.

#### 4.3.2. Experience sharing in federated PON-MECs
To avoid the time cost associated with RL exploration (sub-optimal decisions), multiple PON-MECs share their $Q$-values via a federal function $Q_{fed}$. Local COs refer to $Q_{fed}$ to accelerate convergence toward optimal bandwidth decisions. This process is asynchronous and has low computational complexity ($O(1)$ for value updates).

#### 4.3.3. Key features for federated PON-MEC
FL effectiveness depends on environment homogeneity. The authors identify key network features that determine the relationship between $\text{BW}_{\text{bonus}}$ and latency: number of ONUs, maximum link distance, data rate, traffic load, and packet arrival patterns. Only PON-MECs with similar features should form a federation to prevent performance degradation.

### 4.4. Performance evaluation

#### 4.4.1. FedRL performance
Simulations using tactile-haptic (Generalized Pareto distribution) and UDP traffic show that FedRL reduces latency by $40\%$ compared to baseline schemes for tactile traffic. Increasing the number of federated networks ($N$) significantly speeds up convergence: a federation of $N=10$ PON-MECs achieves $75\text{--}90\%$ time savings in reaching optimal latency compared to purely local RL.

#### 4.4.2. Performance under different PON-MEC features
Analysis shows that increasing the number of ONUs increases final network latency due to higher competition for bandwidth, though convergence speed remains similar. Additionally, longer link distances require a larger $\text{BW}_{\text{bonus}}$ to offset increased round-trip communication time and maintain low latency.

## 5. Summary
The paper concludes that while integrated PON-MEC architectures provide the necessary hardware foundation for 5GB and H2M/R applications, intelligent software—specifically the proposed FedRL framework—is essential to meet stringent QoS requirements. The results demonstrate significant reductions in both network latency and the time required for the system to converge on optimal resource allocation decisions. Future work will focus on refining ML techniques and developing criteria for selecting which PON-MECs should join a federation.
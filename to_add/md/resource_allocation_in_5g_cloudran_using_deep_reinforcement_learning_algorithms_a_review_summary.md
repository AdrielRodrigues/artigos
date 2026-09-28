---
index_terms:
  - 5G Cloud-RAN
  - Resource Allocation
  - Deep Reinforcement Learning
  - Network Slicing
  - Mobile Edge Computing
  - Actor-Critic Algorithms
---

# Resource allocation in 5G cloud-RAN using deep reinforcement learning algorithms: A review

## 1 Introduction
The transition to 5G requires new network architectures to handle massive increases in traffic and complexity for services like self-driving vehicles, remote medicine, and VR. Cloud Radio Access Network (C-RAN) addresses this by decoupling RAN functions from base stations and centralizing them into cloud processing units. This architecture supports network slicing and emerging services such as the Internet of Things (IoT), Vehicle-to-Everything (V2E) communications, and Mobile Edge Computing (MEC).

Resource Allocation (RA) in C-RAN focuses on optimizing the assignment of resources to meet specific Quality-of-Service (QoS) requirements while maximizing system capacity and energy efficiency. While traditional RA relies on mathematical optimization requiring precise channel state information—which often fails to scale with 5G's heterogeneity—Deep Reinforcement Learning (DRL) offers a way to learn decision-making policies directly from raw data without human intervention.

## 2 Literature Review

### 2.1 Overview of traditional methods on RA in 5G C-RAN
Traditional RA research emphasizes power distribution, user association, and virtual machine placement to enhance capacity and reduce latency.

#### 2.1.1 Simultaneous fine-tuning of radio and computational resources to achieve optimal performance
This area focuses on reducing latency by optimizing both radio frequency (RF) and computational resources. Key methods include offloading resource-intensive tasks from mobile devices to cloud servers using successive convex approximation techniques for distributed frameworks. Other research integrates MEC with blockchain technology to balance energy consumption and time-to-finality by decoupling optimization variables for user association, data rates, and computational RA.

#### 2.1.2 Virtualization-based resource management
Virtualization allows for dynamic resource pooling and sharing across virtual networks. This include the use of a Virtual Base Station (VBS) pool and Remote Radio Heads (RRH). Proposed solutions include inter-operator cooperation schemes (IOCS) based on trusted computing platforms and auction-based methods to ensure truthful resource sharing and social welfare among different operators.

#### 2.1.3 QoS-aware RA
To support delay-sensitive applications, research employs cooperative game theory with weight-based policies to ensure fairness across baseband units. Other approaches use Genetic Algorithms (GA) and Discrete Particle Swarm Optimization (DPSO) for load balancing by dynamically re-mapping RRHs to baseband unit sectors.

#### 2.1.4 Energy efficiency (EE)
Energy-efficient schemes focus on minimizing power consumption through sleep mode optimization, base station clustering, and optimized BBU-RRH mapping combined with user association.

### 2.2 Introduction to DRL algorithms and their potential for solving complex decision-making problems
DRL combines Deep Neural Networks (DNNs), which act as function approximators, with Reinforcement Learning (RL), where an agent learns via interaction with an environment to maximize a cumulative reward. The process involves observations, policies (represented by DNNs), and the use of discount factors to balance immediate and future rewards. DRL is particularly suited for wireless networks because it can adapt to non-stationary conditions (interference, mobility) and optimize tasks—like spectrum management—that are too complex for explicit programming.

### 2.3 Cutting-edge DRL algorithms implemented within 5G C-RAN scenarios

#### 2.3.1 Deep Q-network (DQN)
DQN uses NNs to approximate the Q-function, estimating long-term rewards for state-action pairs. It utilizes experience replay and Temporal Difference (TD) learning based on the Bellman equation. Applications include autonomous cellular function activation in Heterogeneous C-RAN (H-CRAN), optimizing IRS-enhanced OFDM systems, and resource orchestration for IIoT devices. The computational complexity is approximately $O(n \cdot m \cdot t)$, where $n$ is the number of parameters, $m$ is iterations, and $t$ is time per iteration.

#### 2.3.2 Policy gradient
Unlike value-based methods, policy gradients directly optimize the mapping from states to actions. They are more effective for continuous action spaces. In 5G RA, they manage intricate environments by optimizing long-term benefits based on past experience. Computational complexity is $O(N \cdot T \cdot d)$.

#### 2.3.3 Actor-critic
This hybrid approach uses an "actor" to select actions and a "critic" to evaluate those actions. It is effective for continuous action spaces, such as optimizing computation offloading in MEC systems and managing user scheduling in HetNets with hybrid energy sources. Complexity is generally $O(k \cdot n)$.

#### 2.3.4 Asynchronous advantage Actor-critic (A3C)
A3C employs multiple independent agents learning in parallel asynchronously, utilizing an "advantage function" to measure action effectiveness against the average. It has been applied to energy-efficient RAN slicing (using SBiLSTM networks) and improving Quality of Experience (QoE) for video streaming over SDMN integrated with MEC.

#### 2.3.5 Proximal policy optimization (PPO)
PPO restricts the size of policy updates to prevent drastic deviations from previous policies, ensuring stability. It has been used for multi-objective RA across various service types, coordinating swarm robotics in automated warehouses via Coordinated Multipoint clustering, and UAV-based QoS management during disasters. Complexity is $O(n)$.

#### 2.3.6 Deep deterministic policy gradient (DDPG)
Designed for continuous control, DDPG uses a deterministic actor. Applications include dynamic computation offloading in Fog Access Points (F-APs) using federated learning to protect privacy and the "DeepRAT" framework for joint RAT assignment and power allocation in HetNets. Complexity is $O(n^2)$.

#### 2.3.7 Twin delayed deep deterministic policy gradient (TD3)
TD3 improves DDPG by employing two critics to reduce Q-value overestimation and adding noise to the target policy to encourage exploration. It has outperformed model-based methods in IoRT power allocation, LEO satellite MsgA channel allocation, and massive MTC service scheduling (via the MPMA-TD3 algorithm). Complexity is $O(n^2)$.

#### 2.3.8 Soft Actor-critic (SAC)
SAC maximizes both expected reward and policy entropy to promote exploration. It has been applied to cooperative computation offloading in edge-cloud/edge-edge servers, dynamic resource scheduling in BAC-NOMA IoT networks, and managing mixed discrete-continuous action spaces for energy harvesting.

### 2.3.9 Implementation Considerations
Implementing DRL in C-RAN requires a systematic pipeline: defining the problem $\rightarrow$ designing state, action, and reward spaces $\rightarrow$ selecting an algorithm $\rightarrow$ implementing a simulation environment $\rightarrow$ training and fine-tuning (hyperparameters) $\rightarrow$ evaluation and deployment. Key considerations include managing network dynamics via online learning and ensuring scalability for real-time decision-making in large networks.

## 3 Challenges and Solutions

### 3.1 Scalability issues in applying DRL to C-RAN RA
Scaling DRL is hindered by the high volume of training data required, increasing problem complexity as networks grow, and the difficulty of designing reward functions for conflicting objectives. Proposed solutions include transfer learning (using pre-trained models), regularization to prevent overfitting, and hierarchical learning to decompose complex problems into smaller sub-problems.

### 3.2 Convergence challenges of DRL algorithms in C-RAN
Convergence is complicated by high-dimensional state representations and the vast number of hyperparameters. Furthermore, the non-stationarity of wireless environments (user mobility, fading) makes it difficult for policies to stabilize. Potential solutions include ensemble learning and the integration of domain knowledge into models.

### 3.3 Ensuring fairness in RA with DRL algorithms
DRL can produce unfair outcomes if training data is biased or if the "black box" nature of NNs obscures decision-making logic. Solutions include incorporating explicit fairness constraints into objective functions, preprocessing training data to reduce bias, and utilizing Explainable AI (XAI).

### 3.4 Security and privacy
The requirement for large datasets exposes sensitive user information and network patterns. Proposed mitigations include:
- **Privacy-preserving algorithms**: Federated learning, differential privacy, and secure multi-party computation.
- **Data anonymization**: Obfuscating personally identifiable information.
- **Secure protocols**: Encryption and authentication in C-RAN infrastructure.
- **Regulatory frameworks**: Policies governing data ownership and consent.

## 4 Future Research Directions

### 4.1 Open areas for future investigation in the application of DRL to C-RAN RA
Future research should focus on:
- More realistic modeling of network dynamics (interplay between BS, CPUs, and fronthaul).
- Advanced reward design considering trade-offs between spectral efficiency and energy.
- Novel exploration-exploitation strategies.
- Feasibility studies for real-time implementation in actual C-RAN hardware.
- Leveraging transfer learning to accelerate training across different network scenarios.

### 4.2 Potential impact of DRL on the development of 5G networks
Key promising areas include Multi-Agent Reinforcement Learning (MARL) for collaborative optimization and applying DRL to heterogeneous networks with varying device capabilities. Overall, DRL can enable autonomous networks that dynamically adjust to conditions, increasing capacity, reducing costs, and optimizing energy consumption without human intervention.

## 5 Conclusion
C-RAN is essential for meeting the diverse demands of 5G, but traditional RA schemes lack scalability. DRL provides a powerful alternative by learning complex policies from data. While challenges in scalability, convergence, fairness, and security remain, state-of-the-art algorithms like DQN, PPO, and SAC demonstrate significant potential to optimize resource allocation and drive the development of autonomous 5G networks.
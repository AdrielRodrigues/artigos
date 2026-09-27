---
index_terms:
  - service migration
  - resource allocation
  - multiaccess edge computing
  - deep reinforcement learning
  - parameterized deep Q-network
  - long short term memory
  - Internet of Things
  - task processing latency
---

# Joint Service Migration and Resource Allocation in Edge IoT System Based on Deep Reinforcement Learning

## Abstract
This paper addresses the challenge of maintaining Quality of Service (QoS) for mobile IoT users in multiaccess edge computing (MEC) environments. Specifically, it tackles the joint optimization of service migration and resource allocation (SMRA) to minimize access delay. The authors propose a DRL-based algorithm combining Long Short-Term Memory (LSTM) for mobility prediction and Parameterized Deep Q-Networks (PDQN) to handle a hybrid discrete-continuous action space. Evaluation using real-world Beijing cab trajectory data demonstrates that this joint approach outperforms baseline methods in reducing task processing latency.

## I. Introduction
MEC reduces access delay by placing services at edge servers (ESs) near IoT users. However, high user mobility and limited ES resources create a conflict: staying connected to a distant source ES increases communication delay, while migrating the service to a closer target ES introduces migration latency. Because resource allocation at the target ES determines the benefit of migrating, SMRA must be optimized jointly.

The authors identify gaps in existing research, noting that most studies treat migration and allocation as separate problems or ignore user mobility patterns. The core contributions are:
1. A joint optimization model for dynamic SMRA considering ES heterogeneity and diverse user requirements.
2. An MDP-based DRL framework utilizing LSTM for mobility prediction and PDQN to manage the hybrid action space of discrete (migration decision) and continuous (resource allocation) variables.
3. Empirical validation using real-world trajectory data showing reduced average task processing latency.

## II. Related Work
### A. Service Migration
Previous works have used Lyapunov optimization or specific placement schemes, but often assume uniform resource allocation across users or ignore the impact of target ES resource policies on the migration decision. Some DRL approaches (e.g., DDPG) are used for task allocation, but they may not account for predictive mobility to ensure seamless handovers. Existing network slice migration research focuses primarily on bandwidth rather than an integrated approach combining computing and communication resources.

### B. Resource Allocation
Existing resource management often relies on static scenarios or simplifies ES computing power as the number of users served rather than CPU cycles. While DRL has been used for computational offloading, many methods use rounding techniques to convert continuous outputs into discrete decisions, which can degrade performance. The authors argue that a PDQN is superior for hybrid action spaces compared to standard DQN or DDPG.

## III. System Model and Problem Formulation
### A. System Model
The system consists of mobile users ($\mathcal{U}$), base stations with integrated ESs ($\mathcal{E}$), and a cloud server acting as the controller. Each user has latency-sensitive tasks defined by data size ($D_{u,e}$) and CPU cycles required per bit ($C_{u,e}$).

1. **Nonmigration Model**: Total delay consists of communication delay (based on Shannon's formula for transmission rate) and computation delay at the source ES.
2. **Migration Model**: Total delay includes:
    - **Migration Delay**: The sum of service instance (SI) suspending time, state context data synchronization time (between ESs), and SI resuming time.
    - **Communication Delay**: Transmission from user to target ES.
    - **Computation Delay**: Processing at the target ES.

### B. Problem Formulation
The objective is a total latency minimization problem ($\mathcal{P}$) over an infinite horizon, minimizing the average sum of processing delays for all users across all time slots. This optimization is subject to:
- CPU capacity constraints at each ES.
- Bandwidth constraints at each ES.
- Binary migration decisions (migrate vs. non-migrate).
- The requirement that each user is served by exactly one ES.

Due to binary variables and dynamic environmental changes, the problem is nonconvex and complex, necessitating a DRL approach.

## IV. DRL-Based SMRA Approach
### A. DRL-Based Framework
The problem is formulated as a Markov Decision Process (MDP):
- **State ($s_t$)**: Includes predicted user location (via LSTM), location of the nearest target ES, resources currently allocated by the source ES, and available resources at the target ES.
- **Action ($a_t$)**: A hybrid set containing discrete migration decisions (migrate or not) and continuous resource allocation values (CPU and bandwidth) for the target ES.
- **Reward ($r_t$)**: Defined as the negative expected sum of total task processing delays for all users.

The authors argue that standard DQN cannot handle continuous actions, and DDPG struggles with discrete ones. PDQN is selected to bridge this gap.

### B. SMRA Algorithm Based on LSTM and PDQN
The framework integrates two components:
1. **LSTM**: Predicts future user locations based on historical trajectory data, which then determines the target ES. This reduces the action space by avoiding a global search of all ESs.
2. **PDQN**: Uses a Q-network to approximate value functions and an "x-network" (deterministic policy network) to map states to continuous action parameters for each discrete action. 

**Algorithm Process:**
The system observes the state, predicts location via LSTM, and uses an $\epsilon$-greedy strategy to select actions from the PDQN. Experience tuples are stored in a replay buffer and used to update the Q-network (via least mean squares loss) and the x-network (to maximize the Q-value).

**Complexity:**
The total time complexity is $\mathcal{O}(z \cdot w_{\text{full}} + z \cdot w_{\text{lstm}})$, where $z$ is iterations, $w_{\text{full}}$ relates to DNN layer dimensions, and $w_{\text{lstm}}$ depends on sequence length and hidden units.

## V. Simulation Results and Discussion
### A. Experimental Settings
Simulations used the Microsoft Research Asia Beijing cab trajectory dataset (10,357 cabs). The setup included 70 mobile users and 60 ESs spaced 5km apart. Baselines for comparison included DDPG-based (with rounding), DQN-based (with discretization), Random Migrate (RMS), Always Migrate (AMS), and Never Migrate (NMS) schemes.

### B. Parameter Analysis
- **Resource Ranges**: As the upper limits of requested CPU and bandwidth increase, the migration ratio decreases because target ESs become unable to satisfy the high resource demands of users. This subsequently increases average task processing latency.
- **Discount Factors ($\gamma$)**: Experiments with $\gamma \in \{0.1, 0.2, 0.5, 0.9\}$ showed that while all converged, different factors influenced the speed and quality of convergence.

### C. Comparison Experiments
- **User Scaling**: As the number of users increases, latency rises for all schemes; however, the proposed PDQN approach grows more slowly than baselines. It outperforms AMS (by avoiding unnecessary migrations) and NMS (by reducing long-distance communication).
- **ES Scaling**: Increasing the number of ESs reduces average latency as total available resources increase. The SMRA scheme remains consistently optimal across varying ES densities.
- **Convergence**: Comparative analysis showed that while DDPG and DQN converge, the proposed PDQN converges to a lower minimum average delay.

## VI. Conclusion
The paper successfully optimizes joint service migration and resource allocation in MEC systems to minimize user access delay. By combining LSTM for mobility prediction and PDQN for hybrid action space management, the authors created a system that ensures service continuity and efficient resource utilization despite high user mobility and ES constraints. Simulation results using real-world data confirm its superiority over traditional DRL methods and static migration policies.
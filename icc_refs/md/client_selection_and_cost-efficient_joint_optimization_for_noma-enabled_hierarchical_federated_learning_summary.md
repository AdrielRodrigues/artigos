---
index_terms:
  - hierarchical federated learning
  - non-orthogonal multiple access
  - fuzzy logic client selection
  - penalty dual decomposition
  - deep deterministic policy gradient
  - resource allocation
---

# Client Selection and Cost-Efficient Joint Optimization for NOMA-Enabled Hierarchical Federated Learning

## I. Introduction
Hierarchical Federated Learning (HFL) improves upon traditional two-layer FL by using a client-edge-cloud architecture, which reduces communication latency and energy overhead while maintaining data privacy. Despite these benefits, the increasing number of clients creates bottlenecks in communication and energy consumption. This paper proposes a NOMA-enabled HFL system under semi-synchronous cloud aggregation to minimize total time and energy costs per global round.

### A. Related Literature
Two-layer FL research has focused on model compression, client scheduling, and resource allocation to handle bottlenecks. Existing HFL research explores edge aggregation intervals, convergence bounds, and basic association schemes. However, most current HFL associations rely on a single criterion (e.g., distance), failing to balance multiple aspects of client heterogeneity. Additionally, there is a lack of joint optimization for client selection, edge scheduling, and resource allocation in NOMA-enabled HFL.

### B. Motivations and Contributions
Practical wireless networks require multi-criteria association policies that consider data volume, model staleness, and channel quality. This paper contributes:
1. A NOMA-enabled HFL system using semi-synchronous cloud aggregation to reduce communication and energy overhead.
2. A fuzzy logic-based client-edge association policy that accounts for wireless channel quality, data quantity, and model staleness.
3. A joint optimization framework for edge server scheduling and resource allocation, formulated as a non-convex mixed-integer non-linear programming (MINLP) problem. This is solved using Penalty Dual Decomposition (PDD) for scheduling and Deep Deterministic Policy Gradient (DDPG) for continuous resource allocation in time-varying environments.

### C. Organization
The paper is structured to present the system model (II), the fuzzy association scheme (III), optimization algorithms for scheduling and resources (IV), simulation results (V), and a conclusion (VI).

## II. System Model
The system consists of a remote cloud server, $M$ edge servers, and $N$ total clients ($N \gg M$). All nodes use single antennas. The HFL process is split into two phases: the client-edge phase and the edge-cloud phase.

### A. Client-Edge Phase
1. **Local Model Training**: Clients update local models via gradient descent. The number of iterations $\tau_1$ depends on a local accuracy threshold $\theta$. Training time $t_n^{cmp}$ and energy consumption $e_n^{cmp}$ are functions of CPU frequency $f_n$, data samples $D_n$, and computational cycles $c_n$.
2. **Client-Edge Transmission**: NOMA allows multiple clients to transmit simultaneously on the same channel. Successive Interference Cancellation (SIC) is used at the edge server, with decoding order based on received power ($p_n |h_{n,m}|^2$). The data rate $R_{n,m}$ depends on the Signal-to-Interference-to-Noise Ratio (SINR). Transmission time $t_{n,m}^{com}$ and energy $e_{n,m}^{com}$ are derived from these rates.
3. **Edge Model Aggregation**: Edge servers aggregate models using weighted averaging. The process repeats for $\tau_2$ iterations until edge accuracy $\xi$ is reached. Total phase time $T_{\mathcal{N}_m}^{edge}$ is determined by the slowest client (synchronous aggregation), and total energy $E_{\mathcal{N}_m}^{edge}$ is the sum across selected clients.

### B. Edge-Cloud Phase
1. **Edge-Cloud Transmission**: Edge servers use OFDMA to upload aggregated models to the cloud. This phase defines transmission time $T_m^{cloud}$ and energy $E_m^{cloud}$.
2. **Cloud Model Aggregation**: A semi-synchronous mechanism is employed where the cloud server selects a subset of $M_c$ edge servers based on their total time consumption. This prevents the "straggler problem" associated with absolute synchrony while avoiding the overfitting and overhead risks of absolute asynchrony. System-wide total time $T$ is the maximum among scheduled servers, and energy $E$ is the sum across all scheduled servers.

## III. Fuzzy Logic Based Client-Edge Association
To handle client heterogeneity, a multi-criteria association policy is designed using fuzzy logic.

### A. Fuzzy Input
Three normalized inputs (0-100%) are used:
1. **Channel Quality (CQ)**: Reflects the actual communication environment rather than just distance.
2. **Data Quantity (DQ)**: Prioritizes clients with more data to improve global model training.
3. **Model Staleness (MS)**: Tracks the time since a client was last selected; higher staleness increases selection probability to ensure timely updates and faster convergence.

### B. Fuzzy Output
Inputs are mapped through fuzzifiers into sets (e.g., CQ $\in$ {weak, medium, strong}). A set of 27 fuzzy rules (Table I) maps these inputs to an output competency level (poor to excellent). The Max-Min method combines multiple rules, and the Center of Gravity (COG) method defuzzifies the result into a numerical value $NO^*$. Edge servers select clients with the highest $NO^*$ values; if a client is selected by multiple servers, it associates with the nearest one.

## IV. Joint Edge Server Scheduling and Optimal Resource Allocation

### A. Problem Formulation
The goal is to minimize the weighted sum of total time and energy cost: $\min \lambda_t T + \lambda_e E$. This is subject to transmit power limits ($p_n$), CPU frequency limits ($f_n$), and binary scheduling indicators ($z_m$). The resulting non-convex MINLP is decomposed into two subproblems.

### B. Edge Server Scheduling
With fixed resources, the problem focuses on scheduling $z_m$. An auxiliary variable $\tilde{z}_m$ is used to handle binary constraints. A double-loop PDD algorithm solves an augmented Lagrangian (AL) problem:
1. **$\tilde{z}_m$ Solution**: Derived via first-order optimality conditions.
2. **$z_m$ Solution**: Solved as a convex problem using the Lagrange dual method, resulting in a closed-form solution based on Lemma 1.
3. **U and W Solutions**: Optimal values for maximum edge time ($U^*$) and overall system time ($W^*$) are calculated.
4. **Updates**: Dual variables $q_m$ and $\tilde{q}_m$ are updated in the outer loop to ensure convergence to stationary solutions.

### C. Resource Allocation
With scheduled servers, the problem optimizes transmit power $\mathbf{p}$ and frequency $\mathbf{f}$. Due to the continuous action space and dynamic channel environment, a Deep Deterministic Policy Gradient (DDPG) algorithm is used:
- **MDP Formulation**: State $S$ includes channel gains and data sizes; Action $A$ consists of power and computation resources; Reward $R$ is the negative total cost.
- **Architecture**: An actor-critic framework with experience replay and target networks is used to ensure stability and avoid overestimation. The online critic network minimizes MSE loss, while the actor network is optimized via policy gradients.

## V. Simulations and Analysis
Simulations use 64 clients and 4 edge servers in a 500m area, testing on MNIST and CIFAR-10 datasets under IID and non-IID distributions.

### A. Fuzzy Logic Based Client-Edge Association
Results show that the proposed scheme selects clients based on comprehensive ability (data size and staleness) rather than proximity alone, effectively balancing heterogeneity.

### B. Performance of HFL
The Fuzzy Client Edge Association (FCEA) consistently achieves higher learning accuracy and lower global loss compared to random (RCEA), greedy (GCEA), and OMA benchmarks. The advantage is most pronounced in non-IID settings, demonstrating that NOMA's ability to include more clients is critical for convergence with heterogeneous data.

### C. Performance of Average MS
FCEA maintains the lowest average model staleness over time compared to other schemes, which accelerates convergence by ensuring local models remain fresh and diverse.

### D. DDPG-Based Resource Allocation
The DDPG-RA algorithm outperforms random (RRA), fixed power (FPA), fixed computation (FCA), and DQN-based resource allocation. The improvement over DQN is attributed to DDPG's continuous action space exploration. Total cost increases with the number of associated clients $N_m$ (due to energy and stragglers) and model size $d_n$, though DDPG-RA shows higher resilience to large model sizes than benchmarks.

## VI. Conclusion
The paper introduces a NOMA-enabled HFL system that minimizes cost through three integrated components: a fuzzy logic policy for multi-criteria client selection, a PDD algorithm for closed-form edge scheduling, and a DDPG algorithm for dynamic resource allocation. Simulations confirm the approach improves training accuracy and reduces overall time and energy costs.
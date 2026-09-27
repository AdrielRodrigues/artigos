---
index_terms:
  - Virtual Optical Network Embedding
  - Elastic Optical Networks
  - Deep Reinforcement Learning
  - Proximal Policy Optimization
  - Invalid Action Masking
  - Blocking Probability
---

# Deep Reinforcement Learning for Infrastructure as a Service over Flexible Optical Networks

## Introduction
Infrastructure as a Service (IaaS) allows customers to lease virtualized computing, storage, and networking resources. When customers request an entire network topology with specific node and link capacities (a virtual network request), the provider must perform Virtual Optical Network Embedding (VONE). This involves allocating compute/storage at nodes and spectrum on links within an Elastic Optical Network (EON). EONs use fine-grained Frequency Slot Units (FSUs) to increase spectral efficiency, but these FSUs must be allocated in continuous and contiguous blocks. The primary goal for IaaS providers is to implement VONE strategies that minimize the blocking probability of these requests.

## Previous Work
Current state-of-the-art solutions for VONE rely on hand-crafted heuristics or distributed protocols. While exact methods like integer linear programming provide optimal results, they are computationally impractical for large networks or dynamic environments. Recent research has explored Deep Reinforcement Learning (DRL) to navigate the combinatorial solution space. Previous DRL attempts often employed multi-agent systems—assigning separate agents to nodes and links—because the action space was considered too large for a single agent. However, these multi-agent approaches are more complex and can result in sub-optimal solutions due to coordination difficulties between agents.

## Contribution
This paper benchmarks VONE heuristics against a single DRL agent to demonstrate that a unified agent produces higher-quality solutions than sequential multi-agent systems. The authors extend previous work by increasing the action space for greater realism and provide an interpretability analysis to compare how the DRL agent utilizes spectrum resources versus heuristic methods.

## Network and Traffic Model
The substrate network is modeled as an undirected graph of $N^s$ nodes and $L^s$ bidirectional links, each with defined capacities and FSUs. Virtual networks are represented as undirected graphs ($N^v$ nodes, $L^v$ links) with specific bandwidth (FSU) and capacity requirements. Traffic is dynamic: requests arrive following a Poisson process and depart according to an exponential distribution based on mean holding time.

## Deep Reinforcement Learning Algorithm
The system consists of an environment (the EON substrate and request generator) and an agent. 

### Observation, Action, and Reward
- **Observation Space:** Includes the current virtual network request, the FSU status of all links, and remaining node resource capacities.
- **Action Space:** Divided into a node section ($1 \times N^{Nv s}$) and a path section ($L^v \times k * N^f$), where $N^f$ is the number of FSUs per link.
- **Reward Function:** A simple signal where successful allocation earns 0 and failure earns -10, avoiding excessive guidance to allow the agent to discover its own policy.

### Implementation Details
The agent utilizes Proximal Policy Optimization (PPO). To handle the constraints of the EON, the authors implement **multi-step invalid action masking**, which recursively prevents the agent from selecting unavailable resources or links already allocated within the same virtual network request.

### Training and Experimental Setup
Training was conducted on the NSFNET topology (14 nodes, 21 links) with 100 FSUs per link and 30 compute units per node. Virtual networks were restricted to 3-node ring topologies for benchmarking consistency. Link requests required {2, 3, 4} FSUs, and nodes required {1, 2} compute units. The agent was trained over 100 episodes of $10^4$ timesteps each at a traffic load of 60 Erlangs, using a discount factor $\gamma = 0.8$ and GAE $\lambda$-factor $= 0.9$.

## Results
The DRL agent was benchmarked against nine combinations of three node-mapping heuristics (CaLRC, NSC, TMR) and three path-mapping heuristics (kSP-FF, kSP-FDL, MSP-EF), as well as a "Random Masked" baseline.

### Heuristic Performance
Among the heuristics, the kSP-FF path mapping performed best across all node mappings. The combination of Consecutiveness-Aware Local Resource Capacity (CaLRC) and kSP-FF (CaLRC+kSP-FF) emerged as the strongest overall heuristic.

### Agent vs. Heuristic Comparison
The DRL agent significantly outperformed CaLRC+kSP-FF. At a traffic load of 40 Erlangs, the agent's mean blocking probability was an order of magnitude lower than the best heuristic; at 100 Erlangs, it remained 15% lower.

### Interpretability Analysis
Utilisation heatmaps reveal that heuristics tend to favor specific links and always utilize the first available FSUs, leading to spectrum fragmentation and congestion on certain paths. In contrast, the DRL agent distributes resource utilization more balancedly across both links and FSUs, which accounts for its superior blocking probability.

## Conclusions
The study identifies CaLRC+KSP-FF as the best-performing traditional heuristic for VONE but demonstrates that a single DRL agent with multi-step action masking provides far superior performance. The analysis suggests that the agent's ability to maintain balanced link and spectrum utilization is the primary driver of its efficiency.
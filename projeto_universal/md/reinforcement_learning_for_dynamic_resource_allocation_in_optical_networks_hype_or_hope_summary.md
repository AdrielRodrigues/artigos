---
index_terms:
  - dynamic resource allocation
  - reinforcement learning
  - optical networks
  - service blocking probability
  - heuristic benchmarking
  - routing and spectrum assignment
  - network defragmentation
  - reproducibility
---

# Reinforcement learning for dynamic resource allocation in optical networks: hype or hope?

## 1. Introduction
The growing demand for data traffic necessitates increasing network capacity without proportional increases in capital expenditure. Dynamic Resource Allocation (DRA) is proposed to maximize throughput by automating service provisioning and reducing the operational margins typically required for transmission uncertainty. While Reinforcement Learning (RL) has emerged as a promising tool for DRA—offering near-optimal results with the speed of heuristics—its adoption is hindered by a lack of standardized benchmarking, poor reproducibility, and limited generalizability of results.

This paper addresses these gaps by reviewing RL progress in DRA, identifying deficiencies in existing benchmarks, and recreating the problem settings of five influential papers to evaluate them against optimized heuristic baselines. The authors also introduce a "resource-prioritized defragmentation" method to estimate empirical lower bounds on blocking probability, determining whether a significant optimality gap remains for future RL research to fill.

## 2. Background

### A. DRA Problems in Optical Networks
**Motivation**: Dynamic operation allows networks to respond to shifting traffic in real-time, reducing the resource margins needed to accommodate uncertainty and thereby increasing overall throughput. RL is particularly suited here because DRA involves large combinatorial search spaces and objective functions that can be optimized via simulation.

**Traffic Models**: The authors focus on *dynamic traffic*, where requests arrive and expire according to probability distributions (typically exponential), unlike static or incremental models.

**Problem Variants**: The paper focuses on Routing and Wavelength Assignment (RWA) for fixed-grid networks, Routing and Spectrum Assignment (RSA) for flex-grid networks, and Routing, Modulation, and Spectrum Assignment (RMSA) which adds modulation format selection as a variable.

**Constraints**: Allocation is governed by three main constraints:
1. **Spectrum continuity**: The same frequency slots must be used across all links in a lightpath.
2. **Spectrum contiguity**: Allocated slots must be adjacent.
3. **No reconfiguration**: Once established, active lightpaths cannot be moved without disruption.

**Solution Methods**: While Integer Linear Programming (ILP) provides exact solutions for static traffic, it is computationally infeasible for dynamic traffic. Heuristics are fast and deterministic but potentially sub-optimal; ML/RL methods attempt to bridge this gap by learning optimized policies.

### B. Reinforcement Learning
RL optimizes sequential decision-making via agents that maximize a reward signal within an environment (Markov Decision Process). The authors distinguish between:
*   **Action-value methods (e.g., Q-learning)**: Estimate the value of actions in specific states; used primarily for route selection.
*   **Policy gradient methods (e.g., A2C, PPO)**: Directly optimize policy parameters to maximize expected rewards and can handle continuous action spaces. Actor-critic architectures are commonly used to reduce variance using a learned value function (the critic).

## 3. Literature Survey

### A. Survey Methodology
A manual review of 97 peer-reviewed papers was conducted, categorizing research into RWA, RSA, RMSA, and "Other" (e.g., traffic grooming, survivability, and multicast provisioning).

### B. Review of Benchmarking Practices
The authors find that benchmarking is often inconsistent. DeepRMSA established a *de facto* standard for problem definitions, but many subsequent papers compare their RL solutions to weak versions of heuristics like K-Shortest Paths First-Fit (KSP-FF). Furthermore, the simulation environment is fragmented across various incompatible toolkits, making fair comparisons difficult.

### C. Recommendations for Benchmarking Best Practice
To improve rigor, the authors recommend:
*   Selecting and tuning the best possible benchmarks (optimizing candidate path counts and sort criteria).
*   Using deterministic algorithms to ensure reproducibility.
*   Ensuring statistical significance through a minimum of 100 blocking events per trial across multiple random seeds.
*   Providing open-source code and utilizing established simulation frameworks.

### D. Selection of Papers for Benchmarking
Five influential papers were selected based on their impact, citation count, and use of the DeepRMSA framework:
1. **DeepRMSA**: Uses an NN to select from K-shortest paths with first-fit spectrum allocation.
2. **Reward-RMSA**: Improves DeepRMSA by incorporating fragmentation data into the reward function.
3. **GCN-RMSA**: Employs Graph Convolutional Networks (GCN) and RNNs for better feature extraction of network states.
4. **MaskRSA**: Uses invalid action masking to select from all available slots on K paths.
5. **PtrNet-RSA**: Utilizes pointer-nets to select nodes for the path, removing the restriction of pre-calculated K-shortest paths.

## 4. Heuristic Algorithm Benchmark Evaluation

### A. Effect of Path Ordering
The authors identify that sorting candidate paths by the **number of hops** (MNH) rather than physical distance in kilometers (#km) significantly reduces service blocking probability (SBP). This is because a path with fewer hops consumes fewer total spectral resources across the network, even if the physical length is slightly longer.

### B. Simulation Setup
Using the XLRON framework, three experiments were conducted across four topologies (NSFNET, COST239, USNET, JPN48) to optimize the number of candidate paths ($K$) and evaluate different heuristics (including KSP-FF, FF-KSP, KSP-BF, BF-KSP, KME-FF, and KCA-FF).

### C. Results and Discussion
*   **Topology Influence**: In smaller networks (NSFNET, COST239), KSP-FF and KME-FF perform best. In larger networks (USNET, JPN48), FF-KSP is significantly superior.
*   **Effect of $K$**: SBP decreases as $K$ increases, generally stabilizing around $K=50$. 
*   **Conclusion**: The strongest heuristic benchmarks are KSP-FF or FF-KSP with $K=50$, utilizing #hops ordering.

## 5. Benchmarking of Previous Work

### A. Holding Time Truncation
The authors discover a critical implementation detail in the DeepRMSA codebase: service holding times are resampled if they exceed twice the mean. This "holding time truncation" reduces the actual traffic load by approximately 31%. Because several landmark papers used this codebase without documenting the truncation, their reported results were achieved under significantly lighter loads than claimed.

### B. Benchmarking of Published Results
The authors recreated the problem settings of the five selected papers and compared published RL results against both a basic KSP-FF ($K=5$) and an optimized heuristic (KSP-FF/FF-KSP with $K=50$ and #hops ordering).

**Findings**: Simple heuristics outperform or match published RL solutions in nearly all cases. Specifically, simply changing the path sort criteria to #hops often beats RL results; increasing $K$ to 50 further improves heuristic performance by over an order of magnitude compared to most RL implementations. This suggests that previous claims of RL superiority were based on weak benchmarks.

## 6. Network Blocking Bounds

### Resource-Prioritized Defragmentation
To determine if there is still room for improvement, the authors propose a method to estimate empirical lower bounds on blocking. They relax the "No Reconfiguration" constraint by allowing **defragmentation**. The algorithm sorts active requests in descending order of required resources (spectral slots $\times$ hops) and re-allocates them sequentially using a strong heuristic. This creates an "omniscient" baseline that represents a physical lower bound on blocking probability.

### Results and Discussion
The gap between the best heuristics and these empirical bounds indicates that traffic load could be increased by **19% to 36%** in flex-grid networks for a fixed SBP (0.1%). This reveals that while current RL solutions fail to beat basic heuristics, a substantial optimality gap still exists, providing a legitimate target for future research.

## 7. Conclusion
The study concludes that the perceived success of RL in optical DRA has been overestimated due to deficient benchmarking and lack of reproducibility (e.g., holding time truncation). However, the introduction of empirical bounds via resource-prioritized defragmentation proves that current heuristics are not yet optimal. The authors suggest that future RL research should focus on bridging this 19%–36% capacity gap or targeting multi-objective optimizations where simple heuristics are less effective.
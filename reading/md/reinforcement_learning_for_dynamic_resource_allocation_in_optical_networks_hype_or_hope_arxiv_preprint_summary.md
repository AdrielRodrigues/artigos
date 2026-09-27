---
index_terms:
  - reinforcement learning
  - dynamic resource allocation
  - optical networks
  - service blocking probability
  - heuristic benchmarking
  - resource-prioritized defragmentation
  - routing and spectrum assignment
---

# Reinforcement Learning for Dynamic Resource Allocation in Optical Networks: Hype or Hope?

## 1. Introduction
The authors address the challenge of increasing optical network capacity without excessive capital expenditure by optimizing dynamic resource allocation (DRA). While reinforcement learning (RL) is presented as a promising tool to approach the efficiency of exact methods (like ILP) with the speed of heuristics, its adoption is hindered by poor benchmarking and lack of reproducibility. This paper aims to establish higher evaluation standards by recreating five landmark RL studies and comparing them against optimized heuristic benchmarks. The authors introduce the "XLRON" simulation framework to promote transparency and provide an empirical lower bound on blocking probability to determine if there is still a theoretical gap for future RL research to fill.

## 2. Background

### A. DRA problems in optical networks
**Motivation and RL Application:** Optical networks require resource margins to handle transmission uncertainty; reducing these margins increases throughput. RL is suitable for DRA due to the large combinatorial search space, clear optimization objectives (e.g., minimizing blocking), and availability of efficient simulators.

**Traffic Models:** Traffic is categorized as static (all requests known), incremental (requests don't expire), or dynamic (on-demand requests with random expiry). This paper focuses on dynamic traffic.

**Problem Variants:** Core problems include Routing and Wavelength Assignment (RWA) for fixed-grids and Routing and Spectrum Assignment (RSA) for flex-grids. Extensions include modulation format selection (RMSA) and core/band selection (RCMSA/RBMSA).

**Constraints:** Three primary constraints govern allocation:
1. **Spectrum Continuity:** The same frequency slot unit (FSU) must be used on all links of a path.
2. **Spectrum Contiguity:** Allocated FSUs for a single request must be adjacent.
3. **No Reconfiguration:** Once established, lightpaths cannot be moved until they expire.

**Solution Methods:** While ILP provides exact solutions for static traffic, it is computationally infeasible for dynamic traffic. Heuristics offer speed and interpretability, while RL policies can provide near-optimal decisions in sub-second time once trained.

### B. Reinforcement learning
The paper defines the RL framework as an agent interacting with an environment to maximize rewards based on a policy (mapping states to actions). It distinguishes between model-based RL (planning) and model-free RL. The latter is split into:
* **Action-value methods:** (e.g., Q-learning) estimating the value of specific actions in states.
* **Policy gradient methods:** (e.g., A2C, PPO) directly optimizing policy parameters; often using Actor-Critic architectures to reduce variance via a learned value function (critic).

## 3. Literature Survey

### A. Survey methodology
The authors reviewed 97 peer-reviewed papers on RL for DRA in optical networks, categorizing them into RWA, RSA, RMSA, and "Other" (e.g., defragmentation, survivability, multicast provisioning).

### B. Review of benchmarking practices
DeepRMSA established a de facto standard for problem definitions and benchmarks. However, the authors note that many subsequent RL papers report 20–30% improvements over heuristics, but these comparisons often rely on weak heuristic implementations. Furthermore, the simulation software landscape is fragmented across several competing toolkits (e.g., Optical-rl-gym, RSA-RL).

### C. Recommendations for benchmarking best practice
The authors propose three pillars for rigorous evaluation:
1. **Benchmark Selection:** Tune heuristic parameters (like candidate path counts) and prefer deterministic algorithms over other ML models to ensure reproducibility.
2. **Statistical Rigor:** Use multiple random seeds and a minimum of 100 blocking events per trial, reporting mean and standard deviation.
3. **Methodological Transparency:** Release code and use established frameworks with unit tests.

### D. Selection of papers for benchmarking
Five influential papers were chosen for re-benchmarking based on their impact and consistent use of the DeepRMSA problem settings:
1. **DeepRMSA:** Uses a NN to select from K-shortest paths with first-fit allocation.
2. **Reward-RMSA:** Modifies the reward function to account for spectral fragmentation.
3. **GCN-RMSA:** Employs Graph Convolutional Networks and RNNs for better state feature extraction.
4. **MaskRSA:** Uses invalid action masking and allows selection from all available slots on K paths.
5. **PtrNet-RSA:** Uses pointer networks to select constituent nodes, removing the restriction of pre-calculated K-shortest paths.

## 4. Heuristic Algorithm Benchmark Evaluation

### A. Effect of path ordering
A critical finding is that sorting candidate paths by the **number of hops** (#hops) rather than total physical distance in km (#km) significantly reduces blocking probability because shorter hop counts generally occupy fewer spectral resources.

### B. Simulation setup
Using the XLRON framework, three experiments were conducted across four topologies (NSFNET, COST239, USNET, JPN48) to test various heuristics:
* **Exp 1:** Evaluated performance as candidate path count (K) increases.
* **Exp 2:** Tested the effect of K across different traffic loads.
* **Exp 3:** Compared all heuristics at a high K-value (K=50) across varying loads.

### C. Results and discussion
The results show that blocking probability decreases monotonically as K increases, stabilizing around K=50. KSP-FF (K-Shortest Path First-Fit) and FF-KSP (First-Fit K-Shortest Path) are the strongest heuristics. Specifically, FF-KSP is superior for larger networks (USNET, JPN48), while KSP-FF performs well on smaller ones. The authors conclude that KSP-FF with K=50 and #hops ordering provides a robust benchmark.

## 5. Benchmarking of Previous Work

### A. Holding time truncation
The authors identify a critical flaw in the widely used DeepRMSA codebase: service holding times are resampled if they exceed twice the mean. This "truncation" reduces the effective mean holding time by ~31%, meaning papers using this code evaluated their agents under significantly lower traffic loads than reported.

### B. Benchmarking of published results
The authors recreated the problem settings of the five selected papers and compared the published RL results against various heuristic versions.
* **Findings:** Simple heuristics (especially 50-SP-FF with #hops ordering) match or exceed the performance of all published RL solutions in nearly every case.
* **Impact:** In many instances, the optimized heuristic reduces blocking probability by over an order of magnitude compared to the reported RL solution. This suggests that previous claims of RL superiority were based on weak benchmarks.

## 6. Network Blocking Bounds

### Resource-Prioritized Defragmentation
To determine if there is still "hope" for RL, the authors develop a method to estimate lower bounds on blocking probability by relaxing the "No Reconfiguration" constraint (allowing defragmentation). The algorithm sorts active requests by resource requirements (spectral slots $\times$ hops) and re-allocates them sequentially. This creates an omniscient baseline that represents the theoretical limit of network capacity.

### A. Experiment setup
The authors compare the best performing heuristic against this Resource-Prioritized Defragmentation bound across a range of traffic loads for the five selected case studies, focusing on the traffic load supported at 0.1% SBP.

### B. Results and discussion
The gap between the best heuristics and the theoretical bound is substantial: in flex-grid networks, supported traffic could be increased by **19–36%**. While PtrNet-RSA's fixed-width requests showed a smaller gap (1–8%), the elastic cases show significant room for improvement. This demonstrates that while current RL solutions are underperforming, there is a considerable optimality gap that justifies further research.

## 7. Conclusion
The authors conclude that RL for DRA in optical networks has been characterized by "hype" due to deficient benchmarking and reproducibility practices; most published RL solutions are outperformed by simple, well-tuned heuristics. However, the existence of a significant gap between these benchmarks and the defragmentation bound proves there is "hope." Future research should adopt rigorous standards (K=50, #hops ordering) and focus on holistic network objectives or bridging the identified optimality gap.
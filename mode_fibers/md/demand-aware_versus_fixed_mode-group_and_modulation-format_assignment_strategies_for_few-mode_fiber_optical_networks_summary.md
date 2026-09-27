---
index_terms:
  - few-mode fiber
  - mode-group division multiplexing
  - resource allocation
  - modulation format assignment
  - blocking probability
  - multidimensional overprovisioning
  - RMMWA problem
---

# Demand-Aware Versus Fixed Mode-Group and Modulation-Format Assignment Strategies for Few-Mode Fiber Optical Networks

## I. Introduction
Few-Mode Fiber (FMF) networks using Mode-Group Division Multiplexing (MGDM) increase capacity by transmitting multiple spatial modes in a single fiber. MGDM groups strongly coupled modes into "spatial superchannels," allowing them to be routed together and detected with reduced MIMO complexity, while different mode-groups can be independently multiplexed and switched.

A central challenge in MGDM-WDM networks is the trade-off between optical reach and transmission capacity; lower-order mode-groups generally offer longer reach but lower capacity. This leads to "multidimensional overprovisioning," where the assigned resource configuration provides more reach or capacity than a specific request requires, wasting resources.

The paper focuses on the Routing, Modulation, Mode-Group, and Wavelength Allocation (RMMWA) problem. While previous heuristics like BANG (perfect-fit) and fixed-order list sorting (Reach-Sorted/RF-MMA and Rate-Sorted/CF-MMA) exist, they do not jointly optimize for both excess capacity and reach. This work proposes the Demand-Aware Mode-Group and Modulation-Format Allocation (DA-MMA) strategy, which dynamically ranks feasible configurations based on a weighted combination of capacity and reach overprovisioning to minimize resource waste and reduce blocking probability.

## II. Models

### A. Physical Layer Model
The system uses MGDM where mode-groups are sets of linearly polarized (LP) modes with similar propagation constants. An optical connection is established at a specific wavelength within a given mode-group. 

Key mathematical representations include:
- **Configuration Matrix ($\mathbf{A}$):** A matrix of all possible pairs of mode-groups ($\mathcal{G}$) and modulation formats ($\mathcal{M}$).
- **Attribute Matrices ($\mathbf{R}$ and $\mathbf{C}$):** Corresponding matrices that define the optical reach (km) and maximum bitrate/capacity (Gbps) for every pair in $\mathbf{A}$.

Two primary constraints are enforced:
1. **Continuity Constraint:** The wavelength must remain constant across the route.
2. **Modal–Spectral Exclusivity Constraint (MSEC):** No two connections can occupy the same combination of wavelength and mode-group on any single link, preventing collisions and crosstalk.

### B. Network and Traffic Models
The network is modeled as a graph $G=(N, L)$. Connection requests are defined by source, destination, and requested bitrate. Requests follow a Poisson arrival process with an exponential distribution for holding time. The offered load is measured in Erlangs.

## III. Mode-Group and Modulation-Format Allocation Algorithms for MGDM-WDM

### RMMWA Framework
The connection provisioning process follows four sequential steps:
1. **Routing Allocation (RA):** Selection of $K$-shortest paths.
2. **Modulation-Format Allocation (MFA) & Mode-Group Allocation (MGA):** Jointly choosing the $(g, m)$ pair (the focus of this paper).
3. **Wavelength Allocation (WA):** Assigning a wavelength using First-Fit, satisfying continuity and MSEC.

### A. Aspects Required for the Construction of Prioritized Lists
The algorithms use bijections ($\pi$) to create prioritized lists of mode-group and modulation-format pairs from index set $\mathcal{I}$. This ordering determines which resources are attempted first during the online allocation phase.

### B. Fixed-MMA Algorithms
Fixed strategies use a static priority list generated offline.
1. **RF-MMA (Reach-Prioritized):** Sorts pairs primarily by ascending optical reach and secondarily by ascending capacity. It aims to minimize reach waste.
2. **CF-MMA (Capacity-Prioritized):** Sorts pairs primarily by ascending transmission capacity and secondarily by ascending optical reach. It aims to minimize capacity waste.

Online, both use a First-Fit policy: the first pair in the list that satisfies the request's bitrate and route length is passed to the wavelength assignment stage.

### C. Adaptive MMA Algorithms
Adaptive strategies build priority lists dynamically for each request.
1. **BANG (Balanced Allocation of Mode-Group):** Employs a strict "perfect-fit" capacity criterion, only considering configurations where supported capacity exactly matches the requested bitrate. Among these, it prioritizes those with the minimum reach slack.
2. **DA-MMA (Demand-Aware Allocation):** 
    - Identifies all physically feasible pairs $\mathcal{A}_k^{(c_r)}$ that meet minimum bitrate and reach requirements.
    - Calculates "slacks" (excesses): $\Delta c_{i,j}$ (capacity) and $\Delta r_{i,j}$ (reach).
    - Computes a normalized decision factor: $F_{i,j} = \beta \bar{\Delta c}_{i,j} + \gamma \bar{\Delta r}_{i,j}$, where $\beta$ and $\gamma$ are tunable weights.
    - Ranks configurations by increasing $F_{i,j}$ (lowest total overprovisioning first).

### D. Computational Complexity Analysis
- **Fixed-MMA (RF/CF):** Online complexity is $\mathcal{O}(KGM)$ as they only scan a precomputed list.
- **Adaptive MMA (BANG/DA-MMA):** Online complexity is $\mathcal{O}(KGM \log(GM))$ due to the need to sort feasible configurations for every request.

## IV. Performance of MMA Algorithms

### A. Simulation Setup
Evaluations were performed using the C++ Flex Net Sim library with $K=3$ shortest paths and First-Fit wavelength assignment. The physical layer parameters (reach/capacity) were based on a BER threshold of $4 \times 10^{-3}$. Three topologies were used: UKNet (dense, high capacity), Extended-UKNet (link lengths scaled by 2.5x to emphasize reach constraints), and a Synthetic 5-node network (low capacity).

### B. Performance Results and Analysis

#### 1) UKNet Topology
In this capacity-abundant scenario where reach is rarely a bottleneck, CF-MMA and DA-MMA perform best. RF-MMA follows, while BANG performs worst because its strict perfect-fit policy discards too many feasible options, leading to higher blocking probability.

#### 2) Extended-UKNet Topology
Blocking probabilities increase significantly for all algorithms due to reach limitations. The performance gap between CF-MMA, RF-MMA, and DA-MMA narrows considerably; when physical feasibility is the primary constraint, the prioritization philosophy becomes less impactful. BANG remains the worst performer.

#### 3) Synthetic 5-Nodes Topology
In this capacity-limited scenario, DA-MMA achieves the best performance, followed by CF-MMA. Both significantly outperform RF-MMA and BANG. The joint slack minimization of DA-MMA provides a robust trade-off when resources are scarce.

#### 4) Quantitative Performance Gain over the Baseline
The Blocking Improvement Ratio (BIR) relative to BANG confirms topology dependence:
- **UKNet:** Capacity-driven strategies (CF-MMA, DA-MMA) provide the highest gain ($\approx 99\%$).
- **Extended-UKNet:** All strategies show similar, modest gains ($\approx 25\%$), as reach is the bottleneck.
- **5-Node Synthetic:** DA-MMA provides the highest gain ($95\%$).

### C. Discussion and Practical Implications
The study concludes that no single allocation strategy is universally optimal. The best choice depends on the network's structural bottleneck:
- **Capacity-dominated regimes:** Capacity-driven schemes (CF-MMA) are preferable.
- **Reach-constrained regimes:** Allocation policies have limited impact; physical layer improvements are more effective.
- **Heterogeneous/Constrained scenarios:** Balanced slack-aware approaches (DA-MMA) provide the most robustness.

## V. Conclusion
The paper demonstrates that DA-MMA effectively reduces blocking probability by balancing capacity and reach overprovisioning. While fixed-order strategies are computationally simpler, they fail to adapt to specific request demands as effectively as DA-MMA in resource-constrained environments. Future work will explore extending these algorithms to elastic optical networks (EONs), incorporating wavelength conversion, and utilizing AI/ML for optimizing decision mechanisms.
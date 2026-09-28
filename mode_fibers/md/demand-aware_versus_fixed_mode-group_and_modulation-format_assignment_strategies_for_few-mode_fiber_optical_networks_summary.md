---
index_terms:
  - Few-Mode Fiber
  - Mode-Group Division Multiplexing
  - Resource Allocation
  - RMMWA Problem
  - Multidimensional Overprovisioning
  - Demand-Aware MMA
---

# Demand-Aware Versus Fixed Mode-Group and Modulation-Format Assignment Strategies for Few-Mode Fiber Optical Networks

## I. Introduction
Few-Mode Fiber (FMF) technology enables Space Division Multiplexing (SDM) to increase network capacity beyond single-mode limits. Mode-Group Division Multiplexing (MGDM) specifically groups coupled modes into "superchannels" to reduce digital signal processing complexity while allowing independent routing and switching of mode-groups.

The primary challenge in MGDM-WDM networks is the Routing, Modulation, Mode-Group, and Wavelength Allocation (RMMWA) problem. Because different mode-group and modulation-format combinations offer varying trade-offs between optical reach and transmission capacity, these systems suffer from multidimensional overprovisioning—where the assigned resource exceeds the actual bitrate or distance required by a connection request.

While previous strategies like BANG (which uses a strict "perfect-fit" capacity policy) and fixed-list algorithms (Reach-Sorted/Rate-Sorted) exist, they either overly restrict feasible configurations or ignore request-specific demands. This paper proposes the Demand-Aware Mode-Group and Modulation-Format Allocation (DA-MMA) strategy, which dynamically prioritizes resources by jointly minimizing excess capacity and reach via a tunable weighting mechanism.

## II. Models

### A. Physical Layer Model
The network utilizes FMF spans and few-mode erbium-doped fiber amplifiers (FM-EDFA), supporting all-optical switching of mode-groups. Mode-groups $\mathcal{G}$ are sets of linearly polarized modes with similar propagation constants; modulation formats $\mathcal{M}$ vary in spectral efficiency.

A conceptual matrix $\mathbf{A}$ represents the set of all feasible (mode-group, modulation format) pairs. Two associated numerical matrices, $\mathbf{R}$ (reach) and $\mathbf{C}$ (capacity), define the physical capabilities of each pair. A key constraint introduced is the Modal–Spectral Exclusivity Constraint (MSEC), which mandates that no two connections occupy the same wavelength and mode-group combination on any single link to prevent crosstalk and collisions.

### B. Network and Traffic Models
The network is modeled as a graph $G=(N, L)$ where links have uniform total capacity. Connection requests are triplets of source, destination, and requested bitrate ($b$). Traffic follows a Poisson arrival process with exponential holding times; the load is measured in Erlangs.

## III. Mode-Group and Modulation-Format Allocation Algorithms for MGDM-WDM
The RMMWA process follows four sequential steps: Routing (using $K$-shortest path), Modulation-Format Allocation, Mode-Group Allocation, and Wavelength Allocation (using First-Fit). This paper focuses specifically on the joint Mode-Group and Modulation-Format Allocation (MMA) stage.

### A. Aspects Required for the Construction of Prioritized Lists
MMA algorithms use a bijection $\pi$ to order the feasible pairs in matrix $\mathbf{A}$ into prioritized lists, which are then scanned during the allocation process.

### B. Fixed-MMA Algorithms
Fixed strategies rely on static priority lists created offline. Online, they apply a First-Fit policy based on this list.
*   **RF-MMA (Reach-Prioritized):** Sorts pairs primarily by ascending optical reach and secondarily by ascending capacity to minimize reach-related waste.
*   **CF-MMA (Capacity-Prioritized):** Sorts pairs primarily by ascending transmission capacity and secondarily by ascending optical reach to minimize capacity-related waste.

### C. Adaptive MMA Algorithms
Adaptive strategies construct priority lists online, tailored to the specific requirements of each incoming request.
*   **DA-MMA (Demand-Aware):** First identifies a subset of physically feasible configurations $\mathcal{A}_k^{(c_r)}$ that meet bitrate and distance needs. It then calculates normalized "slacks" for capacity ($\Delta c$) and reach ($\Delta r$). A decision factor $F_{i,j} = \beta \bar{\Delta c}_{i,j} + \gamma \bar{\Delta r}_{i,j}$ is used to rank configurations in ascending order of total overprovisioning. The weights $\beta$ and $\gamma$ allow for tuning the priority between capacity and reach efficiency.
*   **BANG (Balanced Allocation of Mode-Group):** Implements a strict "perfect-fit" policy, only considering configurations where achievable capacity exactly matches requested bitrate ($c_{i,j} = b$). Among these perfect fits, it prioritizes those with the minimum reach slack.

### D. Computational Complexity Analysis
Fixed algorithms (RF-MMA and CF-MMA) have an online complexity of $\mathcal{O}(KGM)$. Adaptive algorithms (DA-MMA and BANG) require sorting for each request, resulting in a higher complexity of $\mathcal{O}(KGM\log(GM))$, where $G$ is the number of mode-groups, $M$ is the number of modulation formats, and $K$ is the number of candidate routes.

## IV. Performance of MMA Algorithms
Evaluation was conducted across three topologies: UKNet (high capacity, low reach constraint), Extended-UKNet (reach constraints scaled by 2.5x), and a synthetic 5-node network (low overall capacity).

### A. Simulation Setup
Simulations used the C++ Flex Net Sim library with $K=3$ routing and First-Fit wavelength assignment. Reach and capacity values were based on a BER threshold of $4 \cdot 10^{-3}$.

### B. Performance Results and Analysis
*   **UKNet Topology:** CF-MMA and DA-MMA performed best because reach is not a limiting factor, making capacity efficiency the primary driver of blocking probability. BANG performed worst due to its rigid perfect-fit policy, which discards too many feasible options.
*   **Extended-UKNet Topology:** Blocking probabilities increased for all algorithms as reach became the dominant constraint. RF-MMA, CF-MMA, and DA-MMA showed nearly identical performance because the limited set of physically feasible configurations reduced the impact of different prioritization philosophies.
*   **Synthetic 5-node Topology:** In this capacity-limited scenario, DA-MMA achieved the best performance. By balancing both resource dimensions, it proved more robust than purely reach-driven or capacity-driven strategies.

#### 4) Quantitative Performance Gain over the Baseline
Using the Blocking Improvement Ratio (BIR), the proposed algorithms showed significant gains over BANG:
*   **UKNet:** Up to 99% reduction in blocking for CF-MMA and DA-MMA.
*   **Extended-UKNet:** A modest ~25% gain across all strategies, confirming reach as the bottleneck.
*   **5-node Synthetic:** DA-MMA achieved a 95% improvement over BANG.

### C. Discussion and Practical Implications
The findings indicate that no single MMA strategy is universally optimal. The choice of algorithm should depend on the network's structural bottleneck: capacity-driven strategies are best for well-connected, short-reach networks, while balanced slack-aware approaches (DA-MMA) are superior in resource-constrained or heterogeneous environments.

## V. Conclusion
The paper demonstrates that DA-MMA provides a robust trade-off between blocking probability and resource utilization by jointly minimizing capacity and reach overprovisioning. While fixed strategies are computationally simpler, the adaptive nature of DA-MMA is particularly beneficial in capacity-limited scenarios. Future work includes extending these algorithms to elastic optical networks and exploring AI/ML for optimizing decision mechanisms.
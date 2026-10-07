---
index_terms:
  - Elastic Optical Networks
  - RMLSA problem
  - Genetic Algorithm
  - spectral fragmentation
  - resource allocation policies
  - modulation level assignment
---

# Routing, Modulation Level and Spectrum Allocation in EONs via Genetic Algorithm Under Different Assignment Criteria

## I. Introduction
This paper addresses the Routing, Modulation, and Spectrum Assignment (RMLSA) problem in Elastic Optical Networks (EONs). The objective is to optimize network resource usage by maximizing the number of satisfied demands while simultaneously minimizing the demand-blocking ratio and spectral fragmentation. 

The authors propose a Genetic Algorithm (GA) where chromosomes encode possible routes for demands. Unlike previous works that treat spectral fragmentation as a control indicator, this study incorporates it directly into a mixed evaluation function to jointly minimize blocking and fragmentation. The core of the research investigates whether different demand ordering criteria—Random Order (RO), Decreasing Data Rate (DDR), and Most Subcarriers First (MSF)—significantly impact the GA's performance in allocating resources.

## II. Elastic Optical Networks and the RMLSA Problem
EONs utilize a flexible grid (SLICE) technique that divides the optical spectrum into fixed-width slots (12.5 or 6.25 GHz). In a fiber with 4.475 THz bandwidth, 358 slices are available per link. The RMLSA problem involves choosing an optimal route, a modulation level, and a contiguous set of spectral slices to meet a specific bitrate demand.

Key technical constraints include:
- **Routing:** Modified Link State algorithms (like OSPF-TE or IS-IS-TE) and Yen's algorithm are used to determine $k$-shortest paths based on Dijkstra’s algorithm.
- **Modulation:** The transmission rate is defined as $C = B \log_2 M$ (where $B$ is bandwidth and $M$ is the modulation level). Higher modulation levels increase bitrate but reduce noise robustness; therefore, longer routes require lower modulation levels and more spectral slices to achieve the same target bitrate.
- **Spectrum Allocation:** The authors utilize the First-Fit allocation policy, which assigns demands to the first available free slices closest to the beginning of the spectrum.

## III. Proposed Genetic Algorithm
The GA searches for optimal RMLSA solutions using a population of chromosomes. Each gene in a chromosome indexes one of the $k$-shortest paths provided by Yen's algorithm for a specific demand. 

### A. Fitness Function
The fitness function $f_1$ is designed to prioritize solutions with zero blocking and zero fragmentation. It is defined by three conditions:
1. If both Blocking and Fragmentation are zero, fitness is 0 (optimal).
2. If Blocking is zero but Fragmentation is non-zero, fitness is 0.5.
3. Otherwise, a weighted trade-off is used: $f_1 = 5 \times \text{Blocking} + 3 \times \text{Fragmentation}$.

Other performance metrics tracked include the percentage of total transmission rate met, spectral occupancy (average ratio of occupied slices across links), and the index of the last subcarrier used per link.

### B. Demand Ordering for Resource Allocation
The authors test three different schemes for ordering how demands are processed for resource allocation:
- **Random Order (RO):** Demands are attended randomly with no prioritization.
- **Decreasing Data Rate (DDR):** Demands are ordered by requested transmission bitrate in descending order.
- **Most Subcarriers First (MSF):** Demands are ordered by the number of subcarriers required, which is a function of both the demanded bitrate and the route length (modulation level).

## IV. Algorithm Performance Evaluation

### A. Parameters of the Genetic Algorithm
To maintain genetic diversity, the initial population ensures all $K$ possible routes for every demand are present. The total initial population size is $(K + 1) \times D$, where $D$ is the number of demands and $K=3$. Selection is performed via roulette wheel with elitism. Mutation occurs at a rate of 0.2%, and the algorithm stops after 50 generations.

### B. Network Topology
Simulations are conducted on the NSFNET American backbone network, consisting of 16 nodes with realistic geographic distances between them.

### C. Requested Demands
The GA is tested against sets of 75, 100, and 150 demands. Origin and destination nodes are randomly selected, and transmission rates are drawn from a predefined list ranging from 10 Gbps to 1 Tbps.

### D. Number of Rounds
To ensure statistical significance, the authors used the Wilcoxon (Mann-Whitney U) test to determine when the performance indicator distributions stabilized. This resulted in 132 simulation rounds.

### E. Results
The results are analyzed via Cumulative Distribution Functions (CDFs) and variance:
- **75 Demands:** All three criteria show nearly identical blocking ratios (0% at 90th percentile). MSF shows slightly lower fragmentation than RO.
- **100 Demands:** MSF provides the lowest blocking ratio at the 90th percentile (1.8%), followed by DDR (3%) and RO (4%). 
- **150 Demands:** Performance remains similar across criteria, though RO exhibits lower variance in some metrics and slightly better blocking ratios than ordered schemes.

The authors conclude that while the choice of ordering does not drastically change the overall performance, there is a trade-off: ordered schemes (MSF/DDR) are more effective at reducing spectral fragmentation, whereas the Random Order (RO) scheme tends to result in lower blocking ratios and higher transmission rates achieved. This may be because RO prevents premature convergence by maintaining higher variability in the population.

### F. Analysis of the Number of Hops per Demand and the Index of Last Subcarrier Occupied per Link
- **Hops:** The median number of hops is consistently 4 across all scenarios, indicating that routing is primarily driven by Yen's algorithm rather than the fitness function.
- **Last Subcarrier Index:** This metric acts as a proxy for link occupancy. RO typically results in a slightly lower index (less occupied links) compared to MSF and DDR, particularly at lower demand loads (75 demands).

## V. Conclusion
The proposed GA effectively solves the RMLSA problem by minimizing blocking and fragmentation. Statistical analysis indicates that while different assignment criteria do not cause massive performance shifts, RO is preferable for reducing blocking and improving occupancy, whereas ordered schemes are superior for reducing spectral fragmentation. Future research will explore new fitness functions to improve link balancing.
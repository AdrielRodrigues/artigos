---
index_terms:
  - MB-SDM-EONs
  - RSCBA problem
  - stimulated Raman scattering
  - band partition protection
  - genetic algorithm
  - network survivability
  - multi-core fiber
---

# Survivable Routing, Spectrum, Core and Band Assignment in Multi-Band Space Division Multiplexing Elastic Optical Networks

## I. Introduction
The increasing demand for transport network capacity has led to a "capacity crunch." To address this, two primary technologies are utilized: Space Division Multiplexing (SDM), which uses multiple spatial channels (e.g., multi-core fibers), and Multi-Band (MB) transmission, which expands frequency bands beyond the C-band into L, S, E, and O bands. Combining these results in MB-SDM networks, shifting the resource allocation problem from Routing, Spectrum, and Core Assignment (RSCA) to Routing, Spectrum, Core, and Band Assignment (RSCBA).

A significant challenge in MB systems is Stimulated Raman Scattering (SRS), a nonlinear effect that transfers power from higher frequency bands to lower ones, impacting Signal-to-Noise Ratio (SNR) and Quality of Transmission (QoT). Additionally, link failures in high-capacity networks cause massive service interruptions, requiring robust survivability strategies. This paper proposes a "band partition protection scheme" using cold backup, where working resources are allocated in the C-band and protection resources in the L-band to maximize SNR during normal operation by minimizing inter-band interference.

### A. Related Work
Existing research covers multi-band technology (C+L systems), SRS modeling for QoT estimation, and RSCA in SDM-EONs. While some studies have experimentally combined MB and SDM for throughput, the specific RSCBA problem for survivable MB-SDM networks—particularly considering the interaction of SRS and crosstalk—remains unaddressed.

### B. Paper Contributions and Organization
The authors contribute a band partition protection scheme that separates working (C-band) and backup (L-band) resources to reduce SRS impact on active services. They formulate this as an Integer Linear Programming (ILP) model considering both inter-core crosstalk and SRS. To handle large-scale networks where ILP is computationally intractable, they propose a heuristic algorithm based on a Genetic Algorithm (GA).

## II. System Model and QoT Estimation

### A. Network and Traffic Model
The network is modeled as a graph $G(V, E)$ using multi-core fibers (MCF). The available spectrum is divided into C-band ($F^C$) and L-band ($F^L$) frequency slots of 12.5 GHz each. Traffic demands are static and defined by source, destination, and required bandwidth. For each demand, $k$-shortest disjoint path pairs (working and protection) are pre-calculated. Resource allocation must satisfy spectrum contiguity (contiguous slots), spectrum continuity (same slots across a path), and core continuity (same core across a path).

### B. Crosstalk and QoT Estimation
Transmission quality is affected by two primary interferences:
1.  **Inter-core Crosstalk (XT):** Occurs when adjacent cores in an MCF use the same spectrum. The model ensures end-to-end XT remains below a predefined threshold $\Omega$.
2.  **Quality of Transmission (QoT/SNR):** SNR is calculated by considering launch power against Amplified Spontaneous Emission (ASE) noise and Nonlinear Interference (NLI). NLI consists of Self-Channel Interference (SCI) and Cross-Channel Interference (XCI), both of which are modified by SRS, as SRS alters the fiber gain/loss profile and spectral tilt.

## III. ILP Formulation

### A. ILP-BP
The proposed Integer Linear Programming for Band Partitioning (ILP-BP) aims to minimize the maximum index of allocated frequency slots ($F_{max}$) and maximize SNR. 
*   **Path and Core Selection:** Constraints ensure each request has exactly one primary and one backup path that are link-disjoint, and a consistent core assignment across these paths.
*   **Spectrum Assignment:** Constraints enforce non-overlapping FS usage and contiguity requirements.
*   **Band Partitioning:** Specific constraints mandate that working resources reside strictly in the C-band and protection resources reside in the L-band.
*   **Physical Layer Constraints:** Assignments must maintain XT below $\Omega$ and SNR above a minimum threshold $\Xi$.

### B. ILP-MIX
As a baseline, the ILP-MIX model is formulated without band partition constraints, allowing both working and backup resources to be allocated across C and L bands using a first-fit approach.

## IV. Heuristic Algorithm

### A. GA-S-RSCBA-BP
To solve RSCBA for large networks, a Genetic Algorithm (GA) is proposed. 
*   **Encoding:** Each "gene" consists of the selected path pair and core assignments for a demand. A "chromosome" represents a complete network solution.
*   **Fitness Function:** Evaluates solutions based on a weighted balance between the successful protection rate ($S_p$) and resource utilization (measured by the maximum allocated FS index).
*   **Genetic Operators:** Employs elite selection, 2-point crossover, and mutation. To prevent premature convergence to local optima, the crossover ($\rho_C$) and mutation ($\rho_M$) probabilities are adaptively adjusted based on the fitness of individuals relative to the population's best.

### B. Alternative Algorithms
For comparative analysis, several alternatives are implemented: 
*   **D-C+L-BP:** Band partitioning using a Dijkstra framework instead of GA.
*   **GA-C only / D-C only:** Scenarios limited to the C-band only.
*   **GA-C+L-mix:** A mixed scenario where working and protection resources are randomly distributed across bands.

## V. Simulation Results and Discussions
Simulations were performed on 6-node and NSFnet topologies using Gurobi (for ILP) and MATLAB.

### A. Comparison of ILP and Heuristic Algorithm
The GA-S-RSCBA-BP algorithm provides resource allocation results very close to the optimal ILP-BP solution, with a maximum difference in FS index assignment of within 8%. This validates the heuristic's effectiveness for large networks.

### B. Performance of Heuristic Algorithms
*   **SNR Benefits:** GA-S-RSCBA-BP shows a higher SNR ratio compared to GA-C+L-mix as request volume increases. This is because in the MIX scenario, L-band resources are used for working paths, causing SRS interference with C-band paths; however, the BP scheme keeps L-band idle until a failure occurs.
*   **Resource Utilization:** GA-based methods achieve lower maximum FS indices than Dijkstra-based methods due to global optimization and bandwidth-priority sorting.
*   **Survivability:** The protection rate is highest for GA-S-RSCBA-BP. Separating bands reduces SRS interference, which keeps more frequency slots viable (above SNR thresholds), thereby increasing the likelihood of finding valid protection resources.
*   **Capacity expansion:** Combining MB and SDM significantly increases the number of requests that can be served compared to single C-band SDM.
*   **Weight Impact:** Adjusting the fitness function weight $w$ allows a trade-off between maximizing the protection rate and minimizing spectrum fragmentation/utilization.

## VI. Conclusion
The paper demonstrates that a band partition protection scheme (C-band for working, L-band for backup) effectively improves network SNR by mitigating SRS interference without significantly sacrificing spectrum compactness. The proposed GA-S-RSCBA-BP heuristic offers a scalable and near-optimal solution for the RSCBA problem in MB-SDM-EONs. Future work will explore placing working resources in the L-band and investigating inter-core SRS effects.
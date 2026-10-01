---
index_terms:
  - CF-RAN
  - network-assisted free-duplex
  - partial distributed block coordinate descent
  - sum-rate maximization
  - distributed transceiver design
  - duplex mode selection
  - team MMSE
---

# Decentralized Optimization of Spectral Efficiency for Scalable CF-RAN With Network-Assisted Free-Duplex

## I. Introduction
The paper addresses the scalability challenges in Cell-Free Radio Access Networks (CF-RAN) employing network-assisted free-duplex (NA-FD) architecture. While NA-FD allows access points (APs) to dynamically switch between full, hybrid, and flexible duplex modes to increase spectral efficiency (SE), it introduces severe cross-link interference (CLI) and requires heavy centralized processing at the Cloud Computing Unit (CCU). To resolve this, the authors propose a distributed framework that balances computational complexity and performance by leveraging Edge Distributed Units (EDUs). The primary contributions include a sum-rate maximization model transformed into a minimum mean square error (MSE) problem, a partial distributed block coordinate descent (PDBCD) algorithm for transceiver design featuring an adaptive EDU information-sharing mechanism, and a low-complexity greedy search algorithm for optimal AP duplex mode selection.

## II. System Model

### A. CF-RAN With NA-FD Architecture
The system follows a hierarchical structure: the CCU manages AP associations and mode selection; EDUs handle uplink (UL) detection and downlink (DL) precoding; and APs perform radio frequency transmission/reception. Scalability is achieved through flexible cooperation schemes (partial, distributed, or centralized). Resource allocation is joint across spatial, time, and frequency domains, allowing NA-FD to be treated as a specialized form of spatial-domain duplex scheduling.

### B. Channel Model
The system consists of $M$ APs (equipped with $N$ antennas), $X$ EDUs, $K$ downlink UEs, and $J$ uplink UEs. The authors assume frequency-flat fading and model the channel between any two antennas as a product of large-scale fading coefficients and small-scale Rayleigh fading. APs are scheduled as either Transmitting APs (TAPs) or Receiving APs (RAPs).

### C. Downlink Data Transmission Model
The signal received by a downlink UE includes contributions from TAPs, interference from other downlink users, and uplink-to-downlink user interference (IUI). The DL sum-rate is defined based on the Signal-to-Interference-plus-Noise Ratio (SINR) $\gamma_{D,k}$.

### D. Uplink Data Transmission Model
RAPs receive signals from uplink UEs but are subject to inter-AP interference (IAI) caused by TAPs. While EDUs cooperate to suppress IAI using reconstructed signal cancellation, residual IAI persists due to channel estimation errors. The combined UL sum-rate is determined by the aggregated SINR $\gamma_{U,j}$ at the CCU after receiving processed data from all EDUs.

### E. Optimization Model
The goal is to maximize the joint uplink and downlink sum-rate subject to per-AP transmit power constraints, per-UE uplink power limits, and AP duplex mode constraints (each AP must be either a TAP or a RAP). The optimization depends on partial observation information $S_x$ available at each EDU, which may include local channel estimates and shared sideband information from other EDUs.

## III. Distributed Transceiver Design and Duplex Mode Selection

### A. Problem Transformation
To handle the non-convexity of the sum-rate maximization problem, the authors use the MMSE-SINR relationship to transform it into a weighted minimum mean squared error (WMMSE) problem. This involves minimizing an objective function $\chi_D + \chi_U$ across auxiliary variables $\alpha$, receive filters $u_D$, precoding vectors $W$, and receiving vectors $V$.

### B. Distributed Solution for Subproblem 1
This subproblem focuses on optimizing the uplink receiving vectors $V$. The authors propose an EDU-TMMSE (Team MMSE) scheme based on team theory, allowing EDUs to compute local receivers using a two-layer structure: an instantaneous EMMSE receiver $A_x$ and a compensation matrix $B_x$. An EDU sharing mechanism is introduced where EDUs can be in "Shared" (On) or "Non-shared" (Off) states. Shared EDUs exchange instantaneous equivalent channel information, while non-shared EDUs rely on statistical information provided by the CCU, creating a tunable trade-off between signaling overhead and SE.

### C. Distributed Solution for Subproblem 2
This subproblem optimizes downlink precoding $W$, weights $\alpha_D$, and filters $u_D$. Due to the complexity of centralized WMMSE, the authors propose a distributed serial-parallel update scheme. Within each EDU, TAPs are updated serially; across different EDUs, updates occur in parallel via the CCU. To ensure stability and prevent fluctuations during parallel iterations, a Jacobi best-response smoothing scheme is employed.

### D. Centralized Solution for Subproblem 3
The optimization of uplink transmit power $p_U$ and weights $\alpha_U$ is handled centrally at the CCU. This is solved by taking the partial derivative of the MSE function with respect to $p_U$, resulting in a closed-form local optimal solution subject to UE power constraints.

### E. Greedy Search for AP Duplex Mode Selection
Since duplex mode selection ($\mu$) is a binary integer programming problem, an exhaustive search is computationally prohibitive. The authors propose a greedy bit-flipping algorithm: starting from a random configuration, the algorithm iterates through each AP and flips its mode (TAP $\leftrightarrow$ RAP) if it increases the overall sum rate. This reduces complexity from exponential to linear relative to the number of APs while maintaining near-optimal performance.

## IV. Simulation Results and Performance Analysis
Simulations with 48 APs and 4 EDUs validate several key claims:
- **Convergence:** The PDBCD algorithm converges rapidly (typically within 2-3 outer loop iterations).
- **Interference Management:** The greedy mode selection effectively mitigates the impact of residual IAI, outperforming random or fixed duplex modes, especially in high-interference scenarios.
- **Scaling and Resources:** SE increases monotonically with the number of UEs and antennas per AP, with NA-FD benefiting more from additional antennas than TDD due to better interference suppression.
- **Sharing Levels:** A hierarchy of performance is observed: PDBCD-FULL (all EDUs sharing) $\approx$ Centralized MMSE $>$ PDBCD-HALF $>$ PDBCD-NO. The proposed GPDBCD-FULL achieves near-optimal sum-rates within 3 bps/Hz of the centralized upper bound.
- **Backhaul Efficiency:** Under limited backhaul capacity per EDU, G-NAFD demonstrates significantly higher SE compared to TDD (e.g., a 67% improvement at lower capacities), confirming its efficiency in resource utilization.

## V. Conclusion
The paper successfully develops a scalable distributed optimization framework for CF-RAN with NA-FD. By transforming the sum-rate problem into an MSE minimization task and employing PDBCD with team MMSE reception and a serial-parallel precoding update, the authors reduce the computational burden on the CCU. Combined with a greedy duplex mode selection strategy, the proposed scheme achieves high spectral efficiency and robustness against cross-link interference while maintaining low signaling overhead via adaptive EDU sharing.
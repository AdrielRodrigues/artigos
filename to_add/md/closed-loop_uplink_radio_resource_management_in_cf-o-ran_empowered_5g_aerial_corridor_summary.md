---
index_terms:
  - Cell-Free Massive MIMO
  - O-RAN
  - 5G Aerial Corridor
  - Radio Resource Management
  - Spectral Efficiency
  - Uplink Power Control
  - UAV-O-RU Association
  - Channel Knowledge Map
---

# Closed-loop Uplink Radio Resource Management in CF-O-RAN Empowered 5G Aerial Corridor

## Abstract
The paper proposes a radio resource management (RRM) framework for 5G aerial corridors using an Open Radio Access Network (O-RAN) enabled cell-free (CF) massive MIMO system. The goal is to maximize the minimum spectral efficiency (SE) by jointly optimizing unmanned aerial vehicle (UAV)-to-open radio unit (O-RU) association and uplink (UL) transmit power under quality-of-service (QoS) constraints. To solve the NP-hard optimization problem, the authors use alternating optimization (AO) involving a QoS-driven association algorithm and a bisection-guided fixed-point power control algorithm hosted as an xApp in the near-real-time RAN Intelligent Controller (RIC). To reduce signaling overhead from global channel state information (CSI), they implement a channel knowledge map (CKM) in the non-RT RIC. Simulation results indicate significant improvements in minimum SE, QoS satisfaction, and fairness, with a substantial reduction in runtime compared to interior point solvers.

## I. Introduction
Aerial corridors are structured 3D routes for beyond visual line of sight (BVLOS) UAV traffic. Ensuring reliable connectivity requires specialized terrestrial cellular re-engineering. While O-RAN provides programmability via the RIC to manage dynamic UAV scenarios, strong line-of-sight (LoS) links in aerial environments create severe UL interference.

The authors integrate CF mMIMO into the O-RAN architecture because it provides macro-diversity and robust connectivity by serving users through multiple distributed access points. The paper contributes:
1. An O-RAN framework using a CKM in the non-RT RIC to circumvent E2 interface limitations regarding high-rate CSI exchange.
2. A max-min SE optimization problem solved via AO, featuring a QoS-driven association algorithm and a bisection-guided fixed-point power control method.
3. Simulation evidence of improved minimum SE, QoS, and fairness with real-time deployment feasibility.

## II. System Model
The system consists of $K$ single-antenna UAVs served by $L$ distributed O-RUs, each with $N_\ell$ antennas. The network operates in TDD mode. 

**Operational Flow:** A CKM rApp (non-RT RIC) manages propagation statistics to reduce reliance on real-time CSI. Telemetry data flows via the O1 interface to a global database, updates the CKM, and policy/CSI data is sent via the A1 interface to the local RAN DB. RRM xApps (near-RT RIC) then compute decisions based on this data and send instructions via the E2 interface to the O-DU/O-CU, which forwards them to O-RUs.

### A. Channel Model
The channel incorporates large-scale fading (path loss and shadowing using 3GPP UMa-AV height-dependent LoS probability) and small-scale Rician fading (spatially correlated with a dominant LoS component). The channel is represented in mean-plus-deviation form.

### B. Channel Estimation
MMSE channel estimation is used at the O-DU/O-CU, though pilot reuse among $K$ UAVs leads to pilot contamination. L-MMSE combining is applied at O-RUs, and a central CPU combines these using maximal ratio combining (MRC) weights. The UL SE for each UAV is calculated based on the signal-to-interference-plus-noise ratio (SINR).

## III. Problem Formulation
The objective is to maximize the minimum SE across all UAVs by jointly optimizing the association matrix $\mathbf{A}$ and transmit powers $p_k^u$. 

**Constraints include:**
1. Every UAV must connect to at least one O-RU.
2. Each O-RU can serve a maximum of $\tau_p$ UAVs (limited by pilot orthogonality).
3. Minimum SE requirements ($SE_k \ge SE_k^{\min}$) for QoS guarantees.

This is formulated as a mixed-integer nonlinear programming (MINLP) problem, which is NP-hard due to the non-convex nature of the $\log_2(1+\Gamma_k)$ function and the binary association variables.

## IV. Proposed Solution
The authors decouple the problem into two sub-problems solved via alternating optimization (AO).

### A. UAV-O-RU Association Assignment
Since global optimization for association is computationally prohibitive ($\mathcal{O}(2^{KL})$), a three-stage heuristic algorithm is proposed:
1. **UAV-centric initialization:** Each UAV connects to its strongest O-RU based on large-scale fading.
2. **O-RU-centric load balancing:** Under-capacity O-RUs associate with their strongest remaining UAVs to balance load.
3. **QoS-driven refinement:** UAVs failing the $SE_k^{\min}$ threshold are iteratively connected to additional O-RUs in descending order of channel strength until QoS is met or a limit ($\lceil L/2 \rceil$) is reached.

The total computational complexity is approximately $\mathcal{O}(KL)$.

### B. UL Data Transmit Power Allocation
To avoid the high complexity of interior-point solvers (like CVX), the authors propose a Bisection-Guided Fixed-Point Power Control (BG-FPPC) algorithm:
- **Outer Loop:** Uses bisection search to find the maximum feasible target SINR ($\gamma^*$).
- **Inner Loop:** Employs fixed-point iteration to determine the minimum power required to achieve the current $\gamma_{\rm mid}$.
- If $\max p_k^u \le p^{\max}$, the target is feasible, and the search continues for a higher SINR.

Complexity is $\mathcal{O}(K^2)$, which is significantly lower than CVX's $\mathcal{O}(K^{3.5})$.

### C. The Overall Solution to the Problem P0
The coupled problem is solved by alternating between the association algorithm and the power control algorithm, starting with maximum power. Convergence is guaranteed due to the monotonic improvement of a bounded objective, typically occurring within 3–5 iterations.

## V. Numerical Evaluation
Simulations use 100 O-RUs over a $1 \times 1\text{ km}^2$ area following 3GPP UMa-AV specifications.

1. **Minimum SE Performance:** Joint optimization (PA + PP/TP) improves minimum SE by up to 440% compared to the baseline. The proposed BG-FPPC (PP) achieves identical performance to the CVX solver (TP), proving its global optimality.
2. **Success Rate:** The proposed association scheme is the dominant factor in meeting QoS; it achieves a 100% success rate for $K \le 90$ UAVs, whereas baseline associations fail regardless of power control.
3. **Fairness:** Power optimization is the primary driver of fairness. All schemes using max-min power allocation achieve 100% fairness (Jain's index), a 70% improvement over the baseline.
4. **Computational Complexity:** The BG-FPPC algorithm reduces runtime by up to 99.1% compared to CVX, bringing execution time within the 10–150 ms range required for near-RT RIC compliance.

## VI. Conclusion
The paper presents a joint association and power allocation framework for O-RAN enabled CF mMIMO in aerial corridors. By integrating a CKM in the non-RT RIC, they reduce CSI overhead. The study concludes that while association design is critical for meeting QoS requirements, power control is essential for fairness. The proposed AO framework provides an optimal solution within sub-second runtimes, making it suitable for real-time O-RAN deployment. Future work focuses on joint trajectory optimization.
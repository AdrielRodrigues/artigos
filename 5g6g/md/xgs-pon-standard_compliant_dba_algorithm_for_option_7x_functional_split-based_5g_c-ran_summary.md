---
index_terms:
  - XGS-PON
  - 5G C-RAN fronthaul
  - dynamic bandwidth allocation
  - functional splitting
  - traffic prediction
  - fronthaul latency
---

# XGS-PON-Standard Compliant DBA Algorithm for Option 7.x Functional Split-Based 5G C-RAN

## I. Introduction
Centralized Radio Access Network (C-RAN) enhances radio resource allocation and cost efficiency by centralizing Baseband Unit (BBU) functions, splitting the architecture into Remote Radio Heads (RRHs) and a BBU pool. Modern architectures incorporate Radio Units (RU), Distributed Units (DU), and Centralized Units (CU). The primary challenges of C-RAN are massive fronthaul bandwidth requirements and stringent latency constraints (typically $< 300\mu\text{s}$).

The authors propose using 10-Gigabit Capable Symmetrical Passive Optical Network (XGS-PON) as a cost-effective fronthaul solution due to its symmetry, simplicity, and use of passive optical distribution networks.

### A. Motivation
While Option 7.x functional splits reduce bandwidth needs, XGS-PON's inherent upstream scheduling delay—caused by the time required for Dynamic Bandwidth Allocation (DBA) cycles—often exceeds the C-RAN latency budget. Reactive DBA schemes are insufficient for bursty traffic. The authors aim to integrate traffic prediction with enhanced residual bandwidth utilization to optimize both delay and throughput.

### B. Objective
The objective is to jointly optimize throughput and delay in XGS-PON-based C-RAN fronthaul networks using a novel algorithm called Traffic Prediction-based Enhanced Residual Bandwidth Utilization (TP-ERBU). This approach differs from previous works by dynamically reallocating residual bandwidth from lightly loaded Optical Network Units (ONUs) to heavily loaded ones.

### C. Challenges
The main challenge is minimizing upstream delay where ONUs must wait for grants from the Optical Line Terminal (OLT). In conventional DBA, data arriving after a *Report* frame but before a *Gate* frame waits at least one cycle. Additionally, "quiet windows" used for ranging new ONUs can disrupt Constant Bit Rate (CBR) traffic flow.

### D. Contributions
- **TP-ERBU Algorithm:** A standard-compliant DBA algorithm combining a high-order moving average traffic prediction mechanism with dynamic residual bandwidth redistribution.
- **Dynamic Bandwidth Limits:** Instead of constant allocation limits, the algorithm dynamically adjusts maximum allocation bytes based on residual bandwidth from other ONUs.
- **XCRAN-SIMMODULE:** A simulation module developed in OMNeT++ to validate performance against gGIANT and Optimized RR algorithms.
- **Performance Gains:** Demonstrates improvements in packet delay (20.59%), channel utilization (38.33%), packet loss (25.00%), jitter (5.71%), and throughput (15.56%).

## II. Background and Related Work

### A. Functional Split Options for C-RAN Fronthaul
The paper reviews 3GPP functional splits ranging from Option 1 (fully centralized) to Option 8 (fully distributed). Focus is placed on the **Option 7.x** series (intra-PHY layer splits), which provide a balance between fronthaul capacity and control flexibility.

### B. Related Works
The authors examine existing DBA schemes:
- **Cooperative DBA:** Requires complex synchronization between BBU and OLT.
- **gGIANT:** Improves utilization via grouped assured bandwidth but fails C-RAN latency requirements.
- **RR-DBA & Optimized RR:** Round-robin approaches that redistribute excess bandwidth, though still struggling with bursty traffic.
- **ML/DL-based Prediction:** While accurate, deep learning methods suffer from high computational overhead (requiring GPUs) and sensitivity to sudden traffic variations.

### C. Gap in the Literature
Existing XGS-PON research often prioritizes either throughput or resource allocation, neglecting the simultaneous stringent low-latency requirements of 5G C-RAN. Furthermore, complex DL models lack reproducibility and real-time practicality. TP-ERBU fills this gap by combining a simple, computationally efficient prediction model with bandwidth optimization.

## III. Network Architecture and Fronthaul Latency Analysis

### A. XGS-PON System Model
The system consists of an OLT at the central office and multiple ONUs connected via passive splitters. It employs four Transmission Container (T-CONT) types: fixed (T-CONT-1), assured (T-CONT-2), non-assured (T-CONT-3), and best-effort (T-CONT-4). Upstream traffic is managed via a polling mechanism involving *Report* frames from ONUs and BWmap (Bandwidth Map) grants from the OLT.

### B. C-RAN Architecture Employing XGS-PON Fronthaul Transport
The architecture integrates a centralized BBU pool, an OLT at the central office, and RRHs connected to ONUs. The TP-ERBU algorithm is implemented within the OLT to predict traffic arrivals from RRHs and adjust bandwidth grants proactively.

### C. Objective: Joint Optimization of Throughput and Delay
TP-ERBU aims to minimize queuing delays while maximizing upstream channel utilization, specifically for Option 7.x splits where efficiency is paramount.

### D. Fronthaul Bandwidth Requirement Analysis of Option 7.x Splits
Bandwidth requirements depend on cell bandwidth, sub-carriers, modulation order, MIMO layers, I/Q size, and antenna ports. 
- **Option 7.1:** Transmits I/Q symbols in the frequency domain.
- **Option 7.2:** Multiplexes signals from multiple antenna ports to reduce bandwidth compared to 7.1.
- **Option 7.3:** Carries bits rather than I/Q symbols (demodulation occurs near antennas). This option has the lowest capacity requirement and is the primary focus of this study.

### E. Fronthaul Latency Analysis
Latency is analyzed for uplink traffic, including transmission time ($T_i$), propagation delay, compression/decompression delay, and FEC encoding/decoding delay. The authors focus on "Synchronized Phases" (Case A), where CPRI frames reach the ONU simultaneously. The primary goal of TP-ERBU is to minimize the queuing delay ($Q_i$) in the ONU buffer, which is the most significant variable component of total latency.

## IV. Dynamic Bandwidth Allocation for XGS-PON-Based C-RAN Fronthaul
Conventional DBA causes a "waiting period" where data arriving after a report frame must wait an entire cycle before being scheduled.

### A. Traffic Prediction-Based Enhanced Residual Bandwidth Utilization (TP-ERBU)
**1. Traffic Prediction Mechanism:** 
The OLT uses a fourth-order weighted moving average model to predict additional data ($P_i^t$) arriving during the waiting period. It calculates the arithmetic mean of previous cycles and the differences between consecutive cycles, assigning higher weights to more recent data to adapt quickly to bursty traffic without the overhead of deep learning.

**2. Bandwidth Allocation Scheme:**
The algorithm introduces a dynamic maximum allocation bytes limit ($A_i^t$). 
- **Overloaded ONUs:** If predicted demand exceeds the default limit ($A_{max}$), they are marked as overloaded and given a higher limit in the next cycle using residual bandwidth gathered from others.
- **Lightly Loaded ONUs:** These have their limits reset to $A_{max}$.
- **Residual Redistribution:** Total unused bandwidth is calculated at the end of each cycle and uniformly redistributed among heavily loaded ONUs in the subsequent cycle.

### B. Time and Space Complexity Analysis of TP-ERBU
Both time and space complexity are $O(N)$, where $N$ is the number of ONUs, as all operations (polling, prediction, grant assignment) scale linearly. This is significantly more efficient than ML-based methods, which often exhibit $O(N^2)$ complexity and require GPU inference.

### C. Traffic Model for C-RAN Uplink Data
The authors use a Poisson-Pareto Burst Process (PPBP) to model uplink traffic. This captures the "on-off" nature of mobile user activity and the long-range dependency characteristic of real-world 5G fronthaul traffic.

## V. Numerical Simulation

### A. XGS-PON Based C-RAN Simulation Module (XCRAN-SIMMODULE)
Developed using OMNeT++, the module simulates a network with 16 RRHs and 16 ONUs, testing Option 7.2 and 7.3 splits. The baseline for comparison includes gGIANT (latency focus) and Optimized RR (utilization focus). PPBP traffic is injected to simulate bursty conditions over a 10 km distance (RTT = $120\mu\text{s}$).

### B. Simulation Results
- **Mean Upstream Packet Delay:** TP-ERBU significantly outperforms competitors. For Option 7.3, it maintains the $< 300\mu\text{s}$ budget up to a traffic load factor of 0.8, compared to 0.6 for Optimized RR and 0.4 for gGIANT.
- **Packet Loss Ratio:** Reduced by up to 40% vs gGIANT and 25% vs Optimized RR due to proactive transmission of predicted traffic.
- **Throughput Analysis:** Throughput improved by up to 30% (vs gGIANT) and 15.56% (vs Optimized RR), with the most significant gains seen at high load factors where buffers are more likely to overload.
- **Jitter:** Jitter reduced by up to 21.43% compared to gGIANT, as congestion is better managed.
- **Upstream Channel Utilization:** TP-ERBU shows substantial improvement over baselines, particularly under high traffic loads.

### C. Comparison With ML-Based Methods
Comparing the moving average approach with a TensorFlow-based DL model on an NVIDIA RTX 3090 GPU, TP-ERBU achieves:
- **Prediction Time:** $0.01\text{ms}$ vs $0.15\text{ms}$ (93.33% reduction).
- **Packet Delay:** $0.25\text{ms}$ vs $0.28\text{ms}$.
- **Complexity:** Linear $O(N)$ vs Quadratic $O(N^2)$.

### D. Validity and Reproducibility
The authors provide the XCRAN-SIMMODULE source code on GitHub and document all parameters to ensure that other researchers can replicate the results.

## VI. Conclusion
TP-ERBU successfully jointly optimizes delay and throughput for 5G C-RAN fronthaul over XGS-PON by combining traffic prediction with dynamic residual bandwidth reallocation. Simulation results prove its superiority over gGIANT, Optimized RR, and ML-based methods in terms of latency, packet loss, and computational efficiency. Future work includes testing real-world deployment and adapting the algorithm for eCPRI technologies.
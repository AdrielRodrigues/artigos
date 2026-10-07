---
index_terms:
  - Elastic Optical Networks
  - Space Division Multiplexing
  - Routing and Spectrum Allocation
  - Inter-core Crosstalk
  - Spectrum Fragmentation
  - Bandwidth Blocking Probability
  - Contiguous Aligned Slot Ratio
---

# Routing and dynamic core allocation with fragmentation optimization in EON-SDM

## Abstract
The paper proposes a novel spectrum allocation technique termed **Fragmentation Coefficient and Dynamic Core-Changing-based Routing, Spectrum, and Core Allocation (FC-DCC-RSCA)** for Elastic Optical Networks employing Space Division Multiplexing (EON-SDM). The method addresses the challenges of spectrum fragmentation and inter-core crosstalk (XT) by utilizing a new fragmentation coefficient based on the **Continuous Aligned Slot Ratio (CASR)** model. By filtering paths within specific fragmentation ranges and implementing dynamic core switching when XT constraints are violated, the algorithm aims to reduce the Bandwidth Blocking Probability (BBP) and improve spectrum utilization. Simulation results show that FC-DCC-RSCA outperforms SBP-PMC and FMDE-RSCA benchmarks, specifically increasing spectrum utilization by up to 12.5% and reducing the fragmentation ratio (FR) by 13.5% at a traffic load of 450 Erlang.

## 1. Introduction
Conventional Wavelength Division Multiplexing (WDM) networks suffer from inefficient bandwidth use due to fixed 50 GHz channels. Elastic Optical Networks (EON) mitigate this by using flexible frequency slots (FS) of 12.5 GHz, allowing allocation based on actual demand. However, as single-core EONs reach their Shannon limit, Space Division Multiplexing (SDM) using multi-core fibers (MCF) is introduced to increase capacity.

A primary challenge in EON-SDM is **spectrum fragmentation**, where free slots become discontinuous, preventing the establishment of new connections despite available total capacity. The authors distinguish between link fragmentation (discontinuous segments on a single connection) and path fragmentation (failure to meet spectrum consistency across multiple links). 

The proposed FC-DCC-RSCA algorithm adheres to three fundamental RSA constraints:
1. **Spectrum Continuity:** FS must be sequentially adjacent on each link.
2. **Spectrum Consistency:** The same FS indices must be used across all links in a path.
3. **Non-overlapping Spectrum:** Assigned slots cannot overlap with existing connections.

## 2. Related Work
The authors review various RSA and Routing, Modulation, and Spectrum Allocation (RMSA) methods, noting that while some fragmentation-aware or crosstalk-aware algorithms exist (e.g., FA-RSA, CMDE-RSCA), few incorporate **dynamic core adaptability**. Most existing strategies are static or only partially assess fragmentation. The proposed FC-DCC-RSCA is distinguished from benchmarks like SBP-PMC and FMDE-RSCA by its ability to adapt cores dynamically in real-time and its comprehensive approach to managing the balance between spectrum utilization and fragmentation.

## 3. Problem Statement
The core problem is achieving an equilibrium between maximizing spectrum utilization and minimizing fragmentation while adhering to inter-core crosstalk (XT) constraints. XT is defined as interference caused by signals in adjacent cores of a multi-core fiber, which degrades signal quality if it exceeds a specific threshold ($XT_{threshold}$).

### 3.1 Network Model
The network is modeled as a connectivity graph $G(V, E, C, SS)$, where $V$ is nodes, $E$ is links, $C$ is cores per link, and $SS$ is frequency slots. A new connection request is defined by its source (S), destination (D), and requested spectrum slice (SS).

The allocation process follows three phases:
1. **Path Selection:** Utilizing the Dijkstra algorithm to find $k$-shortest paths.
2. **Core Selection:** Evaluating the Fragmentation Coefficient (FC) via CASR; only pairs within a defined range $[minFC, maxFC]$ are retained.
3. **Spectrum Slice Assignment:** Allocating slots based on XT constraints. If the XT level is too high or slots are unavailable, the algorithm triggers **dynamic core selection** to find an alternative.

The paper provides mathematical formulations for calculating the required number of spectrum slots ($\lceil N \rceil$) considering guard bands and modulation, as well as equations to determine inter-core crosstalk based on fiber properties like coupling coefficient, bend radius, and core pitch.

## 4. Fragmentation Coefficient Routing, Core and Spectrum Allocation with Dynamic Core
The FC-DCC-RSCA heuristic optimizes resource allocation through a four-step algorithmic process:

*   **Algorithm 1 (Overall Heuristic):** Orchestrates path finding $\rightarrow$ FC calculation/filtering $\rightarrow$ sorting by minimum FC $\rightarrow$ XT-constrained SS assignment.
*   **Algorithm 2 (Path Selection):** Identifies the $k$-shortest paths between source and destination.
*   **Algorithm 3 (Core Selection):** Computes $FC_{k,c}^{sd}$ using CASR for each path/core pair. It filters out pairs outside the $[minFC, maxFC]$ range and selects the pair with the lowest FC value to maximize slot contiguity.
*   **Algorithm 4 (Spectrum Allocation):** Validates that the chosen SS satisfies $XT < XT_{threshold}$. If this fails, the $(k,c)$ pair is discarded, and the system reverts to Algorithm 3 or employs dynamic core switching.

### 4.2 Time Complexity Analysis
The complexity of path calculation via Dijkstra is $O(V^2)$ (adjacency matrix) or $O((V+E)\log V)$ (binary heap). The overall worst-case time complexity is denoted as $O(M \cdot N \cdot T(S, R, C, B))$, where $M$ and $N$ are the lengths of the minFC and maxFC threshold lists, respectively.

## 5. Simulation and Analysis
### 5.1 Simulation Parameters
Simulations were conducted using **NSFNET** (14 nodes) and **USNET** (24 nodes) topologies with MATLAB. Key parameters included:
*   Traffic loads: 150–700 Gbps.
*   Cores per fiber: 6.
*   Frequency slots per link: 320.
*   XT Threshold: $-16$ dB.

Performance is measured using **Bandwidth Blocking Probability (BBP)**, **Spectrum Utilization (SU)**, and **External Fragmentation ($F_{ext}$)**. $F_{ext}$ is calculated as $1 - CASR$, where a value closer to 0 indicates lower fragmentation.

### 5.2 Simulation Results
*   **BBP and SU:** FC-DCC-RSCA consistently exhibits lower BBP and higher SU than SBP-PMC and FMDE-RSCA across both topologies. At 450 Erlang, the algorithm achieves a BBP of 0.051 in NSFNET. 
*   **Topology Comparison:** USNET generally shows lower BBP than NSFNET because its higher connectivity provides more available resource options. Conversely, SU is lower in USNET for the same number of requests because the load is spread across more links.
*   **Fragmentation Ratio (FR):** The proposed method significantly reduces FR by prioritizing contiguous blocks and using dynamic core switching to avoid fragmented slots. In NSFNET at 450 Erlang, FR was reduced by 13.5% compared to benchmarks.
*   **XT Threshold Impact:** Increasing the XT threshold allows more channels per core but yields diminishing returns after a certain point once the system reaches optimal functioning.

## 6. Conclusion and Future Work
The FC-DCC-RSCA algorithm effectively manages light path demands by integrating fragmentation coefficients and dynamic core allocation with crosstalk awareness. It demonstrates superior performance in reducing bandwidth blocking and improving spectrum efficiency compared to existing RSA methods. The authors suggest that future research should explore energy efficiency, scalability for larger networks, and the integration of machine learning for more autonomous dynamic decision-making.
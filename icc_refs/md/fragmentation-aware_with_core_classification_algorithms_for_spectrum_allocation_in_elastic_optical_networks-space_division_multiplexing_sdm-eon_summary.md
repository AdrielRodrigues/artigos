---
index_terms:
  - SDM-EON
  - Multi-Core Fiber (MCF)
  - spectrum fragmentation
  - Routing and Spectrum Assignment (RSA)
  - blocking probability
  - multipath mechanism
  - priority-based allocation
---

# Fragmentation-Aware with core classification algorithms for spectrum allocation in Elastic Optical Networks-Space Division Multiplexing (SDM-EON)

## Abstract
The paper addresses the critical issue of bandwidth fragmentation in Space Division Multiplexing Elastic Optical Networks (SDM-EON), which occurs due to the dynamic setup and release of lightpaths, thereby increasing connection blocking probability. The authors propose two heuristic fragmentation-aware algorithms—Priority Select Frequency (P-S-F) and Priority Select Core (P-S-CO)—that utilize a multipath mechanism to split bandwidth requests across multiple cores based on three priority levels (high, mid, and low). Results indicate that P-S-CO and P-S-F significantly reduce bandwidth blocking probability compared to existing methods, with P-S-CO offering the most substantial improvement.

## 1. Introduction
Elastic Optical Networks (EON) allow flexible bandwidth allocation but face challenges such as Routing and Spectrum Assignment (RSA), grooming, and fragmentation. RSA must adhere to spectrum continuity (same frequency slot number across all links in a path) and contiguity (slots must be adjacent). Space Division Multiplexing (SDM) using Multi-Core Fibers (MCF) is introduced to increase total capacity.

Fragmentation leads to bandwidth wastage and higher blocking probabilities. While multipath mechanisms—splitting connection demands into multiple routes/sizes—can mitigate fragmentation, improve fault tolerance, and reduce blocking, they introduce disadvantages such as varied end-to-end delays and an increased number of guard bands. This paper aims to reduce the blocking probability (BP) for class-based traffic in SDM-EON by combining fragmentation control with lightpath splitting via two proposed algorithms: P-S-F and P-S-CO.

## 2. Related Work
The authors review various fragmentation-aware RSA algorithms across spatial, spectral, and temporal domains. Key existing methods discussed include:
*   **Core Classification/Region Methods:** These aim to reduce fragmentation by limiting the number of slots allocated in each core or partitioning cores based on requested slot sizes (static manner).
*   **SBMC-RSCA:** An algorithm that allocates bandwidth in different cores based on prime numbers related to the size of the requested blocks. The authors note its scalability issues when the number of cores is small or required slot ranges are wide.
*   **OPT-SBMC-RSCA:** An improvement over SBMC-RSCA that uses powers of 2 instead of prime numbers to improve scalability.

The paper identifies a gap in current research regarding the combined consideration of fragmentation and lightpath splitting for class-based traffic in SDM-EON, particularly noting that existing methods like SBMC-RSCA ignore the cost implications of the required number of transmitters.

## 3. Proposed Algorithms
The proposed algorithms assume $C$ cores per link, three priority levels (1: high, 2: mid, 3: low), and a multipath mechanism. All proposed methods rely on a `FindFirstFreeGap` function, which searches for the first available sequence of contiguous frequency slots (FSs) along a route on a specific core with a complexity of $O(D \times n)$, where $D$ is network diameter and $n$ is the number of FSs.

### 3.1 Priority Select Frequency (P-S-F)
P-S-F reduces blocking probability by partitioning the frequency spectrum of *every* core into three distinct segments based on priority:
*   **Segment 1:** Dedicated to high-priority traffic.
*   **Segment 2:** Dedicated to mid-priority traffic.
*   **Segment 3:** Dedicated to low-priority traffic.

When a request arrives, the algorithm attempts to allocate the required FSs within the designated segment of the cores along $K$-shortest paths. If a single core's segment cannot accommodate the full request, the remaining demand is split and allocated in the corresponding segments of other cores. The complexity of P-S-F is $O(K \times C \times D \times n)$.

### 3.2 Priority Select Core (P-S-CO)
Unlike P-S-F, which partitions the spectrum within each core, P-S-CO partitions the *cores themselves* by priority:
*   **High-priority cores:** A specific group of cores reserved solely for high-priority requests.
*   **Mid-priority cores:** A second group reserved for mid-priority requests.
*   **Low-priority cores:** The remaining cores for low-priority requests.

Requests are split across the available spectrum blocks within their assigned core group using a multipath mechanism. This allows a connection to utilize any frequency slot within the entire spectrum of its designated cores, rather than being restricted to a spectral segment. The complexity is also $O(K \times C \times D \times n)$.

## 4. Performance Evaluation
The algorithms were tested on an NSFNET topology (14 nodes, 21 links) with 7 cores per link and 300 FSs per core. Traffic was distributed as 40% high-priority, 30% mid-priority, and 30% low-priority, with requested bandwidths between 10 and 20 FSs. Performance is measured by Blocking Probability (BP), Bandwidth Blocking Probability (BBP), and Spectrum Utilization (SU).

**Key Findings:**
*   **Overall Performance:** P-S-CO outperformed all other algorithms (including SBMC and Core-Classification) in BP, BBP, and SU. P-S-F also showed improvement over baseline methods but was less effective than P-S-CO.
*   **Blocking Probability:** P-S-CO achieved the lowest BP because partitioning at the core level allows more flexible spectrum use within those cores compared to spectral segmenting.
*   **Priority Impacts:** Low-priority traffic experienced higher BP and BBP and lower SU across both proposed algorithms because they were allocated fewer resources (fewer FSs in P-S-F and fewer cores in P-S-CO).
*   **Quantitative Gains:** Table 1 shows that P-S-CO can improve BBP by up to 25% compared to core-classification and BP by up to 11.3% compared to SBMC.

## 5. Conclusion
The paper concludes that both P-S-F and P-S-CO reduce connection blocking and increase spectrum utilization in SDM-EON. P-S-CO is the superior approach because its core-based partitioning removes the spectral constraints found in P-S-F, allowing for more efficient allocation of frequency slots. Future research will aim to integrate crosstalk limitations into these allocation models.
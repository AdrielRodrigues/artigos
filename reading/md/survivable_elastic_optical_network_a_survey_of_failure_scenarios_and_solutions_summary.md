---
index_terms:
  - Elastic Optical Networks
  - Network Survivability
  - Shared Backup Path Protection
  - Dedicated Path Protection
  - Routing and Spectrum Assignment
  - p-Cycle Protection
  - Software Defined Networking
  - Spectrum Fragmentation
---

# Survivable Elastic Optical Network: A survey of failure scenarios and solutions

## 1. Introduction
Traditional Optical Networks (TON) based on Wavelength Division Multiplexing (WDM) suffer from spectrum inefficiency due to fixed-grid frequency spacing (50 GHz or 100 GHz). Elastic Optical Networks (EON) address this by utilizing Orthogonal Frequency-Division Multiplexing (OFDM) and flex-grid technology, allowing for variable-width frequency slots (FSs) based on traffic demand and modulation formats. However, EONs face a "spectrum continuity constraint," requiring the same contiguous FSs to be used across all links in a path.

The paper identifies that while research has covered Routing and Spectrum Assignment (RSA) and centralized control, network survivability requires deeper investigation. The authors contribute a classification of failure scenarios, a survey of state-of-the-art mechanisms, a proposed hybrid protection model combining Vulnerability Scoring with traffic splitting, and an analysis of open research challenges.

## 2. State of the art of SEON
Survivability in EON is categorized into protection (pre-allocating backup resources) and restoration (dynamically calculating routes after failure). Protection offers fast failover but higher resource overhead; restoration is more resource-efficient but involves longer recovery times due to real-time path computation.

### 2.1 Dedicated path and shared backup path protection scheme
**Dedicated Path Protection (DPP)** allocates exclusive backup lightpaths for each connection. It exists in three forms: 1+1 (simultaneous transmission on both paths, instantaneous recovery), 1:1 (transmission only on working path, longer recovery), and quasi 1+1 (grouping critical paths to optimize spectrum). Partitioned DPP (PDPP) divides transmission rates into multiple disjoint paths to reduce wastage.

**Shared Backup Path Protection (SBPP)** allows multiple primary paths to share a single backup resource, provided that only one failure occurs at a time. While more complex to provision, SBPP is more spectrum-efficient than DPP. Simulation results on the USNET topology indicate that SBPP reduces blocking probability by approximately 30% compared to DPP.

### 2.2 Segmented protection and restoration schemes
This approach divides the network into smaller segments (subset of nodes and links) to localize failure impacts. A segmented protective lightpath is deployed only for a specific primary segment. This method leverages Segment Routing (SR), Multiprotocol Label Switching (MPLS), and Software-Defined Networking (SDN) via OpenFlow to manage traffic grooming and reduce service blocking ratios.

### 2.3 Path and span restoration schemes
**Path Restoration (PR)** reconstructs the entire end-to-end communication route from source to destination following a failure. **Span Restoration (SR)** only repairs the failed segment (a single connection or consecutive links between nodes), which is faster and more resource-efficient for localized failures. 

Simulation results using the USNET topology show that PR achieves a 25% lower blocking probability than SR under moderate to high traffic loads, because SR often suffers from congestion in limited alternative local routes.

### 2.4 Ring cover and p-Cycle protection schemes
**Ring Cover Protection** uses pre-deployed circular backup rings (e.g., UPSR or BLSR). It requires dual opposite fiber pairs to maintain spectrum continuity during recovery.

**p-Cycle Protection** utilizes precomputed backup paths (p-cycles) that provide higher flexibility and resource efficiency than ring covers. Constraints include a maximum cycle length (e.g., five links). Advanced variants include Failure Independent Path-Protecting (FIPP) p-cycles and Spectrum Shared p-cycles (SS-p-cycles). 

Comparative simulations on USNET topology demonstrate that p-Cycle Protection is significantly more efficient than Ring Cover, reducing blocking probability by 42%.

## 3. Different failures scenarios
Failures are hierarchically classified into single link, multi-link, node, and path failures.

### 3.1 Single and dual-link/multi-link failure scenarios
Single-link failures result from fiber cuts or device malfunctions. Multi-link (or dual-link) failures involve simultaneous disruptions across multiple fibers, increasing complexity due to the interdependencies of lost links. Mitigation strategies include Adaptive Survivability (AS) via SDN and optimized Routing, Modulation, and Spectrum Assignment (RMSA) algorithms for anycast and unicast traffic.

### 3.2 Node failure
Node failures occur when routing or forwarding hardware malfunctions. These are more severe than link failures because a single node outage disrupts all communication paths passing through it. Recovery involves rerouting traffic via alternative paths that completely bypass the failed node.

### 3.3 Path failures
Path failures occur when a total route becomes non-operational due to cascading link or node disruptions, fiber cuts, or hardware malfunctions. They are generally viewed as the result of the aforementioned component-level failures.

### 3.4 Hardware failures
Hardware failures affect critical components:
*   **ROADM:** Allows dynamic routing/swapping via software control; improved by Colorless, Directionless, and Contentionless (CDC) characteristics.
*   **WSS:** Manipulates light signals without physical port separation.
*   **SBVT (Sliceable Bandwidth Variable Transponder):** Enables adaptive modulation and supports multiple optical flows with varying data rates (10 Gb/s to 1 Tb/s).
*   **EDFA:** Amplifies optical signals using erbium-doped fiber.

Simulations show that hardware degradation (e.g., thermal stress in amplifiers) severely impacts performance; blocking probability increases from 5.7% at 125 Erlangs to 55.0% at 200 Erlangs. Node failures were found to be the most challenging recovery scenario.

## 4. Open challenges and future researches

### 4.1 Centralized network control and management
The industry is shifting from Generalized Multi-Protocol Label Switching (GMPLS) to Software-Defined Networking (SDN). SDN separates the control and data planes, allowing for global visibility and proactive fault management. Key challenges include the need for standardized protocols beyond OpenFlow that can handle elastic spectrum resources and the integration of blockchain for decentralized security and tamper-resistant logging.

### 4.2 Spectrum management
Spectrum fragmentation occurs when available slots are partitioned into non-contiguous segments due to varying channel sizes. Mitigation strategies include modulation-level aware traffic splitting and the potential use of quantum computing to solve RSA as an optimization problem, which could significantly reduce path computation time.

### 4.3 Artificial Intelligence in SEON
Machine Learning (ML), Neural Networks (NN), and Deep Reinforcement Learning (DRL) are used for proactive resource allocation, traffic prediction, and failure localization. Specifically:
*   **Supervised ML:** Estimates required spectrum slots.
*   **DRL:** Optimizes working and protection schemes dynamically.
*   **Ant Colony Optimization (ACO):** Improves spectral efficiency in SDM-EON.
*   **Failure Management:** SVMs, Naive Bayes, and Bayesian Networks are used to predict board failures or detect mechanical stress on fibers.

### 4.4 Physical layer impairments
Physical Layer Impairments (PLI), such as dispersion and nonlinear effects, degrade the Quality of Transmission (QoT). A major challenge is the discrepancy in OSNR between primary and backup routes due to different path lengths. Strategic placement of regeneration sites is necessary for long-haul links to maintain signal integrity.

### 4.5 Hardware development
Future focus areas include power efficiency and the adoption of SBVTs for adaptive bandwidth allocation. "Bandwidth squeezing" via BVTs allows the network to dynamically adjust resources based on failure severity, reducing unnecessary resource consumption.

### 4.6 Disaster management
Disaster recovery focuses on unpredictable, large-scale events (e.g., tsunamis). Because pre-allocating redundancy for all catastrophic scenarios is economically impossible, the flexibility of SBVT technology is proposed to provide adaptive communication infrastructure during emergencies.

## 5. Implementation and simulation results
The authors propose a **State-Aware Symmetrical Hybrid Protection (SHP)** scheme. This model combines symmetrical traffic splitting with an SBPP-based hybrid mechanism guided by a **Vulnerability Scoring System (VSS)**.

**VSS Methodology:**
Each link is assigned a score based on:
1.  Slot utilization ($U_{uv}$) - Weight: 0.5
2.  Historical failure count ($F_{uv}$) - Weight: 0.3
3.  Physical distance ($l_{uv}$) - Weight: 0.2

The path vulnerability is the average of its constituent links' scores. Paths with lower scores are prioritized for primary and backup selection. Traffic is split symmetrically across link-disjoint primaries to balance load and delay congestion. If a shared backup becomes unreliable or congested, it is dynamically reassigned. To handle contiguity constraints, the system performs global re-optimization (repacking existing allocations) during admission if necessary.

**Comparative Results:**
SHP was compared against Partitioned DPP (PDPPS). Unlike PDPPS, which uses rigid spectrum partitions and "squeezed" restoration (dropping part of the traffic), SHP leverages SBPP and VSS for dynamic, full-capacity recovery. 
*   **Blocking Probability:** SHP reduced blocking probability by 97% on USNET and 80% on NSFNET compared to PDPPS.
*   **Spectrum Utilization:** Increased by 29% (USNET) and 40% (NSFNET).
*   **Traffic Loss:** Decreased by 44% (USNET) and 90% (NSFNET).

## 6. Conclusion
The paper concludes that while traditional protection schemes provide baseline survivability, the future of SEON lies in intelligent, adaptive architectures. Key drivers for this evolution include BVTs, traffic splitting, VSS-based routing, and emerging technologies such as Space Division Multiplexing (SDM) and quantum computing to meet next-generation data demands.
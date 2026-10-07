---
index_terms:
  - network slicing
  - CF-RAN over WDM
  - URLLC
  - eMBB
  - mMTC
  - TAB-FAA algorithm
  - functional splits
---

# Traffic-Aware Network Slicing for 5G Networks in Cloud Fog-RAN over WDM Architecture

## I. Introduction
The paper addresses the challenge of supporting heterogeneous 5G services—Ultra-Reliable Low-Latency Communication (URLLC), Enhanced Mobile Broadband (eMBB), and Massive Machine Type Communication (mMTC)—which have divergent demands for data rate, latency, and reliability. While network slicing via Network Function Virtualization (NFV) allows multiple virtual networks to share physical infrastructure, existing Cloud RAN (C-RAN) architectures face scalability issues, and RU-DU-CU architectures struggle to adapt to random traffic variations due to the centralization of functions in Central Offices (COs).

The authors propose a three-layer Cloud Fog Radio Access Network (CF-RAN) over Wavelength Division Multiplexing (WDM) architecture. This structure consists of:
1. **Layer 1:** Remote Radio Heads (RRHs).
2. **Layer 2:** Fog nodes, positioned closer to RRHs to process delay-sensitive URLLC requests.
3. **Layer 3:** BBU hotels, which handle eMBB and mMTC requests.

By utilizing split option 7.2 for fronthaul transport (via eCPRI), the architecture reduces data rate requirements compared to traditional C-RAN's split option 8.

### A. Literature Review
The authors note that while prior research has focused on VNF placement, resource allocation and cost minimization in C-RAN or RU-DU-CU architectures, there is a gap in understanding how random traffic variations affect network slicing performance within a CF-RAN over WDM framework.

### B. Motivation & Contributions
The primary goal is to evaluate the impact of stochastic incoming slice requests on overall network performance. The core contributions are:
*   An investigation into the effects of random URLLC, eMBB, and mMTC traffic behavior.
*   The development of a heuristic algorithm designed to maximize request fulfillment while minimizing the activation of fog nodes and BBU hotels, subject to capacity and latency constraints, including Grooming Routing and Wavelength Assignment (GRWA).

### C. Paper Organization
This section outlines the structure of the remaining paper: Section II details architecture and traffic; Section III explains the heuristic algorithm; Section IV presents results; and Section V provides the conclusion.

## II. Network Architecture
The proposed 3-layer CF-RAN over WDM connects Cell Sites (CSs), fog nodes, BBU hotels, and a core CO via optical fiber. To maintain slice isolation, distinct wavelengths are assigned to specific service types. Processing is distributed based on request type: URLLC is handled at the fog layer, while eMBB and mMTC are processed at the BBU hotel layer.

### A. Traffic Types
The paper defines three traffic types with strict isolation rules (only identical types share lightpaths):
*   **Type 1 (URLLC):** Fronthaul traffic flows from RRHs to fog nodes; backhaul flows from fog nodes to the core CO (passing through BBU hotels without processing).
*   **Type 2 (eMBB) and Type 3 (mMTC):** Fronthaul traffic bypasses fog nodes via Reconfigurable Optical Add-Drop Multiplexers (ROADMs) to be processed at BBU hotels; backhaul flows from BBU hotels to the core CO.

### B. Functional Splits
The authors analyze 3GPP functional splits, which determine the division of tasks between the RRH and centralized units. They reject split option 8 due to excessive fronthaul data-rate requirements and instead adopt **split option 7**. This option provides a balance between centralization gains and manageable data rates for transport between RRHs and fog nodes/BBU hotels. The architecture avoids "midhaul" traffic (typical of RU-DU-CU) because processing is completed entirely at the fog node or BBU hotel levels.

## III. Traffic Aware Joint BBU Hotel and Fog Node Activation Algorithm (TAB-FAA)
The TAB-FAA heuristic algorithm aims to minimize active hardware while maximizing connectivity. It handles requests as follows:

**For Type 1 (URLLC):**
1.  The algorithm first checks reachable COs with existing BBU hotels. If the path delay ($Q$) is within the maximum allowable limit ($D_t$) and link capacity is available, the request is routed to the core.
2.  If no active BBU hotel can serve it, the algorithm attempts to activate the fog node associated with the source RRH, provided there is sufficient fronthaul/backhaul capacity.
3.  If neither option is viable, the request is blocked.

**For Type 2 (eMBB) and Type 3 (mMTC):**
1.  If the source is not already linked to an active BBU hotel, the algorithm uses Dijkstra's algorithm to find the shortest path to a reachable CO. If latency and capacity constraints are met, it activates a BBU in that CO and routes the request.
2.  If the source is already associated with an active BBU hotel, the algorithm checks for residual link capacity; if sufficient, the request is routed; otherwise, it is blocked.

## IV. Results & Discussions
The researchers simulated a 100-node network (50 CSs, 30 fog nodes, 20 COs) over $200\text{km}^2$ using Matlab and Monte Carlo simulations. Each fiber supports eight 40 Gbps wavelengths, partitioned as: four for eMBB and two each for URLLC and mMTC.

**Traffic Constraints:**
*   **URLLC (Type 1):** Fronthaul $50\text{--}80$ Mbps; latency $\leq 50\mu\text{s}$.
*   **eMBB (Type 2):** Fronthaul $240\text{--}360$ Mbps; latency $\leq 100\mu\text{s}$.
*   **mMTC (Type 3):** Fronthaul $50\text{--}80$ Mbps; latency $\leq 250\mu\text{s}$.

**Key Findings:**
*   **Active Node Count:** An increase in URLLC requests directly increases fog node activation and decreases BBU hotel activation. High eMBB traffic significantly increases the number of required active BBU hotels due to high bandwidth demands. Conversely, a higher proportion of mMTC requests reduces the total number of active nodes because it is the least resource-intensive service.
*   **Served Requests:** The percentage of served requests is highest when Type 3 (mMTC) traffic dominates. It decreases when Type 2 (eMBB) increases due to bandwidth saturation, or when Type 1 (URLLC) becomes excessively high due to stringent latency constraints that fog nodes may eventually fail to meet.
*   **Fronthaul Delay:** Total delay for a specific service type increases as the proportion of that traffic type in the mix increases, indicating resource contention within its dedicated slice.

## V. Conclusion
The paper demonstrates that a 3-layer CF-RAN over WDM architecture can effectively implement network slicing by dynamically distributing processing between fog nodes and BBU hotels. The TAB-FAA algorithm successfully optimizes resource utilization—activating only necessary nodes—while adhering to strict latency and capacity constraints. The results highlight that the ability to adapt to random variations in service request ratios is critical for 5G performance, particularly in managing the tension between the low-latency needs of URLLC and the high-bandwidth needs of eMBB.
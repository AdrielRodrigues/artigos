---
index_terms:
  - Cloud Fog RAN
  - network slicing
  - WDM networks
  - URLLC eMBB mMTC
  - functional split
  - Integer Linear Programming
---

# Efficient Network Slicing for 5G Services in Cloud Fog-RAN Deployment Over WDM Network

## I. Introduction
The paper addresses the challenge of managing diverse 5G traffic with stringent Quality of Service (QoS) requirements. It focuses on three standardized 3GPP slice types: Ultra-Reliable Low-Latency Communication (URLLC), Enhanced Mobile Broadband (eMBB), and Massive Machine Type Communication (mMTC). While Cloud RAN (C-RAN) improves resource utilization by separating Remote Radio Heads (RRH) from Baseband Units (BBU), it suffers from scalability issues, high fronthaul capacity demands for eMBB, and an inability to meet the sub-1ms latency requirements of URLLC.

The authors propose a Cloud Fog RAN (CF-RAN) over Wavelength Division Multiplexing (WDM) architecture consisting of three layers: RRH at layer 1, fog nodes at layer 2, and BBU hotels at layer 3. In this model, time-sensitive URLLC requests are processed at fog nodes located closer to the cell sites, while eMBB and mMTC requests are handled by centralized BBUs. The architecture utilizes the eCPRI protocol (Split Option 7) for fronthaul traffic to reduce bandwidth requirements compared to the standard CPRI protocol.

### A. Related Work
The authors review existing literature on C-RAN and RU-DU-CU architectures, noting that while throughput and energy efficiency have been studied, there is a gap in research concerning network slicing within CF-RAN over WDM specifically regarding slice isolation and the joint optimization of grooming, routing, and wavelength assignment (TGRWA).

### B. Motivation and Contributions
The primary goal is to resolve the tension between URLLC latency needs and eMBB bandwidth demands. The main contributions include:
1. A proposed 3-layer CF-RAN over WDM architecture that uses fog nodes for URLLC processing and eCPRI functional splits.
2. An Integer Linear Programming (ILP) mathematical model to minimize the activation of BBU hotels and fog nodes.
3. Integration of constraints regarding network capacity, fronthaul latency, and isolation-aware routing.
4. A low-complexity greedy heuristic algorithm for practical deployment in large networks.

### C. Paper Organization
The document is structured to describe the architecture (Section II), the system model/problem formulation (Section III), the heuristic algorithm (Section IV), simulation results (Section V), and conclusions (Section VI).

## II. Network Architecture
The CF-RAN over WDM hierarchy flows from Cell Sites (CS) $\to$ Fog Nodes $\to$ BBU Hotels $\to$ Core Central Office (CO). To ensure slice isolation, each service type is assigned a specific wavelength; only traffic of the same service type can be groomed into shared lightpaths.

### A. Network Slicing
Three logical networks are created over the physical infrastructure via Network Function Virtualization (NFV): URLLC (Type 1), eMBB (Type 2), and mMTC (Type 3).

### B. Functional Split
The architecture employs 3GPP Split Option 7 (eCPRI) for fronthaul traffic, which is more bandwidth-efficient than the packet-intensive CPRI (Option 8). Reconfigurable Optical Add-Drop Multiplexers (ROADMs) at fog nodes allow Type 2 and Type 3 traffic to pass through without processing. Consequently:
- **Type 1 (URLLC):** Fronthaul $\to$ Fog Node (Processing) $\to$ Backhaul $\to$ Core CO.
- **Type 2 & 3 (eMBB/mMTC):** Fronthaul $\to$ BBU Hotel (Processing) $\to$ Backhaul $\to$ Core CO.

## III. System Model and Problem Formulation
The system models a WDM network where nodes are partitioned into CSs, fog nodes, and COs. Routing is based on pre-computed paths forming virtual links. Total path delay includes propagation, transmission, interface (due to split point), and electronic switch delays.

### A. Inputs
Key inputs include sets of nodes ($\mathbb{N}$), computed routed paths ($\mathbb{P}$), virtual links ($\mathbb{V}$), requests ($\mathbb{R}$), wavelengths ($\mathbb{W}$), and capacity constraints ($C$). Latency thresholds $D_t$ are defined per request type.

### B. Outputs
The model outputs binary vectors for BBU hotel activation ($\mathbf{b}$) and fog node activation ($\mathbf{x}$), association matrices between RRHs and fog nodes/BBUs, routing indicators for fronthaul and backhaul requests, lightpath counts per wavelength, and the number of fibers deployed per link.

### C. Constraints
1. **Association:** Every RRH must connect to exactly one fog node and one BBU hotel.
2. **Activation:** A node can only serve an RRH if it is active.
3. **Fiber Deployment:** The number of fibers on any link cannot exceed $K$.
4. **Capacity:** The sum of traffic in fronthaul and backhaul requests must not exceed the available wavelength capacity of the virtual links.
5. **Latency:** Total fronthaul delay (propagation + electronic switch + interface + transmission) must be $\le D_t$ for all request types.
6. **Routing Flow:** Constraints ensure URLLC traffic terminates at fog nodes, while eMBB/mMTC traffic terminates at BBU hotels, with subsequent backhaul routing to the core CO.

### D. Objective Function
The objective is to minimize total network cost $\mathcal{Z}$, defined as a weighted sum of active BBU hotels and active fog nodes: $\mathcal{Z} = \alpha \sum \mathbf{b}_i + (1 - \alpha) \sum \mathbf{x}_f$, where $\alpha$ represents the relative weight between the two node types.

### E. Optimization Problem
The problem is formulated as a minimization of $\mathcal{Z}$ subject to constraints (1)-(10). Because this is NP-hard, the authors propose a heuristic algorithm for larger scales.

## IV. Proposed Heuristic Service Aware BBU Hotel and Fog Node Activation Algorithm (SB-FAA)
The SB-FAA is a greedy algorithm that prioritizes minimizing active nodes while reducing request blockage. 
- **For eMBB/mMTC:** It checks if the source RRH is already associated with an active BBU; if not, it searches for reachable COs that satisfy delay and capacity constraints, activating a BBU hotel if necessary.
- **For URLLC:** It first attempts to route through already active COs (if latency permits); otherwise, it checks for available fog nodes near the RRH that can be activated to handle the request.

### A. Computational Complexity
The complexity is analyzed in FLOPS and found to be approximately $O(R \cdot \max\{(10 N^2)B, 8B + 7F\})$, where $R$ is requests, $N$ nodes, $B$ BBU hotels, and $F$ fog nodes. This is significantly more efficient than an exhaustive search.

## V. Results & Discussions
Simulations were performed using AMPL+CPLEX for the ILP model and Python/Networkx for the heuristic.

### A. Simulation Parameters
The test network consists of 30 nodes (13 CS, 7 CO, 10 Fog) over $150\text{ km}^2$. Fiber capacity is 8 wavelengths at 10 Gbps per fiber ($K=1$). Wavelengths are split: 4 for eMBB, 2 for URLLC, and 2 for mMTC.

### B. Simulation Results (ILP)
The 3-layer architecture significantly reduces the number of active nodes for URLLC requests compared to a 2-layer approach. It also provides a 10% improvement in fronthaul delay for URLLC traffic. The 2-layer architecture fails to find feasible solutions under high traffic loads where CF-RAN remains viable.

### C. Performance Evaluation of Proposed SB-FAA
Using a larger network (140 nodes, 5k requests), results show:
- **Fronthaul Delay:** Similar performance for eMBB/mMTC across architectures, but significant gains for URLLC in the 3-layer setup.
- **Active Nodes:** A 33% reduction in active nodes for URLLC traffic compared to 2-layer C-RAN.
- **Connectivity:** The CF-RAN provides up to 20% higher request service rates with fewer active BBU hotels.

### D. Comparison Between ILP and SB-FAA
The heuristic (SB-FAA) performs near-optimally when compared to the Branch & Bound (B&B) algorithm, validating its use for larger networks.

### E. Comparison of Results With Different Optimization Objective
Varying $\alpha$ shifts the priority: lower $\alpha$ prioritizes fewer fog nodes, while higher $\alpha$ prioritizes fewer BBU hotels. Most results use $\alpha=0.5$ to balance cost across both node types.

### F. Convergence Analysis
Convergence is measured by the ratio $c = \frac{\text{active nodes}}{\text{requests served}}$. As the request index increases, the value of $c$ drops sharply, indicating that the algorithm efficiently serves a high percentage of requests with a minimal increase in active nodes.

## VI. Conclusion
The proposed CF-RAN over WDM architecture effectively balances the conflicting needs of 5G services by distributing processing between fog nodes (for URLLC) and BBU hotels (for eMBB/mMTC). The ILP model and SB-FAA heuristic provide a framework to minimize deployment costs while ensuring QoS. Results demonstrate improved hotel centralization, lower fronthaul latency, and higher overall connectivity compared to traditional 2-layer C-RAN. Future work includes integrating an SDN controller and optimizing the weight $\alpha$.
---
index_terms:
  - Cloud Fog-RAN
  - network slicing
  - WDM networks
  - 5G services
  - URLLC
  - BBU placement
  - functional split
---

# Efficient Network Slicing for 5G Services in Cloud Fog-RAN Deployment Over WDM Network

## I. Introduction
The paper addresses the challenge of supporting diverse 5G service requirements—Ultra-Reliable Low-Latency Communication (URLLC), enhanced Mobile Broadband (eMBB), and massive Machine Type Communication (mMTC)—within a single radio access network (RAN) infrastructure. While Cloud RAN (C-RAN) improves resource utilization by centralizing Baseband Units (BBUs) in "hotels," it struggles with the extreme latency demands of URLLC and the high fronthaul bandwidth requirements of eMBB due to its two-layer structure and reliance on data-intensive protocols like CPRI.

To solve this, the authors propose a Cloud Fog RAN (CF-RAN) over Wavelength Division Multiplexing (WDM). This 3-layer architecture introduces fog nodes between the Remote Radio Heads (RRHs) at cell sites (CSs) and the BBU hotels at central offices (COs). By utilizing Network Function Virtualization (NFV) to place limited processing power at fog nodes closer to the user, URLLC latency is reduced. Additionally, the architecture employs the eCPRI protocol (split option 7), which reduces fronthaul bandwidth pressure compared to traditional CPRI (split option 8).

### A. Related Work
The authors survey existing research on C-RAN and RU-DU-CU architectures, noting that while many studies focus on resource allocation or energy efficiency in standard C-RAN, there is a gap in research regarding network slicing within CF-RAN over WDM that simultaneously ensures slice isolation and optimizes routing and wavelength assignment.

### B. Motivation and Contributions
The primary motivation is to bridge the knowledge gap in applying RAN slicing to a 3-layer CF-RAN over WDM. The main contributions are:
1. A novel 3-layer architecture that separates traffic processing based on service type (URLLC at fog nodes; eMBB/mMTC at BBU hotels).
2. An Integer Linear Programming (ILP) model to minimize the number of active BBU hotels and fog nodes, thereby reducing deployment costs.
3. Inclusion of practical constraints: node activation, fronthaul latency, network capacity, and isolation-aware wavelength assignment.
4. A low-complexity greedy heuristic algorithm (SB-FAA) for solving the NP-hard optimization problem in large networks.

### C. Paper Organization
The paper is structured to cover architecture (Section II), the mathematical system model (Section III), the proposed heuristic algorithm (Section IV), simulation results (Section V), and final conclusions (Section VI).

## II. Network Architecture
The CF-RAN over WDM consists of four tiers: Cell Sites (CSs), Fog Nodes, BBU Hotels, and a Core Central Office (CO). Optical fiber links connect these nodes using WDM. To ensure slice isolation—crucial for multi-tenancy and security—distinct wavelengths are assigned to each slice type, preventing different service types from sharing lightpaths.

### A. Network Slicing
The authors implement three logical slices over the physical infrastructure: Type 1 (URLLC), Type 2 (eMBB), and Type 3 (mMTC). Resources are allocated according to the specific requirements of each slice.

### B. Functional Split
The architecture adopts a functional split strategy to optimize traffic flow:
* **Fronthaul:** Uses the eCPRI protocol (Split Option 7) for reduced bandwidth requirements. For URLLC, fronthaul connects RRHs to fog nodes. For eMBB/mMTC, fronthaul connects RRHs directly to BBU hotels, bypassing fog node processing via Reconfigurable Optical Add-Drop Multiplexers (ROADMs).
* **Backhaul:** Connects fog nodes (for URLLC) and BBU hotels (for all types) to the core CO.

## III. System Model and Problem Formulation
The system is modeled as an offline optimization problem for planning optical network deployment. The objective is to minimize a weighted cost function based on the activation of BBU hotels and fog nodes.

### A. Inputs
Inputs include the set of nodes ($\mathbb{N}$), pre-computed routed paths ($\mathbb{P}$), virtual links, physical fiber limits ($K$ fibers per link), request types ($\mathbb{T}$), wavelength capacities ($C$), and maximum allowable fronthaul latencies ($D_t$). The delay model incorporates propagation, transmission, interface (split point), and electronic switch delays.

### B. Outputs
The decision variables include:
* Binary vectors for BBU hotel ($\mathbf{b}$) and fog node ($\mathbf{x}$) activation.
* Association matrices linking CSs to either fog nodes ($\bar{\mathbf{F}}$) or BBU hotels ($\mathbf{Z}$).
* Routing indicators for backhaul ($\mathbf{Y}$) and fronthaul ($\bar{\mathbf{Y}}$) requests.
* Integer variables for lightpath count per wavelength ($\mathbf{U}$) and fiber deployment per link ($\mathbf{o}$).

### C. Constraints
The model is governed by ten constraints:
1. **Association:** Each RRH must connect to exactly one fog node and one BBU hotel.
2. **Activation:** Fog nodes and BBU hotels can only serve requests if they are active.
3. **Capacity:** Total requests on a path cannot exceed the capacity of deployed fibers/wavelengths; fiber count per link is capped at $K$.
4. **Latency:** Total fronthaul delay (propagation + transmission + interface + switch) must be $\leq D_t$ for each request type.
5. **Routing Logic:** Backhaul requests must originate from the processing node (fog or BBU) and end at the core CO; fronthaul requests must start at RRHs and terminate at their respective processing nodes.

### D. Objective Function
The cost function minimizes $\mathcal{Z} = \alpha \sum \mathbf{b}_i + (1 - \alpha) \sum \mathbf{x}_f$, where $\alpha$ is a weight balancing the importance of minimizing BBU hotels versus fog nodes.

### E. Optimization Problem
The problem (OP1) is identified as NP-hard, necessitating the development of a heuristic for larger network scales where exhaustive solvers (like Branch & Bound) are computationally prohibitive.

## IV. Proposed Heuristic SB-FAA Algorithm
The Service Aware BBU Hotel and Fog Node Activation (SB-FAA) algorithm uses a greedy approach to achieve near-optimal solutions.

**Mechanism:**
1. For eMBB/mMTC requests, the algorithm first checks if the source is already associated with an active BBU hotel. If not, it searches for the shortest path to a reachable CO that satisfies latency and capacity constraints; if found, it activates a BBU hotel there.
2. For URLLC requests, the algorithm attempts to use existing active COs first. If no active CO meets the strict latency requirement, it activates a fog node connected to the source RRH, provided capacity is available.
3. Routing and wavelength assignment are performed based on these associations.

### A. Computational Complexity
The complexity is analyzed in FLOPS. The worst-case complexity is approximately $R(\max\{(10 N^2)B, 8B + 7F\})$, where $R$ is the number of requests, $N$ total nodes, $B$ BBU hotels, and $F$ fog nodes. This is significantly lower than exhaustive search methods.

## V. Results & Discussions
Simulations were conducted using AMPL+CPLEX for ILP and Python (Networkx) for the heuristic.

### A. Simulation Parameters
A 30-node scenario (13 CS, 7 CO, 10 Fog) was used for ILP, while a larger 140-node scenario was used for SB-FAA. Wavelengths were distributed unevenly: more wavelengths for eMBB due to higher bandwidth needs. Latency bounds were set strictest for URLLC ($\leq 50\mu s$ fronthaul).

### B. Simulation Results (ILP)
The 3-layer architecture showed a significant reduction in active nodes and a 10% improvement in total fronthaul delay for URLLC compared to the 2-layer C-RAN. The 2-layer approach failed to find feasible solutions under high traffic loads due to latency violations.

### C. Performance Evaluation of SB-FAA
In larger networks, CF-RAN provided up to a 33% reduction in active nodes for URLLC and significantly higher network connectivity (up to 20% more requests served) than the 2-layer approach using the same number of BBU hotels.

### D. Comparison Between ILP and SB-FAA
SB-FAA's results were compared against a Branch & Bound optimal solver. The heuristic provided near-optimal performance, especially for mMTC traffic, confirming its viability for large networks.

### E. Comparison of Results With Different Optimization Objective
Varying $\alpha$ shifted the activation patterns: low $\alpha$ prioritized minimizing fog nodes (increasing BBU activations), while high $\alpha$ prioritized minimizing BBU hotels (increasing fog node activations).

### F. Convergence Analysis
Convergence was measured by the ratio of active nodes to served requests ($c = a/b$). As the number of requests increases, $c$ drops sharply and stabilizes, indicating that the network efficiently services more users without needing proportional increases in active hardware.

## VI. Conclusion
The proposed CF-RAN over WDM architecture effectively manages the conflicting requirements of 5G slices by distributing processing across three layers. By processing URLLC at fog nodes and eMBB/mMTC at BBU hotels, the authors achieved a reduction in deployment costs (fewer active BBU hotels), improved fronthaul latency, and increased network connectivity compared to traditional C-RAN. Future work includes integrating an SDN controller and optimizing the weight $\alpha$.
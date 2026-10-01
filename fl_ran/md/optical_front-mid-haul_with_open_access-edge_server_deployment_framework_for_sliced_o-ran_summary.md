---
index_terms:
  - Open-RAN (O-RAN)
  - TWDM-PON
  - Network Slicing
  - Integer Linear Programming
  - Front-haul and Mid-haul
  - DU and CU Placement
---

# Optical Front/Mid-Haul With Open Access-Edge Server Deployment Framework for Sliced O-RAN

## Abstract
The paper proposes a framework for the optimal deployment of Radio Units (RUs) and their connection to open access-edge servers hosting Distributed Units (DUs) and Centralized Units (CUs) in an Open-RAN (O-RAN) architecture. To ensure cost-efficiency and meet diverse Quality of Service (QoS) requirements for uRLLC, eMBB, and mMTC slices, the authors employ Time-Wavelength Division Multiplexed Passive Optical Networks (TWDM-PON). The framework uses a two-stage integer programming problem and corresponding heuristics to optimize RU association and DU/CU placement, demonstrating superior cost-efficiency over Optical Transport Network (OTN) frameworks across urban, rural, and industrial scenarios.

## I. Introduction
5G networks must support diverse services: ultra-reliable low-latency communication (uRLLC), enhanced mobile broadband (eMBB), and massive machine type communication (mMTC). While Cloud-RAN (C-RAN) provided initial centralization, O-RAN advances this by disaggregating baseband processing into virtualized RUs, DUs, and CUs on commercial off-the-shelf (COTS) hardware. 

A major challenge is the high capacity and low latency required for front-haul interfaces (RU-DU). The authors argue that TWDM-PON is a superior candidate compared to OTN due to cost efficiency, ubiquity in FTTx deployments, and scalability. They further introduce "access-edge clouds" to democratize the network edge, allowing DUs and CUs to be hosted on shared servers. By utilizing network slicing via software-defined everything (SDx) and network function virtualization (NFV), resources can be customized for each service type. The paper specifically aims to optimize RU locations and their connectivity to access-edge servers to minimize total deployment costs while satisfying strict latency constraints.

## II. Review of Related Works
The authors review cell planning methods and functional split options in O-RAN, noting that existing frameworks often overlook the specific benefits of TWDM-PON for flexible DU/CU placement. They discuss existing Dynamic Bandwidth Allocation (DBA) algorithms, mentioning a cooperative mobile-DBA (M-DBA) that reduces uplink waiting times to meet front-haul latency requirements. While previous research has explored RAN slicing and OTN-based RU-DU-CU placement, the authors identify a gap in investigating TWDM-PON-based front/mid-haul interfaces integrated with open access-edge servers for sliced O-RAN.

## III. Open Access-Edge Cloud Network Design With TWDM-PON-Based Front/Mid-Haul

### A. TWDM-PON-Based Front/Mid-Haul Network Architecture
The proposed architecture connects RUs to Optical Line Terminals (OLTs) via Optical Network Units (ONUs) using TWDM-PONs. The system supports flexible functional splits: split-7.2 for RU-DU (front-haul) and split-2 for DU-CU (mid-haul). 
- **Deployment Options:** DUs can be placed at the RU location (for extreme low latency, e.g., uRLLC), at the Stage-I OLT location, or aggregated in larger edge cloud servers. CUs are typically hosted at Stage-I or Stage-II OLT locations.
- **Hierarchical Structure:** To balance cost and latency, a two-stage TWDM-PON approach is used. Stage-I handles front-haul/mid-haul for some slices, while Stage-II aggregates traffic from multiple Stage-I OLTs to reach higher-level CUs or edge clouds, which is particularly efficient for less latency-sensitive mMTC applications.

### B. Novel Scheduling Techniques for Ensuring Low-Latency
To support uRLLC, the authors leverage 5G New Radio (NR) techniques such as mini-slots and grant-free uplink transmission. To address PON upstream latency, a cooperative M-DBA is employed. In this scheme, the DU predicts future traffic loads based on UE scheduling requests and informs the OLT in advance, allowing the OLT to generate bandwidth maps that minimize RU-to-DU waiting times.

### C. Communication and RU-DU-CU Processing Models
The paper defines mathematical models for throughput and computational effort:
- **Throughput:** Maximum RU throughput is calculated based on MIMO layers, modulation order, and numerology. UE throughput considers transmit power and path loss (distinct models for macro and small cells).
- **Computation:** Total BBU processing effort ($C_{BBU}$) is measured in Giga Operations Per Second (GOPS) per Transmission Time Interval (TTI), based on antennas, modulation bits, and coding rates. 
- **Split Distribution:** For the chosen splits, computational load is distributed as 40% at the RU, 50% at the DU, and 10% at the CU.

### D. Optimal TWDM-PON-Based Front/Mid-Haul Design
The design objective is to minimize the number of RUs, OLTs, and access-edge servers (and thus total cost) while satisfying end-to-end latency bounds for uRLLC, eMBB, and mMTC. This is framed as a two-stage problem: first, associating UEs with optimal RU locations; second, optimally connecting those RUs to OLTs and placing DU/CU functions in servers.

## IV. Optimization Problem Formulations

### A. Mobile User Equipment and RU Association Problem ($\mathcal{P}_1$)
The first ILP seeks to minimize the number of installed RUs and total over-the-air (OTA) latency. Constraints include:
1. **Coverage:** UEs must be within a maximum allowable distance from an RU.
2. **Association:** Each UE connects to exactly one active RU.
3. **Latency/Throughput:** The sum of propagation and transmission latencies must not exceed the slice-specific OTA latency bound ($\Delta_s^{OTA}$).

### B. Lagrangian Relaxation Heuristic for UE-RU Association
Because $\mathcal{P}_1$ is NP-hard, a Lagrangian relaxation heuristic is used. It relaxes the "one RU per UE" constraint to find a lower bound (LB) on the cost. A separate heuristic then searches for a feasible upper bound (UB). The sub-gradient method iteratively adjusts Lagrange multipliers until the LB and UB converge or a maximum iteration count is reached, ensuring near-optimal solutions with an analyzed optimality gap.

### C. DU-CU Placement and Front/Mid-Haul Design Problem ($\mathcal{P}_2$)
The second ILP minimizes the total installation cost (OLTs, fiber, and processors). 
- **Constraints:** Fiber lengths must stay within TWDM-PON limits (~20 km), and each RU must connect to one Stage-I OLT. 
- **Placement Flexibility:** DUs can be placed at RUs or Stage-I OLTs; CUs can be at Stage-I or Stage-II OLTs.
- **Latency Requirements:** The model incorporates constraints for communication latency (propagation and transmission) and processing latency (computational load vs. available GOPS in servers). 

### D. Heuristic for Front/Mid-Haul and DU-CU Deployment
A greedy heuristic is proposed to solve $\mathcal{P}_2$. It iteratively activates OLTs and associates RUs based on minimum distance while verifying that all latency constraints (communication and processing) are met. It compares the cost of placing DUs at RU locations versus OLT locations, selecting the cheaper option. The authors provide a theorem proving the heuristic provides an $O(\log_e(O \times \sum B_s))$ approximation to the optimal solution.

## V. Results and Discussion
The framework is evaluated across industrial (high density), urban, and rural (sparse) scenarios with tidal wave traffic patterns.

- **RU Association ($\mathcal{P}_1$):** Results show that eMBB requires the most RUs due to high throughput demands. The Lagrangian heuristic (LgR) produces results very close to the IBM Gurobi optimal solver but is significantly faster for large datasets.
- **Latency Analysis:** All latency bounds for front-haul, mid-haul, and BBU processing are satisfied across all scenarios. Uplink latencies are slightly higher than downlink due to PON waiting times.
- **Cost Optimization:** 
    - A double-stage TWDM-PON architecture is more cost-efficient than a single-stage one when server capacities are limited, as it allows for better aggregation of CU functions. Increasing the Stage-II data rate further reduces costs up to a point ($N=3$).
    - **Comparison with OTN:** The TWDM-PON framework is significantly cheaper (21%–28% saving) than mesh-based OTN frameworks. This is attributed to the tree-and-branch architecture of PONs requiring fewer fiber links and nodes compared to the complex ROADM/E-switch requirements of a mesh OTN.

## VI. Conclusion
The authors successfully developed a framework for planning sliced O-RAN front/mid-haul networks using TWDM-PON and open access-edge servers. By utilizing a two-stage ILP and efficient heuristics, they optimize RU placement and server deployment. The results demonstrate that the proposed architecture not only meets the stringent QoS requirements of diverse 5G slices but also offers substantial cost reductions over traditional OTN-based next-generation front-haul interfaces.
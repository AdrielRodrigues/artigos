---
index_terms:
  - Cell-Free Massive MIMO
  - O-RAN Architecture
  - Fixed-Mobile Convergence
  - XGS-PON
  - Q-Learning
  - 6G Networks
  - Spectral Efficiency
---

# Machine Learning-Based Cell-Free Support in the O-RAN Architecture: An Innovative Converged Optical-Wireless Solution toward 6G Networks

## Abstract
The paper proposes a converged optical-wireless network architecture designed for 6G to support high-demand use cases (e.g., holographic telepresence, Industry 4.0) with near-zero latency. The solution integrates the distributed Cell-Free (CF) networking concept and a serial fronthaul approach into the O-RAN framework. It enables Fixed-Mobile Convergence (FMC) by sharing edge and midhaul infrastructure between mobile and fixed services. Key enablers include modifications to O-RAN interfaces for CF support and the implementation of Machine Learning (ML) at the radio edge.

## Introduction
Future 6G networks must achieve "omnipresence" and "omniscience," supporting massive device density (10 million devices/km²) while reducing CO2 emissions through energy efficiency. To meet these goals, the authors argue for a unified hierarchical infrastructure that pools communication, computation, and storage resources. 

The proposed architecture utilizes a converged optical-wireless X-haul. Specifically:
- **Radio Edge:** Radio Units (RUs) are connected to CF Distribution Units (DUs) via a bus configuration ("Radio Stripes").
- **Backhauling:** 10-Gigabit-Symmetrical Passive Optical Network (XGS-PON) is used to support dense RU deployments.
- **O-RAN Alignment:** The system adopts the 3GPP Next-Generation Radio Access Network (NG-RAN) disaggregation, splitting the gNB into Centralized Unit Control Plane (CU-CP), CU-User Plane (CU-UP), and DU nodes.
- **Innovation:** The authors extend O-RAN by integrating CF high-PHY functions (modulation/precoding) within the virtualized O-RAN Distribution Unit (vO-DU).

## The Cell-Free Networking Approach
Cell-Free (CF) networking eliminates traditional cell boundaries by serving single-antenna User Equipments (UEs) via a large number of distributed Access Points (APs) managed by a central processing pool. This removes "cell-edge" problems and improves energy efficiency and coverage.

The concept has evolved from all APs serving all UEs to a **user-centric** approach, where only a dynamic cluster of APs serves each UE based on channel quality and distance. The paper identifies two primary challenges in this paradigm:
1. **Coordination:** High Spectral Efficiency (SE) requires significant information sharing (e.g., Channel State Information), but full centralization is not scalable due to fronthaul bandwidth constraints.
2. **Scalability Solutions:** "Radio Stripes" and "Radio Weaves" are mentioned as methods to use sequential processing at the AP level to reduce CPU load.

The authors suggest that CF networks must align with Open RAN to provide the flexibility needed for dynamic resource distribution and inter-CPU coordination.

## Design of Cell-Free Based Fronthaul In-Line with the O-RAN Alliance
The proposed architecture replaces traditional C-RAN (which often lacks the bandwidth/flexibility for 5G/6G) with a two-tier distributed edge infrastructure consisting of Regional Edge and Radio Edge nodes.

### CF RAN with Data-Driven, Fully Distributed Processing
To overcome CF limitations, the authors propose dynamic RU clustering based on the fragmentation of the CF CPU into multiple DUs. This allows for distributed computation and coordination between RUs and DUs. 

Key technical strategies include:
- **ML-Based Clustering:** Using real channel measurements (rather than theoretical models) to optimize peak data rates via ML, avoiding suboptimal "divide and conquer" analytical results.
- **Cluster Stability:** To avoid the overhead of updating clusters every Transmission Time Interval (TTI), the authors emphasize analyzing cluster lifetime and using predictive re-formation to maintain performance for mobile users.

### O-RAN Based Near-RT RIC for CF Networking
The architecture follows O-RAN disaggregation, utilizing a virtualized O-RAN Distribution Unit (vO-DU) for real-time functions and a virtualized O-RAN Central Unit (vO-CU) for non-real-time functions. The vO-CU is further split into Control Plane (vO-CU-CP) and User Plane (vO-CU-UP).

Specific enhancements include:
- **Interface Mapping:** Use of the 7.2 split for the Open Fronthaul to balance transport bandwidth and antenna scalability. Deployment puts vO-DU and vO-CU-UP at the Radio Edge, while the Near-RT RIC and vO-CU-CP reside at the Regional Edge.
- **CF Integration:** CF high-PHY functions (modulation/precoding) are integrated with the vO-DU and MAC scheduler via a 5G FAPI-like interface.
- **Radio Resource Management (RRM):** The Near-RT RIC handles global RRM using ML inference, while the vO-DU performs local scheduling to complement this global view. A Near-RT SDN function is also proposed to react to workload variations in sub-second timescales.

### Optical Network for Midhaul Transportation and Fixed-Mobile Integration
The midhaul uses a ring configuration of Reconfigurable Optical Add Drop Multiplexers (ROADMs). It implements Fixed-Mobile Convergence (FMC) by allowing fixed services (FTTH) and mobile radio edge traffic to share the same fiber infrastructure via XGS-PON and Point-to-Point (PtP) interfaces.

Control mechanisms include:
- **SDTN Controller:** A Software Defined Transport Network controller uses RESTCONF messages to dynamically shift unused capacity from PtMP segments to PtP segments based on load.
- **Traffic Management:** Open vSwitch (OVS) handles traffic aggregation at regional nodes, coordinated by a Network-Slicing-as-a-Service (NSaaS) subsystem. This allows for predictive slice reconfiguration and energy saving via the shutdown of idle SFP-OLTs.

### Q-Learning-Based Evaluation of the Proposed Network Architecture
The architecture was evaluated using a simulation of 64 RUs and 10 UEs at 4 GHz, comparing Round Robin (SISO), Maximum Ratio Transmission (MRT), and Zero Forcing (ZF) precoders. A Q-learning algorithm was used to optimize the set of serving RUs for each Physical Resource Block (PRB).

**Key Findings:**
- **Spectral Efficiency (SE):** CF ZF achieved the highest system SE at 89.4 Mb/s/Hz, significantly outperforming CF MRT (74.3 Mb/s/Hz) and SISO Round Robin (58.6 Mb/s/Hz).
- **Coverage:** ZF provided superior coverage (5.93 Mb/s/Hz for the bottom 5% of users), whereas MRT showed poor coverage (0.32 Mb/s/Hz) because it prioritizes users already in good radio conditions.
- **Conclusion on Precoding:** While ZF is highly effective, the authors note that Regularized Zero Forcing (RZF) and Deep RL for MRT are potential areas for further improvement.

## Conclusion
The paper concludes that integrating distributed Cell-Free concepts with a serial fronthaul approach within the O-RAN architecture enables cost-effective scaling of RUs. By combining this with an optical midhaul supporting Fixed-Mobile Convergence and ML-based RU optimization, the proposed configuration provides a viable path toward 6G converged networks.
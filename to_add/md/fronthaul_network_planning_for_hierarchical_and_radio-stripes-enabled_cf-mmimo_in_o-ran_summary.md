---
index_terms:
  - cell-free massive MIMO
  - fronthaul network planning
  - total cost of ownership
  - O-RAN functional splits
  - hierarchical fronthaul scheme
  - radio stripes
  - mixed-technology optimization
---

# Fronthaul Network Planning for Hierarchical and Radio-Stripes-Enabled CF-mMIMO in O-RAN

## I. Introduction
The deployment of ultra-dense networks (UDNs), specifically cell-free massive MIMO (CF-mMIMO), is limited by the high cost and capacity constraints of fronthaul links connecting Access Points (APs) to Central Processing Units (CPUs/DUs). While traditional fiber provides reliability, it lacks scalability and is expensive. This paper introduces a Hierarchical Scheme (HS) as a resilient and cost-effective alternative to the existing Radio Stripes (RS) serial connection architecture. The authors propose a two-tiered optimization framework to minimize Total Cost of Ownership (TCO) by integrating hybrid technologies: fiber optics, millimeter-wave (mmWave), and Free-Space Optics (FSO). The study evaluates these within the O-RAN architecture, comparing various functional splits (FS7.2x vs. FS8) and deployment topologies to find a balance between cost, capacity, and network resilience.

## II. System Model for Hybrid Fronthaul Networks

### A. Hybrid Fronthaul Network Architecture
The model assumes a 2D square area with randomly distributed APs grouped into $G$ clusters via K-Means Clustering (KMC). Each group is associated with one of $W$ Distributed Units (DUs).
- **Radio Stripes (RS):** APs within a group are connected serially via shared fiber. A "leading AP" communicates directly with the DU and forwards data to non-leading APs.
- **Hierarchical Scheme (HS):** Similar to RS but employs a hierarchical/tree topology instead of serial links, reducing single points of failure.
- **Technology Components:** Fiber uses WDM-PON (ONUs, OADMs, OTNs); mmWave utilizes analog beamforming with quantized phase shifters at the DU; FSO relies on P2P transceivers.

### B. FS-Options Capacity Requirements
Fronthaul capacity thresholds ($\psi$) are defined based on O-RAN functional splits:
- **FS8 (PHY-RF split):** APs perform only RF processing, requiring high fronthaul capacity because raw time-domain signals must be transmitted.
- **FS7.2x (Low-PHY split):** Some PHY functions are shifted to the AP, significantly reducing the required data rate compared to FS8.
The model also accounts for non-homogeneous traffic (spatially varying demand) and control plane overhead ($\alpha$), which adds a proportional factor to the user-plane data rate.

### C. Fiber-Based Fronthaul Link Capacity
Fiber links are modeled as lossless with a constant capacity of 10 Gbps, utilizing XGS WDM-PON technology for symmetrical uplink and downlink rates.

### D. mmWave-Based Fronthaul Link Capacity
Using the 3GPP Urban Microcell street canyon model, the paper accounts for both Line-of-Sight (LoS) and Non-Line-of-Sight (NLoS) path loss, including Gaussian shadowing. The DU uses analog beamforming with quantized phase shifters to focus signals toward APs. Capacity is determined by the Signal-to-Noise Ratio (SNR) and available bandwidth.

### E. FSO-Based Fronthaul Link Capacity
FSO capacity is modeled considering atmospheric losses: scattering (visibility-dependent), turbulence (refractive index variations), scintillation, and geometrical spreading. The model assumes LoS transmission with an average visibility of 0.4 km and incorporates rain/fog attenuation to determine the achievable data rate.

## III. Hierarchical and Radio-Stripes-Enabled CF-mMIMO Network Configuration

### A. Preliminary Network Construction Methodology
To ensure balanced clusters, the authors refine KMC results using Split-Merge Rules (SMR). Groups exceeding a maximum threshold ($g_s$) are split, and those below a minimum ($g_m$) are merged with neighbors. This prevents oversized or undersized clusters before topology construction.

### B. Constructing Radio-Stripes-Based CF-mMIMO Network
Within each group, APs are connected serially to minimize total distance. The authors solve the Traveling Salesman Problem (TSP) optimally for small groups and use a Nearest Neighbor (NN) approximation for larger ones. A "Near-Optimal Fronthaul Association and Configuration" (NOFAC) algorithm iteratively optimizes DU placements and leading AP selection until the maximum movement of any DU falls below a threshold $\epsilon$.

### C. Constructing Hierarchical-Based CF-mMIMO Network
HS utilizes a Minimum Spanning Tree (MST) via Prim's or Kruskal's algorithms to minimize inter-AP distances within each group. The leading AP is defined as the node with the highest degree of connectivity in the tree. The NOFAC algorithm is then applied similarly to the RS case to optimize DU locations and associations.

## IV. Fronthaul TCO Optimization Formulation

### A. Tier 1 Optimization
Tier 1 focuses on the shared internal group infrastructure for non-leading APs. This includes the cost of fiber cables per meter and ONU/OADM hardware. Because this is based on the topology generated by NOFAC, these costs remain constant during the second tier of optimization.

### B. Tier 2 Optimization
Tier 2 optimizes the links between leading APs and DUs using an objective function that minimizes TCO (CAPEX + OPEX):
- **Fiber Cost:** Includes ONU/OADM equipment, cabling $\eta$, and DU-side OTN costs.
- **mmWave Cost:** Includes RX hardware at the AP and a massive MIMO antenna array at the DU.
- **FSO Cost:** Aggregated P2P deployment and maintenance costs per group.

**Constraints include:**
1. **Architectural:** Each leading AP must select exactly one technology.
2. **QoS Metrics:** Links must meet the capacity threshold $\psi^{FSX}$ and satisfy a minimum average network availability ($\zeta^{SLA}$).
3. **Technology-Specific:** Fiber cost scales with the number of OTNs required (based on splitter ratio $\Theta$); mmWave DU costs are only incurred if at least one AP uses mmWave.

### C. Final Formulation and Proposed Algorithm
The problem is formulated as an Integer Linear Program (ILP). It is solved using the branch-and-bound method to find a globally optimal selection of technologies $(x, z, u)$ for leading APs and required hardware $(\kappa, v)$ at the DUs.

## V. Numerical Results

### A. Fronthaul Technologies Selection
Results show that fiber is prioritized for APs close to DUs due to low cost, while mmWave is used for distant APs where reliability permits. FSO use is minimal due to high costs and lower reliability. Decentralization (increasing DU count $W$) actually increases the prevalence of fiber as distances shrink.

### B. Network Optimized TCO and Number of Groups
Larger group sizes reduce overall fronthaul cost but increase processing load on DUs. All-mmWave deployments are the cheapest but are often infeasible because they violate capacity constraints. FS7.2x is more cost-effective than FS8 because it requires lower fronthaul rates.

### C. Network Surplus Capacity and Number of Groups
The hybrid optimized scheme provides substantial "surplus capacity" (headroom for future traffic) at a much lower cost than all-fiber networks. FS7.2x consistently offers higher surplus capacity than FS8, reinforcing its superiority as an O-RAN split.

### D. Radio-Stripes, Hierarchical and Small Cells TCO
Compared to traditional P2P small cell architectures, both RS and HS significantly reduce the average TCO per AP by sharing resources within groups, particularly in centralized deployments ($W < 4$).

### E. Non-Homogeneous Traffic Analysis
Using a Gaussian mixture model for traffic hotspots, the authors find that high-demand regions force the optimizer to select fiber over wireless options. If demand exceeds the physical capacity of all available technologies, the framework identifies these as infeasible links, serving as a diagnostic tool for network densification needs.

### F. Network Resilience Analysis
RS is highly vulnerable to cascading failures; a single link break can disconnect multiple subsequent APs in the stripe. HS significantly improves resilience due to its branched tree structure. Increasing the number of groups $G$ (decreasing group size) further reduces failure interdependence, moving closer to the robustness of P2P architectures.

### G. Variance Analysis Across Randomized Deployments
Across 500 random realizations, the optimized ILP approach exhibits a lower median cost and narrower variance than heuristic methods. This advantage grows as the number of DUs ($W$) increases, indicating that joint optimization is critical in complex, decentralized deployments.

## VI. Conclusion
The proposed two-tiered framework effectively minimizes TCO for hybrid CF-mMIMO fronthauls. The findings indicate that a mixed-technology approach is superior to single-technology strategies. Specifically, the Hierarchical Scheme (HS) provides a vital balance of cost-efficiency and resilience over Radio Stripes (RS), and FS7.2x is identified as the most scalable functional split for future 6G UDNs.
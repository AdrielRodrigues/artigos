---
index_terms:
  - Space Division Multiplexing
  - Elastic Optical Networks
  - Priority-based Resource Allocation
  - Multicore Fiber
  - Blocking Probability Ratio
---

# Priority-Aware Resource Allocation Strategies for Space Division Multiplexing-enabled Elastic Optical Networks

## I. Introduction
The surge in data-intensive applications (IoT, cloud services, HD streaming) requires optical networks with higher capacity and flexibility. While Elastic Optical Networks (EONs) provide flexible bandwidth, single-mode fibers are reaching their physical limits. Space Division Multiplexing (SDM), specifically via Multi-Core Fibers (MCFs), addresses this by enabling parallel transmission paths to increase spectral efficiency and total bandwidth.

However, SDM-EONs introduce complex resource management challenges, including the need to allocate routes, modulation formats, spectrum slots, and cores while managing physical impairments like crosstalk. The authors argue that most existing allocation strategies fail to differentiate traffic based on priority. This paper proposes a priority-aware resource allocation strategy designed to reduce bandwidth waste and blocking probabilities for critical (high-priority) demands.

To evaluate this, the authors developed a Python-based simulation using pre-computed k-shortest paths and dynamic traffic generation. The objective is to demonstrate that prioritizing real-time or emergency traffic improves network reliability and responsiveness under high load.

## II. Related Work
The paper reviews several existing approaches to resource allocation in SDM-EONs:
- **RMCSA Algorithms:** Research has focused on Routing, Modulation, Core, and Spectrum Allocation (RMCSA) using score functions to mitigate crosstalk and fragmentation.
- **Machine Learning & Heuristics:** Techniques like Tridental Resource Assignment (TRA) and Spectrum Wastage Avoidance-based Resource Allocation (SWARM) use ML to adapt to dynamic traffic, while other heuristics focus on cost and operational efficiency for large-scale internet traffic.
- **Resilience and Priority:** Some studies introduce fragmentation-aware load balancing or advance reservation for offline survivability. Specifically, the P-TRRA mechanism differentiates between premium, emergency, and best-effort service classes to maintain Quality of Service (QoS) during congestion.
- **Advanced Management:** Other work explores deep reinforcement learning for service function chains, impairment-aware models that account for nonlinear effects, and the use of hidden optical bypasses in multi-layer networks to reroute data dynamically.

## III. Methodology
The authors implement a simulation framework in Python using NumPy to model an SDM-EON environment.

### Network and Traffic Model
The network consists of nodes connected by links, where each link is divided into the smallest allocatable units called "slots." The simulation uses synthetic traffic demands (source, destination, and required slots) stored in input files. To reduce computational overhead during runtime, the three shortest paths for every source-destination pair are pre-computed using a k-shortest path method.

### Priority-Based Allocation Algorithm
The allocation process follows these steps:
1. **Demand Processing:** Each request is read sequentially from the traffic file.
2. **Path Evaluation:** The algorithm checks the primary (shortest) path first. If it lacks sufficient unallocated slots, it proceeds to evaluate the second and third pre-computed paths.
3. **Capacity and Slot Allocation:** Once a viable path is identified, the required slots are marked as occupied for that specific duration.
4. **Priority Logic:** The system differentiates traffic based on priority levels; if multiple paths are available, selection criteria (such as "least used") are applied to optimize placement.
5. **Blocking:** Demands that cannot be accommodated on any of the three paths are logged as blocked.

### Performance Metrics
The primary metric used is the Blocking Probability Ratio (BPR), defined as the number of blocked connections divided by the total number of demands. The authors also track link utilization and the time intervals between successful allocations.

## IV. Results and Discussion

### A. Traffic Demand Allocation and Blocking
Simulation data shows that blocking increases during peak traffic periods due to contention in key network segments. Conversely, during low-traffic intervals, the priority mechanism successfully protects high-priority demands, with any remaining blockages primarily affecting low-priority traffic.

### B. Blocking Probability Analysis
The authors compare three configurations: traditional EON, Priority-Based EON (PB-EON), and Priority-Based SDM-EON (PB SDM-EON). 
- **Traditional EON:** Highest blocking due to a lack of prioritization and spatial flexibility.
- **PB-EON:** Shows higher total blocking than PB SDM-EON because it deliberately rejects low-priority traffic to ensure resources for high-priority demands.
- **PB SDM-EON:** Consistently achieves the lowest BPR. By combining spatial resources (multicore fibers) with priority awareness, it maintains near-optimal performance for demand levels below 250 and effectively differentiates service quality under heavy loads.

### C. Visualization of a Successfully Allocated Demand
The simulation results confirm that the algorithm can successfully identify and highlight valid optical paths between nodes (e.g., Node 1 to Node 4) while adhering to availability and priority rules.

### D. Network Utilization Analysis
Analysis reveals the existence of traffic "hotspots" where certain links are consistently overloaded, indicating a need for better route diversity. The algorithm shows an attempt to balance loads across the network, and shorter intervals between successful allocations indicate high responsiveness to dynamic traffic.

### E. Design Implications and Future Scope
The authors identify several areas for improvement:
- **Fairness:** While priority is handled well, there is room to improve the fairness of resource distribution.
- **Scalability:** Congestion at specific nodes under high load suggests a need for multicore-aware parallel path provisioning.
- **Adaptive Mechanisms:** The integration of distance-adaptive modulation and routing could further enhance spectral efficiency, particularly for long-distance paths in dense traffic.

## V. Conclusion
The paper concludes that integrating priority-aware strategies into SDM-EONs significantly enhances resource allocation efficiency. By combining a literature survey with a Python simulation, the authors demonstrate that utilizing multicore fibers alongside a priority-based allocation mechanism effectively reduces blocking probabilities for critical traffic and ensures scalable network performance compared to traditional EON architectures.
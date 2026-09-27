---
index_terms:
  - network slicing
  - resource management
  - end-to-end (E2E)
  - cross-domain orchestration
  - radio access networks (RAN)
  - transport networks (TN)
  - core networks (CN)
  - 5G/6G networks
---

# Resource Management From Single-Domain 5G to End-to-End 6G Network Slicing: A Survey

## I. Introduction
Network Slicing (NS) allows Mobile Network Operators (MNOs) to create virtual, logical networks tailored to specific service requirements (eMBB, URLLC, mMTC) over shared physical infrastructure. While significant research exists on single-domain slicing, the authors argue that a holistic End-to-End (E2E) approach is necessary because technological domains—Radio Access Network (RAN), Transport Network (TN), and Core Network (CN)—are deeply interdependent. For example, computing resources may be shared between RAN and CN functions; thus, a solution feasible in one domain may fail in an E2E context due to resource exhaustion in another. 

The paper's primary aim is to survey the progress of NS resource management across these domains, analyzing the limitations of single-domain and cross-domain approaches and identifying the research directions required for true E2E 6G slicing.

## II. Key Definitions

### A. Definition
A Network Slice (NS) is a logical E2E network delivered via a Service Level Agreement (SLA). Once activated, it becomes a Network Slice Instance (NSI), composed of several Network Slice Subnet Instances (NSSIs) for different domains. Management is hierarchical: the Communication Service Management Function (CSMF) translates service needs to network requirements; the Network Slice Management Function (NSMF) manages NSIs; and the Network Slice Subnet Management Function (NSSMF) handles specific NSSIs.

### B. Technological Domains
*   **Core Network (CN):** Manages access, mobility, and session management. Modern CNs leverage NFV and MEC to move delay-sensitive functions (e.g., UPF) closer to the edge.
*   **Transport Network (TN):** The links and nodes connecting RAN and CN. Slicing here focuses on link capacity, latency, and SDN-enabled routing efficiency.
*   **Radio Access Network (RAN):** Characterized by functional splits (RU, DU, CU). Open RAN (O-RAN) promotes lower-level splits to enhance flexibility and virtualization.
*   **User Equipment (UE):** The end-device acting as the communication termination point.

### C. Related Stakeholders
NS involves four main actors with potentially conflicting goals: Infrastructure Providers (InPs), MNOs, Slice Tenants (STs), and End-Users. These stakeholders often represent different administrative domains, complicating cross-domain coordination.

### D. Enabling Technologies
*   **NFV:** Deploys network functions as VNFs or CNFs on VMs/containers to reduce cost and increase flexibility.
*   **SDN:** Separates the control plane from the data plane, enabling centralized, programmable network management.
*   **MEC:** Places computing and storage at the edge to reduce latency and backhaul load.

### E. Lifecycle Management (LCM)
The NS LCM follows four phases: Preparation (design/onboarding), Commissioning (creation/allocation), Operation (supervision/modification), and Decommissioning (termination).

### F. Resource Management Functionalities
*   **Admission Control (AC):** Decides whether to accept a slice request based on feasibility.
*   **Resource Allocation (RA):** Assigns specific resources to an accepted slice.
*   **VNF Placement:** Determines the optimal location for VNFs/CNFs and reserves interconnection capacity.
*   **Reconfigurability:** Dynamically scales or adjusts resources during the operation phase.
*   **Orchestration:** Coordinates interactions between management entities across domains.
*   **Security Considerations:** Focuses on slice isolation to prevent inter-slice interference and mitigate attacks (e.g., DDoS).

### G. Considered Problem and Potential Solutions
The authors formulate a generic optimization problem: $\min/\max f(x)$ subject to linear or non-linear constraints. 
*   **Complexity:** NS problems are typically combinatorial and NP-hard due to discrete variables (e.g., VNF placement) and the intersection of feasible regions across different domains.
*   **Problem-Solving Methodologies:**
    *   **Optimization-based:** Includes closed-form (Queueing Theory), relaxation-based (convex approximation), and metaheuristics (Genetic Algorithms).
    *   **Machine Learning (ML):** Supervised Learning for prediction, Unsupervised for pattern recognition, Reinforcement Learning (RL/DRL) for automated decision-making in dynamic environments, and Federated Learning (FL) for privacy-preserving decentralized training.
    *   **Game Theory (GT):** Models strategic interactions between rational stakeholders (e.g., MNOs and STs).

## III. Single-Domain NS Frameworks
Single-domain frameworks manage only one part of the network (RAN, TN, or CN) and suffer from a lack of visibility into other domains.

### A. Admission Control (AC)
Optimization approaches often map AC to multiple knapsack problems but ignore historical request data. DRL-based techniques adapt better to dynamic demands but require large datasets. The core failure is that accepting a slice in one domain without verifying the others leads to QoS violations during operation.

### B. Resource Allocation (RA)
Methods range from genetic algorithms for C-RAN design to model-free DRL for flexible deployment. GT is used primarily for pricing resources between InPs and MNOs. These frameworks create bottlenecks because they ignore interdependent constraints (e.g., allocating RAN resources without ensuring TN bandwidth).

### C. VNF Placement
Research focuses on balancing latency/cost against resource utilization. While DRL allows for dynamic migration of VNFs, the lack of hybrid placement strategies that consider both RAN and CN VNFs simultaneously makes these solutions unrealistic.

### D. Reconfigurability
Reconfigurations (e.g., scaling) are handled either reactively via heuristics or proactively using traffic prediction (DES/NNs). DRL provides better resilience but is often limited to a single domain, leading to over-provisioning in one area and under-utilization in another.

### E. Orchestration
Single-domain orchestration focuses on hierarchical abstraction (e.g., SDN controllers reporting to a domain orchestrator). The main challenge is the lack of full programmability across all hardware vendors.

### F. Security Considerations
Efforts focus on slice isolation to mitigate DDoS attacks and securing Southbound Interfaces (SBI) using QKD. However, protecting one domain leaves the E2E service vulnerable to attack vectors in other domains.

### G. Summary
Single-domain solutions are insufficient because they cannot guarantee E2E QoS due to a lack of cross-domain coordination.

## IV. Cross-Domain NS Frameworks
These frameworks combine two domains (RAN+CN, RAN+TN, or TN+CN).

### A. RAN + CN
*   **AC & RA:** Joint modeling is superior to disjointed approaches but increases combinatorial complexity. Heuristics and DRL (specifically twin-actor DDPG) are used to balance efficiency and optimality.
*   **Reconfigurability:** ML-based schemes can trigger VNF migration based on mobility, but often ignore the most critical radio resources (PRBs).
*   **Orchestration:** Heavy reliance on DRL; however, these systems typically ignore TN congestion.
*   **Security:** Optimization techniques model DDoS-aware restrictions but struggle with the trade-off between detection accuracy and resource efficiency.

### B. RAN + TN
Focuses primarily on RA and reconfigurability. Coordination helps minimize over-provisioning compared to TN-only solutions, though most lack integration with CN VNF placement or compliance with O-RAN standards.

### C. TN + CN
Commonly uses Stochastic Network Calculus (SNC) for latency estimation and PSO for heterogeneous service design. These frameworks often overlook RAN resources, making E2E latency estimates inaccurate.

### D. Extending NS Into the UE Domain
Recent attempts to include User Equipment (UE) feedback (e.g., CQIs) improve RA decisions, but user-level isolation between multiple active slices remains an open problem.

### E. Summary
While cross-domain solutions are more reliable than single-domain ones, they still leave a "blind spot" by ignoring one of the three main technological domains, which can lead to unexpected service failure.

## V. E2E NS Frameworks
True E2E frameworks incorporate RAN, TN, and CN simultaneously under a high-level orchestrator.

### A. Admission Control (AC)
*   **Generic:** Use abstract domain models but are often inaccurate.
*   **E2E Solutions:** Employs RL (e.g., SARSA) or joint optimization to handle the massive dimensionality of E2E resources. These are fairer and more reliable than cross-domain versions.

### B. Resource Allocation (RA)
*   **Generic:** Model nodes/links generically but fail to capture domain-specific nuances like PRB allocation.
*   **E2E Solutions:** Use Queueing Theory for delay estimation or DRL (e.g., PPO) to jointly allocate radio, power, and bandwidth. The challenge is reducing the state-action space without losing accuracy.

### C. Reconfigurability
Research is sparse. Generic heuristics can redefine inter-domain delay budgets, but full E2E dynamic reconfiguration requires hierarchical orchestration to avoid long response times that degrade QoS.

### D. Orchestration
*   **Generic:** Focuses on interoperability via standard interfaces (OSM/NFVO) and Blockchain for trust in multi-InP environments.
*   **E2E Solutions:** Use Multi-agent DRL where domain orchestrators report to a central NSMF. Techniques like "safety DRL" and imitation learning are used to accelerate convergence.

### E. Security Considerations
Most solutions are generic trust frameworks using Blockchain/Smart Contracts for SLA negotiation between stakeholders. There is a lack of integrated intra- and inter-domain security mechanisms that account for non-virtualized resources (e.g., radio power).

### F. Summary
E2E research is still in its infancy. Most "E2E" claims in literature are actually cross-domain solutions with oversimplified models. Full E2E automation remains a primary gap.

## VI. Research Projects and Experimental Testbeds

### A. Research Projects
The authors highlight EU initiatives (Horizon 2020, 6G SNS JU) focusing on AI/ML for RA and trust mechanisms (e.g., 5GZORRO). US-based PAWR provides city-scale testbeds like POWDER and Colosseum for O-RAN slicing.

### B. Experimental Testbeds
Most testbeds are single-domain. Cross-domain examples include those using ONAP or TSN control planes. The "Hyperstrator" orchestrator is noted as a modular, open-source E2E implementation, though it simplifies TN components via OVS containers rather than real optical switches.

## VII. Challenges and Future Directions
*   **Orchestration:** Need for standardized APIs to enable trust and visibility across different administrative domains.
*   **Open RAN Integration:** Leveraging the RIC (Radio Intelligent Controller) and xApps/rApps for more flexible E2E slicing.
*   **Scalability:** Developing Network Digital Twins to virtually test E2E solutions before physical deployment.
*   **Automation:** Integrating ETSI ZSM with O-RAN for zero-touch lifecycle management.
*   **Advanced AI:** Using LLMs for human-friendly configuration, Multi-Agent DRL for decentralized control, and Federated Learning for privacy.
*   **Specialized Slicing:** Investigating Hierarchical (recursive) slicing where a tenant further slices their allocated NSI, and UE-level slicing for multiple active slices per device.
*   **Open Science:** A call for more open-source datasets and frameworks to avoid reliance on outdated synthetic data.

## VIII. Conclusion
Resource management must move from isolated domain optimization to joint E2E orchestration. The authors conclude that while E2E frameworks are the most reliable, they are the most complex to implement. AI/ML is essential for managing this complexity, particularly in transitioning from 5G to 6G.
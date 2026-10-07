---
index_terms:
  - hybrid hierarchical federated learning
  - coordinated multi-point
  - non-IID data
  - convergence analysis
  - 5G/NextG wireless networks
  - training efficiency
---

# Hybrid Hierarchical Federated Learning Over 5G/NextG Wireless Networking

## Abstract
The paper introduces Hybrid Hierarchical Federated Learning (HHFL), an architecture designed for 5G and NextG networks that leverages Coordinated Multi-Point (CoMP) transmission. Unlike traditional Hierarchical Federated Learning (HFL), which restricts clients to a single edge server (ES), HHFL allows clients in overlapping coverage areas to communicate with multiple ESs simultaneously. This enables these clients to act as "knowledge bridges," facilitating inter-ES knowledge sharing, reducing model divergence, and accelerating convergence—particularly when data is non-independent and identically distributed (non-IID) across servers.

## I. Introduction
Standard Federated Learning (FL) often uses a star topology, but large-scale networks require hierarchical structures to reduce the load on centralized cloud servers (CS). While traditional HFL introduces intermediate edge servers, it forces a one-to-one client-ES association. This ignores the capabilities of 5G/6G CoMP technology, where clients can connect to multiple base stations. In HFL, ESs update models in isolation between global aggregations, leading to localized optima and divergence under non-IID conditions. HHFL addresses this by allowing overlapping-region clients to aggregate models from multiple ESs and propagate the resulting fused knowledge back to all associated servers, thereby aligning local updates more closely with the global objective.

## II. Preliminaries and Models

### A. Basic FL Architecture
Basic FL utilizes a centralized CS that broadcasts a global model $w^{t_0}$ to $K$ clients. Clients perform $E$ local steps of stochastic gradient descent (SGD) to update their models based on private data loss functions $F_i$. The CS then aggregates these updates using a weighted average (FedAvg), where weights are based on the proportion of data held by each client.

### B. The HFL Architecture
HFL introduces an intermediate layer: Client $\to$ ES $\to$ CS. 
1. **Downlink:** The global model flows from CS to ESs, then to clients.
2. **Edge Aggregation:** Clients perform local updates and send them to their associated ES for aggregation (Hier-FedAvg). This is repeated for $G$ rounds.
3. **Cloud Aggregation:** After $G$ edge rounds, ESs upload aggregated models to the CS for global refinement.

## III. Architecture Design

### A. Motivation and Architecture Design
Modern wireless networks use CoMP to improve spectral efficiency and QoS by allowing multi-point connectivity. HHFL applies this to FL training:
- **Downlink:** Overlapping clients receive multiple models via frequency-orthogonal physical resource blocks (PRBs) allocated through the Xn interface, avoiding inter-cell interference.
- **Client Aggregation:** Clients in overlapping areas average received models from all connected ESs before local training.
- **Uplink:** A single transmission from a client is processed in parallel by multiple associated ESs using uplink multi-point reception.
- **Implementation:** To minimize overhead, HHFL avoids complex joint decoding and instead uses independent processing at each ES. It employs 5G configured grants (CG) to pre-allocate periodic uplink resources, bypassing dynamic scheduling latency.

### B. HHFL Algorithm Design
The HHFL algorithm iterates through the following steps:
1. **CS Broadcast:** Global model $w^{t_0}$ is sent to all ESs.
2. **Client Aggregation:** Clients initialize their models by averaging parameters from all connected ESs in set $S_i$.
3. **Local Training:** Clients perform $E$ local SGD steps.
4. **Edge Aggregation:** Clients upload updated models to all associated ESs. Each ES aggregates these updates using a weighted sum based on client data proportions and the number of servers each client is connected to.
5. **Cloud Aggregation:** Every $G$ edge rounds, ESs send their models to the CS for global aggregation.

## IV. Performance Analysis

### A. Convergence Analysis
The authors analyze the evolution of local models through state vectors $\mathbf{w}^t$ (initial) and $\mathbf{v}^{t+1}$ (after training but before aggregation). They define a **virtual global model** $\overline{w}^t$ as the weighted sum of all client models to monitor real-time performance.

Using four standard FL assumptions (L-smoothness, $\mu$-strong convexity, bounded stochastic gradient variance, and uniformly bounded squared norms), the authors derive a convergence upper bound. Theorem 1 establishes that the expected difference between the global model and the optimum converges toward zero as $t$ increases. Notably, when ES-level data is non-IID, HHFL's convergence constant ($Z$) is smaller than HFL's ($Z'$), indicating faster convergence.

### B. Comparison Between HFL and HHFL
1. **Steps to Convergence:** In HFL, ES isolation leads to higher gradient variance under non-IID data. HHFL reduces this variance because overlapping clients inject diverse knowledge into each ES, making the starting points for local updates more representative of the global distribution.
2. **Time to Convergence:** Total time includes computation and transmission. Since 5G hardware allows parallel processing of multi-point links, the per-round transmission time $T_{CES}$ is nearly identical for both. However, HHFL requires fewer total steps, resulting in shorter overall wall-clock time.
3. **Resource Consumption:** HHFL increases per-round PRB occupancy and energy use due to more communication links. However, if data is sufficiently non-IID, the reduction in total training rounds outweighs this increase, leading to lower overall system resource consumption.

## V. Experimental Evaluation

### A. Basic Experimental Setup
Experiments use one CS, three ESs (equilateral triangle layout), and 57 clients. Models include logistic regression (convex) and CNN (non-convex) trained on MNIST and CIFAR-10. Scenarios vary by the degree of non-IID data at both client and ES levels.

### B. Experimental Results and Analysis
1. **ES IID Scenario:** When data is distributed identically across servers, HHFL provides no significant advantage over HFL since inter-ES knowledge sharing is unnecessary.
2. **ES non-IID Scenario:** HHFL consistently outperforms HFL. The gap widens as the degree of non-IIDness increases; HFL performance degrades significantly while HHFL remains robust.
3. **Overlapping Proportion:** Increasing the proportion of clients in overlapping regions accelerates HHFL convergence, though returns diminish after a certain threshold (saturation).
4. **Wall-Clock Time and Data Volume:** In non-IID settings, HHFL reaches target accuracy faster in terms of wall-clock time. While it transmits more data per round, the total data volume is lower than HFL's because HHFL converges in far fewer rounds.
5. **Impact of E and G:** Increasing $E$ (local steps) or $G$ (edge rounds before cloud aggregation) aggravates model drift in traditional HFL. In HHFL, the multi-connectivity "bridge" mitigates this drift, making HHFL's relative advantage more pronounced as $E$ and $G$ increase.
6. **CIFAR-10 Robustness:** Results on CIFAR-10 with a VGG-11 backbone mirror MNIST results, confirming that HHFL achieves efficiency gains $> 1.5\times$ in non-IID scenarios regardless of model complexity.

## VI. Related Work
The authors distinguish HHFL from existing hierarchical FL (which focuses on clustering or personalized models but keeps one-to-one client-ES links) and multi-server architectures (like FedMes). While some previous works allowed overlapping area connectivity, they focused on localized sharing. HHFL combines local inter-ES sharing via clients with global synchronization via the CS, which is highly effective in 5G environments where wired backhaul between ESs and the CS is high-speed.

## VII. Conclusion
HHFL extends HFL by integrating CoMP technology to allow multi-server connectivity for overlapping clients. Theoretical and experimental evidence proves that HHFL significantly improves convergence speed and efficiency in non-IID wireless network environments, offering a scalable solution for future 5G/NextG deployments.
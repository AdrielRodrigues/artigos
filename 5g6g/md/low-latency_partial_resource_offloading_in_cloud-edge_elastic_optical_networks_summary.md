---
index_terms:
  - Cloud-Edge Elastic Optical Networks
  - Partial Resource Offloading
  - End-to-End Latency
  - Server Importance Degree
  - Integer Linear Programming
  - Proportional Segmentation
---

# Low-latency partial resource offloading in cloud-edge elastic optical networks

## 1. Introduction
The proliferation of IoT, 5G, and cloud computing has increased the demand for efficient networked computing capacity. While Cloud Computing provides vast resources, it often fails to meet strict latency requirements. Mobile Edge Computing (MEC) addresses this by offloading tasks to servers closer to the user. This paper focuses on Cloud-Edge Elastic Optical Networks (CE-EONs), a three-layer integration of IoT, edge computing, and cloud computing. The core objective is to optimize network resource allocation and reduce end-to-end (E2E) latency by determining whether to offload requests and where to send them. Specifically, the authors introduce partial resource offloading—splitting tasks between local and remote servers—and propose a Server Importance Degree (SID) metric to balance load across regions.

## 2. Related Work and Our Contributions

### A. Resource Offloading Problem
Existing approaches are categorized into binary offloading (all or nothing), partial task offloading (splitting data size), and cloud-edge collaboration. While previous research on CE-EONs explored selective offloading based on resource equalization, they did not specifically investigate reducing E2E latency through the lens of divisible versus indivisible services in an elastic optical context.

### B. E2E Latency Problem
E2E latency comprises transmission time (terminal to node) and processing time (at the server). Current research focuses on joint communication/computing resource allocation, task segmentation strategies, and SDN-based load balancing to minimize this delay.

### C. Our Contributions
The paper contributes:
1. A detailed calculation of E2E latency for partially offloaded tasks.
2. An Integer Linear Programming (ILP) model designed to minimize both average E2E latency and frequency slot occupancy.
3. Four heuristic approaches, including a "proportional segmentation" method.
4. Performance demonstrations showing that proportional segmentation closely approximates the optimal ILP solution while reducing blocking probability and latency in dynamic scenarios.

## 3. System Model and Problem Statement

### A. System Model
The CE-EON is modeled as a weighted undirected graph $G(B, CN, EN, CL, EL, J)$ comprising base stations (BSs), cloud nodes (CNs), edge nodes (ENs), fiber links (cloud and edge links), and optical switches. The network utilizes an Elastic Optical Network (EON) architecture where spectrum resources are divided into 12.5 GHz frequency slots. Bandwidth allocation must adhere to the constraints of spectrum consecutiveness (slots must be adjacent) and consistency (same slots used across a path).

### B. Problem Statement
The study examines both static scenarios (resources not released until all requests are handled) and dynamic scenarios (resources released after processing). Each user request $u$ is defined by its source, bandwidth requirement, computing resource need, and traffic type. The goals are to minimize average E2E latency via partial offloading and optimize network resources using the server importance degree to maintain load balance between regions.

## 4. E2E Latency and Partial Resource Offloading

### A. E2E Latency
Latency is analyzed differently for two types of services:
1. **Indivisible Services:** These are processed as a whole in one of three scenarios: local edge server (Scenario 1), adjacent region edge server (Scenario 2), or cloud server (Scenario 3).
2. **Divisible Services:** These can be split using a proportional segmentation ratio $\lambda_u$. A portion is processed locally, and the remainder $(1 - \lambda_u)$ is offloaded to another region. The total E2E latency is defined as the maximum of the local processing time and the remote transmission/processing time.

### B. Partial Resource Offloading and Server Importance Degree
1. **Offloading Decision Variable ($M_u$):** A binary variable determining if a request stays local ($M_u=1$) or is offloaded ($M_u=0$), calculated based on the local region's computing resource utilization ratio and E2E latency relative to the network's extremes.
2. **Optimal Segmentation Ratio ($\lambda_u$):** To minimize total latency, $\lambda_u$ is derived such that local processing time equals the remote transmission plus processing time. This balance ensures neither component becomes a bottleneck.
3. **Server Importance Degree (SID):** SID is a normalization of E2E latency and available computing resources across edge and cloud servers. It is used to select destination servers that optimize the trade-off between low latency and regional load balancing.

### C. Evaluation Metrics
The system's performance is measured by:
- **Average E2E Latency:** Mean time for all successfully processed requests.
- **Blocking Probability:** Percentage of requests failed due to insufficient spectrum or computing resources.
- **Spectrum Occupancy Ratio (SOR):** Total frequency slots used relative to total available network capacity.
- **Average Hops:** The mean number of fiber links traversed per request.

## 5. ILP Model of Partial Resource Offloading
The authors develop an ILP model to minimize a weighted objective function $P(G) = \alpha T(G) + \beta F(G)$, where $T(G)$ is average E2E latency and $F(G)$ is the total number of frequency slots occupied. 

**Constraints include:**
- **Selection Uniqueness:** Each request must use exactly one path and either one server (whole) or two servers (partial).
- **Node Selection:** Servers cannot be the same as the source node.
- **Capacity:** Total computing resources used at any node cannot exceed its capacity $V_e$, and spectrum usage on any link cannot exceed total frequency slots $|F|$.
- **Spectrum Constraints:** Allocated slots must be continuous in the frequency domain and consistent across all links of a path.

## 6. Heuristic Approaches of Partial Resource Offloading
The paper proposes several heuristics to avoid the NP-hard complexity of ILP:

### A. Partial Resource Offloading Based on Proportional Segmentation (PRO_PS)
This approach classifies requests by type. Indivisible services go to the server with the highest SID. Divisible services are processed locally if the load is below a threshold; otherwise, they are split according to the optimal $\lambda_u$, with the remainder sent to the server with the highest SID.

### B. Collaborative Cloud-Edge (CCE) Offloading Approach
This baseline approach segments tasks based on normalized backhaul communication and cloud computing capabilities, using KKT conditions to minimize E2E latency through joint resource allocation.

### C. Traditional Offloading Approaches
1. **PRO_AS:** Uses a fixed 50/50 average segmentation ratio for divisible services rather than an optimal $\lambda_u$.
2. **All-Resource-Offloading (ARO):** Processes all requests as indivisible units and offloads them entirely to the server with the highest SID.
3. **All-Local-Processing (ALP):** Processes all requests locally using the server with the most available resources; otherwise, they are blocked.

## 7. Complexity Analysis
The ILP model's complexity is high due to its extensive binary variable space. The PRO_PS and CCE heuristics are significantly more efficient, primarily dominated by the K-Shortest Path (KSP) algorithm $O(K \times |S| \times |L|)$ and spectrum allocation via First Fit. ARO and ALP have the lowest complexity as they skip service classification and optimal ratio calculations.

## 8. Simulation and Results

### A. Static Scenario in a 6-Node Network
Using various modulation formats (BPSK to 16-QAM), simulations show:
- **Latency:** PRO_PS is closest to the ILP model (only 3.4% higher). CCE performs worse than PRO_AS because it segments too many services that would be faster if processed locally.
- **Spectrum Occupancy:** ALP has the lowest SOR (no remote transmission), while ARO has the highest. PRO_PS closely follows the ILP's optimized spectrum usage.
- **Average Hops:** ALP is lowest (1 hop). PRO_PS approximates the ILP model, whereas ARO results in the highest hops due to full offloading.

### B. Dynamic Scenario in a 14-Node Network
Simulations with 20,000 requests demonstrate:
- **Blocking Probability:** PRO_PS has the lowest blocking probability because it balances E2E latency with actual server resource availability. ARO is the worst due to lack of segmentation.
- **Average E2E Latency:** PRO_PS achieves the lowest average latency among heuristics by optimizing $\lambda_u$ for divisible tasks and using SID for indivisible ones. ALP performs poorly as load increases because local servers become bottlenecks.
- **Spectrum Occupancy:** ALP remains most efficient in spectrum use, but PRO_PS provides a better balance of performance versus resource usage than CCE or ARO.
- **Average Hops:** ALP is lowest (1 hop); PRO_PS and PRO_AS are similar; CCE and ARO are significantly higher.

## 9. Conclusion
The paper successfully addresses the resource offloading problem in CE-EONs. By introducing partial resource offloading with an optimal segmentation ratio ($\lambda_u$) and a Server Importance Degree (SID) for server selection, the proposed PRO_PS approach provides a near-optimal solution to the ILP model. It effectively reduces average E2E latency and blocking probability while maintaining efficient network spectrum allocation compared to traditional and collaborative offloading methods.
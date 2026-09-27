---
index_terms:
  - optical data center networks
  - software defined optical networks
  - resource scheduling
  - dynamic black widow optimization
  - random forest classification
  - fuzzy c-means clustering
  - spectrum fragmentation
  - blocking probability
---

# Elevating optical networks: Machine learning approach for optimal resource scheduling and performance boost

## Summary
The paper proposes a Dynamic Black Widow Optimized Random Forest (DBWO-RF) strategy to optimize resource scheduling in optical data center networks (ODCNs). The framework integrates Software Defined Optical Networking (SDON) with machine learning (ML) to enhance channel quality assessment and spectrum utilization. Specifically, it employs the Fuzzy C-Means (FCM) algorithm for traffic flow clustering and a Fragmentation-Function-Fit (FFF) algorithm to mitigate blocking risks. Results indicate that this integrated approach reduces blocking probability and improves spectrum efficiency compared to traditional methods.

## 1 | Introduction
Resource scheduling in dynamic computing environments is critical for optimizing assets, reducing latency, and preventing bottlenecks. In optical networks, the transition from copper-based systems to flexible optical transport allows for higher data volumes over longer distances with minimal degradation. Software-Defined Optical Networks (SDON) provide flexibility in control and lower capital costs but require sophisticated algorithms to manage volatile user demands and avoid congestion. Furthermore, optimal resource planning is linked to environmental sustainability by reducing the energy consumption and carbon footprint of communication networks. The primary objective of this research is to implement a DBWO-RF enabled mechanism for flexible connectivity and spectral management within ODCNs.

### 1.1 | Key contributions
The main contributions include:
*   Developing the DBWO-RF technique to enhance optical network performance through adaptive resource allocation.
*   Integrating ML to address the increasing demand for fast, dependable communication.
*   Implementing the FFF algorithm specifically to reduce blocking issues in spectrum allocation.

## 2 | Literature Review
The authors review a wide array of existing ML and DL applications in networking, including:
*   **Deep Learning (DL) & Neural Networks:** Used for predicting model convergence (Optimus), wireless link scheduling based on transmitter/receiver positions, and virtual network function service chaining (vNF-SCs).
*   **Optimization Algorithms:** Use of game models for LTE-LAA/WiFi coexistence, binary computation offloading in H-MEC networks, and Reinforcement Learning (RL) for 5G RAN slicing.
*   **Specific Heuristics:** Application of the African Vulture Optimization Algorithm (AVOA), Aquila Optimizer combined with Whale Optimization (AWOA), and deep Q-learning for Space-Time Networks (STN).
*   **Network Management:** Discussion on Quality of Experience (QoE) forecasting, non-orthogonal multiple access (NOMA) in IoT, and the use of cellular learning automata (ELA-RCP) for controller placement.

## 3 | An SDON and DBWO-RF-Based Resource Allocation Method for ODCNs
The proposed system uses an SDON controller to manage global network topology and resource utilization. The workflow involves collecting physical layer data to build a database, followed by a two-pronged ML approach: supervised learning (DBWO-RF) for channel quality classification and unsupervised learning (FCM) for traffic flow clustering. This intelligence allows the SDON controller to apply adaptive spectrum algorithms like FFF.

### 3.1 | Channel quality classification using (DBWO-RF)
This section details a hybrid model combining Random Forest (RF) with Dynamic Black Widow Optimization (DBWO).
*   **Random Forest (RF):** Used as the classifier to map network attributes ($X_i$) to quality labels ($Y_i$). It aggregates predictions from multiple decision trees using a mode function: $\widehat{Y}_{RF} = \text{mode}\{Z_i^1, Z_i^2, ..., Z_i^K\}$.
*   **DBWO:** An evolutionary algorithm based on the hunting behavior of black widow spiders. It is used to optimize RF parameters, ensuring high classification accuracy and preventing overfitting in dynamic environments.
*   **Classification Levels:** The model categorizes channel quality into four distinct levels: Failed, Average, Good, and Excellent.

### 3.2 | Clustering of traffic flows
To avoid the pitfalls of traditional bandwidth allocation (which often ignores individual Traffic Flow (TF) demands), the authors employ the Fuzzy C-Means (FCM) algorithm. FCM is chosen for its fast convergence and simple implementation. It partitions TFs into clusters based on similarity in patterns, allowing the system to allocate different spectrum resources according to the specific needs of each cluster.

### 3.3 | Suggested algorithms for allocating resources
Spectrum fragmentation occurs when available slot blocks are non-continuous or non-aligned, leading to wasted resources and higher blocking probabilities. The authors propose the Fragmentation-Function-Fit (FFF) algorithm to minimize a Global Spectrum Fragmentation (GSF) function. 
The efficiency is measured by an evaluation function $\eta(c)$, which considers total free subcarriers, the number of required subcarriers ($N_m$), the probability of generation ($P_m$), and duration ($t_d(m)$). A higher $\eta(c)$ indicates greater global fragmentation; the FFF algorithm iteratively allocates resources to keep this value low.

### 3.4 | Mechanism for adaptable resource management (DBWO-RF)
The overall mechanism uses shortest path routing combined with the findings from TF clustering and channel quality assessment. Specifically, high-rate TFs—which consume more resources—are prioritized using the FFF approach to minimize their blocking probability. The resulting system is termed the DBWO-RF based resource management approach.

## 4 | Experimental Results
The system was implemented in Python 3.11.4 on a Windows 11 machine (Intel i5, 32 GB RAM). 
*   **Dataset:** 4060 records with 10 features including power consumption, laser bias current, temperature, optical power, and Bit Error Rate (BER) before/after FEC correction. Data was split into 53% training and 47% testing.
*   **Performance:** DBWO-RF achieved a channel quality classification accuracy of 95.3%.
*   **Simulation Topology:** A 13-node NSFNET topology with three data centers and 22 links.
*   **Findings:** 
    *   The FFF technique resulted in lower blocking probabilities than the standalone DBWO-RF at equivalent load levels.
    *   FFF exhibited higher computational complexity (longer running time) compared to DBWO-RF.
    *   DBWO-RF demonstrated superior spectrum resource utilization efficiency, particularly under high load conditions, reaching a maximum effectiveness of 84.1%.

## 5 | Discussion
The authors argue that the novelty of their approach lies in the synergy between SDON, FCM clustering for traffic analysis, and the FFF algorithm for blocking risk reduction. While FFF is effective at reducing blocking, the authors acknowledge its limitations, such as difficulty handling non-linear systems, potential overfitting to specific datasets, and challenges in modeling complex associations between disconnected mechanisms.

## 6 | Conclusion
The integrated DBWO-RF, FCM, and FFF approach successfully optimizes optical network resource scheduling. The method provides a high classification accuracy (95.3%) for channel quality and strong spectrum utilization efficiency (84.1%). While the current study focused primarily on high traffic flow rates—which may limit broader applicability—the authors suggest that future research should expand to various traffic patterns to improve scalability and versatility.
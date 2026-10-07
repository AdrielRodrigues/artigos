---
index_terms:
  - Cloud-Fog Radio Access Networks
  - SDM-EON
  - Latency-Aware Routing
  - Multidimensional Resource Allocation
  - Adaptive Modulation
  - Bandwidth Blocking Ratio
---

# Latency-Aware Routing and Multidimensional Optical Resource Allocation for CF-RAN over SDM-EON

## 1. Introduction
The proliferation of 5G services—such as autonomous vehicles and remote healthcare—demands high throughput and ultra-low latency. While Cloud-Fog Radio Access Networks (CF-RAN) address these needs by distributing processing between fog nodes (near users) and cloud nodes (centralized), managing the underlying optical transport remains a challenge. Traditional Wavelength Division Multiplexing (WDM) lacks flexibility, while Elastic Optical Networks (EONs) and Space-Division Multiplexing EONs (SDM-EONs) offer higher capacity via multi-core fibers but introduce complexities regarding crosstalk and spectrum fragmentation.

The authors identify a gap in existing research: most studies treat CF-RAN processing and SDM-EON resource allocation independently. To bridge this, the paper proposes **5GEON**, an algorithm that jointly manages traffic classification, latency-aware offloading, and multidimensional optical resource allocation to prioritize Ultra-Reliable Low-Latency Communication (URLLC) while maximizing network efficiency via adaptive modulation.

## 2. Related Works
The authors review literature on CF-RAN processing placement and SDM-EON spectrum management. Previous CF-RAN studies often use Integer Linear Programming (ILP) to minimize energy but abstract the optical layer or assume fixed WDM/PON architectures, ignoring spectrum fragmentation. Conversely, SDM-EON research focuses on routing and core selection (e.g., the Smart-Fit policy) to reduce blocking but ignores 5G-specific latency requirements and traffic differentiation. 5GEON is positioned as a unified solution that considers both processing offloading and multidimensional optical constraints.

## 3. 5GEON Algorithm
The 5GEON algorithm aims to maximize successfully established connections in an SDM-EON backbone by integrating traffic class awareness with physical layer constraints.

### 3.1. Network Architecture
The model utilizes a three-layer CF-RAN: 
- **Edge:** Cell Sites (CS) with Remote Radio Heads (RRHs).
- **Fog/Cloud:** Processing nodes where Baseband Units (BBUs) are virtualized. 

Traffic is categorized into three classes: URLLC (highest priority, processed at fog nodes), and eMBB and mMTC (processed at cloud nodes). The optical backbone uses multi-core fibers (7 cores per link, each with 32 frequency slots of 12.5 GHz). To save energy, processing nodes start inactive; the algorithm activates them only when necessary to meet latency constraints while attempting to reuse already active nodes first.

### 3.2. Operations
For every incoming request $\text{r(src, bw, t)}$, 5GEON executes the following:
1. **Modulation Selection:** Evaluates modulation formats based on decreasing spectral efficiency and maximum transmission reach.
2. **Path/Node Determination:** 
   - For URLLC: Finds paths to active fog nodes within a specific latency threshold ($\text{th}_t$) using shortest-path propagation delay. If no active node fits, it activates a new fog node.
   - For eMBB/mMTC: Performs the same process targeting cloud nodes.
3. **Optical Allocation:** Employs a First-Fit strategy for core selection (preferring adjacent cores to keep the center free and minimize crosstalk) and contiguous slot allocation.
4. **Complexity:** The algorithm operates with polynomial complexity, primarily driven by Dijkstra's method $O(|E| + |V| \log |V|)$, making it suitable for dynamic environments.

## 4. Experimental Design

### 4.1. Simulation Environment
Evaluations were conducted using an extended version of *FlexGridSim*. The topology consists of 100 nodes (50 CS, 30 fog, 20 CO) across a $200\text{ km}^2$ urban area. The SDM-EON configuration includes 7 cores per link and slots of 12.5 GHz, supporting modulation formats from 1 to 6 bits/symbol.

### 4.2. Traffic Model
The simulation uses a Poisson arrival process for 10,000 requests with exponential holding times. Each class has distinct constraints:
- **URLLC:** $\text{Latency} < 50\mu \text{s}$, Bandwidth $50/80\text{ Mbps}$.
- **eMBB:** $\text{Latency} < 100\mu \text{s}$, Bandwidth $240/360\text{ Mbps}$.
- **mMTC:** $\text{Latency} < 250\mu \text{s}$, Bandwidth $50/80\text{ Mbps}$.

### 4.3. Performance Metrics
Three metrics are used:
1. **Bandwidth Blocking Ratio (BBR):** The ratio of total blocked bandwidth to requested bandwidth, calculated both overall and per traffic class.
2. **Energy Efficiency (EE):** The ratio of accepted bandwidth to the total energy consumed by transponders, switches, and amplifiers.
3. **Fragmentation Ratio (FR):** A measure of how available frequency slots are distributed; higher values indicate more fragmentation.

### 4.4. Baseline and Evaluation Procedure
5GEON is compared against the TAB-FAA algorithm (a state-of-the-art WDM-based traffic-aware solution) and two internal variants: one with fixed modulation and one with adaptive modulation.

## 5. Results
- **Bandwidth Blocking:** 5GEON significantly outperforms TAB-FAA because it avoids the rigid spectrum partitioning of WDM. The adaptive modulation variant reduces BBR up to three times compared to fixed modulation by optimizing spectral efficiency as network load increases.
- **Traffic Class Impact:** URLLC traffic experiences much lower blocking in 5GEON due to prioritized fog-node offloading and low-delay routing. While eMBB and mMTC have higher blocking due to backhaul contention, adaptive modulation mitigates this effect by packing requests more efficiently.
- **Energy Efficiency:** The adaptive version of 5GEON is the most energy-efficient, as it accommodates more bandwidth without a proportional increase in hardware power consumption. TAB-FAA is the least efficient due to high blocking and underutilized resources.
- **Spectrum Fragmentation:** While higher traffic generally increases fragmentation, the adaptive modulation variant of 5GEON exhibits lower FR than the fixed version because it uses fewer slots per connection through higher-order modulations.

## 6. Conclusions
The paper concludes that joint optimization of routing, processing placement, and multidimensional resource allocation is essential for supporting 5G services over SDM-EONs. The 5GEON algorithm effectively prioritizes URLLC traffic and enhances network capacity via adaptive modulation. Future research directions include adding protection/restoration mechanisms and utilizing machine learning for proactive resource allocation in B5G/6G architectures.
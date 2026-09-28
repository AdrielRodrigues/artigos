---
index_terms:
  - CF-RAN
  - vBBU placement
  - VPON assignment
  - Integer Linear Programming
  - LP relaxation
  - Long Short-Term Memory
  - traffic forecasting
  - network dimensioning
---

# Deep recurrent neural network for optical fronthaul dimensioning and proactive vBBU placement in CF‑RAN

## 1 Introduction
The Cloud Radio Access Network (C-RAN) centralizes baseband processing to reduce CapEx and OpEx, but this creates significant workloads on the fronthaul and cloud facility. While Dense Wavelength Division Multiplexing (DWDM) offers high capacity, it is costly; therefore, Time-and-Wavelength Division Multiplexing Passive Optical Networks (TWDM-PON) are proposed as a lower-cost alternative for the optical fronthaul.

To address centralization bottlenecks, Cloud-Fog RAN (CF-RAN) introduces fog nodes closer to cell sites to offload traffic when the cloud is overloaded. This creates a trade-off between energy consumption (activating more nodes) and network capacity. Managing this requires efficient virtualized Baseband Unit (vBBU) placement and bandwidth assignment (VB-PWA).

The authors identify three ways to solve VB-PWA:
1. **Integer Linear Programming (ILP):** Provides optimal solutions but suffers from poor scalability and high execution times, often making the resulting configuration outdated by the time it is calculated.
2. **Linear Programming (LP) Relaxation:** Reduces computation time via constraint relaxation and rounding but may produce infeasible solutions.
3. **Machine Learning (ML):** Specifically Deep Recurrent Neural Networks (DRNNs), which can predict traffic patterns to enable proactive resource allocation, decoupling the operational timescale from incoming traffic fluctuations.

The paper contributes a DRNN architecture for traffic prediction, an LP relaxation rounding approach, and an analysis of the trade-off between multi-step prediction error and ILP optimality.

## 2 Related Work
Existing research has used ILP and ML for C-RAN resource management, but few address hybrid CF-RAN architectures or specifically evaluate the benefits of proactive ML-based algorithms over reactive ones. While some works use LP relaxation to handle large-scale networks, they often focus on different optimizations like caching or sub-carrier allocation. This study distinguishes itself by comparing three distinct approaches (ILP, LP, and ML) specifically for vBBU placement and VPON assignment in CF-RAN.

## 3 CF‑RAN Operation and System Architecture
### 3.1 Cloud and Fog Processing Layers
CF-RAN utilizes Network Functions Virtualization (NFV) to deploy vBBUs. The **cloud processing layer** handles centralized baseband processing for light traffic loads via a pool of Virtual Digital Units (VDUs) in dedicated servers. The **fog processing layer** consists of smaller nodes closer to Remote Radio Heads (RRHs). When the cloud is overloaded, the orchestrator activates fog nodes to process RRH traffic. Servers are only powered on when actively used to ensure energy efficiency.

### 3.2 The Optical Fronthaul
The fronthaul uses TWDM-PON with three multiplexing levels:
1. **S1 Splitter:** Internal to fog nodes, connecting ONUs via dedicated fibers.
2. **S2 Splitter:** Connects multiple fog nodes to the level 3 splitter.
3. **S3 Splitter:** Forwards traffic from S2 splitters to the cloud-based Optical Line Terminal (OLT).

Virtual PON channels (VPON) allow RRHs to share optical channels via Time Division Multiplexing (TDM), and these channels can be dynamically created or modified based on demand.

### 3.3 The Workload Orchestrator
A centralized software component in the cloud manages energy efficiency by monitoring active RRHs, fronthaul capacity, and node utilization. It prioritizes placing vBBUs in the cloud; if capacity is exhausted, it activates fog nodes and assigns VPONs. Conversely, it deactivates resources when RRHs go offline to save power.

## 4 Problem Statement and Mathematical Formulations for the VB‑PWA Problem
### 4.1 Problem Statement
The Virtual BBU Placement and Wavelength Assignment (VB-PWA) problem aims to allocate one vBBU for every active RRH demand while minimizing the number of activated processing nodes, VDUs, and VPONs. This is modeled as a bin-packing problem where traffic must be fit into the fewest resources possible to reduce power consumption.

### 4.2 ILP Formulation
The authors propose an ILP model with an objective function that minimizes total power costs ($C_n$ for nodes, $C_{lc}$ for line cards, $C_{vdu}$ for VDUs, and $C_{switch}$ for backplane switches). Constraints ensure:
- Every RRH is mapped to exactly one VDU, processing node, and VPON.
- Bandwidth demands do not exceed VPON capacity ($B_w$).
- Processing demands do not exceed node capacity ($P_n$) or VDU capacity ($I_w$).
- Resources (nodes, switches) are only marked as "active" if they are actually hosting a demand.

### 4.3 LP Relaxation
To improve scalability for large networks, the authors use linear relaxation by changing binary variables to continuous or semi-continuous values. The resulting polynomial-time solution is then passed through a rounding function to return it to an integer state. While this may result in slightly higher costs than pure ILP, it drastically reduces computation time.

## 5 ML-based Formulation
The authors use a Long Short-Term Memory (LSTM) network—a type of DRNN—to forecast traffic demands because its memory cells and gating mechanisms can capture non-stationary patterns in time series data. The multivariate LSTM predicts the network load for the next hour using Mean Absolute Error (MAE) as the loss function and ReLU activation. The model achieved an $R^2$ score of 0.95, indicating high accuracy.

### 5.1 Proactive ML Network Resizing
A polynomial-time heuristic is implemented to resize the network based on LSTM predictions:
1. Incoming predicted traffic is first allocated to the cloud node.
2. If cloud capacity is exceeded, the remainder is allocated to fog nodes.
3. Any remaining demand that cannot be accommodated by available resources is blocked.

## 6 Illustrative Numerical Results
Experiments were conducted using the 5GPy simulator across two scenarios: incremental demand growth and business area traffic patterns.

### 6.1 Multi‑step Time Series Forecasting Evaluation
The authors found a direct correlation between prediction windows and error rates. Predicting one hour in advance results in a low MAE (1.19 Gbps), which is compatible with ILP optimality. However, as the prediction interval increases, the error grows significantly, leading to outdated data and suboptimal resource allocation (increased blocking).

### 6.2 Scalability Analysis
Comparison of ILP, LP relaxation, and ML-based solutions shows:
- **Execution Time:** ILP is impractical for large networks (some loads took over an hour to solve), whereas the ML-based heuristic exhibits linear time complexity and is $>99.99\%$ faster than ILP. LP relaxation's runtime is much lower than ILP but higher than ML.
- **Resource Consumption:** ILP consumes the most CPU and memory, both increasing sharply with network size. The ML-based approach maintains stable and minimal memory usage $(\approx 44\%)$.

#### 6.2.1 One-day Traffic Forecasting
In static evaluations, the "gap" (difference from optimal) between LP relaxation and ILP was near zero, confirming that LP is a viable alternative for optimality. The ML-based heuristic also showed low disparity from ILP results while maintaining superior computational efficiency.

### 6.3 Dynamic Traffic Scenarios
Using business area traffic patterns, the authors observed that the ML-based approach's energy consumption and node activation rates were statistically equivalent to those of the optimal ILP solution. However, the ML approach maintained significantly lower CPU intensity throughout the simulation.

## 7 Conclusion
The study demonstrates that while ILP provides the optimal configuration for vBBU placement and VPON assignment in CF-RAN, its scalability is poor. LP relaxation serves as a fast, near-optimal alternative, but the proposed ML-based proactive heuristic is the most efficient. The LSTM-driven approach allows the network to resize itself based on future demands with minimal computational overhead and near-optimal power consumption. Future work will explore Deep Reinforcement Learning for further improvement.
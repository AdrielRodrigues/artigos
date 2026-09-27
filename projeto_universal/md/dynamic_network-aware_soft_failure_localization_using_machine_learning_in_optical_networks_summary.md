---
index_terms:
  - soft failure localization
  - optical transport networks
  - graph neural networks
  - gNMI/gRPC telemetry streaming
  - ONF-TAPI
  - unsupervised machine learning
  - partially disaggregated networks
---

# Dynamic network-aware soft failure localization using machine learning in optical networks

## 1. Introduction
The authors address the complexity of managing soft failures (SF) in partially disaggregated optical transport networks, where multi-vendor environments and dynamic reconfigurations make traditional monitoring difficult. While hierarchical software-defined networking (SDN) controllers use standardized models like ONF-TAPI to manage domain controllers, visibility into the data plane (DP) for the management plane (MP) remains limited. Current telemetry protocols such as SNMP, NETCONF, and RESTCONF are criticized for being text-based, verbose, and inefficient.

The paper proposes a hybrid machine learning (ML) framework combined with an end-to-end gNMI/gRPC-based telemetry streaming solution using the ONF-TAPI YANG data model. This approach utilizes distributed unsupervised ML for per-device anomaly detection and an inductive Graph Neural Network (GNN) for SF classification and localization, allowing the system to adapt to topology changes without constant retraining.

## 2. State of the Art
Existing research in optical network automation covers resource allocation, fault prediction, and telemetry streaming. However, gaps exist regarding data plane visibility within partially disaggregated architectures and the ability of ML models to handle dynamic topologies (e.g., spectrum defragmentation or node additions). Most existing GNN-based localization methods assume a fixed topology or rely on alarm triggers rather than proactive performance monitoring.

## 3. Background

### A. Challenges in Monitoring a Partially Disaggregated Network
Vendor-specific proprietary YANG models hinder interoperability. While partially disaggregated architectures (where OLS domain controllers are managed by a hierarchical SDN controller) mitigate some issues, the MP still suffers from limited transparency regarding DP state and performance monitoring (PM) data. The authors argue that gRPC is superior to NETCONF and RESTCONF due to its binary serialization and efficient subscription-based streaming model.

### B. Challenges in Soft Failure Localization
Soft failures degrade quality of transmission (QoT) gradually without triggering hard alarms, making them difficult to detect with vendor-defined global thresholds. Monitoring multiple key performance indicators (KPIs) is necessary but complex due to varying data distributions and the lack of labeled training sets for dynamic networks. Furthermore, because failure in one component often causes sequential deviations across nodes, identifying root causes requires modeling node relationships—a task complicated by network dynamicity.

## 4. Proposed Framework: Telemetry Streaming and Soft Failure Localization

### A. E2E Streaming Telemetry Solution
The proposed solution replaces traditional protocols with gNMI/gRPC based on HTTP/2 and protocol buffers for efficient data transport.

#### 1. Southbound: Between DP and CP Components
A telemetry agent (gRPC client) subscribes to PM data from devices (gRPC servers) using XPath definitions. This subscription model reduces uplink traffic compared to the polling mechanism of NETCONF, with smaller payload sizes for both requests and responses.

#### 2. Northbound: Between CP and MP Components
To ensure multi-domain visibility, the authors utilize a unified ONF-TAPI v2.5.1 data model. The telemetry agent in the control plane (CP) acts as a `tapi-gnmi-streaming` server. This allows the management plane (MP) to use a TAPI gNMI/gRPC client to collect PM data into a time-series database, significantly reducing the overhead and latency associated with RESTCONF's verbose JSON format.

### B. Failure Identification Using Unsupervised ML
To avoid reliance on labeled datasets and handle varying KPI distributions, the framework uses distributed unsupervised learning at the device level.

#### 1. OPTICS-Based Anomaly Detection
The authors employ the Ordering Points To Identify the Clustering Structure (OPTICS) algorithm. PM data is normalized using min-max scaling to prevent high-magnitude KPIs from skewing distance calculations.
*   **Mechanism:** The algorithm defines neighborhoods based on a radius ($\varepsilon$) and minimum points ($\zeta$), calculating core and reachability distances. A threshold reachability value ($T$) is established; if new live data exhibits a reachability distance greater than $T$, it is flagged as an anomaly.
*   **Application:** This process identifies four SF types: launch power degradation (terminals), booster amplifier attenuation, amplifier gain degradation, and WSS attenuation. The output for each device is a one-hot encoded vector representing the status of its KPIs.

### C. Failure Localization Using a GNN
The framework uses a two-step process: first identifying anomalies via OPTICS, then classifying the failure type using a GNN.

#### 1. Graph Neural Network—Graph Attention Network (GNN-GAT)
This model uses an attention mechanism to aggregate data from neighboring nodes, weighting their contributions based on learned importance ($\alpha_{ij}$). Features are updated and passed through max-pooling and a fully connected neural network (FCNN). However, GNN-GAT is limited by its reliance on a fixed adjacency matrix, requiring expensive retraining when the topology changes.

#### 2. Graph Neural Network—Sample, Aggregate, and Temporal (GNN-SAT)
To support dynamic networks, the authors propose GNN-SAT:
*   **Sampling/Aggregation:** A node-centric attention mechanism focuses only on nodes exhibiting anomalies and their immediate neighbors, forming a standard matrix based on the *current* adjacency matrix. This makes it inductive and topology-aware in real-time.
*   **Temporal Analysis:** To capture behavior preceding a failure, the model uses convolution layers for spatial feature extraction followed by Long Short-Term Memory (LSTM) layers to process temporal patterns. 
*   **Classification:** The LSTM output is passed to an FCNN to determine the SF label distribution.

## 5. Evaluation
Experiments were conducted on a testbed with two OLS domains in a ring topology, utilizing the TeraFlowSDN controller.

### A. Telemetry Streaming
The gNMI/gRPC approach significantly outperformed text-based protocols:
*   **Southbound:** Traffic load was reduced by 94.2% (uplink) and 82.3% (downlink) compared to NETCONF.
*   **Northbound:** gRPC reduced traffic by 60.6% to 87.6% compared to RESTCONF.
*   **Overall:** End-to-end telemetry traffic load was reduced by 78.4%.

### B. Failure Identification Using OPTICS
The model successfully detected gradual deviations in KPIs (approx. 0.3 dBm/dB). The True Positive Rate (TPR) stabilized with training sizes above 600 samples, using $T=0.4$. The distributed nature is highly scalable; monitoring 25 devices consumed only ~3.7% CPU and 2.14 GB of RAM.

### C. Failure Localization Using a GNN
GNN-SAT was compared against GNN-GAT across several metrics:
*   **Accuracy:** GNN-SAT achieved 97.6% accuracy, significantly higher than GNN-GAT (~84%).
*   **Dynamicity:** GNN-SAT maintained high accuracy when virtual nodes were added without requiring retraining.
*   **Proactivity:** Due to the LSTM module, GNN-SAT could anticipate SFs before they fully manifested by learning temporal KPI deviations.
*   **Efficiency:** GNN-SAT's processing time was ~15.28 ms, compared to ~57 ms for GNN-GAT, as it only processes affected regions rather than the entire graph.

## 6. Conclusion
The paper demonstrates that combining a unified ONF-TAPI gNMI/gRPC streaming solution with a hybrid ML framework enables efficient and robust soft failure localization in partially disaggregated optical networks. The use of distributed OPTICS for anomaly detection and an inductive GNN-SAT model ensures the system remains accurate and computationally efficient even during dynamic network reconfigurations.
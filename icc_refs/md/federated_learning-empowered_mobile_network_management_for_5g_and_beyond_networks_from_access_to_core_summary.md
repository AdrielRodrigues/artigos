---
index_terms:
  - federated learning
  - 5G and 6G networks
  - network management
  - NWDAF
  - distributed artificial intelligence
  - radio resource management
  - non-IID data
---

# Federated Learning-Empowered Mobile Network Management for 5G and Beyond Networks: From Access to Core

## I. Introduction
The transition to 5G and beyond involves integrating communication and computing via virtualization (SDN, NFV, network slicing) and ultra-dense networks (mmWave, THz). These advancements increase the complexity of resource management and orchestration. While AI/ML can automate these processes, traditional centralized training is hindered by enormous network resource consumption and data security risks. 

Federated Learning (FL) is proposed as a distributed alternative where network functions (NFs) train models locally and only exchange parameters. This approach provides three primary advantages:
- **Network Efficiency:** Reduces data transmission by sending model updates instead of raw data.
- **Privacy:** Keeps sensitive data in local storage, minimizing leakage during multi-tenant management.
- **Low Latency:** Enables real-time decision-making through local inference using a global model.

## II. FL: State of the Art

### A. Key Concept of FL
FL allows multiple participants to collectively build a global model without centralizing data. The process follows three steps: 1) Task initialization and participant selection by a central server; 2) Local training on local datasets to minimize loss functions; and 3) Global aggregation (e.g., via FedAvg, Secure Aggregation, or Differential Privacy) to generate an updated global model. This cycle repeats until convergence.

### B. FL Classifications
FL is categorized across three dimensions:
- **Networking Structure:** Centralized FL (CFL) uses a single server; Decentralized FL (DFL) utilizes P2P architectures or blockchain; Hierarchical FL (HFL) employs intermediate aggregation nodes to reduce communication costs and handle non-IID data.
- **Synchronization Approach:** Strong synchronization requires all participants to sync before aggregation; Asynchronous FL allows independent updates to eliminate "stragglers"; Weak synchronization uses varying update frequencies.
- **Data Partitioning:** Horizontal FL involves different samples with the same features; Vertical FL involves the same samples with different features; Federated Transfer Learning (FTL) handles both different samples and different features.

### C. Hardware Architecture
To handle the computational load of local training on limited edge devices, specialized accelerators are used:
- **GPUs:** High throughput but high power consumption.
- **FPGAs:** More energy-efficient than GPUs but require significant storage and bandwidth.
- **ASICs (e.g., EdgeTPU):** Maximum efficiency and speed, though they lack flexibility and have longer development cycles.

### D. Networking Requirements
The primary bottleneck in FL is networking delay (uplink/downlink). Factors like model size and number of participants increase interference and reduce per-user bandwidth. Solutions include gradient compression, efficient participant selection, and over-the-air computation.

### E. FL Management
FL management focuses on optimizing the tradeoff between convergence time, energy consumption, and prediction accuracy. Key decision variables include the set of participating nodes, data utilization levels, and resource configurations (CPU frequency, power). Common solving methods range from convex optimization and greedy heuristics to reinforcement learning (RL) and game theory.

## III. AI-Empowered Mobile Network Management

### A. Background Information About 5G and Beyond Networks
5G utilizes Protocol Data Unit (PDU) sessions and a service-based architecture consisting of virtualized NFs: Access and Mobility Management Function (AMF), Session Management Function (SMF), and User Plane Function (UPF). These are often deployed as containers in Kubernetes. Towards 6G, the ITU-T envisions integrated AI for ubiquitous connectivity and sensing.

### B. Standard Activities for AI-Empowered Mobile Network Management
- **Access Network:** The O-RAN alliance introduces RAN Intelligent Controllers (RICs)—non-real-time and near-real-time—to automate tasks via xAPPs (e.g., traffic steering, SLA assurance). 3GPP research focuses on AI for energy saving, load balancing, and mobility optimization.
- **Core Network:** The 3GPP NWDAF (Network Data Analytics Function) provides analytics for control-plane functions. MDAF handles management data in the OAM domain. ETSI's Zero-touch network management promotes closed-loop automation.

### C. AI-Empowered Network Load/Status Prediction
Prediction methods are categorized as:
- **Simple:** Historical averaging (e.g., EWMA).
- **Parametric:** Statistical models (e.g., ARIMA, Markov models) that assume specific probability distributions.
- **Non-parametric:** Deep learning (e.g., LSTM for temporal patterns, CNNs for spatial patterns). 
Applications include "BS sleeping strategies" to reduce power during off-peak hours and adaptive streaming based on throughput prediction.

### D. AI-Empowered Networking Resource Management
RL and Deep RL (DRL) are used for non-convex problems like power control, rate adaptation, and RB allocation in RAN slicing. Other applications include DRL-based handover management to minimize energy/drops and MDP-based inactivity timer management for PDU sessions.

### E. AI-Empowered Computing Resource Management
This focuses on vertical scaling (adjusting CPU/RAM) and horizontal scaling (adding/removing instances). AI is used for UPF instance scaling, NF placement via multi-objective integer linear programming, and slice admission control to maximize operator revenue.

### F. Industry or Implementation Activities for AI-Empowered Mobile Network Management
Industry leaders (Ericsson, Nokia, Guavus) have implemented NWDAF solutions. Academic projects like OREOS focus on end-to-end orchestration for critical services, while the POWER project explores hierarchical edge-cloud architectures using FL.

## IV. FL-Empowered Mobile Network Management

### A. Distributed NWDAF for FL-Empowered Mobile Network Management
To enhance security, a distributed NWDAF architecture is proposed featuring root and leaf NWDAFs. Leaf NWDAFs perform local training on data from associated NFs, while the root NWDAF aggregates these models. This isolates sensitive data and prevents intervention by unauthorized entities.

### B. FL-Empowered Network Load/Status Prediction
Traffic prediction in wireless networks faces non-IID (non-Independent and Identically Distributed) data challenges. Proposed solutions include:
- **Clustering:** Grouping BSs by location or traffic patterns to enhance convergence (e.g., FedDA).
- **Meta-Learning:** Creating personalized models for heterogeneous datasets.
- **Specialized Models:** BiLSTM for computation offloading prediction and FPLSTM for multi-slice forecasting among MVNOs.

### C. FL-Empowered Networking Resource Management
FL enables collaboration between operators (MVNOs) without sharing raw data. Examples include federated DRL for bandwidth allocation in O-RAN architectures and the use of Shapley values in Vertical FL to reduce communication overhead during UE access control updates.

### D. FL-Empowered Computing Resource Management
Applications include:
- **Autoscaling:** Using FL for time-series forecasting of NF instances across multi-domain networks.
- **Decentralization:** Implementing fully decentralized AI engines (DFL) via P2P to remove the central server bottleneck.
- **Security/Anomaly Detection:** Hierarchical FL and GANs are used to detect VM anomalies in network slices.
- **Caching:** Using FL for content popularity prediction and cooperative caching on MEC servers.

### E. Architecture or Implementation Activities for FL-Empowered Mobile Network Management
Implementations include Kubernetes orchestration prototypes using WebSocket or Apache Kafka pipelines. Blockchain is integrated with FL (e.g., Skunk's system) to eliminate single points of failure, provide immutability, and ensure trust in UAV orchestration and IoT attack detection.

## V. Lessons Learned

### A. Lessons Learned From AI-Empowered Mobile Network Management
Standardization is progressing toward end-to-end automation (NWDAF/MDAF), but practical deployment of DL models is hindered by the need for massive datasets, leading to privacy and scalability bottlenecks. DRL is powerful for sequential decisions but suffers from "cold-start" issues.

### B. Lessons Learned From FL-Empowered Mobile Network Management
Distributed NWDAF effectively balances security and intelligence. In traffic prediction, clustering (HFL) is the most effective way to handle non-IID data. In networking resource management, federated DRL enables multi-operator cooperation, but convergence solutions for unbalanced data are still lacking. A significant remaining challenge is the computational burden FL places on battery-constrained UEs.

## VI. Research Challenges and Directions

### A. Practical Deployment Issues
There is a need for standardized interfaces for NWDAF interoperability and further research into Vertical FL (combining different NF features for one user). Additionally, Explainable AI (XAI) must be integrated to make "black-box" FL decisions transparent and trustworthy for operators.

### B. Scalability Issues
To handle heterogeneous computing capabilities:
- **HFCL:** Hybrid architectures that combine centralized learning (for low-power nodes) and FL (for high-power nodes).
- **DFL:** Fully decentralized frameworks to remove central server dependencies.
- **SFL (Split FL):** Splitting models between clients and servers to reduce the local computational burden, especially for UAVs.

### C. Privacy and Security Issues
While FL is inherently more private, model updates can still leak data. Research directions include differential privacy and anti-jamming schemes (e.g., frequency hopping) or blockchain auditing to prevent "poisoning" attacks from malicious nodes.

### D. OPEX Issues
Reducing operating expenses requires energy-efficient FL through:
- **Dynamic Control:** Adjusting local iterations and participant selection.
- **SNNs:** Replacing deep neural networks with Spiking Neural Networks for brain-like, low-energy training.
- **Compression:** Implementing accuracy loss correction and model compression for wireless links.

### E. Federated Reinforcement Learning (FRL)
FRL is needed to improve sample efficiency in large action/state spaces. While horizontal FRL (sharing experiences among similar agents) is explored, vertical FRL (integrating different feature sets into a shared policy) remains an open research area for mobile network management.

## VII. Conclusion
The paper concludes that FL provides a viable path toward scalable and secure AI-empowered network management in 5G/6G, provided the challenges of non-IID data, computational overhead on devices, and model transparency are addressed through hierarchical architectures, SFL, and XAI.
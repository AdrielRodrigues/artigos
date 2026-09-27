---
index_terms:
  - Zero-Touch Network and Service Management
  - Automated Machine Learning
  - Network Digital Twins
  - 5G+ Network Automation
  - Intent-Based Networking
  - Next-Generation Networks
---

# Zero-touch networks: Towards next-generation network automation

## 1. Introduction
Next-Generation Networks (NGNs), including 5G and 6G, enable critical service areas such as enhanced Mobile Broadband (eMBB), ultra-Reliable Low-Latency Communication (uRLLC), and massive Machine-Type Communication (mMTC). To support these, infrastructures must be flexible and programmable via Software Defined Networking (SDN), Network Function Virtualization (NFV), and Multi-access Edge Computing (MEC). However, the resulting complexity makes manual management prone to error and inefficient. 

Zero-Touch Networks (ZTN) and the Zero-touch network and Service Management (ZSM) framework address this by enabling self-management and self-healing with minimal human intervention. While ZSM relies heavily on Machine Learning (ML), it faces challenges in feature engineering and model tuning. This paper proposes integrating Automated ML (AutoML) and Network Digital Twins (NDTs) to streamline the ML pipeline, reduce operational costs, and provide a risk-free environment for testing network configurations.

## 2. List of acronyms
This section provides a comprehensive glossary of terms spanning Artificial Intelligence (AI), performance metrics, network management, next-generation network components (e.g., gNB, UPF, NWDAF), security threats (e.g., DDoS, MitM), and relevant standardization organizations (e.g., ETSI, 3GPP, ITU).

## 3. Background
### 3.1. Artificial Intelligence and machine learning paradigms
AI simulates human intelligence, while ML allows machines to learn patterns from data. The paper categorizes ML into three types:
- **Supervised Learning (SL):** Uses labeled data for prediction; includes linear regression, SVM, and Deep Learning (CNNs for images, RNNs/LSTMs for sequences).
- **Unsupervised Learning (UL):** Identifies patterns in unlabeled data; includes K-means clustering and Principal Component Analysis (PCA).
- **Reinforcement Learning (RL):** An agent learns through trial and error to maximize a reward signal. Deep RL (DRL) combines this with neural networks for high-dimensional state spaces.

### 3.2. Software defined network
SDN decouples the control plane (centralized logic/controller) from the data plane (physical switches), enabling programmable, dynamic resource allocation and reduced deployment time through softwarization.

### 3.3. Network function virtualization
NFV decouples network functions (e.g., firewalls) from proprietary hardware, implementing them as Virtual Network Functions (VNFs) on commercial off-the-shelf servers via VMs or containers, increasing scalability and reducing CAPEX/OPEX.

### 3.4. Advancing mobile connectivity: From 5G to beyond
5G focuses on high speed, low latency, and massive connectivity. Beyond 5G (6G) aims for a leap in performance: data rates up to 1 Tbps, sub-millisecond latency (10–100 $\mu$s), and device density of $10^7/km^2$. 6G will integrate terahertz communication and advanced network intelligence.

## 4. Zero-touch network and service management overview
### 4.1. Need for ZSM in 5G+ networks
The shift to softwarized, virtualized architectures creates immense complexity that traditional static Management and Orchestration (MANO) cannot handle. ZSM enables "Self-X" operations (self-configuration, monitoring, healing, and optimization) to ensure end-to-end Quality of Experience (QoE).

### 4.2. Current standard — ETSI ZSM
ETSI ZSM aims for full E2E automation across multi-domain environments, covering the lifecycle from design and planning to monitoring and optimizing.

#### 4.2.1. Key architecture principles
The architecture is modular and scalable, utilizing "service composability." It separates concerns between Management Domains (MD) for local resources and E2E cross-domain service management for orchestration across MDs. It utilizes closed-loop automation and intent-based interfaces to achieve objectives without external disruption.

#### 4.2.2. Architecture requirements
Requirements are divided into three categories:
- **Non-functional:** Availability, energy efficiency, vendor independence, and high data availability.
- **Functional:** Support for cross-domain management, closed-loop control, real-time data collection, and automated overload handling.
- **Security:** Data protection at rest and in transit, privacy-by-design, and the ability to automatically detect and mitigate attacks on ML/AI components.

#### 4.2.3. Reference architecture
The framework integrates MDs (handling local physical/virtual resources), an E2E service MD for cross-domain orchestration, and cross-domain data services for global optimization. Management functions within these domains include data collection, intelligence, analytics, control, and orchestration services.

### 4.3. Intents
Intents are high-level business objectives (e.g., "Ensure low latency for VR") that abstract away procedural configuration details. They allow administrators to define a desired state using domain-specific languages, which the system then translates into technical configurations.

#### 4.3.1. Attributes & benefits of network intents
Intents are hardware-independent, contextual, and persistent. Key benefits include improved accuracy (reduced human error), efficiency through automation, enhanced scalability, and easier regulatory compliance.

#### 4.3.2. Example use case: Intent-based approach for configuring a 5G network to support a virtual reality service
In a VR scenario, an intent would specify requirements like "1 Gbps bandwidth" and "5 ms latency," alongside a policy to prioritize this traffic over others. The ZSM system automatically translates these goals into resource allocations without manual switch configuration.

#### 4.3.3. Standardization efforts
Various bodies are standardizing intents: ONF (NorthBound Interface), 3GPP (TR 28.812 for intent-driven management), ETSI (policy-driven orchestration), and IETF/IRTF (Autonomic Networking). Modern advances use Natural Language Processing (NLP) via BERT to translate human language into executable network commands.

#### 4.3.4. Use of intents in the ZSM framework
Intents serve as the primary communication method between humans and the system, and between different management layers. The paper discusses frameworks like CLARA and others that use closed-loop control to monitor network state and adjust configurations automatically to align with specified intents.

### 4.4. Related projects
Several initiatives complement ZSM:
- **IETF AINEMA:** A flexible AI framework for E2E network management.
- **ITU-T SG13:** Standards for AI-based automation in future networks (Recommendation Y.3177).
- **ETSI ENI:** Focuses on cognitive network management and SLA management.
- **TM Forum ZOOM & ODA:** Aims for zero-touch orchestration via open APIs and cloud-native blueprints.
- **EU Horizon 2020 (MonB5G, Hexa-X):** Focuses on distributed slice management and the architectural foundation for 6G.

### 4.5. Zero-touch network operations
Zero-Touch Network Operation (ZNO) applies ZSM to four main areas:
1. **Resource Management:** Dynamic allocation via ML and MEC.
2. **Traffic Control:** Predictive classification and intelligent routing.
3. **Energy Efficiency:** Adapting power use based on real-time demand.
4. **Security & Privacy:** Automated threat detection and response.

## 5. Network resource management
### 5.1. Dynamic resource allocation
DRL is used to solve complex optimization problems in radio resource allocation (e.g., in WLANs) and VNF placement. DRL agents can be trained on Digital Twins to avoid risky configurations on live networks. Case studies show DRL reduces E2E latency and SLA violations for uRLLC services compared to baseline rejection-based methods. Additionally, Autonomous Profiling (NAP) is used to predict performance metrics for untested resource configurations in NFV orchestration.

### 5.2. Network slicing
Network slicing creates virtual networks on a single physical infrastructure. Challenges include the complexity of orchestrating slices as they scale and ensuring isolation. Solutions include RL-based demand prediction for dynamic allocation and the HARNESS system, which ensures high availability for eMBB, uRLLC, and mMTC slices by intelligently handling control plane requests.

### 5.3. Multi-access edge computing
MEC reduces latency by processing data near the user. ZSM integrates with MEC to enable automated healing (detecting faulty links via ML) and optimized service execution placement using algorithms like Vectorial Successive Shortest Path (VSSP), which considers multiple technical dimensions (storage, throughput).

## 6. Network traffic control
### 6.1. Traffic prediction & classification
ZSM uses ML/DL to forecast traffic patterns and categorize flows (e.g., video vs. data). While SVMs show higher accuracy than K-means for labeled data, LSTMs and GRUs are superior for time-series forecasting of cellular traffic due to their ability to handle temporal dependencies.

### 6.2. Intelligent routing
Intelligent routing replaces manual configuration with autonomous paths. The EARS architecture uses DDPG (DRL) to optimize throughput and delay in SDN. In FANETs (drones), DQN is used for vertical routing to improve energy efficiency and reduce link breakages. For V2X, group-based routing combined with 3D beam alignment ensures stability in mmWave 5G systems.

## 7. Towards energy efficiency
Energy efficiency is critical as 5G/6G infrastructure expands. Strategies include "green" radio access technologies and the use of laZSM to automate power scaling. The SCHE2MA framework uses distributed RL for energy-aware deployment of service function chains, reducing latency while improving energy efficiency by 17.1% over centralized solutions. KB5G employs Actor-Critic methods to minimize VNF instantiation costs and energy consumption.

## 8. Network security & privacy
### 8.1. Safeguarding 5G+ networks: Security measures & weaknesses
The distributed nature of 5G+ increases the attack surface across five domains: User Equipment (botnets), RAN (rogue base stations/MitM), Core Network (SDN/VNF hijacking), Slicing (isolation breaches), and SDN (Topology Poisoning).

### 8.2. ZSM security threats
Automation introduces new risks: Open APIs are vulnerable to SQL injection and DoS; Intents can be intercepted (Data Exposure); Closed-loops can be manipulated via Deception Attacks; and ML models are subject to Adversarial, Model Extraction, and Model Inversion attacks.

### 8.3. Advances in 5G+ network trust management
Trust is enhanced using:
- **Blockchain:** Ensures data integrity in ML pipelines through tamper-evident logs.
- **MUD & TRM:** Manufacturer Usage Description (MUD) defines normal device behavior, while Trust and Reputation Managers (TRM) audit infrastructure.
- **Federated Learning:** Allows anomaly detection without centralizing sensitive raw data, improving privacy.

## 9. Zero-touch network enablers/solutions
### 9.1. AI/ML challenges
Traditional ML in ZSM is hindered by: the need for high expertise; massive volumes of uncleaned data; difficulty in selecting the optimal model from many architectures; intensive hyperparameter tuning; and the volatile nature of wireless environments.

### 9.2. Digital twins
A DT is a real-time digital replica of a physical system with bidirectional data flow. It allows "what-if" analysis, risk-free testing, and remote monitoring. Enablers include IoT sensors, cloud computing for storage, and high-performance connectivity to synchronize the virtual and physical worlds.

### 9.3. Network digital twins
NDTs mirror telecom infrastructure to optimize planning and troubleshooting without risking live traffic.

#### 9.3.1. Applications
Applications include online optimization (load balancing), troubleshooting (replicating past failures), what-if analysis (testing disaster scenarios), and strategic planning (predicting resource exhaustion).

#### 9.3.2. Standardization efforts
Standardization is underway via ISO/IEC (manufacturing DTs), IEEE (digital representation of objects), ITU-T (Y.3090 for NDT requirements), and IETF (NDT reference architectures).

#### 9.3.3. Advancements in network digital twins
Recent work includes using DTs to manage metasurface reflectors in 6G THz communications and integrating AutoML with DTs for efficient IDS synchronization in resource-constrained environments. Graph Neural Networks (TwinNet) have also been used to estimate E2E path delays across unseen topologies with high accuracy.

### 9.4. Automated machine learning
AutoML automates the ML pipeline, democratizing AI by reducing the need for data science expertise.

#### 9.4.1. Automated data preprocessing
AutoML handles:
- **Transformation:** Target encoding categorical features.
- **Imputation:** Using model-based (K-NN, XGBoost) or model-free methods to fill missing values.
- **Balancing:** Under/over-sampling to fix class imbalance.
- **Normalization:** Z-score and Min-Max scaling for feature comparability.

#### 9.4.2. Automated feature engineering
This involves automated generation (creating new features), selection (filter, wrapper, or embedded methods), and extraction (e.g., PCA) to optimize the feature set for model performance.

#### 9.4.3. Automated model learning
AutoML uses search algorithms (Grid Search, Random Search, Bayesian Optimization, Hyperband) to find the best model architecture and hyperparameters. It then trains models using advanced optimizers (Adam, SGD) and regularization to prevent overfitting.

#### 9.4.4. Automated model updating
To combat **Data Drift** (distribution shift) and **Concept Drift** (task change), AutoML employs:
- **Detection:** Distribution-based (Kolmogorov–Smirnov test) or performance-based (windowed tracking).
- **Adaptation:** Incremental updates, full retraining, transfer learning, or ensemble methods.

### 9.5. Surveying current trends in AutoML applications
AutoML is applied to cybersecurity for DDoS detection and intrusion detection (IDS), where it dynamically selects the best algorithm based on node power levels and traffic payloads to maintain efficiency in sensor networks.

## 10. Case study: Online AutoML for application throughput prediction
### 10.1. Use case overview
Predicting application throughput is critical for ensuring QoE in 5G+ services (e.g., Netflix). ZSM can use these predictions to scale resources proactively. The study simulates a scenario where traffic congestion causes model drift, necessitating an online AutoML update.

### 10.2. Dataset overview
The authors used a production dataset from an Irish mobile operator capturing 4G/5G traces for video streaming and file downloads, including KPIs like RSRP, RSRQ, and DL_bitrate.

### 10.3. Dataset distribution
Analysis of the data reveals that throughput distributions are generally consistent across days but vary by hour (e.g., skewed towards low values in early morning), highlighting the need for time-aware models.

### 10.4. AutoML framework
The pipeline performs preprocessing $\rightarrow$ feature engineering (using LightGBM importance and Pearson's rank) $\rightarrow$ model learning. It utilizes a **Seq2Seq LSTM** architecture (Encoder-Decoder) optimized via Bayesian optimization. Drift is detected using a windowed performance-based approach; if MAE exceeds a dynamic threshold, the model weights are incrementally updated.

### 10.5. 5G system architecture
The proposed architecture introduces an **Application Edge Slice (AES)** in the RAN to collect traffic data and run the AutoML pipeline locally. Predictions are sent to the Network Data Analytics Function (NWDAF), which informs ZSM decisions for resource allocation via the NSSF and NSSMF.

### 10.6. Results and analysis
#### 10.6.1. AutoML vs. Traditional ML
AutoML with Seq2Seq significantly outperformed traditional LSTM and basic Seq2Seq models across all datasets (4G/5G, streaming/downloads). In 5G file downloads, AutoML reduced MAPE to 3.58% compared to 4.76% for the manual Seq2Seq model.

#### 10.6.2. Complexity-accuracy trade-off analysis
Increasing the "look-back" window (past data) improves accuracy but increases computational cost. Similarly, predicting longer "look-ahead" sequences increases error (MAE), requiring more historical data to maintain precision.

#### 10.6.3. Periodic AutoML model drift monitoring
Simulated data drift caused MAE to spike; the system detected this at the next periodic check (every 10 min) and updated weights, successfully bringing the MAE back down. This demonstrates a trade-off between monitoring frequency and computational overhead.

## 11. Open challenges & future directions
### 11.1. ZSM challenges
#### 11.1.1. Explainable zero-touch management
The "black box" nature of AI is problematic for critical services (e.g., remote surgery). XAI is needed to provide rationales for decisions via interpretable models or post-hoc explanation metrics.

#### 11.1.2. Trustworthy ZSM
Sharing sensitive topology data between operators requires trust mechanisms like Blockchain, TEEs (Trusted Execution Environments), and robust encryption.

#### 11.1.3. Computational complexity in ZSM
Real-time analysis of massive volumes of NGN data is resource-intensive. Future work should explore hardware acceleration (FPGA/GPU) to reduce latency.

### 11.2. AutoML challenges
#### 11.2.1. Interpretability
AutoML often prioritizes accuracy over transparency. Incorporating causality constraints and XAI paradigms (e.g., SHAP, LIME) is necessary for regulatory compliance.

#### 11.2.2. Scalability
The volume of network data can make exhaustive model searching slow. Parallel/distributed algorithms and efficient data sampling are required.

#### 11.2.3. Robustness
AutoML models are vulnerable to adversarial attacks (noise injection). Defensive distillation and adversarial training are proposed solutions.

#### 11.2.4. Cold-start
Initial search processes can be inefficient. Meta-learning, transfer learning from pre-trained models, and integrating domain-specific knowledge can "warm-start" the process.

## 12. Conclusion
ZSM and AutoML represent a paradigm shift toward fully autonomous 5G+ networks. While ZSM provides the framework for self-management, AutoML solves the operational hurdles of ML implementation (tuning/selection), and NDTs provide a safe environment for optimization. The presented case study proves that an online AutoML pipeline can effectively predict application throughput and adapt to network drift, enhancing overall service quality and operational efficiency.
---
index_terms:
  - Open RAN
  - Deep Reinforcement Learning
  - Colosseum Emulator
  - xApps
  - Closed-Loop Control
  - RAN Slicing
---

# ColO-RAN: Developing Machine Learning-Based xApps for Open RAN Closed-Loop Control on Programmable Experimental Platforms

## 1 Introduction
Modern cellular networks require flexibility to handle heterogeneous constraints (e.g., URLLC for autonomous driving vs. high data rates for multimedia). This requires three elements: programmable virtualized stacks, closed-loop control, and data-driven ML. The O-RAN architecture enables this by introducing a RAN Intelligent Controller (RIC) that executes custom logic via xApps.

However, the adoption of Deep Reinforcement Learning (DRL) in RAN is hindered by five main challenges:
1. Difficulty collecting large-scale datasets representing real-world randomness.
2. Lack of scale for testing ML robustness to avoid network outages.
3. Unreliable or inconsistent telemetry data from production systems.
4. Limited generalization of agents to unseen configurations.
5. High dimensionality and the need for meaningful feature selection among hundreds of KPMs.

The paper introduces **ColO-RAN**, a large-scale O-RAN testing framework integrating O-RAN components with the Colosseum wireless emulator, serving as a "wireless data factory." The authors develop three DRL xApps for RAN slicing and scheduling and evaluate them on a 49-node network across both Colosseum and the Arena indoor testbed.

## 2 Machine Learning for the Open RAN
ML deployment in O-RAN follows a five-step pipeline: (1) data collection via the O1 interface $\rightarrow$ (2) model design $\rightarrow$ (3) offline training/testing $\rightarrow$ (4) packaging as an xApp $\rightarrow$ (5) runtime inference and control via the E2 interface.

### 2.1 O-RAN Overview
O-RAN disaggregates the base station into Central Units (CU), Distributed Units (DU), and Radio Units (RU). It introduces two RICs:
- **Non-Real-Time (non-RT) RIC**: Operates on timescales $>1$ s; handles policy management, training, and SMO.
- **Near-Real-Time (near-RT) RIC**: Operates between 10 ms and 1 s; hosts xApps for load balancing, handover, and slicing policies.

### 2.2 ML Pipelines in O-RAN
The pipeline involves identifying specific RAN parameters to input as observations and those to control as outputs (e.g., scheduling policies). Once trained on curated datasets, models are instantiated in the near-RT RIC to perform real-time closed-loop control based on live network conditions.

## 3 ColO-RAN: Enabling Large-Scale ML Research with O-RAN and Colosseum
ColO-RAN addresses the scarcity of large-scale testing facilities by leveraging a hybrid RF and compute environment.

### 3.1 Colosseum as a Wireless Data Factory
Colosseum is a massive emulator featuring 256 USRP X310 SDRs and a Massive Channel Emulator (MCHEM). MCHEM allows researchers to create high-fidelity "scenarios" using real-world tap data or ray-tracing (e.g., mimicking the city of Rome). This provides a controlled environment to collect full-stack datasets without risking commercial network degradation.

### 3.2 O-RAN-Based Colosseum ML Infrastructure
ColO-RAN implements a lightweight, containerized version of the OSC near-RT RIC using LXC and Docker, removing the need for complex Kubernetes deployments. It connects via an E2 interface to base stations running the SCOPE framework and srsRAN. The system supports three slices—eMBB (video), MTC (sensing), and URLLC (latency)—and allows control over Physical Resource Block (PRB) allocation and scheduling policies (Round Robin, Waterfilling, Proportional Fair).

## 4 xApp Design for DRL-Based Control
xApps in ColO-RAN consist of a RIC interface for ASN.1 encoding/decoding and an ML unit combining autoencoders with DRL agents.

### 4.1 DRL Agent Design
Agents are based on the **Proximal Policy Optimization (PPO)** algorithm using an actor-critic architecture to ensure unbiased policy learning and stability. 
- **Autoencoders**: Used for dimensionality reduction, mitigating outliers, and creating a latent representation of high-dimensional RAN data. They are trained with random zero-padding to remain robust against missing telemetry entries.
- **Specific xApps**:
    - `sched-slicing`: Jointly controls PRBs and scheduling; reward optimizes eMBB rate, MTC packets, and URLLC buffer size.
    - `sched`: Per-slice scheduling policy selection with slice-specific rewards.
    - `online-training`: Fine-tunes pre-trained weights via live exploration on the RAN.

### 4.2 Training the DRL Agents
Offline training is performed using data from various base stations to ensure generalization. The actor and critic networks use five fully connected layers (30 neurons each, tanh activation). The encoder uses four layers (ReLU) to reduce input matrices to a size-3 vector.

### 4.3 Large-Scale Data Collection for ColO-RAN
The authors gathered 3.4 GB of data over 73 hours using a scenario mimicking downtown Rome (7 BS, 42 UEs). Two traffic profiles were used: "slice-based" (heterogeneous rates per slice) and "uniform."

## 5 DRL-Based xApp Evaluation

### 5.1 RAN KPM and Feature Selection
Correlation analysis on the dataset revealed that many of O-RAN's $>400$ KPMs are redundant. For example, DL symbols and TBs are highly correlated. To minimize dimensionality without losing information, the authors selected buffer occupancy (or PRB granted/requested ratio), number of TBs, and downlink rate as primary inputs for the DRL agents.

### 5.2 Comparing Different DRL-Based RAN Control Strategies
- **Joint vs. Fixed Slicing**: Joint control of both slicing and scheduling outperformed fixed slicing with adaptive scheduling, particularly improving throughput for users in the lower percentiles.
- **Action Space Impact**: Constraining the action space (e.g., `DRL-reduced-actions`) biases policies; removing certain configurations significantly degraded URLLC performance.
- **Autoencoder Benefit**: Agents using autoencoders outperformed those without them, as they provided a more stable mapping between network state and actions, especially when telemetry was inconsistent.
- **Control Loop Timing**: The average roundtrip time for the control loop is $\sim114$ ms, fitting within near-RT RIC specifications.

## 6 Online Training for DRL-Driven xApps
The authors evaluated fine-tuning pre-trained models on live data using Colosseum and the Arena testbed (using commercial smartphones).
- **Convergence**: Agents adapt to new environments (e.g., switching from slice-based to uniform traffic) relatively quickly, though sequential online exploration takes more wall-clock time than parallel offline training.
- **Performance Trade-offs**: The "exploration phase" of online training causes temporary throughput degradation and high variability, posing a risk for production networks.
- **Adaptability**: Online training allows agents to adapt to environment updates not present in the original dataset, significantly outperforming offline-only models when traffic profiles shift.

## 7 Related Work
While existing ML research covers PHY/MAC layers or theoretical DRL scheduling, this work distinguishes itself by providing a full-stack, large-scale experimental evaluation with closed-loop control on real SDR hardware and O-RAN compliant interfaces.

## 8 Conclusion and Lessons Learned
ColO-RAN demonstrates that integrated, open experimental frameworks are essential for AI/ML in RAN. Key findings include:
1. **System Level**: Bridging siloed projects (OSC, srsRAN) into a portable, containerized framework accelerates research.
2. **Data Engineering**: Autoencoders effectively handle missing or noisy data and reduce input dimensionality.
3. **Feature Selection**: Data-driven correlation analysis is required to avoid the "curse of dimensionality" among hundreds of available KPMs.
4. **Training Strategy**: While online training enables environment-specific adaptation, it requires a safety buffer (like an emulator) to prevent service degradation during exploration. Hardware emulation on Colosseum produces datasets that generalize well to over-the-air deployments.
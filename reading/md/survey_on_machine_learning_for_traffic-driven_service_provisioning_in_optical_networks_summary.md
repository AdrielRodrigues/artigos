---
index_terms:
  - traffic-driven service provisioning
  - optical networks
  - machine learning
  - predictive analytics
  - prescriptive analytics
  - resource allocation
  - deep reinforcement learning
---

# Survey on Machine Learning for Traffic-Driven Service Provisioning in Optical Networks

## I. Introduction
The surge in global Internet traffic and the emergence of 5G/6G services (IoT, AR/VR) have created significant spatio-temporal fluctuations known as tidal traffic. Traditional optical networks rely on static topologies designed for worst-case scenarios, leading to costly resource over-provisioning. Traffic-driven service provisioning addresses this by dynamically reconfiguring connections based on real-time demand and network state. While common at the IP layer, applying machine learning (ML) to the optical layer is essential for automating these complex configurations to maintain quality-of-service (QoS) while reducing costs.

### A. Positioning of the Survey
Existing surveys focus on narrow areas like security diagnostics, failure management, or Quality of Transmission (QoT) estimation, or provide general overviews of AI in optical networking without deep dives into specific functionalities. This paper provides a comprehensive analysis specifically of ML-based techniques for traffic-driven service provisioning. It categorizes solutions into predictive and prescriptive frameworks across proactive and adaptive networks, identifying limitations and research challenges.

## II. Evolution of Service Provisioning
Optical networks are evolving from static configurations toward software-defined networking (SDN) utilizing flexible grids and variable bit-rate coherent optics. This technological shift enables a progression in service provisioning frameworks:

*   **Reactive Networks:** Use static infrastructure with low automation. Reprovisioning is triggered only when utilization exceeds predefined thresholds.
*   **Proactive Networks:** Feature more dynamic infrastructure with external software control. They utilize ML for short-term (hours/weeks) resource reservations based on predicted traffic needs.
*   **Adaptive Networks:** Utilize fully programmable infrastructure with embedded software control and high automation. Provisioning occurs "on the fly" via real-time monitoring and continuous ML model adaptation.

### Qualitative Comparison and Trade-offs
As networks move from reactive to adaptive, spectrum utilization improves and energy consumption decreases. However, this is balanced against increased control/management overhead and a higher risk of QoS disruptions due to frequent reconfigurations.

### ML Subfields in Provisioning
*   **Predictive Provisioning:** Relies on Supervised Learning (SL) for predictive analytics to forecast future traffic, which then informs resource allocation algorithms.
*   **Prescriptive Provisioning:** Utilizes Reinforcement Learning (RL) for prescriptive analytics, learning optimal policies through trial and error without requiring labeled data.
*   **Unsupervised Learning (UL):** Used primarily for clustering traffic trends or identifying similar QoS profiles to guide network slicing.

## III. Taxonomy of Service Provisioning Approaches
The paper organizes service provisioning into a taxonomy spanning static, reactive, proactive, dynamic, and adaptive networks. It notes that baseline rule-based algorithms developed for static/dynamic networks often serve as the foundation upon which ML-aided proactive and adaptive frameworks are built.

## IV. Machine Learning for Predictive Provisioning
Predictive provisioning is split into two sub-problems: short-term traffic prediction and subsequent resource optimization. Traffic is treated as a time-series forecasting problem where non-linear ML methods outperform traditional linear statistical models (e.g., ARIMA) because network traffic is bursty and self-similar.

### A. SL for Network Traffic Prediction
Supervised Learning uses labeled datasets to map input patterns (past traffic values over a window $w$) to output labels (future values over a horizon $s$). Regression is preferred over classification in flexible-grid networks to avoid restricting predictions to predefined classes, which would result in suboptimal resource allocation.

### B. Feature Selection, Data Preprocessing, and Inference
Prediction can occur at different levels: base stations, network hubs/links, or as a full Traffic Demand (TD) matrix. Features include historical traffic values and metadata (day of week, node identity). Common preprocessing involves discretizing time into slots, using sliding windows for dataset creation, and applying scaling to improve training convergence.

### C. Available Datasets
Researchers use either synthetic datasets (generated via Poisson or log-normal distributions) or real traces from networks such as Abilene and GEANT. Real-world data provides the necessary complexity of actual link utilization over time.

### D. ML Models Applied for Network Traffic Prediction
*   **Feedforward NNs/DNNs:** Effective for mapping features, with DNNs generally outperforming shallow NNs.
*   **Recurrent NNs (RNN, LSTM, GRU):** Designed for sequential data. LSTMs solve the vanishing gradient problem of standard RNNs; GRUs offer lower computational costs.
*   **Encoder-Decoders:** Facilitate multi-step ahead prediction, which helps minimize service disruptions during optimization.
*   **Convolutional NNs (CNN/DCNN):** Capture spatial dependencies, making them ideal for predicting TD matrices or link load patterns.
*   **Graph NNs (GNNs):** Represent the network as vertices and edges to model spatio-temporal dependencies of graph-structured data.
*   **Bayesian Learning (e.g., GPR):** Provides probabilistic outputs, offering a measure of uncertainty rather than just point predictions.

### E. Further ML Models to Exploit
Promising future directions include **Transformers**, which allow parallelization and faster training than RNNs, and **Bayesian Deep Learning (BDL)**, which combines the scaling power of DNNs with principled uncertainty estimation to mitigate over- and under-provisioning.

## V. Optimization in Predictive Provisioning
This phase uses ML predictions as inputs for resource allocation algorithms.

### A. Proactive Networks
Optimization is performed off-line on a multi-period basis (e.g., hourly). The process involves predicting the TD matrix, deciding if reconfiguration is necessary based on QoS thresholds, executing a resource allocation algorithm, and implementing changes. Objectives typically include minimizing energy consumption by shutting down idle resources or reducing service disruptions. While proactive networks improve spectrum utilization over static ones, they may slightly increase under-provisioning, which can be mitigated using prediction uncertainty margins.

### B. Adaptive Networks
Optimization is performed on-line at short time scales (seconds/minutes). Predictions regarding connection arrival/departure times are used to assign weights to network links. These weights guide routing heuristics to avoid future congestion and reduce blocking probability. This approach outperforms conventional dynamic provisioning, provided the ML predictions are sufficiently accurate.

## VI. Machine Learning for Prescriptive Provisioning
Prescriptive provisioning uses RL to learn policy-driven optimization. Unlike predictive models that require a separate allocation algorithm, prescriptive agents learn optimal policies directly through interaction with the environment.

### A. RL for TE and Service Provisioning
RL is framed as a Markov Decision Process (MDP) defined by states ($S$), actions ($A$), transition dynamics ($\mathcal{T}$), reward functions ($\mathcal{R}$), and a discount factor ($\gamma$). The agent's goal is to find a policy $\pi$ that maximizes the expected cumulative discounted reward.

### B. RL Algorithms
*   **Value-based:** Estimate state-value functions (e.g., DQN).
*   **Policy-based:** Directly optimize the policy parameters.
*   **Actor-Critic:** Combine both; an actor proposes actions and a critic evaluates them. These are most popular for high-dimensional optical networks, often using GCNs or RNNs as function approximators to capture spatiotemporal dependencies.

### C. State, Action, and Reward Representation
To avoid the "curse of dimensionality," states and actions must be abstracted (e.g., representing the network at the lightpath level rather than the physical link level). Rewards are the primary signal for learning; inappropriate reward scaling can lead to poor policy convergence.

### D. Performance Metrics
Evaluation is based on cumulative reward progress over episodes, training time (convergence speed), and targeted metrics like blocking probability compared against rule-based baselines.

## VII. Optimization in Prescriptive Provisioning
Prescriptive frameworks are applied similarly to proactive (off-line) and adaptive (on-line) networks.

### A. Proactive Networks
Agents provide actionable advice on bandwidth reservation for future intervals. By observing the impact of actions on actual traffic, prescriptive agents can better balance over- and under-provisioning than predictive schemes that lack a feedback loop.

### B. Adaptive Networks
Agent policies are learned to provision requests on-line to minimize blocking probability and spectrum utilization. To reduce complexity, RL is often applied only to sub-problems (e.g., routing) while other decisions use rule-based heuristics. Multi-domain environments often require cooperative DRL agents that share state information to converge effectively.

## VIII. Predictive Provisioning: Survey on ML
Surveying bit-rate, arrival/holding time, and link load predictions reveals that RNNs are best for temporal data and CNNs/GNNs for spatial data.

### Main Outcomes and Research Challenges
*   **Uncertainty:** Bayesian Deep Learning is needed to represent uncertainty flexibly.
*   **Multi-Step Prediction:** Most work focuses on single-step ahead; multi-step prediction via encoder-decoders is needed for better energy/disruption management.
*   **Traffic Disaggregation:** Predicting individual service flows rather than aggregated traffic is challenging but necessary for diverse SLAs.
*   **ML Lifecycle:** Research is lacking on automatic monitoring of model degradation and adaptation to non-stationary traffic.
*   **Edge Training:** Federated Learning (FL) offers a way to train models at the edge while preserving privacy and reducing communication overhead.
*   **Human-Centric ML:** Integration of explainable AI and Human-in-the-Loop (HITL) is necessary for operator trust.

## IX. Predictive Provisioning: Survey on Optimization
### A. Proactive Networks
Energy optimization is achieved by shutting down unutilized resources during low-demand periods, though this introduces a trade-off with increased blocking probability. Elastic spectrum allocation (SA) significantly reduces unserved traffic compared to fixed SA. Furthermore, $\alpha$-fairness algorithms can be used to ensure QoS fairness in congested networks, preventing greedy algorithms from starving certain services.

### B. Adaptive Networks
Predictive RSCA (Routing and Spectrum Allocation) consistently outperforms dynamic provisioning by using predictions to adjust link weights, thereby reducing fragmentation and blocking.

## X. Prescriptive Provisioning: Survey on ML and Optimization
Prescriptive methods generally outperform predictive ones because they optimize for the final QoS target rather than just trying to match a traffic forecast.

### A. Proactive Networks
Cooperative RL agents for bandwidth allocation better manage contention between connections, leading to superior resource utilization compared to SL-based predictions.

### B. Adaptive Networks
DRL frameworks (like DeepRMSA) outperform rule-based heuristics in EONs. Transfer Learning (TL) and Multi-Task Learning are critical for reducing the massive amount of experience (episodes) required for convergence, allowing policies to be transferred across different network topologies. In multi-layer networks, using Auxiliary Graphs (AG) simplifies the state space, enabling DRL agents to optimize wavelength utilization effectively.

### C. Main Outcomes and Research Challenges
The primary hurdle is RL convergence speed. Suggestions include using Supervised Learning to "seed" agents via imitation learning before switching to RL. Other challenges include developing truly cooperative Multi-Agent RL (MARL) and moving from simulated environments with synthetic traffic to real-world, non-stationary network deployments.

## XI. Summary Remarks and Future Directions
ML-aided provisioning significantly improves resource utilization, energy efficiency, and throughput over rule-based methods. Key future directions include:
1.  **Security:** Addressing "adversarial ML" attacks where manipulated traffic data could cause network outages.
2.  **Field Trials:** Validating models on large-scale real networks to test the limits of current SDN/NFV frameworks.
3.  **Efficiency:** Exploring TinyML and spiking NNs to reduce the computational overhead of inference at the edge.
4.  **Human Integration:** Developing HITL systems where human experts handle unexpected events that RL cannot predict.
---
index_terms:
  - traffic-driven service provisioning
  - optical networks
  - machine learning
  - predictive service provisioning
  - prescriptive service provisioning
  - resource allocation
  - deep reinforcement learning
---

# Survey on Machine Learning for Traffic-Driven Service Provisioning in Optical Networks

## I. Introduction
The explosive growth of global Internet traffic and the emergence of 5G/6G services (IoT, autonomous vehicles) create massive spatio-temporal fluctuations known as tidal traffic. Traditional optical networks rely on static topologies designed for worst-case scenarios, leading to significant resource over-provisioning and high operational costs. To combat this, the industry is moving toward traffic-driven service provisioning, where network configurations are dynamically adjusted based on real-time demand and current state to optimize resource efficiency while maintaining Quality of Service (QoS). Machine Learning (ML) is identified as a critical enabler for automating these complex, data-heavy reconfiguration processes at the optical layer.

### A. Positioning of the Survey
While existing surveys cover ML for threat detection, failure management, or Quality of Transmission (QoT) estimation, this paper specifically focuses on traffic-driven service provisioning. It introduces a novel categorization dividing ML-aided approaches into predictive and prescriptive frameworks across proactive and adaptive network architectures.

## II. Evolution of Service Provisioning
Optical networks are evolving from static infrastructures to software-defined networking (SDN) utilizing flexible grids and variable bit-rate coherent optics. This evolution allows for a transition in provisioning frameworks:

*   **Reactive Networks:** Use static infrastructure and descriptive analytics. Reprovisioning is triggered only when performance thresholds (e.g., link utilization) are violated. These suffer from high over-provisioning and low automation.
*   **Proactive Networks:** Utilize more dynamic infrastructure with external software control. They employ predictive or prescriptive analytics to reserve resources a-priori for short-term future needs (hours/weeks).
*   **Adaptive Networks:** Feature highly programmable infrastructure with embedded software control. They use real-time monitoring and ML to provision services on the fly, accounting for both current demand and future behavior to minimize congestion and fragmentation.

The paper distinguishes between two main ML-driven strategies:
1.  **Predictive Provisioning (Supervised Learning - SL):** Uses predictive analytics to forecast traffic, which then serves as input for traditional resource allocation algorithms.
2.  **Prescriptive Provisioning (Reinforcement Learning - RL):** Uses prescriptive analytics to learn optimal resource allocation policies through trial and error, providing direct actionable advice without requiring labeled data.

Unsupervised Learning (UL) is noted as useful for clustering traffic profiles or detecting anomalies to guide these frameworks, though it does not provide future trend predictions.

## III. Taxonomy of Service Provisioning Approaches
The paper establishes a taxonomy that maps service provisioning strategies across network types: static, reactive, proactive, dynamic, and adaptive. It notes that while baseline algorithms from static/dynamic networks are often used as building blocks, the focus of this survey is strictly on ML-aided proactive and adaptive frameworks.

## IV. Machine Learning for Predictive Provisioning
Predictive provisioning consists of two sub-problems: short-term traffic prediction and subsequent resource optimization. Traffic prediction is treated as a time-series forecasting problem where non-linear ML methods are preferred over linear statistical models like ARIMA, which struggle with the burstiness and self-similarity of network traffic.

### A. SL for Network Traffic Prediction
Supervised Learning uses labeled datasets (past traffic values $\mathbf{x}$ to predict future values $\mathbf{y}$). Regression is generally preferred over classification because it provides continuous outputs necessary for flexible infrastructure like Elastic Optical Networks (EONs). Model performance is measured using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

### B. Feature Selection, Data Preprocessing, and Inference
Traffic can be monitored at the base station level, link level, or as a Traffic Demand (TD) matrix for all source-destination pairs. Key preprocessing steps include time slot discretization, using sliding windows to manage computational complexity, and dataset scaling to improve convergence during training.

### C. Available Datasets
The research utilizes both synthetic datasets (generated via simulators or Poisson/log-normal distributions) and real-world traces from networks like Abilene and GEANT.

### D. ML Models Applied for Network Traffic Prediction
*   **Feedforward NNs/DNNs:** Effective for mapping features but often serve as benchmarks for more specialized models.
*   **Recurrent NNs (RNNs, LSTM, GRU):** Designed for sequential data. LSTMs solve the vanishing gradient problem of standard RNNs; GRUs offer a computationally efficient alternative with fewer parameters.
*   **Encoder-Decoders:** Enable multi-step ahead prediction by mapping an input sequence to an output sequence, which is useful for reducing service disruptions during reconfiguration.
*   **CNNs and GNNs:** CNNs capture spatial dependencies (critical for TD matrices), while Graph NNs treat the network as a graph of vertices and edges, making them promising for capturing spatio-temporal relationships.
*   **Bayesian Learning:** Provides probabilistic interpretations and uncertainty measures via Gaussian Process Regression (GPR), which is robust against outliers and sparse data.

### E. Further ML Models to Exploit
The paper suggests two emerging areas: **Transformers**, which allow parallelization of sequential data processing for faster training, and **Bayesian Deep Learning (BDL)**, which combines the scaling power of deep learning with principled uncertainty estimation to mitigate over- and under-provisioning.

## V. Optimization in Predictive Provisioning
Optimization is divided based on whether it occurs off-line (proactive) or on-line (adaptive).

### A. Proactive Networks
Proactive networks use TD matrix predictions (hourly scale) for multi-period re-optimization. The process involves: Prediction $\rightarrow$ Reconfiguration Decision $\rightarrow$ Resource Allocation Algorithm $\rightarrow$ Physical Reconfiguration. Objectives include minimizing energy consumption, connection blocking, and reconfiguration disruptions. Optimization is performed via Integer Linear Programming (ILP) or heuristics.

### B. Adaptive Networks
Adaptive networks perform on-line optimization using short-term predictions (seconds/minutes) of arrival/departure times and spectrum utilization. This information is used to dynamically update link weights, guiding routing algorithms to prioritize resources that increase the likelihood of accepting future requests and reduce blocking.

## VI. Machine Learning for Prescriptive Provisioning
Prescriptive provisioning uses RL to learn a "policy" rather than just predicting traffic. It is model-free and adapts as the environment changes. Because of the high dimensionality of optical networks, most current frameworks combine RL with rule-based heuristics or apply it only to specific sub-problems (e.g., routing).

### A. RL for TE and Service Provisioning
The framework is modeled as a Markov Decision Process (MDP) defined by states ($S$), actions ($A$), transition dynamics ($\mathcal{T}$), reward functions ($\mathcal{R}$), starting states, and a discount factor ($\gamma$). The agent aims to maximize the cumulative discounted reward.

### B. RL Algorithms
*   **Value-based:** Learns the value of being in a state (e.g., Q-learning).
*   **Policy-based:** Directly optimizes the policy $\pi$.
*   **Actor-Critic:** Combines both; an "actor" proposes actions while a "critic" evaluates them. Deep Reinforcement Learning (DRL) actor-critic models are preferred for complex optical network states.

### C. State, Action, and Reward Representation
To avoid the "curse of dimensionality," state and action spaces must be abstracted (e.g., using path-level rather than link-level representations). Rewards must be carefully scaled to ensure the agent converges toward the desired objective (e.g., minimizing blocking probability).

### D. Performance Metrics
Success is measured by the convergence of cumulative rewards over episodes, reduction in blocking probability compared to baselines, and total training time.

## VII. Optimization in Prescriptive Provisioning
Prescriptive optimization provides actionable advice for resource management.

### A. Proactive Networks
In proactive settings, RL agents suggest off-line re-optimization actions. Evidence suggests that prescriptive approaches can outperform predictive ones because they explicitly optimize for QoS targets and congestion rather than relying on an intermediate traffic forecast.

### B. Adaptive Networks
Prescriptive provisioning focuses on on-line request handling. By learning the long-term impact of current decisions, RL agents can outperform conventional dynamic heuristics in terms of spectrum utilization and blocking probability. To maintain tractability, many frameworks use RL for routing while using heuristics for spectrum allocation.

## VIII. Predictive Provisioning: Survey on ML
The paper reviews literature focusing specifically on the prediction sub-problem.

### A. Bit-Rate Prediction
Research shows that aggregated traffic is easier to predict than base station level traffic. DNNs generally outperform simple ANNs. LSTMs are effective for short-term forecasts, but accuracy drops significantly beyond certain thresholds (e.g., 60 seconds). Quantile regression and GPR ensembles are highlighted as superior methods for handling uncertainty and reducing under-provisioning.

### B. Connection Arrival, Holding Time Prediction
LSTMs can predict holding times to assist on-line adaptive provisioning, though accuracy is degraded by unexpected traffic events. Training models on diverse profiles improves robustness.

### C. Link Load Prediction
Graph learning (GCN-GAN) and hybrid DCRNNs are more effective than LSTMs for link load prediction because they capture the topological spatial dependencies of the network alongside temporal trends.

### D. Main Outcomes and Research Challenges
*   **Uncertainty:** There is a need for BDL to represent uncertainty more flexibly.
*   **Multi-Step Prediction:** Most work focuses on single-step; multi-step prediction using encoder-decoders is needed for proactive planning.
*   **Traffic Disaggregation:** Predicting disaggregated traffic (per service SLA) is harder but necessary for VNF-SC provisioning.
*   **ML Lifecycle:** Developing automated monitoring and model adaptation systems for non-stationary traffic is critical.
*   **Edge Training:** Moving toward Federated Learning (FL) to improve privacy and reduce communication overhead.
*   **Human-Centric ML:** Integration of explainable AI and Human-in-the-Loop (HITL) approaches to ensure operator trust.

## IX. Predictive Provisioning: Survey on Optimization
This section reviews the application of predictions to resource allocation.

### A. Proactive Networks
*   **Energy Consumption:** Significant savings are achieved by shutting down idle resources during low-traffic hours, though this creates a trade-off with increased blocking probability.
*   **Service Disruptions:** Constrained reconfiguration (reducing the number of changed lightpaths) reduces disruptions and OPEX but may increase unserved traffic.
*   **Multi-Layer Optimization:** Coordinated optimization across virtual and physical layers is more effective than optimizing a single layer.
*   **ML Uncertainty:** Using quantile margins instead of fixed empirical margins significantly reduces spectrum waste while preventing under-provisioning.
*   **QoS Fairness:** $\alpha$-fairness algorithms prevent "greedy" allocation from starving certain services in congested networks.

### B. Adaptive Networks
Predictive adaptive provisioning consistently outperforms conventional dynamic provisioning in reducing blocking, provided the predictions are accurate. If accuracy is low, predictive schemes can actually perform worse than non-predictive ones.

### C. Main Outcomes and Research Challenges
While benefits over static/reactive networks are clear, challenges remain in adapting these optimizations to emerging technologies (e.g., spatio-spectral multiplexing) and complex problems like VNF-SC.

## X. Prescriptive Provisioning: Survey on ML and Optimization
Prescriptive frameworks avoid the errors inherent in two-step "predict then optimize" pipelines by learning policies directly.

### A. Proactive Networks
Limited research exists here, but results show that prescriptive agents better balance over- and under-provisioning than predictive models because they observe the actual impact of their actions on QoS.

### B. Adaptive Networks
Most work utilizes DRL actor-critic frameworks.
*   **Single-Domain:** DeepRMSA improves blocking probability but requires millions of episodes to converge; Transfer Learning (TL) can reduce this requirement to thousands.
*   **Multi-Layer:** Abstraction is key; agents operating on logical topologies or auxiliary graphs (ADMIRE) converge faster and perform better than link-level agents.
*   **Multi-Domain:** Cooperation via information sharing between DRL agents (DeepCoop) is essential for convergence in multi-domain environments.
*   **VNF-SC:** Hierarchical GNN-based DRL can jointly optimize resource utilization and blocking probability more effectively than non-hierarchical DNNs.

### C. Main Outcomes and Research Challenges
*   **Convergence:** Using imitation learning (learning from baselines) to seed RL agents is a promising way to speed up training.
*   **Cooperation:** Moving toward truly cooperative Multi-Agent RL (MARL) based on game theory.
*   **Human-Centricity:** Developing offline-to-online pipelines and HITL mechanisms to avoid "disastrous" trial-and-error actions in live networks.
*   **Scale:** Transitioning from synthetic simulations to real, large-scale non-stationary environments.

## XI. Summary Remarks and Future Directions
ML-aided provisioning outperforms rule-based approaches across all network types by better capturing time-varying behavior. However, the path to full adoption requires addressing several gaps: the need for field trials at scale, development of "Tiny ML" for edge deployment, and the creation of defenses against adversarial ML attacks that could manipulate traffic data to cause outages or QoS violations. Future research should embrace multidisciplinary approaches combining bio-inspired optimization, Federated Learning, and explainable AI.
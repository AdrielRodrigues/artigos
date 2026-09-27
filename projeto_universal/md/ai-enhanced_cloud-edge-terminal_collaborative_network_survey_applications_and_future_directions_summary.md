---
index_terms:
  - cloud-edge-terminal collaborative network
  - deep reinforcement learning
  - multi-agent reinforcement learning
  - task offloading
  - resource allocation
  - collaborative caching
  - mobility management
---

# AI-Enhanced Cloud-Edge-Terminal Collaborative Network: Survey, Applications, and Future Directions

## I. Introduction
The Cloud-Edge-Terminal Collaborative Network (CETCN) is a paradigm designed to meet the low-latency and ultra-reliability requirements of emerging applications (e.g., remote surgery, smart transportation) that traditional centralized cloud computing cannot satisfy due to propagation delays and bandwidth bottlenecks. 

Key operational challenges in CETCN include:
*   **Task Offloading and Resource Allocation:** Managing limited computing/storage resources on edge nodes and terminal devices while balancing energy consumption and delay.
*   **Collaborative Caching:** Reducing core network traffic and latency by storing popular content at the network edge.
*   **Mobility Management:** Ensuring seamless service continuity for moving users despite dynamic channel conditions.

The authors argue that Deep Reinforcement Learning (DRL) and Multi-Agent DRL (MADRL) are superior to traditional optimization methods because they do not require accurate environment models, can handle high-dimensional dynamic states through iterative interaction, and optimize for long-term performance rather than one-shot gains. MADRL specifically allows different vendors to make optimal decisions using local observations via a centralized training/decentralized execution framework.

## II. Related Concepts

### A. Cloud Computing
Cloud computing provides on-demand resources via IaaS, PaaS, and SaaS models. However, it faces significant challenges: high data transfer latency, potential service outages (reliability), unpredictable costs in pay-as-you-go models, and privacy risks associated with third-party storage. Serverless computing (FaaS) further introduces "cold start" latencies and stateless execution constraints.

### B. Multi-Access Edge Computing (MEC)
MEC shifts computation closer to the user by deploying servers at base stations or access points. Its primary advantages include:
*   **Low Latency:** Drastic reduction in propagation and communication delay compared to remote clouds.
*   **Energy Saving:** Prolongs battery life of IoT devices by offloading compute-intensive tasks.
*   **Enhanced Privacy:** Localized processing reduces the need to transmit sensitive data across the core network.

### C. Fog Computing
Fog computing is a decentralized paradigm that sinks resources to the edge via fog nodes (routers, gateways). Unlike MEC, fog computing is typically designed as a tight extension of the cloud rather than a standalone alternative. It is characterized by heterogeneity and distributed management.

### D. Comparison of Computing Modes
*   **Geography:** Cloud is centralized/core; Fog/MEC are decentralized/edge.
*   **Purpose:** Cloud focuses on big data analysis and long-term storage; Fog/MEC focus on real-time, short-term data processing for local business execution.
*   **Operation:** MEC can operate in stand-alone mode; Fog typically requires cloud connectivity.

### E. Cloud-Edge-Terminal Collaborative Computing
The authors define CETCN as a three-layer architecture (Terminal $\rightarrow$ Edge $\rightarrow$ Cloud) designed to optimize computing, storage, and communication resources across all levels. 
*   **Data Life Cycle:** AI can enhance every stage: preprocessing (collection), adaptive modulation (transmission), pattern recognition (processing), de-duplication (storage), and predictive maintenance (utilization).
*   **Core Challenges:** Managing the heterogeneous capacity of devices, solving NP-hard multi-objective optimization problems, and handling mixed-integer programming (e.g., combining discrete caching decisions with continuous offloading variables).

## III. An Introduction to Reinforcement Learning and its State-of-the-Art

### A. Single-Agent Reinforcement Learning (SARL)
*   **Markov Decision Process (MDP):** Defined by a tuple $\langle \mathcal{S}, \mathcal{A}, R, T, \gamma \rangle$. An agent interacts with the environment to maximize a discounted cumulative reward based on its policy.
*   **Partial Observable MDP (POMDP):** Used when agents cannot see the full system state (e.g., an edge server only knows about its connected users). It adds observations ($\mathcal{O}$) and transition probabilities ($Z$).

### B. Multi-Agent Reinforcement Learning (MARL)
*   **Markov Game (MG):** Extends MDPs to multiple players where rewards depend on joint actions. The goal is often to find a Nash Equilibrium (NE), where no agent can improve its reward by unilaterally changing its policy.
*   **Dec-POMDP:** A cooperative setting where agents make decisions based on local observations to maximize a shared long-term reward.

### C. DRL Algorithms Used in the Survey
*   **DQN & DDQN:** DQN uses replay buffers and target networks for stability; DDQN reduces the overestimation of Q-values by decoupling action selection from evaluation.
*   **Actor-Critic (AC):** Simultaneously learns a policy (actor) and a value function (critic).
*   **DDPG:** An extension of DQN for continuous action spaces.
*   **MADDPG:** Extends DDPG to multi-agent scenarios using centralized training to stabilize the environment.
*   **COMA:** Uses a counterfactual baseline to solve the "credit assignment" problem in cooperative multi-agent settings.
*   **Mean-Field RL (MF-Q, MF-DDPG):** Addresses scalability by approximating the interaction of many agents as an interaction between a single agent and the average effect (mean field) of its neighbors.

## IV. The Architecture of Cloud-Edge-Terminal Collaborative Network

### A. Main Components
*   **Terminal Layer:** Sensors and devices that collect data or generate tasks.
*   **Edge Layer:** Base stations, RSUs, and edge servers that provide low-latency processing using short-range communication (WiFi, Bluetooth, ZigBee).
*   **Cloud Layer:** Centralized data centers for heavy computation and long-term storage.

### B. Cloud-Edge Collaborative Architecture
This architecture emphasizes the complementary nature of cloud and edge. The edge handles real-time control and data analysis, while the cloud manages complex tasks and global orchestration. Applications include industrial infrared service platforms and equipment defect detection.

### C. Cloud-Edge-Terminal Collaborative Architecture
This model utilizes the computing power of the terminal devices themselves (e.g., using parked vehicles or UAVs as auxiliary compute nodes) to further reduce burdens on the edge layer. This is particularly useful in remote areas or during network peak periods.

### D. Cloud-Edge-Terminal Intelligent Collaboration
The authors define this as "endogenous intelligence," focusing on low-cost, high-efficiency collaborative optimization. It offers four key advantages over pure cloud/terminal intelligence: reduced bandwidth costs, higher real-time performance, superior privacy protection, and a higher level of overall system intelligence via DRL.

## V. Task Offloading and Resource Allocation for AI-Enabled CETCN

### A. Classification of Task Offloading Models
*   **Binary Offloading:** Tasks are indivisible; they must be processed entirely by the terminal, an edge server, or the cloud.
*   **Partial Offloading:** Tasks can be split across different computing entities.

### B. Classification of Resource Allocation Models
*   **Computing Model:** Focuses on CPU cycle frequency and energy consumption (which scales quadratically with frequency).
*   **Communication Model:** Addresses challenges like multipath fading, interference, and spectrum scarcity. The authors note that 6G will target millisecond-level air port delay and significantly higher energy efficiency.
*   **Caching Model:** Focuses on placing popular content to reduce backhaul traffic and latency.

### C. Literature Review
The section reviews numerous works applying DRL to offloading:
*   **SARL (DQN, DDQN, AC):** Used for minimizing long-term energy consumption and delay in simple terminal-edge or edge-cloud setups.
*   **POMDP/Dec-POMDP:** Applied when agents have incomplete information about channel states or neighbor workloads.
*   **MARL (MADDPG, MF-RL):** used to manage large populations of users or satellites where coordination is required to avoid congestion.

### D. Lesson Learned and Future Directions
Current research often relies on simplified simulations rather than real-world traces. Future directions include:
*   **Dynamic Workloads:** Adapting strategies to rapid changes in user mobility.
*   **Federated Learning (FL):** Offloading the training of models themselves to maintain privacy.
*   **Green Offloading:** Prioritizing carbon footprint reduction.
*   **QoE Optimization:** Moving beyond raw metrics (latency/energy) toward subjective user satisfaction.

## VI. Collaborative Caching for AI-Enabled CETCN

### A. Collaborative Caching Model
A tiered retrieval process is defined: User $\rightarrow$ Local Edge Server $\rightarrow$ Cooperative Edge Domain $\rightarrow$ Cloud Data Center. The primary constraint is the finite caching capacity $C_i$ of edge nodes.

### B. MEC from a Computer Science Perspective
Caching involves several layers:
*   **Fundamentals:** Use of VMs and containers on edge servers for agility.
*   **Algorithms:** Traditional methods (LRU, LFU, FIFO) are being replaced by AI-driven popularity prediction.
*   **SDN/NFV:** These enable a programmable data plane to dynamically route requests to the most efficient cache location.

### C. Literature Review
The survey highlights DRL's ability to learn content popularity without prior knowledge. Key approaches include:
*   Using **Q-Learning and DQN** for content replacement policies.
*   Integrating **D2D communication** to allow users to share cached content, reducing edge server load.
*   **Federated Caching:** Allowing base stations to collaborate on prediction models without sharing raw user data.

### D. Lesson Learned and Future Directions
Future research should address:
*   **Privacy-Preserving Caching:** Designing strategies that don't require users to disclose their specific content preferences.
*   **Data Replication:** Optimizing where to place copies of data to avoid redundancy while ensuring availability.
*   **Economic Models:** Developing a fair benefit-sharing mechanism between hardware providers, content owners, and operators.

## VII. Mobility Management for AI-Enabled CETCN

### A. Existing 3GPP Standards
Current standards (5G) cover Intra-RAT and Inter-RAT handovers, Idle Mode mobility, Xn/NG-based handovers, Dual Connectivity, and Network Slicing mobility.

### B. Challenges of Mobility Management
Mobility introduces handover disruptions, packet loss, jitter, and signal fluctuations. Traditional Markov chain models are often too simple for the heterogeneity of CETCN.

### C. Literature Review
DRL is used to predict trajectories and optimize handovers:
*   **Trajectory Prediction:** Combining Q-learning with memory networks (RNNs) to anticipate user movement.
*   **Handover Optimization:** Using DQN/DDQN to minimize handover frequency and reduce radio link failure probability.
*   **UAV-Assisted Mobility:** DRL for real-time path planning of UAVs to maintain seamless coverage.

### D. Lesson Learned and Future Directions
Future focus is needed on **Real-time Decision-making**, as the computational overhead of DRL training may conflict with the millisecond requirements of a handover event.

## VIII. Applications for AI-Enabled CETCN

### A. Intelligent Transportation Systems (ITS)
Focuses on V2X and RSU coordination. Key uses include:
*   **Energy Scheduling:** Using Q-learning to manage RSU power cycles.
*   **Dynamic Offloading:** DDPG for balancing energy and latency in vehicle networks.
*   **V2V Collaboration:** Multi-agent systems to allow vehicles to act as edge nodes for each other.

### B. Industrial IoT (IIoT)
Characterized by massive data and strict real-time constraints. 
*   **Task Offloading:** Using DRL to handle non-convex optimization problems that are too slow for traditional convex solvers.
*   **Service Placement:** Applying DQN/DDQN to map Service Function Chains (SFCs) onto edge resources efficiently.

### C. Smart Health
Focuses on the Internet of Medical Things (IoMT). 
*   **Criticality:** High priority on "information freshness" (Age of Information - AoI) for vital sign monitoring.
*   **Reliability:** Use of MADDPG and Blockchain to ensure secure, low-latency offloading of medical data in 6G environments.

### D. Digital Agriculture
Employs UAVs and edge clouds for crop monitoring and irrigation.
*   **Task Migration:** Using DQN to move heavy deep learning models (e.g., wheat growth detection) between devices to balance energy consumption.

## IX. Security Issues for AI-Enabled CETCN

### A. Differential Privacy (DP) Toy Example
The authors explain DP as a method of adding controlled noise to data during collection, aggregation at the edge, or computation in the cloud, ensuring individual records cannot be re-identified.

### B. Literature Review
*   **RL Training:** Using Local Differential Privacy (LDP) and Laplace noise in A3C algorithms to prevent strategy leakage.
*   **Offloading:** Applying DP-DQN to mask user usage patterns from "honest but curious" MEC servers.
*   **Caching/Mobility:** Using LDP for content preferences and generating synthetic trajectories to protect user movement privacy.

### C. Lesson Learned and Future Directions
Future work should target **Dynamic Privacy Budget Management** (adjusting noise levels based on the analysis requirement) and extending DP to complex data types like graphs and images.

## X. Standardization Efforts of Edge Intelligence

The paper reviews efforts by:
*   **ITU-T:** Recommendations for microservices-based signaling and smart agriculture data interfaces.
*   **3GPP:** Integration of AI/ML functional support into the 5G system (Release 18).
*   **IEEE:** The OpenFog reference architecture and standards for IoT terminology and Time-Sensitive Networking (TSN).

Technical challenges remaining include limited edge energy, a lack of unified definitions for "Edge Intelligence," and the need for interoperability between diverse vendor modules.

## XI. Challenges and Future Directions

The authors identify several high-level research gaps:
*   **Training Bottlenecks:** Moving from centralized cloud training to Federated Learning to reduce data movement and enhance privacy.
*   **Dimensionality Explosion:** Using MARL and Game Theory to handle the massive action spaces created by Ultra-Dense Networks (UDN).
*   **Synchronization:** Overcoming the unreliability of wireless links that prevent agents from synchronizing global states in real-time.
*   **Reward Conflict:** Designing "mixed reward" functions that balance competing interests (e.g., user QoS vs. provider revenue).
*   **Heterogeneity:** Moving beyond Mean-Field RL's assumption of isomorphic players to handle devices with vastly different capacities.
*   **Quantum Computing (QCCETCN):** The potential for Quantum Machine Learning (QML) to accelerate the heavy learning phases of DRL and solve complex optimization tasks in seconds.
*   **Mathematical Rigor:** A call for more formal convergence proofs for DRL in CETCN, rather than relying solely on simulation results.

## XII. Conclusion
The CETCN paradigm combined with AI—specifically DRL and MADRL—provides a path toward low-latency, energy-efficient networking. By orchestrating resources across terminal, edge, and cloud layers, the network can support high-demand applications in ITS, IIoT, health, and agriculture while addressing evolving security and standardization needs.
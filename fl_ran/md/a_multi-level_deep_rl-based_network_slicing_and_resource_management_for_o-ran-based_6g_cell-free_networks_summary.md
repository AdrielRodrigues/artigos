---
index_terms:
  - O-RAN
  - cell-free massive MIMO
  - network slicing
  - deep reinforcement learning
  - QMIX algorithm
  - NAF DQL
  - resource management
  - 6G networks
---

# A Multi-Level Deep RL-Based Network Slicing and Resource Management for O-RAN-Based 6G Cell-Free Networks

## I. Introduction

### A. Background
As mobile communication evolves toward the sixth generation (6G), current 5G capabilities—such as peak data rates of 10 Gbps and sub-1ms latency—will be insufficient by 2030. 6G aims for peak data rates exceeding 1 Tbps, user-experienced rates of 1 Gbps, and critical latencies between 10 and 100 $\mu$s to support advanced services like holographic VR and autonomous driving. Central to this is network slicing, which allows the creation of isolated virtual networks (slices) on shared infrastructure to meet contradictory demands of various service types (e.g., FeMBB, umMTC).

### B. Related Work
Current research into 6G RAN slicing frequently employs Machine Learning (ML), specifically Deep Reinforcement Learning (DRL) algorithms like DQN, Double DQN, and DDPG, to optimize resource allocation and QoS. However, most existing works focus on specific problems or simplified network models that lack the necessary architectural entities to host ML algorithms in a real-world deployment.

### C. Motivation and Contributions
The authors identify a gap in combining Open-RAN (O-RAN) and Cell-Free massive MIMO (CF mMIMO). While CF mMIMO eliminates cell boundaries to improve diversity and interference management, it complicates network slicing because slices must not share resource blocks, yet there are no fixed user groups or cell boundaries. 

The paper contributes a comprehensive management approach that utilizes:
- **O-RAN architecture** for programmability and ML hosting.
- **CF mMIMO** for robust 6G physical layer performance.
- **A hierarchical DRL scheme**: A Multi-Agent RL (MARL) level for centralized, cooperative decision-making regarding slice assignment, and a single-agent RL level for decentralized execution of resource allocation.
- **Diverse Service Types**: Consideration of all envisioned 6G services rather than just one or two.

## II. Preliminaries and Enabling Technologies

### A. ML in Wireless Networks
RL is selected over supervised or unsupervised learning because it allows agents to learn optimal policies through interaction with a dynamic environment. Multi-Agent RL (MARL) is specifically highlighted as necessary for addressing the complexity of 6G resource management where multiple decision-makers interact simultaneously.

### B. Open-RAN in Future Intelligent Networks
O-RAN shifts hardware-based ecosystems toward open, cloud-based modular architectures. Key entities include the O-Centralized Unit (O-CU), O-Distributed Unit (O-DU), and O-Remote Unit (O-RU). Intelligence is integrated via the RAN Intelligence Controller (RIC), comprising:
- **Non-Real-Time (non-RT) RIC**: Hosts rApps for network orchestration and long-term optimization.
- **Near-Real-Time (near-RT) RIC**: Hosts xApps for managing QoS requirements in shorter timeframes.

### C. Cell-Free Massive MIMO in Future RAN Implementations
CF mMIMO replaces traditional cells with a distributed set of access points that serve users coherently. This improves spectral and energy efficiency and reduces latency but creates a conflict with network slicing, as the boundaryless nature of CF mMIMO opposes the need for precise resource isolation between slices.

## III. The Proposed Network Slicing and Resource Management Scheme in 6G Environment

### A. Problem Statement and General Idea
The goal is to maximize total network capacity while guaranteeing QoS across diverse slice types in a dynamic O-RAN/CF mMIMO system. To manage complexity, the authors propose splitting the problem into two levels: a high-level cooperative MARL for choosing slice types for requests, and a low-level decentralized RL for assigning actual resource blocks (RBs).

### B. System Model and Compatibility
The architecture aligns with O-RAN specifications:
- **High-Level Part**: Located in the non-RT RIC within the Service Management and Orchestration (SMO) framework. It observes global network status and uses a long time slot ($\mathbf{T_L} > 1\text{s}$) for synchronized slice assignment.
- **Low-Level Part**: Located in the near-RT RIC. It receives assignments from the high level and executes resource allocation within shorter time slots ($\mathbf{T_S}$ between $10\text{ms}$ and $1\text{s}$).

### C. Implementation Technicalities
#### High-level Part
The system considers five 6G service types: FeMBB, umMTC, ERLLC, LDHMC, and ELPC (each with specific KPIs like peak data rate or latency). 
- **Algorithm**: The authors use **QMIX**, which allows centralized training of decentralized policies to avoid the exponential growth of joint action spaces.
- **Reward Function**: $R_{tot-agent_i} = \frac{1}{3} R_{agent_i} + \frac{2}{3} R_{team}$. The individual reward ($R_{agent_i}$) is binary based on resource availability; the team reward ($R_{team}$) is the ratio of resources in use to total available resources.

#### Low-level Part
Single agents are responsible for realizing the QoS requirements of the assigned slice type by allocating RBs.
- **Algorithm**: Since RB allocation requires a continuous action space, the authors employ **Normalized Advantage Function DQL (NAF DQL)**, which provides the stability of Q-learning in continuous environments.
- **Reward**: Rewards are granted when all predefined KPIs for a specific service type fall within their required ranges.

### D. Practicality, Complexity, and Scalability
Complexity is reduced by distributing tasks: high-level agents handle consistency/synchronization, while low-level agents operate locally without needing global network state. QMIX ensures scalability as the action space does not grow exponentially with more agents. Communication overhead is minimized, occurring primarily via the O-RAN A1 interface.

## IV. Evaluation and Results

### Simulation Setup
Simulations were conducted using Python 3.9, PyTorch, and OpenAI Gym. Two environments were created: one for high-level QMIX agents and one for low-level NAF DQL agents. The state space for the high level includes available service types and KPIs; the action is selecting a discrete slice type (0–4).

### High-Level Results
Loss converged around 5,000 episodes, and rewards showed an ascending linear trend. This indicates that the MARL agents learned to maximize resource utilization (network capacity) while making optimal slice assignments.

### Low-Level Results
All five single agents (each trained for one service type) showed loss convergence after approximately 6,000 epochs. The use of a decaying epsilon strategy ensured efficient exploration before transitioning to exploitation via the replay memory.

### KPI Testing
The trained model was tested over 1,000 episodes across three critical KPIs:
- **FeMBB**: System peak data rate remained above $1\text{ Tbps}$ and user-experienced rates stayed above $1\text{ Gbps}$.
- **ERLLC**: Latency was consistently kept below $10\,\mu\text{s}$.
The results confirm that the two-level approach successfully maintains strict 6G QoS requirements.

## V. Conclusion and Future Steps
The authors conclude that the proposed two-level DRL framework is a scalable and practical solution for managing network slicing in O-RAN-based CF mMIMO networks. Future improvements include:
1. Integrating communication link clustering strategies into the low-level agent's logic.
2. Training agents to be versatile across all service types rather than specializing in one per agent.
3. Testing other DRL algorithms and more diverse network environments.
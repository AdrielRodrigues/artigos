---
index_terms:
  - traffic steering
  - federated learning
  - on-device intelligence
  - transfer learning
  - model compression
  - 5G radio access networks
  - deep reinforcement learning
---

# On-Device Intelligence for 5G RAN: Knowledge Transfer and Federated Learning Enabled UE-Centric Traffic Steering

## I. Introduction
Traffic steering (TS) distributes network traffic across transmission paths to connect user equipment (UE) to the optimal base station (BS). Conventional cell-centric TS is centralized, focusing on overall cell performance while ignoring individual UE requirements, leading to high computational burdens on controllers and privacy risks. 

UE-centric TS allows UEs to make autonomous decisions based on local observations, improving scalability, preserving privacy, and tailoring Quality of Service (QoS) for diverse users. However, UE-centric ML faces challenges: limited local data, slow convergence, the "cold start" problem for new UEs, and constrained device resources (energy/compute). 

The authors propose a **Knowledge Transfer and Federated Learning-enabled UE-Centric (KT-FLUC)** TS framework. It integrates three main components:
1. **Attention-weighted group federated learning** to coordinate local decisions and share experience via a global model.
2. **Growing and pruning-based model compression** to reduce the computational and communication overhead on resource-constrained UEs.
3. **Q-value-based knowledge transfer** to provide newcomers with a "jump start" using expert knowledge from existing users.

## II. Related Work
Existing cell-centric TS research focuses on centralized DRL for handover and offloading, which improves average network efficiency but incurs high signaling overhead and risks user privacy. While some UE-centric frameworks exist (using link state prediction or Q-learning), they often overlook the limited resources of mobile devices, fail to facilitate collaboration between UEs, or assume unrealistic static network environments. KT-FLUC differs by combining RL, FL, knowledge transfer, and model compression within a dynamic environment where users join and leave frequently.

## III. System Model and Problem Formulation

### A. Architecture
The system comprises $M$ UEs and $N$ BSs (one LTE Macro BS and $N-1$ 5G Small BSs) supporting dual connectivity for downlink transmission. UEs are categorized by service type: Guaranteed Bit Rate (GBR), which is delay-sensitive, and non-GBR, which requires high throughput.

### B. Communication Model
Total communication delay ($d_m$) equals queuing delay plus transmission delay. Transmission delay is determined by packet length divided by link capacity. Link capacity depends on the signal interference noise ratio (SINR), governed by Shannon's theorem, bandwidth, and transmission power.

### C. Problem Formulation
The goal is to maximize a UE-specific utility function $U_m$:
- **For GBR traffic:** Utility is $1 - d_m/D_{max}$ (minimizing delay).
- **For non-GBR traffic:** Utility is $b_m/B_{max}$ (maximizing throughput).

The problem is formulated as a Markov Decision Process (MDP) because optimal BS selection depends on stochastic parameters and impacts long-term rewards, making traditional optimization difficult.

## IV. Proposed TS Scheme

### A. Algorithm Framework
The KT-FLUC framework operates in stages: first, model compression determines the optimal NN size. Then, grouped attention-weighted FL aggregates experiences from UEs into a global model. This global model is transferred to UEs as an "expert model." In local training, UEs use both their evolving local model and the static expert model for decision-making. Newcomers are initialized using the current global model parameters.

### B. Federated Reinforcement Learning Based UE-Centric TS
Each UE acts as a Deep Q-Network (DQN) agent:
- **State:** RSSI from all BSs, queue length, last packet delay, and currently attached BS.
- **Action:** Selection of the optimal serving BS.
- **Reward:** Defined by the utility function based on traffic type (GBR vs. non-GBR).

**Grouped Attention-Weighted FL:** UEs are grouped by traffic type to ensure relevant experience sharing. To avoid "noisy" updates from poorly trained models, a SoftMax-based attention mechanism assigns weights ($w_m$) to local models based on three indicators: average reward, training data size, and the achievement rate of QoS requirements. The global model is a weighted sum of these local models, which are then used to update local agents via a blending parameter $\eta_2$.

### C. Growing and Pruning-Based Model Compression
To reduce device overhead, NN size is optimized in two phases:
1. **Growing Phase:** Neurons are added by splitting the most "competitive" neurons (those with the lowest Percentage of Zeros (PoZ) after ReLU activation) until reward gains stabilize.
2. **Pruning Phase:** Neurons with the highest PoZ (least competitiveness) are removed one by one.

A specific weight initialization method is used during neuron splitting to ensure that the NN output remains identical immediately after a split, preventing performance decay during the growth process.

### D. Q-Value-Based Knowledge Transfer
Each UE maintains a **Local Model** (trained via local experience) and an **Expert Model** (a replica of the global model). The final TS action is chosen by maximizing the sum of the Q-values from both models: $a = \text{argmax}(Q_{local} + Q_{expert})$.

For newcomers, the global model initializes both their local and expert models. To ensure synergy, a modified loss function is used so that the sum of local and expert Q-values converges toward twice the long-term reward. This architecture allows local training and global aggregation to occur in parallel, as UEs do not need to wait for global feedback before continuing local updates.

### E. Baselines
The framework is compared against:
1. **CL:** Cell-centric centralized DRL.
2. **DIL:** Distributed independent DRL (no experience sharing).
3. **FL:** Standard federated DRL without knowledge transfer.
4. **FLI:** Federated DRL with direct initialization for newcomers.

### F. Computational Complexity Analysis
UE complexity is $O(\sum N_{i-1}N_i)$, proportional to NN size. RAN controller complexity is $O(M\sum N_{i-1}N_i)$, proportional to the number of UEs and NN size. Since global aggregation is non-real-time, the system maintains high scalability as the number of UEs increases.

## V. Simulation Settings and Results

### A. Simulation Settings
Simulations used 5 BSs (1 MBS, 4 SBS) with a mix of GBR (40%) and non-GBR (60%) traffic across varying UE densities (25 to 65). Parameters included 3GPP urban macro/micro channel models and an initial hidden layer size of 32 and 64 neurons.

### B. Performance Analysis Between UE-Centric TS and Cell-Centric TS
KT-FLUC achieves higher system rewards than both CL and DIL. While CL may perform better with very few UEs due to centralized coordination, it degrades as UE numbers increase. KT-FLUC significantly outperforms CL in high-density scenarios, achieving 52% higher throughput for non-GBR traffic and 65% lower delay for GBR traffic when $M=65$. This is attributed to the cell-centric approach's tendency to prioritize aggregate rewards over individual GBR constraints.

### C. Performance Analysis Between Four UE-Centric Frameworks
Comparing UE-centric methods: $\text{KT-FLUC} > \text{FLI} > \text{FL} > \text{DIL}$.
- **DIL** is unstable and oscillates due to a lack of experience sharing.
- **FL** improves stability via shared knowledge.
- **FLI** performs better than FL because initializing newcomers prevents them from contributing "lousy" experience to the global model.
- **KT-FLUC** provides the best performance by using expert models to guide local training and parallelizing aggregation, reducing total running time by 10% compared to FLI.

### D. Performance Analysis of Model Compression
Pre-simulations show that reward increases during the growing phase until a plateau is reached. During pruning, reward remains stable as redundant neurons are removed, eventually dropping sharply once the model becomes too small. The authors identified a threshold of 40 neurons where effectiveness remains above 90%, allowing a compression rate of 1.5 without compromising performance.

## VI. Conclusion
The proposed KT-FLUC framework optimizes traffic steering by leveraging grouped attention-weighted FL for robust global models, knowledge transfer for efficient newcomer integration, and model compression for device efficiency. Results demonstrate superior convergence, stability, and QoS (throughput/delay) compared to centralized and basic distributed methods. The authors suggest this architecture is extensible to other RAN functions like sleep control and edge caching.
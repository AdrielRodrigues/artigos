---
index_terms:
  - multi-band optical networks
  - routing and spectrum assignment
  - deep reinforcement learning
  - blocking probability
  - physical layer impairments
  - quality of transmission
---

# Deep Reinforcement Learning for Resource Allocation in Multi-Band Optical Networks

## Abstract
The paper introduces a Deep Reinforcement Learning (DRL) strategy for Routing and Spectrum Assignment (RSA) in multi-band (MB) optical networks. To ensure accurate performance estimation, the authors integrate the GNPy library. Simulation results indicate that this DRL-RSA approach can reduce blocking probability by up to 80% compared to existing state-of-the-art RSA strategies.

## I. Introduction
Global data traffic growth necessitates increased network capacity. Multi-band (MB) transmission is a viable solution to expand bandwidth without deploying new fiber; however, it increases complexity for Routing and Spectrum Assignment (RSA) due to disparate performance across different frequency bands and a higher number of channels. While traditional heuristic algorithms like k-Shortest Path (k-SP) and First-Fit (FF) are common, they struggle with the non-linear physical layer constraints of MB networks.

The authors propose a DRL-based RSA strategy that learns from network interactions via rewards and penalties. Unlike previous RL attempts in MB networks that failed to outperform heuristics, this approach utilizes the Generalized Gaussian Noise (GGN) model through the GNPy tool to account for wide-band impairments such as Stimulated Raman Scattering (SRS). The contribution includes a novel reward function that considers both path hops and frequency slot usage to optimize resource allocation.

## II. Proposed Approach for Routing and Spectrum Assignment
The DRL framework consists of an agent interacting with an MB network environment. For every connection request, the agent observes the available spectrum across all precomputed paths and bands, then takes an action defined as a tuple of (path, band, channel). 

### Reward Function
A specific reward function is implemented to drive the agent's learning:
- **Successful Establishment:** The agent receives a positive reward calculated as $1 + \frac{1}{\alpha \times \beta}$, where $\alpha$ is the number of allocated channels and $\beta$ is the number of hops. This incentivizes the use of shorter paths and fewer spectral resources.
- **Blocked Request:** The agent receives a penalty of $-1$.

### Implementation and Training
The strategy is built upon the Optical RL-Gym toolkit with two primary enhancements: the integration of GNPy for physical layer impairment modeling and the aforementioned reward function. The agent uses Proximal Policy Optimization (PPO) as its policy optimizer. Training is conducted offline using a digital twin of the network across various traffic loads to allow the agent to adapt to dynamic requests before deployment in a real network.

## III. Simulation Results
The authors evaluate the DRL-RSA strategy using the Japanese network topology (14 nodes, 44 links) with Poisson-distributed traffic loads between 200 and 450 Erlang. Requests are 400 Gb/s, served either via a single DP-16QAM channel (75 GHz) or two DP-QPSK channels (150 GHz), depending on the Generalized Signal-to-Noise Ratio (GSNR).

### Blocking Probability (BP) and Throughput
Across all strategies, BP increases with traffic load. At high loads (450 Erlang), DRL-RSA achieves a significantly lower BP ($3.1 \times 10^{-2}$) than RL-based RSA ($7.7 \times 10^{-2}$) and k-SP FF ($16.5 \times 10^{-2}$). While k-SP FF is slightly more efficient at very low loads, DRL-RSA reduces BP by approximately 80% compared to k-SP FF and 50% compared to RL-RSA as traffic increases. Consequently, the network throughput increases by 20% and 50% over RL-RSA and k-SP FF, respectively.

### Interface Usage and Path Selection
DRL-RSA demonstrates lower average transmitter/receiver (TX/RX) interface usage per demand than RL-RSA. This is because DRL-RSA prefers shorter paths, which maintain higher GSNR values, allowing the use of a single DP-16QAM channel instead of multiple DP-QPSK channels. Unlike heuristic FF approaches, the DRL agent dynamically adjusts its path assignment policy based on real-time network congestion and rewards.

### Spectrum Utilization per Band
The agent autonomously learned to prioritize bands in the order of C > L > S > E (with 43%, 27%, 16%, and 14% usage respectively) without being explicitly programmed with this hierarchy. This prioritization emerged from the agent's internal optimization for path length and GSNR values during training.

## IV. Conclusion
The proposed DRL-based RSA strategy effectively manages resource allocation in multi-band optical networks by accounting for SRS impairments and utilizing a resource-aware reward function. Simulations show that at medium to high traffic loads, it significantly outperforms both heuristic k-SP FF and standard RL strategies in terms of blocking probability, throughput, and interface efficiency.
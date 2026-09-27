---
index_terms:
  - Digital Subcarrier Multiplexing (DSCM)
  - Point-to-Multipoint coherent optics
  - 6G X-Hauling
  - Quality of Transport (QoT) estimation
  - Metro-access convergence
  - Random Forest regression
---

# AI-driven converged metro-access optical network-as-a-service with point-to-multipoint coherent optics for 6G X-Hauling

## 1. Introduction
Future 6G networks require ultra-low latency, high capacity, and energy efficiency to support data-intensive applications like extended reality and autonomous systems. While transparent optical networks can provide the necessary backbone, traditional Point-to-Point (P2P) architectures are inefficient for dense deployments due to linear scaling of hardware, spectral fragmentation, and poor handling of asymmetric traffic. 

To address this, the paper proposes a converged metro-access Optical Network-as-a-Service (ONaaS) architecture utilizing coherent Point-to-Multipoint (P2MP) transmission powered by Digital Subcarrier Multiplexing (DSCM). DSCM allows for fine-grained bandwidth allocation and improved spectral efficiency. The authors aim to evaluate the feasibility of this architecture under strict 6G functional split 7-2 requirements, specifically focusing on Bit Error Rate (BER) and latency constraints. Because managing subcarrier-level resources increases complexity, the paper integrates Software Defined Networking (SDN) and Network Function Virtualization (NFV), while introducing a machine learning (ML) based estimator for rapid Quality-of-Transport (QoT) prediction.

## 2. Metro-access convergence
Modern RAN disaggregation splits functions into Central Units (CUs), Distributed Units (DUs), and Radio Units (RUs). The transport segments—fronthaul (RU-DU) and midhaul (DU-CU)—must handle high capacity and strict latency to support the virtualized approach.

### 2.1. Functional split
The authors focus on the O-RAN Alliance Option 7-2x split, which balances RU complexity with fronthaul bandwidth. For a typical configuration (100 MHz radio bandwidth, 64-QAM), the peak fronthaul bandwidth is approximately 22.2 Gb/s. This demand aligns well with DSCM technology, where a single digital subcarrier provides up to 25 Gb/s, allowing for an efficient one-to-one mapping between traffic demands and optical resources.

### 2.2. Converged metro-access using DSCM-based coherent pluggable
The proposed architecture uses a central Hub (400G) connected to multiple leaf nodes via a passive Splitter/Combiner. Using DP-16QAM modulation, a single 400G wavelength is divided into 16 digital subcarriers (DSCs), each supporting 25 Gb/s. Bidirectional (BiDi) communication is achieved through circulators, allowing full-duplex transmission over a single fiber. This P2MP approach reduces the need for active electronics in the distribution segment and maximizes spectral utilization compared to P2P links.

## 3. Methodology

### 3.1. Experimental testbed
The authors used a back-to-back (B2B) experimental setup with a 400G DSCM coherent pluggable to isolate transceiver (TRX) impairments from fiber line impairments. By varying Received Optical Power (ROP) using a Variable Optical Attenuator, they characterized the relationship between ROP and Signal-to-Noise Ratio ($SNR_{TRX}$). This was modeled as a functional relationship where performance saturates at high ROP but degrades steeply at low ROP near receiver sensitivity limits. This experimentally derived model is embedded into the network simulator to ensure realistic feasibility analysis.

### 3.2. Statistical simulation model
The study utilizes two distinct topologies: $N_1$ (37 nodes, moderate connectivity) and $N_2$ (63 nodes, high redundancy/diversity). These networks consist of metro ROADM nodes (M-nodes) and access nodes (A-nodes), with DUs strategically placed at M-nodes. 

The Python-based simulator evaluates route feasibility by calculating a physical-layer budget that includes fiber attenuation, ROADM insertion loss, amplifier noise, and the aforementioned TRX impairments. Feasibility is determined based on:
1. **BER:** Calculated using the combined effects of Generalized SNR (GSNR) and $SNR_{TRX}$.
2. **Latency:** Modeled as propagation delay ($\approx 5 \mu s/km$).
The simulation uses a Monte Carlo approach to evaluate various hop limits and DU densities under split 7-2 constraints.

### 3.3. ML-based QoT estimation
To avoid the computational burden of exhaustive physical-layer simulations in large networks, the authors propose a regression framework for BER prediction. 

**Feature Selection:** To ensure the model is lightweight, it avoids using parameters derived from full physical calculations (like GSNR). Instead, it uses structural features: `distance` (cumulative impairment proxy) and `boundary_id` (representing source-destination pair diversity).

#### 3.3.1. Training and testing strategy
The model is trained on the simplest configuration (1DU in $N_2$) to ensure it learns general BER behaviors rather than specific routes. It is then tested for:
* **Scalability:** Moving from 1DU to 5DU within $N_2$.
* **Generalization:** Cross-topology testing ($N_2 \rightarrow N_1$).
The researchers also varied the training dataset size (from 10% to 100%) and introduced additive Gaussian noise to test robustness.

#### 3.3.2. Model selection and performance
Linear Regression, Decision Trees, and Random Forest (RF) models were compared using the coefficient of determination ($R^2$). The Random Forest model was selected as the primary estimator because its ensemble structure effectively captures non-linear relationships and reduces overfitting, providing the highest predictive accuracy.

## 4. Results and discussion

### 4.1. Route feasibility analysis
Route feasibility decreases as hop limits increase; beyond 8 hops, most additional routes are non-feasible due to accumulated physical impairments rather than latency alone. Topology $N_2$ shows higher sensitivity to these impairments than $N_1$ because its larger scale and routing diversity lead to longer average paths and greater SNR degradation. This suggests that in converged metro-access networks, connectivity is fundamentally bounded by the physical layer.

### 4.2. Impact of DU placement
Using topology $N_2$, the authors found that DU placement significantly affects the proportion of feasible routes. Placing DUs at highly connected metro nodes reduces average end-to-end path lengths, thereby limiting cumulative attenuation and noise. For instance, in a 3DU scenario, optimized placement increased "strictly feasible" (BER $< 10^{-3}$, latency $< 250 \mu s$) routes compared to suboptimal placements, proving that strategic positioning is more impactful than simply increasing the number of DUs.

### 4.3. QoT estimation with complexity constraints
The RF-based estimator demonstrates high accuracy ($R^2 > 0.98$) and generalizes well across topologies and DU densities. It reaches performance saturation with only 10%–20% of the training data. 

In terms of computation:
* **Exhaustive Simulation:** Time grows sharply with DU density (e.g., $\approx 35$ mins for 1DU to $\approx 389$ mins for 5DU).
* **ML Approach:** Requires a one-time dataset generation and training step, after which inference takes milliseconds.
The total computational reduction is approximately $11\times$, with the inference speedup being five orders of magnitude faster than simulation.

### 4.4. Techno-economic gains of P2MP over P2P
Comparing P2MP (DSCM) and conventional P2P architectures over a 10-year traffic projection (17.2% CAGR):
* **Hardware:** P2MP reduces the number of transceivers at DU sites by $\approx 75\%$ and network-wide transceivers by up to $74.1\%$.
* **Infrastructure:** Router port expansion is delayed due to more efficient subcarrier-level aggregation.
* **Energy:** P2MP achieves a $27\text{--}30\%$ reduction in power consumption under high spectral loads, significantly lowering OPEX.

## 5. Conclusion and future work
The paper demonstrates that an AI-driven P2MP architecture using DSCM is feasible for 6G X-haul, provided DUs are strategically placed to minimize physical impairments. The developed Random Forest estimator enables scalable ONaaS by providing near-instantaneous BER predictions with minimal training data. Techno-economically, the P2MP approach offers substantial CAPEX and OPEX savings over P2P. Future research will explore AI-driven resource allocation for subcarriers and SDN-based telemetry for on-demand reconfigurability.
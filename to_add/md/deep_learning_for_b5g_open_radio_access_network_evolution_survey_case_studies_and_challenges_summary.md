---
index_terms:
  - Beyond 5G (B5G)
  - Open RAN (O-RAN)
  - Deep Learning
  - RAN Intelligent Controller (RIC)
  - MLOps
  - Network Slicing
---

# Deep Learning for B5G Open Radio Access Network: Evolution, Survey, Case Studies, and Challenges

## I. Introduction
Beyond fifth-generation (B5G/6G) networks aim to provide ultra-low latency, high reliability, and massive connectivity to support "connected intelligence" use cases like autonomous systems and telemedicine. Traditional Radio Access Networks (RAN) cannot meet these requirements, necessitating a shift toward software-driven, virtualized architectures leveraging Software Defined Networking (SDN) and Network Function Virtualization (NFV). The O-RAN Alliance introduces a disaggregated RAN architecture where functions are implemented as software components with open interfaces, enabling the integration of Deep Learning (DL) via a hierarchical RAN Intelligent Controller (RIC) to optimize resource management, mobility, and spectrum.

### A. Review of Related Works
Existing surveys typically focus on Cloud-RAN (C-RAN), Virtualized RAN (vRAN), or Fog RAN (F-RAN). While some initial O-RAN studies describe the architecture's general benefits and limitations, there is a gap in mapping specific existing DL-based RAN solutions to the newly emerged O-RAN architectural framework.

### B. Contributions
The paper contributes by:
1. Providing an evolutionary overview and comparison of C-RAN, vRAN, and O-RAN.
2. Reviewing and mapping existing DL-based RAN research to the O-RAN architecture's functional blocks.
3. Proposing case studies for deploying supervised and reinforcement learning in O-RAN.
4. Introducing MLOps concepts to automate the DL lifecycle within O-RAN to combat model degradation.
5. Identifying open technical challenges and future research directions.

### C. Paper Structure
The document is organized as follows: Section II details RAN evolution; Section III maps DL works to O-RAN; Section IV presents deployment case studies; Section V discusses MLOps automation; Section VI analyzes open problems; and Section VII concludes the work.

## II. Evolution of RAN Architectures

### A. From Centralized 2G RAN to Distributed 3/4G RAN Architecture
In 2G, baseband and radio processing were co-located at base stations (BS). 3G/4G transitioned to a Distributed RAN (D-RAN), separating the Baseband Unit (BBU) from the Remote Radio Head (RRH), connected via a fronthaul network.

### B. Centralized and Cloudified RAN Architecture
C-RAN centralizes BBUs into a shared pool, linking multiple RRHs to this cloudified center. This centralization reduces energy consumption and improves scalability and spectral efficiency through virtualization of baseband processing.

### C. Virtualized RAN Architecture
vRAN leverages NFV and SDN to decouple the control and user planes and virtualize resources. It utilizes a DU Cloud where virtual BBUs (vBBUs) run on standard server hardware, allowing for dynamic capacity scaling and improved service reliability.

### D. Open RAN Alliance Architecture
O-RAN disaggregates hardware from software using open interfaces to prevent vendor lock-in. Its architecture consists of:
1. **Non-Real-Time (Non-RT) RIC:** Located at the Service Management and Orchestration (SMO) level; hosts rApps for intelligent optimization on timescales $> 1$ second. It provides policies to the Near-RT RIC via the A1 interface.
2. **Near-Real-Time (Near-RT) RIC:** Controls O-CU and O-DU via the E2 interface in a loop of 10ms–100ms; hosts xApps for spectrum, resource, and mobility management.
3. **O-RAN Central Unit (O-CU):** Split into Control Plane (O-CU-CP) and User Plane (O-CU-UP), managing RRC, SDAP, and PDCP protocols.
4. **O-RAN Distributed Unit (O-DU):** Manages RLC, MAC, and High-PHY layers, including scheduling and radio resource allocation.
5. **O-RAN Radio Unit (O-RU):** Handles Low-PHY and RF processing.
6. **Functional Split Options:** Defines the division of labor between CU, DU, and RU (e.g., Option 2 for high layer; Option 6/7 for low layer) to balance latency and centralization costs.
7. **RAN Deployment Scenarios:** Ranges from fully separated RU/CU/DU locations (requiring fronthaul, midhaul, and backhaul) to full integration of all three units in one location.
8. **O-RAN Slicing Use Cases:** Focuses on creating virtual networks with specific SLAs. ML models at the Near-RT RIC can monitor performance via the E2 interface and adjust RAN behavior to ensure SLA assurance.

### E. A Comparative Study
Compared to C-RAN and vRAN, O-RAN offers superior AI support (via dual RICs) and open interfaces for multi-vendor interoperability. While vRAN and O-RAN both offer low latency, low CAPEX/OPEX, and low energy consumption due to edge support and virtualization, O-RAN's distinguishing feature is its programmable, intelligent control plane and disaggregated functional blocks.

## III. Deep Learning Based Works for RAN
This section maps existing DL research into the O-RAN architecture based on the specific RIC module they would inhabit.

### A. Resources Management Optimization
**Literature Review:** Research focuses on predicting traffic congestion (using LSTM/Deep Tree models), optimizing spectrum allocation for VR users (via Echo State Networks), and dynamic resource scheduling (combining DNNs for large scales and RL for real-time dynamics). Power allocation studies utilize DRL (DQN, DDPG) to maximize sum-rate.
**Integration with O-RAN:** These functions map primarily to the **O-DU**, specifically targeting the MAC layer (resource assignment/scheduling) and High-PHY layer (PDSCH power allocation).

### B. Mobility Management Optimization
**Literature Review:** Research targets conditional handover predictions using DNNs and RNNs to reduce signal blockage risks in mmWave. Base station energy efficiency is addressed via RL (Q-learning, Actor-Critic) to optimize BS sleep modes relative to QoS requirements.
**Integration with O-RAN:** These functions map to the **O-CU-CP**, specifically within the UE/gNB and cell procedure management blocks.

### C. Spectrum Management Optimization
**Literature Review:** Focuses on physical layer tasks including channel estimation (DNNs for OFDM), signal encoding/decoding, and modulation classification (CNN/LSTM). Beam selection for mmWave is addressed using RL and DNNs to handle environmental blockages.
**Integration with O-RAN:** These functions are split between the **O-DU (High-PHY)** for estimation/encoding and the **O-RU (Low-PHY)** for beam selection.

## IV. Case Studies on Deep Learning Deployment in O-RAN

### A. Supervised Deep Learning Deployment
The paper highlights Federated Learning (FL) as an ideal fit for O-RAN's distributed nature. Instead of centralizing raw data, local models are trained at the **O-RU** level $\rightarrow$ weights are aggregated at the **Non-RT RIC** via the O1 interface $\rightarrow$ a global model is deployed to **Near-RT RIC xApps** $\rightarrow$ decisions are pushed to **O-DU/O-CU** via the E2 interface.

### B. Reinforcement Deep Learning Deployment
Agents are deployed at the **Near-RT RIC**. They interact with the RAN environment (O-RU, O-DU, O-CU) using a Markov Decision Process (MDP). Agents take actions via the E2 interface and receive rewards/state updates via the O1 interface. For DQN implementations, a prediction network is updated iteratively while a target network generates stable values to minimize loss.

## V. Automation of All Steps of Machine Learning System Construction in O-RAN
Because RAN data profiles evolve constantly (data drift), static models degrade. The paper proposes adopting MLOps to unify development and operations.

### A. Manual MLOps Process (Level 1)
A basic maturity level where data preparation, training, and deployment are manual. This is insufficient for the dynamic nature of B5G networks as it cannot react quickly to environmental changes.

### B. Automation MLOps Process (Level 2)
A high-maturity level featuring:
- **Continuous Training (CT) and Delivery (CD):** Automated pipelines that trigger retraining based on performance degradation or new data availability.
- **Data and Model Validation:** Checks for "schema skews" (incorrect features) or "value skews" (changed statistical patterns) before deploying updated models.
- **Metadata Management:** Tracking execution history to allow for debugging and model rollbacks.

## VI. Open Problems and Future Research Directions

### A. O-RAN Deployment Security Concerns
Disaggregation increases the attack surface. Open interfaces (A1, E2, front-haul) are vulnerable to Man-in-the-Middle attacks, which can corrupt training data and degrade DL model accuracy. Blockchain is proposed as a potential solution for decentralized authentication.

### B. Network Slicing Integration Concerns
Integrating slicing requires the SMO to manage slice templates and the RICs to monitor slice-specific SLAs. Database partitioning in the RICs is necessary to ensure isolation between slices, potentially using distributed FL.

### C. SON and MEC Integration Concerns
Self-Organizing Network (SON) functions for self-optimization can be integrated into both Non-RT and Near-RT RICs. Multi-access Edge Computing (MEC) integration would allow MEC hosts to reside in the Near-RT RIC, utilizing O-RAN databases for real-time traffic redirection based on user location.

### D. Online and Privacy-Preserving Distributed Learning Concerns
There is a need to shift from offline training at the Non-RT RIC to online, real-time learning within xApps at the Near-RT RIC. Federated Learning (FL) remains critical for maintaining privacy in multi-operator environments.

### E. Convergence and Scalability Concerns of Learning Techniques
As O-RAN scales, ensuring that distributed multi-agent RL converges quickly is a major challenge. Bootstrapping techniques are suggested to stabilize learning.

### F. Energy Concerns with Function Splitting of O-RAN
Optimizing the functional split (CU/DU/RU) using RL can reduce carbon footprints. Future research should explore "green O-RAN" by integrating renewable energy sources and network sharing techniques to optimize power usage under intermittent supply conditions.

## VII. Conclusion
The paper has surveyed the evolution toward O-RAN, mapped DL solutions to its architecture, provided deployment case studies for supervised/RL models, and proposed an MLOps framework for automation. Future work involves implementing these concepts using OpenAirInterface and the Amber open-source software.
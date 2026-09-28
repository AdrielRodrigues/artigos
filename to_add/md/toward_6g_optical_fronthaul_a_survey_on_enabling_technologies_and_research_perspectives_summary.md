---
index_terms:
  - 6G optical fronthaul
  - O-RAN architecture
  - functional splitting options
  - Passive Optical Networks (PON)
  - Free Space Optics (FSO)
  - network virtualization
  - software defined networking
---

# Toward 6G Optical Fronthaul: A Survey on Enabling Technologies and Research Perspectives

## I. Introduction
The anticipated shift toward Sixth Generation (6G) mobile technology by 2030 is driven by an exponential increase in global data traffic—projected to exceed 3 Zetabytes annually—and the need for ubiquitous, three-dimensional coverage. 6G aims to surpass 5G capabilities by offering unprecedented data speeds and ultra-low latency to support emerging applications such as holographic communications, the Internet of Everything (IoE), and Extended Reality (XR).

In the Radio Access Network (RAN) architecture, the fronthaul connects Remote Units (RUs) to Distributed/Digital Unit (DU) pools. While wireless solutions exist, optical technologies are identified as the most sustainable for 6G due to their high bandwidth, reliability, and scalability. This survey examines the current state of optical fronthaul, comparing various technologies and identifying future research trajectories.

### A. Scope of This Survey
The paper provides a comprehensive review of 6G optical fronthaul, covering the evolution of RAN architectures toward the Open-RAN (O-RAN) paradigm, an analysis of functional splitting options, a comparison of optical transport technologies (P2P, PON, FSO), and a discussion of current research projects and future challenges.

### B. Motivation
Existing literature primarily focuses on 5G backhauling or general optical communications. There is a distinct gap in comprehensive surveys specifically addressing the latest advancements and specific architectural requirements for 6G optical fronthaul, necessitating this updated resource for researchers and industry professionals.

### C. Structure of the Paper
The document is organized to move from high-level evolution (Section III) and interface specifications (Section IV) to specific technology assessments (Section V), state-of-the-art research (Section VI), current projects (Section VII), and future directions (Section VIII).

## II. Related Surveys and Our Contributions
The authors review several existing surveys, noting that while they cover C-RAN or 5G backhaul, they often fail to address the specific requirements of 6G, O-RAN interoperability, or a broad comparison across P2P, PON, and FSO technologies.

### A. Related Surveys
Previous works have explored C-RAN architecture [16], wireless backhaul [17], rural connectivity [19], and PON suitability for 5G [20]. More recent studies touched on NG-OANs [22] and the convergence of optical/wireless technologies [25]. However, none provide a holistic analysis tailored specifically to the 6G fronthaul transition.

### B. Survey Contributions
This paper contributes:
1. A comprehensive analysis of latest 5G/6G optical fronthaul advancements.
2. An overview of the progression toward 6G and O-RAN.
3. In-depth discussion on splitting options, capacity, and latency requirements.
4. Evaluation of P2P, PON, and FSO suitability for various 6G scenarios.
5. A review of current research efforts and major international projects.
6. Identification of future research directions to optimize 6G performance.

## III. Evolution Toward 6G

### A. From 5G to 6G
Wireless networks have evolved from basic analog voice (1G) to the high-capacity, low-latency standards of 5G. While 5G introduced eMBB, uRLLC, and mMTC, 6G is expected to provide a "quantum leap," targeting data rates $\geq 100$ Gbps (potentially reaching Tbps), latency $< 100 \mu s$, and reliability of $99.99999\%$. It intends to extend coverage across terrestrial, aerial, space, and sea domains.

### B. Major Challenges for 6G
Challenges are divided into two layers:
- **Radio Layer:** Necessity of utilizing previously unused spectrum, including the sub-THz (100–300 GHz) and Terahertz (100 GHz–10 THz) bands.
- **Transport Layer:** Requirement for ultra-high capacity, extreme resilience, and low latency from cell sites to the core. This includes a need for shared connections to reduce deployment costs and "Space-Earth integration" via satellites and stratosphere platforms.
- **Intelligence:** Integration of AI/ML is deemed imperative for autonomous network optimization.

### C. Lessons Learned
The transition requires continuous spectrum exploration, resilience in transport networks, the adoption of non-terrestrial connectivity (opening doors for FSO), and the shift toward intelligent, self-optimizing systems powered by AI/ML.

### D. RAN Landscape Evolution Toward O-RAN
RAN architectures have evolved to move processing functions and reduce costs:
- **D-RAN:** BBU is collocated with RRH; lacks scalability for 5G/6G.
- **C-RAN:** BBUs are centralized in a pool, allowing for advanced signal processing (CoMP, CA) and reduced site costs, though it places high demands on the fronthaul.
- **HC-RAN:** Integrates small BSs with macro BSs to improve capacity and energy efficiency through cloud computing.
- **F-RAN:** Decentralizes functions closer to users via fog computing to drastically reduce latency (up to 70% reduction) and offload central servers.
- **v-RAN:** Replaces proprietary hardware with software running on COTS servers, improving agility and scalability.
- **O-RAN:** An industry initiative for an open, interoperable infrastructure using standardized interfaces between the O-RU (Radio Unit), O-DU (Distributed Unit), and O-CU (Central Unit). This prevents vendor lock-in and provides a platform for AI/ML integration.

### E. Lessons Learned
The progression toward O-RAN reflects a need for agility and slicing. However, the practical hurdle remains the fronthaul infrastructure's ability to handle massive device density and diverse traffic demands while remaining cost-effective.

## IV. 6G Fronthaul Interface and Main Splitting Options

### A. Fronthaul Interface
The interface comprises several functional layers: RRC (control plane), PDCP (header compression/security), RLC (reliable transmission), MAC (scheduling/HARQ), and PHY (modulation/beamforming).

### B. Main Splitting Options
Functional splits represent trade-offs between centralization gains and fronthaul bandwidth requirements:
- **Option 8 (RF/PHY):** Fully centralized; lowest RU complexity but highest bandwidth and most stringent latency/jitter constraints.
- **Options 7, 6, 5, 4, 3, 2:** Gradually move more PHY/MAC functions to the RU, reducing fronthaul bitrate but increasing RU complexity.
- **Option 1 (PDCP/RRC):** Most distributed; lowest bandwidth requirements but highest RU complexity.
- **O-RAN Specific Splits (7.x family):** 
    - **7.1:** Frequency domain I/Q symbols; high bandwidth requirement.
    - **7.2:** Combined antenna port signals; reduced bandwidth compared to 7.1.
    - **7.3:** Moves modulation/demodulation to the RU, significantly reducing bitrate but increasing RU complexity.

Example: For a specific configuration, Option 7.1 requires $\sim 4.3$ Gbps, while 7.3 requires only $\sim 134$ Mbps. High-end configurations (Option 8) can demand $>800$ Gbps with latency $< 250 \mu s$.

### C. Lessons Learned
The choice of split determines the hardware requirements for RUs and the capacity needs of the optical transport network. O-RAN's flexible splitting allows operators to optimize based on specific use cases.

## V. Optical Communications Technologies for 5G/6G Fronthaul

### A. Motivation for 6G Optical Fronthaul
With projected peak rates $\geq 1$ Tbps and latency $\leq 0.1$ ms, optical solutions are the only viable paths to meeting these targets. The market for mobile fronthaul is expected to grow significantly toward 2030.

### B. Point-to-Point Optical Fiber (P2P)
Dedicated links between RUs and DUs provide maximum capacity, lowest latency, and high security. It is ideal for ultra-high bandwidth needs (Splits 7.1 and 8). Drawbacks include extreme fiber cost and lack of resource sharing (idle links cannot help busy ones). "XR optics" are mentioned as a software-driven approach to make P2P more flexible and reprogrammable.

### C. Passive Optical Networks (PONs)
PONs use a Point-to-MultiPoint (P2MP) architecture, reducing fiber costs through sharing. 
**Evolution:** From early A-PON/GPON to NG-PON2 (TWDM) and current HSP (up to 50 Gbps). Future "super-PON" targets $>100$ Gbps.
**Architectural Types:**
- **TDM-PON:** Cost-effective but hampered by DBA (Dynamic Bandwidth Allocation) processing delays, making it difficult to meet $\mu s$-level latency requirements.
- **WDM-PON:** High capacity and low latency (no DBA), but expensive due to wavelength filters.
- **TWDM-PON:** Combines TDM and WDM; offers high flexibility and coexistence with legacy GPON.
- **OFDM-PON:** High spectral efficiency, suitable for Tbps targets, but requires expensive coherent detection.
- **OCDM-PON:** Uses unique codes for security and asynchronous transmission.
- **NOMA-PON:** Power-domain multiplexing to increase user density; suffers from Self-Induced Intermodulation Interference (SSII).
- **PDM-PON:** Uses polarization diversity to achieve $\geq 100$ Gbps per wavelength.

### D. FSO for 5G and Beyond Fronthaul
Free Space Optics (FSO) uses lasers to transmit data through the atmosphere. It provides high bandwidth ($\sim 100$ Gbps), is unlicensed, and avoids cabling costs in remote or hard-to-reach areas.
**Use Cases:** Terrestrial towers, non-terrestrial networks (UAVs, HAPs, satellites), and underwater communication.
**Challenges:** Atmospheric attenuation (fog, rain) requires Line-of-Sight (LoS). Hybrid FSO/mmWave systems are proposed to ensure $99.999\%$ availability by switching between modalities based on weather.

### E. Lessons Learned
No single technology is sufficient; a hybrid approach is necessary. P2P serves extreme capacity, PONs offer cost-effective density, and FSO enables connectivity in challenging physical environments.

## VI. Cutting-Edge Research Related to 5G/6G Optical Fronthaul

### A. Optical Fronthaul Deployment Cost Reduction
Research focuses on infrastructure sharing (sharing fiber among operators), topology optimization, and repurposing existing residential optical networks to support mobile fronthaul.

### B. Energy Efficiency and Sustainability
Strategies include power-saving modes for ONUs, AI-driven DBA to enter sleep states during low traffic, and the use of passive WDM architectures (e.g., AWGR) to reduce active component energy consumption.

### C. Latency and Jitter Aspects
To avoid handover failures and poor QoS, research proposes encapsulating CPRI over Ethernet (CoE) and optimizing network topology to minimize hops and processing delays.

### D. Integration of Optical Fronthaul With Other Communication Technologies
- **Fiber + Wireless:** Combining optical backbones with mmWave/microwave links increases resilience; if a fiber is cut, the wireless link acts as a backup.
- **FSO + Wireless:** Hybrid FSO/mmWave architectures mitigate weather-induced outages (FSO fails in fog but works in rain; mmWave penetrates fog).

### E. Resource Allocation in the Optical Fronthaul
Efficient allocation improves total throughput and spectral efficiency. The focus is shifting toward AI-driven DBA that can predict traffic spikes and adjust bandwidth in real-time.

### F. ML- and AI-Empowered 6G Optical Fronthaul
AI/ML addresses "model deficits" (lack of physics models) and "algorithm deficits" (computational complexity).
- **Deep Learning:** Traffic flow pattern recognition.
- **Supervised/Unsupervised Learning:** Predicting loads and detecting anomalies/security breaches.
- **Reinforcement Learning:** Real-time routing optimization for latency and throughput.

### G. Enhancement of Flexibility... Using SDN
Software Defined Networking (SDN) allows centralized, programmable control of the fronthaul, enabling dynamic provisioning, proactive fault detection, and automated traffic grooming.

### H. Capacity Enhancement Using SDM
Space Division Multiplexing (SDM)—using multicore or few-mode fibers—is explored to break the capacity limit of single-core fibers, providing a scalable path toward Tbps per link.

### I. Security and Privacy Aspects
Focus areas include physical layer security, ML-based intrusion detection using Optical Performance Monitoring (OPM) data, and Root Cause Analysis (RCA) for autonomous security management.

### J. Lessons Learned
Research is moving toward "intelligent" networks where AI/ML, SDN, and SDM combine to create a resilient, high-capacity, and self-healing infrastructure.

## VII. Research Projects Related to 5G/6G Fronthaul
The paper summarizes various EU projects:
- **5G-PICTURE & 5G-XHaul:** Focused on disaggregated RAN (DA-RAN) and converged optical-wireless solutions.
- **6G Flagship & Hexa-X:** Defining the broader 6G vision, AI-driven air interfaces, and architectural enablers.
- **TERAWAY:** Developing THz transceivers for ultra-broadband fronthaul.
- **MARSAL & EMPOWER-6G:** Investigating cell-free networks and optical-wireless convergence.
- **FLEX-SCALE & PROTEUS-6G:** Targeting Pbps throughput, energy efficiency (sub-pJ per bit), and dynamic functional split management.

## VIII. Future Research Directions

### A. Capacity Enhancement
Focus on coherent PONs and FSO to reach Tbps levels through higher-order modulation and multi-dimensional signaling.

### B. Latency Reduction
Targeting $\leq 10 \mu s$ for critical services (telemedicine, V2X). This requires unified management layers to control end-to-end QoS in real-time and precise latency engineering.

### C. Improving Energy Efficiency
Research into new transceiver materials, renewable energy integration, and cross-layer optimization to reduce the environmental footprint of dense 6G networks.

### D. Cost-Efficient Deployment
Emphasis on upgrading existing fiber assets, network virtualization in PONs, and improving FSO robustness to make wireless optical links a viable cheaper alternative to digging trenches for fiber.

### E. Network Resilience
Developing self-healing mechanisms, hardware redundancy, and adaptive FSO systems that can reroute traffic autonomously during failures or extreme weather.

### F. Security and Privacy Aspects
Need for robust encryption, authentication protocols in PONs, and physical layer security (e.g., Quantum Key Distribution) for FSO to prevent eavesdropping.

### G. Standardization and Interoperability
Developing multivendor-compatible standards to avoid vendor lock-in within the O-RAN framework, ensuring seamless integration of diverse optical components.

### H. Accurate Time and Frequency Synchronization
Essential for Coordinated Multi-Point (CoMP) transmissions; requires new synchronization protocols to ensure precise alignment across distributed elements.

### I. Caching and Edge Computing
Strategically placing caches at the fronthaul layer to minimize latency for XR applications and offload traffic from the core network.

### J. Advanced Monitoring and Diagnostics Techniques
Using AI/ML for predictive maintenance and employing autonomous robotics for physical inspection and repair of optical infrastructure.

### K. Digital Twins (DTs) Empowered Optical Fronthaul
Creating virtual replicas of the physical fronthaul to simulate configuration changes, predict failures, and optimize resource allocation before implementing changes in the real network.

### L. Spatial Modulation for FSO-Based 6G Fronthaul
Applying Sparse Massive MIMO (SM-MIMO) to FSO links to improve spectral efficiency and mitigate atmospheric turbulence/beam wander.

## IX. Conclusion
The realization of 6G depends on an optimized fronthaul capable of supporting massive capacity and ultra-low latency. No single technology is a "silver bullet"; instead, the future lies in the integration of P2P (for extreme speed), PONs (for cost-effective density), and FSO (for challenging environments). The synergy of these technologies with AI/ML, SDN, and Digital Twins will be essential to achieving the ambitious targets of 6G.
---
index_terms:
  - 6G optical fronthaul
  - O-RAN architecture
  - functional splitting options
  - Passive Optical Networks
  - Free Space Optics
  - network virtualization
  - coherent PON
---

# Toward 6G Optical Fronthaul: A Survey on Enabling Technologies and Research Perspectives

## I. Introduction
The transition to Sixth Generation (6G) mobile technology by 2030 is driven by an exponential increase in global data traffic and the need for ultra-high data rates, near-instantaneous communication, and ubiquitous 3D coverage. While 5G focused on enhanced Mobile BroadBand (eMBB), ultra-Reliable and Low-Latency Communications (uRLLC), and massive Machine Type Communication (mMTC), 6G aims to surpass these via integration with Artificial Intelligence (AI), Extended Reality (XR), and the Internet of Everything (IoE). Key expected use cases include autonomous vehicles, holographic communication, digital twins, and the "Connected Sky" (UAVs/satellites).

Within the Radio Access Network (RAN), the fronthaul connects Remote Units (RUs) to Distributed/Digital Units (DUs). Optical technologies are identified as superior to wireless alternatives (microwave/mmWave) for 6G due to their higher bandwidth, reliability, and security. This survey explores optical fiber and Free Space Optics (FSO) as primary enablers for the Open RAN (O-RAN) paradigm, which emphasizes vendor interoperability and softwarization.

### A. Scope of This Survey
The paper reviews 6G optical fronthaul by analyzing wireless network evolution, RAN architectures, fronthaul interface splitting options, and a comparison of Point-to-Point (P2P), Passive Optical Network (PON), and FSO technologies, concluding with current research projects and future directions.

### B. Motivation
The authors argue that existing surveys lack a comprehensive comparison of all optical perspectives specifically for 6G fronthauling. There is a critical need for an updated resource to guide researchers in designing the high-capacity transport layers required for beyond-5G networks.

### C. Structure of the Paper
The document is organized into sections covering related surveys, evolution toward 6G, splitting options, optical technology evaluations, state-of-the-art research, current projects, and future challenges.

## II. Related Surveys and Our Contributions

### A. Related Surveys
The paper evaluates existing literature, noting that previous works focused primarily on either C-RAN generalities, specific PON solutions for 5G, or wireless backhauling. Most fail to address the combined requirements of 6G (Tbps speeds and $\mu$s latency) or provide a holistic comparison between P2P, PON, and FSO in the context of O-RAN.

### B. Survey Contributions
The primary contributions include: an analysis of latest 5G/6G optical fronthaul advancements; detailed discussion on functional splitting options (including 7.x); comparison of transport technologies relative to specific use cases; and identification of future research gaps in capacity, latency, and energy efficiency.

## III. Evolution Toward 6G

### A. From 5G to 6G
Wireless networks have evolved from basic analog voice (1G) to high-speed data (4G/5G). 6G is envisioned as a "quantum leap" offering peak data rates $\ge 100$ Gbps (potentially Tbps), latency $< 100 \mu s$, and reliability of "seven nines" (99.99999%). It expands coverage to terrestrial, aerial, space, and sea domains.

### B. Major Challenges for 6G
Challenges are split between the radio layer (utilizing THz bands and mmWave) and the transport layer (requiring resilient, ultra-high-capacity networks). Key hurdles include the need for Space-Earth integration via satellites/HAPs and the necessary infusion of AI/ML for autonomous network management.

### C. Lessons Learned
The authors conclude that 6G requires continuous spectrum exploration in THz bands, transport layer resilience to support emergent services, and a shift toward intelligent, self-optimizing systems powered by AI to handle the complexity of 3D connectivity.

### D. RAN Landscape Evolution Toward O-RAN
RAN has evolved through several stages:
- **Distributed RAN (D-RAN):** BBU collocated with RRH; lacks flexibility and scalability.
- **Centralized RAN (C-RAN):** BBUs pooled centrally; enables CoMP and Carrier Aggregation but requires high-capacity fronthaul.
- **Heterogeneous C-RAN (HC-RAN):** Combines macro and small BSs to improve throughput and energy efficiency.
- **Fog-RAN (F-RAN):** Decentralizes functions closer to the edge to reduce latency for IoT/autonomous apps.
- **Virtualized RAN (v-RAN):** Replaces proprietary hardware with software running on COTS servers (vBBUs).
- **O-RAN:** An industry initiative creating open, interoperable interfaces between O-RU, O-DU, and O-CU to avoid vendor lock-in and facilitate AI integration.

## IV. 6G Fronthaul Interface and Main Splitting Options

### A. Fronthaul Interface
The interface consists of functional layers: Radio Resource Control (RRC) for signaling; Packet Data Convergence Protocol (PDCP) for header compression/security; Radio Link Control (RLC) for reliability; Medium Access Control (MAC) for scheduling/HARQ; and the Physical layer (PHY) for modulation, beamforming, and MIMO.

### B. Main Splitting Options
Splitting options represent a trade-off between centralization benefits and fronthaul bandwidth:
- **Option 8 (Lower-Layer Split):** Fully centralized; lowest RU complexity but highest bandwidth/latency constraints.
- **Options 2-7:** Varying degrees of PHY/MAC distribution. Higher numbers (e.g., 6, 7) move more processing to the RU, reducing required bitrate.
- **O-RAN 7.x Family:** Specifically splits the PHY layer into 7.1, 7.2, and 7.3. Option 7.3 is the most efficient in terms of bitrate by moving demodulation/modulation to the RU, though it increases RU complexity.

The paper notes that for extreme configurations (Option 8 with massive MIMO), fronthaul capacity needs can exceed 800 Gbps with latency requirements under $250 \mu s$.

### C. Lessons Learned
Understanding the layers and splitting options is vital because each deployment scenario requires a different balance of RU complexity versus transport capacity. O-RAN's open interfaces are essential for tailoring these splits to specific use cases.

## V. Optical Communications Technologies for 5G/6G Fronthaul

### A. Motivation for 6G Optical Fronthaul
With targets of $\ge 1$ Tbps peak rates and $\le 0.1$ ms latency, optical solutions are necessary. The authors examine P2P, PON, and FSO to determine their suitability for these stringent requirements.

### B. Point-to-Point Optical Fiber (P2P)
P2P provides dedicated links between RUs and DUs.
- **Pros:** Lowest latency, highest security, and maximum capacity; ideal for splitting options 7.1 and 8.
- **Cons:** Extremely high deployment cost due to fiber quantity; poor resource utilization since resources are fixed to peak demand.
- **Advancements:** "XR optics" utilize coherent subcarrier aggregation to reduce costs and increase flexibility through software-driven reprogramming.

### C. Passive Optical Networks (PONs)
PON uses a point-to-multipoint (P2MP) architecture with power splitters.
- **Evolution:** Progressed from GPON $\rightarrow$ XGS-PON $\rightarrow$ HSP (50G).
- **Architectures:** 
    - *TDM-PON:* Cost-effective but suffers from high latency due to Dynamic Bandwidth Allocation (DBA) cycles ($\sim 125 \mu s$).
    - *WDM-PON:* Low latency and high capacity; avoids DBA but has higher optical costs.
    - *TWDM-PON:* Combines TDM and WDM; flexible and compatible with legacy systems.
    - *OFDM/OCDM-PON:* High spectral efficiency and security; suitable for Tbps targets.
    - *NOMA-PON:* Uses power-domain multiplexing to support more users per subcarrier.
    - *PDM-PON:* Uses polarization states to exceed 100 Gbps per wavelength.

### D. FSO for 5G and Beyond Fronthaul
FSO transmits data via light beams through the atmosphere.
- **Capabilities:** High bandwidth ($\sim 100$ Gbps), unlicensed spectrum, and ease of deployment in hard-to-reach areas.
- **Limitations:** Requires Line-of-Sight (LoS) and is highly susceptible to weather (fog/rain).
- **Mitigation:** Hybrid FSO/mmWave systems provide "carrier-grade" availability ($99.999\%$) because mmWave penetrates fog while FSO resists rain.
- **Applications:** Terrestrial tower links, non-terrestrial links (UAVs/HAPs), and underwater communication.

### E. Lessons Learned
No single technology is universal. P2P is for ultra-high capacity; PON is for cost-efficient density; FSO is for wireless flexibility. Hybrid combinations are the most likely path to meet 6G's diverse requirements.

## VI. Cutting-Edge Research Related to 5G/6G Optical Fronthaul

### A. Optical Fronthaul Deployment Cost Reduction
Research focuses on infrastructure sharing, topology optimization, and utilizing existing PON networks (repurposing residential fiber) to lower the barrier for ultra-dense 6G deployments.

### B. Energy Efficiency and Sustainability
Strategies include ONU power-saving modes, AI-driven DBA to enter sleep states during low traffic, and using decomposed Arrayed Waveguide Grating Routers (AWGR).

### C. Latency and Jitter Aspects
To support time-sensitive apps, research suggests encapsulating CPRI over Ethernet (CoE) and applying topology optimizations to minimize physical path delays.

### D. Integration of Optical Fronthaul With Other Communication Technologies
The focus is on hybridizing fiber with microwave/mmWave for resilience (backup links) and FSO with mmWave to ensure availability during adverse weather conditions.

### E. Resource Allocation in the Optical Fronthaul
Dynamic Bandwidth Allocation (DBA) is critical for throughput. Current trends involve moving toward AI-driven DBA to optimize spectral efficiency and power consumption in real-time.

### F. ML- and AI-Empowered 6G Optical Fronthaul
AI/ML addresses "model deficits" (lack of physics equations) and "algorithm deficits" (computational complexity). Applications include:
- **Traffic Prediction:** Adjusting splitting options dynamically.
- **Anomaly Detection:** Identifying faults or security breaches via unsupervised learning.
- **Routing Optimization:** Using Reinforcement Learning for real-time latency reduction.

### G. Enhancement of Flexibility and Reconfigurability in Optical Fronthaul Using SDN
Software Defined Networking (SDN) allows centralized control to dynamically reconfigure bandwidth and perform traffic grooming, improving the resilience of the fronthaul infrastructure.

### H. Capacity Enhancement of Optical Fronthaul Using SDM
Space Division Multiplexing (SDM), via multicore or few-mode fibers, provides a scalable way to increase total capacity beyond the limits of single-channel fibers.

### I. Security and Privacy Aspects
Research emphasizes physical layer security, ML-assisted monitoring of Optical Performance Monitoring (OPM) data for intrusion detection, and Root Cause Analysis (RCA) for autonomous security management.

### J. Lessons Learned
Current research highlights that 6G's success depends on the convergence of AI/ML for management, SDN for flexibility, and SDM for raw capacity, all while maintaining a focus on energy sustainability.

## VII. Research Projects Related to 5G/6G Fronthaul
The paper summarizes numerous EU-funded projects:
- **5G-PICTURE:** Focused on resource disaggregation (DA-RAN).
- **6G Flagship & Hexa-X:** Defining the overall 6G architectural enablers and AI-driven air interfaces.
- **FLEX-SCALE:** Targeting massive capacity scaling (10 Pb/s throughput per node) and sub-pJ energy efficiency.
- **PROTEUS-6G:** Developing packet-optical fronthaul for dynamic management of radio functional splits.
- Other projects include TERAWAY (THz transceivers), MARSAL (cell-free O-RAN), and EMPOWER-6G (converged optical-wireless).

## VIII. Future Research Directions

### A. Capacity Enhancement
Focus is on coherent PONs to achieve $\ge 100$ Gbps/$\lambda$ and exploring higher-order modulation formats for FSO to support Tbps requirements.

### B. Latency Reduction
To reach $< 10 \mu s$, research must move toward P2P architectures with unified management layers and real-time monitoring tools that isolate latency violations across different network domains.

### C. Improving Energy Efficiency
Future work should explore new transceiver materials, renewable energy integration (solar/wind), and cross-layer optimization between the physical and network layers.

### D. Cost-Efficient Deployment
Emphasis is on repurposing existing fiber, utilizing PON virtualization for multi-tenant sharing, and developing adaptive modulation for FSO to increase its reliability in cheap deployments.

### E. Network Resilience
Research directions include self-healing mechanisms that autonomously reroute traffic during failures and adaptive optics for FSO to combat atmospheric turbulence.

### F. Security and Privacy Aspects
Priorities include robust encryption, authentication protocols for PONs, and physical layer security (e.g., beamforming and quantum key distribution) for FSO links.

### G. Standardization and Interoperability
There is an urgent need for standardized multivendor interfaces in O-RAN to prevent vendor lock-in and ensure that P2P, PON, and FSO components can coexist seamlessly.

### H. Accurate Time and Frequency Synchronization
Advanced synchronization is required to enable Coordinated Multi-Point (CoMP) transmission, which is essential for 6G reliability.

### I. Caching and Edge Computing
Strategically placing caches at the fronthaul layer can offload the core network and reduce latency for XR applications.

### J. Advanced Monitoring and Diagnostics Techniques
Future networks require AI-driven predictive maintenance and autonomous robotic systems for physical fiber inspection and repair.

### K. Digital Twins (DTs) Empowered Optical Fronthaul
Digital twins (virtual replicas) can be used for proactive capacity planning, simulating configuration changes before deployment, and early fault detection.

### L. Spatial Modulation for FSO-Based 6G Fronthaul
Sparse Massive MIMO (SM-MIMO) is proposed to increase FSO throughput and mitigate the effects of atmospheric beam wander through spatial diversity.

## IX. Conclusion
Realizing 6G requires a hybrid optical approach. P2P satisfies ultra-high capacity/low latency but is costly; PON offers cost-effective density but needs coherent upgrades for Tbps speeds; FSO provides wireless flexibility but requires weather-resilient modulation. No single technology is sufficient; the integration of these technologies, managed by AI and SDN, is the only viable path to meeting 6G's requirements.
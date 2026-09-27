---
index_terms:
  - 6G wireless communication
  - IMT-2030 recommendations
  - Integrated Sensing and Communication (ISAC)
  - Orbital Angular Momentum (OAM) multiplexing
  - Terahertz (THz) communications
  - Reconfigurable Intelligent Surfaces (RIS)
---

# Toward 6G Evolution: Three Enhancements, Three Innovations, and Three Major Challenges

## Abstract
The paper provides a technical overview of the transition from 5G to 6G, specifically aligned with the IMT-2030 vision. It examines three extensions of existing 5G pillars (IMT-2020) and three new functional innovations. The authors analyze implementation challenges regarding standardization, spectrum management, and security, while providing a proof-of-concept for high-speed data transmission using sub-THz orbital angular momentum (OAM) multiplexing.

## Introduction
The roadmap for 6G is guided by the IMT-2030 recommendations, which seek to enhance network flexibility through the integration of artificial intelligence (AI), integrated sensing and communication (ISAC), and non-terrestrial networks (NTNs). The authors identify three primary challenges: effective spectral/energy utilization, technology harmonization across diverse systems, and data security within AI-driven architectures. A key focus is whether terahertz (THz) spectrum can be effectively utilized to meet future capacity needs.

## Background and Motivation
Wireless communication has evolved from basic analog voice (1G) to digital text/voice (2G), mobile internet (3G), high-speed broadband (4G), and the flexible, multi-service framework of 5G. The move toward 6G begins with 3GPP Release 21, which is expected to establish the first official technical specifications for 6G. This evolution shifts from purely communication-centric networks toward an adaptive framework that integrates sensing and intelligence.

## Wireless Evolution and Trend Ahead

### Evolution of Wireless Communication: From 1G to 6G
The progression of wireless generations has been driven by advancements in VLSI circuits, MIMO, and OFDM:
*   **1G:** Analog cellular; basic voice with poor security and capacity.
*   **2G:** Transition to digital (GSM/CDMA), introducing SMS and early data (GPRS/EDGE).
*   **3G:** Enabled mobile internet through HSPA and CDMA-2000 via the 3GPP standardization body.
*   **4G:** Established mobile broadband using all-IP networks, MIMO, and OFDM (3GPP Releases 8–14).
*   **5G:** Introduced mmWave, massive MIMO, and network slicing to support diverse use cases, including AR and IoT via RedCap (Reduced Capability).
*   **6G Expectations:** Focuses on ultra-high speed, low latency, and AI-native architectures. 3GPP Release 20 (5G-Advanced) bridges the gap, while Release 21 marks the start of normative 6G development for services like digital twins and the metaverse.

### Lessons Learned and Trend Ahead
Analyzing wireless evolution through Shannon's capacity theorem ($C = NB \log_2(1+SINR)$), the authors observe three primary levers for increasing data rates:
1.  **Bandwidth ($B$):** Shifting to higher frequencies (THz band) to increase per-user bandwidth from MHz to GHz.
2.  **Antenna Pairs ($N$):** Scaling from high-order MIMO to massive MIMO to create more parallel data paths.
3.  **Channel Conditions ($SINR$):** Using Reconfigurable Intelligent Surfaces (RIS) to transform the environment from an uncontrollable impairment into a controllable variable that enhances signal strength.

#### Pathway to 6G: IMT-2030 Enhancements and Innovations
The authors categorize 6G development into extensions of existing 5G capabilities and entirely new innovations. This involves shifting toward AI-driven virtualization for network function management (NFV) and using ISAC for advanced beam prediction via angle of arrival (AoA) estimation.

#### IMT-2020 Extensions: A Closer View
1.  **Enhanced URLLC (HRLLC):** Evolves Ultra-Reliable Low Latency Communication into "Hyper-Reliable" communication. This requires moving computation to the extreme edge to reduce delays and utilizing the THz band for higher reliability in critical tasks like remote surgery.
2.  **Redefining eMBB (Immersive Communication):** Moves beyond mobile broadband toward immersive experiences using Extremely Large-scale MIMO (XL-MIMO) for spatial degrees of freedom and Cell-Free MIMO (CF-MIMO) to eliminate traditional cell boundaries.
3.  **Beyond mMTC (Massive Communication):** Expands massive Machine Type Communication to a broader ecosystem, specifically integrating non-terrestrial networks (NTN/satellites) to achieve global coverage for the Internet of Everything (IoE).

## 6G Innovations: Newly Added Capabilities
1.  **Ubiquitous Connectivity:** Aims for seamless access regardless of location by combining sensors and devices through cell-free architectures, enabling use cases like precision farming.
2.  **Integrated Sensing and Communication (ISAC):** Fuses sensing and data transmission to allow the network to perform localization and channel estimation simultaneously, improving beamforming and resource efficiency.
3.  **IAAC (Integrated AI and Communication):** Embeds AI into the protocol stack for predictive bandwidth management and spectrum optimization. AI is also used at the edge for faster response times in autonomous systems and for proactive cyber-threat detection.

## Pathway to 6G: Associated Challenges and Efforts

### Associated Challenges: An Insight
1.  **6G Standardization:** The lack of global consensus on performance requirements and the difficulty of integrating AI across different layers of the protocol stack pose significant hurdles. Divergence between bodies like 3GPP and ETSI may hinder harmonization.
2.  **Spectrum Planning and Management:** While THz bands offer Tbps speeds, they face severe propagation losses and a lack of regulatory consensus. Additionally, ensuring backward compatibility with 5G is essential for a smooth transition.
3.  **Security and Privacy:** AI-driven networks are vulnerable to data poisoning and adversarial attacks. ISAC introduces privacy risks by exposing environmental/user data via sensing. Furthermore, while quantum key distribution (QKD) offers security, quantum computing threatens existing cryptographic standards.

## Proof of Concept, Future Prospects, and Research Directions

### Proof of Concept: Sub-THz OAM Transmission
The authors demonstrate the feasibility of sub-THz communication using Orbital Angular Momentum (OAM) multiplexing. 
*   **Method:** A wideband Butler matrix (a passive analog circuit) was used to generate and separate orthogonal OAM beams without digital signal processing.
*   **Results:** Achieved a wireless transmission rate of 1.58 Tbps in the 135–170 GHz range with mode isolation exceeding 15 dB. 
*   **Setup:** The experiment used Uniform Circular Arrays (UCAs) with a diameter of 6 cm over a distance of 1 meter; the authors note that parabolic reflectors can extend this distance to 20 meters.

### Future Research Directions and Visions
1.  **Energy/Spectral Efficiency:** Development of "green" hardware, self-organizing networks, and expanded RedCap standards for sustainable operation.
2.  **Leveraging 5G Numerologies:** Further exploration of flexible sub-carrier spacing (SCS) to provide QoS-based customization for diverse application needs.
3.  **Seamless RIS Integration:** Research into low-complexity channel estimation for RIS to overcome THz attenuation and enable adaptive beamforming.
4.  **Advanced Security Solutions:** Combining physical layer security via RIS with federated learning, allowing AI models to be trained on devices without sharing raw data, thereby preserving privacy.

## Conclusion
The paper maps the trajectory from 5G to 6G by analyzing the IMT-2030 vision. It argues that while extensions of current pillars provide scalability, the true leap to 6G requires the integration of AI and sensing (ISAC) and the utilization of higher spectrums like THz via innovative multiplexing techniques like OAM. Successful implementation depends on solving critical standardization and security challenges through global cooperation.
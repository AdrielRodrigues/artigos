---
index_terms:
  - Extended Reality (XR)
  - Metaverse
  - Smart Culture Applications
  - 5G Service-Based Architecture
  - Multi-Access Edge Computing (MEC)
  - Network Performance Feasibility
  - Cybersecurity in XR
  - Self-Sovereign Identity (SSI)
---

# 5G/6G Architecture Evolution for XR and Metaverse: Feasibility Study, Security, and Privacy Challenges for Smart Culture Applications

## I. Introduction
Extended Reality (XR)—comprising Virtual Reality (VR), Augmented Reality (AR), and Mixed Reality (MR)—is transforming education and cultural heritage by merging digital and physical worlds. To support these immersive experiences, network infrastructures must provide massive bandwidth, ultra-low latency, and high reliability. 5G introduces the Service-Based Architecture (SBA) and Multi-Access Edge Computing (MEC) to move computation closer to the user, yet concerns remain regarding its ability to scale for high-density XR deployments. Additionally, the transition to virtualized networks expands the attack surface, introducing risks related to MEC resources and sensitive biometric data collection.

### A. Related Work
The authors compare their work with existing literature on 5G/6G and XR. While previous studies focus on general 3GPP architectural evolution, holographic communication, or theoretical Metaverse frameworks, this paper specifically targets a "smart culture" domain. It distinguishes itself by providing an empirical feasibility study of performance metrics (bitrate, latency, power) and focusing on user-centric privacy mechanisms like Self-Sovereign Identity (SSI).

### B. Paper Contributions
The paper assesses whether current 5G SBA and MEC infrastructures can meet the real-world demands of immersive cultural experiences. The primary contributions include:
- An exploration of 5G's role in smart culture, emphasizing how SBA and MEC enable low-latency interactivity.
- A feasibility study comparing performance metrics (bitrate, latency, reliability, power) against XR requirements.
- An analysis of security and privacy risks, proposing mitigations such as Cyber Threat Intelligence (CTI) sharing and SSI wallets.

## II. XR and Metaverse Use Cases Related to Smart Culture
Smart culture applications require a distributed edge-based architecture rather than centralized cloud computing to maintain the "sense-decide-act" loops necessary for immersion.

### A. Smart Culture Applications
Key use cases include hybrid museum experiences using AR QR codes, holographic artist projections for remote concerts, and virtual reconstructions of ancient landmarks (e.g., the CHRONOS application for Ancient Greece). The "Internet of Cultural Things" (IoCT) integrates IoT sensors, cameras, and XR to provide personalized visitor paths and multisensory interactions, enhancing accessibility for diverse audiences.

### B. Metaverse
The Metaverse extends these concepts into persistent, interconnected digital platforms. In cultural heritage, this enables lifelike recreations of historical sites, unconditional global participation, and an autonomous economy where creators trade digital assets. The integration of IoT and Tactile Internet allows the Metaverse to react in real-time to physical gestures.

### C. XR and 5G Synergy
5G is essential for high-resolution content delivery and synchronized multi-user activities. Specific synergistic applications include the offline sharing of 3D objects, real-time XR streaming for education, and blended XR conferences that unify remote and in-person participants.

## III. Enabling Immersive Experiences through 5G and XR Support
The authors detail the 5G architectural components required to support high-bandwidth, low-latency XR workloads.

### A. 5G Service-Based Architecture (SBA)
The 5G SBA is a modular, cloud-native design utilizing Network Functions (NFs) that are stateless and communicate via HTTP/2. Key features include network slicing—which allows the creation of virtual networks tailored for eMBB or uRLLC—and an API-driven approach that exposes network capabilities to third-party XR developers.

### B. Multi-Access Edge Computing (MEC)
MEC integrates edge servers with the 5G core, placing the User Plane Function (UPF) and Local Area Data Networks (LADN) near the base station. This reduces end-to-end data distance, facilitating real-time analytics for AR overlays in museums and enabling content caching of high-demand XR assets at the edge.

### C. XR Support in 5GS
3GPP Release 17 and 18 (XRM Work Item) introduce enhancements for XR, including PDU Set-based QoS for precise media delivery, uplink-downlink coordination to reduce latency, and energy-saving strategies tailored for the intermittent nature of XR media streams.

### D. 5G-XR Network Functions
A proposed architecture integrates specific XR network functions: the 5G-XR Application Function (AF), the 5G-XR Application Server (AS), and the 5G-XR Client within the User Equipment (UE). These communicate through standardized interfaces (N6, N3) or sidelink PC5.

### E. 5G Network Analytics for XR
The Network Data Analytics Function (NWDAF) uses AI/ML to transition from reactive to proactive network management. NWDAF can predict network loads in high-traffic areas like museums, optimize resource allocation through intelligent slicing, and dynamically adjust QoS parameters to minimize packet loss and delay.

## IV. Feasibility Study of 5G Networks for XR and Metaverse Use Cases
The authors evaluate current 5G capabilities against the stringent requirements of advanced XR applications.

### A. Audio Bit Rate
While standard XR audio operates around 36 Mbps (which 5G handles well), future lossless high-fidelity audio is projected to require 1.6 Gbps. Current 5G cannot consistently support this rate, and user satisfaction drops significantly as data rates increase in dense environments.

### B. Video Bit Rate
Full-view ultra-high-resolution video (72K x 36K) would require 1 Tb/s raw or ~1 Gb/s compressed. Current 5G struggles with high-bandwidth video in dense areas; user satisfaction declines when rates exceed 30 Mbps. However, algorithms like AIPAT can push this to 40–50 Mbps with low delay.

### C. Latency
To avoid motion sickness, motion-to-photon latency must be under 20 ms. While 5G URLLC achieves sub-10 ms in optimal conditions, high user density increases buffering delays, pushing latency to 50–100 ms, which is unacceptable for immersive experiences.

### D. Reliability
Reliability requires ~99% of frames to be delivered within the target latency. In dense urban environments, reliability drops as more users are added; eMBB traffic can reduce XR capacity by up to 80% unless Inter-cell Interference Coordination (ICIC) or strict PDB adjustments are used.

### E. XR Capacity
Capacity varies significantly by spectrum: FR1 (sub-6GHz) supports only 2–8 UEs per cell at 30-45 Mbps, while FR2 (mmWave) can support 20–35 UEs. Scaling to the high bitrates required for HD VR streaming (200-2000 Mbps) remains unsustainable for current 5G.

### F. Power Consumption
XR devices target power consumption $<3\text{W}$. While 5G modems typically use ~0.5W, maintaining low latency in dense traffic increases draw. 5G-Advanced improves this through DRX (Discontinuous Reception) cycle optimization aligned with media stream periodicity (e.g., 60 FPS).

### G. Position and Timing Accuracy
5G-A achieves microsecond-level timing accuracy (1–10 $\mu$s) via OTA synchronization and PTP. Positioning using UL carrier phase measurements can achieve sub-centimeter accuracy and orientation precision below 1 degree at 28 GHz, making real-time device tracking feasible.

## V. Security and Privacy Concerns in 5G-Enabled Immersive Applications
The expanded attack surface of 5G/MEC architectures introduces specific vulnerabilities for XR users.

### A. Security Aspects
XR systems are vulnerable to standard ICT threats (malware, phishing) and network-specific risks:
1. **Virtualization:** Compromised VM hosts can affect the availability of virtualized services. Trusted Platform Modules (TPM) are proposed to ensure integrity through chains of trust.
2. **API Security:** The reliance on APIs requires robust authentication (token, cookie, or key-based), input sanitization to prevent injection, and the use of mTLS or OAuth 2.0 for encrypted communication.
3. **5G Private Network Security:** Protocol-specific attacks are highlighted: RRC attacks can lead to subscriber ID tampering or DoS; NAS vulnerabilities allow location tracking; GTP protocol flaws enable MitM attacks on real-time environment data; and Diameter protocol exploits can hijack user sessions.

### B. Privacy Aspects
XR sensors collect immense amounts of sensitive biometric and behavioral data, leading to several risks:
- **Anonymity:** The risk of disclosing personal data to third parties in interactive exhibits necessitates GDPR compliance and advanced encryption.
- **Pervasive Collection:** Tracking facial expressions, brain-wave patterns, and subconscious behavior allows for the creation of invasive privacy models without consent.
- **Leakage during Transfer/Storage:** Data is vulnerable to MitM eavesdropping during wireless transfer and "linkage" or "differential" attacks when stored in cloud/edge repositories.

## VI. Challenges and Future Research Directions

### A. XR Capacity Limitations
Future research must focus on better Radio Resource Management (RRM) and interference mitigation. Proposed solutions include PDU-set scheduling, Radio Environment Maps (REMs), and Superposition Coding (SPC) in massive MIMO systems to improve spectral efficiency for URLLC/eMBB coexistence.

### B. Power Consumption
To extend device battery life, the focus is shifting toward embedded AI and energy-aware MEC task offloading, allowing computationally heavy rendering tasks to be moved from the headset to the edge.

### C. XR for Digital Twins
Digital Twin Networks (DTNs) provide real-time virtual replicas of physical networks for predictive maintenance and optimization. Challenges include ownership disputes over digital representations and the need for ultra-low latency synchronization.

### D. Security and Privacy in the Metaverse
To replace vulnerable centralized identity models, the authors advocate for decentralized Self-Sovereign Identity (SSI) and credential wallets (e.g., the EU Digital Identity Wallet). These allow users to share only necessary attributes without disclosing full identities, reducing data breach risks.

## VII. Conclusion
While 5G provides a foundation via SBA and MEC, it cannot currently support large-scale, high-density immersive experiences due to limitations in capacity, power efficiency, and latency under load. The evolution toward 6G is necessary to realize a fully immersive Metaverse. Future research should prioritize AI-driven predictive analytics, decentralized identity frameworks (SSI), and optimized resource allocation for ultra-dense environments.
---
index_terms:
  - 6G communication architecture
  - AI-driven networking
  - Ultra-Reliable Low-Latency Communication
  - Internet of Robotic Things
  - Terahertz communications
  - Network slicing
  - Edge computing
  - Quantum-safe cryptography
---

# Review on 6G communication and its architecture, technologies included, challenges, security challenges and requirements, applications, with respect to AI domain

## 1. Introduction
6G wireless technology is positioned as the successor to 5G, intending to provide unprecedented data rates and connectivity. The core of this evolution is the deep integration of Artificial Intelligence (AI) into the network architecture to drive innovation in efficiency and user experience. This review explores the intersection of AI and 6G across various environments and application domains.

## 2. Architecture

### 2.1 6G Communication Architecture
The proposed 6G architecture is designed for pervasive connectivity across four primary dimensions: space, air, land, and sea/undersea.

#### 2.1.1 6G Architecture in Space
Space-based 6G focuses on global coverage through the deployment of satellite constellations (LEO, MEO, and GEO) to balance latency and capacity. Key technical requirements include advanced inter-satellite communication for direct data exchange, phased array antennas for adaptive beamforming, and cross-layer optimization. Due to power constraints in space, energy efficiency is a primary design driver, alongside robust encryption and seamless integration with terrestrial networks.

#### 2.1.2 6G Architecture in Air
The airborne architecture targets ultra-fast in-flight connectivity for passengers and enhanced aircraft-to-aircraft (A2A) communication to prevent collisions. It enables real-time remote pilot assistance, predictive maintenance via connected sensors, and improved surveillance/navigation. High bandwidth and low latency are required for precise air traffic management and emergency search-and-rescue operations.

#### 2.1.3 6G Architecture in Land
Terrestrial 6G will utilize higher frequency bands (millimetre-wave and Terahertz) to increase capacity. The architecture relies on Massive MIMO, advanced beamforming, and ultra-dense network deployments of small cells in urban areas. AI/ML are integrated for dynamic resource allocation and interference management. There is a strong emphasis on "green" sustainable design to reduce the carbon footprint of high-density networks.

#### 2.1.4 6G Architecture in Sea and Undersea
Because radio frequency (RF) signals attenuate rapidly in water, undersea architecture employs a hybrid approach using acoustic communication for long distances (low rate) and optical communication for short distances (high rate). Integration with satellites is necessary for remote oceanic connectivity. The system supports underwater IoT sensor networks for environmental monitoring and resource management, requiring specialized energy harvesting techniques and high-reliability links.

## 3. 6G Technologies in AI
6G aims to be "AI-native," incorporating various AI types including tiny AI, federated AI, collective AI, and semantic-oriented AI. Key enabling technologies include:
*   **Spectrum & Signal Management:** Terahertz (THz) communications for multi-terabit rates, Massive MIMO for spectral efficiency, and holographic beamforming for highly directional signals.
*   **Network Orchestration:** AI-driven beamforming and network orchestration to adapt the system dynamically to changing demands.
*   **Computation & Security:** Edge AI to reduce latency by processing data near the source; Quantum Communication for next-level security via quantum-enhanced encryption.
*   **Connectivity:** Integrated satellite networks and ultra-dense heterogeneous networks providing seamless global coverage and massive IoT integration.

## 4. Challenges

### 4.1 General Challenges
Integrating AI into 6G introduces several hurdles:
*   **Energy Efficiency:** Advanced technologies increase power consumption, requiring AI-based power management.
*   **Interoperability & Ethics:** The need for standardized protocols across diverse AI modules and the mitigation of algorithmic bias and privacy concerns.
*   **Security:** Protecting AI models from adversarial attacks and managing a significantly expanded attack surface.

### 4.2 Security Challenges in 6G
Specific security threats include:
*   **Infrastructure Vulnerabilities:** Risks associated with network slicing isolation, IoT device entry points, and physical attacks on critical hardware.
*   **Cyber Threats:** Sophisticated DDoS attacks, ransomware, zero-day exploits, and AI-driven manipulation of network decisions.
*   **Operational Risks:** Supply chain compromises (malicious components) and the challenge of maintaining consistent regulatory policies across different jurisdictions.

### 4.3 Security Requirements for 6G
To ensure robustness, 6G must implement:
*   **Advanced Protection:** Strong encryption, quantum-safe cryptography, and privacy-preserving techniques such as differential privacy.
*   **Access Control:** Reliable authentication/authorization and secure key management.
*   **Resilience:** Intrusion detection systems (IDS), network segmentation to isolate slices, and self-healing mechanisms for redundancy.
*   **Lifecycle Security:** Secure software updates and supply chain verification.

### 4.4 Application Layer
6G is expected to enable several high-demand AI applications:

#### 4.4.1 Internet of Vehicles (IoV)
IoV relies on Ultra-Reliable Low-Latency Communication (URLLC) for safety-critical Vehicle-to-Vehicle (V2V) and Vehicle-to-Infrastructure (V2I) interactions. It utilizes network slicing to prioritize emergency messages over infotainment and edge computing for real-time collision avoidance.

#### 4.4.2 Internet of Medical Things (IoMT)
IoMT leverages 6G for remote surgeries, high-definition telemedicine, and continuous monitoring via implantable sensors. Edge servers provide the near-real-time processing needed for critical diagnostics, while AI models enable personalized treatment recommendations.

#### 4.4.3 Internet of Drones (IoD)
6G supports drone swarms through massive device connectivity and URLLC for precise control. It allows high-resolution real-time data transmission for aerial mapping and disaster management, using edge computing to perform local obstacle avoidance.

#### 4.4.4 Internet of Robotic Things (IoRT)
The IoRT focuses on collaborative robotics and teleoperation. Low latency is critical for the "tactile internet" (haptic feedback), while AI-driven systems allow robots to learn from their environment and coordinate complex tasks autonomously.

#### 4.4.5 Industry Internet of Things (IIoT)
Industrial environments require deterministic communication for robotic assembly lines and predictive maintenance. Edge computing reduces response times for safety-critical operations, while high device density allows for comprehensive factory monitoring.

#### 4.4.6 Holographic Communication
This involves transmitting 3D images requiring terabit-per-second speeds and ultra-low latency to avoid perceptual lag. It requires specialized holographic capture/display devices and significant edge computing resources for real-time rendering.

#### 4.4.7 Blockchain
Blockchain is integrated to provide decentralized identity management, immutable data provenance, and secure device authentication. Smart contracts are used to automate network resource orchestration and facilitate transparent data monetization.

#### 4.4.8 Extended Reality (XR)
XR (VR/AR/MR) requires extreme bandwidth for high-fidelity graphics and ultra-low latency to prevent motion sickness. 6G enables spatial computing—real-time mapping of physical spaces integrated with digital overlays—and remote telepresence.

## 5. Middleware Layer: Scheduling and Resource Management

### 5.1 Energy and Performance Optimisation
Middleware uses AI to balance Quality of Service (QoS) with energy sustainability via:
*   **Dynamic Power Management:** Adjusting power based on traffic load and using proactive sleep modes.
*   **Intelligent Allocation:** Context-aware resource distribution and cognitive radio technologies to minimize interference.
*   **Efficiency Tactics:** Data offloading to lower-energy networks (e.g., Wi-Fi) and task consolidation on efficient nodes.

### 5.2 Security in Middleware
Middleware implements a Zero Trust Architecture, assuming no device is trusted by default. It employs end-to-end encryption, quantum-safe cryptography, and AI-driven anomaly detection to identify threats in real time.

### 5.3 Context Aware Data Caching
To reduce latency, middleware uses predictive analysis to preload data based on user location, behavior, and application requirements. This reduces the load on the core network by storing content at Multi-access Edge Computing (MEC) nodes.

### 5.4 Data Availability
6G ensures high availability through a combination of hybrid communication technologies (THz, optical), self-healing networks, and global coverage extensions to remote areas.
*   **IoT Infrastructure:** Designed for massive connectivity and multi-modal access (cellular/satellite).
*   **Edge Infrastructure:** Focuses on decentralized processing to enable real-time decision-making.
*   **Cloud Infrastructure:** Provides centralized high-power computing for big data analytics and disaster recovery.

### 5.5 6G Network Layer
The network layer incorporates several AI-enhanced functions:
*   **Signal & Traffic Management:** ML-based channel estimation, modulation recognition, and traffic classification/prediction.
*   **Routing & Resources:** Intelligent routing to avoid congestion and Radio Resource Management (RRM) for dynamic spectrum sharing.
*   **Maintenance & Security:** AI-driven fault management (self-healing), predictive mobility handover, and detection of intrusions or botnets.
*   **Energy Optimization:** Using ML to predict low-activity periods and dynamically adjust power levels.

## 6. Conclusion
The synergy between AI and 6G architecture is transformative, enabling advanced applications like holographic communication and autonomous robotic systems. However, the realization of this potential depends on overcoming significant challenges in energy efficiency, interoperability, and security through a coordinated effort among policymakers and researchers.
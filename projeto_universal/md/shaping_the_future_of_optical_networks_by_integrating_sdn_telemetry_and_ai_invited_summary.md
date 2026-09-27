---
index_terms:
  - software-defined networking
  - optical network telemetry
  - intent-based networking
  - IP over WDM
  - machine learning for networks
  - OpenOSDK
  - multi-layer network control
---

# Shaping the future of optical networks by integrating SDN, telemetry, and AI

## 1. Introduction
Modern optical networks are evolving toward intelligent, autonomous infrastructures to handle traffic growth from 5G, IoT, and cloud services. This transformation is driven by three pillars: Software-Defined Networking (SDN) for programmability via NETCONF/YANG; Telemetry (gRPC/gNMI) for real-time performance insights; and Artificial Intelligence (AI) for zero-touch management. Additionally, the convergence of packet and optical layers through IPoWDM architectures and coherent optics reduces latency and complexity. Despite these advances, challenges remain regarding multi-vendor interoperability, the energy intensity of AI, and a lack of real-world training data for machine learning models.

## 2. SDN Empowered by Open Modeling
SDN decouples the control and data planes, utilizing a central controller to manage topology and configuration. A current trend is delegating Routing and Spectrum Assignment (RSA) to digital twins to improve Quality of Transmission (QoT) assessment by evaluating physical impairments before lightpath activation.

### A. YANG/NETCONF
The industry relies on the NETCONF protocol and YANG data models to abstract optical node capabilities. Key initiatives include:
*   **Open ROADM:** Focuses on interoperability and disaggregated architectures (separating transponders, ROADMs, and amplifiers) to prevent vendor lock-in.
*   **OpenConfig:** Provides vendor-neutral YANG models and supports gNMI for streaming telemetry.
Despite these efforts, a gap exists where isolated data models and proprietary SDN controllers are still required to access advanced device functionalities.

### B. OpenSDK
To overcome the limitations of standard southbound interfaces, the OpenOSDK (Open Optical Software Development Kit) framework is proposed. It enables third-party microservices (containers/pods) to run directly on network elements via a standardized SDK (e.g., SONiC OS). This allows AI-integrated modules to perform local re-optimization and data collection at the device level, regardless of whether the SDN controller uses standard or proprietary interfaces.

### C. SDN Controllers
Three primary open-source frameworks are highlighted:
1.  **OpenDaylight (TransportPCE):** Known for stability and OpenROADM compatibility.
2.  **ONOS:** Designed for scalability/reliability, supporting an intent-based approach to control packet and optical layers.
3.  **TeraFlowSDN:** A cloud-native, microservices-oriented controller now extending into optical device management via OpenConfig.
For multi-layer environments, a hierarchical architecture is used where a parent controller coordinates specialized child controllers for the IP and optical domains.

## 3. Telemetry Services
Telemetry provides the real-time data necessary for AI training and proactive network management. It leverages gNMI and OpenConfig to create "data lakes" of time-series samples from amplifiers, ROADMs, and pluggables.

### A. Out-of-Band Telemetry (ONT)
ONT transmits monitoring data (SNR, BER, power levels) over separate channels, ensuring no interference with user traffic. It integrates legacy tools like Optical Channel Monitors (OCM) and Optical Time Domain Reflectometers (OTDR). Modern ONT uses Kafka for distributed publish-subscribe telemetry sharing and can be implemented horizontally (peer-to-peer between device agents) to enable local decision-making and reduce the load on the central controller.

### B. In-Band Telemetry (INT)
INT embeds telemetry metadata directly into user traffic headers, requiring programmable data planes (using P4, eBPF, or DPDK). This allows for near-instant detection of "soft failures" within the packet-optical node pipeline. INT facilitates multi-layer optimization by encoding diverse layer data in a single packet header, which is particularly useful for edge computing environments.

### C. Telemetry Trends and Perspectives
The field is moving toward a unified programmable model that replaces rigid NETCONF/YANG systems. The authors envision an integration of Generative AI (e.g., LLM-based bots) that allows operators to issue high-level semantic commands which the system then translates into specific telemetry streams and control operations.

## 4. Control of Packet/Optical Networks
The rise of $\ge$800G coherent pluggable transceivers has accelerated IP over WDM (IPoWDM) adoption, facilitated by the C-CMIS standard for router-to-transceiver communication. IPoWDM reduces CAPEX and power by removing standalone transponders but complicates management.

The **MANTRA** (Metaverse-Ready Architectures for Open Transport) initiative proposes two hierarchical SDN architectures:
*   **Single Architecture:** The IP controller fully manages IPoWDM nodes and pluggables, while the optical controller only manages the Optical Line System (OLS).
*   **Dual Architecture:** Similar to the single approach, but the optical controller is granted read access to IPoWDM nodes to improve decision-making.

## 5. Role of IBN in Optical Networks
Intent-Based Networking (IBN) abstracts complex configurations into high-level business goals expressed in natural language. The IBN system translates these intents into actionable instructions for the SDN controller, which then programs the hardware. This creates a closed-loop system where telemetry provides continuous assurance; if performance degrades (e.g., fiber degradation), the IBN layer automatically triggers rerouting or parameter adjustments to maintain the service level agreement.

## 6. AI/ML in Optical Networks
AI and Machine Learning (ML) are used to model complex phenomena where analytical expressions are insufficient.

### Key ML Applications:
*   **QoT Estimation:** Complementing Gaussian Noise models to refine transmission margins and account for aging effects.
*   **Device Control:** Optimizing the gain spectra and pump settings of EDFAs, Raman, and TDFA amplifiers.
*   **Failure Management:** Predicting and localizing soft failures. To handle imbalanced real-world data, authors suggest data augmentation. ML is also used for alarm clustering to suppress redundant alarms.
*   **Resource Allocation:** Utilizing Reinforcement Learning (RL) and Deep RL for routing and spectrum assignment.
*   **IBN Integration:** Using Natural Language Processing (NLP) for intent classification and supervised learning for network assurance.
*   **Environmental Sensing:** Leveraging deployed fibers as distributed sensors for seismic activity or structural health monitoring.

### Complexity and Sustainability:
The authors note that AI/ML significantly increases power consumption. Analysis shows that standard optimization (e.g., Bayesian) often leaves many neurons inactive, adding unnecessary complexity. To ensure sustainability, they propose **Pruning** (removing weights/biases) and **Knowledge Distillation** (transferring knowledge from a complex "teacher" model to a leaner "student" model), which can reduce complexity by approximately 90% without significant accuracy loss.

## 7. Conclusion
The integration of SDN, telemetry, and AI is essential for building autonomous optical infrastructures. While progress has been made in programmability (OpenOSDK) and multi-layer control (MANTRA), the industry must still address the lack of standardization across vendors and the scarcity of real-world data. The future lies in open, interoperable ecosystems that combine explainable AI with zero-touch management to ensure scalability and sustainability.
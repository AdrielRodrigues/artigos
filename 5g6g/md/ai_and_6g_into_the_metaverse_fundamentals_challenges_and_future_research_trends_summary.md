---
index_terms:
  - Metaverse
  - 6G networks
  - Artificial Intelligence
  - Edge AI
  - Spatial Computing
  - XR (AR/VR/MR)
  - Holographic Telepresence
  - Sustainable Metaverse
---

# AI and 6G Into the Metaverse: Fundamentals, Challenges and Future Research Trends

## I. Introduction
The Metaverse is conceptualized as an evolution of the Internet, consisting of a pool of Extended Reality (XR) spaces where humans and digital avatars interact immersively. It integrates B5G/6G, cloud/edge computing, social media, AR/VR, and AI to create a seamless virtual existence. While 5G has enabled real-time communication and 360° content, it falls short of the requirements for high-fidelity haptic feedback (requiring ~0.1ms latency) and holographic telepresence (requiring Tbps data rates). Consequently, researchers are exploring Terahertz (THz) bands in 6G to provide the necessary bandwidth and ultra-low latency.

### A. Related Surveys
Current literature covers specific niches: AI and blockchain integration, security/privacy, edge intelligence, or wireless architectures. This paper differentiates itself by examining the comprehensive nexus of AI and 6G specifically for realizing a sustainable and ubiquitous Metaverse experience.

### B. Methodology of this Survey
The authors conducted an extensive literature review from January 1995 to December 2022 using databases like IEEE Xplore, Scopus, Science Direct, and Google Scholar. Screening was based on the relevance of abstracts, introductions, and conclusions relative to keywords such as "6G-powered Edge AI," "XR for Metaverse," and "uRLLC."

### C. Contribution and Structure of this Survey
The paper contributes:
1. A technical overview of VR, MR, AR, and spatial computing.
2. An analysis of AI's role in the layered architecture of the Metaverse to extract 6G communication requirements.
3. An evaluation of B5G/6G services required for immersive experiences and holographic telepresence.
4. An exploration of the synergy between AI and 6G (AI for networks and networks for AI) and a discussion on sustainability, use cases, and future research gaps.

## II. AI and 6G for Metaverse: Background and Technical Aspects
The Metaverse is defined as a computer-generated, immersive 3D environment that extends beyond the physical world. It differs from simple cyberspace by its depth of immersion and persistence.

### A. Definition of Metaverse Based on AI and 6G
From a technical standpoint, the Metaverse is an advanced digital realm leveraging AI for personalization and 6G for high-speed, low-latency connectivity to create realistic virtual environments for socializing, working, and trading.

### B. The Background of AI for Metaverse
The transition from Web1 (static pages) and Web2 (controlled social platforms) leads toward a decentralized environment where NFTs represent digital ownership. AI is ubiquitous across the Metaverse layers, particularly through transformers and deep learning models that enable natural language interaction and realistic 3D rendering.

### C. Spatial Computing
Spatial computing integrates AR, VR, and MR to digitize human and object activities in 3D space.
1. **Virtual Reality (VR):** Fully replaces the real world with synthetic vistas, requiring high synchronization among users to avoid latency-induced discomfort.
2. **Augmented Reality (AR):** Overlays digital elements onto the physical world; current challenges include precise mapping and tracking of virtual objects in complex urban environments.
3. **Mixed Reality (MR):** A hybrid where physical and digital objects coexist and interact in real time, requiring advanced computer vision to perceive environmental boundaries and lighting.

### D. Background of B5G/6G
Wireless generations have evolved from voice clarity (1G) to multimedia (4G) and high-capacity connectivity (5G). 6G is envisioned as "connectivity with intelligence," shifting from a data-centric to a human-centric approach.
1. **5G Evolution:** While 5G introduces mmWave for higher speeds, it remains insufficient for the multi-sensory requirements of the Metaverse.
2. **6G and Internet of Everything (IoE):** 6G aims for Tbps data rates using THz waves (0.1–10 THz) and integrated space-air-ground-sea networks (SAGSIN).

### E. AR/VR/MR Deployments on 5G/6G Networks
Scaling XR requires ultra-low latency and high bandwidth. The authors note that private 6G networks may be necessary for mission-critical industrial tasks. Blockchain is proposed to secure digital assets and copyright in these environments, while MEC (Multi-access Edge Computing) is essential to handle the heavy rendering loads that would otherwise drain mobile device batteries.

## III. Role of AI in Metaverse
AI provides the intelligence needed to make the Metaverse believable and scalable.

### A. Layered Architecture of AI in Metaverse
The authors map AI onto a seven-layer architecture:
*   **AIInfra:** Hardware/software (GPUs, MEMS) enabling AI execution.
*   **AIInt:** Intelligent interfaces for accessibility (e.g., BCI for disabled users).
*   **AICont:** AI-driven smart contracts to ensure democratization and detect anomalies in blockchain transactions.
*   **AIVWorld:** Autonomous generation of realistic 3D environments.
*   **AIART-E:** Generative AI (GPT, DALL-E) for economic enrichment through NFT creation.
*   **SocialAI:** Using Explainable AI to reduce bias and detect hate speech in social interactions.
*   **PersonalizedAI:** Hyper-personalization based on real-time emotional and mental analytics.

### B. Learning Paradigms for Metaverse
The field is moving from supervised learning (which is task-dependent) toward self-supervised and reinforcement learning to create autonomous, life-like digital agents that can interact with humans without constant human labeling.

### C. Computer Vision for Metaverse
Computer vision enables the creation of lifelike avatars and holographic images using semantic segmentation and 3D pose estimation. The focus is on creating "digital humans" and optimizing 3D spaces through cognitive theories to improve learning speeds in virtual classrooms.

### D. Object Generation in Metaverse
To avoid the high cost of manual 3D modeling, Generative AI (GANs, Diffusion models) and Neural Radiance Fields (Instant NERF) are used to transform 2D images or text descriptions into high-fidelity 3D assets automatically.

### E. Edge AI for Metaverse
Edge AI moves computation closer to the user to satisfy uRLLC requirements. Techniques like CNN-LSTM combinations are used for channel prediction and traffic forecasting to maintain stable connections.

### F. 6G: A Requirement for AI-Based Metaverse
AI models (especially LLMs) require massive bandwidth and stability. The authors provide data showing that layers like `PersonalizedAI` require transmission bit rates of ~238 Gbps, which exceeds 5G capabilities, making 6G an absolute necessity for full realization.

## IV. Role of B5G/6G in Metaverse
B5G/6G is the "pipe" that enables the immersive data flow required by AI.

### A. Is B5G/6G Need of an Hour?
Yes, because 5G cannot support: (1) the projected proliferation of IoT devices; (2) multi-sensory communications; (3) ultra-massive connectivity in dynamic environments; and (4) the resilient edge AI needed for decentralized intelligence.

### B. What B5G/6G Brings to Metaverse
1. **5G Services:** eMBB provides high throughput for 4K video, while uRLLC and mMTC handle low latency and device density. However, these are mostly limited to rudimentary XR.
2. **6G Services:** Introduces "connectivity with intelligence" via:
    *   **uMBB:** Higher data rates than eMBB.
    *   **uMTC:** Ultra-massive connectivity for dense sensor networks.
    *   **uHPC:** Ultra-high precision and reliability for mission-critical tasks.
    *   **e3DC:** Extended 3D coverage via non-terrestrial satellite networks (SAGSIN).

### C. Immersive Experiences over Wireless
Immersive fidelity requires a combination of mmWave, MEC, and THz communications. The authors highlight that using Field of View (FOV) prediction at the edge can reduce bandwidth requirements by up to 80%. THz bands are essential for indoor high-fidelity VR but face challenges with water-molecule absorption.

### D. Holographic Telepresence in Metaverse
Holographic Telepresence (HT) requires Tbps rates and $<$1ms latency. While a standard hologram may need 0.5–2 Gb/s, full-sized human holograms require up to 4.32 Tb/s. URLLC is the primary enabler for these high-stakes applications like remote surgery.

## V. Nexus of AI and 6G for Metaverse
The synergy creates a feedback loop: 6G enables pervasive AI, and AI optimizes 6G networks.

### A. 6G-Driven Pervasive AI for Metaverse
6G provides the infrastructure (SAGSIN) for ubiquitous intelligence. It allows millions of users to share immersive spaces by reducing inference latency through distributed AI across the end-edge-cloud continuum.

### B. AI-Led Autonomous 6G Networks for Metaverse
1. **Self-X Networks:** To avoid manual configuration, 6G must be self-healing, self-optimizing, and self-organizing (Zero-Touch Management).
2. **AI for Networks:** Deep Reinforcement Learning (DRL) and Federated Learning (FL) are used to manage resources dynamically without compromising user privacy.

### C. AI and 6G for Tactile Internet in Metaverse
The Tactile Internet requires a round-trip delay of $<$1ms. While 5G uses SDN/NFV to reduce latency, the physical speed of light limits transmission distance to ~150km. AI-based predictive models are proposed to "mask" this latency by predicting haptic feedback before it arrives.

## VI. Metaverse Usecases Concerning Sustainability and Privacy
The Metaverse is not just a technological tool but has significant socio-environmental implications.

### A. Virtual Resources in Metaverse
Replacing physical goods (e.g., denim) with digital assets for avatars can significantly reduce water consumption and CO2 emissions.

### B. Travelling through Metaverse
Virtual meetings and concerts can replace discretionary air travel, reducing the carbon footprint of the conference and exhibition industry.

### C. Digital Twins and Metaverse
Digital twins enable sustainable industrial "meta-worlds" by simulating assembly lines and urban environments to optimize energy use and reduce waste before physical implementation.

### D. Social Sustainability with Metaverse
The authors argue for democratization (equal access) over mere decentralization. They highlight the risk of "unconscious bias" in AI models that could lead to digital discrimination based on race or gender.

### E. Sustainable Communication and Connectivity
6G is designed to be more energy-efficient than previous generations, focusing on human development rather than just device performance.

### F. Metaverse Security and Privacy
The collection of 3D biometric data (eye movement, facial features) increases risk. Specific threats identified include:
*   **Ethical Concerns:** Ownership rights and cyberbullying.
*   **Virtual Theft:** Theft of rare NFTs or virtual real estate.
*   **Social Engineering:** Using persuasive avatars to trick users into revealing data.
*   **Malware/Data Breach:** High vulnerability due to the lack of centralized oversight in decentralized systems.

## VII. Metaverse Applications and Usecases in General
The Metaverse interacts with the physical world by mirroring it or extending it.

### A. Use Cases
1. **Marketing:** In-game branded clothing and billboards.
2. **Blockchain:** dApps, NFTs, and peer-to-peer virtual economies.
3. **Virtual Tourism:** Immersive 360° exploration of destinations.
4. **Real-Time Communication:** P2P browser-based communication without intermediary servers.
5. **Office/Learning Spaces:** Hybrid VR workspaces (e.g., Virtuworx) and medical simulations for surgeons.
6. **Healthcare Simulations:** AI-driven diagnostic training in safe, virtual environments.
7. **Smart Cities:** Using 6G IoT sensors to optimize urban traffic and energy flow via a digital twin.

### B. Penetrating Psychological Barriers
Metaverse simulations can be used to make climate change "felt" by the general public, overcoming short-term perceptions of weather to spur pro-environmental action.

### C. Benefits of Metaverse
Key benefits include democratized healthcare access, new "play-to-earn" economic models in gaming, and reduced ecological footprints via virtual offices.

### D. Metaverse Market State
Major players include Meta (Oculus), Epic Games (Unreal Engine), Microsoft (Mesh), and Decentraland. The market is shifting toward a creator economy based on DeFi and NFTs.

## VIII. Projects
The paper lists several ongoing projects:
*   **Decentraland:** A DAO-governed virtual world for real estate and NFT sales.
*   **Oculus:** Meta's hardware/software ecosystem.
*   **Enjin:** An SDK provider for Metaverse NFTs.
*   **Silks:** A blockchain-based horse racing simulation.
*   **XR Initiative (Univ. of Miami):** Focusing on nursing and autism training.
*   **Specialized Projects:** VReality (Real Estate), MetaMed (Telehealth), MetaDrive (Autonomous driving simulation via RL), and Edverse (Blockchain education).

## IX. Lessons Learned
1. **Art/Immersion:** LLMs and Generative AI are essential for unique, scalable visual experiences.
2. **Circular Economy:** Digitalizing events and products can move society toward a waste-free circular economy.
3. **Sustainability:** Regulation is needed to ensure the Metaverse doesn't increase energy consumption via data centers.
4. **Layered Security:** A combination of Federated Learning and Blockchain is required for identity and asset protection.
5. **Wireless Interactivity:** 6G must shift from "connectivity" to "interactivity," using THz bands for zero-error short-range communication.
6. **Service Requirements:** Network slicing in 6G will be critical to handle conflicting requirements (e.g., low latency for haptics vs. high bandwidth for video).
7. **Infrastructure:** Decentralized intelligence and MEC are the only ways to scale for millions of concurrent users.

## X. Challenges and Future Research Directions
### A. Role of AI in Metaverse
Challenges include integrating with Industry 5.0, achieving true democratization (bias-free AI), and protecting intellectual property against easy digital counterfeiting.

### B. Role of B5G/6G in Metaverse
Research is needed for "Zero-Touch Management" to handle massive complexity without human intervention and for optimizing SAGSIN architectures to ensure reliability during satellite handovers.

### C. Integrated Role of AI and 6G
Future work should focus on moving AI from the cloud to the device (Edge AI), developing self-supervision techniques to solve the lack of labeled data, and creating energy-efficient AI models that don't drain device batteries.

### D. Towards Sustainable Metaverse
The industry must shift from "Proof-of-Work" to "Proof-of-Stake" for blockchain transactions to reduce energy use. Additionally, efforts are needed to bridge the "digital divide," as current VR hardware is concentrated in North America and Western Europe.

## XI. Conclusion
The paper concludes that while 5G provides a foundation, the full immersive potential of the Metaverse—including holographic telepresence and tactile internet—requires the synergy of AI and 6G. The integration of pervasive intelligence and THz connectivity will enable a sustainable, ubiquitous virtual world.
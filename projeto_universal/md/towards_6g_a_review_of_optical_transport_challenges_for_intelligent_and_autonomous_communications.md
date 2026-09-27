---
title: "Towards 6G: A Review of Optical Transport Challenges for Intelligent and Autonomous Communications"
tema_principal: projeto_universal
temas_relacionados: []
ano: 2025
autores: []
veiculo: null
pdf: ../pdf/towards_6g_a_review_of_optical_transport_challenges_for_intelligent_and_autonomous_communications.pdf
---

![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

# Review

# Towards 6G: A Review of Optical Transport Challenges for Intelligent and Autonomous Communications

Evelio Astaiza Hoyos, Héctor Fabio Bermúdez-Orozco and Jorge Alejandro Aldana-Gutierrez

# Topic

[Computational Complex Networks](https://www.mdpi.com/topics/Comput_Complex_Netw)

Edited by

Dr. Alexandre G. Evsukoff and Dr. Yilun Shang

![](_page_0_Picture_10.jpeg)

![](_page_0_Picture_11.jpeg)

![](_page_1_Picture_0.jpeg)

![](_page_1_Picture_1.jpeg)

*Review*

# **Towards 6G: A Review of Optical Transport Challenges for Intelligent and Autonomous Communications**

**Evelio Astaiza Hoyos [,](https://orcid.org/0000-0003-2706-0962) Héctor Fabio Bermúdez-Orozco [\\*](https://orcid.org/0000-0002-8101-3764) and Jorge Alejandro Aldana-Gutierrez**

Electronic Engineering Programme, Faculty of Engineering, University of Quindío, Armenia 630004, Quindío, Colombia; eastaiza@uniquindio.edu.co (E.A.H.); jaldana@uniquindio.edu.co (J.A.A.-G.)

**\*** Correspondence: hfbermudez@uniquindio.edu.co; Tel.: +57-3206671107

#### **Abstract**

The advent of sixth-generation (6G) communications envisions a paradigm of ubiquitous intelligence and seamless physical–digital fusion, demanding unprecedented performance from the optical transport infrastructure. Achieving terabit-per-second capacities, microsecond latency, and nanosecond synchronisation precision requires a convergent, flexible, open, and AI-native x-Haul architecture that integrates communication with distributed edge computing. This study conducts a systematic literature review of recent advances, challenges, and enabling optical technologies for intelligent and autonomous 6G networks. Using the PRISMA methodology, it analyses sources from IEEE, ACM, and major international conferences, complemented by standards from ITU-T, 3GPP, and O-RAN. The review examines key optical domains including Coherent PON (CPON), Spatial Division Multiplexing (SDM), Hollow-Core Fibre (HCF), Free-Space Optics (FSO), Photonic Integrated Circuits (PICs), and reconfigurable optical switching, together with intelligent management driven by SDN, NFV, and Artificial Intelligence/Machine Learning (AI/ML). The findings reveal that achieving 6G transport targets will require synergistic integration of multiple optical technologies, AI-based orchestration, and nanosecond-level synchronisation through Precision Time Protocol (PTP) over fibre. However, challenges persist regarding scalability, cost, energy efficiency, and global standardisation. Overcoming these barriers will demand strategic R&D investment, open and programmable architectures, early AI-native integration, and sustainability-oriented network design to make optical fibre a key enabler of the intelligent and autonomous 6G ecosystem.

**Keywords:** 6G; AI-native; Artificial Intelligence/Machine Learning (AI/ML); Coherent Passive Optical Network (CPON); Spatial Division Multiplexing (SDM); Hollow-Core Fibres (HCFs)

![](_page_1_Picture_10.jpeg)

Academic Editors: Alexandre G. Evsukoff and Yilun Shang

Received: 5 November 2025 Revised: 23 November 2025 Accepted: 2 December 2025 Published: 5 December 2025

**Citation:** Astaiza Hoyos, E.; Bermúdez-Orozco, H.F.; Aldana-Gutierrez, J.A. Towards 6G: A Review of Optical Transport Challenges for Intelligent and Autonomous Communications. *Computation* **2025**, *13*, 286. [https://doi.org/10.3390/](https://doi.org/10.3390/computation13120286) [computation13120286](https://doi.org/10.3390/computation13120286)

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license [\(https://creativecommons.org/](https://creativecommons.org/licenses/by/4.0/) [licenses/by/4.0/\)](https://creativecommons.org/licenses/by/4.0/).

# **1. Introduction**

The history of mobile communications is a narrative of constant evolution, marked by generational leaps that have redefined connectivity and enabled new capabilities. From the introduction of analogue mobile voice (1G) to the era of broadband mobile Internet with 4G and 5G, each generation has responded to an exponential demand for data and increasingly sophisticated services. The fifth generation (5G), whose specifications and early deployments laid the foundations for a more connected society, introduced three pillars of use cases: Enhanced Mobile Broadband (eMBB), Ultra-Reliable Low-Latency Communications (URLLC), and Massive Machine-Type Communications (mMTC). Tech*Computation* **2025**, *13*, 286 2 of 29

nologies such as millimetre waves (mmWave), Massive MIMO (mMIMO), and Network Function Virtualisation (NFV) were fundamental to achieving these objectives.

However, the vision for the sixth generation (6G), also known as IMT-2030 by the International Telecommunication Union (ITU), transcends the mere quantitative enhancement of 5G parameters. 6G aspires to catalyse a profound fusion between the physical, digital, and human worlds, creating an intelligent and ubiquitous connective fabric [\[1\]](#page-27-0). This vision will enable transformative applications that are only beginning to emerge today: truly immersive and multisensory extended reality (XR) experiences, holographic communications for telepresence, real-time digital twins for industry and smart cities, advanced industrial automation with remote robotic control, fully autonomous coordinated vehicles, and sophisticated telemedicine applications such as remote surgery.

To realise this ambitious vision, the underlying network infrastructure must undergo a radical evolution. In particular, the optical transport infrastructure—encompassing fronthaul (RU-DU), midhaul (DU-CU), and backhaul (CU–Core/Cloud), collectively referred to as x-Haul—stands as an absolutely critical pillar [\[2\]](#page-27-1). This optical fibre network must support unprecedented performance requirements that surpass even the most advanced 5G networks. The convergence between fixed and mobile networks, as well as the seamless integration of diverse communication technologies (terrestrial, satellite, aerial, and submarine), becomes indispensable within the 6G architecture [\[3\]](#page-27-2).

#### *1.1. Key 6G Requirements for Optical Transport*

The transition to 6G imposes extraordinary demands on the optical transport network, establishing new benchmarks across multiple performance dimensions:

- Throughput: Peak per-device data rates are expected to reach or exceed 1 terabit per second (Tbps), with user-experienced data rates sustained in the range of hundreds of gigabits per second (Gbps). This represents an increase of 50–100 times compared with peak 5G capabilities. Specific applications, such as high-fidelity holographic communications, may require even greater capacities, potentially exceeding 4 Tbps per stream [\[4\]](#page-27-3).
- Latency: End-to-end (E2E) latency must be drastically reduced from the millisecond (ms) range typical of 5G URLLC to microsecond (µs) levels, targeting 10–100 µs [\[5\]](#page-27-4). This constitutes a 10- to 100-fold reduction compared with 5G [\[6\]](#page-27-5). Moreover, not only must average latency be low, but it must also be deterministic, with minimal variation (jitter) [\[7\]](#page-27-6).
- Reliability: The levels of reliability required for hyper-reliable and low-latency communications (HRLLC or eRLLC in 6G terminology) reach extremely high thresholds, with transmission success rates between 99.9999% and 99.9999999%—commonly referred to as "seven to nine nines".
- Connection Density: The 6G network must be capable of supporting a massive density of simultaneously connected devices, potentially ranging between 10<sup>7</sup> and 10<sup>8</sup> devices per square kilometre [\[5\]](#page-27-4). This is fundamental for the Internet of Everything (IoE).
- Synchronisation: The precise coordination of complex network operations, such as advanced beamforming, distributed computing, and cooperative radio interfaces, demands time synchronisation accuracy at the nanosecond (ns) level across the optical network [\[8\]](#page-27-7).
- Energy Efficiency: A significant increase in energy efficiency, measured in bits transmitted per joule of consumed energy, is expected—with improvement targets of up to 100 times compared with 5G [\[5\]](#page-27-4). It is important to note, however, that higher efficiency per bit does not necessarily guarantee a reduction in the network's total energy consumption, given the exponential growth expected in traffic volume [\[9\]](#page-27-8).

*Computation* **2025**, *13*, 286 3 of 29

• AI-Native Intelligence: A fundamental and transversal requirement is that the 6G network architecture must be inherently intelligent (AI-Native). This means that Artificial Intelligence (AI) and Machine Learning (ML) are not merely overlaid applications but are deeply integrated into the fabric of the network—from design to operation and optimisation—including the optical transport layer [\[10\]](#page-27-9).

Table [1](#page-3-0) summarises the magnitude of the leap required in key performance indicators (KPIs) between 5G and 6G, specifically from the perspective of optical transport infrastructure. This table highlights the monumental challenge facing optical infrastructure. The objectives are not merely incremental; they demand a fundamental rethinking of transport architecture and technology to bridge the gap between current capabilities and the ambitious performance targets envisioned for 6G.

| KPI (Key<br>Performance<br>Indicator)    | Unit        | Typical 5G Value     | Target 6G Value                               | Improvement<br>Factor (Approx.) | Sources |
|------------------------------------------|-------------|----------------------|-----------------------------------------------|---------------------------------|---------|
| Peak Data Rate<br>per Device             | Gbps/Tbps   | 20 Gbps              | >1 Tbps                                       | >50×                            | [11]    |
| User-Experienced<br>Data Rate            | Mbps/Gbps   | 100 Mbps             | >1 Gbps                                       | >10×                            | -       |
| End-to-End (E2E)<br>Latency (User Plane) | ms/µs       | ~1 ms                | 10–100 µs                                     | 10×–100×                        | [11]    |
| Reliability<br>(URLLC/HRLLC)             | %           | 99.999% (five nines) | 99.9999–<br>99.9999999%<br>(seven–nine nines) | >100×<br>(in error rate)        | -       |
| Connection Density                       | devices/km2 | 106                  | 107–108                                       | 10×–100×                        | [11]    |
| Synchronisation<br>Accuracy              | µs/ns       | ~µs                  | ~ns                                           | 1000×                           | [12]    |
| Energy Efficiency<br>(Network)           | bits/Joule  | ~107                 | ~109                                          | ~100×                           | [11]    |

<span id="page-3-0"></span>**Table 1.** Comparison of key 5G vs. 6G KPIs for optical transport.

#### *1.2. Second-Order Perspective: Beyond Connectivity*

It is essential to understand that the requirements of 6G, when viewed as a whole, signal a qualitative transformation in the role of the network. It is not simply a linear extension of 5G capabilities. The synergistic combination of terabit-per-second data rates, stable latency in the microsecond range, extreme reliability, and native support for distributed artificial intelligence indicates that 6G is being designed as a platform for real-time interaction between the physical and digital worlds, enabling cyber–physical control on an unprecedented scale—far beyond the mere exchange of data [\[13\]](#page-27-12).

While 5G introduced the ability to support high speed (eMBB), low latency (URLLC), or high density (mMTC), 6G demands the simultaneity of these attributes at extreme levels: ultra-high speed, ultra-low latency, extreme reliability, and high connection density, often required concurrently within the same service or application. This simultaneity is an indispensable prerequisite for the transformative applications defining the 6G vision, such as truly immersive extended reality (XR), precise remote robotic control, and digital twins that reflect and act upon the physical world instantaneously. These applications not only require the transmission of massive data volumes but also their processing, analysis through AI, and, crucially, real-time action on the physical environment (control) with near-instantaneous responsiveness.

*Computation* **2025**, *13*, 286 4 of 29

This fundamentally redefines the role of the optical transport network. It can no longer be regarded as a passive "bit pipe" but must be conceived and designed as an integrated and active platform for communication, computation, and, potentially, sensing geographically distributed and synchronised with nanosecond precision. The location of computing capabilities (at the edge) and the need for ultra-precise synchronisation thus become first-order architectural considerations for 6G optical infrastructure.

The need to achieve terabit-per-second (Tbps) air-interface rates, combined with stable microsecond (µs)-level latencies, reflects a fundamental shift in the focus of network engineering. While 5G concentrated heavily on enhancing radio interface capabilities (e.g., Massive MIMO, mmWave), 6G shifts the critical bottleneck towards the transport and computing infrastructure. Tbps radio-frequency (RF) capabilities and microsecondlevel latency become ineffective if the fibre cannot deliver that volume of data to Edge Computing for real-time processing. This will fundamentally redefine the role of the optical transport network, which can no longer be regarded as a passive "bit pipe" but rather as an active and integrated platform for communication, computation, and, potentially, sensing.

This article is organised as follows: Section [2](#page-4-0) presents the evolution of the optical network architecture and establishes the performance and synchronisation requirements for 6G. Section [3](#page-8-0) provides a detailed analysis of the enabling optical technologies, including a scenario-based selection matrix. Section [4](#page-16-0) addresses AI-driven intelligent management and its associated challenges. Section [5](#page-19-0) discusses nanosecond-level synchronisation. Section [6](#page-22-0) examines implementation, cost, sustainability, and security challenges. Finally, Section [7](#page-25-0) offers conclusions and a strategic roadmap.

# <span id="page-4-0"></span>**2. Evolution of Optical Network Architecture for 6G (x-Haul)**

#### *2.1. Limitations of the Current 5G Optical Infrastructure*

The optical transport infrastructure deployed for 5G, although representing a significant advancement over 4G, presents intrinsic limitations that prevent it from directly meeting the demanding requirements of 6G. These limitations are mainly evident in the fronthaul segment, which is the most latency-sensitive and capacity-intensive part of the network.

#### 2.1.1. G Fronthaul (CPRI/eCPRI over Ethernet/PON)

- Capacity: The Common Public Radio Interface (CPRI) protocol, widely used in 4G and early 5G deployments, has a practical bandwidth limit of approximately 24 Gbps per link and does not scale efficiently to support massive MIMO configurations and the much wider channel bandwidths anticipated for 6G [\[14\]](#page-27-13). The enhanced CPRI (eCPRI) protocol, designed to be more bandwidth-efficient by transporting data in the frequency domain or through higher functional splits, reduces the load but may still prove insufficient for the projected demands of hundreds of Gbps or even Tbps per cell site in 6G [\[15\]](#page-27-14). It is estimated that 6G fronthaul could require more than 500 Gbps per individual cell, aggregating traffic that exceeds 1 Tbps or even 10 Tbps in sites hosting multiple radio units (RUs) [\[16\]](#page-27-15).
- Latency and Jitter: Standard Ethernet, while flexible and cost-effective, lacks inherent mechanisms to guarantee deterministic latency. The variability in packet delay (Packet Delay Variation—PDV), or jitter, introduced by conventional Ethernet switching, is incompatible with the microsecond-level latency requirements and temporal stability necessary for 6G fronthaul [\[14\]](#page-27-13). Passive Optical Network (PON) solutions based on time-division multiplexing (TDM-PON), such as GPON or XGS-PON, although efficient for backhaul or FTTH applications, introduce significant latency (>100 µs) due

*Computation* **2025**, *13*, 286 5 of 29

to their dynamic bandwidth allocation (DBA) mechanisms, making them unsuitable for the most stringent 6G fronthaul segments [\[16\]](#page-27-15).

- Synchronisation: The inherent delay variation in conventional packet-based Ethernet networks poses a major challenge for accurate timing transfer, which is essential to achieve the nanosecond-level synchronisation required by 6G [\[14\]](#page-27-13). Although protocols such as Precision Time Protocol (PTP) over Ethernet can improve accuracy, achieving the nanometric stability and precision required across multiple packetised network hops remains difficult [\[14\]](#page-27-13). A maximum time error of approximately 3 µs is required in O-RAN interfaces, and potentially much lower for advanced 6G functions [\[8\]](#page-27-7).
- 5G PON: Current generations of PON (GPON, XGS-PON, and even the emerging 25G-PON) were not designed to deliver the terabit capacities or microsecond latencies expected to be necessary for aggregated 6G x-Haul transport [\[11\]](#page-27-10). Although 25G-PON represents a significant advancement and may be applicable in certain 5G/5.5G scenarios, a much deeper technological evolution will be required for 6G transport [\[16\]](#page-27-15).

Table [2](#page-5-0) summarises these specific limitations of 5G optical transport in contrast to the projected requirements for 6G x-Haul.

| Parameter                               | Typical 5G<br>Technology     | Typical 5G<br>Limitation | Target 6G Requirement   | Sources |
|-----------------------------------------|------------------------------|--------------------------|-------------------------|---------|
| Fronthaul Capacity (per cell)           | eCPRI over<br>Ethernet/PON   | Tens of Gbps             | >500 Gbps               | [14]    |
| Aggregated Capacity (per site)          | Aggregated<br>Ethernet/PON   | Hundreds of<br>Gbps      | >1–10 Tbps              | [16]    |
| Fronthaul Latency (E2E)                 | Standard<br>Ethernet/TDM-PON | >100 µs (variable)       | <100 µs (deterministic) | [14]    |
| Fronthaul Jitter (PDV)                  | Standard Ethernet            | Variable/High            | Very Low/Controlled     | [14]    |
| Synchronisation Accuracy<br>(Fronthaul) | PTP over<br>Ethernet/PON     | ~µs (variable)           | ~ns (stable)            | [14]    |

<span id="page-5-0"></span>**Table 2.** Limitations of 5G optical transport versus 6G x-Haul requirements.

This table demonstrates that the optical technologies and architectures of 5G, although adequate for their generation, represent a significant bottleneck for 6G. Overcoming these limitations requires not merely incremental improvements but a redefinition of the overall architecture and the adoption of fundamentally new optical technologies.

# 2.1.2. Arquitectura x-Haul Convergente y Flexible Para 6G

To address the challenges and enable the 6G vision, the optical transport architecture must evolve towards a convergent, flexible, open, and intrinsically intelligent model.

- x-Haul Convergence: A unified transport architecture is essential to transparently and efficiently integrate the fronthaul (RU–DU), midhaul (DU–CU), and backhaul (CU–Core/Cloud) segments [\[1\]](#page-27-0). This convergence should support the transport of diverse traffic types (user data, control, synchronisation, management, and AI-related data) with different QoS requirements over a shared physical infrastructure, thereby optimising resource utilisation. The architecture must be adaptable to multiple deployment scenarios, including Distributed Radio Access Networks (DRAN), Centralised (CRAN), and Virtualised (VRAN) topologies [\[17\]](#page-27-16).
- Functional Flexibility (Splits): The disaggregation of base station functions (Baseband Unit—BBU) into Distributed Units (DU) and Centralised Units (CU), promoted by initiatives such as O-RAN, enables flexible division of radio protocol functions

*Computation* **2025**, *13*, 286 6 of 29

(functional splits) [\[1\]](#page-27-0). The 6G optical transport network must dynamically support multiple split options (FFS—Flexible Functional Splits) [\[10\]](#page-27-9). This allows optimisation of the trade-off between required fronthaul bandwidth, end-to-end latency, and the degree of baseband centralisation, adapting to the specific needs of each service and deployment scenario.

- AI-Native Integration: Unlike 5G, where AI is often introduced as an overlay layer, the 6G architecture must be conceived from the ground up to integrate AI natively (AI-Native) [\[10\]](#page-27-9). This means that data collection, AI processing, and ML model execution capabilities must be embedded within optical network elements and management systems, enabling intelligent optimisation, advanced automation, and the creation of AI-driven services.
- Openness and Interoperability: The adoption of open interfaces, such as those specified by the O-RAN Alliance, and the promotion of open-source approaches are crucial to eliminating vendor lock-in, fostering innovation, reducing costs, and ensuring interoperability within a multi-vendor ecosystem [\[3\]](#page-27-2). Global and coordinated standardisation across different organisations (ITU, IEEE, 3GPP, ETSI, O-RAN) is indispensable for the successful deployment of 6G [\[17\]](#page-27-16).
- Proposed Optical Architecture: The emerging architectural vision for 6G x-Haul is based on highly flexible and reconfigurable Wavelength Division Multiplexing (WDM) optical networks. Elements such as Reconfigurable Optical Add-Drop Multiplexers (ROADMs) are extended beyond the core and metro layers to reach the network edge, enabling dynamic wavelength switching [\[18\]](#page-27-17). These reconfigurable WDM networks could be combined with advanced PON technologies (such as Coherent PON) for access and initial aggregation, and could potentially integrate other technologies such as Free-Space Optics (FSO) in specific scenarios. Mesh and flattened architectures are favoured to increase resilience and provide multiple routing paths, as opposed to more rigid ring topologies [\[19\]](#page-27-18).

## 2.1.3. Integration with Edge Computing and Distributed Architectures

The 6G optical architecture cannot be designed in isolation; it must be deeply integrated with distributed computing architectures that are fundamental to enabling many 6G services.

- Cloud–Edge–Device Continuum: 6G materialises the concept of a computational continuum that extends from centralised data centres (Cloud), through multiple tiers of computing nodes at the network edge (Edge Computing, Fog Computing), to processing capabilities embedded in end-user devices themselves [\[19\]](#page-27-18). The optical network acts as the connective fabric that unites this continuum.
- MEC (Multi-Access Edge Computing) and Edge AI: Edge computing (MEC) is crucial for processing data and executing latency-sensitive applications—such as industrial control, AR/VR, and autonomous driving—as well as for enabling AI functions (Edge AI) close to the end user [\[19\]](#page-27-18). The optical transport network must provide ultra-lowlatency, high-bandwidth connectivity to these MEC nodes, whose locations may range from cell sites to regional central offices [\[11\]](#page-27-10). The evolution of ETSI MEC is aimed at supporting 6G requirements [\[20\]](#page-27-19).
- Distributed Computing Paradigms: Beyond MEC, the 6G architecture must support paradigms such as Fog Computing, which introduces an intermediate computing layer between the edge and the cloud, as well as other distributed approaches that optimise processing placement according to application requirements [\[18\]](#page-27-17).
- Joint Communication–Computation Optimisation (JCC): The efficiency of distributed applications in 6G will depend on the network's ability to jointly manage and opti-

*Computation* **2025**, *13*, 286 7 of 29

mise communication resources (optical bandwidth, latency) and computing resources (CPU, GPU, memory, storage) across the Cloud–Edge continuum [\[13\]](#page-27-12). The optical network must enable this joint management by providing not only connectivity but also link-state awareness and rapid reconfiguration capabilities to support the optimal placement of computational tasks.

#### 2.1.4. Second- and Third-Order Perspectives: Architectural Implications

The architectural evolution described above has profound implications that extend far beyond mere technological upgrades.

First, x-Haul convergence and functional split flexibility (FFS) should not be regarded solely as technical optimisations but as critical enablers for resource efficiency and the dynamic adaptability of 6G services. This flexibility allows the network to dynamically locate both network processing functions (from RAN and Core) and application functions (such as AI models or MEC services) at the optimal point within the Cloud–Edge–Device continuum. The placement is determined in real time, based on the specific latency, bandwidth, processing capacity, and energy efficiency requirements of each service or application [\[1\]](#page-27-0). For example, a URLLC service may require a lower split (processing closer to the RU) to minimise latency, at the expense of increased optical fronthaul bandwidth demand, whereas an eMBB service may benefit from a higher split (more centralised processing) to conserve optical bandwidth [\[1\]](#page-27-0). The ability of the optical network to dynamically support and reconfigure these splits [\[19\]](#page-27-18) is therefore fundamental to optimising global resource utilisation (fibre, spectrum, computing, and energy) and ensuring Quality of Service (QoS) for a heterogeneous mix of 6G applications. This, in turn, requires a highly programmable optical network with intelligent and automated orchestration capable of making such complex decisions in real time [\[21\]](#page-27-20).

Second, the deep integration with Edge Computing and the imperative need to support distributed AI including paradigms such as Federated Learning (FL) [\[22\]](#page-27-21) drive a significant decentralization of intelligence and control across the network. While this provides clear benefits in terms of latency and privacy [\[23\]](#page-27-22), it also exponentially increases the complexity of optical network management and orchestration. The network is no longer limited to connecting points A and B; it must now intelligently and dynamically interconnect a multitude of distributed computing nodes at the edge [\[11\]](#page-27-10). Orchestration must now jointly consider and manage heterogeneous resources: optical capacity (wavelengths, bandwidth), optical latency, edge computing resources (CPU, GPU, NPU), distributed storage, and the AI models themselves [\[13\]](#page-27-12). This multidimensional and distributed management is orders of magnitude more complex than traditional connectivity management, making AI itself an indispensable tool to handle the inherent complexity of the 6G architecture [\[24\]](#page-27-23).

#### 2.1.5. Extreme 6G Requirements for Optical Transport

Meeting 6G performance objectives requires an optical transport infrastructure capable of supporting demands far beyond those of 5G. Performance requirements are up to 100 times higher than those of 5G in several key metrics, particularly in the fronthaul, where latency, capacity, and synchronisation constraints are most stringent.

- Throughput: Peak per-device rates are expected to reach or exceed 1 Tbps, with sustained user-experienced rates in the hundreds of Gbps. Specific applications such as high-fidelity holographic communications—may require capacities surpassing 4 Tbps per stream.
- Deterministic Latency: End-to-end (E2E) latency must be drastically reduced, moving from the millisecond-level characteristic of 5G URLLC to microsecond (µs) levels, with targets in the 10–100 µs range. Moreover, a strict requirement is that latency be

*Computation* **2025**, *13*, 286 8 of 29

deterministic, with minimal variation (jitter). Jitter stress is a limiting factor for packet transport, as the optical network must guarantee predictable and stable latency fundamental for real-time control systems and HRLLC (Hyper-Reliable Low-Latency Communication) applications.

• Nanosecond-Level Synchronisation: The precise coordination of complex network operations—such as advanced beamforming, distributed computing, and Integrated Sensing and Communication (ISAC)—demands time synchronisation accuracy at the nanosecond (ns) level across the optical network. This precision requirement represents a 1000-fold improvement over 5G.

The magnitude of this leap underscores the monumental challenge faced by the optical infrastructure, as presented in Table [1.](#page-3-0) The synergistic combination of nanosecond-level synchronisation and microsecond-level latency imposes precision engineering requirements. This compels network designers to adopt engineering approaches that are far closer to industrial control systems (OT) and Time-Sensitive Networking (TSN) than to traditional packet networks, where Packet Delay Variation (PDV) was tolerable. The optical network must therefore be inherently designed to operate as a real-time system, in which temporal stability is just as important as bandwidth. This imperative directly affects the cost and complexity of every transport component.

# <span id="page-8-0"></span>**3. Enabling Optical Technologies for 6G**

To materialise the convergent and flexible x-Haul architecture and meet the stringent 6G KPIs, an arsenal of advanced optical technologies—some evolutionary and others disruptive—is required.

The optical transport infrastructure deployed for 5G represents a significant bottleneck for 6G. A 5G fronthaul based on eCPRI over Ethernet or TDM-PON typically handles only tens of Gbps. This becomes insufficient when the target requirement for 6G fronthaul exceeds 500 Gbps per cell, with aggregated capacity reaching >1–10 Tbps per site. Additionally, standard Ethernet and TDM-PON solutions introduce variable latencies that exceed 100 µs, which is incompatible with the 6G requirement for deterministic latency below 100 µs.

To overcome these limitations, the architecture must evolve towards a convergent, flexible, open, and intrinsically intelligent model.

- X-Haul Convergence: A unified transport architecture is essential to seamlessly integrate fronthaul, midhaul, and backhaul over a reconfigurable WDM infrastructure.
- Functional Flexibility (FFS): The disaggregation of base station functions (promoted by O-RAN) into Distributed Units (DUs) and Centralised Units (CUs) enables dynamic division of radio functions. The 6G optical transport must be capable of dynamically supporting these split options to optimise the trade-off between required bandwidth, end-to-end latency, and the degree of processing centralisation.

The 6G optical network must serve as the backbone of the Cloud–Edge–Device computational continuum. Multi-Access Edge Computing (MEC) and Edge AI are crucial for processing latency-sensitive data close to the end user. The efficiency of distributed 6G applications will depend on the network's ability to jointly manage and optimise communication resources (optical bandwidth, latency) and computing resources (CPU, GPU, etc.).

The emerging architectural vision is based on highly reconfigurable WDM optical networks, where ROADMs (Reconfigurable Optical Add-Drop Multiplexers) extend beyond the core towards the edge to enable dynamic wavelength switching.

*Computation* **2025**, *13*, 286 9 of 29

Figure [1](#page-9-0) illustrates the 6G transport architecture, showing the convergence of fronthaul, midhaul, and backhaul over a unified infrastructure of advanced WDM and PON systems. It depicts the hierarchical distribution of computing nodes (RU, DU/MEC, CU/Cloud) along the Cloud–Edge continuum. The ROADMs extend from the core to the aggregation nodes, enabling dynamic wavelength switching. The entire system is supervised by software-defined Management and Control planes (SDN/NFV) enhanced with AI, with distributed control loops (e.g., O-RAN RICs) for real-time optimisation of functional splits and the joint allocation of optical and computing resources.

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

**Figure 1.** Convergent 6G X-Haul Architectural Model.

The combination of functional flexibility (FFS) and network function virtualisation (NFV/CNF) drives the decentralisation not only of data processing (MEC) but also of the control and management plane itself. The ability of the optical network to support and dynamically reconfigure these splits is essential for optimising the global use of resources (fibre, spectrum, computing, energy). This requires intelligent and automated orchestration capable of making complex real-time decisions regarding the optimal placement of computational tasks. Such multidimensional and distributed management is exponentially more complex than traditional connectivity management, making Artificial Intelligence itself an indispensable tool for handling the inherent complexity of the 6G architecture.

#### *3.1. Evolution of PON: Beyond 50G*

Passive Optical Networks (PONs) are fundamental in current access networks due to their cost efficiency and point-to-multipoint topology. However, for 6G, they must evolve significantly in both capacity and performance.

To achieve capacities above 100 Gbps in access and aggregation networks, Coherent Detection emerges as the key technology for overcoming the dispersion limitations and power budget constraints of Direct Detection solutions (Intensity Modulation and Direct Detection—IM/DD). Coherent detection provides higher receiver sensitivity and enables the use of more spectrally efficient modulation formats. However, the main challenges for CPON lie in the cost and complexity of coherent transceivers and in the efficient implementation of Digital Signal Processing (DSP) to handle the burst-mode upstream traffic.

# 3.1.1. 50G-PON

Standardized by the ITU-T under the G.9804.x series, 50G-PON represents the next evolutionary step, offering symmetric 50 Gbps or asymmetric configurations (50 Gbps downstream/12.5 or 25 Gbps upstream) [\[25\]](#page-27-24). A key innovation is the mandatory introduction of Digital Signal Processing (DSP) to compensate for bandwidth limitations and chromatic dispersion at these data rates [\[26\]](#page-28-0). It allows coexistence with previous genera*Computation* **2025**, *13*, 286 10 of 29

tions (GPON, XGS-PON) over the same fibre infrastructure [\[25\]](#page-27-24). Although it constitutes an important advance, it is regarded primarily as an intermediate step—potentially suitable for backhaul or midhaul in early 5.5G/6G scenarios, but insufficient for the most demanding 6G fronthaul requirements [\[16\]](#page-27-15).

#### 3.1.2. 100G/200G-PON and Beyond

To achieve the hundreds of Gbps or even Tbps capacities required for aggregated 6G x-Haul transport, subsequent generations of PON are being actively investigated, targeting data rates of 100 Gbps, 200 Gbps per wavelength, and even higher [\[26\]](#page-28-0). At such rates, conventional Intensity Modulation/Direct Detection (IM/DD) technology faces severe challenges related to optical power budget limitations and chromatic dispersion penalties, particularly in the C- and L-bands [\[26\]](#page-28-0).

#### 3.1.3. Coherent Optical Access (CPON—Coherent PON)

Coherent PON (CPON) is emerging as a key enabling technology to overcome the limitations of IM/DD and achieve >100 Gbps speeds in PONs [\[26\]](#page-28-0). Coherent detection offers several significant advantages:

- Higher Receiver Sensitivity: Enables greater optical path losses, translating into longer reach or a higher number of users per OLT port (split ratio).
- Advanced Modulation Formats: Allows the use of spectrally efficient modulation schemes (e.g., QAM), increasing the capacity per wavelength.
- DSP-Based Dispersion Compensation: The DSP inherent to coherent detection can linearly compensate for chromatic dispersion and other optical channel impairments.
- Channel Selectivity: Facilitates WDM-PON implementation by allowing fine receiver tuning.

The main challenges for CPON are the cost and complexity of coherent transceivers historically much higher than direct-detection equivalents—and the efficient implementation of DSP, particularly for handling burst-mode upstream signals in TDMA topologies [\[26\]](#page-28-0). The standardisation of CPON is currently underway within organisations such as the ITU-T [\[27\]](#page-28-1).

# 3.1.4. WDM-PON

Wavelength Division Multiplexing in PON (WDM-PON) uses multiple wavelengths over the same fibre, assigning one or more dedicated wavelengths to each user (ONU) or group of users/services. This approach enables a significant increase in aggregate capacity and provides logical point-to-point connections over a physical point-to-multipoint infrastructure. In 6G, WDM-PON could be employed to segment traffic, offer differentiated services, or provide ultra-high-capacity connections closer to the network edge [\[28\]](#page-28-2).

# *3.2. Exponential Capacity Increase: SDM and New Bands*

To scale the capacity of backbone and aggregation networks beyond the limits of conventional Wavelength Division Multiplexing (WDM), new dimensions of multiplexing and spectrum utilisation are being explored.

SDM, which uses Multicore Fibre (MCF) or Few-Mode Fibre (FMF), is fundamental for scaling the capacity of aggregation and core networks beyond the spectral limits of conventional WDM. MCF integrates multiple fibre cores within a single cladding, multiplying capacity according to the number of cores. The most significant challenge is the mitigation of inter-core crosstalk. FMF employs multiple spatial modes of light to carry independent signals, requiring complex modal multiplexing/demultiplexing techniques and DSP (optical MIMO).

*Computation* **2025**, *13*, 286 11 of 29

# Spatial Division Multiplexing (SDM)

This technique exploits the spatial dimension within the optical fibre to transmit multiple data channels in parallel, offering a multiplicative increase in the total fibre capacity [\[12\]](#page-27-11). It is considered fundamental for avoiding the "capacity crunch" of standard single-mode fibre. Two main approaches are under investigation:

- Multi-Core Fibre (MCF): Integrates multiple cores (light-guiding paths) within a single fibre cladding. Each core behaves as an independent fibre, multiplying total capacity by the number of cores [\[12\]](#page-27-11). The main technical challenge lies in inter-core crosstalk, where light leaks from one core into adjacent ones, causing interference. Minimising this crosstalk requires highly precise fibre designs and manufacturing techniques [\[12\]](#page-27-11).
- Few-Mode Fibre (FMF): Employs a single (or enlarged) core that supports the propagation of multiple spatial modes of light, each carrying an independent data signal [\[12\]](#page-27-11). It requires modal multiplexing/demultiplexing techniques (optical MIMO) and Digital Signal Processing (DSP) to separate signals at the receiver. In addition to specialised fibres, SDM demands compatible optical components such as spatial multiplexers/demultiplexers and optical amplifiers capable of simultaneously amplifying signals across all cores or modes [\[12\]](#page-27-11). The associated complexity and cost remain significant barriers to large-scale deployment at present.
- New Optical Bands (Beyond C + L): Traditional optical transmission has focused on the C-band (Conventional, ~1530–1565 nm) and L-band (Long, ~1565–1625 nm) due to the availability of Erbium-Doped Fibre Amplifiers (EDFA). To further increase per-fibre capacity, active research is investigating the utilisation of other ITU-T-defined transmission bands: O (Original, ~1260–1360 nm), E (Extended, ~1360–1460 nm), S (Short, ~1460–1530 nm), and U (Ultra-long, ~1625–1675 nm) [\[29\]](#page-28-3). Recent experiments have demonstrated the feasibility of ultra-long-haul transmission (>800 km) with aggregate capacities exceeding 100 Tbps by jointly exploiting the C, L, and U bands through innovative techniques such as parametric optical band conversion for U-band amplification [\[30\]](#page-28-4). Opening up these new bands could expand the total usable fibre bandwidth beyond 20 THz [\[30\]](#page-28-4), but this requires the development of new optical components (amplifiers, filters, etc.) and efficient conversion techniques to operate within these spectral regions.

#### *3.3. Drastic Latency Reduction: Hollow-Core Fibre (HCF)*

For the most latency-sensitive 6G applications, even the speed of light in silica fibre can become a limiting factor. Hollow-Core Fibre (HCF) is emerging as a disruptive technology.

HCF emerges as a disruptive and crucial technology for the most latency-sensitive 6G applications. By guiding light through a hollow air-filled core, HCF reduces propagation latency by more than 30% (approximately 1.54 µs/km), an unmatched physical advantage for HRLLC services in industrial control or telesurgery. Despite advances in lowering transmission losses (reported to be as low as 0.11 dB/km), the high manufacturing cost, lower production yield, and the difficulty of fusion splicing (approximately 0.1 dB loss) remain significant barriers to large-scale deployment.

#### 3.3.1. Operating Principle

HCF guides light through a central hollow channel filled with air or a vacuum instead of a solid silica core [\[31\]](#page-28-5). Because light travels approximately 50% faster in air than in glass, HCF reduces propagation latency by about 1.54 microseconds per kilometre of fibre, representing a latency improvement of over 30% compared with standard fibre [\[31\]](#page-28-5).

*Computation* **2025**, *13*, 286 12 of 29

# 3.3.2. Additional Benefits

HCF also exhibits significantly lower optical nonlinearity than standard fibre, simplifying or even eliminating the need for nonlinear compensation through complex DSP, particularly at high powers or in dense WDM systems [\[32\]](#page-28-6). Designs featuring low chromatic dispersion are also under active investigation.

# 3.3.3. Status and Advances

Remarkable progress has been achieved in reducing transmission losses in HCF, with reported values as low as 0.11 dB/km—surpassing even the theoretical limit of conventional single-mode fibre [\[32\]](#page-28-6). Commercial HCF cable solutions already exist, including terminations with standard connectors and fusion splicing techniques, and pilot deployments have been carried out in active networks [\[31\]](#page-28-5).

#### 3.3.4. Deployment Challenges

Despite these advances, HCF still faces significant practical challenges. Its fabrication process is more complex and costly than that of standard fibre, and production yield remains lower [\[32\]](#page-28-6). Fusion splicing of HCF requires more sophisticated and expensive equipment, and splice losses (~0.1 dB) are generally higher than with conventional fibre [\[32\]](#page-28-6). Integration with existing fibre infrastructure and long-term compatibility are also areas of active research [\[32\]](#page-28-6). Cost remains a major barrier to widespread adoption [\[33\]](#page-28-7).

## *3.4. Flexible and Resilient Connectivity: Free-Space Optics (FSO)*

Free-Space Optics (FSO) offers a wireless alternative for high-speed data transmission using light beams (laser or LED) propagating through air or space.

FSO provides a high-capacity, low-latency wireless alternative, complementing the optical fibre infrastructure in scenarios where fibre deployment is unfeasible or prohibitively expensive. It is valuable for temporary fronthaul/backhaul links, hard-to-reach sites, or in the non-terrestrial segment (Non-Terrestrial Networks—NTNs). Its main limitation is its susceptibility to atmospheric conditions (fog, rain, turbulence). To mitigate these effects, advanced techniques such as adaptive optics and hybrid RF/FSO systems—using a radio-frequency link (e.g., mmWave) as a backup—are required.

#### 3.4.1. Concept and Application in 6G x-Haul

FSO can complement optical fibre infrastructure, particularly in scenarios where fibre deployment is impractical, costly, or time-consuming [\[34\]](#page-28-8). Typical 6G use cases include fronthaul/backhaul links for hard-to-reach cell sites, temporary connections for events, rapid network extensions, and potentially links in non-terrestrial networks (satellites, HAPS) [\[34\]](#page-28-8). It can also be integrated into hybrid FSO–fibre networks [\[34\]](#page-28-8).

#### 3.4.2. Advantages

FSO provides very high bandwidth (comparable to fibre), extremely low latency (as light travels almost at the speed of vacuum), rapid deployment, and operation in unlicensed spectrum [\[34\]](#page-28-8).

#### 3.4.3. Technical Challenges

The main limitation of FSO is its susceptibility to atmospheric conditions [\[34\]](#page-28-8). Fog, heavy rain, snow, and smoke can severely attenuate or scatter the optical signal. Atmospheric turbulence—caused by variations in temperature and pressure—induces fluctuations in signal intensity (scintillation) and beam wander, degrading link quality [\[34\]](#page-28-8). Maintaining precise alignment between transmitter and receiver (Pointing, Acquisition, and Tracking—PAT) is critical and can be affected by vibration, wind, or thermal expansion

*Computation* **2025**, *13*, 286 13 of 29

of supporting structures [\[34\]](#page-28-8). Interference from other light sources (solar or artificial) and link security (potential interception) are also important considerations [\[34\]](#page-28-8).

## 3.4.4. Solutions

Various techniques are being developed to mitigate these challenges: adaptive modulation and coding schemes that adjust transmission parameters according to channel conditions; hybrid RF/FSO systems employing a radio-frequency link (e.g., mmWave) as a backup when the FSO link degrades; adaptive optics to compensate for turbulence; advanced PAT technologies using MEMS mirrors, optical phased arrays (OPAs), or liquid crystals; spatial filtering to reduce interference; and secure communication protocols [\[34\]](#page-28-8).

#### *3.5. Advanced Optical Components: Photonics and Switching*

Miniaturisation, energy efficiency, and switching flexibility are essential for the 6G optical network, particularly at the network edge.

Silicon Photonics and Photonic Integrated Circuits (PICs) are crucial for miniaturisation, energy efficiency, and large-volume production, leveraging CMOS fabrication processes.

Integration drastically reduces size and weight and minimises the energy consumption of interconnects. The technique of Optical Co-Packaging (CPO), which integrates optical and electronic components within the same package, is fundamental for reducing latency and energy consumption at the electrical–optical interface, particularly in data centres and edge nodes hosting intensive AI workloads. Silicon photonics PICs are essential for enabling advanced RAN functions such as optical beamforming networks for terahertz (THz) and mmWave technologies, as they allow precise beam steering with low signal loss. Recent progress even demonstrates the potential of photonic quantum chips to accelerate complex AI tasks at the Edge.

Advanced Reconfigurable Optical Add-Drop Multiplexing (ROADM) enables remote and programmable reconfiguration of WDM paths without the need for O-E-O (Optical–Electrical–Optical) conversions, improving network agility and efficiency. For 6G, ROADMs are expected to be deployed closer to the edge to facilitate dynamic allocation of optical resources.

The key challenge lies in balancing ROADM flexibility with the stringent latency requirements of 6G services. Switching time must be ultra-fast so as not to introduce latency when reconfiguring paths for critical services. Ultra-high-capacity optical switching architectures are currently being explored to address these needs.

#### 3.5.1. Silicon Photonics and PICs (Photonic Integrated Circuits)

This technology enables the integration of multiple optical components and functions (such as lasers, modulators, photodetectors, multiplexers/demultiplexers, and waveguides) into a single silicon chip, using mature and scalable CMOS fabrication processes [\[35\]](#page-28-9). The key benefits include:

- Miniaturisation: A drastic reduction in the size and weight of optical components.
- Lower Energy Consumption: Integration reduces losses and the power required for inter-component connections.
- Mass Production and Cost: Leverages the economies of scale of the semiconductor industry.
- Co-Packaged Optics (CPO): Facilitates close integration of optical and electronic components to reduce latency and power consumption at the electro–optical interface.
- Silicon photonics and PICs are therefore crucial for developing compact, low-power, and cost-effective optical transceivers, essential for dense 6G edge deployments and for meeting the increasing bandwidth demand of AI-driven data centres [\[35\]](#page-28-9).

*Computation* **2025**, *13*, 286 14 of 29

## 3.5.2. Optical Switching and ROADMs

Reconfigurable Optical Add–Drop Multiplexers (ROADMs) are key nodes in WDM networks that allow the remote and programmable addition, extraction, or passthrough of specific wavelengths without requiring Optical–Electrical–Optical (O–E–O) conversion [\[18\]](#page-27-17). In 6G, ROADMs are expected to be deployed closer to the network edge to provide greater flexibility and agility in optical resource allocation [\[36\]](#page-28-10). Architectures based on ROADMs combined with packet switches can create reconfigurable x-Haul networks that support heterogeneous interfaces and traffic aggregation in both optical and packet domains [\[36\]](#page-28-10).

A key challenge lies in balancing optical reconfiguration flexibility with switching times, which must remain compatible with 6G service latency requirements [\[37\]](#page-28-11). Ultra-fast and ultra-high-capacity optical switching architectures are under investigation for different network needs [\[38\]](#page-28-12).

#### *3.6. Second- and Third-Order Perspectives: Technological Synergies and Trade-Offs*

The selection and integration of these advanced optical technologies are far from trivial and involve important interdependencies and trade-offs.

First, it is crucial to recognise that no single optical technology can, on its own, solve all the multifaceted challenges of 6G transport. HCF offers the lowest latency but faces cost and splicing-complexity barriers [\[31\]](#page-28-5). SDM promises massive capacity but introduces intercore crosstalk and requires complex components [\[12\]](#page-27-11). CPON scales access capacity but increases DSP complexity and transceiver cost [\[26\]](#page-28-0). FSO provides deployment flexibility but is vulnerable to atmospheric conditions [\[34\]](#page-28-8). PICs are efficient and compact but may have limitations in extreme performance metrics [\[35\]](#page-28-9).

Therefore, the optimal solution for 6G optical infrastructure will likely lie in the synergistic and intelligent combination of multiple technologies. A realistic x-Haul architecture should strategically integrate these technologies, leveraging each where its strengths are most advantageous and its weaknesses can be mitigated—either through complementary technologies or through the inherent intelligence and reconfigurability of the network architecture. For example, HCF could be used for ultra-low-latency critical connections, SDM for high-capacity backbones, CPON for flexible access aggregation, FSO for backup or rapiddeployment links, and PICs for efficient edge transceivers. This heterogeneous integration demands extremely sophisticated network planning, management, and orchestration, likely assisted by AI.

Second, there is an inherent and fundamental tension between the pursuit of extreme performance (Tbps throughput, µs latency, 7–9 "nines" reliability), the technological complexity associated with the solutions that enable it (coherent optics, SDM, HCF, advanced DSP, fast optical switching), and the economic imperative to keep deployment and operational costs (CapEx and OpEx) under control—particularly in the access and edge segments, which are the most geographically extensive. Technologies such as coherent optics [\[27\]](#page-28-1), SDM [\[12\]](#page-27-11), and HCF [\[32\]](#page-28-6) are intrinsically more complex and expensive to manufacture, install, and maintain than more traditional optical technologies (IM/DD, standard single-mode fibre).

While they offer the necessary performance leaps for 6G, their mass and economically viable adoption will critically depend on factors such as global standardisation [\[39\]](#page-28-13), largevolume production (where PICs play a key role [\[35\]](#page-28-9)), continuous innovation in materials and processes, and intelligent network architectures that optimise their use (e.g., Open RAN [\[40\]](#page-28-14), infrastructure sharing [\[40\]](#page-28-14)). Network operators will need to make careful strategic decisions about where and when to deploy these advanced technologies, evaluating return on investment and considering whether more conventional solutions may suffice

Computation **2025**, 13, 286 15 of 29

for certain segments or less demanding services. Table 3 summarises the key optical technologies discussed and their potential role in the 6G x-Haul.

<span id="page-15-0"></span>**Table 3.** Key optical technologies for 6G x-Haul.

| Technology                  | Key Principle                            | Main Benefit for 6G x-Haul                                                     | Main Challenge                                                       | Sources |
|-----------------------------|------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------|---------|
| Evolved PON<br>(>50G)/CPON  | Higher speed per<br>λ/Coherent Detection | High Access/Aggregation<br>Capacity; Extended<br>Reach/Split (CPON)            | Cost/Complexity (CPON);<br>Burst-Mode DSP (CPON)                     | [1]     |
| SDM (MCF/FMF)               | Spatial Multiplexing (Cores/Modes)       | Per-Fibre Capacity<br>Multiplication                                           | Crosstalk (MCF); Complexity (Components, DSP); Cost                  | [4]     |
| Hollow-Core Fibre<br>(HCF)  | Propagation in<br>Air/Vacuum             | Ultra-Low Latency (~30%<br>reduction); Low Optical<br>Nonlinearity             | Manufacturing/Deployment<br>Cost; Splice Losses;<br>Robustness       | [40]    |
| Free-Space Optics<br>(FSO)  | Wireless Optical<br>Transmission         | Deployment Flexibility; High<br>Bandwidth; Low Latency                         | Atmospheric Sensitivity;<br>Alignment (PAT); Security                | [1]     |
| Silicon Photonics/PICs      | On-Chip Optical<br>Integration           | Miniaturisation; Low Power<br>Consumption; Cost (High<br>Volume); Co-Packaging | Performance Limitations (vs.<br>Other Materials); Coupling<br>Losses | [35]    |
| ROADMs/Optical<br>Switching | Flexible Wavelength<br>Switching         | Network Agility;<br>Reconfigurability; Efficiency<br>(O-E-O Bypass)            | Switching Speed vs. Latency;<br>Edge Cost                            | [15]    |

Given that 6G infrastructure must be heterogeneous to meet diverse and often conflicting performance requirements (capacity versus latency), the selection and integration of technologies must be strategic. Table 4 provides a framework for decision-making, mapping each technology to its performance niche and weighing the corresponding trade-off. The need to integrate multiple technologies (HCF, SDM, CPON, PICs) in order to meet all 6G KPIs implies a risk of ecosystem fragmentation. Investment in disparate solutions is costly and requires rigorous interface standardisation. If global standardisation fails, or if the costs of mass manufacturing do not fall rapidly (particularly for HCF and SDM), operators may be forced to deploy ad hoc proprietary solutions, losing the economies of scale promised by open architectures and significantly delaying the full deployment of 6G's potential.

<span id="page-15-1"></span>**Table 4.** Optical technology selection matrix for 6G use cases.

| <b>Optical Technology</b>  | Primary KPI<br>Addressed     | Main 6G Application                                                    | Typical Use Scenario                                               | Key Trade-Off                                         |
|----------------------------|------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------|
| HCF (Hollow-Core<br>Fibre) | Latency (<10 μs)             | HRLLC (Industrial Control,<br>Remote Surgery)                          | Critical fronthaul,<br>High-frequency links<br>(financial trading) | High deployment and splicing cost                     |
| SDM (MCF/FMF)              | Capacity (Tbps)              | High-Capacity Core<br>Networks, Data Centre<br>Interconnection (Cloud) | Massive backhaul                                                   | Component complexity, crosstalk risk                  |
| CPON (Coherent)            | Capacity<br>(Gbps)/Reach     | Access and Aggregation,<br>Midhaul with high<br>split ratios           | Dense metropolitan<br>X-Haul                                       | Transceiver cost,<br>burst-mode DSP<br>complexity     |
| PICs/CPO                   | Energy<br>Efficiency/Density | Edge Computing,<br>Fronthaul Aggregation<br>Nodes                      | Edge interconnects                                                 | Extreme performance vs. silicon scalability           |
| FSO                        | Deployment<br>Flexibility    | Temporary<br>Backhaul/Fronthaul,<br>Hard-to-Reach Areas, NTN           | Urban point-to-point links, Hybrid systems                         | Atmospheric<br>vulnerability, need for<br>precise PAT |

*Computation* **2025**, *13*, 286 16 of 29

# <span id="page-16-0"></span>**4. Intelligent Management and Orchestration of the 6G Optical Network**

The inherent complexity of 6G optical architectures and technologies renders traditional network management approaches insufficient. Artificial Intelligence (AI) and advanced automation, enabled by paradigms such as Software-Defined Networking (SDN) and Network Function Virtualisation (NFV), are indispensable.

# *4.1. The Role of SDN/NFV: Towards Automation and Programmability*

Software-Defined Networking (SDN) and Network Function Virtualisation (NFV), which began to be adopted in 5G, become even more critical in 6G to manage the required levels of flexibility and complexity.

#### 4.1.1. SDN (Software-Defined Networking)

By separating the control plane (network intelligence) from the data plane (traffic forwarding), SDN enables centralised and programmatic management of network infrastructure, including optical elements [\[41\]](#page-28-15). An SDN controller can dynamically configure optical paths, allocate wavelengths, adjust transceiver parameters, and manage network topology through open interfaces and Application Programming Interfaces (APIs) [\[42\]](#page-28-16). This is essential for the dynamic reconfigurability of the 6G x-Haul, allowing the network to adapt to changing service demands and channel conditions [\[42\]](#page-28-16). Open-source SDN controllers such as ETSI TeraFlowSDN are evolving to manage complex transport networks that include both optical and packet-based devices [\[42\]](#page-28-16).

#### 4.1.2. NFV (Network Functions Virtualization)

NFV decouples network functions—such as Centralised Unit (CU) and Distributed Unit (DU) functions in RAN, or Core Network functions—from proprietary hardware, enabling them to operate as software-based Virtual Network Functions (VNFs) or, more recently, Cloud-Native Network Functions (CNFs) on standard IT infrastructure (COTS servers, storage, and switches) [\[13\]](#page-27-12). This provides enormous flexibility to deploy, scale, and manage network functions anywhere along the Cloud–Edge continuum, optimising resource utilisation and accelerating the introduction of new services [\[19\]](#page-27-18).

# 4.1.3. Integration SDN/NFV

The combination of SDN and NFV enables automated, end-to-end orchestration of network services [\[43\]](#page-28-17). A Management and Network Orchestration (MANO) system can dynamically request both the optical connectivity required (via the SDN controller) and the necessary virtualised network functions (via the NFV Infrastructure Manager—NFVI) to instantiate and manage a complete 6G service, such as a network slice with specific QoS requirements.

#### *4.2. AI/ML Applications in Optical Network Management*

Artificial Intelligence (AI) and Machine Learning (ML) are the key tools for enabling intelligence within SDN/NFV-based network management and orchestration.

#### 4.2.1. Intelligent Orchestration and Management

Given the multidimensional complexity of 6G networks—encompassing heterogeneous technologies, services, and resources—AI/ML becomes fundamental for autonomous and optimised decision-making in optical network management [\[19\]](#page-27-18).

#### 4.2.2. Resource Optimisation

AI/ML algorithms, particularly Reinforcement Learning (RL), can learn optimal policies for the dynamic allocation of resources within the optical network—such as route

*Computation* **2025**, *13*, 286 17 of 29

selection, wavelength assignment, transmission power adjustment, and functional split configuration—in real time, adapting to changing traffic and channel conditions [\[23\]](#page-27-22). Multi-Agent Systems (MASs), where distributed AI agents collaborate, represent a promising approach for decentralised and rapid decision-making in complex optical networks [\[44\]](#page-28-18).

#### 4.2.3. Predictive Maintenance

AI/ML can analyse large volumes of telemetry data collected from the optical network (e.g., optical power, Optical Signal-to-Noise Ratio—OSNR, error rates) to detect subtle patterns, predict imminent component failures (transceivers, amplifiers, fibres), and schedule proactive maintenance activities before service disruptions occur, thereby improving reliability and reducing operational costs [\[22\]](#page-27-21).

#### 4.2.4. Autonomous Management (Zero-Touch Management—ZSM)

The ultimate goal is to achieve self-managing networks. AI/ML powers the closedloop automation mechanisms that enable the network to monitor itself, analyse its state, make decisions, and execute corrective actions autonomously (self-configuration, selfoptimisation, self-healing) [\[13\]](#page-27-12). Intent-Based Networking (IBN) uses AI to translate highlevel business or service objectives (the "intent") into the low-level configurations and actions required in the optical network [\[19\]](#page-27-18). Large Language Models (LLMs) are being explored to enable intent specification even in natural language [\[44\]](#page-28-18).

# 4.2.5. Security

AI/ML can enhance optical network security through intelligent anomaly detection in traffic or device behaviour that may indicate attacks or intrusions, enabling faster and more accurate responses [\[45\]](#page-28-19).

AI/ML becomes the indispensable engine for orchestration, capable of handling the multidimensional and highly dynamic decision space of 6G. Algorithms such as Reinforcement Learning (RL) can optimise the allocation of optical resources (route selection, functional split configuration) in real time.

Figure [2](#page-18-0) illustrates the closed-loop process (perception, analysis, decision, execution) that is fundamental to autonomous operation. The optical network layer acts as the perceptual system, extracting real-time telemetry data (e.g., latency of HCF links, OSNR in SDM) and feeding this information into the intelligence layer (ML/RL within the RIC or MANO). AI/ML models analyse these data, predict performance, and make optimisation decisions. These decisions are executed through the control plane (SDN) to dynamically reconfigure optical resources (e.g., wavelength switching via ROADM) and virtualised computing resources (e.g., adjusting functional splits or relocating VNFs/CNFs), proactively and autonomously ensuring QoS under a Zero-Touch paradigm. Table [5](#page-17-0) details the application of machine learning models to specific optical transport tasks.

<span id="page-17-0"></span>**Table 5.** Machine learning solutions for 6G optical transport management.

| Application Domain     | Critical Management Task                                 | Representative ML<br>Algorithm/Model                                | Benefit in 6G                                                                                                      |
|------------------------|----------------------------------------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Resource Optimisation  | Dynamic Route and<br>Wavelength Assignment<br>(RWA)      | Reinforcement Learning<br>(RL)/Multi-Agent Systems<br>(MAS)         | Real-time adaptation to traffic and<br>channel variations, optimising<br>throughput and latency.                   |
| Predictive Maintenance | Failure prediction in<br>transceivers, fibre degradation | Recurrent Neural Networks<br>(RNNs)/Anomaly Detection<br>Algorithms | Reduction in operational costs<br>and improved reliability<br>(7–9 nines) by acting proactively<br>before failure. |

*Computation* **2025**, *13*, 286 18 of 29

| Application Domain          | Critical Management Task                                  | Representative ML<br>Algorithm/Model                        | Benefit in 6G                                                                                                      |
|-----------------------------|-----------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Autonomous<br>Orchestration | Implementation of<br>Intent-Based Management<br>(IBM/IBN) | Large Language Models<br>(LLMs)/Bayesian Belief<br>Networks | Translation of high-level<br>objectives into low-level optical<br>and virtual network<br>configurations.           |
| Security and Resilience     | Intrusion or attack detection<br>(DDoS, tampering)        | Unsupervised Learning<br>(Clustering)                       | Identification of anomalous<br>patterns in traffic or telemetry<br>that indicate threats or<br>systemic failures.  |
| Design and Simulation       | Modelling complex<br>environments and AI training         | Digital Twins/Generative AI                                 | Simulation of ultra-dense<br>environments (e.g., SDM, HCF) to<br>validate and train robust, accurate<br>AI models. |

<span id="page-18-0"></span>![](_page_18_Figure_3.jpeg)

**Figure 2.** AI-Driven Autonomous Management Loop (Closed-Loop Automation).

#### *4.3. Second- and Third-Order Perspectives: AI as Master Orchestrator and Critical Challenge*

The integration of AI/ML into 6G optical network management has implications that extend far beyond simple automation.

First, AI/ML emerges not merely as an optimisation tool but as a fundamental and indispensable enabler for managing the unprecedented complexity introduced by x-Haul convergence, functional split flexibility, distributed edge computing, technological heterogeneity, and the massive scale of 6G optical networks. The combination of FFS, Edge Computing, x-Haul convergence, new technologies such as SDM, HCF, and CPON, along with highly diverse and dynamic service requirements, creates a rapidly evolving multidimensional state and decision space [\[23\]](#page-27-22). Traditional manual or algorithmic management methods simply cannot scale or react with the agility and precision required in this environment [\[43\]](#page-28-17). The intrinsic ability of AI/ML to learn complex patterns from massive datasets, predict future states, and make optimal decisions in real time—particularly through techniques such as RL and MAS [\[24\]](#page-27-23)—becomes essential for dynamic resource orchestration, adaptive QoS assurance, and the autonomous operation (IBN, ZSM) required by 6G [\[46\]](#page-28-20). Without AI, efficient and autonomous management of these networks would be practically unfeasible.

Second, the implementation of AI/ML itself represents a double-edged sword. While it is critical for management, it also introduces new challenges and demands on the optical *Computation* **2025**, *13*, 286 19 of 29

network itself. AI/ML models require vast amounts of high-quality, low-latency telemetry data extracted from the optical network for both training and inference [\[44\]](#page-28-18). Therefore, the optical network must be designed not only to be managed by AI but also to efficiently transport the data required by AI towards computing nodes (at the edge or in the cloud) where the models reside [\[47\]](#page-28-21).

Moreover, the execution of these AI models—both for inference and distributed training, as in Federated Learning—consumes significant computing and storage resources at the edge, which must be provisioned, managed, and orchestrated jointly with optical communication resources [\[48\]](#page-28-22). Finally, to ensure interoperability and avoid ecosystem fragmentation, it is essential to develop and standardise AI-related interfaces and functions within the network architecture—such as the Network Data Analytics Function (NWDAF) defined by 3GPP and its extensions, or the AI interfaces defined in O-RAN for the RAN Intelligent Controllers (RICs).

This includes the standardisation of data collection, AI model lifecycle management (training, deployment, monitoring, retraining), and the exposure of AI capabilities as a service [\[46\]](#page-28-20). The need to support AI both as a workload and as a management component adds yet another layer of complexity to the design and operation of 6G optical networks.

The implementation of AI in the management of 6G optical networks presents significant challenges that require a critical perspective.

- 1. Scarcity of High-Fidelity Data and Dependence on Digital Twins: For AI models to be accurate, they require massive amounts of high-quality telemetry data obtained from the optical network. However, acquiring such data from operational optical networks in real time—especially for rare faults or anomalous phenomena—is difficult. Digital Twins are therefore essential. These virtual models allow the simulation of extreme scenarios (e.g., failures in HCF or SDM) and the generation of the massive and realistic datasets needed to train and test AI/ML algorithms, minimising the risk of errors during real-world deployment.
- 2. Interpretability and Trustworthiness: Autonomous systems must be trustworthy. The lack of transparency in AI model decisions (the "black-box" problem) poses a significant operational risk. An erroneous or poorly trained optimisation decision could propagate rapidly across an autonomous, ultra-fast optical network, causing cascading systemic failures. The development of Explainable AI (XAI) techniques is therefore required to enable operators to audit and trust autonomous management actions.
- 3. Risks of Incorrect Autonomous Configuration: Automation eliminates human error but introduces the possibility of algorithmic errors. Since a failure in the optical network may impact an enormous volume of services (up to 100 Tbit/s), the network must be designed for self-healing. This means that AI must be capable of detecting even the slightest irregularities (early signs of fault) and triggering automatic corrective actions (such as rerouting communications to new paths) with extremely low latency, preventing systemic failures without manual intervention.

# <span id="page-19-0"></span>**5. Precision Synchronisation in 6G Optical Networks**

Precise temporal synchronisation is a fundamental—though often underestimated —requirement for the correct and efficient operation of 6G networks.

# *5.1. Strict Synchronisation Requirements*

6G networks demand unprecedented levels of time and phase synchronisation, achieving accuracies within the nanosecond range [\[8\]](#page-27-7). This precision is indispensable for enabling many of the advanced functionalities of the 6G Radio Access Network (RAN), such as:

*Computation* **2025**, *13*, 286 20 of 29

## 5.1.1. Coordinated Multi-Point Transmission/Reception (CoMP)

In CoMP, multiple cells or access points collaborate to transmit or receive user signals, requiring highly accurate phase alignment.

#### 5.1.2. Coordinated Massive MIMO and High-Precision Beamforming

To efficiently direct radio-frequency energy and minimise interference, fine synchronisation between multiple antennas and radio units is essential.

# 5.1.3. Advanced Carrier Aggregation (CA)

The combination of multiple frequency bands requires precise timing alignment.

#### 5.1.4. URLLC/HRLLC Applications

Services such as real-time industrial control, advanced automation, or telesurgery depend on deterministic and ultra-low latency, which in turn requires an extremely accurate temporal base for resource scheduling and signal processing [\[49\]](#page-28-23). Round-trip latency requirements below 100 µs for motion control imply the need for extremely tight synchronisation [\[49\]](#page-28-23).

#### 5.1.5. Integrated Sensing and Communication (ISAC)

Sensing functions that utilise the communication infrastructure may require precise synchronisation to perform accurate distance, velocity, or angle measurements [\[13\]](#page-27-12). Synchronisation is regarded as a dedicated functional plane within architectures such as O-RAN (S-Plane), underscoring its critical importance [\[8\]](#page-27-7).

#### *5.2. Protocols and Techniques: PTP over Fibre*

The de facto standard protocol for achieving the high-precision synchronisation required in packet-based networks—including optical transport—is the Precision Time Protocol (PTP).

# 5.2.1. PTP (IEEE 1588)

PTP is a protocol specifically designed for high-accuracy clock synchronisation in distributed systems over packet networks [\[45\]](#page-28-19). It is capable of achieving sub-microsecond and even nanosecond-level precision, particularly when implemented over optical fibre networks due to their low latency and high stability [\[50\]](#page-28-24).

# 5.2.2. Hierarchical Architecture

PTP operates under a hierarchical master–slave architecture. A high-precision clock, the Grandmaster Clock (GMC), acts as the primary time reference for a PTP domain. Time is distributed from the GMC through a hierarchy of Boundary Clocks (BCs), which synchronise network segments, to Ordinary Clocks (OCs) or slave clocks in end devices (e.g., RUs, DUs) [\[50\]](#page-28-24). Transparent Clocks (TCs) can compensate for delay introduced as messages traverse network equipment [\[50\]](#page-28-24).

#### 5.2.3. Key Mechanisms

PTP achieves high precision through the following mechanisms:

- Precise Timestamping: Accurate time-stamping of PTP messages (Sync, Delay\_Req, etc.) at the exact moment of transmission and reception at network interfaces. Hardwarebased timestamping is preferred to achieve maximum precision [\[8\]](#page-27-7).
- Best Master Clock Algorithm (BMCA): A distributed algorithm that automatically selects the best available clock as the master within each network segment, establishing the synchronisation hierarchy and preventing loops [\[50\]](#page-28-24).

*Computation* **2025**, *13*, 286 21 of 29

• Delay Measurement: Mechanisms to measure and compensate for the propagation delay of PTP messages across the network, using either End-to-End or Peer-to-Peer methods [\[50\]](#page-28-24).

#### 5.2.4. ITU-T Profiles for Telecommunications

The ITU-T has defined specific PTP profiles (G.827x series) that set stringent requirements for the performance of telecommunication clocks (T-BC, T-TSC) and the maximum allowable time error accumulated across the transport network, thereby ensuring the synchronisation quality required for mobile applications [\[8\]](#page-27-7).

#### 5.2.5. Implementation over Optical Fibre

Optical fibre is the ideal medium for carrying PTP signals with high precision due to its inherently low latency, low jitter, and high stability [\[8\]](#page-27-7). To maintain nanosecond-level accuracy, it is crucial to minimise packet delay variation (PDV) within the optical network and properly configure PTP parameters, such as high message exchange rates [\[8\]](#page-27-7).

## *5.3. Second- and Third-Order Perspectives: Synchronisation as a Critical Service*

The requirement for nanosecond-level synchronisation in 6G reveals its fundamental role and the associated challenges within convergent networks.

First, nanosecond-precision synchronisation should not be regarded as an isolated objective but rather as a critical and often "hidden" enabler underlying many of the advanced capabilities that define 6G. Functionalities such as URLLC/HRLLC, advanced RAN coordination (CoMP, coordinated mMIMO), and Integrated Sensing and Communication (ISAC) intrinsically depend on a common and extremely precise temporal reference [\[49\]](#page-28-23). Any failure or degradation in synchronisation quality—even by a few nanoseconds—could directly impact the performance of these key functions, compromising the viability of the most demanding 6G services.

For instance, coordinated beamforming requires that signals from multiple RUs arrive at the user in perfect phase alignment, necessitating very fine temporal synchronisation among those RUs [\[8\]](#page-27-7). URLLC applications, with microsecond-level latency targets, require precise timing for radio resource allocation and signal processing within very short time windows [\[49\]](#page-28-23). Therefore, the 6G optical transport network must be explicitly designed to carry PTP synchronisation signals with minimal degradation (low PDV). In addition, optical network equipment (switches, routers, ROADMs) must be PTP-compliant—operating as high-precision Boundary Clocks (BCs) or Transparent Clocks (TCs)—to preserve and regenerate timing signal quality across the entire x-Haul chain [\[50\]](#page-28-24).

Second, ensuring and maintaining nanosecond-level, end-to-end synchronisation across convergent and heterogeneous 6G networks—integrating optical fibre, FSO, satellite links, and non-3GPP networks such as Wi-Fi—represents a major technical and management challenge. PTP was originally designed with wired Ethernet networks in mind [\[50\]](#page-28-24). Extending its nanosecond precision across wireless links (such as FSO or satellite), which inherently exhibit greater latency variability and jitter, is complex and requires advanced compensation techniques [\[8\]](#page-27-7).

The coexistence of different PTP profiles (e.g., the telecom G.827x profile, the TSN industrial profile) and the need to synchronise diverse technological domains (3GPP RAN, Core, Edge Computing, industrial OT networks) within a single physical infrastructure demand careful synchronisation architecture planning, meticulous clock configuration, and continuous performance monitoring of the synchronisation chain. The standardisation of robust PTP profiles for such convergent scenarios and ensuring interoperability between equipment from different vendors are therefore crucial for successful synchronisation in 6G [\[49\]](#page-28-23).

*Computation* **2025**, *13*, 286 22 of 29

# <span id="page-22-0"></span>**6. Implementation and Standardisation Challenges**

The transition towards a 6G-ready optical infrastructure, although technologically promising, faces significant practical challenges in terms of cost, complexity, energy consumption, and the need for global standardisation and interoperability.

#### *6.1. Cost and Complexity Analysis*

Upgrading optical infrastructure to meet 6G requirements entails significant investment and increased operational complexity.

#### 6.1.1. Infrastructure Investment

Deployment requires substantial investments in:

- New Fibres: Potential deployment of advanced fibres such as HCF or MCF/FMF in critical network segments, although their manufacturing and deployment costs remain high [\[40\]](#page-28-14).
- Equipment Upgrades: Replacement or modernisation of optical transceivers (towards high-speed coherent types), ROADMs (more flexible and faster, deployed closer to the edge), and Ethernet switches (with TSN and high-precision PTP support) [\[50\]](#page-28-24).
- Network Densification: Increasing the number of cell sites and optical access points to improve coverage and capacity, particularly when operating at higher frequencies [\[40\]](#page-28-14).
- Technological and Operational Complexity: The integration of multiple novel technologies (CPON, SDM, HCF, FSO, PICs, AI/ML, SDN/NFV) into a cohesive network significantly increases design, implementation, management, and maintenance complexity [\[40\]](#page-28-14). Highly skilled personnel are required to operate and optimise such advanced networks [\[40\]](#page-28-14). Managing heterogeneous and distributed networks, with virtualised functions and software-defined control, introduces new operational challenges.
- Cost Mitigation Strategies: To make the transition viable, various strategies are being explored:
- 1. Reusing 5G Infrastructure: Maximising the use of existing fibre and cell site infrastructure [\[40\]](#page-28-14).
- 2. Adopting Open RAN: Encouraging vendor competition and the use of COTS (Commercial Off-The-Shelf) hardware to reduce equipment costs [\[40\]](#page-28-14).
- 3. Infrastructure Sharing: Collaborative models where multiple operators share passive (fibre, towers) or even active network elements to reduce CapEx and OpEx [\[40\]](#page-28-14).
- 4. Virtualisation and Automation: NFV and SDN, combined with AI-driven automation, can reduce long-term operational costs by optimising resource usage and simplifying management [\[40\]](#page-28-14).

#### 6.1.2. Energy Consumption and Sustainability

Sustainability is an integral design requirement for 6G, measured not only by technical performance but also by Key Value Indicators (KVIs), including energy efficiency. Despite the goal of achieving a 100-fold improvement in energy efficiency per bit, the exponential growth of traffic and the energy consumption of Edge AI could increase the total net power consumption of the network.

• Quantitative Optical Savings: The adoption of fully optical networks (minimising O-E-O conversions) is the most effective strategy to mitigate the rise in energy consumption. Analyses show that optical networks can reduce greenhouse gas (GHG) emissions by up to 88% per gigabit compared with legacy networks. Technologies such as lowpower PICs and the use of optical bypass through ROADMs are fundamental for minimising energy consumption at the physical layer.

*Computation* **2025**, *13*, 286 23 of 29

• Intelligent Management: The use of AI/ML and SDN to dynamically optimise configuration and energy consumption (e.g., sleep modes in transceivers during low-traffic periods) is essential for efficient and sustainable energy management.

- Energy Challenge: Although 6G aspires to achieve significantly higher energy efficiency per bit transmitted (a key KPI), the expected exponential growth in data traffic, massive proliferation of connected devices, and the energy required for new functionalities (edge computing, AI model training and inference) could lead to a net increase in total network energy consumption [\[9\]](#page-27-8). This poses both economic (operational cost) and environmental (carbon footprint) challenges. Equipment lifecycle issues including manufacturing and electronic waste (e-waste)—also raise sustainability concerns [\[9\]](#page-27-8).
- Solutions for Energy-Efficient Optical Networks: Research and implementation efforts are underway to develop a wide range of approaches aimed at improving the energy efficiency of the 6G optical infrastructure.
- Low-Power Components: Development and adoption of inherently more efficient optical components, such as silicon photonics-based PICs, integrating multiple functions on a single chip to reduce losses and power use [\[35\]](#page-28-9).
- Energy-Efficient Optical Transceivers: Design of high-speed (Tbps) transceivers that minimise energy consumption per transmitted bit [\[19\]](#page-27-18).
- Optimised Optical Architectures: Network architectures designed to minimise unnecessary O–E–O conversions, favouring direct optical switching (optical bypass) and eliminating intermediate layers (e.g., IP-over-optical flattening) to reduce overall energy consumption [\[19\]](#page-27-18).
- Low-Power Modes: Implementation of sleep or low-power modes for network components (transceivers, amplifiers, switches) during low-traffic periods [\[51\]](#page-29-0).
- Intelligent Energy Management: Use of AI/ML and SDN to monitor energy consumption in real time and dynamically optimise network configurations (e.g., selectively powering down elements, routing traffic through efficient paths) to minimise energy expenditure without compromising QoS [\[9\]](#page-27-8).
- Renewable Energy Sources: Powering network nodes and data centres with renewable energy [\[9\]](#page-27-8).

#### 6.1.3. Security, Resilience, and Interoperability in Open Architectures

The disaggregation and multi-vendor dependence inherent to the 6G open architecture (O-RAN) expand the attack surface and complicate security.

- Zero Trust and Resilience: To ensure the availability of essential services and protect network integrity, it is indispensable to migrate to a Zero Trust security model. This model requires continuous verification of the identity and health of every user, device, and optical or virtualised service, mitigating the risks introduced by a complex supply chain.
- Interoperability as a Pillar of Resilience: Global standardisation is not only crucial for economic viability and economies of scale, but also a pillar of systemic resilience. A coherent set of global standards ensures interoperability among equipment from different vendors, enabling rapid component replacement and preventing systemic failures caused by reliance on a single supplier—an essential requirement for achieving 7- to 9-nines network reliability. Effective collaboration and alignment among standardisation bodies (ITU-T, IEEE, 3GPP, O-RAN) are therefore critical.

The global nature and technological complexity of 6G make standardisation and interoperability absolutely crucial to its success.

*Computation* **2025**, *13*, 286 24 of 29

• Critical Need: To create a vibrant global market, foster competition, reduce costs through economies of scale, and ensure a seamless user experience (including international roaming), it is essential that equipment and solutions from different vendors interoperate smoothly. Global harmonised standardisation of interfaces, protocols, and architectures is the key to achieving such interoperability [\[34\]](#page-28-8).

- Key Standardisation Bodies (SDOs): Several international organisations play fundamental and often complementary roles in defining 6G standards, including those relevant to optical transport:
- 1. ITU-R (International Telecommunication Union—Radiocommunication Sector): Leads the global vision for IMT-2030 (6G), defining use scenarios, performance requirements, and evaluation criteria for radio interface technologies [\[34\]](#page-28-8).
- 2. ITU-T (Telecommunication Standardisation Sector): Focuses on the standardisation of fixed networks, including optical transport (OTN), access networks (PON—Study Group 15, SG15), Ethernet, synchronisation (G.827x), and network management and control (e.g., YANG models) [\[11\]](#page-27-10).
- 3. IEEE (Institute of Electrical and Electronics Engineers): Develops fundamental standards for networking technologies such as Ethernet (IEEE 802.3), local wireless networks (Wi-Fi, IEEE 802.11), Time-Sensitive Networking (TSN, within IEEE 802.1), and PTP (IEEE 1588). It also defines high-speed optical interfaces (e.g., 800G, 1.6T) [\[44\]](#page-28-18).
- 4. 3GPP (3rd Generation Partnership Project): The main body responsible for the standardisation of mobile cellular systems (RAN and Core Network). Defines architectures, interfaces (including eCPRI for fronthaul), protocols, and functionalities, including AI/ML integration (e.g., NWDAF). Releases 20 and 21 will mark the beginning of specific normative work for 6G [\[13\]](#page-27-12).
- 5. O-RAN Alliance: Focuses on defining open and disaggregated RAN interfaces to promote multi-vendor interoperability and AI-driven intelligence through RAN Intelligent Controllers (RICs) [\[52\]](#page-29-1).
- 6. ETSI (European Telecommunications Standards Institute): Plays a key role in transposing 3GPP standards into European norms and works in complementary areas such as MEC, NFV, ZSM (Zero-Touch Service Management), and SDN controllers such as TeraFlowSDN [\[42\]](#page-28-16).
- 7. Other Forums and Alliances: Organisations such as OIF (Optical Internetworking Forum), CableLabs, and MOPA (Mobile Optical Pluggable Alliance) also contribute to the standardisation of specific optical interfaces and components [\[17\]](#page-27-16).
- Inter-Organisational Coordination: Given the convergence of fixed and mobile, wired and wireless, and communication and computing technologies in 6G, effective collaboration and alignment among these various standardisation bodies are more crucial than ever to avoid fragmentation and to ensure a coherent and globally harmonised standards framework [\[53\]](#page-29-2).

#### 6.1.4. Second- and Third-Order Perspectives: The 6G Ecosystem

Implementation and standardisation challenges reflect the complexity of the ecosystem required to realise 6G and the growing emphasis on sustainability.

First, achieving 6G is not merely a technical challenge for individual network operators but a complex and multifaceted ecosystem challenge. It involves an intricate network of interdependent actors: network equipment manufacturers, optical component and semiconductor suppliers (developing PICs, HCF, DSP chips, etc.), cloud service providers (supporting the Cloud–Edge continuum), software and AI algorithm developers, the various standardisation bodies that must coordinate efforts, and government regulators managing spectrum and policy frameworks [\[53\]](#page-29-2).

*Computation* **2025**, *13*, 286 25 of 29

No single entity possesses all the pieces of the 6G puzzle. Operators depend on manufacturers [\[53\]](#page-29-2), who in turn rely on the component supply chain [\[35\]](#page-28-9). AI and cloud integration demand close collaboration with technology giants [\[23\]](#page-27-22). Global standardisation requires difficult consensus among multiple SDOs with sometimes divergent interests [\[40\]](#page-28-14). Spectrum policies are critical enablers [\[45\]](#page-28-19). Therefore, the success and pace of 6G implementation will fundamentally depend on the ability of this complex ecosystem to collaborate effectively, align visions, overcome shared technical and economic barriers, and establish truly open and interoperable standards [\[34\]](#page-28-8). Lack of coordination or fragmentation in any of these areas could significantly delay the fulfilment of the 6G promise.

Second, sustainability—environmental, economic, and social—is emerging as an integral and fundamental design requirement for 6G, not as a secondary consideration or an afterthought. The increasing energy consumption of communication networks is a global concern, both for its environmental impact (carbon footprint) and for its operational costs [\[9\]](#page-27-8). The need for massive infrastructure deployments and constant technological upgrades raises issues of investment cost and electronic waste (e-waste) management [\[9\]](#page-27-8).

Moreover, ensuring that the benefits of 6G are accessible and affordable to all bridging the digital divide—is a key social consideration [\[3\]](#page-27-2). Consequently, decisions regarding which optical technologies to implement (e.g., prioritising the energy efficiency of PICs [\[35\]](#page-28-9) or evaluating the full lifecycle of HCF [\[33\]](#page-28-7)), how to design network architectures (e.g., promoting infrastructure sharing [\[40\]](#page-28-14) or adopting circular economy principles), and how to operate the network (e.g., optimising energy consumption through AI [\[9\]](#page-27-8)) will increasingly be influenced by sustainability criteria that complement traditional technical performance KPIs [\[11\]](#page-27-10).

The long-term viability of 6G will therefore depend on its ability to be not only powerful but also sustainable.

# <span id="page-25-0"></span>**7. Conclusions and Recommendations**

# *7.1. Summary of Key Findings*

6G imposes an extreme convergence in Tbps throughput, microsecond-level latency, and nanosecond synchronisation—capabilities that require optical transport to evolve from a passive conduit into an actively managed communication–computing platform. This platform must be a convergent and flexible x-Haul system, integrated with Edge Computing to support real-time services.

The technical solution lies in the synergistic integration of advanced optical technologies. HCF delivers the lowest physical latency, SDM provides massive core capacity, CPON scales access, and PICs enable efficient, compact transceivers for the edge. The orchestration and management of this complexity are infeasible without an AI-Native approach, in which Artificial Intelligence becomes the indispensable engine for dynamic resource optimisation and autonomous operation (ZSM, IBN). However, the adoption of AI introduces critical challenges in reliability, model interpretability, and data management, making extensive use of Digital Twin platforms necessary for simulation and training.

Overcoming the challenges of high cost and complexity requires a cross-cutting focus on sustainability (KVIs) and global collaboration to establish open standards and security frameworks (Zero Trust) that guarantee interoperability and systemic resilience.

#### *7.2. Strategic Recommendations*

To navigate the transition towards 6G optical infrastructure successfully and sustainably, the following strategic priorities are established:

*Computation* **2025**, *13*, 286 26 of 29

#### 7.2.1. Prioritise Investment in Technology Maturation and Cost Reduction

• HCF and PICs: R&D efforts should focus on reducing the manufacturing costs of HCF for deployment in latency-critical links, and on the standardisation of highperformance, low-power PICs/CPO.

• Optical Spectrum: Investment is essential in the development of amplifiers and components compatible with the new optical bands (O, E, S, and U) to unlock the full capacity of fibre.

# 7.2.2. Coordinated Standardisation Roadmap

- ITU-T SG15: Accelerate the standardisation of advanced fibre management protocols (SDM, HCF) and, crucially, ultra-high-speed CPON standards to ensure interoperability of access hardware.
- O-RAN Alliance/3GPP: Harmonise high-precision PTP profiles (G.827x) to guarantee nanosecond-level synchronisation across flexible fronthaul architectures (FFS).

#### 7.2.3. Adoption of Trust Architectures and Digital Twins

- Implement the Zero Trust security model across the entire transport and management chain to ensure network integrity in complex multi-vendor environments.
- Mandate the use of Digital Twin platforms for the design, simulation, and rigorous validation of AI-assisted network configurations before live deployment, minimising the risk of autonomous failures.

#### 7.2.4. Focus on TCO and Sustainability

- Ensure that Energy Efficiency KVIs become mandatory selection criteria for new optical hardware.
- Promote regulatory policies that incentivise active infrastructure sharing (fibre, ducts, COTS) and AI-driven automation as key strategies for reducing CapEx, OpEx, and environmental impact.

Addressing these challenges and following these recommendations will be essential to unlocking the full transformative potential of 6G—ensuring that optical fibre infrastructure becomes not a bottleneck but a key enabler for the next era of intelligent and ubiquitous connectivity.

**Author Contributions:** Conceptualization, E.A.H. and H.F.B.-O.; methodology, E.A.H.; software, E.A.H.; validation, E.A.H., H.F.B.-O. and J.A.A.-G.; formal analysis, H.F.B.-O.; investigation, E.A.H. and H.F.B.-O.; resources, J.A.A.-G.; data curation, J.A.A.-G.; writing—original draft preparation, H.F.B.-O.; writing—review and editing, E.A.H. and H.F.B.-O.; visualization, H.F.B.-O.; supervision, J.A.A.-G.; project administration, E.A.H.; funding acquisition, J.A.A.-G. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research received no external funding, and the APC was funded by University of Quindío [100016837].

**Data Availability Statement:** Not applicable. This study is based on publicly available and cited literature; no new data were generated or deposited.

**Acknowledgments:** The authors would like to acknowledge the support of the Telecommunications Research Group (GITUQ) for its contribution to the development and technical discussion of this study.

**Conflicts of Interest:** The authors declare no conflict of interest.

*Computation* **2025**, *13*, 286 27 of 29

# **References**

<span id="page-27-0"></span>1. Fayad, A.; Cinkler, T.; Rak, J. Toward 6G Optical Fronthaul: A Survey on Enabling Technologies and Research Perspectives. *IEEE Commun. Surv. Tutor.* **2024**, *27*, 629–666. [\[CrossRef\]](https://doi.org/10.1109/COMST.2024.3408090)

- <span id="page-27-1"></span>2. Tomkos, I.; Christofidis, C.; Uzunidis, D.; Moschopoulos, K.; Papapavlou, C.; Tranoris, C.; Marom, D.M.; Nazarathy, M.; Munoz, R.; Famelis, P.; et al. The "X-Factor" of 6G Networks: Optical Transport Empowering 6G Innovations. *IT Prof.* **2024**, *26*, 32–39. [\[CrossRef\]](https://doi.org/10.1109/MITP.2024.3358971)
- <span id="page-27-2"></span>3. Siddiky, M.N.A.; Rahman, M.E.; Uzzal, M.S. Beyond 5G: A Comprehensive Exploration of 6G Wireless Communication Technologies. **2024**; *preprint*. [\[CrossRef\]](https://doi.org/10.20944/preprints202405.0715.v1)
- <span id="page-27-3"></span>4. Tataria, H.; Shafi, M.; Molisch, A.F.; Dohler, M.; Sjoland, H.; Tufvesson, F. 6G Wireless Systems: Vision, Requirements, Challenges, Insights, and Opportunities. *Proc. IEEE* **2021**, *109*, 1166–1199. [\[CrossRef\]](https://doi.org/10.1109/JPROC.2021.3061701)
- <span id="page-27-4"></span>5. Wang, C.-X.; You, X.; Gao, X.; Zhu, X.; Li, Z.; Zhang, C.; Wang, H.; Huang, Y.; Chen, Y.; Haas, H.; et al. On the Road to 6G: Visions, Requirements, Key Technologies and Testbeds. *IEEE Commun. Surv. Tutor.* **2023**, *25*, 905–974. [\[CrossRef\]](https://doi.org/10.1109/COMST.2023.3249835)
- <span id="page-27-5"></span>6. Solyman, A.A.A.; Yahya, K. Key Performance Requirement of Future next Wireless Networks (6G). *Bull. Electr. Eng. Inform.* **2021**, *10*, 3249–3255. [\[CrossRef\]](https://doi.org/10.11591/eei.v10i6.3176)
- <span id="page-27-6"></span>7. IEEE SA. How Time-Sensitive Networking Benefits Fronthaul Transport. Available online: [https://standards.ieee.org/beyond](https://standards.ieee.org/beyond-standards/how-time-sensitive-networking-benefits-fronthaul-transport/)[standards/how-time-sensitive-networking-benefits-fronthaul-transport/](https://standards.ieee.org/beyond-standards/how-time-sensitive-networking-benefits-fronthaul-transport/) (accessed on 27 October 2025).
- <span id="page-27-7"></span>8. Nadim, M.; Islam, T.U.; Reddy, S.; Zhang, T.; Meng, Z.; Afzal, R.; Babu, S.; Ahmad, A.; Qiao, D.; Arora, A.; et al. AraSync: Precision Time Synchronization in Rural Wireless Living Lab. In Proceedings of the ACM MobiCom 2024—Proceedings of the 30th International Conference on Mobile Computing and Networking, Washington, DC, USA, 18–22 November 2024; pp. 1898–1905. [\[CrossRef\]](https://doi.org/10.1145/3636534.3697318)
- <span id="page-27-8"></span>9. Ahmadi, H.; Rahmani, M.; Chetty, S.B.; Tsiropoulou, E.E.; Arslan, H.; Debbah, M.; Quek, T. Towards Sustainability in 6G and beyond: Challenges and Opportunities of Open RAN. *arXiv* **2025**, arXiv:2503.08353. [\[CrossRef\]](https://doi.org/10.1109/MCOMSTD.2025.3575488)
- <span id="page-27-9"></span>10. Ericsson. 6G Network Architecture—A Proposal for Early Alignment. Available online: [https://www.ericsson.com/en/reports](https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/6g-network-architecture)[and-papers/ericsson-technology-review/articles/6g-network-architecture](https://www.ericsson.com/en/reports-and-papers/ericsson-technology-review/articles/6g-network-architecture) (accessed on 27 October 2025).
- <span id="page-27-10"></span>11. Ishtiaq, M.; Saeed, N.; Khan, M.A. Edge Computing in the Internet of Things: A 6G Perspective. *IT Prof.* **2024**, *26*, 62–70. [\[CrossRef\]](https://doi.org/10.1109/MITP.2024.3366778)
- <span id="page-27-11"></span>12. Rademacher, G.; Luís, R.S.; Puttnam, B.J. Space-Division Multiplexing for Optical Fiber Communications. *Optica* **2021**, *8*, 1186–1203. [\[CrossRef\]](https://doi.org/10.1364/optica.427631)
- <span id="page-27-12"></span>13. Pennanen, H.; Hänninen, T.; Tervo, O.; Tölli, A.; Latva-aho, M. 6G: The Intelligent Network of Everything—A Comprehensive Vision, Survey, and Tutorial. *IEEE Access* **2024**, *13*, 1319–1421. [\[CrossRef\]](https://doi.org/10.1109/ACCESS.2024.3521579)
- <span id="page-27-13"></span>14. Vaez-Ghaemi, R.; Solutions, V. The Evolution of Fronthaul Networks. 2020. Available online: [https://www.viavisolutions.com/en](https://www.viavisolutions.com/en-us/literature/evolution-fronthaul-networks-white-papers-books-en.pdf)[us/literature/evolution-fronthaul-networks-white-papers-books-en.pdf](https://www.viavisolutions.com/en-us/literature/evolution-fronthaul-networks-white-papers-books-en.pdf) (accessed on 27 October 2025).
- <span id="page-27-15"></span><span id="page-27-14"></span>15. Skogman, V. *Building Efficient Fronthaul Networks Using Packet Technologies*; Ericsson: Stockholm, Sweden, 2020.
- 16. Sizer, T.; Samardzija, D.; Viswanathan, H.; Le, S.T.; Bidkar, S.; Dom, P.; Harstead, E.; Pfeiffer, T. Integrated Solutions for Deployment of 6G Mobile Networks. *J. Light. Technol.* **2022**, *40*, 346–357. [\[CrossRef\]](https://doi.org/10.1109/JLT.2021.3110436)
- <span id="page-27-16"></span>17. MOPA Alliance. MOPA Technical Paper v3.2. 2025. Available online: [https://mopa-alliance.org/wp-content/uploads/2025/03/](https://mopa-alliance.org/wp-content/uploads/2025/03/MOPA_Technical_Paper-v3.2-Final.pdf) [MOPA\\_Technical\\_Paper-v3.2-Final.pdf](https://mopa-alliance.org/wp-content/uploads/2025/03/MOPA_Technical_Paper-v3.2-Final.pdf) (accessed on 3 March 2025).
- <span id="page-27-17"></span>18. Li, P.; Fan, J.; Wu, J. Exploring the Key Technologies and Applications of 6G Wireless Communication Network. *iScience* **2025**, *28*, 112281. [\[CrossRef\]](https://doi.org/10.1016/j.isci.2025.112281)
- <span id="page-27-18"></span>19. Tomkos, I.; Uzunidis, D.; Christofidis, C.; Moschopoulos, K.; Papapavlou, C.; Trantzas, K.; Marom, D.M.; Munoz, R. Challenges and Innovations of Transport Networks to Support 6G Use-Cases. In Proceedings of the 2024 24th International Conference on Transparent Optical Networks (ICTON), Bari, Italy, 14–18 July 2024; pp. 1–4. [\[CrossRef\]](https://doi.org/10.1109/ICTON62926.2024.10647904)
- <span id="page-27-19"></span>20. Cui, Q.; You, X.; Wei, N.; Nan, G.; Zhang, X.; Zhang, J.; Lyu, X.; Ai, M.; Tao, X.; Feng, Z.; et al. Overview of AI and Communication for 6G Network: Fundamentals, Challenges, and Future Research Opportunities. *Sci. China Inf. Sci.* **2024**, *68*, 171301. [\[CrossRef\]](https://doi.org/10.1007/s11432-024-4337-1)
- <span id="page-27-20"></span>21. Reeves, J. El Futuro de Las Redes: Explicación de Ethernet de 400 GbE—Fibermall.Com 2024. Available online: [https://www.fibermall.com/es/blog/400gbe-ethernet.htm?srsltid=AfmBOoq2OBEAAjPkDPA1JUBy35YfSFCTtIzUfPX8](https://www.fibermall.com/es/blog/400gbe-ethernet.htm?srsltid=AfmBOoq2OBEAAjPkDPA1JUBy35YfSFCTtIzUfPX8EHIJ76wkYcUsUFFS) [EHIJ76wkYcUsUFFS](https://www.fibermall.com/es/blog/400gbe-ethernet.htm?srsltid=AfmBOoq2OBEAAjPkDPA1JUBy35YfSFCTtIzUfPX8EHIJ76wkYcUsUFFS) (accessed on 27 October 2025).
- <span id="page-27-21"></span>22. Sanjalawe, Y.; Fraihat, S.; Al-E'mari, S.; Abualhaj, M.; Makhadmeh, S.; Alzubi, E. A Review of 6G and AI Convergence: Enhancing Communication Networks with Artificial Intelligence. *IEEE Open J. Commun. Soc.* **2025**, *6*, 2308–2355. [\[CrossRef\]](https://doi.org/10.1109/OJCOMS.2025.3553302)
- <span id="page-27-22"></span>23. Liu, Z.; Chen, X.; Wu, H.; Wang, Z.; Chen, X.; Niyato, D.; Huang, K. Integrated Sensing and Edge AI: Realizing Intelligent Perception in 6G. 2025. Available online: <http://arxiv.org/abs/2501.06726> (accessed on 3 October 2025).
- <span id="page-27-23"></span>24. Tshakwanda, P.M.; Arzo, S.T.; Devetsikiotis, M. Advancing 6G Network Performance: AI/ML Framework for Proactive Management and Dynamic Optimal Routing. *IEEE Open J. Comput. Soc.* **2024**, *5*, 303–314. [\[CrossRef\]](https://doi.org/10.1109/OJCS.2024.3398540)
- <span id="page-27-24"></span>25. Calix. 50G Passive Optical Networks: What Is It All About? 2025. Available online: [https://www.calix.com/blog/2025/04/](https://www.calix.com/blog/2025/04/passive-optical-networks.html) [passive-optical-networks.html](https://www.calix.com/blog/2025/04/passive-optical-networks.html) (accessed on 27 October 2025).

*Computation* **2025**, *13*, 286 28 of 29

<span id="page-28-0"></span>26. Zhang, D.; Liu, D.; Wu, X.; Nesset, D. Progress of ITU-T Higher Speed Passive Optical Network (50G-PON) Standardization. *J. Opt. Commun. Netw.* **2020**, *12*, D99–D108. [\[CrossRef\]](https://doi.org/10.1364/JOCN.391830)

- <span id="page-28-1"></span>27. Zhang, H.; Jia, Z.; Choutagunta, K.; Campos, L.A. Coherent Passive Optical Network: Applications, Technologies, and Specification Development [Invited Tutorial]. *J. Opt. Commun. Netw.* **2025**, *17*, A71–A86. [\[CrossRef\]](https://doi.org/10.1364/JOCN.535200)
- <span id="page-28-2"></span>28. Chanclou, P.; Suzuki, H.; Wang, J.; Ma, Y.; Boldi, M.R.; Tanaka, K.; Hong, S.; Rodrigues, C.; Neto, L.A.; Ming, J. How Does Passive Optical Network Tackle Radio Access Network Evolution? *J. Opt. Commun. Netw.* **2017**, *9*, 1030–1040. [\[CrossRef\]](https://doi.org/10.1364/JOCN.9.001030)
- <span id="page-28-3"></span>29. 5G Americas. The 6G Upgrade in the 7–8 GHz Spectrum Range. 2024. Available online: [https://www.5gamericas.org/the-6g](https://www.5gamericas.org/the-6g-upgrade-in-the-7-8-ghz-spectrum-range/)[upgrade-in-the-7-8-ghz-spectrum-range/](https://www.5gamericas.org/the-6g-upgrade-in-the-7-8-ghz-spectrum-range/) (accessed on 27 October 2025).
- <span id="page-28-4"></span>30. NTT. World's First Long-Haul Optical Inline-Amplified Transmission over 100 Tbit/s Capacity Using Ultra Long-Wavelength Band Conversion Toward IOWN/6G, Single-Core Optical Fiber Capacity More than Three Times Larger than Current Technology. Available online: <https://group.ntt/en/newsrelease/2024/09/03/240903b.html> (accessed on 27 October 2025).
- <span id="page-28-5"></span>31. Inniss, D. Hollow Core Fiber Gives High Frequency Traders an Edge 2020. Available online: [https://www.laserfocusworld.com/](https://www.laserfocusworld.com/fiber-optics/article/14183435/hollow-core-fiber-gives-high-frequency-traders-an-edge) [fiber-optics/article/14183435/hollow-core-fiber-gives-high-frequency-traders-an-edge](https://www.laserfocusworld.com/fiber-optics/article/14183435/hollow-core-fiber-gives-high-frequency-traders-an-edge) (accessed on 27 October 2025).
- <span id="page-28-6"></span>32. Zhao, X.; Li, Z.; Cheng, Y.; Li, J.; Han, Y. Ultra-Low-Loss Anti-Resonant Hollow-Core Fiber with Nested Concentric Circle Structures. *Results Phys.* **2022**, *43*, 106113. [\[CrossRef\]](https://doi.org/10.1016/j.rinp.2022.106113)
- <span id="page-28-7"></span>33. Topfiberbox. Air-Core Optical Fiber: 6G Network Breakthrough Technology. 2025. Available online: [https://topfiberbox.com/](https://topfiberbox.com/air-core-optical-fiber-6g/?srsltid=AfmBOop0_4wAQ9nE31gt-B8aTzcD7zPY9RZxz_MzlG5gbBxpJEgqQGM2) [air-core-optical-fiber-6g/?srsltid=AfmBOop0\\_4wAQ9nE31gt-B8aTzcD7zPY9RZxz\\_MzlG5gbBxpJEgqQGM2](https://topfiberbox.com/air-core-optical-fiber-6g/?srsltid=AfmBOop0_4wAQ9nE31gt-B8aTzcD7zPY9RZxz_MzlG5gbBxpJEgqQGM2) (accessed on 27 October 2025).
- <span id="page-28-8"></span>34. Fayad, A.; Pelle, I.; Cinkler, T.; Sonkoly, B. Harnessing Free Space Optics for Efficient 6G Fronthaul Networks: Challenges and Opportunities. *Eng. Rep.* **2025**, *7*, e70051. [\[CrossRef\]](https://doi.org/10.1002/eng2.70051)
- <span id="page-28-9"></span>35. Chang, Y.-H. *Silicon Photonics and Photonic Integrated Circuits 2025–2035: Technologies, Market, Forecasts*; IDTechEx: Cambridge, UK, 2025.
- <span id="page-28-10"></span>36. Tao, Y.; Ranaweera, C.; Edirisinghe, S.; Lim, C.; Nirmalathas, A.; Wosinska, L.; Song, T. Reconfigurable Optical Crosshaul Architecture for 6G Radio Access Networks. *J. Opt. Commun. Netw.* **2023**, *15*, 1008–1018. [\[CrossRef\]](https://doi.org/10.1364/JOCN.499140)
- <span id="page-28-11"></span>37. Iovanna, P.; Puleri, M.; Bottari, G.; Cavaliere, F. Intent-Based AI System in Packet-Optical Networks towards 6G [Invited]. *J. Opt. Commun. Netw.* **2024**, *16*, C31–C42. [\[CrossRef\]](https://doi.org/10.1364/JOCN.514890)
- <span id="page-28-12"></span>38. Uzunidis, D.; Moschopoulos, K.; Papapavlou, C.; Paximadis, K.; Marom, D.M.; Nazarathy, M.; Muñoz, R.; Tomkos, I. A Vision of 6th Generation of Fixed Networks (F6G): Challenges and Proposed Directions. *Telecom* **2023**, *4*, 758–815. [\[CrossRef\]](https://doi.org/10.3390/telecom4040035)
- <span id="page-28-13"></span>39. Yi, Y. *The 6G Network Is on the Horizon*; CableLabs: Louisville, KY, USA, 2024.
- <span id="page-28-14"></span>40. Othman, A. Implementing Cost-Effective 6G Networks: Strategies and Considerations. 2025. Available online: [https:](https://www.researchgate.net/publication/389008580_Implementing_Cost-Effective_6G_Networks_Strategies_and_Considerations?channel=doi&linkId=67b015d98311ce680c63a33e&showFulltext=true) [//www.researchgate.net/publication/389008580\\_Implementing\\_Cost-Effective\\_6G\\_Networks\\_Strategies\\_and\\_Considerations?](https://www.researchgate.net/publication/389008580_Implementing_Cost-Effective_6G_Networks_Strategies_and_Considerations?channel=doi&linkId=67b015d98311ce680c63a33e&showFulltext=true) [channel=doi&linkId=67b015d98311ce680c63a33e&showFulltext=true](https://www.researchgate.net/publication/389008580_Implementing_Cost-Effective_6G_Networks_Strategies_and_Considerations?channel=doi&linkId=67b015d98311ce680c63a33e&showFulltext=true) (accessed on 5 October 2025).
- <span id="page-28-15"></span>41. Ranaweera, C.; Lim, C.; Tao, Y.; Edirisinghe, S.; Song, T.; Wosinska, L.; Nirmalathas, A. Design and Deployment of Optical X-Haul for 5G, 6G, and beyond: Progress and Challenges [Invited]. *J. Opt. Commun. Netw.* **2023**, *15*, D56–D66. [\[CrossRef\]](https://doi.org/10.1364/JOCN.492334)
- <span id="page-28-16"></span>42. Tsolkas, D.; Artuñedo Guillen, D.; Gavras, A.; Tranoris, C.; Laki, S.; Skarmeta Gómez, A.; Barraca, J.P.; Makropoulos, G.; Vilalta, R. Network & Service Management Advancements—Key frameworks and Interfaces towards open, Intelligent and reliable 6G networks. *Zenodo* **2025**. [\[CrossRef\]](https://doi.org/10.5281/zenodo.15011613)
- <span id="page-28-17"></span>43. Akbar, M.S.; Hussain, Z.; Ikram, M.; Sheng, Q.Z.; Mukhopadhyay, S. On Challenges of Sixth-Generation (6G) Wireless Networks: A Comprehensive Survey of Requirements, Applications, and Security Issues. *J. Netw. Comput. Appl.* **2025**, *233*, 104040. [\[CrossRef\]](https://doi.org/10.1016/j.jnca.2024.104040)
- <span id="page-28-18"></span>44. Chen, X.; Guo, Z.; Wang, X.; Yang, H.H.; Feng, C.; Han, S.; Wang, X.; Quek, T.Q.S. Toward 6G Native-AI Network: Foundation Model Based Cloud-Edge-End Collaboration Framework. *IEEE Commun. Mag.* **2025**, *63*, 23–30. [\[CrossRef\]](https://doi.org/10.1109/MCOM.001.2400582)
- <span id="page-28-19"></span>45. Daws, R. IMT-2030 Vision: Industry Experts Outline the Path to 6G 2024. Available online: [https://www.telecomstechnews.com/](https://www.telecomstechnews.com/news/imt-2030-vision-industry-experts-outline-path-to-6g/) [news/imt-2030-vision-industry-experts-outline-path-to-6g/](https://www.telecomstechnews.com/news/imt-2030-vision-industry-experts-outline-path-to-6g/) (accessed on 27 October 2025).
- <span id="page-28-20"></span>46. Unlocking the Full Potential of AI-Native 6G through Standards|Nokia.Com 2025. Available online: [https://www.nokia.com/](https://www.nokia.com/6g/unlocking-the-full-potential-of-ai-native-6g-through-standards/) [6g/unlocking-the-full-potential-of-ai-native-6g-through-standards/](https://www.nokia.com/6g/unlocking-the-full-potential-of-ai-native-6g-through-standards/) (accessed on 27 October 2025).
- <span id="page-28-21"></span>47. Huawei Technologies Co., Ltd. Data-Plane Design for AI-Native 6G Networks. 2024. Available online: [https://www.huawei.](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) [com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks](https://www.huawei.com/en/huaweitech/future-technologies/data-plane-design-ai-native-6g-networks) (accessed on 10 October 2025).
- <span id="page-28-22"></span>48. Letaief, K.B.; Shi, Y.; Lu, J.; Lu, J. Edge Artificial Intelligence for 6G: Vision, Enabling Technologies, and Applications. *IEEE J. Sel. Areas Commun.* **2022**, *40*, 5–36. [\[CrossRef\]](https://doi.org/10.1109/JSAC.2021.3126076)
- <span id="page-28-23"></span>49. Tao, T.; Wang, Y.; Li, D.; Wan, Y.; Baracca, P.; Wang, A. 6G Hyper Reliable and Low-Latency Communication—Requirement Analysis and Proof of Concept. In Proceedings of the 2023 IEEE 98th Vehicular Technology Conference (VTC2023-Fall), Hong Kong, China, 10–13 October 2023. [\[CrossRef\]](https://doi.org/10.1109/VTC2023-FALL60731.2023.10333792)
- <span id="page-28-24"></span>50. Girela-López, F.; López-Jiménez, J.; Jiménez-López, M.; Rodríguez, R.; Ros, E.; Díaz, J. IEEE 1588 High Accuracy Default Profile: Applications and Challenges. *IEEE Access* **2020**, *8*, 45211–45220. [\[CrossRef\]](https://doi.org/10.1109/ACCESS.2020.2978337)

*Computation* **2025**, *13*, 286 29 of 29

<span id="page-29-0"></span>51. IOWN Global Forum. Open All-Photonic Network Functional Architecture October 2023. 2023. Available online: [https://iowngf.org/wp-content/uploads/2025/02/IOWN-GF-RD-Open\\_APN\\_Functional\\_Architecture-2.0.pdf](https://iowngf.org/wp-content/uploads/2025/02/IOWN-GF-RD-Open_APN_Functional_Architecture-2.0.pdf) (accessed on 27 October 2025).

- <span id="page-29-1"></span>52. Bhattacharjee, S.; Schmidt, R.; Katsalis, K.; Chang, C.Y.; Bauschert, T.; Nikaein, N. Time-Sensitive Networking for 5G Fronthaul Networks. In Proceedings of the ICC 2020—2020 IEEE International Conference on Communications (ICC), Dublin, Ireland, 7–11 June 2020. [\[CrossRef\]](https://doi.org/10.1109/ICC40277.2020.9149161)
- <span id="page-29-2"></span>53. IEEE 802 LAN/MAN Standards Committee. July 2024 Plenary Session—Montreal, QC, Canada. 2024. Available online: <https://1.ieee802.org/july-2024-plenary-session-in-montreal-qc-canada/> (accessed on 20 October 2025).

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
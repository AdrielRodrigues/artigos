---
title: "Review on 6G communication and its architecture, technologies included, challenges, security challenges and requirements, applications, with respect to AI domain"
tema_principal: 5g6g
temas_relacionados: []
ano: 2024
autores: []
veiculo: null
pdf: ../pdf/review_on_6g_communication_and_its_architecture_technologies_included_challenges_security_challenges_and_requirements_applications_with_respect_to_ai_domain.pdf
---

DOI: [10.1049/qtc2.12114](https://doi.org/10.1049/qtc2.12114)

#### **REVIEW**

![](_page_0_Picture_6.jpeg)

# **Review on 6G communication and its architecture, technologies included, challenges, security challenges and requirements, applications, with respect to AI domain**

**Pranita Bhide<sup>1</sup>** | **Dhanush Shetty<sup>1</sup>** | **Suresh Mikkili<sup>2</sup>**

#### **Correspondence**

Suresh Mikkili, Department of Electrical and Electronics Engineering, National Institute of Technology Goa, Room No. 45, Second Floor, Abdul Kalam Complex, Kottamoll Plateau, Cuncolim Municipal Area, Salcete Taluka, South Goa District, Cuncolim, Goa 403703, India. Email: [mikkili.suresh@nitgoa.ac.in](mailto:mikkili.suresh@nitgoa.ac.in)

#### **Funding information**

Science and Engineering Research Board, Grant/ Award Number: EEQ/2021/294

#### **Abstract**

The evolution of wireless communication systems has led to the emergence of the sixth generation (6G) communication architecture, characterised by transformative technologies and novel paradigms that transcend the capabilities of its predecessors. This paper presents an overview of the various aspects of 6G communication architecture, focusing on its technologies, challenges, and applications within the domain of artificial intelligence (AI). The abstract provides an overview of a review on 6G communication, focusing on its architecture, technologies, challenges, security concerns, and requirements within the context of the AI domain. The paper explores the evolving landscape of wireless communication, delving into the anticipated features and capabilities of 6G networks. The architecture emphasises the integration of AI‐driven elements, such as intelligent resource allocation and autonomous network management. Various technologies, including terahertz frequencies and integrated satellite networks, are discussed in terms of their potential to reshape connectivity paradigms. However, alongside the promises, a multitude of challenges arise. These encompass spectrum scarcity at terahertz frequencies, energy efficiency concerns, and the need for global standardisation. Addressing security challenges is crucial, considering the expanded attack surface and the integration of AI‐powered functionalities. The paper also delineates the stringent requirements that 6G must fulfil, spanning ultra‐low latency, high bandwidth, massive device connectivity, and reliable communication. Contextualising these discussions, the review highlights applications within the AI domain that stand to benefit from 6G advancements. These include edge AI, augmented reality, autonomous systems, and IoT‐enabled environments. By synergising cutting‐edge wireless capabilities with AI‐driven intelligence, 6G is poised to revolutionise industries and societal experiences in unprecedented ways.

### **KEYW ORDS**

protocols, quantum communication, telecommunication channels, telecommunication security

### **1** | **INTRODUCTION**

6G communication represents [[1–3](#page-21-0)] the next frontier in wireless technology, aiming to enable unprecedented levels of connectivity, data rates, and capabilities.

As artificial intelligence (AI) continues to shape diverse industries, integrating AI with 6G communication architecture opens new avenues for innovation, efficiency, and user experiences [[3](#page-21-0)]. Table [1](#page-1-0) describes the types of 6G communication and its frequency. And Figure [1](#page-1-0) tells us about the mobile network evolution from 1G to 6G.

### **2** | **ARCHITECTURE**

### **2.1** | **6G communication architecture**

The Figure [2](#page-1-0) gives us the view of 6G Architecture ability. Let's discuss about it in detail below.

This is an open access article under the terms of the Creative Commons [Attribution](http://creativecommons.org/licenses/by/4.0/) License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

© 2024 The Author(s). *IET Quantum Communication* published by John Wiley & Sons Ltd on behalf of The Institution of Engineering and Technology.

<sup>1</sup> Department of Electronics and Telecommunication, Don Bosco College of Engineering Goa, Margao, India

Department of Electrical and Electronics Engineering, National Institute of Technology Goa, Cuncolim, India

### <span id="page-1-0"></span>2.1.1 | 6G architecture in space

*Satellite Constellations*: One potential aspect of 6G architecture in space is the deployment of satellite constellations. These constellations could consist of hundreds or even thousands of small satellites working together to provide global coverage. Each satellite would communicate with user devices on Earth or other spacecraft, forming a complex network that enables seamless communication.

*Inter‐Satellite Communication*: 6G in space might involve highly advanced inter‐satellite communication capabilities,

**TABLE 1** Types of 6G communications and its frequency range.

| Types of 6G communications | Frequency   |
|----------------------------|-------------|
| Base band                  | 7–20 GHz    |
| W‐band                     | 75–110 GHz  |
| D‐band                     | 110–175 GHz |
| 1 Hz band                  | 0.3–101 Hz  |

![](_page_1_Figure_7.jpeg)

**FIGURE 1** Mobile network evolution from 1G to 6G.

allowing satellites to exchange data directly with each other. This could enable efficient relay of information across the satellite network and reduce the need for data to travel through ground stations.

*Orbital Diversity*: Different orbits, such as low Earth orbit (LEO), medium Earth orbit, and geostationary orbit (GEO), could be leveraged to provide a mix of coverage, capacity, and latency for various use cases. LEO satellites can offer low latency but require more satellites for global coverage, while GEO satellites provide wider coverage but with higher latency.

*Advanced Antenna Technologies*: 6G could introduce more advanced antenna technologies, such as phased array antennas, to enable dynamic and adaptive beamforming. This would allow satellites to focus their signals on specific areas or devices, improving signal quality and reducing interference.

*Cross‐Layer Optimisation*: To meet the unique challenges of space environments, cross‐layer optimisation could play a crucial role. This involves coordinating communication protocols, network architecture, and physical layer technologies to ensure efficient and reliable communication.

*Energy Efficiency and Power Management*: Space‐based systems require careful energy management due to limited power sources. 6G architecture would need to incorporate energy‐efficient designs to prolong the operational life of satellites and minimise the need for frequent maintenance.

*Security and Reliability*: Space‐based communication systems would need robust security mechanisms to protect against potential threats. Encryption, authentication, and secure key exchange would be crucial components of the architecture.

![](_page_1_Picture_15.jpeg)

BHIDE ET AL. - **3 of 23**

*Integration with Terrestrial Networks*: Seamless integration between space‐based 6G networks and terrestrial 6G networks would enable uninterrupted communication as devices move between Earth and space coverage areas.

## 2.1.2 | 6G architecture in air

*Ultra‐Fast In‐Flight Connectivity*: 6G could offer even faster and [[4](#page-21-0)] more reliable connectivity for aeroplanes, allowing passengers to enjoy high‐definition streaming, virtual reality (VR) experiences, and real‐time communication during flights.

*Enhanced Aircraft Communications*: 6G's low latency and high bandwidth could lead to more efficient and secure communication between aircraft and air traffic control systems. This could enable quicker decision‐making and more precise air traffic management.

*Remote Pilot Assistance*: With 6G's capabilities, there might be opportunities for remote pilots or experts to assist in real‐time with complex flight situations, providing guidance and support to pilots in the air.

*Advanced Surveillance and Navigation*: [\[5\]](#page-21-0) 6G‐enabled sensors and communication systems could enhance aircraft navigation and surveillance, enabling better tracking and coordination of aircraft even in remote or challenging environments.

*Aircraft‐to‐Aircraft Communication*: 6G could facilitate direct communication between nearby aircraft, enhancing collaborative decision‐making and avoiding collisions in congested airspace.

*Predictive Maintenance*: Advanced sensors connected through 6G could enable real‐time monitoring of aircraft systems and components, allowing for predictive maintenance to prevent unexpected failures and reduce downtime.

*Emergency Response and Search and Rescue*: High‐speed 6G connectivity could improve communication during emergencies, aiding in quicker response times and enhancing coordination in search and rescue operations.

*Cabin Automation and Passenger Services*: 6G might support advanced automation within the aircraft cabin, improving passenger services and optimising cabin operations through real‐time data analysis.

*Secure Communication*: 6G's potential advancements in encryption and security could enhance the protection of critical aviation data and communications.

### 2.1.3 | 6G architecture in land

*Higher Frequencies*: Just as with each new generation of wireless technology, 6G is likely to use higher frequencies to accommodate increased data rates and capacity. This could include the use of millimetre‐wave frequencies and potentially even terahertz frequencies.

*Massive multiple‐input, multiple‐output (MIMO) and Beamforming*: 6G is expected to continue the trend of using massive MIMO antenna arrays and advanced beamforming techniques to improve spectral efficiency, coverage, and capacity.

*Ultra‐Dense Networks*: To support the increasing number of connected devices, 6G might employ ultra‐dense network deployments, where small cells and access points are densely packed in urban areas to provide seamless connectivity.

*AI and Network Intelligence*: AI and machine learning (ML) are likely to play a significant role in 6G networks. AI could be used for dynamic resource allocation, interference management, network optimisation, and predictive maintenance.

*Heterogeneous Network Integration*: 6G networks could integrate various wireless technologies, including traditional cellular networks, Wi‐Fi, satellite communication, and possibly new types of communication paradigms that are currently under exploration.

*Terahertz Communications*: Terahertz frequencies could be explored for extremely high data rates, but they also pose challenges due to higher atmospheric absorption and propagation characteristics.

*Integrated Satellite Communication*: 6G might involve tighter integration with satellite communication systems to provide global coverage, including in remote and rural areas.

*Sustainable and Green Design*: There is an increasing emphasis on designing wireless networks with energy efficiency and environmental sustainability in mind. 6G could incorporate design principles to minimise power consumption and reduce the overall carbon footprint.

*Security and Privacy Enhancements*: Given the growing concerns around cybersecurity and user privacy, 6G networks could have built‐in security features and privacy‐preserving technologies from the ground up.

*New Services and Use Cases*: 6G is expected to support a wide range of new applications, including augmented reality (AR), VR, holographic communication, advanced automation, immersive remote experiences, and more.

### 2.1.4 | 6G architecture in sea and undersea

*Underwater Communication Challenges*: Underwater communication presents unique [[6\]](#page-21-0) challenges due to the high attenuation and absorption of radio frequency (RF) signals in water [\[7\]](#page-21-0). Acoustic communication is commonly used underwater due to its better propagation characteristics in water compared to RF signals [\[8\]](#page-21-0). 6G architecture for underwater environments might involve a combination of acoustic communication, optical communication (using visible or near‐ infrared light), and possibly electromagnetic communication using very low frequencies.

*Acoustic Communication*: Underwater acoustic communication involves sending and receiving signals through sound waves. It can support relatively low data rates but can cover longer distances. 6G architecture might include advanced techniques for encoding, modulation, and error correction to improve data rates and reliability.

<span id="page-3-0"></span>*Optical Communication*: Optical communication using light waves could be explored for higher data rates over shorter distances in clear water. However, optical signals are susceptible to scattering and absorption, which can limit their range and effectiveness.

*Integrated Satellite Communication*: Since underwater environments can be remote and challenging to access, integrating underwater communication with satellite communication could provide a comprehensive solution for connectivity in oceanic regions.

*Sensor Networks and IoT*: Undersea architecture could involve deploying sensor networks for various applications such as environmental monitoring, underwater exploration, disaster prevention, and resource management. These networks could be part of the broader 6G ecosystem, providing real‐time data to users on land.

*Energy Considerations*: Powering underwater communication devices is a significant challenge. 6G architecture for undersea environments might need to incorporate energy harvesting techniques or efficient power sources to ensure sustained operation.

*Latency and Reliability*: Latency and reliability are crucial factors in undersea communication, especially for applications like remote operation of underwater vehicles or monitoring of critical infrastructure. 6G architecture should prioritise low‐ latency and reliable communication.

*Environmental Impact*: The impact of new communication technologies on underwater ecosystems must be considered. Minimising interference with marine life and preserving the underwater environment is essential.

### **3** | **6G TECHNOLOGIES IN AI**

There [\[9](#page-21-0)] are many technologies by 6G in AI domain, here below are listed the 6G Technologies in AI domain. The 6G technologies in AI domain are specified in Figure 3.

Thanks to the advancements of different **AI** technologies, such as tiny AI, multi‐skilled AI, federated AI, collective AI, collaborative AI, and semantic‐oriented AI, the Sixth Generation (6G) mobile systems will develop an intelligent, collaborative, and adaptive network architecture with pervasive AI capabilities existing in 6G systems to address this big challenge.

**Terahertz (THz) Communications**: THz frequency bands offer unprecedented bandwidth, enabling multi‐terabit data rates. AI‐powered beamforming and channel prediction will enhance link reliability.

**Massive MIMO (Multiple Input Multiple Output)**: With thousands of antennas, massive MIMO enhances spectral efficiency. AI algorithms will optimise beamforming and user scheduling.

**Dynamic Spectrum Sharing**: AI will enable efficient allocation of spectrum resources, dynamically adapting to varying demands and environments.

![](_page_3_Figure_14.jpeg)

**FIGUR E 3** 6G technologies in AI domain. AI, artificial intelligence.

**Holographic Beamforming**: Leveraging AI‐generated holograms, this technology enables highly directional and efficient signal transmission.

**Quantum Communication**: Quantum‐enhanced encryption and secure key exchange, supported by AI, ensure next‐ level security for sensitive data.

**Ultra‐Dense Heterogeneous Networks**: Integration of various network types like terrestrial, satellite, and airborne to provide seamless coverage and connectivity.

**Integrated Satellite Communication**: Satellite networks as integral components to provide global coverage and enhance connectivity in remote areas.

**AI‐Driven Beamforming**: AI algorithms optimise beamforming, enhancing signal strength and reliability.

**AI‐Powered Network Orchestration**: Dynamic network management and optimisation using AI to adapt to changing conditions and demands.

**Edge AI**: AI processing at the network edge, reducing latency for real‐time applications.6G will continue to emphasise edge computing, where AI processing occurs closer to data sources, reducing latency and enabling real‐time applications.

**Hyper‐Connectivity and Internet of Things (IoT) Integration**: 6G is expected to further integrate the IoT, enabling massive device connectivity with extremely low latency and high reliability.

**Energy Efficiency Solutions**: Given the increasing energy consumption of advanced wireless technologies, 6G will likely incorporate energy‐efficient designs, such as energy harvesting, AI‐based power management, and sleep modes for idle devices.

**AI‐Enhanced Security**: As 6G becomes integral to critical infrastructure, AI‐driven security mechanisms will be essential to detect and mitigate cyber threats, including zero‐day attacks and network anomalies.

BHIDE ET AL. - **5 of 23**

**High‐Quality Mixed Reality (MR)**: With ultra‐high data rates and low latency, 6G can enhance MR experiences, enabling seamless and immersive interactions in virtual and AR environments. Following Figure [3](#page-3-0) gives us the brief idea about 6G technologies in AI domain in various types.

### **4** | **CHALLENGES**

Figure 4 provides the list of challenges faced by 6G communication with AI. Technologies and Methodologies used under 6G communication are given in Table 2.

**AI‐Integrated Security**: Ensuring the [\[10\]](#page-21-0) security of AI‐ augmented 6G networks against adversarial attacks and vulnerabilities in AI algorithms is a critical challenge.

- � **Energy Efficiency**: Power consumption increases with advanced technologies. AI‐based power management and optimisation are vital to sustainably drive 6G networks [\[11\]](#page-21-0).
- � **Interoperability**: Integrating AI modules across diverse network components requires standardised interfaces and protocols.
- � **Ethical AI**: As AI becomes integral to network decision‐ making, addressing biases, privacy concerns, and ethical considerations in AI algorithms becomes paramount.

![](_page_4_Figure_9.jpeg)

**FIGURE 4** Challenges faced by 6G Communication with AI. AI, artificial intelligence.

**TABLE 2** Technologies and methodologies used under 6G communication.

| Technologies                  | Techniques/Methodology                                                                                                                                                                                                       |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Artificial Neural<br>Network  | > Supervised Learning<br>> Unsupervised Learning<br>> Enhance Learning                                                                                                                                                       |
| Short‐packet<br>communication | Packet communication architecture is the structuring<br>of data processing systems as collections of physical<br>units that communicate only by sending information<br>packets of fixed size, using an asynchronous protocol |
| Mobile edge<br>computing      | The near‐real‐time processing of large amounts of<br>data produced by edge devices and applications<br>closest to where it's captured                                                                                        |

� **Security and Privacy**: Ensuring AI‐augmented 6G networks are resilient against cyber threats and protecting user data.

� **Regulatory and Standardisation**: Establishing regulations and standards for AI‐driven 6G networks to ensure global compatibility.

### **4.1** | **Security challenges in 6G can be categorised into various types**

- � *Privacy Concerns*: With increased data collection and sharing, protecting user privacy becomes crucial to prevent unauthorised access to personal information.
- � *Cyberattacks*: As technology advances, the sophistication of cyberattacks also increases. 6G networks could be susceptible to various types of attacks, including DDoS attacks, ransomware, and zero‐day exploits.
- � *Network Slicing Vulnerabilities*: Network slicing in 6G allows multiple virtual networks to run on a single physical infrastructure. Ensuring the isolation and security of these slices is challenging.
- � *AI‐driven Threats*: The integration of AI in 6G networks can lead to security risks, such as adversarial attacks on AI models or the manipulation of AI‐driven decisions. *IoT Security*: The massive deployment of IoT devices in 6G networks creates more entry points for potential attacks and challenges in securing these devices.
- � *Physical Attacks*: As 6G infrastructure becomes more critical, physical attacks on network components or communication facilities become a concern.
- � *Authentication and Authorisation*: Ensuring secure and reliable authentication and authorisation mechanisms for network access and device communication is a fundamental challenge.
- � *Jamming and Interference*: Preventing signal jamming, interference, or disruption is crucial to maintaining reliable communication in 6G networks.
- � *Supply Chain Risks*: Securing the supply chain against malicious components or compromised devices is essential to prevent vulnerabilities from being introduced during manufacturing or distribution.
- � *Regulatory and Policy Challenges*: Developing consistent and effective regulations and policies to address the security challenges of 6G networks across different jurisdictions is a complex task.
- � *Resilience and Redundancy*: Ensuring the resilience of 6G networks against natural disasters, technical failures, and other disruptions is vital.
- � *User Awareness*: Educating users about security risks and best practices in using 6G networks will be necessary to mitigate potential threats [[12\]](#page-21-0).

These challenges highlight the need for a comprehensive approach to security in 6G networks, addressing technical, operational, and regulatory aspects to ensure a robust and secure communication environment.

### **4.2** | **Security requirements for 6G encompass a range of aspects to ensure a robust and secure communication environment. Some types of 6G security requirements include**

- � *Encryption and Data Protection*: [[13](#page-21-0)] Implementing strong encryption mechanisms to safeguard data during transmission and storage, ensuring confidentiality and integrity.
- � *Authentication and Authorisation*: Establishing reliable methods for verifying the identity of users, devices, and entities accessing the network, along with proper authorisation protocols.
- � *Network Segmentation and Isolation*: Designing the network architecture to allow secure isolation of different segments, preventing unauthorised access between them.
- � *Secure Key Management*: Developing secure methods for generating, distributing, and managing encryption keys to prevent unauthorised access to sensitive information.
- � *Intrusion Detection and Prevention*: Implementing systems to detect and respond to unauthorised access or malicious activities within the network.
- � *Resilience and Redundancy*: Ensuring that the network can withstand disruptions and failures, with redundant systems and failover mechanisms.
- � *Secure Network Slicing*: Establishing security measures to ensure the isolation and protection of various network slices running on the same infrastructure.
- � *AI and ML Security*: Incorporating security measures to protect AI and ML algorithms from adversarial attacks and ensuring their robustness.
- � *IoT Device Security*: Enforcing security measures for IoT devices, including device authentication, secure communication protocols, and regular security updates.
- � *Physical Security*: Protecting network infrastructure from physical attacks, tampering, and unauthorised access.
- � *Privacy‐Preserving Techniques*: Implementing methods to collect and share data while preserving user privacy, such as differential privacy.
- � *Regulatory Compliance*: Adhering to legal and regulatory requirements related to data privacy, security, and communication standards.
- � *User Education*: Educating users about security risks, best practices, and potential threats to promote responsible use of the network.
- � *Supply Chain Security*: Ensuring the security of network components and devices throughout their supply chain, preventing the introduction of vulnerabilities.
- � *Emergency Services and Public Safety*: Implementing security measures to ensure the reliability and availability of emergency services in critical situations.
- � *Secure Updates*: Ensuring that software and firmware updates are securely distributed and applied to prevent vulnerabilities.
- � *Jamming and Interference Protection*: Implementing measures to prevent and mitigate signal jamming and interference.

� *Policy Management*: Establishing effective policies and procedures to govern security practices within the network.

These requirements collectively address the diverse range of security challenges in 6G communication systems, safeguarding against potential threats and ensuring the overall integrity, confidentiality, and availability of the network [\[14\]](#page-21-0).

### **4.3** | **Application layer**

### 4.3.1 | Internet of vehicles (IoV)

As of my last update in September 2021, 6G technology and its specific details may not be fully available. However, I can certainly provide you with a general concept of how the [[15\]](#page-21-0) could be integrated with 6G communication, along with a high‐ level diagram of its potential components. The IoV is an extension of the IoT that focuses on the connectivity and communication between vehicles, infrastructure, and other entities within the transportation ecosystem. In the context of 6G communication, IoV is expected to leverage advanced technologies to enable seamless and highly reliable communication, leading to safer and more efficient transportation systems.

In Figure [8](#page-9-0) we are discussing the IoV diagrammatical components in 6G communication.

#### *Components of IoV in 6G communication*

Here's a high‐level diagram of the potential components involved in integrating the IoV with 6G communication:

- 1. *Vehicle‐to‐Vehicle (V2V) Communication*: Vehicles directly communicate with each other using 6G technology. This communication can enable cooperative collision avoidance, traffic coordination, and information sharing between vehicles.
- 2. *Vehicle‐to‐Infrastructure (V2I) Communication*: Vehicles communicate with roadside infrastructure, such as traffic lights, road signs, and smart roadways. This enables real‐ time data exchange for traffic management, safety warnings, and optimised routing.
- 3. *6G Network Infrastructure*: The backbone of the communication system, 6G infrastructure provides ultra‐ high data rates, low latency, and massive device connectivity. It supports the IoV ecosystem by delivering reliable and efficient communication.
- 4. *Cloud Services*: Cloud‐based services play a crucial role in IoV by providing storage, processing, and analysis of vehicle‐generated data. These services can include real‐time traffic analysis, predictive maintenance, and personalised navigation.
  - Figure [5](#page-6-0) illustrates the Different Layers of 6G Applications in AI [[16](#page-21-0)]
- 5. *Vehicle Sensors and Actuators*: Vehicles are equipped with various sensors (e.g. LiDAR, radar, cameras) to gather information about the surrounding environment. Actuators, such as brakes and steering, respond to control commands.

<span id="page-6-0"></span>BHIDE ET AL. - **7 of 23**

6. *Roadside Infrastructure*: Smart Road infrastructure includes sensors, cameras, and communication equipment embedded along roadways. This infrastructure collects data about road conditions and communicates with vehicles to improve safety and traffic flow.

It's important to note that 6G technology is still in the research and development phase, and its exact features and capabilities may evolve over time. The diagram and components provided here are based on the general concepts of IoV and 6G communication as of September 2021. Please consult

![](_page_6_Picture_4.jpeg)

**FIGURE 5** Different layers of 6G applications in AI. AI, artificial intelligence.

**TABLE 3** Parameters of 5G and 6G and IEEE standards.

more recent sources for the latest information on 6G technology and its integration with the IoV.

As of my last update in September 2021, specific details about the implementation of the IoV within the context of 6G communication are not fully available since 6G technology was still in the early stages of development. However, I can provide you with a general idea of how IoV could potentially be integrated into 6G communication based on the trends and concepts observed in previous generations of wireless communication [\[17](#page-21-0)].

The Parameters of 5G and 6G communication and its IEEE standards are given in Table 3. The solutions to overcome the 6G challenges are given in Table [4](#page-7-0).

#### *Potential integration of IoV in 6G communication*

[[11\]](#page-21-0) 6G is expected to push the boundaries of wireless communication with even higher data rates, ultra‐low latency, massive device connectivity, and new capabilities. In the context of IoV, the integration could involve several key aspects:

1. *Ultra‐Reliable Low‐Latency Communication (URLLC)*: 6G is likely to provide ultra‐reliable and low‐latency communication, which is essential for time‐critical applications in IoV. This can facilitate real‐time vehicle‐to‐ vehicle (V2V) and vehicle‐to‐infrastructure (V2I) communication, enabling rapid response to safety hazards and traffic management.

| Parameters               | 6G                               | 5G                | Standards of IEEE     |
|--------------------------|----------------------------------|-------------------|-----------------------|
| Receiver sensitivity     | <−130 dBm                        | −120 dBm          | IEEE 802.15.4         |
| Reliability              | 99.999% (highly reliable)        | 99.9%             | IEEE 802.11ax‐2021    |
| Fraction of coverage     | 99%                              | 70%               | IEEE 802.15.4‐2020    |
| Connection density       | 10 million/km2                   | 1 million/km2     | IEEE/IEC 63195‐1‐2022 |
| Flow density             | 100 Tb/s/km2                     | 10 Tb/s/km2       | IEEE 3002.2‐2018      |
| Personal data rate       | 100 Gb/s                         | 1 Gb/s            | IEEE 802.15.3e‐2017   |
| DL data rate             | >1 Tb/s                          | 20 Gb/s           | IEEE 802.11‐2020      |
| DL spectrum efficiency   | 100 b/s/Hz                       | 30 b/s/Hz         | IEEE 802.11‐2020      |
| User experience rate     | >10 Gb/s 3D                      | 50 Mb/s 2D        | IEEE 1857.8‐2019      |
| Transmission capacity    | 1–10 Gb/s/m2                     | 10 Mb/s/m2        | IEEE 2847‐2021        |
| Processing delay         | 10 ns                            | 100 ns            | IEEE 1497‐2001        |
| C‐plane latency          | <1 ms                            | 10 ms             | IEEE 802.1AS          |
| U‐plane latency          | <0.1 ms                          | 0.5 ms            | IEEE 802.11ad         |
| Maximum mobility         | 1000 km/h                        | 500 km/h          | IEEE 802.11p          |
| Reliability              | 10_9                             | 10_5              | IEEE 802.11ax‐2021    |
| Spectrum efficiency      | 1000 b/s/Hz/m2                   | 10 b/s/Hz/m2      | IEEE 802.11           |
| Positioning accuracy     | Indoor (10 cm), outdoor (1 m) 3D | Outdoor (10 m) 2D | IEEE 802.11az         |
| Coverage area            | Space, ground (desert), ocean    | Ground            | IEEE 802.15.7         |
| Peak throughput          | 100 Gb/s–1 Tb/s                  | 10 Gb/s           | IEEE 802.11‐2020      |
| Communication time delay | <0.1 ms                          | 1 ms              | IEEE 802.1AS          |

<span id="page-7-0"></span>**TABLE 4** 6G challenges and its solutions to overcome.

| 6G challenges                         | Solutions to overcome                                                                                                                                                                                                                               |  |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| From the possibility to the certainty | To over the problem we use network slicing, MEC and relevant technologies is introduced in 5G<br>to offer the end‐to‐end network services capability guaranteed by SLA (service‐level agreement)                                                    |  |
| Openness and customisation            | To prevent this problem an API interfaces for industrial customers to meet the needs of<br>deploying tailor‐made network and customised applications                                                                                                |  |
| Artificial intelligence network       | It requires massive data and computing resources to exert the value of AI artificial intelligence<br>network engine at the maximum. Therefore, the future artificial intelligence network in 6G era<br>needs the interaction between AI and network |  |

Abbreviation: API, Application Programming Interface.

- 2. *Massive Device Connectivity*: IoV involves a large number of vehicles and infrastructure components. 6G's ability to handle massive device connectivity could enable seamless communication between vehicles, infrastructure, pedestrians, and other road users.
  - Figure 6 illustrates the internal structure of IoV [\[18](#page-21-0)].
- 3. *Millimetre‐Wave Communication*: 6G may utilise millimetre‐wave frequencies for enhanced data rates and capacity. This could support high‐definition sensor data exchange between vehicles and the surrounding environment.
- 4. *Network Slicing*: Network slicing is a concept where a single physical network can be divided into multiple virtual networks optimised for specific use cases. In the context of IoV, network slicing could be employed to allocate resources based on the varying requirements of different vehicular applications, such as safety‐critical messages or infotainment data.
- 5. *Edge Computing*: Edge computing involves processing data closer to the source, reducing latency and enabling faster decision‐making. IoV applications, such as real‐time collision avoidance, could benefit from edge computing capabilities provided by 6G.
- 6. *Security and Privacy*: IoV systems handle sensitive information, and security and privacy are paramount. 6G's advancements in security features could help protect vehicular communication from cyber threats and ensure data privacy.
- 7. *AI and ML*: The integration of AI and ML can enhance IoV systems by enabling predictive analytics, intelligent traffic management, and context‐aware applications. 6G could facilitate the exchange of AI‐processed data for more informed decision‐making.
- 8. *Global Coverage and Roaming*: IoV systems might require cross‐border communication as vehicles move between different regions. 6G's potential global coverage and seamless roaming capabilities could support this requirement.

### 4.3.2 | Internet of medical things

The Internet of Medical Things (IoMT) is an extension of the broader IoT [\[19\]](#page-21-0) concept that specifically focuses on the integration of medical devices, sensors, and healthcare systems

![](_page_7_Picture_15.jpeg)

**FIGUR E 6** Internet of vehicles.

to improve patient care, medical research, and healthcare efficiency. When considering the integration of IoMT with 6G communication, there are several potential enhancements and benefits that could be realised:

- 1. *URLLC*: 6G's URLLC capabilities can be crucial in IoMT applications where real‐time data transmission is essential, such as remote surgeries, patient monitoring, and emergency response. The low latency and high reliability of 6G can ensure that critical medical data is transmitted and received without delay [\[20\]](#page-21-0).
- 2. *High‐Quality Telemedicine and Remote Care*: 6G's higher data rates and improved network performance can facilitate high‐definition video streaming and real‐time communication between patients and healthcare providers. This can lead to more accurate remote diagnoses, virtual consultations, and remote patient monitoring.
- 3. *Massive Device Connectivity*: The IoMT involves a vast number of medical devices, wearables, and sensors. 6G's capacity to handle massive device connectivity ensures that a large ecosystem of medical devices can communicate seamlessly within healthcare environments.
- 4. *Edge Computing for Real‐Time Processing*: 6G's support for edge computing allows medical data to be processed locally, near the source of data generation. This can lead to faster data analysis, reduced latency in diagnosis, and more efficient use of network resources.

BHIDE ET AL. - **9 of 23**

- 5. *Enhanced Wearable and Implantable Devices*: 6G can provide the necessary connectivity and bandwidth to support advanced wearable devices and implantable sensors. These devices can continuously monitor patients' health parameters and transmit data to healthcare professionals in real time.
- 6. *Data Security and Privacy*: Medical data is highly sensitive, and maintaining data security and patient privacy is of paramount importance. 6G can offer advanced security features such as enhanced encryption, authentication protocols, and secure device on boarding.
- 7. *AI‐Driven Healthcare*: The integration of AI and ML with IoMT can lead to more accurate diagnostics, personalised treatment recommendations, and predictive analytics. 6G's capabilities can enable the exchange of large datasets for training and deploying AI models.
- 8. *Telehealth in Remote Areas*: 6G's potential for wider coverage and improved connectivity in remote or underserved areas can facilitate telehealth initiatives, enabling patients in rural locations to access quality healthcare remotely.
- 9. *AR and VR in Medical Education*: 6G's low latency and high data rates can support immersive AR and VR experiences, which could enhance medical education and training by enabling realistic simulations and remote learning opportunities.
- 10. *Connectivity for Medical Research and Clinical Trials*: 6G's connectivity can facilitate data sharing and collaboration in medical research, clinical trials, and healthcare data analytics, leading to faster advancements in medical knowledge.

#### *Components of IoMT in 6G communication*

- 1. *Cloud Services*: Cloud platforms provide storage, processing, and analysis of medical data collected from various sources. This includes patient records, diagnostics, treatment plans, and research datasets.
- 2. *Edge Servers and Gateways*: Edge computing servers and gateways are deployed closer to the data source, allowing for real‐time data processing, reducing latency, and enabling faster decision‐making. These components manage data flow between medical devices and the cloud.
  - Figure 7 illustrates the components of IoMT in 6G [[21](#page-21-0)].
- 3. *Medical Devices, Sensors, Wearables, and Implants*: These devices are equipped with sensors to monitor patients' vital signs, health parameters, and other medical data. Wearables and implants can continuously transmit data to the healthcare infrastructure for analysis and decision‐making.
- 4. *6G Network*: The backbone of the communication system, 6G provides ultra‐high data rates, low latency, and massive device connectivity. It ensures seamless and reliable communication between medical devices, healthcare facilities, and cloud services [[22](#page-21-0)].

#### *Communication flows*

1. Medical devices, wearables, and implants continuously collect data from patients.

![](_page_8_Picture_16.jpeg)

**FIGUR E 7** Internet of medical things.

- 2. Edge servers and gateways process and analyse the collected data, filtering out non‐critical information and performing initial data processing.
- 3. Processed data is transmitted through the 6G network to both cloud services and healthcare facilities.
- 4. In cloud services, advanced analytics, ML, and AI algorithms are applied to the data to provide accurate diagnostics, predictive insights, and personalised treatment recommendations.
- 5. Healthcare professionals access the analysed data from cloud services, enabling remote patient monitoring, virtual consultations, and informed decision‐making.
- 6. Healthcare facilities use the insights gained from the data to adjust treatment plans, initiate timely interventions, and optimise patient care.
- 7. The 6G network ensures the real‐time and secure transmission of critical medical data, allowing for rapid responses in emergency situations and enabling the execution of remote surgeries or interventions [[23](#page-21-0)].

### 4.3.3 | Internet of drones (IOD)

The integration of drones with 6G communication has the potential to significantly enhance the capabilities and applications of unmanned aerial vehicles. Drones are used across various industries, including agriculture, logistics, surveillance, and disaster management. When combined with the features of 6G technology, drones can operate more efficiently, safely, and intelligently. Figure [8](#page-9-0) illustrates the components of IOD. Here's an overview of how the IOD could work within the context of 6G communication:

- 1. *URLLC*: 6G's URLLC capabilities can provide drones with real‐time communication, allowing for instant control inputs and immediate responses. This is crucial for applications that require rapid decision‐making, such as autonomous drone navigation and collision avoidance.
- 2. Enhanced Connectivity and Range 6G's increased connectivity and extended range capabilities can enable drones to operate over larger distances and in more challenging environments. This is particularly useful for applications like long‐range delivery, infrastructure inspection, and search and rescue missions.
- 3. *Massive Device Connectivity*: 6G's ability to connect a massive number of devices can support drone fleets

<span id="page-9-0"></span>![](_page_9_Picture_2.jpeg)

**FIGURE 8** Internet of drones.

operating simultaneously. This enables coordinated actions among multiple drones, making swarm robotics and collaborative tasks more efficient.

- 4. *High‐Resolution Data Transmission*: Drones equipped with advanced sensors, cameras, LiDAR, and other data‐ gathering tools can transmit high‐resolution data back to operators or processing centres in real‐time. This supports applications like aerial mapping, environmental monitoring, and surveillance.
- 5. *Edge Computing for Real‐Time Processing*: 6G's support for edge computing allows drones to process data locally, reducing the need to transmit large amounts of data to remote servers. This can lead to quicker decision‐making and reduced latency in critical applications.
- 6. *Autonomous Navigation and AI*: Drones integrated with AI algorithms can use real‐time data from sensors and cameras to navigate autonomously, avoiding obstacles and making intelligent decisions. 6G's capabilities can facilitate the exchange of AI‐processed data for more sophisticated navigation and analysis.
- 7. *Remote Operation and Telepresence*: 6G's low latency and high bandwidth can enable operators to remotely control drones as if they were physically present. This is valuable for scenarios like remote inspections of infrastructure or disaster‐stricken areas.
- 8. *Real‐Time Surveillance and Monitoring*: Drones can transmit live video feeds for surveillance and monitoring purposes. With 6G, these feeds can be of higher quality, more reliable, and streamed seamlessly to security personnel or remote monitoring stations.
- 9. *Dynamic Reconfiguration*: 6G's network slicing capabilities can be applied to allocate network resources for specific drone applications or tasks. This dynamic resource allocation optimises communication based on the drone's current function, enhancing efficiency and performance.
- 10. *Emergency Response and Disaster Management*: Drones can quickly provide situational awareness and assess disaster‐stricken areas. With 6G, first responders can access real‐time data and video feeds to make informed decisions and coordinate rescue efforts.

11. *Secure Communication*: 6G's advanced security features can help protect drone communication from cyber threats, ensuring safe and reliable operation in sensitive applications.

In summary, the integration of drones with 6G communication hold tremendous potential to transform various industries by enabling more sophisticated and versatile drone applications. As with any emerging technology, the actual implementation and capabilities will depend on the evolution of 6G technology and the specific use cases that emerge. Certainly, heres a high‐level diagram illustrating the components of the integration of the IOD with 6G communication:

#### *Components of IOD in 6G communication*

- 1. *Cloud Services*: Cloud platforms provide storage, processing, and analysis of drone‐collected data, including images, videos, telemetry, and mission‐specific information.
- 2. *Edge Servers and Gateways*: Edge computing infrastructure enables real‐time data processing at the edge of the network, allowing for rapid analysis of sensor data, obstacle detection, and immediate decision‐making.
- 3. *Drone Fleet*: This refers to a collection of drones equipped with various sensors, cameras, and communication modules. The fleet operates together for specific tasks or applications.
- 4. *Drone Sensors and Cameras*: Drones are equipped with a variety of sensors, such as Global Positioning System, accelerometers, gyroscopes, LiDAR, and cameras. These sensors gather real‐time data about the drones surroundings and operational status.
- 5. *Drone Controllers*: These devices are used by operators to control and manage drone operations. They can include remote controllers, tablets, smartphones, and specialised control interfaces.
- 6. *6G Network*: The 6G network [[24](#page-21-0)] provides the communication backbone for the entire system, facilitating real‐ time data exchange between drones, edge servers, cloud services, and operators.

#### *Communication flows*

- 1. Drone sensors and cameras collect data about the drone's environment, flight status, and mission‐specific tasks.
- 2. Edge servers and gateways process sensor data locally, performing tasks like obstacle avoidance, terrain analysis, and preliminary image processing.
- 3. Processed data is transmitted through the 6G network to both cloud services and operators' devices, ensuring seamless and high‐quality communication [\[25](#page-21-0)].
- 4. In cloud services, advanced analytics, AI algorithms, and storage capabilities are applied to the drone‐collected data for further analysis and actionable insights.
- 5. Drone operators use their devices to remotely control drones, receive real‐time video feeds, and monitor telemetry data from the drone fleet.
- 6. The 6G network enables low‐latency, high‐bandwidth communication, allowing for precise and immediate

BHIDE ET AL. - **11 of 23**

control inputs to drones, even for complex and time‐critical tasks.

This diagram illustrates how the IOD can leverage 6G communication to enable real‐time control, data collection, processing, and analysis. The integration of drones with 6G technology enhances their capabilities, enabling them to perform a wide range of tasks across industries such as agriculture, surveillance, disaster response, and logistics. It's important to note that the specifics of the components and communication flows may evolve as both drone technology and 6G technology continue to develop.

### 4.3.4 | Internet of robotic things

The integration of Robotic Things with 6G communication holds [\[15\]](#page-21-0) the potential to revolutionise industries by enabling advanced robotic systems to operate more efficiently, intelligently, and autonomously. Robotic Things refer to physical objects that are equipped with robotic capabilities, sensors, and communication interfaces, allowing them to interact with the environment and exchange information with other devices and systems. When combined with the features of 6G technology, Robotic Things can have a profound impact across various sectors. Here's an overview of how the Internet of Robotic Things (IoRT) could work within the context of 6G communication:

- 1. *URLLC*: 6G's URLLC capabilities ensure that real‐time communication between robots and control systems is nearly instantaneous. This is essential for applications that demand quick and precise control, such as teleoperation, remote surgeries, and industrial automation.
- 2. *Massive Device Connectivity*: The IoRT involves a multitude of robotic devices working together collaboratively. 6G's capability to connect a massive number of devices ensures seamless communication among robots, sensors, and control centres.
- 3. *High‐Quality Sensor Data Transmission*: Robotic Things are equipped with various sensors (e.g. cameras, LiDAR, accelerometers) to perceive and interact with their environment. 6G's higher data rates and improved reliability enable high‐quality and real‐time transmission of sensor data for enhanced perception and decision‐making.
- 4. *Edge Computing for Real‐Time Processing*: 6G's support for edge computing allows robotic systems to process sensor data and make decisions closer to the source of data generation. This reduces latency and enables faster response times in real‐time applications.
- 5. *Autonomous and Collaborative Robotics*: Robots integrated with AI algorithms can make decisions based on real‐time sensor data [\[26\]](#page-21-0). With 6G's capabilities, robots can communicate with each other, share information, and work collaboratively to achieve complex tasks.
- 6. *Remote Operation and Telepresence*: 6G's low latency and high bandwidth can facilitate remote operation of robots

- with a sense of presence. This is valuable for tasks like remote inspection, maintenance, and hazardous environment exploration.
- 7. *AI‐Driven Robotic Systems*: 6G can facilitate the exchange of large datasets for training and deploying AI models. This enables robots to adapt and learn from new situations and environments, enhancing their capabilities.
- 8. *Secure Communication*: 6G's advanced security features ensure that communication between robotic systems, control centres, and other devices is secure and protected from cyber threats.
- 9. *Human‐Robot Interaction*: The combination of 6G's low latency and high‐quality communication can improve the naturalness and responsiveness of human‐robot interactions. This is beneficial for applications in healthcare, education, entertainment, and customer service.
- 10. *Remote Monitoring and Diagnostics*: Robots can transmit real‐time operational data and diagnostics to remote experts for analysis and troubleshooting. 6G's capabilities ensure reliable and rapid communication for timely assistance.
- 11. *Industrial Automation*: In industrial settings, robots can be coordinated and controlled to optimise production processes. 6G's low latency and reliability enhance the precision and efficiency of manufacturing and logistics operations.

In summary, the integration of Robotic Things with 6G communication has the potential to transform industries by enabling advanced robotics applications that require real‐time control, collaboration, and intelligent decision‐making. As with any emerging technology, the actual implementation and capabilities will depend on the evolution of 6G technology and the specific use cases that emerge. Figure [9](#page-11-0) illustrates the components of the integration of the IoRT with 6G communication:

### *Components of internet of robotic things in 6G communication*

- 1. *Cloud Services*: Cloud platforms provide storage, processing, and analysis of data generated by robotic systems. This includes sensor data, AI models, operational logs, and task‐ specific information.
- 2. *Edge Servers and Gateways*: Edge computing infrastructure allows robots to process sensor data locally for rapid decision‐making, reducing latency and enabling real‐time responses.
- 3. *Robotic Things*: This encompasses a range of physical objects with robotic capabilities, including sensors, actuators, and communication interfaces. These robotic systems interact with the environment and perform tasks based on inputs and control commands.
- 4. *Robotic Sensors and Actuators*: Sensors gather data about the robot's surroundings and performance, while actuators execute physical actions based on control commands. These components are crucial for perception and interaction.

26328925, 2025, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/qtc2.12114 by University Of Sao Paulo - Brazil, Wiley Online Library on [25/08/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<span id="page-11-0"></span>**12 of 23** - BHIDE ET AL.

![](_page_11_Figure_2.jpeg)

**FIGURE 9** Internet of robotic things. AI, artificial intelligence.

- 5. *Robotic Controllers and AI*: The controllers manage the operation of robotic systems, and AI algorithms enhance their decision‐making capabilities. 6G's capabilities enable AI‐enhanced robots to communicate and learn from their environment more effectively.
- 6. *6G Network*: The 6G network serves as the communication backbone, connecting robots, edge servers, cloud services, and human operators. It provides low‐ latency, high‐bandwidth communication for real‐time interaction.

#### *Communication flows*

- 1. Robotic sensors and cameras collect data about the robot's surroundings, interactions [\[27\]](#page-21-0), and task‐specific requirements.
- 2. Edge servers and gateways process sensor data locally, enabling real‐time decisions for robot navigation, manipulation, and task execution.
- 3. Processed data is transmitted through the 6G network to both cloud services and human operators, ensuring seamless and reliable communication.
- 4. In cloud services, advanced analytics, AI algorithms, and storage capabilities are applied to robot‐generated data, enabling further analysis and decision support.
- 5. Human operators use cloud‐based interfaces to remotely control robots, monitor sensor data, and receive real‐time video feeds for situational awareness.
- 6. The 6G network facilitates low‐latency, high‐bandwidth communication, allowing for immediate control inputs, feedback, and updates between operators and robots.

### 4.3.5 | Industry internet of things

The Industrial Internet of Things (IIoT) is a subset of the broader IoT concept, focussing specifically on the integration of IoT technologies and solutions within industrial and manufacturing environments [\[28\]](#page-21-0). IIoT aims to enhance industrial processes, automation, and efficiency by connecting devices, sensors, machines, and systems to collect and

![](_page_11_Figure_15.jpeg)

**FIGUR E 1 0** Industry internet of things. AI, artificial intelligence; IIoT, industrial internet of things.

exchange data for improved decision‐making and operations. Figure 10 illustrates the components of Industry IoT.

When considering the potential impact of 6G communication on the IIoT, several key aspects come to mind:

- 1. *Ultra‐Reliable and Low Latency Communication*: 6G's advancements in ultra‐reliable and low‐latency communication can greatly benefit the IIoT. Industries such as manufacturing, energy, and transportation require real‐time communication for tasks like remote control, predictive maintenance, and safety‐critical operations. 6G's reduced latency can enable faster response times and more efficient operations.
- 2. *Massive Device Density*: The industrial sector often involves deploying a large number of sensors and devices to monitor and manage various processes. 6G's capacity to handle a higher density of devices can support more comprehensive monitoring and control systems within industrial settings.
- 3. *Mission‐Critical Applications*: Certain IIoT applications, such as robotic assembly lines or autonomous vehicles within factories, demand highly reliable and deterministic communication. 6G's focus on meeting mission‐critical communication requirements can enhance the performance and safety of such applications.
- 4. *Enhanced Automation and Robotics*: With 6G, industrial robots and automated systems can benefit from faster data exchange, enabling more responsive and coordinated movements. This can lead to improved efficiency in manufacturing and logistics.
- 5. *Edge Computing Integration*: 6G's integration of edge computing capabilities can reduce latency by processing data closer to where it's generated. In IIoT scenarios, this means critical data can be analysed and acted upon without the need to send it back to a central data centre, thus improving overall system responsiveness.
- 6. *Advanced Data Analytics*: 6G's increased data speeds and capacities can support more sophisticated data analytics and ML models within IIoT environments. This enables better insights, predictive maintenance, and optimisation of industrial processes [[29\]](#page-21-0).

BHIDE ET AL. - **13 of 23**

- 7. *Energy Efficiency*: The IIoT often involves battery‐operated sensors and devices distributed throughout large facilities. 6G's potential for energy‐efficient communication protocols can extend the battery life of these devices, reducing maintenance efforts.
- 8. *Security and Privacy*: IIoT environments require robust security measures to protect critical infrastructure and sensitive data. 6G's advancements in encryption, authentication, and secure communication protocols can enhance the security posture of IIoT systems [[30](#page-21-0)].
- 9. *Remote Monitoring and Management*: Industries with widespread operations can benefit from 6G's broader coverage and improved connectivity. This enables remote monitoring and management of assets, reducing the need for on‐site visits and improving operational efficiency.

#### *Components*

- 1. *Sensors/Devices*: These are the physical devices placed within the industrial environment to collect data. They can include various types of sensors, actuators, and other monitoring devices that gather information about temperature, pressure, humidity, vibration etc.
- 2. *Sensor Nodes*: These are the nodes that aggregate data from multiple sensors. They process and pre‐process the data before sending it further, reducing the amount of data sent to the higher levels of the system.
- 3. *Edge Computing*: This [\[31](#page-21-0)] layer performs initial processing and analysis of data closer to the source (sensors) rather than sending all the data to a remote cloud server. Edge computing helps reduce latency, optimise data transmission, and enable real‐time decision‐making.
- 4. *IIoT Applications*: These are the specific applications that leverage the data collected from sensors to achieve various goals, such as predictive maintenance, process optimisation, quality control, and more. They run on the edge computing layer.
- 5. *Cloud/Server*: This is the central data processing and storage hub. It stores and processes data received from edge devices, allowing for further [[32](#page-21-0)] analysis, historical tracking, and long‐term storage. Advanced analytics and ML models can also be deployed here.

## 4.3.6 | Holographic communication

Holographic communication is an advanced form of communication that involves transmitting and receiving three‐ dimensional (3D) holographic images, rather than traditional two‐dimensional images or videos. In the context of 6G communication, the capabilities of 6G networks could have a significant impact on the development and deployment of holographic communication technologies. Here's how holographic communication could be influenced by 6G. Figure 11 illustrates Holographic Communication [[33](#page-21-0)]

1. *Ultra‐High Data Rates*: 6G is expected to provide ultra‐ high data rates, potentially reaching terabit‐per‐second

- speeds. Holographic images are data‐intensive due to the complex nature of 3D data. 6G's high data rates could enable the seamless transmission of large and intricate holographic images in real‐time.
- 2. *Low Latency*: Holographic communication requires minimal latency to maintain the perception of real‐time interaction. 6G's focus on ultra‐low latency communication can ensure that holographic interactions are smooth and responsive, making them suitable for applications like remote collaboration, telemedicine, and entertainment.
- 3. *Massive Device Connectivity*: Holographic communication may involve multiple devices, including capture devices (such as holographic cameras), transmission devices, and receiving devices (such as holographic displays). 6G's ability to support a massive number of connected devices can facilitate seamless integration and synchronisation of these devices.
- 4. *High‐Fidelity Data Transfer*: Holographic images require high‐fidelity data transfer to preserve the details and depth of the images. 6G's improved Quality of Service (QoS) and [[34](#page-21-0)] error correction mechanisms can ensure that holographic images are accurately transmitted and received without degradation.
- 5. *Advanced Beamforming and Antenna Technologies*: 6G is expected to introduce advanced beamforming and antenna technologies, enabling highly directional and focused signal transmission. This can be beneficial for holographic communication, as it would allow for efficient data transmission to specific holographic display devices or users.
- 6. *Edge Computing Integration*: Holographic communication involves significant computational requirements, especially for encoding, decoding, and rendering 3D holographic images. 6G's integration of edge computing can provide the necessary computational resources near the user, reducing the processing load on devices and enhancing real‐time interaction.

![](_page_12_Figure_20.jpeg)

**FIGUR E 1 1** Holographic communication.

- 7. *Immersive Experiences*: Holographic communication aims to provide immersive experiences that mimic real‐life interactions. 6G's capabilities can enhance these experiences by supporting features like real‐time gesture recognition, spatial audio, and interactive elements within holographic environments.
- 8. *Security and Privacy*: Transmitting and receiving holographic data involves sensitive visual information. 6G's advancements in security and privacy mechanisms can ensure that holographic communications remain secure and protected from unauthorised access or tampering.
- 9. *Content Creation and Collaboration*: 6G's high data rates and low latency can enable real‐time collaboration on creating and editing holographic content. Multiple users in different locations can interact in real time to design, simulate, or showcase holographic objects or scenes.

#### *Components*

- 1. *Holographic Capture Devices (Cameras)*: These devices capture the real‐world scenes or objects in 3D, converting them into holographic data. These devices could include advanced cameras capable of capturing depth information, colour, and texture for accurate holographic representation.
- 2. *Holographic Processing*: [[35](#page-21-0)] This layer processes the captured data, encoding it into a format suitable for transmission and rendering. It involves compression, encryption, and potentially AI‐driven enhancement to ensure high‐quality holographic data.
- 3. *Edge Computing*: The edge computing layer performs initial processing and optimisation of the holographic data. This can involve data compression, format conversion, and initial rendering to ensure efficient data transmission and reduced latency.
- 4. *Holographic Communication*: This layer is responsible for transmitting the processed holographic data over the 6G network. It leverages 6G's high data rates, low latency, and massive device connectivity to ensure real‐time and high‐ quality holographic communication.
- 5. *Holographic Display Devices*: These devices receive the transmitted holographic data and render it as a 3D holographic image that users can interact with. These devices could include specialised holographic displays or MR devices capable of overlaying holograms onto the real world.
- 6. *Cloud/Server*: The cloud/server stores and manages the holographic data, including content libraries, user profiles, and real‐time communication sessions [[36\]](#page-21-0). It provides a central hub for data storage and distribution, especially for scenarios involving multiple users and content sharing.

### 4.3.7 | Blockchain

Integrating blockchain technology into 6G communication systems has the potential to bring about various benefits, primarily in terms of enhancing security, privacy, trust, and data management [\[37\]](#page-21-0). Here's how blockchain could intersect with 6G communication:

- 1. *Security and Privacy Enhancement*: Blockchain's decentralised and tamper‐resistant nature can strengthen the security and privacy of 6G networks. It can be used to secure communication channels, authenticate devices, and protect sensitive data from unauthorised access.
- 2. *Identity and Access Management*: Blockchain can provide a secure and decentralised way of managing user identities and access permissions. This can help prevent unauthorised access to devices, applications, and data within the 6G ecosystem.
- 3. *Device Authentication and Integrity*: With the massive proliferation of IoT devices in 6G networks, ensuring the authenticity and integrity of devices is crucial. Blockchain can facilitate a trust‐based system where devices are registered on the blockchain, making it harder for malicious devices to infiltrate the network.
- 4. *Data Integrity and Provenance*: Blockchain can be used to establish an immutable record of data transactions and exchanges. In 6G networks, this can help ensure the integrity of data as it moves between devices and systems, reducing the risk of data tampering or manipulation.
- 5. *Secure Communication and Transactions*: Blockchain can enable secure communication and transactions between devices without the need for central intermediaries. This is particularly relevant for scenarios like micropayments, device‐to‐device transactions, and secure communication in IoT networks.
- 6. *Smart Contracts*: 6G and IoT networks can leverage smart contracts on a blockchain to automate and ensure the execution of predefined actions based on specified conditions. This can streamline processes, facilitate interactions, and enhance the efficiency of various applications.
- 7. *Network Management and Orchestration*: Blockchain can assist in managing and orchestrating various components of 6G networks, such as dynamically allocating resources, optimising routing, and ensuring efficient network operation.
- 8. *Data Monetisation and Ownership*: Blockchain can enable users to have more control over their data and its monetisation [\[38\]](#page-21-0). Users could securely grant access to their data in exchange for compensation, fostering a more transparent data economy.
- 9. *Roaming and Cross‐Network Payments*: For 6G networks with global reach, blockchain can facilitate seamless cross‐ network payments and roaming arrangements, making it easier for users to access services while maintaining their privacy and security.
- 10. *Network Management and Coordination*: In complex 6G networks with dynamic resource allocation, blockchain can help manage and coordinate resources, ensuring efficient network operation while maintaining transparency and accountability.

BHIDE ET AL. - **15 of 23**

Figure 12 is a simplified diagram outlining the components and interactions within a [\[39\]](#page-21-0) 6G communication system that incorporates blockchain technology:

### *Components*

- 1. *Cloud/Server (Blockchain Network)*: This represents the decentralised blockchain network where data, transactions, and smart contracts are stored and managed securely.
- 2. *Edge Computing*: The edge computing layer processes and optimises data closer to the source, reducing latency and enhancing responsiveness.
- 3. *Device Identity and Authentication*: Blockchain provides a secure and tamper‐resistant method for authenticating devices and establishing their identities within the network.
- 4. *Data Integrity and Provenance*: Data transactions are recorded on the blockchain to ensure their integrity, traceability, and immutability.
- 5. *Smart Contracts and Autonomous Interactions*: Smart contracts are self‐executing contracts with predefined rules. They automate actions based on specified conditions, enabling autonomous interactions between devices or parties.
- 6. *Secure Communication and Data Exchange*: Blockchain can be used to ensure secure communication channels between devices, protecting data transmission from unauthorised access or tampering.
- 7. *Decentralised Identity and Access Management*: Blockchain can facilitate decentralised identity management, enabling users to maintain control over their identity and access permissions without relying on central authorities.

### 4.3.8 | Extended reality

Extended Reality (XR) [[40](#page-21-0)] refers to the spectrum of immersive technologies that encompass VR, AR, and MR. XR combines the physical and digital worlds to create interactive and immersive experiences for users. In the context of 6G communication, XR can be significantly enhanced and transformed. Here's how XR might evolve with the advent of 6G:

![](_page_14_Figure_13.jpeg)

- 1. *Ultra‐Low Latency*: 6G's ultra‐low latency capabilities will be crucial for XR experiences. In VR and AR, low latency is essential to prevent motion sickness and provide seamless interaction with virtual objects. With 6G, XR experiences can achieve near‐real‐time responsiveness, enhancing immersion.
- 2. *High Data Rates*: XR applications require a substantial amount of data to render high‐quality 3D graphics and visuals. 6G's high data rates can enable more detailed and realistic XR environments, improving the quality of graphics, textures, and animations.
- 3. *Massive Device Connectivity*: XR scenarios can involve multiple devices, such as headsets, sensors, cameras, and interactive objects. 6G's capacity to connect a massive number of devices simultaneously can enhance the coordination and synchronisation of these devices for richer XR experiences.
- 4. *Spatial Computing and Mapping*: 6G's advanced capabilities in edge computing and data processing can support complex spatial computing tasks. This involves real‐time mapping of physical spaces and interaction with digital objects, enabling more sophisticated AR and MR experiences.
- 5. *Haptic Feedback and Interactivity*: XR experiences are more immersive when they involve multiple sensory inputs, including touch and haptic feedback. 6G's low latency can enable real‐time communication between devices, enhancing the responsiveness of haptic devices for a more tactile experience.
- 6. *Remote Collaboration and Telepresence*: With 6G, XR can enable more realistic remote collaboration. People in different locations can feel as if they are present in the same physical space, fostering enhanced communication and collaboration across distances [\[41](#page-21-0)].
- 7. *Advanced Content Streaming*: XR content often requires streaming high‐quality 3D models and visuals. 6G's high data rates can facilitate smoother streaming of XR content without buffering or lag, improving the user experience.
- 8. *MR Integration*: 6G can further blur the lines between the physical and digital worlds in MR. MR combines elements of both AR and VR, and with 6G, these experiences can seamlessly blend real‐world interactions with digital overlays.
- 9. *Immersive Entertainment*: XR has vast potential for immersive entertainment experiences. With 6G, interactive and cinematic XR content can be delivered seamlessly, providing users with novel and engaging forms of entertainment.
- 10. *Training and Simulation*: Industries can leverage XR and 6G for advanced training and simulation applications. From medical training to industrial simulations, users can interact with virtual environments in highly realistic ways.
- 11. *Personalised and Adaptive Experiences*: With the data processing capabilities of 6G, XR experiences can become more personalised and adaptive, responding to users' behaviour, preferences, and surroundings in real time. **FIGURE 1 2** Components of blockchain. Following figure illustrates internal structure XR [[42](#page-21-0)].

Incorporating 6G communication [[16\]](#page-21-0) into XR applications has the potential to revolutionise how users interact with digital content, engage in collaborative activities, and experience the world around them. The combined power of 6G's low latency, high data rates, and massive device connectivity can contribute to making XR experiences more seamless, immersive, and integrated into everyday life. Certainly, Figure 13 is a simplified diagram outlining the components and interactions within an XR system integrated with 6G communication technology:

#### *Components*

- 1. *Cloud/Server (XR Content)*: This represents the cloud or server where XR content is stored, managed, and delivered to users.
- 2. *Edge Computing*: The edge computing layer processes and optimises XR content closer to the user's device, reducing latency and enhancing responsiveness.
- 3. *XR Content Processing, Rendering, and Streaming*: This layer processes XR content, renders 3D graphics, and streams the content to users' devices for a seamless experience.
- 4. *Haptic Feedback and Interaction Devices*: These devices provide haptic feedback and allow users to interact with the XR environment through touch, gestures, and motion.
- 5. *Spatial Mapping and Real‐time Environment Interaction*: This layer involves real‐time mapping of the physical environment and interaction with virtual objects, enabling augmented and MR experiences.
- 6. *Remote Collaboration and Telepresence*: XR can facilitate realistic remote collaboration and telepresence, allowing users in different locations to interact as if they are in the same physical space.

### **4.4** | **Middleware layer: Scheduling and resource management in middleware layer of 6G communication**

Scheduling and resource management in the middleware layer of 6G communication will likely focus on efficiently allocating

![](_page_15_Figure_12.jpeg)

and prioritising resources like bandwidth, spectrum, and computing power to meet the diverse needs of applications. Advanced AI‐driven algorithms could be used to optimise resource allocation and adapt to dynamic network conditions, ensuring low latency and high throughput for various services, from IoT to high‐definition multimedia. This layer will likely play a crucial role in enabling the seamless integration of different technologies and services in the 6G ecosystem.

### 4.4.1 | Energy and performance optimisation

In the middleware layer of 6G communication, energy and performance optimisation are critical considerations to ensure sustainable and efficient network operation. Various techniques are employed to achieve these goals:

*Dynamic Power Management*: This involves adjusting the power levels of different network components based on traffic load and demand, thus minimising energy consumption while maintaining performance.

*Energy‐Efficient Algorithms*: Middleware components can utilise algorithms that prioritise energy‐efficient processing, communication, and resource allocation to prolong device battery life.

*Intelligent Resource Allocation*: AI‐driven resource allocation algorithms can dynamically distribute resources based on real‐time requirements, optimising performance while minimising energy consumption.

*Proactive Sleep Modes*: Devices and network elements can enter low‐power sleep modes when not actively transmitting or receiving data, reducing energy consumption during idle periods.

*Adaptive Frequency and Bandwidth Allocation*: Middleware can intelligently allocate frequency bands and adjust bandwidth based on the current network conditions, optimising performance and energy usage.

*Context‐Awareness*: Middleware can leverage context information (location, user behaviour etc.) to tailor network operations, enabling more efficient use of resources and energy.

*Cognitive Radio Technologies*: These technologies enable devices to intelligently select available frequencies, minimising interference and optimising energy usage.

*QoS Management*: Balancing QoS requirements with energy efficiency is crucial. Middleware can dynamically adjust QoS parameters to achieve a balance between performance and energy consumption.

*Data Offloading*: Middleware can facilitate intelligent data offloading to less energy‐intensive networks (e.g. Wi‐Fi) when available, reducing cellular data usage and extending battery life.

*Task Consolidation and Migration*: Middleware can optimise energy consumption by consolidating tasks on fewer resources or migrating tasks to more energy‐efficient nodes within the network.

These strategies, among others, are designed to create a **FIGURE 1 3** Extended reality (XR). harmonious balance between delivering high performance and BHIDE ET AL. - **17 of 23**

minimising energy usage in the complex 6G communication landscape.

### 4.4.2 | Security

Security in 6G communication is a critical concern due to the increasing complexity and potential vulnerabilities of the evolving network landscape. Here are some aspects of security in 6G:

*End‐to‐End Encryption*: Strong encryption mechanisms will be crucial to safeguard data as it traverses the network, preventing unauthorised access or interception.

*Quantum‐Safe Cryptography*: 6G networks are being designed with the anticipation of quantum computing capabilities. Quantum‐safe cryptography ensures that even with powerful quantum computers, encrypted data remains secure.

*Authentication and Identity Management*: Robust authentication methods will be implemented to ensure that devices, users, and services are legitimate before gaining access to the network.

*Privacy‐Preserving Techniques*: [\[43\]](#page-21-0) With the proliferation of data, mechanisms that allow data sharing while preserving privacy (like differential privacy) will be important to prevent unauthorised access to sensitive information.

*Network Slicing Security*: Network slicing, a key feature of 6G, can potentially introduce security risks if not properly managed. Isolating and securing each network slice is crucial to prevent cross‐slice attacks.

*AI‐Driven Security*: AI and ML will play a role in identifying and mitigating security threats in real time. Anomaly detection and behaviour analysis can help detect unusual activities.

*Supply Chain Security*: Ensuring the security of hardware components and software from the manufacturing stage to deployment is essential to prevent compromise at any point in the supply chain.

*Distributed Ledger Technology*: Technologies like blockchain can enhance security by providing transparency, traceability, and immutability of transactions and communications.

*Zero Trust Architecture*: This approach assumes that no device or user should be trusted by default, requiring continuous authentication and verification for access.

*Threat Intelligence Sharing*: Collaborative efforts between organisations and even between countries to share threat intelligence can help identify and mitigate emerging security risks.

*Physical Layer Security*: Techniques that use the physical properties of wireless communication, like beamforming, can provide additional security layers against eavesdropping and interference.

*Regulatory Measures*: Governments and regulatory bodies will need to enforce security standards and guidelines to ensure that service providers and manufacturers adhere to robust security practices.

Given the anticipated complexities and challenges of 6G networks, a multi‐faceted and proactive approach to security is essential to safeguard the integrity, confidentiality, and availability of communications and data [\[44\]](#page-21-0).

### 4.4.3 | Context aware data caching

Context‐aware data caching in 6G communication involves optimising data storage and retrieval based on the specific context of users, devices, and the network environment. This approach aims to enhance data availability, reduce latency, and improve overall network efficiency. Here's how it works:

*Context Information*: Context includes factors such as user location, device type, application requirements, network conditions, and time of day. This information is collected from various sources, including sensors on devices, network analytics, and user preferences.

*Dynamic Caching*: Rather than storing data uniformly across all caching nodes, context‐aware caching dynamically determines which data to store based on the context. This minimises the amount of unnecessary data stored, optimising cache space.

*Predictive Analysis*: Advanced algorithms use historical data and patterns to predict what content might be requested in the future based on the context. This proactive approach reduces latency by preloading relevant data.

*User Mobility*: As users move, their context changes. Context‐aware caching adapts by updating the cache content to reflect the new context, ensuring that frequently accessed data remains available even as users move between cells or locations.

*QoS Optimisation*: Caching decisions take into account the QoS requirements of applications. For example, real‐time applications might prioritise caching content that reduces latency for those specific services.

*Content Personalisation*: By understanding user preferences and context, content can be personalised and cached accordingly, enhancing user experience.

*Energy Efficiency*: Context‐aware caching reduces the need to fetch data from distant servers, leading to less energy consumption and prolonging device battery life.

*Network Load Reduction*: As popular content is cached closer to users, the load on the core network is reduced, leading to improved network efficiency.

*Multi‐Access Edge Computing (MEC)*: MEC nodes, located closer to users, can leverage context‐aware caching to provide low‐latency access to frequently used content, enhancing the overall edge computing experience.

*ML and AI*: AI‐driven algorithms can continuously analyse context data and optimise caching strategies, adapting to changing usage patterns and network conditions.

Context‐aware data caching aligns with the goals of 6G communication, which emphasise low latency, high data rates, and efficient resource utilisation. By intelligently managing cached content based on the specific needs of users and the network, this approach enhances the overall performance and user experience of 6G networks.

### 4.4.4 | Data availability

Data availability in 6G [[45\]](#page-21-0) communication refers to the accessibility and reliability of data for users and applications within the network. 6G aims to provide seamless, high‐ capacity, and low‐latency connectivity, ensuring that data is readily accessible whenever and wherever needed. Here are some key aspects of data availability in 6G:

*Ultra‐Reliable Communication*: 6G is expected to deliver ultra‐reliable communication, ensuring that critical applications, such as remote surgery, autonomous vehicles, and industrial automation, receive data without disruption.

*Massive Connectivity*: 6G networks are designed to support a massive number of connected devices simultaneously, enabling efficient data exchange and availability for various IoT applications.

*High Data Rates*: 6G aims to provide significantly higher data rates compared to previous generations, enabling faster data transfer and real‐time access to large datasets.

*MEC*: MEC brings computing resources closer to the edge of the network, reducing latency and ensuring faster data processing and delivery, enhancing data availability.

*Advanced Network Slicing*: Network slicing allows the creation of virtual networks optimised for specific applications. This customisation ensures that data availability matches the unique requirements of each application.

*Context‐Aware Data Caching*: As discussed earlier, context‐aware caching optimises data availability by storing frequently used data closer to users, reducing latency and improving user experience.

*Diverse Connectivity Options*: 6G is expected to support a variety of connectivity options, including traditional cellular networks, satellite communication, and terrestrial wireless networks, ensuring data availability in various environments.

*Reliable Backhaul and Transport Networks*: The backbone and transport networks of 6G will be designed to handle the increased data traffic efficiently, ensuring reliable data transmission across the entire network.

*Hybrid Communication Technologies*: 6G will integrate various communication technologies, such as terahertz frequencies and free‐space optical communication, to extend coverage and enhance data availability.

*Self‐Healing Networks*: 6G networks may incorporate self‐ healing mechanisms that detect and repair network issues automatically, ensuring continuous data availability even in the presence of failures.

*Global Coverage*: Efforts will be made to provide global coverage, including in remote and underserved areas, ensuring that data availability is not limited to urban regions.

*Resilience to Interference*: 6G networks will be designed to minimise interference and adapt to changing environmental conditions, maintaining consistent data availability.

Overall, data availability in 6G communication aims to create a network ecosystem where data is highly accessible, reliable, and responsive, enabling a wide range of applications and services to function seamlessly:

#### *IoT infrastructure*

The IoT infrastructure in 6G communication is anticipated to be significantly advanced compared to previous generations. It's designed to handle the massive influx of connected devices, diverse applications, and the unique requirements of IoT ecosystems. Here are some key aspects of the IoT infrastructure in 6G communication:

*Massive Device Connectivity*: 6G is designed to accommodate an immense number of IoT devices, ranging from sensors and actuators to wearable gadgets and industrial machines.

*Ultra‐Low Latency*: IoT applications often require real‐ time or near‐real‐time response. 6G aims to provide ultra‐ low latency connectivity, enabling IoT devices to communicate and respond quickly.

*High Data Rates*: IoT devices generate and transmit substantial amounts of data. With higher data rates, 6G can support the efficient exchange of data between devices and the cloud.

*Network Slicing*: 6G's network slicing capabilities allow the creation of dedicated virtual networks optimised for different IoT use cases, ensuring tailored resources and QoS for each application.

*Edge and Fog Computing*: The integration of edge and fog computing in 6G enables data processing and analysis closer to IoT devices, reducing latency and enhancing real‐time decision‐making.

*Device Diversity*: 6G supports a wide range of IoT devices with varying capabilities, sizes, and power requirements, allowing for more flexibility in IoT deployments.

*Energy Efficiency*: 6G IoT devices will be designed to operate efficiently, conserving energy to prolong battery life and reduce the overall energy consumption of the network.

*AI and ML*: 6G's enhanced capabilities enable IoT devices to leverage AI and ML for data analytics and decision‐making at the edge, optimising IoT applications.

*Advanced Security*: Given the sensitive nature of IoT data, 6G's security features will provide robust protection against cyber threats and vulnerabilities, ensuring data integrity and privacy.

*Global Coverage*: 6G's infrastructure aims to extend coverage to remote and challenging environments, facilitating IoT deployments in previously inaccessible areas.

*Dynamic Resource Allocation*: 6G will allocate network resources dynamically, allowing IoT devices to efficiently use available bandwidth and minimising interference.

*Multi‐Modal Connectivity*: 6G supports multiple communication technologies, such as cellular, satellite, and short‐ range wireless, providing diverse connectivity options for IoT devices.

*Smart Cities and Urban IoT*: 6G can power smart city initiatives by supporting various applications like smart traffic management, waste management, environmental monitoring, and more.

*Industrial IoT (IIoT)*: 6G's reliability, low latency, and high data rates make it well‐suited for industrial automation and BHIDE ET AL. - **19 of 23**

control, enabling safer and more efficient manufacturing processes.

Overall, the IoT infrastructure in 6G communication is designed to unlock the full potential of IoT applications across industries, offering improved connectivity, data handling, responsiveness, and scalability for a connected and intelligent future.

### *Edge infrastructure*

The edge infrastructure in [[46](#page-22-0)] 6G communication refers to the distributed computing and networking resources located closer to the data source or end‐users. This infrastructure plays a crucial role in reducing latency, improving application performance, and enabling new services. Here's an overview of the edge infrastructure in 6G:

*Multi‐Access Edge Computing*: MEC is a key component of 6G's edge infrastructure. It involves deploying computing resources, such as servers and storage, at the edge of the network, closer to users and IoT devices. This enables faster data processing, real‐time analytics, and reduced latency for applications.

*Ultra‐Low Latency*: 6G's edge infrastructure aims to provide ultra‐low latency connectivity, allowing applications that require instant responses, such as autonomous vehicles and AR, to function seamlessly.

*Decentralised Data Processing*: Edge infrastructure distributes data processing tasks across edge nodes, reducing the need to transmit all data to centralised data centres. This enhances efficiency and reduces network congestion.

*Real‐Time Decision‐Making*: Edge computing enables applications to make critical decisions in real time, as data is processed locally rather than being sent to distant servers. This is essential for time‐sensitive applications.

*Improved Bandwidth Efficiency*: By offloading data processing and analytics to edge nodes, the edge infrastructure helps conserve network bandwidth, as only relevant data or summarised results are transmitted to the core.

*Content Delivery and Caching*: Edge nodes can store and deliver content more efficiently, reducing latency and congestion. Context‐aware caching at the edge further optimises content delivery.

*Privacy and Data Localisation*: Edge infrastructure allows sensitive data to be processed locally, enhancing privacy by reducing the need to transmit sensitive information across the network.

*AI at the Edge*: 6G's edge infrastructure supports AI and ML processing at the edge, enabling faster insights and responses without relying on centralised data centres.

*IoT Support*: Edge infrastructure is critical for handling the massive volume of data generated by IoT devices. It enables real‐time data analysis and event‐triggered actions [\[47\]](#page-22-0).

*Network Slicing*: Edge nodes can be partitioned using network slicing, creating virtualised environments tailored to different applications' needs, thus optimising resources and QoS.

*Robust Connectivity*: Edge infrastructure provides connectivity redundancy, ensuring continuous service availability even in cases of core network disruptions.

*Smart Services*: With edge infrastructure, services like smart traffic management, energy optimisation, and healthcare applications can be deployed and executed efficiently in real time.

*Local Data Processing*: Certain applications require processing data close to the source due to privacy concerns or regulatory requirements. Edge infrastructure supports such scenarios.

*Emerging Use Cases*: 6G's edge infrastructure will support emerging use cases such as tactile Internet, haptic communication [\[48\]](#page-22-0), and advanced AR/VR experiences.

Overall, the edge infrastructure in 6G communication is designed to complement traditional cloud computing by bringing computing resources closer to users and data sources. This architecture enhances performance, responsiveness, and scalability for a wide range of applications in the evolving digital landscape.

#### *Cloud infrastructure*

The cloud infrastructure in 6G communication continues to play a vital role in providing centralised computing resources and services to support various applications and services. While edge computing and distributed resources are becoming more prominent in 6G, cloud infrastructure remains a crucial component. Here's how the cloud infrastructure functions in the context of 6G communication:

*Centralised Resources*: Cloud infrastructure in 6G consists of data centres and servers that store and process large volumes of data, providing computing power, storage, and networking resources for various applications.

*Data Storage and Processing*: Cloud infrastructure is ideal for handling massive datasets that don't require real‐time processing. Applications such as big data analytics and historical trend analysis benefit from cloud‐based resources.

*Complex Computing*: Applications that require complex simulations, modelling, and computations may leverage the extensive processing capabilities of the cloud infrastructure.

*Global Accessibility*: Cloud resources are accessible from anywhere with an Internet connection, making it easy for users and devices to access and interact with applications and data.

*Application Scalability*: Cloud infrastructure supports elastic scaling, allowing applications to quickly adapt to changes in demand by provisioning or releasing resources as needed.

*Resource Optimisation*: Hybrid cloud models, which combine both cloud and edge resources, enable applications to dynamically allocate resources based on workload demands and latency requirements.

*AI and ML*: The cloud infrastructure provides an environment conducive to training and deploying AI and ML models, enabling advanced analytics and insights.

*Disaster Recovery*: Cloud‐based backup and disaster recovery services ensure data redundancy and business continuity in case of system failures or disasters.

*Global Services*: Services like online streaming, cloud gaming, and video conferencing can utilise cloud infrastructure to provide consistent and high‐quality experiences to users across the globe.

*Application Deployment*: Developers can easily deploy applications to the cloud, reducing the need for managing complex hardware infrastructure and accelerating time‐to‐ market.

*Resource Sharing*: Multiple users and applications can share cloud resources, optimising hardware utilisation and reducing costs.

*Updates and Maintenance*: Cloud providers handle software updates, security patches, and maintenance, relieving users from the burden of managing infrastructure.

*Collaborative Work*: Cloud infrastructure facilitates collaborative work by allowing multiple users to access and collaborate on shared documents, projects, and applications.

*Flexible Billing Models*: Cloud services often offer pay‐as‐ you‐go or subscription‐based pricing, allowing organisations to scale their usage and expenses as needed.

While edge infrastructure brings computing resources closer to the data source, the cloud infrastructure complements it by offering scalable resources for applications that require extensive computing power, storage, and global accessibility. In 6G communication, a combination of both edge and cloud resources forms a versatile ecosystem that caters to a wide range of application needs.

### 4.4.5 | 6G network layer

CHANNEL ESTIMATION: The 6G network's channel estimation involves advanced techniques to accurately predict wireless signal behaviour, given its complex and dynamic nature. It's likely to use a combination of ML, massive MIMO, and beamforming technologies to enhance signal quality, reduce interference, and improve overall network performance.

MODULATION RECOGNITION: In the context of the 6G network, modulation recognition within the network layer refers to the ability to identify the modulation scheme used by different devices or signals in the network. This is crucial for optimising resource allocation and ensuring efficient communication. Advanced ML algorithms, such as deep learning models, might be employed to recognise and adapt to various modulation schemes, including traditional ones like Quadrature Amplitude Modulation and more innovative techniques that could emerge in 6G.

NETWORK TRAFFIC CLASSIFICATION: In the 6G network, network traffic classification at the network layer involves identifying and categorising different types of traffic flows based on their characteristics. This enables efficient resource allocation, QoS management, and traffic optimisation. Machine learning techniques, including deep learning and pattern recognition, could be employed to accurately classify traffic into categories such as video streaming, IoT data, voice calls, and more, allowing the network to prioritise and handle different types of traffic effectively.

NETWORK TRAFFIC PREDICTION: In the 6G network, network traffic prediction involves forecasting the future behaviour of network traffic based on historical patterns, user behaviour, and other relevant data. This prediction is essential for proactive resource allocation, load balancing, and ensuring efficient network operation. Machine learning techniques, like time series analysis and deep learning models, could be utilised to analyse past traffic patterns and predict future trends. By accurately predicting traffic spikes, shifts, and usage patterns, the network can adapt in real‐time to meet demands, optimise resource allocation, and enhance overall performance.

INTELLIGENT ROUTING: Intelligent routing in the 6G network layer involves using advanced algorithms and technologies to dynamically determine the best paths for data to travel between source and destination. This routing takes into account factors such as network congestion, latency, available bandwidth, and QoS requirements. Machine learning and AI‐ driven approaches could play a significant role in making routing decisions based on real‐time data analysis and predictive modelling. This helps ensure efficient data transmission, reduced latency, and optimised network performance in the evolving 6G landscape.

RADIO RESOURCE MANAGEMENT: In the 6G network layer, radio resource management (RRM) focuses on efficiently allocating and managing the limited radio spectrum resources to ensure optimal performance and QoS. Advanced techniques, such as ML, AI, and network automation, may be employed to enhance RRM. These technologies enable dynamic spectrum sharing, adaptive modulation and coding, beamforming, and interference management. The goal is to achieve improved spectral efficiency, reduced latency, and seamless connectivity while catering to the diverse communication needs of various applications and devices in the 6G ecosystem.

NETWORK FAULT MANAGEMENT: In the 6G network, network fault management involves detecting, diagnosing, and resolving network anomalies, disruptions, or failures to ensure uninterrupted service. This is crucial for maintaining high reliability and availability. Advanced techniques like AI‐driven analytics, predictive maintenance, and automated recovery processes may be utilised. These technologies help identify potential issues before they cause major problems, enabling faster response times and minimising service disruptions. Additionally, self‐healing mechanisms and resilient network designs could be implemented to quickly recover from faults and maintain seamless connectivity in the evolving 6G environment.

MOBILITY MANAGEMENT: In the context of the 6G network, mobility management refers to the strategies and mechanisms employed to enable seamless connectivity as devices move across different network cells or areas. With the proliferation of IoT devices and diverse mobility patterns, mobility management becomes more challenging and critical. 6G could leverage advanced technologies like predictive handover, network slicing, and dynamic spectrum allocation to optimise mobility management. Machine learning and AI could BHIDE ET AL. - **21 of 23**

analyse user behaviour, device mobility patterns, and network conditions to predict when and where handovers are likely to occur. This allows for proactive resource allocation and smoother handover processes, ensuring continuous connectivity and minimising disruptions as devices move within the network.

NETWORK INTRUSION DETECTION: [[49](#page-22-0)] In the 6G network, network intrusion detection focuses on identifying and responding to unauthorised or malicious activities that could compromise the security and integrity of the network. Given the increasing complexity of attacks and the growing attack surface, advanced techniques will likely be employed. Machine learning and AI‐driven approaches could play a significant role in network intrusion detection in 6G. These technologies can analyse vast amounts of network data in real‐ time, identify patterns of abnormal behaviour, and promptly detect potential intrusions or anomalies. Additionally, the integration of behavioural analysis, anomaly detection, and signature‐based methods can provide a multi‐layered defence against a wide range of threats. This approach helps enhance the security posture of the 6G network and safeguard sensitive data and communication.

TRAFFIC ANOMALY DETECTION: In the 6G network layer, traffic anomaly detection focuses on identifying unusual or unexpected patterns in network traffic that might indicate potential security threats, performance issues, or other abnormalities. Advanced techniques, including ML and AI, will likely be utilised to enhance the accuracy and efficiency of anomaly detection. These technologies can analyse large volumes of network data and learn from historical patterns to identify deviations from the norm. By continuously monitoring network traffic, they can promptly detect unusual behaviours, such as sudden spikes in traffic, unusual communication patterns, or suspicious data flows. This enables rapid response to potential security breaches, network performance issues, and other anomalies, ensuring the overall reliability and security of the 6G network [\[50\]](#page-22-0).

NETWORK BOTNET DETECTION: In the 6G network layer, botnet detection is a critical aspect of network security aimed at identifying and mitigating the presence of botnets. Botnets are networks of compromised devices controlled by malicious actors for various illicit purposes. Advanced techniques such as ML, behavioural analysis, and AI‐driven algorithms can play a significant role in detecting botnet activities in the 6G network. These technologies can analyse network traffic, communication patterns, and device behaviours to identify signs of botnet activity. By monitoring for unusual and coordinated behaviour across a wide range of devices, the network can swiftly detect and respond to botnet‐ related threats. This helps prevent the misuse of devices and resources within the 6G network, ensuring a higher level of security and integrity.

NETWORK ENERGY OPTIMISATION: In the 6G network layer, energy optimisation focuses on reducing energy consumption while maintaining network performance and QoS. With the increasing demand for connectivity and the need to minimise environmental impact, energy‐efficient strategies become crucial. Advanced techniques like AI‐driven power management, dynamic sleep modes, and resource‐ efficient algorithms can be employed to optimise energy usage in the 6G network. Machine learning models can analyse traffic patterns, device utilisation, and network conditions to predict periods of low activity and dynamically adjust power levels accordingly. Additionally, techniques like network function virtualisation and edge computing can help distribute processing tasks efficiently, reducing the need for centralised high‐power data centres. This holistic approach helps strike a balance between providing seamless connectivity and minimising the energy footprint of the 6G network.

### **5** | **CONCLUSION**

The convergence of 6G communication architecture and AI technologies promises to reshape industries and society as a whole. While challenges like security, energy efficiency, and ethical considerations must be addressed, the potential applications and benefits in fields ranging from healthcare to smart cities demonstrate the transformative impact of this synergy. A concerted effort from researchers, policymakers, and industries will be necessary to realise the full potential of AI‐driven 6G communication architecture. In summary, the various types of 6G communication architecture incorporate technologies like AI‐driven beamforming, holographic beamforming, and quantum communication. These technologies present opportunities for applications such as autonomous systems, healthcare, smart cities, and more. However, challenges related to security, energy efficiency, interoperability, and ethics must be effectively addressed to fully harness the potential of AI‐ augmented 6G networks.

### **AUTHOR CONTRIBUTIONS**

**Pranita Bhide**: Conceptualisation; formal analysis; methodology; resources; writing—original draft. **Dhanush Shetty**: Conceptualisation; formal analysis; methodology; resources; writing—original draft. **Suresh Mikkili**: Formal analysis; funding acquisition; investigation; project administration; resources; supervision; validation; writing—review & editing.

#### **ACKNOWLEDGEMENTS**

This work was supported by grants from DST/SERB/EEQ/ 2021/294.

### **CONFLICT OF INTEREST STATEMENT**

We do not have any conflict of interest.

#### **DATA AVAILABILITY STATEMENT**

Data sharing not applicable to this article as no datasets were generated or analysed during the current study.

#### **ORCID**

*Suresh Mikkili* <https://orcid.org/0000-0002-5802-3390>

#### <span id="page-21-0"></span>**REFERENCES**

- 1. Yang, Y., et al.: 6G network AI architecture for everyone‐centric customized services. IEEE Netw., 37(5), 71–80 (2020)
- 2. Sajjad Akbar, M., et al.: 6G survey on challenges, requirements, applications, key enabling technologies, use cases, AI integration issues and security aspects (2022)
- 3. Salahdine, F., et al.: 5G, 6G, and beyond: recent advances and future challenges. Ann. Telecommun. 78(9), 525–549 (2022)
- 4. Bandi, A., et al.: A review towards AI empowered 6G communication requirements, applications, and technologies in mobile edge computing. In: Proceedings of the Sixth International Conference on Computing Methodologies and Communication (ICCMC 2022) (2022). IEEE Xplore Part Number: CFP22K25‐ART; ISBN: 978‐1‐6654‐1028‐1
- 5. Naga Srinivasu, P., et al.: 6G driven fast computational networking framework for healthcare applications. IEEE Access 10, 94235–94248 (2022)
- 6. Zaman Chowdhury, M., et al.: 6G wireless communication systems: applications, requirements, technologies, challenges, and research directions. IEEE Open J. Commun. Soc. 1(1), 957–975 (2020)
- 7. Chi, N., et al.: Visible light communication in 6G. IEEE Veh. Technol. Mag. 15(4), 93–102 (2020)
- 8. Ji, B., et al.: A survey of computational intelligence for 6G: key technologies, applications and trends. IEEE Trans. Ind. Inf. 17(10), 7145– 7154 (2021). <https://doi.org/10.1109/tii.2021.3052531>
- 9. Mao, B., et al.: AI models for green communications towards 6G. IEEE Commun. Surv. Tutor. 24(1), 210–247 (2022). [https://doi.org/10.1109/](https://doi.org/10.1109/comst.2021.3130901) [comst.2021.3130901](https://doi.org/10.1109/comst.2021.3130901)
- 10. Ahammed, T.B., et al.: A vision on the artificial intelligence for 6G communication. ICT Express 9, 197–210 (2022)
- 11. Khiadani, N., et al.: Vision, requirements and challenges of sixth generation (6G) Networks. In: 6th Iranian Conference on Signal Processing and Intelligent Systems (ICSPIS) (2020)
- 12. Guan, G., et al.: 6G: opening new horizons for integration of comfort, security, and intelligence. IEEE Wireless Commun. 27(5), 126–132 (2020). <https://doi.org/10.1109/mwc.001.1900516>
- 13. Siriwardhana, Y., et al.: AI and 6G security: opportunities and challenges. In: Joint European Conference on Networks and Communications & 6G Summit (EUCNC/6G Summit): 6G Visions (6GV), UTC (2021)
- 14. Shahjalala, Md., et al.: Enabling technologies for AI empowered 6G massive radio access networks. ICT Express 9(3), 341–355 (2023)
- 15. Chen, S., et al.: Vision, requirements, and technology trend of 6G: how to tackle the challenges of system coverage, capacity, user data‐rate and movement speed. IEEE Wireless Commun. 27(2), 218–228 (2020). <https://doi.org/10.1109/mwc.001.1900333>
- 16. Tan, J., Dai, L.: The precoding for 6G: challenges, solutions, and opportunities. IEEE Wireless Commun. 30(4), 132–138 (2023)
- 17. Arif Hossain, M., et al.: AI in 6G: energy‐efficient distributed machine learning for multilayer heterogeneous networks. IEEE Netw. 36(6), 84– 91 (2022). <https://doi.org/10.1109/mnet.104.2100422>
- 18. Al‐Ansi, A.M., Al‐Ansi, A.: An overview of artificial intelligence (AI) in 6G: types, advantages, challenges and recent applications. Bul. Ilm. Sarj. Tek. Elektro 5(1), 67–75 (2023)
- 19. Wu, W., et al.: AI‐native network slicing for 6G networks. IEEE Wireless Commun. 29(1), 96–103 (2022). [https://doi.org/10.1109/mwc.001.](https://doi.org/10.1109/mwc.001.2100338) [2100338](https://doi.org/10.1109/mwc.001.2100338)
- 20. Shen, X., et al.: Holistic network virtualization and pervasive network intelligence for 6G. IEEE Xplore, IEEE Commun. Surv. Tutor. 24(1), 1– 30 (2022). First Quarter. <https://doi.org/10.1109/comst.2021.3135829>
- 21. Kirubasri, G., et al.: A recent survey on 6G vehicular technology, applications and challenges. In: IEEE Xplore, 2021 9th International Conference on Reliability, Infocom Technologies and Optimization (Trends and Future Directions) (ICRITO), Sep 3–4. Amity University, Noida, India (2021)
- 22. Shehzad, M.K., et al.: Artificial intelligence for 6G networks. IEEE Veh. Technol. Mag. 17(3), 16–25 (2022). [https://doi.org/10.1109/mvt.2022.](https://doi.org/10.1109/mvt.2022.3164758) [3164758](https://doi.org/10.1109/mvt.2022.3164758)
- 23. Yang, H., et al.: Artificial‐intelligence‐enabled intelligent 6G networks. IEEE Netw. 34(6), 272–280 (2020). [https://doi.org/10.1109/mnet.011.](https://doi.org/10.1109/mnet.011.2000195) [2000195](https://doi.org/10.1109/mnet.011.2000195)

24. Letaief, K.B., et al.: Edge artificial intelligence for 6G: vision, enabling technologies, and applications. IEEE J. Sel. Area. Commun. 40(1), 5–36 (2022). <https://doi.org/10.1109/jsac.2021.3126076>

- 25. Ji, B., et al.: Several key technologies for 6G: challenges and opportunities. IEEE Commun. Stand. Mag. 5(2), 44–51 (2021). [https://doi.org/](https://doi.org/10.1109/mcomstd.001.2000038) [10.1109/mcomstd.001.2000038](https://doi.org/10.1109/mcomstd.001.2000038)
- 26. Feng, Z., et al.: Joint communication, sensing, and computation enabled 6G intelligent machine system. IEEE Netw. 35(6), 34–42 (2021). [https://](https://doi.org/10.1109/mnet.121.2100320) [doi.org/10.1109/mnet.121.2100320](https://doi.org/10.1109/mnet.121.2100320)
- 27. Cui, M., et al.: Near‐field MIMO communications for 6G: fundamentals, challenges, potentials, and future directions. IEEE Commun. Mag. 61(1), 40–46 (2023). <https://doi.org/10.1109/mcom.004.2200136>
- 28. Ziegler, V., et al.: Security and trust in the 6G era. IEEE Access 9, 142314–142327 (2021). <https://doi.org/10.1109/access.2021.3120143>
- 29. Salahdine, F., et al.: 5G, 6G, and beyond: recent advances and future challenges. Ann. Telecommun. 78, 525–549 (2022)
- 30. Wang, M., et al.: Security and privacy in 6G networks: new areas and new challenges. ScienceDirect, Digital Commun. Netw. 6(3), 281–291 (2020). <https://doi.org/10.1016/j.dcan.2020.07.003>
- 31. Ali, S., et al.: Research article new trends and advancement in next generation mobile wireless communication (6G): a survey. Wireless Commun. Mobile Comput. 2021, 9614520 (2021)
- 32. Alraih, S., et al.: Revolution or evolution? Technical requirements and considerations toward 6G mobile communications. Sensors 22(3), 762 (2022)
- 33. Wen, T., Ye Li, G.: Nine challenges in artificial intelligence and wireless communications for 6G. IEEE Wireless Commun. 29(4), 140–145 (2022). <https://doi.org/10.1109/mwc.006.2100543>
- 34. Junaid Nawaz, S., et al.: Quantum machine learning for 6G communication networks: state of the art and vision for the future. IEEE Access 7, 46317–46350 (2019). [https://doi.org/10.1109/access.2019.](https://doi.org/10.1109/access.2019.2909490) [2909490](https://doi.org/10.1109/access.2019.2909490)
- 35. Yuan, Y., et al.: Potential key technologies for 6G mobile communications. Sci. China Inf. Sci. Cross Mark 63(8), 183301 (2020). [https://doi.](https://doi.org/10.1007/s11432-019-2789-y) [org/10.1007/s11432](https://doi.org/10.1007/s11432-019-2789-y)‐019‐2789‐y
- 36. Abdel Hakeem, S.A., et al.: Security requirements and challenges of 6G technologies and applications. Sensors 22(5), 1969 (2022). [https://doi.](https://doi.org/10.3390/s22051969) [org/10.3390/s22051969](https://doi.org/10.3390/s22051969)
- 37. Hong, H., et al.: Radar–communication integration for 6G massive IoT services. IEEE Internet Things J. 9(16), 14511–14520 (2022). [https://](https://doi.org/10.1109/jiot.2021.3064072) [doi.org/10.1109/jiot.2021.3064072](https://doi.org/10.1109/jiot.2021.3064072)
- 38. Ismail, L., Buyya, R.: Artificial intelligence applications and self‐learning 6G networks for smart cities digital ecosystems: taxonomy, challenges, and future directions. Sensors 22(15), 5750 (2022). [https://doi.org/10.](https://doi.org/10.3390/s22155750) [3390/s22155750](https://doi.org/10.3390/s22155750)
- 39. Saad, W., et al.: A vision of 6G wireless systems: applications, trends, technologies, and open research problems. IEEE Netw. 34(3), 134–142 (2020). IEEE Network May/June. [https://doi.org/10.1109/mnet.001.](https://doi.org/10.1109/mnet.001.1900287) [1900287](https://doi.org/10.1109/mnet.001.1900287)
- 40. Chergui, H., et al.: Zero‐touch AI‐driven distributed management for energy‐efficient 6G massive network slicing. IEEE Netw. 35(6), 43–49 (2021). <https://doi.org/10.1109/mnet.111.2100322>
- 41. Aslam, M.M., et al.: Research article sixth generation (6G) cognitive radio network (CRN) application, requirements, security issues, and key challenges. Wireless Commun. Mobile Comput. 2021(1), 1331428 (2021)
- 42. You, X., et al.: Toward 6G Tkmicro extreme connectivity: architecture, key technologies and experiments. IEEE Wireless Commun. 30(3), 86– 95 (2023)
- 43. Hu, J., et al.: UAV‐assisted vehicular edge computing for the 6G internet of vehicles: architecture, intelligence, and challenges. IEEE Commun. Stand. Mag. 5(2), 12–18 (2021). [https://doi.org/10.1109/mcomstd.001.](https://doi.org/10.1109/mcomstd.001.2000017) [2000017](https://doi.org/10.1109/mcomstd.001.2000017)
- 44. Zeeshan Asghar, M., et al.: Article evolution of wireless communication to 6G: potential applications and research directions. Sustainability 14(10), 6356 (2022)
- 45. Wang, M., et al.: Transfer learning promotes 6G wireless communications: recent advances and future challenges. IEEE Trans. Reliab. 70(2), 790–807 (2021). <https://doi.org/10.1109/tr.2021.3062045>

26328925, 2025, 1, Downloaded from https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/qtc2.12114 by University Of Sao Paulo - Brazil, Wiley Online Library on [25/08/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<span id="page-22-0"></span>BHIDE ET AL. - **23 of 23**

46. Krishna Prasad, K., Aithal, P.S.: Changing perspectives of mobile information communication technologies towards customized and secured services through 5G & 6G. Int. J. Eng. Res. Mod. Educ. I(II), 210–224 (2016)

- 47. Letaief, K.B., et al.: The roadmap to 6G: AI empowered wireless networks. IEEE Commun. Mag. 57(8), 84–90 (2019). [https://doi.org/10.](https://doi.org/10.1109/mcom.2019.1900271) [1109/mcom.2019.1900271](https://doi.org/10.1109/mcom.2019.1900271)
- 48. Kato, N., et al.: Ten challenges in advancing machine learning technologies toward 6G. IEEE Wireless Commun. 27(3), 96–103 (2020). <https://doi.org/10.1109/mwc.001.1900476>
- 49. Wang, C.‐X., et al.: On the road to 6G: visions, requirements, key technologies, and testbeds. IEEE Commun. Surv. Tutor. 25(2), 905–974 (2023). <https://doi.org/10.1109/comst.2023.3249835>

50. Porambage, P., et al.: The roadmap to 6G security and privacy. IEEE Commun. Soc. 2, 1094–1122 (2021). [https://doi.org/10.1109/ojcoms.](https://doi.org/10.1109/ojcoms.2021.3078081) [2021.3078081](https://doi.org/10.1109/ojcoms.2021.3078081)

**How to cite this article:** Bhide, P., Shetty, D., Mikkili, S.: Review on 6G communication and its architecture, technologies included, challenges, security challenges and requirements, applications, with respect to AI domain. IET Quant. Comm. e12114 (2025). [https://](https://doi.org/10.1049/qtc2.12114) [doi.org/10.1049/qtc2.12114](https://doi.org/10.1049/qtc2.12114)
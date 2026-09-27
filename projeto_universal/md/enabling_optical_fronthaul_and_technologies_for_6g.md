---
title: "Enabling Optical Fronthaul and Technologies for 6G Networks: Principles, Recent Contributions, Concerns, and AI Role"
tema_principal: projeto_universal
temas_relacionados: []
ano: null
autores: []
veiculo: null
pdf: ../pdf/enabling_optical_fronthaul_and_technologies_for_6g.pdf
---

![](_page_0_Picture_1.jpeg)

Date of publication xxxx 00, 0000, date of current version xxxx 00, 0000.

*Digital Object Identifier 10.1109/ACCESS.2024.Doi Number*

# **Enabling Optical Fronthaul and Technologies for 6G Networks: Principles, Recent Contributions, Concerns, and AI Role**

**Sallar S. Murad1, Zainab Abdullah Jasim1, Mohammad D. Soltani1, , Rozin Badeel1, Salman Yussof2, Bha-Aldan M. Oraibi3**

1 Research and Development Division, BEAMBRIDGE LIMITED, Sutton SM1 4DG, UK

Corresponding author: Bha-Aldan M. Oraibi (e-mail: bha.aldan@unitar.my).

**ABSTRACT** A new age of technological and application improvements is about to dawn with the expected debut of Sixth Generation (6G) mobile technology by 2030. This launch will be a watershed moment in the history of wireless communication. There will supposedly be three-dimensional coverage for all things, everywhere, and at all times with 6G's ultra-high data speeds and nearly instantaneous communications. The 6G Radio Access Network (RAN)'s fronthaul links the pool of digital units (DUs) with the geographically distributed Remote Units (RUs). However, optical technologies continue to play a fundamental role in enabling 6G fronthaul, since they provide high-speed, low-latency, and reliable transmission that are needed to fulfil the required standards of 6G. This study is reviewing the fifth generation (5G) and the 6G optical fronthaul, which is describing the current research progress and discusses the important of 6G fronthaul technologies and system designs, It also covers the possible uses of each optical technology and their advantages in 6G fronthaul networks and the impact of the Artificial Intelligent (AI) on them. In order to help researchers and industry experts build future wireless networks that are both strong and efficient, this study seeks to provide a thorough overview of 6G optical fronthaul technologies and explore the future research and their current role in the area.

**INDEX TERMS** Optical fronthaul, 6G, FSO, LiFi, optical networks, artificial intelligence.

### **I. INTRODUCTION**

Recently, especially during the COVID-19 pandemic, communication networks have gained paramount significance across all domains of our lives, including healthcare, innovative manufacturing, online education, and smart cities [1], [2], [3]. The quantity of devices connected to the Internet is anticipated to increase markedly each year, resulting in a considerable rise in traffic volumes managed by mobile networks [4]. By 2030, it is anticipated that these networks would manage a minimum of 5000 Exabytes of data monthly, while worldwide data traffic is expected to surpass 3 Zetabytes [5]. In the last forty years, communication technologies have continually evolved to meet the shifting needs of users. The progression of wireless mobile networks has been especially remarkable, evolving through consecutive generations. Every new generation has brought significant advancements, demonstrating the unyielding speed of invention in this domain.

Progressing from the First Generation (1G) to the contemporary 5G. This progress has been propelled by the escalating need for low-latency and high-capacity wireless communication services [6]. The latest advances in 6G networks, including network softwarization, virtualization, large-scale Multiple-Input-Multiple-Output (MIMO) systems, ultra-dense device deployment, and the adoption of new frequency bands, has yielded significant benefits across multiple sectors. These developments have benefitted commercial providers, academic research institutions, standards

Informatics & Computing in Energy, University Tenaga Nasional, Kajang 43000, Malaysia

<sup>3</sup> Faculty of Business, UNITAR International University, Petaling Jaya 47301, Malaysia

![](_page_1_Picture_1.jpeg)

![](_page_1_Figure_2.jpeg)

**FIGURE 1. Main applications supported by 5G.**

bodies, and most importantly, end-users. 5G signifies a major advancement over prior mobile network generations, as it addresses contemporary communication requirements across a diverse array of use cases in three primary application domains, as shown in **Figure 1**.

Although 5G has profoundly transformed connectivity, the burgeoning interest in 6G mobile technology arises from persistent drive for superior technological advancements in wireless communication. The relentless pursuit of faster, more reliable, and pervasive connectivity has driven researchers, industries, and policy makers to explore the next frontier. 6G is anticipated to surpass the capabilities of its predecessor, providing unprecedented data speeds, ultra-low delay, and seamless integration with emerging technologies such as Artificial Intelligence (AI), Extended Reality (XR), the Internet of Everything (IoE), and holographic communications, which cannot be sufficiently accommodated by 5G. Such paradigm shift is not merely an incremental enhancement but a substantial leap in the field of wireless communication. As society grows more reliant on digital connectivity, the promise of 6G lies in its potential to redefine possibilities, facilitating unprecedented innovation and reshaping our modes of living, working, and engaging with the world [7]. **Figure 2** depicts the expected principal use cases for 6G, including a diverse array of applications.

Prominent telecommunications companies, such as Samsung Research [8], and Huawei [9], have recently articulated their visions for the future of 6G. Several ongoing projects are aimed at developing long-term strategic plans for 6G [10]. This transition is further reinforced by the advancement of RAN, leading to the emergence of Open RAN (O-RAN). O-RAN, increasingly recognized as key paradigm for both existing 5G and future 6G systems, exemplifies openness, accessibility, and interoperability that overcome vendor-specific limitations and proprietary technologies. This multi-vendor approach enhances performance and efficiency while reducing cost, hence promoting an environment that is conducive for innovation [11], [12].

In the evolving landscape of 5G and 6G networks, a critical challenge emerges in implementing an effective fronthaul architecture within the O-RAN framework. Fronthaul refers to the high-speed connections linking baseband processing operations in the DU or Baseband Unit (BBU) to remote RUs at the cell site, serving as a crucial component in this architectural framework. Recognizing an efficient fronthaul is essential for harnessing the complete capabilities of O-RAN within the framework of 5G and 6G networks. The fronthaul portion can be executed via either wireless (microwave and millimeter wave) or optical (optical fiber and free-space optics) technology. Wireless communications systems up to the Fourth Generation (4G), face substantial limitations including inadequate capacity to support forthcoming 5G/6G high-bandwidth applications, restricted spectrum availability, increasing interference, and stringent regulation constraints [11].

Optical technologies are widely recognized as the most sustainable solutions for managing 5G and future wireless network generations. Optical fiber, with its superior bandwidth, dependability, security, versatility, and costefficiency [13], is seen as an exceptionally appropriate option for 6G fronthaul. It provides not only excellent dependability and security but also facilitates long-distance transmission. At the same time, Free Space Optics (FSO), which employs lasers for aerial data transmission, offers a cost-effective alternative to optical fiber in specific scenarios, such as remote locations, temporary deployments, and environments with physical obstructions. Collectively, these optical technologies are expected to play a pivotal role in advancing wireless communication infrastructure, ensuring the requirements of forthcoming high-bandwidth applications in 5G and 6G can be effectively supported.

![](_page_2_Picture_1.jpeg)

![](_page_2_Figure_2.jpeg)

**FIGURE 2. The expected use cases of 6G.**

The purpose of this survey is to examine 6G optical fronthaul, as well as the enabling solutions and emerging research directions. The critical role of fronthaul in the architecture of future wireless communications systems motivated the selection of this topic as the focus of our study. There is also a shortage of comparative works that comprehensively address the diverse perspective on optical fronthaul for 6G networks within the currently available literature.

In the development of next-generation wireless network technologies, optical fronthaul is expected to play an important role. Furthermore, the research area focusing on the development of optical fronthaul for mobile networks is rapidly expanding, with new technologies and standards continuously being integrated. Therefore, there is a strong need for a comprehensive and up-to-date survey that reviews state-of-the-art optical fronthaul solutions for 6G networks.

This work focuses on the fronthaul segment of nextgeneration wireless networks, where stringent performance requirements are imposed by both 5G and emerging 6G systems. In 5G, fronthaul links are expected to support high data rates (typically in the range of 10-25 Gbps per link), ultra-low latency (sub-100 μs), tight synchronization, and high reliability. These requirements are further intensified in 6G, where projected use cases demand Tbps-level capacity, sub-millisecond end-to-end latency, enhanced scalability, and support for AI-driven and ultra-dense network architectures. To meet these requirements, a range of optical and optical-wireless technologies have been investigated. Fiber-based solutions, such as passive optical networks (PON) and wavelength-division multiplexing (WDM), offer high capacity, low latency, and robustness, making them suitable for dense urban deployments. However, their deployment cost and lack of flexibility in certain scenarios motivate the exploration of complementary solutions. Optical wireless communication (OWC), including free-space optics (FSO) and visible light communication (VLC)/LiFi, provides high bandwidth, low interference, and rapid deployment capabilities, making it a promising candidate for flexible and cost-effective fronthaul solutions. Accordingly, this paper narrows its scope to these technologies, aiming to evaluate their suitability in meeting the evolving requirements of 5G and 6G networks.

Unlike existing survey papers that primarily focus on general 6G visions, optical access networks, or isolated optical wireless communication technologies, this work provides a unified and comprehensive review of optical fronthaul solutions for future 5G and 6G systems. The paper jointly investigates fiber-based fronthaul technologies, optical wireless solutions such as Free Space Optics (FSO) and LiFi/VLC, and hybrid optical-wireless architectures within a common framework. In addition, the survey connects these technologies with the evolution of modern RAN architectures, including D-RAN, C-RAN, HC-RAN, F-RAN, vRAN, and O-RAN, highlighting how the fronthaul requirements evolve toward ultra-dense, lowlatency, and AI-driven 6G systems.

Another distinguishing aspect of this survey is the inclusion of analytical modeling for optical wireless fronthaul links. Unlike conventional survey papers that mainly provide qualitative discussions, this work presents analytical formulations for LOS/NLOS optical channel gain, atmospheric attenuation effects, and signal-to-noise ratio analysis in LiFi- and FSO-based fronthaul systems. This enables a deeper understanding of the performance

![](_page_3_Picture_1.jpeg)

limitations and design considerations associated with optical wireless fronthaul deployment in future networks.

Furthermore, the paper provides a dedicated discussion on the role of Artificial Intelligence (AI) and Machine Learning (ML) in enabling intelligent optical fronthaul systems for 5G and 6G networks. The survey examines AIdriven traffic forecasting, adaptive PHY-layer optimization, beam management, predictive maintenance, security and anomaly detection, and intelligent hybrid-link orchestration. In addition, multiple comparative analysis tables are presented to systematically compare recent studies on optical, PON-based, LiFi-based, and hybrid optical wireless fronthaul systems according to architecture type, implementation method, integration strategy, deployment scenario, and performance metrics. Therefore, this survey aims to provide a holistic, up-to-date, and crossdisciplinary reference for researchers and practitioners working on next-generation optical fronthaul technologies.

The rest of the paper is organized as follows: Section 2 provides an overview of 6G evolution, addressing key difficulties and the RAN landscape. Section 3 discusses various technologies for the optical fronthaul of 5G/6G and related concerns. Section 4 provides analytical modelling of optical wireless fronthaul links. Section 5 explores recent contributions of optical wireless and optical fronthaul technologies for 5G/6G. Section 6 discusses how AI will contribute to the fronthaul and optical technologies. Section 7 presents a comparison of the technologies under consideration. Section 8 concludes the manuscript with a brief discussion of future research directions.

### **II. 6G EVOLUTION**

### *A. From 5G to 6G*

This section provides a concise overview of the evolution of wireless mobile network features from 1G to the anticipated 6G. The 1G, introduced in the 1980s, provided basic analog voice communication but was limited in capacity and lacked data support. The Second Generation (2G), emerging in the 1990s, improved call quality and introduced Short Message Services (SMS) along with minimal internet browsing capability. Third Generation (3G) marked a significant advancement by enabling mobile Internet, video conferencing, and interactive messaging [14].

5G has a long developmental history that began in the early 2010s. In contrast to earlier generations, 5G signifies a substantial advancement, designed to meet diverse communication requirements across three principal categories [15], Ultra-Reliable Low-Latency Communications (uRLLC) supports mission-critical applications including autonomous vehicles, unmanned aerial vehicles, industrial automation, and remote medical services. uRLLC ensures immediate and dependable data transmission with exceptionally low delay. Enhanced Mobile BroadBand (eMBB) provides support for bandwidth-intensive applications such as high-definition video, three-dimensional video, cloud computing workloads, and augmented/virtual reality. Massive Machine-To-Machine Communications (mMTC) enables wide-scale device connectivity, supporting applications such as smart homes, buildings, cities, and Internet of thing (IoT).

5G connection speeds can reach up to 20 Gbps for static users and multi-Gbps for mobile devices, with end-to-end transmission latency as low as 1 millisecond. 5G utilizes both conventional sub-6 GHz frequency bands as well as higher mmWave bands, offering bandwidths ranging from tens of megahertz to several gigahertz. 5G applications include high-speed portable internet connectivity, virtual and augmented reality, driverless vehicles, smart cities, and the IoTs. Emerging 6G applications would inevitably require more stringent Quality of Service (QoS) standards than those of 5G networks. Reliable 6G networks can support a wide range of applications such as in cloud computing [16], education [17], [18], and e-government services [19].

The early stage of 6G is referred to in the literature as 5G+ and Beyond 5G (B5G). Future 6G systems are expected to deliver comprehensive 3D coverage across terrestrial, aerial, space, and maritime domains, extending connectivity to remote and underserved regions. This capability will enable truly ubiquitous communication that is accessible anytime and anywhere. Furthermore, new specifications and technologies are expected to arrive in the near future, including advanced man-machine interfaces, universal computation distribution, data fusion, mixed reality, precise sensing and control, along with extensive and scalable connectivity [20], [21].

#### *B. 6G Main Challenges*

The transition to 6G will pose numerous challenges for both academia and industry, particularly in the radio and transport layers. In the radio layer, meeting the demands of bandwidth-intensive applications will require the utilization of previously untapped frequency ranges, including the 7 GHz to 20 GHz band, mmWave bands, the sub-terahertz range of 100 GHz–300 GHz for short-range applications, and the terahertz spectrum spanning from 100 GHz to 10 THz [22], [23]. At the transport layer (which comprises of fronthaul, midhaul, and backhaul), there is a strong need for robust, ultra-high-capacity, and ultra-low latency transport networks that extends from the cellular edge to the core of the network [24], [25]. The Metaverse mandates stringent criteria for 6G regarding communication and networking [25].

The increasing density of network interconnections may promote the utilization of shared connections rather than the traditional P2P linkages, thereby reducing both installation and administration costs in 6G networks [26].

![](_page_4_Figure_2.jpeg)

![](_page_4_Figure_3.jpeg)

**FIGURE 3. UAVs and Cellular networks: (a) drones and pilots at different altitudes, and (b) different stations for different altitudes.**

Moreover, as 6G is anticipated to deliver connectivity at a three-dimensional scale, a space-earth integration network is required, utilizing stratospheric terminal base stations and Low Earth Orbit (LEO) satellites to ensure comprehensive coverage in remote regions [27]. This approach may open new opportunities for emerging transport technologies, including FSO [28].

Industrial applications and future transportation systems that rely on automated vehicles and their integration with intelligent infrastructure and associated services (such as emergency traffic management, data dissemination, and route planning) in remote areas require Critical Machine-Type Communications (cMTC), which in turn depend on Ultra-Reliable Low-Latency Communications (uRLLC). This need will intensify as automation in future mobility, for both goods and individuals, increases and drives the demand for dependable machine-type communication.

Unmanned Aerial Vehicle (UAV) communication has recently attracted significant attention within the context of 6G research [29], [30], [31]. Cellular systems, particularly 6G, can support airborne UAVs by providing extensive, cost-effective, and reliable wireless communication. However, current cellular architectures are primarily optimized for serving user equipment (UE) located near the ground. **Figure 3(a)** illustrates various UAVs and piloted aircraft operating at different altitudes with Cellular networks, while **Figure 3(b)** highlights the role of Geostationary Earth Orbit (GEO) satellites, Low Earth Orbit (LEO) satellites, High-Altitude Platforms (HAPs), and UAVs in enabling multi-layered connectivity.

Furthermore, the integration of AI and Machine Learning (ML) in both the radio and transport layers is essential for realizing intelligent 6G networks [32]. Conventional optimization methods may prove inadequate, given the anticipated dynamism and complexity of 6G due to its scale, density, and heterogeneity. Modeling such systems is extremely challenging, if not infeasible without advanced AI‑driven approaches. Consequently, conventional optimization methods that rely heavily on mathematically convenient models will become insufficient [33].

However, in the complex 6G network environment, establishing clear relationships between decisions and their impact on physical systems is both costly and often analytically intractable. Advancements in Artificial Intelligent (AI), such as Deep Reinforcement Learning (DRL), enable decision-makers to create a feedback loop with physical systems, allowing actions to be continuously refined based on system responses to achieve optimal outcomes.

The 6G technology will facilitate AI-enabled apps on edge mobile devices by leveraging enhanced wireless communications and mobile processing capabilities. Certain AI apps require data to be stored locally on mobile devices rather being uploaded to the cloud for model training in order to preserve privacy. This has motivated research works on on-device distributed training. Ondevice shared computing combines mobile device computation and storage resources to get around edge device resource constraints. Data scrambling plays a crucial role in securely sharing intermediate results among devices [34].

The variety of cloud, edge, and end-user devices create a diverse computing environment for Deep Neural Network (DNN) learning and interpretation. Addressing the challenges of 6G will be a key driver of innovation and research in the coming decade. **Figure 4** shows a summary of this section and lessons learned.

![](_page_5_Figure_2.jpeg)

**FIGURE 4. Summary of sections A and B showing lessons learned.**

### **III. EVOLUTION OF RAN TO O-RAN**

The development of RAN has been an ongoing endeavor focused on enhancing performance, expanding reach and size, and minimizing delay and deployment costs across each generation of mobile technologies, from 1G to 6G [35], [36], [37]. Different architectures of RAN are explained and discussed below.

### 1) Distributed RAN (D-RAN)

The initial generation of RAN systems situated the BBU and Remote Radio Head (RRH) at the cell site. RRHs transmit wireless signals to end users, whereas BBUs manage baseband. The architecture requires a fast backhaul network between the BBU and principal network [35]. D-RAN architecture [35], [38] predominated in wireless generations up to 4G. However, it is too expensive and inflexible to support network slicing and edge computing. Thus, it is inappropriate for 5G and 6G. A typical D-RAN is shown in **Figure 5**.

![](_page_5_Figure_8.jpeg)

**FIGURE 5. The conventional D-RAN architecture features a separation between RRHs and BBUs, with each RRH linked to its own dedicated BBU via fronthaul.**

**Figure 6** shows that radio and signal handling units differ in traditional macro base stations. The RF-only RRH connects directly to the end-user. RRHs provide In-phase and Quadrature (IQ) signals to their BBUs over a transport network using the Common Protocol Radio Interface (CPRI) [39], [40]. For the fronthaul, the RRH and BBU can be connected via optical fiber or microwave technology. When BBU and RRH are 40 km apart in the same network, processing and propagation might be delayed [40]. The D-RAN is an effective 3G and 4G RAN solution. It cannot grow or manage 5G's high bandwidth, low latency, and cost-effective services.

### 2) Centralized RAN (C-RAN)

Developed to fix D-RAN's flaws. All BBUs are in one C-RAN pool. In **Figure 6(a)**, a backhaul link connects this BBU pool to the main network, and a high-capacity fronthaul network connects it to RRHs across the service region [38]. Enhanced Inter-Cell Interference Cancellation (eICIC), Carrier Aggregation (CA), and Coordinated Multi-Point (CoMP) RSP techniques work with C-RAN framework [38]. These techniques eliminate tier-to-tier interference, improving network performance and user experience. This reduces the cost of setting up and maintaining several RAN sites. This grouping optimizes resource allocation, maximizing network capacity and spectrum [35]. Because C-RAN requires high-speed fronthaul links to provide ongoing BBU pool-RRH communication [41], it has budgetary and infrastructural challenges .

According to [42], C-RAN is suitable for 5G and networks beyond cellular networks due to its benefits. **Figure 6(b)** shows that C-RAN decouples all BBUs from their RRHs and consolidates them into a cloud-based, shared, and virtualized BBU pool. All RRHs have fronthaul connections to their BBU pools.

All BBU pools have backhaul connections to the core network and can hold several RRHs. Easily expanding network coverage, upgrading network capacity, facilitating multi-standard operation, improving network resource sharing, and supporting multi-cell collaborative signal processing are all benefits of fully centralized C-RAN (**Figure 6(c)**). Despite these benefits, fully centralized C-RAN faces two fundamental challenges [38]: increased bandwidth and baseband I/Q signal transmission between the RRH and BBU. See **Figure 6(d)** for a partially centralized C-RAN, where the RRH handles radio and baseband processing while the BBU handles high-layer activities. The RRH houses L1 functions, whereas the BBU houses L2 and L3. As baseband processing is shifted from the BBU to the RRH, partially centralized C-RAN requires minimum transmission bandwidth. However, network enhancing flexibility and multi-cell collaborative signal processing are hampered.

![](_page_6_Picture_1.jpeg)

![](_page_6_Figure_2.jpeg)

**FIGURE 6. Illustration of the C-RAN [35], [38], [40], [41]: (a) C-RAN architecture with different types of fronthaul, (b) The C-RAN architecture separates RRHs and BBUs, with all RRHs linked to a centralized baseband computing unit within a virtualized BBU pool via fronthaul, (c) The entirely centralized C-RAN architecture, wherein all functions pertaining to Layer 1, Layer 2, and Layer 3 are situated within the BBU, and (d) The partially centralized C-RAN architecture integrates Layer 1 functions within the RRH, while Layer 2 and Layer 3 functions are situated in the BBU.**

### 3) Heterogeneous C-RAN (HC-RAN)

A heterogeneous setup was created by integrating micro and macro base stations to meet 5G dense network needs [35]. Network administration, mobility management, and system performance depend on macro base stations. Cloud computing helps HC-RAN allot compute workloads and dynamically manage network resources [43]. It increases network capacity and reduces electricity usage. **Figure 7(a)** shows the widespread deployment of several small cell types to suit 5G network capacity and coverage needs. **Figure 7(b)** shows the architecture of HC-RAN system [38]. Separating the control and user planes in the HC-RAN would improve C-RAN operations and efficiency by limiting control plane responsibilities to macro base stations. HC-RAN maximizes spectrum and energy efficiency while increasing data throughput on heterogeneous networks with C-RAN [44].

### 4) FOG-RAN (F-RAN)

Decentralising network services closer to consumers might reduce latency in 5G networks [45]. With fog computing near to RRHs, F-RAN reduces data transfer latency and boosts user engagement. Due to its distributed architecture, F-RAN reduces network edge congestion by moving processing workloads from central servers to fog nodes. It provides ultra-reliable, low-latency access to all your connected devices using the best of both techniques. The 6G smart F-RAN will process and decide IoT data quickly, ensuring continuity and low latency for a wide range of network applications [46]. The F-RAN system architecture, seen in **Figure 8(a)**, comprises the terminal, network access, and cloud computing layers. The mobile fog computing layer comprises Fog Access Points (F-APs) in the network access layer and Fog User Equipments (F-UEs) in the overall layer. The terminal layer enables Fog F-UEs to contact the HPN for system signaling data.

**Figure 8(b)** shows smart F-RAN usage scenarios. The first category centers on holographic communication [47], which promotes interpersonal, intelligent, and mixed communication between forms and users [48], [49]. Participatory robotics, better device communication, and multi-robot communication are the second group. Supportive solutions in the third group include 3D precise location, adaptive mapping, digital twins, digital medical care, and creative areas [50]. The fifth type includes holographic perceiving networks, multi-dimensional observation solutions, and big data applications [51].

### 5) Virtualized RAN (V-RAN)

Emerged lately [41] which replaces hardware-based RAN services with software-based solutions running on COTS servers, known as virtual BBUs. Cost reductions and adaptability increase with this movement away from proprietary gear. The flexibility and agility of v-RAN allows it to react to changing network needs and save money. The hardware-software split simplifies updates and scalability, allowing operators to add virtual BBUs without adding hardware [52].

![](_page_7_Picture_2.jpeg)

![](_page_7_Picture_3.jpeg)

**FIGURE 7. Heterogeneous network: (a) normal cellular configuration, and (b) Architecture of HC-RAN system.**

![](_page_7_Picture_5.jpeg)

![](_page_7_Picture_6.jpeg)

**FIGURE 8. Design of the F-RAN system. (a) The F-RAN system architecture, and (b) smart F-RAN usage scenarios.**

For faster performance, wireless carriers are linking data centers to Multi-access Edge Computing (MEC) [11]. Nevertheless, the 5G mobile network is expected to satisfy the needs of many users' devices, decreased latency services, and higher capacity needs from consumers and specialized enterprises. Virtualization has three significant challenges [41] before it can substantially improve wireless communication:

- Effective sharing of wireless resources across many digital network providers is crucial.
- Resource utilization disturbances must be thoroughly examined.
- Evaluate management and technological challenges before using virtualization in wireless networks.

The fronthaul distributes massive optical channels to V-BSs using TWDM-PON. One OLT and multiple ONUs make up the TWDM-PON. **Figure 9** shows the OLT-DU cloud link. Each DU needs an optical transceiver and Line Card (LC) to convert optical signals and send traffic. To separate traffic by wavelength, a WDM-MUX connects all LCs of each OLT. An ONU is located far from DU Cloud at the end of each optical channel to increase TWDM-PON coverage.

![](_page_7_Figure_14.jpeg)

**FIGURE 9. System architecture of V-CRAN.**

![](_page_8_Picture_1.jpeg)

V-RAN architecture is employed across several wireless generations, encompassing 4G, 5G, and forthcoming developments. Its versatility and scalability make it suitable for dynamic networks requiring efficient resource allocation, rapid service deployment, and cost-effective expansion. As to [53], v-RAN design may decrease energy consumption by as much as 46.1% relative to C-RAN and 84.1% compared to D-RAN, while simultaneously improving network throughput by up to 25%.

### 6) Open Radio Access Networks (O-RAN)

The recently announced O-RAN initiative aims to establish an intelligent, open, and interoperable network architecture to revolutionize future mobile networks' RAN [54]. The goal of O-RAN is to eliminate proprietary hardware and software limitations, making the RAN industry increasingly competitive and creative. Established in 2018, the O-RAN Alliance brings together telecommunications companies, system makers, and suppliers of services to offer open gateways and standardize RAN component standards.

Due to its open interfaces, O-RAN can seamlessly integrate RAN elements from multiple manufacturers, reducing vendor lock-in and speeding up service and application deployment. Open architecture makes O-RAN ideal for AI and ML algorithm deployment. These sophisticated technologies can optimize performance, allot resources, and increase user engagement by dynamically responding to traffic patterns and user behaviors. O-RAN smart network control improves service quality and efficiency [11], [37], [39], [54], [55]. Example of O-RAN design in **Figure 10**.

![](_page_8_Figure_6.jpeg)

**FIGURE 10. The system architecture of O-RAN.**

The need to improve network speed and efficiency while reducing costs has driven RAN structure innovation. Considering that C-RAN is suitable for 4G and 5G, the performance qualities of its successors investigated in this section show promise for beyond 5G and beyond 6G designs. In 6G, v-RAN and O-RAN are favored for network slicing, agility, dynamic resource allocation, and quick deployment. These systems have promising potential, but implementing an efficient fronthaul makes real-world deployment difficult [39]. Device complexity is the biggest obstacle to a successful fronthaul. Smartphones, tablets, wearable technologies, IoT devices, and driverless cars will be connected to 6G networks, each with different needs and features. Advanced data transport, synchronization, and management protocols for the fronthaul network are needed. Besides technological challenges, fronthaul costs limit real-world RAN system deployment. Maintaining a robust fronthaul infrastructure can be costly for network managers and service providers. Modernizing the fronthaul infrastructure to meet new technologies and bandwidth needs might be costly. This material and teachings are summarized in **Figure 11**.

![](_page_8_Figure_10.jpeg)

**FIGURE 11. Summary of this section showing lessons learned.**

### **IV. VARIOUS TECHNOLOGIES FOR THE OPTICAL FRONTHAUL OF 5G/6G AND RELATED CONCERNS**

Here we outline the current research and upcoming trends that will define 5G/6G optical fronthaul networks in the years to come. These include cost, other technologies, energy, resources, latency, and others. A primary challenge in the implementation of ultra-dense 5G/6G networks is the escalating cost of optical fronthaul, which rises with increased network density [26]. Numerous research aim to develop cost-effective optical fronthaul solutions for future 6G networks.

Several strategies have been suggested to reduce network implementation expenses. Based on [56], network operators may reduce the expense of establishing new optical fronthaul systems by pooling resources like fiber facilities. New network planning approaches, topology optimization, and PON utilization may help Mobile Network Operators (MNOs) minimize optical fronthaul deployment for 5G and 6G networks compared to P2P architecture [57]. Reusing existing optical infrastructure is an important approach for decreasing the cost of optical fronthaul installations.

The rapid expansion of data traffic in wireless networks has resulted in a notable rise in energy usage. Consequently, enhancing energy efficiency and sustainability in the optical fronthaul is imperative for various reasons, including surroundings impact, costeffectiveness, and scalability. Models for evaluating the energy consumption of various optical fronthaul architectures are provided in the work [58]. One of the main ways to reduce energy consumption is by using powersaving modes. These modes allow ONUs to turn off or adjust the transmission rate of their transmitters and receivers during low traffic periods, taking into consideration the C-RAN architecture and PON as a fronthaul. This technique was outlined in the work of [59].

![](_page_9_Picture_1.jpeg)

![](_page_9_Figure_2.jpeg)

**FIGURE 12. Issues caused by latency and/or jitter.**

Optical back-end technologies such as PON are now the norm for the implementation of Fiber-Wireless (FiWi) networks. A point-to-multipoint network access design, the PON is cost-effective. A passive optical splitter links a large number of ONUs placed close to users to the Central Office (CO) in a PON network, which in turn allocates OLT to the users. **Figure 13** displays the various degrees of energy use for ONUs.

With an ever-increasing user base, access networks account for the lion's share of telecoms' power usage. The energy-conservation methods for ONU devices are also quite important, as they account for 90% of the energy spent by ONUs in optical access networks. Additionally, PONs aren't good for energy-saving tactics since the OLT is always busy sending and receiving data.

![](_page_9_Figure_6.jpeg)

**FIGURE 13. ONU power consumption under different active and energy-saving states.**

On the other hand, energy-saving measures are well suited to the ONU's transmitter, which sits dormant for most of the time [59]. Two technologies that combine optical and wireless networks in the fronthaul and provide various trade-offs between delay, energy efficiency, complexity, and bandwidth are dynamic bandwidth distribution and radio-over-fiber. The former allows ONUs to enter power-saving modes when they are not in use, while the latter uses traffic requirement and quality-ofservice demands to distribute resources. The time it takes for a signal to get from one location to another is called latency. To provide smooth and effective communication between the BBU and RRH in optical fronthaul, low latency is required. In addition, delay fluctuation across time is known as jitter. Latency and jitter can cause several issues, as seen in **Figure 12**.

Optical fronthaul latency and jitter reduction is essential for many time-sensitive 5G and beyond network applications, including intelligent transportation systems and industrial automation [60]. Since latency and jitter across the optical front-haul have a direct effect on the network's overall performance and quality of service, solutions to these problems are necessary. One example is that the latency and jitter needs of 5G applications may be satisfied by encapsulating Common Public Radio Interface (CPRI) over Ethernet (CoE). Applying topological improvements to the optical fronthaul is another way to decrease the latency over that path [61].

With the goal of combining optical fronthaul with additional means of communication (integration), there are two types, explained below.

### 1) OPTICAL FIBER AND WIRELESS TECHNOLOGY INTEGRATION

A viable strategy for achieving the full potential of 6G is the integration of optical fiber with microwave or millimeter-wave technology in the fronthaul network. This combination has many notable benefits, which will be elaborated as follows:

• **Enhanced Versatility and Scalability**: The hybrid configuration of an integrated optical fiber and microwave or mmWave fronthaul network facilitates

![](_page_10_Picture_1.jpeg)

greater flexibility and scalability. Optical fiber offers a sturdy and dependable foundation for the network, but the wireless functionalities of microwave and mmWave technologies provide flexible and versatile connections. This adaptability is especially beneficial in situations where the installation of supplementary fiber infrastructure may prove difficult, such as in densely populated metropolitan areas or isolated rural regions. Moreover, the network can be readily expanded to meet the escalating number of connected devices and the rising data traffic needs linked to 5G and forthcoming 6G [62].

- **Improved Resilience**: An integrated optical fiber and microwave or mmWave fronthaul network can offer enhanced resilience. By combining the strengths of both wired and wireless technologies, the network can better withstand potential failures or disruptions. For example, if a fiber link is damaged or disconnected, the microwave or mmWave link can act as a backup, ensuring uninterrupted communication at least for critical services. This redundancy helps maintain a high level of reliability required for critical 6G applications and services [63].
- **Cost-effectiveness**: The integration of optical fiber with microwave or millimeter-wave technology may result in cost reductions for the development and operation of the fronthaul network. By using existing fiber infrastructure and augmenting it with wireless connections, network operators may substantially reduce the expenses related to the installation of backup fiber-optic lines. Furthermore, the dynamic and adaptable characteristics of a hybrid design might lead to enhanced resource efficiency, hence decreasing long-term operating expenses [64].

### 2) COMBINING FSO WITH WIRELESS TECHNOLOGY

FSO is a compelling option for the fronthaul of future 6G cellular networks. Nonetheless, meteorological conditions may substantially affect the efficacy of free space optics, especially for long-range FSO connections. The presence of thick clouds, severe fog, or dust storms may significantly impair the functioning of an FSO connection. Adverse meteorological conditions may result in diminished transmission efficacy in free space optical systems. A hybrid FSO/mmWave methodology is advocated to provide elevated capacity and enhanced link availability, possibly providing carrier-grade link availability of 99.999 percent. While mmWave performance may be diminished in rain, it is capable of penetrating fog. In contrast, FSO signals using 800–1700 nm lasers are unable to penetrate severe fog; however rain has a little effect on the FSO system. Hybrid FSO/RF networks may enhance availability, dependability, and resilience to weather conditions [65].

Effective resource allocation in the optical fronthaul is essential for guaranteeing optimal performance of forthcoming 6G networks. The optimal distribution of resources in the Optical Fronthaul of 6G networks yields the following advantages:

### 1) ENHANCED OVERALL NETWORK THROUGHPUT

Optimized resource allocation in the optical fronthaul might provide a more effective use of existing resources, resulting in a greater number of network flows accommodated. This is crucial for managing substantial traffic volumes in 5G and forthcoming 6G networks, since data rate demands are anticipated to exceed those of earlier generations [66]. Maximizing throughput, assigning users, managing spectrum, selecting RRHs, allocating power, and making the network usable are all crucial parts of distributing resources and administration in CRAN.

### 2) ENHANCED SPECTRAL EFFICIENCY

Improved spectrum efficiency, which might lead to increased data rates and decreased latency for end users, could be the outcome of more efficient resource allocation in the optical fronthaul.

With the goal of providing ultra-low latency and large data rates for a variety of applications, this may be a major benefit for future 6G networks [26], [67]. Intensity Modulated/Direct Detection (IM/DD) Point-To-Point (PTP) systems using dedicated fiber connections or Wavelength-Division Multiplexing (WDM) links form the basis of the existing 5G fronthaul [68]. The DU and each Active Antenna Unit (AAU) in an IM/DD system with dedicated fiber connections are linked directly via a bidirectional or unidirectional fiber. Only settings with enough of fiber resources may use this technology.

Except that, with the current tendency of building base stations more densely, the expense of installing a big quantity of fibers is intolerable. WDM permits the transmission of signals via a single fiber connection at several wavelengths. Metro and short-reach operations, such as access networks and data center interconnects, are slowly adopting Coherent Systems (CSs), which are more common in long-haul transmission. CSs offer several benefits over IM/DD systems in terms of transmission functionality:

- They are more efficient at modulation; whereas IM/DD systems can only encode data onto the optical signal amplitude, coherent systems can use amplitude, phase, and polarization to form high order modulation formats with significantly higher spectral efficiencies.
- CSs are better at disturbance compensation; whereas IM/DD systems can be severely hindered by CD, Multipath Interference (MPI), and chaotic effects, CSs make it less difficult to adjust for these transmission impairments.
- Receiver sensitivity is significantly higher in coherent detection than in IM/DD systems due to the use of a Local Oscillator (LO).

![](_page_11_Picture_1.jpeg)

![](_page_11_Figure_3.jpeg)

**FIGURE 14. Visual representation of optical transport networks that may handle many applications, including fronthaul, midhaul, and backhaul.**

The use of amplifiers in optical communications is not recommended for applications with short distances (< 20 km). All of these benefits, plus the significant reductions in price and power consumption over the last decade, have led many to believe that coherent systems are the way to go for access networks in the future. Further, we may provide reconfigurable Digital Signal Processors (DSPs) in CSs and the channel selection capability to offer access networks effective and adaptable Point-To-Multipoint (PTMP) transfer. **Figure 14** illustrates the optical access network for wireless applications, including fronthaul (linking AAUs and DUs), midhaul (linking DUs and Centralized Unit (CU)s), and backhaul (linking CUs and core networks).

One high-speed transceiver at the DU side transmits and receives data from several low-speed transceivers at various AAUs in the fronthaul's PTMP coherent design. The AAUs modulate signals at different wavelengths and multiplex them with an optical mixer in uplink transmission. See [67] for coherent transceivers with 100 kHz transmitter and receiver laser linewidths. The lasers' frequencies automatically frequency-division multiplex subcarriers without aliasing. The DU's high-bandwidth coherent receiver receives multicarrier transmissions. DSP dismultiplexes multicarrier signals into subcarriers. Later, DSP blocks like CD compensation, clock repair, FOC, adaptive 2 x 2 equalization for polarization demultiplexing, remnant inter-symbol interference restoration, and CPR compensate for subcarrier communication shortcomings. To recover data, FEC decoding is used. A distributed unit digitally combines subcarriers and sends them via a highbandwidth coherent transmitter in downlink communication. Multicarrier signal is separated by power splitter and sent to each AAU. A local oscillator with a proper center frequency downconverts the multicarrier signal to baseband after coherence detection at the AAU.

High capacity, easy implementation, and fronthaul network openness and flexibility are achieved with the PTMP coherent architecture. With electronic subcarrier technology and customizable DSP, the fronthaul may direct any subcarrier to any receiver. The DU and each AAU communicate. Communicating with any AAU, the DU connects independent AAUs. The subcarriers can also be tailored for each AAU's needs and connection.

### 3) IMPROVED ENERGY EFFICIENCY

Allocating optical fronthaul resources optimally lowers power usage by decreasing the overall power needed to transmit and process signals [69]. Because of the economic and environmental importance of energy efficiency, this will play a pivotal role in 6G networks.

Future advancements B5G and 6G networks will aim to achieve superior peak data rates (e.g., > 100 Gb/s for 6G), increased traffic density (e.g., > 100 Tb/s/km² for 6G), enhanced energy efficiency (e.g., > 10× for 6G compared to 5G), reduced latency (e.g., < 1 ms for 6G), and broader, more profound coverage, among other improvements [70], [71]. The operational separation in 5G may be insufficient to satisfy the stringent demands of B5G/6G fronthaul. Consequently, the B5G/6G fronthaul necessitates transformative advances in both design and transmission technology to provide elevated peak data rates, reduced delay, and increased interconnectivity.

![](_page_12_Picture_1.jpeg)

![](_page_12_Figure_2.jpeg)

**FIGURE 15. Various ML methods for improving 6G optical fronthaul networks, and related limitations.**

### 4) IMPROVING SCALABILITY AND ADAPTABILITY

Optimized resource allocation in the optical fronthaul can enhance scalability and adaptability, facilitating the network's capacity to support an increased number of users and devices while maintaining performance and responding to fluctuating traffic demands and network conditions in real time. Dynamic Bandwidth Allocation (DBA) facilitates efficient resource allocation in the optical fronthaul by dynamically adjusting bandwidth distribution according to user demands and network circumstances. DBA optimizes resource allocation, promotes network efficacy, and enhances user experience. It guarantees superior service quality for diverse applications and facilitates network scalability [72], [73].

#### *A. Optical Fronthaul and ML/AI*

With technological advancements, DBAs are anticipated to progress by integrating ML and AI for enhanced optimization. A new age of intelligent operations and resource allocation is dawning with the integration of ML and AI [71] into 6G fronthaul technologies. There are two main reasons to use ML [74]:

- Situations where a mathematical model based on physics is lacking, due to a lack of domain-specific knowledge or a "model deficit," make it very persuasive; and
- It is also acceptable when the current algorithms, which run pre-existing mathematical models based on physical principles, are computationally too complex or take too long to process, a problem called a "algorithm deficit".

Optical fronthaul networks are notoriously difficult to study when it comes to implementing AI and ML. This is because these networks are very cost-sensitive, have limited computational resources, are constantly changing, and there aren't enough data acquisition and monitoring systems to provide representative data. On top of that, ML models need to be extremely flexible and able to adapt quickly to new situations in order to support real-time applications. Despite this, these models can optimize performance, reduce congestion, and guarantee a smooth user experience. Moreover, with the help of modern optimization techniques, latency can be enhanced, bandwidth, and energy efficiency, which could impact [75].

In addition, network management gains intelligence via the use of AI algorithms, which paves the way for problem detection, anticipatory maintenance, and dynamic resource allocation. For instance, the IoT and sensor networks gather information from the real world to enrich the digital one, which uses AI techniques via software models of a real system [76]. To improve reliability and minimize downtime, AI may be used to evaluate real-time data from optical fronthaul networks. This data can then be used to detect potential failures and fix problems proactively.

Furthermore, in order to guarantee effective resource use, ML-driven traffic prediction models may dynamically alter the fronthaul interface splitting choices in response to changing demand. As an example, the research [77] took into account the possibility of a flexible functional split, in which the tasks performed by each of the two entities may be changed on the fly. **Figure 15** shows that there are a number of methods [78] to improve the capabilities of 6G optical fronthaul networks powered by AI, building on ML approaches. They put out a model based on queuing that can accurately imitate the actions of these nodes, and we proved it through rigorous simulations. In addition, they used Jackson's theory of networks to determine the fronthaul network's end-to-end latency, which let us test the effects of various networking rules and situations (such as background traffic or heterogeneous technologies).

![](_page_13_Picture_1.jpeg)

Moreover, a paradigm for handling traffic prediction using the enormous potential of ML algorithms was described in the paper [79]. For multi-dimensional datasets, a system called Adaptive Machine Learning-based Cellular Traffic Prediction (AML-CTP) is introduced. Its goal is to make the process of choosing a suitable model for estimating the load of network traffic easier and faster. In order to decrease training time and hardware complexity, the best model is chosen among four supervised prediction methods.

A novel ML architecture dubbed Intelligent Multi-Attentive Generative Adversarial Networks (IMAGAN) was developed in [80] to optimize resource consumption and traffic grooming (TG) in 5G optical fronthaul networks. The proposed IMAGAN-based architecture uses a multi-attentive model to recognize spatiotemporal traffic patterns and a generative adversarial model to generate synthetic network situations. The results show that the IMAGAN-based design improves energy management system resource consumption, bandwidth utilization, rejection ratio, MAE, and RMSE. The study provides a solid foundation for intelligent 5G network design and management advancements.

The research [81] considered an intelligent traffic steering (TS) method in the proposed disaggregated ORAN architecture to maximize resource usage. In the case of unknown dynamic traffic needs, they suggested a combined intelligent traffic prediction, flow-split distribution, dynamic user association, and radio resource management framework.

By adjusting resources in response to changing demand, this adaptive method improves the efficiency of the network. Better allocation of resources is another benefit of AI and ML, which can sift through mountains of data to provide pinpoint forecasts on the behavior of networks. The study [44] covered task offloading in the new 5G O-RAN architecture, which allows the co-location of the Open Central Unit (O-CU) and Open Distributed Unit (O-DU) at the edge cloud for low-latency services. For O-RAN, a fronthaul network connects Radio Units (O-RUs) with edge clouds hosting O-DUs. By utilizing segment routing, O-RAN intelligent controllers, and many edge clouds, they optimized O-RAN offloading, fronthaul routing, and computation delays.

This kind of approach is well-suited to the ever-changing 6G network environment because of its adaptability. Systems powered by AI make it possible to automate network modifications and maintenance, cutting down on the need for human interaction [82]. The excellent security of 5G/6G optical fronthaul may also be ensured using ML.

### *B. Bandwidth Allocation and Capacity Enhancement*

By using Software-Defined Networking (SDN), the optical fronthaul network may be dynamically provisioned and reconfigured to accommodate changing traffic patterns and capacity requirements, all while giving priority to essential services. Dynamic bandwidth allocation and traffic grooming are two examples of advanced traffic engineering approaches that improve resource use and minimize delay [83]. Not only that, SDN's centralized management makes it easy to monitor, debug, and gather performance metrics in real-time for networks. This enables proactive monitoring, fault detection, and incident response [84], [85]. Using the programmability of SDN, operators may improve network performance, identify abnormalities, and foresee possible failures. This, in turn, enhances the resilience of the fronthaul infrastructure.

By using Space Division Multiplexing (SDM), the optical fronthaul capacity may be enhanced. The fundamental concept is to partition an optical fiber's crosssection into several channels, with the ability to transmit distinct data streams across each channel. To determine these channels, one may utilize a variety of strategies, such as a multicore fiber with many cores or a few-mode fiber with various patterns. With the use of these spatial channels, SDM provides a data capacity that is much greater than that of traditional single-channel optical fibers [86]. Supporting the ever-increasing data needs of contemporary communication networks is one of the main benefits of SDM for high-capacity optical fronthaul. An ever-increasing need for faster data transfers and less delay is driving the development of new technologies like 5G and soon 6G, which are bandwidth-intensive applications. By efficiently expanding the capacity of optical fibers, SDM provides a scalable approach to meet these demands [87].

Optical fronthaul systems that are enabled by SDN use AI to convert general service intentions into specific control rules for things like bandwidth allocation [88], slicing [89], and cross-layer optimization [90]. With the help of federated learning and edge computing, AI models can be developed and run near LiFi access points and end devices, which help to decrease latency and protect user privacy. For 6G optical wireless systems to be scalable and privacy-aware, this distributed intelligence is crucial.

### *C. Security and Privacy Concerns*

Security and privacy are major concerns with the introduction of 5G/6G, especially with the optical fronthaul. As a result, new methods for securing synchronization planes, secure environments, certificate enrolment, and security provisioning are required [91]. Moreover, a critical tactic in meeting these difficulties is the incorporation of ML for the administration of network security. From physical-layer assaults to more complex incursions, ML algorithms play a crucial role in identifying and mitigating security breaches [92]. Although most occurrences of security breaches at the optical layer should be protected by confidentiality provisions, more than 1,000 of these events are recorded every year.

**FIGURE 16. Various kind of assaults that may be executed against the optical physical infrastructure: (a) eavesdropping: executed by the establishment of a transient optical coupler, and (b) service interruption assault: executed by synchronized fiber optic severance in a national backbone infrastructure.**

The increasing number of fiber plants being set up, often in unprotected areas, the fact that these plants are shared among many overlay network services that are structured into separate domains with complicated agreements for sharing knowledge, the extremely high data rates, and the extremely long optical reach all add up to make optical network management very complicated.

Eavesdropping and service denial attacks are the two main forms of physical-layer assaults depending on the attacker's aim. A fiber eavesdropping attack seeks unauthorized access to data. Fiber tapping may be used to intercept unencrypted communication by collecting a piece of the optical signal using an eavesdropper's detector. To gain access to the signal, one can either use monitoring ports on optical devices or bend the fiber to violate total internal reflection and leak light out. The rationale behind a popular monitoring approach is shown in **Figure 16(a)** [92], and **Figure 16(b)** shows service interruption assault.

Optical networks are designed and provided with enough redundancy to guarantee resilience against single or multiple fiber cuts, since this is the most prevalent failure type. Such approaches safeguard against inadvertent fiber severance that often occurs when construction machinery inadvertently breaches fiber conduits. Deliberate fiber cut assaults may be orchestrated to cause significant damage by, for instance, simultaneously severing many connections. This may result in some segments of the network remaining disconnected while other segments become overloaded with redirected traffic. The efficacy of the assault may be enhanced by severing essential fiber connections. Furthermore, the design of optical network security administration systems is being restructured to include efficient ML models capable of identifying a diverse range of emerging threats [93]. Adapting to changing attack patterns and improving their detection skills gradually, these systems are built to be proactive. Optical Performance Monitoring (OPM) data contains complicated patterns that may be understood by ML algorithms. These algorithms are vital for detecting even the most minor indications of security breaches, which can greatly improve the safety of optical networks [94]. Examples of this kind of technique include optical network security tracking with ML assistance, which demonstrates how well these methods perform by detecting, identifying, and localizing optical-layer assaults in actual network settings [95].

One significant addition to the family of network analytics is the ability to detect and identify attacks using ML. Although previous research has taken into account connection deterioration due to component failures, the management of physical-layer security concerns is still not fully resolved. Multiple ML approaches can detect and identify assaults. Studies have examined the utilization of Supervised Learning (SL) and Unsupervised Learning (UL) in single-link and single-Optical Channel (OCh) scenarios. However, implementing a network-wide multi-OCh Attack Detection and Identification (ADI) system has difficulties beyond accuracy.

Therefore, evaluate the pros and disadvantages of each ML approach, including model accuracy and network impact. SL, Semi-Supervised Learning (SSL), and UL approaches differ primarily in dataset requirements and training methodologies. Understanding the integration of these models into the Network Management Systems (NMS) is crucial for efficient and reliable security assessment. **Figure 17** [80] shows how SL, SSL, and UL adapt to new connection requests or physical-layer attacks.

For managing the security of autonomous optical networks, Root Cause Analysis (RCA) is essential for getting to the bottom of security incidents [96]. In addition, the network's resilience to new attacks is improved by scalable physical layer security components made for optical SDN controllers that are built on microservices [97].

![](_page_14_Figure_11.jpeg)

**FIGURE 17. How SL, SSL, and UL adapt to new connection requests or physical-layer attacks. Continuous lines symbolize the typical procedure of connecting, operating, and maintaining a link. Dashed lines show ML steps.**

![](_page_15_Picture_1.jpeg)

![](_page_15_Figure_2.jpeg)

**FIGURE 18. The development of NMS architecture in response to the proliferation of telemetry and sophisticated ML methods for threat assessment [96].**

To provide strong security measures that can adapt to the network's changing needs, autonomous security management systems use these components. **Figure 19** depicts the potential course of evolution of the NMS architecture, beginning with a legacy scenario defined by conventional NMS and ending with optical networks that incorporate telemetry systems and optical security ML tools. Damage can be inflicted upon an optical network if unauthorized individuals get access to its management system and maliciously alter the network's settings and configurations, therefore impacting the services. Keeping management systems safe requires ever-more-advanced authentication methods, such as biometric or multi-level. Many optical networks are still managed by classic NMSs, as seen in **Figure 19(a)**. They gather OPM data every 15 minutes with limited storage. Due to technology constraints, operators must use basic reactive tactics like alarm monitoring and manual intervention to address malfunctions and assaults. Security evaluation is challenging due to limited historical data and manual inspections, requiring skilled operators who understand the system. To improve optical network management, telemetry devices incorporated in the NMS gather and store huge OPM data records every second (or few seconds) in a database, as shown in **Figure 19(b)**.

Numerous network system makers offer this technology for future products. Despite the enhanced telemetry system, attack diagnostics remain comparable to previous methods, however remedy table checks may be performed on historical data instead of log files with few entries. A network malfunction might result from a breakdown or a malicious attack. A failure and an attack may have similar symptoms but require distinct treatments. To prevent malfunctions caused by malicious attacks, it is crucial to have a system along with telemetry systems that monitor connection status and optical signal quality. This system can identify and classify attacks based on previously identified patterns.

**Figure 19(c)** depicts an NMS architecture that can detect, identify, and locate the source of an attack. To enable automatic security diagnostics, NMS should have features for tracking new assaults. As an extension of the preceding scenario, the NMS implements an algorithm to distinguish failures from known attacks and classify them accordingly. Human action is necessary to combat new assaults using current technologies. ML-driven RCA functionality offers a breakthrough by providing first insight into the impact of new threats. NMS design with RCA is shown in **Figure 19(d)**.

This method requires no prior knowledge of attack outcomes, but can give valuable insight into their impact on network performance and help operators choose the most effective security solutions. The security frameworks that safeguard optical networks must also adapt to new threats in order to maintain the confidentiality and authenticity of transmitted data. **Figure 18** shows a summary of the lessons learned in this section.

### **V. ANALYTICAL MODELING OF OPTICAL WIRELESS FRONTHAUL LINKS**

Optical wireless communication, encompassing free space optics and LiFi, has emerged as a promising fronthaul solution for beyond-5G and 6G networks due to its ultrahigh data rates, license-free spectrum, and immunity to electromagnetic interference [98], [99]. To evaluate the feasibility and performance limits of such systems, a unified analytical model is essential. This section presents a general analytical framework for optical wireless fronthaul links, applicable to both outdoor FSO and indoor LiFi scenarios.

![](_page_16_Figure_2.jpeg)

FIGURE 19. Summary of this section showing lessons learned.

#### A. SYSTEM MODEL

Consider an optical wireless fronthaul link connecting a distributed unit and a remote unit. The transmitted optical signal which is dependent on IM/DD, is widely adopted in practical LiFi and FSO systems due to its simplicity, robustness, and energy efficiency [100], [101], [102]. The received signal can be expressed as:

$$y(t) = R \cdot h \cdot x(t) + n(t),$$

where x(t) denotes the transmitted optical intensity signal, R is the photodetector responsivity, h represents the overall optical channel gain including both LOS and Non-Line-Of-Sight (NLOS) channels, and n(t) models additive noise, including thermal and shot noise components.

### B. OPTICAL CHANNEL GAIN WITH LOS AND NLOS COMPONENTS

The optical wireless channel gain depends strongly on the propagation environment and the availability of a direct LOS path between the transmitter and receiver. In general, the overall channel gain can be expressed as the superposition of LOS and NLoS components [103]:

$$h = h_{LOS} + h_{NLOS}$$

For outdoor FSO fronthaul links, the LOS component typically dominates due to the highly directional nature of laser beams. In contrast, indoor LiFi fronthaul links exhibit both LOS and diffuse NLOS components caused by reflections from walls, ceilings, and other surfaces.

### 1) LOS CHANNEL GAIN FOR LIFI

For LiFi systems employing LEDs with a Lambertian radiation pattern, the LoS channel gain is given by [102]:

$$h_{\text{LOS}}^{\text{LiFi}} = \begin{cases} \frac{(m+1)A}{2\pi d^2} \cos^m(\emptyset) T_s(\psi) g(\psi) \cos(\psi) & 0 \le \psi \le \Psi_c \\ 0 & \psi \ge \Psi_c \end{cases}$$

where  $m = -\frac{\ln(2)}{\ln(\cos(\Phi_{1/2}))}$  is the Lambertian order;  $\Phi_{1/2}$  is the LED half-power semi-angle; d is the link distance;  $\emptyset$  is the irradiance angle;  $\psi$  is the incidence angle; A is the photodetector area;  $T_s(\psi)$  is the optical filter gain;  $g(\psi)$  is the concentrator gain and  $\Psi_c$  is the receiver field of view (FOV).

### 2) LOS MODEL FOR FSO (OUTDOOR OPTICAL WIRELESS)

Due to the narrow beam divergence and precise alignment inherent to FSO systems, the LOS component accounts for most of the received optical power. The LOS channel gain in FSO fronthaul systems is typically modelled as [104], [105]:

$$\mathbf{\textit{h}}_{\text{LOS}}^{\text{FSO}} = \mathbf{\textit{h}}_{\text{geo}} \cdot \mathbf{\textit{h}}_{\text{atm}} \cdot \mathbf{\textit{h}}_{\text{point}}$$

where  $h_{\rm geo}$  accounts for geometric spreading losses,  $h_{\rm atm}$  represents atmospheric attenuation (dominant in FSO links), and  $h_{\rm point}$  models misalignment and pointing errors. Assuming a Gaussian beam profile, the geometric loss due to beam divergence over a link distance d is given by:

$$h_{\rm geo} = \frac{A}{\pi (d\theta)^2}$$

![](_page_17_Picture_1.jpeg)

where A is the receiver aperture area and  $\theta$  denotes the beam divergence angle.

Atmospheric attenuation caused by fog, haze, rain, and aerosols can be modelled using the Beer–Lambert law:

$$h_{\rm atm} = \exp(-\alpha d)$$

where  $\alpha$  is the atmospheric attenuation coefficient, dependent on weather conditions and optical wavelength. This factor is particularly critical for outdoor FSO fronthaul deployments in urban and long-distance scenarios. Pointing errors arise due to building sway, wind loads, and mechanical vibrations, and are typically modeled as a stochastic fading component. A commonly used approximation is:

$$h_{\text{point}} = \exp\left(-\frac{r^2}{2\sigma^2}\right)$$

where r denotes the radial displacement at the receiver plane and  $\sigma$  represents the jitter standard deviation.

### 3) NLOS CHANNEL GAIN

In indoor LiFi fronthaul scenarios, NLOS propagation arises primarily from diffuse reflections on room surfaces. The NLOS channel gain can be modelled as the sum of contributions from reflected paths [100], [102]:

$$h_{\mathrm{NLOS}}^{\mathrm{LiFi}} = \sum_{i=1}^{N_r} h_i^{\mathrm{ref}}$$

where  $N_r$  denotes the number of reflective elements (walls, ceiling, floor), and each reflected component is expressed as:

$$h_i^{\text{ref}} = \frac{(m+1)A_r\rho_i}{2\pi^2d_{1,i}^2d_{2,i}^2}\cos^{\text{m}}(\emptyset_i)\cos(\alpha_i)\cos(\beta_i)T_s(\psi_i)g(\psi_i),$$

with  $\rho_i$  being the reflection coefficient of surface i,  $d_{1,i}$  and  $d_{2,i}$  denoting transmitter-to-surface and surface-to-receiver distances,  $\alpha_i$  and  $\beta_i$  representing reflection and incidence angles. Although NLOS components contribute less power than LOS paths, they improve coverage robustness and mitigate shadowing effects in LiFi-based fronthaul deployments.

In conventional FSO fronthaul links, NLOS components are typically negligible due to the highly directional laser beams and lack of significant reflective paths in outdoor environments. However, under specific scenarios, such as urban canyon environments or UAV-assisted relays, scattered or reflected components may contribute marginally to the received signal. These contributions are usually ignored in first-order analytical models but may be considered in advanced stochastic channel modelling.

Combining LOS and NLOS contributions, the total optical channel gain can be written as:

$$h = \begin{cases} h_{\text{LOS}}^{\text{LiFi}} + h_{\text{NLOS}}^{\text{LiFi}} & \text{LiFi fronthaul} \ h_{\text{LOS}}^{\text{FSO}} & \text{FSO fronthaul (LoS - dominant)} \end{cases}$$

This unified formulation enables fair performance evaluation and comparison of LiFi- and FSO-based fronthaul technologies under heterogeneous deployment scenarios in 6G networks.

### C. SIGNAL-TO-NOISE RATIO

For IM/DD-based optical wireless links, the electrical SNR at the receiver is expressed as [85]:

$$SNR = \frac{(RP_th)^2}{\sigma_n^2}$$

where  $P_t$  is the transmitted optical power and  $\sigma_n^2$  denotes the total noise variance. This formulation applies to both LiFi and FSO fronthaul links, with noise characteristics adapted to indoor or outdoor operating environments.

### 1) NOISE MODELING IN LIFI AND FSO FRONTHAUL SYSTEMS

In optical wireless fronthaul systems employing IM/DD, the received signal is corrupted by several noise sources originating from the photodetector, receiver electronics, and ambient optical environment. The dominant noise components differ between indoor LiFi and outdoor FSO systems due to their distinct operating conditions.

In general, the total noise variance at the receiver can be expressed as [100]:

$$\sigma_n^2 = \sigma_{\rm shot}^2 + \sigma_{\rm thermal}^2 + \sigma_{\rm background}^2$$

where  $\sigma_{shot}^2$ ,  $\sigma_{thermal}^2$ ,  $\sigma_{background}^2$  denote shot noise, thermal noise, and background light-induced noise variances, respectively. Background noise results from ambient optical sources such as sunlight, fluorescent lamps, and other artificial lighting. This noise component is particularly critical for LiFi systems and outdoor FSO links exposed to solar radiation. In indoor LiFi fronthaul deployments, background noise can be mitigated through narrow FOV receivers, optical filtering, and adaptive gain control.

### 2) SHOT NOISE

Shot noise arises from the discrete nature of photoelectron generation at the photodetector and is proportional to the received optical power. The shot noise variance is given by:

$$\sigma_{\rm shot}^2 = 2qR(P_r + P_{\rm background})B,$$

where q is the electron charge,  $P_r = hP_t$  is the received optical signal power,  $P_{\text{background}}$  denotes the background optical power, and B is the receiver bandwidth.

Shot noise is particularly significant in FSO fronthaul, where higher received optical power levels are common,

![](_page_18_Picture_1.jpeg)

and in LiFi systems operating under strong ambient illumination.

### 3) THERMAL NOISE

Thermal noise originates from electronic components such as resistors and transimpedance amplifiers (TIAs) in the receiver front-end. It is independent of the received optical power and can be expressed as [100], [106]:

$$\sigma_{\mathrm{thermal}}^2 = \frac{4kTB}{R_F} + \frac{16\pi^2 kT\Gamma B^3}{g_m},$$

where k is Boltzmann's constant, T is the absolute temperature,  $R_F$  is the load resistance,  $\Gamma$  is the FET channel noise factor,  $g_m$  is the FET transconductance. Thermal noise dominates in low received power regimes, such as long-distance FSO links under severe atmospheric attenuation or LiFi links with limited LED output power.

### VI. RECENT CONTRIBUTIONS OF OPTICAL WIRELESS AND OPTICAL FRONTHAUL TECHNOLOGIES FOR 5G/6G

The research on the development of optical and opticalwireless fronthaul technologies that underpin 5G and 6G networks is examined in this section. Research on Passive Optical Networks (PON/WDM, TWDM-PON, etc.) for high-capacity, low-latency access was first covered, then models based on optimization for efficient design, and methods for designing optical-fiber networks for scalable deployment. Next, we'll take a look at wireless and hybrid optical-wireless fronthaul, which includes technologies like FSO, Light Fidelity (LiFi)/Visible Light Communication (VLC), and Analog Radio-over-Fiber (ARoF). We'll highlight their contributions to building 6G networks that are smart, robust, and energy efficient. Figure 20 shows the classification of studies that are considered in this section.

Recent studies have further advanced energy-efficient and intelligent optimization strategies for wireless sensor and IoT-enabled networks. Hybrid frameworks combining clustering [107], optimization, and learning-based adaptation have been shown to significantly enhance network performance and energy efficiency. For instance, reinforcement learning-assisted clustering approaches integrating DEEC, K-means, and knapsack-based optimization enable adaptive configuration of network parameters under dynamic conditions, leading to improved energy balancing and reduced communication overhead [108]. In addition, knapsack-driven cluster head selection schemes that exploit residual energy awareness have been demonstrated to extend network lifetime while improving data delivery efficiency and reducing latency. Moreover, integrated EEKA and K-means clustering methods have been reported to enhance energy consumption, throughput, and packet delivery performance by jointly optimizing node grouping and transmission strategies [109].

![](_page_18_Figure_10.jpeg)

FIGURE 20. Classification of the optical wireless and optical fronthaul studies in this section for 5G/6G.

### A. OPTICAL FRONTHAUL FOR 5G/6G NETWORK

In this part, we will go over the research that has used PON-based fronthaul solutions for 5G and 6G mobile networks, including Wavelength Division Multiplexing (WDM-PON) and Time-and-Wavelength Division Multiplexing (TWDM-PON). Systems that rely on PON are seen as having great promise since they provide:

- Multi-wavelength high bandwidth capacity,
- Very low latency acceptable to Cloud-RAN and Open-RAN structures, and
- Cost-efficient, since passive optical components (splitters and filters) work to reduce the power and the maintenance expenses.

The primary goal of [110] was to provide the groundwork for Next-Generation PON Stage 2 (NG-PON2) by creating an open-access paradigm for WDM and TWDM in PONs. Making it possible for several service providers to make efficient use of the same optical infrastructure is their primary goal.

Based on the simulation and analytical results, TWDM-PON is a good fit for high-capacity broadband services because it provides greater bandwidth utilization and scalability than static WDM systems. Accurate wavelength tuning, extensive network administration, and problems with synchronization between several operators are some of the system's shortcomings.

As for next-generation passive optical networks (NG-PON2), another research [111] compares three optical access systems: OTDM-PON, WDM-PON, and TWDM-PON. Over lengths of up to 130 km, all systems were tested at 20 Gbps for both downstream and upstream traffic. According to the results, TWDM-PON has the greatest signal quality (Q-factor), whereas WDM-PON is more expensive but performs well, and OTDM-PON is less expensive but has poor performance over long distances. Conclusion: For future high-speed, long-reach optical networks, TWDM-PON is the best, most cost-effective option. **Table I** sumamarises PON-based fronthaul contributions of recent studies.

![](_page_19_Picture_1.jpeg)

TABLE I. SUMMARY OF OPTICAL AND PON-BASED FRONTHAUL CONTRIBUTIONS OF RECENT STUDIES.

|                                               |       |      |                                                               |                                                           |          | DE     |        | C                 | CC       |                                                                                                |              |                                                   |         | P      |    | A        | Т                              |                                              |
|-----------------------------------------------|-------|------|---------------------------------------------------------------|-----------------------------------------------------------|----------|--------|--------|-------------------|----------|------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------|---------|--------|----|----------|--------------------------------|----------------------------------------------|
|                                               | Ref.  | Year | OpOb                                                          | NAT                                                       | Od.      | In.    | Both   | S                 | M        | System model                                                                                   | Int.         | InM.                                              | Co.     | En.    | BW | PA       | AA                             | Ехр.                                         |
| PON/ TWDM access system                       | [110] | 2014 | Share<br>wavelengths<br>and increase<br>network<br>efficiency | Next-<br>Generatio<br>n PON<br>(NG-<br>PON2)              | <b>√</b> | х      | х      | х                 | <b>√</b> | Wavelength<br>and fiber<br>sharing in<br>WDM/TWD<br>M<br>architectures                         | х            | -                                                 | Х       | х      | ✓  | <b>√</b> | х                              | MATLAB<br>Simulink                           |
|                                               | [111] | 2022 | improve<br>signal<br>quality and<br>transmission<br>distance  | NG-PON2<br>Long-<br>Reach<br>Optical<br>Access<br>Network | ✓        | ×      | ×      | x                 | ✓        | Comparison<br>of OTDM,<br>WDM, and<br>TWDM-<br>PON at 20<br>Gbps over<br>long<br>distances     | x            | _                                                 | x       | x      | ✓  | ✓        | x                              | OptiSystem                                   |
| Optical<br>fronthaul<br>optimization<br>model | [57]  | 2022 | Reduce total<br>network cost<br>(TCO)                         |                                                           | ✓        | x      | х      | х                 | √        | TWDM-<br>PON-based<br>fronthaul<br>minimizing<br>total cost of<br>ownership                    | <b>√</b>     | ILP +<br>Heuristic<br>(K-means,<br>GA)            | ✓       | х      | х  | х        | <b>√</b>                       | ILP/ Heuristic<br>Model (Python<br>/ MATLAB) |
|                                               | [58]  | 2023 | Minimize<br>cost and<br>energy use                            | 5G/6G<br>Optical<br>Fronthaul<br>Network                  | >        | x      | x      | x                 | ✓        | Multi-<br>architecture<br>cost–energy<br>optimization<br>(Fiber, PON,<br>Hybrid<br>PON-FSO)    | >            | ILP +<br>Heuristic<br>(Energy +<br>Cost<br>Model) | ✓       | >      | X  | x        | ✓                              | Heuristic<br>Model<br>(MATLAB +<br>Gurobi)   |
|                                               | [112] | 2024 | Improve<br>energy<br>transfer and<br>reduce<br>power loss     | 6G<br>Optical<br>Fronthaul<br>Network                     | ✓        | x      | х      | ✓                 | х        | Power-over-<br>Fiber (PoF)<br>model for<br>simultaneou<br>s data and<br>energy<br>transmission | х            | -                                                 | х       | ✓      | х  | х        | ✓                              | Experimental<br>Testbed                      |
| Terms                                         |       |      |                                                               | И: Inte                                                   | gration  | n mode | 1; PA: | objecti<br>Passiv |          | Activ                                                                                          | e access; Co | o.: Cos                                           | t; En.: | Energy |    |          | e; M: Multiple;<br>width; Exp: |                                              |

![](_page_19_Figure_4.jpeg)

FIGURE 21. Main strategies of in-operation optical network planning.

![](_page_20_Picture_1.jpeg)

An optimization-based approach for 5G/6G optical fronthaul was presented in [58], with the goal of minimizing energy usage and Total Cost Of Ownership (TCO). Different fronthaul designs, including point-topoint fiber, PON, and hybrid PON-FSO systems, were considered, and an Integer Linear Programming (ILP) model was developed. Their research showed that hybrid systems are more energy-efficient in small or more diverse environments, while fiber-based designs are more costeffective for large-scale deployments. They stressed that in order to create sustainable 6G network designs, energy consumption optimization and cost planning must be integrated.

Another work [57] used optimization to provide a 5G/6G optical fronthaul that is both efficient and inexpensive. By determining the optimal placements for splitters, BBU pools, and fiber connections in a TWDM-PON-based design, they were able to decrease TCO. In addition, they used a number of parameters, including latency, fiber length, and splitter ratios of 1:4, 1:8, and 1:16.

Heuristic approaches, such as evolutionary algorithms and K-means clustering, were employed to effectively manage massive networks and get near-optimal outcomes. As part of the 6G optical fronthaul system, the author suggested the idea of Power over Fiber (PoF) pooling in [112]. In order to power and transfer data to RRHs, their main focus was on optical fibers. In addition, optical switches were employed to regulate the power distribution among RRHs and to control whether they were active or asleep. The system could only work under certain power and distance constraints (up to 15 kilometres). Based on the findings, PoF pooling is a viable option for powering RRHs while maintaining consistent high-speed data connections. By enabling the RRHs to enter deep-sleep states, this strategy further decreases energy consumption, paving the way for flexible and energy-efficient 6G fronthaul networks.

### *B. OPTICAL- FIBRE NETWORK PLANNING*

The following research focuses on the physical architecture and layout of fiber optic networks prior to deployment, as well as the planning, design, and deployment tactics of optical fiber infrastructure to enable 6G and 5G fronthaul networks. Network planners have used a wide variety of tactics, including spectrum defragmentation and shifting, which involves reallocating operationally active wavelength slots to consolidate fragmented spectrum and enable additional light pathways without service interruption [113].

As an alternative to over-provisioning [114], a method known as dynamic traffic prediction makes use of traffic forecasts to activate heuristics that reallocate or re-route resources in reaction to spikes in demand occurring in realtime. Another tactic that Intense uses over several pathways is multi-path routing with defragmentation, which is triggered when fragmentation inhibits single-path allocation and improves spectrum utilization [115]. Moreover, ML (specifically DRL-based resource reallocation) employs reinforcement learning or deep learning to determine the optimal timing and method for reallocating optical channels or resources in live networks, enhancing utilization and flexibility [116]. **Figure 21** shows the main strategies used in in-operation optical network planning.

According to the classification depicted in the preceding image, **Table II** summarizes research on operational optical network planning techniques aimed at optimizing resource use, minimizing service interruptions, and enhancing real-time network adaptability.

### *C. OPTICAL WIRELESS AND OPTICAL FRONTHAUL TECHNOLOGIES FOR 5G/6G NETWORKS*

This section examines studies addressing wireless, opticalwireless, or hybrid fronthaul solutions for 5G and 6G technologies. This encompasses FSO communication, VLC, LiFi, and radio-over-FSO technologies, frequently integrated with fiber networks to create hybrid opticalwireless fronthaul designs. This group's objective is to address fibre deployment constraints by implementing wireless or optical-wireless networks that ensure high throughput, low latency, and adaptable backhaul/fronthaul connectivity.

This study examines the utilization of Line-Of-Sight (LOS) communication, frequently between ground stations, aerial platforms (UAVs), and/or tiny cells, as a transport medium for fronthaul or backhaul in 5G and forthcoming 6G networks. FSO communication has emerged as a viable alternative for high-capacity and low-latency fronthaul in 5G and 6G networks, especially in regions where fiber construction is impracticable or prohibitively expensive.

The study [117] presented an optimum FSO fronthaul structure for 5G C-RAN connectivity between RRHs and BBU pools to save energy. A nonlinear programming (MINLP) model that accounts for atmospheric attenuation, beam divergence loss, and power constraints was used to optimize link alignment and optical power allocation to reduce signal degradation under turbulence and pointing errors.

Adaptive Modulation and Coding (AMC) and hybrid link switching strategies between FSO and mmWave-fibre links were proposed in [118] for FSO-based fronthaul networks for future 6G architectures to identify performance constraints and propose adaptive solutions for reliable optical-wireless transport. A link-layer and network-layer analytical methodology was created to assess FSO performance implications of air turbulence and weatherinduced fading. In [119], scientists analyzed hybrid FSO-PON connection performance under dynamic load circumstances using optical modelling and experimental testing.

![](_page_21_Picture_1.jpeg)

TABLE II. MAIN STRATEGIES USED IN IN-OPERATION OPTICAL NETWORK PLANNING.

| Ref.  | Strategy                         | Purpose                                        | Method used                                | 6G relevance                      |  |
|-------|----------------------------------|------------------------------------------------|--------------------------------------------|-----------------------------------|--|
| [120] | Spectrum Defragmentation         | Free unused spectrum during operation          | •<br>ILP<br>•<br>Heuristic reconfiguration | Keeps bandwidth flexible          |  |
| [121] | Dynamic Traffic Re-Configuration | Adjust capacity based on traffic<br>changes    | ML and heuristic routing                   | Enables smart adaptive networks   |  |
| [122] | Multi-Path Routing               | Maintain service during link failures          | ILP and backup routing                     | Improves reliability              |  |
| [123] | Resource Visualization           | Monitor fibre uses in real time                | GIS or digital-twin tools                  | Supports self-planning networks   |  |
| [124] | Cluster-Based Deployment         | Upgrade networks in small steps                | Regional clustering                        | Scalable for wide-area 6G rollout |  |
| [125] | Traffic Grooming                 | Combine small flows into large ones            | Aggregation heuristics                     | Saves power and spectrum          |  |
| [126] | Adaptive Routing (RWA)           | Choose best path and wavelength<br>dynamically | First-Fit or Least-Used algorithms         | Enables real-time path control    |  |
| [127] | Cross Layer Planning             | Coordinate optical and IP layers               | Multi-objective SDN optimization           | Supports network slicing          |  |
| [128] | Node or OLT Optimization         | Add or move nodes as demand grows              | Location-allocation models                 | Cost-efficient upgrades           |  |
| [129] | Optical Margin Reduction         | Reduce excess power or safety margins          | Power-budget adjustment                    | Frees resources, lowers cost      |  |

Introduce high-capacity FSO-based PON architecture for 5G fronthaul. Their project aimed to decrease fibre reliance by integrating WDM with FSO transmission. By employing machine-learning-assisted channel estimation and adaptive modulation, Environment-Aware Geometric Shaping (EGS) for digital FSO fronthaul networks was presented in [130] to increase spectral efficiency and link flexibility. Adapting modulation geometry to real-time atmospheric channel circumstances was the goal. This adaptable method boosts performance and enables high-density 6G fronthaul networks in changing environments.

In 5G/6G networks, hybrid fibre FSO or fibre-optical wireless converged fronthaul designs provide cost, performance, and deployment flexibility. These systems combine dependable, high-bandwidth fibre connections with FSO or other optical wireless technology to provide flexible, high-speed communication in areas where fibre is costly or unavailable. Fiber and wireless optical fronthaul with end-to-end 4G support of 5G traffic were shown in [131].

They achieved hybrid optical-wireless transmission with little loss by transmitting 5G via an 8 km fibre and 55 m FSO connection. Similarly, the study [132] suggested a cost-effective PON-FSO hybrid fronthaul to C-RAN architectures and showed that FSO in a hybrid fronthaul with passive optical networks can reduce deployment cost and improve dense small-cell deployment scalability. Based on these methods, the study [133] suggested a hybrid FSO system (over 5G) that employs spread spectrum coding and graphene-based optical modulators to strengthen connections in air turbulence.

The high data transfer speeds and durability of FSO make it crucial for ultra-dense 6G small-cell networks. In another aspect, the study [134] optimized the combined fibre and FSO infrastructure planning in IAB networks. They optimize topologies and share resources to save costs and increase network availability. Furthermore, [135] studied hybrid FSO/mmWave fronthaul network coverage under changing weather conditions and how rain and fog affect connection dependability. Their adaptive switching between FSO and mmWave ensured service continuity, proving durable hybrid x-haul architectures are possible. According to these studies, fibre/FSO fronthaul systems can deliver fibre-like performance at lower prices and implementation time. In congested urban and isolated rural regions with limited fibre rollout, they are valuable. More research is needed to improve smart hybrid optical-wireless management and optimization of 6G networks, since link alignment, weather resilience, and compatibility with new improved RAN paradigms like O-RAN and distributed MIMO remain issues. Moreover, in [136], the authors investigated the development of the fronthaul section in next-generation mobile networks, emphasizing open designs like the O-RAN Alliance and the essential technologies that allow flexible optical fronthaul. The utilization of AI/ML for sophisticated fronthaul management has been augmented. The authors assert that forthcoming fronthaul networks must incorporate optical transmission, software-defined control, and intelligence to fulfil 6G objectives, while also emphasizing deficiencies in latency, scalability, and standardization.

High-capacity and low-latency fronthaul systems that support massive MIMO and distributed RANs are in demand due to the rapid development of 5G and 6G networks. ARoF and Radio-over-Free-Space Optical (RoFSO) systems, which directly carry radio signals across optical or optical-wireless channels, have been researched to meet these high criteria. These methods reduce latency, eliminate complicated digital processing at remote units, and enable broadband signal transfer over fronthaul links. A 6G distributed MIMO link-based experimental fronthaul connection for analogue RoFSO was tested in the work [137].

To reach 5G New Radio (NR) signal transmission over an FSO channel, they utilized Long-Wave Infrared (LWIR) optical transmission. The findings proved RoFSO lines can deliver the necessary signal quality for future distributed fronthaul systems, including 5G/NR standards like ACLR

![](_page_22_Picture_1.jpeg)

and Error Vector Magnitude (EVM). In order to efficiently service ultra-dense small-cell networks, the authors of [138] present a 5G RAN architecture that combines ARoF with Ultra-Dense Wavelength-Division Multiplexing (UDWDM). The model emphasizes the ability of ARoF links to aggregate radio carriers without digital conversion, allowing for scalable massive MIMO deployments. For managing massive fronthaul data flows, ARoF with UDWDM provides an affordable solution.

To top it all off, the research [139] developed a hybrid system for high-capacity fronthaul and backhaul transmission using Mode-Division-Multiplexing (MDM) and MIMO radio over free-space optical. The results of their experiments indicated that optical-wireless analogue transmission in 6G situations could be achieved using a 4×4 MIMO configuration with MDM, greatly enhancing spectral efficiency and bit-error performance even in the presence of atmospheric turbulence. All the aforementioned research shows that (ARoF/RoFSO) technologies are a sound foundation for 5G and 6G networks to enable distributed RAN, low-latency fronthaul, and massive MIMO. They merge the benefits of optical fiber bandwidth with those of analogue signal transmission. However, issues like air turbulence and non-linear distortion exist.

In the upcoming 6G networks, optical wireless technologies like LiFi [140], [141], [142], [143], [144], [145], [146], [147], [148], [149], [150] and VLC will play an increasingly important role as both user access links and fronthaul infrastructure. This research aims to bridge the gap between optical wireless access research (LiFi/VLC) and optical fronthaul development, demonstrating how light-based wireless communication can serve as a unified access for 6G networks.

In order to improve optical wireless communication for 6G networks, the research [151] looked into integrating LiFi with Reconfigurable Intelligent Surfaces (RIS). By using RIS panels to reroute the optical signals, their goal was to circumvent LiFi's coverage and line-of-sight limits. Their findings demonstrated that the incorporation of LiFi-RIS enhances channel gain, coverage, and energy efficiency, positioning it as a promising contender for access fronthaul convergence in upcoming 6G systems. In addition, research [152] looks into VLC/LiFi from a techno-economic standpoint in relation to 6G. The paper offers dimensionality criteria such as optical cell radius, density, and cost trade-offs, and evaluates several design approaches (VLC vs. IR-based LiFi). A separate study [153] aims to identify and quantify the synchronization requirements (time, frequency, latency) for fronthaul links in distributed MIMO configurations utilizing LiFi systems, analyze a distributed LiFi architecture wherein multiple remote optical units are interconnected through a fronthaul network to a central unit, and model the impacts of timing/frequency misalignment, jitter, and propagation delays. They emphasize that typical Ethernet-based fronthaul requires enhancement with synchronization protocols (e.g., PTP, SyncE) and low-latency transport techniques to facilitate LiFi distributed MIMO.

The cost and resilience of optical wireless fronthaul systems under different atmospheric conditions, including fog, rain, and turbulence, are the main topics of the following research. Despite their adaptability and low cost, hybrid fiber FSO-mmWave designs are vulnerable to environmental factors that compromise connection availability and reliability, which these studies attempted to address. A hybrid DWDM-FSO architecture with 90 users and 5.4 Tbps data rate was proposed in [154]. They evaluated a hybrid Dense Wavelength Division Multiplexing Free Space Optical (DWDM-FSO) system with integrated 3\*3 MIMO-FSO to improve resilience for 6G networks' high-capacity and low-latency needs. They intended to assess how fog, rain, and turbulence affect link quality and system reliability. The hybrid system performed well in moderate weather with a high Q-factor and BER. DWDM with MIMO-FSO improved nextgeneration optical-wireless fronthaul throughput and robustness. The authors of [155] model both the cost components (fiber deployment, wireless FSO/THz equipment) and availability metrics in various network topologies (point-to-multipoint and point-to-point) embedded in different geographic contexts (dense-urban vs. suburban). They investigated the installation of hybrid FSO and THz lines in order to conduct a cost-benefit analysis of future 6G network access segments. Hybrid FSO-THz installations can only achieve acceptable availability and cost reductions provided the wireless equipment's cost scaling factor is below a particular threshold (α < 180 in this case).

The above analyzed research illustrates advancements in creating cost-effective, durable, and high-capacity optical fronthaul technologies for 5G and 6G networks.

From sophisticated PON and TWDM-PON systems to hybrid fiber-wireless and LiFi-based fronthaul designs. **Table III** encapsulates the principal research and recent contributions on optical wireless and optical fronthaul systems for 5G and 6G networks, emphasizing critical information like aims, methodologies, designs, settings, and essential characteristics such as data throughput, latency, and BER. These studies encompass both modelling and experimental research, demonstrating the application of technologies like FSO, PON, LiFi, THz, and RIS in constructing more dependable and cost-effective fronthaul links for next-generation networks. A considerable quantity of recent research has concentrated on incorporating of LiFi into optical fronthaul and access networks, emphasizing its capacity to provide elevated data speeds, enhanced spectrum efficiency, and less interference relative to conventional RF systems.

![](_page_23_Picture_1.jpeg)

TABLE III. ANALYSIS OF OPTICAL WIRELESS AND OPTICAL FRONTHAUL CONTRIBUTIONS BY RECENT STUDIES FOR 5G/6G NETWORKS.

|                        |       | Objective                                                              |                                                           |                                                   | Ir         | nple         | men           | tation                |                          |                  |                    | Access ty<br>chnology<br>mappi | layer                           |                            |                                                 |
|------------------------|-------|------------------------------------------------------------------------|-----------------------------------------------------------|---------------------------------------------------|------------|--------------|---------------|-----------------------|--------------------------|------------------|--------------------|--------------------------------|---------------------------------|----------------------------|-------------------------------------------------|
| Class /<br>Category    | Ref.  |                                                                        | Method                                                    | Architecture                                      | Simulation | Experimental | ATL / SL      | Tool                  | CT                       | DE               | Integrated Study   | Access Type                    | Typical Technologies            | Layer                      | P                                               |
|                        | [117] | Design optimal<br>FSO fronthaul for<br>CRAN ensuring<br>low latency    | Optimal FSO<br>Fronthaul<br>Framework (OFF-<br>5G-CRAN)   | Cloud-RAN                                         | <b>√</b>   | х            | ✓             | ML /<br>SL            | FSO-only                 | 0                | х                  | ACT                            | FSO                             | Fronthaul                  | Data rate, Link<br>range, Latency               |
|                        | [119] | Develop hybrid<br>FSO-PON for 5G<br>urban deployment                   | FSO-PON Hybrid<br>Fronthaul<br>Architecture               | Hybrid<br>PON–FSO                                 | ✓          | х            | х             | OS                    | Hybrid<br>FSO-<br>PON    | O<br>(Urban)     | <b>√</b>           | НҮВ                            | FSO +<br>PON                    | Fronthaul<br>/ Access      | Data rate,<br>Range, BER                        |
| In                     | [130] | Adaptive<br>modulation<br>scheme to improve<br>link robustness         | Environment-<br>Aware Geometric<br>Shaping (EAGS)         | Digital FSO<br>Fronthaul                          | 1          | х            | х             | ML /<br>CS            | FSO-only                 | 0                | х                  | ACT                            | FSO<br>(Modulat<br>ed)          | Fronthaul                  | Wavelength,<br>Modulation,<br>BER               |
| FSO / Hybrid Fronthaul | [131] | Validate hybrid<br>fiber–wireless<br>coexistence                       | Hybrid Fiber–<br>Wireless Fronthaul<br>Demonstrator       | Hybrid<br>Fiber–<br>Wireless C-<br>RAN            | х          | <b>√</b>     | х             | НТ                    | Fiber +<br>Wireless      | В                | <b>√</b>           | НҮВ                            | Fiber +<br>Wireless             | Fronthaul<br>/ Midhaul     | Wavelength,<br>Frequency,<br>BER                |
| Hybrid                 | [132] | Propose cost-<br>efficient PON–<br>FSO solution                        | Low-Cost PON–<br>FSO Model (LC-<br>FSO)                   | 5G C-RAN                                          | <b>√</b>   | х            | <b>√</b>      | OS /<br>ML            | Hybrid<br>PON–<br>FSO    | 0                | <b>√</b>           | НҮВ                            | PON +<br>FSO                    | Fronthaul<br>/ Access      | Wavelength,<br>Modulation,<br>Split ratio       |
| FSO /                  | [133] | Enhance FSO<br>fronthaul using<br>graphene<br>modulators               | Spread Spectrum<br>Coded Graphene-<br>FSO (SSC-GFSO)      | Beyond 5G<br>FSO Link                             | <b>√</b>   | <b>~</b>     | х             | COMS<br>OL /<br>OS    | FSO-only                 | I (Prototype)    | x                  | ACT                            | Graphene<br>FSO                 | Fronthaul                  | Data rate,<br>Coding, BER                       |
|                        | [134] | Optimize hybrid<br>fiber–FSO<br>infrastructure for<br>IAB              | Joint Fiber–FSO<br>Planning<br>Algorithm (JF-<br>FSO-IAB) | Integrated<br>Access and<br>Backhaul<br>(IAB)     | <b>√</b>   | x            | <b>√</b>      | ML /<br>OM            | Hybrid<br>Fiber–<br>FSO  | 0                | <b>√</b>           | НҮВ                            | Fiber +<br>FSO                  | IAB /<br>Backhaul          | Cost ratio,<br>Capacity,<br>Range               |
|                        | [135] | Evaluate<br>availability and<br>reliability of<br>FSO/mmWave           | Hybrid<br>FSO/mmWave<br>Reliability Model<br>(HFRM)       | Hybrid<br>FSO-<br>mmWave C-<br>RAN                | ✓          | x            | ✓             | ML /<br>CS            | Hybrid<br>FSO–<br>mmWave | 0                | ✓                  | НҮВ                            | FSO +<br>mmWave                 | Fronthaul<br>/ Midhaul     | Wavelength,<br>Frequency,<br>Availability       |
|                        | [137] | Validate analog<br>Ro-FSO for 6G<br>distributed MIMO                   | Analog Ro-LWIR<br>FSO Fronthaul<br>Link                   | 6G<br>Distributed<br>MIMO                         | х          | <b>√</b>     | х             | НТ                    | FSO-only                 | В                | Х                  | ACT                            | Analog<br>Ro-FSO<br>(LWIR)      | Fronthaul                  | Wavelength (10<br>μm), BER,<br>SNR              |
| su                     | [138] | Design UDWDM-<br>PON analog RoF<br>fronthaul for 5G<br>RAN             | Analog RoF<br>UDWDM-PON<br>Fronthaul                      | 5G RAN<br>Hybrid RoF-<br>PON                      | <b>√</b>   | х            | ✓             | OS /<br>ML            | Fiber /<br>PON           | 0                | ✓                  | НҮВ                            | RoF +<br>UDWDM<br>-PON          | Fronthaul                  | Wavelength,<br>Channel<br>spacing, Gain,<br>SNR |
| Hybrid Systems         | [139] | Propose hybrid<br>MDM-MIMO<br>RoFSO system for<br>high-capacity 5G+    | Hybrid MDM-<br>MIMO RoFSO<br>Model                        | 5G/Beyond<br>FSO-MIMO                             | ✓          | x            | x             | ML /<br>SL            | Hybrid<br>RoFSO          | 0                | <b>~</b>           | НҮВ                            | MDM +<br>MIMO<br>FSO            | Fronthaul<br>/<br>Backhaul | Data rate,<br>Scintillation<br>index, BER       |
|                        | [151] | Explore LiFi<br>integration with<br>RIS for 6G access                  | LiFi-RIS<br>Framework for 6G                              | LiFi + RIS<br>Hybrid 6G                           | х          | X            | <b>\</b>      | ATL                   | Optical /<br>LiFi-RIS    | I                | <b>&gt;</b>        | ACT                            | LiFi +<br>RIS                   | Access /<br>Fronthaul      | Path loss, RIS<br>elements,<br>Coverage         |
| 6G / Advanced          | [152] | Assess economic<br>feasibility of dense<br>VLC/IR access               | VLC/IR Dense<br>Access Model                              | Optical<br>Wireless<br>Access<br>Network<br>(OWA) | х          | х            | <b>√</b>      | CS                    | VLC/IR                   | В                | x                  | ACT                            | VLC / IR<br>Optical<br>Wireless | Access                     | Cost, Power,<br>Data rate                       |
|                        | [153] | Analyze sync<br>requirements for<br>distributed LiFi<br>MIMO fronthaul | LiFi Distributed<br>MIMO Sync<br>Model                    | LiFi-MIMO<br>Fronthaul                            | х          | ✓            | ✓             | HT /<br>ML            | LiFi-only                | I                | х                  | ACT                            | LiFi<br>MIMO                    | Fronthaul<br>/ Midhaul     | Clock offset,<br>BER,<br>Throughput             |
|                        | [154] | Analyze DWDM-<br>FSO system<br>performance and<br>reliability          | Hybrid DWDM-<br>FSO Model                                 | 6G Hybrid<br>DWDM-<br>FSO<br>Fronthaul            | <b>√</b>   | x            | ✓             | OS /<br>ML            | Hybrid<br>DWDM-<br>FSO   | 0                | <b>√</b>           | НҮВ                            | DWDM +<br>FSO                   | Fronthaul                  | Wavelength<br>grid, BER, SNR                    |
| Terms                  |       | CT: Channel tyj<br>Simulink; OM:                                       | pe; P: Parameters Optimization mod                        | ; DE: Deploy<br>lel; CS: Custo                    | men<br>miz | t env        | viron<br>mula | ment (I:<br>ation; HT | indoor, O:               | outdoo<br>testbe | or, B: l<br>ed; AT | ooth); M<br>L: Analy           | L: MATLA<br>tical; ACT:         | AB; OS: Op<br>Active; H    | otiSystem; SL:<br>YB: Hybrid;                   |

A two-way LiFi system using POF as a wired feeder to interact with a LiFi wireless link was proposed in [156]. This evaluated POF-LiFi's capacity to transmit data quickly for short-range communication within a building. Through an experimental infrastructure, the authors examined

uplink and downlink performance utilizing POF alone, LiFi alone, and POF and LiFi together. POF provides robust gigabit connections without rate limiting, although wireless channel losses degrade performance when utilized with LiFi devices.

![](_page_24_Picture_1.jpeg)

TABLE IV. SUMMARY OF LIFI-BASED OPTICAL WIRELESS FRONTHAUL CONTRIBUTIONS BY RECENT STUDIES FOR 5G/6G NETWORKS.

|       | Perf                                                         | orman      | ce met                                     | ric               | cy                       | / 0                                                             |                                   |                                                                                                                                                                                                  |
|-------|--------------------------------------------------------------|------------|--------------------------------------------|-------------------|--------------------------|-----------------------------------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ref.  | Data rate / throughput Latency Bit Error Rate (BER) SNR (dB) |            | SNR (dB)                                   | Energy efficiency | Fronthaul type<br>medium | Environment                                                     | Key findings                      |                                                                                                                                                                                                  |
| [156] | ~1 Gbps                                                      | < 5<br>ms  | 10 <sup>-6</sup><br>-<br>10 <sup>-7</sup>  | 25–30<br>dB       | Moderate                 | Bidirectional<br>LiFi over<br>POF                               | Indoor<br>(short-<br>reach)       | Demonstrated stable bidirectional LiFi throughput<br>and low distortion over POF, proving feasibility of<br>cost-effective short-range optical fronthaul.                                        |
| [157] | ≤ 5 Gbps<br>(WDM-<br>aggregate<br>d)                         | < 10<br>ms | 10-6                                       | 28 dB             | High                     | D-MIMO +<br>WDM over<br>POF                                     | Indoor<br>(multi-cell)            | Real-time G.hn-based LiFi infrastructure achieved high capacity and minimal crosstalk, supporting scalable, low-latency 6G fronthaul.                                                            |
| [158] | ~0.5<br>Gbps per<br>node                                     | 5–15<br>ms | 10-5                                       | 20–25<br>dB       | +30 % vs<br>baseline     | Hybrid LiFi-<br>IoT network                                     | Smart<br>building /<br>indoor IoT | Enhanced LiFi for IoT environments; improved energy efficiency and adaptive illumination scheduling for hybrid access—fronthaul 6G systems.                                                      |
| [106] | 10 Gbps                                                      | < 1<br>μs  | 10-9                                       | 35 dB             | High                     | Optical-<br>wireless (LiFi<br>+ optical<br>modulation)          | Aerospace /<br>terrestrial        | Achieved ultra-low latency and high throughput with strong signal integrity, validating LiFi-based optical-wireless fronthaul for 6G mission-critical networks.                                  |
| [159] | 6.5 Gbps                                                     | < 2<br>ms  | 10 <sup>-8</sup><br>-<br>10 <sup>-9</sup>  | 32–36<br>dB       | Moderate                 | All-optical<br>distributed<br>MIMO LiFi<br>system               | Indoor /<br>laboratory            | Compared a spatial diversity and multiplexing in LiFi system using distributed MIMO and achieved high throughput, stable, demonstrating potential signal for massive MIMO 6G fronthaul networks. |
| [160] | Up to 20<br>Gbps                                             | < 2<br>ms  | 10 <sup>-9</sup><br>-<br>10 <sup>-10</sup> | 38–40<br>dB       | High                     | Hybrid<br>OFDM-based<br>HS-PON with<br>front-end LiFi<br>system | Indoor /<br>access<br>fronthaul   | Integrated OFDM-enabled high-speed PON with LiFi front-end for 5G fronthaul; reduced BER and boosted throughput for 6G optical-wireless integration.                                             |

TABLE V. COMPARATIVE ANALYSIS OF FRONTHAUL/OPTICAL TECHNOLOGIES.

| Technology      | Capacity               | Latency   | Deployment<br>Cost | Advantages                              | Limitations                    |  |  |
|-----------------|------------------------|-----------|--------------------|-----------------------------------------|--------------------------------|--|--|
| Fiber (PON/WDM) | Very High              | Ultra-low | High               | Reliability, maturity                   | Expensive, limited flexibility |  |  |
| FSO             | High                   | Low       | Medium             | Fast deployment, high bandwidth         | Weather sensitivity            |  |  |
| VLC / LiFi      | High (short-<br>range) | Low       | Low-Medium         | Spectrum availability, low interference | Limited range, LOS requirement |  |  |
| mmWave          | High                   | Low       | Medium             | Wireless flexibility                    | Blockage, attenuation          |  |  |

POF can be a low-cost feeder to LiFi-based optical fronthaul, however further distance and mobility impacts were not investigated. Another research [157] combined POF-wired fronthaul with Distributed MIMO (D-MIMO) and Wavelength Division Multiplexing for real-time LiFi. A fast, low-latency hybrid network for 5G and 6G communication was the goal. An effective POF-based fronthaul may accommodate several wavelengths and LiFi cells, as shown by the authors' hardware prototype. This design provides steady and high-capacity data transport, according to the findings. However, only indoor and small-scale testing was done.

Recent research and recent contributions on 5G and 6G networks using optical-wireless fronthaul systems based on LiFi is shown in **Table IV**. Generally speaking, these studies demonstrate LiFi as an excellent candidate for

future hybrid optical-wireless 6G fronthaul networks due to its ability to deliver multi-Gbps speeds, low latency, and great efficiency. Improved LiFi technology for upcoming IoT and 6G communication systems is the goal of the ELIoT project, which was suggested in [158].

The primary goal of using D-MIMO technology was to create a hybrid optical wireless fronthaul that could accommodate several users at once and link LiFi access points with POF WDM. Furthermore, the authors demonstrated high-speed, low-latency performance appropriate for dense indoor IoT environments by testing real-time LiFi hardware that was combined with the POF-based fronthaul. By incorporating an optical wireless fronthaul link through VL or a comparable optical wireless communication system, the authors [106] aimed to improve the current wired protocol (FC AE 1553), used in space

![](_page_25_Picture_1.jpeg)

station networks, and create a Hybrid Space Network (HSN) that could withstand the rigors of space travel without sacrificing reliability or throughput. Models demonstrate that, compared to the initial FC-AE-1553 network, the HSN is capable of achieving throughputs around 20 times greater and latency reductions of about 87%.

A distributed MIMO design for a LiFi system connected using POF as the front-haul was examined in the paper [159]. Spatial diversity improves link dependability, while spatial multiplexing raises system throughput. Results reveal that diversity works better when users are near or channels are bad, whereas multiplexing increases capacity when channels are good. In indoor LiFi implementations, it is recommended to dynamically switch between modes for best performance. Another research [160] reported a bidirectional High-Speed Passive Optical Network (HS-PON) solution for 5G fronthaul using an OFDM-modulated TWDM-PON and a front-end LiFi wireless connection. They stimulated 4 downlink and 4 uplink channels at 50 Gb/s each using 16-QAM OFDM via fiber and LiFi, then analyzed BER, OSNR, receiver sensitivity, and range. Although simulation-based and focused on indoor/fronthaul scale, the study shows that hybrid opticalwired plus optical-wireless designs can address 5G highcapacity fronthaul demands.

**Table V** provides a structured comparison of candidate fronthaul technologies in terms of key performance metrics, deployment considerations, and operational constraints. Fiber-based solutions offer superior capacity and reliability but suffer from high deployment cost and limited flexibility. In contrast, optical wireless technologies such as FSO and LiFi provide rapid deployment and cost advantages, albeit with sensitivity to environmental conditions and range limitations. This comparison highlights the trade-offs that must be considered when selecting appropriate fronthaul solutions for 5G and 6G networks.

### **VII. THE ROLE OF AI AND ITS IMPACT**

With the proliferation of complicated hybrid FSO, RoF, local area network (LiFi/VLC), and MIMO systems, smart control methods that can make decisions across several layers of the network stack in real-time are essential. With the use of AI-powered methods, physical, transport, and network layers may all be optimized simultaneously, turning static DBA and heuristic traffic engineering, two rule-based approaches, into systems that can forecast, adapt, and self-organize.

### *A. THE ROLES*

The following subsections introduce and discusses how AI will contribute to the fronthaul and optical technologies.

### 1) *AI-ENABLED TRAFFIC FORECASTING AND PROACTIVE CAPACITY MANAGEMENT*

Optical access and fronthaul traffic predictions [161] can be improved with the help of ML algorithms, such as RL and deep neural networks. Intelligent RRH/AAU placement, adaptive activation of OLTs and ONUs, and proactive DBA are all made possible by AI's ability to forecast spatiotemporal traffic demand. In integrated fiberwireless networks and TWDM-PON in particular, this predictive management considerably lessens congestion and overprovisioning in comparison to reactive schemes. Services that are sensitive to latency, like uRLLC and network slicing in 6G networks, greatly benefit from these features.

### 2) *ADAPTIVE PHY-LAYER OPTIMISATION AND INTELLIGENT LINK CONTROL*

Coherent optical connections, RoFSO systems, and LiFi/VLC channels can all benefit from AI-assisted adaptive modulation, coding, power allocation, and DSP parameter tweaking at the physical layer [162]. AI-based techniques may optimize transmission parameters in advance and anticipate link deterioration [163], unlike traditional AMC systems. These algorithms take use of previous channel behavior and environmental data, such as turbulence, fog, and rain. Since channel conditions can fluctuate non-linearly and quickly, this is especially important for FSO and optical wireless communications.

### 3) *INTELLIGENT BEAM MANAGEMENT AND ALIGNMENT IN OPTICAL WIRELESS SYSTEMS*

Achieving precise beam alignment [164] and aiming is a significant problem for FSO and highly directed optical wireless communications. Automated fine beam steering, jitter correction, and quick re-alignment may be achieved for mobile platforms like UAVs, HAPs, and moving AAUs using AI approaches that combine computer vision, sensor fusion, and deep RL. More dependable deployment of FSO-based fronthaul and backhaul systems in dynamic situations is made possible by these features, which decrease human calibration overhead and boost connection availability.

### 4) *AI-DRIVEN RESILIENCE AND HYBRID LINK ORCHESTRATION*

AI plays a critical role in improving network resilience through intelligent orchestration of hybrid links [165], [166]. By learning the performance characteristics and failure patterns of each technology, AI agents can dynamically switch or load-balance traffic across multiple paths to meet SLA requirements. For instance, during adverse weather conditions that degrade FSO links, AI can proactively reroute traffic to mmWave or fiber alternatives, thereby improving overall service availability and robustness.

![](_page_26_Picture_1.jpeg)

TABLE VI. SUMMARY OF AI ROLES, IMPACTS, AND MITIGATIONS.

| AI role / function                            | Positive impact                                         | Potential negative impact               | Key mitigation / requirement              |  |
|-----------------------------------------------|---------------------------------------------------------|-----------------------------------------|-------------------------------------------|--|
| Traffic forecasting & demand prediction       | Proactive DBA, reduced congestion, improved utilisation | Forecast errors causing misallocation   | Ensemble learning, uncertainty estimation |  |
| Adaptive resource allocation (DBA, slicing)   | Lower latency, higher efficiency                        | Control instability, slice interference | Stability constraints, safety guards      |  |
| PHY/link adaptation (modulation, coding, DSP) | Improved spectral efficiency and robustness             | BER degradation if misconfigured        | Conservative fallbacks, verified profiles |  |
| FSO beam pointing & alignment                 | Higher link availability, faster reacquisition          | Control-loop failure, beam loss         | Redundant sensing, watchdog mechanisms    |  |
| Hybrid link switching (FSO/mmWave/fiber)      | Enhanced resilience and SLA compliance                  | Link flapping and oscillations          | Hysteresis and SLA-aware policies         |  |
| OPM & predictive maintenance                  | Reduced downtime and OPEX                               | False alarms, missed failures           | Human-assisted RCA validation             |  |
| Security & anomaly detection                  | Early attack and fault detection                        | Adversarial evasion, data poisoning     | Secure telemetry, adversarial training    |  |
| SDN orchestration & intent translation        | Automated slicing and fast reconfiguration              | Incorrect intent mapping                | Formal verification, staged rollout       |  |
| Edge & federated learning                     | Low latency, privacy preservation                       | Convergence and heterogeneity issues    | Model personalisation, QoS-aware training |  |
| Digital twins & AI-driven planning            | Safe optimisation and TCO reduction                     | Simulation-reality mismatch             | High-fidelity models and retraining       |  |

### 5) OPTICAL PERFORMANCE MONITORING AND PREDICTIVE MAINTENANCE

AI along with OPM and high-frequency telemetry allows for automated RCA and predictive maintenance [167], [168]. Before issues like fiber aging, connection defects, or power budget violations occur, ML models may identify small degradations in optical signal characteristics. Increased network dependability decreased operating expense, and Mean Time To Repair (MTTR) are all outcomes of this proactive strategy for large-scale fronthaul installations.

## 6) SECURITY AND ANOMALY DETECTION AT THE OPTICAL LAYER

Optical fronthaul networks can be better protected using AI-based anomaly detection [169], [170], which can spot distorted signals, unusual traffic patterns, or OPM abnormalities linked to coordinated fiber-cut assaults, eavesdropping, or fiber tapping. In identifying low-visibility threats, both supervised and unsupervised learning approaches outperform standard threshold-based monitoring. It is necessary to handle the new attack surfaces brought about by AI dependence through secure telemetry and strong model design. These surfaces include adversarial manipulation and data poisoning.

## B. CHALLENGES AND NEGATIVE IMPACTS OF AI ADOPTION

Although AI has many benefits, there are several obstacles to integrating it into optical wireless and fronthaul networks. For uncommon occurrences like severe weather or widespread failures, model generalizability is hindered by data paucity, domain change, and seasonal fluctuation. Also, when it comes to mission-critical fronthaul applications, black-box AI models [171] make people

nervous about their trustworthiness, explainability, and safety. Added difficulties include susceptibility to hostile assaults, rising computing and energy expenses, and complicated systems. These problems call for meticulous system planning, verification, and management.

### C. MITIGATION STRATEGIES AND DESIGN PRINCIPLES

Hybrid control architectures combining learning-based optimization with rule-based protections and human-in-the-loop monitoring can be used by AI-based fronthaul systems to guarantee safe and successful deployment. Addressing privacy and non-stationarity can be done through constant learning and federated learning [172], while explainable AI (XAI) technologies [173] can increase transparency and operational confidence. To validate AI rules under varied failure situations before real-world deployment, digital twins and simulation-in-the-loop testing provide a controlled environment. **Table VI** introduces the role of AI, impact, and requirements.

#### **VIII. CONCLUSIONS AND FUTURE DIRECTIONS**

6G technology offers new applications that can fulfil various social requirements with high-performance, and capacity compared to current abilities. The fronthaul sector is an essential part of 6G networks, which provides high-capacity low-latency connections to end users. In this paper, the development of optical fronthaul technologies in 5G to develop 6G networks has been reviewed and analyzed. This study clarified the fronthaul requirements of 5G and 6G systems and demonstrated how optical and optical-wireless technologies can effectively satisfy these demands.

Since 6G systems aim to achieve both ultra-high datarates and sub-millisecond latency, massive connectivity,

![](_page_27_Picture_1.jpeg)

and smart operation of networks, the fronthaul segment becomes a performance bottleneck and architectural facilitator. Fiber-based systems like IM/DD, WDM-PON, TWDM-PON, and coherent transmission systems were also discussed with respect to capacity, spectral efficiency, scalability, and complexity of deployment. Although IM/DD is appropriate in short-reach connections, coherent systems have better spectral efficiency and drive thus making them good contenders to scalable 6G fronthaul systems.

Optimization of fronthaul infrastructure in 6G presents a big challenge and there is a need to combine the efforts of academics and industry to realize the full potential of 6G networks. As P2P, PON, and FSO, optical technologies play a vital role in achieving high capacity, low latency, high reliability, and security required by all types of splitting options in 5G/6G fronthaul. Moreover, this needs a new latency management approach that would classify and rank different services based on urgency to be able to meet the diverse latency needs of different emerging applications. Optical fronthaul and access networks can be enhanced with AI to be efficient and robust.

Future studies should develop strong and explainable AI models that can work reliably under different network conditions. However, existing technologies improve traffic prediction, adaptive resource planning, and connection management, yet there are many challenges related to optical networks that guarantee the safety, stability, and reliability of AI-related decisions. By integrating digital twin technologies with federated and edge learning, realtime simulation, predictive maintenance, and collaborative intelligence may be achieved at the expense of privacy protection, Latency, spectrum efficiency, and energy optimization can also be improved with the help of crosslayer AI optimization, where physical, link, and orchestration levels are combined.

### **ACKNOWLEDGMENT**

The authors would like to express their gratitude to UNITAR International University for supporting this research.

### **REFERENCES**

- [1] S. S. Murad, S. Yussof, and R. Badeel, "Wireless Technologies for Social Distancing in The Time Of COVID-19: Literature Review, Open Issues, and Limitations," *Sensors*, vol. 22, no. 6, p. 2313, 2022.
- [2] S. S. Murad, R. Badeel, R. A. Ahmed, and S. Yussof, "Using Drones and Robots for Social Distancing: Literature Review, Challenges and Issues," in *2024 Panhellenic Conference on Electronics and Telecommunications, PACET 2024 - Proceedings*, Institute of Electrical and Electronics Engineers Inc., 2024. doi: 10.1109/PACET60398.2024.10497066.
- [3] S. S. Murad, S. Yussof, R. Badeel, and W. Hashim, "A Novel Social Distancing Approach for Limiting the Number of Vehicles in Smart Buildings Using LiFi Hybrid - Network," *Int. J. Environ. Res. Public Health*, vol. 20, no. 4, p. 3438, 2023, doi: /10.3390/ijerph20043438.
- [4] S. S. Murad, S. Yussof, R. Badeel, and R. A. Ahmed, "Impact of COVID-19 Pandemic Measures and Restrictions on Cellular Network Traffic in Malaysia," *International Journal of Advanced Computer Science and Applications*, pp. 630–645, 2022.

- [5] Int. Telecommun. Union, "IMT Traffic Estimates for the Years 2020 to 2030, ITU-Rec. M.2370-0," 2015. Accessed: Apr. 11, 2026. [Online]. Available: www.itu.int/pub/R-REP-M.2370-2015.
- [6] M. Agiwal, A. Roy, and N. Saxena, "Next generation 5G wireless networks: A comprehensive survey," *IEEE Communications Surveys \& Tutorials*, vol. 18, no. 3, pp. 1617–1655, 2016.
- [7] W. Jiang, B. Han, M. A. Habibi, and H. D. Schotten, "The road towards 6G: A comprehensive survey," 2021, *Institute of Electrical and Electronics Engineers Inc.* doi: 10.1109/OJCOMS.2021.3057679.
- [8] Samsung, "The Next Hyper-Connected Experience for All," South Korea, 2020. Accessed: Aug. 06, 2025. [Online]. Available: https://cdn.codeground.org/nsr/downloads/researchareas/20201201\_6 G\_Vision\_web.pdf
- [9] Huawei, "6G: The Next Horizon White Paper," Huawei, Shenzhen, China, 2022. Accessed: Jul. 08, 2025. [Online]. Available: https://www.huawei.com/en/huaweitech/future-technologies/6gwhite-paper
- [10] S. A. Abdel Hakeem, H. H. Hussein, and H. W. Kim, "Vision and research directions of 6G technologies and applications," Jun. 01, 2022, *King Saud bin Abdulaziz University*. doi: 10.1016/j.jksuci.2022.03.019.
- [11] M. Polese, L. Bonati, S. D'Oro, S. Basagni, and T. Melodia, "Understanding O-RAN: Architecture, Interfaces, Algorithms, Security, and Research Challenges," *IEEE Communications Surveys and Tutorials*, vol. 25, no. 2, pp. 1376–1411, 2023, doi: 10.1109/COMST.2023.3239220.
- [12] R. Badeel, S. K. Subramaniam, Z. M. Hanapi, and A. Muhammed, "A review on LiFi network research: Open issues, applications and future directions," *Applied Sciences*, vol. 11, no. 23, p. 11118, 2021.
- [13] S. Miladić-Tešić, G. Marković, D. Peraković, and I. Cvitić, "A review of optical networking technologies supporting 5G communication infrastructure," *Wireless Networks*, vol. 28, no. 1, pp. 459–467, Jan. 2022, doi: 10.1007/s11276-021-02582-6.
- [14] S. Won and S. W. Choi, "Three Decades of 3GPP Target Cell Search through 3G, 4G, and 5G," *IEEE Access*, vol. 8, pp. 116914–116960, 2020, doi: 10.1109/ACCESS.2020.3003012.
- [15] S. A. Mohammed *et al.*, "Supporting Global Communications of 6G Networks Using AI, Digital Twin, Hybrid and Integrated Networks, and Cloud: Features, Challenges, and Recommendations," *Telecom*, vol. 6, no. 2, p. 35, May 2025, doi: 10.3390/telecom6020035.
- [16] S. S. MURAD, R. BADEEL, N. S. A. ALSANDI, R. F. A. R. A. AHMED, A. MUHAMMED, and M. DERAHMAN, "OPTIMIZED MIN-MIN TASK SCHEDULING ALGORITHM FOR SCIENTIFIC WORKFLOWS IN A CLOUD ENVIRONMENT," *J. Theor. Appl. Inf. Technol.*, vol. 100, no. 2, 2022.
- [17] B.-A. M. Oraibi and N. A. B. S. Nizam, "Findings From A Qualitative Study of the Experiences and Challenges Private Virtual University Students had with E-Learning During the Covid-19," *International Journal of Academic Research in Progressive Education and Development*, vol. 13, no. 3, Aug. 2024, doi: 10.6007/IJARPED/v13 i3/21600.
- [18] S. Shahidi Hamedani, S. Aslam, B. A. Mundher Oraibi, Y. B. Wah, and S. Shahidi Hamedani, "Transitioning towards Tomorrow's Workforce: Education 5.0 in the Landscape of Society 5.0: A Systematic Literature Review," *Educ. Sci. (Basel).*, vol. 14, no. 10, p. 1041, Sep. 2024, doi: 10.3390/educsci14101041.
- [19] H. M. Barakat *et al.*, "Wireless and Emerging Technologies to Meet E-Government Demands: Applications, Benefits, and Challenges," *Information*, vol. 17, no. 3, p. 225, Feb. 2026, doi: 10.3390/info17030225.
- [20] N. Chen and M. Okada, "Toward 6G Internet of Things and the Convergence with RoF System," *IEEE Internet Things J.*, vol. 8, no. 11, pp. 8719–8733, Jun. 2021, doi: 10.1109/JIOT.2020.3047613.
- [21] M. H. Alsharif, A. H. Kelechi, M. A. Albreem, S. A. Chaudhry, M. Sultan Zia, and S. Kim, "Sixth generation (6G)wireless networks: Vision, research activities, challenges and potential solutions," Apr. 01, 2020, *MDPI AG*. doi: 10.3390/SYM12040676.
- [22] C. X. Wang, J. Wang, S. Hu, Z. H. Jiang, J. Tao, and F. Yan, "Key Technologies in 6G Terahertz Wireless Communication Systems: A Survey," *IEEE Vehicular Technology Magazine*, vol. 16, no. 4, pp. 27– 37, Dec. 2021, doi: 10.1109/MVT.2021.3116420.

- [23] A. Fayad and T. Cinkler, "Energy-Efficient Joint User and Power Allocation in 5G Millimeter Wave Networks: A Genetic Algorithm-Based Approach," *IEEE Access*, vol. 12, pp. 20019–20030, 2024, doi: 10.1109/ACCESS.2024.3361660.
- [24] M. Adhikari and A. Hazra, "6G-Enabled Ultra-Reliable Low-Latency Communication in Edge Networks," *IEEE Communications Standards Magazine*, vol. 6, no. 1, pp. 67–74, Mar. 2022, doi: 10.1109/MCOMSTD.0001.2100098.
- [25] F. Tang, X. Chen, M. Zhao, and N. Kato, "The Roadmap of Communication and Networking in 6G for the Metaverse," *IEEE Wirel. Commun.*, vol. 30, no. 4, pp. 72–81, Aug. 2023, doi: 10.1109/MWC.019.2100721.
- [26] T. Sizer *et al.*, "Integrated Solutions for Deployment of 6G Mobile Networks," *Journal of Lightwave Technology*, vol. 40, no. 2, pp. 346– 357, Jan. 2022, doi: 10.1109/JLT.2021.3110436.
- [27] M. Ozger *et al.*, "6G for Connected Sky: A Vision for Integrating Terrestrial and Non-Terrestrial Networks," in *2023 Joint European Conference on Networks and Communications and 6G Summit, EuCNC/6G Summit 2023*, Institute of Electrical and Electronics Engineers Inc., 2023, pp. 711–716. doi: 10.1109/EuCNC/6GSummit58263.2023.10188330.
- [28] M. Mozaffari, X. Lin, and S. Hayes, "Toward 6G with Connected Sky: UAVs and Beyond," *IEEE Communications Magazine*, vol. 59, no. 12, pp. 74–80, Dec. 2021, doi: 10.1109/MCOM.005.2100142.
- [29] M. Giordani and M. Zorzi, "Non-Terrestrial Networks in the 6G Era: Challenges and Opportunities," *IEEE Netw.*, vol. 35, no. 2, pp. 244– 251, 2021, doi: 10.1109/MNET.011.2000493.
- [30] E. Calvanese Strinati *et al.*, "6G in the sky: On-demand intelligence at the edge of 3D networks," *ETRI Journal*, vol. 42, no. 5, pp. 643–657, Oct. 2020, doi: 10.4218/etrij.2020-0205.
- [31] G. Geraci *et al.*, "What Will the Future of UAV Cellular Communications Be? A Flight from 5G to 6G," *IEEE Communications Surveys and Tutorials*, vol. 24, no. 3, pp. 1304–1335, Sep. 2022, doi: 10.1109/COMST.2022.3171135.
- [32] K. B. Letaief, W. Chen, Y. Shi, J. Zhang, and Y. J. A. Zhang, "The Roadmap to 6G: AI Empowered Wireless Networks," *IEEE Communications Magazine*, vol. 57, no. 8, pp. 84–90, Aug. 2019, doi: 10.1109/MCOM.2019.1900271.
- [33] Y. Shi, J. Zhang, B. O'Donoghue, and K. B. Letaief, "Large-scale convex optimization for dense wireless cooperative networks," *IEEE Transactions on Signal Processing*, vol. 63, no. 18, pp. 4729–4743, Sep. 2015, doi: 10.1109/TSP.2015.2443731.
- [34] K. Yang, Y. Shi, and Z. Ding, "Data Shuffling in Wireless Distributed Computing via Low-Rank Optimization," *IEEE Transactions on Signal Processing*, vol. 67, no. 12, pp. 3087–3099, Jun. 2019, doi: 10.1109/TSP.2019.2912139.
- [35] M. A. Habibi, M. Nasimi, B. Han, and H. D. Schotten, "A Comprehensive Survey of RAN Architectures Toward 5G Mobile Communication System," 2019, *Institute of Electrical and Electronics Engineers Inc.* doi: 10.1109/ACCESS.2019.2919657.
- [36] V. S. Pana, O. P. Babalola, and V. Balyan, "5G radio access networks: A survey," Jul. 01, 2022, *Elsevier B.V.* doi: 10.1016/j.array.2022.100170.
- [37] S. K. Singh, R. Singh, and B. Kumbhani, "The Evolution of Radio Access Network Towards Open-RAN: Challenges And Opportunities," 2020.
- [38] I. A. Alimi, A. L. Teixeira, and P. P. Monteiro, "Toward an Efficient C-RAN Optical Fronthaul for the Future Networks: A Tutorial on Technologies, Requirements, Challenges, and Solutions," Jan. 01, 2018, *Institute of Electrical and Electronics Engineers Inc.* doi: 10.1109/COMST.2017.2773462.
- [39] D. Wypiór, M. Klinkowski, and I. Michalski, "Open RAN—Radio Access Network Evolution, Benefits and Market Trends," Jan. 01, 2022, *MDPI*. doi: 10.3390/app12010408.
- [40] A. Checko *et al.*, "Cloud RAN for Mobile Networks A Technology Overview," *IEEE Communications Surveys and Tutorials*, vol. 17, no. 1, pp. 405–426, Jan. 2015, doi: 10.1109/COMST.2014.2355255.
- [41] M. Kassi and S. Hamouda, "RAN Virtualization: How Hard Is It to Fully Achieve?," *IEEE Access*, vol. 12, pp. 38030–38047, 2024, doi: 10.1109/ACCESS.2024.3375749.
- [42] M. F. Hossain, A. U. Mahin, T. Debnath, F. B. Mosharrof, and K. Z. Islam, "Recent research in cloud radio access network (C-RAN) for

- 5G cellular systems A survey," Aug. 01, 2019, *Academic Press*. doi: 10.1016/j.jnca.2019.04.019.
- [43] Ramesh Krishna Mahimalur, "Machine Learning Approaches for Resource Allocation in Heterogeneous Cloud-Edge Computing," *International Journal of Scientific Research in Computer Science, Engineering and Information Technology*, vol. 11, no. 2, pp. 2739– 2748, Mar. 2025, doi: 10.32628/cseit25112758.
- [44] A. Ndikumana, K. K. Nguyen, and M. Cheriet, "Federated Learning Assisted Deep Q-Learning for Joint Task Offloading and Fronthaul Segment Routing in Open RAN," *IEEE Transactions on Network and Service Management*, vol. 20, no. 3, pp. 3261–3273, Sep. 2023, doi: 10.1109/TNSM.2023.3245544.
- [45] M. Peng, J. Zhang, S. Yan, and Z. Bai, "Integrated Communication, Sensing and Computing Enabled Fog Radio Access Networks: Issues and Challenges," *IEEE Netw.*, 2025, doi: 10.1109/MNET.2025.3574486.
- [46] L. Zhang, M. Zhang, X. Liu, and L. Guo, "6G smart fog radio access network: Architecture, key technologies, and research challenges," Jun. 01, 2025, *KeAi Communications Co.* doi: 10.1016/j.dcan.2024.10.002.
- [47] B. Di, H. Zhang, Z. Han, R. Zhang, and L. Song, "Reconfigurable Holographic Surface: A New Paradigm for Ultra-Massive MIMO," *IEEE Trans. Cogn. Commun. Netw.*, 2025, doi: 10.1109/TCCN.2025.3547043.
- [48] J. Zhang, Y. Huang, J. Wang, X. You, and C. Masouros, "Intelligent Interactive Beam Training for Millimeter Wave Communications," *IEEE Trans. Wirel. Commun.*, vol. 20, no. 3, pp. 2034–2048, Mar. 2021, doi: 10.1109/TWC.2020.3038787.
- [49] K. A. Szczurek, R. M. Prades, E. Matheson, J. Rodriguez-Nogueira, and M. Di Castro, "Multimodal Multi-User Mixed Reality Human-Robot Interface for Remote Operations in Hazardous Environments," *IEEE Access*, vol. 11, pp. 17305–17333, 2023, doi: 10.1109/ACCESS.2023.3245833.
- [50] M. M. Rathore, S. A. Shah, D. Shukla, E. Bentafat, and S. Bakiras, "The Role of AI, Machine Learning, and Big Data in Digital Twinning: A Systematic Literature Review, Challenges, and Opportunities," 2021, *Institute of Electrical and Electronics Engineers Inc.* doi: 10.1109/ACCESS.2021.3060863.
- [51] H. Zhang *et al.*, "Holographic Integrated Sensing and Communication," *IEEE Journal on Selected Areas in Communications*, vol. 40, no. 7, pp. 2114–2130, Jul. 2022, doi: 10.1109/JSAC.2022.3155548.
- [52] M. A. Habibi, B. Han, M. Nasimi, N. P. Kuruvatti, A. Fellan, and H. D. Schotten, "Towards a Fully Virtualized, Cloudified, and Slicing-Aware RAN for 6G Mobile Networks," 2021, pp. 327–358. doi: 10.1007/978-3-030-72777-2\_15.
- [53] X. Wang *et al.*, "Virtualized Cloud Radio Access Network for 5G Transport," *IEEE Communications Magazine*, vol. 55, no. 9, pp. 202– 209, 2017, doi: 10.1109/MCOM.2017.1600866.
- [54] A. O. Alliance, "O-RAN: Towards an Open and Smart RAN," 2018, *Germany*. Accessed: Aug. 15, 2025. [Online]. Available: https://www.o-ran.org/resources
- [55] "Everything You Need to Know About Open RAN," 2020, *Nashua, U.K.*
- [56] S. K. A. Kumar and E. J. Oughton, "Infrastructure Sharing Strategies for Wireless Broadband," *IEEE Communications Magazine*, vol. 61, no. 7, pp. 46–52, 2023, doi: 10.1109/MCOM.005.2200698.
- [57] A. Fayad, T. Cinkler, J. Rak, and M. Jha, "Design of Cost-Efficient Optical Fronthaul for 5G/6G Networks: An Optimization Perspective," *Sensors*, vol. 22, no. 23, p. 9394, 2022, doi: 10.3390/s22239394.
- [58] A. Fayad, T. Cinkler, and J. Rak, "5G/6G optical fronthaul modeling: cost and energy consumption assessment," *Journal of Optical Communications and Networking*, vol. 15, no. 9, p. D33, 2023, doi: 10.1364/JOCN.486547.
- [59] J. Lorincz, Z. Klarin, and D. Begusic, "Advances in Improving Energy Efficiency of Fiber–Wireless Access Networks: A Comprehensive Overview," *Sensors*, vol. 23, no. 4, p. 2239, 2023, doi: 10.3390/s23042239.
- [60] A. Lometti and V. Sestito, "Fronthaul in 5G Transport Networks: IEEE1914.1 Architecture and Requirements," in *2020 22nd*

- *International Conference on Transparent Optical Networks (ICTON)*, IEEE, 2020, pp. 1–4. doi: 10.1109/ICTON51198.2020.9203468.
- [61] X. Wang, Y. Ji, J. Zhang, L. Bai, and M. Zhang, "Joint Optimization of Latency and Deployment Cost Over TDM-PON Based MEC-Enabled Cloud Radio Access Networks," *IEEE Access*, vol. 8, pp. 681–696, 2020, doi: 10.1109/ACCESS.2019.2959119.
- [62] G. Kalfas *et al.*, "Next Generation Fiber-Wireless Fronthaul for 5G mmWave Networks," *IEEE Communications Magazine*, vol. 57, no. 3, pp. 138–144, 2019, doi: 10.1109/MCOM.2019.1800266.
- [63] N. Chouhan, U. R. Bhatt, and R. Upadhyay, "An optimization framework for FiWi access network: Comprehensive solution for green and survivable deployment," *Optical Fiber Technology*, vol. 53, p. 102002, Dec. 2019, doi: 10.1016/j.yofte.2019.102002.
- [64] W. Shang and V. Friderikos, "Energy Efficient Optimization of In-Band Integrated Access and Backhaul Heterogeneous Networks," *IEEE Trans. Veh. Technol.*, vol. 74, no. 4, pp. 6504–6517, 2025, doi: 10.1109/TVT.2024.3514928.
- [65] K. Boonlom *et al.*, "Multiwavelength Optical Sensing of Water-Level Stratification in Closed Plastic Pipelines Using Signal Attenuation and CIR Analysis," *IEEE Sens. J.*, vol. 25, no. 19, pp. 35991–36001, 2025, doi: 10.1109/JSEN.2025.3598923.
- [66] B. B.S and S. Azeem, "A survey on increasing the capacity of 5G Fronthaul systems using RoF," *Optical Fiber Technology*, vol. 74, p. 103078, 2022, doi: 10.1016/j.yofte.2022.103078.
- [67] Y. Fan *et al.*, "Point-to-Multipoint Coherent Architecture with Joint Resource Allocation for B5G/6G Fronthaul," *IEEE Wirel. Commun.*, vol. 29, no. 2, pp. 100–106, 2022, doi: 10.1109/MWC.004.2100528.
- [68] F. Saliou *et al.*, "Optical access network interfaces for 5G and beyond [Invited]," *Journal of Optical Communications and Networking*, vol. 13, no. 8, p. D32, 2021, doi: 10.1364/JOCN.425039.
- [69] P. Georgiadis, M. Anastasopoulos, A.-I. Manolopoulos, V.-M. Alevizaki, N. Nikaein, and A. Tzanakaki, "Demonstration of Energy Efficient Optimization in Beyond 5G Systems supported by Optical Transport Networks," in *Optical Fiber Communication Conference (OFC) 2023*, Washington, D.C.: Optica Publishing Group, 2023, p. W4F.4. doi: 10.1364/OFC.2023.W4F.4.
- [70] S. Chen, Y. C. Liang, S. Sun, S. Kang, W. Cheng, and M. Peng, "Vision, Requirements, and Technology Trend of 6G: How to Tackle the Challenges of System Coverage, Capacity, User Data-Rate and Movement Speed," *IEEE Wirel. Commun.*, vol. 27, no. 2, pp. 218– 228, Apr. 2020, doi: 10.1109/MWC.001.1900333.
- [71] S. S. Murad *et al.*, "6G Wireless Networks in the Generative AI Age: Overview, Techniques, and Future Trends," 2025. [Online]. Available: www.ijacsa.thesai.org
- [72] Garima, V. Jha, and R. K. Singh, "A Novel Dynamic Bandwidth Allocation Scheme for XGPON based Mobile Fronthaul for Small Cell CRAN," *Optical Switching and Networking*, vol. 45, p. 100674, 2022, doi: 10.1016/j.osn.2022.100674.
- [73] E. Wong and L. Ruan, "Towards 6G: fast and self-adaptive dynamic bandwidth allocation for next-generation mobile fronthaul [Invited]," *Journal of Optical Communications and Networking*, vol. 15, no. 8, p. C203, 2023, doi: 10.1364/JOCN.483983.
- [74] E. Wong, S. Mondal, and L. Ruan, "Machine learning enhanced nextgeneration optical access networks—challenges and emerging solutions [Invited Tutorial]," *Journal of Optical Communications and Networking*, vol. 15, no. 2, p. A49, 2023, doi: 10.1364/JOCN.470902.
- [75] Elaine Wong and Lihua Ruan, "Towards 6G: Machine Learning Driven Resource Allocation in Next Generation Optical Access Networks (Invited)," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Basel Switzerland, 2022, pp. 1–3.
- [76] F. Tao, H. Zhang, A. Liu, and A. Y. C. Nee, "Digital Twin in Industry: State-of-the-Art," *IEEE Trans. Industr. Inform.*, vol. 15, no. 4, pp. 2405–2415, Apr. 2019, doi: 10.1109/TII.2018.2873186.
- [77] L. Diez, A. M. Alba, W. Kellerer, and R. Aguero, "Flexible Functional Split and Fronthaul Delay: A Queuing-Based Model," *IEEE Access*, vol. 9, pp. 151049–151066, 2021, doi: 10.1109/ACCESS.2021.3124374.
- [78] M. K. Shehzad, L. Rose, M. M. Butt, I. Z. Kovacs, M. Assaad, and M. Guizani, "Artificial Intelligence for 6G Networks: Technology Advancement and Standardization," *IEEE Vehicular Technology Magazine*, vol. 17, no. 3, pp. 16–25, 2022, doi: 10.1109/MVT.2022.3164758.

- [79] H. Nashaat, N. H. Mohammed, S. M. Abdel-Mageid, and R. Y. Rizk, "Machine Learning-Based Cellular Traffic Prediction Using Data Reduction Techniques," *IEEE Access*, vol. 12, pp. 58927–58939, 2024, doi: 10.1109/ACCESS.2024.3392624.
- [80] A. Mailybayeva, S. Jain, J. Sidhu, N. Vashisht, N. Thangarasu, and S. Goyal, "A Novel Machine Learning Architecture for Traffic Grooming and Resource Optimization in <scp>5G</scp> Optical Fronthaul," *Internet Technology Letters*, vol. 8, no. 4, Jul. 2025, doi: 10.1002/itl2.70052.
- [81] F. Kavehmadavani, V.-D. Nguyen, T. X. Vu, and S. Chatzinotas, "Intelligent Traffic Steering in Beyond 5G Open RAN Based on LSTM Traffic Prediction," *IEEE Trans. Wirel. Commun.*, vol. 22, no. 11, pp. 7727–7742, Nov. 2023, doi: 10.1109/TWC.2023.3254903.
- [82] J. S. Vardakas *et al.*, "Machine Learning-Based Cell-Free Support in the O-RAN Architecture: An Innovative Converged Optical-Wireless Solution Toward 6G Networks," *IEEE Wirel. Commun.*, vol. 29, no. 5, pp. 20–26, 2022, doi: 10.1109/MWC.002.2200026.
- [83] N. Psaromanolakis *et al.*, "Software Defined Networking in a Converged 5G Fiber-Wireless Network," in *2020 European Conference on Networks and Communications (EuCNC)*, Dubrovnik, Croatia: IEEE, Jun. 2020, pp. 225–230. doi: 10.1109/EuCNC48522.2020.9200957.
- [84] E. Datsika *et al.*, "SDN-Enabled Resource Management for Converged Fi-Wi 5G Fronthaul," *IEEE Journal on Selected Areas in Communications*, vol. 39, no. 9, pp. 2772–2788, 2021, doi: 10.1109/JSAC.2021.3064651.
- [85] D. Camps-Mur *et al.*, "5G-XHaul: A Novel Wireless-Optical SDN Transport Network to Support Joint 5G Backhaul and Fronthaul Services," *IEEE Communications Magazine*, vol. 57, no. 7, pp. 99– 105, 2019, doi: 10.1109/MCOM.2019.1800836.
- [86] B. J. Puttnam, G. Rademacher, and R. S. Luís, "Space-division multiplexing for optical fiber communications," *Optica*, vol. 8, no. 9, p. 1186, 2021, doi: 10.1364/OPTICA.427631.
- [87] S. Wang, H. Yang, Y. Qin, D. Peng, and S. Fu, "Power-Over-Fiber in Support of 5G NR Fronthaul: Space Division Multiplexing Versus Wavelength Division Multiplexing," *Journal of Lightwave Technology*, vol. 40, no. 13, pp. 4169–4177, 2022, doi: 10.1109/JLT.2022.3159540.
- [88] R. Martínez, C. Hernández-Chulde, R. Casellas, R. Vilalta, R. Muñoz, and J. M. Fàbrega, "Applications and Lessons Learned from AI/ML-Driven SDN Control and Management in Optical Transport Networks," in *2025 IEEE International Conference on Machine Learning for Communication and Networking (ICMLCN)*, IEEE, May 2025, pp. 1–6. doi: 10.1109/ICMLCN64995.2025.11140388.
- [89] J. Brenes *et al.*, "Network slicing architecture for SDM and analogradio-over-fiber-based 5G fronthaul networks," *Journal of Optical Communications and Networking*, vol. 12, no. 4, p. B33, Apr. 2020, doi: 10.1364/JOCN.381912.
- [90] Z. Allaw, O. Zein, and A.-M. Ahmad, "Cross-Layer Security for 5G/6G Network Slices: An SDN, NFV, and AI-Based Hybrid Framework," *Sensors*, vol. 25, no. 11, p. 3335, May 2025, doi: 10.3390/s25113335.
- [91] M. Wong, A. Prasad, and A. C. K. Soong, "The Security Aspect of 5G Fronthaul," *IEEE Wirel. Commun.*, vol. 29, no. 2, pp. 116–122, 2022, doi: 10.1109/MWC.002.2100445.
- [92] M. Furdek and C. Natalino, "Machine learning for network security management, attacks, and intrusions detection," in *Machine Learning for Future Fiber-Optic Communication Systems*, Elsevier, 2022, pp. 317–336. doi: 10.1016/B978-0-32-385227-2.00017-6.
- [93] M. Furdek, C. Natalino, A. Di Giglio, and M. Schiano, "Optical network security management: requirements, architecture, and efficient machine learning models for detection of evolving threats [Invited]," *Journal of Optical Communications and Networking*, vol. 13, no. 2, p. A144, 2021, doi: 10.1364/JOCN.402884.
- [94] M. Furdek and C. Natalino, "Machine Learning for Optical Network Security Management," in *2020 Optical Fiber Communications Conference and Exhibition (OFC)*, San Diego, CA, USA, 2020, pp. 1– 3.
- [95] M. Furdek, C. Natalino, F. Lipp, D. Hock, A. Di Giglio, and M. Schiano, "Machine Learning for Optical Network Security Monitoring: A Practical Perspective," *Journal of Lightwave Technology*, pp. 1–1, 2020, doi: 10.1109/JLT.2020.2987032.

- [96] C. Natalino, M. Schiano, A. Di Giglio, and M. Furdek, "Root Cause Analysis for Autonomous Optical Network Security Management," *IEEE Transactions on Network and Service Management*, vol. 19, no. 3, pp. 2702–2713, 2022, doi: 10.1109/TNSM.2022.3198139.
- [97] C. Natalino, C. Manso, R. Vilalta, P. Monti, R. Munoz, and M. Furdek, "Scalable Physical Layer Security Components for Microservice-Based Optical SDN Controllers," in *2021 European Conference on Optical Communication (ECOC)*, Bordeaux, France: IEEE, Sep. 2021, pp. 1–4. doi: 10.1109/ECOC52684.2021.9605943.
- [98] M. A. Khalighi and M. Uysal, "Survey on Free Space Optical Communication: A Communication Theory Perspective," *IEEE Communications Surveys Tutorials*, vol. 16, no. 4, pp. 2231–2258, 2014, doi: 10.1109/COMST.2014.2329501.
- [99] H. Haas, L. Yin, Y. Wang, and C. Chen, "What is LiFi?," *Journal of Lightwave Technology*, vol. 34, no. 6, pp. 1533–1544, Mar. 2016, doi: 10.1109/JLT.2015.2510021.
- [100]J. M. Kahn and J. R. Barry, "Wireless infrared communications," *Proceedings of the IEEE*, vol. 85, no. 2, pp. 265–298, 1997, doi: 10.1109/5.554222.
- [101]J. B. Carruthers and J. M. Kahn, "Modeling of nondirected wireless infrared channels," *IEEE Transactions on Communications*, vol. 45, no. 10, pp. 1260–1268, 1997, doi: 10.1109/26.634690.
- [102]T. Komine and M. Nakagawa, "Fundamental analysis for visible-light communication system using LED lights," *IEEE transactions on Consumer Electronics*, vol. 50, no. 1, pp. 100–107, 2004.
- [103]M. Dehghani Soltani, X. Wu, M. Safari, and H. Haas, "Bidirectional User Throughput Maximization Based on Feedback Reduction in LiFi Networks," *IEEE Transactions on Communications*, vol. 66, no. 7, pp. 3172–3186, 2018, doi: 10.1109/TCOMM.2018.2809435.
- [104]S. Navidpour, M. Uysal, and M. Kavehrad, "BER Performance of Free-Space Optical Transmission with Spatial Diversity," *IEEE Trans. Wirel. Commun.*, vol. 6, no. 8, pp. 2813–2819, Aug. 2007, doi: 10.1109/TWC.2007.06109.
- [105]A. K. Majumdar, "Free-space laser communication performance in the atmospheric channel," *Journal of Optical and Fiber Communications Reports*, vol. 2, no. 4, pp. 345–396, Oct. 2005, doi: 10.1007/s10297- 005-0054-0.
- [106]X. Chang, X. Li, J. He, Y. Ma, G. Li, and L. Lu, "Optical Wireless Fronthaul-Enhanced High-Throughput FC-AE-1553 Space Networks," *Photonics*, vol. 10, no. 12, p. 1331, 2023, doi: 10.3390/photonics10121331.
- [107]A. Aleem and R. Thumma, "Hybrid Energy-Efficient Clustering With Reinforcement Learning for IoT-WSNs Using Knapsack and K - Means," *IEEE Sens. J.*, vol. 25, no. 15, pp. 30047–30059, Aug. 2025, doi: 10.1109/JSEN.2025.3582381.
- [108]Dr. A. K. Lodhi, Dr. B. Unhelkar, Dr. A. Hussain, Dr. P. Chakrabarty, and Dr. M. Khan, "Trust-Aware Clustering for Enhanced Routing Security and Performance in Sensor-Enabled Mobile Ad Hoc Networks," *International Journal of Multidisciplinary Engineering in Current Research*, vol. 11, no. 03, pp. 1–10, Jan. 2026, doi: 10.63665/IJMEC.1103.01.
- [109]"Optimizing Energy Efficiency in IoT-Enabled Wireless Sensor Networks Using an Integrated EEKA-K-means Approach," *International Journal of Intelligent Engineering and Systems*, vol. 18, no. 2, pp. 441–453, Mar. 2025, doi: 10.22266/ijies2025.0331.33.
- [110]A. Dixit *et al.*, "Fiber and Wavelength Open Access in WDM and TWDM Passive Optical Networks," *IEEE Netw.*, 2014.
- [111]M. Kumari, R. Sharma, and A. Sheetal, "Comparative Analysis of High Speed 20/20 Gbps OTDM-PON, WDM-PON and TWDM-PON for Long-Reach NG-PON2," *Journal of Optical Communications*, vol. 43, no. 3, pp. 397–410, 2022, doi: 10.1515/joc-2019-0005.
- [112]C. Vázquez, G. Otero, R. Altuna, J. D. López-Cardona, and D. Larrabeiti, "Power Over Fiber Pooling as Part of 6G Optical Fronthaul," *Journal of Lightwave Technology*, vol. 42, no. 14, pp. 4774–4781, 2024, doi: 10.1109/JLT.2024.3375972.
- [113]E. Etezadi *et al.*, "Deep reinforcement learning for proactive spectrum defragmentation in elastic optical networks," *Journal of Optical Communications and Networking*, vol. 15, no. 10, p. E86, 2023, doi: 10.1364/JOCN.489577.
- [114]H. Maryam, T. Panayiotou, and G. Ellinas, "Multi-Step Traffic Prediction for Multi-Period Planning in Optical Networks," in *2024 24th International Conference on Transparent Optical Networks*

- *(ICTON)*, IEEE, 2024, pp. 1–5. doi: 10.1109/ICTON62926.2024.10648008.
- [115]L. Ruiz, R. J. Duran Barroso, I. De Miguel, N. Merayo, J. C. Aguado, and E. J. Abril, "Routing, Modulation and Spectrum Assignment Algorithm Using Multi-Path Routing and Best-Fit," *IEEE Access*, vol. 9, pp. 111633–111650, 2021, doi: 10.1109/ACCESS.2021.3101998.
- [116]M. Lian *et al.*, "Resource Allocation in Flexible-Bandwidth Fine-Grained Optical Transport Networks for Geo-Distributed Machine Learning," *IEEE Internet Things J.*, vol. 12, no. 13, pp. 25601–25619, 2025, doi: 10.1109/JIOT.2025.3558933.
- [117]A. Israr and A. Israr, "Optimal free space optical fronthaul framework for 5G Cran," *International Journal of Information Technology*, vol. 15, no. 6, pp. 3327–3334, 2023, doi: 10.1007/s41870-023-01371-y.
- [118]A. Fayad, I. Pelle, T. Cinkler, and B. Sonkoly, "Harnessing Free Space Optics for Efficient 6G Fronthaul Networks: Challenges and Opportunities," Mar. 01, 2025, *John Wiley and Sons Inc*. doi: 10.1002/eng2.70051.
- [119]R. Ullah *et al.*, "High-Capacity Free Space Optics-Based Passive Optical Network for 5G Front-Haul Deployment," *Photonics*, vol. 10, no. 10, Oct. 2023, doi: 10.3390/photonics10101073.
- [120]M. Zhang, C. You, and Z. Zhu, "On the Parallelization of Spectrum Defragmentation Reconfigurations in Elastic Optical Networks," *IEEE/ACM Transactions on Networking*, vol. 24, no. 5, pp. 2819– 2833, Oct. 2016, doi: 10.1109/TNET.2015.2487366.
- [121]M. Zhang, C. You, H. Jiang, and Z. Zhu, "Dynamic and Adaptive Bandwidth Defragmentation in Spectrum-Sliced Elastic Optical Networks With Time-Varying Traffic," *Journal of Lightwave Technology*, vol. 32, no. 5, pp. 1014–1023, 2014.
- [122]P. M. Moura and N. L. S. Da Fonseca, "Multipath Routing in Elastic Optical Networks with Space-Division Multiplexing," *IEEE Communications Magazine*, vol. 59, no. 10, pp. 64–69, Oct. 2021, doi: 10.1109/MCOM.111.2100331.
- [123]C. Natalino *et al.*, "Optical Networking Gym: an open-source toolkit for resource assignment problems in optical networks," *Journal of Optical Communications and Networking*, vol. 16, no. 12, pp. G40– G51, 2024, doi: 10.1364/JOCN.532850.
- [124]L. Guo, Y. Liu, F. Wang, W. Hou, and B. Gong, "Cluster-Based Protection for Survivable Fiber-Wireless Access Networks," *Journal of Optical Communications and Networking*, vol. 5, no. 11, p. 1178, 2013, doi: 10.1364/JOCN.5.001178.
- [125]G. Zhang, M. De Leenheer, and B. Mukherjee, "Optical Traffic Grooming in OFDM-Based Elastic Optical Networks [Invited]," *Journal of Optical Communications and Networking*, vol. 4, no. 11, p. B17, 2012, doi: 10.1364/JOCN.4.000B17.
- [126]J. Zhang, J. Xie, L. Guo, B. Li, S. Chen, and R. Zhong, "Adaptive high-efficiency RWA algorithm for optical networks based on reinforcement learning," Institute of Electrical and Electronics Engineers (IEEE), Oct. 2025, pp. 122–127. doi: 10.1109/ngdn66208.2025.11182145.
- [127]I. Sartzetakis, K. Christodoulopoulos, and E. Varvarigos, "Cross-layer adaptive elastic optical networks," *Journal of Optical Communications and Networking*, vol. 10, no. 2, pp. A154–A164, Feb. 2018, doi: 10.1364/JOCN.10.00A154.
- [128]T. Sato, K. Ashizawa, H. Takeshita, S. Okamoto, N. Yamanaka, and E. Oki, "Logical Optical Line Terminal Placement Optimization in the Elastic Lambda Aggregation Network With Optical Distribution Network Constraints," *Journal of Optical Communications and Networking*, vol. 7, no. 9, p. 928, 2015, doi: 10.1364/JOCN.7.000928.
- [129]Y. Pointurier, "Design of Low-Margin Optical Networks," *Journal of Optical Communications and Networking*, vol. 9, no. 1, p. A9, 2017, doi: 10.1364/JOCN.9.0000A9.
- [130]Q. Sun *et al.*, "Environment-aware geometric shaping for digital FSO fronthaul networks," *Journal of Optical Communications and Networking*, vol. 17, no. 11, p. E37, 2025, doi: 10.1364/JOCN.562110.
- [131]A. O. Mufutau, F. P. Guiomar, M. A. Fernandes, A. Lorences-Riesgo, A. Oliveira, and P. P. Monteiro, "Demonstration of a hybrid optical fiber–wireless 5G fronthaul coexisting with end-to-end 4G networks," *Journal of Optical Communications and Networking*, vol. 12, no. 3, p. 72, 2020, doi: 10.1364/JOCN.382654.
- [132]S. S. Jaffer, A. Hussain, M. A. Qureshi, J. Mirza, and K. K. Qureshi, "A low cost PON-FSO based fronthaul solution for 5G CRAN

- architecture," *Optical Fiber Technology*, vol. 63, p. 102500, 2021, doi: 10.1016/j.yofte.2021.102500.
- [133]D. Neves *et al.*, "Beyond 5G Fronthaul Based on FSO Using Spread Spectrum Codes and Graphene Modulators," *Sensors*, vol. 23, no. 8, Apr. 2023, doi: 10.3390/s23083791.
- [134]C. Madapatha, P. Lechowicz, C. Natalino, P. Monti, and T. Svensson, "Joint Fiber and Free Space Optical Infrastructure Planning for Hybrid Integrated Access and Backhaul Networks," Jul. 2025, [Online]. Available: http://arxiv.org/abs/2507.20367
- [135]M. A. Hasabelnaby and M. I. Dessoky, "Network Availability of Hybrid FSO/mmW 5G Fronthaul Network in C-RAN Architecture," 2019.
- [136]H. Shoukat, N. Aslam, M. Waseem, and M. U. Hadi, "Technological Trends in Open Fronthauls for Beyond 5G and 6G Networks," *Communications & Networks Connect*, vol. 1, no. 1, p. 1, 2024, doi: 10.69709/COConnect.2024.093713.
- [137]R. Puerta *et al.*, "NR Conformance Testing of Analog Radio-over-LWIR FSO Fronthaul link for 6G Distributed MIMO Networks," in *Optical Fiber Communication Conference (OFC) 2023*, Washington, D.C.: Optica Publishing Group, 2023, p. Th2A.32. doi: 10.1364/OFC.2023.Th2A.32.
- [138]D. Konstantinou *et al.*, "5G RAN architecture based on analog radioover-fiber fronthaul over UDWDM-PON and phased array fed reflector antennas," *Opt. Commun.*, vol. 454, p. 124464, 2020, doi: 10.1016/j.optcom.2019.124464.
- [139]S. Chaudhary, S. Khichar, M. Saadi, A. Parniarifard, and A. Sharma, "Hybrid MDM-MIMO radio-over-free space optical system for highcapacity 5G and beyond networks under strong and weak scintillation," *Front. Phys.*, vol. 13, 2025, doi: 10.3389/fphy.2025.1556402.
- [140]S. S. Murad, S. Yussof, W. Hashim, and R. Badeel, "Card-Flipping Decision-Making Technique for Handover Skipping and Access Point Assignment: A Novel Approach for Hybrid LiFi Networks," *IEEE Access*, pp. 1–1, 2024, doi: 10.1109/ACCESS.2024.3473938.
- [141]S. S. Murad, R. Badeel, and R. A. Ahmed, "Is LiFi Technology Ready for Manufacturing and Adoption? An End-user questionnaire-based study," *Applied Data Science and Analysis*, vol. 2024, pp. 95–107, Jul. 2024, doi: 10.58496/adsa/2024/009.
- [142]M. Dehghani Soltani, A. A. Purwita, I. Tavakkolnia, H. Haas, and M. Safari, "Impact of Device Orientation on Error Performance of LiFi Systems," *IEEE Access*, vol. 7, no. c, pp. 41690–41701, 2019, doi: 10.1109/ACCESS.2019.2907463.
- [143]M. Dehghani Soltani, X. Wu, M. Safari, and H. Haas, "Access point selection in Li-Fi cellular networks with arbitrary receiver orientation," *IEEE International Symposium on Personal, Indoor and Mobile Radio Communications, PIMRC*, 2016, doi: 10.1109/PIMRC.2016.7794890.
- [144]R. Ahmad, M. D. Soltani, M. Safari, and A. Srivastava, "Load Balancing of Hybrid LiFi WiFi Networks Using Reinforcement learning," in *2020 IEEE 31st Annual International Symposium on Personal, Indoor and Mobile Radio Communications*, pp. 1–6.
- [145]H. Abumarshoud, M. D. Soltani, M. Safari, and H. Haas, "Realistic Secrecy Performance Analysis for LiFi Systems," *IEEE Access*, vol. 9, pp. 120675–120688, 2021, doi: 10.1109/ACCESS.2021.3108727.
- [146]R. Ahmad, M. D. Soltani, M. Safari, and A. Srivastava, "Reinforcement Learning-Based Near-Optimal Load Balancing for Heterogeneous LiFi WiFi Network," *IEEE Syst. J.*, vol. 16, no. 2, pp. 3084–3095, Jun. 2022, doi: 10.1109/JSYST.2021.3088302.
- [147]A. A. Purwita, M. D. Soltani, M. Safari, and H. Haas, "Terminal Orientation in OFDM-Based LiFi Systems," *IEEE Trans. Wirel. Commun.*, vol. 18, no. 8, pp. 4003–4016, 2019, doi: 10.1109/TWC.2019.2920132.
- [148]X. Wu, M. D. Soltani, L. Zhou, M. Safari, and H. Haas, "Hybrid LiFi and WiFi Networks: A Survey," *IEEE Communications Surveys and Tutorials*, vol. 23, no. 2, pp. 1398–1420, 2021, doi: 10.1109/COMST.2021.3058296.
- [149]M. D. Soltani, A. A. Purwita, Z. Zeng, H. Haas, and M. Safari, "Modeling the random orientation of mobile devices: Measurement, analysis and LiFi Use Case," *IEEE Transactions on Communications*, vol. 67, no. 3, pp. 2157–2172, Mar. 2019, doi: 10.1109/TCOMM.2018.2882213.

- [150]S. S. Murad, S. Yussof, B. A. M. Oraibi, R. Badeel, B. Badeel, and A. H. Alamoodi, "A Vehicle Social Distancing Management System Based on LiFi During COVID Pandemic: Real-time Monitoring for Smart Buildings," *IEEE Access*, 2024, doi: 10.1109/ACCESS.2024.3461359.
- [151]H. Abumarshoud, L. Mohjazi, O. A. Dobre, M. Di Renzo, M. A. Imran, and H. Haas, "LiFi through Reconfigurable Intelligent Surfaces: A New Frontier for 6G?," *IEEE Vehicular Technology Magazine*, vol. 17, no. 1, pp. 37–46, 2022, doi: 10.1109/MVT.2021.3121647.
- [152]C. Mas-Machuca, M. Kaufmann, J.-P. Linnartz, M. Riegel, D. Schulz, and V. Jungnickel, "Techno-economic study of very dense optical wireless access using visible or infrared light," *Journal of Optical Communications and Networking*, vol. 15, no. 5, p. B33, 2023, doi: 10.1364/JOCN.482707.
- [153]A. Ebmeyer, K. L. Bober, M. Hinrichs, and V. Jungnickel, "Fronthaul Synchronization Requirements for Distributed MIMO in LiFi Systems," in *2024 IEEE Wireless Communications and Networking Conference (WCNC)*, IEEE, 2024, pp. 1–6. doi: 10.1109/WCNC57260.2024.10571141.
- [154]H. Djellab, O. Allaoua, F. Mammri, S. Riad, F. Boumehrez, and A. Sahour, "Performance analysis of a hybrid DWDM-FSO system for 6G," *Journal of Optical Communications*, 2025, doi: 10.1515/joc-2024-0259.
- [155]S. V. Pendem, C. Natalino, A. Napoli, and P. Monti, "Hybrid FSO-THz Technologies for 6G Access Networks: A Cost-Availability Trade-off Analysis," in *2025 25th Anniversary International Conference on Transparent Optical Networks (ICTON)*, IEEE, 2025, pp. 1–5. doi: 10.1109/ICTON67126.2025.11125338.
- [156]S. M. Kouhini *et al.*, "Performance of Bidirectional LiFi over Plastic Optical Fiber (POF)," in *International Symposium on Communication Systems, Networks and Digital Signal Processing (CSNDSP)*, IEEE, 2020.
- [157]T. E. B. Cunha, C. R. B. Corrêa, J. P. Linnartz, E. Tangdiongga, and F. M. Huijskens, "Real-time hardware G.hn LiFi infrastructure with D-MIMO and WDM over POF Fronthaul," in *IECON 2022 – 48th Annual Conference of the IEEE Industrial Electronics Society*, Oct. 2022, pp. 1–6. doi: 10.1109/IECON49645.2022.9968387.
- [158]J. P. M. G. Linnartz *et al.*, "ELIoT: enhancing LiFi for next-generation Internet of things," *EURASIP J. Wirel. Commun. Netw.*, vol. 2022, no. 1, p. 89, 2022, doi: 10.1186/s13638-022-02168-6.
- [159]S. M. Kouhini *et al.*, "All-Optical Distributed MIMO for LiFi: Spatial Diversity Versus Spatial Multiplexing," *IEEE Access*, vol. 10, pp. 102646–102658, 2022, doi: 10.1109/ACCESS.2022.3207475.
- [160]M. Kumari, M. Banawan, V. Arya, and S. K. Mishra, "Investigation of OFDM-Based HS-PON Using Front-End LiFiSystem for 5G Networks," *Photonics*, vol. 10, no. 12, p. 1384, 2023, doi: 10.3390/photonics10121384.
- [161]O. Aouedi, V. A. Le, K. Piamrat, and Y. Ji, "Deep Learning on Network Traffic Prediction: Recent Advances, Analysis, and Future Directions," *ACM Comput. Surv.*, vol. 57, no. 6, pp. 1–37, Jun. 2025, doi: 10.1145/3703447.
- [162]M. Kulin, T. Kazaz, E. De Poorter, and I. Moerman, "A Survey on Machine Learning-Based Performance Improvement of Wireless Networks: PHY, MAC and Network Layer," *Electronics (Basel).*, vol. 10, no. 3, p. 318, Jan. 2021, doi: 10.3390/electronics10030318.
- [163]Z. Md. Fadlullah *et al.*, "State-of-the-Art Deep Learning: Evolving Machine Intelligence Toward Tomorrow's Intelligent Network Traffic Control Systems," *IEEE Communications Surveys & Tutorials*, vol. 19, no. 4, pp. 2432–2455, 2017, doi: 10.1109/COMST.2017.2707140.
- [164]N. Maharjan and B. W. Kim, "Machine Learning-Based Beam Pointing Error Reduction for Satellite–Ground FSO Links," *Electronics (Basel).*, vol. 13, no. 17, p. 3466, Aug. 2024, doi: 10.3390/electronics13173466.
- [165]T. Panayiotou, M. Michalopoulou, and G. Ellinas, "Survey on Machine Learning for Traffic-Driven Service Provisioning in Optical Networks," *IEEE Communications Surveys & Tutorials*, vol. 25, no. 2, pp. 1412–1443, 2023, doi: 10.1109/COMST.2023.3247842.
- [166]M. Noebels, R. Preece, and M. Panteli, "A machine learning approach for real‐time selection of preventive actions improving power network resilience," *IET Generation, Transmission & Distribution*, vol. 16, no. 1, pp. 181–192, Jan. 2022, doi: 10.1049/gtd2.12287.

![](_page_32_Picture_1.jpeg)

- [167]J. M. Philip, T. Mittal, N. Aamer, R. B. K, H. Patil, and V. Pai, "Artificial Intelligence-Driven Predictive Maintenance for Optical Fiber Networks," in *2025 Global Conference in Emerging Technology (GINOTECH)*, IEEE, May 2025, pp. 1–6. doi: 10.1109/GINOTECH63460.2025.11076936.
- [168]X. Liu *et al.*, "AI-Based Modeling and Monitoring Techniques for Future Intelligent Elastic Optical Networks," *Applied Sciences*, vol. 10, no. 1, p. 363, Jan. 2020, doi: 10.3390/app10010363.
- [169]E. Edozie, A. N. Shuaibu, B. O. Sadiq, and U. K. John, "Artificial intelligence advances in anomaly detection for telecom networks," *Artif. Intell. Rev.*, vol. 58, no. 4, p. 100, Jan. 2025, doi: 10.1007/s10462-025-11108-x.
- [170]K. Abdelli, J. Y. Cho, F. Azendorf, H. Griesser, C. Tropschug, and S. Pachnicke, "Machine-learning-based anomaly detection in optical fiber monitoring," *Journal of Optical Communications and Networking*, vol. 14, no. 5, p. 365, May 2022, doi: 10.1364/JOCN.451289.
- [171]V. Hassija *et al.*, "Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence," *Cognit. Comput.*, vol. 16, no. 1, pp. 45–74, Jan. 2024, doi: 10.1007/s12559-023-10179-8.
- [172]A. F. Pakpahan and I.-S. Hwang, "Peer-to-Peer Federated Learning on Software-Defined Optical Access Network," *IEEE Access*, vol. 12, pp. 84435–84451, 2024, doi: 10.1109/ACCESS.2024.3411639.
- [173]O. Ayoub *et al.*, "Towards explainable artificial intelligence in optical networks: the use case of lightpath QoT estimation," *Journal of Optical Communications and Networking*, vol. 15, no. 1, p. A26, Jan. 2023, doi: 10.1364/JOCN.470812.

![](_page_32_Picture_9.jpeg)

IEEE ICC 2023.

**MOHAMMAD D. SOLTANI** received the M.Sc. degree from the Department of Electrical Engineering, Amirkabir University of Technology, Iran, in 2012, and the Ph.D. degree in electrical engineering from The University of Edinburgh, U.K., in 2019. His current research interests include mobility and handover management in wireless cellular networks, optical wireless communications, visible light communications, and LiFi. He received the Best Paper Awards from IEEE GLOBECOM 2022 and

![](_page_32_Picture_12.jpeg)

RF communications, and LiFi and Systems Simulation networking and Modeling.

**ROZIN BADEEL** Received her bachelor's degree in computer science and information technology in 2012 from Nawroz University in Dahuk, Iraq. Then, she received her M.Sc. degree in Distributed Computing and Networks in 2018 from University Putra Malaysia, Malaysia. Currently, she is pursuing a PhD in Computer Science at the University Putra Malaysia, Malaysia. Her main research interests are focused on cloud computing, Optical Wireless Communication (OWC), hybrid optical wireless and

![](_page_32_Picture_15.jpeg)

Networking Department, UNITEN University. He is currently an Associate Professor with UNITEN University. He is the author of more than 72 publications. His research interests include computer networks, network security, distributed system, image processing, robotic, and evolutionary computing. In recent years, he has been involved with many professional bodies, such as the Association for Computing Machinery (ACM) since 2003, the Malaysian Invention and Design Society (MINDS) since 2004, the Boards of Engineers Malaysia (BEM) since 2005, the Malaysian National Computer Confederation (MNCC) since 2008, and the Internet Society (ISOC) since 2011.

![](_page_32_Picture_17.jpeg)

**SALLAR S. MURAD** received his bachelor's degree in software engineering in 2014 from Al-Rafidain University College, Baghdad, Iraq. Then, he received his M.Sc. degree in Computer Science in 2018 from University Putra Malaysia (UPM), Malaysia. Currently, he is pursuing a PhD in Information and Communication Technology at the University Tenaga Nasional, Malaysia. His main

research interests are the Internet of Things (IoT), cloud computing, visible light communication (VLC), hybrid optical wireless and RF communications, LiFi, and wireless technologies. He has published a few articles in reputable journals, and he is a reviewer in many journals. He also publishes books in Amazon Kindle.

![](_page_32_Picture_20.jpeg)

since 2012 until now.

**ZAINAB ABDULLAH JASIM** received her Bachelor of Computer Science from College of Science, University of Baghdad, in 1989. Master of Computer Science, University of Babylon in 2012. PhD in Information Technology, University of Babylon in 2024. Her research interest is wireless communications, algorithms and blockchain. She supervised many undergraduate students' projects

![](_page_32_Picture_23.jpeg)

**BHA-ALDAN MUNDHER ORAIBI** is a senior lecturer at the faculty of business, UNITAR International University, Malaysia. He holds a BBA from Tikrit University, an MBA and Master of Management (MMgt) from Graduate School of Management (GSM), International Islamic University Malaysia (IIUM), and his doctorate degree in business economics from the School of Business and Economics (formerly known as Faculty of Economics and Management), Universiti Putra Malaysia (UPM). His research

focuses on Careers, Human Resource Management, in particular international and strategic HRM, technology and management, and Organizational Studies.
Received 4 January 2022; accepted 24 January 2022. Date of publication 28 January 2022; date of current version 11 February 2022.

Dieital Object Identifier 10.1109/OJCOMS.2022.3146618

# Deep Learning for B5G Open Radio Access Network: Evolution, Survey, Case Studies, and Challenges

BOUZIANE BRIK<sup>10</sup>1, KARIM BOUTIBA<sup>2</sup>, AND ADLEN KSENTINI<sup>10</sup>2 (Senior Member, IEEE)

<sup>1</sup>DRIVE EA1859, University of Bourgogne Franche-Comté, 25000 Besançon, France

<sup>2</sup>Communication Systems Department, EURECOM, 06410 Sophia-Antipolis, France

 $CORRESPONDING\ AUTHOR:\ B.\ BRIK\ (e-mail:\ bouziane.brik@gmail.com)$ 

This work was supported in part by the European Union's H2020 MonB5G Project under Grant 871780, and in part by 5G! Drones Project under Grant 857031.

ABSTRACT Open Radio Access Network (O-RAN) alliance was recently launched to devise a new RAN architecture featuring open, software-driven, virtual, and intelligent radio access architecture. O-RAN architecture is based on (1) disaggregated RAN functions that run as Virtual Network Function (VNF) and Physical Network Function (PNF); (2) the notion of RAN controller that runs centrally RAN applications such as mobility management, users' scheduling, radio resources allocation, etc. The RAN controller is in charge of enforcing the application decisions by using open interfaces with the RAN functions. One important feature introduced by O-RAN is the heavy usage of Machine Learning (ML) techniques, particularly Deep Learning (DL), to foster innovation and ease the deployment of intelligent RAN applications that are able to fulfill the Quality of Service (QoS) requirements of the envisioned 5G and beyond network services. In this work, we first give an overview of the evolution of RAN architectures toward 5G and beyond, namely C-RAN, vRAN, and O-RAN. We also compare them based on various perspectives, such as edge support, virtualization, control and management, energy consumption, and AI support. Then, we review existing DL-based solutions addressing the RAN part. We also show how they can be integrated/mapped to the O-RAN architecture since these works were not initially adapted to the O-RAN architecture. In addition, we present two case studies for DL techniques deployment in O-RAN. Furthermore, we describe how the main steps of deployed DL models in O-RAN can be automated, to ensure stable performance of these models, introducing ML system operations (MLOps) concept in O-RAN. Finally, we identify key technical challenges, open issues, and future research directions related to the Artificial Intelligence (AI)-enabled O-RAN architecture.

**INDEX TERMS** B5G networks, RAN, open RAN architecture, RAN intelligent controller, deep learning, MLOps.

## I. INTRODUCTION

THE FORTHCOMING Beyond fifth-generation (B5G) networks, or so-called 6G, are revolutionary technology expected to eliminate the bounds of bandwidth, access, latency, and performance limitations on connectivity worldwide [1], [2]. B5G is expected to transform the mobile communication networks from the Internet of Things (IoT) to the "connected intelligence", by leveraging Artificial Intelligence (AI) techniques and connecting billions of people and machines. This makes B5G the key enabler of a wide range of new services improving quality of life around the

world through unparalleled use cases [1], such as connected autonomous systems, eXtended reality (encompassing both augmented and virtual reality), flying vehicles, haptics, telemedicine, etc. To successfully deploy these use-cases, B5G systems must simultaneously provide ultra-low latency, very high and reliable data rates, high energy efficiency, and broad frequency bands (in THz) for heterogeneous devices [2].

The co-existence of such a variety of services needs a versatile network that considers all features. However, these targets cannot be supported by the existing Radio

Access Network (RAN), and hence optimizing the RAN part is greatly needed [\[3\]](#page-19-2). One way to support the variety of service requirements is to design separate network instances, where each one (instance) meets the needs of a given type of service [\[4\]](#page-19-3). In such context, both the industries and academia are leveraging new technologies, including Software Defined Network (SDN) and Network Function Virtualization (NFV), to make the mobile radio network more virtual, software-oriented, intelligent, and energy efficient [\[4\]](#page-19-3).

Another potential solution to fulfill the requirements of the above-mentioned services is to divide the RAN part into several parts based on its main functionality, in order to make the radio network versatile and smarter [\[5\]](#page-19-4). In this context, Open RAN (O-RAN) alliance has recently launched a design of a new RAN architecture for the next-generation mobile networks (5G and beyond) [\[6\]](#page-19-5), [\[7\]](#page-19-6). O-RAN is a major paradigm shift in the RAN architecture aiming to lead the industry towards software-driven, virtual, open, and AI-enabled RAN. Specifically, the basic idea of O-RAN is to disaggregate the main functions of traditional RAN, implement them as software components (i.e., VNF), and connect them using standardized and open interfaces. We also note that the Linux Foundation and the O-RAN Alliance have announced the O-RAN Software Community (OSC) in April 2019 [\[8\]](#page-19-7), giving birth to the first open-source O-RAN Software, named Amber Release, in December 2019 [\[9\]](#page-19-8).

O-RAN has designed a hierarchical RAN Intelligent Controller (RIC), including both near real-time and non real-time RICs that support programmable-based functions. RICs integrate embedded Deep Learning (DL) capabilities to RAN in order to optimize RAN performance and reduce operational complexity. It helps to adapt the radio resource, mobility, and spectrum management operations (admission control, radio resources allocation and scheduling, power allocation, radio link management, etc.) according to applications' requirements, which is very valuable in B5G networks when addressing different vertical industries.

# *A. REVIEW OF RELATED WORKS*

Several survey papers addressing 4G/5G RAN part have been published so far. In [\[3\]](#page-19-2), the authors provided a literature review and an in-depth study of Cloud-RAN (C-RAN), Heterogeneous Cloud RAN (H-CRAN), Virtualzied Cloud RAN (V-CRAN), and Fog RAN (F-RAN). Another survey focused on C-RAN and detailed deep learning applications for the C-RAN architecture, was proposed in [\[10\]](#page-20-0). Similarly, the authors in [\[11\]](#page-20-1) addressed the C-RAN architecture. More specifically, they gave a detailed survey on the resource allocation in such RAN architecture.

In O-RAN context, to the best of our knowledge, we find only three short survey/review studies. In [\[12\]](#page-20-2), the authors gave a short study on what O-RAN can do and what it cannot do (limitations). The authors started first by briefly present the O-RAN architecture, followed by a community survey on the importance of O-RAN. Indeed, this survey was conducted among 95 wireless researchers, and the majority stated that O-RAN will be the foundation of future cellular networks. Then, the authors described the benefits of O-RAN in addition to its current shortcomings and research opportunities. On the other hand, the general architecture, concepts, and requirement of O-RAN first introduced in [\[13\]](#page-20-3). Then, the authors designed an intelligent scheme of radio resource allocation to deal with traffic congestion and show its efficiency by leveraging a real-world dataset. The work concludes with still opened challenges and future research directions. Similarly, the authors provided an overview on O-RAN architecture and its main modules in [\[14\]](#page-20-4). The authors also gave realistic RAN scenarios leveraging AI/ML-based models, on top of the O-RAN architecture, highlighting their disrupting potential. Finally, the main benefits and limitations of O-RAN are detailed along with the conclusions.

Besides, few works have recently proposed technical contributions related to the O-RAN architecture. In [\[15\]](#page-20-5), the O-RAN architecture is leveraged to design a machinelearning-based scheme to optimize the Automatic Neighbour Relation (ANR) function of Self Organizing Network (SON), and hence improving gNodeB (gNB) handovers. The authors in [\[16\]](#page-20-6) reviewed multi-agent systems and team learning schemes, before discussing how these schemes can be deployed on top of O-RAN architecture. In [\[17\]](#page-20-7), [\[18\]](#page-20-8), the authors discussed the evolution of RAN towards Open-RAN, in terms of architectures, functionality, and implementation. While, the potential integration of O-RAN with the 5G Multi-access Edge Computing (MEC), SON, and Network Slicing (NS) concepts are discussed in [\[19\]](#page-20-9). The dynamic function splitting issue of O-RAN is addressed in [\[20\]](#page-20-10). A reinforcement learning-based scheme is designed to dynamically split functions in O-RAN, while optimizing the energy consumption of the RAN software and hardware. In [\[21\]](#page-20-11), a novel framework is designed addressing the challenge of how to slice the RAN in 5G, namely New Radio flexibility (NRflex). NRflex enables to dynamically allocate the bandwidth part (BWP) as well as radio resources the network slices, and their corresponding users, in order to meet the slices' requirement. In addition, the NRflex framework has been mapped to the O-RAN architecture, to dynamically determine the BWPs' sizes for each RAN slice. A new 5G non-public networks (NPN) architectural framework is proposed in [\[22\]](#page-20-12), to enable cost-efficient deployments of 5G private networks. This framework relies on key emergent technologies, such as AI/ML-driven models, MEC, and disaggregated RAN functions, to optimize network management. It also enables efficient RAN sharing in terms of required resource and service orchestration, which are aligned with the O-RAN architecture. In [\[23\]](#page-20-13), [\[24\]](#page-20-14), the authors discussed the implementation of ML-based closedloop solutions on top of the O-RAN architecture. They also provided a first demonstration of O-RAN through an experimental testbed. Thus, they deployed O-RAN using Colosseum network emulator. Then, they used the deployed O-RAN to manage multiple network slices. Finally, the

authors introduced a ML workflow-based on Working Group (WG) 2 ML specifications of the O-RAN alliance, in [\[25\]](#page-20-15). They then implemented this workflow using the open-source software of O-RAN. They used both Acumos Framework and Open Network Automation Platform (ONAP), to generate ML models to be executed in the O-RAN RIC module, and to monitor and manage the designed workflow, respectively.

Even there are several survey papers that addressed the 4G/5G RAN architectures, however, most of them studied the previous RAN architectures including, C-RAN, H-CRAN, V-CRAN, etc. Thus, these works did not address, or include, the O-RAN architecture in their studies. In addition, a wide range of DL-based studies have also been proposed to deal with the main RAN challenges in 4G/5G networks [\[26\]](#page-20-16), [\[27\]](#page-20-17), [\[28\]](#page-20-18), [\[29\]](#page-20-19). However, these studies did not also consider the emerged O-RAN architecture, and hence need to be mapped/integrated into this architecture. On the other hand, existing O-RAN-related survey works are limited to short studies that described the O-RAN architecture and its main modules, in addition to its main benefits as well as shortcomings.

## *B. CONTRIBUTIONS*

In contrast to the existing survey papers, this paper addresses the O-RAN architecture and aims mainly to map/integrate existing DL-based studies to the new O-RAN architecture, via its hierarchical RICs modules. We also propose two case studies of how to deploy ML/DL-based models on top of the O-RAN architecture, and show how the whole ML/DL process can be automated. Based on this, we name the main contributions of this paper as follows.

- We first provide an overview of the RAN architecture evolution, toward the B5G networks. We also compare them based on various perspectives, such as edge support, virtualization, control and management, energy consumption, and AI support.
- We also provide a new review study regarding existing DL-based works for the next generation RAN. Moreover, we show how these works can be realized on top of the O-RAN architecture.
- We describe two case studies for DL techniques deployment in the O-RAN architecture, in addition to how the main steps of DL models deployment may be automated, in order to ensure stable and acceptable performance of deployed models.
- The key technical challenges, open issues, and future research directions related to the AI-enabled O-RAN architecture are finally discussed.

# *C. PAPER STRUCTURE*

Fig. [1](#page-2-0) illustrates the general structure of this paper. Section [II](#page-2-1) gives a general overview of the evolution of the RAN architectures, including the O-RAN architecture and its functional modules. The existing DL-based works addressing the 5G RAN and their integration to the O-RAN architecture are discussed in Section [III.](#page-8-0) Two case studies for

![](_page_2_Figure_11.jpeg)

<span id="page-2-0"></span>**FIGURE 1. The structure of the Paper.**

DL deployment in O-RAN are detailed in Section [IV.](#page-14-0) The automation of the main steps of DL process is presented in Section [V.](#page-16-0) Section [VI](#page-18-0) describes open problems and future research directions. Section [VII](#page-19-9) concludes the paper. Note that used acronyms in this paper are described in Table [1,](#page-3-0) in alphabetical order, for the ease of reference.

#### <span id="page-2-1"></span>**II. EVOLUTION OF RAN ARCHITECTURES**

In this section, we review the evolution of RAN architectures, starting from centralized RAN to Distributed RAN, continuing with Cloud RAN (C-RAN), through virtual RAN (vRAN), and most recently O-RAN architecture. We note that we provide more details on the O-RAN architecture, as it represents the main scope of this work.

## *A. FROM CENTRALIZED 2G RAN TO DISTRIBUTED 3/4G RAN ARCHITECTURE*

In 2G networks, baseband and radio processing functions are implemented at the base stations (BSs) level [\[30\]](#page-20-20). A BS is composed of two functional equipment: Radio Equipment Controller (REC) and Digital Unit (DU). REC is in charge of baseband signal processing, monitoring and managing BSs, whereas DU is responsible for radio functions including, modulation, demodulation, amplification, radio frequency filtering, frequency conversion, and analog-to-digital as well as digital-to-analog conversion.

However, in 3G/4G networks, the signal and radio processing units of 2G BSs are separated from each other (cf. Fig. [2\)](#page-4-0). The radio unit is deployed close to the 3G/4G BS and is called Remote Radio Unit (RRU) or Remote Radio Head (RRH). The baseband signal processing unit is called Baseband Unit (BBU). The BBU provides required resources to its RRHs with respect to the running applications requirements [\[31\]](#page-20-21).

This RAN architecture is called Distributed RAN (D-RAN). Each BBU is interconnected to its corresponding RRH through a transport network, where both optical microwave and fiber can be deployed to link between BBU and RRH (called fronthaul).

**TABLE 1. List of acronyms.**

<span id="page-3-0"></span>

| Acronym         | Definition                                           | Acronym | Definition                                 |
|-----------------|------------------------------------------------------|---------|--------------------------------------------|
| 3GPP            | 3rd Generation Partnership Project                   | O-CU    | Open RAN Central Unit                      |
| AI              | Artificial Intelligence                              | O-CU-CP | Open RAN Central Unit – Control Plane      |
| A3C             | Asynchronous Advantage Actor-Critic                  | O-CU-UP | Open RAN Central Unit – User Plane         |
| AMC             | Automatic Modulation Classification                  | O-DU    | Open RAN Distributed Unit                  |
| ANR             | Automatic Neighbour Relation                         | O-RU    | Open RAN Radio Unit                        |
| BBU             | Baseband Unit                                        | OSC     | Open RAN Software Community                |
| BS              | Base Station                                         | OPEX    | OPerational EXpenditures                   |
| BWP             | Bandwidth Part                                       | OFDM    | Orthogonal Frequency-Division Multiplexing |
| B5G             | Beyond Fifth-Generation                              | PDCP    | Packet Data Control Protocol               |
| BER             | Bit Error Rate                                       | PDCCH   | Physical Downlink Control Channel          |
| CAPEX           | CAPital EXpenditures                                 | PDSCH   | Physical Downlink Shared Channel           |
| CSI             | Channel State Information                            | PNF     | Physical Network Function                  |
| C-RAN           | Cloud Radio Access Network                           | PUCCH   | Physical Uplink Control Channel            |
| CD              | Continuous Delivery                                  | PUSCH   | Physical Uplink Shared Channel             |
| CT              | Continuous Training                                  | PW      | Prediction Windows                         |
| CNN             | Convolutional Neural Network                         | QoS     | Quality of Service                         |
| DL              | Deep Learning                                        | RAN     | Radio Access Network                       |
| DNN             | Deep Neural Network                                  | RIC     | RAN Intelligent Controller                 |
| DQN             | Deep Q-Network                                       | REC     | Radio Equipment Controller                 |
| DRL             | Deep Reinforcement Learning                          | RF      | Radio Frequency                            |
| D-RAN           | Distributed RAN                                      | RLC     | Radio Link Control                         |
| FL              | Federated Learning                                   | RNIS    | Radio Network Information Service          |
| 5G              | Fifth Generation                                     | RRC     | Radio Resource Control                     |
| F-RAN           | Fog RAN                                              | RRM     | Radio Resource Management                  |
| GM-LAMP         | Gaussian Mixture-Learned Approximate Message Passing | RT      | Real Time                                  |
| gNB             | gNodeB                                               | RNN     | Recurrent Neural Network                   |
| H-CRAN          | Heterogeneous Cloud RAN                              | RL      | Reinforcement Learning                     |
| High-PHY        | High physical                                        | RRH     | Remote Radio Head                          |
| iRSS            | intelligent Resource-Scheduling Scheme               | RRU     | Remote Radio Unit                          |
| IoT             | Internet of Things                                   | RB      | Resource Blocks                            |
| LSTM            | Long Short Term Memory                               | RM      | Resource Management                        |
| Low-PHY         | Low Physical                                         | SON     | Self Organizing Network                    |
| ML              | Machine Learning                                     | SDAP    | Service Data Adaptation Protocol           |
| MLOps           | ML system operations                                 | SLA     | Service Level Agreement                    |
| MDP             | Markov Decision Process                              | SMO     | Service Management and Orchestration level |
| MAC             | Medium Access Control                                | SNR     | Signal-to-noise ratio                      |
| MM              | Mobility Management                                  | SCN     | Small Cell Networks                        |
| MEC             | Multi-access Edge Computing                          | SDN     | Software Defined Network                   |
| MIMO            | Multiple Input Multiple Output                       | SM      | Spectrum Management                        |
| NE<br>N. DE DIG | Nash Equilibrium                                     | UE      | User Equipment                             |
| Near RT RIC     | Near Real-Time RAN Intelligent Controller            | V2V     | Vehicle-to-Vehicle                         |
| NFV             | Network Function Virtualization                      | vBBU    | Virtual BBU                                |
| NS              | Network Slicing                                      | VNF     | Virtual Network Function                   |
| NG RAN          | New Generation RAN                                   | vRAN    | Virtual RAN                                |
| NPN             | Non-Public Networks                                  | VR      | Virtual Reality                            |
| Non RT RIC      | Non Real-Time RAN Intelligent Controller             | V-CRAN  | Virtualzied Cloud RAN                      |
| ONAP            | Open Network Automation Platform                     | WG      | Working Group                              |
| O-RAN           | Open Radio Access Network                            |         |                                            |

## *B. CENTRALIZED AND CLOUDIFIED RAN ARCHITECTURE*

With the increase of data traffic and various QoS (Quality of Service) requirement, cellular network actors had to go through cloudification and centralization of BBU part, which contains a pool of network resources. This new architecture is known as C-RAN [\[32\]](#page-20-22), [\[33\]](#page-20-23). As depicted in Fig. [3,](#page-4-1) the basic idea of C-RAN is to link RRHs to cloudified, centralized, and shared BBU pool. Each RRH is linked to its BBU pool via a fronthaul link, and up to ten RRHs can be connected to the same BBU pool.

This RAN architecture is designed on the top of two paradigms: virtualization and centralization of baseband processing part [\[33\]](#page-20-23). Thus, it enables to decrease the energy consumption, increase network throughput, improve network scalability and spectral efficiency, facilitate network management and load balancing.

#### *C. VIRTUALIZED RAN ARCHITECTURE*

5G mobile networks come with various requirements such as the massive number of mobile users, ultra low latency communications, and reliable and high data throughput. To fulfill these requirements, network actors are leveraging emergent technologies of NFV and SDN in order to virtualize all resources and functions in the RAN architecture and also decouple control and data planes. This new trend of access network virtualization represents a new type of RAN, known as Virtualized RAN or vRAN.

![](_page_4_Figure_1.jpeg)

<span id="page-4-0"></span>**FIGURE 2. D-RAN Architecture.**

![](_page_4_Figure_3.jpeg)

<span id="page-4-1"></span>**FIGURE 3. C-RAN Architecture.**

Fig. [4](#page-4-2) shows vRAN architecture which is composed of Digital Unit Cloud (DU Cloud) and RRU parts, interconnected through Fiber Ethernet links [\[34\]](#page-20-24). In the DU Cloud, the BBUs are virtualized (vBBUs) and deployed on multiple NFV platforms, which provide baseband processing related functions. All vBBU are interconnected with each other through a switch (layer 2) that is used to exchange signaling and data among the vBBUs. vRAN is based on standard server hardware that efficiently scales down or up memory, processing, and I/O resources with respect to the demand. Hence, it helps to achieve the full potential of lower energy consumption, dynamic capacity scaling, efficient use of network resources, and improved service reliability and quality.

Besides, RRUs are left at the network edge (the cell sites). In addition, Fiber Ethernet and IP links provide lower latency

![](_page_4_Picture_7.jpeg)

**FIGURE 4. vRAN Architecture.**

<span id="page-4-2"></span>and higher bandwidth fronthaul network for exchanging signaling and data between RRUs and DUs. This also gives more cost-effective options to service providers for fronthaul transport.

#### *D. OPEN RAN ALLIANCE ARCHITECTURE*

The O-RAN Alliance addresses the radio access network domain and promises to make it more open, flexible, and smarter [\[6\]](#page-19-5), [\[7\]](#page-19-6), [\[9\]](#page-19-8). The basic idea is disaggregate hardware from software, and create open interfaces between them. Hence, this helps networks support open interfaces and common development standards, to deliver multi-vendor, interoperable networks and helps to avoid any vendor lockin. Fig. [5](#page-5-0) shows the reference architecture of the O-RAN alliance. This new architecture leverages SDN and NFV technologies to include new interfaces and redefine the RAN functional blocks to allow the deployment of new applications and services on top of RAN. It is worth noting that Fig. [5](#page-5-0) reflects a very specific functional split scenario, where O-RAN's CU (Central Unit), DU (Distributed Unit), and RU (Radio Unit) are in separated locations. In Sections [II-](#page-2-1)D6 and [II-](#page-2-1)D7, we describe the different functional split options and RAN deployment scenarios, respectively. In addition, in what follows, we describe the main elements of the O-RAN architecture. We note that detailing the functional blocks of the O-RAN architecture is not in the scope of this work.

# 1) THE NON REAL-TIME RAN INTELLIGENT CONTROLLER

The non Real-Time (RT) RIC is a logical function implemented at the Service Management and Orchestration level (SMO). It is composed of two main sub-functions: Non-RT RIC framework and Non-RT RIC applications (rApps). The framework is an internal functionality of SMO that provides the needed services to rApps through R1 interface, while the non-RT RIC applications (rApps) leverage the

![](_page_5_Figure_1.jpeg)

<span id="page-5-0"></span>**FIGURE 5. Reference Architecture of the O-RAN Alliance for separated RU, CU, and DU deployment scenario.**

SMO services, such as data monitoring over the O1 interface (stored in a local database) and provisioning services, in order to support intelligent optimization of RAN elements and resources in a non real-time scale (i.e., greater than one second). Thus, Non-RT RIC aims to provide an intelligent RAN policy to near Real-time intelligent controller, through the A1 interface, based mainly on AI/DL training/inference and data analytics.

# 2) THE NEAR REAL-TIME RAN INTELLIGENT CONTROLLER

The Near Real-time (RT) RIC controls and optimizes the O-RAN nodes (O-CU and O-DU) and their resources over the E2 interface with a near real-time control loop (i.e., from 10ms to 100ms). The Near-RT RIC implements a set of primitives to improve the O-RAN nodes' performances, such as monitoring, stop/suspend, control, and/or override. The Near-RT RIC hosts applications, namely xApps, that leverage these primitives and use the E2 interface to monitor near real-time RAN information from the O-RAN nodes. xApps then provide value-added services, with respect to the policies data received from the Non-RT RIC, through the A1 interface. xApps include Spectrum Management (SM), Resources Management (RM), Mobility Management (MM), etc.

## 3) CONTROL AND USER PLANES OF O-RAN CENTRAL UNIT (O-CU-CP AND O-CU-UP)

O-CU is a logical node hosting Radio Resource Control (RRC), Service Data Adaptation Protocol (SDAP), and Packet Data Control Protocol (PDCP) protocols. The control plane of O-CU hosts the RRC and the control plane part of the PDCP protocol, while the user plane part of the PDCP protocol and the SDAP protocol is hosted on the user plane of O-CU (O-CU-UP). Both planes interface over E1 and are in charge of ensuring mainly UE, cell, and gNB procedure management, such as UE mobility and connectivity, base station energy, cell activation, etc.

# 4) O-RAN DISTRIBUTED UNIT (O-DU)

O-DU is a logical node comprising three main layers: Radio Link Control (RLC), Medium Access Control (MAC), and high physical (High-PHY) layers. O-DU interfaces with O-CU through F1 interface to provide many functionalities related to the three layers including, UE and Bearer context management, RLC mode transmitter and receiver, MAC radio resource allocation, MAC scheduler, handling of physical uplink (downlink) shared (control) channels, etc.

# 5) O-RAN RADIO UNIT (O-RU)

O-RU is a logical node hosting the low physical (Low-PHY) layer functions and Radio Frequency (RF) processing. We note that in O-RAN architecture, physical layer functionality is split into High-PHY in O-DU and Low-PHY in O-RU. Besides, an open front haul interface between O-DU and O-RU is defined in O-RAN architecture and is adopted in the split architecture.

# 6) FUNCTIONAL SPLIT OPTIONS IN O-RAN

Conventionally and as shown in Fig. [6,](#page-6-0) 3GPP has defined nine functional blocks and eight split point options in 4G wireless networks [\[36\]](#page-20-25). However, with the high increase in

![](_page_6_Figure_1.jpeg)

<span id="page-6-0"></span>**FIGURE 6. Splitting options of CU, DU, and RU functions in O-RAN. 5G(A) split of high layer; 5G(B) split of low layer; 5G(C) cascaded split [\[35\]](#page-20-26).**

data throughput in 5G, it is critical to relax the bandwidth and latency requirements, while centralizing only a few functions. Hence, the new functional-splitting must consider and find cost-effective tradeoffs between latency, data rates, and functional centralization. In 2017, 3GPP considered Option 2 (PDCP and high RLC) as the high layer split point (called the F1 Interface) and both Option 6 and Option 7 for the low layer split [\[37\]](#page-20-27).

Fig. [6](#page-6-0) shows the mapping of these functional split options to the CU/DU/RU O-RAN blocks. As mentioned before, to support also the 4G deployments, the terminology for BBU and RRH is replaced by CU/DU and RU, respectively. Thus, five CU/DU/RU functional block splitting have been defined: (i) One high layer split, where the CU functions are separated from DU/RU functions (5G(A)). (ii) Two low layer split which separate the RU functions from CU/DU (5G(B)). (iii) Two cascaded layer split, where each functional block is separated from the others [\[36\]](#page-20-25).

## 7) RAN DEPLOYMENT SCENARIOS

Usually, the transport network is composed of fronthaul, midhaul and backhaul networks. Nevertheless, different deployment scenarios may be used by network operators. 3GPP has identified four RAN deployment scenarios.

- Separated RU, CU and DU locations: This scenario comprises the three transport networks (fronthaul, midhaul and backhaul). The distance between CU and DU is in the range of 0-10 kilometers while that between DU and RU is up to 20 kilometers.
- Co-located DU and CU: There is no midhaul in this scenario, since the DU and CU are co-located.
- DU and RU integration: There is no fronthaul in this scenario, as both DU and RU are located together, for example separated by hundreds of meters in the same

- company or building. Moreover, there is no transport equipment between both blocks (through straight fiber for instance), which enables to reduce mainly the cost.
- CU, DU and RU integration: It is clear that there is only backhaul network in this scenario, which may be used for hot-spot and small cell cases.

It is worth noting that the adequate deployment scenario will be identified based on applications or services requirements (ultra low latency, high data rates, etc.), available transport technology, and requirements of operators' deployment.

#### 8) O-RAN SLICING USE CASES

Recently, a working group of the O-RAN alliance started to describe O-RAN slicing architecture, and its related use cases and requirements [\[38\]](#page-20-28). They mainly focus on how to slice the O-RAN architecture into multiple virtual networks, supporting different service requirements. Fig. [7](#page-7-0) gives a sample scenario of O-RAN slicing deployment, where some O-RAN functions are shared between two slices, such as O-RU, O-DU, and O-CU-CP, while other functions are dedicated to each RAN slice, such as O-CU-UP.

Besides, in [\[39\]](#page-20-29), three main O-RAN slicing use cases are identified along with their requirements and benefits: RAN slice SLA (Service Level Agreement) assurance, multivendor slices, and resource allocation optimization. For instance, RAN slice SLA assurance involves Non-RT RIC, Near-RT RIC, E2 interface. Based on slice requirements, the slice performance may be measured continuously through E2 interface. Then, Non-RT RIC and Near-RT RIC can fine-tune RAN performance to meet RAN slice SLAs. To do so, ML/DL models van be deployed at the Near-RT RIC module that, based on measured slice performance from E2, can adjust the RAN behavior to ensure the slice SLAs.

![](_page_7_Figure_1.jpeg)

**FIGURE 7. O-RAN Slice Deployment Scenario.**

<span id="page-7-1"></span>**TABLE 2. A comparison between C-RAN, vRAN, and O-RAN architectures.**

<span id="page-7-0"></span>

| Characteristics                 | C-RAN                                              | vRAN                        | O-RAN                               |
|---------------------------------|----------------------------------------------------|-----------------------------|-------------------------------------|
| Edge support                    | No (Fully centralized) Yes (Partially centralized) | Yes                         | Yes                                 |
| Decouple of Data/Control planes | No                                                 | Yes                         | Yes                                 |
| Virtualization                  | No                                                 | Yes                         | Yes                                 |
| Multi-vendors Support           | No                                                 | Yes                         | Yes                                 |
| CAPEX and OPEX                  | High                                               | Low                         | Low                                 |
| Energy consumption              | Medium                                             | Low                         | Low                                 |
| Latency                         | High                                               | Low                         | Low                                 |
| AI support                      | Medium                                             | Medium                      | High                                |
| Open interfaces-support         | No                                                 | No                          | Yes                                 |
| RAN controller                  | Non-Real time                                      | Non-Real time               | Near-real time<br>and non-real time |
| Control and management          | Centralized                                        | Centralized and distributed | Centralized and distributed         |

# *E. A COMPARATIVE STUDY*

In this subsection, we provide a comparative study between C-RAN, vRAN, and O-RAN from various perspectives. We discuss major differences among them in terms of characteristics in TABLE [2.](#page-7-1)

We note that we do not consider D-RAN in our comparison since, according to [\[32\]](#page-20-22), the D-RAN is an efficient solution only for 3G/4G networks. However, it is not scalable enough to meet the high bandwidth, low latency, and high data rate requirements of 5G and beyond networks.

• *Edge Support:* In the RAN part, the data is processed either in the central cloud computing or in the Multi-access Edge Computing (MEC), which is near to the mobile users [\[40\]](#page-20-30), [\[41\]](#page-20-31). As for the C-RAN, we distinguish two main configurations: fully centralized C-RAN and partially centralized C-RAN [\[3\]](#page-19-2). Thus, the data is processed either in cloud data centers for the fully centralized configuration, or the MEC for the partially centralized one. But, data are processed

- close to the users (MEC), when it comes to vRAN and O-RAN.
- *Virtualization and Decouple of Data/Control Planes:* Unlike C-RAN, both vRAN and O-RAN leverage new technologies such as SDN and NFV to separate user and control planes and virtualize radio access functions, respectively. In fact, decoupling user and control planes and virtualizing the main functions in the RAN part enhances the flexibility and scalability of network architecture, optimizes centralized control logic functions, facilitates the initiation of network slicing for various industry verticals.
- *Multi-Vendors Support:* C-RAN does not support the multi-vendors paradigm since no virtualization of network functions is considered. O-RAN is based on open standards rather than proprietary and legacy interfaces, which link between BBUs and RRUs parts. This enables units from different vendors to interoperate with each other. Similarly, the radio and baseband

- hardware and software of vRAN may be supplied by different vendors, since vRAN leverages on NFV technology to virtualize its architectural components.
- *Capital and Operational Expenditures (CAPEX and OPEX):* The OPEX and CAPEX costs are considered during the design and deployment steps of the RAN architecture. The network operators are looking to reduce both costs by leveraging already deployed infrastructure [\[42\]](#page-20-32). The virtualization and edge support of RAN architectures play a vital role in reducing both CAPEX and OPEX costs. Hence, OPEX and CAPEX are medium in C-RAN, while both vRAN and O-RAN generate low OPEX and CAPEX costs [\[43\]](#page-20-33).
- *Energy Consumption:* More than 50% of cellular networks energy is consumed by base stations [\[44\]](#page-20-34). Thus, decreasing the consumed energy by base stations significantly impacts the total energy consumption of the RAN part, which will also enable to decrease the energy consumption of all ICT sectors and in particular the cellular networks [\[45\]](#page-20-35). In fact, centralizing network functions causes the energy consumption to decrease and virtualizing the network functions results in reducing further the energy consumption [\[44\]](#page-20-34). Therefore, the energy consumption of C-RAN is medium, while the vRAN and O-RAN are low as compared with that of C-RAN.
- *Latency:* Compared to centralized cloud computing, supporting Edge computing has a significant impact on decreasing the network latency, since it brings computing and storage capacities closer to the mobile users [\[46\]](#page-20-36). Hence, the network latency is high in the centralized C-RAN architecture and low in both vRAN and O-RAN.
- *AI and Open Interfaces Support and RAN Controller:* Compared to C-RAN and VRAN, O-RAN architecture is coming with two new paradigms (1) disaggregated RAN functions that run as VNF; (2) the notion of intelligent RAN controller that runs RAN applications such as mobility management, users scheduling, radio resources allocation, etc. This may be in near real-time for realtime applications, or in non real-time for delay tolerant applications. The RAN controller is in charge of enforcing the application decisions by using open interfaces with the RAN functions. One important feature introduced by O-RAN is the heavy usage of machine learning techniques, particularly deep learning, to foster innovation and ease the deployment of intelligent RAN applications that are able to fulfill the QoS requirements of the envisioned 5G and beyond network services. It is worth noting that recently 3GPP RAN3 standard started to study the integration of AI/ML models to RAN, in its new Release-17 [\[47\]](#page-20-37). The corresponding working group has just begun, and focuses on the main functionalities and their corresponding inputs and outputs (data monitoring, and involved interfaces and nodes). In addition, this study focuses on New Generation RAN (NG-RAN),

- and initially targets three main use cases: load balancing, energy saving, and mobility optimization. The main objective is to design a AI/ML-driven framework on top of the NG-RAN architecture.
- *Control and Management:* Distributed control, management, and deployment of the RAN functions improve mainly network performance such as RAN latency, communication reliability, and interference, whereas centralizing the RAN management may generate a large latency which could impact negatively the network performance and in particular the RAN performance.

## <span id="page-8-0"></span>**III. DEEP LEARNING BASED WORKS FOR RAN**

In this section, we review existing Deep Learning-based works addressing the 4G/5G RAN. Then, we show how these works can be realized on top of the O-RAN architecture. Specifically, we discuss the responsible functional block at each architecture level (Near RT RIC, O-CU, O-DU, and O-RU) as well as the role of the O-RAN interfaces.

To do so, we have chosen to group existing works based on the related Near-RT RIC module to which they belong. This includes the three Near RT RIC modules (cf. Fig. [5\)](#page-5-0).

## *A. RESOURCES MANAGEMENT OPTIMIZATION*

It covers mainly radio resource allocation and scheduling, power resource allocation in both uplink and downlink [\[26\]](#page-20-16), [\[27\]](#page-20-17), [\[28\]](#page-20-18), [\[29\]](#page-20-19). This class of works considers the dynamic changes of the radio access and services requirements in terms of latency, throughput, reliability, etc.

## 1) LITERATURE REVIEW

In [\[26\]](#page-20-16), the authors provided a Deep Learning based framework to intelligently assign radio resources in 5G networks. The framework aims to predict traffic congestion and the occupancy state of the eNBs. An adaptive uplink and downlink ratio can then be applied to avoid traffic congestion. The proposed framework implements a deep tree model and a long short-term memory (LSTM) to predict future traffic based on current and past traffic. The tree model uses convolutional layers to deal with spatial features of generated data by the UEs. Therefore, an appropriate resource management mechanism can be deployed based on the predicted future traffic. Similarly, the authors addressed the traffic congestion issue in [\[28\]](#page-20-18). They used the deep LSTM learning algorithm to make traffic load prediction at the eNB. Based on the predictions, the proposed algorithm executes the appropriate action policy in order to avoid/alleviate the congestion in an intelligent way.

In [\[48\]](#page-20-38), the authors studied the resource management for a network of wireless virtual reality (VR) users. The VR users communicate with small cell networks (SCNs) that act as VR control center. In the considered scenario, the SCNs collect the users' tracking information over the uplink channel. Then, the SCNs will send, via the downlink channel, the generated 3-D images with their audio to the VR users. Hence, the authors provided a resource allocation scheme

that considers both downlink and uplink channels. They first formulated a non-cooperative game where the players are the SCNs that look to find an optimal spectrum allocation improving the VR users' QoE in terms of delay and throughput. A learning algorithm based on echo state networks was then used to predict the VR QoSs value resulting from resource allocation and, hence, reach a Nash equilibrium (NE) state.

The challenge of resource scheduling in 5G RAN slicingready while ensuring the performance isolation, service requirements, and network dynamics (user mobility and channel states) was targeted in [\[27\]](#page-20-17). The authors provided an intelligent resource-scheduling scheme (iRSS) where the basic idea is to exploit both Deep Neural Network (DNN) and reinforcement learning (RL) [\[58\]](#page-21-0). In fact, DNN is used to deal with large time-scale resource allocation, while RL is used to provide an online resource scheduling for tackling small time-scale network dynamics, such as erroneous prediction and unexpected network events. Specifically, the time is divided into a set of prediction windows (PW), while DNN based on LSTM is used in each PW to predict traffic volume for the next PW. In addition, inside each PW, RL based on asynchronous advantage actor-critic (A3C) algorithm is used to perform online resource scheduling.

In [\[29\]](#page-20-19), the authors addressed the distributed scheduling challenge in order to deal with inter-cell interference and with the lack of standardization for schedulers. They proposed a reinforcement deep learning-based (RL) approach to dynamically select the suitable scheduler to each cluster of small cells, based on the channel quality and QoS constraints of the users. In this scheme, resource scheduling is performed in a distributed way by using one of the two schedulers: a proportional fair scheduler or a rate guaranteed max-min scheduler. Based on RL and experienced QoS and channel quality of users, a central agent is in charge of performing a dynamic scheduler selection. Similarly, to minimize the packet delays and drop rates, another RL-based scheduling framework was proposed in [\[49\]](#page-20-39). This framework is able not only to select the suitable scheduling rules per cell but also to learn when to apply each scheduler.

In [\[50\]](#page-20-40), the authors addressed the challenge of power allocation in cellular networks by proposing three deep RLbased schemes: REINFORCE, Deep Q-Learning, and deep deterministic policy gradient (DDPG), which are, respectively, policy-based, value-based, and actor-critic-based. These schemes aimed at maximizing the downlink cell sum-rate. Performed simulations showed that the proposed schemes outperform the state-of-art methods in terms of sum-rate with good generalization power. Similarly, another Q-learning based scheme was proposed in [\[51\]](#page-20-41), in order to achieve a near-optimal power allocation policy in a multicell system. This scheme aimed at maximizing the downlink network throughput under maximal power constraints of a cluster of users, sharing the same frequency bands. In the same context, another deep learning-based approach was proposed in [\[54\]](#page-20-42). It aimed to perform sum-rate-max and max-min power allocation in the uplink of a cell massive MIMO (Multiple Input Multiple Output) system. Using a neural network, the authors generated a learning model that can map between input data and the power allocation scheme's optimal solution.

A radio resource allocation scheme for vehicular networks was proposed in [\[52\]](#page-20-43), in order to ensure ultra-reliable lowlatency V2V communications. To model the latency requirement, the authors considered both transmission latency and queuing latency. They then dealt with the queuing latency using the federated learning (FL) concept to enable each vehicle to predict when its queue length is exceeding a predefined threshold, i.e., exceeding the needed latency [\[59\]](#page-21-1). Simulation results showed that the FL-based scheme can provide very accurate predictions and hence helping at reducing the number of vehicles with exceeding queue lengths.

In [\[53\]](#page-20-44), the authors provided a deep RL-based framework for jointly radio resource management and power allocation. It aimed to achieve a trade-off between communication reliability, latency, and data rate. They first formulated a power minimization problem under reliability and latency constraints before solving it using the deep RL-based framework. The proposed framework can dynamically predict the traffic model of each UE and then jointly allocates resource blocks (RBs) and power to downlink UEs.

Although reinforcement learning may represent a powerful tool for radio optimization, it consumes huge energy over time. Thus, in [\[55\]](#page-20-45), the authors discussed algorithm and architecture innovations to achieve green Deep Reinforcement Learning (DRL) when addressing Radio Resource Management (RRM). From an architectural point of view, a distributed DRL scheme is proposed to enable distributed decision-making by RRM entities. Moreover, a transfer learning scheme is also designed to scale the DRL scheme across geographic areas. Another DRL model is proposed to deal with the radio resource scheduling problem in mobile 5G networks [\[56\]](#page-21-2). The proposed model is numerology-agnostic, which supports different 5G numerologies. A reward analysis study is also provided to deduce which policies the DRL model has learned. Similarly, the authors handled the radio resource scheduling issue in 5G networks, in order to assign efficiently frequency resources to mobile users [\[57\]](#page-21-3). They used an advantage pointer critic to implement a deep reinforcement learning agent. The agent is based on a deep pointer network architecture and deployed at the RAN level. The experimental results show the efficiency of the scheme to allocate frequency resources to users as compared to other schemes.

#### 2) DISCUSSION AND INTEGRATION WITH O-RAN

TABLE [3](#page-10-0) illustrates a comparison study between the works belonging to the Resource management module of Near-RT RIC. This study is established according to the addressed challenge, the used learning algorithm, the link with the O-RAN architecture in terms of the software module and its functional blocks where the proposed schemes can be

<span id="page-10-0"></span>**TABLE 3. Resources management works on the top of O-RAN.**

| Works Challenge        |                                           | Learning             |                 | Link with O-RAN architecture                     |                     |  |  |
|------------------------|-------------------------------------------|----------------------|-----------------|--------------------------------------------------|---------------------|--|--|
| WOLKS                  | Chanenge                                  | algorithm            | O-RAN<br>module | Functional<br>blocks                             | Interfaces          |  |  |
| Hossain et al. [26]    | Radio resources management                | Deep tree<br>+ LSTM  | O-DU            | Resource assignment (NR-MAC)                     |                     |  |  |
| Yan et al. [27]        | Resources scheduling                      | DNN+RL               | O-DU            | UL Scheduler (NR-Scheduler)                      |                     |  |  |
| Zhou et al. [28]       | Radio resources management                | RNN with<br>LSTM     | O-DU            | Resource assignment (NR-MAC)                     | O1 (Monitoring)     |  |  |
| Hall et al. [29]       | Resources scheduling                      | RL                   | O-DU            | UL Scheduler (NR-Scheduler)                      | A1 (Data Analytics) |  |  |
| Comşa et al. [50]      | Resources scheduling                      | RL                   | O-DU            | UL Scheduler (NR-Scheduler)                      | AT (Data Analytics) |  |  |
| Fan et al. [51]        | Power allocation<br>(Downlink)            | RL                   | O-DU            | Resource assignment (NR-MAC)<br>PDSCH (High-PHY) | E2 (Realization)    |  |  |
| Kazi et al. [52]       | Power allocation (Downlink)               | RL                   | O-DU            | Resource assignment (NR-MAC)<br>PDSCH (High-PHY) |                     |  |  |
| Chen et al. [49]       | Resource management                       | DNN                  | O-DU            | Resource assignment (NR-MAC)                     |                     |  |  |
| Samarakoon et al. [53] | Power allocation and resources management | FL                   | O-DU            | Resource assignment (NR-MAC)<br>PDSCH (High-PHY) |                     |  |  |
| Kasgari et al. [54]    | Power allocation and resources management | DRL                  | O-DU            | Resource assignment (NR-MAC)<br>PDSCH (High-PHY) |                     |  |  |
| Carmen et al. [55]     | Power allocation (Uplink)                 | DNN                  | O-DU            | Resource Assignment (NR-MAC)                     |                     |  |  |
| Zhiyong et al. [56]    | Radio resources management                | DRL                  | O-DU            | Resource Assignment (NR-MAC)                     |                     |  |  |
| Al-Tam et al. [57]     | Radio resources scheduling                | DRL                  | O-DU            | UL Scheduler (NR-Scheduler)                      |                     |  |  |
| AL-Tam et al. [58]     | Radio resources scheduling                | Pointer Critic (DRL) | O-DU            | UL Scheduler (NR-Scheduler)                      |                     |  |  |

applied, the communication Interfaces for traffic exchanging as well.

- *Radio Resources Allocation:* It is one of the main functions of RAN, since it enables UEs sending (or receiving) their data while meeting the applications' requirements (latency, throughput, reliability, etc.). Both supervised and reinforcement deep learning have been used to deal with such issue. In particular, LSTM algorithm is used to deal with sequence-to-sequence data in predicting traffic demand over time. Reinforcement learning, on the other hand, enabled to create prediction models of radio resources based on the quality of experiences of mobile users [\[60\]](#page-21-4), [\[61\]](#page-21-5).
- *Resources Scheduling:* The scheduler is in charge of defining when each user may access the wireless medium to send (or receive) its data. This function of RAN is critical as, on one hand, it allows users to meet their requirements such as the latency; on the other hand, it helps to avoid inter and intra-cell interference. To deal with, most of the existing works used reinforcement learning in order to build prediction models based on users' feedback in terms of communication reliability.
- *Power Allocation:* It is another important function of RAN, which aims to implement a near-optimal power allocation policy, in a multi-cell system. Reinforcement learning is mostly applied to maximizing the downlink network throughput, while ensuring an optimal power allocation.

Regarding the link with O-RAN, we observe that all these works belong to the O-DU module since they target the resources (radio and power) management challenge. Thus, these works will mainly concern the MAC layer in terms of resource assignment and scheduling and the High-PHY layer to provide the needed power to the shared physical channel when downloading data (PDSCH for Physical Downlink Shared Channel).

## *B. MOBILITY MANAGEMENT OPTIMIZATION*

It addresses the management of users handover and base station energy, based on users mobility [\[62\]](#page-21-6), [\[63\]](#page-21-7), [\[64\]](#page-21-8).

# 1) LITERATURE REVIEW

In [\[62\]](#page-21-6), the authors targeted conditional handover challenge that is one of the promising mobility enhancements in 5G networks. It consists of making early preparation decisions in order to improve the Handover success rate. However, 5G mm-Wave communications are vulnerable to blockages, and hence sudden changes in signal power can lead to making undesired early preparations of Handover. The authors proposed a deep neural network (DNN) based scheme that considers the environment context and predicts the best next base station based on the received signal power. Therefore, the proposed deep learning based helps in making more intelligent preparation decisions of the handover procedure.

In the same context, in [\[63\]](#page-21-7), the authors first gave an analytical model of Handover cost in 5G, in terms of signaling overhead, latency, call dropping, and radio resource wastage. They then proposed a prediction scheme based on the RNN (Recurrent Neural Network) with LSTM algorithm to further minimize the Handover cost. It was shown that good prediction accuracy of the Handover can significantly minimize the cost function in terms of user dissatisfaction, HO latency, resource wastage, and overhead.

**TABLE 4. Mobility management works on the top of O-RAN.**

<span id="page-11-0"></span>

| Works                | Challenge                  | Learning              | Link with O-RAN architecture |                                  |                     |  |
|----------------------|----------------------------|-----------------------|------------------------------|----------------------------------|---------------------|--|
| WOLKS                | Chancinge                  | algorithm             | O-RAN<br>module              | Functional<br>blocks             | Interfaces          |  |
| Lee et al. [63]      | Handover Management        | DNN                   | O-CU-CP                      | UE and gNB procedure management  | O1 (Monitoring)     |  |
| Ozturk et al. [64]   | Handover Management        | RNN with<br>LSTM      | O-CU-CP                      | UE and gNB procedure management  | A1 (Data Analytics) |  |
| Wang et al. [65]     | Handover Management        | LSTM                  | O-CU-CP                      | UE and gNB procedure management  | E2 (Realization)    |  |
| El Amine et al. [66] | Base station energy        | RL (Q-learning)       | O-CU-CP                      | Cell procedure management        |                     |  |
| Salem et al. [67]    | Base station energy        | RL (Q-learning)       | O-CU-CP                      | Cell procedure management        |                     |  |
| YE et al. [68]       | Base station energy        | DRL<br>(Actor Critic) | O-CU-CP                      | Cell procedure management        |                     |  |
| Kaiqiang et al. [69] | Handover Management        | Federated Learning    | O-CU-CP                      | UE and gNB procedure management  |                     |  |
| Wu et al. [70]       | Handover Management        | DRL                   | O-CU-CP                      | UE and gNB procedure management  |                     |  |
| Qiong et al. [71]    | Base station energy        | DNN                   | O-CU-CP                      | Cell procedure management        |                     |  |
| Li et al. [72]       | UE and Base station energy | DNN                   | O-CU-CP                      | UE and Cell procedure management |                     |  |

Similarly, the LSTM algorithm is used, in [\[64\]](#page-21-8), to learn the mobility pattern of each UE from its historical trajectories, and predict its next mobility in the future. Based on the mobility prediction results, the corresponding base station will judge whether a handover is required for the UE or not. If yes, a dual connection will be established for the UE with the two base stations in the handover operation.

In [\[65\]](#page-21-9), the authors studied the energy consumption challenge of base stations (BS), especially with BS densification in 5G architecture. They proposed a reinforcement learning based scheme that controls the states of the BSs while respecting the requirements of users. They considered three levels of sleep modes, and the algorithm chooses how deep a BS can sleep while maximizing the trade-off between energy savings and users' QoS.

Similarly, another RL-based scheme was proposed in [\[66\]](#page-21-10). It aimed to derive a controller that efficiently activates different BSs' sleeping modes according to the targeted utility. Each BS uses its local information in order to learn the best energy-saving policy. In [\[67\]](#page-21-11), a deep reinforcementlearning based scheme was proposed to provide small cell (BS) activation strategy. The proposed scheme activates the optimal subset of small BSs in order to reduce energy consumption without compromising users' QoS. The authors formulated the small BSs on/off switching problem as a Markov Decision Process before solving it using Actor-Critic (AC) reinforcement learning methods.

In [\[68\]](#page-21-12), the authors addressed the handover challenge in 5G millimeter-wave vehicular networks. They proposed a proactive federated learning-based framework to optimize handover delay and thus ensuring the quality of service for users. The proposed framework enables avoiding frequent handovers and decide about handovers based on the mobility pattern of users. Federated learning allows to generate the learning model in a distributed way, which enables to minimize the communication cost of the training step. Simulation results prove the efficiency of the framework as compared to reactive schemes in reducing unnecessary handovers. User handoff in 5G RAN network slicing has been addressed in [\[69\]](#page-21-13). The authors devised an intelligent handoff policy that considers two main constraints: physical resources of base stations and logical connection of network slices. To do so, the authors have modeled the handover in RAN slicing as a Markov decision process and built a learning model using deep reinforcement learning to improve network throughput and users QoS.

To reduce the energy consumption of base stations, a traffic-aware control framework is proposed in [\[70\]](#page-21-14), to effectively activate/deactivate based stations based on traffic demand while ensuring users' QoS requirements. to this end, a data-driven learning scheme is designed to predict traffic demands by considering the semantic and geographical spatial-temporal relationship of mobile traffic. In the same context, the energy efficiency in RAN 5G to support ultrareliable low-latency and high data throughput services for both UEs and base stations has also been addressed in [\[71\]](#page-21-15). This work provides an overview of deep learning-based power-saving schemes in link with 5G standards.

# 2) DISCUSSION AND INTEGRATION WITH O-RAN

TABLE [4](#page-11-0) shows a comparison study between the works belonging to the mobility management module of Near-RT RIC.

• *Handover Management:* It is a critical function of RAN which consists of moving (hand over) users' connection from a cell to another, based on their mobility (users), so users will get better radio conditions and hence a better experience. In the literature, supervised learning techniques such as Deep Neural Network (DNN) is the most used to deal with such issue. DNN considers

the environmental context, such as the received signal power from users, and then predicts the suitable next base station to which users will migrate. Thus, DNN enables early preparation decisions of the handover procedure, which causes to reduce the handover cost. In the O-RAN architecture, the handover procedure will act at O-CU-CP module, in particular the functional block of UE and gNB procedure management.

• *Base Station Energy:* The base stations (BS) represent the main source of energy consumption in cellular networks. Therefore, one of the main functions of RAN is to manage the energy consumption of BSs, especially with BSs densification in 5G networks. In such context, reinforcement learning is the most applied to decide when BSs can switch between sleeping and active modes, while respecting users' QoS. The base station energy function will be implemented at the O-CU-CP module of the O-RAN architecture, which ensures cell procedure management.

We deduce that the works of this class concern mainly the O-CU-CP module that implements the functional blocks of UE, gNB, and Cell procedure management. Thus, the O-CU-CP is in charge of dealing with handover management and base station energy challenges, which are mainly addressed by the works of this class.

# *C. SPECTRUM MANAGEMENT OPTIMIZATION*

It aims at providing spectrum efficiency based on the new enabled 5G technologies, including Massive MIMO and mmWave [\[72\]](#page-21-16), [\[73\]](#page-21-17), [\[74\]](#page-21-18), [\[75\]](#page-21-19). This spectrum efficiency can be in terms of channel estimation, signal encoding and decoding, signal detection for massive MIMO, beam selection for mmWave, etc.

# 1) LITERATURE REVIEW

In [\[72\]](#page-21-16), the authors discussed the performance of deep learning for the following issues.

- Channel estimation: Deep learning was used for orthogonal frequency-division multiplexing (OFDM) systems [\[73\]](#page-21-17), where the output of the deep learning model recovers the input symbols without requiring channel detection. More specifically, the deep model takes as input both the transmitted symbols and received OFDM signals. The deep model will then be trained to minimize the difference between the input and output of the network.
- Signal encoding and decoding: A DNN with multiple dense layers was constructed to deal with signal encoding and decoding in [\[74\]](#page-21-18). The DNN encodes the transmitted signals as a one-hot vector. The transmitted signals through the wireless channel are added as a noise layer and are conveyed to the NN-based receiver. Finally, the decoded messages are the output signals with the highest probability, i.e., k bits comprise 2k messages. The simulation results showed that this

- DNN-based encoding and decoding scheme can generate the same performance as the Hamming code without requiring encoder and decoder functions.
- Signal classification: To provide an Automatic modulation classification (AMC) scheme for the environment and transmitter identification, a deep learningbased framework of signal classification was developed in [\[75\]](#page-21-19). The framework is based on input signals in polar coordinates and is trained to classify 11 typical modulation types. The framework comprises two main modules. The first one is based on LSTM for signal classification at a high signal-to-noise ratio (SNR), while the second one is based on Convolutional Neural Network (CNN) to deal with low SNR.

Finally, as the massive MIMO performance depends mainly on the quality of monitored CSI (Channel State Information) messages, the authors proposed a DNN-based framework for channel estimation issues when collecting CSI packets [\[72\]](#page-21-16). Simulation results showed that DNN is a suitable algorithm for an accurate CSI reconstruction and hence for high-performance channel estimation of the massive MIMO. The massive MIMO challenge of optimal detection at the receiver was also addressed in [\[76\]](#page-21-20). In this context, the maximum likelihood detection algorithm can obtain the lowest bit error rate (BER), however, the computational complexity increases as the number of antennas increases. The authors provided a neural network-based detection scheme. Experimental results showed that the proposed scheme can achieve low BER with low computational complexity.

The authors proposed an online learning algorithm to deal with the beam selection problem in mmWave vehicular communications [\[77\]](#page-21-21), [\[78\]](#page-21-22). The problem is modeled as a contextual multi-armed bandit problem, in which an agent has to select a subset of actions of unknown rewards with the goal to maximize the reward over time. Thus, this algorithm enables the mmWave base stations to autonomously learn about the appearance of blockages and changes in traffic patterns in order to select the best beam. Similarly, a deep learning-based beam Selection scheme was also proposed in [\[79\]](#page-21-23). It exploits CSI of a sub-6 GHz channel, in terms of power-delay profiles, to choose the more suitable mmWave beam.

To improve the accuracy of learned approximate message passing (LAMP) which is based on deep learning, a Gaussian mixture LAMP (GM-LAMP) scheme is proposed to estimate the channel in [\[80\]](#page-21-24). The authors first derive a shrinkage function to optimize the AMP scheme, which then replaces the original shrinkage function in the LAMP scheme. Therefore, a GM-LAMP scheme is designed to estimate the channel accurately. The performance of the proposed scheme is validated through simulation, as compared to the theoretical channel model. Similarly, in [\[81\]](#page-21-25), deep learning is used to enable distributed quantization, feedback, channel estimation, and downlink multi-user precoding for massive MIMO. The authors proposed a joint design of pilots and a deep neural network, to transform the received pilots into feedback

**TABLE 5. Spectrum management works on the top of O-RAN.**

<span id="page-13-0"></span>

| Works                 | Challenge                                      | Learning      | Link with O-RAN architecture |                           |                     |
|-----------------------|------------------------------------------------|---------------|------------------------------|---------------------------|---------------------|
| WOLKS                 | Chantenge                                      | algorithm     | O-RAN<br>module              | Functional<br>blocks      | Interfaces          |
| Huang et al. [73]     | Channel estimation                             | DNN           | O-DU                         | PUCCH<br>(High-PHY)       | O1 (Monitoring)     |
| Ye et al. [74]        | Channel estimation                             | DNN           | O-DU                         | PU(D)C(S)CH<br>(High-PHY) | A1 (Data Analytics) |
| O'Shea et al. [75]    | Signal encoding and decoding                   | DNN           | O-DU                         | PU(D)C(S)CH<br>(High-PHY) | E2 (Realization)    |
| Rajendran et al. [76] | Signal classification (modulation)             | LSTM<br>+ CNN | O-DU                         | PU(D)C(S)CH<br>(High-PHY) | (                   |
| Jia et al. [77]       | Signal detection at the receiver(Massive MIMO) | DNN           | O-DU                         | PUC(S)CH<br>(High-PHY)    |                     |
| Asadi et al. [78][79] | Beam selection<br>(mmWave)                     | RL            | O-RU                         | Low-PHY                   |                     |
| Sim et al. [80]       | Beam selection<br>(mmWave)                     | DNN           | O-RU                         | Low-PHY                   |                     |
| Wei et al. [81]       | Channel estimation                             | DNN           | O-DU                         | PU(D)C(S)CH<br>(High-PHY) |                     |
| Sohrabi et al. [82]   | Feedback and channel estimation                | DNN           | O-DU                         | PU(D)C(S)CH<br>(High-PHY) |                     |

bits at UE level, while mapping the UEs' feedback bits into the precoding matrix at the base stations side. Experimental results show that the proposed scheme can give the same performance when compared to the traditional precoding approaches.

#### 2) DISCUSSION AND INTEGRATION WITH O-RAN

TABLE [5](#page-13-0) compares the aforementioned works of this class, which target three main challenges.

- *Channel Estimation:* This function enables to recover the transmitted signal at the receiver side, in OFDM systems, which is very important for interference suppression. In fact, channel estimation is a challenging problem in wireless communications due to the frequency selectivity and time variance of channels. To deal with this issue, DNN is usually used in order to minimize the difference between the sent and received signals. The channel estimation function will be ensured by the PUCCH (Physical Uplink Control Channel) functional block of the O-RAN O-DU module.
- *Beam Selection:* With the emergence of mmWave and directional communications, the beam selection function consists of selecting the best beam, ensuring accurate beam alignments between the base stations and users. Either supervised learning or reinforcement learning are applied for beam selection. Reinforcement learning enables to update the beam based on users feedback, while DNN can help to predict the best beam based on the environmental context, such as presence of obstacles. In the O-RAN context, the Low-PHY layer of the O-RU module will be responsible of the beam selection function.
- *Signal Encoding, Decoding, and Classification:* This function enables to encode the signal before transmission, decode the signal at the receiver side, and classify automatically the signal in the corresponding modulation type. In this context, DNN is used to

deal with the signal encoding, decoding, and classification. DNN encodes the transmitted signal which is then conveyed to the neural network of the receiver (decoding). DNN classifier may also be built to classify the signals into the suitable modulation type. The PU(D)C(S)CH (Physical Uplink (Downlink) Control (Shared) Channel) functional block of the High-PHY layer is in charge of ensuring the signal encoding, decoding, and classification functions, the O-RAN O-DU module.

We clearly see that these works addressed the physical layer in terms of the O-DU (High-PHY) and O-RU (Low-PHY) modules, since they deal with spectrum-related challenges such as channel estimation at the reception side, signal encoding and decoding, beam selection, etc. These challenges are linked directly to the transmission channels (control and shared) in both uplink and downlink directions. In general, for the three classes of works, we remark that both supervised and reinforcement learning schemes such as DNN, LSTM, and RLs are widely used to deal with emerging challenges at the radio resources management level and the physical layer. These algorithms are usually used offline, i.e., the learning models are generated during an offline step, then only the final models are exploited in real-time. This may affect the performances of these models to deal with events that they did not see before, especially with the dynamic changes of cellular networks at the radio access level.

Moreover, to ensure the proper functioning of these works (the three classes), the O-RAN's O1 interface is in charge to monitor targeted data types from the O-DU module, for training learning models at the Non-RT RIC level. We note that the learning models can be trained offline or online at Non-RT RIC. Then, the generated model inference will be communicated to Near-RT RIC through the A1 interface in order to be executed in real-time at Near-RT RIC. Besides, at the Near-RT RIC, the inference results can be compared to the real data (collected through O1) to help detecting

![](_page_14_Figure_1.jpeg)

<span id="page-14-1"></span>**FIGURE 8. Deployment of Federated Deep Learning in O-RAN.**

resource management violations in real-time, for instance, latency or throughput violations. Hence, This will help to make more adequate decisions, e.g., to set new policies for ensuring the needed RAN requirements. Finally, the Near-RT RIC module can enforce these decisions on O-DUs through the E2 interface.

# <span id="page-14-0"></span>**IV. CASE STUDIES ON DEEP LEARNING DEPLOYMENT IN O-RAN**

In this section, we give two case studies for Deep Learning (DL) deployment in O-RAN. Based on the literature review, two main DL categories have been used: supervised deep learning and reinforcement deep learning.

# *A. SUPERVISED DEEP LEARNING DEPLOYMENT*

Supervised learning has been used either in a centralized way or federated (distributed) way, which is a recent technique developed by Google. Federated Learning (FL) aims to build models in a distributed way, while preserving the privacy of learners and reducing the network overhead. FL is suitable for O-RAN, since the latter is also based on a disaggregated and distributed split architecture (O-DU and O-RU).

Rather than sharing the data in a central node (e.g., cloud data centers [\[82\]](#page-21-26)), FL enables each learner to build locally a learning model using its (learner) proper data. Then, only local models (i.e., models' weights) are sent to a central node for aggregation. Once local models are aggregated, a global model is generated and is sent back to the learners.

In fact, FL suits well the O-RAN architecture as it enables not only to preserve the learners' privacy, especially in a multi-operator system, but also to reduce the network overhead by avoiding to share and transmit the required data. In the O-RAN context, local models can be built at the O-RU level, where generated data by users of a cell (or a subset of cells) are exploited locally to build local learning models, for instance, models to predict radio resources requirements to deal with resources allocation issue, or users mobility to address the handover challenge (**Step 1** in Fig. [8\)](#page-14-1). Then, the local models will be transmitted to the Non RT-RIC module for aggregation, through the O1 interface (**Step 2** in Fig. [8\)](#page-14-1). Aggregating local models enables to generate a global model which is sent to the near RT-RIC to be deployed in the related xApp (**Step 3** in Fig. [8\)](#page-14-1), according to the targeted challenge (radio resources management, spectrum management, mobility management, etc.). Thus, predictions will be performed in near real-time based on monitored data from the O-RU level via the O1 interfaces. However, when decisions must be taken to adjust xApp's parameters, for instance, updating the policy of radio resource allocation or that of the scheduler, the Near RT-RIC sends the DL-based decisions to the corresponding O-RAN module (O-DU or O-CU), through the E2 interface (**Step 4** in Fig. [8\)](#page-14-1).

Besides, data are monitored continuously from the O-RU part and stored in the database through the O1 interface. Hence, to build supervised models in a centralized way, the Non RT-RIC generates directly the needed model by leveraging the monitored and stored data in the database, before deploying them (learning models) in the related Near RT-RIC's xApps.

# *B. REINFORCEMENT DEEP LEARNING DEPLOYMENT*

Reinforcement deep learning enables to deploy an intelligent agent (or a set of agents) that learns in an interactive environment by trial and error, using feedback from its own

![](_page_15_Picture_1.jpeg)

FIGURE 9. Deployment of Reinforcement Deep Learning in O-RAN.

<span id="page-15-0"></span>actions and experiences. In other words, each agent interacts with its environment and gets either rewards or penalties for the actions it performs. Thus, reinforcement learning aims at finding a suitable action model for agents, that would maximize their (agents) total cumulative reward. In such context, the studied systems are usually modeled using Markov Decision Process (MDP) [83], before applying reinforcement learning to devise the optimal policy in terms of actions. MDP models a system as: (i) a set of states  $s \in S$ , (ii) a set of actions  $a \in A$ , (iii) a transition function  $a \in A$ , to move from a state  $a \in A$  to a new state  $a \in A$  when taking an action  $a \in A$ , and (iv) a reward function  $a \in A$ , when performing an action  $a \in A$  at a state  $a \in A$ .

In the literature, both Q-learning and Deep Q-Network (DQN) algorithms have been used to deal with the RAN challenges. Q-learning is used to determine an optimal policy, maximizing the expected total reward for any finite MDP where both state and action spaces are small. However, when the state and action space become high, DQN is applied, which is based on a neural network.

The intelligent agents are deployed at the near RT-RIC module of O-RAN, in order to improve the performance of running xApps (**Step 1** in Fig.. 9). These agents will interact with the external environment, which is composed of O-RU, O-DU, and O-CU. As a MDP system, these agents will periodically take actions to optimize the RAN performance, via the E2 interface (**Step 2** in Fig. 9). Then, through the O1 interface, the agents will receive the obtained reward and new state of the system (**Step 3** in Fig. 9). For example, to deal

with radio resource allocation and scheduling challenges, an intelligent agent may take an action to update the policy of resources allocation and scheduling in the O-DU's MAC layer, in order to meet users requirements (**Step 2** in Fig. 9). In this case, the reward can be determined based on the users quality of experiences, while the new state of the system can be reflected by the total number of allocated resource blocks and users' density. In this way, reinforcement learning helps at devising an optimal policy for resources assignment and scheduling while optimizing the users' quality of experiences.

We note that for DQN, the neural network takes the current state as the input and gives the Q-value (reward) of all possible actions as the output. Specifically, DQN uses two neural networks for learning: a prediction network  $Q(s; a; \theta)$  and target network  $Q'(s'; a; \theta')$ . The prediction network is updated at each iteration and used to evaluate the current state action. The target network  $Q'(s'; a; \theta')$  is used to generate target value. The target network is directly copied from the prediction network every several iterations (**Step 4** in Fig. 9). Thus, DQN aims to minimize the means squared error (loss function) between the outputs of both neural networks, as follows:

$$L = \left(r + \lambda \max_{a' \in A} Q'(s', a', \theta') - Q(s, a, \theta)\right)^{2} \tag{1}$$

where  $\theta$  represents the learning weights of the Q-network, which is updated through gradient back propagation [84]. r

![](_page_16_Figure_1.jpeg)

<span id="page-16-2"></span>**FIGURE 10. Manual ML Process in O-RAN.**

is the received reward. λ is the discount factor that notifies the importance of future rewards.

# <span id="page-16-0"></span>**V. AUTOMATION OF ALL STEPS OF MACHINE LEARNING SYSTEM CONSTRUCTION IN O-RAN**

One of the main features of O-RAN is the abundant usage of ML techniques, particularly Deep Learning (DL), to foster innovation and ease the deployment of intelligent RAN applications. However, the real challenge, in such context, is how to build ML models that ensure stable performances over their life cycle. Indeed, the performance of ML models may be degraded due mainly to constantly evolving data profiles [\[85\]](#page-21-29), hence such degradation must be considered to ensure the proper functioning of RAN applications. Therefore, there is a great need to not only monitor continuously both data profiles and online performance of deployed models, but also automate all steps of deep learning system building, including data preparation, model training, evaluation, and validation [\[86\]](#page-21-30).

This section discusses how to apply DevOps[1](#page-16-1) principles to ML systems (MLOps) in order to unify ML system development (Dev) and ML system operation (Ops) [\[86\]](#page-21-30). In fact, the level of automation of ML steps reflects the speed of

<span id="page-16-1"></span>1. It is a popular practice in designing, developing and operating software systems. It is based mainly on two concepts Continuous Integration (CI) and Continuous Delivery (CD), to provide benefits such as reducing the development cycles, increasing deployment speed, etc.

training new models or updating existing models, given new data profiles.

It is worth noting that this automation deployment concerns only the supervised learning models which are usually built at the O-RAN Non RT-RIC module and deployed at the Near RT-RIC module. In what follows, we describe two levels of MLOps, the most basic level (no automation) and automating all ML process level.

# *A. MANUAL MLOPS PROCESS IN O-RAN (LEVEL 1)*

It is the basic level of maturity, where the entire ML process in terms of creating and deploying learning models is manual. Fig. [10](#page-16-2) shows the main steps of this process that are performed at the Non RT-RIC module of O-RAN. Each step is executed manually, including data preparation, model training and validation. This level is based on a manual transition from one step to another, and driven by source code that is realised interactively, till an executable model is built and deployed at the Near RT-RIC module, via the A1 interface.

In practice, the manual process corresponds to the ML models that are rarely updated, which is not the case with the dynamic changes of wireless RAN. In particular, the performance of RAN's ML models may degrade due either to changes in the dynamics of the radio access environment, or changes in the data profiles describing the environment. Thus, introducing automation in the ML system process for the RAN part is more than required.

![](_page_17_Figure_1.jpeg)

<span id="page-17-0"></span>**FIGURE 11. Automation of ML Process in O-RAN.**

## *B. AUTOMATION MLOPS PROCESS IN O-RAN (LEVEL 2)*

This level aims to automate the ML system process, by performing continuous performance monitoring of models and models training; this then will ensure a continuous provision of model prediction service. We note that the Non RT-RIC module may monitor the performance of deployed ML models from the Near RT-RIC through the A1 interface, in order to enable such automation of the ML process.

To automate the process of considering new data to update deployed models, automated new data and model validation phases, as well as process triggers and metadata management are introduced to the ML process. Fig. [11](#page-17-0) illustrates the automated ML process. The main features and elements of this level are described, as follows.

- Continuous Training (CT) of models: The models are automatically trained leveraging new data and based on ML pipeline triggers.
- Continuous delivery (CD) of models: The ML pipeline continuously outputs prediction services of new trained models that are based on new data. The model deployment step is automated.
- Pipeline deployment: In the manual level, only a trained model is deployed to provide a prediction service. For automated level, an entire training pipeline is deployed, which automatically runs to deliver a prediction service through a trained model.
- Data and model validation: When the ML pipeline is deployed, it starts to be executed automatically, based on

one or more ML pipeline triggers. The pipeline expects fresh and new data to build new models. Hence, an automated data and model validation phase is needed. On one hand, data validation is required to decide whether the execution of the pipeline should be interrupted, or the models should be retrained. In this context, the models have to be retrained for two main reasons: (i) skews of the data schema, when the pipeline receives data that does not correspond to the expected ones, such as receiving new features, not all expected features are received, or receiving unexpected values of features. Therefore, the ML pipeline should be stopped and the developers' team should update it to deal with these issues. (ii) skews in data values, when statistical properties of data and their patterns are changed. In this case, the models should be retrained in order to consider these changes. On the other hand, once the new models are trained, the validation step occurs to evaluate and validate them before deploying them.

• Metadata management: To help in debugging errors and anomalies. The metadata records information about each ML pipeline execution, including parameter arguments of the pipeline and its executor, timestamp of pipeline execution in terms of start and end date time of each executed step, pointers to the outputs of each step of the pipeline as well as to previously built models, if rolling back to previous models will be needed, etc.

• ML pipeline triggers: The ML pipeline execution may be automated to update (retrain) the models based on several use cases: (i) On demand, when the pipeline is executed in a manual and ad-hoc way. (ii) On a schedule, when the pipeline is fed by new data, which is systematically available. (iii) Availability of new data, when new data is available in an ad-hoc way. (iv) On performance degradation of models. And (v) data distributions changes.

## <span id="page-18-0"></span>**VI. OPEN PROBLEMS AND FUTURE RESEARCH DIRECTIONS**

The development of O-RAN architecture is still in its early stages. Despite the various new functionalities it offers, many critical challenges are to be addressed and considered before deploying such architecture. In what follows, we discuss some of these challenges in addition to future research directions.

#### *A. O-RAN DEPLOYMENT SECURITY CONCERNS*

Disaggregating the main functions of RAN and implementing them in software increases the risk of the attack surface and threat of the network. Ericsson has just provided an indepth study on the main security concerns of the O-RAN architecture, including increased threat surface through the new interfaces; for example, A1, open front-haul, E2, etc., newly introduced threats at the Near-RT RIC, a threat to Trust Chain when decoupling of hardware [\[87\]](#page-21-31). These threats may directly affect the performance of the deep learningbased functional blocks. For instance, this split architecture opens the risk of Man-in-the-Middle attacks over the open front-haul interface. Thus, an adversary can manipulate the management and control traffic exchanged between the O-RU and O-DU modules. This can affect the accuracy of the learning models since they are built based on this traffic. Therefore, security measures should be implemented to address the threat risks of O-RAN deployment.

In such context, an O-RAN Security Task Group has started to address these security issues in order to ensure that the O-RAN deployment will meet an expected security level by the industry [\[88\]](#page-21-32). Furthermore, recent solutions started to leverage Blockchain technology, in order to secure and manage authentication and network access between trust-less network entities [\[89\]](#page-21-33). This represents a promising solution for the O-RAN architecture, especially with its disaggregated functions and decentralized management.

#### *B. NETWORK SLICING INTEGRATION CONCERNS*

The O-RAN architecture is expected to support network slicing (NS), which will enable the creation of multiple network slices tailored to fulfill diverse requirements. Thus, integrating NS may impact O-RAN in different manners. The O-RAN orchestrator (SMO) must be configured to consider the network slice template. Then, the performed predictions by AI/DL models, at near-RT RIC, must be compared to the slices' requirements in order to anticipate the slices' SLA violations. Moreover, to ensure network slice isolation, a secure partition of the Non-RT RIC and Near-RT RIC databases must be dedicated to each network slice. This enables to build either AI/DL models proper to each network slice or a global model aggregating network slices models, using, for instance, distributed federated learning [\[90\]](#page-21-34).

In this context, a slicing task working group has started to consider these concerns, and hence to support NSs in the O-RAN architecture [\[6\]](#page-19-5).

#### *C. SON AND MEC INTEGRATION CONCERNS*

Self-Organizing Network (SON) functions consist of a set of functions that aim at providing RAN management self-optimization [\[91\]](#page-21-35). These functions concern mainly the control of network capacity and coverage, QoS, interference, and energy consumption. SON was deployed in 4G networks [\[91\]](#page-21-35). Thus, it is also critical to consider the SON functions in the O-RAN architecture and deploy them in the 5G networks. In fact, the SON functions are based on periodic feedback loops. Therefore, these functions can be deployed at both O-RAN's Non-RT RIC to build AI/DL models and near-RT RIC, to monitor RAN and enabling its management automation. In addition, the Non-RT RIC can also orchestrate the SON services.

Even the 3GPP standard does not design any detailed architecture of SON; however, there is ongoing work on the 5G SON to deal with end-to-end 5G network management [\[92\]](#page-21-36).

On the other hand, ETSI Multi-access Edge Computing (MEC) consists of deploying computation and storage capability close to UEs, and thus reducing the network latency [\[93\]](#page-21-37). To do so, it (MEC) exploits mainly the RAN contextual information to enable time-sensitive and traffic redirection applications, provide service-oriented APIs such as radio conditions and users location contexts, etc. Hence, there is a great need for efficient MEC and O-RAN integration in order to enable MEC-related management. It is worth noting that MEC was defined for 4G networks; however, its integration with the 5G network is still in progress. In fact, since MEC aims to provide a low latency network, MEC hosts can act at the near-RT RIC of O-RAN. In addition, the O-RAN databases can integrate the MEC databases storing, Radio Network Information Service (RNIS), cell performance, users locations, etc [\[94\]](#page-21-38). Moreover, the Non-RT RIC (O-RAN orchestrator) can also orchestrate the mobile edge applications.

# *D. ONLINE AND PRIVACY-PRESERVING DISTRIBUTED LEARNING CONCERNS*

Actually, the O-RAN architecture is adopted to build offline DL models in Non-RT RIC before deploying them at the Near-RT RIC. However, several RAN-related challenges, such as radio resource allocation and scheduling, require to generate online and real-time DL models, using, for instance, reinforcement deep learning. This enables to adapt them (learning models) according to the dynamic radio changes

and contextual information, including users mobility and energy, needed throughput and latency, etc. In such a context, the online DL models must be integrated into the Near-RT RIC as xApp, to be in charge of building and updating learning models in real-time. This integration is already visible to the O-RAN alliance actors, but it must be enforced.

Besides, disaggregating the RAN functions, implementing them in software, and the distributed split architecture (O-DU, O-RU) have motivated the use of distributed deep learning models, such as Federated Learning (FL) [\[16\]](#page-20-6), [\[90\]](#page-21-34). As mentioned before, FL preserves the privacy of learners by sharing only their local models rather than their privacysensitive data. This learning technique corresponds greatly to the O-RAN architecture, for instance, to ensure isolation of running slices on top of O-RAN.

# *E. CONVERGENCE AND SCALABILITY CONCERNS OF LEARNING TECHNIQUES*

As mentioned before, the distributed split architecture (O-DU and O-RU) of O-RAN calls for the use of distributed and multi-agent learning techniques. However, the convergence of such techniques is a challenging problem, where these techniques should converge efficiently and quickly to avoid any instability situation [\[95\]](#page-21-39). In such context, fast boot strapping techniques may be used, which helps to speed the learning schemes convergence [\[96\]](#page-21-40). Furthermore, as the number of O-RAN entities (O-DU and O-RU) tends to increase and almost all of RAN functions are becoming intelligent based on ML/DL models, the scalability of learning schemes and O-RAN architecture must be addressed on a specific basis.

# *F. ENERGY CONCERNS WITH FUNCTION SPLITTING OF O-RAN*

With the growing impetus of O-RAN architecture, ensuring an efficient function splitting in O-RAN, while reducing the energy consumption of the RAN hardware and software is becoming highly important. In fact, energy efficiency plays a vital role in decision-making process of cellular networks, due to the considerable increase in their cost and carbon footprint caused by the high demand for data and network densification. In such a context, leveraging renewable energy sources at the RAN level is a promising approach to optimize the energy consumption of RAN hardware and software. However, network managers need to optimize energy usage since they must store this energy in limited batteries in terms of capacities. In addition, renewable energy is intermittent, and the supply is not always guaranteed [\[97\]](#page-22-0). Hence, under the instability of renewable energies and the dynamic nature of the wireless networks, efficient functional splitting in green O-RAN is becoming a critical need which can be addressed by machine/deep learning schemes, in particular reinforcement learning techniques [\[20\]](#page-20-10). Besides, network sharing techniques also represent ideal candidates to ensure O-RAN energy efficiency. In [\[98\]](#page-22-1), the author discussed about adopting such techniques to 5G networks, to reduce the network cost. The author also mentioned several RAN sharing use cases including, MEC sharing, energy sharing, spectrum and fronthaul sharing, etc. Therefore, these network sharing techniques can be leveraged in the O-RAN context, in order to not only ensure an efficient function splitting, but also to enable an energy efficiency of the RAN part.

# <span id="page-19-9"></span>**VII. CONCLUSION**

This paper reviews deep learning-based works proposed to enhance the 5G RAN part and how it can be integrated with the AI-enabled O-RAN architecture. O-RAN Alliance aims to transform the RAN to an intelligent, open, and interoperable system, by disaggregating the traditional RAN functions, providing their software implementation, and connecting them using standardized and open interfaces.

We first provided a general introduction about the evolution of the RAN architectures towards 5G, including the open RAN architecture and its components. We also compared them based on various perspectives, such as edge support, virtualization, control and management, energy consumption, and AI support. Then, we reviewed existing deep learningbased RAN works, in addition to how they can be integrated into the emerged O-RAN architecture. Moreover, we showed two case studies on deep learning deployment in O-RAN, as well as how the main steps of deep learning process may be automated, to ensure delivering acceptable performance by the deployed learning models. Finally, we discussed key open challenges and future research directions about the O-RAN architecture and the use of deep learning techniques under such architecture.

As future work, we are working to deploy deep learning algorithms in O-RAN as a proof of concept, using both Open Air Interface platform and the open-source O-RAN Software, Amber.

## <span id="page-19-0"></span>**REFERENCES**

- [1] W. Saad, M. Bennis, and M. Chen, "A vision of 6G wireless systems: Applications, trends, technologies, and open research problems," *IEEE Netw.*, vol. 34, no. 3, pp. 134–142, May/Jun. 2020.
- <span id="page-19-1"></span>[2] F. Tariq, M. R. A. Khandaker, K.-K. Wong, M. A. Imran, M. Bennis, and M. Debbah, "A speculative study on 6G," *IEEE Wireless Commun.*, vol. 27, no. 4, pp. 118–125, Aug. 2020.
- <span id="page-19-2"></span>[3] M. A. Habibi, M. Nasimi, B. Han, and H. D. Schotten, "A comprehensive survey of RAN architectures toward 5G mobile communication system," *IEEE Access*, vol. 7, pp. 70371–70421, 2019.
- <span id="page-19-3"></span>[4] A. Ksentini and N. Nikaein, "Toward enforcing network slicing on RAN: Flexibility and resources abstraction," *IEEE Commun. Mag.*, vol. 55, no. 6, pp. 102–108, Jun. 2017.
- <span id="page-19-4"></span>[5] A. Marotta, D. Cassioli, K. Kondepu, C. Antonelli, and L. Valcarenghi, "Exploiting flexible functional split in converged software defined access networks," *IEEE/OSA J. Opt. Commun. Netw.*, vol. 11, no. 11, pp. 536–546, Nov. 2019.
- <span id="page-19-5"></span>[6] "O-RAN: Towards an open and smart RAN," O-RAN Alliance, Alfter, Germany, Rep., Oct. 2018.
- <span id="page-19-6"></span>[7] S. Abeta, T. Kawahara, A. Umesh, and R. Matsukawa, "O-RAN Alliance standardization trends," *NTT DOCOMO Technol. J.*, vol. 21, pp. 38–45, Jul. 2019.
- <span id="page-19-7"></span>[8] "O-RAN Alliance, O-RAN Software Community." Apr. 2019. [Online]. Available: https://O-RAN-sc.org/
- <span id="page-19-8"></span>[9] "Operator Defined Next Generation RAN Architecture And Interfaces." [Online]. Available: https://www.O-RAN.org/ (accessed Feb. 12, 2020).

- <span id="page-20-0"></span>[10] R. T. Rodoshi and W. Choi, "A survey on applications of deep learning in cloud radio access network," *IEEE Access*, vol. 9, pp. 61972–61997, 2021.
- <span id="page-20-1"></span>[11] W. Ejaz, S. K. Sharma, S. Saadat, M. Naeem, A. Anpalagan, and N. A. Chughtai, "A comprehensive survey on resource allocation for CRAN in 5G and beyond networks," *J. Netw. Comput. Appl.*, vol. 160, Jun. 2020, Art. no. 102638.
- <span id="page-20-2"></span>[12] A. S. Abdalla, P. S. Upadhyaya, V. K. Shah, and V. Marojevic, "Toward next generation open radio access network-what O-RAN can and cannot do!" 2021, *arXiv:2111.13754*.
- <span id="page-20-3"></span>[13] S. Niknam *et al.*, "Intelligent O-RAN for beyond 5G and 6G wireless networks," 2020, *arXiv:2005.08374*.
- <span id="page-20-4"></span>[14] A. Garcia-Saavedra and X. Costa-Pérez, "O-RAN: Disrupting the virtualized RAN ecosystem," *IEEE Commun. Stand. Mag.*, vol. 5, no. 4, pp. 96–103, Dec. 2021.
- <span id="page-20-5"></span>[15] H. Kumar, V. Sapru, and S. K. Jaisawal, "O-RAN based proactive ANR optimization," in *Proc. IEEE Globecom Workshops (GC Wkshps*, Taipei, Taiwan, 2020, pp. 1–4.
- <span id="page-20-6"></span>[16] P. E. I. Rivera, S. Mollahasani, and M. Erol-Kantarci, "Multi agent team learning in disaggregated virtualized open radio access networks (O-RAN)," 2021, *arXiv:2012.04861*.
- <span id="page-20-7"></span>[17] S. K. Singh, R. Singh, and B. Kumbhani, "The evolution of radio access network towards open-RAN: Challenges and opportunities," in *Proc. IEEE Wireless Commun. Netw. Conf. Workshops (WCNCW)*, Seoul, South Korea, 2020, pp. 1–6.
- <span id="page-20-8"></span>[18] W. Diego, "Evolution toward the next generation radio access network," in *Proc. IFIP Netw. Conf. (Networking)*, Paris, France, 2020, pp. 685–685.
- <span id="page-20-9"></span>[19] C.-L. I, S. Kuklinskí, and T. Chen, "A perspective of O-RAN integration with MEC, SON, and network slicing in the 5G era," *IEEE Network*, vol. 34, no. 6, pp. 3–4, Nov./Dec. 2020, doi: [10.1109/MNET.2020.9277891.](https://doi.org/10.1109/MNET.2020.9277891)
- <span id="page-20-10"></span>[20] T. Pamuklu, M. Erol-Kantarci, and C. Ersoy, "Reinforcement learning based dynamic function splitting in disaggregated green open RANs," 2021, *arXiv:2012.03213*.
- <span id="page-20-11"></span>[21] K. Boutiba, A. Ksentini, B. Brik, Y. Challal, and A. Balla, "NRflex: Enforcing network slicing in 5G new radio," *Comput. Commun.*, vol. 181, pp. 284–292, Jan. 2022.
- <span id="page-20-12"></span>[22] P. Trakadas *et al.*, "A cost-efficient 5G non-public network architectural approach: Key concepts and enablers, building blocks and potential use cases," *Sensors*, vol. 21, no. 16, p. 5578, 2021.
- <span id="page-20-13"></span>[23] M. Polese, L. Bonati, S. D'Oro, S. Basagni, and T. Melodia, "ColO-RAN: Developing machine learning-based xApps for open RAN closed-loop control on programmable experimental platforms," 2021, *arXiv:2112.09559*.
- <span id="page-20-14"></span>[24] L. Bonati, S. D'Oro, M. Polese, S. Basagni, and T. Melodia, "Intelligence and learning in O-RAN for data-driven NextG cellular networks," *IEEE Commun. Mag.*, vol. 59, no. 10, pp. 21–27, Oct. 2021.
- <span id="page-20-15"></span>[25] H. Lee, J. Cha, D. Kwon, M. Jeong, and I. Park, "Hosting AI/ML workflows on O-RAN RIC platform," in *Proc. IEEE Globecom Workshops (GC Wkshps*, Taipei, Taiwan, 2020, pp. 1–6.
- <span id="page-20-16"></span>[26] M. S. Hossain and G. Muhammad, "A deep-tree-model-based radio resource distribution for 5G networks," *IEEE Wireless Commun.*, vol. 27, no. 1, pp. 62–67, Feb. 2020.
- <span id="page-20-17"></span>[27] M. Yan, G. Feng, J. Zhou, Y. Sun, and Y.-C. Liang, "Intelligent resource scheduling for 5G radio access network slicing," *IEEE Trans. Veh. Technol.*, vol. 68, no. 8, pp. 7691–7703, Aug. 2019.
- <span id="page-20-18"></span>[28] Y. Zhou, Z. M. Fadlullah, B. Mao, and N. Kato, "A deep-learningbased radio resource assignment technique for 5G ultra dense networks," *IEEE Netw.*, vol. 32, no. 6, pp. 28–34, Nov./Dec. 2018.
- <span id="page-20-19"></span>[29] J. Hall, K. Moessner, R. MacKenzie, F. Carrez, and C. H. Foh, "Dynamic scheduler management using deep learning," *IEEE Trans. Cogn. Commun. Netw.*, vol. 6, no. 2, pp. 575–585, Jun. 2020.
- <span id="page-20-20"></span>[30] H. Raza, "A brief survey of radio access network backhaul evolution: Part II," *IEEE Commun. Mag.*, vol. 51, no. 5, pp. 170–177, May 2013.
- <span id="page-20-21"></span>[31] E. Dahlman, S. Parkvall, J. Skold, and P. Beming, *3G Evolution: HSPA and LTE for Mobile Broadband*, 2nd ed. Boston, MA, USA: Academic, 2008.
- <span id="page-20-22"></span>[32] I. A. Alimi, A. L. Teixeira, and P. P. Monteiro, "Toward an efficient C-RAN optical fronthaul for the future networks: A tutorial on technologies, requirements, challenges, and solutions," *IEEE Commun. Surveys Tuts.*, vol. 20, no. 1, pp. 708–769, 1st Quart., 2018.

- <span id="page-20-23"></span>[33] "C-RAN the road towards green RAN-white paper," China Mobile Res. Inst., China Mobile, Beijing, China, Rep. MSU-CSE-06-2, Oct. 2011.
- <span id="page-20-24"></span>[34] X. Wang *et al.*, "Virtualized cloud radio access network for 5G Transport," *IEEE Commun. Mag.*, vol. 55, no. 9, pp. 202–209, Sep. 2017.
- <span id="page-20-26"></span>[35] "Transport network support of IMT-2020/5G," ITU, Geneva, Switzerland, Rep. GSTR-TN5G, 2018.
- <span id="page-20-25"></span>[36] "Technical specification group radio access network; study on new radio access technology: Radio access architecture and interfaces," 3GPP, Sophia Antipolis, France, 3GPP Rep. TR 38.801, 2017.
- <span id="page-20-27"></span>[37] "475 series (ng-RAN; F1 interface), 3GPP Release 15," 3GPP, Sophia Antipolis, France, 3GPP Rep. TS 38.470, 2017.
- <span id="page-20-28"></span>[38] "O-RAN Slicing Architecture 5.0—July 2021 (O-RAN.WG1. Slicing-Architecture-v05.00)." [Online]. Available: https://www.O-RAN.org/specifications (accessed Dec. 29, 2021).
- <span id="page-20-29"></span>[39] "O-RAN Slicing Architecture 4.0—March 2021 (O-RAN.WG1. Slicing-Architecture-v04.00)." [Online]. Available: https://www.O-RAN.org/specifications (accessed Dec. 30, 2021).
- <span id="page-20-30"></span>[40] B. Brik and A. Ksentini, "Toward optimal MEC resource dimensioning for a vehicle collision avoidance system: A deep learning approach," *IEEE Netw.*, vol. 35, no. 3, pp. 74–80, May/Jun. 2021.
- <span id="page-20-31"></span>[41] A. Ksentini and B. Brik, "An edge-based social distancing detection service to mitigate COVID-19 propagation," *IEEE Internet Things Mag.*, vol. 3, no. 3, pp. 35–39, Sep. 2020.
- <span id="page-20-32"></span>[42] A. Checko *et al.*, "Cloud RAN for mobile networks—A technology overview," *IEEE Commun. Surveys Tuts.*, vol. 17, no. 1, pp. 405–426, 1st Quart., 2015.
- <span id="page-20-33"></span>[43] "C-RAN the road towards green RAN," China Mobile Res. Inst., China Mobile, Beijing, China, Rep., Oct. 2011.
- <span id="page-20-34"></span>[44] J. Lorincz, T. Garma, and G. Petrovic, "Measurements and modelling of base station power consumption under real traffic loads," *Sensors*, vol. 12, no. 4, pp. 4281–4310, 2012.
- <span id="page-20-35"></span>[45] N. Carapellese, A. Pizzinat, M. Tornatore, P. Chanclou, and S. Gosselin, "An energy consumption comparison of different mobile backhaul and fronthaul optical access architectures," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Cannes, France, 2014, pp. 1–3.
- <span id="page-20-36"></span>[46] U. Fattore, M. Liebsch, B. Brik, and A. Ksentini, "AutoMEC: LSTMbased user mobility prediction for service management in distributed MEC resources," in *Proc. 23rd Int. ACM Conf. Model. Anal. Simul. Wireless Mobile Syst.*, New York, NY, USA, 2020, pp. 155–159.
- <span id="page-20-37"></span>[47] "Artificial Intelligence and Machine Learning—3GPP, Release-17." Jun. 2021. [Online]. Available: https://www.3gpp.org/newsevents/2201-ai\_ml\_r3 (accessed Dec. 31, 2021).
- <span id="page-20-38"></span>[48] M. Chen, W. Saad, and C. Yin, "Virtual reality over wireless networks: Quality-of-service model and learning-based resource management," *IEEE Trans. Commun.*, vol. 66, no. 11, pp. 5621–5635, Nov. 2018.
- <span id="page-20-39"></span>[49] I. Com¸sa *et al.*, "Towards 5G: A reinforcement learning-based scheduling solution for data traffic management," *IEEE Trans. Netw. Service Manag.*, vol. 15, no. 4, pp. 1661–1675, Dec. 2018.
- <span id="page-20-40"></span>[50] F. Meng, P. Chen, L. Wu, and J. Cheng, "Power allocation in multi-user cellular networks: Deep reinforcement learning approaches," *IEEE Trans. Wireless Commun.*, vol. 19, no. 10, pp. 6255–6267, Oct. 2020.
- <span id="page-20-41"></span>[51] K. I. Ahmed and E. Hossain, "A deep Q-learning method for downlink power allocation in multi-cell networks," 2019, *arXiv:1904.13032*.
- <span id="page-20-43"></span>[52] S. Samarakoon, M. Bennis, W. Saad, and M. Debbah, "Distributed federated learning for ultra-reliable low-latency vehicular communications," *IEEE Trans. Commun.*, vol. 68, no. 2, pp. 1146–1159, Feb. 2020.
- <span id="page-20-44"></span>[53] A. T. Z. Kasgari and W. Saad, "Model-free ultra reliable low latency communication (URLLC): A deep reinforcement learning framework," in *Proc. IEEE Int. Conf. Commun. (ICC)*, Shanghai, China, 2019, pp. 1–6.
- <span id="page-20-42"></span>[54] C. D'Andrea, A. Zappone, S. Buzzi, and M. Debbah, "Uplink power control in cell-free massive MIMO via deep learning," in *Proc. IEEE 8th Int. Workshop Comput. Adv. Multi-Sens. Adapt. Process. (CAMSAP)*, Le Gosier, Guadeloupe, 2019, pp. 554–558.
- <span id="page-20-45"></span>[55] Z. Du, Y. Deng, W. Guo, A. Nallanathan, and Q. Wu, "Green deep reinforcement learning for radio resource management: Architecture, algorithm compression, and challenges," *IEEE Veh. Technol. Mag.*, vol. 16, no. 1, pp. 29–39, Mar. 2021.

- <span id="page-21-2"></span>[56] F. Al-Tam, N. Correia, and J. Rodriguez, "Learn to schedule (LEASCH): A deep reinforcement learning approach for radio resource scheduling in the 5G MAC layer," *IEEE Access*, vol. 8, pp. 108088–108101, 2020.
- <span id="page-21-3"></span>[57] F. AL-Tam, A. Mazayev, N. Correia, and J. Rodriguez, "Radio resource scheduling with deep pointer networks and reinforcement learning," in *Proc. IEEE 25th Int. Workshop Comput.-Aided Model. Des. Commun. Links Netw. (CAMAD)*, Pisa, Italy, 2020, pp. 1–6.
- <span id="page-21-0"></span>[58] S. Bakri, B. Brik, and A. Ksentini, "On using reinforcement learning for network slice admission control in 5G: Offline vs. online," *Int. J. Commun. Syst.*, vol. 34, no. 7, p. e4757, 2021.
- <span id="page-21-1"></span>[59] B. Brik and A. Ksentini, "On predicting service-oriented network slices performances in 5G: A federated learning approach," in *Proc. IEEE 45th Conf. Local Comput. Netw. (LCN)*, Los Alamitos, CA, USA, Nov. 2020, pp. 164–171.
- <span id="page-21-4"></span>[60] W. Chérif, A. Ksentini, D. Négru, and M. Sidibé, "A\_psqa: Efficient real-time video streaming QoE tool in a future media Internet context," in *Proc. IEEE Int. Conf. Multimedia Expo (ICME)*, Barcelona, Spain, Jul. 2011, pp. 1–6.
- <span id="page-21-5"></span>[61] K. Piamrat, A. Ksentini, C. Viho, and J.-M. Bonnin, "QoE-aware vertical handover in wireless heterogeneous networks," in *Proc. 7th Int. Wireless Commun. Mobile Comput. Conf. (IWCMC)*, Istanbul, Turkey, Jul. 2011, pp. 95–100.
- <span id="page-21-6"></span>[62] C. Lee, H. Cho, S. Song, and J.-M. Chung, "Prediction-based conditional handover for 5G mm-wave networks: A deep-learning approach," *IEEE Veh. Technol. Mag.*, vol. 15, no. 1, pp. 54–62, Mar. 2020.
- <span id="page-21-7"></span>[63] M. Ozturk, M. Gogate, O. Onireti, A. Adeel, A. Hussain, and M. A. Imran, "A novel deep learning driven, low-cost mobility prediction approach for 5G cellular networks: The case of the control/data separation architecture (CDSA)," *Neurocomputing*, vol. 358, pp. 479–489, Sep. 2019.
- <span id="page-21-8"></span>[64] C. Wang, Z. Zhao, Q. Sun, and H. Zhang, "Deep learning-based intelligent dual connectivity for mobility management in dense network," in *Proc. IEEE 88th Veh. Technol. Conf. (VTC-Fall)*, Chicago, IL, USA, 2018, pp. 1–5.
- <span id="page-21-9"></span>[65] A. El-Amine, M. Iturralde, H. A. H. Hassan, and L. Nuaymi, "A distributed Q-learning approach for adaptive sleep modes in 5G networks," in *Proc. IEEE Wireless Commun. Netw. Conf. (WCNC)*, Marrakesh, Morocco, 2019, pp. 1–6.
- <span id="page-21-10"></span>[66] F. E. Salem, Z. Altman, A. Gati, T. Chahed, and E. Altman, "Reinforcement learning approach for advanced sleep modes management in 5G networks," in *Proc. IEEE 88th Veh. Technol. Conf. (VTC-Fall)*, Chicago, IL, USA, 2018, pp. 1–5.
- <span id="page-21-11"></span>[67] J. Ye and Y.-J. A. Zhang, "Drag: Deep reinforcement learning based base station activation in heterogeneous networks," *IEEE Trans. Mobile Comput.*, vol. 19, no. 9, pp. 2076–2087, Sep. 2020.
- <span id="page-21-12"></span>[68] K. Qi, T. Liu, and C. Yang, "Federated learning based proactive handover in millimeter-wave vehicular networks," in *Proc. 15th IEEE Int. Conf. Signal Process. (ICSP)*, vol. 1. Beijing, China, 2020, pp. 401–406.
- <span id="page-21-13"></span>[69] Y. Wu, G. Zhao, D. Ni, and J. Du, "Dynamic handoff policy for RAN slicing by exploiting deep reinforcement learning," *EURASIP J. Wireless Comput. Netw.*, vol. 2021, p. 61, Mar. 2021.
- <span id="page-21-14"></span>[70] Q. Wu, X. Chen, Z. Zhou, L. Chen, and J. Zhang, "Deep reinforcement learning with spatio-temporal traffic forecasting for data-driven base station sleep control," *IEEE/ACM Trans. Netw.*, vol. 29, no. 2, pp. 935–948, Apr. 2021.
- <span id="page-21-15"></span>[71] Y.-N. R. Li, M. Chen, J. Xu, L. Tian, and K. Huang, "Power saving techniques for 5G and beyond," *IEEE Access*, vol. 8, pp. 108675–108690, 2020.
- <span id="page-21-16"></span>[72] H. Huang *et al.*, "Deep learning for physical-layer 5G wireless techniques: Opportunities, challenges and solutions," *IEEE Wireless Commun.*, vol. 27, no. 1, pp. 214–222, Feb. 2020.
- <span id="page-21-17"></span>[73] H. Ye, G. Y. Li, and B.-H. Juang, "Power of deep learning for channel estimation and signal detection in OFDM systems," *IEEE Wireless Commun. Lett.*, vol. 7, no. 1, pp. 114–117, Feb. 2018.
- <span id="page-21-18"></span>[74] T. O'Shea and J. Hoydis, "An introduction to deep learning for the physical layer," *IEEE Trans. Cogn. Commun. Netw.*, vol. 3, no. 4, pp. 563–575, Dec. 2017.
- <span id="page-21-19"></span>[75] S. Rajendran, W. Meert, D. Giustiniano, V. Lenders, and S. Pollin, "Deep learning models for wireless signal classification with distributed low-cost spectrum sensors," *IEEE Trans. Cogn. Commun. Netw.*, vol. 4, no. 3, pp. 433–445, Sep. 2018.

- <span id="page-21-20"></span>[76] Z. Jia, W. Cheng, and H. Zhang, "A partial learning-based detection scheme for massive MIMO," *IEEE Wireless Commun. Lett.*, vol. 8, no. 4, pp. 1137–1140, Aug. 2019.
- <span id="page-21-21"></span>[77] A. Asadi, S. Müller, G. H. Sim, A. Klein, and M. Hollick, "FML: Fast machine learning for 5G mmWave vehicular communications," in *Proc. IEEE INFOCOM Conf. Comput. Commun.*, Honolulu, HI, USA, 2018, pp. 1961–1969.
- <span id="page-21-22"></span>[78] G. H. Sim, S. Klos, A. Asadi, A. Klein, and M. Hollick, "An online context-aware machine learning algorithm for 5G mmWave vehicular communications," *IEEE/ACM Trans. Netw.*, vol. 26, no. 6, pp. 2487–2500, Dec. 2018.
- <span id="page-21-23"></span>[79] M. S. Sim, Y.-G. Lim, S. H. Park, L. Dai, and C.-B. Chae, "Deep learning-based mmWave beam selection for 5G NR/6G with sub-6 GHz channel information: Algorithms and prototype validation," *IEEE Access*, vol. 8, pp. 51634–51646, 2020.
- <span id="page-21-24"></span>[80] X. Wei, C. Hu, and L. Dai, "Deep learning for beamspace channel estimation in millimeter-wave massive MIMO systems," *IEEE Trans. Commun.*, vol. 69, no. 1, pp. 182–193, Jan. 2021.
- <span id="page-21-25"></span>[81] F. Sohrabi, K. M. Attiah, and W. Yu, "Deep learning for distributed channel feedback and multiuser precoding in FDD massive MIMO," *IEEE Trans. Wireless Commun.*, vol. 20, no. 7, pp. 4044–4057, Jul. 2021.
- <span id="page-21-26"></span>[82] B. Brik, N. Lagraa, N. Tamani, A. Lakas, and Y. Ghamri-Doudane, "Renting out cloud services in mobile vehicular cloud," *IEEE Trans. Veh. Technol.*, vol. 67, no. 10, pp. 9882–9895, Oct. 2018.
- <span id="page-21-27"></span>[83] Y. Chen, Y. Gao, C. Jiang, and K. J. R. Liu, "Game theoretic Markov decision processes for optimal decision making in social systems," in *Proc. IEEE Global Conf. Signal Inf. Process. (GlobalSIP)*, Atlanta, GA, USA, 2014, pp. 268–272.
- <span id="page-21-28"></span>[84] D. P. Kingma and J. Ba, "Adam: A method for stochastic optimization," in *Proc. 3rd Int. Conf. Learn. Represent. (ICLR)*, San Diego, CA, USA, May 2015, pp. 1–14. [Online]. Available: http://arxiv.org/abs/1412.6980
- <span id="page-21-29"></span>[85] D. Sculley *et al.*, "Machine learning: The high-interest credit card of technical debt," in *Proc. SE4ML Softw. Eng. Mach. Learn. (NIPS Workshop)*, 2014, pp. 1–9.
- <span id="page-21-30"></span>[86] "MLOps: Continuous Delivery and Automation Pipelines in Machine Learning." [Online]. Available: https://cloud.google.com/architecture/ mlops-continuous-delivery-and-automation-pipelines-in-machinelearning (accessed Sep. 21, 2021).
- <span id="page-21-31"></span>[87] "Security Considerations of Open RAN." Ericsson. [Online]. Available: https://www.ericsson.com/en/security/security-considera tions-of-open-ran (accessed May 1, 2021).
- <span id="page-21-32"></span>[88] "The O-RAN Alliance Security Task Group Tackles Security Challenges on all O-RAN Interfaces and Components." O-RAN Alliance. [Online]. Available: https://www.O-RAN.org/blog/2020/ 10/24/the-O-RAN-alliance-security-task-group-tackles-securitychallenges-on-all-O-RAN-interfaces-and-components (accessed May 1, 2021).
- <span id="page-21-33"></span>[89] X. Ling, J. Wang, T. Bouchoucha, B. C. Levy, and Z. Ding, "Blockchain radio access network (b-RAN): Towards decentralized secure radio access paradigm," *IEEE Access*, vol. 7, pp. 9714–9723, 2019.
- <span id="page-21-34"></span>[90] B. Brik, A. Ksentini, and M. Bouaziz, "Federated learning for UAVsenabled wireless networks: Use cases, challenges, and open problems," *IEEE Access*, vol. 8, pp. 53841–53849, 2020.
- <span id="page-21-35"></span>[91] *Telecommunication Management; Self-Organizing Networks (SON); Concepts and Requirements, V16.0.0*, 3GPP Standard TS 32.500, Jul. 2020.
- <span id="page-21-36"></span>[92] *Self-Organizing Networks (SON) for 5G Network, V16.0.0*, 3GPP Standard TS 28.313, Sep. 2020.
- <span id="page-21-37"></span>[93] *Multi-Access Edge Computing (MEC); Framework and Reference Architecture*, ETSI Standard GS MEC 003 v2.1.1, Jan. 2019.
- <span id="page-21-38"></span>[94] B. Brik, P. A. Frangoudis, and A. Ksentini, "Service-oriented MEC applications placement in a federated edge cloud architecture," in *Proc. IEEE Int. Conf. Commun. (ICC)*, Dublin, Ireland, 2020, pp. 1–6.
- <span id="page-21-39"></span>[95] B. Yongacoglu, G. Arslan, and S. Yüksel, "Reinforcement learning for decentralized stochastic control," in *Proc. IEEE 58th Conf. Decis. Control (CDC)*, Nice, France, 2019, pp. 5556–5561.
- <span id="page-21-40"></span>[96] C. Gelada and M. G. Bellemare, "Off-policy deep reinforcement learning by bootstrapping the covariate shift," 2019, *arXiv:1901.09455*.

- <span id="page-22-0"></span>[97] P.-H. Chiang, R. B. Guruprasad, and S. Dey, "Optimal use of harvested solar, hybrid storage and base station resources for green cellular networks," *IEEE Trans. Green Commun. Netw.*, vol. 2, no. 3, pp. 707–720, Sep. 2018.
- <span id="page-22-1"></span>[98] A. Antonopoulos, "Bankruptcy problem in network sharing: Fundamentals, applications and challenges," *IEEE Wireless Commun.*, vol. 27, no. 4, pp. 81–87, Aug. 2020.

![](_page_22_Picture_3.jpeg)

**BOUZIANE BRIK** received the engineering degree (First Class) in computer science and the Magister degree from the University of Laghouat, Algeria, in 2010 and 2013, respectively, and the Ph.D. degree from the University of Laghouat and La Rochelle University, France, in 2017. He is currently working as an Associate Professor with Burgundy (Bourgogne) University and DRIVE Laboratory. Before joining Burgundy University, he was a Postdoctoral Fellow with the University of Troyes, CESI School, and Eurecom School. He

has been working on network slicing in the context of H2020 European projects on 5G, including MonB5G and 5GDrones. His research interests also include the Internet of Things (IoT), the IoT in industrial systems, smart grid, and vehicular networks. He also acted or still acts as a reviewer of many IFIP, ACM, and IEEE conferences (ICC, Globecom, PIMRC, WCNC, VTC, IM/NOMS, IWCMC, GIIS, WiMob, and Wireless Days) and journals, such as the IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, the IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, the IEEE TRANSACTIONS ON INDUSTRIAL INFORMATICS, the *IEEE Communication Magazine*, and the *IEEE Network Magazine*.

![](_page_22_Picture_6.jpeg)

**KARIM BOUTIBA** received the engineering degree from the École Nationale Supérieure d'Informatique, Algeria. He is a currently pursuing the Ph.D. degree with the Communication Systems Department, EURECOM, and supervised by Prof. A. Ksentini. During his internship, he has worked on building a RAN Orchestrator on the top of OpenAirInterface platform that manages the lifecycle of a radio network slice. He is working towards enforcing network slicing in the new generation of radio access network.

![](_page_22_Picture_8.jpeg)

**ADLEN KSENTINI** (Senior Member, IEEE) received the Ph.D. degree in computer science from the University of Cergy-Pontoise on QoS provisioning in the IEEE 802.11-based networks. Since 2016, he has been a Professor with the Communication Systems Department, EURECOM. He is currently an IEEE COMSOC Distinguished Lecturer on topics related to 5G and Network Softwarization. His current research topics are in the field of architectural enhancements to mobile core networks, mobile

cloud networking, network functions virtualization, and SDN. He received the Best Paper Award from IEEE WCNC 2018, IEEE IWCMC 2016, IEEE ICC 2012, ACM MSWiM 2005, and the IEEE Fred W. Ellersik Prize for the Best *IEEE Communications Magazine* for 2017.
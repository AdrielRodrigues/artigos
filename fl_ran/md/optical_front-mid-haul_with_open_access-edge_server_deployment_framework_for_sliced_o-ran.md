---
title: "Optical Front/Mid-Haul With Open Access-Edge Server Deployment Framework for Sliced O-RAN"
tema_principal: fl_ran
temas_relacionados: []
ano: 2022
autores: []
veiculo: null
pdf: ../pdf/optical_front-mid-haul_with_open_access-edge_server_deployment_framework_for_sliced_o-ran.pdf
---

# Optical Front/Mid-Haul With Open Access-Edge Server Deployment Framework for Sliced O-RAN

Sourav Mondal<sup>®</sup>, Member, IEEE, and Marco Ruffini<sup>®</sup>, Senior Member, IEEE

Abstract—The fifth-generation of mobile radio technologies is expected to be agile, flexible, and scalable while provisioning ultra-reliable and low-latency communication (uRLLC), enhanced mobile broadband (eMBB), and massive machine type communication (mMTC) applications. An efficient way of implementing these is by adopting cloudification, network function virtualization, and network slicing techniques with open-radio access network (O-RAN) architecture where the baseband processing functions are disaggregated into virtualized radio unit (RU), distributed unit (DU), and centralized unit (CU) over front/mid-haul interfaces. However, cost-efficient solutions are required for designing front/mid-haul interfaces and time-wavelength division multiplexed (TWDM) passive optical network (PON) appears as a potential candidate. Therefore, in this paper, we propose a framework for the optimal placement of RUs based on long-term network statistics and connecting them to open access-edge servers for hosting the corresponding DUs and CUs over front/mid-haul interfaces while satisfying the diverse QoS requirements of uRLLC, eMBB, and mMTC slices. In turn, we formulate a two-stage integer programming problem and time-efficient heuristics for users to RU association and flexible deployment of the corresponding DUs and CUs. We evaluate the O-RAN deployment cost and latency requirements with our TWDM-PON-based framework against urban, rural, and industrial areas and show its efficiency over the optical transport network (OTN)-based framework.

*Index Terms*—Beyond 5G Open-RAN, front/mid-haul network, integer linear programming, network slicing, TWDM-PON.

## I. INTRODUCTION

THE FIFTH-GENERATION (5G) of mobile radio access networks (RANs) envisions to support a diverse set of applications which are classified into three broad categories, i.e., uRLLC, eMBB, and mMTC. Hence, the 5G networks are expected to possess features like flexibility, scalability, manageability, and customizability [1]. In addition to high throughput (peak uplink: 10 Gbps and peak downlink: 20 Gbps), an extremely high user density (~ 10<sup>6</sup> devices/km<sup>2</sup>) is expected from 5G RANs that leads to a dense base station deployment. Therefore, for a diverse and dense RAN deployment, initially, cloud-radio access network (C-RAN)

Manuscript received 14 September 2021; revised 26 January 2022 and 11 April 2022; accepted 5 May 2022. Date of publication 9 May 2022; date of current version 12 October 2022. This work is financially supported by EU H2020 EDGE/MSCA (grant 713567) and Science Foundation Ireland (SFI) grants 17/CDA/4760 and 13/RC/2077\_P2. The associate editor coordinating the review of this article and approving it for publication was K. Xue. (Corresponding author: Sourav Mondal.)

The authors are with the CONNECT Centre for Future Networks and Communication, Trinity College Dublin, University of Dublin, Dublin 2, D02 PN40 Ireland (e-mail: somondal@tcd.ie; marco.ruffini@tcd.ie).

Digital Object Identifier 10.1109/TNSM.2022.3173915

was considered as a potential architecture by the 5G infrastructure public private partnership (5GPPP) because it enables efficient network management and resource sharing in realtime through a centralized architecture [2]. In the C-RAN architecture, the traditional base stations are decoupled into two parts, viz., remote radio heads (RRHs) and base-band units (BBUs). The RRHs are distributed as remote antenna elements, whereas a cluster of BBUs (known as BBU pool) is placed at a centralized location. The RRHs are connected to the BBU pool by front-haul links, typically using the common public radio interface (CPRI) that requires continuous data streaming (split-8) at high throughput with low-latency and low-jitter (< 65 ns) [3]. However, to foster more open and smarter RANs, major mobile network operators across the globe are collaborating within the Open-RAN (O-RAN) Alliance to standardize the O-RAN architecture by adopting dis-aggregated virtual BBU function processing units like RUs, DUs, and CUs (by exploiting software defined everything (SDx) and network function virtualization (NFV) on commercial off-the-shelf (COTS) hardware), which are interconnected by open front/mid-haul interfaces. This architecture relies on programmability, openness, resource sharing, and edgefication to handle complex network management issues through artificial intelligence-based techniques [4].

Another critical issue of the C-RAN architecture is that continuous bit streaming is required in the front-haul links at a very high data rate that does not scale with actual user traffic and mainly depends on RRH configurations [5]. This issue is overcome by using different split options among RUs, DUs, and CUs in O-RAN architecture that enables a flexible and scalable network deployment [6]. Nonetheless, designing the RU-DU (front-haul) interface is still very challenging as it demands high capacity (typically working on split-7.2 but considerably less demanding than the RRH-BBU split-8 CPRI), low-latency, and low-jitter ( $\leq 40 \mu s$ ) links. The DU-CU (midhaul) interface, on the other hand, demands less throughput and can tolerate relatively higher latency. To meet the nextgeneration front-haul interface (NGFI) requirements, OTNs and TWDM-PONs are recommended by ITU-T as their latest standards can support up to 100 Gbps or more aggregated datarate [5]. As the O-RAN allows RUs to lease on-demand DU and CU processing resources, a better operational cost reduction and energy efficiency can be achieved when a large number of RUs can be aggregated to edge cloud nodes. Thus, the concept of using shared PONs to improve flexibility across access and metro [7] and to provide connectivity to edge cloud nodes [8] is gaining momentum. Note that microwave

1932-4537 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

TABLE I ABBREVIATIONS EMPLOYED

| Abbreviation | Meaning or Description                                  |  |  |
|--------------|---------------------------------------------------------|--|--|
| 3GPP         | The 3rd Generation Partnership Project                  |  |  |
| 5GPPP        | The 5G Infrastructure Public Private Partnership        |  |  |
| BBU          | Base-band processing unit                               |  |  |
| CNF          | Containerized network function                          |  |  |
| COTS         | Commercial off-the-shelf                                |  |  |
| CPRI         | Common public radio interface                           |  |  |
| C-RAN        | Cloud-radio access network                              |  |  |
| CU           | Centralized unit                                        |  |  |
| DU           | Decentralized unit                                      |  |  |
| eMBB         | Enhanced mobile broadband                               |  |  |
| FTTx         | Fiber-to-the-home/curb/business/office                  |  |  |
| GOPS         | Giga operations per second                              |  |  |
| ILP          | Integer linear programming                              |  |  |
| ITU-T        | International Telecommunication Union-Telecommunication |  |  |
| M-DBA        | Mobile dynamic bandwidth allocation                     |  |  |
| mMTC         | Massive machine-type communication                      |  |  |
| NFV          | Network function virtualization                         |  |  |
| NGFI         | Next-generation front-haul interface                    |  |  |
| OFDM         | Orthogonal frequency division multiplexing              |  |  |
| OLT          | Optical line terminal                                   |  |  |
| ONU          | Optical network unit                                    |  |  |
| O-RAN        | Open radio access network                               |  |  |
| OTN          | Optical transport network                               |  |  |
| PDCP         | Packet data convergence protocol                        |  |  |
| PON          | Passive optical network                                 |  |  |
| RRC          | Radio resource controller                               |  |  |
| RRH          | Remote radio head                                       |  |  |
| RU           | Radio unit                                              |  |  |
| SDx          | Software defined everything                             |  |  |
| TTI          | Transmission time interval                              |  |  |
| TWDM         | Time and wavelength division multiplexed                |  |  |
| UE           | User equipment                                          |  |  |
| uRLLC        | Ultra-reliable and low-latency communication            |  |  |
| VNF          | Virtualized network function                            |  |  |

and free-space optics can also be used for implementing the front/mid-haul links [\[9\]](#page-16-8), but they fail to provide the same level of capacity and reliability as optical fiber-based OTN and TWDM-PON. Our motivations behind choosing TWDM-PON are its cost efficiency, the possibility of ubiquitous deployment as they are normally used to provide highly-dense FTTx services, and the convenience to scale up network throughput by introducing additional wavelengths. To the best of our knowledge, the design and planning of O-RAN front/mid-haul networks with TWDM-PON and its merits over OTN are not examined so far in the existing literature.

Alongside front/mid-haul network design, integration of edge/cloud servers or processor pools in O-RAN architecture for efficient DU and CU function processing also presents an important research challenge. Over the past decade, the industry, as well as academic research on cloud/edge computing networks, have taken similar momentum as access networks, which created the premise for a confluence of two technologies, viz., *Telecom cloud* and *IT cloud*. Both Telecom network operators and IT cloud providers are interested in controlling the evolution of the Internet at the edge in their favor, which raises the question: *Where is the edge?* [\[10\]](#page-16-9). The network operators are motivated to integrate cloud technologies with access networks for supporting low-latency and high-bandwidth edge applications because they have existing and widely distributed physical network infrastructure. On the contrary, the cloud operators are keen to saturate metro areas with massive edge

node clusters with very simple access networks such that everything can be provided as a service on COTS hardware. Hence, for providing an open market opportunity to any vendor, *access-edge clouds* for *democratizing the network edge for sustained innovation* is proposed [\[10\]](#page-16-9). These open access-edge cloud servers can be used for hosting DU and CU function processing units as well as executing jobs for edge computing applications.

<span id="page-1-2"></span><span id="page-1-1"></span>Recently, *network slicing* was proposed for efficient handling of diverse network resource requirements of uRLLC, eMBB, and mMTC applications [\[11\]](#page-16-10). Through network slicing, different logical networks (i.e., slices) are constructed on a shared physical network via SDx, NFV, and cloud/edge computing technologies. Each slice can be considered as an end-to-end virtualized network instance and is customized in terms of communication, computation, and storage resources to meet the specific service requirements [\[12\]](#page-16-11). For example, the uRLLC applications demand a low throughput but a very stringent one-way latency of 1 ms, the eMBB applications demand a one-way latency of 4 ms but an average user experience throughput of 50 Mbps in uplink and 100 Mbps in the downlink, and the mMTC applications demand a one-way latency of 10 ms but a very high device density. Therefore, optimizing the RAN resources to accommodate different network slices is an essential research challenge.

Note that two primary aspects of the front/mid-haul design for O-RAN are: (a) identification of RU locations based on user distribution, long-term average throughput, and QoS latency requirements of uRLLC, eMBB, and mMTC applications, and (b) optimally connecting the RUs to open accessedge servers that host the DUs and CUs. In the C-RAN design problem, after the users are assigned to RRHs, optimal locations for BBU pool placement over front-haul (only split-8) interfaces are required. Nevertheless, the flexibility in choosing RU-DU-CU split options and front/mid-haul configurations in O-RAN increases the problem complexity several times more than C-RAN. In this paper, we propose a framework for optimal deployment of network slicing enabled TWDM-PON-based NGFI with integrated open access-edge servers that encompass a minimum cost of O-RAN deployment. Our primary contributions are summarized as follows.

- (i) We propose a framework to identify optimal 5G RU, TWDM-PON optical network unit (ONU), and optical line terminal (OLT) locations with a minimum number of access-edge cloud servers to minimize the RAN deployment cost. Thus, we formulate a two-stage integer linear programming (ILP) problem for user equipment (UE) to RU association and flexible placement of corresponding DUs and CUs for uRLLC, eMBB, and mMTC slices.
- <span id="page-1-0"></span>(ii) We compute the global optimal solution of our ILP formulation by commercially available solvers. In addition, we design efficient heuristics for UE to RU association (Lagrangian relaxation based) and connect the corresponding DUs and CUs (greedy approach based). We show that these heuristics can produce near-optimal solutions while ensuring quick convergence with appropriate convergence and optimality gap analysis.

(iii) We evaluate the proposed framework against urban, rural, and industrial scenarios and present a comparative study on deployment cost, front/mid-haul communication and BBU processing latencies for eMBB, uRLLC, and mMTC slices. We also show that our proposed TWDM-PON-based framework is cost-efficient over OTN-based NGFI framework by using the same RU locations.

The rest of this paper is organized as follows. In Section [II,](#page-2-0) we review some recent related works. In Section [III,](#page-2-1) we briefly discuss our proposed open access-edge network architecture and system model. In Section [IV,](#page-5-0) the ILPs are formulated and the corresponding heuristics are designed. In Section [V,](#page-12-0) framework evaluation methods are described and the numerical results are presented. Finally, in Section [VI,](#page-15-0) our primary observations and achievements are summarized.

#### <span id="page-2-4"></span><span id="page-2-2"></span>II. REVIEW OF RELATED WORKS

<span id="page-2-3"></span><span id="page-2-0"></span>The vision of the 5G mobile communication network consists of a major leap in terms of bandwidth, latency, device density, and various other QoS requirements from its predecessors. In the past, the authors of [\[13\]](#page-16-12) proposed a cell planning method for 4G networks that simultaneously satisfies both cell coverage and capacity constraints. Recently, the authors of [\[14\]](#page-16-13) proposed a cell planning framework for dense and heterogeneous 5G networks. The radio resources are orthogonally partitioned among different slices for optimal distribution among cells and allocation to mobile users. Furthermore, the authors of [\[15\]](#page-16-14) proposed 5G mobile network planning framework for urban areas in Ibb city, Yemen, where 28 GHz millimeter-wave base stations are considered. However, these frameworks are unsuitable for the 5G O-RAN architecture. The authors of [\[16\]](#page-16-15), [\[17\]](#page-16-16) provided crucial insights on the front-haul network design for 5G RANs. As the SDx and NFV technologies play a significant role in Beyond 5G networks, new planning, and dimensioning models are required to achieve a cost-optimal design that supports a wide range of applications [\[18\]](#page-16-17). The authors of [\[19\]](#page-16-18) proposed three optimization models to minimize the network load and data center resources by finding the optimal placement of the data centers, SDx, and NFV mobile network functions. The authors of [\[20\]](#page-16-19) studied the containerized network function (CNF) placement and resource allocation problem of O-RAN with three-layer hierarchical data centers. Furthermore, the authors of [\[21\]](#page-16-20) formulated an optimization problem for RU-DU-CU placement and the allocation of front/mid-haul transmission resources over OTN. The authors of [\[22\]](#page-16-21) formulated an optimization problem for routing, wavelength and bandwidth assignment, and processor pool selection for fine-grained BBU function placement over OTN. However, neither of these works designed TWDM-PON-based front/mid-haul networks for 5G O-RANs that provisions flexible placement of DUs and CUs.

<span id="page-2-11"></span><span id="page-2-9"></span><span id="page-2-8"></span>An important feature of O-RAN architectures is flexible functional splits and the authors of [\[23\]](#page-16-22) presented a comprehensive overview of each functional split option with their respective advantages and disadvantages over evolved common

<span id="page-2-12"></span>public radio interface (eCPRI) and we incorporated this feature in our problem formulation as well. Although the bandwidth demand of front-haul interfaces can be met by TWDM-PONs, the existing dynamic bandwidth allocation algorithms (DBA) fail to satisfy the front-haul latency requirements. Thus, the authors of [\[24\]](#page-16-23) proposed a novel cooperative mobile-DBA (M-DBA) algorithm where each OLT receives future uplink scheduling information from the corresponding BBUs and preallocates time-slots by estimating the arrival period to reduce the waiting time of uplink data at the ONUs.

<span id="page-2-16"></span><span id="page-2-15"></span><span id="page-2-14"></span><span id="page-2-13"></span>Recently, for efficient resource management to support a diverse set of eMBB, uRLLC, and mMTC applications, research on RAN slicing, core network slicing, and front/midhaul slicing has started to gain significant attention [\[25\]](#page-16-24). The authors of [\[26\]](#page-17-0) formulated the network-slicing process as a weighted throughput maximization problem that involves sharing of computational resources, fronthaul capacity, physical RRHs, and radio resources. The authors of [\[27\]](#page-17-1) presented a slice-based 5G architecture and "Network Store in a programmable cloud" that efficiently manages network slices through NFV, SDx, and cloud computing. The authors of [\[28\]](#page-17-2) proposed a unified control and network-slicing architecture for a multi-vendor multi-standard PON-based 5G fronthaul network and experimentally demonstrated its flexible resource management and slicing capability. Moreover, they proposed a multi-vendor network-slicing scheme for converged vehicular and fixed access networks in [\[29\]](#page-17-3). The authors of [\[30\]](#page-17-4) proposed a flexible hierarchical edge cloud architecture to enable 5G optical fronthaul network slicing and a network resource management scheme that jointly allocates bandwidth resources to various network slices. Nonetheless, the performance of network slice enabled 5G O-RAN architecture with TWDM-PON-based front/mid-haul interfaces and integrated open access-edge servers demand a thorough investigation.

# <span id="page-2-18"></span><span id="page-2-17"></span><span id="page-2-1"></span>III. OPEN ACCESS-EDGE CLOUD NETWORK DESIGN WITH TWDM-PON-BASED FRONT/MID-HAUL

<span id="page-2-7"></span><span id="page-2-6"></span><span id="page-2-5"></span>In this section, we discuss the fundamental aspects of TWDM-PON-based front/mid-haul interfaces for sliced 5G O-RAN with integrated access-edge cloud servers.

## *A. TWDM-PON-Based Front/Mid-Haul Network Architecture*

<span id="page-2-20"></span><span id="page-2-19"></span><span id="page-2-10"></span>In Fig. [1,](#page-3-0) we show the proposed TWDM-PON-based front/mid-haul interfaces for 5G O-RAN. Most ONUs are connected to 5G macro, micro, and small cell RUs, and groups of ONUs are connected to OLTs via TWDM-PONs. The TWDM-PONs are being considered for supporting small cell connectivity, with solutions capable of providing slice isolation [\[31\]](#page-17-5) and targeting specific service level agreement targets [\[32\]](#page-17-6). If we consider the 3GPP recommended RU-DU split-7.2 and DU-CU split-2, then radio antenna and low physical layer circuitry run on RU hardware. This mainly includes physical layer tasks like IQ decompression, precoding, digital beamforming, inverse Fourier transform, cyclic prefix addition, and digital-to-analog conversion. In some cases, very smallcapacity open access-edge servers may also be placed along

![](_page_3_Figure_2.jpeg)

Fig. 1. The proposed TWDM-PON-based front/mid-haul network architecture for supporting open and intelligent 5G O-RAN (VR/AR: virtual/augmented reality, OLT: optical line terminal, ONU: optical network unit, RU: radio unit, DU: distributed unit, CU: centralized unit).

with RUs that can host DUs for processing high physical layer, MAC, and RLC functions. Usually, medium or largecapacity access-edge cloud servers are placed at OLT locations whose resources can be distributed for hosting DU, CU, and edge computing applications. These functions can be implemented either as virtualized network functions (VNFs) or as CNFs [\[20\]](#page-16-19). The CUs handle upper layer functions, e.g., RRC, PDCP-C, PDCP-U, and SDAP [\[20\]](#page-16-19).

Actually, functional splits can be chosen flexibly for the RU-DU and DU-CU interfaces which incur different latency requirements, e.g., max 0.1 ms for split-7.2 and max 10 ms for split-2 [\[23\]](#page-16-22). With a split-7.2 RU-DU interface, the fronthaul network can span up to 20 km with a 1:64 power-splitter ratio to meet a maximum one-way latency of 100 μsec. On the other hand, split-2 can be chosen for the DU-CU interface and the mid-haul can span up to 80 km to meet a maximum oneway latency of around 1 msec [\[33\]](#page-17-7). Moreover, the throughput requirement of the mid-haul is nearly 10 times less than that of the front-haul, e.g., with 4x4 MIMO, 100 MHz configuration, around 11.1 Gbps is required for split-7.2 front-haul but only 1.11 Gbps is required for split-2 mid-haul. Therefore, multiple Stage-I TWDM-PONs with DUs located at RU or ONU can be further aggregated through a single Stage-II TWDM-PON.

For clarity, please refer to the first example in Fig. [2](#page-3-1) which shows the RU-DU-CU interfaces for uRLLC (max oneway latency = 1 ms) and eMBB applications (max one-way latency = 4 ms) where Stage-I TWDM-PON is sufficient. A small-capacity server is installed at RU locations for processing the DUs of uRLLC applications and Stage-I TWDM-PON carries its mid-haul traffic. This might be costly but efficient

<span id="page-3-0"></span>![](_page_3_Picture_7.jpeg)

Fig. 2. Some example RU, DU, and CU inter-connections over TWDM-PON front/mid-haul for uRLLC, eMBB, and mMTC slices.

<span id="page-3-3"></span><span id="page-3-2"></span><span id="page-3-1"></span>in meeting strict latency requirements. Nonetheless, the DUs and CUs of eMBB applications are processed by servers at Stage-I OLT locations and the Stage-I TWDM-PON carries its front-haul traffic. The second example in Fig. [2](#page-3-1) shows the RU-DU-CU interfaces for mMTC applications (max oneway latency = 10 ms) where both Stage-I and Stage-II TWDM-PONs are used. An *OLT-ONU box* is used to create a sequential connection among Stage-I OLT, server for DU, and Stage-II ONU. To support a large number of mMTC devices and exploit a higher latency bound, this configuration may prove to be cost-efficient. The edge clouds are always placed after the CUs and play a crucial role in instantiating all the dedicated functions of the uRLLC slice. There are several existing works on edge computing server placement [\[34\]](#page-17-8), hence this is

![](_page_4_Figure_2.jpeg)

Fig. 3. The uplink data transmission scheme from UEs to RU, DU, and CU by cooperative M-DBA in TWDM-PON front-haul.

beyond the scope of this paper. In addition, the cellular core functions run on *remote data centers* where network slice management and orchestration are also performed to create and manage the life cycles of network slices. While latency in PON can be an issue in the upstream direction, mechanisms like the cooperative DBA mentioned previously or other solutions that make use of hardware acceleration [35] can substantially reduce this effect.

#### B. Novel Scheduling Techniques for Ensuring Low-Latency

<span id="page-4-5"></span>Ensuring low-latency for uRLLC applications appears to be a critical challenge, but 5G new radio (NR) attempts to solve this by adopting some key techniques, such as frequent data transmission opportunities to minimize waiting time, flexible transmission duration, short UE processing time, short base-band processing time, and grant-free uplink transmission [36]. A numerology-based frame structure is introduced in 5G NR that allows a flexible set of sub-carrier spacing, i.e., 15, 30, 60, 120, 240, 480 kHz. To achieve a shorter transmission time, mini-slots can also be used that contain 2, 4, or 7 OFDM symbols instead of the traditional slot of 14 OFDM symbols [36]. For scheduling high-priority uRLLC traffic, especially in uplink, instant scheduling and grant-free scheduling techniques are used [37]. In instant scheduling, whenever uRLLC traffic arrives, the ongoing eMBB or mMTC traffic is preempted and uRLLC traffic is scheduled. The grantfree scheduling is adopted where uplink resources are reserved for a single UE (periodic traffic) or a group of contending UEs (non-periodic traffic). To avoid collisions, UEs are allowed to transmit multiple replicas of each packet.

The aggregated traffic from a group of UEs accesses the network through RUs, which are connected with ONUs that use TWDM-PON as front-haul, as shown in Fig. 3. Usually, a set of dedicated wavelengths in a TWDM-PON are used for catering to the stringent front-haul traffic requirements. A cooperative M-DBA is used to schedule upstream ONU traffic according to the transmit time interval (TTI) cycles so that as soon as the data from UEs reach RU, it goes to ONU, and then, is directly transmitted to OLT and DU/CU with minimal waiting time [24]. In this protocol, while sending data in a given slot (T), UEs request wireless capacity for a future slot, say (T+A). Accordingly, the DU takes scheduling decisions and notifies each UE about the allocated wireless resources

for the future slot (T+A). In parallel, the DU calculates the corresponding fronthaul traffic load per RU, based on the scheduling allocations for the corresponding UEs. The DU notifies the traffic load per RU for the future slot to the OLT and the OLT generates a bandwidth map for the future slot (T+A) corresponding to the traffic identifier.

#### C. Communication and RU-DU-CU Processing Models

<span id="page-4-0"></span>To propose a TWDM-PON-based O-RAN planning framework, it is important to consider appropriate models for the communication and computation aspects of the network. In this O-RAN front/mid-haul design framework, we formulate an offline optimization problem for the network deployment stage, where we need to find the maximum possible throughput of a 5G NR RU by the following formula [36]:

<span id="page-4-3"></span>
$$W_b = \sum_{p=1}^{N_c} \left( a^{(p)} \nu^{(p)} Q_m^{(p)} f^{(p)} R_{max} \times \frac{12 \times N_{PRB}^{BW(p),\mu}}{T_s^{\mu}} \left( 1 - OH^{(p)} \right) \right), \quad (1)$$

<span id="page-4-4"></span>where, the number of aggregated carriers in a frequency band is denoted by  $N_c$ , the percentage of resources used for uplink/downlink transmissions in the carrier p is denoted by  $a^{(p)}$ , the number of MIMO layers is denoted by  $\nu^{(p)}$ , the modulation order is denoted by  $\nu^{(p)}$ , the capability mismatch between base-band and RF for UEs is denoted by  $\nu^{(p)}$ , the coding rate is denoted by  $\nu^{(p)}$ , the chosen numerology is denoted by  $\nu^{(p)}$ , the average symbol duration in seconds is denoted by  $\nu^{(p)}$ , and the maximum physical resource block (PRB) in the available bandwidth of a single carrier is denoted by  $\nu^{(p)}$ , and  $\nu^{(p)}$  denotes the overhead. However, the downlink throughput of a UE is dependent on the power transmitted by the connected RU and the path loss. We can calculate the throughput of UE- $\nu$  as follows [38]:

<span id="page-4-7"></span><span id="page-4-1"></span>
$$W_u = B \times \log_2 \left( 1 + \frac{P_b \mathcal{L}(d_{ub})}{\sigma^2 + \sum_{b' \neq b} P_{b'} \mathcal{L}(d_{ub'})} \right), \quad (2)$$

<span id="page-4-6"></span>where, B denotes the bandwidth,  $P_b$  denotes the power transmitted by RU-b,  $\sigma^2$  denotes the noise power, and  $\mathcal{L}(d_{ub})$  denotes the path loss in dB. The considered models for path loss of macro and small-cell RUs against a distance d (km) are respectively given by (derived from [39]):

<span id="page-4-8"></span><span id="page-4-2"></span>
$$\mathcal{L}_M(d) = 128.1 + 37.6 \times \log_{10}(d), \tag{3}$$

<span id="page-4-9"></span>
$$\mathcal{L}_S(d) = 37 + 30 \times \log_{10}(d). \tag{4}$$

A similar model can be used for the uplink throughput of the UEs. If we know the maximum throughput requirements of UEs from any slice, then we can find the maximum allowable UE to RU distance of that slice by using (2)-(4). In a network planning problem, we need to consider the long term network statistics, but mobile user throughput requirement shows *spatio-temporal* and *tidal wave characteristics*, i.e., UE density varies over geography and peak throughput demand arises only during certain hours of a day [40]. Therefore, if we consider the maximum throughput of all UEs, then there

will be severe under-utilization of resources at low-throughput hours. Thus, we use the average UE throughput demand by considering a *semi-static service request model*, i.e., each UE requests a constant amount of resources for its desired service over an interval of time [\[20\]](#page-16-19).

<span id="page-5-2"></span>Recently, the IEEE 802.1CM standard was developed for front/mid-haul interfaces [\[41\]](#page-17-15) and is compatible with Ethernetbased TWDM-PON standards. When UEs are attached to RUs, the corresponding DU and CU processing data in the front/mid-haul interfaces are transmitted as periodic bursts of Ethernet frames. Data is transmitted as undivided blocks in the network [\[21\]](#page-16-20). For a burst interval of δ*t* (sec), the number of frames in a burst, denoted by B, can be calculated as B = *R<sup>D</sup>* × δ*<sup>t</sup>* /P, where *R<sup>D</sup>* denotes required data rate and P denotes the payload size of an Ethernet frame (up to 1500 Bytes) [\[16\]](#page-16-15). Hence, the actual throughput of a flow can be calculated by (B × *F*/δ*t*), where *F* is the Ethernet frame size (1542 Bytes, assuming the best case of maximum packet size). The total computational effort for the BBU functions (here BBU indicates the total digital processing across RU, DU, and CU) per TTI in giga operations per second (GOPS) is given by the following expression [\[22\]](#page-16-21):

$$C_{BBU} = \left(3A + A^2 + \frac{1}{3} \times \mathcal{M} \times \Psi \times \mathcal{S}\right) \times \frac{\Phi}{10}, \quad (5)$$

where, A denotes the number of MIMO antennas, M denotes the number of modulation bits, Ψ denotes the coding rate, S denotes the number of MIMO layers, and Φ denotes the number of PRB. We distribute this total computational effort C*BBU* among RU, DU, and CU based on the "PHY split" and "RLC-PDCP split" in [\[6\]](#page-16-5). With the considered split-7.2 (RU-DU) and split-2 (DU-CU), 40% processing is done by RU, 50% processing is done by DU, and 10% processing is done by CU. Note that the RU functions are typically implemented on dedicated hardware rather than on open access-edge servers, and this will be considered in our optimization problem formulation. The total RU-DU-CU function processing time depends on the number of PRBs, the MCS index, and the CPU frequency and can be computed by the polynomial expression provided in [\[42\]](#page-17-16). Accordingly, we can choose a maximum limit for the sum of RU, DU, and CU processing latencies.

# <span id="page-5-3"></span>*D. Optimal TWDM-PON-Based Front/Mid-Haul Design*

In a practical RAN deployment scenario, UEs are randomly distributed across certain geographic areas and can be classified as either of uRLLC, eMBB, and mMTC application users depending on their throughput and latency demands. These UEs require a set of end-to-end resources from RUs, DUs, and CUs. This chain of resources is known as *service function request (SFR)* [\[20\]](#page-16-19). Therefore, to accommodate all SFRs generated from all UEs in the network design and planning stage, firstly we need to identify a set of possible 5G RU locations belonging to uRLLC, eMBB, and mMTC slices over the considered area such that each UE can be connected to one RU only. The RU locations are also the possible locations for the ONUs of Stage-I TWDM-PONs. In addition, we also need to identify a set of locations for OLTs for Stage-I and Stage-II TWDM-PONs and placement locations of open access-edge servers for hosting DUs and CUs. Our objective

<span id="page-5-1"></span>TABLE II ACCESS-EDGE CLOUD NETWORK PARAMETERS AND SETS

| Symbol                                                             | Definition                                                                        |  |  |  |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------|--|--|--|
|                                                                    | Set of all possible network slices                                                |  |  |  |
| $\mathcal{U}_{5G_s}$                                               | Set of 5G NR UEs in slice s                                                       |  |  |  |
| $\overline{\mathcal{B}_s}$                                         | Set of possible 5G RU locations in slice s                                        |  |  |  |
| 0                                                                  | Set of possible OLT locations of Stage-I TWDM-PONs                                |  |  |  |
| $\overline{\mathcal{Q}}$                                           | Set of possible OLT locations of Stage-II TWDM-PONs                               |  |  |  |
| $D_{u_s b_s}$                                                      | Distance between UE- $u_s \in \mathcal{U}_{5G_s}$ and RU- $b_s \in \mathcal{B}_s$ |  |  |  |
| $D_{b_s r_I}$                                                      | Distance between RU- $b_s$ and RN- $r_I$ of Stage-I TWDM-PON                      |  |  |  |
| $D_{r_Io}$                                                         | Distance between RN- $r_I$ and OLT- $o$ of Stage-I TWDM-PON                       |  |  |  |
| $D_{or_{II}}$                                                      | Distance between Stage-I OLT- $o$ and RN- $r_{II}$ of Stage-II TWDM-PON           |  |  |  |
| $D_{r_{II}q}$                                                      | Distance between RN- $r_{II}$ and OLT- $q$ of Stage-II TWDM-PON                   |  |  |  |
| $D_{max}^e$                                                        | Maximum allowable distance of $e \in \{b_s, o, q\}$                               |  |  |  |
| $W_{b_s}$                                                          | Maximum supported throughput of the RU- $b_s$                                     |  |  |  |
| $W_{u_s}$                                                          | Throughput requirement of the UE- $u_s$                                           |  |  |  |
| $R_o$                                                              | Maximum supported throughput of the Stage-I TWDM-PON                              |  |  |  |
| $R_q$                                                              | Maximum supported throughput of the Stage-II TWDM-PON                             |  |  |  |
| $\eta_{b_s,RU}$                                                    | Required computation resources for RU from RU- $b_s$                              |  |  |  |
| $\frac{\eta_{b_s,RU}}{H_{b_s}}$                                    | Maximum available computation resources for RU at RU- $b_s$                       |  |  |  |
| $\Gamma_{b_s,DU}$                                                  | Required computation resources for DU of RU- $b_s$                                |  |  |  |
| $GD_{b_s}$                                                         | Maximum available computation resources for DU at RU- $b_s$                       |  |  |  |
| $GD_o$                                                             | Maximum available computation resources for DU at Stage-I ONU-o                   |  |  |  |
| $\frac{\Gamma_{b_s,CU}}{GC_o}$                                     | Required computation resources for CU of RU- $b_s$                                |  |  |  |
|                                                                    | Maximum available computation resources for CU at Stage-I OLT-o                   |  |  |  |
| $GC_q$                                                             | Maximum available computation resources for CU at Stage-II OLT-q                  |  |  |  |
| $\Delta_s^{OTA}$                                                   | Over-the-air latency requirement of slice-s                                       |  |  |  |
| $\frac{\frac{\Delta_s^{OTA}}{\Delta_s^{BBU}}}{\frac{\delta^{TTI}}$ | Total BBU processing latency requirement of RU- $b_s$                             |  |  |  |
| $\delta^{TTI}$                                                     | Transmit time interval time of the UEs                                            |  |  |  |
| $\delta_{b_so}/\delta_{oq}$                                        | The reduced waiting time for data ONUs at locations $b_s$ and $o$                 |  |  |  |
| $v_c$                                                              | Speed of light in optical fiber $(2 \times 10^8 \text{ m/s})$                     |  |  |  |
| $\overline{}$                                                      | Speed of electromagnetic wave in the air $(3 \times 10^8 \text{ m/s})$            |  |  |  |

is to install a minimum number of 5G RUs, OLTs, and open access-edge servers because this minimizes the overall cost of 5G O-RAN deployment. Nonetheless, we must ensure that the front/mid-haul communication and total RU, DU, and CU processing latencies of the uRLLC, eMBB, and mMTC slices are satisfied.

<span id="page-5-5"></span><span id="page-5-4"></span>Several UE to base station association mechanisms based on dynamic resource requirements exist in literature for heterogeneous wireless networks [\[43\]](#page-17-17), [\[44\]](#page-17-18) as well as C-RAN [\[45\]](#page-17-19), [\[46\]](#page-17-20). However, we are formulating a UE to RU association problem for O-RAN with long-term network statistics. Firstly, we attempt to find an optimal set of RU locations based on the long-term average SFR requirements of UEs, and secondly, these optimal RU locations are used to find a minimum number of TWDM-PON interconnections between ONUs and OLTs. Besides, we want to install a minimum number of open access-edge servers at RU or Stage-I ONU, Stage-I OLT, and Stage-II OLT locations for hosting DUs and CUs. We incorporate flexible DU and CU deployment in our formulation, but the DUs and CUs corresponding to each SFR must be placed at one location only. Although the front/midhaul deployment for the O-RAN problem can be formulated in several possible ways, the primary benefit of this two-stage ILP formulation is that the optimal solution can be evaluated by commercial solvers with a reasonably large dataset. After the ILP formulations, we employ this framework to design TWDM-PON-based front/mid-haul against urban, rural, and industrial scenarios.

# IV. OPTIMIZATION PROBLEM FORMULATIONS

<span id="page-5-0"></span>In this section, firstly, we formulate an ILP for associating mobile users and RUs based on the long-term network statistics of uRLLC, eMBB, and mMTC applications. Once

TABLE III
OPTIMIZATION DECISION VARIABLES

<span id="page-6-0"></span>

| Variable                                                                            | Definition                                                                       |  |  |  |  |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--|--|--|--|
| $\theta_{b_s}$                                                                      | indicates if $RU$ - $b_s$ from slice $s$ are installed (binary)                  |  |  |  |  |
| $x_{u_s b_s}$                                                                       | indicates if a UE- $u_s$ is connected to a RU- $b_s$ (binary)                    |  |  |  |  |
| $\sigma UI$ .                                                                       | indicates the uplink over-the-air latency (non-negative)                         |  |  |  |  |
| $\frac{\mathcal{T}_{u_sb_s}^{DL}}{\mathcal{T}_{u_sb_s}^{DL}}$                       | indicates the downlink over-the-air latency (non-negative)                       |  |  |  |  |
| $\theta_o$                                                                          | indicates if a Stage-I OLT is installed (binary)                                 |  |  |  |  |
| $\theta_q$                                                                          | indicates if a Stage-II OLT is installed (binary)                                |  |  |  |  |
| $y_{b_so}$                                                                          | indicates if RU- $b_s$ is connected to Stage-I OLT- $o$ (binary)                 |  |  |  |  |
| $z_{oq}$                                                                            | indicates if Stage-I OLT-o is connected to Stage-II OLT-q (binary)               |  |  |  |  |
| $\omega_{b_s}^d$                                                                    | indicates if DU of slice $s$ is installed at RU- $b_s$ (binary)                  |  |  |  |  |
| $\frac{\omega_{os}^{s}}{\omega_{os}^{c}}$ $\frac{\omega_{os}^{c}}{\omega_{qs}^{c}}$ | indicates if DU of slice s is installed at Stage-I OLT-o (binary)                |  |  |  |  |
| $\omega_{os}^{c}$                                                                   | indicates if CU of slice $s$ is installed at Stage-I OLT- $o$ (binary)           |  |  |  |  |
| $\omega_{qs}^{c}$                                                                   | indicates if CU of slice $s$ is installed at Stage-II OLT- $q$ (binary)          |  |  |  |  |
| $\beta_{os}$                                                                        | indicates the number of RUs connected to each OLT-o (integer)                    |  |  |  |  |
| $A_{oas}^{c}$                                                                       | linearizes the integer and binary product term $(\beta_{os} \times K_{oqs}^c)$   |  |  |  |  |
| $Z_{oqs}^c$                                                                         | linearizes the integer and binary product term $(\beta_{os} \times L_{oqs}^{c})$ |  |  |  |  |
| $\chi_{b_so}^d$                                                                     | linearizes binary variable product term $(\omega_{b_s}^d \times y_{b_so})$       |  |  |  |  |
| $\Upsilon^d_{b_so}$                                                                 | linearizes binary variable product term $(\omega_{os}^d \times y_{b_so})$        |  |  |  |  |
| $K_{oqs}^c$                                                                         | linearizes binary variable product term $(\omega_{os}^c \times z_{oq})$          |  |  |  |  |
| $L_{oqs}^c$                                                                         | linearizes binary variable product term $(\omega_{oqs}^c \times z_{oq})$         |  |  |  |  |
| $\mathcal{T}^{UL}_{b_so}$                                                           | indicates the uplink Stage-I TWDM-PON latency (non-negative)                     |  |  |  |  |
| $\frac{\mathcal{T}_{b_so}^{OL}}{\mathcal{T}_{b_so}^{DL}}$ $\mathcal{T}_{cos}^{UL}$  | indicates the downlink Stage-I TWDM-PON latency (non-negative)                   |  |  |  |  |
| $\frac{\mathcal{T}_{oq}^{UL}}{\mathcal{T}^{DL}}$                                    | indicates the uplink Stage-II TWDM-PON latency (non-negative)                    |  |  |  |  |
| $\mathcal{T}_{oq}^{DL}$                                                             | indicates the downlink Stage-II TWDM-PON latency (non-negative)                  |  |  |  |  |
| $\frac{r_{oq}}{\mathcal{T}_{rdc}^{UL}}$                                             | indicates the uplink BBU processing latency (non-negative)                       |  |  |  |  |
| $\mathcal{T}^{DL}_{rdc}$                                                            | indicates the downlink BBU processing latency (non-negative)                     |  |  |  |  |

all the optimal RU locations for different slices are known, we formulate a second ILP to find the optimal TWDM-PON-based front/mid-haul links and placement locations of open access-edge servers to host the respective DUs and CUs.

#### A. Mobile User Equipment and RU Association Problem

We consider that the mobile UEs can be sliced into S sets according to their QoS throughput and latency requirements. Let  $\mathcal{U}_{5G_s} = \{1,2,\ldots,U_s\}$  denote the set of 5G NR UEs in slice  $s \in \mathcal{S} = \{1,2,\ldots,S\}$ , where  $U_s$  denotes the maximum number of UEs in slice s. The average uplink and downlink throughput demands of each UE- $u_s \in \mathcal{U}_{5G_s}$  over its daily active hours are denoted by  $W^{UL}_{u_s}$  and  $W^{DL}_{u_s}$ , respectively. Furthermore,  $\mathcal{B}_s = \{1,2,\ldots,\mathcal{B}_s\}$  denotes the set of possible 5G RU locations corresponding to slice s. The maximum uplink and downlink throughput supported by each RU- $b_s \in \mathcal{B}_s$  are denoted by  $W^{UL}_{b_s}$  and  $W^{DL}_{b_s}$ , respectively. Nonetheless, RUs from all slices will cover the total area so that UEs from all slices can be randomly distributed all over the area. The distance between UE- $u_s$  and 5G RU- $u_s$  are denoted by  $u_s$  and the maximum allowable UE-RU distance for slice s is denoted by  $u_s$ . Note that all the considered network parameters are described in Table III and the decision variables are defined in Table III.

Objective: We consider binary variables  $\theta_{b_s}$  to indicate if every 5G RU- $b_s$  from slice s are installed. We also consider binary variables  $x_{u_sb_s}$  to indicate if a UE- $u_s$  is connected to a RU- $u_s$  RU- $u_s$  from slice  $u_s$  As we want to install minimum number of RUs, the objective is given as:

<span id="page-6-2"></span>
$$\mathcal{P}_1: \min_{\boldsymbol{\theta}_b, \boldsymbol{x}} \quad \alpha \sum_s \sum_{b_s} \theta_{b_s} + \beta \sum_s \sum_{b_s} \sum_{u_s} \left( \mathcal{T}^{UL}_{u_s b_s} + \mathcal{T}^{DL}_{u_s b_s} \right),$$

where,  $\mathcal{T}^{UL}_{u_sb_s}$  and  $\mathcal{T}^{DL}_{u_sb_s}$  represent the uplink and downlink over-the-air (OTA) latencies,  $\alpha=1/(\sum_s B_s)$  unit and  $\beta=1/(\sum_s U_s)$  unit/sec are weight factors to impose a very low importance on latency than the number of RUs as  $\alpha\gg\beta$ . Although the OTA latency upper bound is guaranteed in (10)-(11), we are adding the sum of latencies in (6) for efficiently designing a Lagrangian relaxation-based heuristic. Nonetheless, a problem formulation without the second term in the objective should also produce the same optimal solution.

Connectivity constraints: The binary variables  $x_{u_sb_s}$  variables can take value 1 only if UE- $u_s$  is within the coverage distance of RU- $b_s$  as follows:

<span id="page-6-5"></span>
$$x_{u_s b_s} \le \left\lfloor \frac{D_{b_s}^{max}}{D_{u_s b_s}} \right\rfloor, \ \forall s \in \mathcal{S}, u_s \in \mathcal{U}_{5G_s}, b_s \in \mathcal{B}_s.$$
 (7)

We can determine the maximum allowed distance  $D_{b_s}^{max}$  for each slice  $s \in \mathcal{S}$  by using the maximum throughput, transmit power, and noise power (-174 dBm/Hz) in (2)-(4). Each UE- $u_s$  can be associated with an RU- $b_s$  only if it is installed, which is ensured as follows:

<span id="page-6-4"></span>
$$\theta_{b_s} \ge x_{u_s b_s}, \forall s \in \mathcal{S}, u_s \in \mathcal{U}_{5G_s}, b_s \in \mathcal{B}_s.$$
 (8)

Moreover, each UE- $u_s$  accesses the RAN through some RU- $b_s$  and we consider that each UE is associated with only one RU. This is guaranteed by the following constraint:

<span id="page-6-3"></span>
$$\sum_{b_s \in \mathcal{B}_s} x_{u_s b_s} = 1, \forall s \in \mathcal{S}, u_s \in \mathcal{U}_{5G_s}. \tag{9}$$

Latency constraints: In this work, we consider both the uplink and downlink throughput demands while UE to RU association. Thus, a group of UEs can be associated with a RU only when the uplink and downlink OTA latency bound  $(\Delta_s^{OTA})$  of the corresponding slice s can be supported by that RU- $b_s$  while transmitting the data generated in each TTI duration  $(\delta^{TTI})$ . To ensure this, we introduce the following constraints  $\forall s \in \mathcal{S}, u_s \in \mathcal{U}_{5G_s}, b_s \in \mathcal{B}_s$ :

<span id="page-6-1"></span>
$$\mathcal{T}_{u_{s}b_{s}}^{UL} = \left\{ \frac{x_{u_{s}b_{s}}D_{u_{s}b_{s}}}{c} \right\} + \left\{ \frac{\sum_{u_{s}} x_{u_{s}b_{s}} W_{u_{s}}^{UL} \delta^{TTI}}{W_{b_{s}}^{UL}} \right\} \\
\leq \Delta_{s}^{OTA}, \tag{10}$$

$$\mathcal{T}_{u_{s}b_{s}}^{DL} = \left\{ \frac{x_{u_{s}b_{s}}D_{u_{s}b_{s}}}{c} \right\} + \left\{ \frac{\sum_{u_{s}} x_{u_{s}b_{s}} W_{u_{s}}^{DL} \delta^{TTI}}{W_{b_{s}}^{DL}} \right\} \\
\leq \Delta_{s}^{OTA}, \tag{11}$$

where, the first terms of (10)-(11) denote the wireless signal propagation latency and the second terms denote the data transmission latency in each TTI. The maximum available uplink and downlink throughput of each  $RU-b_s$  can be determined from (1) and these constraints implicitly ensure that the throughput requirements of all the UEs are not more than the total available wireless throughput. Clearly, the aboveformulated optimization problem is an ILP with a linear objective function and linear constraints.

#### B. Lagrangian Relaxation Heuristic for UE-RU Association

<span id="page-6-6"></span>As the locations of the RUs are unknown, the problem of associating UEs to RUs is an NP-hard problem [47]. A

general observation was made around the 1970s that many hard integer programming problems can be considered as easy problems but are complicated by a small set of side constraints. Since then, *Lagrangian relaxation* has gained popularity as the best existing algorithm for problems of this type [48]. Thus, to solve the UE to RU association problem, we design a Lagrangian heuristic algorithm by relaxing constraints (9). This Lagrangian relaxation problem is summarized as:

<span id="page-7-1"></span>
$$\mathcal{R}_{1} \colon \max_{\mathbf{v}} \min_{\boldsymbol{\theta}_{b}, \mathbf{x}} \ \alpha \sum_{s} \sum_{b_{s}} \theta_{b_{s}} + \beta \sum_{s} \sum_{b_{s}} \sum_{u_{s}} \left( \mathcal{T}_{u_{s}b_{s}}^{UL} + \mathcal{T}_{u_{s}b_{s}}^{DL} \right)$$

$$+ \sum_{s} \sum_{u_{s}} \nu_{u_{s}} \left( 1 - \sum_{b_{s}} x_{u_{s}b_{s}} \right)$$
subject to  $(7), (8), (10), (11),$ 

$$\theta_{b_{s}} \in \{0, 1\}, \forall s \in \mathcal{S}, b_{s} \in \mathcal{B}_{s},$$

$$x_{u_{s}b_{s}} \in \{0, 1\}, \forall s \in \mathcal{S}, u_{s} \in \mathcal{U}_{5G_{s}}, b_{s} \in \mathcal{B}_{s},$$

$$(12)$$

where,  $\nu_{u_s}$  are Lagrange multipliers used for relaxing constraints (9). For fixed values of these multipliers, the relaxed problem  $\mathcal{R}_1$  will yield an optimal value of the objective that serves as a *lower bound (LB)* of the original problem  $\mathcal{P}_1$ .

<span id="page-7-0"></span>Proposition 1: The solutions of the Lagrangian relaxation problem  $\mathcal{R}_1$  with given  $\nu_{u_s}$  are given by:

$$x_{u_{s}b_{s}} = \begin{cases} 1, \text{ if } \left\{ \frac{2\beta D_{u_{s}b_{s}}}{c} + \frac{\beta U_{s}W_{u_{s}}^{UL}\delta^{TTI}}{W_{bs}^{UL}} + \frac{\beta U_{s}W_{u_{s}}^{DL}\delta^{TTI}}{W_{bs}^{DL}} - \nu_{u_{s}} \right\} < 0 \text{ and } \theta_{b_{s}} = 1, \\ 0, \text{ otherwise,} \end{cases}$$

$$\theta_{b_{s}} = \begin{cases} 1, \text{ if } \alpha + \sum_{u_{s}} \min \left\{ 0, \frac{2\beta D_{u_{s}b_{s}}}{c} + \frac{\beta U_{s}W_{u_{s}}^{UL}\delta^{TTI}}{W_{b_{s}}^{UL}} + \frac{\beta U_{s}W_{u_{s}}^{DL}\delta^{TTI}}{W_{b_{s}}^{DL}} - \nu_{u_{s}} \right\} < 0, \\ 0, \text{ otherwise.} \end{cases}$$

Proof: For given values of Lagrange multipliers  $\nu_{u_s} \forall s$ , we can minimize the objective function by preferably choosing  $x_{u_sb_s}=1$ , if the corresponding coefficient is  $\{\frac{2\beta D_{u_sb_s}}{c}+\frac{\beta U_sW_{u_s}^{UL}\delta^{TTI}}{W_{b_s}^{UL}}+\frac{\beta U_sW_{u_s}^{UL}\delta^{TTI}}{W_{b_s}^{DL}}-\nu_{u_s}\}<0$ . Otherwise, it is best to set  $x_{u_sb_s}=0$  [48]. Note that the weight factor  $\beta=1/(\sum_s U_s)$ . However, setting  $x_{u_sb_s}=1$  implies that we must also set  $\theta_{b_s}=1$  according to constraint (8), i.e.,  $\theta_{b_s}\geq x_{u_sb_s}, \forall s\in\mathcal{S}, u_s\in\mathcal{U}_{5G_s}, b_s\in\mathcal{B}_s$ . Now, if we set  $\theta_{b_s}=1$ , then we add an excess value of  $\Delta f=\alpha+\sum_{u_s}\min\{0,\frac{2\beta D_{u_sb_s}}{c}+\frac{\beta U_sW_{u_s}^{UL}\delta^{TTI}}{W_{b_s}^{UL}}+\frac{\beta U_sW_{u_s}^{UL}\delta^{TTI}}{W_{b_s}^{UL}}-\nu_{u_s}\}$  to the objective value. If only  $\Delta f$  is negative, the objective value is reduced. Hence, we set  $\theta_{b_s}=1$  when  $\Delta f<0$ .

An optimal solution for the problem  $\mathcal{R}_1$  can be obtained by exploiting Proposition 1. However, it acts only as an LB of the problem  $\mathcal{P}_1$ , denoted by  $\mathcal{P}_{lb}$ , and may not be feasible because (9) is relaxed. Hence, we want to find a feasible solution that acts as the *upper bound (UB)* for  $\mathcal{P}_1$ . Nonetheless, a feasible solution may not always guarantee optimality [48]. Therefore, we need to explore other feasible solutions whose performance are not worse than the best-known UB. To obtain a UB, denoted as  $\mathcal{P}_{ub}$ , we formulate the following problem:

<span id="page-7-2"></span>
$$\mathcal{R}_{2}: \min_{\boldsymbol{\theta}_{b}, \boldsymbol{x}} \sum_{s} \sum_{b_{s}} \boldsymbol{\theta}_{b_{s}} + \sum_{s} \sum_{b_{s}} \sum_{u_{s}} \left( \mathcal{T}_{u_{s}b_{s}}^{UL} + \mathcal{T}_{u_{s}b_{s}}^{DL} - 2\Delta_{s}^{OTA} \right)$$
subject to  $(7), (8), (9), (13), (14).$  (15)

<span id="page-7-5"></span>In  $\mathcal{R}_2$ , the coupling constraint (8) and the integrality constraints (13)-(14) are not relaxed. Note that the latency term is modified to  $\beta \sum_s \sum_{b_s} \sum_{u_s} (\mathcal{T}^{UL}_{u_sb_s} + \mathcal{T}^{DL}_{u_sb_s} - 2\Delta_s^{OTA})$  in the objective, which is equivalent to relaxing (10)-(11). Now, we design a heuristic for  $\mathcal{R}_2$  to check the feasibility of solution from  $\mathcal{R}_1$ . We define a term  $\Delta w_{u_s} = (\mathcal{T}^{UL}_{u_sb_s'} + \mathcal{T}^{DL}_{u_sb_s'}) - (\mathcal{T}^{UL}_{u_sb_s} + \mathcal{T}^{DL}_{u_sb_s})$ , where  $b_s'$  is the initially assigned RU of UE- $u_s$  and  $u_s$  is the re-assigned RU of UE- $u_s$ . We want to associated each UE- $u_s$  to only one RU- $u_s$  such that  $u_s$  is maximized subject to (7), because this minimizes the objective (15). We use  $u_s$  from  $u_s$  but if a UE could not be attached to any RU, then we declare the problem as infeasible. The Lagrangian relaxation method for UE-RU association is summarized in Algorithm 1.

The original problem  $\mathcal{P}_1$  always considers the UB as its best objective value because the UB can guarantee a feasible solution. Nonetheless, different values of Lagrange multipliers can produce different UBs and LBs. Thus, we iteratively adjust the values of  $\nu_{u_s}$  using the *sub-gradient method* [49] and terminate when the UB and LB are close to each other or the maximum number of iterations  $(n_{max})$  is reached. The values of  $\nu_{u_s}$  are updated as follows:

<span id="page-7-4"></span>
$$\nu_{u_s}^{(n+1)} = \nu_{u_s}^{(n)} + \sigma_s^{(n)} \left( 1 - \sum_{b_s} x_{u_s b_s}^{(n)} \right), \forall s \in \mathcal{S}, u_s \in \mathcal{U}_{5G_s},$$
(16)

where,  $\sigma_s^{(n)}$  is the step size at the *n*-th iteration, given by:

<span id="page-7-6"></span><span id="page-7-3"></span>
$$\sigma_s^{(n)} = \frac{\lambda^{(n)} \left( \mathcal{P}_{opt} - \mathcal{P}_{lb}^{(n)} \right)}{\sum_{u_s} \left( 1 - \sum_{b_s} x_{u_s b_s} \right)^2}, \ \forall s \in \mathcal{S}, \tag{17}$$

with  $\lambda^{(n)}$  as a decreasing scalar parameter and  $\mathcal{P}_{opt}$  denotes the best-known solution or UB from previous iterations. Commonly  $\lambda^{(n)}$  is chosen as a constant satisfying  $0 < \lambda^{(n)} \le 2$  and then halved if  $\mathcal{P}_{lb}^{(n)}$  remains constant for several iterations. However, as there is no well-known stopping criteria of this method, the Algorithm 1 needs to be stopped after a finite number iterations  $(n_{max})$  and there may be an optimality gap.

Theorem 1: The optimality gap in the solution for  $\mathcal{P}_1$  produced by the Algorithm 1 tends to zero when the number of iterations  $n \to \infty$ .

<span id="page-7-7"></span>*Proof:* From the properties of Lagrangian relaxation [50], we can state that if for some Lagrangian multiplier vector  $\mathbf{v}$ , the solutions  $\theta_{b_s}^*, x_{u_sb_s}^*$  from  $\mathcal{R}_1$  is feasible in the optimization problem  $\mathcal{P}_1$ , then  $\theta_{b_s}^*, x_{u_sb_s}^*$  is an optimal solution for  $\mathcal{P}_1$ . A feasibility certificate can be obtained from the solution of  $\mathcal{R}_2$ . However, as sub-gradient method is used to evaluate  $\mathcal{R}_1$  and is terminated after a finite number of iterations, there may be

<span id="page-8-0"></span>

```
Algorithm 1 Heuristic Algorithm for UE-RU Assignment Input: \mathcal{S}, \mathcal{U}_{5G_s}, \mathcal{B}_s, D_{b_s}^{max}, D_{u_sb_s}, W_{u_s}^{DL}, W_{u_s}^{UL}, W_{b_s}^{DL},
          Output: Near-optimal solution: x_{u_sb_s}^*, \theta_{b_s}^*, and \mathcal{P}_{opt}^*. Initialize: \nu_{u_s} = 0, x_{u_sb_s} = 0, \theta_{b_s} = 0, \mathcal{P}_{lb} = 0, \mathcal{P}_{ub} = +\infty, \mathcal{P}_{opt} = +\infty, n = 1, feasible = 1.
   1: while \mathcal{P}_{lb}^{(n)} \neq \mathcal{P}_{ub}^{(n)} and n < n_{max} do
2: | Find a LB solution x_{u_sb_s}^{lb} and \theta_{b_s}^{lb} by solving \mathcal{R}_1 using
                     Calculate the LB objective value \mathcal{P}_{lb}^{(n)};
   3:
                    \theta_{b_s}^{ub} \leftarrow \theta_{b_s}^{lb}, \forall s \in \mathcal{S}, b_s \in \mathcal{B}_s;
    4:
                    \begin{array}{ll} \boldsymbol{\sigma}_{b_s} \leftarrow \boldsymbol{\sigma}_{b_s}, \forall s \in \mathcal{S}, \boldsymbol{\sigma}_s \in \mathcal{B}_s, \\ \text{for Each UE-} \boldsymbol{u}_s, \forall s \in \mathcal{S} \text{ do} & \rhd \textit{heuristic for $\mathcal{R}_2$} \\ & \text{Find a set } \{b_s|\boldsymbol{\theta}_{b_s}^{ub} = 1, D_{u_sb_s} \leq D_{b_s}^{max}, \mathcal{T}_{u_sb_s}^{UL} \leq \Delta_s^{OTA}, \\ & \mathcal{T}_{u_sb_s}^{DL} \leq \Delta_s^{OTA}\}; \\ & \text{if } |\{b_s\}| = 0 \text{ then} \end{array}
    5:
    6:
   7:
                                        feasible \leftarrow 0 \text{ and } \mathcal{P}_{ub}^{(n)} \leftarrow +\infty;
    8:
   9:
                               else if |\{b_s\}| = 1 then
10:
                                        Assign UE-u_s to RU-b_s;
11:
                               \begin{vmatrix} x_{u_s}^{ub} & \leftarrow 1; \\ \text{else if } |\{b_s\}| > 1 \text{ then} \end{vmatrix}
12:
13:
                                        Find RU-b_s = \arg \max_{b_s} \{\Delta w_{u_s}\} for UE-u_s;
14:
15:
                                       x_{u_s b_s}^{ub} \leftarrow 1;
16:
17:
                     end for
                    if feasible = 0 then
18:
19:
                           return Infeasible;
20:
                    Calculate the UB objective value \mathcal{P}_{ub}^{(n)}:
21:
                  if \mathcal{P}_{ub}^{(n)} < \mathcal{P}_{opt} then \triangleright Update if x_{u_sb_s} \leftarrow x_{u_sb_s}^{ub}, \forall s \in \mathcal{S}, u_s \in \mathcal{U}_{5G_s}, b_s \in \mathcal{B}_s; \theta_{b_s} \leftarrow \theta_{b_s}^{ub}, \forall s \in \mathcal{S}, b_s \in \mathcal{B}_s; \mathcal{P}_{opt} \leftarrow \mathcal{P}_{ub}^{(n)};
                                                                                                                                ▷ Update if UB is better
22:
23:
24:
25:
26:
27:
                     Update step size \sigma_s according to (17);
28:
                    Update Lagrangian multipliers \nu_{u_s} by (16);
29:
                    n \leftarrow n + 1
30: end while
31: return x_{u_s b_s}, \theta_{b_s}, and \mathcal{P}_{opt};
```

an optimality gap between the true optimal solution  $\mathcal{P}_{opt}^*$  and  $\mathcal{P}_{lb}^{(n)}$ . Note that, with our chosen step-size (17), we ensure that  $[\lambda^{(n)}(\mathcal{P}_{opt} - \mathcal{P}_{lh}^{(n)})] \ge 0, \lim_{n \to \infty} [\lambda^{(n)}(\mathcal{P}_{opt} - \mathcal{P}_{lh}^{(n)})] = 0,$ and  $\sum_{n=1}^{\infty} [\lambda^{(n)} (\mathcal{P}_{opt} - \mathcal{P}_{lb}^{(n)})] = \infty$ . Now, the optimality gap in the solution produced by the sub-gradient method after  $n = n_{max}$  (finite) iterations is given by [49]:

$$\left| \mathcal{P}_{opt}^* - \mathcal{P}_{lb}^{(n)} \right| \le \frac{R^2 + \sum_{n=1}^{n_{max}} \left[ \lambda^{(n)} \left( \mathcal{P}_{opt} - \mathcal{P}_{lb}^{(n)} \right) \right]^2}{(2/G) \sum_{n=1}^{n_{max}} \left[ \lambda^{(n)} \left( \mathcal{P}_{opt} - \mathcal{P}_{lb}^{(n)} \right) \right]}, (18)$$

where,  $\|x_{u_sb_s}^{(1)} - x_{u_sb_s}^*\| \le R$  and  $\sum_{u_s} (1 - \sum_{b_s} x_{u_sb_s})^2 \le G$ . Thus, we can choose R = 1 and  $G = U_s$  for  $\mathcal{P}_1$  to show the optimality gap in the solution produced by Algorithm 1 as:

$$\left| \mathcal{P}_{opt}^* - \mathcal{P}_{lb}^{(n)} \right| \le \frac{1 + \sum_{n=1}^{n_{max}} \left[ \lambda^{(n)} \left( \mathcal{P}_{opt} - \mathcal{P}_{lb}^{(n)} \right) \right]^2}{(2/U_s) \sum_{n=1}^{n_{max}} \left[ \lambda^{(n)} \left( \mathcal{P}_{opt} - \mathcal{P}_{lb}^{(n)} \right) \right]}.$$
(19)

Clearly, under the aforementioned conditions, the optimality gap  $|\mathcal{P}_{ont}^* - \mathcal{P}_{lh}^{(n)}| \to 0$  as  $n \to \infty$ .

After initialization of the Lagrangian multipliers, LB and the optimal values, lines 2-29 iteratively change the Lagrangian multipliers as well as update the LB and UB to find the optimal value  $\mathcal{P}_{opt}$ . In each iteration, the LB is evaluated by lines 2-3 with a complexity of  $O(\sum_s U_s B_s)$  and the UB is evaluated by lines 5-21 with a complexity of  $O(\sum_s U_s B_s)$ . Updating Lagrangian multipliers in lines 22-29 involves a complexity of  $O(\sum_s U_s)$ . Therefore, the convergence rate of Algorithm 1 with an optimality gap of  $|\mathcal{P}_{opt}^* - \mathcal{P}_{lb}^{(n)}|$  is  $O(n_{max}(\sum_s U_s B_s))$  as  $n_{max}$  is the maximum number of iterations. Note that, in general Algorithm 1 can achieve a desired accuracy  $|\mathcal{P}_{opt}^* - \mathcal{P}_{lb}^{(n)}| \leq \epsilon$  with a convergence rate of  $O(1/\epsilon^2)$  [49].

### C. DU-CU Placement and Front/Mid-Haul Design Problem

We denote the set of Stage-I OLTs by  $\mathcal{O} = \{1, 2, \dots, O\}$ and the set of Stage-II OLTs by  $Q = \{1, 2, \dots, q\}$ . The RUs are connected to the Stage-I OLTs through a remote node (RN) where the power splitter is located. Similarly, the Stage-II OLTs are also connected to Stage-I OLTs through an RN. We denote the distances between RUs and Stage-I RNs by  $D_{b_s r_I}$ , the distances between Stage-I RNs and OLTs by  $D_{r_Io}$ , the distances between Stage-I OLTs and Stage-II RNs by  $D_{or_{II}}$ , and the distances between Stage-II RNs and ONUs by  $D_{r_{II}q}$ .

Objective: We use binary variables  $\theta_o$  and  $\theta_q$  to indicate if a Stage-I OLT and a Stage-II OLT are installed, respectively. The cost of installing a Stage-I ONU and a Stage-II ONU are denoted by  $C_o$  and  $C_q$ . Moreover, we use the binary variables  $y_{b_so}$  to denote if RU- $b_s$  is connected to Stage-I OLT-oand the binary variables  $z_{oq}$  to denote if Stage-I OLT-o is connected to Stage-II OLT-q. The cost of optical fiber and installation per km is denoted by  $C_f$ . Furthermore, we use the binary variables  $\omega_{b_s}^d$  and  $\omega_{os}^d$  to indicate if DU of slice s is installed at RU- $b_s$  and Stage-I OLT-o locations, and the binary variables  $\omega^c_{os}$  and  $\omega^c_{qs}$  to indicate if CU of slice s is installed at Stage-I OLT-o and Stage-II OLT-q locations. The DUs and CUs can be placed only if the corresponding node is installed, i.e.,  $\omega_{os}^d \leq \theta_o, \, \omega_{os}^c \leq \theta_o, \forall s \in \mathcal{S}, o \in \mathcal{O}$  and  $\omega_{qs}^c \leq \theta_q, \forall s \in \mathcal{S}, q \in \mathcal{Q}.$  The cost of installation of RU processors, open access-edge servers at Stage-I OLT and Stage-II OLT locations are proportional to the maximum available GOPS/TTI, i.e.,  $G_{b_s}$ ,  $G_o$ ,  $G_q$ , and  $C_q$  denotes cost/GOPS/TTI. The objective to minimize the network installation cost is given as follows:

<span id="page-8-1"></span>
$$\mathcal{P}_{2}: \min_{\boldsymbol{\theta}_{o},\boldsymbol{\theta}_{q},\boldsymbol{y},\boldsymbol{z}} \left\{ \sum_{o \in \mathcal{O}} \left( C_{o}\theta_{o} + C_{f}\rho_{o} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{s \in \mathcal{S}} \sum_{b_{s} \in \mathcal{B}_{s}} C_{g} G_{b_{s}} \omega_{b_{s}}^{d} + \sum_{o \in \mathcal{O}} C_{g} G_{o}\theta_{o} + \sum_{q \in \mathcal{Q}} C_{g} G_{q}\theta_{q} \right\},$$

$$\left\{ \sum_{o \in \mathcal{O}} \left( C_{q}\theta_{o} + C_{f}\rho_{o} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left( C_{q}\theta_{q} + C_{f}\rho_{q} \right) + \sum_{q \in \mathcal{Q}} \left($$

where, the length of optical fibers associated with Stage-I and Stage-II TWDM-PONs are given by:

$$\rho_o = D_{r_I o} + \sum_{s \in \mathcal{S}} \sum_{b_s \in \mathcal{B}_s} y_{b_s o} D_{b_s r_I}, \forall o \in \mathcal{O}, \qquad (21)$$

$$\rho_q = D_{r_{II} q} + \sum_{o \in \mathcal{O}} z_{oq} D_{or_{II}}, \forall q \in \mathcal{Q}.$$
 (22)

Connectivity constraints: The binary variable  $y_{b_so}$  indicate if RU- $b_s$  is attached to Stage-I OLT-o and the binary variable  $z_{oq}$  indicate if Stage-I OLT-o is attached to Stage-II OLT-q. However, their intermediate distances must not be greater than the maximum length of the TWDM-PON ( $\sim$  20 km):

$$y_{b_s o} \le \left\lfloor \frac{D_o^{max}}{D_{b_s r_I} + D_{r_I o}} \right\rfloor, \forall s \in \mathcal{S}, b_s \in \mathcal{B}_s, o \in \mathcal{O},$$
 (23)

$$z_{oq} \le \left\lfloor \frac{D_q^{max}}{D_{or_{II}} + D_{r_{II}} q} \right\rfloor, \forall o \in \mathcal{O}, q \in \mathcal{Q}.$$
 (24)

Moreover, we can connect an RU- $b_s$  to a Stage-I OLT-o only if it is installed. Similarly, we can connect a Stage-I OLT-o to a Stage-II OLT-q only if it is installed. These conditions are ensured by the following constraints:

$$\theta_o \ge y_{b_s o}, \forall s \in \mathcal{S}, b_s \in \mathcal{B}_s, o \in \mathcal{O},$$
 (25)

$$\theta_q \ge z_{oq}, \forall o \in \mathcal{O}, q \in \mathcal{Q}.$$
 (26)

In addition, we must ensure that each  $RU-b_s$  is connected to only one Stage-I OLT-o and each installed Stage-I OLT-o is connected to only one Stage-II OLT-q if required.

$$\sum_{o \in \mathcal{O}} y_{b_s o} = 1, \forall s \in \mathcal{S}, b_s \in \mathcal{B}_s, \tag{27}$$

$$\theta_q \le \sum_{g \in \mathcal{Q}} z_{oq} \le \theta_o, \forall o \in \mathcal{O}, q \in \mathcal{Q}.$$
 (28)

Furthermore, we ensure that DUs and CUs corresponding to each RU- $b_s$  are placed at one location only.

$$\omega_{b_s}^d + \sum_{o \in \mathcal{O}} \omega_{b_s o}^d = 1, \forall s \in \mathcal{S}, b_s \in \mathcal{B}_s, \tag{29}$$

$$\omega_{os}^{c} + \sum_{q \in \mathcal{Q}} \omega_{oqs}^{c} = \theta_{o}, \forall s \in \mathcal{S}, o \in \mathcal{O}.$$
 (30)

Linearization constraints: As we attempt to establish a chain of connections among RUs, DUs, and CUs, a set of binary variable product terms arise. Thus, we introduce a set of binary variables  $\chi^d_{b_so}$ ,  $\Upsilon^d_{b_so}$ ,  $K^c_{oqs}$ , and  $L^c_{oqs}$  for linearizing the binary variable product terms  $(\omega^d_{b_s}y_{b_so})$ ,  $(\omega^d_{os}y_{b_so})$ ,  $(\omega^c_{os}z_{oq})$ , and  $(\omega^c_{oqs}z_{oq})$ , and the corresponding constraints are:

$$\left(1 - \chi_{b_s o}^d\right) \le \left(1 - \omega_{b_s}^d\right) + \left(1 - y_{b_s o}\right),$$

$$\forall s \in \mathcal{S}, b_s \in \mathcal{B}_s, o \in \mathcal{O}, \qquad (31)$$

$$\left(1 - \Upsilon_{b_{s}o}^{d}\right) \leq \left(1 - \omega_{b_{s}o}^{d}\right) + \left(1 - y_{b_{s}o}\right), 
\forall s \in \mathcal{S}, b_{s} \in \mathcal{B}_{s}, o \in \mathcal{O},$$
(32)

$$(1 - K_{oqs}^c) \le (1 - \omega_{os}^c) + (1 - z_{oq}),$$

$$\forall s \in \mathcal{S}, o \in \mathcal{O}, a \in \mathcal{O}. \tag{33}$$

$$(1 - L_{oqs}^c) \le (1 - \omega_{oqs}^c) + (1 - z_{oq}),$$

$$\forall s \in \mathcal{S}, o \in \mathcal{O}, g \in \mathcal{O}. \tag{34}$$

In addition, we introduce integer variables  $\beta_{os} = \sum_{b_s} y_{b_so}$  that denote the number of RUs connected to each OLT-o. To linearize the products  $\beta_{os}K^c_{oqs}$  and  $\beta_{os}L^c_{oqs}$ , we introduce the

binary variables  $A_{oqs}^c$  and  $Z_{oqs}^c$ , and the following constraints:

$$(B_{s} - A_{oqs}^{c}) \leq B_{s} (1 - K_{oqs}^{c}) + (B_{s} - \beta_{os}),$$

$$\forall s \in \mathcal{S}, o \in \mathcal{O}, q \in \mathcal{Q},$$

$$(B_{s} - Z_{oqs}^{c}) \leq B_{s} (1 - L_{oqs}^{c}) + (B_{s} - \beta_{os}),$$

$$\forall s \in \mathcal{S}, o \in \mathcal{O}, q \in \mathcal{Q}.$$

$$(36)$$

Latency constraints: If the DU is placed at RU- $b_s$  location, then its corresponding Stage-I TWDM-PON with OLT-o will act as a mid-haul link, but if the DU is placed at the OLT-o location, then the Stage-I TWDM-PON will act as a front-haul link. This is ensured for the uplink and downlink by the following constraints  $\forall s \in \mathcal{S}, b_s \in \mathcal{B}_s, o \in \mathcal{O}$ :

<span id="page-9-0"></span>
$$\mathcal{T}_{b_{s}o}^{UL} = y_{b_{s}o} \left\{ \delta_{b_{s}o} + \frac{D_{b_{s}r_{I}} + D_{r_{I}o}}{v_{c}} \right\}$$

$$+ \left\{ \frac{\sum_{s} \sum_{b_{s}} \chi_{b_{s}o}^{d} U_{b_{s}}^{UL}}{R_{o}^{UL}} + \frac{\sum_{s} \sum_{b_{s}} \Upsilon_{b_{s}o}^{d} V_{b_{s}}^{UL}}{R_{o}^{UL}} \right\}$$

$$\times \delta^{TTI} \leq \omega_{b_{s}}^{d} \Delta^{FH} + \omega_{os}^{d} \Delta_{s}^{MH}, \qquad (37)$$

$$\mathcal{T}_{b_{s}o}^{DL} = y_{b_{s}o} \left\{ \frac{D_{b_{s}r_{I}} + D_{r_{I}o}}{v_{c}} \right\}$$

$$+ \left\{ \frac{\sum_{s} \sum_{b_{s}} \chi_{b_{s}o}^{d} U_{b_{s}}^{DL}}{R_{o}^{DL}} + \frac{\sum_{s} \sum_{b_{s}} \Upsilon_{b_{s}o}^{d} V_{b_{s}}^{DL}}{R_{o}^{DL}} \right\}$$

$$\times \delta^{TTI} \leq \omega_{b_{s}}^{d} \Delta^{FH} + \omega_{os}^{d} \Delta_{s}^{MH}. \qquad (38)$$

In (37), the parameters  $\delta_{b_so}$  denote the reduced waiting time for uplink data at ONUs associated to RUs within each TTI interval. The second term denotes the signal propagation latency and the third term denotes the uplink data transmission latency per TTI. The parameters  $V_{b_s}^{U\dot{L}}$  and  $V_{b_s}^{DL}$  denote the required uplink and downlink front-haul throughput and  $U_{bs}^{\mathit{UL}}$ and  $U_{b_a}^{DL}$  denote the required uplink and downlink mid-haul throughput of RU- $b_s$ . The parameters  $R_o^{UL}$  and  $R_o^{DL}$  denote the maximum supported throughput of the Stage-I TWDM-PON. At the right side of the inequality, the parameter  $\Delta^{FH}$ denotes the maximum front-haul latency and the parameter  $\Delta_s^{MH}$  denotes the maximum mid-haul latency of slice s. As there is no waiting time in the downlink of TWDM-PON, we consider only signal propagation and data transmission latencies in (38). Note that the DUs are placed either at RU/ONU or at OLT locations of Stage-I TWDM-PON. Therefore, the Stage-II TWDM-PON is required as mid-haul only if the CU is placed at the OLT of the Stage-II TWDM-PON and the uplink and downlink constraints are given below:

<span id="page-9-1"></span>
$$\mathcal{T}_{oq}^{UL} = z_{oq} \left\{ \delta_{oq} + \frac{D_{or_{II}} + D_{r_{II}q}}{v_{c}} \right\} + \left\{ \frac{\sum_{s} \sum_{o} Z_{oqs}^{c} U_{o}^{UL}}{R_{q}^{UL}} \right\}$$

$$\times \delta^{TTI} \leq \omega_{qs}^{c} \Delta_{s}^{MH}, \forall s \in \mathcal{S}, o \in \mathcal{O}, q \in \mathcal{Q}, \qquad (39)$$

$$\mathcal{T}_{oq}^{DL} = z_{oq} \left\{ \frac{D_{r_{II}q} + D_{r_{II}q}}{v_{c}} \right\} + \left\{ \frac{\sum_{s} \sum_{o} Z_{oqs}^{c} U_{o}^{DL}}{R_{q}^{DL}} \right\} \delta^{TTI}$$

$$\leq \omega_{qs}^{c} \Delta_{s}^{MH}, \forall s \in \mathcal{S}, o \in \mathcal{O}, q \in \mathcal{Q}. \qquad (40)$$

Alongside the communication latency constraints, we also consider the processing latency constraints for the RU-DU-CU

<span id="page-10-2"></span>functions as follows 
$$\forall s \in \mathcal{S}, b_s \in \mathcal{B}_s, o \in \mathcal{O}, q \in \mathcal{Q}$$
:

$$\mathcal{T}_{rdc}^{UL} = \begin{cases}
\frac{\eta_{b_s,RU}^{UL}}{H_{b_s}^{UL}} + \frac{\omega_{b_s}^d \Gamma_{b_s,DU}^{UL}}{GD_{b_s}^{UL}} + \frac{\sum_s \sum_{b_s} \Upsilon_{b_s}^d \Gamma_{b_s,DU}^{UL}}{GD_o^{UL}} \\
+ \frac{\sum_s \sum_o A_{oqs}^c \Gamma_{b_s,CU}^{UL}}{GC_o^{UL}} + \frac{\sum_s \sum_o Z_{oqs}^c \Gamma_{b_s,CU}^{UL}}{GC_q^{UL}}
\end{cases}$$

$$\leq \frac{\Delta_{b_s}^{BBU}}{\delta^{TTI}}, \qquad (41)$$

$$\mathcal{T}_{rdc}^{DL} = \begin{cases}
\frac{\eta_{b_s,RU}^{DL}}{H_{b_s}^{DL}} + \frac{\omega_{b_s}^d \Gamma_{b_s,DU}^{DL}}{GD_{b_s}^{DL}} + \frac{\sum_s \sum_b \Upsilon_{b_s}^d \Gamma_{b_s,DU}^{DL}}{GD_o^{DL}} \\
+ \frac{\sum_s \sum_o A_{oqs}^c \Gamma_{b_s,CU}^{DL}}{GC_o^{DL}} + \frac{\sum_s \sum_o Z_{oqs}^c \Gamma_{b_s,CU}^{UL}}{GC_q^{DL}}
\end{cases}$$

$$\leq \frac{\Delta_{b_s}^{BBU}}{\delta^{TTI}}. \qquad (42)$$

In both of these constraints, the first term denotes the RU processing latency at RU location  $b_s$ , the second term denotes the DU processing latency at RU location  $b_s$ , the third term denotes the DU processing latency at Stage-I OLT location o, the fourth term denotes the CU processing latency at Stage-I OLT location o, and the fifth term denotes the CU processing latency at Stage-II OLT location q. The parameters  $n_{b_s,RU}^{UL}$  and  $\eta_{b_s,RU}^{DL}$  denote the required GOPS/TTI for uplink and downlink RU functions, parameters  $\Gamma^{UL}_{b_s,DU}$  and  $\Gamma^{DL}_{b_s,DU}$  denote the required GOPS/TTI for uplink and downlink DU functions, and parameters  $\Gamma^{UL}_{b_s,CU}$  and  $\Gamma^{DL}_{b_s,CU}$  denote the required GOPS/TTI for uplink and downlink CU functions. Moreover, the parameters  $\bar{H}_{b_s}^{UL}$  and  $H_{b_s}^{DL}$  denote the maximum available GOPS/TTI for uplink and downlink RU function processing, parameters  $GD_{b_s}^{UL}$  and  $GD_{b_s}^{DL}$  denote the maximum available GOPS/TTI for uplink and downlink DU function processing at RU- $b_s$  such that  $G_{b_s} = (GD_{b_s}^{UL} + GD_{b_s}^{DL})$ , parameters  $GD_o^{UL}$  and  $GD_o^{DL}$  denote the maximum available GOPS/TTI for uplink and downlink DU function processing at OLT-o, and parameters  $GC_o^{UL}$  and  $GC_o^{DL}$  denote the maximum available GOPS/TTI for uplink and downlink CU function processing at OLT-o such that  $G_o = (GD_o^{UL} + GD_o^{DL} + GC_o^{UL} + GC_o^{DL})$ , and parameters  $GC_q^{UL}$  and  $GC_q^{DL}$  denote the maximum available GOPS/TTI for uplink and downlink CU function processing at OLT-q such that  $G_q=(GC_q^{UL}+GC_q^{DL})$ .

#### D. Heuristic for Front/Mid-Haul and DU-CU Deployment

After evaluating the UE-RU assignment problem  $\mathcal{P}_1$ , we know the locations of installed RUs corresponding to each slice and their respective throughput demands. Now, we proceed to solve the problem  $\mathcal{P}_2$  and design a heuristic algorithm for connecting the installed RUs with TWDM-PON-based front/mid-haul links and placing open access-edge servers for hosting DUs and CUs. The main focus of this algorithm is to connect all the active RUs with a minimum number of open access-edge servers for hosting DUs and CUs while satisfying the communication and BBU processing latency constraints. This, in turn, reduces the cost of TWDM-PON and server deployment according to the objective (20) of  $\mathcal{P}_2$ . The throughput requirement between the RU-DU interface and

the DU-CU interface, mainly depends on the RU configurations, because we consider 100% PRB usage for the network planning purpose. Let us denote  $\mathfrak{B}_s$  as the set of installed but unassigned RUs,  $\mathfrak{D}$  as the final set of installed Stage-I OLTs, and  $\mathfrak{Q}$  as the final set of installed Stage-II OLTs. Initially, all RUs from all slices are unassigned, i.e.,  $\mathfrak{B}_s = \mathcal{B}_s$  and neither of Stage-I and Stage-II OLTs are installed, i.e.,  $\mathfrak{D} = \emptyset$ ,  $\mathfrak{Q} = \emptyset$ . In the first iteration, we activate only one Stage-I OLT-o and add it to  $\mathfrak{D}$ . Firstly, we consider placing DUs at RU locations, and hence, the Stage-I TWDM-PON acts like a mid-haul interface. Then we sequentially choose one RU- $b_s$  from each slice and associate with an OLT- $o \in \mathfrak{D}$  with minimum distance, i.e.,  $o = \min_o \{D_{b_s o} = (D_{b_s r_I} + D_{r_I o}) | o \in \mathfrak{D}$ ,  $D_{b_s o} \leq D_{o}^{max}\}$ , and check if the following front-haul communication and RU+DU processing latencies are satisfied:

<span id="page-10-0"></span>
$$\left\{ \delta_{b_{s}o} + \frac{D_{b_{s}r_{I}} + D_{r_{I}o}}{v_{c}} \right\} + \left\{ \frac{U_{b_{s}}^{UL} + \sum_{s} \sum_{b_{s}' \neq b_{s}} \chi_{b_{s}o}^{d} U_{b_{s}'}^{UL}}{R_{o}^{UL}} \right\} \\
\times \delta^{TTI} \leq \Delta_{s}^{MH}, \tag{43}$$

$$\left\{ \frac{D_{b_{s}r_{I}} + D_{r_{I}o}}{v_{c}} \right\} + \left\{ \frac{U_{b_{s}}^{DL} + \sum_{s} \sum_{b_{s}' \neq b_{s}} \chi_{b_{s}o}^{d} U_{b_{s}'}^{DL}}{R_{o}^{DL}} \right\} \\
\times \delta^{TTI} \leq \Delta_{s}^{MH}, \tag{44}$$

$$\left\{ \frac{\eta_{RU}^{UL}}{H_{b_s}^{UL}} + \frac{\omega_{b_s}^d \Gamma_{b_s,DU}^{UL}}{GD_{b_s}^{UL}} \right\} \le \frac{\Delta_{b_s}^{BBU}}{\delta^{TTI}},$$
(45)

$$\left\{ \frac{\eta_{RU}^{DL}}{H_{b_c}^{DL}} + \frac{\omega_{b_s}^d \Gamma_{DU,b_s}^{DL}}{GD_{b_c}^{DL}} \right\} \le \frac{\Delta_{b_s}^{BBU}}{\delta^{TTI}}.$$
(46)

Secondly, we consider placing DUs at Stage-I OLT locations, and hence, the Stage-I TWDM-PON acts like a front-haul interface and sequentially associate RUs to OLTs. Again, we sequentially choose one  $RU-b_s$  from each slice with minimum distance while checking the following front-haul communication and RU+DU processing latencies are satisfied:

<span id="page-10-1"></span>
$$\left\{ \delta_{b_{s}o} + \frac{D_{b_{s}r_{I}} + D_{r_{I}o}}{v_{c}} \right\} + \left\{ \frac{V_{b_{s}}^{UL} + \sum_{s} \sum_{b'_{s} \neq b_{s}} \Upsilon_{b'_{s}o}^{d} V_{b'_{s}}^{UL}}{R^{UL}} \right\} \\
\times \delta^{TTI} \leq \Delta^{FH}, \tag{47}$$

$$\left\{ \frac{D_{b_{s}r_{I}} + D_{r_{I}o}}{v_{c}} \right\} + \left\{ \frac{V_{b_{s}}^{DL} + \sum_{s} \sum_{b'_{s} \neq b_{s}} \Upsilon_{b'_{s}o}^{d} V_{b'_{s}}^{DL}}{R^{DL}_{o}} \right\} \\
\times \delta^{TTI} \leq \Delta^{FH}, \tag{48}$$

$$\left\{ \frac{\eta_{RU}^{UL}}{H_{b_{s}}^{UL}} + \frac{\Gamma_{b_{s},DU}^{UL} + \sum_{s} \sum_{b'_{s} \neq b_{s}} \Upsilon_{b'_{s}o}^{d} \Gamma_{b'_{s},DU}^{UL}}{GD_{o}^{UL}} \right\} \leq \frac{\Delta_{b_{s}}^{BBU}}{\delta^{TTI}}, \tag{49}$$

$$\left\{ \frac{\eta_{RU}^{DL}}{H_{b_{s}}^{DL}} + \frac{\Gamma_{b_{s},DU}^{DL} + \sum_{s} \sum_{b'_{s} \neq b_{s}} \Upsilon_{b'_{s}o}^{d} \Gamma_{b'_{s},DU}^{DL}}{GD_{o}^{DL}} \right\} \leq \frac{\Delta_{b_{s}}^{BBU}}{\delta^{TTI}}. \tag{50}$$

After this step, we calculate the total cost of OLT installation, fiber deployment, and open access-edge server placement for both the cases, i.e., when the DU is located at the RU and at a Stage-I OLT location. Then we choose the option with minimum cost and accordingly set  $y_{b_so}=1$ ,  $\theta_o=1$ ,  $\omega_{b_s}^d=1$  (Case-1), and  $\omega_{b_so}^d=1$  (Case-2). Then we remove this RU from  $\mathfrak{B}_s$  and continue the same process with the remaining

RUs. If a DU server for any RU could not be installed, then the for loop at lines 2-22 breaks. Clearly, in this case  $\mathfrak{B}_s \neq \emptyset, \forall s$ and lines (25)-(28) are executed. This means a new OLT-o'is inserted to  $\mathfrak{O}$  and the RU assignment loop at lines 2-22 is restarted by the while loop at lines 1-29. When supported throughput of the OLTs are different, then prioritize the OLTs with higher throughput support. If all the RUs are attached to the Stage-I OLTs, the success flag is set, i.e., sucs = 1and the while loop stops. However, if all the Stage-I OLTs are explored, i.e.,  $|\mathfrak{O}| \neq |\mathcal{O}|$  and a DU server could not be installed for some RU, then the while loop as well as the algorithm stops due to infeasibility. Next, we reset the success flag at line 30 and check if we can also deploy the CUs in open access-edge servers at OLT-o locations by adding the respective processing latency terms  $\frac{\Gamma_{b_s,CU}^{UL} + \sum_s \sum_o A_{oqs}^C \Gamma_{b_s',CU}^{UL}}{GC^{UL}}$ 

and  $\frac{\Gamma_{b_s,CU}^{DL} + \sum_s \sum_o A_{oqs}^c \Gamma_{b_s,CU}^{DL}}{GC_o^{DL}}$  to (45)-(46) or (49)-(50). If this step is successful, then we set  $\omega_{os}^c = 1$ , otherwise, we find a Stage-II OLT-q with minimum distance from Stage-I OLT-o for installing open access-edge servers to host CUs. Additionally, we need to check if (39)-(42) are satisfied. We can do this by following a similar process as Stage-I. Here also we start with just one Stage-II OLT in Q and iteratively add new Stage-II OLTs to find CU servers for all the RUs. Once a suitable Stage-II OLT-q is found, we set the corresponding  $\omega_{oas}^c = 1$ ,  $z_{oq} = 1$ . If all the CUs could be successfully placed by the for loop in lines 32-42, then we set sucs = 1 again and the algorithm stops successfully. Otherwise, if a CU server could not be installed against some Stag-I OLT, then the while loop in lines 31-48 stops due to infeasibility. The TWDM-PON-based front/mid-haul design and open access-edge server placement algorithm is given in Algorithm 2.

Theorem 2: The Algorithm 2 provides a  $O(\log_e(O \times I))$  $\sum_s B_s$ )) approximation to the optimal solution for  $\mathcal{P}_2$ .

*Proof:* Let  $O^*$  denote the optimum number of Stage-I OLTs. Initially, there are  $B_0 = (\sum_s B_s)$  unconnected RUs and  $B_t$ denotes the number of RUs remaining to be connected after t greedy iterations. Therefore, after (t-1) iterations,  $B_{t-1}$ RUs are still remaining to be connected and there exists some Stage-I OLT that connects at least  $(B_{t-1}/O^*)$  RUs (by the pigeonhole principle). As our greedy method attempts to connect the maximum number of the remaining RUs to Stage-I OLTs (with properly placed DUs) at every step, it must select a Stage-I OLT connecting at least  $(B_{t-1}/O^*)$  RUs. Hence, the number of remaining RUs to be connected is at most

$$B_t \le \left(B_{t-1} - \frac{B_{t-1}}{O^*}\right) = B_{t-1}\left(1 - \frac{1}{O^*}\right).$$
 (51)

Thus, the number of remaining RUs decreases by a factor of at least  $(1-1/O^*)$  with every iteration and after t iterations, we have  $B_t \leq B_0(1-1/O^*)^t$ . If the greedy method runs for  $(O_G + 1)$  iterations, we must have at least one remaining unconnected RU at the  $O_G$ -th iteration such that

<span id="page-11-1"></span>
$$1 \le B_{O_G} \le B_0 \left( 1 - \frac{1}{O^*} \right)^{O_G} = B_0 \left( 1 - \frac{1}{O^*} \right)^{O^* \times \frac{O_G}{O^*}} \cdot 1 \le B_0 (1/e)^{\frac{O_G}{O^*}} \Rightarrow \frac{O_G}{O^*} \le \log_e(B_0) \Rightarrow O_G \le O^* \log_e(B_0).$$
(52)

# Algorithm 2 Heuristic for Front/Mid-Haul & DU-CU Deploy

```
 \begin{array}{c} \textbf{Input: } \mathcal{S}, \mathcal{B}_{s}, \mathcal{O}, \mathcal{Q}, D_{b_{s}o}, D_{oq}, D_{o}^{max}, D_{q}^{max}, U_{b_{s}}^{U/DL}, \\ V_{b_{s}}^{U/DL}, R_{o}^{U/DL}, R_{q}^{U/DL}, \Gamma_{b_{s},CU}^{U/DL}, \Gamma_{b_{s},DU}^{U/DL}, H_{b_{s}}^{U/DL}, GD_{b_{s}}^{U/DL}, \\ GD_{o}^{U/DL}, GC_{o}^{U/DL}, GC_{q}^{U/DL}, \Delta^{FH}, \Delta_{s}^{MH}, \Delta_{b_{s}}^{BBU}. \end{array} 
      Output: y_{b_so}^*, z_{oq}^*, \omega_{b_s}^{d*}, \omega_{b_so}^{d*}, \omega_{os}^{c*}, \omega_{oqs}^{c*}, \theta_o^*, \theta_q^*. Initialize: \mathfrak{B}_s = \mathcal{B}_s, \mathfrak{S} = \{o\}, \mathfrak{Q} = \{q\}, sucs = 0.
  1: while sucs \neq 1 and |\mathfrak{I}| \neq |\mathcal{O}| do

               for b_s \leftarrow 1 to \max\{B_s\} do
                      for s \leftarrow 1 to S do
  4:
                             if b_s \leq B_s then
                                     Find o = \min_{o} \{D_{b_so} | D_{b_so} \le D_o^{max}\}; if (43)-(46) are satisfied then
  5:
  6:
                                                                                                                         ⊳ Case-1
  7:
                                             Calculate the total cost;
  8:
                                                                                                                         ⊳ Case-2
  9:
                                      if (47)-(50) are satisfied then
10:
                                             Calculate the total cost;
11:
                                      if Case-1 costs minimum then
12:
                                      y_{b_so} \leftarrow 1, \theta_o \leftarrow 1, \omega_{b_s}^d \leftarrow 1; else if Case-2 costs minimum then
13:
14:
                                          \begin{array}{ll} y_{b_so} \leftarrow 1, \ \theta_o \leftarrow 1, \ \omega^d_{b_so} \leftarrow 1; \\ \mathbf{se} & \rhd \ \mathsf{Some} \ \mathsf{RU} \ \mathsf{is} \ \mathsf{unassigned} \end{array}
15:
16:
                                      break;
                                                                                      \triangleright infeasible if |\mathfrak{O}| = |\mathcal{O}|
17:
                                      end if
18:
19:
                              end if
20:
                              \mathfrak{B}_{S} \leftarrow \mathfrak{B}_{S} \setminus b_{S};
21:
                      end for
22:
               end for
23:
               if \mathfrak{B}_s = \emptyset, \forall s then

    All RUs are assigned

                sucs \leftarrow 1;
24:
25:

                      \mathfrak{B}_s \leftarrow \mathcal{B}_s, \forall s;
26:

⊳ RU set reinitialized

                      \mathfrak{O} \leftarrow \mathfrak{O} \cup \{o'\};
27:

               end if
28:
29: end while
30: sucs \leftarrow 0;

    ▶ Reset the success flag

31: while sucs \neq 1 and |\mathfrak{Q}| \neq |\mathcal{Q}| do

    Stage-II design

32:
               for o \leftarrow 1 to |\mathfrak{O}| do
                      for s \leftarrow 1 to S do
33:
                              if CU can be processed at o then
34:
35:
                              \omega_{os}^c \leftarrow 1;
36:
                                     Find q = \min_{q} \{D_{oq} | D_{oq} \leq D_q^{max}\};
Subject to constraints (39)-(42);
37:
38:
39.
                                     \omega_{oqs}^c \leftarrow 1, z_{oq} \leftarrow 1;
                              end if
40:
41:
                      end for
42:
               end for
43:
               if All CUs are placed then
44:
                      sucs \leftarrow 1;
45:
                      \mathfrak{Q} \leftarrow \mathfrak{Q} \cup \{q'\};
                                                                                  ⊳ New Stage-II OLT added
46:
               end if
47:
49: return y_{b_so}, z_{oq}, \omega_{b_s}^d, \omega_{b_so}^d, \omega_{os}^c, \omega_{oqs}^c, \theta_o, \theta_q;
```

Now, using the well-known Taylor series approximation  $(1-x)^{\frac{1}{x}} \gtrsim (1/e)$  in (52), we have,

$$1 \le B_0(1/e)^{\frac{O_G}{O^*}} \Rightarrow \frac{O_G}{O^*} \le \log_e(B_0) \Rightarrow O_G \le O^* \log_e(B_0)$$
(53)

Similarly, we can show that if the greedy method runs for  $(Q_G+1)$  iterations to connect O Stage-I OLTs, then  $Q_G \leq Q^* \log_e(O)$ , where  $Q^*$  denotes the optimal number of Stage-II OLTs. Therefore, the solution for  $\mathcal{P}_2$  produced by Algorithm 2 can be approximated by a factor of  $O(\log_e(B_0) + \log_e O)$  or  $O(\log_e(O \times \sum_s B_s))$  to the optimal solution.

When the problem  $\mathcal{P}_2$  is feasible, every iteration of the first while loop of Algorithm 2 connects at least one RU to a Stage-I OLT while appropriately placing a DU server. It generates all possible RU and Stage-I OLT combinations with complexity  $O((\sum_s B_s)O^2)$  and their feasibility is verified with  $O((\sum_s B_s)O)$ . Thus, we can analyze that the worst-case complexity of this while loop is  $((\sum_s B_s)^2O^3)$ . Similarly, the complexity of designing Stage-II TWDM-PON is  $O(O^2Q^3)$ . Therefore, the Algorithm 2 converges with a worst-case complexity of  $O((\sum_s B_s)^2O^3)$  (as  $O(\sum_s B_s)^2O^3$ ) so  $O(\sum_s B_s)$ 0 to a solution upper-bounded by a factor of  $O(\sum_s B_s)$ 1 to the optimal solution.

#### V. RESULTS AND DISCUSSION

<span id="page-12-0"></span>For evaluating the proposed framework, we consider O-RAN deployment in dense industrial, urban residential, and sparsely populated rural areas. The dimensions of these areas vary from  $1 \times 1 \text{ km}^2$  to  $4 \times 4 \text{ km}^2$  and the maximum UE density in the industrial, urban, and rural areas are 2000, 1000, and 500 #/km<sup>2</sup>, respectively. However, to capture the spatiotemporal and tidal wave characteristics of mobile traffic [40], we consider the hourly UE density variation at different areas as shown in Fig. 4. We generate random UE locations according to the maximum UE densities of different areas but only a fraction of them actively transmit data at peak throughput (from Table IV) at different time instants. The total number of active UEs at different time instants remains consistent with Fig. 4 and their respective throughput requirements are derived as the average of peak throughput across their active data transmission times. This reduces the over-provisioning of resources at the RAN installation stage. After the RAN deployment, UEs can be dynamically associated with RUs in real-time based on their actual QoS requirements.

The maximum number of RUs per km<sup>2</sup> area is 15 and they are classified in uRLLC, eMBB, and mMTC slices according to the UE distribution shown in Table IV. The coverage distance of the RUs varies within 0.5-1 km and the transmission powers of the macro and small-cell RUs are 46 dBm and 30 dBm, respectively. The RU locations are also the locations for Stage-I OLTs. We consider the highest RU configuration as 4x4 MIMO, 2 layers, 100 MHz bandwidth, TTI duration 0.5 msec, and 30 kHz sub-carrier spacing. Thus, the peak wireless throughput supports are uplink: 28 Gbps and downlink: 30 Gbps, respectively [36]. Accordingly, their throughput demands for front-haul (split-7.2) are uplink: 9.632 Gbps, downlink: 11.113 Gbps and for mid-haul (split-2) are uplink: 1.111 Gbps, downlink: 1.111 Gbps [51]. Both Stage-I and Stage-II TWDM-PONs can support a maximum throughput of 100 Gbps. The average reduced waiting time of uplink data at the ONUs is 5  $\mu$ sec [24]. We consider the OTA latency bound as 200-400  $\mu$ sec and the front-haul latency

![](_page_12_Figure_7.jpeg)

<span id="page-12-2"></span>Fig. 4. Active UE density variation in industrial, urban, and rural areas across different hours of a day.

<span id="page-12-1"></span>TABLE IV
UE DISTRIBUTION AND THROUGHPUT REQUIREMENTS

|       | Industrial (%) | Urban<br>(%) | Rural<br>(%) | Uplink<br>(Mbps) | Downlink<br>(Mbps) |
|-------|----------------|--------------|--------------|------------------|--------------------|
| uRLLC | 25%            | 30%          | 20%          | 10-20            | 30-50              |
| eMBB  | 25%            | 50%          | 60%          | 50-80            | 100-150            |
| mMTC  | 50%            | 20%          | 20%          | 10-20            | 10-20              |

bound as 100  $\mu$ sec for all slices. However, the mid-haul latency bounds for uRLLC, eMBB, and mMTC slices considered are 100  $\mu$ sec, 500  $\mu$ sec, and 1000  $\mu$ sec, respectively. In addition, the computational requirement of each RU is 1800 GOPS/TTI and is divided among RUs, DUs, and CUs. The processing capacities of the open access-edge servers are  $10^5$  GOPS/TTI and we choose the BBU processing latency bounds 50, 80, and 100  $\mu$ sec for uRLLC, eMBB, and mMTC slices, respectively [6]. The cost of open access-edge server installation is  $\leq$ 3800, the cost of computational resources is  $1.5 \leq$ /GOPS [22], the cost of optical fiber is  $100 \leq$ /km, the cost of fiber installation is  $2500 \leq$ /km, the cost of a splitter is  $\leq$ 200, the cost of ONU is  $\leq$ 2000, and the cost of OLT is  $\leq$ 16000 [52].

<span id="page-12-4"></span><span id="page-12-3"></span>In Fig. 5, we present the number of required RUs against industrial, urban, and rural areas by evaluating the UE-RU association problem  $\mathcal{P}_1$ . As the area size grows from  $1 \times 1 \text{ km}^2$  to  $4 \times 4 \text{ km}^2$ , the number of UEs increases, which leads to a higher number of RUs against all scenarios. Interestingly, we also observe that the average wireless throughput per RU (total throughput of UEs/number of RUs) also increases. This implies that resources per RU are shared by a higher number of UEs. The RUs in all the areas are classified into uRLLC, eMBB, and mMTC slices and a major share of the RUs belong to the eMBB slice due to its high throughput demand. Both uRLLC and mMTC slices have similar throughput demands, and hence, a similar number of RUs are required. Each group of the vertical bars in the subplots consists of (left to right) the solution obtained by using the proposed Lagrangian relaxation heuristic (LgR), the optimal solution by IBM Gurobi 9.1 solver (Opt), and the lower bound with integrality relaxation (Low). As the integrality constraints are relaxed, the solutions indicated by Low are

![](_page_13_Figure_2.jpeg)

Fig. 5. Comparison of number of RUs by Lagrangian relaxation heuristic (LgR), the optimal solution (Opt), and the lower bound by integrality relaxation (Low), and the average throughput against the considered (a) industrial, (b) urban, and (c) rural deployment scenarios.

![](_page_13_Figure_4.jpeg)

Fig. 6. Average front-haul uplink and downlink latencies of uRLLC, eMBB, and mMTC slices and the total number of installed OLTs of TWDM-PONs against (a) industrial, (b) urban, and (c) rural areas.

not a feasible solution always but provide a minimum benchmark only. Although IBM Gurobi is much faster than IBM CPLEX, the evaluation of problem P1 with a dataset of size 5 × 5 km2 or more on our computer (Intel Core i7 processor, 32 GB RAM) takes more than two days. Nonetheless, a solution can be obtained very quickly with our proposed heuristic Algorithm [1.](#page-8-0) On some occasions, it could yield a solution exactly the same as the optimal solution, but at other times, it yields a slightly higher number of RUs.

After the UEs are associated with RUs for uRLLC, eMBB, and mMTC slices, we use these RU locations to solve the subsequent DU-CU placement and front/mid-haul design problem P2. Again, we use the commercially available solver IBM Gurobi 9.1 to evaluate the optimal solutions against the industrial, urban, and rural scenarios. We also employ our proposed heuristic Algorithm [2](#page-11-0) to evaluate a near-optimal solution in a time-efficient manner. Firstly, we present the average uplink and downlink communication latencies of the fronthaul interface in Fig. [6](#page-13-1) and the mid-haul interface in Fig. [7.](#page-14-0) To generate the Fig. [6,](#page-13-1) we consider that the DUs for all slices are deployed at the Stage-I OLT locations, whereas for Fig. [7,](#page-14-0) we consider that the DUs for all slices are deployed at the RU locations. Note that this is done just for comparison purposes as deploying all DUs at RU locations is costlier than OLT locations where several DUs can be aggregated in <span id="page-13-1"></span><span id="page-13-0"></span>a single server. Although the peak throughput requirements of both uplink and downlink are similar, the average latencies of the uplink traffic in both front-haul and mid-haul interfaces are slightly higher than the respective downlink traffic due to the waiting time of data at ONUs. We also show the total number of installed OLTs of TWDM-PON obtained from the optimal solution as well as the proposed heuristic Algorithm [2](#page-11-0) in Figs. [6-](#page-13-1)[7](#page-14-0) against the industrial, urban, and rural scenarios. We can observe that a higher number of OLTs are required for front-haul interfaces than for mid-haul interfaces.

Secondly, we present the average virtual BBU, i.e., RU, DU, and CU processing latencies of the uRLLC, eMBB, and mMTC slices in Fig. [8.](#page-14-1) This result shows the optimal values where the DUs of the uRLLC slice are placed at RU locations, but the DUs of eMBB and mMTC slices are placed at Stage-I OLT locations. We observe that the average BBU (RU-DU-CU) processing latency of the industrial area in Fig. [8\(](#page-14-1)a) is slightly higher than the urban area in Fig. [8\(](#page-14-1)b), which is again higher than the rural area in Fig. [8\(](#page-14-1)c). This primarily happens due to the increase in the number of RUs and the required computational efforts. Note that the average RU processing latencies of all three slices are very close to each other because we considered the same RU configuration and 100% PRB usage for the network planning problem. However, the

![](_page_14_Figure_2.jpeg)

Fig. 7. Average mid-haul uplink and downlink latencies of uRLLC, eMBB, and mMTC slices and the total number of installed OLTs of TWDM-PONs against (a) industrial, (b) urban, and (c) rural areas.

![](_page_14_Figure_4.jpeg)

Fig. 8. Average BBU function processing latencies of uRLLC, eMBB, and mMTC slices against (a) industrial, (b) urban, and (c) rural areas.

DU processing latency is lowest for the uRLLC slice against all scenarios because dedicated servers are deployed at RU locations for DU function processing. The DU and CU processing latencies of the eMBB and mMTC slices are almost the same or slightly different from each other because a lesser amount of computational resources are allocated due to a relatively relaxed latency bound of the eMBB and mMTC slices. Interestingly, we can observe that the considered latency bounds for front-haul (100 μsec), mid-haul (100, 500, and 1000 μsec), and BBU (RU-DU-CU) function processing (50, 80, and 100 μsec) are satisfied against all scenarios.

Our primary motivation behind proposing a two-stage TWDM-PON-based sliced O-RAN architecture is to provide flexible and cost-efficient RAN deployment options to mobile network operators. Commonly, only Stage-I TWDM-PON front/mid-haul could be the most cost-efficient option, but for certain scenarios, the double-stage TWDM-PON front/midhaul may prove as a better option. For showing this, we consider two different network configurations and plot the OLT/ONU cost, optical fiber+installation cost, and open access-edge server cost components against industrial, urban, and rural areas. In Fig. [9\(](#page-15-1)a), only Stage-I TWDM-PON is sufficient because the access-edge servers have sufficient resources (10<sup>5</sup> GOPS) to host both the DUs and CUs of the aggregated RUs and hence, including Stage-II TWDM-PONs in the <span id="page-14-1"></span><span id="page-14-0"></span>O-RAN architecture is not required. Nonetheless, in Fig. [9\(](#page-15-1)b), we consider the maximum processing capacities of both the Stage-I and Stage-II servers are 0.5 × 10<sup>5</sup> GOPS such that the servers at Stage-I OLTs have resources only to process the DUs of the aggregated RUs but the CUs are processed by servers at Stage-II OLTs. Thus, our proposed framework is compelled to include the Stage-II TWDM-PON along with Stage-I TWDM-PON in the O-RAN architecture for the CU function processing. In this case, the cost of ONU/OLT and the optical fiber is slightly higher than with only Stage-I, but the overall O-RAN deployment cost reduces as the cost of access-edge servers reduces. From Fig. [9\(](#page-15-1)b), it is also evident that the cost reduction increases with a bigger area and a higher number of devices. We can see nearly 26% or lower cost for 4 × 4 km2 industrial, urban, and rural areas. Note that a much better cost reduction may also be achievable if we use a much higher data rate for the Stage-II TWDM-PON. We consider the maximum 100 Gbps data rate for Stage-I TWDM-PON as earlier but a higher maximum data rate of Stage-II TWDM-PON by aggregating more channels. We assume that the cost of ONUs and OLTs increase linearly with the number of aggregated wavelengths. In Fig. [9\(](#page-15-1)c), we plot the cost of 4 × 4 km2 industrial, urban, and rural areas against *N* = (Stage-II datarate)/(Stage-I datarate). From this plot, we can observe that initially, the overall O-RAN

![](_page_15_Figure_2.jpeg)

Fig. 9. Comparison of front/mid-haul interfaces and open access-edge server deployment cost with (a) only Stage-I TWDM-PON and (b) both Stage-I and Stage-II TWDM-PONs. (c) Comparison of cost reduction achieved with a higher datarate Stage-II than Stage-I TWDM-PON.

![](_page_15_Figure_4.jpeg)

Fig. 10. Pictorial description of various cost components in TWDM-PON and OTN-based front/mid-haul interfaces.

deployment cost decreases steadily as *N* increases due to a better aggregation of Stage-I OLT-ONU boxes through the Stage-II TWDM-PONs. However, the cost reduction becomes very minimal beyond *N* = 3 against the considered scenarios because the cost of OLT/ONUs in Stage-II TWDM-PON increases with *N*.

To compare the performance of our proposed TWDM-PONbased NGFI framework against OTN-based NGFI frameworks, we consider the OTN-based O-RAN architecture proposed in [\[21\]](#page-16-20). In OTN architecture, each node is connected to optical links through a re-configurable add/drop multiplexer (ROADM) and an electric switch (E-switch). The ROADM can switch traffic on a wavelength basis with negligible latency, while the electric switch performs the optical-electric-optical conversion and electric switching [\[22\]](#page-16-21). The RUs and servers for DUs (front-haul links) and the servers for DUs and CUs (mid-haul links) are connected by *mesh topology* and the capacity of each optical path is 100 Gbps [\[21\]](#page-16-20). The cost of each ROADM and E-switch is e19200 and a pictorial description of various cost components of both TWDM-PON and OTN are given in Fig. [10.](#page-15-2) Now, in Fig. [11,](#page-16-25) we compare the O-RAN deployment costs with both the TWDM-PON and OTN-based NGFI frameworks against industrial, urban, and <span id="page-15-2"></span><span id="page-15-1"></span>rural areas. Note that the same RU locations and network configurations are used as input to both the TWDM-PON and OTN-based NGFI frameworks. Both the optimal cost (OpT) and the cost obtained by the heuristic Algorithm [2](#page-11-0) (Hur) are compared against the cost for the OTN-based framework (OTN). We observe that the RAN deployment cost obtained by the heuristic Algorithm [2](#page-11-0) is slightly higher than the optimal solution for P2 in some cases because a higher number of TWDM-PONs are installed. However, the cost of OTN-based frameworks is much higher than the TWDM-PONbased framework against all scenarios. The primary reason behind this is the constraints in establishing optical paths with mesh topology among nodes, which leads to the installation of more nodes in OTN than TWDM-PON. Due to the strict latency requirements of the front-haul interfaces, the traffic can not be aggregated and routed through a large number of hops, especially in sparse rural areas. Furthermore, setting up many optical paths is required with mesh-based OTN architecture, whereas the tree-and-branch architecture of TWDM-PON required a much lower number of fiber links. We could observe the maximum cost saving by TWDM-PON-based framework against industrial area is ∼21%, against urban area is ∼23%, and against rural area is ∼28%.

# VI. CONCLUSION

<span id="page-15-0"></span>In this paper, we have proposed an efficient framework for the optimal placement of RUs based on long-term network statistics and connecting them to open access-edge servers for hosting the corresponding DU and CU functions over the front/mid-haul interfaces while satisfying the diverse QoS requirements of uRLLC, eMBB, and mMTC applications. We have proposed a two-stage TWDM-PON network architecture that opportunistically allows us to choose either a single-stage or double-stage deployment. We have formulated a two-stage ILP for UE to RU association and installing TWDM-PON-based front/mid-haul interfaces while flexibly deploying open access-edge servers for hosting DUs and CUs. In turn, we have designed Lagrangian relaxation and greedy approach-based heuristics for solving these ILPs in a timeefficient manner. Using this framework, we find the optimal

![](_page_16_Figure_2.jpeg)

![](_page_16_Figure_3.jpeg)

<span id="page-16-25"></span>![](_page_16_Figure_4.jpeg)

Fig. 11. Comparison of front/mid-haul interfaces and open access-edge server deployment cost with TWDM-PON-based framework, both optimal (OpT) and heuristic (Hur), and OTN-based framework (OTN) against (a) industrial, (b) urban, and (c) rural areas.

number of RUs required for uRLLC, eMBB, and mMTC slices. We also evaluate the communication latencies of the front/mid-haul interfaces and the virtual BBU (i.e., RU-DU-CU) function processing latency. We have shown that the two-stage TWDM-PON-based architecture can lead to better cost optimization against certain network scenarios than a single-stage architecture. Moreover, we evaluate the cost of O-RAN deployment with the proposed TWDM-PON-based as well as the state-of-the-art OTN-based frameworks to show that the TWDM-PON-based framework is at least 21% costefficient over the OTN-based framework due to better network resource utilization.

# REFERENCES

- <span id="page-16-0"></span>[1] A. Gupta and R. K. Jha, "A survey of 5G network: Architecture and emerging technologies," *IEEE Access*, vol. 3, pp. 1206–1232, 2015.
- <span id="page-16-1"></span>[2] L. Gavrilovska, V. Rakovic, and D. Denkovski, "From cloud RAN to open RAN," *Wireless Pers. Commun.*, vol. 113, pp. 1523–1539, Aug. 2020.
- <span id="page-16-2"></span>[3] M. A. Habibi, M. Nasimi, B. Han, and H. D. Schotten, "A comprehensive survey of RAN architectures toward 5G mobile communication system," *IEEE Access*, vol. 7, pp. 70371–70421, 2019.
- <span id="page-16-3"></span>[4] "O-RAN: Towards an open and smart RAN," O-RAN Alliance, Alfter, Germany, White Paper, Oct. 2018. [Online]. Available: https:// static1.squarespace.com/static/5ad774cce74940d7115044b0/t/5bc79b37 1905f4197055e8c6/1539808057078/O-RAN+WP+FInal+181017.pdf
- <span id="page-16-4"></span>[5] "5G wireless fronthaul requirements in a passive optical network context," Telecommun. Standard. Sector ITU (ITU-T), Geneva, Switzerland, Rep. ITU-T G Suppl. 66, Sep. 2020. [Online]. Available: https://www.itu.int/rec/T-REC-G.Sup66/en
- <span id="page-16-5"></span>[6] M. Shehata, A. Elbanna, F. Musumeci, and M. Tornatore, "Multiplexing gain and processing savings of 5G radio-access-network functional splits," *IEEE Trans. Green Commun. Netw.*, vol. 2, no. 4, pp. 982–991, Dec. 2018.
- <span id="page-16-6"></span>[7] M. Ruffini and F. Slyne, "Moving the network to the cloud: The cloud central office revolution and its implications for the optical layer," *J. Lightw. Technol.*, vol. 37, no. 7, pp. 1706–1716, Apr. 1, 2019.
- <span id="page-16-7"></span>[8] S. Das, F. Slyne, A. Kaszubowska, and M. Ruffini, "Virtualized EAST–WEST PON architecture supporting low-latency communication for mobile functional split based on multiaccess edge computing," *IEEE/OSA J. Opt. Commun. Netw.*, vol. 12, no. 10, pp. D109–D119, Oct. 2020.
- <span id="page-16-8"></span>[9] I. Sousa, N. Sousa, M. P. Queluz, and A. Rodrigues, "Fronthaul design for wireless networks," *Appl. Sci.*, vol. 10, no. 14, p. 4754, 2020.
- <span id="page-16-9"></span>[\[10\]](#page-1-0) L. Peterson *et al.*, "Democratizing the network edge," *ACM SIGCOMM Comput. Commun. Rev.*, vol. 49, no. 2, pp. 31–36, May 2019.

- <span id="page-16-10"></span>[\[11\]](#page-1-1) *5G; Management and Orchestration; Concepts, Use Cases and Requirements (3GPP TS 28.530 Version 15.0.0 Release 15)*, ETSI Standard TS 128 530, Oct. 2018. [Online]. Available: https:// www.etsi.org/deliver/etsi\_ts/128500\_128599/128530/15.00.00\_60/ts\_ 128530v150000p.pdf
- <span id="page-16-11"></span>[\[12\]](#page-1-2) H. Zhang, N. Liu, X. Chu, K. Long, A.-H. Aghvami, and V. C. M. Leung, "Network slicing based 5G and future mobile networks: Mobility, resource management, and challenges," *IEEE Commun. Mag.*, vol. 55, no. 8, pp. 138–145, Aug. 2017.
- <span id="page-16-12"></span>[\[13\]](#page-2-2) H. Ghazzai, E. Yaacoub, M.-S. Alouini, Z. Dawy, and A. Abu-Dayya, "Optimized LTE cell planning with varying spatial and temporal user densities," *IEEE Trans. Veh. Technol.*, vol. 65, no. 3, pp. 1575–1589, Mar. 2016.
- <span id="page-16-13"></span>[\[14\]](#page-2-3) F. Bahlke, O. D. Ramos-Cantor, S. Henneberger, and M. Pesavento, "Optimized cell planning for network slicing in heterogeneous wireless communication networks," *IEEE Commun. Lett.*, vol. 22, no. 8, pp. 1676–1679, Aug. 2018.
- <span id="page-16-14"></span>[\[15\]](#page-2-4) R. Q. Shaddad *et al.*, "Planning of 5G millimeterwave wireless access network for dense urban area," in *Proc. 1st Int. Conf. Intell. Comput. Eng. (ICOICE)*, 2019, pp. 1–4.
- <span id="page-16-15"></span>[\[16\]](#page-2-5) G. Otero Pérez, D. L. López, and J. A. Hernández, "5G new radio fronthaul network design for eCPRI-IEEE 802.1CM and extreme latency percentiles," *IEEE Access*, vol. 7, pp. 82218–82230, 2019.
- <span id="page-16-16"></span>[\[17\]](#page-2-5) X. Wang, Y. Ji, J. Zhang, L. Bai, and M. Zhang, "Joint optimization of latency and deployment cost over TDM-PON based MEC-enabled cloud radio access networks," *IEEE Access*, vol. 8, pp. 681–696, 2020.
- <span id="page-16-17"></span>[\[18\]](#page-2-6) W. Xia, T. Q. S. Quek, J. Zhang, S. Jin, and H. Zhu, "Programmable hierarchical C-RAN: From task scheduling to resource allocation," *IEEE Trans. Wireless Commun.*, vol. 18, no. 3, pp. 2003–2016, Mar. 2019.
- <span id="page-16-18"></span>[\[19\]](#page-2-7) A. Basta, A. Blenk, K. Hoffmann, H. J. Morper, M. Hoffmann, and W. Kellerer, "Towards a cost optimal design for a 5G mobile core network based on SDN and NFV," *IEEE Trans. Netw. Service Manag.*, vol. 14, no. 4, pp. 1061–1075, Dec. 2017.
- <span id="page-16-19"></span>[\[20\]](#page-2-8) N. Kazemifard and V. Shah-Mansouri, "Minimum delay function placement and resource allocation for open RAN (O-RAN) 5G networks," *Comp. Netw.*, vol. 188, Apr. 2021, Art. no. 107809.
- <span id="page-16-20"></span>[\[21\]](#page-2-9) M. Klinkowski, "Optimization of latency-aware flow allocation in NGFI networks," *Comput. Commun.*, vol. 161, pp. 344–359, Sep. 2020.
- <span id="page-16-21"></span>[\[22\]](#page-2-10) Y. Xiao, J. Zhang, and Y. Ji, "Can fine-grained functional split benefit to the converged optical-wireless access networks in 5G and beyond?" *IEEE Trans. Netw. Service Manag.*, vol. 17, no. 3, pp. 1774–1787, Sep. 2020.
- <span id="page-16-22"></span>[\[23\]](#page-2-11) L. M. P. Larsen, A. Checko, and H. L. Christiansen, "A survey of the functional splits proposed for 5G mobile crosshaul networks," *IEEE Commun. Surveys Tuts.*, vol. 21, no. 1, pp. 146–172, 1st Quart., 2019.
- <span id="page-16-23"></span>[\[24\]](#page-2-12) T. Tashiro *et al.*, "A novel DBA scheme for TDM-PON based mobile fronthaul," in *Proc. Opt. Netw. Commun. Conf. Exhibit. (OFC)*, 2014, pp. 1–3.
- <span id="page-16-24"></span>[\[25\]](#page-2-13) S. Mondal and M. Ruffini, "A min–max fair resource allocation framework for optical x-haul and DU/CU in multi-tenant O-RANs," in *Proc. IEEE Int. Conf. Commun. (ICC)*, 2022, pp. 1–6. [Online]. Available: https://arxiv.org/abs/2201.07060

- <span id="page-17-0"></span>[\[26\]](#page-2-14) Y. L. Lee, J. Loo, and T. C. Chuah, "A new network slicing framework for multi-tenant heterogeneous cloud radio access networks," in *Proc. Int. Conf. Adv. Electr. Electron. Syst. Eng. (ICAEES)*, 2016, pp. 414–420.
- <span id="page-17-1"></span>[\[27\]](#page-2-15) O. Sallent, J. Perez-Romero, R. Ferrus, and R. Agusti, "On radio access network slicing from a radio resource management perspective," *IEEE Wireless Commun.*, vol. 24, no. 5, pp. 166–174, Oct. 2017.
- <span id="page-17-2"></span>[\[28\]](#page-2-16) D. Liang, R. Gu, Q. Guo, and Y. Ji, "Demonstration of multi-vendor multi-standard PON networks for network slicing in 5G-oriented mobile network," in *Proc. Asia Commun. Photon. Conf. (ACP)*, 2017, pp. 1–3.
- <span id="page-17-3"></span>[\[29\]](#page-2-17) R. Gu, S. Zhang, Y. Ji, and Z. Yan, "Network slicing and efficient ONU migration for reliable communications in converged vehicular and fixed access network," *Veh. Commun.*, vol. 11, pp. 57–67, Jan. 2018.
- <span id="page-17-4"></span>[\[30\]](#page-2-18) C. Song *et al.*, "Hierarchical edge cloud enabling network slicing for 5G optical fronthaul," *IEEE/OSA J. Opt. Commun. Netw.*, vol. 11, no. 4, pp. B60–B70, Apr. 2019.
- <span id="page-17-5"></span>[\[31\]](#page-2-19) M. Ruffini, A. Ahmad, S. Zeb, N. Afraz, and F. Slyne, "Virtual DBA: Virtualizing passive optical networks to enable multi-service operation in true multi-tenant environments," *IEEE/OSA J. Opt. Commun. Netw.*, vol. 12, no. 4, pp. B63–B73, Apr. 2020.
- <span id="page-17-6"></span>[\[32\]](#page-2-20) F. Slyne, S. Zeb, and M. Ruffini, "Stateful DBA hypervisor supporting SLAs with low latency & high availability in shared PON," in *Proc. Opt. Netw. Commun. Conf. Exhibit. (OFC)*, 2021, pp. 1–3.
- <span id="page-17-7"></span>[\[33\]](#page-3-2) "Everything you need to know about open RAN," Parallel Wireless, Nashua, NH, USA, 2020. [Online]. Available: https:// www.parallelwireless.com/resources/everything-you-need-to-knowabout-open-ran/
- <span id="page-17-8"></span>[\[34\]](#page-3-3) Y. Mao, C. You, J. Zhang, K. Huang, and K. B. Letaief, "A survey on mobile edge computing: The communication perspective," *IEEE Commun. Surveys Tuts.*, vol. 19, no. 4, pp. 2322–2358, 4th Quart., 2017.
- <span id="page-17-9"></span>[\[35\]](#page-4-4) D. R. Mafioletti, F. Slyne, R. Giller, M. O'Hanlon, B. Ryan, and M. Ruffini, "A novel low-latency DBA for virtualised PON implemented through P4 in-network processing," in *Proc. Opt. Netw. Commun. Conf. Exhibit. (OFC)*, 2021, pp. 1–3.
- <span id="page-17-10"></span>[\[36\]](#page-4-5) M. Fuentes *et al.*, "5G new radio evaluation against IMT-2020 key performance indicators," *IEEE Access*, vol. 8, pp. 110880–110896, 2020.
- <span id="page-17-11"></span>[\[37\]](#page-4-6) H. Ji, S. Park, J. Yeo, Y. Kim, J. Lee, and B. Shim, "Ultra-reliable and low-latency communications in 5G downlink: Physical layer aspects," *IEEE Wireless Commun.*, vol. 25, no. 3, pp. 124–130, Jun. 2018.
- <span id="page-17-12"></span>[\[38\]](#page-4-7) X. Huang, S. Tang, Q. Zheng, D. Zhang, and Q. Chen, "Dynamic femtocell gNB on/off strategies and seamless dual connectivity in 5G heterogeneous cellular networks," *IEEE Access*, vol. 6, pp. 21359–21368, 2018.
- <span id="page-17-13"></span>[\[39\]](#page-4-8) "5G; Study on channel model for frequencies from 0.5 to 100 GHz (3GPP TR 38.901 version 16.1.0 release 16)," 3GPP, Sophia Antipolis, France, Rep. ETSI TR 138 901, Nov. 2020. [Online]. Available: https://www.etsi.org/deliver/etsi\_tr/138900\_138999/138901/ 16.01.00\_60/tr\_138901v160100p.pdf
- <span id="page-17-14"></span>[\[40\]](#page-4-9) G. Barlacchi *et al.*, "A multi-source dataset of urban life in the city of milan and the province of trentino," *Sci. Data*, vol. 2, Oct. 2015, Art. no. 150055.
- <span id="page-17-15"></span>[\[41\]](#page-5-2) *IEEE Standard for Local and Metropolitan Area Networks–Time-Sensitive Networking for Fronthaul—Amendment 1: Enhancements to Fronthaul Profiles to Support New Fronthaul Interface, Synchronization, and Syntonization Standards*, IEEE Standard 802.1CM, 2020. Accessed: Jul. 9, 2021. [Online]. Available: https://standards.ieee.org/standard/802\_ 1CMde-2020.html
- <span id="page-17-16"></span>[\[42\]](#page-5-3) S. Khatibi, K. Shah, and M. Roshdi, "Modelling of computational resources for 5G RAN," in *Proc. Eur. Conf. Netw. Commun. (EuCNC)*, 2018, pp. 1–5.
- <span id="page-17-17"></span>[\[43\]](#page-5-4) H. Boostanimehr and V. K. Bhargava, "Unified and distributed QoSdriven cell association algorithms in heterogeneous networks," *IEEE Trans. Wireless Commun.*, vol. 14, no. 3, pp. 1650–1662, Mar. 2015.
- <span id="page-17-18"></span>[\[44\]](#page-5-4) W. Saad, Z. Han, R. Zheng, M. Debbah, and H. V. Poor, "A college admissions game for uplink user association in wireless small cell networks," in *Proc. IEEE Int. Conf. Comput. Commun. (IEEE INFOCOM)*, 2014, pp. 1096–1104.
- <span id="page-17-19"></span>[\[45\]](#page-5-5) J. Zuo, J. Zhang, C. Yuen, W. Jiang, and W. Luo, "Energy efficient user association for cloud radio access networks," *IEEE Access*, vol. 4, pp. 2429–2438, 2016.
- <span id="page-17-20"></span>[\[46\]](#page-5-5) J. Yao and N. Ansari, "QoS-aware joint BBU-RRH mapping and user association in cloud-RANs," *IEEE Trans. Green Commun. Netw.*, vol. 2, no. 4, pp. 881–889, Dec. 2018.
- <span id="page-17-21"></span>[\[47\]](#page-6-6) H. M. Soliman and A. Leon-Garcia, "QoS-aware joint RRH activation and clustering in cloud-RANs," in *Proc. IEEE Wireless Commun. Netw. Conf. (WCNC)*, 2016, pp. 1–6.

- <span id="page-17-22"></span>[\[48\]](#page-7-5) M. L. Fisher, "The Lagrangian relaxation method for solving integer programming problems," *Manag. Sci.*, vol. 27, no. 1, pp. 1–18, Jan. 1981.
- <span id="page-17-23"></span>[\[49\]](#page-7-6) D. P. Bertsekas, *Nonlinear Programming*. Belmont, MA, USA: Athena Sci., 1999.
- <span id="page-17-24"></span>[\[50\]](#page-7-7) R. K. Ahuja, T. L. Magnanti, and J. B. Orlin, *Network Flows: Theory, Algorithms, and Applications*. Upper Saddle River, NJ, USA: Prentice-Hall, 1993, ch. 16.
- <span id="page-17-25"></span>[\[51\]](#page-12-3) *IEEE Standard for Packet-based Fronthaul Transport Networks*, IEEE Standard 1914.1-2019, 2020. Accessed: Jun. 2, 2021. [Online]. Available: https://standards.ieee.org/standard/1914\_1-2019.html
- <span id="page-17-26"></span>[\[52\]](#page-12-4) G. V. Arévalo, R. C. Hincapié, and R. Gaudino, "Optimization of multiple PON deployment costs and comparison between GPON, XGPON, NGPON2 and UDWDM PON," *Opt. Switch. Netw.*, vol. 25, pp. 80–90, Jul. 2017.

![](_page_17_Picture_29.jpeg)

**Sourav Mondal** (Member, IEEE) received the B.Tech. degree in electronics and communication engineering from the Kalyani Government Engineering College, West Bengal University of Technology in 2012, the M.Tech. degree in telecommunication systems engineering from the Department of Electronics and Electrical Communication Engineering, Indian Institute of Technology Kharagpur in 2014, and the Ph.D. degree from the Department of Electrical and Electronic Engineering, University of Melbourne in

2020. He was employed as an Engineer with Qualcomm India Pvt., Ltd., from 2014 to 2016. He is currently working as an EDGE/Marie Skłodowska-Curie Postdoctoral Fellow with CONNECT Centre for Future Networks and Communication, Trinity College Dublin, Ireland.

![](_page_17_Picture_32.jpeg)

**Marco Ruffini** (Senior Member, IEEE) received the M.Eng. degree in telecommunications from the Polytechnic University of Marche, Italy, in 2002, and the Ph.D. degree from Trinity College Dublin (TCD) in 2007. He was as a Research Scientist with Philips, Germany. In 2005, he joined TCD, where he is an Associate Professor and a Fellow. He is the Principal Investigator of both the IPIC Photonics Integration Centre and the CONNECT Telecommunications Research Centre. He is currently involved in several Science Foundation Ireland

and H2020 projects, including a new research infrastructure to build a beyond 5G testbed in Dublin. He leads the Optical Network and Radio Architecture Group, TCD, and has authored over 160 international publications, and over ten patents, and contributed to standards at the broadband forum. He has raised research funding in excess of e8M. His main research is in the area of 5G optical networks, where he carries out pioneering work on the convergence of fixed-mobile and access-metro networks, and on the virtualization of nextgeneration networks, and has been invited to share his vision through several keynote and talks at the major international conferences across the world. He leads the new SFI-funded Ireland's Open Networking testbed infrastructure (OpenIreland).
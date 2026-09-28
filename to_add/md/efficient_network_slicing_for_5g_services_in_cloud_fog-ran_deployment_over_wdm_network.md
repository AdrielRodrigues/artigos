# Efficient Network Slicing for 5G Services in Cloud Fog-RAN Deployment Over WDM Network

Muhammad Ahsan , Ashfaq Ahmed , Senior Member, IEEE, Huma Fida, Arafat Al-Dweik , Senior Member, IEEE, Umair Sajid Hashmi , Member, IEEE, and Arsalan Ahmad , Senior Member, IEEE

Abstract—Network slicing in fifth generation (5G) radio access network (RAN) enables serving massive network traffic with diverse and stringent quality of service (QoS) requirements. Multiple logical networks can be built using RAN slicing over a single RAN infrastructure. This paper considers three different types of slices that are standardized by third generation partner project (3GPP): ultra-reliable low-latency communication (URLLC), enhanced mobile broadband (eMBB), and massive machine type communication (mMTC). Each slice type has unique requirements for data rate, latency, and reliability. Cloud RAN (C-RAN) was proposed to address the requirements of 5G services, which involves physical separation between the remote radio head (RRH) and baseband unit (BBU) in 2-layers. While C-RAN enables more efficient resource utilization and energy consumption, it limits network scalability. Furthermore, C-RAN is unable to meet the stringent latency demands of URLLC services, as well as the massive fronthaul capacity required for eMBB requests. To address this issue, we propose a novel cloud fog RAN (CF-RAN) over wavelength division multiplexing (WDM) architecture. In CF-RAN over WDM the RAN functions are divided into 3 layers, which include the RRH at layer 1, fog nodes at layer 2, and BBU hotels at layer 3. We employ the emerging fog computing paradigm in optical and wireless networks in this suggested architecture. To facilitate low latency URLLC requests, the fog nodes are located closer to the cell site (CS). We propose an

Manuscript received 30 December 2022; revised 12 March 2023; accepted 6 April 2023. Date of publication 11 April 2023; date of current version 19 September 2023. This work was supported by the European Union for the Asi@Connect Project under Contract ACA 2016-376-562. The review of this article was coordinated by Prof. Jelena Misic. (Corresponding author: Ashfaq Ahmed.)

Muhammad Ahsan is with the Department of Electrical Engineering, School of Electrical Engineering and Computer Science, National University of Sciences and Technology, Islamabad 24090, Pakistan, and also with the Interdisciplinary Centre for Security, Reliability and Trust, University of Luxembourg, 4365 Esch-sur-Alzette, Luxembourg (e-mail: mahsan.msee18seecs@seecs.edu.pk).

Ashfaq Ahmed and Arafat Al-Dweik are with the Center for Cyber-Physical Systems, Khalifa University, 127788 Abu Dhabi, UAE (e-mail: ashfaq.ahmed@ku.ac.ae; dweik@fulbrightmail.org).

Huma Fida is with the Department of Computing, School of Electrical Engineering and Computer Science, National University of Sciences and Technology, Islamabad 24090, Pakistan (e-mail: habbasi.msit18seecs@seecs.edu.pk).

Umair Sajid Hashmi is with the Department of Electrical Engineering, School of Electrical Engineering and Computer Science, National University of Sciences and Technology, 24090 Islamabad, Pakistan, and also with the Advanced Wireless Technologies, Dell Technologies, Ottawa, ON K2B 8J9, Canada (e-mail: umair.hashmi@seecs.edu.pk).

Arsalan Ahmad is with the Department of Computing, School of Electrical Engineering and Computer Science, National University of Sciences and Technology, Islamabad 24090, Pakistan, and also with the Department of Electrical and Computer Engineering, College of Engineering, Architecture, and Technology, Oklahoma State University, Stillwater, OK 74078 USA (e-mail: arsalan.ahmad@seecs.edu.pk).

Digital Object Identifier 10.1109/TVT.2023.3266234

integer linear programming (ILP)-based mathematical model. The model's objective is to decrease the number of active BBU hotels and fog nodes while remaining compliant with practical network restrictions. Furthermore, a low complexity greedy heuristic algorithm is proposed to solve the problem and is compared to the branch & bound (B&B) algorithm, which is assumed to provide an optimal solution with exponential complexity. The proposed 3-layer CF-RAN over WDM architecture achieves a 70% improvement in BBU centralization and a 50% reduction in request blocking when compared to the standard 2-layer architecture.

Index Terms—Cloud fog radio access network (RAN) (CFRAN) over wavelength division multiplexing (WDM), fifth generation (5G) services, functional split, network slicing.

#### I. INTRODUCTION

ASSIVE traffic flows are anticipated in future 5G and beyond fifth generation (B5G) networks because of the integration of massive low power Internet of Things (IoT) devices into the cellular network. Meanwhile, the 5G and B5G cellular networks are designed to handle mobile services and applications with a broad range of data rates, latencies, and reliability requirements [1]. These services can be classified into three main categories, namely: URLLC, eMBB, and mMTC. The URLLC services have a strict latency requirement of less than 1 ms and more than 99.99% reliability, as in the case of autonomous driving [2], [3]. The eMBB services are more bandwidth-intensive, such as 4 K video streaming and smart city infrastructure [4]. The mMTC services enable the use of a large number of low-cost devices at relatively low data rates [5]. To handle all the heterogeneous services, the notion of network slicing was introduced [6]. Network slicing utilizes network function virtualization (NFV) to establish several logical networks over the same physical infrastructure and allocates resources to each slice based on its requirements [6]. Network slicing is an efficient approach for handling growing traffic demand while also improving network throughput and cost savings [7]. To support the emerging network slicing paradigm and handle the increasing traffic demand, ongoing efforts in network design development are essential.

Cloud radio access network (RAN) (C-RAN) is a paradigm shift in cellular communications [8]. In C-RAN architecture, baseband units (BBUs) are separated from their corresponding remote radio heads (RRHs) and concentrated at a central location in the form of BBU hotels [9]. The RRHs are retained in the cell sites (CSs). Traditionally, C-RAN has been inherited by 5G

0018-9545 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

<span id="page-1-0"></span>networks to address increased traffic demand and latency [\[10\].](#page-12-0) The number of functions executed locally at the CSs and centrally at the BBU hotels vary according to the selected functional split option [\[11\].](#page-12-0) This centralization has led to significant cost savings, enhanced energy efficiency, and improved resource allocation [\[12\],\[13\].](#page-12-0) On the contrary, it is congested as a result of massive fronthaul traffic between the RRH and BBU hotels[\[14\].](#page-12-0) The fronthaul traffic is transmitted over the common public radio interface (CPRI) protocol [\[15\],](#page-12-0) via the split option 8 defined by 3GPP [\[16\],](#page-12-0) which is an extremely data-intensive protocol. Additionally, the C-RAN one-size-fits-all approach makes it impossible to efficiently meet the requirements of a diverse range of services, including URLLC, eMBB, and mMTC.

To efficiently handle all request types and address the issue of massive fronthaul bandwidth demand, we propose a novel CF-RAN over WDM architecture in this work. Limited baseband processing functions are duplicated at the fog node using NFV in CF-RAN over WDM [\[17\].](#page-12-0) These fog nodes are placed closer to the RRHs, which are located at the CSs, to support time-sensitive URLLC applications and to provide functionality similar to the BBUs [\[18\].](#page-12-0) Following fog node activation, traffic between the RRH and the fog node is referred to as fronthaul, whereas traffic between the fog node and the core central office (CO), as well as the traffic between the BBU hotels and the core CO, is referred to as backhaul. In the case of eMBB and mMTC requests, the fronthaul is carried between the RRHs and BBU hotels, which are located at the COs, as they have less stringent fronthaul latency constraints<sup>1</sup> The backhaul traffic is carried between the BBU hotels and the CO core. Fronthaul traffic is transported between the RRH and the fog node for URLLC requests, whereas backhaul traffic is transported from the fog node to the core CO. Fronthaul traffic is routed through the enhanced common public radio interface (eCPRI) utilizing split option 7 [\[15\],](#page-12-0) which has less stringent data rate constraints than split option 8 while maintaining a high level of function centralization. Therefore, by activating fog nodes and relocating cloud functions closer to the user, the fronthaul capacity and low latency concerns for URLLC services are effectively addressed. Additionally, CF-RAN over WDM is a more cost-effective approach, as fewer BBU hotels are active as compared to a conventional 2-layer architecture, as shown in Fig. 2. To meet its stringent latency requirement, URLLC traffic is processed at the fog nodes. Furthermore, fog nodes are less expensive than BBU hotels because they have limited processing capabilities.

# *A. Related Work*

In recent years, extensive research work has been carried out on network architectures capable of serving the requirements of 5G.

A complete survey of C-RAN is presented in [\[19\].](#page-12-0) The paper discussed the benefits of C-RAN in terms of throughput, energy and cost savings over traditional RAN where RRH and BBU were co-located at the CS. The authors of [\[20\]](#page-12-0) proposed an ILP

![](_page_1_Picture_8.jpeg)

Fig. 1. Proposed cloud fog RAN (CF-RAN) over WDM architecture.

![](_page_1_Picture_10.jpeg)

Fig. 2. Traditional 2-layer architecture.

based mathematical model to allow migration from distributed radio access network (D-RAN) to C-RAN with the objective of minimizing capital expenditure (CAPEX) and operational expenditure (OPEX). This work also highlighted the concept of utilizing existing infrastructure to ensure cost-effective C-RAN deployment. Li et al. [\[21\]](#page-12-0) described a technique for optimizing C-RAN's QoS. The authors of [\[22\],](#page-12-0) [\[23\]](#page-12-0) proposed techniques for optimized resource allocation to ensure greater benefits of network slicing in C-RAN. Provisioning of isolated network

<sup>1</sup>In the rest of the paper, the terms RRH and CS, as well as CO and BBU, are used interchangeably.

| Ref. | Architecture | Network<br>Slicing | Isolation<br>and<br>TGRWA | Fog<br>Comput. | 5G<br>services | Delay Model                                    |
|------|--------------|--------------------|---------------------------|----------------|----------------|------------------------------------------------|
| [22] | C-RAN        | <b>√</b>           | ×                         | ×              | Е              | -                                              |
| [23] | C-RAN        | <b>√</b>           | ×                         | ×              | -              | Transmission, processing, propagation          |
| [24] | C-RAN        | <b>√</b>           | ×                         | ×              | U, E, M        | -                                              |
| [25] | C-RAN        | <b>√</b>           | ×                         | ×              | E, M           | Transmission                                   |
| [26] | RU-DU-CU     | <b>√</b>           | ×                         | ×              | U, E, M        | Transmission, electronic switching, processing |
| [28] | RU-DU-CU     | ×                  | <b>√</b>                  | ×              | -              | -                                              |
| [29] | RU-DU-CU     | <b>√</b>           | <b>√</b>                  | ×              | U, E, M        | Propagation                                    |
| [30] | HEC          | <b>√</b>           | ×                         | ×              | U, E, M        | Propagation, transmission, queue, processing   |
| [31] | Hybrid cloud | <b>√</b>           | ×                         | <b>√</b>       | U, E, M        | Propagation                                    |
| This | CF-RAN       | ✓                  | ✓                         | <b>√</b>       | U, E, M        | Propagation, transmission, interface,          |

TABLE I COMPARISON OF PROPOSED WORK WITH STATE-OF-THE-ART WORK; TGRWA: TRAFFIC GROOMING ROUTING AND WAVELENGTH ASSIGNMENT, U: URLLC, E: EMBB, M: MMTC

slices in C-RAN was investigated in [\[24\],](#page-12-0) where the authors proposed a mathematical model based on mixed integer programming (MIP) and a heuristic algorithm, to jointly optimize throughput and functional split for a given type of request. In [\[25\],](#page-12-0) an software defined network (SDN) based solution was presented for the co-existence of eMBB and mMTC request types in C-RAN.

The authors of [\[26\]](#page-12-0) investigated the deployment of the radio unit (RU)-distributed unit (DU)-central unit (CU) architecture to overcome the scalability limitations of C-RAN. They proposed an ILP based mathematical model and a heuristic algorithm for DU-CU placement to address the problem of increased energy consumption caused by the activation of resources as a result of the insufficient DU-CU placement. The reference [\[27\]](#page-12-0) describes the DU-CU processing functions placement problem and provides a ILP-based mathematical model. In [\[28\],](#page-12-0) various options are proposed to enable slice isolation for resource allocation and security in RU-DU-CU architecture. Li et al. [\[29\]](#page-12-0) presented a heuristic algorithm for isolating network slices while ensuring grooming, routing, and wavelength assignment for various request types. In addition, Reference [\[30\]](#page-12-0) presented an architecture based on hierarchical edge cloud (HEC) to support URLLC, eMBB, and mMTC fronthaul traffic, and evaluated the requirements for each of the three request types in terms of throughput, end-to-end (E2E) latency, and jitter. Finally, a hybrid cloud architecture to support 5G services is discussed in [\[31\].](#page-12-0)

# *B. Motivation and Contributions*

According to the review of the literature, adequate research has been conducted on network slicing in 5G cellular networks. Mostly, the researchers focused on network slicing in the standard C-RAN and RU-DU-CU frameworks. A comparison of our work with the previous work in the literature has been provided in Table I. Table I elaborates how our work fills the knowledge gaps in the state-of-the-art work. To our knowledge, no research has been reported that takes the network slicing paradigm in RAN into consideration when installing CF-RAN over WDM architecture, while also ensuring isolation and grooming, routing, and wavelength assignment of slices. The following are the main contributions to this article:

- 1) We propose a novel CF-RAN over WDM network architecture to meet the latency requirements of URLLC services while also satisfying the high fronthaul capacity demand of eMBB. The strict latency constraint of URLLC and the ultra-high bandwidth requirement of eMBB could be fulfilled by enabling full processing of URLLC requests at the fog nodes rather than COs and deploying eCPRI functional split for transport of fronthaul traffic. Greater gains in terms of performance and cost can be realized in this manner. Furthermore, the scalability of fog nodes reduces the complexity of network integration, allowing for the deployment of additional devices in mMTC.
- 2) We propose a mathematical model based on ILP for efficiently satisfying URLLC, eMBB, and mMTC type requests with the minimum possible active BBU hotels and fog nodes, hence lowering the network cost.
- 3) The mathematical model incorporates the constraints associated with the activation of the BBU hotel and fog nodes, fronthaul latency requirements, network capacity, and isolation-aware routing and wavelength assignment of slice requests.
- 4) A low-complexity heuristic technique based on a greedy approach is proposed to solve the problem. The algorithm grooms, routes, and assigns wavelengths to requests while ensuring slice isolation.
- 5) Finally, we obtain results for a wide range of network and traffic scenarios and compare them to the conventional two-layer approach.

# *C. Paper Organization*

The rest of the paper is organized as follows. The network architecture and traffic types are discussed in Section II. In Section [III,](#page-3-0) a mathematical model based on ILP is developed. In Section [IV,](#page-6-0) the proposed problem is solved using a proposed heuristic and greedy algorithms. The results are discussed in Section [V.](#page-7-0) Finally, in Section [VI,](#page-11-0) a conclusion is drawn.

# II. NETWORK ARCHITECTURE

Fig. [1](#page-1-0) shows the proposed hierarchical CF-RAN over WDM architecture. The nodes are organized into, CSs, fog nodes, BBUs hotels, and core CO. The transmission is conducted from

<span id="page-3-0"></span>![](_page_3_Picture_2.jpeg)

Fig. 3. Network slicing considering three traffic types.

the CS to the BBU hotel/fog node, and finally to the core CO. Alternatively, the computing tasks are performed locally at the fog node for the URLLC requests and at the BBU hotel for all other request types. The nodes are connected through optical fiber links. Each fiber comprises many wavelengths, and each slice is assigned a wavelength to ensure isolation between the various slice types. Although assigning wavelengths to each slice may waste resources, slice isolation is required to provide diverse slices over the same physical infrastructure. Wavelength isolation ensures that distinct slices can be provisioned over the same physical network and provides enhanced reliability and security [29]. Such isolation is also necessary for establishing a real multi-tenant environment. It is assumed that only traffic belonging to the same service type can be groomed into shared lightpaths, i.e., optical channels spanning one or multiple physical links [32].

#### A. Network Slicing

The concept of network slicing is introduced to support various 5G services. Using NFV, network slicing creates multiple logical networks over the same physical infrastructure and allocates resources to each slice based on its requirements [6]. We consider three different types of slices, as shown in Fig. 3, where type 1 is the URLLC slice, type 2 is the eMBB slice, and type 3 is the mMTC slice.

#### B. Functional Split

The functional split in C-RAN refers to the division of functions between the RRH and BBU hotels. The split option selected determines the number of operations performed locally at the RRH and centrally at the BBU hotels. Several functional split options are proposed by 3GPP, generally numbered 1 to 8 [33]. Split option 8 is used in C-RAN to carry fronthaul traffic

that utilizes the CPRI interface. Because of CPRI's high data rate requirements, its deployment is not practicable [34]. To address the fronthaul capacity issue, it may be imperative to investigate a lower-level split point [35]. Split option 7 is the most extensively deployed split option that utilizes the eCPRI protocol for fronthaul traffic transfer [36]. The eCPRI protocol has relatively low bandwidth requirements, and it provides more effective use of available bandwidth than its predecessor, CPRI. Additionally, since it is packet-based, it may be framed within Ethernet [35]. We consider fronthaul and backhaul traffic in our proposed CF-RAN over WDM architecture. Split option 7, the eCPRI split, is used to transport fronthaul traffic. The type 1 traffic's fronthaul is carried between the RRH and the fog nodes. reconfigurable optical add-drop multiplexer (ROADM) [37] is installed on the fog nodes. The fog nodes can use the ROADM to add or remove wavelengths from the transport fiber [38]. It enables type 2 and type 3 requests to pass through fog nodes without being processed. As a result, fog nodes process only type 1 traffic. Fronthaul traffic is transported between the RRH and the BBU hotel for type 2 and type 3 requests, while backhaul traffic is transported between the BBU hotel and the core CO. Backhaul is used to connect fog nodes to the core CO in the case of type 1 traffic. It passes through the BBU hotel node unprocessed.

#### III. SYSTEM MODEL AND PROBLEM FORMULATION

We consider a WDM network topology that includes CS, fog, and CO nodes, and a single core CO. The set of nodes is denoted by  $\mathbb{N} = {\mathbb{N}_c \cup \mathbb{N}_f \cup \mathbb{N}_b}$ , where  $\mathbb{N}_c$ ,  $\mathbb{N}_f$ , and  $\mathbb{N}_b$ represent the set of CS nodes, fog nodes, and the set of COs, including the core CO, respectively. The nodes are connected by a maximum of K fibers per link. The request types are denoted as  $t \in \{1, 2, 3\}$ , where t = 1 represents URLLC requests, t=2 represents eMBB requests, and t=3 represents mMTC requests. The set of URLLC, eMBB, and mMTC fronthaul requests is denoted by  $\mathbb{R}_f^{(1)}$ ,  $\mathbb{R}_f^{(2)}$ , and  $\mathbb{R}_f^{(3)}$ , respectively. Since this work is confined to uplink (UL) transmission, a URLLC fronthaul request is routed towards the fog node via the set of dedicated wavelengths through the pre-computed path  $p \in \mathbb{P}$  if the path delay is smaller than  $D_t$ . These pre-computed paths belong to the virtual link  $v \in \mathbb{V}$  that connects RRH and the fog node. Here p is a physical path spanning one or more physical links between a source and destination node. For a URLLC request, the set of wavelengths is denoted as  $\mathbb{W}_t$ , where t=1. Total path delay is the sum of propagation delay  $l_p$ , transmision delay  $l_{tran}$ , interface delay due to deployed split point  $l_s$ , and electronic switch delay  $l_{el}$ . The fog nodes are equipped with baseband processing capabilities and can handle incoming requests. Only requests of the same type could be groomed into a shared lightpath. The backhaul request is initiated at the fog node for URLLC, which is routed to the core CO via paths belonging to the virtual link  $v \in \mathbb{V}$  initiating at the fog node and terminating at core CO. If the RRH generates an eMBB or mMTC request, it is routed through path p belonging to virtual link  $v \in \mathbb{V}$  to the BBU hotel, traversing fog nodes without being processed. If the fronthaul latency constraint is satisfied, the

<span id="page-4-0"></span>request is forwarded over wavelengths dedicated to eMBB or mMTC slice. The request is processed at the BBU hotel, and a backhaul request is initiated at the BBU hotel, which is carried to the core CO. It is worth noting that the proposed system represents an offline optimization model, which is used to plan an efficient deployment of an optical network.

#### A. Inputs

The inputs to the proposed system are given as,

- $\mathbb{N}$  is a set of nodes, such that  $\mathbb{N} = \{\mathbb{N}_c \cup \mathbb{N}_f \cup \mathbb{N}_b\}$ . Here  $\mathbb{N}_c$  is a set containing the indices of CSs,  $\mathbb{N}_f$  contains the indices of fog nodes, and  $\mathbb{N}_b$  contains the indices of CO nodes, including the core CO,  $\{o\}$  represents the index of core CO. Moreover, N, F, and B, denote the total number of nodes, the total number of fog nodes, and the total number of BBU hotels (equal to the total number of COs), respectively. The total number of CSs are represented as  $N_c$ .
- $\mathbb{N}_{fb} = {\mathbb{N}_f \cup \mathbb{N}_b}$  is a set that contains the indices of all fog nodes and COs, including the core CO.
- $\mathbb{P}$  is a set of computed routed paths derived from the topology of all source and destination nodes. Furthermore,  $\bar{\mathbb{P}}_{ij} \in \mathbb{P}$  is a set of all possible paths from node i to node j. The set  $\bar{\mathbb{P}}_{i*}$  contains all paths that begin with node i, and the set  $\bar{\mathbb{P}}_{*i}$  contains all paths that end with node i. Similarly,  $\bar{\mathbb{P}}_i$  is a set of paths that begin or end at node i.
- $\mathbb{V}$  is a set containing all the virtual links in the network. Furthermore,  $\bar{\mathbb{V}}_i \in \mathbb{V}$  is a set of all virtual links that begin or end at node i. The set  $\bar{\mathbb{V}}_{i*}$  contains all virtual links that begin at node i, and the set  $\bar{\mathbb{V}}_{*i}$  contains all virtual links that end at node i. The paths are pre-computed based on the topology to create virtual links. Multiple paths must be established between each source and destination node to prevent link capacity from being exhausted and to ensure improved reliability. This work refers to the paths between source and destination nodes as virtual links.
- The set of physical links is represented by  $\mathbb{E}$ , with each element denoted by e.
- $\mathbb{T}$  is a set containing the types of requests, where each element of  $\mathbb{T}$  is denoted by the symbol t.
- $\mathbb{P}_v$  is a set of paths that constitute a virtual link v.
- $\mathbb{P}_e$  is a set of paths that pass through link e, and  $P_e$  is the total number of paths along link e.
- $\mathbb{R}$  is a set of requests, with each element denoted by r. Furthermore,  $\mathbb{R} = \{\mathbb{R}_{fn}^{(t)}, \mathbb{R}_{bn}^{(t)}\}$ , where  $\mathbb{R}_{fn}^{(t)}$  and  $\mathbb{R}_{bn}^{(t)}$  are the sets of all fronthaul and backhaul requests of type t from the nth node. The total number of requests is given as R.
- W is a set of all wavelengths. An element in W is denoted by λ. Furthermore, the set of wavelengths dedicated to the tth request type is denoted as W<sub>t</sub> ∈ W. In addition, the capacity of each wavelength is denoted as C.
- The required capacities for fronthaul and backhaul requests of type t are C<sub>f</sub><sup>(t)</sup> and C<sub>h</sub><sup>(t)</sup>.
- The maximum number of fibers that can be placed on each link is K.

- $D_t$  represents the maximum allowable fronthaul latency for a request of type t.
- The delay introduced by each electronic switch is denoted by the symbol  $l_{el}$ . Furthermore, the interface delay introduced by the deployed split option is denoted by the symbol  $l_s$ , and the transmission delay is represented by  $l_{tran}$ .
- The length of the path p is represented by  $l_p$ . It can also be expressed as propagation delay.

# B. Outputs

The outputs of the proposed optimization problem are b,  $\bar{F}$ , x, Z, Y,  $\bar{Y}$ , U, and o, where

- **b** is a binary vector such that  $\mathbf{b} \in \mathbb{B}^{1 \times B}$ , where B is the total number of BBU hotels located at COs. An element in **b** is given as  $b_i$ , with  $b_i = 1$  if a BBU hotel is activated at node i, otherwise  $b_i = 0$ .
- $\bar{\mathbf{F}}$  denotes a binary matrix such that  $\bar{\mathbf{F}} \in \mathbb{B}^{F \times N_c}$ , where F and  $N_c$  denote the total number of fog nodes, and total number of CSs, respectively. An element in  $\bar{\mathbf{F}}$  is represented as  $\bar{f}_{f,n}$ , with  $\bar{f}_{f,n}=1$  if the CS n is connected to fog node f, and  $\bar{f}_{f,n}=0$  otherwise.
- x is a binary indicator for the activation of fog nodes, such that x ∈ B<sup>1×F</sup>. An element in x is denoted as x<sub>f</sub>, where x<sub>f</sub> = 1 if fog node f is activated, otherwise x<sub>f</sub> = 0.
- **Z** is the binary matrix defined as  $\mathbf{Z} \in \mathbb{B}^{B \times N_c}$ , where B is the total number of BBU hotels, and  $N_c$  is the total number of CSs. A **Z** element is represented as  $z_{i,n}$ , with  $z_{i,n} = 1$  if RRH at CS n is connected to CO i, and  $z_{i,n} = 0$  otherwise.
- **Y** is a binary matrix of the form  $\mathbf{Y} \in \mathbb{B}^{R_b \times V}$ , where  $R_b$  denotes the total number of backhaul requests and V denotes the total number of virtual links.  $y_{r,v}$  represents an element of  $\mathbf{Y}$ , such that  $y_{r,v} = 1$  if a backhaul request r is routed over the virtual link v, otherwise  $y_{r,v} = 0$ .
- $\bar{\mathbf{Y}}$  is a binary matrix of the form  $\bar{\mathbf{Y}} \in \mathbb{B}^{R_f \times P}$ , where  $R_f$  denotes the total number of fronthaul requests and P denotes the total number of paths. An element of  $\bar{\mathbf{Y}}$  is denoted as  $\bar{y}_{r,p}$ , such that  $\bar{y}_{r,p} = 1$ , if a fronthaul request r is routed through path p,  $\bar{y}_{r,p} = 0$  otherwise.
- $\mathbf{U} \in \mathbb{Z}^{P \times L}$  is a matrix indicating the number of lightpaths with a particular wavelength established along a particular path. The element  $u_{p\lambda}$  in  $\mathbf{U}$  denotes the number of lightpaths established on path p with wavelength  $\lambda$ .
- o is an integer vector of the form  $\mathbf{o} \in \mathbb{Z}^{1 \times E}$ , with E denoting the total number of links.  $o_e = \{0, 1, \dots, K\}$  is an element of  $\mathbf{o}$ , where K is the maximum number of fibers that can be allocated in a single link.

# C. Constraints

This section discusses the practical network constraints associated with the placement of the BBU hotels in the 5G C-RAN and the implications of this placement.

1) Fog Node Association: The RRH at the CS must be connected to a single fog node. Mathematically, it is given as,

$$\sum_{f=1}^{F} \bar{f}_{f,n} = 1, \ \forall n \in \{1, \dots, N_c\}.$$
 (1)

<span id="page-5-0"></span>2) BBU Hotel Association: An RRH must be connected to a single BBU hotel.

$$\sum_{i=1}^{B} z_{i,n} = 1, \ \forall n \in \{1, \dots, N_c\}.$$
 (2)

3) Fog Nodes Activation: A fog node can serve an RRH only if it is active.

$$\bar{f}_{f,n} \le x_f, \ \forall f \in \{1,\dots,F\}, \ n \in \{1,\dots,N_c\}.$$
 (3)

4) BBU Hotel Activation: The processing functions of a BBU hotel at CO are activated only if it serves at least one RRH.

$$b_i \ge z_{i,n}, \ \forall i \in \{1, \dots, B\}, n \in \{1, \dots, N_c\}.$$
 (4)

5) Fiber Deployment: Each link cannot have more fibers than the maximum allowed of K.

$$\sum_{p=1}^{P_e} u_{p\lambda} \le o_e \le K, \ \forall e \in \{1, \dots, E\},$$

$$t \in \{1, 2, 3\}, \lambda \in \mathbb{W}_t. \tag{5}$$

This constraint determines the number of fibers on each link. The number of fibers on each link must be greater than the number of lightpaths with the same  $\lambda$  that pass through that link, i.e.,  $u_{p\lambda} \leq o_e$ . Furthermore, the number of fibers on each link is limited by K.

6) Fronthaul Capacity: The total number of fronthaul requests routed via a path p should be less than the maximum capacity of the path.

$$\sum_{r \in \mathbb{R}_{fn}^{(t)}} \sum_{p \in \mathbb{P}_v} C_f^{(t)} \bar{y}_{r,p} \le \sum_{\lambda \in \mathbb{W}_t} \sum_{p \in \mathbb{P}_v} Cu_{p\lambda}, \ \forall v \in \mathbb{V}, t \in \mathbb{T}.$$
 (6)

This constraint assures that the aggregate capacity of all fronthaul requests routed through a path p is less than the path's maximum capacity. When a request is routed via path p belonging to virtual link v,  $\bar{y}_{r,p}$  becomes active. The left side of the equation is equal to the sum of all fronthaul requests of type t carried over paths associated with virtual link v. The capacity of a fronthaul request of type t is denoted by  $C_f^{(t)}$ . If a path utilizes the wavelength  $\lambda$ , then  $u_{p\lambda}$  becomes active. The right-hand side of the equation equals the maximum capacity of routes associated with virtual link v, where C is the maximum capacity of a lightpath.

7) Backhaul Capacity: The aggregate of all backhaul requests routed over a virtual link should not exceed the capacity of the virtual link.

$$\sum_{r \in \mathbb{R}^{(t)}} C_b^{(t)} y_{r,v} \le \sum_{\lambda \in \mathbb{W}_t} \sum_{p \in \mathbb{P}_v} C u_{p\lambda}, \ \forall v \in \mathbb{V}, t \in \mathbb{T}.$$
 (7)

This constraint assures that the aggregate of all backhaul requests transported over a virtual link v is less than the virtual link's maximum capacity. When a backhaul request is routed via virtual link v,  $\bar{y}_{r,v}$  is enabled. The left side of the equation equals the sum of all backhaul requests of type t that are carried over the virtual link v. The capacity of a backhaul request of type

t is denoted by  $C_b^{(t)}$ . If a path associated with virtual link v uses the wavelength  $\lambda$ , then  $u_{p\lambda}$  becomes active. The right-hand side of the equation equals the maximum capacity of routes associated with virtual link v, where C is the maximum capacity of a lightpath.

8) Constraint 8: Fronthaul Delay: The delay in fiber propagation  $l_p$ , electronic switch delay  $l_{el}$ , transmission delay  $l_{tran}$  that depends on the link capacity and request size, and RRH interface delay for the split point  $l_s$  should all be less than or equal to the maximum allowable fronthaul latency  $D_t$  for request type t. In the proposed model, the backhaul latency constraint is not taken into account, as the backhaul latency requirement is significantly less stringent than the fronthaul requirement [39]. This constraint ensures that the latency requirements for each service type request are satisfied.

$$\sum_{p \in \mathbb{P}} (l_p + l_{el} + l_s + l_{tran}) \bar{y}_{r,p} \le D_t, \forall t \in \mathbb{T}, r \in \mathbb{R}_{fn}^{(t)}.$$
 (8)

9) Constraint 9: Backhaul Requests Routing: This constraint ensures that backhaul requests are routed via virtual links beginning at fog nodes (for type 1 requests) and BBU hotels (for types 2 and 3 requests) and ending at the core CO.

$$\sum_{v \in \overline{\mathbb{V}}_{*i}} y_{r,v} - \sum_{v \in \overline{\mathbb{V}}_{i*}} y_{r,v} = \begin{cases} 1 - z_{i,n}, & \text{if } i = o, \ t = \{2,3\} \\ -z_{i,n}, & \text{if } i \in \mathbb{N}_b \setminus o, \ t = \{2,3\} \\ 1, & \text{if } i = o, \ t = \{1\} \\ -\bar{f}_{i,n}, & i \in \mathbb{N}_f, \ t = \{1\} \end{cases}$$

$$\forall n \in \mathbb{N}_c, t \in \mathbb{T}, i \in \mathbb{N}_{fb}, r \in \mathbb{R}_{bi}^{(t)}. \tag{9}$$

If the BBU hotel of a node is placed in the core CO, the first term on the right-hand side becomes 0, indicating that no backhaul traffic is sent. If the BBU hotel for a node is placed in an intermediate CO, backhaul requests are carried out through a virtual link launched from that CO  $(-z_{i,n}=-1)$  and ended at the core CO  $(1-z_{i,n}=1)$ . Backhaul requests of type 1 are transmitted over a virtual link initiated at the fog node (i.e.,  $-\bar{f}_{i,n}=-1$ ) and terminating at the core CO (third term on the right hand side =1).

10) Constraint 10: Fronthaul Requests Routing: This constraint ensures that fronthaul requests are routed via lightpaths that originate at RRHs in CSs and terminate at fog nodes (for type 1 requests) and BBU hotels in COs (for type 2 and type 3 requests)

$$\sum_{p \in \overline{\mathbb{P}}_{*i}} \bar{y}_{r,p} - \sum_{p \in \overline{\mathbb{P}}_{i*}} \bar{y}_{r,p} = \begin{cases} \bar{f}_{i,n}, & \text{if } i \neq \{n, o\}, \ t = \{1\} \\ \bar{z}_{i,n}, & \text{if } i \neq n, \ t = \{2, 3\} \\ -1, & \text{if } i = n \end{cases}$$

$$\forall n \in \mathbb{N}_c, t \in \mathbb{T}, i \in \mathbb{N}, r \in \mathbb{R}_{fn}^{(t)}.$$
(10)

Fronthaul requests are launched by RRHs at the CSs and terminate at the fog nodes for type 1 requests, and at COs where the BBUs hotels of the respective RRHs are activated for type 2 and 3 requests. When a type 1 request is carried over a lightpath from the request generating node n to the fog node i,  $\bar{f}_{i,n} = 1$ 

<span id="page-6-0"></span>indicates that the request has been terminated at i. Similarly,  $z_{i,n}=1$  indicates that request r has been terminated at the BBU location for node n. On the right-hand side of the equation, the third term denotes the generation of requests by the CSs. Thus ensuring that only type 1 fronthaul requests are serviced by fog nodes, while eMBB and mMTC requests are handled by BBU hotels.

# D. Objective Function

The main objective of this work is to reduce the network cost, which is proportional to the number of active BBU hotels and fog nodes, while still conforming to practical network constraints. The deployed fibers affect the network cost, but this factor is not accounted for in the objective function, as the objective of our work is to minimize the number of active nodes. Additionally, the number of fibers per link (each containing multiple wavelengths) is constrained by K. Furthermore, the cost of resource deployment is considered in this work, although the cost of energy consumption is not. The authors present a model for multi-objective optimization in which  $\alpha$  and  $(1-\alpha)$  are the weights of each objective, such that  $\alpha \in (0,1)$ . The objective function is described as follows:

$$\mathcal{Z} = \alpha \sum_{i \in \mathbb{N}_b} \mathbf{b}_i + (1 - \alpha) \sum_{f \in \mathbb{N}_f} \mathbf{x}_f.$$
 (11)

#### E. Optimization Problem

Finally, the proposed optimization problem is expressed as,

OF 1: 
$$\min_{\substack{\mathbf{b}, \mathbf{x}, \bar{\mathbf{F}}, \\ \mathbf{Z}, \mathbf{Y}, \bar{\mathbf{Y}}, \\ \mathbf{U}, \mathbf{o}}} \mathcal{Z}$$
such that

Constraints  $(1) - (10)$ 

$$\mathbf{b} \in \{0, 1\}^{1 \times B}, \ \mathbf{x} \in \{0, 1\}^{1 \times F}$$

$$\bar{\mathbf{F}} \in \{0, 1\}^{F \times N_c}, \ \mathbf{Z} \in \{0, 1\}^{B \times N_c}$$

$$\mathbf{Y} \in \{0, 1\}^{R_b \times V}, \ \bar{\mathbf{Y}} \in \{0, 1\}^{R_f \times P}$$

$$\mathbf{U} \in \{0, 1, \dots, K\}^{P \times L}, \ \mathbf{o} \in \{1, 2, \dots, K\}^{1 \times E} \quad (12)$$

The optimization problem in (12) is an NP-hard problem. It takes real effort to get an optimal solution to an NP-hard problem. Some solvers fairly tackle NP-hard problems and produce near-optimal solutions. However, the technique's complexity scales with network size, making it challenging to get useful results for larger networks in an acceptable timeframe from these solvers. Therefore, we present a low-complexity heuristic algorithm based on a greedy approach. For large-scale network scenarios, the proposed algorithm sufficiently solves the problem with significantly less complexity.

# IV. PROPOSED HEURISTIC SERVICE AWARE BBU HOTEL AND FOG NODE ACTIVATION ALGORITHM (SB-FAA)

We present a low complexity heuristic algorithm for obtaining a near-optimal solution to the optimization problem (12). The

**Algorithm 1:** Service Aware BBU Hotel and Fog Node Activation Algorithm (SB-FAA).

```
Input: Network topology, \mathbb{N} \leftarrow set of nodes, r \leftarrow request of
                type t \in \mathbb{T} from source s
                Define: C_{ab} \leftarrow calculates residual capacity of path
                between node a and b
    Initialization: \mathbf{b} \leftarrow zero(1, B), \mathbf{x} \leftarrow zero(1, F), flag \leftarrow 0
    Output: b, x, F and Z
1 forall r \in \mathbb{R} do
2
           s \leftarrow \text{Request generator source}, t \leftarrow \text{Request type}
3
           if t = 2 or t = 3 then
                 if \sum_{i=1}^{B} z_{i,s} == 0 then
 4
                        forall l \in \{Reachable \ COs \ from \ s\} do
 5
                               P_{sl} \leftarrow \text{Shortest path between } s \text{ and } l
 6
                               Q \leftarrow \text{Delay of } P_{sl}
 7
                               if Q \leq D_t then
 8
                                     \begin{aligned} \mathbf{if} \ \mathcal{C}_{sl} > &= C_f^{(t)} \ \textit{and} \ \{1|l = o, \\ \mathcal{C}_{lo} > &= C_b^{(t)}|l \neq o\} \ \textbf{then} \\ &= z_{l,s} \leftarrow 1, \ b_l \leftarrow 1 \end{aligned}
10
                                            Route r on path P_{so}
11
                                            Break
12
                         if \sum_{i=1}^{B} z_{i,s} == 0 then
13
                              Return request-block
14
15
                        j \leftarrow find(z_{:,s} == 1)
16
                        if C_{sj} >= C_f^{(t)} and \{1|j=o,
17
                          C_{jo} >= C_b^{(t)} | j \neq o \} then Route r on path P_{so}
18
19
                          Return request-block
20
21
22
                   l \in \{Reachable\ COs\ from\ s,\ having\ BBU\ hotels\}
                        Q \leftarrow \text{Delay of path between } s \text{ and } l
23
                        if Q \leq D_t then
24
                              if C_{sl} \ge C_f^{(t)} and \{1|l=o, C_{lo}>=C_b^{(t)}|l \ne o\} then Route r on path P_{so}
25
26
27
                                     flag \leftarrow 1 \implies \mathbf{Break}
                 if flag == 0 then
28
                        forall f \in \mathbb{N}_f do
29
                               if s is connected to f then
30
                                     if C_{sf} \geq C_f^{(t)} and C_{fo} \geq C_b^{(t)} then x_f \leftarrow 1, \ \bar{f}_{sf} \leftarrow 1 Route r on path P_{so}
31
32
33
                                      else
34
                                            Return request-blocked
35
                               Break
```

proposed method is named service aware baseband unit hotel and fog node activation algorithm (SB-FAA) and is described in detail in Algorithm 1. The method minimizes the number of active BBU hotels and fog nodes for all requests and performs grooming routing and wavelength assignment (GRWA) [40]. Additionally, the algorithm aims to minimize blocked requests while enhancing connectivity. The request generating node s

<span id="page-7-0"></span>and its type t are used to characterize an incoming request r. If r represents an eMBB or mMTC request, the algorithm determines whether s is associated with an active BBU hotel. If such an association does not exist, the algorithm determines all COs that are reachable from node s. The shortest path is computed between node s and candidate CO, and the path length is calculated using the Dijkstra algorithm [41], (step 1–7). The path length is used to calculate the required latency, which includes interface delay  $l_s$  at RRH due to the employed split, propagation delay  $l_p$ , the transmission delay  $l_{tran}$ , as well as delay due to electronic switches  $l_{el}$ . If the required latency is less than the maximum allowable fronthaul latency, the residual capacity of the path is evaluated. If the path has enough capacity to transport both  $C_f^{(t)}$  and  $C_b^{(t)}$ , then s is associated with the candidate CO. If candidate CO does not already have an active BBU hotel, it is activated and r is routed through the computed path (steps 8–12). If no node is capable of hosting BBU for the request-generating node s, the request is blocked (steps 13–14). The algorithm assesses whether s is associated with an active BBU hotel upon receipt of request r. If such an association exists, the algorithm determines location of BBU hotel for s using the find function. The algorithm then determines the residual capacity of the links along the determined path. If the capacity is sufficient to transport both  $C_f^{(t)}$  and  $C_b^{(t)}$ , r will be transported via that path; otherwise, the request will be blocked (steps 16-20).

If the request r is of type 1, the algorithm determines whether it can be processed at an active CO. The distance between s and active COs is calculated. The path delay is calculated using the calculated path length. The path is used to route r if its latency is less than the maximum allowable fronthaul latency  $D_t$  and the capacity of the path's links is sufficient to carry r (steps 22–27). If no active CO satisfies r, the algorithm calculates the residual capacity in the link between s and the fog node f, as well as the link between f and f0 (steps 28–31). If sufficient capacity is available, the fog node that f0 is connected to is activated if it was not active already, and f1 is routed along the computed path (steps 32–33). f3 is blocked if f3 is unable to satisfy f3 (steps 34–35).

The if statement on step 30 and the break statement on step **36** ensure that each RRH is connected to a single fog node, as in (1), whereas **steps 4** and **12** satisfy (2). The constraints in (3) and (4) are established on **steps 32** and **11**, respectively, where we ensure that each fog node/BBU hotel serve an RRH only if it is active. Each link in the proposed system and network topology can have a maximum of K fibers. The constraints in (6) and (7) are satisfied in steps 9, 17, 25, and 31. The algorithm ensures that a request is only routed if the link capacity of paths between RRH and fog node/BBU hotel and core CO is sufficient. The fronthaul delay constraint in (8) is satisfied in steps 8 and 24. These steps ensure that each service type's latency requirements are met. The steps 11, 18, 26, and 33 ensure the routing of fronthaul and backhaul requests between RRH and fog node/BBU hotels, and between fog node/BBU hotels and the core CO, respectively, satisfying the constraints in (9) and (10).

#### A. Computational Complexity

The complexity of the algorithm is frequently expressed in float-point operations (FLOPS). Since FLOPS are machine-independent, they provide a fair method for conducting a precise and reliable complexity analysis.

The proposed algorithm can be divided into 2 major blocks, namely block 1 (steps 1–20) and block 2 (steps 21–36). Given the fact that the blocks are mutually exclusive, they can never run concurrently. The first block contains a for loop that executes up to B times, where B is the total number of nodes equipped with BBU hotel. Dijkstra Algorithm is used to find the shortest path inside the loop. It has a worst-case complexity of  $N^2$ , where N is the total number of nodes. There are approximately ten assignments within the loop, and assuming one FLOPS for each assignment, there will be a total of ten FLOPS. The block from steps 16-20 contains simple assignments and requires a total of 5 FLOPS. As a result, the complexity of block 1 in the worst-case scenario is  $\approx (10 \ N^2)B$ . There is a for loop in block 2 from steps 22-27. The loop executes a maximum of B times. There are approximately eight assignments within the loop. As a result, the complexity of this for loop is approximately 8B. At steps 29–36, the for loop executes F times, where F is the total number of fog nodes. There are seven assignments contained within the loop. As a result, this loop's complexity is 7F. Block 2's total complexity will be  $\approx 8B + 7F$ . Finally, the proposed algorithm's worst-case complexity is specified as  $\approx R(\max\{(10 N^2)B, 8B + 7F\})$ , where R is the total number of requests. It is evident that the complexity of the proposed algorithm is significantly less than the exhaustive search algorithm.

#### V. RESULTS & DISCUSSIONS

The results of the ILP and heuristic algorithms are discussed in this section. The AMPL+CPLEX is used to solve the ILP. The computer simulations for the proposed heuristic algorithm are performed using the Python programming language and the Networkx library.

## A. Simulation Parameters

To solve the ILP model proposed in Section III, we consider a network of 30 nodes divided into 13 macro CSs, 7 COs including a core CO, and 10 fog nodes. These nodes are evenly distributed over a 150 km<sup>2</sup> suburban geographical area [42]. Furthermore, the nodes are linked to one another via optical fiber links with a maximum of one fiber per link, i.e., K = 1. Each fiber link can support eight wavelengths at a rate of 10 Gbps. To provide wavelength isolation for each slice type, four wavelengths are dedicated to eMBB requests, and two wavelengths each to URLLC and mMTC requests. Due to the increased capacity requirement compared to URLLC and mMTC, additional wavelengths are dedicated to eMBB requests. Each slice type generates a total of 500 traffic requests. These requests are distributed uniformly across all CSs. While we examine split option 7 for fronthaul traffic transmission, the fronthaul capacity required for each URLLC, eMBB, and mMTC request is 120 Mbps, 720 Mbps,

![](_page_8_Figure_2.jpeg)

Fig. 4. Number of active nodes for ILP. (a) 3-layer architecture. (b) 2-layer architecture.

TABLE II
LATENCY REQUIREMENT OF FRONT/BACKHAUL FOR EACH SLICE TYPE [29]

| Request | Type | Fronthaul Latency | Backhaul Latency |
|---------|------|-------------------|------------------|
| URLLC   | 1    | $\leq 50\mu s$    | $\leq 500 \mu s$ |
| eMBB    | 2    | $\leq 100 \mu s$  | $\leq 20ms$      |
| mMTC    | 3    | $\leq 250 \mu s$  | $\leq 20ms$      |

and 80 Mbps, respectively [30]. The required backhaul for URLLC and mMTC requests is uniformly distributed between 10 and 20 Mbps, whereas the required backhaul for eMBB requests is 240 Mbps. Table II shows the required fronthaul and backhaul latencies for each request type. The fronthaul latency for URLLC, eMBB, and mMTC requests, respectively, is less than  $50 \,\mu$  s,  $100 \,\mu$ s, and  $250 \,\mu$ s. The delay caused by an electronic switch is  $20 \,\mu$ s, while the interface delay at RRH for split option 7 is  $25 \,\mu$ s [43].

## B. Simulation Results

The proposed three-layer CF-RAN over WDM architecture is evaluated in terms of active nodes, fronthaul delay, and the total number of requests served. The optimization goal is to minimize the number of active BBU hotels and fog nodes in the network while adhering to practical network constraints.

The proposed 3-layer architecture is compared to the two-layer architecture in terms of the total number of active BBU and fog nodes for three slice types, as shown in Fig. 4(a) and (b). As can be seen, both approaches result in an increase in the total number of active nodes as traffic increases. The proposed architecture behaves identically to the two-layer architecture in terms of eMBB and mMTC requests, as both approaches serve these requests via BBU hotels. The URLLC slice type results in a significant reduction in activated nodes because the same amount of traffic can be routed through fewer activated fog nodes. As traffic increases, the 2-layer approach no longer provides a feasible solution. On the other hand, CF-RAN over WDM can provide a viable solution for all generated requests without activating all available fog nodes.

![](_page_8_Figure_10.jpeg)

Fig. 5. Comparison between 2-layer and 3-Layer in terms of total fronthaul delay for ILP.

The comparison of the proposed three-layer design to the two-layer architecture for three slice types in terms of total fronthaul delay is shown in Fig. 5. As illustrated in Fig. 5, the total fronthaul delay is nearly identical for the mMTC and eMBB slice types. The 3-layer technique achieves a 10% improvement for the URLLC slice type. Additionally, the two-layer architecture is unable to provide a feasible solution under huge traffic loads. To comply with the delay constraints, URLLC requests are always executed at nearby fog nodes. Due to the large distance between the CSs and the BBU nodes, a significant fronthaul delay is induced, making it hard to execute URLLC requests at the BBU nodes.

# C. Performance Evaluation of Proposed SB-FAA

To evaluate the performance of the heuristic algorithm, we consider a network that consists of 140 nodes divided into

![](_page_9_Figure_2.jpeg)

Fig. 6. Comparison between 2-layer and 3-layer architecture in terms of total fronthaul delay for heuristic algorithm.

70 Macro CSs, 30 COs including a core CO, and 40 fog nodes. These nodes are evenly distributed across a 300 km<sup>2</sup> sub-urban geographical area. Furthermore, the nodes are linked by optical fiber links, with a maximum of one fiber per link. Each fiber link can support 16 wavelengths at 40 Gbps each.

To provide wavelength isolation for each slice type, eight wavelengths are reserved for eMBB requests and four for URLLC and mMTC requests, respectively. We randomly generate the arrival of 5000 traffic requests for each slice type. These 5000 requests are uniformly distributed among all RRHs. Each CO contains a BBU hotel that is activated upon the receipt of a request. Similarly, each fog node can process baseband traffic and is triggered in response to the receipt of a type 1 request. A Monte Carlo simulation is performed to average the results of random simulations.

Fig. 6 compares the performance of the proposed 3-layer architecture to the 2-layer architecture for three slice types in terms of fronthaul delay. For eMBB and mMTC, the two architectures provide about comparable performance with a small number of requests, with just a minor improvement with CF-RAN over WDM for large number of requests. This is because like in 2-layer architecture, eMBB and mMTC requests are processed at BBU hotels in CF-RAN over WDM. As with ILP, the maximum 10% gain in fronthaul delay for the URLLC slice type can be observed because type 1 requests are catered at fog nodes in CF-RAN over WDM, as opposed to the 2-layer architecture.

The total number of active nodes in terms of total requests is depicted in Fig. 7 for both 3-layer and 2-layer architectures. As illustrated in Fig. 7, more nodes are activated as the number of requests increases for both architectures. Additionally, the number of active BBU hotels is the same for both approaches in the case of eMBB and mMTC slices. In both architectures, the eMBB and mMTC requests are satisfied by the BBU hotels, and hence the required number of BBU hotels is equal. A notable difference of 33% in the number of active nodes is observed for

![](_page_9_Figure_8.jpeg)

Fig. 7. Comparison between 2-layer and 3-layer architecture in terms of number of active nodes for heuristic algorithm.

![](_page_9_Figure_10.jpeg)

Fig. 8. Request blockage rate for 3-layer approach.

URLLC requests. This is because, in the proposed architecture, URLLC requests are always served by fog nodes, unless the request generating node is connected to an already-active BBU hotel. The request generating node must be connected to the active BBU node through a path that satisfies the required latency constraint in this case. Each fog node serves multiple RRHs and are placed closer to the RRH thus satisfying the fronthaul delay constraint. On the other hand, in 2-layer architecture more BBU hotels closer to the RRHs are activated to satisfy fronthaul latency constraint. Thus, resulting in the activation of higher number of nodes.

Fig. 8 depicts the request blockage percentage with respect to the increasing number of active BBU hotels and traffic for the proposed 3-layer CF-RAN over WDM architecture. The request blocking is higher when fewer BBU hotels are active in the network, especially for higher traffic. The request blocking percentage is reduced with the increase in the number of active

![](_page_10_Figure_2.jpeg)

Fig. 9. Comparison of 3- and 2-layer approaches in terms of served requests vs. the total number of BBU hotels.

![](_page_10_Figure_4.jpeg)

Fig. 10. Comparison of 3- and 2-layer approaches in terms of served requests vs. the total number of requests.

BBU hotels, and no request is blocked when the number of active BBU hotels is increased.

Another important metric for validating the proposed architecture is the percentage of served requests. Figs. 9 and 10 compare the proposed 3-layer architecture to the 2-layer approach in terms of the percentage of requests served. In both cases, we set the same number of active BBU hotels represented by B in Fig. 10. As can be seen in both figures, an increase in the number of requests reduces the percentage of requests served when the number of active BBU hotels is lower in both cases. The request serving percentage increases in both cases as we increase the number of active BBU hotels. However, the proposed CF-RAN over WDM provides up to 20% greater network connectivity than the 2-layer approach with significantly fewer active BBU hotels.

![](_page_10_Figure_8.jpeg)

Fig. 11. Comparison between the ILP and heuristic algorithm.

# *D. Comparison Between ILP and SB-FAA*

The proposed heuristic algorithm is compared with the B&B algorithm in terms of the total number of active nodes. The B&B algorithm can find the exact solution for a variety of optimization problems. The algorithm traverses the whole search space using a tree search technique and filters solutions that do not lead to further optimization. The performance of the algorithm may be regulated by defining three crucial components, i.e., the search technique, the branching strategy, and the pruning rules. The B&B algorithm is a fundamental and commonly employed technique for obtaining optimal solutions to non-deterministic polynomial time (NP)-hard optimization problems. The method divides the problem under consideration into subproblems by storing the partial solutions in a tree structure. The tree nodes generate new children by subdividing the search space into smaller regions. The branching approach is then employed to address these regions recursively. In addition, pruning rules are used to eliminate suboptimal solutions. This process is known as bounding. After examining the entire tree, the optimal solution is returned [\[44\].](#page-13-0)

We consider a network of 30 nodes divided into 13 Macro CSs, 7 COs, including a core COs, and 10 fog nodes. Once again, the nodes are uniformly distributed across a 50 km2 region. For a fair comparison, we consider the same parameters and network scenarios in both architectures. For the 3-layer architecture, the comparison is provided in terms of the number of active fog nodes and BBU hotels in the network. As shown in Fig. 11, the number of active nodes increases as the number of requests increases for both techniques. For higher traffic loads, ILP slightly beats SB-FAA for URLLC and eMBB type requests, whereas for mMTC traffic, both techniques provide comparable results. The near-optimal performance of the proposed heuristic SB-FAA demonstrates that CF-RAN over WDM outperforms the traditional 2-layer approach regardless of the technique used. Therefore, it is obvious that the proposed algorithm performs comparably to the B&B, which employs an optimal exhaustive search approach.

<span id="page-11-0"></span>![](_page_11_Figure_2.jpeg)

Fig. 12. Number of active nodes w.r.t. total number of requests for ILP in 3-layer architecture for different  $\alpha$  values. (a)  $\alpha = 0.25$ . (b)  $\alpha = 0.5$ . (c)  $\alpha = 0.75$ .

# E. Comparison of Results With Different Optimization Objective

The proposed system model describes a multi-objective problem, with  $\alpha$  representing the relative weight of each objective. Although the optimal value of  $\alpha$  has a considerable impact on the performance of the system, this work is limited to only fixed values of  $\alpha$ . The performance is measured using various fixed  $\alpha$  values.

Further simulations of the ILP are conducted with  $\alpha=\{0.25,0.5,0.75\}$  to determine  $\alpha$ 's effect on the proposed system. Fig. 12 demonstrates the results of ILP in terms of the number of active nodes. As depicted in Fig. 12, the number of active nodes increases with an increase in traffic for all  $\alpha$  values, but the number of active nodes for each service type varies with the variation in  $\alpha$ . In Fig. 12(a), the minimization of fog nodes is assigned a greater weight when  $\alpha=0.25$ . As URLLC requests are serviced by fog nodes, a smaller number of nodes are activated to serve URLLC requests than in the cases where  $\alpha=0.5$  and  $\alpha=0.75$ . The number of activated nodes for eMBB and mMTC requests decreases as  $\alpha$  increases, and fewer BBU hotels are activated at  $\alpha=0.75$ .

It is obvious that variations in  $\alpha$  influence network performance. Most of the results in this work are evaluated for  $\alpha=0.5$  because the main goal of our work is to minimize network cost, which is largely dependent on both the number of active fog nodes and BBU hotels at the same time.

#### F. Convergence Analysis

The algorithm's convergence is depicted in Fig. 13. In this scenario, a network of 70 nodes consisting of 40 BBU hotels and 30 fog nodes is considered. In addition, 1000 requests are considered. The x-axis represents the request index, while the y-axis provides the normalized values for each plot. The request indices (x-axis) correspond to the *forall*  $R \in \mathbb{R}$  loop in the Algorithm 1. It can be seen that around 0.25% of nodes are activated to fulfill approximately 98% of requests. A new metric is introduced to demonstrate the algorithm's convergence. Assuming that a and b denote the normalized number of activated nodes and the normalized number of requests served,

![](_page_11_Figure_10.jpeg)

Fig. 13. Convergence of Algorithm 1.

respectively. Consequently, c represents the ratio of active nodes to requests served, i.e.,  $c = \frac{a}{b}$ . The goal is to serve the highest proportion of requests with the fewest number of nodes. In the convergence plot, it can be observed that when the request index increases, the value of c drops drastically, demonstrating the convergence of the proposed algorithm.

# VI. CONCLUSION

We proposed a novel CF-RAN over WDM architecture in this work to address the stringent requirements of the URLLC, eMBB and mMTC services. For CF-RAN over WDM architecture deployment, we jointly optimize the BBU hotel and fog node activation problem. The fog nodes handle URLLC traffic that requires low latency, whereas the eMBB and mMTC traffic is handled by the BBU hotels. In addition, each request type has its own set of wavelengths. We presented a mathematical model based on ILP that reduces network costs by using the minimum number of active BBU hotels and fog nodes while serving the maximum number of requests. Furthermore, for realistic

<span id="page-12-0"></span>network scenarios, we present a low-complexity, greedy-based heuristic algorithm. The results achieved using the CF-RAN over WDM architecture are compared to the conventional 2-layer centralization architecture. According to simulation results, the proposed architecture outperforms the existing 2-layer architecture in terms of hotel centralization, fronthaul delay, and overall network connection. As URLLC requests are handled at the fog nodes in the proposed architecture, a substantial reduction in the number of active BBU hotels is noticed, providing a notable gain in terms of network deployment cost. Furthermore, as compared to the typical 2-layer technique, results show a significant improvement in fronthaul latency and network connectivity for all slice types.

We intend to continue our work and integrate the SDN controller into the BBU cloud in the CF-RAN architecture in the future. Moreover, the optimal value of  $\alpha$  would have a significant impact on the system's performance. Although in this work we are dealing with fixed  $\alpha$  values, in the future we want to optimize the value of  $\alpha$  in order to gain a deeper insight of the proposed system.

#### REFERENCES

- [1] N. Alliance, "5G white paper," Next generation mobile networks, White Paper, vol. 1, 2015. [Online]. Available: https://www.ngmn.org/publications/ngmn-5g-white-paper.html
- [2] T. Fehrenbach, R. Datta, B. Göktepe, T. Wirth, and C. Hellge, "URLLC services in 5G low latency enhancements for LTE," in *Proc. IEEE 88th Veh. Technol. Conf.*, 2018, pp. 1–6.
- [3] J. Mazgula, J. Sapis, U. S. Hashmi, and H. Viswanathan, "Ultra reliable low latency communications in mmWave for factory floor automation," *J. Indian Inst. Sci.*, vol. 100, no. 2, pp. 303–314, 2020.
- [4] R. Kassab, O. Simeone, and P. Popovski, "Coexistence of uRLLC and eMBB services in the C-RAN uplink: An information-theoretic study," in *Proc. IEEE Glob. Commun. Conf.*, 2018, pp. 1–6.
- [5] N. H. Mahmood, M. Lauridsen, G. Berardinelli, D. Catania, and P. Mogensen, "Radio resource management techniques for eMBB and mMTC services in 5G dense small cell scenarios," in *Proc. IEEE 84th Veh. Technol. Conf.*, 2016, pp. 1–5.
- [6] X. Foukas, G. Patounas, A. Elmokashfi, and M. K. Marina, "Network slicing in 5G: Survey and challenges," *IEEE Commun. Mag.*, vol. 55, no. 5, pp. 94–100, May 2017.
- [7] M. Kalil, A. Moubayed, A. Shami, and A. Al-Dweik, "Efficient low-complexity scheduler for wireless resource virtualization," *IEEE Wireless Commun. Lett.*, vol. 5, no. 1, pp. 56–59, Feb. 2016.
- [8] M. Kalil, A. Al-Dweik, M. F. Abu Sharkh, A. Shami, and A. Refaey, "A framework for joint wireless network virtualization and cloud radio access networks for next generation wireless networks," *IEEE Access*, vol. 5, pp. 20814–20827, 2017.
- [9] M. Ahsan, A. Ahmed, A. Al-Dweik, and A. Ahmad, "Functional split-aware optimal BBU placement for 5G cloud-RAN over WDM access/aggregation network," *IEEE Syst. J.*, vol. 17, no. 1, pp. 122–133, Mar. 2023. doi: 10.1109/JSYST.2022.3150468.
- [10] J. Wu, Z. Zhang, Y. Hong, and Y. Wen, "Cloud radio access network (C-RAN): A primer," *IEEE Netw.*, vol. 29, no. 1, pp. 35–41, Jan./Feb. 2015
- [11] L. M. P. Larsen, A. Checko, and H. L. Christiansen, "A survey of the functional splits proposed for 5G mobile crosshaul networks," *IEEE Commun. Surv. Tut.*, vol. 21, no. 1, pp. 146–172, Firstquarter 2019.
- [12] U. S. Hashmi, S. A. R. Zaidi, A. Darbandi, and A. Imran, "On the efficiency tradeoffs in user-centric cloud RAN," in *Proc. IEEE Int. Conf. Commun.*, 2018, pp. 1–7.
- [13] F. Tan, P. WU, Y-C. Wu, and M. Xia, "Cooperative beamforming for wireless fronthaul and access links in ultra-dense C-RANs with SWIPT: A first-order approach," *IEEE J. Sel. Topics Signal Process.*, vol. 15, no. 5, pp. 1242–1257, Aug. 2021.
- [14] C. C. Erazo-Agredo, M. Garza-Fabre, R. A. Calvo, L. Diez, J. Serrat, and J. Rubio-Loyola, "Joint route selection and split level management for 5G C-RAN," *IEEE Trans. Netw. Serv. Manage.*, vol. 18, no. 4, pp. 4616–4638, Dec. 2021

- [15] Ericsson, "Common public radio interface (CPRI); interface specification v7.0," CPRI Consortium, Ericsson, Huawei, NEC, Nokia, Nortel, and Siemens, Tech. Rep., 2015. [Online]. Available: http://www.cpri.info/ downloads/CPRI\_v\_7\_0\_2015-10-09.pdf
- [16] 3GPP, "Study on new radio access technology: Radio access architecture and interfaces v14.0.0 (2017-03)," Tech. Rep., 2017. [Online]. Available: https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3056
- [17] B. Brik, K. Boutiba, and A. Ksentini, "Deep learning for B5G open radio access network: Evolution, survey, case studies, and challenges," *IEEE Open J. Commun. Soc.*, vol. 3, pp. 228–250, 2022.
- [18] R. I. Tinini, D. M. Batista, G. B. Figueiredo, M. Tornatore, and B. Mukherjee, "Low-latency and energy-efficient BBU placement and VPON formation in virtualized cloud-fog RAN," *IEEE J. Opt. Commun. Netw.*, vol. 11, no. 4, pp. B37–B48, Apr. 2019.
- [19] A. Checko et al., "Cloud RAN for mobile networks A technology overview," *IEEE Commun. Surv. Tut.*, vol. 17, no. 1, pp. 405–426, Firstquarter 2015.
- [20] D. Harutyunyan and R. Riggio, "How to migrate from operational LTE/LTE-A networks to C-RAN with minimal investment?," *IEEE Trans. Netw. Serv. Manage.*, vol. 15, no. 4, pp. 1503–1515, Dec. 2018.
- [21] M. Khan, R. S. Alhumaima, and H. S. Al-Raweshidy, "QoS-aware dynamic RRH allocation in a self-optimized cloud radio access network with RRH proximity constraint," *IEEE Trans. Netw. Serv. Manage.*, vol. 14, no. 3, pp. 730–744, Sep. 2017.
- [22] H. Zhang and V. W. S. Wong, "A two-timescale approach for network slicing in C-RAN," *IEEE Trans. Veh. Technol.*, vol. 69, no. 6, pp. 6656–6669, Jun. 2020.
- [23] J. Khamse-Ashari, G. Senarath, I. Bor-Yaliniz, and H. Yanikomeroglu, "An agile and distributed mechanism for inter-domain network slicing in next-generation mobile networks," *IEEE Trans. Mobile Comput.*, vol. 21, no. 10, pp. 3486–3501, Oct. 2022.
- [24] B. Ojaghi, F. Adelantado, A. Antonopoulos, and C. Verikoukis, "Slice-dRAN: Service-aware network slicing framework for 5G radio access networks," *IEEE Syst. J.*, vol. 16, no. 2, pp. 2556–2567, Jun. 2022.
- [25] S. Costanzo, I. Fajjari, N. Aitsaadi, and R. Langar, "Dynamic network slicing for 5G IoT and eMBB services: A new design with prototype and implementation results," in *Proc. IEEE 3rd Cloudification Internet Things*, 2018. pp. 1–7.
- [26] Y. Xiao, J. Zhang, and Y. Ji, "Energy-efficient DU-CU deployment and lightpath provisioning for service-oriented 5G metro access/aggregation networks," J. Lightw. Technol., vol. 39, no. 17, pp. 5347–5361, Sep. 2021.
- [27] H. Yu, F. Musumeci, J. Zhang, Y. Xiao, M. Tornatore, and Y. Ji, "DU/CU placement for C-RAN over optical metro-aggregation networks," in *Proc. Int. IFIP Conf. Opt. Netw. Des. Model.*, 2019, pp. 82–93.
- [28] A. Marotta, D. Cassioli, M. Tornatore, Y. Hirota, Y. Awaji, and B. Mukherjee, "Reliable slicing with isolation in optical metro-aggregation networks," in *Proc. Opt. Fiber Commun. Conf. Exhib.*, 2020, pp. 1–3.
- [29] H. Yu, F. Musumeci, J. Zhang, M. Tornatore, and Y. Ji, "Isolation-aware 5G RAN slice mapping over WDM metro-aggregation networks," *J. Lightw. Technol.*, vol. 38, no. 6, pp. 1125–1137, Mar. 2020.
- [30] C. Song et al., "Hierarchical edge cloud enabling network slicing for 5G optical fronthaul," *IEEE J. Opt. Commun. Netw.*, vol. 11, no. 4, pp. B60–B70, Apr. 2019.
- [31] A. De Domenico, Y.-F. Liu, and W. Yu, "Optimal virtual network function deployment for 5G network slicing in a hybrid cloud infrastructure," *IEEE Trans. Wireless Commun.*, vol. 19, no. 12, pp. 7942–7956, Dec. 2020.
- [32] A. Ahmad, A. Bianco, and E. Bonetto, "Traffic grooming and energy-efficiency in flexible-grid networks," in *Proc. IEEE Int. Conf. Commun.*, 2014, pp. 3264–3269.
- [33] ITU-T, "5G wireless fronthaul requirements in a PON context," *Int. Telecommun. Union*, ITU-T Supplement G.Sup66, 2020. [Online]. Available: https://www.itu.int/rec/T-REC-G.Sup66-202009-I/en
- [34] A. Checko, A. P. Avramova, M. S. Berger, and H. L. Christiansen, "Evaluating C-RAN fronthaul functional splits in terms of network level energy and cost savings," *J. Commun. Netw.*, vol. 18, no. 2, pp. 162–172, Apr. 2016.
- [35] G. O. Pérez, D. L. López, and J. A. Hernández, "5G new radio fronthaul network design for eCPRI-IEEE 802.1 CM and extreme latency percentiles," *IEEE Access*, vol. 7, pp. 82218–82230, 2019.
- [36] J.-P. Elbers and J. Zou, "A flexible X-haul network for 5G and beyond," in *Proc. IEEE 24th OptoElectron. Commun. Int. Conf. Photon. Switching Comput.*, 2019, pp. 1–3.
- [37] A. Ahmad, A. Bianco, E. Bonetto, M. Garrich, and J. R. F. Oliveira, "Switching node architectures in flexible-grid networks: A performance comparison," in *Proc. IEEE Int. Conf. Opt. Netw. Des. Model.*, 2014, pp. 49–54

- <span id="page-13-0"></span>[38] T. A. Strasser and J. L. Wagener, "Wavelength-selective switches for ROADM applications," *IEEE J. Sel. Topics Quantum Electron.*, vol. 16, no. 5, pp. 1150–1157, Sep./Oct. 2010.
- [39] P.-H. Kuo and A. Mourad, "Millimeter wave for 5G mobile fronthaul and backhaul," in *Proc. IEEE Eur. Conf. Netw. Commun*, 2017, pp. 1–5.
- [40] A. Ahmad, A. Bianco, H. Chouman, V. Curri, G. Marchetto, and S. Tahir, "A transmission layer aware network design for fixed and flexible grid optical networks," in *Proc. IEEE 17th Int. Conf. Transparent Opt. Netw.*, 2015, pp. 1–4.
- [41] D. B. Johnson, "A note on Dijkstra's shortest path algorithm," *J. ACM*, vol. 20, no. 3, pp. 385–388, 1973.
- [42] F. Musumeci, C. Bellanzon, N. Carapellese, M. Tornatore, A. Pattavina, and S. Gosselin, "Optimal BBU placement for 5G C-RAN deployment over WDM aggregation networks," *J. Lightw. Technol.*, vol. 34, no. 8, pp. 1963–1970, Apr. 2016.
- [43] Y. Alfadhli et al., "Latency performance analysis of low layers function split for URLLC applications in 5G networks," *Comput. Netw.*, vol. 162, 2019, Art. no. 106865.
- [44] D. R. Morrison, S. H. Jacobson, J. J. Sauppe, and E. C. Sewell, "Branchand-bound algorithms: A survey of recent advances in searching, branching, and pruning," *Discrete Optim.*, vol. 19, pp. 79–102, 2016.

![](_page_13_Picture_9.jpeg)

**Muhammad Ahsan** received the Master of Science degree in electrical engineering from the National University of Sciences and Technology (NUST), Islamabad, Pakistan, in 2021. He is currently working toward the Ph.D. degree with the Interdisciplinary Centre for Security, Reliability, and Trust (SnT), University of Luxembourg, Esch-sur-Alzette, Luxembourg. He was a Researcher with NUST Optical Networks and Technologies Lab and an Assistant Manager with the Largest Telecom Operator (PTCL) in Pakistan. His research interests include encom-

pass 6G non-terrestrial networks, network slicing, open RAN, cloud RAN, resource allocation, and network optimization. He has practical experience in the simulation and modeling of optimization problems, as well as proficiency in optimization tools, such as CPLEX and MATLAB.

![](_page_13_Picture_12.jpeg)

**Ashfaq Ahmed** (Senior Member, IEEE) received the M.S. and Ph.D. degrees from the Department of Electronics and Telecommunications, Politecnico di Torino, Torino, Italy, in 2010 and 2014, respectively. He is currently affiliated with the Center for Cyber-Physical Systems (C2PS), Department of Electrical Engineering and Computer Science, Khalifa University, Abu Dhabi, UAE. From March 2014 to March 2021, he was an Assistant Professor with the Department of Electrical and Computer Engineering, COM-SATS University Islamabad, Wah Campus, Pakistan.

His research interests include hardware security, security protocols, computational intelligence, evolutionary algorithms, convex optimization, resource allocation, and applied optimization for 5G and beyond 5G applications, cloud computing, and physical layer wireless communication. He has hands-on experience with simulation and modeling of optimization problems, as well as working with a variety of optimization toolboxes, including the MATLAB optimization toolbox and the OPTI toolbox. He also developed heuristics and applied several meta-heuristics to various optimization problems.

![](_page_13_Picture_15.jpeg)

**Huma Fida Abbasi** received the master's degree in information technology from the National University of Sciences and Technology, Islamabad, Pakistan. From July 2019 to November 2022, she was a Software Test Engineer with Deloitte in the United States. She is currently employed by Reach PLC, a leading news Publisher in the United Kingdom. Her main research interests revolve around 5G technology and network slicing.

![](_page_13_Picture_17.jpeg)

**Arafat Al-Dweik** (Senior Member, IEEE) received the M.S. (*Summa Cum Laude*) and Ph.D. (*Magna Cum Laude*) degrees in electrical engineering from Cleveland State University, Cleveland, OH, USA, in 1998 and 2001, respectively. He is currently with the Department of Electrical Engineering and Computer Science, Khalifa University, Abu Dhabi, UAE. He was also with Efficient Channel Coding, Inc., Cleveland, Department of Information Technology, Arab American University, Jenin, Palestine, and University of Guelph, Guelph, ON, Canada. He is currently a

Visiting Research Fellow with the School of Electrical, Electronic, and Computer Engineering, Newcastle University, Newcastle upon Tyne, U.K, and a Research Professor with Western University, London, ON, Canada, and University of Guelph. He has extensive research experience in various areas of wireless communications that include modulation techniques, channel modeling and characterization, synchronization and channel estimation techniques, OFDM technology, error detection and correction techniques, MIMO, and resource allocation for wireless networks. Dr. Al-Dweik is an Associate Editor for the IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY and *IET Communications*. He is a Member of Tau Beta Pi and Eta Kappa Nu. From 1997 to 1999, he was awarded the Fulbright Scholarship. He was the recipient of the Hijjawi Award for Applied Sciences in 2003, Fulbright Alumni Development Grant in 2003 and 2005, Dubai Award for Sustainable Transportation in 2016, UAE Leader-Founder Award in 2019. He is a Registered Professional Engineer in the Province of Ontario, Canada.

![](_page_13_Picture_20.jpeg)

**Umair Sajid Hashmi** (Member, IEEE) received the B.S. degree in electronics engineering from the GIK Institute of Engineering Sciences and Technology, Topi, Pakistan, in 2008, the M.Sc. degree in advanced distributed systems from the University of Leicester, Leicester, U.K., in 2010, and the Ph.D. degree in electrical and computer engineering from the University of Oklahoma, Tulsa, OK, USA, in 2019. During his Ph.D. degree, he was a Graduate Research Assistant with the AI4Networks Research Center. He was also with AT&T and Nokia Bell Labs, on multiple research

internships and co-ops. Since 2019, he was an Assistant Professor with the School of Electrical Engineering and Computer Science, National University of Sciences and Technology, Islamabad, Pakistan, where his focus is on the broad area of 5G wireless networks and application of artificial intelligence toward system-level performance optimization of wireless networks, and health care applications. He is currently with the Advanced Wireless Technologies, Dell Technologies, Canada, on design and implementation of AI / ML applications within Open RAN reference architecture. He has authored or coauthored 20 technical papers in high impact journals and proceedings of IEEE flagship conferences on communications. He has been involved in four NSF funded projects on 5G SON with a combined award worth of four million. He also contributed as a co-PI on more than an Erasmus Consortium Project titled Capacity Building for Digital Health Monitoring and Care Systems in Asia-DigiHealth-Asia. Since 2020, he has been the Review Editor of IoT and Sensor Networks stream in the *Frontiers in Communications and Networks* journal.

![](_page_13_Picture_23.jpeg)

**Arsalan Ahmad** (Senior Member, IEEE) received the M.Sc. degree in communication engineering and the Ph.D. degree in electronics and communication engineering from Politecnico di Torino, Turin, Italy, in 2010 and 2014, respectively. Later he was a Postdoc with Politecnico di Torino, and Research Fellow with CONNECT Research Centre, Trinity College Dublin, Dublin, Ireland. In 2015, he joined the National University of Sciences and Technology (NUST), Pakistan. He is currently an Associate Professor and the Director and Principal Investigator (PI) of Optical

Networks and Technologies (ONT) Lab, NUST. Since January 2023, he has been a Visiting Professor with the Department of Electrical and Computer Engineering, Oklahoma State University, Stillwater, OK, USA. His main research interests include optical networks, network planning, virtual PONs, network slicing, and software defined networking.
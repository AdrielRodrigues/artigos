---
title: "Low-latency partial resource offloading in cloud-edge elastic optical networks"
tema_principal: 5g6g
temas_relacionados: []
ano: 2024
autores: []
veiculo: null
pdf: ../pdf/low-latency_partial_resource_offloading_in_cloud-edge_elastic_optical_networks.pdf
---

# Low-latency partial resource offloading in cloud-edge elastic optical networks

**Bowen Chen,1, \* Ling Liu,<sup>1</sup> Yuexuan Fan,<sup>1</sup> Weidong Shao,<sup>1</sup> Mingyi Gao,<sup>1</sup> Hong Chen,<sup>1</sup> Weiguo Ju,<sup>2</sup> Pin-Han Ho,<sup>3</sup> Jason P. Jue,<sup>4</sup> AND Gangxiang Shen<sup>1</sup>**

<sup>1</sup>School of Electronic and Information Engineering, Soochow University, Suzhou, Jiangsu Province, 215006, China

Received 10 July 2023; revised 19 October 2023; accepted 28 November 2023; published 24 January 2024

**In the context of the rapid deployment of IoT, 5G, and cloud computing, numerous emerging applications demand efficient networked computing capacity for task offloading from mobile and IoT users. This paper focuses on the optimization of network resource allocation and reduction of end-to-end (E2E) latency through the strategic decision of whether and where to offload user requests in a cloud-edge elastic optical network (CE-EON). To address this problem, we first formulate the problem into an integer linear programming (ILP) model as an initial solution. Additionally, we introduce several heuristic approaches that leverage the concept of partial resource offloading, specifically based on proportional segmentation (PRO\_PS), partial resource offloading based on average segmentation (PRO\_AS), all resource offloading (ARO), and all local processing (ALP). Furthermore, we implement a collaborative cloud-edge (CCE) offloading approach as a baseline for comparison. Our results demonstrate that the PRO\_PS approach closely approximates the optimal solutions obtained from the ILP model in static scenarios. Moreover, the PRO\_PS approach achieves the lowest E2E latency, blocking probability, and optimized network resource allocation in dynamic scenarios. This highlights the effectiveness of the proposed approach in improving system performance and addressing the challenges of CE-EONs.** © 2024 Optica Publishing Group

https://doi.org/10.1364/JOCN.500117

# 1. INTRODUCTION

In recent years, the rapid development of Internet of Things (IoT) has given rise to a wide range of mobile applications, including smart cities, intelligent transportation systems, and virtual reality [1,2]. These applications often impose significant bandwidth demands while operating under strict latency requirements. Additionally, the exponential increase in user requests from the core network further intensifies the need for efficient processing. Cloud-edge computing offers a potential solution that could alleviate computing and storage limitations and improve interoperability for response service provision [3]. Moreover, the cloud-edge infrastructure can introduce latencyaware strategies to solve potential data leakage for deploying data stream processing applications [4]. Consequently, relying solely on cloud computing may not effectively meet the fundamental requirements of user requests [5–7].

To address the limitations of traditional cloud computing architectures, the European Telecommunications Standards Institute (ETSI) has introduced the concept of mobile edge computing (MEC). MEC represents a novel computing model that enables the offloading of computing tasks from mobile terminals to edge servers located in close proximity [8]. By partially offloading the required resources from mobile terminals to nearby edge servers instead of solely relying on cloud servers, computation-intensive applications can be deployed with optimal performance, satisfying power-saving, latency, storage, and bandwidth requirements [9].

One significant research area focuses on leveraging the benefits of both cloud computing and MEC within elastic optical networks (EONs), specifically known as cloud-edge elastic optical networks (CE-EONs). CE-EONs are designed to integrate cloud and edge computing functionalities, enabling efficient offloading while meeting power-saving and latency constraints [10]. Figure 1 illustrates the three-layer integration architecture of cloud computing, edge computing, and the IoT, facilitating task offloading from IoT devices to the edge or cloud through heterogeneous network environments. When an edge server is chosen to serve a device, the task request is forwarded to the edge server for processing through the macro base station. Conversely, if a cloud server is selected, the macro station aggregates data traffic from multiple small base stations and routes it to the cloud server in the core network. It is worth

Institute of ICT Technology, China Information Consulting & Designing Institute Co., Ltd., Nanjing, Jiangsu Province, 210019, China

<sup>3</sup>Department of Electrical and Computer Engineering, University of Waterloo, Waterloo, Ontario N2L 3G1, Canada

<sup>4</sup>Erik Jonsson School of Engineering and Computer Science, The University of Texas at Dallas, Richardson, Texas 75080, USA \*bwchen@suda.edu.cn

![](_page_1_Figure_3.jpeg)

Fig. 1. Three-layer integrated architecture of cloud computing, edge computing, and IoT.

noting that the core network connects to the Internet via a network gateway typically located near a large data center (DC), which can cache and provide robust data processing capabilities as needed.

Motivated by this observation, current research efforts on CE-EONs predominantly focus on resource offloading strategies aimed at reducing latency and energy consumption, and enhancing user experience. For example, the resource offloading problem involves making decisions on whether and where to delegate the extensive computing data requested by user devices [11], while meeting the power-saving and latency requirements of each user request. When sufficient resources are available at the network edge for processing the task requests, the computing results are returned directly from the edge server to the corresponding devices without involving the cloud server [12]. In this context, the edge servers, also known as proxy servers, are typically situated at base stations and/or wireless access points. However, the previous studies did not investigate how to reduce the end-to-end (E2E) latency and spectrum resource occupancy in CE-EONs.

In this paper, unlike previous studies about resource offloading approaches that do not consider the partial resource offloading, we discuss the effect of indivisible services and divisible services on the E2E latency when the user requests are offloaded to the servers at the edge or cloud regions. On the one hand, we emphasize the low-latency partial resource offloading by considering the proportional and average segmentation. We formulate the concept of server importance degree to achieve equilibrium between average E2E latency and the load balancing between regions for the user request offloading. On the other hand, we formulate an integer linear programming (ILP) model with partial resource offloading to minimize the E2E latency and spectrum resource occupancy. We also propose partial resource offloading approaches based on proportional and average segmentation to achieve low E2E latency and high spectrum efficiency, as well as the collaborative cloud-edge (CCE) offloading approach in CE-EONs. Our proposed partial resource offloading approaches closely approximate the optimal solutions of the ILP model and achieve efficient resource offloading in CE-EONs more effectively than the other traditional approaches.

This paper investigates the resource offloading problem in CE-EONs and is organized as follows. Section 2 discusses the related work and highlights our contributions. Section 3 presents the system model and defines the problem statement. The formulation of E2E latency and partial resource offloading is presented in Section 4. Section 5 presents an ILP model for partial resource offloading, followed by the introduction of heuristic approaches in Section 6. The performance evaluation and discussion of the ILP model and proposed heuristics are presented in Sections 7 and 8. Finally, Section 9 concludes the paper.

#### 2. RELATED WORK AND OUR CONTRIBUTIONS

#### A. Resource Offloading Problem

State-of-the-art resource offloading approaches reported in the literature can be classified into three categories: binary offloading, partial task offloading, and cloud-edge collaboration. Binary resource offloading is typically formulated as a mixed integer nonlinear programming problem, known to be non-deterministic polynomial hard (NP-hard). A game-based multitype task offloading scheme was proposed to alleviate high-load mobile-edge computing for the tasks with different types, indicated by computation amount and data size [13]. Task partitioning and offloading algorithms were designed to jointly optimize the computation delay and energy consumption to the user requests [14]. To minimize both energy consumption and execution latency, a value iteration-based reinforcement learning method was proposed to determine the joint policy of computation offloading and resource allocation [11,15]. Our previous studies investigated selective offloading by exploring the regions' resource equalization and E2E latency for network resource optimization with latency sensitivity [16], where three schemes or selective resource offloading heuristic approaches, namely, resource priority offloading, distance priority offloading, and coordinated distance and resource offloading were introduced [17,18]. None of these considered partial resource offloading in CE-EONs.

In contrast to binary resource offloading, determining which part of the task should be offloaded becomes crucial in the design of partial resource offloading schemes. An optimal strategy was presented in [19] to control the offloading data size and latency/sub-channel allocation while minimizing energy consumption. By considering users' quality of service and energy consumption, a Lagrange multiplier method was employed to solve a user energy consumption minimization problem [20]. Recognizing the collaboration inherent in augmented reality (AR) applications, where different users share computing tasks and input/output data, Al-Shuwaili and Simeone [21] proposed an effective resource offloading scheme that allows users to offload shared data to MEC servers for execution.

Establishing a collaborative offloading model that combines cloud and edge computing addresses the limitations of edge computing, which offers low latency but limited computing capacity, and cloud computing, which provides rich computing resources but higher latency [10]. Wu *et al.* [22] proposed an edge–cloud collaborative multi-task resource offloading model that considers both latency and energy consumption. They used the nonlinear exponential inertia weight particle swarm optimization algorithm to solve the problem. Peng *et al.* [23] introduced three constrained multi-objective evolutionary algorithms to solve IoT-enabled resource offloading problems in collaborative edge and cloud computing networks. Additionally, a cloud mobile edge computing collaborative task offloading scheme based on service choreography was proposed, which enables differentiated offloading decisions for tasks with varying resource requirements and latency sensitivity. The scheme incorporates an orchestrating data-as-services mechanism based on software-defined networking [24].

#### B. E2E Latency Problem

End-to-end latency refers to the time taken to complete a given offloading task, generally consisting of the transmission latency for offloading data from the terminal equipment to the edge node and the processing latency of the offloaded data at the edge node. To reduce the E2E latency, Li *et al.* [25] enabled terminal devices to offload computing tasks to multiple edge nodes and perform repeated offloading tasks. Ren *et al.* proposed a joint communication and computing resource allocation problem and deduce an optimal task segmentation strategy to minimize the total latency of all mobile devices based on the normalized backhaul communication and cloud computing capacities [26]. Additionally, an area-based offloading policy (ABOP) algorithm was proposed to offload as many tasks as possible in different regions, aiming for low latency and a high completion rate [27]. For latency-sensitive applications, a mobile edge computing framework was studied for multi-user resource offloading and transport scheduling [28]. Considering the tradeoff between local computing and edge computing, wireless characteristics, and the noncooperative game behavior of mobile users, a new mechanism called MOTM was proposed to jointly determine the resource offloading scheme, transmission scheduling rules, and pricing rules [29]. Techniques such as dynamic voltage frequency adjustment and power control were employed to optimize data transmission and computation offloading, respectively, to optimize execution latency and reduce execution errors [28].

Reducing E2E latency while considering traffic load balancing between regions is one of the current research hotspots. To minimize the processing latency of computation tasks in vehicles, Zhang *et al.* [30] proposed an SDN-based load-balancing task offloading scheme in FiWi-enhanced vehicular edge computing networks. They introduced SDN to provide centralized network and vehicle information management support. In order to maintain load balance among independent cloudlets while improving quality of service and users' quality of experience, Zhang and Wang [31] transformed the cloudlets' load-balancing issue into a competition where each user aims to minimize its task execution time. They proposed a multiuser decentralized learning algorithm to obtain the pure Nash equilibrium strategy for each user. Flow shop sequencing and job shop scheduling techniques were applied to process user requests and reduce server idle time. Raj extended Johnson's sequencing for load balancing based on these aspects [32].

# C. Our Contributions

Our contributions in this study can be summarized as follows:

- (1) We introduce the concept of partial resource offloading with the objective of reducing E2E latency. We provide a detailed calculation of the E2E latency, considering the scenarios where tasks can be offloaded partially.
- (2) We develop a novel ILP model for partial resource offloading. The model aims to minimize both the E2E latency and total number of frequency slots required. It allows each user request to be processed either as a whole or in segmented form.
- (3) We propose four heuristic selective offloading approaches that combine and complete resource offloading. Among these approaches, we find that the partial resource offloading approach based on proportional segmentation achieves results that are closest to the performance of the ILP model.
- (4) We demonstrate the effectiveness of our proposed partial resource offloading approach based on the proportional segmentation approach in reducing average E2E latency, lowering the blocking probability, and optimizing the allocation of network resources.

# 3. SYSTEM MODEL AND PROBLEM STATEMENT

# A. System Model

The network architecture of CE-EONs is shown in Fig. 2, which includes base stations (BSs), edge servers, cloud servers, and EONs. Each BS has an edge server nearby and connects with a corresponding switch, and edge servers are also deployed with switches. Each BS can be deployed and updated to support different generations of mobile communication, such as the third generation (3G), 4G, 5G, and 6G, and so on. The bandwidth and traffic flow will gradually increase with the development of mobile communications in different generations, as well as the computing resources. In this situation, the capacity of bandwidth resources and computing resources must expand in order to meet the requirements of user requests in CE-EONs. Due to high data rate and low latency, CE-EON can meet the requirements of the bandwidth and computing resources in the future 6G era.

The elastic optical network consists of a set of optical switches that are connected with a corresponding switch and set of fiber links. The optical switches consist of sets of wavelength cross-connects (WXCs) [33]. Optical amplifiers are placed before and after the WXC to compensate fiber and node losses. The fiber links have spectrum resources to carry the bandwidth requirements of user requests. The spectrum resources are divided into different frequency slots, where each frequency slot has 12.5 GHz bandwidth in the frequency domain. Thus, the bandwidth requirements of user requests can be flexible spectrum allocation. The spectrum allocation

![](_page_3_Figure_3.jpeg)

**Fig. 2.** Network architecture of CE-EONs.

must meet the constraints of spectrum consecutiveness in the frequency domain and spectrum consistency on each link through the reserved path.

A CE-EON system model is considered as a physical network represented by a weighted undirected graph G(B,CN,EN,CL,EL,J), where  $\textbf{B} = \{b_1,b_2,...,b_{|\textbf{B}|}\}$  refers a sets of BSs,  $\textbf{CN} = \{cn_1,cn_2,...,cn_{|\textbf{CN}|}\}$  is a set of cloud nodes (CNs) that include a large number of cloud servers to provide the computing resources,  $\textbf{EN} = \{en_1,en_2,...,en_{|\textbf{CN}|}\}$  denotes a set of edge nodes (ENs) that include several edge servers to provide the computing resources,  $\textbf{CL} = \{cl_1,cl_2,...,cl_{|\textbf{CL}|}\}$  is a set of cloud links (CLs) that are the fiber links,  $\textbf{EL} = \{el_1,el_2,...,el_{|\textbf{EL}|}\}$  is a set of edge links (ELs) that are the fiber links, and  $\textbf{J} = \{j_1,j_2,...,j_{|\textbf{J}|}\}$  represents a sets of optical switches. |B|,|CN|,|EN|,|CL|,|EL|, and |J| represent the numbers of BSs, cloud nodes, edge nodes, cloud links, edge links, and optical switches, respectively.

Structurally, a CE-EON is divided into two layers. The bottom layer, also referred to as the edge layer, consists of multiple edge nodes, each containing a set of edge servers, switches, and base stations, that can effectively provision both computing and transmitting functions. The top level, also referred to as the cloud layer, is composed of multiple cloud nodes that have both cloud servers and switches to provide cloud computing and transmitting services. Fiber links are used between the BSs, edge servers, and switches to transmit user requests.

#### **B. Problem Statement**

In this paper, we consider two scenarios with static and dynamic CE-EONs. For the static scenario, computing and spectrum resources are not released after establishing the user requests one by one. However, in the dynamic scenario, the edge server releases computing resources and the fiber link liberates the spectrum resources after processing the user requests. The statement of the problem is as follows: A CE-EON is given and is represented by a symbol, G(B, CN, EN, CL, EL, J),

and a set of user requests,  $\mathbf{U} = \{\mathbf{u}_1, \mathbf{u}_2, ..., \mathbf{u}_{\|\mathbf{U}\|}\}$ , where each user request is defined as u(s, f, r, t), including the source node s, bandwidth resource requirements f, computing resource requirement r, and traffic type t. We proceed with the offloading of each user request in the CE-EON by allocating computing resources in the cloud and edge layers, as well as spectrum resources on the fiber links. In the offloading process, we take into account both the E2E latency and the optimization of network resources. Additionally, we consider the concept of partial resource offloading and the importance degree of servers for each user request.

Our objective is twofold: first, to minimize the average E2E latency by leveraging partial resource offloading, thereby reducing the time required for task completion. Second, we aim to optimize the allocation of network resources, ensuring efficient utilization while maintaining a balanced traffic load between different regions. The server importance degree is taken into consideration to achieve this balance and effectively distribute the workload among servers. By addressing these objectives, we aim to enhance the overall performance of the system and improve the user experience.

# 4. E2E LATENCY AND PARTIAL RESOURCE OFFLOADING

In this section, we discuss the E2E latency, partial resource offloading, and server importance degree for processing user requests in CE-EONs. The user requests are classified into divisible and indivisible services, where the former can be split and partially transferred to other edge servers for processing, while the latter can only be processed as a whole.

# A. E2E Latency

#### 1. Indivisible Services

E2E latency includes network transmission latency and computing latency. We consider three different scenarios of dealing with user requests in order to reduce the E2E latency, and the corresponding transmission routes of the three scenarios are shown in Fig. 2.

In Scenario 1, the user request is processed at an edge server in the local region and the network transmission latency can be ignored. Thus, the E2E latency only needs to consider computing latency. The latency of scenario 1 is as follows:

$$T_1^u = \frac{r_u}{C_c}.$$
(1)

Here,  $r_u$  and  $C_s$  are the computing resource requirements of a user request u and the computing capacity per unit time of edge server s in the local region.

In Scenario 2, the user request needs to offload to an edge server in an adjacent region for processing, and the E2E latency includes transmission and computing latency, which is written as follows:

$$T_2^u = t_{u,b,j}^{L_1} + t_{u,j,s}^{L_2} + \frac{r_u}{C}$$
 (2)

Here,  $L_1$ ,  $L_2$ ,  $t_{u,b,j}^{L_1}$ ,  $t_{u,j,s}^{L_2}$ , and  $C_s$  are the distance from BS b to optical switching node j, the distance from j to edge server

s in the edge layer, the transmission latency of a user request u from b to j, the transmission latency of a user request u from j to s, and the computing capacity per unit time of an edge server s in an adjacent region, respectively.

In Scenario 3, we transmit the user request to the cloud server, and thus the network transmission latency and computing latency are considered as

$$T_3^u = t_{u,b,j}^{L_1} + t_{u,j,s}^{L_3} + \frac{r_u}{C_c}$$
 (3)

Here,  $L_3$ ,  $t_{u,j,s}^{L_3}$ , and  $C_s$  are the distance from the optical switching node j to an edge server s in the cloud layer and the transmission latency of a user request u from j to s and the computing capacity per unit time of an edge server s or cloud server s, respectively.

#### 2. Divisible Services

On the grounds of partial resource offloading, we propose a proportional segmentation approach which splits divisible user requests into two parts; one part of a user request is processed in the local region and the remaining part is offloaded to another region for disposing. Hence, we redefine the calculation of E2E latency for the three different scenarios.

In Scenario 1, on account of the relatively short length of the transmission path, the transmission latency can be ignored and the E2E latency only needs to consider processing latency. Thus, the latency of processing  $T_1^u$  for a user request u in the local region is as follows:

$$T_1^u = \frac{\lambda_u r_u}{C_{s_i}}.$$
(4)

Here,  $\lambda_u$  in [0,1] represents the optimal segmentation ratio of partial resource offloading;  $r_u$  and  $C_{s_i}$  are the computing resource requirements of a user request u and the computing capacity per unit time of an edge server  $s_i$  in the local region, respectively.

 $T_2^u$  and  $T_3^u$  represent the E2E latency of processing a user request u in the edge layer and cloud layer, respectively. In these scenarios, the transmission latency and processing latency together make up the E2E latency for user requests. The calculation of E2E latency is shown in Eqs. (5) and (6):

$$T_2^u = t_{u,b,j}^{L_1} + t_{u,j,s_j}^{L_2} + \frac{(1 - \lambda_u) r_u}{C_{s_j}},$$
 (5)

$$T_3^u = t_{u,b,j}^{L_1} + t_{u,j,s_j}^{L_3} + \frac{(1 - \lambda_u) r_u}{C_{s_i}}.$$
 (6)

Here,  $C_{s_j}$  is the computing capacity per unit time of an edge server  $s_j$  in an adjacent region [i.e., Eq. (5)] or a cloud server  $s_j$  [i.e., Eq. (6)].  $L_1$ ,  $L_2$ , and  $L_3$  are respectively the distance from BS b to optical switching node j, the distance from optical switching node j to edge server  $s_j$  in the edge layer, and the distance from optical switching node j to edge server  $s_j$  in the cloud layer. Furthermore,  $t_{u,b,j}^{L_1}$ ,  $t_{u,j,s_j}^{L_2}$ , and  $t_{u,j,s_j}^{L_3}$  represent the transmission latency of a user request u from b to b, the transmission latency of user request b from b to b, respectively.

As a consequence, the E2E latency of a user request u can be described as

$$T = \max \left\{ T_1^u, \, \eta_1 \times T_2^u + \eta_2 \times T_3^u \right\}. \tag{7}$$

Here,  $\eta_1$  and  $\eta_2$  are two binary variables, where  $\eta_1 = 1$  represents offloading user requests to adjacent regions in the edge layer, and  $\eta_2 = 1$  means offloading user requests to adjacent regions in the cloud layer.

Obviously, the E2E latency mainly depends on the maximum latency of processing user requests locally and offloading user requests to adjacent or cloud regions.

## B. Partial Resource Offloading and Server Importance Degree

#### 1. Offloading Decision Variable

In order to reduce the E2E latency and balance the traffic load between regions as much as possible, the concept of an offloading decision variable is proposed to offload user requests.  $M_u \in \{0, 1\}$ ,  $M_u = 1$  means that the user request is processed locally, while  $M_u = 0$  represents that the user request is sent to another region for handling. The calculation of  $M_u$  is shown as

$$M_{u \in \mathbf{U}} = \text{round} \left\{ \varphi \frac{Re_{\text{max}} - Re_i}{Re_{\text{max}} - Re_{\text{min}}} + \omega \frac{D_{\text{max}} - D_i}{D_{\text{max}} - D_{\text{min}}} \right\}.$$
 (8)

Here,  $Re_i$  and  $D_i$  denote the computing resource utilization ratio of the local region i and the E2E latency when processing the user request locally, respectively.  $Re_{\rm max}$ ,  $Re_{\rm min}$ ,  $D_{\rm max}$ , and  $D_{\rm min}$  represent the maximum and minimum computing resource utilization ratios among all regions, and the maximum and minimum E2E latency for dealing with user requests in different regions, respectively. In Eq. (8), two adjustable factors,  $\varphi$  and  $\omega$ , satisfy  $\varphi + \omega = 1$ . In addition, the value of  $M_u$  is rounded. The values of  $M_u$  are the decimals from 0 to 1. We can offload the user request at the local region if the value of  $M_u$  is close to 1, i.e.,  $M_u = 1$ . The reason is that the values of the  $Re_i$  and  $D_i$  are very small. Conversely, the user request should be offloaded to the other region rather than the local region when  $M_u = 0$ .

#### 2. Derivation of the Optimal Segmentation Ratio

It's not difficult to see from these equations that  $T_1^u$  increases with the increase of segmentation ratio  $\lambda_u$ , while  $T_2^u$  and  $T_3^u$  decrease with the increase of segmentation ratio  $\lambda_u$ . Moreover, the total E2E latency of one user request is composed of  $T_1^u$  and  $T_2^u$  or  $T_1^u$  and  $T_3^u$ . Therefore, when the value of  $T_1^u$  is relatively close to that of  $T_2^u$  or  $T_3^u$ , the total latency can reach the minimum. The derivation process of the optimal segmentation ratio is as follows:

$$\frac{\lambda_{u} r_{u}}{C_{s_{i}}} = \max \left\{ \eta_{1} \times \left( t_{u,b,j}^{L_{1}} + t_{u,j,s_{j}}^{L_{2}} + \frac{(1 - \lambda_{u}) r_{u}}{C_{s_{j}}} \right), \right.$$

$$\eta_{2} \times \left( t_{u,b,j}^{L_{1}} + t_{u,j,s_{j}}^{L_{3}} + \frac{(1 - \lambda_{u}) r_{u}}{C_{s_{j}}} \right) \right\}. \tag{9}$$

In Eq. (9),  $\eta_1$  and  $\eta_2$  are two binary variables. The size of the segmentation ratio only affects the size of processing latency, while transmission latency has nothing to do with segmentation ratio. Therefore, in order to simplify the derivation, we replace the transmission latency in Eq. (9) with t'. Then Eq. (9) can be transformed:

$$\frac{\lambda_u r_u}{C_{s_i}} = t' + \frac{(1 - \lambda_u) \, r_u}{C_{s_i}},\tag{10}$$

$$\lambda_{u}r_{u} \times C_{s_{j}} = t' \times C_{s_{i}}C_{s_{j}} + (1 - \lambda_{u}) r_{u} \times C_{s_{i}},$$
 (11)

$$\lambda_u r_u \times \left(C_{s_i} + C_{s_j}\right) = t' \times C_{s_i} C_{s_j} + r_u \times C_{s_i}, \qquad (12)$$

$$\lambda_{u} = \frac{t' \times C_{s_{i}} C_{s_{j}}}{r_{u} \times \left(C_{s_{i}} + C_{s_{j}}\right)} + \frac{C_{s_{i}}}{C_{s_{i}} + C_{s_{j}}},$$
(13)

$$\lambda_u = \frac{t' \times C_{s_i} C_{s_j} + r_u \times C_{s_i}}{r_u \times (C_{s_i} + C_{s_j})},$$
(14)

where  $C_{s_i}$  and  $C_{s_j}$  are the computing capacity per unit time of an edge server  $s_i$  and a cloud sever  $s_j$ .

#### 3. Server Importance Degree

In order to achieve equilibrium between average E2E latency and the load balancing between regions, the concept of server importance degree (SID) is proposed to optimize the user request offloading. The definition of SID is the normalization of E2E latency processing and computing resources of the edge server. The detailed computation of the SID is as follows:

$$SID_{s \in \mathbf{S}} = \varepsilon \left( \gamma \frac{E_{s} - E_{\min}}{E_{\max} - E_{\min}} + \delta \frac{C_{s} - C_{\min}}{C_{\max} - C_{\min}} \right) + \zeta \left( \frac{L_{s} - L_{\min}}{L_{\max} - L_{\min}} \right).$$
(15)

Here, both  $E_s$  and  $C_s$  are computing resources of an edge server s and cloud computing server s, and  $L_s$  is E2E latency of processing a user request in edge server s. In addition,  $E_{\min}$ ,  $E_{\max}$ ,  $C_{\min}$ ,  $C_{\max}$ ,  $L_{\min}$ , and  $L_{\max}$  are the minimum and maximum computing resources of edge servers in the edge layer, the minimum and maximum computing resources of cloud servers in the cloud layer, and the minimum and maximum E2E latency of processing user requests in server s, respectively. a and b are two binary variables, where the value of  $\gamma$  is 1, i.e.,  $\gamma = 1$ , when a server s is in the edge layer while the value of  $\delta$  is 1, i.e.,  $\delta = 1$  when a server s is in the cloud layer. In Eq. (15), two adjustable factors,  $\varepsilon$  and  $\beta$ , satisfy  $0 \le \varepsilon$ ,  $\zeta \le 1$ , and  $\varepsilon + \zeta = 1$ .

Figure 3 shows the calculation of E2E latency of partial resource offloading. The corresponding values can be calculated according to the variables and segmentation ratio just proposed, where the hexagons contain the values for the SID. According to Eq. (14), we can determine the segmentation ratio  $\lambda_u = 0.3$ . Furthermore, the E2E latency of processing in node 0 and node 4 separately is 0.057 and 0.125 s. Introducing partial offloading, one part of the user request is processed

![](_page_5_Figure_15.jpeg)

**Fig. 3.** Calculation of E2E latency of partial resource offloading.

in node 0 and the other part is dealt with in node 5, then the latency turns to 0.04 and 0.038 s, respectively. Obviously, the total latency decreased sharply and the overall latency is 0.04 s.

#### C. Evaluation Metrics

We give several evaluation indexes after the completion of selecting the optimal server to process user requests.

(1) Average E2E latency: The average E2E latency of user requests is defined as

$$T_{\text{ave}} = \sum_{u \in U} \frac{T_1^u + T_2^u + T_3^u}{|U_s|}.$$
 (16)

Here,  $T_1^u$ ,  $T_2^u$ , and  $T_3^u$  are the E2E latency of three scenarios, the transmission latency and E2E latency of processing user requests in the edge and cloud layers, respectively.  $|U_s|$  is the number of user requests that are successfully processed and established in the CE-EONs.

- (2) Blocking probability: The blocking probability of the entire network is composed of the blocking probability of spectrum and computing resources, which refers to the percentage of user requests processed unsuccessfully due to insufficient spectrum or computing resources to process user requests.
- (3) Spectrum occupancy ratio: The ratio of the number of frequency slots occupied by all user requests over the total number of frequency slots in the entire network. Therefore, the spectrum occupancy ratio can be written as

$$SOR = \frac{\sum_{u \in U} f_u \cdot B_j}{LN \cdot SN}.$$
 (17)

Here,  $f_u$  is the bandwidth resource requirements of a user request u(s, f, r, t) and  $B_j$  are binary variables which represent whether a use request u is successfully processed. LN and SN represent the number of all fiber links and frequency slots in each fiber link, respectively.

(4) *Average hops*: The average number of fiber links that a user requests from the source node to destination node.

# 5. ILP MODEL OF PARTIAL RESOURCE OFFLOADING

In order to minimize the E2E latency and spectrum resource occupancy, we develop an ILP model of partial resource offloading which optimally chooses a set of servers to deal with user requests. The proposed ILP model of partial resource offloading must satisfy the constraints of computing resources of nodes and bandwidth resources of fiber links. The input parameters, variables, objectives, and equations of the ILP model are given as follows.

### Input parameters:

- G: a given CE-EON, G = G(B, CN, EN, CL, EL, J)
- U: a given set of user requests in a CE-EON.
- L: a set of fiber links in a CE-EON.
- **F**: a set of frequency slots of each fiber link in a CE-EON.
- $\mathbf{E}_e$ : a set of edge servers in a CE-EON.
- **E**<sub>c</sub>: a set of cloud servers in a CE-EON.
- **E**: a set of edge and cloud servers, i.e.,  $\mathbf{E} = \mathbf{E}_e \cup \mathbf{E}_c$  in a CE-EON.
  - u: a user request, i.e., u = u(s, f, r, t).
- (u, s): the user request u transmitted to node s processing.
- $T_{(u,s)}$ : the traffic type of the user request u transmitted to node s processing;  $T_{(u,s)} = 0$  denotes the user request u cannot be split for processing, while  $T_{(u,s)} = 1$  represents the user request u can be divided into parts for processing.
- $F_{(u,s)}$ : the bandwidth resource requirements of the user request u transmitted to node s processing.
- $R_{(u,s)}$ : the computing resource requirements of the user request u.
  - (k, l): the fiber link from node k to node l.
  - |**U**|: the number of all user requests in a CE-EON.
  - |L|: the number of fiber links in a CE-EON.
- $|\mathbf{F}|$ : the maximum number of frequency slots on a fiber link (k, l).
  - $|\mathbf{E}_e|$ : the number of edge servers in a CE-EON.
  - $|\mathbf{E}_c|$ : the number of cloud servers in a CE-EON.
  - |**E**|: the number of edge and cloud servers in a CE-EON.
  - *Ve*: the capacity of computing resources in node *e*.
  - *C*: the speed of light in fiber links.
- $W_{(u,s),(k,l)}^{e,i}$ : the length of link (k, l) that belongs to the ith reserved path, and user request u is transmitted to node e.
  - α: the adjustable factor regulating E2E latency.
  - $\beta$ : the adjustable factor influencing the frequency slots.
- $M_e$ : the capacity of the available computing resource for a
- $\tau$ : the extra latency of transmitting to the cloud computing server.
  - $\varphi$ : the maximum load of the edge server.
- $\theta$ : the total number of spectrum resources of the entire CE-EON. It is equal to the product of the total number of fiber links and the frequency slot capacity of the fiber links, which is  $\theta = |\mathbf{F}| \times |\mathbf{L}|$ .
- $P_{(u,s),(k,l)}^{e,i}$ : A fiber link (k,l) of the *i*th given candidate transmission path from the node *s* to the node *e* for the *u*th user request in advance. Its value is  $P_{(u,s),(k,l)}^{e,i} = 1$  when the *u*th user request uses a fiber link (k,l) from node *s* to node *e*;

otherwise, its value is  $P_{(u,s),(k,l)}^{e,i} = 0$  when the *u*th user request does not use a fiber link (k, l) from node *s* to node *e*.

#### Variables:

- $x_{(u,s)}^{e,i}$ : binary variable. It takes the value of 1 if the user request u is processed at server node e and transmitted through the ith reserved transmission path, i.e.,  $x_{(u,s)}^{e,i} = 1$ , and takes the value of 0 otherwise.
- $y_{(u,s)}^{e,i}$ : binary variable. It takes the value of 1 if the user request u is partially processed at server node e and transmitted through the ith reserved transmission path, i.e.,  $y_{(u,s)}^{e,i} = 1$ , and takes the value of 0 otherwise.
- $z_{(u,s)}$ : binary variable. It takes the value of 1 if the user request u is sent to the cloud layer for processing, i.e.,  $x_{(u,s)}^{e,i} = 1$ , and takes the value of 0 otherwise.
- $z'_{(u,s)}$ : binary variable. It takes the value of 1 if the user request u is partially sent to the cloud layer for processing, i.e.,  $y^{e,i}_{(u,s)} = 1$ , and takes the value of 0 otherwise.
- $w_{(u,s)(k,l)}^{e,f}$ : binary variable. It takes the value of 1 if the user request u is sent to the server node e for processing and the fth frequency slot is occupied on the fiber link (k, l), i.e.,  $w_{(u,s)(k,l)}^{e,f} = 1$ , and takes the value of 0 otherwise.
- $v_{(u,s)(k,l)}^{e,f}$ : binary variable. It takes the value of 1 if the partial user request u is sent to the server node e for processing and the fth frequency slot is occupied on the fiber link (k, l), i.e.,  $v_{(u,s)(k,l)}^{e,f} = 1$ , and takes the value of 0 otherwise.
- i.e.,  $v_{(u,s)(k,l)}^{e,f} = 1$ , and takes the value of 0 otherwise.

    $R_{1(u,s)}^{e}$ : the computing resource of the user request u that is processed in the server node e while  $x_{(u,s)}^{e,k} = 1$ .
- $R_{2(u,s)}^e$ : the computing resource of the user request u that is partially processed in the server node e while  $y_{(u,s)}^{e,i} = 1$ .

#### **Objective:**

Objective function (18) of the ILP model is to minimize the average E2E latency and the total number of frequency slots occupied in the CE-EON:

Minimize: 
$$P(G) = \alpha \times T(G) + \beta \times F(G)$$
. (18)

Here, T(G) and F(G) denote the average E2E latency and the total frequency slots occupied in the CE-EON, respectively. The objective function is composed of a primary and secondary objective, where the weight of the objective function can be changed by adjusting the values of  $\alpha$  and  $\beta$  (0 <  $\alpha$ ,  $\beta$  ≤ 1), and  $\alpha$  +  $\beta$  = 1, so as to achieve different optimization objectives.

In addition, the specific calculation formula of T(G) and F(G) is shown as Eqs. (19) and (20), respectively. The average E2E latency can be reduced by optimizing the choice of servers, and the number of frequency slots occupied in a CE-EON can be decreased by optimizing the sum of  $w_{(u,s)(k,l)}^{e,f}$  and  $v_{(u,s)(k,l)}^{e,f}$ .

$$T(G) = \frac{1}{|\mathbf{U}\mathbf{R}|} \left\{ \sum_{(u,s)\in\mathbf{U}}^{e\in\mathbf{E},i\in\mathbf{K}} \left( x_{(u,s)}^{e,i} \times \frac{W_{(u,s),(k,l)}^{e,i}}{C} \right) + \sum_{(u,s)\in\mathbf{U}}^{e\in\mathbf{E}} \frac{R_{1(u,s)}^{e}}{M_{e}} + \sum_{(u,s)\in\mathbf{U}} z_{(u,s)} \times \tau \right\},$$
(19)

$$F(G) = \sum_{(k,l)\in L, f\in F}^{e\in E, (u,s)\in U} \left( w_{(u,s)(k,l)}^{e,f} + v_{(u,s)(k,l)}^{e,f} \right).$$
 (20)

#### Constraints:

(1) Node and path selection uniqueness constraints: A user request can be processed by one server or two servers in collaboration, and each user request must select one of the *i*th transmission paths to transmit the user request:

$$\sum_{e \in E}^{i \in K} x_{(u,s)}^{e,i} = 1, \quad \forall (u,s) \in U,$$
 (21)

$$\sum_{e \in E} y_{(u,s)}^{e,i} \le T_{(u,s)}, \quad \forall (u,s) \in U.$$
 (22)

(2) Node selection constraint: The selected server that processes user requests cannot be the same as the source node. Determine whether the node in the cloud region processes user requests:

$$\sum_{i \in K} x_{(u,s)}^{e,i} \neq \sum_{i \in K} y_{(u,s)}^{e,i}, \quad \forall (u,s) \in U, \ e \in E, \quad (23)$$

$$\sum_{i \in K} x_{(u,s)}^{e,i} > 0, \quad \forall (u,s) \in U, \ e \in E, \ e \neq s, \quad \text{(24)}$$

$$\sum_{i \in V} x_{(u,s)}^{s,i} = 0, \quad \forall (u,s) \in U,$$
 (25)

$$\sum_{i \in K} y_{(u,s)}^{s,i} = 0, \quad \forall (u,s) \in U,$$
 (26)

$$\sum_{e \in E_c}^{i \in K} x_{(u,s)}^{e,i} = z_{(u,s)}, \quad \forall (u,s) \in U,$$
 (27)

$$\sum_{e \in E_c}^{i \in K} y_{(u,s)}^{e,i} = z'_{(u,s)}, \quad \forall (u,s) \in U.$$
 (28)

(3) Partial offloading variables constraint: The amount of requested computing resources processed by node *e* cannot exceed the required amount:

$$\sum_{i \in K} x_{(u,s)}^{e,i} \times R_{(u,s)} \ge R_{1(u,s)}^{e}, \quad \forall (u,s) \in U, e \in E,$$
(29)

$$\sum_{i \in K} y_{(u,s)}^{e,i} \times R_{(u,s)} \ge R_{2(u,s)}^{e}, \quad \forall (u,s) \in \mathbf{U}, e \in \mathbf{E}.$$

(4) Latency constraint: If a part of the user request is processed in the local region, the remaining part is offloaded to another region, and thus the E2E latency is included in the part with longer latency:

$$\left(\sum_{e \in E}^{i \in K} x_{(u,s)}^{e,i} \times \frac{W_{(u,s),(k,l)}^{e,i}}{C} + \sum_{e \in E} \frac{R_{1(u,s)}^{e}}{M_{e}} + \sum_{(u,s) \in U} z_{(u,s)} \times \tau\right) - \left(\sum_{e \in E}^{i \in K} y_{(u,s)}^{e,i} \times \frac{W_{(u,s),(k,l)}^{e,i}}{C} + \sum_{e \in E} \frac{R_{2(u,s)}^{e}}{M_{e}} + \sum_{(u,s) \in U} z'_{(u,s)} \times \tau\right) \ge 0, \quad \forall (u,s) \in U.$$
(31)

(5) Computing resource capacity of a node: The computing resources processed by selected servers must not be less than the computing resource requirements of user requests. Furthermore, the total computing resources processed by each server node cannot exceed the computing resource capacity of the corresponding node:

$$\sum_{e \in E} \left( \frac{R_{1(u,s)}^{e}}{M_{e}} + \frac{R_{2(u,s)}^{e}}{M_{e}} \right) \ge R_{(u,s)}, \quad \forall (u,s) \in U,$$
(32)

$$\sum_{(u,s)\in U} \left( \frac{R_{1(u,s)}^e}{M_e} + \frac{R_{2(u,s)}^e}{M_e} \right) \le V_e, \quad \forall e \in E. \quad \textbf{(33)}$$

(6) Spectrum occupancy uniqueness constraint: Whether partial offloading is performed or not, the number of frequency slots occupied by the user request *u* transmitted to the edge server node *e* on the fiber link (*k*, *l*) is equal to the bandwidth resource requirements of each user request. In addition, the *f*th frequency slot of each fiber link can be occupied for only one user request:

$$\sum_{f \in F} w_{(u,s)(k,l)}^{e,f} = \sum_{i \in K} x_{(u,s)}^{e,i} \times P_{(u,s),(k,l)}^{e,i} \times F_{(u,s)},$$

$$\forall (u, s) \in U, e \in E, (k, l) \in L,$$
 (34)

$$\sum_{f \in F} v_{(u,s)(k,l)}^{e,f} = \sum_{i \in K} y_{(u,s)}^{e,i} \times P_{(u,s),(k,l)}^{e,i} \times F_{(u,s)},$$

$$\forall (u, s) \in U, e \in E, (k, l) \in L,$$
 (35)

$$\sum_{(u,s)\in U}^{e\in E} \left( w_{(u,s)(k,l)}^{e,f} + v_{(u,s)(k,l)}^{e,f} \right) \le 1, \ \forall (k,l) \in L, \ f \in F.$$
(36)

(7) Spectrum resource capacity constraint: The number of frequency slots occupied by each fiber link cannot exceed the total number of frequency slots of the fiber link:

$$\sum_{(u,s)\in U}^{e\in E,f\in F} \left( w_{(u,s)(k,l)}^{e,f} + v_{(u,s)(k,l)}^{e,f} \right) \le |F|, \quad \forall (k,l) \in L.$$
(37)

(8) Spectrum consecutiveness constraint:  $\theta$  represents the total frequency slots of the entire network. Equations (38)–(41) can guarantee that the allocated frequency slots must be continuous in the frequency

domain on each fiber link. This constraint is written as follows:

$$\left(w_{(u,s)(k,l)}^{\epsilon,f}-w_{(u,s)(k,l)}^{\epsilon,f+1}-1\right)\times (-\theta) \geq \sum_{z\in [f+2,|F|]} w_{(u,s)(k,l)}^{\epsilon,z},$$

$$\forall (u, s) \in U, (k, l) \in L, f \in F.$$
 (38)

$$\left(w_{(u,s)(k,l)}^{e,f}-1\right)\times\theta+F_{(u,s)}\leq\sum_{f\in F}w_{(u,s)(k,l)}^{e,f},$$

$$\forall (u, s) \in U, (k, l) \in L, f \in F.$$
 (39)

$$\left(v_{(u,s)(k,l)}^{e,f}-v_{(u,s)(k,l)}^{e,f+1}-1\right)\times(-\theta)\geq\sum_{z\in[f+2,|F|]}v_{(u,s)(k,l)}^{e,z},$$

$$\forall (u, s) \in U, (k, l) \in L, f \in F.$$
 (40)

$$\left(v_{(u,s)(k,l)}^{\epsilon,f}-1\right)\times\theta+F_{(u,s)}\leq\sum_{f\in F}v_{(u,s)(k,l)}^{\epsilon,f},$$

$$\forall (u, s) \in U, (k, l) \in L, f \in F.$$
 (41)

(9) Spectrum consistency constraint is defined as allocation of the same indexes of frequency slots on each link through the reserved transmission path. This constraint is written as follows:

$$w_{(u,s)(k_{1},l_{1})}^{e,f} = w_{(u,s)(k_{2},l_{2})}^{e,f}, \quad \forall (u,s) \in \mathbf{U}, (k_{1},l_{1}) \in \mathbf{L},$$

$$(k_{2},l_{2}) \in \mathbf{L}, \ (k_{1},l_{1}) \neq (k_{2},l_{2}), \ P_{(u,s),(k_{1},l_{1})}^{e,k} = P_{(u,s),(k_{2},l_{2})}^{e,k}.$$

$$\mathbf{(42)}$$

$$v_{(u,s)(k_{1},l_{1})}^{e,f} = v_{(u,s)(k_{2},l_{2})}^{e,f}, \quad \forall (u,s) \in \mathbf{U}, (k_{1},l_{1}) \in \mathbf{L},$$

$$(k_{2},l_{2}) \in \mathbf{L}, \ (k_{1},l_{1}) \neq (k_{2},l_{2}), \ P_{(u,s),(k_{1},l_{1})}^{e,k} = P_{(u,s),(k_{2},l_{2})}^{e,k}.$$

# 6. HEURISTIC APPROACHES OF PARTIAL RESOURCE OFFLOADING

To further reduce the average E2E latency, partial resource offloading approaches are proposed on the basis of different types of services via a proportional segmentation approach against its counterparts, namely, the collaborative cloud-edge approach and the traditional offloading approaches, which are taken for comparison in this study. The difference of the resource offloading approaches are described as follows.

We consider two types of proportional segmentation and average segmentation when employing the partial resource offloading approach. For the collaborative cloud-edge offloading approach, we do not consider the proportional and average segmentation when the resource offloading for user requests occurs on the edge and cloud servers. For the all-resource offloading approach, there is no distinction between indivisible and divisible services, where we can process all user requests

without partial resource offloading. For the all-local processing approach, we do not classify indivisible and divisible services and only offload the resources in the local region.

# A. Partial Resource Offloading Based on Proportional Segmentation Approach

The partial resource offloading approach is developed through a proportional segmentation approach that splits divisible user requests into two parts. One part of a user request is processed in the local region and the remaining part is offloaded to another region for processing. To summarize, upon the arrival of a user request, we first classify its type. If the use request is categorized as an indivisible service, it is processed by the server with the highest SID. However, if the user request is classified as a divisible service, we check if the traffic load constraint of the local region is exceeded. If the constraint is not exceeded, the user request is processed locally. On the other hand, if the traffic load conditions are exceeded, the user request undergoes segmentation based on the optimal segmentation ratio. The segmented parts are then processed locally, while the remaining parts are forwarded to the server with the highest SID for processing. The steps of the partial resource offloading approach based on proportional segmentation (PRO\_PS) is outlined in Approach 1.

An example of the partial resource offloading approach based on proportional segmentation is described in Fig. 4. The dotted line circle next to the server shows the real-time computing resources of the corresponding server. For user request  $u_1(s, f, r, t)$ , since the local load does not exceed the threshold, the local server shall be used to handle the request by taking path 1 as the corresponding transmission path. For user request  $u_2(s, f, r, t)$ , since the service type is divisible and the local load exceeds the threshold, we use Eq. (14) to calculate the proportion of local processing and the SID value of other servers besides the local server, as given in the hexagon box beside the server. We can see that some of the user requests are processed locally, while the remaining ones are offloaded to the server with the highest SID value by taking paths 2 and 3 as the established transmission paths.

![](_page_8_Picture_21.jpeg)

**Fig. 4.** Example of the partial resource offloading approach based on proportional segmentation.

#### **Approach 1: PRO\_PS Offloading Approach**

**Input:** A CE-EON physical network G(**B**, **CN**, **EN**, **CL**, **EL**, **J**), a set of user requests, **U**, *u*(*s*, *f*, *r*, *t*) ∈ **U**.

**Output:** Average E2E latency, blocking probability, spectrum occupancy ratio, and average hops of entire network after processing all user requests in the CE-EON architecture.

**Step 1:** For a user request *u*(*s*, *f*, *r*, *t*), the type of user request is first classified. In the event the service type is indivisible, enter Step 2; else enter Step 3.

**Step 2:** Calculate offloading decision variable *M<sup>u</sup>* and server importance degree according to Eqs. (14) and (15). If *M<sup>u</sup>* = 1, a user request *u* is handled in the local region. Otherwise, the edge server *s* with the highest SID is selected as destination server processing this user request; then enter Step 3.

**Step 3:** When the traffic load of the local region hasn't exceeded our set traffic load restriction, the user request is transferred to edge server *s* with most computing resources in the local region. Otherwise, we split user request *u*(*s*, *f*, *r*, *t*) into two parts on condition that traffic load surpasses traffic load restriction. On the whole, the computing resources of one part is λ*<sup>u</sup>* × *r<sup>u</sup>* , which is handled locally. Then the computing resources of the other part is (1 − λ*<sup>u</sup>* )*r<sup>u</sup>* , and we select the server with the highest SID to offload user request *u*(*s*, *f*, *r*, *t*).

**Step 4:** A user request *u*(*s*, *f*, *r*, *t*) is blocked on the condition that the chosen server doesn't have enough computing resources; else enter Step 5.

**Step 5:** For a user request *u*(*s*, *f*, *r*, *t*), we calculate *k* transmission paths from source node to destination node using *k* shortest path algorithm. The transmission paths are sorted on the basis of the length of the path, and the shortest path is ranked first. If transmission paths cannot be found, then the user request *u*(*s*, *f*, *r*, *t*) is terminated; else enter Step 6.

**Step 6:** According to the number of free frequency slots and length of each transmission path, the path with more free frequency slots and less distance from the *K* candidate paths is selected as a transmission path.

**Step 7:** After a user request *u*(*s*, *f*, *r*, *t*) establishes the transmission path successfully, we can search for the available frequency slots using the first fit algorithm, where the first fit algorithm can find the available spectrum resources from the smallest index of frequency slots to the largest one along the transmission path. We then allocated the available spectrum resources according to the constraints of spectrum consistency and spectrum consecutiveness on the selected transmission path. If available frequency slots are found, spectrum resources are allocated and spectrum status is updated. If not, spectrum allocation fails and a user request *u*(*s*, *f*, *r*, *t*) is blocked.

**Step 8:** The computing resources of the selected server is updated and the number of successful user requests is also recorded.

**Step 9:** Calculate average E2E latency, blocking probability, spectrum occupancy ratio, and average hops.

#### B. Collaborative Cloud-Edge Offloading Approach

In order to make full use of the edge computing capacity of base stations and cloud computing capacity of cloud servers, the tasks of each mobile device can be partially processed at edge nodes and partially offloaded to cloud servers for processing [26]. For the sake of minimizing the latency of all mobile devices, a joint communication and computing resource allocation approach is proposed. First, the optimal allocation of communication resources is derived in a closed form. Second, the tasks are segmented according to normalized backhaul communication and cloud computing capabilities. Then, the original joint communication and computing resource allocation problems are transformed into equivalent optimization problems using an optimal task partitioning strategy. Finally, owing to the Karush–Kuhn–Tucker (KKT) condition, a closed form of computing resource allocation is obtained to minimize the E2E latency.

The steps of the CCE offloading approach are shown in Approach 2.

### C. Traditional Offloading Approaches

(1) *Partial resource offloading based on average segmentation approach (PRO\_AS)*

The main difference between the PRO\_AS approach and the PRO\_PS approach is that they use different segmentation ratios. The influence of the different segmentation ratios on the E2E latency of a user request is analyzed. In the PRO\_AS approach, we first determine whether the user request needs to offload to another region. If the user requests require computational offloading, the method of average partition is adopted to determine the segmentation ratio of user requests, that is, half the user requests are processed by the local edge server and the other half are processed by servers in other regions.

(2) *All-resource-offloading approach (ARO)*

In the ARO approach, there is no distinction between indivisible and divisible services, and all user requests are processed as a whole without considering partial resource offloading. All resources are completely offloaded for each use request. Furthermore, the server with the highest SID is selected as the target server. If the selected server does not have sufficient computing resources to process the user request, the user request will be blocked. Then, the *K* shortest path (KSP) algorithm is used to establish the transmission path between the user request and selected destination server, and the spectrum resources are allocated on the transmission path according to the bandwidth resource requirements of the user request and constraints of spectrum consistency and consecutiveness.

(3) *All-local-processing approach (ALP)*

Similar to the ARO approach, the ALP approach does not classify indivisible and divisible services, and all user requests are processed by the server with the most computing resources in the local region. If no servers in the local region can meet the requirements of user requests, the user requests are blocked. If the selected server can meet the user's demand for computing resources, the KSP algorithm is used to establish a transmission path from the source node to the destination node, and spectrum

#### Approach 2: CCE Offloading Approach

**Input:** A CE-EON physical network G(**B**, C**N**, E**N**, C**L**, E**L**, **J**), a set of user requests, **U**,  $u(s, f, r, t) \in \mathbf{U}$ .

**Output:** Average E2E latency, blocking probability, spectrum occupancy ratio, and average hops of entire network after processing all user requests in the CE-EON architecture.

**Step 1:** For a user request u(s, f, r, t), the type of user requests is firstly classified. In the event the service type is indivisible, enter Step 2; else enter Step 3.

**Step 2:** Calculate offloading decision variable  $M_u$  and server importance degree according to Eqs. (14) and (15). If  $M_u = 1$ , a user request u(s, f, r, t) is handled in the local region. Otherwise, the server s with the highest SID is selected as the destination server processing user request; then enter Step 4.

**Step 3:** The values of the normalized backhaul communication and cloud computing capabilities are calculated, and the optimal task segmentation strategy is determined based on the values of these parameters. Some of the services are processed locally, and the remaining ones are calculated and offloaded; then Step 4 is performed.

Step 4: A user request is blocked on the condition that the chosen server does not have enough computing resources; else enter Step 5.

**Step 5:** For a user request u(s, f, r, t), we calculate k transmission paths from source node to destination node using k shortest path algorithm. The transmission paths are sorted on the basis of the length of the path, and the shortest path is ranked first. If transmission paths cannot be found, then the user request u(s, f, r, t) is terminated; else enter Step 6.

**Step 6:** According to the number of free frequency slots and length of each transmission path, the path with more free frequency slots and less distance from the *K* candidate paths is selected as a transmission path.

**Step 7:** After the user request u(s, f, r, t) establishes the transmission path successfully, we can search for the available frequency slots using the first fit algorithm, where the first fit algorithm can find the available spectrum resources from the smallest index of frequency slots to the largest one along the transmission path. We then allocate the available spectrum resources according to the constraints of spectrum consistency and consecutiveness on the selected transmission path. If available frequency slots are found, spectrum resources are allocated and spectrum status is updated. If not, spectrum allocation fails and user request u(s, f, r, t) is blocked.

Step 8: The computing resources of selected server is updated and the number of successful user requests is also recorded.

Step 9: Calculate average E2E latency, blocking probability, spectrum occupancy ratio, and average hops.

resources are allocated on the transmission path according to bandwidth resources of use requests and the constraints of spectrum consistency and consecutiveness.

## 7. COMPLEXITY ANALYSIS

For the complexity of the ILP model, it depends on the computational dimension space of variables. For the ILP model of partial resource offloading, the complexity of binary variables,  $x_{(u,s)}^{e,k}$ ,  $z_{(u,s)}$ ,  $w_{(u,s)(k,l)}^{e,f}$ , and  $R_{1(u,s)}^{e}$ , is  $O(K \times (|\mathbf{E}|-1))$ ,  $O(|\mathbf{E}_e|)$ ,  $O(|\mathbf{E}| \times |\mathbf{F}| \times |\mathbf{L}|)$ , and  $O(|\mathbf{E}|)$ , respectively. Similarly, since the partial offloading approach is adopted, the complexity of binary variables,  $y_{(u,s)}^{e,k}$ ,  $z_{(u,s)}^{e}$ ,  $v_{(u,s)(k,l)}^{e}$ , and  $R_{2(u,s)}^{e}$  is the same as the complexity of binary variables,  $x_{(u,s)}^{e,k}$ ,  $z_{(u,s)}^{e}$ ,  $w_{(u,s)(k,l)}^{e,f}$ , and  $R_{1(u,s)}^{e}$ . Thus, the total complexity of the ILP model of partial resource offloading is as follows:

$$O(2 \times (K \times (|\mathbf{E}| - 1) + |\mathbf{E}_c| + |\mathbf{E}| \times |\mathbf{F}| \times |\mathbf{L}| + |\mathbf{E}|)).$$
(44)

For indivisible traffic, the PRO\_PS approach adopts the concept of offloading decision variable and server importance degree to determine whether and where to offload, and its complexity is  $O(|\mathbf{Z}|)$  and  $O(|\mathbf{S}|)$ , where  $|\mathbf{Z}|$  and  $|\mathbf{S}|$  represent the number of regions and the number of nodes, respectively. For divisible traffic, the PRO\_PS approach must calculate the split ratio and then offload the traffic of each user request, where its complexity is  $O(|\mathbf{S}|)$ . Furthermore, the KSP algorithm is adopted to establish K candidate paths, the complexity of the PRO\_PS approach is  $O(K \times |\mathbf{S}| \times |\mathbf{L}| + |\mathbf{S}| \times \log(|\mathbf{S}| - 1))$ , where  $|\mathbf{L}|$  represent the number of fiber links. After traversing

the frequency slots and length of candidate paths, the path with shorter length and more free frequency slots is selected as the path, and the complexity is  $O(K \times |\mathbf{F}|)$ , where  $|\mathbf{F}|$  denotes the number of frequency slots in each fiber link. In addition, frequency slots are allocated for the selected path according to the constraints of spectrum consistency and consecutiveness. The complexity of the PRO\_PS approach is  $O(K \times (|\mathbf{F}| - f) \times f \times \log |\mathbf{S} - 1|)$ , where f is on behalf of the bandwidth resource requirement of each user request. Therefore, the total complexity of the PRO\_PS approach is as follows:

$$O(|\mathbf{Z}| + 2|\mathbf{S}| + K \times (|\mathbf{S}| \times (|\mathbf{L}| + |\mathbf{S}| \times \log(|\mathbf{S}| - 1)))$$

$$+ (|\mathbf{F}| - f) \times f \times \log(|\mathbf{S}| - 1) + |\mathbf{F}|)).$$
(45)

For traditional offloading approaches, the PRO\_AS and PRO\_PS approaches are differentiated only in the segmentation ratio, so the complexity is the same in the worst case. Similar to the PRO\_PS approach, the total complexity of the CCE approach is as follows:

$$O(K \times (|\mathbf{S}| \times (|\mathbf{L}| + |\mathbf{S}| \times \log(|\mathbf{S}| - 1)) + (|\mathbf{F}| - f)$$

$$\times f \times \log(|\mathbf{S}| - 1) + |\mathbf{F}|)).$$
(46)

For the ARO and ALP approaches, the distinguish between indivisible and divisible services is no longer carried out. We need to consider the complexity of the establishing path and the allocating frequency resources. Thus, the total complexity of the ARO and ALP approaches is described as Eqs. (47) and (48), respectively:

$$O(|\mathbf{Z}| + |\mathbf{S}| + K \times (|\mathbf{L}| + |\mathbf{S}| \times \log(|\mathbf{S}| - 1)) + (|\mathbf{F}| - f)$$

$$\times f \times \log(|\mathbf{S}| - 1) + |\mathbf{F}|)$$
(47)

$$O(|\mathbf{S}| + K \times (|\mathbf{L}| + |\mathbf{S}| \times \log(|\mathbf{S}| - 1)) + (|\mathbf{F}| - f)$$

$$\times f \times \log(|\mathbf{S}| - 1) + |\mathbf{F}|).$$
(48)

#### 8. SIMULATION AND RESULTS

In this section, we present the simulation results of the proposed ILP model as well as heuristic approaches of partial resource offloading in both 6- and 14-node CE-EONs. The simulation topologies of the 6- and 14-node CE-EONs are shown in Fig. 5. The ILP model and heuristic approaches are implemented using C++ in ILOG CPLEX V12.2 and Visual Studio 2008.

# A. ILP Model and Heuristic Approaches of Partial Resource Offloading with Static Scenario in a 6-Node Network

In static user requests, we run the ILP model and heuristic approaches, including the PRO\_PS, PRO\_AS, CCE, ALP, and ARO approaches, in a 6-node network with eight bidirectional fiber links in Fig. 5(a). The dotted circle presented near each node represents the corresponding computing resources of each server, and each fiber link provides 50 frequency slots. Each frequency slot has 12.5 GHz width. The bandwidth requirements of a user request are 10, 40, 80, and 100 Gbps with the uniform distribution, which correspond to the modulation formats, BPSK, QPSK, 8-QAM, and 16-QAM, respectively. The transmission reaches of the modulation formats BPSK, QPSK,

![](_page_11_Figure_9.jpeg)

**Fig. 5.** Simulation topologies: (a) a 6-node network and (b) a 14-node network.

8-QAM, and 16-QAM are 5000, 2500, 1250, and 625 km [34], respectively. The number of the required frequency slots for each user request is 2, 3, 4, and 5 for four different line rates, 10 Gbps, 40 Gbps, 80 Gbps, and 100 Gbps, respectively. We must emphasize that the proposed ILP model, PRO\_PS, PRO\_AS, CCE, ALP, and ARO, can support other multiple modulation formats. The computing resource requirements of user requests are in the range from 2 to 5 units, respectively. Each data point is obtained by averaging the results of applying 10 sets of user requests upon the ILP model and heuristic approaches.

Figure 6 calculates the average E2E latency using the ILP model and heuristic approaches under different numbers of user requests. The ILP model of partial resource offloading optimizes latency and spectrum occupancy ratio, thus achieving the lowest latency among all offloading approaches. The PRO\_PS approach can reduce the overall latency by classifying user requests according to different service types. The average latency is closest to that of the ILP model, which is 3.4% higher than that of the ILP model. The PRO\_AS approach adopts the average segmentation method for the separable services, so the E2E latency is higher than that of the PRO\_PS approach when the number of user requests is larger than 26. Although the CCE approach can effectively reduce the latency using the optimal task segmentation strategy, it does not consider setting the traffic load threshold. Most of the divisible services will be segmented, and the total latency of segmented processing is higher than that of completely local processing. Therefore, the E2E latency is higher than the PRO\_AS approach. Owing to the lack of consideration of service types, the latency of the ALP and ARO approaches is relatively high.

As shown in Fig. 7, the spectrum occupancy ratio of the ILP model and heuristic approaches are evaluated under different user requests. Since the ILP model of partial resource offloading aims to jointly optimize the average latency and number of frequency slots occupied, the ILP model has lower spectrum occupancy ratio, which is only slightly higher than the ALP approach. This is because the ALP approach is completely processed locally, and the transmission path in the static 6-node network only needs to go through one fiber link, so the spectrum occupancy ratio is the lowest. The main difference

![](_page_11_Figure_14.jpeg)

**Fig. 6.** Average E2E latency of partial resource offloading approaches.

![](_page_12_Figure_3.jpeg)

Fig. 7. Spectrum occupancy ratio of partial resource offloading approaches.

between the PRO\_PS and the PRO\_AS approach is reflected in the segmentation ratio. When the number of user requests is small, the spectrum occupancy ratio is relatively close. As the number of user requests increases, the spectrum occupancy ratio of the PRO\_PS approach is the closest to the ILP model and the PRO\_PS approach has 3.4% higher spectrum occupancy ratio than the ILP model. The spectrum occupancy ratio of the CCE approach is slightly higher than that of the PRO\_AS and PRO\_PS approaches because a large number of user requests are offloaded. The ARO approach adopts the processing method of complete offloading, and the number of links through the transmission path is large, so the spectrum occupancy ratio is always the highest.

Figure 8 illustrates the average hops of the ILP model and the heuristic approaches for varying numbers of user requests. It can be observed that the ALP approach maintains an average hops value of 1 since it processes all user requests locally. The ILP model optimizes both the number of occupied frequency slots and the average E2E latency, resulting in slightly higher average hops compared to the ALP approach. For the PRO\_PS approach, different types of user requests are classified and processed. Consequently, the average hops of the PRO\_PS approach closely resembles that of the ILP model, with only an 8.3% difference in average hops. When the number of user

![](_page_12_Figure_7.jpeg)

Fig. 8. Average hops of partial resource offloading approaches.

requests is small, the average hops of the PRO\_AS approach matches that of the PRO\_PS approach. However, as the number of user requests increases, more requests need to be split and processed, leading to an increase in average hops for the PRO\_AS approach, surpassing that of the PRO\_PS approach. Additionally, the CCE approach aims to minimize latency through cloud-side network cooperation without considering the occupancy of spectrum resources in the network. Hence, the average hops for the CCE approach is higher than that of the PRO\_AS approach. Finally, the ARO approach offloads all user requests, utilizing a large number of links, resulting in the highest average hops.

## B. Heuristic Approaches of Partial Resource Offloading with Dynamic Scenario in a 14-Node Network

In this section, we adopt the 14-node network topology shown in Fig. 5(b) to simulate proposed heuristic approaches of the partial resource offloading with the dynamic user requests. Let each edge server and fiber link contain 80 units of computing and 100 units of frequency slots, respectively. The cloud servers have infinite computing resources. The other network parameters are the same as in Section 8.A. The adjustable parameters of server importance degree are set as ε = 0.2 and ζ = 0.8. The adjustable parameter of the offloading decision variable are set as ϕ = 0.4, and ω = 0.6. 20000 user requests are launched in generating each data set. We then analyze the blocking probability, average E2E latency, spectrum occupancy ratio, and average hops of the heuristic approaches.

Figure 9 presents the blocking probability of the heuristic approaches under different traffic loads. It is evident that the blocking probability of the PRO\_PS approach is the lowest among the heuristics. This can be attributed to the PRO\_PS approach considering both the E2E latency and the computing resources of servers simultaneously. By adopting an average segmentation method, the PRO\_AS approach is less flexible in determining the partition proportion, resulting in a higher blocking probability compared to the PRO\_PS approach. The CCE approach aims to minimize latency by leveraging both cloud and edge computing. The task segmentation proportion is determined based on the proposed parameters of normalized backhaul communication capability and normalized cloud computing capability. However, the reasonable allocation of network link resources is not taken into account, leading to a higher blocking probability than that of the PRO\_AS approach. Furthermore, the ALP approach has lower blocking probability than the CEE approach when the traffic load is lower than 200 Erlang. However, as the traffic load exceeds 200 Erlang, the blocking probability of the ALP approach is larger than that of the CEE approach due to the single processing methods for the ALP approach. In addition, the ARO approach has the highest blocking probability among all the heuristic approaches since it does not consider task segmentation or offloading to other servers.

Figure 10 illustrates the average E2E latency of the heuristic offloading approaches. In the PRO\_PS approach, for indivisible services, the offloading decision variable and server importance degree are considered to determine whether and

![](_page_13_Figure_3.jpeg)

Fig. 9. Blocking probability of partial resource offloading approaches.

![](_page_13_Figure_5.jpeg)

Fig. 10. Average E2E latency of partial resource offloading approaches.

where to offload, resulting in effective latency reduction. For divisible services, a portion of the service is processed locally while the remaining part is offloaded to other regions. Overall, the PRO\_PS approach achieves latency reduction for both types of user requests, leading to the lowest average E2E latency among the heuristics. In comparison, the PRO\_AS approach does not yield as significant optimization results as the PRO\_PS approach, resulting in higher latency than the PRO\_PS approach. The CCE approach, despite its goal of minimizing latency, does not take into account the local processing of user requests. Therefore, the average E2E latency of the CCE approach is higher than that of the PRO\_PS and PRO\_AS approaches. Furthermore, the ARO approach exhibits higher E2E latency than the PRO\_AS approach due to its offloading all user requests. Lastly, while the ALP approach may neglect the transmission latency in local processing, the computing capacity of the local edge server is limited. As the server load increases, the processing speed decreases, leading to prolonged processing latency. Consequently, the ALP approach has the highest average E2E latency among all the heuristic approaches.

![](_page_13_Figure_8.jpeg)

Fig. 11. Spectrum occupancy ratio of partial resource offloading approaches.

Figure 11 displays the spectrum occupancy ratio of the heuristic approaches under varying traffic load. Unquestionably, the ALP approach exhibits the lowest spectrum occupancy ratio. This is primarily because the ALP approach does not require transferring user requests to other regions, resulting in minimal spectrum usage. In contrast, on the one hand, the PRO\_PS approach splits user requests for processing, necessitating two transmission paths to transfer the requests to different destination servers. As a result, the spectrum occupancy ratio of the PRO\_PS approach is higher than that of the ALP approach. On the other hand, the PRO\_AS approach evenly divides user requests, requiring the establishment of two transmission paths and thereby maintaining a consistently high spectrum occupancy ratio. For the CCE approach, its spectrum occupancy ratio is higher than that of the ALP and ARO approaches. However, its spectrum occupancy ratio is lower than that of the PRO\_PS and PRO\_AS approaches. The reason is that the CCE approach considers the collaborative cloud-edge offloading for each user request. The ARO approach offloads all user requests and utilizes a large number of links, resulting in a continuously higher spectrum occupancy ratio than ALP approach.

Figure 12 illustrates the average hops of the heuristic approaches under different traffic loads. The ALP approach, which processes all user requests locally, requires only one hop to transmit the requests, resulting in the lowest average hops. The PRO\_PS and PRO\_AS approaches utilize the concept of SID for server selection, with the only difference being the segmentation ratio. Consequently, the average hops for both approaches are nearly identical. However, the PRO\_PS and PRO\_AS approaches reduce latency by establishing two transmission paths for divisible services, leading to a slightly higher average hops compared to the ALP approach. Although the CCE approach leverages cloud and edge computing for cooperative processing of user requests, it does not consider local processing. Therefore, the average hops for the CCE approach exceeds that of the PRO\_PS and PRO\_AS approaches. Similarly, the ARO approach employs a full resource offloading mode, resulting in a larger number of

![](_page_14_Figure_3.jpeg)

Fig. 12. Average hops of partial resource offloading approaches.

links traversed in the transmission path. As a result, the ARO approach consistently exhibits the highest average hops.

# 9. CONCLUSION

This paper focuses on addressing the resource offloading problem in CE-EONs by investigating the optimal latency and location for offloading user requests. The primary objective is to reduce the average E2E latency, minimize the blocking probability, and optimize the allocation of network resources. To achieve these goals, we develop a novel ILP model of partial resource offloading that effectively reduces latency and optimizes the utilization of frequency slots. Additionally, we propose the PRO\_PS approach, which utilizes an optimal segmentation ratio to split user requests for processing. On the one hand, the simulation results show that the PRO\_PS approach can yield very close performance in terms of the E2E latency, spectrum efficiency, and average hops to that by the ILP models for a given set of user requests in the static traffic scenario. On the other hand, through extensive simulations in the dynamic traffic scenario, we can demonstrate the effectiveness of our proposed PRO\_PS approach in reducing the average E2E latency, lowering the blocking probability, and optimizing the network resource allocation compared to the existing CCE and traditional offloading approaches. Therefore, our results confirm that our proposed approach outperforms other approaches in achieving efficient resource offloading.

Funding. National Key Research and Development Program of China (2022YFB2903303); Natural Science Foundation of Jiangsu Province (BK20200099); Ministry of Science and ICT, South Korea (NRF-2022H1D3A2A0106367); Jiangsu Engineering Research Center of Novel Optical Fiber Technology, and Communication Network; Suzhou Key Laboratory of Advanced Optical Communication Network Technology.

#### REFERENCES

- 1. K. Zhang, S. Leng, Y. He, S. Maharjan, and Y. Zhang, "Mobile edge computing and networking for green and low-latency Internet of Things," IEEE Commun. Mag. 56(5), 39–45 (2018).
- 2. Y. Qi, L. Tian, Y. Zhou, and J. Yuan, "Mobile edge computingassisted admission control in vehicular networks: the convergence

- of communication and computation," IEEE Veh. Technol. Mag. 14(1), 37–44 (2019).
- 3. A. Bachoumis, N. Andriopoulos, K. Plakas, A. Magklaras, P. Alefragis, G. Goulas, A. Birbas, and A. Papalexopoulos, "Cloudedge interoperability for demand response-enabled fast frequency response service provision," IEEE Trans. Cloud Comput. 10, 123–133 (2022).
- 4. A. da Silva Veith, M. Dias de Assunção, and L. Lefèvre, "Latencyaware strategies for deploying data stream processing applications on large cloud-edge infrastructure," IEEE Trans. Cloud Comput. 11, 445–456 (2023).
- 5. S. Yin, Y. Jiao, C. You, M. Cai, T. Jin, and S. Huang, "Reliable adaptive edge-cloud collaborative DNN inference acceleration scheme combining computing and communication resources in optical networks," J. Opt. Commun. Netw. 15, 750–764 (2023).
- 6. B. Panchali, "Edge computing-background and overview," in Proceedings of the International Conference on Smart Systems and Inventive Technology (ICSSIT) (2018), pp. 580–582.
- 7. T. Taleb, K. Samdanis, B. Mada, H. Flinck, S. Dutta, and D. Sabella, "On multi-access edge computing: a survey of the emerging 5G network edge cloud architecture and orchestration," IEEE Commun. Surv. Tutorials 19, 1657–1681 (2017).
- 8. P. Mach and Z. Becvar, "Mobile edge computing: a survey on architecture and resource offloading," IEEE Commun. Surv. Tutorials 19, 1628–1656 (2017).
- 9. Y. Mao, C. You, J. Zhang, K. Huang, and K. B. Letaief, "A survey on mobile edge computing: the communication perspective," IEEE Commun. Surv. Tutorials 19, 2322–2358 (2017).
- 10. Q. Ou, Y. Wang, W. Song, N. Zhang, J. Zhang, and H. Liu, "Research on network performance optimization technology based on cloud-edge collaborative architecture," in Proceedings of the International Conference on Big Data, Artificial Intelligence and Internet of Things Engineering (ICBAIE) (2021), pp. 274–278.
- 11. H. Zhou, K. Jiang, X. Liu, X. Li, and V. C. M. Leung, "Deep reinforcement learning for energy-efficient computation offloading in mobileedge computing," IEEE Internet Things J. 9, 1517–1530 (2022).
- 12. Y. Miao, G. Wu, M. Li, A. Ghoneim, M. Al-Rakhami, and M. S. Hossain, "Intelligent task prediction and resource offloading based on mobile-edge cloud computing," Future Gener. Comput. Syst. 102, 925–931 (2020).
- 13. W. Fan, L. Yao, J. Han, F. Wu, and Y. Liu, "Game-based multitype task offloading among mobile-edge-computing-enabled base stations," IEEE Internet Things J. 8, 17691–17704 (2021).
- 14. M. Gao, R. Shen, L. Shi, W. Qi, J. Li, and Y. Li, "Task partitioning and offloading in DNN-task enabled mobile edge computing networks," IEEE Trans. Mob. Comput. 22, 2435–2445 (2023).
- 15. S. Wang, B. Chen, R. Liang, L. Liu, H. Chen, M. Gao, J. Wu, W. Ju, and P.-H. Ho, "Energy-efficient workload allocation in edge-cloud fiber-wireless networks," Opt. Express 30, 44186–44200 (2022).
- 16. L. Liu, W. Ma, B. Chen, M. Gao, H. Chen, and J. Wu, "Network resource optimization with latency sensitivity in collaborative cloud-edge computing networks," in Proceedings of the Asia Communications and Photonics Conference (ACP) and International Conference on Information Photonics and Optical Communications (IPOC) (2020).
- 17. L. Liu, R. Liang, S. Wang, H. Chen, M. Gao, B. Chen, and J. Wu, "Selective offloading network resource optimization approaches in collaborative cloud-edge computing networks," in Proceedings of the International Conference on Optical Communications and Networks (ICOCN) (2021).
- 18. L. Liu, B. Chen, W. Ma, H. Chen, M. Gao, W. Shao, J. Wu, L. Peng, and P. H. Ho, "Selective resource offloading in cloud-edge elastic optical networks," J. Lightwave Technol. 41, 6431–6445 (2023).
- 19. C. You, K. Huang, H. Chae, and B. Kim, "Energy-efficient resource allocation for mobile-edge resource offloading," IEEE Trans. Wireless Commun. 16, 1397–1411 (2017).
- 20. X. Tao, K. Ota, M. Dong, H. Qi, and K. Li, "Performance guaranteed resource offloading for mobile-edge cloud computing," IEEE Wireless Commun. Lett. 6, 774–777 (2017).
- 21. A. Al-Shuwaili and O. Simeone, "Energy-efficient resource allocation for mobile edge computing-based augmented reality applications," IEEE Wireless Commun. Lett. 6, 398–401 (2017).

- 22. J. Wu, Z. Cao, Y. Zhang, and X. Zhang, "Edge-cloud collaborative resource offloading model based on improved practical swarm optimization in MEC," in Proceedings of the International Conference on Parallel and Distributed Systems (ICPADS) (2019), pp. 959–962.
- 23. G. Peng, H. Wu, H. Wu, and K. Wolter, "Constrained multi-objective optimization for IoT-enabled resource offloading in collaborative edge and cloud computing," IEEE Internet Things J. 8, 13723–13736 (2021).
- 24. M. Huang, W. Liu, T. Wang, A. Liu, and S. Zhang, "A cloud–MEC collaborative task offloading scheme with service orchestration," IEEE Internet Things J. 7, 5792–5805 (2020).
- 25. K. Li, M. Tao, and Z. Chen, "A computation-communication tradeoff study for mobile edge computing networks," in Proceedings of the IEEE International Symposium on Information Theory (ISIT) (2019), pp. 2639–2643.
- 26. J. Ren, G. Yu, Y. He, and G. Y. Li, "Collaborative cloud and edge computing for latency minimization," IEEE Trans. Veh. Technol. 68, 5031–5044 (2019).
- 27. W. Shi, J. Zhang, R. Zhang, and K. Hu, "An area-based offloading policy for computing offloading in MEC-assisted wireless mesh network," in Proceedings of the IEEE/CIC International Conference on Communications in China (ICCC) (2019).
- 28. C. Yi, J. Cai, and Z. Su, "A multi-user mobile resource offloading and transmission scheduling mechanism for delay-sensitive applications," IEEE Trans. Mob. Comput. 19, 29–43 (2020).
- 29. Y. Mao, J. Zhang, and K. B. Letaief, "Dynamic resource offloading for mobile-edge computing with energy harvesting devices," IEEE J. Sel. Areas Commun. 34, 3590–3605 (2016).
- 30. J. Zhang, H. Guo, J. Liu, and Y. Zhang, "Task offloading in vehicular edge computing networks: a load-balancing solution," IEEE Trans. Veh. Technol. 69, 2092–2104 (2020).
- 31. F. Zhang and M. M. Wang, "Stochastic congestion game for load balancing in mobile-edge computing," IEEE Internet Things J. 8, 778–790 (2021).
- 32. P. H. Raj, "Extended Johnson's sequencing for load balancing in edge computing," in Proceedings of the International Conference on Intelligent Computing and Control Systems (ICICCS) (2021), pp. 142–146.
- 33. M. Jinno, B. Kozicki, H. Takara, A. Watanabe, Y. Sone, T. Tanaka, and A. Hirano, "Distance-adaptive spectrum resource allocation in spectrum-sliced elastic optical path network [Topics in Optical Communications]," IEEE Commun. Mag. 48(8), 138–145 (2010).
- 34. L. Wei and Z. Zuqing, "Dynamic service provisioning of advance reservation requests in elastic optical networks," J. Lightwave Technol. 31, 1621–1627 (2013).

![](_page_15_Picture_16.jpeg)

![](_page_15_Picture_17.jpeg)

**Ling Liu** received the B.E. degree in communications engineering from Soochow University, Suzhou, China, in 2019, where she is currently pursuing the M.S. degree in information and communication. Her current research interests include optical network design and edge-cloud computing networks.

![](_page_15_Picture_19.jpeg)

**Yuexuan Fan** received the B.E. degree in communication engineering from Soochow University, Suzhou, China, in 2019, where she is currently pursuing the M.S. degree in information and communication. Her current research interests include optical network design, edgecloud computing networks, and elastic optical networks.

![](_page_15_Picture_21.jpeg)

**Weidong Shao** received the B.E. degree from Huazhong University of Science and Technology (HUST), Wuhan, China, in 1990; the M.S. degree from Qufu Normal Univesity, Qufu, China, in 1999; and the Ph.D. degree from Shanghai Institute of Technical Physics, Chinese Academy of Science, in 2002. He is currently an associate professor with the School of Electronic and Information Engineering, Soochow University, Suzhou, China. His current research

interests include optical network design, network survivability, and elastic optical networks.

![](_page_15_Picture_24.jpeg)

**Mingyi Gao** received the Ph.D. degree in information and communication engineering from Shanghai Jiao Tong University, Shanghai, China, in 2007. She was a Research Fellow at the Japan Society for the Promotion of Science (JSPS) with the University of Tokyo, Tokyo, Japan, from 2007 to 2009. From 2009 to 2013, she was with the National Institute of Advanced Industrial Science and Technology, Tsukuba, Japan. She is currently an associate professor in the School of Electronic

and Information Engineering, Soochow University. Her current research interests include coherent optical communication, multicarrier PON, digital signal processing, machine learning, and FPGA.

![](_page_15_Picture_27.jpeg)

**Hong Chen** received the M.S. degree in electronics and communication engineering from Soochow University, Suzhou, China in 2008. She is currently an associate professor in the School of Electronics and Information, Soochow University. Her current research interests include optical networking technology and network resource optimization.

![](_page_15_Picture_29.jpeg)

**Weiguo Ju** received the Ph.D. degree from Beijing University of Posts and Telecommunications, Beijing, China, in 2013. He is currently a senior engineer in the Institute of ICT Technology, China Information Consulting & Designing Institute Co., Ltd. His current research interests include software-defined optical network and edge-cloud computing networks.

![](_page_16_Picture_3.jpeg)

**Pin-Han Ho** (Fellow, IEEE) received the Ph.D. degree from Queens University, Kingston, ON, Canada, in 2002. He is currently a full professor in the Department of Electrical and Computer Engineering, University of Waterloo. He is the author/coauthor of over 400 refereed technical papers and several book chapters and the coauthor of two books on Internet and optical network survivability. His current research interests cover a wide range of topics in broadband wired and

wireless communication networks, including wireless transmission techniques, mobile system design and optimization, and network dimensioning and resource allocation. He holds the ranks of IEEE Fellow and Professional Engineer Ontario (PEO).

![](_page_16_Picture_6.jpeg)

**Jason P. Jue** (Senior Member, IEEE) received the B.S. degree in electrical engineering and computer science from the University of California, Berkeley, in 1990; the M.S. degree in electrical engineering from the University of California, Los Angeles, in 1991; and the Ph.D. degree in computer engineering from the University of California, Davis, in 1999. He is currently a Professor with the Department of Computer Science at the University of Texas at Dallas. His

current research interests include optical networks and network survivability.

![](_page_16_Picture_9.jpeg)

**Gangxiang Shen** (Fellow, Optica, Senior Member, IEEE) received the B.E. degree from Zhejiang University, China; the M.Sc. degree from Nanyang Technological University, Singapore; and the Ph.D. degree from the University of Alberta, Canada, in 2006. He is currently a distinguished professor with the School of Electronic and Information Engineering, Soochow University, China. Before he joined Soochow University, he was a lead engineer with

Ciena, Linthicum, Maryland. He was also an Australian ARC postdoctoral

fellow with the University of Melbourne. He has authored and coauthored more than 200 peer-reviewed technical papers. His research interests include integrated optical and wireless networks, spectrum efficient optical networks, and green optical networks. He is a lead guest editor of the *IEEE Journal on Selected Areas in Communications* Special Issue on Next-Generation Spectrum-Efficient and Elastic Optical Transport Networks and a guest editor of the *IEEE Journal on Selected Areas in Communications* Special Issue on Energy-Efficiency in Optical Networks. He was an associate editor for the IEEE/Opitca *Journal of Optical Communication and Networking*, is currently an associate editor for the IEEE/Optica *Journal of Lightwave Technology* and *IEEE Networking Letters*, and is an editorial board member of *Optical Switching and Networking* and *Photonic Network Communications*. He was a secretary of the IEEE Fiber-Wireless (FiWi) Integration Sub-Technical Committee. He was the recipient of the Young Researcher New Star Scientist Award in the 2010 Scopus Young Researcher Award Scheme in China. He was the recipient of the Izaak Walton Killam Memorial Award from the University of Alberta and a Canadian NSERC Industrial Research and Development Fellowship. He was selected as a Highly Cited Chinese Researcher by Elsevier in 2014–2018. He was elected as an IEEE ComSoc Distinguished Lecturer for 2018–2019. He is also a voting member of the IEEE ComSoc Strategic Planning Standing Committee (2018–2019) and is currently a TPC member of both OFC and ECOC.
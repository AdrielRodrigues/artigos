# Energy-Efficient Flexible Functional Splitting in Latency-Constrained O-RAN

Matias Romario Pinheiro Dos Santo[s](https://orcid.org/0000-0002-8356-157X) ´ , Rodrigo Izidoro Tinini, and Gustavo Bittencourt Figueiredo [,](https://orcid.org/0000-0001-9756-378X) *Senior Member, IEEE*

*Abstract*—Cloud Radio Access Network (CRAN) has become a popular approach for migrating Baseband Units (BBUs) to the cloud using Network Functions Virtualization (NFV). However, bandwidth and latency constraints are significant challenges for CRAN deployment. To address these limitations, Cloud-Fog RAN (CF-RAN) has been proposed as an alternative solution. In this paper, we consider a cutting-edge CF-RAN scenario with different functional-split choices of virtualized BBUs with varying bandwidth and latency constraints. We propose an Integer Linear Programming (ILP) model to optimize functional split and allocate resources for optimal virtualized BBU placement, with the objective of minimizing power consumption. Our approach includes a novel queuing delay model based on the eCPRI standard. We also introduce a heuristic to address scalability issues. Dynamic simulations show that our method improves network availability by 35% and optimizes power consumption by 9.93%, outperforming prior studies. Our findings contribute to developing efficient CF-RAN systems and demonstrate the effectiveness of our proposed approach.

*Index Terms*—6G, O-RAN, flexible functional splitting, VPON, QoS.

#### I. INTRODUCTION

T HE emergence of sixth-generation mobile networks (6G) will demand highly adaptive and efficient Cloud Radio Access Network (RAN) architectures. Cloud Radio Access Networks (CRAN) have gained attention for supporting high traffic demands flexibly and efficiently. However, strict endto-end (E2E) delay constraints and limited transmission and processing capacity have hindered their adoption [\[1\].](#page-12-0) Hybrid architectures like Cloud-Fog RAN (CF-RAN) and Open-RAN (O-RAN) leverage Cloud and Fog computing paradigms to address these limitations [\[2\],](#page-12-1) [\[3\].](#page-12-2)

<span id="page-0-2"></span><span id="page-0-1"></span>To ease O-RAN fronthaul development, the 3GPP has endorsed Functional Split (FS) to reduce overhead by moving part of the baseband processing closer to Open Radio Units

Received 3 March 2025; revised 13 August 2025; accepted 3 December 2025. Date of publication 10 December 2025; date of current version 23 December 2025. This work was supported in part by the National Council for Scientific and Technological Development (CNPq) under Grant 313623/2023-6, in part by the Fundac¸ao de Amparo ˜ a Pesquisa do Estado da Bahia ` (FAPESB) INCITE under Grant PIE0002/2022, and in part by the Brazilian Federal Agency for Support and Evaluation of Graduate Education (CAPES). The editor coordinating the review of this article was A. Nag. *(Corresponding author: Gustavo Bittencourt Figueiredo.)*

Matias Romario Pinheiro dos Santos is with the Federal University of Bahia, ´ Salvador 40170-115, Brazil, and also with the Instituto Federal do Ceara,´ Acopiara, Ceara 63560-000, Brazil (e-mail: matias.romario@ifce.edu.br). ´

Rodrigo Izidoro Tinini is with the Federal University of ABC, Sao Paulo ˜ 09210-580, Brazil (e-mail: rodrigo.tinini@ufabc.edu.br).

Gustavo Bittencourt Figueiredo is with the Federal University of Bahia, Salvador 40170-115, Brazil (e-mail: gustavobf@ufba.br).

Digital Object Identifier 10.1109/TGCN.2025.3642779

(O-RU). The Open Central Unit (O-CU) handles higher-layer processing in a cloud data center, while the Open Distributed Unit (O-DU) handles lower-layer processing near users. This division reduces required bandwidth and relaxes delay requisites. Flexible Functional Split (FFS) extends FS by allowing Mobile Network Operators (MNOs) to dynamically select FS options based on operational needs and resources, serving different QoS levels [\[4\],](#page-12-3) [\[5\],](#page-12-4) [\[6\],](#page-12-5) [\[7\].](#page-12-6) Enhanced Common Public Radio Interface (eCPRI) [\[8\]](#page-12-7) further decreases bandwidth requisites by transmitting digitized radio signals over Ethernet, IP, and UDP.

<span id="page-0-7"></span><span id="page-0-6"></span><span id="page-0-5"></span><span id="page-0-4"></span><span id="page-0-3"></span>However, deploying eCPRI with FFS in O-RAN fronthaul presents challenges, especially regarding energy efficiency and latency. Increased O-DU activation to host baseband functions escalates energy consumption but alleviates fronthaul traffic and relaxes delay tolerances [\[9\],](#page-12-8) [\[10\],](#page-12-9) [\[11\].](#page-12-10) Addressing this trade-off is central to advancing efficient and resilient 6G O-RAN frameworks.

<span id="page-0-10"></span><span id="page-0-9"></span><span id="page-0-8"></span>Proper function splitting placement and fronthaul dimensioning are essential, requiring scalable approaches to address latency constraints while balancing power consumption and centralization benefits [\[12\],](#page-12-11) [\[13\],](#page-12-12) [\[14\].](#page-12-13) Although FFS reduces data transported over fronthaul links, packetized eCPRI operation may introduce additional latency due to queuing at transmission links and processing entities.

<span id="page-0-13"></span><span id="page-0-12"></span><span id="page-0-11"></span><span id="page-0-0"></span>Most literature fails to address the intricacies of latencyconstrained Flexible Functional Splitting with energy efficiency for O-RAN. Studies often focus on isolated aspects, such as latency reduction or energy efficiency, without integrating both within a flexible functional splitting framework [\[15\],](#page-12-14) [\[16\],](#page-12-15) [\[17\],](#page-13-0) [\[18\].](#page-13-1) For instance, [\[19\]](#page-13-2) emphasized that while centralizing baseband operations reduces energy consumption but increases transport capacity demands, dispersed placement increases energy usage but lowers network capacity needs.

<span id="page-0-18"></span><span id="page-0-17"></span><span id="page-0-16"></span><span id="page-0-15"></span><span id="page-0-14"></span>The latency thresholds and queuing strategies adopted in this work are based on several applications, including time-sensitive applications, as specified for URLLC and Time-Sensitive Networking service classes. Applications such as remote robotic control, autonomous vehicular networks, and industrial automation (Industry 4.0) impose stringent oneway latency requirements—often below 100µs for fronthaul transport— as defined in 3GPP specifications TS 22.261 and TS 23.501.

In this paper, we provide a holistic solution for sizing an O-RAN optical fronthaul using FFS and eCPRI. We propose a comprehensive queuing model that considers data, synchronization, and control connections between RU and O-CU/O-DU. Additionally, we introduce an Integer Linear Programming (ILP) model to optimally determine the FFS for each RU, minimizing network energy consumption while considering QoS latency constraints and processing resources. Lastly, we present a graph-based model and heuristic algorithm as alternatives to ILP for larger networks. Our results show that the ILP identifies optimal FFS solutions, and the heuristic generates comparable sub-optimal solutions with reduced execution time, outperforming existing CF-RAN solutions by reducing power consumption by 9.93%. In addition, a graph-based heuristic is proposed as an online and scalable alternative, capable of dynamically reallocating functional splits and processing nodes in response to traffic surges, ensuring latency compliance.

The rest of this paper is organized as follows: Section [II](#page-1-0) presents the literature review. Section [III](#page-2-0) overviews CF-RAN architecture and functional split choices. Section [IV](#page-4-0) proposes a delay model for eCPRI and the mathematical model to solve the FS option selection, resource allocation, and power minimization. Section [V](#page-7-0) presents our heuristic algorithm and the graph-theory-based model. Section [VI](#page-8-0) explains numerical results. Section [VII](#page-11-0) presents concluding remarks and future study guidelines.

#### <span id="page-1-2"></span><span id="page-1-1"></span>II. RELATED WORKS

<span id="page-1-0"></span>Research on optimal placement of vBBUs in CRAN and CF-RAN has explored various approaches leveraging Virtual Network Functions (VNFs) to efficiently host baseband functions on network nodes [\[20\],](#page-13-3) [\[21\].](#page-13-4) Efficient network service allocation in NFV environments is vital for ensuring quality of service and scalability in 5G networks, with a combination of techniques applied to this end. For instance, [\[22\]](#page-13-5) presents a solution based on A\* search and Branchand-Bound. As many approaches assume static scenarios, which may not reflect dynamic environments, the authors incorporated machine learning to adapt service allocation to shifting network demands.

<span id="page-1-6"></span><span id="page-1-5"></span><span id="page-1-4"></span><span id="page-1-3"></span>Mathematical and heuristic models have been widely used to tackle key issues like reducing delay, bandwidth, and processing resource usage [\[23\],](#page-13-6) [\[24\],](#page-13-7) [\[25\].](#page-13-8) However, these methods often struggle in dynamic environments due to scalability limitations or simplified assumptions about network traffic behavior.

Regarding FS-options, [\[14\]](#page-12-13) proposed a Constraint Programming (CP) model to minimize power and midhaul bandwidth consumption in Hybrid-CRAN through optimal functional splits. Their findings underscore the interdependence between energy and bandwidth in split decisions, a critical aspect addressed in our study. Similarly, while [\[23\]](#page-13-6) optimized fronthaul resources under latency constraints, their model lacks flexibility for hybrid architectures. To bridge these gaps, our paper integrates an ILP model with a queue-based delay model grounded in the eCPRI standard, addressing scalability and latency efficiency.

<span id="page-1-7"></span>Authors in [\[26\]](#page-13-9) examined baseband function placement in a 5G metro network using an ILP model focused on energy efficiency. Although effective in static conditions, their model does not cater to dynamic CF-RAN environments. Our approach, combining ILP and heuristic methods, targets CF-RAN's variable demands, supporting energy efficiency while maintaining scalability. This dual strategy differentiates our work from [\[26\]](#page-13-9) and others by optimizing resources under fluctuating service demands.

Dynamic and flexible functional splitting in virtualized and Open RAN environments has emerged as a key strategy for optimizing both performance and operational cost, particularly in the context of increasingly heterogeneous and energy-aware network deployments. To enable real-time adaptability, recent research has explored the integration of machine learning (ML) and reinforcement learning (RL) techniques to dynamically decide the most suitable functional split points between centralized and distributed units.

<span id="page-1-8"></span>In [\[27\],](#page-13-10) a constrained deep reinforcement learning (CDRL) approach is proposed for selecting optimal functional splits in virtualized RANs. The method employs a sequence-tosequence LSTM architecture to manage the high-dimensional action space, combined with a constrained policy gradient to enforce service-level constraints. The solution achieves nearoptimal results, with an optimality gap below 0.05%, while significantly reducing computational time compared to exact optimization methods. It also demonstrates cost savings when compared to fixed-function C-RAN and D-RAN architectures.

<span id="page-1-9"></span>In the context of energy-efficient Open RAN scenarios, Pamuklu et al. [\[28\]](#page-13-11) present an RL-based framework for dynamically selecting functional splits in networks powered by renewable energy. The RL agent learns to adapt split decisions in response to fluctuations in both energy availability and traffic load, with the goal of minimizing operational costs. The model is trained and validated using real-world solar irradiance and traffic traces, and additionally provides recommendations for the optimal sizing of solar panels and battery storage for sustainable RAN deployment.

<span id="page-1-13"></span><span id="page-1-12"></span><span id="page-1-11"></span><span id="page-1-10"></span>For latency-specific challenges with eCPRI, various studies explore mitigation techniques [\[29\],](#page-13-12) [\[30\],](#page-13-13) [\[31\].](#page-13-14) Authors in [\[32\]](#page-13-15) demonstrated network slicing's effectiveness in reducing 5G latency, but these studies lack a comprehensive model integrating latency-aware functional splits. Our work addresses this by incorporating a delay-aware queuing model into the ILP.

<span id="page-1-14"></span>In queuing models, authors [\[6\],](#page-12-5) [\[15\],](#page-12-14) [\[33\]](#page-13-16) evaluated systems from M/M/1 to G/G/1 for network delay prediction. Our model differs by capturing traffic behaviors under Split E, I, and D scenarios, applying deterministic D/D/1 or stochastic M/M/1 based on traffic properties. Incorporating these delay estimates into our ILP enables dynamic FS-options tailored to each RU's requirements. To our knowledge, this is the first ILP model in CF-RAN to use a queuing model for split decision-making, addressing both static and dynamic scenarios.

Unlike the aforementioned works, we combine ILP, heuristics, and a queuing model to account for delay in each splitting option. The queuing model provides latency bounds to the ILP, which selects the lowest-latency FS-option for each RU. To the best of our knowledge, no other work presents an ILP model where delay-related decisions are informed by an analytical queuing model in a CF-RAN architecture. Furthermore, while most studies focus on static or dynamic scenarios separately,

![](_page_2_Figure_2.jpeg)

<span id="page-2-1"></span>Fig. 1. Illustration of O-RAN architecture showing logical interfaces and functional split options across processing nodes.

our work addresses both by proposing a latency-aware, flexible functional splitting approach that offers energy-efficient and scalable solutions for Cloud Fog RAN, presenting a more comprehensive solution than previous works.

# III. SYSTEM ARCHITECTURE

<span id="page-2-0"></span>In this section, we outline the specifics of the O-RAN architecture considered in this work. The architecture consists of an overlay network with a RAN processing layer and an optical transmission layer, as illustrated in Fig [1.](#page-2-1) The RAN processing layer includes multiple O-RUs and two types of processing nodes: fog nodes and the cloud, which host O-DUs and O-CUs, respectively. User Equipment (UE) connects to O-RUs, which collect their baseband signals and forward them to the processing nodes for further processing.

The O-RAN architecture considered in this work leverages virtualization to enable the dynamic deployment of O-DUs and O-CUs across the processing nodes. A key advantage of the virtualization of O-DUs/O-CUs is the ability to manage power consumption based on real-time network demand, resulting in significant energy savings. For example, during periods of low network demand, processing nodes—and by extension, the O-DUs and O-CUs can be deactivated to conserve power. Therefore, efficient deployment of O-DUs/O-CUs is crucial for optimizing resource utilization and ensuring the scalability of the network infrastructure [\[34\].](#page-13-17)

In the optical domain, a key aspect is the integration of multiple types of interfaces within Virtual Passive Optical Networks (VPONs). This integration ensures that the fronthaul interface not only connects O-RUs to O-DUs and O-CUs but also supports other critical network interfaces. VPONs serve as a central enabler for seamless network operations, efficiently transmitting traffic across several interfaces, including the F1, Xn, and E1 interfaces [\[1\].](#page-12-0) In the architecture considered in this work, multiple interfaces share the same optical channel using Time Division Multiplexing (TDM). The F1 interface handles the connection between O-DUs and O-CUs [\[1\],](#page-12-0) while the eCPRI protocol connects O-RUs to O-CUs, transmitting packetized radio signals. Different functional split options, such as FS-options E, I, and D, define the bandwidth and latency requirements between O-RUs, O-DUs, and O-CUs. Also, in the optical transmission layer, the three eCPRI connections—synchronization, control, and user data—are multiplexed using TDM. This integration ensures efficient utilization of available bandwidth while meeting the distinct requirements of each connection. For example, the deterministic nature of synchronization and control traffic allows for predictable scheduling, while the bursty nature of user data traffic requires dynamic resource allocation to prevent congestion and excessive queuing delays.

<span id="page-2-2"></span>In the optical transmission layer, we assume that O-RUs are connected to processing nodes via a two-level Time-Wavelength Division Multiplexing Passive Optical Network (TWDM-PON). Each O-RU is linked to an Optical Network Unit (ONU), which transmits data to virtualized Optical Line Terminals (vOLTs) deployed in the processing nodes. Line cards within the vOLTs receive traffic from the ONUs/O-RUs and forward it to the processing entities. Multiple O-RUs share a specific VPON, transmitting their data to a common processing node by utilizing a wavelength channel in a time-division manner. VPONs enable ONUs to dynamically tune to available wavelengths, optimizing resource usage and improving overall network performance. The first-level optical splitter aggregates traffic from a group of ONUs onto a feeder fiber, while the second-level splitter further aggregates traffic from multiple feeders and directs it to the corresponding line card, which then forwards it to the vOLT.

By employing Functional Split Selection (FFS), the processing load at each node varies according to the traffic demand from the O-RUs. The number of active O-DUs and O-CUs is determined by the chosen functional split and the network's baseband processing requirements. Efficiently solving the FFS selection problem is essential for achieving power-efficient O-RAN operation, as it aims to deploy the required O-DUs and O-CUs while minimizing the number of active processing nodes. A typical solution for it involves deploying O-DUs/O-CUs on the fewest possible processing nodes. However, this approach can increase overall fronthaul traffic on a few VPONs/links, leading to significant queuing delays at transmission queues of ONUs. This, in turn, raises the latency experienced by O-RUs and their connected UEs, ultimately degrading the QoS for user applications.

Therefore, a key aspect of O-RAN operation is solving the FFS selection problem in a power-efficient manner while minimizing the number of processing nodes needed to deploy the O-DUs and O-CUs required to meet the network demand and yet keeping overall network latency within pre-established limits. In section [III-A,](#page-3-0) we will explore the functional splitting enabled by eCPRI and introduce the FFS proposal.

#### <span id="page-3-0"></span>*A. Functional Splitting Options*

Functional splitting optimizes the allocation of baseband processing tasks across Radio Units (O-RUs), cloud, and fog nodes to enhance flexibility and performance in the O-RAN. The eCPRI protocol defines key split options—Split E, I, D, and B—integrated into the O-RAN TWDM-PON architecture. Each O-RU connects to its assigned processing node via dedicated optical channels with dynamically adjusted bandwidth, ensuring reliable latency and throughput for realtime applications.

The Split E centralizes most of the processing in the cloud, retaining only RF functions in the O-RU, such as transmitting and receiving. Split I performs Fast Fourier Transformation (FFT), modulation, and other functions locally, reducing the bit rate to 40% relative to Split E. Split D offloads PHY-layer tasks locally, while MAC and network layers remain in the cloud, reducing fronthaul bandwidth at the expense of more stringent latency requirements. Split B executes RLC and buffer functions locally, significantly easing latency constraints but with limitations in coordinated features like CoMP.

The estimated bandwidth requirements for each FS option are given by:

<span id="page-3-1"></span>
$$\begin{cases} \textbf{Split E} = A \times S_r \times S_{f,iq} \times 2 \times N_p \times \left(\frac{16}{15}\right) \times \left(\frac{N_{RB}}{12}\right) \\ \times \left(\frac{14}{12}\right) \\ \textbf{Split I} = N_{RB} \times N_{sym} \times N_{layer} \times S_{iq} \times 2 + O_{phy,D} \\ \textbf{Split D} = PR_u + O_{MAC,u} \\ \textbf{Split B} = PR_u + OPR_u \end{cases}$$

$$(1)$$

<span id="page-3-2"></span>Following the formulation adapted from [\[35\]](#page-13-18) and aligned with 3GPP TR 38.801 and IEEE 1914.1, Equation [1](#page-3-1) provides a bandwidth estimation for each functional split based on the placement of baseband functions and traffic encapsulation requirements. The variables are defined as follows: A denotes the number of antennas (dimensionless, e.g., A = 2 for 2 × 2 MIMO); S<sup>r</sup> is the baseband sampling rate in MS/s (e.g., S<sup>r</sup> = 30.72 MS/s for a 20 MHz LTE channel); Sf,iq represents the number of bits per I/Q sample (bits/sample, typically Sf,iq = 15 bits); N<sup>p</sup> is the number of physical ports (dimensionless, e.g., one per antenna branch); NRB is the number of allocated resource blocks (dimensionless, e.g., NRB = 100 for 20 MHz bandwidth); Nsym is the number of OFDM symbols per subframe (dimensionless, typically Nsym = 14); Nlayer refers to the number of MIMO layers (dimensionless, up to Nlayer = 2 in our simulations); Siq is the number of bits per complex modulation symbol (bits/symbol, e.g., Siq = 6 bits for 64-QAM); Ophy,D accounts for PHY-layer overhead as a dimensionless factor (e.g., including FEC and CRC); P R<sup>u</sup> is the user-specific payload rate in Mb/s after MAC scheduling; OMAC,u is the MAC-layer overhead per user in Mb/s (e.g., HARQ processes and MAC headers); and OP R<sup>u</sup> includes additional overhead from upperlayer protocols in Mb/s, particularly PDCP and RLC. The constants 16/15 and 14/12 are dimensionless overhead factors that model typical line-coding and framing overheads present in practical fronthaul protocols such as CPRI and eCPRI.

where parameters such as A (number of antennas per sector), S<sup>r</sup> (sampling rate), and NRB (number of resource blocks) can vary depending on specific 5G implementations. These formulas provide baseline bandwidth estimates but can fluctuate with real-time network conditions due to eCPRI's variable packetization rates. By dynamically adjusting processing distribution and bandwidth allocation, FFS options support a range of latency-sensitive applications in CF-RAN, offering a scalable and efficient response to 6G's demands.

*1) Flexible Functional Splitting:* Flexible Functional Splitting (FFS) enhances resource allocation in 5G by dynamically distributing protocol stack functions between the O-CU and O-DU, allowing adaptation to varying traffic loads. Unlike fixed splits, FFS offers finer control over network resources, optimizing performance across diverse scenarios. Each split—such as Split E with high centralization or Split D with local PHY processing—presents unique bandwidth and latency profiles, affecting queuing in the ONUs and transmission demands (Table [I\)](#page-4-1).

| Split Option | Functional Configuration                | Transmission Characteris-         | Bandwidth (Mb/s) |
|--------------|-----------------------------------------|-----------------------------------|------------------|
|              |                                         | tics                              |                  |
| Split E      | I/Q sample transport over eCPRI; high   | 256-QAM, 2x2 MIMO,                | 1966             |
|              | fronthaul demand                        | 20 MHz, $f_s = 30.72 \text{ MHz}$ |                  |
| Split I      | Frequency-domain I/Q transport; partial | 256-QAM, 2x2 MIMO,                | 674.4            |
|              | PHY centralized                         | 20 MHz, 14 OFDM                   |                  |
|              |                                         | symbols                           |                  |
| Split D      | MAC-PHY split; user-level scheduling    | Scheduled data, 2x2 MIMO,         | 119              |
|              | in Fog nodes                            | MAC + overhead                    |                  |
| Split B      | PDCP-RLC split; minimal fronthaul re-   | Payload + PDCP/RLC over-          | 44               |
|              | quirement                               | head                              |                  |

<span id="page-4-1"></span>TABLE I

COMPARISON OF FFS SPLITS AND EXPECTED BANDWIDTH

![](_page_4_Picture_4.jpeg)

<span id="page-4-2"></span>(a) Split E and I.

(b) Split D and B.

Fig. 2. Functional split architecture in eCPRI, with deterministic connections (control and synchronization) for splits E and I (CBR), and variable traffic connections (user data) for splits D and B.

#### IV. QUEUE AND MATHEMATICAL MODEL

<span id="page-4-0"></span>In this section, we formally define and present a queueing and an ILP model used to drive the decisions about the adopted splitting option. We start by discussing the proposed queueing model to determine the latency upper bounds that would be experienced for each split option. For simplicity, we assume that all RUs connected to a single ONU generate traffic in a synchronized fashion. The proposed model considers two distinct scenarios. The first scenario, shown in Fig 2(a), corresponds to functional splits E and I. In that case, as discussed in Section III-A, O-RUs generate I/Q samples and transmit them in Constant Bit Rate (CBR) to centralized baseband processing functions in a central facility.

The latency thresholds and queuing strategies adopted in this work are based on several applications, including time-sensitive applications, as specified for URLLC and Time-Sensitive Networking service classes. Applications such as remote robotic control, autonomous vehicular networks, and industrial automation (Industry 4.0) impose stringent one-way latency requirements—often below  $100\mu$ s for fronthaul transport— as defined in 3GPP specifications TS 22.261 and TS 23.501.

# A. Queuing Delay Model

To formalize the analysis, we define the set  $S = \{E, I, D, B\}$ , which represents all possible functional split options in the modeled system. For this first scenario, however, we restrict our focus to the options E (Split E) and I (Split I). Thus, we consider the subset  $\mathcal{I} = \{E, I\} \subset S$ , where  $\mathcal{I}$  encapsulates the specific modes under investigation.

In these modes, we assume that all RUs are synchronized and the traffic generated by either Split E or I is modeled by

a D/D/1 queue. Thus, the maximum delay is given by:

<span id="page-4-3"></span>
$$d^{i} = \frac{\mu_{i} - \lambda_{i}}{\mu_{i} \lambda_{i}}, \quad i \in \mathcal{I}, \tag{2}$$

where  $\mu_E = \mu_{rc}$  represents the optical fronthaul capacity of the O-RU-to-O-CU Split E,  $\mu_I = \mu_{fc}$  represents the optical fronthaul capacity of the O-DU-to-O-CU in Split I, and  $\lambda_i$  is the generated traffic rate for each respective split option as shown in Fig 2(a).

The second scenario, illustrated in Fig. 2(b), corresponds to Splits B and D. To maintain consistency with the treatment of splits E and I, we now extend the same modeling principles to those splits. For them, the user's traffic plays a pivotal role; therefore, in this second scenario, unlike the fronthaul queueing modeling works proposed in the literature [36], [37], in this work, we consider individually the three simultaneous connections, namely synchronization, control, and user connection, established between the O-RU and the O-DU/O-CU. Moreover, the total delay for the splits B and D is composed of two segments: the delay between the O-RU and the O-DU  $(d_{rd}^i)$  and the delay between the O-DU and the O-CU  $(d_{dc}^i)$ :

<span id="page-4-6"></span><span id="page-4-5"></span><span id="page-4-4"></span>
$$d_{max}^{i} = d_{rd}^{i} + d_{dc}^{i}, \quad i \in S \setminus \mathcal{I}, \tag{3}$$

where  $S \setminus \mathcal{I} = \{B, D\}$  represents the remaining splits in the set S. As mentioned before, for these splits, the fronthaul traffic is dependent on user traffic characteristics. Each path segment j experiences different types of traffic: user data (u), control (c), and synchronization (s). The maximum delay in each segment is determined by:

$$d_i^i = \max\{d_u^i, d_c^i, d_s^i\} \tag{4}$$

where  $d_u^i$ ,  $d_c^i$ , and  $d_s^i$  represent the delays for user data, control, and synchronization traffic, respectively.

Control and synchronization traffic follow a CBR pattern. For these types of traffic, we maintain the same modeling as used for splits E and I, adopting a **D/D/1 queue**. The delay for control and synchronization traffic in each segment is given by:

$$d_j^i = \left[\frac{\mu - \lambda_j^i}{\mu \cdot \lambda_j^i}\right]_{rd} + \left[\frac{\mu - \lambda_j^i}{\mu \cdot \lambda_j^i}\right]_{dc} \tag{5}$$

The first term  $\left[\frac{\mu-\lambda_j^i}{\mu\cdot\lambda_j^i}\right]_{rd}$  represents the delay in the O-RU-to-O-DU segment, the second term  $\left[\frac{\mu-\lambda_j^i}{\mu\cdot\lambda_j^i}\right]_{dc}$  represents the delay in the O-DU-to-O-CU segment. Note that, we consider

<span id="page-5-0"></span>TABLE II NOTATION USED FOR THE MODEL

| Symbol                                           | Definitions                                                                                                                  |  |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|--|
| Sets                                             |                                                                                                                              |  |
| $i \in R$                                        | set of O-RU traffic demands $i$                                                                                              |  |
| $n \in N$                                        | set of processing nodes $n$                                                                                                  |  |
| $w \in W$                                        | set of available wavelengths $w$                                                                                             |  |
| $s \in S$                                        | set of split options $s$                                                                                                     |  |
| Parameters                                       |                                                                                                                              |  |
| $B_i^s$                                          | bandwidth demand of O-RU $i$ according to the split $s$                                                                      |  |
| $B_w$                                            | capacity of wavelength $w$                                                                                                   |  |
| $P_i^s$                                          | processing demand of O-RU demands $i$ according to the split $s$                                                             |  |
| $\begin{array}{c} B_w \ P_i^s \ P_n \end{array}$ | processing capacity of node $n$                                                                                              |  |
| M                                                | a very big number                                                                                                            |  |
| $C_n$                                            | power cost of node $n$                                                                                                       |  |
| $C_{lc}$                                         | power cost of a $LC$                                                                                                         |  |
| $C_{onu}$                                        | power cost of a $onu$                                                                                                        |  |
| $C_{split}$                                      | cost for a $FS-option$                                                                                                       |  |
| $D_{max}^s$                                      | maximum latency tolerated in the split s                                                                                     |  |
| $D_{total_n}$                                    | total latency in node $n$                                                                                                    |  |
| Binary Variables                                 |                                                                                                                              |  |
| $y_{wns}^i$                                      | 1 if the traffic demand $i$ is processed at node $n$ delimited by split $s$ being transmitted at the VPON $w$ , 0 otherwise. |  |
| $z_{wn}$                                         | 1 if wavelength $w$ is allocated to node $n$ , 0 otherwise.                                                                  |  |
| $x_n$                                            | 1 if processing functions and elements of node $n$ is activated, 0 otherwise.                                                |  |
| $d_{in}$                                         | 1 if demand of $i$ was allocated to node $n$ , 0 otherwise.                                                                  |  |
| $\delta_{is}$                                    | 1 if demand of $i$ is associated with split option $s$ , 0 otherwise.                                                        |  |
| $t_{isn}$                                        | 1 if demand of $i$ has it split option $s$ being processing at node $n$ , 0 otherwise.                                       |  |

in this case that all traffic sources are synchronized, thus, resulting in CBR traffic.

As for the user traffic, to ensure bounded delay, we assume that it is admitted under a Token Bucket Admission Control (TBAC) policy, which regulates incoming user's traffic based on two parameters: r, the admitted rate, and β, the maximum burst size. The maximum queuing delay due to a burst event is given by:

$$d_u^i = \frac{1}{\mu_u - \lambda_u^i} \left( \beta + \frac{\lambda_u^i - r}{r} \right) \tag{6}$$

In this context, d i u represents a significant part of the total delay, as it reflects the impact of variable user traffic on the system. An increase in d i u can lead to an overall increase in total delay, affecting the performance of the system as a whole.

Finally, we express the overall worst-case delay in terms of bursty traffic and service capacity:

$$d_{j}^{i} = \frac{1}{\mu_{i} - \lambda_{j}^{i}} \left( \beta + \frac{\lambda_{j}^{i} - r}{r} \right) + \frac{1}{\mu_{fc} - \lambda_{j}^{i}} \left( \beta + \frac{\lambda_{j}^{i} - r}{r} \right). \tag{7}$$

where r denotes the token consumption rate of the auxiliary bucket in the TBAC mechanism.

To finalize the integration of the maximum delay representation, we define D<sup>s</sup> max as the maximum tolerated latency for each split option s, where s ∈ S. This value is determined by taking the maximum delay among user traffic (d s u ), control traffic (d s c ), and synchronization traffic (d s s ). The formulation ensures that the worst-case latency scenario is considered for each split option, which is critical for meeting the stringent latency requirements of 5G/B5G and 6G networks.

$$D_{max}^s = \max\{d_u^s, d_c^s, d_s^s\}, \ \forall s \in S,$$
 (8)

Specifically, D<sup>s</sup> max = max{d s u , d<sup>s</sup> c , d<sup>s</sup> <sup>s</sup>} captures the impact of variable user traffic modeled as M/M/1 with TBAC, deterministic control traffic modeled as D/D/1, and deterministic

TABLE III SIMULATION PARAMETERS FOR FRONTHAUL MODELING AND FUNCTIONAL SPLITS

| Parameter                          | Value                                                  |  |
|------------------------------------|--------------------------------------------------------|--|
| Topology                           | 1 Cloud, 4 Fog nodes (each with 1/6 of Cloud capacity) |  |
| O-RU Configuration                 | 20 MHz, 2x2 MIMO                                       |  |
| Power Consumption (Cloud, Fog)     | 600 W (Cloud), 300 W (Fog)                             |  |
| OLT, Line Card, ONU Power          | 100 W (OLT), 20 W (Line Card), 3 W (ONU)               |  |
| Optical Propagation Delay          | $\approx$ 5 $\mu$ s per km                             |  |
| Split E Bandwidth Requirement      | 1966 Mb/s                                              |  |
| Split I Bandwidth Requirement      | 674.4 Mb/s                                             |  |
| Split D Bandwidth Requirement      | 119 Mb/s                                               |  |
| Split B Bandwidth Requirement      | 44 Mb/s                                                |  |
| Split E Latency Constraint         | $\leq 100 \ \mu s$                                     |  |
| Split I / D / B Latency Constraint | $\leq 500 \ \mu s$                                     |  |
| TBAC Parameters                    | $r = 0.6, \beta = 10$                                  |  |
| Queue Model Types                  | D/D/1 (Splits E, I); M/M/1-TBAC (Splits D, B)          |  |

synchronization traffic also modeled as D/D/1. This formulation encompasses all functional splits in the system: for splits E and I, which involve centralized processing, the traffic is entirely deterministic and modeled using D/D/1 queues, ensuring predictable delays. In contrast, for splits B and D, the model accounts for both deterministic traffic (control and synchronization) and variable user traffic, with the latter regulated by TBAC to manage burstiness.

# *B. ILP Model Formulation*

We introduce the proposed ILP model to tackle the latency-aware FS-option problem while minimizing power consumption in CF-RAN. The notations used in the problem formulation are presented in Table [II.](#page-5-0)

# *1) Objective Function:*

<span id="page-5-1"></span>
$$Min C_{n} \sum_{n=1}^{N} x_{n} + C_{lc} \sum_{w=1}^{W} \sum_{n=1}^{N} z_{wn} + (C_{onu} + C_{split}) \sum_{i=1}^{I} \sum_{s=1}^{S} \delta_{is}$$
(9)

#### 2) Constraints:

<span id="page-6-0"></span>
$$\sum_{s=1}^{S} \delta_{is} = 1, \ \forall i \in R$$

(10)

(12)

$$\sum_{n=1}^{N} d_{in} = 2, \ \forall i \in R \tag{11}$$

$$\sum_{w=1}^{W} \sum_{n=1}^{N} \sum_{s=1}^{S} y_{wns}^{i} = 2, \ \forall i \in R$$

<span id="page-6-1"></span>
$$\sum_{n=1}^{N} z_{wn} \le 1, \ \forall w \in W \tag{13}$$

$$\sum_{w=1}^{W} \sum_{n=1}^{N} y_{wns}^{i} \le \delta_{is}, \ \forall i, s \in R, S$$
 (14)

$$\sum_{n=1}^{N} t_{isn} \le \delta_{is}, \ \forall i, s \in R, S$$
 (15)

$$\sum_{w=1}^{W} y_{wns}^{i} \le t_{isn}, \ \forall i, s, n \in R, S, N$$
 (16)

$$\sum_{i=1}^{R} \sum_{n=1}^{N} \sum_{s=1}^{S} (y_{wns}^{i} \times B_{i}^{s}) \le B_{w}, \ \forall w \in W$$
 (17)

$$\sum_{i=1}^{R} \sum_{w=1}^{W} \sum_{s=1}^{S} (y_{wns}^{i} \times P_{i}^{s}) \le P_{n}, \ \forall n \in \mathbb{N}$$
 (18)

$$M \times x_n \ge \sum_{i=1}^{R} \sum_{w=1}^{W} \sum_{s=1}^{S} y_{wns}^i, \ \forall n \in N$$
 (19)

$$x_n \le \sum_{i=1}^R \sum_{w=1}^W \sum_{s=1}^S y_{wns}^i, \ \forall n \in N$$
 (20)

$$M \times z_{wn} \ge \sum_{i=1}^{R} \sum_{s=1}^{S} y_{wns}^{i}, \ \forall w, n \in W, N$$
 (21)

$$z_{wn} \le \sum_{i=1}^{R} \sum_{s=1}^{S} y_{wns}^{i}, \ \forall n, w \in N, W$$
 (22)

$$M \times d_{in} \ge \sum_{w=1}^{W} \sum_{s=1}^{S} y_{wns}^{i}, \ \forall n, i \in N, R$$
 (23)

$$d_{in} \le \sum_{w=1}^{W} \sum_{s=1}^{S} y_{wns}^{i}, \ \forall n, i \in N, R$$
 (24)

$$\sum_{i=1}^{R} \sum_{s=1}^{S} t_{isn} \times D_{max}^{s} \ge D_{total_n}, \ \forall n \in \mathbb{N}$$
 (25)

The objective function aims at minimizing power consumption in O-RAN by minimizing the overall processing elements activation, such as processing nodes, O-DUs, O-CUs, Line Cards, and other network elements by placing the maximum O-RUs demands i into a single VPON to be transmitted to the cloud for processing to solve the latency-aware FS-option problem. Our model seeks decreasing values in the costs of the FS-option to promote the choice with maximum centralization in the cloud for cost-efficiency and that can satisfy the tolerated latency threshold. So, with a focus on energy savings, the most centralized option (Option E) is the

initial choice. This formulation uses a component-based static power model, where each network element is assigned a fixed energy cost.

Constraint (10) ensures that each O-RU is associated with one FS-option. Constraints (11, 12) ensure that two VPONs will be initially created to transmit demand i to different processing nodes regarding the FS-option. This means that in the case of Splitting in two processing nodes, one VPON will be allocated to each processing node Constraint (13) ensures that a VPON is allocated to at most one processing node. Constraints (14, 15, 16) ensures that demand i is mapped using constraint (15), and is split accurately between cloud and fog. Constraints (17, 18) ensure that the total capacity of VPONs and processing nodes are respected, which makes it possible to send demands if there is processing capacity.

<span id="page-6-2"></span>Constraints (19, 20, 21, 22) perform the activation of processing nodes and VPONs to correctly react to demands and perform the allocation. Constraints (23, 24) enforce the activation of processing nodes and other network elements for redirection decisions. Lastly, constraint (25) ensures that FS-option is selected based on the overall latency constraint. Constraint (25) incorporates the delay model previously presented to capture the latency. We associate the decision of the splitting option based on the delay identified in the network and on the threshold tolerated by the options and the values present in Tab. III.

While the ILP model can yield optimal solutions for the FFS problem, it becomes computationally impractical for large-scale networks due to the exponential growth in decision variables. This leads to high computational costs and long processing times, making ILP unsuitable for real-time network dimensioning in large, dynamic 5G/B5G and 6G environments. For example, solving ILP for networks with over 100 O-RUs and multiple fog nodes could take hours, which is infeasible for time-sensitive applications.

To overcome these limitations, we propose a heuristic that produces near-optimal solutions much faster than the ILP model. This graph-based heuristic represents O-RAN processing and transport as a flow network, with processing nodes and links modeled as vertices and edges. It enables dynamic task allocation that adapts to current network constraints, reducing computation time while closely approximating the ILP's solution quality.

#### <span id="page-6-3"></span>C. Illustrative Example

To illustrate the model behavior, consider a small topology with two fog nodes  $(n_1, n_2)$ , one cloud node  $(n_3)$ , and three O-RUs  $(i_1, i_2, i_3)$ . Each O-RU supports all four splits. The wavelength set is  $W = \{w_1, w_2\}$ , each with capacity  $B_w = 10$  Gb/s.

Let demand  $i_1$  choose split E, requiring  $B^E_{i_1}=7$  Gb/s and  $P^E_{i_1}=2$  units. The delay  $d^E$  is computed using the D/D/1 model with arrival rate  $\lambda=7$  and service rate  $\mu=10$ , resulting in  $d^E\approx 0.043$  ms. If the TBAC is used (for a split D demand), and parameters are r=5,  $\beta=2$ , the user queuing delay increases due to burst accommodation, especially as  $\lambda\to\mu$ .

The ILP model assigns each demand to a node (fog or cloud) and a wavelength, minimizing delay and power consumption, while ensuring capacity and latency constraints are satisfied.

#### V. On-Line Heuristic Solution

<span id="page-7-0"></span>The ILP model can provide optimal solutions but lacks scalability for large networks. To address this, we propose a graph-based heuristic that minimizes runtime by modeling the O-RAN network dimensioning problem, where processing nodes and fronthaul links are represented as vertices and arcs, respectively. Processing tasks are allocated based on the capacities of the nodes (O-RU, Fog, Cloud) while adhering to latency and bandwidth constraints.

The O-RAN network is modeled as a directed graph G =(V, E), where the vertices (V) represent processing and transmission elements. Specifically, the vertices set includes the source node S, which represents traffic demands originating from the O-RUs, the processing nodes  $P_i^f$ , where i denotes the index of the processing node and  $f \in \{1, 2, 3\}$  indicates the baseband function to be processed, with i = 1 corresponding to O-RU-level processing, i=2 to fog-level processing, and i=3 to cloud-level processing, and the sink node O, which represents the final destination of the allocated traffic. While the heuristic enables dynamic reassignment of functional splits based on real-time load and latency metrics, we acknowledge that frequent reconfigurations may incur orchestration overheads. These include control-plane signaling to reprogram ONUs, adjust vOLT mappings, or reallocate wavelengths in TWDM-PON environments. Although not explicitly modeled in our formulation, such costs are mitigated via threshold mechanisms that implicitly discourage excessive re-splitting when system performance remains within acceptable bounds.

#### A. Graph Construction

The graph G=(V,E) is constructed by instantiating a layered topology, where each layer corresponds to a possible functional processing location (O-RU, Fog, or Cloud) and baseband function. For each O-RU, a vertex  $P_1^f$  is created to represent local processing of function  $f\in 1,2,3$ . Similarly, for each Fog node and Cloud node capable of processing a given function, corresponding vertices  $P_2^f$  and  $P_3^f$  are instantiated. The complete set of processing vertices is thus indexed by the tuple (i,f), where  $i\in 1,2,3$  denotes the location and f the baseband function.

Edges E are defined in three categories: (i) from the source S to all O-RU vertices  $P_1^f$ , modeling the injection of traffic demands; (ii) from  $P_i^f$  to  $P_j^g$ , with  $j \geq i$  and g > f, modeling valid transitions along the functional processing chain, respecting the no-backtracking constraint; and (iii) from each final processing vertex  $P_j^3$  to the sink O, capturing the delivery of fully processed traffic. Each edge  $(u,v) \in E$  is annotated with a cost w(u,v) representing transmission and processing latency, and a capacity c(u,v) corresponding to the available fronthaul bandwidth. The flow variable x(u,v) tracks the amount of traffic routed through each edge and satisfies the constraint  $0 \leq x(u,v) \leq c(u,v)$ .

![](_page_7_Figure_9.jpeg)

<span id="page-7-1"></span>Fig. 3. Network flow graph and options for the placement and processing of the requests. Ellipse represents the edges associated with a particular processing node.

### B. Key Constraint on Function Indexing

If function f is processed at node i, all subsequent functions g > f must be processed at the same node or at a higher-indexed node. For example, if f is processed in the Fog (i=2), then g > f can only be processed in the Fog (i=2) or Cloud (i=3), ensuring that the processing flow does not backtrack to lower-indexed nodes (e.g., from Fog to O-RU).

**Edges** (E) represent fronthaul connections between vertices: (1)  $(S, P_1^f)$ , links connecting the source S to O-RU processing nodes; (2)  $(P_i^f, P_j^g)$ , functional allocation paths among O-RU, Fog, and Cloud nodes, subject to capacity and latency constraints, where these edges are directional and respect the indexing constraint (i.e.,  $j \geq i$ ); and (3)  $(P_i^f, O)$ , links ensuring processed traffic is correctly forwarded to the sink O. Each edge  $e \in E$  is associated with: (1) **Capacity** c(e), the available bandwidth on the link; (2) **Cost** w(e), the latency incurred by transmitting traffic along the edge; and (3) **Flow** x(e), the traffic assigned to the edge, satisfying  $0 \leq x(e) \leq c(e)$ .

The graph representation is depicted in Fig. 3. The graph is constructed algorithmically as follows. Initially, a source node S is introduced to represent all traffic demands originating from O-RUs. Subsequently, for each processing node i, where  $i \in \{1,2,3\}$  denotes the processing level (i = 1 for O-RU-level, i = 2 for Fog-level, and i = 3 for Cloud-level), processing nodes  $P_i^f$  are instantiated to correspond to distinct baseband function allocations, with f representing the index of the baseband function being processed. Edges are then established to model the flow of traffic. Specifically, edges  $(S, P_1^f)$  represent the initiation of traffic demands at the O-RU level, edges  $(P_i^f, P_i^g)$  model functional allocation paths among O-RU, Fog, and Cloud nodes while adhering to capacity, latency, and indexing constraints (i.e.,  $j \geq i$ ), and edges  $(P_i^f, O)$  ensure the proper termination of processed traffic at the sink node O.

The baseband function allocation problem is formulated as a minimum-cost maximum-flow problem. The objective function maximizes the total flow from the source S to the sink O, ensuring efficient utilization of resources:

$$\max \sum_{i \in R} f(S, P_i^j), \tag{26}$$

where  $f(S, P_i^j)$  represents the flow initiated from the source S to the j-th processing node. Flow conservation constraints

![](_page_8_Figure_2.jpeg)

<span id="page-8-1"></span>Fig. 4. Illustrative example of a solution where node function 1 is placed in node 2 and functions 2 and 3 are placed in node 3.

ensure that flow is conserved at each vertex  $v_i \in V$ :

$$\sum_{j \in V} f(v_i, v_j) - \sum_{j \in V} f(v_j, v_i) = \begin{cases} d_i & \text{if } v_i = S, \\ -d_i & \text{if } v_i = O, \ \forall v_i \in V, \\ 0 & \text{otherwise,} \end{cases}$$

where  $d_i$  is the demand originating from O-RU i. Capacity constraints enforce limits on all edges:

$$0 \le f(v_i, v_j) \le c(v_i, v_j), \ \forall (v_i, v_j) \in E.$$
 (28)

Latency constraints incorporate latency thresholds into the flow model:

$$\sum_{e \in E} w(e)f(e) \le D_{\max}^s, \ \forall s \in S, \tag{29}$$

where w(e) is the latency cost of edge e, and  $D_{\max}^s$  is the maximum tolerated latency for split option s. Indexing constraints ensure that processing flows respect the indexing constraint:

$$f(P_i^f, P_j^g) = 0, \ \forall f > g,$$
 (30)

where f and g are the indices of the baseband functions being processed. This ensures that no "backtracking" occurs (e.g., traffic cannot move from Cloud to Fog).

The heuristic operates as follows. First, during initialization, all traffic demands originating from O-RUs are directed to the Cloud  $(P_3^f)$  if the total delay remains below  $d_E$  (latency threshold for Option E) and the CloudLink capacity can accommodate the demand. Next, during redistribution, if CloudLink bandwidth or latency constraints are violated, the flow is partially redistributed to Fog nodes  $(P_2^f)$  to prevent congestion and blocking, ensuring that any redistribution respects the indexing constraint (e.g., traffic cannot move back to O-RU-level processing). Then, during the allocation, the most centralized functional split k that satisfies both delay and capacity constraints is selected:

$$k = \arg\min_{s \in S} \left( C_{\text{split}} + \sum_{e \in E} w(e) f(e) \right), \tag{31}$$

where  $C_{\rm split}$  is the cost associated with functional split s. Finally, during final routing, traffic is forwarded to the sink O, ensuring that all processed demands are correctly allocated and meet network constraints.

Fig. 4 shows the network flow representation, with a possible solution path that ensures minimal cost while adhering to latency, capacity, and indexing constraints. In this example, traffic initially flows from the source node S to the fog node  $P_2^1$ , where the first stage of processing occurs. Subsequently,

partial processing is offloaded to the cloud via the edge  $P_2^1 \to P_3^2$ , representing the transition of computational tasks to a higher-indexed node. The remaining processing is then completed within the cloud at node  $P_3^3$ , as indicated by the edge  $P_3^2 \to P_3^3$ . Finally, fully processed traffic is forwarded to the sink node O through the edge  $P_3^3 \to O$ , ensuring that all demands are allocated correctly and meet the constraints of the network.

<span id="page-8-2"></span>The computational complexity of the proposed heuristic is based on modeling the problem as a minimum-cost maximumflow problem on a directed graph G = (V, E), where nodes represent processing and transmission elements, and edges model fronthaul connections. Constructing this graph takes linear time, O(|V| + |E|), with |E| growing faster. The dominant complexity arises from solving the minimum-cost maximumflow problem. Classical algorithms like Ford-Fulkerson or Edmonds-Karp incur  $O(|V| \cdot |E|^2)$ , while more efficient methods such as Orlin's or successive shortest path reduce it to  $O(|V|^2 \cdot |E|)$ , making them more practical for large networks [38], [39]. The heuristic consists of initialization, redistribution, split selection, and final routing, requiring at most  $O(m + |S| \cdot m)$ , where m is the number of traffic demands and |S| is the number of functional split options. Since demands are evaluated independently against available splits, this step scales linearly with m and |S|. Thus, the total complexity is  $O(|V| \cdot |E|^2 + |S| \cdot m)$ . Given  $|E| = O(|V|^2)$ , the worst-case complexity reaches  $O(|V|^5)$ , though practical optimizations significantly reduce execution time. Empirical results confirm this scalability, with execution times under seconds for large networks, compared to up to 30,000 seconds for the ILP, as shown in Fig. 8.

### <span id="page-8-4"></span><span id="page-8-3"></span>VI. NUMERICAL RESULTS

<span id="page-8-0"></span>To assess the performance of the proposed approach, we conducted a series of experiments using simulation. To this end, we used the 5GPy simulator [40]. In our setup, each RU is initially deactivated, and RU activations follow a Poisson process with rate  $\lambda = \frac{e}{60}$ , where e is the maximum Erlang value for a given hour of the day. This simulates the progressive growth of network load in accordance with user activity over 24 hours. Generated demands also follow a Poisson arrival process, and the service times are modeled with a negative exponential distribution, reflecting the traffic behavior described in Chunyi et al. [41].

<span id="page-8-5"></span>We evaluated the performance of the ILP and the heuristic algorithm under static and dynamic network traffic scenarios considering the same O-RAN architecture. In the static scenario, the total demand request is known in advance, which allows us to measure the time required for both solutions to reach convergence. In the dynamic scenario, we assessed the benefits of the proposed FS CF-RAN approach by comparing it against two baseline operation modes: C-RAN (fully centralized mode) and CF-RAN without flexible functional splitting. This comparison quantifies the impact of FFS on O-RAN networks, particularly regarding energy consumption reduction and system availability improvement.

The system parameters used in our simulation are grounded in realistic models and standard specifications. The bandwidth

![](_page_9_Figure_2.jpeg)

![](_page_9_Figure_3.jpeg)

![](_page_9_Figure_4.jpeg)

Fig. 5. ILP Illustrative results.

<span id="page-9-1"></span>![](_page_9_Figure_7.jpeg)

<span id="page-9-0"></span>Fig. 6. Simulated daily traffic behavior over a 24-hour period.

demands for each functional split were derived following the methodology in [\[35\],](#page-13-18) which considers sampling rate, MIMO configuration, and functional decomposition. Latency constraints follow 3GPP TS 23.501 and O-RAN WG6, especially for time-sensitive services such as URLLC.

#### *A. Simulation Traffic Profile*

The 24-hour traffic profile adopted in our simulations reflects typical mobile usage in commercial and business areas (Fig. [6\)](#page-9-0), where network load gradually increases in the morning, peaks around 2 PM, and declines during the evening. To ensure generalization across different network scales, traffic demand was normalized in the range [0, 1], with 1.0 representing the peak intensity.

In the simulation scenario, the peak corresponds to approximately 120 Gb/s. The normalized average traffic load over the 24-hour period was calculated as:

Average Load = 
$$\frac{1}{24} \sum_{h=1}^{24} \lambda_h \approx 0.318$$
 (32)

This results in an average daily traffic of approximately 38.2 Gb/s. The peak-to-average ratio (PAR) is then:

$$PAR = \frac{120}{38.2} \approx 3.14 \tag{33}$$

This moderately intermittent profile is representative of urban deployments cited in the literature and its relationship tends to directly impact queue delays and fronthaul congestion.

# *B. Scenario I: Static Traffic*

In the first scenario, we evaluated the proposed ILP model using as metrics the power consumption, the service availability, and the ratio of the delay and the system availability. For these simulations, we considered a scenario with one cloud and four fog nodes for demands processing operating under a 24-hour daily traffic pattern as in [\[40\]](#page-13-23) and [\[41\].](#page-13-24) The results for the static traffic scenario are presented in Fig. [5](#page-9-1) [\(a\)\(b\)\(c\),](#page-9-1) where we show the system availability, power consumption, and the ratio of experienced latency and service availability for our proposed FS CF-RAN, compared to centralized scenario (C-RAN) [\[14\]](#page-12-13) and a distributed scenario without our proposed approach (CF-RAN) [\[40\].](#page-13-23)

Fig [5](#page-9-1) [\(a\)](#page-9-1) shows the average energy consumption of the three approaches. C-RAN has the lowest energy consumption but suffers from a high request blocking rate, reducing system availability. CF-RAN consumes more energy due to additional fog node activation. The proposed FS CF-RAN balances energy efficiency and availability. Fig [5](#page-9-1) [\(b\)](#page-9-1) presents system availability, reflecting the network's ability to meet traffic demands within latency and capacity constraints. C-RAN struggles due to frequent request blocking, while CF-RAN maintains over 98% availability. FS CF-RAN ensures 100% availability throughout, demonstrating superior adaptability. Fig [5](#page-9-1) [\(c\)](#page-9-1) examines service availability versus fronthaul latency. When latency exceeds 100 µs (Split E), C-RAN's availability drops sharply due to queue delays and fronthaul limitations. FS CF-RAN, however, maintains availability even under high latency, proving its robustness in static scenarios. Overall, FS CF-RAN outperforms the other architectures under variable traffic, making it a strong candidate for next-generation radio access networks.

The sharp availability degradation observed for the centralized C-RAN architecture in Fig. [5](#page-9-1) is primarily attributed to queuing congestion and latency violations at the optical fronthaul interface under high traffic conditions. Specifically, under functional split E, which requires the transport of raw I/Q samples with a strict delay bound of 100 µs, any accumulation of queuing delay at the ONUs or contention in VPON channels leads to service blocking.

In this context, synchronized synchronization and control traffic—modeled as deterministic arrivals—compete with bursty user traffic (subject to token bucket regulation), increasing the chance of buffer saturation. As traffic load increases, queuing delays rise non-linearly, violating latency thresholds and resulting in dropped requests. Since C-RAN lacks adaptive mechanisms for shifting processing functions, it cannot offload to edge nodes or adjust to more relaxed splits. Consequently, the system experiences abrupt declines

![](_page_10_Figure_2.jpeg)

![](_page_10_Figure_3.jpeg)

![](_page_10_Figure_4.jpeg)

- <span id="page-10-1"></span>

Fig. 7. Graph-based model illustrative results.

![](_page_10_Figure_9.jpeg)

<span id="page-10-0"></span>Fig. 8. Heuristic vs. ILP execution time.

in availability once latency or bandwidth constraints are exceeded.

In contrast, the proposed architecture dynamically reconfigures split types in response to real-time network state. When split E becomes unfeasible, the system transitions to less demanding splits (e.g., I or D), mitigating queuing stress and preserving availability. This adaptive behavior—coupled with TBAC-based admission control—ensures latency compliance and high service continuity. The observed trends align with prior models such as those in [\[2\],](#page-12-1) [\[6\],](#page-12-5) and [\[15\],](#page-12-14) which highlight the limitations of centralized, non-adaptive designs in latencysensitive environments."

In Fig. [7](#page-10-1) [\(a\),](#page-10-1) [\(b\),](#page-10-1) and [\(c\),](#page-10-1) we present the performance of the graph-based model under static traffic using the same metrics shown in Fig. [5,](#page-9-1) ensuring a fair comparison between the optimal solutions provided by the ILP and the near-optimal solutions generated by the heuristic. The results reinforce the findings obtained with the ILP approach, demonstrating that the heuristic achieves proximal comparable performance while significantly reducing execution time. The importance of latency thresholds, such as the 100 µs limit for the BBU Pool, lies in their alignment with QoS requirements for 5G/B5G applications. Exceeding these thresholds leads to request redirection to fog nodes, which have limited processing capacity, resulting in higher blocking rates. These thresholds also influence the choice of functional splits, balancing centralization benefits with latency constraints. By incorporating these thresholds into the evaluation, our analysis ensures practical and realistic insights into the trade-offs involved in O-RAN dimensioning.

It is important to note that the CF-RAN approach without functional splitting was unable to allocate all demands, leading to unallocated requests and increased blocking. The inability to receive new demands under saturation in its link capacity contributes to this behavior. When the BBU Pool's 100 µs limit is exceeded, direct allocation occurs to fog nodes, which have limited capacity to process the demands.

The results obtained with the FS CF-RAN approach demonstrate a consistent operation near to 100% up time while reducing energy consumption compared to the CF-RAN approach. Additionally, the FS CF-RAN approach correctly allocated the demands based on the latency in the fronthaul, avoiding the saturation of fog nodes. Similar to the ILP approach, the proposed heuristic approach successfully allocated all demands while maintaining 100% network coverage.

In Fig. [8,](#page-10-0) we show the execution times of the ILP solver and the graph-based heuristic for networks with varying demands. As shown, the ILP solver required up to 30,000 seconds at peak demand, while the heuristic consistently took under 1 second per run. The ILP's prolonged execution time limits its practicality for real-time network dimensioning and split option selection, thereby compromising scalability.

Although the ILP model does not explicitly minimize energy consumption, the number of active processing nodes—represented by the binary variable —can be interpreted as a proxy for energy usage. A reduced number of active nodes, particularly during low-demand periods, implies lower static energy expenditure. Furthermore, the model tends to assign functional splits to processing nodes that require fewer computational resources (e.g., Fog instead of Cloud), which also contributes to energy efficiency. These behaviors reflect the architecture's capacity to balance performance and resource consumption in a dynamic manner.

# *C. Scenario Ii: Dynamic Traffic*

In this section, we assess our proposed approach in a dynamic traffic scenario. Fig [9](#page-11-1) [\(a\)](#page-11-1) and [\(b\)](#page-11-1) show the relationship between the maximum delay of processed demands under a given network load in the dynamic simulation and the blocking of demands observed in the CRAN and FS CF-RAN approaches. These two approaches were selected due to their contrasting characteristics, which highlight the trade-offs between centralization and flexibility in O-RAN architectures. CRAN, a fully centralized solution, achieves low energy consumption but suffers from high blocking rates due to strict latency constraints. In contrast, FS CF-RAN employs a flexible functional splitting strategy, dynamically adapting to

![](_page_11_Figure_2.jpeg)

![](_page_11_Figure_4.jpeg)

Fig. 9. Relationship between latency of processed demands and unallocated demands.

<span id="page-11-1"></span>![](_page_11_Figure_7.jpeg)

<span id="page-11-2"></span>Fig. 10. Average of unallocated demands.

traffic demands to ensure high system availability even under increased latency and computational load.

The results in Fig. [10](#page-11-2) illustrate the relationship between demand non-allocation and the need for processing in fog nodes. This non-allocation occurs due to latency violations in the fully centralized approach or limitations in the fronthaul link. The results show that even CF-RAN blocks demands when fog nodes reach saturation or when latency exceeds the 100µs threshold. In contrast, FS CF-RAN effectively avoids unallocated demands through better resource dimensioning, whereas CRAN suffers from a high blocking rate due to latency violations and the lack of intermediary processing nodes.

We now present the results of demand allocation and show the chosen functional splitting option under network variations. Fig. [11](#page-11-3) shows the aggregated average results over a full day (24-hour simulation), comparing the ILP and heuristic approaches in the same scenario. The ILP achieved better compliance with the maximum allowed function centralization

![](_page_11_Figure_12.jpeg)

<span id="page-11-3"></span>Fig. 11. Average split option used in simulation.

in the cloud (see the objective function in [\(9\)\)](#page-5-1), resulting in the lowest energy consumption among FS CF-RAN solutions. However, its runtime is impractical (see Fig. [8\)](#page-10-0). In contrast, the heuristic exhibited only a marginal loss in centralization while significantly reducing execution time. Although this slightly increased energy consumption, the drastic improvement in computational efficiency makes the heuristic a more practical solution.

#### VII. CONCLUDING REMARKS

<span id="page-11-0"></span>In this work, we addressed the problem of FS allocation in the presented architectures with packetized fronthaul, proposing two complementary approaches: an ILP formulation and a proposition of a scalable heuristic based on graph theory. These methods aim to dynamically reallocate functional splits and processing nodes in response to fluctuating traffic conditions, mitigating latency bottlenecks introduced by packetized fronthaul links.

Comparative evaluations against traditional C-RAN and hybrid solutions from the literature demonstrated that FS CF-RAN offers improved network flexibility, dynamic resizing capabilities, and energy efficiency. However, we also observed that improper split allocation or fronthaul overuse can introduce new challenges — especially under constrained or bursty conditions.

The ILP approach achieved optimal solutions but was limited by high computational complexity, becoming impractical in large-scale scenarios. On the other hand, our proposed heuristic maintained performance comparable to the ILP while significantly reducing computation time, making it suitable for real-time or large-scale deployments.

Furthermore, we incorporated queuing models (D/D/1 and M/M/1) to analyze delay behavior across different FS types and applied token bucket admission control (TBAC) to regulate bursty traffic. Sensitivity analysis revealed that parameters such as token rate and bucket size critically impact the stability and delay performance of the system.

These findings support the feasibility of FS CF-RAN as a dynamic, low-latency, and energy-efficient solution for future O-RAN deployments. Future work will explore its integration with standardized O-RAN interfaces and testbed validation.

# *A. Orchestration Overhead and FS Reconfiguration Costs*

While our model focuses on optimizing FS selection to minimize delay and resource usage, frequent FS reconfiguration may lead to additional signaling and orchestration overhead. These costs include control plane signaling exchanges between O-RUs, O-DUs, and O-CUs, buffer synchronization, state transitions, and temporary performance fluctuations during switching. Although our ILP and heuristic algorithms do not explicitly model these costs, they are mitigated by the fact that FS changes are driven by significant load or latency variations and not executed continuously. Moreover, in future extensions, we plan to introduce soft reconfiguration penalties or delay-aware hysteresis functions to prevent unnecessary FS oscillations. Such additions would preserve system responsiveness while limiting the orchestration burden on the RIC and control entities.

The proposed architecture also supports energy-aware behavior by implicitly minimizing node activations and promoting traffic consolidation. Although energy was not modeled explicitly, the reduction in the number of active processing units and the preference for less energy-intensive nodes suggest inherent energy efficiency. Future extensions of this work will incorporate detailed energy consumption models to make this relationship explicit and enable trade-offs between latency and energy use.

#### *B. Scalability Analysis and Runtime Environment*

To assess the practical feasibility of our proposed models in large-scale O-RAN scenarios, we evaluated the scalability of both the ILP formulation and the graph-based heuristic. Although the ILP provides an optimal solution baseline, it becomes computationally intractable as the number of O-RUs increases. In our experiments, the CPLEX solver was unable to return valid solutions within a reasonable time frame when the network exceeded approximately 60 O-RUs. Execution times surpassed 30,000 seconds (≈ 8.3 hours) and, in many instances, the process was terminated due to memory exhaustion or wall-time limits. These results were obtained using a dedicated Linux environment without background interference, following practices in the optimization literature [\[42\],](#page-13-25) [\[43\].](#page-13-26)

<span id="page-12-17"></span><span id="page-12-16"></span>To address this limitation, we proposed a graph-based heuristic capable of near-real-time execution. This heuristic consistently generated feasible solutions within milliseconds, even in high-load conditions, and achieved cost values close to the best ILP solutions within the solver's tractable range. However, we observed that solution quality degrades slightly under severe latency constraints or extremely high traffic loads. Despite the absence of formal sub-optimality bounds, the heuristic provides a scalable and latency-aware alternative that enables dynamic orchestration in dense deployments.

# *C. Toward Real-World FS CF-RAN Deployment*

Bringing the proposed FS CF-RAN architecture into real-world O-RAN deployments requires integration with standardized open interfaces (O1, A1, E2) and the O-RAN Software Community (O-RAN SC) framework. FS selection and queuing-aware placement strategies can be implemented as xAPPs in the near-real-time RIC or as SMO services, enabling policy-based control over virtualized RAN components.

The offline ILP must be complemented by a lightweight, real-time mechanism—such as the proposed graph-based heuristic—capable of reacting to traffic and topology variations in cloud-native environments. Experimental validation on O-RAN–compliant testbeds (e.g., OpenAirInterface, srsRAN) with hardware supporting flexible fronthaul protocols (e.g., eCPRI, F1/E1) is essential to assess orchestration latency, signaling overhead, and reconfiguration smoothness.

Future enhancements include extending the queuing model to handle asynchronous traffic and synchronization impairments, and adopting ML-driven orchestration to predict optimal FS configurations, reduce oscillations, and maintain latency guarantees. These steps close the gap between theoretical modeling and operational deployment, reinforcing the viability of FS CF-RAN in next-generation O-RAN networks.

#### REFERENCES

- <span id="page-12-0"></span>[\[1\]](#page-0-0) *ETSI, 5G: Study on New Radio Access Technology*, ETSI TR 138 912 V14.1.0, European Telecommunications Standards Institute, 2017. [Online]. Available: https://www.etsi.org/deliver/ etsi tr/138900 138999/138912/14.01.00 60/tr 138912v140100p.pdf
- <span id="page-12-1"></span>[\[2\]](#page-0-1) R. I. Tinini, D. M. Batista, G. B. Figueiredo, M. Tornatore, and B. Mukherjee, "Low-latency and energy-efficient BBU placement and VPON formation in virtualized cloud-fog RAN," *J. Opt. Commun. Netw.*, vol. 11, no. 4, pp. B37–B48, Apr. 2019.
- <span id="page-12-2"></span>[\[3\]](#page-0-2) L. Chen, Z. Jiang, D. Yang, C. Wang, and T.-M.-T. Nguyen, "Fog radio access network optimization for 5G leveraging user mobility and traffic data," *J. Netw. Comput. Appl.*, vol. 191, Oct. 2021, Art. no. 103083.
- <span id="page-12-3"></span>[\[4\]](#page-0-3) D. Harutyunyan and R. Riggio, "Flex5G: Flexible functional split in 5G networks," *IEEE Trans. Netw. Service Manage.*, vol. 15, no. 3, pp. 961–975, Sep. 2018.
- <span id="page-12-4"></span>[\[5\]](#page-0-4) L. M. P. Larsen, A. Checko, and H. L. Christiansen, "A survey of the functional splits proposed for 5G mobile crosshaul networks," *IEEE Commun. Surveys Tuts.*, vol. 21, no. 1, pp. 146–172, 1st Quart., 2019.
- <span id="page-12-5"></span>[\[6\]](#page-0-5) L. Diez, A. M. Alba, W. Kellerer, and R. Aguero, "Flexible functional ¨ split and fronthaul delay: A queuing-based model," *IEEE Access*, vol. 9, pp. 151049–151066, 2021.
- <span id="page-12-6"></span>[\[7\]](#page-0-6) M. Ahsan, A. Ahmed, A. Al-Dweik, and A. Ahmad, "Functional split-aware optimal BBU placement for 5G cloud-RAN over WDM access/aggregation network," *IEEE Syst. J.*, vol. 17, no. 1, pp. 122–133, Mar. 2023.
- <span id="page-12-7"></span>[\[8\]](#page-0-7) eCPRI Specification (eCPRI Forum), "Common Public Radio Interface (eCPRI): eCPRI Interface Specification," eCPRI Specification V2.0, Tech. Rep., May 2019. [Online]. Available: http://www.cpri.info/ downloads/eCPRI-v-2.0-2019-05-10c.pdf
- <span id="page-12-8"></span>[\[9\]](#page-0-8) A. Fayad, T. Cinkler, and J. Rak, "5G/6G optical fronthaul modeling: Cost and energy consumption assessment," *J. Opt. Commun. Netw.*, vol. 15, no. 9, pp. D33–D46, 2023.
- <span id="page-12-9"></span>[\[10\]](#page-0-9) Q. Wang et al., "Resource allocation based on radio intelligence controller for open RAN toward 6G," *IEEE Access*, vol. 11, pp. 97909–97919, 2023.
- <span id="page-12-10"></span>[\[11\]](#page-0-10) C.-C. Chen, M. Irazabal, C.-Y. Chang, A. Mohammadi, and N. Nikaein, "FlexApp: Flexible and low-latency xApp framework for RAN intelligent controller," in *Proc. IEEE Int. Conf. Commun. (ICC)*, May 2023, pp. 5450–5456.
- <span id="page-12-11"></span>[\[12\]](#page-0-11) J. Wu, Z. Zhang, Y. Hong, and Y. Wen, "Cloud radio access network (C-RAN): A primer," *IEEE Netw.*, vol. 29, no. 1, pp. 35–41, Jan. 2015.
- <span id="page-12-12"></span>[\[13\]](#page-0-12) J. Chen, "5G transport networks: Capacity, latency and cost," in *Proc. OSA Adv. Photon. Congr. (AP) (IPR, Netw., NOMA, SPPCom, PVLED)*, 2019, p. NeTh2D.3.
- <span id="page-12-13"></span>[\[14\]](#page-0-13) X. Wang, A. Alabbasi, and C. Cavdar, "Interplay of energy and bandwidth consumption in CRAN with optimal function split," in *Proc. IEEE Int. Conf. Commun. (ICC)*, May 2017, pp. 1–6.
- <span id="page-12-15"></span><span id="page-12-14"></span>[\[15\]](#page-0-14) M. S. Akhtar, J. Gupta, M. I. Alam, S. Majhi, and A. Adhya, "Fronthaul latency and capacity constrained cost-effective and energy-efficient 5G C-RAN deployment," *Opt. Fiber Technol.*, vol. 80, Oct. 2023, Art. no. 103392.

- [\[16\]](#page-0-15) M. Sharara, F. Fossati, S. Hoteit, V. Veque, and F. Bassi, "Minimizing ` energy consumption by joint radio and computing resource allocation in cloud-RAN," *Comput. Netw.*, vol. 234, Oct. 2023, Art. no. 109870.
- <span id="page-13-0"></span>[\[17\]](#page-0-16) L. Valcarenghi, A. Marotta, C. Centofanti, F. Graziosi, and K. Kondepu, "Energy-efficient integrated O-RAN/PON access network," in *Proc. IEEE Int. Conf. Commun.*, Jun. 2024, pp. 4967–4972.
- <span id="page-13-1"></span>[\[18\]](#page-0-17) K. Ali and M. Jammal, "Proactive VNF scaling and placement in 5G O-RAN using ML," *IEEE Trans. Netw. Service Manage.*, vol. 21, no. 1, pp. 174–186, Feb. 2024.
- <span id="page-13-2"></span>[\[19\]](#page-0-18) G. Baldini et al., "Toward sustainable O-RAN deployment: An in-depth analysis of power consumption," *IEEE Trans. Green Commun. Netw.*, vol. 9, no. 2, pp. 429–444, Jun. 2025.
- <span id="page-13-3"></span>[\[20\]](#page-1-1) H. Biallach, M. Bouhtou, K. Kumbria, D. Nace, and A. Tomaszewski, "Virtual network function reconfiguration in 5G networks: An optimization perspective," *Networks*, vol. 83, no. 4, pp. 673–691, Jun. 2024.
- <span id="page-13-4"></span>[\[21\]](#page-1-2) M. Masoumi et al., "Efficient protected vnf placement and mec location selection for dynamic service provisioning in 5G networks," in *Proc. 20th Int. Conf. Distrib. Comput. Artif. Intell., Special Sessions I (DCAI)* (Lecture Notes in Networks and Systems), vol. 741, Guimaraes, Portugal. Cham, Switzerland: Springer, 2023, pp. 448–456, doi: [10.1007/978-3-031-38318-2](http://dx.doi.org/10.1007/978-3-031-38318-2%5F44) 44.
- <span id="page-13-5"></span>[\[22\]](#page-1-3) M. Taghavian, Y. Hadjadj-Aoul, G. Texier, N. Huin, and P. Bertin, "An approach to network service placement reconciling optimality and scalability," *IEEE Trans. Netw. Service Manage.*, vol. 20, no. 3, pp. 2218–2229, Sep. 2023.
- <span id="page-13-6"></span>[\[23\]](#page-1-4) M. Tohidi, H. Bakhshi, and S. Parsaeefard, "Flexible function splitting and resource allocation in C-RAN for delay critical applications," *IEEE Access*, vol. 8, pp. 26150–26161, 2020.
- <span id="page-13-7"></span>[\[24\]](#page-1-5) N. Kazemifard and V. Shah-Mansouri, "Minimum delay function placement and resource allocation for open RAN (O-RAN) 5G networks," *Comput. Netw.*, vol. 188, Apr. 2021, Art. no. 107809.
- <span id="page-13-8"></span>[\[25\]](#page-1-6) T. Tsourdinis, I. Chatzistefanidis, N. Makris, T. Korakis, N. Nikaein, and S. Fdida, "Service-aware real-time slicing for virtualized beyond 5G networks," *Comput. Netw.*, vol. 247, Jun. 2024, Art. no. 110445.
- <span id="page-13-9"></span>[\[26\]](#page-1-7) L. M. Moreira Zorello, M. Sodano, S. Troia, and G. Maier, "Power-efficient baseband-function placement in latency-constrained 5G metro access," *IEEE Trans. Green Commun. Netw.*, vol. 6, no. 3, pp. 1683–1696, Sep. 2022.
- <span id="page-13-10"></span>[\[27\]](#page-1-8) F. W. Murti, S. Ali, and M. Latva-Aho, "Constrained deep reinforcement based functional split optimization in virtualized RANs," *IEEE Trans. Wireless Commun.*, vol. 21, no. 11, pp. 9850–9864, Nov. 2022.
- <span id="page-13-11"></span>[\[28\]](#page-1-9) T. Pamuklu, M. Erol-Kantarci, and C. Ersoy, "Reinforcement learning based dynamic function splitting in disaggregated green open RANs," in *Proc. IEEE Int. Conf. Commun.*, Jun. 2021, pp. 1–6.
- <span id="page-13-12"></span>[\[29\]](#page-1-10) D. Careglio et al., "Results and achievements of the ALLIANCE project: New network solutions for 5G and beyond," *Appl. Sci.*, vol. 11, no. 19, p. 9130, Sep. 2021.
- <span id="page-13-13"></span>[\[30\]](#page-1-11) D. Wypior, M. Klinkowski, and I. Michalski, "Open RAN—Radio access ´ network evolution, benefits and market trends," *Appl. Sci.*, vol. 12, no. 1, p. 408, Jan. 2022. [Online]. Available: https://www.mdpi.com/ 2076-3417/12/1/408
- <span id="page-13-14"></span>[\[31\]](#page-1-12) S. O. Edeagu, R. A. Butt, S. M. Idrus, and N. J. Gomes, "A hybrid dynamic bandwidth allocation scheme operating with IACG and cooperative DBA for converged fronthaul networks," *Opt. Fiber Technol.*, vol. 75, Jan. 2023, Art. no. 103199.
- <span id="page-13-15"></span>[\[32\]](#page-1-13) B. Shariati et al., "Demonstration of latency-aware 5G network slicing on optical metro networks," *J. Opt. Commun. Netw.*, vol. 14, no. 1, pp. A81–A90, Jan. 2022.
- <span id="page-13-16"></span>[\[33\]](#page-1-14) D. Larrabeiti, L. M. Contreras, G. Otero, J. A. Hernandez, and ´ J. P. Fernandez-Palacios, "Toward end-to-end latency management of 5G network slicing and fronthaul traffic (invited paper)," *Opt. Fiber Technol.*, vol. 76, Mar. 2023, Art. no. 103220.
- <span id="page-13-17"></span>[\[34\]](#page-2-2) M. R. P. dos Santos, R. I. Tinini, T. O. Januario, and G. B. Figueiredo, "Deep recurrent neural network for optical fronthaul dimensioning and proactive vBBU placement in CF-RAN," *Photonic Netw. Commun.*, vol. 43, no. 1, pp. 59–73, Feb. 2022, doi: [10.1007/s11107-022-00964-0.](http://dx.doi.org/10.1007/s11107-022-00964-0)
- <span id="page-13-18"></span>[\[35\]](#page-3-2) A. Marotta, D. Cassioli, K. Kondepu, C. Antonelli, and L. Valcarenghi, "Exploiting flexible functional split in converged software defined access networks," *J. Opt. Commun. Netw.*, vol. 11, no. 11, pp. 536–546, Nov. 2019.
- <span id="page-13-19"></span>[\[36\]](#page-4-5) L. Li et al., "Enabling flexible link capacity for eCPRI-based fronthaul with load-adaptive quantization resolution," *IEEE Access*, vol. 7, pp. 102174–102185, 2019.
- <span id="page-13-21"></span><span id="page-13-20"></span>[\[37\]](#page-4-6) D. Koulougli, K. K. Nguyen, and M. Cheriet, "ECPRI supports in 5G O-RAN fronthaul with FlexEthernet," in *Proc. IEEE Global Commun. Conf.*, Dec. 2023, pp. 1968–1973.

- [\[38\]](#page-8-2) K. Hoppmann-Baum, "On the complexity of computing maximum and minimum min-cost-flows," *Networks*, vol. 79, no. 2, pp. 236–248, Mar. 2022.
- <span id="page-13-22"></span>[\[39\]](#page-8-3) L. Chen, R. Kyng, Y. P. Liu, R. Peng, M. P. Gutenberg, and S. Sachdeva, "Almost-linear-time algorithms for maximum flow and minimum-cost flow," *Commun. ACM*, vol. 66, no. 12, pp. 85–92, Dec. 2023.
- <span id="page-13-23"></span>[\[40\]](#page-8-4) R. I. Tinini, M. R. P. D. Santos, G. B. Figueiredo, and D. M. Batista, "5GPy: A SimPy-based simulator for performance evaluations in 5G hybrid cloud-fog RAN architectures," *Simul. Model. Pract. Theory*, vol. 101, May 2020, Art. no. 102030.
- <span id="page-13-24"></span>[\[41\]](#page-8-5) C. Peng, S.-B. Lee, S. Lu, H. Luo, and H. Li, "Traffic-driven power saving in operational 3G cellular networks," in *Proc. 17th Annu. Int. Conf. Mobile Comput. Netw.* New York, NY, USA: Association for Computing Machinery, Sep. 2011, pp. 121–132, doi: [10.1145/2030613.2030628.](http://dx.doi.org/10.1145/2030613.2030628)
- <span id="page-13-25"></span>[\[42\]](#page-12-16) S. Z. H. Zahidi, F. Aloul, A. Sagahyroon, and W. El-Hajj, "Optimizing complex cluster formation in MANETs using SAT/ILP techniques," *IEEE Sensors J.*, vol. 13, no. 6, pp. 2400–2412, Jun. 2013.
- <span id="page-13-26"></span>[\[43\]](#page-12-17) Z. Cao et al., "An accurate solution to the cardinality-based punctuality problem," *IEEE Intell. Transp. Syst. Mag.*, vol. 12, no. 4, pp. 78–91, Winter. 2020.

![](_page_13_Picture_30.jpeg)

Matias Romario Pinheiro Dos Santos ´ received the B.Sc. degree in computer science from CEUT, Teresina, the M.Sc. degree in computer science from the Federal University of Ceara, and the Ph.D. ´ degree in computer science from the Federal University of Bahia. He is a Faculty Member with the Federal Institute of Ceara (IFCE). His current ´ research interests include mobile networks, artificial intelligence applied to optical and mobile networks, and AI-driven decision support.

![](_page_13_Picture_32.jpeg)

Rodrigo Izidoro Tinini received the degree in computer science from the Municipal University of Sao Caetano do Sul in 2011, the master's degree ˜ in computer science from the Federal University of ABC, Sao Paulo, Brazil, in 2014, and the Ph.D. ˜ degree in computer science from the University of Sao Paulo in 2019. Since 2022, he has been an ˜ Assistant Professor with the Federal University of ABC. His current research interests include optical networks, B5G/6G networks, the Internet of Things, and artificial intelligence applied to optical and mobile networks.

![](_page_13_Picture_34.jpeg)

Gustavo Bittencourt Figueiredo (Senior Member, IEEE) received the B.Sc. degree in computer science from Salvador University in 2001, and the M.Sc. and Ph.D. degrees in computer science from the University of Campinas, in 2003 and 2009, respectively. He is an Associate Professor with the Federal University of Bahia (UFBA), where he has been a Faculty Member since 2010. Over the years, he has coordinated several research and development projects with public and industrial funding. His main research interests include the design and analysis of

network algorithms, graph theory, combinatorial optimization, and machine learning problems involving optical and mobile networks. He has served as a TPC member for several prestigious conferences in the field.
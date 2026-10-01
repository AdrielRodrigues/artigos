---
title: "XGS-PON-Standard Compliant DBA Algorithm for Option 7.x Functional Split-Based 5G C-RAN"
tema_principal: 5g6g
temas_relacionados: []
ano: 2024
autores: []
veiculo: null
pdf: ../pdf/xgs-pon-standard_compliant_dba_algorithm_for_option_7x_functional_split-based_5g_c-ran.pdf
---

# XGS-PON-Standard Compliant DBA Algorithm for Option 7.x Functional Split-Based 5G C-RAN

Md Shahbaz Akhtar<sup>®</sup>, Mohit Kumar<sup>®</sup>, Md Iftekhar Alam, and Aneek Adhya<sup>®</sup>, Senior Member, IEEE

Abstract—A 10-Gigabit Capable Symmetrical Passive Optical Network (XGS-PON) is considered as a cost-efficient fronthaul network solution for the Fifth Generation (5G) Centralized Radio Access Network (C-RAN). However, meeting the stringent latency requirements of C-RAN fronthaul with XGS-PON is challenging, as its upstream capacity is shared in the time-domain, and Dynamic Bandwidth Allocation (DBA) mechanism is employed to manage upstream traffic. The major issue with conventional DBA algorithms is that data arriving in the Optical Network Unit (ONU) buffer must wait for at least one DBA cycle before being scheduled, leading to poor delay performance. To address this, we propose a novel DBA algorithm named Traffic Predictionbased Enhanced Residual Bandwidth Utilization (TP-ERBU) that integrates a traffic prediction mechanism with enhanced residual bandwidth utilization to optimize delay performance in Option 7.x functional split-based C-RAN fronthaul over XGS-PON. The algorithm predicts future traffic to reduce delays in ONUs and reallocates residual bandwidth from lightly loaded ONUs to heavily loaded ones. Additionally, we develop an XGS-PONbased C-RAN simulation module named XCRAN-SIMMODULE, using the OMNeT++ network simulator. Simulation results demonstrate that TP-ERBU improves packet delay by 20.59%, upstream channel utilization by 38.33%, packet loss by 25.00%, jitter by 5.71%, and throughput by 15.56% compared to existing algorithms.

Index Terms—5G, C-RAN fronthaul, dynamic bandwidth allocation, functional splitting, XGS-PON.

#### I. INTRODUCTION

<span id="page-0-0"></span>ENTRALIZED Radio Access Network (C-RAN) is a potential next-generation RAN design, where the Baseband Unit (BBU) functions are managed centrally for enhanced radio resource allocation, energy efficiency, and cost savings [1], [2]. In addition to resource efficiency, C-RAN brings agility, flexibility, and rapid time-to-market acceleration for future network capabilities that can be achieved via software upgrades without any major hardware changes [3]. C-RAN, originally introduced by China Mobile, refers to the split of base station functionalities into two entities: the Remote Radio Head (RRH) and the BBU [4]. However, over time, the concept has evolved to include more complex architectures. The introduction of new standards by 3GPP (such as in

Received 7 June 2024; revised 30 October 2024 and 10 March 2025; accepted 26 May 2025. Date of publication 2 June 2025; date of current version 7 October 2025. The associate editor coordinating the review of this article and approving it for publication was H. Wu. (Corresponding author: Md Shahbaz Akhtar.)

Md Shahbaz Akhtar, Mohit Kumar, and Md Iftekhar Alam are with the Department of Electronics and Communication Engineering, Purnea College of Engineering, Purnea 854301, India (e-mail: shahbaz.iitp@gmail.com).

Aneek Adhya is with the Department of GSSST, Indian Institute of Technology Kharagpur, Kharagpur 721302, India.

Digital Object Identifier 10.1109/TNSM.2025.3575938

Release 15 for 5G) and the O-RAN Alliance extended the C-RAN architecture to a more modular design, often including Radio Units (RU), Digital Units (DU), and Centralized Units (CU). The lower physical layer functions are performed by the RUs, while the DUs handle higher physical layer functions, Media Access Control (MAC) operations, and radio control tasks. The Common Protocol Radio Interface (CPRI) or Open Base Station Architecture Initiative (OBSAI) protocol defines the rules for data transmission between DU and RU [5]. The higher-level RAN operations such as Radio Resource Control (RRC) and Packet Data Convergence Protocol (PDCP) are carried out by the CUs. While CUs and DUs are often placed in a centralized location called the BBU pool for coordinating radio resource allocation and performing complex operations such as radio scheduling and channel coding, the RUs are positioned as close to the antennas as possible.

<span id="page-0-3"></span>Two critical challenges associated with C-RAN design include (A) the large fronthaul bandwidth requirement and (B) the long transmission reach between RRHs and their controlling DUs (i.e., fronthaul reach). The first challenge is closely related to the RAN functional splitting between high and low physical layers. The functional splits impose technological complexity and cost-efficiency trade-offs while enabling lower fronthaul line rates and laxer latency requirements. The required fronthaul bandwidth varies between 614.4 Mbps (for Option 1) to 10.1376 Gbps (for Option 8). Moreover, if the total end-to-end latency budget is taken into account, the fronthaul network's latency should normally be less than 300s [6]. Considering these huge bandwidth and stringent latency requirements, fiber-based fronthaul solutions are ideally suited for C-RAN design.

<span id="page-0-5"></span><span id="page-0-4"></span><span id="page-0-2"></span><span id="page-0-1"></span>While a point-to-point (PtP) fiber link may initially seem like a viable fronthaul solution, its practicality is hindered by the high cost of fiber and transceivers required [7], [8]. Therefore, our focus is on a Time Division Multiplexed (TDM)-based 10-Gigabit Capable Symmetrical PON (XGS-PON) fronthaul network due to its simplicity and the widespread availability of Optical Distribution Network (ODN). XGS-PON utilizes passive devices in the ODN that do not require a power source to operate, resulting in reduced operational and maintenance costs [9], [10]. Additionally, XGS-PON offers a symmetrical data rate of 10 Gbps in both the downlink and uplink directions.

# <span id="page-0-6"></span>A. Motivation

Option 7.x has been identified by standardization bodies (3GPP, O-RAN, Small Cell Forum) as a suitable functional

split for 5G C-RAN, enabling reduced fronthaul capacity and latency requirements. While XGS-PON offers a cost-effective fronthaul solution, its inherent upstream scheduling delay (one DBA cycle, typically 125 μs to 1 ms) significantly exceeds the C-RAN latency budget of 300 μs, making reactive DBA schemes insufficient under bursty traffic conditions. Existing DBA proposals attempt to minimize delay, but most focus on IEEE PONs (e.g., 10G EPON) rather than ITU PONs like XGS-PON, which support lower delays through fixed frame length and frame fragmentation. While prior studies explore traffic prediction in XGS-PON-based fronthaul, our work uniquely integrates a prediction mechanism with enhanced residual bandwidth utilization to jointly optimize delay and throughput in Option 7.x-based C-RAN.

### *B. Objective*

The primary objective of this paper is to address the challenge of jointly optimizing throughput and delay in XGS-PON-based C-RAN fronthaul networks, specifically for Option 7.x functional splits. While existing DBA algorithms focus on either throughput or delay optimization, our work seeks to achieve a balance between these two critical performance metrics. To this end, we propose a novel DBA algorithm named *Traffic Prediction-based Enhanced Residual Bandwidth Utilization (TP-ERBU)*, which integrates a traffic prediction mechanism with enhanced residual bandwidth utilization. Unlike prior works, our approach dynamically reallocates residual bandwidth from lightly loaded ONUs to heavily loaded ones, ensuring efficient resource utilization while minimizing latency. This dual focus on throughput and delay optimization distinguishes our work from existing solutions and addresses a critical gap in the literature.

# *C. Challenges*

The primary challenge lies in designing an XGS-PONstandard-compliant DBA for transparent optical transport carrying Constant Bit Rate (CBR) traffic on the C-RAN fronthaul with minimal delay. The delay in XGS-PON is particularly noticeable in the upstream direction, where the Optical Network Unit (ONU) awaits the DBA grant from the optical line terminal (OLT) before initiating upstream transmission. In conventional DBA schemes, *Report* frames are transmitted to the OLT to indicate ONU buffer occupancy, following which the DBA engine at the OLT determines bandwidth allocation for each ONU. Allocated bandwidth to each ONU is communicated via *Gate* frames, and an ONU may transmit data only as permitted by Gate frames. Consequently, uplink data arriving at an ONU from the RRH between the transmission of Report frames and the reception of Grant frames must wait for at least one DBA cycle before being scheduled. This leads to increased packet delay and poor upstream channel utilization. Any traffic prediction-based technique capable of estimating future traffic can significantly reduce the waiting period in the ONU buffer. However, the challenge lies in how the OLT learns the traffic arrival patterns of individual ONUs in real-time and anticipates traffic during the waiting period. Another challenge arises from the fact that typical TDM-PONs require a quiet window to range new ONUs, during which no transmission is permitted, thereby disrupting the CBR traffic flow of CPRI.

### *D. Contributions*

The main contributions of this research work are outlined as follows:

- *•* We introduce a XGS-PON-standard compliant DBA algorithm named *TP-ERBU* to enhance delay performance and upstream channel utilization in Option 7.x functional split-based C-RAN fronthaul. The proposed TP-ERBU algorithm is specifically designed to address the challenges of dynamic bandwidth allocation in XGS-PON based 5G C-RAN. It integrates a traffic prediction mechanism, adapted from techniques used in GPON networks [\[11\]](#page-12-10), with an enhanced residual bandwidth utilization scheme to optimize resource allocation and minimize latency. This integrated solution effectively predicts future traffic demands and dynamically adjusts bandwidth allocation to reduce queuing delays and improve overall network performance.
- <span id="page-1-1"></span>*•* In each DBA cycle, the proposed algorithm tracks and stores the residual bandwidth of lightly loaded ONUs in the present cycle, then uniformly distributes it to heavily loaded ONUs in the subsequent cycle. Thus, unlike conventional approaches in which the maximum allocation bytes limit was assumed to be constant, the limit in our approach is dynamic.
- *•* We developed an XGS-PON-based C-RAN simulation module, named XCRAN-SIMMODULE, using OMNeT++ network simulator to validate TP-ERBU's performance against two state-of-the-art DBA algorithms: gGAINT [\[12\]](#page-12-11) and Optimized RR [\[13\]](#page-12-12).
- <span id="page-1-3"></span><span id="page-1-2"></span>*•* The results exhibit substantial enhancements in packet delay performance, upstream channel utilization, reduced packet loss and jitter, and improved throughput compared to existing algorithms.

The rest of the paper is structured as follows: In Section [II,](#page-1-0) we discuss the background of C-RAN functional splits and related work. In Section [III,](#page-3-0) we describe the network architecture and fronthaul latency analysis of C-RAN. In Section [IV,](#page-6-0) we discuss the traffic prediction approach and dynamic bandwidth allocation scheme employed in TP-ERBU. Section [V](#page-8-0) discusses the numerical assessment and performance comparison of our proposed TP-ERBU algorithm against the existing DBA algorithms. Section [VI](#page-12-13) concludes the paper with some suggestions for future research directions.

# II. BACKGROUND AND RELATED WORK

### <span id="page-1-0"></span>*A. Functional Split Options for C-RAN Fronthaul*

The functional split options for C-RAN fronthaul, as suggested by 3GPP, are critical in determining the fronthaul bandwidth and latency requirements. These options range from fully centralized (Option 1) to fully distributed (Option 8), with varying degrees of centralization in the RAN protocol stack. Figure [1](#page-2-0) illustrates the eight functional split options, which are briefly described below:

![](_page_2_Figure_2.jpeg)

Fig. 1. 3GPP functional split options for C-RAN fronthaul [\[14\]](#page-12-14), [\[15\]](#page-12-15).

- *• Option 1:* The entire RAN stack is centralized, providing minimal latency and maximum control.
- *• Option 2:* The PDCP layer is centralized, while the RLC and lower layers remain at the edge, balancing control with reduced fronthaul data rates.
- *• Option 3:* The RRC layer is centralized, allowing for adaptive RAN configurations with minimal latency on the fronthaul.
- *• Option 4:* The RLC layer is centralized, while MAC functions remain at the edge, reducing fronthaul data rates by transmitting processed packets.
- *• Option 5:* The MAC layer is centralized, enabling centralized scheduling and resource allocation while keeping PHY tasks local.
- *• Option 6:* The split occurs within the PHY layer itself, centralizing high-PHY functions to support centralized beamforming and control with lower bandwidth requirements.
- *• Option 7.x:* This series of splits (Options 7.1, 7.2, and 7.3) focuses on intra-PHY layer splits, allowing flexible bandwidth utilization and control.
- *• Option 8:* Only RF functions are retained at the edge, allowing maximum centralization but requiring the highest fronthaul bandwidth.

# *B. Related Works*

Numerous studies have delved into the latency issues associated with TDM-PON-based fronthaul technology. In [\[16\]](#page-12-16), a cooperative DBA scheme is introduced to reduce fronthaul delay by allocating bandwidth to ONUs using mobile scheduling information from the BBU. This approach has achieved reasonable fronthaul latency for fiber lengths of 10- 20 km. However, the strategy requires strong synchronization and coordination between the BBU and the OLT, which can be challenging to establish. In [\[12\]](#page-12-11), a group-assured GIANT (gGIANT) DBA algorithm is proposed to improve the delay performance of XG-PON for transporting backhaul traffic. By distributing unused data from individual assured bandwidth to other Transmission Containers (T-CONTs) within the same group, the gGIANT algorithm provides a pool of guaranteed bandwidth to all group members. Although upstream channel

<span id="page-2-3"></span><span id="page-2-1"></span><span id="page-2-0"></span>utilization has improved significantly, the algorithm fails to meet the latency requirements for C-RAN fronthaul. The Round-robin DBA (RR-DBA) is the first XG-PON-standard compliant DBA algorithm introduced for fronthaul in [\[17\]](#page-12-17). RR-DBA assigns the same amount of bandwidth to all T-CONTs, which is less than or equal to a predefined value. Despite good delay performance, the 300s latency required for fronthaul has not been met under bursty traffic conditions. In paper [\[13\]](#page-12-12), the authors propose an improved version of RR-DBA named optimized RR-DBA to support fronthauling over XG-PONs. The algorithm determines the total excess bandwidth in each upstream cycle and redistributes it to congested T-CONTs in the next cycle. This enables congested T-CONTs to leverage the extra bandwidth of less congested T-CONTs, addressing issues with the RR-DBA algorithm.

<span id="page-2-6"></span><span id="page-2-5"></span><span id="page-2-4"></span><span id="page-2-2"></span>Since DBA alone cannot fully resolve latency issues in TDM-PON-based C-RAN fronthaul, traffic prediction has been proposed to reduce ONU buffer waiting time. P-DBA [\[11\]](#page-12-10) uses a high-order moving average model to estimate traffic arrivals in GPON, achieving high bandwidth and low latency but lacking clarity on traffic generation methods. Kyriakopoulos and Papadimitriou [\[18\]](#page-12-18) employ T-CONT-based traffic prediction to improve bandwidth allocation and reduce upstream delays. Singh et al. [\[19\]](#page-12-19) propose an ML-based DBA for XGS-PON, dynamically allocating bandwidth using realtime traffic data. While improving bandwidth utilization, it is sensitive to sudden traffic variations and lacks an efficient latency management mechanism, making it less suitable for 5G C-RAN fronthaul. Similarly, Zhang et al. [\[20\]](#page-12-20) employ deep learning for traffic prediction and resource allocation, enhancing accuracy but focusing on bandwidth efficiency rather than real-time latency challenges. The high computational cost further limits its applicability to low-latency fronthaul networks. One of the key limitations of DL-based methods is their sensitivity to sudden traffic variations, which can lead to inaccurate predictions and suboptimal resource allocation. In contrast, our proposed high-order moving average model is designed to handle sudden traffic variations more effectively. By incorporating a weighted moving average of past traffic data, our method can adapt to rapid changes in traffic patterns without requiring extensive computational resources. This makes our approach more suitable for the dynamic and bursty

![](_page_3_Figure_2.jpeg)

<span id="page-3-1"></span>Fig. 2. Illustration of XGS-PON network architecture. The wavelength ranges for upstream traffic (1260-1280 nm, shown in blue) and downstream traffic (1575-1580 nm, shown in red) are indicated at the bottom of the figure.

<span id="page-3-3"></span>nature of C-RAN fronthaul traffic, where sudden variations are common. Wang et al. [\[21\]](#page-12-21) apply reinforcement learning for resource allocation in optical networks. However, its reliance on static resource allocation and long training times limits adaptability to fluctuating 5G C-RAN traffic, making it unsuitable for latency-sensitive applications.

### *C. Gap in the Literature*

While the aforementioned studies have made significant contributions to improving DBA algorithms for XGS-PONbased fronthaul networks, a critical gap remains in the literature. Specifically, existing works such as [\[19\]](#page-12-19), [\[20\]](#page-12-20) focus on improving resource allocation and throughput but often neglect the stringent low-latency requirements of 5G C-RAN fronthaul. Moreover, these works suffer from reproducibility issues due to their reliance on complex deep learning models, which require extensive training and real-time updates, making them unsuitable for practical deployment in lowlatency scenarios. In contrast, our work addresses this gap by proposing a novel DBA algorithm, which integrates an advanced traffic prediction mechanism with enhanced residual bandwidth utilization. Unlike prior works, TP-ERBU is specifically designed to meet the low-latency requirements of 5G C-RAN fronthaul while ensuring high throughput and efficient resource utilization. This dual focus on latency and throughput optimization, combined with the algorithm's simplicity and reproducibility, distinguishes our work from existing solutions.

# <span id="page-3-0"></span>III. NETWORK ARCHITECTURE AND FRONTHAUL LATENCY ANALYSIS

# *A. XGS-PON System Model*

XGS-PON is a fiber-based transport network in which the OLT (placed at operator's central office) and the ONU are the two primary active transmission devices (shown in Figure [2\)](#page-3-1). At the remote node, passive devices such as power splitters and combiners are deployed, that don't need any power source to fan-out a single feeder fiber from the OLT to several ONUs. XGS-PON provides four distinct bandwidth categories associated with T-CONTs for the quality of service purposes: *fixed* (T-CONT-1), *assured* (T-CONT-2),

![](_page_3_Figure_10.jpeg)

<span id="page-3-2"></span>Fig. 3. (a) D-RAN Architecture (b) C-RAN Architecture and (C) XGS-PON based C-RAN fronthaul.

*non-assured* (T-CONT-3), and *best-effort* (T-CONT-4). The T-CONT-1 has a fixed bandwidth and is statically served, whereas the assured bandwidth is assigned dynamically based on the queue's bandwidth demand. Non-assured bandwidth and best-effort bandwidth are excess bandwidth that an OLT can dynamically distribute to a queue based on the queue's bandwidth request. The service priority order is T-CONT-1, followed by T-CONT-2 (assured bandwidth), T-CONT-3 (nonassured bandwidth), and T-CONT-4 (best-effort bandwidth).

For each ONU to be able to transmit data in the upstream channel without interfering with the traffic of another ONU, a DBA mechanism is implemented at the OLT. In each DBA cycle, ONUs send their bandwidth requests through upstream frames, and the OLT processes those requests and assigns grants to the ONU in the subsequent DBA cycle. The DBA generates a schedule of time-slots based on its scheduling priorities and broadcasts it to all the ONUs through a bandwidth map (BWmap), which is a header field in the downstream frame. Each BWmap may have multiple fields like Alloc ID (unique allocation identifier for each T-CONT), start time (time to synchronize upstream data from ONUs located at different locations), DBRu (notifies authorization for the Alloc ID of an ONU to send the data in the next upstream frame), and Grant size (total bandwidth allocated to a specific Alloc ID).

# *B. C-RAN Architecture Employing XGS-PON Fronthaul Transport*

<span id="page-3-4"></span>Figures [3\(](#page-3-2)a) and [3\(](#page-3-2)b) show the architectural difference between the Distributed RAN (D-RAN) and C-RAN architecture. In the traditionally deployed D-RAN architecture, the entire base station functionalities are performed at the cell sites. The major problems with the D-RAN architecture include the lack of centralization, resource sharing, greener communication, and the capability to support advanced wireless technologies [\[22\]](#page-12-22), [\[23\]](#page-12-23). To address the above issues, C-RAN has been proposed, where the majority of base station <span id="page-4-5"></span>functionalities are performed at centrally located BBU pool, leaving behind the low energy consuming RRHs at the cell site [24]. The radio signals originating from hundreds of RRHs (connected via the fronthaul network) are controlled by the centrally located BBU pool [25].

<span id="page-4-6"></span>The network topology of the C-RAN architecture using XGS-PON-based fronthaul is depicted in Figure 3(c). The architecture consists of a centralized BBU pool, several RRHs connected to ONUs, and an OLT located at the central office. The XGS-PON fronthaul network carries the traffic from the RRHs to the BBU pool via the ONUs and OLT. ONUs serve as intermediate nodes responsible for transmitting data received from the RRHs to the OLT. The OLT performs the bandwidth allocation for all ONUs by dynamically distributing the available upstream capacity based on the traffic demand. The proposed TP-ERBU algorithm is integrated into the OLT and operates by predicting future ONU traffic and reallocating residual bandwidth accordingly. The algorithm works as follows: traffic from the RRHs arrives at the ONUs, which then send buffer occupancy reports to the OLT. Using these reports, the TP-ERBU algorithm predicts future traffic arrivals at each ONU and adjusts the bandwidth allocation in advance. The residual bandwidth from lightly loaded ONUs is redistributed to heavily loaded ONUs, ensuring optimal bandwidth utilization and reduced latency. This architecture ensures that the stringent latency and bandwidth requirements of the 5G Option 7.x functional splits are met efficiently.

### C. Objective: Joint Optimization of Throughput and Delay

The primary goal of this work is to jointly optimize throughput and delay in XGS-PON-based C-RAN fronthaul networks. While existing DBA algorithms often focus on either throughput or delay, our proposed TP-ERBU algorithm addresses both metrics simultaneously. By integrating a traffic prediction mechanism with enhanced residual bandwidth utilization, TP-ERBU ensures efficient resource allocation, minimizes queuing delays, and maximizes upstream channel utilization. This dual focus on throughput and delay optimization is critical for meeting the stringent requirements of 5G C-RAN fronthaul, particularly for Option 7.x functional splits, where latency and bandwidth efficiency are paramount.

# D. Fronthaul Bandwidth Requirement Analysis of Option 7.x Splits

When we look at the intra physical layer split options (i.e., Option 7.x), the fronthaul bandwidth is a very important key performance indicator. Different 7.x split options facilitates beamforming, coordination between cells, reduced RRH complexity, etc., and are considered to be future-proof since they let the addition of advance wireless capabilities via software updates. The fronthaul bandwidth requirements of 7.x splits are primarily governed by physical characteristics defined as follow:

- The cell bandwidth  $(B_{cell})$  and the number of sub-carriers  $(N_s)$ .
- The modulation order (M), i.e., number of bits per symbol.

<span id="page-4-1"></span>TABLE I
FRONTHAUL CAPACITY REQUIREMENT FOR OPTION 8
AND OPTION 7.X FUNCTIONAL SPLITS

| Functional      | $R_x$ [Gbps] |        |        |         |  |
|-----------------|--------------|--------|--------|---------|--|
| Split           | 10 Mhz       | 20 Mhz | 40 Mhz | 100 Mhz |  |
| Option 8        | 3.677        | 7.357  | 14.714 | 36.787  |  |
| Option 7.1      | 2.15         | 4.3    | 8.6    | 21.5    |  |
| Option 7.2      | 0.537        | 1.075  | 2.15   | 5.376   |  |
| Option 7.3 (DL) | 0.067        | 0.134  | 0.268  | 0.67    |  |
| Option 7.3 (UL) | 0.335        | 0.67   | 1.34   | 3.35    |  |

- Number of MIMO layers  $(N_l)$ .
- The I/Q size  $(IQ_{bw})$ , i.e., the required number of bits to code a constellation point.
- The number of antenna ports  $(N_a)$ .

(1) 7.1 split: In this split, I/Q symbols are transmitted in the frequency domain. The overhead incurred by the frequency to time conversion is saved with this split option. The fronthaul bandwidth  $R_{7.1}$  (in bit/s) required by the 7.1 split primarily depends on the symbol size and number of antenna ports, and is calculated as:

<span id="page-4-4"></span>
$$R_{7.1} = 2 \cdot IQ_{hw} \cdot (T_s)^{-1} \cdot N_s \cdot N_a \cdot N_l \tag{1}$$

Here  $T_s$  is the symbol period that denotes the number of symbols transmitted in a time-slot. For example, considering normal cyclic prefix, LTE network transmitting 7 symbols per slot of 0.5ms, the value of  $T_s$  will be 0.5/7 = 0.07ms.

(2) 7.2 split: Similar to 7.1 split, 7.2 split sends I/Q signals in the frequency domain. However, signals received from multiple antenna ports are multiplexed together. As a result, the required fronthaul bandwidth  $R_{7.2}$  is divided by  $N_a$ , and the resulting bandwidth is:

<span id="page-4-2"></span>
$$R_{7.2} = 2 \cdot IQ_{bw} \cdot (T_s)^{-1} \cdot N_s \cdot N_l \tag{2}$$

(3) 7.3 split: The fronthaul with 7.3 split carries bits rather than I/Q symbols because the demodulation and modulation functions are performed near to the antennas. As a result, the required fronthaul bandwidth  $R_{7.3}$  is then divided by  $2 \cdot IQ_{bw}$ . The required fronthaul bandwidth in the downlink and uplink directions is calculated as:

<span id="page-4-3"></span>
$$R_{7.3DL} = M \cdot (T_s)^{-1} \cdot N_s \cdot N_l \tag{3}$$

$$R_{7.3UL} = M \cdot (T_s)^{-1} \cdot N_s \cdot N_l \cdot S_b \tag{4}$$

Here  $S_b$  denotes the soft bit size. It is important to note that the downlink sends hard bits, whereas the uplink sends soft bits (coded as real values).

Table I shows the required fronthaul bandwidth for a cell with bandwidths of 10, 20, 40, and 100 MHz, 2x2 MIMO  $(N_l=2)$ , 4 antenna ports  $(N_a=4)$ , and 16 QAM modulation (M=4). The required fronthaul bandwidth for Option 8 is shown for reference. While the required fronthaul bandwidth is reduced by half when employing 7.1 split as opposed to the earlier CPRI-based solution (i.e., Option 8), this study

<span id="page-4-0"></span><sup>&</sup>lt;sup>1</sup>In contrast to physical antennas, antenna ports are logical entities. On a single physical antenna, signals from multiple antenna port can be transmitted. In the same way, signal from a single port can be spread across multiple physical antennas.

focuses on Option 7.3 due to its lower fronthaul capacity requirement, making it more suitable for XGS-PON based C-RAN fronthaul.

This is important to note that the default values used in the bandwidth requirement analysis are selected based on guidelines and specifications provided by industry standards and prior research. Specifically, the bandwidth calculation follows the specifications in 3GPP TR 38.801, which outlines the fronthaul bandwidth requirements for various functional split options, including Option 7.x [26]. Additionally, the XGS-PON standards defined in ITU-T G.9807.1 [27] are used to determine the upstream and downstream data rates. Further insights on fronthaul bandwidth calculations and parameter assumptions can be found in [28], which supports the parameter choices for compression rates and functional split designs.

### <span id="page-5-3"></span>E. Fronthaul Latency Analysis

CPRI data is divided into blocks and then reassembled at the XGS-PON termination to multiplex several fronthaul lines onto the single XGS-PON. A block is sent using the DBA method on the XGS-PON at a set time slot once it has arrived on a particular fronthaul link. Also, CPRI rates can be different for each link, but the length of a CPRI frame is always the same. Therefore, the block duration, represented by  $T_b$ , is given in seconds instead of bits. For instance, when multiplexing at the hyper-frame level, the value of  $T_b$  will be 66.67s, whereas the standard TDM-PON have frame duration of 125s. In general, we can take any value of  $T_b$  that is convenient for multiplexing.

Prior to calculating the total fronthaul latency, we must estimate the transmission time of CPRI data (segmented into blocks) across the XGS-PON. We define the following parameters for this calculation:

- N: The number of fronthaul links between the BBU pool and RRHs. As shown in Figure 3(c), the links, ONUs, and RRHs are indexed by i = 1, ..., N.
- $-R_i$ : The bit rate on a particular fronthaul link i. The value of  $R_i$  depends on the functional splitting in use. In this study, we consider three different variants of Option 7 functional split, so the value of  $R_i$  can be any of the fronthaul line rates shown in Table I.
- C: The capacity of the XGS-PON. The capacity is considered to be symmetric with data rate of 10 Gbps for both uplink and downlink.
- B: Transmission time from the BBU Pool to the OLT.
- $l_i$ : The distance (in km) from the BBU pool to RRH i.
- $P(l_i)$ : Propagation delay (in seconds) over a distance  $l_i$  and is calculated at 5s/km.
- $T_b$ : The duration of a block (in s)
- $\rho$ : Compression ratio
- $-\mu$ : FEC code rate
- $H_b$ : Header bits added to the payload
- $G_b$ : Guard bits added to the payload. Note that the guard bits only affect the uplink traffic, i.e.,  $G_b=0$  for downlink.
- $-\kappa_i$ : Represents the additional smoothing time required to maintain synchronization across different fronthaul

links. This smoothing time accounts for any necessary adjustments to ensure that CPRI frames from multiple links arrive in a synchronized manner at the ONU and BBU pool.

- $-Q_i$ : Queuing delay of CPRI data at ONU buffer
- $D_c$ : Compression and decompression delay
- $D_e$ : FEC encoding and decoding delay
- $-D_m$ : Other miscellaneous electronic delays such as, scrambling and de-scrambling, reading from and writing to memory, etc.

<span id="page-5-2"></span><span id="page-5-1"></span>The transmission time from the ONU over the XGS-PON for a block from link i is calculated as:

$$T_i = \frac{T_b \cdot R_i \cdot \rho}{C \cdot \mu} + \frac{H_b + G_b}{C} \tag{5}$$

In the above equation, the block duration  $T_b$  refers to the payload transmission time, while  $H_b$  and  $G_b$  represent the time added for headers and guard bits, respectively. These elements ensure the integrity and synchronization of the transmission but are separate from the payload time.

Queue Stability Constraint: For the ONU queue buffer to be stable, XGS-PON needs to have adequate capacity to handle the total traffic coming in from all CPRI links, i.e.,

<span id="page-5-0"></span>
$$\sum_{i=1}^{N} \frac{R_i \cdot \rho}{\mu} \le C \tag{6}$$

or more precisely it can be defined as:

$$\sum_{i=1}^{N} T_i \le T_b \tag{7}$$

After estimating the transmission time of CPRI data over XGS-PON, we now assess the fronthaul network's total latency, which includes all delay components. We only look at the uplink, as the key difference in the downlink is the exclusion of the guard bits  $G_b$  only. Aside than that, the link is simply inverted, with the latency components being symmetrical analogues. The overall latency for the CPRI link i is calculated as:

$$F_i = B + Q_i + T_i + P(l_i) + \kappa_i + D_c + D_e + D_m$$
 (8)

The values of  $Q_i$  and  $\kappa_i$  vary according to the application scenario, leading to three different cases:

- Case A: Synchronized Phases In this case, all fronthaul links are perfectly synchronized, and no smoothing time  $(\kappa_i = 0)$  is required. The queuing delay  $Q_i$  is minimized, as data blocks from all links arrive at the ONU simultaneously.
- Case B: Unsynchronized with Controlled Phases In this case, minor phase misalignments exist between the fronthaul links. A small smoothing time  $(\kappa_i > 0)$  is introduced to maintain synchronization. The queuing delay  $Q_i$  increases slightly, as data blocks may arrive at different times, but the phases are still controlled.
- Case C: Unsynchronized with Random Phases In this case, significant random phase misalignment occurs between the fronthaul links, requiring a larger smoothing time  $(\kappa_i)$  to restore synchronization. This results in a

![](_page_6_Figure_2.jpeg)

Fig. 4. An example of synchronized phases with three CPRI links.

<span id="page-6-1"></span>larger queuing delay  $Q_i$ , as data blocks arrive at the ONU at different times and must wait longer for transmission.

In this study, we only consider the case of synchronized phases, in which the traffic phase is synchronized on all CPRI links. This means that CPRI frames must reach to the ONU on all CPRI lines at the same time and must also reach at the BBU in synchrony. This is a common situation when all BBUs in a pool are owned by the same network operator.

In Figure 4, we demonstrate the synchronized phase with three CPRI links (i.e., N = 3), along with the breakdown of  $T_b$  into its payload, header  $(H_b)$ , and guard bits  $(G_b)$ . The payload occupies the block duration  $T_b$ , while headers and guard bits are added separately to the overall transmission time. Each CPRI link has a periodic arrival of 1 block in every B seconds. In general, the bit rates on these links can be any value; however, for illustration, we consider the bit rate on link 2 to be double than that of links 1 and 3 (which are equal). We ensure that the Queue Stability Constraint defined in Eq. (6) is satisfied. The traffic from RRH is multiplexed and queued in the ONU buffer until a transmission slot becomes available. Without sacrificing generality, the RRHs are considered to be serviced in increasing order. We compute the delay by taking link 2 as an example. After B seconds of transmission time from RRH to ONU, link 2 suffers a queuing time  $Q_2$  due to the transmission time  $T_1$  of link 1 across the PON followed by transmission time  $T_2$  and propagation delay  $P(l_2)$  for the block to reach the OLT. Similarly, each CPRI link i incurs a delay equal to  $Q_i + T_i + P(l_i)$ , and the worst-case delay for on any link i is calculated as:

<span id="page-6-2"></span>
$$F_i^{max} = B + \max_i (Q_i + T_i + P(l_i)) + D_c + D_e + D_m$$
 (9)

Among all the delay components stated in Eq. (9), we seek to minimize the queuing delay  $Q_i$  of CPRI data in the ONU buffer using our proposed TP-ERBU DBA scheme.

### <span id="page-6-0"></span>IV. DYNAMIC BANDWIDTH ALLOCATION FOR XGS-PON-BASED C-RAN FRONTHAUL

In the conventional DBA schemes, ONUs transmit request frames to the OLT for reporting the amount of data present in the ONU buffer, and the OLT updates the BWmap based on the request frame. Following the calculation of the bandwidth assignment, the OLT sends grant messages to ONUs to assign

![](_page_6_Figure_11.jpeg)

<span id="page-6-3"></span>Fig. 5. Polling Mechanism Diagram.

the transmission time slot. We describe the polling mechanism involved in this process, taking ONU i as an example in Figure 5. Consider if the  $t^{th}$  cycle's entire time slot is  $T_1$ - $T_3$ and the data packets are sent in  $T_1$ - $T_2$ , then the waiting period between the  $t^{th}$  cycle and its subsequent cycle is  $T_2$ - $T_3$ . The amount of data that was in the queue at time  $T_2$  is reported in the request frame. However, additional data will arrive in the queue during the waiting period without being reported. Therefore, the request frame does not represent the real-time ONU buffer occupancy. In other words, data received during the waiting period must be queued for at least one DBA cycle before being scheduled. This increases the network delay significantly [29].

# <span id="page-6-4"></span>A. Traffic Prediction-Based Enhanced Residual Bandwidth *Utilization (TP-ERBU)*

To better describe the TP-ERBU algorithm, we define the following parameters:

- $B_w^{total}$ : Total XGS-PON upstream frame size (in bytes).  $B_{res}^t$ : Total Residual bandwidth in the  $t^{th}$  cycle.
- N: Number of ONUs in the network.
- $A_{max}$ : Maximum allocation bytes limit.
- $A_i^t$ : Updated maximum allocation byte limit of ONU i for the  $t^{th}$  cycle.
- $R_i^t$ : Data requested by ONU i in the  $t^{th}$  cycle.
- $G_i^t$ : Data granted to ONU i for the  $t^{th}$  cycle.
- $Y_i^t$ : Additional data received during the waiting period at ONU i in the  $t^{th}$  cycle.
- $P_i^t$ : Data predicted by traffic prediction mechanism for ONU i during waiting period in the  $t^{th}$  cycle.
- Q: A boolean variable use to mark an ONU as overloaded or lightly loaded.
- M: A counter that counts the total number of heavily loaded ONUs in each allocation cycle.
- i: A counter for indexing scheduled ONU during the allocation cycle, where  $1 \le i \le N$ .
- t: A counter for counting allocation cycle number.
- k: Number of DBA cycle before  $t^{th}$  cycle.
- <span id="page-6-5"></span>1) Traffic Prediction Mechanism: ONU i forecasts the amount of additional data that will arrive in the waiting period based on the amount of actual data that had arrived in the waiting period in the k cycle before the current cycle. A highorder moving average model is used to improve the accuracy of the prediction [30]. It anticipates the amount of data arrived during the waiting period in the current cycle  $(P_i^t)$  based on the actual amount of data received in waiting period in multiple cycles prior to this cycle, i.e.,  $Y_i^{t-1}$ ,  $Y_i^{t-2}$ ,..,  $Y_i^{t-k}$ . The

high-order moving average model effectively handles sudden traffic variations by assigning higher weights to recent data, enabling rapid adaptation. In contrast, deep learning-based methods require retraining or fine-tuning, increasing latency and computational overhead. By leveraging a weighted moving average, our approach maintains prediction accuracy under sudden traffic changes, making it well-suited for real-time C-RAN fronthaul applications.

The predicted data during waiting period is calculated as:

<span id="page-7-0"></span>
$$P_i^t = W_i^{t-k} + \beta_1 \cdot \Delta Y_i^{t-1} + \beta_2 \cdot \Delta Y_i^{t-2} + \dots + \beta_k \cdot \Delta Y_i^{t-k}$$

$$(10)$$

where,

$$W_i^{t-k} = \frac{1}{k} \sum_{t-k}^{t-1} Y_i^t t = 1, 2, \dots, k = 1, 2, \dots,$$
 (11)

$$\Delta Y_i^t = Y_i^t - Y_i^{t-1} \tag{12}$$

In Eq. (10),  $W_i^{t-k}$  denotes the arithmetic mean of the data sequence of k items before the  $t^{th}$  cycle,  $\Delta Y_i^t$  is the difference between  $Y_i^t$  and  $Y_i^{t-1}$ , and  $\beta_1$ ,  $\beta_2,\ldots,\beta_k$  are the weighting factors. According to the above relations, there is a high correlation between the amount of data coming during the waiting period and the actual amount of data arrived during the waiting period in the preceding cycles. To make sure the prediction is accurate, the moving average order must be increased. However, as the number of periodic intervals goes up, the correlation between the predicted data and the actual received data goes down. In addition, the cost of real implementation will grow as the number of orders increases. Therefore, the number of orders should not be blindly taken a high value while making predictions. For good performance, we use a fourth-order moving average and weighting values of 0.1, 0.2, 0.3, and 0.4 based on several experiment [11].

**Execution Process:** The traffic prediction mechanism is executed at the OLT. ONUs send buffer occupancy reports in each DBA cycle, and the OLT uses these reports to estimate the additional traffic expected to arrive before the next cycle. This predicted value is then added to the reported buffer occupancy, allowing the OLT to allocate grants in advance, thereby reducing queuing delays.

2) Bandwidth Allocation Scheme: In Option 7.x split-based C-RAN, the instantaneous traffic directed to each ONU exhibits significant temporal variance. Consequently, certain ONUs may experience light loading during each upstream frame transmission cycle, necessitating a lower maximum allocation bytes limit  $(A_{max})$  in grant allocations. Conversely, other ONUs may face overloading and require grant allocations exceeding the maximum allocation bytes limit. The excess bandwidth from lightly loaded ONUs cannot be efficiently reused when employing a DBA protocol with a fixed maximum allocation byte limit, leading to suboptimal utilization of the XGS-PON capacity. To overcome these limitations, we propose the concept of utilizing the dynamic maximum allocation bytes limit  $(A_i^t)$ . Initially, we calculate the total residual bandwidth by summing the unused bandwidth of each lightly loaded ONU at the end of each allocation

**Algorithm 1:** Traffic Prediction-Based Enhanced Residual Bandwidth Utilization (TP-ERBU)

```
Result: Optimal grant allocation for ONUs
Initialize all parameters. B_w^{total}=155.52\mathrm{KB};~M=0; B_{res}^t=0;~P_i^t=0;~A_i^t=A_{max}=B_w^{total}/N;~t=0 // Start of DBA cycle
 2 Start DBA cycle
 3 for i \leftarrow 1 to N do
        // Poll each ONU for its buffer
       poll ith ONU's T-CONT for its buffer occupancy
        report R_i^t;
        calculate W_i^{t-k} and \Delta Y_i^t using Eqs. (2) and (3);
        predict the traffic arrived during the waiting period
        (P_i^t) using Eq. (1);
        send the buffer report as (R_i^t + P_i^t);
        after receiving buffer report, assign grant allocation
       to i^{th} ONU as G_i^t = \min(R_i^t + P_i^t, A_i^{t-1}); increase the counter, i + +;
        if R_i^t + P_i^t > A_{max} then
            mark ONU as overloaded (Q = True);
            increase the number of overloaded ONU as
12
            M = M + 1;
            add the residual bandwidth to the ONU's
13
            maximum allocation bytes as
            A_i^t = A_{max} + B_{res}^{i,t-1};
14
            mark ONU as lightly loaded (Q = False);
15
            set the maximum allocation bytes to default
16
            value, A_i^t = A_{max};
17
        if all ONUs are polled then
18
            calculate residual bandwidth in the current cycle
19
            as B_{res}^t = (B_w^{total} - \sum_{i=0}^M A_i^t)/N; formulate bandwidth map;
            go to line 1:
21
22
           go to line 3;
24
```

cycle. Subsequently, we evenly redistribute the total residual bandwidth among heavily loaded ONUs in the subsequent allocation cycle. The detailed procedure of TP-ERBU is outlined in Algorithm 1 and elucidated as follows:

In the beginning of first allocation cycle, the algorithm initializes all defined parameters and commences the DBA cycle. The maximum allocation bytes are set to  $A_{max} = B_w^{total}/N$ , and the total residual bandwidth is initialized to  $B_{res}^t = 0$ . The process begins by polling ONUs for buffer occupancy reports. Each ONU transmits a report containing the actual data presently available in the ONU buffer along with the predicted data  $(R_i^t + P_i^t)$ . It's important to note that the accuracy of predicted data at the beginning may be limited due to the insufficient number of previous data sequences. Upon receiving

25 end

reports from all ONUs regarding buffer occupancy, the DBA engine utilizes these reports to assign grant allocations to each ONU as  $G_i^t = \min(R_i^t + P_i^t, A_i^{t-1})$ . Simultaneously, the DBA engine categorizes ONUs as overloaded if  $(R_i^t + P_i^t > A_{max})$ , otherwise, they are marked as lightly loaded, and the counter M is updated accordingly. The value of counter M is essential at the end of the allocation cycle to calculate the total residual bandwidth available for each overloaded ONU, which can be allocated in the next cycle. For overloaded ONUs, the residual bandwidth from the previous allocation cycle is added to the maximum allocation byte limit, resulting in an updated limit of  $A_i^t = A_{max} + B_{res}^{i,t-1}$ . Conversely, for lightly loaded ONUs, the maximum allocation byte is reset to the default limit  $(A_i^t =$  $A_{max}$ ). Once all ONUs are scheduled in the current allocation cycle and the number of heavily loaded ONUs is determined, the algorithm computes the residual bandwidth that can be uniformly allocated to all heavily loaded ONUs using  $B_{res}^t =$  $(B_w^{total} - \sum_{i=0}^M A_i^t)/N$ . Finally, the bandwidth allocation map is formulated and broadcasted back to the ONUs.

# B. Time and Space Complexity Analysis of TP-ERBU

We analyze the time and space complexity of TP-ERBU based on the number of ONUs, denoted as N. The time complexity is determined by per-ONU operations, including polling buffer occupancy, computing parameters ( $W_{*}^{t-k}$ ,  $\Delta Y_i^t$ ), predicting traffic via Eq. (1), and assigning bandwidth grants-each taking O(1) time. Since these operations run for all N ONUs, the total time complexity is O(N). Additionally, residual bandwidth computation and bandwidth map updates also take O(N) time, maintaining an overall time complexity of O(N). The space complexity is governed by storage for parameters like buffer occupancy reports  $(R_i^t)$ , predicted traffic  $(P_i^t)$ , and allocated bandwidth  $(A_i^t)$ , each requiring O(N) space. Residual bandwidth and constants require O(1)space, making the overall space complexity O(N). Thus, both time and space complexity scale linearly with the number of ONUs, resulting in O(N) for both.

While ML-based traffic prediction methods [19], [20] offer high accuracy, they incur significant computational overhead. Deep learning models require GPU-based inference, which, despite being fast (sub-millisecond), adds latency and complexity, making them less suitable for low-latency C-RAN fronthaul networks. Additionally, ML methods demand extensive training and frequent updates to adapt to traffic variations, further increasing their computational burden. In contrast, TP-ERBU's moving-average-based approach relies only on simple arithmetic operations, eliminating the need for complex models or GPUs. This ensures real-time deployment in latency-sensitive fronthaul networks with minimal computational cost. Section V-C quantifies the trade-offs between TP-ERBU and ML-based methods through an experimental comparison.

# C. Traffic Model for C-RAN Uplink Data

C-RAN fronthaul traffic may be characterized using the same model as used to characterize the backhaul traffic of small-cell LTE eNodeBs. This is because fronthaul data

<span id="page-8-3"></span><span id="page-8-2"></span>traffic dynamically changes based on the activity of mobile users, akin to backhaul traffic. The Next Generation Mobile Networks (NGMN) alliance has devised a framework for estimating backhaul traffic in small-cell LTE eNodeBs [31]. According to this framework, backhaul traffic of a base station exhibits two distinct loading conditions, dictated by the spatial distribution of mobile users within the cell [32]. These conditions are busy periods and silent periods. During busy periods, numerous users concurrently utilize the cell's radio resources. Conversely, during silent periods, only a single user may access the cell, monopolizing the cell's resources entirely. A densely deployed C-RAN comprises numerous RRHs, resulting in the aggregation of extensive fronthaul traffic containing data characterized by both busy and silent periods. Consequently, this leads to on-off processes with heavy-tailed on-periods or off-periods.

<span id="page-8-5"></span><span id="page-8-4"></span>The accumulation of a large number of on-off processes with heavily tailed on-periods and off-periods results in longrange dependency [33]. Reference [34] further confirms the presence of long-range dependence in backhaul traffic of LTE and LTE-advanced base stations. Since Option 7.3 split fronthaul traffic exhibits similar characteristics to backhaul traffic due to its dependence on user demand and activity, the Poisson-Pareto burst process (PPBP), a popular synthetic traffic generator that builds a long-range dependent arrival process and emulates the statistical behavior of real-world network traffic [35], can be used to model the traffic in this scenario. While this model effectively captures the burstiness and long-range dependence of traffic in Option 7.3, it is a simplification of the potential dynamic variations that could arise in eCPRI-based fronthaul. Future work will explore more comprehensive traffic models to account for the dynamic behavior of eCPRI.

#### <span id="page-8-8"></span><span id="page-8-6"></span>V. NUMERICAL SIMULATION

# <span id="page-8-0"></span>A. XGS-PON Based C-RAN Simulation Module (XCRAN-SIMMODULE)

We have developed an XGS-PON-based C-RAN simulation module named xCRAN-SIMMODULE<sup>2</sup> using the OMNeT++ network simulator [37]. Through multiple simulations, we compared the performance of our proposed *TP-ERBU* algorithm with that of the *gGIANT* [12] and *Optimized RR* [13] DBA algorithms. These algorithms are chosen because they represent two different optimization strategies commonly used in PON-based fronthaul networks. *gGIANT* prioritizes latency reduction by improving grant scheduling efficiency, while *Optimized RR enhances* upstream bandwidth utilization by dynamically reallocating bandwidth among ONUs. Since TP-ERBU is designed to jointly optimize both delay and throughput, comparing it against these two approaches provides a comprehensive assessment of its effectiveness in XGS-PON-based 5G C-RAN fronthaul.

In our simulation setup, we configured a C-RAN fronthaul network comprising 16 RRHs (each configured with

<span id="page-8-7"></span><span id="page-8-1"></span><sup>&</sup>lt;sup>2</sup>The source code for the XCRAN-SIMMODULE used in our simulations is available at [36].

![](_page_9_Figure_2.jpeg)

Fig. 6. Simulation scenario of XCRAN-SIMMODULE.

<span id="page-9-1"></span>TABLE II TRAFFIC GENERATION PARAMETERS [\[13\]](#page-12-12), [\[32\]](#page-13-3)

| Parameters                          | Details |
|-------------------------------------|---------|
| Traffic generation model            | PPBP    |
| Traffic type                        | Bursty  |
| Mean burst time length              | 2ms     |
| Maximum number packets/burst        | 5000    |
| Minimum number packets/burst        | 1       |
| Hurst parameter                     | 0.8     |
| Pareto shape parameter (ON-Period)  | 1.4     |
| Pareto shape parameter (OFF-Period) | 1.2     |
| Packet size                         | 1470B   |

20 MHz bandwidth, three sectors, and four antennas) connected to 16 ONUs. For this network configuration, each RRH required 1.075 Gbps fronthaul capacity for Option 7.2 split and 0.67 Gbps for Option 7.3 split (refer to Table [I\)](#page-4-1). We excluded Option 7.1 from our investigation due to its fronthaul capacity requirement of 4.3 Gbps per RRH, exceeding the capability of XGS-PON. Each ONU was equipped with a single T-CONT featuring an assured bandwidth type (i.e., T-CONT-2), with the maximum size of the T-CONT-2 queue buffer set to 1 MB. To approximate a fronthaul distance of 10 km, we selected a round-trip propagation delay (RTT) of 120s. It's worth noting that for a fronthaul distance of 10 km, the RTT is typically 100s, with the remaining 20s allocated as a delay margin to accommodate processing delays from OLT/ONU and other fronthaul elements.

We inject PPBP traffic into each ONU in order to generate C-RAN fronthaul uplink traffic (parameters are mentioned in Table [II\)](#page-9-0). The maximum data transfer rate for the PPBP traffic source is set to 8.928 Gbps (during ON-period) enabling us to

<span id="page-9-2"></span>TABLE III DBA SIMULATION PARAMETERS AND SYSTEM CONFIGURATION

<span id="page-9-0"></span>

| Description                   | Details                   |  |
|-------------------------------|---------------------------|--|
| Number of RRHs (ONUs)         | 16                        |  |
| T-CONT Max Allocation Size    | 9.72kB                    |  |
| T-CONT Max Service Interval   | 4 Frames                  |  |
| Bandwidth per T-CONT (gGIANT) | 621 Mbps                  |  |
| T-CONT per ONU                | 1                         |  |
| Propagation Delay             | 120μs (RTT)               |  |
| T-CONT Buffer Size            | 1 MB                      |  |
| Maximum Polling Interval      | 125μs                     |  |
| Operating System              | Ubuntu 20.04 LTS          |  |
| Processor                     | Intel(R) Core i9 @3.70GHz |  |
| Memory                        | 128 GB                    |  |
| Compiler                      | gcc                       |  |
| Simulation Environment        | OMNeT++ 5.6.2             |  |
| Mobility Model                | None                      |  |
| Simulation Style              | Cmdenv-express-mode       |  |
| Simulation Script             | Cmdenv, Tcl/Tkenv         |  |
| Simulation time               | 100s                      |  |

use 90% of the total upstream capacity and reserve the remainder for network management and protection. Figure [6](#page-9-1) shows the snapshot of XCRAN-SIMMODULE during simulation on OMNeT++ network simulator. Table [III](#page-9-2) describes the DBA simulation parameters and system configuration that we use in our simulation.

### *B. Simulation Results*

*1) Mean Upstream Packet Delay:* The mean upstream delay performance of all three DBA algorithms for Option 7.2 and Option 7.3 splits is illustrated in Figure [7.](#page-10-0) Across both split options, TP-ERBU demonstrates the lowest upstream

![](_page_10_Figure_2.jpeg)

<span id="page-10-0"></span>Fig. 7. Mean upstream delay performance of gGAINT [\[12\]](#page-12-11), Optimized RR [\[13\]](#page-12-12) and TP-ERBU for (a) Option 7.2 and (b) Option 7.3 splits.

delay, followed by Optimized RR and gGIANT. This improvement in performance can be attributed to the traffic prediction mechanism and the efficient utilization of XGS-PON upstream capacity offered by TP-ERBU compared to the other two DBAs. In the case of Option 7.3 split, TP-ERBU meets the fronthaul latency requirement of 300 microseconds up to a traffic load factor of 0.8, whereas Optimized RR and gGIANT only satisfy this requirement up to traffic load factors of 0.6 and 0.4, respectively. Similarly, for Option 7.2 split, TP-ERBU fulfills the fronthaul delay requirement of 300 microseconds up to a traffic load factor of 0.5, while Optimized RR and gGIANT achieve this only up to traffic load factors of 0.3 and 0.2, respectively. The TP-ERBU algorithm achieves a 34.95% reduction in packet delay compared to the gGiant algorithm and a 20.59% reduction compared to the Optimized RR algorithm.

*2) Packet Loss Ratio:* Figure [8](#page-10-1) illustrates the packet loss ratio of all three DBA algorithms for both split options. Packet loss is reduced upto by 40.00% with TP-ERBU, compared to gGiant, and by 25.00% compared to Optimized RR. This superiority can be attributed to TP-ERBU's ability to mitigate network congestion by predicting and transmitting future traffic within the current grant, even if it was not reported to the OLT in earlier report frames. Moreover, TP-ERBU facilitates T-CONTs to transmit data through dynamic

![](_page_10_Figure_6.jpeg)

<span id="page-10-1"></span>Fig. 8. Packet loss ratio comparison of gGIANT [\[12\]](#page-12-11), Optimized RR [\[13\]](#page-12-12) and TP-ERBU for (a) Option 7.2 and (b) Option 7.3 splits.

transmission windows, thereby efficiently utilizing the unused bandwidth of the ONU/T-CONT. It's worth noting that in Figure [8\(](#page-10-1)a), results are displayed up to a traffic load factor of 0.7 since beyond this load, the packet loss ratio for all three algorithms exceeds the acceptable limit.

*3) Throughput Analysis:* Figure [9](#page-11-1) presents a comparison of the average throughput (in Gbps) achieved by each DBA algorithm for Option 7.3 functional split. It is evident from the graph that throughput increases upto by 30.00% compared to gGiant and by 15.56% compared to Optimized RR. This result stems from the traffic prediction approach adopted by TP-ERBU, which allows it to utilize the available capacity of upstream frames during each allocation cycle. The difference in throughput between TP-ERBU and the other algorithms varies: it is minimal when the ONU load factor is 0.25, moderate at 0.5, and substantial at 1. This variation is due to the differing amounts of traffic handled by the majority of ONUs under low, moderate, and high loads, respectively. Moreover, the likelihood of an ONU buffer becoming overloaded significantly increases under higher load factors, highlighting the effectiveness of our algorithm in such scenarios.

*4) Jitter:* The performance comparison of jitter obtained by TP-ERBU versus gGIANT and Optimized RR for Option 7.3 functional split is depicted in Figure [10.](#page-11-2) Jitter is reduced

![](_page_11_Figure_2.jpeg)

Fig. 9. Average throughput achieved by TP-ERBU compared to gGIANT and Optimized RR for Option 7.3 functional split with different RRH traffic load factors.

<span id="page-11-1"></span>![](_page_11_Figure_4.jpeg)

<span id="page-11-2"></span>Fig. 10. Achieved jitter in TP-ERBU versus gGIANT and Optimized RR.

upto by 21.43% compared to gGiant and by 5.71% compared to Optimized RR. This superiority can be attributed to the fact that packet jitter is primarily influenced by network congestion, causing the delay between consecutive received packets to fluctuate rather than remain constant. Additionally, the plot illustrates that packet jitter increases proportionally with network congestion.

*5) Upstream Channel Utilization:* Figure [11](#page-11-3) illustrates the percentage improvement in upstream channel utilization contributed by TP-ERBU over gGAINT and Optimized RR, respectively. As expected, TP-ERBU significantly enhances upstream channel utilization compared to the other two algorithms. However, the improvement becomes more pronounced at higher traffic load factors, as the network experiences less congestion at lower loads, and all three algorithms efficiently handle the traffic with the available XGS-PON capacity. The highest improvement achieved by TP-ERBU compared to gGIANT and Optimized RR is 9.28% and 3.92%, respectively, for a traffic load factor of 1.

### <span id="page-11-0"></span>*C. Comparison With ML-Based Methods*

To quantify the trade-offs between the proposed movingaverage-based approach and ML-based methods, we conducted an experimental comparison using a deep learning-based traffic prediction model similar to the one proposed in [\[19\]](#page-12-19). The

![](_page_11_Figure_10.jpeg)

<span id="page-11-3"></span>Fig. 11. Percentage improvement in upstream channel utilization in TP-ERBU against gGIANT and Optimized RR.

<span id="page-11-4"></span>TABLE IV COMPARISON OF TP-ERBU WITH ML-BASED METHOD [\[19\]](#page-12-19)

| Metric                   | TP-ERBU | ML-Based | Improvement |
|--------------------------|---------|----------|-------------|
| Prediction Time (ms)     | 0.01    | 0.15     | 93.33%      |
| Packet Delay (ms)        | 0.25    | 0.28     | 10.71%      |
| Throughput (Gbps)        | 8.5     | 8.4      | 1.19%       |
| Computational Complexity | O(N)    | $O(N^2)$ | -           |

ML-based model was implemented using TensorFlow and trained on the same dataset used for the TP-ERBU simulations. The model was deployed on a GPU (NVIDIA RTX 3090) to ensure optimal performance.

As shown in Table [IV,](#page-11-4) the proposed TP-ERBU algorithm outperforms the ML-based method in terms of prediction time, packet delay, and throughput. Specifically, TP-ERBU achieves a 93.33% reduction in prediction time, a 10.71% reduction in packet delay, and a 1.19% improvement in throughput compared to the ML-based approach. Moreover, the computational complexity of TP-ERBU is significantly lower (*O*(*N* )) than that of the ML-based method (*O*(*N* <sup>2</sup>)), making it more suitable for real-time deployment in lowlatency fronthaul networks.

### *D. Validity and Reproducibility*

While our simulation results follow established practices and are validated through extensive experimentation, certain assumptions in the setup–such as network parameters, traffic models, and configurations–may differ in real-world deployments. Although these variations could impact specific performance metrics, the overall benefits of TP-ERBU in traffic prediction and dynamic bandwidth allocation remain valid.

To ensure reproducibility, we have publicly shared the **XCRAN-SimModule** source code at [\[36\]](#page-13-8), enabling researchers to replicate our experiments. Additionally, all simulation parameters and configurations are documented in the manuscript for exact replication.

### VI. CONCLUSION

<span id="page-12-13"></span>In this paper, we proposed a novel Dynamic Bandwidth Allocation (DBA) algorithm called Traffic Prediction-based Enhanced Residual Bandwidth Utilization (TP-ERBU) for XGS-PON-based 5G C-RAN fronthaul networks, particularly focusing on Option 7.x functional splits. The key contribution of TP-ERBU is its integration of an advanced traffic prediction mechanism, which accurately forecasts future ONU traffic, with a dynamic residual bandwidth reallocation scheme that ensures efficient bandwidth utilization and reduced latency. The TP-ERBU algorithm not only optimizes the upstream traffic scheduling but also addresses the challenges associated with low-latency mobile fronthaul over time-division multiplexed (TDM) PONs. Our extensive simulation results, using the custom-built XGS-PON-based C-RAN simulation module (XCRAN-SimModule), demonstrate that TP-ERBU outperforms existing DBA algorithms such as gGIANT and Optimized RR in various performance metrics, including a 20.59% reduction in packet delay, a 38.33% improvement in upstream channel utilization, a 25.00% reduction in packet loss, a 5.71% improvement in jitter, and a 15.56% increase in throughput. These improvements make TP-ERBU highly suitable for the stringent latency and bandwidth requirements of 5G C-RAN.

In addition to our ongoing work, there are several potential research directions to explore in the field of dynamic bandwidth allocation for 5G fronthaul. Future studies could investigate the real-world deployment of the proposed TP-ERBU algorithm in 5G networks and evaluate its performance in live environments. Moreover, the algorithm's adaptability to other fronthaul technologies, such as eCPRI, and its impact on bandwidth requirements could be explored. Researchers could also explore integrating more advanced machine learning techniques for traffic prediction and bandwidth optimization, which may lead to further improvements in network performance.

# REFERENCES

<span id="page-12-0"></span>[\[1\]](#page-0-0) M. Ahsan, A. Ahmed, A. Al-Dweik, and A. Ahmad, "Functional split-aware optimal BBU placement for 5G cloud-RAN over WDM access/aggregation network," *IEEE Syst. J.*, 2022.

- <span id="page-12-1"></span>[\[2\]](#page-0-0) A. Younis, T. X. Tran, and D. Pompili, "Energy-efficient resource allocation in C-RANs with capacity-limited Fronthaul," *IEEE Trans. Mobile Comput.*, vol. 20, no. 2, pp. 473–487, 2021.
- <span id="page-12-2"></span>[\[3\]](#page-0-1) R. Guerra-Gómez, S. Ruiz-Boqué, M. García-Lozano, and U. Saeed, "Energy and cost footprint reduction for 5G and beyond with flexible radio access network," *IEEE Access*, vol. 9, pp. 142179–142194, 2021.
- <span id="page-12-3"></span>[\[4\]](#page-0-2) N. Panwar, S. Sharma, and A. Singh, "Evolution of RAN architecture: From Centralized to Virtualized and open RAN," *IEEE Wireless Commun.*, vol. 29, no. 3, pp. 58–66, 2022.
- <span id="page-12-4"></span>[\[5\]](#page-0-3) A. De la Oliva, J. A. Hernandez, D. Larrabeiti, and A. Azcorra, "An overview of the CPRI specification and its application to C-RAN-based LTE scenarios," *IEEE Commun. Mag.*, vol. 54, no. 2, pp. 152–159, 2016.
- <span id="page-12-5"></span>[\[6\]](#page-0-4) J. S. Zou, S. A. Sasu, M. Lawin, A. Dochhan, J.-P. Elbers, and M. Eiselt, "Advanced optical access technologies for next-generation (5G) mobile networks," *J. Opt. Commun. Netw.*, vol. 12, no. 10, pp. D86–D98, 2020.
- <span id="page-12-6"></span>[\[7\]](#page-0-5) F. Council, "FTTH council report: The economics of point-to-point fiber networks," *FTTH Council Rep.*, 2022.
- <span id="page-12-7"></span>[\[8\]](#page-0-5) I. S. Association, "IEEE report on fiber transceivers and cost comparison in network deployments," *IEEE Commun. Mag.*, 2022.
- <span id="page-12-8"></span>[\[9\]](#page-0-6) M. S. Akhtar, P. Biswas, A. Adhya, and S. Majhi, "Cost-efficient mobile Backhaul network design over TWDM-PON," in *Proc. IEEE Int. Conf. Adv. Netw. Telecommun. Syst. (ANTS)*, 2020, pp. 1–6.
- <span id="page-12-9"></span>[\[10\]](#page-0-6) M. S. Akhtar, P. Biswas, and A. Adhya, "An ILP-based CapEx and OpEx efficient multi-stage TDM/TWDM PON design methodology," *Opt. Fiber Technol.*, vol. 46, pp. 205–214, 2018.
- <span id="page-12-10"></span>[\[11\]](#page-1-1) Z. Qi-yu, L. Bin, and W. Run-ze, "A dynamic bandwidth allocation scheme for GPON based on traffic prediction," in *Proc. 9th Int. Conf. Fuzzy Syst. Knowl. Discovery*. IEEE, pp. 2043–2046.
- <span id="page-12-11"></span>[\[12\]](#page-1-2) P. Alvarez, N. Marchetti, D. Payne, and M. Ruffini, "Backhauling mobile systems with XG-PON using grouped assured bandwidth," in *Proc. 19th Eur. Conf. Netw. Opt. Commun.-(NOC)*. IEEE, 2014, pp. 91–96.
- <span id="page-12-12"></span>[\[13\]](#page-1-3) A. M. Mikaeil, W. Hu, T. Ye, and S. B. Hussain, "Performance evaluation of XG-PON based mobile front-haul transport in cloud-RAN architecture," *J. Opt. Commun. Netw.*, vol. 9, no. 11, pp. 984–994, 2017.
- <span id="page-12-14"></span>[\[14\]](#page-2-1) ITU-T G.Sup66, "5G wireless Fronthaul requirements in a PON context," Tech. Rep., 2019.
- <span id="page-12-15"></span>[\[15\]](#page-2-1) J. S. Wey, Y. Luo, and T. Pfeiffer, "5G wireless transport in a PON context: An overview," *IEEE Commun. Standards Mag.*, vol. 4, no. 1, pp. 50–56, 2020.
- <span id="page-12-16"></span>[\[16\]](#page-2-2) N. Shibata et al., "Performance evaluation of mobile front-haul employing ethernet-based TDM-PON with IQ data compression," *J. Opt. Commun. Netw.*, vol. 7, no. 11, pp. B16–B22, 2015.
- <span id="page-12-17"></span>[\[17\]](#page-2-3) J. A. Arokkiam, X. Wu, K. N. Brown, and C. J. Sreenan, "Experimental evaluation of TCP performance over 10Gb/s passive optical networks (XG-PON)," in *Proc. IEEE global Commun. Conf.*. IEEE, 2014, pp. 2223–2228.
- <span id="page-12-18"></span>[\[18\]](#page-2-4) C. A. Kyriakopoulos and G. I. Papadimitriou, "Predicting and allocating bandwidth in the optical access architecture XG-PON," *Opt. Switching Netw.*, vol. 25, pp. 91–99, 2017.
- <span id="page-12-19"></span>[\[19\]](#page-2-5) S. Singh, A. Kumar, and P. Sharma, "Machine learning-based dynamic bandwidth allocation algorithm for XGS-PON," *J. Opt. Commun. Netw.*, vol. 15, no. 1, pp. 1–12, 2023.
- <span id="page-12-20"></span>[\[20\]](#page-2-6) X. Zhang, Y. Li, Z. Wang, and M. Chen, "Deep learning-based traffic prediction and resource allocation for 5G fronthaul networks," *IEEE Trans. Veh. Technol.*, vol. 71, no. 1, pp. 813–825, 2022.
- <span id="page-12-21"></span>[\[21\]](#page-3-3) J. Wang, X. Liu, Y. Zhao, and H. Zhang, "Dynamic resource allocation in optical access networks using reinforcement learning," *J. Lightw. Technol.*, vol. 41, no. 1, pp. 207–218, 2023.
- <span id="page-12-22"></span>[\[22\]](#page-3-4) M. Peng, Y. Sun, X. Li, Z. Mao, and C. Wang, "Recent advances in cloud radio access networks: System architectures, key techniques, and open issues," *IEEE Commun. Surveys Tuts.*, vol. 18, no. 3, pp. 2282–2308, 2016.
- <span id="page-12-23"></span>[\[23\]](#page-3-4) K. Chen and R. Duan, "C-RAN the road towards green RAN. white paper," *China Mobile Res. Inst., Tech. Rep*, 2011.
- <span id="page-12-24"></span>[\[24\]](#page-4-5) J. Wu, Z. Zhang, Y. Hong, and Y. Wen, "Cloud radio access network (C-RAN): A primer," *IEEE Netw.*, vol. 29, no. 1, pp. 35–41, 2015.
- <span id="page-12-25"></span>[\[25\]](#page-4-6) H. S. Abbas and M. A. Gregory, "The next generation of passive optical networks: A review," *J. Netw. Comput. Appl.*, vol. 67, pp. 53–74, 2016.
- <span id="page-12-26"></span>[\[26\]](#page-5-1) 3GPP, "Study on new radio access technology: Radio access architecture and interfaces (release 14)," 3rd Generation Partnership Project (3GPP), Tech. Rep., 2017.
- <span id="page-12-27"></span>[\[27\]](#page-5-2) ITU-T, *ITU-T G.9807.1: 10-Gigabit-capable symmetric passive optical network (XGS-PON)*, Std., 2016.
- <span id="page-12-28"></span>[\[28\]](#page-5-3) J. Doe and A. Smith, "Fronthaul bandwidth estimation for 5G C-RAN under functional splits," *IEEE Trans. Commun.*, vol. 69, no. 5, pp. 3120–3132, 2021.

- <span id="page-13-0"></span>[\[29\]](#page-6-4) J. Smith and H. Chen, "Impact of XGS-PON latency in 5G Fronthaul networks," *J. Opt. Commun.*, vol. 30, no. 2, pp. 45–53, 2022.
- <span id="page-13-1"></span>[\[30\]](#page-6-5) S. Kim and Y. Zhao, "Predictive models for traffic in dynamic optical networks," *IEEE Trans. Netw. Manage.*, 2022.
- <span id="page-13-2"></span>[\[31\]](#page-8-2) N. Alliance, "Further study on critical C-RAN technologies," *Next Gener. Mobile Netw.*, 2015.
- <span id="page-13-3"></span>[\[32\]](#page-8-3) Y. Zhou, R. Li, Z. Zhao, X. Zhou, and H. Zhang, "On the α-stable distribution of base stations in cellular networks," *IEEE Commun. Lett.*, vol. 19, no. 10, pp. 1750–1753, 2015.
- <span id="page-13-4"></span>[\[33\]](#page-8-4) X. Liu and J. S. Baras, "Aggregation of heavy-tailed on-off flows is multifractal," in *Proc. 8th Int. Conf. Commun. Syst., 2002. ICCS 2002.*, vol. 1. IEEE, 2002, pp. 578–582.
- <span id="page-13-5"></span>[\[34\]](#page-8-5) R. K. Polaganga and Q. Liang, "Self-similarity and modeling of LTE/LTE-a data traffic," *Measurement*, vol. 75, pp. 218–229, 2015.
- <span id="page-13-6"></span>[\[35\]](#page-8-6) D. Ammar, T. Begin, and I. Guerin-Lassous, "A new tool for generating realistic internet traffic in ns-3," in *Proc. 4th Int. ICST Conf. Simul. Tools Techn.*, 2012.
- <span id="page-13-8"></span>[\[36\]](#page-8-7) S. Akhtar, "XCRAN-SIMMODULE: A simulation module for C-RAN networks," 2024, gitHub repository. [Online]. Available: https://github. com/shahbazpce/XCRAN-SIMMODULE.git
- <span id="page-13-7"></span>[\[37\]](#page-8-8) A. Varga, "OMNeT++," in *Modeling and Tools for Network Simulation*, Springer, 2010, pp. 35–59.

![](_page_13_Picture_11.jpeg)

**Mohit Kumar** received the Bachelor of Engineering degree in electronics and communication engineering from Rajiv Gandhi Technical University, Bhopal, India, in 2013, the M.Tech. degree in electronics and communication engineering from the Indian Institute of Technology, Bhubaneswar, India, in 2016, and the Ph.D. degree in image processing from the National Institute of Technology at Patna, Patna. From 2018 to 2022, he served as an Assistant Professor with the Department of Electronics and Communication Engineering, Muzaffarpur Institute

of Technology, Muzaffarpur. Since January 2023, he has been working as an Assistant Professor with the Department of Electronics and Communication Engineering, Purnea College of Engineering, Purnea, under the Department of Science, Technology and Technical Education, Government of Bihar, India. His research interests include image processing, pattern recognition, and soft computing.

![](_page_13_Picture_14.jpeg)

**Md Iftekhar Alam** received the B.Tech. degree in electronics and communication engineering from the MIT Muzaffarpur, Baba Saheb Bhimrao Ambedkar Bihar University, India, in 2010, and the M.Tech. degree in electronics and communication engineering with a specialization in communication from the B.I.T.M Santiniketan, West Bengal University of Technology, India, in 2014. He is currently an Assistant Professor with the Department of Electronics and Communication Engineering, Purnea College of Engineering, Purnea, India. His

research interests include wireless communication and networking, softwaredefined networks, and network virtualization.

![](_page_13_Picture_17.jpeg)

**Md Shahbaz Akhtar** received the B.Tech. degree in electronics and communication engineering from NSUT East Campus (formerly AIACT&R), New Delhi, India, in 2013, the M.Tech. degree from the Indian Institute of Technology (IIT) Dhanbad, India, in 2015, and the Ph.D. degree from the Department of Electrical Engineering, IIT Patna, India, in 2021. He is currently an Assistant Professor with the Department of Electronics and Communication Engineering, Purnea College of Engineering, Purnea, India. He has also completed postdoctoral research

with IIT Madras and IIT Kharagpur. His research interests include computer communication and networks, mobile communications, survivable and energyefficient next-generation passive optical networks, and hybrid wireless–optical access networks.

![](_page_13_Picture_20.jpeg)

**Aneek Adhya** (Senior Member, IEEE) received the B.Tech. degree in electronics and communication engineering from the Kalyani Government Engineering College, Kalyani, India, in 2001, the M.Tech. degree in optics and optoelectronics from the University College of Science and Technology, University of Calcutta, Calcutta, India, in 2003, and the Ph.D. degree from the Electronics and Electrical Communication Engineering Department, Indian Institute of Technology (IIT) Kharagpur, Kharagpur, India, in 2009, where he is currently

serving as an Associate Professor with the G.S. Sanyal School of Telecommunication. Before that, he also served as an Assistant Professor with the Electrical Engineering Department, IIT Patna and the G.S. Sanyal School of Telecommunication, IIT Kharagpur. His research interests include 5G/6G networks, optical networks, artificial intelligence, and hybrid wireless-optical access networks.
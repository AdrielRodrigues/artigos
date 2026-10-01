---
title: "Decentralized Optimization of Spectral Efficiency for Scalable CF-RAN With Network-Assisted Free-Duplex"
tema_principal: fl_ran
temas_relacionados: []
ano: 2026
autores: []
veiculo: null
pdf: ../pdf/decentralized_optimization_of_spectral_efficiency_for_scalable_cf-ran_with_network-assisted_free-duplex.pdf
---

# Decentralized Optimization of Spectral Efficiency for Scalable CF-RAN With Network-Assisted Free-Duplex

Xinjiang Xi[a](https://orcid.org/0000-0003-3326-8022) , *Member, IEEE*, Yuhang Sun, Yunxiang Guo [,](https://orcid.org/0000-0001-8158-1684) *Graduate Student Member, IEEE*, Wenqi Zhao, Zhihao Gu [,](https://orcid.org/0009-0002-4456-0846) Xinyu Wang, Dongming Wan[g](https://orcid.org/0000-0003-2762-6567) , *Member, IEEE*, Jiangzhou Wang [,](https://orcid.org/0000-0003-0881-3594) *Fellow, IEEE*, and Xiaohu You [,](https://orcid.org/0000-0002-0809-8511) *Fellow, IEEE*

*Abstract*—Cell-free radio access networks (CF-RANs) with network-assisted free-duplex (NA-FD) architecture unify flexibleduplex, hybrid-duplex, and full-duplex operations, but the coupled uplink/downlink interference and centralized processing impose substantial computational and signaling burdens. To address these challenges, this paper studies distributed transceiver design and access point (AP) duplex mode selection under edge distributed unit (EDU)-level information constraints and per-AP power limitations. We develop a partial distributed block coordinate descent (PDBCD) algorithm that decomposes the original sum-rate maximization into three tractable subproblems and iteratively approximates MMSE performance. The proposed design fully leverages EDU computing resources, reducing the computation load at the cloud computing unit (CCU), and significantly lowering fronthaul signaling overhead through an adaptive inter-EDU information sharing mechanism. Furthermore, by integrating a low-complexity greedy search for duplex mode assignment, the algorithm effectively mitigates cross-link interference (CLI) in NA-FD systems. Simulation results show that the proposed scheme improves spectral efficiency compared with conventional duplex mode, and centralized/distributed MMSE baselines, while maintaining strong scalability under practical deployment constraints.

Received 9 July 2025; revised 16 December 2025; accepted 1 February 2026. Date of publication 10 February 2026; date of current version 19 February 2026. This work was supported in part by the National Natural Science Foundation of China (NSFC) under Grant 62371346, in part by Major Science and Technology Project of Jiangsu Province under Grant BG2024002. The associate editor coordinating the review of this article and approving it for publication was D. Mishra. *(Corresponding authors: Dongming Wang; Yunxiang Guo; Zhihao Gu.)*

Xinjiang Xia is with Purple Mountain Laboratories, Nanjing 211111, China (e-mail: xinjiang xia@aa.seu.edu.cn).

Yuhang Sun is with the School of Telecommunications and Information Engineering, Nanjing University of Posts and Telecommunications, Nanjing 210003, China (e-mail: b22012717@njupt.edu.cn).

Yunxiang Guo is with the School of Electronic Information, Luoyang Institute of Science and Technology, Luoyang 471023, China (e-mail: ieguoyunxiang@seu.edu.cn).

Wenqi Zhao and Xinyu Wang are with the National Mobile Communications Research Laboratory, Southeast University, Nanjing 210096, China (e-mail: 220231215@seu.edu.cn; 220231227@seu.edu.cn).

Zhihao Gu is with Huawei Technologies Company Ltd., Shanghai 200120, China (e-mail: 220221051@seu.edu.cn).

Dongming Wang, Jiangzhou Wang, and Xiaohu You are with the National Mobile Communications Research Laboratory, Southeast University, Nanjing 210096, China, and also with Purple Mountain Laboratories, Nanjing 211111, China (e-mail: wangdm@seu.edu.cn; j.z.wang@kent.ac.uk; xhyu@seu.edu.cn).

Digital Object Identifier 10.1109/TCOMM.2026.3663503

*Index Terms*—Cell-free radio access network, networkassisted free-duplex, partial distributed block coordinate descent, resource allocation, transceiver design.

#### <span id="page-0-2"></span><span id="page-0-1"></span>I. INTRODUCTION

<span id="page-0-0"></span>T O MEET the rapid growth of data services, wireless transmission continues to evolve, leading to the upgrading of mobile communication standards. The requirements for technical indicators of future mobile communication standards will be orders of magnitude higher than those of current standards [\[1\],](#page-14-0) [\[2\],](#page-14-1) which obviously exceeds the capabilities of existing technical frameworks and network architectures. Therefore, it is necessary to explore innovative key technologies and networking methods. This approach, while increasing network capacity, introduces significant inter-cell interference and elevates handover frequency, consequently exacerbating data congestion at cell edges. References [\[3\],](#page-14-2) [\[4\],](#page-14-3) [\[5\],](#page-14-4) [\[6\]](#page-14-5) pioneered the CF-mMIMO architecture, which mitigates the inherent boundary effects of cellular systems by eliminating traditional cell boundaries. In CF-mMIMO networks, a large number of APs are deployed throughout the coverage area, with all APs interconnected via fronthaul links and operating on identical time-frequency resources. By introducing overlapping service areas that eliminate the concept of cell boundaries, CF-mMIMO ensures consistent quality of service (QoS) across the entire coverage region.

<span id="page-0-9"></span><span id="page-0-8"></span><span id="page-0-7"></span><span id="page-0-6"></span><span id="page-0-5"></span><span id="page-0-4"></span><span id="page-0-3"></span>Traditional wireless communication systems typically operate in half-duplex (HD) mode, employing dedicated channels for bidirectional end-to-end transmission [\[7\].](#page-14-6) In HD systems, transceivers work in non-overlapping time slots or frequency bands, known as time division duplexing (TDD) or frequency division duplexing (FDD). While this configuration avoids self-interference (SI) between transmitters and receivers, it results in reduced resource utilization. Next-generation wireless technologies demand higher spectral efficiency [\[8\].](#page-14-7) Full-duplex (FD) communication has emerged as a potential solution, enabling simultaneous transmission and reception on the same time-frequency resource block. Compared to TDD and FDD, the emerging co-time cofrequency full duplex (CCFD) promises to double the ergodic capacity of HD systems [\[9\],](#page-14-8) [\[10\].](#page-14-9) However, CCFD faces a critical challenge in signal integrity: due to the strong coupling

0090-6778 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

between transmit and receive links at FD base stations (BSs), high-power SI signals are generated at the receiver, which can overwhelm the desired signals from remote transmitting antennas [\[11\],](#page-14-10) [\[12\].](#page-14-11)

<span id="page-1-1"></span><span id="page-1-0"></span>In multi-user scenarios, CCFD systems introduce CLI as an additional interference component, significantly complicating the interference environment in full-duplex cellular networks beyond the conventional inter-cell BS-UE and UE-BS interference present in HD systems. The emerging interference components include uplink-downlink UE interference, intercell BS-BS interference and residual self-interference after cancellation. To fully exploit the potential performance gains of CCFD systems, intelligent scheduling algorithms must be implemented to effectively coordinate uplink and downlink UEs with heterogeneous transmission rates and power levels, thereby maximizing the overall network utility while addressing these complex interference challenges [\[13\],](#page-14-12) [\[14\].](#page-14-13)

To more effectively manage CLI and achieve truly flexible duplexing while addressing challenges posed by asymmetric uplink-downlink traffic, references [\[15\],](#page-14-14) [\[16\]](#page-14-15) proposed a network-assisted full-duplex (NAFD) architecture that builds upon the inherent advantages of CF-mMIMO networks by unifying all duplexing modes, where each AP can dynamically operate in FD mode, hybrid-duplex mode, or flexible-duplex mode, enabling simultaneous uplinkdownlink services through real-time configuration according to network conditions. When implementing NAFD via flexibleduplex operation, all APs operate in HD mode as either transmitting APs (TAPs) for downlink or receiving APs (RAPs) for uplink, completely eliminating intra-AP co-channel interference and simplifying transceiver design, while the dedicated uplink/downlink AP specialization in CF-mMIMO networks significantly reduces CLI compared to CCFD systems [\[17\],](#page-14-16) [\[18\].](#page-14-17)

<span id="page-1-13"></span><span id="page-1-12"></span><span id="page-1-11"></span><span id="page-1-10"></span><span id="page-1-9"></span><span id="page-1-8"></span><span id="page-1-7"></span><span id="page-1-6"></span>The CF-mMIMO with NAFD architecture has garnered significant academic attention due to its substantial improvements in both spectral efficiency (SE) and energy efficiency (EE). Reference [\[15\]](#page-14-14) employed deterministic equivalents to analyze the SE of CF-mMIMO with NAFD networks using zero-forcing (ZF) and regularized zero-forcing (RZF) precoding with MMSE receivers. Reference [\[16\]](#page-14-15) developed a beamforming training scheme for inter-AP interference cancellation. Reference [\[19\]](#page-14-18) proposed an optimization framework for transceiver design in large-scale distributed antenna systems with NAFD, maximizing the sum uplink-downlink rate while satisfying QoS and backhaul constraints. However, these studies adopted fixed mode assignment strategies, which inherently limit flexible traffic adaptation and reduce resource utilization efficiency. To address the inherent challenges of CF-mMIMO and fully exploit the flexible duplexing advantages of NAFD, comprehensive considerations must be given to transceiver design, uplink-downlink power control, AP-UE association and AP operation modes [\[20\],](#page-15-0) [\[21\],](#page-15-1) [\[22\],](#page-15-2) [\[23\],](#page-15-3) [\[24\].](#page-15-4) Specifically, Reference [\[20\]](#page-15-0) proposed a dual-layer iterative optimization scheme for secure CF-mMIMO with NAFD systems, where the inner loop utilizes successive convex approximation to obtain optimal secure beamforming, uplink power allocation and receive vectors, while the outer loop employs a quantum-inspired tabu search meta heuristic algorithm to dynamically adjust duplex modes, achieving higher secure SE gains compared to fixed-mode NAFD. However, the aforementioned studies all rely on centralized optimization at CCU, which inevitably incurs substantial computational complexity and backhaul overhead. Such fully centralized processing fails to leverage the inherent advantages of cell-free distributed computing and scalability. This limitation highlights the critical need for further research into scalable distributed processing schemes that can effectively balance performance and operational efficiency in practical deployments.

<span id="page-1-20"></span><span id="page-1-19"></span><span id="page-1-18"></span><span id="page-1-17"></span><span id="page-1-16"></span><span id="page-1-15"></span><span id="page-1-14"></span><span id="page-1-5"></span><span id="page-1-4"></span><span id="page-1-3"></span><span id="page-1-2"></span>To achieve an optimal trade-off between computational complexity and performance in cooperative transmission [\[25\],](#page-15-5) [\[26\],](#page-15-6) [\[27\],](#page-15-7) reference [\[28\]](#page-15-8) proposed a novel CF-RAN architecture that, in contrast to conventional CF-mMIMO systems, partitions physical-layer functionalities into APs, EDUs and user-centric distributed units (UCDU). In this architecture, RRUs are responsible for radio frequency signal transmission/reception and forwarding, the newly introduced EDUs perform distributed precoding and reception across multiple RRUs, while UCDUs handle user data combining and distribution. This innovative framework demonstrates superior cooperative transmission performance even with limited-scale AP deployments [\[28\],](#page-15-8) [\[29\],](#page-15-9) [\[30\].](#page-15-10) Based on the scalability and space-time-frequency resource scheduling capabilities of CF-RAN systems, CF-mMIMO with NAFD architecture has evolved into CF-RAN with NA-FD architecture, in which the concept of full-duplex has evolved into the concept of free-duplex [\[31\].](#page-15-11) Specifically, the CF-RAN with NA-FD architecture has the characteristics of non-overlapping subband full-duplex (SBFD), and AP duplex can be scheduled in spatial, time and frequency to efficiently utilize system resources. In CF-RAN with NA-FD, APs are in duplex modes such as hybrid duplex, flexible duplex and full duplex. The CLI can be reduced by scheduling the duplex mode, beamforming and power control, thereby improving system performance. The CF-RAN with NA-FD architecture also has the characteristics of distributed scalability, which means that more flexible signal processing methods can be used to meet the growing communication capacity requirements, ensure user communication quality, and greatly reduce the computational complexity of processing data and the requirements for system hardware equipment deployment. Despite the aforementioned advances, a critical research gap remains unaddressed: while CF-RAN is inherently designed for scalability, the introduction of NA-FD operation fundamentally challenges this scalability due to the strong uplink-downlink coupling, residual cross-link interference, and substantially increased centralized processing demands. Existing works on CF-mMIMO with NAFD [\[15\],](#page-14-14) [\[16\],](#page-14-15) [\[19\],](#page-14-18) [\[20\]](#page-15-0) predominantly assume either half-duplex operation, flexible-duplex with fixed mode assignment, or fully centralized CSI aggregation at the CCU, thereby circumventing the scalability challenge inherent to NA-FD. Furthermore, prior duplexmode selection studies typically focus on single-cell systems, co-located massive MIMO, or idealized full-duplex architectures without the hierarchical EDU/CCU processing structure

![](_page_2_Figure_2.jpeg)

<span id="page-2-0"></span>Fig. 1. CF-RAN with NA-FD system model.

characteristic of CF-RAN. Consequently, the fundamental question of how to achieve scalable NA-FD operation in CF-RAN architectures—jointly optimizing duplex-mode selection and distributed transceiver design under realistic EDU-level information constraints—remains open. This paper aims to fill this gap by developing a distributed optimization framework that restores scalability to NA-FD CF-RAN while approaching centralized performance. The main contributions of this paper are as follows:

- Establishment of a CF-RAN with NA-FD transmission model that transforms the sum uplink-downlink rate maximization problem into a sum minimum mean square error (MSE) optimization problem by leveraging MMSE-SINR relationships;
- 2) For the sum-rate maximization problem, we propose a parallel distributed block coordinate descent (PDBCD) algorithm that achieves optimal transceiver design, which further introduces an EDU sharing mechanism that dynamically balances signaling overhead and performance through inter-EDU common information sharing, and a polynomial-time greedy search algorithm is developed for optimal duplex mode selection;
- 3) Simulation results demonstrate the superiority of the proposed PDBCD algorithm with greedy search in CF-RAN with NA-FD, outperforming conventional TDD and CCFD schemes, and the proposed algorithm achieves higher performance gains when all EDUs operate in shared mode compared to centralized MMSE solutions.

#### II. SYSTEM MODEL

#### A. CF-RAN With NA-FD Architecture

We propose a CF-RAN with NA-FD system architecture as shown in Fig. 1, where CCU determines the association between EDUs and APs and performs mode selection for APs based on CSI, while EDUs are responsible for uplink data detection and downlink precoding design. In the uplink, EDUs detect the signals received by APs and forward them to CCU via fronthaul links. In the downlink, CCU distributes user data streams to EDUs, which perform precoding processing

![](_page_2_Figure_11.jpeg)

<span id="page-2-1"></span>Fig. 2. Space-time-frequency domain resource allocation for CF-RAN with NA-FD system.

before transmitting the data to downlink UEs through APs via fronthaul links.

In terms of scalability, CF-RAN with NA-FD supports multiple cooperation schemes to mitigate CLI, including partial cooperation, fully distributed cooperation, and fully centralized cooperation. The system can flexibly adjust cooperation strategies to achieve a trade-off between performance and computational complexity. For instance, in sparse-density environments such as suburban areas, full cooperation or partial cooperation can be employed to enhance user quality of service. Conversely, in ultra-dense scenarios like stadiums, the system may adopt distributed downlink precoding generation at APs, partial cooperation among EDUs for uplink decoding vector generation, and coordinated power control through EDU or UCDU cooperation to ensure high-efficiency data processing.

In terms of resource allocation, CF-RAN with NA-FD supports duplex mode selection and scheduling in both time and frequency domains, enabling joint spatial-time-frequency resource allocation and scheduling. As illustrated in Fig. 2, APs and multi-antenna users can flexibly schedule resources across the spatial, time and frequency domains, where NAFD can be regarded as a special case of spatial-domain duplex scheduling at the AP. Unlike static spatial-domain allocation within fixed time-frequency resources, time-domain scheduling must account for system stability and the frequency of uplink/downlink antenna switching. Meanwhile, frequencydomain scheduling supports flexible adaptive duplexing, allowing dynamic reuse of frequency resources for uplink and downlink. By leveraging frequency-division characteristics, it enables CLI cancellation, better aligning with the transmission requirements of practical systems.

We consider a CF-RAN with NA-FD system consists of M APs connected to X EDUs, where each AP is equipped with N antennas, serving K single-antenna downlink UEs and J single-antenna uplink UEs. Let  $\mathcal{X} = \{1,\ldots,X\}$ ,  $\mathcal{M} = \{1,\ldots,M\}$ ,  $\mathcal{J} = \{1,\ldots,J\}$ ,  $\mathcal{K} = \{1,\ldots,K\}$  represent the set of EDU, AP, uplink UE and downlink UE, respectively. Due to the flexibility and scalability of CF-RAN architecture, any EDU x is associated with a variable number of  $M_x$  APs, which can be written as  $M = \sum_{i=1}^{K} M_x$ .

#### B. Channel Model

Assuming all APs are HD devices, and the duplex mode is uniformly scheduled by CCU, which can be flexibly selected to better manage CLI. We denote APs operating in downlink mode as TAPs and those in uplink mode as RAPs, and assume that there are L TAPs and Z RAPs in our system, satisfying M=L+Z, while the number of APs associated with EDU x follows  $M_x=L_x+Z_x$ . The values of L and Z can be dynamically adjusted according to uplink and downlink traffic demands. We define binary mode selection variables  $\mu_{\mathrm{D},m},\mu_{\mathrm{U},m}\in\{0,1\}$ , satisfying  $\mu_{\mathrm{D},m}+\mu_{\mathrm{U},m}=1$ . When  $\mu_{\mathrm{D},m}=1$ , it indicates that AP m is a TAP; otherwise, it is a RAP.

This paper considers a frequency-flat fading channel model, which is appropriate for narrowband transmission or a single subcarrier in OFDM systems. The extension to frequencyselective channels with multi-tap delay profiles is left for future work. For the channel coefficient  $h_{ab}$  between any two antennas a and b, it can be modeled as  $h_{ab} =$  $\sqrt{\beta_{ab}}g_{ab}$ , where  $\beta_{ab}$  is the large-scale fading coefficient,  $g_{ab} \sim \mathcal{CN}(0,1)$  is the small-scale fading coefficient. The channel matrix between all UEs and APs are defined as  $H \in \mathbb{C}^{MN \times (K+J)}$ . According to mode vector  $\mu_{\mathrm{D}} =$  $[\mu_{\mathrm{D},1}\mu_{\mathrm{D},2}\dots\mu_{\mathrm{D},2}]^T\in\mathbb{C}^{M\times 1}$  and  $\boldsymbol{\mu}_{\mathrm{U}}=1-\boldsymbol{\mu}_{\mathrm{D}}$  with select function  $g(\cdot)$ , we can obtain uplink channel between UEs and RAPs  $H_{\rm U} = g(H, \mu_{\rm U})$  and downlink channel between UEs and TAPs which are needed in transceiver design. To facilitate subsequent derivation, some channel composition forms are given, where  $\boldsymbol{H}_{\mathrm{D}} = \begin{bmatrix} \boldsymbol{H}_{\mathrm{D},1}^{\mathrm{H}} & \boldsymbol{H}_{\mathrm{D},2}^{\mathrm{H}} & \dots & \boldsymbol{H}_{\mathrm{D},X}^{\mathrm{H}} \end{bmatrix} \in \mathbb{C}^{NL \times K}, \ \boldsymbol{H}_{\mathrm{U}} = \begin{bmatrix} \boldsymbol{H}_{\mathrm{U},1}^{\mathrm{H}} & \boldsymbol{H}_{\mathrm{U},2}^{\mathrm{H}} & \dots & \boldsymbol{H}_{\mathrm{U},X}^{\mathrm{H}} \end{bmatrix} \in \mathbb{C}^{NZ \times J}, \ \boldsymbol{H}_{\mathrm{D},x} = \begin{bmatrix} \boldsymbol{h}_{\mathrm{D},x1} & \boldsymbol{h}_{\mathrm{D},x2} & \dots & \boldsymbol{h}_{\mathrm{D},xK} \end{bmatrix} \in \mathbb{C}^{NL_x \times K}, \ \boldsymbol{H}_{\mathrm{U},x} = \begin{bmatrix} \boldsymbol{h}_{\mathrm{U},x1} & \boldsymbol{h}_{\mathrm{U},x2} & \dots & \boldsymbol{h}_{\mathrm{U},xJ} \end{bmatrix} \in \mathbb{C}^{NZ_x \times J}. \ \boldsymbol{H}_{\mathrm{D},x} \ \text{ and } \ \boldsymbol{H}_{\mathrm{U},x} \ \text{ rep-}$ resent the channel between TAPs associated with EDU x and downlink UEs and the channel between RAPs associated with EDU x and uplink UEs, respectively. According to the MMSE channel estimation in [32], we assume  $H_{\mathrm{D},x}$  and  $H_{\mathrm{U},x}$  as the corresponding estimated channel,  $H_{\mathrm{D},x}$  and  $H_{\mathrm{U},x}$  as the corresponding estimated error.

#### <span id="page-3-3"></span>C. Downlink Data Transmission Model

In the downlink transmission, the signal received by the k-th downlink UE is

$$y_{D,k} = \sum_{x=1}^{X} \boldsymbol{h}_{D,xk}^{H} \boldsymbol{w}_{xk} s_{D,k} + \sum_{x=1}^{X} \sum_{k' \neq k}^{K} \boldsymbol{h}_{D,xk}^{H} \boldsymbol{w}_{xk'} s_{D,k'} + \sum_{j=1}^{J} h_{IUI,kj} \sqrt{p_{U,j}} s_{U,j} + n_{D,k},$$
(1)

where  $w_{xk}$  represents the precoding vector of the k-th downlink UE at EDU x,  $s_{\mathrm{D},k} \sim \mathcal{CN}\left(0,1\right)$  represents the symbol sent to the k-th downlink UE,  $h_{\mathrm{IUI},kj}$  represents the interference channel between the j-th uplink UE and the k-th downlink UE,  $p_{\mathrm{U},j}$  represents the transmit power of the j-th uplink UE,  $s_{\mathrm{U},j} \sim \mathcal{CN}\left(0,1\right)$  represents the transmit symbol of the j-th uplink UE, and  $n_{\mathrm{D},k} \sim \mathcal{CN}\left(0,\sigma_{\mathrm{D}}^{2}\right)$  represents the additive white Gaussian noise (AWGN) at the k-th downlink

UE. The signal to interference noise ratio (SINR) of the k-th downlink UE is

<span id="page-3-1"></span>
$$\gamma_{\mathrm{D},k} = \frac{\left|\sum\limits_{x=1}^{X} \boldsymbol{h}_{\mathrm{D},xk}^{\mathrm{H}} \boldsymbol{w}_{xk}\right|^{2}}{\sum\limits_{k'\neq k}^{K} \left|\sum\limits_{x=1}^{X} \boldsymbol{h}_{\mathrm{D},xk}^{\mathrm{H}} \boldsymbol{w}_{xk'} s_{\mathrm{D},k'}\right|^{2} + \sum\limits_{j=1}^{J} p_{\mathrm{U},j} |h_{\mathrm{IUI},kj}|^{2} + \sigma_{\mathrm{D}}^{2}}.$$
The corresponding downlink sum-rate is  $R_{\mathrm{D}} = \sum\limits_{k=1}^{K} R_{\mathrm{D},k} = \frac{1}{2} \left(\frac{1}{2} \sum_{k=1}^{K} R_{\mathrm{D},k}\right)$ 

## D. Uplink Data Transmission Model

 $\sum_{K}^{K} \log_2 \left( 1 + \gamma_{D,k} \right)$ 

In the uplink transmission, RAPs receive the uplink UEs transmission signal and forward it to EDUs. At this time, the received signal at EDU x is aggregated into

<span id="page-3-2"></span>
$$\mathbf{y}_{U,x} = \sum_{j'=1}^{J} \mathbf{h}_{U,xj'} \sqrt{p_{U,j'}} s_{U,j'} + \sum_{x'=1}^{X} \sum_{k=1}^{K} \mathbf{H}_{IAI,xx'} \mathbf{w}_{x'k} s_{D,k} + \mathbf{n}_{U,x}$$
(3)

where  $H_{\text{IAI},xx'} \in \mathbb{C}^{NZ_x \times NL_x}$  denotes the interference channel between TAPs associated with EDU x' and RAPs associated with EDU x,  $n_{\text{U},x} \sim \mathcal{CN}\left(\mathbf{0}, \sigma_{\text{U}}^2 I_{NZ_x}\right)$  represents the noise at the receiver. Since EDUs cooperate with each other, EDU x can acquire the downlink signals transmitted by other EDU x'. This enables the reconstruction of inter-AP interference (IAI) signals, thereby effectively suppressing CLI between APs. However, due to inherent channel estimation errors, complete elimination of IAI is infeasible. Taking residual IAI into account, the uplink signal received at EDU x can be expressed as

$$\mathbf{y}_{\text{U},x} = \sum_{j'=1}^{J} \mathbf{h}_{\text{U},xj'} \sqrt{p_{\text{U},j'}} s_{\text{U},j'} 
+ \sum_{x'=1}^{X} \sum_{k=1}^{K} \tilde{\mathbf{H}}_{\text{IAI},xx'} \mathbf{w}_{x'k} s_{\text{D},k} + \mathbf{n}_{\text{U},x},$$
(4)

where  $\tilde{\boldsymbol{H}}_{\mathrm{IAI},xx'} = \boldsymbol{H}_{\mathrm{IAI},xx'} - \hat{\boldsymbol{H}}_{\mathrm{IAI},xx'}$ ,  $\hat{\boldsymbol{H}}_{\mathrm{IAI},xx'}$  is the estimated channel between EDUs,  $\tilde{\boldsymbol{H}}_{\mathrm{IAI},xx'}$  is the estimated error, consistent with the assumptions in [33], the elements in  $\tilde{\boldsymbol{H}}_{\mathrm{IAI},xx'}$  satisfy the Gaussian distribution where  $\operatorname{vec}\left(\tilde{\boldsymbol{H}}_{\mathrm{IAI},xx'}\right) \sim \mathcal{CN}\left(\mathbf{0},\sigma_{\mathrm{IAI},xx'}^2\boldsymbol{I}_{NZ_xL_{x'}}\right)$ ,  $\sigma_{\mathrm{IAI},xx'}^2$  represents the error gain remaining due to non-ideal interference cancellation.

<span id="page-3-0"></span>To detect the transmitted signal of the j-th uplink UE, let  $v_{xj} \in \mathbb{C}^{NZ_x \times 1}$  represent the receiving vector of the j-th uplink UE at EDU x, then the uplink data demodulated at EDU x is

<span id="page-3-4"></span>
$$\hat{s}_{\mathrm{U},xj} = \boldsymbol{v}_{xj}^{H} \left( \sum_{j'=1}^{J} \boldsymbol{h}_{\mathrm{U},xj'} \sqrt{p_{\mathrm{U},j'}} s_{\mathrm{U},j'} \right.$$

$$+ \sum_{x'=1}^{X} \sum_{k=1}^{K} \tilde{\boldsymbol{H}}_{\mathrm{IAI},xx'} \boldsymbol{w}_{x'k} s_{\mathrm{D},k} + \boldsymbol{n}_{x} \right). \tag{5}$$

Finally, the user data demodulated at EDUs is transmitted to CCU and combined with the uplink data of the j-th UE, where

$$\hat{s}_{\text{U},j} = \sum_{x=1}^{X} v_{xj}^{\text{H}} \sum_{j'=1}^{J} \boldsymbol{h}_{\text{U},xj'} \sqrt{p_{\text{U},j'}} s_{\text{U},j'}$$

$$+ \sum_{x=1}^{X} v_{xj}^{\text{H}} \sum_{x'=1}^{X} \sum_{k=1}^{K} \tilde{\boldsymbol{H}}_{\text{IAI},xx'} \boldsymbol{w}_{x'k} s_{\text{D},k} + \sum_{x=1}^{X} v_{xj}^{\text{H}} \boldsymbol{n}.$$
(6)

According to the above equation, the uplink SINR of the j-th UE is

$$\gamma_{\mathrm{U},j} = p_{\mathrm{U},j} \left| \sum_{x=1}^{X} \boldsymbol{v}_{xj}^{H} \boldsymbol{h}_{\mathrm{U},j} \right|^{2} / \left( \sum_{j' \neq j}^{J} p_{\mathrm{U},j'} \left| \sum_{x=1}^{X} \boldsymbol{v}_{xj}^{H} \boldsymbol{h}_{\mathrm{U},j'} \right|^{2} + \sum_{x=1}^{X} \sum_{x'=1}^{X} \sum_{k=1}^{K} \left| \boldsymbol{v}_{xj}^{H} \tilde{\boldsymbol{H}}_{\mathrm{IAI},xx'} \boldsymbol{w}_{x'k} \right|^{2} + \sum_{x=1}^{X} \left\| \boldsymbol{v}_{xj} \right\|^{2} \sigma_{\mathrm{U}}^{2} \right).$$
(7)

The corresponding uplink sum-rate is  $R_{\rm U}=\sum_{j=1}^J R_{{\rm U},j}=\sum_{j=1}^J \log_2{(1+\gamma_{{\rm U},j})}.$ 

#### E. Optimization Model

By comprehensively considering the uplink UE power constraints, TAP transmission power constraints and EDU information exchange constraints, we address the joint uplink-downlink sum-rate maximization problem in our system. Let  $\boldsymbol{w}_{xk} \in \mathbb{C}^{NL_x \times 1}$  denote the precoding vector for the k-th downlink UE at EDU x, and  $\boldsymbol{v}_{xj} \in \mathbb{C}^{NZ_x \times 1}$  denote the receiving vector for the j-th uplink UE at EDU x. In the distributed optimization framework, these vectors are functions of the partial observation information  $\boldsymbol{S}_x$  available at EDU x, denoted as  $\boldsymbol{w}_{xk}\left(\boldsymbol{S}_x\right)$  and  $\boldsymbol{v}_{xj}\left(\boldsymbol{S}_x\right)$ , respectively. The optimization problem is formulated as follows:

$$\max_{S_1} \sum_{k=1}^{K} R_{D,k} + \sum_{j=1}^{J} R_{U,j},$$
 (8a)

s.t. 
$$\boldsymbol{w}_{xk} = \boldsymbol{w}_{xk} \left( \boldsymbol{S}_x \right), \quad \forall x \in \mathcal{X}, \forall k \in \mathcal{K}$$
 (8b)

$$\mathbf{v}_{xj} = \mathbf{v}_{xj} \left( \mathbf{S}_x \right), \quad \forall x \in \mathcal{X}, \forall j \in \mathcal{J}$$
 (8c)

$$S_x = o_x \left( \hat{H}_D, \hat{H}_U \right), \quad \forall x \in \mathcal{X}$$
 (8d)

<span id="page-4-3"></span>
$$\sum_{k=1}^{K} \|\boldsymbol{w}_{lk}\|^2 \le p_{\text{AP}}, \quad \forall l \in \mathcal{L}$$
 (8e)

<span id="page-4-4"></span>
$$0 \le p_{\mathrm{U},j} \le p_{\mathrm{UE}}, \quad \forall j \in \mathcal{J}$$
 (8f)

$$\mu_{D,m}, \mu_{U,m} \in \{0,1\}, \mu_{D,m} + \mu_{U,m} = 1, \quad \forall m \in \mathcal{M}$$
(8g)

Where  $S_1 = \{ \boldsymbol{W}, \boldsymbol{p}_{\text{U}}, \boldsymbol{V}, \boldsymbol{\mu}_{\text{D}}, \boldsymbol{\mu}_{\text{U}} \}$ , (8b), (8c) represent the downlink precoding and uplink receiver obtained by the x-th EDU, which are functions of partial observation information  $\boldsymbol{S}_x$ . In constraint (8d),  $o_x$  (•) is an observation function, which means that for any EDU x, the processing unit can not only obtain the local channel estimation information  $\hat{\boldsymbol{H}}_x$ , including

<span id="page-4-7"></span>the estimated channels of the downlink UE-TAP (associated with EDU x) and the uplink UE-RAP (associated with EDU x), that is,  $\hat{\boldsymbol{H}}_x = \left\{ \hat{\boldsymbol{H}}_{D,x}, \hat{\boldsymbol{H}}_{\mathrm{U},x} \right\}$ , and there may be cooperation between EDUs. EDU x can receive shared information from other EDUs, referred to as sideband information  $S_x$ . When signaling exchange exists between all EDUs in the system,  $S_x = \hat{H}$ . If there is no signaling exchange, the sideband information  $S_x = 0$ , and in this case,  $S_x = H_x$ . (8e) represents the transmit power constraint for each TAP, where  $p_{AP}$  is the AP power threshold. In practical applications, this limits the transmit power of a set of antennas deployed on a single AP, which is more reasonable compared to the system's total power constraint. (8f) represents the uplink UE power constraint, where  $p_{UE}$  is the UE power threshold. (8g) is the AP duplex mode selection constraint, indicating that a single AP can only operate in half-duplex mode. This eliminates the significant self-interference within APs in CCFD.

## <span id="page-4-9"></span><span id="page-4-8"></span>III. DISTRIBUTED TRANSCEIVER DESIGN AND DUPLEX MODE SELECTION

#### A. Problem Transformation

For a given AP duplex mode, we first focus on the distributed transceiver design. To handle the non-convex rate terms, we transform optimization problem (8) using an MSE-based transceiver design approach. Prior works [34], [35] have demonstrated that minimizing the MSE can maximize a tight lower bound of UE achievable rate. When employing MMSE receivers, the MSE-based optimization problem becomes equivalent to the maximum-SINR optimization problem, satisfying the relationship MSE =  $\frac{1}{1+\text{SINR}}$  [36], [37], [38]. Consequently, the rate optimization based on  $\log_2 (1 + \text{SINR})$  can be equivalently reformulated as an MSE-based optimization problem, i.e.,  $-\log_2 (\text{MSE})$ .

<span id="page-4-12"></span><span id="page-4-11"></span><span id="page-4-10"></span><span id="page-4-6"></span><span id="page-4-0"></span>It is worth noting that the rate-to-WMMSE transformation via the MMSE-SINR relationship is a well-established technique in the literature [34], [38]. However, the novelty of our work lies not in this transformation itself, but in the following three aspects that extend beyond existing WMMSEbased frameworks: (i) NA-FD transmission model with joint UL/DL treatment—unlike prior CF-mMIMO studies that consider half-duplex or fixed-mode operation, our formulation incorporates dynamic per-AP duplex mode selection with coupled UL-DL interference management; (ii) Two-layer EDU-TMMSE framework—we introduce serial-parallel EDU-wise distributed updates with an explicit information-sharing policy, ensuring scalability across multiple EDUs while approaching centralized performance; (iii) Greedy duplex-mode selection under imperfect CSI—a low-complexity heuristic is embedded within the optimization loop to adaptively configure UL/DL operation, which has not been addressed in prior WMMSE formulations for CF-RAN systems.

<span id="page-4-5"></span><span id="page-4-2"></span><span id="page-4-1"></span>Next, we use the weighted minimum mean squared error (WMMSE) method to remodel the rate term in (8) [34]. For downlink transmission, we first introduce the scalar receive filter  $u_{D,k}$  for downlink UE k, and calculate the MSE on the downlink received signal in (1) as

$$e_{\mathrm{D},k}\left(u_{\mathrm{D},k},\boldsymbol{W},\boldsymbol{p}_{\mathrm{U}}\right)=\mathbb{E}\left\{\left|s_{\mathrm{D},k}-u_{k}^{*}y_{\mathrm{D},k}\right|^{2}\right\}$$

$$=1+|u_{k}|^{2} \sum_{k'=1}^{K} \left| \sum_{x=1}^{X} \hat{\boldsymbol{h}}_{D,xk}^{H} \boldsymbol{w}_{xk'} \right|^{2} - 2\mathcal{R} \left\{ u_{k}^{*} \sum_{x=1}^{X} \hat{\boldsymbol{h}}_{D,xk}^{H} \boldsymbol{w}_{xk} \right\} + |u_{k}|^{2} \left( \sum_{x=1}^{X} \sum_{k=1}^{K} \boldsymbol{w}_{xk}^{H} \tilde{\boldsymbol{R}}_{D,xk} \boldsymbol{w}_{xk} + \sum_{j=1}^{J} \beta_{IUI,kj} p_{U,j} + \sigma_{D}^{2} \right),$$
(9)

where  $\tilde{\bm{R}}_{\mathrm{D},xk} = \mathbb{E}\left\{\tilde{\bm{h}}_{\mathrm{D},xk} \tilde{\bm{h}}_{\mathrm{D},xk}^{\mathrm{H}}\right\}$  represents the channel estimation error correlation matrix between EDU x and downlink UE k, and  $\beta_{\text{IUI},kj}$  denotes the large-scale fading from uplink UE j to downlink UE k.

For uplink UE j using the receive vector  $v_i$ , the MSE on the uplink demodulated signal in (6) is calculated as

$$e_{\mathrm{U},j}\left(\boldsymbol{v}_{j},\boldsymbol{p}_{\mathrm{U}},\boldsymbol{W}\right) = \mathbb{E}\left\{\left|s_{\mathrm{U},j} - \hat{s}_{\mathrm{U},j}\right|^{2}\right\}$$

$$= 1 + \sum_{j'=1}^{J} p_{\mathrm{U},j'} \mathbb{E}\left\{\left|\sum_{x=1}^{X} \boldsymbol{v}_{xj}^{\mathrm{H}} \boldsymbol{h}_{\mathrm{U},xj'}\right|^{2}\right\}$$

$$- 2\sqrt{p_{\mathrm{U},j}} \mathbb{E}\left\{\sum_{x=1}^{X} \boldsymbol{v}_{xj}^{\mathrm{H}} \boldsymbol{h}_{\mathrm{U},xj}\right\}$$

$$+ \mathbb{E}\left\{\sum_{k=1}^{K} \left|\sum_{x=1}^{X} \sum_{x'=1}^{X} \boldsymbol{v}_{xj}^{\mathrm{H}} \tilde{\boldsymbol{H}}_{\mathrm{IAI},xx'} \boldsymbol{w}_{x'k}\right|^{2}\right\}$$

$$+ \sigma_{\mathrm{U}}^{2} \mathbb{E}\left\{\left\|\sum_{x=1}^{X} \boldsymbol{v}_{xj}\right\|^{2}\right\}. \tag{10}$$

To facilitate the subsequent derivation of Subproblem 1, since the receive vector  $v_i$  is a function of the estimated channel, we first regard it as a random variable, and only the preliminary derivation result is given in (10), which will be derived in detail later.

Finally, auxiliary variables  $\alpha_{\rm D} = [\alpha_{\rm D,1},\ldots,\alpha_{\rm D,K}]^{\rm T}$  and  $\alpha_{\rm U} = [\alpha_{\rm U,1}, \dots, \alpha_{\rm U,J}]^{\rm T}$  are introduced. Using the well-known MSE-SINR relationship, the equivalent problem of (8) is obtained as

$$\min_{\substack{\left\{\boldsymbol{\alpha}_{\mathrm{U}}, \boldsymbol{p}_{\mathrm{U}}, \boldsymbol{V} \right\} \\ \left\{\boldsymbol{\alpha}_{\mathrm{D}}, \boldsymbol{u}_{\mathrm{D}}, \boldsymbol{W} \right\}}} \quad \chi_{\mathrm{D}}\left(\boldsymbol{W}, \boldsymbol{p}_{\mathrm{U}}, \boldsymbol{\alpha}_{\mathrm{D}}, \boldsymbol{u}_{\mathrm{D}} \right) + \chi_{\mathrm{U}}\left(\boldsymbol{W}, \boldsymbol{p}_{\mathrm{U}}, \boldsymbol{V}, \boldsymbol{\alpha}_{\mathrm{U}} \right),$$

s.t. 
$$(8b) - (8f)$$
 (11b)

where

$$\chi_{\mathrm{D}}(\boldsymbol{\alpha}_{\mathrm{D}}, \boldsymbol{u}_{\mathrm{D}}, \boldsymbol{W}, \boldsymbol{p}_{\mathrm{U}})$$

$$= \sum_{k=1}^{K} \alpha_{\mathrm{D},k} e_{\mathrm{D},k} (u_{\mathrm{D},k}, \boldsymbol{W}, \boldsymbol{p}_{\mathrm{U}}) - \log_{2} (\alpha_{\mathrm{D},k}), \qquad (12a)$$

$$\chi_{\mathrm{U}}(\boldsymbol{W}, \boldsymbol{p}_{\mathrm{U}}, \boldsymbol{V}, \boldsymbol{\alpha}_{\mathrm{U}})$$

$$= \sum_{i=1}^{J} \alpha_{\mathrm{U},j} e_{\mathrm{U},j} (\boldsymbol{v}_{j}, \boldsymbol{p}_{\mathrm{U}}, \boldsymbol{W}) - \log_{2} (\alpha_{\mathrm{U},j}). \qquad (12b)$$

In the traditional BCD algorithm, an iterative method is used to optimize each variable one by one while keeping the other variables fixed until convergence [39]. Inspired by this, we decompose the optimization problem (11) into three subproblem blocks and derive closed-form solutions for each

subproblem block, enabling partial distributed computation and significantly improving overall optimization and computational efficiency.

#### <span id="page-5-5"></span>B. Distributed Solution for Subproblem 1

For the given  $\{\bm{\alpha}_{\mathrm{U}}, \bm{p}_{\mathrm{U}}\}$  and  $\{\bm{\alpha}_{\mathrm{D}}, \bm{u}_{\mathrm{D}}, \bm{W}\}$ , the optimal receiver matrix V is obtained by solving the subproblem (13a) in the optimization problem (11):

<span id="page-5-2"></span>
$$\min_{\mathbf{V}} f_1(\mathbf{V}), \qquad (13a)$$

s.t. 
$$(8c), (8d)$$
 (13b)

where  $f_1(\mathbf{V}) = \sum_{j=1}^{J} \alpha_{\mathrm{U},j} e_{\mathrm{U},j}(\mathbf{v}_j)$ . We further approximate the minimization of the weighted sum MSE problem by decomposing it into J MSE minimization problems. For any uplink UE j, the subproblem (14) is solved to obtain the suboptimal receiver vector  $v_i$ :

$$\min_{\boldsymbol{v}_{j}} e_{\mathrm{U},j} \left( \boldsymbol{v}_{j} \right), \tag{14a}$$

<span id="page-5-9"></span><span id="page-5-8"></span><span id="page-5-7"></span><span id="page-5-3"></span>s.t. 
$$(13b)$$
 (14b)

<span id="page-5-0"></span>To solve (14) and enable distributed computation, we leverage the team theory in [40] and extend the traditional LMMSE method into CF-RAN systems [41], [42]. By utilizing the cooperation and switching capabilities of EDUs, we propose an EDU-TMMSE reception scheme, which enables each EDU to independently calculate its local receiver matrix  $V_x$ according to its own information and sideband information. Additionally, it can dynamically adjust the amount of shared sideband information in real-time according to backhaul load and user rate, achieving a dynamic balance between signaling and performance with flexible scalability.

We continue processing (10) and rewrite the MSE function of uplink UE j,  $e_{U,j}(\boldsymbol{v}_j)$  as follows:

<span id="page-5-4"></span>
$$e_{\mathrm{U},j}\left(\boldsymbol{v}_{j}\right) \triangleq \mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}}\left\{\left\|\boldsymbol{v}_{j}^{\mathrm{H}}\boldsymbol{H}_{\mathrm{U}}\boldsymbol{P}^{1/2} - \boldsymbol{e}_{j}^{\mathrm{H}}\right\|^{2} + \boldsymbol{v}_{j}^{\mathrm{H}}\boldsymbol{\Omega}_{\mathrm{IAI}}\boldsymbol{v}_{j} + \sigma_{\mathrm{U}}^{2}\|\boldsymbol{v}_{j}\|^{2}\right\},\tag{15}$$

where  $\mathbb{E}_{H_{11}}\{.\}$  represents the expectation over the random variable  $H_{U}$ ,  $e_{j}$  is a unit vector with the j element equal to 1, and  $\Omega_{\rm IAI}$  is the inter-AP residual interference matrix. The average power of the interference signal received by the RAP associated with EDU x from the TAP associated with EDU x' for downlink user k is  $\mathbb{E}\left\{\tilde{\bm{H}}_{\text{IAI},xx'}\bm{w}_{x'k}\bm{w}_{x'k}^{\text{H}}\tilde{\bm{H}}_{\text{IAI},xx'}^{\text{H}}\right\}=$  $\sigma_{\text{IAI},xx'}^2 \mathbb{E}\left\{\|\boldsymbol{w}_{x'k}\|^2\right\} \boldsymbol{I}_{NZ_x}$ . Using the property that channel estimation errors between different EDUs are independent, we finally obtain the block diagonal IAI matrix  $\Omega_{\mathrm{IAI}} =$ blkdiag  $\left(\sum_{x'=1}^{X}\sum_{k=1}^{K}\sigma_{\text{IAI},xxx'}^{2}\|\boldsymbol{w}_{x'k}\|^{2}\boldsymbol{I}_{NZ_{x}}|_{x\in\mathcal{X}}\right)\in\mathbb{C}^{NZ\times NZ}.$ To obtain the optimal distributed receiver, let  $\boldsymbol{F}_{\text{U}}=$ 

<span id="page-5-6"></span> $H_{\rm II}P^{1/2}$  and further expand (15) as

$$\begin{split} e_{\mathrm{U},j}\left(\boldsymbol{v}_{j}\right) &= \mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}}\{\boldsymbol{v}_{j}^{\mathrm{H}}\boldsymbol{F}_{\mathrm{U}}\boldsymbol{F}_{\mathrm{U}}^{\mathrm{H}}\boldsymbol{v}_{j} - \boldsymbol{v}_{j}^{\mathrm{H}}\boldsymbol{f}_{\mathrm{U},j} \\ &- \boldsymbol{f}_{\mathrm{U},j}^{\mathrm{H}}\boldsymbol{v}_{j} + 1 + \sigma_{\mathrm{U}}^{2}\boldsymbol{v}_{j}^{\mathrm{H}}\boldsymbol{v}_{j} + \boldsymbol{v}_{j}^{\mathrm{H}}\boldsymbol{\Omega}_{\mathrm{IAI}}\boldsymbol{v}_{j}\} \\ &= \mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}}\{\boldsymbol{v}_{j}^{\mathrm{H}}\left(\boldsymbol{F}_{\mathrm{U}}\boldsymbol{F}_{\mathrm{U}}^{\mathrm{H}} + \sigma_{\mathrm{U}}^{2}\boldsymbol{I}_{NZ} + \boldsymbol{\Omega}_{\mathrm{IAI}}\right)\boldsymbol{v}_{j} \end{split}$$

<span id="page-5-1"></span>(11a)

$$- v_j^{\mathrm{H}} f_{\mathrm{U},j} - f_{\mathrm{U},j}^{\mathrm{H}} v_j + 1 \}, \tag{16}$$

$$\Omega_{\mathrm{IAI}} = \mathrm{diag} \left( \sum_{x'=1}^{X} \sigma_{\mathrm{IAI},xxx'}^2 p_{\mathrm{D},x'} I_{N\mathrm{Z}_x} |_{x \in \mathcal{X}} \right)$$
 when  $p_{\mathrm{D},x'} = \sum_{x'=1}^{X} \| \boldsymbol{w}_{x'k} \|^2$ , where each EDU needs to share its precoding power with other EDUs to obtain the complete IAI matrix. To simplify the analysis, we assume  $\sigma_{\mathrm{IAI},xx'}^2 = \sigma_{\mathrm{IAI}}^2$  and  $p_{\mathrm{D},total} = \sum_{x=1}^{X} p_{\mathrm{D},x}$ . The IAI matrix can be further simplified to  $\Omega_{\mathrm{IAI}} = p_{\mathrm{D},total}\sigma_{\mathrm{IAI}}^2 I_{NZ}$ . Under this assumption, EDUs do not need to share their precoding power with each other. Instead, they first send transmit power  $p_{\mathrm{D},x}$  to CCU, which calculates the total transmit power  $p_{\mathrm{D},total}$  and shares it with all EDUs. This approach effectively reduces the number of signaling exchanges. Finally, the MSE of uplink UE  $j$  can be simplified as

$$e_{\mathrm{U},j}\left(\boldsymbol{v}_{j}\right) = \mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}}\left\{\boldsymbol{v}_{j}^{\mathrm{H}}\left(\boldsymbol{F}_{\mathrm{U}}\boldsymbol{F}_{\mathrm{U}}^{\mathrm{H}} + \sigma_{\mathrm{U},eff}^{2}\boldsymbol{I}_{NZ}\right)\boldsymbol{v}_{j} - \boldsymbol{v}_{j}^{\mathrm{H}}\boldsymbol{f}_{\mathrm{U},j} - \boldsymbol{f}_{\mathrm{U},j}^{\mathrm{H}}\boldsymbol{v}_{j} + 1\right\},\tag{17}$$

where  $\sigma_{\mathrm{U},eff}^2 = \sigma_{\mathrm{U}}^2 + \sigma_{\mathrm{IAI}}^2 p_{\mathrm{D},total}$ . Next,  $\boldsymbol{U} = \boldsymbol{F}_{\mathrm{U}} \boldsymbol{F}_{\mathrm{U}}^{\mathrm{H}} + \sigma_{\mathrm{U}}^2 \boldsymbol{I}_{NZ} + \boldsymbol{\Omega}_{\mathrm{IAI}}$ , then the optimization objective for uplink UE j can be expressed as a typical quadratic team problem

$$\boldsymbol{v}_{j}^{\star} = \operatorname*{arg\,min}_{\boldsymbol{v}_{j}} \mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}} \left\{ \boldsymbol{v}_{j}^{\mathrm{H}} \boldsymbol{U} \boldsymbol{v}_{j} - \boldsymbol{v}_{j}^{\mathrm{H}} \boldsymbol{f}_{\mathrm{U}, j} - \boldsymbol{f}_{\mathrm{U}, j}^{\mathrm{H}} \boldsymbol{v}_{j} + 1 \right\}.$$
(18)

<span id="page-6-1"></span>Lemma 1 (Stationary Condition for Quadratic Team Decision): Consider the quadratic team decision problem in (18), where each EDU x makes local decisions  $v_{xj}$  based on partial observation  $S_x$ . The problem admits a unique optimal solution if and only if the following conditional expectation partial derivative condition holds:

$$\nabla_{\boldsymbol{v}_{x_j}} \mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}} \left\{ e_{\mathrm{U},j}(\boldsymbol{v}_j) \, | \, \boldsymbol{S}_x \right\} = \boldsymbol{0}, \quad \forall x \in \mathcal{X}.$$
 (19)

Expanding this condition yields:

$$\mathbb{E}_{\boldsymbol{H}_{U}} \left\{ \boldsymbol{U}_{xx} \mid \boldsymbol{S}_{x} \right\} \boldsymbol{v}_{xj}^{\star} + \sum_{x' \neq x}^{X} \mathbb{E}_{\boldsymbol{H}_{U}} \left\{ \boldsymbol{U}_{xx'} \boldsymbol{v}_{x'j}^{\star} \mid \boldsymbol{S}_{x} \right\} - \mathbb{E}_{\boldsymbol{H}_{U}} \left\{ \boldsymbol{f}_{U,xj} \mid \boldsymbol{S}_{x} \right\} = \mathbf{0}, \tag{20}$$

where the first term represents the local interference-plus-noise contribution, the second term captures inter-EDU coupling, and the third term is the desired signal component.

*Proof:* This lemma is a restatement of Theorem 2.6.6 in [46] adapted to our system notation. The proof follows from the first-order optimality condition for constrained optimization under partial information. Since each EDU x can only observe  $S_x$ , the optimal decision  $v_{xj}^*$  must satisfy the conditional expectation of the gradient being zero. The uniqueness follows from the strict convexity of the quadratic objective and the positive definiteness of  $U_{xx}$ .

According to Lemma 1, for any EDU x, under the given observation information  $S_x$ , for a given set of  $\left\{v_{x'j}^\star\right\}_{x'\neq x}$ , if  $e_{\mathrm{U},j}\left(v_{xj}^\star\right)<\infty$  and  $\nabla_{v_{xj}}e_j\left(v_{xj},\left\{v_{x'j}^\star\right\}_{x'\neq x}|S_x\right)=0$  hold, then (18) has a stationary solution  $v_{xj}^\star\left(S_x\right)$ . To obtain

the receiver matrix at each EDU, we need to express the objective function in (18) as a function of  $v_{xj}$ 

<span id="page-6-2"></span>
$$\mathbb{E}_{\boldsymbol{H}_{\mathbf{U}}} \left\{ \boldsymbol{v}_{j}^{\mathbf{H}} \boldsymbol{U} \boldsymbol{v}_{j} - \boldsymbol{v}_{j}^{\mathbf{H}} \boldsymbol{f}_{\mathbf{U},j} - \boldsymbol{f}_{\mathbf{U},j}^{\mathbf{H}} \boldsymbol{v}_{j} + 1 \right\}$$

$$= \mathbb{E}_{\boldsymbol{H}_{\mathbf{U}}} \left\{ \sum_{x=1}^{X} \sum_{x'=1}^{X} \boldsymbol{v}_{xj}^{\mathbf{H}} \boldsymbol{U}_{xx'} \boldsymbol{v}_{x'j} - \sum_{x=1}^{X} \boldsymbol{v}_{xj}^{\mathbf{H}} \boldsymbol{f}_{\mathbf{U},xj} - \sum_{x=1}^{X} \boldsymbol{f}_{\mathbf{U},xj}^{\mathbf{H}} \boldsymbol{v}_{xj} + 1 \right\}, \qquad (21)$$

where  $U_{xx} = F_{U,x}F_{U,x}^H + \sigma_{U,eff}^2I_{NZ_x}$  and  $U_{xx'} = F_{U,x}F_{U,x'}^H$ ,  $(x \neq x')$ , by setting the partial derivative of (21) with respect to  $v_{xj}$  to zero, we can obtain the stationary condition for (14) as

<span id="page-6-3"></span>
$$\mathbb{E}_{\boldsymbol{H}_{U}} \left\{ \boldsymbol{U}_{xx} \left| \boldsymbol{S}_{x} \right\} \boldsymbol{v}_{xj}^{\star} + \sum_{x' \neq x}^{X} \mathbb{E}_{\boldsymbol{H}_{U}} \left\{ \boldsymbol{U}_{xx'} \boldsymbol{v}_{x'j}^{\star} \left| \boldsymbol{S}_{x} \right. \right\} - \mathbb{E}_{\boldsymbol{H}_{U}} \left\{ \boldsymbol{f}_{U,xj} \left| \boldsymbol{S}_{x} \right. \right\} = \mathbf{0},$$
 (22)

where  $\mathbb{E}_{H_{\mathrm{U}}}\{U_{xx}|S_x\}$  represents the expectation of  $U_{xx}$  over the uplink channel  $H_{\mathrm{U}}$  given the conditional information  $S_x$ , and the rest follows similarly.

<span id="page-6-0"></span>To enhance the robustness of the reception scheme, we also consider the channel estimation error between uplink UEs and RAPs, satisfying  $\boldsymbol{H}_{\mathrm{U}} = \hat{\boldsymbol{H}}_{\mathrm{U}} + \tilde{\boldsymbol{H}}_{\mathrm{U}}$ , where  $\hat{\boldsymbol{H}}_{\mathrm{U}}$  and  $\tilde{\boldsymbol{H}}_{\mathrm{U}}$  represent the estimated channel and the error channel, respectively. Due to the orthogonality of MMSE estimation,  $\hat{\boldsymbol{h}}_{\mathrm{U},xj}$  and  $\tilde{\boldsymbol{h}}_{\mathrm{U},xj}$  are independent. Additionally, the channel and error correlation matrices for the uplink UE j estimated by EDU x are represented as  $\hat{\boldsymbol{R}}_{\mathrm{U},xj} = \mathbb{E}\left\{\hat{\boldsymbol{h}}_{\mathrm{U},xj}\hat{\boldsymbol{h}}_{\mathrm{U},xj}^{\mathrm{H}}\right\}$  and  $\tilde{\boldsymbol{K}}_{\mathrm{U},xj} = \mathbb{E}\left\{\hat{\boldsymbol{h}}_{\mathrm{U},xj}\hat{\boldsymbol{h}}_{\mathrm{U},xj}^{\mathrm{H}}\right\}$ , respectively. For convenience, we previously defined  $\boldsymbol{F}_{\mathrm{U}} = \boldsymbol{H}_{\mathrm{U}}\boldsymbol{P}^{1/2}$ ,  $\boldsymbol{F}_{\mathrm{U}} = \hat{\boldsymbol{F}}_{\mathrm{U}} + \tilde{\boldsymbol{F}}_{\mathrm{U}}$ , where  $\hat{\boldsymbol{F}}_{\mathrm{U}}$  and  $\tilde{\boldsymbol{F}}_{\mathrm{U}}$  correspond to the effective estimated channel and error, respectively.

Based on the above analysis, we can derive  $\mathbb{E}_{H_{\mathrm{U}}}\left\{\hat{F}_{\mathrm{U},x}\hat{F}_{\mathrm{U},x}^{\mathrm{H}}|S_{x}\right\} = \hat{F}_{\mathrm{U},x}\hat{F}_{\mathrm{U},x}^{\mathrm{H}}$ ,  $\mathbb{E}_{H_{\mathrm{U}}}\left\{\hat{F}_{\mathrm{U},x}\tilde{F}_{\mathrm{U},x}^{\mathrm{H}}|S_{x}\right\} = 0$ ,  $\mathbb{E}_{H_{\mathrm{U}}}\left\{\tilde{F}_{\mathrm{U},x}\hat{F}_{\mathrm{U},x}^{\mathrm{H}}|S_{x}\right\} = 0$ ,  $\mathbb{E}_{H_{\mathrm{U}}}\left\{\tilde{F}_{\mathrm{U},x}\tilde{F}_{\mathrm{U},x}^{\mathrm{H}}|S_{x}\right\} = \sum_{j=1}^{J}p_{\mathrm{U},j}\tilde{R}_{\mathrm{U},xj}$ . Thus, the first term in (22) can be expressed as

<span id="page-6-4"></span>
$$\mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}} \left\{ \boldsymbol{U}_{xx} | \boldsymbol{S}_{x} \right\}$$

$$= \mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}} \left\{ \boldsymbol{F}_{\mathrm{U},x} \boldsymbol{F}_{\mathrm{U},x}^{\mathrm{H}} + \sigma_{\mathrm{U},eff}^{2} \boldsymbol{I}_{NZ_{x}} | \boldsymbol{S}_{x} \right\}$$

$$= \mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}} \left\{ \left( \hat{\boldsymbol{F}}_{\mathrm{U},x} + \tilde{\boldsymbol{F}}_{\mathrm{U},x} \right) \left( \hat{\boldsymbol{F}}_{\mathrm{U},x}^{\mathrm{H}} + \tilde{\boldsymbol{F}}_{\mathrm{U},x}^{\mathrm{H}} \right) | \boldsymbol{S}_{x} \right\}$$

$$+ \sigma_{\mathrm{U},eff}^{2} \boldsymbol{I}_{NZ_{x}}$$

$$= \hat{\boldsymbol{F}}_{\mathrm{U},x} \hat{\boldsymbol{F}}_{\mathrm{U},x}^{\mathrm{H}} + \sum_{j=1}^{J} p_{\mathrm{U},j} \tilde{\boldsymbol{R}}_{\mathrm{U},xj} + \sigma_{\mathrm{U},eff}^{2} \boldsymbol{I}_{NZ_{x}}. \tag{23}$$

For the second term in (22), we can obtain

$$\mathbb{E}_{\boldsymbol{H}_{\mathbf{U}}}\left\{\boldsymbol{U}_{xx'}\boldsymbol{v}_{x'j}^{\star}|\boldsymbol{S}_{x}\right\} = \mathbb{E}_{\hat{\boldsymbol{H}}_{\mathbf{U}}}\left\{\hat{\boldsymbol{F}}_{\mathbf{U},x}\hat{\boldsymbol{F}}_{\mathbf{U},x'}^{\mathbf{H}}\boldsymbol{v}_{x'j}^{\star}|\boldsymbol{S}_{x}\right\}$$
$$= \hat{\boldsymbol{F}}_{\mathbf{U},x}\mathbb{E}_{\hat{\boldsymbol{H}}_{\mathbf{U}}}\left\{\hat{\boldsymbol{F}}_{\mathbf{U},x'}^{\mathbf{H}}\boldsymbol{v}_{x'j}^{\star}|\boldsymbol{S}_{x}\right\}. \tag{24}$$

For the third term in (22), it can be further simplified as

$$\mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}}\left\{\boldsymbol{f}_{\mathrm{U},xj}\left|\boldsymbol{S}_{x}\right.\right\}$$

$$=\mathbb{E}_{\boldsymbol{H}_{\mathrm{U}}}\left\{\left(\hat{\boldsymbol{F}}_{\mathrm{U},x}+\tilde{\boldsymbol{F}}_{\mathrm{U},x}\right)\boldsymbol{e}_{j}\left|\boldsymbol{S}_{x}\right.\right\}=\hat{\boldsymbol{F}}_{\mathrm{U},x}\boldsymbol{e}_{j}.\tag{25}$$

Finally, the stationary condition (22) can be reformulated as

$$\left(\hat{\boldsymbol{F}}_{\mathrm{U},x}\hat{\boldsymbol{F}}_{\mathrm{U},x}^{\mathrm{H}} + \sum_{j=1}^{J} p_{\mathrm{U},j}\tilde{\boldsymbol{R}}_{\mathrm{U},xj} + \sigma_{\mathrm{U},eff}^{2} \boldsymbol{I}_{NZ_{x}}\right)^{-1} \boldsymbol{v}_{xj}^{\star} (\boldsymbol{S}_{x})$$

$$+ \sum_{x'\neq x}^{X} \hat{\boldsymbol{F}}_{\mathrm{U},x} \mathbb{E} \left\{ \hat{\boldsymbol{F}}_{\mathrm{U},x'}^{\mathrm{H}} \boldsymbol{v}_{x'j}^{\star} | \boldsymbol{S}_{x} \right\} + \hat{\boldsymbol{F}}_{\mathrm{U},x} \boldsymbol{e}_{j} = \boldsymbol{0}. \tag{26}$$

For uplink UE j, the optimal receiver at EDU x is

$$\boldsymbol{v}_{xj}^{\star}(\boldsymbol{S}_{x}) = \left(\hat{\boldsymbol{F}}_{\mathrm{U},x}\hat{\boldsymbol{F}}_{\mathrm{U},x}^{\mathrm{H}} + \sum_{j=1}^{J} p_{\mathrm{U},j}\tilde{\boldsymbol{R}}_{\mathrm{U},xj} + \sigma_{\mathrm{U},eff}^{2}\boldsymbol{I}_{NZ_{x}}\right)^{-}$$

$$\hat{\boldsymbol{F}}_{\mathrm{U},x}\left(\boldsymbol{e}_{j} - \sum_{x'\neq x}^{X} \mathbb{E}_{\hat{\boldsymbol{H}}_{\mathrm{U}}}\left\{\hat{\boldsymbol{F}}_{\mathrm{U},x'}^{\mathrm{H}}\boldsymbol{v}_{x'j}^{\star} | \boldsymbol{S}_{x}\right\}\right)$$

$$= \boldsymbol{A}_{x}\left(\boldsymbol{e}_{j} - \sum_{x'\neq x}^{X} \mathbb{E}_{\hat{\boldsymbol{H}}_{\mathrm{U}}}\left\{\hat{\boldsymbol{F}}_{\mathrm{U},x'}^{\mathrm{H}}\boldsymbol{v}_{x'j}^{\star} | \boldsymbol{S}_{x}\right\}\right), \quad (27)$$

where

$$\boldsymbol{A}_{x} = \left(\hat{\boldsymbol{F}}_{\mathrm{U},x}\hat{\boldsymbol{F}}_{\mathrm{U},x}^{\mathrm{H}} + \sum_{j=1}^{J} p_{\mathrm{U},j}\tilde{\boldsymbol{R}}_{\mathrm{U},xj} + \sigma_{\mathrm{U},eff}^{2} \boldsymbol{I}_{NZ_{x}}\right)^{-1} \hat{\boldsymbol{F}}_{\mathrm{U},x}.$$
(28)

<span id="page-7-8"></span><span id="page-7-7"></span>It can be found that this is consistent with the LMMSE receiver form derived in the previous CF-mMIMO correlation work [43], [44]. However, we can further enhance the cooperative reception capability on the basis of LMMSE by adding EDU processing. we denote (28) as EMMSE receiver, since EMMSE only uses EDU channel estimation information for reception, the sideband information is 0, the performance is limited. To further improve the overall performance, it is necessary to make full use of the existing information in CF-RAN systems for appropriate compensation. Therefore, we consider a two-layer receiver, where the reception vector of EDU x for uplink UE j can be expressed as  $v_{xj} = A_x B_x e_j$ , where  $A_x$  is a function of the estimated channel  $H_{U,x}$  and is composed of instantaneous information. For the compensation matrix  $B_x$ , its components can be dynamically adjusted, and it is a function of the sideband information  $\hat{S}_x$ .

Since the two-layer combiner satisfies the form  $V_x = A_x B_x$ , substituting it into (27), we can get (29) that holds for any EDU. we adopt an EDU-sharing mechanism that has been proved in [40], since an EDU can share information with other EDUs through signaling on the fronthaul link, we assume that each EDU has two states: shared (On) and non-shared (Off). If EDU x is in the shared state, it shares its local instantaneous equivalent channel  $\hat{F}_{U,x}^H A_x$  with other EDUs. Otherwise, CCU shares the statistical equivalent channel information of EDU x, denoted as  $\mathbb{E}_{\hat{H}_U} \left\{ \hat{F}_{U,x}^H A_x \right\}$ , with other EDUs. It is assumed that CCU has knowledge of the statistical information of the entire system. Unlike instantaneous shared information,

this statistical information only needs to be shared once and does not require real-time updates.

<span id="page-7-2"></span>
$$A_{x}B_{x}e_{j}$$

$$= A_{x}\left(e_{j} - \sum_{x'\neq x}^{X} \mathbb{E}_{\hat{H}_{U}}\left\{\hat{F}_{U,x'}^{H}v_{x'j}^{\star}|S_{x}\right\}\right), \qquad (29a)$$

$$\rightarrow \hat{F}_{U,x}B_{x}e_{j}$$

$$= \hat{F}_{U,x}\left(e_{j} - \sum_{x'\neq x}^{X} \mathbb{E}_{\hat{H}_{U}}\left\{\hat{F}_{U,x'}^{H}v_{x'j}^{\star}|S_{x}\right\}\right), \qquad (29b)$$

$$\rightarrow \hat{F}_{U,x}\left(B_{x} + \sum_{x'\neq x}^{X} \mathbb{E}_{\hat{H}_{U}}\left\{\hat{F}_{U,x'}^{H}A_{x'}B_{x'}|S_{x}\right\} - I\right)e_{j} = 0, \qquad (29c)$$

$$\rightarrow B_{x} + \sum_{x'\neq x}^{X} \mathbb{E}_{\hat{H}_{U}}\left\{\hat{F}_{U,x'}^{H}A_{x'}|S_{x}\right\}\mathbb{E}_{\hat{H}_{U}}\left\{B_{x'}|S_{x}\right\} = I. \qquad (29d)$$

<span id="page-7-3"></span><span id="page-7-1"></span>For any EDU x, its partial observation information  $S_x$  contains information about other EDUs, but the form depends on the state of the other EDUs. This can be handled according to the following criteria,

$$\mathbb{E}\left\{\hat{\boldsymbol{F}}_{\mathrm{U},x'}^{\mathrm{H}}\boldsymbol{A}_{x'}\left|\boldsymbol{S}_{x}\right.\right\} = \left\{\hat{\boldsymbol{F}}_{\mathrm{U},x'}^{\mathrm{H}}\boldsymbol{A}_{x'}, \mathrm{EDU}x' = \mathrm{On}\right.$$

$$\mathbb{E}\left\{\hat{\boldsymbol{F}}_{\mathrm{U},x'}^{\mathrm{H}}\boldsymbol{A}_{x'}\right\}, \mathrm{EDU}x' = \mathrm{Off}$$
(30)

<span id="page-7-0"></span>Finally, EDU can locally solve the linear system (29d) to obtain  $B_x$ . However,  $\mathbb{E}_{\hat{H}_U}\{B_{x'}|S_x\}$  remains implicit, making the system difficult to solve. Fortunately, due to the EDU sharing mechanism, for any EDU x, it will receive the instantaneous information of shared EDUs in real-time and the statistical information of non-shared EDUs obtained in advance as the common information of the entire CF-RAN. Each EDU fully utilizes this common information, and  $B_x$  can be solved from the following linear system,

$$\boldsymbol{B}_{x} + \sum_{x' \neq x}^{X} \mathbb{E}_{\hat{\boldsymbol{H}}_{U}} \left\{ \hat{\boldsymbol{F}}_{U,x'}^{H} \boldsymbol{A}_{x'} | \boldsymbol{S}_{x} \right\} \boldsymbol{B}_{x'} = \boldsymbol{I}, \forall x \in \mathcal{X}. \quad (31)$$

Let (32)-(34), as shown at the bottom of the next page.

Then (29d) can be further transformed into  $\Phi B = C$ , and then the overall compensation matrix is obtained as

<span id="page-7-6"></span><span id="page-7-5"></span>
$$\boldsymbol{B} = \boldsymbol{\Phi}^{-1} \boldsymbol{C}. \tag{35}$$

Before presenting the algorithm, we establish the theoretical foundation for the existence and uniqueness of the ETMMSE solution. Our analysis builds upon the team MMSE framework developed in [40], which provides rigorous conditions for distributed MMSE optimization under partial information constraints.

<span id="page-7-4"></span>Assumption 1: The following conditions hold for the CF-RAN with NA-FD system: (1) The channel covariance matrices  $\mathbf{R}_{\mathrm{U},xj} = \mathbb{E}\{\mathbf{h}_{\mathrm{U},xj}\mathbf{h}_{\mathrm{U},xj}^{\mathrm{H}}\}$  are bounded and positive semi-definite for all  $x \in \mathcal{X}$  and  $j \in \mathcal{J}$ ; (2) The effective noise

covariance  $\sigma_{\rm U,eff}^2 {\bf I} + {\bf \Omega}_{\rm IAI}$  is positive definite; (3) For any pair of EDUs (x, x') where  $x \neq x'$ , the following Markov chain holds:  $\mathbf{H}_{\mathrm{U},x} \to \hat{\mathbf{H}}_{\mathrm{U},x} \to \mathbf{S}_x \to \mathbf{S}_{x'} \to \hat{\mathbf{H}}_{\mathrm{U},x'} \to \mathbf{H}_{\mathrm{U},x'}$ .

Proposition 1: Under Assumption 1, the linear system in (31) admits a unique solution  $\mathbf{B} = \mathbf{\Phi}^{-1}\mathbf{C}$ , and the resulting ETMMSE receiver  $V_x = A_x B_x$  for each EDU x is the unique stationary solution that minimizes the uplink MSE  $e_{U,j}(\mathbf{v}_j)$ in (14).

*Proof:* The proof follows from Lemma 1 and Theorems 2-3 in [40]. Under Assumption 1, the matrix  $\mathbf{U} = \mathbf{F}_{\mathrm{U}}\mathbf{F}_{\mathrm{U}}^{\mathrm{H}} +$  $\sigma_{\mathrm{U.eff}}^2 \mathbf{I}_{NZ} + \mathbf{\Omega}_{\mathrm{IAI}}$  in (18) satisfies  $\mathbb{E}[\|\mathbf{U}\|_{\mathrm{F}}^2] < \infty$  due to the bounded channel statistics. Furthermore, the positive definiteness of the noise-plus-interference covariance ensures that  $\Phi$  in (32) is invertible. The Markov chain condition in Assumption 1.3 guarantees that the conditional expectations in the stationary condition (22) are well-defined. Consequently, the team MMSE framework guarantees both existence and uniqueness of the solution.

Moreover, the convergence of the alternating updates between V, W, and p<sub>U</sub> in the outer PDBCD loop (Algorithm 3) follows from the block coordinate descent convergence theory [39], as each subproblem yields a unique optimal solution under the stated assumptions.

It can be observed that sharing EDU information in CF-RAN systems will alter the conditional expectations in  $\Phi$ . As the number of shared EDUs increases, more statistical information will be replaced by instantaneous information, thereby improving system performance. Thus, we can dynamically adjust the number of shared EDUs to balance backhaul load and performance. When all EDUs are shared, the performance reaches its optimum. Finally, we obtain the reception matrix of EDU x as  $V_x = A_x B_x$ , achieving distributed computation. The specific steps are shown in Algorithm 1.

We now briefly analyze the signaling cost of the EDU sharing mechanism. For a non-shared EDU  $(x \notin \mathcal{X}_s)$ , the CCU broadcasts its statistical equivalent channel  $\mathbb{E}\{F_{\mathrm{U},x}^{\mathbf{n}}A_x\}$ , which is computed offline and does not require real-time updates. For a shared EDU  $(x \in \mathcal{X}_s)$ , the instantaneous equivalent channel  $\hat{\pmb{F}}_{\mathrm{U},x}^{\mathrm{H}} \pmb{A}_x \in \mathbb{C}^{J \times J}$  is exchanged via fronthaul in each coherence interval. The total signaling dimension scales as  $S_{\text{total}}(X_s) = \mathcal{O}(X_s \cdot J^2)$ , linear in the number of shared EDUs  $X_s$ . This linear scaling enables flexible performanceoverhead trade-offs.

### C. Distributed Solution for Subproblem 2

For the given  $\{\alpha_{\rm U}, p_{\rm U}, V\}$ , we obtain the optimal solution of  $\{\boldsymbol{\alpha}_{\mathrm{D}}, \boldsymbol{u}_{\mathrm{D}}, \boldsymbol{W}\}$ ,

$$\min_{\{\boldsymbol{\alpha}_{\mathrm{D}},\boldsymbol{u}_{\mathrm{D}},\boldsymbol{W}\}} f_{2}(\boldsymbol{\alpha}_{\mathrm{D}},\boldsymbol{u}_{\mathrm{D}},\boldsymbol{W}), \qquad (36a)$$
s.t.  $(8b),(8d),(8e)$   $(36b)$ 

<span id="page-8-1"></span>s.t. 
$$(8b), (8d), (8e)$$
 (36b)

where  $f_2\left(\boldsymbol{u}_{\mathrm{D}}, \boldsymbol{W}, \boldsymbol{\alpha}_{\mathrm{D}}\right) = \chi_D\left(\boldsymbol{W}, \boldsymbol{a}_D, \boldsymbol{u}_D\right) + \sum_{x=1}^{X} \sum_{k=1}^{K} \sum_{l=1}^{L} \|\boldsymbol{v}_{xj}\|^2 \|\boldsymbol{w}_{lk}\|^2 \sigma_{\mathrm{IAI}}^2$ , since  $\{\boldsymbol{\alpha}_{\mathrm{D}}, \boldsymbol{u}_{\mathrm{D}}, \boldsymbol{W}\}$  are all related to downlink transmission with strong correlation, according to the idea of block optimization, we iteratively optimize the current subproblem (36) in an inner loop to make it converge to the optimal solution.

Using alternating optimization (AO) method, by fixing  $\{\alpha_{\rm U}, p_{\rm U}, V\}$  and  $\{\alpha_{\rm D}, W\}$ , (36) is concave with respect to  $\{u_{D,k}\}_{k\in\mathcal{K}}$  with no constraints, then we take partial derivatives of  $u_{D,k}$  and set it to 0 to obtain the optimal  $u_{D,k}^*$ . Similarly, by fixing  $\{\boldsymbol{\alpha}_{\textsf{U}}, \boldsymbol{p}_{\textsf{U}}, \boldsymbol{V}\}$  and  $\{\boldsymbol{u}_{\textsf{D}}, \boldsymbol{W}\}$ , we can obtain the optimal  $\alpha_{D,k}^*$ , where

<span id="page-8-2"></span><span id="page-8-0"></span>For fixed  $\{\alpha_{\rm U}, p_{\rm U}, V\}$  and  $\{\alpha_{\rm D}, u_{\rm D}\}$ , since the objective function (36) is a convex function with convex constraints concerning the precoding matrix W, it can be solved using the Lagrange multiplier method based on KKT conditions.

$$\Phi = \begin{bmatrix}
\mathbf{I} & \mathbb{E}_{\hat{H}_{U}} \left\{ \hat{F}_{U,2}^{H} \mathbf{A}_{2} | \mathbf{S}_{1} \right\} \dots \mathbb{E}_{\hat{H}_{U}} \left\{ \hat{F}_{U,X}^{H} \mathbf{A}_{X} | \mathbf{S}_{1} \right\} \\
\mathbb{E}_{\hat{H}_{U}} \left\{ \hat{F}_{U,1}^{H} \mathbf{A}_{1} | \mathbf{S}_{2} \right\} & \mathbf{I} \dots \mathbb{E}_{\hat{H}_{U}} \left\{ \hat{F}_{U,X}^{H} \mathbf{A}_{X} | \mathbf{S}_{2} \right\} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbb{E}_{\hat{H}_{U}} \left\{ \hat{F}_{U,1}^{H} \mathbf{A}_{1} | \mathbf{S}_{X} \right\} \mathbb{E}_{\hat{H}_{U}} \left\{ \hat{F}_{U,2}^{H} \mathbf{A}_{2} | \mathbf{S}_{X} \right\} \dots \mathbf{I}
\end{bmatrix}, (32)$$

$$\boldsymbol{B} = \begin{bmatrix} \boldsymbol{B}_{1}^{\mathrm{H}} \ \boldsymbol{B}_{2}^{\mathrm{H}} \ \dots \ \boldsymbol{B}_{X}^{\mathrm{H}} \end{bmatrix}^{\mathrm{H}} \in \mathbb{C}^{XJ \times J}, \tag{33}$$

$$C = \begin{bmatrix} I & I & \dots & I \end{bmatrix}^{\mathrm{H}} \in \mathbb{C}^{XJ \times J}. \tag{34}$$

$$u_{\mathrm{D},k}^{\star} = \frac{\sum_{x=1}^{X} \hat{\boldsymbol{h}}_{xk}^{\mathrm{H}} \boldsymbol{w}_{xk}}{\left| \sum_{x=1}^{X} \hat{\boldsymbol{h}}_{xk}^{\mathrm{H}} \boldsymbol{w}_{xk} \right|^{2} + \sum_{x=1}^{X} \sum_{k=1}^{K} \boldsymbol{w}_{xk'}^{\mathrm{H}} \tilde{\boldsymbol{R}}_{xk} \boldsymbol{w}_{xk'} + \sum_{j=1}^{J} \beta_{\mathrm{IUI},kj} p_{\mathrm{U},j} + \sigma_{\mathrm{D}}^{2}},$$
(37)

<span id="page-8-3"></span>
$$\alpha_{D,k} = \frac{1}{1 - u_{D,k}^* \sum_{x=1}^{X} \hat{\boldsymbol{h}}_{xk}^H \boldsymbol{w}_{xk}}.$$
(38)

## <span id="page-9-0"></span>Algorithm 1 Team Theory Algorithm for Solving (14)

**Input:** Uplink transmission power  $p_{\mathrm{U}}$ , total downlink precoding power  $p_{\mathrm{D},total}$ , Set of shared EDUs  $\mathcal{X}_s$ , CCU forwards the equivalent channel statistical information of non-shared EDUs  $\mathbb{E}_{\hat{H}_{\mathrm{U}}} \left\{ \hat{F}_{\mathrm{U},x_s}^{\mathrm{H}} A_{x_s} \right\}_{x_s \in \mathcal{X}_s}$  to all EDUs.

- 1: Each EDU uses its local estimated channel  $\hat{H}_{D,x}$  to compute EMMSE receiver  $A_x$  according to (28), and decides whether to share its instantaneous equivalent channel  $\hat{F}_{U,x}^H A_x$  with the rest of the system according to its sharing status.
- 2: Each EDU uses the obtained sideband information to compute  $B_x$  according to (35).

**Output:** Optimal receiver for each EDU  $V_x = A_x B_x$ 

<span id="page-9-8"></span><span id="page-9-7"></span>Traditional WMMSE algorithms are typically applied in CCU, as the number of UEs, APs and antennas increases, the computational complexity of centralized WMMSE precoding also increase [45], [47]. Therefore, we propose a distributed serial-parallel update EDU-WMMSE algorithm to obtain the precoding coefficients for each EDU, avoiding direct signaling exchange between EDUs while enabling parallel accelerated processing.

To fully utilize the computational power of EDUs and reduce the complexity of computing W, we revisit the MSE term (9) for downlink UE k and decouple the optimization problem (36) into multiple subproblems for processing. Optimal solutions for each subproblem are obtained iteratively using alternating optimization. Considering the TAP transmission power constraint, the optimal precoding coefficients obtained for each subproblem should correspond to a TAP. This decomposition allows the original WMMSE problem to be distributed across L TAPs. For the l-th optimization problem, the optimal solution can be obtained by fixing the other L-1 subproblems.

First, we define  $w_{A,l} = \operatorname{vec}(\boldsymbol{W}_l)$ , where  $\boldsymbol{W}_l$  is the precoding matrix computed by the EDU associated with TAP l. The optimization problem (36), with  $\{\boldsymbol{\alpha}_D, \boldsymbol{u}_D, \boldsymbol{w}_{A,l'\neq l}\}$  fixed, is reformulated as

$$\min_{\boldsymbol{w}_{A,l}} \quad \boldsymbol{w}_{A,l}^{\mathrm{H}} \boldsymbol{\Psi}_{l} \boldsymbol{w}_{A,l} + 2\Re \left\{ \boldsymbol{q}_{l}^{\mathrm{H}} \boldsymbol{w}_{A,l} \right\}, \tag{39a}$$

<span id="page-9-5"></span>s.t. 
$$(36b)$$
 (39b)

where

$$\mathbf{\Psi}_{l} = \mathbf{I}_{K} \otimes \left(\hat{\mathbf{H}}_{\mathrm{D},l} \mathbf{\Lambda} \hat{\mathbf{H}}_{\mathrm{D},l}^{\mathrm{H}}\right) + \mathbf{\Pi}_{l}$$
 (40a)

$$\mathbf{\Pi}_{l} = \left(\sum_{k=1}^{K} \alpha_{\mathrm{D},k} |u_{\mathrm{D},k}|^{2} \tilde{\beta}_{lk}^{2} + \sum_{x=1}^{X} ||\mathbf{v}_{xj}||^{2} ||\mathbf{w}_{A,l}||^{2} \sigma_{\mathrm{IAI}}^{2}\right) \mathbf{I}_{NK}$$
(40b)

$$\boldsymbol{q}_{l} = -\boldsymbol{\Gamma} \hat{\boldsymbol{h}}_{A,l} + \sum_{l' \neq l}^{L} \left( \boldsymbol{I}_{K} \otimes \left( \hat{\boldsymbol{H}}_{\mathrm{D},l} \boldsymbol{\Lambda} \hat{\boldsymbol{H}}_{\mathrm{D},l'}^{\mathrm{H}} \right) \right) \boldsymbol{w}_{A,l'} \quad (40c)$$

Additionally,  $\mathbf{\Lambda} = \operatorname{diag}\left(\left\{\alpha_{\mathrm{D},k}|u_{\mathrm{D},k}|^2\right\}_{k\in\mathcal{K}}\right),\ \tilde{\beta}_{lk}^2$  represents the channel estimation error gain between TAP l

and downlink UE k,  $\hat{\boldsymbol{h}}_{A,l} = \operatorname{vec}\left(\hat{\boldsymbol{H}}_{\mathrm{D},l}\right)$ , and  $\Gamma = \operatorname{diag}\left(\left\{u_k\alpha_{\mathrm{D},k}\right\}_{k\in\mathcal{K}}\right)\otimes \boldsymbol{I}_N$ .

Furthermore, for the subproblem of  $w_{A,l}$ , we use the Lagrange multiplier method to transform (39) into an unconstrained problem and obtain the local optimal solution of  $w_{A,l}$  through the first-order KKT condition [48]

<span id="page-9-9"></span><span id="page-9-2"></span>
$$\boldsymbol{w}_{A,l} = -(\boldsymbol{\Psi}_l + \lambda_l \boldsymbol{I}_{NK})^{-1} \boldsymbol{q}_l, \tag{41}$$

where  $\lambda_l \geq 0$  is the Lagrange multiplier. To satisfy the TAP power constraint, the current power of TAP l is calculated as

$$p(\lambda_l) = \boldsymbol{q}_l^{\mathrm{H}} (\boldsymbol{\Psi}_l + \lambda_l \boldsymbol{I}_{NK})^{-2} \boldsymbol{q}_l. \tag{42}$$

It can be observed that  $p\left(\lambda_l\right)$  is a monotonically decreasing function with respect to  $\lambda_l \geq 0$ . Therefore, if  $p\left(0\right) < p_{AP}$ , the optimal  $\lambda_l = 0$ , and the AP will transmit underpowered. Otherwise, using the bisection method, we find the dual variable  $\lambda_l$  that satisfies  $p\left(\lambda_l\right) = p_{AP}$  and substitute it into (41) to obtain the optimal precoding coefficients. The precoding coefficients for other TAPs are updated using the same approach.

Since each TAP is associated with an EDU, the TAP only performs transmission and forwarding functions, while channel estimation, precoding computation and other functions are implemented at the corresponding EDU. Define the set of TAPs associated with EDU x as  $\mathcal{L}_x$ , with a size of  $|\mathcal{L}_x|$ . Thus, EDU x can complete the optimization of  $|\mathcal{L}_x|$  subproblems at once and perform serial iterative updates. If EDUs can directly communicate with each other, then after EDU x completes its updates, it can share the information with EDU x+1 for serial updates. However, while fully serial updates can distribute computational load, it takes a longer time. Therefore, we propose a serial-parallel update scheme, where serial updates are performed within each EDU, and parallel computation is performed across EDUs. After all EDUs complete their internal serial updates, a parallel update is performed via CCU for all EDUs.

For the t-th TAP on the x-th EDU corresponding to  $q_{(x,t)}$ , we rewrite (40c) into the following form,

$$\boldsymbol{q}_{(x,t)}^{(n)} = -\boldsymbol{\Gamma}^{(n)} \hat{\boldsymbol{h}}_{A,(x,t)} + \left(\boldsymbol{I}_K \otimes \hat{\boldsymbol{H}}_{(x,t)}\right) \left(\bar{\boldsymbol{\varepsilon}}_{(x,t)}^{(n)} + \bar{\bar{\boldsymbol{\varepsilon}}}_x^{(n)}\right),\tag{43}$$

<span id="page-9-1"></span>where n represents the n-th parallel iteration,

$$\bar{\bar{\boldsymbol{\varepsilon}}}_{x}^{(n)} = \sum_{(x'',t'') \neq (x,t)} \operatorname{vec}\left(\boldsymbol{\Lambda}^{(n)}\hat{\boldsymbol{H}}_{(x'',t'')}^{H} \boldsymbol{W}_{(x'',t'')}^{(n)}\right), \quad (44)$$

<span id="page-9-6"></span>
$$\bar{\boldsymbol{\varepsilon}}_{(x,t)}^{(n)} = \sum_{(x,t' < t)}^{L_x} \boldsymbol{I}_K \otimes \left(\boldsymbol{\Lambda}^{(n)} \hat{\boldsymbol{H}}_{(x,t')}^{\mathsf{H}}\right) \boldsymbol{w}_{A,(x,t')}^{(n+1)}$$

$$+\sum_{(x,t'>l)}^{L_x} \boldsymbol{I}_K \otimes \left(\boldsymbol{\Lambda}^{(n)} \hat{\boldsymbol{H}}_{(x,t')}^{\mathrm{H}}\right) \boldsymbol{w}_{A,(x,t')}^{(n)}. \tag{45}$$

<span id="page-9-3"></span>At this point, each EDU receives the shared information obtained from the n-th parallel iteration from CCU:

<span id="page-9-4"></span>
$$\boldsymbol{\varepsilon}^{(n)} = \sum_{(\bar{x},\bar{t}) \in \mathcal{L}} \operatorname{vec}\left(\boldsymbol{\Lambda}^{(n)} \hat{\boldsymbol{H}}_{(\bar{x},\bar{t})}^{\mathrm{H}} \boldsymbol{W}_{(\bar{x},\bar{t})}^{(n)}\right). \tag{46}$$

For EDU x, when computing the precoding matrix for the t-th TAP associated with it, according to the information already available within each EDU, we can extract the

## <span id="page-10-2"></span>Algorithm 2 AO Algorithm for Solving Problem (36)

```
Input: Set iteration index n = 0, initialize feasible point
 1: Update \{\boldsymbol{\alpha}_D, \boldsymbol{u}_D\}^{(0)} according to (37) and (38)
 2: repeat
         Set n = n + 1
 3:
         CCU computes \varepsilon^{(n)} according to (46) and distributes
 4.
         it to all EDUs.
         for x \in \mathcal{X} do
 5:
            Parallel Processing
 6:
             for (x,t) \in \mathcal{L}_x do
 7:
                 Serial Processing
 8:
                Compute \Psi_{(x,t)}^{(n)} and q_{(x,t)}^{(n)} according to (40a) and
 9.
                Update \boldsymbol{w}_{A,(x,t)}^{(n)} according to (47).
10:
11:
         end for
12:
         CCU updates \{\alpha_{\rm D}, u_{\rm D}\}^{(n+1)} according to (37) and
13.
```

14: until The objective function no longer changes.

**Output:** Optimal solution  $W^*$ 

aggregated shared information  $\bar{\bar{\varepsilon}}_x^{(n)}$  from the shared quantity  $\varepsilon^{(n)}$ . This shared information remains constant during the serial iteration within EDU x. Additionally, we can obtain the partially updated shared information  $\bar{\varepsilon}_{(x,t)}^{(n)}$  for EDU x itself and compute the new  $q_{(x,t)}^{(n)}$ . At this point, the computational complexity of  $q_{(x,t)}^{(n)}$  does not increase with the number of APs. The optimal precoding coefficient for the t-th TAP in EDU x

$$\boldsymbol{w}_{A,(x,t)}^{(n)} = -\left(\boldsymbol{\Psi}_{(x,t)}^{(n)} + \lambda_{(x,t)}^{(n)} \boldsymbol{I}_{NK}\right)^{-1} \boldsymbol{q}_{(x,t)}^{(n)}.$$
 (47)

After completing the serial updates for the corresponding TAP subproblems within each EDU, the information needs to be shared with CCU. For EDU x, it is denoted as  $\delta_{xk}^{(n+1)} =$  $\sum_{x=1}^{X} \hat{\boldsymbol{h}}_{xk}^{\mathrm{H}} \boldsymbol{w}_{xk}^{(n)}$ , and  $u_k^{(n+1)}$  and  $\alpha_{D,k}^{(n+1)}$  are updated according to (37) and (38), respectively, until convergence.

In subsequent validations, we also found that parallel updates may cause significant fluctuations in the sum rate during iterations. This is because the vector  $q_{(x,t)}$  of TAP (x,t) depends on the information  $\bar{\varepsilon}_x$  from other EDUs, which can only be obtained in subsequent parallel iterations. To address this issue, we adopt a Jacobi best-response scheme to update the precoding coefficients gradually as

$$\mathbf{w}_{A,(x,t)}^{(n)} = \eta \mathbf{w}_{A,(x,t),tmp}^{(n)} + (1 - \eta) \mathbf{w}_{A,(x,t)}^{(n-1)}.$$
 (48)

The primary advantage of the serial-parallel update approach for solving subproblem (36) lies in distributing computational tasks, fully leveraging the computational capabilities of EDUs and reducing computational complexity. Additionally, it balances convergence speed while ensuring algorithm stability, making it more practical. The specific algorithm is shown in Algorithm 2.

## <span id="page-10-0"></span>Algorithm 3 PDBCD Algorithm for Solving (11)

**Input:** Set i = 0, initialize feasible points  $\{\alpha_D, \mathbf{u}_D, \mathbf{W}\}^{(0)}$ ,  $\{\boldsymbol{\alpha}_{\mathrm{U}},\mathbf{p}_{\mathrm{U}},\mathbf{V}\}^{(0)}$ 1: repeat

- 2: EDU updates  $V^{(i)}$  according to fixed  $\{\mathbf{p}_{\mathrm{U}},\mathbf{W}\}^{(i-1)}$  using Algorithm 1.
- 3: EDU updates  $\{ \boldsymbol{\alpha}_{\rm D}, {\bf u}_{\rm D}, {\bf W} \}^{(i)}$  according to fixed  ${\bf p}_{\rm U}{}^{(i-1)}$ using Algorithm 2.
- 4: CCU updates  $\{\mathbf{p}_{\mathrm{U}}\}^{(i)}$  according to fixed  $\{\boldsymbol{\alpha}_{\mathrm{D}}, \mathbf{u}_{\mathrm{D}}, \mathbf{V}\}^{(i)}$  and  $\{\boldsymbol{\alpha}_{\mathrm{U}}\}^{(i-1)}$  using (51).
- 5: CCU updates  $\{\boldsymbol{\alpha}_{\text{U}}\}^{(i)}$  according to fixed  $\{\mathbf{p}_{\text{U}},\mathbf{V}\}^{(i)}$  and  $\{\mathbf{W}\}^{(i)}$  using (52).
- 6: Set i = i + 1
- 7: until The objective function no longer changes.

**Output:** Optimal solution  $\{\alpha_D^\star, \mathbf{u}_D^\star, \mathbf{W}^\star, \alpha_U^\star, \mathbf{p}_U^\star, \mathbf{V}^\star\}$ 

## <span id="page-10-4"></span>Algorithm 4 Greedy Search Algorithm for Solving (11)

**Input:** Initialize mode selection vectors  ${\bm \mu}_{\rm D}^{(0)}$  and  ${\bm \mu}_{\rm U}^{(0)}$ 

- 1: for  $m \in \mathcal{M}$  do
- 2: According to  $\mu_{\mathrm{D}}^{m-1}$ , complete transceiver design using **Algorithm 3**, and calculate the uplink and downlink sum rate  $R_0^{(m)}$
- 3: Flip the *m*-th element of  $\mu_{\rm D}^{m-1}$ , complete transceiver design using Algorithm 3, and calculate the uplink and downlink sum rate  $R_1^{(m)}$ 4: Compare  $R_0^{(m)}$  and  $R_1^{(m)}$ , select the better mode, and
- update  $\mu_{\mathrm{D}}^{m}$  and  $\mu_{\mathrm{U}}^{m}$
- 5: end for

**Output:** Optimized mode selection vectors  $\mu_{\rm D}$  and  $\mu_{\rm U}$ 

#### <span id="page-10-1"></span>D. Centralized Solution for Subproblem 3

After subproblem 2 converges internally, the next step is to fix  $\{\alpha_{\rm D},u_{\rm D},W\},~\{\alpha_{\rm U},V\}$  and solve the following subproblem at CCU for centralized optimization of  $p_{\rm U}$ .

$$\min_{\mathbf{p}_{\mathrm{U}}} \quad f_{3}\left(\mathbf{p}_{\mathrm{U}}\right), \tag{49a}$$
s.t.  $(8d)$   $(49b)$ 

s.t. 
$$(8d)$$
 (49b)

where  $f_3(\boldsymbol{p}_U) = \sum\limits_{k=1}^K \alpha_{\mathrm{D},k} |u_{\mathrm{D},k}|^2 \sum\limits_{j=1}^J \beta_{\mathrm{IUI},kj} p_{\mathrm{U},j} + \chi_{\mathrm{U}}(\boldsymbol{p}_U).$  To simplify the process, let the optimization variable  $\rho_{\mathrm{U},j} = 0$ 

 $\sqrt{p_{\mathrm{U},j}}$ . Setting the partial derivative to 0, i.e.,  $\frac{\partial f(\rho_{\mathrm{U},j})}{\partial \rho_{\mathrm{U},j}} = 0$ , yields the local optimal solution for any uplink UE j, (50) and (51), as shown at the bottom of the next page.

Finally, fix  $\{\alpha_D, u_D, W\}$ ,  $\{p_D, V\}$ , V is no longer treated as a random variable and substitute it into (10) to compute the MSE for uplink UE j and update  $\alpha_{\rm U}$ ,

<span id="page-10-3"></span>
$$\alpha_{\mathrm{U},j} = \frac{1}{e_{\mathrm{U},j}\left(\mathbf{v}_{j}, \mathbf{p}_{\mathrm{U}}, \mathbf{W}\right)}.$$
 (52)

At this point, all optimization variables have been updated, the specific algorithm is shown in Algorithm 3.

### E. Greedy Search for AP Duplex Mode Selection

The above joint optimization is executed under a given AP duplex mode, due to constraint (8g), duplex mode selection

![](_page_11_Figure_2.jpeg)

<span id="page-11-2"></span>Fig. 3. CDF of relative optimality gap for different mode selection schemes (M=10, X=2, K=J=3, 300 channel realizations).

problem becomes a 0-1 integer programming problem. We propose a simple greedy search algorithm [49], [50], with the specific implementation process as follows.

First, a random duplex mode is selected for M APs. Then, APs are traversed sequentially from index 1 to M. For the mode selection vector  $\mu_D$ , a bit-flipping strategy is adopted to select the optimal mode for the currently traversed AP. If the current AP in downlink transmission brings a higher sum rate to the overall system compared to uplink reception, the corresponding position in  $\mu_{\rm D}$  is set to 1, and the corresponding position in  $\mu_{II}$  is set to 0, and so on. It can be observed that our algorithm can be completed within M optimizations, significantly reducing complexity. The specific algorithm is shown in Algorithm 4.

The computational complexity of the greedy algorithm is  $\mathcal{O}(M \cdot T_{\text{PDBCD}})$ , where  $T_{\text{PDBCD}} = \mathcal{O}(\bar{Z}^3 + \bar{Z}^2(K+J) + KJ)$ denotes the per-iteration complexity of the PDBCD solver due to matrix inversions, with  $\bar{Z}$  being the average number of APs per EDU. This is significantly lower than the exhaustive search complexity of  $\mathcal{O}(2^M \cdot T_{\text{PDBCD}})$ , making the algorithm practical for large-scale deployments.

To validate the near optimality, Fig. 3 compares the CDF of relative optimality gap for five mode selection schemes on a small scale network (M = 10, X = 2, K = J = 3) where exhaustive enumeration is tractable. The proposed greedy search algorithm achieves a median gap below 5% from the exhaustive optimum, with over 90% of instances within 10% of optimal. The one step local search provides only marginal improvement, confirming that the greedy solution is already near a local optimum. Tabu search achieves comparable

<span id="page-11-3"></span>TABLE I SIMULATION PARAMETERS

| Parameter                                                                                   | Value                    |
|---------------------------------------------------------------------------------------------|--------------------------|
| Number of APs (M)                                                                           | 48                       |
| Number of EDUs $(X)$                                                                        | 4                        |
| Number of DL/UL UEs $(K/J)$                                                                 | 6 (default), 4–8 (swept) |
| Antennas per AP $(N)$                                                                       | 1 (default), 1–5 (swept) |
| TAP Power Threshold                                                                         | 30 dBm                   |
| Uplink UE Power Threshold                                                                   | 20 dBm                   |
| Path Loss                                                                                   | 128.1+37.6log10(d)       |
| Rayleigh Fading                                                                             | 0 dB                     |
| Shadow Fading                                                                               | 8 dB                     |
| Noise Power ( $\sigma^2 = \sigma_{\mathrm{D},k}^2 = \sigma_{\mathrm{U},j}^2, \forall k,j$ ) | -104 dBm                 |

![](_page_11_Figure_10.jpeg)

<span id="page-11-6"></span><span id="page-11-5"></span><span id="page-11-4"></span>Fig. 4. Outer Loop Convergence.

performance, validating that our approach is competitive with more sophisticated metaheuristics.

#### IV. SIMULATION RESULTS AND PERFORMANCE ANALYSIS

In this section, we validate the effectiveness of the proposed PDBCD transceiver design and greedy search duplex mode selection scheme through simulations. We consider a simulation scenario with a radius of 200m. To ensure good coverage, 48 half-duplex APs are uniformly distributed on a circle and randomly associated with 4 EDUs. Six singleantenna downlink UEs and six single-antenna uplink UEs are uniformly distributed within the circle. We assume that the residual interference power between EDUs is equal, i.e.,  $\sigma_{\text{IAL},xx'}^2 = \Delta \sigma^2, \forall x, x'.$  Unless otherwise stated, the channel model and other parameters used in the simulation are given in Table I, where d represents the distance in meters.

First, we validate the convergence of the proposed PDBCD algorithm, using the EMMSE receiver as the initial iteration i = 0. Fig. 4 shows the relationship between SE and the number of outer loop iterations. It can be observed that

<span id="page-11-1"></span>(51)

<span id="page-11-0"></span>
$$\rho_{\mathrm{U},j}^{\star} = \min \left( \frac{\alpha_{\mathrm{U},j} \mathcal{R} \left\{ \sum_{x=1}^{X} \boldsymbol{v}_{xj}^{\mathrm{H}} \boldsymbol{h}_{\mathrm{U},xj} \right\}}{\left( \sum_{k=1}^{K} \alpha_{\mathrm{D},k} |u_{\mathrm{D},k}|^{2} \beta_{\mathrm{IUI},kj} + \sum_{j'=1}^{J} \alpha_{\mathrm{U},j'} \left| \sum_{x=1}^{X} \boldsymbol{v}_{xj'}^{\mathrm{H}} \boldsymbol{h}_{\mathrm{U},xj} \right|^{2} \right), \sqrt{p_{\mathrm{UE}}}} \right),$$

$$p_{\mathrm{U},j}^{\star} = \left( \rho_{\mathrm{U},j}^{\star} \right)^{2}.$$
(50)

![](_page_12_Figure_2.jpeg)

Fig. 5. Convergence of precoding updates with varying EDU numbers.

<span id="page-12-0"></span>![](_page_12_Figure_4.jpeg)

<span id="page-12-1"></span>Fig. 6. Time required vs. number of EDUs.

the PDBCD algorithm exhibits good convergence, achieving convergence within 2-3 iterations. As SI increases, the number of iterations required for convergence slightly increases.

Next, we investigated the relationship between the downlink sum rate and the number of inner-loop iterations of the PDBCD algorithm. As shown in Fig. [5,](#page-12-0) with an increasing number of EDUs, the number of iterations required for the proposed hybrid serial-parallel update scheme also increases, lying between the fully serial and fully parallel update schemes. When the number of EDUs is 4, convergence is achieved within 12 iterations, and the performance approaches that of the serial update scheme. Combined with Fig. [6,](#page-12-1) it can be observed that the serial update requires the longest time, while the parallel update requires the least. However, in practical applications, the poor convergence of the parallel update increases the signaling overhead between EDUs and CCU. Therefore, the proposed hybrid serial-parallel update scheme in the inner loop achieves a balance between performance, time and signaling overhead, further validating the effectiveness of the PDBCD algorithm.

Fig. [7](#page-12-2) compares the SE of four duplexing schemes as a function of residual interference power ∆ under both Wrap-around and PPP deployments, where G-NAFD represents NAFD with greedy mode selection, R-NAFD represents NAFD with random mode selection. The results show that the SE of G-NAFD, R-NAFD and CCFD schemes increases with improved IAI suppression, while TDD remains constant as it does not experience IAI. When ∆ ≤ −50 dB, the SE of

![](_page_12_Figure_9.jpeg)

<span id="page-12-2"></span>Fig. 7. Spectral efficiency vs. residual IAI level (∆) under Wrap-around and PPP deployments with i.i.d. and geometry-dependent IAI models.

![](_page_12_Figure_11.jpeg)

<span id="page-12-3"></span>Fig. 8. Spectral efficiency vs. number of UEs (K = J) under Wrap-around and PPP deployments.

G-NAFD and R-NAFD stabilizes. When ∆ ≥ −30 dB and ∆ ≥ −35 dB, R-NAFD and CCFD schemes are significantly affected by strong IAI, resulting in performance lower than TDD. The geometry-dependent IAI model provides more realistic performance estimates than the i.i.d. model. Wraparound deployment consistently outperforms PPP. The greedy scheme effectively mitigates the impact of IAI across all deployment scenarios, making it more practical.

Fig. [8](#page-12-3) examines the relationship between the number of UEs and the SE of four duplexing schemes when ∆ = −45 dB under both Wrap-around and PPP deployments. Assuming K = J, the total number of UEs is K +J. It can be observed that the SE of all duplexing schemes increases monotonically with the number of UEs under both scenarios. Wrap-around deployment consistently provides higher SE than PPP across all user counts due to the boundary-free torus topology. Notably, increasing the number of UEs leads to stronger CLI. This result demonstrates that the proposed PDBCD scheme effectively manages CLI in G-NAFD, R-NAFD and CCFD schemes under both practical deployment scenarios.

Fig. [9](#page-13-0) shows the relationship between the SE and the number of antennas per AP, N, when ∆ = −45 dB under both Wrap-around and PPP deployments. It can be observed that

![](_page_13_Figure_2.jpeg)

<span id="page-13-0"></span>Fig. 9. Spectral efficiency vs. number of AP antennas (N) under Wrap-around and PPP deployments.

![](_page_13_Figure_4.jpeg)

<span id="page-13-1"></span>Fig. 10. CDF of spectral efficiency for different transceiver schemes under PPP deployment.

increasing the number of AP antennas significantly improves system performance under both scenarios. TDD saturates earlier and achieves diminishing returns for  $N \geq 3$ , while NA-FD schemes continue to benefit from additional antennas. This is because additional antennas provide extra spatial degrees of freedom to suppress interference between different devices, and NA-FD schemes leverage this capability more effectively than TDD. Based on the above analysis, we conclude that the proposed PDBCD algorithm with greedy search achieves higher system gains and effectively addresses the CLI challenge faced by NA-FD under both practical deployment scenarios.

Fig. 10 compares the cumulative distribution functions (CDF) of SE for different transceiver schemes in NA-FD when  $\Delta=-45\,\mathrm{dB}$  under PPP deployment. EDU-MMSE represents MMSE transceiver relying on the estimated channel of EDU, CPU-MMSE represents centralized transceiver design, PDBCD-NO represents the case where all uplink receivers are EMMSE receivers, PDBCD-TEAM represents the case where all EDUs are non-sharing, PDBCD-HALF represents the case where half of EDUs are sharing, and PDBCD-FULL represents

![](_page_13_Figure_8.jpeg)

<span id="page-13-2"></span>Fig. 11. Sum-rate vs. maximum AP transmit power  $P_{\rm AP}^{\rm max}$  for nine schemes ( $M=48,~X=4,~K=J=6,~N=1,~\Delta=-45\,{\rm dB}$ ).

the case where all EDUs are sharing. G denotes greedy duplex mode selection. Fully distributed transceivers perform poorly, while fully centralized designs provide higher gains when CLI is high. The information sharing hierarchy is clearly validated, confirming the benefit of inter-EDU cooperation. Additionally, CPU-MMSE scheme does not effectively allocate uplink power, the downlink performance is degraded. The proposed GPDBCD scheme demonstrates significant advantages over existing schemes, while dynamically adjusting the number of sharing EDUs to balance the performance and the backhaul load.

<span id="page-13-3"></span>Fig. 11 compares ten schemes including proposed Greedy with FULL/HALF/NO EDU sharing, Mode Selection without sharing, Random/Fixed duplex modes, Centralized WMMSE, Pure DL-only baseline, and two representative methods from the literature: Half-Array [50] and SCA-based [51]. The results demonstrate that the proposed GPDBCD with FULL sharing achieves 132 bps/Hz, within 3 bps/Hz of the centralized upper bound (135 bps/Hz). EDU information sharing provides 2-4 bps/Hz gains per level. Compared with existing methods, the proposed scheme outperforms SCA-based [52] by 7 bps/Hz and Half-Array 11 bps/Hz. Random/Fixed modes achieve by 101–112 bps/Hz, approximately 20–30 bps/Hz below the proposed schemes. These results confirm near-optimal performance with distributed scalability while demonstrating clear advantages over existing methods.

<span id="page-13-4"></span>Fig. 12 presents the impact of the shared EDU count  $X_s$  on system performance. As  $X_s$  increases, the system achieves higher sum-rates and lower computation times, balanced against a linear increase in signaling overhead. This confirms that partial sharing provides an effective means to control the trade-off between spectral efficiency and system overhead.

To evaluate the practical impact of limited backhaul capacity, we conduct simulations under per-EDU backhaul constraints. The backhaul capacity  $C_{\rm BH}$  (in bps/Hz) bounds the total load at each EDU, including downlink data, uplink data, and CSI overhead.

![](_page_14_Figure_2.jpeg)

Fig. 12. Tri-view performance: sum-rate, signaling cost, and runtime versus the number of shared EDUs Xs (M = 48, X = 8, K = J = 6, N = 1).

<span id="page-14-19"></span>![](_page_14_Figure_4.jpeg)

<span id="page-14-20"></span>Fig. 13. Spectral efficiency vs. backhaul capacity per EDU (M = 48, X = 4, K = J = 6, N = 1, ∆ = −45 dB).

Fig. [13](#page-14-20) presents the spectral efficiency as a function of backhaul capacity per EDU, ranging from 40 to 140 bps/Hz. The results demonstrate that: (i) G-NAFD achieves superior performance across all backhaul capacities, reaching approximately 130 bps/Hz at CBH ≥ 100 bps/Hz; (ii) NA-FD schemes are more backhaul-efficient, with G-NAFD achieving 107 bps/Hz at CBH = 70 bps/Hz compared to only 64 bps/Hz for TDD (67% improvement); (iii) all schemes exhibit saturation for CBH ≥ 90 bps/Hz, indicating transition from backhaul-limited to interference-limited operation; (iv) greedy mode selection provides consistent 10–15 bps/Hz gains over random mode selection across all backhaul capacities. These results confirm that the proposed G-NAFD scheme efficiently utilizes limited backhaul resources while maintaining superior spectral efficiency.

## V. CONCLUSION

This paper investigates the distributed transceiver design and duplex mode selection in CF-RAN with NA-FD systems to maximize the sum rate. First, we establish the signal transmission model for both uplink and downlink in CF-RAN with NA-FD systems and derive the sum rate expression according to the transmission model, formulating the optimization objective function. Next, leveraging the MSE-SINR relationship, we transform the original non-convex rate maximization problem into a more tractable MSE minimization problem. Considering that distributed systems possess strong computational potential but also face information constraints, we propose a PDBCD algorithm for resource allocation and distributed transceiver design. This algorithm fully exploits the computing power of EDUs, significantly reducing CCU computational complexity while maintaining high scalability. Finally, simulation results demonstrate that compared to TDD, CCFD, R-NAFD, Half-Array [\[51\],](#page-15-31) SCA-based [\[52\],](#page-15-32) as well as fully distributed and fully centralized MMSE transceiver schemes, our proposed PDBCD algorithm with greedy search duplex mode selection achieves greater scalability and superior performance.

#### REFERENCES

- <span id="page-14-0"></span>[\[1\]](#page-0-0) C.-X. Wang et al., "On the road to 6G: Visions, requirements, key technologies, and testbeds," *IEEE Commun. Surveys Tuts.*, vol. 25, no. 2, pp. 905–974, 2nd Quart., 2023.
- <span id="page-14-1"></span>[\[2\]](#page-0-1) X. You et al., "Toward 6G *TK*µ extreme connectivity: Architecture, key technologies and experiments," *IEEE Wireless Commun.*, vol. 30, no. 3, pp. 86–95, Jun. 2023.
- <span id="page-14-2"></span>[\[3\]](#page-0-2) H. Q. Ngo, A. Ashikhmin, H. Yang, E. G. Larsson, and T. L. Marzetta, "Cell-free massive MIMO versus small cells," *IEEE Trans. Wireless Commun.*, vol. 16, no. 3, pp. 1834–1850, Mar. 2017.
- <span id="page-14-3"></span>[\[4\]](#page-0-3) E. Nayebi, A. Ashikhmin, T. L. Marzetta, H. Yang, and B. D. Rao, "Precoding and power optimization in cell-free massive MIMO systems," *IEEE Trans. Wireless Commun.*, vol. 16, no. 7, pp. 4445–4459, Jul. 2017.
- <span id="page-14-4"></span>[\[5\]](#page-0-4) S. Buzzi and C. D'Andrea, "Cell-free massive MIMO: User-centric approach," *IEEE Wireless Commun. Lett.*, vol. 6, no. 6, pp. 706–709, Dec. 2017.
- <span id="page-14-5"></span>[\[6\]](#page-0-5) X. You, D. Wang, and J. Wang, *Distributed MIMO and Cell-Free Mobile Communication*. Cham, Switzerland: Springer, 2021.
- <span id="page-14-6"></span>[\[7\]](#page-0-6) X. Zhang, W. Cheng, and H. Zhang, "Full-duplex transmission in phy and mac layers for 5G mobile wireless networks," *IEEE Wireless Commun.*, vol. 22, no. 5, pp. 112–121, Oct. 2015.
- <span id="page-14-7"></span>[\[8\]](#page-0-7) M. Matthaiou, O. Yurduseven, H. Q. Ngo, D. Morales-Jimenez, S. L. Cotton, and V. F. Fusco, "The road to 6G: Ten physical layer challenges for communications engineers," *IEEE Commun. Mag.*, vol. 59, no. 1, pp. 64–69, Jan. 2021.
- <span id="page-14-8"></span>[\[9\]](#page-0-8) Z. Zhang, K. Long, and A. V. Vasilakos, "Full-duplex wireless communications: Challenges, solutions, and future research directions," *Proc. IEEE*, vol. 104, no. 7, pp. 1369–1409, 2016.
- <span id="page-14-9"></span>[\[10\]](#page-0-9) S. K. Sharma, T. E. Bogale, L. B. Le, S. Chatzinotas, X. Wang, and B. Ottersten, "Dynamic spectrum sharing in 5G wireless networks with full-duplex technology: Recent advances and research challenges," *IEEE Commun. Surveys Tuts.*, vol. 20, no. 1, pp. 674–707, 1st Quart., 2017.
- <span id="page-14-10"></span>[\[11\]](#page-1-0) M. Duarte, C. Dick, and A. Sabharwal, "Experiment-driven characterization of full-duplex wireless systems," *IEEE Trans. Wireless Commun.*, vol. 11, no. 12, pp. 4296–4307, Dec. 2012.
- <span id="page-14-11"></span>[\[12\]](#page-1-1) A. Sabharwal, P. Schniter, D. Guo, D. W. Bliss, S. Rangarajan, and R. Wichman, "In-band full-duplex wireless: Challenges and opportunities," *IEEE J. Sel. Areas Commun.*, vol. 32, no. 9, pp. 1637–1652, Sep. 2014.
- <span id="page-14-12"></span>[\[13\]](#page-1-2) S. Goyal, P. Liu, and S. S. Panwar, "Full duplex cellular systems: Will doubling interference prevent doubling capacity?," *IEEE Commun. Mag.*, vol. 53, no. 5, pp. 121–127, 2015.
- <span id="page-14-13"></span>[\[14\]](#page-1-3) Z. He, W. Xu, H. Shen, D. W. K. Ng, Y. C. Eldar, and X. You, "Full-duplex communication for ISAC: Joint beamforming and power optimization," *IEEE J. Sel. Areas Commun.*, vol. 41, no. 9, pp. 2920–2936, Sep. 2023.
- <span id="page-14-14"></span>[\[15\]](#page-1-4) D. Wang, M. Wang, P. Zhu, J. Li, J. Wang, and X. You, "Performance of network-assisted full-duplex for cell-free massive MIMO," *IEEE Trans. Commun.*, vol. 68, no. 3, pp. 1464–1478, Mar. 2020.
- <span id="page-14-15"></span>[\[16\]](#page-1-5) J. Li, Q. Lv, P. Zhu, D. Wang, J. Wang, and X. You, "Network-assisted full-duplex distributed massive MIMO systems with beamforming training based CSI estimation," *IEEE Trans. Wireless Commun.*, vol. 20, no. 4, pp. 2190–2204, Apr. 2021.
- <span id="page-14-16"></span>[\[17\]](#page-1-6) M. Mohammadi, Z. Mobini, H. Quoc Ngo, and M. Matthaiou, "Ten years of research advances in full-duplex massive MIMO," *IEEE Trans. Commun.*, vol. 73, no. 3, pp. 1756–1786, Mar. 2025.
- <span id="page-14-18"></span><span id="page-14-17"></span>[\[18\]](#page-1-7) Y. Kim, H.-J. Moon, H. Yoo, B. Kim, K.-K. Wong, and C.-B. Chae, "A state-of-the-art survey on full-duplex network design," *Proc. IEEE*, vol. 112, no. 5, pp. 463–486, May 2024.

- [\[19\]](#page-1-8) X. Xia, P. Zhu, J. Li, D. Wang, Y. Xin, and X. You, "Joint sparse beamforming and power control for a large-scale DAS with network-assisted full duplex," *IEEE Trans. Veh. Technol.*, vol. 69, no. 7, pp. 7569–7582, Jul. 2020.
- <span id="page-15-0"></span>[\[20\]](#page-1-9) X. Xia et al., "Joint uplink power control, downlink beamforming, and mode selection for secrecy cell-free massive MIMO with networkassisted full duplexing," *IEEE Syst. J.*, vol. 17, no. 1, pp. 720–731, Mar. 2023.
- <span id="page-15-1"></span>[\[21\]](#page-1-10) M. Mohammadi, T. T. Vu, H. Q. Ngo, and M. Matthaiou, "Network-assisted full-duplex cell-free massive MIMO: Spectral and energy efficiencies," *IEEE J. Sel. Areas Commun.*, vol. 41, no. 9, pp. 2833–2851, Sep. 2023.
- <span id="page-15-2"></span>[\[22\]](#page-1-11) A. Chowdhury and C. R. Murthy, "Half-duplex APs with dynamic TDD versus full-duplex APs in cell-free systems," *IEEE Trans. Commun.*, vol. 72, no. 7, pp. 3856–3872, Jul. 2024.
- <span id="page-15-3"></span>[\[23\]](#page-1-12) X. Xia et al., "Joint user selection and transceiver design for cell-free with network-assisted full duplexing," *IEEE Trans. Wireless Commun.*, vol. 20, no. 12, pp. 7856–7870, Dec. 2021.
- <span id="page-15-4"></span>[\[24\]](#page-1-13) X. Xia, D. Wang, J. Zhao, Z. Zhang, and X. You, "Joint energy harvesting and transmission optimization for cell-free massive MIMO with network-assisted full duplexing," *IEEE Trans. Veh. Technol.*, vol. 72, no. 6, pp. 7439–7453, Jun. 2023.
- <span id="page-15-5"></span>[\[25\]](#page-1-14) G. Interdonato, E. Bjornson, H. Quoc Ngo, P. Frenger, and E. G. Lars- ¨ son, "Ubiquitous cell-free massive MIMO communications," *EURASIP J. Wireless Commun. Netw.*, vol. 2019, no. 1, pp. 1–13, Dec. 2019.
- <span id="page-15-6"></span>[\[26\]](#page-1-15) E. Bjornson and L. Sanguinetti, "Making cell-free massive MIMO ¨ competitive with MMSE processing and centralized implementation," *IEEE Trans. Wireless Commun.*, vol. 19, no. 1, pp. 77–90, Jan. 2020.
- <span id="page-15-7"></span>[\[27\]](#page-1-16) E. Bjornson and L. Sanguinetti, "Scalable cell-free massive MIMO ¨ systems," *IEEE Trans. Commun.*, vol. 68, no. 7, pp. 4247–4261, Jul. 2020.
- <span id="page-15-8"></span>[\[28\]](#page-1-17) D. Wang et al., "Full-spectrum cell-free RAN for 6G systems: System design and experimental results," *Sci. China Inf. Sci.*, vol. 66, no. 3, Mar. 2023, Art. no. 130305.
- <span id="page-15-9"></span>[\[29\]](#page-1-18) Y. Cao et al., "Implementation of a cell-free RAN system with distributed cooperative transceivers under ORAN architecture," *IEEE J. Sel. Areas Commun.*, vol. 43, no. 3, pp. 765–779, Mar. 2025.
- <span id="page-15-10"></span>[\[30\]](#page-1-19) Y. Guo et al., "Stochastic geometry analysis of scalable cell-free RAN with dynamic association and deployment," *IEEE J. Sel. Topics Signal Process.*, vol. 19, no. 2, pp. 398–411, Mar. 2025.
- <span id="page-15-11"></span>[\[31\]](#page-1-20) X. Li et al., "Joint uplink and downlink resource allocation for cellfree radio access network with network-assisted free duplex," in *Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops)*, Jun. 2024, pp. 834–839.
- <span id="page-15-12"></span>[\[32\]](#page-3-3) U. T. Demir, E. BjErnson, and L. Sanguinetti, "Foundations of usercentric cell-free massive MIMO," *Found. Trends Signal Process.*, vol. 14, nos. 3–4, pp. 162–472, Jan. 2021.
- <span id="page-15-13"></span>[\[33\]](#page-3-4) X. Xia, P. Zhu, J. Li, H. Wu, D. Wang, and Y. Xin, "Joint optimization of spectral efficiency for cell-free massive MIMO with networkassisted full duplexing," *Sci. China Inf. Sci.*, vol. 64, no. 8, pp. 1–16, Aug. 2021.
- <span id="page-15-14"></span>[\[34\]](#page-4-8) Q. Shi, M. Razaviyayn, Z.-Q. Luo, and C. He, "An iteratively weighted MMSE approach to distributed sum-utility maximization for a MIMO interfering broadcast channel," *IEEE Trans. Signal Process.*, vol. 59, no. 9, pp. 4331–4340, Sep. 2011.
- <span id="page-15-15"></span>[\[35\]](#page-4-9) D. P. Palomar, J. M. Cioffi, and M. A. Lagunas, "Joint Tx-Rx beamforming design for multicarrier MIMO channels: A unified framework for convex optimization," *IEEE Trans. Signal Process.*, vol. 51, no. 9, pp. 2381–2401, Sep. 2003.
- <span id="page-15-16"></span>[\[36\]](#page-4-10) S. Shi, M. Schubert, and H. Boche, "Downlink MMSE transceiver optimization for multiuser MIMO systems: MMSE balancing," *IEEE Trans. Signal Process.*, vol. 56, no. 8, pp. 3702–3712, Aug. 2008.
- <span id="page-15-17"></span>[\[37\]](#page-4-11) A. Abrardo, G. Fodor, M. Moretti, and M. Telek, "MMSE receiver design and SINR calculation in MU-MIMO systems with imperfect CSI," *IEEE Wireless Commun. Lett.*, vol. 8, no. 1, pp. 269–272, Feb. 2019.
- <span id="page-15-18"></span>[\[38\]](#page-4-12) S. Mashdour, A. R. Flores, S. Salehi, R. C. de Lamare, A. Schmeink, and P. R. B. da Silva, "Robust resource allocation in cell-free massive MIMO systems," *IEEE Trans. Commun.*, vol. 73, no. 8, pp. 5745–5759, Aug. 2025.
- <span id="page-15-19"></span>[\[39\]](#page-5-6) S. Boyd, "Distributed optimization and statistical learning via the alternating direction method of multipliers," *Found. Trends Mach. Learn.*, vol. 3, no. 1, pp. 1–122, 2010.
- <span id="page-15-21"></span><span id="page-15-20"></span>[\[40\]](#page-5-7) L. Miretti, E. Bjornson, and D. Gesbert, "Team MMSE precoding ¨ with applications to cell-free massive MIMO," *IEEE Trans. Wireless Commun.*, vol. 21, no. 8, pp. 6242–6255, Aug. 2022.

- [\[41\]](#page-5-8) Z. Hong, T. Li, C. Li, D. Wang, and X. You, "Group-joint MMSE complementary-based distributed uplink for cell-free massive MIMO," *IEEE Trans. Wireless Commun.*, vol. 23, no. 10, pp. 13648–13663, Oct. 2024.
- <span id="page-15-22"></span>[\[42\]](#page-5-9) Z. Hong, S. Xu, T. Li, C. Li, D. Wang, and X. You, "Robust cascaded team MMSE precoding for cell-free distributed downlink under hierarchical fronthaul," *IEEE Trans. Wireless Commun.*, vol. 23, no. 10, pp. 14515–14529, Oct. 2024.
- <span id="page-15-24"></span>[\[43\]](#page-7-7) Z. Wang, J. Zhang, E. Bjornson, and B. Ai, "Uplink performance of cell- ¨ free massive MIMO over spatially correlated Rician fading channels," *IEEE Commun. Lett.*, vol. 25, no. 4, pp. 1348–1352, Apr. 2021.
- <span id="page-15-25"></span>[\[44\]](#page-7-8) M. Bashar, P. Xiao, R. Tafazolli, K. Cumanan, A. G. Burr, and E. Bjornson, "Limited-fronthaul cell-free massive MIMO with local ¨ MMSE receiver under Rician fading and phase shifts," *IEEE Wireless Commun. Lett.*, vol. 10, no. 9, pp. 1934–1938, Sep. 2021.
- <span id="page-15-26"></span>[\[45\]](#page-9-7) J. Fu, Z. Mobini, H. Q. Ngo, P. Zhu, and M. Matthaiou, "WMMSEbased processing in cell-free massive MIMO systems," *IEEE Wireless Commun. Lett.*, vol. 14, no. 2, pp. 330–334, Feb. 2025.
- <span id="page-15-23"></span>[\[46\]](#page-6-4) S. Yuksel and B. Tamer, *Stochastic Networked Control Systems: Stabilization and Optimization Under Information Constraints*. Cham, Switzerland: Springer, 2013.
- <span id="page-15-27"></span>[\[47\]](#page-9-8) Z. Wang, J. Zhang, H. Q. Ngo, B. Ai, and M. Debbah, "Uplink precoding design for cell-free massive MIMO with iteratively weighted MMSE," *IEEE Trans. Commun.*, vol. 71, no. 3, pp. 1646–1664, Mar. 2023.
- <span id="page-15-28"></span>[\[48\]](#page-9-9) L. Miretti, R. L. G. Cavalcante, E. Bjornson, and S. Sta ¨ nczak, "UL-DL ´ duality for cell-free massive MIMO with per-AP power and information constraints," *IEEE Trans. Signal Process.*, vol. 72, pp. 1750–1765, 2024.
- <span id="page-15-29"></span>[\[49\]](#page-11-5) H. Liu, J. Zhang, X. Zhang, A. Kurniawan, T. Juhana, and B. Ai, "Tabusearch-based pilot assignment for cell-free massive MIMO systems," *IEEE Trans. Veh. Technol.*, vol. 69, no. 2, pp. 2286–2290, Feb. 2020.
- <span id="page-15-30"></span>[\[50\]](#page-11-6) Z. Hong, Y. Luo, and S. Na, "A joint spectral efficiency optimization algorithm based on greedy algorithm and improved PSO for cell-free massive MIMO networks," in *Proc. IEEE 100th Veh. Technol. Conf. (VTC-Fall)*, Oct. 2024, pp. 1–7.
- <span id="page-15-31"></span>[\[51\]](#page-13-3) H. V. Nguyen, V.-D. Nguyen, O. A. Dobre, Y. Wu, and O.-S. Shin, "Joint antenna array mode selection and user assignment for full-duplex MU-MISO systems," *IEEE Trans. Wireless Commun.*, vol. 18, no. 6, pp. 2946–2963, Jun. 2019.
- <span id="page-15-32"></span>[\[52\]](#page-13-4) Y. Zhu, J. Li, P. Zhu, H. Wu, D. Wang, and X. You, "Optimization of duplex mode selection for network-assisted full-duplex cell-free massive MIMO systems," *IEEE Commun. Lett.*, vol. 25, no. 11, pp. 3649–3653, Nov. 2021.

![](_page_15_Picture_36.jpeg)

Xinjiang Xia (Member, IEEE) received the B.S. and M.S. degrees in communication and information systems from Hohai University, China, in 2009 and 2012, respectively, and the Ph.D. degree from the National Mobile Communications Research Laboratory, Southeast University, Nanjing, China, in 2021. He is currently an Associate Professor with Purple Mountain Laboratories. From 2012 to 2016, he was a Software Development Engineer with China Postal Express and Logistics, Nanjing. His research interests include massive MIMO, cell-free, signal

processing, and distributed antenna systems.

![](_page_15_Picture_39.jpeg)

Yuhang Sun is currently pursuing the bachelor's degree with Nanjing University of Posts and Telecommunications, Nanjing, China. His research interests include massive MIMO, cell-free, space-airground integrated networks, and federated learning.

![](_page_16_Picture_2.jpeg)

Yunxiang Guo (Graduated Student Member, IEEE) received the B.S. degree in communication engineering from Zhengzhou University, China, in 2017, the M.S. degree in electronics and communications engineering from Hainan University, China, in 2020, and the Ph.D. degree in information and communication engineering from Southeast University, China, in 2025. He is currently a Lecturer with the School of Electronic Information, Luoyang Institute of Science and Technology, China. His research interests include cell-free massive MIMO, signal processing, and performance analysis.

![](_page_16_Picture_4.jpeg)

Dongming Wang (Member, IEEE) received the B.S. degree from Chongqing University of Posts and Telecommunications in 1999, the M.S. degree from Nanjing University of Posts and Telecommunications in 2002, and the Ph.D. degree from Southeast University, China, in 2006. In 2006, he joined the National Mobile Communications Research Laboratory, Southeast University, where he is currently a Professor. His research interests include signal processing for wireless communications and largescale distributed MIMO systems (cell-free massive

MIMO). He served as the Symposium Co-Chair for 2015 IEEE International Conference on Communications (ICC 2015) and IEEE Wireless Communications and Signal Processing Conference (IEEE WCSP 2017). He is an Associate Editor of *Science China Information Sciences*.

![](_page_16_Picture_7.jpeg)

Wenqi Zhao received the B.S. degree in communication and information systems from Hohai University, China, in 2023. She is currently pursuing the master's degree with Southeast University. Her research interests include massive MIMO, cell-free, marine signal transmission, and resource scheduling.

![](_page_16_Picture_9.jpeg)

Zhihao Gu received the M.S. degree in communication engineering from Southeast University, Nanjing, China, in 2025. During the graduate studies, he focused on wireless resource allocation and networkassisted full-duplex (NAFD) communications, with particular emphasis on spectrum efficiency optimization and interference management in next-generation wireless networks. He is currently a Communication Algorithm Engineer with Huawei Technologies Company Ltd., Shanghai, China, where he is engaged in research and development of advanced

wireless communication technologies.

![](_page_16_Picture_12.jpeg)

Xinyu Wang received the B.S. degree in telecommunications engineering from Nanjing University of Science and Technology, China, in 2023. She is currently pursuing the M.S. degree with Southeast University. Her research interests include cell-free massive MIMO systems and distributed antenna systems.

![](_page_16_Picture_14.jpeg)

Jiangzhou Wang (Fellow, IEEE) is a Professor with Southeast University, China. He has published more than 500 papers and five books. His research interests include mobile communications. He is an International Member of Chinese Academy of Engineering (CAE); and a fellow of the Royal Academy of Engineering (RAEng), U.K. He was a recipient of the 2024 IEEE Communications Society Fred W. Ellersick Prize and the 2022 IEEE Communications Society Leonard G. Abraham Prize. He was the Technical Program Chair of 2019 IEEE

International Conference on Communications (ICC2019), Shanghai; the Executive Chair of IEEE ICC2015, London; and the Technical Program Chair of IEEE WCNC2013.

![](_page_16_Picture_17.jpeg)

Xiaohu You (Fellow, IEEE) received the B.S., M.S., and Ph.D. degrees in electrical engineering from Nanjing Institute of Technology, Nanjing, China, in 1982, 1985, and 1989, respectively. From 1987 to 1989, he was with Nanjing Institute of Technology, as a Lecturer. Since 1990, he has been with Southeast University, first as an Associate Professor and later as a Professor. He is the Chief of the Technical Group of China 3G/B3G Mobile Communication Research and Development Project. His research interests include mobile communications,

adaptive signal processing, and artificial neural networks, with applications to communications and biomedical engineering. He received the Excellent Paper Prize from China Institute of Communications in 1987; the Elite Outstanding Young Teacher Awards from Southeast University in 1990, 1991, and 1993; and the 1989 Young Teacher Award of Fok Ying Tung Education Foundation, State Education Commission of China.
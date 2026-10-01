---
title: "Demand-Aware Versus Fixed Mode-Group and Modulation-Format Assignment Strategies for Few-Mode Fiber Optical Networks"
tema_principal: mode_fibers
temas_relacionados: []
ano: 2026
autores: []
veiculo: null
pdf: ../pdf/demand-aware_versus_fixed_mode-group_and_modulation-format_assignment_strategies_for_few-mode_fiber_optical_networks.pdf
---

![](_page_0_Picture_0.jpeg)

Received 4 June 2026, accepted 15 July 2026, date of publication 20 July 2026, date of current version 27 July 2026.

*Digital Object Identifier 10.1109/ACCESS.2026.3715065*

![](_page_0_Picture_3.jpeg)

# Demand-Aware Versus Fixed Mode-Group and Modulation-Format Assignment Strategies for Few-Mode Fiber Optical Networks

CATALINA CUEVAS-[ALI](https://orcid.org/0000-0001-8581-3411)AGA<sup>1</sup> , JUAN PI[NTO](https://orcid.org/0000-0003-2495-8929)-RÍOS [1](https://orcid.org/0000-0002-5177-2874) , ARIEL LEIV[A](https://orcid.org/0000-0001-8130-5399) <sup>1</sup> , ASTRID LOZAD[A](https://orcid.org/0000-0003-1596-3312) <sup>2</sup> , RICARDO OLIVARES <sup>2</sup> , NICOLÁS JARA <sup>2</sup> , (Member, IEEE), D[ANI](https://orcid.org/0000-0002-1084-1159)LO BÓRQUEZ-PAREDE[S](https://orcid.org/0000-0001-6590-2329) <sup>3</sup> , GABRIEL SAAVEDR[A](https://orcid.org/0000-0002-5450-3661) <sup>4</sup> , (Member[, IE](https://orcid.org/0000-0003-1423-1646)EE), IGNACIO DE MIGUEL <sup>5</sup> , (Senior Member, IEEE), AND RAMÓN J. DURÁN BARROSO <sup>5</sup>

Corresponding author: Ariel Leiva (ariel.leiva@pucv.cl)

This work was supported in part by ANID Doctorado Nacional under Grant 2022-21220867, in part by ANID FONDECYT under Grant 1241362, Grant 1250775, and Grant 1231826, in part by ANID AC3E CIA under Grant 250006, in part by DI-PUCV under Grant 039.773/2025, in part by ANID CTI Innovation Center for Sustainable Energy Transition (SET-Chile) under Grant 250019, and in part by MICIU/AEI/10.13039/501100011033 and by ERDF/EU under Grant PID2023-148104OB-C41.

**ABSTRACT** Few-Mode Fiber (FMF) networks based on Mode-Group Division Multiplexing (MGDM) introduce new challenges for dynamic resource allocation due to the trade-off between optical reach and transmission capacity across mode-group and modulation-format combinations. In this context, the Routing, Modulation, Mode-Group, and Wavelength Allocation (RMMWA) problem is affected by multidimensional resource overprovisioning under modal–spectral exclusivity constraints. This paper proposes a novel adaptive Demand-Aware Mode-Group and Modulation-Format Allocation (DA-MMA) strategy for MGDM-WDM optical networks and comparatively evaluates it against previously introduced reach-driven (RF-MMA) and capacity-driven (CF-MMA) strategies, as well as the perfect-fit baseline (BANG), under dynamic traffic conditions. Blocking probability and multidimensional overprovisioning are assessed across three representative topologies: UKNet, a length-extended UKNet, and a synthetic low-capacity 5-node network. Results show that performance is strongly topology-dependent. Capacitydriven prioritization achieves the largest blocking reduction in capacity-abundant networks, whereas in capacity-limited scenarios the proposed DA-MMA provides the best overall trade-off by jointly minimizing excess capacity and reach. When reach constraints dominate, performance differences narrow as physical feasibility becomes the primary limiting factor. Overall, no single allocation philosophy consistently provides the best performance; its effectiveness depends on the structural characteristics of the network.

**INDEX TERMS** Optical networks, few-mode, resource allocation, mode-group and modulation allocation.

## **I. INTRODUCTION**

Few-Mode Fiber (FMF) technology [\[1\]](#page-15-0) has emerged as a viable solution to increase the capacity of optical networks

The associate editor coordinating the review of this manuscript and approving it for publication was Fang Yang [.](https://orcid.org/0000-0003-3575-5086)

<span id="page-0-1"></span><span id="page-0-0"></span>beyond the limits of conventional single-mode wavelengthdivision multiplexing (WDM) [\[2\]. B](#page-15-1)y enabling the simultaneous transmission of multiple spatial modes within a single fiber, FMF-based Space Division Multiplexing (SDM) provides substantial capacity gains without requiring proportional expansion of the spectral domain. In this context,

<sup>1</sup>School of Electrical Engineering, Pontificia Universidad Católica de Valparaíso, Valparaíso 2370200, Chile

<sup>2</sup>Department of Electronic Engineering, Universidad Técnica Federico Santa María, Valparaíso 2390123, Chile

<sup>3</sup>Faculty of Engineering and Sciences, Universidad Adolfo Ibáñez, Viña del Mar 2520000, Chile

<sup>4</sup>Electrical Engineering Department, Universidad de Concepción, Concepción 4030000, Chile

<sup>5</sup>ETSI de Telecomunicación, Universidad de Valladolid, 47002 Valladolid, Spain

![](_page_1_Picture_1.jpeg)

Mode-Group Division Multiplexing (MGDM) represents a novel alternative for implementing SDM, complementing other well-established SDM paradigms based on Multi-Core Fibers (MCFs) and Multi-Fiber systems [\[3\]. O](#page-15-2)ne option to implement FMF systems is to use full digital Multiple-Input Multiple-Output (MIMO) signal processing, which enables the detection of all received spatial modes, even when significant intermodal crosstalk (IM-XT) is experienced [\[4\],](#page-15-3) [\[5\]. T](#page-15-4)his requires all spatial modes to follow the same physical path in order to be processed jointly at the receiver after coherent detection [\[4\],](#page-15-3) [\[5\], w](#page-15-4)hich, in a networking context, may be infeasible.

<span id="page-1-2"></span>Unlike previous full-MIMO SDM-FMF systems, Mode-Group Division Multiplexing (MGDM) [\[4\]](#page-15-3) has attracted increasing interest due to its ability to group strongly coupled modes, reducing the complexity of digital signal processing while preserving spatial multiplexing efficiency [\[5\].](#page-15-4) A mode-group is a set of spatial modes in a FMF that share similar propagation constants. Within a mode-group, individual modes experience significant intra-group coupling during fiber propagation, which makes their joint detection necessary; however, the inter-group crosstalk is theoretically weak [\[5\]. Th](#page-15-4)is mode-group organization allows the modes of the same group to be treated as a single spatial superchannel, propagating together along the same network path and being jointly detected with reduced-complexity or even no MIMO processing [\[4\],](#page-15-3) [\[5\],](#page-15-4) [\[6\]. At](#page-15-5) the same time, it enables different mode-groups to be independently multiplexed, routed, and switched within the network.

<span id="page-1-3"></span>In MGDM-WDM optical networks, connection provisioning requires the joint assignment of routes, wavelengths, modulation formats, and mode-groups, while accounting for physical-layer impairments [\[4\]](#page-15-3) such as differential mode delay, mode-dependent loss, IM-XT, and nonlinear effects. These impairments introduce a nontrivial trade-off between optical reach and transmission capacity across different mode-group and modulation-format combinations, making resource allocation a key challenge in dynamic network scenarios [\[5\]. In](#page-15-4) particular, in MGDM-WDM systems operating with a fixed maximum spectral bandwidth, each mode-group and modulation-format pair provides a predefined maximum transmission bitrate, referred to in this work as capacity, together with an associated optical reach. Consequently, depending on the bitrate demand and route length of a connection request, the selected configuration may introduce excess capacity and/or excess reach, leading to inefficient utilization of optical resources during the provisioning process. This multidimensional overprovisioning effect is inherent to MGDM-WDM systems due to the discrete nature of the available mode-group and modulation-format configurations. In contrast, such capacity overprovisioning does not inherently occur in Elastic Optical Networks (EONs), where the allocated spectral bandwidth can be dynamically adjusted according to the bitrate requirements of each connection request, leaving optical reach as the primary remaining source of potential overprovisioning.

<span id="page-1-5"></span><span id="page-1-4"></span><span id="page-1-1"></span><span id="page-1-0"></span>The resource allocation problem for establishing connections in MGDM-WDM networks is commonly formulated as the Routing, Modulation, Mode-Group, and Wavelength Allocation (RMMWA) problem [\[7\]. E](#page-15-6)arly solutions for the RMMWA problem rely on heuristics for the joint Mode-Group and Modulation-Format Allocation (MMA) process. The first MMA algorithm specifically proposed for MGDM-WDM networks is the Balanced Allocation of Mode-Group (BANG) algorithm [\[8\]. T](#page-15-7)his algorithm operates in an adaptive manner by explicitly considering the bit-rate requirement of each incoming connection request. In particular, it follows a perfect-fit philosophy, prioritizing mode-group and modulation-format pairs whose achievable capacity exactly matches the requested bitrate. While this demand-driven behavior enables tighter capacity allocation, it may also increase the blocking probability when no exact capacity match is available for a given request.

<span id="page-1-6"></span>To mitigate the potential increase in blocking probability and reduce the computational complexity associated with the adaptive perfect-fit behavior of BANG, alternative listsorting-based strategies have been proposed for the joint selection of mode-groups and modulation formats. In particular, the Reach-Sorted and Rate-Sorted algorithms [\[9\], pr](#page-15-8)eviously introduced by the authors, construct fixed prioritized lists based on a single physical attribute, namely supported optical reach or achievable bitrate, respectively. By avoiding per-request list construction and relaxing the strict perfect-fit condition, these methods offer lower computational complexity and improved operational simplicity. Moreover, they have demonstrated significant reductions in blocking probability compared to BANG across representative network scenarios.

Despite the recent emergence of MMA-based resource allocation schemes for MGDM-WDM networks, existing approaches still exhibit important limitations. Adaptive strategies such as BANG rely on strict perfect-fit capacity policies, which may significantly reduce the set of admissible configurations under dynamic operation. In contrast, previously proposed fixed-order approaches, such as Reach-Sorted and Rate-Sorted allocation, employ static prioritization policies that do not explicitly account for the bitrate and route-length requirements of each incoming connection request. Consequently, existing MMA schemes do not jointly optimize excess capacity and excess optical reach during the allocation process. To address these limitations, this paper introduces a new adaptive scheme named Demand-Aware Mode-Group and Modulation-Format Allocation (DA-MMA) for MGDM-WDM optical networks. Unlike fixed-order methods based on pre-established priority lists, and unlike BANG, which enforces an exact-capacity matching criterion, the proposed algorithm dynamically constructs, for each incoming connection request, a prioritized list of feasible mode-group and modulation-format pairs. The prioritization is governed by a weighted combination of capacity and reach overprovisioning, enabling a joint and tunable control of both resource dimensions. By explicitly accounting for excess capacity and excess reach during the

![](_page_2_Picture_1.jpeg)

ranking process, the proposed approach seeks to reduce resource waste and improve blocking performance under dynamic traffic conditions. Previous literature [10], [11] has already explored multidimensional prioritization strategies for resource allocation in both WDM and EON optical networks. However, to the best of our knowledge, the proposed DA-MMA algorithm constitutes the first approach of this type specifically designed for MGDM-WDM networks.

The main contributions of this work are summarized as follows:

- Demand-aware allocation: A novel connection-driven Mode-Group and Modulation-Format Allocation strategy (DA-MMA) for MGDM-WDM networks.
- Slack-based prioritization for DA-MMA: A formal multi-dimensional slack model that jointly quantifies excess capacity and excess reach, enabling a balanced and tunable prioritization mechanism within the proposed DA-MMA algorithm.
- Formalization of fixed allocation strategies: A unified and rigorous mathematical formulation of the previously proposed Reach-Sorted and Rate-Sorted algorithms, providing a consistent notation and an explicit permutation-based representation of their prioritized lists.
- Overprovisioning analysis: A quantitative assessment of capacity and reach overprovisioning induced by each allocation strategy, providing insights into their resource utilization efficiency under dynamic traffic conditions.

This paper is structured as follows: Section II presents the physical layer model, the network model and the main assumptions considered. Then, in Section III the RMMWA framework together with the fixed-order and demandaware allocation algorithms are described. Next, Section IV presents the performance of these approaches evaluated through simulation results. Finally, Section V summarizes the concluding remarks.

#### <span id="page-2-0"></span>**II. MODELS**

#### <span id="page-2-1"></span>A. PHYSICAL LAYER MODEL

We consider a MGDM-WDM optical network in which mode-groups are composed of linearly polarized (LP) modes that share similar normalized propagation constants. Figure 1 shows a simplified schematic of a link operating with MGDM technology for a system supporting two mode-groups. Modegroup  $g_1$  (MG- $g_1$ ) includes LP<sub>01</sub> mode, while mode-group  $g_2$  (MG- $g_2$ ) includes the degenerate LP<sub>11a</sub> and LP<sub>11b</sub> modes. On the transmitter side, WDM signals are generated independently for each LP-mode. Through the use of mode multiplexers (M MUX) mode-groups are formed, enabling mode-group-level routing. The link is composed of multiple FMF spans, each followed by few-mode erbium-doped fiber amplifiers (FM-EDFA), and interconnected through intermediate network nodes supporting MGDM capabilities. These MGDM nodes implement an all-optical architecture to switch, add, drop and bypass mode-groups at each <span id="page-2-3"></span><span id="page-2-2"></span>network node [4]. Mode demultiplexers (M DEMUX) allow mode-groups to be separated. On the receiver side, after the M DEMUX, the individual modes are recovered and, thanks to coherent detection, with reduced digital signal processing (DSP) complexity when compared to full MIMO systems that do not leverage mode-group structuring [5]. In this context, an optical connection is established at a specific wavelength in a given mode-group, which carries in parallel the bitrates of all LP modes belonging to the mode-group.

<span id="page-2-4"></span>Coupling among LP modes occurs within mode-groups, where intra-group modes exhibit strong coupling, while inter-group coupling is comparatively weak. This propagation regime is consistent with the intermediate-coupling approach [12], in which coupling matrices are introduced in short fiber sections to represent misaligned fiber splices. Using this physical-layer configuration, the optical reach values used in this study are based on the results reported in [8], considering specific modulation formats and quality-of-transmission constraints, as summarized in Table 4. The mathematical model adopted in [8], and detailed in [12], considers both linear and nonlinear physical-layer impairments, including attenuation, chromatic dispersion, crosstalk, mode-dependent loss, differential mode delay, and nonlinear effects arising from the Kerr phenomenon.

In the MGDM-WDM network under study, the modegroups supported per optical fiber are denoted by:

$$\mathcal{G} = \{g_1, g_2, \dots, g_G\} \tag{1}$$

where  $\mathcal{G}$  denotes a set, rather than numerical quantities, and each element is related to the mode-groups which are ordered from lowest to highest spatial order. Here, G represents the maximum number of mode-groups, with each group comprising one or more LP modes [4]. Various modulation schemes are assumed, and each mode-group can support M distinct modulation formats, ordered from the least to the most spectrally efficient. Similarly to set  $\mathcal{G}$ , the modulation format set is represented as:

$$\mathcal{M} = \{m_1, m_2, \dots, m_M\}. \tag{2}$$

The set of available Mode-Group and Modulation-Format pairs for establishing a connection is defined through a non-numerical matrix given by:

$$\mathbf{A} \triangleq \mathcal{G} \times \mathcal{M}. \tag{3}$$

The matrix **A** is organized such that each row is associated with a fixed element of  $\mathcal{G}$ , while each column is associated with a fixed element of  $\mathcal{M}$ . Accordingly, the (i, j)-th entry of **A** corresponds to the ordered pair  $(g_i, m_i)$ , where:

$$\mathbf{A}_{i,j} = \{(g_i, m_j): i = 1, \dots, G, j = 1, \dots, M\}.$$
 (4)

For clarity, the matrix A can be written explicitly as:

$$\mathbf{A} = \begin{bmatrix} (g_1, m_1) & (g_1, m_2) & \cdots & (g_1, m_M) \\ (g_2, m_1) & (g_2, m_2) & \cdots & (g_2, m_M) \\ \vdots & \vdots & \ddots & \vdots \\ (g_G, m_1) & (g_G, m_2) & \cdots & (g_G, m_M) \end{bmatrix}.$$
 (5)

<span id="page-3-1"></span>**FIGURE 1.** Schematic of a MGDM-WDM system with two mode-groups. Mode multiplexers (M MUX) allow the formation of mode-groups, while mode demultiplexers (M DEMUX) allow them to be separated. The dotted red rectangle represents a mode-group receiver. The link consists of few-mode fiber (FMF) spans followed by few-mode erbium-doped fiber amplifiers (FM-EDFA). Several intermediate MGDM nodes may be present along the link, providing switching as well as add and drop functionalities at the mode-group level.

Next, two numerical matrices are defined to represent different attributes for each pair in matrix **A**:

$$\mathbf{R} = [r_{i,j}] \in \mathbb{R}^{G \times M}, \quad r_{i,j} \leftrightarrow (g_i, m_j)$$
 (6)

$$\mathbf{C} = [c_{i,j}] \in \mathbb{R}^{G \times M}, \quad c_{i,j} \leftrightarrow (g_i, m_j)$$
 (7)

where matrices **R** and **C** represent the reach (in km) and maximum bitrate (in Gbps, considering the spectral spacing of the WDM grid and the reach) of each element in **A**, respectively. **For simplicity, hereafter in this paper, we refer to the maximum supported bitrate of each element in A as capacity.**

These parameters depend on the physical layer impairments present along the optical route as well as the characteristics of the selected modulation scheme. When the modulation format is fixed, a trade-off emerges between optical reach and transmission capacity across different mode-groups [\[5\],](#page-15-4) [\[8\]. Sp](#page-15-7)ecifically, lower-order mode-groups tend to offer longer optical reach, as they are composed of fewer LP modes and therefore suffer less from intergroup coupling. In contrast, the total transmission capacity of a mode-group increases with the number of LP modes, since each LP mode can independently transmit at the same bitrate [\[13\].](#page-15-12)

<span id="page-3-2"></span>In addition to these physical-layer considerations, resource allocation must also satisfy fundamental feasibility constraints inherent to transparent WDM systems with spatial multiplexing. First, the continuity constraint requires that a connection preserve the same wavelength along its entire route, ensuring end-to-end optical feasibility in the absence of wavelength conversion. Beyond this classical requirement, an additional constraint specific to MGDM-WDM architectures is introduced. While this constraint has been implicitly used in prior works [\[8\],](#page-15-7) [9] [thr](#page-15-8)ough operational rules, it has not been explicitly formalized or named. In this work, we refer to it as the Modal–Spectral Exclusivity Constraint (MSEC), which stipulates that no two connections may simultaneously occupy the same combination of wavelength and mode-group on a given link. By enforcing exclusivity in the mode–wavelength domain, the MSEC prevents collisions and ensures that mode-groups are not partially reused in ways that could compromise optical reach, capacity, or acceptable levels of inter-modal crosstalk. Together, these constraints ensure a consistent and conflict-free utilization of both spectral and spatial resources in few-mode fiber networks.

## B. NETWORK AND TRAFFIC MODELS

The network topology is represented as a graph 0 = (N ,L), where N denotes the set of network nodes and L represents the set of unidirectional links, containing *N* nodes and *L* links, respectively. Each link possesses an identical total capacity, defined by the number of available mode-groups and the number of carrier wavelengths allocated per mode-group.

Each connection request *c<sup>r</sup>* is defined by a triplet (*src*, *dst*, *b*), where *src* and *dst* denote the source and destination nodes, respectively, and *b* indicates the requested bitrate. Source-destination pairs are chosen according to a discrete uniform distribution. Similarly, the bitrate is drawn uniformly from a predefined set of values, denoted as B.

Connection requests are generated according to an exponential distribution with an inter-arrival rate λ, while the holding time of each connection also follows an exponential distribution, with a mean duration of 1/µ. The traffic intensity or offered load in the network is expressed as λ/µ and is measured in Erlangs.

## <span id="page-3-0"></span>**III. MODE-GROUP AND MODULATION-FORMAT ALLOCATION ALGORITHMS FOR MGDM-WDM**

The Routing, Modulation, Mode-Group and Wavelength Allocation (RMMWA) problem defines the set of operations required to establish a connection in an MGDM-WDM optical network. Specifically, in a sequential sense:

**Routing Allocation (RA):** selecting a candidate route between the source and destination nodes. In this work, the RA problem is solved by the well-known *K*-shortest path algorithm. Each candidate route is denoted by *p<sup>k</sup>* , with *k* = 1, . . . ,*K*.

**Modulation-Format Allocation (MFA):** choosing a modulation format compatible with the required bitrate and the physical reach of the candidate route.

![](_page_4_Picture_1.jpeg)

**Mode-Group Allocation (MGA):** selecting the spatial mode-group that will carry the signal.

**Wavelength Allocation (WA):** assigning an available wavelength across all links of the candidate route and Mode-Group and Modulation-Format candidate from previous stages, satisfying the continuity criterion and the MSEC constraint. In this work, the WA is solved using the wellknown First-Fit algorithm.

The MSEC constraint applied to MGDM-WDM networks inherently leads to resource waste or underutilization when a given RMMWA algorithm allocates optical resources to establish connections. This occurs because a connection request may require lower capacity and/or shorter reach than those provided by a selected mode-group and modulationformat pair, potentially increasing the blocking probability due to inefficient use of the assigned resources. To illustrate this phenomenon, Fig. [2](#page-5-0) presents a simplified example of the reach–capacity trade-off in the process of allocating a mode-group and modulation-format pair, considering a system with two mode-groups and three available modulation formats. Each green rectangular panel represents a candidate configuration (*gi*, *mj*), with *i* ∈ {1, 2} and *j* ∈ {1, 2, 3}, where the achievable reach *ri*,*<sup>j</sup>* and the supported capacity *ci*,*<sup>j</sup>* are compared against the demand requirements (*b*, *p<sup>k</sup>* ) of a connection request *c<sup>r</sup>* (the blue rectangular panel on the right). The green panels illustrate resource waste in terms of excess reach or capacity when the selected configuration provides transmission capabilities beyond those required by the route length or bitrate demand. The figure also presents well-matched allocations that exhibit no capacity waste (corresponding to configuration (*g*1, *m*1)) and no reach inefficiency (corresponding to configuration (*g*2, *m*2)). Finally, cases in which the achievable reach of a configuration is shorter than the candidate route length are depicted; in such situations, the allocation of the corresponding resource is not feasible.

The main distinction among RMMWA algorithms lies in how they choose the modulation format and modegroup, since routing and wavelength allocation are usually performed using typical criteria. Therefore, the contribution of this section focuses exclusively on the design and comparison of Mode-Group and Modulation-Format Allocation (MMA) strategies, while keeping routing and wavelength assignment fixed across all evaluated approaches to ensure a fair comparison.

To address the RMMWA problem in MGDM-WDM optical networks, we consider a general categorization of joint MMA algorithms into fixed and adaptive approaches, each reflecting a different philosophy for resource management in FMF-based systems. This classification captures two fundamentally distinct allocation paradigms based on [\[14\]:](#page-15-13) fixed approaches rely on precomputed and static priority orders of mode-group and modulation-format candidate pairs, whereas adaptive approaches dynamically construct priority lists on a per-request basis, tailoring the allocation decision to the characteristics of the incoming connection demand and, when applicable, to the instantaneous state of the network.

Each type of MMA algorithm, either fixed or adaptive, consists of two stages: an offline stage and an online stage. The offline stage is performed prior to network deployment and is responsible for preparing the information required for the MMA algorithm to operate during the online stage. The online stage corresponds to the MMA algorithm in operation when the network is active, embedded within an RMMWA algorithm, and is triggered each time a connection request arrives.

## A. ASPECTS REQUIRED FOR THE CONSTRUCTION OF PRIORITIZED LISTS

Fixed algorithms require the construction of a single prioritized list during the offline stage, which remains unchanged during network operation. In contrast, demandaware algorithms build a prioritized list for each incoming connection request, and therefore perform this process during the online stage.

Considering the matrix **A** of feasible mode-group and modulation-format pairs, with associated reach and capacity matrices **R** = [*ri*,*j*] and **C** = [*ci*,*j*], the index set is defined as:

$$\mathcal{I} \triangleq \{(i,j) : i = 1, \dots, G, j = 1, \dots, M\}.$$
 (8)

Each (*i*, *j*) ∈ I corresponds to the candidate pair **A***i*,*<sup>j</sup>* = (*gi*, *mj*) and its associated attributes (*ri*,*j*, *ci*,*j*). For fixed and adaptive approaches, prioritized lists of mode-group and modulation-format candidate pairs are constructed by defining a bijection π : 1, . . . , *GM* → I, which induces an ordering over all feasible pairs.

To facilitate the reading of the MMA formulations proposed in this section, Table [1](#page-5-1) is provided to summarize the notation associated with the mode-group and modulationformat pairs, the ordered sets and decision metrics used in the RF-MMA, CF-MMA, BANG and DA-MMA algorithms.

## B. FIXED-MMA ALGORITHMS

This category comprises algorithms that rely on a predefined and static allocation sequence during the MMA process, regardless of the characteristics of the incoming connection request. These methods systematically traverse a pre-ordered list of mode-group and modulation-format pairs, based on capacity, reach, or other criteria, and attempt to allocate resources accordingly.

Rather than aiming at global optimality, Fixed-MMA algorithms are conceived as low-complexity heuristics that explore representative points of the reach–capacity tradeoff inherent to MGDM–WDM systems. Their simplicity, predictability, and low computational overhead make them an attractive benchmark against more adaptive approaches.

The offline and online stages are described as follows:

<span id="page-4-0"></span>**Offline stage:** The offline stage of these algorithms mainly consists of constructing the prioritized list. Based on the attributes introduced in Section [II-A,](#page-2-1) i.e., the reach and capacity of each mode-group and modulation-format pair,

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

**FIGURE 2.** Illustrative example of reach-capacity trade-offs in the selection of mode-group and modulation format.

<span id="page-5-1"></span>**TABLE 1.** Summary of the main mathematical symbols used in the MMA formulations.

| Symbol            | Description                                                                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •                 |                                                                                                                                                                   |
| $\mathcal{I}$     | Index set containing all feasible mode-group and modulation-format pairs $(i,j)$ associated with the conceptual matrix ${\bf A}$ .                                |
| $\pi_R$           | Bijection defining the ordering of feasible pairs in the RF-MMA algorithm according to ascending optical reach and, secondarily, ascending capacity.              |
| $S_R$             | Reach-sorted prioritized list generated by RF-MMA using the ordering induced by $\pi_R$ .                                                                         |
| $r_{\pi_R(\ell)}$ | Optical reach associated with the $\ell\text{-th}$ element of the RF-MMA prioritized list.                                                                        |
| $c_{\pi_R(\ell)}$ | Transmission capacity associated with the $\ell\text{-th}$ element of the RF-MMA prioritized list.                                                                |
| $\pi_C$           | Bijection defining the ordering of feasible pairs in the CF-MMA algorithm according to ascending transmission capacity and, secondarily, ascending optical reach. |
| $S_C$             | Capacity-sorted prioritized list generated by CF-MMA using the ordering induced by $\pi_C$ .                                                                      |
| $r_{\pi_C(\ell)}$ | Optical reach associated with the $\ell\text{-th}$ element of the CF-MMA prioritized list.                                                                        |
| $c_{\pi_C(\ell)}$ | Transmission capacity associated with the $\ell\text{-th}$ element of the CF-MMA prioritized list.                                                                |
| A                 | Conceptual matrix containing all feasible mode-group and modulation-format pairs $(g_i, m_j)$ .                                                                   |
| $\mathbf{R}$      | Reach matrix whose entries $r_{i,j}$ represent the supported optical reach of each pair $(g_i, m_j)$ .                                                            |
| $\mathbf{C}$      | Capacity matrix whose entries $c_{i,j}$ represent the achievable transmission bitrate of each pair $(g_i, m_j)$ .                                                 |
| $r_{i,j}$         | Optical reach supported by the mode-group and modulation-format pair $(g_i,m_j)$ .                                                                                |
| $c_{i,j}$         | Transmission capacity supported by the mode-group and modulation-format pair $(g_i, m_j)$ .                                                                       |
| $\Delta c_{i,j}$  | Capacity slack, defined as the excess capacity allocated with respect to the requested bitrate.                                                                   |
| $\Delta r_{i,j}$  | Reach slack, defined as the excess optical reach allocated with respect to the candidate route length.                                                            |
| $F_{i,j}$         | Decision factor used in DA-MMA to jointly evaluate capacity and reach overprovisioning.                                                                           |
| $\beta, \gamma$   | Weighting coefficients controlling the relative importance of capacity and reach slack in the DA-MMA decision factor.                                             |

a prioritized list is constructed as an ordered version of the matrix **A**, according to a selected criterion. The resulting list constitutes a fundamental input for the MMA procedure executed during network operation.

A second important aspect for the operation of the MMA algorithms presented in this work is the precomputation of lengths for the different paths between each pair of network nodes.

**Online stage:** During network operation, Fixed-MMA algorithms adopt a First-Fit allocation policy using the prioritized list constructed in the offline stage.

For each incoming connection request, *c<sup>r</sup>* , the routing allocation (RA) stage provides a candidate route, which serves as input to the MMA stage. The MMA algorithm sequentially scans the prioritized list and selects the first mode-group and modulation-format pair that simultaneously satisfies the reach constraint (supported reach greater than or equal to the route length) and the capacity constraint (supported bitrate greater than or equal to the requested bitrate). If such a pair is found, it is passed to the wavelength assignment stage, which attempts to allocate an available wavelength (WA) following a first-fit policy while complying with the MSEC.

Since the online operation of all Fixed-MMA algorithms follows the same procedure, the remainder of this subsection focuses exclusively on the construction of the prioritized lists in the offline stage.

#### 1) RF-MMA: FIXED REACH-PRIORITIZED ALLOCATION

The RF-MMA algorithm [9] [em](#page-15-8)ploys a reach-prioritized list constructed offline. For this case, let π*<sup>R</sup>* : {1, . . . , *GM*} → I

![](_page_6_Picture_1.jpeg)

be a bijection such that, for  $\pi_R(\ell) = (i_\ell, j_\ell)$ , the sequence  $\{(r_{i_\ell,j_\ell}, c_{i_\ell,j_\ell})\}_{\ell=1}^{GM}$  is sorted lexicographically with primary key  $r_{i,j}$  (ascending) and secondary key  $c_{i,j}$  (ascending), i.e.,

$$(r_{i_{\ell},j_{\ell}}, c_{i_{\ell},j_{\ell}}) \leq_{\text{lex}} (r_{i_{\ell+1},j_{\ell+1}}, c_{i_{\ell+1},j_{\ell+1}}),$$
  
 $\forall \ell = 1, \dots, GM - 1.$  (9)

or, equivalently,

$$\pi_R(\ell) \prec \pi_R(q) \iff \left(r_{\pi_R(\ell)} < r_{\pi_R(q)} \text{ or } \right.$$

$$\left[r_{\pi_R(\ell)} = r_{\pi_R(q)} \land c_{\pi_R(\ell)} \le c_{\pi_R(q)}\right]\right)$$

$$\tag{10}$$

where  $r_{\pi_R(\ell)} \equiv r_{i_\ell,j_\ell}$  and  $c_{\pi_R(\ell)} \equiv c_{i_\ell,j_\ell}$ . The resulting reach-sorted prioritized list is:

$$S_{R} \triangleq (\mathbf{A}_{\pi_{R}(1)}, \mathbf{A}_{\pi_{R}(2)}, \dots, \mathbf{A}_{\pi_{R}(GM)})$$

$$= ((g_{i_{1}}, m_{j_{1}}), (g_{i_{2}}, m_{j_{2}}), \dots, (g_{i_{GM}}, m_{j_{GM}})).$$
(11)

In essence, RF-MMA follows a fixed reach-driven prioritization, where mode-group and modulation-format pairs are examined from shorter to longer reach, with capacity acting only as a tie-breaking attribute. In this way, the heuristic aims to establish connections while reducing reach-related resource waste.

#### 2) CF-MMA: FIXED CAPACITY-PRIORITIZED ALLOCATION

In CF-MMA [9], the offline prioritized list is constructed by sorting all feasible pairs according to capacity. For this case, let  $\pi_C: \{1,\ldots,GM\} \to \mathcal{I}$  be a bijection such that, for  $\pi_C(\ell) = (i_\ell,j_\ell)$ , the sequence  $\{(c_{i_\ell,j_\ell},r_{i_\ell,j_\ell})\}_{\ell=1}^{GM}$  is sorted lexicographically with primary key  $c_{i,j}$  (ascending) and secondary key  $r_{i,j}$  (ascending), i.e.,

$$(c_{i_{\ell},j_{\ell}}, r_{i_{\ell},j_{\ell}}) \leq_{\text{lex}} (c_{i_{\ell+1},j_{\ell+1}}, r_{i_{\ell+1},j_{\ell+1}}),$$
  
 $\forall \ell = 1, \dots, GM - 1.$  (12)

Equivalently,

$$\pi_C(\ell) \prec \pi_C(q) \iff \left(c_{\pi_C(\ell)} < c_{\pi_C(q)} \text{ or } \right]$$

$$\left[c_{\pi_C(\ell)} = c_{\pi_C(q)} \land r_{\pi_C(\ell)} \le r_{\pi_C(q)}\right]$$
(13)

where  $c_{\pi_C(\ell)} \equiv c_{i_\ell,j_\ell}$  and  $r_{\pi_C(\ell)} \equiv r_{i_\ell,j_\ell}$ . The resulting capacity-sorted prioritized list is:

$$S_{C} \triangleq (\mathbf{A}_{\pi_{C}(1)}, \mathbf{A}_{\pi_{C}(2)}, \dots, \mathbf{A}_{\pi_{C}(GM)})$$

$$= ((g_{i_{1}}, m_{j_{1}}), (g_{i_{2}}, m_{j_{2}}), \dots, (g_{i_{GM}}, m_{j_{GM}})).$$
(14)

In essence, CF-MMA follows a fixed capacity-driven prioritization, where mode-group and modulation-format pairs are examined from lower to higher capacity, with reach acting only as a tie-breaking attribute. In this way, the heuristic aims to establish connections while reducing capacity-related resource waste.

#### C. ADAPTIVE MMA ALGORITHMS

Adaptive MMA algorithms extend the Fixed-MMA paradigm by dynamically adapting the prioritization of mode-group and modulation-format pairs during network operation according to the requested bitrate and route length.

In this work, two adaptive strategies are considered for MGDM-WDM optical networks: the Balanced Allocation of Mode-Group (BANG) algorithm [8] and the proposed Demand-Aware MMA (DA-MMA) scheme.

BANG constitutes the first MMA-based resource allocation algorithm specifically proposed for MGDM-WDM networks [8]. It operates in a demand-driven manner by constructing, for each incoming connection request, a prioritized list restricted to capacity-matching configurations, thus following a strict perfect-fit (capacity-exact) criterion. While this adaptive behavior enables tight bitrate alignment, it may increase blocking probability when no exact-capacity configuration satisfies the reach constraints of a given request.

In contrast, the proposed DA-MMA generalizes the adaptive paradigm by introducing a multi-dimensional slack-aware prioritization mechanism. Rather than enforcing exact capacity matching, DA-MMA dynamically ranks feasible configurations according to a joint evaluation of capacity and reach overprovisioning. By explicitly minimizing the combined slack in both resource dimensions, the proposed approach seeks to improve the balance between resource utilization efficiency and blocking performance under dynamic traffic conditions.

Next, the offline and online stages of both adaptive algorithms are formally described.

**Offline stage:** In contrast to Fixed-MMA algorithms, both adaptive approaches considered in this work do not impose a predefined ordering over the conceptual matrix  $\mathbf{A}$  during the offline stage. Instead, the offline process is limited to the construction and storage of the attribute matrices  $\mathbf{R} = [r_{i,j}]$  and  $\mathbf{C} = [c_{i,j}]$ , which associate each feasible mode-group and modulation-format pair  $\mathbf{A}_{i,j} = (g_i, m_j)$  with its corresponding optical reach and capacity. These matrices constitute the common static input required by both adaptive MMA strategies to perform connection-aware decisions during network operation.

#### 1) DA-MMA: DEMAND-AWARE ALLOCATION

**Online stage:** The proposed algorithm dynamically constructs, for each incoming connection request, a dedicated prioritized list explicitly determined by the demand bitrate and route length.

Consider an incoming connection request,  $c_r$ , and a candidate path  $p_k$  (obtained from the preceding routing stage) with physical length  $d_k$ . The MMA first constructs the subset of feasible configurations that satisfy both capacity and reach constraints along  $p_k$ , given by

$$\mathcal{A}_{k}^{(c_r)} \triangleq \left\{ \mathbf{A}_{i,j} \in \mathbf{A} \mid c_{i,j} \ge b \land r_{i,j} \ge d_k \right\}. \tag{15}$$

![](_page_7_Picture_1.jpeg)

At this stage, no information related to the current spectral or modal occupancy of the network is considered. The set  $\mathcal{A}_k^{(c_r)}$  therefore represents the configurations that are physically feasible along the path  $p_k$  with respect to the requirements of the connection request only.

For each configuration  $\mathbf{A}_{i,j} \in \mathcal{A}_k^{(c_r)}$ , two non-negative slack variables are computed as:

$$\Delta c_{i,j} \triangleq c_{i,j} - b, \quad \Delta r_{i,j} \triangleq r_{i,j} - d_k.$$
 (16)

Simultaneous demand—distance decision factor: To jointly account for excess capacity and excess reach through a single sorting key, the MMA associates each feasible configuration with a scalar decision factor defined as:

$$F_{i,j} \triangleq \beta \, \bar{\Delta c_{i,j}} + \gamma \, \bar{\Delta r_{i,j}}, \quad \beta, \gamma \ge 0,$$
 (17)

where  $\bar{\Delta c}_{i,j}$  and  $\bar{\Delta r}_{i,j}$  denote normalized capacity and reach slacks, respectively. Specifically, normalization is performed over the finite configuration space **A** as:

$$\bar{\Delta c}_{i,j} \triangleq \frac{\Delta c_{i,j}}{c_{\max} - c_{\min}}, \quad \bar{\Delta r}_{i,j} \triangleq \frac{\Delta r_{i,j}}{r_{\max} - r_{\min}}, \quad (18)$$

with  $c_{\max} \triangleq \max_{(u,v) \in \mathcal{I}} c_{u,v}$ ,  $c_{\min} \triangleq \min_{(u,v) \in \mathcal{I}} c_{u,v}$ , and analogously for  $r_{\max}$  and  $r_{\min}$ . This normalization renders the decision factor dimensionless and ensures that both slack components contribute on a comparable scale, allowing the coefficients  $\beta$  and  $\gamma$  to explicitly control the relative importance of capacity and reach overprovisioning. The weighting parameters  $\beta$  and  $\gamma$  should be properly adjusted in order to identify the combination of both parameters that minimizes the blocking probability for each evaluated topology, since they directly determine the relative importance assigned to excess capacity and excess reach during the connection establishment process.

Rather than selecting a single configuration, the MMA constructs an ordered list by ranking the elements of  $\mathcal{A}_k^{(c_r)}$  according to increasing values of  $F_{i,j}$ , such that configurations exhibiting smaller combined slack are prioritized. In the event of identical decision-factor values, ties are deterministically resolved using a lexicographic ordering based on  $(\Delta c_{i,j}, \Delta r_{i,j})$ , i.e., configurations are first compared in terms of excess capacity, and only if equal, in terms of excess reach.

Let

$$\mathcal{I}_k^{(c_r)} \triangleq \{(i,j) \in \mathcal{I} : \mathbf{A}_{i,j} \in \mathcal{A}_k^{(c_r)}\}$$
 (19)

denote the index set of feasible mode-group and modulation-format pairs for request  $c_r$  along path  $p_k$ .

The resulting prioritization is formalized through a bijection

$$\pi_k^{(c_r)}: \{1, \dots, |\mathcal{I}_k^{(c_r)}|\} \to \mathcal{I}_k^{(c_r)},$$
 (20)

such that, for  $\pi_k^{(c_r)}(\ell)=(i_\ell,j_\ell)$ , the sequence  $\{F_{i_\ell,j_\ell}\}_{\ell=1}^{|\mathcal{I}_k^{(c_r)}|}$  is sorted in non-decreasing order, i.e.,

$$F_{i_{\ell},j_{\ell}} \le F_{i_{\ell+1},j_{\ell+1}}, \quad \forall \ell = 1, \dots, |\mathcal{I}_k^{(c_r)}| - 1.$$
 (21)

Equivalently,

$$\pi_k^{(c_r)}(\ell) \prec \pi_k^{(c_r)}(q) \iff F_{\pi_k^{(c_r)}(\ell)} < F_{\pi_k^{(c_r)}(q)}$$

$$\begin{split} \left[ F_{\pi_{k}^{(c_{r})}(\ell)} &= F_{\pi_{k}^{(c_{r})}(q)} \wedge (\Delta c_{\pi_{k}^{(c_{r})}(\ell)}, \Delta r_{\pi_{k}^{(c_{r})}(\ell)}) \\ &\leq_{\text{lex}} \dots (\Delta c_{\pi_{k}^{(c_{r})}(q)}, \Delta r_{\pi^{(c_{r})}(q)}) \right]. \end{split} \tag{22}$$

The resulting prioritized list for request  $c_r$  and path  $p_k$  is given by

$$S_k^{(c_r)} \triangleq \left( \mathbf{A}_{\pi_b^{(c_r)}(1)}, \mathbf{A}_{\pi_b^{(c_r)}(2)}, \dots, \mathbf{A}_{\pi_b^{(c_r)}(|\mathcal{I}_b^{(c_r)}|)} \right). \tag{23}$$

The list  $S_k^{(c_r)}$  is then passed to the WA module, which sequentially evaluates each candidate configuration along the path  $p_k$  following a First-Fit policy while enforcing wavelength continuity and the MSEC constraint.

The success or failure of a connection request is therefore determined exclusively by the WA process. If the assignment attempt fails for a given configuration due to resource unavailability, the WA requests the next configuration in the MMA-prioritized list. If wavelength assignment succeeds, the connection is immediately established. Otherwise, the algorithm proceeds to evaluate the next candidate route. A connection request is rejected only after all candidate paths have been evaluated without success.

#### 2) BANG: BALANCED ALLOCATION OF MODE-GROUP

**Online stage:** This baseline algorithm, proposed in [8], generates a dedicated prioritized list for each incoming connection request by retaining only *perfect-fit* configurations in terms of capacity, i.e., those whose achievable capacity exactly matches the requested bitrate.

Consider an incoming connection request,  $c_r$ , requiring bitrate b, and a candidate path  $p_k$  (obtained from the preceding routing stage) with physical length  $d_k$ . The MMA first constructs the subset of perfect-fit and reach-feasible configurations along  $p_k$  as:

$$\mathcal{A}_{k,\text{PF}}^{(c_r)} \triangleq \left\{ \mathbf{A}_{i,j} \in \mathbf{A} \mid c_{i,j} = b \land r_{i,j} \ge d_k \right\}. \tag{24}$$

At this stage, no information related to the current spectral or modal occupancy of the network is considered. The set  $\mathcal{A}_{k,\mathrm{PF}}^{(c_r)}$  therefore represents the configurations that perfectly match the demand capacity and are physically feasible along the path  $p_k$  with respect to the requirements of the connection request only.

For each configuration  $\mathbf{A}_{i,j} \in \mathcal{A}_{k,\mathrm{PF}}^{(c_r)}$ , the reach slack is computed as:

$$\Delta r_{i,j} \triangleq r_{i,j} - d_k \ge 0. \tag{25}$$

Note that, by construction,  $\Delta c_{i,j} \triangleq c_{i,j} - b = 0$  for all retained configurations.

Rather than selecting a single configuration, the MMA constructs an ordered list by ranking the elements of  $\mathcal{A}_{k,\text{PF}}^{(c_r)}$  according to increasing values of  $\Delta r_{i,j}$ , thus prioritizing the tightest reach-feasible perfect-fit options. In the event

![](_page_8_Picture_1.jpeg)

<span id="page-8-1"></span>TABLE 2. Online computational complexity of the MMA algorithms.

| Algorithm | Online Complexity per Request |
|-----------|-------------------------------|
| RF-MMA    | $\mathcal{O}(KGM)$            |
| CF-MMA    | $\mathcal{O}(KGM)$            |
| BANG      | $\mathcal{O}(KGM\log(GM))$    |
| DA-MMA    | $\mathcal{O}(KGM\log(GM))$    |

of identical reach-slack values, ties are deterministically resolved using a lexicographic ordering over (i, j).

Let

$$\mathcal{I}_{k,\text{PF}}^{(c_r)} \triangleq \{(i,j) \in \mathcal{I} : \mathbf{A}_{i,j} \in \mathcal{A}_{k,\text{PF}}^{(c_r)}\}$$
 (26)

denote the index set of perfect-fit mode-group and modulation-format pairs for request  $c_r$  along path  $p_k$ .

The resulting prioritization is formalized through a bijection

$$\pi_{k,\text{PF}}^{(c_r)}: \{1, \dots, |\mathcal{I}_{k,\text{PF}}^{(c_r)}|\} \to \mathcal{I}_{k,\text{PF}}^{(c_r)},$$
(27)

such that, for  $\pi_{k,\text{PF}}^{(c_r)}(\ell) = (i_\ell, j_\ell)$ , the sequence  $\{\Delta r_{i_\ell, j_\ell}\}_{\ell=1}^{|\mathcal{I}_{k,\text{PF}}^{(c_r)}|}$  is sorted in non-decreasing order, i.e.,

$$\Delta r_{i_{\ell},j_{\ell}} \le \Delta r_{i_{\ell+1},j_{\ell+1}}, \quad \forall \ell = 1,\dots, |\mathcal{I}_{k,\mathrm{PF}}^{(c_r)}| - 1.$$
 (28)

Equivalently,

$$\pi_{k,\mathrm{PF}}^{(c_r)}(\ell) \prec \pi_{k,\mathrm{PF}}^{(c_r)}(q) \iff \Delta r_{\pi_{k,\mathrm{PF}}^{(c_r)}(\ell)} < \Delta r_{\pi_{k,\mathrm{PF}}^{(c_r)}(q)}$$

$$\label{eq:rate_relation} \left[ \Delta r_{\pi_{k,\mathrm{PF}}^{(c_r)}(\ell)} = \Delta r_{\pi_{k,\mathrm{PF}}^{(c_r)}(q)} \quad \wedge \quad \pi_{k,\mathrm{PF}}^{(c_r)}(\ell) \preceq_{\mathrm{lex}} \pi_{k,\mathrm{PF}}^{(c_r)}(q) \right]. \tag{29}$$

The resulting prioritized list for request  $c_r$  and path  $p_k$  is given by

$$S_{k,\text{PF}}^{(c_r)} \triangleq \left( \mathbf{A}_{\pi_{k,\text{PF}}^{(c_r)}(1)}, \mathbf{A}_{\pi_{k,\text{PF}}^{(c_r)}(2)}, \dots, \mathbf{A}_{\pi_{k,\text{PF}}^{(c_r)}(|\mathcal{I}_{k,\text{PF}}^{(c_r)}|)} \right). \tag{30}$$

The list  $S_{k,PF}^{(c_r)}$  is then passed to the WA module, which sequentially evaluates each candidate configuration along the path  $p_k$  following a First-Fit policy while enforcing wavelength continuity and the MSEC constraint.

If the assignment attempt fails for a given configuration due to resource unavailability, the WA requests the next configuration in the MMA-prioritized list. If wavelength assignment succeeds, the connection is immediately established. Otherwise, the algorithm proceeds to evaluate the next candidate route. A connection request is rejected only after all candidate paths have been evaluated without success.

#### D. COMPUTATIONAL COMPLEXITY ANALYSIS

The computational complexity analysis presented in this work focuses exclusively on the online operation of the Mode-Group and Modulation-Format Allocation (MMA) stage, since routing allocation and wavelength assignment are identical for all evaluated algorithms and therefore do not affect the relative comparison among MMA strategies.

Let G denote the number of available mode-groups and M the number of supported modulation formats. Consequently, the configuration space contains GM candidate mode-group and modulation-format pairs. In addition, let K denote the maximum number of candidate routes evaluated per connection request.

For RF-MMA and CF-MMA, the prioritized list of (g, m) pairs is precomputed offline and remains fixed during network operation. Therefore, upon the arrival of a connection request, the MMA stage sequentially scans the prioritized list and verifies the reach and capacity constraints associated with each candidate pair for a given candidate route. In the worst case, all GM configurations must be evaluated for each candidate route.

Hence, the online computational complexity of RF-MMA and CF-MMA is given by

$$\mathcal{O}(KGM)$$
. (31)

In contrast, DA-MMA dynamically constructs a dedicated prioritized list for each incoming connection request and candidate route. First, the algorithm scans the complete configuration space to identify the feasible (g, m) pairs satisfying both reach and capacity constraints. Then, the corresponding slack variables and decision factors are computed for each feasible configuration. Finally, the feasible configurations are sorted according to the decision factor. In the worst-case scenario, all GM configurations are feasible, such that the sorting stage dominates the overall computational cost.

Therefore, the online computational complexity of DA-MMA is given by

$$\mathcal{O}(KGM\log(GM)).$$
 (32)

Similarly, BANG dynamically constructs and sorts a request-dependent prioritized list during online operation. Therefore, its asymptotic complexity is equivalent to that of DA-MMA, i.e.,

$$\mathcal{O}(KGM\log(GM)).$$
 (33)

Table 2 summarizes the online computational complexity of the evaluated MMA algorithms.

Although DA-MMA introduces additional online processing compared to fixed approaches due to the dynamic construction and sorting of the prioritized list, the computational overhead remains moderate because the size of the configuration space *GM* is typically limited in practical MGDM-WDM systems.

#### <span id="page-8-0"></span>IV. PERFORMANCE OF MMA ALGORITHMS

This section presents a performance evaluation of the four MMA algorithms considered in this paper in terms of blocking probability and capacity and reach overprovisioning, with particular emphasis on their behavior under different network topology scenarios. The analysis is conducted over three representative network topologies: the UKNet topology, an extended version of UKNet in which the link lengths are

![](_page_9_Picture_1.jpeg)

**TABLE 3.** Summary of the network characteristics of the topologies considered in this work.

<span id="page-9-0"></span>

| Parameter                           | UKNet  | Extended-UKNet | 5-node synthetic |
|-------------------------------------|--------|----------------|------------------|
| Number of nodes $(N)$               | 21     | 21             | 5                |
| Number of links $(L)$               | 78     | 78             | 12               |
| Network density $(\alpha)$          | 0.18   | 0.18           | 0.6              |
| Shortest link (km)                  | 11     | 27.5           | 100              |
| Longest link (km)                   | 463    | 1157.5         | 450              |
| Average link length (km)            | 138.21 | 345.51         | 275              |
| Shortest route $(k = 1)$ (km)       | 11     | 27.5           | 100              |
| Longest route $(k = 1)$ (km)        | 771    | 1927.5         | 800              |
| Average route length $(k = 1)$ (km) | 288.81 | 722.04         | 371.58           |

scaled by a factor of 2.5, and a synthetic five-node network. These three network topologies differ in size and density (α), where α = *L*/[*N*(*N* − 1)], and their main characteristics are summarized in Table [3.](#page-9-0)

The network topologies are selected such that, for every possible source–destination pair, the length of the shortest route does not exceed the maximum optical reach supported by at least one mode-group and modulation-format pair. This design choice ensures that all connection requests have the potential to be established in a fully optical manner and are not inherently blocked by reach constraints, without requiring the use of optoelectronic regeneration. The chosen topologies enable a comparative assessment between wide-area networks and highly connected scenarios, thereby facilitating a robust evaluation under diverse operating conditions.

The analysis is organized into two main parts: the Simulation Setup, which outlines the parameters and assumptions used, and the Performance Results and Analysis, where the main outcomes are reported and the factors driving the behavior of each algorithm are discussed. Taken together, these sections provide a comprehensive assessment of how the proposed demand-aware strategies compare with fixed-order approaches in terms of blocking probability and optical resource utilization efficiency.

## A. SIMULATION SETUP

<span id="page-9-1"></span>To evaluate the performance of the proposed MMA algorithms, the C++ Flex Net Sim event-driven simulator library [\[15\], i](#page-15-14)ncluding its SDM-oriented event module [\[16\],](#page-15-15) was employed to model dynamic MGDM-WDM network scenarios. The proposed MMA algorithms operate within a sequential RMMWA framework, in which the routing stage is based on a *K*-shortest path strategy with *K* = 3. The *K* shortest routes for each source–destination pair are computed offline prior to the simulation process and are commonly used by all evaluated algorithms. Furthermore, wavelength assignment is performed using the First-Fit policy.

Regarding the physical layer parameters, Table [4](#page-10-0) summarizes the optical reach and achievable bitrate (capacity) associated with each mode-group and modulation format combination, evaluated under a bit error rate (BER) threshold of 4 · 10−<sup>3</sup> prior to Forward Error Correction. These reach values, originally reported in [\[8\], w](#page-15-7)ere obtained under a worst-case operating scenario in which each mode-group supports 81 wavelength channels, corresponding to full C-band occupancy (1530–1565 nm) with a WDM channel spacing of 50 GHz. The optical reach was determined from the minimum signal-to-noise ratio (SNR) threshold required by each modulation format, considering the LP mode with the lowest SNR within the corresponding mode-group. The physical-layer model accounts for both linear and nonlinear impairments in the intermediate-coupling regime and FM-EDFA amplification.

Table [5](#page-11-0) summarizes the simulation parameters adopted in this study, encompassing physical-layer characteristics, traffic-related settings, and network-level configuration parameters. In addition, the specific values of β and γ used by the DA-MMA algorithm for the different evaluated topologies are also included.

#### B. PERFORMANCE RESULTS AND ANALYSIS

This section presents the performance evaluation of the proposed Demand-Aware Mode-Group and Modulation- Format Allocation (DA-MMA) algorithm by analyzing its blocking probability and capacity and reach overprovisioning across representative network topologies, namely UKNet, extended-UKNet, and the synthetic 5-node network. The results are compared against the baseline Balanced Allocation of Mode-Group (BANG) algorithm [\[8\], as](#page-15-7) well as the fixed-order CF-MMA and RF-MMA strategies [\[9\].](#page-15-8)

#### 1) UKNET TOPOLOGY

According to the parameters reported in Table [3,](#page-9-0) the UKNet topology (Fig. [3.\(a\)\)](#page-10-1) exhibits a high capacity to accommodate connection requests, mainly due to its relatively large number of links (78) and its network density of α = 0.3. On the other hand, the optical reach supported by the mode-group and modulation-format pairs considered in this work ranges from 600 km to 2200 km as shown Table [4.](#page-10-0) As a result for this topology, route lengths do not appear to constitute a limiting factor for the evaluated resource allocation algorithms.

<span id="page-9-2"></span>Figure [3.\(b\)](#page-10-1) reports the blocking probability for the UKNet topology under increasing offered load for the BANG, RF-MMA, CF-MMA and DA-MMA (β = 1 and γ = 0.2) resource allocation algorithms. The figure also includes 95% confidence intervals computed using the Wilson score interval method implemented in the Flex Net Sim library [\[15\]. E](#page-15-14)ach simulation point was obtained from 10<sup>6</sup> stochastic connection requests. All methods exhibit the expected monotonic increase in blocking probability as the offered load grows; however, significant performance differences arise among the evaluated techniques. Capacitybased fixed MMA algorithm (CF-MMA) and DA-MMA achieve the best overall performance across the entire load range, followed by RF-MMA, and finally, the baseline BANG algorithm under low traffic conditions. As the network approaches the saturation regime, the performance gap among CF-MMA, RF-MMA, and DA-MMA narrows, as they exhibit nearly identical blocking behavior while still outperforming BANG. RF-MMA, CF-MMA and DA-MMA

![](_page_10_Picture_1.jpeg)

**TABLE 4.** Optical reach and bitrate per Mode-Group for different modulation formats [\[8\], ba](#page-15-7)sed on a bit error rate (BER) threshold of 4 · 10−<sup>3</sup> before forward error correction.

<span id="page-10-0"></span>

| mode-groups set $(G)$        | $m_1: \mathbf{C}$ | PSK            | $m_2: 16$        | -QAM           | $m_3: 64$        | -QAM           |
|------------------------------|-------------------|----------------|------------------|----------------|------------------|----------------|
| $(g_1 + g_2 + g_3)$          | $C_{g,m}$ [Gbps]  | $R_{g,m}$ [km] | $C_{g,m}$ [Gbps] | $R_{g,m}$ [km] | $C_{g,m}$ [Gbps] | $R_{g,m}$ [km] |
| $g_1 (LP_{01})$              | 100               | 2200           | 200              | 2100           | 300              | 900            |
| $g_2 (LP_{11-a/b})$          | 200               | 1300           | 400              | 1200           | 600              | 700            |
| $g_3 (LP_{02}, LP_{21-a/b})$ | 300               | 900            | 600              | 800            | 900              | 600            |

<span id="page-10-1"></span>![](_page_10_Figure_4.jpeg)

**FIGURE 3.** (a) UKNet topology, (b) blocking probability as a function of the offered load (Erlangs), and (c) frequency histograms illustrating the distribution of capacity waste (left) and reach waste (right) for successfully established connections at 1700 Erlangs.

algorithms focus on establishing connections while minimizing resource overprovisioning in terms of capacity or optical reach, either through pre-established prioritization strategies or by explicitly considering demand characteristics. In contrast, the baseline algorithm (BANG) exhibits the poorest performance due to its strict perfect-fit capacity criterion. By prioritizing only exact-capacity configurations, BANG intentionally discards alternative feasible options that involve capacity overprovisioning, seeking to preserve higher-capacity mode-group and modulation-format pairs for future connection requests with larger bitrate demands. However, this avoidance strategy significantly reduces the set of admissible configurations for each request, thereby increasing the likelihood of connection blocking. As a result, BANG attains the highest blocking probability among the evaluated schemes.

Figure [3.\(c\)](#page-10-1) presents histograms of the resource waste corresponding to the connections successfully established by the different MMA algorithms under a traffic load of 1700 Erlangs. The results show that CF-MMA, DA-MMA and BANG tend to concentrate on lower levels of capacity waste, whereas RF-MMA is characterized by reduced reach

![](_page_11_Picture_1.jpeg)

**TABLE 5.** Simulation parameters.

<span id="page-11-0"></span>

| Parameters                          | Value                                          |
|-------------------------------------|------------------------------------------------|
| Physical layer parameters           |                                                |
| Mode-Group set $\mathcal{G}$        | $g_1:(LP_{01})$                                |
|                                     | $g_2:(LP_{11a}, LP_{11b})$                     |
|                                     | $g_3:(LP_{02}, LP_{21a}, LP_{21b})$            |
| Modulation formats set $M$          | QPSK, 16-QAM, 64-QAM                           |
| Number of Wavelengths               | 81 per Mode-Group                              |
| Capacities and optical reaches      | Described in Table 4                           |
| Network and Traffic parameters      |                                                |
| Topologies                          | UKNet, Extended-UKNet, Synthetic 5-Node        |
| Bitrate set $B$                     | [100, 200, 300, 400, 600] Gbps                 |
| Traffic model                       | Poisson process                                |
| Offered load range (UKNet, E-UKNet) | [1000 to 3000] Erlangs                         |
| Offered load range (5-Node)         | [600 to 1500] Erlangs                          |
| Number of connection requests       | 10 <sup>6</sup> requests for each simulation   |
| Resource allocation algorithms      |                                                |
| Baseline MMA algorithm              | BANG [8]                                       |
| Proposed MMA algorithms             | RF-MMA and CF-MMA Fixed-Algorithms             |
|                                     | and DA-MMA Adaptive-Algorithm                  |
| $\beta$ and $\gamma$ values         | UKNet: $(\beta = 1, \gamma = 0.2)$             |
|                                     | UKNet-extended: $(\beta = 0.75, \gamma = 1)$   |
|                                     | Synthetic 5-node: $(\beta = 0.15, \gamma = 1)$ |

waste values. It can also be observed that BANG, due to its strict perfect-fit strategy in terms of capacity, does not generate capacity waste values other than zero. This behavior reflects its avoidance-oriented allocation policy, which systematically selects configurations with minimum excess capacity. However, despite eliminating capacity overprovisioning, this strategy does not translate into a higher number of successfully established connections compared to the other algorithms.

Overall, for this topology, characterized by high traffic-carrying capability and the absence of significant reach limitations due to its route lengths, MMA algorithms that prioritize efficient capacity utilization (with the exception of BANG strict avoidance policy) deliver superior performance in the transient operating region of the network, i.e., before saturation is reached.

## 2) EXTENDED-UKNET TOPOLOGY

To stress the MMA algorithms considered in this work, the UKNet-extended topology (Fig. [4.\(a\)\)](#page-12-0) is employed. While this topology preserves the density characteristics of the original UKNet, scaling the link lengths by a factor of 2.5 increases the relevance of optical reach constraints. As a result, this modified topology still exhibits a high capacity to accommodate connection requests, but with route lengths that ensure each connection can at least be established over its shortest candidate route (i.e., *k* = 1) using at least one feasible (*g*, *m*) pair. More specifically, since the lengths of the shortest routes range from 27.5 km to 1927.5 km, the (*g*1, *m*1) and (*g*1, *m*2) pairs can be assigned to establish at least the shortest route for any source–destination pair in the network.

Figure [4.\(b\)](#page-12-0) presents the blocking probability for this extended topology. In contrast to the original UKNet case, significantly higher blocking probability values are observed for all algorithms. This degradation is primarily attributed to reach limitations, as the feasible space of *K*-shortest paths becomes considerably reduced under longer link distances. Among the evaluated methods, BANG exhibits a relatively high blocking probability, which can be attributed to its avoidance-oriented strategy that enforces a strict perfect-fit selection of configurations, potentially limiting the establishment of other connection requests. It is worth noting from Fig. [4.\(b\)](#page-12-0) that the CF-MMA, RF-MMA, and DA-MMA (β = 0.75 and γ = 1) algorithms exhibit nearly identical values and therefore appear superimposed in the blocking probability plot.

Figure [4.\(c\)](#page-12-0) presents histograms of the resource waste corresponding to the connections successfully established under a traffic load of 1700 Erlangs. The aggregate frequency across all bins reveals that BANG achieves the lowest number of successfully established connections among the evaluated algorithms. For this topology, characterized by significantly longer link distances, the histograms provide additional insight into the behavior of each strategy. RF-MMA, by prioritizing configurations with minimal reach slack, tends to allocate lower-order mode-groups that offer longer optical reach but reduced transmission capacity. As a consequence, higher-capacity mode-groups remain available only in limited scenarios, which may deteriorate the allocation opportunities for future connection requests requiring both high capacity and extended reach. This effect is reflected in an increased capacity waste distribution. CF-MMA exhibits an analogous behavior from the capacity perspective. By minimizing capacity slack, it frequently selects configurations with higher spectral efficiency but shorter reach, resulting in larger reach waste values. In a topology where feasible route lengths are already constrained by reach limitations, this behavior can negatively impact the acceptance of subsequent long-distance connection requests. DA-MMA, which represents a balanced trade-off between reach- and capacity-driven prioritization, produces a broader distribution of both capacity and reach waste. While this joint consideration mitigates extreme overprovisioning in a single dimension, it may still limit the availability of optimal configurations for future requests under severe reach constraints. In this particular extended topology, BANG exhibits typical behavior, as its strict perfect-fit capacity policy and avoidance of overprovisioned allocations limit its ability to increase the number of successfully established connections, resulting in the worst performance among all evaluated algorithms.

## 3) SYNTHETIC 5-NODES TOPOLOGY

To create a low-capacity network scenario in terms of traffic-carrying capability, a synthetic five-node network is considered, as shown in Fig. [5.\(a\),](#page-13-0) whose main characteristics are reported in Table [3.](#page-9-0) This topology is intended to stress the algorithms in terms of efficient capacity allocation across the different mode groups and modulation formats. For this reason, the range of the offered load is adjusted to lower values than those considered for the UKNet topology, in order to avoid analyzing only saturation conditions.

Figure [5.\(b\)](#page-13-0) illustrates the blocking probability for the synthetic 5-node topology. In this scenario, DA-MMA

![](_page_12_Picture_1.jpeg)

<span id="page-12-0"></span>![](_page_12_Figure_2.jpeg)

**FIGURE 4.** (a) Extended-UKNet topology, (b) blocking probability as a function of the offered load (Erlangs), and (c) frequency histograms illustrating the distribution of capacity waste (left) and reach waste (right) for successfully established connections at 1700 Erlangs.

(β = 0.15 and γ = 1) achieves the best overall performance, followed by CF-MMA. Both algorithms outperform RF-MMA by nearly one order of magnitude at low traffic loads (below 1100 Erlangs) and exhibit similar performance as the network approaches the saturation region (above 1400 Erlangs). In contrast, BANG shows the poorest performance across the entire traffic range, including the saturation regime, where its blocking probability remains nearly one order of magnitude higher than that of the bestperforming algorithms.

Figure [5.\(c\)](#page-13-0) presents histograms of the resource waste corresponding to the connections successfully established under a traffic load of 1200 Erlangs. It can be clearly observed that CF-MMA and DA-MMA achieve a higher number of established connection requests. In particular, CF-MMA exhibits a distribution strongly concentrated around the minimum capacity waste values, indicating its strict prioritization of near-perfect capacity fits. In contrast, DA-MMA shows a broader distribution; however, the frequency gradually decreases as both capacity and reach waste move away from zero. This behavior reflects its joint consideration of both resource dimensions within the decision factor. Conversely, RF-MMA presents higher occurrences at larger capacity waste values, which helps explain its higher blocking probability compared to CF-MMA and DA-MMA. This observation is consistent with its allocation policy, which prioritizes the minimization of reach slack, as can also be appreciated in the corresponding reach-waste histogram. On the other hand, BANG yields the poorest performance across the traffic range due to its avoidance-oriented policy. By strictly selecting configurations that perfectly match the requested capacity, it refrains from allocating slightly overprovisioned resources, which becomes detrimental in a topology already stressed in terms of capacity.

Overall, for this topology, characterized by limited trafficcarrying capability, MMA algorithms that prioritize efficient capacity utilization (with the exception of the strict avoidance policy of BANG) achieve superior performance.

## 4) QUANTITATIVE PERFORMANCE GAIN OVER THE BASELINE

<span id="page-12-1"></span>To quantify the performance gains in terms of blocking probability, we employ the Blocking Improvement Ratio (BIR) defined in [\[17\]. T](#page-15-16)his metric captures the relative reduction

<span id="page-13-0"></span>![](_page_13_Figure_2.jpeg)

**FIGURE 5.** (a) Synthetic 5-node topology, (b) blocking probability as a function of the offered load (Erlangs), and (c) frequency histograms illustrating the distribution of capacity waste (left) and reach waste (right) for successfully established connections at 1200 Erlangs.

in Connection Blocking Probability (CBP) achieved by the proposed MMA algorithms with respect to the BANG baseline:

$$BIR(\%) = \frac{CBP_{\text{base}} - CBP_{\text{prop}}}{CBP_{\text{base}}} \times 100$$
 (34)

Here, *CBP*base denotes the blocking probability under the BANG baseline algorithm, while *CBP*prop corresponds to the blocking probability of the evaluated MMA algorithm (DA-MMA, CF-MMA, or RF-MMA). Higher BIR values indicate greater performance improvement.

The resulting BIR values are reported in Table [6](#page-14-1) for representative offered traffic loads of 1700 Erlangs in the UKNet-based topologies and 1200 Erlangs in the 5-node synthetic topology.

The quantitative results summarized in Table [6](#page-14-1) provide clear evidence that the relative performance of MMA strategies is strongly topology-dependent. In the UKNet topology, characterized by high traffic-carrying capability and negligible reach limitations, capacity-driven prioritization (CF-MMA and DA-MMA considering β = 1 and γ = 0.2) achieves the largest blocking reduction (99%), followed by RF-MMA (80%). This indicates that, in capacityabundant scenarios without significant reach limitations, minimizing capacity overprovisioning is the dominant factor in reducing blocking probability.

In contrast, under severe reach constraints as in the Extended-UKNet topology, all evaluated strategies achieve identical relative gains (approximately 25%). This convergence reveals that when optical reach becomes the primary limiting factor, the feasible configuration space is significantly restricted, thereby reducing the impact of different prioritization philosophies.

For the capacity-limited 5-node synthetic topology, the proposed DA-MMA achieves the highest performance gain (95%), slightly outperforming CF-MMA (92%) and RF-MMA (85%). This result confirms that jointly accounting for excess capacity and excess reach through a slack-balanced prioritization mechanism provides a more robust allocation strategy when both resource dimensions interact under constrained conditions.

![](_page_14_Picture_1.jpeg)

<span id="page-14-1"></span>**TABLE 6.** BIR: Percentage reduction in blocking probability relative to the baseline BANG algorithm for each evaluated topology.

| Topology         | DA-MMA | CF-MMA | RF-MMA |
|------------------|--------|--------|--------|
| UKNet            | 99%    | 99%    | 80%    |
| Extended-UKNet   | 27%    | 25%    | 25%    |
| 5-node synthetic | 95%    | 92%    | 85%    |

Overall, these results demonstrate that no single allocation philosophy is universally optimal. Instead, the effectiveness of a given MMA strategy depends on the structural bottleneck of the network. Capacity-driven schemes are preferable in capacity-dominated regimes, whereas balanced slack-aware approaches exhibit superior robustness in heterogeneous or resource-constrained scenarios.

#### C. DISCUSSION AND PRACTICAL IMPLICATIONS

The results obtained across the evaluated topologies reveal that the effectiveness of MMA strategies is strongly governed by the interaction between network topology, traffic conditions, and physical-layer constraints.

In capacity-abundant and well-connected networks, minimizing capacity overprovisioning is the dominant factor in reducing blocking probability, which explains the strong performance of capacity-driven strategies such as CF-MMA and DA-MMA considering β = 1 and γ = 0.2. In these scenarios, optical reach constraints are rarely binding; therefore, efficient spectrum utilization becomes the key optimization objective.

Conversely, when optical reach becomes a limiting factor, as in the extended-UKNet topology, the performance differences among allocation strategies tend to diminish. This indicates that, under strong physical-layer constraints, the feasible configuration space is significantly restricted, and therefore the impact of the allocation policy itself is inherently limited. In such cases, improvements at the physical layer may be more effective than further optimization of allocation strategies.

In capacity-constrained scenarios, such as the synthetic 5-node topology, adaptive approaches such as DA-MMA provide the best overall performance by balancing capacity and reach overprovisioning. This highlights the importance of demand-aware allocation mechanisms in environments where resource scarcity and traffic heterogeneity dominate.

Overall, these findings suggest that no single MMA strategy is universally optimal. Instead, the selection of an allocation policy should be aligned with the network's structural characteristics. This opens the possibility of adaptive or hybrid control schemes capable of dynamically adjusting allocation strategies based on real-time network conditions.

## <span id="page-14-0"></span>**V. CONCLUSION**

This paper presented a comparative assessment of fixed-order and demand-aware Mode-Group and Modulation-Format Allocation (MMA) strategies for MGDM-WDM Few-Mode Fiber networks under dynamic traffic conditions. In addition to evaluating existing reach-driven (RF-MMA), capacitydriven (CF-MMA), and perfect-fit (BANG) heuristics, a novel Demand-Aware MMA (DA-MMA) algorithm was proposed. The study explicitly analyzed blocking probability and multidimensional resource overprovisioning, jointly accounting for excess capacity and excess reach induced by the Modal–Spectral Exclusivity Constraint.

Simulation results across three representative topologies with distinct structural characteristics demonstrated that algorithm performance is strongly topology-dependent. In networks with high traffic-carrying capability and negligible reach limitations, capacity-efficient strategies such as CF-MMA and DA-MMA consistently achieved the lowest blocking probability, while strict perfect-fit approaches (BANG) exhibited reduced flexibility and higher blocking due to their avoidance policy.

When optical reach constraints become dominant, as in the Extended-UKNet scenario, the feasible configuration space is significantly restricted by physical limitations. Under this regime, the performance gap among prioritization strategies narrows, as reach feasibility becomes the primary driver of allocation decisions. This convergence indicates that, when the network operates close to its reach limits, the impact of different allocation philosophies is inherently reduced.

In capacity-limited scenarios, such as the synthetic 5-node topology, the proposed DA-MMA (based on joint slack minimization) provided the best overall trade-off between blocking performance and resource utilization. By simultaneously accounting for excess capacity and excess reach, the algorithm achieved superior robustness under constrained resource conditions, outperforming both reach-driven and strict capacity-preserving strategies.

Overall, the results indicate that no single allocation philosophy is universally superior in terms of performance. Instead, the relative relevance of reach-aware and capacityaware prioritization depends on the structural characteristics of the network. Capacity-driven schemes are preferable in capacity-dominated regimes, whereas balanced slack-aware approaches provide enhanced robustness when multiple resource dimensions interact. These findings offer design insights for the development of adaptive RMMWA strategies capable of dynamically adjusting their prioritization criteria according to real-time network conditions.

Future work will consider extending the proposed algorithm to heterogeneous network scenarios, including elastic optical networks and flex-grid architectures, as well as evaluating the impact of wavelength conversion and 3R regeneration. In addition, future research will explore MMA algorithms that explicitly consider the link occupation state across the network during the allocation process. Further research will also investigate the application of AI/ML-based strategies to algorithms such as DA-MMA, with the objective of optimizing or potentially replacing existing decision mechanisms through intelligent models. Moreover, new algorithmic variants derived from DA-MMA may emerge from this line of investigation, thereby extending the applicability,

![](_page_15_Picture_1.jpeg)

adaptability, and efficiency of the proposed MGDM-WDM framework within the broader context of intelligent optical networking and autonomous resource allocation.

#### **REFERENCES**

- <span id="page-15-0"></span>[\[1\] K](#page-0-0).-i. Kitayama and N.-P. Diamantopoulos, ''Few-mode optical fibers: Original motivation and recent progress,'' *IEEE Commun. Mag.*, vol. 55, no. 8, pp. 163–169, Aug. 2017.
- <span id="page-15-1"></span>[\[2\] H](#page-0-1). Waldman, ''The impending optical network capacity crunch,'' in *Proc. SBFoton Int. Opt. Photon. Conf. (SBFoton IOPC)*, Oct. 2018, pp. 1–4.
- <span id="page-15-2"></span>[\[3\] F](#page-1-0). Arpanaei, M. R. Zefreh, C. Natalino, P. Lechowicz, S. Yan, J. M. Rivas-Moscoso, Ó. González de Dios, J. P. Fernández-Palacios, H. Rabbani, M. Brandt-Pearce, A. Sánchez-Macián, J. A. Hernández, D. Larrabeiti, and P. Monti, ''Ultra-high-capacity band and space division multiplexing backbone EONs: Multi-core versus multi-fiber,'' *J. Opt. Commun. Netw.*, vol. 16, no. 12, pp. H66–H78, 2024.
- <span id="page-15-3"></span>[\[4\] P](#page-1-1). Boffi, N. Sambo, P. Martelli, P. Parolari, A. Gatto, F. Cugini, and P. Castoldi, ''Mode-group division multiplexing: Transmission, node architecture, and provisioning,'' *J. Lightw. Technol.*, vol. 40, no. 8, pp. 2378–2389, Apr. 15, 2022.
- <span id="page-15-4"></span>[\[5\] N](#page-1-2). Sambo, P. Martelli, P. Parolari, A. Gatto, P. Castoldi, and P. Boffi, ''Mode-group division multiplexing for provisioning in SDM networks,'' in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Dec. 2020, pp. 1–4.
- <span id="page-15-5"></span>[\[6\] A](#page-1-3). Gatto, P. Martelli, P. Parolari, N. Sambo, P. Castoldi, and P. Boffi, ''Mode group division multiplexing in 5 mode-group FMF enabling MIMO-free solutions,'' *IEEE Photon. Technol. Lett.*, vol. 34, no. 21, pp. 1167–1170, Nov. 1, 2022.
- <span id="page-15-6"></span>[\[7\] M](#page-1-4). Klinkowski, P. Lechowicz, and K. Walkowiak, ''Survey of resource allocation schemes and algorithms in spectrally-spatially flexible optical networking,'' *Opt. Switching Netw.*, vol. 27, pp. 58–78, Jan. 2018.
- <span id="page-15-7"></span>[\[8\] A](#page-1-5). Lozada, R. Olivares, D. Bórquez-Paredes, F. M. Ferreira, and A. Beghelli, ''Few-mode amplification-aware resource allocation in modegroup division multiplexing systems,'' in *Proc. IEEE Latin-Amer. Conf. Commun. (LATINCOM)*, Nov. 2024, pp. 1–6.
- <span id="page-15-8"></span>[\[9\] C](#page-1-6). Cuevas-Aliaga, J. Pinto-Ríos, A. Leiva, A. Lozada, N. Jara, R. Olivares, D. Bórquez-Paredes, G. Saavedra, R. Durán, and I. de Miguel, ''Performance evaluation of list-sorting-based allocation algorithms in few-mode fiber SDM optical networks,'' in *Proc. 25th Anniversary Int. Conf. Transparent Opt. Netw. (ICTON)*, Jul. 2025, pp. 1–6.
- <span id="page-15-9"></span>[\[10\]](#page-2-2) J. Yuan, Z. Ren, R. Zhu, Q. Zhang, X. Li, and Y. Fu, ''A RMSA algorithm for elastic optical network with a tradeoff between consumed resources and distance to boundary,'' *Opt. Fiber Technol.*, vol. 46, pp. 238–247, Dec. 2018. [Online]. Available: [https://www.sciencedirect.com/science/](https://www.sciencedirect.com/science/article/pii/S1068520018305145) [article/pii/S1068520018305145](https://www.sciencedirect.com/science/article/pii/S1068520018305145)
- <span id="page-15-10"></span>[\[11\]](#page-2-3) K. Manousakis, A. Angeletou, and E. Varvarigos, ''Energy efficient RWA strategies for WDM optical networks,'' *J. Opt. Commun. Netw.*, vol. 5, no. 4, pp. 338–348, Apr. 2013.
- <span id="page-15-11"></span>[\[12\]](#page-2-4) F. M. Ferreira, C. S. Costa, S. Sygletos, and A. D. Ellis, ''Semi-analytical modelling of linear mode coupling in few-mode fibers,'' *J. Lightw. Technol.*, vol. 35, no. 18, pp. 4011–4022, Sep. 15, 2017.
- <span id="page-15-12"></span>[\[13\]](#page-3-2) N. K. Fontaine, R. Ryf, H. Chen, A. V. Benitez, J. E. A. Lopez, R. A. Correa, B. Guan, B. Ercan, R. P. Scott, S. J. B. Yoo, L. Grüner-Nielsen, Y. Sun, and R. J. Lingle, ''30×30 MIMO transmission over 15 spatial modes,'' in *Proc. Opt. Fiber Commun. Conf. Exhib. (OFC)*, 2015, pp. 1–3.
- <span id="page-15-13"></span>[\[14\]](#page-4-0) N. Jara, J. Bermudez, P. Morales, H. Pempelfort, R. Olivares, and A. Leiva, ''Multiband elastic optical networks: Comprehensive insights into band resource management,'' in *Proc. Int. Conf. Opt. Netw. Design Model. (ONDM)*, May 2025, pp. 1–6.
- <span id="page-15-14"></span>[\[15\]](#page-9-1) D. Bórquez-Paredes and M. Zitkovich, ''Flex Net sim: A C++ library to benchmark spectrum allocation algorithms in elastic optical networks,'' *J. Opt. Commun. Netw.*, vol. 18, no. 9, pp. D16–D29, Sep. 2026. [Online]. Available: <https://opg.optica.org/jocn/abstract.cfm?URI=jocn-18-9-D16>
- <span id="page-15-15"></span>[\[16\]](#page-9-2) M. Zitkovich, G. Saavedra, and D. Bórquez-Paredes, ''Event-oriented simulation module for dynamic elastic optical networks with space division multiplexing,'' in *Proc. 13th Int. Conf. Simulation Modeling Methodologies, Technol. Appl.*, 2023, pp. 295–302.
- <span id="page-15-16"></span>[\[17\]](#page-12-1) J. Pinto-Ríos, B. D. Feris, C. Vásquez, G. Saavedra, D. Bórquez-Paredes, N. Jara, R. Olivares, S. Amjad, A. Leiva, and C. Mas-Machuca, ''Benchmarking framework for resource allocation algorithms in multicore fiber elastic optical networks,'' *J. Opt. Commun. Netw.*, vol. 16, no. 11, pp. 11–27, 2024.

![](_page_15_Picture_21.jpeg)

CATALINA CUEVAS-ALIAGA received the B.Sc. degree in electronic engineering from Pontificia Universidad Católica de Valparaíso (PUCV), Valparaíso, Chile, where she is currently pursuing the M.Sc. degree in electrical engineering with a specialization in optical communications. Her research interests include resource allocation in optical networks, spatial division multiplexing, and few-mode fiber (FMF) technologies. She has worked on routing, modulation, mode, and

wavelength assignment algorithms for dynamic optical networks. In addition to her research activities, she is involved in engineering projects related to telecommunications infrastructure and network monitoring.

![](_page_15_Picture_24.jpeg)

JUAN PINTO-RÍOS received the B.Sc. and M.Sc. degrees in electronic engineering from Pontificia Universidad Católica de Valparaso (PUCV), Chile, in 2019 and 2021, respectively. He is currently pursuing the Ph.D. degree in electrical engineering with PUCV, supported by ANID Scholarship, Chile. His research interests include optical networks, fiber-optic communication systems, and the application of artificial intelligence to communication networks.

![](_page_15_Picture_26.jpeg)

ARIEL LEIVA received the B.Sc. and M.Sc. degrees in electronic engineering from Pontificia Universidad Católica de Valparaíso (PUCV), Chile, in 2003 and 2007, respectively. He received the Ph.D. degree from Universidad Técnica Federico Santa María, Valparaíso, Chile, in 2013. He is currently an Assistant Professor with Pontificia Universidad Católica de Valparaíso, Chile. His current interests include fiber optic communication systems and optical networking.

![](_page_15_Picture_28.jpeg)

ASTRID LOZADA received the M.Sc. and Ph.D. degrees in electronic engineering from Universidad Técnica Federico Santa María, Chile, in 2020 and 2025, respectively. She is currently a full-time Professor with the Department of Electronic Engineering from the Universidad Técnica Federico Santa María. Her main research interests include fiber optic communication systems, optical amplification, and space and band division multiplexing technologies.

![](_page_15_Picture_30.jpeg)

RICARDO OLIVARES received the B.Sc. degree in engineering and the electronic engineering professional title from Universidad Técnica Federico Santa María (UTFSM), Chile, in 1983, and the M.Sc. and D.Sc. degrees in electrical engineering from the Pontificia Universidade Católica do Rio de Janeiro, Brazil, in 1994 and 2001, respectively. He has been with the Department of Electronic Engineering with UTFSM since 1986. His current interests include RF measurements, fiber optic

communication systems, fiber optic amplifier design and nonlinear optics.

![](_page_16_Picture_1.jpeg)

![](_page_16_Picture_2.jpeg)

NICOLÁS JARA (Member, IEEE) received the B.Sc. and M.Sc. degrees in telematics engineering from Universidad Técnica Federico Santa María (UTFSM), Chile, in 2010, and the Ph.D. degree from the Université de Rennes I, France, in 2017, and UTFSM, in 2018. He is currently an Assistant Professor with the Department of Electronics, UTFSM. His current research interests include optical networks design, networks performability, and simulation techniques.

![](_page_16_Picture_4.jpeg)

DANILO BÓRQUEZ-PAREDES received the B.Eng. degree in telematics engineering from Universidad Técnica Federico Santa María (UTFSM), Valparaiso, Chile, in 2012, and the Ph.D. degree from Universidad Adolfo Ibáñez, in September 2018. He also received the professional title in telematics engineering from UTFSM. He is currently a full-time Professor with the Faculty of Engineering and Sciences, Universidad Adolfo Ibáñez. His research interests include the dynamic

allocation of resources in flexible optical networks, network virtualization, graph theory, and optimization.

![](_page_16_Picture_7.jpeg)

GABRIEL SAAVEDRA (Member, IEEE) received the B.Eng. degree in telecommunication engineering and the M.Sc. degree from the Universidad de Concepción, Chile, in 2013 and 2014, respectively, and the Ph.D. degree from University College London (UCL), London, U.K., in 2019. He is currently an Associate Professor with the Universidad de Concepción. His research interests include nonlinear fiber effects, nonlinear compensation methods, and digital signal processing for optical communications.

![](_page_16_Picture_9.jpeg)

IGNACIO DE MIGUEL (Senior Member, IEEE) received the B.Eng. degree in telecommunication engineering and the Ph.D. degree from the Universidad de Valladolid (UVa), Spain, in 1997 and 2002, respectively. He is currently a Full Professor with UVa and has been a Visiting Research Fellow at University College London (UCL), U.K. His research interests include the design, control, and performance evaluation of communication infrastructures, optical networks, edge computing,

and the application of artificial intelligence techniques in these environments. He was the recipient of the Nortel Networks Prize to the Best Ph.D. Thesis on Optical Internet in 2002, awarded by the Spanish Institute and the Association of Telecommunication Engineers (COIT/AEIT).

![](_page_16_Picture_12.jpeg)

RAMÓN J. DURÁN BARROSO received the Ph.D. degree in telecommunications from the Universidad de Valladolid (UVa), Spain, in 2008. He is currently a Full Professor with UVa. His research interests include the design and optimization of optical communication networks, wavelength routing, cognitive optical networks, passive optical access networks, and the integration of distributed computing resources at the edge and in the cloud. He has published more than 60 papers in indexed

journals and over 130 conference papers, and has participated in numerous European and national research projects. His work interests include the application of artificial intelligence to communication networks and the holistic design of infrastructures to meet the requirements of 5G/6G, IoT, and autonomous systems.
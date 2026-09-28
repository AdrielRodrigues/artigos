# Performance Evaluation of List-sorting-based Allocation Algorithms in Few-Mode Fiber SDM Optical Networks

Catalina Cuevas-Aliaga\*<sup>‡‡</sup>, Juan Pinto-Ríos\*, Ariel Leiva\*, Astrid Lozada<sup>†</sup>, Nicolás Jara<sup>†</sup>, Ricardo Olivares<sup>†</sup>, Danilo Bórquez-Paredes<sup>‡</sup>, Gabriel Saavedra<sup>§</sup> Ramon Durán<sup>¶</sup> and Ignacio de Miguel<sup>¶</sup>

\*School of Electrical Engineering, Pontificia Universidad Católica de Valparaíso, Valparaíso, Chile 
†Department of Electronic Engineering, Universidad Técnica Federico Santa María, Valparaíso, Chile 
‡Faculty of Engineering and Sciences, Universidad Adolfo Ibáñez, Viña del Mar, Chile 
§Electrical Engineering Department, Universidad de Concepción, Concepción, Chile 
¶ETSI de Telecomunicación, Universidad de Valladolid, Valladolid, Spain 
‡‡ Corresponding author email: catalina.cuevas@pucv.cl

Abstract—Mode-Group Division Multiplexing (MGDM) in Few-Mode Fiber-based Spatial Division Multiplexing (SDM) networks offers a promising solution for current Wavelength Division Multiplexing (WDM) optical networks, where increasing bandwidth demands require more efficient resource allocation. This work analyzes the performance of two proposals about Route, Modulation, Mode-Group, and Wavelength Allocation algorithms based on reach and capacity sorting criteria applied to MGDM-WDM optical networks. Simulations evaluated their blocking performance applied to two network topologies. The results show that the proposals achieve significant reductions in blocking probability, compared to the baseline algorithm based on Mode-Group sorting criteria, with relative reductions of 77% and 9% under low and high offered loads, respectively.

*Index Terms*—Optical networks, WDM optical networks, Few-Mode, Mode-Group allocation.

#### I. Introduction

The increasing demand for Internet traffic is rapidly pushing individual optical fibers to their capacity limits, which poses significant challenges to the scalability of existing Wavelength Division Multiplexing (WDM) optical network designs [1]. Few-Mode Fiber (FMF) technology [2] has emerged as a practical approach to address this issue by utilizing Mode Group Division Multiplexing (MGDM) [3]. This new technology enables the simultaneous transmission of multiple signals through different spatial mode-groups in a single fiber, significantly improving capacity.

However, the practical deployment of FMF technology faces several challenges that must be addressed. From a hardware perspective, the development of few-mode optical amplifiers, mode multiplexers, and demultiplexers is critical to maintaining the signal in multiple spatial modes [4]. On the

Financial support from projects: ANID Doctorado Nacional (2022-21220867, 2021-21211075), Fondecyt (1241362, 1250775, 1231826) is gratefully acknowledged, USM under grants PI\_LIR\_24\_21, DP N° 069/2024, as well as grants PID2023-146254OB-C41 and PID2020-112675RB-C42 funded by MICIU/AEI/10.13039/501100011033 and the former also by ERFD/EU.

network side, effective resource management for establishing new connections is crucial, as MGDM-WDM optical networks require the allocation of an optical carrier (wavelength) to specific Mode-Groups, considering the physical limitations of each mode [3]. This involves addressing mode coupling, differential mode delay, and crosstalk, which can degrade transmission quality and reduce network performance [5]. Furthermore, optimizing the usage of spectral and spatial resources in MGDM-WDM optical networks requires solving complex resource allocation problems, such as Routing, Modulation, Mode-Group, and Wavelength Allocation (RMMWA) [6].

The RMMWA process involves the allocation of a route, a spatial Mode-Group, an appropriate modulation format, and a specific wavelength for incoming connection requests [7]. Addressing these challenges is essential for maintaining good network operation, maintaining a high quality of transmission (QoT) between connections, maximizing network utilization, and minimizing blocking probability [6].

The literature explores strategies for Mode-Group allocation, including the first approaches such as the Balanced AllocatioN of Mode-Group (BANG) algorithm [8], which systematically identifies and organizes combinations of Mode-Groups and modulation formats according to capacity and reach criteria. Given a connection request, the BANG algorithm attempts to allocate resources by going through an ordered list of candidate Mode-Groups and modulation-format pairs, starting with the highest-level Mode-Group (highest capacity), going through the least spectrally efficient modulation formats (longest optical reach) up to the most spectrally efficient (shortest reach) available in the network. If resources cannot be allocated for the first Mode-Group and the last modulation-format because other connections occupy them, the algorithm attempts the same procedure but with the next lowest-level Mode-Groups. This process continues until all Mode-Groups and modulation formats are exhausted. The fixed order may not always be optimal because it doesn't consider other possible sequences. These alternative orders can lead to better resource allocation, potentially improving the network performance by reducing blocking probabilities. The BANG algorithm is used as a baseline in this study, serving as a reference to assess the improvements introduced by the new allocation strategies.

This work proposes approaches for sorting and allocating Mode-Groups in a novel context using FMF in MGDM-WDM optical networks. The proposed algorithms consider criteria such as reach or capacity (in bit rate terms) into the sorting process, prioritizing Mode-Groups that align most effectively with each requests requirements. Additionally, the impact of these sorting-based strategies on network performance is evaluated and compared with a previous proposal.

#### II. MODELS

## *A. Physical layer model*

We consider a MGDM-WDM optical network, where Mode-Groups are formed by linearly polarized (LP) modes with normalized propagation constants of similar value. On the transmitter side, WDM signals are generated per Mode-Group. Thanks to Mode-Group multiplexers/demultiplexers, Mode-Groups can be added and dropped at each network node, enabling Mode-Group routing for each independent Mode-Group. On the receiver side, Mode-Groups are separated with reduced digital signal processing (DSP) complexity compared to a non-Mode-Group full-MIMO solution [6]. This approach defines a channel as a wavelength supporting a Mode-Group.

Coupling between LP modes occurs within Mode-Groups. LP modes in the same Mode-Group exhibit strong coupling, while those in different Mode-Groups exhibit weaker coupling. We used the optical reach values presented by [8]. This study accounts for both linear and non-linear (intramodal and intermodal) physical layer impairments, including attenuation, dispersion, crosstalk, mode-dependent loss, differential mode delay, and non-linear impairments due to the Kerr effect.

The MGDM-WDM optical network considered support links with Mode-Groups G = {g1, . . . , g<sup>i</sup> , . . . , gG} per optical fiber, which is ordered from lower-order Mode-Groups to higher-order Mode-Groups. Here, G represents the maximum number of Mode-Groups, each composed of one or several LP [3] modes. Different modulation schemes are considered, and each Mode-Group handles M modulation formats, ordered from the lowest number of bits per symbol to the highest, based on their efficiency concerning reach. So, the modulation set M is given by M = {m1, . . . , m<sup>j</sup> , . . . , mM}.

A connection can be established using a Mode-Group and a specific modulation format, which together determine the optical reach Rm,g and the transmission capacity Cm,g. These parameters are determined by the physical layer impairments along the optical path and the characteristics of the modulation scheme used. Considering a fixed modulation format, a tradeoff exists between optical reach and transmission capacity when using different Mode-Groups [6, 8]. Mode-Groups of lower-order achieve longer optical reach but lower capacity compared to higher-order Mode-Groups. This is because lower-order mode groups will experience less intermodal interference due to a reduced number of LP modes composing the group. Conversely, the total capacity of a Mode-Group scales with the number of LP modes, as each LP mode within a Mode-Group can transmit at the same bitrate [9]. Considering the variations in optical reach and bitrate of Mode-Groups when designing resource allocation algorithms is necessary to use the resources efficiently.

The set of available Mode-Group and Modulationformat pairs to establish a connection A is defined as A = {a1, . . . , ak, . . . , aM×G}, where each a<sup>k</sup> has a specific Mode-Group g<sup>i</sup> , a modulation format m<sup>j</sup> , an optical reach Rg,m, and capacity Cg,m in terms of bitrate for each carrier wavelength. Furthermore, the system can operate at any bitrate defined within the set B, which is a set of different bitrate values that are compatible with the transmitters and receivers.

#### *B. Network and traffic models*

The network topology is modeled as a graph Γ = (N ,L), where N represents the set of network nodes and L denotes the set of unidirectional links, each comprising N and L elements, respectively. Each link in the network has the same capacity, determined by the number of Mode-Groups and carrier wavelengths available per Mode-Group.

Connection requests follow an exponential distribution, with an inter-arrival rate λ. The holding time for each connection request also follows an exponential distribution with a mean of 1/µ. The network traffic intensity or offered load is quantified as λ/µ [Erlang].

Each connection request is characterized by the triplet (src, dst, b), where src and dst correspond to the source and destination nodes, and b represents the requested bitrate. The source and destination nodes are uniformly distributed across the network, meaning that each node has an equal probability of being chosen as a source or destination. Similarly, the bitrate is uniformly selected from a predefined set of values B.

## III. SORTED-BASED ALGORITHMS PROPOSALS

We propose two sorting-based allocation algorithms to prioritize the most suitable use of available optical reach or bitrate capacities of Mode-Groups.

The proposed algorithms, named Reach-Sorted and Rate-Sorted, operate in two stages as follows:

Offline stage: Initially, and prior to network operation, a sorted\_list (reach\_list or rate\_list) is created by sorting the entries from the set A, in descending order based on the optical reach value Rm,g or capacity Cm,g. The K-shortest paths are also computed for each pair of nodes.

Online stage: This stage consists of three steps: (I) Routing, (II) Modulation and Mode-Group selection, and (III) Wavelength allocation. When a connection request arrives, described by the triplet (src, dst, b), the algorithm performs the following steps:

- (I) Routing: The algorithm iterates over the function shortest\_path(k, src, dst) to provide the precalculated k-shortest path (route) between the source (src) and destination (dst) nodes.
- (II) Modulation and Mode-Group Selection: Given the input bitrate request b and the k-shortest path obtained in the previous step, the algorithm utilizes the list sorted\_list, which is ordered in descending order based on optical reach (reach\_list) or capacity (rate\_list). This list is then truncated using the function trunc(sorted\_list, b, route) to generate the subset AUX\_M, which includes all elements from sorted\_list that meet the requested demand, ensuring that b does not exceed the available capacity Cm,g and that the selected route length remains within Rm,g. Next, the algorithm selects a Mode-Group from AUX\_M. It iterates through the list sequentially, choosing the first available modulation format and Mode-Group pair. If the selected pair does not satisfy the demand, the algorithm moves to the next entry in the list until a valid selection is found.
- (III) Wavelength Allocation: The function wave\_alloc(mode\_group, route) assigns the first available wavelength, ensuring that the same Mode-Group and wavelength are allocated across all links in the route. If sufficient resources are available, the request is accepted (REQUEST\_ALLOCATED); otherwise, it is rejected (REQUEST\_REJECTED).

The pseudocode for the Online stage illustrating the implementation of the RMMWA algorithm, is provided in Algorithm 1:

Algorithm 1 Online stage: RMMWA algorithm, for both criteria

```
1: Function RMMWA(src, dst, b)
2: for k ← 1 to K do
3: route ← shortest_path(k, src, dst)
4: AUX_M ← trunc(sorted_list,b,route)
5: for i ← 0 to ∥AUX_M∥ − 1 do
6: mode group ← AUX_M(i)
7: if wave_alloc(mode_group, route)= SUC-
      CESS then
8: return REQUEST_ALLOCATED
9: end if
10: end for
11: end for
12: return REQUEST_REJECTED
```

Algorithm 1 uses K routes already precomputed and then goes through the M Mode-Group of the set. Then, it applies a First Fit method to allocate the connection in the ℓ links in the path [10]. Therefore, the Big-O Algorithmic Complexity is given by O(K · M · G · W · L), where K is the number of routes, M is the number of modulation formats, G is the number of mode-groups, W is the number of wavelengths, and L is the number of links in the network.

To illustrate the different sorting strategies used to generate the proposed sorted lists, the BANG algorithm—hereafter referred to as mode\_group\_sorted— used as a reference, is shown in Figure 1. This baseline is compared with the sorting strategies applied during the Offline stage of this proposal, reach\_sorted, and rate\_sorted lists. Figures 1, 2 and 3 illustrate the sorting process for the BANG (baseline), Reach-Sorted, and Rate-Sorted algorithms, respectively, highlighting how each approach organizes Mode-Group and modulation format combinations.

Each table in the figures is constructed based on the WDM channel bandwidth used by the system. Therefore, the capacity and reach depend on the modulation schemes applied to each Mode-Group. The table includes a specific column for the Mode-Group, sorted from the lowest-capacity Mode-Group to the highest-capacity one, while the rows represent the capacity and reach of each Mode-Group according to a specific modulation set, organized from the least spectrally efficient to the most spectrally efficient modulation format.

| Mode-<br>Group          | Modulation 1 (Lowest spectral efficiency) |                  | Modulation 2 |                  | Modulation 3 (Highest spectral efficiency) |           |
|-------------------------|-------------------------------------------|------------------|--------------|------------------|--------------------------------------------|-----------|
| a (Lowest Capacity)     | C <sub>1,a</sub>                          | $R_{1,a}$        |              | R <sub>2,a</sub> | Er<br>S,a                                  | $R_{3,a}$ |
| b                       | $C_{1,b}$                                 | $R_{I,b}$        | $C_{2,b}$    | $R_{2,b}$        | Ĉ3,b                                       | $R_{2,h}$ |
| C<br>(Highest Capacity) | C <sub>L</sub> ,                          | R <sub>I.c</sub> | <b>S</b> 2,c | $R_{2.c}$        | C3,c                                       | $R_{2,c}$ |

Fig. 1. An example illustrating the trajectory considered for sorting the list, based on the criterion for the BANG algorithm (sorted by mode-group).

All algorithms employ a fixed sorting strategy, wherein resources are assigned in a predetermined sequence. As illustrated in Figure 1, the BANG algorithm creates the mode\_group\_sorted list by iterating through the table of Mode-Groups and modulation sets. It selects candidate Mode-Group and modulation format pairs, starting with the highestcapacity Mode-Group and progressing from the least spectrally efficient (longest optical reach) to the most spectrally efficient (shortest reach) modulation format available in the network. If no modulation sets remain available, the algorithm moves to the next lower-capacity mode group and repeats the process.

As can be seen in Figure 2, the Reach-Sorted algorithm creates the reach\_sorted list by iterating through the table of mode-groups and modulation sets. It selects candidate pairs based on their maximum optical reach, prioritizing those with the longest reach and progressing sequentially to those with shorter reach.

In Figure 3, the Rate-Sorted algorithm creates the rate\_sorted list by iterating through the table of modegroups and modulation sets. It selects candidate pairs based

| Mode-<br>Group          | Modulation 1 (Lowest spectral efficiency) |           | Modulation 2 |           | Modulation 3 (Highest spectral efficiency) |                  |  |
|-------------------------|-------------------------------------------|-----------|--------------|-----------|--------------------------------------------|------------------|--|
| a (Lowest Capacity)     | $C_{I,a}$                                 | <b>rt</b> | $C_{2,a}$    | $R_{2,a}$ | $C_{3,a}$                                  | $R_{3,a}$        |  |
| b                       | $C_{I,b}$                                 | $R_{1,b}$ | $C_{2,b}$    | $R_{2,0}$ | $C_{3,b}$                                  | $R_{3,b}$        |  |
| C<br>(Highest Capacity) | $C_{I,c}$                                 | $R_{1,c}$ | C2,c         | $R_{2,c}$ | $C_{3,c}$                                  | R <sub>3.c</sub> |  |

Fig. 2. An example illustrating the trajectory considered for sorting the list, based on the criterion for the Reach-Sorted algorithm (sorted by reach).

| Mode-<br>Group                 | Modulation 1 (Lowest spectral efficiency)                          | Modulation 2 |           | Modulation 3 (Highest spectral efficiency) |                  |
|--------------------------------|--------------------------------------------------------------------|--------------|-----------|--------------------------------------------|------------------|
| <b>a</b> (Lowest Capacity)     | $\begin{array}{c c} \textbf{End} \\ C_{I,a} & R_{I,a} \end{array}$ | $C_{2,a}$    | $R_{2,a}$ | $C_{3,a}$                                  | $R_{3,a}$        |
| b                              | $C_{I,b}$ $R_{I,b}$                                                | $C_{2,b}$    | $R_{2,b}$ | $C_{3,b}$                                  | $R_{3,b}$        |
| <b>C</b><br>(Highest Capacity) | $C_{I,c}$ $R_{I,c}$                                                | C2,c         | $R_{2,c}$ | C <sub>3,c</sub>                           | R <sub>3,c</sub> |

Fig. 3. An example illustrating the trajectory considered for sorting the list, based on the criterion for the Rate-Sorted algorithm (sorted by rate).

on their maximum capacity, prioritizing those with the highest data rate and progressing sequentially to those with lower rates.

Although the paths shown in Figure 2 and Figure 3 appear less straightforward compared to Figure 1, this is a result of the prioritization of a single variable in the Reach-Sorted and Rate-Sorted approaches. These algorithms define the path based solely on candidate pairs that meet the respective sorting criterion, whether it be maximum reach or highest capacity.

# IV. SIMULATION RESULTS

This section presents the simulation setup and evaluation criteria used to analyze the performance of the proposed resource allocation algorithms. The simulations assess blocking probability across two network topologies, comparing the effectiveness of the proposed approaches against the baseline BANG algorithm.

Table I presents the simulation parameters used in this work, which consist of: physical layer, traffic parameters, and network parameters.

Table II presents the optical reach and achievable bitrate (capacity) for each combination of Mode-Group and modulation format, based on a bit error rate (BER) threshold of 4 · 10<sup>−</sup><sup>3</sup> before Forward Error Correction. These optical reach values were calculated in [8] under a worst-case scenario, assuming that each Mode-Group can accommodate 81 wavelength-

TABLE I SIMULATION PARAMETERS

| Parameters                     | Value                                   |  |  |  |
|--------------------------------|-----------------------------------------|--|--|--|
| Physical layer parameters      |                                         |  |  |  |
| Mode-Group set G               | g1 : (LP01)                             |  |  |  |
|                                | g2 : (LP11a, LP11b)                     |  |  |  |
|                                | g3 : (LP02, LP21a, LP21b)               |  |  |  |
| Modulation formats set M       | BPSK, 16-QAM, 32-QAM                    |  |  |  |
| Capacities and optical reaches | Described in Table II                   |  |  |  |
| Traffic parameters             |                                         |  |  |  |
| Traffic model                  | Poisson process                         |  |  |  |
| Arrival rate λ                 | [1000, 1500, 2000, 2500, 3000]          |  |  |  |
| Service rate µ                 | 1                                       |  |  |  |
| Offered load range             | [1000 to 3000] Erlangs                  |  |  |  |
| Number of connection request   | 106<br>requests for each simulation     |  |  |  |
| Network parameters             |                                         |  |  |  |
| Topologies                     | NSFNet (Figure 4)                       |  |  |  |
|                                | N = 14, L = 42 and α = 0.23             |  |  |  |
|                                | UKNET (Figure 5)                        |  |  |  |
|                                | N = 21, L = 78 and α = 0.18             |  |  |  |
| Bitrate set B                  | [100, 200, 300, 400, 600] Gbps          |  |  |  |
| Number of Wavelengths          | 81 per Mode-Group                       |  |  |  |
| Resource allocation algorithms |                                         |  |  |  |
| Baseline algorithm             | BANG [8]                                |  |  |  |
| Proposed algorithms            | Reach-Sorted and Rate-Sorted Algorithms |  |  |  |

channels, representing full utilization of the C-band, with a WDM channel bandwidth of 50 GHz.

![](_page_3_Figure_13.jpeg)

Fig. 4. The National Science Foundation Network (NSFNet) topology described in Table I.

![](_page_3_Figure_15.jpeg)

Fig. 5. The United Kingdom Network (UKNet) topology described in Table I.

To assess the performance of the proposed algorithms, we utilize the C++ Flex Net Sim event-driven simulator [11], Optical reach and Bit Rate per Mode-Group for different modulation formats [8], based on a bit error rate (BER) threshold of  $4 \cdot 10^{-3}$  before Forward Error Correction.

| mode-groups set $(G)$        | $m_1: \mathbf{QPSK}$ |                | $m_2:$ 16-QAM    |                | $m_3: 64\text{-}\mathbf{QAM}$ |                |
|------------------------------|----------------------|----------------|------------------|----------------|-------------------------------|----------------|
| $(g_1 + g_2 + g_3)$          | $C_{m,g}$ [Gbps]     | $R_{m,g}$ [km] | $C_{m,g}$ [Gbps] | $R_{m,g}$ [km] | $C_{m,g}$ [Gbps]              | $R_{m,g}$ [km] |
| $g_1 (LP_{01})$              | 100                  | 2200           | 200              | 2100           | 300                           | 900            |
| $g_2 (LP_{11-a/b})$          | 200                  | 1300           | 400              | 1200           | 600                           | 700            |
| $g_3 (LP_{02}, LP_{21-a/b})$ | 300                  | 900            | 600              | 800            | 900                           | 600            |

applying it to two network topologies. These topologies vary in size and connectivity ( $\alpha$ ), defined as  $\alpha = L/N(N-1)$ . In the proposed algorithm, the K-shortest path approach is used with K=3. The networks evaluated include NSFNet [12] and UKNet [13], whose topology parameters are presented in Table I. Considering the simulation setup established in [8], and to ensure consistency and provide a fair comparison, the NSFNet is scaled to match the maximum length of the UKNet topology. Then, the average lengths of the links in NSFNet and UKNet are 150 km and 137 km, respectively. We have included a baseline algorithm (BANG algorithm) that adheres to the approach proposed in [8], which serves as a reference to evaluate the performance of both sorting-based proposals. For this study, the BANG algorithm is considered as a Mode\_Group-Sorted algorithm.

Figure 6 presents the blocking probability for each offered load in the NSFNet topology for three sorted-based algorithms: Reach-Sorted, Rate-Sorted, and Mode\_Group-Sorted. As offered load increases, all algorithms exhibit a similar rise in blocking probability. The Reach-Sorted and Rate-Sorted algorithms consistently outperform the Mode\_Group-Sorted algorithm, particularly at low to medium offered loads, achieving a maximum variation of 21% relative to the baseline for low-mid offered load of around 1000 Erlangs. This performance is due to the NSFNet topology combining short- and long-range links, necessitating resource prioritization based on optical reach. This strategy optimizes network resource allocation by favoring paths with the most extended optical reach, which are essential for high bitrate demands.

Figure 7 highlights the performance variations among the algorithms in the UKNet topology. In this case, between the three algorithms, Rate-Sorted consistently achieves the lowest blocking probability, particularly at mid-to-high offered loads, achieving a maximum variation of 77% relative to the baseline and 9% for high offered load of around 3000 Erlangs, suggesting its efficiency in prioritizing mode-groups with higher capacity. The Reach-Sorted algorithm exhibits slightly lower performance; however, it presents a higher blocking probability in certain scenarios. This behavior is influenced by the features of the UKNet topology, which consists of relatively shorter links and nodes with higher connectivity compared to NSFNet. This underscores the effectiveness of employing a sorting strategy that prioritizes capacity over optical reach, considering the features of the topology.

![](_page_4_Figure_6.jpeg)

Fig. 6. Blocking probability for Mode\_Group-Sorted, Reach-Sorted and Rate-Sorted algorithms in the NSFNet topology (plots are made with 95% confidence interval).

![](_page_4_Figure_8.jpeg)

Fig. 7. Blocking probability for for Mode\_Group-Sorted, Reach-Sorted and Rate-Sorted algorithms in the UKNet topology (plots are made with 95% confidence interval).

#### V. CONCLUSION

This study evaluates the performance of the Reach-Sorted, Rate-Sorted, and Mode\_Group-Sorted algorithms within the RMMWA framework across two distinct network topologies: NSFNet and UKNet. The simulation results highlight that the effectiveness of each algorithm is significantly influenced by the specific characteristics of the network topology and offered load conditions. In NSFNet, the Reach-Sorted algorithm exhibited superior performance under low-to-medium offered loads, benefiting from its prioritization of longer optical paths, which enhances resource allocation efficiency in a topology with mixed short- and long-range links. In contrast, UKNet favored the Rate-Sorted algorithm under mid-to-high offered loads, as its strategy of prioritizing higher-capacity mode groups effectively minimized blocking probability. This difference is primarily attributed to NSFNet longer links, which make reach-based prioritization more effective, while UKNet shorter links and higher node degree facilitate better traffic distribution under high-load scenarios.

Overall, these findings underscore the importance of tailoring resource allocation strategies to the specific topological and traffic features of the network. Algorithms that leverage reach- or capacity-based prioritization outperform those relying solely on Mode-Group sorting in terms of blocking probability.

Future research should explore integrating these findings into adaptive algorithms capable of dynamically adjusting to different network conditions by monitoring certain performance metrics in real time.

## REFERENCES

- [1] H. Waldman, The impending optical network capacity crunch, in: 2018 SBFoton International Optics and Photonics Conference (SBFoton IOPC), 2018, pp. 1–4. doi:10.1109/SBFoton-IOPC.2018.8610949.
- [2] K.-i. Kitayama, N.-P. Diamantopoulos, Few-mode optical fibers: Original motivation and recent progress, IEEE Communications Magazine 55 (8) (2017) 163–169. doi:10.1109/MCOM.2017.1600876.
- [3] P. Boffi, N. Sambo, P. Martelli, P. Parolari, A. Gatto, F. Cugini, P. Castoldi, Mode-group division multiplexing: Transmission, node architecture, and provisioning, Journal of Lightwave Technology 40 (8) (2022) 2378– 2389. doi:10.1109/JLT.2021.3135636.
- [4] P. Sillard, K. Benyahya, D. Soma, G. Labroille, P. Jian, K. Igarashi, R. Ryf, N. K. Fontaine, G. Rademacher, K. Shibahara, Few-mode fiber technology, deployments, and systems, Proceedings of the IEEE 110 (11) (2022) 1804–1820. doi:10.1109/JPROC.2022.3207012.
- [5] Y. Weng, X. He, Z. Pan, Space division multiplexing optical communication using few-mode fibers, Optical Fiber Technology 36 (2017) 155–180. doi:https://doi.org/10.1016/j.yofte.2017.03.009.
- [6] N. Sambo, P. Martelli, P. Parolari, A. Gatto, P. Castoldi, P. Boffi, Mode-group division multiplexing for provisioning in sdm networks, in: 2020 European Conference on Optical Communications (ECOC), 2020, pp. 1–4. doi:10.1109/ECOC48923.2020.9333236.

- [7] M. Klinkowski, P. Lechowicz, K. Walkowiak, Survey of resource allocation schemes and algorithms in spectrally-spatially flexible optical networking, Optical Switching and Networking 27 (2018) 58–78. doi:https://doi.org/10.1016/j.osn.2017.08.003.
- [8] A. Lozada, R. Olivares, D. Borquez-Paredes, F. M. ´ Ferreira, A. Beghelli, Few-mode amplification-aware resource allocation in mode-group division multiplexing systems, in: 2024 IEEE Latin-American Conference on Communications (LATINCOM), 2024, pp. 1–6. doi:10.1109/LATINCOM62985.2024.10770656.
- [9] N. K. Fontaine, R. Ryf, H. Chen, A. Velazquez Benitez, J. E. Antonio Lopez, R. Amezcua Correa, B. Guan, B. Ercan, R. P. Scott, S. J. Ben Yoo, L. Gruner-Nielsen, ¨ Y. Sun, R. J. Lingle, 30×30 mimo transmission over 15 spatial modes, in: 2015 Optical Fiber Communications Conference and Exhibition (OFC), 2015, pp. 1–3. doi:10.1364/OFC.2015.Th5C.1.
- [10] F. Falcon, G. Espa ´ na, D. B ˜ orquez-Paredes, Flex net sim: ´ A lightly manual (2021). arXiv:2105.02762.
- [11] M. Zitkovich, G. Saavedra, D. Borquez-Paredes, Event- ´ oriented simulation module for dynamic elastic optical networks with space division multiplexing, in: Proceedings of the 13th International Conference on Simulation and Modeling Methodologies, Technologies and Applications - Volume 1: SIMULTECH, INSTICC, SciTePress, 2023, pp. 295–302. doi:10.5220/0012084500003546.
- [12] B. Chinoy, H.-W. Braun, et al., The national science foundation network, Tech. rep., Technical Report GA-A21029, SDSC (1992).
- [13] P. Morales, P. Franco, A. Lozada, N. Jara, F. Calderon, ´ J. Pinto-R´ıos, A. Leiva, Multi-band environments for optical reinforcement learning gym for resource allocation in elastic optical networks, in: 2021 International Conference on Optical Network Design and Modeling (ONDM), IEEE, 2021, pp. 1–6. doi:10.23919/ONDM51796.2021.9492435.
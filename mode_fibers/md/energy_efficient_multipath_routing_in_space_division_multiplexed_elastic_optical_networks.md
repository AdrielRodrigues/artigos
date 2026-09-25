---
title: "Energy efficient multipath routing in space division multiplexed elastic optical networks"
tema_principal: mode_fibers
temas_relacionados: []
pdf: ../pdf/energy_efficient_multipath_routing_in_space_division_multiplexed_elastic_optical_networks.pdf
---

![](_page_0_Picture_1.jpeg)

Contents lists available at ScienceDirect

# Computer Networks

journal homepage: www.elsevier.com/locate/comnet

![](_page_0_Picture_5.jpeg)

![](_page_0_Picture_6.jpeg)

# Energy efficient multipath routing in space division multiplexed elastic optical networks

Soheil Hosseini \*, Ignacio de Miguel , Noemí Merayo , Ramón de la Rosa , Rubén M. Lorenzo , Ramón J. Durán Barroso \*

Universidad de Valladolid, Valladolid, Spain

#### ARTICLE INFO

Keywords:
Space division multiplexing
Elastic optical network
Multi-core fibers
Multipath routing
Resource allocation
Energy efficiency
Latency

#### ABSTRACT

This paper introduces a novel dynamic multipath routing, modulation level, spatial and spectrum assignment algorithm for space division multiplexing (SDM) enabled elastic optical networks (EON) with the aim of minimizing the blocking probability and the energy consumed by bandwidth variable transponders (BVTs). The adopted multipath routing strategy allows the splitting of the demand into several sublightpaths using different fiber cores but ensuring that all of them utilize the same set of fibers in order to avoid differential delay. The method also imposes continuity constraints in both spectrum and core location in order to use cost-effective SDM Reconfigurable Optical Add and Drop Multiplexers (ROADMs) without lane change support. The complete usage of multi-core fibers (MCFs) in this kind of networks is restricted due to inter-core crosstalk (XT), which can reduce the quality of received signals. Therefore, the method besides using the most effective modulation format, also ensures that the XT of the lightpaths (or sublightpaths) does not exceed the threshold for each modulation format. A simulation study comparing our method with another similar proposal from the literature is presented for different types of topologies in terms of link distances. Simulation results demonstrate that the proposed multipath routing algorithm in networks including links close to or beyond 1000 km significantly boost the dynamic performance in terms of blocking probability, energy consumption, and latency.

## 1. Introduction

High-performance optical networks, which are flexible, cost-effective, and bandwidth efficient, are much needed as a result of the rise of high-speed and bandwidth-hungry applications on the Internet [1]. The advent of elastic optical networks (EON) is rooted from the limitations faced by the previous generation of optical networks based on wavelength division multiplexing (WDM), and allow to increase the efficiency of the network in a productive way [2,3]. It is not surprising that EONs based on orthogonal frequency division multiplexing (OFDM) are highly accepted as the next generation of optical networks, leveraging on flexible spectrum reservation and adaptive selection of the most suitable modulation format [4].

In these networks, allocating resources for end-to-end dynamic connection requests, considering the restrictions of spectrum continuity and contiguity, is a fundamental problem, known as the routing and spectrum assignment (RSA) problem [5]. Moreover, greater scalability can be obtained by using more spectrally efficient modulation formats

(provided they meet Quality of Transmission, QoT, requirements), thus reducing the number of frequency slots (FSs) needed to support the demands, and resulting in more connection requests being accepted. Therefore, in EONs, the valuable concept of distance-adaptive modulation cannot be overlooked. Hence, the RSA problem transforms into the route, modulation level and spectrum assignment (RMLSA) problem [6].

Elastic optical networks, due to the dynamic allocation of spectral resources to connections, suffer from spectrum fragmentation, leaving small sets of unused spectral slots in different fiber. These noncontinuous and non-contiguous available FSs are ineffective to fulfill upcoming requests [7,8]. Therefore, spectrum fragmentation results in increased blocking of demands. One solution to overcome that problem consists in employing multipath routing or split spectrum techniques, which divide the demanded bandwidth into sub-flows of lower bandwidth. Thus, rather than establishing a single lightpath, several ones (called sublightpaths from now on) are established.

Despite the additional flexibility provided by EONs, the capacity limit of single-mode fibers (SMFs) has become a critical concern.

E-mail addresses: soheil.hosseini@uva.es (S. Hosseini), rduran@tel.uva.es (R.J. Durán Barroso).

 $<sup>^{\</sup>ast}$  Corresponding authors.

<span id="page-1-0"></span>Therefore, the introduction of spectrally and spatially flexible optical networks applying space division multiplexing (SDM) looks an extremely promising solution to get around the capacity crunch in upcoming optical transmission networks [\[9,10\]](#page-15-0). SDM networks provide an additional degree of freedom in the format of the spatial domain. In order to transport optical signals in SDM systems, every link holds various spatial paths, which can be a fiber (in a multi-fiber cable), a core (in a multi-core fiber, MCF), or even a mode (in a multi-mode fiber, MMF) [\[11\]](#page-15-0). In particular, boosted capacity, appropriate spatial switching granularity, and similar features of attenuation with a customary single-core fiber are all strong incentives for utilizing MCFs. The new dimension (space) with the vertical direction relative to the frequency zone acts as an effective factor to grant a great deal of freedom in signal management [\[12\].](#page-15-0) Evidently, the higher the degree of freedom, the greater the complexity of network control, leading to the use of route, space, and spectrum assignment (RSSA) or even route, modulation level, space and spectrum assignment (RMLSSA) algorithms. In [\[13\],](#page-15-0) it is shown that in networks with MCFs, using an architecture based on Reconfigurable Optical Add and Drop Multiplexers (ROADMs) without lane changes (therefore, imposing core continuity constraint in the routes of the connection) is much more economic (and reduces complexity), at the expense of a small reduction in performance.

Nevertheless, a problem with MCFs is the leakage of a fraction of the signal power of a core to the neighbor ones, which triggers signal interference if the same spectral slots are used [\[14\].](#page-15-0) This phenomenon is known as inter-core crosstalk (XT), and causes a decrease in signal quality [\[15\].](#page-15-0) Taking some approaches such as trench-assisted multi-core fibers, emplacing certain distance among cores, and distributing optical signals in the contrary directions over the adjacent cores can contribute to the inter-core XT reduction [\[11\]](#page-15-0). However, it does not mean that the impact of XT can be fully cleared. Therefore, XT-aware RSSA methods are required for lightpath allocation, to ensure that such an impairment does not exceedingly influence the lightpath quality [16–[19\].](#page-15-0)

In this paper, we propose a novel energy efficient and XT-aware multipath routing algorithm to solve the dynamic RMLSSA problem in SDM-EONs with MCFs to serve dynamic traffic demands. In our approach, multipath routing, when required, is performed over a single path (i.e., sublightpaths use different cores but are routed through the same set of fibers), so that the connection is not affected by the differential delay problem which typically arises when multipath solutions are adopted. Moreover, continuity constraints in both the spectrum and the core assigned to the lightpaths (or sublightpaths) are assumed in order to use the efficient ROADM architecture presented in Rumipamba-Zambrano et al. [\[13\]](#page-15-0). In the proposed method, the use of distance adaptive modulation formats is considered, and the impact of inter-core XT is also incorporated. This new method is compared with an efficient multipath method proposed by Moura and Da Fonseca [\[20\]](#page-15-0). Through an in-depth simulation analysis, we demonstrate that our proposed method is as efficient as Moura and Da Fonseca's proposal in networks with short links (typically national networks), while it significantly outperforms in networks with long links (large countries, continental and inter-continental networks). This advantage manifests as a reduction in blocking ratio, energy consumption, the number of sublightpaths generated per demand, and average end-to-end delay.

The rest of this paper is organized as follows. Section 2 provides an overview of existing studies in the context of SDM-EON multipath routing. In [Section 3,](#page-2-0) the network model as well as some definitions and assumptions are presented. We discuss the proposed algorithm in [Sec](#page-4-0)[tion 4](#page-4-0), and [Section 5](#page-8-0) is dedicated to present a simulation study and analyze the numerical results. The work reaches an end by providing a conclusion in [Section 6.](#page-14-0)

## **2. Related works**

Multipath routing has been studied in the context of EONs and, more recently, in the context of SDM-EON. Jafari-Beyrami et al. [\[21\]](#page-15-0) have

presented two fragmentation-aware heuristics with/without inter-core XT consideration in SDM-EON with MCFs. Whenever a connection is going to be blocked through the single path strategy; it will be divided upmost into two sub-demands across the cores. For alleviating the fragmentation rate of the path links, those sub-demands are assigned to two cores with the highest fragmentation level. However, because the provided algorithms consider the central core as the common core, they would only be able to work in the MCFs with central core structure. Another proposal to reduce fragmentation is that of Trindade and Da Fonseca [\[22\],](#page-15-0) which sets a maximum number of paths and a minimum number of frequency slots for a connection to use multipath routing. In [\[23\]](#page-15-0), authors introduced three heuristics to minimize the amount of fragmentation in SDM-EON. The aim of the introduced algorithms is to reduce the blocking probability. In that paper, the Spectrum Block Multipathing per Cores (SBMC) leads to better results in terms of blocking ratio compared to the other proposed algorithms. However, in SBMC, an incoming connection might be divided into *n* sub-demands to be established over different cores of the fiber, which leads to the usage of more network resources.

Paira et al. [\[24\]](#page-15-0) have proposed different survivable multipath routing algorithms and assessed their performance in terms of blocking probability, energy efficiency, fragmentation, and XT awareness. The introduction of survivability is the main contribution of the paper, demonstrating improved blocking rate compared with the traditional p-cycle and shared protection methods. However, a single demand may be divided between three different paths, which increases the differential delay among those flows. Zhu et al. [\[25\]](#page-15-0) have proposed a distance-adaptive energy-aware resource allocation (DERA) algorithm using a survival multipath scheme. In that work, the selection of the paths is done by taking into account the expected energy consumption rather than simply relying on shortest path considerations. Halder et al. [\[26\]](#page-15-0) have proposed two route, core and spectrum allocation schemes for offline survivable SDM-EON using multipath-based protection, and consider two classes of incoming connection requests, those that have to be established immediately upon arrival and those which can tolerate some delay until being established. Oliveira et al. [\[27\]](#page-15-0) have introduced an algorithm called Multi/singlepath rOuting For multIcOre network (MOFIO). When a single path is employed to connect the source to the destination, shared backup path protection (SBPP) is utilized to make the network resilient against failure. When multipath routing is performed, the SBPP method is executed to protect each of the produced primary paths. For multipath routing, two different paths are considered in order to improve the ratio of accepted requests, which increases the level of differential delay.

In another study on multipath routing in SDM-EONs, by Moura and da Fonseca [\[20\],](#page-15-0) two families of RMLSSA algorithms, named Connected Component Labeling (CCL) and Inscribed Rectangles Algorithm (IRA), are proposed and compared, with an algorithm called Multipath Inscribed Rectangles Algorithm Minimal Crosstalk (MPIRAXT) generally providing the best results in those tests. The algorithms are based on the use of image processing techniques with the objective of reducing the computational complexity. In this study, rectangles of different sizes show the available set of frequency slots. In each rectangle, the width multiplied by the length should fulfill the amount of frequency slots requested by an incoming connection. If a single path is not capable of satisfying the requested demand, the bandwidth can be divided between two to five shortest paths. Although the authors give priority to using the rectangles, which stretch across only one spatial path, the employment of multiple paths as well as the selection of the rectangles with more than one unit length as the block of free frequency slots increase the energy consumption associated with the optical transponders and the amount of differential delay.

Accordingly, in this paper, we propose a novel multipath RMLSSA algorithm with the aim of avoiding differential delay and reducing energy consumption, while keeping the blocking probability low enough, and considering continuity constraints in both spectrum and core

<span id="page-2-0"></span>**Table 1**Transmission reach and XT-threshold for each modulation level for a MCF with seven cores with hexagonal arrangement (based on [21]).

| Modulation level                                      | BPSK        | QPSK           | 8QAM           | 16QAM          |
|-------------------------------------------------------|-------------|----------------|----------------|----------------|
| Transmission Reach [km]  XT <sub>threshold</sub> [dB] | —<br>-22.75 | 4000<br>-25.76 | 2000<br>-28.77 | 1000<br>-31.79 |
| $L_{\rm modulation}$                                  | 1           | 2              | 3              | 4              |

**Table 2**Crosstalk parameters for a MCF with seven cores with hexagonal arrangement [29].

| Parameter                               | Value              |
|-----------------------------------------|--------------------|
| Bending radius $(R_B)$ [m]              | 0.05               |
| Propagation constant ( $\beta$ ) [1 /m] | $4 \times 10^6$    |
| Coupling coefficient ( $\kappa$ )       | $4 \times 10^{-4}$ |
| Core pitch (A) [m]                      | $4 \times 10^{-5}$ |

location in order to use cost-effective SDM ROADMs without lane change support.

## 3. Network model, definitions and assumptions

In this study, the network topology is represented by a connected graph,  $\mathcal{S}=(\mathcal{N},\mathcal{E})$ , where  $\mathcal{N}$  is the set of switching nodes and  $\mathcal{E}$  the set of links. Moreover, N and E denote the number of nodes and links, respectively. Links are bidirectional, having an individual multicore fiber for each direction. Each multicore fiber has a set of C cores identified by  $\mathcal{E}=\{1,\,2,\,...,\,C\}$ , and the spectrum of each core is divided into an ordered collection of F frequency slots,  $\mathcal{F}=\{1,\,2,\,...,F\}$ . Regarding modulation formats, we assume the use of binary phase shift keying (BPSK), quadrature phase shift keying (QPSK), and 8 and 16 quadrature amplitude modulation (8QAM and 16QAM).

A dynamic operation scheme is regarded for forthcoming connection demands, so that the associated lightpaths are dynamically established and released. Every connection request R is characterized by  $R(s, d, \gamma, \tau)$ , where s and d are the source and destination nodes, respectively,  $\gamma$  is the number of required frequency slots (assuming a BPSK modulation

level), and  $\tau$  specifies the time span (or service time) of the connection. However, a more spectrally efficient (but less robust) modulation format than BPSK can be used if the route, r, employed for establishing that connection does not exceed the transmission reach for that modulation format (as shown in Table 1 [21]). If that is the case, the demanded bandwidth (number of frequency slots) of that specific request can be reduced to  $\gamma_{\rm modified}$ , calculated by Eq. (1) [28] in accordance with the selected modulation level for that route. Thus,

$$\gamma_{\rm modified} = \left[ \frac{\gamma}{L_{\rm modulation}^r} \right],$$
 (1)

where  $L^r_{\rm modulation}$  is the number of bits per symbol associated to the topmost attainable modulation level of route r when taking into account the transmission reach (Table 1). Be aware that Eq. (1) may lead to a floating-point number for some connection requests; thus, the ceiling function is called for the sake of being rounded up to an integer number. Note that the data shown in Table 1, based on [21] correspond to the use of trench-assisted single-mode seven-core fibers, where the cores have an even-wide hexagonal structure, and considering that paths exceeding 4000 km must use BPSK modulation format, which are the conditions that we will also assume in the simulation studies in this paper.

Regarding spectrum, we assume spectrum continuity and contiguity constraints, i.e., identical slots indexes have to be employed by an end-to-end lightpath from the source to the destination node, and the entire set of allocated FSs to a lightpath should be spectrally adjacent. To prevent interference between spectrally adjacent connections, a guard-band of one slot is considered. Moreover, core continuity is also assumed along the routes to use the efficient ROADM architecture presented in Rumipamba-Zambrano et al. [13].

As previously mentioned, transmission in SDM-EONs with MCFs is impaired by inter-core XT, which arises from the occupancy of similar spectrum ranges in neighbor cores, thereby leading to the signal quality reduction. Accordingly, it is crucial to estimate the accumulated XT in lightpaths established in MCFs to ensure they satisfy quality of transmission requirements.

The XT value for a signal propagating through a certain core of a MCF is computed by Eq. (2) (in natural units) [29],

Algorithm 1
Energy efficient multipath routing, modulation level, core, and spectrum assignment algorithm (EEMPR)

Given: Physical network topology  $G = (\mathcal{N}, \mathcal{E})$ 

Set of K-shortest distance paths for each s-d pair (sorted with increasing length for each s-d pair),  $\mathbf{p}_k$ 

Availability of each frequency slot (f) in each core (c) in each link (e)

 $s_{ecf}, e \in \mathcal{E}, c \in \mathcal{C}, f \in \mathcal{F}$  (being TRUE if available and FALSE if unavailable)

**Input:** An incoming connection request  $R(s, d, \gamma, \tau)$ ,

**Output:** Establishment of lightpath (or sublightpaths) for the arrived connection request, and updated spectral utilization of each core/link

## **Auxiliary procedures:**

XT\_is\_OK(): checks XT requirements by using the method described in section 3 classify\_gaps(): classifies spectral gaps in three categories according to the comparison of their size with the required number of slots (shown below, lines 71-77).

## **Algorithm 1** (*continued* )

## <span id="page-4-0"></span>**Algorithm 1** (*continued* )

$$XT = \frac{n - n \cdot \exp(-(n+1)hl)}{1 + n \cdot \exp(-(n+1)hl)},$$
(2)

where *n* represents the number of neighbor cores having at least one common used FS with the connection being evaluated, and *l* is the transmission length in meters. The mean value of increased XT per unit length, can be determined by Eq. (3) [\[29\].](#page-15-0)

$$h = \frac{2\kappa^2 R_B}{\beta \Lambda}. (3)$$

where *RB*, *β*, *κ* and Λ are, respectively, the bending radius, propagation constant, coupling coefficient, and core pitch of the fiber. The parameters considered in this study (again, for a MCF with seven cores arranged in a hexagonal structure) are shown in [Table 2](#page-2-0) [\[29\]](#page-15-0).

The summation of the value of inter-core XT over the links in the lightpath should be calculated as the accumulated XT to assure the lightpath quality. In particular, the maximum threshold of XT should be met by the accumulated XT when a connection demand is served. The maximum optical reach based modulation format is taken into account as a reference of the inter-core XT threshold for every lightpath ([Table 1](#page-2-0)).

## **4. Dynamic energy efficient multipath routing, modulation level, core, and spectrum assignment algorithm (EEMPR)**

In this section, we propose a XT-aware multipath routing, modulation level, core, and spectrum assignment, which can effectively reduce the blocking probability and improve energy efficiency. We provide a general description of the algorithm, accompanied by a simple example, as well as the pseudocode of the method ([Algorithm 1](#page-2-0)).

The algorithm works as follows. First of all, the *K*-shortest distance paths for each source-destination pair must be precomputed. Then, for each request, *R*(*s, d, γ, τ*), the algorithm starts by considering the shortest of those paths between *s* and *d* (lines 1–2) and the most spectrally efficient modulation format that can be used according to the length of the path is selected. Thus, a set of *γ*modified available frequency slots along that route must be searched (line 3). It should be noted that a frequency slot of a core *c* is available for the connection, only if is available in the same core number *c* of all the links composing the path. Therefore, the intersection of the frequency slots' status of the correspondent cores of the different links over the selected route must be computed (line 4).

In order to allocate resources, the algorithm searches iteratively for spectral availability (in the whole route) from core number 1 to *C*, and within each core from slot 1 to *F* (lines 9–30). However, for resource allocation (lines 32–65) it uses an Best-Fit strategy [\[30\]](#page-15-0), that is, it prioritizes the allocation of a set of contiguous FSs in a single core whose size exactly matches the demand, i.e., its size is equal to *γ*modified plus the guardband slot if required (lines 36–44) and as long as XT requirements are also fulfilled (lines 38). If a set of available frequency slots of exact size is not found (or cannot be used due to XT), but at least one set of available consecutive slots has a larger size, then the set with the smallest size that satisfies the demand is used [\[30](#page-15-0),[31\]](#page-15-0) (lines 45–53). In contrast, if no set of available consecutive slots is equal to or greater than the required number (or does not comply with XT requirements), then multipath routing will be used (lines 54–62), and the demand will be split to be served through different spectral gaps (possibly in different cores) along the same path. In that case the biggest available set of consecutive slots found in any of the cores will be selected to serve the demand. For the allocation of the remaining required spectral slots (line

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

**Fig. 1.** (a) Example network topology (distances are given in km), (b) Core and spectrum availability through the selected path (s-A-B-d), (c) Allocation of resources to request R with multipath routing.

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

**Fig. 2.** The NSFNET topology [\[32\]](#page-15-0) (distances are given in km).

![](_page_6_Figure_4.jpeg)

**Fig. 3.** The even-wide hexagonal structure for a seven-core fiber.

59), the procedure mentioned above will be repeated (i.e., an exact-fit strategy will be used), until the demand is fully satisfied. It should be noted that resources are only effectively allocated if the demand can be fully served by multipath routing (lines 40 and 49); otherwise, no resources will be allocated at all (line 65), i.e., a demand cannot be

![](_page_6_Figure_7.jpeg)

**Fig. 4.** Request blocking rate of EEMPR in NSFNet at *K* = 1, 3, 5, 7. **Fig. 5.** Request blocking rate of MPIRA in NSFNet at *K* = 1, 3, 5, 7.

partially fulfilled. If no available resources are found in any of the *K*-shortest paths between the *s* and *d* nodes, the request will be blocked (line 68).

The time complexity of the algorithm (including XT computation) in the worst-case scenario is O(*KC*<sup>3</sup> *F*3 *E*). The main 'for' loop of the algorithm (lines 1–66) runs *K* times. For each candidate path, first, the intersection of the frequency slots' status in the cores of the links must be computed (line 4), which has a complexity of O(*CFE*). Then, an inner loop (lines 10–30) runs *C* times, and has an additional loop running *F*  times, where spectral gaps are identified and added to a sorted list according to the sizes of those gaps (measured in frequency slots) and core numbers. The complexity of lines 10–30 is thus O(*C*<sup>2</sup> *F*2 ). Finally, in lines 33–63, there is a 'do-while' loop which is executed up to *CF* times. Internally, gaps are classified (line 35), with complexity O(*CF*), and there are three sequential loops (lines 36–44, 45–53 and 54–62), each executed again up to *CF* times. In these loops, the most demanding task is the XT computation, which has complexity O(*CFE*). Thus, the complexity of lines 33–63 is O(*C*<sup>3</sup> *F*3 *E*). Therefore, the complexity of the algorithm is O(*K*(*CFE* + *C*<sup>2</sup> *F*2 + *C*<sup>3</sup> *F*3 *E*)), which is asymptotically equivalent to O(*KC*<sup>3</sup> *F*3 *E*).

Regarding space complexity, the algorithm needs to store the *K*shortest paths of up to *E*− 1 links, for a set of *N*(*N*− 1) different sourcedestination pairs, so the space complexity is O(*KEN*<sup>2</sup> ). Additionally, the availability state of the spectral slots in each core of each fiber link needs also to be stored, which has space complexity O(*FCE*). Although there are additional variables and data structures, their space

![](_page_6_Figure_12.jpeg)

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

Fig. 6. Bandwidth blocking rate of EEMPR in NSFNet at K = 1, 3, 5, 7.

![](_page_7_Figure_4.jpeg)

Fig. 7. Bandwidth blocking rate of MPIRA in NSFNet at K = 1, 3, 5, 7.

complexity is equal or lower. Therefore, the space complexity of the algorithm is  $O(KEN^2 + FCE)$ .

To show an example of the algorithm, let us assume an optical network comprising 5 nodes and 6 links (Fig. 1). Every fiber consists of

![](_page_7_Figure_8.jpeg)

**Fig. 8.** Energy consumption per transmitted bit of EEMPR in NSFNet at K=1, 3, 5, 7.

seven cores, and the spectrum is divided into 15 frequency slots. For the sake of simplicity, we assume that there are no idle slots in the last two cores, and thus, only five cores (1 to 5) are represented in the figure. A request, R, to establish a connection between nodes s and d, requiring 19 slots (if BPSK were used), is received. A set of K-shortest distance paths (with K=3) for each source-destination pair has been previously precomputed. Thus, Fig. 1(a) shows the 3-shortest distance paths between nodes s and d. The shortest of these paths, s-A-B-d (represented in blue), has a length of 2000 km, is selected as the first option to serve the request. Then, based on Table 1, since the distance of the path is less than 4000 km and more than or equal to 2000 km, the QPSK modulation format is selected. Therefore,  $\gamma_{\rm modified} = \left\lceil \frac{19}{2} \right\rceil = 10$  slots as specified by Eq. (1).

Fig. 1(b) shows the spectral availability through the selected path (s-A-B-d). Blue slots in the figure represent frequency slots that are used in each core by other connections in at least one of the links of the path (and thus cannot be used to serve the connection request, R), and white slots represent available spectral slots through the whole path. Taking into account the core continuity and the spectrum continuity constraints, it is not feasible for R to be accommodated using a single lightpath through path s-A-B-d, as there are not 10 consecutive available slots in any single core. Therefore, the request must be served by means of several sublightpaths. Through first-fit core evaluation from the core with the smallest index to the one with the highest one, the largest number of successive empty frequency slots (6) is found in core number 5. As a result, slots 1 to 5 would be allocated for traffic transmission, and slot 6 would be reserved but used as a guard-band (sublightpath 1 in Fig. 1(c)). Therefore, 5 additional slots should still be provided to satisfy the demand. There is no such a big gap. The biggest available spectral available gap is then found in core 1, which has a size of 4 slots, and in fact does not require a guard-band, as it is at the end of the spectral range and, at the other side, slot 11 is already a guard-band. Those slots are then reserved (sublightpath 2 in Fig. 1(c)). For the final spectral slot to be provided to satisfy the demand, the first exact-fit gap is found in core 2, so that one would be selected and then the demand would be fully served (sublightpath 3 in Fig. 1(c)), assuming in this example, for the sake of simplicity, that XT requirements are also fulfilled.

In the case that not enough spectral resources were available in path s-A-B-d (even exploiting multipath routing), the algorithm would then check with the second shortest available path, and then, if necessary, with the third one (as K = 3 in this example).

![](_page_7_Figure_13.jpeg)

**Fig. 9.** Energy consumption per transmitted bit of MPIRA in NSFNet at K = 1, 3, 5, 7.

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

**Fig. 10.** Delay relative to shortest path of EEMPR in NSFNet at *K* = 1, 3, 5, 7.

![](_page_8_Figure_4.jpeg)

**Fig. 11.** Delay relative to shortest path of MPIRA in NSFNet at *K* = 1, 3, 5, 7.

## **5. Simulation setup and results**

In this section, the performance of EEMPR is assessed and compared with MPIRAXT (from now on MPIRA) [\[20\]](#page-15-0). For that aim, an SDM-EON simulator has been developed in Python. The physical topology considered in the simulation is the National Science Foundation

![](_page_8_Figure_8.jpeg)

**Fig. 12.** Request blocking ratio comparison in NSFNet topology at *K* = 5.

![](_page_8_Figure_10.jpeg)

**Fig. 13.** Bandwidth blocking ratio comparison in NSFNet topology at *K* = 5.

Network (NSFNET) topology, with 14 nodes and 21 links, as depicted in [Fig. 2](#page-6-0) [\[32\]](#page-15-0). Each link is composed by two unidirectional multicore fibers (on per direction). Each fiber has seven cores with even-wide hexagonal structure ([Fig. 3\)](#page-6-0). Optical transmission employs the C-band, and the spectrum per core is partitioned into 320 frequency slots of 12.5 GHz.

Connection requests arrive at the network according to a Poisson process with average arrival rate *λ*, and the duration of each established connection (*τ*) is based on an exponential distribution with average *T*. The source and the destination nodes of each connection request are randomly selected considering a uniform distribution. The number of required frequency slots for each connection (assuming a BPSK modulation level), *γ*, is also obtained from a uniform distribution between *γ*min = 1 and *γ*max = 24 frequency slots, therefore with average *γ*avg = (*γ*max − *γ*min)*/*2. Since different connections may demand a different number of frequency slots, rather than using the classical traffic load in erlangs (*λT*), we use the normalized version given by Eq. (4), which takes into account the average and maximum capacity of the connections, as well as the number of nodes in the network, *N*.

$$load = \frac{\lambda T}{N(N-1)} \frac{\gamma_{\text{avg}}}{\gamma_{\text{max}}} \tag{4}$$

Transceivers in the network are assumed to be able to use BPSK, QPSK, 8QAM, and 16QAM modulation formats, subject to the

![](_page_8_Figure_16.jpeg)

**Fig. 14.** Energy consumption per transmitted bit comparison in NSFNet topology at *K* = 5.

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

**Fig. 15.** Reduction in energy per bit in NSFNet topology at *K* = 5.

![](_page_9_Figure_4.jpeg)

**Fig. 16.** Reduction in number of sublightpaths in NSFNet topology at *K* = 5.

transmission constraints and the spectral efficiency described in [Table 1](#page-2-0). Therefore, for establishing connections, *γ*modified spectral slots should be reserved instead of *γ*. However, an additional slot should also be

![](_page_9_Figure_7.jpeg)

**Fig. 17.** Delay in relation to shortest path comparison in NSFNet topology at *K*  = 5.

reserved for the connections to provide a spectral guard-band.

In each simulation, 105 requests are generated for warming up the network, but no metrics are collected during that phase. Then 106 additional requests are generated, for which performance metrics are retrieved.

![](_page_9_Figure_11.jpeg)

**Fig. 18.** Network topologies (a) SmallNet [\[34\]](#page-15-0), (b) USNet [\[34\],](#page-15-0) (c) JPN12 [\[35\],](#page-15-0) (d) DT [\[36\]](#page-15-0) (distances in km).

**Table 3**  . Characteristics of the five network topologies.

| Topology | Number of<br>nodes | Number of<br>links | Avg. link length<br>(km) | Min. length of the 5-shortest<br>paths (km) | Avg. length of the 5-shortest<br>paths (km) | Max. length of the 5-shortest<br>paths (km) |
|----------|--------------------|--------------------|--------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| SmallNet | 10                 | 22                 | 2080.0                   | 1810                                        | 5152.91                                     | 8820                                        |
| NSFNet   | 14                 | 21                 | 1080.95                  | 300                                         | 4341.09                                     | 9200                                        |
| USNet    | 24                 | 43                 | 997.67                   | 250                                         | 4012.13                                     | 8750                                        |
| JPN12    | 12                 | 17                 | 436.88                   | 48                                          | 1554.14                                     | 4003                                        |
| DT       | 14                 | 23                 | 186.25                   | 36.9                                        | 685.61                                      | 1379.6                                      |

## *5.1. Analysis for different numbers of K-shortest paths*

First of all, we have analyzed the performance of EEMPR and the baseline algorithm, MPIRA [\[20\],](#page-15-0) separately, for different numbers of *K*-shortest paths, setting *K* to 1, 3, 5 and 7. As we have mentioned, in EEMPR, all sublightpaths are routed through the same path; however, up to *K* different paths can be explored for resource availability. Four different metrics have been studied. First of all, [Figs. 4 and 5](#page-6-0) show the request blocking ratio (RBR) for EEMPR and MPIRA, respectively. The RBR is defined as the fraction of requests that are blocked. Results are represented together with 95 % confidence intervals. Then, [Figs. 6 and 7](#page-7-0)  represent the bandwidth blocking ratio (BBR) for both algorithms. The BBR takes into account that different requests need different bandwidths. Thus, BBR is computed as the quotient between the sum of the requested bandwidths (*γ*modified) associated with blocked requests and the sum of the requested bandwidths of all requests. Next, [Figs. 6](#page-7-0) and [7](#page-7-0)  show the energy required by network transponders for the transmission of a single bit. The energy consumption associated to the transmission through each core has been estimated by using the model by Lopez ´ et al. [\[33\]](#page-15-0), considering the spectral resources employed in that core. Finally, [Figs. 8 and 9](#page-7-0) show the average delay of the longest distance sublightpath compared to that of the shortest distance path for both algorithms.

These metrics will be analyzed in more detail in the following subsection. At this point, our objective is to see the trade-off on blocking ratio vs other parameters when using different values of *K*. Increasing *K*  leads to lower values of blocking ratio, but the energy consumption per bit and the differential delay increase, when using either the EEMPR or the MPIRA algorithms. Our main goal is to minimize the blocking probability, and when going from *K* = 5 to *K* = 7, there is no improvement on blocking probability (again, for both EEMPR and MPIRA). Therefore, in the following subsections we compare and analyze in detail the results for *K* = 5 ([Figs. 10 and 11](#page-8-0)).

## *5.2. Comparison of EEMPR and MPIRA for K* = *5 shortest paths*

We now focus on the *K* = 5 case and plot the results for EEMPR and MPIRA in the same figures to facilitate comparison. First of all, [Figs. 12](#page-8-0)  [and 13](#page-8-0) show the RBR and BBR, respectively, for different traffic loads. As it can be observed, EEMPR always obtains a lower blocking ratio than MPIRA, achieving approximately up to 50 % reduction in RBR and BBR for a traffic load of 7.5.

Then, [Fig. 14](#page-8-0) shows the energy required by network transponders for the transmission of a single bit. As shown in [Fig. 14](#page-8-0), EEMPR leads to lower consumed energy per bit than MPIRA. This is mainly due to the fact that MPIRA typically requires a higher number of paths to satisfy a demand thereby leading to higher utilization of network transponders (especially at high loads). The savings in energy consumption per transmitted bit of EEMPR when compared with MPIRA are shown in [Fig. 15](#page-9-0). Employing only one single path to accommodate a connection request and only limiting the division of a demand just across the cores, like EEMPR does, leads to a decrease on the consumed energy per bit.

In multipath routing, a demand can be served by using several paths (sublightpaths). However, with EEMPR, the average number of sublightpaths required is much lower than with MPIRA, a reduction of more than 15 % for a load of 7.5, as shown in [Fig. 16](#page-9-0). The reduction in number of sublightpaths, which is yielded by EEMPR leads to a more efficient use of transponders and spectrum as a lower number of guard-band slots are required.

A key advantage of EEMPR is that it removes the differential delay associated to transmission through different paths, since they all use the same route (just a different core). This fact is very important as a significant difference can cause the unneeded retransmission of packets and malfunctions (or inefficiencies) in the protocols of upper layers. Moreover, EEMPR also reduces the average delay in relation to the shortest distance path. The average delay of the longest distance sublightpath compared to that of the shortest distance path is shown in [Fig. 17](#page-9-0) for EEMPR and MPIRA, obtaining again better results with EEMPR.

## *5.3. Analysis for other topologies*

We have also analyzed the performance of EEMPR (compared with MPIRA) in four additional topologies: SmallNet [\[34\],](#page-15-0) USNet [\[34\]](#page-15-0), JPN12 [\[35\]](#page-15-0) and DT [\[36\].](#page-15-0) The topologies are shown in [Fig. 18,](#page-9-0) and their characteristics, together with those of the NSFNet, are shown in Table 3. The USNet topology has a higher number of nodes and links than the other topologies. Nevertheless, considering the length of the links, we can observe two distinct groups of topologies. The SmallNet, NSFNet and USNet topologies are characterized for having long links (around or higher than 1000 km), and thus the average length of the 5-shortest paths exceeds 4000 km for each of those networks. In contrast, the JPN12 and DT topologies have lower link distances (below 500 km), and the average length of the 5-shortest paths is less than 2000 km. Note that for paths with length lower than 2000 km, spectrally efficient modulation formats like 8QAM or 16QAM are employed ([Table 1\)](#page-2-0), while for paths exceeding 4000 km, BPSK must be used, which is more robust but less spectrally efficient. As we will show next, this feature has an impact on the results obtained.

First, the results for the topologies with long links, SmallNet and USNet, are shown in [Fig. 19.](#page-11-0) The conclusions are similar to those obtained for the NSFNet (also a topology with long links). For most loads, EEMPR gets lower BBR than the baseline algorithm, MPIRA, and the reduction is particularly significant for the SmallNet topology. Moreover, EEMPR also reduces energy consumption, around 11 % for SmallNet and 5 % for USNet (considering the traffic loads leading to a BBR ~10<sup>−</sup> <sup>3</sup> ) when compared with MPIRA, as well as the delay in relation to the shortest path.

Then, the results for the topologies with shorter links, JPN12 and DT, are shown in [Fig. 20](#page-12-0). In this case, in contrast to the previous networks, the results are very similar for EEMPR and MPIRA, both in terms of BBR and energy consumption.

As shown in Table 3, SmallNet, NSFNet and USNet, have long links,

<span id="page-11-0"></span>![](_page_11_Figure_2.jpeg)

**Fig. 19.** Analysis in the SmallNet (left column) and USNet (right column) topologies in terms of BBR (a and d), energy consumption (c and d) and delay in relation to shortest path (e and f).

<span id="page-12-0"></span>![](_page_12_Figure_2.jpeg)

**Fig. 20.** Analysis in the JPN12 (left column) and DT (right column) topologies in terms of BBR (a and d), energy consumption (c and d) and delay in relation to shortest path (e and f).

![](_page_13_Figure_2.jpeg)

**Fig. 21.** Histograms of the 5-shortest paths lengths for the NSFNet.

and thus the length of the *K*-shortest paths is higher. In contrast, JPN12 and DT are smaller networks and thus have shorter *K*-shortest paths. Figs. 21 and 22 show the histogram of the length of the paths for these five networks for *K* = 5. The histograms also represent the modulation format associated with those paths, based on the limitations shown in [Table 1](#page-2-0).

In networks with long links, BPSK must be used for a considerable number of paths, resulting in increased bandwidth requirements (a higher number of spectral slots) to achieve a specific data rate. In contrast, for networks with short links, most connections can be established with 16QAM and 8QAM, so they require less bandwidth (and thus a lower number of spectral slots) to achieve a specific data rate. EEMPR is more efficient when dealing with requests demanding a high number of spectral slots than MPIRA and for that reason, EEMPR outperforms MPIRA in networks with long links. This is due to the fact that MPIRA has more constraints when searching for 'rectangles' in cores and frequency slots for resource allocation (see [Section 2](#page-1-0) and [\[20\]](#page-15-0)), while EEMPR operates with more freedom. This translates in EEMPR requiring a lower number of sublightpaths to serve the requests, which brings advantages in terms of energy consumption, and also in terms of requiring a lower number of guard-bands (and so additional spectral savings). The reduction in the number of sublightpaths is shown in [Fig. 23](#page-14-0). For instance, focusing on the traffic load for which the BBR is around 10<sup>−</sup> <sup>3</sup> , EEMPR, compared with MPIRA, reduces the number of sublighpaths in around 22 % for USNet, 12 % for NSFNet ([Fig. 16](#page-9-0)) and 35 % for SmallNet (i.e., in the networks with long links), and around 2 % for JPN and 6 % for DT (i.e., in the networks with short links).

As a conclusion, EEMPR is as efficient as MPIRA in networks with short links (typically national networks), while it clearly outperforms in networks with long links (large countries, continental and intercontinental networks).

![](_page_13_Figure_7.jpeg)

**Fig. 22.** Histograms of the 5-shortest paths lengths for (a) SmallNet, (b) USNet, (c) JPN12 and (d) DT.

<span id="page-14-0"></span>![](_page_14_Figure_2.jpeg)

**Fig. 23.** Reduction in the number of sublightpaths for (a) SmallNet, (b) USNet, (c) JPN12 and (d) DT.

## **6. Conclusion**

We have proposed a new dynamic multipath routing, space, and spectrum assignment algorithm for SDM-EONs. It has been designed with the aim of decreasing blocking ratio and energy consumption, as well as setting the differential delay parameter arising in multipath strategies to zero. Since the appearance of inter-core crosstalk (XT) in SDM systems decreases the signal quality, the proposed method also checks that the accumulated XT does not exceed certain thresholds to validate the connection establishment. In case there are not enough resources to satisfy the demand with a single lightpath, the demand will be split, using the minimum number of cores as possible. Keeping the number of generated sublightpaths low is essential to prevent the use of many BVTs, and thus improving energy efficiency. The simulation study has been conducted considering different network topologies with different link distances. We have demonstrated that in network topologies with long links (like large countries, continental or intercontinental networks), our proposal outperforms another proposal from the literature in both blocking ratio and energy consumption. Moreover, our proposal keeps the delay closer to that of the shortest path, and hence, it clearly improves network performance.

## **CRediT authorship contribution statement**

**Soheil Hosseini:** Conceptualization, Investigation, Methodology, Software, Visualization, Writing – original draft. **Ignacio de Miguel:**  Conceptualization, Funding acquisition, Methodology, Project administration, Supervision, Writing – original draft. **Noemí Merayo:** Supervision, Validation, Writing – review & editing. **Ramon** ´ **de la Rosa:**  Validation, Writing – review & editing. **Ruben** ´ **M. Lorenzo:** Validation, Writing – review & editing. **Ramon** ´ **J. Duran** ´ **Barroso:** Conceptualization, Funding acquisition, Methodology, Project administration, Software.

## **Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## **Data availability**

Raw simulation results will be made available upon request

## <span id="page-15-0"></span>**Acknowledgment**

This work is part of the IoTalentum project, which has received funding from the EU H2020 Research and Innovation Programme under the MSCA grant agreement no. 953442. It is also supported by Ministerio de Ciencia e Innovacion ´ / Agencia Estatal de Investigacion ´ (Grant PID2020-112675RB-C42 funded by MCIN/AEI/10.13039/ 501100011033), and by Consejería de Educacion ´ de la Junta de Castilla y Leon ´ and the European Regional Development Fund (Grant VA231P20).

## **References**

- [1] [E. Agrell, et al., Roadmap of optical communications, J. Opt. 18 \(6\) \(2016\) 063002.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0001)
- [2] [O. Gerstel, et al., Elastic optical networking: a new dawn for the optical layer? IEEE](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0002)  [Commun. Mag. 50 \(2\) \(2012\) s12](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0002)–s20.
- [3] [M. Jinno, et al., Spectrum-efficient and scalable elastic optical path network:](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0003)  [architecture, benefits, and enabling technologies, IEEE Commun. Mag. 47 \(11\)](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0003) [\(2009\) 66](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0003)–73.
- [4] [C. Politi, et al., Routing in dynamic future flexi-grid optical networks, in:](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0004)  [International Conference on Optical Network Design and Modelling \(ONDM\), IEEE,](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0004)  [2012](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0004).
- [5] [B.C. Chatterjee, et al., Routing and spectrum allocation in elastic optical networks:](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0005)  [a tutorial, IEEE Commun. Surv. Tutor. 17 \(3\) \(2015\) 1776](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0005)–1800.
- [6] [K. Christodoulopoulos, et al., Elastic bandwidth allocation in flexible OFDM-based](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0006)  [optical networks, J. Lightwave Technol. 29 \(9\) \(2011\) 1354](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0006)–1366.
- [7] [B.C. Chatterjee, et al., Fragmentation problems and management approaches in](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0007)  [elastic optical networks: a survey, IEEE Commun. Surv. Tutor. 20 \(1\) \(2017\)](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0007)  183–[210.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0007)
- [8] [S. Talebi, et al., Spectrum management techniques for elastic optical networks: a](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0008) [survey, Opt. Switch. Netw. 13 \(2014\) 34](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0008)–48.
- [9] [T.J. Xia, et al., Introduction of spectrally and spatially flexible optical networks,](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0009)  [IEEE Commun. Mag. 53 \(2\) \(2015\) 24](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0009)–33.
- [10] [R.J. Essiambre, et al., Breakthroughs in photonics 2012: space-division](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0010) [multiplexing in multimode and multicore fibers for high-capacity optical](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0010)  [communication, IEEE Photonics J 5 \(2\) \(2013\) 0701307.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0010)
- [11] [M. Klinkowski, et al., Survey of resource allocation schemes and algorithms in](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0011) [spectrally-spatially flexible optical networking, Opt. Switch. Netw. 27 \(2018\)](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0011)
- 58–[78.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0011) [12] [D. Siracusa, et al., Resource allocation policies in SDM optical networks, in:](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0012)  [International Conference on Optical Network Design and Modeling \(ONDM\), IEEE,](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0012)
- [2015.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0012) [13] [R. Rumipamba-Zambrano, et al., Space continuity constraint in dynamic flex-grid/](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0013)  [SDM optical core networks: an evaluation with spatial and spectral super-channels,](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0013)  [Comput. Commun. 126 \(2018\) 38](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0013)–49.
- [14] [W. Klaus, et al., Advanced space division multiplexing technologies for optical](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0014) [networks, J. Opt. Commun. Netw. 9 \(4\) \(2017\) C1](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0014)–C11.
- [15] [S. Hosseini, et al., Survivable time-aware traffic grooming in spatial division](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0015) [multiplexing elastic optical networks with minimized crosstalk, Comput. Electr.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0015) [Eng. 83 \(2020\) 106579.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0015)
- [16] [H. Tode, et al., Routing, spectrum, and core and/or mode assignment on space](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0016)[division multiplexing optical networks, J. Opt. Commun. Netw. 9 \(1\) \(2017\)](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0016)  A99–[A113.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0016)
- [17] [M. Klinkowski, et al., Dynamic crosstalk-aware lightpath provisioning in](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0017)  spectrally–[spatially flexible optical networks, J. Opt. Commun. Netw. 11 \(5\)](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0017)  [\(2019\) 213](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0017)–225.
- [18] [B.C. Chatterjee, et al., Priority-based inter-core and inter-mode crosstalk-avoided](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0018)  [resource allocation for spectrally-spatially elastic optical networks, IEEE/ACM](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0018)  [Trans. Netw. 29 \(4\) \(2021\) 1634](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0018)–1647.
- [19] [B.C. Chatterjee, et al., BPRIA: crosstalk-avoided bi-partitioning-based counter](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0019)[propagation resource identification and allocation for spectrally-spatially elastic](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0019) [optical networks, IEEE Trans. Netw. Serv. Manag. 19 \(4\) \(2022\) 4369](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0019)–4383.
- [20] [P.M. Moura, N.L. da Fonseca, Multipath routing in elastic optical networks with](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0020)  [space-division multiplexing, IEEE Commun. Mag. 59 \(10\) \(2021\) 64](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0020)–69.
- [21] [M. Jafari-Beyrami, et al., On-demand fragmentation-aware spectrum allocation in](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0021)  [space division multiplexed elastic optical networks with minimized crosstalk and](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0021)  [multipath routing, Comput. Netw. 181 \(2020\) 107531](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0021).
- [22] S. Trindade and N.L.S. Da Fonseca, *Split-demand and multipath routing in spacedivision multiplexing optical networks*, IEEE Latin-American Conference on Communications (LATINCOM), 2022.
- [23] [F. Yousefi, et al., Novel fragmentation-aware algorithms for multipath routing and](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0023)  [spectrum assignment in elastic optical networks-space division multiplexing \(EON-](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0023)[SDM\), Opt. Fiber Technol. 46 \(2018\) 287](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0023)–296.
- [24] [S. Paira, et al., On energy efficient survivable multipath based approaches in space](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0024)  [division multiplexing elastic optical network: crosstalk-aware and fragmentation](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0024)[aware, IEEE Access 8 \(2020\) 47344](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0024)–47356.
- [25] [R. Zhu, et al., Survival multipath energy-aware resource allocation in SDM-EONs](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0025) [during fluctuating traffic, J. Lightwave Technol. 39 \(7\) \(2021\) 1900](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0025)–1912.
- [26] [J. Halder, et al., A novel RSCA scheme for offline survivable SDM-EON with](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0026) [advance reservation, IEEE Trans. Netw. Serv. Manag. 19 \(2\) \(2022\) 804](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0026)–817.

- [27] [H.M. Oliveira, et al., Multipath routing, spectrum and core allocation in protected](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0027)  [SDM elastic optical networks, in: IEEE Global Communications Conference](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0027) [\(GLOBECOM\), IEEE, 2019.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0027)
- [28] [X. Wan, et al., Dynamic routing and spectrum assignment in spectrum-flexible](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0028)  [transparent optical networks, J. Opt. Commun. Netw. 4 \(8\) \(2012\) 603](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0028)–613.
- [29] A. Muhammad, et al., *[Resource allocation for space-division multiplexing: optical white](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0029)  box* versus *optical black box networking*[, J. Lightwave Technol. 33 \(23\) \(2015\)](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0029) [4928](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0029)–4941.
- [30] [F.S. Abkenar, et al., Best fit \(bf\): a new spectrum allocation mechanism in elastic](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0030)  [optical networks \(eons\), in: International Symposium on Telecommunications](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0030)  [\(IST\), IEEE, 2016.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0030)
- [31] [R.A. Cortes, et al., Spectrum allocation algorithms for elastic DWDM networks on](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0031)  [dynamic operation, IEEE Latin Am. Trans. 12 \(6\) \(2014\) 1012](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0031)–1018.
- [32] [H. Huang, et al., Virtual network provisioning over space division multiplexed](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0032) [optical networks using few-mode fibers, J. Opt. Commun. Netw. 8 \(10\) \(2016\)](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0032)  726–[733.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0032)
- [33] J. Lopez, ´ [et al., On the energy efficiency of survivable optical transport networks](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0033)  [with flexible-grid, in: European Conference and Exhibition on Optical](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0033)  [Communication \(ECOC\), IEEE, 2012.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0033)
- [34] [Y. Li, et al., Adaptive FEC-based lightpath routing and wavelength assignment in](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0034) [WDM optical networks, Opt. Switch. Netw. 14 \(](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0034) Part 3) (2014) 241–249.
- [35] [H. Tode, Y. Hirota, Routing, spectrum, and core and/or mode assignment on space](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0035)[division multiplexing optical networks, J. Opt. Commun. Netw. 9 \(1\) \(2017\)](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0035)  A99–[A113.](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0035)
- [36] [S. Azodolmolky, et al., Experimental demonstration of an impairment aware](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0036) [network planning and operation tool for transparent/translucent optical networks,](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0036)  [J. Lightwave Technol. 29 \(4\) \(2011\) 439](http://refhub.elsevier.com/S1389-1286(24)00181-6/sbref0036)–448.

![](_page_15_Picture_41.jpeg)

**Soheil Hosseini** received his B.Sc. and M.Sc. degrees in IT Engineering from Kermanshah University of Technology, Kermanshah, Iran and Computer Engineering from Sahand University of Technology, Tabriz, Iran, respectively.

Currently, he is working as a Ph.D. fellow under the framework of Marie Skłodowska-Curie Actions (MSCA) H2020, IoTalentum project at the Universidad de Valladolid and Telefonica ´ Innovacion ´ Digital, Spain. His research interests are mainly focused on optical networking, AI applied to optical systems, optical communications at the network edge supporting 5G/6G, and softwarization and virtualization of computer networks.

![](_page_15_Picture_44.jpeg)

**Ignacio de Miguel** received the degree in telecommunication engineering and the Ph.D. degree from the Universidad de Valladolid (UVa), Spain, in 1997 and 2002, respectively.

He is currently an Associate Professor at UVa and the Coordinator of the master's degree in telecommunication engineering. He has also been a Visiting Research Fellow at University College London, U.K. His main research interests include the design, control and performance evaluation of communication infrastructures, optical networks, edge computing, and the application of artificial intelligence techniques in these environments. He has published more than 40 papers in international journals and more than 170 conference papers.

Dr. de Miguel has been a member of the Technical Program Committee of several international conferences, besides being the Chair of the TPC and the Local Organizing Committee of NOC 2009. He was a recipient of the Nortel Networks Prize to the Best Ph.D. Thesis on Optical Internet in 2002, awarded by the Spanish Institute and the Association of Telecommunication Engineers (COIT/AEIT).

![](_page_15_Picture_48.jpeg)

**Noemí Merayo** received the Telecommunication Engineer degree in engineering from the Valladolid University, Spain, in February of 2004 and the Ph.D. degree in the Optical Communication Group at the Universidad de Valladolid, in July 2009.

Since 2005 she works as Lecturer at the Universidad de Valladolid. She has also been a Visiting Research Fellow at the University of Hertfordshire in the Optical Networks Group, Science and Technology Research Institute (STRI), at the TOyBA research group of the University of Zaragoza and more recently in the Technology University or Munich (TUM). Her research focuses on the design and performance evaluation of optical networks, especially passive optical networks and the

application of artificial intelligence techniques.

Dr. Merayo is currently coordinating the Master in Physics and Technology of lasers at the University of Valladolid and the University of Salamanca.

![](_page_16_Picture_2.jpeg)

**Ramon** ´ **de la Rosa** received the M.Sc. degree from the School of Telecommunication Engineering (STE), Universidad de Valladolid, Spain, in 1999, and the Ph.D. degree, in 2005.

After a short period of working in QA for the main HFC network provider in Madrid, he enrolled in the Signal Theory, Communications, and Telematic Engineering Doctorate Program at the Universidad de Valladolid. His research is related to bioengineering and the measurement of non-ionizing electromagnetic fields (EMF) in populated areas, pioneering the earlier works in Spain to map the EMF levels in the main cities of the Castile and Leon ´ region. He is currently with Space Communications, being in charge of the STE's ground station for satellite tracking and acting as a reviewer in the field of

space communications in the yearly M.Sc. and Ph.D. awards of the Professional Association of Telecommunication Engineers. He was awarded by the 3M Foundation for his work related to neuromuscular human–machine interfaces, in 2007.

![](_page_16_Picture_6.jpeg)

**Ruben** ´ **M. Lorenzo** received the Telecommunication Engineer and Ph.D. degrees from the University of Valladolid, Spain, in 1996 and 1999, respectively.

From 1996 to 2000, he was a Junior Lecturer with the University of Valladolid, where he joined the Optical Communications Group. Since 2000, he has been a Lecturer. He was the Head of the Faculty of Telecommunication Engineering, University of Valladolid, and the Research Director of Center for the Development of Telecommunications (CEDETEL). His research interests include integrated optics, optical communication systems, and optical networks.

![](_page_16_Picture_9.jpeg)

**Ramon** ´ **J. Duran** ´ **Barroso** received his Ph.D. degree from the Universidad of Valladolid (UVa), Spain in 2008. Since the year 2023, he has held the position of Full Professor at that University.

Initially, he began working in the design of optical devices and, from 2004 onwards, his focus shifted primarily to optical communication networks. Specifically, he concentrated on the design and optimization of networks with wavelength routing, hybrid networks (introducing the concept of polymorphic networks), cognitive optical networks (proposing CHRON networks), and passive optical access networks. Artificial intelligence (AI) has been employed to address all the design and optimization challenges in these networks. In recent years, he

has integrated the deployment of distributed computing resources at the edge and in the cloud into the design and optimization of communication networks. This integration is driven by the need for a holistic design and operation of all these resources to meet the requirements of 5G/6G, IoT, and autonomous vehicles.

The dissemination activity of his research has resulted in 55 papers published in JCR journals and more than 130 conference papers. He assumes the role of a guest editor for seven special issues in JCR Journals, organizes workshops at four conferences, and is a member of the TPC for various conferences.

Prof. Ramon ´ J. Duran ´ Barroso has consistently been involved in competitive projects, encompassing 3 European, 14 national, and 9 regional projects. He has served as the principal investigator in 8 of them, comprising 2 international and 6 national projects. Moreover, his leadership extends beyond the UVa team to the coordination of the European project IoTalentum, involving 14 partners, as well as two national projects: ONOFRE-2 with 3 partners, and Go2Edge, a research network with 15 partners. Furthermore, he has been involved in 74 contracts with companies and institutions, assuming the leadership role in 12 of them.
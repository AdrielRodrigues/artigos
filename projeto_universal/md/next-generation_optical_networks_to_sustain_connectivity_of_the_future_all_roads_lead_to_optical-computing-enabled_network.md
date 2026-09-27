---
title: "Next-generation optical networks to sustain connectivity of the future: All roads lead to optical-computing-enabled network?"
tema_principal: projeto_universal
temas_relacionados: []
ano: null
autores: []
veiculo: "Internet of Things"
pdf: ../pdf/next-generation_optical_networks_to_sustain_connectivity_of_the_future_all_roads_lead_to_optical-computing-enabled_network.pdf
---

Contents lists available at [ScienceDirect](https://www.elsevier.com/locate/iot)

# Internet of Things

journal homepage: [www.elsevier.com/locate/iot](https://www.elsevier.com/locate/iot)

![](_page_0_Picture_5.jpeg)

![](_page_0_Picture_6.jpeg)

# Next-generation optical networks to sustain connectivity of the future: All roads lead to optical-computing-enabled network?

Dao Thanh Hai [a](#page-0-0) ,[∗](#page-0-1) , Isaac Woungang [b](#page-0-2)

- <span id="page-0-0"></span><sup>a</sup> *School of Science, Engineering and Technology, RMIT University Vietnam, Viet Nam*
- <span id="page-0-2"></span><sup>b</sup> *Department of Computer Science, Toronto Metropolitan University, Canada*

#### A R T I C L E I N F O

#### *Keywords:*

Optical communication-computing integrated network Optical-computing-enabled network In-network optical computing Optical-bypass network Computed lightpath Integrated lightpath Optical-layer intelligence Optical aggregation Optical XOR Routing Wavelength and network coding assignment Wavelength and computing assignment Optical network design and planning 2.0

Integer linear programming

#### A B S T R A C T

The rise and then rapid developments of various nascent technologies, encompassing notably Internet of Things (IoT), Big Data and Artificial Intelligence (AI) have been heralding a new era of connectivity, spanning from people, things, to ultimately intelligence. Such connectivity of the future will be expected to drive explosive Internet traffic growths and thus, posing unprecedented challenges for network operators in scaling up the capacity in a greater cost and energy efficiency. Optical communications and networks constituting the backbone of Internet infrastructure will thus have to be radically different in the next 10 years and beyond. Indeed, there have been a number of on-going technological innovations holding the promises of order-of-magnitude capacity expansion, notably multi-band and/or spatial-divisionmultiplexing-based technologies. On the other hand, from an architectural perspective with the main goal of reducing the effective traffic load in the network and thus gaining greater operational efficiency, optical networks have been essentially remained unchanged in the recent two decades since the year 2000s with the success and then dominance of optical-bypass mode, featuring both significant cost and energy savings compared to the predecessor optical-electricaloptical operation. In the optical-bypass-enabled network, provisioning a lightpath involves the essential cross-connection function whose the underlying principle lies in the fact that in crossconnecting in-transit lightpaths over an intermediate node, such lightpaths must be guarded from each other in a certain dimension, be it the time, frequency or spatial domain, to avoid interference, which is treated as a destructive factor. In view of the rapid progresses in the realm of optical computing enabling the purposed interference between optical channels that are tailored to various computing capabilities, we envision a different perspective to turn around the long-established wisdom in optical-bypass network by putting the optical channel interference to a good use, resulting into the new operational paradigm, entitled, *optical-computing-enabled network*, weaving together optical communication and computing infrastructure. The opticalcomputing-enabled network is essentially characterized by the new capability at optical nodes permitting the superposition of transitional lightpaths to compute new ones of better spectrum utilization and/or for special computing purposes such as large-scale AI training. In underlining the potential merits of bringing in-network optical computing functions into the optical layer, this paper presents two illustrative examples based on the optical aggregation and optical XOR operations which have been progressively maturing and thus, could be feasibly integrated into the current legacy infrastructure with possibly minimal disruptions. As a departure from optical-bypass operation, the new optical computing capabilities available at the optical nodes imply a radical change in the network design problems and deriving the associated algorithmic

*E-mail addresses:* [hai.dao5@rmit.edu.vn](mailto:hai.dao5@rmit.edu.vn), [iwoungan@torontomu.ca](mailto:iwoungan@torontomu.ca) (I. Woungang).

<span id="page-0-1"></span><sup>∗</sup> Corresponding author.

> solutions, which are broadly termed as optical network design and planning 2.0, so that the capital and operational efficiency could be fully unlocked. As a proof-of-efficiency for the new operational paradigm, we propose a detailed case study in formulating and solving the network coding-enabled optical networks, demonstrating the efficacy of the *optical-computing-enabled network*, and highlighting the unique challenges tied with greater complexities in network design problems, compared to optical-bypass counterpart.

#### **1. Introduction**

By the end of 2023, it has been known that the Internet accessibility has reached to more than two-thirds of the global population and the remaining will soon be connected thanks to excellent initiatives aiming at connecting the unconnected and thus closing the connectivity gap [\[1,](#page-11-0)[2](#page-11-1)]. As broadband Internet services have and will become ubiquitous globally, network operators both at global, regional and national scales thus need to ensure the availability of adequate resources to sustain the quality and scale of future connectivity, particularly towards faster, more transparent, and greener communication networks [\[3–](#page-11-2)[5](#page-11-3)]. Indeed, the majority of Internet traffic today has been carried over optical communications and networks infrastructure, spanning from access, metro to core ones, providing high-capacity channels that make it possible for a plethora of services nowadays, such as Internet-of-things (IoT), Big Data and Artificial Intelligence (AI). In practice, the current fiber-optic communication is operated on a particular wavelength region called C-band featuring minimal and nearly uniform transmission losses across the band. Although C-band used to be viewed as an infinite capacity in the context of traditional voiced-dominated services, the fact that (i) its bandwidth is physically finite (i.e. about 5 THz), and (ii) there is an explosive traffic growth driven by the increasing proliferation of various data-centric and bandwidth-intensive applications, could lead to its exhaustion as resource. This well-known phenomenon is often referred as the capacity crunch problem [[6](#page-11-4)[,7\]](#page-11-5). On the other hand, as coherent transmission has been the mainstream in optical communication systems and digital signal processing plays a critical role in the coherent transceiver on the transmit and receive sides, continuing to increase the system capacity will be eventually be bottle-necked by the electronic processing limitation. Sustaining the explosive Internet traffic growth driven by the future connectivity requirements will thus entail ground-breaking innovations in the realm of optical communication and networking. Indeed, optical transport networks have been advancing year-by-year thanks to unabated technological and architectural improvements [[8](#page-11-6)[–17](#page-12-0)] and in the next 10-year time-frame, major changes encompassing both technological and architectural aspects will be envisioned, foreseeing a disruptive capacity expansion to support massive connectivity of a hyper-connected world in a greater cost and energy efficiency [[18–](#page-12-1)[21\]](#page-12-2). On one hand, technology-based approaches relying on the development of more advanced transmission systems, higher-order modulation formats and recently wideband transmission, pave the way for expanding the system capacity by orders of magnitude [[22\]](#page-12-3). Particularly, the two emerging Multi-band (MB) and Space-Division Multiplexing (SDM) transmission technologies have been garnering significant attention from both the academia and leading industrial players to boost the system capacity by many order-of-magnitude. For SDM technology, the main principle is to exploit the parallelization in transmission over a bundle of multiple fibers and/or over multi-core/mode fibers (MCF/MMF). Although SDM technology holds the promise of more than hundred-fold improvements in fiber capacity which makes it a rewarding candidate for supporting future connectivity, the main drawback yet lies in the massive requirement of deploying new types of fibers and optical components such as wavelength-selective switches, filters, and amplifiers, raising critical commercial concerns with the current stages of technologies and implementation [\[23](#page-12-4)[–25](#page-12-5)]. As an alternative potential capacity-enhancement solution, the MB-based transmission exploiting the remaining available spectrum in the conventional single-mode fibers (SMFs) in addition to the C-band may represent a viable route to sustain the traffic growth in the near-term perspective. As conventional networks likely reaching their physical limit soon, a.k.a, capacity crunch, the MB transmission may appear as a practical and promising upgrade direction with minimal disruption with the current infrastructure. Indeed, it has been experimentally reported that a more than ten-fold capacity expansion could be achieved with the MB transmission [[23,](#page-12-4)[26\]](#page-12-6).

On the architectural front where the major goal is less on enlarging the system capacity, but more on reducing the effective network traffic and thus dropping the capital and operational cost of per-transmitted bits, optical networking has been gradually migrated from the simple point-to-point connections based on the optical-electrical-optical (O-E-O) mode to optical-bypass operations; the key difference being that the transiting lightpaths in optical-bypass mode, rather than undergoing unnecessary and costly O-E-O conversions, could profit from optical cross-connect at intermediate nodes en route from the source to destination [[27–](#page-12-7)[35\]](#page-12-8). Thanks to massive gains enabled by optical-bypass mode and rapid advances in both devices, systems and networking technologies permitting the wide deployments of optical-bypass-enabled networks, such networks have remained the architecture of choice by worldwide operators in the last two decades since the year 2000s [\[36](#page-12-9)]. In optical-bypass framework, the add/drop and cross-connect functions constitute the fundamental operations in handling the traffic at the optical layer, where the underlying principle lies in the fact that in cross-connecting in-transit lightpaths over an intermediate node, these lightpaths must be guarded from each other in either time, frequency or spatial domain, to avoid interference which is treated as destructive [[36,](#page-12-9)[37\]](#page-12-10). This turns out to be a fundamental limitation as various optical computing operations could be performed between such transitional lightpaths to produce the new ones which could be spectrally more-efficient than its inputs and/or could serve special computing purposes at scale such as training large-scale AI models. Inspired by the rapid progresses in the realm of optical computing enabling the controlled interference of optical channels that are tailored to various computing capabilities, we envision a different perspective to turn around the longestablished wisdom in optical-bypass network, by putting the optical channel interference to a good use, resulting into the so-called

optical-computing-enabled network and that potentially marks the next frontier of optical network architecture with the arrival of optical communication-computing integrated networks. Our proposal is essentially defined by the added capability of optical nodes leveraging the superposition of transitional lightpaths to compute new ones of greater capacity efficiency and/or for emerging large-scale AI-training computing services. In particular, two illustrative examples underlining the potential merits of bringing about in-network optical computing functions, that is, optical aggregation and optical XOR gate, are presented. The new optical computing capabilities armed at optical nodes therefore necessitate a radical change in the manner that network problems should be formulated and their associated algorithmic solutions be investigated. This paradigm shift is collectively referred as optical network design and planning 2.0. As a continuation of our previous works on promoting optical-layer intelligence in handling traffic in a greater spectral efficiency manner [[38](#page-12-11)[–52](#page-13-0)] and the extension of our conference paper [\[53](#page-13-1)], this work proposes a case study for network-codingenabled optical networks, showing the efficacy of optical-computing-enabled network and the unique challenges that are tied with greater complexities in network design problems compared to the optical-bypass counterpart. Note that the term *optical-processingenabled network* was first used in our previous works [\[39](#page-12-12),[43\]](#page-12-13) to denote a new possibility of manipulating in-transit lightpaths in optical domain for improving spectral efficiency, as a departure from the legacy optical-bypass-enabled network. Although opticalprocessing-enabled and optical-computing-enabled network could be used interchangeably, the latter one is particularly inclined to the vision where many computing functions are pushed down to the optical layer, leveraging the photon's bandwidth and energyefficiency, paving the way for the era of optical-layer intelligence. The optical communication infrastructure will thus be repurposed to include optical computing services, resulting into the seamless optical computing-communication integrated network addressing both the scalability challenges of explosive traffic growth and the rise of massive AI-model training, particularly in the context towards the carbon-neutral economy [\[54](#page-13-2)[–58\]](#page-13-3).

The remainder of the paper is structured as follows. In Section [2,](#page-2-0) the concept of optical-computing-enabled paradigm is described in-depth, and the applications of two optical computing operations, i.e., optical aggregation and optical XOR, are highlighted. The computational impact and intricacies for network design and planning in the paradigm of optical-computing-enabled networking, is also addressed. In uncovering the more complicated network design problem arisen in the optical computing-communication network, a.k.a optical-computing-enabled network, a mathematical formulation for solving the routing, wavelength and network coding assignment problem, which is based on the integer linear programming (ILP) model, is presented in Section [3.](#page-6-0) In Section [4](#page-7-0), we show some numerical evaluations, where our proposal which leverages the use of optical XOR encoding within the framework of optical-computing enabled mode, is compared against the traditional optical-bypass networking paradigm, using realistic COST239 and NSF NET network topologies. We also highlight the critical difference between solving the traditional routing and wavelength assignment (RWA) problem arisen in the context of optical-bypass mode to its evolved variant, i.e. the routing, wavelength and network coding assignment problem (RWNCA) emerged in the new operational paradigm, optical-computing-enabled mode. Finally, Section [5](#page-10-0) concludes the paper and highlights potential future works.

## **2. Optical computing-communication integrated network**

<span id="page-2-0"></span>In 1965, a groundbreaking prediction appeared in the Electronics magazine which has then become the famous Moore's law that governed the evolution of integrated circuits complexity for over five decades, enabling the use of billions of transistors in chip designs. However, the era of predictable transistor scaling is showing signs of abating; new paradigm shifts are therefore constantly sought out to advance the computing performance, particularly in the context of massive computing requirements from AI-driven applications. One promising solution is the transition to photonic-based computing and in that endeavor, silicon photonics demonstrated by Intel in 2013, showcased reduced power consumption and size while achieving superior speed compared to the conventional electronic computing counterparts [[59\]](#page-13-4). Leading tech companies have then been actively exploring silicon photonics such as Broadcom developing 25.6 Tb/s and 51.2 Tb/s co-packaged switches, integrating PICs with ASIC SerDes. Cisco has been developing large-scale silicon photonic PICs for diverse applications while HP has been using silicon photonics for HPC applications, achieving high bandwidth and low-power operation. IBM has recently announced a \$3 billion investment to explore next-generation low-power transistors and silicon photonics, among other pioneering initiatives [\[60](#page-13-5)[–63](#page-13-6)]. In the wake of AI-driven computing, massive investments have been targeted to light-based solutions, such as those from LightIntelligence and LightMatter companies to accelerate the AI developments by exploiting the computing capability at the speed of light [\[64](#page-13-7)[–67](#page-13-8)]. The rapid rise of optical computing thus begs a question on the need to re-design the current optical transport network to provide a fertile soil for utilization of photons in computing.

For many years, optical communication and networks have been serving the transportation of information from one point to another while the computing is performed at the electrical layer. Optical layer thus plays a static role in handling the traffic, where en route from the source to destination, the optical channel is simply cross-connected over intermediate nodes without further processing/computing operations. Inspired by the renewed interests and then rapid advances in optical computing technologies, it would be envisioned to have a paradigm shift from the current optical communication networks to the optical communicationcomputing integrated networks, where both the transmission and computing functions are available at the optical layer. Our proposal is named as optical-computing-enabled network to differentiate itself from the currently used optical-bypass mode. As a major departure from the legacy infrastructure, optical-computing-enabled network featuring the interaction of transitional optical channels paves the way for redefining the optical network architecture, turning around the conventional assumption of keeping the transitional lightpaths untouched. In this context, the optical-computing-enabled framework could be foreseen as a part of the next evolution of optical-bypass networking.

This section is dedicated to illustrate the efficient use and consequently network-wide impact of introducing two optical computing operations, namely, optical aggregation/de-aggregation and optical XOR into the optical layer of the optical transport networks. It is worth noting that the enabling technologies for realizing such these two optical computing operations have been rapidly accelerating, paving the way for technological readiness of upgrading optical nodes with optical computing functionalities. Besides, while the discussion in this section is restricted to the two operations, it does not exclude other optical computing operations that could be performed at the lightpath scale. Indeed, as photonic computing technologies move forward, a wide range of computing functions could be technologically feasible and such advances will be expected to have massive impacts to optical networks from both the design, planning, operation and management standpoints.

#### 2.1. Optical aggregation/de-aggregation

It remains an essential function in the operation of optical networks concerning the efficient aggregation of lower-speed channels into a single higher-speed one so that high-capacity optical channels could be optimally utilized. The more efficient the aggregation is, the greater capacity efficiency could be achieved thanks to freeing up the lightpaths of lower wavelength utilization. In optical transport networks, the aggregation functionality has been conventionally performed in the electronic domain which includes terminating the optical channels, re-assembling, re-modulating and eventually back-converting them to the optical domain. As the optical channels operate at an increasingly higher rate, that traditional way of aggregation poses many limitations and clearly it is not scalable for the era of very high bit-rate operations. As a potential solution, the concept of optical aggregation has been recently proposed, investigated and experimentally demonstrated [68–70]. The leading tech company for this revolutionary effort, Infinera, has been stepping up to develop a new ecosystem of devices and components with the capability of transforming the traditional operation of optical nodes [71–74].

From the implementation perspective, optical aggregation and de-aggregation have been realized by exploiting the nonlinear effects when two or more optical channels co-propagate in a nonlinear medium. Specifically, the second and/or third-order susceptibility of nonlinear mediums such as highly nonlinear fiber and semiconductor optical amplifiers resulting in nonlinear phenomenons, i.e., four-wave mixing, cross-phase modulation, self-phase modulation, and cross-gain modulation have been the major mechanism to implement optical aggregation and de-aggregation functions [69,70,75,76]. From the functional perspective, two or more optical channels of lower bit-rate and lower-order modulation format could be optically added together into a single higher bit-rate and higher-order modulation format thanks to using an optical aggregator. In the following illustrative case, the utilization of an optical aggregator to combine two QPSK signals into a single 16-QAM channel and an optical de-aggregator for the vice-versa are examined. Fig. 1 depicts the schematic diagram for the addition of two QPSK channels of lower bit-rate into a single 16-QAM channel of higher rate, leading to two-fold improvement in the spectral efficiency.

In revealing how to achieve network-wide profit from using the above optical aggregator, we first consider the conventional way of accommodating the traffic demands in optical-bypass networking. Fig. 2 shows the routing and wavelength assignment for two demands a and b of the same line-rate 100G and format QPSK. In the absence of a wavelength converter, it is well-known that due to the wavelength uniqueness constraint, two wavelengths are required on link XI and IC. Now lets switch to a different perspective, supposing that at node X, the optical aggregation is enabled. Under such new operational paradigm, the two 100G QPSK transitional lightpaths  $a_{\lambda_1}$  and  $b_{\lambda_1}$  crossing the same node X could be optically interfered with each other to generate the output signal of 200G which is modulated on 16-QAM format and on the same wavelength  $\lambda_1$  (i.e.,  $(a+b)_{\lambda_1}$ ) and that aggregated lightpath carrying the traffic of both demand a and b is routed all the way to the destination node. At the common destination node C, the aggregated lightpath undergoes the de-aggregation process to extract constituent ones and such decomposition operation could be performed either in the optical and electrical domain. It should be bear in mind that the computing sense in this context is interpreted as the addition of bits-per-symbol, that is, 2 bits/symbol for QPSK and 4 bits/symbol for 16-QAM. In comparing two approaches for accommodating the traffic demands, it is clearly observed from the Fig. 3 that the optical-computing-enabled one results into greater capacity efficiency as for the whole network, a single wavelength is required compared to the two wavelengths requirement for the optical-bypass one.

It is worth noting that the optical-computing-enabled paradigm paves the way for a new dimension, that is, the interference of transitional lightpaths for computing purposes and it leads to new network design and planning algorithms so that network-wide gain could be fully attained. In the case of the above optical aggregation, the added complexity lies in selecting pairs of lightpaths for aggregation, the corresponding aggregation node, and more importantly, the determination of the route and wavelength for the aggregated lightpaths.

#### 2.2. Optical XOR encoding/decoding

Photonic-based logic gates technologies have been rapidly accelerating in recent years, making it feasible to perform the bit-wise exclusive-or (XOR) between optical signals of very high bit-rates and/or different modulation formats [67,77]. A schematic representation of such device is depicted in Fig. 5(a), where two optical signals carrying 100G modulated on the same wavelength and format QPSK are optically XOR-coded to produce the output X of the same bit-rate, format and wavelength.

The utilization of optical XOR at the optical layer in optical transport networks is illustrated in this part through the protection scenario. Assuming that there are two demands a and b requesting the same bit-rate of 100G from node A and node B, respectively to node C. Both demands are also under the dedicated protection scheme. One way of provisioning such two demands are shown in Fig. 4 for the optical-bypass framework where the route and wavelength for both working and backup lightpaths of both demands are

![](_page_4_Figure_1.jpeg)

<span id="page-4-0"></span>**Fig. 1.** Schematic representation of the optical aggregation operation: Adding two QPSK signals to generate one 16-QAM signal.

![](_page_4_Figure_3.jpeg)

**Fig. 2.** Provisioning two requests in the optical-bypass networking.

<span id="page-4-1"></span>![](_page_4_Figure_5.jpeg)

**Fig. 3.** Optical-computing-enabled paradigm with optical aggregation and de-aggregation.

<span id="page-4-2"></span>determined subject to typical constraints of wavelength uniqueness and link-disjointedness. It is noticed that as the backup lightpath of demands and crossing the same links and , it therefore requires two wavelengths on those links as a consequence of wavelength uniqueness constraint. We now turn the attention to the case of optical-computing-enabled paradigm when node is armed with the optical XOR encoding capability as shown in [Fig.](#page-5-0) [5](#page-5-0)(b). Under this assumption, the backup signal of demand and demand could thus be optically XOR-encoded with each other at node X to produce the new lightpath = *⊕* of the same bit-rate, format and same wavelength as the inputs. That new computed lightpath carrying the encoded traffic between demand and is routed all the way from node to the shared destination node , consuming a single wavelength channel on both link and which results in a spectral saving of 50% compared to the optical-bypass mode. In facing single-link failure events on the working paths, the recovery capability for both demand and demand is guaranteed by making use of the XOR operation on the two remaining signals. Specifically, if the working signal of demand is lost, it can be retrieved alternatively by the following operation: = ( *⊕* ) *⊕* and the same principle is applied in the lost of the working signal of demand .

![](_page_5_Figure_2.jpeg)

**Fig. 4.** Provisioning two requests with dedicated protection in optical-bypass networking.

<span id="page-5-1"></span>![](_page_5_Figure_4.jpeg)

**Fig. 5.** Optical-computing-enabled paradigm with optical XOR encoding and decoding.

<span id="page-5-0"></span>As shown in the above illustration, the use of optical XOR encoding in the context of dedicated protection appears to be a good match as it can, on one hand, attain greater capacity efficiency while on the other hand, still retaining the merit of near-immediate recovery speed. In a general case, exploiting the network coding benefits rely on the capability to solve more complicated network design problems. Specifically, the added complexity lies in determining a set of pairs of demand for encoding, together with encoding nodes and the selection of routes and/or transmission parameters for encoded lightpaths.

### *2.3. Network design and planning: Optical-computing-enabled vs. Optical-bypass framework*

It is worth noting that the *optical-computing-enabled* paradigm featuring the interference among two or more favorable lightpahts for computing purposes introduces more networking flexibility as a new dimension accounting for the interaction of lightpath is established. Such new dimension clearly poses significant ramifications in both the formulation and solving network design and planning problems to fully tap into the potential benefits [[39](#page-12-12),[44,](#page-12-14)[46–](#page-12-15)[48,](#page-12-16)[55](#page-13-17)[,56](#page-13-18)].

In optical-bypass networking, the routing and wavelength assignment (RWA) problem remains the central one in design, planning and operation of a network, determining the network efficiency. In essence, solving the traditional RWA problem involves the selection of a route and the assignment of transmission parameters including wavelength/spectrum and/or format for each individual demand subject to a set of typical constraints including mainly the wavelength uniqueness, wavelength continuity and/or contiguity. Unlike in optical-bypass, more complicated network design problems arise in the optical-computing-enabled paradigm due to the interaction of the transitional lightpaths. Specifically, beyond identifying the route and wavelength/spectrum for each demand, the determination of pairs of lightpath to compute and the corresponding node needs to be taken into account. Furthermore, the arrival of special lightpaths resulting from the interaction of two or many demands gives rise to the issue of selecting their route and assigning their wavelength/spectrum. That said, the RWA problem is extended by an additional dimension, which may generally be referred as the computing assignment involving the pairing of in-transit lightpaths for computing purposes. This represents a major departure in the network design and planning, leading to a revisit of the traditional set of algorithms that have been well-developed for optical-bypass networking in many years. In addressing this fundamental shift, a new framework that may collectively be named

as optical network design and planning 2.0 should be investigated and developed, encompassing new problems emerging from the various ways that transitional lightpaths could be optically mixed, and the associated algorithms that include exact/heuristic solutions for solving them could be derived.

In the next part, we showcase the problem, entitled, the routing, wavelength and network coding assignment problem (RWNCA) arisen in the utilization of optical XOR in the context of optical-computing-enabled network, along with the mathematical formulation in the form of the integer linear programming model for optimally solving it.

#### 3. A mathematical formulation for optical-computing-enabled network design with optical XOR encoding and decoding

<span id="page-6-0"></span>This section is focused on the case of designing network-coding-enabled optical networks in supporting a given set of traffic demands such that the wavelength link utilization is minimized. The optical network coding scheme utilized is the simple XOR operation. The optical XOR gate receives input signals of the same wavelength, line-rate and format and then produces the XOR-coded version output of the same wavelength and format and line-rate as inputs. Such XOR coding between signals of the same wavelength features the distinct advantage, that is, the elimination of a probe signal and therefore, could lead to greater cost-efficiency and less operational complexity [78]. Besides, for the practical purpose of easing the operation as the optical XOR is introduced at the optical layer, the optical encoding is permitted to be performed only on the backup signals of demands that share the destination node. We also assume that there is a maximum of one encoding operation for each demand and thus, the decoding, if any, is only allowed at the destination. As a consequence of the aforementioned assumptions, following constraints on the network coding assignment for any two code-able demands must be ensured: (i) two demands must have a common destination (ii) two demands must use same wavelength (iii) the link-disjointedness constraint between two demands' working paths and one's working to the another's backup path (iv) the two demands's backup paths must have a common sub-path whose one end is the common destination of two demands.

Inputs:

- G(V, E): A graph models the physical network topology consisting of |V| nodes and |E| fiber links. The beginning and ending node making up a link  $e \in E$  is represented by s(e) and r(e), respectively.
- D: A set of traffic demands, indexed by d. The source and destination node of a demand  $d \in D$  are notated respectively as s(d) and r(d), and all demands are assumed to request the same wavelength capacity (e.g., 400G)
- W: A set represents available wavelengths on each fiber link, indexed by w. The link capacity measured in number of
  wavelength is |W|

#### Design Variables:

- $\alpha_{e,w}^d \in \{0,1\}$ : equals 1 if link e and wavelength w is used for working path of demand d, 0 otherwise.
- $\beta_{e,w}^d \in \{0,1\}$ : equals 1 if link e and wavelength w is used for the backup path of demand d, 0 otherwise.
- $\theta_w^d \in \{0,1\}$ : equals 1 if wavelength w is used for demand d, 0 otherwise.
- $z_{e.w}^{d,v} \in \{0,1\}$ : equals 1 if demand d on wavelength w is encoded at node v and the coding path includes link e, 0 otherwise
- $\delta_v^d \in \{0,1\}$ : equals 1 if at node v, demand d is encoded with another demand, 0 otherwise
- $f_{d_1}^{d_2} \in \{0,1\}$ : equals 1 if demand  $d_1$  is encoded with demand  $d_2$ , 0 otherwise
- $\gamma_{ew}$ : equals 1 if wavelength w is used on link e, 0 otherwise

### Objective function:

$$Minimize \sum_{e \in E} \sum_{w \in W} \gamma_{e,w} \tag{1}$$

Subject to:

$$\sum_{w \in W} \theta_w^d = 1 \ \forall d \in D$$
 (2)

<span id="page-6-6"></span><span id="page-6-5"></span><span id="page-6-4"></span><span id="page-6-3"></span><span id="page-6-2"></span><span id="page-6-1"></span>
$$\sum_{e \in E : v \equiv s(e)} \alpha_{e,w}^d(\beta_{e,w}^d) - \sum_{e \in E : v \equiv r(e)} \alpha_{e,w}^d(\beta_{e,w}^d) =$$

$$\begin{cases} \theta_{w}^{d} & \text{if } v \equiv s(d) \\ -\theta_{w}^{d} & \text{if } v \equiv r(d) \\ 0 & \text{otherwise} \end{cases} \quad \forall v \in V, \forall d \in D, \forall w \in W$$
 (3)

$$\alpha_{e,w}^d + \beta_{e,w}^d \le 1 \qquad \forall d \in D, \forall w \in W, \forall e \in E$$
 (4)

$$\sum_{d \in D} \alpha_{e,w}^d + \sum_{d \in D} \beta_{e,w}^d - \frac{1}{2} \sum_{d \in D} \sum_{v \in V} z_{e,w}^{d,v} = \gamma_{e,w}$$
(5)

$$\forall e \in E, \forall w \in W$$

$$\sum_{v \in V} \delta_v^d \le 1 \quad \text{and} \quad \delta_v^d = 0 \quad \text{if } v \equiv r(d) \quad \forall d \in D$$
(6)

<span id="page-7-1"></span>
$$\sum_{d \in D} f_{d_1}^{d_2} \le 1 \qquad \forall d_1 \in D \tag{7}$$

$$f_{d_1}^{d_1} + \sum_{d_2 \in D: r(d_2) \neq r(d_1)} f_{d_2}^{d_1} = 0 \qquad \forall d_1 \in D$$
 (8)

<span id="page-7-3"></span><span id="page-7-2"></span>
$$f_{d_1}^{d_2} = f_{d_2}^{d_1} \qquad \forall d_1, d_2 \in D \tag{9}$$

$$\sum_{d_2 \in D} f_{d_1}^{d_2} = \sum_{v \in V} \delta_v^{d_1} \qquad \forall d_1 \in D \tag{10}$$

$$\sum_{w \in W} \sum_{v \in V} z_{e,w}^{d_1,v} \le \sum_{d_1 \in D} f_{d_1}^{d_2} \qquad \forall d_1 \in D, \forall e \in E$$

$$\tag{11}$$

$$\sum_{u \in V} z_{e,w}^{d,v} \le \delta_v^d \qquad \forall d \in D, \forall v \in V, \forall e \in E$$
(12)

$$\sum_{w \in W} \alpha_{e,w}^{d_1} + \sum_{w \in W} \alpha_{e,w}^{d_2} + f_{d_1}^{d_2} \le 2 \qquad \forall d_1, d_2 \in D, \forall e \in E$$
(13)

$$\sum_{w \in W} \alpha_{e,w}^{d_1} + \sum_{w \in W} \beta_{e,w}^{d_2} + f_{d_1}^{d_2} \le 2 \qquad \forall d_1, d_2 \in D, \forall e \in E$$
(14)

$$\theta_w^{d_1} - \theta_w^{d_2} + f_{d_1}^{d_2} \le 1 \qquad \forall d_1, d_2 \in D, \forall w \in W$$
 (15)

$$\theta_w^{d_2} - \theta_w^{d_1} + f_{d_1}^{d_2} \le 1 \qquad \forall d_1, d_2 \in D, \forall w \in W$$
 (16)

$$\delta_{v}^{d_{1}} - \delta_{v}^{d_{2}} + f_{d_{1}}^{d_{2}} \le 1 \qquad \forall d_{1}, d_{2} \in D, \forall v \in V$$
 (17)

$$\delta_v^{d_2} - \delta_v^{d_1} + f_{d_1}^{d_2} \le 1 \qquad \forall d_1, d_2 \in D, \forall v \in V$$
 (18)

$$z_{e,w}^{d,v} \le \beta_{e,w}^d \qquad \forall d \in D, \forall v \in V, \forall e \in E, \forall w \in W$$
 (19)

<span id="page-7-12"></span><span id="page-7-11"></span><span id="page-7-10"></span><span id="page-7-9"></span><span id="page-7-8"></span><span id="page-7-7"></span><span id="page-7-6"></span><span id="page-7-5"></span><span id="page-7-4"></span>
$$\sum_{w \in W} (\sum_{e \in E: i = s(e)} z_{e,w}^{d,v} - \sum_{e \in E: i = r(e)} z_{e,w}^{d,v}) =$$

$$\begin{cases} \delta_v^d & \text{if } i \equiv v \\ -\delta_v^d & \text{if } i \equiv r(d) \\ 0 & \text{otherwise} \end{cases} \quad \forall d \in D, \forall v \in V, \forall i \in V$$

The objective function in Eq. (1) aims at minimizing the wavelength link cost. The constraints in Eq. (2) is to guarantee that all demands are served by finding the proper wavelength. The conservation for both the working and backup flow are ensured by the constraints formulated in Eq. (3). The link-disjointedness condition between the working and backup route is captured in Eq. (4). The wavelength uniqueness condition on each link is guaranteed by Eq. (5). The assumption that each demand has at most one coding node which is different from its destination is ensured by Eq. (6). The condition that each demand is coded with at most one another demand of the same destination is indicated by the constraints in Eqs. (7)–(9). Constraints formulated in Eqs. (10)–(12) are for coherence purpose, i.e., if a demand is encoded, the respective coding node, coding links and coding wavelength must be found. Constraints given in Eqs. (13) and (14) are to guarantee that if two demands are encoded with each other, their working routes must be link-disjointed and the working route of one demand must also be link-disjointed with the backup route of another demand. Such constraint are to ensure the recovery capability against any single link failure. The same wavelength condition for code-able demands is captured in Eqs. (15) and (16). Constraints in Eqs. (17) and (18) mean that if two demands are encoded together, the same coding node must prevail. The coherence between coding link(s) and backup route is expressed by Eq. (19). The last constraint in Eq. (20) is the traditional flow conservation one.

The above formulation is in the form of an integer linear programming model whose complexity is well-known to be NP-hard. It is worth noting that in addition to the standard variables and constraints representing the route selection and wavelength assignment for each demand, new variables and constraints accounting for the interference of transitional lightpaths for computing purposes have been introduced. Specifically, the existence of variable  $z_{e,w}^{d,v} \in \{0,1\}$  and constraints in Eq. (20) give the rise to the model one order of magnitude computationally harder than its counterpart, that is, the traditional routing and wavelength assignment in optical-bypass networking. In acknowledging the NP-hard nature of the model, we therefore propose the following scalable heuristic as described in Fig. 6 to be used in large-scale networks.

# 4. Numerical simulation results

<span id="page-7-0"></span>This section is dedicated to reveal numerical simulation results drawing on a comparative evaluation between our proposal that leverages the efficient use of optical XOR encoding within the framework of optical-computing-enabled networks and the traditional optical-bypass networking. The comparison is experimented on the realistic COST239 and NSFNET network topologies

![](_page_8_Figure_2.jpeg)

**Fig. 6.** Flowchart of the heuristic algorithm for solving the routing, wavelength and network coding assignment problem.

<span id="page-8-0"></span>**Table 1** Performance comparison between NC-based (NC) and conventional design (w-NC) [[53](#page-13-1)].

<span id="page-8-1"></span>

| Load |            |      | Optimal solution from the ILP-based model | Heuristic |      |                   |  |
|------|------------|------|-------------------------------------------|-----------|------|-------------------|--|
|      | w-NC<br>NC |      | Relative gain                             | w-NC      | NC   | Relative gain     |  |
| 30%  | 32.6       | 30.6 | Max: 9%, Mean: 6%                         | 32.6      | 31.2 | Max: 9%, Mean: 4% |  |
| 70%  | 75.8       | 67.9 | Max: 12%, Mean: 10%                       | 75.8      | 70.6 | Max: 9%, Mean: 7% |  |
| 100% | 108        | 99   | Max=Mean= 8%                              | 108       | 100  | Max=Mean= 7%      |  |

which are shown in [Fig.](#page-9-0) [7.](#page-9-0) The considered performance metric is the conventional wavelength link cost that represents the spectrum utilization efficiency in supporting a given set of traffic demands. Two designs, w-NC and NC, are brought into consideration where the former refers to the design based on the solving the routing and wavelength assignment problem in optical-bypass networking while the latter is obtained from solving the more advanced problem, i.e., routing, wavelength and network coding assignment in optical-computing-enabled networks.

As both the RWA and RWNCA problem is known to be NP-hard complexity, we first evaluate the optimal solutions from solving their ILP models on a small-scale topology including 6 nodes of all degree three, as shown in [Fig.](#page-8-0) [6\(](#page-8-0)a) and compare that with the heuristic ones. The traffic under consideration is generated randomly between nodes with uniform bit-rate requirement (i.e., one wavelength capacity) and the fiber capacity is assumed to be large enough to support all demands (i.e., in our studied case, it is set to be 40 wavelengths). The traffic loads are simulated to represent various conditions from the light, medium and high one corresponding to 30%, 70% and 100% (full-mesh) node-pair traffic exchange. Apart from the full-mesh case, for each other traffic condition, there are 20 instances to be simulated. The result in [Table](#page-8-1) [1](#page-8-1) is thus averaged across 20 samples. For the network codingbased design (NC) in full-mesh traffic, as the execution time was observed to be exceedingly long and thus, the non-optimal results were collected after 10 h of running. As revealed in [Table](#page-8-1) [1,](#page-8-1) the well-studied heuristic for w-NC achieved optimal results which are on a par with its ILP model while the heuristic for NC produced reasonably good solutions with very close gap compared to its ILP model, avoiding the overly long computational time. In view of the sub-optimal nature of heuristic algorithms, the gain obtained by these algorithms were slightly reduced compared to the one from ILP [\[53](#page-13-1)].

As the heuristic algorithm's performance for the NC-based design has been verified on the small-scale topology, that algorithm was then used for the larger networks, that is, NSFNET and COST239 topologies, under the same setting about the traffic generation, fiber capacity and number of traffic instances. The obtained results were shown in [Table](#page-9-1) [2](#page-9-1). It is observed that up to about 8% gain could be achieved with the NSFNET network. For the more densely connected COST239 network, the lower gain of up to 5% was realized. It is worth noting that in our studied cases, the NC-based design is consistently better than that from the w-NC design,

**Table 2** Numerical results for realistic topologies [[53\]](#page-13-1).

<span id="page-9-1"></span>

| Network | Load | w-NC  | NC    | Relative gain       | Average no of<br>coding operations |
|---------|------|-------|-------|---------------------|------------------------------------|
|         | 30%  | 318.3 | 299.5 | Max = 8%, Mean = 6% | 9.7                                |
| NSFNET  | 70%  | 730.4 | 682.4 | Max = 8%, Mean = 7% | 24.5                               |
|         | 100% | 1048  | 981   | Max = Mean = 6%     | 35                                 |
|         | 30%  | 126.2 | 123.3 | Max = 3%, Mean = 2% | 1.4                                |
| COST239 | 70%  | 295.6 | 285.4 | Max = 5%, Mean = 3% | 5.1                                |
|         | 100% | 420   | 404   | Max = Mean = 4%     | 8                                  |

![](_page_9_Figure_3.jpeg)

<span id="page-9-2"></span>**Fig. 7.** Network topologies under investigation.

<span id="page-9-0"></span>resulting in therefore an improved capacity efficiency. Compared to the findings on the O-E-O case as reported in [\[79](#page-13-20)], where the gain was known to be up to 20%, there was a reduced gain in the all-optical case. This may be due to the wavelength-related constraints for network coding assignments, curbing the coding capability among the demands. Moreover, it should be noted that the gain is highly dependent on the structure of the network topology, traffic and network design algorithms.

#### *4.1. A closer look on the difference between the general Routing, Wavelength and Network Coding Assignment Problem versus the traditional Routing and Wavelength Assignment*

In this part, we highlight the critical difference between solving the Routing, Wavelength and Network Coding Assignment Problem and the traditional Routing and Wavelength Assignment through an instance of traffic matrix shown in [Table](#page-10-1) [3.](#page-10-1) For simplicity and yet without the loss of generality, the traffic matrix is selected so that there is a high opportunity for encoding between the backup lightpaths. Specifically, there are two source nodes, that is, node 5 and node 10, while there are 6 common destination nodes. For the purpose of illustration, we slightly modify the objective function in Eq. [\(1\)](#page-6-1) to become Eq. [\(21](#page-9-2)) as followed.

$$Minimize \sum_{w \in W} x_w + \frac{1}{|E||W|+1} \sum_{e \in E} \sum_{w \in W} \gamma_{e,w}$$
 (21)

The new objective formulated in Eq. [\(21](#page-9-2)) consists of two weighted sub-objectives where the first and prioritized one is to minimize the number of used wavelengths and the secondary goal is to minimize the wavelength link usage. The priority of constituent objectives and consequently the order of optimization is ensured by putting the proper weights as shown in the equation.

[Table](#page-10-2) [4](#page-10-2) showcases the routing and wavelength assignment for the working and backup paths of all demands. Note that the solution provides a standard information similar to what is obtained when solving the traditional routing and wavelength assignment. Overall, there are six wavelengths needed to support the traffic demands. However, as there are the interaction between backup lightpaths by the optical XOR operation, the determination of which pair of demands are encoded together and at which node such encoding operation occurs should be found and optimized. Also, as the consequence of encoding backup lightpaths and it results in computed lightpaths of greater efficiency than the original ones, the routing and allocating wavelength for such newly appeared lightpaths must be taken into account. In term of complexity, solving the RWNCA problem therefore is one order of magnitude computationally harder than the traditional RWA. [Table](#page-10-3) [5](#page-10-3) highlights the added information obtained from solving RWNCA where

**Table 3** An instance of traffic matrix.

<span id="page-10-1"></span>

| NodeID | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|--------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|
| 1      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 2      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 3      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 4      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 5      | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 6      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 7      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 8      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 9      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 10     | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 11     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 12     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 13     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |
| 14     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  |

**Table 4** Routing and wavelength allocation information for traffic demands.

<span id="page-10-2"></span>

| Source node → Destination node | W-path        | W-𝜆 | B-path          | B-𝜆 |
|--------------------------------|---------------|-----|-----------------|-----|
| 5 → 1                          | (5-4-2-1)     | 5   | (5-7-3-1)       | 2   |
| 10 → 1                         | (10-11-8-1)   | 5   | (10-7-3-1)      | 1   |
| 5 → 2                          | (5-4-2)       | 4   | (5-7-3-2)       | 6   |
| 10 → 2                         | (10-11-8-1-2) | 4   | (10-7-3-2)      | 6   |
| 5 → 3                          | (5-4-2-3)     | 6   | (5-7-3)         | 3   |
| 10 → 3                         | (10-11-8-1-3) | 1   | (10-7-3)        | 5   |
| 5 → 4                          | (5-4)         | 1   | (5-7-3-2-4)     | 5   |
| 10 → 4                         | (10-11-1-9-4) | 3   | (10-7-3-2-4)    | 4   |
| 5 → 6                          | (5-4-2-1-8-6) | 3   | (5-6)           | 5   |
| 10 → 6                         | (10-11-8-6)   | 6   | (10-7-5-6)      | 3   |
| 5 → 7                          | (5-7)         | 1   | (5-6-8-1-3-7)   | 6   |
| 10 → 7                         | (10-7)        | 2   | (10-11-8-1-3-7) | 2   |

**Table 5** Network coding assignment information between backup lightpaths.

<span id="page-10-3"></span>

| Computed lightpaths | Computing node | Route     | Wavelength assignment |  |  |
|---------------------|----------------|-----------|-----------------------|--|--|
| (5 → 1) ⊕ (10 → 1)  | 7              | (7-3-1)   | 2                     |  |  |
| (5 → 2) ⊕ (10 → 2)  | 7              | (7-3-2)   | 5                     |  |  |
| (5 → 3) ⊕ (10 → 3)  | 7              | (7-3)     | 6                     |  |  |
| (5 → 4) ⊕ (10 → 4)  | 7              | (7-3-2-4) | 4                     |  |  |
| (5 → 7) ⊕ (10 → 7)  | 8              | (8-1-3-7) | 1                     |  |  |

the pair of demands for encoding, the encoding node, the route as well as the wavelength for computed lightpaths are optimally provided. It is important to note that the spectral gain from exploiting the optical XOR operation comes at the expenses of solving a more difficult network design problem, which is, RWNCA.

#### **5. Summary**

<span id="page-10-0"></span>In supporting the connectivity of the future driven by the fusion of digital and physical world, network operators have been constantly seeking out innovative solutions to upgrade their network infrastructures so that more traffic could be supported in a greater cost and energy efficiency manner, in addition to supporting stricter requirements on resilience, security and latency. From transmission perspectives, space division multiplexing and ultra-wideband optical technologies have been proposed, actively investigated and progressively experimented to increase the per-fiber capacity by orders-of-magnitude, marking the paradigm shift compared to the current legacy infrastructure. On the parallel front, optical computing has been advancing rapidly to support emerging large-scale AI training services. Optical network architecture has though remained essentially unchanged for the two recent decades since 2000s with the dominance of optical-bypass mode that has successfully integrated technological innovations of its time such as long-haul coherent transmission and reconfigurable optical add/drop multiplexer. This context therefore begs a new architecture that holds the promises of making best uses of technological advances, that is, new optical transmission and optical computing, to support massive connectivity, including future pervasive AI computing traffic.

In this paper, we have challenged the status quo with a new perspective of integrating optical computing layer into the traditional legacy optical communication infrastructures, resulting into the new realm of optical communication-computing integrated networks. Our proposal was named as optical-computing-enabled network whose the underlying principle is to reverse the wisdom in optical-bypass operation, that is, instead of keeping in-transit lightpaths over an intermediate node apart from each other in either

time, frequency or spatial domain, exploiting the superimposing of such lightpaths in the optical domain for computing purposes is proposed as a way to achieve greater network efficiency. Two illustrative examples highlighting the efficient uses of optical aggregation and optical XOR have been presented and contrasted with the optical-bypass mode. In addressing the new operational paradigm enabled by optical-computing-enabled mode, we have then presented the mathematical formulation for optimal designs of network coding-enabled optical networks. Numerical results evaluating our proposal on the realistic networks, COST239 and NSFNET have been provided, demonstrating its efficacy in comparison with the conventional operation in optical-bypass mode. We have also gone deeper to pinpoint the critical difference in solving the new routing and resource allocation arisen in opticalcomputing-enabled mode, that is, routing, wavelength and network coding assignment (RWNCA) and the traditional routing and wavelength assignment (RWA).

The inherent merit of light over electronic for computing, particularly in the background of ending of Moore's law and massive investment for AI accelerators has put light-based computing solutions at a rapid growth than ever. The rise of optical computing and the quest for both capacity expansion and energy efficiency in optical transport networks have thus been creating a ripe environment for the integration of optical communication and computing infrastructure, laying the foundation for realizing the optical-layer intelligence. This entails a new operational paradigm for optical transport networks, hinting at a radical change in network design problems formulation as well as algorithm developments to tap into new opportunities enabled by the seamless optical computing and communication integration. Various remaining challenges spanning from devices, systems, and networks requiring multidisciplinary efforts will be needed to make optical-computing-enabled mode a practical reality.

#### **CRediT authorship contribution statement**

**Dao Thanh Hai:** Writing – original draft, Visualization, Validation, Supervision, Software, Resources, Project administration, Investigation, Formal analysis, Data curation, Conceptualization. **Isaac Woungang:** Writing – review & editing, Supervision, Methodology, Investigation.

#### **Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

#### **Data availability**

Data will be made available on request.

# **References**

- <span id="page-11-0"></span>[1] Connecting the unconnected, 2024, URL <https://ctu.ieee.org/>.
- <span id="page-11-1"></span>[2] Cisco, 2022, URL <https://www.cisco.com/c/en/us/solutions/executive-perspectives/annual-internet-report/index.html>.
- <span id="page-11-2"></span>[3] P.J. Winzer, D.T. Neilson, A.R. Chraplyvy, Fiber-optic transmission and networking: the previous 20 and the next 20 years, Opt. Express 26 (18) (2018) 24190–24239, <http://dx.doi.org/10.1364/OE.26.024190>, URL [http://www.opticsexpress.org/abstract.cfm?URI=oe-26-18-24190.](http://www.opticsexpress.org/abstract.cfm?URI=oe-26-18-24190)
- [4] A. Lord, C. White, A. Iqbal, Future optical networks in a 10 year time frame, in: 2021 Optical Fiber [Communications](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb4) Conference and Exhibition, OFC, [2021,](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb4) pp. 1–3.
- <span id="page-11-3"></span>[5] R. Sabella, P. Iovanna, G. Bottari, F. Cavaliere, Optical transport for industry 4.0, J. Opt. Commun. Netw. 12 (8) (2020) 264–276, [http://dx.doi.org/10.](http://dx.doi.org/10.1364/JOCN.390701) [1364/JOCN.390701](http://dx.doi.org/10.1364/JOCN.390701), URL <http://jocn.osa.org/abstract.cfm?URI=jocn-12-8-264>.
- <span id="page-11-4"></span>[6] A. Lord, C. White, A. Iqbal, Future optical networks in a 10 year time frame, in: 2021 Optical Fiber [Communications](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb6) Conference and Exhibition, OFC, [2021,](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb6) pp. 1–3.
- <span id="page-11-5"></span>[7] P.J. Winzer, Capacity scaling through spatial parallelism: From subsea cables to short-reach optical links, in: 2021 Optical Fiber [Communications](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb7) Conference and [Exhibition,](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb7) OFC, 2021, 1–1.
- <span id="page-11-6"></span>[8] D. Hai, M. Morvan, P. Gravey, On the routing and spectrum assignment with multiple objectives, in: Advanced Photonics for Communications, Optical Society of America, 2014, p. JT3A.12, URL [http://www.osapublishing.org/abstract.cfm?URI=PS-2014-JT3A.12.](http://www.osapublishing.org/abstract.cfm?URI=PS-2014-JT3A.12)
- [9] P. Gravey, D. Hai, M. Morvan, On the advantages of CO-OFDM transponder in network-side protection, in: Advanced Photonics for Communications, Optical Society of America, 2014, p. PW1B.3, [http://dx.doi.org/10.1364/PS.2014.PW1B.3,](http://dx.doi.org/10.1364/PS.2014.PW1B.3) URL <http://www.osapublishing.org/abstract.cfm?URI=PS-2014-PW1B.3>.
- [10] H. Dao Thanh, M. Morvan, P. Gravey, On the usage of flexible transponder in survivable transparent flex-grid optical network, in: 2014 9th International Symposium on Communication Systems, Networks Digital Sign, CSNDSP, 2014, pp. 1123–1127, <http://dx.doi.org/10.1109/CSNDSP.2014.6923998>.
- [11] H.D. Thanh, M. Morvan, P. Gravey, F. Cugini, I. Cerutti, On the spectrum-efficiency of transparent optical transport network design with variable-rate forward error correction codes, in: 16th International Conference on Advanced Communication Technology, 2014, pp. 1173–1177, [http://dx.doi.org/10.](http://dx.doi.org/10.1109/ICACT.2014.6779143) [1109/ICACT.2014.6779143.](http://dx.doi.org/10.1109/ICACT.2014.6779143)
- [12] D.T. Hai, On the spectrum-efficiency of qos-aware protection in elastic optical networks, Optik 202 (2020) 163563, [http://dx.doi.org/10.1016/j.ijleo.2019.](http://dx.doi.org/10.1016/j.ijleo.2019.163563) [163563.](http://dx.doi.org/10.1016/j.ijleo.2019.163563)
- [13] D.T. Hai, H.T. Minh, L.H. Chau, Qos-aware protection in elastic optical networks with distance-adaptive and reconfigurable modulation formats, Opt. Fiber Technol., Mater. Devices Syst. 61 (2021) 102364, [http://dx.doi.org/10.1016/j.yofte.2020.102364.](http://dx.doi.org/10.1016/j.yofte.2020.102364)
- [14] D.T. Hai, W.E. Kassa, F. Zhou, On three shades of partial protection in elastic optical networks, Opt. Fiber Technol., Mater. Devices Syst. 80 (2023) 103394, <http://dx.doi.org/10.1016/j.yofte.2023.103394>, URL <https://www.sciencedirect.com/science/article/pii/S1068520023001748>.
- [15] D.T. Hai, On achilles heel of some optical network designs and performance comparisons, Opt. Quantum Electron. 54 (69) (2022) [http://dx.doi.org/10.](http://dx.doi.org/10.1007/s11082-021-03279-y) [1007/s11082-021-03279-y.](http://dx.doi.org/10.1007/s11082-021-03279-y)
- [16] D.T. Hai, A novel integer linear programming formulation for designing transparent WDM optical core networks, in: 2019 International Conference on Advanced Technologies for Communications, ATC, 2019, pp. 273–277, [http://dx.doi.org/10.1109/ATC.2019.8924515.](http://dx.doi.org/10.1109/ATC.2019.8924515)

<span id="page-12-0"></span>[17] D.M. Nguyen, L.A. Ngoc, P.T.V. Huong, N.H. Son, D.T. Hai, An efficient column generation approach for solving the routing and spectrum assignment problem in elastic optical networks, in: 2019 6th NAFOSTED Conference on Information and Computer Science, NICS, 2019, pp. 130–135, [http:](http://dx.doi.org/10.1109/NICS48868.2019.9023831) [//dx.doi.org/10.1109/NICS48868.2019.9023831.](http://dx.doi.org/10.1109/NICS48868.2019.9023831)

- <span id="page-12-1"></span>[18] P.J. Winzer, K. Nakajima, C. Antonelli, Scaling optical fiber capacities [scanning the issue], Proc. IEEE 110 (11) (2022) 1615–1618, [http://dx.doi.org/10.](http://dx.doi.org/10.1109/JPROC.2022.3212229) [1109/JPROC.2022.3212229](http://dx.doi.org/10.1109/JPROC.2022.3212229).
- [19] P.J. Winzer, The future of communications is massively parallel, J. Opt. Commun. Netw. 15 (10) (2023) 783–787, <http://dx.doi.org/10.1364/JOCN.496992>, URL <https://opg.optica.org/jocn/abstract.cfm?URI=jocn-15-10-783>.
- [20] M. Shtaif, C. Antonelli, A. Mecozzi, V.X. Chen, The information capacity of the fiber-optic channel: Bounds and prospects, 2024, [http://](http://dx.doi.org/10.1364/opticaopen.24864648.v2) [dx.doi.org/10.1364/opticaopen.24864648.v2,](http://dx.doi.org/10.1364/opticaopen.24864648.v2) URL [https://preprints.opticaopen.org/articles/preprint/The\\_Information\\_Capacity\\_of\\_the\\_Fiber-Optic\\_Channel\\_](https://preprints.opticaopen.org/articles/preprint/The_Information_Capacity_of_the_Fiber-Optic_Channel_Bounds_and_prospects/24864648) [Bounds\\_and\\_prospects/24864648.](https://preprints.opticaopen.org/articles/preprint/The_Information_Capacity_of_the_Fiber-Optic_Channel_Bounds_and_prospects/24864648)
- <span id="page-12-2"></span>[21] N. Sambo, P. Martelli, P. Parolari, A. Gatto, F. Cugini, P. Castoldi, P. Boffi, Mode group division multiplexing: transmission, node architecture, and provisioning, in: Photonics in Switching and Computing 2021, Optical Society of America, 2021, p. W1A.2, URL [http://www.osapublishing.org/abstract.](http://www.osapublishing.org/abstract.cfm?URI=PSC-2021-W1A.2) [cfm?URI=PSC-2021-W1A.2](http://www.osapublishing.org/abstract.cfm?URI=PSC-2021-W1A.2).
- <span id="page-12-3"></span>[22] NICT, Demonstration of world record: 319 tb/s transmission over 3,001 km with 4-core optical fiber, 2021, URL [https://www.nict.go.jp/en/press/2021/](https://www.nict.go.jp/en/press/2021/07/12-1.html) [07/12-1.html.](https://www.nict.go.jp/en/press/2021/07/12-1.html)
- <span id="page-12-4"></span>[23] R. Kalkunte, R.K. Jana, S. Ferdousi, A. Srivastava, A. Mitra, M. Tornatore, A. Lord, B. Mukherjee, GSNR-aware resource re-provisioning for C to C+L-bands upgrade in optical backbone networks, Photonic Netw. Commun. (2024) [http://dx.doi.org/10.1007/s11107-024-01023-6.](http://dx.doi.org/10.1007/s11107-024-01023-6)
- [24] J. Renaudier, A. Napoli, M. Ionescu, C. Calò, G. Fiol, V. Mikhailov, W. Forysiak, N. Fontaine, F. Poletti, P. Poggiolini, Devices and fibers for ultrawideband optical communications, Proc. IEEE 110 (11) (2022) 1742–1759, <http://dx.doi.org/10.1109/JPROC.2022.3203215>.
- <span id="page-12-5"></span>[25] W. Klaus, P.J. Winzer, K. Nakajima, The role of parallelism in the evolution of optical fiber communication systems, Proc. IEEE 110 (11) (2022) 1619–1654, <http://dx.doi.org/10.1109/JPROC.2022.3207920>.
- <span id="page-12-6"></span>[26] M. van den Hout, Ultra-wideband and Space-division Multiplexed Optical Transmission Systems (Ph.D. thesis), Electrical Engineering, 2024, [http:](http://dx.doi.org/10.6100/jnxx-6t19) [//dx.doi.org/10.6100/jnxx-6t19,](http://dx.doi.org/10.6100/jnxx-6t19) Proefschrift.
- <span id="page-12-7"></span>[27] A. Saleh, J.M. Simmons, Technology and architecture to enable the explosive growth of the internet, Commun. Mag., IEEE 49 (1) (2011) 126–132, [http://dx.doi.org/10.1109/MCOM.2011.5681026.](http://dx.doi.org/10.1109/MCOM.2011.5681026)
- [28] J.M. Simmons, Optical Network Design and Planning, Second ed., Springer Publishing Company, [Incorporated,](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb28) 2014.
- [29] H. Dao Thanh, Contribution to Flexible Optical Network Design: Spectrum Assignment and Protection (Ph.D. thesis), Télécom Bretagne ; Université de Bretagne Occidentale, 2014, URL <https://hal.archives-ouvertes.fr/tel-01206788>.
- [30] D.T. Hai, K.M. Hoang, An efficient genetic algorithm approach for solving routing and spectrum assignment problem, in: 2017 International Conference on Recent Advances in Signal Processing, Telecommunications Computing, SigTelCom, 2017, pp. 187–192, [http://dx.doi.org/10.1109/SIGTELCOM.2017.](http://dx.doi.org/10.1109/SIGTELCOM.2017.7849820) [7849820](http://dx.doi.org/10.1109/SIGTELCOM.2017.7849820).
- [31] D.T. Hai, K.M. Hoang, On the efficient use of multi-line rate transponder for shared protection in WDM network, in: 2017 International Conference on Recent Advances in Signal Processing, Telecommunications Computing, SigTelCom, 2017, pp. 181–186, [http://dx.doi.org/10.1109/SIGTELCOM.2017.7849819.](http://dx.doi.org/10.1109/SIGTELCOM.2017.7849819)
- [32] D.T. Hai, A novel adaptive operation of multi-line rate transponder for dedicated protection in WDM network, in: 2017 Seventh International Conference on Information Science and Technology, ICIST, 2017, pp. 69–74, <http://dx.doi.org/10.1109/ICIST.2017.7926494>.
- [33] D.T. Hai, Multi-objective genetic algorithm for solving routing and spectrum assignment problem, in: 2017 Seventh International Conference on Information Science and Technology, ICIST, 2017, pp. 177–180, [http://dx.doi.org/10.1109/ICIST.2017.7926753.](http://dx.doi.org/10.1109/ICIST.2017.7926753)
- [34] D.T. Hai, M. Morvan, P. Gravey, Combining heuristic and exact approaches for solving the routing and spectrum assignment problem, IET Optoelectron. 12 (2) (2018) 65–72, [http://dx.doi.org/10.1049/iet-opt.2017.0013.](http://dx.doi.org/10.1049/iet-opt.2017.0013)
- <span id="page-12-8"></span>[35] H. Dao, M. Morvan, P. Gravey, An efficient network-side path protection scheme in OFDM-based elastic optical networks, Int. J. Commun. Syst. 31 (1) e3410, [http://dx.doi.org/10.1002/dac.3410,](http://dx.doi.org/10.1002/dac.3410) e3410 dac.3410, [arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1002/dac.3410](http://arxiv.org/abs/https://onlinelibrary.wiley.com/doi/pdf/10.1002/dac.3410), URL [https://onlinelibrary.](https://onlinelibrary.wiley.com/doi/abs/10.1002/dac.3410) [wiley.com/doi/abs/10.1002/dac.3410](https://onlinelibrary.wiley.com/doi/abs/10.1002/dac.3410).
- <span id="page-12-9"></span>[36] A. Saleh, J.M. Simmons, All-optical networking: Evolution, benefits, challenges, and future vision, Proc. IEEE 100 (5) (2012) 1105–1117, [http://dx.doi.](http://dx.doi.org/10.1109/JPROC.2011.2182589) [org/10.1109/JPROC.2011.2182589](http://dx.doi.org/10.1109/JPROC.2011.2182589).
- <span id="page-12-10"></span>[37] B. Collings, M. Filer, Optical node architectures, in: B. Mukherjee, I. Tomkos, M. Tornatore, P. Winzer, Y. Zhao (Eds.), Springer Handbook of Optical Networks, Springer International Publishing, Cham, 2020, pp. 259–286, [http://dx.doi.org/10.1007/978-3-030-16250-4\\_8](http://dx.doi.org/10.1007/978-3-030-16250-4_8).
- <span id="page-12-11"></span>[38] D.T. Hai, On routing, wavelength, network coding assignment, and protection configuration problem in optical-processing-enabled networks, IEEE Trans. Netw. Serv. Manag. 20 (3) (2023) 2504–2514, [http://dx.doi.org/10.1109/TNSM.2023.3283880.](http://dx.doi.org/10.1109/TNSM.2023.3283880)
- <span id="page-12-12"></span>[39] D.T. Hai, Optical networking in future-land: from optical-bypass-enabled to optical-processing-enabled paradigm, Opt. Quantum Electron. 55 (864) (2023) [http://dx.doi.org/10.1007/s11082-023-05123-x.](http://dx.doi.org/10.1007/s11082-023-05123-x)
- [40] D.T. Hai, Network coding in photonicland: Three commandments for future-proof optical core networks, in: 2021 IEEE Microwave Theory and Techniques in Wireless Communications, MTTW, 2021, pp. 165–170, <http://dx.doi.org/10.1109/MTTW53539.2021.9607182>.
- [41] D.T. Hai, Quo vadis, optical network architecture? Towards an optical-processing-enabled paradigm, in: 2022 Workshop on Microwave Theory and Techniques in Wireless Communications, MTTW, 2022, pp. 193–198, <http://dx.doi.org/10.1109/MTTW56973.2022.9942542>.
- [42] D.T. Hai, Photonic network coding and partial protection in optical-processing-enabled network: two for a tango, Opt. Quantum Electron. 54 (282) (2022) <http://dx.doi.org/10.1007/s11082-022-03628-5>.
- <span id="page-12-13"></span>[43] D.T. Hai, If optical-processing-enabled networks come, in: 2022 Workshop on Recent Advances in Photonics, WRAP, 2022, pp. 1–2, [http://dx.doi.org/10.](http://dx.doi.org/10.1109/WRAP54064.2022.9758386) [1109/WRAP54064.2022.9758386.](http://dx.doi.org/10.1109/WRAP54064.2022.9758386)
- <span id="page-12-14"></span>[44] D.T. Hai, L.H. Chau, N.T. Hung, A priority-based multiobjective design for routing, spectrum, and network coding assignment problem in network-coding-enabled elastic optical networks, IEEE Syst. J. 14 (2) (2020) 2358–2369, [http://dx.doi.org/10.1109/JSYST.2019.2938590.](http://dx.doi.org/10.1109/JSYST.2019.2938590)
- [45] T.H. Dao, On optimal designs of transparent WDM networks with 1+1 protection leveraged by all-optical XOR network coding schemes, Opt. Fiber Technol., Mater. Devices Syst. 40 (2018) 93–100, [http://dx.doi.org/10.1016/j.yofte.2017.11.009.](http://dx.doi.org/10.1016/j.yofte.2017.11.009)
- <span id="page-12-15"></span>[46] D.T. Hai, A bi-objective integer linear programming model for the routing and network coding assignment problem in WDM optical networks with dedicated protection, Comput. Commun. 133 (2019) 51–58, <http://dx.doi.org/10.1016/j.comcom.2018.08.006>.
- [47] D.T. Hai, On routing, spectrum and network coding assignment problem for transparent flex-grid optical networks with dedicated protection, Comput. Commun. (2019) [http://dx.doi.org/10.1016/j.comcom.2019.08.005.](http://dx.doi.org/10.1016/j.comcom.2019.08.005)
- <span id="page-12-16"></span>[48] D.T. Hai, Leveraging the survivable all-optical WDM network design with network coding assignment, IEEE Commun. Lett. 21 (10) (2017) 2190–2193, <http://dx.doi.org/10.1109/LCOMM.2017.2720661>.
- [49] D.T. Hai, An optimal design framework for 1+1 routing and network coding assignment problem in WDM optical networks, IEEE Access 5 (2017) 22291–22298, <http://dx.doi.org/10.1109/ACCESS.2017.2761809>.
- [50] D.T. Hai, Re-designing dedicated protection in transparent WDM optical networks with XOR network coding, in: 2018 Advances in Wireless and Optical Communications, RTUWO, 2018, pp. 118–123, [http://dx.doi.org/10.1109/RTUWO.2018.8587873.](http://dx.doi.org/10.1109/RTUWO.2018.8587873)
- [51] D.T. Hai, On solving the 1 + 1 routing, wavelength and network coding assignment problem with a bi-objective integer linear programming model, Telecommun. Syst. 71 (2) (2019) 155–165, <http://dx.doi.org/10.1007/s11235-018-0474-9>.

<span id="page-13-0"></span>[52] D.T. Hai, Network coding for improving throughput in WDM optical networks with dedicated protection, Opt. Quantum Electron. 51 (387) (2019) [http://dx.doi.org/10.1007/s11082-019-2104-5.](http://dx.doi.org/10.1007/s11082-019-2104-5)

- <span id="page-13-1"></span>[53] D.T. Hai, I. Woungang, On network design and planning 2.0 for [optical-computing-enabled](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb53) networks, in: L. Barolli (Ed.), Advanced Information Networking and [Applications,](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb53) Springer Nature, Switzerland, Cham, 2024, pp. 91–102.
- <span id="page-13-2"></span>[54] D.T. Hai, What comes after optical-bypass network? A study on optical-computing-enabled network, Opt. Fiber Technol., Mater. Devices Syst. 84 (2024) 103730, <http://dx.doi.org/10.1016/j.yofte.2024.103730>, URL <https://www.sciencedirect.com/science/article/pii/S1068520024000750>.
- <span id="page-13-17"></span>[55] D.T. Hai, M. Nguyen, I. Woungang, Optical-computing-enabled network: A new dawn for optical-layer intelligence? in: Proceedings of the 8th Asia-Pacific Workshop on Networking, APNet '24, Association for Computing Machinery, New York, NY, USA, 2024, pp. 215–216, [http://dx.doi.org/10.1145/3663408.](http://dx.doi.org/10.1145/3663408.3665822) [3665822](http://dx.doi.org/10.1145/3663408.3665822).
- <span id="page-13-18"></span>[56] D.T. Hai, Optical-computing-enabled network: An avant-garde architecture to sustain traffic growth, Results Opt. 13 (2023) 100504, [http://dx.doi.org/10.](http://dx.doi.org/10.1016/j.rio.2023.100504) [1016/j.rio.2023.100504](http://dx.doi.org/10.1016/j.rio.2023.100504), URL [https://www.sciencedirect.com/science/article/pii/S2666950123001566.](https://www.sciencedirect.com/science/article/pii/S2666950123001566)
- [57] X. Chen, L. Yang, C. Li, Y. Li, Carbon emission-aware virtual optical network embedding over elastic optical networks, J. Lightwave Technol. 42 (20) (2024) 7056–7069, <http://dx.doi.org/10.1109/JLT.2024.3420929>.
- <span id="page-13-3"></span>[58] D. Pile, Optical computing and artificial intelligence, Nature Photonics 18 (2024) [http://dx.doi.org/10.1038/s41566-024-01582-0.](http://dx.doi.org/10.1038/s41566-024-01582-0)
- <span id="page-13-4"></span>[59] N. Margalit, C. Xiang, S.M. Bowers, A. Bjorlin, R. Blum, J.E. Bowers, Perspective on the future of silicon photonics and electronics, Appl. Phys. Lett. 118 (22) (2021) 220501, [http://dx.doi.org/10.1063/5.0050117,](http://dx.doi.org/10.1063/5.0050117) [arXiv:https://pubs.aip.org/aip/apl/article-pdf/doi/10.1063/5.0050117/20022318/220501\\_1\\_5.](http://arxiv.org/abs/https://pubs.aip.org/aip/apl/article-pdf/doi/10.1063/5.0050117/20022318/220501_1_5.0050117.pdf) [0050117.pdf](http://arxiv.org/abs/https://pubs.aip.org/aip/apl/article-pdf/doi/10.1063/5.0050117/20022318/220501_1_5.0050117.pdf).
- <span id="page-13-5"></span>[60] P.L. McMahon, The physics of optical computing, Nat. Rev. Phys. 5 (2023) [http://dx.doi.org/10.1038/s42254-023-00645-5.](http://dx.doi.org/10.1038/s42254-023-00645-5)
- [61] W. Bogaerts, D. Pérez, J. Capmany, D.A.B. Miller, J. Poon, D. Englund, F. Morichetti, A. Melloni, Programmable photonic circuits, Nature 586 (2020) [http://dx.doi.org/10.1038/s41586-020-2764-0.](http://dx.doi.org/10.1038/s41586-020-2764-0)
- [62] S. SeyedinNavadeh, M. Milanizadeh, F. Zanetto, G. Ferrari, M. Sampietro, M. Sorel, D.A.B. Miller, A. Melloni, F. Morichetti, Determining the optimal communication channels of arbitrary optical systems using integrated photonic processors, Nature Photonics 18 (2024) [http://dx.doi.org/10.1038/s41566-](http://dx.doi.org/10.1038/s41566-023-01330-w) [023-01330-w.](http://dx.doi.org/10.1038/s41566-023-01330-w)
- <span id="page-13-6"></span>[63] S. Shekhar, W. Bogaerts, L. Chrostowski, J.E. Bowers, M. Hochberg, R. Soref, B.J. Shastri, Roadmapping the next generation of silicon photonics, Nature Commun. 15 (2024) [http://dx.doi.org/10.1038/s41467-024-44750-0.](http://dx.doi.org/10.1038/s41467-024-44750-0)
- <span id="page-13-7"></span>[64] Z. Zhong, M. Yang, J. Lang, C. Williams, L. Kronman, A. Sludds, H. Esfahanizadeh, D. Englund, M. Ghobadi, Lightning: A reconfigurable photonic-electronic smartnic for fast and energy-efficient inference, in: Proceedings of the ACM SIGCOMM 2023 Conference, in: ACM SIGCOMM '23, Association for Computing Machinery, New York, NY, USA, 2023, pp. 452–472, [http://dx.doi.org/10.1145/3603269.3604821.](http://dx.doi.org/10.1145/3603269.3604821)
- [65] M. Yang, Z. Zhong, M. Ghobadi, On-fiber photonic computing, in: Proceedings of the 22nd ACM Workshop on Hot Topics in Networks, HotNets '23, Association for Computing Machinery, New York, NY, USA, 2023, pp. 263–271, [http://dx.doi.org/10.1145/3626111.3628177.](http://dx.doi.org/10.1145/3626111.3628177)
- [66] P. Minzioni, C. Lacava, T. Tanabe, J. Dong, X. Hu, G. Csaba, W. Porod, G. Singh, A.E. Willner, A. Almaiman, V. Torres-Company, J. Schröder, A.C. Peacock, M.J. Strain, F. Parmigiani, G. Contestabile, D. Marpaung, Z. Liu, J.E. Bowers, L. Chang, S. Fabbri, M.R. Vázquez, V. Bharadwaj, S.M. Eaton, P. Lodahl, X. Zhang, B.J. Eggleton, W.J. Munro, K. Nemoto, O. Morin, J. Laurat, J. Nunn, Roadmap on all-optical processing, J. Opt. 21 (6) (2019) 063001, [http://dx.doi.org/10.1088/2040-8986/ab0e66.](http://dx.doi.org/10.1088/2040-8986/ab0e66)
- <span id="page-13-8"></span>[67] L.-K. Chen, M. Li, S.C. Liew, Breakthroughs in photonics 2014: Optical physical-layer network coding, recent developments, and challenges, IEEE Photonics J. 7 (3) (2015) 1–6, <http://dx.doi.org/10.1109/JPHOT.2015.2418264>.
- <span id="page-13-9"></span>[68] A. Misra, S. Preußler, K. Singh, J. Meier, T. Schneider, Optical channel aggregation based on modulation format conversion by coherent spectral superposition with electro-optic modulators, APL Photonics 8 (8) (2023) 086112, <http://dx.doi.org/10.1063/5.0150989>, [arXiv:https://pubs.aip.org/aip/](http://arxiv.org/abs/https://pubs.aip.org/aip/app/article-pdf/doi/10.1063/5.0150989/18095171/086112_1_5.0150989.pdf) [app/article-pdf/doi/10.1063/5.0150989/18095171/086112\\_1\\_5.0150989.pdf](http://arxiv.org/abs/https://pubs.aip.org/aip/app/article-pdf/doi/10.1063/5.0150989/18095171/086112_1_5.0150989.pdf).
- <span id="page-13-13"></span>[69] A. Fallahpour, F. Alishahi, K. Zou, Y. Cao, A. Almaiman, A. Kordts, M. Karpov, M.H.P. Pfeiffer, K. Manukyan, H. Zhou, P. Liao, C. Liu, M. Tur, T.J. Kippenberg, A.E. Willner, Demonstration of tunable optical aggregation of QPSK to 16-QAM over optically generated nyquist pulse trains using nonlinear wave mixing and a Kerr frequency comb, J. Lightwave Technol. 38 (2) (2020) 359–365, <http://dx.doi.org/10.1109/JLT.2019.2959803>.
- <span id="page-13-10"></span>[70] A.E. Willner, A. Fallahpour, K. Zou, F. Alishahi, H. Zhou, Optical signal processing aided by optical frequency combs, IEEE J. Sel. Top. Quantum Electron. 27 (2) (2021) 1–16, [http://dx.doi.org/10.1109/JSTQE.2020.3032554.](http://dx.doi.org/10.1109/JSTQE.2020.3032554)
- <span id="page-13-11"></span>[71] D. Welch, A. Napoli, J. Bäck, W. Sande, J. Pedro, F. Masoud, C. Fludger, T. Duthel, H. Sun, S.J. Hand, T.-K. Chiang, A. Chase, A. Mathur, T.A. Eriksson, M. Plantare, M. Olson, S. Voll, K.-T. Wu, Point-to-multipoint optical networks using coherent digital subcarriers, J. Lightwave Technol. 39 (16) (2021) 5232–5247, [http://dx.doi.org/10.1109/JLT.2021.3097163.](http://dx.doi.org/10.1109/JLT.2021.3097163)
- [72] J. Bäck, P. Wright, J. Ambrose, A. Chase, M. Jary, F. Masoud, N. Sugden, G. Wardrop, A. Napoli, J. Pedro, M.A. Iqbal, A. Lord, D. Welch, CAPEX savings enabled by point-to-multipoint coherent pluggable optics using digital subcarrier multiplexing in metro aggregation networks, in: 2020 European Conference on Optical Communications, ECOC, 2020, pp. 1–4, <http://dx.doi.org/10.1109/ECOC48923.2020.9333233>.
- [73] D. Welch, A. Napoli, J. Bäck, W. Sande, J. Pedro, F. Masoud, C. Fludger, T. Duthel, H. Sun, S.J. Hand, T.-K. Chiang, A. Chase, A. Mathur, T.A. Eriksson, M. Plantare, M. Olson, S. Voll, K.-T. Wu, Point-to-multipoint optical networks using coherent digital subcarriers, J. Lightwave Technol. 39 (16) (2021) 5232–5247, [http://dx.doi.org/10.1109/JLT.2021.3097163.](http://dx.doi.org/10.1109/JLT.2021.3097163)
- <span id="page-13-12"></span>[74] Y. Zhang, Q. Lv, R. Li, X. Tian, Z. Zhu, Planning of survivable wavelength-switched optical networks based on P2MP transceivers, IEEE Trans. Netw. Serv. Manag. (2023) [http://dx.doi.org/10.1109/TNSM.2023.3287302,](http://dx.doi.org/10.1109/TNSM.2023.3287302) 1–1.
- <span id="page-13-14"></span>[75] Q. Yang, X. Wang, Q. Zhang, X. Xin, R. Gao, Y. Tao, Q. Tian, F. Tian, Y. Wang, W. Zhang, H. Chang, D. Chen, J. Qian, All-optical [aggregation](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb75) scheme based on joint modulation, in: 2020 Asia [Communications](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb75) and Photonics Conference (ACP) and International Conference on Information Photonics and Optical [Communications,](http://refhub.elsevier.com/S2542-6605(24)00386-X/sb75) IPOC, 2020, pp. 1–3.
- <span id="page-13-15"></span>[76] H. Liu, H. Wang, Z. Xing, Y. Ji, Simultaneous all-optical channel aggregation and de-aggregation based on nonlinear effects for OOK and MPSK formats in elastic optical networking, Opt. Express 27 (21) (2019) 30158–30171, [http://dx.doi.org/10.1364/OE.27.030158,](http://dx.doi.org/10.1364/OE.27.030158) URL [http://www.osapublishing.org/](http://www.osapublishing.org/oe/abstract.cfm?URI=oe-27-21-30158) [oe/abstract.cfm?URI=oe-27-21-30158](http://www.osapublishing.org/oe/abstract.cfm?URI=oe-27-21-30158).
- <span id="page-13-16"></span>[77] A. Kotb, K.E. Zoiros, C. Guo, 1 Tb/s all-optical XOR and AND gates using quantum-dot semiconductor optical amplifier-based turbo-switched Mach–Zehnder interferometer, J. Comput. Electron. (2019) [http://dx.doi.org/10.1007/s10825-019-01329-z.](http://dx.doi.org/10.1007/s10825-019-01329-z)
- <span id="page-13-19"></span>[78] C. Porzi, et al., All-optical XOR gate by means of a single semiconductor optical amplifier without assist probe light, in: LEOS '09. IEEE, 2009, pp. 617–618, [http://dx.doi.org/10.1109/LEOS.2009.5343425.](http://dx.doi.org/10.1109/LEOS.2009.5343425)
- <span id="page-13-20"></span>[79] H. Overby, et al., Cost comparison of 1+1 path protection schemes: A case for coding, in: ICC 2012, IEEE, 2012, pp. 3067–3072, [http://dx.doi.org/10.](http://dx.doi.org/10.1109/ICC.2012.6363928) [1109/ICC.2012.6363928.](http://dx.doi.org/10.1109/ICC.2012.6363928)
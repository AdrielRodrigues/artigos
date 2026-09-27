---
title: "Forthcoming optical x-haul infrastructure supporting 6G mobile network requirements"
tema_principal: projeto_universal
temas_relacionados: []
ano: 2025
autores: []
veiculo: null
pdf: ../pdf/forthcoming_optical_x-haul_infrastructure_supporting_6g_mobile_network_requirements.pdf
---

# Forthcoming optical x-haul infrastructure supporting 6G mobile network requirements

**C. Papapavlou,<sup>1</sup> K. Moschopoulos,<sup>1</sup> C. Christofidis,<sup>1</sup> D. Uzunidis,<sup>1</sup> K. Paximadis,<sup>1</sup> D. M. Marom,<sup>2</sup> R. Muñoz,<sup>3</sup> M. Nazarathy,<sup>4</sup> AND I. Tomkos1, \***

Received 30 June 2025; revised 14 August 2025; accepted 19 August 2025; published 22 September 2025

**The sixth generation of communication networks necessitates a series of significant technological innovations to accommodate ultra-high rates, ultra-low latency, high energy efficiency, and software-defined programmability for supporting the emerging use cases and the exponential growth in traffic demands. Ultra-wideband (UWB) and spatial division multiplexing technologies have emerged as key enablers in meeting these challenges, offering both scalable network capacity and improved energy efficiency. In this paper, we propose an advanced optical transport architecture designed to fulfill the rigorous performance criteria of next-generation optical networks covering all critical network segments. At the core of this infrastructure—the backhaul segment—we introduce a three-layered UWB/SDM-based multi-granular optical node architecture that utilizes photonic integrated circuit (PIC)-based waveband selective switches, enabling scalable network performance and delivering over 10 Pb/s of flexible optical switching capacity while maintaining a high optical signal-to-noise and interference ratio. At the network edge—the fronthaul segment—we introduce a spatially diverse point-to-multipoint PIC-based optical subcarrier interconnectivity architecture that incorporates a low-loss module—referred to as the interlacer which interconnects cascaded half-band Nyquist-shaped interleaver filters in order to flexibly perform routing at the subcarrier group level. Across all network segments, we consider innovative, energy-efficient optical digitalto-analog converter-based transceivers capable of achieving transmission rates in the order of terabits per second per channel, while ensuring a small footprint and low power consumption. These transceivers can be flexibly reconfigured to either direct detect or coherent operation, serving the specific needs of the different network segments. Extensive numerical simulations are conducted, with parameters mostly derived from experimental data, to assess the feasibility, scalability, and cascadability of the subsystems that are incorporated to optimize the overall performance of the proposed architecture. Finally, the overall design ensures full compatibility with a service management and orchestration framework, enabling software-defined programmability across all interconnected segments.** © 2025 Optica Publishing Group under the terms of the Optica Open Access Publishing Agreement

https://doi.org/10.1364/JOCN.571798

# 1. INTRODUCTION

The International Telecommunication Union (ITU-R) has recently published a recommendation [1] that defines the overall objectives, capabilities, and expected use-case categories of "International Mobile Telecommunications for 2030" (IMT-2030). Addressing the demands of next-generation networks requires fundamental and cross-layer technological innovations across all transport segments. The allocation of available wireless access communication resources—such as spectrum, timeslots, multiple-input multiple-output (MIMO) layers, antenna ports, and beams—along with computing resources, including central processing units (CPUs), graphics processing units (GPUs), and memory, is intelligently and dynamically orchestrated to meet the specific performance demands of various use-case categories. Wireless signals, once they are down-converted by the antenna system, undergo a sequence of radio frequency signal processing operations to become functionally disaggregated across distinct radio access network (RAN) components: the radio unit (RU), the distributed unit (DU), and the central unit (CU). The transport links connecting these elements are categorized as follows: the interface between the RU and DU is referred to as the fronthaul (FH), while the link between the DU and CU is known as the midhaul (MH). Digitized radio (DR) signals are subsequently forwarded from the CU toward the core network (CN) via the

<sup>1</sup>Department of Electrical and Computer Engineering, University of Patras, Rio 26504, Greece

<sup>2</sup>Applied Physics Department, Hebrew University of Jerusalem, Jerusalem, Israel

<sup>3</sup>Centre Tecnologic de Telecomunicacions de Catalunya, Barcelona, Spain

<sup>4</sup>Faculty of Electrical and Computer Engineering, Technion, Israel Institute of Technology, Haifa, Israel

<sup>\*</sup>itom@ece.upatras.gr

![](_page_1_Figure_3.jpeg)

Fig. 1. The packet-optical transport network serves the data traffic coming from the wireless access side. The x-haul network consists of the front/mid/backhaul continuum, facilitating many innovations in terms of transceivers and node architectures with different capabilities per network segment. An SMO framework enables software-defined programmability across all interconnected segments through proper interfaces and controllers.

backhaul (BH), as shown in Fig. 1. Collectively, these transport segments—FH, MH, and BH—are denoted as the x-haul network, which underpins end-to-end connectivity from the RAN to the broader Internet. Extensive scientific efforts—driven by industry consortia and collaborative research initiatives—have focused on advancing novel solutions across all segments of next-generation transport networks [2–6].

The third-generation partnership project (3GPP) proposed functional-split (FS) architectures for the RAN in cellular networks, consisting of eight FS options to be adapted by the operators to particular network characteristics, traffic features, and service requirements. Each split presents unique demands on the transport network in terms of capacity, latency, and synchronization [7]. Regarding latency, the switching speed of the ONs plays a crucial role. At the fronthaul, ONs require fast switching to support the low-latency requirements, even though they typically handle lower capacities.

On the other hand, the ONs located in the backhaul must be able to support large throughputs, however, with less

#### Abbreviations

| CS    | Crossbar switch                  |
|-------|----------------------------------|
| DSCM  | Digital subcarrier multiplexing  |
| FFS   | Full fiber switching             |
| FIR   | Finite impulse response          |
| MG-ON | Multi granular optical node      |
| MZI   | Mach–Zehnder interferometer      |
| ODAC  | Optical digital analog converter |
| OXC   | Optical cross connect            |
| PIC   | Photonic integrated circuit      |
| RAN   | Radio access network             |
| SDM   | Space division multiplexing      |
| UWB   | Ultra-wide band                  |
| WBSS  | Waveband selective switch        |
| WSS   | Wavelength selective switch      |
|       |                                  |

demanding switching speed requirements. These FS architectures define degrees of decentralization of the traditional baseband unit (BBU) processing functions. CUs and DUs can be grouped together in virtualization pools/clusters, and the associated processing can be implemented in virtual machines/servers. As processing functions are centralized, further performance benefits are expected, such as reduced operational costs and effective interference mitigation, albeit at the cost of increased capacity and latency requirements in the fronthaul/midhaul network. We have defined two scenarios for the lower and upper ranges of reference values, "6G basic" versus "6G advanced," to estimate the transport capacity requirements, as reported in [7].

Our motivation is to capitalize on the combined advantages of wavelength-division multiplexing (WDM), wavebanddivision multiplexing (WBDM), and space division multiplexing (SDM) by introducing a set of disruptive switching architectures, including fronthaul/midhaul reconfigurable optical add-drop multiplexers (ROADMs) operating at the subcarrier level [6] and backhaul multi-granular optical nodes (MG-ONs). Related studies have also explored the use of photonic integrated circuits (PICs) to advance x-haul architectures in [8,9].

In this work, we are focusing on the optical network layer innovations (Fig. 1, green dotted box) and specifically the following:

- 1. For the fronthaul/midhaul network segment, we introduce a low-loss, PIC-based optical filter that supports dynamic resource allocation with high-speed switching and real-time bandwidth elasticity.
- 2. For the backhaul segment, we propose a novel UWB/ SDM-capable MG-ON framework, incorporating a novel PIC-based WBSS. This switch bridges the gap between current super-channel wavelength selective switches

(WSSs) and the envisioned FSS platforms of future optical networks.

3. Energy-efficient transceivers essentially alleviate the reliance on faster and thus more power-consuming electronics by leveraging parallelized photonic components (e.g., multiple optical modulators finely integrated).

It is worth mentioning that, to comply with the software-defined programmability, the underlying physical infrastructure is managed by an SMO platform, initially introduced by the O-RAN Alliance and further extended in this work to enable cross-domain coordination. The SMO interfaces with domain-specific orchestrators and controllers responsible for IP, optical, and wireless segments. This unified end-to-end platform can support full network automation, flexible FS, and end-to-end network slicing (E2E-NS) [3]. In this work, we are not delving into a detailed analysis of the SMO, but all the hardware innovations are fully compatible with it. The rest of the paper is structured as follows: Section 2 presents the proposed fronthaul/midhaul PIC-based SDPtMP node and backhaul MG-ON architectures, including their design, functionality, and performance, while also evaluating the scalability and cascadability of the MG-ON node under various scenarios. Section 3 presents the optical digital-toanalog converter (oDAC)-based transceivers, highlighting both their superior performance and energy efficiency compared to conventional designs. Section 4 concludes with key findings, discusses limitations, and outlines directions for future research.

# 2. OPTICAL SWITCHING ARCHITECTURES FOR THE X-HAUL

# A. Novel Nyquist-Shaped Node Element for Supporting Flexible Fronthaul Networking

Time division multiplexing and multiple access (TDM/ TDMA) is the current legacy approach for passive optical networks (PONs), limiting the per-site capacity, as it is shared, and introducing access delay incommensurate with 6G specifications and splitting losses that need to be compensated [10]. The PON architecture can utilize an alternative multipleaccess solution based on subcarrier multiplexing and multiple access (SCM/SCMA), whereby digital subcarriers are assigned, as needed, for both upstream and downstream directions between the CO and cell sites. A single DSCM transceiver can feed multiple cell sites, utilizing, based on today's state-ofthe-art capabilities, 16 subcarriers at 4 GHz channel spacing and carrying a 25 Gb/s data rate [11]. Coherent technology using SCMA can provide flexible resource allocation to a large number of access points by dividing subcarriers of the digital subcarrier multiplexing (DSCM) signal [12] into time slots for time-and-frequency division. This compelling solution replaces the stochastic nature of TDMA for SCMA, thereby guaranteeing finite bandwidth and reducing access delay, with capacity scaling being afforded by additional wavelength multipliers. Yet, the existing DSCM PON scheme is not adequately matched to forthcoming 6G specifications in scaling capacity (maximum number of generated subcarriers) and reconfigurability. By essentially overlaying four different spatial feeds, each cell site is allowed to subscribe to any one out of four different PON options, hence to any access CO, supporting flexible FS [3] and avoiding fixed associations between cell sites and the CO.

To this end, we introduce a novel optical distribution element—the circular interlacer—which serves as the key enabler of the spatially diverse point-to-multi-point (SD-PtMP) architecture illustrated in Fig. 2. By supporting multiple parallel optical feeds (four in our case), the SD-PtMP architecture allows all inputs to reside on the same center optical wavelength, but note that the circular subcarrier interlacer functions for any spectrally aligned wavelength channel input, and we foresee multiple wavelength channels being processed all-optically (WDM) and in parallel [12]. The subcarrier interlacer shuffles the subcarriers from its four inputs, resulting in four new DSCM signals, each containing a unique set of subcarriers from the four input sources (Fig. 2). These four outputs are distributed to cell sites by wavelength routing/selection, such that each edge receives subcarriers from each of the four sources on a particular wavelength, forming a unique association between several sources and each cell site. This approach performs nearly lossless filtering and passive routing of the parallel feeds to the distribution fibers.

The circular interlacer is implemented as a two-stage cascaded network of half-band interleaver filters arranged in

![](_page_2_Figure_12.jpeg)

Fig. 2. Fronthaul and midhaul network segments are connected via a node (ROADM) that is based on the circular subcarrier interlacer, which represents a major device innovation. The fabricated interlacer PIC is depicted as an inset.

![](_page_3_Figure_3.jpeg)

Fig. 3. Operation of the circular subcarrier interlacer. The switch has four input ports to which the DSCM transceivers are connected. Four interleavers in a butterfly interconnection then distribute the subcarriers. (The letters are used to help the reader follow the cyclic subcarrier distribution and the switch operation.)

a butterfly pattern (Fig. 3). This configuration enables the circular functionality illustrated by the letter distribution at the four outputs. Two stages of high-selectivity interleavers are required to achieve subcarrier-level interlacing of the input and output ports [12–14]. Operating at a 64 GHz spectral periodicity, the first stage separates complementary 30 GHzwide channels. The second stage, using an identical interleaver design, is frequency-shifted by <sup>1</sup> /<sup>4</sup> of the cycle (16 GHz) relative to the filter's reference frequency, enabling precise subcarrier alignment.

The interlacer design leads to four separated subcarrier groups, each occupying a width of 14 GHz, sufficient for supporting three subcarriers of 4 GHz bandwidth with ±1 GHz alignment tolerance. Feeding all four inputs of the interleaver network with DSCM transceiver signals, even at the same optical carrier, we obtain a circular subcarrier-group interlacer, generating four outputs with each subcarrier group originating from a different input source. Since the 64 GHz spectral periodicity continues indefinitely, additional DSCM on other grid-aligned center wavelengths will be identically processed [14]. We sacrifice a subcarrier at the transition bands; hence, four out of sixteen subcarriers (4/16 subcarriers) are not utilized for data transmission. Hence, the fronthaul feed is spatially widened by a factor of four [7], but only 75% of the subcarriers are utilized [15], leaving a net 3× capacity gain. It is worth noting that the interlacer, functionality-wise, is similar to a cyclic arrayed waveguide grating router (AWGR); however, the interlacer achieves higher bandwidth utilization, has lower loss, requires a smaller footprint, and can be fine-tuned [16].

We are further incorporating the interlacer element into the TEFNET24 network topology [14], presenting the required number of fronthaul SDPtMP elements within the network. We aim to provide initial insights into how network capacity scales with node count and traffic demands, anticipated to reach several terabits per second (Tb/s) in the fronthaul and midhaul segments of 6G networks [7]. Each midhaul node is equipped with prototype transceivers [15], capable of generating up to 16 subcarriers, each operating at approximately 4 GBaud and utilizing dual-polarization 16-QAM modulation. This configuration delivers a net data rate of 25 Gb/s per subcarrier and 75 Gb/s per base station (BS). One interlacer or fronthaul SDPtMP architecture is required for every four transceivers. Each node serves 75 BSs on average

Table 1. Number of Average Fronthaul SDPtMP Scaling in Terms of Capacity in the TEFNET Topology [14]

| #-Ring | Occurrence | N<br>(Ring) | N<br>(Node) | Average Fronthaul<br>ROADMs/Ring |
|--------|------------|-------------|-------------|----------------------------------|
| 1      | 6          | 6           | 33          | 31                               |
| 2      | 26         | 52          | 266         | 24                               |
| 3      | 16         | 48          | 274         | 25                               |
| 4      | 3          | 12          | 83          | 30                               |
| 6      | 2          | 12          | 69          | 24                               |
| Total  | 53         | 130         | 725         |                                  |

[16]. Table 1 summarizes the TEFNET24 metro-regional ring structures [14]. The first four columns show the number of rings per structure, total structures, rings, and nodes, respectively. Fronthaul ROADMs are estimated at one per four transceivers. The data show wide structural variation—from 2-node to 10-node rings—with 2-node rings most common (26 instances) and 4-node rings having the highest transceiver density (130 per ring). These differences in structure directly impact resource demands and play a crucial role in shaping the network's energy optimization strategies.

#### B. MG-ON Architecture and Operation

Emerging architectures and networks are likely to be based on UWB transmission and SDM technologies [17]. Scaling the current WSS technology utilized in ROADM nodes results in high port counts to host UWB and poses significant challenges in terms of cost, volume of packaging, and installation [18]. A proposed high-port count ROADM architecture that combines two types of network elements, space switches, and wavelength-routing switches, presented in [19], demonstrated that the ROADM port count can be cost-effectively expanded while maintaining acceptable routing performance. The ideal optical node should exhibit various characteristics such as cost-effectiveness, multi-granularity, reconfigurability, and the ability to operate across multiple bands (at least the S-, C-, and L-bands). These features are essential for maximizing efficiency and flexibility in terms of network management and performance.

Several proposed architectures [19–21] aim to address these demands by employing hierarchical optical cross connect (OXC) designs across two or three layers optimized for specific data flows. A recently proposed architecture that implements a modular design composed of PIC-based multi-band WSSs was presented in [22]. This design incorporates S/C/L bandseparating Bragg filters and channel-resolving micro-ring resonator filters, along with a Mach–Zehnder interferometer (MZI) switching tree architecture. The scalability and node connectivity aspects of this solution have not been rigorously investigated. Another architecture that aims to address the transition from multi-band to multi-rail core networks and from wavelength switching to band/fiber switching was presented in [23]. This design utilizes fixed band separation filters, but with limited flexibility because of its static configuration. Furthermore, it requests additional hardware for implementation. As UWB transmission is already a reality (mainly focusing on the C- and L-bands), the design and implementation of a WBSS element becomes crucial [22,23]. The existence of WBSSs is important, as they will serve as the intermediate step, the missing piece, between the currently available super-channel switches and future full-fiber switches.

Figure 4 depicts the proposed MG-ON architecture for the backhaul network segment, incorporating the novel flex-WBSS technology.

Previous WBSS implementations of concatenated cyclic AWGR with optical switches lacked the flexibility to adapt to bandwidth requirements and so could not provide the desirable UWB spectral support. To address this problem, our novel MG-ON architecture has been designed to address the technological transition from existing wavelength channels to future full-fiber switches. The MG-ON incorporates PICbased, state-of-the-art flex-WBSSs with a small footprint, low expected insertion losses, rapid switching capabilities (less than 10 ms using piezo actuators on silicon nitride waveguides), and less than 23 dB crosstalk at the output. This design can address the scaling challenges and is fully compatible with the upcoming UWB/SDM technologies. To achieve this, it comprises three layers, each with different capabilities. Layer 1 performs route and select at the fiber/band level, Layer 2 adds/drops traffic at the band level, while Layer 3 provides the routing and adding/dropping at the wavelength level. All layers' operation is explained below.

#### 1. Layer 1: Flex-Band Route and Select

At the top of the hierarchy, ingress and egress fiber ports are connected to flex-WBSS modules, enabling a route-and-select switching topology at the flexibly defined band level. The WBSS partitions the UWB spectrum into bands (up to four) using reconfigurable lattice filters [5], enabling switching at the full-fiber granularity by bypassing the delay stages (all the fiber spectrum/content, C<sup>1</sup> in Fig. 4). The solid black lines from the "West" input to the "East" and "South" output directions indicate available connection paths (C<sup>2</sup> in Fig. 4), with others excluded for simplicity. The East and West links have SDM dimensions equal to three, while the South links are equal to two, respectively. The routing and select capabilities support spatial lane changes (SLCs), providing the relocation of bands from one input spatial lane (or rail) to another in the case of a link failure at the cost of additional WBSS output ports. By switching the whole bandwidth of a band or fiber and thus avoiding unnecessary lower-level traffic switching, this layer implements the synergy of packet and optical layers and the packet offloading technique proposed in [8].

#### 2. Layer 2: Flex-Band Add/Drop

In the middle of the hierarchy, an inter-band OXC provides the interconnectivity between added/dropped flexibly defined bands and shared banks of band transceivers. This interband OXC offers colorless, directionless, and contentionless (C/D/C) access to the band transceivers. Blue lines originating

![](_page_4_Figure_10.jpeg)

Fig. 4. Proposed multi-granular three-layered UWB/SDM-based optical node architecture, providing route and select incorporating flex-WBSS modules at Layer 1, C/D/C band add/drop at Layer 2, and compatibility with legacy wavelength routing and add/drop at Layer 3.

![](_page_5_Figure_3.jpeg)

Fig. 5. (a) The internal structure of the flexible waveband selective switch (flex-WBSS) consists of an adaptive filtering stage combined with a non-blocking spatial crossbar switch (CS) that directs signals to the output ports [25]. (b) Fabricated WBSS/crossbar-switch PICs on a large silicon nitride wafer. (c) The packaged module of one of the WBSS/switch PICs.

from the West ingress WBSS send the selected flex-bands to the inter-band OXC (C<sup>3</sup> in Fig. 4), which assigns each dropped band to an available band receiver (C<sup>4</sup> in Fig. 4). Emerging energy-efficient, full-band transceivers based on integrated comb sources can enable wideband add/drop with simplified hardware [5,24]. Blue lines from the inter-band OXC to the East/South egress WBSS represent additional paths for signals originating from the band transmitters, with reconfiguration performed by the inter-band OXC. The additional blue lines are excluded for simplicity.

# 3. Layer 3: Legacy Wavelengths Access for Routing and Add/Drop

At the lowest level of the hierarchy, compatibility with legacy equipment (e.g., C-band transmission) is maintained. Bands (S/C/L) requiring wavelength access are configured via a conventional WSS that interfaces with an intra-band OXC, providing routing and/or wavelength add/drop to singlechannel transceivers (C<sup>5</sup> in Fig. 4), which are also connected to the intra-band OXC. As wavelength access is expected to be gradually phased out, resources at this layer can be decommissioned over time, and the MG-ON will continue to function over its top two levels.

## C. Waveband Selective Switch

#### 1. WBSS Architecture

As presented in Fig. 5(a), the WBSS comprises an adaptive filtering stage, implemented with cascaded optical finiteimpulse response (FIR) lattice filters [Fig. 5(a) inset], where k1−k<sup>4</sup> denote the coupling coefficients, 1ϕ1−1ϕ<sup>3</sup> represent tunable phase shifters, and 1*L* segments indicate optical path length differences between the two arms of each MZI stage. This configuration enables carving the UWB spectrum into one or up to four flexible and disjoint bands. Subsequently, a (4 × N) crossbar space switch (CS) routes each carved band to a designated output port. The sharpness of the lattice filters is determined by the number of filter taps, with sharper filters necessitating finer resolution and a greater number of taps.

The optical delay is dictated by the filter's large bandwidth support, spanning about 165 nm (∼21 THz total bandwidth). Both the FIR filters and the crossbar switch incorporate phase modulators to set their states, drawing minimal power when implemented with piezo technology. Figure 5(b) shows a fabricated, compact prototype of the WBSS/crossbar-switch PICs on a large silicon nitride wafer. The presented PICs include a crossbar switch and an L-band lattice filter. Figure 5(c) depicts the packaged module of one of the WBSS/switch PICs intended for integration within the proposed MG-ON node.

#### 2. WBSS Modeling

Although the flex-WBSS is designed to operate with negligible intrinsic loss, its overall insertion loss (IL) is influenced by two key components: FIR filters and the CS. FIR filter losses scale with the number of taps at 0.1 dB/tap, while crossbar losses scale with the number of traversed junctions at 0.05 dB/junction. In conventional CS designs, most MZI switches are set to the cross state, with only the active switching path set to the bar state. However, we find that the bar state exhibits superior crosstalk performance, particularly under UWB operation, where directional coupler imperfections become more pronounced. To address this, we adopt an inverted logic configuration [25], where most MZIs are set to bar and intersections are handled using waveguide crossings at each intersection. Despite adding insertion loss, waveguide crossings generally exhibit lower crosstalk compared to imperfect directional couplers, especially across wide spectral ranges. Thus, when waveguide crossings outperform directional couplers in terms of the crosstalk loss trade-off, this approach yields a net performance benefit. The total insertion loss of the WBSS is calculated as the sum of the FIR filter IL and the CS:

$$\begin{split} IL_{WBSS}(dB) &= 2 \cdot IL_{FIR}(Taps) \\ &+ IL_{CROSSBAR} \, (Worst, \; Best, \; Average). \end{split} \tag{1}$$

## D. MG-ON Scaling Studies and Capacity Evaluation

#### 1. Analytical Formalism

Regarding the scalability analysis of the MG-ON, we evaluate various scenarios of different configurations of spatial lanes and node degrees to investigate the throughput capacity of the MG-ON, considering both optical routing and add/drop traffic.

The total number of deployed WBSSs for routing and select per degree (*D*) and spatial lanes (*Si*) is defined by the number of fiber ingress/egress ports:

$$N_{\text{WBSS}} = \sum_{i=1}^{D} (2 \cdot S_i) .$$
 (2)

Furthermore, the port count of WBSSs per degree (*D*) is derived by

$$P_{\text{WBSS}} = \sum_{j=1}^{D-1} (S_j) + K_B,$$
 (3)

in support of routing to other directions and spatial lanes, and *K<sup>B</sup>* is the additional port count per WBSS devoted to flex-band add/drop (one up to four flexible bands). Finally, the port count for the inter-OXC is given by

$$P_{\text{INTER-OXC}} = \left[ \sum_{i=1}^{D} (K_B \cdot S_i) + N_{BTx} + K_w \right]$$

$$\cdot \left[ \sum_{i=1}^{D} (K_B \cdot S_i) + N_{BRx} + K_w \right], \quad (4)$$

where *NBTx*/*NBRx* represents the number of band transmitters/receivers in the add/drop part of the node (Layer 2). *K <sup>W</sup>* represents the ports of the inter-OXC dedicated to switching to Layer 3 in support of wavelength granularity.

The following expression estimates the number of band transceivers:

$$N_{BTx} = N_{BRx} = \frac{1}{2} \cdot \sum_{i=1}^{D} (S_i).$$
 (5)

Next, the intra-OXC port count, operating in the *j*th band, is given by

$$P_{\text{INTRA-OXC}} = \left[ \left( 1 + K_{j \text{legacy}} \right) \cdot \left( N_{j \text{WSS}} + P_{j \text{WSS}} \right) \right]^2, \quad \textbf{(6)}$$

where *K <sup>j</sup>*legacy denotes the percentage of ports of the intraband granularity OXC for local add/drop in the *j*th band. In the current study, we consider that 25% of the channels that enter/exit the node are dropped/added to/from the intra-OXCs.

The number of the WSSs operating in the *j*th band is given by

$$N_{jWSS} = 2 \cdot K_j \sum_{i=1}^{D} (S_i \cdot K_B),$$
 (7)

where *K <sup>j</sup>* is a percentage of the number of ports of the interband granularity OXC connected to the WBSSs. In other words, bands sent down to the inter-band OXC must emerge either at a band transceiver or a WSS for wavelength processing. The factor *K <sup>j</sup>* captures the fraction destined to the WSS of the number of ports of the inter-band granularity OXC that lead to the WSSs operating in the *j*th band. MG-ON throughput is the product of the number of I/O fibers, supported bandwidth (spanning S + C + L = 21.6 THz minus guard bands), and spectral efficiency (SE). In our case, we consider an SE of 10 b/s/Hz, by, e.g., assuming polarization multiplexed channels of 128 Gbaud and 32-quadrature amplitude modulation (QAM) or even higher cardinality modulation formats.

#### 2. Scalability Performance Assumptions

The component and capacity scaling studies are based on the following key assumptions:

- 1. **WBSS scaling**. The port count or switching radix of WBSS modules scales linearly with the number of spatial lanes, maintaining compatibility with SDM systems. Add/drop ports connected to Layer 2 are included in port count calculations.
- 2. **Band routing strategy**. Up to four contiguous bands can be routed/switched. Two remain in Layer 1 and are directed to egress ports; the other two are transferred between Layer 1 and Layer 2. Of the latter, one is routed to/from Layer 2 transceivers, while the other connects to/from Layer 3.
- 3. **Full fiber switching**. Full fiber switching (FFS) is enabled when FIRs operate in pass-through mode, supporting fullspectrum switching. FFS is more likely to become popular as router interfaces occupy the entire optical bandwidth and with SDM link-parallelism scale out.
- 4. **OXC port calculations**. Inter- and intra-OXC port counts are based on distinct ingress and egress ports. However, only ingress ports are considered in throughput calculations, as they represent incoming traffic to the node.
- 5. **Guard bands in Layer 2**. Throughput calculations for Layer 2 account for guard bands—transition bandwidths excluded from the usable UWB spectrum, which spans up to 21 THz.

Total node capacity is primarily determined by the number of spatial lanes (S) and the node degree (D), across all three layers (Layers 1–3). To accurately assess capacity and scalability, we evaluate multiple network design scenarios, accounting for both pass-through and add/drop traffic. We consider small

![](_page_7_Figure_3.jpeg)

Fig. 6. Total MG-ON throughput for different node configurations: small (D = 4), medium (D = 5), and large-scale (D = 6) for various spatial dimensions (S = 2, 4, 6, 8), considering different sizes of MG-ON node components.

(D = 4), medium (D = 5), and large-scale (D = 6) node configurations, with varying spatial dimensions S = {2, 4, 6, 8}, assuming an SE of 10 bit/s/Hz for the transceivers (TRx).

#### 3. MG-ON Scalability Results

Figure 6 illustrates how net throughput scales with the number of MG-ON components—flex-WBSSs, inter-OXCs, WSSs, and intra-OXCs—highlighting the trade-offs between capacity and hardware requirements across all three MG-ON layers. A small-scale node with D = 4 achieves 3.76 Pb/s using only Layer 1 and 32 1 × 14 flex-WBSSs. Medium-scale configurations, such as D = 5 and S = 8, reach ∼9.4 Pb/s (via FFS) using 80 1 × 34 flex-WBSSs. Large-scale nodes with D = 6 and S ≥ 8 can surpass 10 Pb/s, though this configuration requires more than 80 WBSSs. Higher degrees and spatial lane counts yield increased throughput at the extra cost of greater hardware complexity.

Layer-specific analysis shows that maximum capacities are ∼6 Pb/s for Layer 2 and ∼3 Pb/s for Layer 3, with Layer 1 offering up to 4 Pb/s more capacity due to its ability to support high traffic volumes. This capacity gain underscores the rationale for transitioning from waveband switching to full fiber switching. For example, in Layer 2, a small-scale node (D = 4, S = 2) achieves 0.9 Pb/s using a 26 × 26 port inter-OXC.

In large-scale node configurations, significantly higher capacities are achievable, albeit with increased hardware demands. For example, with D = 6 and S = 8, a maximum capacity of 5.6 Pb/s is attained using a 156 × 156 port inter-OXC. In Layer 3, designed for legacy support, throughput scales linearly with the number of spatial lanes. Degree-6 nodes deliver the highest performance, reaching ∼3.1 Pb/s at S = 8, enabled by 96 1 × 10 WSSs and a 960 × 960 port intra-OXC. Conversely, Degree-4 nodes yield the lowest throughput of 0.5 Pb/s at S = 2 using 16 1 × 8 WSSs and a 128 × 128 port intra-OXC. SE is calculated assuming UWB operation over the 1460–1625 nm band (∼21.6 THz across the S + C + L bands). The transceiver rate is 1.6 Tb/s per wavelength [5]. The proposed MG-ON node—integrating novel flex-WBSSs and advanced transceivers—can achieve net throughputs beyond 10 Pb/s.

# E. MG-ON Cascadability Studies

In UWB systems, the primary physical-layer impairments limiting performance are amplified spontaneous emission (ASE) noise, nonlinear interference (NLI), and stimulated Raman scattering (SRS). To quantify their combined impact on the transmitted signal for the *i*th channel after *j* fiber spans—crucial for node cascadability studies—we use the optical signal-to-noise plus interference ratio (OSNIR) as the merit function [26]:

$$OSNIR = \frac{P_i}{P_{ASE,i} + P_{NLi,i}},$$
 (8)

where *P<sup>i</sup>* is the power of the *i*th channel at the node egress, and *P*ASE,*<sup>i</sup>* and *P*NLI,*<sup>i</sup>* denote the powers due to ASE and NLI accumulation for the *i*th channel at the end of the path, respectively. The power of NLI can be estimated using the closed-form expression of [26], while to calculate the power of ASE noise at the end of an optical link consisting of *N<sup>s</sup>* fiber– x-doped fiber amplifier (xDFA) spans (with x representing the ion doping providing gain in each band), we exploit the following closed-form expression:

$$P_{\text{ASE},i} = \sum_{j=1}^{N_s} \left[ h f_i (NF \cdot G_i - 1) B_0 \prod_{r=i+1}^{N_s} G_{\text{SRS},r} \right].$$
 (9)

The cumulative ASE noise over a transmission path is obtained by summing the ASE power contributions from each span.

Table 2. Insertion Losses of the WBSS When the Switching Is Performed Using MZIs Set at the Cross and Bar States

|             | S1-band  | S2-band  | C-band   | L-band   |
|-------------|----------|----------|----------|----------|
| Cross state | 19.96 dB | 15.71 dB | 14.81 dB | 14.81 dB |
| Bar state   | 15.09 dB | 14.94 dB | 14.91 dB | 14.91 dB |

Table 3. Physical Layer Parameters for the Different Bands Considered in the Node Cascadability Studies

|                | S1-band | S2-band                       | C-band | L-band    |
|----------------|---------|-------------------------------|--------|-----------|
| Range (nm)     |         | 1460–1485 1490–1525 1530–1565 |        | 1570–1625 |
| Nch            | 69      | 92                            | 87     | 129       |
| λ (nm)         | 1472.5  | 1507.5                        | 1547.5 | 1597.5    |
| α (dB/km)      | 0.243   | 0.225                         | 0.211  | 0.210     |
| D (ps/nm/km)   | 12.38   | 14.58                         | 16.94  | 19.69     |
| γ (1/W/km)     | 1.50    | 1.44                          | 1.32   | 1.24      |
| Aeff (µm2<br>) | 74      | 76                            | 80     | 83        |
| NF (dB)        | 5.5     | 5.5                           | 5.5    | 6         |

The *G*SRS,*<sup>j</sup>* captures the SRS-induced gain or loss in the *j*th span, computed using the form in [27], which models power exchange across spectra up to 35 THz.

In order to estimate the WBSS losses, we exploit Eq. (1) for two cases, when the switching is performed in a) a cross state and b) a bar state. Following the estimations shown in [25] and adding the IL of the FIR filters with 56 taps (5.6 dB IL per FIR filter), the total insertion losses of the WBSS (basic parameters derived from experimental data) for the average case in the crossbar switch and for the middle wavelength of four bands (S1, S2, C, and L), when the switching is performed in the cross and bar states, are tabulated in Table 2.

To mitigate these losses, the parallel amplification scheme is exploited, as in [26,27], where several DFAs are placed in parallel (four in our case). In addition, the parallel amplification scheme is also exploited to compensate for the losses induced by the optical fiber. In both cases, the amplification gain is equal to either the WBSS or the fiber losses, plus 2 dB for the losses of the band filters placed before and after the xDFAs. The physical layer parameters of the different bands considered in our study are illustrated in Table 3. Each channel is operated at a baud rate of 50 Gbaud.

An additional assumption in this study concerns the mitigation of SRS-induced power tilt. Prior work addresses this using three main approaches. The first involves power allocation algorithms [28–30], which estimate per-channel input power such that the output power remains uniform across all channels in a band. While hardware-free, this method has high computational complexity, especially with large channel counts. The second method integrates an attenuation function within the WBSS, enabling dynamic spectral tilt correction similar to standard WSS-based solutions [31]. The third method uses pre-compensating filters [32,33], designed with an inverse spectral tilt to offset SRS-induced gain, thereby flattening intra-band power. This method is static, best suited for fixed scenarios such as fully populated links. In this study, we adopt the third approach, assuming filters are placed within the amplification stage at each node ingress. The analysis is based on Telefónica Spain's national network topology [34], assuming average inter-node distances of 150 km (three 50 km spans). DFAs are positioned before the first and after the second WBSS to fully offset WBSS losses. All channels are injected at the first node, traverse Layer 1 of *N* − 1 MG-ONs and are dropped at Layer 3 of the Nth MG-ON.

The physical-layer performance is estimated using the closed-form expressions of Eqs. (8) and (9), including ASE noise from the MG-ON amplifiers. Band power levels are optimized via two methods: (i) s-OSNIR (*s* stands for similar), equalizing OSNIR across all bands, and (ii) 2z-OSNIR (2z stands for two zones), leading to higher OSNIR in the C- and L-bands and lower OSNIR in the S-band. To calculate the OSNIR values for s-OSNIR or 2z-OSNIR, we exploited the methodology of [34] to calculate the power for the middle channel of each band. Figure 7 presents the OSNIR evolution across cascaded MG-ONs with MZIs set to either the cross or bar state. With s-OSNIR [Figs. 7(a) and 7(b)] and 2z-OSNIR [Figs. 7(c) and 7(d)], the bar state yields ∼0.8 dB higher OSNIR due to reduced S-band ASE noise, stemming from lower required gain. Under s-OSNIR, PM-16QAM can interconnect adjacent nodes using all bands. With 2z-OSNIR, PM-16QAM is viable across two nodes in the C- and L-bands, while the S-band supports only adjacent-node connectivity in the bar state. PM-8QAM supports up to three MG-ONs under s-OSNIR and five MG-ONs using the C- and L-bands in 2z-OSNIR. PM-QPSK maintains performance across six (cross state) and seven (bar state) nodes in s-OSNIR and across eleven and more than four nodes in the C–L- and S-bands, respectively, under 2z-OSNIR. Overall, the study shows that national-scale networks (∼1000 km, or seven MG-ON hops) can reliably support PM-QPSK under s-OSNIR, and potentially higher-order formats (e.g., PM-16QAM) under 2z-OSNIR depending on the connectivity and capacity objectives set by the network designer.

# 3. INNOVATIVE oDAC-BASED TRANSCEIVERS FOR THE X-HAUL

The advances in both MG-ON and ROADM-based nodes emphasize the need for novel, reconfigurable transceiver architectures that can seamlessly align with the diverse switching capabilities and bandwidth, power, and cost requirements of next-generation optical nodes. All-optical signal processing (AOSP) techniques [35–40] can address these demands by replacing power-hungry electronic components [e.g., digital signal processing (DSP) engines and digital-to-analog and analog-to-digital converters (DACs/ADCs)] with alternatives that employ all-optical solutions. The combination of reconfigurable high-capacity transmitters that can change the order of the employed modulation format on-the-fly (e.g., from 64/16QAM to PAM8/4) in a cost- and energy-efficient manner has been proposed. In this respect, the concept of oDAC can provide the flexibility needed in terms of switching between different constellation formats and tackle the constraints that hinder commercial transceivers [41,42]. Initially, the use of serial segmented Mach–Zehnder modulators (SEMZMs) was explored, where multiple modulation segments are placed along the MZM waveguides to serially

![](_page_9_Figure_3.jpeg)

Fig. 7. OSNIR evolution for a different number of MG-ONs, using the s-OSNIR method for (a) the cross state and (b) the bar state and the 2z-OSNIR method for (c) the cross state and (d) the bar state.

accumulate binary-modulated optical phases [43,44]. This approach leverages binary-weighted phase shifts across different segments, with each segment contributing specific phase contributions to generate multi-level optical signals. We have investigated the "perfect" segment length ratio for a PAM4 segmented oDAC in [45]. Along these lines, a similar architecture is introduced where multiple MZMs are arranged in parallel rather than in series [41]. The multi-parallel oDAC (MPoDAC) configuration demonstrates this concept through a practical implementation where a continuous wave (CW) optical signal is split using tunable optical splitters to feed multiple parallel MZM paths. For example, as shown in Fig. 8(a), an optical PAM8 signal can be realized by configuring the power ratios to 3/7 and 4/7, where the algorithmic intelligent controller (AIC) is responsible for controlling and calibrating the optical paths by tuning phase modulators (PMs). The AIC implements control and calibration (C&C) algorithms as discussed in [41,46], which provide the methodology in general for C&C of large-scale PICs (as is the case, e.g., for the WBSS and interlacer PICs). Figure 8(b) illustrates the concept of combining the two optical signals into one. A fabricated oDAC chip is provided in Fig. 8(c), with its capabilities presented in [47]. Figure 9 demonstrates the performance comparison of 64-QAM signal generation using two distinct approaches, highlighting the advantages of the novel oDAC architecture over conventional methods.

More specifically, Fig. 9(a) shows the generated signal constellation for a conventional modulator utilizing PAM-8 uniform electrical drivers configured to operate with backoff (i.e., reduced peak-to-peak voltage) to maintain MZM operation in the linear regime, where the highlighted red area represents the resulting modulation loss [42]. Despite the back-off, some residual optical distortion will also arise (evidenced by the unequal symbol spacings). Figure 9(b) illustrates the resulting constellation for the novel two-path oDAC, where the parallel MZM oDAC architecture enables operating the MZMs at full-scale driving voltage (thus minimizing the undesirable modulation loss and optical distortion), while the non-linearity of the MZM transfer function suppresses the electronic drivers' noise [as shown in Fig. 9(b)], resulting in further performance improvement of the signal constellation quality, collectively reaching 6.6 dB EVM improvement in the particular simulation setup [48]. This beneficial "noise squelching" effect is more pronounced in the outer symbols

![](_page_9_Figure_8.jpeg)

Fig. 8. (a) Operation schematic of an oDAC generating an optical PAM8 signal. (b) Operational concept of an oPAM8 oDAC. (c) Fabricated oDAC PIC [47].

![](_page_10_Picture_3.jpeg)

Fig. 9. 64-QAM signal generation using three different methods. (a) The conventional modulator was used where PAM-8 electrical drivers were employed without predistortion. The red area represents the modulation loss that the conventional Tx suffers from in order to operate in the linear region of the MZM. In (b), we show that, by using the novel oDAC modulator with two parallel MZM paths, we achieve significant improvement in signal constellation quality compared with the conventional Tx, as discussed in [48].

of each quadrant of the constellation diagram, in which the symbols are created with driving voltages that reach the edge of the transfer function, and less pronounced in the inner symbols of the quadrant, where the symbols are created exploiting the linear region of the MZM. Recent work has advanced to hybrid serial–parallel designs that exploit both approaches simultaneously [49]. The innovative two serial–two parallel oDAC architecture parallelizes a pair of optimized two-segment serial MZMs driven by uncoupled NRZ signals. This configuration can generate up to 256QAM constellations using only eight uncoupled NRZ drivers in an IQ-nested configuration, achieving remarkable data rates of 3.2 Tbps per wavelength using commercially available photonic and electronic components. The serial–parallel hybrid approach optimizes the segment/branch ratio to achieve higher performance, as shown in [50]. In terms of the power consumption, the oDAC-based transceivers achieve over 30%–40% reduction per bit compared to conventional electronic digital-to-analog converter (eDAC)-based solutions [24]. In conclusion, the oDAC innovation offers a path to bit-rate scalable, energy-efficient transceivers by replacing high-resolution eDACs with parallel MZMs driven by low-resolution PAM2/PAM4 drivers/eDACs that directly synthesize high-order multi-level optical signals.

## 4. SUMMARY AND CONCLUDING REMARKS

In this work, we propose an advanced optical infrastructure designed to fulfill the stringent performance requirements of emerging 6G mobile networks. Our forthcoming infrastructure spans the fronthaul, midhaul, and backhaul segments of the x-haul optical network, integrating a suite of state-ofthe-art technologies to enable ultra-high capacity, low latency, high energy efficiency, and software-defined programmability. By incorporating novel switching and transceiver technologies across all network segments, our architecture delivers unprecedented levels of scalability, efficiency, and flexibility. At the core of the infrastructure lies a multi-granular optical node (MG-ON), utilizing novel PIC-based waveband selective switches (WBSSs), achieving a scalable throughput exceeding 10 Pb/s while maintaining superior flexibility and spectral efficiency. The fronthaul segment is enhanced by an SDPtMP architecture, incorporating the interlacer module and achieving a threefold capacity improvement compared to conventional PtMP approaches. Finally, across all segments, the deployment of oDAC-based transceivers offers bit rates beyond 1 Tb/s per channel with improved transmission performance while drastically reducing power consumption per bit. Finally, cascadability studies over an existing topology confirm strong signal performance over national-scale distances (∼1000 km) using PM-QPSK or even higher-order modulation schemes under different OSNIRs. Future research will focus on real-world implementation trials of the proposed infrastructure, leveraging AI-driven orchestration to enhance automation, adaptability, and overall performance in complex 6G environments.

Funding. HORIZON EUROPE Framework Programme (101096909, 101139134).

Acknowledgment. The authors would like to acknowledge the support of Polariton Technologies Ltd. The publication fees of this manuscript have been financed by the Research Council of the University of Patras.

Disclosures. The authors declare no conflicts of interest.

## REFERENCES

- 1. "Framework and overall objectives of the future development of IMT for 2030 and beyond," ITU-R Recommendation M.2160-0 (2023).
- 2. D. Uzunidis, K. Moschopoulos, C. Papapavlou, et al., "A vision of 6th generation of fixed networks (F6G): challenges and proposed directions," Telecom 4, 758–815 (2023).
- 3. I. Tomkos, C. Christofidis, D. Uzunidis, et al., "The 'X-Factor' of 6G networks: optical transport empowering 6G innovations," IT Prof. 26, 32–39 (2024).
- 4. I. Tomkos, D. Uzunidis, K. Moschopoulos, et al., "The role of optical networking in the 6G era," in Optical Fiber Communication Conference (OFC) (2024), paper Tu3B.1.
- 5. https://6g-flexscale.eu/en [accessed 1 June 2025].
- 6. https://proteus-6g.eu/ [accessed 1 June 2025].
- 7. A. Larranaga, S. Lagen, J. M. Fabrega, et al., "Fronthaul/midhaul networks: capacity and latency requirements imposed by 6G disaggregated RANs," IEEE Commun. Mag. 63(5), 86–93 (2025).
- 8. P. Iovanna, A. Bianchi, A. Bigongiari, et al., "Packet-optical transport network for future radio infrastructure," J. Opt. Commun. Netw. 16, D96–D110 (2024).
- 9. P. Iovanna, F. Cavaliere, F. Testa, et al., "Future proof optical network infrastructure for 5G transport," J. Opt. Commun. Netw. 8, B80–B92 (2016).
- 10. L. Fan, Y. Yang, S. Gong, et al., "Hardware-efficient and robust DSP scheme for coherent DSCM system in presence of transmitter IQ impairments," J. Lightwave Technol. 41, 6187–6198 (2023).
- 11. D. Welch, A. Napoli, J. Back, et al., "Digital subcarrier multiplexing: enabling software-configurable optical networks," J. Lightwave Technol. 41, 1175–1191 (2023).

- 12. C. Christofidis, G. Gorgias, H. Georgopoulos, et al., "Spatiallydiverse point-to-multipoint optical distribution network for enhanced 6G fronthaul," in International Conference on Photonics in Switching and Computing (PSC), Mantova, Italy, 2023.
- 13. D. M. Marom, C. G. H. Roeloffzen, R. Botter, et al., "Fine-resolution, four-port optical interlacer for subcarrier-level optical fronthaul networking," in IEEE Summer Topicals Invited (2024).
- 14. J. M. Rivas-Moscoso, F. Arpanaei, G. Otero Pérez, et al., "TEFNET24: reference packet optical network topology for edge to core transport," J. Opt. Commun. Netw. 16, G28–G39 (2024).
- 15. A. Rashidinejad, A. Yekani, T. A. Eriksson, et al., "Real-time point-tomultipoint for coherent optical broadcast and aggregation–enabled by digital subcarrier multiplexing," in Optical Fiber Communication Conference (OFC) (2023), paper W3H.1.
- 16. D. Uzunidis, C. Christofidis, I. De Francesca, et al., "Quantifying the operational benefits of deep learning based dynamic traffic prediction using real-world dataset," in Optical Fiber Communication Conference (OFC) (2025), paper W2A.46.
- 17. D. M. Marom, Y. Miyamoto, D. T. Neilson, et al., "Optical switching in future fiber-optic networks utilizing spectral and spatial degrees of freedom," Proc. IEEE 110, 1835–1852 (2022).
- 18. N. K. Fontaine, M. Mazur, R. Ryf, et al., "36-THz bandwidth wavelength selective switch," in European Conference on Optical Communication (ECOC), Bordeaux, France, 2021.
- 19. T. Kuno, Y. Mori, S. Subramaniam, et al., "Design and evaluation of a reconfigurable optical add-drop multiplexer with flexible wave-band routing in SDM networks," J. Opt. Commun. Netw. 14, 248–256 (2022).
- 20. K. Nakada, H. Takeshita, Y. Kuno, et al., "Single multicore-fiber bidirectional spatial channel network based on spatial cross-connect and multicore EDFA efficiently accommodating asymmetric traffic," in Optical Fiber Communication Conference (OFC) (2023), paper M4G.7.
- 21. K. Matsumoto and M. Jinno, "Core selective switch based branching unit architectures and efficient bidirectional core assignment scheme for regional SDM submarine system," in Optical Fiber Communication Conference (OFC) (2022), paper W3F.3.
- 22. M. U. Masood, I. Khan, L. Tunesi, et al., "Network performance of ROADM architecture enabled by novel wideband-integrated WSS," in IEEE Global Communications Conference (GLOBECOM), Rio de Janeiro, Brazil, 2022, pp. 2945–2950.
- 23. R. Schmogrow, "Solving for scalability from multi-band to multi-rail core networks," J. Lightwave Technol. 40, 3406–3414 (2022).
- 24. K. Moschopoulos, V. Tsourtis, C. Christofidis, et al., "Reducing the power consumption of optical interconnects by employing oDAC-based transmitters," Proc. SPIE 13374, 133740B (2025).
- 25. C. Papapavlou, K. Paximadis, B. Gomez, et al., "Performance analysis of an UWB/SDM optical network node with PIC-based WaveBand Selective Switches (WBSSs)," in Conference on Laser & Electro-Optics (CLEO), Charlotte, North Carolina, 2024.
- 26. D. Uzunidis, E. Kosmatos, C. Matrakidis, et al., "Strategies for upgrading an operator's backbone network beyond the C-band: towards multi-band optical networks," IEEE Photonics J. 13, 7200118 (2021).
- 27. D. Uzunidis, K. Nikolaou, C. Matrakidis, et al., "Closed-form expressions for the impact of stimulated Raman scattering beyond 15 THz," in European Conference on Optical Communication (ECOC) (2022).
- 28. N. Guo, G. Shen, N. Deng, et al., "Can channel power optimization with GSNR flatness maximize capacities of C+L-band optical systems and networks?" J. Lightwave Technol. 42, 5506–5521 (2024).
- 29. A. Anchal and E. Lichtman, "A few milliseconds-fast SRS-induced loss and tilt compensation algorithm for dynamic C+L-band networks," in European Conference on Optical Communication (ECOC), Basel, Switzerland, 2022.
- 30. B. Correia, R. Sadeghi, E. Virgillito, et al., "Power control strategies and network performance assessment for C+L+S multiband optical transport," J. Opt. Commun. Netw. 13, 147–157 (2021).
- 31. R. Kraemer, F. Nakamura, M. van den Hout, et al., "Multi-band photonic integrated wavelength selective switch," J. Lightwave Technol. 39, 6023–6032 (2021).

- 32. R. K. Jana, A. Srivastava, A. Lord, et al., "Effect of gain flattening filter placement for nonlinear-impairment mitigation in multiband optical transport network," in IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS), Jaipur, India, 2023, pp. 102–107.
- 33. T. Peng, N. Guo, T. He, et al., "Pre-tilting gain for multi-stage C+Lband EDFA by gain flattening filter," in Asia Communications and Photonics Conference (ACP), Shenzhen, China, 2022, pp. 804–808.
- 34. K. Nikolaou, D. Uzunidis, F. Arpanei, et al., "Maximizing the transport capacity of optical multi-band WDM systems through power optimization," in Optical Network Design and Modeling (ONDM), Madrid, Spain, 2024.
- 35. Y. Sobu, Y. Tsunoda, T. Mori, et al., "High-speed and low-power optical DAC transmitter using all-silicon lumped segmented modulator directly driven by CMOS inverter driver," in Optical Fiber Communication Conference (OFC) (2024), paper Th2A.11.
- 36. A. Talkhooncheh, W. Zhang, M. Wang, et al., "A 2.4 pJ/b 100 Gb/s 3D-integrated PAM-4 optical transmitter with segmented SiP MOSCAP modulators and a 2-channel 28 nm CMOS driver," in International Solid-State Circuits Conference (2022).
- 37. I. Tomkos, A. Tolmachev, A. Agmon, et al., "Low-cost/power coherent transceivers for intra-datacenter interconnections and 5G fronthaul links," in 21st International Conference on Transparent Optical Networks (ICTON), Angers, France, 2019.
- 38. C. Doerr, S. Chandrasekhar, P. Winzer, et al., "Simple multichannel optical equalizer mitigating intersymbol interference for 40-Gb/s nonreturn-to-zero signals," J. Lightwave Technol. 22, 249–256 (2004).
- 39. A. Nespola, G. Franco, F. Forghieri, et al., "Proof of concept of polarization-multiplexed PAM using a compact Si-Ph device," IEEE Photonics Technol. Lett. 31, 62–65 (2019).
- 40. Y. Zhao, C. Doerr, F. G. Vanani, et al., "Dual-polarization IMDD system for data-center connectivity," J. Lightwave Technol. 43, 6044– 6049 (2025).
- 41. M. Nazarathy and I. Tomkos, "Accurate power-efficient formatscalable multi-parallel optical digital-to-analogue conversion," Photonics 8, 38 (2021).
- 42. K. Moschopoulos, J. Lambrecht, M. Verplaetse, et al., "Challenges in scaling transceiver bit rate to 1.6 Tbps and beyond," in 14th International Symposium on Communication Systems, Networks and Digital Signal Processing (CSNDSP), Rome, Italy, 2024.
- 43. A. Giuglea, G. Belfiore, M. Khafaji, et al., "Comparison of segmented and traveling-wave electro-optical transmitters based on silicon photonics Mach-Zehnder modulators," in Photonics in Switching and Computing (PSC), Limassol, Cyprus, 19–21 September 2018, pp. 2018–2020.
- 44. J. Verbist, J. Lambrecht, M. Verplaetse, et al., "DAC-less and DSPfree 112 Gb/s PAM-4 transmitter using two parallel electroabsorption modulators," J. Lightwave Technol. 36, 1281–1286 (2018).
- 45. M. Nazarathy and I. Tomkos, "'Perfect' PAM4 serial digital-optical conversion," IEEE Photonics Technol. Lett. 33, 475–478 (2021).
- 46. J. Fisher, A. Kodanev, and M. Nazarathy, "Multi-degree-offreedom stabilization of large-scale photonic-integrated circuits," J. Lightwave Technol. 33, 2146–2166 (2015).
- 47. D. Moor, "420 Gb/s plasmonic optical DAC for coherent and IM/DD," in European Conference on Optical Communication (ECOC) (2025).
- 48. K. Moschopoulos, M. Nazarathy, and I. Tomkos, "Scalable multilevel oDAC-based PAM-m | QAM-m2 Tx using just PAM-2|4 electronic drivers—comparative performance," in Optical Network Design and Modeling (ONDM), Madrid, Spain, 2024.
- 49. M. Nazarathy and I. Tomkos, "2Serial-2Parallel optical DAC for high-resolution photonic-efficient energy-efficient 4|16|64|256 QAM," IEEE Photonics Technol. Lett. 35, 465–468 (2023).
- 50. S. Sygletos, K. Moschopoulos, M. Nazarathy, et al., "Evaluation of optical-DAC based transmitter for 1.6-Tbps data-centre interconnection," in IEEE Photonics Conference (IPC), Rome, Italy, 2024.
---
title: "A survey on challenges of Spatial Division Multiplexing enabled elastic optical networks"
tema_principal: reading
temas_relacionados: []
ano: null
autores: []
veiculo: "Optical Switching and Networking"
pdf: ../pdf/a_survey_on_challenges_of_spatial_division_multiplexing_enabled_elastic_optical_networks.pdf
---

Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/)

# Optical Switching and Networking

journal homepage: [www.elsevier.com/locate/osn](http://www.elsevier.com/locate/osn)

![](_page_0_Picture_5.jpeg)

# A survey on challenges of Spatial Division Multiplexing enabled elastic optical networks

![](_page_0_Picture_7.jpeg)

Ítalo Brasileiro [∗](#page-0-0), Lucas Costa, André Drummond

*Computer Department, University of Brazilia, Brazilia, Federal District, Brazil*

ARTICLE INFO

*Keywords:* Elastic optical networks Space-division multiplexing Multi-core fiber Crosstalk

#### ABSTRACT

Elastic Optical Networks (EON) emerge as a viable solution to support the current growing demand for bandwidth. With the application of multi-core fibers (MCF) in EON links, it is possible to increase the availability of spectral resources and explore the spatial dimension. An EON network with MCF enables Space-Division Multiplexing (SDM), allowing the use of more resources in fibers and increasing the capacity of attending circuit requests. However, the use of SDM brings some problems of interference between the circuits in fiber, with greater emphasis on inter-core crosstalk interference. In this survey, some important concepts around EON are presented, along with the characterization of SDM supporting equipment. The impact of crosstalk interference between fiber cores is discussed, with the elements responsible for its occurrence. The Routing, Modulation, Spectrum, and Core Allocation (RMSCA) problem is also characterized, and some solutions currently found in the literature are evaluated. The goal is to show the performance of different allocation techniques, in terms of the circuit blocking ratio. This survey is concluded with an evaluation of the state-of-art, and a presentation of the main challenges found from a systematic review of the related literature.

# **1. Introduction**

Currently, numerous efforts are applied to develop new technologies for higher transmission capacities in large transport networks. In this context, the *Elastic Optical Network* (EON) [\[1–5\]](#page-14-0) gain prominence because the use of light as a data vector allows achieving high transmission rates. Also, the EON allows the establishment of multiple circuits in a single fiber, through the allocation of different light frequency ranges. The EON has the optical spectrum divided into frequency ranges of 12*.*5 GHz, named slots. Thus, slots can be grouped, forming channels with higher transmission capacity and allowing the establishment of circuits with larger bandwidth requirements [\[6\]](#page-14-1). Currently, most of the works in the literature considers a 4 THz C-band capacity for each link [\[7\]](#page-14-2), divided into 12*.*5 GHz frequency intervals, which results in 320 slots in each fiber [\[8](#page-14-3)[,9\]](#page-14-4).

The optical signal can use different modulation levels by shaping characteristics of the lightwave, such as amplitude, phase, and polarity. The combination of different levels of amplitude and phase applied to the optical signal enables the transmission of a higher bit amount per symbol when compared to the traditional model of one-bit per symbol *Binary Phase-Shift Keying* (BPSK). Therefore, the choice of the appropriate modulation level, the choice of route and slot range available to the circuit has become a problem frequently addressed in the EON literature, known as *Routing, Modulation Level and Spectrum Allocation* (RMLSA) [\[10\]](#page-14-5).

The RMLSA problem can also be modeled to consider interferences of the physical environment in the signal propagation [\[11\]](#page-14-6). In this context, the model is closer to reality because some constraints are added, such as the reach limitation for the modulation levels, the interference that occurs due to the fiber type used as propagation medium, and the interference that occurs between the circuits in the same fiber.

The optical fibers considered in the traditional EONs have a single core and are referred to as *Single-Core Fiber* (SCF). Recently, some authors have hypothesized the use of a different type of fiber, called *Multi-Core Fiber* (MCF) [\[12\]](#page-14-7). The MCF introduces a new dimension into the RMLSA problem, since they have more than one core (usually 7 or 12), and each core has its own slot set. Superficially, each MCF is operated as a pool of single-core fibers.

The use of MCFs enables the occurrence of *Spatial Division Multiplexing* (SDM), which results in increase of available spectral resources. Considering an EON with MCF, the RMLSA problem will present another component, characterized as *core choice*. Some papers refer to this new

<span id="page-0-0"></span>*E-mail address:* [italo.barbosabrasileiro@yahoo.com.br](mailto:italo.barbosabrasileiro@yahoo.com.br) (Í. Brasileiro), (L. Costa), (A. Drummond).

<sup>∗</sup> Corresponding author.

approach as *Routing, Modulation, Spectrum and Core Allocation* (RMSCA) problem [\[9\]](#page-14-4). There are various types of technologies for SDM transmission medium [\[9\]](#page-14-4), but this survey focuses on multi-core fiber techniques.

To ensure the application cost, the performance of a MCF with *n* cores should be the same when compared to a pool of *n* SCF. Thus, there is a reduction in monetary cost. However, to achieve the same performance of coupled *n* SCF, it is necessary to reduce the interference between the MCF cores. Among the interferences, what stands out the most is the *crosstalk*, and its intensity depends on the symbol rate, the modulation used, and especially on the physical characteristics of the fiber [\[13\]](#page-14-8). One of the main challenges for MCF scenarios [\[14\]](#page-14-9) is to achieve low crosstalk and high core density.

In [\[12\]](#page-14-7) is shown the evolution of transmission capacity in optical fibers. The authors state that the SDM concept is as old as the emergence of fiber-optical communication, but the current development of technologies that support the application of SDM has stimulated interest in the scientific community. In Ref. [\[15\]](#page-14-10) a demonstration of the first EON with spectral-spatial division is presented, with an MCF with 7 cores. The authors construct a network of 4 nodes and 5 links (approximately 3 km each) and show the feasibility of adopting MCF in optical network scenarios. The authors also present results to show the occurrence of *crosstalk* and other interferences from the physical environment. In Ref. [\[16\]](#page-14-11), the performance of the different modulation levels is investigated in the SDM scenario. They also evaluate the performance of different switching models (independent switching, joint-switching, and fractional-joint switching) for MCF. In Ref. [\[17\]](#page-14-12) an evaluation of different traffic aggregation policies is made in EON scenarios with SDM.

As shown, many papers in the literature highlight the feasibility and high performance on the application of MCF in EON. Surveys related to the SDM scenario found in the literature deal with equipment and technologies for using multi-core fibers [\[18,](#page-14-13)[19\]](#page-14-14). This paper presents a survey on the literature around *Spatial-Division Multiplexing Elastic Optical Network* (SDM-EON) found in the main publication channels. Authors in the survey [\[18\]](#page-14-13) focuses in spectrally and spatially flexible *Reconfigurable Add-Drop Multiplexer* (ROADM) architectures, classifications and their enabling technologies. Authors in survey [\[19\]](#page-14-14) review research around SDM fibers, network components and technologies (such as amplifiers, multiplexers, switches) and perform an evaluation of crosstalk interference in 7-core and 19-core fibers, considering different fiber lengths.

Differently from the mentioned surveys, this paper shows a study on different forms of considering the crosstalk interference and also analyzes different forms of resource allocation found in the literature regarding the RMSCA problem. This survey aims to check the state of the art and highlight research opportunities in SDM-EON scenarios. Some contributions of this survey are:

• Show a classification of crosstalk evaluation models, and through experimental analysis demonstrates how large can be the crosstalk impact in terms of circuit blocking.

- Performs an experiment to define crosstalk thresholds according to different modulation levels, and defines the crosstalk threshold for each of them.
- Classifies the RMSCA algorithms found in the literature.
- Compares the performance of some RMSCA proposals, to demonstrate the impact of different allocation strategies in terms of circuit blocking.
- Summarizes open research challenges, pointed out as research opportunities.

This paper is organized as follows: Section [2](#page-1-0) presents basic concepts of SDM technology; Section [3](#page-2-0) presents the proposed equipment to support SDM-EON; Section [4](#page-3-0) defines the characteristics and evaluation of *crosstalk* interference; Section [5](#page-6-0) presents the definition of the RMSCA problem and the proposed solutions found in the literature; finally, Section [6](#page-13-0) presents the challenges, conclusions and some proposals for future work.

#### <span id="page-1-0"></span>**2. Spatial Division Multiplexing in elastic optical networks**

This section presents some definitions around SDM on elastic optical networks.

The current growth of interest is observed in MCF technologies [\[12\]](#page-14-7). The MCFs have extra cores in the fiber, unlike traditional single-core fibers, and each core has its own individual set of slots. Thus, MCF has additional channels in the spatial domain, which increases the transmission capacity [\[15\]](#page-14-10). This characteristic provided by the MCF is called spatial-division multiplexing, and the elastic optical networks constituted by MCF are called SDM-EON.

The concept of SDM relies on placing numerous spatial channels in a given fiber structure or fiber arrangement [\[19\]](#page-14-14). The type of channel depends on the employed technology. Another SDM-enabling technologies besides MCF are: Single-Mode Fiber Bundle, which is an arrangement of fibers with single spatial dimension, packed together to create a fiber bundle; Multi-Mode Fibers (and Few-Mode Fiber), which are fibers that supports tens of transverse guided modes for a given optical frequency and polarization; Few-Mode Multi-Core Fibers, which are the combination of multi-core fibers and few-mode fibers; Vortex Fiber for Orbital Angular Momentum multiplexing, which uses light beams made of photons to carry orbital angular momentum; Hollow-Core Photonic Band Gap Fiber, which are hollow fibers and wave-guiding is achieved via photonic bandgap mechanism; and Multi-Element Fiber, which consists of multiple fiber elements drawn and coated together. Authors in Ref. [\[19\]](#page-14-14) presents further detail and some references to these different fiber types. The scope of this survey is delimited to MCF related papers. [Fig. 1](#page-1-1) shows some examples of multi-core fibers.

<span id="page-1-1"></span>At first sight, the use of MCFs with more cores is more advantageous, due to higher resource availability. However, the main factor of signal interference in the MCF is the leakage of a fraction of the signal power

![](_page_1_Figure_18.jpeg)

**Fig. 1.** Multi core fiber, with (a) 7, (b) 12 and (c) 19 cores.

from a given core to its neighboring cores. This phenomenon, called *crosstalk* (discussed in Section [4\)](#page-3-0), turns impracticable the allocation of some slots, due to high interference caused by the active circuits in its neighboring cores. Thus, to enable the application of MCFs with a large number of cores, the development of fibers that provide smaller crosstalk between neighboring cores is required [\[20,](#page-14-15)[21\]](#page-14-16).

In most of the papers found in the literature, 7-core fibers [\(Fig. 1 \(a\)\)](#page-1-1) are used, arranged in an hexagonal array [\[22,](#page-14-17)[23\]](#page-14-18). In this configuration, the central core presents 6 neighbors, and consequently suffers higher *crosstalk* impact. The peripheral cores (0, 1, 2, 3, 4 and 5 of [Fig. 1 \(a\)\)](#page-1-1) have only 3 neighbors each. 12-core fibers present cores ring-like arrangement [\(Fig. 1 \(b\)\)](#page-1-1). In this scenario, each core has only 2 neighbors, and all cores have the same *crosstalk* mean value. Fibers with 19 cores [\(Fig. 1 \(c\)\)](#page-1-1) have up to 6 neighbors per core, resulting in a higher incidence of *crosstalk*. Still, MCF with more cores can be used over smaller distances. For example, a MCF with 19 cores and diameter of 200 has high crosstalk, but can be applied when fiber length is limited to values close to 10 km [\[12\]](#page-14-7).

Besides the number of cores, the cores arrangement and the fiber physical properties have a strong impact on the crosstalk between the cores. [Fig. 2](#page-2-1) shows the layout of the elements in a trench-assisted MCF model.

The use of trench-assisted MCF results in a reduction in the effects of *crosstalk*. The power overlap of adjacent cores will be smaller because the trench [\(Fig. 2\)](#page-2-1) reduces the power leakage for the cores. The crosstalk of a trench-assisted MCF is around 20 dB smaller than that found in a standard MCF [\[21\]](#page-14-16). Interference between cores can be

![](_page_2_Picture_6.jpeg)

**Fig. 2.** Layout of the elements of (a) a trench-assisted MCF and (b) of one core.

reduced by increasing the space between them (which reduces the number of cores, since the diameter of the fiber does not increase proportionally) or improving the confinement of each core, like the trenchassisted fibers [\[14\]](#page-14-9). The *crosstalk* between neighboring cores also has a strong dependence on the spacing between the cores (core pitch).

The increase of outer cladding thickness was proposed [\[24\]](#page-14-19), to avoid the increase of micro-bending loss in the outer MCF surface. However, fibers with a coating diameter larger than 200 μm are inappropriate for use because it is more susceptible to fractures. Thus, a thin outer cladding is favored, to provide better core scattering, higher core density, and to maintain the fiber mechanical flexibility [\[21\]](#page-14-16).

Possible values for fiber parameters found in the literature are [\[20,](#page-14-15)[25](#page-14-20)[,26\]](#page-14-21): core pitch: 40.7–51 μm; cladding diameter: 144.6–188 μm; outer cladding thickness: 31.6–47.7 μm; coating diameter: 256–334 μm. The authors in Ref. [\[27\]](#page-14-22) present a table with different parameter sets found in the literature and verify the impact of parameters variation on the network crosstalk calculation.

For the sake of completeness, it is important to attest that SDM-EON can be implemented by other technologies besides multi-core fiber (MCF), such as few-mode fiber (FMF) or even bundles of conventional single-mode fiber (SMFB) [\[28\]](#page-14-23). Nevertheless, the vast majority of the literature defines MCF as the enabling technology for SDM, and thus will be the focus of this survey.

## <span id="page-2-0"></span>**3. Support equipment for SDM-EON**

Equipment that allows the circuit switching between different cores along the route enables the spatial lane change (SLC) [\[29\]](#page-14-24) and bring significant innovation to the SDM-EON scenario. The use of MCFs, and consequently the expansion of the link transmission capacity, coupled with the greater flexibility of switch between cores, leads to a relaxation of the RMSCA problem constraints. However, a few papers in the literature attempt to propose a system model adapted to the scenario of SDM-EON. A more in-depth analysis is presented in Refs. [\[12,](#page-14-7)[18,](#page-14-13)[29\]](#page-14-24). [Fig. 3](#page-2-2) presents a node model with support for SDM fibers.

Current optical networks have flexibility due to ROADM, which allows the establishment of independent lightpaths within an optical fiber, as well as making it possible to switch them when necessary. It is considered that future SDM-EON will enable this same flexibility. [Fig. 3](#page-2-2) presents a ROADM adapted to SDM scenario (SDM-ROADM), which performs the circuit switching between fiber cores, besides the add/drop function to transmitters and receivers (Tx and Rx, respectively) [\[12\]](#page-14-7). More detailed information around components, equipment cost, power consumption, and transceiver models can be found in Ref. [\[29\]](#page-14-24). [Fig. 4](#page-3-1) presents another switch architecture proposal for SDM technology.

<span id="page-2-2"></span><span id="page-2-1"></span>When crossing a node, the input fiber crosses a spatial demultiplexer (SDM demux), which performs the separation of the spatial channels (cores). After the split, SCF are used for each core in the input fiber,

![](_page_2_Picture_16.jpeg)

**Fig. 3.** Potential architecture of a SDM node, adapted from Ref. [\[12\]](#page-14-7).

![](_page_3_Picture_2.jpeg)

**Fig. 4.** Potential architecture of a SDM switch, adapted from Ref. [\[18\]](#page-14-13).

![](_page_3_Picture_4.jpeg)

**Fig. 5.** Photonic-lantern multiplexer [\[30\]](#page-14-25).

and each SCF is addressed to a *Wavelength-Selective Switch* (WSS). The main function of WSS is to perform switching in a lower granularity and redirect each circuit of the SCF independently. At this point, the complexity grows with the increase of the number of output ports inside the WSS. After being switched to the appropriate port, the circuit can be directed to the current node (drop) or follow the route to another node. In this case, it is directed to another WSS. This WSS adds the circuit to the SCF of the next appropriate core (not necessarily the same core of the input fiber). Then, the SCF will be multiplexed and with the other SCF composes the output MCF. Some equipment can be adapted as SDM mux/demux, such as *photonic-lantern multiplexer* (PLM) [\[30\]](#page-14-25), which compresses *n* low capillary SCF to a MCF with *n* cores [\[30\]](#page-14-25). [Fig. 5](#page-3-2) illustrates a PLM.

Based on the observation of papers related to SDM-EON equipment proposals, it is concluded that there is no precise definition of the architecture to be adopted. There are also no detailed studies of financial or energy cost for the proposed architectures, which opens up research opportunities on the topic.

# <span id="page-3-0"></span>**4. Crosstalk**

The *crosstalk* is seen as the main interference on MCF [\[22\]](#page-14-17). It occurs mainly at discrete points along the fiber, called Phase-Matching Points (PMP). The force of interaction between two cores occurs even with small perturbations in the fiber (radius of curvature *>* 1 m) [\[14\]](#page-14-9). [Fig. 6](#page-4-0) shows an example of PMP occurrence in a fiber and (b) power loss in several fiber PMPs [\[14\]](#page-14-9),

The crosstalk (after fiber propagation and installation) is a statistical value, since the occurrence of *crosstalk* in the PMPs is influenced by the phase-shift variations between the neighboring cores, and because the phase displacement is easily varied by small changes in the conditions of the fiber, such as curvature and torsion [\[25\]](#page-14-20).

In [Fig. 1 \(a\),](#page-1-1) a circuit allocated to core 0, slots 2, 3 and 4 would suffer *crosstalk* interference if circuits are allocated in cores 1, 5 or 6, in slots 2, 3 and 4. The circuit signal becomes noise if its *crosstalk* level <span id="page-3-4"></span>exceeds the threshold allowed by the network. Equation [\(2\)](#page-3-3) shows how the Crosstalk (XT) [\[31\]](#page-14-26) is calculated.

$$h = \frac{2k^2r}{\beta w_{tr}},\tag{1}$$

<span id="page-3-3"></span>
$$XT = \frac{n - n \cdot exp[-(n+1) \cdot 2hL]}{1 + n \cdot exp[-(n+1) \cdot 2hL]}.$$
 (2)

In Eq. [\(1\),](#page-3-4) *h* is the increment of *crosstalk* per unit length, *k* is the fiber coupling coefficient, *r* is the fiber bending radius, is the propagation constant and *wtr* is the distance between cores (core pitch), as defined in Ref. [\[32\]](#page-14-27). In Equation [\(2\),](#page-3-3) *n* is the number of adjacent cores (neighboring cores) and *L* is the fiber length. Some papers propose a less complex way to calculate crosstalk by using lists to store information about the impact of crosstalk in slots, which reduces the number of crosstalk verifications [\[33\]](#page-14-28). Still, in these cases, Eq. [\(2\)](#page-3-3) is also used to measure crosstalk. [Fig. 7](#page-4-1) presents a demonstration of the crosstalk occurrence in a 3-core fiber [\[34\]](#page-14-29).

<span id="page-3-1"></span>In [Fig. 7](#page-4-1) is observed that core 2 suffers more intense crosstalk, since two adjacent cores (1 and 3) present some active circuits in the same range of slots, as the slots 1, 2, 4, 5 and 6. Therefore, the circuit allocation in MCF should verify the index of allocated slots in neighboring cores to avoid *crosstalk*. This intensifies the spectral fragmentation because some allocable slots are avoided, to reduce interference.

<span id="page-3-2"></span>Crosstalk levels below −25 dB are required to avoid significant penalties in transmission [\[12\]](#page-14-7). Circuits that reach a *crosstalk* level bellow the threshold present problems in signal interpretation on the destination receiver. Therefore, circuits allocation should not occur in slots whose index is the same as occupied slots in neighboring cores, to avoid interference. However, this spectral allocation results in greater disorganization of circuits in the spectrum, since it increases the spectral fragmentation.

It is also possible to consider other physical layer interferences besides *crosstalk*. In Ref. [\[35\]](#page-14-30), the authors call *3D* the EON that use the three domains: temporal, spectral and spatial. The authors propose two physical impairment-aware algorithms (*Fragmentation-Aware Routing, Spectrum, Spatial Mode and Modulation Format Assignment* (FA-RSSMA) and *Fragmentation-Aware Routing, Spectrum, Spatial Mode and Modulation Format Assignment with Congestion Avoidance* (FA-RSSMA-CA)), and evaluate performance compared to SP-FF (*Shortest Path* and *First Fit*). The *Quality of Transmission* (QoT) of the signal is also considered.

### *4.1. Calculating crosstalk thresholds*

The paper presented in Refs. [\[9\]](#page-14-4) defines different crosstalk thresholds for each modulation level, calculated with an empirical model proposed in Ref. [\[36\]](#page-14-31). However, it is noted that the distance thresholds found in the literature [\[10\]](#page-14-5) for modulation levels are overestimated when compared to the crosstalk threshold. In other words, the crosstalk thresholds [\[9\]](#page-14-4) causes lower blocking when compared to the scenario where only are considered the distance threshold [\[10\]](#page-14-5) as equivalent to the physical impairment.

Experiments were performed to estimate the crosstalk threshold for modulations distance thresholds found in the literature. The goal is to measure the crosstalk for different values of distances, corresponding to the modulation thresholds. The EON papers found in the literature consider different reach for different modulation levels. For example, the BPSK modulation (with low spectral efficiency) has an optical threshold of 8000 km, while the 64QAM modulation (high efficiency) has a threshold of only 250 km. In this experiment, the crosstalk value is calculated by Eq. [\(2\),](#page-3-3) for each modulation distance threshold, and the result is a more appropriate crosstalk threshold.

Simulations were performed by the authors with the ONS simulator [\[37\]](#page-14-32). The independent replication method was employed to generate confidence intervals with 95% confidence level, and 5 replications. Each replication involved 100.000 requests with the following connection requests rates: 10, 20, 40, 80, 160 e 200 Gbps, all with the same

![](_page_4_Picture_2.jpeg)

**Fig. 6.** (a) Crosstalk occurrence in a PMP, adapted from Ref. [\[14\]](#page-14-9) and (b) different PMPs along the fiber.

![](_page_4_Picture_4.jpeg)

**Fig. 7.** Crosstalk occurrence in 3-core fiber.

arrival probability. A load point of 1*,* 000 Erlangs was evaluated. Connection requests follow a Poisson process with the mean holding time of 600 s, according to a negative exponential distribution and uniformlydistributed among all nodes-pairs. To do the crosstalk evaluation, the following values are used in Equation [\(2\):](#page-3-3) *k* = 4∗10−4, *r* = 50 mm, = 4∗106 e *wtr* = 40 μm as defined in Ref. [\[9\]](#page-14-4).

A pair of nodes is considered, with one bidirectional link. A total of 12 simulations are performed, and for each simulation, the link length is 1000 km longer than the previous simulations. The evaluated link lengths are from 1000 km to 10,000 km. Also, are evaluated the distances 250 km and 500 km, since they represent the reach of 64QAM and 32QAM modulations, respectively. The granularity of frequency slots is 12.5 GHz. The fiber is a 7-MCF [\(Fig. 1\(](#page-1-1)a)), with 320 slots in each core. The guard band between two adjacent lightpaths is assumed to be of 1 slot.

Considering the evaluation made in the scenario of [Fig. 8,](#page-4-2) crosstalk thresholds were defined for the modulation levels according to their respective distance threshold. [Table 1](#page-5-0) presents the crosstalk thresholds equivalent to the reach of the modulation levels.

# *4.2. Defining interference among neighbors*

Besides the constants from the physical characteristics of the MCF (such as bending radius and core pitch), two variables must be considered for crosstalk calculation. The distance L, which is obtained by the chosen route length, and the number of neighbors *n* of the core chosen for allocation.

<span id="page-4-1"></span><span id="page-4-0"></span>![](_page_4_Figure_11.jpeg)

<span id="page-4-2"></span>**Fig. 8.** Crosstalk variation with increasing of distance.

Two groups can be created to classify the SDM-EON papers in literature, based on the considered number of neighbors. The first group uses a fixed value as the number of neighbors, which is *n* = 3 to peripheral cores and *n* = 6 to central core [\[9\]](#page-14-4). Some papers classify it as a worst-case crosstalk estimation [\[38\]](#page-14-33). The second group uses a dynamic number of neighbors, which counts only neighbors with active circuits, in the same slot index of the evaluated circuit [\[39\]](#page-14-34). This case is defined as a precise XT estimation [\[40\]](#page-14-35). [Fig. 7](#page-4-1) can be cited as an example, in which the circuit allocated in slots 8 and 9 of core 2 has *n* = 1 because it has one active neighbor (slots 7 and 8 in core 3).

**Table 1** Definition of modulation threshold for the respective distance reach.

<span id="page-5-0"></span>

| Modulation | Transmission Capacity | Distance Reach (km) | Crosstalk Threshold | Threshold in literature [9] |
|------------|-----------------------|---------------------|---------------------|-----------------------------|
| BPSK       | 12.5 Gbps             | 8000                | −22.75              | −14.0                       |
| QPSK       | 25 Gbps               | 4000                | −25.76              | −18.5                       |
| 8QAM       | 37.5 Gbps             | 2000                | −28.77              | −21.0                       |
| 16QAM      | 50 Gbps               | 1000                | −31.79              | −25.0                       |
| 32QAM      | 62.5 Gbps             | 500                 | −34.80              | −27.0                       |
| 64QAM      | 75 Gbps               | 250                 | −37.81              | −34.0                       |

**Table 2** Classification of crosstalk on evaluated papers.

<span id="page-5-1"></span>

| Static N                   | Dynamic N without Neighbors XT | Dynamic N with Neighbors XT | Without XT                 | Without Classification  |
|----------------------------|--------------------------------|-----------------------------|----------------------------|-------------------------|
| Yuanlong Tan et al. [34]   | K. Hashino et al. [41]         | R. Zhu et al. [42]          | Richardson et al. [12]     | H Tode et al. [39]      |
| Y. Zhao and J. Zhang [43]  |                                | H. Tode et al. [39]         | H. M. Oliveira et al. [44] | K. Takenaga et al. [21] |
| A. Muhammad et al. [9]     |                                | G. Savva et al. [23]        | H. M. Oliveira et al. [45] | K. Imamura et al. [46]  |
| L. Zhang et al. [47]       |                                | K. Hashino et al. [33]      | R. Zhu et al. [48]         | K. Imamura et al. [49]  |
| A. Muhammad et al. [50]    |                                | M. KlinKowski et al. [40]   | S. Sugihara et al. [51]    | Y. Cao et al. [52]      |
| M. Yang et al. [53]        |                                | F. Tang et al. [54]         | H. M. Oliveira et al. [55] | J. Zhu et al. [56]      |
| D. Kumar et al. [57]       |                                |                             | P. Khodashenas et al. [16] | K. Walkowiak et al. [7] |
| Y. Zhao et al. [58]        |                                |                             | R. Proietti et al. [35]    | M. Cantono et al. [59]  |
| H. M. Oliveira et al. [60] |                                |                             | Rui Tian et al. [17]       | S. Trindade et al. [61] |
| Y. Zhao et al. [62]        |                                |                             | S. Fujii et al. [63]       | K. Kubota et al. [64]   |
| T. Hayashi et al. [25]     |                                |                             | H. M. Oliveira et al. [65] |                         |
| S. Fujii et al. [22]       |                                |                             | D. M. Marom et al. [18]    |                         |
| Q. Yao et al. [66]         |                                |                             | S. Fujii et al. [67]       |                         |
| K. Takenaga et al. [68]    |                                |                             | Iyer S [69].               |                         |
| T. Hayashi et al. [70]     |                                |                             | M. Yaghubi et al. [71]     |                         |
| G. M. Saridis et al. [19]  |                                |                             | H. M. Oliveira et al. [72] |                         |
| K. Takenaga et al. [73]    |                                |                             | S. Iyer et al. [74]        |                         |
| M. Klinkowski et al. [75]  |                                |                             | Q. Yao et al. [76]         |                         |
| Q. Zhu et al. [77]         |                                |                             | H. Oliveira et al. [78]    |                         |
| K. Walkowiak et al. [38]   |                                |                             | P. Lechowicz et al. [79]   |                         |
| H. Oliveira et al. [80]    |                                |                             |                            |                         |
| E. Moghaddam et al. [81]   |                                |                             |                            |                         |
| Y. Lei et al. [82]         |                                |                             |                            |                         |

Besides the problem in using static or dynamic *n* value, we also highlight another concern around the crosstalk effect. In some papers, when establishing a new circuit, the crosstalk validation is also performed on active circuits of neighboring cores [\[31\]](#page-14-26). This evaluation is made in scenarios with a dynamic number of neighbors. The maximum neighbor capacity (3 to peripheric cores and 6 to the central core) is already used in the crosstalk equation for the scenario with a static number of neighbors. [Table 2](#page-5-1) presents the classification of papers related to SDM-EON literature considering the crosstalk calculation.

According to [Table 2,](#page-5-1) most papers consider scenario with *static n* or *without crosstalk*. Using scenarios without crosstalk is most appropriate for cases where the applied MCF is a bundle of SCF, and crosstalk has no impact between cores [\[16\]](#page-14-11). Nevertheless, the crosstalk verification is recommended in properly multi-core fiber scenarios, since it is the most significant interference [\[42\]](#page-14-37). Using the static number of neighbors (3 for peripheral cores and 6 for the central core) simplifies the crosstalk evaluation since the number of neighbors will be the highest possible and does not require reassessment in active circuits, on new circuit establishments.

Some papers consider a *dynamic number of neighbors*, in which crosstalk occurs only in slots with active neighboring cores, on the same slot index. These papers can be divided into two groups: one with crosstalk reassessment of previously established circuits (when their *n* values are changed), and the other group without this reassessment. We emphasize that the use of *dynamic n* implies in a slightly complex evaluation since the crosstalk of some circuits will be calculated more than once.

Another feature that contributes to complexity increase is the crosstalk evaluation when '*n*' is zero. In this case, there should be other ways to consider interferences or there will be no impairments in the established circuit and any modulation level will be allowed, even those with low reach and high efficiency. To represent other physical layer impairments, it is recommended to apply the modulation distance threshold along with the crosstalk threshold.

Experiments were made to evaluate the performance of choosing a static or dynamic number of neighbors. The modulation thresholds presented in [Table 1](#page-5-0) are used. Cases with and without reassessment of crosstalk in the active circuits are considered, in the dynamic number of neighbors scenario. The simulations were done by the authors and the scenario presents the same parameters of the scenario considered in the evaluation of [Fig. 8.](#page-4-2) The USA topology (24 nodes and 43 3 links, detailed in [Fig. 13\)](#page-11-0) is used. The allocation of resources is made by *First-Fit* policy, for the choice of core and the choice of slots.

For the performance evaluation shown in [Fig. 9,](#page-6-1) it is noticed a lower blocking ratio for the scenario with dynamic number of neighbors without the crosstalk assessment for neighbors. In this scenario, there is a high occurrence of *n* = 0, which results in remarkably low crosstalk and favors the adoption of higher-level modulations for the majority of circuits.

The worst performance occurs for the scenario with dynamic number of neighbors and crosstalk reassessment for neighbors. As in the previous scenario, the dynamic number of neighbors allows the occurrence of cases where *n* = 0. When the circuits with *n* = 0 are established, higher-level modulations are applied, because at this moment there is no crosstalk impact. Then, when occurs the resource allocation in their neighboring cores, circuits previously established prevent the establishment of new circuits. It occurs because the previously established circuits use higher-level modulation, which has lower crosstalk

![](_page_6_Figure_2.jpeg)

**Fig. 9.** Blocking variation with static and dynamic values of n.

threshold, and the modification of *n* (from 0 to 1, for example), would change their crosstalk value to values higher than the threshold allowed by the modulation level.

The choice of the crosstalk model plays an important role in the modeling of the SDM-EON scenario since it causes a variation in the blocking rate results. In the scenario with the dynamic number of neighbors and no crosstalk assessment for neighbors, there is a blocking reduction of 66*.*09*%* when compared to the static number of neighbors evaluation and 74*.*13*%* when compared to the dynamic number of neighbors evaluation with crosstalk reassessment for active circuits.

An evaluation of the crosstalk model is also made in Ref. [\[40\]](#page-14-35), in which the authors define variations of the crosstalk calculation model, defining the worst case (static number of neighbors) and the precise calculation case (dynamic number of neighbors), evaluated in fibers of 3, 7 and 12 cores. The authors propose and compare solutions to the resource allocation problem, based on variations of the First Fit policy (which may be per core or slot index), and compare different models of calculating crosstalk (worst case or precise calculation). The results indicate that 12-core fiber is less likely to block circuits using the crosstalk precise calculation model.

This Section highlights the divergence in the literature regarding the adopted crosstalk model. The adoption of different models has a strong impact on the evaluation of SDM-EON scenarios, mainly in verifying the performance of network resource allocation proposals. Allocation solutions with good performance in a scenario can lose quality when subjected to a different crosstalk assessment.

## <span id="page-6-0"></span>**5. RMSCA problem**

The circuit establishment in optical networks requires the allocation of resources, which are reserved for data transmission. In a dynamic traffic scenario, when a circuit request arrives, the source and destination nodes *pair*(*s, d*) for the new circuit are informed, in addition to the data rate for transmission. In the static traffic scenario, the traffic matrix for all the circuits is previously known, and it can be evaluated to define an optimized allocation configuration.

The first step for circuit establishment is the selection of the appropriate route between *pair*(*s, d*). The route is the set of fiber links and optical nodes that will be crossed by the circuit until it reaches the destination node. Some papers choose to allocate the shortest path [\[50\]](#page-15-6) or k-shortest paths [\[16\]](#page-14-11) routes, to efficiently accommodate the new circuit and save resources for future allocations.

After the route choice, the distance of the lightpath transmission becomes known. This information is important to solve the next step in the circuit establishment process: the choice of modulation level [\[51\]](#page-15-7). The modulation level represents the density of the optical signal. Higher-level modulations allow the transmission of more bits per signal, while the lower-levels transmit fewer bits per signal. Thus, higher

![](_page_6_Figure_12.jpeg)

<span id="page-6-2"></span><span id="page-6-1"></span>**Fig. 10.** Continuity and contiguity restrictions blocking the establishment of a 2-slot circuit.

modulation levels require less spectral resources, once they can transmit more data when compared to the lower level signals [\[51\]](#page-15-7).

Determining the modulation level enables to define the transmission capacity of the new optical circuit for the required data rate. Then it is possible to define the channel spectral size that should be created for the new lightpath. In EON, the optical spectrum is systematized as small frequency slots, which are grouped to create a new channel able to keep the new circuit. Thus, the next step of the circuit creation process is the selection of the appropriate slot range.

The problem of slot allocation must attend some restrictions from the optical medium. During propagation of the signal, it is preferable to keep the data transmission in the optical medium, avoiding conversion to the electronic medium, to reduce the resource utilization and the transmission delay. Therefore, it is required to fulfill some constraints from the optical medium, called *continuity* and *contiguity* constraints. In the continuity constraint, the permanence of the optical signal in the same slot range between the source and destination nodes becomes mandatory. Thus, the chosen slot set must be free in all links of the selected route. In contiguous constraint, the allocated slots must be adjacent to each other in the spectrum. Therefore, a single transmitter is reserved by each circuit, and only one contiguous slot range is allocated. [Fig. 10](#page-6-2) demonstrates a scenario where the constraints block the establishment of a 2-slot circuit, on the route composed by fibers A, B, and C.

[Fig. 10 \(a\)](#page-6-2) presents a 2-slots circuit request, which must be attended using the resources of [Fig. 10 \(b\).](#page-6-2) The route was chosen in a previous stage, and the circuit must travel through the fibers A, B and C. Considering the constraints, it is not possible to establish the circuit: there is no set of two adjacent free slots (restriction of contiguity) maintaining the index in all three links of the route (restriction of continuity).

As a consequence of the mentioned constraints, the occurrence of small free slot intervals interferes with the network operation, since some requests will not be attended even if there are enough free slots. These slots will be scattered in the optical spectrum (as in the example of [Fig. 10\)](#page-6-2), unable to be allocated due to the continuity and contiguity constraints. This problem is well discussed in the EON literature, and is called the *fragmentation problem* [\[83,](#page-15-39)[84\]](#page-15-40). Fragmentation increases the blocking of circuit requests, causing inefficient utilization of spectral resources [\[61\]](#page-15-17). Authors in Refs. [\[79\]](#page-15-35) evaluates several fragmentation metrics for SDM-EON networks, and proposes a resource allocation algorithm based in fragmentation metrics.

The route choice, the definition of modulation level, and spectral allocation are notable problems in the literature of EON, and together they compose the RMLSA problem. [Fig. 11](#page-7-0) demonstrates the RMLSA problem in a simple network.

As shown in [Fig. 11,](#page-7-0) the first step of the RMLSA problem is the route selection. For the node pair 1–5, there are two available short-

![](_page_7_Figure_2.jpeg)

**Fig. 11.** RMLSA problem to circuit between nodes 1 and 5.

est paths: 1–2 − 5 and 1–6 − 5. After solving the routing problem, the total distance to be crossed by the lightpath becomes known. With this information, the second step is the selection of the modulation level to be applied in the signal. The choice of the modulation level (BPSK or QPSK in the example of [Fig. 11\)](#page-7-0) is done based on the route length. High-level modulations have a shorter reach due to the fragility of the signal, which is impaired by the transmission medium. When the modulation level is selected, the number of slots for the requested bandwidth is defined. Finally, the third step is the slot allocation in the optical spectrum of the chosen route [\[85\]](#page-15-41), given the required number of slots. In this phase, the optical constraints should be considered.

With MCF, the RMLSA problem will also include the choice of the most suitable core for the circuit. Thus, the new problem is called RMSCA [\[9\]](#page-14-4). For the core allocation phase, it is important to observe the indexes of the slots already allocated in the adjacent cores (or neighbors) to the chosen core, since the interference between cores (*crosstalk*, detailed in Section [4\)](#page-3-0) is an important factor and should be considered in studies for closer proximity to real SDM-EON scenarios.

# *5.1. RMSCA: literature review*

To reduce the fragmentation problem in fiber cores, some solutions proposed to the RMSCA problem create allocation priorities [\[22](#page-14-17)[,39\]](#page-14-34). [Fig. 12](#page-7-1) presents some allocation models with (a) priorities by slots index and (b) priorities per core.

[Fig. 12 \(a\)](#page-7-1) presents an example of allocations with prioritized areas delimited by a slot range [\[39\]](#page-14-34). In this case, there are slots sets in the spectrum, which are exclusive for the allocation of circuits with a specific number of slots. As an example, in [Fig. 12 \(a\),](#page-7-1) slots 1 to 4 are exclusive for 4-slots requests in all cores. Moreover, is delimited a slot range named *common area*, which should allocate circuits that cannot be allocated in its respective prioritized area, due to resources unavailability or fragmentation. In [Fig. 12 \(b\),](#page-7-1) the circuits are allocated primarily in prioritized cores [\[22](#page-14-17)[,77\]](#page-15-33). As an example, 4-slot requests are allocated primarily in cores 5 or 6. There is also a core used as *common area*.

<span id="page-7-0"></span>Some authors evaluate the use of MCF on static traffic scenarios, in which the circuit requests have a source, destination and bandwidth defined, and the traffic matrix is known. In Ref. [\[50\]](#page-15-6), the crosstalk information is added as a constraint to the circuit establishment, and the algorithm *Shortest Path with Cumulative Spectrum Availability* (SPSA) is proposed for routing, core, and slot allocation. A 3-core MCF is considered in the evaluation. The authors observed that the effects of crosstalk are attenuated with the use of fibers with higher slots availability. It reduces the interference between cores because the circuits can be scattered in the spectrum. In Ref. [\[9\]](#page-14-4), an objective function is proposed for the choice of route, slots, and cores. The preferred resources (route, slots, and core) are those which meet the crosstalk threshold and maximize the objective function. The results show the performance of the proposed objective function, considering two different forms of modulation selection (*Modulation Format Fixed* (MFF) and *Modulation Format Switching* (MFS)).

The algorithm *Anycast Routing, Spectrum and Core Allocation with Shortest Path* (ARSCA-SP) is proposed in Ref. [\[47\]](#page-15-3), and it allocates slots closest to the lowest index slot (*First Fit*) in all cores of the network links. An ILP strategy is used to make a performance comparison. In Ref. [\[81\]](#page-15-37) is presented a crosstalk aware RMSCA solution applied to scenarios with two request types: *advance reservation* (AR), which require reserved resources when they occur, and *immediate reservation* (IR), for which the resources are chosen at the moment it is generated, with no guaranty of availability. The proposal reduces both the maximum allocated slot index (*F*max) and the Average Initial Delay Ratio (AID Ratio). The performance evaluation of AR and IR circuits is also made in Ref. [\[76\]](#page-15-32), which uses a spectrum optimization scheme based on transfer learning to predict spectrum fragmentation and reduce blocking for incoming requests.

Some papers propose solutions for routing, modulation, core, and spectral range choice in scenarios of SDM-EON with dynamic traffic. In Ref. [\[63\]](#page-15-19), an SCA (Spectrum and Core Allocation) method is proposed for core and slot selection. The algorithm reserves cores to requests with a specified number of slots and use priority levels for cores. A performance evaluation compares the proposal with the algorithms *First*

![](_page_7_Figure_13.jpeg)

<span id="page-7-1"></span>**Fig. 12.** Circuits allocated and organizated in (a) priority by slot index and (b) priority by core.

**Table 3** Classification of static RMSCA proposals found on literature.

<span id="page-8-1"></span>

| Reference                     | Core Continuity |    | XT-Aware | Protection | Contributions Highlights                                                                                                                                                                    |
|-------------------------------|-----------------|----|----------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                               | Yes             | No |          |            |                                                                                                                                                                                             |
| A. Muhammad et al. [9]        |                 | ✓  | ✓        |            | Proposes strategies for the RMSCA problem that<br>jointly optimizes the switching and spectrum<br>resource efficiency.                                                                      |
| G. Savva et al. [23]          |                 | ✓  |          |            | Proposes XT-aware RCSA solutions to provide efficient<br>resource utilization and minimize the number of<br>connections that cannot be established due to low QoT.                          |
| L. Zhang et al. [47]          | ✓               |    |          |            | The first work that considers the anycast<br>routing problem in SDM-EON with MCF. Proposes<br>an RCSA algorithm to solve the problem.                                                       |
| A. Muhammad et al. [50]       |                 | ✓  |          |            | Formulates the RCSA problem using integer linear<br>programming. Proposes an algorithm and compares the<br>performance with the ILP optimal solution                                        |
| M. Yang et al. [53]           |                 | ✓  | ✓        |            | Formulates the RCSA problem using a<br>node-arc-based ILP method and proposes<br>an XT-aware-based heuristic algorithm.                                                                     |
| S. Fujii et al. [63]          | ✓               |    |          |            | Proposes on-demand RCSA algorithm which constructs<br>virtual grid for SDM-EON.                                                                                                             |
| M. Yaghubi-Namaad et al. [71] | ✓               |    |          |            | Formulates the RMSCA problem as an ILP path-based.<br>Proposes a stepwise greedy algorithm and<br>four different sorting policies to find<br>near-optimal solution to RMSCA problem         |
| E. Moghaddam et al. [81]      |                 | ✓  | ✓        |            | Models the RMSCA problem and XT in an SDM with<br>Advance Reservation and Immediate Reservation<br>traffic. The problem is formulated as a<br>MILP and a heuristic is proposed to solve it. |
| F. Tang et al. [54]           |                 | ✓  | ✓        |            | Develops an ILP model to solve the RSCTA problem,<br>with an auxiliary graph heuristic algorithm.                                                                                           |

*Fit* and *Random*, in 7-core MCF. The proposal obtains a lower blocking ratio, smaller crosstalk average, and less fragmentation. In Ref. [\[8\]](#page-14-3), a solution is proposed for core and slot allocation. The algorithm is compared with *First Fit* and *Random Fit* allocation algorithms in a 7-core fiber, and presents better performance. The proposal also has a smaller *crosstalk* per *slot*. The comparison with *First Fit* and *Random* algorithms is also done in Ref. [\[22\]](#page-14-17), which proposes a method for core classification and prioritization, in which cores are exclusives to a given bandwidth request. The authors use 7, 12 and 19-core fibers, and check *crosstalk* through a crosstalk-by-slot (CpS) indicator, presented in Equation [\(3\)](#page-8-0) and also used in other papers [\[8,](#page-14-3)[45\]](#page-15-1):

<span id="page-8-0"></span>
$$CpS = \frac{n_C}{n_T},\tag{3}$$

In the equation, *nT* represents the number of occupied slots in the link and *nC* represents the number of occupied slots that are also occupied at the same index in adjacent cores.

In [\[39\]](#page-14-34) the *Intra-Area FF Assignment* algorithm is proposed, for spectrum and core allocation. The algorithm creates "exclusive areas" in the optical spectrum for certain bandwidths and "common areas" for allocation if the exclusive areas are unavailable. The slot allocation inside the common area follows the policy *First Fit* to circuits with an even number of slots and *Last Fit* to circuits with an odd number of slots. The proposal is compared to *Random* and *First Fit*. The authors in Ref. [\[41\]](#page-14-36) defines the concept of *XT-prohibited slot*, which are free slots that can not be allocated since they allow the increase of crosstalk to the unwanted levels. In Ref. [\[82\]](#page-15-38), the RMSCA algorithm RCSA–IC–SCM is proposed to reduce crosstalk. The results show that there is a reduction in the average crosstalk, but has a side effect in the increase of blockage due to increased spectral fragmentation.

The authors in Ref. [\[64\]](#page-15-20) presents a crosstalk-aware resource allocation. Also, they present an intra-node crosstalk modeling, which is a way to measure the occurrence of crosstalk within nodes, between fiber input and output ports, in the Wavelength Selective Switches (WSS). The proposal is compared to the crosstalk aware FF policy version. The authors in Ref. [\[77\]](#page-15-33) shows the service-classified routing, core, and spectrum assignment (SC-RCSA) algorithm, also crosstalk-aware, which allocates the spectral resources in dedicated cores. The algorithm is compared to the *First Fit* and *Random Fit* policies, in crosstalk-aware and not-aware scenarios. The SC-RCSA proposal has a slightly higher blocking ratio than its competitors but has a lower average crosstalk and fragmentation rate than the other proposals evaluated.

In [\[55\]](#page-15-11), the algorithm *Failure-Independent Path Protecting for MultiCore network* (FIPPMC) is proposed for the survivability scenario in EON. The algorithm FIPPMC creates a list of "candidate paths", which corresponds to all possible combinations of route and spectrum available to the circuit. Each candidate path receives an evaluation value, which considers the occurrence of *crosstalk*. The candidate path chosen as the primary path is the one with the lowest evaluation value, and the path for dedicated protection is the one with the lowest evaluation value and links disjoint from the main path. In Ref. [\[44\]](#page-15-0) the proposal of [\[55\]](#page-15-11) is adapted to use shared routes for protection. The same authors, in Ref. [\[45\]](#page-15-1), propose the algorithm *Minimum Interference and Failure-independent path protecting for MultiCore networks* (MIFMC), also for protection. In the proposed algorithm, the circuit is only established if there is an available disjoint route. If the disjoint route does not exist, another primary route is searched, and the disjoint routes are evaluated. This procedure is repeated until all possible primary routes are evaluated. The authors also propose RMSCA algorithm models to protection scenarios in Ref. [\[78,](#page-15-34)[80\]](#page-15-36).

The authors in Ref. [\[34\]](#page-14-29) proposes the algorithm *Crosstalk-aware provisioning strategy with dedicated path protection* (CaP) for primary and backup route selection. The algorithm chooses two disjoint routes in the first available core and slots interval, which respect the crosstalk threshold. Authors in Ref. [\[69\]](#page-15-25) proposes an RCSA strategy to protection, named FIPP-p-cycles. The algorithm seeks a route for protection, disjoint from the primary route. The algorithm uses weights (*Wi*) to fetch available links and cores, and look for a p-cycle to ensure protection. If no new p-cycle is found, the new circuit request is blocked.

Some papers take into account information about the network state during the operational phase, such as the spectral fragmentation. A spectral fragmentation analysis is done in Ref. [\[48\]](#page-15-4). The authors propose two fragmentation-aware algorithms for core and spectrum alloca-

**Table 4** Classification of dynamic XT-aware RMSCA proposals found on literature.

<span id="page-9-0"></span>

| Reference                 | Core Continuity |    | Protection | Contributions Highlights                                                 |
|---------------------------|-----------------|----|------------|--------------------------------------------------------------------------|
|                           | Yes             | No |            |                                                                          |
| S. Fujii et al. [22]      |                 | ✓  |            | Proposes RCSA algorithm which uses core                                  |
|                           |                 |    |            | prioritization policy to reduce crosstalk and                            |
|                           |                 |    |            | core classification policy to reduce fragmentation.                      |
| Y. Tan et al. [34]        |                 | ✓  | ✓          | Investigates dedicated path protection considering                       |
|                           |                 |    |            | XT in SDM-EON. Proposes an XT-aware RCSA provisioning                    |
|                           |                 |    |            | strategy with dedicated path protection.                                 |
| K. Hashino et al. [41]    |                 | ✓  |            | Proposes an XT-aware RCSA with                                           |
|                           |                 |    |            | the concept of "crosstalk prohibited frequency slot"                     |
|                           |                 |    |            | to suppress the crosstalk.                                               |
| R. Zhu et al. [42]        |                 | ✓  |            | Models the RCSA problem and uses the CASC metric                         |
|                           |                 |    |            | to measure spectrum status. Proposes two XT-aware RMSCA                  |
|                           |                 |    |            | algorithms combined with the CASC metric.                                |
| Y. Zhao et al. [43]       |                 | ✓  |            | Proposes an XT-aware cross-core virtual concatenation                    |
|                           |                 |    |            | (CCVC) RMSCA to solve the fragmentation in SDM-EON.                      |
| Q. Yao et al. [66]        | ✓               |    |            | Proposes a crosstalk estimation model with machine                       |
|                           |                 |    |            | learning in Few-mode MCF. Also proposes an XT-aware RSCMA                |
|                           |                 |    |            | algorithm to resource allocation (core, mode and spectrum).              |
| Q. Zhu et al. [77]        |                 | ✓  |            | Proposes a service-classified RCSA to improve                            |
|                           |                 |    |            | spectral efficiency in SDM-EON.                                          |
| K. Hashino et al. [33]    |                 | ✓  |            | Proposes a strict and less computationally RCSA with                     |
|                           |                 |    |            | xt-prohibited slots, to reduce the processing                            |
|                           |                 |    |            | complexity and avoids the XT influence.                                  |
| K. Walkowiak et al. [38]  |                 | ✓  |            | Proposes an RCSA algorithm based on worst-case crosstalk estimation. The |
|                           |                 |    |            | lightpath should attend the XT threshold in a translucent SDM-EON        |
|                           |                 |    |            | with distance adatpative transmission and signal regeneration.           |
| M. Klinkowski et al. [40] | ✓               |    |            | Proposes two XT-aware RSCMA algorithm that consider                      |
|                           |                 |    |            | the worst-case XT and the precise-case XT.                               |
| K. Kubota et al. [64]     |                 | ✓  |            | Proposes an RCSA with prohibited                                         |
|                           |                 |    |            | frequency slots and node interaction cost to suppress                    |
|                           |                 |    |            | crosstalk at fiber and nodes in SDM-EON.                                 |
| Y. Lei et al. [82]        |                 | ✓  |            | Proposes a RCSA which evaluates the inter-core crosstlak                 |
|                           |                 |    |            | spectrum crosstalk measurement (IC-SCM) in SDM-EONs.                     |

tion: *First Fit Multidimensional Resource Compactness* (FF-MRC) and *Random Fit Multidimensional Resource Compactness* (RF-MRC). The authors compare the results with the implementation of *Dijkstra* for routing and *First Fit* for core and spectrum allocation. In Ref. [\[31\]](#page-14-26) the same authors add *crosstalk* information to the core and spectrum allocation, and propose the *First Fit Crosstalk-Aware Spectrum Compactness* (FFCASC) and *Random Fit Crosstalk-Aware Spectrum Compactness* (RF-CASC) algorithms. In Ref. [\[51\]](#page-15-7) are created dedicated areas for the different request bandwidths. Besides, slot and core allocation are also fragmentationaware. In Ref. [\[61\]](#page-15-17) two fragmentation-aware RMSCA solutions are proposed. For the establishment of the circuit, the proposals use allocation with prioritized cores and take into account the level of spectrum fragmentation and the potential creation of bottleneck links.

The spectral defragmentation procedure can be done to overcome network fragmentation. The active circuits are reallocated, to reduce the occurrence of small ranges of free slots and to enable the establishment of new circuits. Some papers [\[86](#page-15-42)[,87\]](#page-15-43) discuss the push-pull mechanism for defragmentation, in which circuits are reallocated to different indexes and cores with no need for circuit shutdown. This is due to the slide of the circuit on empty slots. A defragmentation model is proposed in Ref. [\[58\]](#page-15-14), and uses the SC (spectrum compactness) metric. The defragmentation will occur in cores with SC value under the threshold. Defragmentation is performed by reallocating the circuit in a different core (keeping the slot range) or in a different slot range (maintaining the same cores). Defragmentation solutions are also proposed in SDM-EON with time multiplexing [\[88\]](#page-15-44).

In [\[43\]](#page-14-38), a technique called *virtual concatenation* is proposed. This model allocates slots from the same circuit in different cores in a noncontiguous way, mitigating the fragmentation problem. This approach is less discussed in the literature since the equipment has not yet been developed to support this type of allocation.

To summarize the RMSCA proposals found in the literature, [Tables 3–5](#page-8-1) are designed with important aspects of RMSCA proposals, clustered in tables for scenarios with static [\(Table 3\)](#page-8-1) and dynamic traffic. The dynamic RMSCA algorithms are divided in two tables, which groups the XT-aware [\(Table 4\)](#page-9-0) and XT-unaware [\(Table 5\)](#page-10-0) algorithms. The designed tables uses the following notation to describe the allocation models: RCSA to design routing, core, and spectrum allocation strategies; RSCMA to design routing, spectrum, core and/or mode allocation strategies; RMSCA to design routing, modulation, core and spectrum allocation strategies; and RSCTA to design routing, spectrum, core, and time allocation.

Both tables presents the main characteristics of the RMSCA proposals found in the EON-SDM literature. There is a higher utilization of dynamic traffic scenarios [\(Tables 4 and 5\)](#page-9-0), corresponding to 73*.*08*%* of the evaluated papers. Dynamic traffic scenarios are more similar to real scenarios, in which information about future circuit requests, such as duration, required bandwidth, and source and destination nodes are unknown. In addition, most of the papers do not consider the core continuity constraint (84*.*46*%*). If the core continuity is considered, a circuit must use the same core for all the links in its route. Therefore, remove the core continuity constraint implies in the relaxation of slot continuity constraint, once it is possible to maintain the same allocated slot range through the whole route and switch between cores in different links. Authors in Ref. [\[79\]](#page-15-35) performs comparation around scenarios with and without core continuity.

The XT-aware RMSCA proposals are also evaluated. These algorithms use information about crosstalk measurement to choose the best spectral resources for new circuit requests. Around 30*.*77*%* of RMSCA proposals are XT-aware. Lastly, 26*.*92*%* of the RMSCA proposals found are adapted to protection scenarios.

**Table 5** Classification of dynamic XT-unaware RMSCA proposals found on literature.

<span id="page-10-0"></span>

| Reference                  | Core Continuity |    | Protection | Contributions Highlights                                                                                        |  |  |
|----------------------------|-----------------|----|------------|-----------------------------------------------------------------------------------------------------------------|--|--|
|                            | Yes             | No |            |                                                                                                                 |  |  |
| H. Tode et al. [39]        |                 | ✓  |            | Introduces MCF or MMF and proposes a RSCMA which                                                                |  |  |
|                            |                 |    |            | exploits prioritized area concept, and is XT-aware                                                              |  |  |
|                            |                 |    |            | depending if the MCF or MMF supports XT.                                                                        |  |  |
| H. M. Oliveira et al. [44] |                 | ✓  | ✓          | Proposes an RCSA algorithm to dynamically generates                                                             |  |  |
|                            |                 |    |            | primary and backup paths using a shared bachup scheme.                                                          |  |  |
| H. M. Oliveira et al. [45] |                 | ✓  | ✓          | Proposes an RCSA algorithm to provide failure-independent                                                       |  |  |
|                            |                 |    |            | path protecting p-cycle with minimum interference.                                                              |  |  |
| R. Zhu et al. [48]         |                 | ✓  |            | Designs a metric named "multi-dimensional resource                                                              |  |  |
|                            |                 |    |            | compactness and proposes two RCSA algorithms based on it,                                                       |  |  |
|                            |                 |    |            | with first-fit and random-fit allocation policies.                                                              |  |  |
| S. Sugihara et al. [51]    |                 | ✓  |            | Proposes an RMSCA algorithm with prioritized areas to                                                           |  |  |
|                            |                 |    |            | reduce fragmentation and controls the service level of                                                          |  |  |
|                            |                 |    |            | Advance Reservation and Immediate Reservation requests.                                                         |  |  |
| H. M. Oliveira et al. [55] |                 | ✓  | ✓          | Introduces an algorithm based on p-cycle to provide                                                             |  |  |
|                            |                 |    |            | failure-independent path protection in elastic                                                                  |  |  |
|                            |                 |    |            | optical networks.                                                                                               |  |  |
| K. Walkowiak et al. [7]    |                 | ✓  |            | Proposes a RCSA algorithm for lightpath provisioning                                                            |  |  |
|                            |                 |    |            | in translucent SDM-EON, with signal back-to-back                                                                |  |  |
|                            |                 |    |            | regeneration and modulation conversion.                                                                         |  |  |
| H. M. Oliveira et al. [60] |                 | ✓  | ✓          | Investigates the problem of dynamic protection against two                                                      |  |  |
|                            |                 |    |            | simultaneous failures in SDM-EON. Proposes a path-protection                                                    |  |  |
|                            |                 |    |            | sharing spectrum and stradding p-cycle FIPP algorithm.                                                          |  |  |
| H. M. Oliveira et al. [65] |                 | ✓  | ✓          | Proposes an RMSCA algorithm to generate primary and                                                             |  |  |
|                            |                 |    |            | backup paths using shared backup scheme in SDM-EON.                                                             |  |  |
| S. Fujii et al. [67]       |                 | ✓  |            | Proposes an energy-efficient network system with                                                                |  |  |
|                            |                 |    |            | architeture on demand satisfies (AoD) nodes. Also,                                                              |  |  |
|                            |                 |    |            | proposes an on-demand RCSA algorithm that satisfies the                                                         |  |  |
|                            |                 |    |            | restricted spectrum arrangement required by the AoD nodes.                                                      |  |  |
| S. Iyer [69]               |                 | ✓  |            | Proposes an RCSA algorithm for provisioning spatial super                                                       |  |  |
|                            |                 |    |            | channels, which ensures the spectral requirements and                                                           |  |  |
|                            |                 |    |            | reduce of transceivers utilization.                                                                             |  |  |
| H. M. Oliveira et al. [72] |                 | ✓  | ✓          | Proposes an RMSCA algorithm for path protection to provide                                                      |  |  |
|                            |                 |    |            | failure-independent path protecting p-cycle.                                                                    |  |  |
| S. Iyer et al. [74]        |                 | ✓  | ✓          | Designs a independent-failure p-cycle RCSA, which                                                               |  |  |
|                            |                 |    |            | provides disjoint protection to primary routes.                                                                 |  |  |
| S. Trindade et al. [61]    |                 | ✓  |            | Proposes two RMSCA proactive algorithms to avoid spectral                                                       |  |  |
|                            |                 |    |            | fragmentation. The algorithms considers the spectral<br>fragmentation state and potential bottleneck formation. |  |  |
| Q. Yao et al. [76]         |                 |    |            | Proposes an RCSA strategy based on transfer learning in                                                         |  |  |
|                            |                 | ✓  |            | SDM-EON, considering a scenario with Advance Reservation                                                        |  |  |
|                            |                 |    |            | and Immediate Reservation.                                                                                      |  |  |
| H. Oliveira et al. [78]    |                 | ✓  | ✓          | Proposes an RCSA algorithm that employs minimum interference                                                    |  |  |
|                            |                 |    |            | routing, FIPP p-cycle, traffic grooming and spectrum overlap                                                    |  |  |
|                            |                 |    |            | to increase spectral efficiency in protected SDM-EON.                                                           |  |  |
| H. Oliveira et al. [80]    | ✓               |    | ✓          | Proposes an RCSA protection algorithm using hybrid routing and                                                  |  |  |
|                            |                 |    |            | FIPP p-cycle. The algorithm prioritizes the use of single path                                                  |  |  |
|                            |                 |    |            | routing and multipath if no single path is available.                                                           |  |  |
| P. Lechowicz et al. [79]   | ✓               | ✓  |            | Evaluates several fragmentation metrics in SDM-EON.                                                             |  |  |
|                            |                 |    |            | Proposes a fragmentation-aware RCSA algorithm that                                                              |  |  |
|                            |                 |    |            | uses information about fragmentation metrics.                                                                   |  |  |

### *5.2. Performance evaluation*

To verify the behavior of different allocation methods, we evaluate through simulations some RMSCA solutions found in the literature. The ONS simulator [\[37\]](#page-14-32) was used to perform simulations. The scenario is the same used in Section [4.](#page-3-0) Five load points were evaluated, and 5 replications were performed for each loading point.

The american USA topology (24 nodes and 43 bidirectional links) is used, shown in [Fig. 13.](#page-11-0) The granularity of frequency slot is 12.5 GHz, and all the fibers are 7-MCF [\(Fig. 1\(](#page-1-1)a)), with 320 slots in each core. The guard band between two adjacent lightpaths is assumed to be 1 slot.

Three algorithms are evaluated, to demonstrate the behavior of different schemes for resource allocation (shown in [Fig. 12\)](#page-7-1), compared to a classical literature allocation model (solution based on *First Fit* policy). The first solution, called *FF-CASC*, is an adaptation of the FirstFit algorithm. It uses the Dijkstra (DJK) algorithm [\[89\]](#page-16-0) for routing and the *FirstFit* allocation policy for slot and core selection. In the first allocation attempt for a given circuit request, the algorithm searches for the first available core and slot. When an available resource is not found or the selected slot cannot be allocated (due to physical limitations), the FF-CASC takes a step forward and uses a metric named *Crosstalk-Aware Spectrum Compactness* (CASC), to select resources (core and slot) that increases the *Spectrum Compactness* (SC). A higher SC value is associated with larger contiguous blocks of allocated slots and less occurrence of small intervals of free slots between allocated slots. The CASC metric is also used in some of the papers cited above [\[47,](#page-15-3)[48\]](#page-15-4).

The second algorithm is RF-CASC [\[31\]](#page-14-26), and it uses the same CASC metric as the FF-CASC. The first step of RF-CASC is the random selection of spectral resources (cores and slots), always according to spectral continuity and contiguity constraints. If it is not possible to attend the circuit request in the first step, the RF-CASC uses the CASC metric to select new spectral resources with higher SC value. At last, the third evaluated algorithm is the Intra-Area [\[39\]](#page-14-34). This algorithm requires a previous network simulation, to measure the occurrence of different

![](_page_11_Figure_2.jpeg)

**Fig. 13.** USA topology.

bandwidth circuits allocated in the bottleneck link. From that information, different priority areas are created inside all cores, and the available slot range for each bandwidth is proportional to that bandwidth occurrence rate in the bottleneck link. Also is added a common area ratio , which corresponds to the percentage of slots reserved for the common area. The resource allocation inside each area follows the FirstFit policy, as well as for the core allocation.

The main idea of this simple comparison is to show the performance between algorithms that consider different levels of the spectral organization, in an SDM-EON scenario. The evaluation considers the RF-CASC, an algorithm with very small spectral organization owing to random allocation; the FF-CASC, an algorithm with some level of spectral organization by the ordered resource allocation; and the Intra-Area, which prioritizes high spectral organization through the separation of allocated circuits by its required bandwidth.

The simulations were done by the authors and performed in a crosstalk-aware scenario, and different modulation levels are used. The available modulation levels are the same provided by [Table 1.](#page-5-0) The modulation maximum transmission reach is also verified, as an indicator of other physical-layer impairments beyond crosstalk. The value of *n* is dynamic for Equation [\(2\).](#page-3-3) It means that *n* corresponds to the number of active neighbors. Moreover, when a new circuit request is about to be attended, the crosstalk of previously established circuits is also reevaluated.

The following values are used in Equation [\(2\)](#page-3-3) to perform the crosstalk evaluation: *k* = 4*.*0∗10−4, *r* = 50 mm, = 4∗106 e *wtr* = 40 μm [\[9\]](#page-14-4). The metrics evaluated are the blocking ratio and bandwidth blocking ratio. [Fig. 14](#page-11-1) shows the blocking ratio for the USA topology.

![](_page_11_Figure_8.jpeg)

**Fig. 14.** Blocking ratio (%) on USA topology.

<span id="page-11-0"></span>The blocking ratio is the rate between the number of blocked circuits (as a consequence of lack of resources or physical impairments) by the total number of generated circuits. In [Fig. 14,](#page-11-1) the best performance of the FF-CASC proposal is noted, with an average reduction of 66*.*41*%* in the blocking ratio compared to the second-best competitor. Among the compared algorithms, FF-CASC maintains higher spectral organization, since it considers the sequential allocation of FirstFit policy and always tries to compress the spectrum by the CASC metric, which means to reduce the occurrence of small free slots gaps [\[31\]](#page-14-26). The Intra-Area algorithm presents a lower performance in the evaluated scenario. Intra-Area segments the spectrum into different allocation areas, each one dedicated to requests with the specific number of slots. The lower performance is justified by the wide variation in requirement of slots, resulting from the combination of 6 different generated bandwidths and 6 modulation levels available for use. This variety heads to the creation of many allocation areas, causing vast spectrum partitioning.

The RF-CASC algorithm presents average performance when compared to the two competitors, as it randomly allocates the circuits in the spectrum, but also sometimes uses the CASC metric to improve the spectral compactness. [Fig. 15](#page-11-2) shows the results of the bandwidth blocking ratio on USA topology.

The bandwidth blocking ratio is the relation between the total amount of bandwidth blocked on the network and the total generated bandwidth. When looking at [Fig. 15,](#page-11-2) the FF-CASC algorithm still performs better in terms of bandwidth blocking ratio, with an average reduction of 56*.*44*%* compared to the second-best competitor (Intra-Area). However, there is a variation in Intra-Area and RF-CASC behavior, when compared to the presented in [Fig. 14.](#page-11-1) It occurs because larger

![](_page_11_Figure_13.jpeg)

<span id="page-11-2"></span><span id="page-11-1"></span>**Fig. 15.** Bandwidth blocking ratio (%) on USA topology.

![](_page_12_Figure_2.jpeg)

**Fig. 16.** External fragmentation on USA topology.

bandwidth circuits have more difficulty to be allocated, once they need a bigger channel of contiguous and continuous slots in the spectrum. The Intra-Area algorithm makes it possible to establish these circuits due to the dedicated area for each different bandwidth requirement. The RF-CASC algorithm reduces the chances of allocating larger bandwidth circuits with the increasing load, due to its random allocation.

In addition to blocking ratio metrics, also is performed an external fragmentation assessment, a metric to measure the level of spectrum fragmentation presented in Refs. [\[85\]](#page-15-41). External Fragmentation can be measured by Eq. [\(4\).](#page-12-0)

<span id="page-12-0"></span>
$$F_{ext} = 1 - \frac{biggestFreeInterval}{totalFree},\tag{4}$$

The slot block idea is used and corresponds to a set of contiguous slots with the same state (all free or all occupied). In Eq. [\(4\),](#page-12-0) the *biggestFreeInterval* designates the number of slots in the biggest free slot block in the route, and *totalFree* represents the total sum of free slots. In this case, one free slots is a slot available continuously in the whole selected route, to the current request. [Fig. 16](#page-12-1) presents the external fragmentation results in the USA topology.

In the external fragmentation, it is possible to evaluate the average size of big free slot blocks inside the routes, and compare it to the other free slots. A higher discrepancy between the number of slots in the largest block and the number of free slots signifies a more fragmented spectrum. Randomized allocation creates higher spectral fragmentation to the RF-CASC allocation. The FF-CASC algorithm is more organized, because it always does slots allocation with the FirstFit policy, forming a big block of occupied slots at the beginning of the spectrum, and pushing free slots to the end of the spectrum. Intra-Area also allocates with FirstFit policy, but inside the prioritized areas. Thus, it has a medium degree of fragmentation, as the spectrum is segmented into allocation areas, which makes it difficult to form larger blocks of free slots.

<span id="page-12-1"></span>In the evaluated scenario, the FF-CASC algorithm achieves the best performance, with the lower blocking ratio and bandwidth blocking ratio. The Intra-Area achieves the worst blocking ratio performance, and the RF-CASC achieves the worst bandwidth blocking ratio performance. The FirstFit policy provides the best performance for FF-CASC, due to the higher spectral organization, which allows more circuit allocations. On the other hand, RF-CASC randomly allocates cores and slots through *Random Fit* policy, which reduces the availability of larger channels for higher bandwidths circuits. In the case of Intra-Area, it breaks the spectrum in prioritized allocation areas. Both algorithms form small free slot blocks and make harder the establishment of new circuits.

The use of RMSCA solution that creates priority areas does not perform well in scenarios with high variation in circuits bandwidth size. Thus, the RMSCA selection depends on the traffic profile, and the best solution for one scenario may result in poor performance when applied with another traffic profile. The crosstalk impairment also has a major impact on resource allocation, as XT-aware RMSCA solutions increases the fragmentation of network resources, leading to the dispersion of free

![](_page_12_Figure_12.jpeg)

<span id="page-12-2"></span>**Fig. 17.** SDM related papers classification.

**Table 6** SDM related papers classification.

<span id="page-13-1"></span>

| Type (Fig. 17)       | References                                                                                            |
|----------------------|-------------------------------------------------------------------------------------------------------|
| TDM                  | [35,54]                                                                                               |
| grooming             | [17,78,90]                                                                                            |
| core continuity      | [40,66,79,80,91]                                                                                      |
| core switching       | [7,16,18,31,33,38,43–45,54,61,62,64,71,74,76–79,81,82]                                                |
| non-uniform traffic  | [17,38,52]                                                                                            |
| dynamic traffic      | [17,22,27,31,33,34,38,40,41,44,45,48,51,58,61,62,64,69,72,74,76–79,82,90]                             |
| static traffic       | [23,47,50,53,54,56,71,75,81,92]                                                                       |
| physical impairments | [23]                                                                                                  |
| static n             | [9,19,22,27,31,34,38,40,43,53,57,58,60,62,66,70,81,82,90]                                             |
| dynamic n            | [40,41,54]                                                                                            |
| xt-aware             | [9,23,27,33,34,38,40,41,43,52–54,56,58,62,64,77,81,82]                                                |
| protection           | [34,44,60,65,72,78,80,90]                                                                             |
| slot priority        | [39]                                                                                                  |
| ia techniques        | [66,76]                                                                                               |
| core priority        | [61,63,77,81]                                                                                         |
| single modulation    | [17,43,47,52,58,60,62,64,66,76,78,80]                                                                 |
| multiple modulation  | [7,9,16,39,51,63,65,67,69,71,72,91,93]                                                                |
|                      | [22,23,27,38,40,54,61,71,75,79,81,92]                                                                 |
| defragmentation      | [87,88] [? ] [86]                                                                                     |
| 19 cores             | [19,22,23,41,49,54,62,71,93]                                                                          |
| 12 cores             | [22,40,56,57,62,71,79,93]                                                                             |
| 8 cores              | [51]                                                                                                  |
| 7 cores              | [9,15,17,19,21,22,26,27,31,33,34,38–41,43–46,48,53,54] [56,58,60–67,70,71,73,74,76–78,81,82,90,91,93] |
| 3 cores              | [40,50,53,56,74,81]                                                                                   |
| fiber parameters     | [9,12,14,19–21,25–27,31,32,40,43,46,49,50,53,54,57,60,66,70,73,77,81,82,88]                           |
| SCF bundle           | [92,94]                                                                                               |
| experimental network | [15]                                                                                                  |

slots within the spectrum. A study can be developed to better understand the behavior of crosstalk and RMSCA solutions in different scenarios, with variations of traffic profile and fiber parameters (such as bending radius and propagation constant).

# <span id="page-13-0"></span>**6. Conclusions and challenges**

The use of multi-core fibers guarantees higher resource availability because each core of MCF is equivalent to a single-core fiber of the standard EON. Regarding the papers found in the literature of SDM-EON, [Fig. 17](#page-12-2) presents a characterization of them.

There are a variety of traffic scenarios, equipment, fiber types and RMSCA solutions. [Table 6](#page-13-1) presents the distribution of some references according to the characteristics presented in [Fig. 17.](#page-12-2)

Thus, we can conclude that most of the papers use dynamic traffic configuration. Besides, there are several spectrum and core allocation solution proposals. However, the solutions are compared to classic algorithms, which are not crosstalk-aware. There are no comparisons between the new proposals. Furthermore, the *crosstalk* is a significant problem in the SDM-EON scenario because employing information of the physical-layer approximates the model performance to real scenarios of data transmission. Few papers consider survivability (8 papers) and traffic grooming (3 papers).

The evaluation presented in the literature around the SDM-EON theme allows the recognition of some challenges, which are open research questions. Below, some challenges are listed:

- The development of suitable equipment to switch the optical circuit in the SDM-EON. Papers found in the literature refer to hypothetical architectures, capable of switching the signal between different cores (in some cases). The performed evaluations of viable architectures [\[12](#page-14-7)[,18\]](#page-14-13) cite as a solution the adoption of devices (switches, amplifiers, and multiplexers) found in other types of networks.
- A challenge found in SDM-EON is the mitigation of the *crosstalk* effect. This interference of the physical layer is responsible for the unavailability of spectral resources, which are idle when crosstalk is high enough (XT above − 25 dB [\[12\]](#page-14-7)), and turns inadequate the circuit allocation. Some types of fiber are proposed to reduce the

crosstalk effect (such as Trench-Assisted MCF), regarding a distance threshold defined by the manufacturer.

- The production of equipment with a low financial cost, leading to low cost for SDM-EON implementation. Besides, the performance achieved by a *n* core MCF should be similar to the performance obtained by *n* coupled single-core fibers, which reinforces the development of fibers with higher immunity to crosstalk interference.
- We demonstrate in this paper that the value of *n* in crosstalk equation can be used statically or dynamically, and also can analyze the crosstalk impact from the new circuit to already established circuits. These different scenarios provide a high impact on the network blocking ratio, resulting in blocking differences up to 74*.*13*%*. In-depth investigation in the impact of different crosstalk scenarios can also be done in the future, to outline the scenario closest to the crosstalk occurrence in a real network.
- The elaboration of high efficiency (RMSCA) solution is also necessary. Nowadays, the papers found in the literature that propose RMSCA solutions compare their performance with classical literature algorithms such as the Dijkstra algorithm for routing and the First Fit strategy for spectrum allocation. There are no comparisons between the main proposed RMSCA solutions. Besides, different traffic profiles should be considered as some RMSCA solutions get better performance in specific traffic configurations.

In SDM-EON literature, some scenarios are predominant, such as dynamic configuration for request generation, 7-core fibers, consideration of *crosstalk*, and multiple levels of modulation for the signal. There are also many improvement opportunities, which will be explored as future works, such as the comparison between already proposed slot and core allocation techniques, the application of other physical layer effects besides *crosstalk*, and the proposition of impairment-aware allocation algorithms.

### **Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### **Acknowledgments**

We would like to thank the Coordination for the Improvement of Higher Education Personnel (CAPES), for funding the research developed.

### <span id="page-14-0"></span>**References**

- [1] M. Jinno, H. Takara, B. Kozicki, Y. Tsukishima, Y. Sone, S. Matsuoka, Spectrum-efficient and scalable elastic optical path network: architecture, benefits, and enabling technologies, IEEE Commun. Mag. 47 (11) (2009) 66–73, [https://](https://doi.org/10.1109/MCOM.2009.5307468) [doi.org/10.1109/MCOM.2009.5307468.](https://doi.org/10.1109/MCOM.2009.5307468)
- [2] R. Zhu, S. Li, P. Wang, Y. Tan, J. Yuan, Gradual migration of co-existing fixed/flexible optical networks for cloud-fog computing, IEEE Access 8 (2020) 50637–50647, [https://doi.org/10.1109/ACCESS.2020.2979895.](https://doi.org/10.1109/ACCESS.2020.2979895)
- [3] J. Yuan, R. Zhu, Y. Zhao, Q. Zhang, X. Li, D. Zhang, A. Samuel, A spectrum assignment algorithm in elastic optical network with minimum sum of weighted [resource reductions in all associated paths, J. Lightwave Technol. 37 \(21\) \(2019\)](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref3) 5583–5592.
- [4] R. Zhu, S. Li, P. Wang, J. Yuan, Time and spectrum fragmentation-aware virtual optical network embedding in elastic optical networks, Opt. Fiber Technol. 54 (2020) 102117, [https://doi.org/10.1016/j.yofte.2019.102117.](https://doi.org/10.1016/j.yofte.2019.102117)
- [5] J. Yuan, Y. Fu, R. Zhu, X. Li, Q. Zhang, J. Zhang, A. Samuel, A constrained-lower-indexed-block spectrum assignment policy in elastic optical networks, Opt. Switch. Netw. 33 (2019) 25–33, [https://doi.org/10.1016/j.osn.](https://doi.org/10.1016/j.osn.2019.03.001) [2019.03.001.](https://doi.org/10.1016/j.osn.2019.03.001)
- <span id="page-14-1"></span>[6] B.C. Chatterjee, N. Sarma, E. Oki, IEEE Commun. Surv. Tutor. 17 (3) (2015) 1776–1800, [https://doi.org/10.1109/COMST.2015.2431731.](https://doi.org/10.1109/COMST.2015.2431731)
- [7] K. Walkowiak, M. Klinkowski, P. Lechowicz, Dynamic routing in spectrally spatially flexible optical networks with back-to-back regeneration, IEEE/OSA J. Opt. Commun. Network. 10 (5) (2018) 523–534, [https://doi.org/10.1364/JOCN.](https://doi.org/10.1364/JOCN.10.000523) [10.000523.](https://doi.org/10.1364/JOCN.10.000523)
- <span id="page-14-3"></span>[8] H. Tode, Y. Hirota, Routing, spectrum and core assignment for space division multiplexing elastic optical networks, in: 2014 16th International Telecommunications Network Strategy and Planning Symposium (Networks), 2014, pp. 1–7, [https://doi.org/10.1109/NETWKS.2014.6958538.](https://doi.org/10.1109/NETWKS.2014.6958538)
- [9] A. Muhammad, G. Zervas, R. Forchheimer, Resource allocation for space-division multiplexing: optical white box versus optical black box networking, J. Lightwave Technol. 33 (23) (2015) 4928–4941, [https://doi.org/10.1109/JLT.2015.2493123.](https://doi.org/10.1109/JLT.2015.2493123)
- [10] L.R. Costa, A.C. Drummond, New distance-adaptive modulation scheme for elastic optical networks, IEEE Commun. Lett. 21 (2) (2017) 282–285, [https://doi.org/10.](https://doi.org/10.1109/LCOMM.2016.2624288) [1109/LCOMM.2016.2624288.](https://doi.org/10.1109/LCOMM.2016.2624288)
- <span id="page-14-6"></span>[11] [H. Beyranvand, J.A. Salehi, A quality-of-transmission aware dynamic routing and](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref11) spectrum assignment scheme for future elastic optical networks, J. Lightwave Technol. 31 (18) (2013) 3043–3054.
- <span id="page-14-7"></span>[12] [D. Richardson, J. Fini, L. Nelson, Space-division multiplexing in optical fibres, Nat.](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref12) Photon. 7 (5) (2013) 354–362.
- <span id="page-14-8"></span>[13] G. Rademacher, R.S. Lus, B.J. Puttnam, Y. Awaji, N. Wada, Crosstalk dynamics in multi-core fibers, Optic Express 25 (10) (2017) 12020–12028, [https://doi.org/10.](https://doi.org/10.1364/OE.25.012020) [1364/OE.25.012020,](https://doi.org/10.1364/OE.25.012020) [http://www.opticsexpress.org/abstract.cfm?URIoe-25-10-](http://www.opticsexpress.org/abstract.cfm?URIoe-25-10-12020) [12020.](http://www.opticsexpress.org/abstract.cfm?URIoe-25-10-12020)
- <span id="page-14-9"></span>[14] [J.M. Fini, B. Zhu, T.F. Taunay, M.F. Yan, K.S. Abedin, Crosstalk in multi-core](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref14) optical fibres, in: 2011 37th European Conference and Exhibition on Optical Communication, 2011, pp. 1–3.
- <span id="page-14-10"></span>[15] N. Amaya, M. Irfan, G. Zervas, R. Nejabati, D. Simeonidou, J. Sakaguchi, W. Klaus, B. Puttnam, T. Miyazawa, Y. Awaji, N. Wada, I. Henning, Fully-elastic multi-granular network with space/frequency/time switching using multi-core fibres and programmable optical nodes, Optic Express 21 (7) (2013) 8865–8872, [https://doi.org/10.1364/OE.21.008865,](https://doi.org/10.1364/OE.21.008865) [http://www.opticsexpress.org/abstract.](http://www.opticsexpress.org/abstract.cfm?URIoe-21-7-8865) [cfm?URIoe-21-7-8865.](http://www.opticsexpress.org/abstract.cfm?URIoe-21-7-8865)
- <span id="page-14-11"></span>[16] P.S. Khodashenas, J.M. Rivas-Moscoso, D. Siracusa, F. Pederzolli, B. Shariati, D. Klonidis, E. Salvadori, I. Tomkos, Comparison of spectral and spatial super-channel allocation schemes for sdm networks, J. Lightwave Technol. 34 (11) (2016) 2710–2716, [https://doi.org/10.1109/JLT.2016.2551299.](https://doi.org/10.1109/JLT.2016.2551299)
- [17] R. Tian, Y. Zhao, J. Zhang, X. Yu, Y. Li, C. Yu, J. Zhang, C. Liu, G. Zhang, Dynamic traffic grooming based on auxiliary graph in spatial division multiplexing enabled elastic optical networks, in: 2016 15th International Conference on Optical Communications and Networks (ICOCN), 2016, pp. 1–3, [https://doi.org/10.1109/](https://doi.org/10.1109/ICOCN.2016.7875878) [ICOCN.2016.7875878.](https://doi.org/10.1109/ICOCN.2016.7875878)
- <span id="page-14-13"></span>[18] D.M. Marom, P.D. Colbourne, A. DErrico, N.K. Fontaine, Y. Ikuma, R. Proietti, L. Zong, J.M. Rivas-Moscoso, I. Tomkos, Survey of photonic switching architectures and technologies in support of spatially and spectrally flexible optical networking [invited], IEEE/OSA J. Opt. Commun. Network. 9 (1) (2017) 1–26, [https://doi.](https://doi.org/10.1364/JOCN.9.000001) [org/10.1364/JOCN.9.000001.](https://doi.org/10.1364/JOCN.9.000001)
- <span id="page-14-14"></span>[19] G.M. Saridis, D. Alexandropoulos, G. Zervas, D. Simeonidou, Survey and evaluation of space division multiplexing: from technologies to optical networks, IEEE Commun. Surv. Tutor. 17 (4) (2015) 2136–2156, [https://doi.org/10.1109/](https://doi.org/10.1109/COMST.2015.2466458) [COMST.2015.2466458.](https://doi.org/10.1109/COMST.2015.2466458)
- <span id="page-14-15"></span>[20] K. Takenaga, Y. Arakawa, Y. Sasaki, S. Tanigawa, S. Matsuo, K. Saitoh, M. Koshiba, A large effective area multi-core fiber with an optimized cladding thickness, Optic Express 19 (26) (2011) B543–B550, [https://doi.org/10.1364/OE.](https://doi.org/10.1364/OE.19.00B543) [19.00B543,](https://doi.org/10.1364/OE.19.00B543) [http://www.opticsexpress.org/abstract.cfm?URIoe-19-26-B543.](http://www.opticsexpress.org/abstract.cfm?URIoe-19-26-B543)

- <span id="page-14-16"></span>[21] K. Takenaga, Y. Arakawa, S. Tanigawa, N. Guan, S. Matsuo, K. Saitoh, M. Koshiba, Reduction of crosstalk by trench-assisted multi-core fiber, in: 2011 Optical Fiber [Communication Conference and Exposition and the National Fiber Optic Engineers](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref21) Conference, 2011, pp. 1–3.
- <span id="page-14-17"></span>[22] S. Fujii, Y. Hirota, H. Tode, K. Murakami, On-demand spectrum and core allocation for reducing crosstalk in multicore fibers in elastic optical networks, IEEE/OSA J. Opt. Commun. Network. 6 (12) (2014) 1059–1071, [https://doi.org/](https://doi.org/10.1109/JOCN.2014.6985898) [10.1109/JOCN.2014.6985898.](https://doi.org/10.1109/JOCN.2014.6985898)
- <span id="page-14-18"></span>[23] G. Savva, G. Ellinas, B. Shariati, I. Tomkos, Physical layer-aware routing, spectrum, and core allocation in spectrally-spatially flexible optical networks with multicore fibers, in: 2018 IEEE International Conference on Communications (ICC), 2018, pp. 1–6, [https://doi.org/10.1109/ICC.2018.8422782.](https://doi.org/10.1109/ICC.2018.8422782)
- <span id="page-14-20"></span><span id="page-14-19"></span>[24] [J.A. Jay, An Overview of Macrobending and Microbending of Optical Fibers,](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref24) White paper of Corning, 2010, pp. 1–21.
- [25] T. Hayashi, T. Taru, O. Shimakawa, T. Sasaki, E. Sasaoka, Characterization of crosstalk in ultra-low-crosstalk multi-core fiber, J. Lightwave Technol. 30 (4) (2012) 583–589, [https://doi.org/10.1109/JLT.2011.2177810.](https://doi.org/10.1109/JLT.2011.2177810)
- <span id="page-14-21"></span>[26] T. Hayashi, T. Taru, O. Shimakawa, T. Sasaki, E. Sasaoka, Uncoupled multi-core fiber enhancing signal-to-noise ratio, Optic Express 20 (26) (2012) B94–B103, [https://doi.org/10.1364/OE.20.000B94,](https://doi.org/10.1364/OE.20.000B94) [http://www.opticsexpress.org/abstract.](http://www.opticsexpress.org/abstract.cfm?URIoe-20-26-B94) [cfm?URIoe-20-26-B94.](http://www.opticsexpress.org/abstract.cfm?URIoe-20-26-B94)
- <span id="page-14-22"></span>[27] M. Klinkowski, P. Lechowicz, K. Walkowiak, A study on the impact of inter-core crosstalk on SDM network performance, in: 2018 International Conference on Computing, Networking and Communications, ICNC 2018, 2018, pp. 404–408, [https://doi.org/10.1109/ICCNC.2018.8390393.](https://doi.org/10.1109/ICCNC.2018.8390393)
- <span id="page-14-23"></span>[28] P.J. Winzer, D.T. Neilson, From scaling disparities to integrated parallelism: a decathlon for a decade, J. Lightwave Technol. 35 (5) (2017) 1099–1115, [https://](https://doi.org/10.1109/JLT.2017.2662082) [doi.org/10.1109/JLT.2017.2662082.](https://doi.org/10.1109/JLT.2017.2662082)
- <span id="page-14-24"></span><span id="page-14-2"></span>[29] M. Yang, Q. Wu, K. Guo, Y. Zhang, Evaluation of device cost, power consumption, and network performance in spatially and spectrally flexible sdm optical networks, J. Lightwave Technol. 37 (20) (2019) 5259–5272, [https://doi.org/10.1109/JLT.](https://doi.org/10.1109/JLT.2019.2931143) [2019.2931143.](https://doi.org/10.1109/JLT.2019.2931143)
- <span id="page-14-25"></span>[30] N.K. Fontaine, Photonic lantern spatial multiplexers in space-division multiplexing, in: 2013 IEEE Photonics Society Summer Topical Meeting Series, 2013, pp. 97–98, [https://doi.org/10.1109/PHOSST.2013.6614504.](https://doi.org/10.1109/PHOSST.2013.6614504)
- <span id="page-14-26"></span>[31] R. Zhu, Y. Zhao, H. Yang, H. Chen, J. Zhang, J.P. Jue, Crosstalk-aware rcsa for spatial division multiplexing enabled elastic optical networks with multi-core fibers, Chin. Optic Lett. 14 (10) (2016) 100604. [http://col.osa.org/abstract.cfm?](http://col.osa.org/abstract.cfm?URIcol-14-10-100604) [URIcol-14-10-100604.](http://col.osa.org/abstract.cfm?URIcol-14-10-100604)
- <span id="page-14-27"></span><span id="page-14-4"></span>[32] M. Koshiba, K. Saitoh, K. Takenaga, S. Matsuo, Multi-core fiber design and analysis: coupled-mode theory and coupled-power theory, Optic Express 19 (26) (2011) B102, [https://doi.org/10.1364/oe.19.00b102.](https://doi.org/10.1364/oe.19.00b102)
- <span id="page-14-28"></span><span id="page-14-5"></span>[33] K. Hashino, Y. Hirota, Y. Tanigawa, H. Tode, A Strict and Less Computational Crosstalk-Aware Spectrum and Core Allocation Method with Crosstalk-Prohibited Frequency Slots in SDM-EONs, 2018 Photonics in Switching and Computing (PSC), 2019, pp. 1–3, [https://doi.org/10.1109/ps.2018.8751434.](https://doi.org/10.1109/ps.2018.8751434)
- <span id="page-14-29"></span>[34] Y. Tan, R. Zhu, H. Yang, Y. Zhao, J. Zhang, Z. Liu, Q. Qu, Z. Zhou, Crosstalk-aware provisioning strategy with dedicated path protection for elastic multi-core fiber networks, in: 2016 15th International Conference on Optical Communications and Networks (ICOCN), 2016, pp. 1–3, [https://doi.org/10.1109/ICOCN.2016.](https://doi.org/10.1109/ICOCN.2016.7875849) [7875849.](https://doi.org/10.1109/ICOCN.2016.7875849)
- <span id="page-14-30"></span>[35] R. Proietti, L. Liu, R.P. Scott, B. Guan, C. Qin, T. Su, F. Giannone, S.J.B. Yoo, 3d elastic optical networking in the temporal, spectral, and spatial domains, IEEE Commun. Mag. 53 (2) (2015) 79–87, [https://doi.org/10.1109/MCOM.2015.](https://doi.org/10.1109/MCOM.2015.7045394) [7045394.](https://doi.org/10.1109/MCOM.2015.7045394)
- <span id="page-14-31"></span>[36] C. T. Politi, V. Anagnostopoulos, C. Matrakidis, A. Stavdas, A. Lord, V. Lpez, J. Fernndez-Palacios, Dynamic Operation of Flexi-Grid Ofdm-Based Networks doi:10.1364/OFC.2012.OTh3B.2.
- <span id="page-14-32"></span>[37] L.R. Costa, L.S. de Sousa, F.R. de Oliveira, K.A. da Silva, P.J.S. Jnior, A.C. Drummond, ONS: simulador de Eventos Discretos para Redes pticas WDM/EON, in: SBRC 2016 - Salao de Ferramentas, 2016, [http://sbrc2016.ufba.br/downloads/](http://sbrc2016.ufba.br/downloads/Salao_Ferramentas/154765.pdf) [Salao\\_Ferramentas/154765.pdf.](http://sbrc2016.ufba.br/downloads/Salao_Ferramentas/154765.pdf)
- <span id="page-14-33"></span>[38] K. Walkowiak, A. Wlodarczyk, M. Klinkowski, Effective Worst-Case Crosstalk Estimation for Dynamic Translucent SDM Elastic Optical Networks, 2019, pp. 1–7, [https://doi.org/10.1109/icc.2019.8761568.](https://doi.org/10.1109/icc.2019.8761568)
- <span id="page-14-34"></span><span id="page-14-12"></span>[39] H. Tode, Y. Hirota, Routing, spectrum, and core and/or mode assignment on space-division multiplexing optical networks [invited], IEEE/OSA J. Opt. Commun. Network. 9 (1) (2017) A99–A113, [https://doi.org/10.1364/JOCN.9.000A99.](https://doi.org/10.1364/JOCN.9.000A99)
- <span id="page-14-35"></span>[40] M. Klinkowski, G. Zalewski, Dynamic crosstalk-Aware lightpath provisioning in spectrally-spatially flexible optical networks, J. Opt. Commun. Netw. 11 (5) (2019) 213–225, [https://doi.org/10.1364/JOCN.11.000213.](https://doi.org/10.1364/JOCN.11.000213)
- <span id="page-14-36"></span>[41] K. Hashino, Y. Hirota, Y. Tanigawa, H. Tode, Crosstalk-aware spectrum and core allocation with crosstalk-prohibited frequency slot in space-division multiplexing elastic optical networks, in: Advanced Photonics 2017 (IPR, NOMA, Sensors, Networks, SPPCom, PS), Optical Society of America, 201[7https://doi.org/10.](https://doi.org/10.1364/PS.2017.PM3D.2) [1364/PS.2017.PM3D.2,](https://doi.org/10.1364/PS.2017.PM3D.2) p. PM3D.2 [http://www.osapublishing.org/abstract.cfm?](http://www.osapublishing.org/abstract.cfm?URIPS-2017-PM3D.2) [URIPS-2017-PM3D.2.](http://www.osapublishing.org/abstract.cfm?URIPS-2017-PM3D.2)
- <span id="page-14-37"></span>[42] R. Zhu, Y. Zhao, H. Yang, H. Chen, J. Zhang, J.P. Jue, Crosstalk-aware rcsa for spatial division multiplexing enabled elastic optical networks with multi-core fibers, Chin. Optic Lett. 14 (10) (2016) 100604. [http://col.osa.org/abstract.cfm?](http://col.osa.org/abstract.cfm?URIcol-14-10-100604) [URIcol-14-10-100604.](http://col.osa.org/abstract.cfm?URIcol-14-10-100604)
- <span id="page-14-38"></span>[43] Y. Zhao, J. Zhang, Crosstalk-aware cross-core virtual concatenation in spatial division multiplexing elastic optical networks, Electron. Lett. 52 (20) (2016) 1701–1703, [https://doi.org/10.1049/el.2016.2132.](https://doi.org/10.1049/el.2016.2132)

- <span id="page-15-0"></span>[44] H.M.N.S. Oliveira, N.L.S. da Fonseca, Algorithm for shared path for protection of space division multiplexing elastic optical networks, in: 2017 IEEE International Conference on Communications (ICC), 2017, pp. 1–6, [https://doi.org/10.1109/](https://doi.org/10.1109/ICC.2017.7997378) [ICC.2017.7997378.](https://doi.org/10.1109/ICC.2017.7997378)
- <span id="page-15-1"></span>[45] H.M.N. da Silva Oliveira, N.L.S. da Fonseca, The minimum interference p-cycle algorithm for protection of space division multiplexing elastic optical networks, IEEE Latin Am. Trans. 15 (7) (2017) 1342–1348, [https://doi.org/10.1109/TLA.](https://doi.org/10.1109/TLA.2017.7959516) [2017.7959516.](https://doi.org/10.1109/TLA.2017.7959516)
- <span id="page-15-2"></span>[46] K. Imamura, K. Mukasa, T. Yagi, Investigation on multi-core fibers with large aeff and low micro bending loss, in: 2010 Conference on Optical Fiber Communication (OFC/NFOEC), Collocated National Fiber Optic Engineers Conference, 2010, pp. 1–3, [https://doi.org/10.1364/OFC.2010.OWK6.](https://doi.org/10.1364/OFC.2010.OWK6)
- [47] L. Zhang, N. Ansari, A. Khreishah, Anycast planning in space division multiplexing elastic optical networks with multi-core fibers, IEEE Commun. Lett. 20 (10) (2016) 1983–1986, [https://doi.org/10.1109/LCOMM.2016.2593479.](https://doi.org/10.1109/LCOMM.2016.2593479)
- [48] R. Zhu, Yongli Zhao, Hui Yang, X. Yu, Yuanlong Tan, Jie Zhang, N. Wang, J.P. Jue, Multi-dimensional resource assignment in spatial division multiplexing enabled elastic optical networks with multi-core fibers, in: 2016 15th International Conference on Optical Communications and Networks (ICOCN), 2016, pp. 1–3, [https://doi.org/10.1109/ICOCN.2016.7875672.](https://doi.org/10.1109/ICOCN.2016.7875672)
- [49] K. Imamura, H. Inaba, K. Mukasa, R. Sugizaki, 19-core multi core fiber to realize high density space division multiplexing transmission, in: 2012 IEEE Photonics Society Summer Topical Meeting Series, 2012, pp. 208–209, [https://doi.org/10.](https://doi.org/10.1109/PHOSST.2012.6280776) [1109/PHOSST.2012.6280776.](https://doi.org/10.1109/PHOSST.2012.6280776)
- <span id="page-15-6"></span>[50] [A. Muhammad, G. Zervas, D. Simeonidou, R. Forchheimer, Routing, spectrum and](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref50) core allocation in flexgrid sdm networks with multi-core fibers, in: 2014 International Conference on Optical Network Design and Modeling, 2014, pp. 192–197.
- <span id="page-15-7"></span>[51] S. Sugihara, Y. Hirota, S. Fujii, H. Tode, T. Watanabe, Dynamic resource allocation for immediate and advance reservation in space-division-multiplexing-based elastic optical networks, IEEE/OSA J. Opt. Commun. Network. 9 (3) (2017) 183–197, [https://doi.org/10.1364/JOCN.9.000183.](https://doi.org/10.1364/JOCN.9.000183)
- [52] Y. Cao, Y. Zhao, X. Yu, Q. Ou, Z. Liu, X. Liao, J. Zhang, Mode conversion-based crosstalk-aware routing, spectrum and mode assignment in space-division multiplexing elastic optical networks, in: 2017 16th International Conference on Optical Communications and Networks (ICOCN), 2017, pp. 1–3, [https://doi.org/](https://doi.org/10.1109/ICOCN.2017.8121478) [10.1109/ICOCN.2017.8121478.](https://doi.org/10.1109/ICOCN.2017.8121478)
- <span id="page-15-9"></span>[53] M. Yang, Y. Zhang, Q. Wu, Routing, spectrum, and core assignment in sdm-eons with mcf: node-arc ilp/milp methods and an efficient xt-aware heuristic algorithm, IEEE/OSA J. Opt. Commun. Network. 10 (3) (2018) 195–208, [https://doi.org/10.](https://doi.org/10.1364/JOCN.10.000195) [1364/JOCN.10.000195.](https://doi.org/10.1364/JOCN.10.000195)
- <span id="page-15-10"></span>[54] [F. Tang, Y. Li, G. Shen, G. Rouskas, Minimizing inter-core crosstalk jointly in](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref54) spatial, frequency, and time domains for scheduled lightpath demands in multi-core fiber-based elastic optical network, J. Lightwave Technol. (2020) 11.
- [55] H.M.N.S. Oliveira, N.L.S. da Fonseca, Algorithm for protection of space division multiplexing elastic optical networks, in: 2016 IEEE Global Communications Conference (GLOBECOM), 2016, pp. 1–6, [https://doi.org/10.1109/GLOCOM.](https://doi.org/10.1109/GLOCOM.2016.7841575) [2016.7841575.](https://doi.org/10.1109/GLOCOM.2016.7841575)
- <span id="page-15-12"></span>[56] J. Zhu, Z. Zhu, Physical-layer security in mcf-based sdm-eons: would crosstalk-aware service provisioning be good enough? J. Lightwave Technol. 35 (22) (2017) 4826–4837, [https://doi.org/10.1109/JLT.2017.2757956.](https://doi.org/10.1109/JLT.2017.2757956)
- [57] D. Kumar, R. Ranjan, Optimal design for crosstalk analysis in 12-core 5-lp mode homogeneous multicore fiber for different lattice structure, Opt. Fiber Technol. 41 (2018) 95–103, [https://doi.org/10.1016/j.yofte.2018.01.002.](https://doi.org/10.1016/j.yofte.2018.01.002)
- [58] Y. Zhao, L. Hu, R. Zhu, X. Yu, X. Wang, J. Zhang, Crosstalk-aware spectrum defragmentation based on spectrum compactness in space division multiplexing enabled elastic optical networks with multicore fiber, IEEE Access 6 (2018) 15346–15355, [https://doi.org/10.1109/ACCESS.2018.2795102.](https://doi.org/10.1109/ACCESS.2018.2795102)
- [59] [M. Cantono, V. Curri, Coupled vs. uncoupled sdm solutions: a physical layer aware](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref59) networking comparison, in: 2018 20th International Conference on Transparent Optical Networks (ICTON), 2018, pp. 1–4.
- [60] H.M.N.S. Oliveira, N.L.S. da Fonseca, Sharing spectrum and straddling p-cycle fipp for protection against two simultaneous failures in sdm elastic optical networks, in: 2017 IEEE 9th Latin-American Conference on Communications (LATINCOM), 2017, pp. 1–6, [https://doi.org/10.1109/LATINCOM.2017.8240175.](https://doi.org/10.1109/LATINCOM.2017.8240175)
- [61] S. Trindade, N.L.S. da Fonseca, Proactive fragmentation-aware routing, modulation Format, core, and spectrum allocation in EON-SDM, in: ICC 2019 - 2019 IEEE International Conference on Communications (ICC), 2019, pp. 1–6, [https://doi.org/10.1109/icc.2019.8762005.](https://doi.org/10.1109/icc.2019.8762005)
- [62] Y. Zhao, L. Hu, C. Wang, R. Zhu, X. Yu, J. Zhang, Multi-core virtual concatenation scheme considering inter-core crosstalk in spatial division multiplexing enabled elastic optical networks, China Commun. 14 (10) (2017) 108–117, [https://doi.](https://doi.org/10.1109/CC.2017.8107636) [org/10.1109/CC.2017.8107636.](https://doi.org/10.1109/CC.2017.8107636)
- <span id="page-15-19"></span>[63] S. Fujii, Y. Hirota, H. Tode, Dynamic resource allocation with virtual grid for space division multiplexed elastic optical network, in: 39th European Conference and Exhibition on Optical Communication (ECOC 2013), 2013, pp. 1–3, [https://doi.](https://doi.org/10.1049/cp.2013.1653) [org/10.1049/cp.2013.1653.](https://doi.org/10.1049/cp.2013.1653)
- <span id="page-15-20"></span>[64] K. Kubota, Y. Tanigawa, H. Tode, Y. Hirota, Spectrum allocation considering crosstalk impacts at both fibers and nodes in space-division multiplexing elastic [optical networks, in: 2019 24th OptoElectronics and Communications Conference](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref64) (OECC) and 2019 International Conference on Photonics in Switching and Computing (PSC), 2019, pp. 1–3.
- <span id="page-15-22"></span><span id="page-15-21"></span>[65] H.M.N.S. Oliveira, N.L.S. da Fonseca, Routing, spectrum, core and modulation level assignment algorithm for protected sdm optical networks, in: GLOBECOM 2017 - 2017 IEEE Global Communications Conference, 2017, pp. 1–6, [https://doi.](https://doi.org/10.1109/GLOCOM.2017.8254039) [org/10.1109/GLOCOM.2017.8254039.](https://doi.org/10.1109/GLOCOM.2017.8254039)

- [66] Q. Yao, H. Yang, R. Zhu, A. Yu, W. Bai, Y. Tan, J. Zhang, H. Xiao, Core, mode, and spectrum assignment based on machine learning in space division multiplexing elastic optical networks, IEEE Access 6 (2018) 15898–15907, [https://doi.org/10.](https://doi.org/10.1109/ACCESS.2018.2811724) [1109/ACCESS.2018.2811724.](https://doi.org/10.1109/ACCESS.2018.2811724)
- <span id="page-15-23"></span>[67] S. Fujii, Y. Hirota, H. Tode, T. Watanabe, On-demand routing and spectrum allocation for energy-efficient aod nodes in sdm-eons, IEEE/OSA J. Opt. Commun. Network. 9 (11) (2017) 960–973, [https://doi.org/10.1364/JOCN.9.000960.](https://doi.org/10.1364/JOCN.9.000960)
- <span id="page-15-24"></span>[68] K. Takenaga, S. Tanigawa, N. Guan, S. Matsuo, K. Saitoh, M. Koshiba, Reduction of crosstalk by quasi-homogeneous solid multi-core fiber, in: 2010 Conference on Optical Fiber Communication (OFC/NFOEC), Collocated National Fiber Optic Engineers Conference, 2010, pp. 1–3, [https://doi.org/10.1364/OFC.2010.OWK7.](https://doi.org/10.1364/OFC.2010.OWK7)
- <span id="page-15-25"></span>[69] S. Iyer, On the cost minimization in space division multiplexing based elastic optical networks, J. Opt. Commun..
- <span id="page-15-26"></span><span id="page-15-4"></span><span id="page-15-3"></span>[70] T. Hayashi, T. Taru, O. Shimakawa, T. Sasaki, E. Sasaoka, Design and fabrication of ultra-low crosstalk and low-loss multi-core fiber, Optic Express 19 (17) (2011) 16576–16592, [https://doi.org/10.1364/OE.19.016576,](https://doi.org/10.1364/OE.19.016576) [http://www.opticsexpress.](http://www.opticsexpress.org/abstract.cfm?URIoe-19-17-16576) [org/abstract.cfm?URIoe-19-17-16576.](http://www.opticsexpress.org/abstract.cfm?URIoe-19-17-16576)
- <span id="page-15-27"></span>[71] M. Yaghubi-Namaad, A.G. Rahbar, B. Alizadeh, Adaptive modulation and flexible resource allocation in space-division- multiplexed elastic optical networks, IEEE/OSA J. Opt. Commun. Network. 10 (3) (2018) 240–251, [https://doi.org/10.](https://doi.org/10.1364/JOCN.10.000240) [1364/JOCN.10.000240.](https://doi.org/10.1364/JOCN.10.000240)
- <span id="page-15-28"></span><span id="page-15-5"></span>[72] H.M.N.S. Oliveira, N.L.S. Da Fonseca, Protection, routing, modulation, core, and spectrum allocation in sdm elastic optical networks, IEEE Commun. Lett. 22 (9) (2018) 1806–1809, [https://doi.org/10.1109/LCOMM.2018.2850346.](https://doi.org/10.1109/LCOMM.2018.2850346)
- <span id="page-15-29"></span>[73] K. Takenaga, Y. Arakawa, S. Tanigawa, N. Guan, S. Matsuo, K. Saitoh, M. Koshiba, An investigation on crosstalk in multi-core fibers by introducing random fluctuation along longitudinal direction, E94.B, IEICE Trans. Commun. (2) (2011) 409–416, [https://doi.org/10.1587/transcom.E94.B.409.](https://doi.org/10.1587/transcom.E94.B.409)
- <span id="page-15-30"></span>[74] S. Iyer, S.P. Singh, A novel protection strategy for elastic optical networks based on space division multiplexing, in: SPCOM 2018 - 12th International Conference on Signal Processing and Communications, 2018, pp. 41–45, [https://doi.org/10.](https://doi.org/10.1109/SPCOM.2018.8724423) [1109/SPCOM.2018.8724423.](https://doi.org/10.1109/SPCOM.2018.8724423)
- <span id="page-15-31"></span><span id="page-15-8"></span>[75] M. Klinkowski, G. Zalewski, K. Walkowiak, Optimization of spectrally and spatially flexible optical networks with spatial mode conversion, in: 2018 International Conference on Optical Network Design and Modeling (ONDM), 2018, pp. 148–153, [https://doi.org/10.23919/ONDM.2018.8396122.](https://doi.org/10.23919/ONDM.2018.8396122)
- <span id="page-15-32"></span>[76] Q. Yao, H. Yang, A. Yu, J. Zhang, Transductive transfer learning-based spectrum optimization for resource reservation in seven-core elastic optical networks, J. Lightwave Technol. 37 (16) (2019) 4164–4172, [https://doi.org/10.1109/jlt.2019.](https://doi.org/10.1109/jlt.2019.2902454) [2902454.](https://doi.org/10.1109/jlt.2019.2902454)
- <span id="page-15-33"></span>[77] Q. Zhu, L. Lv, L. Zhu, T. Wang, L. Gao, Y. Lei, B. Chen, Q. Zhang, Service-classified routing, core, and spectrum assignment in spatial division multiplexing elastic optical networks with multicore fiber, in: Asia Communications and Photonics Conference, ACP 2018-Octob, 2018, pp. 1–3, [https://doi.org/10.1109/ACP.2018.](https://doi.org/10.1109/ACP.2018.8596169) [8596169.](https://doi.org/10.1109/ACP.2018.8596169)
- <span id="page-15-34"></span><span id="page-15-11"></span>[78] H.M.N.S. Oliveira, N.L.S. da Fonseca, Protection, routing, spectrum and core allocation in EONs-SDM for efficient spectrum utilization, in: ICC 2019 - 2019 IEEE International Conference on Communications (ICC), 2019, pp. 1–6, [https://](https://doi.org/10.1109/icc.2019.8761380) [doi.org/10.1109/icc.2019.8761380.](https://doi.org/10.1109/icc.2019.8761380)
- <span id="page-15-35"></span><span id="page-15-13"></span>[79] P. Lechowicz, M. Tornatore, A. Wodarczyk, K. Walkowiak, Fragmentation metrics and fragmentation-aware algorithm for spectrally/spatially flexible optical networks, J. Opt. Commun. Netw. 12 (5) (2020) 133–145, [https://doi.org/10.](https://doi.org/10.1364/JOCN.382838) [1364/JOCN.382838,](https://doi.org/10.1364/JOCN.382838) [http://jocn.osa.org/abstract.cfm?URIjocn-12-5-133.](http://jocn.osa.org/abstract.cfm?URIjocn-12-5-133)
- <span id="page-15-36"></span><span id="page-15-14"></span>[80] H.M.N.S. Oliveira, N.L.S. da Fonseca, P-cycle protected multipath routing, spectrum and core allocation in SDM elastic optical networks, in: ICC 2019 - 2019 IEEE International Conference on Communications (ICC), 2019, pp. 1–6, [https://](https://doi.org/10.1109/icc.2019.8762098) [doi.org/10.1109/icc.2019.8762098.](https://doi.org/10.1109/icc.2019.8762098)
- <span id="page-15-37"></span><span id="page-15-15"></span>[81] E.E. Moghaddam, H. Beyranvand, J.A. Salehi, crosstalk-aware routing, modulation level, core and spectrum assignment, and scheduling in SDM-based elastic optical networks, in: 9th International Symposium on Telecommunication: with Emphasis on Information and Communication Technology, IST 2018, 2019, pp. 160–165, [https://doi.org/10.1109/ISTEL.2018.8661122.](https://doi.org/10.1109/ISTEL.2018.8661122)
- <span id="page-15-38"></span><span id="page-15-16"></span>[82] Y. Lei, B. Chen, M. Gao, L. Xiang, Q. Zhang, Dynamic routing, core, and spectrum assignment with minimized crosstalk in spatial division multiplexing elastic optical networks, in: Asia Communications and Photonics Conference, ACP 2018-Octob, 2018, pp. 1–3, [https://doi.org/10.1109/ACP.2018.8595895.](https://doi.org/10.1109/ACP.2018.8595895)
- <span id="page-15-39"></span><span id="page-15-17"></span>[83] R. Wang, B. Mukherjee, Spectrum management in heterogeneous bandwidth optical networks, Opt. Switch. Netw. 11 (2014) 83–91, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.osn.2013.09.003) [osn.2013.09.003.](https://doi.org/10.1016/j.osn.2013.09.003) Part A [http://www.sciencedirect.com/science/article/pii/](http://www.sciencedirect.com/science/article/pii/S1573427713000799) [S1573427713000799.](http://www.sciencedirect.com/science/article/pii/S1573427713000799)
- <span id="page-15-40"></span><span id="page-15-18"></span>[84] B.C. Chatterjee, S. Ba, E. Oki, Fragmentation problems and management approaches in elastic optical networks: a survey, IEEE Commun. Surv. Tutor. 20 (1) (2018) 183–210, [https://doi.org/10.1109/COMST.2017.2769102.](https://doi.org/10.1109/COMST.2017.2769102)
- <span id="page-15-41"></span>[85] A.K. Horota, G.B. Figueiredo, N.L.S. da Fonseca, Algoritmo de roteamento e atribuio de espectro com minimizao de fragmentao em redes pticas elsticas, [Simpsio Brasileiro de Redes de Computadores e Sistemas Distribudos 32 \(2014\)](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref85) 895–908.
- <span id="page-15-42"></span>[86] G. Meloni, F. Fresi, M. Imran, F. Paolucci, F. Cugini, A. D'Errico, L. Giorgi, T. Sasaki, P. Castoldi, L. Pot, Software-defined defragmentation in space-division multiplexing with quasi-hitless fast core switching, J. Lightwave Technol. 34 (8) (2016) 1956–1962, [https://doi.org/10.1109/JLT.2015.2503434.](https://doi.org/10.1109/JLT.2015.2503434)
- <span id="page-15-44"></span><span id="page-15-43"></span>[87] M. Imran, F. Paolucci, F. Cugini, A. D'Errico, L. Giorgi, T. Sasaki, P. Castoldi, L. Poti, Quasi-hitless software-defined defragmentation in space division multiplexing (sdm), in: 2015 European Conference on Optical Communication (ECOC), 2015, pp. 1–3, [https://doi.org/10.1109/ECOC.2015.7341673.](https://doi.org/10.1109/ECOC.2015.7341673)

- [88] Y. Zhao, L. Hu, R. Zhu, X. Yu, Y. Li, W. Wang, J. Zhang, Crosstalk-aware spectrum defragmentation by re-provisioning advance reservation requests in space division multiplexing enabled elastic optical networks with multi-core fiber, Optic Express 27 (4) (2019) 5014–5032, [https://doi.org/10.1364/OE.27.005014,](https://doi.org/10.1364/OE.27.005014) [http://www.](http://www.opticsexpress.org/abstract.cfm?URIoe-27-4-5014) [opticsexpress.org/abstract.cfm?URIoe-27-4-5014.](http://www.opticsexpress.org/abstract.cfm?URIoe-27-4-5014)
- [89] [E.W. Dijkstra, A note on two problems in connexion with graphs, Numer. Math. 1](http://refhub.elsevier.com/S1573-4277(20)30046-1/sref89) (1) (1959) 269–271.
- <span id="page-16-1"></span>[90] H.M. Oliveira, N.L. Da Fonseca, Spectrum overlap and traffic grooming in P-Cycle algorithm protected SDM optical networks, in: IEEE International Conference on Communications 2018-May, 2018, pp. 1–6, [https://doi.org/10.1109/ICC.2018.](https://doi.org/10.1109/ICC.2018.8422322) [8422322.](https://doi.org/10.1109/ICC.2018.8422322)
- <span id="page-16-3"></span><span id="page-16-2"></span>[91] H.M. Oliveira, N.L. da Fonseca, Routing, spectrum and core assignment algorithms for protection of space division multiplexing elastic optical networks, J. Netw. Comput. Appl. 128 (2019) 78–89, [https://doi.org/10.1016/j.jnca.2018.12.009.](https://doi.org/10.1016/j.jnca.2018.12.009)
- [92] P. Lechowicz, K. Walkowiak, M. Klinkowski, Greedy randomized adaptive search procedure for joint optimization of unicast and anycast traffic in spectrally-spatially flexible optical networks, Comput. Network. 146 (2018) 167–182, [https://doi.org/10.1016/j.comnet.2018.09.011.](https://doi.org/10.1016/j.comnet.2018.09.011)
- <span id="page-16-4"></span><span id="page-16-0"></span>[93] S. Fujii, Y. Hirota, H. Tode, K. Murakami, On-demand spectrum and core allocation for multi-core fibers in elastic optical network, 12 in: Optical Fiber Communication Conference/National Fiber Optic Engineers Conference 2013, vol. 6, 201[3https://doi.org/10.1364/OFC.2013.OTh4B.4.](https://doi.org/10.1364/OFC.2013.OTh4B.4) OTh4B.4 [http://www.](http://www.osapublishing.org/abstract.cfm?URIOFC-2013-OTh4B.4) [osapublishing.org/abstract.cfm?URIOFC-2013-OTh4B.4.](http://www.osapublishing.org/abstract.cfm?URIOFC-2013-OTh4B.4)
- <span id="page-16-5"></span>[94] K. Walkowiak, M. Klinkowski, P. Lechowicz, Scalability analysis of spectrally-spatially flexible optical networks with back-to-back regeneration, in: International Conference on Transparent Optical Networks 2018-July, 2018, pp. 18–21, [https://doi.org/10.1109/ICTON.2018.8473726.](https://doi.org/10.1109/ICTON.2018.8473726)
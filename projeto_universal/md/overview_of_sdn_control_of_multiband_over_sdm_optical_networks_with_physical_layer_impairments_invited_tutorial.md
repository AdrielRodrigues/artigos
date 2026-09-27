---
title: "Overview of SDN control of multiband over SDM optical networks with physical layer impairments [Invited Tutorial]"
tema_principal: projeto_universal
temas_relacionados: []
ano: 2025
autores: []
veiculo: null
pdf: ../pdf/overview_of_sdn_control_of_multiband_over_sdm_optical_networks_with_physical_layer_impairments_invited_tutorial.pdf
---

# Overview of SDN control of multiband over SDM optical networks with physical layer impairments [Invited Tutorial]

**Ramon Casellas,\* Ricardo Martinez, Ricard Vilalta, AND Raul Muñoz**

CTTC-CERCA, Av. Carl Friedrich Gauss n7 08860 Castelldefels, Barcelona, Spain \*ramon.casellas@cttc.es

Received 15 July 2024; revised 6 November 2024; accepted 20 November 2024; published 13 January 2025

**This paper, an extended version of a tutorial presentation given at OFC'24, aims to provide an overview of key aspects in the design and development of a control plane for multiband over spatial division multiplexing optical networks following software defined networking principles. The tutorial will address system design considerations such as the systematic use of data modeling model-driven development; will detail selected, industry-adopted northbound and southbound interfaces for full and partially disaggregated networks; and will introduce advanced considerations such as accounting for physical layer impairments, externalizing path computation and path validation functions or the multilevel control when considering the management of network media channels over dynamically switched spatial channels. We show a prototype of an SDN controller with multigranular nodes combining flexigrid DWDM switching over SDM/core switching, including transport API extensions for the new protocol layer qualifier.** © 2025 Optica Publishing Group. All rights, including for text and data mining (TDM), Artificial Intelligence (AI) training, and similar technologies, are reserved.

https://doi.org/10.1364/JOCN.536816

# 1. INTRODUCTION

Given the relative maturity of optical technology, a significant effort has been made to define generic use cases, requirements and frameworks for the control of optical networks adopting software defined networking (SDN) principles [1], and to subsequently extend and produce open and standard data models. Until recently, SDN frameworks and data models have assumed the usage of the C-band due to its low attenuation and the properties of EDFAs. However, the increase in traffic and the need for additional capacity [2] justifies the usage of additional optical bands—often referred to as multiband (MB) or wideband networking—as a first step and, in the long-term, exploiting the capacity increase provided by spatial domain multiplexing (SDM).

Despite a significant adoption of SDN for the configuration and control of optical networks in the metro/aggregation and core domains, there is a continuous development driven by new or improved technologies at the data plane, to efficiently exploit the increasing programmability and to ensure an efficient and optimal usage of resources with satisfactory quality of transmission with increasing data rates. The adoption of MB as well as SDM raises new challenges and requirements to the control plane: It is no longer possible to assume neither homogeneous devices nor simple models for transmission and signal propagation nor a single frequency range with quasiuniform behavior for all channels within the band.

Further development of physical layer impairment (PLI) models, which became necessary with the "beyond 100G" data rates and the adoption of coherent technologies, is critical. The main function of the SDN control plane is to enable the dynamic provisioning with recovery of data services enabling certain automation; thus, extending SDN for multiband implies accounting for a (potentially) variable number of arbitrary bands and their effects and constraints, and, similarly, extending it for SDM requires researchers to carefully consider the implications on network control of having parallel links (SDM lanes) as well as crosstalk and related effects between such parallel lanes, which has, until now, not been modeled from a control plane perspective. In both cases, accounting for heterogeneous composition of devices is also necessary.

This paper is an extension of our OFC tutorial [3]. Its purpose is to provide an overview of the evolution of the control plane design and challenges to support multiband over SDM (MBoSDM). The paper is structured as follows: In this introductory section, we provide a short overview of optical technologies for capacity scaling and basic ITU-T flexigrid terminology. Section 2 provides a recap of the SDN framework, based on the adoption of model-driven development and open and standard data models as well as architectural, algorithmic, and modeling challenges. Section 3 further elaborates on ongoing data modeling affecting control plane constructs, devices, and networks. Section 4 addresses the joint control of multiband flexigrid networks addressing SDM either as parallel bundles of fibers (BoFs) or as multicore fibers (MCFs), relying on the so-called multigranular optical nodes (MGONs) [4]. Section 5 describes a proof-of-concept (PoC) of a single SDN control plane instance controlling an optical network with dual switching capabilities. Section 6 concludes the paper.

## A. Optical Transport Networks and Technologies for Capacity Scaling

A key enabler technology for sustained capacity scaling is multiband transmission, which offers increased capacity in standard single mode fibers (SSMF) by exploiting the S-, E-, O-, and U-bands in addition to the C- and/or the commercially available C+L-bands. MB maximizes the use of the currently deployed network infrastructure, with reduced CapEx [5]. Similarly, according to the estimations derived from the traffic analysis of [6], regional and national nodes should efficiently manage the aggregated traffic, ranging from a few Tb/s in the short-term, 10 Tb/s in the medium-term, and potentially reaching up to a hundred Tb/s in the long-term. Other drivers for the adoption of multiband are capacity scaling, the deployment of optical links in support of data center interconnects, cloud storage/computing, and on-demand media consumption, notably when reusing the fiber plant is a key cost factor. The diversity in performance characteristics across different frequency bands provides a strategic advantage, as transmission can be flexibly adapted to the specific user needs. However, MB transmission also introduces new challenges such as nonlinear effects [i.e., stimulated Raman scattering (SRS)], which must be considered within the system design. Specifically, a power transfer between wavelengths with specific spacing occurs because of the interplay of wavelength division multiplexing (WDM) channels across the various bands [7,8]. Finally, different optical amplifiers, filters, modulators, detectors, and lasers should be included according to the operating band. In general, adopting technologies tailored for specific bands, beyond the traditional C-band, is often accompanied by higher implementation costs [9].

In the medium- and long-term, solutions will combine wideband and space division multiplexing. The adoption of the technology is gradual, from point-to-point systems focusing on transmission aspects and later addressing switching by means of specialized devices. Introducing SDM switching (either as fiber switching or core/mode switching and variations thereof ) enables the optical bypass, enabling *spatial channels and cross-connects*.

Having several layers does not necessarily mean better performance. An MB over SDM network will have a lower blocking rate if the SDM links are always terminated (no switching) and switching happens at the higher WDM layer, allowing an any-to-any switching. Optical bypass becomes of interest in terms of cost efficiency, e.g., when there are specific traffic patterns that favor grooming (multiplexing several high-level connections into a low-level connection) without resource waste and to reduce node internal architecture and cost or when a single (or small number of ) client signal(s) may occupy the entire available spectrum of either a conventional SSMF or one core in a few-mode MCF.

In this context, control plane design deals with the overall question of how to support dynamic provisioning and network automation, identifying initial requirements and proposed extensions.

## B. Flexigrid Reference Network for Control and Management

Before moving into the specifics of the control plane, we need to define a reference network and introduce (simplified) key terminology, with the help of Fig. 1. An optical tributary signal (OTSi) [10] is defined as an "optical signal that is placed within a network media channel for transport across the optical network ... and may consist of a single modulated optical carrier or a group of modulated optical carriers or subcarriers." This corresponds to the superseded "optical channel" (OCh). The OTSi is unidirectional in nature and is typically characterized by its modulation format, baud rate, etc. A straightforward extension is the OTSi group (OTSiG) [11], defined as a "set of optical tributary signals (OTSi) that supports a single digital client." Consequently, there is a degree of flexibility in how a digital signal (e.g., 400 Gb/s) can be modulated in the optical domain, i.e., in terms of a single OTSi or group of OTSis using single or multicarrier modulation formats. Usually, there is a trade-off in terms of reach/robustness, used spectrum, and efficiency. In any case, for a given OTSiG, it is defined that the different components of the OTSi are 1) co-routed over the same fibers and 2) transmitted ensuring a controlled differential delay. Finally, a transceiver [12] commonly corresponds to a Tx/Rx pair and terminates a single OTSi where multiple transceivers can be grouped in a transponder.

From the resource perspective, a media channel (MC) [11] is defined as a media (as in optical transmission media) association that represents the topology (i.e., the path) and the resource (i.e., the frequency slot or spectrum range) that it occupies. In simple terms, it can be understood as an effective (resulting from a concatenation of filters) frequency range in an optical media topological construct such as a fiber or concatenation of fibers and filters. More specifically, a media channel supports zero or more OTSis; a network media channel (NMC, also referred to as an end-to-end media channel) is then defined between transceiver media ports (zero or one OTSi) and roughly corresponds to the optical channel carrier (OCC) in fixed grid networks. Finally, a media channel group (MCG) [11] is a unidirectional point-to-point management/control abstraction that represents a set of one or more media channels that are co-routed. A media channel group is bounded by a pair of media ports. Of specific relevance in a multidomain context are the optical transmission section (OTS) MCG, which from a management perspective is a topological construct between two adjacent amplifiers (booster/in-line-amplifier/. . . /pre-amplifier) and the optical multiplex section (OMS) MCG, which is the topological relationship between the media port on a filter or coupler where a set of media channels are aggregated and the media port on a filter or coupler where one or more media channel is added to or removed from that aggregate. In this setting, all media channels that are represented by the OMS MCG must be carried over the same serial concatenation of OTS MCGs

![](_page_2_Figure_3.jpeg)

Fig. 1. Concepts of OTSi and MC and OMS/OTS MCGs.

and amplifiers, and a fiber encompasses either an atomic media channel or media channel group, which corresponds to the usable bands in such a fiber. When characterizing a "C-band only" OMS/OTS, it is commonly assumed as a single MC or frequency range.

## 2. SDN CONTROL OF MULTIBAND NETWORKS

# A. Software Defined Networking and Model Driven Development

The increased programmability of optical devices, including those being extended to support multiband transmission and switching, is a key driver for the adoption of SDN in the control and management of optical networks, which, along with flexible optical telemetry platforms, enable more autonomous networks by closing the observe/decide/act loop.

Model driven development (MDD) is an approach to designing distributed systems based on the systematic use of data models, which can be automatically processed and validated, used with optimized transfer protocols in such a way that uses cases, business logic, and applications can be developed. There are several pillars for MDD: a functional architecture, usually following a client/server approach; transport protocols optimized for the operations of configuration and telemetry such as NETCONF/RESTCONF or gNMI; open and standard data models describing systems and devices; and finally a data modeling language to define the data models such as YANG. SDN remains a logically centralized control model architecture, enabling an application layer, although as we will see next, the current trend is to decompose into functional elements or entities and jointly address aspects of 1) configuration and control and 2) monitoring and telemetry.

# B. Challenges to the SDN Control of Multiband Networks

As stated, the macroscopic goal is dynamic service provisioning and introducing a certain degree of automation. In this sense, an optical controller is expected to export a standard northbound interface (NBI) that is consumed by applications and, more recently, also by specialized functions deployed in a modular way. Provisioning workflows involve multiple actors and, based on a set of constraints, devices and subsystems are configured following their data models.

The starting initial considerations include 1) to address the additional complexity in network control and management due to the usage of additional optical bands and multiple switching layers, 2) to remove the assumption of quasiuniform behavior for channels and address heterogeneity in devices in terms of capabilities and configurations, and 3) to account for physical layer impairments such as SRS or launch power optimization. To meet these objectives, the challenges that an SDN control plane needs to address in this evolution are manyfold and they cover the following:

- 1. architectural aspects, in which monolithic approaches are being replaced by more modular systems with specialized functions (including, for example, externalized path computation);
- 2. algorithmic aspects that are needed to perform resource allocation based on resource allocation and multiband transmission modeling with QoT validation; and
- 3. modeling aspects, to cover the modeling of physical layer impairments, node internal architectures and restrictions (e.g., the existence of per-band demultiplexing), and other applicable concepts.

#### 1. Functional Architecture Challenges

A simplistic architecture view of an SDN control plane (in terms of a single centralized controller on top of an underlying infrastructure and enabling an application ecosystem) is no longer adapted to evolving requirements. Monolithic systems are not flexible and modular enough to support emerging use cases; there is an increasing integration of the packet and optical layers, including pluggable transponders [13], which can be addressed with multiple deployment models.

An SDN control plane requires the coordination (orchestration) of dedicated systems as well as the consolidation of specialized software for aspects such as path computation, path validation, or function placement. This is being extended to address the application of digital twins [14] for various aspects of network operation as well as the integration of AI/ML assisted operation. For example, as seen in Fig. 2, a control plane instance may involve an optical controller that configures the transceivers and that delegates the configuration of the line system to a dedicated (OLS) controller, which may, in turn, coordinate with a separate amplifier control. At any level, a controller may rely on external functions. The overall SDN control plane may be containerized and deployed as a service.

![](_page_3_Figure_3.jpeg)

Fig. 2. Control plane architecture involving several dedicated components in a "separation of concerns" disaggregated approach.

![](_page_3_Figure_5.jpeg)

Fig. 3. Optical monitoring and telemetry platform, including the SDN control plane acting as the producer/consumer of telemetry data.

This evolution toward more *service-based architectures* applying a *separation of concerns* design guideline, instead of monolithic solutions, further highlights the need for standard and open interfaces.

This evolution applies not only to configuration and control functions but also to optical monitoring and streaming telemetry with dedicated systems and platforms, (as, shown for example, in a hierarchical setting in Fig. 3), which are enablers for advanced algorithms and for closed-loop network automation. While there has been a lot of work related to optical telemetry [15–17], most of it applies to *device telemetry*, in which optical devices (transceivers, amplifiers, ROADMs) act as sources of data. Given the increasing need for telemetry, dedicated platforms are being deployed to assist network operation. Such telemetry platforms can scale to hundreds of data sources, efficiently manage aspects such as time-series databases, leverage on architectural options such as message buses or producers/consumers, and solve scalability concerns by decoupling the production of telemetry data out of the storage and consumption/visualization of data.

Given this previously presented functional decomposition of the control plane, the need for state synchronization (e.g., in terms of topology, deployed services, etc.) becomes important. As such, aspects related to *controller telemetry* in which the different components of the control plane become streaming telemetry data sources show increased efficiency compared with methods based on, e.g., polling. For example, as seen in Fig. 4, several use cases benefit from controller telemetry in which a state is synchronized such as 1) hierarchical control planes in which parent controllers need an abstracted topology view of child domains; 2) fault management, where a delegate controller may notify a higher entity of a specific failure or threshold crossing alert; 3) externalized path computation in which a path computation element (PCE) requires an updated traffic engineering database; or 4) the usage of DT to keep an updated virtual copy of a physical system.

#### 2. Path Computation and Resource Allocation Challenges

The concepts of path computation, path validation, and routing and spectrum assignment (RSA) are often used interchangeably. In the context of this work, the path computation function can be defined as finding a topological path, as a sequence of links, and a set of resources to be allocated to support a given connectivity service. In the specific case of the photonic media layer where the main resource is the flexigrid optical spectrum, the path computation includes assigning the corresponding media channel (group), characterized by its effective frequency slot (nominal central frequency and slot width) and the properties of the corresponding OTSi (group) such as modulation format, or transmission power. This is often referred to as RSA and admits variations depending on the type and terminology of the resources potentially being

![](_page_3_Figure_13.jpeg)

Fig. 4. Common use cases for controller telemetry in which an SDN controller or control plane functional element behaves as a data source, sending asynchronous events that can be considered a stream and stored in a time-series database.

![](_page_4_Figure_3.jpeg)

**Fig. 5.** Diagram of the interaction between the SDN controller and the multiband PCE with a macroscopic view of inputs [20].

allocated (optical band, fiber core, or transceiver operational mode) [18]. On the other hand, the path validation function deals with evaluating the path feasibility, e.g., its satisfactory quality of transmission (QoT) and the impact of the new service on existing services using different techniques such as analytical or simulation models or, more recently, AI/ML models. Although these functions are clearly related (and in some cases path validation is part of the computation function), they may be decoupled due to, e.g., a formal separation of concerns. Reasons for this include the fact that specialized and externalized software tools may be available (e.g., GNPy [19]), and these may require inventory data and equipment characterization in terms of a physical layer that may not be available to the control plane. Variations of this approach exist, e.g., the modulation format assignment can be part of the validation process. Finally, let us note that different deployment models apply, including the case where a given path may be precomputed and prevalidated and provided to the control plane as an additional constraint in the provisioning process.

Path computation and validation are two critical functions, and they are increasingly expected to operate in hybrid mode, e.g., as part of planning operations or online, e.g., during the dynamic provisioning of connectivity services. Common approaches range from simple heuristics, e.g., based on a combination of Dijkstra/Yen k-shortest paths using linear multiband transmission modeling accounting for OSNR estimation that depends on reach, amplifier noise figure, and fiber attenuation, iterating on the available/feasible bands, and using a first-fit approach to more advanced approaches as the one in [20] (see Fig. 5) or using well-proven approaches like GNPy [19]. More recently, the usage of deep/reinforcement learning to assist the RSA is gaining traction [21]. More generic digital twins may also recommend rerouting actions upon a certain event, such as exceeding a defined monitoring threshold, closing the loop where the network state, used as input data, is gathered by means of asynchronous streaming telemetry.

Regardless of the path computation function actual implementation, it is a common requirement that the control

plane needs to model any required algorithm inputs in an efficient and scalable way. This means that it may not be able to characterize specific parameters on a "per-frequency or per wavelength" basis but work with aggregation, abstraction, and simplifications requiring careful analysis of the underlying trade-off and implications. The amount of modeling data that may be required may have a significant impact on the overall provisioning latency when considering complex workflows that involve multiple control plane entities. To support externalized PCE/DT, the control plane may typically advertise network information related to the following, as a macroscopic example:

- Network topology, in terms of media channel constructs, OTSs, OMSs (links), ROADMs, amplifiers (as network nodes), service endpoints (Tx/Rx pairs, transceivers), supported optical bands, and applicable characteristics.
- Capabilities of the deployed transceiver in terms of supported operational modes, frequency ranges, or tunability constraints.
  - ROADMs: internal interconnection restrictions
- Characterization of amplifiers' gains, ripple, operational ranges, noise figures, etc.
  - Existing services (e.g., OTSi signals).
- Effects (optical impairments) at different stages, including fiber linear/nonlinear effects, filtering effects, insertion losses, etc.

Algorithms thus need to be carefully stated in terms of their *inputs* and *outputs*, and this should be translated into requirements in the format and semantics of data as well as in aspects related to how these data are made available to externalized tools. Modeling challenges all relate to providing those inputs while enabling close to optimal solutions.

# 3. Data Modeling Challenges

Finally, the third key challenge discussed in this paper is related to the actual data modeling, having as a key objective to properly model (i.e., in terms of objects, their attributes, and their relationships such as containment of references) network services, networks topologies, control plane constructs, and data plane devices with different levels of abstraction to enable path computation, QoT validation, and performance monitoring, while accounting for the existence of multiple optical bands (arbitrary frequency ranges). Standard models are key for information exchange and are among the most active aspects of standardization.

Such modeling work includes, but is not limited to, migrating from *an implicit ban* toward a *per band* parameter grouping multiplicity. This means qualifying given data by the band in which it applies, and a systematic methodology is to revisit existing data models, extend the multiplicity and composition, and parameterize a given aspect with the applicable frequency range.

For example, a basic modeling item relies on the notion of OMSs/OTSs and how the states on nominal central frequencies within available bands/frequency ranges are encoded, either as port or link attributes. It is, for example, possible to model each OMS MC of the OMS MCG as a distinct entity, enabling finer per-band characterization or, alternatively, to

![](_page_5_Figure_3.jpeg)

Fig. 6. GUI of a TAPI-enabled controller showing bands as photonic media network edge point (NEP) media channel pools of a single OMS instance.

model the whole MCG in a single instance by addressing *different media-channel pools* (see Fig. 6). The choice is based, notably, on the heterogeneity of transfer parameters of each band.

The former approach is simple and straightforward but fails to capture specific aspects of the band transfer parameters and presents a clear trade-off: wideband transmission modeling may benefit from a finer characterization (e.g., per wavelength) but may not scale or such characterization may not be available. The latter approach multiplies the number of managed entities and instances.

Another recurrent aspect to address scalability relies on the usage of profiles, which are groupings of static, invariant data that groups and centralizes related information and that is reused/referred to across several instances, avoiding needless duplication, but at the same time is also stored and retrieved as part of the data models to ease information retrieval from a limited number of sources. Specific standards defining organizations (SDOs) or projects are currently defining or augmenting common profiles that cover key aspects of optical networks, including fiber profiles, amplification profiles, or transceiver operational profiles. Despite efforts to make profiles common across SDOs, they still need to fit in their respective control frameworks and information models, but it should be relatively easy to map information between different profiles. The benefits of using profiles depend on the number of similar instances, but this is often justified.

# C. Modeling Multiband Transmission

To leverage the additional capacity offered by additional optical bands, it is of the essence to model multiband transmission considering nonnegligible frequency dependent parameters. Although the ITU-T has defined the set of optical bands, good design practice should account for a variable number of arbitrary bands and arbitrary frequency ranges, without assumptions of the specific nominal central frequency granularity or slot width granularity. Let us note that, when considering multiband systems, it is often not effective to consider optical fibers as linear media; further, in general, fiber nonlinearities need to be addressed during the design and provisioning phases. In multichannel systems, in addition to cross-phase modulation (XPM) and four-wave mixing (FWM) nonlinear effects, SRS leads to power transfer from some channels to other channels. Therefore, it is common to adjust the power levels to minimize the effects of nonlinear impairments and their fluctuation as done, for example, in [20]. This explains the need to further develop the modeling of the physical layer and to augment control plane constructs with data models enabling transmission and switching modeling and optical power management. Band-specific effects and constraints on the optical signals (also referred to as "media channel transfer parameters") can be analytically modeled or simulated. This includes, e.g., fibers and amplification transfer functions, including attenuation (in dB/km) or chromatic dispersion (in ps/nm/km).

To this end, ad hoc models compute an optical signal-tonoise and interference ratio (OSNIR), which accounts for amplifier spontaneous emission (ASE) noise accumulation and for fiber nonlinearities. The latter incorporates intraband effects such as cross-channel interference and self-channel interference as well as interband effects such as SRS, including closed-form approximations [22,23].

Similarly, the usage of the generalized SNR as a fast and accurate QoT estimation [24,25] has been demonstrated, and such an approach has been recently used in different scenarios and use cases, including the consolidation of open-source software projects for this purpose (e.g., GNPy and its application to multiband [26]).

# 3. CONTROL PLANE DATA MODELS FOR MULTIBAND

As introduced in the previous sections, one of the critical challenges is to model networks, devices, and, generically, control plane constructs, which is always a trade-off in the abstraction and selection of the level of details. Key modeling issues include how are transceiver tunability constraints managed, how are WSS/ROADM hardware restrictions/specifications encoded, and how are the different bands efficiently represented in the SDN controller, exporting information that can be usable by clients or external entities. When augmenting existing data models, a recurrent question refers to how do we "retrofit" enhanced data models into current ones, thus minimizing backward compatibility issues. In this section, we list some of the work items in the standards process in support for multiband.

In this section, we briefly mention ongoing extensions in the Linux Foundation Transport API [27] data models in support of the requirements. Let us note that there are similar relevant projects, including from the IETF [28,29], which will not be described here.

## A. Summary of the TAPI Core Information Model and Concepts

In TAPI terminology, the common context serves as shared information between a TAPI client (e.g., a network orchestrator) and the TAPI server (the optical SDN controller). The context can be graphically represented as shown in Fig. 7. This model organizes the optical domain by means of service interface points (SIPs, blue circles in the diagram), identifiable by

![](_page_6_Figure_3.jpeg)

Fig. 7. Graphical representation of the TAPI context showing the network topology and in service connections along with the NEP/CEP roles and relationship (protocol stacking).

their universally unique identifiers (UUIDs), providing endpoints between which connectivity services can be deployed. When the topology model is also supported, the context is augmented with the inclusion of one or more topologies. In most cases, each topology consists of a collection of nodes (which model terminals, ROADMs, or amplifiers) and is equipped with NEPs (purple boxes), which are ports that belong to specific protocol layers. When a connectivity service is provisioned, the controller instantiates connections at different sublayers, referred to as protocol layer qualifiers (e.g., OMS, MC layer). Those connections can be "top-level," indicating an end-to-end connectivity, or "lower-connections" (or cross-connections), reflecting an active configuration internal to a node. TAPI connections are defined in terms of specific connection end points (CEPs, yellow boxes), which are instantiated over the corresponding NEPs. Macroscopically, NEPs encode resource availability (e.g., usable frequency ranges), potential configuration, and quasistatic parameters. CEPs reflect active configuration and allocated resources to the connection (e.g., used frequency slot, modulation format).

#### B. OTS/OMS Characterization (Fibers)

A first modeling item (Fig. 8) covers the characterization of fibers in terms of PLI. OTS\_MEDIA NEPs/CEPs group aspects like total loss or loss coefficient, PMD and connection losses, or length. NEPs may also refer to static fiber profiles that include static information such as fiber type.

# C. Transmission: Operational Modes and Transceiver Profiles

To perform configuration tasks related to modulation format and FEC selection, it is important to characterize, to a fine degree, the different operational modes of a transceiver. By consensus, this is currently modeled in TAPI by using transceiver profiles. Specific per-model augmentations provide details on a given profile type. TAPI NEPs can refer to transmission capability profiles (see Fig. 9), including the potential payload structure. In the photonic media context, transceiver profiles can be either standard or explicit. Standard profiles are referred by code or value to a defined application and need no

![](_page_6_Figure_10.jpeg)

Fig. 8. TAPI models for the OTS media layer protocol qualifier (fiber).

![](_page_6_Figure_12.jpeg)

Fig. 9. TAPI models for transceiver profiles characterizing transceiver usable operational models.

further detail. Explicit modes include aspects like max accepted CD and PMD dispersion, modulation format, baud rate, FEC type, and threshold and can be extended to add additional parameters. Let us note that, for explicit profiles (profiles for which most of the parameters are directly encoded), there is a pair of values specifying the applicable frequency range. Different per band transceiver profiles may then coexist.

For example, the sliceable bandwidth variable transceiver [30] that is controlled by means of an SDN agent based on extended OpenConfig data models (see Fig. 10 [31]) and can transmit in the S- and C-bands (work on the L-band is ongoing) exports OpenConfig operational mode details that are mapped into TAPI profiles by the SDN controller.

#### D. Switching: ROADM Capabilities and Impairments

In many cases, it is often assumed that ROADMs in the optical line system are colorless, directionless, and contentionless (CDC) and enable any-to-any cross-connections. In more advanced implementations, a basic description of the internal node is provided, e.g., in terms of a connectivity matrix that specifies which input degrees are connected to which add/drop stages and/or output degrees. Recently (Fig. 11), new data

![](_page_7_Figure_3.jpeg)

**Fig. 10.** Optical spectrum of the S-BVT transmitting in the C-band (left) and in the S-band (right), from [31].

![](_page_7_Figure_5.jpeg)

**Fig. 11.** Characterization of the PLI penalties by means of aggregated add, drop, or express paths.

models have been introduced to characterize signal penalties for an aggregated number of cases.

Given the different migration strategies toward multiband networks, it is important to also characterize and represent hardware limitations and architectural restrictions. This further presents a clear trade-off, since optimal solutions may need detailed internal node interconnection; however, device models that need to scale and control plane instances may be required to support hundreds of nodes and devices.

Despite that current data models allow researchers to characterize internal interconnection and account for basic physical impairment effects by describing a signal degradation for express/add and drop paths, the extension to multiband networks requires further specifying which bands are supported at each degree and extend connectivity and degradation on a per band basis. In all, from the control plane perspective, actual physical architectures are constrained by the underlying technology (a critical example is that there are no WSSs that cover all bands with the same granularity in terms of central

frequency and slot width [32]), but, at the same time, device models need to scale for large networks.

#### E. Amplification and Amplifier Characterization

Front the point of view of modeling, the characterization of amplifiers relies on a combination of amplification profiles, which characterize static aspects like gain range, noise figure range, and min and max power and gain, as well as new attributes and extensions to the OMS CEP entities, with parameters such as actual gain and actual tilt out-VOA or in-VOA. Let us note that these parameters are grouped into lists characterized by the frequency range of application, and it is then possible to have different values for different bands.

However, doped fiber amplifiers that can cover multiple bands are either not technologically mature, do not exist [33], or apply only in specific scenarios such as in the C+L-band. The physical architecture of a multiband amplifier may rely on the deployment of one amplifier per band and the usage of DEMUX/MUX stages [25] (Fig. 12). In these cases, the characteristics of each band amplifier may be heterogeneous. It is then a challenge to present the amplifier with an abstracted architecture that does not require the description of internals, either as a topological node or as set of amplification functions with selected operating point characteristics. Initial efforts characterize such amplifiers with a reduced set of parameters as in [34] or [27]. It is expected that refinements in the modeling and characterization of amplifiers will be developed as the technology progresses.

## 4. MULTIGRANULAR NODES AND MBoSDM

The steady traffic increase means that solutions based on exploiting additional bands will not suffice in the long-term. Further capacity scaling means going parallel and exploiting the spatial dimension [35,36], including the usage of recently developed sliceable multidimensional (spectral and spatial) transceivers [37]. In this paper, we consider 1) single level or flat networks and 2) multilevel networks.

![](_page_7_Figure_16.jpeg)

**Fig. 12.** Multiband ROADM and amplifier sample physical architectures. Device models can abstract physical details in view of efficiency.

![](_page_8_Figure_3.jpeg)

Fig. 13. Multilevel networks with single switching nodes (left) and with hybrid/multigranular nodes (right).

#### A. Single Level (Flat) Networks

In single-level or flat optical networks, parallel links are deployed either as BoFs or, in a longer term, as multicore fibers with fan-in/fan-out systems. However, such SDM systems are mostly point-to-point, and switching only happens at the photonic media/media channel (DWDM) level. In other words, the SDM or spatial layer is systematically terminated at each node, and transported OTSi signals are switched (by switching their media channels). ROADM architectures based on WSSs require, in such cases, many ports. A network with a max node degree of 9 with bundles of 8 fibers may typically require WSSs with ∼70 ports (this is without considering add/drop ports). Considering node architectures such as nonspatial lane switching or limiting internal connectivity may reduce the number of required ports at the expense of reduced performance, the introduction of additional bands and the limitations of WSS technology render this problem even more complex.

From the control plane perspective, control functions need to consider internal ROADM connectivity with, e.g., WSS modeling, e.g., by means of internal links between circuit pack ports, as in OpenROADM device data models [29]. In this sense, this represents a straightforward upgrade, yet the scaling control plane implications means potential scalability issues in the number of controlled entities since there is an N-fold increase in the number of managed links and a subsequent increase in path computation complexity and path computation latency; overall, the control plane functions remain mostly unmodified.

## B. Multilevel Networks

Multilevel networks (see Fig. 13) extend single-level networks by introducing different switching granularities (levels); these may encompass, for example, WDM switching (media channel switching, either in fixed- or flexigrid), optical band switching (e.g., C-band switching), waveband switching [38], or fiber/core switching. At specific points, signals may be switched at a given level/layer. It is known that switching at the highest level (e.g., DWDM switching) yields better performance, but introducing switching at the lowest (aggregated) layers may simplify node architectures and be more cost effective.

From the control plane implications, multilevel networks are more complex to manage than single-level networks, for the simple fact that the SDN control plane needs to address the additional associated complexity of controlling multiple levels. In this setting, node modeling and abstraction are critical aspects to consider, and the control plane needs to account for the existence of transitional links (from one client level or layer). SDN control can leverage previous know-how in terms of control of multilayer networks.

#### 1. Multilevel Networks with Single Switching Nodes

In this specific case, multilevel networks encompass single switching network elements (nodes with one switching capability or layer). The network can be segmented into what is called "technology domains" or "regions," with, e.g., multiband DWDM/flexigrid switching and core/fiber switching, respectively. The control plane implications are addressed by having a hierarchical arrangement of SDN controllers and orchestrators, as is common practice in reference architectures (TAPI, ACTN). In this case, nodes are simpler, and technology specific SDN controllers can be deployed. Multiplexing and demultiplexing connections are commonly coordinated by a parent controller or network orchestrator (see [2]). In [39] (Fig. 14), network orchestration with DWDM services over MCF was shown; in [40], it was extended to cover of dynamic deployment of SDN-enabled WDM virtual network topologies (VNTs) over SDM networks.

#### 2. Multilevel Networks with Hybrid (Multigranular) Nodes

In this, more generic, case network elements are able to terminate data links with different switching capabilities and are characterized by the ability to terminate and/or switch connections at different levels. In the optical domain, such nodes are also referred to as multigranular nodes. Cases of interest are nodes with dual DWDM (i.e., multiband) over fiber or core (SDM) switching. Such nodes present a classical arrangement with different switching (sub) matrices. Scalability/efficiency or feasibility constraints drive multistage configurations or hierarchical/coarse/multigranular nodes.

![](_page_9_Figure_3.jpeg)

Fig. 14. Network control and orchestration in SDM and WDM optical networks [39] (top) and the demonstration of SDN-enabled WDM VNTs over SDM networks [40] (bottom).

From the control plane perspective, the question to address is what are the extensions (architectural, protocol, or algorithmic) required to, potentially jointly, address wavelength (media channel), waveband, and SDM switching. With a common deployment model of a single SDN controller per domain, further modeling and standardization work is required to efficiently reuse the model-driven development and existing frameworks for SDN control of MB over SDM networks. In summary, in addition to the previous challenges, the extension to multilevel networks requires the following:

- Addressing VNTs at different levels, the management of logical (virtual) links supported by low layer connections, and the overall formal description of additional protocol layers and layer protocol qualifiers (e.g., formally introducing the capability of "core switching"/fiber switching in a standard way).
- Characterizimg optical links at the SDM layer (e.g., identifying fiber indexes within a bundle of fibers or identifying cores/modes in a multicore setting.
- Defining propagation models and physical impairments extensions to account for aspects such as intercore cross-talk.
- Extending node capability and interconnection models and related abstractions, including transactional links.
- Devising new multilayer algorithms that enable optical bypass and grooming with the addition of constraints such as the core-continuity constraint, in which the path computation function and resource allocation must ensure that a given spatial path uses a single core index, analog to the spectrum continuity constraint of WDM networks.

## 5. PoC OF A MBoSDM SDN CONTROL PLANE

#### A. PoC Architecture

To illustrate concepts presented in this paper, in this section we detail the proof-of-concept of an SDN control plane for the control of multilevel networks with multiband-enabled flexigrid networks over SDM (MBoSDM), like the one shown in [41]. The SDM layer can be either BoF links with fiber switching or MCF in which the nodes have performed core switching thanks to the usage of core selective switches (CSSs) [42].

The network is composed of four multigranular (MBoSDM) nodes (see Fig. 15). The optical controller NBI interface, based on the set of Linux Foundation TAPI models has been augmented, introducing an experimental protocol layer qualifier (PHOTONIC\_MEDIA/SDM\_CORE). Different entities (NEPs, CEPs) have been augmented to encompass the status of cores/fibers. The user requests an NMC service between client ports, and the SDN controller may allocate SDM connections as needed (which involves

![](_page_9_Figure_15.jpeg)

Fig. 15. PoC with a 4 node and 10 MCF link topology shown by the controller (left) and resulting media channel service between nodes 1 and 2 using optical bypass (core switching). CoreId = 1 (red) was allocated by the RSCA algorithm with core continuity constraints.

![](_page_10_Figure_3.jpeg)

Fig. 16. Detail of the considered multigranular optical nodes showing the configured SDM/CORE service (dotted red), the instantiated MB WDM link (purple), and the flexigrid 50 GHz media channel service between WXC client ports (dotted gray).

![](_page_10_Figure_5.jpeg)

Fig. 17. Representation in terms of the TAPI core information model.

allocating a single core service between network elements with continuity constraints). In the case shown in Figs. 16 and 17, to support a virtual DWDM flexigrid link, the SDN controller provisions a connection in the SDM layer (i.e., a core service) using the core c1, which was assigned by the algorithm. Subsequently, such a core is marked as in use at both links and cannot be assigned to other connections; further, a core cross-connection is configured at the intermediate nodes.

# 1. Path Computation and Resource Allocation

Upon request from an NBI client, the path computation algorithm finds a path between two WXC client ports, using, to this end, the set of virtual flexigrid/MC links (the VNT). If the algorithm fails, a second step is executed involving finding a core service from the source to the destination node and instantiating a new DWDM virtual link. The controller must deduce the set of usable bands from the underlying characteristics of the cores/fibers that the service uses. A media channel is then established using the newly allocated link. Virtual links remain instantiated as long as there is at least one client service. In the example, the user requests a 50 GHz NMC service between node\_1\_port\_1 and node\_2\_port\_2. The SDN controller must provision a core service between nodes (c1) in two links (red dotted connection), which supports the MB link (purple link) on top of which is a 50 GHz NMC.

#### 2. MBoSDM Information Models

After the multilevel path has been computed, the SDN controller needs to configure the submatrix operations (see Fig. 16). The macroscopic operations that the SDN agents at the MBoSDM nodes must support are the following:

- Set up and release an *add core* from one WXC output port to the CSS of the outgoing degree.
- Set up and release an *express core* connection from one input degree CSS to another output degree CSS.
- Set up and release a *drop core* from the CSS of the input degree to one input port in the WXC.
- Configure connections from the WXC client and line ports or between line ports (the latter for switching at the WDM layer and grooming).

Figure 17 shows the representation in terms of the TAPI core information model (NEPs/CEPs/connections), including our proposed extensions for the SDM\_CORE switching protocol layer qualifier of the PHOTONIC\_MEDIA layer. SDM\_CORE NEPs report of the available and allocated core identifiers and SDM\_CORE CEPs report on the assigned core. A cross-connection at Node 3 enables bypassing media channel (WDM) switching.

## 6. CONCLUSIONS

The provisioning of network connectivity services needs to be automated via an SDN control plane, using well-established frameworks and platforms. The adoption of MDD, including open and standard interfaces has brought SDN solutions to maturity. That said, in addition to challenges to support the increasing role of network telemetry for autonomous networking, including integration of AI/ML and developments toward more service-based architectures and modular deployments, further research work is required to address optical technologies for sustained capacity scaling such as multiband systems or SDM. A significant part of the work involves properly modeling services, networks, control plane constructs, and data plane devices at different levels of abstraction to enable path computation, QoT validation, and performance monitoring while accounting for the existence of multiple optical bands. There is a trade-off in device modeling, which should remain generic yet account for hardware restrictions.

Current work items in different research communities and SDOs include, but are not limited to, migrating from "an implicit band" toward a "per band" parameter grouping multiplicity.

Overall, extensions to SDN control planes to support multiband over SDM networks are required to efficiently use the additional capacity, either in single- or multilayer deployments, and need to address architectural, algorithmic, and modeling challenges. Overall, this means a significant increase in complexity, and there is a critical role of standards to ensure interoperability. Generically speaking, standardization of control plane aspects is not fully addressed without a reference and standard data plane. For example, standardization on control of flexigrid DWDM networks relied on extended ITU-T OTN recommendations, defining concepts such as frequency slots, media channels, or OTSi. Regarding SDM, to the best of our knowledge, standardization of control aspects is not addressed by the main SDOs at this point, beyond initial proof-of-concept initiatives and research. In some cases (e.g., bundle of fibers), existing standards may be reused (as in fiber switching), but, for multicore fibers, data plane aspects such as proper ITU-T layering, fiber core characterization, and fiber core switching operations need to be addressed first.

Funding. HORIZON EUROPE Digital, Industry and Space (101092766, 101096120, ALLEGRO, SEASON); Ministerio de Asuntos Económicos y Transformación Digital, Gobierno de España (TSI-063000-2021-22, TSI-063000-2021-23, TSI-063000-2021-115, PID2021-127916OB-I00, 6G-OPTRAN-CONTELEM, 6G-OPTRAN-WHITOPEN, RELAMPAGO, 6G-OPTRAN-STEROID).

## REFERENCES

- 1. Telecom Infra Project, "Mandatory use cases for SDN transport (MUST)," white paper, https://telecominfraproject.com/oopt/.
- 2. R. Casellas, R. Martínez, R. Vilalta, et al., "Advances in SDN control and telemetry for beyond 100G disaggregated optical networks [Invited]," J. Opt. Commun. Netw. 14, C23–C37 (2022).
- 3. R. Casellas, R. Martínez, R. Muñoz, et al., "SDN control of multiband over SDM optical networks with physical layer impairments (tutorial)," in Optical Fiber Communication Conference (OFC) (2024), paper W1C.1.
- 4. R. Muñoz, V. Lohani, R. Casellas, et al., "Control of packet over multi-granular optical networks combining wavelength, waveband and spatial switching for 6G transport," in Optical Fiber Communication Conference (OFC) (2024), paper Th1I.4.
- 5. T. Hoshida, V. Curri, L. Galdino, et al., "Ultrawideband systems and networks: beyond C+L-band," Proc. IEEE 110, 1725–1741 (2022).
- 6. M. Ruiz, J. A. Hernandez, M. Quagliotti, et al., "Network traffic analysis under emerging beyond-5G scenarios for multi-band optical technology adoption," J. Opt. Commun. Netw. 15, F36–F47 (2023).
- 7. N. Deng, L. Zong, H. Jiang, et al., "Challenges and enabling technologies for multi-band WDM optical networks," J. Lightwave Technol. 40, 3385–3394 (2022).
- 8. A. Napoli, N. Costa, J. K. Fischer, et al., "Towards multiband optical systems," in Advanced Photonics (2018), paper NeTu3E.1.
- 9. A. Sgambelluri, A. Pacini, F. Paolucci, et al., "Reliable and scalable Kafka-based framework for optical network telemetry," J. Opt. Commun. Netw. 13, E42–E52 (2021).
- 10. "Optical transport network physical layer interfaces," ITU-T Recommendation G.959.1 (2024), https://www.itu.int/rec/T-REC-G.959.1.
- 11. "Generic functional architecture of the optical media network," ITU-T Recommendation G.807 (2020), https://www.itu.int/rec/T-REC-G.807.
- 12. "Amplified multichannel dense wavelength division multiplexing applications with single channel optical interfaces," ITU-T Recommendation G.698.2 (2018), https://www.itu.int/rec/T-REC-G.698.2.
- 13. A. Giorgetti, D. Scano, A. Sgambelluri, et al., "Enabling hierarchical control of coherent pluggable transceivers in SONiC packet–optical nodes," J. Opt. Commun. Netw. 15, 163–173 (2023).
- 14. R. Vilalta, L. Gifre, R. Casellas, et al., "Applying digital twins to optical networks with cloud-native SDN controllers," IEEE Commun. Mag. 61(12), 128–134 (2023).
- 15. F. Paolucci, A. Sgambelluri, P. Castoldi, et al., "Telemetry solutions in disaggregated optical networks: an experimental view," in Optical Fiber Communication Conference (OFC) (2021), paper W1G.1.
- 16. P. González, R. Casellas, J. Pedreno-Manresa, et al., "Distributed architecture supporting intelligent optical measurement aggregation and streaming event telemetry," in Optical Fiber Communication Conference (OFC) (2023), paper M3Z.4.
- 17. R. Vilalta, R. Casellas, R. Martínez, et al., "Optical network telemetry with streaming mechanisms using transport API and Kafka," in European Conference on Optical Communication (ECOC), Bordeaux, France, 2021.

- 18. B. Chatterjee, S. Nityananda, and E. Oki, "Routing and spectrum allocation in elastic optical networks: a tutorial," IEEE Commun. Surv. Tutorials 17, 1776–1800 (2015).
- 19. A. Ferrari, M. Filer, K. Balasubramanian, et al., "GNPy: open source application for physical layer aware open optical networks," J. Opt. Commun. Netw. 12, C31–C40 (2020).
- 20. E. Kosmatos, R. Casellas, K. Nikolaou, et al., "SDN-enabled path computation element for autonomous multi-band optical transport networks," J. Opt. Commun. Netw. 15, F48–F62 (2023).
- 21. C. Hernández-Chulde, R. Casellas, R. Martínez, et al., "Experimental evaluation of a latency-aware routing and spectrum assignment mechanism based on deep reinforcement learning," J. Opt. Commun. Netw. 15, 925–937 (2023).
- 22. D. Uzunidis, E. Kosmatos, C. Matrakidis, et al., "Strategies for upgrading an operator's backbone network beyond the C-band: towards multi-band optical networks," IEEE Photonics J. 13, 7200118 (2021).
- 23. D. Uzunidis, K. Nikolaou, C. Matrakidis, et al., "Closed-form expressions for the impact of stimulated Raman scattering beyond 15 THz," in European Conference on Optical Communications (ECOC), Basel, Switzerland, 2022.
- 24. N. Sambo, A. Ferrari, A. Napoli, et al., "Provisioning in multi-band optical networks," J. Lightwave Technol. 38, 2598–2605 (2020).
- 25. N. Sambo, B. Correia, A. Napoli, et al., "Network upgrade exploiting multi band: S- or E-band?" J. Opt. Commun. Netw. 14, 749–756 (2022).
- 26. A. Ferrari, A. Napoli, J. K. Fischer, et al., "Assessment on the achievable throughput of multiband ITU-TG.652.D fiber transmission systems," J. Lightwave Technol. 38, 4279–4291 (2020).
- 27. A. Mazzini, N. Davis, and R. Casellas, eds., "TAPI reference implementation agreement (RIA)," v3.1, ONF TR-547, https://github. com/OpenNetworkingFoundation/TAPI/blob/v2.5.0/TR-547-TAPI %20Reference%20Implementation%20Agreement\_v3.1.pdf.
- 28. D. Beller, E. Le Rouzic, S. Belotti, et al., "A YANG data model for optical impairment-aware topology," draft, work in progress.
- 29. "OpenROADM device data models," http://openroadm.org/ overview/.
- 30. L. Nadal, R. Martínez, M. Ali, et al., "Advanced optical transceiver and switching solutions for next-generation optical networks," J. Opt. Commun. Netw. 16, D64–D75 (2024).

- 31. R. Casellas, L. Nadal, R. Martínez, et al., "Photonic device programmability in support of autonomous optical networks," J. Opt. Commun. Netw. 16, D53–D63 (2024).
- 32. Y. Ma, L. Stewart, J. Armstrong, et al., "Recent progress of wavelength selective switch," J. Lightwave Technol. 39, 896–903 (2021).
- 33. Z. Chen, L. Wan, S. Gao, et al., "On-chip waveguide amplifiers for multi-band optical communications: a review and challenge," J. Lightwave Technol. 40, 3364–3373 (2022).
- 34. N. Sambo, M. Radovic, A. Sgambelluri, et al., "Multiband optical networks control and provisioning," in Proceedings of Photonics in Switching Conference (PSC) (2023).
- 35. W. Klaus, P. Winzer, and K. Nakajima, "The role of parallelism in the evolution of optical fiber communication systems," in Proceedings of the IEEE (2022).
- 36. Y. Miyamoto and R. Kawamura, "Space division multiplexing optical transmission technology to support the evolution of high-capacity optical transport networks," NTT Tech. Rev. 15, 1–7 (2017).
- 37. R. Muñoz, N. Yoshikane, R. Vilalta, et al., "SDN control of sliceable multidimensional (spectral and spatial) transceivers with YANG/NETCONF," J. Opt. Commun. Netw. 11, A123–A133 (2019).
- 38. D. M. Marom, P. D. Colbourne, A. D'errico, et al., "Survey of photonic switching architectures and technologies in support of spatially and spectrally flexible optical networking [Invited]," J. Opt. Commun. Netw. 9, 1–26 (2017).
- 39. R. Muñoz, N. Yoshikane, R. Vilalta, et al., "Network control and orchestration in SDM and WDM optical networks," in Optical Fiber Communication Conference (OFC) (2020), paper T3J.2.
- 40. C. Manso, R. Muñoz, F. Balasis, et al., "First demonstration of dynamic deployment of SDN-enabled WDM virtual network topologies (VNTs) over SDM networks," in European Conference on Optical Communication (ECOC) (2021).
- 41. A. Sgambelluri, N. Sambo, M. Ismaeel, et al., "TeraFlowSDN controlling SDM and wideband optical networks," in Optical Fiber Communication Conference (OFC) (2024), paper Th2A.2.
- 42. Y. Kuno, M. Kawasugi, Y. Hotta, et al., "Core-selective switch for SDM network based on LCPG and MEMS technology," in Optical Fiber Communication Conference (OFC) (2023), paper M4J.4.
---
title: "Shaping the future of optical networks by integrating SDN, telemetry, and AI [Invited]"
tema_principal: projeto_universal
temas_relacionados: []
ano: 2025
autores: []
veiculo: null
pdf: ../pdf/shaping_the_future_of_optical_networks_by_integrating_sdn_telemetry_and_ai_invited.pdf
---

# Shaping the future of optical networks by integrating SDN, telemetry, and AI [Invited]

**Piero Castoldi,1, \* Filippo Cugini,<sup>2</sup> Molka Gharbaoui,<sup>1</sup> Alessio Giorgetti,3,4 Francesco Paolucci,<sup>2</sup> Anna Lina Ruscelli,<sup>1</sup> Nicola Sambo,<sup>1</sup> Andrea Sgambelluri,<sup>1</sup> AND Luca Valcarenghi<sup>1</sup>**

<sup>1</sup>Scuola Superiore Sant'Anna, Pisa, Italy

Received 23 December 2024; revised 20 February 2025; accepted 28 February 2025; published 27 March 2025

**This paper investigates the most prominent lines of optical network control evolution, focusing on softwaredefined networking (SDN), NETCONF/YANG protocols, telemetry techniques, advancements in packet/optical networking, and the integration of artificial intelligence (AI) within optical networks. We show how the integration of SDN with open modeling frameworks allows to devise hierarchical control models where we trade-off between the segregation of proprietary hardware and the creation of open interfaces like in the OpenSDK scenario. In addition, we depict the convergence of packet and optical layers with advancements in coherent technologies and pervasive telemetry techniques to create new flexible scenarios for controlling optical networks. On top of these approaches, the intent-based networking allows to implement configuration solutions using natural primitives. Finally, key applications of AI, mainly machine learning (ML), including quality-of-transmission estimation, failure prediction, and resource optimization, are analyzed to improve optical network control efficiency alongside their challenges, such as energy efficiency and data scarcity. By addressing advances in the aforementioned areas of research, this work outlines the transformative potential of combining programmability, real-time telemetry, and AI to build resilient, adaptive, and sustainable optical infrastructures for the future.** © 2025 Optica Publishing Group. All rights, including for text and data mining (TDM), Artificial Intelligence (AI) training, and similar technologies, are reserved.

https://doi.org/10.1364/JOCN.553843

## 1. INTRODUCTION

Modern optical network control and management are under profound transformation, driven by network softwarization capable of better supporting the increasing demands for dynamic, scalable, and resilient network infrastructures. Emerging architectural solutions, centered on software-defined networking (SDN), telemetry, and artificial intelligence (AI), have set the stage for an era of intelligent, autonomous, and efficient optical networks. This evolution is a direct response to the growth in global data traffic, caused by the proliferation of 5G networks, internet of things (IoT) devices, augmented and virtual reality (AR/VR) applications, and cloud-centric services [1].

The adoption of SDN has fundamentally changed how optical networks are managed and controlled. By decoupling the control and data planes, SDN introduces programmability and flexibility, enabling operators to automate tasks, optimize resource allocation, and enhance interoperability across heterogeneous systems. The use of open protocols such as NETCONF and data models like YANG has further standardized device configuration, creating a framework for seamless integration and collaborative innovation [2]. Telemetry, on the other hand, has emerged as a cornerstone for real-time network monitoring. Through advanced protocols such as gRPC and gNMI, telemetry delivers granular, time-sensitive insights into network performance and health, facilitating predictive analytics and preemptive fault management [3,4].

Moreover, both SDN controllers and telemetry techniques could be integrated within a single framework, namely the intent-based networking (IBN) framework, which presents a promising solution for simplifying network management and automating provisioning tasks while providing more agility and improving responsiveness to dynamic business requirements [5].

The integration of packet and optical layers is another pivotal development aimed at addressing the growing need for high-capacity, low-latency networks. Technologies such as coherent optics and smart network interface cards

<sup>2</sup>CNIT, Pisa, Italy

<sup>3</sup>Department of Information Engineering (DII), University of Pisa, Pisa, Italy

<sup>4</sup>CNR-IEIIT, Pisa, Italy

<sup>\*</sup>piero.castoldi@santannapisa.it

(SmartNICs) enhance the efficiency of data transport while reducing latency and operational complexity [6]. The adoption of IP-over-WDM (IPoWDM) architectures, coupled with the development of open standards such as OpenROADM and OpenConfig, has enabled seamless multi-layer control and management [7]. These innovations are essential to support emerging paradigms such as edge computing, virtualized services, and IBN, which prioritize agility, scalability, and user-centric operation [8,9].

AI and machine learning (ML) further enrich the capabilities of optical networks by enabling intelligent automation and enhanced decision-making [10,11]. From optimizing the quality of transmission (QoT) and controlling amplifiers to detecting soft failures and predicting network behavior, AI/ML applications are reshaping how networks are managed [10,11]. The integration of AI with SDN controllers and telemetry systems paves the way for zero-touch, autonomous network management, reducing operational complexity while enhancing performance and reliability [12]. Intent-based networking takes this a step further by abstracting user and business objectives into high-level intents, which are then translated into actionable network configurations and adjustments through AI-driven processes [13,14].

Despite these advancements, the progress toward fully autonomous optical networks is still paved with challenges. The heterogeneity of devices and protocols, the complexity of integrating packet and optical domains, and the energyintensive nature of AI-driven solutions need to be further investigated [15]. Additionally, the lack of standardization across vendor implementations and the scarcity of realworld data for ML model training limit the scalability and interoperability of current systems [16].

This paper investigates the state-of-the-art techniques that define modern approaches for optical network control and management, including SDN architectures, telemetry services, packet-optical integration, and the role of AI/ML. We explore the implications of these technologies, their integration within frameworks like OpenOSDK and hierarchical SDN architectures, and their potential to address pressing challenges such as scalability, energy efficiency, and operational complexity [17,18]. Moreover, we highlight the role of telemetry-enabled data collection for ML training, the potential of intent-driven management for achieving operational goals, and the need for standardization to foster interoperability in multi-vendor environments [19]. Through this analysis, the paper aims to provide a roadmap for the future of optical networking, emphasizing the critical interplay of programmability, intelligence, and automation also by addressing the gaps in existing solutions.

The rest of this paper is organized as follows. Section 2 presents an overview on how SDN can be empowered by YANG/NETCONF modeling, the concept of OpenSDK, and the practical implementation of SDN controllers. In Section 3, telemetry approaches are presented, discussing both out-of-band and in-band telemetry techniques. In Section 4, we introduce the control techniques for modern packet/optical networks, and in Section 5, we elaborate on the intent-based networking concept. Section 6 reviews some innovative AI/ML applications for network control optimization. Finally, we summarize this paper in Section 7.

## 2. SDN EMPOWERED BY OPEN MODELING

SDN has emerged in the last years as a possible solution to control optical networks. In this architecture, the SDN controller is the central entity devoted to the management of the entire network. By exploiting a dedicated control plane channel, the SDN controller is in charge of maintaining an up-to-date topology and performing the nodes configuration.

In traditional optical SDN architecture, the SDN controller is also responsible for routing and spectrum assignment (RSA) computation, but the recent trend, in order to achieve an accurate QoT assessment, is to delegate the RSA computation to specific components that also can provide the assignment of other parameters, such as the transmission power and the modulation format (i.e., digital-twin [20]). This solution allows for the effective evaluation of the physical impairments impact before the activation of a new lightpath, leveraging advanced heuristics and models.

Different protocols have been exploited in the years for the communication among the SDN controller and optical devices.

### A. YANG/NETCONF

The most suitable solution is based on the adoption of the NETCONF protocol for the exchange of XML messages structured according to specific YANG models. In particular, the NETCONF protocol offers the important benefit of not working at the protocol level (encoding/decoding of specific fields), without requiring extension, but to support the adoption of representation models. In this way, the scientific community has put a lot of effort on the definition of models capable of abstracting the capability of optical nodes. The need of more efficient solution has foreseen the adoption of telemetry protocols (e.g., gRPC/gNMI) in the control plane, with the scope of reducing the transmission overhead, while enabling new advanced functionalities.

In recent years, the need of the operators has pushed the adoption of the network disaggregation paradigm, where heterogeneous nodes (with elements/components provided by different vendors) can co-exist in the same network and need to be controlled by the same SDN controller.

This has led to different initiatives, driven by different telco operators in the format of working groups, with the scope to define and design clear models and procedures to be adopted by an SDN controller for the control and monitoring of optical nodes.

Open ROADM was established by a group of telecommunications providers, equipment vendors, and other stakeholders. The primary goal is to enable interoperability between optical equipment from different vendors, fostering a more open and cost-efficient optical network ecosystem.

The main Open ROADM targets are as follows: (i) the interoperability: defining standardized interfaces and protocols to ensure seamless integration of equipment from various vendors; (ii) open and programmable: enables the

![](_page_2_Picture_3.jpeg)

Fig. 1. SDN control and telemetry for AI-driven autonomous optical networking.

use of SDN controllers with open APIs and models (YANG and NETCONF); (iii) disaggregated architecture: separates network functions into modular components, such as transponders, ROADMs, and amplifiers, rather than relying on monolithic systems; and (iv) standardization: providing detailed specifications for ROADMs, transponders, and amplifiers, covering parameters like wavelengths, signal formats, and physical interfaces.

OpenConfig is an initiative for network management that provides a vendor-neutral, open-source model for configuring and operating network devices. It is a collaborative effort led by network operators, aiming to simplify and unify the way network equipment is configured and monitored.

The main OpenConfig targets are as follows: (i) vendorneutral data models: OpenConfig uses YANG to define standardized models for network device configuration and telemetry. These models abstract vendor-specific implementations, allowing operators to manage diverse hardware using a unified approach; (ii) focus on interoperability: designed to work across multiple vendors and platforms, reducing the need of proprietary management systems; (iii) programmatic interface: OpenConfig supports gNMI (gRPC network management interface), a modern protocol for streaming telemetry and configuration management; (iv) streaming telemetry: provides a scalable and real-time method for monitoring network state; and (v) modular design: the models are modular, making it easier to adapt to new use cases or extend functionality as network technology evolves.

The presence of multiple independent initiatives (OpenROADM, OpenConfig, and others) has led to the definition of isolated data models, with only few vendors supporting them in real systems. In some cases, the models are well designed, but no clear procedures are described, leaving the possibility to different interpretation and implementation of the models. This has led to a lack of interoperability, even under the same initiative. Finally, even if a standard control plane is designed, operators rely on proprietary SDN controllers to fully exploit advanced functionalities of the SDN agents, which are not available with standard YANG models.

Figure 1 shows the current state-of-the-art of the SDN control of optical networks, encompassing telemetry and AI-assisted re-optimization, following the framework of the zero-touch networking.

### B. OpenSDK

Considering the aforementioned limitations, new research initiatives are emerging, proposing alternative ways to exploit optical network disaggregation. With the term OpenOSDK, the open optical software development kit is considered, enabling third-party tools and resources to run on the heterogeneous hardware elements. This solution leverages the integration of different modules, supporting microservices (pods or containers) running on an operating system [i.e., SONiC Operating System (OS)], with the hardware. This integration is achieved by means of standard tools (i.e., SDK) to control and manage the underlying optical hardware components of a network element.

By adopting OpenOSDK, the control of heterogeneous hardware is guaranteed by standardized SDKs in a vendorneutral way. In fact, no constraints/limitations are conceived at the southbound interface among the SDN controller and the network element, hosting the SDN agent, where any even proprietary solution can be exploited. The main innovation of OpenOSDK is the possibility to deploy AI-integrated SDN-controlled modules at the network element, allowing

![](_page_3_Figure_3.jpeg)

Fig. 2. OpenOSDK scenario.

efficient re-optimization, exploiting local and remote monitoring. All the work performed by disaggregation initiatives can be a valid starting point for the modeling of the network elements, i.e., maintaining state and config parameters by OpenROADM/OpenConfig.

Figure 2 shows the evolution of the SDN approach from a standard NETCONF/gRPC/YANG schema to an OpenOSDK approach. On the left side, the traditional approach is reported with standard agent exposing NETCONF-based APIs toward the SDN controller. Each vendor is in charge of implementing the SDN agent. Where a multi-vendor scenario is considered, different SDN agents are exploited. On the right side of the figure, the OpenOSDK scenario is shown, where any southbound interface (standard or proprietary) can be exploited to realize the communication among the SDN controller and the network element. There, cloud-native modules, with advanced capability (i.e., AI) can rely on the OpenOSDK interface to perform the collection of data and the (re-)configuration of the devices.

## C. SDN Controllers

From the perspective of SDN controllers, various open-source initiatives have emerged over recent years to design and implement effective controller software, targeting flexibility, scalability, and reliability. Today, there are at least three widely recognized transport controller frameworks.

The first is based on the OpenDaylight open-source controller (e.g., TransportPCE), which is fully compatible with OpenROADM modeling, offering robust stability and extensively tested routines. The framework combines the path computation capability, with topology and multi-domain/multi-layer capability.

The second option is the Open Network Operating System (ONOS), an open-source framework built for reliability and scalability, supporting both OpenConfig and OpenROADM models. This software was designed to target distributed and reliable control plane architecture. By combining an intent approach with different drivers, packet and optical layers are controlled, supporting the execution of ad-hoc defined applications.

More recently, a third option, the TeraFlowSDN controller, has been introduced. Although the control of optical network is not the main focus of the framework, the main scope of this initiative is to support a cloud-native controller implementation, supporting a micro-services modular approach. In the last years, this framework has been extended to manage optical devices and features an initial implementation supporting the OpenConfig model.

To manage a multi-layer network encompassing both optical and packet domains, a hierarchical architecture is typically employed. In this setup, child controllers (such as an IP controller and an optical controller) are coordinated by a parent controller, which oversees the end-to-end workflow.

## 3. TELEMETRY SERVICES

Packet-optical telemetry will play a key role in next-generation network management by providing detailed, real-time insights into the performance and health of network components, and massive data sources for AI training. Telemetry services leverage advanced southbound frameworks, such as NETCONF/YANG, to facilitate seamless communication between controllers and network devices. These frameworks are enhanced by open models like OpenConfig/gNMI and OpenROADM, which establish standardized data models and interfaces for managing diverse optical network elements. Due to open initiatives, software-defined networking (SDN) controllers, open line system (OLS) controllers, and disaggregated node controllers can be equipped to dynamically configure and activate telemetry service to retrieve inline streams of timeseries samples of packet-optical parameters. These parameters, in the pure optical domain, originate from various network components, including optical cards and pluggables, reconfigurable optical add-drop multiplexers (ROADMs), optical cross-connects (OXCs), and line amplifiers [3]. The disaggregation framework amplifies the degree of freedom of telemetry configurability.

By enabling telemetry activation, operators can gain continuous visibility into the state of their optical networks, such as power levels, signal quality metrics, and fault conditions. This capability allows for automatic collection of data lakes and datasets for AI training, proactive management, automation, and optimization of network performance, aligning with the demands of high-capacity, low-latency services. Additionally, the use of open standards ensures interoperability across multi-vendor environments, driving innovation and reducing operational complexity in packet-optical networking.

#### A. Out-of-Band Telemetry

Quality of transmission (QoT) telemetry for optical connections and monitoring data retrieval at the pure optical domain is commonly carried out using out-of-band network telemetry (ONT), which involves the transmission of monitoring and performance data over separate channels rather than through the same channel used for the network traffic. In this context, ONT utilizes control or dedicated channels to relay information about the status and quality of optical signals, such as signal-to-noise ratio (SNR), bit error rate (BER), and power levels.

Classical telemetry, exploited by operators to monitor QoT, can rely on legacy systems employing optical channel monitors (OCMs) at the link level and optical supervisory channels (OSCs) at the lightpath level. This type of monitoring can be performed while the network and the services are in operation. In addition, optical time domain reflectometer (OTDR) measurements can be exploited to quickly diagnose fiber/connector faults. In most cases, this type of monitoring requires interruption of the link/path operation and it is very suitable for hard failures recovery (e.g., localization of fiber cuts). All such methods, historically separated from the network control, are being integrated, handled, and automatized in ONT driven by SDN through on-demand metadata streaming, thanks also to disaggregation and open models.

This approach provides the isolation of telemetry data from the main traffic, ensuring that monitoring processes do not interfere with the actual data being transmitted. In practical implementations, out-of-band telemetry is instrumental in enabling advanced network management functions such as fault detection, performance optimization, and predictive maintenance [7]. It supports the operation of controllers by providing a steady stream of telemetry data, which is critical for making informed decisions about network configurations and adjustments. This separation of monitoring traffic enhances the scalability and manageability of optical networks, particularly in high-capacity scenarios where minimizing disruptions is essential.

The challenges of network automation and failure management, particularly in handling the vast amounts of fine-granularity telemetry data required for performance monitoring and service quality assurance, are effectively addressed by adopting novel distributed intelligence architectures with specialized data aggregation techniques, as discussed in Ref. [12]. This approach significantly reduces data volumes by up to three orders of magnitude—while preserving the accuracy and timeliness needed for effective network automation and fault detection. Hard and soft failure detection and localization, and in general anomaly detection of optical performance KPI at the card/amplifier level has become feasible by relying on telemetry cross-correlation and analysis, thanks also to vertical monitoring platforms such as Kafka, providing distributed and modular publish-subscribe platform and enabling configurable telemetry sharing among different management entities [21,22]. ONT may also be realized horizontally, exploiting the communication between device agents, and realizing peer-topeer relationships [4]. In this way, intelligent device agents may take local decisions (in the future driven by local AI engines), based on telemetry data received by agents related to shared channels parameters, thus alleviating the central controller and speeding up the re-optimization procedure. Finally, to enable third-party data analytics (i.e., for tenants, sliced networking, or multi-stakeholder scenarios), optical telemetry streams encoding/decoding techniques have been proposed to ensure accurate machine learning classification while preserving the operator confidential data [19].

# B. In-Band Telemetry

In scenarios involving wavelengths activated between pluggable optics hosted in programmable packet-optical switches, in-band network telemetry (INT) is emerging as a viable and powerful approach. Unlike ONT, which relies on separate control or dedicated channels, INT embeds telemetry data directly within the same data path as the user traffic. This method allows for real-time collection and analysis of telemetry information, conveyed as protocol extra-headers, without requiring additional parallel communication channels. Data plane programmability plays an essential role to enable custom headers, parsers, and additional metadata processing, thanks to emerging languages such as P4 and data plane backends and development kits such as eBPF, XDP, and DPDK.

As illustrated in Ref. [23] (see Fig. 1), INT is particularly well-suited to use in cases where rapid response to anomaly telemetry patterns is essential. By enabling fast, localized in-band control mechanisms, INT ensures that issues such as soft failures—minor degradations in the optical signal are detected and addressed promptly within the pipeline of the packet-optical node itself, thanks to data plane programmability. This capability is critical in modern, high-speed networks, where even brief delays in reacting to faults can impact service quality. For instance, INT enables real-time monitoring of key parameters like signal integrity and optical power levels, triggering immediate corrective actions to mitigate potential service disruptions. Additionally, the integration of telemetry and traffic in the same data path simplifies network management by reducing reliance on external telemetry channels, leading to a more efficient and scalable architecture for packetoptical networks. Finally, programmable INT opens the way to multi-layer and multi-segment dynamic optimization, up to the application layer. By encoding telemetry data related to different layers in the same packet headers, it is possible to implement extremely fast local policies, e.g., in the context of packet-optical infrastructure for the edge continuum and taking into account real-time edge parameters [24,25].

### C. Telemetry Trends and Perspectives

The evolution toward programmable packet-optical nodes is driving a transformative shift in network control and management paradigms. In our vision, the next generation of control frameworks will break the rigid limitations of traditional NETCONF/YANG-based systems, moving toward a unified programmable model environment. This advanced layer will enable the massive and decentralized streaming of joint control and telemetry messages, continuously supported by AI-driven insights. This paradigm shift includes the integration of novel management and application frameworks that leverage explainable and generative AI tools, as well as APIs designed for intuitive human-to-system interaction. For instance, ChatGPT-like bots will allow operators to issue highlevel semantic commands, which can be dynamically translated into precise control plane operations and telemetry streams. This innovation simplifies complex network interactions, empowering operators with greater efficiency and contributing to a substantial reduction in operational complexity and costs (OPEX).

## 4. CONTROL OF PACKET/OPTICAL NETWORKS

The advent of coherent pluggable transceivers, now capable of delivering 800G and beyond, even in compact QSFP-DD form factors, has accelerated the adoption of IP over wavelength division multiplexing (IPoWDM) solutions. In this

![](_page_5_Figure_3.jpeg)

Fig. 3. (a) Traditional multi-layer scenario. (b) Pluggable-based IPoWDM scenario.

continuously evolving scenario, the optical internetworking forum (OIF) has standardized the Common Management Interface Specification (CMIS), further extending it to digital coherent modules (DCO) through C-CMIS (Coherent CMIS). This interface enables the initialization and control of optical modules, covering the gap on the critical mapping between routers and coherent pluggable transceivers.

The introduction of IPoWDM brings significant advantages while presenting new challenges for network management. On one hand, it removes the need for traditional transponders and muxponder devices, offering reduced capital expenditures (CAPEX), lower latency by eliminating intermediary equipment, reduced power consumption, and simpler processes for planning, installation, and maintenance due to fewer network components. On the other hand, IPoWDM demands the creation of advanced SDN architectures to facilitate integrated management of IP and optical resources. In Fig. 3(a), IP and WDM systems have operated in silos, each managed by dedicated controllers, considering packet or optical resources coordinated by a parent entity.

To address these challenges, the Telecom Infra Project (TIP) has introduced the MANTRA (Metaverse-Ready Architectures for Open Transport) initiative, which aims to define a holistic hierarchical control architecture for multilayer networks, including the use of IPoWDM nodes. In recent studies [17,26], two distinct SDN architectures—dual and single—were proposed [see Fig. 3(b)]. In both designs, only the IP controller is authorized to perform the configuration of the IPoWDM nodes and pluggable transceivers.

In the single architecture, the IPoWDM boxes are fully controlled by the SDN packet controller, responsible for the complete configuration and monitoring of the element (including optical parameters of the pluggable transceivers), while the optical controller is responsible of the control and monitoring of the OLS (e.g., ROADMs and amplifiers). The yellow dotted line of the figure is not enabled. In the dual architecture, the main change consists on the activation of an additional control plane channel (e.g., the yellow dotted line in the figure), where the optical controller is granted read access to gather fundamental information from the environment for taking the appropriate decisions.

Both architectures utilize a parent controller in coordination with an IP controller and an optical controller.

Demonstrations of the MANTRA architecture, as described in Ref. [18], highlighted the setup of point-to-point connectivity services while characterizing 400 ZR/ZR+ coherent pluggable transceivers in terms of their tunability. The results emphasized the critical importance of traffic recovery in multi-layer networks employing IPoWDM nodes. While the proposed solutions were successfully validated, they also revealed notable complexity, underscoring the need for further refinement and optimization.

## 5. ROLE OF IBN IN OPTICAL NETWORKS

Intent-based networking (IBN) is a modern approach that enables flexible and loosely coupled interactions between users and network operators. It allows users to express their desired operational goals in intuitive terms (e.g., using natural language), while allowing the network operating system to determine the best way to achieve those goals through its own optimization processes [13]. IBN can play an evolutionary role in the management of optical networks by allowing network administrators to manage and configure complex optical infrastructures based on high-level business or operational intents rather than low-level commands [8].

In fact, several aspects can be improved in the optical network management that span from automated and dynamic configuration to proactive network optimization and resilience. More specifically, IBN enables optical networks to be configured and optimized automatically based on the expressed intents, such as achieving low-latency routes, maximizing bandwidth, or prioritizing specific data flows. Instead of manually configuring numerous parameters on each optical device, the intent layer interprets high-level intents and automatically generates the required configurations, significantly reducing setup time and human error. IBN can also contribute to the improvement of optical networks performance by continuously monitoring network conditions (e.g., through telemetry) and autonomously making adjustments to meet defined performance goals. As part of its assurance operations, if a link, e.g., begins experiencing increased error rates or latency or there is a fiber degradation, the IBN system can reroute traffic or adjust signal parameters to maintain quality of service. In this way, continuous validation processes allow to assure that network behavior strictly aligns with service requirements throughout the entire intent lifecycle [14].

Finally, IBN can be easily integrated with SDN controllers, where high-level intent abstraction and SDN's programmable control plane can together allow networks to become more adaptive, responsive, and aligned with business requirements [9]. In fact, the intent layer interprets the intents and translates them into actionable instructions for the SDN controller. The SDN controller then takes these instructions and programs

![](_page_6_Figure_3.jpeg)

Fig. 4. Intent-based networking—key concepts.

the underlying optical network devices accordingly, handling lower-level details like adjusting wavelengths, configuring modulation formats, and setting up optical paths. Based on the real-time telemetry data, if the network conditions change (e.g., increased latency or degradation on an optical link), the SDN controller detects this and informs the IBN layer. Consequently, the IBN system can re-evaluate the intents and direct the SDN controller to make necessary adjustments, such as rerouting traffic, allocating more bandwidth, or dynamically configuring new optical paths.

Figure 4 illustrates the concept of intent-based networking (IBN) and its key components. IBN is shown as a centralized system integrating analytics, policy, and automation. Telemetry collects real-time data from the network and feeds it into the analytics module. Analytics processes these data to ensure the network's behavior meets predefined intents. Policy defines high-level rules and objectives, which are translated into actionable configurations. Translation converts user intents into specific instructions for the network. Assurance validates that the network operates as intended, adapting dynamically. Below the IBN framework, context flows from the network infrastructure (devices, servers, and base stations) into IBN, and activation flows back to configure the underlying systems, enabling automation, scalability, and real-time adaptation.

# 6. AI/ML IN OPTICAL NETWORKS

AI and ML are being investigated to empower the control and management of optical networks. AI is a wide field of computer science spanning from *search methods*, *optimization theory*, *game theory*, *statistical models*, etc. to *ML* [10]. In particular, ML is a powerful tool when the modeling of a specific phenomenon is particularly complex, since ML intrinsically learns relations among training data. As an example, AI techniques (e.g., tabu search algorithms, genetic algorithms, game theory) have been studied in optical networks to optimize resource allocation [27–29]. Then, other AI techniques as statistical models (e.g., Bayesian networks and hidden Markov models) have been applied to failure identification [30] or quality of service management [31]. This section will be mainly focused on recent advances in ML applications; for a more generic overview of AI applications, the reader can refer to Ref. [10].

Several use cases for the adoption of ML have been identified [11], mainly including QoT estimation/prediction, device control (amplifiers), (soft-)failure management, traffic prediction, and resource allocation. ML applied to QoT estimation and prediction has been investigated in the literature [32,33], e.g., in the context of digital twin (DT) formulations [33]. In parallel, transmission performance models have reached good performance in several data plane scenarios (e.g., C-band transmission): the Gaussian Noise model [34] and its extensions (e.g., the Generalized Gaussian Noise Model) have been widely accepted—e.g., by industrial players within the Telecom Infra Project (TIP)—and also tested [35] by the optical community. Thus, given the availability of enough-quality transmission models, ML might also be used to complement these models to reduce margins and to estimate the input parameters to feed analytical expressions [16,36,37], as physical parameter values typically differ between the reality and the datasheet (even due to ageing effects).

Regarding the control of data plane devices, ML can be adopted to characterize the complex behavior of devices, such as amplifiers [38–43]: erbium-doped-fiber amplifiers (EDFAs), Raman amplifiers, and thulium-doped fiber amplifiers (TDFAs). ML has been proven to be suitable to characterize the EDFA gain spectrum [41] or to set the amplifier pumps in order to optimize the amplifier performance, e.g., for a Raman amplifier [40] or for a TDFA [43].

(Soft-)failure management is another field of application for ML [44]: e.g., it can be exploited for failure prediction [45– 47], identification [48–51], localization [50,52–55], and for alarm suppression. Regarding identification, which is typically a classification problem, some failures occur more frequently than others. Consequently, data collected from real networks to train ML models are imbalanced among classes limiting ML performance, as shown in Ref. [51], where data were collected for seven months on an operating network. However, data augmentation techniques [49] can mitigate data class imbalance, improving ML performance. Regarding failure localization, models can combine path correlations among failed lightpath together with a statistical evaluation of the failure probability of each link [52,54], particularly useful to disambiguate complex failure scenarios [54]. Then, a critical event can raise flood of alarms in network management system and alarm clustering [56] simplifies the management of alarms by grouping related ones together. ML can assist alarm suppression.

Reinforcement learning (RL) and deep reinforcement learning (DRL) have been applied for resource allocation (routing and spectrum assignment) [57,58]. It has been shown that RL and DRL can achieve good performance, although valid heuristics could be adopted.

ML can also be integrated across the entire life cycle of intent-based networking, enhancing its functionalities, adaptability, and efficiency [5,8]. More specifically, ML plays an important role in intents classification by accurately interpreting user intents and mapping them to appropriate network policies [59]. Natural language processing (NLP) techniques, such as supervised learning and deep learning models, enable the system to analyze textual or structured inputs, classify intents, and translate them into actionable configurations [60]. This automation reduces manual intervention, enhances accuracy, and ensures that network behavior aligns with business objectives. Regarding assurance operations, by analyzing real-time telemetry data, ML models can predict failures, detect anomalies, and optimize network performance without manual intervention [61]. Moreover, supervised learning helps classify traffic patterns, while unsupervised learning identifies deviations and clusters similar behaviors [62]. Overall, ML empowers IBN with intelligence, making networks more autonomous, resilient, and responsive to changing demands, though challenges such as model interpretability and the need for continuous retraining remain.

In general, ML applied to the control and management of optical networks is still under investigation. However, there are relevant limitations for a full awareness of the realistic use cases: data from real networks to feed research activities are scarce because of confidentiality reasons; lab setups can hardly reflect the behavior of a real network given the environment under control (e.g., improbable realistic fiber stresses), a limited number of channels, the setup dimensions, and the reduced observation time windows they are available. However, lab trials have provided anyway interesting insights, as shown by the state of the art. Probably, the most promising applications (summarized in Table 1) for ML are (i) QoT estimation joining transmission modeling and ML; (ii) control of amplifiers; (iii) (soft-)failure and alarm management; and (iv) IBN.

Moreover, besides telco applications, optical fibers can act as environmental sensors: strain, temperature, and pressure sensing through fibers have attracted interest in the last tens of years. Optical fiber sensors may find use in seismic applications [63–65], for structural health monitoring (e.g., bridges, railways) [66,67], or security against physical intrusions [68]. A relevant advantage is that deployed network infrastructures can be also used as distributed sensors alongside data transmission [65]. Even in the field of optical fiber sensing, AI/ML is widely under investigation (e.g., Refs. [69–71]) with possible uses for events prediction, detection, classification, and localization [64,69,70].

Finally, a dissertation should also be deserved to the increased complexity (and thus power consumption) introduced by AI/ML. In March 2024, during a symposium on energy consumption at the Optical Fiber Communications Conference and Exhibition, industrial players highlighted that

Table 1. Possible Applications for ML in Optical Networks

| Application                      | Literature |
|----------------------------------|------------|
| ML refining QoT modeling         | [16,36,37] |
| Amplifier control                | [38–43]    |
| (Soft-)failure identification    | [48–51]    |
| Failure localization             | [50,52–55] |
| Failure prediction               | [45–47]    |
| Alarm clustering and suppression | [56]       |
| Intent-based networking          | [8]        |
| Sensing                          | [69–71]    |

![](_page_7_Figure_9.jpeg)

Fig. 5. Neurons' activity in a neural-network-based classification problem upon Bayesian optimization.

AI/ML-based data centers consume 10 times more of power than traditional data centers. Thus, the penetration of ML in optical networks may further increase power consumption (currently, the Information and Communication Technology counts for around 9% of the global electricity consume). Therefore, techniques to reduce ML complexity may be needed and investigated. In Ref. [15], the authors have shown that traditional neural-network optimization techniques—such as grid search, random search, and Bayesian optimization—focusing on accuracy maximization (e.g., F1-score optimization) finally may result in the under-utilization of neurons (thus, introducing unnecessary complexity). Figure 5 shows neurons' activity of a neural network during the inference phase of a classification problem (soft-failure identification) upon Bayesian optimization [15]: a huge number of neurons are inactive but they contribute to the neural-network complexity. The reduction of neural-network complexity is under investigation, some examples are pruning [72] and knowledge distillation (KD) [73]. Pruning consists of removing NN parameters: e.g., the connections' weights or biases that the NN learns during training. However, in general, only the weights are pruned, leaving the biases intact. Thus, pruning of a dense (i.e., fully connected) NN results in a sparse (i.e., with missing connections or neurons) NN and the more sparse the NN is, more performance degradations are experienced during inference phase. KD is a model compression method involving the transfer of knowledge from a high-complexity model, known as a teacher model, to a reduced-complexity model, designated as a student model [73]. In Ref. [15], the activity of neurons during the inference phase is monitored, and inactive neurons are iteratively removed until the accuracy (e.g., f1-score) is degraded below a certain threshold, achieving a complexity reduction of around 90%.

Thus, besides the issues of having access to data from real networks and identifying realistic use cases for ML applications, neural-network complexity reduction—which finally would result in lower energy consumption—should be also taken into account in order to keep the network sustainable.

## 7. CONCLUSION

The advancements in optical network control and management, driven by SDN, telemetry, and AI, represent a significant step forward in addressing the demands of modern, data-intensive applications. These innovations have demonstrated their potential to transform optical networks into more intelligent, automated, and adaptable infrastructures, capable of supporting the exponential growth in data traffic.

Through the exploration of SDN architectures, telemetry frameworks, and AI integration, this paper highlights key areas of progress and remaining challenges. SDN has emerged as a cornerstone for achieving programmability and flexibility, facilitating automation and interoperability across multivendor environments. Telemetry, with its ability to provide real-time, granular insights into network health, is instrumental in enabling proactive and predictive management. AI and ML further enhance these capabilities by enabling intelligent automation, predictive fault detection, and dynamic optimization of network resources.

However, the paper also highlights aspects that need more investigations. The lack of standardization in multi-vendor implementations and the complexity of integrating packet and optical domains continue to hinder seamless deployment. Furthermore, the scarcity of real-world data for AI model training limits the scope of current implementations, highlighting the need for collaborative efforts to create shared datasets and test environments.

Future optical network architectures must address these challenges by fostering open, interoperable ecosystems that leverage the strengths of SDN, telemetry, and AI. The adoption of frameworks such as OpenOSDK and hierarchical SDN architectures, combined with advancements in programmable nodes and intent-based networking, paves the way for zero-touch, autonomous network management. Additionally, integrating explainable AI and generative AI tools can further enhance human–machine collaboration, simplifying network operations while ensuring reliability and scalability.

Funding. Ministero dell'Università e della Ricerca (PE00000001 program "RESTART"), DIPE AIROBOTICS 2023-2027); HORIZON EUROPE Framework Programme (101096120).

# REFERENCES

- 1. Z. Li, Y. Zhao, Y. Li, et al., "Self-optimizing optical network with cloud-edge collaboration: architecture and application," IEEE Open J. Comput. Soc. 1, 220–229 (2020).
- 2. H. Song, G. Luo, and H. J. Chao, "Network telemetry: state-ofthe-art and research challenges," Commun. Surveys Tuts. 21, 1829–1853 (2019).
- 3. F. Paolucci, A. Sgambelluri, F. Cugini, et al., "Network telemetry streaming services in SDN-based disaggregated optical networks," J. Lightwave Technol. 36, 3142–3149 (2018).
- 4. F. Paolucci, A. Sgambelluri, M. Felipe Silva, et al., "Peer-to-peer disaggregated telemetry for autonomic machine-learning-driven transceiver operation," J. Opt. Commun. Netw. 14, 606–620 (2022).
- 5. A. Leivadeas and M. Falkner, "A survey on intent-based networking," Commun. Surveys Tuts. 25, 625–655 (2023).
- 6. M. Glick and J. E. Bowers, "Packet and optical convergence: technologies, architectures, and trends," IEEE Netw. 35, 252–259 (2021).
- 7. R. P. Pinto, K. S. Mayer, D. S. Arantes, et al., "Packet-optical differentiated survivability implemented by P4 slices and GNMI

- telemetry," in Optical Fiber Communications Conference and Exhibition (OFC) (2023), pp. 1–3.
- 8. L. Velasco, S. Barzegar, F. Tabatabaeimehr, et al., "Intent-based networking and its application to optical networks [invited tutorial]," J. Opt. Commun. Netw. 14, A11–A22 (2022).
- 9. B. Martini, M. Gharbaoui, and P. Castoldi, "Intent-based zero-touch service chaining layer for software-defined edge cloud networks," Comput. Netw. 212, 109034 (2022).
- 10. J. Mata, I. de Miguel, R. J. Duran, et al., "Artificial intelligence (AI) methods in optical networks: a comprehensive survey," Opt. Switching Netw. 28, 43–57 (2018).
- 11. F. Musumeci, C. Rottondi, A. Nag, et al., "An overview on application of machine learning techniques in optical networks," Commun. Surveys Tuts. 21, 1383–1408 (2019).
- 12. L. Velasco, P. Gonzalez, and M. Ruiz, "Distributed intelligence for pervasive optical network telemetry," J. Opt. Commun. Netw. 15, 676–686 (2023).
- 13. A. Clemm, L. Ciavaglia, L. Z. Granville, et al., "Intent-based networking - concepts and definitions," Internet Engineering Task Force, 2022, https://datatracker.ietf.org/doc/rfc9315/.
- 14. Y. Wei, M. Peng, and Y. Liu, "Intent-based networks for 6G: insights and challenges," Digital Commun. Netw. 6, 270–280 (2020).
- 15. L. Z. Khan, J. Pedro, O. Ayoub, et al., "Optimizing deep learningbased failure management in optical networks by monitoring relative neural activity," in International Conference on Optical Network Design and Modeling (ONDM) (2024), pp. 1–3.
- 16. E. Seve, J. Pesic, C. Delezoide, et al., "Learning process for reducing uncertainties on network parameters and design margins," J. Opt. Commun. Netw. 10, A298–A306 (2018).
- 17. A. Sgambelluri, D. Scano, R. Morro, et al., "Failure recovery in the MANTRA architecture with an IPoWDM SONIC node and 400ZR/ZR+ pluggables," J. Opt. Commun. Netw. 16, B26–B34 (2024).
- 18. R. Morro, E. Riccardi, D. Scano, et al., "First demonstration of MANTRA IPoWDM convergent SDN architecture using sonic white box and 400ZR/ZR+ pluggables," in International Conference on Optical Network Design and Modeling (ONDM) (2023).
- 19. M. F. Silva, A. Sgambelluri, A. Pacini, et al., "Confidentialitypreserving machine learning algorithms for soft-failure detection in optical communication networks," J. Opt. Commun. Netw. 15, C212–C222 (2023).
- 20. G. Borraccini, S. Straullu, A. Giorgetti, et al., "Experimental demonstration of partially disaggregated optical network control using the physical layer digital twin," IEEE Trans. Netw. Serv. Manage. 20, 2343–2355 (2023).
- 21. A. Sgambelluri, A. Pacini, F. Paolucci, et al., "Reliable and scalable kafka-based framework for optical network telemetry," J. Opt. Commun. Netw. 13, E42–E52 (2021).
- 22. S. Shen, J. Han, H. Li, et al., "Unified monitoring and telemetry platform for future intelligent optical networks," in 24th International Conference on Transparent Optical Networks (ICTON) (2024), pp. 1–5.
- 23. F. Cugini, C. Natalino, D. Scano, et al., "P4-based telemetry processing for fast soft failure recovery in packet-optical networks," in Optical Fiber Communications Conference and Exhibition (OFC) (2023), pp. 1–3.
- 24. I. Pelle, F. Paolucci, B. Sonkoly, et al., "Latency-sensitive edge/cloud serverless dynamic deployment over telemetrybased packet-optical network," IEEE J. Sel. Areas Commun. 39, 2849–2863 (2021).
- 25. I. Pelle, F. Paolucci, B. Sonkoly, et al., "P4-assisted seamless migration of serverless applications towards the edge continuum," Future Gener. Comput. Syst. 146, 122–138 (2023).
- 26. O. G. De Dios, J. Giménez, and S. Melin, "MANTRA whitepaper IPoWDM convergent SDN architecture - motivation, technical definition and challenges," in Telecom Infra Project White Paper (2022), Version 3.
- 27. R. Goscien, K. Walkowiak, and M. Klinkowski, "Tabu search algorithm for routing, modulation and spectrum allocation in elastic optical network with anycast and unicast traffic," Comput. Netw. 79, 148–165 (2015).

- 28. D. Monoyios and K. Vlachos, "Multiobjective genetic algorithms for solving the impairment-aware routing and wavelength assignment problem," J. Opt. Commun. Netw. 3, 40–47 (2011).
- 29. J. Zhu, B. Zhao, and Z. Zhu, "Leveraging game theory to achieve efficient attack-aware service provisioning in EONs," J. Lightwave Technol. 35, 1785–1796 (2017).
- 30. M. Ruiz, F. Fresi, A. P. Vela, et al., "Service-triggered failure identification/localization through monitoring of multiple parameters," in 42nd European Conference on Optical Communication (ECOC) (2016).
- 31. K. Chitra and M. R. Senkumar, "Hidden Markov model based lightpath establishment technique for improving QoS in optical WDM networks," in 2nd International Conference on Current Trends In Engineering and Technology (ICCTET) (2014), pp. 53–62.
- 32. M. Ibrahimi, H. Abdollahi, C. Rottondi, et al., "Machine learning regression for QoT estimation of unestablished lightpaths," J. Opt. Commun. Netw. 13, B92–B101 (2021).
- 33. D. Sequeira, M. Ruiz, N. Costa, et al., "OCATA: a deep-learningbased digital twin for the optical time domain," J. Opt. Commun. Netw. 15, 87–97 (2023).
- 34. P. Poggiolini, G. Bosco, A. Carena, et al., "The GN-model of fiber non-linear propagation and its applications," J. Lightwave Technol. 32, 694–721 (2014).
- 35. A. Nespola, S. Straullu, A. Carena, et al., "GN-Model validation over seven fiber types in uncompensated PM-16QAM Nyquist-WDM links," IEEE Photon. Technol. Lett. 26, 206–209 (2014).
- 36. C. Delezoide, K. Christodoulopoulos, A. Kretsis, et al., "Field trial of marginless operations of an optical network facing ageing and performance fluctuations," in European Conference on Optical Communication (ECOC) (2018), pp. 1–3.
- 37. N. Morette, I. F. de Jauregui Ruiz, H. Hafermann, et al., "On the robustness of a ML-based method for QoT tool parameter refinement in partially loaded networks," in Optical Fiber Communication Conference (OFC) (2022), pp. 1–3.
- 38. M. Ionescu, A. Ghazisaeidi, and J. Renaudier, "Machine learning assisted hybrid EDFA-Raman amplifier design for C+L bands," in European Conference on Optical Communications (ECOC) (2020).
- 39. M. P. Yankov, F. Da Ros, U. C. de Moura, et al., "Flexible Raman amplifier optimization based on machine learning-aided physical stimulated Raman scattering model," J. Lightwave Technol. 41, 508–514 (2023).
- 40. D. Zibar, A. M. Rosa Brusin, U. C. de Moura, et al., "Inverse system design using machine learning: the Raman amplifier case," J. Lightwave Technol. 38, 736–753 (2020).
- 41. M. P. Yankov, U. C. de Moura, and F. D. Ros, "Power evolution modeling and optimization of fiber optic communication systems with EDFA repeaters," J. Lightwave Technol. 39, 3154–3161 (2021).
- 42. G. Marcon, A. Galtarossa, L. Palmieri, et al., "Model-aware deep learning method for Raman amplification in few-mode fibers," J. Lightwave Technol. 39, 1371–1380 (2021).
- 43. M. Radovic, A. Sgambelluri, N. Sambo, et al., "Neural networkbased control of TDFA," in International Conference on Optical Network Design and Modeling (ONDM) (2024).
- 44. F. Musumeci, C. Rottondi, G. Corani, et al., "A tutorial on machine learning for failure management in optical networks," J. Lightwave Technol. 37, 4125–4139 (2019).
- 45. T. B. Anderson, A. Kowalczyk, K. Clarke, et al., "Multi impairment monitoring for optical networks," J. Lightwave Technol. 27, 3729–3736 (2009).
- 46. D. Rafique, T. Szyrkowiec, A. Autenrieth, et al., "Analytics-driven fault discovery and diagnosis for cognitive root cause analysis," in Optical Fiber Communications Conference and Exposition (OFC) (2018), pp. 1–3.
- 47. M. F. Silva, A. Pacini, A. Sgambelluri, et al., "Learning long- and short-term temporal patterns for ML-driven fault management in optical communication networks," IEEE Trans. Netw. Serv. Manage. 19, 2195–2206 (2022).
- 48. B. Shariati, M. Ruiz, J. Comellas, et al., "Learning from the optical spectrum: Failure detection and identification," J. Lightwave Technol. 37, 433–440 (2019).

- 49. L. Z. Khan, J. Pedro, N. Costa, et al., "Data augmentation to improve performance of neural networks for failure management in optical networks," J. Opt. Commun. Netw. 15, 57–67 (2023).
- 50. J. Babbar, A. Triki, R. Ayassi, et al., "Machine learning models for alarm classification and failure localization in optical transport networks," J. Opt. Commun. Netw. 14, 621–628 (2022).
- 51. C. Tremblay, A. Mahmoudialami, P. A. Ngani Sigue, et al., "Detection and root cause analysis of performance degradation in optical networks using machine learning," in 49th European Conference on Optical Communications (ECOC) (2023), pp. 1278–1281.
- 52. T. Panayiotou, S. P. Chatzis, and G. Ellinas, "Leveraging statistical machine learning to address failure localization in optical networks," J. Opt. Commun. Netw. 10, 162–173 (2018).
- 53. K. S. Mayer, R. P. Pinto, J. A. Soares, et al., "Demonstration of MLassisted soft-failure localization based on network digital twins," J. Lightwave Technol. 40, 4514–4520 (2022).
- 54. C. Delezoide, P. Ramantanis, and P. Layec, "Streamlined failure localization method and application to network health monitoring," J. Lightwave Technol. 41, 6119–6125 (2023).
- 55. S. Behera, T. Panayiotou, and G. Ellinas, "Machine learning framework for timely soft-failure detection and localization in elastic optical networks," J. Opt. Commun. Netw. 15, E74–E85 (2023).
- 56. D. Maillot-Tchofo, A. Triki, M. Laye, et al., "Clustering of live network alarms using unsupervised statistical models," in 49th European Conference on Optical Communications (ECOC) (2023), pp. 1246–1249.
- 57. N. E. D. E. Sheikh, E. Paz, J. Pinto, et al., "Multi-band provisioning in dynamic elastic optical networks: a comparative study of a heuristic and a deep reinforcement learning approach," in International Conference on Optical Network Design and Modeling (ONDM) (2021), pp. 1–3.
- 58. A. Terki, J. Pedro, A. Eira, et al., "Deep reinforcement learning for resource allocation in multi-band optical networks," in International Conference on Optical Network Design and Modeling (ONDM) (2024).
- 59. A. T. Al-Tuama and D. A. Nasrawi, "Intent classification using machine learning algorithms and augmented data," in International Conference on Data Science and Intelligent Computing (ICDSIC) (2022), pp. 234–239.
- 60. R. Caldelli, P. Castoldi, M. Gharbaoui, et al., "On helping users in writing network slice intents through NLP and user profiling," in IEEE 9th International Conference on Network Softwarization (NetSoft) (2023), pp. 545–550.
- 61. X. Zheng and A. Leivadeas, "Network assurance in intent-based networking data centers with machine learning techniques," in 17th International Conference on Network and Service Management (CNSM) (2021), pp. 14–20.
- 62. T. T. Nguyen and G. Armitage, "A survey of techniques for internet traffic classification using machine learning," Commun. Surveys Tuts. 10, 56–76 (2008).
- 63. M. Cantono, J. C. Castellanos, S. Batthacharya, et al., "Optical network sensing: opportunities and challenges," in Optical Fiber Communications Conference and Exhibition (OFC) (2022), pp. 1–3.
- 64. M. Cantono, J. C. Castellanos, V. Kamalov, et al., "Seismic sensing in submarine fiber cables," in European Conference on Optical Communication (ECOC) (2021).
- 65. A. M. R. Brusin, G. Rizzelli, M. Fasano, et al., "Overview and analysis of optical sensing techniques over deployed telecom networks," in 24th International Conference on Transparent Optical Networks (ICTON) (2024), pp. 1–4.
- 66. D. Anastasopoulos, G. De Roeck, and E. P. Reynders, "One-year operational modal analysis of a steel bridge from high-resolution macrostrain monitoring: influence of temperature vs. retrofitting," Mech. Syst. Sig. Process. 161, 107951 (2021).
- 67. C. Du, S. Dutta, P. Kurup, et al., "A review of railway infrastructure monitoring using fiber optic sensors," Sens. Actuators A 303, 111728 (2020).
- 68. G. Allwood, G. Wild, and S. Hinckley, "Optical fiber sensors in physical intrusion detection systems: a review," IEEE Sens. J. 16, 5497–5509 (2016).

- 69. P. D. Hernández, J. A. Ramírez, and M. A. Soto, "Deep-learningbased earthquake detection for fiber-optic distributed acoustic sensing," J. Lightwave Technol. 40, 2639–2650 (2022).
- 70. A. Venketeswaran, N. Lalam, J. Wuenschell, et al., "Recent advances in machine learning for fiber optic sensor applications," Adv. Intell. Syst. 4, 2100067 (2022).
- 71. U. Jayawickrema, H. Herath, N. Hettiarachchi, et al., "Fibre-optic sensor and deep learning-based structural health monitoring
- systems for civil structures: a review," Measurement 199, 111543 (2022).
- 72. E. Diao, G. Wang, J. Zhang, et al., "Pruning deep neural networks from a sparsity perspective," in 7th International Conference on Learning Representations (2023).
- 73. J. H. Cho and B. Hariharan, "On the efficacy of knowledge distillation," in IEEE/CVF International Conference on Computer Vision (2019), pp. 4794–4802.
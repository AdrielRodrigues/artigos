---
title: "Convergence of Networking and Cloud/Edge Computing: Status, Challenges, and Opportunities"
tema_principal: projeto_universal
temas_relacionados: []
pdf: ../pdf/convergence_of_networking_and_cloud_edge_computing_status_challenges_and_opportunities.pdf
---

## Convergence of Networking and Cloud/Edge Computing: Status, Challenges, and Opportunities

Qiang Duan, Shangguang Wang, and Nirwan Ansari

## Abstract

The wide applications of virtualization and service-oriented principles in various emerging networking technologies introduce a trend of network cloudification that enables network systems to be realized based on cloud technologies and allows network services to be provisioned following the cloud service model. Network cloudification together with the critical role of networking in the latest cloud/edge computing technologies leads to the convergence of networking and cloud/edge computing, which calls for a holistic vision across the fields of networking and computing that may shape relevant technology developments. In this article, we attempt to sketch a big picture to reflect the current status of on-going research toward network-cloud/edge convergence. We first describe the notion of such convergence and present an architectural framework for converged network-cloud/edge systems. Then, we survey the state of the art of enabling technologies for network-cloud/edge convergence by reviewing recent progress in relevant standardization and technology developments in representative research projects. We also discuss challenges that must be fully addressed for realizing the convergence of networking and cloud/ edge computing and identify some opportunities for future research in this exciting interdisciplinary field.

## Introduction

A main technical strategy employed by the networking research community for building the future Internet lies in leveraging the virtualization and service-oriented principles in network architecture and service models. Virtualization, which essentially separates system functions from their implementations, has been adopted as a key principle for cloud computing. Network virtualization decouples network service provisioning from data transport/process capabilities, thus enabling virtual networks customized for multi-tenant requirements to share a common infrastructure. A milestone of network virtualization is the Network Function Virtualization (NFV) architecture developed by ETSI, which realizes network functions as software instances that can be deployed on commodity servers and storage [1].

The service-oriented principle realized through

the Everything-as-a-Service (XaaS) paradigm (e.g., IaaS, SaaS, PaaS, and so on) is also a key to cloud computing. When applied in networking this principle allows abstraction of network resources and functions as self-contained components that can be exposed, accessed, and composed for service provisioning through loose-coupling interfaces. NFV embraces the service-oriented principle and supports XaaS at various levels including NFV Infrastructure-as-a-Service (NFVIaaS), Virtual Network Function-as-a-Service (VNFaaS), and Virtual Network-as-a-Service (VNaaS). 3GPP has proposed a service-based architecture for 5G networks that encapsulates network functions as service components to support network slicing [2].

The virtualization and service-oriented principles in network design introduce a trend of *cloudification* in networking that enables network systems to be realized based on cloud technologies and network services to be provisioned following the cloud service model. On the other hand, networking has been the foundation for cloud data centers and a key to cloud service provisioning. The merging edge computing paradigm, which essentially embeds decentralized cloud capabilities into network infrastructures mainly at the network edge, requires networking as an indispensable component [3].

The trend of network cloudification and the critical role of networking in cloud/edge computing are enabling the convergence of these two fields that used to be relatively independent. Such convergence leads to a holistic vision across networking and computing that allows integrated resource/function management across network and cloud/edge systems and unified provisioning of network and cloud/edge services [4]. The convergence may benefit stakeholders in the network-cloud/edge ecosystem through improved resource utilization, more flexible service management, and enhanced service performance. The interdisciplinary nature of such convergence may stimulate innovations in networking/computing technologies, and therefore has attracted extensive interest from both academia and industry. Although research progress toward network-cloud/edge convergence has been reported in various literatures, we feel that a survey reflecting a big picture of ongoing research in this exciting field would be beneficial to the research community.

Digital Object Identifier: 10.1109/MNET.011.2000089 *Qiang Duan is with Pennsylvania State University; Shangguang Wang is with Beijing University of Posts and Telecommunications; Nirwan Ansari is with New Jersey Institute of Technology.*

![](_page_1_Figure_0.jpeg)

FIGURE 1. An Architectural Framework for convergence of networking and cloud/edge computing.

In this article, we attempt to review the current status of research on network-cloud/edge convergence and identify some challenges/opportunities for future work. We first describe the notion of network-cloud/edge convergence and present an architectural framework. Then, we summarize recent advances in related standardization and review key technologies developed in some representative projects. We discuss challenges and research opportunities and draw conclusions in the final section

## Convergence of Networking and Cloud/Edge Computing

The ongoing network cloudification is replacing specially designed network appliances with data center-like systems constructed with commodity servers and storage upon which virtual network functions can be deployed as software instances and composed as service components for service provisioning. Therefore, networks are being transformed from infrastructures dedicated to data communications to versatile platforms for supporting both networking and computing services. On the other hand, network cloudification adopts the cloud service model for network service delivery, which allows the data centers and edge servers originally built for cloud/edge computing to be utilized for hosting virtual network functions.

Networking and cloud/edge computing, which used to focus on data communications and data process/storage respectively, are now merging together, thus calling for a holistic vision across these two fields for various technology developments. For example, the heterogeneous infrastructure resources for data transport, process, and storage should be managed by unified mechanisms and utilized through a common abstraction layer by various virtual functions. The services delivered to end users should be composite network-cloud/edge services provisioned through federated orchestration of diverse network/compute functions offered by different service providers. In this article, we refer to the trend in technology developments toward a merging field of networking-cloud/edge computing with a holistic vision of system design, management, and operation as the convergence of networking and cloud/edge computing.

An architectural framework for a converged network-cloud/edge system is depicted in Fig. 1. The infrastructure layer in this framework consists of multiple admin-domains operated by different infrastructure providers. Each admin-domain may be composed of multiple tech-domains, each of which comprises a certain type of infrastructure for networking, computing, or storage. The virtualization layer provides a common abstraction of the heterogeneous computing and networking infrastructure resources and exposes the virtual resources via the IaaS paradigm. Various virtual network functions (VNFs) and virtual compute functions (VCFs) are realized on the virtual function layer by leveraging infrastructure services. VNFs and VCFs are orchestrated as service components on the service layer to provision composite services for supporting multi-tenant users/ applications.

This framework indicates that common virtualization and service-oriented abstraction across networking and computing domains form a foundation for network-cloud/edge convergence. Infrastructure-level virtualization offers a general abstraction of heterogenous network-compute resources that allows VNFs/VCFs to be realized through leveraging various infrastructure services. Function-level virtualization abstracts both VNFs and VCFs as service components that can be orchestrated through common mechanisms to enable federated network-cloud/edge service management. Upon such a foundation, inter-domain cooperations among networking and computing systems play a crucial role in network-cloud/edge convergence, which demands new technologies for i) unified resource management across tech-domains comprising heterogenous network and compute infrastructures; ii)

IEEE Network • Novembe/December 2020 149

ETSI ISG NFV is a main driving force for network cloudification and offers some key technologies for enabling network-cloud/edge convergence. In the NFV architecture, network and compute infrastructures are abstracted by a common virtualization layer through which virtual resources may be leveraged for realizing VNFs.

> federated service management across admin-domains operated by different network and cloud/ edge service providers; and iii) holistic life-cycle management of virtual network/compute functions and network/cloud/edge services.

> Network-cloud/edge convergence is expected to benefit various skateholders in the entire ecosystem of networking and cloud/edge computing. The holistic vision for architectural design, resource management, system operations, and service provisioning across networking and computing fields may significantly improve resource utilization and service performance, lower capital/ operational costs and generate new revenues, and introduce new service models that stimulate innovations and create new business opportunities.

> In the following two sections, we attempt to present the current status of research on network-cloud/edge convergence by reviewing recent progress in relevant standardization and developments in some representative projects.

### Standardization Progress toward Network-Cloud/Edge Convergence ETSI Network Function Virtualization (NFV)

ETSI ISG NFV is a main driving force for network cloudification and offers some key technologies for enabling network-cloud/edge convergence. In the NFV architecture, network and compute infrastructures are abstracted by a common virtualization layer through which virtual resources may be leveraged for realizing VNFs. Management and Orchestration (MANO) is responsible for service/ resource management and orchestration. Virtualized Infrastructure Manager (VIM) in MANO supports unified management of network-compute resources. The NFV Orchestrator (NFVO) orchestrates VNFs as service components for end-to-end service provisioning [5].

Recent developments in NFV further enhance its support for network-cloud/edge convergence. NFV Release-3 [6] includes enhancements for service provisioning spanning multiple admin-domains and new interaction mechanisms between MANOs for inter-domain service orchestration. NFV now supports cloud-native VNF implementations by leveraging container-based virtualization and the micro-services architecture. MANO has also been enhanced for deploying service components across the access, transport, and core networks; this is critical for composite network-cloud/edge service provisioning.

#### ETSI Multi-Access Edge Computing (MEC)

The MEC architecture developed by IETF ISG MEC essentially embeds decentralized cloud capabilities in the network infrastructure at the network edge and thus can be regarded as a representative case of convergence between networking and computing. The MEC architecture comprises three levels: networks, MEC host, and MEC system. The compute, storage, and network resources at the MEC host are abstracted by a common virtualization layer and leveraged by the MEC platform for running MEC applications [3]. Such a virtualization layer enables unified resource abstraction and management across network and compute domains thus forming a basis for network-cloud/edge convergence.

The true impact of edge computing relies on its interaction with networking including orchestration between computing and networking capabilities. Recent developments in MEC support integration of MEC and NFV, which allows MEC applications and VNFs to share the same virtual infrastructure and NFV MANO to be leveraged for MEC management and orchestration. With MEC-NFV integration, recent progress in NFV for enabling network-cloud/edge convergence is embraced in the MEC architecture.

#### IETF Service Function Chaining (SFC)

The SFC notion developed by IETF also offers enabling technologies for network-cloud/edge convergence. An SFC is defined as an abstract view of service comprising a set of required service functions and their execution order. The IETF SFC architecture comprises service classification functions (SCFs), service function forwarders (SFFs), and service functions (SFs) as the key components, and provides a mechanism to form service paths for traffic steering through SFs [7]. It has been a consensus that SFC and NFV complement each other. NFV enables flexible SFC through virtualization and orchestration of service functions while SFC offers a service provisioning model in NFV.

Recent developments in SFC include a hierarchical SFC architecture that supports service provisioning across multiple tech- and/or admin-domains, which may facilitate orchestration of network and cloud/edge services toward their convergence. Another important piece of workin-progress is SFC in edge computing, including distributed service discovery and management mechanisms that are applicable in edge computing environments.

#### MEF Lifecycle Service Orchestration (LSO)

MEF LSO attempts to enable flexible service orchestration across multiple provider networks as well as different tech-domains [8]. The LSO architecture comprises four layers from top to bottom, business applications, service orchestration functionality, infrastructure control and management, and element control and management, with service-oriented abstraction between the layers. LSO supports inter-domain service orchestration via APIs between business applications in different domains and interfaces between domain orchestrators.

The flexible inter-domain service orchestration enabled by LSO supports composite network-cloud service provisioning, which is considered as a main application scenario of LSO. In addition, the Cloud Service Architecture developed by OpenCloud Connect1 considers application and connectivity as the key elements of the inter-cloud interface for integrating cloud applications and network connections.

150 IEEE Network • Novembe/December 2020

<sup>1</sup> OpenCloud Connect is an independent organization under the MEF umbrella.

#### 3GPP/5G-PPP 5GNetwork Slicing

The 5G network architecture developed in the 3GPP/5G-PPP community identifies network slicing as a key to realizing multi-tenant virtual networks upon shared network-compute infrastructures for supporting various vertical applications [9]. The 5G architecture adopts NFV with the SDN paradigm as the foundation and leverages virtualization, softwarization, programmability, and service-based architecture as enablers of network slicing. The VNFIaaS, VNFaaS, and VNaaS paradigms are also applied in 5G architecture for service provisioning.

Network slicing offers a promising approach to convergence of networking and cloud/edge computing. 5G architecture emphasizes an end-to-end slicing perspective that spans over tech-domains comprising network/compute infrastructures and admin-domains operated by network, edge, and cloud service providers. Toward this direction, 3GPP/5G-PPP is developing a common abstraction layer for unifying network-compute resource virtualization and an inter-domain orchestration framework for supporting composite network-cloud/edge service provisioning. The 5G network is expected to be a main platform for edge service delivery and thus forms a base for network-cloud/edge convergence.

## Representative Projects Related to Network-Cloud/Edge Convergence UNIFY

UNIFY is an EU-funded FP7 project that aims at unifying cloud systems and carrier networks in a common architecture [10]. The UNIFY architecture comprises an infrastructure layer (IL), an orchestration layer (OL), and a service layer (SL). The IL consists of multiple tech-domains of network and cloud infrastructures and each domain has its own controller. The OL contains a resource orchestrator (RO) upon a controller adaption (CA) sub-layer. The CA provides an interface between each domain controller and the RO, which is responsible for inter-domain resource orchestration to support end-to-end service provisioning.

UNIFY employs a hierarchical structure for resource management across infrastructure domains. The RO is a global orchestrator that coordinates a set of domain controllers for composite network-cloud service provisioning. IaaS is applied on the CA sub-layer to enable common abstraction of heterogeneous infrastructure resources. The unified resource management of network-compute infrastructures in UNIFY provides a foundation for network-cloud/edge convergence. On the other hand, the assumption of a single administrator in UNIFY limits its capability of inter-domain service-orchestration.

#### T-NOVA

The objective of the T-NOVA project is to develop an architecture for provisioning, managing, monitoring, and optimizing VNFs over integrated network-compute infrastructures for composite service delivery [11]. The T-NOVA architecture comprises the layers of infrastructure, infrastructure management, orchestration, and marketplace

The 5G architecture adopts NFV with the SDN paradigm as the foundation and leverages virtualization, softwarization, programmability, and service-based architecture as enablers of network slicing. The VNFIaaS, VNFaaS, and VNaaS paradigms are also applied in 5G architecture for service provisioning.

from bottom to top. The infrastructure management layer coordinates the management of datacenter infrastructures and inter-datacenter network connections. The orchestration layer comprises a service orchestrator and a resource orchestrator for end-to-end service provisioning spanning over different tech-domains of networking and computing.

Following the service-oriented principle, T-NOVA realizes a Network Function-as-Service (NFaaS) paradigm that enables VNFs to be published as service components that can be selected and composed by a broker on the marketplace layer. The brokerage platform allows end-to-end services to be provisioned through composing VNF service components. Although T-NOVA currently focuses on network services, its unified management of heterogeneous infrastructure resources and brokerage/orchestration across different service domains support network-cloud/ edge convergence.

#### CORD

CORD (Central Office Rearchitected as a Data-center) is an ONF (Open Network Foundation) project for reinventing architecture of central offices at the network edge by leveraging data center technologies [12]. The CORD project unifies NFV, SDN, and cloud technologies on both the infrastructure and service layers. The infrastructure layer consists of servers/storage for hosting VNF instances and a leaf-spine network fabric. OpenStack, Docker and Kubernetes are employed for virtual infrastructure management. The network fabric is implemented as an SDN with an ONOS controller. Service orchestration is realized by the XOS module that composes the infrastructure services provided by OpenStack/ Kubernetes, control services provided by ONOS, and other network and cloud services.

CORD adopts the XaaS paradigm for unified resource abstraction and service orchestration. VNFaaS allows VNFs to be deployed in the same way as cloud services upon the infrastructure layer via the IaaS paradigm. The CORD architecture supports container-based VNF instances required by the micro-services architecture. Through cloudification of central offices located at the network edge, CORD may significantly enhance the capability of carrier networks for hosting edge applications, thus supporting the convergence of networking and cloud/edge computing. Based on the CORD platform, ONF has developed a reference architecture M-CORD (https://www.opennetworking.org/mcord/) as a cloud-native solution for virtualization of RAN and mobile core (including vEPC) in 5G networks to enable mobile edge applications/services using a micro-services architecture.

#### 5G Exchange (5GEx)

A main objective of the 5GEx project is to realize an exchange framework for orchestration of network and cloud resources over multiple tech- and

IEEE Network • Novembe/December 2020 151

| Project        | Service-oriented abstraction | Unified resource management | Federated service orchestration      | Convergence scope  |
|----------------|------------------------------|-----------------------------|--------------------------------------|--------------------|
| UNIFY          | Infrastructure-as-a-Service  | Hierarchical orchestration  | Limited to single admin-domain       | Network-cloud      |
| T-NOVA         | VNF-as-a-Service             | Hierarchical orchestration  | Centralized brokerage                | Network-cloud      |
| CORD           | Everything-as-a-Service      | Hierarchical orchestration  | Limited to single admin-domain       | Network-edge       |
| 5G-Exchange    | Slice-as-a-Service           | Hierarchical orchestration  | Cascade inter-provider orchestration | Network-edge-cloud |
| 5G-Transformer | Slice-as-a-Service           | Hierarchical orchestration  | Inter-provider federation            | Network-edge-cloud |

TABLE 1. Comparison of key enabling technologies for network-cloud/edge convergence developed in representative projects.

![](_page_4_Figure_2.jpeg)

FIGURE 2. Hierarchical structures employed in the UNIFY and CORD projects for unified management of heterogeneous resources in a single admin-domain.

admin-domains in 5G networks [13]. The 5GEx architecture is based on a three-layer model comprising:

- Multi-operator wholesale relationship that enables cooperation among service providers.
- Multi-vendor inter-operation with orchestration capability over multiple tech-domains.
- An infrastructure layer of network, compute, and storage resources.

5GEx employs a decentralized cascade approach for inter-provider service orchestration; each provider acts as a service reseller to customers but the delivered services may contain sub-services and/or resources from other providers.

5GEx introduces a Slice-as-a-Service (SlaaS) paradigm, which combines NFVIaaS, VNFaaS, and connectivity services for composite network-cloud/edge service provisioning. Various technologies employed in 5GEx, including fully software-driven design, network-compute resource integration in individual services, and automatic resource trading and orchestration for service delivery, overcome the segregation between networking and computing, and may thus greatly facilitate network-cloud/edge convergence.

#### 5G-Transformer

The 5G-Transformer project aims to transform today's mobile networks into an SDN/NFV-based networking-computing platform upon which network slices can be constructed for supporting various vertical industries [14]. 5G-Transform takes a twofold technical approach: enable customized network slices for meeting vertical requirements, and integrate networking-computing resources throughout the virtual infrastructure from the access network to the core network and then to cloud data centers. The 5G-Transformer architecture comprises a Vertical Slicer (5G-VS) for creating and managing network slices, a Service Orchestrator (5G-SO) for service orchestration across tech- and/or admin-domains, and a Mobile Transport and Computing Platform (5G-MTP) as the underlying virtual infrastructure.

5G-Transform architecture supports service deployment upon multiple tech-domains and service orchestration across admin-domains, which are key enablers for network-cloud/edge convergence. 5G-Transform employs a hierarchical structure for unified resource management, in which an orchestrator coordinates the managers in different tech-domains comprising network, compute, and storage infrastructures. 5G-Transform supports federation between the service orchestrators in different admin-domains at both the service and resource levels for composite service provisioning. 5G-Transform includes edge application management in its architecture, thus supporting the integration of MEC in 5G networks.

#### Comparison of Representative Research Projects

A comparison of the reviewed projects shows some trends in key technologies for network-cloud/edge convergence, as summarized in Table 1.

Service-oriented abstraction is employed in all the projects for achieving common virtualization of networking and computing resources/functions. We noticed a trend of applying the XaaS paradigm from underlying infrastructures (IaaS in UNIFY) to virtual functions (VNFaaS in T-NO-VA) and then to network services and slices (XaaS in CORD and Slice-as-a-Service in 5GEx and 5G-Transform), each providing a higher-level abstraction based on all the lower-level abstractions beneath it.

For unified resource management across heterogeneous tech-domains, all the reviewed projects follow a hierarchical structure as illustrated by Fig. 2 in which each tech-domain has a controller for managing a certain type of infrastructure resources and a global orchestrator coordinates the tech-domain controllers for inter-domain resource management.

A variety of approaches have been proposed for federated service management across admin-domains (service providers).2 T-NOVA employs a centralized broker for selecting and composing VNFs offered by different providers to provision composite services. The more recent 5G-Exchange and 5G-Transform projects both advocate a decentralized model for service orchestration/federation across the admin-domains owned by different service providers, as shown in Fig. 3.

Combining the service-level (inter-admin-domain) and resource-level (inter-tech-domain) orchestration in these projects shows a trend toward a hybrid structure with decentralized service federation between admin-domains and

<sup>2</sup> The UNIFY and CORD projects focus on integrating heterogeneous infrastructures resources within an admin-domain and thus lack service orchestration capability across admin-domains.

hierarchical resource orchestration across tech-domains within individual admin-domains.

The reviewed projects also reflect an extension of the network-cloud/edge convergence scope from network core to network edge. UNIFY and T-NOVA focus on unifying carrier networks and cloud data centers. CORD naturally integrates networking and computing at the network edge. Both 5GEx and 5G-Transformer extends the convergence to the whole consortium of access-transport-core networks with edge servers (embedded in access/transport networks) and cloud data centers (attached to core networks).

# CHALLENGES AND RESEARCH OPPORTUNITIES CHALLENGES

Heterogeneity in Resources and Functions: Heterogeneity in infrastructure resources and service functions is a main challenge to network-cloud/edge convergence. The resources in different tech-domains of network, compute, and storage impose heterogeneous implementations but need to be integrated into a common infrastructure layer with holistic management. Virtual functions for networking and computing may have guite different features and requirements. For example, VNFs often require shorter latency, larger throughput, and higher reliability as compared to typical cloud/edge functions. A wide variety of service chains/network slices are constructed to meet the highly diverse requirements of multitenant users. End-to-end service provisioning in a converged network-cloud/edge environment typically spans across autonomous admin-domains operated by different service providers. Therefore, how to fully utilize heterogenous virtual resources and functions across tech- and admin-domains for composite service provisioning to meet diverse user requirements becomes a challenging problem.

Scalability in System and Function Design: Network-cloud/edge convergence pushes the scalability requirement of the system design to a new level. Virtualization across the network-compute infrastructures enables various functions to be deployed as software instances and thus significantly increases the number of function modules involved in the system. The micro-services architecture supported by container-based virtualization further decomposes virtual functions to finer-grained service components interconnected through network connections. This presents new challenges to system scalability due to the increased number of function components and the communication overheads among them. In addition, network-cloud/edge convergence leads to a common service platform for meeting the diverse multi-tenant requirements, which incurs a large number of network slices to be constructed and managed through the orchestration of numerous network-compute service components. Therefore, engineering a scalable design of system architecture and control/management is a challenging open issue.

Flexibility, Agility, and Performance of Service Provisioning: Convergence of networking and cloud/edge computing expects flexible and agile provisioning of composite services with performance guarantees. In addition to the heterogeneous resources/functions in a large scale converged network-cloud/edge system, integration

![](_page_5_Figure_6.jpeg)

FIGURE 3. Decentralized structures for service orchestration/federation across admin-domains in the 5GEx and 5G-Transformer projects.

of decentralized computing capabilities in networks with finer-grained function components enabled by the micro-services architecture introduces even more dynamism in various aspects, including availability, capacity, mobility, and lifespan of both hosting infrastructures and virtual function instances. All of these factors together call for more sophisticated service management, among which inter-domain federation for end-to-end provisioning of composite services is particularly challenging. Information exchange between autonomous domains, collaboration between service providers, holistic management of resources and services are all challenging problems that demand thorough investigation. Service performance guarantee, which has been an important issue in network virtualization, becomes even more challenging due to network-cloud/edge convergence. Optimal mapping from service requirements to resource allocation, flexible inter-domain resource management for service delivery, effective evaluation and verification of end-to-end service performance are all open issues to be fully studied.

Integration of 5G Network and Edge Computing: The 5G network provides an environment in which edge computing may be widely deployed; therefore, integrating 5G network and edge computing forms a representative scenario of network-cloud/edge convergence. The unprecedented complexity of the 5G network introduces challenges to its integration with edge computing. Such complexity comes from various aspects, for example, the dense and heterogeneous network functions, highly diverse applications, ultra-low latency requirements for vehicle communications, growing demand for location-based services with

IEEE Network • Novembe/December 2020

We believe that cross-fertilization among multiple fields, for example network virtualization, cloud-native networking, network slicing, cloud/edge computing, and micro-services architecture, with a holistic vision of network-compute convergence may trigger technology innovations that will significantly enhance the future information infrastructure.

> high positioning accuracy, and so on. Therefore, deploying edge computing within 5G network becomes an important research area where comprehensive solutions are to be developed for addressing the challenges of heterogeneity, scalability, flexibility, and performance.

#### Research Opportunities

Architecture Design of Converged Network-Cloud/Edge Systems: Architectural design forms a technical foundation for enabling network-cloud/edge convergence. Combining the software-defined principle with service-oriented virtualization in architecture design may offer promising approaches to addressing the aforementioned challenges. Software-defined networking essentially decouples the data and control planes to enable a network operating system with programmability. Integrating the software-defined principle into the virtualization-based architecture allows a global programmable control platform respectively for the infrastructure layer and service layer, which may significantly enhance composite service provisioning. Therefore, this direction provides opportunities for future research. Inter-domain service federation is an important aspect of architectural design that presents multiple options, including hierarchical structure with a single master orchestrator, peer-to-peer structure with a cluster of domain orchestrators, and hybrid structure with multiple federated hierarchical systems. Thorough evaluation of these options is also an important subject that deserves more future work.

Resource and Service Modelling for Unified Abstraction: Developing and standardizing a common set of models for unified abstraction of the resources/services across network and cloud/ edge domains plays a key role in addressing the heterogeneity challenge to network-cloud/edge convergence. Following the virtualization principle of decoupling services from infrastructures, abstraction models should be standardized on both the resource and service layers for supporting multi-level virtualization (e.g., virtual infrastructures, virtual functions, and virtual networks). At the same time, mapping from high-level models for service specification to low-level models for resource configuration is also critical. The standard models should include both functional and non-functional features (e.g., performance and capacity requirements) to facility high-performance service management. On the other hand, an appropriate level of information aggregation is important in order to face the scalability challenge. Research efforts toward resource/service modeling are fairly recent and more study is needed in this area, thus offering research opportunities.

New Technologies for Composite Service Management: Service management in a converged networking-cloud/edge computing environment calls for novel mechanisms for design, instantiation, deployment, execution, and optimization of composite services upon integrated network-compute infrastructures. A key problem is to achieve holistic service management across heterogeneous tech- and admin-domains. Unified resource management across tech-domains is being studied in various fields such as NFV, 5G network slicing, cloud data centers, and edge computing, but more work is expected for seamless integration of the available technologies in a large scale converged network-cloud/edge system. Less progress has been made so far in federated service management across admin-domains/ service providers, thus offering more opportunities for future research. Automation and intelligence are expected to be key attributes of service management in order to face the challenges of heterogeneity, scalability, and flexibility, which demand novel technologies to be developed probably by leveraging methods in areas such as game theory, control theory, and machine learning. Big data analytics and machine learning techniques could be particularly useful to address the challenges of heterogeneity, scalability, flexibility, and performance introduced by integrating edge computing within 5G networks [15]. Performance assurance is another important aspect of service management. Analytical evaluation and experimental verification of end-to-end performance of composite network-cloud/edge services is also an important problem for future research.

## Conclusions

The virtualization and service-oriented principles applied in networking technologies enable cloudbased networking while the latest developments in cloud/edge computing lead to a network-based computing paradigm. Convergence of networking and cloud/edge computing calls for a holistic vision across these two fields and thus may significantly impact relevant technology developments. In this article, we first described the notion of network-cloud/edge convergence with an architectural framework of converged network-cloud/edge systems. Then, we gave a brief survey on representative works to reflect the start-of-the-art research toward network-cloud/edge convergence, including recent progress in relevant standardization and technology developments in representative research projects. We also discussed challenges to realizing network-cloud convergence and identified some opportunities for future research. We found that although exciting progress has been made toward convergence of networking and cloud/edge computing, this interesting interdisciplinary area is still in its infancy, thus offering rich research opportunities. We believe that cross-fertilization among multiple fields, for example network virtualization, cloud-native networking, network slicing, cloud/edge computing, and micro-services architecture, with a holistic vision of network-compute convergence may trigger technology innovations that will significantly enhance the future information infrastructure.

#### Acknowledgment

This work was partially supported by the National Key Research and Development Program of China (2018YFE0205503); the National Natural Science Foundation of China (61922017); and the Funds for Creative Research Groups of China (61921003).

154 IEEE Network • Novembe/December 2020

#### References

- [1] B. Yi *et al.*, "A Comprehensive Survey of Network Function Virtualization," *Computer Networks*, vol. 133, 2018, pp. 212–262.
- [2] 3GPP, "TS 23.501: System Architecture for the 5G System, version 15.2.0," June 2018.
- [3] ETSI, "Mobile-Edge Computing (MEC) Framework and Reference Architecture, version 2.1.1," Jan. 2019.
- [4] Q. Duan and S. Wang, "Network Cloudification Enabling Network-cloud/Fog Service Unification: State of the Art and Challenges," *Proc. 2019 IEEE World Congress on Services (SERVICES)*, IEEE, 2019, pp. 153–59.
- [5] ETSI, "Network function virtualization (NFV) architectural framework version 1.2.1," Dec. 2014.
- [6] ETSI, "NFV Realease 3 Definition version 0.14.0," Sept. 2019.
- [7] IETF, "RFC 7665: Service Function Chaining (SFC) Architecture," Oct. 2015.
- [8] MEF, "Lifecycle Service Orchestration (LSO) Reference Architecture and Framework," Mar. 2016.
- [9] 5G-PPP, "View on 5G Architecture version 3.0," June 2019.
- [10] B. Sonkoly *et al*., "Unifying Cloud and Carrier Network Resources: An Architectural View," *Proc. 2015 IEEE Global Commun. Conf. (GLOBECOM 2015)*, 2015, pp. 1–7.
- [11] M.-A. Kourtis *et al.*, "T-NOVA: An Open-Source MANO Stack for NFV Infrastructures," *IEEE Trans. Network and Service Management*, vol. 14, no. 3, 2017, pp. 586–602.
- [12] L. Peterson *et al*., "Central Office Re-Architected as a Data Center," *IEEE Commun. Mag*., vol. 54, no. 10, 2016, pp. 96–101.
- [13] G. Biczok *et al.*, "Manufactured by Software: SDN-Enabled Multi-Operator Composite Services with the 5G Exchange," *IEEE Commun. Mag.*, vol. 55, no. 4, 2017, pp. 80–86.
- [14] A. De la Oliva *et al*., "5G-Transformer: Slicing and Orchestrating Transport Networks for Industry Verticals," *IEEE Commun. Mag*., vol. 56, no. 8, 2018, pp. 78–84.
- [15] Q. Liu, T. Han, and N. Ansari, "Learning-Assisted Secure End-to-End Network Slicing for Cyber-Physical Systems," *IEEE Network Mag*., vol. 34, no. 2, 2020.

#### Biographies

Qiang Duan Qiang Duan (S'00–M'03–SM'17) is a professor of information sciences and technology at the Pennsylvania State University Abington College. His current research interests include next generation Internet, software-defined networking, network function virtualization, and cloudnative networking. He has (co-)authored three books, six book chapters, and more than 100 journal articles and conference papers in these areas. He is an editor for multiple research journals and has been regularly serving as a reviewer for various IEEE transactions and magazines. He received IEEE Communications Society Outstanding Reviewer Award in 2015. He has also served on the TPCs for numerous international research conferences including GLOBECOM, ICC, ICCCN, WCNC, AINA, ICNC, etc. He is a senior member of IEEE.

Shangguang Wang Shangguang Wang received his Ph.D. degree from Beijing University of Posts and Telecommunications (BUPT) in 2011. He is currently a professor and deputy director at the State Key Laboratory of Networking and Switching Technology, BUPT. He has published more than 100 papers, and participated in organizing many international conferences as a general chair or PC chair. His research interests include edge computing, service computing, and cloud computing. He is a senior member of IEEE, and the Editor-in-Chief of the International Journal of Web Science.

Nirwan Ansari Nirwan Ansari (S'78–M'83–SM'94–F'09) is Distinguished Professor of electrical and computer engineering at NJIT. He is also a Fellow of the National Academy of Inventors. He has (co-)authored three books and more than 600 technical publications. He has also been granted more than 40 U.S. patents. He has guest-edited a number of special issues covering various emerging topics in communications and networking. He has served on the editorial/advisory board of over 10 journals including as Associate Editor-in-Chief of *IEEE Wireless Communications Magazine*. His current research focuses on green communications and networking, cloud computing, drone-assisted networking, and various aspects of broadband networks.

IEEE Network • Novembe/December 2020 155
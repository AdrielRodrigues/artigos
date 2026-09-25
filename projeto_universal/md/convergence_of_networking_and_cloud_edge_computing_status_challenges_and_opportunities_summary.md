# Convergence of Networking and Cloud/Edge Computing: Status, Challenges, and Opportunities

## Abstract
The paper explores "network cloudification," where networking leverages cloud technologies and service models to provision services. This trend, combined with the necessity of networking for edge computing, has led to a convergence of networking and cloud/edge computing. The authors propose an architectural framework for this convergence, survey current standardization efforts and research projects, identify existing technical challenges, and suggest future research directions.

## Introduction
Networking is increasingly adopting virtualization and service-oriented principles—key foundations of cloud computing. Network Function Virtualization (NFV) separates system functions from hardware, while the Everything-as-a-Service (XaaS) paradigm allows network resources to be abstracted as self-contained components (e.g., VNFaaS, VNaaS). 

This "cloudification" means networks are becoming versatile platforms for both computing and networking services. Simultaneously, edge computing embeds cloud capabilities into the network infrastructure. The convergence of these fields aims for a holistic vision where resource management is integrated across network-compute systems and service provisioning is unified. This integration intends to improve resource utilization, flexibility, and overall service performance.

## Convergence of Networking and Cloud/Edge Computing
Convergence is defined as the merging of networking (traditionally focused on data communication) and cloud/edge computing (focused on processing and storage). In this converged state, network appliances are replaced by commodity server systems hosting virtual functions, and cloud servers are used to host network functions.

### Architectural Framework for Converged Systems
The authors propose a four-layer framework:
*   **Infrastructure Layer:** Comprised of multiple administrative domains (admin-domains), each containing various technical domains (tech-domains) for networking, computing, or storage.
*   **Virtualization Layer:** Provides a common abstraction of heterogeneous resources via the IaaS model.
*   **Virtual Function Layer:** Hosts Virtual Network Functions (VNFs) and Virtual Compute Functions (VCFs).
*   **Service Layer:** Orchestrates VNFs and VCFs as components to provide composite services for multi-tenant users.

For this framework to function, three key capabilities are required: unified resource management across tech-domains, federated service management across different admin-domains, and holistic life-cycle management of virtual functions and services.

### Standardization Progress toward Network-Cloud/Edge Convergence
#### ETSI Network Function Virtualization (NFV)
ETSI NFV drives cloudification by abstracting infrastructure through a virtualization layer. The Management and Orchestration (MANO) framework—specifically the Virtualized Infrastructure Manager (VIM) and NFV Orchestrator (NFVO)—enables unified resource management and end-to-end service provisioning. Recent updates include support for multi-admin-domain orchestration, container-based cloud-native VNFs, and micro-services architecture.

#### ETSI Multi-Access Edge Computing (MEC)
MEC integrates decentralized cloud capabilities at the network edge via a three-level structure: networks, MEC hosts, and the MEC system. By utilizing a common virtualization layer for compute and network resources, MEC provides a basis for convergence. Integration with NFV allows MEC applications and VNFs to share infrastructure and management tools.

#### IETF Service Function Chaining (SFC)
SFC defines services as ordered sequences of service functions. It complements NFV by providing the service provisioning model that directs traffic through specific SFs. Current developments focus on hierarchical SFC architectures for multi-domain orchestration and distributed discovery mechanisms for edge environments.

#### MEF Lifecycle Service Orchestration (LSO)
MEF LSO enables flexible orchestration across different providers and tech-domains using a four-layer architecture (Business, Service Orchestration, Infrastructure Control, and Element Control). It specifically supports the provisioning of composite network-cloud services through inter-domain APIs.

#### 3GPP/5G-PPP 5G Network Slicing
5G uses SDN and NFV to create multi-tenant virtual networks (slices) on shared infrastructure. Convergence is achieved by treating slices as end-to-end entities spanning across various tech-domains and admin-domains. The goal is a common abstraction layer for all network-compute resources to facilitate edge service delivery.

## Representative Projects Related to Network-Cloud/Edge Convergence
### UNIFY
UNIFY seeks to unify carrier networks and cloud systems using an Infrastructure Layer (IL), Orchestration Layer (OL), and Service Layer (SL). It uses hierarchical resource management via a global orchestrator; however, it is primarily limited to single admin-domain operations.

### T-NOVA
T-NOVA focuses on the delivery of composite services by managing VNFs over integrated infrastructures. It introduces a "Network Function-as-a-Service" (NFaaS) paradigm and utilizes a marketplace broker to select and compose VNF components into end-to-end services.

### CORD
CORD re-architects central offices as data centers using SDN, NFV, and cloud technologies (e.g., OpenStack, Kubernetes). It adopts the XaaS paradigm for unified abstraction, allowing VNFs to be deployed like any other cloud service. M-CORD extends this to a cloud-native solution for 5G RAN and core virtualization.

### 5G Exchange (5GEx)
5GEx provides an exchange framework for orchestrating resources across multiple providers using a decentralized cascade approach (where providers act as resellers). It introduces "Slice-as-a-Service" (SlaaS), merging connectivity and compute into a single composite service.

### 5G-Transformer
This project transforms mobile networks into SDN/NFV platforms for vertical industries. Its architecture includes a Vertical Slicer, Service Orchestrator, and Mobile Transport and Computing Platform. It supports inter-provider federation at both the resource and service levels to integrate MEC into 5G.

### Comparison of Representative Research Projects
The authors identify several trends across these projects:
1.  **Abstraction:** A move from low-level abstraction (IaaS) toward higher-level models (VNFaaS $\rightarrow$ XaaS $\rightarrow$ SlaaS).
2.  **Resource Management:** A consistent reliance on hierarchical structures within individual admin-domains.
3.  **Federation:** A shift from centralized brokerage to decentralized service federation between different providers.
4.  **Scope:** An expansion of convergence focus from the network core/cloud data centers toward the network edge and access networks.

## Challenges and Research Opportunities
### Challenges
*   **Resource and Function Heterogeneity:** Integrating diverse implementations of networking, compute, and storage into one layer is difficult. VNFs have stricter performance requirements (latency, throughput) than standard cloud functions, complicating composite service provisioning across autonomous domains.
*   **System Scalability:** The shift toward micro-services and containerization increases the number of function components and communication overhead, straining system architecture and control mechanisms.
*   **Provisioning Agility and Performance:** High dynamism in infrastructure availability and mobility requires sophisticated inter-domain federation. Ensuring end-to-end performance guarantees remains an open problem during resource mapping.
*   **5G and Edge Integration:** The complexity of 5G (dense functions, ultra-low latency for vehicles, high positioning accuracy) creates significant hurdles for seamless edge computing integration.

### Research Opportunities
*   **Architectural Design:** Integrating SDN principles to create programmable control platforms for both infrastructure and service layers. Evaluating different federation structures (hierarchical vs. peer-to-peer).
*   **Unified Abstraction Modeling:** Creating standardized models for multi-level virtualization that include both functional and non-functional (performance) requirements, while balancing detail with scalability.
*   **Composite Service Management:** Developing automated and intelligent mechanisms for inter-domain orchestration using game theory, control theory, and machine learning to manage the complexity of integrated network-compute systems.

## Conclusions
The convergence of networking and cloud/edge computing represents a shift toward a holistic infrastructure where networks act as computing platforms and computing resources are embedded within networks. While standardization (NFV, MEC) and projects (CORD, 5GEx) have made progress, the field is still in its infancy. The authors argue that cross-fertilization between network virtualization, cloud-native networking, and micro-services architecture will be essential to enhancing future information infrastructures.
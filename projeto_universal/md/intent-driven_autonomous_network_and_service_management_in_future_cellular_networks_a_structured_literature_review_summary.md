---
index_terms:
  - Intent Based Networking
  - Autonomous Network Management
  - Service Level Agreement
  - 5G and Beyond Networks
  - Network Orchestration
  - Machine Learning for Networking
  - Declarative Policy
  - NFV/SDN Infrastructure
---

# Intent-driven autonomous network and service management in future cellular networks: A structured literature review

## 1. Introduction
Traditional network management relies on human experts and static scripts to monitor and configure services, a process that is becoming unsustainable due to the rising complexity of modern networks, high deployment costs, and the slow pace of administrator retraining. Autonomous network management emerges as a solution to these challenges by reducing human intervention through automation.

Intent-driven networking (IBN) enables this autonomy by allowing users and service providers to specify "intents"—high-level, abstract goals—without needing to define the low-level technical configurations required to achieve them. An autonomous network interprets these intents and automatically translates them into specific node configurations across various layers.

### 1.1. Standardization and related surveys
Several initiatives drive this evolution: ETSI’s Zero-touch Network and Service Management (ZSM) focuses on end-to-end automation and self-healing; Experiential Network Intelligence (ENI) integrates AI and context-aware policies for cognitive management; and IETF’s ANIMA works toward an integrated autonomic model.

While existing surveys cover intent semantics, orchestration, or general architectures, the authors argue that there is a gap in literature regarding:
1. Intent processing specifically for mobile communication services.
2. Converged architectural frameworks for future cellular networks.
3. Deep analysis of the relationship between subscriber and service provider intents.
4. Trade-offs involved in the mapping of abstract intents to physical configurations.

### 1.2. Scope and search protocol
The review aims to answer how declarative intents can dictate network design beyond 5G, the roles of various stakeholders, the core components of the IBN lifecycle, and the enabling technologies required for implementation. The authors performed a structured literature review across databases including Scopus, IEEE Xplore, ACM, ScienceDirect, and WileyOnline, narrowing 5,484 initial results down to 60 unique, relevant studies published between 2015 and 2021.

### 1.3. Contributions and paper organization
The paper contributes a formal definition of intent semantics, an analysis of the evolution from traditional to intent-based management, a review of enabling technologies (AI/ML, SDN/NFV), a proposed converged architectural framework focusing on SLA and KPI management, and a roadmap of open research challenges.

## 2. Intents: Lifecycle and management

### 2.1. Definition
An intent is defined as a set of operational goals and outcomes described in a declarative manner (what is needed) rather than an imperative manner (how to achieve it). This abstraction allows stakeholders to manage network functions without exposing internal resource complexities, facilitating the deployment of vertical-specific services (e.g., ultra-low latency for industrial automation) through intent translation functions.

### 2.2. Intent- and policy-based network management
Policy-based management is imperative: it uses a set of "if-then" rules to trigger specific actions based on events, often requiring centralized control and detailed implementation knowledge. In contrast, intent-based management is goal-oriented; it specifies the desired state (context, capabilities, constraints) and allows the network—treating itself as a single entity rather than discrete nodes—to determine the best implementation path. This decentralizes processing to the device level and improves scalability.

### 2.3. Lifecycle of an intent
Intents are categorized as transient (active for a single operation) or persistent (remain active until decommissioned). Persistent intents follow a structured lifecycle across three domains:

#### 2.3.1. User domain
This domain handles the recognition and formulation of intents. Through human-machine interfaces, users provide high-level instructions. An intent recognition engine interacts with the user to resolve conflicts and produce an actionable intent formatted for processing.

#### 2.3.2. Processing domain
The core of the lifecycle involves translating human-readable intents into machine-readable configurations using Natural Language Processing (NLP) or ontology mapping. Key functions include:
*   **Conflict Resolution:** Optimizing resources to prevent contention between multiple intents.
*   **Closed-loop Feedback:** Ensuring that generated configurations adhere to SLAs and adapting them to dynamic network conditions.
*   **Translation Techniques:** Approaches range from complex NLP and recurrent neural networks (RNNs) to "controlled" NLP with limited vocabularies for better scalability.

#### 2.3.3. Implementation domain
Configurations are deployed here, with a heavy focus on service quality assurance. This domain verifies that the implementation complies with the intent's objectives and reports outcomes back to the processing domain to complete the closed-loop cycle.

### 2.4. Intent stakeholders and classification
Intents vary by stakeholder goals: customers seek performance (e.g., high throughput), while operators focus on resource efficiency. Intents are classified into four types:
1. **Customer service intents:** Map customer requests via SLAs.
2. **Network service intents:** Guide the deployment of network functionalities.
3. **Strategy intents:** Manage QoS, fault resolution, and general policies.
4. **Validation/Customization intents:** Provide verification and modification guidelines for other intents.

### 2.5. Industry adoption of IBN
The authors analyze three primary industry implementations:
*   **Cisco:** Focuses on Digital Network Architecture using SDN to automate data center environments.
*   **Huawei:** Uses a dedicated "Intent Engine" with NETCONF/YANG models for campus environment closed-loop control.
*   **Juniper (Apstra):** A multi-vendor, software-based solution utilizing a context model and telemetry for automated reconfigurations.
The review notes that no fully converged multi-domain IBN solution currently exists.

## 3. Beyond 5G network and service modeling

### 3.1. Communication services evolution
Future networks must move beyond the basic 5G categories (eMBB, uRLLC, mMTC) to support complex use cases such as Holographic Type Communications (HTC), Multi-Sense Networks (MSN), and Time-Engineered Communications (TEC). These require a higher level of management agility than currently available.

### 3.2. Communication services ecosystem
The transition requires collaboration between network operators, cloud providers, and application providers using NFV, SDN, and Multi-access Edge Computing (MEC). Open-source platforms like ONAP, OSM, and ONOS are critical for enabling the runtime orchestration of these virtualized resources.

### 3.3. SLA compliance and assurance
A fundamental tradeoff exists between resource over-provisioning (wasteful) and under-provisioning (poor quality). The authors propose "SLA decomposition," where high-level end-to-end SLAs are broken down into specific, flexible intent-based targets for different network segments/domains. This allows the network to provide differentiated QoS based on actual vertical requirements.

### 3.4. Service design process and requirements
The proposed framework maps expectations between the Communication Service Customer (CSC) and Provider (CSP). The Communication Service Management Function (CSMF) manages this via two interfaces:
*   **Customer-Facing Communication Service (CFCS):** Handles cataloging, SLA interpretation, and user exposure.
*   **Resource-Facing Communication Service (RFCS):** Manages the lifecycle (preparation $\rightarrow$ commissioning $\rightarrow$ operation $\rightarrow$ decommissioning) of service instances.

### 3.5. Communication service and network orchestration
To realize these services, the GSMA's Generic Slicing Template (GST) is used as a deployment-agnostic blueprint. This allows the RFCS to trigger the instantiation of Network Slicing Instances (NSIs) in the network management layer regardless of the underlying physical infrastructure.

## 4. IDM enablers and motivation

### 4.1. SDN/NFV
SDN provides a programmable control plane for policy enforcement, while NFV abstracts network functions into Virtualized Network Functions (VNFs). Together, they enable IBN by making service chaining and traffic steering more flexible than in physical-only networks.

### 4.2. ZSM and autonomous networking
ZSM provides the necessary e2e orchestration and analytics framework for a "zero-touch" approach. It supports closed management loops that handle monitoring, root-cause analysis, and automated reconfiguration based on defined levels of autonomy.

### 4.3. Networks-2030
The ITU's Networks-2030 vision identifies gaps in programmability and lifecycle agility. IBN addresses these by introducing SLO-aware interfaces and supporting coordinated services where multiple interdependent requests are negotiated via closed-loop feedback.

### 4.4. ENI
ETSI’s ENI adds cognitive capabilities, including situational awareness and knowledge management. It defines a path toward full autonomicity (Cat-4/5) where the network can perform self-initiated optimization using intents as the primary human-machine interface.

### 4.5. ML and AI
AI is essential for the "inference" part of IBN. Specific applications include extracting service primitives from abstract text, optimizing orchestration paths, mapping intent to historic user behavior, and proactive resource monitoring. The authors suggest "Machine Learning as a Service" (MLaaS) as a viable deployment model for these functions.

## 5. Intent-based network and service management
The authors propose a converged framework consisting of four layers: Application, Intent, Network Management & Orchestration, and Resources.

### 5.1. Application layer
This layer focuses on intent representation. To balance human readability with machine scalability, the authors suggest using Constrained Natural Language (CNL) or Softgoal Inter-dependency Graphs (SIG). Some implementations use RNN-based chatbots to extract performance goals from users.

### 5.2. Intent layer
The Intent Controller acts as the intermediary between user desires and network reality.

#### 5.2.1. Intent expression and NBI
Declarative Northbound Interfaces (NBI) ensure that intent sources remain independent of provider implementations. The system uses mapping tables and catalogs to translate human terminology into machine-readable forms.

#### 5.2.2. Service model and orchestration
The system generates service models using Service Descriptors (SD) governed by Finite-State-Machines (FSM). These descriptors are converted into domain-specific requirements using languages like TOSCA and YANG, then forwarded to orchestrators (e.g., OSM or M-CORD).

#### 5.2.3. Service assurance and optimization
Closed-loop feedback monitors the state of deployed services. If resources change, the service graph is updated. The authors highlight the use of Generative Adversarial Networks (GANs) to predict future resource states and optimize Service Graph (SG) selection via Deep Reinforcement Learning (DRL).

#### 5.2.4. Role of intent API
The Intent API facilitates two-way communication: it exposes underlying infrastructure capabilities (via YANG/TOSCA) to the controller and pushes processed service descriptors down to the network layer.

### 5.3. Network management and orchestration layer
This layer comprises domain controllers (SDN, NFV MANO). It translates high-level orchestrator models into device-specific configurations (XML, YAML) and manages the actual deployment of VNF graphs and Service Function Chains (SFCs). Monitoring modules here provide the raw data needed for the Intent Layer to perform reactive or proactive refinements.

### 5.4. Resources and SBI
The physical layer provides compute, storage, and connectivity. Southbound Interfaces (SBI) are critical for exposing real-time resource status back up the chain, enabling the "closed loop" that allows an intent-based system to be truly autonomous.

## 6. Open issues and future directions

### 6.1. Intent description
There is a persistent tension between human readability and machine scalability. Future research should focus on contextual NLP methods that can handle vague human input without sacrificing processing speed.

### 6.2. Intent interpretation and service mapping
Mapping declarative intents to physical resources requires deep knowledge of network capabilities. The authors suggest adopting "microservices" from software engineering to decompose the service design lifecycle into modular, context-aware sub-services.

### 6.3. Role of ML/AI integration in intent management lifecycle
While NLP handles structure, more advanced models (BERT, Attention mechanisms) are needed for semantic retrieval. There is a need for dedicated studies on how to integrate MLaaS directly into the IBN control loop.

### 6.4. IBN deployment with NFV & SDN architecture
Current softwarized networks still rely largely on imperative policies. The challenge lies in creating a mapping mechanism that converts declarative parameters from multiple stakeholders into an autonomous lifecycle for VNFs and SFCs.

### 6.5. Compatibility of data modeling languages with IBN
Existing languages like YANG and TOSCA are insufficient for fully autonomous IBN. Improvements needed include:
*   **Service Model:** Better reuseability and inheritance for complex templates.
*   **Automation:** Inclusion of language semantics for imperative policies and dynamic dependency models that allow runtime modification of service graphs.

### 6.6. Multi-domain intents
Centralized orchestrators cannot scale to multi-domain environments due to a lack of global context and potential conflicts between local domain permissions and overarching inter-domain intents. Distributed orchestration is required.

### 6.7. IBN security
IBN increases the attack surface by giving users more influence over network design. Key concerns include:
*   **Malicious Intents:** The need for complex verification policies to prevent unauthorized resource appropriation.
*   **Transparency:** Establishing clear ownership and audit trails for intents within the domain.

## 7. Conclusion
IBN is an essential evolution toward autonomous networking, bridging the gap between high-level business goals and low-level technical configurations. By integrating closed-loop control, AI/ML inference, and software-defined infrastructure (SDN/NFV), future networks can achieve the agility required for beyond 5G services. The proposed converged framework emphasizes a layered approach where intent translation is supported by robust data models and continuous monitoring to ensure SLA compliance.
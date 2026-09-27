---
index_terms:
  - edge computing
  - mobile edge computing
  - 6G wireless networks
  - computation offloading
  - resource allocation
  - CROWN framework
  - integrated sensing and communications
---

# Edge computing in future wireless networks: A comprehensive evaluation and vision for 6G and beyond

## 1. Introduction
The exponential growth of connected devices—projected to reach 500 billion by 2030—renders centralized cloud systems insufficient due to network congestion and high latency. Emerging real-time applications such as autonomous vehicles, telemedicine, and AR/VR require instantaneous responses that only Edge Computing (EC) can provide by bringing storage and computation closer to the data source. While 5G has initiated this shift, 6G will necessitate even higher frequencies and lower latencies. Current edge architectures often rely on fixed infrastructure at specific sites, which limits scalability; therefore, there is a critical need for long-term strategies that integrate terrestrial and space networks to manage massive data traffic efficiently while ensuring privacy and autonomy.

## 2. Background and literature review
### 2.1. Edge computing
The proliferation of mobile broadband and IoT has created a demand for network performance (latency, throughput, dependability) ten times higher than current levels. Moving intelligence to the edge reduces backbone traffic and costs.

#### 2.1.1. Solutions based on edge
Edge solutions minimize bandwidth demands and reliance on connectivity by processing data at the gateway or device level. These systems include cloudlets, Cyber Foraging, Fog Computing, and Mobile Edge Computing (MEC).

#### 2.1.2. Content delivery networks (CDNs)
Developed to solve the "flash crowd" problem, CDNs distribute content across multiple edge servers to reduce the load on single central servers and improve user experience through localized storage of web data.

#### 2.1.3. Ubiquitous computing
Also known as pervasive computing, this paradigm embeds computing capabilities seamlessly into the daily environment, allowing smart devices to collaborate invisibly to enhance user experience and efficiency.

#### 2.1.4. P2P
Peer-to-peer architectures enable direct resource sharing between equal nodes without a central server, increasing resilience and scalability for applications like file sharing and cryptocurrencies.

#### 2.1.5. Cloud computing
A model delivering on-demand computing services (IaaS, PaaS, SaaS) via the internet on a pay-as-you-go basis, eliminating the need for local physical infrastructure.

#### 2.1.6. Cloudlet
Small-scale data centers located at the network edge that act as intermediaries between mobile devices and the cloud to reduce latency for time-sensitive tasks like AR/VR.

#### 2.1.7. Mobile edge computing
Originally defined by ETSI, MEC (now Multi-Access Edge Computing) extends cloud features to the RAN by deploying servers at base stations (eNodeB) or RNC sites using virtualization technologies.

#### 2.1.8. Fog computing
Pioneered by Cisco, fog computing is an extension of the cloud that incorporates both central and peripheral infrastructure. Unlike MEC's fixed locations, fog nodes can be deployed flexibly (e.g., on power poles or in vehicles).

### 2.2. Literature review
Existing research primarily focuses on minimizing service time delay (computation and communication) and energy consumption. Key findings include:
*   **Offloading Optimization:** Various algorithms exist to balance local vs. remote execution, utilizing VM migration, UAV-assisted connectivity, and reinforcement learning.
*   **Application Deployment:** Research emphasizes the need for application-aware offloading and microservice-based deployment to optimize resource-constrained edges.
*   **Collaborative Computing:** There is a trend toward "mobile clouds" or "transient clouds" where neighboring user devices collaborate to process tasks.
*   **Caching and Pre-fetching:** Strategies range from popularity-based caching at the edge to UE-side pre-fetching using social recommendations, though collaborative pre-fetching remains under-explored.
*   **Information-Centric Networking (ICN):** Named Data Networking (NDN) is highlighted for its ability to prioritize critical traffic and enable remote computation without IP mapping, though it introduces higher overhead than TCP/IP.
*   **Reputation-based Trust:** To secure NDN, reputation schemes based on historical behavior are proposed as alternatives to traditional cryptographic certificates.

## 3. Edge computing fundamentals
### 3.1. Resource management
This involves creating resource pools (CPU, memory, I/O) and managing their pooling, provisioning, transfer, and scheduling to optimize the utilization of scattered edge nodes.

### 3.2. Computation offloading
Offloading is the decision-making process of where to execute a task. Directions include end-device-to-end-device, device-to-cloud, and vertical/horizontal transfers across the mist-fog-cloud continuum.

### 3.3. Data management
This encompasses data acquisition, storage, and dissemination. It is more complex than cloud management due to the diverse geographic distribution of edge nodes.

### 3.4. Network management
Focuses on monitoring and dynamically adjusting network states using technologies like Software Defined Networking (SDN), Network Function Virtualization (NFV), and Cloud-RAN (C-RAN).

### 3.5. Security and privacy
Edge devices are more susceptible to physical attacks (e.g., cooling system attacks) than centralized data centers. However, EC enhances privacy by keeping sensitive data local.

### 3.6. EC pricing and billing
The market involves four main actors: clients, ISPs, cloud providers, and Edge Service Providers (ESPs), whose interrelations determine the cost of services.

### 3.7. Practical implications and potential applications of EC
*   **Autonomous Vehicles:** Enables real-time decision-making for safety.
*   **Smart Cities:** Supports traffic management and environmental monitoring.
*   **Healthcare:** Facilitates remote patient monitoring and rapid medical imaging diagnostics.
*   **Industrial Automation:** Allows predictive maintenance and real-time process control.
*   **Immersive Media:** Provides the low latency required for AR/VR gaming and training.
*   **Energy & Security:** Optimizes distributed energy resources (DERs) and enables local real-time video analytics for surveillance.

## 4. Resource allocation
Resource allocation focuses on solving task offloading, scheduling, and joint resource allocation problems to ensure Quality of Experience (QoE).

*   **Task Offloading:** Deciding "what" and "where" to offload. The paper provides mathematical models for computation capacity, data size constraints, latency ($l = \sum T_{local} + T_{offload}$), and energy consumption.
*   **Task Scheduling:** Assigning tasks to specific edge devices to minimize the overall makespan (completion time) and balance loads across heterogeneous hardware. 
*   **Joint Resource Allocation:** The coordination of CPU, memory, bandwidth, and storage across both mobile devices and servers. This requires adaptive algorithms—often based on Game Theory or AI—to handle the dynamic nature of edge environments.

### 4.1. Integrated sensing and communications (ISAC) in EC
ISAC allows wireless signals to simultaneously transmit data and sense the environment. In EC, this provides real-time context (user location/mobility), allowing for the dynamic adjustment of computational resources and energy conservation by putting servers into low-power states during sensed inactivity.

## 5. Lack of research
The authors identify two primary gaps in current research:
1.  **Scalability and Complexity:** Current systems struggle with the unpredictability of resource patterns and the diverse requirements of heterogeneous devices/applications in dynamic environments.
2.  **Global Resource Orchestration:** There is a lack of optimal offloading mechanisms for nodes distributed over wide geographic areas, particularly when dealing with mobility and strict resource constraints.

## 6. Edge computing and 5G/6G networks
EC and next-gen wireless networks are complementary. The paper notes that 5G allows the integration of IoT and cloud via edge platforms (demonstrated through test-beds for time-sensitive control loops). For 6G, a vision is presented where MEC functions are integrated into non-terrestrial platforms (satellites, aerial vehicles), creating "space-based MEC" for 3D on-demand intelligence.

*   **5G Applications:** Focuses on AR/VR, IoT data reduction, and smart city local processing.
*   **6G Potential:** Anticipates ultra-low latency haptic communication, distributed AI/ML models processed locally at the edge, and more granular network slicing for specific EC needs.

### 6.1. Synergy between edge intelligence and 5G/6G networks
Edge Intelligence integrates AI directly into edge nodes. When combined with 6G's high data rates and massive connectivity, it enables real-time learning and decision-making at the periphery, significantly enhancing data privacy and system responsiveness.

## 7. Contractual, reputational, and opportunistic wireless networking
To solve the "entropy problem" (the difficulty of discovering resources in a dynamic, heterogeneous environment), the authors propose **CROWN**.

**Core Concepts:**
*   **Resource Mapping:** Dynamically maps link ($l$), storage ($s$), and computation ($c$) capacity.
*   **OEDMA:** Transforms the NP-hard resource mapping problem into a convex optimization problem called "Orthogonal Entropy-Division Multiple Access" (OEDMA).
*   **PASS Metrics:** Projecting node availability onto three metrics: *Primacy* (selection rank), *Supremacy* (task suitability), and *Sway* (occupancy duration).

**Implementation Framework:**
1.  **Contractual and Opportunistic Broadcasting (COB):** Nodes proactively broadcast their context and available resources.
2.  **Proof of Reputation (POR):** Uses reinforcement learning to assign PASS values based on a node's historical performance.
3.  **Proof of Consensus (POC):** Utilizes blockchain for coordination and consensus on PASS values among nodes.

The goal is to move toward a completely decentralized, federated environment that democratizes computation resources, potentially leading to cost-free cloud services.

## 8. Discussion of the future EC and MEC
Future research must focus on:
*   **Interoperability:** Creating standards for diverse edge ecosystems to coexist.
*   **Vehicular Edge Computing (VEC):** Leveraging vehicles as both users and infrastructure to optimize traffic flow and safety.
*   **Sustainability:** Developing energy-efficient architectures and AI-driven power management as local computation increases.
*   **Security:** Implementing robust encryption and real-time threat detection for the distributed edge perimeter.

## 9. Conclusion
Edge computing is essential for real-time sensitive applications. While significant progress has been made in task offloading and resource allocation, gaps remain in security, server positioning, and hybrid system optimization. The future of the internet depends on a transition toward hybrid edge-cloud architectures capable of balancing small-scale real-time intelligence with large-scale centralized processing.
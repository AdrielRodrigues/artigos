---
index_terms:
  - optical network control
  - elastic optical networks
  - software defined networking
  - path computation element
  - network disaggregation
  - intent-based networking
  - zero-touch management
---

# Optical networks management and control: A review and recent challenges

## 1. Introduction
The paper traces the evolution of optical networking through four distinct eras, each influencing the required management and control architectures:
1. **Era of Regeneration:** Focuses on Wavelength Switched Optical Networks (WSON) where traffic is managed via lightpaths, constrained by wavelength availability and path length.
2. **Era of Amplified Dispersion-Managed Systems:** Introduces amplification; shifts from manual management to automatic calibration using impairment models or network probing.
3. **Era of Amplified Coherent Systems:** Marks the advent of Elastic Optical Networks (EON), utilizing advanced modulation formats and coherent detection to improve spectral efficiency and enable end-to-end performance monitoring via digital signal processing.
4. **Era of High Capacity Networking:** The current stage, exploring capacity increases through bands beyond C (e.g., E, S, L), orbital angular momentum (OAM) multiplexing, and space division multiplexing.

### 1.1. Management vs. control
The authors distinguish between two functional planes:
- **Management Plane:** Handles high-level planning, installation, configuration, and supervision (FCAPS: Fault, Configuration, Accounting, Performance, and Security). Traditionally centralized and manual, it is now moving toward automation and machine learning.
- **Control Plane:** Manages real-time topology discovery, routing, and signaling to automate connection establishment.
While early networks relied solely on the management plane for static provisioning, modern dynamic networks use a control plane (e.g., GMPLS or SDN) to allow network elements to autonomously establish switched connections, often bypassing the management plane during setup.

### 1.2. Wavelength switched optical networks (WSON)
WSONs utilize wavelength multiplexing to route traffic flows. Early provisioning was operator-driven and centralized. The introduction of the GMPLS protocol suite automated this process by managing Generalized Label Switched Paths (G-LSPs). The field is transitioning from a fixed ITU-T grid (50 GHz spacing), which limits rates above 100 Gb/s, to a flexible DWDM grid using slots in multiples of 12.5 GHz.

### 1.3. Elastic optical networks
EONs aim for higher spectral efficiency and better resource matching through:
- **Flexible Grid:** Replaces fixed spacing with configurable slot widths based on actual bandwidth requirements.
- **Enabling Hardware:** Bandwidth-variable Wavelength Selective Switches (BV-WSS) allow filtering of configurable spectrum portions, and bandwidth-variable transponders support multiple rates and modulation formats. This elasticity can reduce fiber spectrum usage by approximately 30%.

### 1.4. Data center networks
To address the massive growth in intra-data center traffic and the power/bandwidth limits of electronic switching, optical interconnects are being introduced. The primary challenge is implementing effective controllers and schedulers that ensure low packet latency and high throughput.

### 1.5. Physical layer issues
Optical signal quality (Quality of Transmission - QoT) is degraded by linear effects (attenuation, chromatic dispersion) and non-linear effects (SPM, XPM). To manage this, operators typically use "margins"—pessimistic buffers added to OSNR estimations—to ensure stability despite worst-case scenarios (e.g., all channels lit). While distributed QoT-aware setup has been proposed via GMPLS extensions, the complexity of these computations often necessitates centralized elements like a Path Computation Element (PCE) or SDN controller.

## 2. Distributed optical network control
Distributed control requires a separate network for the control plane to ensure that data plane failures do not disable the ability to recover the network.

### 2.1. Generalized multiprotocol label switching (GMPLS)
In GMPLS, each node has a control agent. The framework relies on three main protocols:
- **OSPF-TE:** Advertises topology and traffic engineering information.
- **RSVP-TE:** Handles resource reservation via *Path* (forward) and *Resv* (backward) messages.
- **LMP:** Monitors point-to-point links.
A key issue in this distributed model is "backward blocking," where a connection fails during the *Resv* phase due to resource contention, necessitating multiple signaling attempts or protocol extensions.

### 2.2. The Path Computation Element (PCE)
To resolve sub-optimal routing and resource contention inherent in fully distributed control, the PCE provides centralized path computation. It communicates with node agents via the PCEP protocol. While a PCE improves resource utilization and can account for physical impairments more effectively, it may introduce activation delays during restoration due to communication overhead and queuing.

### 2.3. Control of multidomain optical networks via PCE and GMPLS
Scalability limits prevent full resource advertisement across domains. The paper identifies several inter-domain strategies:
- **Per-domain computation:** Path segments are computed sequentially as signaling moves through domains.
- **Inter-PCE computation:** End-to-end paths are computed before signaling, often using backward recursive PCE-based computation (BRPC).
- **Hierarchical PCE (H-PCE):** A parent PCE (pPCE) coordinates domain sequences and end-to-end paths, while child PCEs (cPCE) handle intra-domain segments.

## 3. SDN-based control in optical network
Software Defined Networking (SDN) decouples the data plane (forwarding hardware) from the control plane (software logic), managed by a centralized SDN Controller.

### 3.1. SDN vs GMPLS optical networks
While OpenFlow was an early interface, its packet-centric nature is limited for optical layers; NETCONF/YANG has become the de facto standard due to its model-based approach. Comparisons indicate that SDN's centralized path computation and parallelized signaling significantly reduce both provisioning and restoration times compared to GMPLS.

### 3.2. Disaggregated optical networks
Disaggregation separates hardware (white boxes) from software via open interfaces (e.g., YANG). Two types exist:
- **Partial Disaggregation:** Only transponders are vendor-neutral; the rest of the line system remains proprietary.
- **Full Disaggregation:** Includes ROADMs as white boxes. 
Initiatives like OpenConfig and OpenROADM aim to eliminate vendor lock-in.

### 3.3. Optical network slicing
Disaggregation enables "network slicing," where a physical infrastructure is partitioned into multiple virtual networks. This is achieved via device hypervisors that ensure performance and connectivity isolation by dedicating specific physical resources (e.g., media channels) to each slice.

## 4. Multi-layer network control

### 4.1. Packet-optical networks
SDN allows for joint configuration of packet and optical layers. The authors describe an orchestrator (e.g., Open Source MANO) that coordinates computational resources (OpenStack) and networking resources (ONOS). An example provided is a video streaming service where a failure triggers the simultaneous activation of a new optical lightpath and the reconfiguration of IP/MAC flow rules at the packet switch to redirect users to a backup server.

### 4.2. Multi-domain orchestration
Future B5G telco clouds will involve Core, Metro, and Edge Data Centers (DCs). The core challenge is balancing two opposing latency components: **network latency** (higher for distant Core DCs) and **processing latency** (higher for resource-constrained Edge DCs). Orchestration must balance resource utilization rates against the risk of SLA violations.

### 4.3. Open network database for multilayer networks
To avoid the inefficiency of segregated Traffic Engineering Databases (TEDs), the authors propose an Open Network Database (ONDB). This independent, shared distributed database stores protocol-independent topology and TE information from different layers/domains. Experimental results show that ONDB can perform inter-layer correlation (e.g., for link maintenance) in a few milliseconds across 100 nodes.

## 5. Advanced control and management techniques

### 5.1. Autonomous optical networks
To reduce the inefficiency of conservative margins, "autonomous" networks use an **observe-decide-act** loop. Real-time monitoring allows the network to re-adapt parameters (e.g., modulation format or FEC) on the fly. If performance degrades, the system can switch from PM-16QAM to PM-QPSK; while this reduces the bit rate, it increases robustness. Hierarchical architectures are proposed to handle the massive amount of monitoring data and avoid controller bottlenecks.

### 5.2. P4-based programmable data plane
The P4 language allows for a programmable data plane, enabling wire-speed, stateful forwarding decisions without waiting for the SDN controller. Key advantages include:
- **In-band telemetry:** Custom headers allow real-time network observation.
- **Stateful objects:** Counters and meters enable context-aware traffic engineering directly at the node level.

### 5.3. Intent-based networking (IBN)
IBN shifts from imperative ("how") to declarative ("what") management. Users express high-level "Intents" (e.g., "ensure high availability for gold users"), which an Intent Layer translates into specific configurations. This layer operates a closed-loop workflow consisting of **fulfillment** (deployment) and **assurance** (continuous verification and tuning).

## 6. Recent research challenges

### 6.1. Zero-touch network and service management in optical networks
ZSM aims for fully autonomous operation using AI/ML for predictive analytics (e.g., forecasting traffic to scale resources proactively). The authors map ZSM functions to the OODA loop (Observe, Orient, Decide, Act), noting that the overall system response time depends heavily on the delay of data exchange between these functional elements.

### 6.2. Telemetry-based optical network control
Traditional polling (SNMP) is too slow for modern requirements. New telemetry services utilize gRPC and protobuf to stream real-time transmission parameters from devices to collectors at sub-second intervals, enabling proactive SDN routines and faster failure localization.

### 6.3. Optical packet switching in data center networks
The paper analyzes two segments:
- **Inter-rack:** Uses architectures like rings, Torus, or Clos. Focus is on fast schedulers (implemented in FPGA/ASIC) to manage wavelength assignment.
- **Intra-rack:** Employs multi-plane switching (e.g., combining space and wavelength domains) to improve scalability. High-performance schedulers have demonstrated the ability to handle up to 1000 ports with microsecond computation times.

## 7. Conclusions
Optical network control has evolved in a circular fashion: starting as centralized (Management Plane), moving to distributed (GMPLS), then partially centralized (PCE), and finally returning to a fully software-defined centralized model (SDN). The trend is now moving toward total autonomy through IBN, ZSM, and programmable data planes (P4) to meet the stringent latency requirements of next-generation networks.
---
index_terms:
  - reconfigurable optical networks
  - data center networks
  - wide area networks
  - wavelength selective switching
  - software defined networking
  - elastic optical networks
---

# A Survey of Reconfigurable Optical Networks

## 1. Introduction
The surge in communication traffic driven by AI, machine learning, and data-centric applications has necessitated a shift toward optical communication due to its high bandwidth and energy efficiency. Reconfigurable optical networks (RONs) provide the ability to adapt network topology in data centers and capacity in wide-area networks (WANs), allowing infrastructure to be demand-aware rather than statically over-provisioned.

### 1.1. Novelty and Contribution
This paper provides an end-to-end perspective on RONs, bridging the gap between optical hardware technologies and the algorithms/systems that manage them. A clustering analysis of networking journals reveals a significant divide between physical-layer optical research and higher-layer networked systems research; this survey aims to unify these domains.

### 1.2. Scope
The survey focuses on enterprise and core networks, specifically addressing data centers and WANs, while excluding last-mile passive optical networks or mobile front-haul.

### 1.3. Organization
The document is structured to move from network architecture models (Section 2) and hardware foundations (Section 3) to specific applications in data center networks (Section 4) and wide-area networks (Section 5), concluding with open challenges (Section 6).

## 2. Network Architectures
Reconfigurable optics are integrated into two primary architectural models: IP-over-OTN for long-haul transport and hybrid electric-optical fabrics for data centers.

### 2.1. IP-over-Optical Transport Network
The IP-over-OTN (ITU-T G.709) model connects hosts to routers, which then connect via an optical transport network utilizing Optical Cross-Connects (OXCs). Data is transmitted as "lambdas" (wavelengths/circuits). Historically, these networks were statically over-provisioned with redundant fiber and DWDM channels to accommodate worst-case traffic surges.

### 2.2. Data Center Architecture
To avoid the cost of massive packet-switched fabrics, modern data centers use hybrid architectures where bandwidth between hosts can change periodically via optical circuit switching (OCS). These systems use either fixed deterministic scheduling or demand-aware changes based on mutual connectivity requests.

### 2.3. Software Defined Networking
SDN decouples the control and data planes, enabling centralized management of optical paths. This allows for better utilization of bandwidth and latency policies by adapting the physical layer in a demand-aware manner.

### 2.4. Elastic Optical Networks (EONs)
Unlike fixed-grid networks with rigid frequency spacing (e.g., 50 GHz), EONs (or flex-grid networks) allow channel widths and center frequencies to be multiples of smaller slots (6.25 GHz and 12.5 GHz). This improves spectral efficiency but introduces the problem of spectrum fragmentation.

### 2.5. Summary
The transition toward SDN and EONs allows both data centers and WANs to move from static provisioning to a more flexible, demand-responsive infrastructure.

## 3. Enabling Hardware Technologies
Hardware serves as the foundation for RON systems, with recent advances focusing on reducing loss, increasing switching speed, and lowering costs via silicon photonics.

### 3.1. Wavelength Selective Switching
Wavelength Selective Switches (WSS) enable the creation of optical circuits:
- **Polymer Waveguides:** Low-cost architectures using Array Waveguide Gratings (AWG). Recent use of fluorocarbons has reduced signal loss, enabling speeds below 820 ps.
- **Microelectromechanical Systems (MEMS):** Use tiny mirrors to reflect light. They are slower than polymer waveguides due to physical mirror movement but offer lower insertion loss and higher flexibility.
- **Liquid Crystal on Silicon (LCOS):** Uses diffraction gratings and voltage-controlled pixels to steer light. Response times range from 10–100 $\mu$s, offering a modular design without moving parts.

### 3.2. ROADMs
Reconfigurable Add-Drop Multiplexers (ROADMs) allow operators to add or drop wavelengths without electronic conversion:
- **C-ROADM (Colorless):** Independent of specific light frequencies.
- **CD-ROADM (Directionless):** Allows waves to travel in any direction, though it may suffer from port contention.
- **CDC-ROADM (Contentionless):** Uses shared add/drop ports to eliminate contention.
- **CDC-F (Flex-grid):** Supports non-uniform grid alignment for Elastic Optical Networks.

### 3.3. Bandwidth-Variable Transponders
Transponders use modulation formats (OOK, QPSK, QAM) to determine bits per symbol based on the Signal to Noise Ratio (SNR). Bandwidth Variable Transponders (BVTs) allow programmable modulation and baud rates, trading off capacity for reach (e.g., using QPSK for long distances and 16-QAM for short reaches). Sliceable-BVTs (S-BVT) further reduce waste by propagating multiple channels simultaneously.

### 3.4. Silicon Photonics
Silicon photonics (SiP) leverages CMOS manufacturing to lower hardware costs. While silicon faces challenges like coupling loss, the integration of Indium Phosphide (InP) lasers on chips has significantly reduced power loss and improved in-line amplification.

### 3.5. Summary
The convergence of fast WSS, flexible ROADMs, and S-BVTs—all accelerated by SiP—is making high-radix, low-cost reconfigurable optics commercially viable.

## 4. Optically Reconfigurable Data Centers
DCNs face the challenge of highly variable communication patterns between Top-of-Rack (ToR) switches across different applications.

### 4.1. DCN-specific Technologies
- **Free-space Optics (FSO):** Light propagates through air using Digital Micromirror Devices (DMDs) and ceiling-mounted mirrors ("disco-balls"). This reduces cabling but is susceptible to atmospheric attenuation and physical misalignment.
- **Sub-second Switching:** Short distances in DCNs allow for microsecond or even nanosecond reconfiguration. However, such speed requires adjustments to TCP buffer sizes and host behaviors to prevent throughput drops.

### 4.2. Cost Modeling
Quantitative models are used to justify the transition from Packet Switched Only (PSO) networks. Simulations show that using optical circuits can reduce rack-to-rack traffic by up to 50% compared to static topologies.

### 4.3. Algorithms
Establishing optimal optical paths requires various algorithmic strategies:
- **Matchings:** Using maximum weight or $b$-matching to maximize throughput and latency.
- **Oblivious Approaches:** Cycling through a fixed set of matchings (e.g., RotorNet) to provide periodic connectivity without computing real-time demand.
- **Traffic Matrix Scheduling:** Computing schedules based on snapshots of traffic demand, often using Birkhoff-von Neumann decomposition to create sequences of reconfigurations.
- **Self-Adjusting Data Structures:** Inspired by splay trees and Huffman coding, these algorithms make local, rapid changes to strike a balance between reconfiguration cost and routing benefit.
- **Machine Learning:** Utilizing neural networks for traffic-driven topology adaptation (e.g., xWeaver).
- **Additional Aspects:** Using edge-coloring to avoid signal interference in shared mediums and optical splitters for multicast implementations.

### 4.4. Systems Implementations
Implementations differ by fabric choice (hybrid electric-optical vs. all-optical) and control plane (demand-aware vs. oblivious). Hybrid designs are superior for short-lived flows, while all-optical oblivious designs (e.g., Sirius) provide nanosecond reconfiguration but may struggle with skewed traffic demands.

### 4.5. Summary
While DCN reconfigurability offers huge potential, the main hurdle remains scaling demand-aware control planes to match the speed of the underlying hardware.

## 5. Reconfigurable Optical Metro and Wide-Area Networks
WAN reconfigurability focuses on adapting capacity (via BVTs) and steering light paths rather than changing physical topology.

### 5.1. Metro/WAN-specific Challenges and Solutions
- **Chromatic Dispersion:** Different wavelengths travel at different speeds, causing pulse broadening; DWDM systems must actively manage this.
- **ASE Noise:** Adding/removing channels requires adjusting amplifier gain to maintain SNR. Machine learning (Case-Based Reasoning) is used to optimize these settings quickly.
- **Synchronization:** Management relies on protocols like SNMP and NETCONF, or the 3-way handshake (3WHS) for reserving paths via an out-of-band optical supervisory channel.

### 5.2. Cost Modeling
WAN fiber is extremely expensive. Research shows that joint IP/Optical layer optimization can reduce transponder requirements by 40-60%. Other models analyze the capacity gains of CDC-ROADMs over C-ROADMs and optimize the placement of regenerators to improve service velocity.

### 5.3. Algorithms
WAN algorithms focus on shifting bandwidth across fixed fiber edges:
- **Routing & Resilience:** Using shortest lightpath routing and Integer Linear Programs (ILP) to ensure SLRG-diverse routes for fault tolerance.
- **Bulk Transfers:** OWAN uses simulated annealing for sub-second wavelength allocation; DaRTree employs Steiner Tree heuristics for multicast transfers under deadlines.
- **Traffic Engineering (TE):** OptFlow uses "fake links" in the IP layer to allow standard TE tools to optimize dynamic optical capacities without needing a total redesign of the TE system.
- **AI and VNF Embedding:** Using deep learning for circuit activation and ranking heuristics to embed Virtual Network Function (VNF) service chains into elastic optical networks.

### 5.4. Systems Implementations
Notable systems include RADWAN (focusing on rate-adaptive transceivers to increase throughput by 40%) and CORONET (demonstrating Bandwidth-on-Demand). The *Iris* system reduces complexity by switching at the fiber-strand level, avoiding the need for frequent amplifier reconfiguration.

### 5.5. Summary
WAN reconfigurability requires intense cross-layer coordination to manage physical impairments while meeting high-level performance metrics.

## 6. Open Challenges in Reconfigurable Optical Networks
The authors identify critical gaps across three domains:
- **Hardware:** Reducing the cost of CDC-F ROADMs and mitigating signal loss at WSS modules via silicon photonics.
- **Data Centers:** Standardizing the modeling of reconfiguration costs, developing constant-factor approximation algorithms for NP-hard topology problems, and improving online predictive routing.
- **Metro/WANs:** Establishing standardized white-box system stacks (e.g., OpenConfig) and automating power coordination across long-haul amplifiers.

## 7. Conclusion and Future Work
Reconfigurable optical networks are an emerging field where the trade-offs between cost, resilience, and performance are not yet fully understood. The authors emphasize a critical need for better models of reconfiguration costs and a determination of whether centralized or decentralized control planes are more effective for future deployments.
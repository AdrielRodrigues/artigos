---
index_terms:
  - elastic optical networking
  - 5G transport networks
  - network slicing
  - centralized radio access network
  - software defined optical networking
  - bandwidth variable transponders
---

# Elastic Optical Networking for 5G Transport

## 1 Introduction
The transition to 5G introduces a diverse set of use cases—ranging from massive broadband and high-definition media to ultra-reliable machine-type communication (uMTC) and tactile Internet—each with conflicting quality of service (QoS) requirements regarding latency, jitter, reliability, and bandwidth. To avoid "one-size-fits-all" architectures, 5G employs a networks-as-a-service model utilizing network slicing and Network Function Virtualization (NFV). These slices span multiple domains: wireless radio, access/metro/core transport networks, and geographically distributed data centers (DCs) hosting the Evolved Packet Core (EPC).

Current transport architectures based on 4G LTE are hindered by decentralized baseband processing at antenna sites and proprietary hardware for EPC functions. While IP-over-WDM/DWDM is used in metro/core segments, these fixed-grid technologies are insufficient for 5G due to rigid spectrum allocation, poor resource utilization, high capital expenditure (CapEx), and an inability to dynamically scale based on slice demands. Elastic Optical Networks (EONs) emerge as the solution by providing flexible grid spectrum allocation, programmable devices, and adaptive modulation to satisfy the massive capacity and dynamic scaling needs of 5G.

## 2 Fixed-Grid and Elastic Optical Networks

### 2.1 Conventional Fixed-Grid Optical Networks
Fixed-grid networks (WDM/DWDM) operate as circuit-switched systems where lightpaths are established using fixed spectral widths defined by ITU-T G.694.1 (typically 12.5, 25, 50, or 100 GHz). These networks utilize transponders and Optical Add/Drop Multiplexers (OADMs) or Re-configurable OADMs (ROADMs) with Wavelength Selective Switches (WSS). A primary constraint is the wavelength continuity constraint, requiring a lightpath to maintain the same wavelength across all links.

Major limitations include:
- **Spectrum Waste:** Mandatory guardbands between adjacent channels and the "fixed width" nature lead to significant underutilization when demand does not perfectly match the grid size.
- **Rigidity:** Reconfiguration often requires hardware changes, as modulation levels are tied to specific transponder types.
- **Traffic Grooming Overhead:** To minimize wastage, electronic grooming is used at the IP/MPLS layer. This necessitates optical-electrical-optical (O-E-O) conversions at intermediate nodes, increasing latency and power consumption.

### 2.2 Elastic Optical Networks (EONs)
EONs replace fixed wavelengths with small, flexible frequency units called sub-carriers. Using techniques like Orthogonal Frequency Division Multiplexing (OFDM), multiple adjacent sub-carriers are aggregated to create a channel tailored to the specific bandwidth demand of a connection. EONs are governed by spectrum contiguity (sub-carriers must be adjacent) and continuity constraints.

Key enabling technologies include:
- **Bandwidth Variable Transponders (BVTs) and Sliceable BVTs (S-BVTs):** These allow software-configurable modulation formats (e.g., BPSK, QPSK, x-QAM), enabling a trade-off between optical reach and spectral efficiency.
- **Bandwidth Variable Optical Cross-Connects (BVOXCs):** These replace WSS to provide flexible spectral switching windows.
- **Digital Signal Processing (DSP):** Enables the dynamic adjustment of bit rates, FEC, and modulation based on distance and demand.

EONs overcome fixed-grid limitations by eliminating guardbands between sub-carriers, reducing transponder counts through virtualization via S-BVTs, and enabling hitless software-defined reconfiguration of lightpaths to match time-varying traffic. Optical layer grooming is also possible, removing the need for O-E-O conversions.

## 3 EON in 5G Transport Networks

### 3.1 Challenges in 5G Access Transport Networks
Traditional Distributed RAN (D-RAN) architectures are too costly and power-hungry for the dense small-cell deployments required by 5G and suffer from poor inter-cell interference coordination. Consequently, 5G shifts toward Centralized RAN (C-RAN), where Baseband Units (BBUs) are pooled in central offices or edge DCs. While C-RAN improves resource use and enables Coordinated Multipoint (CoMP) transmission, it places extreme demands on the access transport network:
- **Capacity:** Massive data rates for digital/analog Radio-over-Fiber (RoF) and M-MIMO.
- **Latency:** Extremely strict synchronization and timing requirements for centralized radio coordination.
- **Dynamicity:** The need to dynamically pair RRUs with BBUs in a pool based on traffic fluctuations.

### 3.2 How EON Can Help (Access Transport)
EONs address C-RAN challenges by providing the granularity needed to support diverse signals (analog and digital RoF) on a single fiber. Unlike fixed-grid networks, EONs facilitate "any-to-any" RRU-BBU assignments through S-BVTs and software-defined reconfiguration, which is essential for BBU pooling and improved CoMP. Additionally, by performing grooming at the optical layer and avoiding O-E-O conversions, EONs significantly reduce end-to-end latency and energy consumption compared to electronic grooming.

### 3.3 Challenges in 5G Core Transport Networks
Core networks face an aggregate data rate increase of roughly 1000x compared to 4G, requiring Tbps transmission rates. Traffic is highly unpredictable due to user mobility and "tidal" phenomena (e.g., flash crowds). The current EPC architecture's reliance on proprietary hardware prevents elastic scaling; specifically, the tight coupling of control and user planes in SGW and PGW leads to poor resource utilization because their scaling requirements differ (CPU-bound vs. I/O-bound).

### 3.4 How IP-Over-EON Can Help (Core Transport)
Integrating EONs with a Software Defined Networking (SDN) controller creates a Software Defined Elastic Optical Network (SDEON). This architecture supports the virtualized EPC by:
- **High Capacity:** Achieving Tbps rates via adaptive modulation and variable spectrum widths more efficiently than inverse multiplexing in DWDM.
- **Cost Reduction:** S-BVTs reduce the number of required IP routers and BVOXC ports through virtualization, lowering CapEx and OpEx.
- **VNF Optimization:** The SDEON controller uses global network knowledge to optimally place virtualized network functions (VNFs) and establish QoS-aware lightpaths (e.g., assigning latency-sensitive slices to the shortest paths).

## 4 Research Directions

### 4.1 What has been Done
Prior research largely focused on WDM/DWDM for C-RAN, optimizing BBU placement and routing but remaining limited by fixed-grid rigidity. Recent experimental work has begun exploring EONs: demonstrating elastic lightpath provisioning between RRUs and BBUs in SDN testbeds and proposing SDEON architectures for the mobile core to handle load balancing and handovers.

### 4.2 What can be Done
The authors identify several open research challenges for full EON deployment in 5G:
- **Joint Optimization:** Developing algorithms that simultaneously optimize RRU-BBU assignment, routing, spectrum, and modulation while respecting strict latency/sync constraints and the physics of optical reach.
- **Traffic Prediction:** Using Deep Learning to predict mobile traffic patterns, allowing the network to allocate "just-enough" resources and achieve statistical multiplexing gains.
- **Spectrum Defragmentation:** Creating hitless, reactive defragmentation strategies to combat spectrum fragmentation caused by high churn in 5G demands.
- **Differentiated Survivability:** Developing protection schemes that provide different levels of reliability based on the specific QoS requirements of a network slice.
- **Energy Management:** Implementing intelligent sleep modes for EON devices and developing new energy harvesting techniques integrated with optical bypass.
- **Control Plane Evolution:** Extending existing protocols (GMPLS, OSPF, RSVP-TE) or designing new SDN-based orchestration layers to manage end-to-end connectivity across wireless, transport, and DC domains.

## 5 Conclusion
The demands of 5G—virtualization, slicing, and massive capacity—require a transport network that is flexible and programmable. Fixed-grid WDM/DWDM technologies are too rigid and costly to support these needs. Elastic Optical Networking (EON), through the use of S-BVTs, BVOXCs, and software-defined control, provides the necessary resource efficiency and scalability to enable 5G's disruptive capabilities in both access and core transport domains.
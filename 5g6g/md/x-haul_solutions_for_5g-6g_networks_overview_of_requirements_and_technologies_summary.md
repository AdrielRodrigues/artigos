---
index_terms:
  - x-haul networks
  - 5G/6G RAN
  - Passive Optical Networks
  - Functional Splits
  - Network Slicing
  - Cloud-RAN
  - Fiber Optic Transport
---

# X-haul solutions for 5G/6G networks: Overview of requirements and technologies

## 1. Introduction
The shift toward ultra-dense heterogeneous networks (HetNets) in 5G and the projected goals of 6G have shifted the capacity bottleneck from the Radio Access Network (RAN) to the transport network. The author defines **x-haul** as a collective term for three layers in Cloud-RAN (C-RAN) architecture: **fronthaul** (connecting remote radio heads [RRH] to baseband units [BBU]), **midhaul** (linking gNBs/eNBs via the X2 interface), and **backhaul** (connecting aggregation points to the core network via the S1 interface).

The paper contrasts different architectures:
- **C-RAN**: Centralizes BBUs for better resource management.
- **D-RAN**: Distributed architecture.
- **F-RAN (Fog RAN)**: Integrates C-RAN with fog computing and AI at the edge to improve Quality of Service (QoS) through caching and real-time processing.

5G use cases—enhanced mobile broadband (**eMBB**), massive machine-type communication (**mMTC**), and ultra-reliable low latency communication (**URLLC**)—drive specific transport demands. 6G is expected to extend these with **Computation-oriented communications (CoC)**, **Contextually agile eMBB (CAeC)**, and **Event-defined URLLC (EDURLLC)**, targeting data rates up to 10 Tbps and latency below 1 ms.

## 2. X-haul requirements
X-haul design is driven by bandwidth, latency, reliability, and energy efficiency. Massive MIMO (mMIMO) and coordinated multipoint (CoMP) specifically necessitate ultra-low latency and high bandwidth in ultra-dense deployments.

### 2.1. Functional splits
The division of the physical (PHY) layer between the Radio Unit (RU) and Distributed Unit (DU) determines transport load:
- **Option 7.1**: High performance but demands maximum bandwidth and minimum latency.
- **Option 7.2**: Reduces bandwidth requirements relative to 7.1 by combining signals from multiple antenna ports.
- **Option 7.3**: Moves modulation/demodulation to the RU, significantly lowering capacity demands (e.g., from ~4 Gbps in Option 7.1 to ~134 Mbps for specific configs) but increasing RU complexity.

### 2.2. X-haul challenges in terms of mobile network KPIs
The author identifies several critical challenges:
- **Network Capacity**: Fronthaul rates scale with antenna count and sampling rates. For a $32\times32$ MIMO mmWave setup at 3.5 GHz, the required CPRI rate can reach ~162 Gbps per sector.
- **Configuration**: High densification of small base stations (SBSs) requires wavelength or time multiplexing to avoid excessive fiber counts.
- **Availability and Latency**: Wireless solutions are prone to weather interference. Fronthaul round-trip time (RTT) must be kept well below the Timing Advance (ADV) window, typically targeting 200–500 $\mu$s with an accuracy of $\pm130$ ns.
- **Cost and Coverage**: Convergence with Fiber-to-the-Home (FTTH) networks is suggested as a cost-reduction strategy for urban deployments.

The paper provides projections for bandwidth/latency requirements across three scenarios: Small Cell, Macro Cell, and Ultra Dense. In 6G, fronthaul demands are expected to reach 120–250 Gbps in ultra-dense environments with latency $\le 50 \mu\text{s}$.

### 2.3. Cloud-RAN
In C-RAN, the degree of functional centralization determines transport pressure. Higher centralization (moving more functions to the BBU) increases capacity and reliability requirements on the fronthaul, regardless of actual user traffic. Therefore, x-haul capabilities must be considered jointly with the choice of functional split.

### 2.4. Control/user plane split
Control/User Plane Split (CUPS) offloads user plane data to small cells while keeping coordination and signaling at the macro cell level. This minimizes frequent handovers in dense networks but requires very low-latency backhaul for efficient synchronization via SDN controllers.

### 2.5. Softwarization
Software Defined Networking (SDN) and Network Function Virtualization (NFV) enable programmable, multi-vendor interoperable networks.
- **Benefits**: Up to 14% CAPEX reduction through optimized routing and resource allocation.
- **Drawbacks**: Increased signaling load on physical links due to the separation of control and data planes; heightened security risks from external breaches.
- **Emerging Trends**: Use of AI/ML for fault management, traffic prediction, and "Digital Twins" for network optimization.

### 2.6. Energy efficiency
Fiber optics, particularly Passive Optical Networks (PON), are more energy-efficient than microwave solutions. Optimization is achieved through Dynamic Bandwidth Allocation (DBA) in PONs, Radio-over-Fiber (RoF), and the use of SDN to enable low-power routing hardware.

### 2.7. Network slicing
Slicing creates independent virtual networks on shared physical infrastructure. The pressure on different x-haul segments depends on the slice type:
- **s-VCC (mMTC)**: Low volume, high reliability $\rightarrow$ primarily pressures the fronthaul.
- **eRTC (URLLC)**: High volume, <1ms latency $\rightarrow$ primarily pressures the aggregation layer (~55% of traffic).
- **eMBB**: High throughput $\rightarrow$ primarily pressures midhaul and backhaul.

### 2.8. Additional 6G requirements
6G introduces new spectral and architectural demands:
- **Spectrum**: Focus on FR3 (7–24 GHz) for capacity/propagation balance, and THz bands (100 GHz–3 THz) for rates up to 1 Tbps. THz faces extreme air loss, requiring ultra-dense infrastructure.
- **RIS**: Reconfigurable Intelligent Surfaces introduce a new backhaul segment between base stations and RIS elements, increasing control plane latency.
- **Edge Cloud**: Moving computation closer to the RAN reduces x-haul distance and overall system latency.
- **Intelligentization**: Shift toward "network of subnetworks" utilizing AI for predictive maintenance and dynamic resource allocation.

## 3. Review of current solutions and emerging trends in x-haul networks

### 3.1. Wired X-haul solutions
Fiber is the gold standard due to bandwidth and reliability but is limited by high deployment costs. Copper (Ethernet/DSL) is considered outdated for 5G/6G demands.

### 3.2. Wireless X-haul solutions
Wireless options are cost-effective but weather-dependent:
- **mmWave (30–300 GHz)**: High data rates (1–2 Gbps), short reach, and requires strict Line-of-Sight (LoS).
- **Microwave (6–60 GHz)**: Longer reach (~50 km) but lower spectral efficiency; susceptible to rain/fading.
- **THz (300 GHz–3 THz)**: Potential for 100 Gbps+, but range is severely limited (<100m with directional antennas).
- **Free Space Optics (FSO)**: Uses lasers in air; license-free and high capacity. It can reduce deployment costs by 50% vs fiber but fails in fog or heavy rain.
- **Satellites**: LEO/HTS satellites provide connectivity for sparse areas where terrestrial infra is unavailable.

## 4. Fiber optics as a x-haul solution in 5G/6G networks

### 4.1. Topology
- **Point-to-Point (PtP)**: High security and OAM, but expensive. BiDi PtP standards now support up to 50 Gbps over 40 km.
- **Point-to-Multi-Point (PtMP)**: More cost-effective; PON solutions can reduce backhaul costs by up to 60%.

### 4.2. Enabling fiber optic technologies
Capacity increases are driven by Space Division Multiplexing (SDM) and Multi-core fibers (MCF). Analog Radio-over-Fiber (A-RoF) allows for higher centralization of RF oscillators at the central office. Ribbon fibers reduce physical footprint, while ROADMs enable intelligent, reconfigurable WDM networks.

### 4.3. PON solutions
PONs are highlighted as the most cost-effective fiber solution. The author evaluates several types against NG-PON2 standards:
- **TDM-PON**: Evolving from GPON to 50G-PON and eventually VHSP (100–200 Gbps by 2035). Upstream latency remains a bottleneck.
- **WDM-PON**: Dedicated wavelengths per ONU; low latency and high scalability, but expensive transceivers make it less viable for some 5G scenarios.
- **TWDM-PON**: A hybrid of TDM and WDM. It is identified as the **most promising solution** for mobile fronthaul due to its balance of cost, capacity, and flexibility.
- **OFDM-PON**: High spectral efficiency in downstream via DSP; unsuitable for upstream due to lack of coordination.
- **OCDMA-PON**: Uses optical codes for asynchronous access but is currently impractical due to immature photonic encoders/decoders.
- **SDM-PON**: Uses MCFs to create parallel spatial channels; avoids complex MIMO-DSP if weakly coupled cores are used.
- **NOMA-PON**: Employs power-domain multiplexing and Successive Interference Cancellation (SIC) to increase user capacity in 6G fronthaul.
- **PDM-PON**: Uses polarization states for $\ge 100$ Gbps per wavelength; promising for high-performance needs.

## 5. Conclusions
X-haul must be tailored to specific RAN deployments. While wireless solutions (mmWave, FSO, THz) provide cost advantages in certain contexts, fiber optics remain the future-proof solution. Among fiber options, TWDM-PON is singled out as the most viable candidate for next-generation mobile fronthaul because of its ability to flexibly handle both time and wavelength resources.
---
index_terms:
  - Multiband Optical Networks
  - Spatial Division Multiplexing
  - Software Defined Networking
  - Model Driven Development
  - Transport API
  - Physical Layer Impairments
  - Routing and Spectrum Assignment
  - Multigranular Optical Nodes
---

# Overview of SDN control of multiband over SDM optical networks with physical layer impairments [Invited Tutorial]

## 1. Introduction
The increasing demand for network capacity necessitates a transition from traditional C-band systems to multiband (MB) and eventually Spatial Division Multiplexing (SDM). While SDN principles have matured for C-band, MB and SDM introduce heterogeneity in devices and complex physical layer impairments (PLIs), rendering previous assumptions of quasi-uniform channel behavior obsolete. The paper aims to provide an overview of the control plane design required to support Multiband over SDM (MBoSDM).

### A. Optical Transport Networks and Technologies for Capacity Scaling
Multiband transmission exploits additional spectrum (S, E, O, and U bands) to maximize existing fiber infrastructure and reduce CapEx. However, this introduces nonlinear effects such as Stimulated Raman Scattering (SRS), causing power transfer between wavelengths, and requires band-specific components (amplifiers, lasers). In the long term, SDM provides further scaling via multicore fibers or fiber bundles. The paper argues that while switching at the highest WDM layer yields better performance (lower blocking rates), optical bypass at lower layers is more cost-efficient for specific traffic patterns.

### B. Flexigrid Reference Network for Control and Management
The authors define a reference terminology for control:
*   **Optical Tributary Signal (OTSi):** A unidirectional signal within a network media channel.
*   **OTSi Group (OTSiG):** A set of OTSis supporting one digital client, requiring co-routing and controlled differential delay.
*   **Media Channel (MC) & Network Media Channel (NMC):** An MC represents a frequency slot/range on a specific path; an NMC is the end-to-end equivalent between transceiver ports.
*   **Media Channel Group (MCG):** A management abstraction for co-routed media channels. This includes **Optical Transmission Sections (OTS)** (between amplifiers) and **Optical Multiplex Sections (OMS)** (between filter/coupler ports).

## 2. SDN Control of Multiband Networks

### A. Software Defined Networking and Model Driven Development
Modern optical control relies on Model Driven Development (MDD), using standardized data models (YANG) and transport protocols (NETCONF/RESTCONF, gNMI). The architectural trend is moving from monolithic controllers toward modular, service-based architectures that separate configuration/control from monitoring/telemetry.

### B. Challenges to the SDN Control of Multiband Networks
Dynamic provisioning in MB networks faces three primary challenges:
1.  **Functional Architecture:** Monolithic systems are replaced by modular functions (e.g., externalized path computation) and "separation of concerns." A key development is **controller telemetry**, where control plane components act as streaming data sources to synchronize state across hierarchical controllers or Digital Twins (DT).
2.  **Path Computation and Resource Allocation:** The process involves Routing and Spectrum Assignment (RSA). This includes finding a topological path and assigning resources (band, core, frequency slot). Path computation is increasingly decoupled from **path validation**, which uses analytical or AI/ML models (e.g., GNPy) to estimate Quality of Transmission (QoT).
3.  **Modeling Aspects:** There is a need to shift from "implicit band" assumptions to "per-band" parameter grouping, using profiles to group invariant data and ensure scalability.

## 3. Modeling and Data Models for Multiband

### A. Modeling Multiband Transmission
Multiband systems cannot be treated as linear media due to fiber nonlinearities. SRS causes interband power transfer, necessitating precise optical power management. The paper highlights the use of **Optical Signal-to-Noise and Interference Ratio (OSNIR)** and generalized SNR to account for amplifier spontaneous emission (ASE) and both intra- and inter-band effects.

### B. Control Plane Data Models for Multiband
The authors discuss extending the Linux Foundation Transport API (TAPI) to support MB:
*   **Core Concepts:** TAPI uses Service Interface Points (SIPs), Network Edge Points (NEPs) for resource availability, and Connection End Points (CEPs) for active configurations.
*   **Fiber Characterization:** OTS/OMS layers are modeled using NEPs/CEPs to capture loss, PMD, and length, often referring to static fiber profiles.
*   **Transceiver Profiles:** To handle modulation formats and FEC, TAPI uses transceiver profiles that specify applicable frequency ranges for different operational modes.
*   **ROADM Capabilities:** Modeling must account for internal connectivity restrictions (non-CDC architectures) and signal penalties on a per-band basis, as WSS technology varies across bands.
*   **Amplification:** Since multi-band amplifiers are often heterogeneous (e.g., separate amps per band), the control plane must abstract these into simplified amplification functions while managing gain and tilt via frequency-range-specific lists.

## 4. Multigranular Nodes and MBoSDM

### A. Single Level (Flat) Networks
In flat SDM networks, switching occurs only at the DWDM level; the spatial layer is terminated at every node. This leads to a "port explosion" problem for WSS-based ROADMs (e.g., 8 fibers with a degree of 9 may require ~70 WSS ports). While this is a straightforward SDN upgrade, it significantly increases path computation complexity and latency.

### B. Multilevel Networks
These networks allow switching at different granularities (WDM, waveband, or fiber/core).
1.  **Single Switching Nodes:** These are organized into technology domains (e.g., one region for WDM switching, another for core switching) managed by hierarchical controllers and orchestrators.
2.  **Hybrid (Multigranular) Nodes:** These nodes can switch at both the DWDM and SDM levels. This requires new control plane extensions to handle:
    *   Virtual Network Topologies (VNTs) across protocol layers.
    *   Spatial characterization (core/mode identifiers).
    *   **Core-continuity constraints**, ensuring a spatial path remains within a single core, similar to spectrum continuity in WDM.

## 5. PoC of a MBoSDM SDN Control Plane

### A. PoC Architecture
The authors implemented a proof-of-concept using four multigranular nodes and multicore fibers (MCF). They extended TAPI with an experimental protocol layer qualifier: `PHOTONIC_MEDIA/SDM_CORE`. This allows the controller to allocate specific cores for optical bypass, reducing the need for WDM switching at intermediate nodes.

### B. Path Computation and Resource Allocation
The algorithm follows a two-step process: first, it attempts to find a path using existing virtual flexigrid links (VNT). If unsuccessful, it instantiates a new "core service" from source to destination to create a new virtual DWDM link. 

### C. MBoSDM Information Models
The system supports specific submatrix operations via SDN agents: setting up/releasing "add core," "express core," and "drop core" connections, as well as configuring Wavelength Cross-Connect (WXC) ports. This is represented in the TAPI model through SDM_CORE NEPs (reporting availability) and CEPs (reporting assigned cores).

## 6. Conclusions
The transition to MBoSDM requires a shift toward modular SDN architectures and refined data models that move from implicit band assumptions to per-band multiplicities. A critical gap exists in the standardization of the SDM data plane; without standard ITU-T layering for core characterization and switching, full control plane interoperability remains elusive. The authors emphasize the necessity of balancing detailed device modeling (for optimal routing) with generic abstractions (for network scalability).
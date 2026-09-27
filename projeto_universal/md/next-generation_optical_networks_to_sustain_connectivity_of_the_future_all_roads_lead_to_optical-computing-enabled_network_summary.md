---
index_terms:
  - optical-computing-enabled network
  - optical bypass
  - spectral efficiency
  - optical XOR encoding
  - optical aggregation
  - RWNCA problem
  - in-network optical computing
---

# Next-generation optical networks to sustain connectivity of the future: All roads lead to optical-computing-enabled network?

## 1. Introduction
Future global connectivity, driven by IoT, Big Data, and AI, is causing an explosive growth in Internet traffic that threatens to exhaust the physical capacity of current C-band fiber-optic infrastructure (the "capacity crunch"). While technological solutions like Multi-band (MB) and Space-Division Multiplexing (SDM) offer order-of-magnitude capacity increases, they often require expensive new hardware. 

Architecturally, optical networks have relied on "optical-bypass" mode for two decades to avoid costly optical-electrical-optical (OEO) conversions. The core principle of optical-bypass is the strict avoidance of signal interference in the time, frequency, or spatial domains. This paper proposes a paradigm shift toward an **optical-computing-enabled network**, where controlled interference between transitional lightpaths is utilized for computing purposes rather than being treated as destructive. This approach aims to improve spectral efficiency and support large-scale AI training directly within the optical layer, necessitating a new framework termed "optical network design and planning 2.0."

## 2. Optical computing-communication integrated network
The end of predictable transistor scaling (Moore's Law) has spurred interest in silicon photonics and light-based computing for AI acceleration due to superior speed and energy efficiency. The authors argue that the transport layer should evolve from a static role (simply moving data) to an integrated communication-computing infrastructure where transmission and processing occur simultaneously at the optical layer.

### 2.1. Optical aggregation/de-aggregation
Traditional channel aggregation is performed electronically, which is not scalable for very high bit rates. **Optical aggregation** leverages nonlinear effects (e.g., four-wave mixing, cross-phase modulation) in mediums like semiconductor optical amplifiers to combine multiple lower-speed channels into a single higher-speed channel with a higher-order modulation format. For example, two QPSK signals can be aggregated into one 16-QAM signal. This results in superior spectral efficiency; whereas an optical-bypass network would require separate wavelengths for these demands on shared links, an optical-computing-enabled network can consolidate them into a single wavelength.

### 2.2. Optical XOR encoding/decoding
Using photonic logic gates, bit-wise exclusive-or (XOR) operations can be performed on high-bit-rate optical signals. This is particularly useful for **dedicated protection schemes**. In an optical-bypass network, backup paths often overlap and require multiple wavelengths to avoid interference. In a computing-enabled network, the backup signals of two demands sharing a destination can be XOR-encoded at an intermediate node into a single computed lightpath. This reduces wavelength consumption on shared links by 50% while maintaining near-immediate recovery speeds via XOR operations during link failure.

### 2.3. Network design and planning: Optical-computing-enabled vs. Optical-bypass framework
The transition to computing-enabled networking adds a new dimension of flexibility: the interaction of lightpaths. In traditional optical-bypass networks, the primary challenge is the Routing and Wavelength Assignment (RWA) problem. In the new paradigm, this evolves into a more complex problem that includes **computing assignment**. Designers must now determine which pairs of lightpaths to compute, identify optimal computing nodes, and route the resulting computed lightpaths. This shift defines "optical network design and planning 2.0."

## 3. A mathematical formulation for optical-computing-enabled network design with optical XOR encoding and decoding
The authors present an Integer Linear Programming (ILP) model to minimize wavelength link utilization in a network utilizing optical XOR encoding. The model assumes that encoding occurs on backup signals of demands sharing a common destination, using the same wavelength, and requires link-disjointedness between working paths and backups to ensure resilience.

The ILP objective is to minimize the total number of wavelengths used across all links. Constraints include:
*   **Flow conservation:** Ensuring working and backup paths are continuous from source to destination.
*   **Wavelength constraints:** Enforcing wavelength uniqueness on each link.
*   **Coding logic:** Limiting each demand to one encoding operation and ensuring a common destination for encoded pairs.
*   **Resilience:** Guaranteeing that if two demands are encoded, their working routes are disjointed from each other and from the corresponding backup routes to permit recovery after any single link failure.

Because this problem is NP-hard and computationally more intensive than traditional RWA (due to variables tracking encoding nodes and computed paths), the authors also propose a scalable heuristic algorithm for larger networks.

## 4. Numerical simulation results
The proposal was tested against traditional optical-bypass networking using NSFNET and COST239 topologies, measuring wavelength link cost as the primary metric.

*   **Small-scale tests:** ILP optimal solutions showed that network coding (NC) provides significant gains over designs without network coding (w-NC). The proposed heuristic performed closely to the ILP model.
*   **Realistic topologies:** NC consistently improved capacity efficiency, achieving up to an 8% gain in NSFNET and a 5% gain in COST239. The authors note that these gains are lower than those seen in electronic OEO coding (which can reach 20%) because all-optical coding is more restricted by wavelength constraints.

### 4.1. A closer look on the difference between the general Routing, Wavelength and Network Coding Assignment Problem versus the traditional Routing and Wavelength Assignment
Using a specific traffic matrix instance, the authors demonstrate that while RWA provides basic routing and wavelength data, the **Routing, Wavelength and Network Coding Assignment (RWNCA)** problem requires an additional layer of optimization. Specifically, RWNCA must optimally determine the encoding pairs, the precise computing nodes (e.g., node 7 or 8 in their example), and the routing for the resulting computed lightpaths. This confirms that RWNCA is computationally one order of magnitude harder than RWA.

## 5. Summary
The paper argues that to sustain future connectivity and AI traffic, optical networks must move beyond the optical-bypass paradigm. By integrating computing capabilities—specifically optical aggregation and XOR operations—directly into the transport layer, operators can significantly increase spectral efficiency and energy savings. The authors have provided a theoretical framework for this "optical-layer intelligence," including an ILP formulation for network coding and numerical evidence of its efficacy over traditional architectures. Future realization will require multidisciplinary efforts to advance devices, systems, and network management algorithms.
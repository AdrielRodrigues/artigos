---
index_terms:
  - 6G x-haul infrastructure
  - Space Division Multiplexing
  - Multi-granular optical node
  - Waveband selective switch
  - Optical digital-analog converter
  - Ultra-wideband transmission
---

# Forthcoming optical x-haul infrastructure supporting 6G mobile network requirements

## 1. Introduction
The transition to 6G (IMT-2030) requires fundamental innovations in transport networks to handle ultra-high rates and low latency. The "x-haul" network comprises the fronthaul (FH, RU to DU), midhaul (MH, DU to CU), and backhaul (BH, CU to core network). 6G's disaggregated Radio Access Network (RAN) utilizes various functional splits (FS) that impose distinct capacity and latency demands on these segments.

The proposed infrastructure addresses these needs through three primary innovations:
1. **Fronthaul/Midhaul:** A PIC-based optical filter for dynamic resource allocation and high-speed switching.
2. **Backhaul:** A Multi-Granular Optical Node (MG-ON) utilizing a Photonic Integrated Circuit (PIC)-based Waveband Selective Switch (WBSS) to support Ultra-Wideband (UWB) and Space Division Multiplexing (SDM).
3. **Transceivers:** Energy-efficient optical digital-to-analog converter (oDAC) transceivers that reduce reliance on power-intensive electronics.

The entire physical infrastructure is designed for software-defined programmability via a Service Management and Orchestration (SMO) framework, enabling network automation and end-to-end slicing.

## 2. Optical Switching Architectures for the x-haul

### A. Novel Nyquist-Shaped Node Element for Supporting Flexible Fronthaul Networking
To overcome the capacity limits and access delays of traditional Time Division Multiplexing (TDM) in Passive Optical Networks (PONs), the authors propose a Spatially Diverse Point-to-Multi-Point (SD-PtMP) architecture based on subcarrier multiplexing. 

The core innovation is the **circular interlacer**, a PIC-based element consisting of two stages of cascaded half-band Nyquist-shaped interleaver filters in a butterfly pattern. It shuffles subcarriers from four input sources into four unique output signals, allowing cell sites to associate flexibly with different central offices (COs). While some subcarriers are lost at transition bands (75% utilization), the architecture provides a net 3$\times$ capacity gain and offers lower loss and smaller footprints than cyclic AWGR routers. Evaluation using the TEFNET24 topology shows that requirements vary significantly based on ring size and transceiver density, necessitating adaptive energy strategies.

### B. MG-ON Architecture and Operation
The proposed Multi-Granular Optical Node (MG-ON) is designed for backhaul scaling using UWB and SDM, moving beyond traditional Wavelength Selective Switches (WSS). The architecture uses a three-layer hierarchy:

*   **Layer 1 (Flex-Band Route and Select):** Operates at the fiber/band level using flex-WBSS modules. It enables Full Fiber Switching (FFS) by bypassing delay stages and supports Spatial Lane Changes (SLC) to relocate bands between spatial rails during link failures.
*   **Layer 2 (Flex-Band Add/Drop):** Uses an inter-band Optical Cross Connect (OXC) to provide colorless, directionless, and contentionless (C/D/C) access to wideband transceivers based on integrated comb sources.
*   **Layer 3 (Legacy Wavelengths Access for Routing and Add/Drop):** Maintains compatibility with legacy C-band equipment via conventional WSS and intra-band OXCs; these components can be decommissioned as the network evolves toward full band switching.

#### 1. WBSS Architecture
The Waveband Selective Switch (WBSS) combines an adaptive filtering stage (cascaded FIR lattice filters) with a non-blocking spatial crossbar switch (CS). This allows carving the UWB spectrum into up to four flexible bands. To optimize performance, the authors use "inverted logic" where most Mach–Zehnder Interferometer (MZI) switches are set to the bar state rather than the cross state, as the bar state exhibits superior crosstalk performance across wide spectral ranges.

#### 2. WBSS Modeling
Insertion loss (IL) is modeled as the sum of FIR filter losses (0.1 dB/tap) and crossbar junction losses (0.05 dB/junction). Despite the addition of waveguide crossings to reduce crosstalk, the overall IL remains manageable for UWB operation.

### C. MG-ON Scaling Studies and Capacity Evaluation

#### 1. Analytical Formalism
Capacity is modeled based on node degree ($D$), spatial lanes ($S$), spectral efficiency (SE = 10 b/s/Hz), and a UWB spectrum of $\sim$21 THz. Formalisms are provided to calculate the required number of WBSS modules, port counts for inter- and intra-band OXCs, and the number of band transceivers.

#### 2. Scalability Performance Assumptions
The study assumes linear scaling of WBSS ports with spatial lanes and a routing strategy where two bands remain in Layer 1 (route/select) while two are transferred to Layers 2 or 3 (add/drop). Full Fiber Switching is assumed to be enabled when FIR filters operate in pass-through mode.

#### 3. MG-ON Scalability Results
Simulation results demonstrate that throughput scales with node degree and spatial dimension:
*   **Small-scale ($D=4$):** $\sim$3.76 Pb/s.
*   **Medium-scale ($D=5, S=8$):** $\sim$9.4 Pb/s via FFS.
*   **Large-scale ($D=6, S \ge 8$):** Exceeds 10 Pb/s.
Layer 1 provides the most significant capacity gain, validating the transition from waveband to full fiber switching.

### D. MG-ON Cascadability Studies
The study evaluates physical layer impairments (ASE noise, NLI, and SRS) using the Optical Signal-to-Noise plus Interference Ratio (OSNIR). To mitigate SRS-induced power tilt, pre-compensating filters are used at node ingress. 

Testing against a national network topology ($\sim$1000 km/7 hops) shows:
*   **State Performance:** The bar state provides $\sim$0.8 dB higher OSNIR than the cross state.
*   **Modulation Viability:** PM-QPSK is reliable across the entire national scale. Higher-order formats like PM-16QAM are viable for adjacent nodes or in specific bands (C and L) under 2z-OSNIR power allocation strategies.

## 3. Innovative oDAC-Based Transceivers for the x-haul
To replace energy-intensive electronic DACs and DSP engines, the authors propose Optical Digital-to-Analog Converters (oDAC). These use parallel Mach–Zehnder Modulators (MZMs) to directly synthesize high-order multi-level optical signals from low-resolution drivers.

Key technical advantages include:
*   **Noise Squelching:** Utilizing the non-linearity of the MZM transfer function suppresses electronic driver noise, resulting in a 6.6 dB Error Vector Magnitude (EVM) improvement over conventional modulators.
*   **Scalability:** A hybrid serial-parallel oDAC architecture can generate up to 256QAM constellations using only eight NRZ drivers, achieving rates of 3.2 Tbps per wavelength.
*   **Efficiency:** These transceivers reduce power consumption per bit by 30%–40% compared to traditional eDAC solutions.

## 4. Summary and Concluding Remarks
The proposed x-haul infrastructure provides a comprehensive hardware solution for 6G requirements. Key outcomes include a backhaul MG-ON capable of $>$10 Pb/s throughput, a fronthaul SD-PtMP architecture with 3$\times$ capacity improvement via the circular interlacer, and energy-efficient oDAC transceivers exceeding 1 Tb/s per channel. Cascadability analysis confirms that these technologies can support national-scale distances ($\sim$1000 km) using PM-QPSK. Future work will focus on real-world trials and AI-driven orchestration for network automation.
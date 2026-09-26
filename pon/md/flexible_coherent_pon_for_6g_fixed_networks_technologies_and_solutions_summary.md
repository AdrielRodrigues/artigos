---
index_terms:
  - Flexible Coherent PON
  - F6G Fixed Networks
  - P2MP Optical Aggregation
  - Probabilistic Constellation Shaping
  - Burst-Mode DSP
  - FDMA/TDMA Integration
---

# Flexible Coherent PON for 6G Fixed Networks: Technologies and Solutions

## Abstract
The future sixth-generation fixed (F6G) network requires drastic improvements in capacity, connectivity, and latency. To meet these goals, flexible coherent passive optical networks (PON) are proposed, leveraging coherent optics, flexible multiple access, and flexible-rate technologies. A key application is coherent point-to-multipoint (P2MP) optical aggregation, which can replace traditional point-to-point electrical aggregation to reduce costs and latency. This architecture enables joint frequency-division multiple access (FDMA) and time-division multiple access (TDMA), combined with flexible-rate technology and specialized burst-mode digital signal processing (DSP) for efficient upstream transmission.

## Introduction
Fixed networks are evolving from F5G (focused on fiber-to-the-everything) toward F6G, which aims for a tenfold increase in capacity, connectivity, and latency performance. Current direct-detection (DD) PONs are limited by receiver sensitivity and spectral efficiency, making it difficult to achieve these targets. Flexible coherent PONs provide a solution due to their superior sensitivity and spectral efficiency. However, practical implementation requires solving challenges regarding the balance of network metrics and the development of burst-mode DSP for multiple access scenarios.

## Key Technologies for Flexible Coherent PON
The authors trace the evolution of ITU-T PON standards from ATM-PON (622Mb/s) to 50G-PON. They predict that "Beyond 50G-PON" will target data rates of 200Gb/s. While DD optics are currently used, they struggle with optical power budgets ($\ge$ 32dB) and high latency in TDMA. Coherent optics technology is presented as the superior path because it allows for higher spectral efficiency (via polarization multiplexing and I/Q modulation) and enables flexible multiple access and rate adjustments.

### Coherent Optics Technology
While 800Gb/s and 1.6Tb/s coherent technologies exist for point-to-point networks, their application in PONs is hindered by high costs and power consumption at the Optical Network Unit (ONU). To make coherent PONs commercially viable, development must focus on low-cost transceivers and DSP architectures with fast convergence and low complexity.

### Flexible Multiple Access
Traditional TDMA increases throughput via statistical multiplexing but introduces high latency and requires expensive burst-mode devices. While FDMA and CDMA are common in wireless networks, they were avoided in DD PONs because unstable laser wavelengths caused "beat signals" that degraded performance. Coherent optics eliminate this beat signal problem, allowing the integration of FDMA, CDMA, and TDMA to optimize connectivity and latency. FDMA specifically allows for lower-bandwidth devices at the ONU, reducing cost.

### Flexible-Rate Technology
Link losses vary significantly between different ONUs due to fiber length and splitter counts. Current fixed-rate systems are limited by the worst-case ONU, wasting potential capacity. Flexible-rate technology adjusts data rates based on individual link budgets:
*   **ONU Grouping:** To manage complexity, ONUs are grouped by similar link losses, allowing for discrete rather than continuous rate adjustments.
*   **PCS Modulation:** Probabilistic Constellation Shaping (PCS) is used to adjust spectral efficiency. In peak-power constrained (PPC) PONs without amplifiers, inverse PCS-PAM is preferred for single-carrier signals, while common PCS-QAM is used for multi-carrier entropy-loading systems.
*   **Flexible FEC Technology:** By using shortening and puncturing operations on a single code word, the system can continuously adjust the payload and overhead of Forward Error Correction (FEC), trading off optical power budget for net data rate.

## Coherent P2MP Optical Aggregation
Coherent P2MP optical aggregation is proposed as an alternative to P2P electrical aggregation. In electrical aggregation, routers converge multiple low-speed flows into one high-speed flow; in coherent P2MP, a passive optical splitter converges these flows optically.

**Advantages:**
*   **Cost/Complexity:** Reduces the total number of transceivers by 50%, lowering CAPEX and OPEX.
*   **Performance:** Eliminates router processing, reducing latency.
*   **Scalability:** Capacity can be upgraded flexibly by adding digital subcarriers rather than replacing all hardware simultaneously.

**Challenges:**
*   **Flexibility:** Passive splitters lack the programmability, authentication features, and reliability monitoring of routers.
*   **Signal Quality:** Direct optical transmission suffers from higher link loss compared to regenerated electrical signals, potentially requiring optical amplifiers.
*   **Capacity Limits:** Current FDMA-based aggregation is limited by laser phase noise when using many low-bandwidth subcarriers.

## Joint FDMA and TDMA for Flexible Multiple Access
To balance connectivity and latency, the authors propose a hybrid architecture based on entropy-loading digital subcarrier multiplexing (DSCM).
*   **Downlink:** The central office (CO) broadcasts DSCM signals. ONUs use local oscillators shifted to their specific subcarrier frequency, allowing them to ignore other traffic and use lower-bandwidth transceivers.
*   **Uplink:** ONUs are allocated specific subcarriers and time slots. They generate an optical subcarrier matching the subcarrier width, which is then aggregated at the CO via a passive splitter. 
*   **Rate Optimization:** Flexible-rate technology assigns spectral efficiencies based on link loss to maximize total network capacity.

## Burst-Mode DSP for Coherent TDMA
Standard continuous-mode DSP uses blind algorithms with feedback loops that converge too slowly for short upstream bursts, reducing payload efficiency. A burst-mode DSP is proposed using feed-forward estimation and a specialized preamble:
*   **Preamble Design:** 
    *   **Preamble A:** Uses frequency tones (at half and quarter baud rates) for X and Y polarizations to enable frame detection, frequency offset estimation (FOE), state-of-polarization (SOP) estimation, and sampling phase offset (SPO) initialization.
    *   **Preamble B:** Employs constant-amplitude-zero-autocorrelation (CAZAC) sequences with specific multiplication coefficients to facilitate frame synchronization and tap coefficient estimation.
*   **Timing Recovery:** Feed-forward SPO estimation based on Preamble A eliminates the long convergence time typically associated with feedback loops.
*   **MIMO Equalizer:** Tap coefficients are estimated using either Minimum Mean Square Error (MMSE) or Zero-Forcing (ZF) algorithms based on Preamble B. MMSE offers better performance, while ZF provides lower computational complexity. Proper initialization via the preamble ensures that the subsequent feedback loop has no convergence time.

## Conclusion
Flexible coherent PONs are essential for achieving F6G goals. By replacing electrical aggregation with coherent P2MP optical aggregation and implementing joint FDMA/TDMA with flexible-rate technology, networks can optimize capacity and latency while reducing costs. The proposed burst-mode DSP further enables these systems by ensuring rapid convergence for upstream TDMA signals.
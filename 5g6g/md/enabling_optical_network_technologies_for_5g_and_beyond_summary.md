---
index_terms:
  - 5G x-haul
  - hybrid digital-analog RoF
  - probabilistic constellation shaping
  - 50G-PON
  - OSUflex
  - F5G
  - network slicing
  - long-haul optical transmission
---

# Enabling Optical Network Technologies for 5G and Beyond

## I. Introduction
The deployment of 5G and future 6G networks necessitates a robust optical infrastructure to connect remote units (RUs), distributed units (DUs), central units (CUs), and the core network (5GC). These networks must support three primary application scenarios: enhanced mobile broadband (eMBB) for high-bandwidth data, ultra-reliable low-latency communications (uRLLC) for mission-critical tasks, and massive machine type communications (mMTC) for IoT. To meet these needs, optical networks must provide higher bandwidth to accommodate massive MIMO and increased spectrum, lower latency and precise synchronization for C-RAN/CoMP, and fine-grained network slicing for optimized quality of service (QoS).

## II. Optical Technologies for 5G X-Haul

### A. Overview of 5G X-Haul
X-haul comprises front-haul (RU to DU), mid-haul (DU to CU), and back-haul (CU to 5GC) segments. Latency requirements vary significantly across these segments, from 100 $\mu$s for CPRI/eCPRI to 10 s for mMTC. Typical distances are limited to <10 km for front-haul, <40 km for mid-haul, and <80 km for back-haul, with data center interconnections (DCI) typically under 120 km. The varying distance and capacity requirements across these segments dictate the use of different modulation, detection, and multiplexing technologies.

### B. C-Band WDM Based Front-Haul
A "semi-active" wavelength-division multiplexing (WDM) system using WDM-PON is proposed for front-haul. It utilizes 20 wavelength pairs for bidirectional (BiDi) transmission, where active equipment is required at DU/CU sites but not at RU sites. The architecture employs cyclic arrayed waveguide gratings (AWG) with a 2.6 THz free spectral range to multiplex downstream and demultiplex upstream channels, providing high reliability through type-B protection.

### C. O-Band WDM Based Front-Haul
To support aggregated capacities of 300 Gb/s per fiber (twelve 25-Gb/s channels), two O-band schemes are discussed:
*   **L-WDM:** Extends LAN-WDM from eight to twelve channels. It uses cyclic AWGs and optical circulators for BiDi transmission, maintaining a dispersion penalty of <1 dB over 10 km of standard single-mode fiber (SSMF).
*   **M-WDM:** Doubles the number of CWDM channels by shifting existing channels by $\pm$3.5 nm. This scheme faces higher dispersion penalties than L-WDM, requiring mitigation strategies for 25-Gb/s NRZ signals.

### D. CPRI-Compatible DA-RoF
Traditional analog radio-over-fiber (A-RoF) is limited by SNR and error-vector magnitude (EVM), making it difficult to support high-order modulations like OFDM-1024QAM. To solve this, Hybrid Digital-Analog RoF (DA-RoF) is introduced.
*   **Method:** DA-RoF uses cascaded probabilistic constellation shaping (PCS)-n-QAM for digital approximation of the waveform and pulse code modulation (PCM) to represent approximation errors.
*   **Results:** This technique trades spectral efficiency (reducing it by 50% compared to A-RoF) for a significant SNR gain (>10 dB), reducing EVM to levels capable of supporting 1024-QAM. 
*   **Scalability:** By integrating 400G-ZR coherent transceivers, DA-RoF can scale to multi-Tb/s CPRI-equivalent bit rates per wavelength for future 6G requirements.

## III. Shannon-Limit-Approaching Long-Haul Transmission

### A. Capacity-approaching FEC
Forward Error Correction (FEC) is critical for reaching the Shannon limit in long-haul transmission. High-performance codes such as CFEC, CFEC+, and OFEC, alongside low-density parity check (LDPC) codes with 20-25% overhead, have been demonstrated. Soft-decision (SD) decoding implementations of these codes are now within 1.4 dB of the SD Shannon limit for 16-QAM signals.

### B. Probabilistic Constellation Shaping (PCS)
To further close the gap to Shannon capacity, PCS is used to optimize signal constellations. 
*   **Probabilistic Amplitude Shaping (PAS):** This method combines a distribution matcher with systematic binary FEC encoding. PAS offers simple DSP implementation and compatibility with existing QAM modulations and FEC codes.
*   **Findings:** Field trials show that activating PCS can double transmission reach; for example, extending the error-free reach of 16-QAM from 1500 km to 2000 km, providing an effective OSNR gain of approximately 2 dB.

### C. Super C and L Bands
Increasing fiber capacity requires wider amplification bandwidths. The use of super C+L erbium-doped fiber amplifiers (EDFAs) provides a 6 THz window in the super-C band and a 5 THz window in the super-L band. This expansion allows for up to 88 Tb/s single-fiber transmission capacity using 800-Gb/s channels on a 100-GHz grid.

### D. State-of-the-Art Optical Transmission Systems
Modern long-haul systems integrate digital coherent detection, subcarrier multiplexing, and nonlinearity mitigation. Current commercial capabilities include per-fiber capacities of 88 Tb/s for DCI and over 26 Tb/s for transatlantic links, with reaches extending up to 15,000 km via flexible modulation and coding.

## IV. Low-Latency 50G-PON
As part of the ITU-T higher speed PON (HSP) project, 50G-PON is developed to replace or augment XG(S)-PON while utilizing existing optical distribution networks (ODNs). To overcome the increased sensitivity and dispersion penalties associated with 50 Gb/s signals, it employs DSP-based channel equalization, LDPC codes, low-chirp transmitters, and semiconductor optical amplifiers.

To support strict 5G x-haul latency requirements, three mechanisms are introduced:
1.  **Cooperative Dynamic Bandwidth Allocation (CoDBA):** Shares RAN scheduling with PON scheduling to eliminate negotiation latency between ONU and OLT.
2.  **Accelerated DBA Scheduling:** Allows multiple bursts per ONU per 125-$\mu$s frame, reducing maximum waiting time from 125 $\mu$s to approximately 16 $\mu$s.
3.  **Dedicated Activation Wavelength (DAW):** Uses a separate wavelength for discovery and ranging, eliminating the ranging window to ensure uninterrupted low-latency communication.

## V. Service-Oriented OTN
Traditional Optical Transport Networks (OTN) are limited by the ODU0 minimum size ($\sim$1.24 Gb/s), which is inefficient for smaller services. 
*   **OSUflex:** A flexible Optical Service Unit (OSU) container allows bandwidth granularity of $\sim$2 Mb/s, enabling a single 100-Gb/s wavelength to support over 1000 client services.
*   **Performance:** OSU-based OTN utilizes sequential forwarding to reduce switching latency; demonstrations show an end-to-end latency reduction from 4398 $\mu$s to 1289 $\mu$s ($\sim$70% improvement).
*   **Network Slicing:** OSUflex enables "hard" network slicing with guaranteed bandwidth and deterministic latency, reducing resource fragmentation for services under 500 Mb/s.

## VI. The Vision of Fiber-to-Everywhere (F5G)
The Fifth Generation Fixed Network (F5G) aims to extend fiber connectivity beyond the home to every device and machine. F5G evolves from three initial scenarios—enhanced fixed broadband (eFBB), guaranteed reliable experience (GRE), and full fiber connection (FFC)—into a hexagonal model including:
*   **Energy-Efficient Broadband Communication (EEBC):** Utilizing passive optical LANs for campuses and enterprises.
*   **Real-Time Broadband Communication (RTBC):** Applying latency-constrained networks and hollow-core fibers for industrial AI and robot control.
*   **Harmonized Communication and Sensing (HCS):** Using the fiber infrastructure itself as a sensor. Examples include detecting earthquakes/tsunamis via polarization changes in submarine cables and utilizing Distributed Acoustic Sensing (DAS) or phase variations for vibration localization.

## VII. Conclusion
The transition to 5G and beyond requires a synchronized evolution of optical technologies across x-haul, long-haul core networks, access PONs, and transport networks. By integrating WDM, DA-RoF, PCS, 50G-PON, and OSU-based OTN, the network can provide the necessary throughput, latency, and slicing capabilities. The F5G vision complements mobile networks by providing a ubiquitous fiber foundation that supports both high-speed communication and environmental sensing.
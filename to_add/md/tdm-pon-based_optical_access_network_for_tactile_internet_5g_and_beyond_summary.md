---
index_terms:
  - TDM-PON
  - Optical Access Network
  - Tactile Internet
  - Dynamic Bandwidth Allocation
  - Channel Bonding
  - Network Slicing
  - 5G/6G Fronthaul
---

# TDM-PON-Based Optical Access Network for Tactile Internet, 5G, and Beyond

## Abstract
The paper explores the role of Time-Division Multiplexing Passive Optical Networks (TDM-PON) in supporting high-bandwidth and low-latency services required by 5G, 6G, and the Tactile Internet (e.g., AR/VR, machine-to-machine interaction). It details a feasibility demonstration of a Tactile Internet testbed and identifies critical technical challenges regarding capacity, latency reduction, and network virtualization.

## Introduction
Optical access networks are evolving to support explosive data growth driven by 5G and beyond. As mobile carrier frequencies increase, cell sizes shrink, necessitating deeper fiber penetration and higher speeds (exceeding 25 Gb/s per wavelength). A primary driver is the "Tactile Internet," which requires control-based communications with response times of approximately 1 ms to match human tactile perception, unlike conventional content-oriented networks. Different services exhibit varied needs: IoT devices require low data rates and can tolerate higher latency ($\sim 100$ ms), whereas autonomous vehicles and AR require $\sim 1$ Gb/s capacity and sub-1 ms latency. The authors propose using packet-level channel bonding and cyclic dynamic bandwidth allocation (DBA) to achieve 50 Gb/s+ capacity and <1 ms latency.

## High-Capacity and Low-Latency PON

### Constraints of the Optical Access Network
Unlike core networks that prioritize cost per bit, access networks must maximize capacity while maintaining low cost per user. Implementation is constrained by the "outside plant" dogma: electrical power, optical amplifiers, and dispersion compensating fibers are generally prohibited in the passive optical distributed network (ODN). To address these constraints, researchers are moving toward using the O-band for both upstream and downstream transmission to mitigate chromatic dispersion and utilizing Avalanche Photo Diode (APD) receivers to improve power budgets. Additionally, enhanced DBA schemes are necessary because conventional TDM-PON fairness-based scheduling cannot meet the strict latency requirements of Tactile Internet applications.

### TDM-PON Prototype Based on 25 Gb/s Per Wavelength
The authors implemented a prototype based on IEEE 50G-EPON using an FPGA-based Optical Line Terminal (OLT) and 25G bidirectional optical sub-assembly (BOSA) modules. Key technical features include:
- **Channel Bonding:** Implemented in the multipoint reconciliation sublayer (MPRS), this allows an Optical Network Unit (ONU) to use multiple wavelengths to increase capacity (e.g., two wavelengths for a 50G ONU). It utilizes envelope alignment buffers and markers (EPAM) for frame synchronization. This increased upstream throughput from 8.3 Gb/s to 16.7 Gb/s in tests.
- **Low-Latency DBA:** A differential Quality of Service (QoS) approach divides uplink capacity into four tiers: Gold, Silver, Bronze, and Best Effort. The "Gold" class uses a static cycle-based method to guarantee latency (served every 250 $\mu$s), ensuring that time-critical tactile services are prioritized.
- **Experimental Results:** Tests showed downstream sensitivity of –24 dBm at $10^{-3}$ BER and stable performance over 50 hours. Gold class traffic maintained latency below 0.4 ms regardless of load, while lower tiers exceeded 10 ms under high load. The system successfully supported commercial IPTV and file transfers (reaching $\sim 8$ Gb/s, limited by the IP network interface).

### Tactile Internet Testbed
A feasibility testbed was constructed connecting an access network in Daejeon to a core network (KOREN) over 278 km. The core network utilized ROADMs and 100 Gb/s DP-QPSK coherent transceivers. 
- **Application:** An inverted pendulum was used to simulate a remotely controlled robot. To maintain balance, the system required millisecond-order control loops between the controller (Seoul) and the pendulum (Daejeon).
- **Traffic Load:** The system simultaneously transmitted uncompressed 4K UHD video at 6 Gb/s to emulate robotic vision.
- **Findings:** Total latency was dominated by fiber propagation delay ($\sim 1.3$ ms for long-haul, $\sim 0.3$ ms for access). With the high-capacity TDM-PON prototype, the pendulum remained balanced and video quality was clear. When latency or capacity were intentionally degraded, the pendulum lost balance and video froze, validating the necessity of high-speed, low-latency PONs for tactile applications.

## Optical Access for Future Networks

### High Capacity
Future ports will target 100 Gb/s and beyond. The main challenge is maintaining the power budget despite poor receiver sensitivity and chromatic dispersion at high speeds. Potential physical layer (PHY) solutions include:
- **Coherent Detection:** Using DP-QPSK or DP-QAM for superior sensitivity and dispersion compensation, though cost remains a barrier for ONU deployment.
- **Direct Detection:** Utilizing NRZ-OOK, PAM, or DQPSK combined with DSP; these are simpler and more cost-effective but struggle with dispersion and baud rate limits.
- **Channel Bonding:** Supplementing modulation improvements by aggregating multiple wavelengths to exceed 100 Gb/s.

### Low Latency
While current advanced DBA is sufficient for midhaul/backhaul, fronthaul applications require further reductions. The authors propose **Cooperative DBA (Co-DBA)**, where the OLT and mobile equipment exchange traffic patterns via a Cooperative Transport Interface (CTI). This allows the OLT to proactively allocate bandwidth based on actual mobile traffic demands rather than reacting to ONU requests. This requires high-precision time synchronization (e.g., IEEE-1588 or SyncE) accurate to several microseconds.

### Virtualization and Slicing
To accommodate diverse services in one ODN, the network must move toward virtualization and optical disaggregation. By separating the OLT into a physical part (ports/cards) and a logical part (DBA types/bandwidth profiles), the network can be "sliced." This enables the allocation of exclusive logical resources to specific applications on demand, providing flexibility that fixed-hardware TDM-PONs currently lack.

## Summary
The paper demonstrates that high-capacity (via channel bonding) and low-latency (via advanced DBA) TDM-PON prototypes can successfully support Tactile Internet and 5G services, including remote robotics and uncompressed 4K video. Future development must focus on selecting cost-effective modulation formats for 100 Gb/s+ speeds, implementing Co-DBA for ultra-low latency fronthaul, and adopting network slicing via OLT virtualization.
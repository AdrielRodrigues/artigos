---
index_terms:
  - 6G mobile networks
  - optical access networks
  - fixed-mobile convergence
  - mobile x-haul
  - all-photonic networks
  - Open RAN
  - network sustainability
  - AI-native architecture
---

# Optical access networks to support future 5G and 6G mobile networks [Invited]

## 1. Introduction—6G in a Nutshell
The sixth generation (6G) of mobile networks focuses on sustainability, inclusivity, and ubiquitous intelligence. It evolves existing 5G scenarios—enhanced mobile broadband (eMBB), massive machine-type communication (mMTC), and ultra-reliable low-latency communication (URLLC)—into immersive communication, massive communication, and hyper-reliable low-latency communication (HRLLC). Additionally, it introduces new domains: ubiquitous connectivity, AI-integrated communication, and integrated sensing and communication.

**6G Capabilities and Use Cases**
According to the ITU-R IMT-2030 framework, 6G targets ambitious performance benchmarks: peak data rates up to 1 Tbps, user experienced rates of 1–10 Gbps, latency between 0.1–1 ms, reliability up to 99.99999%, and positioning accuracy of 1–10 cm. These capabilities enable advanced use cases such as holographic communications, ultra-precise digital twins, and AI-driven services in healthcare and smart cities.

**Operator Perspectives (Orange)**
From an operator's viewpoint, the transition to 6G must be evolutionary rather than revolutionary to avoid massive hardware overhauls. While mobile traffic growth is slowing globally due to market saturation and better compression, there remains a need for incremental capacity and performance gains. Key 6G KPIs include a significant increase in area capacity (up to 3 Tb/s/km² in dense urban areas) and a tenfold increase in energy efficiency compared to 5G.

**Technological Enablers**
*   **Spectrum:** Use of the "upper mid-band" (FR3: 7.125–24.25 GHz), alongside 6 GHz and 7–15 GHz ranges, to increase data rate capacity.
*   **Radio Access:** Implementation of higher-order MIMO and narrow beamforming, Sub-THz bands for sensing/obstacle penetration, and the integration of satellite communications.
*   **Architecture:** Shift toward cloud-native and AI-native architectures (Level 4 automation) and "softwarization" through Open RAN to improve security and interoperability.

**Sustainability Goals**
The ICT sector's carbon footprint is a major concern. Orange aims for net-zero emissions by 2040, noting that the majority of its emissions are Scope 3 (indirect). Consequently, 6G design must prioritize power-efficient technologies and circular economy principles to ensure that performance gains do not jeopardize environmental targets.

## 2. Fixed Access Technologies for 5G and 6G Mobile X-Haul Networks
Fiber is the primary medium for mobile x-haul (fronthaul, mid-haul, backhaul). 6G demands ultra-high transmission capacity (Tbps range), deterministic low latency, and minimal jitter.

**Point-to-Point (PtP) Connectivity**
PtP remains the preferred choice for Fiber-to-the-Antenna (FTTA) and Fiber-to-the-Office (FTTO) because it provides full bandwidth and minimizes signal processing latency. Current evolution targets 100 Gbit/s bidirectional transmission over 40 km, with a long-term trajectory toward 800 Gbit/s interfaces derived from data center technologies.

**Wavelength Division Multiplexing (WDM)**
WDM is considered where fiber availability is limited. To mitigate chromatic dispersion at rates of 50 or 100 Gbit/s, transmission in the O-band is preferred over the C-band. PAM4 modulation is identified as a likely initial implementation for these higher bitrates.

**Passive Optical Networks (PON)**
While TDM/TDMA PONs are ideal for high-density residential (FTTH) or small business (FTTE) connections, they are less suited for mobile fronthaul due to packet delay variation and latency issues associated with Dynamic Bandwidth Allocation (DBA). However, Very High-Speed PON (VHSP) supporting 200G may serve private campus networks.

**Future Fixed Network Generations (F5G and F6G)**
*   **F5G Advanced:** Aims for $\ge$10 G fiber-to-the-room, sub-1 ms latency, and autonomous networking to support 6G.
*   **F6G/IOWN:** Envisions All-Photonic Networks (APNs) transitioning connectivity from site-to-site to memory-to-memory, with bandwidth exceeding 10 Tbit/s per endpoint. To further reduce latency, an "extended CTI" (Cooperative Transport Interface) is proposed to allow APN controllers to receive data directly from the CU/DU.

**Fixed Network Sustainability**
Sustainability in x-haul can be improved by increasing PON split ratios, utilizing highly dynamic sleep modes for network terminations, and implementing coordinated intelligent controllers.

## 3. Toward Flexible and Autonomous Networks for Fixed Mobile Convergence
The convergence of fixed and mobile networks requires a shift toward autonomous architectures managed by AI and software-defined networking (SDN).

**AI and Network Autonomy**
AI is envisioned as both an enhancer of communication and a beneficiary of it. In the physical and transport layers, AI will be used for dynamic resource allocation, anomaly detection, and predictive maintenance based on sensing data (e.g., fiber strain, traffic loads, and user mobility).

**O-RAN and Network Slicing**
Open RAN (O-RAN) and Cloud RAN enable network slicing, allowing a single physical infrastructure to be partitioned into virtual segments tailored to specific requirements (bandwidth, latency, security) for residential, business, or mobile services. This is complemented by the convergence of OLT management with Radio Intelligent Controllers (RIC).

**Architectural Shifts and Innovations**
*   **Edge Integration:** To reduce carbon footprints and improve performance, computing functions (MEC, Edge AI) must move closer to the user rather than staying in central offices.
*   **Photonic Switching:** The Octopus project explores multi-Tbit/s photonic switching with SDN controllers to support time-sensitive networking. Optical bypasses of the OLT are also proposed for power savings and lower latency.
*   **Hollow-Core Fiber:** New hollow-core fibers can reduce latency from 5 $\mu$s/km (standard fiber) to 3.5 $\mu$s/km, though manufacturing hurdles remain before large-scale deployment.

## 4. Conclusion
The convergence of fixed and mobile access networks in the 6G era will be driven by synergy between OLTs, AI-driven optimization, and end-to-end network slicing. The OLT is positioned as a critical aggregation point for both traffic types, potentially evolving into all-optical architectures to support immersive experiences and URLLCs. Success depends on overcoming challenges in standardization, interoperability, and security through industry-wide collaboration.
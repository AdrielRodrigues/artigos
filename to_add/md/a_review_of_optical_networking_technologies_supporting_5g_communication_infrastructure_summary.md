---
index_terms:
  - 5G communication infrastructure
  - optical networking technologies
  - smart city architecture
  - passive optical networks
  - elastic optical networks
  - network flexibility
---

# A review of optical networking technologies supporting 5G communication infrastructure

## Abstract
The paper examines the necessary integration of 5G wireless and optical technologies to realize the "smart city" concept. Because smart cities require massive data transmission for services like traffic management and electrical grids, a reliable communication infrastructure is essential. The authors provide an overview of advanced optical networking developments intended to support 5G transport networks and the connection of vast numbers of devices in future urban environments.

## 1 Introduction
Urbanization and the rise of high-bandwidth streaming video have significantly increased global data traffic. While optical fibers are ideal for smart cities due to their bandwidth, low attenuation, and immunity to electromagnetic interference, current fixed spectrum allocation technologies are insufficient for 5G's rigid demands. The authors argue that a migration toward flexible networking concepts is necessary. The paper specifically addresses four research questions (RQs): the requirements of 5G wireless on optical networks; available/emerging supporting technologies; the benefits of flexibility in the optical domain; and current research challenges regarding network flexibility implementation.

## 2 Smart city layered architecture: an overview
The authors distinguish between a city's physical architecture and its communication architecture. The proposed communication architecture consists of four functional layers:
*   **Device/Sensing Layer:** Composed of sensors, cameras, and actuators. While bandwidth needs are low, this layer requires low latency and long battery life; optical sensors may be used here.
*   **Communication Layer:** Consists of transport and access networks providing enhanced mobile broadband (eMBB), massive machine-type communications (mMTC), and ultra-reliable low-latency communication (URLLC). This is achieved through a combination of Dense Wavelength Division Multiplexing (DWDM) for long distances and Passive Optical Networks (PON) or point-to-point (P2P) links for the "last mile" fronthaul/backhaul.
*   **Data Layer:** Handles data organization, filtering, storage, and decision-making via various processing techniques.
*   **Application Layer:** The interface with citizens, encompassing services like smart healthcare, energy, and governance.

## 3 Data synthesis

### 3.1 What are the requirements of 5G wireless on optical networking?
To support IoT and smart infrastructure, optical networks must meet several stringent criteria:
*   **Bandwidth and Capacity:** End-user data rates must reach up to 10 Gb/s (10–100x higher than 4G) to accommodate a device density 100 times greater than previous generations.
*   **Latency:** Time-critical applications (e.g., healthcare, traffic safety) require end-to-end delays of a few milliseconds, with some needing less than 1 ms.
*   **Energy Efficiency:** Due to cell densification, the network must minimize power consumption through low-cost equipment and efficient transmission to extend device battery life.
*   **Spectral Efficiency:** Optical networks must achieve at least three times the spectral efficiency of 4G to manage huge traffic volumes within available spectrum ranges.

### 3.2 What are the available and emerging optical technologies supporting 5G wireless?
The shift toward Cloud-RAN (C-RAN)—where baseband units (BBUs) are centralized—necessitates advanced optical fronthaul/backhaul. While P2P technology is limited by distance and resource intensity, PON is highlighted as a superior alternative for smart cities due to its point-to-multipoint architecture, which reduces fiber usage through high split ratios (up to 1:256). Emerging standards include XGS-PON and NG-PON2.

#### 3.2.1 TDM-PON
Time Division Multiplexing PON shares the same wavelength among users via assigned time slots. While cost-effective, it suffers from security vulnerabilities and latency issues caused by Dynamic Bandwidth Allocation (DBA) processing times. Research focuses on reducing DBA cycle lengths to improve efficiency.

#### 3.2.2 WDM-PON
Wavelength Division Multiplexing PON assigns a dedicated wavelength per Optical Network Unit (ONU), providing higher capacity and lower power insertion loss, making it ideal for 5G fronthaul. To support densification (requiring $\geq$25 Gb/s per wavelength), the use of colorless ONUs with tunable transponders is essential.

#### 3.2.3 OCDM-PON
Optical Code Division Multiplexing PON uses encoders and decoders to implement coherent or incoherent systems. This technology improves network security and bandwidth efficiency through one-dimensional (time/wavelength) or two-dimensional encoding.

#### 3.2.4 OFDM-PON
Orthogonal Frequency Division Multiplexing PON utilizes orthogonal subcarriers to eliminate interference and provide flexible spectrum allocation. It enables "optical grooming," where small connections are grouped without guard bands, though it is susceptible to frequency offsets from carrier mismatch.

## 3.3 What are the benefits of flexibility in optical networking supporting 5G communication infrastructure?
The authors advocate for a shift from Fixed Grid (fixed channel spacing) to Elastic Optical Networks (EON). In EON, the spectrum is discretized into smaller "frequency slots," allowing paths to be formed using only the necessary amount of spectrum. This is enabled by Sliceable Bandwidth Variable Transponders (SBVT) and Reconfigurable Optical Add-Drop Multiplexers (ROADM). 

Key benefits over fixed grids include:
*   **Spectrum Savings:** Adjustable spectral width based on frequency slots rather than fixed wavelengths.
*   **Service Variety:** Ability to support diverse services through variable channel counts and modulation types.
*   **Efficiency:** Optical traffic grooming eliminates guard bands, reduces O/E/O conversions, lowers latency, and minimizes the number of required transponders.

## 3.4 What are the research challenges on network flexibility implementation?
Implementing EON involves several open research problems:
*   **Routing and Spectrum Allocation (RSA):** Developing algorithms for dynamic lightpath establishment in C-RAN that balance latency and energy consumption.
*   **Traffic Prediction:** Using machine learning to predict uncertain mobile traffic patterns to optimize resource allocation.
*   **Spectrum Fragmentation:** Addressing the blocking of new demands caused by fragmented available spectrum through proactive or reactive solutions.
*   **Survivability:** Implementing protection and restoration schemes to prevent data loss from fiber or transponder failure, tailored to different QoS levels.
*   **Energy Management:** Reducing consumption via O/E/O elimination and employing "sleep mode" for antennas/devices during low traffic.
*   **Control Plane Design:** Employing Software Defined Networking (SDN) principles to manage data transmission across different domains.

## 4 Conclusion
The integration of optical networking is fundamental to the viability of 5G-enabled smart cities. While core networks are vital, improving optical access networks—specifically through PON technologies targeting 100 Gb/s and above—is critical for fronthaul/backhaul efficiency. The authors conclude that the transition from fixed to flexible optical grids (EON) is indispensable for achieving the capacity, reliability, and low latency required by the massive device density of future urban infrastructures.
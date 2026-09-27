---
index_terms:
  - 5G communication infrastructure
  - optical networking
  - smart city architecture
  - Passive Optical Networks (PON)
  - Elastic Optical Networks (EON)
  - C-RAN
  - spectral efficiency
---

# A review of optical networking technologies supporting 5G communication infrastructure

## Abstract
The paper examines the necessary integration of 5G wireless and optical technologies to realize smart city infrastructures. Because smart cities require the transmission of massive amounts of data for services like traffic management and electrical grids, reliable high-capacity transport networks are essential. The authors provide an overview of advanced optical networking developments required to support 5G core networking and connect the vast number of devices inherent in future smart city applications.

## 1 Introduction
Urbanization is driving a massive increase in data traffic, largely due to streaming video services (over 70% of Internet traffic). Optical fibers are the optimal medium for smart city development because they offer high bandwidth, low attenuation, and immunity to electromagnetic interference. However, current optical technologies using fixed spectrum allocation cannot meet the rigid demands of 5G. Consequently, there is a shift toward flexible network concepts.

The paper addresses four primary research questions (RQs):
- **RQ1:** The requirements 5G wireless places on optical networking.
- **RQ2:** Available and emerging optical technologies that support 5G.
- **RQ3:** The benefits of flexibility in the optical domain for 5G infrastructure.
- **RQ4:** Research challenges regarding the implementation of network flexibility.

## 2 Smart city layered architecture: an overview
The authors distinguish between physical architecture (buildings, roads) and communication architecture. They focus on a four-layer communication model necessary for IoT integration in smart cities:
- **Device/Sensing Layer:** Comprised of sensors and actuators that collect physical data; requires low latency and long battery life.
- **Communication Layer:** Consists of transport and access networks supporting enhanced mobile broadband (eMBB), massive machine-type communications (mMTC), and ultra-reliable low-latency communication (URLLC). This layer utilizes DWDM for long distances and PON or point-to-point (P2P) links for fronthaul/backhaul.
- **Data Layer:** Handles the organization, analysis, filtering, and storage of collected data to enable decision-making.
- **Application Layer:** The interface with citizens, delivering services such as smart healthcare, energy, and governance.

## 3 Data synthesis

### 3.1 What are the requirements of 5G wireless on optical networking?
5G infrastructure must meet stringent criteria for latency, bandwidth, and connectivity:
- **Traffic Volume:** Expected to be 100 times higher than 4G, with end-user data rates reaching 10 Gb/s.
- **Latency:** End-to-end delay must be a few milliseconds, with time-critical applications (e.g., healthcare, traffic safety) requiring less than 1 ms.
- **Energy Efficiency:** There is a critical need to minimize power consumption across sensing and transmission devices to ensure long battery life.
- **Spectral Efficiency:** Must be at least three times higher than 4G to accommodate huge traffic volumes within the available optical spectrum.

### 3.2 What are the available and emerging optical technologies supporting 5G wireless?
The transition from distributed RAN (D-RAN) to Cloud-RAN (C-RAN)—where baseband units (BBUs) are centralized—necessitates advanced optical transport for fronthaul and backhaul.
- **P2P Technology:** Limited to distances under 20 km; insufficient for the broader traffic demands of 5G.
- **PON Technology:** A point-to-multipoint architecture that reduces fiber usage through sharing (split ratios up to 1:256). It consists of an optical line terminal (OLT), optical distribution network (ODN), and optical network units (ONUs).

#### 3.2.1 TDM-PON
Time Division Multiplexing PON shares bandwidth on a single wavelength by assigning specific time slots to ONUs. While cost-effective, it suffers from security vulnerabilities and latency issues caused by the Dynamic Bandwidth Allocation (DBA) process in the OLT.

#### 3.2.2 WDM-PON
Wavelength Division Multiplexing PON assigns a dedicated wavelength to each ONU. This provides high capacity and low power insertion loss, making it suitable for 5G fronthaul. To support cell densification, research is focusing on tunable transponders to enable "colorless" ONUs capable of 25 Gb/s+.

#### 3.2.3 OCDM-PON
Optical Code Division Multiplexing PON uses encoders and decoders (coherent or incoherent) to separate signals. It offers superior network security and bandwidth efficiency compared to TDM.

#### 3.2.4 OFDM-PON
Orthogonal Frequency Division Multiplexing PON utilizes orthogonal subcarriers to eliminate interference and allow flexible spectrum allocation. This enables "optical grooming," where small connections are grouped into one transmitter. A primary disadvantage is the potential for frequency offset due to carrier mismatch. 

*Note:* Hybrid architectures, such as TWDM-PON, combine these technologies to maximize benefits.

### 3.3 What are the benefits of flexibility in optical networking supporting 5G communication infrastructure?
Traditional WDM/DWDM uses a "fixed grid" with equal channel spacing, which wastes spectrum when demand is low. Elastic Optical Networks (EON) replace this with a flexible grid where spectrum is discretized into frequency slots or slices.
- **Hardware requirements:** EON requires sliceable bandwidth variable transponders (SBVT) and reconfigurable optical add-drop multiplexers (ROADM).
- **Key Benefits:** 
    - **Spectrum Savings:** Adjustable spectral widths prevent waste.
    - **Efficiency:** Reduced O/E/O conversions, minimized latency, and optimized energy use through the use of variable transponders.
    - **Versatility:** Supports diverse services with varying modulation formats.

### 3.4 What are the research challenges on network flexibility implementation?
Implementing EON involves several complex challenges to minimize Capex and Opex:
- **Routing and Spectrum Allocation (RSA):** Developing algorithms for dynamic lightpath establishment in C-RAN that balance latency and energy consumption.
- **Traffic Prediction:** Using machine learning to predict uncertain mobile traffic patterns based on time and location to optimize resource allocation.
- **Spectrum Fragmentation:** Managing "holes" in the spectrum caused by dynamic demand to prevent new requests from being blocked.
- **Survivability:** Creating protection and restoration schemes for fiber or transponder failures while maintaining QoS tiers.
- **Energy Reduction:** Reducing O/E/O conversions and employing sleep modes for antennas during low-traffic periods.
- **Control Plane Design:** Implementing Software Defined Networking (SDN) to manage data transmission across different network domains.

## 4 Conclusion
The authors conclude that optical networking is the essential backbone for 5G-enabled smart cities. While PON technologies are strong candidates for fronthaul/backhaul due to their point-to-multipoint efficiency, they must evolve toward rates of 100 Gb/s and beyond via tunable transponders and new modulation formats. Ultimately, migrating from fixed grids to elastic optical networks (EON) is indispensable for achieving the capacity, reliability, and energy efficiency required by a massive number of future smart city devices.
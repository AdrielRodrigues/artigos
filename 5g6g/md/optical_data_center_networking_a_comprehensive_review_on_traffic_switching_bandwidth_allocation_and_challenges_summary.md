---
index_terms:
  - optical data center networking
  - optical switching technologies
  - bandwidth allocation schemes
  - DCN traffic characteristics
  - energy efficiency in DCs
  - silicon photonics
  - space division multiplexing
  - resource disaggregation
---

# Optical Data Center Networking: A Comprehensive Review on Traffic, Switching, Bandwidth Allocation, and Challenges

## I. Introduction
The rapid proliferation of AI/ML applications (e.g., ChatGPT) and data-intensive cloud services (IoT, AR/VR) has caused an explosion in data center (DC) traffic. Training deep neural networks requires massive data exchange via model, data, or hybrid parallelism, overloading existing electrical data center networks (DCNs).

### A. Motivation
Next-generation DCNs must meet stringent requirements: high bisection bandwidth, microsecond ($\mu\text{s}$) end-to-end latency, nanosecond ($\text{ns}$) switching times, and low energy consumption. Optical switching is the primary candidate to resolve these issues because it eliminates power-hungry optical-to-electrical (O/E) and electrical-to-optical (E/O) conversions, removes electronic processing delays, and provides data rate transparency.

### B. Related Surveys
While existing surveys focus on individual aspects such as energy consumption, topology, reconfigurability, or wireless DCNs, this paper provides a combined analysis of traffic characteristics, switching technologies, bandwidth allocation, space division multiplexing (SDM), disaggregated architectures, and power consumption.

### C. Original Review Contribution and Structure
The paper reviews the transition toward all-optical DCNs to serve time-sensitive cloud/edge applications. It is structured to cover background concepts, switching technologies, bandwidth allocation schemes, power consumption analysis, and future research directions.

## II. Background and Basic Concepts
Effective DCN design requires optimizing throughput and latency while managing traffic diversity and burstiness.

### A. Links
DCN links have evolved from Coarse WDM (CWDM) to Dense WDM (DWDM) to support higher data rates and optical amplification. Data rate capabilities have progressed rapidly: from 10 Gb/s (2007) to the current dominance of 400 Gb/s, with a shift toward 800 Gb/s using coherent digital signal processor (DSP) technology and future targets of 1.6T and 3.2T.

### B. Traffic
Traffic is analyzed as "flows" (sequences of packets related to one task). Modern DCN traffic is highly heterogeneous and categorized into three priority classes:
*   **Online/Real-time:** Time-sensitive (AR/VR, IoT) requiring the highest priority.
*   **Computing Applications:** Big data/AI training requiring medium priority and low packet loss.
*   **Storage Back-up:** Bandwidth-heavy but delay-tolerant applications with low priority.

#### 1) Locality
Traffic is primarily "East-West" (internal to the DC), comprising ~75% of total traffic. Intra-rack traffic ratios vary: university/enterprise DCs see 10–40%, while commercial cloud DCs reach up to 80% due to strategic server placement.

#### 2) Flow Size, Duration and Arrival Rate
Most flows are "mice flows" (small size, $<10\text{ KB}$), but a small percentage of "elephant flows" ($>100\text{ MB}$) account for the majority of transferred bytes. AI/ML applications generate significantly longer and larger flows than standard cloud services.

#### 3) Packet Size and Interarrival Time
Packet sizes follow a bimodal distribution: short control packets ($\sim 200\text{ B}$) and large data packets ($\sim 1400$–$1500\text{ B}$). Interarrival times vary by application; for example, media streaming requires very low interarrival times ($<12\mu\text{s}$) for real-time delivery.

#### 4) Burstiness
TCP slow start and hardware offloading (e.g., Large Send Offload) cause high traffic burstiness, leading to buffer occupancy, data loss, and increased task completion time, particularly at the Top-of-Rack (ToR) tier.

#### 5) Link Utilization and Congestion
Link utilization is typically higher in the core tier than in aggregation or ToR tiers. However, congestion and packet loss are more frequent at lower tiers due to bursty traffic patterns.

### C. Main DCN Design Objectives
*   **Performance Effectiveness:** Achieving deterministic low latency ($\mu\text{s}$) and high throughput by upgrading links (800G) and adopting all-optical switching.
*   **Scalability:** The ability to add hardware without degrading communication, necessitating adaptable routing protocols.
*   **Reconfigurability:** Real-time resource adjustment via SDN or ML/AI to balance loads; reconfiguration must occur on a millisecond scale to match traffic dynamics.
*   **Fault Tolerance:** Ensuring uninterrupted operation through redundant links and hybrid switching schemes to avoid single points of failure.

## III. Switching in DCNs

### A. Electrical Switching
Traditional three-tier architectures (ToR $\rightarrow$ Aggregation $\rightarrow$ Core) rely on electrical switches that require frequent O/E/O conversions. This results in high power consumption and bandwidth bottlenecks due to oversubscription and hardware limitations (e.g., switch chip pin counts). Co-packaged optics is an emerging research area to mitigate these limits.

### B. Optical Switching
Optical switching offers bit-rate transparency, lower power per bit, and a decoupling of port count from data rate.

#### 1) Optical Circuit Switching (OCS)
OCS establishes a dedicated optical path before transmission. While it provides high bandwidth and is used by companies like Google (via MEMS), it suffers from long setup times ($\text{ms}$) and poor utilization in bursty traffic environments due to the lack of optical RAM.

#### 2 and 3) Optical Packet (OPS) and Burst Switching (OBS)
*   **OPS:** Routes traffic per packet, offering high flexibility and statistical multiplexing. However, it is currently non-viable for large scale due to the absence of optical buffering.
*   **OBS:** Transmits a control header before the data burst, reducing setup time compared to OCS. It avoids the need for buffers but requires complex contention resolution to prevent dropping bursts.

#### 4) Technologies for Optical Switching
*   **MEMS:** 2D-MEMS are fast ($\text{sub-}\mu\text{s}$) but limited in port count; 3D-MEMS support large scales (hundreds of ports) but are slow ($\text{ms}$).
*   **LCoS and Piezoelectric:** Provide $\text{ms}$-scale switching.
*   **MRR and MZI:** Use thermo-optic or electro-optic effects to achieve $\mu\text{s}$ to $\text{ns}$ speeds. Silicon photonics integration enables the $\text{ns}$ scale.
*   **Wavelength Routing (AWG):** Achieves $\text{ns}$ switching based on tunable laser speeds.
*   **SOA:** Provides extremely fast ($\text{ns}$) switching but is limited by Amplified Spontaneous Emission (ASE) noise.

## IV. Bandwidth Allocation in Optical DCNs
Bandwidth allocation aims to minimize latency and packet loss through effective access control.

### A. Bandwidth Allocation for Intra-Rack Communication
Intra-rack systems often use Passive Optical Interconnects (POI), such as couplers or splitters, to reduce power. 
*   **Access Control:** Distributed schemes are preferred over centralized SDN controllers to avoid single points of failure and reduce delay.
*   **Strategies:** Synchronous strategies can totally avoid collisions via Pre-Transmission Coordination (PTC) but require expensive synchronization. Asynchronous strategies are more flexible but rely on Carrier Sensing (CS) or Control Messages (CM).

### B. Bandwidth Allocation for Inter-Rack Communication
Inter-rack allocation manages the configuration of optical switches to route lightpaths between ToRs.
*   **Prototypes:** Early hybrid E/O systems used MEMS; recent all-optical prototypes use SOA-based switching for $\text{ns}$ reconfiguration.
*   **Mechanisms:** Most inter-rack schemes use synchronous transmission and PTC or Routing and Wavelength Assignment (RWA) algorithms to eliminate collisions.

## V. Power Consumption in DCNs

### A. Power Consumption for Cooling
Cooling accounts for $\sim 40\%$ of total DC power. Efficiency is measured by Power Usage Effectiveness (PUE). Hyperscale DCs achieve PUE $\approx 1.1$ through liquid cooling and "free cooling" (placing DCs in cold climates).

### B. ML/AI Impact on DC Power Consumption
AI workloads dramatically increase energy demand; GPUs consume up to 15 times more power than CPUs. AI queries (e.g., ChatGPT) are significantly more energy-intensive per request than standard search queries, leading to forecasts of tripled energy demands by 2030.

### C. DCN Architecture Impact on Power Consumption
Hierarchical Tree-tier architectures are the most energy-efficient due to fewer switches and links but suffer from capacity bottlenecks. Fat-Tree offers a balance of performance and efficiency. BCube and DCell are generally less efficient because servers act as relay nodes, requiring more network interfaces.

### D. Directions for DCN Power Consumption Reduction
*   **Switching Integration:** Replacing electrical switches with optical ones to remove O/E/O conversions (e.g., Google's 41% saving in Jupiter).
*   **Silicon Photonics:** Using MRR and MZI structures; Phase Change Materials (PCM) like $VO_2$ and GST provide non-volatile, energy-efficient switching.
*   **Transceivers:** Adopting VCSELs for short reach and coherent lasers for inter-DC links.
*   **Management:** Implementing SDN-based "energy-aware" routing to power down underutilized links and using ML/AI to predict traffic and deactivate idle devices.

## VI. Future Directions in Optical DCNs Research

### A. ns Switching Control
While physical switching can happen in $\text{ns}$, the *decision* process (header processing) is still too slow. Scaling this control logic to $\text{ns}$ levels is a critical open challenge.

### B. Fast Clock Data Recovery
Optical receivers must perform CDR within $\text{ns}$ for bursty traffic at 800 Gbps+ rates; otherwise, throughput drops and latency increases.

### C. Optical Buffering
The lack of optical RAM prevents the realization of true OPS. Fiber Delay Lines (FDLs) exist but are too complex and introduce excessive queuing delay for large-scale DCNs.

### D. Bandwidth & Access Control Efficiency
Because there is no buffering, contention resolution must be perfect to avoid data loss. This necessitates more advanced bandwidth allocation schemes that account for AI-driven traffic burstiness.

### E. Self-Driven DCN Reconfigurability
Integrating ML/AI (e.g., Deep Reinforcement Learning) allows the network to automatically forecast traffic and reconfigure topology, routing, and resource allocation without human intervention.

### F. Space Division Multiplexing (SDM)
To overcome WDM capacity limits, SDM uses multi-core fibers (MCF). The primary challenge is Inter-Core Crosstalk (IC-XT), which can be mitigated by using uncoupled cores or bi-directional transmission in adjacent cores.

### G. Disaggregation in DCNs
The "resource-centric" paradigm disaggregates CPU, memory, and storage into shared pools to eliminate resource fragmentation. This requires an ultra-low latency optical fabric to ensure that remote memory access mimics local memory speeds ($\text{ns}$ scale).

## VII. Conclusion
The surge of AI/ML and data-intensive applications necessitates a shift from electrical to optical DCNs. While OCS is currently used for core tiers, the future lies in all-optical networks featuring $\text{ns}$-scale switching, SDM for massive capacity, and ML-driven self-reconfigurability to handle heterogeneous, bursty traffic efficiently.
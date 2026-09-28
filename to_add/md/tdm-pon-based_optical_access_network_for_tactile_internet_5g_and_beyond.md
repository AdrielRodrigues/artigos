# TDM-PON-Based Optical Access Network for Tactile Internet, 5G, and Beyond

HwanSeok Chung, Han Hyub Lee, Kwang Ok Kim, Kyeong-Hwan Doo, YongWook Ra, and ChanSung Park

# Abstract

An optical access network plays a critical role in accommodating explosive new services such as augmented reality (AR), virtual reality (VR), machineto-machine, and human-to-machine interaction applications. Continuous expansion of capacity as well as low latency in the optical access network are very important issues to avoid loss of connectivity for 5G and Tactile Internet. A time-division multiplexing passive optical network (TDM-PON) is an attractive solution to provide optical connectivity to end users in residential, business, and mobile applications since multiple remote nodes with simple optical power splitters give us easy-to-use optical connection anywhere in an optical distributed network. This article reviews TDM-PON-based optical access technologies for bandwidth-intensive as well as low-latency services, and introduces a recent feasibility demonstration of a Tactile Internet testbed. Technical challenges faced by TDM-PON for future networks in terms of capacity, latency, and virtualization/slicing are also discussed.

# Introduction

The optical access network uses optical fiber as the main transmission medium to provide broadband services to end users typically within a distance of 20 km [1, 2]. With the replacement of traditional copper wires with optical fibers since the 2000s, time-division multiplexed passive optical networks (TDM-PONs) have been deployed so far in public fiber-to-the-home or -building (FTTH/ FTTB) networks for broadband services. With the help of the simplicity of a passive point-to-multipoint (PtMP) optical distributed network (ODN) architecture, TDM-PON is an attractive solution to provide optical connectivity in a cost-effective way since multiple remote nodes with simple optical power splitters give us easy-to-use optical connection anywhere in the ODN. As a result, TDM-PONs are currently expanding its applications beyond residential FTTH areas such as in mobile communication networks to accommodate 5G and 6G.

The growing demand for mobile data traffic is a main driving force in the optical access network, as shown in Fig. 1. As mobile communications continue to evolve over 4G, 5G, and beyond 5G, the carrier frequency is getting higher to accommodate explosive data traffic [3]. Because high carrier frequency cannot propagate into indoor or long-distance, the cell size would be decreased for better coverage and capacity distribution. The higher carrier frequency of mobile networks shortens the propagation distance of wireless links, and optical fiber penetrates deeper toward end users. In addition, the speed of the optical access network should be upgraded from 10 Gb/s to 25 Gb/s or beyond. For example, 4G LTE fronthaul with common public radio interface (CPRI) requires only 2.5 Gb/s optical access speed in the case of a 2 2 multiple-input multiple-output (MIMO) scheme. The 5G network will provide up to 20 Gb/s peak data rate with millimeter-wave band, which leads to optical access speed over 25 Gb/s per wavelength even though function split fronthaul is employed. Thus, cost-effective solution of high-speed optical connectivity to the end user becomes a very important issue.

Another driving force in the optical access network is the Tactile Internet applications required in machine-to-machine and human-to-machine interaction [4, 5]. Unlike the content-oriented conventional network focusing on the delivery of audiovisual and data traffic, Tactile Internet requires control-based communications providing real-time control and physical tactile experiences over the Internet along with conventional data traffic. Among the human senses, the response time of audio and visual information are on the order of 100 ms and 10 ms, respectively. The tactile sense requires an extremely short response time of around 1 ms. Since all human senses can interact with machines and their environments, the network must meet the speed of our natural reaction times in order for network to match human interaction with their environment and machine-to-machine interactions.

The emerging new services such as 8K UHD, virtual reality (VR) and augmented reality (AR), smart factory, vehicle-to-everything (V2X), online meeting, and online broadcasting of single-person independent media do not have the same bandwidth and latency needs [6]. Many of these applications could be delivered on existing networks. Machine-to-machine connectivity and Internet of Things (IoT) devices could be accommodated with low data rate less than 10 Mb/s and relatively high latency around 100 ms. The latency is less well tolerated in videoconferencing than in video streaming where some buffering can be used. However, autonomous vehicles, AR, and Tactile Internet need a new network, and these applications require 1 Gb/s capacity and less than 1 ms latency. The future optical access networks need to respond to a range of speed from low data rates to very high data rates with various latencies.

This article reviews a recent feasibility demonstration of a Tactile Internet testbed to support bandwidth-intensive as well as low-latency appli-

Digital Object Identifier:

10.1109/MNET.008.2100641 *The authors are with the Electronics and Telecommunications Research Institute, Korea.*

cations. A packet-level channel bonding over multiple wavelengths and low-latency-oriented cyclic dynamic bandwidth allocation (DBA) are utilized to support capacity of 50 Gb/s or higher and latency of less than 1 ms. Technical challenges that TDM-PON will face in the future network in terms of capacity, latency, and virtualization/ slicing are also discussed.

# High-Capacity and Low-Latency PON

### Constraints of the Optical AccessNetwork

The optical access network has different industry and research goals and constraints compared to those in the core network. In the core network, maximizing capacity in a single fiber and decreasing cost per bit are important issues. However, increasing capacity maintaining low cost per user is the main objective in the access area, which requires a clever idea to improve performance where constraints of legacy infrastructure, service, and serving area are important. There has been a dogma that electrical power at the outside plant, an optical amplifier, and dispersion compensating fiber are not allowed in the optical access network for cost-effective implementation, as shown in Fig. 2. Thus, a simple method having reasonable performance is needed to satisfy ODN structure, bandwidth, latency, quality of service, transmitter and dispersion penalty (TDP), and coexistence.

Recently, there have been substantial efforts to find practical solutions for the optical access network to accommodate emerging new services. Research has been carried out in two directions: increasing speed per wavelength and reducing latency per connection. Unlike 1G-Ethernet PON (EPON), Gigabit PON (GPON), 10G-EPON, and 10 Gigabit-capable symmetric PON (XGS-PON) which utilize conventional-band (C-band) downstream and original-band (O-band) upstream, the beyond 10G PON such as IEEE 50G-EPON [1] and 25GS-PON multi-source agreement (MSA) [2], or International Telecommunication Union Telecommunication Standardization Sector (ITU-T) higher-speed PON (HSP), utilize O-band for both upstream and downstream transmission. This is because chromatic dispersion, power budget, size, and cost of optics issues could be resolved by O-band with non-return-to-zero (NRZ) modulation. Enhanced receiver sensitivity with an avalanche photo diode (APD)-based receiver is a possible solution for the power budget issue. Since the upstream transmission in the typical TDM-PON is mostly focused on higher bandwidth efficiency to ensure fairness among the residential users, Tactile Internet applications could not be accommodated in conventional TDM-PON. Thus, enhanced DBA schemes have been widely investigated to have low latency in upstream transmission [7]. The enhanced DBA allows time-critical applications such as Tactile Internet services to be accommodated with residential applications within the same ODN.

## TDM-PONPrototype Based on 25 Gb/s Per Wavelength

Figure 3a shows a high-capacity and low-latency PON prototype for Tactile Internet applications. Channel bonding and low-latency DBA were installed in the field programmable gate array (FPGA)-based optical line terminal (OLT) line card. We also implemented a 25G bidirectional optical sub-assembly (BOSA) module, and installed it in

![](_page_1_Picture_7.jpeg)

FIGURE 1. Mobile traffic, the driving force of the optical access network.

![](_page_1_Figure_9.jpeg)

FIGURE 2. Constraints in the optical access network.

the 25G PON transceiver. The prototype is implemented based on IEEE 50G-EPON due to its ONU capacity over 25 Gb/s and capacity upgradability by channel bonding. Channel bonding, one of the unique features of 50G-EPON, enables coexistence of multi-speed optical network units (ONUs) in a single ODN. The ONU capacity depends on the number of wavelengths used by an ONU. For example, in the case of channel bonding with two wavelengths, a 25G ONU utilizes one wavelength (-0) and 50G ONU utilizes two wavelengths (-0 and -1). These two different-speed ONUs could share upstream bandwidth by time-division multiplexing. Easy capacity upgrade is also possible by channel bonding. In the first generation, only 25G ONU exists in the ODN, and the OLT serves only 25G ONU. In the second generation, some ONUs could be upgraded to 50 Gb/s by adding additional wavelength. 100 Gb/s ONU capacity is also possible by using four wavelengths, even though 100 Gb/s speed is not adopted in 50G-EPON. The channel bonding is implemented in a multipoint reconciliation sublayer (MPRS) of the Ethernet protocol layer. A two-dimensional envelope alignment buffer and an envelope position alignment marker (EPAM) were used for frame alignment and skew compensation [8]. The channel bonding doubles the ONU capacity by using two wavelengths, and the DBA selects available wavelength for delivering a packet for low-latency services. Thus, selecting a specific wavelength for low-latency transmission is difficult [1]. When channel bonding is implemented with FPGA and 10 Gb/s upstream burst-mode transmission, the measured upstream throughput was 16.7 Gb/s, whereas the throughput was limited to less than 8.3 Gb/s without channel bonding. The upstream throughput depends on the length

IEEE Network • March/April 2022 77

![](_page_2_Figure_0.jpeg)

FIGURE 3. a) High-capacity and low-latency PON prototype based on IEEE 50GEPON; b) experimental setup for optical link performance, commercial IPTV transmission, and the measured result of file upload/down test.

of Ethernet payload and forward error correction (FEC) overhead. In the case of a long payload packet, the throughput would be around 8.7 Gb/s. In our experiment, we have utilized variable payload length from 64 bytes to 1518 bytes, which reduced the upstream throughput to around 8.3 Gb/s.

The DBA algorithm in conventional TDM-PON systems is mostly focused on high utilization of upstream capacity and fairness among ONUs. Upstream latency becomes several milliseconds due to the competition of each ONU, while downstream latency is very low. This could be resolved by low-latency DBA with a differential quality of service (QoS) method. Total uplink capacity is divided into four levels: gold, silver, bronze, and best effort services. First of all, the upstream bandwidth is assigned to the gold class using a static cycle-based method. The remaining bandwidth is then dynamically assigned to the other classes by credit-based weighted fair queueing. Because bandwidth is assigned to this class at least once within up to two cycles in the DBA algorithm, the latency of the gold class is guaranteed [8]. Gold level services are served every 250 s, and long-length traffic in other classes are divided and served in the next cycle. The tactile service is assigned to gold or silver class, and non-time-critical services are allocated to bronze or best effort. However, it should be noted that this value is not sufficient for the fronthaul application, and the cooperative DBA (Co-DBA) described below is one solution to solve this issue.

Figure 3b shows the experimental setup for the performance evaluation of an optical link. The distance of trunk fiber was set to 5 km, and the distances between remote node and different-speed ONUs were set to be 1 km, 10 km, and 15 km, respectively. First of all, we have measured opti-

78 IEEE Network • March/April 2022

![](_page_3_Figure_0.jpeg)

FIGURE 4. Feasibility demonstration of Tactile Internet.

cal link performances. The sensitivity of 25 Gb/s downstream was measured to be –24 dBm at bit error rate (BER) of 10–3, and there was no difference among the ONU distance. From the 10 dB to 22 dB loud and soft ratio, burst mode transmission has very uniform packet loss rate performance. During the 50-hour long-term stability test, all the ONUs show uniform performance. Latency in the gold class traffic is less than 0.4 ms regardless of offered traffic condition. As we increase traffic load, the latency in the silver, bronze, and best-effort classes goes over 10 ms. When we turned on FEC, it makes 6 dB optical gain, and there was no packet drop in the downstream and upstream. Commercial IP television (IPTV) services were also connected to 50G-EPON OLT and ONU to evaluate typical residential applications for the implemented PON prototype. The quality on the screen was very clear, and we could select any IPTV channel. File upload and download speed were also measured with a commercial server. The upstream and downstream speed were measured to be less than 8.9 Gb/s and 8.2 Gb/s, respectively. This is mostly due to the speed limitation of the 10GE link between the IP network and the PON system.

### Tactile Internet Testbed

Figure 4 shows the testbed for the feasibility demonstration of Tactile Internet based on TDM-PON. The testbed is composed of optical access and core network. The OLT and ONU, the same TDM-PON prototype used in Fig. 3, were placed in the access network on the Electronics and Telecommunications Research Institute (ETRI) side, Daejeon. The transmission link in the core network, the Korea advanced research network (KOREN), was composed of reconfigurable optical add/drop multiplexer (ROADM), 258 km of single mode fiber, Erbium doped fiber amplifier (EDFA), and a dual polarization-quadrature phase shift keying (DP-QPSK)-based coherent optical transceiver operating at 100 Gb/s. For the demonstration of low-latency application with Tactile Internet tested, an inverted pendulum was utilized. An inverted pendulum is a pendulum that has its center of mass above its pivot point. It can be suspended stably in this inverted position by using a control system to monitor the angle of the pole and move the pivot point horizontally back under the center of mass when it starts to fall over, keeping it balanced. To properly keep the pendulum upright and maintain balance, the control and position information between controller and pendulum should be exchanged around millisecond order. Thus, the inverted pendulum corresponds to simulating a remotely controlled robot requiring a Tactile Internet connection. The inverted pendulum was set beside the ONU located at the optical access network, and the controller was installed on the Seoul node, 278 km away from the pendulum. Uncompressed 4K ultra high density (UHD) video with a transmission speed of 6 Gb/s was also utilized to emulate a robot's vision. The traffic output from an uncompressed 4K UHD server was sent to the OLT via 20 km access link and then traveled through 258 km of ROADM link. After the Ethernet switch and UHD receiving system, the video was displayed on the monitor located at the Seoul site. The measured latency of access link and long-haul link were around 300 s and 1.3 ms, respectively. The optical propagation delay over the 258 km of optical fiber is the dominant factor in the measured latency. A feedback control system at the Seoul site monitors the pendulum's angle and controls the position of the pivot point before the pendulum starts to fall over, which leads to the inverted pendulum being properly controlled and maintaining balance. The measured quality of uncompressed 4K UHD video after transmission of 278 km over a TDM-PON link and long- haul link was also very clear. On the other hand, when we intentionally set high latency and low capacity in a TDM-PON system, the inverted pendulum lost its balance, and the video was also frozen and degraded. The feasibility of high-capacity and low-latency PON was successfully confirmed by the IPTV service, file upload/ download, and Tactile Internet testbed combined with optical access link and long-haul link.

# Optical Access for FutureNetworks

Future optical access networks based on TDM-PON will have various challenges including high capacity, low latency, virtualization, and slicing. The capacity of current PON standards is not enough for 6G applications. The latency with advanced DBA is good for backhaul and midhaul application; however, reduced latency is needed for fronthaul application. To support different types of applications within the same ODN and to accommodate more functions flexibly, we need virtualization and slicing of the access network.

IEEE Network • March/April 2022 79

![](_page_4_Figure_0.jpeg)

FIGURE 5. Modulation formats for high-speed TDM-PON.

### High Capacity

First of all, the speed of PON port will evolve to 100 Gb/s and beyond. The high-speed channel over 100 Gb/s must be accommodated while keeping the power budget of the legacy PON and ODN. However, limited launched power, poor receiver sensitivity of high-speed optical components, and chromatic dispersion of fiber are still obstacles to maintain high power budget in the TDM-PON [9, 10]. Recently, there have been many research studies to find an appropriate modulation format for high-speed PON, as shown in Fig. 5. One approach is coherent detection with a single carrier or orthogonal frequency-division multiplexing (OFDM). Multi-level modulation such as DP-QPSK or dual polarization-quadrature amplitude modulation (DP-QAM) can be used for data modulation. Direct detection including NRZ-on/off keying (OOK), duo-binary, differential quadrature phase shift keying (DQPSK), or multilevel pulse amplitude modulation (PAM) combined with electrical digital signal processing (DSP) is also a solution for the high-speed PON. Unlike the medium access layer (MAC), the structure and cost of the physical (PHY) layer are significant depending on the modulation method. The relative cost of optical transceivers employing an advanced modulation format is more important for ONU transceivers since the cost of an ONU transceiver is not shared across ONUs. A direct detection has merits of simple configuration and nonlinearity tolerance, particularly in NRZ format, whereas the chromatic dispersion compensation and relatively high baud rate are issues to be resolved. The coherent detection has many merits such as good receiver sensitivity, chromatic dispersion compensation, and distortion mitigation. The cost-effective implementation with low-complexity structure would be a good approach to practically use coherent optics in high-speed PONs [11, 12]. It should be noted that channel bonding can be also used to increase the capacity of a PON port over 100 Gb/s in addition to multi-level modulation and coherent detection.

### Low Latency

Low-latency data transmission in the optical access network is also important. In the legacy TDM-PON system with advanced DBA, the achievable latency of upstream traffic depends on DBA cycle time, allocated time for time-critical applications, and fiber delay. A short DBA cycle reduces latency, but in the case of large overhead, it reduces packet throughput. The required latency in the midhaul and backhaul in the mobile network is higher than the typical latency of TDM-PON with advanced DBA. For the use of TDM-PON in the fronthaul, however, the latency should be further reduced. Ultra-low-latency transport technologies are being standardized in the Open Radio Access Network (ORAN) alliance [7] and ITU-T [12]. 5G mobile traffic utilizes slot-based scheduling, and each slot has its own upstream and downstream traffic configuration. To reduce the upstream latency in a TDM-PON, Co-DBA in OLT allocates variable bandwidth to follow a variable mobile traffic pattern by exchanging the pattern of mobile traffic and scheduling information between optical and mobile equipment via a cooperative transport interface (CTI) message. It is based on the notification of information about the mobile traffic pattern from mobile equipment to the OLT. With this information, the OLT can apply targeted bandwidth allocations aimed to address the corresponding traffic volumes and time intervals as indicated in the information. The OLT and mobile equipment should share a common time of day (ToD) reference for low-latency transmission. Since the required accuracy for CO-DBA is on the order of multiple microseconds, the accuracy for synchronization at the OLT offered by any usual method such as IEEE-1588 and Synchronous Ethernet (SyncE) could be used.

### Virtualization and Slicing

Other demands in future PONs are optical access slicing and flexibility through virtualization and optical disaggregation [14],[15]. The assignment of logically separated network resources optimized for different service characteristics is needed to accommodate different types of services. Scalability to serve more functions independent of physical infrastructure is also considered. Because of the structure of a purpose-oriented OLT system, assigning optimized resources for various services or replacing new functions has limited flexibility. The flexibility and slicing of an optical access network could be achieved by abstracting and virtualizing a physical PON after disaggregating an OLT into a physical part and a logical part. The legacy TDM-PON is composed of fixed hardware and fixed functions. The OLT controls ONU bandwidth with one DBA per PON port in one physical network. By disaggregating and virtualization, the PON can be divided into physical and logical resources. The physical resources include upstream ports, PON cards, PON ports, and ONUs, while the logical resources comprise hardware forwarding entries, bandwidth profile, and type of DBA. These OLT resources can be allocated on demand and then exclusively used by the intended slices for different applications.

# Summary

The recent feasibility demonstration of a TDM-PON prototype is reviewed for Tactile Internet, 5G, and beyond. High capacity by multiple channel bonding and low latency with advanced DBA were implemented with FPGA and installed in the OLT

80 IEEE Network • March/April 2022

and ONU prototype. Commercial IPTV service, file upload/download, remote control of inverted pendulum, and transmission of uncompressed 4K UHD traffic are successfully accommodated by the TDM-PON prototype. Technical challenges faced by TDM-PON for future access networks are also discussed. Future optical access networks will have various challenges such as choosing an appropriate modulation format for a 100 Gb/s optical access network, ultra-low-latency packet transmission, and optical access slicing and flexibility through virtualization and optical disaggregation.

### Acknowledgment

This work was supported by Institute of Information & Communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (MSIT) (No. 2019-0-00452, High speed optical access and slicing technology for B5G).

#### References

- [1] IEEE P802.3ca 100G-EPON Task Force, "Physical Layer Specifications and Management Parameters for 25 Gb/s and 50 Gb/s Passive Optical Networks," 2018; http://www. ieee802.org/3/ca/.
- [2] Multi-Source Agreement, "25GS-PON Specification v1.0," Oct. 2020; https://www.25gspon-msa.org/wp-content/ uploads/2020/10/25GSPONSpecification- V1.0-public.pdf.
- [3] IEEE, "5G and Beyond Technology Roadmap," white paper, Oct., 2017.
- [4] ITU-T Technology Watch Report, "The Tactile Internet," Aug. 2014.
- [5] W. Na *et al*., "Simulation and Measurement: Feasibility Study of Tactile Internet Applications for mmWave Virtual Reality," *ETRI J*., vol. 42, no. 2, Apr. 2020, pp. 163–74.
- [6] D. Warren and C. Dewar, "Understanding 5G: Perspectives on Future Technological Advancements in Mobile," *GSMA Intelligence*, 2014.
- [7] ORAN-WG4.CTI-TCP.0-v01.00, "Cooperative Transport Interface, Transport Control Plane Specification," 2020
- [8] K.-O. Kim *et al.*, "High Speed and Low Latency Passive Optical Network for 5G Wireless Systems," *IEEE/OSA J. Lightwave Technol.*, vol. 37, no. 12, June 15, 2019, pp. 2873–82.
- [9] V. Houtsma and D. van Veen, "Optical Strategies for Economical Next Generation 50 and 100G PON," *Proc. OFC*, San Diego, CA, 2019, Paper M2B.1.
- [10] Han Hyub Lee *et al.*, "Demonstration of High-Power Budget TDM-PON System with 50 Gb/s PAM4 and Saturated SOA," *IEEE/OSA J. Lightwave Tech*., vol. 39, no. 9, May 2021, pp. 2762–68.
- [11] Z. Jia and L. A. Campos, "Coherent Optics Ready for Prime Time in Shorthaul Networks," *IEEE Network*, Jan./Feb. 2021. [12] M. S. Erkılınç *et al*., "Comparison of Low Complexity Coher-

The recent feasibility demonstration of a TDM-PON prototype is reviewed for Tactile Internet, 5G, and beyond. High capacity by multiple channel bonding and low latency with advanced DBA were implemented with FPGA and installed in the OLT and ONU prototype.

ent Receivers for UDWDM-PONs (l-to-the-User)," *IEEE/OSA J. Lightwave Tech.*, vol. 36, no. 16, Aug., 2021, pp. 3453–64. [13] ITU-T, "Network Slicing in a PON Context," Apr., 2021. [14] H. Uzawa *et al.*, "First Demonstration of Bandwidth-Allocation Scheme for Network-Slicing-Based TDM-PON toward 5G and IoT Era" *Proc. OFC*, San Diego, CA, 2019, Paper W3J.2.

#### Additional Reading

[1] ITU-T, "OLT Capabilities for supporting CO-DBA," Apr. 2021.

### Biographies

Hwan Seok Chung has been with ETRI, where he leads the research of optical access network for mobile traffic, since 2005. He served as a TPC member of OFC, ECOC, OECC, and Photonics West. He has been the recipient of the Prime Minister Award from the Korean Government for distinguished achievement in industry (2019).

Han Hyub Lee received his Ph.D. degree in physics from Chungnam National University, Republic of Korea, in 2005. He is a principal researcher at ETRI, where he is responsible for highspeed optical access network research. He has been active in ITU-T, IEC, and IEEE.

KwangOk Kim received his Ph.D. degree in electronic engineering from Chungnam University in 2014. Since 2001, he has worked at ETRI. His current research interests include the next-generation optical access network and wired/wireless converged network.

Kyeong-Hwan Doo received his Ph.D. degree in electronic engineering from Chungnam National University in 2013. Since 2000, he has worked at ETRI. His research interests include low-latency scheduling algorithms in passive optical networks.

YongWook Ra received his Ph.D. degree from Korea Advanced Institute of Science and Technology, Daejeon, Republic of Korea, in 2019. Since 2001, he has been a principal research staff member at ETRI. His research interests include next-generation networks, carrier-class Ethernet, MPLS-TP, and optical communications.

Chansung Park received his B.S. degree from the Department of Computer Science, Inje University, Kimhae, Republic of Korea, in 2011. Since 2012, he has worked at ETRI as a researcher. His research interests include software infrastructure in cloud, software defined networking platform, machine intelligent networking, and optical communications.

IEEE Network • March/April 2022 81
![](_page_0_Picture_1.jpeg)

# A review of optical networking technologies supporting 5G communication infrastructure

Suzana Miladić-Tešić<sup>1</sup> • Goran Marković<sup>2</sup> • Dragan Peraković<sup>3</sup> • Ivan Cvitić<sup>3</sup>

Accepted: 24 February 2021 / Published online: 13 March 2021 © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2021

#### **Abstract**

The advanced communication networks require heterogeneous emerging technologies to be combined while enabling various future applications. The integration of 5G wireless and optical technology is considered an unavoidable approach to reach this goal. Based on 5G mobile communications and densification of cells, the upcoming idea of smart city becomes feasible and put on a lot of attention from the research community due to its effect on everyday life's improvement and modernization. The concept of a smart city should support everything from electrical grids to traffic management and requires the transmission of a huge amount of data. Smart city planning with a reliable communication infrastructure that can provide stringent network requirements is unfeasible without the joint of optical and wireless technologies. This paper aims to provide an overview of recent developments of advanced optical networking to provide 5G transport networks and their applications in connecting a huge number of devices in future smart city infrastructures. The implementation of optical technologies in 5G core networking open numerous questions of how wireless and optical can coexist to provide sophisticated future applications, such as the smart city concept. Within this research, we will provide the answers to some of the key related questions.

**Keywords** 5G · Backhaul/fronthaul · Optical networking · Elasticity · Convergence

#### 1 Introduction

The expansion of urbanization brings huge challenges in city functioning causing that terabytes of data will be moved and processed by hosted cloud computing servers. The global information infrastructure that provides data transmission and processing relies on optical fiber communications and the upcoming question is how deep these communications will penetrate other forms of communications. It is evident that more than 70% of all Internet traffic belongs to the advanced streaming video services and this percentage is further rising. The definition of a

Optical fibers are the right choice in smart city development due to their inviolable benefits, such as the extremely high bandwidths, low attenuation, no electromagnetic interference, small size, etc. For existing wireless backhaul networks as well as for fronthaul, the optical fiber

![](_page_0_Picture_16.jpeg)

smart city in the literature is not yet standardized due to broad viewpoints. Various cities have diverse development areas of interest which makes different the criteria to become smart. Smart city definitions were analyzed by the ITU-T (International Telecommunication Union Telecommunication Standardization Sector) Focus Group on Smart Sustainable Cities (FG-SSC). Definition approved by the FG-SSC is as follows: "A smart sustainable city is an innovative city that uses information and communication technologies (ICTs) and other means to improve quality of life, efficiency of urban operation and services, and competitiveness, while ensuring that it meets the needs of present and future generations concerning economic, social and environmental aspects" [1]. The main challenges and trends in implementation of smart cities are presented in

Suzana Miladić-Tešić suzana.miladictesic@sf.ues.rs.ba

Faculty of Transport and Traffic Engineering, University of East Sarajevo, Doboj, Bosnia and Herzegovina

Faculty of Transport and Traffic Engineering, University of Belgrade, Belgrade, Serbia

Faculty of Transport and Traffic Sciences, University of Zagreb, Zagreb, Croatia

technology is a promising solution. To achieve all that 5G networks are expected to offer, considering the plenty of connected devices, numerous residential, enterprise and broadband mobile services, a denser fiber network infrastructure will be required. The role of optical technologies to provide the key network performances such as ultra-high latency, reliability and high data rates has been surveyed in [\[3](#page-6-0)]. It is evident that currently available optical technologies with fixed spectrum allocation will not be capable to fulfill the rigid and huge future demands. That is why the migration to flexible concept is the subject of extensive researching in recent years.

In this paper, we extend notably our preliminary research recently presented in [\[4](#page-6-0), [5](#page-6-0)], focusing on more comprehensive analyse of optical networking technologies to support the 5G communication infrastructure that is needed for smart city development. More specifically, our main goal here is to provide the extended answers to some research questions (RQ) considering the 5G communication infrastructure deployment including the following:

- RQ 1. What are the requirements of 5G wireless on optical networking?
- RQ 2. What are the available and emerging optical technologies supporting 5G wireless?
- RQ 3. What are the benefits of flexibility in optical domain supporting 5G communication infrastructure? RQ4. What are the research challenges on network flexibility implementation?

To answer these research questions, the structure of the paper is as follows. The basic smart city communication architecture is presented in the second section. The third section gives the answers to the pointed questions. Finaly, the fourth section concludes the paper.

## 2 Smart city layered architecture: an overview

There are two types of smart city architectures: the physical that is composed of buildings, roads, transportation and power elements and the communication architecture that enables the physical elements to be interconnected. We are focused here on the smart city communication architecture.

The basic characteristics of a smart city are presented in [\[1](#page-6-0), [2](#page-6-0)]. The smart city indicators related to economy, transportation, urban planning, governance, etc. are commonly used for evaluation in various studies to investigate what city is the smartest. In order to connect a huge number of smart city objects, communication networking plays a major role. It is clear that the Internet of Things (IoT) paradigm is directly related to the smart city concept deployment. Regarding the IoT, things are elements or parts of the physical or the information world. Physical things can be sensed and connected while virtual things can be stored, processed, and accessed [[6\]](#page-6-0).

The architecture composed of following key layers is the starting point for the smart city operation [[7\]](#page-6-0): application layer, data layer, communication layer and device/sensing layer (as shown in Fig. 1). Such architecture is partly possible to be realized with the existing communication networks, while the evolving or next-generation networks are the promising future solution.

Device/Sensing layer is composed of a huge number of devices, cameras, sensors and actuators that monitor and collect data and different parameters from the physical infrastructure. Superior sensor coverage means higher level of city's smartness. This is the layer where optical technologies could be presented in form of optical sensors and actuators. Sensors do not require high bandwidth, but low latency and long batery life.

The communication layer is composed of transport and access networks that enable smart city services to be realized. This layer should provide enhanced mobile broadband (eMBB), massive machine-type communications (mMTC) and ultra-reliable low-latency communication (URLLC) services as required for 5G networks. Optical technologies complemented with wireless networks can meet these requirements. Depending on the operator's goals, a suitable optical technology (for transport and access network) will be chosen to meet the incoming demands (as shown in Fig. [2\)](#page-2-0). Dense wavelength division multiplexing (DWDM) network could be exploited for transmission over long distances providing high capacities. On the other side, 5G fronthaul/backhaul could be realized with optical access networks such as PON (Passive Optical Networks) as the last mile between users and providers or with P2P (point-to-point) [[8](#page-6-0)].

The data layer supports data organizing, analyzing, filtering, storing and decision-making tasks. The efficiency of this layer is tightly important for a smart city deployment

![](_page_1_Figure_16.jpeg)

Fig. 1 Smart city communication architecture (adapted from [\[7\]](#page-6-0))

![](_page_1_Picture_18.jpeg)

<span id="page-2-0"></span>![](_page_2_Figure_2.jpeg)

Fig. 2 The basis of smart city communication transport and access network architecture (adapted from [[9\]](#page-6-0))

and that is why many techniques are used to enhance data processing [\[10](#page-6-0)].

The application layer consists of numerous IoT applications such as the smart transportation, smart energy, smart healthcare, smart governance, etc. and it directly interacts with citizens.

## 3 Data synthesis

In this section, the designated research questions will be answered.

## 3.1 What are the requirements of 5G wireless on optical networking?

5G network deployment necessary for many IoT applications and future smart infrastructures comprise the fullfilment of rigid requirements considering the latency, bandwidth, massive device connectivity and extremely high quality of experience (QoE) [\[11–15](#page-6-0)].

The ever increasing user requirements for advanced service applications cause the exponential growth of traffic volume. Compared to 4G wireless networks, traffic volume is expected to be significantly larger since the number of connected devices that generate traffic will be more than 100 times higher.

5G networks should support end-user data rates up to 10 Gb/s what is 10 to 100 times higher than in 4G [\[15](#page-6-0)]. Time-critical applications are increasing due to digitalization and urbanization. Some applications such as transportation and traffic safety or health care have highly critical latency. Various requirements for 5G services are summarized in [\[15](#page-6-0)]. Based on the application latency, services in 5G networks require an E2E (end-to-end) delay of a few milliseconds and for time-critical applications less than 1 ms [[15,](#page-6-0) [16](#page-6-0)]. As a result, the stringent goals of 5G smart cities cannot be realized without fibers.

The increase of traffic volume increases the energy consumption, too. When analyzing the energy consumption, all the smart city components have to be considered such as the sensing elements, devices for data transmission, networking devices as well as data storages. The major goal is to minimize the energy consumption and make the network devices with long battery life. Smart city communication architecture requires low-cost equipment that will deliver the traffic with the same or lower energy consumption than 4G. The study in [\[17](#page-6-0)] investigated the radio access network architecture under different levels of centralization of the baseband functions, resulting in different levels of power consumption.

High spectral efficiency is expected to be an imperative task in 5G networks, at least three times higher compared to 4G networks. Although there is a much wider availlable spectrum range in the optical domain, it is still necessary to be used as efficiently as possible in order to provide enough capacities for huge traffic volumes. Some spectrum management techniques for optical networks have been analyzed in [[18\]](#page-6-0).

## 3.2 What are the available and emerging optical technologies supporting 5G wireless?

The increasing number of connected devices which causes the exponential growth of traffic volume, the development of machine-to-machine communications and 5G network densification (increase in the number of 5G cells) as smart infrastructure are the main drivers for the progress and fast

![](_page_2_Picture_17.jpeg)

implementation of advanced optical network technologies [\[19](#page-6-0), [20\]](#page-6-0). 5G densification required for the smart city applications means shorter range, but more cells to ensure coverage. The transport network of current 4G/LTE (Long Term Evolution) consists of two parts: fronthaul and backhaul. Mobile fronthaul connects baseband units (BBUs) with remote radio heads (RRHs) while the core network is connected with BBUs by mobile backhaul. Migration to 5G leads to cloud-based RAN (C-RAN) architecture. C-RAN differs from traditional distributed RAN (D-RAN) because the BBUs are centralized at the central office so that the resources can be shared among multiple cells. In order to support mobile fronthaul and backhaul and the cloud infrastructures, optical technologies will play an essential role.

P2P (point-to-point) technology supports bidirectional transmission with one or two fibers for distances mostly shorter than 20 km [\[8](#page-6-0)]. Transmission distance affects the latency and more resources such as fibers or power elements are needed. In such a way, traffic requirements imposed by 5G wireless networks cannot be served.

Compared to P2P, PON is a technology where one signal source is used to connect many devices or point-tomultipoint. It is ideal for smart cities because of its connectivity and it reduces the amount of fiber and the equipment. Better use of fibers is achieved with the advantages of fiber sharing and split ratios up to 1:256. As fiber replaces copper, PON is setting the basis for the Internet of Things. The major parts of PON technology are optical line terminal (OLT), Optical Distribution Network (ODN) and Optical Network Units (ONU). Standards for PON architectures are developed by the Institute of Electrical and Electronics Engineers (IEEE) and the Telecommunication Standardization Sector of the International Telecommunication Union (ITU-T). The standardization of some latest generations of PON technologies by the ITU-T and IEEE is shown in Table 1 [\[3](#page-6-0)].

The innovations in PON generations or updated standards, such as XGS-PON (10 Gigabit Symmetrical PON) or NG-PON2 (next generation PON2) are following the growing demands and are in focus of interest of various providers. The ''X'' in XGS represents the number 10, and the ''S'' means symmetrical. Further development of 5G

Table 1 Available (after 2010 year) and future PON standards [[3\]](#page-6-0)

| Name         | Standard       | Data rates      |                   |
|--------------|----------------|-----------------|-------------------|
|              |                | Upstream (Gb/s) | Downstream (Gb/s) |
| NG-PON2      | ITU-T G.989.x  | 10              | 10/2.5            |
| XGS-PON      | ITU-T G.9807.1 | 10              | 10                |
| NG-PON2 Amd1 | ITU-T G.989.x  | 10              | 10                |
| NG-EPON      | IEEE 802.3ca   | 25              | 25                |
| G.hsp.x      | ITU-T SG15     | 50              | 50                |

wireless networks where latency and bandwidth are essentially considered will be supported with one of the emerging PON technologies that offer up to 100 Gb/s: high-speed TDM-PON (Time Division Multiplexing PON), WDM-PON (Wavelength Division Multiplexing PON), OCDM-PON (Optical Code Division Multiplexing PON), OFDM-PON (Orthogonal Frequency Division Multiplexing PON) and hybrid technologies [[21\]](#page-6-0). We will make here a review of some pure technologies depending on the techniques employed to enhance capacity and fiber efficiency.

#### 3.2.1 TDM-PON

In TDM-PON technology, the same bandwidth is shared among multiple users, but using the same wavelength. A specified time is assigned to every ONU by OLT to control upstream transmissions [\[21](#page-6-0)]. TDM-PON has been widely deployed because of its cost advantage. Because of shared infrastructure, it is not secured enough. Also, efforts on emerging TDM-PON are made to latency reduction [\[22](#page-7-0), [23](#page-7-0)]. The standard TDM-PON with dynamic bandwidth allocation (DBA) has greater latency. Time taken to process the DBA in the OLT or the grant processing time increases the latency. Since the DBA method directly affects processing time it is important to avoid the complex methods. For this purpose, a low latency DBA method to reduce the DBA cycle or latency as well as to improve bandwidth efficiency has been proposed in [[23\]](#page-7-0) where DBA cycle length depends on traffic load.

### 3.2.2 WDM-PON

For WDM-PON, a specific wavelength is assigned to each ONU for transmission. The wavelengths can be selected with passive wavelength splitters (in ODN) or with wavelength filters (in ONUs) [[8\]](#page-6-0). In such transmission, shared fiber infrastructure is used for multiple wavelengths providing high capacity, fiber savings and simple network management. This makes power insertion loss smaller. These features make the technology suitable for 5G fronthaul. In order to fulfill 5G densification, each wavelength is required 25 Gb/s and above. For this purpose, colorless

![](_page_3_Picture_13.jpeg)

ONUs using tunable transponders technology will be applied. WDM-PON is divided into DWDM and CWDM (Coarse WDM), depending on the available wavelengths. Various approaches for implementation in WDM-PON are analyzed in [\[21](#page-6-0)] such as externally seeded WDM-PON, tunable WDM-PON, wavelength re-use WDM-PON etc. So, considering WDM-PON in a new generation of highspeed PON requires research on the tunable transceivers.

### 3.2.3 OCDM-PON

Two main categories of OCDM are coherent and incoherent systems or bipolar and unipolar approach for implementation, respectively. Besides transponders, encoders and decoders are needed. The encoding could be onedimensional with the time or wavelength domain or twodimensional, as a combination of domains [\[21](#page-6-0)]. Types of OCDM codes with advantages of three-dimensional code are presented in [\[24](#page-7-0)]. Using OCDM technology, network security and efficient use of bandwidth could be achieved what is required for 5G communications.

#### 3.2.4 OFDM-PON

OFDM uses a number of orthogonal subcarriers with small spacing to carry traffic.

The subcarriers are orthogonal and for downstream and upstream two different wavelengths are used [[25\]](#page-7-0). This technology enables the flexibility in spectrum allocation because the total bandwidth is divided on subcarriers or slots. Because there is no overlapping due to orthogonality in OFDM, there is no interference. Also, the technology allows some spectrum engineering techniques to be applied such as traffic grooming at the optical level. Optical connections of small size are grouped and generated with one transmitter without guard bands. The disadvantage of OFDM could be a frequency offset due to carrier frequencies mismatch [\[26](#page-7-0)].

It should be mentioned that the advantages of WDM-PON and TDM-PON can be jointly exploited and the result is hybrid TWDM-PON architecture as well as some hybrid architectures such as XDM/WDM, XDM/TDM, XDM/ TDM/WDM [\[8](#page-6-0), [21,](#page-6-0) [26\]](#page-7-0).

## 3.3 What are the benefits of flexibility in optical networking supporting 5G communication infrastructure?

The main drawback of today's WDM/DWDM technology is the fixed spectrum allocation or fixed grid technology. One of the first steps towards emerging optical infrastructures is to make fixed grid a flexible. It means migration to flexible EON (Elastic Optical Network) infrastructures. Fixed grid refers to equal channel spacing and spectrum allocation to a demand, without considering its capacity. That is why a part of the spectrum has been always wasted. If a communication network is adaptable to some traffic or network conditions (such as spacing between channels or types of modulation), then it has the flexibility property [\[27](#page-7-0)]. The flexibility property has been standardized by updating ITU Recommendation G. 694.1 [[28\]](#page-7-0), where the DWDM fixed grid of 50 GHz and 100 GHz has been reduced to 25 GHz, 12.5 GHz or even 6.25 GHz. Spectrum savings with such allocation are shown in Fig. [3.](#page-5-0) Figure [3](#page-5-0)(b) shows much finer spectrum granularity than a fixed ITU-T grid (3a). The whole spectrum is discretized into units called frequency slots or slices. In this way, elastic optical paths are formed using just enough spectrum. So, the role of flexibility is more efficient spectrum utilization and to cope with growing traffic demands. Such a network is called a flexible or elastic network. Elasticity could be the basis for a lot of spectrum engineering techniques such as optical grooming [\[18](#page-6-0)]. Some benefits of network flexibility in optical domain for 5G communication infrastructure are shown in Table [2.](#page-5-0)

Elastic optical networking is possible with hardware elements such as sliceable bandwidth variable transponders (SBVT) capable of adapting to the modulation format and central frequency of the incoming signal, and reconfigurable optical add-drop multiplexers (ROADM) used for switching along the path. SBVT can form elastic optical paths that consist of several groomed connections or optical paths with different spectral widths. In such a way, the right amout of resources such as spectrum or transponders is used.

## 3.4 What are the research challenges on network flexibility implementation?

In order to provide higher capacity and a huge number of connections for a smart city, a network provider is subject to higher Capex and Opex. To be competitive in such an environment, solutions that minimize infrastructure costs should be found. Since the elastic optical network technology is yet in the development phase, a lot of research challenges should be addressed.

Dynamic lightpath establishing in the C-RAN deployment is one of the challenges. Therefore, suitable algorithms for routing and spectrum allocation (RSA) while satisfying latency or energy consumption should be proposed.

The second challenge is development of models to predict traffic variations [[29\]](#page-7-0). Since mobile traffic demands have complex and uncertain nature, machine learning techniques could be applied to capture parameters such as location, time, etc. The predicted demands allow the

![](_page_4_Picture_17.jpeg)

<span id="page-5-0"></span>Fig. 3 Spectrum allocation: a fixed grid and b flexible grid [[28](#page-7-0)]

![](_page_5_Figure_3.jpeg)

Table 2 Benefits of flexible grid vs fixed grid

| Fixed grid                             | Flexible grid (EON)                                                     | Benefits of EON for smart city                                                                                                                                                            |
|----------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Spectral width fixed<br>per wavelength | Spectral width adjustable according to<br>the number of frequency slots | Spectrum savings, more services realized                                                                                                                                                  |
| Fixed number of<br>channels            | Variable                                                                | Different services could be realized                                                                                                                                                      |
| One type of<br>modulation              | Different types of modulation                                           | Spectral efficiency through longer and shorter distances                                                                                                                                  |
| Bandwidth fixed<br>transponders        | Bandwidth variable transponders                                         | Spectral and energy efficiency                                                                                                                                                            |
| Electrical traffic<br>grooming         | Optical traffic grooming                                                | Spectrum savings are achieved by eliminating the guard bands, the number of<br>O/E/O conversions is minimized, the latency is minimized, the number of<br>optical transponders is reduced |

allocation of just enough spectrum and transponders resources. Therefore, predictive models suited for EONs are under investigation.

The consequence of satisfying routing and spectrum allocation constraints is spectrum fragmentation. A smart city implies a very dynamic traffic environment with traffic demands ranging from low to high bandwidth. If there is not enough available spectrum when a new demand arrives, it is blocked. Fragmentation could be solved with some proactive or reactive approaches [\[29](#page-7-0)].

Survivability techniques are another challenge in elastic optical networking. Failure in an optical fiber or sliceable transponder could have a huge effect on the end-user and loss of data. Survivability techniques are related to protection and restoration schemes. In the concept of 5G networks, QoS requirements are also considered and different levels of protection are applied (lightpaths with higher reliability and best effort lightpaths).

The energy issue is also important in smart city environment because densification of cells will increase the energy consumption. The energy consumption could be reduced with O/E/O (Optical/Electrical/Optical) conversion eliminations at transit nodes and using sliceable transponders instead of several transponders. When traffic is close to a certain threshold, some devices or small antennas could be put into sleep mode to avoid energy consumption.

At the last, design of the advanced control plane to support emerging smart city applications is required. This will imply SDN (Software Defined Networking) principles

![](_page_5_Picture_12.jpeg)

<span id="page-6-0"></span>to be employed. The control plane will enable data transmission across different domains. The design of a control plane and extensions for elastic optical networks are discussed in [\[30](#page-7-0)].

## 4 Conclusion

Optical technologies suitable to meet the 5G wireless demands in fortcoming smart cities are researched in this paper. The paper begins with an overview of the basic communication architecture of a 5G-based smart city concept. 5G densification and reliable communication infrastructure that is the basis for transforming cities into the smart cities requires a lot of optical networking isuses to be researched. Besides the core networks, communication demands imposed by 5G wireless, such as high capacity, low latency and low cost, trigger the optical access networks to be improved. PON technologies are potential candidates for the design of 5G fronthaul/backhaul because of shared spectrum, its point-to-multipoint architecture and innovation progress. Innovative PON technologies are targeting to a single wavelength data rate at 100 Gb/s and above. To achieve such goals, new modulation formats are investigated, reducing latency in TDM-PON as well as tunable transponders technology in WDM-PON. It is clear that coordination between C-RAN deployment and PON is needed. Migration to flexible optical grids will be indispensable in order to provide large-capacity, reliable, low-latency and high-efficiencycommunication infrastructure for a huge number of devices in the future smart cities.

## References

- 1. Kondepudi, S. N., Ramanarayanan, V., Jain, A., Singh, G. N., Agarwal, N. K. N., Kumar, R., Singh, R., Bergmark, P., Hashitani T., Gemma P., Sang, Z., Torres, D., Ospina, A., & Menon, M. (2014). A smart sustainable cities: An analysis of definitions. Technical report. ITU-T. Retrieved November 25th, 2020, from [https://www.itu.int/en/ITU-T/focusgroups/ssc/Pages/default.aspx.](https://www.itu.int/en/ITU-T/focusgroups/ssc/Pages/default.aspx)
- 2. Silva, B. N., Khan, M., & Han, K. (2018). Towards sustainable smart cities: A review of trends, architectures, components, and open challenges in smart cities. Sustainable Cities and Society, 38, 697–713.
- 3. Aleksic, S. (2019). A survey on optical technologies for IoT, smart industry, and smart infrastructures. Journal of Sensor and Actuator Networks, 8(47), 1–18.
- 4. Miladic´-Tesˇic´, S., & Markovic´, G. (2020). Development of optical networking for 5G smart infrastructures. In 5th EAI international conference on management of manufacturing systems. Springer. [https://www.springer.com/gp/book/](https://www.springer.com/gp/book/9783030672409#aboutBook) [9783030672409#aboutBook](https://www.springer.com/gp/book/9783030672409#aboutBook) (in Press).

- 5. Miladic´-Tesˇic´, S., Markovic´, G., & Nonkovic´, N. (2020). Optical technologies in support of the smart city concept. Tehnika, 67(2), 209–215.
- 6. ITU-T. (2012). Overview of the Internet of Things. Recommendation Y. 2060. ITU. Retrieved December 15th, 2020, from <https://www.itu.int/rec/T-REC-Y.2060-201206-I>.
- 7. Ortiz, R., Narvaez, W., Azurza, W., Sang, Z., Gemma, P., & Anthopoulos, L. (2015). Overview of smart sustainable cities architecture. Technical report. ITU-T. Retrieved December 30th, 2020, from [https://www.itu.int/en/ITU-T/focusgroups/ssc/Pages/](https://www.itu.int/en/ITU-T/focusgroups/ssc/Pages/default.aspx) [default.aspx](https://www.itu.int/en/ITU-T/focusgroups/ssc/Pages/default.aspx).
- 8. Wey, J. S., & Zhang, J. (2018). Passive optical network for 5G transport: Technology and standards. Journal of Lightway Technology, 37(12), 2830–2837.
- 9. Doo, K.-H., Kim, K., Lee, H. H., Kim, S. H., & Park, H. (2019). Optical access and transport technologies for 5G and beyond. In 24th OptoElectronics and communications conference (OECC) and 2019 international conference on photonics in switching and computing (PSC) (pp. S1–S3). IEEE.
- 10. Silva, B. N., Khan, M., & Han, K. (2017). Big data analytics embedded smart city architecture for performance enhancement through real-time data processing and decision-making. Wireless Communication and Mobile computing, 2017, 1–12.
- 11. Shafi, M., Molisch, A. F., Smith, P. J., Haustein, T., Zhu, P., De Silva, P., Tufvesson, F., Benjebbour, A., & Wunder, G. (2017). 5G: A tutorial overview of standards, trials, challenges, deployment, and practice. IEEE Journal on Selected Areas in Communications, 35(6), 1201–1221.
- 12. Jaber, M., Ali Imran, M., Tafazolli, R., & Tukmanov, A. (2016). 5G backhaul challenges and emerging research directions: A survey. IEEE Access, 4, 1743–1766.
- 13. Ijaz, A., Zhang, L., Grau, M., Mohamed, A., Vural, S., Quddus, A. U., Imran, M. A., Foh, C. H., & Tafazolli, R. (2016). Enabling massive IoT in 5G and beyond systems: PHY radio frame design considerations. IEEE Access, 4, 3322–3339.
- 14. Liu, X., & Effenberger, F. (2016). Emerging optical acces network technologies for 5G wireless [Invited]. Journal of Optical Communication and Networking, 8(12), B70–B79.
- 15. Parvez, I., Rahmati, A., Guvenc, I., Sarwat, A. I., & Dai, H. (2018). A survey on low latency towards 5G: RAN, core network and caching solutions. IEEE Communications Surveys & Tutorials, 20(4), 3098–3130.
- 16. Iovanna, P., Bottari, G., Ponzini, F., & Contreras, L. M. (2018). Latency-driven transport for 5G. Journal of Optical Communications and Networking, 10(8), 695–702.
- 17. Fiorani, M., Tombaz, S., Ma˚rtensson, J., Skubic, B., Wosinska, L., & Monti, P. (2016). Modeling energy performance of C-RAN with optical transport in 5G network scenarios. Journal of Optical Communications and Networking, 8(11), B21–B34.
- 18. Talebi, S., Alam, F., Katib, I., Khamis, M., Salama, R., & Rouskas, G. N. (2014). Spectrum management techniques for elastic optical networks: A survey. Optical Switching and Networking, 13, 34–48.
- 19. Chowdhury, M. Z., Shahjalah, M., Hasan, M. K., & Jang, Y. M. (2019). The role of optical wireless communication in 5G/6G and IoT solutions: Prospects, directions and challenges. Applied Sciences, 9(20), 4367.
- 20. Alimi, I. A., Tavares, A., Pinho, C., Abdalla, A. M., Monteiro, P. P., & Teixeira, A. L. (2019). Enabling optical wired and wireless technologies for 5G and beyond networks. In I. A. Alimi, P. P. Monteiro, & A. L. Teixeira (Eds.), Telecommunication systems-principles and applications of wireless-optical technologies. IntechOpen.
- 21. Abbas, H. S., & Gregory, M. A. (2016). The next generation of passive optical networks: A review. Journal of Network and Computing Applications, 67, 53–74.

![](_page_6_Picture_27.jpeg)

- <span id="page-7-0"></span>22. Houtsma, V., & Van Veen, D. (2018). Bi-directional 25G/50G TDM-PON with extended power budget using 25G APD and coherent detection. Journal of Lightwave Technology, 36(1), 122–127.
- 23. Hatta, S., Tanaka, N., & Sakamoto, T. (2017). Low latency dynamic bandwidth allocation method with high bandwidth efficiency for TDM-PON. Ntt Technical Review, 15(4), 1–7.
- 24. Yen, C.-T., & Chen, C.-M. (2015). A study of three-dimensional optical code-division multipleaccess for optical fiber sensor networks. Computers and Electrical Engineering, 49, 136–145.
- 25. Shaddad, R. Q., Mohammad, A. B., Al-Gailani, S. A., Al-hetar, A. M., & Elmagzoub, M. A. (2014). A survey on access technologies for broadband optical and wireless networks. Journal of Network and Computer Applications, 41, 459–472.
- 26. Bindhaiq, S., Supa, A. S. M., Zulkifli, N., Mohammad, A. B., Shaddad, R. Q., Elmagzoub, M. A., & Faisal, A. (2015). Recent development on time and wavelength-division multiplexed passive optical network (TWDM-PON) for next-generation passive optical network stage 2 (NG-PON2). Optical Switching and Networking, 15, 53–66.
- 27. Peters, A., Hugues-Salas, E., Gunkel, M., & Zervas, G. (2017). Key performance indicators for elastic optical transponders and ROADMs: The role of flexibility. Optical Switching and Networking, 25, 1–12.
- 28. ITU-T. (2012). Spectral grids for WDM applications: DWDM frequency grid. v2.0. Recommendation G.694.1. ITU. Retrieved December 15th, 2020, from [https://www.itu.int/rec/T-REC-G.](https://www.itu.int/rec/T-REC-G.694.1/en) [694.1/en](https://www.itu.int/rec/T-REC-G.694.1/en).
- 29. Boutaba, R., Shahriar, N., & Fathi, S. (2017). Elastic optical networking for 5G transport. Journal of Network and System Management, 25(4), 819–847.
- 30. So´crates-Dantas, J., Careglio, D., Perello´, J., Silveira, R. M., Ruggiero, W. V., & Sole`-Pareta, J. (2014). Challenges and requirements of a control plane for elastic optical networks. Computer Networks, 72, 156–171.

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](_page_7_Picture_12.jpeg)

Suzana Miladic´-Tesˇic´ received her Ph.D degree in telecommunication traffic and networks engineering from the University of Belgrade—Faculty of Transport and Traffic Engineering, Serbia, in 2020. She started her academic career at University of East Sarajevo, Bosnia and Herzegovina, in 2012 where she currently works with the Faculty of Transport and Traffic Engineering. She is an IEEE member. Her research interest include optical networking,

traffic and network engineering, optical technologies supporting 5G, smart mobility, smart cities. She has published more than 30 papers in journals and refered international and national conferences and was included in several projects supported by Ministry of Science and Technology. She has been invited as a reviewer in several international journals.

![](_page_7_Picture_15.jpeg)

Goran Markovic´ received his B.Sc., M.Sc., and Ph.D. degrees, all in telecommunication traffic and networks engineering from the University of Belgrade, Serbia. Since 1997, he has been employed at the University of Belgrade—Faculty of Transport and Traffic Engineering, where he is currently a Full Professor and holds the position of Head of Department for Telecommunication Traffic and Networks. His research interests include routing in communication net-

works, optical networking, design and optimization of telecommunication networks, intelligent traffic systems etc. He has participated in several scientific and research projects and published nearly 140 scientific papers in international or national journals and conference proceedings. He is also the author or coauthor of several university textbooks and monograph chapters. He has been invited as a reviewer in several international SCI journals and has been a member of editorial board and program committee of international and national scientific conferences.

![](_page_7_Picture_18.jpeg)

Dragan Perakovic´ received his Master's and Ph.D. degrees in the field of technical sciences from the Faculty of Transport and Traffic Sciences (FPZ) at the University of Zagreb. After graduation, he began his career at the FPZ, where he is currently working as a Full Professor and holds the positions of Head of Department for Information and Communication Traffic and Head of Chair of Information and Communication Systems and Services Management. He

has engaged in several international scientific projects and R&D studies as a researcher, leading researcher, and evaluator. Also, he is an author or co-author of more than 140 scientific papers and a member, board member, and official editor of several journals and conferences in his research field. His current research interest is in security, digital forensic, innovative communication services in the transport system, smart city, industry 4.0.

![](_page_7_Picture_21.jpeg)

Ivan Cvitic´ received his Master's degree from the Faculty of Transport and Traffic Sciences at the University of Zagreb in 2013. A Ph.D. degree in the field of technical sciences he received at the same institution in 2020. Currently, he is with the Faculty of Transport and Traffic Sciences as a Postdoctoral Researcher and as an Associate in the Laboratory for Security and Forensic Analysis of Information and Communication System. He has published

more than 40 scientific papers at international conferences, scientific books, and highly rated journals. He is a member of the editorial

![](_page_7_Picture_24.jpeg)

board, reviewer board, and guest editor for several highly rated scientific journals and international conferences. His research domain and interests are in cybersecurity, applied machine learning and

artificial intelligence methods, modeling network traffic anomalies, DDoS, Internet of Things, digital forensics, communication networks.

![](_page_8_Picture_4.jpeg)
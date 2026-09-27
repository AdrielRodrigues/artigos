---
title: "Enabling Optical Network Technologies for 5G and Beyond"
tema_principal: 5g6g
temas_relacionados: []
ano: 2021
autores: []
veiculo: null
pdf: ../pdf/enabling_optical_network_technologies_for_5g_and_beyond.pdf
---

# Enabling Optical Network Technologies for 5G and Beyond

Xiang Liu<sup>®</sup>, Fellow, IEEE, Fellow, OSA

(Invited Paper)

Abstract—We review a series of innovative optical network technologies for 5G and beyond mobile networks, enabling highthroughput mobile any-haul (x-haul) via wavelength-division multiplexing, bandwidth-efficient mobile front-haul via hybrid digital-analog radio-over-fiber, Shannon-limit-approaching longhaul transmission for core networks via advanced coding and probabilistic constellation shaping, low-latency 50-Gb/s passive optical network for cost-effective x-haul traffic aggregation, and service-enabling optical transport network capable of bandwidthguaranteed network slicing with fine granularity. The vision and main application scenarios of the 5th generation fixed network (F5G) are also discussed. With its capability to support enhanced fixed broadband, guaranteed reliable experience, full fiber connection, energy-efficient broadband communication, real-time broadband communication, and harmonized communication and sensing, F5G is well positioned to not only support mobile networks, but also complement them to jointly meet the ever-increasing communication demands in the era of 5G and 6G.

Index Terms—5G, 6G, distributed acoustic sensing, fiber sensing, network slicing, front-haul, optical network, optical transport network, passive optical network, probabilistic constellation shaping, radio-over-fiber.

#### I. INTRODUCTION

PTICAL networks are essential for supporting the fifthgeneration mobile network (5G) by providing connectivity to remote units (RUs), distribute units (DUs), central units (CUs), and the 5G core network (5GC) [1], [2]. In addition, optical networks connect widely deployed data centers, which provide the needed computation and storage functions, as well as content generation and routing functions. 5G represents a significant evolution from the previous generations of mobile networks by meeting the unprecedented communication demands for many use cases under three main application scenarios [3]:

• Enhanced mobile broadband (eMBB), supporting applications such as ultra-high-definition video, 3D video, work and play in the cloud, and augmented reality (AR) and virtual reality (VR).

Manuscript received June 16, 2021; revised July 16, 2021; accepted July 19, 2021. Date of publication July 26, 2021; date of current version January 16, 2022.

The author is with Futurewei Technologies, Bridgewater, NJ 08807 USA (e-mail: xiang.liu@futurewei.com).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/JLT.2021.3099726.

Digital Object Identifier 10.1109/JLT.2021.3099726

- Ultra-reliable and low-latency communications (uRLLC), supporting applications such as self-driving cars and drones, industry automation, remote medical procedures, and other mission critical applications.
- Massive machine type communications (mMTC), supporting applications such as smart home, smart building, smart city and internet of things (IoT).

The 6<sup>th</sup> generation mobile network (6G) is expected to be launched around 2030 [4], [5]. There have been many studies aiming to envision what 6G will be. Among the envisioned enhancements of 6G are continued improvements in downlink and uplink speeds, spectrum efficiency, latency, traffic density, connection density, mobility, and positioning/sensing, to better support existing and new application scenarios. Such 5G and beyond mobile networks bring to modern optical networks new requirements such as high bandwidth, low latency, accurate synchronization, and the ability to perform network slicing [1], [2]. The requirement for high bandwidth is driven by increased RF spectrum bandwidth and the use of massive multiple-input and multiple-output (MIMO) antenna systems, while the requirements for low latency and accurate synchronization are mainly driven by applications such as cloud radio access network (C-RAN) and coordinated multi-point (CoMP). The requirement for network slicing aims to meet the quality of service (QoS) of any given service and do so with the optimized resource utilization. These requirements are being addressed in the so-called 5G-oriented optical networks [1], [2].

In this paper, we review a series of enabling optical network technologies for 5G and beyond mobile networks. This paper is organized as follows. In Section II, we describe optical technologies for mobile front-haul, mid-haul, and backhaul, which are generally referred to as any-haul (x-haul). Particularly, high-throughput wavelength-division multiplexing (WDM) schemes in both the C-band and the O-band [6]-[8], as well as bandwidth-efficient hybrid digital-analog radio-overfiber (DA-RoF) scheme [9], are described. In Section III, we describe advances in high-capacity long-haul transmission for core networks including capacity-approaching forward error correction (FEC) [10]–[15], probabilistic constellation shaping (PCS) [16]-[18], and super C+L band transmission [19]. In Section IV, we describe low-latency 50-Gb/s passive optical network (50G-PON) for cost-effective x-haul network traffic aggregation [20]. In Section V, we describe service-enabling optical transport network (OTN) capable of bandwidth-guaranteed

0733-8724 © 2021 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

![](_page_1_Figure_2.jpeg)

Fig. 1. Illustration of an exemplary metro-area 5G C-RAN with front-haul, mid-haul, back-haul, and data center interconnection (DCI), as well as connection to backbone optical network. MEC: multi-access edge computing; CDN: content delivery network; GW: gateway; UP: user plane; CP: control plane.

network slicing with fine granularity for the aggregation and transport [21]. In Section VI, the vision and main application scenarios of the 5th generation fixed network (F5G) are discussed [22]–[24]. Finally, concluding remarks are given in Section XII.

# II. OPTICAL TECHNOLOGIES FOR 5G X-HAUL

#### *A. Overview of 5G X-Haul*

A common 5G C-RAN consists of front-haul, mid-haul, and back-haul network segments, which are referred to as X-haul network segments. Fig. 1 illustrates an exemplary metro-area 5G C-RAN with the three X-haul network segments connecting RUs with their corresponding DUs, DUs and their corresponding CUs, and CUs and their corresponding 5GCs. According to 3GPP, the one-way latencies for CPRI/eCPRI, uRLLC, eMBB user plane (UP), eMBB control plane (CP), mMTC are typically 100 µs, 0.5 ms, 4 ms, 10 ms, and 10 s, respectively [3]. As shown in Fig. 1, uRLLC, eMBB-UP, eMBB-CP are respectively processed at an access data center (DC), an aggregation DC, and a core DC. With the consideration of the latencies due to fiber propagation and DU/CU processing, as well as the typical metro-area network configurations, the typical distances of front-haul, mid-haul, and back-haul segments are limited to 10 km, 40 km, and 80 km, respectively. In addition, there are usually multiple core DCs that serve one metro-area to provide the needed processing and protection capabilities. The data center interconnection (DCI) distances are usually less than 120 km.

In the first phase 5G deployment in China, approximately 600000 base stations were deployed in 50 major cities by the end of 2020 [25], indicating an average of about 12000 RUs for a typical major city. In an exemplary metro network deployment scenario, 12000 RUs can be supported by 400 DUs if each DU serves 30 RUs [26]. These 400 DUs can then be supported by 20 CUs if each CU serves 20 DUs. Finally, these 20 CUs can be served by four 5GC nodes that reside in four core DCs, each supporting five CUs. The four core DCs are interconnected via a mesh network for low-latency communication and high-reliability protection, as illustrated in Fig. 1. The key 5G

![](_page_1_Picture_9.jpeg)

Fig. 2 Schematic of a WDM-PON based semi-active WDM system for fronthaul with 20 wavelength pairs for end-to-end BiDi transmission.

X-haul network features of the exemplary metro network are listed in Table I.

As shown in Table I, the transmission distance and capacity requirements in the front-haul, mid-haul, back-haul, and 5GC network segments are different. Consequently, different optical technologies in terms of modulation, detection, and multiplexing are needed to optimally support the various segments of 5G C-RAN. We will highlight three mobile front-haul technologies in the following subsections.

#### *B. C-Band WDM Based Front-Haul*

Fig. 2 shows the schematic of a recently demonstrated WDM-PON based "semi-active" WDM system for front-haul with 20 wavelength pairs for end-to-end bidirectional (BiDi) transmission [6]. The term "semi-active" here means that active equipment requiring additional power supplier is needed at the DU/CU sites but not at the RU sites where pluggable optical transceiver modules are inserted directly into the RUs. In this demonstration, the pairing of the downstream and upstream wavelengths follows the ITU G.698.4 recommendation for 100- GHz-spaced dense WDM (DWDM) channels, as shown in Fig. 3. The 20 downstream channels are in the wavelength range from 1529.55 nm (196 THz) to 1544.53 nm (194.1 THz), which pair with the 20 upstream channels that are in the wavelength range from 1550.12 nm (193.4 THz) to 1565.50 nm (191.5 THz),

TABLE I 5G X-HAUL FEATURES IN AN EXEMPLARY METRO NETWORK

| Segment    | Feature                                          | Typical value/scheme                    |  |
|------------|--------------------------------------------------|-----------------------------------------|--|
| Front-haul | Number of RUs <sup>(1)</sup>                     | 12,000                                  |  |
|            | Bit rate to/from DU per RU <sup>(2)</sup>        | 50 Gb/s                                 |  |
|            | Transmission distance                            | <20 km (typically <10 km)               |  |
|            | Typical optical transceiver types                | 25Gb/s NRZ, BiDi, WDM,<br>L-WDM, M-WDM. |  |
|            | Total bit rate to/from DUs                       | 600 Tb/s                                |  |
| Mid-haul   | Number of DUs <sup>(3)</sup>                     | 400                                     |  |
|            | Bit rate to/from CU per DU <sup>(4)</sup>        | 300 Gb/s                                |  |
|            | Transmission distance                            | <80 km (typically <40 km)               |  |
|            | Typical optical transceiver types                | 50-Gb/s PAM4,<br>100-Gb/s coherent, WDM |  |
|            | Total bit rate to/from CUs                       | 120 Tb/s                                |  |
| Back-haul  | Number of CUs <sup>(5)</sup>                     | 20                                      |  |
|            | Bit rate to/from 5GC per CU <sup>(6)</sup>       | 3 Tb/s                                  |  |
|            | Transmission distance                            | <80 km (typically)                      |  |
|            | Typical optical transceiver types                | 200G/400G coherent,<br>DWDM             |  |
|            | Total bit rate to/from 5GCs                      | 60 Tb/s (per direction)                 |  |
| 5G Core    | Number of 5GC nodes <sup>(7)</sup>               | 4                                       |  |
|            | Bit rate from one 5GC to another (8)             | 7.5 Tb/s                                |  |
|            | Transmission distance                            | <120 km (typically)                     |  |
|            | Typical optical transceiver types                | 400G/800G coherent,<br>DWDM             |  |
|            | Total bit rate to/from other 5GCs <sup>(9)</sup> | 45 Tb/s                                 |  |

- (1).Based on recent 5G base station deployment for large cities [25].
- (2).Assuming eCPRI bit rate for a typical 5G RU with 200-MHz bandwidth.
- (3).Assuming that each DU is connected to 10 cell sites each having 3 RUs.
- (4).Assuming a 5-fold reduction in interface bit rate after the DU processing.
- (5).Assuming that each CU is connected to 20 DUs.
- (6).Assuming a 2-fold reduction in outer interface rate after the CU processing.
- (7).Assuming a typical metro network configuration where 5GC nodes are hosted in 4 core DCs.
- (8).Assuming a 2-fold reduction in outer interface rate after 5GC processing.
- (9).Assuming 6 mesh connections for the 4 core DCs.

![](_page_2_Figure_13.jpeg)

Fig. 3. Measured 20 pairs of WDM-PON downstream/upstream wavelengths.

respectively. At the optical line terminal (OLT) side, a cyclic arrayed waveguide grating (AWG) with a free spectral range (FSR) of 2.6 THz is used to multiplex the downstream channels and demultiplex the upstream channels. At the optical network unit (ONU) side, another identical cyclic AWG is used to enable each pair of downstream and upstream channels to coexist in a

![](_page_2_Figure_16.jpeg)

Fig. 4. Channel plans of the 12-channel L-WDM (upper) and the 12-channel M-WDM (lower).

drop fiber that is connected to the intended ONU for end-to-end BiDi transmission. The guard band between the downstream and the upstream channels is 600 GHz (or ∼4.8 nm).

This demonstration also showed the use of WDM-PON to support 5G front-haul with easy management (via embedded control signaling) and high reliability (via the type-B protection) [6]. In 2020, ITU had started the standardization effort on WDM-PON for 5G front-haul applications [20], and more industry-wide developments on the WDM-PON technology can be expected.

#### *C. O-Band WDM Based Front-Haul*

With the evolved common public radio interface (eCPRI), a typical 5G RU site with 3 sectors and 200-MHz RF bandwidth may need twelve 25-Gb/s channels to achieve an aggregated per-fiber capacity of 300 Gb/s for downlink and uplink. There are two promising 12-channel WDM schemes based on LAN-WDM and coarse WDM (CWDM), which are referred to as L-WDM [7] and M-WDM [8], respectively. The 12-channel L-WDM leverages the ecosystem for LAN-WDM and expands the number wavelength channels from eight (in LAN-WDM) to twelve as shown in Fig. 4. The dispersion penalty of 25-Gb/s NRZ with low-cost directly modulated laser (DML) after 10-km standard single-mode fiber (SSMF) transmission in the L-WDM wavelength range between ∼1268 nm and ∼1319 nm can be less than 1 dB [7]. To allow for the end-to-end BiDi transmission, two 1:6 cyclic AWGs can be used at the head end and the tail end such that each pair of BiDi channels can share the same fiber throughout the front-haul link (including the feeder fiber and drop fiber sections). The FSR of each of the 1:6 cyclic AWGs can be set to 4.8 THz, in which case the first six L-WDM channels, Lch1∼Lch6, are paired with the last six channels, Lch7∼Lch12, respectively. To separate each pair of L-WDM BiDi channels in an optical transceiver, an optical circulator can be used. As the optical circulator is usually a broadband device that can operate over the entire O-band, this circulator-based band separation works universally for all the six pairs of BiDi channels.

The 12-channel M-WDM leverages the ecosystem for CWDM and doubles the number wavelength channels to twelve in the wavelength range of the first six CWDM channels, by shifting each CWDM channel by ±3.5 nm, as also shown in Fig. 4. The dispersion penalty of 25-Gb/s NRZ with DML after 10-km SSMF transmission in the M-WDM wavelength range between  $\sim$ 1266 nm and  $\sim$ 1376 nm, which is more than twice that of the L-WDM, can span from -1 dB to 5 dB, so care needs to be taken to mitigate the impact of the dispersion penalty [8].

#### D. CPRI-Compatible DA-RoF

In recent experimental demonstrations of high-speed analog RoF (A-RoF) [9], the best error-vector magnitude (EVM) performance was about 6%, corresponding to an effective signal-to-noise ratio (SNR) of 24.4 dB. This is primarily limited by the effective number of bits (ENOBs) of the high-speed DAC and ADC used, as well as the noise and signal distortion introduced in fiber optical transmission link. To support advanced 5G modulation formats such as OFDM-1024QAM, the EVM of the received wireless signal needs to be less than 2.5%, corresponding to an SNR of higher than 32 dB. To reserve margins for signal distortions occurred outside the fronthaul link, it is desirable for the fronthaul link segment to have an even higher SNR, e.g., 36 dB, corresponding to an EVM of 1.6%. So, it is of value to explore techniques that can substantially improve the SNR, e.g., by over 10 dB.

Phase modulation (PM) has been shown to offer the ability to trade the spectral efficiency (SE) of A-RoF for improved SNR performance [27], [28]. With PM, the SNR increases quadratically with the PM index, i.e., the SNR increases by 6 dB for each doubling of the signal bandwidth or halving of the SE. Such SNR adaptation has been experimentally demonstrated by flexibly adjusting the PM index in the transmitter digital signal processing (DSP), achieving a wide SNR range of between 29 and 62 dB [29].

Recently, it has also been shown that the theoretical SE of digital RoF (e.g., based on CPRI) can approach that of A-RoF when Shannon capacity approaching techniques are applied [30]. In a proof-of-concept experiment, D-RoF was shown to achieve a SNR gain over A-RoF of  $\sim$ 8.2 dB at halved SE and an output EVM of 3.13% for a CPRI-equivalent data rate of about 60 Gb/s [30]. The SNR gain is a few decibels lower than the theoretical gain due to the implementation limitations.

The same concept of trading the transmission SE for the achievable signal fidelity can be applied to DSP-assisted A-RoF. Recently, a novel DA-RoF technique has been proposed and experimentally demonstrated [9]. It is based on cascaded PCS-n-QAM modulation and pulse code modulation (PCM), where the digital PCS-n-QAM signal provides a natural approximation of the RoF waveform and the PCM provides the analog representation of the approximation error with a suitably chosen "magnification" to effectively increase the SNR of the received RoF signal, as shown in Fig. 5.

Fig. 6 shows the experimental setup. The digital part is based on PCS-121-QAM with an entropy of 5.12 bits/symbol. The constellation diagrams of an original/recovered RoF waveform, its digital PCS-121-QAM part, and its analog PCM part are added as insets to illustrate the DA-RoF modulation and demodulation. The recovered DA-RoF signal spectra before and after fiber transmission (with 17 ps/nm dispersion) at -8 dBm

![](_page_3_Figure_9.jpeg)

Fig. 5. Illustration of the CPRI-compatible DA-RoF concept based on cascaded digital PCS-n-QAM modulation and analog PCM.

![](_page_3_Figure_11.jpeg)

Fig. 6. Schematic of the experimental setup for DA-RoF. Insets (a)/(f), (b)/(e), and (c)/(d) are the original/recovered constellation diagrams of the RoF waveform, its digital PCS-121-QAM part, and its analog PCM part, respectively. Inset (g) is the recovered DA-RoF signal spectra before and after the fiber transmission. Insets (h) and (i) are representative recovered constellation diagrams of the 16-QAM CW signal and the OFDM-64-QAM wireless signal, respectively, at  $-8~\mathrm{dBm}$  received optical power.

received optical power (RoP) are shown in inset (g). Representative constellation diagrams of the recovered 16-QAM control word (CW) signal and OFDM-64-QAM wireless signal after fiber transmission are shown in insets (h) and (i), respectively.

Fig. 7 shows the SNR (a) and EVM (b) of the recovered wireless signal as a function of the RoP. At a RoP between -8 dBm and -2 dBm, DA-RoF provides a SNR gain between 10.5 dB and 12.8 dB, respectively. At a RoP between -8 dBm and -2 dBm, the EVM for the DA-RoF case is reduced substantially to 2.28% and 1.38%, respectively. Representative constellation diagrams of the recovered wireless signals with 64-QAM and 1024-QAM subcarrier modulations are shown as insets in Fig. 7 to indicate

![](_page_4_Figure_2.jpeg)

Fig. 7. Experimentally measured SNR (a) and EVM (b) of the recovered wireless signal as a function of the received optical power for both DA-RoF and A-RoF. Insets (i)/(iii) and (ii)/(iv) are representative constellation diagrams for the recovered wireless signals at the received optical powers indicated in (a) via A-RoF and DA-RoF, respectively.

the dramatic performance improvements enabled by DA-RoF. The largest 5G wireless signal constellations applied so far are 256-QAM and 1024-QAM, which require an EVM of below 3.5% and 2.5%, respectively [9]. Thus, the DA-RoF technique enables the support of these large constellations with additional margin for signal distortions outside the fronthaul segment.

It is worth noting that the SNR gain provided by DA-RoF is at the expense of reduced SE. In the case of CPRI-compatible DA-RoF, the CPRI-equivalent data rate for the 8-Gaud signal is 160 Gb/s, which is 62.5% of that of CPRI-compatible A-RoF (256 Gb/s) [31]. In the absence of the CS, the SE of DA-RoF is 50% of that of A-RoF, because each complex sample of an A-RoF waveform is represented by two samples in DA-RoF, one modulated by PCS and the other by PCM. Thus, DA-RoF is capable of achieving a SNR gain over A-RoF of >10 dB at halved SE, which can enable the transmission of high-fidelity wireless signals over links with limited SNRs. As compared to the capacity-approaching D-RoF [30], the DA-RoF shows superior performance and does not require computation-intensive FEC, so energy-efficient and low-latency RoF transmission can be readily supported.

Using 400G-ZR type coherent transceiver with dual-polarization modulation at 64 Gbaud, the CPRI-equivalent bit rate of the DA-RoF scheme can be increased by 16 times

TABLE II High-Performance FEC Codes Recently Demonstrated for 16-QAM Based High-Speed Transmission

| FEC code           | BER <sub>in</sub> for                 | Code rate | NCG      |
|--------------------|---------------------------------------|-----------|----------|
|                    | BER <sub>out</sub> =10 <sup>-15</sup> |           |          |
| CFEC [11]          | 1.22×10 <sup>-2</sup>                 | 0.871     | 10.76 dB |
| CFEC+ [12]         | 1.81×10 <sup>-2</sup>                 | 0.871     | 11.45 dB |
| OFEC [13]          | 1.98×10 <sup>-2</sup>                 | 0.867     | 11.60 dB |
| A 20%-OH LDPC [14] | ~2.76×10 <sup>-2</sup>                | 0.833     | 12.12 dB |
| A 25%-OH LDPC [15] | ~3.45×10 <sup>-2</sup>                | 0.8       | ~12.5 dB |

![](_page_4_Figure_9.jpeg)

Fig. 8. The Shannon limits of HD and SD NCGs for 16-QAM and some recently demonstrated FEC codes with BER $_{\rm out}$  set at  $10^{-15}$ .

to 2.56 Tb/s. Thanks to the advances in the field of digital coherent transceivers, such coherent transceiver can fit into a QSFP-DD format factor with a total power consumption of <15 W [32]. Thus, the DA-RoF technique enables multi-Tb/s CPRI-equivalent bit rate per wavelength in an energy-efficient manner, potentially useful in future 6G mobile network having much more RF bandwidth and massive MIMO elements.

# III. SHANNON-LIMIT-APPROACHING LONG-HAUL TRANSMISSION

#### A. Capacity-approaching FEC

High-capacity long-haul optical fiber transmission is important in forming the global optical network that supports communication services such as 5G and cloud services. FEC is an important technology to enable a communication link to approach the Shannon limit. For high-speed transmission based on 16-QAM, multiple high-performance FEC codes have been studied. Table II shows some of the recently demonstrated FEC codes and their performances. The first code is the CFEC code adopted by the OIF for 400ZR [11]. Its required input bit error ratio (BER<sub>in</sub>) for an output BER (BER<sub>out</sub>) of 10<sup>-15</sup> is  $1.22\times10^{-2}$ , and its code rate is 0.871, leading to a net coding gain (NCG) of 11.76 dB. The second code is an enhanced version of CFEC, named as CFEC+, which offers an increased NCG of 11.45 dB [12]. The third code is referred to as OFEC, which was adopted by the Open ROADM Multi-Source Agreement (MSA) and was proposed by the ITU for 450 km black link applications [13]. The OFEC offers a further increased NCG of 11.6 dB.

Fig. 8 shows the Shannon limits of hard decision (HD) and soft-decision (SD) NCGs for 16-QAM, together with some

recently demonstrated high-performance FEC codes. For HD decoding, the staircase FEC is again only ∼0.6 dB away from the HD Shannon limit. For SD decoding, the CFEC+, OFEC, the 20% overhead (OH) low density parity check (LDPC) [14], and the 25%-OH LDPC [15] described in Table II are all within 1.4 dB from the SD Shannon limit. The above analysis shows the remarkable progresses made in approaching the Shannon limit via advanced FEC coding designs and implementations.

#### *B. Probabilistic Constellation Shaping (PCS)*

To approach the Shannon capacity even closer, signal constellations need to be optimized. For the conventional m-QAM constellations, there is a theoretical performance gap from the Shannon capacity, which can be reduced via constellation shaping [16]–[18]. In the limit of high spectral efficiency (SE), the optical signal-to-noise ratio gain that can be achieved via constellation shaping, or the shaping gain, approaches πe/6 or 1.53 dB. Constellation shaping (CS) can be realized through geometric shaping (GS) or PCS. Aiming to achieve the shaping gain with simple implementations, a new shaping method called probabilistic amplitude shaping (PAS) was introduced in 2014 [16]. The PAS scheme concatenates a distribution matcher (DM) for PCS with a systematic binary encoder for FEC. At the receiver, bit-metric decoding is used without any iterative demapping. This PAS scheme directly applies to two-dimensional QAM constellations by mapping two real-valued M-ary PAM symbols to one complex M2-QAM symbol. The newly developed PAS scheme offers the following advantages:

- -Simple DSP implementation without iterative processes.
- - Compatibility with common QAM constellations. making modulation, gray mapping, equalization and demodulation straightforward.
- - Compatibility with common FEC encoding and decoding processes, enabling the use of already developed highperformance FEC codes.
- - Flexible rate adaptation by changing the distribution of the PAS before FEC encoding.

As the first real-time demonstration of PCS in commercial optical transmission systems, a field trial on the use of PCSprogrammable real-time 200-Gb/s coherent transceivers in a deployed core optical network was reported in 2018, achieving a 2-fold increase in reach when the PCS is activated [18]. PDM-PCS-16QAM real-time coherent transceivers have also been used for 200-Gb/s upgrade of legacy metro/regional WDM networks [15]. While the unshaped 16-QAM allowed error-free transmission of up to 1500 km, the PCS-16QAM extended the reach to 2000 km with additional OSNR margin. The effective OSNR gain of PCS-16QAM over unshaped 16-QAM was found to be about 2 dB [15]. More recently, real-time demonstration of PDM-PCS-64QAM at 800-Gb/s net data rate using 7-nm ASIC has also been reported [14].

# *C. Super C and L Bands*

To increase the transmission capacity per fiber, wider optical amplification bandwidth is desirable. Fig. 9 shows the widened amplification window supported by the super C+L EDFAs. In the super-C band, there is a 6-THz amplification window that can

![](_page_5_Figure_12.jpeg)

Fig. 9. The widened wavelength window enabled by the super C+L EDFAs.

TABLE III KEY CAPABILITIES OF COMMERCIAL HIGH-CAPACITY LONG-HAUL OPTICAL FIBER TRANSMISSION SYSTEMS IN THE EARLY 2020S

| 100/200/400/600/800 Gb/s                                      |  |
|---------------------------------------------------------------|--|
| PDM-BPSK/QSPK/<br>8QAM/16QAM/64QAM                            |  |
| 30 ∼ 100 Gbaud                                                |  |
| 15% ~ 33%                                                     |  |
| PCS with flexible entropy loadings                            |  |
| 50/75/100/125 GHz                                             |  |
| 4.8 THz (Extended C), 6 THz (Super C), and 11 THz (Super C+L) |  |
| 10 Tb/s ~ 88 Tb/s                                             |  |
| 200 km ~ 15,000 km                                            |  |
|                                                               |  |

be used to support 60 100-GHz-spaced DWDM channels, or 120 50-GHz-spaced DWDM channels. In the super-L band, there is a 5-THz amplification window that can be used to support 50 100- GHz-spaced DWDM channels, or 100 50-GHz-spaced DWDM channels. With the use of 800-Gb/s wavelength channels in the super C+L band on a 100-GHz grid, a total single-fiber transmission capacity of 88 Tb/s has been achieved for data center interconnect applications [19].

#### *D. State-of-the-Art Optical Transmission Systems*

The field of high-capacity long-haul optical fiber transmission has witnessed great technical advances in the 5G era, such as flexible PDM-n-QAM modulation, digital coherent detection, digital subcarrier multiplexing [18], fiber nonlinearity mitigation and compensation, capacity-approaching FEC, PCS, improved optical fibers with less nonlinearity and lower loss, and wideband EDFAs to name a few. With these advances, per-fiber capacity has been increased to 88 Tb/s in commercial DCI applications on one hand [19], and over 26 Tb/s in ultra-longhaul transatlantic undersea links [33] on the other hand. Via flexible modulation, coding and shaping, different transmission data rates, capacities and distances can be realized to optimally address the diverse applications of high-capacity and long-haul transmission in metro, regional, national, continental, intercontinental, and trans-oceanic optical networks.

Table III summaries the key capabilities of commercial highcapacity long-haul optical fiber transmission systems in the early 2020s. Going forward, we can expect new innovations to be made to further approach the nonlinear Shannon limit. Better ASIC technologies will help reduce the power consumption per bit further. Higher speed modulation beyond 100 Gbaud will help reduce the cost per bit. Tighter integration between photonics and electronics would help reduce the overall power consumption, size and cost. The superchannel concept can be used to achieve multi-Tb/s throughput per transceiver module, leverage large-scale photonic integration, and increase WDM spectral efficiency.

# IV. LOW-LATENCY 50G-PON

In anticipation of the ever-increasing capacity demand in broadband access, especially in the 5G era, ITU-T established the higher speed passive optical network (HSP) project to define the next generation PON in 2018 [20]. 50-Gb/s PON (50G-PON) has been selected as a primary technology for HSP, which is being standardized as ITU-T G.9804.

Historically, a new generation of PON needs to support the same ODNs used by the previous generations of PON, meaning that 50G-PON needs to achieve similar loss budgets as XG(S)- PON. Theoretically, the receiver sensitivity of a 50-Gb/s signal is 5 times (or 7 dB) worse than a 10-Gb/s signal of the same modulation format, which is non-return-to-zero (NRZ) on-off-keying (OOK). In addition, the dispersion tolerance of a 50-Gb/s signal is 25 times smaller than that of a 10-Gb/s signal of the same modulation format. Thus, new physical layer technologies and system designs are required to enable 50G-PON to be deployable in the same ODNs used by previous generations of PON. The key new physical layer technologies used in 50G-PON include receiver-side DSP-based channel equalization for improved receiver sensitivity and dispersion tolerance, LDPC for achieving higher coding gain than the Reed-Solomon codes used in previous PON generations, low-chirp downstream transmitter for reduced dispersion penalty, and semiconductor optical amplifier for increased downstream transmitter power.

TDM-PON can be used to cost-effectively support certain 5G front-haul, mid-haul and back-haul services. To meet the stringent latency requirements of 5G x-haul, three enabling technologies have been introduced to 50G-PON as follows.

- -Cooperative dynamic bandwidth allocation (CoDBA).
- - Accelerated DBA scheduling with multiple bursts per ONU per 125-μs frame.
- - Elimination of the ranging window by optionally using a dedicated activation wavelength (DAW).

With the CoDBA, the radio access network (RAN) scheduling can be shared with the PON scheduling in advance, so that the upstream traffic from wireless user equipment (UE) can be seamlessly carried over by the TDM-PON system without having to wait for negotiation between the ONU and the OLT, as illustrated in Fig. 10. In effect, CoDBA eliminates the latency associated with the DBA negotiation in PON systems. Along with the ITU-T 50G-PON standardization effort, the OLT capabilities for supporting CoDBA are defined in an ITU-T Supplement [34]. For the specific use case of low-latency mobile front-haul over PON, the cooperative transport interface (CTI) defined by the Open RAN Alliance (O-RAN) can be used for the communication between the PON OLT and the mobile distributed unit [35].

![](_page_6_Picture_11.jpeg)

Fig. 10. Illustration of the use of 50G-PON to support low-latency 5G fronthaul communications via CoDBA.

![](_page_6_Picture_13.jpeg)

Fig. 11. Illustrations of the traditional DBA allowing only one burst per ONU per frame (a) and the low-latency DBA allowing multiple bursts per ONU per frame.

![](_page_6_Figure_15.jpeg)

Fig. 12. Illustration of the use of a dedicated activation wavelength (DAW) to support 50G-PON to achieve uninterrupted low-latency communication for 5G front-haul. CU: centralized unit; DU: distributed unit; RU: remote unit.

With the accelerated DBA scheduling, multiple bursts (or time slots) are allowed to transmit by an ONU during each 125-μs PON frame. For example, when each ONU is allowed to transmit 8 bursts per PON frame, the maximum waiting time is reduced by 8 times from 125 μs to ∼16 μs, as illustrated in Fig. 11. Assuming that the OLT is serving 16 ONUs, each burst can last up to ∼1 μs. To limit the burst-mode overhead time to below 10% of the bust duration, the OLT needs to complete the tracking of each upstream burst within ∼100 ns. This calls for fast burst-mode tracking that includes synchronization and channel equalization for data recovery. DSP-assisted burst-mode receiver is capable of fast burst-mode data recovery with a preamble time of <100 ns. Thus, the accelerated DBA scheduling to further reduce the DBA latency can be readily supported by the DSP technology being adopted in 50G-PON.

With the elimination of the ranging window by a DAW, uninterrupted low-latency communication can be realized. As 50G-PON can co-exist with either GPON or XG(S)-PON, the DAW can be conveniently chosen to be either the GPON upstream wavelength centered at 1310 nm or the XG(S)-PON upstream wavelength centered at 1270 nm. Fig. 12 shows an implementation example where 50G-PON is used for high-speed

![](_page_7_Figure_2.jpeg)

Fig. 13. Aggregation of various services with fine granularity by using OSUflex.

![](_page_7_Figure_4.jpeg)

Fig. 14. Direct support of various types of services using OSUflex in cooperation with OTUk and OTUCn.

low-latency x-haul communications and the DAW is set as the GPON upstream wavelength at 1310 nm. The 50G-PON medium access control (MAC) coordinates with the GPON MAC to discover new ONUs, obtain their serial numbers, and conduct the needed ranging to achieve uninterrupted low-latency communication. The use of the DAW to eliminate the ranging window for low-latency PON has been included as an implementation option in ITU-T G.9804.2 [36].

# V. SERVICE-ORIENTED OTN

To better support diverse client services, OTN has been involving to service-oriented OTN based on optical service units (OSUs) [21]. The smallest optical data unit (ODU) of the traditional OTN is ODU0 with a speed of ∼1.24 Gb/s, which makes it inefficient to carry a client service whose bit rate is less than 1 Gb/s. In OSU-based OTN, a flexible OSU container (OSUflex) is used to provide flexible bandwidth allocation with a fine bandwidth granularity of ∼2 Mb/s, thereby dramatically increasing the OTN bandwidth efficiency for carrying typical client services with bit rates between 2 Mb/s and 500 Mb/s. Note that in OSU-OTN, hitless bandwidth adjustment from 2 Mb/s to 100 Gb/s can be supported with no service interruption [37]. Fig. 13 illustrates the aggregation of various services with fine granularity by using OSUflex, while Fig. 14 shows the implementation of the OSU-based OTN.

In traditional OTN, due to the minimum ODU size of ∼1.24 Gb/s, a 100-Gb/s wavelength channel can only support up to 80 services. In OSU-based OTN, on the other hand, the tributary port number can specify over 1000 OSU containers in a single wavelength. Thus, a 100-Gb/s wavelength channel can support over 1000 client services as long as the aggregated bandwidth of these services is less than 100 Gb/s. Note that the bandwidth resources are allocated to services on demand and can be reconfigured when new services are added, or existing services are completed.

OSU-based OTN supports sequential forwarding to implement the first-in first-out mechanism during centralized crossconnection, thereby greatly reducing the switching latency. In a proof-of-concept demonstration [21], the end-to-end (E2E) latency for a 2-Mb/s service was reduced from 4398 µs using the traditional OTN technology to 1289 µs using the OSU-based OTN technology, representing a remarkable latency reduction of over 70%.

In OSU-based OTN, the OSUflex container supports bandwidth-guaranteed (or hard) network slicing with flexibly adjustable bandwidth, which provides guaranteed service bandwidth that is independent of other services in the same OTN. Network slicing at a fine granularity (of ∼2 Mb/s) also reduces bandwidth resource fragmentation and improves bandwidth utilization efficiency, especially for E2E networking slicing for typical client services whose bit rates are less than 500 Mb/s. Once the E2E network slicing path is established, the E2E latency experienced by a service is fully deterministic.

A key feature of 5G mobile network is the ability to perform E2E network slicing to achieve service-specific optimization in terms of both quality of service (QoS) and resource utilization. With future advances in network orchestration and control, E2E network slicing over both optical access network and OTN can be realized with virtualization and automation capabilities [24].

#### VI. THE VISION OF FIBER-TO-EVERYWHERE

In the 5G era, optical fiber connectivity is expected to play an increasingly important role in supporting broadband access to 5G base stations, homes, offices, business buildings, factories, and smart cities. By the first half of 2019, 570 million fiberto-the-home (FTTH) users have been registered worldwide, according to an Omdia report [38]. It is also estimated that 700 million households will have implemented optical access by 2023. Reaching closer to the end users and devices, optical fiber will realize its full potential to support a fully connected, intelligent world. Fig. 15 illustrates such a fiber-to-everywhere vision in the 5G era. Teaming up with advanced wireless technologies such as Wi-Fi6, the fiber-to-everywhere approach can provide high-bandwidth, high-reliability, low-latency connectivity to people and machines with flexibility and moderate mobility. Similar to mobile networks, fixed networks had entered their 5th generation (F5G) around year 2020. The European Telecommunications Standards Institute (ETSI) has started the definition and specification of F5G since 2020 [22]–[24]. With the fiber-to-everywhere vision, F5G aims to transform how people and machines communicate in the 5G era.

![](_page_8_Figure_2.jpeg)

Fig. 15. Illustration of the F5G vision of fiber-to-everywhere.

F5G [22]–[24] supports three main application scenarios:

- - Enhanced fixed broadband (eFBB), supporting applications that require large bandwidth.
- - Guaranteed reliable experience (GRE), supporting applications that require high reliability.
- - Full fiber connection (FFC), supporting applications that require massive fiber connections.

Looking beyond 5G, F5G is evolving with enhanced technical capabilities and extended application scenarios. The enhanced technical capabilities are witnessed in the emerging technologies described in previous sections. The extended application scenarios can be described as:

- - Energy-Efficient Broadband Communication (EEBC), supporting broadband communication for remote access points, local area networks, metro-access networks, and data center networks via fiber-based energy-efficient solutions.
- - Real-Time Broadband Communication (RTBC), supporting reliable, low-latency, large-bandwidth communication for industrial applications.
- - Harmonized Communication and Sensing (HCS), supporting communication and sensing functions simultaneously for applications such as precise indoor positioning, distributed fiber sensing, monitoring of communication and industrial infrastructures, and environmental monitoring for earthquake and tsunami.

In effect, the three new scenarios, EEBC, RTBC, and HCS, can be regarded as the enhancements of the three original F5G scenarios, with EEBC on the foundation of eFBB and FFC, RTBC on the foundation of GRE and eFBB, and HCS on the foundation of FFC and GRE. Thus, the F5G application space is broadened from the original triangle to a hexagon, as illustrated in Fig. 16.

For EEBC, F5G can leverage the low loss of optical fiber to passively connect the access points of a local area network (LAN), forming the so-called passive optical LAN (POL) for enterprises and campuses [23].

For RTBC, latency-constrained optical network can be used to support high-bandwidth and low-latency communications in the cloud-based industrial applications such as AI-based video analysis and real-time control of actuators/robots [24]. The emerging hollow-core fibers can be used to further reduce the fiber propagation induced latency [39], [40].

![](_page_8_Figure_15.jpeg)

Fig. 16. Illustration of the six application scenarios of F5G and beyond.

For HCS, the optical fiber communication infrastructure itself can provide environmental monitoring. As an example, the polarization change in optical communication traffic was recently used to detect earthquakes and water swells via a 10000 kilometer-long fiber-optic submarine cable, potentially enabling the global submarine fiber-optic cables to effectively serve as continuous real-time earthquake and tsunami observatories [41]. In addition, distributed acoustic sensing (DAS) can be used to provide high-accuracy detection and localization of vibrations in areas with deployed telecommunications optical fiber cables [42], [43]. Moreover, when bi-directional transmission fibers are available, vibration detection and localization can be realized by analyzing the optical phase variations of the bi-directionally transmitted signals themselves [44]–[46]. With the vision of fiber-to-everywhere being gradually materialized, the more and more ubiquitous optical fiber network infrastructure will provide both communication and sensing in a harmonized manner.

# VII. CONCLUSION

We have reviewed a series of innovative optical network technologies for 5G and beyond, enabling high-throughput WDM-based mobile front-haul, bandwidth-efficient DA-RoF, Shannon-limit-approaching long-haul transmission for core networks, low-latency 50G-PON for cost-effective x-haul traffic aggregation, and service-enabling OTN for E2E network slicing. The vision and main application scenarios of F5G are also discussed. With its capabilities in eFBB, GRE, FFC, EEBC, RTBC, and HCS, F5G is well positioned to not only support 5G and beyond mobile networks, but also complement them to jointly meet the communication demands of our society. Consequently, close collaboration between the mobile network community and the fixed network community will continue to be essential to the realization of the vision of a fully connected, intelligent world for the benefit of our global society in the exciting era of 5G and beyond.

### ACKNOWLEDGMENT

The author wishes to thank many colleagues in Futurewei and Huawei for past collaborations, which had resulted in several publications cited in this paper.

# REFERENCES

- [1] X. Liu, "Evolution of fiber-optic transmission and networking toward the 5G era," *iScience*, vol. 22, pp. 489–506, 2019.
- [2] X. Liu and N. Deng, "Emerging optical communication technologies for 5G," in *Chapter 17 of Optical Fiber Telecommunications VII*, ed. by A. Willner, Ed., New York, NY, USA: Academic Press, 2019.
- [3] ITU-T Technical Report, "Transport network support of IMT-2020/5G," [Online]. Available: [https://www.itu.int/pub/T-TUT-HOME-2018,](https://www.itu.int/pub/T-TUT-HOME-2018) 2018
- [4] X. You, C. X. Wang, and J. Huang, "Towards 6G wireless communication networks: Vision, enabling technologies, and new paradigm shifts," *Sci. China Inf. Sci.*, vol. 64, 2021, Art. no. 110301.
- [5] W. Tong and P. Zhu, *6G: The Next Horizon: From Connected People and Things to Connected Intelligence*, Cambridge, U. K.: Cambridge Univ. Press; 1st ed. Jun. 2021.
- [6] X. Wu, D. Zhang, Z. Ye, H. Lin, and X. Liu, "Real-time demonstration of 20×25 Gb/s WDM-PON for 5G fronthaul with embedded OAM and type-B protection," in *Proc. Optoelectron. Commun. Conf.*, 2019, Paper TuA3-2.
- [7] J. Li, "Recent advances in next-generation optical transport networks," in *Proc. Eur. Conf. Opt. Commun. Invited Talk Workshop*, vol. 14, 2020.
- [8] H. Li, "Vision and trend analysis for transport networks in 5G era," in *Proc. Asia Commun. Photon. Conf. (ACP), Plenary Talk*, 2020.
- [9] X. Liu, "Hybrid digital-analog radio-over-fiber (DA-RoF) modulation and demodulation achieving a SNR gain over analog RoF of *>*10 dB at halved spectral efficiency," in *Proc. Opt. Fiber Commun. Conf.*, 2021, Paper Tu5D.4.
- [10] B. P. Smith, A. Farhood, A. Hunt, F. R. Kschischang, and J. Lodge, "Staircase codes: FEC for 100 Gb/s OTN," *J. Lightw. Technol.*, vol. 30, no. 1, pp. 110–117, Jan. 2012.
- [11] R. Nagarajan and I. Lyubomirsky, "Low-complexity DSP for inter-data center optical fiber communications," in *Proc. Eur. Conf. Opt. Commun.*, 2020, Paper SC04.
- [12] Y. Hirbawi, Q. Zhu, and J.-M. Caia, "Continuation & results of FEC proposals evaluation for ITU G.709.3 200-400G 450 km black link," Contribution to the ITU G.709.3, CD11 M10, May 2019.
- [13] J. Roese *et al.*, "Proposal to specify OFEC for FlexO-LR 450 km application," Contribution to the ITU Study Group 15, Q11, SG15-C1345R1, Jul. 2019.
- [14] H. Sun *et al.*, "800G DSP ASIC design using probabilistic shaping and digital sub-carrier multiplexing," *J. Lightw. Technol.*, vol. 38, no. 17, pp. 4744–4756, Sep. 2020.
- [15] Y. Loussouarn and E. Pincemin, "Probabilistic-shaping DP-16QAM CFP-DCO transceiver for 200G upgrade of legacy metro/regional WDM infrastructure," in *Proc. Opt. Fiber Commun. Conf.*, 2020, Paper M2D.2.
- [16] F. Buchali, F. Steiner, G. Böcherer, L. Schmalen, P. Schulte, and W. Idler, "Rate adaptation and reach increase by probabilistically shaped 64-QAM: An experimental demonstration," *J. Lightw. Technol.*, vol. 34, no. 7, pp. 1599–1609, Apr. 2016.
- [17] J. Cho *et al.*, "Trans-Atlantic field trial using high spectral efficiency probabilistically shaped 64-QAM and single-carrier real-time 250-Gb/s 16-QAM," *J. Lightw. Technol.*, vol. 36, no. 1, pp. 103–113, Jan. 2018.
- [18] J. Li *et al.*, "Field trial of probabilistic-shaping-programmable real-time 200-Gb/s coherent transceivers in an intelligent core optical network," in *Proc. Asia Commun. Photon. Conf.*, 2018, PDP Su2C.1.
- [19] [See, for example, \[Online\]. Available: https://www.cio.com/article/](https://www.cio.com/article/3607195/huawei-optixtrans-dc908-ranked-dci-leader-again-by-globaldata.html) 3607195/huawei-optixtrans-dc908-ranked-dci-leader-again-byglobaldata.html
- [20] ITU-T Recommendation G.9804.1, "Higher speed passive optical networks-Requirements," 2019.
- [21] L. Bai, "Optical service unit (OSU)-based next generation optical transport network (NG OTN) technology and verification," in *Proc. MATEC Web Conf.*, 2021, vol. 336, New York: Academic Press, Paper 04014.
- [22] ETSI F5G white paper, "The fifth generation fixed network (F5G): Bringing fibre to everywhere and everything," Sep. 2020.
- [23] ETSI F5G Use Cases Release #1, Feb. 2021; [Online]. Available: [https://www.etsi.org/deliver/etsi\\_gr/F5G/001\\_099/002/01.01.01\\_60/](https://www.etsi.org/deliver/etsi_gr/F5G/001_099/002/01.01.01_60/gr_F5G002v010101p.pdf) gr\_F5G002v010101p.pdf

- [24] [See for example, ETSI ISG-F5G, \[Online\]. Available: https://www.etsi.](https://www.etsi.org/committee/f5g) org/committee/f5g
- [25] [See for example, \[Online\]. Available: https://www.rcrwireless.com/](https://www.rcrwireless.com/20200609/5g/china-end-2020-over-600000-5g-base-stations-report) 20200609/5g/china-end-2020-over-600000-5g-base-stations-report
- [26] China Telecom, "5G-Ready OTN technical white paper," Accessed: [Sep. 2017.\[Online\]. Available: http://www.ngof.net/en/download/5G-](http://www.ngof.net/en/download/5G-Ready_OTN_Technical_White_Paper.pdf)Ready\_OTN\_Technical\_White\_Paper.pdf
- [27] D. Che, F. Yuan, and W. Shieh, "High-fidelity angle-modulated analog optical link," *Opt. Exp.*, vol. 24, pp. 16320–16328, 2016.
- [28] S. Ishimura, H. Kao, K. Tanaka, K. Nishimura, and M. Suzuki, "SSBIfree 1024QAM single-sideband direct-detection transmission using phase modulation for high-quality analog mobile fronthaul," in *Proc. Eur. Conf. Opt. Commun.*, 2019, Paper PD.1.2.
- [29] D. Che, "Digital SNR adaptation of analog radio-over-fiber links carrying up to 1048576-QAM signals," in *Proc. Eur. Conf. Opt. Commun.*, 2020, Paper PDP 2.1.
- [30] H. Ji, C. Sun, and W. Shieh, "Spectral efficiency comparison between analog and digital RoF for mobile fronthaul transmission link," *J. Lightw. Technol.*, vol. 38, no. 20, pp. 5617–5623, 2020.
- [31] X. Liu, H. Zeng, N. Chand, and F. Effenberger, "CPRI-compatible efficient mobile fronthaul transmission via equalized TDMA achieving 256 Gb/s CPRI-equivalent data rate in a single 10-GHz-bandwidth IM-DD channel," in *Proc. Opt. Fiber Commun. Conf.*, 2016, Paper W1H.3.
- [32] Optical Internetworking Forum (OIF), "Implementation agreement [400ZR," \[Online\]. Available: https://www.oiforum.com/wp-content/](https://www.oiforum.com/wp-content/uploads/OIF-400ZR-01.0_reduced2.pdf) uploads/OIF-400ZR-01.0\_reduced2.pdf, Mar. 2020
- [33] S. Grubb *et al.*, "Real-time 16QAM transatlantic record spectral efficiency of 6.21 b/s/Hz enabling 26.2 tbps capacity," in *Proc. Opt. Fiber Commun. Conf.*, 2019, Paper M2E.6.
- [34] ITU-T Work Item G.sup.CoDBA (2017-2020), "OLT capabilities for cooperative DBA,".
- [35] O.-R. A. N. Specification O-RAN.WG4.CTI-TCP.0-v01.00 2020, "Cooperative transport interface transport control plane specification,".
- [36] ITU-T Recommendation G.9804.2 2021, "Higher speed passive optical networks: Common transmission convergence layer specification,".
- [37] [See, for example, \[Online\]. Available: https://networkmatter.com/2020/](https://networkmatter.com/2020/03/11/huaweis-liquid-otn-promises-more-flexible-and-granular-optical-transport/) 03/11/huaweis-liquid-otn-promises-more-flexible-and-granular-opticaltransport/
- [38] Omdia Report, "Global fiber development index analysis 2020," Ac[cessed: Aug. 5, 2021, \[Online\]. Available: https://omdia.tech.informa.](https://omdia.tech.informa.com/OM014270/Global-Fiber-Development-Index-Analysis-2020) com/OM014270/Global-Fiber-Development-Index-Analysis-2020
- [39] B. Zhu *et al.*, "First demonstration of hollow-core-fiber cable for low latency data transmission," in *Proc. Opt. Fiber Commun. Conf.*, 2020, Paper Th4B.3.
- [40] H. Sakr *et al.*, "Hollow core NANFs with five nested tubes and record low loss at 850, 1060, 1300 and 1625nm," in *Proc. Opt. Fiber Commun. Conf.*, 2021, Paper F3A.4.
- [41] Z. Zhan *et al.*, "Optical polarization-based seismic and water wave sensing on transoceanic cables," *Science*, vol. 371, no. 6532, pp. 931–936, 2021.
- [42] G. Wellbrock, "Fiber sensing in existing telecom fiber networks," in *Proc. Opt. Fiber Commun. Conf.*, 2021, Paper Tu6F.1.
- [43] E. Ip *et al.*, "Distributed fiber sensor network using telecom cables as sensing media: Technology advancements and applications," in *Proc. Opt. Fiber Commun. Conf.*, 2021, Paper Tu6F.2.
- [44] G. Marra *et al.*, "Ultrastable laser interferometry for earthquake detection with terrestrial and submarine cables," *Science*, vol. 361, pp. 486–490, 2018.
- [45] Y. Yan, F. N. Khan, B. Zhou, A. P. T. Lau, C. Lu and C. Guo, "Forward transmission based ultra-long distributed vibration sensing with wide frequency response," *J. Lightw. Technol.*, vol. 39, no. 7, pp. 2241–2249, Apr. 2021.
- [46] E. Ip *et al.*, "Field trial of vibration detection and localization using coherent telecom transponders over 380-km link," in *Proc. Opt. Fiber Commun. Conf.*, 2021, Paper F3B.2.

**Xiang Liu** (Fellow, IEEE) received the Ph.D. degree in applied physics from Cornell University, Ithaca, NY, USA, in 2000. He is currently the Vice President of optical transport and access with Futurewei Technologies, Bridgewater, NJ, USA. For 14 years, he was with Bell Labs working on high-speed optical transmission technologies. He has authored more than 350 publications and holds more than 100 US patents. His research interests include optical communication technologies, systems, and networks. He was the General Co-Chair of OFC 2018 and is currently the Deputy Editor of the *Optics Express*. He is a Fellow of the OSA.
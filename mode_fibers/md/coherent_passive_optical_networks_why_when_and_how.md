---
title: "Coherent Passive Optical Networks: Why, When, and How"
tema_principal: mode_fibers
temas_relacionados: []
pdf: ../pdf/coherent_passive_optical_networks_why_when_and_how.pdf
---

# Coherent Passive Optical Networks: Why, When, and How

Md Saifuddin Faruk, Xiang Li, Derek Nesset, Iván N. Cano, Albert Rafel, and Seb J. Savory

While the capacity of the next-generation access network is expected to be 100 Gb/s and beyond, coherent optics is going to be a logical choice for the physical layer as the currently used intensity-modulation/direct-detection technology will fail to meet the required power budget of such high line-rate systems.

## Abstract

While the capacity of the next-generation access network is expected to be 100 Gb/s and beyond, coherent optics is going to be a logical choice for the physical layer as the currently used intensity-modulation/direct-detection technology will fail to meet the required power budget of such high line-rate systems. In this article, we present an overview of necessities, timeframe, and technological challenges for the future passive optical network utilizing coherent technology.

## Introduction

The bandwidth requirement in access networks is increasing tremendously due to advanced services and applications including 5G/6G mobiles, 4K/8K video streaming, cloud computing, and so on. A passive optical network (PON) is a cost-effective approach to deliver the high data rate fiber access service to the user. IEEE recently standardized a 25 Gb/s line-rate PON [1], and the International Telecommunication Union — Telecommunication Standardization Sector (ITU-T) has just standardized a 50 Gb/s line-rate PON [2]. Moving forward, the research for the future generations of PON has already started considering a data rate of 100 Gb/s and beyond [3].

Given the historical timeline of PON standardization, as shown in Fig. 1, at least a four-fold increment in capacity is observed between two adjacent ITU-T PON generations. Considering the same trend, the 200 Gb/s PON is a natural choice for the next generation of fiber access beyond 50G PON. Even though 100 Gb/s PON is also being researched [4], only two-fold increase capacity might not be sufficiently future-proof considering the huge investment by network operators in access deployment.

So far, all standardized PON solutions are based on simple optical intensity modulation (IM) and then a direct-detection (DD) receiver that detects only the power of the incoming optical field. However, such an approach does not seem to be feasible for PON at 100 Gb/s+ due to limited receiver sensitivity. Thus, IM/DD will not meet the required loss budget of the deployed optical distribution networks (ODNs). As an alternative, coherent technology, which enables modulation and detection of amplitude, phase, and polarization of optical signal, is a promising candidate for such high-capacity future access.

To date, all PON systems are fixed rate, but

flexible line-rate might be an interesting feature for future PON. Since each user experiences a different channel due to the point-to-multipoint nature of the PON structure, and there is a variable bandwidth requirement for different use cases, the throughput of each class of user can be optimized by exploiting flexible line-rate. In this article, we focus on the 200 Gb/s line-rate future PON; however, with a flexible modulation format, the proposed transceiver can support lower line-rate such as 100 Gb/s with higher link budget.

In this article, first, we discuss the rationale behind the use of coherent optics for next-generation PON. Then we speculate about the possible coherent PON (Coh-PON) technology development timeframe. Next, a possible system architecture exploiting Coh-PON is presented. After that, the technological challenges and possible solutions of using coherent optics for PON are explicitly discussed. The key challenges considered are the reduction of cost and complexity of the subscriber-side optical network unit (ONU) while ensuring robust detection of burst-mode signals at the optical line terminal (OLT) in the network operator's central office.

## WhyCoherentOptics forPON?

The commonly used DD receiver detects only the intensity of the incoming optical signal. With increasing line-rate, the receiver sensitivity decreases due to more integrated noise within the larger signal bandwidth, and the penalty due to fiber chromatic dispersion also increases, which leads to a very limited power budget.

In a DD receiver, the linear channel impairments convert to nonlinear due to the square-law detection process, which makes it difficult to fully compensate with digital signal processing (DSP). On the other hand, a coherent receiver enables linear conversion of the optical field, facilitating detection of the signal amplitude, phase, and polarization. It offers several key benefits in the PON application.

First, it gives improved receiver sensitivity and thus an adequate power budget with a modest transmitting power. The enhanced sensitivity is achieved through pure amplification of the signal through the local oscillator (LO) power. The increased power budget could extend the reach and/or support a larger number of connected users. Coh-PON is a good fit for both supporting rural areas and reducing the amount of outside

Digital Object Identifier: 10.1109/MCOM.010.2100503

*Md Saifuddin Faruk, Xiang Li, and Seb J. Savory are with the University of Cambridge; Derek Nesset and Iván N. Cano are with Huawei Technologies; Albert Rafel is with BT Applied Research.* plant in urban areas. Furthermore, the data rate requirement of 5G and beyond mobile xHaul could be as large as a few hundred gigabits per second, which is quite challenging for conventional PON. Coherent optics could be a promising solution here.

Second, being a linear receiver, Coh-PON allows the use of advanced multi-level modulation formats by exploiting four degrees of freedom for data transmission (in-phase and quadrature modes in two polarization states), and enables efficient use of DSP algorithms. These in turn allow the use of higher-order modulation formats with lower-bandwidth transceiver components. DSP techniques can further relax the bandwidth requirements of receivers. For example, a digital pre-emphasis at the transmitter can mitigate the penalty due to the limited bandwidth of transceivers. This comes at the expense of additional signal processing and the associated power consumption. The fi ber chromatic dispersion can be fully compensated using DSP, and thus the linear transmission penalty can be neglected. The DSPbased perfect chromatic dispersion compensation also allows operation in the low fi ber attenuation wavelength band (around 1550 nm), giving an extra margin of power budget and easy coexistence with the legacy TDM-PON through wavelength overlay.

Third, coherent detection has inherent frequency selectivity through the choice of LO wavelength. This is particularly advantageous in wavelength-division multiplexing (WDM)-PON, where the channel of interest can be detected without any optical fi lters.

## tIMeLIne for coherent pon

Herein we present a hypothetical timeframe for Coh-PON based on the history of past PON standardization and deployment. It takes five to ten years between two generations of standardized PON systems. Furthermore, typically eight years are needed between deployments of each generation. Therefore, considering the earliest conceivable time interval, the coherent generation of TDM-PON could be standardized by 2026. With two to five years before deployments, following the fi nalization of standards, the operation of Coh-PON might start in 2028. Early applications might be for lower-volume business and services, and then gradually move through medium- to high-volume applications such as 6G xHaul and residential services (e.g., fiber to the home, FTTH), respectively. Considering this scenario, a speculative, and optimistic, timeline for Coh-PON is illustrated in Fig. 2.

## reference ArchItectureof coherent pon

A PON is a point-to-multipoint network in which an OLT at the network operator's central office is connected to many ONUs on the subscriber side through a passive optical distribution network that includes transmission fi ber and one or more optical power splitter stage(s). Typically, there is no in-line amplifi cation, and fi ber is used bidirectionally with different wavelengths employed in each direction. For effi cient sharing of bandwidth resources, three PON structures are considered in standards: time-division multiplexed PON (TDM-PON), WDM-PON, and time- and wave-

![](_page_1_Figure_7.jpeg)

FIGURE 1. The line-rate progression in diff erent PON standards of ITU-T and IEEE.

| 50G PON<br>Standard | 50G PON<br>Deployment | Coh-PON<br>Study Starts<br>in ITU | Coh-PON<br>Standard | Coh-PON<br>Systems<br>Available | Coh-PON<br>for 6G<br>xHaul | Coh-PON in<br>FTTH |
|---------------------|-----------------------|-----------------------------------|---------------------|---------------------------------|----------------------------|--------------------|
| 2021                | 2023+                 | 2024                              | 2026+               | 2028+                           | 2029+                      | 2030+              |

FIGURE 2. Possible PON technology evolution timeline.

length-division multiplexed PON (TWDM-PON) [2]. Among them, due to the highly cost-eff ective approach, TDM-PON is the most widely deployed to date (> 95 percent gigabit-class and 10 gigabit-class PONs). Thus, single wavelength per direction TDM-PON is the main focus of the rest of this article.

A reference architecture for a Coh-PON is shown in Fig. 3. Here, TDM is used in the downstream direction with continuous mode operation and time-division multiple access (TDMA) in the upstream direction with burst-mode operation. On the OLT side, a conventional dual-polarization (DP) coherent transceiver is used, whereas on the ONU side, we propose a simplifi ed coherent receiver and the simplest of amplitude-modulated transmitters, for example, based on an electro-absorption modulated laser (EML). The rationale behind this approach is that the ONU is a more cost-sensitive unit than the OLT as the cost of the latter is shared by all subscribers on the PON.

Since the ODN construction is the major cost portion of a PON deployment, it is desirable that the ODN can be reused for Coh-PON. Therefore, the current loss budgets of legacy PON systems also need to be maintained for Coh-PON. Furthermore, while upgrading to Coh-PON, the already deployed PON technologies are expected to coexist on the same fiber. Therefore, the Coh-PON needs to operate using diff erent wavelengths than does the existing PON technology. It can be seen in Fig. 3 that three possible wavelength windows for Coh-PON in the S, C, and L bands (1500 nm–1524 nm, 1544 nm–1575 nm, and 1581 nm–1596 nm) can be considered. All three of these windows have the benefi ts brought by low fi ber attenuation. The C-band option may be preferable for the ONU because of mature and high-volume optical transmitter component availability. Selecting the S-band for the OLT can ease the separation of the counter-propagating Coh-PON signals and blocking of the coexisting PON signals. A possible wavelength plan for Coh-PON is shown in Fig. 3 with the downstream at 1510 ± 2 nm and upstream at 1560 ± 2 nm. The number of optoelectronic components can be halved by using heterodyne detection and baseband downconversion at the DSP unit (as shown in the inset of Fig. 4). Also, the optical 90° hybrid is replaced by a much simpler 3 dB optical coupler. However, such a simplification comes at the cost of increased receiver bandwidth requirements, at least twice those of intradyne detection.

![](_page_2_Figure_1.jpeg)

FIGURE 3. Schematic reference architecture for a TDM-PON employing coherent technology serving different end-user services. The TDM-PON downstream and upstream data types are illustrated along with a possible transmitter wavelength assignment for the two directions in Coh-PON. (Rx: receiver; Tx: transmitter; BM: burst mode; CM: continuous mode; CEx: coexistence element; US: upstream; DS: downstream; G-: GPON; XG-:XG-PON; TW-: TWDM-PON; Coh-PON: coherent PON).

Note that this proposal also does not overlap with any wavelength used by IEEE PON technology. Additionally, it is assumed that the RF video wavelength (1550 nm-1560 nm) deployed by some network operators will no longer be used as video services move to Internet streaming.

### LOW-COMPLEXITY RECEIVER FOR DOWNSTREAM

A typical DP-coherent intradyne receiver used in core networks comprises two polarization beam splitters (PBSs), four balanced photodiodes, four transimpedance amplifiers (TIAs), and four analog-to-digital converters (ADCs), as shown in Fig. 4 [5]. The complexity, cost, and power consumption of such a receiver are too high for application at the ONU side of a PON. Therefore, at present, the stripped-down coherent receiver approach is an active research topic.

The number of optoelectronic components can be halved by using heterodyne detection and baseband downconversion at the DSP unit (as shown in the inset of Fig. 4). Also, the optical 90° hybrid is replaced by a much simpler 3 dB optical coupler. However, such a simplification comes at the cost of increased receiver bandwidth requirements, at least twice those of intradyne detection.

The receiver can be further simplified by using single-polarization detection and sacrificing spectral efficiency. We can construct a single-polarization heterodyne receiver with only a 3 dB coupler, a single balanced photodiode, and one ADC, as shown in Fig. 4. However, such simplification requires larger bandwidth, higher ADC sampling rate, and more processing power. Also, performance of such a receiver is sensitive to polarization fluctuation of the incoming signal. To make this receiver polarization-insensitive, a polarization diversity technique can be implemented at the OLT transmitter side instead of at the cost-constrained ONU. There are several techniques to achieve this: Alamouti coding in two polarization tributaries, differential group delay (DGD) pre-distortion, and polarization scrambling [6]. Among them, the most robust polarization-insensitive operation can be achieved using the Alamouti coding approach, where the transmitted symbol pairs in two polarization states in a time slot are mutually orthogonal in the next time slot, as shown in the inset of Fig. 4 [7]. It is important to note here that the sensitivity performance of such a simplified receiver is close to that of a typical coherent receiver since there is less insertion loss between LO and photodiodes [8].

Figure 5 shows the simulation results for the power budget at a forward error correction (FEC) bit error rate (BER) limit of 10<sup>-2</sup> as a function of launch power for the three aforementioned coherent receiver configurations considering 200 Gb/s line-rate transmission at 1510 nm with 16-QAM (quadrature amplitude modulation) format and 40 km reach. Thermal and shot noise terms are considered in the receiver (i.e., the dominant sources of noise for unrepeated transmission). At the shot noise limit, with sufficiently high LO power, a similar sensitivity is expected for both DP intradyne and heterodyne receivers with ideal front-end components. However, we consider an LO power of 10 dBm to keep the ONU cost low, and at such a power level, thermal noise contributes considerably. Therefore, the heterodyne receiver has better performance compared to the intradyne one mainly due to having less thermal noise for the reduced number of TIAs. The single-polarization heterodyne receiver has the least thermal noise; however, it provides less power budget than the DP case due to the inherent sensitivity penalty for doubling the symbol rate for the same line-rate. Nevertheless, we can achieve a maximum power budget of 38.05 dB with the simplified heterodyne receiver satisfying the E2 class loss budget (i.e., 35 dB) of ITU-T standards.

There are other simplified coherent architectures available in the literature such as the single-ended DP heterodyne receiver (known as the Glance receiver), and the use of a  $3\times 3$  coupler with intradyne and heterodyne detection [9]. However, considering that the packaging cost of the receiver, including the subsequent ADC, scales with the number of interfaces, the single-polarization heterodyne receiver seems to be the simplest and most cost-effective solution.

![](_page_3_Figure_0.jpeg)

FIGURE 4. The concept of coherent receiver simplification steps. Compared to a DP-intradyne receiver, a DP-heterodyne one replaces 90° optical hybrid with a simpler optical coupler, and other optoelectronic components are halved. Single-polarization realization further reduces half of the components. (LO: local oscillator; PBS: polarization-beam-splitter; BPD: balanced photodiodes; TIA: transimpedance amplifier; ADC: analog-to-digital converter; DSP: digital signal processing; LPF: low pass filter; OC: optical coupler).

The other key challenge of ONU receiver design is to implement a low-complexity DSP algorithm to keep the power consumption down. The sampling rate of ADC is one of the main factors of the power consumption of DSP. However, with sub-Nyquist sampling and advanced DSP, the signal can still be recovered with a reasonably low penalty [10]. As for the DSP algorithm, the adaptive filter for equalization is a power-hungry unit [10]. Its complexity can be reduced in several ways, for example, by implementing it in the frequency domain or hybrid time-frequency domain [5], separating the polarization filter from the static filter [11], and multiplier-free update such as sign-sign constant modulus algorithm [5]. Another challenging DSP block for Coh-PON is the carrier recovery algorithm due to its complexity. Since the ODN reach in PON is typically limited to a couple of tens of kilometers, the polarization mode dispersion (PMD) is expected to be low. Hence, it is possible to estimate the phase noise in one polarization and then use the value for the other polarization channel [11].

With the significant advancement of photonic integration in the last decade, various active and passive optical components now can be integrated in a single device. Thus, it is expected that the coherent module will benefit from this progress to enable a substantial reduction in cost, footprint, and power consumption within the timescale for Coh-PON applications.

#### CHALLENGES FOR COHERENT UPSTREAM

The use of a conventional DP-IQ transmitter at the user end for upstream transmission is cost-prohibitive and a key limitation. The IQ modulator used in such a transmitter requires complex bias control and monitoring. Also, it has a large insertion loss requiring an optical booster amplifier, which is undesirable at the ONU side. In the case of heterodyne detection, the LO can conceivably be shared with the upstream transmitter; however, such an approach makes it challenging to implement a low-cost diplexer. Also, we need a high-power (and thus more costly) LO; otherwise, the ONU receiver sensitivity will degrade significantly due to reduced LO power for sharing with

![](_page_3_Figure_6.jpeg)

FIGURE 5. Power budget at λ = 1510 nm as a function of launch power for different coherent receiver configurations with 200 Gb/s line-rate and 40 km reach. (DP; dual-polarization; SP; single-polarization).

the upstream transmitter. Furthermore, a spectral guard band would be needed between the downstream and upstream, increasing the bandwidth requirement of the ONU receiver. Therefore, one reasonable technology choice is to use a conventional EML or DML to generate IM signals such as binary non-return to zero (NRZ) and pulse amplitude modulation (PAM). At the OLT, a coherent receiver is still necessary to achieve high sensitivity and thus the required link budget.

The main challenge of the OLT coherent receiver is to detect the burst-mode signal effectively. First, the receiver needs to cope with a dynamic range up to 20 dB. Such a wide dynamic range severely degrades the signal-to-noise ratio (SNR) of the received signal due to two factors. The first one is the limited linear region of TIA. If TIA gain is optimized for the weak burst signal, the strong bursts are clipped due to the saturation of TIA degrading its performance. The second issue is the inadequate ADC vertical resolution. If the ADC's full-scale range (FSR) is adjusted to detect strong burst, a weak burst does not use the full vertical resolution and suffers from large quantization noise. To cope with the wide dynamic range, burst-mode optical amplifiers such as burst-mode

The use of a conventional DP-IQ transmitter at the user end for upstream transmission is cost-prohibitive and a key limitation. The IQ modulator used in such a transmitter requires complex bias control and monitoring. Also, it has a large insertion loss requiring an optical booster amplifier, which is undesirable at the ONU side.

In the last decades, coherent technology has been widely deployed in core networks. Recently, its use has been transferred to short-reach applications such as data center interconnect with the introduction of 400G ZR. Still, there are a few key limitations left for its deployment in access such as higher cost, power, and footprint of the coherent module.

![](_page_4_Figure_1.jpeg)

FIGURE 6. Principle of using comb source as LO for the coherent receiver (OA: optical amplifier; LPF: low pass filter).

erbium-doped fiber amplifier (BM-EDFA), burstmode semiconductor optical amplifi er (BM-SOA), or electrical burst-mode TIA can be used [12]. Schemes with such amplifiers usually have two cascaded amplifi er stages with independent automatic gain control (AGC) where the first stage attenuates the strong bursts and the second one sets all the bursts at the same amplitude levels.

Another key challenge is to design a reliable and effi cient, but short, preamble of a burst frame [13]. The incoming upstream signals from different ONUs arrive burst by burst, and typically have diff erent signal powers, state of polarization (SOP), degradation due to fi ber transmission, and timing. The receiver DSP needs to adapt to those changes within the short preamble time. In particular, adaptive equalization has to converge very quickly. This can be achieved by setting initial tap weights with predefi ned values that give relatively good performance for all ONUs, using precalculated equalizer settings for diff erent ONUs in the discovery process and handover, or utilizing a fast converging adaptation algorithm such as the ones based on variable step size techniques.

A further challenge in burst-mode coherent detection is the frequency locking of the LO to the received signals from different ONUs. The laser wavelength of low-cost packaged transmitters like DML or EML at the ONU side may drift even a few nanometers. A promising solution to cope with such wavelength drift is to use a wavelength comb source as the LO [14], as shown in Fig. 6. This approach avoids the need for fast LO tuning and allows the ONU laser to drift within the range of the comb source spectrum. An optical amplifi er may be used with the comb source to increase the power per comb line to operate the receiver near the shot noise limit. The principle of such comb LO-based detection is also depicted in Fig. 6. The channel spacing among the comb lines is chosen approximately equal to the bandwidth of the upstream signal. In the coherent detection process, the signal beats with one of the comb lines. The received signal is then passed through a low pass filter in the digital domain to recover the signal spectrum. It may be noted that a practical and mature comb source device is not yet available for application as the LO of a coherent receiver. Promising approaches using photonic integration will need research and development.

Aside from the TDM/TDMA approach, other multiplexing options have recently been investigated for Coh-PON including digital subcarrier multiplexing (SCM) and TFDM [15].

## concLudInG reMArKs

In the last decades, coherent technology has been widely deployed in core networks. Recently, its use has been transferred to short-reach applications such as data center interconnect with the introduction of 400G ZR. Still, there are a few key limitations left for its deployment in access such as higher cost, power, and footprint of the coherent module. With the advancement of technology, such problems will be solved in the near future by co-design and co-packaging of optics, RF, and DSP ASIC in a pluggable coherent transceiver. Therefore, coherent technology can be a natural choice for next-generation PON-based access networks at 100 Gb/s per wavelength and beyond.

#### references

- [1] IEEE Std 802.3ca-2020, "IEEE Standard for Ethernet Amendment 9: Physical Layer Specifications and Management Parameters for 25 Gb/s and 50 Gb/s Passive Optical Networks," 2020; https://standards.ieee.org/standard/802\_ 3ca-2020.html, accessed June 2, 2021.
- [2] ITU-T Rec. G.9804.1, "Higher Speed Passive Optical Networks: Requirements," 2019; https://www.itu.int/rec/T-REC-G.9804.1-201911-I/en, accessed June 2, 2021.
- [3] J. Zhang *et al*., "200 Gbit/s/ PDM-PAM-4 PON System Based on Intensity Modulation and Coherent Detection," *J. Opt. Commun. Net*., vol. 12, no. 1, Jan. 2020, pp. A1-A8.
- [4] Z. Jia *et al*., "CableLabs Live Webinar: 100G Single-Wavelength PON Project Launch," Live Webinar, Apr. 2021; https://www.cablelabs.com/event/live-webinar-100g-project-launch, accessed June 2, 2021.
- [5] M. S. Faruk and S. J. Savory, "Digital Signal Processing for Coherent Transceivers Employing Multilevel Formats," *J. Lightwave Tech.*, vol. 35, no. 5, 1 Mar., 2017, pp. 1125–41.
- [6] M. S. Faruk and S. J. Savory, "Coherent Access: Status and Opportunities," *Proc. IEEE Photon. Soc. Sum. Topicals Meet*., 2020, paper TuA1.2.
- [7] M. S. Erkılınç *et al*., "Polarization-Insensitive Single-Balanced Photodiode Coherent Receiver for Long-Reach WDM-PONs," *J. Lightwave Tech.*, vol. 34, no. 8, Apr. 2016, pp. 2034–41.
- [8] S. J. Savory, M. S. Faruk, and X. Li, "Low Complexity Coherent for Access Networks," *Proc. Sig. Processing in Photo. Commun.*, 2020, paper SpW1I.3.
- [9] Y. Zhu *et al.*, "Comparative Study of Cost-Eff ective Coherent and Direct Detection Schemes for 100 Gb/s/ PON," *J. Opt. Commun. Net*., vol. 12, no. 9, Sept. 2020, pp. D36–47.
- [10] Z. Jia and L. A. Campos, "Coherent Optics Ready for Prime Time in Short-Haul Networks," *IEEE Network*, vol. 35, no. 2, Mar./Apr. 2021, pp. 8–14.
- [11] K. Matsuda *et al.*, "Hardware-Effi cient Adaptive Equalization and Carrier Phase Recovery for 100-Gb/S/-Based Coherent WDM-PON Systems," *J. Lightwave Tech*., vol. 36, Apr. 2018, pp. 1492–97.
- [12] A. Teixeira *et al*., "DSP Enabled Optical Detection Techniques for PON," *J. Lightwave Tech*., vol. 38, no. 3, Feb. 2020, pp. 684–95.
- [13] J. Zhang *et al*., "Effi cient Preamble Design and Digital Signal Processing in Upstream Burst-Mode Detection of 100G TDM Coherent-PON," *J. Opt. Commun. Net*., vol. 13, no. 2, Feb. 2021, pp. A135–43.
- [14] M. M. H. Adib *et al*., "Colorless Coherent Passive Optical Network Using a Frequency Comb Local Oscillator," *Proc. OFC*, 2019, paper Th3F.4.
- [15] J. Zhang *et al*., "Rate-Flexible Single-Wavelength TFDM 100G Coherent PON Based on Digital Subcarrier Multiplex ing Technology," *Proc. OFC*, 2020, paper W1E.5.

#### bIoGrAphIes

MD saIfUDDIN farUk [M'18] (msf35@cam.ac.uk) received his Ph.D. degree in electrical engineering and information systems from the University of Tokyo, Japan, in 2011. He joined as a faculty member of DUET, Bangladesh, in 2004. Currently, he is on leave from DUET and working as a senior research associate at the University of Cambridge, United Kingdom. His current research interests include DSP for coherent transceivers and optical access networks.

XIaNG lI (xl470@cam.ac.uk) received a Ph.D. degree from the School of Electrical and Electronic Engineering, Nanyang Technology University, Singapore, in 2016. Currently, he is working as a senior research associate at the University of Cambridge. His research interest focuses on high-speed coherent optical communications techniques. in long-haul transmission and passive optical networks.

Derek Nesset [M'00, SM'13] (derek.nesset@huawei.com) joined Huawei in 2017 to research new technologies for PON systems. Previously, he worked at BT, Marconi, and Corning. He has spent over 15 years contributing to next generation PON standards. He co-chaired the NG-PON task group in FSAN and was an Editor of G.9807.1 (XGS-PON).

Iván N. Cano (ivan.cano@huawei.com) joined Huawei in 2017, where he currently carries out research on high-speed and next-generation optical access networks. He has participated in several national and EU-funded projects related to short reach optical access networks.

Albert Rafel [M'18] (albert.2.rafel@bt.com) received a degree in telecoms engineering and a Ph.D. degree in optical communications, both from UPC, Catalonia, Spain. He joined BT in April 2001, where his research includes PON solutions for 5G, and has been active in ITU-T and FSAN for more than 12 years. He has participated in several EU research projects and has several technical published papers as well as patents.

Seb J. Savory [M'07, SM'11, F'17] (sjs1001@cam.ac.uk) received his M.Eng., M.A., and Ph.D. degrees in engineering from the University of Cambridge. He is currently the Professor of Optical Fibre Communication at the University of Cambridge. He was previously at University College London, from which he left as a professor, and prior to that Nortel (previously STL), where his interest in the field began when he joined the STL Harlow labs in 1991.
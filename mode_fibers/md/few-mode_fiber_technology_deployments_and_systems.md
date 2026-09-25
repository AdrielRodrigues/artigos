---
title: "Few-Mode Fiber Technology Deployments and Systems"
tema_principal: mode_fibers
temas_relacionados: []
pdf: ../pdf/few-mode_fiber_technology_deployments_and_systems.pdf
---

![](_page_0_Picture_0.jpeg)

# **Few-Mode Fiber Technology, Deployments, and Systems**

*This article reviews the third advanced category of space-division multiplexing fibers, which use the coupled waveguide modes of few-mode fibers in conjunction with multiple-input–multiple-output (MIMO) digital signal processing to achieve the highest spatial information density.*

By PIERRE SILLARD , *[Mem](https://orcid.org/0000-0002-0806-7133)ber IEEE*, KAOUTAR BENYAHY[A](https://orcid.org/0000-0002-1523-8674) , DAIKI SOMA , [GU](https://orcid.org/0000-0003-1012-8334)ILLAUME LABROILLE, PU JIAN, KOJI IGARA[SH](https://orcid.org/0000-0002-9156-6928)I , ROLAND RYF, *Fellow IEEE*, NICOLAS K. F[ONT](https://orcid.org/0000-0003-3540-6820)AINE , *Fellow IEEE*, GEORG RADEMACHER , *Senior Member IEEE*, AND KOHKI SHIBAHARA , *Member IEEE*

**ABSTRACT** | Mode-division multiplexing (MDM) using few-mode fibers (FMFs) appears as a promising technology to increase fiber capacity by a few orders of magnitude and sustain the traffic demand for the decades to come. The potential of MDM lies in its ability to exploit multiple modes within a single optical fiber strand. Since 2011 and the first promising demonstrations, impressive progress has been made. In this article, we will show how the most recent advances in design and fabrication have improved the performance of FMFs and MDM systems, and allowed to turn research demonstrations into practical deployments.

**KEYWORDS** | Optical fiber communication; optical fibers.

### **I. INTRODUCTION**

Since the beginning of optical fiber communication in the 1970s, fiber capacity growth has closely followed

Manuscript received 30 September 2021; revised 15 March 2022 and 8 June 2022; accepted 12 September 2022. Date of publication 3 October 2022; date of current version 11 November 2022. *(Corresponding author: Pierre Sillard.)* **Pierre Sillard** is with the Prysmian Group, 62092 Haisnes, France (e-mail: pierre.sillard@prysmiangroup.com).

**Kaoutar Benyahya** is with the Nokia Bell Labs Paris, 91620 Nozay, France (e-mail: kaoutar.benyahya@nokia-bell-labs.com).

**Daiki Soma** is with KDDI Research, Inc., Saitama 365-8502, Japan (e-mail: da-souma@kddi-research.jp).

**Guillaume Labroille** and **Pu Jian** are with Cailabs, 35200 Rennes, France (e-mail: guillaume@cailabs.com; pu@cailabs.com).

**Koji Igarashi** is with the Graduate School of Engineering, Osaka University, Osaka 565-0871, Japan (e-mail: iga@comm.eng.osaka-u.ac.jp).

**Roland Ryf** and **Nicolas K. Fontaine** are with the Nokia Bell Labs, New Providence, NJ 07974 USA (e-mail: roland.ryf@nokia-bell-labs.com; nicolas.fontaine@nokia-bell-labs.com).

**Georg Rademacher** is with the National Institute of Information and Communications Technology, Tokyo 184-8795, Japan (e-mail: georg.rademacher@nict.go.jp).

**Kohki Shibahara** is with the NTT Network Innovation Laboratories, Yokosuka 239-0847, Japan (e-mail: kouki.shibahara.nv@hco.ntt.co.jp).

Digital Object Identifier 10.1109/JPROC.2022.3207012

the exponential growth of traffic demand. The capacity increase has been enabled by the introduction of many novel technologies. Among them are optical amplification, wavelength-division multiplexing (WDM), coherent detection with digital signal processing (DSP), and polarizationdivision multiplexing modulation formats using both phase and amplitude. However, as we are closely approaching the nonlinear capacity limit of single-mode fibers (SMFs), there is a growing realization that these technologies will soon no longer suffice, and therefore, novel technologies are needed to keep up with traffic demand.

Spatial multiplexing in fibers, introduced more than four decades ago [1], [2], appears as a promising technology to increase fiber capacity and sustain the traffic demand for a few more decades. The potential of space-division multiplexing (SDM) lies in its ability to exploit multiple cores [in multicore fibers (MCFs)] or multiple modes [in few-mode fibers (FMFs)] or both (in FM-MCFs) within a single optical fiber strand.

One key advantage of FMFs is that they can be designed to guide a large number of modes (>∼100), each considered an independent data channel. Note that, throughout this article, we will use the term FMFs, even if such fibers can support many modes, to distinguish them from standard multimode fibers (MMFs) that are used for data communications (hundreds of modes carrying the same data at 850 nm). FMFs also have a standard cladding diameter of 125 μm and can be made with standard manufacturing processes. In comparison, (FM-)MCFs usually have cladding diameters of >125 μm to accommodate few tens of cores (only) and are made with nonstandard manufacturing processes (mostly by drilling or stacking and drawing) that are not adapted to low-cost and largescale production yet.

0018-9219 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

![](_page_1_Figure_1.jpeg)

Fig. 1. Experimental crosstalk values versus the number of LP mode groups for weakly coupled step-index-core-based FMFs: standard structure (solid red circles) and structure with a depressed-inner zone (open black circles).

 $125\text{-}\mu\text{m}\text{-}\text{cladding FMFs}$  offer advantages over larger-diameter (FM-)MCFs in terms of long-term mechanical reliability [3] and compatibility with standard connectivity solutions and cabling technology. It also improves fiber productivity because, for a given preform size, the fiber length is proportional to the inverse of the square of the cladding diameter.

If the number of exploitable modes in FMFs can be high, the inherent modal crosstalk ultimately limits the capacity improvements. There are two well-known approaches to cope with this issue. The first one, called the weakly coupled approach, consists of minimizing the crosstalk in all components of the MDM system so that each (group of) mode(s) is separately detected without using (complex) multiple-input—multiple-output (MIMO) techniques. The second one, called the full-MIMO approach, consists of minimizing the differential mode group delays (DMGDs) between all modes so that they can be simultaneously detected at reception, and MIMO can efficiently compensate for crosstalk.

In this article, we will review the most recent advances in design and realizations of FMFs and MDM systems for both approaches, and we will show how research demonstrations can now turn into practical deployments. We will also give a glimpse of their potential and perspectives.

## II. WEAK COUPLING

## A. Fiber Design and Manufacturing

Step-index-core-based profiles (see insets of Fig. 1) are well adapted to weakly coupled FMFs because of their simplicity in terms of design and manufacturing [4]. Usual SMF processes can be used allowing for low-cost and large-scale production.

Step-index-core fibers with two [5], [6], [7], four [7], [8], [9], six [10], [11], and seven [11] LP mode groups have been reported, most with attenuations  $\leq$ 0.25 dB/km at 1550 nm (see Section II-B1 for the use of FMF of

[11] and see Sections II-B2 and II-C2 for the use of FMF of [10]). For such FMFs, the main issue is the crosstalk that increases with the number of spatial modes and ultimately limits the achievable distance. Values increase from < 40 dB/km for two LP mode groups to  $\sim$  35 dB/km for four LP mode groups,  $\sim$  30 dB/km for six LP mode groups, and  $\sim$  25 dB/km for seven LP mode groups (see solid circles in Fig. 1).

One way to reduce crosstalk is to increase the effective index differences,  $\Delta n_{\rm eff}$ , between (groups of) modes (Min| $\Delta n_{\rm eff}| \geq 0.5 \times 10^{-3}$ , and preferably  $\geq 1 \times 10^{-3}$ , between any two (groups of) modes). However, this becomes more and more difficult as the number of modes increases. The core index must be significantly increased, and the core radius decreased, which yields to smaller effective areas and higher attenuations. Critical levels of effective areas (<70  $\mu m^2$ ) and attenuations (>0.25 dB/km) are expected for step-index-core seven-LP-mode-group fibers with Min| $\Delta n_{\rm eff}|=1\times 10^{-3}$  [12].

Alternative index profiles have, thus, been investigated to increase Min $|\Delta n_{\rm eff}|$ . The most commonly used approach consists of introducing a kind of the depressed-index zone in the center of the step-index core to reduce the effective index of the cylindrically symmetric modes or increase that of the other modes. This has allowed to increase Min $|\Delta n_{\rm eff}|$ from  $<1.0 \times 10^{-3}$  to  $>1.5 \times 10^{-3}$  for four- [13], six-[11], [14] and seven-LP-mode-group fibers [11], without impacting effective areas or attenuations. Despite these improvements, the crosstalk has not drastically decreased (about 2 dB/km only; see open circles in Fig. 1). This is due to the high mode overlapping between LP mode groups that have  $\Delta n_{\rm eff} > {\rm Min}|\Delta n_{\rm eff}|$  and still significantly contribute to the overall crosstalk [15]. As a result, to design weakly coupled FMFs with more than four LP mode groups and crosstalk values <-35 dB/km to reach tens or even hundreds of kilometers, one will have to work on the overlapping aspect.

Note that graded-index-core FMFs can also be used as weakly coupled FMFs. The issue is that their mode groups are composed of an increasing number of modes that can be difficult to recover at reception (see Sections II-B1 and II-C1).

Because of crosstalk, weakly coupled FMFs are more adapted to short-reach applications. Use mode group-division multiplexing (MGDM) and direct detection (DD) or simple  $2 \times 2$  and  $4 \times 4$  MIMOs and coherent detection, as will be discussed in Sections II-B and II-C.

#### **B.** Transmission Demonstrations

1) MGDM and DD: MGDM has been proposed as a good alternative to drastically increase the throughput over conventional graded-index-core MMFs for short-reach intensity-modulation (IM) DD transmissions [16], [17], [18], [19], [20]. Multiplexing a group of modes having the same propagation velocity instead of independent modes enabled to reduce the system complexity and avoid the

![](_page_2_Figure_1.jpeg)

**Fig. 2.** *Four mode groups used for transmission.*

application of full MIMO. A record of 14.5 Tb/s over more than 2 km of standard MMF (OM2) has been reported thanks to MGDM based on multiplane light conversion (MPLC) technique [21], [22] (see Section II-C1) using low-cost IM-DD schemes [23]. To extend the benefit of MGDM over longer distances, weakly coupled FMFs have been proposed to reduce the system limitations specifically in terms of modal crosstalk and power loss. Recently, dense SDM transmission experiments over a 38-core threemode fiber achieved a record capacity of 10.66 Pb/s [24]. However, dense SDM and coherent schemes are expensive for short-reach communications. Also, the fiber of [24] has a cladding diameter of 312 μm that prevents its practical use because of mechanical reliability issues [3]. Therefore, MGDM with IM-DD and weakly coupled FMFs with a standard cladding diameter of 125 μm are good candidates to increase capacity for short-link applications, such as interdatacenter interconnects while keeping low cost [25], [26].

In [26], MGDM with MPLC technology enabled 200-Gb/s bidirectional transmission over 20 km of weakly coupled step-index-core-based FMF fiber using selective excitation of four LP mode groups, DD, and a single laser in each propagative direction. The FMF [11] guides six LP mode groups: two nonspatially degenerate LP mode groups (LP01 and LP02) and four two-time spatially degenerate LP mode groups (LP11a,b, LP21a,b, LP31a,b, and LP12a,b). Only four LP mode groups are used for transmission, each transmitting independent data over the FMF (see Fig. 2). The maximum DMGD between the six LP mode groups has been measured at 23.7 ps/m. The chromatic dispersions (CDs) obtained by simulation for G1, G2, G3, and G4 are 20.5, 25.35, 31.25, and 26.95 ps/nm/km, respectively. As CD is not digitally compensated in IM-DD transceivers, with the highest dispersion, G3 will transport the lowest capacity over 20 km. Considering only the impact of CD, its propagation distance is equivalent to 36.4 km over standard SMF. Furthermore, lowering the number of modes compared to a standard MMF (OM2) [27] enables to reduce the crosstalk generated by the mode group multiplexer (MGM) and the mode group demultiplexer (MGD). The average crosstalk in a back-to-back configuration is −19.2 dB. Table 1 gives the loss and the crosstalk values

**Table 1** Measured Loss and Crosstalk

| MGM + 20km FMF + 2 splices + MGD |           |                |  |  |
|----------------------------------|-----------|----------------|--|--|
|                                  | Loss [dB] | Crosstalk [dB] |  |  |
| G1                               | -10       | -23            |  |  |
| G3                               | -11.7     | -17            |  |  |
| G2                               | -10.5     | -10.1          |  |  |
| G4                               | -12.4     | -16.6          |  |  |

of the MGD and the MGM, including 20 km of spliced FMF. A part of the crosstalk may arise from the quality of the splices. G1 and G3 propagate in one direction and G2 and G4 propagate in the reverse direction so that the same number of modes is managed by the MGM and MGD. The MGM converts the fundamental mode of each SMF connected at its input to one mode within the mode group. Excitation of only one mode is sufficient to excite all the modes in the same mode group due to their high mode coupling. However, all the modes of the same group should be detected at the receiver to avoid large power fluctuations. Here, all mode groups are LP mode groups (so a maximum of two spatial modes to detect at reception), which allows scaling this strategy to any number of mode groups and can, thus, provide increasing capacity with decreasing the cost per bit. If mode groups are composed of an increasing number of spatial modes, as is the case for graded-index-core FMFs or standard MMFs, detecting all modes of the same mode group becomes complex and makes the scalability of this strategy difficult. FMFs are connected to the output of the MGD. Furthermore, the MGD converts the higher order modes to the lowest ones typically for G3 and G4, as illustrated in Fig. 2, to benefit from the high bandwidth of the photodiode having a small effective area.

The crosstalk can encounter time fluctuations [29], [30], [31]. Hence, it is important to ensure system margins for all the mode groups in terms of transmitted bitrate. Fig. 3(a) and (b) displays the bit error rate (BER)

![](_page_2_Figure_9.jpeg)

**Fig. 3.** *BER variations versus time because of crosstalk fluctuations at 55 Gb/s: (a) G1 and G3. (b) G2 and G4.*

![](_page_3_Figure_1.jpeg)

**Fig. 4.** *(a) Entropy of each WDM channel. (b) Measured NGMIs of all MDM/WDM tributaries.*

variations over 150 min for the four mode groups modulated at 55 Gb/s with DMT format. The BER performance of all mode groups fluctuates between the worst case and the best case. However, it stays below the forwarderror-correction (FEC) threshold. This observation could give interesting information about the variation speed of the crosstalk phase. Statistical characterization of crosstalk fluctuations in a DD regime is reported in [30]. It reveals the dependency of the BER penalty on the chosen modulation format. Experimental comparison of 100-Gbs four-PAM and 100-Gbs DMT shows that DMT is more resilient to crosstalk and could, thus, be the best candidate for IM-DD MGDM transmissions.

*2) High-Capacity MDM With 2* × *2 and 4* × *4 MIMOs:* Weakly coupled MDM transmissions with lower order MIMO processing have also been proposed to mitigate the burden of MIMO processing for higher order MDM transmissions [32]. In this part, we demonstrate weakly coupled ten-spatial-mode multiplexed transmission with only 2 × 2 MIMOs and 4 × 4 MIMOs over a 48-km 125-μm cladding ten-spatial-mode fiber (10MF) [33], [34]. By using the rate-adaptive probabilistically shaped (PS) dualpolarization (DP) 16 quadrature amplitude modulation (QAM) signals in the *C*- and *L*-bands, we achieved a fiber capacity of 402.7 Tb/s per single-core fiber.

In this experiment, we measured the normalized generalized mutual information (NGMI) [35] for ten-spatial-mode-multiplexed 747-WDM 12-Gbaud PS-DP-16QAM signals after 48-km weakly coupled 10-MF transmission. The PS-16QAM signals were generated by using probabilistic amplitude shaping [36], and their entropy was optimized for each WDM channel to maximize spectral efficiency. The 379 WDM channels

(1527.459–1565.138 nm) in the *C*-band and 368 WDM channels (1569.851–1608.490 nm) in the *L*-band were modulated by the PS-16QAM signals. After these WDM signals were combined and power-equalized over the *C*- and *L*-bands, we obtained 12.5-GHz-spaced 12-Gbaud 747-WDM Nyquist-shaped PS-DP-16QAM signals.

The generated WDM signals were fed into each port of a highly mode-selective ten-spatial-mode multiplexer. Ten spatial modes, namely, LP01, LP11a, LP11b, LP21a, LP21b, LP02, LP31a, LP31b, LP12a, and LP12b, were generated and excited into 10 MF by the MPLC technique [37] (see Section II-C1). The average crosstalk between the two LP mode groups and the total crosstalk from the other LP mode groups in this ten-spatial-mode multiplexer/demultiplexer measured at 1550 nm were approximately −22.9 and −13.6 dB, respectively.

10 MF, which has a step-index-core profile, was designed with large <sup>Δ</sup>*n*eff (>0.6 <sup>×</sup> <sup>10</sup>*−*3) between adjacent LP mode groups to suppress the crosstalk [10]. The core diameter and the cladding diameter of the 10 MF were 17 and 125 μm, respectively. In this transmission experiment, we optimized the launched signal power of each mode into individual input ports of the mode multiplexer across the *C*- and *L*-bands at 1550 and 1590 nm so that the differences in the measured NGMIs between the ten spatial modes caused by the differences of crosstalk were equalized.

After 48-km transmission, the ten-spatial-mode multiplexed WDM signals were mode demultiplexed by the ten-spatial-mode demultiplexer and then wavelength demultiplexed by optical bandpass filters. Five demultiplexed lower order modes (LP01, LP11a, LP11b, LP21a, and LP21b) or five higher order modes (LP02, LP31a, LP31b, LP12a, and LP12b) were simultaneously detected by

![](_page_4_Picture_1.jpeg)

Fig. 5. Photograph of a mode multiplexer based on MPLC.

five coherent receivers based on heterodyne detection. In off-line processing, the stored samples were independently processed by two adaptive  $2 \times 2$  MIMO equalizers for  $LP_{01}/LP_{02}$  and four  $4 \times 4$  MIMO equalizers for  $LP_{11ab}/LP_{21ab}/LP_{31ab}/LP_{12ab}$ . The MIMO tap size was set at 350 for all the modes. The MIMO tap coefficients were updated based on the decision-directed least mean square (LMS) algorithm [38]. After the symbols were decoded, the NGMIs were measured [35].

In this experiment, the entropies of the WDM channels were roughly optimized zone by zone in the wavelength so that the worst NGMI in the ten spatial modes was close to the FEC threshold. Here, we assumed an FEC with 25.5% overhead [39] whose Q limit of 4.95 dB corresponds to the NGMI threshold of 0.8571. Fig. 4(a) shows the entropy of each WDM zone. Finally, we measured NGMIs of the ten-spatial-mode multiplexed 747-WDM channels. Fig. 4(b) shows the NGMIs of all the spatial and wavelength channels (7470 channels). The NGMIs of the measured MDM/WDM tributaries exceed the FEC threshold of 0.8571. In this experiment, we achieved a transmission capacity of 402.7 Tb/s with only  $2 \times 2$  MIMOs and  $4 \times 4$  MIMOs over 48 km of weakly coupled 10 MF.

#### C. Deployments

1) MGDM to Increase Local Area Networks' Capacity: The global need for increasing throughput in optical fiber is particularly acute in local area networks (LANs). High bandwidth demands for storage, streaming media, cluster computing, digital imaging, and so on are hindered by the limited capacity of standard MMFs that are ubiquitous in LANs. MGDM proves to be a solution to increase the capacity of these standard MMFs without the cost and complexity of rolling out SMFs.

We use an MGM based on the MPLC technique [22], a patented technology developed by Cailabs in 2013. MPLC is a technique that allows performing any unitary spatial transform. Theoretically, any unitary spatial transform can be implemented by a succession of transverse phase profiles separated by free space propagation for optical Fourier transforms. The MPLC cavity is formed by a mirror and the reflective phase plate, implementing the successive phase profiles and optical transforms (see Fig. 5). Indeed, the unitarity of the transform ensures that there is no

intrinsic loss in the mode conversion. Losses in MPLC only occur due to imperfect optical elements (e.g., coating or imperfect phase plate manufacturing). The inverse unitary transform, given by using the MPLC in the reverse direction, implements the demultiplexing operation of the same modes.

Based on MPLC, the fabrication of 45-spatial-mode multiplexers has been reported in 2018 with an average 4-dB insertion loss and -28-dB crosstalk all over the C-band into a standard MMF (OM2) [40]. The MPLC was also used as an SDM to achieve 10.16-Pb/s dense SDM/WDM transmission [41]. In this type of SDM architecture, the use of MIMO combined with coherent detection allows to exploit all the SDM channels to maximize the transmission (see Section III). Standard LANs work with DD for which it is not possible to use MIMO technology.

In an MGDM configuration, the MPLC technology converts each single-mode input into one mode of a mode group [42]. Only one mode of each group needs to be excited. Indeed, due to the strong intramode group coupling, all the modes of the same mode group will be excited all along the transmission into the intermediate fiber and need to be detected simultaneously at the demultiplexing stage to avoid large power fluctuations at the receiver (see Section II-B1). The reception is obtained by demultiplexing all modes and then summing the optical fields by coupling the modes of the same mode group in an MMF pigtail [43]. This last stage of summation and coupling is also performed passively, without any additional optical element, by the MPLC that has been designed to selectively demultiplex each group into a distinct output MMF (see Fig. 6).

First, we performed the experimental evaluation in a laboratory environment by measuring the BER in a configuration comprising an MGM, 600 m of standard MMF (OM1), and an MGD. BERs lower than  $10^{-9}$  have been measured using commercial 10-Gb/s transceivers with OOK modulation format at 1550 nm on all four mode groups (see Fig. 7).

Field tests were then performed: we realized  $4 \times 10$  Gb/s transmissions using the same types of commercial transceivers over 400 m and up to 940 m in various MMF pairs (OM1 and OM2) in LANs that propose

![](_page_4_Figure_13.jpeg)

Fig. 6. Diagram of an MPLC MGM configuration with a standard MMF (OM2) with Hermite–Gaussian modes.

![](_page_5_Figure_1.jpeg)

**Fig. 7.** *BERs at 1550 nm of a four-mode-group 10-Gb/s MGDM transmission over 600 m of standard MMF (OM1).*

a standard bit rate of 100 Mb/s, resulting in a gain factor of 400 in maximum bit rates [44]. We measured average insertion loss of around 6.5 dB and worst crosstalk value of around −14 dB (MGM + MGD configuration) The different field tests, as summarized in Table 2, took place in several typical LAN typologies (hospital, university, corporate campus, and so on) under different environmental conditions with different generations of fibers and different deployment years.

A concrete example is the upgrade of a 1999 OM1 link of 3300 m length in the two Alpes ski resorts in France located at 2600 and 3200 m altitudes in 2017. The MGDM technology for this ski resort network infrastructure renovation project reduced drastically the costs and minimized disruptions. This achievement represents an important milestone for the deployment of high-capacity network equipment for future network growth demands inside standard MMF infrastructures.

*2) Real-Time MDM With 2* × *2 and 4* × *4 MIMOs:* Realtime implementation of MIMO-DSP based on applicationspecific integrated circuits (ASICs) is indispensable for the practical deployment of MDM systems. The capacities of MDM systems are limited by the size of the implementable MIMO-DSP because the MIMO size increases in proportion to the square of the number of modes. To clarify the achievable capacities in practical MDM systems, investigating to

**Table 2** MGDM Field Trials Examples With MPLC Technology

| Network     | Length of  | MMF  | Deployment | Bit rates |
|-------------|------------|------|------------|-----------|
| type        | fiber link | type | year       |           |
| Hospital    | 552m       | OM1  | 1989       | 4×10Gbps  |
| University  | 926m       | OM2  | 2004       | 4×10Gbps  |
| Urban       | 940m       | OM1  | 1997       | 4×10Gbps  |
| Community   |            |      |            |           |
| Industrial  | 2200m+600m | OM1  | 1980       | 4×10Gbps  |
| site        |            |      |            |           |
| Ski station | 3300m      | OM1  | 1999       | 4×10Gbps  |

what extent the size of the MIMO can be implemented is essential.

The MIMO-DSP size is determined not only by *N* but also by the tap size of the FIR filters, which can be long because of the accumulated DMGDs in MDM systems. Instead of the use of long-tap FIR filters, frequency-domain equalization is effective to reduce the computational complexity [45]. However, it is unsuitable for MDM transmissions because the adaptive control based on the block processing becomes slow and cannot track the dynamic changes of the crosstalk.

There have been a lot of reports investigating the required tap size and calculation complexity of the MIMO-DSP [46], [47], [48]. A notable way to reduce this required tap size is to employ multicarrier modulation [49] instead of single-carrier modulation. By reducing the signal baud rate, the impulse response spread is proportionally decreased, reducing the required tap size. In this part, we consider moderate tap size in the MIMO, assuming to apply the multicarrier modulation.

Because ASIC-based development is extremely costly, implementation based on field-programmable gate array (FPGA) circuits is a reasonable step for ASIC-based product design. Although MDM transmission experiments had previously been conducted mainly using off-line DSP on personal computers (PCs), demonstrations of real-time MDM transmission began in the mid-2010s. The first demonstration of real-time MDM transmission was reported in 2015 [50]. Three-spatial-mode multiplexed DP quadrature phase shift keying (DP-QPSK) optical signals were transmitted over 60 km of a coupled three-core fiber and decoded using parallel coherent receivers, which was followed by FPGA-implemented MIMO-DSP. In 2019, realtime ten-spatial-mode multiplexed transmission experiments of DP-QPSK optical signals over 48 km of the weakly coupled ten-spatial-mode fiber were demonstrated [51], [52]. Recently, real-time MDM transmission experiments over coupled MCFs have also been reported [53], [54], [55].

In this part, we introduce our demonstration of a realtime ten-spatial-mode multiplexed transmission experiment using real-time MIMO implemented on FPGAs. We also discuss technical issues regarding the real-time implementation of adaptive MIMO equalization.

*a) Resource requirement for real-time MIMO DSP* In current 200-Gb/s DP SMF coherent systems, a complexvalue 2 × 2 MIMO is in practical use based on 16-nm CMOS technology, and it is considered as a baseline in this subpart. Fig. 8(a) reviews the future roadmap for enhancing transistor density in CMOS-based large-scale integration (LSI). Currently, the 16-nm CMOS technology has been widely employed in LSI for optical communications. The 5-nm CMOS platform technology has been ready since 2020 [55], and the transistor density can be increased by approximately ten times compared to that of the current 16-nm technology. For the next generation, the 3-nm process is expected to begin in late 2022. The

![](_page_6_Figure_1.jpeg)

**Fig. 8.** *(a) Roadmap of transistor density in feature CMOS technology. (b) Resource requirement for MIMO implementation.*

cutting-edge CMOS technology can enhance the density by 30 times.

Fig. 8(b) shows the CMOS resources required for MIMO implementation. The gray area indicates the size of the 2 × 2 MIMO in the DP SMF system. The full-MIMO MDM system with *N* multiplexed spatial modes requires a 2*N* × 2*N* MIMO. The required resources increase in proportion to the square of the multiplexed spatial mode number *N*. For the three-spatial-mode system, the required size is nine times greater than that of a DP SMF system. The requirement could be met by the next 5-nm CMOS technology. In the six-spatial-mode case, an MIMO that is 36 times larger is required. Although it is very challenging, the 3-nm CMOS technology could make it possible.

Unlike the full-MIMO MDM approach, the weakly coupled MDM approach is effective at avoiding the use of large-scale MIMO. As long as the couplings between different LP mode groups are suppressed, the mode couplings are limited between two-time spatially degenerate LP mode groups, such as LP11a and LP11b, thereby drastically reducing the required MIMO size to the 4×4 matrix, which is called partial MIMO, as shown in Fig. 8(b). Although the resource requirement with the approach is reasonable, sufficiently suppressing couplings between different LP mode groups in FMFs, FM optical amplifiers, mode multiplexers, and demultiplexers is challenging.

*b) Real-time implementation of adaptive MIMO equalization* We consider the algorithm that is most suitable for the adaptive control of real-time MIMO in large-scale MDM systems. Adaptive algorithms are roughly divided into two categories: training and blind. The training algorithm uses known symbols transmitted with information symbols. In the well-known LMS algorithm, the tap coefficients of MIMO are controlled such that the mean square errors are minimized. Because it is phase-sensitive, the tracking speed is too slow to be applied to optical coherent systems in the presence of considerable laser phase noise. By contrast, the blind algorithm uses signal statistics, such as constant intensity in the PSK format. Although the blind method is simpler because it does not require any training sequences, the singularity problem becomes critical for the application to large-scale MDM systems. Fig. 9 shows the numerical results of the occurrence probability of the singularity problem as a function of the mode number [52].

![](_page_6_Figure_7.jpeg)

**Fig. 9.** *Numerical dependence of occurrence probability of the singularity problem on mode number.*

![](_page_6_Figure_9.jpeg)

**Fig. 10.** *Parallel configuration of DSP in an optical receiver.*

![](_page_6_Figure_11.jpeg)

**Fig. 11.** *Required BER for BER of 10−<sup>2</sup> as a function of spectral linewidth normalized by DSP bandwidth, δf · δ/fDSP. Here, δf: linewidth; δ: pipelined delay; and fDSP: DSP clock frequency.*

In the simulation, DP-QPSK optical signals with *N* modes were decoded using adaptive MIMO equalization based on the blind algorithm. The closed and open marks indicate the results obtained using conventional CMA and modified CMA [57], respectively. Note that the singularity problem becomes more significant as the number of multiplexed modes increases, even when using the modified CMA. These results suggest that the blind algorithm is not applicable to large-scale MDM systems.

The calculation delay is inevitable in real-time implementation. The sampling frequency *fs* of analog-to-digital converters (ADCs) in optical receivers must be faster than

![](_page_7_Figure_1.jpeg)

Fig. 12. Configuration of our fabricated real-time MIMO receiver prototype.

![](_page_7_Figure_3.jpeg)

Fig. 13. Our fabricated MIMO with separated carrier phase and frequency offset compensators.

twice the baud rate of the received signals (i.e., several tens of gigahertz). However, the clock frequency  $f_{\rm DSP}$  in DSP circuits remains several hundreds of megahertz. To bridge the frequency gap between  $f_s$  and  $f_{\rm DSP}$ , deserialization or parallelization is required, as shown in Fig. 10. The received signals are sampled and digitized at the sampling frequency  $f_s$  and then deserialized into multiple tributaries to perform real-time DSP at the clock frequency  $f_{\rm DSP}$ . In the parallel configuration, symbol-by-symbol processing is not possible, and the DSP speed is limited by the clock frequency. A delay also occurs when the calculation is not executed completely within a single clock cycle. This is called a pipelined delay. The total delay is determined by multiplying the parallelized delay P with the pipelined delay  $\delta$  (i.e.,  $P \cdot \delta$ ).

Note that the calculation delay in the real-time DSP destabilizes feedback control while significantly degrading the performance of adaptive control. We numerically evaluated the BER performance of adaptive MIMO equalization based on the LMS algorithm for single-mode DP-QPSK signals in the presence of laser phase noise with spectral linewidth  $\delta f$  [52]. The calculated required signal-to-noise ratio for a BER of  $10^{-2}$  is shown in Fig. 11(a). The BER performance is determined not only from  $\delta f$  but also from  $\delta$  and  $f_{\rm DSP}$  although it does not depend on the signal baud rate in the real-time DSP because symbol-by-symbol processing is not possible. We found that  $\delta f \cdot \delta/f_{\rm DSP}$  of less than  $4 \times 10^{-5}$  was required to maintain a signal-to-noise ratio penalty of less than 2 dB in the conventional LMS algorithm.

![](_page_7_Figure_7.jpeg)

Fig. 14. Measured BER values for all spatial modes and all subcarriers.

multiplexed Real-time ten-mode transmission experiments We fabricated a real-time MIMO receiver prototype to receive ten-spatial-mode multiplexed DP-QPSK signals in weakly coupled MDM systems [51], [52]. Fig. 12 shows the configuration of the receiver prototype, which was designed to receive ten-spatialmode multiplexed 18-subcarrier modulated DP-QPSK optical signals. The baud rate of one subcarrier was 625 Mbaud, and the signal bandwidth was 12 GHz. The mode multiplexed signals were demultiplexed into two-time-spatially LP mode groups using a mode demultiplexer based on the MPLC technique [22], and the demultiplexed modes were then simultaneously received using two coherent receivers, which were followed by two four-channel 1.25-Gsample/s ADCs (Abaco FMC126) connected to two FPGA evaluation boards (Xilinx Virtex-7 FPGA VC707). The sampled sequences were transferred to another FPGA evaluation board (Xilinx Vertex-7 FPGA VC7215), where the sequences were deserialized into four tributaries to perform adaptive MIMO equalization at a clock frequency of 156.25 MHz.

Fig. 13 shows the configuration of our implemented MIMO equalizer based on the training algorithm. Note that phase and frequency offset compensators based on single taps were separated from the MIMO part, and the tap coefficients were simultaneously updated, thereby improving phase tracking speed. This is called the Mori algorithm [57]. The numerical results, as shown in Fig. 11, suggest that the Mori algorithm improves phase tracking speed by five times over that of the conventional LMS algorithm.

We conducted a real-time ten-spatial-mode multiplexed transmission over 48 km of weakly coupled FMFs using the real-time MIMO receiver prototype [52], [53]. The measured BER results of all the subcarriers and ten spatial modes with DP are shown in Fig. 14. We observed that the measured BER values were maintained below  $2.7 \times 10^{-2}$ , which corresponds to the BER threshold for 20% overhead forward error correction. In our experiments, one complexvalue channel was decoded only because of the resource limitation of the FPGA board. To decode all subcarriers and all channels of the two-mode multiplexed signals, we needed approximately 200 FPGAs. In our prototype, one-generation-ago Xilinx Virtex-7 FPGAs were used. If we were to use cutting-edge FPGAs, such as Xilinx Virtex Ultrascale+ FPGA, the required number of FPGAs would be drastically reduced (i.e., by one-third or 70 FPGAs), which is acceptable for ASIC-based products.

#### III. FULL MIMO

## A. Fiber Design and Manufacturing

Trench-assisted graded-index-core profiles (see inset of Fig. 15) have proven to be well adapted to low-DMGD FMFs for full-MIMO MDM transmissions [4]. The graded-index core minimizes the DMGDs (as for standard MMFs), and the trench reduces the bending sensitivity.

![](_page_8_Figure_7.jpeg)

Fig. 15. Max|DMGD| versus number of mode groups for low-DMGD trench-assisted graded-index-core FMFs: calculations (open blue circles for standard processes and open black squares for MM processes) and experiments (solid black squares for MM processes). Lines are guides for the eye.

Usual MMF processes can be used to manufacture such FMFs, allowing for low-cost and large-scale production (see below).

Fibers with three [58], [59], six [59], [60], ten [9], [60], [61], and 15 [62], [63] spatial modes have been reported with attenuations ≤0.22 dB/km at 1550 nm. For such FMFs, the main concern is not the crosstalk but the DMGD, which increases with the number of spatial modes, and the resulting increased MIMO complexity. In theory, DMGDs of  $\sim 0$  ps/km for three spatial modes,  $\sim 75$  ps/km for 15 spatial modes, and  $\sim$ 115 ps/km for 28 spatial modes can be obtained [12], [15]. DMGDs, however, are highly sensitive to process variability [9], [59], which prevents them from reaching these minimum theoretical values. To account for this sensitivity, we simulated Gaussian distributions of index profiles with mean values corresponding to the optimized designs and with standard deviations that match process tolerances. The resulting mean values of the DMGDs of these profiles are representative of actual manufacturing [62]. For standard processes, DMGDs now steeply increase from ~25 ps/km for three spatial modes to  $\sim$ 180 ps/km for 15 spatial modes and  $\sim$ 410 ps/km for 28 spatial modes (see open circles in Fig. 15).

To cope with this issue, standard trench-assisted graded-index-core MM preforms, appropriately rescaled in diameter, adjusted in alpha (exponent of the graded-index cores) and in trench position, can be used [61], [62], [63], [64]. The resulting FMFs benefit from the tight process tolerances of MM production and the reduced impact of DMGD sensitivity that goes with it (see squares in Fig. 15). This has allowed reaching record DMGDs <80 ps/km for a 15-spatial-mode fiber [63] (see Sections III-B2 and III-B4). Using MM processes also allows for mass production.

One other (complementary) option to reduce these values is to concatenate fibers with DMGDs with opposite signs and, thus, realize DMGD-compensated links. DMGDs

![](_page_9_Figure_1.jpeg)

**Fig. 16.** *(a) 45-mode MIMO transmission experiment: quality factors Q of the 90 spatial tributaries for QPSK and 16-QAM transmission over 26.5-km FMF. (b) Average Q-factor for QPSK and 16-QAM as a function of wavelength. The error bars represent the best and the worst spatial tributaries [71].*

can then be reduced by factors of 2–4 [65]. As an example, a fiber link with values ≤40 ps/km for 45 spatial modes has been reported [15] (see Section III-B1).

These low-DMGD FMFs have larger effective areas than those of weakly coupled FMFs (≥<sup>90</sup> <sup>μ</sup>m<sup>2</sup>) mainly because there is no constraint on crosstalk and, thus, Δ*n*eff. They have allowed demonstrating several records transmissions using full MIMO and coherent detection, and could be used for future deployments, as will be discussed in Section III-B.

# **B. Transmission Demonstrations and Deployments**

*1) High Spectral Efficiency MDM Over 45-Spatial-Mode Graded-Index-Core FMF:* One key advantage of gradedindex-core FMFs is that they can be designed to support a large number of modes and potentially scale to proportionally large transmission capacities. It is, therefore, of interest to understand if there are practical limitations on the number of modes stemming from the required components, such as mode multiplexers or the MIMO DSP algorithms.

Since the first experimental full MIMO transmission demonstration in 2011 [66], over the years, the number of modes was continuously increased to six [67], ten [68], 15 [69], 36 [70], and 45 modes [71], following the natural mode group structure of graded-index-core fibers. As these experiments are very hardware intensive, particularly because phase, amplitude, and polarization for all the modes at the receiver have to be detected simultaneously and at high sampling rates, new measurements techniques using SMFs as optical storage delay have been developed [72], thus reducing the number of captured real-time channels by a factor of 3 or more. In addition, new highperformance mode multiplexers with large mode counts had to be developed. While, up to ten or 15 modes, photonic lanterns are preferable as mode multiplexers because of the small additional insertion loss, for a larger number of modes, the fabrication becomes tedious, and mode multiplexers based on MPLC technique become attractive, as they can be scaled up over 1000 modes [73], with only a modest increase in the number of additionally required phase planes in the multiplane light converter.

The experimental results of a 45-mode (90 × 90 MIMO) transmission are reported in Fig. 16. The experiment was performed over a 26.5-km-long FMF, consisting of four spools with lengths of 8.878, 4.35, 8.878, and 4.445 km, and DMGDs of −57, 140, 172, and 171 ps/km, respectively, resulting in a total accumulated DMGD of 2.4 ns [15]. The DMGD is a key parameter for full MIMO transmission, as it dictates the temporal length of the digital MIMO filter needed to recover the signals after mode mixing along the fiber.

The modes are multiplexed in the FMF by using a pair of mode multiplexers [74] based on the MPLC technique. Fig. 17 shows the precise modal content of the multiplexers measured using off-axis digital interferometry, which also can determine crosstalk and, most importantly, the modedependent loss (MDL) of the mode multiplexers and fiber spools at various stages. The mode multiplexers had a typical insertion loss of 4 dB and a peak-to-peak MDL of 3 dB measured for each multiplexer, resulting in a total loss, and MDL for the span including the mode multiplexers is 14 and 8 dB, respectively, including all nine mode groups.

The test signal for the experiment consisted of ten WDM channels spaced by 50 GHz and modulated with a dualcarrier 15-Gbaud signal, resulting in 20 Nyquist-shaped 15-Gbaud QPSK or 16-QAM wavelength channels; the test signal was delay decorrelated by a 45-way split and injected into mode multiplexer.

The 45 polarization-multiplexed transmitted signals are detected using a 1:3 time multiplexing scheme [72], followed by 15 polarization-diverse heterodyne receivers (PD-HRxs) and detected on 30 electrical channels of a 40-Gsamples/s digital storage oscilloscope (DSO). The reconstructed 90 complex amplitude signals are processed

![](_page_10_Figure_1.jpeg)

**Fig. 17.** *(a) Mode profiles at the output of the device (MPLC free-space outputs). (b) Modes after 3-m 50-µm graded-index-core FMF (MPLC fiber-coupled). (c) Mode profiles after 1 m,10 km, and 20 km of FMF (Group #) [74].*

![](_page_10_Figure_3.jpeg)

**Fig. 18.** *(a) Intensity impulse response of a 26.5-km-long FMF obtained from a channel estimation. (b) Intensity transfer matrix showing the coupling between the nine mode groups [71].*

by a frequency-domain 90 × 90 MIMO equalizer with 300 symbol-spaced taps. The initial convergence of the equalizer is obtained by using the data-aided LMS algorithm, whereas the constant-modulus algorithm (CMA) is used afterward. Finally, carrier-phase recovery and BER counting are performed, and Q factors are computed by evaluating an inverse Q function of the BER.

The obtained Q factors are reported for a wavelength of 1549.70 nm in Fig. 16(a) as a function of the mode group and sorted by performance within the mode group. For QPSK signals, all modes have *Q* > 9.8 dB for all wavelengths, whereas, for 16-QAM, the Q factors vary from 5.8 to 12 dB and are >8 dB for almost all of the first eight mode groups. The Q factors calculated from the average BERs are 13.5 and 9.2 dB for QPSK and 16-QAM, respectively. This value is representative of a system that uses a simple bit-interleaved encoding scheme [68] and is within the capability of a hard-decision FEC, and results in spectral efficiency of 202 b/s/Hz if an FEC overhead of 7% is assumed. In Fig. 16(b), we show the average and best/worst spatial tributaries represented as error bars for all 20 WDM channels under test, confirming a consistent performance as a function of the wavelength.

The intensity impulse response averaged over the 90 × 90 impulse responses was obtained from channel estimation and is shown in Fig. 18(a). The impulse response shows the effect of modal group dispersion where some of the peaks corresponding to the mode groups are visible. The overall width of the impulse response is around 2.5 ns, consistent with the DMGD measurements. The intensity transfer matrix between the input and output nine mode groups is shown in Fig. 18(b).

The experiments clearly show that MIMO-based transmission up to 45 modes is possible, resulting in spectral efficiency of 202 b/s/Hz over a distance of 26.5 km.

*2) High-Capacity MDM:* To maximize the total throughput of MDM transmission systems and scale the data rates compared to SMF with the number of spatial modes, it is necessary to transmit wideband signals, spanning

![](_page_11_Figure_1.jpeg)

**Fig. 19.** *Schematic of the transmission system demonstration.*

the *C*-band or even the *C*- and *L*-bands. To demonstrate the feasibility of transmitting such wideband signals over a 15-spatial-mode fiber, a transmission demonstration was preformed according to the schematic in Fig. 19. 15 MDM × 382 WDM 24.5-GBaud DP-64-QAM signals were modulated on 25-GHz spaced carrier lines, generated by a single optical comb source. The signals were modemultiplexed in mode-selective mode multiplexers [75] that were based on the MPLC technique, where the 15 input spots from an SMF array were transformed through 15 reflections on phase masks into 15 orthogonal modes that could be guided by the 15-spatial-mode fiber. The mode multiplexer had an insertion loss of around 9.5 dB, while the modal loss variation was below 3.5 dB.

The 23-km-long FMF had a trench-assisted, gradedindex profile with a core radius of 14.1 μm [63]. The profile was chosen to minimize the DMGD of the fiber at 1550 nm. The attenuation spectrum of the first four mode groups was similar, ranging between 0.22 dB/km at 1530 nm and 0.21 dB/km at 1590 nm, while the fifth mode group had up to 0.32-dB/km attenuation at a 1610-nm wavelength. After transmission, the signals were modedemultiplexed, and the 15 output signals were received in a 15-channel coherent receiver where the signals were digitized simultaneously in a real-time oscilloscope, operating

at 80 GSample/s. As signals mixed during transmission, coherent MIMO equalization was implemented with 30 × 30 time-domain equalizers, taking into account the two polarizations of each fiber spatial mode. The equalizer used 281 half-symbol-spaced taps and was initialized in a data-aided mode before switching into a decisiondirected mode for signal performance evaluation. Additional details on the transmission experiment can be found in [76] and [77].

One key parameter, determining the complexity of the MIMO-DSP implementation, is the temporal spread that signals experience during transmission as a result of the DMGD. This can be analyzed through the impulse response duration that a signal experiences when transmitted over the transmission system. Fig. 20(a) shows the impulse response duration for all 382 MDM/WDM channels. At 1530-nm wavelength, the impulse response is shortest at approximately 2 ns, which corresponds to a linear accumulation of temporal spread with transmission distance, as the DMGD was measured at less than 100 ps/km (see Fig. 15, black square labeled [63]). Toward longer wavelength channels, the impulse response duration increases up to approximately 3.7 ns at 1610 nm. This is due to the spectral variations of the DMGD, an inherent property of FMF. MDL is a channel property that can fundamentally limit the channel capacity. Spectral MDL variations were measured between 7 dB in the central *C*-band up to 10 dB at the high *L*-band. While it was found that MDL was mostly introduced by the mode multiplexers, the increased loss in the fifth mode group at high *L*-band channels also contributed to the total MDL. Fig. 20(b) shows the data rate after FEC for all 382 MDM/WDM channels. Data rates between 1.9 and 3.5 Tb/s were measured across more than 82-nm bandwidth, with lower performance toward the edges of the transmission window. In the high *L*-band, this can be explained by increased MDL. In addition, signals with larger spectral separation from the comb-generator seed at 1558 nm suffered from increased phase noise, contributing to reduced signal quality. The total data rate, calculated as the sum of all MDM/WDM channels, was

![](_page_11_Figure_7.jpeg)

**Fig. 20.** *(a) Impulse response duration. (b) Data rates of all 382 MDM/WDM channels.*

1.01 Pb/s, the highest reached today in an optical fiber that maintains the current standard for cladding diameters of 125 μm.

*3) Ultralong-Haul MDM:* In addition to the advantage of the enhanced efficiency of the use of the spatial degree of freedom in a fiber, low-DMGD FMFs can also be used to improve the tolerance against the fiber nonlinearity due to larger effective areas [78] (see Section III-A). In consideration for future practical use in a scalable MDM transport system, one key aspect is the steady development and establishment of MDM technologies that boost the achievable transmission reach of MDM signals over FMF transmission links. Signal performance in long-haul MDM transmission is, however, still dominantly affected by some specific "linear" phenomena that characterize *n* MDM transmission link, including DMGD and MDL. This part focuses on key techniques enabling long-haul MDM transmission with a brief review of the state-of-the-art progress.

Fig. 21 overviews the progress of currently reported long-haul MDM transmission experiments. The first MDM/WDM transmission with a distance exceeding 100 km was reported in 2012 [79], followed by some record-breaking experiments in terms of MDM transmission reach and/or capacity per fiber [80], [81]. In these earlier MDM transmission experiments, achievable transmission reach was restricted to around 1000 km. This is attributed to the fact that mode-relevant properties accumulate with an increased transmission distance because of low coupling efficiency between mode groups [82]. One fundamental performance-limiting factor is DMGD. From the perspective of information-carrying signals, DMGD causes time-domain pulse spreading in the impulse response. This inevitably enlarges a computational complexity requirement on receiver-side MIMO-DSP. Other negative features to deal with DMGD include

![](_page_12_Figure_4.jpeg)

**Fig. 21.** *Progress on MDM transmission with a distance exceeding 100 km.*

increased complexity of MIMO-DSP proportional to the squared number of the spatial channels [49], a larger amount per unit fiber length relative to other dispersion phenomena (i.e., CD and polarization mode dispersion), and wavelength-dependent dispersion slope [83] (see Section II-C1). Another obstacle to be overcome is MDL (or mode-dependent gain) that mainly arises from MDM components located in MDM transmission links, including multiplexers/ demultiplexers, optical amplifiers, optical nodes, and splicing/connection points. MDL imposes a different loss on each spatial mode and directly decreases achievable MIMO capacity. In terms of MIMO signal detection, the difficulty in dealing with MDL lies especially in MIMO-DSP because orthogonality between spatial channels is lost due to the MDL's presence, which generally makes signal detection complicated due to a higher intermodal correlation in received signals [84].

Various techniques based on both digital and optical approaches have been reported to reduce the impacts of DMGD and MDL. An obvious way is to design and fabricate MDM system components covering a wide wavelength range with lower DMGD profiles (e.g., zero-DMGDslope FMF [83]) and lower MDL (e.g., a ring-core FM amplifier [85]). Another common strategy is to stimulate intermode mixing in the optical domain [86], [87] or the digital domain [88]. Managing DMGD profile along a transmission link is analogous to CD management in a single-mode fiber link and was introduced in a threespatial-mode MDM transmission experiment with a longer reach of 3500 km [89] and one with an enhanced capacity of 159 Tb/s over *C* + *L*-bands [90]. In these experiments, an end-to-end cumulative DMGD was carefully designed to be minimized by concatenating fiber segments with different DMGD profiles. As a counterpart approach, the use of cyclic mode permutation (CMP) was proposed in [84] where forced mode interchanges in each span were carried out to achieve a first-ever transoceanic-class MDM transmission over 6300 km. In MDM transmission with the CMP technique, it is expected that the MDM transmission regime is converted from weak coupling to "quasi"-strong coupling, consequently greatly relaxing a requirement for MIMO-DSP computational load. The CMP technique was further investigated for the application to MDM transmission links supporting propagation of several mode groups or wideband MDM transmission, achieving the longest six-spatial-mode MDM transmission over 3250- [91] and 3060-km three-spatial-mode MDM transmissions with the capacity of 40.2 Tb/s across the full *C*-band [92]. As a digital approach for DMGD-impact mitigation, parallel processing of low symbol rate signals in conjunction with frequency-domain MIMO equalization was shown to reduce a required computational complexity to 1.5% relative to that of conventional time-domain processing in a 527-km 12-core three-spatial-mode transmission [49]. In [93], a digital interference canceler was proposed to remove intermode interference to tackle MDLinduced orthogonality loss of spatial channels, thereby

![](_page_13_Picture_1.jpeg)

Fig. 22. Map of the fiber-optic infrastructure of L'Aquila. The 6-km green ring is deployed in a multiservice underground tunnel (in the historical downtown area). The 20-km red ring consists of traditional ducts (surrounding the urban area).

achieving the longest dense SDM transmission with a spatial multiplicity of 36 with a distance of 3000 km over a 12-core three-spatial-mode fiber. While a high potential of the full-MIMO MDM approach has been demonstrated, further research is needed to bring MDM transmission technologies (connectivity and amplification [94]) into future transport systems.

4) FMF Cable Deployment in L'Aquila: An FMF cable was fabricated by the Prysmian Group, for the first time to the best of our knowledge, using graded-indexcore low-DMGD 15-spatial-mode fibers [63]. This 26-km dielectric optical cable was designed for duct installation technique. It has a standard structure composed of six 2.2-mm-diameter loose tubes (two of which contain four 15-spatial-mode fibers) disposed around a 2.4-mm-diameter central strength member. The cable's outer diameter is 13 mm, and its weight is 195 kg/km. It is compliant with the mechanical specifications of IEC 60794-1-21. It is part of the fiber-optic infrastructure in the city center of L'Aquila, developed within the INCIPCT project [95]. The cable has been deployed for 6.1 km of its length in an underground tunnel underneath the historical city center, mostly in the same path as a multicore-fiber cable supplied by Sumitomo Electric [96], and it is fully functional. The remaining 20 km will be installed in traditional ducts to be deployed around the city center in 2023

(see Fig. 22). The eight 15-spatial-mode fibers contained in the deployed 6.1-km cable have been spliced together to yield a total span length of 48.8 km. To couple light both into and out of the 15-mode-spatial fibers, the two ends of the span have been spliced to a pair of Cailabs mode multiplexers based on MPLC (see Section II-C1).

The FMF cable is available to the international research community for field trials and some interesting results have already been recently reported [97], [98]. Equipment can be shipped to L'Aquila as a supplement to that available therein, and experiments can be performed. Accumulating data on MDM transmissions in cables will lay the ground for future deployments.

#### IV. CONCLUSION

Mode-division multiplexing (MDM) using FMFs that have a standard cladding diameter of 125  $\mu m$  and are made with standard manufacturing processes is a promising technology to increase fiber capacity by a few orders of magnitude and sustain the traffic demand for the decades to come.

In the weakly coupled category that is more suited to short-reach applications, MGDM with IM-DD and with-out MIMO processing has enabled 200-Gb/s bidirectional transmission over 20 km, and the same technique has been deployed to multiply the capacity of MMF-based LANs by a factor of 400. MDM with coherent detection and simple  $2 \times 2$  and  $4 \times 4$  MIMO equalization has reached a record capacity of 402.7 Tb/s over 48 km using ten spatial modes, and real-time experiments that lay the ground to actual deployments have also been reported.

In the full-MIMO category that is more suited to long-reach applications, MDM with coherent detection has allowed demonstrating several records: spectral efficiency of 202 b/s/Hz over 26.5 km with 45 spatial modes (90  $\times$  90 MIMO), the capacity of 1.01 Pb/s over 23 km with 15 spatial modes (30  $\times$  30 MIMO), and a distance of 3250 km with six spatial modes (12  $\times$  12 MIMO). Also, a 15-spatial-mode cable, which is part of the fiber-optic infrastructure of L'Aquila, already allows performing field MDM transmissions, which will enable a further step toward future deployed MDM transmission systems.

All these demonstrations show how active the research is to develop ever improved MDM fibers and systems that already allow for practical deployments.

#### REFERENCES

- S. Inao, T. Sato, S. Sentsui, T. Kuroha, and Y. Nishimura, "Multicore optical fiber," in *Proc. Opt. Fiber Commun. Conf.*, 1979, pp. 1–3, Paper WB1.
- [2] S. Berdagué and P. Facq, "Mode division multiplexing in optical fibers," Appl. Opt., vol. 21, no. 11, pp. 1950–1955, 1982.
- [3] S. Matsuo *et al.*, "Large-effective-area ten-core fiber with cladding diameter of about 200 μm," *Opt. Lett.*, vol. 36, no. 23, pp. 4626–4628, 2011.
- [4] P. Sillard, "Few-mode-fiber developments and applications," in Proc. 23rd Opto-Electron. Commun. Conf. (OECC), Jul. 2018, pp. 1–3, Paper 3C1-2.
- [5] T. Sakamoto, T. Mori, T. Yamamoto, and S. Tomita, "Differential mode delay managed transmission

- line for wide-band WDM-MIMO system," in *Proc. Opt. Fiber Commun. Conf.*, 2012, pp. 1–3, Paper OTh3I.4.
- [6] K. Jespersen, Z. Li, L. Grüner-Nielsen, B. Pálsdóttir, F. Poletti, and J. W. Nicholson, "Measuring distributed mode scattering in long, few-moded fibers," in *Proc. Opt. Fiber Commun. Conf.*, 2012, pp. 1–3, Paper OTh31.4.
- [7] R. Maruyama, N. Kuwaki, S. Matsuo, and M. Ohashi, "Relationship between mode coupling and fiber characteristics in few-mode fibers analyzed using impulse response measurements technique," J. Lightw. Technol., vol. 35, no. 4, pp. 650–657, Sep. 13, 2017.
- [8] P. Sillard, M. Bigot-Astruc, D. Boivin, H. Maerten, and L. Provost, "Few-mode fiber for uncoupled mode-division multiplexing transmissions," in Proc. 37th Eur. Conf. Expo. Opt. Commun., 2011, pp. 1–3, Paper Tu.S.LeCervin.7.
- [9] P. Sillard, M. Bigot-Astruc, and D. Molin, "Few-mode fibers for mode-division-multiplexed systems," *J. Lightw. Technol.*, vol. 32, no. 16, pp. 2824–2829, Aug. 15, 2014.
  [10] Y. Wakayama, D. Soma, K. Igarashi, H. Taga, and
- [10] Y. Wakayama, D. Soma, K. Igarashi, H. Taga, and T. Tsuritani, "Experimental characterization of step-index few-mode fiber for weakly-coupled 10-mode-multiplexed transmission," in Proc. Opto-Electron. Commun. Conf. (OECC) Photon.

- *Global Conf. (PGC)*, Jul. 2017, pp. 1–3, Paper 31K-4. [11] M. Bigot-Astruc, D. Molin, K. De Jongh, D. Van Ras, F. Achten, and P. Sillard, "Next-generation multimode fibers for space division multiplexing," in *Proc. Photon. Netw. Devices*, 2017, pp. 1–3, Paper NeM3B.4.
- [12] P. Sillard, "Few-mode fibers for space division multiplexing," in *Proc. Opt. Fiber Commun. Conf.*, 2016, pp. 1–3, Paper Th1J.1.
- [13] L. Ma *et al.*, "Ring-assisted 7-LP-mode fiber with ultra-low intermode crosstalk," in *Proc. Asia Commun. Photon. Conf.*, 2016, pp. 1–3, Paper AS4A.5.
- [14] D. Ge *et al.*, "Design of a weakly-coupled ring-core FMF and demonstration of 6-mode 10-km IM/DD transmission," in *Proc. Opt. Fiber Commun. Conf.*, 2018, pp. 1–3, Paper W4K.3.
- [15] P. Sillard, "Advances in few-mode fiber design and manufacturing," in *Proc. Opt. Fiber Commun. Conf. (OFC)*, 2020, pp. 1–3, Paper W1B.4.
- [16] G. Labroille *et al.*, "30 Gbit/s transmission over 1 km of conventional multi-mode fiber using mode group multiplexing with OOK modulation and direct detection," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2015, pp. 1–3, Paper p. 5.12.
- [17] H. S. Chen, H. P. A. van den Boom, and A. M. J. Koonen, "30 Gbit/s 3 *×* 3 optical mode group division multiplexing system with mode-selective spatial filtering," in *Proc. Opt. Fiber Commun. Conf./Nat. Fiber Optic Eng. Conf.*, 2011, pp. 1–3, Paper OWB1.
- [18] C. Simonneau, A. D'Amato, P. Jian, G. Labroille, J.-F. Morizur, and G. Charlet, "4*×*50 Gb/s transmission over 4.4 km of multimode OM2 fiber with direct detection using mode group multiplexing," in *Proc. Opt. Fiber Commun. Conf.*, 2016, pp. 1–3, Paper Tu2J.3.
- [19] M. Bigot-Astruc *et al.*, "Weakly-coupled 6-LP-mode fiber with low differential mode attenuation," in *Proc. Opt. Fiber Commun. Conf. (OFC)*, 2019, pp. 1–3, Paper M1E.3.
- [20] K. Benyaha *et al.*, "5 Tb/s transmission over 2.2 km of multimode OM2 fiber with wavelength and mode group multiplexing and direct detection," in *Proc. Opt. Fiber Commun. Conf.*, 2017, pp. 1–3, Paper M2D.2.
- [21] J.-F. Morizur *et al.*, "Programmable unitary spatial mode manipulation," *J. Opt. Soc. Amer. A, Opt. Image Sci.*, vol. 27, no. 11, pp. 2524–2531, 2010.
- [22] G. Labroille *et al.*, "Efficient and mode selective spatial mode multiplexer based on multi-plane light conversion," *Opt. Exp.*, vol. 22, no. 13, pp. 15599–15607, 2014.
- [23] K. Benyahya *et al.*, "14.5 Tb/s mode-group and wavelength multiplexed direct detection transmission over 2.2 km OM2 fiber," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2017, pp. 1–3, Paper Th.2.A.3.
- [24] G. Rademacher *et al.*, "10.66 peta-bit/s transmission over a 38-core-three-mode fiber," in *Proc. Opt. Fiber Commun. Conf. (OFC)*, 2020, pp. 1–3, Paper Th3H.1.
- [25] H. Liu *et al.*, "3*×*10 Gb/s mode group-multiplexed transmission over a 20 km few-mode fiber using photonic lanterns," in *Proc. Opt. Fiber Commun. Conf.*, 2017, pp. 1–3, Paper M2D.5.
- [26] K. Benyahya *et al.*, "200 Gb/s transmission over 20 km of FMF fiber using mode group multiplexing and direct detection," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2018, pp. 1–3, Paper Tu1G.5.
- [27] K. Benyahya *et al.*, "Multiterabit transmission over OM2 multimode fiber with wavelength and mode group multiplexing and direct detection," *J. Lightw. Technol.*, vol. 36, no. 2, pp. 355–360, Jan. 15, 2018.
- [28] G. Rademacher, R. S. Luís, B. J. Puttnam, Y. Awaji, and N. Wada, "Crosstalk dynamics in multi-core fibers," *Opt. Exp.*, vol. 25, no. 10, pp. 12020–12028, May 2017.
- [29] K. Choutagunta, I. Roberts, and J. M. Kahn, "Efficient quantification and simulation of modal dynamics in multimode fiber links," *J. Lightw. Technol.*, vol. 37, no. 8, pp. 1813–1825, Apr. 15, 2019.

- [30] K. Benyahya *et al.*, "Statistical characterization of intermodal crosstalk in direct detection schemes: M-PAM versus DMT," in *Proc. 45th Eur. Conf. Opt. Commun. (ECOC)*, 2019, pp. 1–3, Paper W.3.A.3.
- [31] F. M. Ferreira, C. S. Costa, S. Sygletos, and A. D. Ellis, "Semi-analytical modelling of linear mode coupling in few-mode fibers," *J. Lightw. Technol.*, vol. 35, no. 18, pp. 4011–4022, Sep. 15, 2017.
- [32] C. Koebele *et al.*, "40 km transmission of five mode division multiplexed data streams at 100 Gb/s with low MIMO-DSP complexity," in *Proc. 37th Eur. Conf. Expo. Opt. Commun.*, 2011, pp. 1–3, Paper Th13.C.3.
- [33] D. Soma *et al.*, "402.7-TB/S weakly-coupled 10-mode multiplexed transmission using rate-adaptive PS PDM-16QAM WDM signals," in *Proc. 45th Eur. Conf. Opt. Commun. (ECOC)*, 2019, pp. 1–3, Paper W.2.A.2.
- [34] S. Beppu *et al.*, "402.7-Tb/s MDM-WDM transmission over weakly coupled 10-mode fiber using rate-adaptive PS-16QAM signals," *J. Lightw. Technol.*, vol. 38, no. 10, pp. 2835–2841, May 15, 2020.
- [35] J. Cho, L. Schmalen, and P. J. Winzer, "Normalized generalized mutual information as a forward error correction threshold for probabilistically shaped QAM," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2017, pp. 1–3, Paper M.2.D.2.
- [36] F. Buchali, F. Steiner, G. Böcherer, L. Schmalen, P. Schulte, and W. Idler, "Rate adaptation and reach increase by probabilistically shaped 64-QAM: An experimental demonstration," *J. Lightw. Technol.*, vol. 34, no. 7, pp. 1599–1609, Apr. 1, 2016.
- [37] G. Labroille, P. Jian, N. Barré, B. Denolle, and J.-F. Morizur, "Mode selective 10-mode multiplexer based on multi-plane light conversion," in *Proc. Opt. Fiber Commun. Conf.*, 2016, pp. 1–3, Paper Th3E.5.
- [38] Y. Mori, C. Zhang, and K. Kikuchi, "Novel FIR-filter configuration tolerant to fast phase fluctuations in digital coherent receivers for higher-order QAM signals," in *Proc. Opt. Fiber Commun. Conf.*, 2012, pp. 1–3, Paper OTh4C.4.
- [39] K. Sugihara *et al.*, "A spatially-coupled type LDPC code with an NCG of 12 dB for optical transmission beyond 100 Gb/s," in *Proc. Opt. Fiber Commun. Conf./Nat. Fiber Optic Eng. Conf.*, 2013, pp. 1–3, Paper OM2B.4.
- [40] S. Bade *et al.*, "Fabrication and characterization of a mode-selective 45-mode spatial multiplexer based on multi-plane light conversion," in *Proc. Opt. Fiber Commun. Conf.*, 2018, pp. 1–3, Paper Th4B.3.
- [41] D. Soma *et al.*, "10.16-peta-B/s dense SDM/WDM transmission over 6-mode 19-core fiber across the C+L band," *J. Lightw. Technol.*, vol. 36, no. 6, pp. 1362–1368, Jan. 30, 2018.
- [42] B. Franz and H. Bulow, "Experimental evaluation of principal mode groups as high-speed transmission channels in spatial multiplex systems," *IEEE Photon. Technol. Lett.*, vol. 24, no. 16, pp. 1363–1365, Aug. 15, 2012.
- [43] B. Franz, L. Ali, L. Schmalen, and W. Idler, "High speed data transmission over GI-MMF using mode group division multiplexing," 2015, *arXiv:1501.02125*.
- [44] K. Lengle *et al.*, "4*×*10 Gbit/s bidirectional transmission over 2 km of conventional graded-index OM1 multimode fiber using mode group division multiplexing," *Opt. Exp.*, vol. 24, no. 25, pp. 18605–28594, 2016.
- [45] B. Inan *et al.*, "DSP complexity of mode-division multiplexed receivers," *Opt. Exp.*, vol. 20, no. 9, pp. 10859–10869, 2012.
- [46] K.-P. Ho and J. M. Kahn, "Statistics of group delays in multimode fiber with strong mode coupling," *J. Lightw. Technol.*, vol. 29, no. 21, pp. 3119–3128, Aug. 18, 2011.
- [47] C. Antonelli, A. Mecozzi, M. Shtaif, and P. J. Winzer, "Stokes-space analysis of modal dispersion in fibers with multiple mode transmission," *Opt. Exp.*, vol. 20, no. 11, pp. 11718–11733, 2012.
- [48] S. Arik, D. Askarov, and J. M. Kahn, "Effect of mode coupling on signal processing complexity in

- mode-division multiplexing," *J. Lightw. Technol.*, vol. 31, no. 3, pp. 423–431, Dec. 28, 2013.
- [49] K. Shibahara *et al.*, "Dense SDM (12-core *×* 3-mode) transmission over 527 km with 33.2-ns mode-dispersion employing low-complexity parallel MIMO frequency-domain equalization," *J. Lightw. Technol.*, vol. 34, no. 1, pp. 196–204, Jan. 1, 2016.
- [50] S. Randel *et al.*, "First real-time coherent MIMO-DSP for six coupled mode transmission," in *Proc. IEEE Photon. Conf. (IPC)*, Oct. 2015, pp. 1–3, Paper PD4.
- [51] K. Igarashi *et al.*, "Real-time weakly-coupled mode division multiplexed transmission over 48 km 10-mode fibre," in *Proc. 45th Eur. Conf. Opt. Commun. (ECOC)*, 2019, pp. 1–3, Paper W.2.A.3.
- [52] S. Beppu *et al.*, "Weakly coupled 10-mode-division multiplexed transmission over 48-km few-mode fibers with real-time coherent MIMO receivers," *Opt. Exp.*, vol. 28, no. 13, pp. 19655–19668, 2020.
- [53] S. Beppu *et al.*, "Real-time strongly-coupled 4-core fiber transmission," in *Proc. Opt. Fiber Commun. Conf. (OFC)*, 2020, pp. 1–3, Paper Th3H.2.
- [54] S. Beppu *et al.*, "Real-time transoceanic coupled 4-core fiber transmission," in *Proc. Opt. Fiber Commun. Conf. (OFC)*, 2021, pp. 1–3, Paper F3B.4.
- [55] G. Yeap *et al.*, "5 nm CMOS production technology platform featuring full-fledged EUV, and high mobility channel FinFETs with densest 0.021 μm<sup>2</sup> SRAM cells for mobile SoC and high performance computing applications," in *IEDM Tech. Dig.*, Dec. 2019, pp. 36.7.1–36.7.4.
- [56] L. Liu *et al.*, "Initial tap setup of constant modulus algorithm for polarization de-multiplexing in optical coherent receivers," in *Proc. Opt. Fiber Commun. Conf.*, 2009, pp. 1–3, Paper OMT2.
- [57] Y. Mori, C. Zhang, and K. Kikuchi, "Novel configuration of finite-impulse-response filters tolerant to carrier-phase fluctuations in digital coherent optical receivers for higher-order quadrature amplitude modulation signals," *Opt. Exp.*, vol. 20, pp. 26236–26251, Nov. 2012.
- [58] L. Grüner-Nielsen, Y. Sun, J. W. Nicholson, D. Jakobsen, R. Lingle, and B. Pálsdóttir, "Few mode transmission fiber with low DGD, low mode coupling and low loss," in *Proc. Opt. Fiber Commun. Conf.*, 2012, pp. 1–3, Paper PDP5A.1.
- [59] L. Grüner-Nielsen *et al.*, "Splicing of few mode fibers," in *Proc. Opt. Fiber Commun. Conf.*, 2014, pp. 1–3, Paper P. 1.15.
- [60] T. Mori *et al.*, "Few-mode fibers supporting more than two LP modes for mode-division-multiplexed transmission with MIMO DSP," *J. Lightw. Technol.*, vol. 32, no. 14, pp. 2468–2478, Jul. 15, 2014.
- [61] P. Sillard *et al.*, "Micro-bend-resistant low-differential-mode-group-delay few-mode fibers," *J. Lightw. Technol.*, vol. 35, no. 4, pp. 734–740, Feb. 15, 2017.
- [62] P. Sillard *et al.*, "Low-differential-mode-group-delay 9-LP-mode fiber," *J. Lightw. Technol.*, vol. 34, no. 2, pp. 425–430, Jan. 15, 2016.
- [63] D. Molin, M. Bigot-Astruc, A. Amezcua-Correa, and P. Sillard, "Recent advances on MMFs for WDM and MDM," in *Proc. Opt. Fiber Commun. Conf.*, 2018, pp. 1–3, Paper W3C.1.
- [64] P. Sillard, D. Molin, M. Bigot-Astruc, K. de Jongh, and F. Achten, "Rescaled multimode fibers for mode-division multiplexing," *J. Lightw. Technol.*, vol. 35, no. 8, pp. 1444–1449, Apr. 15, 2017.
- [65] P. Sillard, D. Molin, M. Bigot-Astruc, A. Amezcua-Correa, K. de Jongh, and F. Achten, "DMGD-compensated links," in *Proc. Opt. Fiber Commun. Conf.*, 2017, pp. 1–3, Paper Tu2J.4.
- [66] R. Ryf *et al.*, "Mode-division multiplexing over 96 km of few-mode fiber using coherent 6 *×* 6 MIMO processing," *J. Lightw. Technol.*, vol. 30, no. 4, pp. 521–531, Feb. 12, 2012.
- [67] R. Ryf *et al.*, "12 *×* 12 MIMO transmission over 130-km few-mode fiber," in *Proc. Frontiers Opt.*, 2012, pp. 1–3, Paper FW6C.4.
- [68] J. van Weerdenburg *et al.*, "10 spatial mode transmission using low differential mode delay 6-LP fiber using all-fiber photonic lanterns," *Opt. Exp.*, vol. 23, no. 19, pp. 24759–24769, 2015.
- [69] N. K. Fontaine *et al.*, "30*×*30 MIMO transmission

- over 15 spatial modes," in *Proc. Opt. Fiber Commun. Conf. Post*, 2015, pp. 1–3, Paper Th5C.1.
- [70] R. Ryf *et al.*, "Mode-multiplexed transmission over 36 spatial modes of a graded-index multimode fiber," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2018, pp. 1–3, Paper Tu1G.2.
- [71] R. Ryf *et al.*, "High-spectral-efficiency mode-multiplexed transmission over graded-index multimode fiber," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2018, pp. 1–3, Paper Th3B.1.
- [72] R. G. Van Uden *et al.*, "Time domain multiplexed spatial division multiplexing receiver," *Opt. Exp.*, vol. 22, no. 10, pp. 12668–12677, 2014.
- [73] N. K. Fontaine *et al.*, "Hermite-Gaussian mode multiplexer supporting 1035 modes," in *Proc. Opt. Fiber Commun. Conf. (OFC)*, 2021, pp. 1–3, Paper M3D.4.
- [74] N. K. Fontaine *et al.*, "Packaged 45-mode multiplexers for a 50-μm graded index fiber," in *Proc. Eur. Conf. Opt. Commun.*, 2018, pp. 1–3, Paper Mo4E.1.
- [75] N. K. Fontaine, R. Ryf, H. Chen, D. T. Neilson, K. Kim, and J. Carpenter, "Laguerre-Gaussian mode sorter," *Nature Commun.*, vol. 10, no. 1, p. 1865, Dec. 2019.
- [76] G. Rademacher *et al.*, "1.01 peta-bit/s C+L-band transmission over a 15-mode fiber," in *Proc. Eur. Conf. Opt. Commun.*, 2020, pp. 1–3, Paper Th3A-3.
- [77] G. Rademacher *et al.*, "Peta-bit-per-second optical communications system using a standard cladding diameter 15-mode fiber," *Nature Commun.*, vol. 12, no. 1, p. 4238, Dec. 2021.
- [78] F. Yaman *et al.*, "10 *×* 112 Gb/s PDM-QPSK transmission over 5032 km in few-mode fibers," *Opt. Exp.*, vol. 18, no. 20, pp. 21342–21349, 2010.
- [79] V. A. J. M. Sleiffer *et al.*, "73.7 Tb/s (96 *×* 3 *×* 256-Gb/s) mode-division-multiplexed DP-16QAM transmission with inline MM-EDFA," in *Proc. Eur. Conf. Opt. Commun.*, 2012, pp. 1–3, Paper Th.3.C.4.
- [80] E. Ip *et al.*, "146λ *×* 6 *×* 19-Gbaud wavelength-and mode-division multiplexed transmission over 10 *×* 50-km spans of few-mode

- fiber with a gain-equalized few-mode EDFA," *J. Lightw. Technol.*, vol. 32, no. 4, pp. 790–797, Nov. 19, 2013.
- [81] R. Ryf *et al.*, "Distributed Raman amplification based transmission over 1050-km few-mode fiber," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2015, pp. 1–3, Paper Tu.3.2.3.
- [82] J. M. Kahn, K.-P. Ho, and M. B. Shemirani, "Mode coupling effects in multi-mode fibers," in *Proc. Opt. Fiber Commun. Conf.*, 2012, pp. 1–3, Paper OW3.D3.
- [83] R. Maruyama *et al.*, "Two mode optical fibers with low and flattened differential modal delay suitable for WDM-MIMO combined system," *Opt. Exp.*, vol. 22, no. 12, pp. 14311–14321, 2014.
- [84] K. Shibahara *et al.*, "DMD-unmanaged long-haul SDM transmission over 2500-km 12-core *×* 3-mode MC-FMF and 6300-km 3-mode FMF employing intermodal interference cancelling technique," in *Proc. Opt. Fiber Commun. Conf.*, 2018, pp. 1–3, Paper Th4C.6.
- [85] H. Ono, T. Hosokawa, K. Ichii, S. Matsuo, and M. Yamada, "Improvement of differential modal gain in few-mode fibre amplifier by employing ring-core erbium-doped fibre," *Electron. Lett.*, vol. 51, no. 2, pp. 172–173, Jan. 2015.
- [86] J. Fang *et al.*, "Low-DMD few-mode fiber with distributed long-period grating," *Opt. Lett.*, vol. 40, no. 17, pp. 3937–3940, 2015.
- [87] H. Liu, H. Wen, R. Amezcua-Correa, P. Sillard, and G. Li, "Reducing group delay spread in a 9-LP mode FMF using uniform long-period gratings," in *Proc. Opt. Fiber Commun. Conf.*, 2017, pp. 1–3, Paper Tu2J.5.
- [88] K. Shibahara *et al.*, "Space-time coding-assisted transmission for mitigation of MDL impact on mode-division multiplexed signals," in *Proc. Opt. Fiber Commun. Conf.*, 2016, pp. 1–3, Paper Th4C.4.
- [89] G. Rademacher *et al.*, "3500-km mode-multiplexed transmission through a three-mode graded-index few-mode fiber link," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2017, pp. 1–3, Paper M.2.E.4.

- [90] G. Rademacher *et al.*, "159 Tbit/s C+L band transmission over 1045 km 3-mode graded-index few-mode fiber," in *Proc. Opt. Fiber Commun. Conf.*, 2018, pp. 1–3, Paper Th4C.4.
- [91] K. Shibahara *et al.*, "Long-haul DMD-unmanaged 6-mode-multiplexed transmission employing cyclic mode-group permutation," in *Proc. Opt. Fiber Commun. Conf.*, 2020, pp. 1–3, Paper Th3H.3.
- [92] K. Shibahara *et al.*, "Full C-band 3060-km DMD-unmanaged 3-mode transmission with 40.2-Tb/s capacity using cyclic mode permutation," in *Proc. Opt. Fiber Commun. Conf. (OFC)*, 2019, pp. 1–3, Paper W3F.2.
- [93] K. Shibahara *et al.*, "Iterative unreplicated parallel interference canceler for MDL-tolerant dense SDM (12-core *×* 3-mode) transmission over 3000 km," in *Proc. Eur. Conf. Opt. Commun.*, 2018, pp. 1–3, Paper Tu3F.6.
- [94] T. Mizuno, K. Shibahara, H. Ono, and Y. Miyamoto, "Long-distance PDM-32QAM 3-mode fibre transmission over 1000 km using hybrid multicore EDFA/Raman repeated amplification with cyclic mode permutation," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2018, pp. 1–3, Paper Mo3G.6.
- [95] C. Antonelli *et al.*, "The city of L'Aquila as a living lab: The INCIPICT project and the 5G trial," in *Proc. IEEE 5G World Forum (5GWF)*, Jul. 2018, pp. 410–415.
- [96] T. Hayashi *et al.*, "Field-deployed multi-core fiber testbed," in *Proc. 24th OptoElectron. Commun. Conf. (OECC) Int. Conf. Photon. Switching Comput. (PSC)*, Jul. 2019, pp. 1–3, Paper PDP 3.
- [97] R. S. Luís *et al.*, "Demonstration of a spatial super channel switching SDM network node on a field deployed 15-mode fiber network," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2022, Paper Th3B.5.
- [98] G. Rademacher *et al.*, "Characterization of the first field-deployed 15-mode fiber cable for high density space-division multiplexing," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, Sep. 2022, Paper Th3C.1.

#### **ABOUT THE AUTHORS**

**Pierre Sillard** (Member, IEEE) received the Engineering Diploma degree from Télécom ParisTech, Paris, France, in 1994, and the Ph.D. degree in optics from the University of Paris VI, Paris, in 1998, in collaboration with Thales Research & Technology, Palaiseau, France, with a focus on the subject of nonlinear interactions in laser resonators.

He has been working in the field of optical

fibers since 1999. He is currently with the Prysmian Group, Haisnes, France. He has been involved in the development and deployment of new fibers for fiber to the home (FttH), long haul, and local area networks. He has authored or coauthored more than 300 papers. He holds more than 100 patents. His research interests include modeling and characterizing optical fibers and systems.

Dr. Sillard is a member of the IEEE and OPTICA Societies. He serves as a reviewer and a committee member of several journals and conferences. In 2004, he received the TR35 Innovator Award from the MIT Technology Review. He was the Technical Program Committee Co-Chair of the European Conference on Optical Communication (ECOC) 2021.

**Kaoutar Benyahya** received the Engineering degree in photonics from ENSSAT, Lannion, France, in 2016, and the Ph.D. degree in optical communication systems from the University of Rennes 1, Rennes, France, in 2019. Her Ph.D. degree was focused on increasing capacity over multimode fibers for short-reach optical communication systems based on mode group-division multiplexing.

Her main research interests span from short-reach to ultralonghaul optical communication systems, including space-division multiplexing, wavelength-division multiplexing transmissions, digital signal processing, and optical system design for low-cost direct detection and coherent schemes.

Dr. Benyahya received the Best Student Paper Award at the European Conference on Optical Communication (ECOC) 2017.

![](_page_15_Picture_40.jpeg)

He joined KDDI Corporation, Tokyo, Japan, in 2012. Since 2013, he has been working with KDDI R&D Laboratories, Inc. (currently KDDI Research, Inc.), Saitama, Japan, and has been engaged in research on space-

![](_page_15_Picture_42.jpeg)

division multiplexed optical fiber transmission systems. Mr. Soma was a recipient of the 2017 Institute of Electronics, Information and Communication Engineers (IEICE) Communications Society OCS Young Researchers Award in 2017, the Young Researcher's Award of IEICE in 2018, and the 2020 IEICE Communications Society OCS Best Paper Award in 2020.

**Guillaume Labroille** graduated from Télécom ParisTech, Paris, France. He received the Ph.D. degree in physics from the École Polytechnique, Palaiseau, France, in 2011.

He cofounded Cailabs, Rennes, France, during his postdoctorate at the Kastler Brossel Laboratory, Paris, in 2013. As the Chief Technical Officer, he is responsible for the research and development of the company's new products and protecting the related intellectual property rights.

**Pu Jian** graduated in quantum optics from the École Normale Supérieure, Paris, France, and the Ph.D. degree from Sorbonne University, Paris, and the École Normale Supérieure.

As the VP of Product Management and Partnerships, she has launched all of Cailabs' award-winning products and defined their marketing strategy since joining the company in 2014. She manages the cooperation between Cailabs, Rennes, France, and its strategic partners.

**Koji Igarashi** received the B.E. degree in electrical and computer engineering from Yokohama National University, Yokohama, Japan, in 1997, and the M.E. and Ph.D. degrees in electronic engineering from The University of Tokyo, Tokyo, Japan, in 1999 and 2002, respectively.

From 2002 to 2004, he was with Furukawa Electric Corporation, Ltd., Chiba, Japan. Since 2004, he has been with The University of Tokyo. From 2007 to 2011, he was an Assistant Professor earlier with the Department of Frontier Informatics and then the Department of Electrical Engineering and Information Systems, The University of Tokyo. From 2012 to 2013, he was with KDDI R&D Laboratories, Inc., Saitama, Japan. He is currently an Associate Professor with the Department of Electrical, Electronic and Info-Communications Engineering, Osaka University, Osaka, Japan. His current research interests include high-capacity long-haul optical fiber transmission systems, signal processing for coherent optical communication systems, and optical measurement techniques.

**Roland Ryf** (Fellow, IEEE) received the Diploma degree in electrical engineering from the University of Applied Sciences (NTB), Buchs, Switzerland, and the Diploma and Ph.D. degrees in physics from the Swiss Federal Institute of Technology, ETH Zürich, Zürich, Switzerland, with a focus on the photorefractive effects and its applications in optical storage and fast optical correlation.

![](_page_16_Picture_8.jpeg)

After joining Nokia Bell Labs, New Providence, NJ, USA, in 2000, he worked on MEMS-based large port-count optical cross-connect switches and high-resolution optical wavelength filters. In addition, he worked on MEMS-based infrared cameras with optical readout

and laser-based microprojectors. Since 2009, he has been working on multimode and multicore components, wavelength-selective switches and optical amplifiers, and numerous first experimental demonstrations of long-distance high-capacity space-division multiplexed transmission over multimode fibers and coupled-core multicore fibers. He authored/coauthored over 250 journal and conference publications. He holds over 50 patents.

Dr. Ryf is a Fellow of the Optical Society of America. He is a Bell Labs Fellow. He was a recipient of the 2018 IPS William Streifer Scientific Achievement Award.

**Nicolas K. Fontaine** (Fellow, IEEE) received the Ph.D. degree in electrical engineering from the Next Generation Network Systems Laboratory, University of California at Davis, Davis, CA, USA, in 2010. In his dissertation, he studied how to generate and measure the amplitude and phase of broadband optical waveforms in many narrowband spectral slices.

Since June 2011, he has been a Technical Staff Member with the Advanced Photonics Division, Bell Laboratories, Crawford Hill, NJ, USA. At Bell Laboratories, he develops devices for space-division multiplexing in multicore and few-mode fibers, builds wavelength cross-connects and filtering devices, and investigates spectral slice coherent receivers for THz bandwidth waveform measurement.

**Georg Rademacher** (Senior Member, IEEE) received the Dipl.Ing. and Dr.Ing. degrees from Technische Universität Berlin, Berlin, Germany, in 2011 and 2015, respectively.

Since 2016, he has been with the National Institute of Information and Communications Technology (NICT), Tokyo, Japan, where he is currently a Senior Researcher. His research focuses on systems and subsystems for high-capacity optical fiber transmission systems, primarily by applying space-division multiplexing.

Dr. Rademacher is a Senior Member of the IEEE Photonics Society and a member of the Verband Deutscher Elektrotechniker (VDE). He received the 2017 ITG Award from the VDE, Germany, the Best Paper Award at the 2018 Photonics in Switching and Computing (PSC) Conference, and the 2020 Maejima Hisoka Award.

**Kohki Shibahara** (Member, IEEE) received the B.S. degree in physics, the M.S. degree in geophysics, and the Ph.D. degree in informatics from Kyoto University, Kyoto, Japan, in 2008, 2010, and 2017, respectively.

He joined the NTT Network Innovation Laboratories, Yokosuka, Japan, in 2010. His current research interests include spatialdivision multiplexing transmission systems and advanced multipleinput–multiple-output signal processing.

Dr. Shibahara is a member of the Institute of Electronics, Information and Communication Engineers (IEICE) and the IEEE/Photonics Society. He received the Tingye Li Innovation Prize from the OPTICA in 2016 and the Young Researcher's Award from the IEICE in 2017.
---
title: "Advanced Technologies for Next-Generation Passive Optical Networks"
tema_principal: pon
temas_relacionados: []
ano: null
autores: []
veiculo: null
pdf: ../pdf/advanced_technologies_for_next-generation_passive_optical_networks.pdf
---

# Advanced Technologies for Next-Generation Passive Optical Networks

Md Saifuddin Faruk School of Computer Science and Engineering Bangor University Bangor, U.K. m.faruk@bangor.ac.uk

Wei Jin School of Computer Science and Engineering Bangor University Bangor, U.K. w.jin@bangor.ac.uk

Jianming Tang School of Computer Science and Engineering Bangor University Bangor, U.K. j.tang@bangor.ac.uk

*Abstract***—This paper provides an overview and recent advancement of emerging technologies including transceivers, flexibility features, optical sensing and physical layer security for next-generation passive optical networks (PON).**

*Keywords—passive optical network, digital signal processing, simplified coherent transceivers, distributed fiber optic sensing, physical layer security.* 

## I. INTRODUCTION

The most recent passive optical network (PON) standardization by the International Telecommunication Union-Telecommunications Standardization Sector (ITU-T) considers a rate of 50 Gb/s/λ [1]. Though this standard still considers intensity modulation/ direction (IM/DD) with on-off keying (OOK) format, the use of digital signal processing (DSP) in the transceiver is considered for the first time. Moving forward, ITU-T initiated a new project on very highspeed PON (VHSP) systems, named G.suppl.VHSP which aims to collect system requirements, characteristics, and candidate technologies for future PON systems beyond 50 Gb/s [2].

Though 100 Gb/s per channel is a popular design choice, following the four-fold increase in bandwidth between two PON standards, the next step after 50 Gb/s could be 200 Gb/s/λ [3]. The IM/DD-based PON struggles to achieve the required loss budget at such a high line rate. Thus, the coherent transceivers might be the rational choice for next-generation PON considering their inherent high sensitivity and ability to compensate fiber transmission impairments using DSP [4]. The introduction of coherent transceivers and advanced DSP could thus allow additional functionalities in future PON like monitoring and sensing.

This paper first describes the potential transceiver technologies for the PON for a line rate beyond 50 Gb/s. Then we explore the concept of flexible PON where the flexibility can be achieved at the physical layer, higher layer, or even in the optical distribution network (ODN). After that, the progress of monitoring and sensing technologies for PON is described. Finally, the enabling technologies for the physical layer security are presented.

# II. TRANSCEIVER TECHNOLOGIES

Different transceiver technologies have been investigated for PON applications at 100 Gb/s and beyond. Those can be broadly classified as below:

## *A. Intensity Modulation/ Direct-Detection*

There are several demonstrations of IM/DD PON at 100 Gb/s/λ achieving the required loss budget [5, 6, 7, 8]. The key features used to achieve a higher power budget include the use of (i) PAM-4 modulation format instead of OOK to increase the spectral efficiency, (ii) a nonlinear equalizer to reduce the impact of transceiver bandwidth limitation and nonlinearity, (iii) a booster amplifier to launch more power into the fiber, and (iv) an SOA plus PIN or an APD as the receiver. There are few research investigations into 200 Gb/s/λ IM/DD solutions [9, 10]; however, they require expensive components and highly computationally complex DSP and thus that makes it challenging to implement in a commercial PON application.

## *B. Intensity Modulation/ Coherent Detection*

An intensity modulation at the optical line terminal (OLT) side to reduce the coherent receiver DSP complexity at the optical network unit (ONU) side has been demonstrated for 200 Gb/s PON [11]. However, a more rational choice is to use a simple intensity modulator at the cost-sensitive ONU side, while using a coherent receiver at the OLT side where the cost is shared among the users [12].

## *C. Coherent/ Simplified Coherent Transceivers*

Though a dual polarization intradyne coherent receiver, commonly used for core networks, has been demonstrated for access networks with superior performance, implementing such transceivers in PON application may be challenging due to higher costs [13]. Therefore, the design of simplified coherent receivers for PON has attracted significant attention in recent years [14].

Two key techniques enable the simplification of coherent receivers. Firstly, using a heterodyne detection at the expense of a larger receiver bandwidth requirement. Heterodyne detection not only allows halving the optoelectronic components compared to the intradyne receiver but also 90<sup>0</sup> optical hybrids can be replaced by simpler 3-dB couplers. Secondly, to remove the polarization diversity to construct a single polarization receiver, which further halves the optoelectronic components, but at the expense of reduced spectral efficiency. Thus, the single-polarization heterodyne receiver is a lite coherent receiver requiring only a 3-dB coupler and a single balanced photodiode [15]. Replacing the balanced photodiode with a single-ended photodiode constructs the minimal coherent receiver having a comparable complexity to that of a direct detection receiver [16]. However, the receiver sensitivity is decreased in such a case.

To achieve the polarization-insensitive operation of the simplified single-polarization receiver, it is desirable to implement the polarization diversity at the transmitter side, *i.e.* at OLT. There are several ways to attain that such as polarization scrambling, DGD-pre distortion, Alamouticoding, etc. [17]. Among these approaches, the Alamouti coding proves the best performance in terms of performance variation with the state of polarization (SOP) of the incoming signal [18].

## III. FLEXIBLE PON

So far the deployed PON has a fixed network design to serve the worst-case scenario; for example, considering the ONU at the furthest distance. Likewise, very limited flexibility options are available in the PON standards. The recent ITU-T 50 Gb/s standard has adopted dispersion eye closure (TDEC) measurement that enables flexibility to trade off the quality of transmission and minimum launch power [1]. It also allows flexible forward error correction (FEC) for upstream transmission.

The inclusion of DSP in recent standards drives research interest in flexible PON which can be achieved in various ways. For example, flexibility can be introduced in the physical media dependent (PMD) layer with different modulation formats or transmission convergence (TC) layer with variable FEC code rate [19]. It can also be achieved at the transceivers such as using a time-and-frequency-division multiplexing (TFDM) PON architecture based on digital subcarrier multiplexing technology [20]. Finally, the flexible rate PON can be further extended in the ODN level, for example, by using adjustable variable splitters (AVSs) inside the ODN and then the power for each ONU is adjusted according to the desired power distribution [21].

Though there are different ways to introduce flexibility in a PON, often the flexibility features introduce complexity and thus additional cost which might be challenging in the costconstraint PON applications. Therefore, choosing flexible features where the cost is low or can be recovered by the operator is important.

## IV. OPTICAL SENSING FOR PON

Recently distributed fiber optic sensing (DFOS) gained significant research interest in monitoring the optical network and the civil infrastructures around the fiber. However, the use of DFOS in a point-to-multipoint PON scenario is challenging for several reasons. Measuring the backscatter signal is difficult as it is very weak after a passive splitter due to the high losses. In addition, there is an ambiguous result beyond the splitter due to the superimposing of back-scattered and back-reflected light from all drop fibers. Also, the use of commercial DFOS is too expensive in the cost-sensitive PON scenario.

Several demonstrations of sensing applications in the PON using DFOS are available. In [22], a reflective semiconductor optical amplifier (RSOA) was used at each ONU. To monitor a particular ONU, the RSOA of that ONU is turned on to amplify and reflect the sensing pulse. However, this approach requires modification of ONU with additional components and a control arrangement to turn on a particular RSOA. An enhanced scatter fiber (ESF) in the distribution link was used in [23] to enable distributed acoustic sensing. However, this approach requires ODN modification by replacing the SMF fiber in the distribution link with ESF. Vibration monitoring in a PON was also reported using an interferometry-based sensing interrogator with two fibers and Faraday rotator mirrors (FRM) at ONU [24]. Again such an approach requires modification in the ODN.

As coherent technology might be used in the future PON, low-cost DSP-based sensing such as monitoring of polarization state and digital longitudinal monitoring [25] might be a possibility for an efficient sensing approach for PON.

## V. PHYSICAL LAYER SECURITY

In a PON, the downstream signal is broadcasted to all the ONUs making it vulnerable to eavesdropping. Therefore, the security problem in the PON application is a key concern and as such the ITU-T SG15/Q2 group has already initiated the work item G.sup.PONsec which will deal with the practical aspects of PON security [26].

Unlike high-layer encryption techniques, the physical layer security techniques can protect the data without introducing any extra transmission overhead and increasing latency. For PON, several physical layer encryption techniques are investigated including quantum key distribution (QKD) [27, 28] and chaos communications [29, 30]. The QKD techniques use the fundamentals of quantum mechanics to produce shared random secret keys, which are unconditionally protected from eavesdroppers. The chaos communication techniques utilize unpredictable and noiselike optical chaotic carriers to mask the transmitted information. However, both techniques suffer from several disadvantages, including limited rates of communication data or key distribution, stringent requirements on optical devices, high overall costs, and their suitability for point-to-point transmission systems.

To cost-effectively address the technical challenges associated with the abovementioned schemes, recently, we have proposed a new physical layer security method by employing chaotic digital filters [31, 32]. It utilizes a 'noiselike' orthogonal frequency-division multiplexing (OFDM) signals as unique private security keys.

The proposed PLS system can deliver three unique features. Firstly, *security-by-design*, as chaotic digital filters are implemented in transceivers in the designed stage. Secondly, *openness-by-design*, due to the ease of its interoperability across various vendors' equipment. Thirdly, *dynamic security at the traffic level*, as it allows traffic to be selected dynamically to enable/disable the security without interrupting the traffic flow of the whole network.

# VI. CONCLUSION

Introducing the advanced DSP and coherent transceivers will enable new functionalities and technologies in the next generation of PONs. In this paper, we have summarized the research progress and challenges of such emerging technologies.

## ACKNOWLEDGMENT

This work has been partly funded by the Engineering and Physical Sciences Research Council Project TITAN [EP/Y037243/1].

## REFERENCES

- [1] ITU-T Recommendation, "50-Gigabit-capable passive optical networks (50G-PON): PMD layer specification," G.9804.3, 2021.
- [2] ITU-T Recommendation, "PON transmission technologies above 50 Gb/s per wavelength," G.suppl.VHSP, 2023.
- [3] P. Torres-Ferrera, F. Effenberger, M. S. Faruk, Seb J. Savory, and R. Gaudino,, "Overview of high-speed TDM-PON beyond 50 Gbps per wavelength using digital signal processing [Invited Tutorial]," *J. Opt. Commun. Netw.,* vol. 14, no. 12, pp. 982-996 , 2022.
- [4] M. S. Faruk et al., "Coherent passive optical networks: why, when, and how," *IEEE Comm. Mag.,* vol. 59, no. 12, pp. 112-117, 2021.

- [5] J. Zhang et al., "SOA pre-Amplified 100 Gb/S/Λ PAM-4 TDM-PON downstream transmission using 10 Gbps O-Band transmitters," *J. Lightw. Technol.,* vol. 38, no. 2, pp. 185-193, 2020.
- [6] K. Wang et al., "100-Gbit/s/λ PAM-4 signal transmission over 80 km SSMF based on an 18-GHz EML at O-band," in *Proc. Opt. Fiber Commun. (OFC)*, pp. 1-3, 2020.
- [7] L. Xue et al., "100G PAM-4 PON with 34 dB power budget using joint nonlinear Tomlinson-Harashima precoding and volterra equalization," in *Proc. Eur. Conf. Opt. Commun. (ECOC)*, pp. 1-4, 2021.
- [8] G. Caruso, I. N. Cano, D. Nesset, G. Talli, and R. Gaudino,, "Realtime 100 Gb/s PAM-4 for access links with up to 34 dB power budget," *J. Lightw. Technol.,* vol. 41, no. 11, pp. 3491-3497, 2023.
- [9] J. Li, X. Zhang, M. Luo, C. Yang, Z. He, and X. Xiao, "SOA preamplified 200 Gb/s/λ PON using high-bandwidth TFLN modulator," in *Proc. Eur. Conf. Opt. Comm. (ECOC)*, pp. 1-3, 2022.
- [10] R. Borkowski et al., "200G IM/DD time-and-polarization-divisionmultiplexed PON with >29dB power budget using boosted EML and APDs," in *Proc. Opt. Fib. Comm. (OFC)*, p. Th1E.5, 2024.
- [11] J. Zhang, "200 Gbit/s/λ PDM-PAM-4 PON system based on intensity modulation and coherent detection," *J. Opt. Commun. Netw.,* vol. 12, no. 1, pp. A1-A8, 2020.
- [12] I. B. Kovacs, M. S. Faruk, P. Torres-Ferrera and S. J. Savory, "Simplified coherent optical network units for very-high-speed passive optical networks," *J. Opt. Commun. Netw.,* vol. 16, no. 7, pp. C1-C10, 2024.
- [13] J. Zhang and Z. Jia, "Coherent passive optical networks for 100G/λand-beyond fiber access: recent progress and outlook," *IEEE Netw.,*  vol. 36, no. 2, pp. 116-123, 2022.
- [14] I. B. Kovacs, M. S. Faruk and S. J. Savory, "Simplified coherent receivers for passive optical networks," in *Eur. Conf. Opt. Commun. (ECOC)*, pp. 1182-1185, 2023.
- [15] M. S. Faruk, X. Li, and S. J. Savory, "Experimental demonstration of 100/200-Gb/s/λ PON downstream transmission using simplified cohernt receivers," in *Opt. Fib. Commun. Conf.*, p. Th3E.5, 2022.
- [16] I. B. Kovacs, M. S. Faruk and S. J. Savory, ""A minimal coherent receiver for 200 Gb/s/λ PON downstream with measured 29 dB power budget," *IEEE Photon. Technol. Lett.,* vol. 35, no. 5, pp. 257- 260, 2023.
- [17] M. S. Faruk and Seb J. Savory, "Coherent access: status and opportunities," in *IEEE Photon. Soc. Sum. Topic. Meet.*, pp. 1-2, 2020.
- [18] M. S. Faruk, H. Louchet, M. S. Erkılınç, and Seb J. Savory, "DSP algorithms for recovering single-carrier Alamouti coded signals for PON applications," *Opt. Exp.,* vol. 24, no. 21, pp. 24083-24091, 2016.
- [19] R. Borkowski et al., "FLCS-PON A 100 Gbit/s flexible passive optical network: concepts and field trial," *J. Lightw. Technol.,* vol. 39, no. 16, pp. 5314-5324, 2021.

- [20] J. Zhang, Z. Jia, H. Zhang, M. Xu, J. Zhu and L. A. Campos, "Rateflexible single-wavelength TFDM 100G coherent PON based on digital subcarrier multiplexing technology," in *Opt. Fib. Commun. Conf. (OFC)*, pp. 1-3, 2020.
- [21] M. Straub, A. Mahadevan, and R. Bonk, "Flexible-rate PON with loss-configurable ODN splitters for throughput optimization," in *Eur. Conf. Opt. Commun. (ECOC)*, p. Tu.C.3.4, 2023.
- [22] E. Ip, Y. Huang, M. Huang, M. Salemi, Y. Li, T. Wang, Y. Aono, G. A. Wellbrock, and T. J. Xia, "Distributed fiber sensor network using telecom cables as sensing media: applications," in *Opt. Fib. Commun. Conf. (OFC)*, paper Tu6F.2, 2021.
- [23] B. Zhu, P. Westbrook, K. Feder, Z. Shi, P. Lu, R. Dyer, X. Sun, J. Li, D. Peterson, and D. J. DiGiovanni, "Distributed acoustic sensing over passive optical networks using enhanced scatter fiber," in *Opt. Fib. Commun. Conf. (OFC)*, p. M1K.1, 2024.
- [24] I. Luch, et al., "Demonstration of structural vibration sensing in a deployed PON infrastructure," in *Eur. Conf. Opt. Commun. (ECOC)*, p. We1E2, 2019.
- [25] M. S. Faruk and S. J. Savory, "Measurement informed models and digital twins for optical fiber communication systems," *J. Lightw. Technol.,* vol. 42, no. 3, pp. 1016-1030, 2024.
- [26] ITU-T recommendation, "Practical aspects of PON security," in *G.sup.PONsec*, 2024-2027.
- [27] B. Fröhlich et al., "Quantum secured gigabit optical access networks," *Sci. Rep.,* vol. 5, p. 18121, 2015.
- [28] H. Wang, Y. Zhao, M. Tornatore, X. Yu, and J. Zhang, "Dynamic secret-key provisioning in quantum-secured passive optical networks (PON)," *Opt. Exp.,* vol. 29, no. 2, p. 1578–1596, 2021.
- [29] W. Zhang, C. Zhang, C. Chen, H. Zhang, W. Jin and K. Qiu, "Hybrid chaotic confusion and diffusion for physical layer security in OFDM-PON," *IEEE Photon. J.,* vol. 9, no. 2, p. 7201010, 2017.
- [30] J. Ren et al., "Chaotic constant composition distribution matching for physical layer security in a PS-OFDM-PON," *Opt. Exp.,* vol. 28, no. 26, pp. 39266-39276, 2020.
- [31] J. Tang, "DSP-enabled subsystem and system solutions for realising converged access networks with improved performances and new functionalities," in *Asia Commun. Photon. Conf. (ACP)*, p. ACPPOEM-1010-1, 2023.
- [32] J. He, W. Jin, R. P. Gidding and J. Tang, "Chaotic digital filter-based physical layer security for heterogeneous access networks," in *Asia Commun. Conf. (ACP)*, Submitted, 2024.
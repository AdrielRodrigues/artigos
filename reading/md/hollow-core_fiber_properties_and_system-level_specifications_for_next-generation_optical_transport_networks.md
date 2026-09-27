---
title: "Hollow-Core Fiber Properties and System-Level Specifications for Next-Generation Optical Transport Networks"
tema_principal: reading
temas_relacionados: []
ano: 2026
autores: []
veiculo: null
pdf: ../pdf/hollow-core_fiber_properties_and_system-level_specifications_for_next-generation_optical_transport_networks.pdf
---

![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

## Article

# Hollow-Core Fiber Properties and System-Level Specifications for Next-Generation Optical Transport Networks

Bruno Correia and João Pedro

# Special Issue

[Specialty Optical Fibers: Advances in Design, Fabrication, Performance and Applications](https://www.mdpi.com/journal/photonics/special_issues/P8E5SS6XHK)

Edited by

Dr. Antonella Maria Loconsole and Dr. Francesco Anelli

![](_page_0_Picture_10.jpeg)

![](_page_0_Picture_11.jpeg)

![](_page_1_Picture_0.jpeg)

![](_page_1_Picture_1.jpeg)

*Article*

# **Hollow-Core Fiber Properties and System-Level Specifications for Next-Generation Optical Transport Networks**

**Bruno Correia 1,[\\*](https://orcid.org/0000-0002-2848-8517) and João Pedro 1,[2](https://orcid.org/0000-0003-4471-7401)**

- <sup>1</sup> Nokia, Optical Networks, 2790-078 Carnaxide, Portugal; joao.pedro@nokia.com
- Instituto de Telecomunicações, Instituto Superior Técnico, 1049-001 Lisboa, Portugal
- **\*** Correspondence: bruno.correia@nokia.com

#### **Abstract**

In light of the recent advances in hollow-core fiber (HCF) design and manufacturing, widescale deployments of this fiber type to realize next-generation optical transport networks may become viable in the foreseeable future, with benefits in terms of lower latency and improved capacity/reach. Nevertheless, several uncertainties remain regarding the properties of HCF that can be manufactured at scale, as well as the specifications of optical amplifiers developed to leverage the negligible low linearity of this fiber type. This work evaluates the performance of HCFs considering a wide range of potential fiber and amplifier parameters and compares them with traditional standard single-mode fiber (SSMF) and pure-silica-core fiber (PSCF). The resulting analysis allows us to determine, at a system and network level, the combination of fiber and amplifier parameters that will allow HCF to become a competitive transmission medium for next-generation optical transport networks.

**Keywords:** hollow-core fiber; multiband transmission; optical performance; network design; optical transport networks

## **1. Introduction**

The advances in hollow-core fibers (HCFs) have been substantial in recent years, emerging as a promising new fiber technology which can replace traditional silica fibers in the future [\[1\]](#page-13-0). The first main advantage of this fiber type is the potential to decrease the attenuation profile, which nowadays is around 0.21 and 0.17 dB/km for standard single-mode fiber (SSMF) and pure-silica-core fiber (PSCF), respectively, to values below 0.11 dB/km [\[2\]](#page-13-1) and potentially even lower. Besides lower attenuation values, HCF also presents a potential wider spectral low-loss region, making the adoption of ultra-wide band (UWB) [\[3\]](#page-13-2) transmission systems more attractive. Furthermore, HCFs have a low nonlinearity and negligible stimulated Raman scattering (SRS) [\[4\]](#page-13-3), which allow the transmission of channels with higher power without signal degradation. In silica-based fibers, SRS, which induces power transfer from higher to lower frequencies, requires a careful and complex power optimization in UWB transmission [\[5\]](#page-13-4). In the absence of SRS, power optimization in these transmission systems is greatly simplified. Finally, light is transmitted 50% faster through HCF due to its near-vacuum medium [\[6\]](#page-13-5). Therefore, the latency presented by this fiber type is around 33% lower than SSMF/PSCF, which makes it suitable for latency-constrained applications. With all the aforementioned advantages, HCF deployment is envisioned across a wide range of applications, from data center interconnect (DCI) to ultra-long-haul optical networks.

![](_page_1_Figure_13.jpeg)

Received: 9 December 2025

Revised: 8 January 2026 Accepted: 9 January 2026 Published: 13 January 2026 **Copyright:** © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the [Creative Commons](https://creativecommons.org/licenses/by/4.0/) [Attribution \(CC BY\) license.](https://creativecommons.org/licenses/by/4.0/)

*Photonics* **2026**, *13*, 71 2 of 14

Importantly, despite all the advantages of HCF, some drawbacks and uncertainties need to be addressed or properly considered/managed in order for this fiber type to compete and potentially outperform traditional solid core fibers. Firstly, exploiting the ability to launch high signal powers into HCF requires the availability of optical amplifiers with a high maximum total output power. Key parameters, such as the noise figure and complexity/cost of these devices, are paramount to leverage this benefit of HCF. Secondly, an additional penalty, negligible in silica fibers, is the inter-modal interference (IMI), which consists of the loss induced by high-order modes in the fundamental mode. It has been shown that IMI has no meaningful impact in performance if it is below −60.0 dB/km [\[7\]](#page-13-6). Still, IMI values between −40.0 and −55.0 dB/km have been considered in previous works [\[2,](#page-13-1)[4,](#page-13-3)[8\]](#page-13-7). In view of the uncertainty around the large-scale production of HCF and the properties of these fibers, a range of IMI values should be considered when reporting system-level analysis. Another aspect that requires consideration involves the larger connection losses, such as fiber splices and interconnection with solid core fibers. The former loss is required, e.g., in the event of fiber cuts, while the later need to be considered for HCF deployment as the whole optical environment of components, e.g., erbium-doped fiber amplifiers (EDFA) and reconfigurable optical add-drop multiplexers (ROADM), were developed for traditional fiber types. These losses have been decreasing, with the latest record set at 0.18 dB per splice [\[9\]](#page-13-8).

Modeling the uncertainty around the referred fiber and amplifier parameters and their interplay is, therefore, key to understanding the pre-conditions for HCF in becoming competitive with traditional fibers and setting targets for improved fiber manufacturing, amplifier design, and deployment techniques (e.g., splicing). To the best of our knowledge, the only works that analyzed HCF deployment in optical transport networks are the ones presented in [\[10](#page-14-0)[–12\]](#page-14-1), which did not consider comprehensive HCF parameter variations. This article focuses on expanding our preliminary analysis reported in [\[13\]](#page-14-2), evaluating the scenarios in which HCF deployment is competitive, when compared with two reference fiber types—SSMF and PSCF.

This paper is organized as follows. Section [2](#page-2-0) describes the optical line system characterization, with Section [2.1](#page-2-1) addressing the fiber characteristics and Section [2.2](#page-3-0) describing the variations of amplifiers' parameters and types used in our analysis. Section [3](#page-4-0) details the simulation workflow, including the quality of transmission (QoT) computation procedure (Section [3.1\)](#page-4-1), the launch power optimization (Section [3.2\)](#page-4-2), and the network simulation framework (Section [3.3\)](#page-5-0). The simulation results are presented in Section [4,](#page-6-0) split between transmission performance results in Section [4.1](#page-6-1) and network simulation results in Section [4.2.](#page-10-0) Finally, Section [5](#page-12-0) draws the main conclusions of this work.

#### <span id="page-2-0"></span>**2. Line System Characterization**

#### <span id="page-2-1"></span>*2.1. Fiber Characterization*

To assess the impact of different HCF realizations, we defined a wide range for the attenuation profile between 0.11 and 0.31 dB/km, as illustrated in Figure [1a](#page-3-1), alongside with the typical attenuation profiles of SSMF and PSCF. This range allows us to consider cases where HCF offers lower, comparable, or higher attenuation than SSMF or PSCF.

Figure [1b](#page-3-1) shows the Raman gain profile of all three fiber types, with peak values of 0.38 and 0.22 1/(W·km) for SSMF and PSCF, respectively. As referred, the SRS effect is not present in HCF [\[4\]](#page-13-3) and, hence, it is set to zero for every frequency offset value. The final HCF internal design and evolution of splicing technology will determine the fiber splicing and connection losses. Hence, in this study we varied this source of losses between 0.05 and 0.5 dB per 2 km of fiber. Regarding IMI power, in order to evaluate its impact together with the variation of attenuation and connection losses, it is assumed

Photonics **2026**, 13, 71 3 of 14

<span id="page-3-1"></span>to range between -45.0 and -60.0 dB/km. The simplified modeling of the impact of IMI in HCF transmission performance is detailed in Section 3.1. All aforementioned fiber parameters, together with chromatic dispersion, chromatic dispersion slope, effective area, and nonlinear coefficient (with their respective references) are summarized in Table 1, where we show only the average value (Avr.) when the parameter is frequency dependent.

![](_page_3_Figure_2.jpeg)

**Figure 1.** Comparison of (**a**) fiber attenuation profile and (**b**) fiber Raman gain profile parameters for SSMF, PSCF, and HCF.

<span id="page-3-2"></span>

| Table 1. Fibe | r parameters | of SSMF, | PSCF | , and HCF. |
|---------------|--------------|----------|------|------------|
|               |              |          |      |            |

|                                          | SSMF  | PSCF                 | HCF                      |
|------------------------------------------|-------|----------------------|--------------------------|
| Avr. loss [dB/km]                        | 0.21  | 0.17                 | {0.11, 0.13,, 0.31}      |
| Avr. CD [ps/(nm·km)]                     | 16.8  | 21.0                 | 3.0 [7]                  |
| Avr. CD slope [ps/(nm <sup>2</sup> ·km)] | 0.058 | 0.061                | 0.0 [14]                 |
| Effective area [μm²]                     | 83.0  | 130.0                | 417.0 [14]               |
| Nonlinear coeff. [1/(W·km)]              | 1.12  | $6.24 \cdot 10^{-1}$ | $5.01 \cdot 10^{-4}$ [7] |
| Raman gain coeff. peak [1/(W·km)]        | 0.38  | 0.22                 | 0.0 [4]                  |
| Splice loss per 2 km [dB]                | 0.02  | 0.02                 | $\{0.05, 0.10,, 0.50\}$  |
| IMI [dB/km]                              | _     | _                    | $\{-60, -55, -50, -45\}$ |

It is worth mentioning that polarization mode dispersion (PMD), which can be slightly higher in HCF when compared with traditional fibers, is not considered in this work.

#### <span id="page-3-0"></span>2.2. Optical Amplifier Characterization

In optical transport networks, the most common option for signal amplification is the usage of EDFAs. This mature and widely used technology nowadays can amplify both Cand L-band [15] spans with lengths that can exceed 100 km, presenting a very competitive performance and cost when compared to other amplification technologies. The second option of optical amplification is the usage of the Raman gain through Raman amplifiers, which usually are combined with EDFAs and are known as hybrid EDFA/Raman amplification (HFA) [16]. As this type of amplification is performed along the fiber using counter-propagated high-power pumps, the launch power in the fiber can be reduced, decreasing the penalties from nonlinearities, and lesser gains are required from EDFAs, reducing the amplified spontaneous emission (ASE) noise. This results in a performance improvement (compared with only EDFAs), but at the expense of higher costs [17]. Importantly, since the SRS effect is virtually absent in HCF transmission, HFA is not available with this fiber type, which must rely only on EDFAs. Conversely, due to the same reason (negligible nonlinear interference), significantly higher powers can be launched into HCF before incurring signal degradation due to nonlinear effects. Leveraging these higher powers depends on the ability to manufacture EDFAs that feature high power and relatively low noise figure values at a competitive cost. A comprehensive analysis of the

Photonics 2026, 13, 71 4 of 14

different amplification options available according to fiber type demands considering, on the one hand, mature EDFA and HFA options for SSMF and PSCF, and on the other hand, different potential realizations of high-power EDFAs for HCF. The description of amplifier parameters, i.e., maximum total output power (Max. Pow.) and noise-figure (NF) for each spectral band, are described in Table 2 for both spectral scenarios tested. Note that we assume that to realize cost-effective higher power amplifiers there is an increase in the average noise figure for devices with higher maximum total output power.

<span id="page-4-3"></span>

| _                  | SuperC          |         | SuperL          |         |
|--------------------|-----------------|---------|-----------------|---------|
|                    | Max. Pow. [dBm] | NF [dB] | Max. Pow. [dBm] | NF [dB] |
| SSMF/PSCF          | 24.0            | 5.5     | 24.0            | 6.0     |
| HCF amp. config. 1 | 27.0            | 5.5     | 24.0            | 6.0     |
| HCF amp. config. 2 | 30.0            | 6.5     | 27.0            | 7.0     |
| HCF amp. config. 3 | 33.0            | 7.5     | 30.0            | 8.0     |
| HCF amp. config. 4 | 36.0            | 8.5     | 33.0            | 9.0     |

#### <span id="page-4-0"></span>3. Performance Modeling and Optimization

#### <span id="page-4-1"></span>3.1. Optical Performance Model

In this work, the QoT of a span traversed by an optical channel or lightpath (LP) is evaluated by the generalized signal-to-noise ratio (GSNR) [18]. With traditional silica fibers (SSMF and PSCF), the GSNR considers the ASE power, generated by optical amplifiers, and the nonlinear interference (NLI), generated by fiber transmission. When transmitting using HCFs, a third contribution of noise is added to the GSNR computation, the IMI power, as discussed in Section 2.1. Factoring in the different noise and noise equivalent terms, the GSNR of a channel with frequency f is given as follows [7]:

$$GSNR_f = \frac{P_f}{P_{ASE,f} + P_{NLI,f} + P_{IMI,f}}$$
 (1)

where  $P_f$  is the power of the channel and  $P_{ASE,f}$ ,  $P_{NLI,f}$ , and  $P_{IMI,f}$  are the ASE, NLI, and IMI powers, respectively, of the same channel. Assuming an incoherent accumulation of the NLI, the QoT evaluation over the entire LP p (also for a channel with frequency f) can be given by the following:

$$GSNR_{f,p}^{-1} = OSNR_{Tx,p}^{-1} + \sum_{s \in S_p} GSNR_{f,s}^{-1} + OSNR_{add,p}^{-1} + OSNR_{drop,p}^{-1} + \sum_{r \in R_p} OSNR_{int r,p}^{-1}$$
 (2)

where  $S_p$  denotes the set of fiber spans traversed,  $OSNR_{Tx,p}$ ,  $OSNR_{add,p}$ ,  $OSNR_{drop,p}$ ,  $OSNR_{int\,r,p}$  are the OSNR contributions for the optical transmitter and the reconfigurable optical add/drop multiplexer (ROADM) at the add node, drop node, and intermediate node r, respectively.  $R_p$  denotes the set of intermediate ROADMs traversed by LP p. It is worth mentioning that we consider typical ROADM insertion losses of 21.0, 20.5, and 13.5 dB for add, drop, and intermediate nodes, respectively.

The WDM spectral scenarios assumed in this work are composed by SuperC and SuperL bands with total bandwidths of 6.1 and 5.5 THz, respectively. It is assumed that each band is populated by 120 Gbaud signals within a 150 GHz WDM grid, resulting in a total of 40 and 36 channels in SuperC and SuperL bands, respectively.

#### <span id="page-4-2"></span>3.2. Launch Power Optimization

As transmission impairments are affected by the SRS effect in traditional fibers, the launch power into the fiber needs to be properly defined to maximize the signal QoT.

*Photonics* **2026**, *13*, 71 5 of 14

In this work, when transmitting using SSMF and PSCF, we used the pre-tilted input power profile [\[5\]](#page-13-4) to counteract the SRS effect, defining the EDFA average power per channel and tilt. In the HFA cases, besides the EDFA power and tilt, the Raman pumps' frequencies and powers also need to be defined. For both cases (EDFA and HFA) we used the Genetic Algorithm (GA)-based optimization method proposed by [\[19\]](#page-14-8). Moreover, for HCF transmission, the input power per channel is mostly limited by the amplifier maximum total output power. The GSNR profile of a single span of 80 km, after launch power optimization, is presented in Figure [2.](#page-5-1) The HCF scenario shown in this plot is for a single HCF instance, with an average fiber attenuation of 0.16 dB/km, connection loss of 0.12 dB, IMI of −55 dB/km, and HCF amplifier configuration 3, as shown in Table [2.](#page-4-3)

<span id="page-5-1"></span>![](_page_5_Figure_2.jpeg)

**Figure 2.** GSNR profiles comparison for (**a**) SuperC and (**b**) SuperC+L with EDFA (circle) and HFA (down triangle) amplification, between SSMF (blue), PSCF (orange), and HCF (green).

The SuperC case shown in Figure [2a](#page-5-1) presents GSNR averages of 27.5 and 34.5 dB for SSMF with EDFA and HFA, respectively, 31.5 and 37.4 dB for PSCF with EDFA and HFA, respectively, and finally, an average of 34.5 dB for HCF. Figure [2b](#page-5-1) shows the SuperC+L case, with the following GSNR averages: 27.2 and 27.8 dB for SuperC and SuperL, respectively, for SSMF with EDFA; 32.3 and 29.4 dB (SuperC/L) for SSMF with HFA, 31.2 and 31.5 dB for SuperC and SuperL, respectively, for PSCF with EDFA and 35.9 and 32.9 (SuperC/L) for PSCF with HFA; and finally, 34.5 and 37.0 dB for SuperC and SuperL, respectively, using HCF transmission. For this particular case of HCF transmission, its performance is similar to SSMF using HFA for the SuperC case, whereas in the SuperC+L case, the HCF performance is better than PSCF using HFA in SuperL, but slightly worse in the SuperC band. Comparing both plots already hints that HCF may be a better transmission medium for wideband optical systems, since it is performing comparatively better in the SuperC+L-band case. Section [4.1](#page-6-1) details the performance comparison among all the HCF scenarios tested in this work.

#### <span id="page-5-0"></span>*3.3. Network Assessment Framework*

In order to also evaluate the impact of HCF deployment at a network level and compare it with traditional fiber types, the Telecom Italia (TIM) network topology was assessed. This topology, shown in Figure [3,](#page-6-2) comprises 44 ROADM nodes and 142 OMSs with a total of 400 spans of 80 km.

*Photonics* **2026**, *13*, 71 6 of 14

<span id="page-6-2"></span>![](_page_6_Figure_1.jpeg)

**Figure 3.** TIM national reference network topology showing the ROADM nodes (blue boxes) and the OMSs (blue curves).

The network assessment is performed for several total offered traffic loads (the range varies between scenarios using SuperC and SuperC+L), showing the average results obtained by running 20 independent simulations (based on different traffic matrices) for each load value. Each traffic matrix is populated with random client connections of 100 and 400 G following a uniform distribution between ROADM nodes. Moreover, our framework orders all the connections from the longest to the shortest ones, trying to allocate them sequentially, following a *k*-shortest routing algorithm with *k* = 3 and first-fit as the spectrum allocation policy. The bit rate of each WDM channel is defined based on the OpenROADM MSA [\[20\]](#page-14-9) transceiver, with three modes delivering 800, 600, and 400 Gbps with a required OSNR (ROSNR) of 25.1, 22.0, and 17.4 dB/0.1 nm, respectively. For a more realistic modeling, the ROSNR limits are increased by additional penalties from polarization-dependent loss (PDL) contributions (coming from the traversed ROADMs and amplifiers) and a system margin (e.g., to account for component and fiber aging), which is set to 1.0 dB in this work.

#### <span id="page-6-0"></span>**4. Results and Discussion**

#### <span id="page-6-1"></span>*4.1. Transmission Performance Comparison*

To evaluate the scenarios in which HCF can match or outperform traditional fibers, Figure [4](#page-8-0) shows, for a single 80 km span, the heatmap plots of the ∆GSNR = GSNRHCF − GSNRSSMF/PSCF, where we compare the combination of HCF attenuation and connection loss values for a total of 966 combinations. This analysis used the HCF amplifier configuration 3 from Table [2](#page-4-3) and an IMI power of −55 dB/km. *Photonics* **2026**, *13*, 71 7 of 14

Eight different scenarios are presented, combining the spectral cases (SuperC and SuperC+L), the type of amplification used (EDFA and Hybrid), and finally, the two reference fiber types (SSMF and PSCF). These plots show in green color the combination of HCF properties where this fiber type outperforms traditional fibers, while red color highlights the cases where HCF has lower performance.

In the first case, presented in Figure [4a](#page-8-0) and consisting of SuperC/SSMF/EDFA, HCF outperforms SSMF by a maximum of 8.1 dB, for the lowest values of attenuation and connection loss, and for a total of 573 cases (59%). By introducing hybrid amplification, which is the case of the results shown in Figure [4b](#page-8-0), the maximum gain in a single-span GSNR achieved by HCF drops to around 1.1 dB, totaling 90 cases (9%). Considering PSCF as a the reference fiber type for comparison, and still with SuperC, the number of combinations in which HCF outperforms this fiber type are 307 (32%) and 0 for EDFA (Figure [4c](#page-8-0)) and HFA (Figure [4d](#page-8-0)), respectively. Notably, for PSCF with hybrid amplification, the lower attenuation profile and Raman gain coefficient of this fiber type, together with a limited spectrum bandwidth and a higher performance enabled by this amplification scheme, allow the system to always outperform the HCF realizations considered. Using a wider spectral bandwidth, as shown in Figure [4e](#page-8-0) for the SuperC+L/SSMF/EDFA case, HCF outperforms SSMF in 514 combinations (53%), achieving a maximum gain in GSNR of 12.1 dB. By using hybrid amplification (Figure [4f](#page-8-0)), this value decreases to 313 cases (32%) with a maximum advantage of 8.7 dB. Comparing this scenario with its counterpart based on the narrower SuperC bandwidth (Figure [4b](#page-8-0)), we notice an increase by more than three times in the number of cases where HCF outperforms SSMF. This comes from the fact that, as we enlarge the spectral usage, the nonlinear effect of the SRS is stronger, decreasing the average performance of SSMF. As the HCF has negligible nonlinear effects, increasing the used bandwidth makes HCF more advantageous compared to traditional fibers, even when it has slightly higher combined losses (fiber attenuation plus connection loss). Finally, both scenarios (EDFA and HFA) with PSCF using SuperC+L, shown in Figures [4g](#page-8-0) and [4h](#page-8-0), respectively, present maximum GSNR gains of 8.3 and 5.1 dB, and the number of cases where HCF outperforms this fiber type is 289 and 136 for EDFA and HFA, respectively. Again, for this fiber type, we noticed that the tolerance for higher performance is maintained in the same levels for EDFA amplification, while for hybrid amplification these values increase considerably, as no case with HCF outperformed PSCF using only the SuperC. Notably, the plots shown in Figure [4](#page-8-0) only show the results for fixed values of the amplifiers' maximum total output power and the IMI. In order to assess the impact of these parameters, in the following, we focus on the white region of the plots, approximately forming a curve that corresponds to the HCF properties where the GSNR is approximately the same as that of the reference silica-based fiber type. It is clear that the cases that lay below this curve are the ones where HCF outperforms the reference fiber type. Therefore, to represent more cases in a single plot, the next set of figures only shows this curve, hereafter designated as the parity curve.

In order to expand the results shown in Figure [4,](#page-8-0) Figure [5](#page-9-0) presents the parity curves of all tested cases, showing where the performance between SSMF/PSCF and HCF is similar.

*Photonics* **2026**, *13*, 71 8 of 14

<span id="page-8-0"></span>![](_page_8_Figure_1.jpeg)

**Figure 4.** Heatmaps with a single span of 80 km ∆GSNR with IMI = −55.0 dB/km and HCF amplification configuration 3 for (**a**) SuperC-SSMF-EDFA, (**b**) SuperC-SSMF-HFA, (**c**) SuperC-PSCF-EDFA, (**d**) SuperC-PSCF-HFA, (**e**) SuperC+L-SSMF-EDFA, (**f**) SuperC+L-SSMF-HFA, (**g**) SuperC+L-PSCF-EDFA, and (**h**) SuperC+L-PSCF-Hybrid.

*Photonics* **2026**, *13*, 71 9 of 14

<span id="page-9-0"></span>![](_page_9_Figure_1.jpeg)

**Figure 5.** Parity curves with a single span of 80 km for (**a**) SuperC-SSMF-EDFA, (**b**) SuperC-SSMF-HFA, (**c**) SuperC-PSCF-EDFA, (**d**) SuperC-PSCF-HFA, (**e**) SuperC+L-SSMF-EDFA, (**f**) SuperC+L-SSMF-HFA, (**g**) SuperC+L-PSCF-EDFA, and (**h**) SuperC+L-PSCF-HFA.

These plots include results with all four HCF IMI values considered—from −45 to −60 dB/km—and the lowest and highest values of maximum amplifier output powers, corresponding to HCF amplifier configurations 1 and 4, respectively. Figure [5a](#page-9-0) presents the parity curves for the scenario with SuperC/SSMF/EDFA, showing that HCF outperforms SSMF only for IMI powers equal or lower than −50 dB/km (green curves). Moreover, we notice that the difference between the curves with an IMI of −55 (orange) and −60 dB/km (blue) is negligible in this case. If we fix the fiber attenuation to 0.21 dB/km and assume IMI = −60, the tolerance to connection losses can increase from 0.23 dB (output power of 27.0 dBm–circle) to 0.38 dB (output power of 36.0 dBm–triangle). When hybrid

*Photonics* **2026**, *13*, 71 10 of 14

amplification is used instead (SuperC/SSMF/HFA), Figure [5b](#page-9-0) shows that only IMI powers below −55 dB/km enable the better performance of HCF. Moreover, this case shows a considerable difference between the curves with IMI values of −60 and −55 dB/km for both amplification schemes, varying by around 0.1 dB in connection loss tolerance for the same fiber attenuation. The plots comparing HCF with PSCF for SuperC without and with hybrid amplification are shown in Figures [5c](#page-9-0) and [5d](#page-9-0), respectively. For the former, HCF starts to outperform PSCF with IMI values of −55 dB/km or lower, with a difference of 0.4 dB in connection loss for a fixed fiber attenuation, while the later presents cases where HCF is better only for IMI = −60 dB/km, with a reduced tolerance of losses, especially for lower maximum amplifier' output power. Unlikely the results with SuperC, when we expand the spectrum usage with SuperC+L, all scenarios (SSMF/PSCF with EDFA/Hybrid amplification) present at least one parity curve with IMI = −45 dB/km, showing the importance of having negligible nonlinear effects in multiband transmission with HCF. The SuperC+L comparison between HCF and SSMF with EDFA amplification shown in Figure [5e](#page-9-0) depicts a negligible difference between an IMI value of −60 and −55 dB/km, whereas the tolerance decreases by about 0.03 dB (IMI = −50 dB/km) and 0.10 dB (IMI = −45 dB/km) in splice loss for the same fiber attenuation. As expected, allowing hybrid amplification with SSMF (Figure [5f](#page-9-0)) results in a lower tolerance to losses for HCF to overcome SSMF, with a considerable difference between different IMI values. Finally, Figures [5g](#page-9-0) and [5h](#page-9-0) present the comparison between HCF and PSCF with EDFA and hybrid amplification, respectively. Comparing both cases, the trend follows the same pattern as the comparison with SSMF, with lower tolerance to losses, as the PSCF presents a lower attenuation profile and is less impacted by the SRS effect. As an example, HCF outperforms PSCF for a short number of combinations of fiber attenuation and connection losses for the highest IMI value (−45 dB/km) and the lowest performance amplifier (27.0/24.0 dBm) (red circle curve) in the EDFA case, but not if HFA is used.

#### <span id="page-10-0"></span>*4.2. Network Capacity Comparison*

The network assessment using the framework introduced in Section [3.3](#page-5-0) was performed for four combinations of silica-based fibers and amplification types, i.e., SSMF and PSCF with EDFA and HFA. Additionally, we evaluated two HCF scenarios. The first one, which is called Worst, assumes a HCF attenuation average of 0.21 dB/km together with HCF amplifier configuration 1 from Table [2.](#page-4-3) The second configuration (Best), assumes a HCF attenuation average of 0.11 dB/km combined with HCF amplifier configuration 4 from Table [2.](#page-4-3) For both HCF scenarios, we used the splice loss of 0.18 dB, which is one of the lowest values reported so far [\[9\]](#page-13-8).

Firstly, in Figure [6,](#page-11-0) we evaluate the number of end-to-end optical channels that are feasible with each possible bit rate (800, 600 and 400 Gbps) for traffic loads from 30 to 60 Tbps for SuperC and traffic loads from 90 to 120 Tbps for SuperC+L. Note that for each path being considered, only the highest feasible bit rate is accounted for in the analysis, i.e., if a given path supports 800 Gbps, then it is accounted for only for the total count of channels with this bit rate and not for the lower ones.

For the SuperC scenario (Figure [6a](#page-11-0)), it is possible to observe that the configuration which enables the highest number of channels with 800 Gbps is the PSCF with hybrid amplification (red bar), with around 175 channels for an offered traffic of 60 Gbps, while for the same load, both HCF Best (brown) and SSMF (Hybrid) (orange) enable around 150 channels, with slight advantage for HCF Best. As expected, the opposite trend is found when we analyze the number of channels using the lowest bit rate (400 Gbps), presenting no channels with PSCF (Hybrid) and less than 5 channels with HCF Best and SSMF (Hybrid), for all offered traffic points. The results for SuperC+L, presented in Figure [6b](#page-11-0), highlight

Photonics 2026, 13, 71 11 of 14

that HCF Best is the configuration that enables the highest number of channels with 800 Gbps, ranging from 263 (90 Tbps) to 326 channels (120 Tbps), while the second best configuration (PSCF (Hybrid)) allows 190 (90 Tbps) and 229 channels (120 Tbps). Moreover, the only configuration which does not require channels with the lowest bit rate (400 Gbps) is HCF Best, with HCF Worst presenting the highest number of this channel bit rate, ranging from 155 to 201 channels. The variation in the number of channels per channel capacity of HCF cases highlights how the HCF fiber parameter values can significantly impact network performance.

Finally, Figure 7 presents the overall network offered traffic versus carried traffic on the left y-axis (total traffic demands successfully routed) and blocked traffic on the right y-axis (total traffic demands blocked).

<span id="page-11-0"></span>![](_page_11_Figure_3.jpeg)

**Figure 6.** Number (Represented by the symbol #) of optical channels per bit rate mode used versus the offered total traffic for (a) SuperC and (b) SuperC+L scenarios.

For the SuperC spectral scenario in Figure 7a, the cases with the lowest carried traffic, and consequently highest blocked traffic, are the SSMF (EDFA) and HCF (Worst), achieving a carried traffic load of only around 96 Tbps when 150 Gbps is offered. For the same offered traffic load, the PSCF (EDFA) is able to allocate around 100 Gbps, while the other two cases, PSCF (HFA) and HCF (Best), successfully support around 104 Gbps. When we expand the spectral usage to SuperC+L, shown in Figure 7b, we notice that the difference between cases is more clear. Specifically, for the highest offered traffic load of 220 Tbps in this scenario, we obtained carried traffic load values of 171.7, 171.9, 178.2, 181.4, 185.8, and 191.1 Tbps for SSMF (EDFA), HCF (Worst), SSMF (Hybrid), PSCF (EDFA), PSCF (Hybrid), and HCF (Best), respectively. Comparing this plot with the SuperC case shown in Figure 7a, the advantages of HCF usage are more clear when you expand the spectral usage. We would like to highlight that, in order to be conservative in our analysis, the HCF cases evaluated in the network assessment used splice losses of 0.18 dB, which is 9 times higher than the one of traditional fibers. Moreover, as presented in Table 2, the amplifiers with higher maximum total output power present a significantly higher NF, impacting the signal QoT and decreasing the ability of HCF to outperform silica-based fibers. Even in this restricted scenario, HCF shows potential to improve the performance of optical transport networks. If technology bottlenecks, like connection losses, amplifiers with higher output power capacity maintaining comparable NF levels as the ones used in today's networks, and scalable manufacturing processes with low attenuation can be improved, HCF will

Photonics 2026, 13, 71 12 of 14

not be restricted to latency-constrained scenarios and could be deployed in future optical transport networks.

<span id="page-12-1"></span>![](_page_12_Figure_2.jpeg)

**Figure 7.** Offered versus carried/blocked traffic for (a) SuperC and (b) SuperC+L scenarios. The black circles indicates to which axis (left or right y-axis) the curves belong.

#### <span id="page-12-0"></span>5. Conclusions

In this work, an extensive simulation assessment was carried out to evaluate the performance of HCF compared with traditional silica-based fibers for high-capacity regional/long-haul optical transport network deployment. We evaluated a wide range of HCF parameters, such as IMI power, fiber attenuation, and splice losses, as well as amplifier maximum total output power, together with its noise figure. Regarding current fiber technologies, we compare HCF performance with two fiber types, the market dominant SSMF and best-in-class PSCF, together with two different amplification options, one using only EDFAs and another allowing the possibility to use EDFA together with Raman amplification, with the later presenting a higher performance at the expense of higher cost. Besides the span performance analysis, a network assessment was performed for a couple of HCF systems and compared with traditional ones, evaluating its impact in terms of optical channel bit-rate capacity and overall allocated traffic. Finally, it is worth noting that all the aforementioned aspects were performed for the single-band case using SuperC and for a wide-band system composed of SuperC+L.

One of the key findings of this work was the confirmation and quantification of the performance advantage of HCF versus SSMF/PSCF when a wider spectral range is used, in this case, SuperC+L instead of SuperC. The results clearly show that with SuperC+L, there is scope for deploying HCF with worse parameters, e.g., IMI and losses, while still matching the performance of traditional silica-based fibers. Conversely, improved HCF realizations are required when SuperC is considered. Another important observation is that using hybrid amplification with SSMF/PSCF, which is not viable with HCF, improves

*Photonics* **2026**, *13*, 71 13 of 14

the performance obtained with these fibers, although at the expense of additional cost with amplification devices. To cope with this improvement, improved HCF specifications and/or higher power amplifiers are required to match or surpass the performance of traditional fibers. Overall, it can be concluded that when compared to the lowest cost silicabased fiber solution—SSMF and EDFA—HCF can become competitive even with relatively relaxed specifications (even more for SuperC). On the other hand, if the reference is the costlier PSCF and HFA solution, improved realizations of HCF are required. Finally, the network-level simulations over a reference optical transport network and using the latest generation of 800G-capable coherent pluggable transceivers provided further evidence of how improved span-level performance translates into higher carried traffic load.

**Author Contributions:** Conceptualization, B.C. and J.P.; methodology, B.C. and J.P.; software, B.C. and J.P.; validation, B.C. and J.P.; formal analysis, B.C. and J.P.; investigation, B.C. and J.P.; resources, B.C. and J.P.; data curation, B.C. and J.P.; writing—original draft preparation, B.C. and J.P.; writing—review and editing, B.C. and J.P.; visualization, B.C. and J.P.; supervision, J.P.; project administration, J.P.; funding acquisition, J.P. All authors have read and agreed to the published version of the manuscript.

**Funding:** This work has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement No. 101092766 (ALLEGRO Project), by national funds through FCT–Fundação para a Ciência e a Tecnologia, I.P., and, when eligible, co-funded by EU funds under project/support UID/50008/2025–Instituto de Telecomunicações, with DOI identifier [https://doi.org/10.54499/UID/50008/2025.](https://doi.org/10.54499/UID/50008/2025)

**Data Availability Statement:** Dataset available on request from the authors.

**Conflicts of Interest:** The authors declare no conflicts of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.

#### **References**

- <span id="page-13-0"></span>1. Fokoua, E.N.; Mousavi, S.A.; Jasion, G.T.; Richardson, D.J.; Poletti, F. Loss in hollow-core optical fibers: Mechanisms, scaling rules, and limits. *Adv. Opt. Photonics* **2023**, *15*, 1–85. [\[CrossRef\]](http://doi.org/10.1364/AOP.470592)
- <span id="page-13-1"></span>2. Chen, Y.; Petrovich, M.; Fokoua, E.N.; Adamu, A.; Hassan, M.; Sakr, H.; Slavík, R.; Gorajoobi, S.B.; Alonso, M.; Ando, R.F.; et al. Hollow Core DNANF Optical Fiber with <0.11 dB/km Loss. In Proceedings of the Optical Fiber Communication Conference (OFC), San Diego, CA, USA, 24–28 March 2024; p. Th4A.8. [\[CrossRef\]](http://dx.doi.org/10.1364/OFC.2024.Th4A.8)
- <span id="page-13-2"></span>3. Ferrari, A.; Napoli, A.; Fischer, J.K.; Costa, N.; D'Amico, A.; Pedro, J.; Forysiak, W.; Pincemin, E.; Lord, A.; Stavdas, A.; et al. Assessment on the Achievable Throughput of Multi-Band ITU-T G.652.D Fiber Transmission Systems. *J. Light. Technol.* **2020**, *38*, 4279–4291. [\[CrossRef\]](http://dx.doi.org/10.1109/JLT.2020.2989620)
- <span id="page-13-3"></span>4. Nespola, A.; Straullu, S.; Bradley, T.D.; Harrington, K.; Sakr, H.; Jasion, G.T.; Fokoua, E.N.; Jung, Y.; Chen, Y.; Hayes, J.R.; et al. Transmission of 61 C-Band Channels Over Record Distance of Hollow-Core-Fiber With L-Band Interferers. *J. Light. Technol.* **2021**, *39*, 813–820. [\[CrossRef\]](http://dx.doi.org/10.1109/JLT.2020.3047670)
- <span id="page-13-4"></span>5. Correia, B.; Sadeghi, R.; Virgillito, E.; Napoli, A.; Costa, N.; Pedro, J.; Curri, V. Power control strategies and network performance assessment for C+L+S multiband optical transport. *J. Opt. Commun. Netw.* **2021**, *13*, 147–157. [\[CrossRef\]](http://dx.doi.org/10.1364/JOCN.419293)
- <span id="page-13-5"></span>6. Sticca, G.S.; Ibrahimi, M.; Cicco, N.D.; Musumeci, F.; Tornatore, M. Hollow-Core-Fiber Placement in Latency-Constrained Metro Networks with edgeDCs. In Proceedings of the Optical Fiber Communication Conference (OFC), San Diego, CA, USA, 24–28 March 2024; p. Tu3B.2. [\[CrossRef\]](http://dx.doi.org/10.1364/OFC.2024.Tu3B.2)
- <span id="page-13-6"></span>7. Poggiolini, P.; Poletti, F. Opportunities and Challenges for Long-Distance Transmission in Hollow-Core Fibres. *J. Light. Technol.* **2022**, *40*, 1605–1616. [\[CrossRef\]](http://dx.doi.org/10.1109/JLT.2021.3140114)
- <span id="page-13-7"></span>8. Jasion, G.T.; Sakr, H.; Hayes, J.R.; Sandoghchi, S.R.; Hooper, L.; Fokoua, E.N.; Saljoghei, A.; Mulvad, H.C.; Alonso, M.; Taranta, A.; et al. 0.174 dB/km Hollow Core Double Nested Antiresonant Nodeless Fiber (DNANF). In Proceedings of the Optical Fiber Communication Conference (OFC), San Diego, CA, USA, 6–10 March 2022; p. Th4C.7. [\[CrossRef\]](http://dx.doi.org/10.1364/OFC.2022.Th4C.7)
- <span id="page-13-8"></span>9. Zhong, A.; Fokoua, E.N.; Ding, M.; Dousek, D.; Suslov, D.; Zvánovec, S.; Poletti, F.; Slavík, R.; Komanec, M. Connecting Hollow-Core and Standard Single-Mode Fibers with Perfect Mode-Field Size Adaptation. *J. Light. Technol.* **2024**, *42*, 2124–2130. [\[CrossRef\]](http://dx.doi.org/10.1109/JLT.2023.3329738)

*Photonics* **2026**, *13*, 71 14 of 14

<span id="page-14-0"></span>10. Sticca, G.; Ibrahimi, M.; Cicco, N.D.; Musumeci, F.; Tornatore, M.; Milano, P.D. On High-Power Optical Amplification in Hollow Core Fibers for Energy Efficiency and Network Throughput Maximization. In Proceedings of the 50th European Conference on Optical Communication (ECOC) 2024, Frankfurt, Germany, 22–26 September 2024; pp. 1010–1013.

- 11. Ibrahimi, M.; Sticca, G.S.; Musumeci, F.; Tornatore, M. On the Benefits of Hollow-Core Fiber in Next-Generation Optical Networks [Invited]. In Proceedings of the 2025 International Conference on Optical Network Design and Modeling (ONDM), Pisa, Italy, 6–9 May 2025; pp. 1–5. [\[CrossRef\]](http://dx.doi.org/10.23919/ONDM65745.2025.11029345)
- <span id="page-14-1"></span>12. Iqbal, M.A.; Wright, P.; Parkin, N.; Lord, A. Performance Assessment of Hollow Core Fibre in High-Capacity National Backbone Networks. In Proceedings of the Conference on Lasers and Electro-Optics, San Jose, CA, USA, 15–20 May 2022; p. SM2J.1. [\[CrossRef\]](http://dx.doi.org/10.1364/CLEO_SI.2022.SM2J.1)
- <span id="page-14-2"></span>13. Correia, B.; Pedro, J.; Costa, N. Hollow-Core Fiber Specifications for Competitive Deployment in Regio/Long-Haul Optical Networks. In Proceedings of the Optical Fiber Communication Conference (OFC), San Francisco, CA, USA, 30 March–3 April 2025; p. Tu3I.3. [\[CrossRef\]](http://dx.doi.org/10.1364/OFC.2025.Tu3I.3)
- <span id="page-14-3"></span>14. Borzycki, K.; Osuch, T. Hollow-Core Optical Fibers for Telecommunications and Data Transmission. *Appl. Sci.* **2023**, *13*, 10699. [\[CrossRef\]](http://dx.doi.org/10.3390/app131910699)
- <span id="page-14-4"></span>15. Rapp, L.; Eiselt, M. Optical Amplifiers for Multi–Band Optical Transmission Systems. *J. Light. Technol.* **2022**, *40*, 1579–1589. [\[CrossRef\]](http://dx.doi.org/10.1109/JLT.2021.3120944)
- <span id="page-14-5"></span>16. Lundberg, L.; Andrekson, P.A.; Karlsson, M. Power Consumption Analysis of Hybrid EDFA/Raman Amplifiers in Long-Haul Transmission Systems. *J. Light. Technol.* **2017**, *35*, 2132–2142. [\[CrossRef\]](http://dx.doi.org/10.1109/JLT.2017.2668768)
- <span id="page-14-6"></span>17. Pedro, J.; Costa, N. Hybrid amplifier placement in mesh DWDM networks using integer linear programming models. *J. Opt. Commun. Netw.* **2023**, *15*, E29–E39. [\[CrossRef\]](http://dx.doi.org/10.1364/JOCN.493242)
- <span id="page-14-7"></span>18. Ferrari, A.; Filer, M.; Balasubramanian, K.; Yin, Y.; Rouzic, E.L.; Kundrát, J.; Grammel, G.; Galimberti, G.; Curri, V. GNPy: An open source application for physical layer aware open optical networks. *J. Opt. Commun. Netw.* **2020**, *12*, C31–C40. [\[CrossRef\]](http://dx.doi.org/10.1364/JOCN.382906)
- <span id="page-14-8"></span>19. Souza, A.; Costa, N.; Pedro, J.; Pires, J. Raman amplifier design and launch power optimization in multi-band optical systems. *J. Opt. Commun. Netw.* **2025**, *17*, A13–A22. [\[CrossRef\]](http://dx.doi.org/10.1364/JOCN.534006)
- <span id="page-14-9"></span>20. OpenROADM. OpenROADM Specifications v7.0. 2024. Available online: [https://view.officeapps.live.com/op/view.aspx?src=](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fwiki%2FOpenROADM%2FOpenROADM_MSA_Public%2Ffiles%2F20240307_open-roadm_msa_specification_ver7.0.xlsx&wdOrigin=BROWSELINK) [https%3A%2F%2Fraw.githubusercontent.com%2Fwiki%2FOpenROADM%2FOpenROADM\\_MSA\\_Public%2Ffiles%2F2024030](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fwiki%2FOpenROADM%2FOpenROADM_MSA_Public%2Ffiles%2F20240307_open-roadm_msa_specification_ver7.0.xlsx&wdOrigin=BROWSELINK) [7\\_open-roadm\\_msa\\_specification\\_ver7.0.xlsx&wdOrigin=BROWSELINK](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fwiki%2FOpenROADM%2FOpenROADM_MSA_Public%2Ffiles%2F20240307_open-roadm_msa_specification_ver7.0.xlsx&wdOrigin=BROWSELINK) (accessed on 7 February 2025).

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
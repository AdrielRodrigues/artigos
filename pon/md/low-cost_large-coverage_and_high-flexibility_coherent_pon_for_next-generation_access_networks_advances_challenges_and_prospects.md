---
title: "Low-cost, large-coverage, and high-flexibility coherent PON for next-generation access networks: advances, challenges, and prospects [Invited]"
tema_principal: pon
temas_relacionados: []
pdf: ../pdf/low-cost_large-coverage_and_high-flexibility_coherent_pon_for_next-generation_access_networks_advances_challenges_and_prospects.pdf
---

![](_page_0_Picture_1.jpeg)

# Low-cost, large-coverage, and high-flexibility coherent PON for next-generation access networks: advances, challenges, and prospects [Invited]

Sizhe Xing (邢思哲) $^{1,2}$ , Junwen Zhang (张俊文) $^{1,2^*}$ , Wangwei Shen (申王伟) $^{1,2}$ , An Yan (颜 安) $^{1,2}$ , Guoqiang Li (李国强) $^{1,2}$ , Aolong Sun (孙奥龙) $^{1,2}$ , Ji Zhou (周 骥) $^3$ , Dong Guo (郭 栋) $^4$ , Jianyang Shi (施剑阳) $^{1,2}$ , Ziwei Li (李子薇) $^{1,2}$ , Chao Shen (沈 超) $^{1,2}$ , and Nan Chi (迟 楠) $^{1,2}$ 

Received September 23, 2023 | Accepted December 1, 2023 | Posted Online April 18, 2024

Increasing bandwidth requirements have posed significant challenges for traditional access networks. It is difficult for intensity modulation/direct detection to meet the power budget and flexibility requirements of the next-generation passive optical network (PON) at 100G and beyond considering the new requirements. This is driving researchers to develop novel optical access technologies. Low-cost, wide-coverage, and high-flexibility coherent PON is emerging as a strong contender in the competition. In this article, we will review technologies that reduce the complexity of coherent PON (CPON), enabling it to meet the commercial requirements. Also, advanced algorithms and architectures that can enhance system coverage and flexibility are also discussed.

**Keywords:** access network; coherent optics; flexible data rate; low complexity; wide dynamic range. **DOI:** 10.3788/COL202422.040604

#### 1. Introduction

With the advent of the fifth generation fixed network (F5G) era, a host of transformative functionalities are becoming a reality. F5G is emerging as a pivotal enabler for various applications, encompassing the Internet of Things, 8K/16K streaming, mixed reality, and more. Access networks, such as passive optical networks (PONs), form the last-mile connectivity for end-users and are instrumental in harnessing the full potential of F5G. These networks must be capable of handling the increased data rates and low-latency requirements of F5G<sup>[1-4]</sup>, thereby serving as a critical bridge between the core F5G infrastructure and endusers. The current standards of IEEE's 25/50G NG-EPON and the ITU-T 50 GPON are anticipated to no longer meet the market's demands, necessitating the pursuing for 100G and even beyond 200G PON networks<sup>[5-7]</sup>. However, it is becoming more and more difficult for conventional intensity modulation and direct detection (IM/DD) technology to support such a high speed, considering the power budget. Considering the development trend of PON, the 200G PON

network is considered to be the most powerful contender for the next generation network. Although some work has demonstrated its feasibility, it comes at the cost of high equipment expenses<sup>[8,9]</sup>. Coherent optical technology is a powerful solution that has proved its superior sensitivity and high-speed performance in long-haul and core networks. Coherent PONs (CPONs) with high-speed and large dynamic ranges have been demonstrated in recent years  $^{[10-12]}$ . Low-cost coherent communication systems over 200G have been proposed by simplifying the transceiver<sup>[13–15]</sup>. By enhancing the system dynamic range through electric or optical adjustment, 200G coherent PONs with ultra-large dynamic range have been proposed [10,16,17]. Various schemes supporting flexible coherent PON networks over 200G have also been validated<sup>[11,18–20]</sup>. The current standard and the state-of-the-art works in the field of CPON are shown in Table 1. The power budgets of all technologies, aside from the standard ones, are displayed at a 200G line rate.

As shown in Fig. 1(a), PON is a point-to-multipoint system that comprises an optical line terminal (OLT) and numerous optical network units (ONUs). Therefore, it is more

<sup>1</sup> Key Laboratory of EMW Information (MoE), Fudan University, Shanghai 200433, China

<sup>&</sup>lt;sup>2</sup> Department of Communication Science and Engineering, Shanghai ERC of LEO Satellite Communication and Applications, Shanghai CIC of LEO Satellite Communication Technology, Fudan University, Shanghai 200433, China

<sup>&</sup>lt;sup>3</sup> Department of Electronic Engineering, Jinan University, Guangzhou 510632, China

 $<sup>^4</sup>$ School of Information and Electronics, Beijing Institute of Technology, Beijing 100081, China

<sup>\*</sup>Corresponding author: junwenzhang@fudan.edu.cn

<span id="page-1-0"></span>Table 1. Typical Research on CPON.

| Low-Cost<br>(Y/N) | Power<br>Budget (dB) | Flexibility<br>(Y/N)                                                                                                                           | Line Rate<br>(Gb/s)                                                                                                                                                                                            |
|-------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| N                 | 20                   | N                                                                                                                                              | 50                                                                                                                                                                                                             |
| Υ                 | 32.5                 | N                                                                                                                                              | 200                                                                                                                                                                                                            |
| Υ                 | 33                   | N                                                                                                                                              | 200                                                                                                                                                                                                            |
| N                 | 38                   | N                                                                                                                                              | 200                                                                                                                                                                                                            |
| N                 | 31                   | Υ                                                                                                                                              | 300                                                                                                                                                                                                            |
| N                 | >24                  | Υ                                                                                                                                              | 400                                                                                                                                                                                                            |
|                   | (Y/N)  N  Y  Y  N  N | (Y/N)         Budget (dB)           N         20           Y         32.5           Y         33           N         38           N         31 | (Y/N)         Budget (dB)         (Y/N)           N         20         N           Y         32.5         N           Y         33         N           N         38         N           N         31         Y |

cost-sensitive compared to other point-to-point systems. To reduce the power consumption and thereby meet the size and cost requirements for access applications, numerous methods of low complexity coherent architectures and digital signal processing (DSP) have been proposed, such as Alamouti coding, heterodyne detection, and intensity modulation with coherent detection<sup>[15,21,22]</sup>. The Alamouti receiver is shown in Fig. 1(b) as a representative, which is polarization-independent assisted by a space-time block coding scheme, achieving a significant complexity reduction in a coherent ONU receiver<sup>[23]</sup>. These solutions make the deployment of coherent PONs possible.

Coherent reception lays the groundwork for advanced DSP technology, enabling the recovery of distortions such as dispersion and frequency offset. Additionally, it supports signal transmission in the low-loss C-band, significantly extending the signal's reach length. Leveraging the unique architecture of coherent reception, the local oscillator (LO) can provide coherent beating gain and thereby enhance the power budget. Also, by adjusting the LO power, the system can adapt to a wider range of

received power, resulting in a wider dynamic range<sup>[17,24]</sup>. Leveraging these technologies, CPONs can offer wide coverage and work under various channel conditions, including optical path loss (OPL), fiber length, and nonlinearity.

In traditional PON, all users are provided with the same net data rate (NDR). However, different users possess varying channel conditions, which can limit the peak rate to that of the poorest ONU. Flexible PON (FLCS-PON) was initially introduced to address this issue by offering different NDRs to different users. This technology was originally demonstrated in IM/DD systems by the adaptive coding rate method. In coherent systems, due to the increased operational dimensions, it can provide even greater flexibility in speed regulation. Three typical FLCS-CPON methods are listed in Fig. 1(d), including the time and frequency division multiplexing (TFDM) CPON architecture [19,25], adaptive coded-modulation approach [11,26], probabilistic shaping (PS)-based entropy adjusted CPON [10,18,27,28]. The abbreviations "K," "M," "S," and "P" in the context of FEC coding methods denote the information length, parity length, shortening length, and puncturing length, respectively. Further details can be found in Ref. [29].

These approaches can offer fine adjustment granularity, enabling the full utilization of each user's channel condition and maximizing the overall throughput.

In this article, we initially discuss several cost-effective coherent architectures, encompassing the simplified transmitter, receiver, and equalization algorithms. Subsequently, we introduce solutions for achieving extensive coverage through algorithmic and architectural innovations. Lastly, two demonstrations of FLCS-CPON are shown, one leveraging PS technology and the other utilizing the TFDM architecture. These demonstrations serve as exemplary models for next-generation CPON, exhibiting characteristics of low cost, wide coverage, and flexibility.

![](_page_1_Figure_10.jpeg)

Fig. 1. (a) Point-to-multipoint schematic of the CPON system; (b)–(d) present the three key advancements in next-generation CPON, low cost, wide coverage, and high flexibility.

# 2. Low-Cost Optimization of Coherent Optics for PON

Coherent optics is renowned for its exceptional sensitivity and high spectral efficiency[\[4,5](#page-7-0),[30,31\]](#page-8-0) . Nonetheless, the adoption of this technology in access networks has been limited due to the significant complexity of its components and DSP. Cost is the challenge that must be resolved to introduce coherent optics into access networks. In order to tackle the cost issue, several low-cost coherent architectures have been proposed, which target the reduction of expenses in the transmitter, receiver, and DSP, respectively. In this section, we will delve into the low-cost optimization of coherent optics for passive optical networks, focusing on both upstream and downstream scenarios. As PON includes one OLT and numerous ONUs, the ONU side is more cost-sensitive. Therefore, the primary simplification strategies are aimed at reducing complexity at the ONU. In the upstream scenario, the primary objective is to reduce the complexity of the transmitter. And in the downstream scenario, the complexity of the receiver should be kept as minimal as possible. When discussing the low-cost optimization of coherent PON, it is important to mention that the benefits come with sacrifices in terms of rate and sensitivity. For example, the modulation dimensions are reduced to one, and the simplification of the receiver decreases signal sensitivity. These factors should be taken into account when considering these approaches.

# 2.1. Upstream

To reduce costs at the user end, the Mach–Zehnder modulator (MZM) is considered as an alternative to IQ modulators. Based on this transmitter configuration, three feasible simplified transmitter schemes are presented in Fig. 2. Figure 2(a) represents the IM scheme, aiming to achieve equal power differences between different signals, as indicated by the eye diagram where different signals have equal optical power differences. However, after coherent reception, the signal's amplitude is no longer uniformly distributed, requiring squaring of the signals to obtain the final output. The drawback of this scheme is that, as the final reception is an intensity signal, it prevents signal processing in the complex domain. Nonetheless, the advantage lies in having the same receiver DSP as the DD scheme, leading to the simplest DSP operations. Additionally, it exhibits excellent tolerance to frequency offset. In Ref. [\[32\]](#page-8-0), by adopting this approach in conjunction with a 3 × 3 coupler, −21.4 dBm optical sensitivity at 50 Gb/s has been achieved. Correspondingly, the receiver has also been simplified to a certain extent, which would impact the system's sensitivity.

The other two amplitude modulation schemes are shown in Figs. 2(b) and 2(c). Both schemes operate in the complex domain, allowing for more sophisticated DSP and the potential for superior performance. The difference between the two lies in that the scheme in Fig. 2(b) does not utilize phase information, while the scheme in Fig. 2(c) additionally utilizes phase information, specifically only 0° and 180°. Consequently, the scheme in

![](_page_2_Figure_7.jpeg)

Fig. 2. (a) Intensity signal with coherent detection and DSP; (b) amplitude signal with coherent detection and DSP; (c) PAM-4 ASK signal coherent detection and DSP.

Fig. 2(c) requires carrier recovery to obtain accurate phase information. Based on the scheme in Fig. 2(b), Ref. [[33](#page-8-0)] has achieved the first single-wavelength 100-Gb/s PAM-4 TDM-PON transmission in the C-band with over 32 dB power budget using simplified and phase insensitive coherent detection. The scheme in Fig. 2(c) has been demonstrated in Ref. [[15](#page-8-0)], and a 200 Gb/s PDM-PAM-4 signal was transmitted over 20 km fiber with an over 29 dB power budget using heterodyne coherent detection.

#### 2.2. Downstream

In the downstream scenario, users receive signals from the OLT. Simplifying the coherent receiver structure can significantly reduce costs. Figure 3(a) illustrates the structure of a dual-polarization coherent receiver, which requires two  $90^{\circ}$  hybrids and four balanced photodiodes (BPDs). In Figs. 3(b)-3(e), several representative simplified coherent receivers are shown, which can inherit the capability of using LO to provide power gain while reducing the expenses of components and DSP.

Figure 3(b) shows a DP-heterodyne coherent receiver with two  $2 \times 2$  couplers and two BPDs. The receiver current from one polarization can be calculated by [15,34,35]

$$i_{x/y} = 2 R E_{x/y} E_{LO} \cos(2\pi \Delta \omega t + \theta), \qquad (1)$$

where R is the photodiode responsivity.  $E_{x/y}$  and  $E_{LO}$  represent the amplitude of the signal and LO, respectively.  $\Delta \omega$  is the frequency offset between the signal and LO, and  $\theta$  is the phase noise.

The coherent detection structure can be further simplified to just two SPDs and one  $2 \times 2$  coupler, as shown in Fig. 3(c). Due to only one of the coupler's outputs being detected, there is a natural 3 dB power loss. By pre-designing to ensure that the polarization beam splitter (PBS) can split two polarizations of LO signals with the same amplitude, both being  $E_{\rm LO}$ , the current of a single channel can be represented as follows:

$$\begin{split} i_{x/y} &= R \left| \frac{E_{x/y} + E_{LO}}{\sqrt{2}} \right|^2 \\ &= \frac{R}{2} (E_{x/y}^2 + E_{LO}^2 + 2E_{x/y} E_{LO} \cos(2\pi \Delta \omega t + \theta)) \\ &\approx \frac{R}{2} (E_{LO}^2 + 2E_{x/y} E_{LO} \cos(2\pi \Delta \omega t + \theta)). \end{split} \tag{2}$$

Next, the direct current (DC) offset of the LO–LO beating term can be removed using a DC blocker. However, while the structure becomes simpler, the output signal's power is reduced compared to Eq. (1).

The structure shown in Fig. 3(d) can receive only a single polarization signal. However, it offers advantages over the scheme in Fig. 3(b) as it uses only three single-ended photodiodes (SPDs) and a  $3\times3$  coupler, making it less complex. Additionally, it can achieve higher sensitivity compared to the scheme in Fig. 3(c). The output of the coupler can be expressed as  $^{[35-37]}$ 

$$\begin{pmatrix} E_{1,x} & E_{1,y} \\ E_{2,x} & E_{2,y} \\ E_{3,x} & E_{3,y} \end{pmatrix} = \begin{pmatrix} a & b & b \\ b & a & b \\ b & b & a \end{pmatrix} \begin{pmatrix} E_{k,x} & E_{k,y} \\ E_{\text{LO},x} & 0 \\ 0 & E_{\text{LO},y} \end{pmatrix}, \quad (3)$$

where k is the channel number. The coefficients a and b are simply given by Ref. [38] as

$$a = 2 \exp(j2\pi/9)/3 + \exp(-j4\pi/9)/3,$$
  

$$b = \exp(-j4\pi/9)/3 - \exp(j2\pi/9)/3,$$
(4)

and the three currents can be simply derived by  $i_k = R(|E_{k,x}|^2 + |E_{k,y}|^2)$ . By summing the squares of the three currents, we can obtain the final output as follows:

$$S(t) = \frac{2}{3}R^2 E_{LO}^2 E_S^2 \left( 1 - \sin(2\varphi) \times \sin\left(\frac{\pi}{6} - 4\pi\Delta\omega t - \psi\right) \right),\tag{5}$$

where  $E_S$  is the modulated amplitude,  $\varphi$  is the orientation of the main axis of the polarization ellipse, and  $\psi$  is the SOP ellipticity angle<sup>[36]</sup>. This scheme has the advantage of being polarization-independent. However, it can only detect the intensity information of the signal.

The structure shown in Fig. 3(d) is another simplified single-polarization heterodyne receiver, which is known as the receiver of Alamouti coded signals  $^{[21,23,39-41]}$ . It consists of a  $2 \times 2$  coupler and a BPD. This type of receiver has specific requirements for the transmitted signal. The symbols are grouped into pairs of time slots  $^{[39]}$ . It transfers the single polarization signal to an Alamouti dual-polarization signal on a single block as

![](_page_3_Figure_18.jpeg)

Fig. 3. The concept of coherent receiver simplification schemes. (a) A DP-intradyne receiver; (b) a DP-heterodyne receiver; (c) a 2 × 2 coupler and single-ended PD (SPD)-based heterodyne receiver; (d) a single polarization heterodyne coherent receiver with a 3 × 3 coupler; and (e) an Alamouti single-polarization heterodyne receiver.

![](_page_4_Picture_2.jpeg)

Fig. 4. The system diagram based on Alamouti coding

$$\begin{bmatrix} E_{x1} & E_{x2} \\ 0 & 0 \end{bmatrix} \Rightarrow \begin{bmatrix} E_{x1} & -E_{x2}^* \\ E_{x2} & E_{x1}^* \end{bmatrix}, \tag{6}$$

where  $E_{x1}$  and  $E_{x2}$  are two consecutive symbols on *X*-polarization, and \* represents the complex conjugate operation. The system diagram based on Alamouti coding is shown in Fig. 4.

At the receiver end, coherent DSP also consumes a significant amount of power, which needs to be reduced for application in the ONU. Among those processes, the adaptive equalization (AEQ) has the greatest circuit complexity [42]. In Ref. [43], by splitting the conventional AEQ into a 1-tap butterfly finite impulse response (FIR) filter and two nonbutterfly FIR filters, the proposed scheme can reduce the number of taps by half. And the number of multiplications is reduced by 41% compared with more conventional cases. Frequency domain (FD) signal equalization is also an effective way to reduce DSP complexity. An FD training-aided equalization supported by  $2 \times 2$  multiinput multi-output channel estimation is proposed in Ref. [44]. The FD filter provides the receiver with the advantage of being independent from the filter length. And the robustness of the proposed methods is demonstrated with respect to the main degrading optical propagation effects. In recent years, there have been studies aimed at reducing the complexity of nonlinear equalization algorithms<sup>[45-48]</sup>. However, due to a comprehensive consideration of cost and benefits, nonlinear equalization has not been practically applied in PON systems.

## 3. Coherent Detection Enabled Wide Coverage

In access networks, different users experience varying channel conditions influenced by factors such as transmission distance and splitting ratios. These introduce distortions like dispersion and losses. IM/DD access networks face challenges in covering areas with either excessively low or high OPL. When the OPL is too high, the received signal is adversely affected by limited SNR and significant dispersion, resulting in severe degradation. Conversely, for users with excessively low OPL, additional nonlinearity can be introduced during burst mode due to limitations in the ADC range. However, coherent detection technology can significantly enhance the coverage area of access networks. This advantage is primarily based on advanced DSP techniques [49–54] and the power gain provided by LO.

The DSP processes of coherent detection are in Fig. 5. In the downstream mode, the signal is broadcasted from the OLT to all users, which is also known as continuous mode. The OLT receiver will compensate chromatic dispersion (CDC), lock the clock, correct the state of polarization, and handle the

![](_page_4_Figure_10.jpeg)

Fig. 5. Advanced DSP in both upstream and downstream.

frequency offsets, phases, and other channel responses. This approach can significantly enhance the sensitivity, enabling the system to maintain a dynamic range of 20 dB at a data rate of up to  $300G^{[10]}$  and achieve a dynamic range of 39 dB at a speed of  $200G^{[55]}$ . The dynamic range refers to the range of variation in the power of the received signal. In a coherent PON system, due to the shorter transmission distance and the ability to compensate for dispersion, the split ratio is the most significant factor affecting the received power.

In the upstream mode, the OLT receives signals from different users, also known as burst mode. Hence, the receiver at this stage must be capable of recognizing the modulation formats of received signals and performing fast detection with various channel impairments they experience. It needs to handle different clocks, random SOP, different carrier frequency offsets and phases, and different channel responses from different bursts <sup>[56]</sup>. The frame structure shown in Fig. 5 is designed for fast convergence to ensure a low handoff latency for real-time bandwidth allocation <sup>[57]</sup>. Different synchronization patterns (SPs) serve different functions, corresponding to the DSP processes in burst mode. Due to the burst-mode reception, uneven error distribution can lead to a decrease in FEC performance <sup>[58]</sup>. Some solutions such as bit interleaving coding have been proposed to alleviate this issue <sup>[59]</sup>.

Recently, there have been studies proposing new specially designed SP structures and novel equalization methods to accelerate convergence rates and enhance the range of supported channel conditions in CPON systems<sup>[27,60,61]</sup>. By using an inserted pilot structure, it can realize fast SOP, carrier phase tracking, and channel estimation. The pre-stored FIR coefficients can also be used to reduce the convergence time. Several neural network-based equalization methods have been proposed to achieve more efficient channel equalization<sup>[62,63]</sup>. For instance, leveraging end-to-end optimized deep neural networks has been shown to highly enhance sensitivity<sup>[55]</sup>.

In upstream, due to the limitations of ADC range, utilizing a burst-mode fast tunable amplifier is an effective solution to widen the receiver input dynamic range. Electronic burst-mode amplification techniques have been extensively studied for this purpose<sup>[16,64]</sup>. Harnessing the distinctive architecture of a coherent receiver, optical burst-mode amplification can be realized through the integration of a power-controlled LO. The power of the output signal from a coherent receiver can be represented as

$$\begin{split} I_{I}(t) &= A_{\text{TIA}} \cdot \frac{R}{2} (E_{\text{sig}}(t) \cdot E_{\text{LO}}^{*}(t) + E_{\text{Sig}}^{*}(t) \cdot E_{\text{LO}}(t)) \\ &= A_{\text{TIA}} \cdot R \sqrt{P_{\text{Sig}} P_{\text{LO}}} \cos(\phi_{\text{Sig}} - \phi_{\text{LO}}), \\ I_{Q}(t) &= A_{\text{TIA}} \cdot \frac{R}{2} (E_{\text{sig}}(t) \cdot E_{\text{LO}}^{*}(t) e^{-j\pi/2} + E_{\text{Sig}}^{*}(t) \cdot E_{\text{LO}}(t) e^{j\pi/2}) \\ &= A_{\text{TIA}} \cdot R \sqrt{P_{\text{Sig}} P_{\text{LO}}} \sin(\phi_{\text{Sig}} - \phi_{\text{LO}}), \end{split} \tag{7}$$

![](_page_5_Figure_4.jpeg)

**Fig. 6.** Two examples of the possible implementation of LO power adjustment: (a) adjustment based on the detected photocurrent output from the photodiodes; (b) adjustment based on the optical input signal power.

where  $E_{\text{sig}}(t)$  and  $E_{\text{LO}}(t)$  represent the electric fields of the input signal and LO, respectively;  $\phi_{\mathrm{Sig}}$  and  $\phi_{\mathrm{LO}}$  represent the phases of the input signal and LO, respectively; and R and  $A_{TIA}$  represent the responsivity of the BPDs and TIA, respectively. Thus, the flexible adjustment of the LO power enables effective control of the received signal's power. To maintain LO wavelength stability, a variable optical attenuator (VOA) can be utilized to regulate the LO's light power<sup>[24]</sup>. Figure 6 illustrates two possible implementations for adjusting the LO power. The difference between these two methods lies in the origin of the reference signal employed to adjust the LO power. The first scheme in Fig. 6(a) regulates the LO power by monitoring the magnitude of the electrical signal at the input ADC. In the alternative scheme, the intensity of the signal light serves as the reference. When the signal light increases, the LO power is decreased, and when the signal light decreases, the LO power is increased. This strategy ensures the steadfastness of the received electrical signal<sup>[17,24,30]</sup>, while the first approach has lower cost.

We tested the effect of LO power adjustment on dynamic range. Figure 7 displays the BER curves for QPSK, 16QAM, and 64QAM with and without LO power adjustment. When LO power adjustment is not used and the scale is set to  $0.1V_{\rm max}$  with an LO power of 10 dBm, the dynamic ranges of QPSK, 16QAM, 64QAM are 32.6 dB, 18 dB, 5 dB respectively. LO power can be adjusted to achieve higher dynamic ranges. As the received optical power (ROP) increases, the LO power is gradually decreased to maintain the BER below the threshold. Because of the inherent attenuation of the 20 km fiber, the maximum ROP can only reach -4 dBm, and at this point, the BER of the signals for all three modulation formats has not yet exceeded the threshold. Therefore, LO power adjustment can significantly increase the dynamic range of the signal.

## 4. Rate-Adaptive Accesses for Flexible CPON

In the conventional access network where only one rate is transmitted in the system, the peak rate is limited by the worst ONU. How to fully utilize the channel conditions of all users is a challenge. The concept of FLCS-PON is introduced to address this challenge. This technology can tailor the NDR for each user by

![](_page_5_Figure_10.jpeg)

Fig. 7. BER performance versus different ROP with or without LO adjustment in (a) QPSK, (b) 16QAM, and (c) 64QAM.

considering their unique channel conditions, such as nonlinearity, attenuation, and noise. Several methods have been demonstrated in IM/DD PON to realize adaptive rate adjustment, such as PS and adaptive FEC coding rate. With the expansion of modulation dimensions and advancements in signal processing techniques brought about by coherent detection, we gain increased flexibility in manipulating signals. Several ways of changing the entropy of the signal in the CPON system have been put forward, including TFDM CPON architecture<sup>[19,25]</sup>, adaptive coded-modulation approach<sup>[11]</sup>, and PS-based entropy adjusted CPON<sup>[18,55,65,66]</sup>.

In Fig. 8, we show a PS-based FLCS-CPON system. PS is a technique that adjusts the entropy of transmitted signals by changing the signal's distribution<sup>[67–72]</sup>. As shown in the setup, only single-mode fiber (SMF) exists between the transmitter and receiver. Due to the improved sensitivity in the coherent system, optical amplifiers can be eliminated to lower the cost. HPS is employed in such a peak-power constraint (PPC) system. The transmitted signal first undergoes the distribution matcher (DM), which is the most significant process. The task of the DM is to transform a sequence of bits into a probabilistic shaped amplitude at the transmitter and to carry out the inverse operation at the receiver<sup>[73]</sup>. Given CCDM's serial nature, complexity increases with block size<sup>[74]</sup>, creating a complexity-rate tradeoff. In FLCS-PON, we support 2 dB rate-change fitness, accepting short blocks for lower complexity. Shaping methods for shorter block lengths have been studied to address this [75,76]. The probability distribution of the constellation symbols is adjusted to approximate the Maxwell-Boltzmann distribution,

$$P_X(x) = \frac{e^{-\nu|x|^2}}{\sum_{x' \in X} e^{-\nu|x'|^2}},$$
 (8)

where v is a shaping factor to control the entropy. x and x' represent the constellation symbols on the complex plane. In classical probabilistic shaping (CPS) method, the v is always greater than 0. And the inner points exhibit a higher probability than the points in outer rings. As the value of v increases, the probability of outer ring points also increases. The method

![](_page_6_Figure_6.jpeg)

Fig. 8. Schematic of a hybrid PS (HPS)-based flexible CPON system without any optical amplifiers.

HPS combines the CPS and reversed PS (RPS). RPS is the better solution in a PPC system that can help reach a higher NDR [20,69]. And CPS shows its capability to counteract the clipping nonlinearity in burst-mode. In the HPS system, the constellation entropy decreases as the absolute value of  $\nu$  increases from 0. When  $\nu$  is 0, the constellation yields to the equal distribution. The constellation entropy H can be calculated by

$$H = -\sum_{x \in X} P_X(x) \log_2(P_X(x))$$

$$= -\sum_{x \in X} \frac{e^{-\nu|x|^2}}{\sum_{x' \in X} e^{-\nu|x'|^2}} \log_2\left(\frac{e^{-\nu|x|^2}}{\sum_{x' \in X} e^{-\nu|x'|^2}}\right). \tag{9}$$

And the corresponding NDR can be calculated accordingly as

$$NDR = B \times (H - (1 - R_c)m), \tag{10}$$

where B,  $R_c$ , and m correspond to the modulation bandwidth, FEC code rate, and constellation modulation order, respectively.

The frame generation and frame detection are utilized in burst-mode to make sure the start of a signal frame can be detected and equalized quickly. Several 3D constellations are also placed at the bottom of the figure, the shaping factor  $\nu$  of which varies from -0.1 to 0.1.

Recently, TFDM-based FLCS-CPON has attracted the attention of many researchers<sup>[19,25,77]</sup>. By utilizing the multiple dimensions of coherent signals, TFDM CPON can provide more flexible bandwidth allocation. Huawei's latest research showcases a simplified CPON system based on the TFDM architecture. This study introduces a distinctive FD signal design that leads to the simplification of ONU transceivers. This achievement can significantly reduce costs at the user end and realize a flexible rate adjustment at the same time<sup>[78]</sup>. The architecture of the simplified TFDM-CPON is shown in Fig. 9. Five digital subcarriers are transmitted, while only four of them carry data. The middle one is a blank carrier required by heterodyne detection. To meet the changing needs of all ONUs, FLCS-CPON can schedule resources in two dimensions: time and frequency. In the time dimension, each subcarrier can transmit varying QAM orders at different times. Additionally, PS technology can also be used to finely adjust the transmitted data entropy. In the frequency dimension, each subcarrier can transmit QAM of different orders at the same time. The subcarrier allocation for each user can also be adjusted to provide users with varying rates. To reduce the cost of an ONU, a single-polarization heterodyne receiver based on Alamouti coding can be used. And the upstream data can also be transmitted by an MZM.

#### 5. Conclusion and Prospects

In this article, we have reviewed the recent progress for using a low-cost, wide-coverage, and high-flexibility CPON for next generation 100G and beyond access networks. The high complexity of coherent receivers is the major factor limiting their

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

Fig. 9. The architecture of simplified TFDM CPON with adaptive rate.

application in access networks. This article comprehensively discusses methods to effectively reduce complexity, covering the transmitter, receiver, and DSP algorithm. These techniques enable significant cost reduction at the ONU end in both upstream and downstream scenarios, meeting commercial requirements. Due to the beating gain from the LO, coherent receivers inherently have a significant high sensitivity. Additionally, coherent receivers support the utilization of more powerful DSP algorithms at the receiving end. This article shows several recently proposed advanced techniques that can effectively mitigate channel noise and enable a larger dynamic range. The flexibility of the PON is another research hotspot. FLCS-PON can greatly increase the overall throughput of the system. Adaptive FEC coding and PS are commonly used methods in IM/DD systems to enhance flexibility. They have also been proven feasible in CPON. Another approach enabled by coherent receivers is the TFDM. Two typical FLCS-CPON schemes are introduced in the paper, which simultaneously consider low cost, wide coverage, and high flexibility. These schemes demonstrate the integration of these three aspects in the CPON and serve as templates for the future development of CPON.

Looking ahead, the prospects for CPON technology appear promising. As research and development continue, we anticipate further innovations that will refine CPONs for broader adoption in access networks. Enhanced integration of low-cost, wide-coverage, and high-flexibility aspects will be a key focus. Aided by these advanced technologies, we foresee CPONs contributing significantly to the realization of the sixth-generation fixed network (F6G). It can not only satisfy the growing bandwidth demands but also make "fiber to the X" (FTTX) a practical reality, where X represents the home (FTTH), office (FTTO), building (FTTB), and mobile cell (FTTC)<sup>[6,79]</sup>. The F6G is poised to address the unique challenges presented by these applications, such as stringent power budgets and the need for adaptive data rates. Low-cost, wide-coverage, and high-flexibility CPON technology is on a trajectory of continuous

improvement and adaptation, which will provide significant support for the construction of the F6G.

# **Acknowledgements**

This work was supported in part by the National Key Research and Development Program of China (No. 2023YFB2905700), in part by the National Natural Science Foundation of China (Nos. 62171137, 62235005, and 61925104), and in part by the Natural Science Foundation of Shanghai (No. 21ZR1408700).

#### References

- D. Zhang, D. Liu, X. Wu, et al., "Progress of ITU-T higher speed passive optical network (50G-PON) standardization," J. Opt. Commun. Netw. 12, D99 (2020).
- Z. Jia and L. A. Campos, "Coherent optics ready for prime time in short-haul networks," IEEE Netw. 35, 8 (2021).
- J. S. Wey and J. Zhang, "Passive optical networks for 5G transport: technology and standards," J. Lightwave Technol. 37, 2830 (2019).
- K. Kikuchi, "Fundamentals of coherent optical fiber communications," J. Lightwave Technol. 34, 157 (2016).
- M. S. Faruk, X. Li, D. Nesset, et al., "Coherent passive optical networks: why, when, and how," IEEE Commun. Mag. 59, 112 (2021).
- J. Zhang and Z. Jia, "Coherent passive optical networks for 100G/λ-andbeyond fiber access: recent progress and outlook," IEEE Netw. 36, 116 (2022).
- D. Lavery, S. Erkilinç, P. Bayvel, et al., "Recent progress and outlook for coherent PON," in Optical Fiber Communications Conference and Exposition (OFC) (2018), p. 1.
- D. Che and X. Chen, "Modulation format and digital signal processing for IM-DD optics at post-200G era," J. Lightwave Technol. 42, 588 (2024).
- J. Li, X. Li, M. Luo, et al., "Demonstration of 200 Gb/s/λ PON in O-band with high-bandwidth TFLN modulator," J. Lightwave Technol. 41, 3594 (2023).
- S. Xing, G. Li, A. Sun, et al., "Demonstration of PS-QAM based flexible coherent PON in burst-mode with 300G peak rate and ultra-wide dynamic range," J. Lightwave Technol. 41, 1230 (2023).
- M. Xu, H. Zhang, Z. Jia, et al., "Adaptive modulation and coding scheme in coherent PON for enhanced capacity and rural coverage," in Optical Fiber Communication Conference (OFC) (2021), paper Th5I.4.

- <span id="page-8-0"></span>12. R. Ullah, S. Ullah, A. Ali, et al., "Optical 1.56 Tbps coherent 4-QAM transmission across 60 km SSMF employing OFC scheme," [AEU Int. J. Electron.](https://doi.org/10.1016/j.aeue.2019.04.004) [Commun.](https://doi.org/10.1016/j.aeue.2019.04.004) 105, 78 (2019).
- 13. D. Zhang, X. Hu, X. Huang,et al.,"Experimental demonstration of 200 Gb/s/ λ coherent PON with a low-complexity receiver and a multi-purpose neural network," in Optical Fiber Communication Conference (OFC) (2022), paper Th3E.4.
- 14. A. Hraghi, G. Rizzelli, A. Pagano,et al.,"Analysis and experiments on C band 200G coherent PON based on Alamouti polarization-insensitive receivers," [Opt. Express](https://doi.org/10.1364/OE.472470) 30, 46782 (2022).
- 15. J. Zhang, J. Yu, X. Li,et al.,"200 Gbit/s/λ PDM-PAM-4 PON system based on intensity modulation and coherent detection," [J. Opt. Commun. Netw.](https://doi.org/10.1364/JOCN.12.0000A1) 12, A1 (2020).
- 16. R. Koma, M. Fujiwara, J. Kani, et al., "Wide dynamic range burst-mode digital coherent detection using fast ALC-EDFA and pre-calculation of FIR filter coefficients," in Optical Fiber Communication Conference (2016), paper M3C.6.
- 17. G. Li, S. Xing, J. Jia, et al., "Local oscillator power adjustment-based adaptive amplification for coherent TDM-PON with wide dynamic range," [J.](https://doi.org/10.1109/JLT.2022.3216763) [Lightwave Technol.](https://doi.org/10.1109/JLT.2022.3216763) 41, 1240 (2022).
- 18. Z. Wei, J. Zhang, W. Li, et al., "400-Gbps/80-km rate-flexible PCS-64-QAM WDM-CPON with pseudo-m-QAM chaotic physical layer encryption," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2023.3235308) 41, 2413 (2023).
- 19. W. Shen, S. Xing, G. Li, et al., "Demonstration of beyond 100G three-dimensional flexible coherent PON in downstream with time, frequency and power resource allocation capability," in Optical Fiber Communications Conference (OFC) (2023), paper W1I.5.
- 20. S. Xing, G. Li, A. Yan, et al., "Principle and strategy of using probabilistic shaping in a flexible coherent passive optical network without optical amplifiers," [J. Opt. Commun. Netw.](https://doi.org/10.1364/JOCN.487860) 15, 507 (2023).
- 21. S. M. Alamouti, "A simple transmit diversity technique for wireless communications," [IEEE J. Sel. Areas Commun.](https://doi.org/10.1109/49.730453) 16, 1451 (1998).
- 22. A. Hraghi, G. Rizzelli, A. Pagano,et al.,"Analysis and experiments on C band 200G coherent PON based on Alamouti polarization-insensitive receivers," [Opt. Express](https://doi.org/10.1364/OE.472470) 30, 46782 (2022).
- 23. M. S. Erkilinc, R. Emmerich, K. Habel, et al., "PON transceiver technologies for ≥50 Gbits/s per λ: Alamouti coding and heterodyne detection [Invited]," [J. Opt. Commun. Netw.](https://doi.org/10.1364/JOCN.12.00A162) 12, A162 (2020).
- 24. S.-Y. Kim, J. Kani, J. Terada, et al., "A coherent-based OLT receiver with a power-controlled optical local oscillator for upstream OFDM/TDMA-PON," in Optical Fiber Communication Conference (OFC) (2014), paper Th3G.2.
- 25. J. Zhang, Z. Jia, H. Zhang, et al., "Rate-flexible single-wavelength TFDM 100G coherent PON based on digital subcarrier multiplexing technology," in Optical Fiber Communication Conference (OFC) (2020), paper W1E.5.
- 26. R. Borkowski, M. Straub, Y. Ou, et al., "World's first field trial of 100 Gbit/s flexible PON (FLCS-PON)," in European Conference on Optical Communications (ECOC) (2020), p. 1.
- 27. S. Yao, A. Mahadevan, Y. Lefevre, et al., "Artificial neural network assisted probabilistic and geometric shaping for flexible rate high-speed PONs," [J.](https://doi.org/10.1109/JLT.2023.3259929) [Lightwave Technol.](https://doi.org/10.1109/JLT.2023.3259929) 41, 5217 (2023).
- 28. R. Zhang, N. Kaneda, Y. Lefevre, et al., "Probabilistic and geometric shaping for next-generation 100G flexible PON," in European Conference on Optical Communications (ECOC) (2020), p. 1.
- 29. R. Borkowski, M. Straub, Y. Ou, et al., "FLCS-PON A 100 Gbit/s flexible passive optical network: concepts and field trial," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2021.3102383) 39, 5314 (2021).
- 30. G. Li, S. Xing, Z. Li, et al., "200-Gb/s/λ coherent TDM-PON with wide dynamic range of >30-dB based on local oscillator power adjustment," in Optical Fiber Communication Conference (OFC) (2022), paper Th3E.3.
- 31. L. A. Campos, Z. Jia, M. Xu, et al., "Coherent optics for access from P2P to P2MP," in Optical Fiber Communications Conference and Exhibition (OFC) (2022), paper Th3E.1.
- 32. V. Houtsma and D. Van Veen, "Bi-directional 25G/50G TDM-PON with extended power budget using 25G APD and coherent detection," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2017.2742465) 36, 122 (2017).
- 33. J. Zhang, J. S. Wey, J. Shi, et al., "Single-wavelength 100-Gb/s PAM-4 TDM-PON achieving over 32-dB power budget using simplified and phase insensitive coherent detection," in European Conference on Optical Communication (ECOC) (2018), p. 1

- 34. M. S. Erkilinc, D. Lavery, K. Shi,et al.,"Comparison of low complexity coherent receivers for UDWDM-PONs (λ-to-the-user),"[J. Lightwave Technol.](https://doi.org/10.1109/JLT.2018.2835376) 36, 3453 (2018).
- 35. Y. Zhu, L. Yi, B. Yang, et al., "Comparative study of cost-effective coherent and direct detection schemes for 100 Gb/s/λ PON," [J. Opt. Commun. Netw.](https://doi.org/10.1364/JOCN.390911) 12, D36 (2020).
- 36. E. Ciaramella, "Polarization-independent receivers for low-cost coherent OOK systems," [IEEE Photon. Technol. Lett.](https://doi.org/10.1109/LPT.2013.2296943) 26, 548 (2014).
- 37. J. Tabares, V. Polo, and J. Prat, "Polarization-independent heterodyne DPSK receiver based on 3 × 3 coupler for cost-effective udWDM-PON," in Optical Fiber Communications Conference and Exhibition (OFC) (2017), paper Th1K.3.
- 38. Y. H. Ja, "Analysis of four-port optical fiber ring and loop resonators using a 3 × 3 fiber coupler and degenerate two-wave mixing," [IEEE J. Quantum](https://doi.org/10.1109/3.166469) [Electron.](https://doi.org/10.1109/3.166469) 28, 2749 (1992).
- 39. Md. S. Faruk, H. Louchet, M. S. Erkılınç, et al., "DSP algorithms for recovering single-carrier Alamouti coded signals for PON applications," [Opt.](https://doi.org/10.1364/OE.24.024083) [Express](https://doi.org/10.1364/OE.24.024083) 24, 24083 (2016).
- 40. M. S. Faruk, X. Li, and S. J. Savory, "Experimental demonstration of 100/ 200-Gb/s/λ PON downstream transmission using simplified coherent receivers,"in Optical Fiber Communication Conference (OFC) (2022), paper Th3E.5.
- 41. M. S. Erkılınç, D. Lavery, K. Shi, et al., "Bidirectional wavelength-division multiplexing transmission over installed fibre using a simplified optical coherent access transceiver," [Nat. Commun.](https://doi.org/10.1038/s41467-017-00875-z) 8, 1043 (2017).
- 42. K. Matsuda and N. Suzuki, "Hardware-efficient signal processing technologies for coherent PON systems," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2018.2878408) 37, 1614 (2019).
- 43. K. Matsuda, R. Matsumoto, and N. Suzuki, "Hardware-efficient adaptive equalization and carrier phase recovery for 100-Gb/s/λ-based coherent WDM-PON systems," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2017.2784804) 36, 1492 (2018).
- 44. F. Pittala, I. Slim, A. Mezghani, et al., "Training-aided frequency-domain channel estimation and equalization for single-carrier coherent optical transmission systems," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2014.2358933) 32, 4849 (2014).
- 45. Y. Yu, T. Bo, Y. Che, et al., "Low-complexity nonlinear equalizer based on absolute operation for C-band IM/DD systems," [Opt. Express](https://doi.org/10.1364/OE.394961) 28, 19617 (2020).
- 46. Y. Fu, D. Kong, M. Bi, et al., "Computationally efficient 104 Gb/s PWL-Volterra equalized 2D-TCM-PAM8 in dispersion unmanaged DML-DD system," [Opt. Express](https://doi.org/10.1364/OE.384805) 28, 7070 (2020).
- 47. N.-P. Diamantopoulos, H. Nishi, W. Kobayashi, et al., "On the complexity reduction of the second-order Volterra nonlinear equalizer for IM/DD systems," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2018.2890118) 37, 1214 (2019).
- 48. G. S. Yadav, C.-Y. Chuang, K.-M. Feng, et al., "Reducing computation complexity by using elastic net regularization based pruned Volterra equalization in a 80 Gbps PAM-4 signal for inter-data center interconnects," [Opt. Express](https://doi.org/10.1364/OE.411465) 28, 38539 (2020).
- 49. H. Ji, L. Yi, L. Xue, et al., "Upstream dispersion management of 25 Gb/s duobinary and PAM-4 signals to support 0–40 km differential reach," [Chin. Opt. Lett.](https://doi.org/10.3788/COL201715.022502) 15, 022502 (2017).
- 50. W. Ren, J. Sun, P. Hou,et al.,"Direct phase control method for binary phaseshift keying space coherent laser communication," [Chin. Opt. Lett.](https://doi.org/10.3788/COL202220.060601) 20, 060601 (2022).
- 51. S. J. Savory, "Digital filters for coherent optical receivers," [Opt. Express](https://doi.org/10.1364/OE.16.000804) 16, 804 (2008).
- 52. C. Zhu, N. Kaneda, and J. Lee, "Reception of burst mode high-order QAM signals with pilot-aided digital signal processing," in Optical Fiber Communication Conference (2018), paper M1C.5.
- 53. Z. Y. Choi and Y. H. Lee, "Frame synchronization in the presence of frequency offset," [IEEE Trans. Commun.](https://doi.org/10.1109/TCOMM.2002.800815) 50, 1062 (2002).
- 54. F. Cao, M. Gao, P. Wang, et al., "Optimized blind equalization for probabilistically shaped high-order QAM signals," [Chin. Opt. Lett.](https://doi.org/10.3788/COL202220.080601) 20, 080601 (2022).
- 55. S. Xing, Z. Li, G. Li, et al., "End-to-end intelligent user-specific constellation optimization in PS-32-QAM-based flexible coherent PON with enhanced sensitivity and dynamic range," in European Conference on Optical Communications (ECOC) (2023).
- 56. J. Zhang, Z. Jia, M. Xu, et al., "Efficient preamble design and digital signal processing in upstream burst-mode detection of 100G TDM coherent-PON," [J. Opt. Commun. Netw.](https://doi.org/10.1364/JOCN.402591) 13, A135 (2021).
- 57. H. Wang, J. Zhou, Z. Xing, et al., "Fast-convergence digital signal processing for coherent PON using digital SCM,"[J. Lightwave Technol.](https://doi.org/10.1109/JLT.2023.3243828) 41, 4635 (2023).

- <span id="page-9-0"></span>58. N. Brandonisio, D. Carey, S. Porto, et al., "Burst-mode FEC performance for PON upstream channels with EDFA optical transients," in International Conference on Optical Network Design and Modeling (ONDM) (2018), p. 190.
- 59. M. Yang, L. Li, X. Liu, et al., "Real-time verification of soft-decision LDPC coding for burst mode upstream reception in 50G-PON," [J. Lightwave](https://doi.org/10.1109/JLT.2019.2961338) [Technol.](https://doi.org/10.1109/JLT.2019.2961338) 38, 1693 (2020).
- 60. H. Wang, J. Zhou, Z. Xing, et al., "Fast-convergence digital signal processing for coherent PON using digital SCM,"[J. Lightwave Technol.](https://doi.org/10.1109/JLT.2023.3243828) 41, 4635 (2023).
- 61. G. Li, A. Yan, S. Xing, et al., "Pilot-aided continuous digital signal processing for multi-format flexible coherent TDM-PON in downstream," in Optical Fiber Communications Conference and Exhibition (OFC) (2023), paper W1I.3.
- 62. V. Bajaj, F. Buchali, M. Chagnon, et al., "Deep neural network-based digital pre-distortion for high baudrate optical coherent transmission,"[J. Lightwave](https://doi.org/10.1109/JLT.2021.3122161) [Technol.](https://doi.org/10.1109/JLT.2021.3122161) 40, 597 (2022).
- 63. B. Karanov, M. Chagnon, F. Thouin, et al., "End-to-end deep learning of optical fiber communications," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2018.2865109) 36, 4843 (2018).
- 64. R. Koma, M. Fujiwara, J. Kani, et al., "Demonstration of real-time burstmode digital coherent reception with wide dynamic range in DSP-based PON upstream," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2016.2637357) 35, 1392 (2017).
- 65. W. Mo, J. Zhou, G. Liu, et al., "Simplified LDPC-assisted CNC algorithm for entropy-loaded discrete multi-tone in a 100G flexible-rate PON," [Opt.](https://doi.org/10.1364/OE.482952) [Express](https://doi.org/10.1364/OE.482952) 31, 6956 (2023).
- 66. S. Xing, G. Li, J. Chen, et al., "First demonstration of PS-QAM based flexible coherent PON in burst-mode with 300G peak-rate and record dynamicrange and net-rate product up to 7,104 dB·Gbps," in Optical Fiber Communications Conference and Exhibition (OFC) (2022), p. 1.
- 67. Z. Qu and I. B. Djordjevic,"On the probabilistic shaping and geometric shaping in optical communication systems," [IEEE Access](https://doi.org/10.1109/ACCESS.2019.2897381) 7, 21454 (2019).
- 68. T. Fehenberger, A. Alvarado, G. Bocherer, et al., "On probabilistic shaping of quadrature amplitude modulation for the nonlinear fiber channel," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2016.2594271) 34, 5063 (2016).

- 69. D. Che, J. Cho, and X. Chen,"Does probabilistic constellation shaping benefit IM-DD systems without optical amplifiers?" [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2021.3083530) 39, 4997 (2021).
- 70. G. Böcherer, F. Steiner, and P. Schulte,"Fast probabilistic shaping implementation for long-haul fiber-optic communication systems," in European Conference on Optical Communication (ECOC) (2017), p. 1.
- 71. H. Huang, Z. Yu, L. Shu, et al., "Low-resolution optical transmission using joint shaping technique of signal probability and quantization noise," [Chin.](https://doi.org/10.3788/COL202321.050602) [Opt. Lett.](https://doi.org/10.3788/COL202321.050602) 21, 050602 (2023).
- 72. M. Liu, M. Gao, and J. Ke,"Multi-distributed probabilistically shaped PAM-4 system for intra-data-center networks," [Chin. Opt. Lett.](https://doi.org/10.3788/COL202119.110604) 19, 110604 (2021).
- 73. T. Fehenberger, D. S. Millar, T. Koike-Akino, et al., "Partition-based probabilistic shaping for fiber-optic communication systems," in Optical Fiber Communication Conference (OFC) (2019), paper M4B.3.
- 74. M. Goukhshtein, S. C. Draper, and J. Mitra, "Probabilistic shaping using a block-based bit-level distribution matcher," in 17th Canadian Workshop on Information Theory (CWIT) (2022), p. 68.
- 75. D. S. Millar, T. Fehenberger, T. Koike-Akino, et al., "Distribution matching for high spectral efficiency optical communication with multiset partitions," [J. Lightwave Technol.](https://doi.org/10.1109/JLT.2018.2887188) 37, 517 (2019).
- 76. T. Fehenberger, D. S. Millar, T. Koike-Akino, et al., "Multiset-partition distribution matching," [IEEE Trans. Commun.](https://doi.org/10.1109/TCOMM.2018.2881091) 67, 1885 (2019).
- 77. M. Xu, Z. Jia, H. Zhang, et al., "Intelligent burst receiving control in 100G coherent PON with 4×25G TFDM upstream transmission," in Optical Fiber Communication Conference (OFC) (2022), paper Th3E.2.
- 78. Z. Xing, K. Zhang, X. Chen, et al., "First real-time demonstration of 200G TFDMA coherent PON using ultra-simple ONUs," in Optical Fiber Communications Conference and Exhibition (OFC) (2023), paper Th4C.4.
- 79. D. Uzunidis, K. Moschopoulos, C. Papapavlou, et al., "A vision of 6th generation of fixed networks (F6G): challenges and proposed directions," [Telecom](https://doi.org/10.3390/telecom4040035) 4, 758 (2023).
# A Bidirectional WDM-PON Free Space Optical (FSO) System for Fronthaul 5 G C-RAN Networks

Fady El-Nahal , Tianhua Xu, Member, IEEE, Dokhyl AlQahtani, and Mark Leeson, Senior Member, IEEE

Abstract—High-speed cellular technologies require low-latency and high-capacity optical networks. The Centralized Radio Access Network (C-RAN) architecture offers a cost-effective solution for mobile network deployment. To maximize flexibility and minimize deployment costs of fronthaul networks, we propose a hybrid bidirectional fronthaul C-RAN topology based on Wavelength Division Multiplexing (WDM) passive optical networks (PONs) and free space optical communication (FSO). The wavelength reuse scheme utilized here relies on reflective semiconductor optical amplifiers (RSOAs) to reduce cost and increase capacity. The system was demonstrated for 20 Gbps 16-quadrature amplitude modulation (16-QAM) intensity-modulated orthogonal frequency-division multiplexing (OFDM) downstream signals and 5 Gbps On-off keying (OOK) upstream signals, respectively. A Gamma-Gamma channel model is used to demonstrate optical signal transmission over an FSO link. The bit error rate (BER) results indicate that the hybrid WDM-PON-FSO based fronthaul architecture could achieve 320 Gbps over 20 km of single-mode fiber (SMF) and 700 m free space transmission.

*Index Terms*—Free Space Optics (FSO), centralized radio access network (C-RAN), passive optical network (PON).

### I. INTRODUCTION

HE demand for high-speed data services is increasing dramatically as a result of the popularity of cloud computing, Big Data processing, and high-definition video broadcasting. Passive optical network (PON) and wireless access systems would be the most promising options for providing cost-effective last-mile access high-speed data to end users. WDM-PON is an excellent candidate for a future broadband access network since it can achieve greater capacity access and provide nearly infinite bandwidth to each end node. However, the PON system may not be the best option in areas where fiber installation is costly owing to geographical limitations. Hence, free-space

Manuscript received 14 November 2022; revised 12 December 2022; accepted 22 December 2022. Date of current version 4 January 2023. This work was supported by EU Horizon 2020 MSCA under Grant 101008280. (Corresponding author: Fady El-Nahal)

Fady El-Nahal is with the School of Engineering, University of Warwick, Coventry CV47AL, U.K., and also with the Department of Electrical Engineering, Islamic University of Gaza, Gaza 108, Palestine (e-mail: fady.el-nahal@warwick.ac.uk).

Tianhua Xu is with the School of Engineering, University of Warwick, Coventry CV47AL, U.K., and also with the Tianjin University, Tianjin 300072, China (e-mail: tianhua.xu@ieee.org).

Dokhyl AlQahtani is with the Electrical Engineering Department, College of Engineering, Prince Sattam Bin Abdulaziz University, Al-Kharj 11942, Saudi Arabia (e-mail: dm.alqahtani@psau.edu.sa).

Mark Leeson is with the School of Engineering, University of Warwick, CV4 7AL Coventry, U.K. (e-mail: mark.leeson@warwick.ac.uk).

Digital Object Identifier 10.1109/JPHOT.2022.3232081

optical communication (FSO) technology can be merged with it to overcome the problem [1], [2], [3].

FSO systems employ a laser signal that travels through the atmosphere to transmit data. Thus, FSO technology offers the following advantages, spectrum use without a license, high data rate and security, lower costs, full-duplex connection, protocol transparency, and infrastructure flexibility [4]. Moreover, Point-to-Point (PtP) or Point-to-Multi-Point (PtMP) connections are commonly used in FSO systems. High-capacity FSO connections can be achieved by employing wavelength division multiplexing (WDM) technology that provides a high fan-out (i.e., a significant number of channels per FSO connection) and elastic topologies [5]. Therefore, there is no capacity issue since each link requires a dedicated pair of telescopes. Additionally, FSO systems are utilized and implemented for last mile access in PtP and fiber backup connectivity to ensure network security and overcome geographical limitations [3].

The FSO signal is mainly impacted by atmospheric turbulence, known as intensity scintillation [6], which is random and unpredictable. Therefore, in the hybrid FSO-PON system, high-reliability transmission is also an essential factor [7]. The range of the FSO link relies on the acquired optical sensitivity, which decreases with increasing data rate, and the overall power budget of the FSO-PON network [8]. Therefore, to attain a longer FSO transmission length, the FSO signal data traffic should be carefully selected [3].

Mobile network operators are considering expanding network capacity by massively deploying extra small cells to meet the ever-increasing traffic demand. This small cell approach has become the most popular one for network expansion [9]. However, the deployment of more sites using conventional radio access methods will significantly raise costs. The proposed enhanced centralized radio access network architecture (C-RAN) enables the deployment of a vast number of cell sites cost-effectively [10]. C-RAN is a promising option since it simplifies site installation and enables radio access network (RAN) operations with low energy consumption [11]. The Base Band Unit (BBU) in C-RAN is relocated to a centralized location while the Radio Remote Head (RRH) is located at the cell site. Fronthaul connectivity between BBU and RRH is generally supported via wired options such as dedicated fiber or an optical fiber-based network, or wireless options such as FSO, microwave, or millimeter wavelengths [9], [12].

PONs meet the high-capacity demands of both wired and wireless end users with low deployment costs by sharing fiber resources. Additionally, WDM-PON enables a direct optical PtP

<span id="page-1-0"></span>![](_page_1_Figure_2.jpeg)

Fig. 1. The WDM FSO architecture.

connection between each optical network unit (ONU) near end users and the optical line terminal (OLT) at the central office (CO). This eliminates the need for sophisticated PON-over-Ethernet mapping and network administration. The simplicity, cost-effectiveness, and low latency of WDM-PON make it an excellent choice for 5 G Mobile Front Haul (MFH) applications. For 5 G deployment, a WDM-PON with a dedicated wavelength for each user and a speed of 25 Gbps or more has been suggested [\[13\].](#page-7-0) One of the major technologies for WDM-PON is colorless ONUs with tunable transceivers [\[14\].](#page-7-0) A 25 Gbps colorless ONU with a reflecting electro-absorption modulator and a semiconductor optical amplifier for 5 G fronthaul has been investigated in [\[15\].](#page-7-0)

The development and maintenance of a stand-alone PON system may not be practical for the deployment of fronthaul/backhaul networks, especially in dense metropolitan areas, because fiber deployment is not always practicable or expensive in every context. PON and FSO can be integrated to reduce the cost of the fronthaul network. FSO fronthaul links offer a cost-effective alternative to fiberbased fronthaul, allowing a significant decrease in deployment costs [\[9\].](#page-7-0)

## II. RELATED WORK

Various designs and technologies have been considered for fronthaul deployment. According to [\[16\],](#page-7-0) a moderate deployment of C-RAN, in which some BBU functions are relocated to the cell site to reduce the bandwidth requirements of the fronthaul segment, is preferred over a completely centralized model in which all BBU processing is performed at the central site. High-speed PON technologies, which support 5 G wireless with high capacity, low latency, low power per bit, and low cost, were explored in [\[17\].](#page-7-0) The authors in [\[18\]](#page-7-0) investigated the advantages of PON, which features superior bandwidth management and fiber sharing resources, over PtP fiber for fronthaul deployment. In [\[19\],](#page-7-0) a coherent WDM-PON system with a DP-16 quadrature amplitude modulation (DP-16QAM) transceiver was investigated to meet the aggregate capacity demands of 5G-and-beyond cellular networks. Fronthaul and backhaul network costs could be reduced considerably by employing PONs, according to [\[20\].](#page-7-0) A comparison of fiber-based backhaul systems with existing fiber-to-the-home solutions is presented in [\[21\].](#page-7-0) The economic effects of fiber and microwave backhaul systems for low and high wireless traffic requirements were investigated in [\[22\].](#page-7-0) In [\[23\],](#page-7-0) the optimal deployment costs associated with different deployment scenarios and different fronthaul technologies, including Analog and Digital Radio over Fiber were analyzed. A costefficient GPON backhaul deployment for small-cell networks compared to typical Ethernet-based PtP fiber backhauling was investigated in [\[24\].](#page-7-0)

There has been extensive research on FSO-based systems for deployment as access networks, both for fronthaul and backhaul in recent years [\[25\].](#page-7-0) FSO could minimize fronthaul network deployment costs, particularly in cases where fiber cannot be economically deployed [\[1\],](#page-7-0) [\[26\].](#page-7-0) An FSO link was deployed and evaluated in [\[27\]](#page-7-0) for fiber protection in PON distribution. In [\[9\],](#page-7-0) a low-cost hybrid PON-FSO-based fronthaul solution for 5 G C-RAN architecture was investigated for deployment in congested urban areas. In [\[28\],](#page-7-0) PON technology was utilized for a hybrid fiber/FSO fronthaul wireless scenario in order to increase flexibility and reduce deployment costs. A full-duplex

<span id="page-2-0"></span>![](_page_2_Figure_2.jpeg)

Fig. 2. BER versus OSNR plots for downlink.

![](_page_2_Figure_4.jpeg)

Fig. 3. BER versus OSNR plots for uplink.

| TABLE I               |  |  |
|-----------------------|--|--|
| SIMULATION PARAMETERS |  |  |

| Parameter                                   | Value                                  |
|---------------------------------------------|----------------------------------------|
| Laser power                                 | 10 dBm                                 |
| FSO attenuation                             | 3 dB km <sup>-1</sup>                  |
| Beam divergence                             | 2 mrad                                 |
| Transmitter aperture diameter               | 5 cm                                   |
| Receiver aperture diameter                  | 20 cm                                  |
| Index refraction structure $(C_n^2)$        | $5 \times 10^{-15} m^{\frac{-2}{3}}$   |
| Spacing between WDM channels                | 50 GHz                                 |
| Responsivity of PIN                         | $1 \; {\rm A} \; {\rm W}^{-1}$         |
| PIN thermal power density                   | $15 \times 10^{-24} \text{ W Hz}^{-1}$ |
| PIN dark current                            | 10 nA                                  |
| Gain of electrical amplifier                | 10 dB                                  |
| Electrical amplifier power spectral density | $-60 \text{ dBm Hz}^{-1}$              |

architecture for the transmission of ultrawideband (UWB) signals over the FSO network that offers the benefits of installation simplicity and mobility was presented in [\[29\].](#page-7-0) Dahrouj et al.[\[30\]](#page-7-0) have demonstrated that a radio frequency and FSO system can be combined to create a robust and cost-effective transport network infrastructure. All-optical generation and transmission of multiple UWB signals to radio access units over an FSO link was demonstrated in [\[6\]](#page-7-0) using a centralized frequency comb source.

A full C-RAN design will most likely use fiber for the fronthaul network, although PON, millimeter/microwave, and FSO-based technologies are potential options for a partial C-RAN network. Fronthaul deployment scenarios depend on several factors, including spectrum license fees, deployment time, equipment availability, and quality of service desired. As a result, PON and FSO technologies could be merged to enable fronthaul connection to diverse networks in crowded urban environments [\[3\],](#page-7-0) [\[9\].](#page-7-0)

WDM PON can be made more cost-effective by utilizing a wavelength reuse scheme, where no optical sources are required for upstream transmission. The upstream and downstream channels of these systems utilize the same wavelength to maximize wavelength utilization. A wavelength signal is remodulated with uplink data and then transmitted back as an uplink signal [\[31\].](#page-7-0) Reflective semiconductor optical amplifiers (RSOAs) are widely used in WDM-PONs utilizing wavelength reuse. Owing to its optical gain, integration capability, and wide optical bandwidth, the RSOA can be used as an uplink colorless transmitter and modulator [\[32\].](#page-7-0)

There is an ever-increasing demand for higher bandwidth in optical communication networks. Therefore, it is imperative that modulation speeds be improved. Traditionally, fiber optic networks have used dense wavelength division multiplexing (DWDM) to transmit separately modulated On-off keying (OOK) signals. As a result, the restricted total optical spectrum, coupled with the low bit rates achievable per optical signal, limits the bandwidth available overall. There has been a growing interest in wideband modulation schemes which utilize higher spectral efficiency modulation and multi-tone carriers, such as optical orthogonal frequency-division multiplexing (OFDM) [\[33\].](#page-7-0) This is a multicarrier, high-data-rate transmission method used primarily in wireless communications. The OFDM system utilizes several lower-rate orthogonal subcarriers in order to transmit the total high data rate. It is possible to modulate the orthogonal subcarriers of an OFDM signal in a variety of ways, such as QAM.

Here we have evaluated a novel hybrid bidirectional PON-FSO architecture based on wavelength reuse for 5 G C-RAN fronthaul, in which fiber would be laid as long as it is costeffective and practical. Then FSO links would be utilized to expand this access to several sites and eventually interconnect mobile users. The wavelength reuse scheme utilized here relies on RSOAs to reduce cost and increase capacity since no optical source is needed for upstream transmission. Here, 20 Gbps OFDM and 5 Gbps OOK WDM signals can be transmitted over a 20 km SMF and 700 m FSO link for downstream and upstream traffic, respectively. The proposed hybrid PON-FSO system provides low-cost transmission of high-data-rate signals, mobility, and shortened deployment times.

# III. WDM-FSO ARCHITECTURE

The proposed bidirectional WDM-PON FSO architecture is shown in Fig. [1,](#page-1-0) where the BBU is located at the CO, and the

<span id="page-3-0"></span>![](_page_3_Figure_2.jpeg)

Fig. 4. Constellation diagrams of different WDM channels obtained at different reaches of SMF (a) λ1*,* 10 km, (b) λ8*,* 10 km, (c) λ16*,* 10 km, (d) λ1*,* 20 km, (e) λ8*,* 20 km, (f) λ16*,* 20 km.

![](_page_3_Figure_4.jpeg)

Fig. 5. Eye diagrams of different WDM channels obtained at different reach of SMF (a) λ1*,* 10 km, (b) λ8*,* 10 km, (c) λ16*,* 10 km, (d) λ1*,* 20 km, (e) λ8*,* 20 km, (f) λ16*,* 20 km.

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

Fig. 6. BER versus FSO Link range plots for downlink and uplink.

RRHs are situated in the small cells (ONUs). The source used in this architecture consists of a multi-wavelength comb source, including a DeMux and Mux stage, as well as broadband modulators. The UWB signal is generated by integrating multiple optical wavelengths, each modulated by an RF OFDM input. The OFDM signals in this work utilized 16-QAM modulation, to provide better spectral efficiency and higher transmission rates than OOK. OFDM also provides FSO systems with a transmission method that offers resilience in the presence of multipath fading, frequency selective fading, and intersymbol interference (ISI), thus increasing their transmission range. Here, the input data are encoded into a serial stream of 16-QAM symbols using a QAM sequence encoder (4 bits per symbol). This input serial data stream is then converted into a parallel stream of OFDM symbols. Following the placement of data into several OFDM symbols, these are assigned to orthogonal subcarriers and this QAM-OFDM signal is used to modulate the optical WDM signal. The OFDM symbols must be converted from the frequency domain into the time domain to be transmitted along an optical carrier. This is achieved by applying an inverse fast fourier transform (IFFT) to each of them. In each WDM channel, a non-return to zero (NRZ)  $2^{23} - 1$  pseudorandom bit stream (PRBS) sequence has been generated with a data rate of 40 Gbps. Using an OFDM modulator with 512 subcarriers and 1024 FFT points, a data rate of  $(512/1024) \times 40 = 20$  Gbps was generated from this signal. After the IFFT, a cyclic prefix of 100 was added to each OFDM symbol to avoid ISI. The proposed architecture had N=16 wavelengths spanning from 1556.96 nm to 1550.92 nm (192.55 THz to 193.3 THz) with a transmission capacity of 320 Gbps. To minimize ISI, cosine roll-off filters were used to shape pulses before transmission. The OFDM modulated signal was up-converted from the electrical to the optical domain using a Mach-Zehnder modulator (MZM). The optical signal was combined with other WDM signals using a WDM MUX, amplified using an Erbium-doped fiber amplifier (EDFA), and transmitted over the single-mode fiber (SMF). The WDM signals were subsequently separated with a WDM DeMux, before being sent over FSO links to the ONUs. As each WDM signal was received at the ONU, it was split by 3 dB optical splitters and half of the OFDM modulated signal was then sent to an OFDM receiver. At the receiver, a PIN photodetector (PD) converted each WDM signal into an electrical signal, which was amplified by an electrical amplifier. A quadrature demodulator was then used to down-convert the amplified signal and recover it. An OFDM demodulator then retrieved the QAM symbols and a QAM sequence decoder converted the received symbols into bits based on the number of bits per symbol.

For the up-link, an RSOA remodulated the other half of the downstream OFDM-modulated signal to generate a 5 Gbps NRZ OOK PRBS  $2^{23}-1$  upstream signal. Since the seeding power of an RSOA significantly affects its modulation characteristics, a variable optical attenuator (VOA) was utilized to maintain the power at the input of the RSOA at a level where the RSOA operated in the gain saturation region. The OOK signals were transmitted as upstream data via FSO links and combined with a WDM Mux before being sent via SMF back to the CO. There, they were separated by a WDM DeMux and each OOK signal was detected directly by a PIN receiver.

FSO is mainly impacted by atmospheric attenuation and random variation of signal intensity and phase caused by atmospheric turbulence, referred to as intensity scintillation [6]. Various FSO statistical channel models are used to estimate the turbulence of an optical signal, for example the Log-normal model, K model, Negative exponential model, Gamma-Gamma model, and Log-normal Rician model [27]. The Gamma-Gamma FSO model is commonly used to simulate atmospheric turbulence and attenuation over a broad range of turbulence conditions [9].

In this case, the probability density function of the normalized light intensity I is given by [34]:

$$P(I) = \frac{2\left(\alpha\beta\right)^{\frac{\alpha+\beta}{2}}}{\Gamma(\alpha)\Gamma(\beta)} I^{\frac{\alpha+\beta}{2}-1} K_{\alpha-\beta} \left(2\sqrt{\alpha\beta I}\right) \tag{1}$$

$$\alpha = exp \left[ \frac{0.49\sigma_R^2}{\left(1 + 1.11\sigma_R^{\frac{12}{5}}\right)^{\frac{5}{6}}} \right] - 1 \tag{2}$$

$$\beta = exp \left[ \frac{0.51\sigma_R^2}{\left(1 + 0.69\sigma_R^{\frac{12}{5}}\right)^{\frac{5}{6}}} \right] - 1 \tag{3}$$

 $\alpha$  and  $\beta$  are the numbers of small and large turbulence cells,  $\Gamma(\cdot)$  is the Gamma function and  $K_{\alpha-\beta}(\cdot)$  is a modified Bessel function of the second kind.

The intensity variance  $\sigma_R^2$ , which directly depends on the magnitude of atmospheric turbulence, is given by:

$$\sigma_R^2 = 1.23C_n^2 k^{\frac{7}{6}} z^{\frac{11}{6}} \tag{4}$$

where  $C_n^2$  is the refractive index structure parameter with value ranges from  $10^{-13}$   $m^{\frac{-2}{3}}$  for strong turbulence to  $10^{-17}$   $m^{\frac{-2}{3}}$  for weak turbulence,  $k=\frac{2\pi}{\lambda}$  is the optical wavenumber and z is the range of the FSO link. The quasi-static model, also known as the frozen channel model, is used to calculate channel time fluctuations. According to this model, channel fading remains

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

Fig. 7. Constellation diagrams of different WDM channels obtained at different reach of FSO (a) λ1*,* 500 m, (b) λ8*,* 500 m, (c) λ16*,* 500 m, (d) λ1*,* 1000 m, (e) λ8*,* 1000 m, (f) λ16*,* 1000 m.

![](_page_5_Figure_4.jpeg)

Fig. 8. Eye diagrams of different WDM channels obtained at different reaches of FSO (a) λ1*,* 500 m, (b) λ8*,* 500 m, (c) λ16*,* 500 m, (d) λ1*,* 1000 m, (e) λ8*,* 1000 m, (f) λ16*,* 1000 m.

TABLE II MAIN RSOA PARAMETERS

| Parameter                  | Value                      |
|----------------------------|----------------------------|
| Input Facet Reflectivity   | $50 \times 10^{-6}$        |
| Output Facet Reflectivity  | $50 \times 10^{-6}$        |
| Active Length              | $0.0006 \ m$               |
| Taper Length               | $0.0001 \ m$               |
| Width                      | $0.4 \times 10^{-6}$       |
| Height                     | $0.4 \times 10^{-6}$       |
| Optical Confinement Factor | 0.45                       |
| Nonlinear gain parameter   | $112 \times 10^{-6} \ m^3$ |

the same over the course of a frame of symbols (coherence time), changing between frames to a new value.

#### IV. RESULTS AND DISCUSSION

The Optiwave simulation tool for optical system design was used to assemble and evaluate the WDM-PON FSO architecture [35]. Table I lists the parameters used in the simulation of the system. Bit error rate (BER) versus optical signal-to-noise ratio (OSNR) measurements were carried out to evaluate the performance of the bidirectional WDM-PON FSO architecture. Figs. 2 and 3 show the BER curves for the OFDM downstream and OOK upstream traffic, respectively, using three selected wavelength signals: 1556.96 nm ( $\lambda_1$ ), 1554.13 nm ( $\lambda_8$ ), and  $1550.92 \text{ nm} (\lambda_{16})$  over different lengths of SMF (10 and 20 km), while keeping the FSO range fixed at 500 m. It is evident from the downlink results in Fig. 2 that the BER improves as the OSNR increases, as is expected. In addition, it can be seen that increasing the SMF range generally has a minimal impact on the BER performance. This can be attributed to the fact that OFDM is resilient to fiber impairments, which increase with the expansion of PON's reach. Moreover, it is obvious that the BER performance degraded gradually as the WDM signal moved to a shorter wavelength position. For example, at OSNR = 32 dB, the BER increases from  $4.1 \times 10^{-5}$  for  $\lambda_1$  to  $2.5 \times 10^{-4}$  for  $\lambda_{16}$ after 10 km of SMF and from  $8.1\times 10^{-5}$  for  $\lambda_1$  to  $1.7\times 10^{-3}$ for  $\lambda_{16}$  after 20 km of SMF respectively.

For the uplink, however, it is evident from Fig. 3 that the BER varies slightly with increasing OSNR for each WDM signal, which can be predicted since the RSOA operates in the gain saturation region. Table II lists the parameters of the RSOA used here. The BER performance, however, has worsened with the increase in PON reach from 10 to 20 km, as expected. As PON reach increases, fiber impairments significantly impact data-modulated optical signals, especially OOK signals, compared with OFDM signals, resulting in poor BER performance.

The performance of various WDM signals has been further evaluated using constellation and eye diagrams obtained at various SMF ranges and a fixed FSO range of 500 m. Fig. 4 displays the constellation diagrams of various downstream WDM signals ( $\lambda_1$ ,  $\lambda_8$ , and  $\lambda_{16}$ ) obtained at 10 km and 20 km of SMF. There are slight variations in the constellations of  $\lambda_1$  and  $\lambda_8$  as the length of SMF is extended. However, the constellation for  $\lambda_{16}$  has been slightly distorted by increasing the length of SMF from 10 to 20 km. The results confirm that the BER performance degrades with the decreasing wavelength of the WDM signal.

Fig. 5 depicts the eye diagrams of different upstream WDM signals obtained at 10 km and 20 km of SMF lengths. It is shown in Fig 5 that as the length of the SMF increases, the opening of the eyes decreases, indicating that the BER performance is declining.

Fig. 6 shows the BER performance of the downstream and upstream FSO traffic over various FSO link ranges while keeping the SMF range fixed at 20 km. It is clear from Fig. 6 that as free space transmission distance increases, the BER performance of the system degrades. At the forward error correction (FEC) limit of  $\sim 3.8 \times 10^{-3}$  that defines the maximum BER level at which FEC can be used reduce BER to a tolerable level, for instance, the WDM signals 1556.96 nm ( $\lambda_1$ ), 1554.13 nm ( $\lambda_8$ ), and 1550.92 nm ( $\lambda_{16}$ ) could reach nearly 890 m, 880 m, and 700 m downstream, and 950 m, 960 m, and approximately 1000 m upstream, respectively. Accordingly, the FSO signal was capable of bidirectional transmission over 700 m depending on the wavelength. As downstream and upstream signals travel on different paths across the FSO link, no crosstalk is visible.

The performance of various WDM signals has been further evaluated by using constellation and eye diagrams derived at different FSO reach points. Figs. 7 and 8 show the constellation and eye diagrams of different downstream and upstream WDM signals ( $\lambda_1, \lambda_8$ , and  $\lambda_{16}$ ) at different FSO ranges, respectively. As can be seen from the results, the constellation and eye diagrams have been significantly distorted by increasing the range of the FSO link from 500 to 1000 m. For the downlink, it is evident that the effect of expanding the FSO range is more significant at shorter wavelengths ( $\lambda_{16}$ ) than at longer wavelengths ( $\lambda_1$ ). The results indicate that longer wavelength downstream traffic can achieve better BER performance and an extended range than shorter wavelengths. This can be explained by the fact that at shorter wavelengths, the attenuation resulting from atmospheric absorption increases slightly, degrading the performance of the system [36]. However, for upstream traffic, the BER performance of the different wavelengths is comparable even shorter wavelengths have a slightly better performance than longer ones. This is clear from the BER results in Figs. 3 and 7 and the eye diagram results in Figs. 5 and 8. This can be explained by the gain characteristics of the RSOA [37]. Moreover, the results demonstrate that the upstream signals are relatively unaffected by the Rayleigh backscattering noise caused by the downstream signals. This has been achieved by operating the RSOA in the gain saturation region to remove the downlink modulation on the seeding wavelength.

# V. CONCLUSION

We have evaluated a hybrid fronthaul C-RAN topology based on WDM-PONs and free space optics (FSOs) to accommodate the aggregate capacity demands of high-speed cellular networks. The PON-FSO system utilizes a centralized multi-wavelength comb source and direct detection, where a wavelength reuse scheme based on wavelength-seeded RSOAs is employed to reduce the cost of the architecture. On the downlink, an OFDM-modulated signal was transmitted, while on the uplink, an RSOA at the ONU re-modulated the downstream OFDM signal into an

<span id="page-7-0"></span>OOK signal. As shown by the BER measurements of WDM signals, the hybrid PON-FSO system may achieve 20 Gbps downstream and 5 Gbps upstream traffic for each wavelength over a 20 km SMF and 700 m free space transmission distance. The results demonstrate that the proposed PON-FSO topology offers a great alternative to fiber-based optical interconnect in PtP links in PONs, allowing high data rates in both directions.

#### REFERENCES

- [1] C.-H. Yeh, J.-R. Chen, W.-Y. You, W.-P. Lin, and C.-W. Chow, "Free space optical communication in long-reach unidirectional ringarchitecture fiber network," *IEEE Access*, vol. 8, pp. 159574–159580, 2020.
- [2] C.-Y. Li et al., "A flexible two-way PM-based fiber-FSO convergence system," *IEEE Photon. J.*, vol. 10, no. 2, pp. 1–9, Apr. 2018.
- [3] C.-H. Yeh, B.-S. Guo, Y.-J. Chang, C.-W. Chow, and C.-S. Gu, "Bidirectional free space optical communication (FSO) in WDM access network with 1000-m supportable free space link," *Opt. Commun.*, vol. 435, pp. 394–398, 2019.
- [4] K. Kazaura, K. Wakamori, M. Matsumoto, T. Higashino, K. Tsukamoto, and S. Komaki, "A proposal for a broadband wireless access technology based on radio-on-FSO links," in *Proc. IEEE Globecom Workshops*, 2008, pp. 1–6.
- [5] A. S. Hamza, J. S. Deogun, and D. R. Alexander, "Classification framework for free space optical communication links and systems," *IEEE Commun. Surveys Tuts.*, vol. 21, no. 2, pp. 1346–1382, Apr./Jun. 2019.
- [6] J. Mirza, S. Ghafoor, and A. Hussain, "All-optical generation and transmission of multiple ultrawideband signals over free space optical link," *Opt. Eng.*, vol. 58, no. 5, 2019, Art. no. 056103.
- [7] V. V. Mai and A. T. Pham, "Integrated FSO/PON for broadband access networks: A comprehensive protocol stack design and analysis," in *Proc. IEEE Glob. Commun. Conf.*, 2015, pp. 1–7.
- [8] H.-H. Lu et al., "Bidirectional fiber-wireless and fiber-IVLLC integrated system based on polarization-orthogonal modulation scheme," *Opt. Exp.*, vol. 24, no. 15, pp. 17250–17258, 2016.
- [9] S. S. Jaffer, A. Hussain, M. A. Qureshi, J. Mirza, and K. K. Qureshi, "A low cost PON-FSO based fronthaul solution for 5G CRAN architecture," *Opt. Fiber Technol.*, vol. 63, 2021, Art. no. 102500.
- [10] D. Jiang and G. Liu, "An overview of 5G requirements," *5G Mobile Commun.*, vol. 38, pp. 3–26, 2017.
- [11] J. Zhang, Y. Xiao, H. Li, and Y. Ji, "Performance analysis of optical mobile fronthaul for cloud radio access networks," in *Proc. J. Phys.: Conf. Ser.*, vol. 910, no. 1, 2017, Art. no. 012053.
- [12] M. Jaber, M. A. Imran, R. Tafazolli, and A. Tukmanov, "5G backhaul challenges and emerging research directions: A survey," *IEEE Access*, vol. 4, pp. 1743–1766, 2016.
- [13] W. W. Shbair and F. I. El-Nahal, "Coherent passive optical network for 5G and beyond transport," *Optoelectron. Lett.*, vol. 17, no. 9, pp. 546–551, 2021.
- [14] F. El-Nahal and N. Hanik, "Technologies for future wavelength division multiplexing passive optical networks," *IET Optoelectron.*, vol. 14, no. 2, pp. 53–57, 2020.
- [15] X. Zhou and N. Deng, "A 25-Gb/s 20-km wavelength reused WDM system for mobile fronthaul applications," in *Proc. Eur. Conf. Opt. Commun.*, 2015, pp. 1–3.
- [16] J. S. Wey and J. Zhang, "Passive optical networks for 5G transport: Technology and standards," *J. Lightw. Technol.*, vol. 37, no. 12, pp. 2830–2837, Jun. 2019.
- [17] X. Liu and F. Effenberger, "Emerging optical access network technologies for 5G wireless [invited]," *J. Opt. Commun. Netw.*, vol. 8, no. 12, pp. B70–B79, 2016.

- [18] C. J. Bernardos, A. De Domenico, J. Ortin, P. Rost, and D. Wübben, "Challenges of designing jointly the backhaul and radio access network in a cloud-based mobile network," in *Proc. Future Netw. Mobile Summit*, 2013, pp. 1–10.
- [19] A. Barzaq, I. Ashour, W. Shbair, and F. I. El-Nahal, "2 Tbit/s based coherent wavelength division multiplexing passive optical network for 5G transport," *Optoelectron. Lett.*, vol. 17, no. 5, pp. 308–312, 2021.
- [20] C. S. Ranaweera, P. P. Iannone, K. N. Oikonomou, K. C. Reichmann, and R. K. Sinha, "Design of cost-optimal passive optical networks for small cell backhaul using installed fibers [invited]," *J. Opt. Commun. Netw.*, vol. 5, no. 10, pp. A230–A239, 2013.
- [21] D. Breuer, S. Krauss, F. Geilhardt, E. Weis, and J. Belschner, "Cost evaluation of small cell backhaul architectures," in *Proc. Conf. Telecommun., Media Internet Techno-Econ.*, 2015, pp. 1–5.
- [22] A. A. W. Ahmed, J. Markendahl, C. Cavdar, and A. Ghanbari, "Study on the effects of backhaul solutions on indoor mobile deployment 'macrocell vs. femtocell,"' in *Proc. IEEE 24th Annu. Int. Symp. Pers., Indoor, Mobile Radio Commun.*, 2013, pp. 2444–2448.
- [23] C. Ranaweera, E. Wong, A. Nirmalathas, C. Jayasundara, and C. Lim, "5G C-RAN with optical fronthaul: An analysis from a deployment perspective," *J. Lightw. Technol.*, vol. 36, no. 11, pp. 2059–2068, Jun. 2018.
- [24] C. Ranaweera, P. Iannone, K. Oikonomou, K. Reichmann, and R. Sinha, "Cost optimization of fiber deployment for small cell backhaul," in *Proc. Opt. Fiber Commun. Conf. Expo. Nat. Fiber Optic Engineers Conf.*, 2013, pp. 1–3.
- [25] I. K. Son and S. Mao, "A survey of free space optical networks," *Digit. Commun. Netw.*, vol. 3, no. 2, pp. 67–77, 2017.
- [26] C.-H. Yeh, J.-R. Chen, W.-Y. You, and C.-W. Chow, "Hybrid WDM FSO fiber access network with Rayleigh backscattering noise mitigation," *IEEE Access*, vol. 8, pp. 96449–96454, 2020.
- [27] J. Mirza, W. A. Imtiaz, A. J. Aljohani, A. Atieh, and S. Ghafoor, "Design and analysis of a 32× 5 Gbps passive optical network employing FSO based protection at the distribution level," *Alexandria Eng. J.*, vol. 59, no. 6, pp. 4621–4631, 2020.
- [28] F. Tonini, C. Raffaelli, L. Wosinska, and P. Monti, "Cost-optimal deployment of a C-RAN with hybrid fiber/FSO fronthaul," *J. Opt. Commun. Netw.*, vol. 11, no. 7, pp. 397–408, 2019.
- [29] J. Mirza, S. Ghafoor, and A. Hussain, "A full duplex ultrawideband over free-space optics architecture based on polarization multiplexing and wavelength reuse," *Microw. Opt. Technol. Lett.*, vol. 62, no. 12, pp. 3999–4006, 2020.
- [30] H. Dahrouj, A. Douik, F. Rayal, T. Y. Al-Naffouri, and M.-S. Alouini, "Cost-effective hybrid RF/FSO backhaul solution for next generation wireless systems," *IEEE Wireless Commun.*, vol. 22, no. 5, pp. 98–104, Oct. 2015.
- [31] C. Yeh, C.-W. Chow, H. Chen, J. Sung, and Y. Liu, "Demonstration of using injection-locked Fabry-Perot laser diode for 10 Gbit/s 16-QAM OFDM WDM-PON," *Electron. Lett.*, vol. 48, no. 15, pp. 940–942, 2012.
- [32] F. I. El-Nahal, "A WDM-PON with DPSK modulated downstream and OOK modulated upstream signals based on symmetric 10 Gbit/s wavelength reused bidirectional reflective SOA," *Optoelectron. Lett.*, vol. 13, no. 1, pp. 67–69, 2017.
- [33] J. Armstrong, "OFDM for optical communications," *J. Lightw. Technol.*, vol. 27, no. 3, pp. 189–204, Feb. 2009.
- [34] Z. Wang, W.-D. Zhong, S. Fu, and C. Lin, "Performance comparison of different modulation formats over free-space optical (FSO) turbulence links with space diversity reception technique," *IEEE Photon. J.*, vol. 1, no. 6, pp. 277–285, Dec. 2009.
- [35] "Optisystem package from optiwave," Accessed: Jun. 6, 2022. [Online]. Available:<https://optiwave.com/>
- [36] Y. Yang, J. Gao, and Y. Zhang, "Effects of fog-haze random media on the short-range optical wireless communications link," *Optik*, vol. 138, pp. 8–14, 2017.
- [37] Y. Chien-Hung and C. Chi-Wai, "Utilization of reflective semiconductor optical amplifier (RSOA) for multiwavelength and wavelengthtunable fiber lasers," in *Fiber Laser*. London, U.K.: IntechOpen, 2016, pp. 151–164.
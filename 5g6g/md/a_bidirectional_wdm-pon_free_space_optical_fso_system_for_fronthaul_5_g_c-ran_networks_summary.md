---
index_terms:
  - WDM-PON
  - Free Space Optics (FSO)
  - C-RAN fronthaul
  - Reflective Semiconductor Optical Amplifier (RSOA)
  - 16-QAM OFDM
  - wavelength reuse
  - atmospheric turbulence
---

# A Bidirectional WDM-PON Free Space Optical (FSO) System for Fronthaul 5 G C-RAN Networks

## I. Introduction
To support the high capacity and low latency required by 5G cellular networks, the authors propose a hybrid fronthaul architecture for Centralized Radio Access Networks (C-RAN). This topology combines Wavelength Division Multiplexing Passive Optical Networks (WDM-PON) with Free Space Optical (FSO) communication to overcome the cost and geographical barriers associated with installing fiber in every urban location. While WDM-PON provides high-capacity point-to-point connections between the Central Office (CO) and Radio Remote Heads (RRHs), FSO serves as a flexible, license-free alternative for the "last mile" or where fiber is impractical. The primary challenge identified is atmospheric turbulence (intensity scintillation), which impacts signal reliability.

## II. Related Work
The paper reviews existing fronthaul strategies, noting that while fully centralized C-RANs are ideal, partial deployments are often more practical to reduce bandwidth requirements. Previous research highlights the advantages of PON over point-to-point fiber regarding resource sharing and cost. The authors specifically highlight two key technological improvements:
1.  **Wavelength Reuse:** Utilizing Reflective Semiconductor Optical Amplifiers (RSOAs) allows upstream signals to use the same wavelength as downstream signals, eliminating the need for expensive optical sources at each Optical Network Unit (ONU).
2.  **Advanced Modulation:** Transitioning from On-off keying (OOK) to Optical Orthogonal Frequency-Division Multiplexing (OFDM) increases spectral efficiency and resilience against fiber impairments and atmospheric fading.

## III. WDM-FSO Architecture
The proposed system places the Base Band Unit (BBU) at the CO and RRHs at the ONUs, utilizing a hybrid SMF-FSO link.

### Downlink Signal Path
The downstream path employs 16-QAM intensity-modulated OFDM to maximize spectral efficiency and mitigate multipath fading and intersymbol interference (ISI). The system uses a multi-wavelength comb source producing 16 channels spanning $1550.92$ nm to $1556.96$ nm, providing a total capacity of 320 Gbps. Each channel transmits at 20 Gbps (derived from a 40 Gbps PRBS signal using 512 subcarriers and 1024 FFT points). The signals are modulated via Mach-Zehnder modulators (MZM), amplified by Erbium-doped fiber amplifiers (EDFA), transmitted over SMF, and finally delivered through FSO links to the ONU. At the receiver, a PIN photodetector and quadrature demodulator recover the data.

### Uplink Signal Path
The upstream path uses a wavelength reuse scheme via RSOAs at the ONU. The RSOA remodulates the downstream signal to generate a 5 Gbps NRZ OOK signal. A variable optical attenuator (VOA) is used to ensure the RSOA operates in the gain saturation region, which helps eliminate downlink modulation from the returning seed wavelength and minimizes Rayleigh backscattering noise. These signals return through the FSO link and SMF to be detected by PIN receivers at the CO.

### FSO Channel Modeling
To simulate atmospheric effects, the authors employ the Gamma-Gamma model, which accounts for small- and large-scale turbulence cells ($\alpha$ and $\beta$). The model incorporates the refractive index structure parameter ($C_n^2$) to represent different levels of turbulence (from weak to strong) and utilizes a "frozen channel" quasi-static model to account for time fluctuations across symbol frames.

## IV. Results and Discussion
The system was evaluated using Optiwave simulation software, focusing on Bit Error Rate (BER) relative to Optical Signal-to-Noise Ratio (OSNR) over 10–20 km of SMF and various FSO distances.

### Downlink Performance
Downlink BER improves as OSNR increases. The researchers found that OFDM's resilience makes the system relatively insensitive to changes in SMF length. However, performance degrades at shorter wavelengths ($\lambda_{16}$) compared to longer ones ($\lambda_1$), likely due to higher atmospheric absorption at those wavelengths.

### Uplink Performance
Uplink BER is less sensitive to OSNR variations because the RSOA operates in gain saturation. Unlike the downlink, the uplink (using OOK) is significantly more affected by SMF length increases, as OOK is more susceptible to fiber impairments than OFDM.

### FSO Link Impact and Reach
As the FSO transmission distance increases, BER degrades for both paths. At the Forward Error Correction (FEC) limit ($\sim 3.8 \times 10^{-3}$), the maximum supportable distances are:
*   **Downlink:** Approximately 700 m to 890 m depending on the wavelength.
*   **Uplink:** Approximately 950 m to 1000 m.

Upstream signals generally exhibit better or comparable performance in the FSO link due to the gain characteristics of the RSOA. No significant crosstalk was observed between bidirectional traffic since they utilize different modulation formats and operating regimes.

## V. Conclusion
The authors successfully demonstrated a hybrid WDM-PON-FSO architecture for 5G C-RAN fronthaul. By integrating wavelength reuse via RSOAs and combining OFDM (downlink) with OOK (uplink), the system achieves a total aggregate capacity of 320 Gbps. The results confirm that the system can reliably support 20 Gbps downstream and 5 Gbps upstream per channel over a combined reach of 20 km SMF and 700 m free space, providing a cost-effective alternative to full fiber deployments.
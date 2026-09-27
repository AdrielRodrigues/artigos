---
index_terms:
  - hollow-core fiber
  - optical transport networks
  - generalized signal-to-noise ratio
  - multiband transmission
  - inter-modal interference
  - stimulated Raman scattering
---

# Hollow-Core Fiber Properties and System-Level Specifications for Next-Generation Optical Transport Networks

## 1. Introduction
Hollow-core fibers (HCFs) are proposed as alternatives to traditional silica-based fibers, such as standard single-mode fiber (SSMF) and pure-silica-core fiber (PSCF). HCFs offer several fundamental physical advantages: attenuation potentials below 0.11 dB/km, a wider spectral low-loss region facilitating ultra-wide band (UWB) transmission, negligible nonlinearity and stimulated Raman scattering (SRS), and approximately 33% lower latency due to the near-vacuum propagation medium.

Despite these benefits, several deployment challenges exist: the need for optical amplifiers with high maximum total output power, penalties from inter-modal interference (IMI)—which becomes significant if it exceeds -60 dB/km—and higher connection/splice losses when interfacing HCF with traditional components like ROADMs and EDFAs. This paper aims to model these uncertainties to determine the specific combinations of fiber properties and amplifier specifications that make HCF competitive against SSMF and PSCF.

## 2. Line System Characterization

### 2.1. Fiber Characterization
The study evaluates HCF across a range of attenuation values (0.11 to 0.31 dB/km) and splice losses (0.05 to 0.5 dB per 2 km). IMI power is modeled between -45.0 and -60.0 dB/km. A critical distinction is that HCF's SRS effect is set to zero, whereas SSMF and PSCF exhibit peak Raman gain coefficients of 0.38 and 0.22 1/(W·km), respectively. HCF also features a significantly larger effective area (417 $\mu\text{m}^2$) and a much lower nonlinear coefficient compared to silica fibers.

### 2.2. Optical Amplifier Characterization
While SSMF and PSCF can utilize both Erbium-Doped Fiber Amplifiers (EDFAs) and Hybrid EDFA/Raman Amplification (HFA), HCF is limited to EDFAs because the absence of SRS makes Raman amplification non-viable. To leverage HCF's low nonlinearity, high-power EDFAs are required. The authors define four potential HCF amplifier configurations with increasing maximum total output power (ranging from 27 to 36 dBm for SuperC) and corresponding increases in Noise Figure (NF), reflecting the cost/complexity trade-off of high-power devices.

## 3. Performance Modeling and Optimization

### 3.1. Optical Performance Model
The Quality of Transmission (QoT) is measured using the generalized signal-to-noise ratio (GSNR). Unlike traditional fibers, the GSNR for HCF includes a third noise term: IMI power ($P_{IMI,f}$), in addition to ASE and NLI powers. The total lightpath QoT accounts for incoherent accumulation of NLI across spans and OSNR contributions from transmitters and ROADMs (including specific insertion losses for add, drop, and intermediate nodes). The study focuses on "SuperC" (6.1 THz) and "SuperL" (5.5 THz) spectral bands using 120 Gbaud signals in a 150 GHz grid.

### 3.2. Launch Power Optimization
For silica fibers, launch power is optimized using a pre-tilted profile to counteract SRS. HCF launch power is primarily constrained by the maximum output power of the amplifier rather than nonlinearities. Preliminary results indicate that while HCF's performance is comparable to SSMF with HFA in the SuperC band, it shows a distinct advantage in the combined SuperC+L scenario because the strong SRS effects that degrade wideband silica systems are absent in HCF.

### 3.3. Network Assessment Framework
The authors use the Telecom Italia (TIM) network topology (44 nodes, 400 spans of 80 km) to evaluate system-level impact. The framework employs a $k$-shortest routing algorithm ($k=3$) and first-fit spectrum allocation for random traffic demands (100/400 G). Transceiver modes are based on OpenROADM MSA specifications (800, 600, and 400 Gbps), with ROSNR requirements adjusted for polarization-dependent loss (PDL) and a 1.0 dB system margin.

## 4. Results and Discussion

### 4.1. Transmission Performance Comparison
Using $\Delta GSNR$ heatmaps for a single 80 km span, the authors find:
* **Against SSMF:** HCF outperforms SSMF in 59% of cases for SuperC (EDFA), but this advantage increases significantly in SuperC+L scenarios because wideband SRS severely penalizes SSMF.
* **Against PSCF:** HCF is less competitive; it never outperforms PSCF using hybrid amplification in the SuperC band due to PSCF's lower attenuation and Raman gain properties.
* **Impact of IMI:** Parity curves reveal that for SuperC, HCF generally requires IMI $\le -50$ dB/km to beat SSMF. However, in SuperC+L, HCF remains competitive even with higher IMI (-45 dB/km) because the lack of SRS outweighs the IMI penalty.

### 4.2. Network Capacity Comparison
The network is tested using "Worst" (0.21 dB/km loss, lowest-power amp) and "Best" (0.11 dB/km loss, highest-power amp) HCF configurations:
* **SuperC Scenario:** PSCF with hybrid amplification provides the highest number of 800 Gbps channels. HCF Best is slightly better than SSMF Hybrid but lower than PSCF Hybrid.
* **SuperC+L Scenario:** HCF Best becomes the superior configuration, enabling the most 800 Gbps channels (up to 326) and the highest overall carried traffic (191.1 Tbps vs 171.7 Tbps for SSMF EDFA at 220 Tbps offered load).
* **Key Insight:** The advantage of HCF is most pronounced when expanding spectral bandwidth, as it avoids the capacity-limiting effects of SRS present in silica fibers.

## 5. Conclusions
The study concludes that HCF's primary value proposition lies in wideband (SuperC+L) transmission where its immunity to SRS provides a significant performance edge over SSMF and PSCF. While current technological bottlenecks—such as high splice losses and the trade-off between amplifier power and noise figure—limit its potential, HCF is already competitive against standard SSMF/EDFA setups. To outperform high-end PSCF/HFA solutions, future developments must focus on reducing attenuation through scalable manufacturing and developing low-noise, high-power amplifiers.
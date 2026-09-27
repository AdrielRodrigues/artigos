---
index_terms:
  - coherent passive optical networks
  - 100G fiber access
  - burst-mode coherent detection
  - digital signal processing
  - rate-adaptive access
  - time-frequency division multiplexing
---

# Coherent Passive Optical Networks for 100G/-and-Beyond Fiber Access: Recent Progress and Outlook

## Abstract
Coherent optics is proposed as the primary solution for achieving single-wavelength passive optical networks (PONs) at speeds of 100 Gb/s and higher. By utilizing a local oscillator (LO), coherent systems offer superior receiver sensitivity, extending power budgets to support high-capacity, long-reach access with large split ratios. This review examines the use cases and challenges of coherent PONs, technical innovations for reducing complexity and cost, and methods for upstream burst-mode detection. It further proposes rate-flexible architectures using digital subcarrier multiplexing (DSCM) for time-and-frequency-division multiplexing (TFDM) and adaptive modulation schemes.

## Introduction
PON technology has evolved from broadband PON (B-PON) to current 25G/50G standards, driven by the need for low-cost "last mile" connectivity. However, emerging demands from 5G, cloud networking, and high-definition streaming are pushing requirements toward 100 Gb/s per wavelength. While Intensity Modulation/Direct Detection (IM/DD) has been the standard due to simplicity, it faces severe sensitivity limits and dispersion penalties at speeds above 50 Gb/s. Although multi-wavelength IM/DD solutions exist, single-wavelength systems are preferred for reducing component counts and simplifying resource management. Coherent optics is presented as a viable alternative to overcome these physical layer limitations in the post-50G PON era.

## Motivations

### Application Scenarios
The demand for 100G-and-beyond access is driven by three primary scenarios:
*   **Residential Broadband Access:** The rise of 8K/16K video and VR/AR services is expected to require downlink bandwidths of 3–4 Gb/s per user. With a 1:64 split ratio, total bandwidth could exceed 84 Gb/s by 2030.
*   **Mobile X-haul:** The transition toward B5G and 6G requires high-capacity links between distributed units (DU) and radio units (RU). Depending on function splits, peak downlink requirements range from ~3 Gb/s to over 86 Gb/s.
*   **Business Services:** Following Nielsen's Law of Internet Bandwidth (predicting a 50% CAGR for high-end users), 100G capacity will be necessary by approximately 2030 to support enterprise and cloud service providers.

### Advantages of Coherent PONs
Coherent detection provides four critical advantages over IM/DD systems:
1.  **Superior Receiver Sensitivity:** Coherent beating with an LO significantly improves sensitivity (e.g., >14 dB improvement for 100 Gb/s PDM-QPSK vs. NRZ). This allows for longer transmission distances and higher split ratios, meeting the PR-30 power budget (>31 dB) where IM/DD fails.
2.  **Advanced Modulation Formats:** Coherent systems can detect amplitude, phase, and polarization. This enables high spectral efficiency through multidimensional modulation (e.g., PDM-QPSK for 100G or PDM-16-QAM for 200G) using relatively low-bandwidth (25 GHz) optoelectronic devices.
3.  **Digital Dispersion Compensation:** Linear conversion of the optical field allows digital signal processing (DSP) to completely eliminate chromatic dispersion. This enables high-speed operation in the C-band, expanding available spectral windows beyond the O-band.
4.  **Filter-less Channel Selection:** The inherent frequency selectivity of the LO allows for channel or subchannel selection without physical optical filters, facilitating future WDM and FDM extensions.

## Challenges

### Cost, Complexity, and Power Consumption
Implementing coherent optics in access networks is hindered by the high cost of components traditionally used in long-haul systems. Coherent PONs require additional hardware—including LO lasers, complex modulators, multiple photodetectors, ADCs/DACs, and DSP ASICs—which increase overall transceiver cost and energy consumption compared to IM/DD configurations.

### Upstream Burst-Mode Detection
Unlike the continuous broadcast of downstream signals, upstream traffic arrives in bursts from different users with varying power levels, clocks, frequencies, phases, and states of polarization (SOP). This necessitates:
*   **Burst-Mode Linear Amplification:** The need for multiple linear, identical TIAs to handle diversity paths.
*   **Rapid Burst-Mode DSP:** Standard point-to-point DSP is too slow; burst-mode systems require extremely fast acquisition times and a wide frequency-offset compensation range to accommodate wavelength drift.

## Enabling Technologies

### Simplification and Optimization of Coherent Optics
To make coherent PONs economically viable, several optimizations are proposed:
*   **Laser Source Reduction:** Using remote laser sources from the OLT or replacing expensive external cavity lasers (ECL) with lower-cost distributed feedback (DFB) lasers.
*   **Receiver Simplification:** Replacing full-field receivers with heterodyne detection to halve the number of PDs and ADCs, or using polarization scrambling/coding to remove polarization-diversity hardware.
*   **DSP Optimization:** Reducing computational complexity by eliminating fixed chromatic dispersion and PMD compensation (unnecessary over 20 km links) and sharing phase estimation between polarizations.

### Coherent Burst-Mode Detection
Recent progress in upstream detection includes:
*   **Amplification:** Using automatic gain control SOAs (AGC-SOA) or SiGe:C linear burst-mode receivers to level signal power before the coherent receiver.
*   **Preamble and DSP Design:** Implementing a structured preamble with specific synchronization patterns (SP-1 for settling, SP-2 for clock recovery, SP-3 for frame/frequency synchronization, and SP-4 for adaptive channel equalization). Using conjugate symmetric symbols and Jones matrix inversion further reduces convergence time.

## Future Research Directions

### Flexible Multiplexing Beyond TDM
Coherent detection enables a transition from simple Time-Division Multiplexing (TDM) to more flexible schemes:
*   **TFDM:** A rate-flexible architecture using digital subcarrier multiplexing (DSCM) allows for simultaneous resource sharing in both time and frequency domains using a single wavelength and transceiver.
*   **Multidimensional Access:** Integration of TDM, FDM, WDM, and PDM, alongside potential exploration of CDMA and NOMA.

### Rate-Adaptive Access
To avoid the "worst-case" performance bottleneck where all ONUs are limited by the lowest-performing link, rate-adaptive access is proposed:
*   **Mechanisms:** Using adaptive LDPC-FEC or Probabilistic Shaping (PS).
*   **Probabilistic Shaping (PS):** PS allows for fine-grained adjustment of the information rate based on the effective SNR. Simulations show net data rates can vary continuously from 255 Gb/s (64-QAM) down to 85 Gb/s (QPSK) as received optical power decreases, maximizing channel capacity.

## Conclusions
Coherent optics is a promising candidate for $\ge$100G fiber access due to its sensitivity and modulation flexibility. While cost, power consumption, and upstream burst-mode detection remain significant hurdles, innovations in simplified hardware and rapid DSP are making these systems more feasible. Beyond speed, the potential for TFDM and rate-adaptive networking indicates a shift toward highly flexible, high-capacity access networks.
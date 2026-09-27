---
index_terms:
  - Coherent Passive Optical Networks
  - TDM-PON
  - Receiver Sensitivity
  - Burst-Mode Detection
  - Frequency Comb Local Oscillator
  - Digital Signal Processing
---

# Coherent Passive Optical Networks: Why, When, and How

## Abstract
The authors argue that for next-generation access networks reaching 100 Gb/s and beyond, coherent optics is the necessary physical layer choice because current intensity-modulation/direct-detection (IM/DD) technology cannot satisfy the required power budgets at such high line rates. The paper examines the necessity, expected timeframe, and technological hurdles associated with implementing coherent Passive Optical Networks (Coh-PON).

## Introduction
Bandwidth demands are surging due to 5G/6G, cloud computing, and high-resolution video streaming. While IEEE and ITU-T have standardized 25 Gb/s and 50 Gb/s PONs respectively, the authors suggest a target of 200 Gb/s for future generations to ensure long-term viability for network operators. Conventional IM/DD systems are unsuitable for rates exceeding 100 Gb/s because limited receiver sensitivity prevents them from meeting the loss budgets of deployed optical distribution networks (ODNs). Coherent technology, which detects amplitude, phase, and polarization, is proposed as the alternative. Additionally, coherent optics enables flexible line-rates to optimize throughput based on specific user needs.

## Why Coherent Optics for PON?
Direct-detection (DD) receivers only detect signal intensity; as line rates increase, sensitivity drops due to increased noise bandwidth and chromatic dispersion penalties. Because DD is a square-law process, linear impairments become nonlinear and difficult to compensate via Digital Signal Processing (DSP). In contrast, coherent detection offers:
*   **Enhanced Sensitivity:** Local oscillator (LO) power provides signal amplification, improving the power budget, extending reach, and allowing more connected users or better support for 5G xHaul.
*   **Linearity and DSP Efficiency:** Coherent systems exploit four degrees of freedom (two polarizations, in-phase and quadrature modes), enabling higher-order modulation formats with lower-bandwidth components. DSP can fully compensate for chromatic dispersion, allowing operation in the low-attenuation 1550 nm band and coexistence with legacy TDM-PONs via wavelength overlay.
*   **Frequency Selectivity:** The choice of LO wavelength allows for inherent filtering, which is highly beneficial for WDM-PON architectures to avoid separate optical filters.

## Timeline for Coherent PON
Based on historical patterns where five to ten years pass between standards and eight years between deployments, the authors propose an optimistic timeline:
*   **2026:** Standardization of coherent TDM-PON.
*   **2028:** Initial operational deployment.
*   **Adoption Path:** Transitioning from low-volume business services to 6G xHaul (approx. 2029) and finally residential FTTH (approx. 2030).

## Reference Architecture of Coherent PON
The proposed architecture focuses on single-wavelength per direction TDM-PON, utilizing Time Division Multiplexing (TDM) for downstream and Time Division Multiple Access (TDMA) for upstream. To balance performance and cost:
*   **OLT (Central Office):** Uses a conventional dual-polarization (DP) coherent transceiver.
*   **ONU (Subscriber):** Employs a simplified coherent receiver and basic amplitude-modulated transmitters (e.g., electro-absorption modulated lasers) to minimize cost.

To reuse existing ODNs, the system must maintain legacy loss budgets and use distinct wavelengths for coexistence. Suggested wavelength windows are in the S, C, and L bands, with a specific plan proposing downstream at 1510 $\pm$ 2 nm and upstream at 1560 $\pm$ 2 nm.

### Low-Complexity Receiver for Downstream
Standard DP-intradyne receivers are too complex and power-hungry for ONUs. The authors propose several simplification levels:
*   **Heterodyne Detection:** Replacing the 90° optical hybrid with a 3 dB coupler and using baseband downconversion in the DSP reduces optoelectronic components by half, though it doubles the required receiver bandwidth.
*   **Single-Polarization (SP) Heterodyne:** Further reducing components to one balanced photodiode and one ADC. To mitigate polarization fluctuations without adding ONU complexity, "Alamouti coding" (orthogonal symbol pairs) is implemented at the OLT transmitter.
*   **Performance:** Simulations for 200 Gb/s using 16-QAM over 40 km show that a simplified heterodyne receiver can achieve a power budget of 38.05 dB, exceeding the ITU-T E2 class loss budget (35 dB).

To reduce DSP power consumption at the ONU, the authors suggest sub-Nyquist sampling and frequency-domain equalization. Additionally, since polarization mode dispersion is low in PON reaches, phase noise can be estimated in one polarization and applied to the other.

### Challenges for Coherent Upstream
Using high-end DP-IQ transmitters at the ONU is cost-prohibitive due to complex bias control and insertion loss. Instead, the authors propose using simple EML or DML lasers to generate intensity-modulated signals (NRZ/PAM), while maintaining a coherent receiver at the OLT for sensitivity. This introduces three primary challenges:
1.  **Dynamic Range:** The OLT must handle burst signals with up to 20 dB variance, which typically causes TIA saturation or ADC quantization noise. Solution: Use burst-mode amplifiers (BM-EDFA or BM-SOA) with dual-stage automatic gain control (AGC).
2.  **Rapid Adaptation:** DSP must converge quickly during the short preamble of each burst to account for different ONU signal powers and polarization states. Solutions include predefined tap weights or variable step-size adaptation algorithms.
3.  **Frequency Locking:** Low-cost ONU lasers drift in wavelength. The authors propose using a **wavelength comb source as the LO** at the OLT, allowing the signal to beat with one of the comb lines and eliminating the need for fast LO tuning.

## Concluding Remarks
Coherent technology has already migrated from core networks to data center interconnects (e.g., 400G ZR). While cost, power, and footprint remain hurdles for access networks, the authors conclude that advancements in photonic integration and the co-packaging of optics, RF, and DSP ASICs will make coherent optics the natural choice for PON systems operating at 100 Gb/s per wavelength and beyond.
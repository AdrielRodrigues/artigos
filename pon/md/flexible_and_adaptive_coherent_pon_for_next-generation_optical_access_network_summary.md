---
index_terms:
  - Coherent PON
  - rate-adaptive access
  - probabilistic shaping
  - time-frequency division multiplexing
  - optical power budget
  - digital signal processing
---

# Flexible and Adaptive Coherent PON for Next-Generation Optical Access Network

## 1. Introduction
The demand for high-bandwidth optical access is surging due to 8K/16K video, VR/AR, edge computing, and 5G/6G mobile X-haul, with expected requirements of 100G to 200G per wavelength by 2030. Traditional Intensity Modulation/Direct Detection (IM/DD) PONs are reaching their physical limits at 50G because maintaining a high power budget (e.g., PR-30) becomes extremely difficult due to sensitivity constraints and fiber dispersion in the O-band.

Coherent Passive Optical Networks (C-PON) are proposed as a superior alternative. C-PON leverages multi-access coherent optics and Digital Signal Processing (DSP) to provide:
- **Enhanced Sensitivity:** Beating gain from the local oscillator allows for significantly higher power budgets, enabling long-reach and high split-ratio access.
- **Higher Speeds:** Advanced modulation formats and linear conversion of optical fields to digital domains facilitate higher data rates and digital dispersion compensation.
- **Spectrum Flexibility:** The use of C-band wavelengths avoids O-band congestion and allows coexistence with legacy systems.
- **Frequency Selectivity:** Inherent ability to perform frequency-division multiplexing without optical filters.

The authors argue that "flexibility"—specifically in access data rates, multiplexing architectures, and deployment scenarios—is critical for supporting diverse use cases ranging from residential (FTTH) to mobile cell sites (FTTC).

## 2. Rate-Adaptive Access for Flexible C-PON

### 2.1 Motivations and Realization
Standard PONs often limit overall throughput by assigning a fixed data rate based on the worst-performing Optical Network Unit (ONU). A rate-adaptive approach optimizes capacity by assigning higher data rates to users with better channel conditions (lower optical path loss, OPL).

While IM/DD systems use multi-rate NRZ or adaptive coding, C-PON offers more degrees of freedom. The paper identifies several rate-adaptive schemes:
- **Adaptive Baud Rate:** Adjusts clock and sampling rates (large granularity).
- **Adaptive Modulation Orders:** Switches between formats like BPSK to 16QAM based on link budget (large granularity).
- **Multidimensional Modulation:** Utilizes I/Q-imbalanced modulation.
- **Adaptive Modulation and Coding (MCS):** Combines various FEC code rates with different modulation formats to reduce the gap between discrete modulation levels (medium granularity).
- **Adaptive Probabilistic Shaping (PS):** Adjusts source entropy to approach optimal channel capacity, providing fine-grained rate adjustment.

### 2.2 Demonstration of 300G Flexible C-PON based on PS-QAM
The authors describe a 300G peak-rate TDM C-PON using Probabilistic Shaping QAM (PS-QAM). To achieve a dynamic range exceeding 35 dB, they employ local-oscillator power adjustment.

**Methodology:**
- **Tx Side:** Raw data is split; one branch undergoes distribution matching to create a Maxwell-Boltzmann distribution for amplitude shaping. This is followed by FEC encoding and QAM mapping.
- **Optimization:** Channel estimation informs the source entropy of the PS-QAM signals, and look-up-table (LUT) technology is used for pre-equalizing distortion.
- **Rx Side:** Uses burst-mode DSP to synchronize and demodulate incoming signals from different ONUs.

**Findings:** The system demonstrated net data rates ranging from 255 Gbps down to 85 Gbps as the OPL increased from 3 dB to 38 dB over a 20 km fiber link.

## 3. Flexible Multiple-Access Beyond TDM

### 3.1 Motivations and Realization
While Time Division Multiplexing (TDM) is efficient for bandwidth sharing, it suffers from scheduling latency. Coherent detection enables several alternative or hybrid multiple-access schemes:
- **WDMA/UDWDM:** Assigns specific wavelengths to high-end users for low-latency, secure P2P services.
- **FDMA:** Uses digital subcarrier multiplexing to allocate bandwidth sub-bands on a single wavelength.
- **NOMA:** Operates in the power domain via constellation multiplexing to enhance network capacity.
- **CDMA:** Multiplexes users using unique spreading sequences, allowing simultaneous transmission in the same time/frequency slot.

The authors highlight that combining these (e.g., WDM-FDM or TFDM) creates a multidimensional access system with extreme flexibility.

### 3.2 Example of the Flexible TFDM C-PON
The paper details a 100G single-wavelength Time-Frequency Division Multiplexing (TFDM) C-PON using digital subcarrier multiplexing. In this setup, four 25-Gbps PDM-QPSK subcarriers are used.

**Key Features:**
- **Architecture:** The OLT uses an I/Q modulator to send four subcarriers downstream; the ONU detects them separately. Upstream, the OLT uses a single broadband coherent receiver to aggregate subcarriers from multiple ONUs.
- **Flexibility:** Bandwidth is allocated in two dimensions. Low-latency services can be granted dedicated P2P frequency channels, while other users share bandwidth via TDM.
- **Trade-off:** To prevent signal overlap caused by laser wavelength drift, guard bands must be implemented, which slightly reduces total spectral efficiency.

## 4. Flexible Deployment Scenarios for C-PON

### 4.1 Motivations and Realization
The high sensitivity of coherent detection (providing >10 dB gain over IM/DD) allows operators to redefine the trade-off between split ratio and fiber distance, governed by the equation: $Power Budget = Loss_{Transmission} + Loss_{Split}$.

**Deployment Capabilities:**
With a power budget increase of 10 dB, C-PON can support:
- High-density scenarios: Up to 256 ONUs at a 20 km reach.
- Long-reach scenarios: up to 70 km for small groups (e.g., 8 ONUs).
- Hybrid scenarios: Simultaneously supporting users at different distances (e.g., 32 ONUs at 30 km and 16 ONUs at 50 km).

This flexibility allows C-PON to efficiently cover diverse geographic areas—Urban (short reach, high density), Suburban (mixed), and Rural (long reach, low density)—by adapting modulation formats or coding rates to the specific OPL of each node.

## 5. Discussion and Summary
The authors conclude that while C-PON offers significant flexibility in speed, architecture, and deployment, several barriers to adoption remain:
- **Cost and Complexity:** Full-field coherent transceivers are expensive. They suggest using low-cost DFB lasers (instead of ECLs) or remote laser sources to reduce costs.
- **DSP Overhead:** While C-PON requires DSP, the authors argue that for 100G and beyond, the complexity of IM/DD's required electronic dispersion compensation eventually exceeds that of coherent DSP, making C-PON the more attractive choice at this threshold.
- **Integration:** Photonic Integrated Circuit (PIC) technology is identified as essential for reducing size, power consumption, and cost.

The proposed strategy for adoption is a "use scenario-driven" approach: starting with high-bandwidth users (business campuses, mobile X-haul) before progressing to broader residential deployment as the technology matures.
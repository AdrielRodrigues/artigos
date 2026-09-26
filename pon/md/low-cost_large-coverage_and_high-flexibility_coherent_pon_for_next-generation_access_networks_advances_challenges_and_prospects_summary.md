---
index_terms:
  - Coherent PON
  - Low-cost coherent optics
  - Burst-mode reception
  - Probabilistic Shaping
  - TFDM architecture
  - Local Oscillator adjustment
  - Wide dynamic range
  - Next-generation access networks
---

# Low-cost, large-coverage, and high-flexibility coherent PON for next-generation access networks: advances, challenges, and prospects

## 1. Introduction
As fixed network requirements transition toward the F5G era to support high-bandwidth applications (e.g., 8K streaming and IoT), traditional intensity modulation/direct detection (IM/DD) passive optical networks (PONs) struggle with power budgets at speeds of 100G and beyond. Coherent PON (CPON) is presented as a viable alternative due to its superior sensitivity, high-speed performance, and ability to handle large dynamic ranges. While CPON offers significant technical advantages, its adoption depends on reducing equipment costs, specifically at the optical network unit (ONU). This paper explores strategies for simplifying transceivers and digital signal processing (DSP), enhancing system coverage through local oscillator (LO) power adjustment, and implementing flexible rate capabilities via probabilistic shaping and time-frequency division multiplexing (TFDM).

## 2. Low-Cost Optimization of Coherent Optics for PON
The primary barrier to CPON commercialization is the cost and complexity of components and DSP at the ONU. The authors argue that reductions in modulation dimensions or receiver sensitivity are acceptable trade-offs for significantly lower costs.

### 2.1. Upstream
To replace expensive IQ modulators, Mach–Zehnder modulators (MZMs) are used to implement simplified transmitter schemes:
*   **Intensity Modulation (IM):** Uses coherent detection but produces an intensity signal requiring squaring at the receiver. It offers the simplest DSP and high frequency-offset tolerance but precludes complex domain processing.
*   **Amplitude Modulation:** Two variants exist—one that ignores phase information and one using only 0° and 180° phases (PAM-4 ASK). The latter enables sophisticated DSP in the complex domain but requires carrier recovery.

### 2.2. Downstream
Simplification of the coherent receiver reduces component counts for those receiving OLT signals:
*   **Heterodyne Architectures:** Options include DP-heterodyne receivers using $2\times2$ couplers and balanced photodiodes (BPDs), or even simpler versions using single-ended photodiodes (SPDs) which, while incurring a 3 dB power loss, reduce hardware costs.
*   **Specialized Couplers:** A $3\times3$ coupler approach allows for polarization-independent intensity detection with only three SPDs.
*   **Alamouti Coding:** To avoid dual-polarization receivers at the ONU, Alamouti coding transforms single-polarization signals into a space-time block code, allowing a simplified receiver ($2\times2$ coupler and one BPD) to recover the data.

### 2.3. DSP Complexity Reduction
DSP power consumption is reduced by optimizing adaptive equalization (AEQ). Specifically:
*   **Filter Optimization:** Splitting conventional AEQ into butterfly and non-butterfly FIR filters can halve the number of taps and reduce multiplications by 41%.
*   **Frequency Domain (FD) Equalization:** FD training-aided equalization provides robustness against optical propagation effects independent of filter length. While nonlinear equalization exists, it is currently deemed impractical for PON due to the cost-benefit ratio.

## 3. Coherent Detection Enabled Wide Coverage
CPON overcomes the limitations of IM/DD in high or low optical path loss (OPL) scenarios through advanced DSP and LO power gain.

### 3.1. Downstream and Upstream Processing
*   **Downstream (Continuous Mode):** DSP compensates for chromatic dispersion, clock synchronization, and state of polarization (SOP), enabling dynamic ranges as high as 39 dB at 200G.
*   **Upstream (Burst Mode):** The OLT must handle rapid transitions between users with different clocks, SOPs, and frequency offsets. This is managed via specific frame structures with synchronization patterns (SPs) for fast convergence and pilot structures for rapid channel estimation. Neural networks are also noted as a method to enhance sensitivity.

### 3.2. Local Oscillator (LO) Power Adjustment
To prevent ADC saturation from high-power signals while maintaining sensitivity for low-power signals, the LO power can be dynamically adjusted:
*   **Implementation:** This is achieved using a variable optical attenuator (VOA). Adjustment can be based on monitoring the electrical signal at the ADC input or by referencing the optical input signal power.
*   **Impact:** Experimental data shows that without adjustment, dynamic ranges for high-order modulations (e.g., 64QAM) are very narrow (5 dB). LO adjustment significantly expands this range by decreasing LO power as received optical power increases, keeping the bit error rate (BER) below the threshold.

## 4. Rate-Adaptive Accesses for Flexible CPON
Flexible PON (FLCS-PON) addresses the inefficiency of providing a uniform data rate to all users regardless of their channel conditions.

### 4.1. Probabilistic Shaping (PS) based FLCS-CPON
PS adjusts the probability distribution of constellation symbols to approximate a Maxwell-Boltzmann distribution, optimizing the net data rate (NDR) against peak-power constraints:
*   **Hybrid PS (HPS):** Combines Classical PS (CPS), which handles clipping nonlinearity in burst mode, and Reversed PS (RPS), which is more efficient under peak-power constraints. 
*   **Entropy Control:** By adjusting the shaping factor $\nu$, the system can finely tune constellation entropy $H$ to match user channel conditions, thereby maximizing overall throughput.

### 4.2. TFDM-based FLCS-CPON
The TFDM architecture provides higher flexibility by allocating resources in both time and frequency:
*   **Architecture:** Uses multiple digital subcarriers (e.g., five carriers where one is blank for heterodyne detection). 
*   **Resource Allocation:** Rates are adjusted by varying the QAM order per subcarrier (frequency dimension) or utilizing PS and different QAM orders at different time slots (time dimension). This approach is often paired with Alamouti-coded receivers to maintain low ONU costs.

## 5. Conclusion and Prospects
The paper concludes that CPON is a strong candidate for 100G+ access networks if complexity is reduced through the discussed transmitter/receiver simplifications and DSP optimizations. By combining LO power adjustment for wide coverage and PS or TFDM for flexibility, CPON can meet commercial requirements. The authors foresee these technologies as foundational for the sixth-generation fixed network (F6G) and the widespread realization of Fiber to the X (FTTX).
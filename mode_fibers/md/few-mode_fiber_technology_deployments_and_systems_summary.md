---
index_terms:
  - mode-division multiplexing
  - few-mode fibers
  - space-division multiplexing
  - MIMO digital signal processing
  - differential mode group delay
  - multiplane light conversion
---

# Few-Mode Fiber Technology, Deployments, and Systems

## I. Introduction
Optical fiber capacity is approaching the nonlinear limit of single-mode fibers (SMFs), necessitating space-division multiplexing (SDM). SDM can be achieved via multicore fibers (MCF) or few-mode fibers (FMF). FMFs are particularly advantageous because they support a high number of independent data channels (modes) while maintaining a standard 125 $\mu$m cladding diameter. This compatibility ensures mechanical reliability and allows the use of existing connectivity and cabling infrastructure, unlike MCFs which often require larger diameters and non-standard manufacturing.

The primary challenge in FMFs is modal crosstalk. The paper identifies two strategies to address this:
1. **Weakly Coupled Approach:** Minimizing crosstalk across components so that modes or mode groups can be detected separately without complex multiple-input–multiple-output (MIMO) processing.
2. **Full-MIMO Approach:** Minimizing differential mode group delays (DMGD) and using MIMO digital signal processing (DSP) to compensate for crosstalk at the receiver.

## II. Weak Coupling

### A. Fiber Design and Manufacturing
Step-index-core profiles are preferred for weakly coupled FMFs due to low-cost, large-scale manufacturability. However, crosstalk increases as more spatial modes are added; values range from $<40$ dB/km (two LP mode groups) to $\sim 25$ dB/km (seven LP mode groups). To mitigate this, designers attempt to increase the minimum effective index difference ($\text{Min}|\Delta n_{\rm eff}|$). While introducing a depressed-index zone in the core center increases $\text{Min}|\Delta n_{\rm eff}|$ without significantly harming attenuation or effective area, crosstalk reduction is limited by high mode overlapping between groups. Consequently, weakly coupled FMFs are currently most suitable for short-reach applications using mode group-division multiplexing (MGDM) and direct detection (DD).

### B. Transmission Demonstrations

#### 1) MGDM and DD
MGDM increases throughput in intensity-modulation direct detection (IM-DD) systems by multiplexing groups of modes with the same propagation velocity, avoiding the need for full MIMO. Multiplane light conversion (MPLC) is used to achieve this. 
* **Performance:** Records include 14.5 Tb/s over 2 km of standard multimode fiber (MMF). In a specific demonstration using weakly coupled step-index FMF, 200 Gb/s bidirectional transmission was achieved over 20 km using four LP mode groups. 
* **Findings:** Discrete Fourier Transform (DMT) modulation is found to be more resilient to crosstalk fluctuations than PAM4 for IM-DD MGDM transmissions.

#### 2) High-Capacity MDM With $2 \times 2$ and $4 \times 4$ MIMOs
To reduce DSP complexity, low-order MIMO can be used. The authors demonstrate a ten-spatial-mode multiplexed transmission over a 48 km weakly coupled fiber using rate-adaptive probabilistically shaped (PS) dual-polarization 16QAM in the C- and L-bands. By utilizing only $2 \times 2$ and $4 \times 4$ MIMO equalizers, they achieved a total fiber capacity of 402.7 Tb/s.

### C. Deployments

#### 1) MGDM to Increase Local Area Networks' Capacity
MGDM using MPLC technology is applied to upgrade legacy LAN infrastructures without replacing existing standard MMFs. 
* **Implementation:** The system converts single-mode inputs into mode groups, allowing a total of four mode groups to be used for transmission.
* **Field Results:** Field trials in hospitals and universities showed $4 \times 10$ Gb/s transmissions over distances up to 3300 m (e.g., in French ski resorts), providing a 400-fold increase over standard 100 Mb/s LAN rates.

#### 2) Real-Time MDM With $2 \times 2$ and $4 \times 4$ MIMOs
Real-time deployment requires ASIC or FPGA implementation. MIMO complexity scales quadratically with the number of modes ($N^2$), making full MIMO computationally expensive. The weakly coupled approach (partial MIMO) drastically reduces this resource requirement.

**a) Resource requirement for real-time MIMO DSP**
Using CMOS roadmaps, the authors note that while $2 \times 2$ MIMO is standard for DP-SMF, a full-MIMO system with many modes would require transistor densities only possible with next-generation (3nm) technology. Partial MIMO is far more feasible with current hardware.

**b) Real-time implementation of adaptive MIMO equalization**
The paper argues that blind algorithms (like CMA) are unsuitable for large-scale MDM due to the "singularity problem," where the probability of failure increases with the number of modes. Instead, training algorithms (LMS) are preferred. To handle calculation delays in FPGA parallelization (pipelined delay), the authors employ the Mori algorithm, which improves phase tracking speed by five times compared to conventional LMS.

**Real-time ten-mode transmission experiments**
A prototype receiver using FPGAs and MPLC multiplexers demonstrated real-time ten-spatial-mode transmission over 48 km of weakly coupled FMF. Using DP-QPSK with 18 subcarriers, the system maintained BER below the $2.7 \times 10^{-2}$ threshold for 20% overhead FEC.

## III. Full MIMO

### A. Fiber Design and Manufacturing
Trench-assisted graded-index cores are used to minimize DMGD, which is the primary bottleneck for full-MIMO systems. While standard processes lead to a steep increase in DMGD as mode count increases (e.g., $\sim 410$ ps/km for 28 modes), using rescaled multimode (MM) preforms with tighter tolerances can keep DMGD below 80 ps/km for 15-mode fibers. Additionally, concatenating fibers with opposite-sign DMGDs can reduce total link delay spread by factors of 2–4.

### B. Transmission Demonstrations and Deployments

#### 1) High Spectral Efficiency MDM Over 45-Spatial-Mode Graded-Index-Core FMF
To test the scaling limits, an experiment was conducted over a 26.5 km FMF with a total accumulated DMGD of 2.4 ns using MPLC multiplexers and a $90 \times 90$ MIMO equalizer. The system achieved a spectral efficiency of 202 b/s/Hz, with Q-factors for QPSK exceeding 9.8 dB across all modes.

#### 2) High-Capacity MDM
Using a wideband approach (C+L bands), the authors demonstrated a transmission using a 15-mode fiber and an optical comb source. By multiplexing 382 WDM channels, they achieved a total data rate of 1.01 Pb/s over 23 km. Results showed that impulse response duration increases at longer wavelengths due to spectral variations in DMGD, and total capacity is limited by mode-dependent loss (MDL).

#### 3) Ultralong-Haul MDM
Long-haul transmission is limited by the accumulation of DMGD (increasing MIMO complexity) and MDL (destroying channel orthogonality). Mitigation strategies include:
* **Optical methods:** Zero-DMGD slope fibers, ring-core amplifiers, and Cyclic Mode Permutation (CMP)—the latter converts weak coupling to "quasi-strong" coupling.
* **Digital methods:** Frequency-domain MIMO equalization and digital interference cancelers for MDL. 
Using CMP, a record transoceanic-class transmission of 6300 km was achieved.

#### 4) FMF Cable Deployment in L'Aquila
A 26 km dielectric cable containing eight 15-spatial-mode fibers has been deployed in the city center of L'Aquila (INCIPCT project). This provides a real-world field testbed for the research community to gather data on MDM transmissions in an actual urban environment.

## IV. Conclusion
The authors conclude that FMFs with standard 125 $\mu$m cladding are viable for sustaining future traffic growth. Weakly coupled systems are ideal for short-reach and LAN applications (achieving up to 402.7 Tb/s), while full-MIMO systems are suited for long-haul transport, having already demonstrated records in spectral efficiency (202 b/s/Hz) and total capacity (1.01 Pb/s).
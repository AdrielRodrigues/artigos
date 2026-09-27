---
index_terms:
  - mid-infrared communication
  - free-space optical communications
  - wavelength-division multiplexing
  - mode-division multiplexing
  - orbital angular momentum
  - difference frequency generation
---

# High-capacity free-space optical communications using wavelength- and mode-division-multiplexing in the mid-infrared region

## Results

### Concept of mid-IR FSO communication system using both WDM and MDM
The system employs a hybrid multiplexing approach to increase data capacity in the mid-infrared (mid-IR) spectrum (~3.4 $\mu$m). To leverage high-performance C-band transceivers, the authors use nonlinear periodically-poled lithium niobate (PPLN) waveguides to perform wavelength conversion via difference frequency generation (DFG). At the transmitter, a C-band signal mixed with a 1064 nm pump generates a mid-IR idler. To incorporate mode-division multiplexing (MDM), Gaussian beams are passed through spiral phase plates (SPPs) to create orbital angular momentum (OAM) beams. The receiver reverses this process: inverse SPPs convert OAM beams back to Gaussian beams, and a second PPLN waveguide converts the mid-IR signal back to the C-band for coherent detection. The authors note that using independent pump lasers at each end would introduce phase noise and frequency shifts, though these can be mitigated via digital signal processing (DSP).

### Wavelength conversions between the C-band and mid-IR wavelengths
The study experimentally validates the conversion of three WDM channels (3.396, 3.397, and 3.398 $\mu$m) with a channel spacing of 27.5 GHz. Mid-IR power generation is influenced by pump power, signal power (which saturates above 1W due to potential pump depletion), and PPLN temperature, which must be optimized for quasi-phase-matching. Conversion efficiency was measured at approximately -26.5 dB. The system's phase-matching bandwidth allows multiple C-band WDM channels to be converted simultaneously within a single PPLN waveguide.

### Mid-IR FSO communication system using WDM only
A 150 Gbit/s system (three 50 Gbit/s QPSK channels) was demonstrated using Gaussian beams. The measured crosstalk between adjacent wavelengths is lower than -13 dB, though this depends on the optical filter's sharpness. In terms of performance, mid-IR transmission incurs an optical signal-to-noise ratio (OSNR) penalty of ~2 dB compared to direct C-band transmission due to wavelength conversion (caused by in-band crosstalk and pump laser noise). Multiplexing three wavelengths adds an additional ~1 dB OSNR penalty.

### Mid-IR FSO communication system using MDM and a combination of WDM and MDM
The authors demonstrated OAM beams with orders +1 and +3, verified by ring-shaped intensity profiles and twisted-arm interferograms. An inverse SPP successfully separates desired modes from other OAM channels via spatial filtering. The total capacity was increased to 300 Gbit/s by combining WDM and MDM (three wavelengths $\times$ two OAM modes), with each of the six channels carrying a 50 Gbit/s QPSK signal. All channels achieved a bit error rate (BER) below the 7% forward error correction (FEC) threshold. The OSNR penalty for OAM multiplexing was found to be less than 1 dB, primarily due to modal crosstalk arising from misalignment between the beam axis and the SPP center.

### Discussion
The authors highlight several key considerations for scaling and implementing this system:
*   **Hardware:** While C-band components were used for convenience, native mid-IR modulators could be integrated as they become available. Scaling WDM would require PPLN waveguides with wider phase-matching bandwidths (e.g., thin-film lithium niobate).
*   **Efficiency & Safety:** Current conversion efficiency is low (-26.5 dB), requiring high pump power; more efficient PPLN designs could reduce this. For eye safety, transmitted power should remain below 10 mW for wavelengths >1.4 $\mu$m.
*   **Atmospheric Impact:** Mid-IR offers lower atmospheric attenuation in clear weather compared to the C-band. It is also less susceptible to turbulence-induced phase distortion. However, mid-IR's larger beam divergence requires larger receiver apertures to prevent power loss and modal coupling (crosstalk) in OAM systems.
*   **Pointing Errors:** Lateral displacement and angular tip/tilt can cause signal power loss in Gaussian beams and inter-channel crosstalk in OAM-based MDM systems.

## Methods

### Experimental setup of the WDM MDM mid-IR FSO communication link
The transmitter uses two IQ modulators to impose 25 Gbaud QPSK signals on three C-band laser sources (linewidth ~100 kHz). These are amplified by an EDFA and coupled into PPLN1 with a YDFA-amplified 1064 nm pump. Mid-IR band-pass filters (Germanium windows) remove the pump and signal remnants. The mid-IR beam is split and passed through SPPs (+1, +3) before propagating 0.5 m in free space. At the receiver, inverse SPPs (-1, -3) revert OAM beams to Gaussian beams; these are then converted back to C-band via PPLN2 and a second pump laser, followed by amplification (EDFA) and coherent detection using an oscilloscope (80 GSa/s).

### Digital signal processing for coherent detection
To manage signal integrity:
*   **Transmitter:** Nyquist pulse shaping uses a raised cosine filter with a low roll-off factor (0.05) to minimize spectral bandwidth and guard bands.
*   **Receiver:** Offline DSP includes band-pass filtering to suppress adjacent wavelength crosstalk, coarse and fine carrier phase recovery (CPR) using fourth power-based and Kalman filtering methods, and a 48-tap FIR feed-forward equalizer to compensate for linear distortions from the hardware chain.

### OAM beam generation with SPPs
OAM beams are created using Zinc Selenide SPPs with a helical surface. The height gradient of the surface is specifically calculated based on the mid-IR wavelength (~3.4 $\mu$m), OAM order, and the refractive index of the material ($\approx 2.4$). These SPPs demonstrated high transmission efficiency with an insertion loss of approximately 0.45 dB.
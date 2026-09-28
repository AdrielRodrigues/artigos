---
index_terms:
  - forward Brillouin scattering
  - few-mode fibers
  - torsional-radial acoustic modes
  - inter-modal coupling
  - photoelastic effect
  - orbital angular momentum
---

# Forward Brillouin scattering in few-mode fibers

## Abstract
The paper investigates forward Brillouin scattering (FBS) in few-mode optical fibers, extending previous research that focused on single-mode fibers (SMF). In SMFs, FBS is restricted to radial and two-fold azimuthal symmetric acoustic modes with frequencies typically below 600 MHz. By utilizing a commercial step-index few-mode fiber, the authors demonstrate the stimulation of acoustic modes with first-order and fourth-order azimuthal symmetries and observe frequencies up to 1.8 GHz. They find that acoustic modes can be stimulated above their cut-off frequencies and that angular momentum is transferred between optical and acoustic orbital degrees of freedom.

## Introduction
Brillouin scattering involves opto-mechanical coupling between traveling optical and acoustic waves. While backward scattering stimulates longitudinal acoustic modes in the core, forward scattering couples co-propagating optical fields with predominantly transverse acoustic modes guided by the fiber cladding. In SMFs, FBS is limited to specific acoustic mode classes due to spatial overlap constraints. 

The authors propose that few-mode fibers provide additional degrees of freedom because optical fields can propagate in various spatial modes, allowing for a broader range of acoustic mode stimulation. The objective is to analyze and experimentally demonstrate FBS in step-index few-mode fibers, focusing on the simulation of higher-order azimuthal symmetries and increased frequency ranges.

## Analysis of forward Brillouin scattering in standard fewmode fibers

### Optical Modes
The authors describe optical modes using linearly polarized (LP) mode groups ($LP_{ln}$), where $l$ is the azimuthal symmetry order and $n$ is the radial order. The radial profile $G_{ln}(r)$ is defined by Bessel functions, while the transverse electric field vectors are split into $HE_{ln}$ and $EH_{ln}$ components.

### Electro-strictive Force
Two co-propagating optical fields create an electro-strictive stress tensor $\sigma$, which generates a driving force per unit volume $\vec{F}$. This force propagates with frequency $\Omega$ (the difference between the two optical frequencies) and axial wavenumber $K = \beta_1 - \beta_2$. The azimuthal orders of the resulting force are limited to $l_1 \pm l_2$. 
- **Intra-modal processes:** When both fields are in the same mode, $K$ is very small ($1\text{--}10 \text{ rad}\cdot\text{m}^{-1}$).
- **Inter-modal processes:** When fields occupy different modes, $K$ can be significantly larger ($\sim 10^4 \text{ rad}\cdot\text{m}^{-1}$), comparable to bulk acoustic waves in silica.

### Torsional-Radial (TR) Acoustic Modes
The fiber cladding acts as an acoustic waveguide supporting torsional-radial ($TR_{pm}$) modes, defined by azimuthal order $p$ and radial order $m$. 
- **Cut-off Frequency ($\Omega_{pm}$):** Below this frequency, the mode cannot propagate axially; at cut-off, the axial wavenumber vanishes.
- **Classification:** Modes are categorized as predominantly dilatational (longitudinal wave motion) or shear-like (transverse wave motion).
- **Dispersion:** Near cut-off, the relationship between frequency and axial wavenumber is $\Omega - \Omega_{pm} \approx \frac{\nu_{L,S}^2}{2\Omega_{nm}} K^2$.

### Acoustic Stimulation and Overlap
The stimulation of an acoustic wave depends on the spatial overlap integral $Q_{1,2,pm}^{(ES)}$ between the electro-strictive force $\vec{f}_{1,2}$ and the acoustic mode displacement $\vec{u}_{pm}$. A key selection rule is established: an acoustic mode can only be stimulated if its azimuthal order $p$ equals $l_1 \pm l_2$. In SMFs ($l=1$), this limits stimulation to $p=0, 2$; in few-mode fibers, higher values of $l$ allow for various other symmetries.

### Photoelastic Coupling and Wavenumber Matching
Acoustic strain induces perturbations in the dielectric tensor ($\Delta\varepsilon_{pm}$), which couples light between optical modes 3 and 4 via a photoelastic overlap integral $Q_{3,4,pm}^{(PE)}$.
- **Wavenumber Matching:** For intra-modal processes, frequency matching automatically ensures wavenumber matching. For inter-modal processes, matching requires specific differences in the effective indices of the involved optical modes: $(n_{\text{eff},3} - n_{\text{eff},4})\omega_s/c = \pm K$.

### Gain Coefficient and Resonance
The forward Brillouin gain coefficient $\gamma_{1,2,pm}(\Omega)$ reaches a maximum at the resonance frequency $\Omega_{pm}^{(R)}$. For intra-modal scattering, $\Omega_{pm}^{(R)}$ is approximately the cut-off frequency $\Omega_{pm}$. For inter-modal scattering, there is a shift: $\Omega_{pm}^{(R)} \approx \Omega_{pm} + \frac{k_0^2 v_{L,S}^2}{2\Omega_{pm}}(n_{\text{eff},1} - n_{\text{eff},2})^2$.

## Numerical calculations of forward Brillouin scattering spectra in a few-mode fiber
Calculations were performed for a fiber with a $4.8 \mu\text{m}$ core and $62.8 \mu\text{m}$ cladding, supporting $LP_{01}$, $LP_{02}$, and the $LP_{11}$ group.

- **Intra-modal $LP_{01}$:** Results mirror SMF behavior; radial modes ($R_{0m}$) are stronger than two-fold symmetric modes ($TR_{2m}$), with efficiency dropping significantly above 500 MHz.
- **Intra-modal $LP_{02}$:** Supports higher acoustic frequencies (up to 1.8 GHz) because the higher-order optical mode profile better matches high-frequency acoustic displacement profiles. Shear modes dominate between 500–900 MHz, while dilatational modes dominate above 1 GHz.
- **Inter-modal $LP_{01}$ and $LP_{02}$:** Spectra for radial and two-fold symmetric modes differ from intra-modal cases due to the wavenumber shift.
- **$LP_{11}$ group:** Stimulates $R_{0m}$, $TR_{2m}$, and—crucially—four-fold symmetric $TR_{4m}$ and purely torsional $T_{0m}$ modes. The $TR_{4m}$ modes are driven by the $HE_{21}$ component.
- **Inter-modal $LP_{01}$ and $LP_{11}$:** This combination stimulates first-order ($TR_{1m}$) and third-order ($TR_{3m}$) azimuthal symmetry modes.

## Experimental results

### Intra-modal scattering in $LP_{01}$ and $LP_{02}$
Measurements of the $LP_{01}$ mode matched calculations, showing radial and two-fold symmetric modes. Linewidths scaled linearly with frequency, attributed to cladding diameter nonuniformity. In the $LP_{02}$ mode, acoustic modes were observed up to 1.8 GHz, confirming that higher-order optical modes enable high-frequency SBS stimulation.

### Scattering in the $LP_{11}$ group
The authors successfully observed the first-ever instance of four-fold symmetric $TR_{4m}$ modes in fibers. These were identified by their frequency offset (1–2 MHz lower) from the adjacent $TR_{2m}$ peaks. Purely torsional $T_{0m}$ modes were not resolved, likely due to weak signal-to-noise ratios or insufficient power in specific mode components ($TE_{01}, TM_{01}$).

### Inter-modal scattering
- **$LP_{01}$ and $LP_{11}$:** The researchers demonstrated the stimulation of first-order symmetric $TR_{1m}$ modes, which are inaccessible in SMFs.
- **$LP_{01}$ and $LP_{02}$:** Resonance frequencies were consistently higher than those in intra-modal scattering. This shift $\Delta\Omega$ was found to be inversely proportional to frequency $\Omega$, validating the theoretical prediction for inter-modal wavenumber matching.

## Discussion
The research demonstrates that few-mode fibers expand the scope of FBS by allowing arbitrary azimuthal symmetry stimulation and increasing accessible acoustic frequencies (up to 1.8 GHz). The ability to excite modes above their cut-off frequencies with large axial wavenumbers suggests potential for creating non-reciprocal optical coupling or narrowband isolation.

Further applications include:
- **Sensing:** Using different mode groups to characterize the elastic properties of surrounding media across a broader frequency range.
- **Lasers:** Creating extremely coherent forward Brillouin lasers with greater design flexibility than polarization-maintaining fibers.
- **Quantum Technology:** Manipulating quantum states via the exchange of orbital angular momentum between optical and mechanical waves.

The authors acknowledge that some predicted modes (e.g., $TR_{3m}$ and $T_{0m}$) were not observed due to limited signal-to-noise ratios or spectral overlap with stronger peaks.

## Materials and methods

### Intra-modal setup
A 1550 nm laser was modulated by an EOM at frequency $\Omega$ and launched into the fiber via a mode division multiplexer (MDM). A separate 1532 nm signal wave monitored the induced acoustic waves. Detection used two channels:
1. **Sagnac interferometer:** To detect radial modes $R_{0m}$ through photoelastic phase modulation (pump polarization was scrambled to isolate these).
2. **Polarizer:** To detect torsional-radial modes via polarization rotation. 
The Kerr effect was removed by performing an offline inverse-Fourier transform and time-gating the impulse response.

### Inter-modal setup
Two pump branches were used: one offset in frequency by $\Omega$ (via SSB modulator) and another at a different frequency. Both were intensity-modulated at distinct frequencies ($f_1, f_2$) using lock-in amplifiers. Coupling between these modes manifested as intensity modulation at $f_1 \pm f_2$, which was monitored via a 20 GHz photoreceiver.

## Appendix A: Spatial overlap integrals
The appendix provides a mathematical proof in Cartesian coordinates showing that the spatial overlap integral for electro-strictive stimulation ($Q^{(ES)}$) is identical to the overlap integral for photoelastic scattering ($Q^{(PE)}$), provided the fields vanish at the cladding boundary.
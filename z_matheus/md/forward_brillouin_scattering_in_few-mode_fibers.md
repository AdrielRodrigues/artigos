ARTICLE Open Access

# Forward Brillouin scattering in few-mode fibers

Elad Layosh<sup>1</sup>, Elad Zehavi<sup>1</sup>, Alon Bernstein<sup>1,2</sup>, Mirit Hen<sup>1</sup>, Maayan Holsblat<sup>1</sup>, Ori Pearl<sup>1</sup> and Avi Zadok<sup>1,2 Mirit</sup>

#### **Abstract**

Forward Brillouin scattering is an opto-mechanical effect in which two co-propagating optical fields couple with an acoustic mode in a common medium. The effect has been studied in standard optical fibers since 1985, however nearly all studies have been limited to the single optical mode regime. Forward Brillouin scattering in single-mode fibers takes place through two classes of acoustic modes only: purely radial ones and modes of two-fold azimuthal symmetry. Acoustic modes may only be stimulated at their cut-off frequencies, and the acoustic frequencies in standard fibers are limited to 600 MHz. In this work, we extend the study of forward Brillouin scattering to few-mode optical fibers through analysis, calculations, and experiment. Measurements are performed in a commercial, off-the-shelf step-index fiber with standard cladding through three optical modes. We demonstrate for the first time the stimulation of acoustic modes with first-order and fourth-order azimuthal symmetries. Acoustic frequencies up to 1.8 GHz are observed, and the acoustic modes are stimulated above their cut-off frequencies. Angular momentum is transferred between the orbital degrees of freedom of the optical and acoustic waves. The results extend the understanding and formulation of forward Brillouin scattering in optical fibers, and they may find applications in fiber lasers, sensing, non-reciprocal propagation effects, and quantum states manipulation.

#### Introduction

Brillouin scattering is an opto-mechanical interaction that couples between traveling optical and acoustic waves in a common medium<sup>1-8</sup>. The phenomenon has been studied in fibers for over 50 years 1-8. Brillouin scattering in standard fibers may take place in either the backward or forward directions<sup>1–8</sup>. In backward interactions, two counter-propagating optical field components may stimulate a longitudinal acoustic mode that is guided in the core of the fiber<sup>6-8</sup>. In forward Brillouin scattering, two co-propagating optical fields couple with a predominantly transverse acoustic mode that is guided by the entire cladding cross-section<sup>1–5</sup>. Forward Brillouin scattering in single-mode fibers has been formulated and reported in 1985<sup>1</sup>. Interest in the effect has increased in recent years, towards sensing of substances outside the boundaries of standard cladding, where guided light does not reach<sup>5,9-24</sup>. The decay rates of the acoustic modes in

forward Brillouin scattering interactions are affected by the elastic boundary conditions at the edge of the cladding, and their monitoring enables the analysis of surrounding media<sup>5,9–24</sup>.

Most studies of forward Brillouin scattering in standard fibers were carried out in the single-mode regime<sup>1-5</sup>. A pair of optical fields in the fundamental, single mode may only stimulate acoustic modes of two specific classes: purely radial ones, and modes of two-fold azimuthal symmetry<sup>1-5</sup>. Although the fiber cladding supports guided acoustic modes of any integer order of azimuthal symmetry, other classes of acoustic modes cannot be addressed through forward Brillouin scattering in singlemode fibers. The efficiency of forward Brillouin scattering scales with the spatial overlap between the transverse profiles of the optical and acoustic modes involved<sup>1–5</sup>. In standard single-mode fibers, that overlap is maximal for acoustic modes of frequencies between 200-600 MHz<sup>1-5</sup>. The effect diminishes strongly at higher acoustic frequencies. Lastly, forward Brillouin stimulation of acoustic modes in single-mode fibers is only possible at their cutoff frequencies<sup>1–5</sup>. At that limit, the acoustic modes are almost entirely transverse, and their axial wavenumbers are vanishingly small<sup>1-5</sup>.

© The Author(s) 2025

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

Correspondence: Avi Zadok (Avi.Zadok@technion.ac.il)

<sup>&</sup>lt;sup>1</sup>Faculty of Engineering and Institute for Nano-Technology and Advanced Materials, Bar-llan University, Ramat-Gan 5290002, Israel

<sup>&</sup>lt;sup>2</sup>Presently with the Faculty of Electrical and Computer Engineering and the Solid State Institute, Technion – Israel Institute of Technology, Haifa 3200003, Israel

<span id="page-1-0"></span>Over the last decade, few-mode optical fibers have taken an increasing role in space-division multiplexing of optical telecommunication channels<sup>25,26</sup>, and they have also found many sensing applications<sup>27</sup>. The number of mode groups supported by the fiber can be controlled through the dimensions and index contrast of the core<sup>28,29</sup>. Few-mode fibers provide additional degrees of freedom for Brillouin scattering interactions, as the optical fields that take part in the process may be guided in different spatial modes. Brillouin scattering interactions through multiple guided optical modes have been reported in photonic integrated waveguides<sup>30-32</sup> and in thin tapered fibers<sup>33,34</sup>. Backward Brillouin scattering interactions have been investigated in standard few-mode fibers<sup>35,36</sup>, and they were used towards strain and temperature sensing and for modal dispersion analysis<sup>37</sup>. The forward effect has been studied in standard, panda-type polarization-maintaining fibers, in which the two polarization modes are nondegenerate<sup>38</sup>. However, the difference in effective indices between the two principal states of the fiber is comparatively small, in the fourth decimal point. In addition, the guided acoustic modes of the panda-type fiber cannot be solved analytically and do not maintain regular azimuthal symmetries<sup>38</sup>. Forward Brillouin scattering in standard few-mode fibers has yet to be examined.

In this work, we report the analysis, calculations, and experimental demonstration of forward Brillouin scattering in a step-index few-mode fiber with standard cladding. The spectrum of forward Brillouin scattering is formulated for the launch of each of the optical fields involved in an arbitrary guided mode. The experimental setup supported selective coupling of light to the fundamental  $LP_{01}$  mode, the  $LP_{02}$  mode, or the  $LP_{11}$  mode group of a few-mode fiber. The results show that forward Brillouin scattering in the  $LP_{02}$  mode reaches acoustic frequencies up to 1.8 GHz, much higher than in the fundamental mode. The measurements demonstrate the Brillouin stimulation of additional classes of acoustic modes, with first-order and fourth-order azimuthal symmetries, which are inaccessible through the corresponding process in single-mode fibers. Further, inter-modal interactions between optical waves in the  $LP_{01}$  and  $LP_{02}$  modes stimulate acoustic modes that are detuned from their cut-off frequencies by a few MHz. Certain inter-modal forward Brillouin interactions signify the transfer of angular momentum quanta between the orbital degrees of freedom of optical and acoustic waves<sup>39,40</sup>. The results extend the formulation and scope of fiber opto-mechanics beyond the single-mode regime, and they may find applications in fiber lasers, sensing, and quantum states manipulation.

#### Results

# Analysis of forward Brillouin scattering in standard fewmode fibers

Solutions to Maxwell's equations in standard stepindex optical fibers are given by a discrete set of optical modes, denoted by  $HE_{ln}$  and  $EH_{ln}$  [29]. The first integer index  $l \geq 0$  denotes the order of azimuthal symmetry of a given solution, whereas the second integer  $n \geq 1$ refers to the radial order. In the  $HE_{ln}$  modes the axial component of the magnetic field is larger than that of the electric field. The opposite is true for the  $EH_{ln}$ modes. In both categories, the axial field components are much smaller than the transverse ones. For l=0the solutions are referred to as  $TE_{0n}$  and  $TM_{0n}$  modes, in which the transverse vector profile of the electric field is purely radial (for  $TM_{0n}$ ) or purely torsional (for  $TE_{0n}$ ).

The exact modal solutions may be classified in groups which share the same transverse radial profiles. These mode groups are referred to as the linearly polarized (LP) modes  $LP_{ln}$  [29]. Each  $LP_{0n}$  group consists of the  $HE_{1n}$  mode only, and each  $LP_{1n}$  group includes the  $TE_{0n}$ ,  $TM_{0n}$  and  $HE_{2n}$  modes. For  $l \geq 2$ , each  $LP_{ln}$  group consists of the  $HE_{l+1,n}$  and  $EH_{l-1,n}$  modes. The differences in the refractive indices among modes within the same LP group are in the order of  $10^{-5}$  refractive index units (RIU), 2-3 orders of magnitude smaller than the corresponding differences between different LP mode groups. In the following we disregard the small differences between effective indices of modes in the same LP group.

Let us denote the axial propagation constant of optical modes group  $LP_{ln}$  as  $\beta_{ln}$ , and define:  $h_{ln}^{core} = \sqrt{n_1^2 k_0^2 - \beta_{ln}^2}$  and  $h_{ln}^{clad} = \sqrt{\beta_{ln}^2 - n_2^2 k_0^2}$ . Here  $n_{1,2}$  are the refractive indices of the uniform core and cladding, respectively, and  $k_0$  is the vacuum wavenumber of incident light. Within the weak guiding approximation, which is valid for standard fibers, the radial profile of the optical field in group  $LP_{ln}$  is given by

$$G_{ln}(r) = E_{ln} \begin{cases} \frac{J_l(h_{ln}^{core}r)}{h_{ln}^{core}J_{l+1}(h_{ln}^{core}a)} r \le a \\ \frac{K_l(h_{ln}^{clad}r)}{h_{ln}^{clad}K_{l+1}(h_{ln}^{clad}a)} r > a \end{cases}$$
 (1)

In Eq. (1), r is the radial transverse coordinate, a denotes the core radius,  $J_l$  is the Bessel function of the first kind, order l, and  $K_l$  represents the modified Bessel function of the second kind, order l. The factor  $E_{ln}$  is a normalization constant (see below). The normalized transverse profiles of the electric field vectors in the

<span id="page-2-0"></span>guided optical core modes of the fiber are expressed as

$$\vec{E}_{T,ln}^{(HE)}(r,\phi) = G_{l-1,n}(r) \left[ \left\{ \frac{\cos(l\phi)}{\sin(l\phi)} \right\} \hat{r} + \left\{ \frac{-\sin(l\phi)}{\cos(l\phi)} \right\} \hat{\phi} \right]$$
(2

$$\vec{E}_{T,ln}^{(EH)}(r,\phi) = G_{l+1,n}(r) \left[ \begin{cases} \cos(l\phi) \\ \sin(l\phi) \end{cases} \hat{r} + \begin{cases} \sin(l\phi) \\ -\cos(l\phi) \end{cases} \hat{\phi} \right]$$
(3)

The expressions in Eqs. (2) and (3) relate to the  $HE_{ln}$  and  $EH_{ln}$  modes, respectively. In the above equations  $\phi$  denotes the transverse azimuthal coordinate and  $\hat{r}$ ,  $\hat{\phi}$  are unit vectors in the radial and azimuthal directions, respectively. Each mode includes two spatially orthogonal solutions, denoted in the curled brackets. The normalization constants  $E_{ln}$  in Eq. (1) are defined so that  $\iint \left| \vec{E}_{T,ln}^{(HE),(EH)}(r,\phi) \right|^2 r dr d\phi = 1.$  The units of  $G_{ln}$  (and of  $\vec{E}_{T,ln}^{(HE),(EH)}$ ) are m<sup>-1</sup>.

Consider two co-propagating optical fields of optical frequencies  $\omega_{1,2}=\omega_p\pm\frac{1}{2}\Omega$ , in spatial modes 1 and 2, respectively,

$$\vec{E}_{1,2}(r,\phi,z,t) = A_{1,2}(z)\vec{E}_{T,1,2}(r,\phi) \exp\Bigl(j\beta_{1,2}z - j\omega_{1,2}t\Bigr) + c.c \tag{4}$$

Here  $\omega_p$  is a central optical frequency,  $\Omega$  denotes a frequency detuning on the acoustic scale,  $A_{1,2}(z)$  represent scalar complex magnitudes in Volts that may vary with axial position z, and t stands for time.  $\beta_{1,2}$  and  $\vec{E}_{T1,2}$  are the propagation constants and normalized transverse profiles of the two waves, according to their specific modes. The electro-strictive stress tensor  $\sigma_{1,2}$   $[{\rm N}\times{\rm m}^{-2}]$  associated with the two fields in spatial modes 1 and 2 includes components which propagate along the fiber axis with the frequency difference  $\Omega$  and an axial wavenumber  $K=\beta_1-\beta_2$ . These components of the stress tensor are given by  $^{41}$ 

components of  $\vec{E}_{T,1,2}$ , and  $E_{\phi,1,2}$  are the corresponding azimuthal components. The electro-strictive driving force per unit volume  $\vec{F}_{1,2}$  [N × m<sup>-3</sup>], induced by the pair of fields in modes 1 and 2, is derived from the stress tensor<sup>41</sup>:

$$\vec{F}_{1,2}(r,\phi,z,t) = -\left[\frac{\partial \sigma_{r,1,2}}{\partial r} + \frac{1}{r}\frac{\partial \sigma_{r\phi,1,2}}{\partial \phi} + \frac{1}{r}\left(\sigma_{rr,1,2} - \sigma_{\phi\phi,1,2}\right)\right]\hat{\boldsymbol{r}} - \left[\frac{\partial \sigma_{r\phi,1,2}}{\partial r} + \frac{1}{r}\frac{\partial \sigma_{\phi\phi,1,2}}{\partial \phi} + \frac{2}{r}\sigma_{r\phi,1,2}\right]\hat{\boldsymbol{\phi}}$$
(6)

The expression may be rearranged as

$$\vec{F}_{1,2}(r,\phi,z,t) = \frac{1}{4n_0c} \vec{f}_{1,2}(r,\phi) P(\Omega,z) \exp(jKz - j\Omega t) + c.c$$
 (7)

The vector  $\vec{f}_{1,2}(r,\phi)$  (units of m<sup>-3</sup>) contains the transverse dependence of the electro-strictive force per unit volume. Examination of Eq. (7) reveals that the electrostrictive force per unit volume  $\vec{F}$  propagates along the fiber axis as a wave, whose magnitude scales with the beating power P between the two optical fields. The frequency of that wave equals the difference  $\Omega$  between the two optical frequencies, and its axial wavenumber K is the difference between the two optical propagation constants. Further, substitution of Eqs. (2) and (3) into Eqs. (5) and (6) reveals that the electro-strictive force includes terms with azimuthal orders  $l_1 \pm l_2$  only, where  $l_{1,2}$  are the azimuthal orders of the two optical fields. For example, when both optical waves are guided in the fundamental mode  $LP_{01}$  ( $l_{1,2}=1$ ), the electro-strictive force per unit volume consists of a radially symmetric term and a term of twofold azimuthal symmetry. Expressions for the specific case are given in many references $^{1-5}$ . By contrast, if the optical fields 1 and 2 propagate in arbitrary high-order modes, the electro-strictive force may take up any integer order of azimuthal symmetry.

The axial wavenumber of the electro-strictive force per unit volume varies considerably between intra-modal processes, in which the two optical fields propagate in the same spatial mode, and inter-modal processes in which

$$\begin{pmatrix} \sigma_{rr,1,2}(r,\phi,z,t) \\ \sigma_{\phi\phi,1,2}(r,\phi,z,t) \\ \sigma_{r\phi,1,2}(r,\phi,z,t) \end{pmatrix} = -\frac{1}{4n_0c} n_0^4 \begin{pmatrix} p_{11} & p_{12} & 0 \\ p_{12} & p_{11} & 0 \\ 0 & 0 & p_{44} \end{pmatrix} \begin{pmatrix} E_{r,1}(r,\phi)E_{r,2}(r,\phi) \\ E_{\phi,1}(r,\phi)E_{\phi,2}(r,\phi) \\ E_{r,1}(r,\phi)E_{\phi,2}(r,\phi) \end{pmatrix} \times P(\Omega,z) \exp(jKz - j\Omega t) + c.c$$
 (5)

In Eq. (5),  $p_{11}, p_{12}$  and  $p_{44} = \frac{1}{2}(p_{11} - p_{12})$  are unitless photoelastic parameters of silica,  $n_0 \approx n_{1,2}$  is the refractive index of silica, and c denotes the speed of light in vacuum.  $P(\Omega, z) = 2nc\varepsilon_0 A_1(z)A_2^*(z)$  [W] refers to the beating power between the two optical waves, where  $\varepsilon_0$  is the vacuum permittivity. Lastly,  $E_{r,1,2}$  denote the radial

the two modes are different. In the intra-modal case,  $K=n_{\rm eff,1}\Omega/c$ , where  $n_{\rm eff,1}$  is the effective index of the common optical mode. That wavenumber is very small, typically in the order of  $1-10~{\rm rad}\times {\rm m}^{-1}$ . By contrast, in inter-modal interactions we find  $K=n_{\rm eff,1}(\omega_{\rm p}+\frac{1}{2}\Omega)/c-n_{\rm eff,2}(\omega_{\rm p}-\frac{1}{2}\Omega)/c\approx (n_{\rm eff,1}-n_{\rm eff,2})\omega_{\rm p}/c$ , where  $n_{\rm eff,2}$  is the effective

<span id="page-3-0"></span>index of optical mode 2 [38]. Since the difference in effective indices between mode groups may reach the second decimal point, the axial wavenumber of the electro-strictive force driven by two distinct mode groups may reach the order of  $10^4 \, \mathrm{rad} \times \mathrm{m}^{-1}$ . These values may be within a single order of magnitude of the wavenumbers of bulk acoustic waves of frequency  $\Omega$  in silica. The large differences in wavenumbers between intra-modal vs.

$$\Psi = \frac{\Omega b}{\nu_L}; \Phi = \frac{\Omega b}{\nu_S}; \Theta_{\mathbf{p}}(\xi) = \frac{\xi J_{p-1}(\xi)}{J_p(\xi)}$$
(9)

Here  $v_{L,S}$  are the velocities of dilatational and shear acoustic waves in silica, respectively, and b denotes the cladding radius. The normalized displacement profile of mode  $TR_{pm}$  is given by  $^{1-5}$ 

$$\vec{u}_{pm}(r,\phi) = D_{pm} \left[ A_{pm} \frac{\Omega_{pm}}{\nu_L} J_p' \left( \frac{\Omega_{pm}}{\nu_L} r \right) + \frac{p}{r} C_{pm} J_p \left( \frac{\Omega_{pm}}{\nu_S} r \right) \right] \left\{ \frac{\cos(p\phi)}{\sin(p\phi)} \right\} \hat{r} + D_{pm} \left[ \frac{p}{r} A_{pm} J_p \left( \frac{\Omega_{pm}}{\nu_L} r \right) + C_{pm} \frac{\Omega_{pm}}{\nu_S} J_p' \left( \frac{\Omega_{pm}}{\nu_S} r \right) \right] \left\{ \frac{-\sin(p\phi)}{\cos(p\phi)} \right\} \hat{\phi}$$

$$(10)$$

inter-modal scattering manifest in the forward Brillouin spectra of the two settings, as discussed later in this section.

The standard cladding of an optical fiber also serves as an acoustic waveguide, supporting several categories of guided acoustic modes 42,43. Solutions to the elastic wave equations for the boundary conditions of a bare fiber in air are in the form of torsional-radial (TR) modes  $TR_{nm}$ , in which the transverse profiles of material displacement are described by an integer azimuthal order  $p \ge 0$  and an integer radial order  $m \ge 1$ . Displacement in modes with p = 0 is either purely radial, (such modes are denoted by  $R_{0m}$ ), or entirely torsional (in so-called  $T_{0m}$  modes). Unlike the optical modes discussed above, which are highly confined to the core, the acoustic TR modes relevant to forward Brillouin scattering span the entire crosssection of the fiber cladding. (Note, however, that acoustic modes guided by the core of standard fibers exist as well, and so do optical cladding modes that span the entire fiber cross-section. These categories of acoustic core modes and optical cladding modes are not considered in this work.)

Each TR-guided acoustic mode is characterized by a cut-off frequency  $\Omega_{pm}$ , below which it may no longer propagate in the axial direction. Close to their cut-offs, the axial wavenumbers of the acoustic modes vanish and their phase velocities in the axial direction approach infinity. At that limit, both the material displacement vectors and the wave vectors of the acoustic modes are almost entirely transverse<sup>42,43</sup>. The cut-off frequency  $\Omega_{pm}$  is given by the  $m^{\rm th}$  eigen-value of the boundary conditions equation for a bare fiber cladding in air<sup>1-5</sup>:

$$\begin{vmatrix} p^2 - 1 - \frac{1}{2} \Psi^2 & 2(p^2 - 1) \left[ \Theta_p(\Psi) - p \right] - \Psi^2 \\ \Theta_p(\Phi) - p - 1 & 2p^2 - 2 \left[ \Theta_p(\Psi) - p \right] - \Psi^2 \end{vmatrix} = 0$$

The coefficients  $A_{pm}$ ,  $C_{pm}$  are given by the elements of the eigen-vector corresponding to the eigen-value  $\Omega_{pm}$  of the boundary conditions equation<sup>44</sup>, and the normalization constant  $D_{pm}$  is chosen so that  $\iint \left|\vec{u}_{pm}(r,\phi)\right|^2 r dr d\phi = 1.$  The units of  $\vec{u}_{pm}$  are therefore m<sup>-1</sup>. The prime superscript represents the derivative of a function with respect to its argument.

The radial and azimuthal components of the normalized displacement in Eq. (10) consist of two terms each. The first term in each pair describes dilatational wave motion, governed by velocity  $v_L$ , whereas the second term in each pair represents shear wave motion with velocity  $v_S$  [44]. Every  $TR_{pm}$  mode with  $p \ge 1$  includes nonzero contributions of both types of waves. The relative magnitudes of the two contributions are proportional to  $A_{pm}$ ,  $C_{pm}$ . TR modes may be broadly classified as either predominantly dilatational, where  $A_{pm} \gg C_{pm}$ , or shear-like, in cases where  $C_{pm} \gg A_{pm}$  [17,18,44]. Monitoring both classes of TR modes extends sensing applications of forward Brillouin scattering<sup>44</sup>. The radial modes  $R_{0m}$  are purely dilatational, whereas the  $T_{0m}$  modes are strictly shear waves. The spacing between the cut-off frequencies  $\Omega_{pm}$  of TR modes of the same order p that are primarily dilatational is approximately  $v_L/(2b)$ , and the corresponding spacing for shear-like modes equals approximately  $v_S/(2b)$ [17,18]. While the classification of modes as either dilatational or shear-like is not complete, and the above frequency spacings are not precise, they are nevertheless useful in the study of forward Brillouin scattering processes<sup>17,18,44</sup>

Close to cut-off, the dispersion relations between axial wavenumber K and frequency  $\Omega$  of dilatational or shear-dominated modes may be approximated by  $^{1-5}$ 

$$\Omega - \Omega_{pm} \approx \frac{\nu_{L,S}^2}{2\Omega_{nm}} K^2 \tag{11}$$

The detuning from cut-off may reach several MHz for the *K* values of inter-modal forward Brillouin stimulation. <span id="page-4-0"></span>The electro-strictive force per unit volume may stimulate the propagation of guided acoustic modes of the same frequency  $\Omega$  and wavenumber K. The displacement in [m] of the stimulated acoustic wave can be expressed as

$$\vec{U}_{pm}(r,\phi,z,t) = b_{pm}(\Omega,z)\vec{u}_{pm}(r,\phi)\exp(jKz - j\Omega t) + c.c$$
(12)

Here  $b_{pm}(\Omega,z)$  [m<sup>2</sup>] denotes a modal magnitude which is frequency dependent and may also vary with axial position. The acoustic wave magnitude scales with the beating power between the optical fields  $P(\Omega,z)$ , and with the spatial overlap integral between the transverse profiles of the electro-strictive force per unit volume and the acoustic mode displacement<sup>1–5</sup>:

$$Q_{1,2,pm}^{(ES)} = \int_{0}^{2\pi} \int_{0}^{b} \vec{u}_{pm}(r,\phi) \cdot \vec{f}_{1,2}(r,\phi) r dr d\phi$$
 (13)

The spatial overlap integral depends on the choices of the optical modes 1 and 2 and of the acoustic mode  $TR_{pm}$ . The overlap vanishes when the azimuthal orders of  $\vec{u}_{pm}$  and  $\vec{f}_{1,2}$  do not match. Consequently, the azimuthal order p of the stimulated acoustic mode must equal  $l_1 \pm l_2$ . Referring again to the specific case of two optical fields in the fundamental mode in which  $l_{1,2}=1$ , we find that only acoustic modes with p=0,2 may be excited through forward Brillouin interactions:  $R_{0m}$ ,  $T_{0m}$ , or  $TR_{2m}$ . Further, the azimuthally independent component of  $\vec{f}_{1,1}$  in single-mode fiber is entirely in the  $\hat{r}$  direction  $\hat{f}_{1,1}$  in Single-mode fiber is entirely in the  $\hat{r}$  direction  $\hat{f}_{1,1}$  in single-mode fiber is entirely in the  $\hat{r}$  direction  $\hat{f}_{1,1}$  in single-mode fiber is entirely in the  $\hat{r}$  direction  $\hat{f}_{1,1}$  in single-mode fiber is entirely in the  $\hat{r}$  direction  $\hat{f}_{1,1}$  in single-mode fiber is entirely in the  $\hat{r}$  direction  $\hat{f}_{1,1}$  in single-mode fiber, but the  $\hat{f}_{1,1}$  are not.

By contrast, forward Brillouin interactions in few-mode fibers, with one or both optical fields propagating in optical modes with  $l \neq 1$ , may result in the stimulation of additional classes of guided acoustic modes with different azimuthal symmetries. For example, the  $LP_{1,1}$  group contains modes with l=0 and l=2. Electro-strictive stimulation through optical modes within that group may generate acoustic waves with azimuthal orders p=0,2,4. Inter-modal interactions between optical fields in the  $LP_{0,1}$  mode and the  $LP_{1,1}$  group might stimulate acoustic modes with p=1 or p=3.

Material displacement in the stimulated acoustic mode is associated with symmetric strain in the form of a unitless tensor  $S_{pm}$ :

$$\mathbf{S}_{pm}(r,\phi,z,t) = b_{pm}(\Omega,z)\mathbf{s}_{pm}(r,\phi)\exp(j\mathbf{K}z-j\Omega t) + c.c$$
 (14)

The elements of the symmetric normalized strain tensor  $s_{pm}(r, \phi)$ , in units of m<sup>-2</sup>, are defined as<sup>42,43</sup>

$$s_{rr,pm}(r,\phi) = \frac{\partial u_{r,pm}(r,\phi)}{\partial r} \tag{15}$$

$$s_{\phi\phi,pm}(r,\phi) = \frac{u_{r,pm}(r,\phi)}{r} + \frac{1}{r} \frac{\partial u_{\phi,pm}(r,\phi)}{\partial \phi}$$
(16)

$$s_{r\phi,pm}(r,\phi) = \frac{1}{2} \left( \frac{1}{r} \frac{\partial u_{r,pm}(r,\phi)}{\partial \phi} + \frac{\partial u_{\phi,pm}(r,\phi)}{\partial r} - \frac{u_{\phi,pm}(r,\phi)}{r} \right)$$

$$(17)$$

In the above relations,  $u_{r,pm}$  and  $u_{\phi,pm}$  denote the radial and azimuthal components of the normalized displacement vector, respectively (see Eq. (10)). Strain in the fiber medium gives rise to photoelastic perturbations to the dielectric tensor<sup>1-5,41</sup>:

$$\Delta \varepsilon_{pm}(r, \phi, z, t) = b_{pm}(\Omega, z) \mu_{pm}(r, \phi) \exp(jKz - j\Omega t) + c.c$$
(18)

where the elements of the transverse dependence tensor  $\mu_{pm}$  are of the form  $^{1-5,41}$ 

$$\begin{pmatrix} \mu_{rr,pm}(r,\phi) \\ \mu_{\phi\phi,pm}(r,\phi) \\ \mu_{r\phi,pm}(r,\phi) \end{pmatrix} = -n_0^4 \begin{pmatrix} p_{11} & p_{12} & 0 \\ p_{12} & p_{11} & 0 \\ 0 & 0 & p_{44} \end{pmatrix} \begin{pmatrix} s_{rr,pm}(r,\phi) \\ s_{\phi\phi,pm}(r,\phi) \\ 2s_{r\phi,pm}(r,\phi) \end{pmatrix}$$
(19)

The perturbations to the dielectric tensor propagate along the fiber as a wave of frequency  $\Omega$  and wavenumber K. The perturbations scale with the modal displacement magnitude  $b_{pm}(\Omega,z)$ , and hence also with the beating power between the two stimulating optical fields,  $P(\Omega,z)$  [1-5].

The acoustically induced dielectric perturbation may couple light between a pair of optical fields,  $\vec{E}_{3,4}$ , propagating in optical modes 3 and 4:

$$\vec{E}_{3,4}(r,\phi,z,t) = A_{3,4}(z)\vec{E}_{T,3,4}(r,\phi) \exp(j\beta_{3,4}z - j\omega_{3,4}t) + c.c$$
(20)

Here  $A_{3,4}$  are the scalar complex magnitudes of the two fields [V],  $\beta_{3,4}$  are their propagation constants in their respective modes,  $\vec{E}_{T,3,4}$  are the corresponding normalized transverse profiles of the two modes, and  $\omega_{3,4}$  are their respective optical frequencies. Effective coupling requires matching in frequency and wavenumber between the pair of optical fields and the photoelastic perturbations: The difference in frequencies  $\omega_3 - \omega_4$  should equal the acoustic frequency  $\pm \Omega$ . The difference in wavenumbers  $\beta_3 - \beta_4$  must equal  $\pm K$ . In intra-modal processes, where all four optical waves involved propagate in the same

<span id="page-5-0"></span>mode 1, fulfillment of the frequency requirement guarantees that the wavenumbers condition is met as well. Since  $\beta_i=n_{\rm eff,1}\omega_i/c,\ i=1\dots 4$ , whenever  $\omega_3-\omega_4=\pm\Omega=\pm(\omega_1-\omega_2)$ , we automatically obtain also  $\beta_3-\beta_4=\pm(\beta_1-\beta_2)=\pm K.$  This property holds as long as chromatic dispersion remains negligible. It suggests that intra-modal forward Brillouin scattering would couple a third, input optical signal wave with both its sidebands, spectrally detuned by  $\pm\Omega$ , regardless of its optical frequency. The coupling may take the form of phase modulation, polarization rotation, or both, depending on the choice of acoustic mode and the state of polarization of the optical signal wave  $^{1-5,39}$ .

The requirement for wavenumber matching is markedly different in the case of inter-modal scattering, in which the acoustic wave is stimulated by optical fields in distinct spatial modes 1 and 2. Let us denote the optical frequencies  $\omega_{3,4}$  as  $\omega_s \pm \frac{1}{2}\Omega$ , where  $\omega_s$  is their average. Wavenumber matching in photoelastic coupling between  $\vec{E}_{3,4}$  is reached when  $(n_{\rm eff,3}-n_{\rm eff,4})\omega_{\rm s}/c=\pm(n_{\rm eff,1}-n_{\rm eff,4})\omega_{\rm s}/c$  $n_{\rm eff,2})\omega_{\rm p}/c=\pm K$ . Here  $n_{\rm eff,3}$  and  $n_{\rm eff,4}$  denote the effective indices in modes 3 and 4, respectively. Wavenumber matching for photoelastic scattering in the inter-modal process is guaranteed between the two initial stimulating waves  $E_{1,2}$ , as  $\omega_s = \omega_p$ ,  $n_{\text{eff},3} = n_{\text{eff},1}$  and  $n_{\text{eff},4} = n_{\text{eff},2}$ . In that case the forward Brillouin interaction is in the stimulated regime, with the same pair of optical waves used to both generate the acoustic wave and to monitor its induced scattering of light. Forward stimulated Brillouin scattering results in the amplification of the lowerfrequency optical field, at the expense of the higherfrequency one<sup>1–5</sup>. If the pair of modes 3 and 4 differs from the pair of modes 1 and 2, the wavenumbers for photoelastic coupling between  $\vec{E}_{3,4}$  might only be matched for specific frequencies  $\omega_s$ , if at all.

The photoelastic coupling between a pair of optical waves and a given acoustic mode scales with the three-way overlap integral between the transverse profiles of the dielectric perturbations and the two optical modes involved  $^{1-5}$ :

$$\begin{split} Q_{3,4,pm}^{(PE)} &= \int\limits_{0}^{2\pi} \int\limits_{0}^{b} \left[ \mu_{rr,pm} E_{r,3} E_{r,4} + \mu_{\phi\phi,pm} E_{\phi,3} E_{\phi,4} \right. \\ &\left. + \mu_{r\phi,pm} \left( E_{r,3} E_{\phi,4} + E_{\phi,3} E_{r,4} \right) \right] r dr d\phi \end{split} \tag{21}$$

Here  $E_{r,3}$  and  $E_{r,4}$  denote the radial components of  $\vec{E}_{T,3,4}$ , respectively, and  $E_{\phi,3}$ ,  $E_{\phi,4}$  are the corresponding azimuthal components. One may show that when optical modes 1 and 3 are the same, and so are modes 2 and 4, the overlap integrals of electro-strictive stimulation and photoelastic coupling (Eqs. (13) and (21)) become equal:  $Q_{1,2,\mathrm{pm}}^{(ES)} = Q_{1,2,\mathrm{pm}}^{(PE)}$  ([41], see Appendix). We denote that overlap integral below as  $Q_{1,2,\mathrm{pm}}$ . The spatial overlap

vanishes unless the azimuthal order p of the acoustic mode equals  $l_3 \pm l_4$ , where  $l_{3,4}$  are the azimuthal orders of optical modes 3 and 4, respectively.

The forward Brillouin scattering gain coefficient  $\gamma_{1,2,pm}(\Omega)$ , between a pair of optical modes 1 and 2 and an acoustic mode  $TR_{pm}$ , is given by  $^{5,45}$ 

$$\gamma_{1,2,pm}(\Omega) = j \frac{k_0 Q_{1,2,pm}^2}{8n_0^2 c \rho_0 \Gamma_{pm} \Omega_{pm}^{(\mathbb{R})}} \frac{1}{1 - 2j \frac{\Omega - \Omega_{pm}^{(\mathbb{R})}}{\Gamma_{pm}}} = j \gamma_{1,2,pm}^{(0)} \frac{1}{1 - 2j \frac{\Omega - \Omega_{pm}^{(\mathbb{R})}}{\Gamma_{pm}}}$$

$$(22)$$

Here  $k_0$  is the vacuum wavenumber at optical frequency  $\omega_{\rm p}$ ,  $\rho_0$  is the density of silica, and  $\Gamma_{pm}$  denotes the linewidth (or decay rate) of mode  $TR_{pm}$ . That linewidth depends on the mechanical impedance of media outside the cladding, and its monitoring provides the basis for forward Brillouin fiber sensing. For bare fibers in air, the linewidths are determined by acoustic dissipation in silica and by inhomogeneities in the cladding radius, and scale quadratically with acoustic frequency. Typical values in bare standard single-mode fibers range between tens to hundreds of kHz.

The frequency  $\Omega_{pm}^{(R)}$  of maximum forward Brillouin interaction is given by Eq. (11):

$$\Omega_{pm}^{(R)} \approx \Omega_{pm} + \frac{v_{L,S}^2}{2\Omega_{pm}} K^2 \approx \Omega_{pm} + \frac{k_0^2 v_{L,S}^2}{2\Omega_{pm}} (n_{\text{eff},1} - n_{\text{eff},2})^2$$
(23)

The latter approximate equality in Eq. (23) refers to inter-modal scattering, in which the detuning from cut-off is inversely proportional to the acoustic frequency. The resonance frequency  $\Omega_{pm}^{(R)}$  practically reduces to the cut-off frequency  $\Omega_{pm}$  for intra-modal forward Brillouin scattering processes. The velocities  $\nu_{L,S}$  apply to acoustic modes that are dominated by their dilatational or shear components, respectively.

The units of the gain coefficient  $\gamma_{1,2,pm}(\Omega)$  are W<sup>-1</sup> × m<sup>-1</sup>. It takes up its maximum magnitude on resonance:

$$\gamma_{1,2,pm}^{(0)} = \frac{k_0}{8n_0^2c\rho_0} \frac{Q_{1,2,pm}^2}{\Gamma_{pm}\Omega_{pm}^{(R)}}$$
(24)

Typical  $\gamma_{1,1,0\mathrm{m}}^{(0)}$  values for radial acoustic modes in standard, bare single-mode fibers reach the order of  $10\,\mathrm{W}^{-1}\times\mathrm{m}^{-1}$  [5]. These values are an order of magnitude weaker than those of backward Brillouin scattering in the same fiber, in which the acoustic waves are confined to the core in larger overlap with the optical mode<sup>6–8</sup>. Calculations of forward Brillouin scattering spectra for a specific few-mode fiber used in this work are presented next.

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

Fig. 1 Calculated opto-mechanical spectra  $|\gamma(\Omega/2\pi)|$  in a few-mode fiber. a Intra-modal forward Brillouin scattering between two optical waves in the fundamental  $LP_{01}$  mode, through radial acoustic modes  $R_{0m}$ . **b** Same as panel **a**, with torsional-radial acoustic modes of two-fold azimuthal symmetry  $TR_{2m}$ 

# Numerical calculations of forward Brillouin scattering spectra in a few-mode fiber

The forward Brillouin scattering gain coefficients were calculated for the parameters of the few-mode fiber used in experiments (see the section Experimental Results). The fiber has a standard cladding of pure silica with radius b of 62.8  $\mu$ m and refractive index  $n_2$  of 1.445 RIU. The uniform core of the fiber has a radius a of 4.8  $\mu$ m, with a refractive index  $n_1 = 1.461$  RIU. The V parameter of the fiber at a vacuum wavelength of 1550 nm is 4.196, and it supports the  $LP_{01}$  and  $LP_{02}$  modes and the  $LP_{11}$  and  $LP_{21}$ mode groups. The mode multiplexers used in our experiments supported the selective coupling of light to the  $LP_{01}$  mode,  $LP_{02}$  mode, and  $LP_{11}$  group only, hence the  $LP_{21}$  mode group was not considered further. The effective indices for the  $LP_{01}$  mode,  $LP_{02}$  mode, and  $LP_{11}$ mode group are 1.458, 1.446, and 1.453 RIU, respectively. The differences between the effective indices of the three constituent modes of the  $LP_{11}$  group are below  $5 \times 10^{-5}$ RIU. In the following calculations, the fiber was assumed to be uncoated with air outside the cladding. The modal linewidths  $\Gamma_{pm}$  were fitted based on experiments<sup>5</sup> (see the section Experimental Results).

Figure 1a presents the calculated opto-mechanical spectrum  $\left|\gamma_{LP01,LP01,0m}(\Omega)\right|$  of intra-modal forward Brillouin scattering between two optical waves in the fundamental  $LP_{01}$  mode, through the radial acoustic modes  $R_{0m}$ . Figure 1b shows the corresponding spectrum  $\left|\gamma_{LP01,LP01,2m}(\Omega)\right|$  for the same optical mode and the  $TR_{2m}$  acoustic modes. Both spectra are very similar to those of the corresponding processes in standard single-mode fibers 1-5. Forward Brillouin scattering through the  $R_{0m}$  modes is stronger, with  $\gamma_{LP01,LP01,0m}^{(0)}$  reaching  $20~{\rm W}^{-1}\times$ 

km<sup>-1</sup> at frequencies near 300 MHz, compared with maximum values of  $2.5-3 \text{ W}^{-1} \times \text{ km}^{-1}$  for the  $TR_{2m}$ modes. Similar values have been calculated and observed for single-mode fibers<sup>39</sup>. The peak magnitudes  $\gamma_{LP01,LP01,0m}^{(0)}$  decrease monotonously beyond 300 MHz frequency. The radial modes are purely dilatational, with regular spacing between their resonance frequencies (Fig. 1a). The spectrum of Fig. 1b consists of both predominantly dilatational and shear-like  $TR_{2m}$  acoustic with overall irregular spacing between modes, peaks  $^{17,18,44}$ . The  $|\gamma_{\mathit{LPO1},\mathit{LPO1},2m}(\Omega)|$  spectrum also decreases considerably beyond acoustic frequencies of 500 MHz. At higher frequencies, the radial dependence of the material displacement profile  $\vec{u}_{pm}$  changes sign within the spatial extent of the fundamental optical mode, and the spatial overlap integral largely cancels out.

Figure 2 presents the opto-mechanical spectra of intramodal forward Brillouin scattering in the  $LP_{02}$  mode.  $R_{0m}$ and  $TR_{2m}$  acoustic modes are considered in Fig. 2a, b, respectively. The peaks of the radial modes spectrum  $|\gamma_{\mathit{LP02,LP02,0m}}(\Omega)|$  reach a maximum at 300 MHz and decrease by nearly two orders of magnitude towards 600 MHz. The peak magnitudes  $\gamma_{LP02,LP02,0m}^{(0)}$  increase again towards acoustic frequencies of 1.2 GHz. Compared with the fundamental  $LP_{01}$  mode, the radial profiles of the displacement vectors of a high-frequency acoustic modes match better with the higher-order  $LP_{02}$  mode, leading to more efficient Brillouin stimulation. The  $|\gamma_{LP02,LP02,2m}(\Omega)|$ spectrum of Fig. 2b consists again of dilatational as well as shear  $TR_{2m}$  modes. In the 500–900 MHz range, the spectrum is dominated by the shear modes, identified by the closer spacing  $v_S/(2b)$  between adjacent peaks. In that frequency range, the radial profiles of the shear modes

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

Fig. 2 Calculated opto-mechanical spectra  $|\gamma(\Omega/2\pi)|$  in a few-mode fiber. a Intra-modal forward Brillouin scattering between two optical waves in the  $LP_{02}$  mode, through radial acoustic modes  $R_{0m}$ . b Same as panel a, with torsional-radial acoustic modes of two-fold azimuthal symmetry  $TR_{2m}$ 

![](_page_7_Figure_4.jpeg)

Fig. 3 Calculated opto-mechanical gain coefficients  $\operatorname{Im}\{\gamma(\Omega/2\pi)\}\$  in a few-mode fiber. a Inter-modal forward Brillouin scattering between one optical wave in the  $LP_{01}$  mode and another in the  $LP_{02}$  mode, through radial acoustic modes  $R_{0m}$ . b Same as panel a, with torsional-radial acoustic modes of two-fold azimuthal symmetry  $TR_{2m}$ 

better match with those of the optical mode  $LP_{02}$ . The dilatational modes, noted by a larger frequency spacing of approximately  $\nu_L/(2b)$ , become dominant beyond 1 GHz frequency.

Figure 3 shows the calculated spectra of inter-modal forward Brillouin scattering between the  $LP_{01}$  and  $LP_{02}$  modes. In this figure, the imaginary part of the gain coefficient  $\mathrm{Im}\{\gamma_{LP01,LP02,pm}(\Omega)\}$  is plotted, rather than its absolute value as in Figs. 1 and 2, since the experimental procedure for the characterization of inter-modal scattering processes measures the imaginary part directly<sup>5</sup>, (see Methods Section). Here too, only the  $R_{0m}$  and  $TR_{2m}$  acoustic modes may be stimulated. Figure 3a presents the  $\mathrm{Im}\{\gamma_{LP01,LP02,0m}(\Omega)\}$  spectrum, and  $\mathrm{Im}\{\gamma_{LP01,LP02,2m}(\Omega)\}$ 

is plotted in Fig. 3b. Both spectra differ from those of the intra-modal scattering processes through the same acoustic modes, as shown in Fig. 1 and Fig. 2. The intermodal scattering spectrum through the  $TR_{2m}$  modes is dominated by shear modes up to 700 MHz frequency and by dilatational modes above that frequency.

Figure 4 presents calculated spectra of forward Brillouin scattering interactions driven by optical fields in the  $LP_{11}$  mode group. The group consists of the  $TE_{01}$ ,  $TM_{01}$  and  $HE_{21}$  exact modal solutions. The experimental setup only allows for the coupling of light to all three modes together, and it does not separate between them. Figure 4a presents the  $|\gamma_{LP11,LP11,0m}(\Omega)|$  forward Brillouin scattering spectrum through the radial  $R_{0m}$  acoustic modes. The

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

Fig. 4 Calculated opto-mechanical spectra  $|\gamma(\Omega/2\pi)|$  in a few-mode fiber. a Forward Brillouin scattering between optical waves within the  $LP_{11}$  mode group, through radial acoustic modes  $R_{0m}$ . b Same as panel a, with torsional-radial acoustic modes of two-fold azimuthal symmetry  $TR_{2m}$ . c Same as panel a, with torsional-radial acoustic modes of four-fold azimuthal symmetry  $TR_{4m}$ . d Same as panel a, with purely torsional acoustic modes  $T_{0m}$ 

spectrum includes contributions of intra-modal scattering in each of the three modes within the  $LP_{11}$  mode group. The radio frequency phases of the three contributions may vary. In the example shown here, the mean value of the three terms is presented. Differences between the acoustic resonance frequencies of the three contributions are much smaller than the modal linewidths and cannot be observed. The spectrum extends towards higher frequencies than those of the corresponding process in the fundamental  $LP_{01}$  mode (Fig. 1a). The frequencies range is similar to that of the intra-modal scattering in the  $LP_{02}$ mode (Fig. 2a). The forward Brillouin scattering spectrum  $|\gamma_{LP11,LP11,2m}(\Omega)|$  for  $TR_{2m}$  acoustic modes is shown in Fig. 4b. The spectrum differs from those of  $TR_{2m}$  stimulated by other optical modes combinations, as presented earlier. It is dominated by dilatational modes above acoustic frequencies of 800 MHz.

Optical waves within the  $LP_{11}$  modes group can stimulate additional classes of acoustic modes, beyond the  $R_{0m}$  and  $TR_{2m}$  groups discussed thus far. Figure 4c shows the spectrum  $|\gamma_{LP11,LP11,4m}(\Omega)|$  of forward Brillouin scattering through the four-fold symmetric  $TR_{4m}$  acoustic modes. These modes can be driven by two pump fields in the  $HE_{21}$  optical mode within the  $LP_{11}$  group. This class of acoustic modes cannot be observed in forward Brillouin scattering over single-mode fibers. Shear modes within the  $TR_{4m}$  category dominate the spectrum up to 700 MHz, giving way to dilatational modes at higher frequencies. The cut-off frequencies  $\Omega_{4m}$  of the  $TR_{4m}$  modes are

similar to those of the  $TR_{2m}$  modes. However, the  $\Omega_{4m}$  frequencies are consistently lower than the corresponding  $\Omega_{2m}$  values by  $2\pi \times 1$ -2 MHz. These offsets are used to identify peaks associated with the  $TR_{4m}$  modes in experimental measurements (see the section Experimental Results).

Inter-modal forward Brillouin scattering between one optical field in the  $TE_{01}$  mode and another in the  $TM_{01}$  mode within the  $LP_{11}$  group can stimulate purely torsional  $T_{0m}$  acoustic modes as well. The calculated spectrum is shown in Fig. 4d. The process couples optical power between the  $TE_{01}$  and  $TM_{01}$  components within the  $LP_{11}$  mode group. The cut-off frequencies of the  $T_{0m}$  modes are higher than those of adjacent  $TR_{2m}$  modes by  $2\pi \times 1$ -2 MHz. The peak magnitudes of the optomechanical stimulation of  $T_{0m}$  modes are highest near 500 MHz frequency. Material displacement in the  $T_{0m}$  modes includes shear wave motion only.

Lastly, Fig. 5 shows the calculated spectra of intermodal forward Brillouin scattering between one optical wave in the fundamental  $LP_{01}$  mode and another in the  $LP_{11}$  modes group. The process involves the stimulation of the  $TR_{1m}$  acoustic modes of first-order azimuthal symmetry (panel a), and the three-fold symmetric  $TR_{3m}$  modes (Fig. 5b). Both classes of modes are inaccessible to forward Brillouin scattering in single-mode fibers. The peak magnitudes of  $\operatorname{Im}\{\gamma_{LP01,LP11,1m}(\Omega)\}$ , corresponding to the  $TR_{1m}$  modes, are four times stronger than those of  $\operatorname{Im}\{\gamma_{LP01,LP11,3m}(\Omega)\}$ , representing the  $TR_{3m}$  modes. The

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

Fig. 5 Calculated opto-mechanical gain coefficients  $\operatorname{Im}\{\gamma(\Omega/2\pi)\}$  in a few-mode fiber. a Inter-modal forward Brillouin scattering between one optical wave in the  $LP_{01}$  mode and another in the  $LP_{11}$  mode group, through torsional-radial acoustic modes  $TR_{1m}$  of first-order azimuthal symmetry. b Same as panel a, with torsional-radial acoustic modes of three-fold azimuthal symmetry  $TR_{3m}$ 

![](_page_9_Figure_4.jpeg)

spectrum of  $TR_{1m}$  modes is dominated by the dilatational ones.

### **Experimental results**

Figure 6a shows the measured normalized spectrum  $|\gamma_{LP01,LP01,0m}(\Omega)|^2$  of intra-modal forward Brillouin scattering in the fundamental  $LP_{01}$  mode of a few-mode fiber, through the radial acoustic modes  $R_{0m}$ . For the details of the experimental setup and protocols, see the Methods section. The fiber under test was 5 meters long, and it was stripped off its protective polymer coating to enhance forward Brillouin scattering. The parameters of the fiber were the same as those used above for calculations. The

corresponding calculated spectrum is plotted as well (see Fig. 1a). The agreement between experiment and calculations is very good. The spectrum is very similar to that of forward Brillouin scattering through the same acoustic modes in single-mode fibers<sup>1–5</sup>, as expected. The linewidths of the spectral peaks increase with frequency, from 100 kHz width for the 80 MHz peak up to about 1 MHz width at the resonance frequency of 700 MHz. The linewidths are broader than previously observed in uncoated single-mode fibers, and they scale linearly with acoustic frequency. Such scaling suggests broadening due to nonuniformity of the cladding diameter along the fiber under test<sup>46</sup>. Figure 6b presents the normalized measured

![](_page_10_Figure_2.jpeg)

in the  $LP_{02}$  mode of a few-mode fiber. a Radial acoustic modes  $R_{0m}$ . b Torsional-radial modes. The spectrum consists of the  $TR_{2m}$  modes only

and calculated spectra of intra-modal scattering in the fundamental optical mode through torsional-radial acoustic modes. The spectrum consists of two-fold symmetric  $TR_{2m}$  acoustic modes only. Here too, the experimental results agree with calculations and with known results in single-mode fibers<sup>1-5</sup>. Both dilatational and shear modes are observed. Note that the forward Brillouin scattering spectra through radial and torsional-radial modes are acquired using different detection schemes (see Methods). Therefore, the comparison between spectra in absolute scales is not provided. For experimental comparison between radial and torsional-radial modes excitation, see earlier works<sup>39</sup>.

Figure 7 shows the measured and calculated normalized spectra of intra-modal forward Brillouin scattering in the higher-order  $LP_{02}$  mode. Here too, the process takes place through  $R_{0m}$  (panel a) and  $TR_{2m}$  acoustic modes (panel b). Modes of both categories are observed up to a frequency of 1.8 GHz, much higher than those of corresponding intra-modal scattering in the fundamental mode. The peak magnitudes of the dilatational  $R_{0m}$  modes pass through a local minimum at acoustic frequencies near 800 MHz, due to poor spatial overlap with the optical mode. The  $TR_{2m}$  modes spectrum at that frequency range is dominated by the shear modes, identified by their closer spectral spacing, which exhibit better spatial overlap with the optical mode. The dilatational modes dominate the  $TR_{2m}$  spectrum beyond 1.1 GHz frequency. The experimental observations are in good agreement with calculations.

Next, the normalized spectra of forward Brillouin scattering between two optical fields in the  $LP_{11}$  group are presented. Figure 8 shows the spectrum of scattering through the radial  $R_{0m}$  modes,  $|\gamma_{LP11,LP11,0m}(\Omega)|^2$ . The

![](_page_10_Figure_7.jpeg)

Fig. 8 Measured (solid, blue) and calculated (dashed, red) normalized spectra  $|\gamma_{LP11,LP11,0m}(\Omega)|^2$  of intra-modal forward Brillouin scattering in the  $LP_{11}$  modes group of a few-mode fiber, through the radial acoustic modes Rom

measurements meet expectations. Figure 9a shows the corresponding spectra for torsional radial modes. The spectrum is dominated by the two-fold symmetric  $TR_{2m}$ modes, and it matches well with calculations. This time, however, many of the spectral peaks corresponding to the  $TR_{2m}$  modes are accompanied by adjacent secondary peaks, at frequencies that are 1-2 MHz lower. The secondary set of peaks represents the stimulation of the fourfold symmetric  $TR_{4m}$  modes. The observed frequency separation matches the difference between calculated cutoff frequencies  $(\Omega_{2m} - \Omega_{4m})/2\pi$ . The  $TR_{4m}$  acoustic modes are driven by optical fields in the  $HE_{21}$  component of the  $LP_{11}$  group. They do not appear in the spectra of

<span id="page-11-0"></span>![](_page_11_Figure_2.jpeg)

**Fig. 9 Observation of four-fold symmetric torsional-radial acoustic modes. a** Measured (solid, blue) and calculated (dashed, red) normalized spectra of intra-modal forward Brillouin scattering in the  $LP_{11}$  modes group of a few-mode fiber, through torsional-radial acoustic modes. The spectrum is dominated by the  $TR_{2m}$  modes. **b, c** Magnified views of the experimental trace of panel (a) (blue), alongside the measured, normalized torsional-radial modes spectrum of intra-modal scattering in the  $LP_{01}$  mode (red, repeated from Fig. 6b as a reference). The torsional-radial acoustic modes spectrum following stimulation through the  $LP_{11}$  modes group exhibits secondary peaks, which do not appear in the corresponding  $LP_{01}$  process. The frequencies of the secondary peaks are lower than those of the primary ones by 1–2 MHz. The secondary peaks represent the stimulation of  $TR_{4m}$  acoustic modes. Two examples of pairs of peaks are shown in the figure, however many others were observed

torsional-radial modes for intra-modal forward Brillouin scattering in the  $LP_{01}$  and  $LP_{02}$  modes (see Fig. 9). Two examples of pairs of peaks are shown in Fig. 9b, c, and many other pairs were observed in the frequencies range of 200–400 MHz. The results signify the first observation of the  $TR_{4m}$  class of modes in forward Brillouin scattering in fibers.

Calculations also predict the stimulation of purely torsional  $T_{0m}$  acoustic modes by one field component in the  $TE_{01}$  mode and another in the  $TM_{01}$  mode within the  $LP_{11}$  group (see Fig. 4d). Such stimulation would be accompanied by the coupling of optical power between the two components and may lead to polarization rotation of the combined  $LP_{11}$  polarized field. The cut-off frequencies of the  $T_{0m}$  acoustic modes are higher than those of adjacent  $TR_{2m}$  modes by  $2\pi \times 1-2$  MHz (as opposed to the cut-of frequencies of the  $TR_{4m}$ , which are lower than those of the  $TR_{2m}$  modes by comparable offsets). We were unable to resolve the stimulation of  $T_{0m}$  acoustic modes in our measurements. The division of the input field among the three constituent modes of the  $LP_{11}$  group is not controlled. The magnitudes of the launched  $TE_{01}$  and  $TM_{01}$  field components might have been too weak, and the polarization rotation induced by the  $T_{0m}$  modes might have been too small to be identified alongside the much stronger response of adjacent  $TR_{2m}$  modes.

The measured normalized coupling coefficient  $\operatorname{Im}\{\gamma(\Omega)\}$  of inter-modal forward Brillouin scattering between the  $LP_{01}$  optical mode and the  $LP_{11}$  mode group

![](_page_11_Figure_7.jpeg)

Fig. 10 Observation of torsional radial acoustic modes of first-order azimuthal symmetry. Solid blue—measured normalized gain coefficient of inter-modal forward stimulated Brillouin scattering between one optical wave in the fundamental  $LP_{01}$  mode and another in the  $LP_{11}$  mode group. Dashed red—calculated normalized gain coefficient  $Im\{y_{LP}01, LP11, 1m\}$  of inter-modal forward Brillouin scattering between the two optical modes through the  $TR_{1m}$  acoustic modes. Agreement with experiment is very good. The weaker stimulation of  $TR_{3m}$  modes, suggested by the analysis, was not observed in the measurements

is presented in Fig. 10. For the experimental setup and protocols for measuring inter-modal scattering, see Methods Section. The spectrum consists of stimulated  $TR_{1m}$  acoustic modes of first-order azimuthal symmetry.

![](_page_12_Figure_2.jpeg)

**Fig. 11 Stimulation of acoustic modes above their cut-off frequencies. a** Solid blue—measured normalized gain coefficient of inter-modal forward stimulated Brillouin scattering between one optical wave in the fundamental  $LP_{01}$  mode and another in the  $LP_{02}$  mode. Dashed red—calculated normalized gain coefficient of the inter-modal scattering process through the  $R_{0m}$  and  $TR_{2m}$  acoustic modes. Agreement with experiment is very good. **b**, **c** Magnified view of the measured normalized inter-modal scattering spectrum (blue), alongside the measured normalized spectra of intra-modal scattering in the fundamental  $LP_{01}$  mode. In both panels,  $R_{0m}$  modes are shown in red and  $TR_{2m}$  modes in green. In panel **b**, the resonance frequency of a dilatational  $R_{0m}$  mode is higher by 3.4 MHz in the intra-modal trace. The corresponding difference for the  $TR_{2m}$  shear mode shown in panel **c** is 1.9 MHz

Forward Brillouin scattering through this set of acoustic modes is also observed for the first time in this work. Like the  $TR_{4m}$  modes seen in Fig. 9, the  $TR_{1m}$  set of modes cannot be stimulated in single mode fibers. The cut-off frequencies  $\Omega_{1m}$  of these modes differ from  $\Omega_{0m}$  or  $\Omega_{2m}$  by tens of MHz, hence the observed peaks are distinct. The  $R_{0m}$  and  $TR_{2m}$  acoustic modes were not stimulated in this experiment, as expected. The spectrum is dominated by dilatational modes, although shear modes are observed as well at acoustic frequencies below 600 MHz.

Our analysis suggests that the inter-modal scattering process would also excite the  $TR_{3m}$  class of acoustic modes. However, the opto-mechanical coefficients for the stimulation of these modes are considerably smaller than those of the  $TR_{1m}$  modes (see Fig. 5), and the cut-off frequencies  $\Omega_{1m}$  and  $\Omega_{3m}$  of the two classes differ by only  $2\pi \times 1-2$  MHz. We were unable to resolve the stimulation of  $TR_{3m}$  modes in our experiments, and their study remains for future work.

The normalized spectrum of inter-modal forward Brillouin scattering between the  $LP_{01}$  and  $LP_{02}$  optical modes is presented in Fig. 11a. The measured response consists of the  $R_{0m}$  and  $TR_{2m}$  acoustic modes, and it agrees well with expectations. Careful comparison between the response of Fig. 11a and the spectra of  $R_{0m}$  and  $TR_{2m}$ 

modes obtained through intra-modal scattering reveals a significant difference. The resonance frequencies  $\Omega_{0m}^{(R)}$  and  $\Omega_{2m}^{(R)}$  of the inter-modal scattering spectrum are consistently higher than those observed through intra-modal scattering. Examples are shown in Fig. 11b, c. The difference is due to the larger axial wavenumber K of intermodal electro-strictive stimulation (see earlier analysis). Figure 12 plots the difference  $\Delta\Omega$  between the intermodal and intra-modal resonance frequencies, as a function of  $\Omega$ . The difference is inversely proportional to  $\Omega$ , and it follows the prediction of Eq. (23). The difference  $\Delta\Omega$  is larger for dilatational acoustic modes, due to their higher velocity.

# Discussion

This work extended the study of forward Brillouin scattering in standard, uniform-cladding fibers to the multi-optical mode regime, through analysis, calculations, and experiment. The process supports many possible combinations of intra-modal and inter-modal scattering. Unlike polarization maintaining or photonic crystal fibers, the forward Brillouin scattering spectra in the few-mode fiber are calculated analytically. Acoustic modes of arbitrary azimuthal orders can be stimulated in the few-mode fiber, as opposed to the  $R_{0m}$  and  $TR_{2m}$  modes only in single-mode fibers. The stimulation of

<span id="page-13-0"></span>![](_page_13_Figure_2.jpeg)

Fig. 12 Stimulation of acoustic modes above their cut-off frequencies. Circular markers—measured spectral offsets  $\Delta\Omega/2\pi$  between the resonance frequencies of inter-modal forward Brillouin scattering between the  $LP_{01}$  and  $LP_{02}$  modes, and the corresponding resonance frequencies of intra-modal scattering. The experimental uncertainties represent the measurement resolution of 100 kHz. Solid lines—calculated offsets according to Eq. (23). Modes dominated by their dilatational components are shown in blue, whereas those that are primarily of shear characteristics are shown in red. The observed spectral offsets agree with analysis. The offsets are inversely proportional to frequency, and they are larger for the dilatational modes due to their higher acoustic velocity

 $TR_{1m}$  and  $TR_{4m}$  modes has been demonstrated experimentally.

The forward Brillouin scattering spectra of the fewmode fiber extend to higher acoustic frequencies than in standard single-mode fibers: resonance frequencies up to 1.8 GHz were observed in the measurements. Further, inter-modal stimulation in the few-mode fiber may excite acoustic modes a few MHz above their cut-off frequencies. The acoustic modes, in this case, may take up axial wavenumbers in the order of  $10^4 \text{ rad} \times \text{m}^{-1}$ . Such large wavenumbers can lead to non-reciprocal coupling of counter-propagating signal waves between spatial optical modes and to narrowband optical isolation, as shown in polarization maintaining fibers and photonic integrated circuits<sup>38,47</sup>. The effect of media outside the cladding on the acoustic linewidth may differ among classes of modes<sup>44</sup>. Addressing additional mode groups may enhance the application of forward Brillouin scattering in fiber sensing 17,18,44. The elastic properties of media under test may also vary with acoustic frequency. The extension of forward Brillouin scattering towards higher acoustic frequencies over few-mode fibers would enable broader characterization of acoustic dispersion.

Inter-modal forward Brillouin scattering is associated with the amplification of one input optical field at the expense of another<sup>1–5</sup>. This amplification mechanism has

been the basis for a forward Brillouin laser over polarization maintaining fiber <sup>48</sup>, and may support similar lasing in few-mode fiber as well. The gain bandwidth of forward Brillouin scattering is extremely narrow, only 100 kHz in bare fibers, hence forward Brillouin lasers can become extremely coherent. The boundary conditions of acoustic modes make forward Brillouin fiber lasers highly sensitive to their environment <sup>48</sup>. Compared with polarization maintaining fibers, the few-mode fibers provide greater freedom for the choice of modes and the design of forward Brillouin lasers.

Both the optical and acoustic waves used in this work can carry angular momenta in their orbital degree of freedom<sup>39,40</sup>. The forward Brillouin scattering interactions through specific choices of modes signify the exchange of orbital angular momentum quanta between the optical and mechanical domains. These interactions may potentially serve towards the manipulation of quantum states at cryogenic temperatures.

While the reported characterization of forward Brillouin scattering in the few-mode fiber under test has been rather extensive, it is by no means exhaustive. Even with the three-mode fiber available to us, there are many additional possible combinations for the allocation of input fields to specific modes. For example, two intramodal scattering processes can be coupled through a common acoustic mode: A pair of pump waves in a common optical mode 1 would stimulate the acoustic wave through a first intra-modal process, and a signal wave in optical mode 2 would be scattered by the same acoustic wave in a second intra-modal process. We have successfully demonstrated such coupling between intramodal forward Brillouin scattering processes in polarization-maintaining fibers<sup>38</sup>, and their exploration over few-mode fibers remains for future study.

In this work, we were not able to resolve the simulation of  $TR_{3m}$  acoustic modes alongside the  $TR_{1m}$  ones in an inter-modal forward Brillouin scattering process, even though our analysis suggests that these modes should have been observed. The difficulty may have to do with the limited signal-to-noise ratio of the inter-modal measurements protocol. The signal-to-noise ratio may be improved using longer, uncoated fibers. Another limitation stems from the small separation between the cut-off frequencies of the  $TR_{1m}$  and  $TR_{3m}$  modes. The spectra of the  $TR_{3m}$  modes might be overshadowed by adjacent, stronger peaks due to  $TR_{1m}$  modes. We also could not observe the stimulation of the  $T_{0m}$  acoustic modes by optical fields within the  $LP_{11}$  mode group. The monitoring of forward Brillouin scattering within the  $LP_{11}$  group relies on polarization rotation. It is possible that the rotation associated with the coupling of light between the  $TE_{01}$  and  $TM_{01}$  field components within the  $LP_{11}$  group was too weak to be detected. The identification of the  $T_{0m}$ 

<span id="page-14-0"></span>![](_page_14_Figure_2.jpeg)

Fig. 13 Schematic illustrations of experimental setups used in characterization of forward Brillouin scattering in a few-mode fiber. a Intra-modal scattering. b Inter-modal scattering. EOM Mach-Zehnder electro-optic intensity modulator, SSB single-sideband electro-optic modulator, EFDA erbium-doped fiber amplifier, MDM mode division multiplexer, PC polarization controller

acoustic mode is also challenging due to the presence of adjacent, stronger peaks associated with the  $TR_{2m}$  modes category. The stimulation of the  $T_{0m}$  and  $TR_{3m}$  will be revisited in future work.

In summary, the study of forward Brillouin scattering in standard few-mode fibers extends the fundamental understanding and formulation of the effect, reaches higher acoustic frequencies and additional modal symmetries, and may find applications in fiber sensing, fiber lasing, non-reciprocal propagation, and quantum technologies.

#### **Materials and methods**

Figure 13a illustrates the experimental setup for the characterization of intra-modal forward Brillouin scattering in a few-mode fiber<sup>5,10,44,49</sup>. A laser diode of 1550 nm wavelength was the source of pump optical waves used to stimulate forward Brillouin scattering in the fiber. Pump light passed through an electro-optic intensity modulator, driven by a sine wave voltage of variable radio frequency  $\Omega$  from the output port of an electrical vector network analyzer. The modulator was biased at quadrature. The modulated pump wave was amplified in an erbium-doped fiber amplifier to an average optical power of 0.2-0.4 W and launched to one of the three input ports of a first mode-division multiplexer. In some of the measurements, a polarization scrambler was used in the pump branch. The magnitude of the pump power modulation  $P_{\nu}(\Omega)$  was calibrated for each radio frequency.

The mode multiplexer coupled the input pump wave to either the fundamental  $LP_{01}$  mode, the  $LP_{02}$  mode, or the  $LP_{11}$  mode group. The few-mode fiber under test (SK Photonics FMF) was 5 m long, and its parameters were specified in the description of numerical calculations. The fiber was stripped off its protective polymer coating to

enhance forward Brillouin scattering. The coating was removed through mechanical stripping and overnight immersion in acetone for the removal of residues. The output end of the fiber under test was connected to a second mode division multiplexer which separated the  $LP_{01}$  mode, the  $LP_{02}$  mode, and the  $LP_{11}$  group into three different physical output ports. An optical bandpass filter blocked the pump wave at the mode multiplexer output.

A continuous-wave signal from a second laser diode was used for monitoring the stimulated acoustic waves through photoelastic scattering. The signal wavelength was 1532 nm and its optical power was 2 mW. The signal wave was coupled with the modulated pump and launched into the same input port of the mode division multiplexer. The stimulated acoustic waves imprinted phase modulation and/or polarization rotation at radio frequency  $\Omega$  on the co-propagating signal wave<sup>5</sup>. The optical bandpass filter at the fiber under test output was adjusted to transmit the signal wave.

The output signal was analyzed through two detection channels. In one channel, the output signal was connected through a directional coupler to form a Sagnac interferometer loop<sup>49</sup>. Photoelastic phase modulation of the signal wave was converted to an intensity reading at the loop output<sup>49</sup>. Polarization controllers were used to maximize the output intensity modulation<sup>49</sup>. The output signal wave was detected by a photo-receiver of 1.6 GHz bandwidth, and the obtained voltage was connected to the input port of the electrical vector network analyzer. The analyzer measured the transfer function  $S(\Omega)$  of radio frequency voltage between the modulation of the optical pump wave and that of the detected signal wave. Traces were acquired with frequency steps of 10-20 kHz and an intermediate frequency bandwidth of 100 kHz and were averaged over 200 repetitions.

The frequency response of the forward Brillouin scattering process under test was estimated by the ratio  $H(\Omega) = S(\Omega)/P_p(\Omega)$  [5,49]. The polarization of the pump wave was scrambled during data acquisition at hundreds of kHz rates. In that manner, the contributions of all TR modes to the photoelastic modulation were canceled out of the collected data<sup>39</sup>. The measured response  $H(\Omega)$  was affected by the intra-modal forward Brillouin scattering through the radial modes  $R_{0m}$  only.

The signal wave at the output of the optical bandpass filter was split into a second detection channel which was based on a polarizer. A polarization controller was used to align the signal state of polarization to 50% transmission of optical power to the polarizer output. Photoelastic polarization rotation of the signal wave was converted to intensity modulation at the polarizer output 1,10,44. Polarization rotation takes place through torsional-radial modes of all orders, but not through radial modes<sup>39</sup>. The output signal was routed to an identical photoreceiver and the detected voltage was analyzed by the vector network analyzer using the same settings. The transfer function  $H(\Omega) = S(\Omega)/P_n(\Omega)$ of radiofrequency voltage in this case is related to the intramodal forward Brillouin scattering through all TRpm modes, of all azimuthal orders<sup>39</sup>. The polarization of the pump wave was not scrambled when using this detection channel. Since the radial and torsional-radial modes spectra are detected through different channels, the direct comparison between the absolute magnitudes of their excitation is not supported by the setup.

In addition to forward Brillouin scattering, the pump wave also induced phase modulation and polarization rotation of the signal via the Kerr effect<sup>50</sup>. The response of the Kerr effect is that of an immediate impulse, whereas that of photoelastic modulation extends over microseconds scale. The contribution of the Kerr effect may be effectively removed from the measurements using time gating, which eliminates the first few nanoseconds of the response<sup>49</sup>. Such gating is often performed by a synchronized optical switch within the experimental testbed<sup>49</sup>. Alternatively, when the output signal is acquired in the time domain, gating can be implemented through offline processing<sup>9,50</sup>. In this work, the forward Brillouin scattering processes were monitored in the frequency domain, and time gating could not be implemented directly. Instead, the inverse-Fourier transform of the complex-valued  $H(\Omega)$  was calculated offline to obtain the corresponding time-domain impulse response h(t). The impulse response was then gated to remove the contribution of the Kerr effect, and the Fourier transform  $H(\Omega)$  of the gated h(t) was calculated for further data analysis. The obtained  $H(\Omega)$  is proportional to the intra-modal forward Brillouin scattering coefficient  $\gamma_{1,1,pm}(\Omega)$ , through either the radial or the torsional-radial modes.

Figure 13b presents a schematic illustration of the setup for characterization of inter-modal forward Brillouin scattering in the same few-mode fiber 38,51. Light from a laser diode source of 1550 nm wavelength was split into two paths. Light in the upper branch passed through a single-sideband electro-optic modulator, driven by voltage of variable radio frequency  $\Omega$  from the output port of a microwave generator. The optical frequency of the upper branch wave was thereby offset by  $\Omega$ . The light wave was then intensity-modulated in an electro-optic Mach-Zehnder modulator, driven by a voltage of frequency  $f_1 = 200 \, \text{kHz}$  from one output port of a dualchannel lock-in amplifier. The modulated wave was amplified to an average optical power of 0.1 W and launched to the few-mode fiber through one input port of the mode-division multiplexer.

The optical wave at the lower branch was intensity modulated at frequency  $f_2 = 503 \, \mathrm{kHz}$  in a second electro-optic Mach-Zehnder modulator, driven by voltage from a second output port of the lock-in amplifier. The lower branch wave was amplified to 0.5 W average power and launched through the fiber under test through a second, different port of the mode division multiplexer. Intermodal forward Brillouin scattering may lead to the coupling of optical power between the two input waves, depending on their frequency offset  $\Omega$ . Such coupling manifests in intensity modulation of both waves at frequencies  $f_1 \pm f_2$  [38,51].

Light from one of the output ports of the second mode division multiplexer, located at the far end of the fiber under test, was detected using a photo-receiver of 20 GHz bandwidth. The detected voltage was analyzed at the input port of the lock-in amplifier, and the magnitude of the  $f_1+f_2$  frequency component was monitored. That component is proportional to the coupling coefficient of inter-modal forward Brillouin scattering,  $\mathrm{Im}\{\gamma(\Omega)\}$  [38]. The coupling of power may take place through all acoustic modes, radial and torsional-radial alike. Note that the Kerr effect does not induce coupling of optical power between the two fields, and its removal was not required as part of this protocol.

#### Acknowledgements

This research was supported in part by the European Research Council (ERC), through Grant no. 101001069 (SAW-SBS).

#### Data availability

The data that supports the findings of this study are available from the corresponding author upon reasonable request.

### Conflict of interest

All authors declare no conflict of interest.

# Appendix A

# Spatial overlap integrals of electro-strictive stimulation and photoelastic scattering

In this Appendix, we show that the two overlap integrals used in our analysis, that of electro-strictive stimulation and that of photoelastic scattering, are identical. The derivation is detailed in Cartesian coordinates for convenience, but it holds for any choice of coordinates system.

Let us denote the normalized transvers profiles of optical modes 1 and 2 as  $\vec{E}_{T1,2}(x,y)$  [m<sup>-1</sup>], where x and y are the Cartesian coordinates in the transverse plane. Each profile consists of two components:

$$\vec{E}_{T1,2}(x,y) = E_{x1,2}(x,y)\hat{x} + E_{y1,2}(x,y)\hat{y}$$
(A1)

Here  $\hat{x}$  and  $\hat{y}$  denote the unit vectors in the x and y directions, respectively. We define next the tensor  $I_{1,2}$  of cross-products between normalized field components. The elements of this tensor are

$$I_{ii,1,2} = E_{i1}E_{i2} \tag{A2}$$

where i,j may equal x or y. Next, we may express the normalized transverse dependence of the electro-strictive stress tensor as follows<sup>41</sup> (see Eq. (5)):

$$\widetilde{\boldsymbol{\sigma}}_{T1,2} = -n_0^4 \boldsymbol{p}_T : \boldsymbol{I}_{1,2} \tag{A3}$$

Here, the : symbol denotes the tensor product, and  $p_T$  is the transverse sub-set of the fourth-rank photo-elastic tensor p of the silica fiber. The dimensions of  $p_T$  are  $2 \times 2 \times 2 \times 2$ .  $\tilde{\sigma}_T$  is a  $2 \times 2$  tensor, whose elements can be explicitly written as

$$\widetilde{\sigma}_{Tij,1,2} = -n_0^4 \sum_{k,l} p_{T,ijkl} I_{kl,1,2}$$
 (A4)

Here k, l also scan over x or y. The transverse profile of the electro-strictive force per unit volume is given by (see Eq. (6) and Eq. (7)):

$$\vec{f}_{12} = -\nabla \cdot \widetilde{\boldsymbol{\sigma}}_{T12} \tag{A5}$$

$$f_{i,1,2} = -\sum_{i} \frac{\partial}{\partial j} \widetilde{\sigma}_{Tij,1,2} \tag{A6}$$

The normalized profile of material displacement  $[m^{-1}]$  in mode  $TR_{vm}$  can expressed as

$$\vec{u}_{nm}(x,y) = u_{x,nm}(x,y)\hat{x} + u_{y,nm}(x,y)\hat{y} \tag{A7}$$

The spatial overlap integral of electro-strictive stimulation through optical modes 1 and 2 and acoustic mode

 $TR_{nm}$  equals:

$$Q_{1,2,pm}^{(ES)} = \int \int \sum_{i} f_{i,1,2} u_{i,pm} ds$$
 (A8)

where ds is an infinitesimal area element in the transverse plane. We may write

$$\begin{split} &\sum_{i} f_{i,1,2} u_{i,pm} = -\sum_{i} \sum_{j} \frac{\partial}{\partial j} \widetilde{\sigma}_{Tij,1,2} u_{i,pm} \\ &= n_{0}^{4} \sum_{i} \sum_{j} \frac{\partial}{\partial j} \left( \sum_{k,l} p_{T,ijkl} I_{kl,1,2} \right) u_{i,pm} = n_{0}^{4} \sum_{i,j,k,l} p_{T,ijkl} u_{i,pm} \frac{\partial}{\partial j} I_{kl,1,2} \end{split} \tag{A9}$$

Leading to

$$Q_{pm}^{(ES)} = n_0^4 \iiint \left( \sum_{i,j,k,l} p_{T,ijkl} u_{i,pm} \frac{\partial}{\partial j} I_{kl,1,2} \right) ds$$
 (A10)

In Eq. (A9) we assume that the tensor  $p_T$  is constant across the silica fiber, and neglect small scale differences between core and cladding. Expressing the summation over j = x, y explicitly, and moving the summation outside the integral, we obtain

$$Q_{1,2,pm}^{(ES)} = n_0^4 \sum_{i,k,l} \iiint \left( p_{T,ixkl} u_{i,pm} \frac{\partial}{\partial x} I_{kl,1,2} + p_{T,iykl} u_{i,pm} \frac{\partial}{\partial y} I_{kl,1,2} \right) ds$$
(A11)

Next, we address the spatial overlap integral of photoelastic scattering. The normalized strain associated with the material displacement is a  $2 \times 2$  tensor:

$$\mathbf{s}_{pm} = \nabla \vec{u}_{pm} \tag{A12}$$

With elements:

$$s_{ij,pm} = \frac{\partial}{\partial i} u_{i,pm} \tag{A13}$$

Strain leads to photoelastic perturbations in the dielectric tensor of the fiber. The transverse dependence of the perturbations is in the form of a tensor  $\mu_{T,pm}$  [41]:

$$\boldsymbol{\mu}_{T,pm} = -n_0^4 \boldsymbol{p}_T : \boldsymbol{s}_{pm} \tag{A14}$$

$$\mu_{T,ij,pm} = -n_0^4 \sum_{k,l} p_{T,ijkl} s_{kl,pm}$$
 (A15)

The spatial overlap integral of photoelastic scattering between optical modes 1 and 2 through acoustic mode <span id="page-17-0"></span> $TR_{pm}$  is given by (see Eq. (21)):

$$Q_{1,2,pm}^{(PE)} = \int \int \sum_{i,j} \mu_{T,ij,pm} I_{ij,1,2} ds$$
 (A16)

This integrand can be rearranged in the following form

$$\sum_{i,j} \mu_{T,ij,pm} I_{ij,1,2} = -n_0^4 \sum_{i,j} \sum_{k,l} p_{T,ijkl} s_{kl,pm} I_{ij,1,2}$$

$$= -n_0^4 \sum_{i,j,k,l} p_{T,ijkl} I_{ij,1,2} \frac{\partial}{\partial l} u_{k,pm}$$
(A17)

With a change of indices i' = k, j' = l, k' = i, l' = j, we obtain

$$\sum_{i,j} \mu_{T,ij,pm} I_{ij,1,2} = -n_0^4 \sum_{k,l,l,i,j,j} p_{T,k,ll,ij,j} I_{k'l',1,2} \frac{\partial}{\partial j'} u_{l',pm}$$
 (A18)

(The prime superscripts are omitted hereunder). The tensor  $p_T$  is symmetric, hence  $p_{T,klij} = p_{T,ijkl}$ . The photoelastic overlap integral is therefore brought to the following form

$$Q_{1,2,pm}^{(PE)} = -n_0^4 \sum_{i,j,k,l} \iint p_{T,ijkl} I_{kl,1,2} \frac{\partial}{\partial j} u_{i,pm} ds$$
 (A19)

Expressing once again the summation with respect to index j in a direct form, we obtain

$$Q_{1,2,pm}^{(PE)} = -n_0^4 \sum_{i,k,l} \iint \left( p_{T,ixkl} I_{kl,1,2} \frac{\partial}{\partial x} u_{i,pm} + p_{T,iykl} I_{kl,1,2} \frac{\partial}{\partial y} u_{i,pm} \right) ds$$
(A20)

Integration in parts yields:

$$\begin{split} Q_{1,2,pm}^{(PE)} &= n_0^4 \sum_{i,k,l} \int\!\!\int \left( p_{T,ixkl} u_{i,pm} \frac{\partial}{\partial x} I_{kl,1,2} + p_{T,iykl} u_{i,pm} \frac{\partial}{\partial y} I_{kl,1,2} \right) \! ds \\ &- n_0^4 \sum_{i,k,l} \left( \oint_L p_{T,ixkl} u_{i,pm} I_{kl,1,2} dy + \oint_L p_{T,iykl} u_{i,pm} I_{kl,1,2} dx \right) \end{split} \tag{A21}$$

The first two terms in Eq. (A21) equal  $Q_{1,2,\mathrm{pm}}^{(ES)}$  (see Eq. A(11)). The last two terms are integrals carried out over the outer circumference of the cladding cross-section. At the cladding edge,  $I_{kl,1,2}=0$ . These two terms therefore vanish, and we obtain

$$Q_{1.2.pm}^{(PE)} = Q_{1.2.pm}^{(ES)} \tag{A22}$$

Received: 22 November 2024 Revised: 22 April 2025 Accepted: 24 April 2025

Published online: 09 July 2025

#### References

- Shelby, R. M., Levenson, M. D. & Bayer, P. W. Guided acoustic-wave Brillouin scattering. Phys. Rev. B 31, 5244–5252 (1985).
- Biryukov, A. S., Sukharev, M. E. & Dianov, E. M. Excitation of sound waves upon propagation of laser pulses in optical fibres. *Quantum Electron.* 32, 765–775 (2002)
- Russell, P. S. J., Culverhouse, D. & Farahi, F. Experimental observation of forward stimulated Brillouin scattering in dual-mode single-core fibre. *Electron. Lett.* 26, 1195–1196 (1990)
- Russell, P. S. J., Culverhouse, D. & Farahi, F. Theory of forward stimulated Brillouin scattering in dual-mode single-core fibers. *IEEE J. Quantum Electron.* 27, 836–842 (1991).
- Zadok, A. et al. Forward Brillouin Scattering in Standard Optical Fibers (Springer, 2022)
- Ippen, E. P. & Stolen, R. H. Stimulated Brillouin scattering in optical fibers. Appl. Phys. Lett. 21, 539–541 (1972).
- Nikles, M., Thevenaz, L. & Robert, P. A. Brillouin gain spectrum characterization in single-mode optical fibers. J. Lightwave Technol. 15, 1842–1851 (1997).
- Kobyakov, A., Sauer, M. & Chowdhury, D. Stimulated Brillouin scattering in optical fibers. Adv. Opt. Photonics 2, 1–59 (2010).
- Antman, Y. et al. Optomechanical sensing of liquids outside standard fibers using forward stimulated Brillouin scattering. Optica 3, 510–516 (2016).
- Hayashi, N. et al. Experimental study on depolarized GAWBS spectrum for optomechanical sensing of liquids outside standard fibers. Opt. Express 25, 2239–2244 (2017)
- Chow, D. M. et al. Distributed forward Brillouin sensor based on local light phase recovery. Nat. Commun. 9, 2990 (2018).
- Chow, D. M. & Thévenaz, L. Forward Brillouin scattering acoustic impedance sensor using thin polyimide-coated fiber. Opt. Lett. 43, 5467–5470 (2018).
- Bashan, G. et al. Optomechanical time-domain reflectometry. Nat. Commun. 9, 2991 (2018).
- Diamandi, H. H. et al. Distributed opto-mechanical analysis of liquids outside standard fibers coated with polyimide. APL Photonics 4, 016105 (2019).
- Diamandi, H. H. et al. Forward stimulated Brillouin scattering analysis of optical fibers coatings. J. Lightwave Technol. 39, 1800–1807 (2021).
- London, Y. et al. Opto-mechanical fiber sensing of gamma radiation. J. Lightwave Technol. 39, 6637–6645 (2021).
- Sánchez, L. A. et al. High accuracy measurement of Poisson's ratio of optical fibers and its temperature dependence using forward-stimulated Brillouin scattering. Opt. Express 30, 42–52 (2022).
- Sánchez, L. A. et al. Recent advances in forward Brillouin scattering: sensor applications. Sensors 23, 318 (2022).
- Hua, Z. J. et al. Non-destructive and distributed measurement of optical fiber diameter with nanometer resolution based on coherent forward stimulated Brillouin scattering. *Light: Adv. Manuf.* 2, 25 (2021).
- Yang, G. J. et al. Simultaneous sensing of temperature and strain with enhanced performance using forward Brillouin scattering in highly nonlinear fiber. Opt. Lett. 48, 3611–3614 (2023).
- Zeng, K. Y. et al. High-sensitivity acoustic impedance sensing based on forward Brillouin scattering in a highly nonlinear fiber. Opt. Express 31, 8595–8609 (2023)
- Li, T. F. et al. 3-mm recognition capability of forward stimulated Brillouin scattering measurement by Brillouin selective sideband amplification. J. Lightwave Technol. 42, 898–906 (2024).
- Li, T. F. et al. Forward Brillouin scattering for bubble and flow interruption detection toward microscale liquid systems. J. Lightwave Technol. 43, 354–361, https://doi.org/10.1109/JLT.2024.3445167 (2025).
- Sánchez, L. A. et al. Forward Brillouin scattering spectroscopy in optical fibers with whispering-gallery modes. Adv. Optical Mater. 12, 2301629 (2024).
- Yaman, F. et al. Long distance transmission in few-mode fibers. Opt. Express 18, 13250–13257 (2010).
- Kitayama, K. I. & Diamantopoulos, N. P. Few-mode optical fibers: original motivation and recent progress. *IEEE Commun. Mag.* 55, 163–169 (2017).
- Li, A. et al. Few-mode fiber based optical sensors. Opt. Express 23, 1139–1150 (2015).
- Snyder, A. W. & Young, W. R. Modes of optical waveguides. J. Optical Soc. Am. 68, 297–309 (1978).
- 29. Snyder, A. W. & Love, J. D. Optical Waveguide Theory (Springer, 1983).
- Kittlaus, E. A., Otterstrom, N. T. & Rakich, P. T. On-chip inter-modal Brillouin scattering. Nat. Commun. 8, 15819 (2017).
- 31. Otterstrom, N. T. et al. A silicon Brillouin laser. Science 360, 1113–1116 (2018)

- <span id="page-18-0"></span>32. Liu, Y. et al. Circulator-free Brillouin photonic planar circuit. *Laser Photonics Rev.* **15**, 2000481 (2021).
- 33. Xu, W. D. et al. Ultranarrow-linewidth stimulated intermodal forward Brillouin scattering. In: *Proceedings of 2023 Conference on Lasers and Electro-Optics, San Jose, CA, USA* 1–2 (IEEE, 2023).
- Xu, W. D. et al. Strong optomechanical interactions with long-lived fundamental acoustic waves. Optica 10, 206–213 (2023).
- 35. Li, S. P., Li, M. J. & Vodhanel, R. S. All-optical Brillouin dynamic grating generation in few-mode optical fiber. *Opt. Lett.* **37**, 4660–4662 (2012).
- 36. Song, K. Y., Kim, Y. H. & Kim, B. Y. Intermodal stimulated Brillouin scattering in two-mode fibers. *Opt. Lett.* **38**, 1805–1807 (2013).
- Catalano, E. et al. Distributed modal birefringence measurement in a fewmode fiber based on stimulated Brillouin scattering. J. Lightwave Technol. 42, 2473–2479 (2024).
- Bashan, G. et al. Forward stimulated Brillouin scattering and opto-mechanical non-reciprocity in standard polarization maintaining fibres. *Light Sci. Appl.* 10, 119 (2021).
- Diamandi, H. H. et al. Interpolarization forward stimulated Brillouin scattering in standard single-mode fibers. Laser Photonics Rev. 16, 2100337 (2022).
- 40. Zeng, X. L. et al. Stimulated Brillouin scattering in chiral photonic crystal fiber. *Photonics Res.* **10**, 711–718 (2022).

- Qiu, W. J. et al. Stimulated Brillouin scattering in nanoscale silicon step-index waveguides: a general framework of selection rules and calculating SBS gain. Opt. Express 21, 31402–31419 (2013).
- Sittig, E. Zur Systematik der elastischen Eigenschwingungen isotroper Kreiszvlinder. Acta Acust. U. Acust. 7, 175–180 (1957).
- 43. Auld, A. B. Acoustic Fields and Waves in Solids. (Wiley and Sons, 1973).
- 44. Bernstein, A. et al. Tensor characteristics of forward Brillouin sensors in bare and coated fibers. *APL Photonics* **8**, 126105 (2023).
- Butsch, A. et al. Optomechanical nonlinearity in dual-nanoweb structure suspended inside capillary fiber. Phys. Rev. Lett. 109, 183904 (2012).
- Wang, J. et al. FSBS resonances observed in a standard highly nonlinear fiber. Opt. Express 19, 5339–5349 (2011).
- 47. Cheng, H. T. et al. A terahertz bandwidth non-magnetic isolator. *Nat. Photon.* **19**, 533–539 (2025).
- 48. Bashan, G. et al. A forward Brillouin fibre laser. Nat. Commun. 13, 3554 (2022).
- Kang, M. S. et al. Tightly trapped acoustic phonons in photonic crystal fibres as highly nonlinear artificial Raman oscillators. Nat. Phys. 5, 276–280 (2009).
- London, Y. et al. Distributed analysis of nonlinear wave mixing in fiber due to forward Brillouin scattering and Kerr effects. APL Photonics 3, 110804 (2018).
- 51. Zarifi, A. et al. Highly localized distributed Brillouin scattering response in a photonic integrated circuit. *APL Photonics* **3**, 036101 (2018).
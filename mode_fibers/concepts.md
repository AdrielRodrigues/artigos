# Key Concepts

Reference notes synthesizing the core concepts needed to read this collection of papers on space-division multiplexing, few-mode fibers, coherent PON, elastic optical networks, and 5G-oriented optical transport.

## The Capacity Crunch and Why New Multiplexing Dimensions Are Needed

Single-mode fiber (SMF) capacity, boosted for decades by optical amplification, WDM, coherent detection, and polarization multiplexing, is approaching its nonlinear Shannon limit. Traffic growth (5G/6G, video, cloud, data-center interconnect) keeps outpacing this limit, motivating a new physical dimension for scaling: space. This is the shared motivation behind SDM, few-mode fibers, and multi-band transmission covered throughout the collection.

## Space-Division Multiplexing (SDM)

SDM increases fiber capacity by exploiting parallel spatial paths instead of only wavelength or spectral efficiency. A spatial path can be a separate fiber (multi-fiber cable), a core within a multi-core fiber (MCF), or a mode/mode-group within a multi-mode or few-mode fiber (MMF/FMF). SDM adds a new "space" resource dimension to network resource-allocation problems, alongside routing and spectrum, at the cost of extra crosstalk and switching complexity.

## Multi-Core Fibers (MCF) and Inter-Core Crosstalk

MCFs place several independent cores inside one standard-diameter cladding. Their main impairment is inter-core crosstalk (XT): signal power leaks between neighboring cores, especially when they carry overlapping spectrum. XT grows with core proximity, bend radius, and transmission length, and is typically modeled with coupled-power equations depending on the coupling coefficient, propagation constant, and core pitch. Trench-assisted designs, larger core spacing, and counter-propagating adjacent cores reduce it. XT imposes a threshold that each modulation format must respect, directly linking spatial design to reach and modulation choice.

## Few-Mode Fibers (FMF) and Mode-Division Multiplexing (MDM)

FMFs guide a small number of spatial modes (a few to over a hundred) in a single core, each usable as an independent (or grouped) data channel — this is MDM. Unlike bulky multi-core fibers, FMFs keep the standard 125 µm cladding diameter, so they are mechanically reliable and manufacturable with conventional processes. Modes are commonly described by their LP (linearly polarized) designation (LP01, LP11a/b, LP21a/b, etc.). The central design trade-off is between crosstalk (favoring fewer, well-separated modes) and DSP complexity (favoring smaller MIMO sizes).

## Weakly-Coupled vs. Full-MIMO (Strongly-Coupled) FMF Regimes

Two design philosophies exist for handling modal crosstalk. The weakly-coupled approach uses step-index-core fibers engineered to keep coupling between (groups of) modes very low, so that each channel can be detected with little or no MIMO processing — well suited to short-reach, low-cost links. The full-MIMO (strongly-coupled) approach instead uses trench-assisted graded-index-core fibers designed to minimize differential mode-group delay (DMGD) so that all modes mix but can be jointly recovered by a large coherent MIMO equalizer, enabling long-haul, high-spectral-efficiency transmission at the cost of DSP complexity that scales roughly with the square of the number of modes.

## Mode-Group Division Multiplexing (MGDM)

MGDM is a practical middle ground: modes with similar propagation constants are bundled into "mode-groups." Intra-group modes couple strongly and must be jointly detected, but inter-group coupling is weak, so different mode-groups can be independently routed, switched, added/dropped, and detected with reduced- or zero-MIMO complexity. This makes mode-groups behave like independent spatial super-channels in a network, which is the basis for mode-group-aware routing and resource-allocation algorithms (RMMWA).

## Mode Coupling, DMGD, and Mode-Dependent Loss (MDL)

Three linear impairments dominate FMF/MDM system design. Differential mode-group delay (DMGD) is the difference in propagation time between modes/mode-groups; it dictates how long (in taps) the receiver-side MIMO filter must be, since the digital equalizer must span the accumulated temporal spread. Mode-dependent loss (MDL) is uneven attenuation/gain across modes (from multiplexers, amplifiers, splices) that breaks the orthogonality MIMO relies on and fundamentally limits channel capacity. Intermodal crosstalk (IM-XT) is power leakage between modes during propagation. Techniques to manage these include DMGD-compensated links (concatenating fiber spans with opposite-sign DMGD), cyclic mode permutation, ring-core amplifiers to reduce differential gain, and digital interference cancellation.

## MIMO Digital Signal Processing for MDM

Full-MIMO MDM reception requires a complex-valued 2N×2N adaptive equalizer for N spatial modes (2x for two polarizations), so hardware cost grows quadratically with mode count. Weakly-coupled/MGDM systems instead need only small (e.g., 2x2 or 4x4) "partial MIMO" blocks per mode-group. Real-time implementations must address ADC-to-DSP clock-rate mismatch (via parallelization, incurring pipelined delay), training vs. blind adaptive algorithms (blind algorithms like CMA suffer a "singularity problem" that worsens with mode count), and carrier-phase recovery shared across polarizations/modes to save complexity.

## Mode/Space Multiplexers and Demultiplexers

Coupling light into and out of specific spatial modes requires mode (de)multiplexers. Multi-plane light conversion (MPLC) is a widely used technique: it applies a succession of phase transforms via reflections off phase plates to implement any unitary spatial transform losslessly (in principle), and scales to very large mode counts (over 1000). Photonic lanterns are an alternative, preferred for lower mode counts due to lower insertion loss.

## Coherent Detection Fundamentals

Coherent detection mixes ("beats") the received optical signal with a local oscillator (LO) laser before photodetection, enabling linear (not just intensity) recovery of the optical field's amplitude, phase, and polarization. This gives: (1) much better receiver sensitivity than direct detection, since the LO acts as an optical pre-amplifier; (2) the ability to use multi-level, multi-dimensional modulation (QAM formats, polarization multiplexing) for higher spectral efficiency; (3) full digital compensation of linear impairments (chromatic dispersion, polarization mode dispersion) in DSP, since square-law direct detection instead converts linear impairments into hard-to-compensate nonlinear distortion; and (4) inherent frequency selectivity (channel selection by tuning the LO wavelength, without optical filters).

## Modulation Formats and Constellation Shaping

Common formats, in increasing spectral efficiency but decreasing robustness/reach, are BPSK, QPSK, 8-QAM, 16-QAM, up to 64-QAM, often combined with polarization-division multiplexing (PDM/DP) to double throughput. Distance-adaptive modulation selects the most spectrally efficient format that still meets the reach/SNR/crosstalk requirement of a given route — shorter or higher-quality links get higher-order QAM, long links fall back to more robust formats like QPSK or BPSK. Probabilistic constellation shaping (PCS) reshapes the symbol distribution to approach the Shannon capacity limit (a theoretical gain of ~1.53 dB), enabling continuous, fine-grained rate adaptation and extended reach compared with fixed uniform QAM.

## Passive Optical Network (PON) Architecture

A PON is a point-to-multipoint (P2MP) access architecture: an optical line terminal (OLT) at the operator's central office connects to many optical network units (ONUs) at subscribers through a passive optical distribution network (ODN) — fiber plus passive splitters, with no active elements or amplification in between. Downstream traffic is broadcast continuously to all ONUs; upstream traffic arrives burst-by-burst from different ONUs sharing the same fiber via time-division multiple access (TDMA), each burst with potentially different power, phase, and polarization. Standard bodies (ITU-T/FSAN for GPON/XGS-PON/50G-PON, IEEE 802.3 for EPON/NG-EPON) have driven per-wavelength speeds from hundreds of Mb/s to the current 25/50 Gb/s.

## Coherent PON: Motivation and Challenges

Beyond ~50 Gb/s per wavelength, conventional intensity-modulation/direct-detection (IM/DD) PON cannot meet the required loss/power budget (a PON must tolerate ~29-35 dB of splitter and fiber loss). Coherent detection extends the power budget by 10-20+ dB via LO gain, enabling higher split ratios, longer reach, and higher per-wavelength rates using advanced modulation. The two central engineering challenges are: (1) cost/complexity/power — long-haul-grade coherent transceivers (narrow-linewidth lasers, full polarization/phase-diversity receivers with many ADCs) must be radically simplified for cost-sensitive ONUs (e.g., heterodyne detection to halve components, single-polarization receivers, cheaper DFB lasers, reduced-tap DSP); and (2) upstream burst-mode coherent detection — the OLT receiver must rapidly adapt (fast automatic gain control, short preambles, quick equalizer convergence) to bursts from different ONUs with varying power, frequency offset, and polarization, unlike the continuous-mode operation coherent DSP was originally designed for.

## Rate-Adaptive and Flexible-Multiplexing Access

Because different ONUs experience different channel quality but legacy PON gives everyone the same peak rate, rate-adaptive schemes (adaptive FEC, hybrid modulation, probabilistic shaping) let each ONU's throughput track its actual channel capacity. Coherent detection's extra degrees of freedom (amplitude, phase, two polarizations) also enable multiplexing beyond simple TDM: frequency-division multiplexing/multiple access (FDM/FDMA) via digital subcarrier multiplexing, hybrid time-and-frequency-division multiplexing (TFDM), and even WDM-PON, all detectable with a single coherent receiver/LO by digital channel selection.

## Elastic Optical Networks (EON) and Flex-Grid

EONs replace the rigid, fixed-width wavelength grid of traditional WDM with a flexible ("flex-grid") spectrum divided into narrow frequency slots (FSs, e.g., 12.5 GHz), which can be grouped adaptively to fit each connection's bandwidth demand. Combined with distance-adaptive modulation, this lets the network allocate just enough spectrum for the required bitrate and reach, improving spectral efficiency versus fixed-grid WDM. The dynamic, elastic allocation of resources introduces new problems: spectrum fragmentation (small, unusable leftover slot gaps) and the need for spectrum continuity/contiguity constraints in path establishment.

## Routing and Spectrum Assignment (RSA / RMLSA)

In EONs, establishing a connection means jointly deciding a route and a spectrum allocation obeying continuity (same slot indices) and contiguity (adjacent slots) constraints — the RSA problem. Adding distance-adaptive modulation choice turns it into Routing, Modulation Level, and Spectrum Assignment (RMLSA/RMSA). Guard bands (extra reserved slots) separate adjacent connections to prevent interference. This is the foundational assignment problem that SDM, multi-band, and few-mode extensions all generalize.

## Generalized Assignment Problems: RSCA / RSCBA / RMSA / RMMWA

Adding spatial and/or band dimensions multiplies the resource-allocation problem: with multi-core fibers it becomes Routing, Spectrum, and Core Assignment (RSCA) or, with modulation, RMLSSA; adding multiple transmission bands (see below) yields Routing, Spectrum, Core, and Band Assignment (RSCBA); and for mode-group/few-mode systems it becomes Routing, Modulation, Mode-Group, and Wavelength Allocation (RMMWA). All variants share the same skeleton — pick a route, then jointly pick modulation format and spatial/band resource, then assign spectrum/wavelength — while adding dimension-specific physical constraints (core continuity to allow simple ROADMs without "lane changes," modal-spectral exclusivity so no two connections share the same wavelength+mode-group on a link, crosstalk thresholds, per-band SNR limits, etc.).

## Fixed vs. Demand-Aware (Adaptive) Resource Allocation Strategies

Algorithms for mode-group/modulation-format (or generally spatial+format) assignment fall into two philosophies. Fixed strategies precompute one static priority order of resource-configuration pairs offline (e.g., sorted by reach or by capacity) and apply it identically to every request via first-fit. Demand-aware (adaptive) strategies instead build a request-specific priority list online, tailored to that connection's bitrate and route length. A key inefficiency, multidimensional overprovisioning, arises because each mode-group/modulation pair offers a fixed, discrete (reach, capacity) combination: a request may be forced into a configuration with more reach or capacity than it needs, wasting resources. The perfect-fit philosophy (e.g., the BANG algorithm) tries to match capacity exactly, which minimizes capacity waste but can raise blocking when no exact match is reach-feasible. Slack-aware demand-driven algorithms (e.g., DA-MMA) instead rank feasible configurations by a weighted combination of normalized excess capacity and excess reach ("slack"), balancing both forms of waste. Which philosophy performs best is topology-dependent: capacity-driven prioritization wins in capacity-abundant, reach-unconstrained networks; balanced slack-aware/demand-aware approaches win when both capacity and reach are simultaneously scarce; and when reach is the dominant bottleneck, all strategies converge to similar performance because physical feasibility (not resource-allocation cleverness) becomes the limiting factor.

## Multipath Routing and Spectrum Fragmentation

When no single spatial channel (core/mode) has enough contiguous free spectrum for a request, multipath routing splits the demand across several "sublightpaths," ideally reusing the same physical route but different cores/modes to avoid differential delay between sub-flows. This mitigates spectrum fragmentation-driven blocking but increases the number of transponders needed (and thus energy consumption) and can reintroduce differential delay if paths genuinely diverge. Algorithms trade off blocking probability against energy consumption, number of sublightpaths, and delay.

## Multi-Band Transmission and Stimulated Raman Scattering (SRS)

Multi-band (MB) transmission extends usage beyond the conventional C-band (1530-1565 nm) into adjacent bands — L, S, E, and O — on already-deployed standard single-mode fiber, without needing new fiber but requiring new transceivers/amplifiers/ROADMs. As transmission spans a wider spectrum approaching ~13 THz, inter-channel stimulated Raman scattering (SRS) becomes significant: it transfers power from higher-frequency to lower-frequency channels, tilting the gain/loss profile and modifying noise and nonlinear-interference generation across bands. SRS must therefore be included in SNR/QoT models for multi-band systems (it is negligible in C-band-only systems). Combining MB with SDM (MB-SDM) maximizes throughput but compounds the resource-allocation problem into RSCBA and requires joint SNR analysis across bands.

## Quality of Transmission (QoT): SNR, ASE, and Nonlinear Interference

Optical signal quality is commonly estimated via the (generalized) signal-to-noise ratio, combining amplified spontaneous emission (ASE) noise from optical amplifiers and nonlinear interference (NLI) from fiber Kerr effects (self-channel and cross-channel interference, SCI/XCI). A connection is only admitted if its end-to-end SNR (and, where relevant, accumulated crosstalk) stays above/below threshold. QoT estimation becomes route-, modulation-, and now band-/mode-dependent, which is why RSA/RSCA/RSCBA algorithms must embed physical-layer models rather than treating "distance" as the only constraint.

## Forward Error Correction (FEC) and the Shannon Limit

FEC adds redundancy so that a much higher pre-FEC bit-error rate can still be corrected to error-free operation, at the cost of some rate overhead. Modern high-performance codes (staircase, LDPC-based) approach within roughly 1-1.5 dB of the Shannon limit for a given modulation format. Combined with probabilistic constellation shaping, coding can push real systems very close to the fundamental channel capacity, enabling higher data rates or longer reach for the same optical signal-to-noise ratio.

## Network Survivability and Protection

Because a single fiber/link failure can disrupt many high-capacity multiplexed connections at once, survivable resource allocation reserves backup resources. Dedicated backup path protection (DBPP, "hot" backup — active in parallel, fast recovery, costly) contrasts with shared backup path protection (SBPP, "cold" backup — reserved but inactive until failure, cheaper but slower). In multi-band SDM-EONs, a band-partition protection scheme can place working traffic in the higher-quality band (e.g., C-band) and reserve protection capacity in a lower-quality band (e.g., L-band), improving normal-operation SNR while still guaranteeing recovery. Working and backup paths must be link-disjoint; problems are typically formulated as integer linear programs (exact but not scalable) with heuristics (e.g., genetic algorithms) for large networks.

## Energy Efficiency in SDM-EONs

Because each sublightpath needs its own bandwidth-variable transponder (BVT), splitting a demand across many paths/cores raises energy consumption per transmitted bit. Energy-aware algorithms therefore try to minimize the number of sublightpaths and prefer single-path, single-core allocation whenever feasible, only invoking multipath as a fallback, and factor per-bit energy models into path/modulation selection alongside blocking probability.

## 5G/6G X-Haul: Fronthaul, Midhaul, Backhaul

A cloud radio access network (C-RAN) splits base-station functionality across remote units (RUs), distributed units (DUs), and centralized units (CUs), connected respectively by fronthaul, midhaul, and backhaul links — collectively "X-haul." Each segment has different distance (roughly 10 km, 40 km, 80 km typical), bit-rate, and latency requirements (from ~100 µs for CPRI-like fronthaul to seconds for massive-machine-type traffic), which drives the choice of optical technology per segment: WDM-PON or CWDM/LAN-WDM for cost-effective fronthaul aggregation, PAM4 or entry-level coherent for midhaul, and high-capacity coherent DWDM for backhaul and 5G-core interconnection.

## Radio-over-Fiber (RoF) for Fronthaul

RoF transports radio waveforms optically instead of pre-processed digital baseband. Analog RoF (A-RoF) is spectrally efficient but limited by transceiver noise/ENOB; digital RoF (D-RoF, e.g., CPRI) is more robust but rate-hungry. Hybrid digital-analog RoF (DA-RoF) combines probabilistically-shaped QAM with pulse-code modulation of the residual error, trading spectral efficiency for a large SNR gain, letting fronthaul links support high-order modulation formats (e.g., 1024-QAM) required by advanced 5G radios without the cost of full digital FEC-based transmission.

## Low-Latency PON for Mobile X-Haul

To let TDM-PON carry latency-sensitive 5G traffic, techniques such as cooperative dynamic bandwidth allocation (CoDBA, sharing RAN and PON scheduling in advance to skip negotiation delay), accelerated DBA (multiple upstream bursts per ONU per 125 µs frame instead of one), and a dedicated activation wavelength (to skip the ranging procedure during coexistence with legacy PON) reduce end-to-end latency to levels compatible with 5G fronthaul/midhaul requirements.

## Optical Transport Network (OTN) and Network Slicing

OTN aggregates and switches client services using optical data units (ODUs). Traditional OTN's minimum granularity (~1.24 Gb/s) is wasteful for the many sub-Gb/s 5G services; service-oriented OTN introduces a flexible optical service unit (OSUflex) with ~2 Mb/s granularity, enabling many more services per wavelength, faster switching (via sequential forwarding), and bandwidth-guaranteed ("hard") network slicing — dedicated, isolated bandwidth per service or tenant, essential for 5G's differentiated QoS requirements.

## Fifth-Generation Fixed Network (F5G) Vision

F5G is the fixed-network counterpart to 5G mobile evolution, envisioning "fiber to everywhere": enhanced fixed broadband (eFBB), guaranteed reliable experience (GRE), and full fiber connection (FFC), later extended with energy-efficient broadband communication (EEBC, e.g., passive optical LANs), real-time broadband communication (RTBC, for latency-critical industrial applications), and harmonized communication and sensing (HCS) — using the fiber infrastructure itself (via distributed acoustic sensing or polarization/phase monitoring of live traffic) to also detect vibrations, intrusions, or even seismic events.

## Free-Space Optical (FSO) Multiplexing and Orbital Angular Momentum (OAM)

Beyond guided-fiber systems, the same multiplexing principles (WDM and mode-division multiplexing) apply to free-space optical links. Here, "modes" are realized as orbital-angular-momentum (OAM) beams — beams with a helical phase front characterized by an integer OAM order — generated and separated using spiral phase plates or metasurfaces. Combining WDM and OAM-based MDM multiplies FSO capacity the same way fiber-based SDM does, though practical deployment must additionally contend with atmospheric attenuation, turbulence-induced modal crosstalk, beam divergence, and receiver-aperture/pointing-error losses that have no analog in guided fiber systems.

## Wavelength Conversion for Reaching Non-Standard Bands

To operate at wavelengths without mature transceivers (e.g., mid-infrared for FSO, where atmospheric absorption is lower than in the C-band), signals can be generated and detected using mature C-band coherent equipment and then shifted via nonlinear wavelength conversion (difference-frequency generation in periodically-poled lithium niobate waveguides) to and from the target band. This lets a system inherit C-band modulation/detection maturity while transmitting in a band chosen for its propagation properties, at the cost of conversion-efficiency and added-noise penalties.

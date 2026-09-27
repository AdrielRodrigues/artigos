---
index_terms:
  - Elastic Optical Networks
  - Space Division Multiplexing
  - Multi-Core Fiber
  - Inter-core Crosstalk
  - RMSCA problem
  - Spectrum Fragmentation
---

# A survey on challenges of Spatial Division Multiplexing enabled elastic optical networks

## 1. Introduction
Elastic Optical Networks (EON) address growing bandwidth demands by utilizing a flexible grid where the spectrum is divided into 12.5 GHz slots, which can be grouped to create channels with varying capacities. The traditional resource allocation problem in EON is known as Routing, Modulation Level and Spectrum Allocation (RMLSA). To further increase capacity, Spatial Division Multiplexing (SDM) via Multi-Core Fibers (MCF) is introduced, adding a "core choice" dimension to the problem, now termed Routing, Modulation, Spectrum and Core Allocation (RMSCA). 

The primary physical impairment in MCF is crosstalk—interference between adjacent cores. This paper surveys SDM-EON literature, focusing on the classification of crosstalk evaluation models and the performance of RMSCA algorithms. Its specific contributions include estimating crosstalk thresholds for various modulation levels and analyzing how different allocation strategies impact circuit blocking ratios.

## 2. Spatial Division Multiplexing in elastic optical networks
SDM increases transmission capacity by utilizing multiple spatial channels within a single fiber structure. While technologies like multi-mode fibers or fiber bundles exist, this survey focuses on MCF. In MCF, the arrangement of cores significantly impacts crosstalk:
* **7-core fibers:** Hexagonal array; the central core is most vulnerable as it has six neighbors, whereas peripheral cores have only three.
* **12-core fibers:** Ring-like arrangement; all cores have two neighbors, resulting in uniform average crosstalk.
* **19-core fibers:** High density and higher crosstalk incidence, typically limited to shorter distances ($\approx 10$ km).

To mitigate power leakage between cores, "trench-assisted" MCFs are used, which can reduce crosstalk by approximately 20 dB compared to standard MCFs. Key physical parameters influencing performance include core pitch (distance between cores), cladding diameter, and coating thickness.

## 3. Support equipment for SDM-EON
The feasibility of SDM-EON depends on the ability to perform Spatial Lane Changes (SLC)—switching circuits between different cores at network nodes. A proposed SDM-ROADM architecture involves:
1. **SDM Demultiplexer:** Separates spatial channels into individual Single-Core Fibers (SCF).
2. **Wavelength-Selective Switches (WSS):** Performs fine-grained switching to redirect circuits.
3. **Second WSS and SDM Multiplexer:** Re-combines the SCFs into an output MCF, potentially shifting the circuit to a different core.

Equipment such as photonic-lantern multiplexers (PLM) can facilitate the transition between SCF bundles and MCFs. The authors note that precise architectural definitions and detailed financial or energy cost analyses for these components are currently lacking in the literature.

## 4. Crosstalk
Crosstalk occurs due to power leakage at Phase-Matching Points (PMP), influenced by fiber curvature and torsion. It is modeled as a statistical value based on coupling coefficients, bending radius, core pitch, and fiber length. If crosstalk exceeds a specific threshold, the signal becomes noise, rendering the circuit unusable.

### 4.1. Calculating crosstalk thresholds
The authors conducted simulations using the ONS simulator to establish a relationship between modulation levels (from BPSK to 64QAM) and their corresponding crosstalk thresholds based on transmission reach. They found that existing literature often overestimates these thresholds. Their findings indicate that higher-order modulations (e.g., 64QAM), which have shorter reaches, require much stricter (lower) crosstalk thresholds ($\approx -37.81$ dB) compared to BPSK ($\approx -22.75$ dB).

### 4.2. Defining interference among neighbors
Crosstalk calculation depends on the number of active neighboring cores ($n$). The survey identifies two modeling approaches:
* **Static N:** Assumes worst-case scenarios (e.g., $n=6$ for central cores), simplifying evaluation but potentially overestimating interference.
* **Dynamic N:** Counts only neighbors with active circuits in the same slot index, providing a precise estimation.

Simulation results on a USA topology show that using a dynamic $n$ without reassessing existing circuits leads to the lowest blocking ratio. Conversely, Dynamic $N$ with crosstalk reassessment performs worst because newly established circuits may push previously allocated high-efficiency modulations above their strict crosstalk thresholds, causing them to be blocked.

## 5. RMSCA problem
The RMSCA process involves selecting a route $\rightarrow$ choosing a modulation level (based on distance) $\rightarrow$ allocating contiguous slots in the spectrum $\rightarrow$ selecting an appropriate core. Two primary constraints are:
* **Continuity:** The same slot range must be available across all links in a route.
* **Contiguity:** Allocated slots for a single circuit must be adjacent.

Failure to manage these leads to "spectral fragmentation," where small gaps of free slots become unusable, increasing the blocking ratio.

### 5.1. RMSCA: literature review
The authors categorize various RMSCA strategies designed to combat fragmentation and crosstalk:
* **Priority-based allocation:** Some algorithms reserve specific slot ranges for specific bandwidths or prioritize certain cores for high-capacity requests.
* **Traffic Scenarios:** Most research focuses on dynamic traffic (unknown future requests) rather than static traffic matrices.
* **Protection Schemes:** Several papers propose failure-independent path protecting (FIPP) and p-cycle algorithms to ensure survivability in SDM-EON.
* **Defragmentation:** Techniques like "push-pull" mechanisms allow circuits to be reallocated without shutdown to consolidate free spectrum.

A comprehensive classification reveals that the majority of researchers ignore core continuity constraints (allowing core switching), and only about 30% of proposals are explicitly crosstalk-aware.

### 5.2. Performance evaluation
The authors compare three allocation algorithms on a USA topology: **FF-CASC** (First-Fit with a Spectrum Compactness metric), **RF-CASC** (Random Fit with CASC), and **Intra-Area** (bandwidth-based priority areas).

Findings include:
* **FF-CASC:** Achieves the lowest blocking ratio and bandwidth blocking ratio. Its sequential allocation and compactness metric maintain high spectral organization.
* **Intra-Area:** Performs poorly when there is a wide variation in requested bandwidths, as the spectrum becomes over-partitioned into too many small areas.
* **RF-CASC:** Causes the highest external fragmentation due to random placement, making it difficult to allocate larger contiguous bandwidth blocks as network load increases.

## 6. Conclusions and challenges
While MCF provides significantly more resources than SCF, several open research challenges remain:
1. **Hardware Realization:** Current SDM-ROADM architectures are largely hypothetical; real-world equipment for efficient core switching is needed.
2. **Crosstalk Mitigation:** Development of fibers with higher immunity to crosstalk (like Trench-Assisted MCF) and a better understanding of the impact of $n$ values in mathematical models.
3. **Economic Viability:** Reducing the cost of SDM components so that an $n$-core MCF is financially competitive with $n$ separate SCFs.
4. **Algorithm Benchmarking:** There is a lack of direct comparisons between proposed RMSCA solutions; most are only compared against basic First-Fit/Dijkstra baselines.
5. **Traffic Diversity:** Future work should explore the impact of diverse traffic profiles and other physical layer impairments beyond crosstalk.
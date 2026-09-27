---
index_terms:
  - space division multiplexing
  - elastic optical networks
  - multi-core fibers
  - multipath routing
  - energy efficiency
  - inter-core crosstalk
  - RMLSSA algorithm
---

# Energy efficient multipath routing in space division multiplexed elastic optical networks

## Abstract
The paper presents a dynamic multipath routing, modulation level, spatial and spectrum assignment algorithm for Space Division Multiplexing (SDM) enabled Elastic Optical Networks (EONs). The primary objective is to minimize blocking probability and energy consumption of bandwidth variable transponders (BVTs). To prevent differential delay, the proposed multipath strategy splits demands into sublightpaths that use different fiber cores but share the same set of fibers. The approach maintains spectrum and core continuity constraints to support cost-effective ROADMs without lane changes. Additionally, it incorporates inter-core crosstalk (XT) awareness to ensure signal quality across various modulation formats.

## 1. Introduction
As bandwidth demand grows, Elastic Optical Networks (EONs) utilizing Orthogonal Frequency Division Multiplexing (OFDM) offer flexibility through adaptive spectrum reservation and modulation. However, EONs face the Route, Modulation Level, and Spectrum Assignment (RMLSA) problem and suffer from spectrum fragmentation. While multipath routing can mitigate fragmentation by splitting bandwidth into sub-flows, standard single-mode fibers have reached their capacity limit. 

Space Division Multiplexing (SDM), specifically using Multi-Core Fibers (MCFs), provides an additional spatial dimension to increase capacity. However, this introduces complexity in resource allocation—the RMLSSA problem—and the physical impairment of inter-core crosstalk (XT). The authors propose a novel energy-efficient and XT-aware multipath routing algorithm that avoids differential delay by restricting sublightpaths to a single route across different cores.

## 2. Related works
The authors review existing SDM-EON heuristics, noting that some fragmentation-aware methods are restricted to specific MCF structures (e.g., central core) or increase resource usage through excessive sub-demands. Other survivable multipath algorithms improve blocking rates but introduce differential delay by routing flows over different physical paths. The paper specifically compares its proposal against the Multipath Inscribed Rectangles Algorithm Minimal Crosstalk (MPIRAXT/MPIRA), which uses image processing techniques to reduce complexity but can increase energy consumption and delay due to its path selection strategy.

## 3. Network model, definitions and assumptions
The network is modeled as a connected graph $\mathcal{S}=(\mathcal{N},\mathcal{E})$ with bidirectional links consisting of MCFs. Each fiber has $C$ cores and $F$ frequency slots (FS) per core.
- **Modulation Formats:** BPSK, QPSK, 8QAM, and 16QAM are used. The choice depends on the transmission reach; shorter paths use more spectrally efficient formats (reducing required FS), while longer paths require more robust formats like BPSK.
- **Constraints:** The model assumes spectrum continuity, spectrum contiguity, a one-slot guard-band to prevent interference, and core continuity to minimize ROADM complexity.
- **Inter-core Crosstalk (XT):** XT is modeled based on the number of neighbor cores sharing frequency slots and the transmission length. The accumulated XT must remain below specific thresholds defined by the selected modulation format to ensure Quality of Transmission (QoT).

## 4. Dynamic energy efficient multipath routing, modulation level, core, and spectrum assignment algorithm (EEMPR)
The EEMPR algorithm operates on precomputed $K$-shortest paths for each source-destination pair. For a request $R(s, d, \gamma, \tau)$:
1. **Path Selection:** It evaluates the shortest path first and selects the most efficient modulation format based on distance.
2. **Resource Search:** It checks spectral availability across all links of the route for each core (from 1 to $C$) and slot (from 1 to $F$).
3. **Allocation Strategy:** A Best-Fit strategy is employed. The algorithm first seeks a single contiguous block of FS in one core that exactly matches the demand while satisfying XT requirements. If no exact match exists, it seeks the smallest larger block.
4. **Multipath Split:** If a single lightpath cannot be established, EEMPR splits the demand into sublightpaths across different cores *of the same route*. It repeatedly assigns the largest available gaps until the demand is met or resources are exhausted.
5. **Fallback:** If the shortest path fails, the algorithm proceeds to the next of the $K$-shortest paths.

**Complexity Analysis:** 
- **Time Complexity:** $O(KC^3F^3E)$ in the worst case, driven by the iterative search and XT computations across $K$ paths.
- **Space Complexity:** $O(KEN^2 + FCE)$, required to store shortest paths and spectral availability states.

## 5. Simulation setup and results
The algorithm was tested using a Python simulator on several topologies: NSFNET, SmallNet, USNet (long links), and JPN12, DT (short links). Each fiber contains seven cores in a hexagonal structure with 320 frequency slots of 12.5 GHz.

### 5.1 Analysis for different numbers of K-shortest paths
Testing $K=1, 3, 5, 7$ showed a trade-off: increasing $K$ reduces the Request Blocking Ratio (RBR) but increases energy consumption and delay. The authors found no significant improvement in blocking probability when moving from $K=5$ to $K=7$, thus using $K=5$ for detailed comparisons.

### 5.2 Comparison of EEMPR and MPIRA for K = 5 shortest paths
Using the NSFNET topology, EEMPR outperformed MPIRA across all metrics:
- **Blocking:** Lower RBR and Bandwidth Blocking Ratio (BBR), reducing blocking by up to 50% at high traffic loads.
- **Energy:** Lower energy consumption per bit because it utilizes fewer total transponders by limiting sublightpaths to a single route.
- **Sublightpaths:** A significant reduction in the average number of sublightpaths generated per demand, which saves spectral resources (fewer guard-bands).
- **Delay:** EEMPR eliminates differential delay and maintains an average delay closer to the shortest path.

### 5.3 Analysis for other topologies
The performance varies based on link distance:
- **Long Link Networks (SmallNet, NSFNet, USNet):** EEMPR significantly outperforms MPIRA. In these networks, BPSK is frequently required, increasing bandwidth demand. EEMPR's flexible allocation manages these larger demands more efficiently than MPIRA's "rectangle" constraints.
- **Short Link Networks (JPN12, DT):** Performance is similar between the two algorithms because high-order modulations (16QAM, 8QAM) are viable, resulting in smaller bandwidth requirements that both algorithms can handle easily.

## 6. Conclusion
The proposed EEMPR algorithm effectively reduces blocking ratios and energy consumption while eliminating differential delay. By combining distance-adaptive modulation with XT-aware multipath routing limited to a single physical route, the method optimizes resource use. The findings highlight that EEMPR is particularly advantageous for continental or intercontinental networks where long link distances necessitate robust but bandwidth-heavy modulation formats.
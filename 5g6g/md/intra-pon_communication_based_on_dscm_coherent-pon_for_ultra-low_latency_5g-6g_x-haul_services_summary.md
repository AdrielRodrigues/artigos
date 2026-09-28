---
index_terms:
  - Coherent PON
  - Digital Subcarrier Multiplexing
  - X-haul services
  - ONU-to-ONU communication
  - ultra-low latency
  - optical distribution network
---

# Intra-PON communication based on DSCM coherent-PON for ultra-low latency 5G/6G X-haul services

## 1. Introduction
The authors address the demand for high bitrates and extremely low latency in future (B5G/6G) X-haul networks. While Very High Speed PON (VHSP) initiatives explore coherent transmission and digital subcarrier multiplexing (DSCM), traditional TDMA-based PONs suffer from latency issues due to the requirement that all traffic must traverse the Optical Line Terminal (OLT). To mitigate this, the paper proposes physical modifications to the optical distribution network (ODN)—specifically the addition of asymmetrical splitters ("taps")—to enable direct, all-optical communication between Optical Network Units (ONUs), bypassing the OLT's electronic switching and O-E-O conversion. This approach is designed to support both intra-PON (within one tree) and inter-PON (between trees) connectivity.

## 2. Future Radio Requirements and X-Hauling Trends
Future radio networks require transport bitrates and latencies that vary based on the chosen functional split (CU/DU/RU). 
- **Bitrate Requirements:** Low-layer splits (e.g., Split 8) demand massive bandwidth (up to 1.25 Tb/s for 6G), which exceeds current VHSP capabilities, making mid-range options like Split 7.x more viable compromises.
- **Latency Constraints:** Service-specific requirements for Ultra-Reliable Low-Latency Communications (URLLC) demand end-to-end latencies as low as 0.5 ms. Transport networks must therefore target one-way propagation delays below 250 $\mu$s.
- **Infrastructure Trend:** Given the massive existing PON footprint, shifting X-haul to shared PON infrastructure is more scalable than point-to-point fiber, provided that latency bottlenecks are resolved.

## 3. Proposed ONU-to-ONU Architectures Enabled by DSCM-Based Coherent PON
The proposal focuses on establishing direct optical links between ONUs to avoid the "hairpin" forwarding delay associated with OLT electronic switches.

### A. Proposed Physical Architectures
The authors propose four configurations based on single-stage or two-stage splitting:
- **One-to-One (Single Stage):** Two asymmetrical taps and a short fiber patch-cord are added inside the splitter cabinet to create a direct path between two ONUs.
- **One-to-Few (Single Stage):** A combination of taps and a symmetrical splitter allows one ONU (e.g., a Distributed Unit, DU) to communicate with several other ONUs (e.g., Radio Units, RUs).
- **Two-Stage Splitting:** 
    - **Intra-stage:** Similar to the single-stage approach, connecting ONUs within the same second-stage cabinet.
    - **Inter-stage:** Connecting ONUs in different second-stage cabinets by modifying the first-stage splitter or adding a point-to-point fiber between cabinets.

**DSCM Integration:** The architecture uses DSCM to assign specific subcarriers (SCs) for intra-PON communication, keeping them distinct from regular PON traffic and using subcarrier interleaving to manage bidirectional transmission on a single fiber. This ensures coexistence with legacy IM-DD PONs via wavelength separation.

### B. Link Budget First-Order Analysis
The feasibility is analyzed based on ITU-T N1 class (29 dB loss limit) and a maximum allowable power imbalance of 10 dB between subcarriers at the receiver.
- **One-to-One results:** For 40 km links, an optimal tap split ratio of 20/80% requires only a 1.3 dB additional margin beyond the N1 limit. For 20 km, 10/90% is optimal with a 0.75 dB extra margin.
- **One-to-Few results:** A 1-to-4 ONU configuration over 40 km remains feasible with an additional margin of approximately 2 dB.
- **Statistical Analysis:** Using log-normal ODN loss distributions from real-world data, split ratios of 10/90 and 20/80 are identified as the most stable for maintaining power balance.
- **Two-Stage splitting:** Intra-stage communication is feasible with minimal extra margin (0.5–2.2 dB), but inter-stage communication faces significantly higher loss, requiring much larger margins or specific split ratios to remain viable.

## 4. Converged Coherent Metro + PON
The authors extend the concept to converged networks where coherent transmission reaches from the metro core to the access edge without O-E-O conversion via ROADMs.

### A. Metro + PON Physical Architecture
Three connection types are defined:
1. **Intra-PON:** As described in Section 3.
2. **Pre-metro:** Communication between an ONU and a node located before the metro segment, implemented using three taps to drop signals at a pre-metro DU.
3. **Inter-PON:** All-optical links between ONUs in different PON trees via optical splitters within the central optical matrix of the metro network.

### B. Metro + PON First-Order Link Budget Analysis
The analysis incorporates Optical Signal-to-Noise Ratio (OSNR) penalties associated with metro traversal (e.g., a 4 dB penalty for 17 dB OSNR). For pre-metro links, a main DU tap split ratio of 2/98% is found to be optimal for minimizing power imbalance between the RU-DU link and the DU-OLT link.

## 5. First-Order Latency Analysis in the Proposed Architectures
Latency is calculated considering fiber propagation (5 $\mu$s/km), Tx/Rx DSP processing (~31 $\mu$s), and electrical switching delays (20–30 $\mu$s). The proposed direct optical links provide significant reductions:
- **Intra-PON:** Reduces latency from ~287 $\mu$s to 131 $\mu$s ($\sim$54% reduction) by removing the OLT switch and one set of Tx/Rx conversions.
- **Pre-metro:** Reduces latency from ~387 $\mu$s to 131 $\mu$s ($\sim$66% reduction) by bypassing metro hops and OLT processing.
- **Inter-PON:** Reduces latency from ~437 $\mu$s to 281 $\mu$s ($\sim$35% reduction).

## 6. Conclusion
The authors demonstrate that simple physical modifications (taps) combined with DSCM coherent-PON enable direct all-optical ONU-to-ONU communication. This approach is backward-compatible and requires very little additional power margin (as low as 1.3 dB over N1 class for 40 km links). The primary advantage is a substantial reduction in physical-layer latency, making it highly suitable for the stringent requirements of 5G/6G X-haul services.
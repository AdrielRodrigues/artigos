---
index_terms:
  - Multiband-Elastic Optical Networks
  - Dedicated Path Protection
  - RBMSA
  - C+L band transmission
  - Bitrate Blocking Probability
---

# Routing, Band, Modulation and Spectrum Assignment with Dedicated Protection in Multiband-Elastic Optical Networks

## Abstract
The paper examines resource allocation and protection strategies within Multiband-Elastic Optical Networks (MB-EON), focusing on the integration of routing, band selection, modulation format, and spectrum assignment (RBMSA). The authors compare five specific approaches—one fully flexible (DPP-RBMSA), two dedicated band schemes (DBP-$C_w$-$L_b$ and DBP-$C_b$-$L_w$), and two hybrid schemes (hyb-DBP-$C_w$-$L_b$ and hyb-DBP-$C_b$-$L_w$). Using Bitrate Blocking Probability (BBP), Backup to Working Resources Ratio (BWRR), and Band Spectrum Utilization (BSU), the study identifies that while `hyb-DBP-Cb-Lw` offers the lowest blocking, `DPP-RBMSA` provides the highest level of protection.

## I. Introduction
To address exponential global data traffic growth, MB-EON utilizes Band Division Multiplexing (BDM) to extend capacity beyond the C-band into L, S, E, and O bands. The authors focus on C+L band deployments using wideband amplifiers, which provide approximately 11.5 THz of bandwidth and can be deployed over existing infrastructure. 

The primary challenge is balancing traffic acceptance with network resilience. The paper focuses on Dedicated Path Protection (DPP), which employs a 1+1 redundancy strategy where backup resources are reserved via link-disjoint paths to protect against both fiber cuts and amplifier failures. The goal is to evaluate the trade-off between computational complexity, blocking rates, and protection levels across flexible and dedicated band allocation strategies.

## II. Related Works
The authors review existing survivability research in MB-EON, noting prior work on band partitioning, GSNR-sensitive schemes, and virtual bypasses for backup paths. They distinguish this study by focusing specifically on fully upgraded networks with wideband amplifiers and a strict requirement for link-disjoint routes to ensure 100% survivability against both fiber and amplifier failures.

## III. Proposed Methodology
The network is modeled as a graph $G(N, L)$ where each link contains C and L bands with specific spectrum slots (SS). The RBMSA process calculates the required number of SS based on bitrate demand, modulation level ($m$), and a 12.5 GHz slot width, including a guard band. Modulation is selected based on the transmission reach of the specific band; notably, the C-band is more robust (longer reach) than the L-band.

The five evaluated protection approaches are:
*   **DPP-RBMSA**: A flexible first-fit approach searching both bands for working and backup routes, prioritizing the C-band. If a working route is found but no disjoint backup route exists, the request is accepted as "Unprotected."
*   **DBP-$C_w$-$L_b$**: Dedicated Band Protection where working resources are strictly limited to the C-band and backup resources strictly to the L-band.
*   **DBP-$C_b$-$L_w$**: Working resources are strictly in the L-band, while backup resources are strictly in the C-band.
*   **hyb-DBP-$C_w$-$L_b$**: A hybrid approach where backups are restricted to the L-band, but working resources can be searched in both C and L bands.
*   **hyb-DBP-$C_b$-$L_w$**: Backups are restricted to the C-band, while working resources can be searched in both L and C bands.

## IV. Performance Evaluation
The authors simulated these approaches across six topologies (US-24, Paneuro, Coronet, Cost239, DT-17, JP-12) using a Matlab event-driven simulator. Parameters include Poisson arrival rates and exponential holding times, with bitrate demands of 100, 200, or 400 Gbps.

### Key Findings and Analysis
*   **Bitrate Blocking Probability (BBP)**: In both small-scale (JP-12) and large-scale (US-24) networks, `hyb-DBP-Cb-Lw` consistently achieved the lowest BBP. This is attributed to the flexibility of searching for working resources in both bands while utilizing the more robust C-band for backups.
*   **Protection Level**: Despite lower blocking, `hyb-DBP-Cb-Lw` often had a lower percentage of Protected Requests (PR) compared to `DPP-RBMSA`. In large networks (US-24, Paneuro, Coronet), `DPP-RBMSA` provided significantly higher protection levels with only a marginal increase in blocking.
*   **Resource Efficiency (BWRR and BSU)**: `DBP-Cb-Lw` and its hybrid version showed BWRR values closer to one because the backup route in the C-band requires fewer additional spectrum slots due to better transmission reach than L-band working routes. 
*   **Network Scale Trade-offs**: In small networks (e.g., JP-12), `hyb-DBP-Cb-Lw` is highly effective for reducing blocking. However, in geographically vast networks (e.g., US-24), the flexible `DPP-RBMSA` approach is preferred because the substantial gain in protected requests outweighs the slight increase in blocked bitrate.

## V. Conclusion
The study concludes that there is a clear trade-off between maximizing traffic acceptance (lowest BBP) and ensuring maximum resilience (highest PR%). While dedicated band strategies like `hyb-DBP-Cb-Lw` minimize blocking by leveraging band-specific characteristics, the flexible `DPP-RBMSA` approach provides superior protection for large-scale networks. Future research is suggested regarding the impact of other configurations and the potential use of shared backup resources to further optimize capacity.
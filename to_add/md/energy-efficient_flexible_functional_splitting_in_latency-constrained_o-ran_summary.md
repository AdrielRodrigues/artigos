---
index_terms:
  - O-RAN
  - flexible functional splitting
  - Cloud-Fog RAN
  - Integer Linear Programming
  - queuing delay model
  - energy efficiency
---

# Energy-Efficient Flexible Functional Splitting in Latency-Constrained O-RAN

## Abstract
The paper addresses bandwidth and latency challenges in Cloud Radio Access Networks (CRAN) by proposing a Cloud-Fog RAN (CF-RAN) architecture. The authors introduce an Integer Linear Programming (ILP) model to optimize flexible functional splitting (FFS) and resource allocation, aiming to minimize power consumption while adhering to QoS latency constraints. A novel queuing delay model based on the eCPRI standard is used to determine latency bounds. For scalability in larger networks, a graph-based heuristic is proposed. Simulation results indicate that this approach improves network availability by 35% and reduces power consumption by 9.93% compared to previous CF-RAN studies.

## I. Introduction
The transition to 6G requires adaptive RAN architectures. While CRAN allows for centralization, it faces strict end-to-end delay and capacity constraints. Hybrid Cloud-Fog RAN (CF-RAN) and Open-RAN (O-RAN) mitigate this by placing processing functions closer to the user via Open Radio Units (O-RU), Open Distributed Units (O-DU), and Open Central Units (O-CU). Flexible Functional Splitting (FFS) allows operators to dynamically select split options based on resources and QoS needs. 

The authors identify a trade-off: centralizing baseband operations reduces energy but increases fronthaul traffic and latency; dispersing them increases energy usage but relaxes capacity demands. The paper contributes a holistic solution for sizing O-RAN optical fronthauls using eCPRI, incorporating a queuing model that accounts for synchronization, control, and data connections to inform an ILP and a scalable heuristic algorithm.

## II. Related Works
The authors review existing research on vBBU placement and NFV service allocation, noting that many current models assume static scenarios or focus on either latency or energy in isolation. While some studies use Machine Learning (ML) or Reinforcement Learning (RL) for dynamic splitting, the authors argue that these often lack comprehensive analytical queuing models integrated into an optimization framework. This work distinguishes itself by combining a delay-aware queuing model with both ILP and heuristics to address both static and dynamic CF-RAN scenarios.

## III. System Architecture
The considered architecture consists of a RAN processing layer (O-RUs, Fog nodes for O-DUs, and Cloud for O-CUs) and an optical transmission layer based on Virtual Passive Optical Networks (VPONs). These VPONs use Time-Wavelength Division Multiplexing (TWDM-PON), where multiple interfaces (F1, Xn, E1) share channels via Time Division Multiplexing (TDM).

### A. Functional Splitting Options
Functional splitting distributes processing tasks to balance bandwidth and latency. The paper evaluates four eCPRI split options:
*   **Split E:** Most centralized; only RF functions in O-RU. Highest bandwidth demand but lowest local processing.
*   **Split I:** Partial PHY centralization; reduces bit rate to 40% of Split E via local FFT and modulation.
*   **Split D:** MAC/PHY split; schedules users in Fog nodes, reducing bandwidth while increasing latency sensitivity.
*   **Split B:** PDCP-RLC split; most distributed, significantly easing latency constraints but limiting coordinated features like CoMP.

Bandwidth requirements for these splits are calculated using formulas based on antennas, sampling rates, and MIMO layers. A comparison table (Table I) shows that bandwidth demand drops drastically from Split E (1966 Mb/s) to Split B (44 Mb/s).

## IV. Queue and Mathematical Model
The authors define a framework to determine latency upper bounds for each split option to inform the optimization model.

### A. Queuing Delay Model
Latency is modeled based on two scenarios:
1.  **Splits E and I:** Traffic is characterized as Constant Bit Rate (CBR) and modeled using **D/D/1 queues**, where delay depends on optical capacity and traffic rate.
2.  **Splits B and D:** Total delay is the sum of O-RU-to-O-DU and O-DU-to-O-CU segments. Control and synchronization traffic remain CBR (D/D/1), but user data is modeled using **Token Bucket Admission Control (TBAC)** to manage burstiness, effectively utilizing an M/M/1 logic for peak events. 

The overall worst-case delay ($D_{max}^s$) for any split $s$ is the maximum of the delays experienced by user, control, and synchronization traffic.

### B. ILP Model Formulation
An Integer Linear Programming (ILP) model is proposed to minimize total power consumption, defined as the sum of costs from active processing nodes, line cards, and the chosen functional splits. 

**Key constraints include:**
*   Each O-RU must be associated with exactly one FS-option.
*   VPON bandwidth and node processing capacities must not be exceeded.
*   Processing nodes and VPONs are activated only if they host demands.
*   The selected split for a given RU must satisfy the overall latency constraint derived from the queuing model.

The authors note that while ILP provides optimal solutions, it is computationally impractical for large networks due to exponential growth in decision variables.

### C. Illustrative Example
A small-scale example with two fog nodes, one cloud node, and three O-RUs demonstrates how the ILP assigns demands based on bandwidth requirements and queuing delays (e.g., Split E results in low delay when capacity is high, but shifts to other splits as $\lambda \to \mu$).

## V. On-Line Heuristic Solution
To ensure scalability, a graph-based heuristic is proposed that models the network as a directed flow network.

### A. Graph Construction
The network is represented as a graph $G=(V,E)$. Vertices represent processing levels (O-RU $\to$ Fog $\to$ Cloud) and specific baseband functions. Edges are annotated with costs (latency) and capacities (bandwidth). The problem is formulated as a minimum-cost maximum-flow problem.

### B. Key Constraint on Function Indexing
A "no-backtracking" constraint is enforced: if function $f$ is processed at level $i$, subsequent functions $g > f$ must be processed at level $j \ge i$. 

The heuristic algorithm follows four steps:
1.  **Initialization:** Direct all traffic to the Cloud.
2.  **Redistribution:** Shift flow to Fog nodes if Cloud capacity or latency constraints are violated.
3.  **Split Selection:** Select the most centralized split that satisfies constraints.
4.  **Final Routing:** Forward processed traffic to the sink node.

The complexity is $O(|V| \cdot |E|^2 + |S| \cdot m)$, which allows execution in milliseconds, unlike the ILP's potential for hours of computation.

## VI. Numerical Results
Experiments were conducted using the 5GPy simulator with a 24-hour urban traffic profile (peak load $\approx$ 120 Gb/s).

### A. Simulation Traffic Profile
The daily traffic is normalized [0, 1], peaking at 2 PM. The peak-to-average ratio (PAR) is approximately 3.14, creating intermittent loads that test the queuing model's stability.

### B. Scenario I: Static Traffic
Comparing FS CF-RAN against C-RAN and non-FFS CF-RAN shows:
*   **Availability:** FS CF-RAN achieves nearly 100% availability, whereas C-RAN suffers from sharp drops when Split E latency exceeds 100 $\mu$s due to queuing congestion.
*   **Energy:** FS CF-RAN is more energy-efficient than non-FFS CF-RAN because it avoids unnecessary fog node activation by optimizing split choices.
*   **Performance:** The heuristic's results are closely aligned with the ILP's optimal solutions but offer drastically lower execution times (under 1 second vs. up to 30,000 seconds).

### C. Scenario II: Dynamic Traffic
In dynamic simulations, FS CF-RAN effectively prevents demand blocking by adapting splits in real-time as load increases. While C-RAN blocks demands during latency violations and non-FFS CF-RAN blocks them when fog nodes saturate, the flexible approach optimizes resource dimensioning to maintain service continuity.

## VII. Concluding Remarks
The paper concludes that combining a queuing-aware ILP/heuristic approach allows O-RAN to balance energy efficiency with strict latency requirements. The heuristic is highlighted as the only practical choice for real-time large-scale deployment.

### A. Orchestration Overhead and FS Reconfiguration Costs
The authors acknowledge that frequent splitting changes introduce signaling overhead. They suggest that because changes are triggered by significant load variations, oscillations are limited, but propose adding hysteresis functions in future work to further reduce orchestration burden.

### B. Scalability Analysis and Runtime Environment
Empirical evidence shows the ILP solver fails (due to memory or time limits) for networks exceeding 60 O-RUs. The graph-based heuristic remains feasible in milliseconds regardless of scale, though a slight degradation in solution quality occurs under extreme constraints.

### C. Toward Real-World FS CF-RAN Deployment
For real-world application, the authors suggest implementing these strategies as xApps within the Near-Real-Time RIC or as SMO services. Future work will focus on testing the model on O-RAN compliant testbeds (e.g., OpenAirInterface) and using ML to predict optimal configurations.
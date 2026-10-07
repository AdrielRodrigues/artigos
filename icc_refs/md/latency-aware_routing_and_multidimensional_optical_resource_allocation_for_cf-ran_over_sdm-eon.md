![](_page_0_Picture_1.jpeg)

# Latency-Aware Routing and Multidimensional Optical Resource Allocation for CF-RAN over SDM-EON

Edson Adriel Rodrigues<sup>1</sup> , Daniel Macedo Batista ˆ 1 , Helder Oliveira<sup>1</sup>

1 Institute of Mathematics, Statistics and Computer Science (IME) University of Sao Paulo (USP) – S ˜ ao Paulo, SP – Brazil ˜

{adrielrodrigues, batista, helderoliveira}@ime.usp.br

*Abstract. Cloud-Fog Radio Access Networks (CF-RAN) are a promising architecture to support heterogeneous 5G services with stringent latency requirements. However, efficient optical resource allocation remains a challenge under dynamic traffic conditions. This paper proposes 5GEON, a routing and multidimensional optical resource allocation algorithm for CF-RAN over Space-Division Multiplexing Elastic Optical Networks (SDM-EON). The solution jointly considers traffic classification, latency-aware offloading, and adaptive modulation. Simulation results show that 5GEON significantly reduces blocking, achieving up to three times lower bandwidth blocking ratio than a state-of-the-art baseline, while effectively prioritizing Ultra-Reliable Low-Latency Communication (URLLC) traffic.*

# 1. Introduction

Mobile communication networks carry an increasing share of global Internet traffic, driven by emerging applications such as virtual and augmented reality, autonomous vehicles, remote healthcare, smart cities, and large-scale Internet of Things deployments. These applications impose stringent latency constraints while demanding high data rates, requiring network infrastructures capable of delivering high throughput with low end-toend delay [Srinivas et al. 2024].

This sustained traffic growth, fueled by immersive multimedia services and massive device connectivity, places unprecedented pressure not only on radio access networks but also on the transport infrastructure supporting fronthaul and backhaul communications [Dias et al. 2023]. Fifth-generation (5G) networks address these challenges by enabling high data rates and ultra-low latency communication, with radio signal processing split between Remote Radio Heads (RRHs) and Baseband Units (BBUs) interconnected through high-capacity optical fronthaul networks subject to strict latency and bandwidth constraints [Aktar et al. 2024].

To overcome fronthaul capacity and scalability limitations, Cloud-Fog Radio Access Networks (CF-RAN) distribute processing resources across fog and cloud nodes, enabling latency-sensitive traffic to be handled closer to end users while offloading less stringent workloads to centralized infrastructures. However, this architectural flexibility introduces new challenges related to traffic offloading decisions and efficient resource management across heterogeneous processing layers [Ahsan et al. 2023, Dos Santos et al. 2025].

The optical transport network plays a fundamental role in enabling communication between CF-RAN layers [Al-Tarawneh et al. 2024]. While traditional Wavelength Division Multiplexing (WDM) networks offer high capacity, they lack flexibility to efficiently support heterogeneous traffic demands. Elastic Optical Networks (EONs) address this limitation through fine-grained spectrum allocation, improving adaptability and spectrum efficiency [Wang et al. 2024]. This flexibility is further extended by Space-Division Multiplexing EONs (SDM-EONs), which employ multi-core fibers to increase capacity, at the cost of introducing challenges related to multidimensional resource allocation, spectrum fragmentation, and inter-core crosstalk [Hafezi and Rahbar 2024].

Despite advances in both CF-RAN architectures and optical network technologies, most existing works address these domains independently [Liu et al. 2024]. CF-RANoriented solutions often overlook transport-layer constraints, while SDM-EON resource allocation studies typically ignore the latency requirements and traffic differentiation inherent to 5G services. As a result, the joint problem of traffic-aware offloading and multidimensional optical resource allocation remains insufficiently explored.

Unlike existing approaches, this paper proposes 5GEON, an algorithm that jointly addresses traffic-aware offloading and multidimensional optical resource allocation in SDM-EONs under explicit 5G latency constraints. The alorithm prioritizes latencysensitive traffic, incorporates adaptive modulation, and proactively offloads processing across fronthaul and backhaul layers. Simulation results demonstrate that 5GEON significantly improves network performance, allowing up to three times more requests to be allocated compared to state-of-the-art approaches under adaptive modulation scenarios.

The main contributions of this paper are summarized as follows: (i) We propose a novel algorithm, named 5GEON, for routing and multidimensional resource allocation in SDM-EONs supporting CF-RAN architectures; (ii) The proposed solution jointly considers 5G traffic classification and processing offloading decisions, prioritizing latency-sensitive services; (iii) We incorporate adaptive modulation into the allocation process, improving spectrum utilization and reducing blocking probability; (iv) Extensive simulation-based experiments demonstrate that 5GEON significantly outperforms a stateof-the-art baseline in terms of bandwidth blocking ratio, energy efficiency, and spectrum fragmentation.

This paper is organized as follows: Section 2 presents a review of the literature on the network model considered and discusses the potential of the proposal, Section 3 presents details of the network architecture considered for the work and the proposed solution, Section 4 discusses the procedures taken to evaluate performance, Section 5 presents and discusses the results obtained in simulation on network performance, and Section 6 discusses the conclusions obtained from the analysis of the model and proposal.

# 2. Related Works

Several studies have investigated resource management and processing placement in CF-RAN. The authors in [dos Santos et al. 2022] propose solutions for Virtual Passive Optical Network allocation and virtualized BBU placement in CF-RAN. They formulate an Integer Linear Programming (ILP) model that incorporates processing and cost constraints with the objective of minimizing energy consumption. Although near-optimal solutions are obtained through ILP relaxation and machine learning techniques, the optical transport network is abstracted, and spectrum fragmentation and multidimensional optical resource allocation are not explicitly considered. In contrast, we explicitly model the elastic optical transport layer and its constraints.

In [Santos et al. 2021], the authors investigate a hybrid CF-RAN architecture aiming at optimal fronthaul scaling. Their ILP-based solution determines the best location for processing functions in order to reduce energy consumption, considering Quality of Service requirements. While this work provides valuable insights into processing centralization, it assumes a Time and Wavelength Division Multiplexing Passive Optical Network (TWDM-PON) and does not analyze the impact of offloading decisions on elastic or space-division multiplexed optical backbones. Unlike this approach, we focus on SDM-EONs and jointly evaluates processing offloading and optical resource allocation.

A three-layer CF-RAN communication architecture is proposed in [Ahsan et al. 2024], where services are classified according to their latency requirements and assigned to fog or cloud nodes accordingly. The fronthaul and backhaul communications rely on a WDM-based optical infrastructure. Although this solution incorporates traffic awareness, it relies on fixed spectrum allocation and does not explore the flexibility offered by elastic optical networks. Our work extends this perspective by employing SDM-EONs, enabling finer-grained spectrum allocation and adaptive modulation to better accommodate heterogeneous traffic demands.

From the perspective of elastic optical networks, several studies focus on spectrum and core allocation strategies. The Smart-Fit policy proposed in [Hafezi and Ghaffarpour Rahbar 2024] aims to reduce spectrum wastage by allocating frequency slots that exactly match the request size, combined with multi-path routing per core. While effective in reducing fragmentation, this approach does not consider traffic classification or latency constraints typical of 5G services, which are fundamental aspects addressed in our proposal.

Fragmentation-aware strategies are also explored in [Khorasani et al. 2023], where core and frequency slot selection policies are proposed to reduce blocking probability in SDM-EONs. Similarly, the work in [Vasundhara and Mandloi 2024] introduces a routing and dynamic core allocation approach that incorporates crosstalk constraints into the resource allocation process. Although these solutions improve spectrum utilization, they are evaluated independently of mobile network architectures and do not consider processing offloading or differentiated service requirements.

Overall, the existing literature addresses either CF-RAN processing and traffic management or optical resource allocation in elastic and space-division multiplexed networks. However, few works consider the interaction between these two domains. This paper fills this gap by proposing a unified solution that jointly addresses traffic-aware offloading decisions in CF-RAN architectures and multidimensional resource allocation in SDM-EONs, considering both optical constraints and 5G service requirements.

# 3. 5GEON Algorithm

This section presents the *5GEON* Algorithm, designed to perform efficient routing and multidimensional optical resource allocation, while respecting the multiclass heterogeneous latency requirements to support 5G traffic offloading in CF-RAN architectures. The *5GEON* aims to maximize the number of successfully established connections over a SDM-EON backbone by jointly considering traffic classification, processing offloading decisions, and multidimensional resource availability in the optical transport network.

| Table 1. Comparison of related works in terms of considered architectures and |  |
|-------------------------------------------------------------------------------|--|
| optical technologies.                                                         |  |

| Work                                 | CF-RAN | EON | SDM-EON |
|--------------------------------------|--------|-----|---------|
| [dos Santos et al. 2022]             | ✓      |     |         |
| [Santos et al. 2021]                 | ✓      |     |         |
| [Ahsan et al. 2024]                  | ✓      |     |         |
| [Hafezi and Ghaffarpour Rahbar 2024] |        | ✓   |         |
| [Khorasani et al. 2023]              |        | ✓   | ✓       |
| [Vasundhara and Mandloi 2024]        |        | ✓   | ✓       |
| This work                            | ✓      | ✓   | ✓       |

# 3.1. Network Architecture

The network architecture follows a three-layer CF-RAN model composed of edge, fog, and cloud nodes. At the edge, Cell Sites (CS) equipped with Remote Radio Heads (RRHs) are responsible for radio frequency transmission and reception. In accordance with the 5G functional split paradigm, Baseband Units (BBUs) are decoupled from RRHs, requiring high-capacity and low-latency communication between radio and processing components.

![](_page_3_Picture_5.jpeg)

**Figure 1. Optical architecture for CF-RAN.**

Figure 1 shows the CF-RAN architecture and the interaction between its layers. Traffic flows from CS towards processing nodes through optical fronthaul. The traffic is classified according to service requirements into three categories: Ultra-Reliable Low-Latency Communication (URLLC), Enhanced Mobile Broadband (eMBB), and Massive Machine-Type Communication (mMTC). Due to its stringent latency constraints, URLLC traffic must be processed as close to the user as possible and is therefore prioritized for execution at fog nodes. In contrast, eMBB and mMTC traffic can tolerate higher latency and is often offloaded to cloud processing nodes.

Fog nodes provide limited processing capacity and are geographically closer to end users, while cloud nodes offer higher computational resources at the cost of increased propagation delay. Existing processing nodes, both fog and cloud, start inactive. The algorithm checks for each request to see if there is a responsible processing node that meets latency restrictions. The priority is to establish the connection on active nodes to minimize processing energy consumption. If no active node can fulfill the request, a node from the set is activated. The goal is to minimize the number of active nodes while prioritizing transmission. Latency logs track the time interval between the source and the path to the processing node, abstracting delays caused by the node's state.

An Optical Transport Network based on multi-core fibers operates to interconnect fog and cloud layers. Each optical link is bidirectional and composed of 7 cores, with each core divided into 32 frequency slots of 12.5 GHz granularity. The optical backbone operates under the SDM-EON paradigm, enabling flexible spectrum and multidimensional optical resource allocation.

#### 3.2. Operations

The operation of the proposed 5GEON algorithm is formally described in Algorithm 1. The algorithm performs routing and multidimensional optical resource allocation for each incoming traffic request, taking into account service classification, latency constraints, and the availability of optical resources in the SDM-EON backbone.

```
Algorithm 1: 5GEON
   Input : G = (V, E), C, S, R
   Output: Set of established lightpaths L
 1 L ← ∅;
 2 foreach r = (src, bw, t) ∈ R do
 3 foreach m ∈ M ordered by decreasing spectral efficiency do
 4 if t = URLLC then
 5 Fa ← set of active fog nodes;
 6 P ← {p(src, f) | f ∈ Fa ∧ d(p) ≤ tht};
 7 else
 8 Ca ← set of active cloud nodes;
 9 P ← {p(src, c) | c ∈ Ca ∧ d(p) ≤ tht};
 10 if P ̸= ∅ then
 11 p
              ∗ ← arg minp∈P d(p);
 12 if ∃(c, s) ∈ (C, S) such that p
                                    ∗
                                     supports (bw, m) then
 13 Allocate (c, s) along p
                                 ∗
                                  ;
 14 L ← L ∪ {lp(p
                            ∗
                             , c, s, m)};
 15 break;
 16 else
 17 Activate processing node satisfying tht;
 18 Recompute feasible path set P;
19 return L;
```

Initially, the network topology G = (V, E) and the set of traffic requests R are loaded. Each request is represented by the tuple r(src, bw, t), where src denotes the source Cell Site, bw the required bandwidth, and t the traffic class. Requests are processed sequentially. For each request, the algorithm evaluates a predefined set of modulation formats M, ordered by decreasing spectral efficiency. The selection of a modulation format is constrained by the maximum transmission reach associated with the candidate path.

For URLLC requests, the algorithm prioritizes processing at fog nodes due to their stringent latency requirements. In this case, the algorithm constructs the set of feasible paths connecting the source node to active fog nodes whose end-to-end delay satisfies the latency threshold associated with the URLLC class. Candidate paths are computed using a shortest-path algorithm considering propagation delay as the link weight. If this set is non-empty, the feasible path with minimum end-to-end delay is selected and the allocation procedure continues. Otherwise, a fog node satisfying the latency constraint is activated, and the set of feasible paths is recomputed.

For eMBB and mMTC requests, which tolerate higher end-to-end delay, the same procedure is applied considering cloud processing nodes. The algorithm first attempts to serve the request using active cloud nodes. Similarly, candidate paths are computed based on minimum propagation delay, and only paths satisfying the latency threshold of the traffic class are considered. If no feasible path satisfies the latency constraint, a new cloud processing node is activated, provided that the latency requirement can be met.

Once a feasible processing node and path are determined, the algorithm performs multidimensional optical resource allocation over the SDM-EON backbone. The core selection is made from adjacent cores, using a first-fit strategy to keep the central core free and reduce crosstalk between cores. The slots are also selected in first-fit order, contiguously, and respecting the selected band and modulation. In this way, both contiguity and continuity restrictions are respected. If sufficient optical resources are not available along the selected path, the request is blocked.

This procedure is repeated for all incoming traffic requests, resulting in the dynamic establishment of lightpaths connecting Cell Sites to fog or cloud processing nodes. By jointly considering traffic classification, latency constraints, modulation selection, and multidimensional optical resource availability, the proposed algorithm enables efficient and traffic-aware resource allocation across the CF-RAN architecture. Table 2 summarizes the notation used in Algorithm 1 and throughout the proposed model, providing a reference for the symbols and variables adopted in the routing, modulation selection, and multidimensional resource allocation procedures.

Regarding computational complexity, the proposed *5GEON* algorithm processes each incoming request independently. For each request, a limited set of modulation formats is evaluated, and a delay-constrained shortest path computation is performed. Assuming a shortest-path algorithm based on Dijkstra's method, the path computation step has a complexity of O(|E| + |V | log |V |), where |V | and |E| denote the number of nodes and links in the network, respectively. The subsequent verification of multidimensional optical resource availability involves scanning a constant number of cores and frequency slots along the selected path. As a result, the overall complexity of the algorithm grows polynomially with the network size and the number of traffic requests, making the proposed solution suitable for dynamic CF-RAN scenarios.

# 4. Experimental Design

This section describes the experimental setup adopted to evaluate the performance of the proposed 5GEON algorithm. The experiments aim to assess the effectiveness of the algorithm in allocating optical resources under heterogeneous 5G traffic demands while minimizing request blocking and improving spectrum and energy efficiency.

**Table 2. Algorithm notation.**

| Symbol         | Description                                                                   |
|----------------|-------------------------------------------------------------------------------|
| G<br>= (V, E)  | Network graph composed of nodes V<br>and links E                              |
| V              | Set of network nodes                                                          |
| E              | Set of network links                                                          |
| C              | Set of fiber cores per link                                                   |
| S              | Set of frequency slots per core                                               |
| R              | Set of traffic requests                                                       |
| r(src, bw, t)  | Traffic request with source src, bandwidth<br>bw, and class<br>t              |
| t              | Traffic class, t<br>∈ {URLLC,<br>eMBB,<br>mMTC}                               |
| Rt             | Set of requests of class t                                                    |
| M              | Set of modulation formats                                                     |
| p              | Candidate routing path                                                        |
| d(p)           | End-to-end propagation delay of path p                                        |
| tht            | Latency threshold associated with traffic class t                             |
| c              | Selected fiber core                                                           |
| s              | Allocated set of frequency slots                                              |
| lp(p, c, s, m) | Established lightpath over path p, core<br>c, slots<br>s, and modulation<br>m |

**Table 3. Modulation Parameters.**

|                          | BPSK | QPSK  | 8-QAM | 16-QAM | 32-QAM | 64-QAM |
|--------------------------|------|-------|-------|--------|--------|--------|
| Transmission Reach (km)  | 125  | 250   | 500   | 1000   | 2000   | 4000   |
| Capacity (GHz)           | 12.5 | 25    | 37.5  | 50     | 62.5   | 75     |
| Crosstalk Threshold (dB) | -14  | -18.5 | -21   | -25    | -28.5  | -31    |

# 4.1. Simulation Environment

The experiments were conducted using FlexGridSim [Moura and Drummond ], a discrete-event simulator for elastic optical networks. The simulator was extended to support the considered CF-RAN architecture and the classification of 5G traffic into distinct service classes and it is available on GitHub repository1 . These extensions allow the joint evaluation of processing offloading decisions and multidimensional optical resource allocation in SDM-EONs.

The simulated network consists of 100 nodes distributed over an area of 200 km<sup>2</sup> , representing a dense urban scenario. Among these nodes, 50 represent Cell Sites (CSs), 30 correspond to fog processing nodes, and 20 represent Central Offices (COs), which may host cloud processing resources. At the beginning of the simulation, only one CO is active, while additional fog and cloud nodes are dynamically activated based on traffic demand and latency constraints.

The optical transport network is based on a Space-Division Multiplexing Elastic Optical Network architecture. Each optical link is bidirectional and composed of seven cores, each divided into 32 frequency slots of 12.5 GHz. The modulation formats supported transmit between one and six bits per symbol, and the selected modulation depends on the total transmission distance, ensuring compliance with physical layer constraints, as shows Table 3.

<sup>1</sup>[FlexgridSim 5G - https://github.com/AdrielRodrigues/flexgridsim-5g](https://github.com/AdrielRodrigues/flexgridsim-5g)

**Table 4. Simulation parameters.**

| Parameter                  | Value             |
|----------------------------|-------------------|
| Simulation area            | 200 km2           |
| Total number of nodes      | 100               |
| Cell Sites (CSs)           | 50                |
| Fog nodes                  | 30                |
| Cloud nodes (COs)          | 20                |
| Initial active cloud nodes | 1                 |
| Number of requests         | 10000             |
| Arrival process            | Poisson           |
| Holding time distribution  | Exponential       |
| Fiber cores per link       | 7                 |
| Frequency slots per core   | 32                |
| Slot bandwidth             | 12.5 GHz          |
| Modulation formats         | 1–6 bits/symbol   |
| Traffic classes            | URLLC, eMBB, mMTC |
| URLLC latency constraint   | 50 µs             |
| eMBB latency constraint    | 100 µs            |
| mMTC latency constraint    | 250 µs            |

### 4.2. Traffic Model

Traffic requests are generated at the Cell Sites following a Poisson arrival process. The total number of generated requests is set to 10,000, proportionally distributed among the three 5G traffic classes: URLLC, eMBB, and mMTC. The holding time of accepted requests follows an exponential distribution, a common assumption in elastic optical network simulations. Once a request is accepted, the corresponding optical and processing resources remain allocated for the entire duration of the holding time and are released upon its completion.

Each traffic class is associated with specific latency and bandwidth requirements. URLLC requests require end-to-end latency below 50 µs and bandwidth demands of 50/80 Mbps. eMBB requests tolerate up to 100 µs of latency and require bandwidths of 240/360 Mbps. mMTC requests tolerate up to 250 µs of latency and require bandwidths of 50/80 Mbps. These values are aligned with typical service requirements adopted in the literature. Once a request is accepted, the corresponding optical and processing resources remain allocated for the duration of the request. If sufficient resources are not available or latency constraints cannot be satisfied, the request is blocked.

Table 4 summarizes the main simulation parameters adopted in the experiment, including network topology characteristics, traffic generation assumptions, optical resource configuration, and latency constraints associated with each 5G service class.

# 4.3. Performance Metrics

The performance of the proposed solution is evaluated using three metrics: Bandwidth Blocking Ratio (BBR), Energy Efficiency (EE), and Fragmentation Ratio (FR). All metrics are computed considering a 95% confidence interval.

The BBR quantifies the proportion of bandwidth requests that could not be successfully allocated due to insufficient network resources. It is defined as the ratio between the total blocked bandwidth and the total requested bandwidth, as expressed in Equation (1).

$$BBR = \frac{\sum_{i=1}^{n} \alpha_i \cdot BW_{blocked}(i)}{\sum_{j=1}^{m} \beta_j \cdot BW_{request}(j)}$$
(1)

In Equation (1),  $\alpha_i$  represents the number of times the bandwidth request i is blocked,  $\beta_j$  denotes the number of occurrences of bandwidth request j,  $BW_{\text{blocked}}(i)$  is the blocked bandwidth of request i, and  $BW_{\text{request}}(j)$  is the requested bandwidth.

In addition to the overall BBR, this metric is also computed separately for each 5G traffic class in order to evaluate the impact of resource contention on differentiated services. The BBR for a given traffic class t is defined as:

$$BBR_{t} = \frac{\sum_{i \in \mathcal{R}_{t}} \alpha_{i} \cdot BW_{blocked}(i)}{\sum_{j \in \mathcal{R}_{t}} \beta_{j} \cdot BW_{request}(j)}, \quad t \in \{URLLC, eMBB, mMTC\},$$
 (2)

Where  $\mathcal{R}_t$  denotes the set of requests belonging to traffic class  $t \in \{\text{URLLC}, \text{eMBB}, \text{mMTC}\}$ . This per-class evaluation allows assessing whether latency-sensitive traffic is effectively prioritized under heterogeneous demand conditions.

EE evaluates how efficiently the network utilizes energy to transmit data. It is defined as the ratio between the total accepted bandwidth and the total energy consumption of the optical network components, including transponders, switches, and amplifiers, as shown in Equation (3).

$$EE = \frac{\sum_{i=1}^{n} \gamma_i \cdot BW_{\text{accepted}}(i)}{\sum_{j=1}^{l} \epsilon_j \cdot (P_{\text{transponder}}(j) + P_{\text{switch}}(j) + P_{\text{amplifier}}(j))}$$
(3)

In Equation (3),  $\gamma_i$  represents the accepted bandwidth of request i, while  $\epsilon_j$  denotes the energy consumed by the optical components on link j [Agarwal et al. 2025].

FR measures the degree of spectrum fragmentation in the optical network and reflects how evenly the available frequency slots are distributed. It is defined according to Equation (4).

$$FR = \frac{\max\left(\sum_{i=1}^{n} \mu_i \cdot Slot_{\text{available}}(i)\right)}{\sum_{i=1}^{l} \delta_i \cdot S_{\text{available}}(j)}$$
(4)

In Equation (4),  $\mu_i$  denotes the number of contiguous blocks of available slots for request i,  $Slot_{\rm available}(i)$  represents the number of available slots for that request,  $\delta_j$  denotes the total number of slots on link j, and  $S_{\rm available}(j)$  represents the total number of available slots in the network.

# 4.4. Baseline and Evaluation Procedure

The proposed 5GEON algorithm is compared against the TAB-FAA algorithm [Ahsan et al. 2024], which represents a state-of-the-art solution for traffic-aware

allocation in CF-RAN architectures over WDM networks. In addition, two variants of the proposed algorithm are evaluated: one employing fixed modulation formats and another incorporating adaptive modulation.

For each simulation scenario, multiple independent runs are performed to ensure statistical significance. Performance metrics are averaged across runs, and confidence intervals are computed. This evaluation methodology enables a fair comparison between the proposed solution and the baseline under identical traffic and network conditions.

# 5. Results

This section presents and discusses the results obtained from the simulation experiments. The performance of the proposed 5GEON algorithm is evaluated in terms of BBR, EE, and FR, as defined in Equations (1), (3), and (4), respectively. The results are compared against the TAB-FAA algorithm and two variants of the proposed solution, with and without adaptive modulation.

![](_page_9_Figure_5.jpeg)

**Figure 2. Bandwidth Blocking Ratio (BBR) computed according to Eq. (1).**

Figure 2 presents the BBR obtained according to Equation (1), which represents the fraction of the total requested bandwidth that could not be successfully allocated due to limitations in optical or processing resources. As illustrated in Figure 2, the TAB-FAA algorithm consistently exhibits higher blocking levels than 5GEON under all traffic loads. This behavior stems from its reliance on fixed spectrum allocation regions per traffic class, which reduces allocation flexibility and leads to premature resource exhaustion when heterogeneous bandwidth demands coexist in the network. In contrast, the proposed 5GEON algorithm substantially reduces bandwidth blocking by enabling flexible and multidimensional spectrum allocation while dynamically adapting resource usage to traffic class requirements. Moreover, the adoption of adaptive modulation further enhances network performance by improving spectral efficiency, allowing a larger amount of bandwidth to be transmitted using the same spectral resources. This gain becomes increasingly pronounced as network load grows, since higher contention intensifies spectrum fragmentation and limits contiguous slot availability. Under these conditions, the adaptive version of 5GEON mitigates fragmentation effects and exploits shorter transmission distances to select higher-order modulation formats, resulting in up to a threefold reduction in bandwidth blocking ratio when compared to the approach without modulation.

To further analyze the impact of traffic classification, Figure 3 presents the BBR computed separately for each 5G service class, according to Equation (1). The results in-

![](_page_10_Figure_1.jpeg)

**Figure 3. Bandwidth Blocking Ratio by Class.**

dicate that the proposed 5GEON algorithm achieves a substantial reduction in the blocking of URLLC traffic when compared to the baseline approach. This behavior directly reflects the effectiveness of the latency-aware offloading strategy, which prioritizes URLLC requests for processing at fog nodes and restricts path selection to low-delay routes, thereby reducing competition with less time-sensitive traffic. As a result, URLLC flows are less affected by spectrum contention and resource fragmentation. In contrast, eMBB and mMTC services exhibit higher blocking levels due to their more flexible latency constraints, which increase the number of competing requests and intensify contention for optical resources in the backhaul. However, the adaptive modulation variant of 5GEON significantly mitigates this effect by improving spectral efficiency, enabling more efficient packing of heterogeneous bandwidth demands and reducing the impact of spectrum fragmentation across traffic classes.

![](_page_10_Figure_4.jpeg)

**Figure 4. Energy Efficiency computed according to Eq. (3).**

Figure 4 presents the EE results obtained according to Equation (3), which mea-

sures the ratio between the accepted bandwidth and the energy consumed by optical network components. As shown in Figure 4, the 5GEON algorithm with adaptive modulation achieves the highest energy efficiency among the evaluated solutions. This result stems from its improved spectral efficiency and flexible resource allocation, which allow a larger number of traffic requests to be successfully accommodated without a proportional increase in energy consumption. Consequently, the energy expenditure of optical components is more effectively amortized over active connections. Conversely, the TAB-FAA algorithm exhibits the lowest energy efficiency due to its limited allocation flexibility and higher blocking levels, which lead to a significant fraction of energy being consumed by idle or underutilized optical resources.

![](_page_11_Figure_2.jpeg)

**Figure 5. Fragmentation Ratio computed according to Eq. (4).**

Figure 5 presents the FR results obtained according to Equation (4), which quantify the degree of spectrum fragmentation based on the distribution of available frequency slots across the network. As shown in Figure 5, solutions that accommodate a larger number of traffic requests tend to increase spectrum fragmentation due to the dynamic and heterogeneous occupation of frequency slots. In this context, the 5GEON algorithm without adaptive modulation exhibits higher fragmentation levels, since each request occupies wider spectral intervals, reducing slot contiguity along optical paths. In contrast, the adaptive modulation variant of 5GEON effectively mitigates spectrum fragmentation by allocating fewer frequency slots per connection, which preserves spectral contiguity and improves overall spectrum usability. The TAB-FAA algorithm achieves intermediate fragmentation levels, reflecting its limited allocation flexibility when handling heterogeneous traffic demands.

# 6. Conclusions

The continuous growth of mobile traffic and the increasing demand for latency-sensitive services pose significant challenges to current radio access and transport networks. In this context, optical networks play a fundamental role in supporting the stringent requirements of 5G services, particularly when combined with distributed processing architectures such as Cloud-Fog Radio Access Networks (CF-RAN).

5GEON is a routing and multidimensional optical resource allocation algorithm designed for CF-RAN architectures over Space-Division Multiplexing Elastic Optical Networks (SDM-EONs). The proposed solution jointly considers 5G traffic classification, latency-aware processing offloading, adaptive modulation, and multidimensional optical resource allocation.

Simulation results show that 5GEON outperforms a state-of-the-art baseline in terms of Bandwidth Blocking Ratio, Energy Efficiency, and Fragmentation Ratio. By integrating traffic differentiation with flexible optical resource management, the algorithm efficiently allocates fronthaul and backhaul resources while prioritizing Ultra-Reliable Low-Latency Communications (URLLC). Adaptive modulation further improves spectrum utilization, enabling up to three times more requests to be accommodated under high traffic load.

From a practical standpoint, these results indicate that 5GEON can be adopted by mobile network operators to improve transport network efficiency and service quality in 5G deployments, especially in dense and heterogeneous traffic scenarios. By dynamically adapting routing, modulation, and processing placement decisions, the proposed approach supports scalable and energy-efficient CF-RAN implementations while meeting strict latency requirements.

As future work, the model can be extended to incorporate protection and restoration mechanisms, alternative core and spectrum selection strategies, and learning-based approaches for traffic prediction and proactive resource allocation, as well as evaluated under different traffic distributions, failure scenarios, and emerging beyond-5G and 6G architectures.

# Acknowledgement

Research partially funded by CNPq (grants no. #305489/2023-2) and by the Sao Paulo ˜ Research Foundation (FAPESP), Brasil. Process Number 2025/03079-4.

# References

- Agarwal, A. K., Kaur, H., Rakesh, N., Rama Krishna, K., Kumar Dewangan, B., and Sahana, S. (2025). Energy-efficient optical network design for next-generation data centers. In *2025 Optical Communication, Photonics, Telecommunications, and Intelligent Machine Applications (OPTIMA)*, pages 195–201.
- Ahsan, M., Ahmed, A., Ekin, S., O'Hara, J., and Ahmad, A. (2024). Traffic-aware network slicing for 5g networks in cloud fog-ran over wdm architecture. In *2024 International Conference on Smart Applications, Communications and Networking (Smart-Nets)*, pages 1–6.
- Ahsan, M., Ahmed, A., Fida, H., Al-Dweik, A., Hashmi, U. S., and Ahmad, A. (2023). Efficient network slicing for 5g services in cloud fog-ran deployment over wdm network. *IEEE Transactions on Vehicular Technology*, 72(9):12099–12112.
- Aktar, M. R., Anower, M. S., Sakar, M. Z. I., Bappy, H. K., et al. (2024). Energy efficient bandwidth aware virtualized bbu pool for 5g c-ran. In *2024 6th International Conference on Electrical Engineering and Information & Communication Technology (ICEEICT)*, pages 84–88. IEEE.
- Al-Tarawneh, L., Alqatawneh, A., Tahat, A., and Saraereh, O. (2024). Evolution of optical networks: from legacy networks to next-generation networks. *Journal of Optical Communications*, 44(s1):s955–s970.

- Dias, I., Ruan, L., Ranaweera, C., and Wong, E. (2023). From 5g to beyond: Passive optical network and multi-access edge computing integration for latency-sensitive applications. *Optical Fiber Technology*, 75:103191.
- Dos Santos, M. R. P., Tinini, R. I., and Figueiredo, G. B. (2025). Energy-efficient flexible functional splitting in latency-constrained o-ran. *IEEE Transactions on Green Communications and Networking*, 10:1538–1551.
- dos Santos, M. R. P., Tinini, R. I., Januario, T. O., and Figueiredo, G. B. (2022). Deep recurrent neural network for optical fronthaul dimensioning and proactive vbbu placement in cf-ran. *Photonic Network Communications*, 43(1):59–73.
- Hafezi, M. and Ghaffarpour Rahbar, A. (2024). Fragmentation-aware with core classification algorithms for spectrum allocation in elastic optical networks-space division multiplexing (sdm-eon). *Optical Fiber Technology*, 82:103622.
- Hafezi, M. and Rahbar, A. G. (2024). Fragmentation-aware with core classification algorithms for spectrum allocation in elastic optical networks-space division multiplexing (sdm-eon). *Optical Fiber Technology*, 82:103622.
- Khorasani, Y., Ghaffarpour Rahbar, A., and Jafari-Beyrami, M. (2023). Fragmentation management to reduce bandwidth wastage in sdm-eon networks. *Photonic Network Communications*, 46(2):51–67.
- Liu, G., Ma, Y., Yang, X., and Sun, Q. (2024). Dynamic resource allocation for multicast service based on core node rerouting in sdm-eons. In *2024 7th International Conference on Mechatronics and Computer Technology Engineering (MCTE)*, pages 1716–1721.
- Moura, P. M. and Drummond, A. C. FlexGridSim: Flexible Grid Optical Network Simulator. http://www.lrc.ic.unicamp.br/FlexGridSim/.
- Santos, M., Tinini, R., Januario, T., and Figueiredo, G. (2021). Dimensionamento otimo ´ de fronthaul optico com divis ´ ao flex ˜ ´ıvel de func¸oes de processamento em cf-ran. ˜ In *Anais do XXXIX Simposio Brasileiro de Redes de Computadores e Sistemas Dis- ´ tribu´ıdos*, pages 210–223, Porto Alegre, RS, Brasil. SBC.
- Srinivas, A. M., Kumar, R., Barla, P., et al. (2024). Blocking triggered multi-path routing with spectrum retuning in elastic optical networks. *Optical Fiber Technology*, 83:103673.
- Vasundhara and Mandloi, A. (2024). Routing and dynamic core allocation with fragmentation optimization in eon-sdm. *Optical Fiber Technology*, 83:103658.
- Wang, Y., Kong, L., Zhu, M., Gu, J., Cai, Y., and Zhang, J. (2024). Availability-aware and delay-sensitive ran slicing mapping based on deep reinforcement learning in elastic optical networks. *IEEE Transactions on Network and Service Management*.
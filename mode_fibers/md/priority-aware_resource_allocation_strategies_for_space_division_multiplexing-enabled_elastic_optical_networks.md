---
title: "Priority-Aware Resource Allocation Strategies for Space Division Multiplexing-enabled Elastic Optical Networks"
tema_principal: mode_fibers
temas_relacionados: []
ano: null
autores: []
veiculo: null
pdf: ../pdf/priority-aware_resource_allocation_strategies_for_space_division_multiplexing-enabled_elastic_optical_networks.pdf
---

# Priority-Aware Resource Allocation Strategies for Space Division Multiplexing-enabled Elastic Optical Networks

1st Devlina Adhikari

*Dept. of Information and Technology Pandit Deendayal Energy University* Gandhinagar, India devlina 2008@ymail.com

2nd Aishwarya Raj Dept. of Electronics and Communication *Pandit Deendayal Energy University* Gandhinagar, India aishwaryaraj3004@gmail.com

3rd Mfashigihe Seth Dept. of Information and Technology *Pandit Deendayal Energy University* Gandhinagar, India Mfashigihe.sict20@sot.pdpu.ac.in

*Abstract*—In the rapidly expanding domain of digital communications, the soaring demand for data-intensive applications such as the Internet of Things (IoT), high-definition video streaming, and cloud-based services has sparked a pressing need for increased optical network capacity. Elastic Optical Networks (EONs), with their flexible bandwidth allocation capabilities, have emerged as a promising solution to accommodate this data surge. However, traditional single-mode fiber infrastructures are nearing their capacity limits, prompting the exploration of advanced techniques to boost network scalability and efficiency. Space Division Multiplexing (SDM), particularly through the use of multicore fibers (MCFs), offers a transformative approach by enabling parallel transmission paths and significantly enhancing spectral efficiency. Within this context, the incorporation of priority-based resource allocation becomes essential for optimizing the performance of SDM-EONs. By intelligently assigning resources based on traffic priority, networks can ensure service differentiation, reduce blocking probability for high-priority demands, and maintain quality of service under dynamic conditions. This paper investigates the integration of SDM into EONs alongside priority-aware strategies, highlighting their combined potential to address growing bandwidth demands and provide a foundation for resilient, future-proof optical infrastructures.

*Index Terms*—Elastic Optical Network (EON), Space division Multiplexing (SDM), Routing Modulation Spectrum and Core Allocation (RMSCA), Priority-based Resource Allocation, Multicore fiber (MCF).

## I. INTRODUCTION

With the rapid growth of data-intensive applications such as cloud computing, video streaming, and IoT services, today's communication networks are under increasing pressure to deliver higher capacity, better flexibility, and improved efficiency [1]. To meet these demands, Elastic Optical Networks (EONs) have emerged as a promising solution. In particular, the integration of Space Division Multiplexing (SDM) into EONs has gained attention for its ability to significantly boost transmission capacity by exploiting the spatial domain [2].

SDM-EONs utilize Multi-Core Fibers (MCFs), where multiple optical cores within a single fiber allow parallel light paths to be transmitted simultaneously [3]. This spatial parallelism provides a substantial increase in bandwidth, making SDM-EONs a strong candidate for next-generation optical networks. However, this architectural advantage also introduces several resource management challenges. These include how to efficiently assign routes, modulation formats, spectrum slots, and cores, while also considering physical constraints like crosstalk and core isolation.

Over the past few years, many researchers have proposed different resource allocation strategies for SDM-EONs. These include traditional routing and spectrum allocation techniques [4], core and modulation format assignment, and approaches that reduce crosstalk and improve load balancing [5]. More recent works have introduced machine learning-based algorithms [6], as well as heuristics for fragmentation and blocking probability reduction. Despite these advancements, many of these strategies are not tailored to differentiate between traffic types based on priority, which is a crucial aspect in real-world scenarios.

![](_page_0_Figure_14.jpeg)

Fig. 1. Examples of different SDM fiber structures and the corresponding spatial mode patterns. (a) Single-core, single-mode fiber; (b) Seven-core MCF; (c) Few-mode fiber; (d) Ring-core fiber with OAM modes; (e) Three-core FM-MCF; (f) Heterogeneous-core MCF [7]

Recent advancements made by researchers in [7] in fiber design have enabled the deployment of multiple spatial channels within a single fiber structure, making Space Division Multiplexing (SDM) a promising solution to overcome the limitations of conventional single-core systems. Fig 1 illustrates various types of fibers used in SDM, including multicore fibers (MCFs), few-mode fibers (FMFs), and hybrid structures, along with the corresponding spatial modes they support. These structures demonstrate the diversity of mode propagation possibilities, which are central to achieving highcapacity and scalable optical networks.

This paper focuses on the design and evaluation of a priority-based resource allocation strategy in SDM-EONs. The main objective is to reduce bandwidth wastage and blocking probabilities while improving overall network performance by considering traffic priority during allocation. Demands with higher importance, such as real-time or emergency traffic, should be given preference over less critical data. By introducing such a mechanism, the network can become more responsive, reliable, and efficient, particularly during high-load situations.

To test this approach, a simulation framework was developed using Python. The simulation models a realistic SDM-EON environment, including network topology, dynamic traffic generation, and a custom allocation algorithm. The algorithm reads each demand from a traffic file, checks resource availability along pre-computed paths, and allocates slots based on traffic priority. If a path is not available, alternative paths are considered, and if no feasible option exists, the demand is marked as blocked.

The simulation uses various input files such as adjacency matrices and pre-computed k-shortest paths, and outputs files like allocation matrices and blocked connections. Metrics such as blocking probability and link utilization are calculated to assess the network's performance under different traffic conditions.

The paper aims to make several contributions. First, it demonstrates how priority-based allocation can reduce the number of blocked demands in an SDM-EON. Second, it highlights the importance of dynamic, intelligent resource management strategies in large-scale optical networks. Finally, it provides a practical simulation environment that can be extended in future research to include machine learning, encryption, or fault-tolerant mechanisms.

Additionally, the work explores advanced reservation techniques and multipath routing strategies to further improve reliability and efficiency. By allowing demands to reserve resources ahead of time or use multiple paths, the network can better handle bursty or mission-critical traffic. These methods are particularly useful for applications requiring guaranteed bandwidth or low latency, such as healthcare, finance, or disaster recovery systems.

In summary, this work aims to improve SDM-EON performance by introducing a realistic, priority-based resource allocation framework. By combining detailed simulation, algorithm development, and empirical analysis, the project provides useful insights into how modern optical networks can evolve to meet increasing data demands in a cost-effective and efficient manner. We also present a brief survey of recent work in SDM-EON resource management, identifying key gaps and motivations for our approach.

The remainder of this paper is structured as follows: Section

II presents a comprehensive review of related work in SDM-EON resource allocation. Section III describes the system model and outlines the problem formulation. Section IV details the proposed priority-based allocation algorithm and the simulation environment. Section V discusses the simulation results and performance evaluation. Section VI highlights key observations and outlines future research directions. Finally, Section VII concludes the paper with a summary of findings and contributions.

## II. RELATED WORK

Space Division Multiplexing (SDM) in Elastic Optical Networks (EONs) has emerged as a transformative solution to address the growing bandwidth demands of modern dataintensive applications. SDM-EONs combine the flexibility of elastic bandwidth allocation with the high-capacity advantages of spatial multiplexing, enabling enhanced spectral efficiency and scalability. However, the complexity of managing resources—especially under varying traffic demands and service priorities—has driven extensive research into more efficient, priority-aware allocation mechanisms.

- A significant contribution to this domain was made by the researchers in [8], who introduced a routing, modulation, core, and spectrum allocation (RMCSA) algorithm using a score function. This method specifically addressed the dual challenges of crosstalk and fragmentation, two critical factors in SDM-EON performance. By balancing these impairments, their approach improved both spectral efficiency and connection success rates.
- Building on this foundation, the work in [3] proposed machine learning-assisted resource allocation strategies. Two key methods—Tridental Resource Assignment (TRA) and Spectrum Wastage Avoidance-based Resource Allocation (SWARM)—were designed to dynamically adapt to changing traffic conditions and network states. These techniques significantly reduced bandwidth blocking probabilities. In a related direction, Mrad et al. in [9] developed an assignment-based heuristic tailored for routing and spectrum assignment in multi-core fiber networks. Their method was shown to be effective in handling largescale internet traffic, offering improvements in cost and operational efficiency.
- The authors in [10] focused on enhancing path diversity and spectral usage through a fragmentation-aware, loadbalanced RMSCA algorithm. Their solution addressed physical-layer limitations and provided better load distribution, making it well-suited for complex SDM-EON topologies.
- Survivability and proactive resource planning were explored in [11], where a novel RSCA scheme with advance reservation was proposed. This offline strategy allowed better spectrum preparation and fault tolerance in highpriority scenarios. Complementing this, the study in [12] introduced a priority-aware traffic routing and resource allocation (P-TRRA) mechanism. By differentiating between service classes—such as premium, emergency, or

best-effort—their model ensured that high-priority traffic maintained quality of service even under congestion.

- Further emphasizing network resilience, the authors in [13] discussed resilient routing strategies as a foundation for future SDM-EON networks. Their research highlighted the need for robust, fault-tolerant systems capable of handling dynamic and bursty traffic patterns. In [14], another study explored the handling of high- and lowpriority traffic within multi-layer network architectures. Their work proposed differentiated treatment policies to preserve service continuity for mission-critical data under stressed conditions.
- To address signal degradation in dense traffic environments, the impairment-aware model in [15] incorporated both nonlinear effects and service priorities during spectrum allocation. This approach aimed to reduce quality loss while meeting diverse service requirements. The integration of artificial intelligence was also advanced in [15], where deep reinforcement learning was used to automate and scale service function chains. Their model responded in real-time to traffic changes, optimizing network resource utilization and performance.
- Resilient routing was extended to the domain of mobile and 5G networks in [17], where SDM-EONs were shown to offer critical advantages for access network survivability. At the same time, [18] proposed a novel scheme that enabled the coexistence of protected and unprotected services using idle slot reuse, improving spectrum efficiency without compromising protection.
- Traffic modeling and control mechanisms were further examined in [19], where the authors analyzed call admission control based on priority. Their simulations demonstrated how differentiated admission policies affected blocking probabilities and load balancing. Lastly, the work in [20] proposed a method for deploying automatic hidden optical bypasses in multilayer networks. This mechanism allowed the dynamic rerouting of data through less-congested paths, thereby enhancing continuity and service reliability without manual reconfiguration.

Together, these studies highlight the progress and ongoing challenges in building efficient, reliable, and intelligent SDM-EON infrastructures. The integration of advanced algorithms, AI techniques, and resilience-focused designs plays a key role in addressing the complex requirements of future high-speed optical communication systems.

# III. METHODOLOGY

In this study, we develop and analyze a simulation framework designed to evaluate priority-based resource allocation in Spatial Division Multiplexing - Elastic Optical Networks (SDM-EON). The aim is to enhance network efficiency by effectively managing the allocation of optical resources among competing demands, prioritizing based on predetermined criteria. This section details the simulation environment, data preparation, algorithmic processes, and the metrics used to assess performance.

The simulation is implemented in Python, a versatile programming language favored for its readability and extensive support of numerical and scientific computing libraries. We utilize NumPy for its efficient array operations, which are crucial for managing large datasets and matrix manipulations representative of network states. The file module is employed for reading and writing data, allowing for easy interchange of input parameters and results.

The network within the simulation is represented as a set of nodes interconnected by links, where each link has a certain number of slots available. These slots represent the smallest unit of network resource that can be allocated to a demand. The network's state is dynamically updated and is central to determining the feasibility of accommodating new demands as they arise. Traffic demands are synthetically generated to simulate various network loading scenarios. Each demand specifies a source node, a destination node, and the number of slots required. These demands are stored in a file, which serves as the primary input for the simulation. This approach allows the simulation to be tailored to different hypothetical or real-world traffic patterns.

The network within the simulation is represented as a set of nodes interconnected by links, as illustrated in Fig 2. Each link has a certain number of slots available, which represent the smallest unit of network resource that can be allocated to a demand. Potential paths between nodes are

![](_page_2_Picture_12.jpeg)

Fig. 2. Network topology used in the simulation, consisting of six interconnected nodes with varying link distances.

pre-computed and stored in file by K-shortest path method employed to get the three shortest path from source-destination pair. This file includes information on the paths available for each node pair and the links that constitute these paths. By pre-computing the paths, the simulation can efficiently assess each demand against available resources without recalculating routes dynamically, which can be computationally expensive.

Figure 3 presents an overview of the complete simulation workflow. After initializing the topology, path data, and traffic demands, the simulation iteratively processes each demand. For every request, the algorithm checks the priority level and evaluates whether any of the precomputed paths can accommo-

![](_page_3_Figure_0.jpeg)

Fig. 3. Flowchart illustrating the priority-based resource allocation process used in SDM-EON simulation.

date the required slots. If a suitable path is found, the demand is allocated and network state is updated; otherwise, the demand is logged as blocked. This process continues until all demands are evaluated, after which metrics such as Blocking Probability Ratio (BPR) and utilization are computed. The core of our methodology lies in the resource allocation algorithm, which processes each demand in sequence and attempts to find a viable path that can accommodate it based on current network conditions.

As each demand is read from the input file, the algorithm assesses its source, destination, and slot requirements. The demand's priority level is considered the shortest path from source to destination. If the first path is not available, the rest two paths are checked for allocation and further process. For each demand, the algorithm evaluates each available path:

- Capacity Check: It first checks if the path has enough unallocated slots to meet the demand.
- Slot Allocation: If the path can accommodate the demand, the slots are marked as occupied from the source to the destination for the duration required.
- Priority Handling: If multiple paths can satisfy the demand, the one with the highest priority (based on some

metric like least used or shortest path) is chosen.

If no paths can accommodate a demand, it is marked as blocked. The simulation tracks these events carefully to analyze the network's performance under stress. Blocked demands may be queued for rerouting attempts, where the algorithm waits for the release of slots from completed transmissions or explores less direct paths that might have become viable. The simulation outputs detailed logs of each operational step, including the decisions made for each demand, the paths chosen, the slots allocated, and any blocks encountered. These logs are crucial for debugging and for validating the simulation model.

#### IV. RESULTS AND DISCUSSION

The simulation results of the priority-based resource allocation in Space Division Multiplexed Elastic Optical Networks (SDM-EONs) offer valuable insights into the efficiency and practicality of the implemented algorithms. This section analyzes the outcomes using data generated from various output files and visual representations, focusing on demand satisfaction, blocking probabilities, resource utilization, and overall network performance under varying traffic loads.

#### A. Traffic Demand Allocation and Blocking

One of the key objectives of the simulation was to evaluate the network's ability to accommodate incoming traffic demands under a priority-based allocation mechanism. Each demand, as defined in the traffic file, included asource, destination, and the number of required frequency slots.

The simulation attempted to fulfill these demands while adhering to resource availability and priority constraints. Successfully allocated demands were recorded, while unfulfilled requests were stored in the file.

*Blocking Patterns:* Analysis of blocked demands revealed the following:

- Peak-Time Overloads: A noticeable increase in blocking was observed during peak traffic periods, highlighting capacity constraints in key network segments and a higher probability of contention.
- Low-Traffic Performance: During low-demand intervals, the network exhibited improved performance. While some blockages still occurred, they primarily affected low-priority demands, suggesting that the prioritization mechanism was effective in safeguarding critical traffic.

The *blocking probability ratio* was calculated using the following formula:

**Blocking Probability Ratio** = 
$$\frac{Number\ of\ Blocked\ Connections}{Total\ Number\ of\ Demands}$$
 (1)

This metric quantifies the network's failure rate in fulfilling demands and is a core indicator of algorithmic effectiveness.

## *B. Blocking Probability Analysis*

To evaluate the impact of traffic demand on network performance, a comparison of the Blocking Probability Ratio (BPR) was conducted across three network configurations: traditional EON, PB-EON (Priority-Based EON), and PB SDM-EON (Priority-Based SDM-EON). The BPR was computed for increasing levels of traffic demand.

![](_page_4_Figure_2.jpeg)

Fig. 4. Comparison of Blocking Probability Ratio (BPR) vs Traffic Demand across EON, PB-EON, and PB SDM-EON configurations.

As seen in Fig. 4, the PB SDM-EON configuration consistently achieved the lowest blocking probability, particularly under low-traffic conditions. While traditional EON lacks prioritization and spatial flexibility, both PB-EON and PB SDM-EON improved the handling of high-priority traffic. Although PB-EON introduced a priority mechanism, it still saw higher overall blocking—mainly due to the deliberate rejection of low-priority demands to accommodate critical ones. This trade-off improved service for important traffic but raised the total blocking rate. PB SDM-EON, by combining priority awareness with spatial resources via multicore fibers, reduced blocking more effectively. It maintained minimal blocking in light traffic and prioritized high-priority demands under heavier loads, with most rejections affecting only low-priority traffic. This demonstrates more efficient resource utilization and stronger service differentiation.

Overall, these results highlight the benefits of integrating spatial and priority-based strategies. Notably, for demand levels below 250, PB SDM-EON maintained near-optimal performance, reflecting its scalability and suitability for dynamic network environments.

# *C. Visualization of a Successfully Allocated Demand*

Fig 5 shows a real result from the simulation, where the algorithm successfully allocated a demand from node 1 to node 4. The red-highlighted path corresponds to the optical links that were chosen based on availability and priority rules at the time of simulation. This result confirms that the implemented algorithm is capable of identifying valid paths and assigning

![](_page_4_Figure_9.jpeg)

Fig. 5. Result of a successfully allocated demand between nodes 1 and 4

resources efficiently within the constraints of the network topology.

## *D. Network Utilization Analysis*

Key findings include:

- Utilization Rates: Certain links exhibited consistently high usage, indicating traffic hotspots or inefficient routing convergence.
- Load Distribution: The spread of slot allocation showed that the algorithm attempted to balance load, although improvement is possible through better route diversity.
- Allocation Efficiency: Time-based intervals between successive allocations helped evaluate the network's responsiveness to dynamic traffic — shorter intervals with high fulfillment indicate faster processing and better adaptability.

# *E. Design Implications and Future Scope*

- Priority System Effectiveness: The algorithm successfully prioritized high-priority demands, although occasional blockages indicate scope for enhancing the fairness and adaptability of the mechanism.
- Scalability Concerns: Under simulated high-traffic loads, performance degradation was observed at congested nodes and links, pointing to the need for more scalable architectures and possibly multicore-aware parallel path provisioning.
- Distance-Adaptive Mechanism Integration: Insights from allocation and blocking patterns suggest that integrating distance-adaptive modulation and routing mechanisms could improve spectral efficiency and reduce congestion, particularly for longer paths in dense traffic scenarios.

# V. CONCLUSION

This paper presents a focused review of recent advances in resource allocation for Space Division Multiplexing-enabled Elastic Optical Networks (SDM-EONs), with an emphasis on priority-aware strategies. The survey explored various techniques including routing and spectrum assignment algorithms, core selection methods, and mechanisms to reduce crosstalk and fragmentation. Special attention was given to approaches that support service differentiation based on traffic criticality—an essential requirement in practical optical networks.

To support the literature, a small-scale simulation was implemented in Python to evaluate the effectiveness of prioritybased resource allocation. Using network topology, precomputed k-shortest paths, and dynamic traffic demands, a custom algorithm allocated resources based on availability and demand priority. Key performance metrics such as blocking probability and slot utilization were analyzed under varying traffic loads.

The results demonstrated that incorporating priority significantly improves allocation efficiency and ensures better service for critical traffic. This simple yet effective experiment validates insights from the literature and underscores the value of priority-aware mechanisms in SDM-EONs. Together, the survey and simulation highlight the importance of intelligent allocation strategies for scalable and efficient optical networking.

# REFERENCES

- [1] B. C. Chatterjee, N. Sarma, and E. Oki, "Routing and Spectrum Allocation in Elastic Optical Networks: A Tutorial," *IEEE Commun. Surv. Tutor.*, vol. 17, no. 3, pp. 1776–1800, 2015, doi: 10.1109/COMST.2015.2431731.
- [2] J. Wang, S. Chen, Q. Wu, Y. Tan, and M. Shigeno, "Solving the Static Resource-Allocation Problem in SDM-EONs via a Node-Type ILP Model," *Sensors*, vol. 22, no. 24, p. 9710, Dec. 2022, doi: 10.3390/s22249710.
- [3] S. Petale and S. Subramaniam, "Advanced Resource Allocation Strategies for MCF-based SDM-EONs: Crosstalk Aware and Machine Learning Assisted Algorithms," in *2023 23rd International Conference on Transparent Optical Networks (ICTON)*, Bucharest, Romania, Jul. 2023, pp. 1–4, doi: 10.1109/ICTON59386.2023.10207504.
- [4] H. M. N. Da S. Oliveira and N. L. S. Da Fonseca, "Backup, Routing, Modulation, Spectrum and Core Allocation in SDM-EON for Efficient Spectrum Utilization," in *2022 IEEE Latin-American Conference on Communications (LATINCOM)*, Rio de Janeiro, Brazil, Nov. 2022, pp. 1–6, doi: 10.1109/LATINCOM56090.2022.10000434.
- [5] B. S. Heera, A. Sharma, V. Lohani, and Y. N. Singh, "Crosstalk Compliant Routing, Modulation, Core and Spectrum Assignment Techniques in SDM-EON," in *2022 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)*, Gandhinagar, India, Dec. 2022, pp. 261–264, doi: 10.1109/ANTS56424.2022.10227766.
- [6] R. Jashvantbhai Pandya, "Machine learning-oriented resource allocation in C + L + S bands extended SDM-EONs," *IET Commun.*, vol. 14, no. 12, pp. 1957–1967, Jul. 2020, doi: 10.1049/iet-com.2019.1191.
- [7] Marom, Dan and Blau, Miri. (2015). Switching solutions for WDM-SDM optical networks. Communications Magazine, IEEE. 53. 60-68. 10.1109/MCOM.2015.7045392.
- [8] J. L. Ravipudi and M. Brandt-Pearce, "A Score Function Heuristic for Crosstalk- and Fragmentation-Aware Dynamic Routing, Modulation, Core, and Spectrum Allocation in SDM-EONs," in *2022 IEEE Future Networks World Forum (FNWF)*, Montreal, QC, Canada, Oct. 2022, pp. 83–87, doi: 10.1109/FNWF55208.2022.00023.
- [9] M. Mrad, U. S. Suryahatmaja, A. O. Elsayed, A. Gharbi, and M. A. Esmail, "Assignment-based heuristic for SDM Networks with Multi-Core Fibers," in *2022 5th International Conference on Advanced Systems and Emergent Technologies (IC ASET)*, Hammamet, Tunisia, Mar. 2022, pp. 279–284, doi: 10.1109/IC ASET53395.2022.9765950.
- [10] Q. Lan, Y. Cai, S. Chen, X. Chen, and J. Shen, "A Fragmentation-Aware Load-Balanced RMSCA Algorithm in Space-Division Multiplexing Elastic Optical Networks," in *2022 3rd Information Communication*

- *Technologies Conference (ICTC)*, Nanjing, China, May 2022, pp. 56–60, doi: 10.1109/ICTC55111.2022.9778371.
- [11] J. Halder, T. Acharya, and U. Bhattacharya, "A Novel RSCA Scheme for Offline Survivable SDM-EON With Advance Reservation," *IEEE Trans. Netw. Serv. Manag.*, vol. 19, no. 2, pp. 804–817, Jun. 2022, doi: 10.1109/TNSM.2022.3142857.
- [12] R. da S. Lopes, D. L. do Rosario, E. C. Cerqueira, H. M. N. da Silva ´ Oliveira, and S. Zeadally, "Priority-aware traffic routing and resource allocation mechanism for space-division multiplexing elastic optical networks," *Computer Networks*, vol. 218, p. 109389, Dec. 2022, doi: 10.1016/j.comnet.2022.109389.
- [13] R. S. Lopes and H. M. N. S. Oliveira, "Resilient Routing for SDM-EON as a Crucial Enabler for the Future Networks," in *Anais do V Workshop de Computac¸ao Urbana (CoUrb) ˜* , 2023, pp. 139–152, doi: 10.5753/courb.2023.230185.
- [14] E. Biernacka, P. Boryło, P. Jurkiewicz, R. Wojcik, and J. Dom ´ zał, ˙ "Handling high- and low-priority traffic in multi-layer networks," *Bull. Pol. Ac.: Tech.*, vol. 70, no. 2, p. e141091, 2022, doi: 10.24425/bpasts.2022.141091.
- [15] K. Munasinghe, N. K. D. Dharmaweera, R. Parthiban, and Y. A. S¸ ekerciolu, "Novel impairment-aware resource allocation scheme for elastic optical networks serving traffic with different service priorities," *IET Commun.*, vol. 18, no. 3, pp. 200–210, 2024, doi: 10.1049/cmu2.12781.
- [16] X. Kong and L. Peng, "Priority-Aware Deployment of Autoscaling Service Function Chains Based on Deep Reinforcement Learning," *J. Netw. Netw. Appl.*, vol. 4, no. 2, pp. 94–101, 2024.
- [17] R. S. Lopes and H. M. N. S. Oliveira, "Resilient Routing for SDM-EON as a Crucial Enabler for the 5G Access Networks," in *2022 IEEE Latin-American Conference on Communications (LATINCOM)*, Rio de Janeiro, Brazil, Nov. 2022, pp. 1–6, doi: 10.1109/LATIN-COM56090.2022.10000418.
- [18] M. M. L. Cavalcanti, G. W. Teixeira, H. A. Dinarte, R. C. Almeida Jr., R. Boutaba, and D. A. R. Chaves, "Enhancing the Efficiency of Resilient Multipath-Routed Elastic Optical Networks: A Novel Approach for Coexisting Protected and Unprotected Services with Idle Slot Reuse," *Sensors*, vol. 24, no. 12, p. 3965, 2024, doi: 10.3390/s24123965.
- [19] P. Boryło, R. Wojcik, J. Dom ´ zał, and E. Biernacka, "Simulation ˙ Analysis of Traffic Characteristics of Elastic Optical Network Nodes with Priority-Based Call Admission Control Mechanisms," in *2023 23rd International Conference on Transparent Optical Networks (IC-TON)*, Bucharest, Romania, Jul. 2023, pp. 1–4, doi: 10.1109/IC-TON59386.2023.10207575.
- [20] E. Biernacka, R. Wojcik, P. Jurkiewicz, and J. Dom ´ zał, "Automatic Hid- ˙ den Elastic Optical Bypasses in Multi-Layer Networks," *IEEE Access*, vol. 10, pp. 55694–55705, 2022, doi: 10.1109/ACCESS.2022.3177439.
- [21] S. Petale, J. Zhao, and S. Subramaniam, "TRA: an efficient dynamic resource assignment algorithm for MCF-based SS-FONs," *J. Opt. Commun. Netw.*, vol. 14, no. 7, pp. 511–523, 2022.
- [22] S. Zhang and K. L. Yeung, "Revisiting the modulation format selection problem in crosstalk-aware sdm-eons," *Computer Networks*, vol. 221, p. 109524, 2023, doi: 10.1016/j.comnet.2022.109524.
- [23] S. Zhang and K. L. Yeung, "Efficient embedding of Service Function Chains in space-division multiplexing elastic optical networks," *Computer Networks*, vol. 233, p. 109869, 2023, doi: 10.1016/j.comnet.2023.109869.
- [24] Y. Ma, C. Zhang, Z. Zhang, Y. Wang, and J. Lin, "Dynamic resource allocation for multicast in SDM-EON: time-decoupled dynamic path cross talk and joint weight," *J. Opt. Commun. Netw.*, vol. 15, no. 9, pp. 687–699, 2023.
- [25] S. Petale and S. Subramaniam, "Machine learning aided optimization for balanced resource allocations in SDM-EONs," *J. Opt. Commun. Netw.*, vol. 15, no. 5, pp. B11–B22, 2023.
- [26] U. Enendu, J. Ncube, and A. Asiya, "Anycast Transmission in Routing Modulation Level Spectrum Assignment (RMLSA) Problem on Space Division Multiplexing (SDM) Elastic Optical Networks (EON)," *Journal of Computer and Communications*, vol. 10, pp. 14–44, 2022, doi: 10.4236/jcc.2022.105002.
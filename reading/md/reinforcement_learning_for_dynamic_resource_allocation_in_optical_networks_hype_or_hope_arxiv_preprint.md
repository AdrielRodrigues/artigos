---
title: "Reinforcement Learning for Dynamic Resource Allocation in Optical Networks: Hype or Hope?"
tema_principal: reading
temas_relacionados: []
ano: 2024
autores: []
veiculo: null
pdf: ../pdf/reinforcement_learning_for_dynamic_resource_allocation_in_optical_networks_hype_or_hope_arxiv_preprint.pdf
---

# **Reinforcement Learning for Dynamic Resource Allocation in Optical Networks: Hype or Hope?**

**MICHAEL DOHERTY**1\* **, ROBIN MATZNER**<sup>1</sup> **, RASOUL SADEGHI**<sup>1</sup> **, POLINA BAYVEL**<sup>1</sup> **, AND ALEJANDRA BEGHELLI**<sup>1</sup>

<sup>1</sup>*Optical Networks Group, University College London, Torrington Place, London WC1E 7JE, United Kingdom*

*Compiled April 23, 2025*

**The application of reinforcement learning (RL) to dynamic resource allocation in optical networks has been the focus of intense research activity in recent years, with almost 100 peer-reviewed papers. We present a review of progress in the field, and identify weaknesses in benchmarking practices and reproducibility. To demonstrate best practice, we exactly recreate the problem settings from five landmark papers and apply improved benchmarks. To determine the best benchmarks, we evaluate several heuristic algorithms and optimize the candidate path count and sort criteria for path selection. We apply the improved benchmarks and demonstrate that simple heuristics outperform the published RL solutions, often with an order of magnitude lower blocking probability. Finally, to estimate the limits of improvement on the benchmarks, we present empirical lower bounds on blocking probability using a novel defragmentationbased method. Our method estimates that traffic load can be increased by 19–36% for the same blocking in our examples, which may motivate further research on optimized resource allocation. We make our simulation framework and results openly available to promote reproducible research and standardized evaluation https://doi.org/10.5281/zenodo.12594495.**

<http://dx.doi.org/10.1364/ao.XX.XXXXXX>

# **1. INTRODUCTION**

Network operators are faced with a problem: how to increase capacity for fast-growing data traffic without increasing the price of services [\[1\]](#page-10-0). Advances in transmission technology have so far provided the solution by exponentially increasing the point-topoint capacity of the optical channel. However, as the throughput of the installed C+L bands approaches the nonlinearitylimited information bounds [\[2\]](#page-10-1), costly infrastructure upgrades are required to scale capacity through spatial division multiplexing or ultra-wideband transmission [\[3\]](#page-10-2). Operators seek to minimize or delay the required capital expenditure and offset it with reduced operational costs. Online optimization of network resource allocation offers a path towards these aims by increasing the achievable network throughput with dynamic and automated service provisioning.

Reinforcement learning (RL) has emerged as a promising technique for dynamic resource allocation (DRA) from a range of exact solution methods, heuristic algorithms, and artificial intelligence (AI) approaches. RL solutions can approach the quality of exact methods such as integer linear programming (ILP), with an online allocation time comparable to simple heuristics [\[4\]](#page-11-0). In fact, many works have demonstrated RL solutions that are superior to selected heuristics across various optical network

problems (see section [3\)](#page-2-0).

However, despite the many papers that investigate RL for optical networks, adoption of machine learning (ML) techniques by network operators has been limited by non-technological barriers [\[5\]](#page-11-1). One barrier is a lack of clear benchmarks and demonstrable benefits. Studies of resource allocation problems in optical networks often present results on specific topologies and traffic models, without fair comparison to previous results. Often results are not generalizable.

In this paper we address this barrier by providing analysis of and recommendations for benchmarking practices. We identify 5 papers that provide the best examples of benchmarking in the field and exactly recreate their problem settings. By "problem settings", we mean the exact network topologies, traffic models, and other details of the network simulations. We then evaluate a range of heuristic algorithms and apply the best to each case. The best heuristic algorithms outperform or equal the reported RL results in all cases.

To understand if it is possible to improve on these new benchmarks, we propose a heuristic-based lower bound network blocking estimation method, termed Resource-Prioritized Defragmentation (section [6\)](#page-8-0). For each case of study, we apply this method over a range of traffic loads and estimate that the supported traffic load at a fixed blocking (0.1%) may be increased by

<sup>\*</sup>*Corresponding author: michael.doherty.21@ucl.ac.uk*

19-36% for flex-grid networks. These estimates suggest further improvement is possible.

This is the first time that a thorough analysis and benchmarking of previous work has been carried out, and highlights deficient benchmarking standards. Our findings suggest that previous attempts to find better resource allocation policies using RL have been unsuccessful, and new efforts are required to find solutions, using RL or other methods, that improve on the best benchmarks and approach the estimated bounds.

This paper aims to: 1) Promote higher standards for evaluation and benchmarking in research on RL for DRA. 2) Improve reproducibility and transparency of research by open sourcing our simulation framework and providing discussion of implementation details that significantly affect results (e.g. path ordering in Section 4[.A](#page-4-0) and holding time truncation in Section 5[.A\)](#page-6-0). 3) Encourage new research into optimized DRA by demonstrating that previous RL approaches have failed to beat our benchmarks but there remains a considerable optimality gap between the benchmarks and our estimated bounds.

The contributions of this work are:

- 1. A comprehensive survey of progress on RL approaches to DRA in optical networks.
- 2. A systematic study of the factors affecting heuristic algorithm performance and recommendations for better heuristic benchmarks.
- 3. A recreation of problems from five landmark papers in the field with comparisons to improved heuristic benchmarks, showing previous RL results have failed to improve on heuristics.
- 4. The introduction of a novel empirical throughput bound estimation method, which shows benchmarks can be improved.
- 5. The release of our simulation framework, "XLRON", to promote reproducible research and enable fair comparison across different studies.

All of the code necessary to generate data and plots from this paper are available on Github [\[6\]](#page-11-2).

We begin with essential background on DRA problems and RL techniques in Section 2, followed by a literature review in Section 3. Section 4 presents the investigation of heuristic algorithms for benchmarking. Section 5 details the analysis of the previously published results and comparison with benchmarks. Section 6 presents new empirical bounds for network throughput, with recommendations for future research directions in Section 7.

# <span id="page-1-0"></span>**2. BACKGROUND**

# **A. DRA problems in optical networks**

# *Motivation for dynamic operation and RL*

As discussed by Augé [\[7\]](#page-11-3) and Pointurier [\[8\]](#page-11-4), optical networks must operate with a margin of additional resources between the minimum requirements to fulfill a data service request and the resources allocated to that request, for example by allocating additional spectrum. This margin is required due to uncertainty in physical parameters of the transmission network or future traffic variations. Reducing the margin can increase the network throughput or reduce costs.

Dynamic operation allows the allocated resources to vary temporally in response to shifting traffic, thereby allowing more accurate matching of resources to current demand, which reduces margins. The time constraints of dynamic operation may preclude exact solution methods, but a trained RL agent can compute an allocation in sub-second time [\[4\]](#page-11-0).

RL is appropriate for these problems because they possess three characteristics that merit the application of AI [\[9\]](#page-11-5): 1) a large combinatorial search space, 2) a clear objective function for optimization, and 3) plentiful training data and/or accurate and efficient simulators for data generation.

#### *Traffic models*

Network traffic comprises a set of requests to connect source and destination nodes with fixed data rates on dedicated lightpaths. Traffic can be modeled as static, incremental, or dynamic [\[10\]](#page-11-6).

Static traffic assumes knowledge of all connection requests that the network must accommodate. Incremental traffic lies between static and dynamic in stochasticity: requests are not known in advance but do not expire once allocated. For dynamic traffic, connection requests are served on-demand without knowledge of future requests, and active connections expire randomly. The request arrival and expiry times are sampled from probability distributions, often assumed to be exponential [\[11\]](#page-11-7). Dynamic traffic is considered a paradigm for future optical networks, that have the necessary systems in place to enable real-time response to changing network conditions [\[12\]](#page-11-8).

#### *Problem variants*

The classic optimization problem in an optical network is Routing and Wavelength Assignment (RWA) for fixed-grid networks or Routing and Spectrum Assignment (RSA) for flex-grid networks, where spectrum is divided into frequency slot units (FSU) [\[13\]](#page-11-9). Further degrees of freedom in the optimization are added by considering the selection of Modulation formats (RMSA), and the fiber Core or spectral transmission Band utilized by each channel in the case of multi-core or multi-band networks (RCMSA/RBMSA). Launch Power has also been considered as a parameter in the optimization objective for dynamic networks (RPMSA) [\[14\]](#page-11-10) [\[15\]](#page-11-11).

While most DRA problems in optical networks from the literature are concerned with point-to-point connections, some consider virtual networking tasks such as virtual optical network embedding (VONE) [\[16,](#page-11-12) [17\]](#page-11-13) or virtual network function placement (VNF) [\[18\]](#page-11-14). We choose to focus on RWA/RSA/RMSA in this paper because they are the most widely studied DRA problems in the context of optical networks and they form a core sub-task of variants such as VNF or VONE.

## *Constraints*

Three fundamental constraints govern resource allocation in optical networks:

- 1. Spectrum Continuity: A lightpath must use identical FSU on each link, without wavelength conversion.
- 2. Spectrum Contiguity: FSU allocated to a lightpath must be adjacent.
- 3. No Reconfiguration: Active lightpaths cannot be reallocated once established, meaning allocation decisions are permanent while connections remain active.

The 'No Reconfiguration' constraint is not a physical limitation but an operational assumption that active services cannot be disrupted. Reconfiguration may sometimes be desirable, especially in flex-grid networks that may suffer from spectral

fragmentation [\[19\]](#page-11-15), and has been used in a production network by Meta Platforms Inc. to free up spectral resources [\[20\]](#page-11-16).

#### *Solution methods*

Allocation of static traffic is a NP-hard combinatorial optimization problem [\[21\]](#page-11-17), for which the computational complexity of finding a solution scales super-polynomially with the space of possible allocations. Exact solution methods such as Integer Linear Programming (ILP) have been formulated for static traffic [\[22,](#page-11-18) [23\]](#page-11-19) but show limited scalability[1](#page-2-1)and are infeasible for dynamic traffic without a priori knowledge of all requests.

For dynamic traffic, any allocation decision must be taken within the constraint of the time interval between request arrivals. No standard limit has been defined for this constraint in the literature but it could be on the order of seconds, with a lower limit set by the switching time of reconfigurable optical add-drop multiplexers (currently 1ms to 100ms, depending on the switching technology [\[24\]](#page-11-20)).

Many simple heuristic algorithms [\[25–](#page-11-21)[29\]](#page-11-22) have been proposed for these problems, with the goal to minimize resources, lightpath distances and required bandwidth. Heuristics have the advantages of fast execution time and deterministic and interpretable allocation decisions.

Machine learning approaches to DRA problems have included nature-inspired techniques like particle swarm optimization (PSO) [\[30\]](#page-11-23) and genetic algorithms (GA) [\[31\]](#page-11-24). Once trained, an RL policy can compute an allocation faster than other ML approaches [\[4\]](#page-11-0).

## **B. Reinforcement learning**

RL is a framework for learning to optimize sequential decision making under uncertainty. It emerged from Bellman's foundational work on optimal control theory in the 1950s, specifically dynamic programming and Markov Decision Processes (MDP) [\[32,](#page-11-25) [33\]](#page-11-26). MDPs model decision-making processes as an agent that takes actions in an environment to maximize a reward signal. The method of action selection is a mapping from states to actions termed the policy, which can be expressed in tabular form or approximated by a neural network (NN). The use of NN for function approximation is sometimes distinguished as "Deep" RL. Tabular RL has been applied to optical networks [\[34\]](#page-11-27), but function approximation with NN is widely used [\[11,](#page-11-7) [28,](#page-11-28) [35–](#page-11-29) [37\]](#page-11-30) when the set of state-action pairs is too large to be tabulated [\[38\]](#page-11-31).

The reader is referred to Sutton and Barto's authoritative textbook [\[38\]](#page-11-31) for details. However, to aid the discussion of RL applied to DRA problems, several terms are defined here.

RL algorithms can be classified as model-based or modelfree. Model-based RL uses a model of the environment to plan future actions, but so far no works have applied this paradigm to DRA problems in optical networks. Model-free RL algorithms learn through direct interaction with the environment, without planning. Model-free algorithms can be further categorized into:

• **Action-value methods**, such as Q-learning, which learn to estimate the value of taking actions in different environment states. These methods were the first to be developed in RL [\[39,](#page-11-32) [40\]](#page-11-33) and have been used for route selection in optical networks [\[41\]](#page-11-34).

<span id="page-2-2"></span>![](_page_2_Figure_13.jpeg)

**Fig. 1.** Count of publications related to RL for resource allocation problems in optical networks. Citations for each classification category are: RWA [\[4,](#page-11-0) [46](#page-12-0)[–58\]](#page-12-1), RSA [\[37,](#page-11-30) [59–](#page-12-2)[75\]](#page-12-3), RMSA [\[11,](#page-11-7) [28,](#page-11-28) [34](#page-11-27)[–36,](#page-11-35) [41,](#page-11-34) [76–](#page-13-0)[102\]](#page-13-1), Other [\[103–](#page-13-2)[134\]](#page-14-0).

• **Policy gradient methods**, which directly optimize the policy parameters to maximize expected rewards. These methods can handle continuous action spaces, unlike actionvalue methods, which optimize an action-value function. Policy gradient methods are enhanced by using an Actor-Critic architecture, as in algorithms such as A2C [\[42\]](#page-11-36) and PPO [\[43\]](#page-11-37), which reduce variance in the policy gradient by using a learned value function (critic) to estimate the value of each state. Policy gradient methods have been used in many works on DRA in optical networks, such as A2C for DeepRMSA [\[11\]](#page-11-7).

## <span id="page-2-0"></span>**3. LITERATURE SURVEY**

There exists a considerable body of literature on RL for DRA problems in optical networks. DRA in optical networks is distinguished from similar problems in electronically linked networks by the nature of fiber optic links, which carry a set of wavelengths or FSU, defined by the ITU standards G.671 and G.694.2 [\[44,](#page-11-38) [45\]](#page-12-4). In this work we only consider publications related to optical networks but acknowledge the closely related literature on RL for other graph-based resource allocation problems.

## **A. Survey methodology**

To provide an overview of research progress on RL applied to DRA problems in optical networks, we searched to gather all relevant research papers. We performed a manual review of results from citation databases to create the final set of 97 peer-reviewed papers. Figure [1](#page-2-2) shows the count of papers by publication year. The papers are grouped in 4 categories: 'RWA', 'RSA', 'RMSA', and 'Other'. We use this set of papers for our analysis of benchmarking practices in the field, which we present in the next section with further commentary on Figure [1.](#page-2-2)

#### **B. Review of benchmarking practices**

In optical networks research, the first benchmark for RL was established by DeepRMSA [\[11\]](#page-11-7) (discussed in detail in Section [B\)](#page-7-0). DeepRMSA was the first RL approach to achieve lower service blocking probability than KSP-FF, or any heuristic that considers multiple candidate paths. As a result of this breakthrough performance, and its open source codebase, the prob-

<span id="page-2-1"></span><sup>1</sup> [\[23\]](#page-11-19) Jaumard et al. scale their ILP formulation to 690 requests on the USNET topology (24 nodes and 86 links) with 380 FSU per link, without considering distance-adaptive modulation formats.

lem definition from DeepRMSA (topologies, traffic model, modulation format reach, FSU per link, etc.) became a de facto standard. Follow-up works used identical or similar problem definitions and compared to DeepRMSA on their problem [\[28,](#page-11-28) [36,](#page-11-35) [37,](#page-11-30) [65,](#page-12-5) [80,](#page-13-3) [89,](#page-13-4) [99,](#page-13-5) [102\]](#page-13-1). Arguably, comparing to Deep-RMSA has become standard benchmarking practice.

Previous work has called for more rigorous benchmarking practices for research on RL for optical networking [\[4\]](#page-11-0), with recommendations for comparison against other machine learning approaches such as GA and PSO, in addition to estimated bounds on network blocking or throughput. Some studies of RL for resource allocation have restricted themselves to sufficiently small problem sizes and static traffic, to enable comparison to ILP results [\[4,](#page-11-0) [55,](#page-12-6) [57,](#page-12-7) [67,](#page-12-8) [87\]](#page-13-6). Although this provides a reliable bound, it is not applicable to dynamic traffic.

Benchmarking against standard heuristic algorithms, such as KSP-FF, avoids the complexity of training a competing machine learning approach, performs deterministic allocation, and can scale to large problem instances. However, it is important to choose the best performing heuristic for a particular case of study as a benchmark. Of the papers that benchmark their RL solution to KSP-FF (or other heuristics that consider multiple candidate paths) [\[4,](#page-11-0) [11,](#page-11-7) [28,](#page-11-28) [34–](#page-11-27)[37,](#page-11-30) [56,](#page-12-9) [63,](#page-12-10) [65,](#page-12-5) [74,](#page-12-11) [77,](#page-13-7) [78,](#page-13-8) [80,](#page-13-3) [81,](#page-13-9) [84–](#page-13-10) [86,](#page-13-11) [89,](#page-13-4) [92](#page-13-12)[–94,](#page-13-13) [113,](#page-14-1) [121,](#page-14-2) [124\]](#page-14-3), most achieve 20-30% reduction in service blocking probability compared to their best heuristic. Only 3 papers achieve a reduction greater than this: MaskRSA [\[35\]](#page-11-29), PtrNet-RSA [\[37\]](#page-11-30), and Terki et al [\[83\]](#page-13-14). Despite these impressive results, we demonstrate in Section [5](#page-5-0) that MaskRSA and PtrNet-RSA are beaten by KSP-FF or FF-KSP by considering 50 candidate paths and ordering the paths by number of hops[2](#page-3-0) .

Benchmarking is further complicated by the fast evolution of optical networking, with novel paradigms such as multiband [\[90\]](#page-13-15) and multi-core [\[88\]](#page-13-16) emerging, and the wide variety of network topologies [\[135\]](#page-14-4) and components that can be considered. The evolution of optical networks research is evidenced by growth in the 'Other' category of Figure [1,](#page-2-2) which includes papers on RL applied to: traffic grooming [\[116,](#page-14-5) [121,](#page-14-2) [123,](#page-14-6) [130\]](#page-14-7), defragmentation [\[119,](#page-14-8) [120,](#page-14-9) [122,](#page-14-10) [124\]](#page-14-3), survivability or service restoration [\[67,](#page-12-8) [68,](#page-12-12) [105,](#page-13-17) [107,](#page-13-18) [113,](#page-14-1) [118,](#page-14-11) [136\]](#page-14-12), multicast provisioning [\[46,](#page-12-0) [114,](#page-14-13) [126\]](#page-14-14), and other problems such as transceiver parameter optimization [\[111,](#page-14-15) [117,](#page-14-16) [137\]](#page-14-17) or launch power optimization [\[129\]](#page-14-18)

The establishment of reliable benchmarks is made more difficult by the fragmented software environment for optical network simulations for RL. Several open source toolkits have been introduced to aid researchers and improve productivity, but none has proved sufficiently popular for it to become standard. Optical-rl-gym [\[108\]](#page-14-19) was the first paper to attempt to introduce a new standard library for this task. This was followed by an extension to multi-band environments [\[115\]](#page-14-20) and in 2024 was further extended to include a more sophisticated physical layer model for lightpath SNR calculations, renamed as the Optical Networking Gym [\[132\]](#page-14-21). Additionally, MaskRSA provides an open source simulation framework (RSA-RL) [\[35\]](#page-11-29) and Deep-RMSA's codebase is widely used [\[138\]](#page-14-22). SDONSim [\[133\]](#page-14-23) and DREAM-ON-GYM [\[134\]](#page-14-0) are other recent additions to the landscape of available simulation frameworks that further fragment the available options.

In summary, progress in applying RL to DRA problems in

optical networks has been difficult to quantify due to several factors. First, the lack of standardized benchmarking practices has made it challenging to fairly compare different approaches. Second, while some studies have used ILP solutions as benchmarks, these are limited to small problem sizes and static traffic scenarios, making them impractical for large-scale or dynamic applications. Third, multiple competing simulation frameworks and publications without open source code have made it difficult to ensure consistent testing conditions across different studies. Finally, the rapid evolution of optical networking technology means benchmarks must constantly evolve to remain relevant.

The lack of reliable benchmarks, and the resulting difficulty in assessing progress in the field, is what motivates our investigations of heuristic benchmarks in Section [4](#page-4-1) and their application to our recreation of previous work in Section [5.](#page-5-0)

#### **C. Recommendations for benchmarking best practice**

Based on our review of the field, we make the following recommendations for selecting benchmarks and evaluating solutions to DRA problems in optical networks:

- **Benchmark selection**: Assess multiple benchmarks and select the best available. Tune parameters such as number of candidate paths and path sort criteria (see section [4A\)](#page-4-0) to maximize performance. Prefer deterministic algorithms that can be reproduced without re-training ML components.
- **Statistical rigor**: Perform sufficient trials for statistical significance (minimum 100 blocking events is a rule of thumb) with multiple random seeds. Report mean and a measure of variability of results e.g. standard deviation.
- **Methodological transparency**: Be transparent in your choice of benchmark and its implementation details. Release code to facilitate verification and extension of research findings. Utilize established simulation frameworks where possible to minimize implementation discrepancies across studies, with unit tests to ensure correctness.

We implement these recommendations in our analyses in sections [4](#page-4-1) and [5.](#page-5-0) We note that these recommendations apply to the evaluation of any solution method for DRA problems, including RL, other ML approaches, or novel heuristic algorithms.

#### <span id="page-3-2"></span>**D. Selection of papers for benchmarking**

To assess progress in RL for DRA, we select 5 papers to rebenchmark in section [5.](#page-5-0) We select these papers primarily because they all compare their results to "DeepRMSA"[3](#page-3-1)with similar traffic models and topologies, therefore present the most consistent application of benchmarks in the field. We also select based on their impact, which we assess by qualitative and quantitative criteria. The qualitative criteria are novelty, contribution, and reputation of publication or conference. The quantitative criterion is their blocking performance relative to benchmarks. They are also among the most highly cited papers in the field, as of April 2025.

1. **DeepRMSA** [\[11\]](#page-11-7) constructs a feature matrix to represent the available paths for the current requests and applies a NN with 5 x 128 hidden units to select from the K-shortest paths with first-fit spectrum allocation. It demonstrates

<span id="page-3-0"></span><sup>2</sup>We have not re-created the study of Terki et al. for benchmarking in Section [5](#page-5-0) as it is multi-band and out of scope of this work. We hypothesise that their approach performs strongly because, similar to PtrNet-RSA, it is not limited to selecting from only K paths.

<span id="page-3-1"></span><sup>3</sup>We note that the training of RL solutions is highly sensitive to hyperparameters [\[139\]](#page-14-24) and non-deterministic factors [\[140\]](#page-14-25), therefore the comparisons that the selected papers make to re-trained DeepRMSA agents may not be robust.

service blocking probability (SBP) reduced by 20% vs. KSP-FF on the NSFNET and COST239 topologies. DeepRMSA's impact was enhanced by its open source codebase.

- Reward-RMSA [28] builds on the DeepRMSA framework and changes the reward function to incorporate fragmentation-related information. They report SBP reduced by 32% vs. multiple heuristics and 55% vs. DeepRMSA on NSFNET and COST239.
- 3. GCN-RMSA [36] is notable as the first work to use advanced NN architectures to improve performance. They use a graph convolutional network (GCN) (including recurrent neural network (RNN) as the path aggregation function) in the policy and value functions, which they claim allows improved feature extraction from the network state. Like DeepRMSA and Reward-RMSA, the policy selects from K paths with first-fit spectrum allocation. They report SBP reduced by up to 30% vs. multiple heuristics and 18% vs. DeepRMSA. on NSFNET, COST239, and USNET.
- 4. MaskRSA [35] innovated by selecting from the entire range of available slots on the K paths and using invalid action masking [141] to increase the efficiency of training. Despite the RSA in the title, the paper does consider distancedependent modulation format (RMSA). MaskRSA presented improvements over KSP-FF on NSFNET and JPN48 topologies with over an order of magnitude lower SBP, or a 35-45% increase in the supported traffic in their cases of study. The authors of MaskRSA also contributed to open source by releasing their simulation framework, RSA-RL.
- 5. PtrNet-RSA [37], published in 2024. It innovates in both the problem setting and its use of pointer-nets [142]. The pointer-net is used to select the constituent nodes of the target path, thereby removing the restriction of selecting from the pre-calculated K-shortest paths. Invalid action masking is used to allow selection from all available spectral slots. Additionally, the paper considers joint optimization of the mean path SNR and the SBP through its reward function. It demonstrates SBP reduced by over an order of magnitude vs. KSP-FF and their implementation of MaskRSA on NSFNET, COST239, and USNET.

#### <span id="page-4-1"></span>4. HEURISTIC ALGORITHM BENCHMARK EVALUATION

To evaluate the results of the selected papers from Section 3D, we must determine the best (lowest blocking probability) heuristic algorithms to use as benchmarks. In this section, we present comparisons of the heuristics listed in Table 1, evaluated on different traffic loads, topologies, and considering different numbers of candidate paths (K). On the basis of this analysis, we select the benchmarks to apply in section 5. We also include a discussion of the effect of different sort criteria for candidate paths in Section A, which significantly affects the blocking performance.

We select the algorithms in Table 1 because they are commonly used as benchmarks or have been reported as superior to other heuristics.

<span id="page-4-0"></span>Figure 2 shows the topologies used in the selected papers. The node and link count for each topology is: NSFNET (14, 22), COST239 (11, 25), USNET (24, 43), JPN48 (48, 82). We use these topologies to analyze the performance of the heuristic algorithms and in our recreation of the papers' problems in section 5. We make all topology data available in our open source codebase [143].

<span id="page-4-2"></span>

| Heuristic                    | Acronym | Reference     |
|------------------------------|---------|---------------|
| K-Shortest Paths First-Fit   | KSP-FF  | [10]          |
| First-Fit K-Shortest Paths   | FF-KSP  | [25]          |
| K-Shortest Paths Best-Fit    | KSP-BF  | [26]          |
| Best-Fit K-Shortest Paths    | BF-KSP  | [26]          |
| K-Minimum Entropy First-Fit  | KME-FF  | [27]          |
| K-Congestion Aware First-Fit | KCA-FF  | CA2 from [29] |

**Table 1.** RMSA heuristics used for benchmarking.

#### A. Effect of path ordering

All the heuristics in Table 1 select from the available precomputed paths on the basis of sort criteria. The primary criterion may be a measure of the path congestion (KCA-FF), spectral fragmentation (KME-FF), or length (KSP-FF). In the event of multiple paths with equal value, a default ordering (usually ascending order of length) determines the selected path.

Conventionally, path length is considered as distance in km. However, we find that considering path length as number of hops (with length in km as a secondary sort criterion), significantly improves the performance of the heuristics. This has been observed previously by Baroni [144], who referred to it as Minimum Number of Hops routing (MNH). The intuitive explanation for this is that, if two paths can support the same order of modulation format, the path that comprises fewer links occupies fewer spectral resources.

We refer to these two orderings as path length in km (#km) or path length in number of hops (#hops). Our comparisons of KSP-FF for these two orderings in Section 5 Figure 5 evidence the reduction in blocking probability from #hops ordering. In our comparisons of heuristics in the next section, we use #hops ordering.

## B. Simulation setup

For each heuristic and topology, we carried out three simulation scenarios to investigate the effects of varying traffic loads and values of K on the relative blocking performance of the heuristics.

## **Experiment 1** - Increasing K:

**Aim**: Investigate relative performance of heuristics with increasing K. **Method**: Record service blocking probability (SBP) for each heuristic at values of K ranging from 2 to 26 at fixed traffic load. We arbitrarily select the traffic load for each topology so that the heuristics give a SBP of  $\sim$ 1%.

**Experiment 2** - Increasing K at high to low traffic:

**Aim**: Investigate the effect of increasing K at different traffic loads. **Method**: Record SBP at K ranging from 2 to 40 for a range of traffic loads. We select the traffic loads for each topology such that they result in  $10^{-5}$  to  $10^{-1}$  SBP. To simplify the analysis and plots, we only present results for KSP-FF.

# **Experiment 3** - Increasing traffic load at K=50:

**Aim**: Using the findings from Experiments 1 and 2, determine the lowest-blocking heuristic with optimized K-value across traffic loads. **Method**: Record SBP for high K (K=50) at varying traffic loads. We select the traffic loads for each topology such that they result in a range of SBP ( $10^{-5}$  to  $10^{-1}$ ). This experiment provides evidence on which heuristic is the best overall for each topology.

<span id="page-5-1"></span>![](_page_5_Figure_1.jpeg)

**Fig. 2.** Network topologies used in our case studies from: DeepRMSA, Reward-RMSA, GCN-RMSA, MaskRSA, PtrNet-RSA [\[11\]](#page-11-7) [\[28\]](#page-11-28) [\[36\]](#page-11-35) [\[35\]](#page-11-29) [\[37\]](#page-11-30). We note that the USNET topology differs between GCN-RMSA and PtrNet-RSA. We show the GCN-RMSA version here. PtrNet-RSA also uses a variant of the COST239 topology.

For each experiment and heuristic, data was collected from 3000 independent trials with unique random seeds. The SBP was calculated after 10,000 connection requests, with the mean and standard deviation calculated across trials. Each data point in Figure [3](#page-6-1) therefore shows summary statistics from 30 million connection requests, which gives high confidence in our results.

We considered dynamic traffic with fixed mean service holding time at 10 units. We considered the same traffic model and other settings as DeepRMSA[4](#page-5-2) : uniform traffic probability between each node pair, Poissonian arrival and departure statistics, uniform random selection of data rate from 25 to 100Gbps in 1Gbps intervals, and distance-dependent modulation formats from BPSK, QPSK, 8QAM, 16QAM, and maximum transmission distances of 10,000km, 2500km, 1250km, 625km, respectively, We consider topologies with dual fibre links (one for each direction of propagation), 12.5GHz FSU width, and 100 FSU per fibre.

## **C. Results and discussion**

**Experiment 1** results in Figure [3\(](#page-6-1)a) show different outcomes for smaller networks (NSFNET and COST239) and larger networks (USNET and JPN48). For NSFNET and COST239, KSP-FF and KME-FF are approximately equal and give the lowest blocking. Their blocking decreases to a minimum for approximately K=23 and above for NSFNET and continues to decrease for K>26 for COST239.

For USNET and JPN48, FF-KSP is clearly the best heuristic, with blocking reduced by half for JPN48. Blocking from FF-KSP decreases with K until K=26 for USNET and continues dropping sharply for K>26 for JPN48. For USNET, KSP-FF and

KME-FF become competitive with FF-KSP at large K. It can be argued that FF-KSP performs better in networks with higher numbers of nodes and links where there are many viable paths between source and destination, and dense packing of utilized wavelengths increases in relative importance to path selection.

The results from Experiment 1 indicate that KSP-FF and FF-KSP generally give the lowest blocking, depending on the network topology, and blocking decreases monotonically with increasing K. This experiment looked at a moderately high traffic load (∼1% SBP), therefore experiment 2 investigates if the effect of increasing K holds at different traffic loads.

**Experiment 2** results in Figure [3\(](#page-6-1)b) show that, regardless of the traffic load, increasing K decreases the SBP, until SBP reaches a minimum and increasing K does not decrease SBP further. Across all topologies and traffic loads tested in our experiments, we found that SBP does not decrease significantly for K>50. For very high traffic (approximately equivalent to incremental loading), the value of K beyond which SBP does not continue to decrease can be much lower.

**Experiment 3** results in Figure [3\(](#page-6-1)c) show the variation of SBP with traffic load for each heuristic with K=50. We verified that at least 50 unique paths are possible for every node pair on our investigated topologies. We select K=50 on the basis of experiments 1 and 2. These results confirm the initial findings from Experiment 1 - that KSP-FF and KME-FF are the lowest blocking for NSFNET and COST239[5](#page-5-3) , while FF-KSP is better for USNET and JPN48, with an order of magnitude lower blocking probability on JPN48 compared to the next best heuristic.

In summary, we highlight the generally strong performance of the KSP-FF and FF-KSP heuristics. We find that increasing the number of candidate paths decreases the blocking probability, as does the ordering of candidate paths. We find #hops ordering is superior to #km for reduced blocking probability, as evidenced in Section [5](#page-5-0) Figure [5.](#page-8-1)

We point out that the list of heuristics we evaluate is not exhaustive and superior algorithms may exist. We therefore encourage thorough analysis to determine the strongest heuristic benchmark for a particular problem, as we have exemplified here. However, for the purposes of this study and our comparisons to previous work in Section [5,](#page-5-0) we find that KSP-FF with K=50 and #hops ordering demonstrates lower blocking probability than previous RL approaches.

#### <span id="page-5-0"></span>**5. BENCHMARKING OF PREVIOUS WORK**

As discussed in our literature review (Section [3\)](#page-2-0), it is difficult to assess progress in the field due to several factors, particularly the diversity of problem definitions and use of weak benchmarks. To address this, we exactly recreate the problem settings from five influential papers from the literature, and apply the bestperforming heuristics from Section [4](#page-4-1) in each case.

In this section, we first provide analysis of holding time truncation, an implementation detail present in the DeepRMSA codebase that significantly affects the blocking probability. We then present the results of our reproductions of the selected papers and compare to the heuristics, which have significantly lower blocking probability all of the published RL solutions.

We have corresponded with the authors of the selected papers to clarify details of their implementation and ensure that our recreations exactly match all the relevant details of their

<span id="page-5-2"></span><sup>4</sup>We consider the DeepRMSA problem settings in these experiments because it is used by most of the papers presented in Section [5.](#page-5-0)

<span id="page-5-3"></span><sup>5</sup>Although Figure [3\(](#page-6-1)c) shows KME-FF gives slightly lower blocking than KSP-FF at lower traffic, we prefer KSP-FF for benchmarking purposes because of its widespread use and its greater simplicity.

<span id="page-6-1"></span>![](_page_6_Figure_1.jpeg)

**Fig. 3.** Comparison of heuristic algorithms. (a) Service blocking probability (SBP) at fixed traffic and varying numbers of candidate paths (K). (b) SBP for KSP-FF at varying traffic loads and K=2 to K=40. (c) SBP at varying traffic load for K=50. The mean and standard deviation (shaded area) are calculated from 3000 trials of 10,000 traffic requests per data point. KSP-FF or FF-KSP with K=50 are found to give the lowest blocking.

problems. The table of Appendix A provides numerical comparisons of the results of KSP-FF from the papers and our recreation of their problems, which show good agreement within one standard error. We point out that we do not reproduce the training of the published RL results. We choose not to reproduce training because of insufficient training details and the widely documented difficulties in reproduction of RL training due to sensitivity to hyperparameters and random seeds [\[139,](#page-14-24) [145\]](#page-15-4). Extracting RL results from published papers gives a more reliable and fair comparison.

<span id="page-6-0"></span>We use our high-performance simulation framework, XLRON [\[146\]](#page-15-5), for all experiments. It has demonstrated 10x faster execution on CPU and over 1000x faster when parallelized on GPU compared to optical-rl-gym [\[131\]](#page-14-26). This is possible due to its array-based data model and use of the JAX numerical array computing framework, that enables just-in-time compilation to accelerator hardware. It also offers a complete suite of unit tests for core functionality, making it reliable, and includes features to reproduce the problem settings of the selected papers. We use it for these reasons and for its simple command-line interface, which facilitates experiment automation and reproducibility.

#### **A. Holding time truncation**

In dynamic traffic simulations, the service holding time and time until the next arrival of a service request are modeled as exponentially distributed random variables, which is consistent with the assumption of Poisson arrival processes. Random sampling from these exponential distributions is used to generate times for each service request in the simulation.

DeepRMSA, Reward-RMSA, and GCN-RMSA use the same original DeepRMSA codebase as the basis for their experiments. This codebase includes a significant detail: the service holding time is resampled if the resulting value is more than twice the mean of the distribution. We refer to this detail as holding time truncation. In order to recreate the problems from these papers, we analyze the effect of holding time truncation.

#### *A.1. Experiment setup*

To understand the effect of truncation on the traffic statistics, we define an exponential distribution with unit mean. We take 10<sup>6</sup> samples from the distribution, both with and without truncation, and calculate the mean of the resulting sample populations in both cases.

<span id="page-7-1"></span>![](_page_7_Figure_1.jpeg)

**Fig. 4.** Histogram of service holding holding times. The truncated distribution resamples the holding time when the sampled value exceeds 2\*mean. This reduces the mean holding time by 31% compared to the standard exponential distribution.

#### A.2. Results and discussion

Figure 4 compares histograms of service holding times with and without truncation. The y-axis shows the probability density, which is normalized so the area of each histogram gives unit probability. The truncated case shows a cutoff at twice the mean holding time. The vertical lines indicate the mean for each case.

Holding time truncation reduces the mean by approximately 31%. This results in 31% lower traffic load. Therefore, papers that use the DeepRMSA codebase (including DeepRMSA, Reward-RMSA, and GCN-RMSA) evaluate their solutions at traffic loads 31% lower than reported. This detail is not made explicit in the published papers. This finding highlights the challenges in making fair comparisons between papers, and the need for transparency in research code.

#### <span id="page-7-0"></span>B. Benchmarking of published results

Our analysis of the best performing heuristics, of holding time truncation, and our correspondence with the authors enables us to benchmark the published results from the five selected influential papers. The aim of this comparison is to determine if any of the published RL solutions achieve lower SBP than the heuristics.

#### B.1. Experiment methodology

We recreate the problems from each selected paper in our own simulation framework [131]. We match the topologies (NSFNET, COST239, JPN48, USNET), mean service arrival rates, mean service holding times, data-rate or bandwidth request distributions, and uniform traffic matrices. We use the same measurement methodology as described in the respective papers to reproduce results, which is 3000 request warm-up period (to allow the network blocking probability to reach steady-state after the 'initial transient' [147]) followed by 10,000 requests. The SBP is calculated at the end of the episode. We run 10 independent episodes at each traffic load per problem and calculate the mean and standard deviation across trials.

We extract published results for KSP-FF and RL solutions from the papers, using textual values where available otherwise reading from charts. All published results report only a single data point for each traffic value, without uncertainty estimates. We check that our results for KSP-FF with K=5 (green line in Figure 5) match the published results for KSP-FF (blue line in Figure 5) within two standard deviations to ensure faithful reproduction. This comparison gives us a high degree of confidence that we have exactly recreated each problem setting.

#### B.2. Results and discussion

Figure 5 shows our reproduction of results from the selected papers, with SBP against traffic load in Erlangs in each subplot. The plots are organized by paper (columns) and topology (rows). PtrNet-RSA has two columns reflecting its two test cases: networks with 40 FSU per link and 1 FSU requests, and networks with 80 FSU per link and 1-4 FSU requests. PtrNet-RSA only considers fixed-bandwidth requests (no distance-dependent modulation format). MaskRSA and PtrNet-RSA only consider single fibre links (counter-propagating channels) , whereas the other cases consider dual fibre links (one fibre for each direction of propagation), which increases their capacity.

Each plot contains 5 datasets:

RL: Published results for the RL approach

**5-SP-FF** $_{km}^{published}$ : Published results for KSP-FF (K=5) with paths ordered by #km

**5-SP-FF** $_{km}$ : Our results for KSP-FF (K=5) with paths ordered by #km

**5-SP-FF**<sub>hops</sub>: Our results for KSP-FF (K=5) with paths ordered by #hops

 $50\text{-SP-FF}_{hops}$ : Our results for KSP-FF (K=50) with paths ordered by #hops

Points show mean values, shaded areas indicate standard deviation and lines interpolate between points. The DeepRMSA paper provides data for only one traffic load per topology. The excellent agreement between 5-SP-FF $_{km}^{published}$  and 5-SP-FF $_{km}$  in all cases confirms that our framework accurately reproduces the published scenarios.

From Figure 5, we highlight the comparisons of 'RL' (red) with 5-SP-FF<sub>hops</sub> (orange), and 50-SP-FF<sub>hops</sub> (purple). 5-SP-FF<sub>hops</sub> reduces the blocking probability by up to an order of magnitude compared to RL in all cases for NSFNET, 4/5 cases for COST239 and 1/3 cases for USNET. This shows that ordering paths by #hops is sufficient to beat the RL results in these cases.

For larger topologies, considering more candidate paths (K>5) improves the heuristic performance significantly, often by over an order of magnitude. As shown by Figure 5, 50-SP-FF<sub>hops</sub> gives the lowest SBP of all approaches in all cases, except PtrNet-RSA-80 USNET (bottom right).

For PtrNet-RSA-80 USNET, we consider it plausible that the pointer-net architecture is a contributing factor to the strong performance, as it is not limited to selecting from a pre-defined set of paths. However, as the published results in this case fall within one standard deviations of the mean for 50-SP-FF $_{hops}$ , the result could be spurious. This highlights the need for summary statistics and confidence intervals from multiple trials to be included with published results.

In summary, the results show that making minor changes (ordering paths by #hops and considering more paths) to simple heuristic algorithms is sufficient to achieve lower blocking probability than the sophisticated RL solutions that have been published.

We highlight that this analysis, and the selected papers, focus on SBP as the optimization objective. In realistic scenarios, net-

<span id="page-8-1"></span>![](_page_8_Figure_1.jpeg)

**Fig. 5.** Mean SBP against traffic load. Each column is a publication and each subplot is for a topology. Error bars and shaded areas show standard deviations. 50-SP-FF $_{hops}$  exceeds or matches the RL performance for each case.

work blocking or throughput must be balanced with other metrics such as latency and total cost of operation from transceiver launch power, amplifiers, and other network elements. Future research should therefore focus on problems that take a holistic approach to network operations optimization with multiple objectives [58], and incorporate sophisticated models of all physical layer effects for improved accuracy [148, 149].

All data shown in Figure 5 is provided in tabular form in Appendix A.

## <span id="page-8-0"></span>6. NETWORK BLOCKING BOUNDS

We have demonstrated in Section 5 that many influential works on RL for DRA problems in optical networks have failed to improve on a simple heuristic algorithm. The extent to which it is possible to reduce the blocking probability, and increase supported traffic, is an important motivating factor in any future research into this topic.

To understand the limits of blocking probability, we derive empirical lower bounds. By comparing these lower bounds to the performance of our best solution for a target SBP, we can estimate the additional traffic load that can be supported and, therefore, the maximum benefit from applying an intelligent resource allocation method such as RL.

As discussed in section 2, DRA problems in optical networks that require RSA are subject to three constraints: spectrum continuity, spectrum contiguity, and no reconfiguration. By relaxing any of these constraints, the optimal or near-optimal solution of the relaxed problem is a bound on the solution of the full problem. The cut-sets bound method of Cruzado et al [150, 151]

relaxes the spectrum continuity constraint and uses insights from the min-cut max-flow theorem to estimate a lower bound SBP. We instead relax the constraint on reconfiguring already-established connections, a process known as defragmentation.

We couple this defragmentation with resource prioritization: sorting the active connection requests by their required resources and allocating them sequentially. The sorting of active requests in descending order of required resources was found to improve the achievable capacity to optimal or near-optimal by Baroni [144] in static RWA and later Beghelli [152] for dynamic RWA, a method they refer to as 'reconfigurable routing'. Since our problem settings are elastic optical networks, we prefer the term defragmentation. The intuition behind this approach is to allocate requests with longer paths and higher spectral requirements first so that requests with lower resource requirements may be squeezed into remaining spectral gaps later.

#### **Resource-Prioritized Defragmentation**

The resource-prioritized defragmentation algorithm is outlined in Algorithm 1. It utilizes four key subroutines:

- REMOVEEXPIREDREQUESTS(N, t) maintains network state by removing connections that have expeired. For current time t, and request with arrival time  $t_{\rm arrival}$  and holding time  $t_{\rm holding}$ , the expiry condition is defined as:  $t_{\rm arrival} + t_{\rm holding} < t$ .
- ALLOCATEREQUEST(N, request) establishes a new connection subject to continuity and contiguity constraints, and

<span id="page-9-0"></span>**Algorithm 1.** Resource-Prioritized Defragmentation Blocking Bound Estimation

```
Require: Network topology G, Set of requests R, Frequency
   slots per link F
Ensure: Blocking probability Pb
 1: N ← INITIALIZENETWORK(G, F) ▷ Initialize network state
   with empty spectrum slots
 2: blocked ← false
 3: blocked_requests ← 0
 4: for t ← 1 to |R| do
 5: N ← REMOVEEXPIREDREQUESTS(N, t)
 6: rt ← current request from R
 7: N, blocked ← ALLOCATEREQUEST(N,rt)
 8: if blocked then
 9: active_requests ← GETACTIVEREQUESTS(R, t)
10: sorted_requests ← SORTBYRESOURCE(active_requests)
11: Ntemp ← INITIALIZENETWORK(G, F)
12: blocked ← false
13: for r ∈ sorted_requests do
14: N, blocked ← ALLOCATEREQUEST(Ntemp,r)
15: if blocked then
16: break
17: if not blocked then
18: N ← Ntemp
19: else
20: blocked_requests ← blocked_requests + 1
21: return blocked_requests
             |R|
```

returns the updated network state and a boolean to indicate if the connection was blocked. We use the KSP-FF or FF-KSP algorithm with K=50. We select the algorithm that produces the lowest SBP for the problem instance.

- GETACTIVEREQUESTS(R, *t*) identifies requests where *t*arrival ≤ *t* < *t*arrival + *t*holding, determining which connections require reallocation during defragmentation.
- SORTBYRESOURCE(*requests*) orders active requests by required resources (product of required spectral slots and hops of shortest path), prioritizing larger requests during reallocation to maximize the probability of finding viable configurations.

A shortcoming of our method of blocking bound estimation is its reliance on the internal ALLOCATEREQUEST heuristic. To have confidence that the solution presents a true bound, the allocation method must be as close to optimal as possible. We therefore evaluate multiple heuristics for each case, as shown in Section [4,](#page-4-1) and select the one with lowest SBP. We find the best performing heuristic is KSP-FF*hops* with K=50 for most cases, except MaskRSA JPN48 which is FF-KSP.

An advantage of our method compared to cut-sets analysis is it computes an allocation that is guaranteed to be physically possible, as it relaxes the 'No Reconfiguration' constraint instead of the physical spectrum continuity constraint. Relaxing the 'No Reconfiguration' constraint makes Algorithm [1](#page-9-0) omniscient (it has complete knowledge of requests to be allocated) rather than a strictly on-line algorithm, according to definitions from Awerbuch et al [\[153\]](#page-15-12). This gives Algorithm [1](#page-9-0) a fundamental competitive advantage over on-line algorithms like KSP-FF/FF-KSP, therefore it can be considered a lower bound estimator of blocking probability.

We note that our algorithm is general and can be applied to any DRA problem in optical networks by using a strong heuristic for ALLOCATEREQUEST and defining the resource-based sort criteria appropriately.

#### **A. Experiment setup**

For each problem from the five selected papers, we run the best performing heuristic for a range of traffic loads that result in SBP from 0.01% to 1%. For the lowest-blocking heuristic and for Algorithm [1,](#page-9-0) we run 10 episodes of 10,000 requests with unique random seeds and calculate the mean and standard deviation of SBP across episodes. We calculate the mean and standard deviation SBP across episodes in each case.

We compare the resulting SBP from the best heuristic and from algorithm [1.](#page-9-0) We seek to estimate the additional network capacity that can be achieved at 0.1% SBP for each case of study from the five selected papers. We select 0.1% SBP to align with previous studies of network throughput estimation by Cruzado et al [\[150,](#page-15-9) [151\]](#page-15-10).

#### **B. Results and discussion**

Similar to Figure [5,](#page-8-1) each subplot in Figure [6](#page-10-3) represents a different problem instance. DeepRMSA, Reward-RMSA, and GCN-RMSA are combined into a single set of plots since they use identical topologies and traffic models. The purple lines show the best performing heuristic in each case (KSP-FF with K=50, or FF-KSP for JPN48), with paths sorted in ascending order of number of hops. The grey lines show the resource-prioritized defragmentation bounds. At 0.1% SBP, we compare the network traffic loads that can be supported in each case, with the difference highlighted by a red horizontal line. The relative increase in network capacity is calculated as the difference between the upper bound traffic load and the heuristic traffic load, as a percentage of the heuristic load.

PtrNet-RSA-40 shows differences of 5%, 1%, and 8% across its three test cases. These relatively low values are due to the fixed width requests size of 1 FSU used in this case, which makes it equivalent to RWA and reduces the impact of fragmentation compared to RSA/RMSA.

For the Deep/Reward/GCN-RMSA, MaskRSA and PtrNet-RSA-80 cases, the difference between the supported traffic in the heuristic case and the upper bound ranges from 19% (MaskRSA JPN48) to 36% (Deep/Reward/GCN-RMSA NSFNET). These results show larger but comparable optimality gaps to those from the cut-sets method of Cruzado et al. [\[151\]](#page-15-10), who found gaps of 5% to 16% in their cases of study. This shows that defragmentation can unlock significant network capacity, but it is unknown theoretically how close an intelligent online allocation method, such as RL, can come to this bound. This will be the subject of future research.

# **7. CONCLUSION**

Our review of the field of RL applied to DRA problems in optical networks shows that it has been the subject of significant research interest, with almost 100 peer-reviewed papers published so far. Technical innovations from ML research, such as invalid action masking [\[35,](#page-11-29) [37,](#page-11-30) [56\]](#page-12-9) and GNNs [\[36,](#page-11-35) [96,](#page-13-19) [154\]](#page-15-13), have been applied to the problem area and have demonstrated incremental improvements in network blocking.

However, the field has suffered from a lack of standardization in problems, selective application of benchmark algorithms, and

<span id="page-10-3"></span>![](_page_10_Figure_1.jpeg)

**Fig. 6.** Mean SBP against traffic load for the lowest-blocking heuristic in each case (KSP-FF or FF-KSP with K=50) and the estimated bound from Algorithm [1.](#page-9-0) Each column is a publication and each subplot is for a topology. Shaded areas show standard deviations. Red lines and text indicate relative increase in supported traffic at 0.1% SBP from heuristic to bound.

poor practices for reproducibility. We have addressed these problems by assessing a range of heuristic algorithms, optimizing their path ordering and number of candidate paths, and applying them to the problem settings from five influential papers on RL for DRA. We use our simulation framework for this work, which enabled recreation of diverse problem settings and fast computation.

From our assessment and optimization of heuristic algorithms, we determine that KSP-FF or FF-KSP with K=50 are the best of those we evaluated. We highlight the result that ordering the candidate paths by number of hops gives significantly lower blocking probability than ordering by distance. These recommended benchmarks can be applied to future studies of RL or other solution methods.

Our most significant findings are in the benchmarking of previous RL results. By extracting the published results of RL from the selected papers, and comparing to the best heuristic benchmarks on recreated problem settings, we show that simple heuristics exceed or match the RL results in all cases, often with over an order of magnitude lower SBP. This shows the relative performance of previous RL solutions on these problems has been overestimated due to weak benchmarks, and highlights the need for more rigorous standards of evaluation on these problems to avoid trivial results. These standards also apply to other non-RL resource allocation algorithms.

Finally, to ascertain the practical value of pursuing further research into optimized DRA, we provide the Resource-Prioritized Defragmentation method of estimating the lower bound network blocking probability. Compared to the best heuristics available for each case, this method estimates the upper bound additional dynamic traffic load that can be supported on flex-grid networks is approximately 19% to 36%. These results suggest there is room for improvement over the best benchmarks, which may motivate further research into DRA with RL or other methods. Alternatively, research into network optimization with RL could focus on other objectives for which there are not yet good heuristic solutions.

# **ACKNOWLEDGMENTS**

This work was supported by the Engineering and Physical Sciences Research Council (EPSRC) grant EP/S022139/1 - the Centre for Doctoral Training in Connected Electronic and Photonic Systems - and EPSRC Programme Grant TRANSNET EP/R035342/1. In addition, Polina Bayvel is supported through a Royal Society Research Professorship.

# **REFERENCES**

- <span id="page-10-0"></span>1. A. Lord, C. White, and A. Iqbal, "Future Optical Networks in a 10 Year Time Frame," in *2021 Optical Fiber Communications Conference and Exhibition (OFC),* (2021), pp. 1–3.
- <span id="page-10-1"></span>2. M. Shtaif, C. Antonelli, A. Mecozzi, and X. Chen, "The Information Capacity of the Fiber-Optic Channel: Bounds and prospects," in *2024 Optical Fiber Communications Conference and Exhibition (OFC),* (2024), pp. 1–3.
- <span id="page-10-2"></span>3. P. J. Winzer, "The future of communications is massively parallel," J. Opt. Commun. Netw. **15**, 783 (2023).

- <span id="page-11-0"></span>4. N. Di Cicco, E. F. Mercan, O. Karandin, O. Ayoub, S. Troia, F. Musumeci, and M. Tornatore, "On Deep Reinforcement Learning for Static Routing and Wavelength Assignment," IEEE J. Sel. Top. Quantum Electron. **28**, 1–12 (2022).
- <span id="page-11-1"></span>5. F. N. Khan, "Non-technological barriers: the last frontier towards AIpowered intelligent optical networks," Nat. Commun. **15**, 5995 (2024).
- <span id="page-11-2"></span>6. M. Doherty, "micdoh/XLRON: Reinforcement Learning for Dynamic Resource Allocation in Optical Networks: Hype or Hope?" (2024). URL: <https://zenodo.org/doi/10.5281/zenodo.14561463> (accessed 2024-12- 27).
- <span id="page-11-3"></span>7. J.-L. Augé, "Can we use Flexible Transponders to Reduce Margins?" in *Optical Fiber Communication Conference/National Fiber Optic Engineers Conference 2013,* (OSA, Anaheim, California, 2013), p. OTu2A.1.
- <span id="page-11-4"></span>8. Y. Pointurier, "Design of Low-Margin Optical Networks," J. Opt. Commun. Netw. **9**, A9 (2017).
- <span id="page-11-5"></span>9. D. Hassabis, "Nobel Prize Lecture," (2024). URL: [https:](https://www.nobelprize.org/prizes/chemistry/2024/hassabis/lecture/) [//www.nobelprize.org/prizes/chemistry/2024/hassabis/lecture/](https://www.nobelprize.org/prizes/chemistry/2024/hassabis/lecture/) (accessed 2024-12-25).
- <span id="page-11-6"></span>10. H. Zang, J. P. Jue, and B. Mukherjee, "A review of routing and wavelength assignment approaches for wavelength-routed optical WDM networks," Opt. Networks Mag. **1**, 47–60 (2000).
- <span id="page-11-7"></span>11. X. Chen, B. Li, R. Proietti, H. Lu, Z. Zhu, and S. J. B. Yoo, "DeepRMSA: A Deep Reinforcement Learning Framework for Routing, Modulation and Spectrum Assignment in Elastic Optical Networks," J. Light. Technol. **37**, 4155–4163 (2019).
- <span id="page-11-8"></span>12. A. Lord, S. J. Savory, M. Tornatore, and A. Mitra, "Flexible Technologies to Increase Optical Network Capacity," Proc. IEEE **110**, 1714–1724 (2022).
- <span id="page-11-9"></span>13. B. Mukherjee, I. Tomkos, M. Tornatore, P. Winzer, and Y. Zhao, eds., *Springer Handbook of Optical Networks*, Springer Handbooks (Springer International Publishing, Cham, 2020).
- <span id="page-11-10"></span>14. D. J. Ives, P. Bayvel, and S. J. Savory, "Routing, modulation, spectrum and launch power assignment to maximize the traffic throughput of a nonlinear optical mesh network," Photonic Netw. Commun. **29**, 244– 256 (2015).
- <span id="page-11-11"></span>15. F. Arpanaei, M. R. Zefreh, J. A. Hernández, B. Shariati, J. Fischer, J. M. Rivas-Moscoso, F. Jiménez, J. P. Fernández-Palacios, and D. Larrabeiti, "Launch Power Optimization for Dynamic Elastic Optical Networks over C+L Bands," arXiv. (2023).
- <span id="page-11-12"></span>16. L. Gong and Z. Zhu, "Virtual Optical Network Embedding (VONE) Over Elastic Optical Networks," J. Light. Technol. **32**, 450–460 (2014).
- <span id="page-11-13"></span>17. M. Doherty and A. Beghelli, "Deep Reinforcement Learning for Infrastructure as a Service over Flexible Optical Networks," (IEEE, Glasgow, UK, 2023).
- <span id="page-11-14"></span>18. C. Zhou, B. Zhao, J. Tao, and B. Wang, "Applications of Reinforcement Learning in Virtual Network Function Placement: A Survey," in *2022 18th International Conference on Mobility, Sensing and Networking (MSN),* (IEEE, Guangzhou, China, 2022), pp. 871–876.
- <span id="page-11-15"></span>19. O. Gerstel, M. Jinno, A. Lord, and S. B. Yoo, "Elastic optical networking: a new dawn for the optical layer?" IEEE Commun. Mag. **50**, s12–s20 (2012).
- <span id="page-11-16"></span>20. S. Balasubramanian, V. Dangui, J. P. Eason, and S. Singh Ahuja, "Targeted Defragmentation of a Production Optical Network," in *2023 International Conference on Optical Network Design and Modeling (ONDM),* (IEEE, Coimbra, Portugal, 2023), pp. 1–3.
- <span id="page-11-17"></span>21. I. Chlamtac, A. Ganz, and G. Karmi, "Lightpath communications: an approach to high bandwidth optical WAN's," IEEE Transactions on Commun. **40**, 1171–1182 (1992).
- <span id="page-11-18"></span>22. K. Walkowiak, P. Lechowicz, M. Klinkowski, and A. Sen, "ILP modeling of flexgrid SDM optical networks," in *2016 17th International Telecommunications Network Strategy and Planning Symposium (Networks),* (2016), pp. 121–126.
- <span id="page-11-19"></span>23. B. Jaumard, A. Mohammed, and Q. A. Nguyen, "Decomposition Models for the Routing and Slot Provisioning Problem," in *2023 International Conference on Computing, Networking and Communications (ICNC),* (2023), pp. 659–665.
- <span id="page-11-20"></span>24. Y. Goto, S. Shinada, Y. Hirota, and H. Furukawa, "LCOS-based Flexible Optical Switch for Heterogeneous SDM Fiber Networks," in *2024 24th*

- *International Conference on Transparent Optical Networks (ICTON),* (2024), pp. 1–4.
- <span id="page-11-21"></span>25. R. J. Vincent, D. J. Ives, and S. J. Savory, "Scalable Capacity Estimation for Nonlinear Elastic All-Optical Core Networks," J. Light. Technol. **37**, 5380–5391 (2019).
- <span id="page-11-39"></span>26. F. S. Abkenar, A. Ghaffarpour Rahbar, and A. Ebrahimzadeh, "Best fit (BF): A new Spectrum Allocation mechanism in Elastic Optical Networks (EONs)," in *2016 8th International Symposium on Telecommunications (IST),* (2016), pp. 24–29.
- <span id="page-11-40"></span>27. P. Wright, M. C. Parker, and A. Lord, "Minimum- and maximum-entropy routing and spectrum assignment for flexgrid elastic optical networking [invited]," J. Opt. Commun. Netw. **7**, A66–A72 (2015).
- <span id="page-11-28"></span>28. B. Tang, Y.-C. Huang, Y. Xue, and W. Zhou, "Heuristic Reward Design for Deep Reinforcement Learning-Based Routing, Modulation and Spectrum Assignment of Elastic Optical Networks," IEEE Commun. Lett. **26**, 2675–2679 (2022).
- <span id="page-11-22"></span>29. S. J. Savory, "Congestion Aware Routing in Nonlinear Elastic Optical Networks," IEEE Photonics Technol. Lett. **26**, 1057–1060 (2014).
- <span id="page-11-23"></span>30. A. Hassan and C. Phillips, "Chaotic Particle Swarm Optimization for Dynamic Routing and Wavelength Assignment in All-Optical WDM networks," in *2009 3rd International Conference on Signal Processing and Communication Systems,* (2009), pp. 1–7.
- <span id="page-11-24"></span>31. R. S. Barpanda, A. K. Turuk, B. Sahoo, and B. Majhi, "Genetic Algorithm techniques to solve Routing and Wavelength Assignment problem in Wavelength Division Multiplexing all-optical networks," in *2011 Third International Conference on Communication Systems and Networks (COMSNETS 2011),* (IEEE, Bangalore, 2011), pp. 1–8.
- <span id="page-11-25"></span>32. R. Bellman, "The theory of dynamic programming," Bull. Am. Math. Soc. **60**, 503–515 (1954).
- <span id="page-11-26"></span>33. R. BELLMAN, "A Markovian Decision Process," J. Math. Mech. **6**, 679– 684 (1957). Publisher: Indiana University Mathematics Department.
- <span id="page-11-27"></span>34. A. B. Terki, J. Pedro, A. Eira, A. Napoli, and N. Sambo, "Routing and Spectrum Assignment Based on Reinforcement Learning in Multi-Band Optical Networks," in *2023 International Conference on Photonics in Switching and Computing (PSC),* (IEEE, Mantova, Italy, 2023), pp. 1–3.
- <span id="page-11-29"></span>35. M. Shimoda and T. Tanaka, "Mask RSA: End-To-End Reinforcement Learning-based Routing and Spectrum Assignment in Elastic Optical Networks," in *2021 European Conference on Optical Communication (ECOC),* (IEEE, Bordeaux, France, 2021), pp. 1–4.
- <span id="page-11-35"></span>36. L. Xu, Y.-C. Huang, Y. Xue, and X. Hu, "Deep Reinforcement Learning-Based Routing and Spectrum Assignment of EONs by Exploiting GCN and RNN for Feature Extraction," J. Light. Technol. **40**, 4945–4955 (2022).
- <span id="page-11-30"></span>37. Y. Cheng, S. Ding, Y. Shao, and C.-K. Chan, "PtrNet-RSA: A Pointer Network-based QoT-aware Routing and Spectrum Assignment Scheme in Elastic Optical Networks," J. Light. Technol. pp. 1–12 (2024).
- <span id="page-11-31"></span>38. R. S. Sutton and A. G. Barto, *Reinforcement learning: an introduction (2nd ed.)*, Adaptive computation and machine learning (MIT Press, Cambridge, Mass, 2018).
- <span id="page-11-32"></span>39. C. Watkins, "Learning from Delayed Reward," Ph.D. thesis, Cambridge University (1989).
- <span id="page-11-33"></span>40. R. S. Sutton, "Learning to predict by the methods of temporal differences," Mach. Learn. **3**, 9–44 (1988).
- <span id="page-11-34"></span>41. N. B. Bryant, K. K. Chung, J. Feng, S. Harris, K. N. Umeh, and M. Aibin, "Q-Learning Based Routing in Optical Networks," in *2022 IEEE Canadian Conference on Electrical and Computer Engineering (CCECE),* (IEEE, Halifax, NS, Canada, 2022), pp. 419–422.
- <span id="page-11-36"></span>42. V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. P. Lillicrap, T. Harley, D. Silver, and K. Kavukcuoglu, "Asynchronous Methods for Deep Reinforcement Learning," (2016). URL: <http://arxiv.org/abs/1602.01783> (accessed 2023-09-26), arXiv:1602.01783 [cs].
- <span id="page-11-37"></span>43. J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, "Proximal Policy Optimization Algorithms," (2017). URL: [http://arxiv.org/abs/](http://arxiv.org/abs/1707.06347) [1707.06347](http://arxiv.org/abs/1707.06347) (accessed 2023-01-20), arXiv:1707.06347 [cs].
- <span id="page-11-38"></span>44. International Telecommunication Union, "Spectral grids for WDM applications: CWDM wavelength grid," Recommendation G.694.2, ITU Telecommunication Standardization Sector (2002).

<span id="page-12-4"></span>45. International Telecommunication Union, "Transmission characteristics of optical components and subsystems," Recommendation G.671, ITU Telecommunication Standardization Sector (2012).

- <span id="page-12-0"></span>46. P. Garcia, A. Zsigri, and A. Guitton, "A multicast reinforcement learning algorithm for WDM optical networks," in *Proceedings of the 7th International Conference on Telecommunications, 2003. ConTEL 2003.*, (IEEE, Zagreb, Croatia, 2003), pp. 419–426 vol.2.
- 47. Y. Pointurier and F. Heidari, "Reinforcement learning based routing in all-optical networks," in *2007 Fourth International Conference on Broadband Communications, Networks and Systems (BROADNETS '07),* (IEEE, Raleigh, NC, USA, 2007), pp. 919–921.
- 48. I. Koyanagi, T. Tachibana, and K. Sugimoto, "A Reinforcement Learning-Based Lightpath Establishment for Service Differentiation in All-Optical WDM Networks," in *GLOBECOM 2009 - 2009 IEEE Global Telecommunications Conference,* (IEEE, Honolulu, Hawaii, 2009), pp. 1–6.
- 49. J. Suárez-Varela, A. Mestres, J. Yu, L. Kuang, H. Feng, A. Cabellos-Aparicio, and P. Barlet-Ros, "Routing in optical transport networks with deep reinforcement learning," J. Opt. Commun. Netw. **11**, 547 (2019).
- 50. R. Shiraki, Y. Mori, H. Hasegawa, and K.-i. Sato, "Dynamic Control of Transparent Optical Networks with Adaptive State-Value Assessment Enabled by Reinforcement Learning," in *2019 21st International Conference on Transparent Optical Networks (ICTON),* (IEEE, Angers, France, 2019), pp. 1–4.
- 51. R. Shiraki, Y. Mori, H. Hasegawa, and K.-i. Sato, "Reinforcementlearning-based optical-path routing and wavelength assignment with adaptation to traffic-distribution change," IEICE Tech. Report; IEICE Tech. Rep. **119**, 23–27 (2019). Publisher: IEICE.
- 52. Y.-C. Huang, J. Zhang, and S. Yu, "Self-learning Routing for Optical Networks," in *Optical Network Design and Modeling,* vol. 11616 A. Tzanakaki, M. Varvarigos, R. Muñoz, R. Nejabati, N. Yoshikane, M. Anastasopoulos, and J. Marquez-Barja, eds. (Springer International Publishing, Cham, 2020), pp. 467–478. Series Title: Lecture Notes in Computer Science.
- 53. Z. Zhao, Y. Zhao, H. Ma, Y. Li, S. Rahman, D. Han, H. Zhang, and J. Zhang, "Cost-efficient routing, modulation, wavelength and port assignment using reinforcement learning in optical transport networks," Opt. Fiber Technol. **64**, 102571 (2021).
- 54. M. Freire-Hermelo, A. Lavignotte, and C. Lepers, "Dynamic Modulation Format and Wavelength Assignment in Optical Networks using Reinforcement Learning," in *OSA Advanced Photonics Congress 2021,* (Optica Publishing Group, Washington, DC, 2021), p. NeF2B.4.
- <span id="page-12-6"></span>55. Y. Liu, B. Chen, G. Su, M. Dai, and X. Lin, "A Waveband Routing Method in Optical Networks Based on the Deep Reinforcement Learning," in *26th Optoelectronics and Communications Conference,* (Optica Publishing Group, Hong Kong, 2021), p. JS3C.1.
- <span id="page-12-9"></span>56. J. W. Nevin, S. Nallaperuma, N. A. Shevchenko, Z. Shabka, G. Zervas, and S. J. Savory, "Techniques for applying reinforcement learning to routing and wavelength assignment problems in optical fiber communication networks," J. Opt. Commun. Netw. **14**, 733–748 (2022).
- <span id="page-12-7"></span>57. N. Di Cicco, M. Ibrahimi, S. Troia, and M. Tornatore, "DeepLS: Local Search for Network Optimization based on Lightweight Deep Reinforcement Learning," IEEE Transactions on Netw. Serv. Manag. pp. 1–1 (2023).
- <span id="page-12-1"></span>58. S. Nallaperuma, Z. Gan, J. Nevin, M. Shevchenko, and S. J. Savory, "Interpreting multi-objective reinforcement learning for routing and wavelength assignment in optical networks," J. Opt. Commun. Netw. **15**, 497 (2023).
- <span id="page-12-2"></span>59. R. R. Reyes and T. Bauschert, "Adaptive and State-Dependent Online Resource Allocation in Dynamic Optical Networks," J. Opt. Commun. Netw. **9**, B64 (2017).
- 60. B. Li and Z. Zhu, "DeepCoop: Leveraging Cooperative DRL Agents to Achieve Scalable Network Automation for Multi-Domain SD-EONs," in *2020 Optical Fiber Communications Conference and Exhibition (OFC),* (2020), pp. 1–3.
- 61. X. Li, Y. Zhao, Y. Li, S. Rahman, F. Wang, X. Li, and J. Zhang, "Multi-Objective Routing and Resource Allocation Based on Reinforcement Learning in Optical Transport Networks," in *Asia Communications and Photonics Conference/International Conference on Information Photon-*

- *ics and Optical Communications 2020 (ACP/IPOC),* (Optica Publishing Group, Beijing, 2020), p. M4A.205.
- 62. R. Romero Reyes and T. Bauschert, "Towards DRL-based Routing and Spectrum Assignment in Optical Networks: Lessons to be Learned from Markov Decision Processes," in *2021 IEEE Latin-American Conference on Communications (LATINCOM),* (IEEE, Santo Domingo, Dominican Republic, 2021), pp. 1–6.
- <span id="page-12-10"></span>63. Z. Zhao, Y. Zhao, Y. Li, S. Rahman, D. Han, and J. Zhang, "Reinforced Resource Allocation based on n-Dimensional Matrix Diagram for Multi-Modal Optical Networks," in *26th Optoelectronics and Communications Conference,* (Optica Publishing Group, Hong Kong, 2021), p. JS2A.1.
- 64. Y. Wang, Y. Mori, and H. Hasegawa, "Dynamic Routing and Spectrum Allocation Based on Actor- critic Learning for Multi-fiber Elastic Optical Networks," in *Photonics in Switching and Computing 2021,* (Optica Publishing Group, Washington, DC, 2021), p. W1B.3.
- <span id="page-12-5"></span>65. H. T. Quang, O. Houidi, J. Errea-Moreno, D. Verchère, and D. Zeghlache, "MAGC-RSA: Multi-Agent Graph Convolutional Reinforcement Learning for Distributed Routing and Spectrum Assignment in Elastic Optical Networks," 2022 Eur. Conf. on Opt. Commun. (ECOC) pp. 1–4 (2022).
- 66. K. Cruzado, R. Shiraki, Y. Mori, T. Tanaka, K. Higashimori, F. Inuzuka, T. Ohara, and H. Hasegawa, "Reinforcement-Learning-based Network Design and Control with Stepwise Reward Variation and Link-Adjacency Embedding," in *2022 European Conference on Optical Communication (ECOC),* (2022), pp. 1–4.
- <span id="page-12-8"></span>67. L. Zhao, S. Yin, Y. Chai, Y. Jiao, and S. Huang, "A RSA Policy with Failure Probability Based on Reinforcement Learning in Multi-band Optical Network," in *2022 20th International Conference on Optical Communications and Networks (ICOCN),* (2022), pp. 1–3.
- <span id="page-12-12"></span>68. Y. Jiao, S. Yin, T. Jin, L. Liu, L. Zhao, and S. Huang, "Reliability-Oriented RSA Combined with Reinforcement Learning in Elastic Optical Networks," in *2022 20th International Conference on Optical Communications and Networks (ICOCN),* (IEEE, Shenzhen, China, 2022), pp. 1–3.
- 69. P. Almasan, J. Suárez-Varela, K. Rusek, P. Barlet-Ros, and A. Cabellos-Aparicio, "Deep reinforcement learning meets graph neural networks: Exploring a routing optimization use case," Comput. Commun. **196**, 184–194 (2022).
- 70. G. Zhang, H. Ding, Y. Wang, L. Wang, and X. Han, "A Service Routing Optimization Algorithm for Power Communication Optical Transport Network Based on Knowledge Graph and Reinforcement Learning," in *Proceedings of 2021 International Conference on Autonomous Unmanned Systems (ICAUS 2021),* vol. 861 M. Wu, Y. Niu, M. Gu, and J. Cheng, eds. (Springer Singapore, Singapore, 2022), pp. 1337–1346. Series Title: Lecture Notes in Electrical Engineering.
- 71. S. Arce, L. A. Albertini, I. Rios, D. P. Pinto-Roa, J. Colbes, and M. Villagra, "Reinforcement Learning applied to the Routing and Spectrum Assignment in Elastic Optical Networks," in *2022 IEEE Latin American Conference on Computational Intelligence (LA-CCI),* (IEEE, Montevideo, Uruguay, 2022), pp. 1–6.
- 72. P. Sharma, S. Gupta, V. Bhatia, and S. Prakash, "Deep reinforcement learning-based routing and resource assignment in quantum key distribution-secured optical networks," IET Quantum Commun. **4**, 136–145 (2023).
- 73. X. Lin, Y.-C. Huang, H. Zhang, and J. Zhang, "A Deep-Reinforcement-Learning-based Dynamic Scheduling of Delay-Tolerant Requests in Elastic Optical Networks," in *2023 Asia Communications and Photonics Conference/2023 International Photonics and Optoelectronics Meetings (ACP/POEM),* (2023), pp. 01–04.
- <span id="page-12-11"></span>74. C. Hernández-Chulde, R. Casellas, R. Martínez, R. Vilalta, and R. Muñoz, "Experimental evaluation of a latency-aware routing and spectrum assignment mechanism based on deep reinforcement learning," J. Opt. Commun. Netw. **15**, 925–937 (2023). Publisher: Optica Publishing Group.
- <span id="page-12-3"></span>75. J. Chen, X. Li, J. Wu, Y. Zheng, and W. Xiao, "GSADDQN: Combining GraphSAGE and reinforcement learning for routing optimization in software-defined optical transport network," Opt. Fiber Technol. **89**, 104059 (2024).

- <span id="page-13-0"></span>76. Y. Wang, Y. Mori, and H. Hasegawa, "Resource Assignment based on Core-State Value Evaluation to Handle Crosstalk and Spectrum Fragments in SDM Elastic Optical Networks," in *2020 Opto-Electronics and Communications Conference (OECC),* (IEEE, Taipei, Taiwan, 2020), pp. 1–3.
- <span id="page-13-7"></span>77. C. Shi, M. Zhu, J. Gu, T. Shen, and X. Ren, "Deep-reinforced impairment-aware dynamic resource allocation in nonlinear elastic optical networks," in *26th Optoelectronics and Communications Conference,* (Optica Publishing Group, Hong Kong, 2021), p. M4A.8.
- <span id="page-13-8"></span>78. M. Shimoda and T. Tanaka, "Deep Reinforcement Learning-based Spectrum Assignment with Multi-metric Reward Function and Assignable Boundary Slot Mask," in *2021 Opto-Electronics and Communications Conference (OECC),* (2021), pp. 1–3.
- 79. N. E. D. E. Sheikh, E. Paz, J. Pinto, and A. Beghelli, "Multi-band provisioning in dynamic elastic optical networks: a comparative study of a heuristic and a deep reinforcement learning approach," in *2021 International Conference on Optical Network Design and Modeling (ONDM),* (2021), pp. 1–3.
- <span id="page-13-3"></span>80. L. Xu, Y.-C. Huang, Y. Xue, and X. Hu, "Spectrum Continuity and Contiguity Aware State Representation for Deep Reinforcement Learning-Based Routing of EONs," in *2021 IEEE 6th Optoelectronics Global Conference (OGC),* (2021), pp. 73–76.
- <span id="page-13-9"></span>81. X. Chen, R. Proietti, C.-Y. Liu, and S. J. B. Yoo, "A Multi-Task-Learning-Based Transfer Deep Reinforcement Learning Design for Autonomic Optical Networks," IEEE J. on Sel. Areas Commun. **39**, 2878–2889 (2021).
- 82. M. Gonzalez, F. Condon, P. Morales, and N. Jara, "Improving Multi-Band Elastic Optical Networks Performance using Behavior Induction on Deep Reinforcement Learning," in *2022 IEEE Latin-American Conference on Communications (LATINCOM),* (IEEE, Rio de Janeiro, Brazil, 2022), pp. 1–6.
- <span id="page-13-14"></span>83. A. B. Terki, J. Pedro, A. Eira, A. Napoli, and N. Sambo, "Routing and Spectrum Assignment Assisted by Reinforcement Learning in Multiband Optical Networks," in *2022 European Conference on Optical Communication (ECOC),* (2022), pp. 1–4.
- <span id="page-13-10"></span>84. B. Tang, Y.-C. Huang, Y. Xue, and W. Zhou, "Deep Reinforcement Learning-Based RMSA Policy Distillation for Elastic Optical Networks," Mathematics. **10**, 3293 (2022).
- 85. L. Cheng and Y. Qiu, "Routing and spectrum assignment employing long short-term memory technique for elastic optical networks," Opt. Switch. Netw. **45**, 100684 (2022).
- <span id="page-13-11"></span>86. Y. Tu, B. Tang, and Y.-C. Huang, "Entropy-based Reward Design for Deep Reinforcement Learning-enabled Routing, Modulation and Spectrum Assignment of Elastic Optical Networks," in *2022 Asia Communications and Photonics Conference (ACP),* (2022), pp. 1168–1172.
- <span id="page-13-6"></span>87. J. Momo Ziazet and B. Jaumard, "Deep Reinforcement Learning for Network Provisioning in Elastic Optical Networks," in *ICC 2022 - IEEE International Conference on Communications,* (IEEE, Seoul, Korea, Republic of, 2022), pp. 4450–4455.
- <span id="page-13-16"></span>88. J. Pinto-Ríos, F. Calderón, A. Leiva, G. Hermosilla, A. Beghelli, D. Bórquez-Paredes, A. Lozada, N. Jara, R. Olivares, and G. Saavedra, "Resource Allocation in Multicore Elastic Optical Networks: A Deep Reinforcement Learning Approach," Complexity. **2023**, 1–13 (2023).
- <span id="page-13-4"></span>89. J. Errea, D. Djon, H. Q. Tran, D. Verchere, and A. Ksentini, "Deep Reinforcement Learning-aided Fragmentation-aware RMSA Path Computation Engine for Open Disaggregated Transport Networks," in *2023 International Conference on Optical Network Design and Modeling (ONDM),* (IEEE, Coimbra, Portugal, 2023), pp. 1–3.
- <span id="page-13-15"></span>90. A. Beghelli, P. Morales, E. Viera, N. Jara, D. Bórquez-Paredes, A. Leiva, and G. Saavedra, "Approaches to dynamic provisioning in multiband elastic optical networks," in *2023 International Conference on Optical Network Design and Modeling (ONDM),* (2023), pp. 1–6.
- 91. T. Tanaka and M. Shimoda, "Pre- and post-processing techniques for reinforcement-learning-based routing and spectrum assignment in elastic optical networks," J. Opt. Commun. Netw. **15**, 1019–1029 (2023). Publisher: Optica Publishing Group.
- <span id="page-13-12"></span>92. L. Xu, Y.-C. Huang, Y. Xue, and X. Hu, "Hierarchical Reinforcement Learning in Multi-Domain Elastic Optical Networks to Realize Joint

- RMSA," J. Light. Technol. **41**, 2276–2288 (2023).
- 93. R. Sadeghi, B. Correia, E. London, A. Napoli, N. Costa, J. Pedro, and V. Curri, "Performance Comparison of Optical Networks Exploiting Multiple and Extended Bands and Leveraging Reinforcement Learning," in *2023 International Conference on Optical Network Design and Modeling (ONDM),* (2023), pp. 1–6.
- <span id="page-13-13"></span>94. Y. Tang, D. Chen, M. You, and B. Xia, "A Routing and Spectrum Assignment Algorithm for Electric Power Elastic Optical Networks Based on Deep Reinforcement Learning," in *2023 2nd Asia Power and Electrical Technology Conference (APET),* (2023), pp. 729–733.
- 95. Y. Teng, C. Natalino, H. Li, R. Yang, J. Majeed, S. Shen, P. Monti, R. Nejabati, S. Yan, and D. Simeonidou, "Deep-reinforcement-learningbased RMSCA for space division multiplexing networks with multi-core fibers [Invited Tutorial]," J. Opt. Commun. Netw. **16**, C76 (2024).
- <span id="page-13-19"></span>96. Z. Xiong, Y.-C. Huang, and X. Hu, "Graph Attention Network Enhanced Deep Reinforcement Learning Framework for Routing, Modulation, and Spectrum Allocation in EONs," in *2024 Asia Communications and Photonics Conference (ACP) and International Conference on Information Photonics and Optical Communications (IPOC),* (IEEE, Beijing, China, 2024), pp. 1–6.
- 97. Y. Teng, C. Natalino, F. Arpanaei, A. Sánchez-Macián, P. Monti, S. Yan, and D. Simeonidou, "DRL-Assisted Dynamic QoT-Aware Service Provisioning in Multi-Band Elastic Optical Networks," (2024). URL: <https://arxiv.org/abs/2408.03221> (accessed 2024-08-12), version Number: 1.
- 98. E. Unzain, R. Fernandez, and D. P. Pinto-Roa, "Reinforcement Learning Based Routing, Modulation Level and Spectrum Assignment in Elastic Optical Networks," in *2024 L Latin American Computer Conference (CLEI),* (IEEE, Buenos Aires, Argentina, 2024), pp. 1–8.
- <span id="page-13-5"></span>99. Z. Zhou, R. Gu, X. Zhang, L. Yunxuan, L. Bai, and J. Yuefeng, "Opti-DeepRoute: A Topology-Adaptive Deep Reinforcement Learning Based Service Provisioning Framework for Elastic Optical Network," in *IEEE INFOCOM 2024 - IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS),* (IEEE, Vancouver, BC, Canada, 2024), pp. 1–2.
- 100. S. Li, X. Lin, Y. Liu, G. Li, and J. Li, "OpticGAI: Generative AI-aided Deep Reinforcement Learning for Optical Networks Optimization," in *Proceedings of the 1st SIGCOMM Workshop on Hot Topics in Optical Technologies and Applications in Networking,* (ACM, Sydney NSW Australia, 2024), pp. 1–6.
- 101. J. Xie, Y. Song, Y. Zhang, S. Li, M. Zhang, and D. Wang, "Physical Layer-Aware Route and Spectrum Allocation in Optical Networks by Multi-Objective Deep Reinforcement Learning," in *2024 Asia Communications and Photonics Conference (ACP) and International Conference on Information Photonics and Optical Communications (IPOC),* (IEEE, Beijing, China, 2024), pp. 1–4.
- <span id="page-13-1"></span>102. D. Yan, N. Feng, J. Lv, D. Ren, J. Hu, and J. Zhao, "DRL-based fragmentation- and impairment-aware resource allocation algorithm in C + L band elastic optical networks," Opt. Fiber Technol. **90**, 104133 (2024).
- <span id="page-13-2"></span>103. J. Boyan and M. Littman, "Packet Routing in Dynamically Changing Networks: A Reinforcement Learning Approach," in *Advances in Neural Information Processing Systems,* vol. 6 J. Cowan, G. Tesauro, and J. Alspector, eds. (Morgan-Kaufmann, 1993).
- 104. H. Ma, Y. Zhao, Y. Li, W. Wang, Y. Wang, D. Wang, C. Wan, and J. Zhang, "Demonstration of Image Processing Based on Reinforcement Learning in Multi-Modal Optical Transport Networks," in *2019 18th International Conference on Optical Communications and Networks (ICOCN),* (IEEE, Huangshan, China, 2019), pp. 1–3.
- <span id="page-13-17"></span>105. Z. Zhao, Y. Zhao, D. Wang, Y. Wang, and J. Zhang, "Reinforcement-Learning-Based Multi-Failure Restoration in Optical Transport Networks," in *2019 Asia Communications and Photonics Conference (ACP),* (2019), pp. 1–3.
- 106. X. Wang, Y.-C. Huang, J. Liu, and S. Yu, "A Subcarrier-Slot Autonomous Partition Scheme Based on Deep-Reinforcement-Learning in Elastic Optical Networks," in *2019 Asia Communications and Photonics Conference (ACP),* (2019), pp. 1–3.
- <span id="page-13-18"></span>107. X. Luo, C. Shi, L. Wang, X. Chen, Y. Li, and T. Yang, "Leveraging

double-agent-based deep reinforcement learning to global optimization of elastic optical networks with enhanced survivability," Opt. Express **27**, 7896 (2019).

- <span id="page-14-19"></span>108. C. Natalino and P. Monti, "The Optical RL-Gym: An open-source toolkit for applying reinforcement learning in optical networks," in *2020 22nd International Conference on Transparent Optical Networks (ICTON),* (2020), pp. 1–5. ISSN: 2161-2064.
- 109. Q. Ma, A. Xiong, P. Yu, S. Guo, N. Xing, W. Li, L. Feng, and Q. Xue-Song, "Co-Allocation of Service Routing in SDN-driven 5G IP+Optical Smart Grid Communication Networks based on Deep Reinforcement Learning," in *2020 International Wireless Communications and Mobile Computing (IWCMC),* (IEEE, Limassol, Cyprus, 2020), pp. 868–873.
- 110. C. Wang, N. Yoshikane, F. Balasis, and T. Tsuritani, "DeepCMS <sup>3</sup> : A Deep Reinforcement Learning Framework for Core, Mode and Spectrum Sequential Scheduling over Optical Transport Network," in *2020 European Conference on Optical Communications (ECOC),* (IEEE, Brussels, Belgium, 2020), pp. 1–4.
- <span id="page-14-15"></span>111. R. Weixer, S. Kuhl, R. M. Morais, B. Spinnler, W. Schairer, B. Sommerkorn-Krombholz, and S. Pachnicke, "A Reinforcement Learning Framework for Parameter Optimization in Elastic Optical Networks," in *2020 European Conference on Optical Communications (ECOC),* (IEEE, Brussels, Belgium, 2020), pp. 1–4.
- 112. H. Liu, R. Gu, Z. Li, and Y. Ji, "Multi-Agent Federated Reinforcement Learning for Privacy-enhanced Service Provision in Multi-domain Optical Network," in *2021 Asia Communications and Photonics Conference (ACP),* (2021), pp. 1–3.
- <span id="page-14-1"></span>113. Z. Zhao, Y. Zhao, Y. Li, F. Wang, X. Li, D. Han, and J. Zhang, "Service restoration in multi-modal optical transport networks with reinforcement learning," Opt. Express **29**, 3825 (2021).
- <span id="page-14-13"></span>114. X. Tian, B. Li, R. Gu, and Z. Zhu, "Reconfiguring multicast sessions in elastic optical networks adaptively with graph-aware deep reinforcement learning," J. Opt. Commun. Netw. **13**, 253–265 (2021). Publisher: Optica Publishing Group.
- <span id="page-14-20"></span>115. P. Morales, P. Franco, A. Lozada, N. Jara, F. Calderón, J. Pinto-Ríos, and A. Leiva, "Multi-band Environments for Optical Reinforcement Learning Gym for Resource Allocation in Elastic Optical Networks," in *2021 International Conference on Optical Network Design and Modeling (ONDM),* (2021), pp. 1–6.
- <span id="page-14-5"></span>116. T. Tanaka and K. Higashimori, "Reinforcement-Learning-based Multilayer Path Planning Framework that Designs Grooming, Route, Spectrum, and Operational Mode," in *2022 European Conference on Optical Communication (ECOC),* (2022), pp. 1–4.
- <span id="page-14-16"></span>117. R. Koch, S. Kühl, R. M. Morais, B. Spinnler, W. Schairer, B. Sommernkorn-Krombholz, and S. Pachnicke, "Reinforcement Learning for Generalized Parameter Optimization in Elastic Optical Networks," J. Light. Technol. **40**, 567–574 (2022). Publisher: Optica Publishing Group.
- <span id="page-14-11"></span>118. C. Hernández-Chulde, R. Casellas, R. Martínez, R. Vilalta, and R. Muñoz, "Evaluation of Deep Reinforcement Learning for Restoration in Optical Networks," in *2022 Optical Fiber Communications Conference and Exhibition (OFC),* (2022), pp. 1–3.
- <span id="page-14-8"></span>119. E. Etezadi, C. Natalino, R. Diaz, A. Lindgren, S. Melin, L. Wosinska, P. Monti, and M. Furdek, "DeepDefrag: A deep reinforcement learning framework for spectrum defragmentation," in *GLOBECOM 2022 - 2022 IEEE Global Communications Conference,* (2022), pp. 3694–3699.
- <span id="page-14-9"></span>120. E. Etezadi, C. Natalino, R. Diaz, A. Lindgren, S. Melin, L. Wosinska, P. Monti, and M. Furdek, "Deep reinforcement learning for proactive spectrum defragmentation in elastic optical networks," J. Opt. Commun. Netw. **15**, E86 (2023).
- <span id="page-14-2"></span>121. T. Tanaka, "Adaptive Traffic Grooming Using Reinforcement Learning in Multilayer Elastic Optical Networks," in *2023 Optical Fiber Communications Conference and Exhibition (OFC),* (2023), pp. 1–3.
- <span id="page-14-10"></span>122. S. S. Johari, S. Taeb, N. Shahriar, S. R. Chowdhury, M. Tornatore, R. Boutaba, J. Mitra, and M. Hemmati, "DRL-Assisted Reoptimization of Network Slice Embedding on EON-Enabled Transport Networks," IEEE Transactions on Netw. Serv. Manag. **20**, 800–814 (2023).
- <span id="page-14-6"></span>123. J. Zhang, Z. Chen, B. Zhang, R. Wang, H. Ma, and Y. Ji, "ADMIRE: collaborative data-driven and model-driven intelligent routing engine

- for traffic grooming in multi-layer X-Haul networks," J. Opt. Commun. Netw. **15**, A63–A73 (2023).
- <span id="page-14-3"></span>124. Y. Fan, Y. Li, B. Zhang, L. Chen, Y. Wang, J. Guo, W. Wang, Y. Zhao, and J. Zhang, "Blocking-Driven Spectrum Defragmentation Based on Deep Reinforcement Learning in Tidal Elastic Optical Networks," in *2023 21st International Conference on Optical Communications and Networks (ICOCN),* (2023), pp. 1–3.
- 125. M. Lian, Y. Zhao, Y. Li, A. Nag, and J. Zhang, "Dynamic slicing of multidimensional resources in DCI-EON with penalty-aware deep reinforcement learning," J. Opt. Commun. Netw. **16**, 112 (2024).
- <span id="page-14-14"></span>126. X. Li and Y. Wang, "TABDeep: A two-level action branch architecturebased deep reinforcement learning for distributed sub-tree scheduling of online multicast sessions in EON," Comput. Networks **243**, 110288 (2024).
- 127. Y. Wang, L. Kong, M. Zhu, J. Gu, Y. Cai, and J. Zhang, "Availability-Aware and Delay-Sensitive RAN Slicing Mapping Based on Deep Reinforcement Learning in Elastic Optical Networks," IEEE Transactions on Netw. Serv. Manag. pp. 1–1 (2024).
- 128. S. Yin, L. Liu, M. Cai, Y. Chai, Y. Jiao, Z. Duan, Y. Li, and S. Huang, "DNN distributed inference offloading scheme based on transfer reinforcement learning in metro optical networks," J. Opt. Commun. Netw. **16**, 852 (2024).
- <span id="page-14-18"></span>129. S. K. Tse, X. Zhao, A. Chan, D. Tang, A. Mohan, C. Natalino, and M. Aibin, "Reinforcement Learning for Power Management in Lowmargin Optical Networks," in *2024 24th International Conference on Transparent Optical Networks (ICTON),* (IEEE, Bari, Italy, 2024), pp. 1–4.
- <span id="page-14-7"></span>130. T. Tanaka, "Reinforcement-learning-based path planning in multilayer elastic optical networks [Invited]," J. Opt. Commun. Netw. **16**, A68–A77 (2024).
- <span id="page-14-26"></span>131. M. Doherty and A. Beghelli, "XLRON: Accelerated Reinforcement Learning Environments for Optical Networks," in *2024 Optical Fiber Communications Conference and Exhibition (OFC),* (2024), pp. 1–3.
- <span id="page-14-21"></span>132. C. Natalino, T. Magalhães, F. Arpanaei, F. R. L. Lobato, J. C. W. A. Costa, J. A. Hernández, and P. Monti, "Optical Networking Gym: an open-source toolkit for resource assignment problems in optical networks," J. Opt. Commun. Netw. **16**, G40 (2024).
- <span id="page-14-23"></span>133. R. McCann, A. Rezaee, and V. M. Vokkarane, "SDONSim: An Advanced Simulation Tool for Software-Defined Elastic Optical Networks," (2024). URL: <https://arxiv.org/abs/2410.13999> (accessed 2024-12-31), version Number: 1.
- <span id="page-14-0"></span>134. N. Jara, H. Pempelfort, E. Viera, J. Sanchez, G. España, and D. Borquez-Paredes, "DREAM-ON GYM: A Deep Reinforcement Learning Environment for Next-Gen Optical Networks:," in *Proceedings of the 14th International Conference on Simulation and Modeling Methodologies, Technologies and Applications,* (SCITEPRESS - Science and Technology Publications, Dijon, France, 2024), pp. 215–222.
- <span id="page-14-4"></span>135. R. Matzner, A. Ahuja, R. Sadeghi, M. Doherty, A. Beghelli, S. J. Savory, and P. Bayvel, "Topology Bench: Systematic Graph Based Benchmarking for Core Optical Networks," (2024). URL: [https://arxiv.org/abs/2411.](https://arxiv.org/abs/2411.04160) [04160](https://arxiv.org/abs/2411.04160) (accessed 2024-11-29), version Number: 1.
- <span id="page-14-12"></span>136. Z. Luo, S. Yin, L. Zhao, Z. Wang, W. Zhang, L. Jiang, and S. Huang, "Survivable Routing, Spectrum, Core and Band Assignment in Multi-Band Space Division Multiplexing Elastic Optical Networks," J. Light. Technol. **40**, 3442–3455 (2022).
- <span id="page-14-17"></span>137. R. Koch, S. Kuhl, W. Schairer, B. Spinnler, and S. Pachnicke, "High-Generalizability Reinforcement Learning Based Capacity Optimization in WDM Long-Haul Networks," IEEE Photonics Technol. Lett. **34**, 891– 894 (2022).
- <span id="page-14-22"></span>138. X. Chen, "DeepRMSA GitHub repository," URL: [https://github.com/](https://github.com/xiaoliangchenUCD/DeepRMSA) [xiaoliangchenUCD/DeepRMSA](https://github.com/xiaoliangchenUCD/DeepRMSA) (accessed 2024-01-06).
- <span id="page-14-24"></span>139. L. Engstrom, A. Ilyas, S. Santurkar, D. Tsipras, F. Janoos, L. Rudolph, and A. Madry, "Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO," (2020). URL: [http://arxiv.org/abs/](http://arxiv.org/abs/2005.12729) [2005.12729](http://arxiv.org/abs/2005.12729) (accessed 2023-07-08), arXiv:2005.12729 [cs, stat].
- <span id="page-14-25"></span>140. P. Nagarajan, G. Warnell, and P. Stone, "The Impact of Nondeterminism on Reproducibility in Deep Reinforcement Learning," in *2nd Reproducibility in Machine Learning Workshop at ICML 2018,* (Stockholm,

- Sweden, 2018).
- <span id="page-15-0"></span>141. S. Huang and S. Ontañón, "A Closer Look at Invalid Action Masking in Policy Gradient Algorithms," The Int. FLAIRS Conf. Proc. **35** (2022).
- <span id="page-15-1"></span>142. O. Vinyals, M. Fortunato, and N. Jaitly, "Pointer Networks," (2015). URL: <https://arxiv.org/abs/1506.03134> (accessed 2024-06-30), version Number: 2.
- <span id="page-15-2"></span>143. Michael Doherty, "2024\_jocn\_xlron (Revision 75def23)," (2024). URL: [https://huggingface.co/micdoh/2024\\_JOCN\\_XLRON](https://huggingface.co/micdoh/2024_JOCN_XLRON) .
- <span id="page-15-3"></span>144. S. Baroni, "Routing and wavelength allocation in WDM optical networks," Ph.D. thesis, University College London, United Kingdom (1998).
- <span id="page-15-4"></span>145. P. Henderson, R. Islam, P. Bachman, J. Pineau, D. Precup, and D. Meger, "Deep Reinforcement Learning that Matters," (2019). URL: <http://arxiv.org/abs/1709.06560> (accessed 2023-07-08), arXiv:1709.06560 [cs, stat].
- <span id="page-15-5"></span>146. M. Doherty, "XLRON: Accelerated Learning and Resource Allocation for Optical Networks," (2023). URL: [https://github.com/micdoh/XLRON.](https://github.com/micdoh/XLRON.git) [git](https://github.com/micdoh/XLRON.git) .
- <span id="page-15-6"></span>147. K. P. White and S. Robinson, "The problem of the initial transient (again), or why MSER works," in *Proceedings of the 2009 INFORMS Simulation Society Research Workshop,* L. H. Lee, M. E. Kuhl, J. W. Fowler, and S. Robinson, eds. (Institute for Operations Research and the Management Sciences, Baltimore, 2009), pp. 90–95.
- <span id="page-15-7"></span>148. V. Curri, "GNPy model of the physical layer for open and disaggregated optical networking \[Invited\]," J. Opt. Commun. Netw. **14**, C92–C104 (2022). Publisher: Optica Publishing Group.
- <span id="page-15-8"></span>149. H. Buglia, M. Jarmolovicius, A. Vasylchenkova, E. Sillekens, L. Galdino, ˇ R. I. Killey, and P. Bayvel, "A Closed-Form Expression for the Gaussian Noise Model in the Presence of Inter-Channel Stimulated Raman Scattering Extended for Arbitrary Loss and Fibre Length," J. Light. Technol. **41**, 3577–3586 (2023).
- <span id="page-15-9"></span>150. K. Cruzado, Y. Mori, S.-C. Lin, M. Matsuura, S. Subramaniam, and H. Hasegawa, "Effective Capacity Estimation Based on Cut-Set Load Analysis in Optical Path Networks," in *2023 International Conference on Photonics in Switching and Computing (PSC),* (2023), pp. 1–3.
- <span id="page-15-10"></span>151. K. Cruzado, Y. Mori, S.-C. Lin, M. Matsuura, S. Subramaniam, and H. Hasegawa, "Capacity-Bound Evaluation and Routing and Spectrum Assignment for Elastic Optical Path Networks with Distance-Adaptive Modulation," in *2024 Optical Fiber Communications Conference and Exhibition (OFC),* (2024), pp. 1–3.
- <span id="page-15-11"></span>152. A. Beghelli, "Resource allocation and scalability in dynamic wavelengthrouted optical networks," Ph.D. thesis, University of London (2006).
- <span id="page-15-12"></span>153. B. Awerbuch, Y. Azar, and S. Plotkin, "Throughput-competitive on-line routing," in *Proceedings of 1993 IEEE 34th Annual Foundations of Computer Science,* (IEEE, Palo Alto, CA, USA, 1993), pp. 32–40.
- <span id="page-15-13"></span>154. B. Li and Z. Zhu, "GNN-Based Hierarchical Deep Reinforcement Learning for NFV-Oriented Online Resource Orchestration in Elastic Optical DCIs," J. Light. Technol. **40**, 935–946 (2022).

## **A. APPENDIX: DATA FROM PREVIOUS WORKS AND OUR BENCHMARKS**

Comparison of service blocking probabilities for KSP-FF and RL solutions across various topologies and traffic loads.

|             | Topology | Nslots | Load<br>(Erlang) | Service blocking probability (%) |         |             |             | Mean         |             |
|-------------|----------|--------|------------------|----------------------------------|---------|-------------|-------------|--------------|-------------|
| Publication |          |        |                  | Published                        |         | Ours        |             |              | improvement |
|             |          |        |                  | RL                               | 5-SP-FF | 5-SP-FF     | 5-SP-FFhops | 50-SP-FFhops | over RL (%) |
| DeepRMSA    | NSFNET   | 100    | 250              | 4.00                             | 5.10    | 5.00 ± 0.29 | 2.93 ± 0.22 | 2.33 ± 0.25  | 42          |
| DeepRMSA    | COST239  | 100    | 600              | 5.75                             | 6.75    | 6.69 ± 0.35 | 3.80 ± 0.39 | 2.61 ± 0.36  | 55          |
| Reward-RMSA | NSFNET   | 100    | 168              | 0.35                             | 1.00    | 1.06 ± 0.11 | 0.10 ± 0.02 | 0.02 ± 0.01  | 94          |
| Reward-RMSA | NSFNET   | 100    | 182              | 0.70                             | 1.40    | 1.53 ± 0.15 | 0.25 ± 0.03 | 0.08 ± 0.03  | 89          |
| Reward-RMSA | NSFNET   | 100    | 196              | 1.20                             | 2.10    | 2.06 ± 0.12 | 0.48 ± 0.07 | 0.21 ± 0.04  | 83          |
| Reward-RMSA | NSFNET   | 100    | 210              | 1.80                             | 2.70    | 2.68 ± 0.20 | 0.95 ± 0.11 | 0.47 ± 0.05  | 74          |
| GCN-RMSA    | NSFNET   | 100    | 154              | 0.51                             | 0.67    | 0.69 ± 0.08 | 0.03 ± 0.02 | 0.01 ± 0.00  | 98          |
| GCN-RMSA    | NSFNET   | 100    | 168              | 0.66                             | 1.00    | 1.06 ± 0.11 | 0.10 ± 0.02 | 0.02 ± 0.01  | 97          |
| GCN-RMSA    | NSFNET   | 100    | 182              | 0.98                             | 1.42    | 1.53 ± 0.15 | 0.25 ± 0.03 | 0.08 ± 0.03  | 92          |
| GCN-RMSA    | NSFNET   | 100    | 196              | 1.50                             | 2.10    | 2.06 ± 0.12 | 0.48 ± 0.07 | 0.21 ± 0.04  | 86          |
| GCN-RMSA    | NSFNET   | 100    | 210              | 2.10                             | 2.76    | 2.68 ± 0.20 | 0.95 ± 0.11 | 0.47 ± 0.05  | 78          |
| GCN-RMSA    | COST239  | 100    | 368              | 0.71                             | 0.78    | 0.80 ± 0.08 | 0.07 ± 0.03 | 0.00 ± 0.00  | 100         |
| GCN-RMSA    | COST239  | 100    | 391              | 0.85                             | 1.30    | 1.13 ± 0.12 | 0.17 ± 0.07 | 0.00 ± 0.00  | 100         |
| GCN-RMSA    | COST239  | 100    | 414              | 1.25                             | 1.70    | 1.57 ± 0.13 | 0.28 ± 0.09 | 0.01 ± 0.01  | 100         |
| GCN-RMSA    | COST239  | 100    | 437              | 1.75                             | 2.30    | 2.02 ± 0.13 | 0.46 ± 0.11 | 0.02 ± 0.02  | 99          |
| GCN-RMSA    | COST239  | 100    | 460              | 2.10                             | 2.70    | 2.53 ± 0.21 | 0.73 ± 0.20 | 0.07 ± 0.03  | 97          |
| GCN-RMSA    | USNET    | 100    | 320              | 0.65                             | 0.75    | 0.98 ± 0.10 | 0.25 ± 0.07 | 0.00 ± 0.01  | 100         |
| GCN-RMSA    | USNET    | 100    | 340              | 0.83                             | 1.20    | 1.31 ± 0.16 | 0.42 ± 0.07 | 0.01 ± 0.02  | 99          |
| GCN-RMSA    | USNET    | 100    | 360              | 1.05                             | 1.50    | 1.69 ± 0.12 | 0.73 ± 0.16 | 0.04 ± 0.04  | 96          |
| GCN-RMSA    | USNET    | 100    | 380              | 1.60                             | 2.15    | 2.18 ± 0.19 | 1.05 ± 0.19 | 0.09 ± 0.09  | 94          |
| GCN-RMSA    | USNET    | 100    | 400              | 2.20                             | 2.70    | 2.79 ± 0.24 | 1.53 ± 0.18 | 0.23 ± 0.09  | 90          |
| MaskRSA     | NSFNET   | 80     | 80               | 0.01                             | 0.26    | 0.33 ± 0.06 | 0.00 ± 0.00 | 0.00 ± 0.00  | 100         |
| MaskRSA     | NSFNET   | 80     | 90               | 0.05                             | 0.60    | 0.64 ± 0.07 | 0.01 ± 0.01 | 0.00 ± 0.00  | 100         |
| MaskRSA     | NSFNET   | 80     | 100              | 0.20                             | 0.90    | 1.08 ± 0.10 | 0.08 ± 0.05 | 0.04 ± 0.02  | 80          |
| MaskRSA     | NSFNET   | 80     | 110              | 0.50                             | 1.80    | 1.68 ± 0.11 | 0.25 ± 0.09 | 0.13 ± 0.03  | 74          |
| MaskRSA     | NSFNET   | 80     | 120              | 0.79                             | 2.47    | 2.39 ± 0.14 | 0.60 ± 0.14 | 0.33 ± 0.12  | 58          |
| MaskRSA     | NSFNET   | 80     | 130              | 1.80                             | 3.00    | 3.14 ± 0.22 | 1.35 ± 0.12 | 0.86 ± 0.14  | 52          |
| MaskRSA     | NSFNET   | 80     | 140              | 3.00                             | 4.00    | 4.05 ± 0.21 | 2.26 ± 0.23 | 1.71 ± 0.27  | 43          |
| MaskRSA     | NSFNET   | 80     | 150              | 4.30                             | 5.00    | 5.19 ± 0.28 | 3.43 ± 0.21 | 2.84 ± 0.26  | 34          |
| MaskRSA     | NSFNET   | 80     | 160              | 5.30                             | 6.00    | 6.37 ± 0.26 | 4.65 ± 0.35 | 4.15 ± 0.27  | 22          |
| MaskRSA     | JPN48    | 80     | 120              | 0.05                             | 1.60    | 1.92 ± 0.27 | 0.32 ± 0.08 | 0.00 ± 0.00  | 100         |
| MaskRSA     | JPN48    | 80     | 130              | 0.20                             | 2.50    | 2.75 ± 0.31 | 0.64 ± 0.10 | 0.02 ± 0.01  | 90          |
| MaskRSA     | JPN48    | 80     | 140              | 0.55                             | 3.50    | 3.69 ± 0.30 | 0.97 ± 0.14 | 0.04 ± 0.03  | 93          |
| MaskRSA     | JPN48    | 80     | 150              | 0.90                             | 4.50    | 4.55 ± 0.32 | 1.41 ± 0.15 | 0.09 ± 0.04  | 90          |
| MaskRSA     | JPN48    | 80     | 160              | 1.60                             | 5.00    | 5.40 ± 0.36 | 2.00 ± 0.21 | 0.18 ± 0.04  | 89          |

## continued from previous page

|             |          |        | Load     | Service blocking probability (%) |         |             |             |              | Mean        |
|-------------|----------|--------|----------|----------------------------------|---------|-------------|-------------|--------------|-------------|
| Publication | Topology | Nslots |          | Published                        |         | Ours        |             |              | improvement |
|             |          |        | (Erlang) | RL                               | 5-SP-FF | 5-SP-FF     | 5-SP-FFhops | 50-SP-FFhops | over RL (%) |
| PtrNet-RSA  | NSFNET   | 40     | 180      | 0.01                             | 0.80    | 0.93 ± 0.11 | 0.00 ± 0.00 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | NSFNET   | 40     | 190      | 0.03                             | 1.25    | 1.27 ± 0.10 | 0.01 ± 0.01 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | NSFNET   | 40     | 200      | 0.08                             | 1.50    | 1.68 ± 0.10 | 0.02 ± 0.01 | 0.00 ± 0.01  | 100         |
| PtrNet-RSA  | NSFNET   | 40     | 210      | 0.19                             | 1.90    | 2.06 ± 0.11 | 0.09 ± 0.04 | 0.03 ± 0.02  | 84          |
| PtrNet-RSA  | NSFNET   | 40     | 220      | 0.23                             | 2.50    | 2.58 ± 0.11 | 0.22 ± 0.09 | 0.09 ± 0.05  | 61          |
| PtrNet-RSA  | NSFNET   | 40     | 230      | 0.75                             | 2.90    | 3.14 ± 0.14 | 0.48 ± 0.12 | 0.26 ± 0.10  | 65          |
| PtrNet-RSA  | NSFNET   | 40     | 240      | 1.30                             | 3.50    | 4.01 ± 0.22 | 0.90 ± 0.18 | 0.54 ± 0.15  | 58          |
| PtrNet-RSA  | COST239  | 40     | 340      | 0.01                             | 2.50    | 3.36 ± 0.16 | 0.02 ± 0.02 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | COST239  | 40     | 360      | 0.04                             | 3.25    | 4.02 ± 0.20 | 0.04 ± 0.02 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | COST239  | 40     | 380      | 0.12                             | 3.80    | 4.72 ± 0.29 | 0.10 ± 0.03 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | COST239  | 40     | 400      | 0.24                             | 4.60    | 5.43 ± 0.36 | 0.25 ± 0.09 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | COST239  | 40     | 420      | 0.39                             | 5.50    | 6.24 ± 0.25 | 0.46 ± 0.12 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | USNET    | 40     | 210      | 0.01                             | 0.85    | 1.02 ± 0.20 | 0.14 ± 0.05 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | USNET    | 40     | 220      | 0.08                             | 1.40    | 1.46 ± 0.25 | 0.29 ± 0.08 | 0.00 ± 0.01  | 100         |
| PtrNet-RSA  | USNET    | 40     | 230      | 0.22                             | 1.85    | 1.99 ± 0.31 | 0.46 ± 0.10 | 0.02 ± 0.01  | 91          |
| PtrNet-RSA  | USNET    | 40     | 240      | 0.38                             | 2.20    | 2.59 ± 0.38 | 0.77 ± 0.18 | 0.08 ± 0.06  | 79          |
| PtrNet-RSA  | USNET    | 40     | 250      | 0.68                             | 3.10    | 3.25 ± 0.32 | 1.19 ± 0.28 | 0.19 ± 0.09  | 72          |
| PtrNet-RSA  | USNET    | 40     | 260      | 1.10                             | 3.60    | 3.87 ± 0.49 | 1.81 ± 0.35 | 0.42 ± 0.15  | 62          |
| PtrNet-RSA  | USNET    | 40     | 270      | 1.80                             | 4.40    | 4.67 ± 0.50 | 2.39 ± 0.41 | 0.72 ± 0.27  | 60          |
| PtrNet-RSA  | USNET    | 40     | 280      | 2.20                             | 4.90    | 5.40 ± 0.46 | 3.16 ± 0.48 | 1.25 ± 0.34  | 43          |
| PtrNet-RSA  | NSFNET   | 80     | 200      | 0.01                             | 0.60    | 0.61 ± 0.09 | 0.00 ± 0.00 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | NSFNET   | 80     | 210      | 0.03                             | 0.80    | 0.83 ± 0.10 | 0.00 ± 0.00 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | NSFNET   | 80     | 220      | 0.11                             | 1.20    | 1.07 ± 0.09 | 0.02 ± 0.02 | 0.01 ± 0.02  | 91          |
| PtrNet-RSA  | NSFNET   | 80     | 230      | 0.16                             | 1.40    | 1.32 ± 0.13 | 0.05 ± 0.03 | 0.02 ± 0.02  | 88          |
| PtrNet-RSA  | NSFNET   | 80     | 240      | 0.50                             | 1.90    | 1.63 ± 0.15 | 0.11 ± 0.06 | 0.05 ± 0.04  | 90          |
| PtrNet-RSA  | COST239  | 80     | 420      | 0.01                             | 2.50    | 2.66 ± 0.11 | 0.08 ± 0.03 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | COST239  | 80     | 440      | 0.16                             | 3.00    | 3.05 ± 0.16 | 0.13 ± 0.06 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | COST239  | 80     | 460      | 0.65                             | 3.50    | 3.52 ± 0.19 | 0.25 ± 0.07 | 0.01 ± 0.01  | 98          |
| PtrNet-RSA  | USNET    | 80     | 260      | 0.03                             | 1.00    | 1.21 ± 0.18 | 0.46 ± 0.13 | 0.00 ± 0.00  | 100         |
| PtrNet-RSA  | USNET    | 80     | 270      | 0.09                             | 1.20    | 1.48 ± 0.24 | 0.64 ± 0.18 | 0.16 ± 0.09  | -78         |
| PtrNet-RSA  | USNET    | 80     | 280      | 0.15                             | 1.40    | 1.78 ± 0.20 | 0.87 ± 0.21 | 0.38 ± 0.13  | -153        |
| PtrNet-RSA  | USNET    | 80     | 290      | 0.29                             | 1.70    | 2.13 ± 0.24 | 1.12 ± 0.24 | 0.54 ± 0.15  | -86         |
| PtrNet-RSA  | USNET    | 80     | 300      | 0.52                             | 2.20    | 2.46 ± 0.23 | 1.42 ± 0.29 | 0.61 ± 0.20  | -33         |
| PtrNet-RSA  | USNET    | 80     | 310      | 0.66                             | 2.40    | 2.79 ± 0.26 | 1.75 ± 0.32 | 0.88 ± 0.23  | -33         |
| PtrNet-RSA  | USNET    | 80     | 320      | 1.00                             | 2.80    | 3.18 ± 0.31 | 2.08 ± 0.35 | 1.15 ± 0.26  | -15         |
| PtrNet-RSA  | USNET    | 80     | 330      | 1.50                             | 3.10    | 3.50 ± 0.28 | 2.42 ± 0.31 | 1.46 ± 0.30  | 3           |
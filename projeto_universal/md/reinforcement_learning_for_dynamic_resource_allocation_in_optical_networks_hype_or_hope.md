---
title: "Reinforcement learning for dynamic resource allocation in optical networks: hype or hope?"
tema_principal: projeto_universal
temas_relacionados: []
ano: 2025
autores: []
veiculo: null
pdf: ../pdf/reinforcement_learning_for_dynamic_resource_allocation_in_optical_networks_hype_or_hope.pdf
---

# Reinforcement learning for dynamic resource allocation in optical networks: hype or hope?

**Michael Doherty,\* Robin Matzner, Rasoul Sadeghi, Polina Bayvel, AND Alejandra Beghelli**

Optical Networks Group, University College London, Torrington Place, London WC1E 7JE, UK \*michael.doherty.21@ucl.ac.uk

Received 19 February 2025; revised 20 April 2025; accepted 5 May 2025; published 26 June 2025

**The application of reinforcement learning (RL) to dynamic resource allocation in optical networks has been the focus of intense research activity in recent years, with almost 100 peer-reviewed papers. We present a review of progress in this field and identify weaknesses in benchmarking practices and reproducibility. To demonstrate best practice, we exactly recreate the problem settings from five landmark papers and apply improved benchmarks. To determine the best benchmarks, we evaluate several heuristic algorithms and optimize the candidate path count and sort criteria for path selection. We apply the improved benchmarks and demonstrate that simple heuristics outperform the published RL solutions, often with an order of magnitude lower blocking probability. Finally, to estimate the limits of improvement on the benchmarks, we present empirical lower bounds on blocking probability using a novel, to our knowledge, defragmentation-based method. Our method estimates that traffic load can be increased by 19%–36% for the same blocking in our examples, which may motivate further research on optimized resource allocation. We make our simulation framework and results openly available to promote reproducible research and standardized evaluation: https://doi.org/10.5281/zenodo.12594495.** © 2025 Optica Publishing Group. All rights, including for text and data mining (TDM), Artificial Intelligence (AI) training, and similar technologies, are reserved.

https://doi.org/10.1364/JOCN.559990

# 1. INTRODUCTION

Network operators are faced with a problem: how to increase capacity for fast-growing data traffic without increasing the price of services [1]. Advances in transmission technology have so far provided the solution by exponentially increasing the point-to-point capacity of the optical channel. However, as the throughput of the installed C + L bands approaches the nonlinearity-limited information bounds [2], costly infrastructure upgrades are required to scale capacity through spatial division multiplexing or ultra-wideband transmission [3]. Operators seek to minimize or delay the required capital expenditure and offset it with reduced operational costs. Online optimization of network resource allocation offers a path toward these aims by increasing the achievable network throughput with dynamic and automated service provisioning.

Reinforcement learning (RL) has emerged as a promising technique for dynamic resource allocation (DRA) from a range of exact solution methods, heuristic algorithms, and artificial intelligence (AI) approaches. RL solutions can approach the quality of exact methods such as integer linear programming (ILP), with an online allocation time comparable to simple heuristics [4]. In fact, many works have demonstrated RL solutions that are superior to selected heuristics across various optical network problems (see Section 3).

However, despite the many papers that investigate RL for optical networks, adoption of machine learning (ML) techniques by network operators has been limited by nontechnological barriers [5]. One barrier is a lack of clear benchmarks and demonstrable benefits. Studies of resource allocation problems in optical networks often present results on specific topologies and traffic models, without a fair comparison to previous results. Often, results are not generalizable.

In this paper, we address this barrier by providing an analysis of, and recommendations for, benchmarking practices. We identify five papers that provide the best examples of benchmarking in the field and exactly recreate their problem settings. By "problem settings," we mean the exact network topologies, traffic models, and other details of the network simulations. We then evaluate a range of heuristic algorithms and apply the best to each case. The best heuristic algorithms outperform or equal the reported RL results in all cases.

To understand if it is possible to improve on these new benchmarks, we propose a heuristic-based lower bound network blocking estimation method, termed resource-prioritized defragmentation (Section 6). For each case of study, we apply this method over a range of traffic loads and estimate that the supported traffic load at a fixed blocking (0.1%) may be increased by 19%–36% for flex-grid networks. These estimates suggest further improvement is possible.

This is the first time that a thorough analysis and benchmarking of previous work have been carried out and highlights deficient benchmarking standards. Our findings suggest that previous attempts to find better resource allocation policies using RL have been unsuccessful, and new efforts are required to find solutions, using RL or other methods, that improve on the best benchmarks and approach the estimated bounds.

This paper aims to 1) promote higher standards for evaluation and benchmarking in research on RL for DRA; 2) improve reproducibility and transparency of research by open-sourcing our simulation framework and providing discussion of implementation details that significantly affect results (e.g., path ordering in Section 4.A and holding time truncation in Section 5.A); and 3) encourage new research into optimized DRA by demonstrating that previous RL approaches have failed to beat our benchmarks, but there remains a considerable optimality gap between the benchmarks and our estimated bounds.

The contributions of this work are the following:

- 1. A comprehensive survey of progress on RL approaches to DRA in optical networks.
- 2. A systematic study of the factors affecting heuristic algorithm performance and recommendations for better heuristic benchmarks.
- 3. A recreation of problems from five landmark papers in the field, with comparisons to improved heuristic benchmarks, showing previous RL results have failed to improve on heuristics.
- 4. The introduction of a novel empirical throughput bound estimation method, which shows that benchmarks can be improved.
- 5. The release of our simulation framework, "XLRON," to promote reproducible research and enable fair comparison across different studies.

All of the code necessary to generate data and plots from this paper is available on GitHub Code 1, Ref. [6].

We begin with essential background on DRA problems and RL techniques in Section 2, followed by a literature review in Section 3. Section 4 presents the investigation of heuristic algorithms for benchmarking. Section 5 details the analysis of the previously published results and comparison with benchmarks. Section 6 presents new empirical bounds for network throughput, with recommendations for future research directions in Section 7.

# 2. BACKGROUND

#### A. DRA Problems in Optical Networks

# 1. Motivation for Dynamic Operation and RL

As discussed by Augé [7] and Pointurier [8], optical networks must operate with a margin of additional resources between the minimum requirements to fulfill a data service request and the resources allocated to that request, for example, by allocating additional spectrum. This margin is required due to uncertainty in the physical parameters of the transmission network or future traffic variations. Reducing the margin can increase the network throughput or reduce costs.

Dynamic operation allows the allocated resources to vary temporally in response to shifting traffic, thereby allowing more accurate matching of resources to current demand, which reduces margins. The time constraints of dynamic operation may preclude exact solution methods, but a trained RL agent can compute an allocation in sub-second time [4].

RL is appropriate for these problems because they possess three characteristics that merit the application of AI [9]: 1) a large combinatorial search space, 2) a clear objective function for optimization, and 3) plentiful training data and/or accurate and efficient simulators for data generation.

## 2. Traffic Models

Network traffic comprises a set of requests to connect source and destination nodes with fixed data rates on dedicated lightpaths. Traffic can be modeled as static, incremental, or dynamic [10].

Static traffic assumes knowledge of all connection requests that the network must accommodate. Incremental traffic lies between static and dynamic in stochasticity: requests are not known in advance, but do not expire once allocated. For dynamic traffic, connection requests are served on demand without knowledge of future requests, and active connections expire randomly. The request arrival and expiry times are sampled from probability distributions, often assumed to be exponential [11]. Dynamic traffic is considered a paradigm for future optical networks that have the necessary systems in place to enable real-time response to changing network conditions [12].

## 3. Problem Variants

The classic optimization problem in an optical network is routing and wavelength assignment (RWA) for fixed-grid networks or routing and spectrum assignment (RSA) for flex-grid networks, where spectrum is divided into frequency slot units (FSUs) [13]. Further degrees of freedom in the optimization are added by considering the selection of Modulation formats (RMSA), and the fiber Core or spectral transmission Band utilized by each channel in the case of multi-core or multi-band networks (RCMSA/RBMSA). Launch Power has also been considered as a parameter in the optimization objective for dynamic networks (RPMSA) [14,15].

While most DRA problems in optical networks from the literature are concerned with point-to-point connections, some consider virtual networking tasks such as virtual optical network embedding (VONE) [16,17] or virtual network function (VNF) placement [18]. We choose to focus on RWA/RSA/RMSA in this paper because they are the most widely studied DRA problems in the context of optical networks, and they form a core sub-task of variants such as VNF or VONE.

#### 4. Constraints

Three fundamental constraints govern resource allocation in optical networks:

- 1. Spectrum continuity: a lightpath must use identical FSUs on each link, without wavelength conversion.
- 2. Spectrum contiguity: an FSU allocated to a lightpath must be adjacent.
- 3. No reconfiguration: active lightpaths cannot be reallocated once established, meaning allocation decisions are permanent while connections remain active.

The "No Reconfiguration" constraint is not a physical limitation but an operational assumption that active services cannot be disrupted. Reconfiguration may sometimes be desirable, especially in flex-grid networks that may suffer from spectral fragmentation [19], and has been used in a production network by Meta Platforms Inc. to free up spectral resources [20].

#### 5. Solution Methods

Allocation of static traffic is an NP-hard combinatorial optimization problem [21], for which the computational complexity of finding a solution scales super-polynomially with the space of possible allocations. Exact solution methods such as ILP have been formulated for static traffic [22,23] but show limited scalability and are infeasible for dynamic traffic without a priori knowledge of all requests. [Jaumard *et al.* [23] scale their ILP formulation to 690 requests on the USNET topology (24 nodes and 86 links) with 380 FSUs per link, without considering distance-adaptive modulation formats.]

For dynamic traffic, any allocation decision must be taken within the constraint of the time interval between request arrivals. No standard limit has been defined for this constraint in the literature, but it could be on the order of seconds, with a lower limit set by the switching time of reconfigurable optical add-drop multiplexers (currently 1 to 100 ms, depending on the switching technology [24]).

Many simple heuristic algorithms [25–29] have been proposed for these problems, with the goal to minimize resources, lightpath distances, and required bandwidth. Heuristics have the advantages of fast execution time and deterministic and interpretable allocation decisions.

Machine learning approaches to DRA problems have included nature-inspired techniques such as particle swarm optimization (PSO) [30] and genetic algorithms (GAs) [31]. Once trained, an RL policy can compute an allocation faster than other ML approaches [4].

# B. Reinforcement Learning

RL is a framework for learning to optimize sequential decision making under uncertainty. It emerged from Bellman's foundational work on optimal control theory in the 1950s, specifically dynamic programming and Markov decision processes (MDPs) [32,33]. MDPs model decision-making processes as an agent that takes actions in an environment to maximize a reward signal. The method of action selection is a mapping from states to actions termed the policy, which can be expressed in a tabular form or approximated by a neural network (NN). The use of an NN for function approximation is sometimes distinguished as "Deep" RL. Tabular RL has been applied to optical networks [34], but function approximation with an NN is widely used [11,28,35–37] when the set of state-action pairs is too large to be tabulated [38].

The reader is referred to Sutton and Barto's authoritative textbook [38] for details. However, to aid the discussion of RL applied to DRA problems, several terms are defined here.

RL algorithms can be classified as model-based or modelfree. Model-based RL uses a model of the environment to plan future actions, but so far, no works have applied this paradigm to DRA problems in optical networks. Model-free RL algorithms learn through direct interaction with the environment, without planning. Model-free algorithms can be further categorized as follows:

- **Action-value methods**, such as Q-learning, which learn to estimate the value of taking actions in different environment states. These methods were the first to be developed in RL [39,40] and have been used for route selection in optical networks [41].
- **Policy gradient methods**, which directly optimize the policy parameters to maximize expected rewards. These methods can handle continuous action spaces, unlike action-value methods, which optimize an action-value function. Policy gradient methods are enhanced by using an actor–critic architecture, as in algorithms such as A2C [42] and PPO [43], which reduce variance in the policy gradient by using a learned value function (critic) to estimate the value of each state. Policy gradient methods have been used in many works on DRA in optical networks, such as A2C for DeepRMSA [11].

# 3. LITERATURE SURVEY

There exists a considerable body of literature on RL for DRA problems in optical networks. DRA in optical networks is distinguished from similar problems in electronically linked networks by the nature of fiber optic links, which carry a set of wavelengths or FSUs, defined by the ITU standards G.671 and G.694.2 [44,45]. In this work, we only consider publications related to optical networks but acknowledge the closely related literature on RL for other graph-based resource allocation problems.

## A. Survey Methodology

To provide an overview of research progress on RL applied to DRA problems in optical networks, we gathered all relevant research papers. We performed a manual review of results from citation databases to create the final set of 97 peer-reviewed papers. Figure 1 shows the count of papers by publication year. The papers are grouped in four categories: "RWA," "RSA," "RMSA," and "Other." We use this set of papers for our analysis of benchmarking practices in the field, which we present in the following section with further commentary on Fig. 1.

![](_page_3_Figure_3.jpeg)

Fig. 1. Count of publications related to RL for resource allocation problems in optical networks. Citations for each classification category are as follows: RWA [4,46–58], RSA [37,59–75], RMSA [11,28,34–36,41,76–102], and Other [103–134].

## B. Review of Benchmarking Practices

In optical networks research, the first benchmark for RL was established by DeepRMSA [11] (discussed in detail in Section 3.D). DeepRMSA was the first RL approach to achieve a lower service blocking probability than KSP-FF or any heuristic that considers multiple candidate paths. As a result of this breakthrough performance and its open-source codebase, the problem definition from DeepRMSA (topologies, traffic model, modulation format reach, FSU per link, etc.) became a *de facto* standard. Follow-up works used identical or similar problem definitions and compared them to DeepRMSA on their problem [28,36,37,65,80,89,99,102]. Arguably, comparing them to DeepRMSA has become standard benchmarking practice.

Previous work has called for more rigorous benchmarking practices for research on RL for optical networking [4], with recommendations for comparison against other machine learning approaches such as GA and PSO, in addition to estimated bounds on network blocking or throughput. Some studies of RL for resource allocation have restricted themselves to sufficiently small problem sizes and static traffic to enable comparison to ILP results [4,55,57,67,87]. Although this provides a reliable bound, it is not applicable to dynamic traffic.

Benchmarking against standard heuristic algorithms, such as KSP-FF, avoids the complexity of training a competing machine learning approach, performs deterministic allocation, and can scale to large problem instances. However, it is important to choose the best-performing heuristic for a particular case of study as a benchmark. Of the papers that benchmark their RL solution to KSP-FF (or other heuristics that consider multiple candidate paths) [4,11,28,34–37,56,63,65, 74,77,78,80,81,84–86,89,92–94,113,121,124], most achieve a 20%–30% reduction in service blocking probability compared to their best heuristic. Only three papers achieve a reduction greater than this: MaskRSA [35], PtrNet-RSA [37], and Terki *et al.* [83]. Despite these impressive results, we demonstrate in Section 5 that MaskRSA and PtrNet-RSA are beaten by KSP-FF or FF-KSP by considering 50 candidate paths and ordering the paths by number of hops. (We have not re-created the study of Terki *et al*. for benchmarking in Section 5, as it is multi-band and out of scope of this work. We hypothesize that their approach performs strongly because, similar to PtrNet-RSA, it is not limited to selecting from only K paths.)

Benchmarking is further complicated by the fast evolution of optical networking, with novel paradigms such as multi-band [90] and multi-core [88] emerging, and the wide variety of network topologies [135] and components that can be considered. The evolution of optical networks research is evidenced by growth in the "Other" category of Fig. 1, which includes papers on RL applied to traffic grooming [116,121,123,130], defragmentation [119,120,122,124], survivability or service restoration [67,68,105,107,113,118,136], multicast provisioning [46,114,126], and other problems such as transceiver parameter optimization [111,117,137] or launch power optimization [129].

The establishment of reliable benchmarks is made more difficult by the fragmented software environment for optical network simulations for RL. Several open-source toolkits have been introduced to aid researchers and improve productivity, but none have proved sufficiently popular for it to become standard. Optical-RL-Gym [108] was the first paper to attempt to introduce a new standard library for this task. This was followed by an extension to multi-band environments [115], and in 2024, it was further extended to include a more sophisticated physical layer model for lightpath SNR calculations, renamed as the Optical Networking Gym [132]. Additionally, MaskRSA provides an open-source simulation framework (RSA-RL) [35], and DeepRMSA's codebase is widely used [138]. SDONSim [133] and DREAM-ON-GYM [134] are other recent additions to the landscape of available simulation frameworks that further fragment the available options.

In summary, progress in applying RL to DRA problems in optical networks has been difficult to quantify due to several factors. First, the lack of standardized benchmarking practices has made it challenging to fairly compare different approaches. Second, while some studies have used ILP solutions as benchmarks, these are limited to small problem sizes and static traffic scenarios, making them impractical for large-scale or dynamic applications. Third, multiple competing simulation frameworks and publications without open-source code have made it difficult to ensure consistent testing conditions across different studies. Finally, the rapid evolution of optical networking technology means benchmarks must constantly evolve to remain relevant.

The lack of reliable benchmarks and the resulting difficulty in assessing progress in the field motivate our investigations of heuristic benchmarks in Section 4 and their application to our recreation of previous work in Section 5.

## C. Recommendations for Benchmarking Best Practice

Based on our review of the field, we make the following recommendations for selecting benchmarks and evaluating solutions to DRA problems in optical networks:

• **Benchmark selection**: Assess multiple benchmarks and select the best available. Tune parameters such as the number of candidate paths and path sort criteria (see Section 4.A) to maximize performance. Prefer deterministic algorithms that can be reproduced without re-training ML components.

- **Statistical rigor**: Perform sufficient trials for statistical significance (a minimum of 100 blocking events is a rule of thumb) with multiple random seeds. Report the mean and a measure of variability of results, e.g., standard deviation.
- **Methodological transparency**: Be transparent in your choice of benchmark and its implementation details. Release the code to facilitate verification and extension of research findings. Utilize established simulation frameworks where possible to minimize implementation discrepancies across studies, with unit tests to ensure correctness.

We implement these recommendations in our analyses in Sections 4 and 5. We note that these recommendations apply to the evaluation of any solution method for DRA problems, including RL, other ML approaches, or novel heuristic algorithms.

#### D. Selection of Papers for Benchmarking

To assess progress in RL for DRA, we select five papers to re-benchmark in Section 5. We select these papers primarily because they all compare their results to "DeepRMSA" with similar traffic models and topologies, therefore presenting the most consistent application of benchmarks in the field. (We note that the training of RL solutions is highly sensitive to hyperparameters [139] and non-deterministic factors [140]; therefore, the comparisons that the selected papers make to re-trained DeepRMSA agents may not be robust.) We also select based on their impact, which we assess by qualitative and quantitative criteria. The qualitative criteria are novelty, contribution, and reputation of publication or conference. The quantitative criterion is their blocking performance relative to benchmarks. They are also among the most highly cited papers in the field, as of April 2025.

- 1. **DeepRMSA** [11] constructs a feature matrix to represent the available paths for the current requests and applies an NN with 5 × 128 hidden units to select from the K-shortest paths with first-fit spectrum allocation. It demonstrates service blocking probability (SBP) reduced by 20% versus KSP-FF on the NSFNET and COST239 topologies. DeepRMSA's impact was enhanced by its open-source codebase.
- 2. **Reward-RMSA** [28] builds on the DeepRMSA framework and changes the reward function to incorporate fragmentation-related information. They report SBP reduced by 32% versus multiple heuristics and 55% versus DeepRMSA on NSFNET and COST239.
- 3. **GCN-RMSA** [36] is notable as the first work to use advanced NN architectures to improve performance. They use a graph convolutional network (GCN) [including a recurrent neural network (RNN) as the path aggregation function] in the policy and value functions, which they claim allows improved feature extraction from the network state. Like DeepRMSA and Reward-RMSA, the policy selects from K paths with first-fit spectrum allocation. They report SBP reduced by up to 30% versus multiple

- heuristics and 18% versus DeepRMSA on NSFNET, COST239, and USNET.
- 4. **MaskRSA** [35] innovated by selecting from the entire range of available slots on the K paths and using invalid action masking [141] to increase the efficiency of training. Despite the RSA in the title, the paper does consider a distance-dependent modulation format (RMSA). MaskRSA presented improvements over KSP-FF on NSFNET and JPN48 topologies with over an order of magnitude lower SBP, or a 35%–45% increase in the supported traffic in their case studies. The authors of MaskRSA also contributed to open source by releasing their simulation framework, RSA-RL.
- 5. **PtrNet-RSA** [37], published in 2024, innovates in both the problem setting and its use of pointer-nets [142]. The pointer-net is used to select the constituent nodes of the target path, thereby removing the restriction of selecting from the pre-calculated K-shortest paths. Invalid action masking is used to allow selection from all available spectral slots. Additionally, the paper considers joint optimization of the mean path SNR and the SBP through its reward function. It demonstrates SBP reduced by over an order of magnitude versus KSP-FF and their implementation of MaskRSA on NSFNET, COST239, and USNET.

# 4. HEURISTIC ALGORITHM BENCHMARK EVALUATION

To evaluate the results of the selected papers from Section 3.D, we must determine the best (lowest blocking probability) heuristic algorithms to use as benchmarks. In this section, we present comparisons of the heuristics listed in Table 1, evaluated on different traffic loads and topologies and considering different numbers of candidate paths (K). On the basis of this analysis, we select the benchmarks to apply in Section 5. We also include a discussion of the effect of different sort criteria for candidate paths in Section 4.A, which significantly affects the blocking performance.

We select the algorithms in Table 1 because they are commonly used as benchmarks or have been reported as superior to other heuristics.

Figure 2 shows the topologies used in the selected papers. The node and link count for each topology is NSFNET (14, 22), COST239 (11, 25), USNET (24, 43), and JPN48 (48, 82). We use these topologies to analyze the performance of the heuristic algorithms and in our recreation of the papers' problems in Section 5. We make all topology data available in our open-source codebase Code 1, Ref. [6].

Table 1. RMSA Heuristics Used for Benchmarking

| Heuristic                    | Acronym | Reference     |
|------------------------------|---------|---------------|
| K-shortest paths first-fit   | KSP-FF  | [10]          |
| First-fit K-shortest paths   | FF-KSP  | [25]          |
| K-shortest paths best-fit    | KSP-BF  | [26]          |
| Best-fit K-shortest paths    | BF-KSP  | [26]          |
| K-minimum entropy first-fit  | KME-FF  | [27]          |
| K-congestion aware first-fit | KCA-FF  | CA2 from [29] |

![](_page_5_Figure_3.jpeg)

**Fig. 2.** Network topologies used in our case studies from DeepRMSA, Reward-RMSA, GCN-RMSA, MaskRSA, and PtrNet-RSA [11,28,35–37]. We note that the USNET topology differs between GCN-RMSA and PtrNet-RSA. We show the GCN-RMSA version here. PtrNet-RSA also uses a variant of the COST239 topology. (a) NSFNET. (b) COST239. (c) USNET. (d) JPN48.

#### A. Effect of Path Ordering

All the heuristics in Table 1 are selected from the available precomputed paths on the basis of the sort criteria. The primary criterion may be a measure of the path congestion (KCA-FF), spectral fragmentation (KME-FF), or length (KSP-FF). In the event of multiple paths with an equal value, a default ordering (usually ascending order of length) determines the selected path.

Conventionally, path length is considered the distance in km. However, we find that considering path length as a number of hops (with length in km as a secondary sort criterion) significantly improves the performance of the heuristics. This has been observed previously by Baroni [143], who referred to it as minimum number of hops routing (MNH). The intuitive explanation for this is that, if two paths can support the same order of modulation format, the path that comprises fewer links occupies fewer spectral resources.

We refer to these two orderings as path length in km (#km) or path length in number of hops (#hops). Our comparisons of KSP-FF for these two orderings in Section 5 (see Fig. 5) evidence the reduction in blocking probability from #hops ordering. In our comparisons of heuristics in the following section, we use #hops ordering.

## **B. Simulation Setup**

For each heuristic and topology, we carried out three simulation scenarios to investigate the effects of varying traffic loads and values of K on the relative blocking performance of the heuristics.

# Experiment 1: Increasing K

**Aim**: Investigate relative performance of heuristics with increasing K. **Method**: Record the SBP for each heuristic at values of K ranging from 2 to 26 at a fixed traffic load. We arbitrarily select the traffic load for each topology so that the heuristics give an SBP of  $\sim 1\%$ .

**Experiment 2**: Increasing K from high to low traffic

**Aim**: Investigate the effect of increasing K at different traffic loads. **Method**: Record the SBP at K ranging from 2 to 40 for a range of traffic loads. We select the traffic loads for each topology such that they result in  $10^{-5}$  to  $10^{-1}$  SBP. To simplify the analysis and plots, we only present results for KSP-FF.

**Experiment 3:** Increasing traffic load at K = 50

**Aim**: Using the findings from Experiments 1 and 2, determine the lowest-blocking heuristic with optimized K-value across traffic loads. **Method**: Record the SBP for high K (K = 50) at varying traffic loads. We select the traffic loads for each topology such that they result in a range of SBP ( $10^{-5}$  to  $10^{-1}$ ). This experiment provides evidence on which heuristic is the best overall for each topology.

For each experiment and heuristic, data were collected from 3000 independent trials with unique random seeds. The SBP was calculated after 10,000 connection requests, with the mean and standard deviation calculated across trials. Each data point in Fig. 3 therefore shows summary statistics from 30 million connection requests, which gives high confidence in our results.

We considered dynamic traffic with a fixed mean service holding time at 10 units. We considered the same traffic model and other settings as DeepRMSA: uniform traffic probability between each node pair; Poissonian arrival and departure statistics; uniform random selection of the data rate from 25 to 100 Gbps in 1 Gbps intervals; distance-dependent modulation formats from BPSK, QPSK, 8QAM, and 16QAM; and maximum transmission distances of 10,000, 2500, 1250, and 625 km, respectively. (We consider the DeepRMSA problem settings in these experiments because it is used by most of the papers presented in Section 5.) We consider topologies with dual fiber links (one for each direction of propagation), 12.5 GHz FSU width, and 100 FSU per fiber.

#### C. Results and Discussion

The results of **Experiment 1** in Fig. 3(a) show different outcomes for smaller networks (NSFNET and COST239) and larger networks (USNET and JPN48). For NSFNET and COST239, KSP-FF and KME-FF are approximately equal and give the lowest blocking. Their blocking decreases to a minimum of approximately K = 23 and above for NSFNET and continues to decrease for K > 26 for COST239.

For USNET and JPN48, FF-KSP is clearly the best heuristic, with blocking reduced by half for JPN48. Blocking from FF-KSP decreases with K until K=26 for USNET and continues dropping sharply for K>26 for JPN48. For USNET, KSP-FF and KME-FF become competitive with FF-KSP at large K. It can be argued that FF-KSP performs better in networks with higher numbers of nodes and links, where there are many viable paths between the source and destination, and dense packing of utilized wavelengths increases in relative importance to path selection.

![](_page_6_Figure_3.jpeg)

Fig. 3. Comparison of heuristic algorithms. (a) SBP at fixed traffic and varying numbers of candidate paths (K). (b) SBP for KSP-FF at varying traffic loads and K = 2 to K = 40. (c) SBP at varying traffic loads for K = 50. The mean and standard deviation (shaded area) are calculated from 3000 trials of 10,000 traffic requests per data point. KSP-FF or FF-KSP with K = 50 are found to give the lowest blocking.

The results from Experiment 1 indicate that KSP-FF and FF-KSP generally give the lowest blocking, depending on the network topology, and blocking decreases monotonically with increasing K. This experiment looked at a moderately high traffic load (∼1% SBP); therefore, Experiment 2 investigates if the effect of increasing K holds at different traffic loads.

The results of **Experiment 2** in Fig. 3(b) show that, regardless of the traffic load, increasing K decreases the SBP until it reaches a minimum, and increasing K does not decrease the SBP further. Across all topologies and traffic loads tested in our experiments, we found that the SBP does not decrease significantly for K > 50. For very high traffic (approximately equivalent to incremental loading), the value of K beyond which the SBP does not continue to decrease can be much lower.

The results of **Experiment 3** in Fig. 3(c) show the variation of the SBP with traffic load for each heuristic with K = 50. We verified that at least 50 unique paths are possible for every node pair on our investigated topologies. We select K = 50 on the basis of Experiments 1 and 2. These results confirm the initial findings from Experiment 1—that KSP-FF and KME-FF are the lowest blocking for NSFNET and COST239, while FF-KSP is better for USNET and JPN48, with an order of magnitude lower blocking probability on JPN48 compared to the next best heuristic. (Although Fig. 3(c) shows KME-FF giving slightly lower blocking than KSP-FF at lower traffic, we prefer KSP-FF for benchmarking purposes because of its widespread use and its greater simplicity.)

In summary, we highlight the generally strong performance of the KSP-FF and FF-KSP heuristics. We find that increasing the number of candidate paths decreases the blocking probability, as does the ordering of candidate paths. We find #hops ordering is superior to #km for reduced blocking probability, as evidenced in Section 5 (see Fig. 5).

We point out that the list of heuristics we evaluate is not exhaustive, and superior algorithms may exist. We therefore encourage thorough analysis to determine the strongest heuristic benchmark for a particular problem, as we have exemplified here. However, for the purposes of this study and our comparisons to previous work in Section 5, we find that KSP-FF with K = 50 and #hops ordering demonstrates lower blocking probability than previous RL approaches.

# 5. BENCHMARKING OF PREVIOUS WORK

As discussed in our literature review (Section 3), it is difficult to assess progress in the field due to several factors, particularly the diversity of problem definitions and the use of weak benchmarks. To address this, we exactly recreate the problem settings from five influential papers from the literature and apply the best-performing heuristics from Section 4 in each case.

In this section, we first provide an analysis of holding time truncation, an implementation detail present in the DeepRMSA codebase that significantly affects the blocking probability. We then present the results of our reproductions of the selected papers and compare them to the heuristics, which have significantly lower blocking probability than all of the published RL solutions.

We have corresponded with the authors of the selected papers to clarify details of their implementation and ensure that our recreations exactly match all the relevant details of their problems. The table in Appendix A provides numerical comparisons of the results of KSP-FF from the papers and our recreation of their problems, which show good agreement within one standard error. We point out that we do not reproduce the training of the published RL results. We choose not to reproduce training because of insufficient training details and the widely documented difficulties in the reproduction of RL training due to sensitivity to hyperparameters and random seeds [139,144]. Extracting RL results from published papers gives a more reliable and fair comparison.

We use our high-performance simulation framework, XLRON Code 1, Ref. [6], for all experiments. It has demonstrated 10× faster execution on a CPU and over 1000× faster when parallelized on a GPU compared to the Optical-RL-Gym [131]. This is possible due to its array-based data model and use of the JAX numerical array computing framework, which enables just-in-time compilation to accelerator hardware. This also offers a complete suite of unit tests for core functionality, making it reliable, and includes features to reproduce the problem settings of the selected papers. We use it for these reasons and for its simple command-line interface, which facilitates experiment automation and reproducibility.

# A. Holding Time Truncation

In dynamic traffic simulations, the service holding time and time until the next arrival of a service request are modeled as exponentially distributed random variables, which is consistent with the assumption of Poisson arrival processes. Random sampling from these exponential distributions is used to generate times for each service request in the simulation.

DeepRMSA, Reward-RMSA, and GCN-RMSA use the same original DeepRMSA codebase as the basis for their experiments. This codebase includes a significant detail: the service holding time is resampled if the resulting value is more than twice the mean of the distribution. We refer to this detail as holding time truncation. In order to recreate the problems from these papers, we analyze the effect of holding time truncation.

#### 1. Experimental Setup

To understand the effect of truncation on the traffic statistics, we define an exponential distribution with unit mean. We take 10<sup>6</sup> samples from the distribution, both with and without truncation, and calculate the mean of the resulting sample populations in both cases.

![](_page_7_Figure_11.jpeg)

Fig. 4. Histogram of service holding times. The truncated distribution resamples the holding time when the sampled value exceeds 2∗ mean. This reduces the mean holding time by 31% compared to the standard exponential distribution.

#### 2. Results and Discussion

Figure 4 compares histograms of service holding times with and without truncation. The y axis shows the probability density, which is normalized so that the area of each histogram gives unit probability. The truncated case shows a cutoff at twice the mean holding time. The vertical lines indicate the mean for each case.

Holding time truncation reduces the mean by approximately 31%. This results in 31% lower traffic load. Therefore, papers that use the DeepRMSA codebase (including DeepRMSA, Reward-RMSA, and GCN-RMSA) evaluate their solutions at traffic loads 31% lower than reported. This detail is not made explicit in the published papers. This finding highlights the challenges in making fair comparisons between papers and the need for transparency in the research code.

#### B. Benchmarking of Published Results

Our analysis of the best-performing heuristics, of holding time truncation, and our correspondence with the authors enables us to benchmark the published results from the five selected influential papers. The aim of this comparison is to determine if any of the published RL solutions achieve lower SBP than the heuristics.

### 1. Experimental Methodology

We recreate the problems from each selected paper in our own simulation framework [131]. We match the topologies (NSFNET, COST239, JPN48, and USNET), mean service arrival rates, mean service holding times, data-rate or bandwidth request distributions, and uniform traffic matrices. We use the same measurement methodology as described in the respective papers to reproduce results, which is a 3000-request warm-up period (to allow the network blocking probability to reach steady-state after the "initial transient" [145]), followed by 10,000 requests. The SBP is calculated at the end of the episode. We run 10 independent episodes at each traffic load per problem and calculate the mean and standard deviation across trials.

We extract published results for KSP-FF and RL solutions from the papers, using textual values where available; otherwise, reading from charts. All published results report only a single data point for each traffic value, without uncertainty estimates.

We check that our results for KSP-FF with K=5 (green line in Fig. 5) match the published results of KSP-FF (blue line in Fig. 5) within two standard deviations to ensure faithful reproduction. This comparison gives us a high degree of confidence that we have exactly recreated each problem setting.

#### 2. Results and Discussion

Figure 5 shows our reproduction of results from the selected papers, with the SBP against traffic load in Erlangs in each subplot. The plots are organized by paper (columns) and topology (rows). PtrNet-RSA has two columns reflecting its two test cases: networks with 40 FSUs per link and 1 FSU request and networks with 80 FSUs per link and 1–4 FSU requests. PtrNet-RSA only considers fixed-bandwidth requests (no distance-dependent modulation format). MaskRSA and PtrNet-RSA only consider single-fiber links (counter-propagating channels), whereas the other cases consider dual-fiber links (one fiber for each direction of propagation), which increases their capacity.

Each plot contains five datasets:

**RL**: published results for the RL approach.

**5-SP-FF**<sub>km</sub> : published results for KSP-FF (K = 5) with paths ordered by #km.

**5-SP-FF**<sub>km</sub>: our results for KSP-FF (K = 5) with paths ordered by #km.

**5-SP-FF**<sub>hops</sub>: our results for KSP-FF (K = 5) with paths ordered by #hops.

**50-SP-FF**<sub>hops</sub>: our results for KSP-FF (K = 50) with paths ordered by #hops.

Points show mean values, shaded areas indicate standard deviation, and lines interpolate between points. The DeepRMSA paper provides data for only one traffic load per topology. The excellent agreement between 5-SP-FF $_{\rm km}^{\rm published}$  and 5-SP-FF $_{\rm km}$  in all cases confirms that our framework accurately reproduces the published scenarios.

From Fig. 5, we highlight the comparisons of "RL" (red) with 5-SP-FF<sub>hops</sub> (orange) and 50-SP-FF<sub>hops</sub> (purple). 5-SP-FF<sub>hops</sub> reduces the blocking probability by up to an order of magnitude compared to RL in all cases for NSFNET, 4/5 cases for COST239, and 1/3 cases for USNET. This shows that ordering paths by #hops is sufficient to beat the RL results in these cases.

For larger topologies, considering more candidate paths (K>5) improves the heuristic performance significantly, often by over an order of magnitude. As shown in Fig. 5, 50-SP-FF<sub>hops</sub> gives the lowest SBP of all approaches in all cases, except PtrNet-RSA-80 USNET (bottom right).

For PtrNet-RSA-80 USNET, we consider it plausible that the pointer-net architecture is a contributing factor to the strong performance, as it is not limited to selecting from a pre-defined set of paths. However, as the published results in this case fall within one standard deviation of the mean for

![](_page_8_Figure_17.jpeg)

**Fig. 5.** Mean SBP against traffic load. Each column is a publication, and each subplot is for a topology. Error bars and shaded areas show standard deviations. 50-SP-FF<sub>hops</sub> exceeds or matches the RL performance for each case.

50-SP-FF<sub>hops</sub>, the result could be spurious. This highlights the need for summary statistics and confidence intervals from multiple trials to be included with published results.

In summary, the results show that making minor changes (ordering paths by #hops and considering more paths) to simple heuristic algorithms is sufficient to achieve lower blocking probability than the sophisticated RL solutions that have been published.

We highlight that this analysis, and the selected papers, focus on the SBP as the optimization objective. In realistic scenarios, network blocking or throughput must be balanced with other metrics such as latency and total cost of operation from transceiver launch power, amplifiers, and other network elements. Future research should therefore focus on problems that take a holistic approach to network operations optimization with multiple objectives [58], and incorporate sophisticated models of all physical layer effects for improved accuracy [146,147].

All data shown in Fig. 5 are provided in tabular form in Appendix A.

#### 6. NETWORK BLOCKING BOUNDS

We have demonstrated in Section 5 that many influential works on RL for DRA problems in optical networks have failed to improve on a simple heuristic algorithm. The extent to which it is possible to reduce the blocking probability and increase supported traffic is an important motivating factor in any future research into this topic.

To understand the limits of blocking probability, we derive empirical lower bounds. By comparing these lower bounds to the performance of our best solution for a target SBP, we can estimate the additional traffic load that can be supported and, therefore, the maximum benefit from applying an intelligent resource allocation method such as RL. As discussed in Section 2, DRA problems in optical networks that require RSA are subject to three constraints: spectrum continuity, spectrum contiguity, and no reconfiguration. By relaxing any of these constraints, the optimal or near-optimal solution of the relaxed problem is a bound on the solution of the full problem. The cut-sets bound method of Cruzado et al. [148,149] relaxes the spectrum continuity constraint and uses insights from the min-cut max-flow theorem to estimate a lower bound SBP. We instead relax the constraint on reconfiguring already-established connections, a process known as defragmentation.

We couple this defragmentation with resource prioritization: sorting the active connection requests by their required resources and allocating them sequentially. The sorting of active requests in descending order of required resources was found to improve the achievable capacity to optimal or near-optimal by Baroni [143] in static RWA and later by Beghelli [150] for dynamic RWA, a method they refer to as "reconfigurable routing." Since our problem settings are elastic optical networks, we prefer the term defragmentation. The intuition behind this approach is to allocate requests with longer paths and higher spectral requirements first so that requests with lower resource requirements may be squeezed into the remaining spectral gaps later.

# Algorithm 1. Resource-Prioritized Defragmentation Blocking Bound Estimation

```
Require: network topology G, set of requests \mathcal{R}, frequency slots per
      link F
Ensure: blocking probability P_b
                                                      ⊳ Initialize network state
 1: N \leftarrow \text{InitializeNetwork}(G, F)
    with empty spectrum slots
 2: blocked \leftarrow \texttt{false}
 3: blocked\_requests \leftarrow 0
 4: for t \leftarrow 1 to |\mathcal{R}| do
       N \leftarrow \text{RemoveExpiredRequests}(N, t)
       r_t \leftarrow current request from \mathcal{R}
 7:
        N, blocked \leftarrow AllocateRequest (N, r_t)
 8.
       if blocked then
 9:
            active\_requests \leftarrow GetactiveRequests(\mathcal{R}, t)
 10:
            sorted_requests ← SortbyResource (active_requests)
             N_{temb} \leftarrow \text{InitializeNetwork}(G, F)
 12:
            blocked \leftarrow false
            for r \in sorted\_requests do
 13:
                N, blocked \leftarrow AllocateRequest (N_{temp}, r)
 14:
 15:
                if blocked then
 16:
            if not blocked then
 17:
 18:
                N \leftarrow N_{temp}
 19:
 20:
                blocked\_requests \leftarrow blocked\_requests + 1
```

#### Resource-Prioritized Defragmentation

21: **return**  $\frac{blocked\_requests}{|\mathcal{R}|}$ 

The resource-prioritized defragmentation algorithm is outlined in Algorithm 1. It utilizes four key subroutines:

- RemoveExpiredRequests(N, t) maintains the network state by removing connections that have expired. For the current time t and a request with the arrival time t<sub>arrival</sub> and the holding time t<sub>holding</sub>, the expiry condition is defined as t<sub>arrival</sub> + t<sub>holding</sub> < t.
- ALLOCATEREQUEST(N, request) establishes a new connection subject to continuity and contiguity constraints, and returns the updated network state and a boolean to indicate if the connection was blocked. We use the KSP-FF or FF-KSP algorithm with K=50. We select the algorithm that produces the lowest SBP for the problem instance.
- GETACTIVEREQUESTS( $\mathcal{R}$ , t) identifies requests where  $t_{\text{arrival}} \leq t < t_{\text{arrival}} + t_{\text{holding}}$ , determining which connections require reallocation during defragmentation.
- SORTBYRESOURCE (requests) orders active requests by required resources (product of required spectral slots and hops of shortest path), prioritizing larger requests during reallocation to maximize the probability of finding viable configurations.

A shortcoming of our method of blocking bound estimation is its reliance on the internal AllocateRequest heuristic. To have confidence that the solution presents a true bound, the allocation method must be as close to optimal as possible. We therefore evaluate multiple heuristics for each case, as shown in Section 4, and select the one with the lowest SBP. We find the best-performing heuristic is KSP-FF $_{hops}$  with K=50 for most cases, except MaskRSA JPN48, which is FF-KSP.

An advantage of our method compared to cut-sets analysis is that it computes an allocation that is guaranteed to be

![](_page_10_Figure_3.jpeg)

Fig. 6. Mean SBP against traffic load for the lowest-blocking heuristic in each case (KSP-FF or FF-KSP with K = 50) and the estimated bound from Algorithm 1. Each column is a publication, and each subplot is for a topology. Shaded areas show standard deviations. Red lines and text indicate a relative increase in supported traffic at 0.1% SBP from heuristic to bound.

physically possible, as it relaxes the "No Reconfiguration" constraint instead of the physical spectrum continuity constraint. Relaxing the "No Reconfiguration" constraint makes Algorithm 1 omniscient (it has complete knowledge of requests to be allocated) rather than a strictly online algorithm, according to definitions from Awerbuch *et al.* [151]. This gives Algorithm 1 a fundamental competitive advantage over online algorithms such as KSP-FF/FF-KSP; therefore, it can be considered a lower-bound estimator of blocking probability.

We note that our algorithm is general and can be applied to any DRA problem in optical networks by using a strong heuristic for AllocateRequest and defining the resource-based sort criteria appropriately.

## A. Experimental Setup

For each problem from the five selected papers, we run the best-performing heuristic for a range of traffic loads that result in an SBP from 0.01% to 1%. For the lowest-blocking heuristic and for Algorithm 1, we run 10 episodes of 10,000 requests with unique random seeds and calculate the mean and standard deviation of SBP across episodes. We calculate the mean and standard deviation of SBP across episodes in each case.

We compare the resulting SBP from the best heuristic and Algorithm 1. We seek to estimate the additional network capacity that can be achieved at 0.1% SBP for each case study from the five selected papers. We select 0.1% SBP to align with previous studies of network throughput estimation by Cruzado *et al.* [148,149].

# B. Results and Discussion

Similar to Fig. 5, each subplot in Fig. 6 represents a different problem instance. DeepRMSA, Reward-RMSA, and GCN-RMSA are combined into a single set of plots since they use identical topologies and traffic models. The purple lines show the best-performing heuristic in each case (KSP-FF with K = 50 or FF-KSP for JPN48), with paths sorted in ascending order of number of hops. The gray lines show the resource-prioritized defragmentation bounds. At 0.1% SBP, we compare the network traffic loads that can be supported in each case, with the difference highlighted by a red horizontal line. The relative increase in network capacity is calculated as the difference between the upper bound traffic load and the heuristic traffic load, as a percentage of the heuristic load.

PtrNet-RSA-40 shows differences of 5%, 1%, and 8% across its three test cases. These relatively low values are due to the fixed-width request size of 1 FSU used in this case, which makes it equivalent to RWA and reduces the impact of fragmentation compared to RSA/RMSA.

For the Deep/Reward/GCN-RMSA, MaskRSA, and PtrNet-RSA-80 cases, the difference between the supported traffic in the heuristic case and the upper bound ranges from 19% (MaskRSA JPN48) to 36% (Deep/Reward/GCN-RMSA NSFNET). These results show larger but comparable optimality gaps to those from the cut-sets method of Cruzado *et al.* [149], who found gaps of 5% to 16% in their cases of study. This shows that defragmentation can unlock significant network capacity, but it is unknown theoretically how close an intelligent online allocation method, such as RL, can come to this bound. This will be the subject of future research.

# 7. CONCLUSION

Our review of the field of RL applied to DRA problems in optical networks shows that it has been the subject of significant research interest, with almost 100 peer-reviewed papers published so far. Technical innovations from ML research, such as invalid action masking [35,37,56] and GNNs [36,96,152], have been applied to the problem area and have demonstrated incremental improvements in network blocking.

However, the field has suffered from a lack of standardization in problems, selective application of benchmark algorithms, and poor practices for reproducibility. We have addressed these problems by assessing a range of heuristic algorithms, optimizing their path ordering and number of candidate paths, and applying them to the problem settings from five influential papers on RL for DRA. We use our simulation framework for this work, which enables the recreation of diverse problem settings and fast computation.

From our assessment and optimization of heuristic algorithms, we determine that KSP-FF or FF-KSP with K = 50 are the best of those we evaluated. We highlight the result that ordering the candidate paths by number of hops gives significantly lower blocking probability than ordering by distance. These recommended benchmarks can be applied to future studies of RL or other solution methods.

Our most significant findings are in the benchmarking of previous RL results. By extracting the published results of RL from the selected papers and comparing them to the best heuristic benchmarks on recreated problem settings, we show that simple heuristics exceed or match the RL results in all cases, often with over an order of magnitude lower SBP. This shows that the relative performance of previous RL solutions on these problems has been overestimated due to weak benchmarks and highlights the need for more rigorous standards of evaluation on these problems to avoid trivial results. These standards also apply to other non-RL resource allocation algorithms.

Finally, to ascertain the practical value of pursuing further research into optimized DRA, we provide the resourceprioritized defragmentation method of estimating the lower bound network blocking probability. Compared to the best heuristics available for each case, this method estimates the upper bound additional dynamic traffic load that can be supported on flex-grid networks is approximately 19% to 36%. These results suggest there is room for improvement over the best benchmarks, which may motivate further research into DRA with RL or other methods. Alternatively, research into network optimization with RL could focus on other objectives for which there are not yet good heuristic solutions.

# APPENDIX A: DATA FROM PREVIOUS WORKS AND OUR BENCHMARKS

Comparison of service blocking probabilities for KSP-FF and RL solutions across various topologies and traffic loads.

|             |          | Nslots | Load (Erlang) | Service Blocking Probability (%) |         |                |                |                |                  |
|-------------|----------|--------|---------------|----------------------------------|---------|----------------|----------------|----------------|------------------|
| Publication |          |        |               | Published                        |         | Ours           |                |                | Mean Improvement |
|             | Topology |        |               | RL                               | 5-SP-FF | 5-SP-FF        | 5-SP-FFhops    | 50-SP-FFhops   | over RL (%)      |
| DeepRMSA    | NSFNET   | 100    | 250           | 4.00                             | 5.10    | 5.00 ±<br>0.29 | 2.93 ±<br>0.22 | 2.33 ±<br>0.25 | 42               |
| DeepRMSA    | COST239  | 100    | 600           | 5.75                             | 6.75    | 6.69 ±<br>0.35 | 3.80 ±<br>0.39 | 2.61 ±<br>0.36 | 55               |
| Reward-RMSA | NSFNET   | 100    | 168           | 0.35                             | 1.00    | 1.06 ±<br>0.11 | 0.10 ±<br>0.02 | 0.02 ±<br>0.01 | 94               |
| Reward-RMSA | NSFNET   | 100    | 182           | 0.70                             | 1.40    | 1.53 ±<br>0.15 | 0.25 ±<br>0.03 | 0.08 ±<br>0.03 | 89               |
| Reward-RMSA | NSFNET   | 100    | 196           | 1.20                             | 2.10    | 2.06 ±<br>0.12 | 0.48 ±<br>0.07 | 0.21 ±<br>0.04 | 83               |
| Reward-RMSA | NSFNET   | 100    | 210           | 1.80                             | 2.70    | 2.68 ±<br>0.20 | 0.95 ±<br>0.11 | 0.47 ±<br>0.05 | 74               |
| GCN-RMSA    | NSFNET   | 100    | 154           | 0.51                             | 0.67    | 0.69 ±<br>0.08 | 0.03 ±<br>0.02 | 0.01 ±<br>0.00 | 98               |
| GCN-RMSA    | NSFNET   | 100    | 168           | 0.66                             | 1.00    | 1.06 ±<br>0.11 | 0.10 ±<br>0.02 | 0.02 ±<br>0.01 | 97               |
| GCN-RMSA    | NSFNET   | 100    | 182           | 0.98                             | 1.42    | 1.53 ±<br>0.15 | 0.25 ±<br>0.03 | 0.08 ±<br>0.03 | 92               |
| GCN-RMSA    | NSFNET   | 100    | 196           | 1.50                             | 2.10    | 2.06 ±<br>0.12 | 0.48 ±<br>0.07 | 0.21 ±<br>0.04 | 86               |
| GCN-RMSA    | NSFNET   | 100    | 210           | 2.10                             | 2.76    | 2.68 ±<br>0.20 | 0.95 ±<br>0.11 | 0.47 ±<br>0.05 | 78               |
| GCN-RMSA    | COST239  | 100    | 368           | 0.71                             | 0.78    | 0.80 ±<br>0.08 | 0.07 ±<br>0.03 | 0.00 ±<br>0.00 | 100              |
| GCN-RMSA    | COST239  | 100    | 391           | 0.85                             | 1.30    | 1.13 ±<br>0.12 | 0.17 ±<br>0.07 | 0.00 ±<br>0.00 | 100              |
| GCN-RMSA    | COST239  | 100    | 414           | 1.25                             | 1.70    | 1.57 ±<br>0.13 | 0.28 ±<br>0.09 | 0.01 ±<br>0.01 | 100              |
| GCN-RMSA    | COST239  | 100    | 437           | 1.75                             | 2.30    | 2.02 ±<br>0.13 | 0.46 ±<br>0.11 | 0.02 ±<br>0.02 | 99               |
| GCN-RMSA    | COST239  | 100    | 460           | 2.10                             | 2.70    | 2.53 ±<br>0.21 | 0.73 ±<br>0.20 | 0.07 ±<br>0.03 | 97               |
| GCN-RMSA    | USNET    | 100    | 320           | 0.65                             | 0.75    | 0.98 ±<br>0.10 | 0.25 ±<br>0.07 | 0.00 ±<br>0.01 | 100              |
| GCN-RMSA    | USNET    | 100    | 340           | 0.83                             | 1.20    | 1.31 ±<br>0.16 | 0.42 ±<br>0.07 | 0.01 ±<br>0.02 | 99               |
| GCN-RMSA    | USNET    | 100    | 360           | 1.05                             | 1.50    | 1.69 ±<br>0.12 | 0.73 ±<br>0.16 | 0.04 ±<br>0.04 | 96               |
| GCN-RMSA    | USNET    | 100    | 380           | 1.60                             | 2.15    | 2.18 ±<br>0.19 | 1.05 ±<br>0.19 | 0.09 ±<br>0.09 | 94               |
| GCN-RMSA    | USNET    | 100    | 400           | 2.20                             | 2.70    | 2.79 ±<br>0.24 | 1.53 ±<br>0.18 | 0.23 ±<br>0.09 | 90               |
| MaskRSA     | NSFNET   | 80     | 80            | 0.01                             | 0.26    | 0.33 ±<br>0.06 | 0.00 ±<br>0.00 | 0.00 ±<br>0.00 | 100              |
| MaskRSA     | NSFNET   | 80     | 90            | 0.05                             | 0.60    | 0.64 ±<br>0.07 | 0.01 ±<br>0.01 | 0.00 ±<br>0.00 | 100              |
| MaskRSA     | NSFNET   | 80     | 100           | 0.20                             | 0.90    | 1.08 ±<br>0.10 | 0.08 ±<br>0.05 | 0.04 ±<br>0.02 | 80               |

*(Table continued)*

|             |          |        |               | Service Blocking Probability (%) |         |                |                |                |                  |
|-------------|----------|--------|---------------|----------------------------------|---------|----------------|----------------|----------------|------------------|
|             |          |        |               | Published                        |         | Ours           |                |                | Mean Improvement |
| Publication | Topology | Nslots | Load (Erlang) | RL                               | 5-SP-FF | 5-SP-FF        | 5-SP-FFhops    | 50-SP-FFhops   | over RL (%)      |
| MaskRSA     | NSFNET   | 80     | 110           | 0.50                             | 1.80    | 1.68 ±<br>0.11 | 0.25 ±<br>0.09 | 0.13 ±<br>0.03 | 74               |
| MaskRSA     | NSFNET   | 80     | 120           | 0.79                             | 2.47    | 2.39 ±<br>0.14 | 0.60 ±<br>0.14 | 0.33 ±<br>0.12 | 58               |
| MaskRSA     | NSFNET   | 80     | 130           | 1.80                             | 3.00    | 3.14 ±<br>0.22 | 1.35 ±<br>0.12 | 0.86 ±<br>0.14 | 52               |
| MaskRSA     | NSFNET   | 80     | 140           | 3.00                             | 4.00    | 4.05 ±<br>0.21 | 2.26 ±<br>0.23 | 1.71 ±<br>0.27 | 43               |
| MaskRSA     | NSFNET   | 80     | 150           | 4.30                             | 5.00    | 5.19 ±<br>0.28 | 3.43 ±<br>0.21 | 2.84 ±<br>0.26 | 34               |
| MaskRSA     | NSFNET   | 80     | 160           | 5.30                             | 6.00    | 6.37 ±<br>0.26 | 4.65 ±<br>0.35 | 4.15 ±<br>0.27 | 22               |
| MaskRSA     | JPN48    | 80     | 120           | 0.05                             | 1.60    | 1.92 ±<br>0.27 | 0.32 ±<br>0.08 | 0.00 ±<br>0.00 | 100              |
| MaskRSA     | JPN48    | 80     | 130           | 0.20                             | 2.50    | 2.75 ±<br>0.31 | 0.64 ±<br>0.10 | 0.02 ±<br>0.01 | 90               |
| MaskRSA     | JPN48    | 80     | 140           | 0.55                             | 3.50    | 3.69 ±<br>0.30 | 0.97 ±<br>0.14 | 0.04 ±<br>0.03 | 93               |
| MaskRSA     | JPN48    | 80     | 150           | 0.90                             | 4.50    | 4.55 ±<br>0.32 | 1.41 ±<br>0.15 | 0.09 ±<br>0.04 | 90               |
| MaskRSA     | JPN48    | 80     | 160           | 1.60                             | 5.00    | 5.40 ±<br>0.36 | 2.00 ±<br>0.21 | 0.18 ±<br>0.04 | 89               |
| PtrNet-RSA  | NSFNET   | 40     | 180           | 0.01                             | 0.80    | 0.93 ±<br>0.11 | 0.00 ±<br>0.00 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | NSFNET   | 40     | 190           | 0.03                             | 1.25    | 1.27 ±<br>0.10 | 0.01 ±<br>0.01 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | NSFNET   | 40     | 200           | 0.08                             | 1.50    | 1.68 ±<br>0.10 | 0.02 ±<br>0.01 | 0.00 ±<br>0.01 | 100              |
| PtrNet-RSA  | NSFNET   | 40     | 210           | 0.19                             | 1.90    | 2.06 ±<br>0.11 | 0.09 ±<br>0.04 | 0.03 ±<br>0.02 | 84               |
| PtrNet-RSA  | NSFNET   | 40     | 220           | 0.23                             | 2.50    | 2.58 ±<br>0.11 | 0.22 ±<br>0.09 | 0.09 ±<br>0.05 | 61               |
| PtrNet-RSA  | NSFNET   | 40     | 230           | 0.75                             | 2.90    | 3.14 ±<br>0.14 | 0.48 ±<br>0.12 | 0.26 ±<br>0.10 | 65               |
| PtrNet-RSA  | NSFNET   | 40     | 240           | 1.30                             | 3.50    | 4.01 ±<br>0.22 | 0.90 ±<br>0.18 | 0.54 ±<br>0.15 | 58               |
| PtrNet-RSA  | COST239  | 40     | 340           | 0.01                             | 2.50    | 3.36 ±<br>0.16 | 0.02 ±<br>0.02 | 0.00 ±<br>0.00 | 100              |
|             |          |        |               |                                  |         | 4.02 ±         | 0.04 ±         | 0.00 ±         |                  |
| PtrNet-RSA  | COST239  | 40     | 360           | 0.04                             | 3.25    | 0.20<br>4.72 ± | 0.02<br>0.10 ± | 0.00<br>0.00 ± | 100              |
| PtrNet-RSA  | COST239  | 40     | 380           | 0.12                             | 3.80    | 0.29<br>5.43 ± | 0.03<br>0.25 ± | 0.00<br>0.00 ± | 100              |
| PtrNet-RSA  | COST239  | 40     | 400           | 0.24                             | 4.60    | 0.36           | 0.09           | 0.00           | 100              |
| PtrNet-RSA  | COST239  | 40     | 420           | 0.39                             | 5.50    | 6.24 ±<br>0.25 | 0.46 ±<br>0.12 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | USNET    | 40     | 210           | 0.01                             | 0.85    | 1.02 ±<br>0.20 | 0.14 ±<br>0.05 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | USNET    | 40     | 220           | 0.08                             | 1.40    | 1.46 ±<br>0.25 | 0.29 ±<br>0.08 | 0.00 ±<br>0.01 | 100              |
| PtrNet-RSA  | USNET    | 40     | 230           | 0.22                             | 1.85    | 1.99 ±<br>0.31 | 0.46 ±<br>0.10 | 0.02 ±<br>0.01 | 91               |
| PtrNet-RSA  | USNET    | 40     | 240           | 0.38                             | 2.20    | 2.59 ±<br>0.38 | 0.77 ±<br>0.18 | 0.08 ±<br>0.06 | 79               |
| PtrNet-RSA  | USNET    | 40     | 250           | 0.68                             | 3.10    | 3.25 ±<br>0.32 | 1.19 ±<br>0.28 | 0.19 ±<br>0.09 | 72               |
| PtrNet-RSA  | USNET    | 40     | 260           | 1.10                             | 3.60    | 3.87 ±<br>0.49 | 1.81 ±<br>0.35 | 0.42 ±<br>0.15 | 62               |
| PtrNet-RSA  | USNET    | 40     | 270           | 1.80                             | 4.40    | 4.67 ±<br>0.50 | 2.39 ±<br>0.41 | 0.72 ±<br>0.27 | 60               |
| PtrNet-RSA  | USNET    | 40     | 280           | 2.20                             | 4.90    | 5.40 ±<br>0.46 | 3.16 ±<br>0.48 | 1.25 ±<br>0.34 | 43               |
| PtrNet-RSA  | NSFNET   | 80     | 200           | 0.01                             | 0.60    | 0.61 ±<br>0.09 | 0.00 ±<br>0.00 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | NSFNET   | 80     | 210           | 0.03                             | 0.80    | 0.83 ±<br>0.10 | 0.00 ±<br>0.00 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | NSFNET   | 80     | 220           | 0.11                             | 1.20    | 1.07 ±<br>0.09 | 0.02 ±<br>0.02 | 0.01 ±<br>0.02 | 91               |
| PtrNet-RSA  | NSFNET   | 80     | 230           | 0.16                             | 1.40    | 1.32 ±<br>0.13 | 0.05 ±<br>0.03 | 0.02 ±<br>0.02 | 88               |
| PtrNet-RSA  | NSFNET   | 80     | 240           | 0.50                             | 1.90    | 1.63 ±<br>0.15 | 0.11 ±<br>0.06 | 0.05 ±<br>0.04 | 90               |
| PtrNet-RSA  | COST239  | 80     | 420           | 0.01                             | 2.50    | 2.66 ±<br>0.11 | 0.08 ±<br>0.03 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | COST239  | 80     | 440           | 0.16                             | 3.00    | 3.05 ±<br>0.16 | 0.13 ±<br>0.06 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | COST239  | 80     | 460           | 0.65                             | 3.50    | 3.52 ±<br>0.19 | 0.25 ±<br>0.07 | 0.01 ±<br>0.01 | 98               |
| PtrNet-RSA  | USNET    | 80     | 260           | 0.03                             | 1.00    | 1.21 ±<br>0.18 | 0.46 ±<br>0.13 | 0.00 ±<br>0.00 | 100              |
| PtrNet-RSA  | USNET    | 80     | 270           | 0.09                             | 1.20    | 1.48 ±<br>0.24 | 0.64 ±<br>0.18 | 0.16 ±<br>0.09 | −78              |
| PtrNet-RSA  | USNET    | 80     | 280           | 0.15                             | 1.40    | 1.78 ±<br>0.20 | 0.87 ±<br>0.21 | 0.38 ±<br>0.13 | −153             |
| PtrNet-RSA  | USNET    | 80     | 290           | 0.29                             | 1.70    | 2.13 ±<br>0.24 | 1.12 ±<br>0.24 | 0.54 ±<br>0.15 | −86              |
| PtrNet-RSA  | USNET    | 80     | 300           | 0.52                             | 2.20    | 2.46 ±<br>0.23 | 1.42 ±<br>0.29 | 0.61 ±<br>0.20 | −33              |
| PtrNet-RSA  | USNET    | 80     | 310           | 0.66                             | 2.40    | 2.79 ±<br>0.26 | 1.75 ±<br>0.32 | 0.88 ±<br>0.23 | −33              |
| PtrNet-RSA  | USNET    | 80     | 320           | 1.00                             | 2.80    | 3.18 ±<br>0.31 | 2.08 ±<br>0.35 | 1.15 ±<br>0.26 | −15              |
| PtrNet-RSA  | USNET    | 80     | 330           | 1.50                             | 3.10    | 3.50 ±<br>0.28 | 2.42 ±<br>0.31 | 1.46 ±<br>0.30 | 3                |

Funding. Engineering and Physical Sciences Research Council (EP/S022139/1, EP/R035342/1); Royal Society.

Acknowledgment. This work was supported by the Engineering and Physical Sciences Research Council (EPSRC) grant EP/S022139/1 the Centre for Doctoral Training in Connected Electronic and Photonic Systems—and EPSRC Programme Grant TRANSNET EP/R035342/1. In addition, Polina Bayvel is supported through a Royal Society Research Professorship. For the purpose of open access, the author has applied a Creative Commons Attribution (CC BY) licence to any Author Accepted Manuscript version arising.

# REFERENCES

- 1. A. Lord, C. White, and A. Iqbal, "Future optical networks in a 10 year time frame," in Optical Fiber Communication Conference (OFC) (2021), paper M2A.3.
- 2. M. Shtaif, C. Antonelli, A. Mecozzi, et al., "The information capacity of the fiber-optic channel: bounds and prospects," in Optical Fiber Communication Conference (OFC) (2024), paper M4K.3.
- 3. P. J. Winzer, "The future of communications is massively parallel," J. Opt. Commun. Netw. 15, 783–787 (2023).

- 4. N. Di Cicco, E. F. Mercan, O. Karandin, et al., "On deep reinforcement learning for static routing and wavelength assignment," IEEE J. Sel. Top. Quantum Electron. 28, 3600112 (2022).
- 5. F. N. Khan, "Non-technological barriers: the last frontier towards AI-powered intelligent optical networks," Nat. Commun. 15, 5995 (2024).
- 6. M. Doherty, "micdoh/XLRON: reinforcement learning for dynamic resource allocation in optical networks: hype or hope?" Zenodo (2024), https://doi.org/10.5281/zenodo.12594495.
- 7. J.-L. Augé, "Can we use flexible transponders to reduce margins?" in Optical Fiber Communication Conference/National Fiber Optic Engineers Conference (OFC/NFOEC) (2013), paper OTu2A.1.
- 8. Y. Pointurier, "Design of low-margin optical networks," J. Opt. Commun. Netw. 9, A9–A17 (2017).
- 9. D. Hassabis, "Nobel Prize Lecture" (2024) [accessed 25 December 2024], https://www.nobelprize.org/prizes/chemistry/2024/hassabis/ lecture/.
- 10. H. Zang, J. P. Jue, and B. Mukherjee, "A review of routing and wavelength assignment approaches for wavelength-routed optical WDM networks," Opt. Netw. Mag. 1, 47–60 (2000).
- 11. X. Chen, B. Li, R. Proietti, et al., "DeepRMSA: a deep reinforcement learning framework for routing, modulation and spectrum assignment in elastic optical networks," J. Lightwave Technol. 37, 4155–4163 (2019).
- 12. A. Lord, S. J. Savory, M. Tornatore, et al., "Flexible technologies to increase optical network capacity," Proc. IEEE 110, 1714–1724 (2022).
- 13. B. Mukherjee, I. Tomkos, M. Tornatore, et al., eds., Springer Handbook of Optical Networks (Springer, 2020).
- 14. D. J. Ives, P. Bayvel, and S. J. Savory, "Routing, modulation, spectrum and launch power assignment to maximize the traffic throughput of a nonlinear optical mesh network," Photonics Netw. Commun. 29, 244–256 (2015).
- 15. F. Arpanaei, M. R. Zefreh, J. A. Hernández, et al., "Launch power optimization for dynamic elastic optical networks over C + L bands," arXiv (2023).
- 16. L. Gong and Z. Zhu, "Virtual optical network embedding (VONE) over elastic optical networks," J. Lightwave Technol. 32, 450–460 (2014).
- 17. M. Doherty and A. Beghelli, "Deep reinforcement learning for infrastructure as a service over flexible optical networks," in 49th European Conference on Optical Communications (ECOC) (IEEE, 2023).
- 18. C. Zhou, B. Zhao, J. Tao, et al., "Applications of reinforcement learning in virtual network function placement: a survey," in 18th International Conference on Mobility, Sensing and Networking (MSN) (IEEE, 2022), pp. 871–876.
- 19. O. Gerstel, M. Jinno, A. Lord, et al., "Elastic optical networking: a new dawn for the optical layer?" IEEE Commun. Mag. 50(2), s12– s20 (2012).
- 20. S. Balasubramanian, V. Dangui, J. P. Eason, et al., "Targeted defragmentation of a production optical network," in Optical Network Design and Modeling (ONDM) (IEEE, 2023).
- 21. I. Chlamtac, A. Ganz, and G. Karmi, "Lightpath communications: an approach to high bandwidth optical WAN's," IEEE Trans. Commun. 40, 1171–1182 (1992).
- 22. K. Walkowiak, P. Lechowicz, M. Klinkowski, et al., "ILP modeling of flexgrid SDM optical networks," in 17th International Telecommunications Network Strategy and Planning Symposium (Networks) (2016), pp. 121–126.
- 23. B. Jaumard, A. Mohammed, and Q. A. Nguyen, "Decomposition models for the routing and slot provisioning problem," in International Conference on Computing, Networking and Communications (ICNC) (2023), pp. 659–665.
- 24. Y. Goto, S. Shinada, Y. Hirota, et al., "LCOS-based flexible optical switch for heterogeneous SDM fiber networks," in 24th International Conference on Transparent Optical Networks (ICTON) (2024).
- 25. R. J. Vincent, D. J. Ives, and S. J. Savory, "Scalable capacity estimation for nonlinear elastic all-optical core networks," J. Lightwave Technol. 37, 5380–5391 (2019).

- 26. F. S. Abkenar, A. Ghaffarpour Rahbar, and A. Ebrahimzadeh, "Best fit (BF): a new spectrum allocation mechanism in elastic optical networks (EONs)," in 8th International Symposium on Telecommunications (IST) (2016), pp. 24–29.
- 27. P. Wright, M. C. Parker, and A. Lord, "Minimum- and maximumentropy routing and spectrum assignment for flexgrid elastic optical networking [Invited]," J. Opt. Commun. Netw. 7, A66–A72 (2015).
- 28. B. Tang, Y.-C. Huang, Y. Xue, et al., "Heuristic reward design for deep reinforcement learning-based routing, modulation and spectrum assignment of elastic optical networks," IEEE Commun. Lett. 26, 2675–2679 (2022).
- 29. S. J. Savory, "Congestion aware routing in nonlinear elastic optical networks," IEEE Photonics Technol. Lett. 26, 1057–1060 (2014).
- 30. A. Hassan and C. Phillips, "Chaotic particle swarm optimization for dynamic routing and wavelength assignment in all-optical WDM networks," in 3rd International Conference on Signal Processing and Communication Systems (2009).
- 31. R. S. Barpanda, A. K. Turuk, B. Sahoo, et al., "Genetic algorithm techniques to solve routing and wavelength assignment problem in wavelength division multiplexing all-optical networks," in Third International Conference on Communication Systems and Networks (COMSNETS 2011) (IEEE, 2011).
- 32. R. Bellman, "The theory of dynamic programming," Bull. Am. Math. Soc. 60, 503–515 (1954).
- 33. R. Bellman, "A Markovian decision process," J. Math. Mech. 6, 679–684 (1957).
- 34. A. B. Terki, J. Pedro, A. Eira, et al., "Routing and spectrum assignment based on reinforcement learning in multi-band optical networks," in International Conference on Photonics in Switching and Computing (PSC) (IEEE, 2023).
- 35. M. Shimoda and T. Tanaka, "Mask RSA: end-to-end reinforcement learning-based routing and spectrum assignment in elastic optical networks," in European Conference on Optical Communication (ECOC) (IEEE, 2021).
- 36. L. Xu, Y.-C. Huang, Y. Xue, et al., "Deep reinforcement learningbased routing and spectrum assignment of EONs by exploiting GCN and RNN for feature extraction," J. Lightwave Technol. 40, 4945–4955 (2022).
- 37. Y. Cheng, S. Ding, Y. Shao, et al., "PtrNet-RSA: a pointer networkbased QoT-aware routing and spectrum assignment scheme in elastic optical networks," J. Lightwave Technol. 42, 5808–5819 (2024).
- 38. R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction, 2nd ed., Adaptive Computation and Machine Learning (MIT Press, 2018).
- 39. C. Watkins, "Learning from delayed reward," Ph.D. thesis (Cambridge University, 1989).
- 40. R. S. Sutton, "Learning to predict by the methods of temporal differences," Mach. Learn. 3, 9–44 (1988).
- 41. N. B. Bryant, K. K. Chung, J. Feng, et al., "Q-learning based routing in optical networks," in IEEE Canadian Conference on Electrical and Computer Engineering (CCECE) (IEEE, 2022), pp. 419–422.
- 42. V. Mnih, A. P. Badia, M. Mirza, et al., "Asynchronous methods for deep reinforcement learning," arXiv (2016).
- 43. J. Schulman, F. Wolski, P. Dhariwal, et al., "Proximal policy optimization algorithms," arXiv (2017).
- 44. "Spectral grids for WDM applications: CWDM wavelength grid," ITU-T Recommendation G.694.2 (2002).
- 45. "Transmission characteristics of optical components and subsystems," ITU-T Recommendation G.671 (2012).
- 46. P. Garcia, A. Zsigri, and A. Guitton, "A multicast reinforcement learning algorithm for WDM optical networks," in Proceedings of the 7th International Conference on Telecommunications (ConTEL) (IEEE, 2003), pp. 419–426.
- 47. Y. Pointurier and F. Heidari, "Reinforcement learning based routing in all-optical networks," in Fourth International Conference on Broadband Communications, Networks and Systems (BROADNETS) (IEEE, 2007), pp. 919–921.
- 48. I. Koyanagi, T. Tachibana, and K. Sugimoto, "A reinforcement learning-based lightpath establishment for service differentiation

- in all-optical WDM networks," in IEEE Global Telecommunications Conference (GLOBECOM) (IEEE, 2009).
- 49. J. Suárez-Varela, A. Mestres, J. Yu, et al., "Routing in optical transport networks with deep reinforcement learning," J. Opt. Commun. Networking 11, 547–558 (2019).
- 50. R. Shiraki, Y. Mori, H. Hasegawa, et al., "Dynamic control of transparent optical networks with adaptive state-value assessment enabled by reinforcement learning," in 21st International Conference on Transparent Optical Networks (ICTON) (IEEE, 2019).
- 51. R. Shiraki, Y. Mori, H. Hasegawa, et al., "Reinforcement-learningbased optical-path routing and wavelength assignment with adaptation to traffic-distribution change," IEICE Tech. Rep. 119, 23–27 (2019).
- 52. Y.-C. Huang, J. Zhang, and S. Yu, "Self-learning routing for optical networks," in Optical Network Design and Modeling (ONDM) (2020), pp. 467–478.
- 53. Z. Zhao, Y. Zhao, H. Ma, et al., "Cost-efficient routing, modulation, wavelength and port assignment using reinforcement learning in optical transport networks," Opt. Fiber Technol. 64, 102571 (2021).
- 54. M. Freire-Hermelo, A. Lavignotte, and C. Lepers, "Dynamic modulation format and wavelength assignment in optical networks using reinforcement learning," in OSA Advanced Photonics Congress (2021), paper NeF2B.4.
- 55. Y. Liu, B. Chen, G. Su, et al., "A waveband routing method in optical networks based on the deep reinforcement learning," in 26th Optoelectronics and Communications Conference (Optica Publishing Group, 2021), paper JS3C.1.
- 56. J. W. Nevin, S. Nallaperuma, N. A. Shevchenko, et al., "Techniques for applying reinforcement learning to routing and wavelength assignment problems in optical fiber communication networks," J. Opt. Commun. Netw. 14, 733–748 (2022).
- 57. N. Di Cicco, M. Ibrahimi, S. Troia, et al., "DeepLS: local search for network optimization based on lightweight deep reinforcement learning," IEEE Trans. Netw. Serv. Manage. 21, 108–119 (2023).
- 58. S. Nallaperuma, Z. Gan, J. Nevin, et al., "Interpreting multiobjective reinforcement learning for routing and wavelength assignment in optical networks," J. Opt. Commun. Netw. 15, 497–507 (2023).
- 59. R. R. Reyes and T. Bauschert, "Adaptive and state-dependent online resource allocation in dynamic optical networks," J. Opt. Commun. Netw. 9, B64–B77 (2017).
- 60. B. Li and Z. Zhu, "DeepCoop: leveraging cooperative DRL agents to achieve scalable network automation for multi-domain SD-EONs," in Optical Fiber Communication Conference (OFC) (2020), paper Th2A.29.
- 61. X. Li, Y. Zhao, Y. Li, et al., "Multi-objective routing and resource allocation based on reinforcement learning in optical transport networks," in Asia Communications and Photonics Conference/ International Conference on Information Photonics and Optical Communications (ACP/IPOC) (Optica Publishing Group, 2020), paper M4A.205.
- 62. R. Romero Reyes and T. Bauschert, "Towards DRL-based routing and spectrum assignment in optical networks: lessons to be learned from Markov decision processes," in IEEE Latin-American Conference on Communications (LATINCOM) (IEEE, 2021).
- 63. Z. Zhao, Y. Zhao, Y. Li, et al., "Reinforced resource allocation based on n-dimensional matrix diagram for multi-modal optical networks," in 26th Optoelectronics and Communications Conference (Optica Publishing Group, 2021), paper JS2A.1.
- 64. Y. Wang, Y. Mori, and H. Hasegawa, "Dynamic routing and spectrum allocation based on actor-critic learning for multi-fiber elastic optical networks," in Photonics in Switching and Computing 2021 (Optica Publishing Group, 2021), paper W1B.3.
- 65. H. T. Quang, O. Houidi, J. Errea-Moreno, et al., "MAGC-RSA: multi-agent graph convolutional reinforcement learning for distributed routing and spectrum assignment in elastic optical networks," in European Conference on Optical Communication (ECOC) (2022).
- 66. K. Cruzado, R. Shiraki, Y. Mori, et al., "Reinforcement-learningbased network design and control with stepwise reward variation

- and link-adjacency embedding," in European Conference on Optical Communication (ECOC) (2022).
- 67. L. Zhao, S. Yin, Y. Chai, et al., "A RSA policy with failure probability based on reinforcement learning in multi-band optical network," in 20th International Conference on Optical Communications and Networks (ICOCN) (2022).
- 68. Y. Jiao, S. Yin, T. Jin, et al., "Reliability-oriented RSA combined with reinforcement learning in elastic optical networks," in 20th International Conference on Optical Communications and Networks (ICOCN) (IEEE, 2022).
- 69. P. Almasan, J. Suárez-Varela, K. Rusek, et al., "Deep reinforcement learning meets graph neural networks: exploring a routing optimization use case," Comput. Commun. 196, 184–194 (2022).
- 70. G. Zhang, H. Ding, Y. Wang, et al., "A service routing optimization algorithm for power communication optical transport network based on knowledge graph and reinforcement learning," in International Conference on Autonomous Unmanned Systems (ICAUS) (2022), pp. 1337–1346.
- 71. S. Arce, L. A. Albertini, I. Rios, et al., "Reinforcement learning applied to the routing and spectrum assignment in elastic optical networks," in IEEE Latin American Conference on Computational Intelligence (LA-CCI) (IEEE, 2022).
- 72. P. Sharma, S. Gupta, V. Bhatia, et al., "Deep reinforcement learning-based routing and resource assignment in quantum key distribution-secured optical networks," IET Quantum Commun. 4, 136–145 (2023).
- 73. X. Lin, Y.-C. Huang, H. Zhang, et al., "A deep-reinforcementlearning-based dynamic scheduling of delay-tolerant requests in elastic optical networks," in Asia Communications and Photonics Conference/International Photonics and Optoelectronics Meetings (ACP/POEM) (2023).
- 74. C. Hernández-Chulde, R. Casellas, R. Martínez, et al., "Experimental evaluation of a latency-aware routing and spectrum assignment mechanism based on deep reinforcement learning," J. Opt. Commun. Netw. 15, 925–937 (2023).
- 75. J. Chen, X. Li, J. Wu, et al., "GSADDQN: combining GraphSAGE and reinforcement learning for routing optimization in softwaredefined optical transport network," Opt. Fiber Technol. 89, 104059 (2024).
- 76. Y. Wang, Y. Mori, and H. Hasegawa, "Resource assignment based on core-state value evaluation to handle crosstalk and spectrum fragments in SDM elastic optical networks," in Opto-Electronics and Communications Conference (OECC) (IEEE, 2020).
- 77. C. Shi, M. Zhu, J. Gu, et al., "Deep-reinforced impairment-aware dynamic resource allocation in nonlinear elastic optical networks," in 26th Optoelectronics and Communications Conference (Optica Publishing Group, 2021), paper M4A.8.
- 78. M. Shimoda and T. Tanaka, "Deep reinforcement learningbased spectrum assignment with multi-metric reward function and assignable boundary slot mask," in Opto-Electronics and Communications Conference (OECC) (2021).
- 79. N. E. D. E. Sheikh, E. Paz, J. Pinto, et al., "Multi-band provisioning in dynamic elastic optical networks: a comparative study of a heuristic and a deep reinforcement learning approach," in Optical Network Design and Modeling (ONDM) (2021).
- 80. L. Xu, Y.-C. Huang, Y. Xue, et al., "Spectrum continuity and contiguity aware state representation for deep reinforcement learning-based routing of EONs," in IEEE 6th Optoelectronics Global Conference (OGC) (2021), pp. 73–76.
- 81. X. Chen, R. Proietti, C.-Y. Liu, et al., "A multi-task-learning-based transfer deep reinforcement learning design for autonomic optical networks," IEEE J. Sel. Areas Commun. 39, 2878–2889 (2021).
- 82. M. Gonzalez, F. Condon, P. Morales, et al., "Improving multi-band elastic optical networks performance using behavior induction on deep reinforcement learning," in IEEE Latin-American Conference on Communications (LATINCOM) (IEEE, 2022).
- 83. A. B. Terki, J. Pedro, A. Eira, et al., "Routing and spectrum assignment assisted by reinforcement learning in multi-band optical networks," in European Conference on Optical Communication (ECOC) (2022).

- 84. B. Tang, Y.-C. Huang, Y. Xue, et al., "Deep reinforcement learningbased RMSA policy distillation for elastic optical networks," Mathematics 10, 3293 (2022).
- 85. L. Cheng and Y. Qiu, "Routing and spectrum assignment employing long short-term memory technique for elastic optical networks," Opt. Switching Netw. 45, 100684 (2022).
- 86. Y. Tu, B. Tang, and Y.-C. Huang, "Entropy-based reward design for deep reinforcement learning-enabled routing, modulation and spectrum assignment of elastic optical networks," in Asia Communications and Photonics Conference (ACP) (2022), pp. 1168–1172.
- 87. J. Momo Ziazet and B. Jaumard, "Deep reinforcement learning for network provisioning in elastic optical networks," in IEEE International Conference on Communications (ICC 2022) (IEEE, 2022), pp. 4450–4455.
- 88. J. Pinto-Ríos, F. Calderón, A. Leiva, et al., "Resource allocation in multicore elastic optical networks: a deep reinforcement learning approach," Complexity 2023, 1–13 (2023).
- 89. J. Errea, D. Djon, H. Q. Tran, et al., "Deep reinforcement learningaided fragmentation-aware RMSA path computation engine for open disaggregated transport networks," in Optical Network Design and Modeling (ONDM) (IEEE, 2023).
- 90. A. Beghelli, P. Morales, E. Viera, et al., "Approaches to dynamic provisioning in multiband elastic optical networks," in Optical Network Design and Modeling (ONDM) (2023).
- 91. T. Tanaka and M. Shimoda, "Pre- and post-processing techniques for reinforcement-learning-based routing and spectrum assignment in elastic optical networks," J. Opt. Commun. Netw. 15, 1019–1029 (2023).
- 92. L. Xu, Y.-C. Huang, Y. Xue, et al., "Hierarchical reinforcement learning in multi-domain elastic optical networks to realize joint RMSA," J. Lightwave Technol. 41, 2276–2288 (2023).
- 93. R. Sadeghi, B. Correia, E. London, et al., "Performance comparison of optical networks exploiting multiple and extended bands and leveraging reinforcement learning," in Optical Network Design and Modeling (ONDM) (2023).
- 94. Y. Tang, D. Chen, M. You, et al., "A routing and spectrum assignment algorithm for electric power elastic optical networks based on deep reinforcement learning," in 2nd Asia Power and Electrical Technology Conference (APET) (2023), pp. 729–733.
- 95. Y. Teng, C. Natalino, H. Li, et al., "Deep-reinforcement-learningbased RMSCA for space division multiplexing networks with multi-core fibers [Invited Tutorial]," J. Opt. Commun. Networking 16, C76–C87 (2024).
- 96. Z. Xiong, Y.-C. Huang, and X. Hu, "Graph attention network enhanced deep reinforcement learning framework for routing, modulation, and spectrum allocation in EONs," in Asia Communications and Photonics Conference (ACP) and International Conference on Information Photonics and Optical Communications (IPOC) (IEEE, 2024).
- 97. Y. Teng, C. Natalino, F. Arpanaei, et al., "DRL-assisted dynamic QoT-aware service provisioning in multi-band elastic optical networks," arXiv (2024).
- 98. E. Unzain, R. Fernandez, and D. P. Pinto-Roa, "Reinforcement learning based routing, modulation level and spectrum assignment in elastic optical networks," in L Latin American Computer Conference (CLEI) (IEEE, 2024).
- 99. Z. Zhou, R. Gu, X. Zhang, et al., "Opti-DeepRoute: a topologyadaptive deep reinforcement learning based service provisioning framework for elastic optical network," in IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS) (IEEE, 2024).
- 100. S. Li, X. Lin, Y. Liu, et al., "OpticGAI: generative AI-aided deep reinforcement learning for optical networks optimization," in Proceedings of the 1st SIGCOMM Workshop on Hot Topics in Optical Technologies and Applications in Networking (ACM, 2024).
- 101. J. Xie, Y. Song, Y. Zhang, et al., "Physical layer-aware route and spectrum allocation in optical networks by multi-objective deep reinforcement learning," in Asia Communications and Photonics Conference (ACP) and International Conference on Information Photonics and Optical Communications (IPOC) (IEEE, 2024).

- 102. D. Yan, N. Feng, J. Lv, et al., "DRL-based fragmentation- and impairment-aware resource allocation algorithm in C + L band elastic optical networks," Opt. Fiber Technol. 90, 104133 (2024).
- 103. J. Boyan and M. Littman, "Packet routing in dynamically changing networks: a reinforcement learning approach," in Advances in Neural Information Processing Systems, vol. 6, J. Cowan and G. Tesauro, eds. (Morgan-Kaufmann, 1993).
- 104. H. Ma, Y. Zhao, Y. Li, et al., "Demonstration of image processing based on reinforcement learning in multi-modal optical transport networks," in 18th International Conference on Optical Communications and Networks (ICOCN) (IEEE, 2019).
- 105. Z. Zhao, Y. Zhao, D. Wang, et al., "Reinforcement-learning-based multi-failure restoration in optical transport networks," in Asia Communications and Photonics Conference (ACP) (2019).
- 106. X. Wang, Y.-C. Huang, J. Liu, et al., "A subcarrier-slot autonomous partition scheme based on deep-reinforcement-learning in elastic optical networks," in Asia Communications and Photonics Conference (ACP) (2019).
- 107. X. Luo, C. Shi, L. Wang, et al., "Leveraging double-agent-based deep reinforcement learning to global optimization of elastic optical networks with enhanced survivability," Opt. Express 27, 7896–7911 (2019).
- 108. C. Natalino and P. Monti, "The Optical RL-Gym: an open-source toolkit for applying reinforcement learning in optical networks," in 22nd International Conference on Transparent Optical Networks (ICTON) (2020).
- 109. Q. Ma, A. Xiong, P. Yu, et al., "Co-allocation of service routing in SDN-driven 5G IP+optical smart grid communication networks based on deep reinforcement learning," in International Wireless Communications and Mobile Computing (IWCMC) (IEEE, 2020), pp. 868–873.
- 110. C. Wang, N. Yoshikane, F. Balasis, et al., "DeepCMS<sup>3</sup> : a deep reinforcement learning framework for core, mode and spectrum sequential scheduling over optical transport network," in European Conference on Optical Communications (ECOC) (IEEE, 2020).
- 111. R. Weixer, S. Kuhl, R. M. Morais, et al., "A reinforcement learning framework for parameter optimization in elastic optical networks," in European Conference on Optical Communications (ECOC) (IEEE, 2020).
- 112. H. Liu, R. Gu, Z. Li, et al., "Multi-agent federated reinforcement learning for privacy-enhanced service provision in multi-domain optical network," in 2021 Asia Communications and Photonics Conference (ACP) (2021), pp. 1–3.
- 113. Z. Zhao, Y. Zhao, Y. Li, et al., "Service restoration in multi-modal optical transport networks with reinforcement learning," Opt Express 29, 3825–3840 (2021).
- 114. X. Tian, B. Li, R. Gu, et al., "Reconfiguring multicast sessions in elastic optical networks adaptively with graph-aware deep reinforcement learning," J. Opt. Commun. Netw. 13, 253–265 (2021).
- 115. P. Morales, P. Franco, A. Lozada, et al., "Multi-band environments for optical reinforcement learning gym for resource allocation in elastic optical networks," in Optical Network Design and Modeling (ONDM) (2021).
- 116. T. Tanaka and K. Higashimori, "Reinforcement-learning-based multilayer path planning framework that designs grooming, route, spectrum, and operational mode," in European Conference on Optical Communication (ECOC) (2022).
- 117. R. Koch, S. Kühl, R. M. Morais, et al., "Reinforcement learning for generalized parameter optimization in elastic optical networks," J. Lightwave Technol. 40, 567–574 (2022).
- 118. C. Hernández-Chulde, R. Casellas, R. Martínez, et al., "Evaluation of deep reinforcement learning for restoration in optical networks," in Optical Fiber Communication Conference (OFC) (2022), paper Th2A.19.
- 119. E. Etezadi, C. Natalino, R. Diaz, et al., "DeepDefrag: a deep reinforcement learning framework for spectrum defragmentation," in IEEE Global Communications Conference (GLOBECOM) (2022), pp. 3694–3699.
- 120. E. Etezadi, C. Natalino, R. Diaz, et al., "Deep reinforcement learning for proactive spectrum defragmentation in elastic optical networks," J. Opt. Commun. Networking 15, E86–E96 (2023).

- 121. T. Tanaka, "Adaptive traffic grooming using reinforcement learning in multilayer elastic optical networks," in Optical Fiber Communication Conference (OFC) (2023), paper Tu2D.6.
- 122. S. S. Johari, S. Taeb, N. Shahriar, et al., "DRL-assisted reoptimization of network slice embedding on EON-enabled transport networks," IEEE Trans. Netw. Serv. Manage. 20, 800–814 (2023).
- 123. J. Zhang, Z. Chen, B. Zhang, et al., "ADMIRE: collaborative data-driven and model-driven intelligent routing engine for traffic grooming in multi-layer X-Haul networks," J. Opt. Commun. Networking 15, A63–A73 (2023).
- 124. Y. Fan, Y. Li, B. Zhang, et al., "Blocking-driven spectrum defragmentation based on deep reinforcement learning in tidal elastic optical networks," in 21st International Conference on Optical Communications and Networks (ICOCN) (2023).
- 125. M. Lian, Y. Zhao, Y. Li, et al., "Dynamic slicing of multidimensional resources in DCI-EON with penalty-aware deep reinforcement learning," J. Opt. Commun. Netw. 16, 112–126 (2024).
- 126. X. Li and Y. Wang, "TABDeep: a two-level action branch architecture-based deep reinforcement learning for distributed sub-tree scheduling of online multicast sessions in EON," Comput. Netw. 243, 110288 (2024).
- 127. Y. Wang, L. Kong, M. Zhu, et al., "Availability-aware and delaysensitive RAN slicing mapping based on deep reinforcement learning in elastic optical networks," IEEE Trans. Netw. Service Manage. 21, 6026–6040 (2024).
- 128. S. Yin, L. Liu, M. Cai, et al., "DNN distributed inference offloading scheme based on transfer reinforcement learning in metro optical networks," J. Opt. Commun. Netw. 16, 852–867 (2024).
- 129. S. K. Tse, X. Zhao, A. Chan, et al., "Reinforcement learning for power management in low-margin optical networks," in 24th International Conference on Transparent Optical Networks (ICTON) (IEEE, 2024).
- 130. T. Tanaka, "Reinforcement-learning-based path planning in multilayer elastic optical networks [Invited]," J. Opt. Commun. Networking 16, A68–A77 (2024).
- 131. M. Doherty and A. Beghelli, "XLRON: accelerated reinforcement learning environments for optical networks," in Optical Fiber Communication Conference (OFC) (2024), paper Th2A.21.
- 132. C. Natalino, T. Magalhães, F. Arpanaei, et al., "Optical Networking Gym: an open-source toolkit for resource assignment problems in optical networks," J. Opt. Commun. Networking 16, G40–G51 (2024).
- 133. R. McCann, A. Rezaee, and V. M. Vokkarane, "SDONSim: an advanced simulation tool for software-defined elastic optical networks," arXiv (2024).
- 134. N. Jara, H. Pempelfort, E. Viera, et al., "DREAM-ON GYM: a deep reinforcement learning environment for next-gen optical networks," in Proceedings of the 14th International Conference on Simulation and Modeling Methodologies, Technologies and Applications (SCITEPRESS - Science and Technology Publications, 2024), pp. 215–222.
- 135. R. Matzner, A. Ahuja, R. Sadeghi, et al., "Topology Bench: systematic graph based benchmarking for core optical networks," arXiv (2024).
- 136. Z. Luo, S. Yin, L. Zhao, et al., "Survivable routing, spectrum, core and band assignment in multi-band space division multiplexing

- elastic optical networks," J. Lightwave Technol. 40, 3442–3455 (2022).
- 137. R. Koch, S. Kuhl, W. Schairer, et al., "High-generalizability reinforcement learning based capacity optimization in WDM long-haul networks," IEEE Photonics Technol. Lett. 34, 891–894 (2022).
- 138. X. Chen, "DeepRMSA GitHub repository," GitHub (2019) [accessed 6 January 2024], https://github.com/xiaoliangchenUCD/ DeepRMSA.
- 139. L. Engstrom, A. Ilyas, S. Santurkar, et al., "Implementation matters in deep policy gradients: a case study on PPO and TRPO," arXiv (2020).
- 140. P. Nagarajan, G. Warnell, and P. Stone, "The impact of nondeterminism on reproducibility in deep reinforcement learning," in 2nd Reproducibility in Machine Learning Workshop at ICML 2018 (2018).
- 141. S. Huang and S. Ontañón, "A closer look at invalid action masking in policy gradient algorithms," in The International FLAIRS Conference Proceedings, Vol. 35 (2022).
- 142. O. Vinyals, M. Fortunato, and N. Jaitly, "Pointer networks," arXiv (2015).
- 143. S. Baroni, "Routing and wavelength allocation in WDM optical networks," Ph.D. thesis (University College London, 1998).
- 144. P. Henderson, R. Islam, P. Bachman, et al., "Deep reinforcement learning that matters," arXiv (2019).
- 145. K. P. White and S. Robinson, "The problem of the initial transient (again), or why MSER works," in Proceedings of the 2009 INFORMS Simulation Society Research Workshop, L. H. Lee, M. E. Kuhl, J. W. Fowler, et al., eds. (Institute for Operations Research and the Management Sciences, 2009), pp. 90–95.
- 146. V. Curri, "GNPy model of the physical layer for open and disaggregated optical networking [Invited]," J. Opt. Commun. Netw. 14, C92–C104 (2022).
- 147. H. Buglia, M. Jarmolovicius, A. Vasylchenkova, ˇ et al., "A closedform expression for the Gaussian noise model in the presence of inter-channel stimulated Raman scattering extended for arbitrary loss and fibre length," J. Lightwave Technol. 41, 3577–3586 (2023).
- 148. K. Cruzado, Y. Mori, S.-C. Lin, et al., "Effective capacity estimation based on cut-set load analysis in optical path networks," in International Conference on Photonics in Switching and Computing (PSC) (2023).
- 149. K. Cruzado, Y. Mori, S.-C. Lin, et al., "Capacity-bound evaluation and routing and spectrum assignment for elastic optical path networks with distance-adaptive modulation," in Optical Fiber Communication Conference (OFC) (2024), paper W3C.6.
- 150. A. Beghelli, "Resource allocation and scalability in dynamic wavelength-routed optical networks," Ph.D. thesis (University of London, 2006).
- 151. B. Awerbuch, Y. Azar, and S. Plotkin, "Throughput-competitive on-line routing," in IEEE 34th Annual Foundations of Computer Science (IEEE, 1993), pp. 32–40.
- 152. B. Li and Z. Zhu, "GNN-based hierarchical deep reinforcement learning for NFV-oriented online resource orchestration in elastic optical DCIs," J. Lightwave Technol. 40, 935–946 (2022).
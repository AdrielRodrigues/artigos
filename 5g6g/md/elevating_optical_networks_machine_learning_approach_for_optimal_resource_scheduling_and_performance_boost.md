---
title: "Elevating optical networks: Machine learning approach for optimal resource scheduling and performance boost"
tema_principal: 5g6g
temas_relacionados: []
ano: null
autores: []
veiculo: null
pdf: ../pdf/elevating_optical_networks_machine_learning_approach_for_optimal_resource_scheduling_and_performance_boost.pdf
---

#### RESEARCH ARTICLE

![](_page_0_Picture_6.jpeg)

# Elevating optical networks: Machine learning approach for optimal resource scheduling and performance boost

Neetha Kala S.S. <sup>1</sup> | Aaditya Jain<sup>2</sup> | Rahul Bhatt <sup>3</sup> | Sanjay Kumar Sinha<sup>4</sup> | Pankaj Saraswat <sup>5</sup> | Prabhakaran<sup>6</sup>

2 College of Computing Science and Information Technology, TeerthankerMahaveer University, Moradabad,Uttar Pradesh, India, India 3 School of Engineering and Computer, Dev Bhoomi Uttarakhand University, Dehradun, India

4 Department of Computer Science & Engineering, Vivekananda Global University, Jaipur, India

5 Department of Computer Science & Engineering, Sanskriti University, Mathura, India

6 Department of Computer Application, Presidency College, Bangalore, India

### Correspondence

Neetha Kala S.S., Assistant Professor, Department of Computer Science and Information Technology, Jain (Deemed to be University), Bangalore, Karnataka, India.

Email: [ssneethakala55@gmail.com](mailto:ssneethakala55@gmail.com)

### Summary

The increasing demand for massaging networks that are stable and quick needs reevaluations of standard optical networking administration strategies. To improve the efficacy of optical networks by integrating machine learning (ML) approach for the best resource scheduling, this research presents an innovative dynamic block widow optimized random forest (DBWO-RF) strategy. To implement the DBWO-driven resource allocation method in accordance with the categorization and clustering findings, the RF method is incorporated with the software defined optical to achieve channel quality assessment after successfully clustering employs the RF approach to achieve channel quality assessment after successfully clustering traffic patterns using the fuzzy C-means (FCM) algorithm. To lessen the likelihood of blocking, the fragmentation-function-fit (FFF) algorithm was provided and the findings indicate that this approach possesses a reduced blocking risk. Using multiple approaches to modulation for various channel quality, the suggested resource allocation system leverages the DBWO approach to distribute the necessary resources based on various "traffic flow (TF)" clustering findings. The examination's outcomes demonstrate that, compared to other techniques under various given load levels, the present study has a reduced blocking risk, a sufficient complexity degree and greater effectiveness in the utilization of spectrum resources.

#### KEYWORDS

blocking risk, complexity, dynamic black widow optimized random forest (DBWO-RF), optical network, resource scheduling, SDON controller

# 1 | INTRODUCTION

Performance boost and optimal resource scheduling are essential in today's dynamic computing and project management environments. In the rapidly changing world of technology, where productivity and efficiency are critical, it is essential for individuals as well as organizations to allocate resources and strive for improved performance.[1](#page-10-0) The art of resource scheduling, which involves assigning and managing resources like assets, labor, and time, has become essential to improving project outputs and workflows.[2](#page-10-0) Using the newly developed flexible optical transport technology, spectrum resources in optical data center networks (ODCNs) are more equitably distributed among individual requests.

<sup>1</sup> Department of Computer Science and Information Technology, Jain (Deemed to be University), Bangalore, Karnataka, India, India

10991131, 2024, 17, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/dac.5936 by University Of Sao Paulo - Brazil, Wiley Online Library on [25/08/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Efficient resource scheduling guarantees timely work completion. In addition, it facilitates the optimization of available assets, guarantees that each asset is fully engaged, and thus augments total success and economy of range.[3](#page-10-0) In the everchanging telecommunications setting, the increasing need for high-speed protected data transmission has pressed optical network to the forefront of technical innovation. These networks, which use light to spread data, are attractive essential in overcoming the drawbacks of conventional copper-based systems.[4](#page-10-0)

Advanced reserve allocation algorithms in optical networks are essential for the growing number of bandwidthintensive application and the exponential increase of digital in sequence. Advanced scheduling algorithms are necessary due to various challenges, including varying traffic patterns, congestion organization, and the elaborate design of this network.[5](#page-10-0) Successful resource forecasting is essential for reducing latency, packet loss, and power usage, as well as maximizing throughput, all of which improve user experience. Understanding the basic history of optical networks is crucial for understanding the complexities of efficient resource allocation in these networks.[6](#page-10-0) The increase of optical networks signifies a model change in data transfer, outperforming the constraints of usual copper-based system. A large volume of data can be transmitted over great distances with little signal degradation using optical fibers, which form the basis of current communication networks.[7](#page-10-0)

The "software-defined optical networks (SDON)" benefits of huge optic transport capacity, low power consumption, and lower capital cost are highlighted, together with flexible SDN control.[8](#page-10-0) Because of the volatility of user needs and the intense complexity of such networks, superior arrangement algorithms are essential to ensure efficient reserve utilization and avoid bottlenecks[.9](#page-10-0) In optical networks, resource scheduling is a complex process that includes allocating bandwidth, routing pathway, and other fundamental assets to meet a range of traffic demands. In addition to being critical for improving network effectiveness, a well-designed scheduling system helps to reduce energy usage, latency, and packet loss. The interdependence of variables highlights the inclusive strategy needed for source arrangement to attain the best outcome.[10](#page-10-0)

The sustainable growth of optical networks is an increasing concern in the modern world. The carbon footprint is influenced by the energy usage of communication networks, especially optical networks. By giving out resources depending on demand, optimal planning of resources can contribute in minimizing energy usage and lowering the overall environmental effect.[11](#page-10-0) Traditional ODCNs are under a lot of strain due to the internet's high-rate traffic demand expanding quickly, such as demands from big data, cloud-based applications, and high-definition films.[12](#page-10-0)

The main objective of this approach is to use the DBWO-RF enabled flexible allocation of resources mechanism to provide flexible connectivity and spectral management in ODCN.

# 1.1 | Key contributions

- The main contribution of this research is the proposed use of DBWO-RF to enhance optical networks
- This study presents a novel method, the DBWO-RF technique, to address the expanding demand for fast and dependable communication networks in optical networks.
- The objective of this research is to optimize the efficiency of optical networks through the implementation of the DBWO-RF strategy, which incorporates ML to enable adaptive resource allocation. Reducing blocking issues is the main objective of the FFF algorithm.

The remaining research can be grouped into the following categories: Section 2 outlined a technique for allocating resources in ODCNs that relies on ML and SDON. In Section [3,](#page-3-0) we present our proposed method. Section [4](#page-6-0) describes the experimental result of this study, and Section [5](#page-9-0) concludes the paper.

# 2 | LITERATURE REVIEW

Peng et al[.13](#page-10-0) implemented online resource-performance models, Optimus, an adapted work scheduling for deep neural network (DNN) clusters, which reduced the required processing time. Optimus employed online fitting to predict model convergence during training and set up models of performance to precisely determine the rate of training as a result of resources allocated in each task. Cui et al[.14](#page-10-0) employed a deep learning (DL) technique that enabled effective scheduling of links based on the relative positions of transmitters and receivers, thereby avoiding the need for channel estimation. This approach is particularly useful because wireless channel intensity varies due to distance-dependent path loss in various propagation environments.

Liu et al[.15](#page-10-0) presented a resource allocation strategy that trades off "energy efficiency and spectrum efficiency (EE +SE)" to minimize the weighted sum of secondary interference power. Challita et al.[16](#page-11-0) presented a unique resource allocation methodology for "long term evolution - licensed assisted access (LTE-LAA)" and WiFi coexistence in the unregulated band. They developed a game model in which all "small base stations (SBS)" aiming to achieve long-term equal-weighted fairness along with "Wireless Local Area Network (WLAN)" as well as LTE-LAA operators transmitting in the same channel have to optimize their rates in a specified time horizon. Li et al[.17](#page-11-0) suggested a framework for AIassisted provisioning to enable "virtual network function service chain (vNF-SCs)" in "inter-datacenter elastic optical network (IDC-EONs)" to be provisioned on-demand and affordably. Because the framework was intended to be a discretetime system, its operations were scheduled into set "time slots (TS)," with predeployment and provisioning phases occurring during each TS. Wang et al[.18](#page-11-0) examined the way to use supervised learning to uncover the commonalities concealed in a sizable body of historical information on scenarios and offered an ML structure for allocating resources. The optimal or nearly optimal approach for a highly similar historical case was chosen to assign the radio resources to the present scenario by taking advantage of the extracted similarities. Jiang et al.[19](#page-11-0) suggested the use of binary computation offloading in conjunction with "hybrid DL-driven online offloading (H2O)" to reduce the overall consumption of energy of "user equipment's (UEs)" in an H-MEC network. The three AI algorithms were part of the structure. Zhuge et al.[20](#page-11-0) recognized the use of ML in the model and monitor of natural language interfaces (NLI). Specifically, their initial suggestion was to standardize the inaccuracy of existing fiber nonlinearity model using the ML technique.

Yan et al[.21](#page-11-0) presented an "intelligent resource scheduling technique (iRSS)" for "5G RAN" slicing. iRSS's primary goal was to take benefit of a shared educational framework that collective reinforcement learning (RL) and DL. To be more specific, large-scale store allocation was accepted out using DL and small-scale system dynamics, such as invalid predictions and unexpected network states, were handled by RL using online reserve scheduling. Martin et al[.22](#page-11-0) established the network resource allocator technique for autonomous network management that considers "quality of experience (QoE)." That system forecasted demand to anticipate how many group resources would need to be assigned and what construction would be needed to handle the required traffic. Qiu et al.[23](#page-11-0) suggested deploying a "softwaredefined Space-Time Network (STN) to organize and control computing, network and caching resources." They engaged a deep Q-learning system to attempt the joint allocate assets problem, which they phrased as a joint optimization problem. Khan et al.[24](#page-11-0) established a discussion of the mathematical underpinnings of fundamental ML methods from the standpoints of signal processing and communication theory. That in turn clarified the kinds of networking and optical communication issues that logically necessitate the application of ML. Zappone et al[.25](#page-11-0) provided a description of two techniques that bring the proposal into action with the goal of improving wireless networks. Furthermore, numerical outcomes were presented to evaluate the effectiveness of the suggested methods in comparison to implementations that were based on data.

Singh and Jukan[26](#page-11-0) demonstrated a "ML-based resource allocation and reallocation (ML-RAR)" strategy that relied on predictive and statistical knowledge of connection mean holding times. While demonstrating the benefits of traffic forecasting in resource allocation, data center traffic follows heavy-tailed distributions such as lognormal. Liu et al[.27](#page-11-0) examined a heterogeneous Internet of things system based on "non-orthogonal multiple access (NOMA)" and assumed incomplete "successive interference cancellation (SIC)." To assign radio resources and pair users, an energy-efficient optimization problem was created. A particular technique was used to examine the cognitive radio networks. Li et al.[28](#page-11-0) established a hybrid computation framework and developed an efficient resource scheduling technique for satisfying real-time needs for smart production using edge computing support. Tran and Pompili[29](#page-11-0) suggested an elaborate strategy for sharing resources and offloading tasks in a multicell "mobile-edge computing (MEC)" system. An extremely intricate "mixed-integer nonlinear program (MINLP)" was used to originate the fundamental optimization problem. Yang et al.[30](#page-11-0) examined ambient "orthogonal frequency division multiplexing (OFDM)" carriers in a "full-duplex AmBC network (F-ABCN)." Together, the "backscattering devices (BDs)" control reflecting coefficients, subcarrier control allowance from the "full-duplex access point (FAP)," and backscatter time allocation were optimized to maximize the lowest throughput among all BDs.

Rahimi et al.[31](#page-11-0) discuss dynamic radio resource allocation in an SDN-based virtual Fog radio access network (RAN), aiming to maximize transmit beam forming, resource block assignment, and user equipment assignment while accounting for incomplete channel information. Partial optimization problem with set of RUs for efficient design (POPSOED) seeks to optimize resource efficiency and IIoT user satisfaction by successively addressing mixed-integer nonlinear and multiple knapsack problems. This minimizes network power consumption and maximizes feasible sum-rate. Kalpana et al[.32](#page-11-0) focus on using IoT to improve the efficiency of renewable energy sources, namely, in the evaluation of solar and wind energy and in the estimation of module lifetimes. The goal of the project is to increase the prediction accuracy of <span id="page-3-0"></span>green energy output by using machine learning techniques to forecast electricity generated by wind. It assesses IoT technologies and algorithms for energy consumption projections, highlighting the importance of more accurate weather forecasts and reduced RMSE for the dependability of green energy. Tsai et al.[33](#page-11-0) utilize a two-level quality of service (QoS) model to maximize request satisfaction, and quality-aware fog service orchestrator (Q-FSO) addresses issues with IIoT application provisioning. This methodology maximizes service orchestration in fog computing (FC) settings by integrating critical variables such as cost, reaction time, availability, and dependability. In order to effectively handle concurrent requests, Q-FSO uses a local QoS assignment strategy based on MMKP-based heuristic algorithms (ISM and GMM). Scalability is ensured by a decentralized workflow construction protocol, which improves IIoT application orchestration speed, resource utilization, and service processing throughput. Salehnia et al.[34](#page-11-0) present an SDN-based method for job scheduling in IoT-fog systems (IoTFS) termed aquila optimizer combined with whale optimization algorithm (AWOA). By effectively allocating FC resources and lowering latency for IoT devices, AWOA seeks to optimize task execution time, makespan, and throughput. The concept improves network efficiency and reduces traffic overhead by utilizing a centralized IoTFS controller and SDN capabilities. This improves QoS metrics like task completion time. Yuan et al.[35](#page-11-0) presented an innovative dynamic controller assignment approach for Internet of Vehicles (IoV) applications. In order to assign controllers in real time, this method leverages a hierarchically distributed control plane that is distinct from the data plane. It does this by using control traffic load and vehicle location data. Cooperative multiagent deep reinforcement learning methods are applied to solve the problem, which is described as a multiagent Markov game. Simulation results with real-world vehicle mobility data reveal improved performance over the state-of-the-art approaches, with less packet loss and control latency in IoV situations.

Lin et al.[36](#page-11-0) suggest an SDIoV architecture that incorporates edge intelligence to fight traffic jams. In order to handle transmission and inference delays from cloud centralized computing, it uses a distributed multiagent reinforcement learning model for real-time vehicle routing decisions. Distributed training efficiency is improved using a softwaredefined device collaboration optimization technique. The distributed-learning-based vehicle routing determination algorithm (DLRD) is proven to be successful in minimizing traffic congestion and dynamically adjusting road conditions. Pushpavalli et al.[37](#page-11-0) present sophisticated deep learning models for accurate electrical power demand forecasting. It uses a structured workflow of data preprocessing, sequence generation, model training, and future demand prediction by utilizing historical load data, temperature, wind speed, and day-ahead market pricing. Compared to traditional methods, our methodology significantly improves prediction accuracy by over 11%. Beyond mere precision, its goal is to maximize the distribution of energy within local communities, presenting opportunities for sustainable energy practices and affordable management Montazerolghaem[38](#page-11-0) addresses load imbalance and energy loss issues in Internet of Multimedia Things (IoMT) networks by proposing a modular resource management system. Because of its computational complexity, it classifies the simultaneous optimization of load and energy as an NP-hard task. A dynamic controller efficiently distributes load across servers and routes traffic through switches by adjusting IoMT network resources based on size by utilizing virtual resources and network softwarization. Bagha et al.[39](#page-11-0) suggest the ELA-RCP algorithm for controller placement optimization in SDN to improve the network dependability and efficiency. It solves the controller placement problem (CPP) by strategically putting the ideal controller numbers according to path dependability, delay, and energy considerations, using cellular learning automata. By utilizing a greedy algorithm and queuing theory, ELA-RCP enhances both controller dependability and load balancing. Comparing simulations to current optimization techniques such as particle swarm and firefly algorithms, significant gains are shown in energy usage, delay, and network survivability. Gupta et al.[40](#page-11-0) suggests innovative methods for resource optimization in IoT devices, with an emphasis on scalability and energy efficiency in the face of heterogeneous device designs. With carefully placed edge servers, it presents a full-stack system architecture that can accommodate a range of IoT device needs. It improves the efficiency of data transmission by utilizing the African vulture optimization algorithm (AVOA) to link Cluster Head (CH) nodes and choose edge nodes based on proximity to cut down on latency and energy usage.

# 3 | AN SDON AND DBWO-RF-BASED RESOURCE ALLOCATION METHOD FOR ODCNS

In ODCNs, an overview of the topology on the global network and the use of resources are provided by the SDON controller. It selects an ideal modulation format after determining the best channel and data center node for the service based on the most efficient routing algorithm. It assesses the path's transmission performance. The goal of flexible resource allocation is to improve bandwidth efficiency in utilization and lessen spectral fragmentation.

FIGURE 1 A system for resource allocation in ODCNs based on ML and SDON. Source: Author.

To build an ODCN system database, we must collect data and eliminate physical layer features. To design a flexible transitional system for different offerings, we use "supervised ML" (DBWO-RF) to organize the "channel's quality" into four phases and "unsupervised ML" (FCM) for clustering the TFs. The predictive ML algorithm provides data to the SDON controller of the optical data storage network, which utilizes its TF clustering result. Adaptive spectrum algorithms like FFF are allocated by it. The ODCN system database is scheduled to be updated by the results of the network's resource allocation. The system model is shown in Figure 1.

# 3.1 | Channel quality classification using (DBWO-RF)

Channel quality classification using dynamic black widow optimized random forest (DBWO-RF). It combines DBWO with the efficient RF algorithm to improve the concert and flexibility of the model. DBWO enhances organizational effectiveness and accuracy by actively optimizing attribute collection and consideration changes. Through iterative design enhancement, DBWO-RF provides flexibility in dynamic channel environments, making it ideal for real-world applications such as wireless communication systems. The arrangement of DBWO and RF allow for perfect channel quality classification, which is important for improving user knowledge in an assortment of setting and network concert optimization. In optical networks, RF is a dependable ML advance for classifying channel quality. RF studies the association between channel quality labels  $(Y_i)$  and optical network attributes  $(X_i)$  by utilizing an assortment of decision trees. RF is employed for classifying channel quality. It constructs a collection of decision trees and aggregates their predictions to make the final classification. Integrating individual tree forecasts, each modified by a random selection of attributes and data points, yields the prediction  $\widehat{Y}_{RF}$ . In terms of math, this is stated as

$$\widehat{Y}_{RF} = \text{mode}\left\{Z_i^1, Z_i^2, ..., Z_i^K\right\}$$
(1)

where  $Y_i^K$  is the RF method's projected class of the  $K_{th}$  tree; the algorithm is good at addressing high-dimensional feature spaces, offering robustness to noise along with sudden shifts in optical network conditions and affording insights into the relevance of features. By using it, automatic and precise channel quality evaluations are made possible, which improves the dependability and effectiveness of optical systems for communication.

DBWO algorithm is applied to optimize RF parameters, ensuring classification accuracy while preventing overfitting. It adapts to variations in network conditions, traffic patterns, and topologies. The parameters are optimized using the DBWO algorithm. Which optimizes classification accuracy while preventing overfitting? DBWO is an evolutionary method modeled after the cooperative hunting behavior of black widow spiders. DBWO demonstrates its efficacy in optical network optimization by adjusting to network environment variations, including traffic patterns, connection conditions, and network topologies.

In this study, to perform inclusive evaluation and centralized processing of the data obtain from the telecom con-

In this study, to perform inclusive evaluation and centralized processing of the data obtain from the telecom contributor, we merge RF and DBWO. We aim to enable accurate and successful organization study by mapping the features of the visual link state to the channel quality. As a method for optimization to progress the categorization model's performance, we present DBWO method. Furthermore, we build a multiclassifier based on RF to assess and categorize the channel quality into four unusual levels, failed, excellent, good, and average. In order to increase the likelihood of identifying damaged transport links, this method offers a robust and flexible configuration for control quality assessment. The incorporation of DBWO optimization with RF classification improves the model's capacity to handle difficult connections in the data, resulting in better channel quality level classification exactness. Our goal is to offer telecom operators a more plastic and well-organized way to optimize network concert and locate areas for advance by using this novel method.

# 3.2 | Clustering of traffic flows

Traditional ODCNs use bandwidth allocation algorithms that take the entire size or quantity of packets waiting in queues, neglecting the different demands of TFs. After obtaining the telecom operator's realistic TFs, we use the FCM algorithm to arrange the patterns of traffic in ODCNs so that different spectrum assets can be allocated to TF. To distribute varied spectrum allocation across TFs, we obtain the actual TF from the telecom network. TFs in ODCNs are clustered using FCM due to its quick convergence time and straightforward premise. In clustering, FCM method works effectively. The FCM method provides strong clustering performance, an easy-to-understand principle, and a fast convergence time. FCM algorithm is used for clustering traffic flows in ODCNs. It partitions TFs based on similarities in traffic patterns, enabling the allocation of spectrum resources to different TF clusters.

# 3.3 | Suggested algorithms for allocating resources

Fragmentation is a measure of the amount of spectrum resources utilized. Additionally, it can indicate the probability of blockage in certain networks system, which further contributes to resource unused. The two factors that led to the fragmentation of the spectrum were the nonaligned and noncontinuous available slot blocks. If one or more open slot block is not next to one another, there are not enough neighboring blocks. This leads to the former situation. The reason behind the latter is improper arrangement of certain accessible slotted block on several links along the same route. The spectrum slot becomes accessible only when it appears on each link that opens up the path. FFF algorithm is proposed to reduce blocking probability by optimizing spectrum resource allocation. It iteratively allocates resources to minimize the global spectrum fragmentation function, thereby enhancing bandwidth efficiency.

This work proposes the FFF algorithm, which reduces the blockage probability. The blocking probability is a percentage of the blocked quantity to all service numbers. It can estimate the recommended system's available bandwidth resource more precisely. The "FFF algorithm" allocates in a way that will result in the lowest "global spectrum fragmentation function (GSF)" value by iteratively going through all of the large enough available slot blocks. Because it can reduce the waste of tiny spectrum fragments, this method places a strong emphasis on the bandwidth efficiency parameter. The definition of an enhanced evaluation function is

$$\eta(c) = -\frac{\sum\limits_{m=1}^{M} N_m \times Free(N_m) \times P_m \times t_d(m)}{totalfree}$$
 (2)

"M" is the overall amount of available subcarriers at that point, *totalfree* is all of the amenities available, and " $\eta(c)$ " is the length of time for a "spectrum fragmentation." The total amount of subcarriers required for facilities "(m)" at any given time is denoted by Nm. All of the network's continuous part of the package is represented by the value

are governed by the applicable Creative Commons

<span id="page-6-0"></span>"Free( $N_m$ )." The service has a Poisson distribution, a length of  $t_d(m)$  and a probability that is generated of  $P_m$ . A higher value of  $\eta(c)$  indicates the network is experiencing an additional fragmented spectrum globally. The increased "spectrum fragment perception function  $\eta(c)$ " functions as the foundation for the "spectrum fragment." With such a feature, amount of occurrence of invalid bandwidth resources and the growth and period of overall network spectral fragment.

# 3.4 | Mechanism for adaptable resource management (DBWO-RF)

The algorithm of shortest path routing is employed in this investigation. In accordance with the findings of TF clustering, we suggest a method for linking spectrum allocation methods. To manage network resources, it chooses the appropriate channel quality level. Clustering is the process used in this mechanism to group the TF rates.

The highest TF rate is found. The majority of the FCM clustering results are occupied by the largest TFs. "FFF" approach with the blocking probability is kept as low as feasible because these TFs use more resources. The "spectrum resource" needed provision demands provided to the highest degree possible. It has a quick convergence time and can lessen overall spectral blockage. We use a contraction for this system: DBWO-RF based resource management approach. Figure 2 displays the DBWO-RF mechanism flow chart.

#### 4 | EXPERIMENTAL RESULTS

This research used Python 3.11.4 to develop the required protocols, using a Windows 11 laptop with an Intel i5 11th Gen CPU and 32 GB of RAM. Figure 3 displays the fuzzy C-means clustering result. Light and dark red represent the TF with the lowest and highest rates, respectively, which shows the FCM algorithm clustering result. The majority of the quickest TFs are found in the ODCNs, as shown by these clustering results.

A total of 4060 records are extracted using Python for data preprocessing and each record contains 10 features: "power consumption (%), laser bias current (mA), detection point temperature (°C), module temperature inside (°C), input optical power (dBm), output optical power (dBm), central wavelength (nm), BER before and after FEC error correction, RS error rate and unusable time (s)." These features make up the model's input data. Every data sample consists of a feature array  $\chi_i$ , where  $\chi_i \in \chi = (\chi_1, \chi_2, \chi_3...\chi_{12})$ , according to the DBWO-RF. The label for each  $\chi_i$  is displayed in Table 1. In addition, we measure the information to [-4, 4], with 47% of the data that are used for testing and 53% for training. The classification accuracy with the DBWO algorithm was 95.3%. This result implies that channel quality is classified accurately by our method.

![](_page_6_Figure_10.jpeg)

<span id="page-7-0"></span>![](_page_7_Figure_3.jpeg)

FIGURE 3 Fuzzy C-means clustering outcome with higher and lower rates. Source: Author.

TABLE 1 Standard parameters for channel classification.

| Label               | 1                                                                                         | 1<br>                                                                                 | 3                                                                                    | 2                                                                                    |
|---------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Judging<br>criteria | After the FEC error<br>10,<br>correction, BER  (10<br>7<br>10<br>) unusable time  (0, 10) | After the FEC error<br>7<br>correction, BER  (10<br>, 100)<br>unusable time  (10, +∞) | After the FEC error<br>20,<br>correction, BER  (10<br>15)<br>10<br>unusable time = 0 | After the FEC error<br>15,<br>correction, BER  (10<br>10)<br>10<br>unusable time = 0 |
| Rank                | Medium                                                                                    | Failed                                                                                | Excellent                                                                            | Good                                                                                 |

![](_page_7_Figure_7.jpeg)

FIGURE 4 Inter-ODCN network topology. Source: Author.

We use many service types to simulate various scenarios in the static network topology. The inter-ODCN network structure is shown in Figure 4. This is a simulation-based "13-nodes" "National Science Foundation Network topology (NSFNET)" through "three data centers and 22 links." Table [2](#page-8-0) shows the parameters used in the simulation.

The blocking probability of the FFF technique is shown in Figure [5](#page-8-0) to be lower than that of DBWO-RF at the same load level. This is correlated with a higher efficiency of spectrum resource use and a smaller percentage of discontinuities by means of the spectrum in the link.

When comparing algorithm complexity, Figure [6](#page-8-0) illustrates that FFF has a greater complexity than DBWO-RF based on the running duration at the same level. The performance of the DBWO-RF is improved when combined with the blocking possibility and algorithm complexity.

<span id="page-8-0"></span>TABLE 2 Parameters for simulation.

| Simulation parameters                           | Values       |
|-------------------------------------------------|--------------|
| Quantity of frequency slots for each wavelength | 50           |
| A frequency slot's bandwidth                    | 12.5 GHz     |
| Quantity of wavelengths for each link           | 5            |
| Time spent in simulation                        | 10 s         |
| Range of the transmission speed                 | 100–400 Gbps |
| Computational power (per DC)                    | 5000         |
| Amount of guard-band slots                      | 2            |
| Quantity of potential paths for an S-D pair     | 3            |

![](_page_8_Figure_4.jpeg)

FIGURE 5 The blocking probability of proposed method. Source: Author.

![](_page_8_Figure_6.jpeg)

FIGURE 6 Algorithm complexity of proposed method. Source: Author.

The efficiency of our suggested DBWO-RF algorithm in utilizing spectrum resources is higher than the FFF technique, as shown in Figure [7.](#page-9-0) The improvement in DBWO-RF's resource consumption efficiency is greatest at higher load levels.

<span id="page-9-0"></span>![](_page_9_Figure_3.jpeg)

FIGURE 7 Spectrum resources utilization efficiency of the proposed method. Source: Author.

# 5 | DISCUSSION

In the discussion section of the study, the focus is on interpreting the results and providing insights into the implications of the findings. It's an opportunity to analyze the effectiveness of the proposed DBWO-RF strategy in addressing the challenges of optical network resource allocation. Key points can include a detailed examination of the experimental results, comparisons with existing approaches, and a discussion on the practical implications of the findings for telecommunications operators. Additionally, the discussion can explore potential limitations of the study and suggest areas for future research. Overall, the discussion section serves to contextualize the results within the broader field of optical networking and highlight the significance of the research contributions in advancing resource scheduling techniques. The study highlights the implication of the future DBWO-RF advance by contextualizing it within existing research. However, the novelty of the DBWO-RF approach lies in its incorporation with SDON, FCM cluster for traffic investigation, and FFF algorithm for reducing blocking risk. These unique elements contribute to its efficiency in optimizing visual network effectiveness, as demonstrated by experimental results. The limitations of FFF include its restricted ability to work with non-linear systems, the potential for overfitting to certain data sets, and the challenge of accurately modeling complex functions. Furthermore, it could have trouble expressing complex associations between disconnected mechanism, which would reduce its generalizability and analytical efficiency. By analyzing the drawbacks of existing approaches, our proposed DBWO-RF technique achieves better results.

# 6 | CONCLUSION

The study proposed an inclusive reevaluation of optical networking organization strategy to attend to the rising need for robust and efficient communication networks. Resource development in optical networks was revolutionized by the DBWO-RF method, which integrates ML. DBWO-RF that was included with the SDON controller uses the FFF technique to minimize blocking risk and FCM for traffic analysis. Resources are allocated effectively depending on channel quality with regard to the flexibility of the approach in accommodating different TF clusters and the use of several modulation schemes. When compared to various approaches at different load levels, analysis shows its superiority in minimizing spectrum resource use, guaranteeing an ideal degree of complexity, and lowering blocking risk. According to the findings, the FFF algorithm was utilized to provide services that need more spectrum resources since it has reduced blocking probabilities. DBWO-RF can achieve a 95.3% classification accuracy for channel quality, demonstrating its ability to facilitate elastic transport for a wide range of services in ODCNs. With a spectrum utilization effectiveness of 84.1%, DBWO-RF was able to accomplish a high spectrum utilization of resources and an elastic transport mechanism. The main drawback of the study was focused primarily on high TF, which can limit its broader applicability. The limitation of this research is its focus primarily on high traffic flow rates, potentially limiting the applicability of the <span id="page-10-0"></span>proposed DBWO-RF approach to broader traffic conditions. Future research could expand the scope to address various traffic patterns and optimize resource allocation for a broader range of scenarios, enhancing the scalability and versatility of the proposed approach. It was recommended that future research broaden its scope by tackling different traffic conditions.

# ETHICS APPROVAL AND CONSENT TO PARTICIPATE

No participation of humans takes place in this implementation process.

### HUMAN AND ANIMAL RIGHTS

No violation of human and animal rights is involved.

# AUTHOR CONTRIBUTIONS

All authors contributed equally to this work.

### ACKNOWLEDGMENTS

There is no acknowledgement involved in this work.

### CONFLICT OF INTEREST STATEMENT

Conflict of interest is not applicable in this work.

### DATA AVAILABILITY STATEMENT

Data sharing is not applicable to this article as no datasets were generated or analyzed during the current study.

### ORCID

Neetha Kala S.S. <https://orcid.org/0009-0009-7238-5441>

# REFERENCES

- 1. Rubel K. Increasing the efficiency and effectiveness of inventory management by optimizing supply chain through enterprise resource planning technology. Efflat Multidiscip J. 2021;5(2):1739-1756.
- 2. Lin YK, Chong CS. Fast GA-based project scheduling for computing resources allocation in a cloud manufacturing system. J Intell Manuf. 2017;28(5):1189-1201. doi[:10.1007/s10845-015-1074-0](info:doi/10.1007/s10845-015-1074-0)
- 3. Sun J, Zhang Z. A post-disaster resource allocation framework for improving resilience of interdependent infrastructure networks. Transp Res Part D: Transp Environ. 2020;85:102455. doi:[10.1016/j.trd.2020.102455](info:doi/10.1016/j.trd.2020.102455)
- 4. Jihad, N.J., AbdAlmuhsan, M.A.: Future trends in optical wireless communications systems (2023). [10.47577/technium.v13i.9474](info:doi/10.47577/technium.v13i.9474).
- 5. Moharrami M, Fallahpour A, Beyranvand H, Salehi JA. Resource allocation and multicast routing in elastic optical networks. IEEE Trans Commun. 2017;65(5):2101-2113. doi:[10.1109/TCOMM.2017.2667664](info:doi/10.1109/TCOMM.2017.2667664)
- 6. Sun X, Zhao J, Ma X, Li Q. Enhancing the user experience in vehicular edge computing networks: an adaptive resource allocation approach. IEEE Access. 2019;7:161074-161087. doi:[10.1109/ACCESS.2019.2950898](info:doi/10.1109/ACCESS.2019.2950898)
- 7. Htay ZMM. A High-Speed Reconfigurable Free Space Optical Communication System Utilizing Software Defined Radio Environment. Doctoral dissertation, University of Northumbria at Newcastle (United Kingdom). 2023.
- 8. Yu A, Yang H, Xu T, et al. Long-term traffic scheduling based on stacked bidirectional recurrent neural networks in inter-datacenter optical networks. IEEE Access. 2019;7:182296-182308. doi:[10.1109/ACCESS.2019.2959303](info:doi/10.1109/ACCESS.2019.2959303)
- 9. Saif MAN, Niranjan SK, Al-Ariki HDE. Efficient autonomic and elastic resource management techniques in cloud environment: taxonomy and analysis. Wirel Netw. 2021;27(4):2829-2866. doi:[10.1007/s11276-021-02614-1](info:doi/10.1007/s11276-021-02614-1)
- 10. Kokkinos P, Soumplis P, Varvarigos EA. Pattern-driven resource allocation in optical networks. IEEE Trans Netw Serv Manag. 2019; 16(2):489-504. doi[:10.1109/TNSM.2019.2910321](info:doi/10.1109/TNSM.2019.2910321)
- 11. Winzer PJ, Neilson DT, Chraplyvy AR. Fiber-optic transmission and networking: the previous 20 and the next 20 years. Opt Express. 2018;26(18):24190-24239. doi:[10.1364/OE.26.024190](info:doi/10.1364/OE.26.024190)
- 12. Tzanakaki A, Anastasopoulos MP, Simeonidou D. Converged optical, wireless, and data center network infrastructures for 5G services. J Opt Commun Netw. 2019;11(2):A111-A122. doi:[10.1364/JOCN.11.00A111](info:doi/10.1364/JOCN.11.00A111)
- 13. Peng Y, Bao Y, Chen Y, Wu C, Guo C. Optimus: an efficient dynamic resource scheduler for deep learning clusters. In: Proceedings of the Thirteenth EuroSys Conference. Association for Computing Machinery; 2018:1-14. doi:[10.1145/3190508.3190517](info:doi/10.1145/3190508.3190517)
- 14. Cui W, Shen K, Yu W. Spatial deep learning for wireless scheduling. IEEE J Sel Areas Commun. 2019;37(6):1248-1261. doi[:10.1109/](info:doi/10.1109/JSAC.2019.2904352) [JSAC.2019.2904352](info:doi/10.1109/JSAC.2019.2904352)
- 15. Liu M, Song T, Hu J, Yang J, Gui G. Deep learning-inspired message passing algorithm for efficient resource allocation in cognitive radio networks. IEEE Trans Veh Technol. 2018b;68(1):641-653. doi:[10.1109/TVT.2018.2883669](info:doi/10.1109/TVT.2018.2883669)

- <span id="page-11-0"></span>16. Challita U, Dong L, Saad W. Proactive resource management for LTE in unlicensed spectrum: a deep learning perspective. IEEE Trans Wirel Commun. 2018;17(7):4674-4689. doi:[10.1109/TWC.2018.2829773](info:doi/10.1109/TWC.2018.2829773)
- 17. Li B, Lu W, Liu S, Zhu Z. Deep-learning-assisted network orchestration for on-demand and cost-effective vNF service chaining in inter-DC elastic optical networks. J Opt Commun Netw. 2018;10(10):D29-D41. doi[:10.1364/JOCN.10.000D29](info:doi/10.1364/JOCN.10.000D29)
- 18. Wang JB, Wang J, Wu Y, et al. A machine learning framework for resource allocation assisted by cloud computing. IEEE Netw. 2018; 32(2):144-151. doi[:10.1109/MNET.2018.1700293](info:doi/10.1109/MNET.2018.1700293)
- 19. Jiang F, Wang K, Dong L, Pan C, Xu W, Yang K. Deep-learning-based joint resource scheduling algorithms for hybrid MEC networks. IEEE Internet Things J. 2019;7(7):6252-6265. doi:[10.1109/JIOT.2019.2954503](info:doi/10.1109/JIOT.2019.2954503)
- 20. Zhuge Q, Zeng X, Lun H, et al. Application of machine learning in fiber nonlinearity modeling and monitoring for elastic optical networks. J Lightwave Technol. 2019;37(13):3055-3063. doi:[10.1109/JLT.2019.2910143](info:doi/10.1109/JLT.2019.2910143)
- 21. Yan M, Feng G, Zhou J, Sun Y, Liang YC. Intelligent resource scheduling for 5G radio access network slicing. IEEE Trans Veh Technol. 2019;68(8):7691-7703. doi[:10.1109/TVT.2019.2922668](info:doi/10.1109/TVT.2019.2922668)
- 22. Martin A, Egaña J, Florez J, et al. Network resource allocation system for QoE-aware delivery of media services in 5G networks. - IEEE Trans Broadcast. 2018;64(2):561-574. doi:[10.1109/TBC.2018.2828608](info:doi/10.1109/TBC.2018.2828608)
- 23. Qiu C, Yao H, Yu FR, Xu F, Zhao C. Deep Q-learning aided networking, caching, and computing resources allocation in softwaredefined satellite-terrestrial networks. IEEE Trans Veh Technol. 2019;68(6):5871-5883. doi:[10.1109/TVT.2019.2907682](info:doi/10.1109/TVT.2019.2907682)
- 24. Khan FN, Fan Q, Lu C, Lau APT. An optical communication's perspective on machine learning and its applications. J Lightwave Technol. 2019;37(2):493-516. doi[:10.1109/JLT.2019.2897313](info:doi/10.1109/JLT.2019.2897313)
- 25. Zappone A, Di Renzo M, Debbah M, Lam TT, Qian X. Model-aided wireless artificial intelligence: embedding expert knowledge in deep neural networks for wireless system optimization. IEEE Veh Technol Mag. 2019;14(3):60-69. doi:[10.1109/MVT.2019.2921627](info:doi/10.1109/MVT.2019.2921627)
- 26. Singh SK, Jukan A. Machine-learning-based prediction for resource (re)allocation in optical data center networks. J Opt Commun Netw. 2018;10(10):D12-D28. doi[:10.1364/JOCN.10.000D12](info:doi/10.1364/JOCN.10.000D12)
- 27. Liu M, Song T, Gui G. Deep cognitive perspective: resource allocation for NOMA-based heterogeneous IoT with imperfect SICS. IEEE Internet Things J. 2018a;6(2):2885-2894. doi[:10.1109/JIOT.2018.2876152](info:doi/10.1109/JIOT.2018.2876152)
- 28. Li X, Wan J, Dai HN, Imran M, Xia M, Celesti A. A hybrid computing solution and resource scheduling strategy for edge computing in smart manufacturing. IEEE Trans Industr Inform. 2019;15(7):4225-4234. doi:[10.1109/TII.2019.2899679](info:doi/10.1109/TII.2019.2899679)
- 29. Tran TX, Pompili D. Joint task offloading and resource allocation for multi-server mobile-edge computing networks. IEEE Trans Veh Technol. 2018;68(1):856-868. doi[:10.1109/TVT.2018.2881191](info:doi/10.1109/TVT.2018.2881191)
- 30. Yang G, Yuan D, Liang YC, Zhang R, Leung VC. Optimal resource allocation in full-duplex ambient backscatter communication networks for wireless-powered IoT. IEEE Internet Things J. 2018;6(2):2612-2625. doi:[10.1109/JIOT.2018.2872515](info:doi/10.1109/JIOT.2018.2872515)
- 31. Rahimi P, Chrysostomou C, Pervaiz H, Vassiliou V, Ni Q. Joint radio resource allocation and beamforming optimization for industrial internet of things in software-defined networking-based virtual fog-radio access network 5G-and-beyond wireless environments. IEEE Trans Industr Inform. 2021;18(6):4198-4209. doi:[10.1109/TII.2021.3126813](info:doi/10.1109/TII.2021.3126813)
- 32. Kalpana RVS, Lokanadham R, Amudha K, et al. Internet of things (IOT) based machine learning techniques for wind energy harvesting. Electr Power Compon Syst. 2023;1-17. doi[:10.1080/15325008.2023.2293952](info:doi/10.1080/15325008.2023.2293952)
- 33. Tsai JS, Chuang IH, Liu JJ, Kuo YH, Liao W. QoS-aware fog service orchestration for industrial Internet of Things. IEEE Trans Serv Comput. 2020;15(3):1265-1279. doi:[10.1109/TSC.2020.2978472](info:doi/10.1109/TSC.2020.2978472)
- 34. Salehnia T, Montazerolghaem A, Mirjalili S, Khayyambashi MR, Abualigah L. SDN-based optimal task scheduling method in Fog-IoT network using combination of AO and WOA. In: Handbook of Whale Optimization Algorithm. Academic Press; 2024:109-128. doi[:10.](info:doi/10.1016/B978-0-32-395365-8.00014-2) [1016/B978-0-32-395365-8.00014-2](info:doi/10.1016/B978-0-32-395365-8.00014-2)
- 35. Yuan T, da Rocha Neto W, Rothenberg CE, Obraczka K, Barakat C, Turletti T. Dynamic controller assignment in software defined internet of vehicles through multi-agent deep reinforcement learning. IEEE Trans Netw Serv Manag. 2020;18(1):585-596. doi[:10.1109/TNSM.](info:doi/10.1109/TNSM.2020.3047765) [2020.3047765](info:doi/10.1109/TNSM.2020.3047765)
- 36. Lin K, Li C, Li Y, Savaglio C, Fortino G. Distributed learning for vehicle routing decision in software defined Internet of vehicles. IEEE Trans Intell Transp Syst. 2020;22(6):3730-3741. doi:[10.1109/TITS.2020.3023958](info:doi/10.1109/TITS.2020.3023958)
- 37. Pushpavalli M, Dhanya D, Kulkarni M, et al. Enhancing electrical power demand prediction using LSTM-based deep learning models for local energy communities. Electr Power Compon Syst. 2024;1-18. doi:[10.1080/15325008.2024.2316246](info:doi/10.1080/15325008.2024.2316246)
- 38. Montazerolghaem A. Software-defined Internet of Multimedia Things: energy-efficient and load-balanced resource management. IEEE Internet Things J. 2021;9(3):2432-2442. doi[:10.1109/JIOT.2021.3095237](info:doi/10.1109/JIOT.2021.3095237)
- 39. Bagha MA, Majidzadeh K, Masdari M, Farhang Y. ELA-RCP: an energy-efficient and load balanced algorithm for reliable controller placement in software-defined networks. J Netw Comput Appl. 2024;225:103855. doi:[10.1016/j.jnca.2024.103855](info:doi/10.1016/j.jnca.2024.103855)
- 40. Gupta S, Patel N, Kumar A, et al. Intelligent resource optimization for scalable and energy-efficient heterogeneous IoT devices. Multimed Tools Appl. 2024;1-25. doi[:10.1007/s11042-024-18176-1](info:doi/10.1007/s11042-024-18176-1)

How to cite this article: S.S. NK, Jain A, Bhatt R, Sinha SK, Saraswat P, Prabhakaran. Elevating optical networks: Machine learning approach for optimal resource scheduling and performance boost. Int J Commun Syst. 2024;37(17):e5936. doi:[10.1002/dac.5936](info:doi/10.1002/dac.5936)
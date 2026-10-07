# Machine learning aided optimization for balanced resource allocations in SDM-EONs

**Shrinivas Petale\* AND Suresh Subramaniam**

Department of Electrical and Computer Engineering, The George Washington University, Washington, D.C., 20052, USA \*srpetale@gwu.edu

Received 22 November 2022; revised 28 January 2023; accepted 6 February 2023; published 13 April 2023

**A fine-grained flexible frequency grid for elastic optical transmission and space division multiplexing in conjunction with spectrally efficient modulations is an excellent solution to the coming capacity crunch. In space division multiplexed elastic optical networks (SDM-EONs), the routing, modulation, core, and spectrum assignment (RMCSA) problem is an important lightpath resource assignment problem. Intercore cross talk (XT) reduces the quality of parallel transmissions on separate cores, and the RMCSA algorithm must ensure that XT requirements are satisfied while optimizing network performance. There is an indirect trade-off between spectrum utilization and XT tolerance; while higher modulations are more spectrum efficient, they are also less tolerant of XT since they permit fewer connections on neighboring cores on the overlapping spectra. Numerous XT-aware RMCSA algorithms restrict the number of litcores, cores on which overlapping spectra are occupied, to guarantee XT constraints are met. In this paper, we present a machine learning (ML) aided threshold optimization strategy that enhances the performance of** *any* **RMCSA algorithm for any network model. We show that our strategy applied to a few algorithms from the literature improves the bandwidth blocking probability by up to three orders of magnitude. We also present the RMCSA algorithm called spectrum-wastage-avoidance-based resource allocation (SWARM), which is based on the idea of spectrum wastage due to spectrum requirements and XT constraints. We note that SWARM not only outperforms other RMCSA algorithms, but also its ML-optimized variant outperforms other ML-optimized RMCSA algorithms.** © 2023 Optica Publishing Group

https://doi.org/10.1364/JOCN.481415

### 1. INTRODUCTION

To accommodate the unceasing rise of Internet traffic [1], optical network architecture and management tools must continuously adapt and incorporate new technological developments. In particular, the new paradigm of elastic optical networks (EONs) is characterized by the adoption of coherent transmission technologies [2] (enabling higher spectral efficiency via adjustable modulations, for example) and a flexible spectrum grid [3] that partitions the optical spectrum into finegrained frequency slots to better adapt channel bandwidths to traffic demands. Multicore fiber (MCF)-based space division multiplexed EONs (SDM-EONs) allow parallel multicarrier distance adaptive transmissions on different cores of the same fiber [4,5]. However, intercore cross talk (XT) between parallel transmissions on the weakly coupled cores significantly affects the quality of transmission (QoT) of signals, leading to dropped connections and thus loss of data [6,7]. Routing, modulation, core, and spectrum assignment (RMCSA) is a fundamental SDM-EON planning problem, which entails assigning to each traffic demand a lightpath (i.e., an all-optical end-to-end circuit) linking its source node to its destination node across an appropriate spectral bandwidth. To determine the viability of an SDM-EON RMCSA solution, the QoT of each prospective lightpath must be ensured to be within bounds prior to deployment.

In SDM-EON, lightpaths are routed through cores on fiber routes utilizing contiguous and continuous frequency slices (FSs). The selected modulation decides the spectrum requirement and QoT constraints to be met during the existence of the connection in the network. The transmission reach of a modulation is the maximum distance that can be traversed using this modulation and still maintaining the QoT requirements. The core geometry decides the number of adjacent cores of each core. Thus, the XT effects on ongoing connections differ based on the selected core for assignment. On a core, there are different spectrum choices, and the occupancy of overlapping spectra on adjacent cores varies, which leads to different effects of XT. In addition, different modulations require different bandwidths for the same datarate due to their unique spectrum efficiency. Choosing a spectrally efficient modulation conserves spectrum while reducing XT tolerance and transmission reaches, and vice versa. Thus, utilizing multiple-efficient modulation types complicates the resource allocation problem. In other words, there is a clear *trade-off* between spectrum utilization and XT accumulation [8,9]. Several RMCSA approaches limit the number of adjacent litcores on overlapping spectra to comply with XT restrictions [10,11] without improving the selection of modulations and spectrum choice.

Machine learning (ML) has recently been investigated extensively for addressing complex challenges in optical networks [12]. The ML model helps discover and learn a fundamental relationship between network features and corresponding output labels, and subsequently suitable network models can be created. In this work, we offer an ML-aided optimization strategy for learning such an underlying relationship for better selection of core–modulation–spectrum to balance the trade-off between spectrum utilization and XT tolerance. Our method differs from others in that it can be used to potentially improve the performance of *any* RMCSA algorithm for *any* network model in MCF-based SDM-EONs. We have also quantified the trade-off in the form of spectrum wastage and designed an efficient algorithm based on the concept of spectrum wastage to balance the trade-off called spectrumwastage-avoidance-based resource management (SWARM). SWARM uses the concept of spectrum wastage due to the selection of a particular core–modulation pair, unlike our previous tridental resource allocation (TRA) algorithm in [8,9], which selects the core–modulation–spectrum combination jointly. One dimension (i.e., spectrum) is not used in SWARM, thereby making it faster. The objective is to improve resource utilization while satisfying XT constraints in an MCFbased SDM-EON to minimize bandwidth blocking. One way is to develop a sophisticated and complex algorithm to get highly efficient resource allocation, e.g., TRA. Another way is to optimize the static parameter(s) exhaustively to improve the performance of existing RMCSAs, e.g., precise XT (P-XT) [13], TRA, etc. A compromise between the two is to develop a statistically complex and computationally less expensive RMCSA. SWARM falls into this category, and we show that it performs better than other RMCSA algorithms.

In our previous work [14], we presented an ML-based approach to choose litcore thresholds (i.e., the maximum number of adjacent cores allowed to be occupied) by learning the underlying and unquantifiable relationship between a set of litcore thresholds and bandwidth blocking probability (BBP). We achieve the balance in the trade-off between spectrum utilization and XT accumulations with the help of predicted litcore thresholds. A preliminary version of this work was presented in [14]. This paper makes the following additional contributions: (i) an ML-aided litcore threshold selection approach with enhanced data processing; (ii) a detailed comparison among the training–tuning–testing phase, scalability, and effectiveness to ease the selection of a specific ML model as per use; (iii) a solution to deal with the scarcity of training data and time required to generate training data; (iv) a comparative analysis of different ML models; (v) analysis presented for multi-MCF links for different multicore geometries; (vi) detailed explanation of the effect of thresholds on spectrum utilization and XT accumulations; (vii) a novel algorithm, SWARM, which balances the trade-off between spectrum utilization and XT accumulations, which demonstrates superior performance over other algorithms with and without MLaided optimization; and (viii) a detailed analysis of the BBP in terms of the utilization of modulations and types of blocking.

The paper is organized as follows. A brief survey of recent literature on the topic is presented in Section 2. The network model is introduced in Section 3. The ML-aided approach and detailed analysis are presented in Section 4. Important concepts useful to understand the proposed work are presented in Section 5. The SWARM algorithm is introduced in Section 6. Section 7 presents extensive simulation results, and the last section concludes the work.

#### 2. RELATED WORK

The RMCSA problem includes the selection of resources for incoming connection requests, including route, modulation, core, and spectrum. Due to cheaper computing, there has been a recent emphasis on the development of complex algorithms [6,15]. Apart from single-objective routing, core, and spectrum assignment algorithms, the joint selection of core and spectrum to decrease XT and fragmentation for on-demand requirements is investigated [16,17]. Multipath routing, as opposed to shortest path routing, can prevent the accumulation of XT on a given connection. By proposing other routes for assignment in a congested network, multipath routing also helps reduce the bandwidth blocking [13].

Variants such as looking for a lower spectrum instead of lower core index [13,18] and considering maximum value, as opposed to average value, of XT experienced by each FS in a desired collection of FSs [13] have also been investigated. Resource allocation approaches that group the weakly coupled cores in MCFs are presented in [19,20]. By selecting the physical parameters and assumptions, bandwidth blocking is shown to be reduced [20,21]. Various XT-based algorithmic techniques to decrease the BBP are investigated in [10], where an XT-aware strategy with the dynamic computation of XT levels is employed to allocate spectrum instead of worst-case estimations. The XT restrictions may be utilized to model the impact of XT on signal transmission as described in [10]. It is essential to select a significant XT threshold based on realistic standards [22], which can be achieved by selecting a substantial value for the power coupling coefficient and span length [7,11].

ML techniques have been applied recently for particular challenges such as QoT estimation when data are scarce [12], complicated but efficient regression approaches [23], data manipulation [24], etc. ML has not been thoroughly studied for a large array of optical networking problems [6,12,25,26]. Static planning may be performed using supervised learning to facilitate dynamic provisioning for subproblems of larger problems [25,27].

Supervised learning algorithms require a very large amount of training samples, in the range of hundreds or even thousands of observations of lightpaths [28] to develop an appropriate prediction model. Techniques such as observations and extraction of network data from network devices are done using telemetry equipment [29]. In actual installations, however, the gathering of training samples is sometimes hampered by practical constraints such as the unavailability of optical monitors in some network nodes or a dearth of monitorable lightpaths in networks in their early deployment phases. Data scarcity has always been an obstacle in training the ML model. In addition, quality of data over quantity helps better learning. Data scarcity and its expense have been addressed in studies such as [30,31]. One of the approaches to address the issues is to enlarge the dataset by adding simulated data and then labeling them based on previous observations or by selectively picking the source of data [32]. It can be done via active learning [33] or transfer learning [34] such as widely accepted domain adaptation [35] with data being extracted from different sources.

In this paper, we use model tuning as a tool to deal with scarcity of data. We also rely on data processing to further improve the data-generation phase and training process. We discuss how the quality of data can be maintained over quantity and how it helps learning in Section 4. We deal with data scarcity by using the best hyperparameters to enhance the training process. We use the concept of core-grouping in weakly coupled MCFs and design the concept of spectrum wastage as a means to relate spectrum utilization and XT accumulations. We then propose our resource allocation algorithm (SWARM) based on these concepts and demonstrate that it is better at minimizing bandwidth blocking than other RMCSA algorithms with or without ML-aided threshold optimization.

#### 3. NETWORK MODEL

We assume the SDM-EON is equipped with coherent transceivers (TRXs) and operates on a flexible grid with a 12.5 GHz grid granularity, denoted as  $\delta$ . TRXs offer adjustable bit rates and support multiple modulations [13]. They operate at a constant baud rate of 28 GBaud, and each sends and receives optical signals on a carrier whose total bandwidth occupies three FSs (37.5 GHz), denoted as  $N_t$ . If the desired bit rate exceeds the capacity of a single TRX with a certain modulation, the request is formed by several optical carriers inside a single superchannel (SCh). A 12.5 GHz guard band separates each SCh from its adjacent channels. The nodes are linked using optical connections based on MCF technology. Each fiber link is composed of MCFs with identical core geometries in both directions. We assume multiple MCFs on a single link uniformly distributed in the range [1, F], where F is the highest number of fibers a link can hold in a single direction. As multiple links on the same path between a source-destination pair can have multiple fibers, fiber switching is allowed while maintaining the core continuity constraint along with a spectrum continuity and contiguity constraint.

We consider 3-core, 7-core, and 13-core geometries. We assume that the effect of XT affects just neighboring/neighbor cores and has no influence on cores that are not adjacent. For example, each core of a three-core fiber has two neighboring cores as shown in Fig. 4(a) below. Likewise, the outer cores of a seven-core fiber are surrounded by three adjacent cores, while the center core is encircled by six adjacent cores as shown in Fig. 4(b) below. In addition, spatial continuity is ensured, which means that the same core is assigned to each lightpath. Lightpath requests arrive dynamically at a Poisson rate with an exponentially distributed mean holding time of one (arbitrary units), whereas lightpath datarates are evenly distributed within a predefined range.

The mean XT experienced in a core of an MCF, represented as  $XT_{\mu}$  and shown in Eq. (1), may be calculated using an

analytical model using coupled-power theory [13,36].  $\gamma$ , h, and L are the number of litcores, a design parameter representing the increase in XT per unit of fiber length, and route length, respectively.  $\gamma$  is the number of adjacent cores on which overlapping spectra are occupied by ongoing (parallel) transmissions; i.e., the overlapping spectra on these adjacent cores are occupied. The set of modulations is denoted as D. Polarization multiplexed-quadrature phase shift keying (PM-QPSK), polarization multiplexed-8 quadrature amplitude modulation (PM-8QAM), PM-16QAM, PM-32QAM, and PM-64QAM (|D| = 5) are considered; these can be used without the requirement for multiple-input and multiple-output (MIMO) digital signal processing (DSP) if  $XT_{\mu} = -40 \text{ dB}$ and the bit error rate (BER) is less than  $3.8 \times 10^{-3}$ . Moreover, the XT thresholds for MIMO DSP-free transmission at BER =  $3.8 \times 10^{-3}$  were published in [37]. For example, the PM-QPSK and PM-64QAM XT thresholds are -15.6 and -28.1 dB, respectively. By using an average XT of -40 dB between neighboring cores after a single span of propagation, we can ensure that the transmission is MIMO DSP-free for all modulations and litcore counts. Numbers of 1, 2, 3, 4, 5, and 6 lit neighbor cores represent XT of -40, -37, -35.2, -34. -33, and  $-32.2 \, dB$  after a single span of propagation, respectively. The term litcore-threshold alternately means an XT threshold in dB to make sure the selection of modulation is made by always maintaining the QoT constraint. The maximum transmission reach ( $L_{max}$ ) can be calculated using Eq. (2), where  $L_{\text{span}}$ , EVM<sub>0</sub>, and EVM<sub>span</sub> represent the span length, error-vector magnitude (EVM) to achieve the target BER, and EVM of the span, respectively [38]. As  $\gamma$  increases from zero to  $(\mathfrak{C}-1)$ , where  $\mathfrak{C}$  is the maximum number of cores in a cluster of cores adjacent to each other, the average XT contribution per span goes from -40 dB(0.0001 in linear scale) to -32.28 dB for a -40 dB average XT per span (0.000592 in linear scale). The EVM-obtained transmission reach guarantees a BER of  $3.8 \times 10^{-3}$  for h of  $3.15 \times 10^{-9}$  and a span length of 50 km. The associated transmission reach model is shown in [38]:

$$XT_{\mu} = \frac{\gamma - \gamma \exp(-(\gamma + 1)hl)}{1 + \gamma \exp(-(\gamma + 1)hl)},$$
 (1)

$$L_{\text{max}} = L_{\text{span}} \left| \frac{\text{EVM}_0^2}{\text{EVM}_{\text{span}}^2} \right|.$$
 (2)

The transmission reach is dependent upon modulation and  $\gamma$ . A higher modulation, which is more spectrally efficient but more XT sensitive, has a lower transmission reach than a lower modulation for the same  $\gamma$ . Moreover, for a given modulation, the transmission reach decreases as  $\gamma$  increases, as each increase in  $\gamma$  increases the accumulation of XT. The modulation selection for a lightpath may be regulated by setting a maximum  $\gamma$  value for each dth modulation, denoted as  $\gamma^d_{\max}$ , which acts as the modulation selection threshold. In other words,  $\gamma^d_{\max}$  represents the maximum number of adjacent cores allowed to be occupied on overlapping spectra. This implies that if the dth modulation is selected, no more than  $\gamma^d_{\max}$  ( $0 \le \gamma^d_{\max} \le \mathfrak{C} - 1$ ) are allowed to be occupied by other existing/future connections on overlapping spectra. This guarantees that the XT will be

capped to preserve the QoT. Using a larger  $\gamma_{\max}^d$  permits more adjacent cores on overlapping spectra to be used by other connections; nevertheless, this results in a lower transmission reach because of the increased possible accumulated XT. Thus, the set  $\{\gamma_{\max}^d: d=1,\ldots,|D|\}$  [also called the *set of thresholds (ST)*] may be used to control the selection of modulations. For an incoming connection request, a resource allocation algorithm would select the modulation with the highest transmission reach that exceeds the connection's path length; here, the transmission reach is dependent on the ST.

#### 4. MACHINE-LEARNING-AIDED OPTIMIZATION

We now describe a novel method for identifying the optimal set of litcore thresholds using ML. This method may be implemented by any RMCSA algorithm that satisfies XT requirements with litcore thresholds. This section discusses the ML model's requirements and its operating principle. Recall that D represents the set of modulations, and  $\gamma_{\max}^d$  represents the litcore threshold for the dth modulation. The initial stage is to gather samples of STs, followed by ML model training. The optimal value of  $\gamma_{\max}^d$  is represented by  $\gamma_*^d$ . Figure 1 illustrates and describes the stages in ML-aided threshold optimization to obtain  $\gamma_*^d$  for all modulations using ML.

First, the plan of action is determined by formulating the problem for the given network model and key performance indicator(s) during the Problem Specification stage. The Data Generation and Storage stage is then used to generate the training data as described below.

#### A. Data Generation and Storage

This stage consists of four blocks. The ST generator block generates a few samples of STs randomly. The network simulator block then generates the corresponding BBP through simulation for the given RMCSA algorithm. To create a single value of the BBP from an ST, it is necessary to simulate dynamic network processes, which include the selection of modulations only when the path length is lower than or equal to the transmission reach corresponding to the litcore threshold, also defined in Definition II.1 in [14]. Because modeling performance for all potential STs would need a prohibitive amount of time, we let the ML model discover the relationship between the ST and the BBP and choose the ideal ST from a limited set of STs. Therefore, several hundred ST samples are generated, and the corresponding BBP values are obtained by simulation. These STs are then input to the ML model for training and

thereafter predicting the BBP for any ST. Training and prediction durations for the ML model are low compared to the overall time necessary to obtain the BBP for every ST through simulation. Moreover, the ML model is easily modifiable by adjusting the hyperparameters, which boosts the adaptability of the learning procedure. For exact predictions, the ML model is tuned and calibrated using the difference between expected and actual BBP values for STs with known BBPs. The ith ST and corresponding BBP are denoted as  $S_i^{\gamma}$  ( $|S_i^{\gamma}| = |D|$ ) and  $B_i$ , respectively. Each ST is utilized to construct the filtered transmission reach model, which is then used to pick the modulation from candidate modulations as per the selection pattern of the given RMCSA. Here, a filtered transmission reach model is the model with the highest transmission reach per modulation based on the litcore threshold of the modulation. The given RMCSA algorithm is applied to the selection of route, modulation, core, and spectrum.

It is unlikely that the optimal ST is in the small collection of randomly chosen STs used for training. Therefore, the load for generation of training data is chosen to be larger than normal so that the BBP values are considerably higher than desired ( $\approx 10^{-1}$ ). This helps the ML model to differentiate between distinct STs (as lower loads may give a BBP of zero for several STs).

#### 1. Data Processing and Storage

The availability of information-rich and diverse training data plays an extremely important role in training an ML model. The presence of repeated and non-diverse data increases bias in decision-making. We have observed that when one of the litcore thresholds is changed by one, the effect over the BBP is lowest or negligible. Such samples are necessary in limited quantity but if present in large numbers are redundant and shown to be detrimental due to high bias. Thus, we have used a window  $\tau$  in the data analyzer block such that the samples in the range of  $\pm \tau$  of the label of already selected samples are used up to a limited amount for training the ML model. We store the selected thresholds and corresponding BBPs in a database in a desired format for training.

#### 2. Data Analysis

To show the relationship between STs and the BBP, we generate the dataset for an XT-aware first-fit (xtFF) algorithm for the generic German (DT) topology and European (EURO) topology, shown in [9], for C = 3 using the network model

![](_page_3_Figure_15.jpeg)

**Fig. 1.** Machine learning approach for selection of optimal ST.

![](_page_4_Figure_3.jpeg)

**Fig. 2.** Comparison of various sets of thresholds and the experimental BBP (*B*) to show the change in the BBP with respect to changing thresholds.

given in Section 3 for only 10k connection requests after the network is warmed up with 1k connections. In Fig. 2, we show the variation of the BBP corresponding to the STs, where  $S_0^{\gamma}$ ,  $S_{+1}^{\gamma}$ ,  $S_{\min_1}^{\gamma}$ ,  $S_{\min_2}^{\gamma}$ ,  $S_{\min_3}^{\gamma}$ , and  $S_{\epsilon}^{\gamma}$  denote STs when all thresholds are set to zero, the threshold for the lowest modulation is set to one and the rest to zero, thresholds corresponding to the lowest BBP, thresholds corresponding to the second lowest BBP, thresholds corresponding to the third lowest BBP, and thresholds set to the highest possible threshold, respectively. There is always no change in BBP between  $S_0^{\gamma}$  and  $S_{+1}^{\gamma}$  (and for a few samples), and the BBP corresponding to  $S_{\epsilon}^{\gamma}$  is always lower than or equal to  $S_0^{\gamma}$ . There are many STs that give the lowest BBP, and these are usually not the extreme cases of  $S_0^{\gamma}$  and  $S_{\epsilon}^{\gamma}$ . Once the ML model learns the relationship between the ST and the BBP, its task is to find  $S_{\min_1}^{\gamma}$ , ideally.

#### **B.** Machine Learning Platform

We tested various ML models for each scenario and now present the detailed analysis over the selection of the ML model. The search for the optimal threshold boils down to an approximation problem where we approximate the relationship between STs and BBPs. As can be seen from Fig. 2, the relationship between STs and BBPs is partially linear and nonlinear. Thus, we tested different ML models and show the comparison among their performances in Fig. 3. The analyzed ML models are untuned deep neural network (uDNN), tuned DNN, k-nearest neighbors (KNN) algorithm, linear regression (LIN), lasso regression (LAS), and support vector regression (SVR) [30]. First, we explain model tuning and then compare the ML models to choose the best ML model for our case.

#### 1. Model Tuning

The ML model is susceptible to overfitting during the training phase whereby it performs well with training (seen) data but worse with the testing (unseen) data. Tuning helps avoid overfitting and underfitting. In addition, the tuned ML models are observed to extract the exact relationship between STs and BBPs from the same available training data. We use the two-step method [14], wherein we first divide a portion of the training dataset into the validation dataset to track validation loss, and second, we search the hyperparameters for the ML model. In overfitting, the losses decrease very fast with each epoch of training. Early stopping can be used to prevent that, and callbacks can be used to avoid overfitting the model. The patience level is set where if the model is not getting better,

![](_page_4_Figure_10.jpeg)

**Fig. 3.** Comparison of ML models in terms of (a) RMSE and (b) BBP. Comparison of experimental and predicted BBPs for (c) untuned DNN and (d) tuned DNN.

the training stops even when training epochs remain. This saves time and has a lower memory requirement. In DNN, we implement callbacks that cause early termination of the learning process if the DNN's performance does not improve.

Hyperparameter tuning is to find the set of hyperparameters for which the predictions are accurate. The sets of hyperparameters and corresponding errors form a multi-dimensional polytope. The set with minimum error, i.e., minima of the polytope, is desired. However, the search-space of sets of hyperparameters increases exponentially with choices per hyperparameter. Therefore, we use more choices for the most sensitive hyperparameters, e.g., learning rate in DNN, and use a small number of choices for the least sensitive ones, e.g., number of hidden layers, and then find the minima.

#### 2. Comparison of Machine Learning Models

We now present the comparison of the better performing ML models. All the models are tuned except uDNN, which shares the structure with DNN. The ML models are trained on a portion of the training data described in Section 4.A for the DT topology.

As shown in Fig. 3(a), the root mean squared error (RMSE) is the least for DNN. We plot the experimental values of the BBP when the STs are set to zero  $(B^0)$ , to max values  $(B^e)$  and to optimal values  $(B^*)$ , and their corresponding predicted BBPs denoted as  $\hat{B}^0$ ,  $\hat{B}^e$ , and  $\hat{B}^*$ , respectively, in Fig. 3(b). The predicted BBPs are closer to the experimental values in the cases of DNN and uDNN as compared to other models. They are also able to get the optimal STs closer to experimental minima. We also compare the experimental BBP (B) and predicted BBP  $(\hat{B})$  of the trained model for a portion of the STs by uDNN and DNN in Figs. 3(c) and 3(d), respectively. The deviation of predicted values is lesser for DNN than uDNN.

As the training data fed to the DNN are the same, the training times are the same for all choices of topologies, types of cores, and network models. The training times of different ML models may differ based on the type of model and selected hyperparameters for the same training data. The training,

tuning, and testing times depend on the size of the data. Thus, the ML model is scalable for any topology, core geometry, or network model. However, the time required for data generation varies with the selection of topology, core geometry, and network model.

The training and testing datasets are normalized using the mean and standard deviation of the training dataset using standard-scalar [39]. The model is trained using tuned hyperparameters and processed data. In the deployment stage, the trained DNN is combined with the GridSearchCV algorithm [39] to obtain optimal STs ( $S_*^{\gamma}$ ). The ML model trains over given STs and corresponding BBPs, which can be generated for any topology, network model, or RMCSA algorithm. Consequently, the ML model functions as a *generalized model* that is compatible with any network model and RMCSA in MCF-based SDM-EON.

#### 5. DEFINITIONS AND IMPORTANT CONCEPTS

In this section, we discuss some definitions and concepts useful for understanding the proposed SWARM algorithm.

#### A. Spectrum Requirement and Slice Window

The spectrum requirement for the mth datarate  $M_m$  and dth modulation  $f_d$  with spectral efficiency  $\eta_d$  is denoted as  $\beta^{m,d}$  and calculated using

$$\beta^{m,d} = \left\lceil \frac{M_m}{\delta N_t n_d} \right\rceil * N_t.$$
 (3)

A block of spectrum slices is called a *slice window*. The size of the *n*th slice window for the *m*th datarate and *d*th modulation is denoted as  $\beta_n^{m,d}$ . Here, *n* ranges from 1 to  $S - \beta^{m,d} + 1$  (=  $(S + g_b) - (\beta^{m,d} + g_b) + 1$ ); i.e., there are different candidate slice windows for each pair of datarates and modulations. Only an *available* slice window can be assigned to a connection. The available slice window is exactly defined in Definition V.1 in [8] and Definition 6.1 in [9]. Basically, an available slice window is a spectrum slice that is free, can

accommodate the current connection based on the XT constraint of the selected modulation, and does not violate the QoT constraint of ongoing connections on overlapping spectra on adjacent cores as per their XT sensitivities.

#### **B.** Core-Groups

A core-group is a set of cores with the same number of adjacent cores. It is denoted as  $G_{\alpha}$ , where  $\alpha$  is the number of adjacent cores to the member cores of that core-group. Also,  $\alpha_c$  denotes the number of adjacent cores of the cth core. The set of  $\alpha$  values is denoted as  $\Phi$ . For example, there are four possible core-groups with  $\alpha$  equal to 2, 3, 5, and 6 in the three types of MCFs we consider. The core-groups for a three-core fiber are  $G_2 = \{1, 2, 3\}$  as shown in Fig. 4(a). The core-groups for a seven-core fiber are  $G_3 = \{1, 2, 3, 4, 5, 6\}$  and  $G_6 = \{7\}$  as shown in Fig. 4(b). The core-groups for a 13-core fiber are  $G_2 = \{1, 2, 3, 4, 5, 6\}$ ,  $G_5 = \{7, 8, 9, 10, 11, 12\}$ ,  $G_6 = \{13\}$  as shown in Fig. 4(c).

#### C. SWARM Coefficient

We first define *allowed litcores* and *spectrum wasted* and then define the SWARM coefficient using these definitions to quantify the trade-off.

**Definition 5.1 (Allowed Litcores).** On a path with length l, the allowed litcore value when the dth modulation is chosen, denoted as  $\gamma^d$ , is the number of adjacent cores, with corresponding transmission reach  $T_d^{\gamma}$ , which relates to the guarantee that the QoT is maintained, that are allowed to be occupied (lit) on overlapping spectra such that  $l \geq T_d^{\gamma}$ .

**Definition 5.2 (Spectrum Wasted).** The total amount of spectrum wasted, on a path of length l for the mth datarate, slice window of size  $\beta^{m,d}$  using the dth modulation with  $\gamma^d$  s.t.  $T_d^{\gamma} \geq l$  is selected on the cth core with  $\alpha_c$  adjacent cores, is the sum of the not-allowed-to-be-occupied overlapping spectra on adjacent cores due to the XT constraint of the selected modulation. The not-allowed-to-be-occupied overlapping spectra are the product of  $\beta^{m,d}$  and remaining adjacent cores apart from allowed litcores.

![](_page_5_Figure_18.jpeg)

**Fig. 4.** Core types and the effect of selection of modulation: (a) C = 3, (b) C = 7, (c) C = 13, and (d) C = 13. (e) Different scenarios of spectrum wastage.

The impact of XT on the QoT of optical connections is measured in terms of allowed litcores, defined in Def. 5.1. The selection of core and modulation leads to the trade-off between spectrum utilization and XT accumulation, as introduced earlier. The trade-off leads to spectrum wastage as defined in Def. 5.2. When resources are allocated to a connection request, spectra not only on the selected core but also on one or more adjacent cores may become unavailable due to XT constraints. The concept of spectrum wasted is similar to that of busy and unused frequency slots in [40]. However, the mathematical formulations and use of spectrum wasted and SWARM are different from that in [40]. In addition, we use the SWARM coefficient in a unique way. The total spectrum that becomes unavailable due to assignment to the arriving connection (sum of FSs assigned and slices wasted) is called the s SWARM coefficient. The SWARM coefficient of the nth slice window on the cth core using the dth modulation, denoted as  $\sigma_{c,n}^d$ , is given in

$$\sigma_{c,n}^{d} = \begin{cases} (\alpha - \gamma^{d} + 1)\beta^{m,d} + g_{b}, & \text{if } \alpha > \gamma^{d} \\ \beta^{m,d} + g_{b}, & \text{otherwise.} \end{cases}$$
 (4)

After the selection of resources, irrespective of spectrum wastage, i.e., values of  $\alpha$  and  $\gamma^d$ , the nth slice window on the cth core will be used. Thus, the lowest value of  $\sigma^d_{c,n}$  is  $\beta^{m,d} + g_b$ , which is represented by an addition of one in the multiplication factor when  $\alpha > \gamma^d$ . Also, as the guard band does not carry any data, it does not affect the ongoing connections on adjacent cores. Therefore, the spectrum used as a guard band is unusable only on the core to be assigned.

#### **D. Illustrative Example**

We now illustrate an example to calculate  $\sigma_{c,n}^d$  in a variety of scenarios using Fig. 4(d), Fig. 4(e), and Table 1.

Suppose a connection arrives between two nodes with a datarate of 200 Gbps (m = 5,  $M_5$ ) and the length of the shortest path connecting these two nodes is 1016 km (path 5-6-10-11 between nodes 5 and 11 in the DT topology). Let us take the example of two possible modulations: PM-16QAM (d = 3) and PM-8QAM (d = 2). Using Eq. (3) with  $\delta = 12.5$  GHz,  $N_t = 3$  FSs,  $\eta_3 = 5.92$ ,  $\eta_2 = 4.44$ , and  $g_b = 1$ ,  $\beta^{5.3} = 3$  and  $\beta^{5.2} = 6$ . Also, using the transmission reaches reported in Table 1 and Def. 5.1,  $\gamma^3 = 0$  and  $\gamma^2 = 6$ . Suppose

we have two candidate cores, 1 and 13, for assignment. The adjacent cores of core 1 are 7 and 8 ( $G_2$ ), and the adjacent cores of 13 are 7, 8, 9, 10, 11, and 12 ( $G_6$ ) as shown in Fig. 4(d), so  $\alpha_1 = 2$  and  $\alpha_{13} = 6$ . Assume that the first slice window is available for both modulations on both cores. Thus, on core 1 with PM-16QAM (d = 3),  $\alpha_1 = 2$ ,  $\gamma^3 = 0$ , and  $\beta^{5,3} = 3$ , the SWARM coefficient of the first slice window (n = 1)using Eq. (4),  $\sigma_{1,1}^3 = 10 \ (= (2 - 0 + 1) \times 3 + 1)$ , where the not-allowed-to-be-occupied overlapping spectra are six FSs  $(=(2-0)\times 3)$ , and the utilized spectrum on core 1 is four FSs (= 3 + 1). Similarly,  $\sigma_{13,1}^3 = 22$  (=  $(6 - 0 + 1) \times 3 + 1$ ),  $\sigma_{1,1}^2 = 7 \ (= 6 + 1)$ , and  $\sigma_{13,1}^2 = 7 \ (= 6 + 1)$ . Thus, the best choice is to choose d = 2 on core 1. It is observed that, for a given modulation, the SWARM coefficient for cores in a lower core-group is always less than or equal to that for cores in higher core-groups. Also, for a given modulation, the SWARM coefficient is the same for all available slice windows on all cores within a specific core-group.

## 6. SPECTRUM-WASTAGE-AVOIDANCE-BASED RESOURCE MANAGEMENT

We describe the proposed algorithm, SWARM, using the definitions in Section 5. The selection of core, modulation, and spectrum not only leads to occupation of the selected spectrum on the core under consideration, but also wastes overlapping spectra on adjacent cores when the XT constraints are restrictive. A connection request on route r with mth datarate  $M_m$  is denoted as  $\Delta(r, m)$ . The set of shortest paths (SPs) on route r is denoted as  $\mathbb{S}(r)$  and the set of corresponding path lengths  $\mathbb{L}$ . The lightpath, denoted as  $\mathcal{L}_{r,m}(k, c, \beta_n^{m,d})$ , representing the *n*th slice window of size  $\beta_n^{m,d}$ , is on core c on the kth shortest path on route r for the mth datarate. The set of modulations is denoted as D, and the set of marked modulations with unique spectrum requirements for the mth datarate is denoted as  $D^m$ [9]. For the *m*th datarate, we denote sets of resources as follows.  $V^{m,d}$  is the set of  $\beta_n^{m,d}$  for all n.  $B^{m,d}$  represents the set of all slice windows for the dth modulation on all cores and fibers.  $H^m$  represents the set of all  $B^{m,d}$  for all modulations. The state of the topology at time t is denoted as  $\mathbb{G}(\mathbb{V}, \mathbb{E})(t)$ .

The pseudocode of the SWARM algorithm is presented in Algorithm 1. The optimal lightpath for assignment, denoted

Table 1. Transmission Reaches (in km) of Modulations for Different Values of Allowable Litcore ( $\gamma$ ) for a Seven-Core MCF for an Average XT after a Single Span of Propagation of  $-40\,\mathrm{dB}$  for a 28 GBaud Transceiver (from Table 1 in [38])

| γ (Litcores) | XT per Span<br>(dB) | Modulation Formats $( D  = 5)$ |                 |                  |                  |                  |  |
|--------------|---------------------|--------------------------------|-----------------|------------------|------------------|------------------|--|
|              |                     | PM-QPSK $(d=1)$                | PM-8QAM $(d=2)$ | PM-16QAM $(d=3)$ | PM-32QAM $(d=4)$ | PM-64QAM $(d=5)$ |  |
| 0            | None                | 5200                           | 2050            | 1100             | 550              | 250              |  |
| 1            | -40.0               | 4650                           | 1850            | 1000             | 500              | 250              |  |
| 2            | -37.0               | 4200                           | 1650            | 900              | 450              | 200              |  |
| 3            | -35.2               | 3850                           | 1500            | 800              | 400              | 200              |  |
| 4            | -34.0               | 3550                           | 1400            | 750              | 400              | 150              |  |
| 5            | -33.0               | 3300                           | 1300            | 700              | 350              | 150              |  |
| 6            | -32.2               | 3050                           | 1200            | 650              | 300              | 150              |  |

#### Algorithm 1. SWARM

```
Input: \mathbb{G}(\mathbb{V}, \mathbb{E})(t), \Delta(r, m), \mathbb{S}, l_r^k \in \mathbb{L} and H^m, S
         Output: \mathcal{L}^*_{\Delta(r,m)}(k^*, c^*, \beta_n^{m,d*})
1: Initialize: \mathcal{L}^*_{\Delta(r,m)} \leftarrow \emptyset, \sigma(\mathcal{L}^*_{\Delta(r,m)}) \leftarrow \infty, k \leftarrow 1
2: while \mathcal{L}^*_{\Delta(r,m)} = \emptyset \land k \neq K do
             for all (f_d \in D^m \wedge T_d^{\gamma*} \geq l_r^k) do
                  Get litcore \gamma^d \leftarrow \gamma for which T_d^{\gamma} \geq l_r^k
4:
5:
                  while c \in G_{\alpha}, \alpha \in \Phi \wedge \mathcal{L}^*_{\Delta(r,m)} = \emptyset do
                      while (b_{c,n}^{m,d} \in B_d^m; B_d^m \in H^m) \land (n \le (S - \beta^{m,d} + 1)) \land
6:
                       \mathcal{L}^*_{\Delta(r,m)} = \emptyset do
                               Get candidate lightpath \mathcal{L}_{\Delta(r,m)} \leftarrow (k, c, \beta_n^{m,d})
7:
                               if Slice window is available as per (Definition V.1
8:
                                [8] or Definition 6.1 [9]) then
9:
                               Calculate \sigma(\mathcal{L}_{\Delta(r,m)})
                                 if \sigma(\mathcal{L}_{\Delta(r,m)}) < \sigma(\mathcal{L}^*_{\Delta(r,m)}) then
10:
                                      \sigma(\mathcal{L}^*_{\Lambda(r,m)}) \leftarrow \sigma(\mathcal{L}_{\Lambda(r,m)})
12:
                                       \mathcal{L}^*_{\Delta(r,m)} \leftarrow \mathcal{L}_{\Delta(r,m)}
13:
                                      break
                                 end if
14.
                             end if
15:
16:
                         end while
                         Update \alpha to next value in \Phi to check other cores in
17:
                         higher group
18:
                    end while
19:
               end for
20:
               if \mathcal{L}^*_{\Delta(r,m)} = \emptyset then
21:
                    k \leftarrow k + 1
22:
               end if
23: end while
```

as  $\mathcal{L}^*_{\Delta(r,m)}$ , corresponding SWARM coefficient, and shortest path index are initialized in line 1. The search continues until either the optimal lightpath is obtained or the SPs are exhausted in line 2, where K denotes the total number of SPs available on the route. In line 3, the search for the smallest SWARM coefficient for all marked modulations in  $D^m$  is executed only if the path length of the kth SP on route r,  $l_r^k$ , corresponding to the optimal threshold of the modulation,  $T_d^{\gamma}$ , is short enough to allow the use of this modulation. For RMCSAs without ML-aided optimization,  $\gamma^* = 0$ , meaning that the path length must be lower than or equal to  $T_d^0$ . The number of allowed litcores,  $\gamma^d$ , is obtained in line 4 such that the corresponding transmission reach is greater than or equal to the path length when compared with the transmission reach of higher values of  $\gamma$  to  $\gamma_d^*$ . In line 5, the cores in the lowest coregroup (with lower  $\alpha$ ) are searched from lower index to higher index. In line 6, the loop iterates through all possible slice windows in  $B_d^m$ . The candidate lightpath,  $\mathcal{L}_{\Delta(r,m)}$ , is initiated in line 7. In lines 8 and 9, the SWARM coefficient for  $\mathcal{L}_{\Delta(r,m)}$ ,  $\sigma(\mathcal{L}_{\Delta(r,m)})$ , is obtained for each available slice window. If a slice window with a lower SWARM coefficient is obtained, the

search stops, else continues in lines 10–14. If the slice window is not obtained on any of the cores in the core-group, the search is initiated for the cores in the next core-group in line 17. If the lightpath is not obtained for any of the modulations or on any of the cores on the current shortest path, then k is incremented to start the search over the next shortest path in line 21. As SWARM uses a first-fit policy in core and spectrum selection, the search in lines 5 and 6 over other options stops when the optimal lightpath is obtained for a given modulation.

#### 7. SIMULATION RESULTS

We now present simulation results comparing several RMCSA algorithms with and without ML-aided optimization for a variety of scenarios. We use two practical topologies: DT and EURO, as used in [9]. The statistical data of these topologies are given in Table 2. The spectrum of 4 THz (Bw = 4000) is considered on each link with each slice of 12.5 GHz  $(\delta = 12.5)$ , i.e., 320 FSs (S = 320). A Poisson connection arrival process with an exponentially distributed holding time of one (arbitrary time unit) is assumed. Erlang loads were chosen so that the BBP values generally range between 10<sup>-5</sup> and 10<sup>-1</sup>. A total of 100,000 requests are generated per trial (excluding 10,000 warmup requests to bring the network to steady state); 95% confidence intervals are obtained for 10 trials in each experiment. The datarates are uniformly distributed at 40-400 Gbps with granularity of 40 Gbps. We use three SPs between every source-destination pair (K = 3). A total of five modulations (|D| = 5), i.e.,  $f_1$  to  $f_5$ , are used, viz., PM-QPSK ( $\eta_1 = 2.96$ ), PM-8QAM ( $\eta_2 = 4.44$ ), PM-16QAM  $(\eta_3 = 5.92)$ , PM-32QAM  $(\eta_4 = 7.4)$ , and PM-64QAM  $(\eta_5 = 8.88)$  [38,41]. The supported bit rates for each modulation by a TRX carrier are 111, 166.5, 222, 277.5, and 333 Gbps, respectively. The transmission reach model for each modulation with the average XT between two adjacent cores after a single span of propagation of  $-40 \, dB$  with 28 GBaud TRX with the span length of 50 km is used from [38]. The number of fibers per link is either one or two, chosen with equal probability (i.e., F = 2). The ML model is trained on just 200-1000 samples. We use a DNN with three hidden layers with 16, 32, and 16 neurons in a layer, as we observed better performance of DNN for these hyperparameters for this network model similar to [14]. As we find the tuned DNN model outperforming all other models, we use that to generate final results for all network scenarios.

We compare the performance of the xtFF algorithm [10] with modulation selection (xtFM), P-XT [13], SWARM, and pSWARM, which is the SWARM algorithm with prioritized path selection (PPS), which we proposed in [9]. In PPS, the path priority is calculated offline for each shortest path on a route based on the network traffic and the paths with higher

Table 2. Percentage Path Length Distribution in Different Topologies

|          | Path Length Distribution (%) |            |             |              |              | Path Lengths (in km) |      |         |
|----------|------------------------------|------------|-------------|--------------|--------------|----------------------|------|---------|
| Topology | (0, 250]                     | (250, 550] | (550, 1100] | (1100, 2050] | (2050, 5200] | Max                  | Min  | Avg     |
| DT       | 7.07                         | 23.73      | 69.19       | 0            | 0            | 48                   | 1099 | 637.98  |
| EU       | 0.27                         | 4.72       | 12.78       | 58.89        | 23.33        | 218                  | 3309 | 1626.19 |

priority are checked first. K-shortest paths routing is used for all algorithms except pSWARM. xtFF chooses the highest modulation and the first (i.e., lowest index) available slice window for assignment. xtFM chooses the highest modulation (i.e., most spectrally efficient) for which the core and spectrum are available in first-fit fashion. P-XT does an XT-aware spectrum assignment with exhaustive search on all routes. The spectrum available on the lowest index among the ones available on all the path-core pairs is selected. All algorithms are compared for the same parameters and network models including the transmission reach. The scaled execution time of all the algorithms with respect to that of xtFF, averaged over all loads and core types, is shown in Table 3. It is interesting to see that the ML-aided variants take less time for execution because of more resource availability. In addition, SWARM takes more time for execution as compared to P-XT; however, the time of execution significantly reduces when we use PPS with SWARM, i.e., pSWARM.

The optimal thresholds for each scenario are shown in Table 4. The threshold of average XT between two adjacent cores after a single span of propagation is shown for each litcore threshold value in Table 1 [38] obtained using Eq. (1). For example, the  $S_*^{\gamma}$  calculated using ML for SWARM at C=7

Table 3. Scaled Average Execution Time over All Loads and Core Types for All Variants of RMCSA Algorithms

| RMCSA     | DT Topology | EURO Topology |  |  |
|-----------|-------------|---------------|--|--|
| xtFF      | 1.0         |               |  |  |
| xtFM      | 2.209784158 | 1.201509862   |  |  |
| P-XT [13] | 1.499590617 | 1.913999159   |  |  |
| SWARM     | 2.094551759 | 1.25007854    |  |  |
| pSWARM    | 1.224802344 | 1.065307645   |  |  |
| xtFF-ML   | 0.886255683 | 0.635475543   |  |  |
| xtFM-ML   | 1.55104838  | 0.705274764   |  |  |
| P-XT-ML   | 1.33099628  | 1.728307934   |  |  |
| SWARM-ML  | 2.079262407 | 1.064714527   |  |  |
| pSWARM-ML | 1.216111348 | 0.945922638   |  |  |

for the EURO topology is  $\{1, 2, 4, 5, 6\}$ , which converts into -40.0, -37.0, -34.0, -33.0, and -32.2 dB thresholds, respectively. The BBP is obtained for different loads for all RMCSAs with or without ML-aided optimization for C=13, C=7, and C=3 as shown in Fig. 5. RMCSAs with ML-aided optimization have the suffix "-ML." We observe that all RMCSAs with ML-aided optimization outperform their original forms. We also observe that SWARM and pSWARM

Table 4. ML-Based  $S_*^{\gamma} = \{\gamma_*^1, \gamma_*^2, \gamma_*^3, \gamma_*^4, \gamma_*^5\}$  for Various Scenarios

| RMCSA     |                     | DT Topology         |                     | EURO Topology       |                     |                     |  |
|-----------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|--|
|           | C = 3               | C = 7               | C = 13              | C = 3               | C = 7               | C = 13              |  |
| xtFF      | {2, 0, 2, 0, 2}     | {0, 0, 3, 6, 3}     | {3, 6, 5, 5, 2}     | {0, 2, 2, 1, 2}     | {5, 4, 6, 2, 0}     | {0, 5, 6, 5, 6}     |  |
| xtFM      | $\{0, 2, 1, 1, 2\}$ | $\{6, 0, 4, 6, 2\}$ | ${4, 0, 5, 2, 2}$   | $\{1, 1, 2, 1, 2\}$ | $\{6, 3, 3, 6, 4\}$ | $\{2, 4, 3, 3, 6\}$ |  |
| P-XT [13] | $\{2, 0, 0, 2, 2\}$ | $\{6, 0, 2, 0, 1\}$ | ${3, 3, 5, 6, 1}$   | $\{2, 2, 0, 1, 1\}$ | $\{2, 1, 3, 2, 1\}$ | $\{6, 0, 2, 2, 0\}$ |  |
| SWARM     | $\{0, 2, 1, 1, 2\}$ | $\{6, 6, 0, 0, 6\}$ | $\{5, 0, 0, 4, 0\}$ | $\{2, 2, 0, 2, 1\}$ | $\{1, 2, 4, 5, 6\}$ | $\{0, 0, 1, 3, 6\}$ |  |
| pSWARM    | $\{0, 0, 1, 0, 0\}$ | $\{2, 0, 0, 5, 4\}$ | $\{0, 2, 2, 2, 0\}$ | {2, 2, 2, 2, 1}     | $\{0, 0, 2, 5, 0\}$ | $\{6, 2, 0, 6, 6\}$ |  |

![](_page_8_Figure_10.jpeg)

**Fig. 5.** Variation in the BBP with respect to traffic for  $XT^{sp} = -40$  dB and all C values for (a)–(c) the DT topology and (d)–(f) the EURO topology. (a) C = 13, (b) C = 7, (c) C = 3, (d) C = 13, (e) C = 7, and (f) C = 3.

outperform all other RMCSAs with or without ML-aided optimization. SWARM-ML performs better than P-XT-ML for all cases of DT topology but not EURO topology. This happens because as SWARM depends on a litcore-based SWARM coefficient, it is affected due to longer path lengths, as shown in Table 2, which leads to selection of lower litcore values. However, ML-aided optimization helps P-XT get higher litcore thresholds for the same longer paths. The improvement in performance of P-XT with ML-aided optimization is larger than that of SWARM and pSWARM. The improvement provided by PPS in pSWARM is significant and is comparable to the performance improvement that ML-aided optimization provides to SWARM. The gains are not higher because SWARM and pSWARM judiciously select resources based on litcore values, which on the other hand is done by ML-aided optimization for the other RMCSAs. We obtain the admitted traffic at ≈1% of bandwidth blocking averaged over 10 trials for all RMCSAs. For example, in the case of the EURO topology and *C* = 7, the average admitted traffic for pSWARM-ML, SWARM-ML, P-XT-ML, xtFM-ML, xtFF-ML, pSWARM, SWARM, P-XT, xtFM, and xtFF is 12,940, 8476, 8020, 5328, 11,120, 12,156, 6984, 2120, 2668, and 2096 Gbps, respectively. It is clear that for all RMCSAs, the average admitted traffic by ML-aided versions is higher as compared to their original versions. In addition, SWARM-ML admits more traffic than the rest of the algorithms. The same comparison can be observed from Fig. 5(e) at the load of 3000 Erlangs. Similar observations are made for all scenarios.

The utilization of modulations for both ML and non-ML variants of RMCSAs for the *C* = 13 and *C* = 3 cases is shown in Fig. 6. In all scenarios, the selection of lower modulations is slightly increased [e.g., PM-64QAM in xtFF-ML in Fig. 6(a)], and the selection of higher modulations is slightly decreased [e.g., PM-8QAM in xtFF-ML in Fig. 6(a)] for the ML variant of each RMCSA. This clearly shows that with the ML-aided optimization, the trade-off between spectrum utilization and XT accumulations is balanced with proper selection of higher and lower modulations, which results in better performance. The utilization of modulations is almost the same for SWARM and pSWARM, but the corresponding BBP performance is better for pSWARM because of PPS resulting in lower spectrum blocking [e.g., SWARM and pSWARM in Fig. 7(a)]. With the proper selection of thresholds, the selection of lower modulations can be increased for more path lengths leading to better performance. Some modulations are never used because either higher modulations are used due to smaller path lengths or lower modulations are used with less XT sensitivity.

The connection is blocked if either the spectrum (slice window) is not free or the spectrum is free but not available due to QoT constraints. Thus, the blocked connections can be divided into the two categories of spectrum blocking and QoT blocking, and the corresponding probabilities are called the spectrum blocking probability (SBP) and the QoT-based blocking probability (QBP). The variation in these blocking types for *C* = 13 and *C* = 3 is shown in Fig. 7. In all cases, the ML-aided optimization helps in reducing QoT blocking because the trade-off is better balanced. In addition, QoT blocking is dominant in the EURO topology because of longer paths as shown in Table 2.

Although ML-aided optimization enhances the performance of any RMCSA by improving the selection of modulations, the performance gain is higher for RMCSAs that use first-fit policy in modulation selection, such as xtFF, xtFM, and P-XT, than those that exhaustively search all modulations, such as

![](_page_9_Figure_8.jpeg)

Fig. 6. Distribution of modulations for all RMCSAs and their ML-aided versions for (a), (b) the DT topology and (c), (d) the EURO topology. (a) *C* = 13, (b) *C* = 3, (c) *C* = 13, and (d) *C* = 3.

![](_page_9_Figure_10.jpeg)

Fig. 7. Distribution of spectrum and QoT blocking for all RMCSAs and their ML-aided versions for (a), (b) the DT topology and (c), (d) the EURO topology. (a) *C* = 13, (b) *C* = 3, (c) *C* = 13, and (d) *C* = 3.

SWARM, pSWARM, and TRA [42]. ML-aided optimization helps fill the gap between the pattern of selection of resources of an algorithm, which is in general highly sub-optimal, with a more judicious pattern of selection of resources by controlling the selection of modulations using litcore thresholds. For simpler algorithms, ML-aided optimization provides significant performance improvement. The computational complexity of SWARM is comparable to that of P-XT; however, SWARM offers better performance due to balancing the trade-off better instead of just looking for a spectrum with a low index. P-XT searches through all cores on all links on all shortest paths to find a spectrum with a low index. Instead, SWARM uses a firstfit algorithm on core-groups, then cores within the core-group, and then spectrum on the core, for all modulations. It outperforms P-XT due to more focus on balancing the trade-off using a SWARM coefficient for all modulations.

#### 8. CONCLUDING REMARKS

We studied XT-aware RMCSA algorithms for MCF-based SDM-EONs. There exists a trade-off between spectrum utilization and XT accumulation for each selection of modulation format along with the selection of a core and spectrum. In this work, we proposed an ML-aided optimization technique for the selection of optimal thresholds on the number of adjacent cores that are allowed to be occupied. We showed that this effectively controls the selection of modulations and leads to a better trade-off. Our proposed optimization is a general solution that is applicable to any RMCSA scheme for any network model. We also proposed an RMCSA algorithm called SWARM, which is based on the idea of spectrum wastage. We assessed the performance of many existing RMCSA methods and their ML-aided variants, demonstrating that the latter significantly reduce the bandwidth blocking of dynamic connection requests by up to three orders of magnitude for various combinations of topologies and types of cores. SWARM and all its variants handle the trade-off efficiently, leading to the best performance. Intriguingly, the performance of the ML-aided variant of the baseline approach with the worst performance surpasses that of some better performing algorithms that do not utilize ML to optimize the thresholds.

Funding. National Science Foundation (CNS-1813617).

### REFERENCES

- 1. Cisco, "Cisco annual Internet report (2018–2023) white paper," 2020, https://www.cisco.com/c/en/us/solutions/collateral/executiveperspectives/annual-internet-report/white-paper-c11-741490.html.
- 2. O. Gerstel, M. Jinno, A. Lord, and S. B. Yoo, "Elastic optical networking: a new dawn for the optical layer?" IEEE Commun. Mag. 50(2), s12–s20 (2012).
- 3. S. Talebi, F. Alam, I. Katib, M. Khamis, R. Salama, and G. N. Rouskas, "Spectrum management techniques for elastic optical networks: a survey," Opt. Switching Netw. 13, 34–48 (2014).
- 4. Y. Awaji, J. Sakaguchi, B. J. Puttnam, R. S. Lus, J. M. D. Mendinueta, W. Klaus, and N. Wada, "High-capacity transmission over multi-core fibers," Opt. Fiber Technol. 35, 100–107 (2017).
- 5. G. M. Saridis, D. Alexandropoulos, G. Zervas, and D. Simeonidou, "Survey and evaluation of space division multiplexing: from technologies to optical networks," IEEE Commun. Surv. Tutorials 17, 2136–2156 (2015).

- 6. M. Klinkowski, P. Lechowicz, and K. Walkowiak, "Survey of resource allocation schemes and algorithms in spectrally-spatially flexible optical networking," Opt. Switching Netw. 27, 58–78 (2018).
- 7. T. Hayashi, T. Taru, O. Shimakawa, T. Sasaki, and E. Sasaoka, "Design and fabrication of ultra-low crosstalk and low-loss multi-core fiber," Opt. Express 19, 16576–16592 (2011).
- 8. S. Petale, J. Zhao, and S. Subramaniam, "Tridental resource assignment algorithm for spectrally-spatially flexible optical networks," in IEEE International Conference on Communications (ICC) (IEEE, 2021).
- 9. S. Petale, J. Zhao, and S. Subramaniam, "TRA: an efficient dynamic resource assignment algorithm for MCF-based SS-FONs," J. Opt. Commun. Netw. 14, 511–523 (2022).
- 10. M. Yang, Y. Zhang, and Q. Wu, "Routing, spectrum, and core assignment in SDM-EONS with MCF: node-arc ILP/MILP methods and an efficient XT-aware heuristic algorithm," J. Opt. Commun. Netw. 10, 195–208 (2018).
- 11. K. Walkowiak, A. Wlodarczyk, and M. Klinkowski, "Effective worstcase crosstalk estimation for dynamic translucent SDM elastic optical networks," in IEEE International Conference on Communications (ICC) (IEEE, 2019).
- 12. F. Musumeci, C. Rottondi, A. Nag, I. Macaluso, D. Zibar, M. Ruffini, and M. Tornatore, "An overview on application of machine learning techniques in optical networks," IEEE Commun. Surv. Tutorials 21, 1383–1408 (2018).
- 13. M. Klinkowski and G. Zalewski, "Dynamic crosstalk-aware lightpath provisioning in spectrally-spatially flexible optical networks," J. Opt. Commun. Netw. 11, 213–225 (2019).
- 14. S. Petale and S. Subramaniam, "An ML approach for crosstalkaware modulation format selection in SDM-EONs," in International Conference on Optical Network Design and Modeling (ONDM) (IEEE, 2022).
- 15. Í. Brasileiro, L. Costa, and A. Drummond, "A survey on challenges of spatial division multiplexing enabled elastic optical networks," Opt. Switching Netw. 38, 100584 (2020).
- 16. S. Fujii, Y. Hirota, H. Tode, and K. Murakami, "On-demand spectrum and core allocation for reducing crosstalk in multicore fibers in elastic optical networks," J. Opt. Commun. Netw. 6, 1059–1071 (2014).
- 17. G. Savva, K. Manousakis, and G. Ellinas, "Providing confidentiality in optical networks: metaheuristic techniques for the joint network coding-routing and spectrum allocation problem," in 22nd International Conference on Transparent Optical Networks (ICTON) (IEEE, 2020).
- 18. H. Tode and Y. Hirota, "Routing, spectrum, and core and/or mode assignment on space-division multiplexing optical networks," J. Opt. Commun. Netw. 9, A99–A113 (2017).
- 19. A. Agrawal, V. Bhatia, and S. Prakash, "Core arrangement based spectrum-efficient path selection in core-continuity constrained SS-FONs," in International IFIP Conference on Optical Network Design and Modeling (Springer, 2019), pp. 570–583.
- 20. A. Agrawal and S. G. Kulkarni, "Spectrum-efficiency analysis for trench-assisted and heterogeneous-index multicore fiber networks," in IEEE International Conference on Communications (ICC) (IEEE, 2022), pp. 3022–3027.
- 21. A. Agrawal, V. Bhatia, and S. Prakash, "Towards zero-crosstalkmargin operation of spectrally-spatially flexible optical networks using heterogeneous multicore fibers," in Optical Fiber Communication Conference (Optica Publishing Group, 2020), paper W2A.23.
- 22. L. Zhang, N. Ansari, and A. Khreishah, "Anycast planning in space division multiplexing elastic optical networks with multi-core fibers," IEEE Commun. Lett. 20, 1983–1986 (2016).
- 23. M. Ibrahimi, H. Abdollahi, C. Rottondi, A. Giusti, A. Ferrari, V. Curri, and M. Tornatore, "Machine learning regression for QoT estimation of unestablished lightpaths," J. Opt. Commun. Netw. 13, B92–B101 (2021).
- 24. T. Panayiotou, G. Savva, B. Shariati, I. Tomkos, and G. Ellinas, "Machine learning for QoT estimation of unseen optical network states," in Optical Fiber Communication Conference (Optica Publishing Group, 2019), paper. Tu2E.2.

- 25. Y. Zhang, J. Xin, X. Li, and S. Huang, "Overview on routing and resource allocation based machine learning in optical networks," Opt. Fiber Technol. 60, 102355 (2020).
- 26. J. A. Gordon, A. Battou, M. P. Majurski, D. Kilper, U. Celine, M. Tonatore, J. Pedro, J. Simsarian, J. Westdorp, and D. Zibar, Summary: Workshop on Machine Learning for Optical Communication Systems (2020).
- 27. R. J. Pandya, "Machine learning-oriented resource allocation in C + L + S bands extended SDM–EONs," IET Commun. 14, 1957–1967 (2020).
- 28. C. Rottondi, L. Barletta, A. Giusti, and M. Tornatore, "Machinelearning method for quality of transmission prediction of unestablished lightpaths," J. Opt. Commun. Netw. 10, A286–A297 (2018).
- 29. K. Christodoulopoulos, P. Kokkinos, A. Di Giglio, A. Pagano, N. Argyris, C. Spatharakis, S. Dris, H. Avramopoulos, J.-C. Antona, C. Delezoide, P. Jennevé, J. Pesic, Y. Pointurier, N. Sambo, F. Cugini, P. Castoldi, G. Bernini, G. Carrozzo, and E. Varvarigos, "ORCHESTRA—Optical performance monitoring enabling flexible networking," in 17th International Conference on Transparent Optical Networks (ICTON) (IEEE, 2015).
- 30. F. Musumeci, C. Rottondi, G. Corani, S. Shahkarami, F. Cugini, and M. Tornatore, "A tutorial on machine learning for failure management in optical networks," J. Lightwave Technol. 37, 4125–4139 (2019).
- 31. N. Di Cicco, M. Ibrahimi, C. Rottondi, and M. Tornatore, "Calibrated probabilistic QoT regression for unestablished lightpaths in optical networks," in International Balkan Conference on Communications and Networking (BalkanCom) (IEEE, 2022), pp. 21–25.
- 32. L. Velasco, B. Shariati, F. Boitier, P. Layec, and M. Ruiz, "Learning life cycle to speed up autonomic optical transmission and networking adoption," J. Opt. Commun. Netw. 11, 226–237 (2019).
- 33. D. Azzimonti, C. Rottondi, and M. Tornatore, "Reducing probes for quality of transmission estimation in optical networks with active learning," J. Opt. Commun. Netw. 12, A38–A48 (2020).

- 34. J. Yu, W. Mo, Y.-K. Huang, E. Ip, and D. C. Kilper, "Model transfer of QoT prediction in optical networks based on artificial neural networks," J. Opt. Commun. Netw. 11, C48–C57 (2019).
- 35. W. M. Kouw and M. Loog, "An introduction to domain adaptation and transfer learning," arXiv, arXiv:1812.11806 (2018).
- 36. M. Klinkowski, P. Ksieniewicz, M. Jaworski, G. Zalewski, and K. Walkowiak, "Machine learning assisted optimization of dynamic crosstalk-aware spectrally-spatially flexible optical networks," J. Lightwave Technol. 38, 1625–1635 (2020).
- 37. B. Puttnam, R. Luis, T. Eriksson, W. Klaus, J.-M. D. Mendinueta, Y. Awaji, and N. Wada, "Impact of intercore crosstalk on the transmission distance of QAM formats in multicore fibers," IEEE Photon. J. 8, 0601109 (2016).
- 38. C. Rottondi, P. Martelli, P. Boffi, L. Barletta, and M. Tornatore, "Crosstalk-aware core and spectrum assignment in a multicore optical link with flexible grid," IEEE Trans. Commun. 67, 2144–2156 (2018).
- 39. F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay, "Scikit-learn: machine learning in Python," J. Mach. Learn. Res. 12, 2825–2830 (2011).
- 40. F. Arpanaei, N. Ardalani, H. Beyranvand, and B. Shariati, "QoTaware performance evaluation of spectrally–spatially flexible optical networks over FM-MCFs," J. Opt. Commun. Netw. 12, 288–300 (2020).
- 41. B. C. Chatterjee, A. Wadud, I. Ahmed, and E. Oki, "Priority-based inter-core and inter-mode crosstalk-avoided resource allocation for spectrally-spatially elastic optical networks," IEEE/ACM Trans. Netw. 29, 1634–1647 (2021).
- 42. S. Petale and S. Subramaniam, "Machine learning-aided resource assignment in space division multiplexed elastic optical networks," in Proceedings of the International Conference on Computer Communications and Networks (ICCCN) (2021).
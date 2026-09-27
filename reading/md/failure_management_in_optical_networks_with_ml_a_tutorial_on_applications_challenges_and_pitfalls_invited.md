---
title: "Failure management in optical networks with ML: a tutorial on applications, challenges, and pitfalls [Invited]"
tema_principal: reading
temas_relacionados: []
ano: 2025
autores: []
veiculo: null
pdf: ../pdf/failure_management_in_optical_networks_with_ml_a_tutorial_on_applications_challenges_and_pitfalls_invited.pdf
---

# Failure management in optical networks with ML: a tutorial on applications, challenges, and pitfalls [Invited]

**Francesco Musumeci\* AND Massimo Tornatore**

Politecnico di Milano, Milano, Italy \*francesco.musumeci@polimi.it

Received 16 December 2024; revised 19 May 2025; accepted 20 May 2025; published 26 June 2025

**This tutorial identifies and discusses the main design choices and challenges arising in the application of machine learning (ML) to optical network failure management (ONFM), including quality of transmission estimation, failure detection, prediction, root-cause identification, localization, and magnitude estimation. We focus on input data preparation and on interpreting and validating model outputs, tackling data scarcity, data confidentiality, model explainability, uncertainty quantification, and other critical factors, in order to highlight the potential risks for practitioners when adopting ML-based solutions for ONFM. An overview of publicly available datasets is also provided.** © 2025 Optica Publishing Group. All rights, including for text and data mining (TDM), Artificial Intelligence (AI) training, and similar technologies, are reserved.

https://doi.org/10.1364/JOCN.551910

# 1. INTRODUCTION

Addressing failure management in optical networks is of utmost importance, as optical networks represent the backbone of modern high-speed communications, and optical technologies are extremely pervasive in all segments of communication networks, from access/metro and up to core and data center network segments. Therefore, the ability to prevent or quickly react to failures is crucial to provide high network availability.

Traditional techniques for optical network failure management (ONFM) have relied heavily on manual intervention and rule-based algorithms, often resulting in slow response times and suboptimal recovery actions in the face of network failures. To address these shortcomings, machine learning (ML) has emerged as a promising solution for automating and optimizing failure diagnosis and consequently improving management and recovery processes in optical networks. More generally, the application of ML to various optical networking use cases has been extensively studied in the recent literature, also investigating the role played by advanced AI tools, such as large language models (LLMs), generative AI, meta-learning, etc., in fully automating optical networks.

For the specific case of ONFM, different surveys and tutorials have already appeared in the literature [1–6], demonstrating the successful application of ML to address various failure management use cases. These existing surveys have highlighted the power of data-driven algorithms to predict and analyze failures, adapt to dynamic network conditions, and offer more efficient and proactive strategies to maintain network performance. However, as with any emerging technology, the integration of ML into optical network management comes with its own set of challenges, mainly including issues related to data quality, model interpretability and explainability, and scalability.

This paper reports on and extends the tutorial in [7] and aims to provide a comprehensive overview of these challenges, focusing on the application of advanced ML frameworks to ONFM, namely, active, continual, federated and transfer learning, generative-AI-based data augmentation, explainable AI, and uncertainty quantification.

We systematically discuss how input data should be selected, collected, and shared, and how ML model outputs should be interpreted and validated. To this aim, after an overview of ML-driven failure management applications, we identify key areas where recent work has brought substantial improvements in 1) input data refinement and 2) model output interpretation, also emphasizing potential gaps in existing research.

The remainder of this paper is organized as follows. In Section 2, we briefly discuss the main applications of MLbased ONFM, reporting the most relevant literature for various cases. In Section 3, we identify the most relevant problem design choices that need to be considered when dealing with ML-based ONFM. Section 4 overviews the currently available datasets used for ONFM. The most relevant challenges, related to improving the quality of input data and properly interpreting and validating ML model outputs, are discussed in Section 5. We conclude the paper in Section 6, where we also identify other open research directions.

Table 1. Different ONFM Use Cases and Adopted ML Algorithms

| Use Case             | Addressed Question              | ML Algorithms             |               |            |            |
|----------------------|---------------------------------|---------------------------|---------------|------------|------------|
|                      |                                 | NN-Based                  | SVM           | Tree-Based | Others     |
| QoT estimation       | Can we avert a failure?         | [8–12]                    | [9]           | [9,13]     | [9,14–16]  |
| Detection            | Is there a failure now?         | [1,11,12,17–32]           | [1,22,27,33]  | [1,33–35]  | [33,35–39] |
| Prediction           | Will there be a failure?        | [9,40–44]                 | –             | –          | –          |
| Identification       | What is the failure root-cause? | [1,12,19,23–27,45–54]     | [10,11,27,52] | [52]       | [52]       |
| Localization         | Where is the failure?           | [17,21,23,29–31,40,55–65] | [10,11,64]    | [55,64,66] | [67,68]    |
| Magnitude estimation | What is the failure severity?   | [1,12]                    | –             | –          | [67]       |

### 2. ONFM APPLICATIONS OVERVIEW

ONFM involves a wide set of use cases, targeting different objectives along the lifetime of an optical network, a lightpath, or a set of optical devices. Table 1 reports a summary of the different ONFM use cases together with references to a selection of the most recent papers covering them. The different ONFM applications are also overviewed in the following subsections.

#### A. QoT Estimation

When accommodating a new lightpath request to transport a given amount of traffic between two points of the network, different choices should be made concerning the used wavelength and bandwidth, route, adopted modulation scheme, coding rate, etc. For each candidate option, assessing lightpath feasibility, i.e., performing **QoT estimation**, even before it is established, is crucial to avoid service disruption and also use spectrum resources effectively.

Today's most common approach to estimate lightpath QoT, e.g., in terms of the end-to-end optical signal-to-noise ratio (OSNR), generalized signal-to-noise ratio (GSNR), Q-factor, SNR, or bit error rate (BER), is by leveraging analytical models that take into account the main physical-layer impairments, such as nonlinear interference, amplified spontaneous emission (ASE) noise, and optical filtering [69,70]. However, real optical networks often encompass different sources of uncertainty, e.g., related to unknown connector losses, EDFA gain ripple, fiber type, and precise fiber link length. Therefore, analytical models account for these uncertainties by introducing fixed QoT margins, which might induce a waste of spectrum and transponder resources.

An alternative approach is to perform ML-based QoT estimation by leveraging historical data. As illustrated in Fig. 1, historical data that map the characteristics (i.e., the input features, such as route, modulation, wavelength, etc.) of previously-established lightpaths with the corresponding *measured* QoT (e.g., the SNR) can be leveraged by ML models to learn the effects of physical layer impairments, *including uncertainties*, on lightpath QoT with no need to accurately estimate the individual sources of uncertainty. Then, trained ML models can provide a more accurate QoT estimation for future candidate lightpaths given the knowledge of their characteristics. However, note that trained ML models are often subject to biases that can be introduced by the specific traffic and network conditions occurring during data collection. Developing robust ML models capable of generalizing across

| Route              | Wavelength | Modulation | SNR        |
|--------------------|------------|------------|------------|
| A-C-B              | 1550 nm    | BPSK       | 18dB       |
| C-B-E              | 1553 nm    | 8-QAM      | 23dB       |
| A-C-D-E            | 1556 nm    | QPSK       | 16B        |
| Lightpath features |            |            | QoT metric |

![](_page_1_Figure_15.jpeg)

Fig. 1. ML-based QoT estimation.

different network conditions (even unobserved ones) and without necessarily involving extensive data collection is a subject deserving further attention in the applications of ML to optical networks, including ONFM.

An intermediate approach, which has gained momentum in these last years, is what we refer to as *input refinement*. In this case, analytical models are preserved, but the estimation of the uncertain model parameters is refined using ML [71].

Independently of the chosen approach, QoT estimation allows operators to make more informed (hence, less conservative) decisions on the QoT margins to be used to protect the system against outages due to QoT fluctuations, resulting in decreased resource waste.

# B. Failure Detection and Prediction

During the lightpath lifetime, even though the QoT estimated before its deployment is adequate to correctly receive the transported information, several factors can contribute to the deterioration of the original quality, such as the presence of newly deployed lightpaths, equipment aging, deterioration or malfunctioning, fiber bending, etc., possibly causing service disruption. In this context, ML can be used to extract useful information from monitored parameters, as shown in the example in Fig. 2. In the example, we assume that the BER (as an example of a QoT metric) is continuously monitored at the lightpath receiver and that the lightpath is experiencing

![](_page_2_Figure_3.jpeg)

Fig. 2. ML-based failure detection and prediction.

deterioration due to which, once the BER increases above a certain intolerable threshold, a failure occurs. Exploiting ML, the idea is to identify a *signature* in the BER *behavior* that goes beyond the simple comparison between raw BER values and the specific intolerable threshold, e.g., by analyzing how BER statistics (e.g., mean, standard deviation, peak, etc.) vary over time. Doing so, we can predict the failure occurrence in advance (**failure prediction**) or in its immediate proximity (**failure detection** or **early detection**), and allow enough time to prevent or limit service disruption, e.g., via lightpath reconfiguration, traffic rerouting, modulation format downgrade, etc.

# C. Failure Identification, Localization, and Magnitude Estimation

Once a failure has been detected over a lightpath, further information might be useful to limit service disruption and reduce the cost of reparation, especially concerning the failure's root cause, its location, and its severity. Addressing these issues is commonly referred to as failure identification, failure localization, and failure magnitude estimation, respectively.

Concerning **failure identification**, note that different root causes can be the source of the failure, e.g., a filter shift or tightening in a wavelength selective switch (WSS) within a ROADM, a malfunctioning EDFA that provides an unexpectedly low gain, laser drift at the transmitter, a bent fiber, a deteriorated connector, etc. Discriminating between the different root causes allows the intervention to be focused on the subset of specific devices that can be the source of the failure, thus reducing the time required for troubleshooting. Each of the aforementioned root causes typically has a different impact on the affected lightpath, which can be discriminated by, e.g., observing some QoT metric at the receiver. Figure 3 qualitatively shows the behavior of a generic QoT metric for the cases of anomalies caused by a malfunctioning WSS or EDFA (green and red curves, respectively), compared to a normal QoT behavior (black curve). It is important to note that, in general, any anomaly may provide significantly different QoT compared to a normal situation where a lightpath is not affected by a failure. However, simply looking at the raw QoT values may not be enough to discriminate between the failure causes, as shown in the figure, where the QoT curves related to the two different sources of failure overlap. With ML, instead, it is possible to extract useful information by observing the possible "hidden" signature of the failure cause on the monitored QoT metric.

Similar considerations can be drawn for the cases of **failure localization** and **magnitude estimation**, with the idea that a failure originated by a certain root cause has different effects on

![](_page_2_Figure_10.jpeg)

Fig. 3. ML-based failure identification.

the monitored QoT at the receiver (or even on other metrics collected through the entire lightpath), according to the specific location (e.g., whether hitting a WSS at one ROADM or another) and/or different magnitude levels (e.g., a WSS filter tightening of 1 or 5 GHz).

Therefore, knowing the exact location of the failure allows it to directly operate on the affected network component and, consequently, reduces the time required for failure recovery. Additionally, estimating the failure magnitude is important if different recovery actions are possible. For example, a weaker failure can be solved by simply restarting/reconfiguring a device, while a more severe failure may necessitate in-field intervention, e.g., to physically fix or even replace a malfunctioning device. Evidently, the ability to discriminate between such different situations makes it possible to limit unnecessary operational costs and reduce (or even avoid) service disruption.

It is important to note that most existing studies focus on one of the aforementioned objectives at a time. However, the rigid distinction between different failure scenarios, as considered during ML model development, is not always an adequate representation of all the possible conditions in the real network. As an example, when developing an ML model for failure localization, available data typically includes samples of the same failure type "X" and, in some cases, also with the same magnitude, occurring at different locations (e.g., a 3 dB gain reduction in EDFAs located in different links of the network). Therefore, rigorously, the developed ML model has been trained to distinguish between the occurrences of *that specific failure "X"* (with that specific magnitude) on the different links, and there is often no guarantee that the same model will provide similar localization performance in the case of different failure types and/or different failure magnitudes.

Therefore, considering the combined effect of different failure causes, different failure locations, and different failure magnitudes is not trivial and, to the best of our present knowledge, it is largely unaddressed in current literature.

# 3. DESIGN CHOICES

To address ONFM, especially when considering ML-assisted approaches where network data is essential, several design choices and intertwined decisions must be taken into account already before data collection starts, and of course also during ML model development, as detailed below.

#### **What type of data should we collect?**

Modern networks support extensive data collection and telemetry targeting different objectives beyond the application to failure management. Extremely diverse types of information are extracted from the network at the physical, network, and even application levels, including transmission quality parameters, bit/packet losses, data rate, service latency, etc. Considering this plethora of information, it is not trivial to determine *a priori* which data will turn out to be more useful for ONFM and the particular objective at hand. This decision has several implications on 1) the way data shall be transferred from the different monitors toward a location where data are processed, 2) the necessary memory and computing resources to store and process collected data, 3) the ML model selection, i.e., whether to analyze time-series data or tabular data has an impact on the type of algorithm to use, and 4) model complexity and training duration. Existing work, e.g., [31,33], evaluates the performance of different models by comparing various sources of collected data.

#### **Where to set monitor locations?**

This aspect is evidently intertwined with the above choice of data collection. After selecting the type(s) of data to use, the number of monitors and their locations impact the trade-off arising between data transfer/storage requirements and the performance of the ML models as, on the one hand, collecting and processing more data implies higher communication and computing costs, while, on the other hand, larger datasets generally favor ML models' performance, as analyzed in [15,62].

# **Which network domains and technologies are of interest?**

The penetration of photonics in the modern Internet is undoubted and covers all network segments, from core to metro and access segments and up to intra-datacenter networks, and as well it involves multiple technologies and operational standards, such as wavelength division multiplexing (WDM), flexi-grid and elastic optical networks (EONs) [40], optical transport network (OTN) [57], passive optical networks (PONs) [60], fiber-to-the-home and similar technologies (FTTx), free space optics (FSO), etc. Each of these domains and technologies is subject to failures and, of course, operators have an interest in failure management across all of them. However, in case a choice is necessary, an operator may privilege domains/technologies where the highest probability of failure is expected, where the highest amount of traffic would be affected by a failure, or also where the cost of ineffective failure recovery is higher (i.e., time-consuming or causing unnecessary resource waste). Consequently, focusing on some domains/technologies rather than others has an impact on data collection, data storage, and processing, and how to leverage ML model outputs to repair the failure.

# **What types of failures do we target?**

Since multiple types of failures can affect a network, one may want to concentrate on specific ones, e.g., the most frequent, the hardest to handle, the ones potentially affecting the highest amount of traffic, etc. Another major distinction between failures concerns the difference between hard failures, consisting of sudden and typically unpredictable events (e.g., fiber cuts) [72], and soft failures, involving gradual degradation of signal quality (e.g., see [24,27,39,40,47,56,63], etc.). Moreover, the possibility of having concurrent failures should be taken into account, which may lead to different conclusions compared to the cases where failures are handled one at a time (e.g., different impacts on the monitored parameters, different classes of failures to be distinguished with the ML model, etc.). Selecting which types of failures are of interest, among all the types above, mainly impacts data collection, especially considering the inherent failure data scarcity from real operational networks, and ML model training, as a model optimized using some type of failure data for training can provide poor performance if, at the deployment phase, the type of failures to handle is different. In this case, one can aim at training a generalized ML model including multiple failure types, at the cost of possibly lowering the global model performance and with the intrinsic limitation of collecting more diverse data before training.

# **Who is in charge of ONFM decision-making?**

Regardless of the physical locations where data are collected and how ML models combine the different sources of information, a main issue arises when deciding who is in charge of failure monitoring and handling. For example, an operator may have visibility of data collected across the whole network and therefore develop ML models fed with all the data generated in its network. Conversely, it is also possible that the operator may require specialized assistance from vendors to interpret the meaning and behavior of data retrieved by some specific devices. On the other hand, vendors may leverage in-house domain knowledge on their equipment but often cannot freely access data of all other equipment in the same network, especially in disaggregated network scenarios [36,55], where equipment of multiple vendors co-exist. Therefore, a collaborative environment where operators and vendors cooperate to monitor the network and address failures is often preferable to centralized scenarios where a single player makes decisions in an isolated manner [30]. For the same reasons, fully automating failure management is not always possible, but in some cases, a hybrid human–machine interaction might be necessary, also considering the possible uncertain outputs retrieved by a "black box" ML model. All these aspects impact, in particular, the way network data are collected and shared among different players.

# **Are the data used for ONFM confidential?**

In most cases, the transfer of sensitive data is necessary to develop ML models, due to the fact that ML models are typically trained on centralized servers that are not co-located with the monitoring locations of the necessary data and, more importantly, the data collector and data user are not always the same entity. This aspect has an impact on the type of data that can be shared with third parties, possibly via a public network, and hence on the information that can be leveraged during the training phase. Data encryption can be leveraged to exploit valuable information from network data while still preserving privacy [36,38,39], which implies additional storage and computing requirements that need to be taken into account when developing the ML models.

# **What is the proper time horizon for failure management?**

The time dimension plays a fundamental role in all phases of ONFM, from data collection to model training during the model development phase, and up until inference frequency and data/model updates at the deployment phase. More specifically, how often should data be collected is not trivial, especially considering that each type of data can provide valuable information at different time scales. For example, routing information (and similarly, all other lightpath "design" characteristics, such as modulation, central wavelength, etc.) can be collected less frequently as this information is typically stable over time, whereas signal quality indicators (e.g., OSNR, BER, input/output power in EDFAs), instead, vary much more frequently and so provide useful information if continuously collected. Moreover, it is not trivial to decide when performing ML model training, e.g., when a sufficient amount of data has been collected. Similarly, in case updating the ML model is necessary, e.g., due to a change in input data distributions and/or in the inputs/outputs relationship over time (known as *data drift*), deciding the moment to perform such an update impacts the trade-off between model performance and storage/computing requirements. Finally, the appropriate frequency to perform inference is also crucial, especially in ONFM, where detecting failure presence and determining failure root cause, location, etc., is fundamental to reduce or avoid service downtime. For higher frequency, more aggressive ONFM can be pursued with the objective of reducing service downtime as much as possible; however, at the same time, a higher computational effort as well as more extensive data collection is necessary to perform inference.

# **What ML algorithms can be used for failure management?**

Several ML algorithms can be adopted for ONFM, including supervised, e.g., linear and logistic regression, neural networks (NNs), support vector machines (SVMs), K-nearest neighbors (KNNs), tree-based models such as random forest (RF) or eXtreme gradient boosting (XGB), and unsupervised algorithms, such as K-means, isolation forest, DBSCAN, etc. The choice of ML algorithms depends on several factors, including the presence/absence of labels in the dataset, the structure of the data, and the degree of correlation among the different features in the dataset. As a general rule, when dealing with tabular data, tree-based models have proven to be very powerful, as shown in some recent studies [73,74], while models based on NN are typically the most suitable when there is a correlation between different samples and/or different features in the dataset, as happens for time sequences or images. A detailed discussion of these algorithms is out of the scope of this paper, and the reader is referred to fundamental books (e.g., [75–77]) for rigorous discussion. Table 1 indicates which algorithms have been adopted for the various use cases in the surveyed papers.

The key questions discussed in this section are summarized in Table 2 together with some possible options for each of them.

# 4. AVAILABLE DATASETS

Although a very wide set of papers has addressed ONFM in these years, to the best of our knowledge, only a few datasets are publicly available at the time of writing. Indeed, most of the datasets are obtained either from private testbeds or from operational networks and are not published for confidentiality reasons. Other data sources are developed by generating synthetic datasets with commercial simulators or analytical models. For example, MATLAB code for dataset generation suitable for QoT estimation is available in [78], which allows monitoring of various optical parameters including the laser

Table 2. Different Design Choices in ONFM

| Key Parameters     | Options                                                                                       |  |  |
|--------------------|-----------------------------------------------------------------------------------------------|--|--|
| Collected data     | Power, BER, OSNR, spectrum, alarms,                                                           |  |  |
|                    | OTDR, latency, physical versus                                                                |  |  |
|                    | network/app-level info                                                                        |  |  |
| Monitor location   | Receivers/transmitters, ROADMs, EDFAs,                                                        |  |  |
|                    | links, spans, all devices                                                                     |  |  |
| Network domain     | Single lightpath versus network, single- versus<br>multi-domain, core/metro/access/datacenter |  |  |
| Network technology | WDM, OTN, EON, PON, FTTx, FSO                                                                 |  |  |
| Failure type       | Hard versus soft failures, single versus multiple                                             |  |  |
|                    | failures                                                                                      |  |  |
| Decision maker     | Operator, vendor(s), centralized versus                                                       |  |  |
|                    | distributed, collaborative, fully-automated                                                   |  |  |
|                    | versus human assisted                                                                         |  |  |
| Data ownership     | Shared versus private data                                                                    |  |  |
| Time horizon       | Continuous versus periodic data collection<br>and inference                                   |  |  |
| ML algorithms      | Linear/logistic regression, NN, SVM, KNN,                                                     |  |  |
|                    | RF, XGB; K-means, isolation forest,                                                           |  |  |
|                    | DBSCAN, etc.                                                                                  |  |  |

launch power, total input power of each fiber, attenuation values at variable optical attenuators (VOAs), EDFA gains, etc.

Among the publicly available datasets, the "Optical Failure Dataset" in [79] includes data collected from a laboratory testbed at Scuola Superiore Sant'Anna (Pisa, Italy), where different types of failures are emulated over a lightpath by altering WSS characteristics. Moreover, among the collected metrics for the various failure scenarios, there are OSNR and BER traces at lightpath receivers, as well as optical input/output power values at intermediate optical amplifiers.

Moreover, the dataset described in [80] includes a variety of transmission scenarios in a WDM system developed in a laboratory at the Fraunhofer Institute for Telecommunications (Berlin, Germany) and is suitable for various use cases, including QoT estimation. In this dataset, OSNR, BER, SNR, EVM, and Q-factor are collected as QoT metrics.

Furthermore, the dataset in [81] consists of optical time domain reflectometry (OTDR) traces and includes various fiber failures, i.e., fiber cut, eavesdropping, dirty connector, and bad splice, making the dataset suitable for failure detection, identification, localization, and other ONFM applications. Similar OTDR datasets are also available in [82], which includes failures due to reflective events, and [72], where reflective and non-reflective events, as well as a mixture of them (mainly, fiber cuts and fiber bends) are included. Finally, the dataset in [83] includes reflective failures with different magnitudes.

# 5. MAIN CHALLENGES IN INPUT DATA AND OUTPUT DECISIONS

Even though nowadays it is possible to develop extremely efficient ML models, as demonstrated by the wide research in this area, and considering the large amounts of tools, libraries, and documentation available for fast ML software development, still, the most critical challenges, and possible sources of pitfalls in ML-assisted ONFM reside in how to obtain *valuable input*

![](_page_5_Figure_3.jpeg)

Fig. 4. Main challenges and pitfalls in ML-assisted ONFM.

*data* and how the *output predictions* of ML models are interpreted, as graphically shown in Fig. 4. For all these challenges, there exist specific ML frameworks that can be adopted and that, in some cases, have already been considered in recent literature, as discussed below.

#### A. How to Collect Good Training Data?

As discussed in Section 3, different aspects need to be considered already during data collection, including deciding the type of collected data, data sampling frequency, etc. Additionally, even after addressing these issues, there is still no *a priori* guarantee that the ML model developed using such data will be the best possible model to deploy in the field, regardless of any possible optimization that can be done on the ML algorithms and on the selection of their hyperparameters. This is mainly due to the quality of the input data, which plays a crucial role in the ML model performance. In particular, even assuming that the collected data and considered features are the most informative out of all the possible combinations, the input data should still incorporate sufficient diversity to be fully representative of the real-life data distributions that the ML model will encounter at the inference phase. Consider the example of Fig. 5, where we show data points expressed through a generic two-dimensional feature space distinguishing classes A and B (red circles and green crosses, respectively). Assume that, in an initial phase, no data have been collected in the gray-shaded area of the feature space. In such a condition, an ML model, even properly trained, may lead to an incorrect decision boundary (see dashed line in Fig. 5), just because the initial training set is missing important data for training.

By means of *active learning*, useful data (e.g., light red circles and light green crosses in Fig. 5) can be collected, labeled, and added to the training dataset so that the model can be retrained in order to improve the decision boundary of the ML classifier.

Sometimes, even visually inspecting how the available data are distributed over the selected feature space might be sufficient to identify regions where collecting new data might provide additional information. Note that the reasons for missing labeled data can be different, e.g., it might occur that few data points are available for certain feature space areas or even that such data points have not been labeled. In the first case,

![](_page_5_Figure_10.jpeg)

Fig. 5. Input refinement through active learning.

using *probes* (i.e., forcing the system to generate specific data in a specific area) is necessary. In any case, additional effort might be required to annotate the newly generated data with a proper label, which is typically costly and time-consuming as it is performed by human experts. Considering this, and assuming that a (wide) set of unlabeled data are available, still, which data should be annotated first must be decided. A structured and widely adopted approach to do so consists of training a preliminary model with the available labeled data and then perform inference on the entire set of unlabeled data, assigning to each prediction a *score* (e.g., based on entropy, uncertainty, or other metrics) to measure how much the model is *confident* in this prediction. An example of the application of this approach for failure management, although in the context of microwave networks, is available in [84], but no similar approaches exist in optical networks, to the best of our knowledge.

An early work addressing QoT estimation [15] leveraged active learning to optimize and decrease the amount of probe lightpaths needed to build a training dataset capable of representing the variety of lightpath configurations in an optical network. Since then, most of the literature has relied on other strategies to increase and obtain good quality data, such as analytical models and developing network digital twins (see Section 5.B for more details).

# B. How to Deal with Data Scarcity?

The availability of training data is a key factor in developing ML models for ONFM, as it is difficult to collect failure data from real optical networks/systems due to the fact that failures rarely occur compared to normal operating conditions. To address this issue, which is tightly intertwined with the availability of *good* training data, as discussed in Section 5.A, three main approaches have already been adopted in the literature, i.e., 1) perform *data augmentation* via synthetic data generation; 2) develop *digital twins (DTs)* of a real network, consisting of a digitally simulated counterpart of a real network or even a physical replica (e.g., in a laboratory environment) of a part of the network, where failures are simulated/enforced with the objective of generating data [85,86]; and 3) use *transfer learning (TL)* to leverage the knowledge on a source domain (e.g., a different network), where a larger amount of data are available, and transfer it to the domain (e.g., the network) of interest, known as the target domain.

Synthetic data generation has been used in [25,47,48], where the authors leverage a variational autoencoder (VAE) [87] and a generative adversarial network (GAN) [88,89] to address data scarcity for failure detection and identification and show that a very limited amount of real data are needed to reach significant classification performance when using such data augmentation approaches and that even unknown failure causes can be identified. A variant of GAN, i.e., conditionaltabular GAN (CT-GAN), has been used in [49] together with another simpler approach, known as the synthetic minority oversampling technique (SMOTE), to improve the classification performance of failure identification under extreme data imbalance, which is a very critical issue in real networks as some failure causes may occur rarely.

The concept of DT has been used in [12] to generate data in a simulated environment by modeling the propagation of optical signals from the transmitter to the receiver in the optical time domain and address failure detection, identification, and magnitude estimation. Moreover, the authors of [63] use an experimental testbed as a DT to augment a base of field data with additional single-failure data and focus on failure localization. Furthermore, in [56,59], a DT is used to generate multiple mirror models of a real network where different types of failures are simulated to enlarge the knowledge base for future ML developments targeting failure localization.

Both synthetic data generation and the use of DTs aim at addressing data scarcity with additional data. Still in this area, semi-supervised learning can be adopted to increase the dataset size by training an ML model in a supervised manner in order to automatically annotate unlabeled data. This approach has been used in [20], where the authors perform failure detection in OTN equipment.

TL, instead, has been used in [22], to address data scarcity when developing a system capable of identifying vibrations in optical networks, which are the most relevant precursor of fiber cuts. Moreover, in [26,29] TL has been leveraged to address data scarcity in the context of failure detection, identification, and localization, focusing on transferring the knowledge acquired on one lightpath onto another lightpath [26] and also across different ONFM applications [29]. A particular flavor of TL, known as domain adaptation, has been used in [14] and compared with active learning to address data scarcity for QoT estimation.

### C. What to Do When Training Data Becomes Outdated?

During a network lifetime, the distribution of input data and the relationship between input features and their corresponding outputs (i.e., the labels) may change over time, e.g., due to equipment aging or changes in network status. This implies that new data should be collected to have an up-to-date representation of network conditions and, consequently, update ML models considering new data distribution. This approach, known as *continual learning*, has been used in some recent papers addressing QoT estimation, such as [90], where the authors leverage continuous model updates in response to shifts in data distribution over time. Nonetheless, we believe that further research is needed in this context, not only to cover ONFM applications beyond QoT estimation but also especially to address key aspects such as defining the appropriate criteria for model retraining (i.e., how frequently), the amount of new data needed to perform a model update, and how to avoid catastrophic forgetting of older data distributions upon model retraining with new data.

#### D. Is It Always Possible to Share Data?

Failure data are typically sensitive information that operators and vendors are not always willing to share through a public network. Therefore, instead of transferring data to centralized locations where ML models are trained, adopting *federated learning (FL)*, possibly combined with encryption strategies such as homomorphic encryption [91], enables privacy preservation of failure data to reach ONFM objectives. This paradigm also allows multiple parties, e.g., different vendors, operators, providers, etc., to cooperate and build ML models that leverage multiple types of data sources, possibly collected by different equipment types and/or different failure scenarios, thus representing complementary pieces of information.

Two different flavors of FL are possible, namely, horizontal and vertical FL (HFL and VFL, respectively), illustrated in Fig. 6 by an example. In the HFL case, different parties own information on different data instances through the same set of features. The example of the application of HFL in ONFM (see the upper part of Fig. 6) is the case of different vendors of the same type of equipment (e.g., a ROADM) that collect failure data, leveraging the same (or a similar) set of alarms' status, to perform failure identification. In this case, assuming that data for different failure causes are present in local datasets at each vendor, each vendor has interest in cooperating to develop a model capable of discriminating between multiple types of failure causes, leveraging the knowledge of the other vendor. Conversely, in the VFL case, the different parties own only a subset of features pertaining to the same data instances. As an example (see the lower part of Fig. 6), information pertaining to the same lightpath that traverses different monitor locations (e.g., OSNR at the receiver, input/output power of EDFAs, etc.) in a multi-operator scenario can be collected by the different operators, each controlling a subset of the monitors. In this case, the different operators can cooperate to share information and perform failure management over the same lightpath, e.g., to determine the failure location.

![](_page_7_Figure_3.jpeg)

Fig. 6. Collaboration between vendors or operators in ONFM with HFL and VFL.

Note that, in both the HFL and VFL cases, the different parties are assumed to own not only a subset of data instances (HFL) or a subset of features (VFL) but also the outputs (i.e., the labels) corresponding to the various data instances.

Cooperative learning based on HFL has been used in [45] by collecting failure data from multiple network domains with the aim of improving the generalization capability of failure detection while preserving the data confidentiality of the different domains. Moreover, the authors of [55] leverage VFL with homomorphic encryption in order to preserve the data privacy of different operators managing different equipment traversed while performing failure localization.

It is worth noting that FL is not the only privacy-preserving method to address failure management. For example, the authors of [36,38,39] perform failure detection by adopting data scrambling, also combined, in some selected scenarios, with homomorphic encryption and the distributed application of principal component analysis (PCA), that allow training on subsets of scrambled data without losing the original information contained in the ordered (i.e., unscrambled) data.

#### E. What Level of Confidence Do We Have in Our Decisions?

Accurate outputs provided by an ML model can be extremely critical for subsequent decisions in any ONFM application. As an example, assume that an ML model identifies a specific failure cause as the most likely to have happened after a failure occurs on a lightpath and that failure severity has been determined (possibly, by a different ML model) to be such that an in-field intervention is needed to substitute a ROADM card. If any of these two decisions is wrong, misclassification will lead to an unnecessary replacement of a device, with a consequent waste of resources.

For this reason, it is extremely important to allow ML models to provide *informed* decisions, e.g., by associating each prediction with a numerical score that quantifies the confidence of the prediction itself. A widely adopted instrument to evaluate this confidence is by *uncertainty quantification* of a predicted class for a given data instance [92], which is based on the concept of probabilistic classification [93]. The information brought by prediction uncertainty can be exploited by the decision maker to, e.g., decide whether to trust the output provided by the ML model automatically or if it is more convenient to explore more accurately the data instance, e.g., by involving a human domain expert and/or collect more information to fine-tune the decision. Another approach to provide confident and informed decisions is *conformal prediction*, based on ML models providing classification (similarly, regression) outputs in the form of *prediction sets* (respectively, prediction intervals), which globally provide a predefined level of formal guarantees of correctness [94].

An example of uncertainty quantification in ML-based ONFM is available in [43], where the authors leverage quantile regression and Bayesian uncertainty for QoT forecasting models relying on multi-layer perceptrons and long–short-term-memory-based neural networks (LSTM NNs). Moreover, probabilistic classification is also used in [45] to evaluate the model uncertainty for failure detection.

#### F. How Do We Explain Model Decisions?

In addition, providing a quantitative metric to assess prediction uncertainty, it is often desirable to obtain *qualitative* explanations of model behavior, e.g., what features had a major impact on the classification of a specific data instance, or what features globally provided more information for the model. *Explainable artificial intelligence (XAI)* includes a set of mathematical tools that provide quantifiable explanations of models' behavior. While there already exist simple algorithms, such as linear or rule-based (e.g., decision trees) models, that are inherently interpretable, i.e., they can provide an interpretation of model decisions that can be understood by humans (e.g., the set of thresholds on the considered features that are evaluated in a tree-based model), the power of XAI is that it is mostly model agnostic and can be adopted regardless of the ML model used to perform training and inference, hence including more complex non-linear models such as NNs.

Several XAI frameworks exist, including the well-known local interpretable model-agnostic explanations (LIMEs) [95]; however, the most frequently adopted in the context of ONFM is SHAP. The SHAP approach takes its origin from game theory and the concept of *Shapley value*, which aims at fair payout assignments to players based on their contribution to the total payout in a game. In the context of XAI, the game corresponds to the process of model inference by the ML model, features play the role of players in the game, and the payout of the game is represented by the output of the ML model, e.g., a certain class for an ONFM classification application.

The Shapley (SHAP) value is computed as the *marginal contribution* brought by a given feature toward a certain class, averaged across all possible subsets of features in the problem. More formally, SHAP measures the individual contribution of each feature for each data point by evaluating the difference in model output with and without using the feature, as detailed in Eq. (1):

#### Class being explained: Class "A" Color code: relative values of features y axis: list of - f6 is high (red dots): f22 most f6 impacts decision impactful Feature Value towards Class A features - f6 is low (blue dots): f6 impacts decision against Class A Each dot is one f21 data point x axis: feature impact (importance) according to SHAP value

**Fig. 7.** Use of a summary plot with SHAP values to explain the behavior of a model with respect to a generic class "A."

$$\phi_i(f, x) = \sum_{z' \subseteq x} \frac{|z'|!(M - |z'| - 1)!}{M!} \left[ f(z') - f(z'/i) \right].$$

Here, the SHAP value  $\phi_i(f, x)$  is calculated for a feature i and a given data point x and an ML model f. The marginal contribution  $\phi_i(f, x)$  is calculated over all possible coalitions z', i.e., the subsets of the overall features set x. Term  $\frac{|z'|!(M-|z'|-1)!}{M!}$ , represents a weight given to each coalition, where |z'| is the cardinality of the set of features in z' and Mis the total number of features. This weight is high for small and large coalitions, while it is low for medium-sized coalitions. For each feature i under evaluation and for each subset of the feature z',  $|f_x(z') - f_x(z'/i)|$  is the contribution (or importance) of the feature i to the coalition, evaluated as the difference between  $f_x(z')$ , the output of the model when feature i is considered, and  $f_x(z'/i)$ , the output of the model without feature i. Note that the same values of a feature in different data points can contribute differently to the output, depending on the values of other features for each of the data points, which makes the importance of a single feature valuable, in particular, concerning the coalition with other features.

One of the most widely adopted ways to leverage the informativeness brought by the SHAP value is to visualize *summary plots*, such as the one in Fig. 7, which shows an example of a summary plot to explain the behavior of an ML classifier with respect to a generic class "A." Details of the elements of the graph are shown in the figure. This type of graph is useful to understand the features' importance (the most important are shown in the top part of the figure, as they provide the highest absolute range of SHAP values across all data points), and to explain, for each feature and each data point, how the relative value of that feature has contributed to a decision toward (high positive SHAP) or against (high negative SHAP) the class being explained.

SHAP has been used in [42] to explain the predictions of an ML model estimating laser lifetime (corresponding to the mean time to failure, hence equivalent to failure prediction), by quantifying the relevance of the input features on the individual predictions. Moreover, in [34], the authors include domain experts' knowledge as an additional feature used in a classical supervised learning model. Here, the new features encompassing domain expertise are automatically obtained by a decision tree trained on historical data labeled by human experts. To confirm the intuition and the validity

of the decision-tree-based expertise enhancement, the authors use SHAP values to estimate feature importance, showing that the expertise-related features are always revealed to be the most important across several different ML models. Additionally, SHAP-based XAI has been adopted in [66] to evaluate the impact of different features collected at different monitoring points within a lightpath in localizing failures, in [96] to evaluate overall feature importance for failure detection, and in [13] to explain misclassifications in QoT estimation.

# 6. CONCLUSION AND FUTURE DIRECTIONS

Although a relevant amount of work has already been produced to address failure management in optical networks by leveraging ML, significant attention is yet to be put on obtaining high-quality data to train ML models and to evaluate and explain model decisions. In this paper, we discussed in detail specific research challenges in these two domains, also identifying available ML frameworks that are useful to address them, including active learning, data augmentation, digital twinning, transfer learning, continual learning, federated learning, uncertainty quantification, and XAI. For each of these techniques, we overviewed the main benefits and, where available, some of the papers that have already leveraged them to address the aforementioned challenges. Moreover, we discussed the characteristics of publicly available datasets suitable for various ONFM applications.

In addition to these, there are also other promising investigation areas that are worth mentioning and that are still unexplored. Among them, we believe the most important are in 1) the use of LLMs, transformers, and generative-AI to support ONFM in both data preparation and output interpretation/explanation, which are already being investigated in very recent literature [97,98]; 2) the standardization processes required to define common workflows between data collection, data transfer, data processing, and model development within large-scale networks; 3) the development of in-network inference, enabled by data plane programmability, to allow implementation of ML models directly in network equipment and at line rate; and 4) the definition of practical deployments of storage and computing resources dedicated to ML-assisted ONFM, considering the presence of multiple geographically distributed data sources and the possible need for distributed training and inference.

Funding. Ministero dell'Università e della Ricerca.

**Acknowledgment.** This work was supported by the Italian Ministry of University and Research under the Italian PRIN Project ZetON and PRIN PNRR project GASTON.

#### **REFERENCES**

- F. Musumeci, C. Rottondi, G. Corani, et al., "A tutorial on machine learning for failure management in optical networks," J. Lightwave Technol. 37, 4125–4139 (2019).
- R. Gu, Z. Yang, and Y. Ji, "Machine learning for intelligent optical networks: a comprehensive survey," J. Netw. Comput. Appl. 157, 102576 (2020).
- G. Villa, C. Tipantuña, D. S. Guamán, et al., "Machine learning techniques in optical networks: a systematic mapping study," IEEE Access 11, 98714–98750 (2023).

- 4. S. Cruzes, "Failure management overview in optical networks," IEEE Access 12, 169170 (2024).
- 5. D. Wang, C. Zhang, W. Chen, et al., "A review of machine learningbased failure management in optical networks," Sci. China Inf. Sci. 65, 211302 (2022).
- 6. M. Nouioua, P. Fournier-Viger, G. He, et al., "A survey of machine learning for network fault management," in Machine Learning and Data Mining for Emerging Trend in Cyber Dynamics (Springer, 2021), pp. 1–27.
- 7. F. Musumeci, "Machine-learning-assisted optical network failure management: challenges and pitfalls," in 50th European Conference on Optical Communication (ECOC) (2024).
- 8. X. Yang, T. Eldahrawy, C. Sun, et al., "Integrating PPE and inputs refinement for enhanced QoT estimation and optimization in an optical mesh network," in 50th European Conference on Optical Communications (ECOC) (2024), pp. 491–494.
- 9. S. Allogba, S. Aladin, and C. Tremblay, "Machine-learning-based lightpath QoT estimation and forecasting," J. Lightwave Technol. 40, 3115–3127 (2022).
- 10. L. E. Kruse and S. Pachnicke, "Joint QoT estimation and soft-failure localization using variational autoencoder," in Optical Network Design and Modeling (ONDM) (2023).
- 11. L. E. Kruse, S. Kühl, A. Dochhan, et al., "Experimental validation of machine learning-based joint failure management and quality of transmission estimation," IEEE Photonics J. 15, 8600309 (2023).
- 12. M. Devigili, M. Ruiz, N. Costa, et al., "Applications of the OCATA time domain digital twin: from QoT estimation to failure management," J. Opt. Commun. Netw. 16, 221–232 (2024).
- 13. O. Ayoub, S. Troia, D. Andreoletti, et al., "Towards explainable artificial intelligence in optical networks: the use case of lightpath QoT estimation," J. Opt. Commun. Netw. 15, A26–A38 (2023).
- 14. D. Azzimonti, C. Rottondi, A. Giusti, et al., "Comparison of domain adaptation and active learning techniques for quality of transmission estimation with small-sized training datasets [Invited]," J. Opt. Commun. Netw. 13, A56–A66 (2021).
- 15. D. Azzimonti, C. Rottondi, and M. Tornatore, "Reducing probes for quality of transmission estimation in optical networks with active learning," J. Opt. Commun. Netw. 12, A38–A48 (2020).
- 16. M. Ibrahimi, H. Abdollahi, C. Rottondi, et al., "Machine learning regression for QoT estimation of unestablished lightpaths," J. Opt. Commun. Netw. 13, B92–B101 (2021).
- 17. K. Abdelli, M. Lonardi, J. Gripp, et al., "Unsupervised anomaly detection and localization with generative adversarial networks," in 50th European Conference on Optical Communications (ECOC) (2024), pp. 998–1001.
- 18. A. Raj, Z. Wang, F. Slyne, et al., "Interference identification in multi-user optical spectrum as a service using convolutional neural networks," in 50th European Conference on Optical Communications (ECOC) (2024), pp. 314–317.
- 19. Q. Lin, X. Chen, Z. Ouyang, et al., "Scaling optical network fault management with decentralized graph learning," in Optical Fiber Communication Conference (OFC) (2024), paper Th3I.2.
- 20. Z. Sun, C. Zhang, M. Zhang, et al., "Semi-supervised learning model synergistically utilizing labeled and unlabeled data for failure detection in optical networks," J. Opt. Commun. Netw. 16, 541–552 (2024).
- 21. K. Abdelli, M. Lonardi, J. Gripp, et al., "Anomaly detection and localization in optical networks using vision transformer and SOP monitoring," in Optical Fiber Communication Conference (OFC) (2024), paper Tu2J.4.
- 22. K. Abdelli, M. Lonardi, J. Gripp, et al., "Risky event classification leveraging transfer learning for very limited datasets in optical networks," J. Opt. Commun. Netw. 16, C51–C68 (2024).
- 23. L. E. Kruse, S. Kühl, A. Dochhan, et al., "Experimental demonstration of soft-failure management using variational autoencoder and GAN on optical spectrum," in 49th European Conference on Optical Communications (ECOC) (2023), pp. 420–423.
- 24. H. Lun, M. Fu, Y. Zhang, et al., "A GAN based soft failure detection and identification framework for long-haul coherent optical communication systems," J. Lightwave Technol. 41, 2312–2322 (2023).

- 25. L. Z. Khan, J. Pedro, N. Costa, et al., "Data augmentation to improve performance of neural networks for failure management in optical networks," J. Opt. Commun. Netw. 15, 57–67 (2023).
- 26. F. Musumeci, V. G. Venkata, Y. Hirota, et al., "Domain adaptation and transfer learning for failure detection and failure-cause identification in optical networks across different lightpaths [Invited]," J. Opt. Commun. Netw. 14, A91–A100 (2022).
- 27. K. Sun, Z. Yu, L. Shu, et al., "Digital residual spectrum-based generalized soft failure detection and identification in optical networks," IEEE Trans. Commun. 71, 324–338 (2023).
- 28. K. Sun, Z. Yu, H. Huang, et al., "Autonomous and generalized soft failure detection based on digital residual spectrum in optical networks," in Optical Fiber Communication Conference (OFC) (2022), paper Th3D.5.
- 29. F. Musumeci, G. G. Marchionni, and M. Tornatore, "Cross-task and cross-lightpath failure detection and localization in optical networks using transfer learning," in IEEE International Conference on Communications (ICC) (2023), pp. 435–440.
- 30. X. Chen, C.-Y. Liu, R. Proietti, et al., "On cooperative fault management in multi-domain optical networks using hybrid learning," IEEE J. Sel. Top. Quantum Electron. 28, 3700209 (2022).
- 31. M. F. Silva, A. Pacini, A. Sgambelluri, et al., "Learning long- and short-term temporal patterns for ML-driven fault management in optical communication networks," IEEE Trans. Netw. Serv. Manage. 19, 2195–2206 (2022).
- 32. S. Liu, D. Wang, C. Zhang, et al., "Semi-supervised anomaly detection with imbalanced data for failure detection in optical networks," in Optical Fiber Communication Conference (OFC) (2021), paper Th1A.24.
- 33. S. Aladin, L. Wosinska, and C. Tremblay, "Detecting anomalies in the optical layer using unsupervised machine learning," in Optical Fiber Communication Conference (OFC) (2024), paper Th3I.4.
- 34. C. Zhang, Z. Sun, W. Yang, et al., "Expertise-enhanced machine learning for failure detection on field-deployed optical modules," J. Lightwave Technol. 43, 137–154 (2025).
- 35. W. Yang, C. Zhang, D. Wang, et al., "Data labeling using unsupervised cascaded pre-training with fused multi-port data for optical failure management," in Optical Fiber Communication Conference (OFC) (2024), paper W2B.8.
- 36. R. F. Sales, A. Ribeiro, M. F. Silva, et al., "Disaggregated confidentiality-preserving scheme for fault detection in optical networks," in Optical Fiber Communication Conference (OFC) (2024), paper Th3I.8.
- 37. A. N. Ribeiro, R. F. Sales, F. R. Lobato, et al., "PCA-assisted fuzzy clustering approach for soft-failure detection in optical networks," in Optical Network Design and Modeling (ONDM) (2024).
- 38. M. F. Silva, A. Sgambelluri, A. Pacini, et al., "Confidential detection of multiple failures in optical networks: an experimental evaluation," in Optical Fiber Communication Conference (OFC) (2023), paper Th2A.16.
- 39. M. F. Silva, A. Sgambelluri, A. Pacini, et al., "Confidentialitypreserving machine learning algorithms for soft-failure detection in optical communication networks," J. Opt. Commun. Netw. 15, C212–C222 (2023).
- 40. S. Behera, T. Panayiotou, and G. Ellinas, "Machine learning framework for timely soft-failure detection and localization in elastic optical networks," J. Opt. Commun. Netw. 15, E74–E85 (2023).
- 41. C. Xing, C. Zhang, Y. Wang, et al., "Spatio-temporal failure prediction using LSTGM for optical networks," in Optical Fiber Communication Conference (OFC) (2024), paper Th3I.6.
- 42. K. Abdelli, H. Grießer, and S. Pachnicke, "An interpretable machine learning approach for laser lifetime prediction," J. Lightwave Technol. 42, 2094–2102 (2024).
- 43. S. Yousefi, H. Chouman, P. Djukic, et al., "Forecasting lightpath quality of transmission and implementing uncertainty in the forecast models," J. Lightwave Technol. 41, 4871–4881 (2023).
- 44. S. Behera, T. Panayiotou, and G. Ellinas, "Modeling soft-failure evolution for triggering timely repair with low QoT margins," in IEEE Global Communications Conference (GLOBECOM) (2022), pp. 2140–2145.

- 45. X. Chen, C.-Y. Liu, R. Proietti, et al., "Automating optical network fault management with machine learning," IEEE Commun. Mag. 60(12), 88–94 (2022).
- 46. W. Yang, C. Zhang, X. Jiang, et al., "Spatio-temporal graph attention networks for alarm root cause recognition in optical transport network," in 50th European Conference on Optical Communications (ECOC) (2024), pp. 1002–1005.
- 47. L. E. Kruse, S. Kühl, A. Dochhan, et al., "Experimental investigation of machine-learning-based soft-failure management using the optical spectrum," J. Opt. Commun. Netw. 16, 94–103 (2024).
- 48. L. E. Kruse, S. Kühl, A. Dochhan, et al., "Monitoring data augmentation of spectral information using VAE and GAN for soft-failure identification," in Optical Fiber Communication Conference (OFC) (2024), paper M3I.4.
- 49. L. Z. Khan, J. Pedro, N. Costa, et al., "Model and data-centric machine learning algorithms to address data scarcity for failure identification," J. Opt. Commun. Netw. 16, 369–381 (2024).
- 50. L. Z. Khan, J. Pedro, O. Ayoub, et al., "Optimizing deep learningbased failure management in optical networks by monitoring relative neural activity," in Optical Network Design and Modeling (ONDM) (2024).
- 51. L. Z. Khan, J. Pedro, N. Costa, et al., "Model-centric versus data-centric machine learning for soft-failure cause identification in optical networks," in 49th European Conference on Optical Communications (ECOC) (2023), pp. 1027–1030.
- 52. C. Tremblay, A. Mahmoudialami, P. A. Ngani Sigue, et al., "Detection and root cause analysis of performance degradation in optical networks using machine learning," in 49th European Conference on Optical Communications (ECOC) (2023), pp. 1278–1281.
- 53. L. Z. Khan, P. J. Freire, J. Pedro, et al., "Data augmentation to reduce computational complexity of neural-network-based softfailure cause identifier," in Optical Fiber Communication Conference (OFC) (2023), paper M3G.3.
- 54. C. Zhang, D. Wang, J. Jia, et al., "Potential failure cause identification for optical networks using deep learning with an attention mechanism," J. Opt. Commun. Netw. 14, A122–A133 (2022).
- 55. M. Ibrahimi, F. Temiz, F. Musumeci, et al., "Vertical federated learning for failure localization in partially disaggregated optical networks," in IEEE 25th International Conference on High Performance Switching and Routing (HPSR) (2024).
- 56. R. Wang, J. Zhang, Z. Gu, et al., "Digital-twin-assisted meta learning for soft-failure localization in ROADM-based optical networks," J. Opt. Commun. Netw. 16, C11–C19 (2024).
- 57. Y. Jiao, P.-H. Ho, X. Lu, et al., "A novel framework for optical layer device board failure localization in optical transport network," IEEE Trans. Netw. Serv. Manage. 21, 5374–5383 (2024).
- 58. Y. Jiao, P.-H. Ho, X. Lu, et al., "A novel framework of failure localization in optical transport network," IEEE Commun. Mag. 61(12), 142–147 (2023).
- 59. R. Wang, J. Zhang, F. Musumeci, et al., "Meta-learning-based failure localization with digital-twin-enabled multi-mirror models in optical networks," in 49th European Conference on Optical Communications (ECOC) (2023), pp. 898–901.
- 60. K. Abdelli, C. Tropschug, H. Griesser, et al., "Faulty branch identification in passive optical networks using machine learning," J. Opt. Commun. Netw. 15, 187–196 (2023).
- 61. R. Wang, J. Zhang, S. Yan, et al., "Suspect fault screen assisted graph aggregation network for intra-/inter-node failure localization in ROADM-based optical networks," J. Opt. Commun. Netw. 15, C88–C99 (2023).
- 62. C. Zeng, J. Zhang, R. Wang, et al., "Multiple attention mechanismsdriven component fault location in optical networks with network-wide monitoring data," J. Opt. Commun. Netw. 15, C9–C19 (2023).
- 63. K. S. Mayer, R. P. Pinto, J. A. Soares, et al., "Demonstration of MLassisted soft-failure localization based on network digital twins," J. Lightwave Technol. 40, 4514–4520 (2022).
- 64. J. Babbar, A. Triki, R. Ayassi, et al., "Machine learning models for alarm classification and failure localization in optical transport networks," J. Opt. Commun. Netw. 14, 621–628 (2022).

- 65. H. Yang, X. Zhao, Q. Yao, et al., "Accurate fault location using deep neural evolution network in cloud data center interconnection," IEEE Trans. Cloud Comput. 10, 1402–1412 (2022).
- 66. O. Karandin, O. Ayoub, F. Musumeci, et al., "If not here, there. Explaining machine learning models for fault localization in optical networks," in Optical Network Design and Modeling (ONDM) (2022).
- 67. M. Cai, X. Liu, Y. Zhang, et al., "A physics-based learning approach for ROADM-induced anomaly localization and estimation," J. Lightwave Technol. 42, 4433–4443 (2024).
- 68. C. Delezoide, P. Ramantanis, and P. Layec, "Streamlined failure localization method and application to network health monitoring," J. Lightwave Technol. 41, 6119–6125 (2023).
- 69. P. Poggiolini, G. Bosco, A. Carena, et al., "The GN-model of fiber non-linear propagation and its applications," J. Lightwave Technol. 32, 694–721 (2014).
- 70. I. F. de Jauregui Ruiz, A. Ghazisaeidi, T. Zami, et al., "An accurate model for system performance analysis of optical fibre networks with in-line filtering," in 45th European Conference on Optical Communication (ECOC) (2019).
- 71. X. Yang, C. Sun, G. Charlet, et al., "Digital-twin-based active input refinement for insertion loss estimation and QoT optimization in C and C + L networks," J. Opt. Commun. Netw. 16, 1261–1274 (2024).
- 72. K. Abdelli, C. Tropschug, H. Griesser, et al., "An OTDR event dataset," IEEE DataPort (2022), https://dx.doi.org/10.21227/pw43- 9p78.
- 73. L. Grinsztajn, E. Oyallon, and G. Varoquaux, "Why do treebased models still outperform deep learning on tabular data?" in International Conference on Neural Information Processing Systems (2022).
- 74. R. Shwartz-Ziv and A. Armon, "Tabular data: deep learning is not all you need," Inf. Fusion 81, 84–90 (2021).
- 75. T. Hastie, R. Tibshirani, and J. Friedman, The Elements of Statistical Learning (Springer, 2009).
- 76. I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning (MIT, 2016).
- 77. J. Taeho, Machine Learning Foundations (Springer, 2021).
- 78. "Automated training dataset collection," GitHub (2021), https:// github.com/BrandonLJN/automated-training-dataset-collection.
- 79. "Optical failure dataset," GitHub (2022), https://github.com/ Network-And-Services/optical-failure-dataset.
- 80. C. Santos, A. Moawad, B. Shariati, et al., "Experimental dataset for developing and testing ML models in optical communication systems," J. Opt. Commun. Netw. 16, G1–G10 (2024).
- 81. K. Abdelli, F. Azendorf, C. Tropschug, et al., "Dataset for optical fiber faults," IEEE DataPort (2022), https://dx.doi.org/10.21227/pdpn-1b78.
- 82. K. Abdelli, H. Griesser, P. Ehrle, et al., "An OTDR dataset for optical fiber monitoring," IEEE DataPort (2022), https://dx.doi.org/ 10.21227/y0ek-1s16.
- 83. "Optical fiber link test bench," IEEE DataPort (2018), https://dx. doi.org/10.21227/H2N66K.
- 84. N. Di Cicco, M. Ibrahimi, F. Musumeci, et al., "Machine learning for failure management in microwave networks: a data-centric approach," IEEE Trans. Netw. Serv. Manage. 21, 5420–5431 (2024).
- 85. Q. Zhuge, X. Liu, Y. Zhang, et al., "Building a digital twin for intelligent optical networks [Invited Tutorial]," J. Opt. Commun. Netw. 15, C242–C262 (2023).
- 86. M. R. Sena, R. Emmerich, B. Shariati, et al., "Link tomography: a tool for monitoring optical network and designing digital twins," in 50th European Conference on Optical Communications (ECOC) (2024), pp. 176–179.
- 87. Y. Qu, H. Ma, Y. Jiang, et al., "A network data reinforcement method based on the multiclass variational autoencoder," Secur. Commun. Netw. 2022, 2993963 (2022).
- 88. H. Navidan, P. F. Moshiri, M. Nabati, et al., "Generative adversarial networks (GANs) in networking: a comprehensive survey & evaluation," Comput. Netw. 194, 108149 (2021).
- 89. I. Goodfellow, J. Pouget-Abadie, M. Mirza, et al., "Generative adversarial nets," in Advances in Neural Information Processing

- Systems, Z. Ghahramani, M. Welling, C. Cortes, N. Lawrence, and K. Weinberger, eds. (Curran Associates, 2014), Vol. 27.
- 90. Q. Wang, Z. Cai, and F. N. Khan, "Lifelong QoT prediction: an adaptation to real-world optical networks," J. Opt. Commun. Netw. 16, 1159–1169 (2024).
- 91. L. Yang, D. Chai, J. Zhang, et al., "A survey on vertical federated learning: from a layered perspective," arXiv (2023).
- 92. A. Malinin, L. Prokhorenkova, and A. Ustimenko, "Uncertainty in gradient boosting via ensembles," in International Conference on Learning Representations (2021).
- 93. V. Vovk, I. Petej, and V. Fedorova, "Large-scale probabilistic predictors with and without guarantees of validity," in Advances in Neural Information Processing Systems (2015), vol. 28.
- 94. V. Vovk, A. Gammerman, and G. Shafer, Algorithmic Learning in a Random World (Springer-Verlag, 2005).

- 95. M. T. Ribeiro, S. Singh, and C. Guestrin, ""Why should I trust you?" Explaining the predictions of any classifier," in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (2016), pp. 1135–1144.
- 96. C. Zhang, D. Wang, L. Wang, et al., "Cause-aware failure detection using an interpretable XGBoost for optical networks," Opt. Express 29, 31974–31992 (2021).
- 97. D. Wang, Y. Wang, X. Jiang, et al., "When large language models meet optical networks: paving the way for automation," Electronics 13, 2529 (2024).
- 98. C. Sun, X. Yang, N. Di Cicco, et al., "First experimental demonstration of full lifecycle automation of optical network through fine-tuned LLM and digital twin," in 50th European Conference on Optical Communications (ECOC) (2024), pp. 1002–1005.
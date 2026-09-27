---
index_terms:
  - machine learning
  - deep learning
  - optical fiber communication
  - optical wireless communication
  - optical communication networking
  - nonlinear equalization
  - quality of transmission estimation
  - resource allocation
---

# A Comprehensive Survey on Machine and Deep Learning for Optical Communications

## I. Introduction
Modern optical communication systems are increasingly complex due to numerous interdependent parameters in coherent transceivers, digital signal processing (DSP), and network optimization. Artificial Intelligence (AI)—specifically Machine Learning (ML) and Deep Learning (DL)—has become a pivotal tool for automated self-configuration and data analysis. While ML focuses on algorithms that learn from data to make predictions, DL utilizes multi-layer neural networks to handle large-scale, complex datasets with high accuracy.

In the physical layer, these technologies address modeling, adaptive signal processing, nonlinearity compensation, resource allocation, and constellation shaping. In Optical Communication Networking (OCN), they are applied to routing, fault detection, performance monitoring, and Quality of Transmission (QoT) estimation. 

ML algorithms are categorized into:
- **Supervised Learning (SL):** Labeled data for predictions (e.g., SVM, ANN, kNN).
- **Unsupervised Learning (USL):** Pattern identification in unlabeled data (e.g., K-means, PCA).
- **Reinforcement Learning (RL):** Optimal decision-making through environment interaction.

DL architectures include Deep Neural Networks (DNNs) for general complex relationships, Recurrent Neural Networks (RNNs) for sequential/temporal data, Convolutional Neural Networks (CNNs) for spatial data, and Deep Reinforcement Learning (DRL) for intelligent decision-making in dynamic environments.

### A. Related Works
Previous surveys have focused on specific niches: failure management, routing optimization in software-defined networks (SDNs), or resource allocation (RWA/RSA). Some have explored AI's role in signal processing and OPM (Optical Performance Monitoring) specifically. However, most are limited to a single domain (e.g., only OFC), leaving a gap for a holistic survey across fiber, wireless, and networking paradigms.

### B. Motivations, Novelties, and Contributions
**Motivations:** The rapid emergence of end-to-end learning and RL necessitates an updated, structured review. Existing literature often lacks a methodological/algorithm-centric focus, making it difficult for researchers to understand *how* specific AI techniques solve core optical challenges.

**Novelties and Contributions:** 
- Provides a comprehensive update across OFC, OWC, and OCN.
- Adopts an algorithm-centric approach rather than just an application-based one.
- Incorporates emerging trends like RL for dynamic optimization and end-to-end learning.
- Offers quantitative comparisons of performance gains over conventional algorithms.
- Identifies specific research gaps and proposes future directions.

### C. Paper Organization
The paper is organized by domain: Section II covers Optical Fiber Communication (OFC), Section III focuses on Optical Wireless Communication (OWC), and Section IV addresses Optical Communication Networking (OCN). Each section splits ML and DL approaches into detailed subsections based on algorithm type. Section V discusses challenges and future directions, followed by the conclusion in Section VI.

## II. Optical Fiber Communication

### A. Machine Learning
#### 1) Support Vector Machine (SVM) Algorithm
SVMs use hyperplanes to maximize margins between classes. In OFC, they are highly effective for mitigating Nonlinear Phase Noise (NLPN), laser phase noise, and modulator imperfections. In M-ary modulation (e.g., 16-QAM), SVM detectors improve sensitivity by 1.2–1.8 dB with lower complexity than linear detection. For nonlinear equalization (NLE), SVMs can achieve a 3.5 dB improvement at 60 Gbps and reduce computational complexity by up to 50% compared to traditional equalizers.

#### 2) Artificial Neural Network (ANN) Algorithm
ANNs model complex nonlinear relationships through adaptive learning. Key architectures include Radial Basis Function Neural Networks (RBFNNs) for smooth functions and Multi-Layer Perceptrons (MLPs) for nonlinearly separable data. In NLE, ANNs can improve the Q-factor by 2–8.7 dB compared to Volterra-based methods. They are also used for optimizing cascaded amplifier gains to maintain flatness and minimize noise figures.

#### 3) k-Nearest Neighbors (kNN) Algorithm
As a non-parametric method, kNN is useful for mitigating impairments like NLPN and I/Q imbalance. Enhancements such as distance-related weights improve tolerance to linewidth variations. "Non-Data-Aided kNN" further reduces complexity by using density parameters to identify noiseless data centers, resulting in BER improvements of up to 2 dB in some systems.

#### 4) Linear Models
Regression techniques (Linear, Ridge, Lasso) are used for signal prediction and impairment compensation. Lasso regression is particularly valuable for Space Division Multiplexing (SDM) because its L1 regularization promotes sparsity, identifying relevant perturbation terms while reducing nonlinearity-induced distortion by approximately 3 dB with low computational overhead.

#### 5) Hierarchical Clustering Algorithm
This USL method groups data into a tree-like dendrogram. It is used in NLE to group signals with similar nonlinear distortions. While effective, it is often outperformed by Fuzzy-Logic C-means, which adaptively determines optimal clustering based on fuzzy membership, offering better results for low-level modulation (BPSK/QPSK).

#### 6) K-Means Clustering Algorithm
K-means partitions data into $K$ subsets by minimizing within-cluster variance. Applications include tracking signal variations in Nyquist-WDM systems and RF phase recovery in radio-over-fiber links. It provides a computationally efficient alternative to Volterra series for NLE, improving Q-factors significantly over 500 km links.

#### 7) Expectation Maximization (EM) Clustering Algorithm
EM is a probabilistic approach used primarily to mitigate laser amplitude and phase noise. By modeling data as a mixture of probability distributions, it achieves significant improvements in Mean Squared Error (MSE) for phase noise estimation—up to 20 dB better than conventional methods—and operates ten times faster than Wiener filtering.

#### 8) Independent Component Analysis (ICA) Algorithm
ICA separates mixed signals into independent components without training symbols (uninformed equalization). It is superior to the Constant Modulus Algorithm (CMA) for higher-order modulation (16-QAM) and more robust against Polarization Mode Dispersion (PMD) and polarization-dependent loss (PDL).

### B. Deep Learning
#### 1) Deep Neural Network (DNN) Algorithm
DNNs learn intricate mappings to compensate for linear and nonlinear fiber impairments. They are used for Nonlinear Interference (NLI) mitigation, reducing complexity compared to Digital Backpropagation (DBP). In MDM systems, DNN detectors outperform MIMO Zero-Forcing methods. A major trend is end-to-end training of both transmitter and receiver, which optimizes constellation shaping and power adjustment simultaneously.

#### 2) Recurrent Neural Network (RNN) Algorithm
RNNs (LSTMs, GRUs) handle sequential data by maintaining temporal dependencies. They are highly effective as NLEs in PAM4 transmission, reducing BER by 20% and complexity by 50%. Cascade DNN-RNN architectures further reduce BER by up to 100x over non-cascade models. Bidirectional RNNs improve modeling of dispersive nonlinear channels.

#### 3) Convolutional Neural Network (CNN) Algorithm
CNNs extract spatial hierarchies from data. In Orbital Angular Momentum (OAM) communication, they are used for mode reconstruction and nonlinearity equalization in IM/DD systems. CNNs are significantly faster than iterative algorithms like Gerchberg-Saxton for modal coefficient reconstruction.

#### 4) Deep Reinforcement Learning (DRL) Algorithms
DRL agents optimize system parameters through trial-and-error based on reward functions. A key application is the optimization of Volterra equalizer structures, where DRL identifies optimal structural parameters more efficiently than exhaustive search or greedy methods, reducing complexity without BER loss.

## III. Optical Wireless Communication

### A. Machine Learning
#### 1) Support Vector Machine (SVM)
In Visible Light Communication (VLC), SVMs increase data rates by 35% over direct detection. In Free-Space Optics (FSO), they ensure reliable transmission under high noise and turbulence. They are also used for phase estimation, reducing BER by 60% at 10 dB SNR compared to Viterbi algorithms.

#### 2) Artificial Neural Network (ANN) Algorithm
ANNs handle atmospheric turbulence in FSO via adaptive wavefront correction (Strehl Ratio > 0.9). In VLC, they mitigate artificial light interference and enhance MIMO data rates (e.g., increasing a system from 200 kbps to 1.8 Mbps).

#### 3) k-Nearest Neighbors (kNN) Algorithm
kNN is primarily used for indoor VLC positioning via RSSI fingerprinting, achieving high accuracy (~2.7 cm) without requiring complex mathematical models of the environment.

#### 4) Ensemble Learning Algorithms
Techniques like Random Forest and XGBoost are used to predict RSSI in hybrid FSO/RF systems to enable seamless link switching during blockages. Random Forests have shown higher accuracy (100%) for RSSI prediction than Gradient Boosting.

#### 5) Regression Algorithms
Linear regression reduces VLC positioning errors by ~90%. Kernel Ridge Regression (KRR) with sigmoid preprocessing further improves this, reducing horizontal and vertical positioning errors by up to 48% compared to linear models.

#### 6) Hierarchical Clustering Algorithm
Used in FSO Mobile Ad-Hoc Networks (MANETs) to develop routing protocols that optimize connectivity and reduce the need for direct line-of-sight (LoS) between all nodes.

#### 7) K-Means Clustering Algorithm
Applied to real-time user identification in multi-user FSO and phase retrieval in underwater VLC, where it can increase data rates by correcting phase deviations in 8-QAM modulation.

#### 8) Expectation Maximization (EM) Clustering Algorithm
Used for channel estimation in OOK-FSO and OFDM-VLC systems. EM converges faster than Newton-Raphson methods and can achieve a BER of $10^{-3}$ at 10 dB SNR without requiring pilot symbols.

#### 9) Independent Component Analysis (ICA) Algorithm
ICA facilitates multi-user detection in FSO by separating signals from different wavelengths. It handles underdetermined systems (more transmitters than receivers) by exploiting signal sparsity and integrating with non-orthogonal multiple access (NOMA).

#### 10) Policy-Based Reinforcement Learning Algorithm
Used for iterative point-wise indoor positioning, reducing mean absolute error to 5 cm. It is also applied to adaptive resource allocation in multi-user VLC networks to manage bandwidth and power.

#### 11) Value-Based Reinforcement Learning Algorithm
Q-learning is used for power allocation in SDM-FSO systems and hybrid LiFi-WiFi networks, reducing delay and blocking probabilities compared to static heuristics.

### B. Deep Learning
#### 1) Deep Neural Network (DNN) Algorithm
DNNs are used as detectors and constellation shapers in FSO. In underwater VLC, DNN post-equalization reduces BER significantly compared to LMS equalizers and outperforms Volterra methods in terms of complexity.

#### 2) Recurrent Neural Network (RNN) Algorithm
GRUs predict FSO channel conditions using weather data with <6.9% error. LSTMs mitigate ISI and flicker in VLC; attention mechanisms further improve BER by focusing on relevant past signal components during long delays.

#### 3) Convolutional Neural Network (CNN) Algorithm
CNNs are used for OAM mode demodulation under strong turbulence, achieving >99% accuracy. They also enhance VLP positioning accuracy by 50% through RSS pre-processing and provide efficient wavefront correction in FSO.

#### 4) Deep Reinforcement Learning (DRL) Algorithms
DRL optimizes relay selection in cooperative FSO, power allocation in hybrid RF/VLC networks (outperforming genetic algorithms), and handover management in 6G hybrid architectures.

## IV. Optical Communication Networks

### A. Machine Learning
#### 1) Support Vector Machine (SVM) Algorithm
SVMs are used for QoT estimation with up to 99.95% accuracy, reducing processing time by 90% compared to semi-analytical methods. They also predict failure risks in OCNs with 95% accuracy.

#### 2) Artificial Neural Network (ANN) Algorithm
ANNs estimate OSNR, CD, and PMD using Asynchronous Amplitude Histograms (AAH). In EONs, ANN-based OSNR prediction achieves 95% accuracy and increases network capacity by up to 30% via optimized transceiver configuration.

#### 3) k-Nearest Neighbors (kNN) Algorithm
kNN is used for joint modulation format identification (MFI) and OSNR monitoring in OFDM systems, achieving 100% MFI accuracy with lower computational demand than ANNs.

#### 4) Ensemble Learning Algorithms
Random Forest (RF) provides a high-accuracy, low-complexity alternative for MFI and QoT prediction, reducing complexity by 4.6x compared to DNNs while maintaining higher robustness.

#### 5) Regression Algorithms
Linear regression is applied to fault localization in underground networks, improving distance accuracy and reducing the time required to restore service.

#### 6) K-Means Clustering Algorithm
K-means optimizes PON deployment (reducing cost by 50%) and identifies malicious nodes in OBS networks to prevent packet flooding attacks.

#### 7) Expectation Maximization (EM) Clustering Algorithm
Used for multi-user detection in OCDMA systems, managing multi-user interference without requiring CSI. It achieves BER within 2 dB of the optimal detector.

#### 8) Principal Component Analysis (PCA) Algorithm
PCA reduces dimensionality for real-time monitoring of OSNR and CD. It also enables high-accuracy fiber perimeter intrusion detection (99% rate, 0% false positives).

#### 9) Policy-Based Reinforcement Learning Algorithm
RL optimizes routing and wavelength assignment (RWA), reducing packet loss by 88% during failures in transparent networks. It also reduces blocking probability in OBS networks by up to 90%.

#### 10) Value-Based Reinforcement Learning Algorithm
Q-learning is used for path/wavelength selection in OBS, offering $O(n)$ complexity compared to the higher complexity of shortest-path or dynamic routing.

### B. Deep Learning
#### 1) Deep Neural Network (DNN) Algorithm
DNNs are used for MFI and OSNR monitoring. In EONs, DNN-based RSA reduces spectrum fragmentation by 20% and latency by 15%. They also provide high-accuracy QoT estimation in MDM systems.

#### 2) Recurrent Neural Network (RNN) Algorithm
LSTMs are used for real-time OSNR monitoring (MAE of 0.18 dB) and traffic prediction in multi-core fiber EONs, enabling faster resource allocation than statistical forecasting.

#### 3) Convolutional Neural Network (CNN) Algorithm
CNNs estimate EVM in <100 microseconds and perform joint MFI/OSNR monitoring with >99% accuracy. They also identify ONU fingerprints for network security with 99.25% accuracy.

#### 4) Deep Reinforcement Learning (DRL) Algorithms
DRL optimizes survivable RMSA in EONs, reducing blocking probability by up to 77%. It is also used for flow scheduling in hybrid optical-electrical networks and relay selection in FSO.

## V. Discussions, Challenges, and Future Directions

### A. Discussion of Key Findings
ML/DL significantly enhance signal detection, modulation recognition, and resource management across all three domains. However, the trade-off between accuracy (highest in DL) and computational cost remains a primary concern for real-time deployment.

### B. Categorization of Challenges
- **Data:** Scarcity of high-quality labeled data leads to overfitting.
- **Modeling:** Difficulty in choosing optimal models; lack of interpretability ("black box" nature of DL).
- **Resources:** High computational/memory requirements for training and deploying deep models.
- **Integration:** Incompatibility with legacy optical hardware architectures.

### C. Gaps in Existing Research
There is a shortage of large-scale, real-world implementations compared to laboratory studies. The long-term stability of AI models in live networks is under-researched, as is the full potential of RL for autonomous network control.

### D. Future Research Directions
- **Physics-Informed Neural Networks (PINNs):** Combining physical laws with ML to improve accuracy in data-scarce environments.
- **Dynamic Optimization:** Using RL for real-time adaptation of modulation and power allocation.
- **Hybrid Models:** Integrating traditional DSP with AI to balance performance and complexity.
- **Benchmarking:** Creating real-world case studies and standardized benchmarks.
- **Data Efficiency:** Exploring transfer learning and semi-supervised learning.
- **End-to-End Learning:** Moving from modular design to jointly optimized transceiver pipelines via deep autoencoders.

## VI. Conclusion
This survey provides a roadmap for AI in optical communications by analyzing ML/DL across OFC, OWC, and OCN. It demonstrates that while AI offers transformative gains in performance and automation, practical adoption requires overcoming hurdles in computational efficiency, data availability, and model interpretability.
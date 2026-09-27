---
index_terms:
  - optical performance monitoring
  - modulation format identification
  - machine learning
  - coherent optical detection
  - direct detection
  - stokes space
  - asynchronous sampling
---

# Machine Learning Techniques for Optical Performance Monitoring and Modulation Format Identification: A Survey

## I. Introduction
Optical networks are evolving toward autonomous, cognitive, and elastic architectures to handle increasing data traffic from 5G, IoT, and smart cities. To achieve this, network nodes must be intelligent, utilizing Optical Performance Monitoring (OPM) to estimate signal quality and Modulation Format Identification (MFI) to determine the modulation type at the receiver. These capabilities allow for a tradeoff between spectral efficiency, reach, and signal quality, enabling adaptive transmission based on channel conditions.

### A. Advantages of Using ML in OPM and MFI for Optical Networks
Classical approaches—Likelihood-based (LB), which require exact mathematical models, and Feature-based (FB), which rely on hand-crafted features and manual thresholds—are limited by their rigidity. Machine Learning (ML) provides several benefits:
*   **Real-Time Adaptability:** Online learning allows proactive fault prediction and stable operation through constantly adapting models.
*   **Flexibility:** Data-driven models adapt to diverse operational conditions without prior channel knowledge.
*   **Security:** ML can recognize security breaches by detecting changes in physical layer parameters that lack known mathematical models.
*   **Reduced Cost:** Proactive monitoring improves Quality of Service (QoS) and reduces operational expenses compared to single-task non-ML techniques.
*   **Resource Efficiency:** ML handles complex non-linear behaviors better than closed-form formulas, optimizing the use of tunable parameters in elastic networks.

### B. Review of Relevant Survey Articles
Existing surveys have focused on specific OPM techniques (filtering, interpolation) or ML in Software Defined Networking (SDN) for routing and resource management. While some reviews touch upon physical layer ML, there is a lack of comprehensive surveys specifically targeting the intersection of ML with both OPM and MFI across various network types.

### C. Summary of Paper's Contributions
This paper provides:
1.  A review of current standards, parameters, and commercial products for OPM/MFI.
2.  An extensive analysis of ML techniques for MFI, OPM, and joint tasks in direct and coherent networks over the last two decades.
3.  Tabular comparisons of algorithmic performance and characteristics.
4.  An exploration of ML application in emerging networks (RoF, FSO, SDM/Few-Mode Fiber).

### D. Paper Organization
The paper is structured as follows: Section II details ML algorithms; Section III reviews modulation formats and impairments; Section IV covers traditional and ML-based OPM/MFI for standard fibers; Section V discusses multiplexed signals; Section VI focuses on access networks (RoF, FSO); Section VII provides guidelines for algorithm selection; and Section VIII outlines open research issues.

## II. Machine Learning Algorithms
ML aims to estimate unknown functions mapping inputs to outputs. For OPM/MFI, this typically manifests as a regression problem (numerical values for impairments) or a classification problem (identifying modulation formats). Multi-task learning (MTL) is highlighted as a way to perform both simultaneously.

### A. Supervised Learning
Supervised learning uses labeled training data to minimize prediction error. Key algorithms discussed include:
*   **k-Nearest Neighbor (k-NN):** Nonparametric; predicts based on the majority vote of closest known pairs. Simple but storage-intensive for real-time use.
*   **Support Vector Machine (SVM):** Uses kernel functions to project data into higher dimensions to find a maximal margin hyperplane for separation. Superior accuracy but difficult to optimize meta-parameters.
*   **Artificial Neural Networks (ANNs):** Comprised of layers of neurons with weights and biases. Includes Multi-layer Perceptron 3 (MLP3) and Probabilistic Neural Networks (PNN), which approach Bayes-optimal solutions via radial basis functions. Deep Neural Networks (DNN) use multiple hidden layers for complex non-linear modeling but require large datasets.
*   **Convolutional Neural Networks (CNN):** Specialized for multidimensional/correlated data (e.g., images). Uses convolutional, pooling, and fully connected layers to automatically learn feature maps.
*   **Recurrent Neural Networks (RNN):** Designed for sequential/time-dependent data using internal memory loops. Long Short-Term Memory (LSTM) variants use gates to prevent vanishing gradients in long sequences.
*   **Decision Trees (DT):** Hierarchical binary decisions based on features. Prone to overfitting.
*   **Random Forest:** An ensemble of DTs that uses plurality voting to increase accuracy and reduce overfitting.

### B. Unsupervised Learning
Unsupervised learning extracts patterns from unlabeled data through clustering or dimensionality reduction (DR).
*   **Clustering Algorithms:** 
    *   *Partition-based:* e.g., k-means, which iteratively updates centroids.
    *   *Distribution-based:* e.g., Gaussian Mixture Models (GMM) using Expectation-Maximization (EM) or Variational Bayesian EM (VBEM).
    *   *Density-based:* e.g., DBSCAN and OPTICS, which distinguish core points from outliers based on local density; CFSFDP is an updated version that detects density peaks.
*   **Dimensionality Reduction (DR):** 
    *   *Linear:* Principal Component Analysis (PCA) finds directions of maximum variance; Independent Component Analysis (ICA) extracts linearly independent components.
    *   *Non-linear:* Multidimensional Scaling (MDS) and Stochastic Proximity Embedding (SPE) preserve pairwise distances. Auto-encoders use ANN structures to compress data into a hidden layer. t-SNE projects high-dimensional data onto t-distributions to preserve both local and global structures.

### C. Reinforcement Learning (RL)
RL uses an autonomous agent that takes actions in a search space to maximize a reward function. While widely used for routing and resource allocation in optical networks, the authors note that RL has not yet been significantly applied specifically to OPM and MFI problems.

### D. Lessons Learned
*   OPM generally requires regressors (continuous parameters), while MFI requires classifiers (discrete formats).
*   DR is essential as a preprocessing step to avoid the "curse of dimensionality" and facilitate visualization.
*   Algorithm choice depends on the trade-off between accuracy, dataset size, and computational complexity (e.g., CNNs for images, LSTMs for sequences).

## III. Optical Modulation Formats Generation and Optical Impairments

### A. Optical Modulation Formats
Modulation schemes are categorized by their detection method:
*   **Intensity Modulation–Direct Detection (IM-DD):** Includes On-Off Keying (OOK) in Non-Return-to-Zero (NRZ) or Return-to-Zero (RZ) formats, and Optical Duobinary (ODB), which reduces bandwidth and increases dispersion tolerance.
*   **Phase Modulation–Direct Detection (PM-DD):** Includes Differential Binary Phase Shift Keying (DBPSK) and Differential Quadrature Phase Shift Keying (DQPSK). These are less prone to nonlinear effects than OOK.
*   **Coherent Optical Detection:** Recovers both amplitude and phase using a local oscillator. This supports M-ary PSK and M-QAM, as well as Dual Polarization (DP) to double spectral efficiency.

### B. Optical Impairments
Impairments are divided into linear and nonlinear types:
*   **Linear Impairments:** 
    *   *Attenuation:* Exponential power loss due to scattering/absorption.
    *   *ASE Noise:* Introduced by optical amplifiers; measured as OSNR.
    *   *Chromatic Dispersion (CD):* Frequency-dependent speed causing pulse broadening and ISI.
    *   *Polarization Mode Dispersion (PMD):* Birefringence causes differential group delay (DGD) between orthogonal polarizations.
    *   *Polarization Dependent Loss (PDL):* Power loss difference based on the state of polarization.
    *   *Phase Noise (PN):* Originates from laser linewidth; severely affects coherent systems.
*   **Nonlinear Impairments:** Occur at high power levels. Includes inelastic scattering (SRS, SBS) and Kerr effects (SPM, XPM, FWM).

### C. Current Available Commercial Solutions and Standards/Recommendations for OPM and MFI in Optical Networks
Commercial OPM currently relies on non-ML tools: optical power meters, Optical Spectrum Analyzers (OSA), and specialized devices for CD/PMD monitoring (following ITU-T G.650 standards). OSNR is monitored via various vendors' DWDM solutions. No commercial ML-based OPM or MFI products exist; MFI is viewed as a requirement for future adaptive networks rather than current static ones.

### D. Lessons Learned
*   Impairments distort the unique "signatures" (time, spectrum, constellation) used for MFI/OPM.
*   Coherent receivers provide higher spectral efficiency and better signal recovery but at significantly higher costs than direct detection.
*   Most impairment mitigation is modulation-independent, except for carrier phase/frequency offset recovery, which requires prior knowledge of the format.

## IV. Optical Performance Monitoring and Modulation Format Identification

### A. Conventional OPM and MFI Techniques
*   **Conventional OPM:** OSNR monitoring uses out-of-band noise measurement or in-band techniques (polarization nulling, delay interferometers, electrical sampling). CD is monitored via RF tones or clock phase detection; PMD is monitored using eye diagrams or RF power spectrum.
*   **Conventional MFI:** Split into Likelihood-based (LB) and Feature-based (FB). FB methods use normalized power distributions, higher-order cyclic cumulants, amplitude deviation, information entropy of histograms, or nonlinear power transformations in the frequency domain via FFT.

### B. ML-Based Techniques for OPM and MFI
The general pipeline involves sampling $\rightarrow$ feature extraction (e.g., AH, CDF) $\rightarrow$ offline training $\rightarrow$ online estimation/classification.

#### 1) ML-Based Techniques for OPM
*   **Direct Detection:** Uses ANN/SVM trained on eye diagram features (Zernike moments, Q-factor, jitter). To avoid expensive timing recovery, asynchronous sampling is used; techniques like Asynchronous Amplitude Histograms (AAH), Asynchronous Delay-Tap Sampling (ADTS), and Parametric Asynchronous Eye Diagrams (PAED) extract statistical properties to estimate OSNR, CD, and DGD. CNNs can be applied directly to ADTS images for joint OSNR/CD monitoring.
*   **Coherent Detection:** Uses ANN on asynchronous constellation features or I/Q Histograms (IQH) via SVM. Deep Learning (DNN/LSTM-RNN) allows OPM using raw data without manual feature engineering. Transfer learning is used to accelerate training by leveraging pre-existing weights.

#### 2) ML-Based Techniques for MFI
*   **Direct Detection:** Employs AAH with ANN or Genetic Algorithm (GA) optimization, and Higher-Order Cumulants (HOC) with Decision Trees/SVM for low OSNR scenarios.
*   **Coherent Detection:** 
    *   *Stokes Space:* Maps signals to a 3D space independent of phase noise and polarization rotation. Unsupervised ML (GMM, VBEM, CFSFDP) clusters these points to identify formats. Supervised approaches use PNN or CNNs on Stokes plane images.
    *   *Other Time Domain Features:* Fractal Dimension + SVM for robustness against CD/DGD; intensity fluctuation features + SVM; and Random Forest with AH for M-QAM signals.
    *   *Image Processing:* CNNs applied to constellation diagrams, or Radon Transforms (RT) combined with SVD for high accuracy even at low OSNR.

#### 3) ML-Based Joint MFI and OPM Techniques
*   **Direct Detection:** Utilizes PCA with ADTS/ASCS for simultaneous bit rate, format, and impairment identification. MTL-based ANNs allow a single network to perform classification (MFI) and regression (OPM) simultaneously using AAH features.
*   **Coherent Detection:** Employs AH + DNN or CDF + SVM for joint OSNR and MFI. Cascaded DNNs can first identify the format and then estimate the impairment.

### C. Lessons Learned
Conventional methods are often limited to single impairments or a few formats. ML-based OPM is most viable via direct detection at intermediate nodes due to cost, whereas MFI typically requires coherent receivers for phase recovery and DSP preprocessing. Stokes space features are highly effective for MFI because they are transparent to phase noise and frequency offsets.

## V. OPM and MFI for Multiplexed Signals

### A. Orthogonal Frequency-Division Multiplexing (OFDM)
MFI for OFDM uses ANN with AH from the FFT stage or non-training based CFSFDP algorithms. Joint OSNR/MFI is achieved via k-NN regression. Coherent detection using Modulus Mean Square (MMS) features allows identification of hybrid modulation formats across subcarriers.

### B. Few Mode Fiber (FMF) Multiplexing
FMF introduces mode coupling (MC). Research indicates that ANN classifiers using IQH features can identify modulation formats with high accuracy under low MC, but performance drops as MC and CD increase.

### C. Lessons Learned
ML for multiplexed signals is in its early stages; existing studies often ignore specific impairments like inter-carrier interference (for OFDM) or mode-dependent loss (for FMF).

## VI. MFI and OPM for Access Networks

### A. Radio Over Fiber (RoF) Network
MFI in hybrid RoF utilizes ANN with AAH features or Auto-encoders with pre-processing to classify RF modulation formats over fiber, though performance degrades significantly beyond 70km due to CD.

### B. Free Space Optical (FSO) Communication Network
Focuses on Orbital Angular Momentum (OAM). CNNs are used to monitor atmospheric turbulence (AT) severity and detect OAM modes, providing feedback for transmitter correction.

### C. Lessons Learned
RoF requires accounting for both electrical RF noise and optical fiber impairments. FSO research must expand to include pointing errors and signal scattering alongside turbulence.

## VII. Discussions and Guidelines

### A. Criteria for Identifying the Appropriate Algorithm
Researchers should evaluate: (1) Accuracy, (2) Multitasking capability, (3) Acquisition hardware cost, (4) Ease of implementation, (5) Computational complexity/latency, and (6) The dynamic range of impairments the algorithm can handle.

### B. Features Utilized for OPM and MFI
*   **Asynchronous features (AAH, ADTS):** Low-cost, suitable for direct detection at intermediate nodes, but sensitive to CD/PMD.
*   **Coherent features (AH, CDF):** Robust against phase noise; appropriate for multi-level QAM.
*   **Stokes Space:** Independent of polarization rotation and PN, though sensitive to ASE noise.
*   **Frequency Domain (RF Spectrum):** Effective for OSNR monitoring under high CD.
*   **Image-based features:** High accuracy but computationally expensive.

## VIII. Lessons Learned, Open Issues and Research Direction

### A. Algorithm Multitasking
There is a need for comprehensive features that allow a single multitasking algorithm to monitor wide ranges of impairments and identify diverse formats simultaneously.

### B. New Modulation Formats
Traditional MFI focuses on standard QAM/PSK. Future research must address Probabilistic Constellation Shaping (PCS) and Geometric Shaping, as these non-standard constellations may be misidentified by existing tools.

### C. Nonlinear Impairments
Current ML OPM is mostly linear. Research should move toward monitoring nonlinearities (FWM, SPM, XPM), which limit signal power and transmission distance in WDM networks.

### D. Wireless and Hybrid Optical Networks
Future OPM/MFI must address hybrid channel complexities, including RF noise and fading in RoFSO and VLC networks.

### E. New Multiplexing Techniques
SDM (Multi-core/Few-mode fiber) requires new ML algorithms to handle mode coupling and mode-dependent loss.

### F. Real-Time ML Approaches
Transition is needed from offline training on static datasets to real-time, self-learning, and online adaptive architectures.

### G. Available Algorithms and Frameworks in Other Fields
The authors recommend moving beyond MATLAB toward Python frameworks (TensorFlow, PyTorch) to leverage the broader ML community's open-source tools.

## IX. Conclusion
ML provides a data-driven path toward autonomous optical networks. While supervised learning and ANN are dominant, there is room for growth in unsupervised clustering and deep learning. The future of the field lies in multitasking algorithms, monitoring nonlinear impairments, and adapting to new modulation formats and multiplexing techniques like SDM.
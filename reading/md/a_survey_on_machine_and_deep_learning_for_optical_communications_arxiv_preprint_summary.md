---
index_terms:
  - machine learning
  - deep learning
  - optical fiber communication
  - optical communication networking
  - optical wireless communication
  - nonlinearity compensation
  - quality of transmission estimation
  - resource allocation
---

# A Survey on Machine and Deep Learning for Optical Communications

## I. Introduction
The increasing complexity of optical communication systems, characterized by numerous interdependent parameters, necessitates automated analysis and configuration tools. Artificial Intelligence (AI), specifically machine learning (ML) and deep learning (DL), provides a transformative approach to handle the computational burdens of traditional analytical models. 

### A. Motivations
Despite rapid growth, many ML/DL algorithms remain unexplored in this field. Comprehensive surveys are necessary to synthesize recent advancements, identify research gaps, and guide practitioners toward promising opportunities for enhancing system performance and resilience.

### B. Related Works
Previous literature has focused on specific niches: failure management, routing optimization in Software Defined Networks (SDN), Routing and Resource Allocation (RRA) in various fiber types (WDM, EON, SDM), and Optical Performance Monitoring (OPM). While these have provided insights into physical layer issues and networking, few have integrated all domains of optical communication.

### C. Novelties and Contributions
This paper distinguishes itself from prior surveys by:
- Providing an up-to-date analysis across three distinct domains: Optical Fiber Communication (OFC), Optical Communication Networking (OCN), and Optical Wireless Communication (OWC).
- Adopting an algorithm-centric perspective rather than just an application-centric one.
- Including quantitative measures of gains achieved by ML/DL over conventional methods.
- Comparing the complexity, data requirements, and performance of various architectures to facilitate reproducibility and informed decision-making.

### D. Paper Organization
The survey is organized into a four-tiered structure: three main domains (OFC, OCN, OWC) are each subdivided into ML and DL implementations. ML is further categorized by learning type (Supervised, Unsupervised, Reinforcement), while DL is divided by architecture (DNN, RNN, CNN, DRL). The paper concludes with a discussion on challenges and future directions.

## II. Optical Fiber Communication (OFC)

### A. Machine Learning
ML algorithms are used primarily to mitigate signal impairments and optimize transmission:
- **Support Vector Machines (SVM):** Highly effective for mitigating nonlinear phase noise (NLPN), compensating for laser phase noise, and addressing modulator imperfections. SVMs also improve M-ary signal detection over conventional detectors in various modulation schemes (e.g., 16-QAM).
- **Artificial Neural Networks (ANN):** Used for Nonlinear Equalization (NLE) and amplification gain adjustment. RBFNNs are noted for linear data, while MLPs handle nonlinear data; both significantly enhance Q-factors compared to Volterra filters.
- **k-Nearest Neighbors (kNN):** Applied as detectors for non-Gaussian impairments (ASE noise, I/Q imbalance). Weighting distance-related points improves linewidth and nonlinearity tolerance.
- **Regression Algorithms:** Lasso regression is particularly useful in Spatial Division Multiplexing (SDM) to identify significant perturbation terms for compensating Kerr nonlinearity with low computational overhead.
- **Hierarchical & Fuzzy-Logic Clustering:** Used for NLE; Fuzzy-Logic C-means generally outperforms hierarchical clustering, especially at optimum launched power for BPSK/QPSK formats.
- **K-Means Clustering:** Employs time windowing to track signal variations in Nyquist-WDM systems and is used for multi-dimensional quantization in radio-over-fiber (RoF) to improve SNR.
- **Expectation Maximization (EM):** Leverages Bayesian analysis to mitigate laser amplitude and phase noise, improving launch power tolerance.
- **Independent Component Analysis (ICA):** Used for blind equalization and polarization demultiplexing, effectively mitigating Polarization Mode Dispersion (PMD) without requiring training symbols.

### B. Deep Learning
DL extends ML capabilities by learning higher-order representations of fiber impairments:
- **Deep Neural Networks (DNN):** Applied to compensate for linear/nonlinear effects and predict Raman gain profiles with high accuracy (>99%). End-to-end DNNs optimize both transmitter and receiver for constellation shaping.
- **Recurrent Neural Networks (RNN):** Specifically LSTMs and GRUs, these handle temporal dependencies in signals. They provide significant complexity reductions over ANNs while maintaining BER performance in NLE tasks. Transfer learning is used to adapt RNNs to new operating conditions with minimal retraining.
- **Convolutional Neural Networks (CNN):** Primarily utilized in Orbital Angular Momentum (OAM) systems to predict mode coefficients and perform nonlinearity equalization, outperforming Volterra filters by up to 3 dB.
- **Deep Reinforcement Learning (DRL):** Used to optimize the structure of Volterra-based NLEs, directly searching for optimal structures to reduce complexity without compromising performance.

## III. Optical Communication Networks (OCN)

### A. Machine Learning
ML in OCN focuses on network stability and resource efficiency:
- **SVM:** High accuracy (up to 99.9%) in Quality of Transmission (QoT) estimation and failure risk prediction, outperforming semi-analytical methods.
- **ANN:** Essential for OPM (estimating OSNR, CD, PMD) and traffic prediction. ANNs help calibrate fiber nonlinearity models and optimize symbol rates/modulation formats in bandwidth-variable transceivers.
- **kNN:** Effective for joint Modulation Format Identification (MFI) and OSNR monitoring in OFDM systems with low computational overhead.
- **Ensemble Learning (Random Forest):** Offers a balance of high accuracy and low complexity for MFI and QoT estimation, often outperforming DNNs in real-time implementation.
- **Regression:** Linear regression improves the accuracy and speed of fiber fault localization compared to traditional reflectometry.
- **K-Means Clustering:** Optimizes Passive Optical Network (PON) deployment costs and detects malicious "burst header packet flooding" attacks in OBS networks.
- **EM Clustering:** Enhances multi-user detection in optical CDMA systems by iteratively estimating interference.
- **Principal Component Analysis (PCA):** Used for joint OPM and as a feature extraction tool for perimeter intrusion detection and spectrum distortion analysis.
- **Policy-based RL:** Enables self-healing routing to recover from failures/attacks and reduces blocking probability in buffer-less OBS networks via deflection routing.
- **Value-based RL (Q-Learning):** Optimizes resource allocation in OWC and deflection routing in OBS, adapting to dynamic network conditions via a reward system.

### B. Deep Learning
DL handles the higher dimensionality of network management:
- **DNN:** used for MFI, OSNR monitoring, and Routing and Spectrum Assignment (RSA) in Elastic Optical Networks (EONs), reducing spectrum fragmentation by up to 20%.
- **RNN (LSTM/GRU):** Excels at time-varying OSNR estimation, multi-domain routing prediction (98% accuracy), and future traffic demand forecasting.
- **CNN:** processes constellation images for EVM extraction and joint MFI/OSNR monitoring; also used for device fingerprinting to authenticate legal ONUs in PONs.
- **DRL:** Optimizes global network performance, including survivable routing in EONs and virtual network slicing, significantly reducing blocking probabilities compared to heuristic methods.

## IV. Optical Wireless Communication (OWC)

### A. Machine Learning
ML addresses atmospheric turbulence and indoor positioning:
- **Supervised Learning (SVM):** Improves signal detection in VLC/FSO and mitigates phase offset after CMA equalization.
- **ANN:** Combats atmospheric turbulence in FSO through wavefront correction and filters fluorescent light interference in VLC to achieve error-free communication at high data rates.
- **kNN:** Provides robust indoor positioning for VLC, significantly reducing location error compared to traditional trilateration.
- **Ensemble Learning (RF/XGB):** Predicts RSSI for seamless FSO-to-RF switching and identifies objects via CSI analysis in VLC links.
- **Regression:** Kernel ridge regression with sigmoid preprocessing improves VLP accuracy over linear models.
- **Clustering (Hierarchical/K-Means):** Hierarchical clustering enables robust routing in FSO MANETs; K-means is used for user identification and phase retrieval.
- **EM Clustering:** Provides near-perfect channel estimation in FSO/VLC, often eliminating the need for pilot symbols (blind detection).
- **ICA:** Separates individual transmitted signals in multi-user FSO links by exploiting statistical independence.
- **RL (Policy & Value Based):** Optimizes VLP height information updates, power allocation in SDM-FSO, and resource management in hybrid LiFi-WiFi networks.

### B. Deep Learning
DL enhances the robustness of wireless optical links:
- **DNN:** Used as a low-complexity detector for FSO without needing CSI and to compensate for nonlinearities in underwater VLC.
- **RNN (LSTM/GRU):** Predicts FSO channel characteristics based on weather data and mitigates Inter-Symbol Interference (ISI) in camera-based VLC.
- **CNN:** Essential for OAM mode demodulation under strong turbulence and wavefront correction; also used to filter ambient light noise in VLC.
- **DRL:** Optimizes relay selection in cooperative FSO, power allocation in hybrid RF/VLC, and beamforming policies to prevent eavesdropping.

## V. Discussions, Challenges, and Future Directions

### A. The Challenge of Adaptability
Static models fail when network infrastructure or traffic patterns shift. The authors propose **continual learning** for real-time updates and **transfer learning** to apply knowledge across different networks. Additionally, **active learning** could reduce expensive data collection costs.

### B. Bridging the Gap: Optical Comms vs. established ML
The field should adopt tools from RF communication and image processing. Specifically, shifting from MATLAB to Python (PyTorch/TensorFlow) is recommended to better collaborate with the broader AI community.

### C. Open Dataset Access
A lack of real-world datasets hinders progress due to:
1. **Data Imbalance:** Real networks rarely fail, leaving few "negative" examples for training.
2. **Privacy:** Network operators are reluctant to share sensitive data.
3. **Simulation Gaps:** Synthetic data often lacks real-world nuance.
Solutions include standardized labeling protocols and using GANs to generate realistic synthetic data.

### D. Transparency (The Black Box Dilemma)
ML models often lack interpretability, making troubleshooting difficult for operators. The authors suggest utilizing **explainable AI (XAI)**—such as decision trees or logistic regression—and integrating human expert knowledge into the learning loop (top-down approach).

### E. Hardware Implementation and Complexity
Real-time processing at high data rates requires hardware acceleration via FPGAs. To reduce complexity, researchers should focus on online learning, dimensionality reduction/feature engineering, and model compression.

### F. Scaling: The Reality Gap
Most research is limited to simulations or small testbeds. Bridging the "reality gap" requires incorporating more physical parameters into simulators and conducting rigorous field tests to validate generalizability.

## VI. Conclusion
The survey demonstrates that ML and DL are revolutionizing optical communications by providing automated, high-performance solutions for nonlinearity compensation, OPM, and resource allocation across OFC, OCN, and OWC. While significant gains in BER and throughput have been documented, the field must transition toward transparent, hardware-efficient, and real-world validated implementations to fully realize its potential.
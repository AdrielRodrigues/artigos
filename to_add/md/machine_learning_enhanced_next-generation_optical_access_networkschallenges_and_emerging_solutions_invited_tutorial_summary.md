---
index_terms:
  - optical access networks
  - passive optical networks
  - machine learning
  - dynamic bandwidth allocation
  - transfer learning
  - federated learning
  - mobile fronthaul
  - concept drift detection
---

# Machine learning enhanced next-generation optical access networks—challenges and emerging solutions [Invited Tutorial]

## 1. Introduction
Optical access networks, particularly Passive Optical Networks (PON), are evolving toward capacities exceeding 100 Gbps to support diverse "immersive" services such as mixed reality (XR), holographic communication, and the Tactile Internet. These services introduce highly dynamic and heterogeneous traffic with stringent capacity, latency, and reliability requirements.

The authors argue that while machine learning (ML) is often seen as a solution for network management, its application in access networks faces steeper hurdles than in core or metro networks due to cost sensitivity, limited computational resources at the edge, high traffic dynamicity, and a lack of existing data acquisition infrastructure. ML is justified when physics-based models are unavailable (model deficit) or computationally prohibitive (algorithm deficit). This tutorial explores these challenges and introduces a Fast and Self-Adaptive (FSA) dynamic bandwidth allocation (DBA) scheme that utilizes reinforcement learning (RL) and transfer learning to support immersive human-to-machine (H2M) communications in next-generation mobile fronthaul.

## 2. Drivers and Future Trends
The push for ML in optical access is driven by several industry initiatives:
*   **Fifth Generation Fixed Network (F5G):** Promotes "Fiber To Everywhere/Everything" using a Management, Control, and Analytics (MCA) plane that leverages an AI engine to autonomously coordinate network resources across enhanced fixed broadband, guaranteed reliable experience, and full fiber connection dimensions.
*   **All-Photonics Network (APN):** An optical full-mesh network utilizing a photonic gateway (Ph-GW). ML is envisioned here for capacity and wavelength channel prediction to prevent contention and proactively tune transceivers.
*   **Network 2030:** Focuses on holographic-type communications (HTC) and multi-sense services, requiring distributed intelligence and ubiquitous fiber connectivity to synchronize volumetric data from multiple viewpoints.
*   **Last Meter Fiber Wireless Integration:** Combines PON with WiFi 6E or Optical Wireless Communication (OWC). Proposed architectures use ML at the central office to predict user demand and dynamically allocate resources via virtual access points.
*   **Optical Transport for Next-Generation Mobile Networks:** PON is a primary candidate for 6G mobile fronthaul due to cost and capacity benefits. Achieving 6G goals (>1 Tbps, microsecond latency) requires ML integration across all network layers.

## 3. Machine Learning Overview

### A. 21st Century Revival
The current resurgence of ML is attributed to four main drivers: the availability of big data from IoT and advanced monitoring; open-source software and hardware (specifically GPUs for parallel processing); the democratization of compute via cloud and multi-access edge computing; and significant financial investment from governments and industry.

### B. ML Terminology and Algorithm Classification
The authors distinguish between AI (simulating human behavior/reasoning) and ML (learning from data to perform tasks without explicit programming). ML is categorized into:
*   **Supervised Learning:** Uses labeled data for regression (continuous values) or classification (discrete classes).
*   **Unsupervised Learning:** Uses unlabeled data for clustering or anomaly detection.
*   **Semi-supervised Learning:** Combines a small amount of labeled data with larger unlabeled sets to improve accuracy.
*   **Reinforcement Learning (RL):** An agent learns optimal behavior via a policy to maximize rewards through environment interaction.
*   **Deep Learning:** A subset using artificial neural networks (ANNs) with multiple hidden layers to characterize complex, nonlinear patterns.

## 4. Machine Learning Challenges
Several key obstacles hinder the transition of ML from research to production in optical access:
*   **Availability of Representative Data:** Collecting and labeling high-quality data from deployed networks is expensive and technically difficult. Potential mitigations include Generative Adversarial Networks (GANs) for data augmentation, active learning, online learning, and transfer learning.
*   **Adaptability to Dynamic Environments:** "Concept drift" occurs when the distribution of deployment data differs from training data, rendering models inaccurate. Solutions include online learning, federated learning, and computationally efficient models that allow high-responsivity retraining.
*   **Explainability and Trust:** The "black box" nature of ML is problematic for high-reliability networks managed by domain experts. Explainable AI (XAI) aims to provide interpretable outputs based on metrics like stability, robustness, and reproducibility.
*   **Environmental Impact:** High computational complexity leads to significant carbon emissions. Sustainable AI focuses on energy-efficient hardware (e.g., TinyML microcontrollers) and computationally efficient models.
*   **Data Security and Privacy:** Risks include the manipulation of training data or extraction attacks. Federated learning is proposed as a defense because it keeps raw data local, sharing only model parameters.

## 5. Emerging ML Approaches

### A. Generative Adversarial Network (GAN)
GANs use two competing networks—a generator and a discriminator—to synthesize realistic data. In optical networks, they are used for network traffic synthesis, modeling fiber channels with impairments (e.g., chromatic dispersion), and improving security via anomaly detection and defense against adversarial attacks.

### B. Active Learning
Active learning reduces the need for large labeled datasets by allowing the model to proactively query an "oracle" for labels on the most informative samples. This has been applied to improve channel gain prediction in EDFAs and SNR estimation in flexible grid networks.

### C. Online Learning
This approach involves offline pre-training followed by continuous real-time updates during deployment. It is space and time efficient but requires robust mechanisms to detect and adapt to concept drift.

### D. Virtual (Data) and Real Concept Drift Detection
*   **Virtual/Data Drift:** Changes in input distribution that do not affect the decision boundary. 
*   **Real Concept Drift:** Changes the actual functional relationship between inputs and outputs (shifting the decision boundary). 
Detection methods include error rate monitoring, distance-based distributions of errors, or comparing model parameter updates in a federated learning setup.

### E. Explainable Artificial Intelligence (XAI)
XAI is split into model-agnostic (e.g., SHAP, LIME), which can be applied post hoc to any model, and model-specific (e.g., GRAD-CAM for DNNs). In optical networks, XAI has been used to identify features relevant to Quality-of-Transmission (QoT) estimation and to localize network failures.

### F. Sustainable AI
This focuses on reducing the carbon footprint through energy-efficient hardware like TinyML (computing on microcontrollers), which consumes orders of magnitude less power than GPUs and improves privacy by performing inference at the edge.

### G. Federated Learning
Federated learning enables decentralized devices to collaboratively train a global model by sharing local parameters rather than raw data. In PONs, this is supported by bandwidth slicing for parameter transmission. Research shows it significantly reduces convergence time—up to 80% in some resource allocation scenarios—by leveraging shared knowledge across the federation.

### H. Transfer Learning
Transfer learning re-uses parameters from a source model trained on one task to optimize a target model on a different but related task. This is particularly useful for failure detection (where failure data is scarce) and reducing training time for equalizers in short-reach optical links.

## 6. Self-Adaptive Mobile Fronthaul Bandwidth Allocation

### A. Fast Self-Adaptive DBA for Mobile Fronthaul
The authors propose a Fast Self-Adaptive DBA (FSA-DBA) scheme to manage the shared uplink bandwidth of PONs used as mobile fronthaul (MFH). The goal is to optimize the allocated bandwidth ($T_{grant}$) without prior knowledge of traffic patterns.
*   **Self-adaptive mechanism:** Uses RL where the reward ($R$) is defined as the negative latency at the ONU-RU. A $Q$-value function is updated iteratively to associate specific grants with rewards, optimizing the decision for each unit.
*   **Fast exploration:** To avoid the slow convergence of standard RL, transfer learning is used. The system identifies a pre-existing source knowledge set ($Q_{source}$) most similar to the current target environment and restricts the search space for $T_{grant}$ to a neighborhood around that known optimum, drastically speeding up convergence.

### B. Performance Evaluation
Simulations using a 10 km 10G-EPON with various traffic distributions (Exponential, Generalized Pareto, Gamma) demonstrate that FSA-DBA achieves the lowest uplink latency (~200 $\mu$s), outperforming both baseline and cooperative DBA schemes. Regarding learning rates, empirical results show that while RL alone can eventually find an optimal decision, incorporating transfer learning reduces the required iterations from hundreds to just a few tens.

## 7. Summary
The paper highlights the necessity of ML in next-generation optical access networks to handle the complexity of immersive services and 6G fronthaul. It identifies critical gaps in data availability, adaptability, and explainability, presenting emerging solutions like GANs, Federated Learning, and XAI. The proposed FSA-DBA scheme serves as a practical application of these concepts, demonstrating that combining RL with transfer learning allows for rapid, self-adaptive bandwidth allocation that meets the stringent low-latency requirements of future mobile networks.
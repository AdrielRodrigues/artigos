---
index_terms:
  - federated learning
  - fiber optic sensors
  - biosensing
  - gaussian process regression
  - figure of merit
  - surface plasmon resonance
  - data privacy
---

# Leveraging Federated Learning For Optimizing Fiber Optic Sensor Design For Biodetection

## Abstract
This research proposes a framework using federated learning (FL) to optimize the design of plasmonic-based fiber optic sensors (FOS) for biosensing. The primary goal is to enhance the Figure of Merit (FOM) and generalize machine learning (ML) models across diverse datasets without requiring the centralization of raw data, which is critical for maintaining privacy in medical applications. By employing Gaussian Process Regressor (GPR) models for local training and aggregating parameters collaboratively, the approach seeks to improve sensing proficiency while adhering to strict data privacy regulations.

## Introduction
High-performance optical biosensors are vital for clinical diagnostics, drug discovery, and environmental monitoring. Their effectiveness is measured by sensitivity, accuracy, specificity, response time, and reusability. Surface plasmon resonance (SPR) in fiber optic sensors is particularly advantageous due to flexibility and remote-sensing capabilities.

To enhance performance, the authors highlight the use of 2D materials like molybdenum disulfide ($\text{MoS}_2$), which improves sensitivity through the optimization of radiation damping. The critical metric for evaluation is the Figure of Merit (FOM), defined as the product of sensitivity and accuracy. Optimizing FOM requires precise selection of incident light wavelength ($\lambda$) and metal layer thickness ($d_m$). Because traditional simulations with small step sizes are computationally expensive, ML provides a viable alternative for predicting optimal design parameters.

The authors note that while centralized ML can predict outcomes on unseen data—demonstrated in their previous work where GPR models accurately matched actual FOM trends—medical data is often too sensitive to share centrally. Consequently, federated learning is introduced as a decentralized paradigm that allows model refinement by sharing trained parameters rather than raw data, thus ensuring privacy and scalability across distributed sensor nodes.

## Literature Review
Traditional SPR sensor optimization relies on systematic simulation-based exploration of design parameters, which suffers from computational inefficiency and privacy risks during data aggregation. Recent shifts toward ML have introduced supervised learning to predict sensor performance. Notable examples include the use of ML for tilted fiber Bragg grating (TFBG)-assisted sensors, photonic crystal fiber (PCF) designs via genetic algorithms or the Taguchi approach, "SmartSPR" adaptive sensors, and LSPR sensors for SARS-CoV-2 detection.

The authors reference their own previous GPR-based optimization, which yielded an 11% improvement in FOM (reaching a peak of $6526.23 \text{ RIU}^{-1}$) at a wavelength of $1099.343\text{ nm}$. They found that a smaller light wavelength step size ($0.001\text{ nm}$) was crucial for enhancing FOM via Optical Path Difference (ORD) manipulation. Further validation with larger datasets improved the Mean Absolute Error (MAE) to $65.69 \text{ RIU}^{-1}$ and an $R^2$ near 0.9. Despite these gains, they argue that traditional ML requires centralized data; thus, FL is necessary to harness collective intelligence from distributed networks without exposing sensitive information.

## Methodology
The proposed methodology integrates simulation-based optimization with a privacy-preserving FL framework:

*   **Parameter Optimization:** Systematic variation of incident light wavelength and material choices to maximize sensitivity and accuracy.
*   **Simulation Modeling:** Using simulations to predict sensor behavior across different environmental factors and analyte concentrations.
*   **ML Integration:** Applying supervised learning (specifically GPR) to analyze simulation data and develop predictive models for sensor performance.
*   **Federated Learning Implementation:** Enabling collaborative training across distributed nodes. This allows multiple entities to contribute to a generalized model without centralizing their local datasets, ensuring security and scalability in biosensing applications.

## Federated Learning for Sensor Design Optimization
The authors detail a five-step workflow for applying FL to sensor optimization:

1.  **Data Partitioning:** Sensor data from different environments or sources are kept in decentralized datasets (e.g., FOS dataset 1, 2) to ensure regulatory compliance.
2.  **Local Model Training:** Each node trains a local GPR model. Models must be evaluated for $R^2$ and RMSE; low accuracy at a specific site requires hyperparameter tuning to prevent the degradation of the eventual global model.
3.  **Collaborative Model Aggregation:** Local GPR parameters are combined into a refined global model using weighted averaging, secure multiparty computation, or differential privacy. To handle data heterogeneity (differences in data distribution between nodes), Personalized Federated Learning (PFL) can be utilized to tailor models to specific client attributes.
4.  **Parameter Updates:** Model parameters are updated based on the reliability or quality of the local contributions.
5.  **Global Model Refinement:** The global GPR model is updated to reflect collective knowledge while remaining adaptable to heterogeneous data characteristics.

## Implications and Challenges
Integrating FL into FOS design addresses critical regulatory and privacy concerns in medical contexts by keeping raw data on local devices. However, several challenges remain:
*   **Algorithmic Innovation:** There is a need for advanced FL algorithms that specifically target sensor optimization, including better secure aggregation and differential privacy techniques.
*   **Data Heterogeneity:** Robust strategies are required to manage varying data quality and distributions across different nodes to ensure model convergence.
*   **Real-world Validation:** The transition from theoretical frameworks to practical, real-world biosensing implementations is necessary to validate the effectiveness of this decentralized approach.

## Conclusion
The paper proposes an innovative combination of GPR and federated learning to optimize fiber optic sensors for biosensing. This approach overcomes the trade-off between the need for large, diverse datasets for model generalization and the requirement for strict data privacy. By sharing only model parameters, the framework enables the creation of generalized sensor designs across different geographical locations. Future research will focus on reducing communication overhead, improving aggregation mechanisms, and integrating FL with evolutionary algorithms and reinforcement learning to further refine sensor performance.
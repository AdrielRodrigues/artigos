---
index_terms:
  - TWDM-PON
  - hybrid deep learning
  - performance prediction
  - Gradient Boosting Regression
  - Multi-Layer Perceptron
  - bit error rate
  - Q-factor
  - optical access networks
---

# A Hybrid Deep Learning Approach for Performance Prediction in Optical Communication Systems Based on PON Scenarios

## Abstract
The paper proposes a hybrid deep learning (DL) framework to predict key performance indicators (KPIs)—specifically the Q-factor, receiver sensitivity, and bit error rate (BER)—for asymmetric 160/80 Gbps Time and Wavelength Division Multiplexed Passive Optical Networks (TWDM-PON). To address the limitations of physics-based models in capturing nonlinear stochastic behaviors, the authors integrate Gradient Boosting Regression and Multi-Layer Perceptron (MLP) models into an ensemble structure. Using a synthetic dataset of 1000 samples reflecting various distances, power levels, and noise conditions, the framework achieves high predictive accuracy ($R^2 > 0.94$), offering a computationally efficient alternative to traditional optical simulations for next-generation access networks.

## 1. Introduction
Modern internet demands have pushed passive optical networks (PONs) toward higher capacities, evolving from GPON and XG-PON toward NG-PON2 (TWDM-PON). While physics-based models are standard, they struggle with the complexity of modern networks. The authors note that while AI/DL has been applied to PON fault management and Quality of Transmission (QoT) estimation, many existing models lack generalization when network configurations change.

The primary contributions of this work include:
*   Developing a hybrid DL framework combining Gradient Boosting and MLP regressors specifically for an asymmetric 160/80 Gbps TWDM-PON system with 512 users over 65 km, adhering to ITU-T G.989.1 specifications.
*   Introducing a method that predicts Q-factor, BER, and receiver sensitivity for both upstream (U/S) and downstream (D/S) channels with high precision ($R^2 > 0.94$).
*   Demonstrating that the model can generalize physical-layer performance assessment by learning from a dataset that incorporates attenuation, noise buildup, and signal deterioration.

## 2. Materials and Methods
The proposed methodology follows a pipeline of data generation, preprocessing, ensemble modeling, and evaluation to predict KPIs under varying transmission conditions.

### 2.1. Parameter Definition
To simulate real-world fiber deployment, the study defines:
*   **Transmission Distances:** Discrete values from {0, 10, 20, 40, 45, 70, 75} km.
*   **BER Calculation:** Derived from Gaussian noise statistics using the complementary error function based on the Q-factor: $BER = \frac{1}{2} erfc(Q/\sqrt{2})$.
*   **Receiver Sensitivity:** Modeled as a linear decrease relative to distance, inclusive of stochastic perturbations.
*   **Power Level and Noise Factor:** Power is simulated between -5 and 5 dBm; the noise factor is randomly selected from a uniform distribution [0.1, 2.0].

### 2.2. Synthetic Dataset Generation
A dataset of 1000 synthetic samples was generated using Python 3.11.9. Each sample contains input parameters (distance, power level, noise factor) and target KPIs (Q-factor, BER, and receiver sensitivity for both upstream and downstream channels).

### 2.3. Data Preprocessing
To ensure model stability:
*   **Logarithmic Transformation:** BER values were converted to a base-10 logarithmic scale to handle their exponential nature.
*   **Feature Engineering:** Second-order interaction terms were created by squaring the Power Level and Noise Factor.
*   **Data Splitting:** The dataset was divided into training (80%) and testing (20%) sets using stratified random sampling.

### 2.4. Model Design and Training
The framework employs two primary regressors for each of the six target variables: a Multi-Layer Perceptron (MLP) and a Gradient Boosting Regressor (GBR).
*   **Pipelines:** StandardScaler was used for linear metrics (Q-factor, sensitivity), while MinMaxScaler was applied to BER predictions. 
*   **Optimization:** GridSearchCV with 5-fold cross-validation determined optimal hyperparameters (e.g., hidden layer sizes for MLP and learning rates/depth for GBR).
*   **Ensemble Fusion:** A weighted average is used for final predictions: $y = 0.6 \cdot \hat{y}_{GBR} + 0.4 \cdot \hat{y}_{MLP}$.
*   **Baselines:** The model was compared against Linear Regression, Support Vector Regression (SVR), and Random Forest.

### 2.5. Evaluation Metrics
The framework's accuracy is quantified using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the coefficient of determination ($R^2$).

## 3. Results
The hybrid model was evaluated on its ability to replicate signal degradation trends associated with distance, attenuation, and noise.

### 3.1. Traditional Optical Results vs. Hybrid DL Predictions
Comparisons between traditional physics-based simulations (using EDFA and FBG components) and the DL predictions show:
*   **Trend Alignment:** Both systems correctly identify that as distance increases from back-to-back (BtB) to 70 km, signal quality drops (Q-factor decreases, BER increases).
*   **Prediction Biases:** The DL model slightly overestimates Q-factors in BtB scenarios due to insufficient noise representation in training data for ideal conditions. Conversely, it provides more conservative (more negative) receiver sensitivity estimates at longer distances, which the authors argue provides a necessary safety margin for system designers.

### 3.2. Performance of the Hybrid Deep Learning Model
The hybrid model demonstrated superior performance across all targets:
*   **Accuracy:** All metrics achieved $R^2 > 0.94$, with receiver sensitivity being the most predictable ($R^2 > 0.99$).
*   **Channel Differences:** Upstream channels exhibited slightly higher error metrics than downstream channels due to increased vulnerability to noise and system fluctuations.
*   **Baseline Comparison:** The hybrid model significantly outperformed Linear Regression, SVR, and Random Forest in terms of RMSE (0.76) and MAE (0.58).
*   **Overfitting Mitigation:** Generalization was ensured through 80/20 splitting, cross-validation, L2 regularization for the MLP, and depth constraints for GBR.
*   **Weight Optimization:** Sensitivity analysis determined that a weight ratio of 0.6 (GBR) to 0.4 (MLP) provided the optimal balance between stability and nonlinear learning.

## 4. Discussion
The results validate the hypothesis that combining multiple DL regressors improves prediction accuracy over single-model or purely physics-based approaches. 

Key points include:
*   **Computational Efficiency:** Unlike iterative numerical simulations, which are computationally expensive and time-consuming during parameter sweeps, the hybrid model shifts the load to the training phase. Once trained, inference is near real-time, facilitating rapid "what-if" scenario analysis.
*   **Comparative Standing:** Compared to prior literature, this work focuses on a significantly higher capacity (160/80 Gbps) and a larger splitting ratio (512), demonstrating better scalability for high-density user environments.
*   **Physical Fidelity:** The model effectively captures the underlying physics of optical attenuation and chromatic dispersion without requiring explicit physical equations during prediction.

## 5. Conclusions
The authors conclude that the hybrid DL framework is a robust alternative to traditional simulation methods for predicting Q-factor, BER, and receiver sensitivity in TWDM-PON systems. By merging GBR's stability with MLP's flexibility, the model achieves high precision ($R^2 > 0.94$) and computational efficiency. This approach reduces reliance on expensive hardware setups and speeds up design cycles. The findings suggest that such data-driven intelligence is highly applicable to FTTH/FTTB networks and 5G mobile fronthaul/backhaul infrastructures, marking a shift toward intelligent, real-time network optimization in the era of Industry 4.0.
---
index_terms:
  - SDM-EONs
  - RMCSA problem
  - intercore crosstalk
  - machine learning optimization
  - bandwidth blocking probability
  - litcore thresholds
  - SWARM algorithm
  - spectrum wastage
---

# Machine learning aided optimization for balanced resource allocations in SDM-EONs

## 1. Introduction
The paper addresses the Routing, Modulation, Core, and Spectrum Assignment (RMCSA) problem in Space Division Multiplexed Elastic Optical Networks (SDM-EONs). The primary technical challenge is intercore crosstalk (XT), which degrades the Quality of Transmission (QoT). There is a fundamental trade-off: higher-order modulations improve spectral efficiency but are more sensitive to XT and have shorter transmission reaches.

The authors propose two main contributions:
1. A generalized machine learning (ML) aided threshold optimization strategy that optimizes litcore thresholds (the maximum number of adjacent cores allowed to be occupied on overlapping spectra) for any RMCSA algorithm or network model.
2. The Spectrum-Wastage-Avoidance-based Resource Management (SWARM) algorithm, which balances spectrum utilization and XT by quantifying "spectrum wastage."

## 2. Related Work
The authors review existing RMCSA approaches, noting a shift toward complex algorithms and joint core-spectrum selection to mitigate XT. They highlight the use of multipath routing and dynamic XT computation over worst-case estimations. Regarding ML, they note its application in QoT estimation but emphasize that data scarcity remains a significant barrier. The paper proposes using model tuning and simulated data to overcome these training constraints.

## 3. Network Model
The network operates on a flexible grid (12.5 GHz granularity) with coherent transceivers at a constant baud rate of 28 GBaud. Each carrier occupies three frequency slots (FSs). The study considers multicore fiber (MCF) geometries of 3, 7, and 13 cores, assuming XT only occurs between adjacent cores.

Key models include:
- **XT Calculation:** Average XT ($\text{XT}_{\mu}$) is calculated via coupled-power theory based on the number of litcores ($\gamma$), route length ($l$), and a design parameter ($h$).
- **Transmission Reach:** Maximum reach ($L_{max}$) depends on the modulation format and $\gamma$. As $\gamma$ increases, $L_{max}$ decreases.
- **Litcore Thresholds ($\gamma^d_{\max}$):** To guarantee QoT, the authors introduce a set of thresholds (ST) for each modulation $d$, limiting the number of adjacent cores that can be occupied on overlapping spectra.

## 4. Machine-Learning-Aided Optimization
This section describes a framework to find the optimal set of litcore thresholds ($\gamma_*^d$) to minimize Bandwidth Blocking Probability (BBP).

### A. Data Generation and Storage
The process involves randomly generating ST samples, simulating their resulting BBPs using a network simulator, and training an ML model on these pairs. To avoid "zero BBP" cases that hinder learning, the authors use higher-than-normal traffic loads during data generation to make differences between STs more apparent.

#### 1. Data Processing and Storage
To reduce bias and redundancy, a window $\tau$ is used in a data analyzer block to limit the number of training samples within a specific range of labels, ensuring a diverse and information-rich dataset.

#### 2. Data Analysis
Using the German (DT) and European (EURO) topologies, the authors observe that BBP variation relative to thresholds is partially linear and nonlinear. The optimal threshold is typically not an extreme value (neither zero nor maximum).

### B. Machine Learning Platform
The authors treat the search for optimal thresholds as an approximation problem.

#### 1. Model Tuning
To prevent overfitting and underfitting, the authors employ a two-step method: dividing training data into validation sets to track loss and performing hyperparameter searches (e.g., learning rate). They use early stopping and callbacks in deep neural networks (DNNs) to halt training when performance plateaus.

#### 2. Comparison of Machine Learning Models
The study compares untuned DNN (uDNN), tuned DNN, k-nearest neighbors (KNN), linear regression (LIN), lasso regression (LAS), and support vector regression (SVR). The **tuned DNN** achieved the lowest root mean squared error (RMSE) and most accurately predicted BBPs. This model is combined with GridSearchCV to identify the optimal ST ($\text{S}_*^{\gamma}$).

## 5. Definitions and Important Concepts
This section establishes the mathematical basis for the SWARM algorithm.

### A. Spectrum Requirement and Slice Window
Spectrum requirement $\beta^{m,d}$ is defined by the datarate $M_m$, modulation efficiency $\eta_d$, and grid granularity $\delta$. An "available slice window" must be free and satisfy both the XT constraints of the new connection and the QoT requirements of existing connections on adjacent cores.

### B. Core-Groups
Cores are grouped by their number of adjacent cores ($\alpha$). For example, in a 7-core fiber, the outer six cores form one group ($G_3$, $\alpha=3$) and the center core forms another ($G_6$, $\alpha=6$).

### C. SWARM Coefficient
The authors quantify the trade-off between utilization and XT through two definitions:
- **Allowed Litcores ($\gamma^d$):** The number of adjacent cores that can be lit while still maintaining a transmission reach $T_d^\gamma \ge l$.
- **Spectrum Wasted:** The amount of spectrum on adjacent cores rendered unusable because they cannot be occupied without violating the XT constraints of the chosen modulation.

The **SWARM coefficient ($\sigma_{c,n}^d$)** calculates the total spectrum "cost" (assigned slices + wasted slices):
$$\sigma_{c,n}^{d} = \begin{cases} (\alpha - \gamma^{d} + 1)\beta^{m,d} + g_{b}, & \text{if } \alpha > \gamma^{d} \\ \beta^{m,d} + g_{b}, & \text{otherwise.} \end{cases}$$

### D. Illustrative Example
An example demonstrates that choosing a core in a lower core-group (fewer neighbors) or a more XT-tolerant modulation reduces the SWARM coefficient, thereby preserving more network resources for future requests.

## 6. Spectrum-Wastage-Avoidance-based Resource Management
The SWARM algorithm aims to minimize the SWARM coefficient during resource allocation. The process is as follows:
1. Iterate through shortest paths (SPs).
2. For each path, identify modulations whose reach $T_d^{\gamma^*}$ permits the distance.
3. Search cores starting from the lowest core-group ($\alpha$ smallest) to minimize potential wastage.
4. Within a core, use a first-fit policy to find an available slice window.
5. Select the resource combination that yields the minimum $\sigma$.

## 7. Simulation Results
The authors compare SWARM and other algorithms (xtFF, xtFM, P-XT) with and without ML optimization across DT and EURO topologies using various core counts (3, 7, 13).

**Key Findings:**
- **BBP Reduction:** ML-aided versions of all algorithms outperform their non-ML counterparts, reducing BBP by up to three orders of magnitude.
- **Algorithm Performance:** SWARM and pSWARM (which adds Prioritized Path Selection) consistently outperform other RMCSAs. SWARM-ML provides the best overall performance in most scenarios.
- **Execution Time:** ML-aided variants often execute faster because optimized thresholds increase resource availability, reducing the time spent searching for valid slots.
- **Blocking Analysis:** The authors distinguish between Spectrum Blocking (SBP) and QoT Blocking (QBP). ML optimization primarily reduces QBP by balancing the modulation/XT trade-off.
- **Modulation Distribution:** ML-aided versions show a more judicious balance, slightly increasing the use of higher modulations for short paths while effectively utilizing lower modulations for longer paths.

## 8. Concluding Remarks
The paper concludes that optimizing litcore thresholds via ML is a general solution applicable to any RMCSA algorithm and significantly improves network performance. The proposed SWARM algorithm further enhances this by explicitly avoiding spectrum wastage, resulting in superior bandwidth blocking probabilities across various fiber geometries and topologies.
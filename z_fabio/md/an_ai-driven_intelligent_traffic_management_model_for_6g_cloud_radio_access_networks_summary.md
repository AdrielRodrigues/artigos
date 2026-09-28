---
index_terms:
  - 6G Cloud Radio Access Networks
  - C-RAN traffic management
  - XGBoost prediction
  - network congestion mitigation
  - resource allocation strategies
  - job scheduling optimization
---

# An AI-Driven Intelligent Traffic Management Model for 6G Cloud Radio Access Networks

## Abstract
The paper presents a novel Cloud Radio Access Network (C-RAN) traffic analysis and management model designed to predict RAN traffic congestion and mitigate its impact. The model classifies heterogeneous RAN traffic into specific states based on bandwidth usage and job execution time, employing a cloud-based management system to allocate resources. Experimental results indicate that the proposed model improves bandwidth utilization by 17.07% and reduces job execution latency by up to 18%.

## I. Introduction
With the rise of 6G, IoT, and UAV networks, C-RAN traffic is increasing significantly. While C-RAN offers network virtualization and customization, it creates a conflict between customers (who desire minimal latency) and service providers (who aim for maximum bandwidth utilization and low operational costs). To address this, the authors propose the Traffic Management model for 6G Cloud Radio Network (TM-CRN). This model proactively analyzes traffic to detect potential congestion and filters "contention-suspected" traffic from normal traffic. Key contributions include:
1. A RAN traffic analyzer that identifies probable congestion while reserving physical resource capacity.
2. A classification system for RAN traffic states used to inform scheduling and resource mapping.
3. The implementation of the TM-CRN model, verified against Quality of Service (QoS) metrics and compared with existing methods.

## II. TM-CRN Model
The proposed architecture consists of antennas, radios, and baseband units (BBUs) that generate heterogeneous network traffic. In this C-RAN setup, BBUs act as centralized control stations connected to Remote Radio Frequency Units (RFUs). The cloud platform is divided into three functional units:
*   **RAN Traffic Analyser Unit (RTAU):** Uses an AI-driven predictor and pre-estimated thresholds to identify probable traffic congestion.
*   **Traffic Management Unit (TMU):** Segregates network traffic into distinct states (Fast jobs, Stragglers, Network Hogs, and Heavy jobs) based on execution time and bandwidth consumption. It then applies optimal scheduling and mapping strategies among $Z$ resource allocation options to minimize latency and CPU idle time.
*   **Cloud Services Unit (CSU):** Executes the job requests through storage, computing, and networking services. The CSU provides feedback data (resource usage, job types) back to the RTAU to refine the AI predictor's training samples.

## III. RAN Traffic Analysis
The RTAU utilizes an Extreme-Gradient Boosting (XGBoost) algorithm for traffic prediction. 
*   **Prediction Mechanism:** The predictor employs $\ell$ base learners (decision trees). It minimizes an objective function $L_t$ that consists of a loss term (reducing prediction errors) and a regularization term ($\Psi$) to prevent overfitting by controlling tree complexity based on leaf count ($K$) and split weights ($w$). Optimization is achieved via Taylor expansion to calculate exact losses for each decision tree.
*   **Congestion Detection:** The system compares live traffic deviation $(\mathcal{T}r_{\sigma})$ against a threshold over a specific time interval ($\Delta t$). A traffic status value $\Xi^{status}$ of '1' indicates congestion, '-1' indicates sub-normal traffic, and '0' indicates normal traffic.
*   **Congestion Constraints:** Congestion is formally identified if the aggregated demand for bandwidth (BW), CPU (C), or memory (Mem) exceeds the available capacity across physical machines (PMs) over a duration exceeding the threshold timeperiod ($\Delta t^{thr}$). 
*   **Handling:** Anticipated congestion triggers traffic diversion across multiple pathways to PMs reserved for heavy workloads. Sub-normal traffic is consolidated onto a minimum number of PMs to save resources.

## IV. Cloud-Based Traffic Management
The TMU classifies live RAN traffic into five states based on bandwidth demand ($Nt_i^{BW}$) and execution time ($Nt_i^{Et}$):
1.  **Light jobs ($\mathcal{T}^{Lit}$):** Low bandwidth, low execution time.
2.  **Stragglers ($\mathcal{T}^{Stg}$):** Low bandwidth, high execution time.
3.  **Network Hogs ($\mathcal{T}^{Hog}$):** High bandwidth, low execution time.
4.  **Heavy jobs ($\mathcal{T}^{Hvy}$):** High bandwidth, high execution time.
5.  **Average jobs ($\mathcal{T}^{Avg}$):** All other traffic.

**Resource Allocation Strategies:**
*   **Light jobs:** Allocated via First-Come First-Serve (FCFS) scheduling.
*   **Stragglers:** Mapped to virtual nodes on PMs with the highest CPU and memory capacity to facilitate necessary I/O operations.
*   **Network Hogs:** Managed via hybrid scheduling; they are executed in parallel with stragglers, utilizing resources during the stragglers' I/O-induced idle times.
*   **Heavy jobs:** Distributed across multiple high-capacity PMs to meet their large resource demands.
*   **Average jobs:** Sorted by deadline and priority, then mapped to servers sorted by decreasing processing speed to minimize execution time for the most urgent requests.

These allocations are subject to constraints ($C_1 - C_6$) that ensure each job is assigned to a single virtual node on one PM and that the requested resources do not exceed the available capacity of the VN or the underlying PM.

## V. Operational Design and Complexity
The system operates by initializing lists of jobs, VNs, and PMs, followed by a continuous loop of predicting traffic load for the next interval, computing deviation, analyzing congestion status, classifying traffic states, and applying allocation formulas. The overall time complexity is $\mathcal{O}(PMT)$, where $P$ is the number of physical machines, $M$ is the number of RAN requests, and $T$ represents the time intervals.

## VI. Performance Evaluation and Discussion
### A. Experimental Set-Up and Dataset
The simulation used dual Intel Xeon Silver 4114 CPUs (40 cores) with 128 GB RAM on Ubuntu 16.04 using Python 3.1. The environment simulated IBM server configurations for PMs and Amazon VM instances for VMs. Datasets included call detail records and a YouTube mobile streaming dataset. TM-CRN was compared against FMLA (Federated Meta-Learning Approach), JUFO (Joint UE and Fog Optimization), and OSC-MC (Online Secure Communication Model Cloud).

### B. Numerical Results
*   **Traffic Distribution:** Varying bandwidth and execution time thresholds significantly altered the percentage of traffic falling into each state, confirming the sensitivity of the classification model.
*   **Prediction Accuracy:** The XGBoost predictor showed low Mean Squared Error (MSE) and Mean Absolute Error (MAE). It outperformed FMLA-d specifically in terms of reducing estimation errors in certain scenarios (e.g., Trentino dataset) due to its pattern learning capabilities.
*   **Congestion and Bandwidth:** TM-CRN reduced congestion by up to 10.15% compared to OSC-MC. Bandwidth utilization improved by 17.07% over JUFO, 17.31% over random-fit, and 18% over first-fit.
*   **Latency and Execution Time:** Job execution latency was reduced (relative to FCFS) by between 18.37% and 27.12% depending on threshold values. This reduction is attributed to the parallelism enabled by executing "Network Hogs" during "Straggler" I/O idle times. While TM-CRN takes longer than an "Optimal" case (due to the overhead of prediction and analysis), it significantly outperforms existing heuristic and meta-learning approaches.

## VII. Conclusion
The proposed TM-CRN model effectively manages RAN traffic in 6G environments by combining XGBoost-based congestion prediction with a state-based classification and allocation mechanism. By exploiting parallelism between different job types (specifically hogs and stragglers), the model maximizes bandwidth utilization and minimizes execution latency compared to state-of-the-art methods.
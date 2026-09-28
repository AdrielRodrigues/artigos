---
index_terms:
  - 6G networks
  - edge intelligence
  - network traffic prediction
  - Long Short-Term Memory (LSTM)
  - cloud-native computing
  - Kubeflow
  - eBPF packet tracing
  - encoder-decoder architecture
---

# Edge Intelligence in Softwarized 6G: Deep Learning-enabled Network Traffic Predictions

## Abstract
The paper proposes an edge-native framework for predicting network traffic data flows within the context of 6G visibility services. Because network traffic in dynamic cloud-native environments is often random and sporadic, the authors employ a deep learning prognosis model based on Long Short-Term Memory (LSTM) encoder-decoders. This model is trained on multivariate time-series data collected from edge $\mu$-boxes within a testbed, with results validated against ground truth observations using RMSE and $R^2$ metrics.

## I. Introduction
6G aims for an AI-native, hyper-flexible architecture that integrates Artificial Intelligence (AI), Software-Defined Networking (SDN), Network Function Virtualization (NFV), and cloud-native computing. By utilizing DevOps strategies to decompose hardware services into microservices at the network edge, operators can better meet KPIs for latency and data rates. However, predicting non-linear, aperiodic time-series traffic data remains difficult due to three primary challenges:
1. **Resource Constraints**: Limited storage and computation available at the network edge compared to growing IoT traffic volumes.
2. **Data Quality**: The prevalence of unlabeled raw time-series data and sudden traffic shifts caused by geographic or infrastructure events.
3. **Infrastructure Lag**: Existing networks are not optimized for AI, often leading to resource depletion when deploying AI services.

To address these, the authors propose an edge intelligence framework using the OpenFlow over Trans-Eurasia Information Network (OF@TEIN++) Playground. The primary contributions include a DL-based method for predicting traffic statistics at edge devices, a pipeline for collecting raw traffic flow data via visibility centers, and the use of Kubeflow for orchestrating the training and deployment of the prognosis model.

## II. Experimental Model Description
This section details the infrastructure used to collect the dataset and deploy the AI service.

### A. OF@TEIN Playground Overview
The OF@TEIN playground (OPG) is an SDN-enabled multi-site cloud interconnecting National Research and Education Networks (NRENs). It features "SmartX PG Towers" that manage distributed hyper-converged cloud-native boxes via three operational centers: Provisioning and Orchestration (P+O), Visibility (V), and Intelligence (I).

### B. K8s Edge Cluster over OF@TEIN Playground
The authors deployed a Kubernetes (K8s) edge cluster where the P+O center at the GIST site acts as the master for orchestrating AI microservices via Kubeflow. The edge $\mu$-boxes serve as K8s worker nodes, equipped with three network interfaces (two wired for control/data and one wireless). These boxes utilize a mesh-style networking configuration coordinated by SDN to support containerized functions.

### C. Network Traffic Data Set Collection
Traffic statistics are gathered using extended Berkeley Packet Filtering (eBPF) through the IO Visor tool, which allows for low-CPU overhead packet tracing within the kernel. A custom software implementation accumulates raw packets from $\mu$-box interfaces, and Apache Spark with Scala is used to process these into five multivariate statistical features. This processed data is streamed via Apache Kafka and stored in a MongoDB NoSQL database.

## III. Kubeflow-based AI Service Design
The authors utilize Kubeflow on the K8s cluster to manage the machine learning lifecycle, including data preparation and model tuning, leveraging high-performance computing (HPC) capabilities for auto-scaling ML workloads.

### A. DL-based Data Prediction Model
The authors argue that traditional Recurrent Neural Networks (RNNs) fail to capture long-term dependencies in time-series (TS) data due to the vanishing gradient problem. To solve this, they propose a sequence-to-sequence (s2s) model based on LSTM cells.

#### 1) LSTM Cell
LSTM cells use three specific gates—forget, input, and output—to regulate the flow of information into the cell state (the memory unit). This mechanism allows the model to learn long-term correlations across lengthy multivariate sequences by distributing error derivatives through sums during back-propagation over time.

#### 2) LSTM cell-based Encoder-Decoder Model
The proposed architecture uses a single-layer encoder-decoder structure:
*   **Encoder**: Processes a set of past observations (input sequence $\mathcal{X}_i$) to create an encoded temporal representation.
*   **Decoder**: Uses a repeat vector and the encoder's cell state as initial representations to reconstruct the target output sequences ($\mathcal{Y}_o$) for a future horizon window.

The model is optimized by minimizing the Huber loss function, which provides a robust error metric by switching between squared loss (for small errors) and absolute loss (for large errors) based on a threshold $\tau = 1$.

## IV. Experimental Results Analysis
The model was evaluated using one month of multivariate network flow data (43,000 records at 5-minute intervals), split into 65% training and 35% testing sets.

**Implementation Details**:
*   **Frameworks**: TensorFlow, Keras, and Scikit-learn on Kubeflow.
*   **Configuration**: 100 LSTM cells per layer; min-max normalization to range $[-1, 1]$.
*   **Windowing**: A lookback period of 20 hours was used to predict the subsequent 10 hours.
*   **Training**: Batch size of 32, 40 epochs, Adam optimizer, and a "Learning Rate Schedule" callback for dynamic adjustment.

**Findings**:
*   **Convergence**: Loss curves indicated that training and validation losses converged after epoch 20, suggesting no significant overfitting.
*   **Prediction Accuracy**: The model accurately predicted the trends for average (mean), minimum, and standard deviation of databytes. While total traffic bytes were also predicted, they exhibited lower accuracy than the other four statistical features.
*   **Performance Metrics**: Results showed $R^2$ values close to 1 and RMSE values close to 0 for most features, confirming high predictive precision. Specifically, predicting average, minimum, maximum, and standard deviation was more successful than predicting total databytes (which had a higher RMSE of 231.64 and lower $R^2$ of 0.686).

## V. Conclusion
The paper demonstrates an intelligent prognosis technique for 6G edge traffic using an LSTM-based seq2seq model deployed via Kubeflow on a K8s cluster. By leveraging real-time data from $\mu$-boxes in the OF@TEIN++ testbed, the authors successfully predicted multivariate traffic characteristics over a 10-hour horizon. Future research will focus on automating network resource scaling based on these traffic predictions.
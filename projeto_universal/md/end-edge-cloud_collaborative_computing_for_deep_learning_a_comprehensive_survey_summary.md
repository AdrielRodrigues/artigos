---
index_terms:
  - end-edge-cloud collaboration
  - deep learning models
  - model compression
  - model partitioning
  - knowledge transfer
  - federated learning
  - early exiting
---

# End-Edge-Cloud Collaborative Computing for Deep Learning: A Comprehensive Survey

## I. Introduction
Deep Learning (DL) performance increases with model size, but large pre-trained foundation models (e.g., GPT-3, PaLM) impose massive computing and storage demands that exceed the capabilities of edge nodes and end devices. While cloud centers provide the necessary resources, they suffer from high communication latency, instability in lifelong learning/adaptation due to network interruptions, and significant data privacy risks.

Edge AI—deploying models closer to the data source—mitigates these issues but is limited by individual device constraints. The authors argue for an **end-edge-cloud computing paradigm** that integrates all three layers to achieve real-time, scalable, and secure DL services. This survey differentiates itself from "AI for end-edge-cloud" (using AI to optimize the network) by focusing on "end-edge-cloud for AI," covering the entire model lifecycle: training, inference, and updating.

## II. End-Edge-Cloud Collaborative Computing for Deep Learning
The authors analyze collaboration through three primary dimensions: data, model, and computing power.

### A. Data Dimension
Collaboration is categorized by the level of abstraction shared between nodes:
*   **Data-Based:** Direct uploading of raw observations (common in cloud-based DL).
*   **Information-Based:** Sharing processed data or intermediate results, such as gradients during training or feature maps during inference, to reduce bandwidth and improve privacy.
*   **Knowledge-Based:** Sharing high-level insights—such as instance, representation, or relational knowledge—often utilizing knowledge distillation where a cloud "teacher" guides an edge "student."

### B. Model Dimension
The DL lifecycle is viewed as a continuous process of **training**, **inference**, and **updating**. The authors distinguish "updating" from traditional training by emphasizing lifelong learning and the prevention of "catastrophic forgetting," where new data causes a model to lose previously acquired knowledge.

### C. Computing Power Dimension
Computing resources are distributed across a hierarchy:
*   **Cloud:** Massive resources but high latency and privacy risks.
*   **Edge:** Location-aware processing with reduced latency but limited capacity for large models.
*   **End Devices:** Immediate response capability but severe resource constraints.

Collaboration can be **Vertical** (cross-layer), **Horizontal** (between nodes of the same layer), or **Integrated** (a hybrid of both).

## III. End-Edge-Cloud Collaboration Mechanisms for Deep Learning
This section details how DL tasks are distributed across the architecture throughout the model lifecycle.

### A. End-Edge-Cloud Collaborative Training
Training is divided into two primary parallelism strategies:
*   **Data Parallelism:** Each node holds a model copy and processes a data subset. 
    *   *Centralized:* Uses a parameter server (e.g., FedAvg) to aggregate gradients. 
    *   *Decentralized:* Nodes exchange updates directly without a central server.
    *   *Personalized FL:* Addresses Non-IID (non-independently and identically distributed) data by fine-tuning global models locally or using virtual homogeneity learning.
*   **Model Parallelism:** The model is split across nodes. 
    *   *Layer-level:* Sequential groups of layers are assigned to nodes; pipeline parallelism (e.g., GPipe) reduces idle time via micro-batches.
    *   *Neuron-level:* Tensors/weight matrices are partitioned along dimensions (e.g., Megatron-LM).

### B. End-Edge-Cloud Collaborative Inference
Two main mechanisms enable distributed inference:
*   **Progressive Co-Inference via Early Exiting:** Models incorporate side branches (e.g., BranchyNet). If a sample's confidence exceeds a threshold at an early branch (on the end/edge device), it exits; otherwise, intermediate data is passed to deeper layers in the edge or cloud. 
    *   *Exit Criteria:* Can be **Rule-based** (using entropy or confidence thresholds) or **Learning-based** (training specific modules to predict the optimal exit point).
*   **Distributed Co-Inference via Model Segments:** The model is physically partitioned. 
    *   *Layer-level:* Dividing the model into sequential segments (e.g., JointDNN).
    *   *Neuron-level:* Partitioning weight matrices through channel or spatial splitting.

### C. End-Edge-Cloud Collaborative Updating
Updating focuses on multi-model collaboration via knowledge transfer to achieve domain adaptation and lifelong learning:
*   **Knowledge Types:** Shared knowledge includes instance, data representation, relational (logical rules), feature (output/intermediate), model relational, and structured knowledge (parameters/hyperparameters).
*   **Transfer Methods:** 
    *   *Transfer Learning:* Leveraging source domain knowledge for a target domain.
    *   *Knowledge Distillation (KD):* A teacher model guides a student model's learning.
*   **Federated Continual Learning (FCL):** Allows multiple clients to learn tasks sequentially over time without forgetting, utilizing parameter isolation or distillation.

## IV. Model Compression Technologies for Deep Learning
Compression is essential for deploying models on resource-constrained end/edge nodes.

### A. Pruning and Sparsification
*   **Unstructured vs. Structured:** Unstructured pruning removes individual weights (creating sparse matrices), while structured pruning removes entire filters or rows to maintain hardware compatibility.
*   **Timing:** Pruning can occur **after training** (iterative prune-and-fine-tune) or **at initialization** (using the "Lottery Ticket Hypothesis" to find a winning sparse sub-network via masks).

### B. Parameter Sharing and Quantization
*   **Sharing:** Uses k-means clustering or hash functions to map multiple parameters to a single shared value.
*   **Quantization:** Reduces precision (e.g., 32-bit float to 8-bit int or binary), significantly reducing size but potentially introducing accuracy drops.

### C. Manual Design and Neural Architecture Search (NAS)
*   **Manual Design:** Expert-led creation of lightweight modules (e.g., depthwise separable convolutions in MobileNet).
*   **NAS:** Automates architecture discovery via **Indirect search** (tuning an existing framework) or **Direct search** (exploring the space from scratch), though it remains computationally expensive.

## V. Model Partitioning Technologies for Deep Learning
Partitioning minimizes communication overhead by finding optimal "split points."

### A. Layer-Level Partitioning
This method exploits the fact that intermediate feature maps are often smaller than raw input data. 
*   **Optimization:** Frameworks like Neurosurgeon and DADS (using Directed Acyclic Graphs/DAGs) treat partitioning as a min-cut problem to minimize latency or energy.
*   **Challenges:** Static prediction models struggle with dynamic network conditions, and complex model structures (residual connections) require advanced graph analysis.

### B. Neuron-Level Partitioning
*   **Channel Partitioning:** Split by input channels (partitioning kernels) or output channels (partitioning filters).
*   **Spatial Partitioning:** Split the input data into segments (Grid or Vertical partitioning), requiring each node to hold a full model copy, which is problematic for very large models.

## VI. Knowledge Transfer Technologies for Deep Learning
This section examines how knowledge moves between nodes to facilitate updates.

### A. Transfer Learning
Focuses on transferring knowledge from a source domain to a target domain. This includes **Data-based transfer** (instance/representation) and **Model-based transfer** (structured parameters). Advanced variants include Meta-learning and Multimodal transfer.

### B. Knowledge Distillation (KD)
Transfers model-specific knowledge from teacher to student. 
*   **EEC Context:** Supports multi-teacher learning, knowledge amalgamation (for multiple tasks), and "Teacher Assistants" (medium-sized models that bridge the gap between cloud teachers and end students).
*   **Federated KD:** Replaces heavy parameter exchange with soft-label/logit exchange to improve communication efficiency.

### C. Efficient Fine-Tuning of Foundation Models
To adapt massive foundation models without full retraining:
*   **Parameter-Efficient Tuning:** Updates a small subset of parameters via **Adapters**, **Prompt-tuning**, or **Low-Rank Adaptation (LoRA)**. LoRA is highlighted as superior because it avoids adding inference latency.
*   **Resource-Efficient Tuning:** Uses quantization (e.g., QLoRA) or gradient optimizations to reduce memory footprints during fine-tuning.

## VII. Challenges and Prospects of End-Edge-Cloud Collaborative Deep Learning

### A. System Challenges
*   **Optimization:** Need for unified scheduling across Computing Power Networks (CPN).
*   **Adaptability:** Requirement for dynamic neural networks that adjust structure based on input or environment.
*   **Reliability:** Necessity for real-time monitoring to prevent disruptions in industrial applications.

### B. Communication Bottlenecks
The disparity between internal memory speeds and network bandwidth creates a "bucket effect." Potential solutions include lossless/lossy data compression and the transition to **6G**, which integrates sensing, computing, and communication.

### C. Self-Adaptive Compression and Partitioning
Future research must move toward models that automatically select compression ratios and partition points based on real-time hardware availability and task demands, rather than relying on static thresholds.

### D. Effective Knowledge Transfer
Key gaps include the lack of a unified theoretical framework for knowledge migration and the risk of "negative transfer," where transferred knowledge degrades target model performance.

### E. Security and Privacy
The distributed nature of EEC increases attack surfaces:
*   **Privacy:** The trade-off between data availability and protection (via encryption/blockchain).
*   **IP Protection:** Risk of model theft, requiring solutions like backdoor watermarking.
*   **New Attack Vectors:** "Early exit attacks" designed to disrupt progressive inference mechanisms.

## VIII. Conclusion
The authors conclude that while end-edge-cloud collaboration is nascent, it is essential for meeting the demand for real-time, personalized DL. The proposed framework of co-training, co-inference, and co-updating—supported by compression, partitioning, and knowledge transfer—provides a systematic path toward maturing these systems.
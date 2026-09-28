---
index_terms:
  - large-scale traffic flow prediction
  - generative large language models
  - edge computing
  - spatio-temporal correlations
  - graph segmentation
  - 6G-IATS
---

# Edge Computing Enabled Large-Scale Traffic Flow Prediction With GPT in Intelligent Autonomous Transport System for 6G Network

## I. Introduction
The paper addresses the challenges of large-scale traffic flow prediction (defined as forecasting flow for >1000 roads) within 6G-enabled Intelligent Autonomous Transport Systems (6G-IATS). While Large Language Models (LLMs) show promise in time series analysis, they struggle with two primary issues in this context: an inability to capture complex spatio-temporal correlations of large road networks and low training efficiency caused by the computational burden on central servers.

To solve these, the authors propose **STGLLM-E** (Spatio-Temporal Generative Large Language Model on Edge). The architecture segments large road networks into subgraphs using a method called RoadSort and employs a hybrid model combining a Spatio-Temporal Module (STM) with a Generative LLM (GLLM). Training is decentralized across edge clusters to improve efficiency, utilizing parameter transfer and pruning strategies.

## II. Related Work
### A. Traffic Flow Prediction
The authors trace the evolution of traffic prediction from classical statistical methods (ARIMA) and shallow machine learning (SVR), which fail to capture non-linear spatio-temporal dependencies, to deep learning. They note that while GCNs (DCRNN, GWN) and Transformers (GMAN) are effective for small networks (<350 roads), they exhibit poor accuracy and low efficiency when scaled to large road networks due to the complexity of spatial dependencies and the computational cost of traversing numerous neighbors.

### B. LLMs on Time Series Analysis
Existing LLM frameworks like FPT and LLM4TS have demonstrated high accuracy in general time series tasks. However, the authors argue these models neglect spatio-temporal correlations inherent in road networks and suffer from the inefficiency of centralized fine-tuning when dealing with the massive data volumes produced by large-scale transport systems.

### C. Edge Computing
Edge computing allows processing near the data source via a three-tier architecture: mobile users (data sources), edge servers (local processing), and central servers (coordination). The paper identifies a gap in applying this decentralized approach specifically to large-scale traffic flow prediction in 6G-IATS.

## III. Preliminaries and System Overview
### A. Definitions
*   **Large-Scale Road Network:** Represented as an undirected graph $G=(\mathbb{V}, \mathbb{E})$ where nodes are roads.
*   **Subgraphs:** The network is partitioned into a set of subgraphs $SG = \{SG_1, SG_2, \cdots, SG_E\}$ corresponding to the number of edge clusters $E$.
*   **Subgraph Representations:** Traffic conditions (flow, speed) at timestep $t$ are denoted as $X_j^t \in \mathbb{R}^{n_j \times F}$.

### B. Problem Formulation
The goal is to learn a mapping function $\ell_j(SG_j, X_j)$ that predicts future traffic flow $Y_j$ for $Q$ timesteps. The input historical data $X_j$ is constructed by concatenating three distinct time segments to capture different temporal dynamics:
1.  **Recent:** Data directly adjacent to the prediction window (continuous change).
2.  **Daily-periodic:** Data from the same time intervals over previous days (daily routines/rush hours).
3.  **Weekly-periodic:** Data from the same intervals over previous weeks (weekly rhythms).

### C. System Overview
The STGLLM-E pipeline consists of three main stages:
1.  **RoadSort Graph Segmentation:** Reduces network scale by partitioning the graph into subgraphs while minimizing information loss.
2.  **STGLLM Inference:** A hybrid model where an STM extracts spatio-temporal features and a GLLM (based on GPT-2) generates the future traffic sequences.
3.  **Edge Training Strategy:** Deploys separate STGLLMs on edge clusters, using parameter transfer to initialize neighboring models and pruning to keep them lightweight.

## IV. STGLLM-E Detailed Architecture
### A. Graph Segmentation (RoadSort)
To avoid the loss of crucial information during segmentation, RoadSort identifies "important" roads as center points for subgraphs. It improves upon PageRank by incorporating **Betweenness Centrality** to identify transport hubs and adjusting the damping factor $\beta$ based on the actual shortest-path distance between roads rather than using a constant value.

### B. STGLLM
The model processes each subgraph through three components:
1.  **Subgraph Embedding Layer:** Uses fully connected (FC) layers to map raw traffic data into a higher-dimensional space $d_{\text{model}}$.
2.  **Spatio-Temporal Module (STM):** Consists of $L$ stacked ST blocks, each containing two specific attention mechanisms:
    *   **STBMHSA (Square Target Board Multi-Head Self Attention):** To avoid the quadratic complexity of standard MHSA on large nodes, this mechanism maps roads into a "square target board" of $R$ regions. The road attends to these regional representations at different granularities, reducing complexity from $\mathcal{O}(n^2)$ to linear $\mathcal{O}(Rn)$.
    *   **MHSA:** A standard attention mechanism applied to each road's temporal sequence to capture time-based dependencies.
3.  **Generative Large Language Model (GLLM):** Uses a pre-trained GPT-2 backbone for final prediction:
    *   **Tokenization:** Employs channel-independence and patching to group adjacent timesteps into tokens, reducing the sequence length from $P$ to $P_a$.
    *   **Encoding:** A 1D convolutional layer (patching encoding) preserves local semantic info, which is summed with position embeddings.
    *   **GPT-2 Processing:** Most GPT-2 parameters are frozen to retain general representation knowledge; only Layer Normalization parameters are fine-tuned.
    *   **Output Layer:** Transforms the resulting embedding back into traffic flow sequences via flattening and rearrangement.

## V. Training Strategy of STGLLM-E
To avoid central server bottlenecks, training is distributed across edge clusters. Computing resources (number of servers per cluster) are allocated proportionally to the number of roads in the corresponding subgraph.

The authors implement an **"inference while train"** mode using transfer learning: the first model is trained and its parameters are transferred to initialize the second adjacent cluster's model, and so on. To prevent overfitting and maintain efficiency on limited edge hardware, a pruning strategy removes two attention heads from the MHSA and STBMHSA every three clusters.

## VI. Experiments
### A. Experimental Settings
The model was tested on **LondonHW** and **ManchesterHW** datasets (1000 roads each). Baselines included ARIMA, LSTM, DCRNN, GWN, GMAN, FPT, and LLM4TS. Accuracy was measured via MAE, RMSE, and SMAPE, while efficiency was measured by total training time (TT), average subgraph training time (AT), and GPU memory usage.

### B. Experimental Results
*   **Accuracy:** STGLLM-E outperformed all baselines in both short-term and long-term prediction. Notably, GMAN performed poorly on these large-scale networks compared to its performance in literature for smaller networks. LLM-based models generally beat traditional spatio-temporal models due to their pre-trained intrinsic knowledge.
*   **Efficiency:** STGLLM-E showed faster convergence and lower GPU memory usage than non-frozen deep learning models because of graph segmentation and the frozen GPT-2 backbone.
*   **Ablation Studies:**
    *   **RoadSort:** Proven superior to Degree Centrality and PageRank in maintaining accuracy.
    *   **STBMHSA:** Found more efficient and accurate than standard MHSA or purely local neighborhood attention.
    *   **Pruning:** Equal Pruning-2 (removing 2 heads) provided the best balance between efficiency and accuracy.
    *   **Periodicity:** Including both daily ($P_d$) and weekly ($P_w$) segments significantly improved prediction performance over using only recent data.
*   **Hyperparameter Analysis:** Optimal settings varied by dataset; LondonHW (more complex) required more ST blocks ($L=3$) than ManchesterHW ($L=2$). Increasing the number of subgraphs beyond 10 degraded accuracy due to excessive edge cutting.

## VII. Conclusion
The authors conclude that integrating LLMs with spatio-temporal modules and edge computing allows for accurate and efficient large-scale traffic flow prediction in 6G-IATS. Future research will focus on incorporating external variables like weather and accidents to further enhance predictive capabilities.
---
index_terms:
  - short-reach optical systems
  - passive optical networks
  - signal equalization
  - temporal convolutional networks
  - model compression
  - digital signal processing
---

# Machine Learning in Short-Reach Optical Systems: A Comprehensive Survey

## 1. Introduction
Short-reach optical transmission (typically $\le 100$ km) is critical for inter-data centers, local area networks, and industrial automation due to requirements for high bandwidth and low latency. Passive Optical Networks (PONs) are highlighted as a cost-effective solution using passive splitters, though these introduce power losses and signal impairments such as chromatic dispersion (CD) and nonlinearity.

While coherent systems provide high capacity via complex modulation and DSP, Intensity-Modulated Direct-Detected (IMDD) systems are preferred for short-reach scenarios due to their simplicity and low cost. However, IMDD is susceptible to fiber impairments. The authors argue that integrating Machine Learning (ML) into the receiver's DSP allows these systems to dynamically adapt to stochastic phenomena and nonlinearities without requiring expensive hardware upgrades.

## 2. Applications in Short-Reach Systems
The paper categorizes ML applications in short-reach systems into five primary tasks:

*   **Bandwidth Request and Prediction:** Uses historical network data to forecast future bandwidth availability (e.g., P-DBA). Techniques include k-nearest neighbor, Artificial Neural Networks (ANNs), and Xgboost to reduce latency and optimize allocation for Optical Network Units (ONUs).
*   **Subcarrier Allocation:** Formulated as integer linear programming (ILP) tasks to optimize spectral efficiency. Deep Reinforcement Learning is used for dynamic subcarrier sharing in OFDM-PONs to improve throughput and energy efficiency.
*   **Power Budget Limitations:** Focuses on predicting future energy consumption based on environmental factors and user behavior, though this area is limited by a lack of public datasets.
*   **Equalization:** Aims to minimize fiber-induced distortions (linear and nonlinear). While shallow DL models serve as effective post-equalizers for IMDD and coherent signals, the authors note that centralized pre-equalization at the transmitter can reduce the computational burden on the ONU receiver.
*   **Fault Detection:** Employs ML (Random Forest, ANN, SVM) to proactively monitor Bit-Error Ratio (BER) and predict equipment failures or fiber cuts, overcoming the limitations of conventional monitoring in complex PON architectures.

## 3. DSP for Signal Equalization in Communication Systems
This section reviews conventional linear and nonlinear equalization techniques:

*   **Zero Forcing:** A linear equalizer that minimizes inter-symbol interference (ISI) but suffers from noise enhancement when deep frequency response "valleys" occur.
*   **Feed-Forward Equalizer (FFE):** Processes signals forwardly without feedback; valued for its simplicity and stability.
*   **Decision-Feedback Equalizer (DFE):** Reduces ISI by subtracting previously detected symbols, though it risks error propagation if incorrect decisions are fed back.
*   **Viterbi Equalizer:** Uses a trellis diagram and dynamic programming to find the most likely sequence of transmitted symbols; complexity is $O(T \cdot N^2)$.
*   **Volterra Equalizer:** A nonlinear equalizer using Volterra kernels in stages to compensate for high-order nonlinear distortions from fiber channels and transmitter bandwidth limitations.
*   **Adaptive Filtering:** Iteratively modifies filter parameters to adapt to time-varying channels, typically with a complexity of $O(t)$ per update.

## 4. Traditional Sequential ML Methods
The authors examine deep learning models used as baselines for sequential communication data:

*   **Recurrent Neural Networks (RNN):** Effective for variable-length sequences but suffer from exploding and vanishing gradient problems during training.
*   **Long Short-Term Memory (LSTM):** Introduces a cell state and gating mechanisms (input, forget, output) to maintain long-term dependencies and mitigate gradient issues.
*   **Gated Recurrent Units (GRU):** A simplified LSTM using only update and reset gates; useful for mitigating distortions from CD and nonlinearities in high-speed coherent systems.
*   **Convolutional Neural Networks (CNN):** Utilize weight-sharing and convolutional kernels to extract temporal features. The authors highlight the "Inception" architecture (using multiple kernel sizes) and $1 \times 1$ convolutions for dimensionality reduction.

## 5. Advanced Sequential ML Methods

### 5.1 Distortion Model
The paper analyzes three dominant distortion mechanisms in short-reach PAM-based systems:
*   **Chromatic Dispersion (CD):** A linear transformation where phase velocity varies with frequency, resulting in high-frequency attenuation in the time domain.
*   **Jitter:** Fluctuations in sampling time that create high-frequency amplitude perturbations, potentially disrupting networks relying on low-frequency signals.
*   **Chirp:** Signals where frequency varies over time. 
The authors conclude that because these effects alter both time and frequency domains concurrently, they cannot be eliminated by operations restricted to a single domain.

### 5.2 Temporal Convolution Neural Network (TConv-NN)
Temporal CNNs are proposed as hardware-efficient alternatives to LSTMs. Key architectures discussed include:
*   **FC-SCINet:** Employs series decomposition to separate low and high-frequency signals and uses "SCIBlocks" to perform interactive learning on odd-even sampled sub-sequences, expanding the receptive field.
*   **DLinear:** A very low-complexity model that decomposes raw data into trend (low frequency) and seasonal (high frequency) components using moving average kernels followed by a linear combination.
*   **LightTS:** Uses Interval Sampling (for periodic patterns) and Continuous Sampling (for temporal continuity), processing these via an Information Exchange Block (IEBlock) based on MLPs.

### 5.3 Transformer-Based Network
Transformers utilize scaled dot-product attention to capture global dependencies through Queries ($Q$), Keys ($K$), and Values ($V$). To address the quadratic complexity of vanilla Transformers, the authors highlight:
*   **LSH Attention (Reformer):** Uses hashing to group similar items, reducing complexity for long sequences.
*   **Autoformer:** Replaces the standard encoder with a series decomposition and auto-correlation mechanism to better handle seasonality and trends in time-series data.

### 5.4 Fourier Convolution Neural Network
Processing signals in the Fourier domain is argued to be more efficient due to energy compaction, bijective transformation properties, and $O(n \log n)$ complexity.
*   **TimesNet:** Transforms 1D signals into 2D tensors based on dominant frequencies to capture intra- and inter-periodic variations, using Inception networks for reconstruction.
*   **FreTS:** An MLP-based network that performs non-linear transformations directly in the frequency domain via a Frequency Temporal Learner, avoiding time-domain bottlenecks.

## 6. Model Compression
To address the hardware constraints of deploying large ML models on single GPUs or edge devices (like ONUs), two main compression strategies are discussed:

*   **Knowledge Distillation:** Transfers knowledge from a complex "teacher" model to a compact "student" model. In optical systems, this is specifically suggested as a way to parallelize the otherwise sequential nature of RNNs, making them compatible with high-speed hardware. It can also leverage "privileged information" to improve predictions for small datasets.
*   **Vector Quantization (VQ):** Reduces computational load by representing complex data using a small set of prototype vectors (a codebook). VQ is identified as an effective way to compress the essential information of RNNs or CNNs, facilitating faster inference in high-speed networks.

## 7. Conclusions
The survey provides a new taxonomy for ML models in short-reach optical systems, categorizing them into traditional sequential, temporal convolutional, and Fourier-based networks. The authors emphasize that while DL models offer superior performance in equalization and fault detection, their practical deployment depends on balancing complexity with hardware feasibility through techniques like model compression.
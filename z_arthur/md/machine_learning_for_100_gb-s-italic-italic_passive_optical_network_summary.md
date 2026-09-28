---
index_terms:
  - passive optical network
  - intensity modulation direct detection
  - neural network equalizer
  - nonlinearity compensation
  - 100 Gb/s per wavelength
  - loss budget
  - PAM-8 modulation
---

# Machine Learning for 100 Gb/s/λ Passive Optical Network

## Abstract
The paper demonstrates a 100 Gb/s/λ passive optical network (PON) using Intensity Modulation and Direct Detection (IMDD) technology. To maintain low cost, the authors employ commercially available 20G-class components. A neural network (NN)-based equalizer is implemented to mitigate linear and nonlinear distortions, outperforming traditional feedforward equalizers (FFE) and Volterra nonlinear equalizers (VNE) in high-nonlinearity scenarios. The authors establish strict training/testing protocols using random data to avoid performance overestimation. Experimentally, the system achieves a 30-dB loss budget for a 33 GBd/s PAM8 signal by increasing launch power to 18 dBm and leveraging the NN's nonlinear equalization capabilities.

## I. Introduction
The demand for higher bandwidth driven by 5G and IoT necessitates a move toward 100 Gb/s/λ PON. While coherent technology offers superior sensitivity, it is costly and power-intensive; thus, IMDD is preferred for cost-effectiveness. However, IMDD faces challenges with high loss budgets and inter-symbol interference (ISI) due to limited device bandwidth.

The authors address a critical flaw in existing machine learning research: the use of pseudo-random bit sequences (PRBS) for both training and testing. They argue that NNs may simply recognize PRBS patterns rather than channel characteristics, leading to overestimated results. This paper proposes using random data for training to ensure the NN acts as a true equalizer. The goal is to demonstrate that an NN-based equalizer can enable high launch powers (and thus higher loss budgets) by effectively compensating for the resulting nonlinear distortions.

## II. Principle
The authors compare three equalization methods: FFE, VNE, and NN.

### Feedforward Equalizer (FFE)
FFE is a linear equalizer that computes a symbol as a linear combination of its neighborhood sampled sequence. Because it is a linear mapping, it cannot mitigate nonlinearities from modulation or transmission.

### Volterra Nonlinear Equalizer (VNE)
VNE approximates nonlinear systems by incorporating higher-order features of the sampled signal. While it handles nonlinearity better than FFE, it remains essentially a linear combination of pre-processed higher-order features.

### Neural Network (NN) Based Equalizer
The proposed NN is a symbol-spaced, fully connected 3-layer network (one input layer of 51 nodes, two hidden layers of 128 nodes each, and an output layer of 8 nodes for PAM-8 classification). 
- **Mechanism:** It uses ReLU activation functions for hidden layers and Softmax for the output layer. The loss function is cross-entropy, optimized via back-propagation with the Adam optimizer.
- **Optimization:** To prevent overfitting and improve convergence, the authors implement a dropout rate of 0.2 and batch normalization.
- **Complexity:** NN is computationally more demanding than FFE or VNE in terms of multiplications per symbol, but the authors note that this complexity can be mitigated through parallel processing or by reducing hidden layer size.

## III. Simulation
Simulations were conducted for a 33 GBaud/s PAM-8 system with a 16.2 GHz bandwidth limit and 25 km of standard single-mode fiber (SSMF).

### Training and Test Data Protocol
The authors investigate various data combinations to determine the correct training method:
- **PRBS Pitfalls:** Using PRBS for both training and testing leads to extremely low BER because the NN learns the mathematical rule generating the sequence rather than the channel characteristics. This results in either overestimation (if test data follows the same rule) or underestimation (if test data follows a different PRBS rule).
- **Established Rule:** To ensure fair evaluation, random data must be used for training. Once trained on random data, the NN can then be tested with either random data or PRBS without bias.

### Performance Analysis
Simulation results show that at low launch powers (where linear distortion dominates), FFE, VNE, and NN perform similarly. However, as launch power increases and nonlinearity becomes severe, the NN-based equalizer significantly outperforms both FFE and VNE. This indicates that NN is uniquely suited for high-power transmission where nonlinearity typically limits the BER.

## IV. Experimental Results and Discussions
The experimental setup utilizes a 20 GHz MZM for modulation and an EDFA to control launch power over 20 km of SSMF. 

### System Implementation Details
- **SBS Suppression:** To prevent stimulated Brillouin scattering (SBS) at high launch powers, the authors broaden the optical spectrum by modulating the laser with a low-voltage 100 Mb/s PRBS signal.
- **Receiver Sensitivity:** The authors identify that thermal and shot noise create significant errors for PAM-8 due to small symbol spacing. To isolate the effectiveness of the NN equalizer from these additive noises, they fix the power injected into the photodetector at 3 dBm.

### Results and Loss Budget
- **Optical Back-to-Back (OBTB):** All three equalizers perform similarly since only linear distortions are present.
- **Fiber Transmission:** In the 20 km SSMF test, NN again outperforms VNE and FFE as launch power increases, confirming simulation results.
- **Loss Budget Achievement:** By setting the launch power to 18 dBm—which introduces strong nonlinearity that the NN can compensate for—the system achieves a receiver sensitivity of -12 dBm at the 7% FEC limit ($3.8 \times 10^{-3}$ BER). This results in a total loss budget of 30 dB, meeting the IEEE 802.3av PR30 requirement.

## V. Conclusion
The paper concludes that NN-based equalizers are powerful tools for mitigating both linear and nonlinear distortions in 100 Gb/s/λ IMDD PONs. By adopting a strict training regime using random data, the authors prove that NN is significantly more effective than FFE and VNE at handling high-power nonlinearity. This capability allows for increased launch power, which directly enables the achievement of a 30-dB loss budget using cost-effective 20G-class components.
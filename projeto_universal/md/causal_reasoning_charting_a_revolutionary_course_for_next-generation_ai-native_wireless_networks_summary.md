---
index_terms:
  - causal reasoning
  - AI-native wireless networks
  - structural causal models
  - 6G wireless communications
  - causal reinforcement learning
  - integrated sensing and communication
  - semantic communication
  - distribution generalization
---

# Charting a Revolutionary Course for Next-Generation AI-Native Wireless Networks

## Introduction
Next-generation (6G) wireless networks aim to be "AI-native," integrating machine learning across the protocol stack. However, current data-driven and statistical AI models face six critical challenges: dynamic adaptability, time criticality, intent management, resilience, nonlinear signal dynamics, and human-level cognition/reasoning. 

The authors argue that existing statistical AI is insufficient because it requires massive datasets, suffers from high retraining overhead in volatile environments, lacks transparency (black-box nature), and cannot perform logical deductions or combine experiences to generate novel insights. To resolve these issues, the paper proposes a framework grounded in causal reasoning—comprising causal discovery, causal representation learning (CRL), and causal inference—to create explainable, sustainable, and reasoning-aware networks that emulate human-like cognition through interventions and counterfactuals.

## Contributions
The article provides a holistic vision for causality-driven AI-native networks with the following key contributions:
*   **Theoretical Foundation:** Establish the building blocks of causal reasoning and motivate their application in wireless contexts.
*   **Problem Identification:** Contrast traditional AI's lack of explainability and energy inefficiency with the potential of causal frameworks.
*   **Causal Graphical Models (CGMs):** Demonstrate how causal discovery can enhance THz beamforming, digital twins (DTs), data augmentation, network resilience, and semantic communication.
*   **Analytical Frameworks:** Introduce causal inference tools, including Causal Reinforcement Learning (RL) and Multi-Armed Bandits (MAB), to address wireless control, intent management, and Integrated Sensing and Communication (ISAC).

## Causality Primer
Statistical ML models rely on correlations ($P(X, Y)$), which fail in highly dynamic environments like THz bands where sudden blockages cause power fluctuations that curve-fitting neural networks cannot adapt to. Causal reasoning instead maps the "physics" of the system through directed graphs.

### Fundamental Definitions
*   **Causal Discovery:** Algorithmic learning of the inherent causal structure from observed data, providing directionality and explanation rather than mere correlation.
*   **Structural Causal Models (SCMs):** A collection of endogenous variables (cause/effect) and exogenous variables (noise), where structural functions define how parents in a graph determine their children.
*   **Causal Representation Learning (CRL):** The process of mapping high-dimensional raw data into lower-dimensional causal variables.
*   **Causal Inference:** Using learned structures to predict the effects of interventions or counterfactuals.

### Reasoning Mechanisms
The paper distinguishes between three levels of reasoning:
1.  **Associational ($\mathcal{L}_1$):** Observing $X$ to change beliefs about $Y$ (e.g., standard supervised learning).
2.  **Interventional ($\mathcal{L}_2$):** Using the **do-operator** to manipulate a variable and observe its effect (e.g., "What happens if I increase the number of antennas?").
3.  **Counterfactual ($\mathcal{L}_3$):** Imagining alternative pasts to determine root causes (e.g., "Would QoS have been better if an RIS were placed here?").

## Classical Versus Causal Reasoning-Based AI-Native Wireless Networks

### Lack of Explainability and Trustworthiness
Bayesian models are explainable but struggle with nonlinearities; Deep Learning (DL) handles nonlinearity but is a black box. The authors propose using causal graphs to define the **explanandum** (the phenomenon being explained) and the **explanans** (the sequence of causal relationships and intervened values). Causal Bayesian Optimization (CBO) is suggested as a computationally feasible way to compute optimal intervention sets for resource allocation.

### Inability to Reason and Generalize
Standard Artificial Neural Networks (ANNs) lack distribution invariance, leading to high training overhead. The authors define **distribution generalization** as the ability to find an approximate solution that remains close to the minimax solution across all possible interventions on the wireless environment. Causal ML achieves this more efficiently than transfer or meta-learning by leveraging single causal graphs rather than massive random datasets.

### Energy Efficiency
Foundation models (e.g., LLMs) are energy-inefficient due to billions of parameters. Causality promotes sustainability via:
*   **Lighter Models:** Focusing only on essential causal factors reduces parameters and memory.
*   **Reduced Retraining:** Stable causal relationships persist across contexts, eliminating frequent recurrent training.
*   **Causality-based Semantic Communication:** Transmitting only "causal states" reduces the total volume of data exchanged.

## Causal Discovery and Representation Learning for Next-Generation Wireless Networks

### CGMs for Near-Accurate Dynamic Wireless Environment Modeling
*   **Ultrareliable Beamforming (THz):** Using variational causal networks and Granger causality to model time-varying channel dynamics, reducing the dimensional state space for more sample-efficient estimation.
*   **Digital Twins (DTs):** Causal discovery prevents bias from unknown confounding variables in physical twin modeling, improving traffic prediction and resource allocation.
*   **Training Data Generation:** "Causal generative models" use interventions and counterfactuals to create diverse synthetic training scenarios (e.g., natural disasters or hardware malfunctions) that are more structurally accurate than GANs.

### Resilient Wireless Networks
Resilience is framed as a loop of detection, remediation, and recovery. By monitoring the causal graph $\mathcal{G}$, a base station can predict QoE violations and solve a counterfactual optimization problem to find the best remediation policy using both observational and interventional datasets.

### Causal Discovery and Representation Learning for Semantic Communication (SC)
Semantics are defined as the inherent causal structure of data. By utilizing CRL, networks can form unique representations for states with similar cause-and-effect repertoires, reducing transmission overhead. The authors suggest integrating this with integrated information theory and hypergame theory.

### Causal Discovery for ISAC
Data-driven AI fails in ISAC due to the mobility of scatterers and the volume of sensing data. 
*   **Target Tracking:** Granger causality is proposed to model time-varying objects and improve beam alignment via nonlinear MMSE methods.
*   **Distributed Sensing:** "Causal reasoning games" allow nodes to use SCMs to estimate other users' strategies and optimize resource usage through game-theoretic tools.

## Causal Inference for Next-Generation Wireless Networks

### Causal Inference for Wireless Control
Traditional RL is passive and struggles with Partially Observable Markov Decision Processes (POMDPs). The authors propose **Causal RL**, where actions are treated as interventions. By distilling learning histories from various environments into a sequence model via "behavioral cloning," they suggest creating **Causal Foundation Models** that are invariant to environment changes.

### Causal Bandit Problem for Real-Time Decision Making
To meet 6G synchronization demands, the authors propose Causal Multi-Armed Bandits (MAB). Unlike traditional MABs, these use SCMs to acquire knowledge about non-intervened variables, ensuring distribution invariance without needing extensive new training data.

### Causal Inference for Intent-Based Wireless Networks
Intent-based networks translate business goals into configurations via a closed loop:
1.  **Intent Assurance:** Measuring KPIs against objectives.
2.  **Corrective Actions:** Using SCM decomposition to break high-level intents into manageable subgoals across different OSI layers, enabling deductive reasoning and autonomous self-reflection.

### Causal Inference for ISAC
*   **Nonlinearity:** Causal discovery is used to model the "physics" of self-interference (SI) caused by hardware imperfections, avoiding the need for recurrent retraining.
*   **Waveform Design:** Causal Multi-Objective RL (MO-RL) identifies minimal interventions needed to balance conflicting goals (e.g., radar sensing quality vs. communication QoE), reaching near-Pareto-optimal solutions that standard MO-RL might miss.

## Conclusion and Recommendations
The authors conclude with three primary recommendations for 6G development:
1.  **Causality as a Bedrock:** Move beyond mimicking functions; integrate causal reasoning into sampling, QoS management, encoding, scheduling, and communication across the stack.
2.  **Bias Mitigation:** Shift from pure data-driven foundation models to causality-based ones to create lighter, interpretable models.
3.  **Scalable Architecture:** Implement layer-wise SCMs tailored to specific OSI layers to manage complexity, aligning with Open RAN architectures.
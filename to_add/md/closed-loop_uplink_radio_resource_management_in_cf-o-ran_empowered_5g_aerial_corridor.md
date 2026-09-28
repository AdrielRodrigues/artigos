# Closed-loop Uplink Radio Resource Management in CF-O-RAN Empowered 5G Aerial Corridor

Manobendu Sarker\*, Md. Zoheb Hassan<sup>†</sup>, and Xianbin Wang<sup>‡</sup>
\*Department of Computer and Software Engineering, Polytechnique Montreal, Canada
<sup>†</sup>Department of Electrical and Computer Engineering, Université Laval, Québec City, QC, Canada
<sup>‡</sup>Department of Electrical and Computer Engineering, Western University, London, Canada

Abstract-In this paper, we investigate the uplink (UL) radio resource management for 5G aerial corridors with an openradio access network (O-RAN)-enabled cell-free (CF) massive multiple-input multiple-output (mMIMO) system. Our objective is to maximize the minimum spectral efficiency (SE) by jointly optimizing unmanned aerial vehicle (UAV)-open radio unit (O-RU) association and UL transmit power under quality-of-service (QoS) constraints. Owing to its NP-hard nature, the formulated problem is decomposed into two tractable sub-problems solved via alternating optimization (AO) using two computationally efficient algorithms. We then propose (i) a QoS-driven and multi-connectivityenabled association algorithm incorporating UAV-centric and O-RU-centric criteria with targeted refinement for weak UAVs, and (ii) a bisection-guided fixed-point power control algorithm achieving global optimality with significantly reduced complexity, hosted as xApp at the near-real-time (near-RT) RAN intelligent controller (RIC) of O-RAN. Solving the resource-allocation problem requires global channel state information (CSI), which incurs substantial measurement and signaling overhead. To mitigate this, we leverage a channel knowledge map (CKM) within the O-RAN non-RT RIC to enable efficient environment-aware CSI inference. Simulation results show that the proposed framework achieves up to 440% improvement in minimum SE, 100% QoS satisfaction and fairness, while reducing runtime by up to 99.7% compared to an interior point solver-based power allocation solution, thereby enabling O-RAN compliant real-time deployment.

## I. INTRODUCTION

Aerial corridors are structured three-dimensional routes designed for unmanned aerial vehicle (UAV) traffic operating beyond visual line of sight (BVLOS). They offer a scalable mechanism to concentrate flight risk away from populations and infrastructure while embedding connectivity into route design. Realizing this vision requires re-engineering terrestrial cellular systems to ensure reliable command-and-control (C2), localization, and data links through techniques such as uptilted antennas and coordinated interference management [1]. Coverage analyses across altitudes reveal that existing terrestrial macrocells and millimeter-wave deployments alone are insufficient, motivating new corridor planning that leverages multi-tier fifth generation (5G) connectivity and pre-planned handovers to ensure ubiquitous, low-latency service [2].

To create aerial corridors with guaranteed coverage, cellular networks must collaboratively provide site-specific beam management and optimized UAV-to-base station associations [3]. The open radio access network (O-RAN) architecture is a compelling enabler, augmenting cellular capabilities with near-real-time control and cross-layer programmability via its RAN intelligent controller (RIC), particularly suited to dynamic UAV

scenarios [4]. A recent work [5] demonstrates that O-RAN-based closed-loop control jointly optimizing UAV location and transmission directionality delivers approximately 19% uplink (UL) capacity gain while meeting high-definition video quality-of-service (QoS) on multi-cell testbeds. At the RAN-function level, the RIC orchestrates coordinated association and resource allocation, improving energy efficiency and cooperative coverage for scalable aerial corridors [6].

Although O-RAN-enabled coordination improves average system throughput [5], [6], aerial corridors demand stringent per-UAV QoS guarantees, as any loss of connectivity can jeopardize flight safety and C2 link reliability. The unique propagation characteristics of aerial UAVs present a significant hurdle; their strong (often unobstructed) line-of-sight (LoS) links to multiple ground open radio units (O-RUs) can create severe UL interference, necessitating joint UAV-O-RU association and power control. Furthermore, centralized coordination schemes typically require global channel state information (CSI), yet the standard O-RAN E2 interface is not designed to support the large-scale, low-latency CSI exchange required for real-time, network-wide optimization.

In this paper, we address these intertwined challenges of guaranteed connectivity and interference management by proposing a novel framework that integrates the cell-free (CF) massive multiple-input multiple-output (mMIMO) concept within an O-RAN architecture. In CF mMIMO, users are served concurrently by multiple distributed access points, inherently providing macro-diversity and robust connectivity [7]. To the best of our knowledge, the problem of ensuring multi-connectivity and mitigating interference for 5G aerial corridors in an O-RAN-enabled CF mMIMO system has not been addressed in the literature. The main contributions of this work are summarized as follows.

- We propose an O-RAN-enabled CF mMIMO framework integrating a channel knowledge map [8] within the non-real-time (non-RT) RIC to enable scalable CSI acquisition and circumvent E2 interface limitations.
- We formulate a max-min spectral efficiency (SE) optimization problem jointly optimizing UAV-O-RU association and UL power under per-UAV QoS constraints, and develop an alternating optimization (AO) framework with two efficient algorithms: a QoS-driven association algorithm and a bisection-guided fixed-point power control method achieving global optimality.
- We demonstrate through extensive simulations that the pro-

![](_page_1_Figure_0.jpeg)

Fig. 1: O-RAN-enabled CF mMIMO system for 5G aerial corridor.

posed framework achieves substantial improvements in minimum SE, QoS satisfaction, and fairness while reducing runtime significantly compared to an interior point solver-based methods.

#### II. SYSTEM MODEL

We consider an O-RAN-enabled CF mMIMO system supporting 5G aerial corridor, serving K single-antenna UAVs through L geographically distributed O-RUs, shown in Fig. 1. Each O-RU  $\ell \in \mathcal{L} = \{1,2,\ldots,L\}$  is equipped with  $N_\ell$  antennas and connected to an open distributed/centralized unit (O-DU/O-CU) via fronthaul links. The UAVs operate at altitudes ranging from ground level to several hundred meters and are indexed by  $k \in \mathcal{K} = \{1,2,\ldots,K\}$ . Let  $\mathcal{L}_k$  be the set of O-RUs that serve UAV k. We assume time-division duplex (TDD) operation, where the channel remains constant over a coherence block of  $\tau_c$  symbols. Each coherence block is divided into  $\tau_p$  symbols for UL pilot transmission and  $\tau_c - \tau_p$  symbols for UL data transmission [7].

A Walk-through: As illustrated in Fig. 1, the proposed O-RAN-enabled framework comprises two core components: channel knowledge map (CKM) generation [8] and radio resource management (RRM) decision-making. The CKM serves as a repository of propagation statistics indexed by transmitter and receiver locations, thereby enhancing environmental awareness and reducing reliance on real-time CSI acquisition. By mitigating the challenges posed by high-dimensional channels and training overhead, CKM is envisioned as a key enabler for 6G networks demanding extreme capacity, ultra-low latency, and massive connectivity. CKM can be constructed using canonical interpolation methods, Kriging, kernel regression, matrix and tensor completion, deep learning, and environment model-assisted techniques [8]. In the proposed architecture, CKM is implemented as an rApp, a non-RT RIC application, at the non-RT RIC, while real-time RRM is realized as an xApp, a near-RT RIC application, at the near-RT RIC. In what follows, we present the operational flow of the proposed framework: (1) The O-RAN network provides feedback and telemetry data to the service management and orchestration (SMO)/O-Cloud via the O1 interface, where it is stored in the global database (DB). (2) The global DB updates the CKM rApp through the R1 interface. (3) The CKM refreshes its information, and the Non-RT RIC supplies policy data (e.g., traffic information, RRM xApp configurations) and updated CSI to the local RAN DB via the A1 interface<sup>1</sup>. (4) Using Near-RT internal APIs, the local DB conveys control instructions and CSI to the RRM xApps. (5) The xApps compute RRM decisions and deliver them to the O-DU/O-CU through the E2 interface. (6) Finally, the O-DU/O-CU forwards these decisions to the O-RU via the open fronthaul, which transmits them to UAVs through the air-interface control channels.

## A. Channel Model

The channel between UAV k and O-RU  $\ell$  consists of: (i) large-scale fading capturing path loss, shadowing, and LoS probability; and (ii) small-scale Rician fading with dominant LoS component and multipath scattering [10].

- 1) Large-Scale Fading: Following the 3GPP technical reports for aerial UAV scenarios [11], [12], we adopt the enhanced urban macro-cell aerial (UMa-AV) propagation model that provides height-dependent LoS probability and distinct path loss expressions for LoS and non-LoS (NLoS) propagation conditions. Let  $h_{\rm UT,k}$  and  $h_{\rm O-RU,\ell}$  denote UAV and O-RU heights, and  $d_{k\ell,2\rm D}$  the horizontal distance. The 3D distance is  $d_{k\ell,3\rm D}=\sqrt{d_{k\ell,2\rm D}^2+(h_{\rm UT,k}-h_{\rm O-RU,\ell})^2}$ . LoS probability and path loss  $\overline{\rm PL}_{k\ell}$  (in dB) follow distinct LoS/NLoS models from [12]. The large-scale coefficient is modeled as  $\beta_{k\ell}=10^{-(\overline{\rm PL}_{k\ell}+X_\sigma)/10}$ , where  $X_\sigma\sim\mathcal{N}(0,\sigma_{\rm sh}^2)$  models lognormal shadowing. We assume  $\beta_{k\ell}$  is known via long-term measurements [7].
- 2) Small-Scale Fading: The channel is modeled as spatially correlated Rician fading [13]:

$$\mathbf{h}_{k\ell} = \sqrt{\beta_{k\ell}} \left( \sqrt{\frac{K_{k\ell}}{K_{k\ell} + 1}} \mathbf{a}_{k\ell}^{\text{LoS}} + \sqrt{\frac{1}{K_{k\ell} + 1}} \mathbf{h}_{k\ell}^{\text{scat}} \right) \in \mathbb{C}^{N_{\ell}}, \quad (1)$$

where  $K_{k\ell}$  is the Rician K-factor,  $\mathbf{a}_{k\ell}^{\mathrm{LoS}}$  is the array response with  $\|\mathbf{a}_{k\ell}^{\mathrm{LoS}}\|^2 = N_{\ell}$ , and  $\mathbf{h}_{k\ell}^{\mathrm{scat}} \sim \mathcal{CN}(\mathbf{0}, \mathbf{R}_{k\ell})$  with  $\mathrm{tr}(\mathbf{R}_{k\ell}) = N_{\ell}$ . We use the mean-plus-deviation form  $\mathbf{h}_{k\ell} = \overline{\mathbf{h}}_{k\ell} + \widetilde{\mathbf{h}}_{k\ell}$  [14], where  $\overline{\mathbf{h}}_{k\ell} = \sqrt{\beta_{k\ell} \frac{K_{k\ell}}{K_{k\ell}+1}} \mathbf{a}_{k\ell}^{\mathrm{LoS}}$  with  $\widetilde{\mathbf{h}}_{k\ell} \sim \mathcal{CN}(\mathbf{0}, \mathbf{C}_{k\ell})$  and  $\mathbf{C}_{k\ell} = \frac{\beta_{k\ell}}{K_{k\ell}+1} \mathbf{R}_{k\ell}$ .

## B. Channel Estimation

At the beginning of each coherence block, all K UAVs simultaneously transmit pilot sequences to O-RUs. As in practical systems, we consider  $K > \tau_p$ , thereby pilot sequences must be reused among multiple UAVs, leading to pilot contamination. Considering MMSE channel estimation [15] is being used by O-DU/O-CU, the estimate  $\hat{\mathbf{h}}_{k\ell}$  and error  $\hat{\mathbf{h}}_{k\ell}^{\text{err}} = \mathbf{h}_{k\ell} - \hat{\mathbf{h}}_{k\ell}$  are independent random variables with  $\hat{\mathbf{h}}_{k\ell} \sim \mathcal{CN}(\bar{\mathbf{h}}_{k\ell}, \hat{\mathbf{C}}_{k\ell})$  and  $\hat{\mathbf{h}}_{k\ell}^{\text{err}} \sim \mathcal{CN}(\mathbf{0}, \mathbf{C}_{k\ell}^{\text{err}})$ , where  $\hat{\mathbf{C}}_{k\ell} = \mathbf{C}_{k\ell} - \mathbf{C}_{k\ell}^{\text{err}}$  and  $\mathbf{C}_{k\ell}^{\text{err}} = \mathbf{C}_{k\ell} - \mathbf{C}_{k\ell} \Psi_{k\ell}^{-1} \mathbf{C}_{k\ell}$  with  $\Psi_{k\ell} = \tau_p^2 \sum_{i \in \mathcal{P}_k} p_i^p \mathbf{C}_{i\ell} + \tau_p \sigma^2 \mathbf{I}_{N_\ell}$ . In  $\Psi_{k\ell}$ ,  $\mathcal{P}_k$  is the set of UAVs sharing UAV k's pilot and  $p_k^p$  is the pilot power, and  $\sigma^2$  is the noise power. When  $|\mathcal{P}_k| > 1$ ,  $\hat{\mathbf{h}}_{k\ell}$  is contaminated by LoS components of interfering UAVs.

<sup>&</sup>lt;sup>1</sup>RRM algorithms are implemented as xApps at the near-RT RIC. Because the E2 interface supports control signaling but not high-rate CSI exchange, CKM-derived CSI estimates (based on UAV positions obtained via E2 [9]) are delivered through the A1 interface instead.

After pilot transmission, UAV k transmits data with power  $p_k^{\mathrm{u}} > 0$  over  $\tau_c - \tau_p$  symbols. O-RU  $\ell$  receives  $\mathbf{y}_\ell^{\mathrm{u}} = \sum_{i=1}^K \sqrt{p_i^{\mathrm{u}}} \mathbf{h}_{i\ell} s_i + \mathbf{n}_\ell^{\mathrm{u}}$ , where  $s_k$  are unit-power data symbols and  $\mathbf{n}_\ell^{\mathrm{u}} \sim \mathcal{CN}(\mathbf{0}, \sigma^2 \mathbf{I}_{N_\ell})$ . Each O-RU applies L-MMSE combining  $\mathbf{v}_{k\ell} = \left(\sum_{i=1}^K p_i^{\mathrm{u}} (\hat{\mathbf{h}}_{i\ell} \hat{\mathbf{h}}_{i\ell}^H + \mathbf{C}_{i\ell}^{\mathrm{err}}) + \sigma^2 \mathbf{I}_{N_\ell}\right)^{-1} \hat{\mathbf{h}}_{k\ell}$  to detect UAV k [7]. The serving O-RUs  $\mathcal{L}_k$  forward soft estimates to the CPU, which combines them with  $\{\alpha_{k\ell}\}$ , where  $\alpha_{k\ell} = a_{k\ell} \sqrt{\beta_{k\ell}}$  are maximal ratio combining weights [7]. Using the use-and-then-forget bound [16], the UL SE of UAV k is  $\mathrm{SE}_k = (1 - \tau_p/\tau_c)\log_2(1 + \Gamma_k)$ , where  $\Gamma_k$  is the signal-to-interference-plus-noise ratio (SINR), given in (2).

**Remark.** SE calculation is required to finalize RRM decisions within the Near-RT RIC of O-RAN. Although the channel is estimated via CKM in our framework, the channel model and estimation are included here for the SE calculation model.

#### III. PROBLEM FORMULATION

Our objective is to jointly optimize the UAV-O-RU association assignment and UL data transmit power allocation for maximizing the minimum SE performance while satisfying scalability and QoS requirements. To this end, we define an association matrix  $\mathbf{A} \in \mathbb{R}^{K \times L}$  where  $a_{k\ell} = 1$  if UAV k associates with O-RU  $\ell$ , and 0 otherwise. Thus,  $\mathcal{L}_k = \{\ell : a_{k\ell} = 1\}$  with  $|\mathcal{L}_k| = \sum_{\ell=1}^L a_{k\ell}$ . Using these definitions, the SINR in (2) is reformulated as (3). Thus, the joint optimization problem is expressed as follows:

P0: 
$$\max_{\substack{\mathbf{A} \in \{0,1\}, \\ \{p_u^k\} \in [0,p^{\max}]}} \quad \min_{k \in \mathcal{K}} \quad SE_k, \tag{4a}$$

s.t. 
$$\sum_{\ell \in \mathcal{L}} a_{k\ell} \ge 1, \ \forall k \in \mathcal{K},$$
 (4b)

$$\sum_{k \in \mathcal{K}} a_{k\ell} \le \tau_p, \forall l \in \mathcal{L}, \tag{4c}$$

$$SE_k \ge SE_k^{\min}, \forall k \in \mathcal{K}.$$
 (4d)

In **P0**, constraint (4b) ensures every UAV connects to at least one O-RU for ensuring service coverage. Constraint (4c) restricts each O-RU to serve at most  $\tau_p$  UAVs, dictated by pilot orthogonality, computational capacity, and scheduling overhead [17]. Lastly, constraint (4d) enforces the minimum SE requirement SE<sub>k</sub><sup>min</sup> for QoS guarantees. However, **P0** is a mixed-integer nonlinear programming (MINLP) with binary association  $\{a_{k\ell}\}$  and continuous power  $\{p_k^{\rm u}\}$  variables. Because the objective (4a) and minimum SE constraint (4d) both involve non-convex  $\log_2(1+\Gamma_k)$  functions, where  $\Gamma_k$  depends nonlinearly on power and association. This renders **P0** NP-hard and computationally intractable.

#### IV. PROPOSED SOLUTION

To address the NP-hardness in **P0**, we adopt a decoupling approach where the original problem is split into two subproblems. Each sub-problem focuses on addressing a specific aspect, such as UAV-O-RU association assignment and UL data transmit power allocation.

## A. UAV-O-RU Association Assignment

With fixed UL data transmit power  $p_k^{\rm u}$ , the UAV-O-RU association assignment problem is formulated as follows:

**P1:** 
$$\max_{\mathbf{A}\in\{0,1\}} \quad \min_{k\in\mathcal{K}} \quad \mathbf{SE}_k,$$
 (5a)

s.t. 
$$(4b)-(4c)$$
.  $(5b)$ 

Since the SINR expression is intricately linked to **A** through both channel combining and interference coupling, **P1** constitutes a MINLP. As finding the global optimum entails prohibitive computational complexity on the order of  $\mathcal{O}(2^{KL})$ , we develop an efficient heuristic approach to obtain a near-optimal solution, as detailed below.

- 1) Proposed UAV-O-RU Association Assignment Scheme: To efficiently address the association problem, we propose a three-stage procedure for constructing a feasible, high-quality association matrix, summarized in Algorithm 1.
- Stage 1: UAV-centric initialization (Lines 3–7): Each UAV k initially connects to its strongest O-RU  $\ell$  based on large-scale fading coefficients, ensuring universal connectivity under the O-RU capacity constraint (4c), thereby satisfying constraint (4b).
- Stage 2: O-RU-centric load balancing (Lines 8–14): O-RUs with remaining capacity associate with their  $n_{\text{top}}$  strongest UAVs, where each O-RU  $\ell$  admits  $n_{\text{assign}}(\ell) = \min\left\{n_{\text{top}}, \tau_p \sum_{k=1}^K a_{k\ell}\right\}$ . This improves SE and balances load by leveraging unused capacity.
- Stage 3: QoS-driven refinement (Lines 15–28): UAVs violating QoS (SE $_k$  < SE $_k^{\min}$ ) are identified and iteratively connected to additional candidate O-RUs (up to  $\lceil L/2 \rceil$ ) in descending order of  $\{\beta_{k\ell}\}$ , provided capacity is available. This stage ensures fairness by recovering QoS violations.
- a) Computational Complexity Analysis: Stage 1 requires  $\mathcal{O}(KL\log L)$  operations as each UAV selects its strongest O-RU. Next, Stage 2 sorts K UAVs per O-RU, yielding  $\mathcal{O}(LK\log K)$ , and finally, Stage 3 examines at most  $\lceil L/2 \rceil$  candidates for each QoS-violating UAV, with worst-case cost  $\mathcal{O}(|\mathcal{U}|L\log L)$ . Hence, the total complexity is  $\mathcal{O}(KL\log L + LK\log K + |\mathcal{U}|L\log L) \approx \mathcal{O}(KL)$ , since typically  $|\mathcal{U}| \ll K$ .

# B. UL Data Transmit Power Allocation

Given fixed UAV-O-RU association matrix **A**, the UL data transmit power allocation problem is formulated as follows:

**P2:** 
$$\max_{\{p_u^{\mathbf{k}}\} \in [0, p^{\max}]} \quad \min_{k \in \mathcal{K}} \quad \mathsf{SE}_k, \tag{6a}$$

Although the reformulated problem can be solved using an interior-point solver such as CVX [18], the associated computational complexity is prohibitively high for near-RT RIC operation. To address the computational complexity of the CVX-based solver, we propose a *bisection-guided fixed-point power control* (BG-FPPC) algorithm that achieves near-optimal maxmin SINR performance with significantly reduced complexity, as described next.

$$\Gamma_{k} = \frac{\left| \sqrt{p_{k}^{\mathbf{u}}} \sum_{\ell \in \mathcal{L}_{k}} \alpha_{k\ell} \mathbb{E} \left[ (\mathbf{v}_{k\ell})^{H} \mathbf{h}_{k\ell} \right] \right|^{2}}{p_{k}^{\mathbf{u}} \sum_{\ell \in \mathcal{L}_{k}} \alpha_{k\ell}^{2} \left( \mathbb{E} \left[ |(\mathbf{v}_{k\ell})^{H} \mathbf{h}_{k\ell}|^{2} \right] - |\mathbb{E} \left[ (\mathbf{v}_{k\ell})^{H} \mathbf{h}_{k\ell} \right] |^{2} \right) + \sum_{i \neq k} p_{i}^{\mathbf{u}} \sum_{\ell \in \mathcal{L}_{k}} \alpha_{k\ell}^{2} \mathbb{E} \left[ |(\mathbf{v}_{k\ell})^{H} \mathbf{h}_{i\ell}|^{2} \right] + \sigma^{2} \sum_{\ell \in \mathcal{L}_{k}} \alpha_{k\ell}^{2} \mathbb{E} \left[ ||\mathbf{v}_{k\ell}||^{2} \right],$$
(2)

$$\Gamma_{k} = \frac{\left| \sqrt{p_{k}^{\mathbf{u}}} \sum_{\ell=1}^{L} a_{k\ell} \alpha_{k\ell} \mathbb{E}\left[ (\mathbf{v}_{k\ell})^{H} \mathbf{h}_{k\ell} \right] \right|^{2}}{p_{k}^{\mathbf{u}} \sum_{\ell=1}^{L} a_{k\ell} \alpha_{k\ell}^{2} \left( \mathbb{E}\left[ |(\mathbf{v}_{k\ell})^{H} \mathbf{h}_{k\ell}|^{2} \right] - |\mathbb{E}\left[ (\mathbf{v}_{k\ell})^{H} \mathbf{h}_{k\ell} \right] |^{2} \right) + \sum_{i \neq k} p_{i}^{\mathbf{u}} \sum_{\ell=1}^{L} a_{k\ell} \alpha_{k\ell}^{2} \mathbb{E}\left[ |(\mathbf{v}_{k\ell})^{H} \mathbf{h}_{i\ell}|^{2} \right] + \sigma^{2} \sum_{\ell=1}^{L} a_{k\ell} \alpha_{k\ell}^{2} \mathbb{E}\left[ ||\mathbf{v}_{k\ell}|^{2} \right]}, \quad (3)$$

**Algorithm 1:** Adaptive Joint UAV and O-RU-centric based Association Assignment Scheme

```
Input: K, L, \tau_p, \beta, SE_k^{\min}, n_{top} = 3
      Output: A
    Initialize: \mathbf{A} \leftarrow \mathbf{0}_{K \times L};
 2 for k \leftarrow 1 to K do
3 | \ell^* \leftarrow \arg \max_{\ell} \beta_{k\ell};
              if \sum_{k'=1}^{K} a_{k'\ell^*} < \tau_p then
                a_{k\ell^*}^* \leftarrow 1;
              end if
     end for
     for \ell \leftarrow 1 to L do
 8
              Sort UAVs by descending \beta_{k\ell}: \{k_1, k_2, \dots, k_K\};
10
               n_{\text{assign}} \leftarrow \min \left\{ n_{\text{top}}, \tau_p - \sum_{k=1}^K a_{k\ell}^* \right\};
              for i \leftarrow 1 to n_{assign} do
11
                a_{k_i\ell}^* \leftarrow 1;
              end for
13
14 end for
    Compute \{\Gamma_k\} and \{SE_k\} with \mathbf{A}^*;
15
     \mathcal{U} \leftarrow \{k : SE_k < SE_k^{\min}\};
17 for k \in \mathcal{U} do
18
               while SE_k < SE_k^{\min} \& x \leq \lceil L/2 \rceil do
19
                       \begin{array}{l} \mathcal{L}_k \leftarrow \{\ell: a_{k\ell}^* = 1\}; \\ \text{Sort O-RUs by descending } \beta_{k\ell} \colon \mathcal{C} \leftarrow \{\ell_1, \dots, \ell_L\} \setminus \mathcal{L}_k; \end{array}
20
21
22
                       if x \leq |\mathcal{C}| then
23
                                a_{k\mathcal{C}(x)}^* \leftarrow 1;
24
                                Recompute \{\Gamma_k\} and update \{SE_k\};
25
                        end if
26
                        x \leftarrow x + 1:
27
              end while
28
    end for
```

1) Proposed BG-FPPC Algorithm: Our proposed BG-FPPC algorithm combines classical fixed-point iteration [19] with adaptive bisection to achieve near-optimal max-min SINR with reduced complexity. The complete procedure is summarized in Algorithm 2.

The algorithm starts by setting power of all UAVs at maximum power. Bisection SINR bounds are set as  $\gamma_{\min}$  and  $\gamma_{\max}$ . The precomputed SINR coefficients  $\{a_k,b_{ki},c_k\}$  represent desired signal, inter-UAV interference, and noise, respectively.

The algorithm employs two nested loops. An **outer bisection** (Lines 2–17) searches for the maximum feasible target SINR  $\gamma^*$  by iteratively testing the midpoint  $\gamma_{\rm mid} = (\gamma_{\rm min} + \gamma_{\rm max})/2$  (Line 3), while an **inner fixed-point iteration** (Lines 5–10) computes the minimum power required to achieve the current target via the update in Line 7. At each bisection step, feasibility is checked by verifying  $\max_k p_k^u \leq p^{\rm max}$  (Line 10). The solution is stored if feasibility is satisfied and  $\gamma_{\rm min}$  is updated with the value of  $\gamma_{\rm mid}$  (Lines 12–13), otherwise it updates  $\gamma_{\rm max}$  (Line 15). The process terminates when the relative gap between  $\gamma_{\rm max}$  and  $\gamma_{\rm min}$  is below  $\epsilon_{\rm bisect}$ .

The key novelty of Algorithm 2 is the adaptive target SINR mechanism. Rather than fixing  $\gamma$  a priori as in standard Foschini-Miljanic approaches [19], our algorithm systematically explores the feasible region to solve the max-min problem

**Algorithm 2:** Bisection-Guided Fixed-Point Power Control (BG-FPPC)

```
Input: \{a_k, b_{ki}, c_k\}, P_{\max}, \Gamma_{\text{init}}, \epsilon_{\text{bisect}} = 10^{-4}, \epsilon_{\text{FP}} = \overline{10^{-3}},
                        N_{\rm max}^{\rm FP} = 20
       Output: \mathbf{p}^{\star}, \gamma^{\star}
  1 Initialize: \mathbf{p}_{\text{init}} \leftarrow p^{\text{max}} \mathbf{1}, \ \mathbf{p}^{\star} \leftarrow \mathbf{p}_{\text{init}}, \ \gamma_{\text{min}} \leftarrow 0,
          \gamma_{\max} \leftarrow 1.5 \cdot \max_k \Gamma_{\text{init},k}, \ \gamma^* \leftarrow \min_k \Gamma_{\text{init},k};
      while (\gamma_{\rm max} - \gamma_{\rm min})/\gamma_{\rm max} > \epsilon_{bisect} do
                \gamma_{\text{mid}} \leftarrow (\gamma_{\text{min}} + \gamma_{\text{max}})/2;
  3
                \mathbf{p}^{(0)} \leftarrow p^{\max} \mathbf{1}, n \leftarrow 0;
  4
                repeat
  5
                         for k = 1, \dots, K do
  6
                            I_k \leftarrow \sum_{i \neq k} b_{ki} p_i^{(n)} + c_k, p_k^{(n+1)} \leftarrow \frac{\gamma_{\text{mid}}}{a_k} \cdot I_k;
  7
  8
                         n \leftarrow n + 1;
                until \|\mathbf{p}^{(n+1)} - \mathbf{p}^{(n)}\|_{\infty} < \epsilon_{FP} \cdot p^{\max} or n = N_{\max}^{FP};
10
                if \max_k p_k^{(n)} \leq p^{\max} then
11
                         \gamma_{\min} \leftarrow \gamma_{\min};
12
                         \mathbf{p}^{\star} \leftarrow \min(\mathbf{p}^{(n)}, p^{\max}\mathbf{1}), \gamma^{\star} \leftarrow \min_{k} SINR_{k}(\mathbf{p}^{\star});
13
14
                else
15
                        \gamma_{\text{max}} \leftarrow \gamma_{\text{mid}};
                end if
16
17 end while
```

globally, avoiding local optima of gradient-based methods.

a) Computational Complexity: Each fixed-point iteration incurs  $\mathcal{O}(K^2)$  for interference computation. With  $I_{\text{FP}} \approx 5\text{--}15$  inner iterations and  $I_{\text{bisect}} = \mathcal{O}(\log(1/\epsilon_{\text{bisect}}))$  bisection steps, the total complexity is  $\mathcal{O}(I_{\text{bisect}} \cdot I_{\text{FP}} \cdot K^2) = \mathcal{O}(K^2)$ . Compared to CVX's  $\mathcal{O}(K^{3.5})$  [18], this represents a  $\mathcal{O}(K^{1.5})$  reduction, confirmed by over  $10\times$  runtime reduction in Section V.

#### C. The Overall Solution to the Problem P0

We solve the coupled problem **P0** via AO, initialized with  $p_k^{\rm u}=p^{\rm max}$ . Each iteration alternates between: (i) solving for association **A** with fixed power (Algorithm 1), and (ii) solving for power  $\{p_k^{\rm u}\}$  with fixed **A** (Algorithm 2). The process terminates when the objective (4a) improvement falls below  $\epsilon$  or iteration count reaches  $I_{\rm max}$ . Convergence is guaranteed via monotonic improvement of the bounded objective, typically within 3–5 iterations, with per-iteration complexity  $\mathcal{O}(KL+K^2)$ .

# V. NUMERICAL EVALUATION

This section evaluates the performance of the proposed UAV–O-RU association and UL transmit power allocation schemes in an O-RAN-enabled CF mMIMO network. Table I summarizes the key simulation parameters following 3GPP UMa-AV specifications [11], [12]. The AO algorithm uses  $\epsilon=0.001$  and  $I_{\rm max}=15$  as convergence and iteration limits, respectively. UAV trajectories are assumed predetermined and fixed. Pilot sequences are randomly assigned to UAVs and transmitted at full power. All results are averaged over 500

Monte Carlo realizations, each with independent O-RU and UAV positions, altitudes, and channel realizations.

TABLE I: Simulation Parameters

| TABLE 1. Sillulation Farameters               |                                       |
|-----------------------------------------------|---------------------------------------|
| Parameter                                     | Value                                 |
| Coverage area                                 | $1 \times 1 \text{ km}^2$             |
| Number of O-RUs $(L)$                         | 100                                   |
| Antennas per O-RU $(N_{\ell})$                | 4                                     |
| UAV altitude range                            | [50, 150] m                           |
| Carrier frequency $(f_c)$                     | 2.6 GHz                               |
| Coherence block $(\tau_c)$ / Pilot $(\tau_p)$ | 200 / 10 symbols                      |
| Rician $K$ -factor range                      | [0, 20] dB                            |
| Shadow fading $\sigma_{\rm sh}$ (LoS / NLoS)  | 4 / 6 dB                              |
| Angular spread at O-RUs (mean)                | $[5^{\circ}, 15^{\circ}] (8^{\circ})$ |
| Max UAV transmit power $(p^{\max})$           | 23 dBm                                |
| Noise PSD / Noise figure                      | −174 dBm/Hz / 9 dB                    |

1) Minimum SE Performance: Fig. 2 compares the average minimum SE performance between six schemes combining different UAV-O-RU association and UL transmit power allocation strategies. For association, we consider: (a) the baseline (BA) scheme from [17], where both UAV and O-RU-centric associations are leveraged, and (b) the proposed association (PA) in Algorithm 1. For power allocation, we consider: (a) full power transmission (FP), (b) the proposed Algorithm 2 (PP), and (c) a CVX-based solver applying bisection to problem **P2** (TP). So, the six benchmarks are: (i) 'Baseline' (BA + FP), (ii) 'PA + FP', (iii) 'BA + PP', (iv) 'BA + TP', (v) 'PA + PP', and (vi) 'PA + TP'. The AO framework from Section IV-C is applied only to schemes (v) and (vi), as the association schemes are computed independently of power allocation.

Fig. 2 demonstrates substantial improvements in the minimum SE performance achieved by the proposed schemes. The joint optimization of association and power allocation (PA + PP or PA + TP) attains up to a 440% gain in minimum SE over the Baseline, highlighting the effectiveness of these two schemes. To isolate individual contributions, we note that the proposed association alone (PA) yields up to an 297.8% improvement over the Baseline, owing to the QoS-driven refinement in Algorithm 1, which dynamically assigns additional serving O-RUs to weak UAVs, a feature that is not included in [17]. As for the proposed power allocation scheme (Algorithm 2), it improves the minimum SE performance by up to 82.6% compared to the Baseline. Notably, the proposed BG-FPPC algorithm (PP) achieves the same minimum SE as the CVX-based solver (TP), confirming its global optimality. This equivalence arises because (a) the outer bisection loop systematically searches for the maximum feasible target SINR  $\gamma^*$ , and (b) the inner fixed-point iteration precisely computes the minimum power required to meet each target, ensuring that no feasible solution is overlooked. As expected, the minimum SE decreases with increasing UAV density for all schemes due to higher inter-UAV interference. Interestingly, the proposed association schemes (PA + PP and PA + TP) exhibit steeper degradation than the baseline since they proactively assign more O-RUs to QoSconstrained UAVs, thereby increasing interference sensitivity under dense deployments. In contrast, the baseline association remains static and thus less responsive to variations in UAV

![](_page_4_Figure_5.jpeg)

Fig. 2: Average minimum SE performance of different schemes for varying UAV K with  $SE^{min} = 1$  bit/s/Hz.

![](_page_4_Figure_7.jpeg)

Fig. 3: Average success rate performance of different schemes for varying UAV K with  $\mathrm{SE}^{\min}=1$  bit/s/Hz.

density.

- 2) Success Rate Performance: Fig. 3 shows the average success rate performance, defined as the percentage of UAVs achieving an SE greater than the target threshold SE<sup>min</sup>. Although the baseline association combined with power optimization (in BA + PP and BA + TP schemes) enhances the minimum SE (as shown in Fig. 2), these schemes fail to meet SEmin for any UAV, resulting in a zero success rate across all UAV densities. This limitation arises because the baseline association in [17] does not incorporate QoS-aware O-RU selection, and power control alone cannot compensate for inadequate serving O-RU selection for weak UAVs. On the other hand, the proposed association scheme achieves a 100% success rate for  $K \leq 90$  in PA + PP and PA + TP schemes, corresponding to up to a 135% improvement over the Baseline. When K = 100, the success rate of PA + PP and PA + TP decreases to approximately 80% due to resource scarcity under increased interference, whereas the Baseline exhibits minimal variation with density, consistent with the trend observed in Fig. 2. It is important to note that PA + TP and PA + PP yield identical success rates across all UAV densities, indicating that both power allocation strategies (proposed and CVX-based) equally uphold the QoS guarantees ensured by Algorithm 1. Interestingly, even PA + FP achieves success rates comparable to PA + PP and PA + TP for  $K \le 90$  (differences below 6.5%), confirming that QoS-driven O-RU assignment in Algorithm 1 is the dominant factor in meeting SE<sup>min</sup>, with power optimization providing marginal additional benefit. At K = 100, however, PA + FP provides a 13.4% higher success rate than PA + PP and PA + TP because full power transmission offers greater robustness under resource scarcity.
- 3) Fairness Performance: Fig. 4 presents the average fairness performance, quantified in percentage using Jain's fairness index. All schemes employing power optimization (BA + PP, BA + TP, PA + PP, and PA + TP) achieve 100% fairness, representing a 70% improvement over the Baseline. This substantial gain arises because max-min power allocation inherently promotes equitable SE distribution by prioritizing power allocation to weak UAVs. In comparison, the proposed association alone

![](_page_5_Figure_0.jpeg)

Fig. 4: Average fairness performance of different schemes for varying UAV K with  $SE^{min} = 1$  bit/s/Hz.

![](_page_5_Figure_2.jpeg)

Fig. 5: Average runtime of different schemes for varying UAV K with  $SE^{min} = 1$  bit/s/Hz.

(PA + FP) yields a 50.4% improvement over the Baseline, confirming that QoS-driven O-RU assignment enhances fairness, though it achieves approximately 11% lower fairness than power-optimized schemes. This gap occurs because, without power optimization, even effective O-RU association cannot fully equalize SE across UAVs with diverse channel conditions, establishing power control as the dominant fairness-enabling mechanism.

4) Computational Complexity Performance: Fig. 5 illustrates the average runtime for all schemes except the Baseline. The proposed BG-FPPC algorithm (PP) achieves up to 99.1% runtime reduction compared to the CVX-based scheme (TP), with BA + PP outperforming BA + TP by up to 99.9%. Both BA + PP and PA + PP schemes with proposed algorithm (Algorithm 2) achieve 10-150 ms duration, which is within the near-RT RIC time constraint runtime, enabling O-RAN compliant real-time deployment. Notably, PA + PP incurs only 3.4% additional runtime compared to PA + FP, confirming that the AO framework for coordinating the proposed association and power allocation schemes introduces minimal computational overhead.

# VI. CONCLUSION

This paper presents a joint UAV-O-RU association and power allocation framework for O-RAN-enabled CF mMIMO systems supporting 5G aerial corridors. The key contributions include: (i) an adaptive association algorithm that dynamically selects serving O-RUs by combining UAV and O-RU-centric clustering, followed by QoS-driven refinement for weak UAVs, (ii) a computationally efficient power control method that integrates bisection search with fixed-point iteration achieving global optimality, and (iii) an AO framework integrating both solutions. The framework adopts a CKM within the O-RAN non-RT RIC to mitigate CSI acquisition overhead. Simulation results demonstrated substantial enhancements in minimum SE, QoS compliance, fairness, and computational efficiency compared to baseline approaches. Our analysis reveals that association design is critical for QoS guarantees, while power control dominates fairness. The proposed schemes yield an optimal

solution within sub-second runtime, suitable for O-RAN compliant real-time deployment. Future work will investigate joint UAV trajectory optimization to enhance coverage and SE in dynamic aerial networks.

#### REFERENCES

- [1] A. Bhuyan, I. Guvenc, H. Dai, M. L. Sichitiu, S. Singh, A. Rahmati, S. J. Maeng, E. Ozturk, and M. M. U. Chowdhury, "Advances in secure 5G network for a nationwide drone corridor," Tech. Rep. INL/CON-21-65310-Revision-0, Idaho National Laboratory, Idaho Falls, ID, USA, Mar. 2022.
- [2] N. Cherif, W. Jaafar, H. Yanikomeroglu, and A. Yongacoglu, "3D aerial highway: The key enabler of the retail industry transformation," *IEEE Communications Magazine*, vol. 59, Sept. 2021.
- [3] P. Tarafder, I. Ahmed, D. B. Rawat, M. Z. Hassan, and K. Hasan, "Digitaltwin empowered site-specific radio resource management in 5G aerial corridor," in *IEEE Military Conference on Communications (MILCOM)*, 2025.
- [4] S. Karimi-Bidhendi, G. Geraci, and H. Jafarkhani, "Optimizing cellular networks for UAV corridors via quantization theory," *IEEE Transactions* on Wireless Communications, vol. 23, no. 10, pp. 14924–14939, 2024.
- [5] L. Bertizzolo, T. X. Tran, J. Buczek, B. Balasubramanian, R. Jana, Y. Zhou, and T. Melodia, "Streaming from the air: Enabling drone-sourced video streaming applications on 5G open-RAN architectures," *IEEE Transactions on Mobile Computing*, vol. 22, no. 5, pp. 3004–3017, 2023.
- [6] H. Li, X. Tang, D. Zhai, R. Zhang, B. Li, H. Cao, N. Kumar, and A. Almogren, "Energy-efficient deployment and resource allocation for O-RAN-enabled UAV-assisted communication," *IEEE Transactions on Green Communications and Networking*, vol. 8, no. 3, pp. 1128–1139, 2024.
- [7] E. Björnson and L. Sanguinetti, "Making cell-free massive MIMO competitive with MMSE processing and distributed combining," *IEEE Transactions on Wireless Communications*, vol. 19, no. 1, pp. 77–90, 2020
- [8] Y. Zeng, J. Chen, J. Xu, D. Wu, X. Xu, S. Jin, X. Gao, D. Gesbert, S. Cui, and R. Zhang, "A tutorial on environment-aware communications via channel knowledge map for 6G," *IEEE Communications Surveys & Tutorials*, vol. 26, no. 3, pp. 1478–1519, 2024.
- [9] A. Malik, M. Ahadi, F. Kaltenberger, K. Warnke, N. T. Thinh, N. Bouknana, C. Thienot, G. Onche, and S. Arora, "From concept to reality: 5g positioning with open-source implementation of UL-TDoA in openairinterface," arXiv preprint arXiv:2409.05217, 2024.
- [10] M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, and M. Debbah, "A tutorial on UAVs for wireless networks: Applications, challenges, and open problems," *IEEE Communications Surveys & Tutorials*, vol. 21, no. 3, pp. 2334–2360, 2019.
- [11] 3GPP, "Enhanced LTE support for aerial vehicles," Tech. Rep. TR 36.777, 3rd Generation Partnership Project (3GPP), 2017.
- [12] 3GPP, "Study on channel model for frequencies from 0.5 to 100 GHz," Tech. Rep. TR 38.901, 3rd Generation Partnership Project (3GPP) / ETSI, 2024
- [13] G. Geraci, C. D'Andrea, A. García-Rodríguez, and S. Buzzi, "Cell-free massive MIMO for UAV communications," in 2019 IEEE International Conference on Communications Workshops (ICC Workshops), pp. 1–6, 2019
- [14] A. Adhikary, J. Nam, J.-Y. Ahn, and G. Caire, "Joint spatial division and multiplexing—the large-scale array regime," *IEEE Transactions on Information Theory*, vol. 59, no. 10, pp. 6441–6463, 2013.
- [15] S. M. Kay, Fundamentals of Statistical Signal Processing: Estimation Theory. Prentice Hall, 1993.
- [16] B. Hassibi and B. M. Hochwald, "How much training is needed in multiple-antenna wireless links?," *IEEE Transactions on Information Theory*, vol. 49, no. 4, pp. 951–963, 2003.
- [17] M. Sarker and A. O. Fapojuwo, "Access point-user association and auction algorithm-based pilot assignment schemes for cell-free massive MIMO systems," *IEEE Systems Journal*, vol. 17, no. 3, pp. 4301–4312, 2023
- [18] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, UK: Cambridge University Press, 2004.
- [19] G. J. Foschini and Z. Miljanic, "A simple distributed autonomous power control algorithm and its convergence," *IEEE Trans. Veh. Technol.*, vol. 42, no. 4, pp. 641–646, 1993.
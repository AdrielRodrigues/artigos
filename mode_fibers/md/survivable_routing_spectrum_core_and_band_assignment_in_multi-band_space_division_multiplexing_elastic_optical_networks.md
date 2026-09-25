---
title: "Survivable Routing, Spectrum, Core and Band Assignment in Multi-Band Space Division Multiplexing Elastic Optical Networks"
tema_principal: mode_fibers
temas_relacionados: []
pdf: ../pdf/survivable_routing_spectrum_core_and_band_assignment_in_multi-band_space_division_multiplexing_elastic_optical_networks.pdf
---

# Survivable Routing, Spectrum, Core and Band Assignment in Multi-Band Space Division Multiplexing Elastic Optical Networks

Zhihuan Luo , Shan Yin , Ligang Zhao, Zhenhao Wang, Wenchao Zhang, Liyou Jiang , and Shanguo Huang , *Member, IEEE* 

Abstract—The rapid growth in Internet traffic has contributed to the need to expand network transmission capacity. Multi-band (MB) using existing standard single-mode fibers (SMFs) in the free band is an ideal way to increase the capacity of the fiber. However, the introduction of MB has transferred space division multiplexing - elastic optical networks (SDM-EONs) to multi band-SDM-EONs (MB-SDM-EONs), and changed routing, spectrum and core assignment (RSCA) problem to the routing, spectrum, core and band assignment (RSCBA) problem. At the same time, it introduces a new issue named stimulated Raman scattering (SRS), which affects transmission quality. Although an expanded fiber can carry more services, a large number of services will be interrupted if a link fails, which will bring huge losses. Therefore, it is necessary to propose a reasonable protection strategy to ensure reliable transmission quality. In this paper, the survivable RSCBA problem in MB-SDM-EONs is studied, which copes with link failures and considers SRS in signal-to-noise ratio (SNR) analysis. In order to solve the problem, we propose a band partition protection scheme: working and protection resources are allocated in different frequency bands for increasing SNR in a fault-free network. We formulate this problem and band partition protection scheme as an integer linear programming (ILP) model, which takes into account inter-core crosstalk and SNR analysis. Furthermore, a heuristic algorithm based on genetic algorithm is proposed for large-scale networks. We evaluate the performance of the proposed approaches through experimental simulation. The results demonstrate that both proposed approaches are effective in finding the optimal solutions.

Index Terms—Genetic algorithm (GA), multi band (MB), routing- spectrum- core-band assignment (RSCBA), signal-to-noise ratio (SNR), space division multiplexing (SDM), survivability.

#### I. INTRODUCTION

RAFFIC demands on transport network have continued to grow in recent decades, including the upcoming deployment of 5G services, the growth of IP traffic, cloud computing,

Manuscript received September 30, 2021; revised December 24, 2021 and February 21, 2022; accepted March 19, 2022. Date of publication March 28, 2022; date of current version June 1, 2022. This work was supported by the National Natural Science Foundation of China under Grants 62125103,61821001, and 61601054. (Corresponding author: Shan Yin.)

The authors are with the State Key Laboratory of Information Photonics and Optical Communications, Beijing University of Posts and Telecommunications, Beijing 100876, China (e-mail: luozhihuan@bupt.edu.cn; yinshan@bupt.edu.cn; zlgtop@163.com; wang-zh@bupt.edu.cn; zh\_wenchao@163.com; jiangliyou@bupt.edu.cn; shghuang@bupt.edu.cn).

This article has supplementary material provided by the authors and color versions of one or more figures available at https://doi.org/10.1109/JLT.2022.3161502.

Digital Object Identifier 10.1109/JLT.2022.3161502

TABLE I
[6] BANDS THAT CAN BE USED FOR OPTICAL COMMUNICATIONS

| Name                          | О             | Е             | S             | С             | L             |
|-------------------------------|---------------|---------------|---------------|---------------|---------------|
| Wavelength<br>Range (nm)      | 1260-<br>1360 | 1360-<br>1460 | 1460-<br>1530 | 1530-<br>1565 | 1565-<br>1625 |
| C Band                        |               |               |               | ←35nm→        |               |
| C+L Band                      |               |               |               | ← 951         | nm →          |
| Typical Fiber<br>Loss (dB/km) | 0.36          | 0.28          | 0.22          | 0.18          |               |

and the interconnection between data centers [1]. For example, Google's data center network capacity has expanded 100 times over 10 years, reaching more than 1 Pbps of bisection bandwidth [2]. The annual growth rate in bandwidth is expected to be between 20% and 60%, while Google's long-haul network has grown dramatically by approximately two orders of magnitude in capacity [3]. Several researchers have alerted that the core optical network capacity is about to run out of capacity, a severe situation known as "capacity crunch" [4]. Therefore, it is urgent to solve the problem of depletion of optical network capacity.

Among the existing solutions to avoid the problem of network capacity depletion, Space Division Multiplexing (SDM) and Multi-band (MB) are two dominant technologies. SDM is a technology that uses multiplicity of space channels from core dimension and mode dimension to increase the capacity of optical communication. While, MB increases the capacity of a single fiber by extending the operating frequency bands from the usual C- frequency band to the L-, S-, E- and Ofrequency bands on the standard single-mode fibers (SMFs) already deployed [5]. Bands that can be used for optical communications can be seen in Table I. Multi-core fiber (MCF) is one type of SDM, which is easy to realize, but brings inter-core crosstalk. As for MB, while it is the most viable short-term solution to increase the capacity of optical networks and does not require the installation of new fiber, it requires new transceivers, amplifiers, and ROADM upgrades for use in frequency bands other than the C-band. Currently, network operators are trying to implement MB solutions by installing commercial C+L-band transmission lines. As commercial C+L-band systems are entering the market, research has shifted to the adjacent S-band [7]. While, MB alone can respond to more traffic services in the short term, but from a long-term perspective and the trend

0733-8724 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

of traffic growth, for maximum throughput, it is necessary to optimize each of dimensions [8]. Motivated by the advantages of both two technologies, we suppose that combining SDM and MB (MB-SDM) is a good choice, which can achieve maximum throughput. However, it also raises some new challenges. Unlike RSCA issues in traditional SDM, where routing, spectrum and core assignment (RSCA) problem needs to be solved, multiple frequency bands increase the impairments over the transmission medium in MB-SDM. Thus, when analyzing signal-to-noise ratio (SNR), we need to re-identify the relevant interferences and redefine the relevant SNR formulas during resource allocation to estimate quality of transmission (QoT). Inter-channel stimulated Raman scattering (SRS) is a nonlinear effect that transfers power from high frequency components to lower frequency components within the same optical spectrum. Since SRS modifies the fiber gain/loss profile, it induces spectral tilt, modifies the amplified spontaneous emission (ASE) noise and allows for different generation of non-linear interference (NLI) in the band where the power is transmitted [9]. Because SRS is a broadband phenomenon with maximum efficiency at ∼13 THz spectral down-spacing, it is associated with C- only system but is too weak and can be ignored, since the spectral tilt it causes is very weak and can be compensated for, e.g., by gain flattening filters. While in multiband systems, transmission approaches 13 THz of continuous spectral occupation (such as for C+L-band line systems), so SRS increases and becomes an important factor on SNR estimation [10]. There is also a survey which proves that outage occurs for some of lightpaths, if ignoring the SRS process in the SNR estimation. Thus, it is important to consider SRS in SNR analysis [11]. Meanwhile, multi-band adds the band dimension at the resource level. Thus in MB-SDM, the RSCA problem evolves into the routing, spectrum, core and band assignment problem (RSCBA).

In large-scale networks, there are optical outages caused by fiber level failures [12]. Since a single link or path failure can affect several established connections and cause enormous losses in terms of resources. It is necessary to improve their survivability and minimize failure repercussions. Therefore, survivable RSCBA algorithms for resource allocation with protection schemes are needed in MB-SDM, so that the networks can provide good service to the requests. The core of the protection scheme is to quickly activate an alternative link/path when a request working one fails, which requires that the working link/path and the alternative link/path not overlap. In this way, it allows the request to continue transmission. In previous studies, protection strategies are mainly divided into two categories: hot backup strategy and cold backup strategy. The hot backup strategy is a protection strategy, in which the backup resources are executed simultaneously with the primary resources for timely recovery at the cost of high workload. While in cold backup strategy, the backup resources are not treated as active workload until the failure occurs to reduce resource utilization with the cost of longer recovery time [13]. Among the known link protection methods, a typical hot backup method is dedicated backup path protection (DBPP), while a typical cold backup method is shared backup path protection (SBPP). However, due to the disjoint nature of the work-backup resources and the multi-band feature in MB-SDM, we can propose a protection scheme that differs from typical backup strategies.

## *A. Related Work*

In the past few years, MB was promoted due to the dramatic network traffic growth. We hereby review the related work from five aspects in the following: 1) Related MB technology; 2) SRS on QoT estimation; 3) Resource allocation problem in SDM- EONs; 4) Combination of MB and SDM; 5) Network survivability or resource backup.

For MB technology, the author in [14] outlined components and techniques for implementing MB transmission through single-mode fiber (SMF). Several works have evaluated the transmission capacity through MB techniques using multiple spectral band combinations from the O- to L-band [15]–[17]. Nowadays, C + L-band technology is relatively mature and is currently in commercial use. [6] showed a record demonstration of 800 km transmission at 56.4 Tb/s C+L-band using commercial C+L-band system technology. In addition, there are some senior researches considering using S-, O-, and U- bands [18], [19]. [20] indicated the feasibility of further extending O-band transmission systems in long-haul optical networks. [17] reported an ultra-wideband WDM system across the S+C+Lband. [16] demonstrated a 5-band (O-, E-, S-, C-, and L-) WDM coherent transmission over 60-km of SSMF. In the article [21], the authors reviewed challenges and opportunities for C+L-line systems and compared C- and C+L-systems, showing the better propagation performance of the latter one, which also proves that C+L- systems represent a viable solution to scale capacity in optical networks. Meanwhile, authors in [22] pointed out that the C-band performance of the C-only system exceeds that of its C+L- system counterpart (C-band in C+L- system) due to energy transfer from C-band carriers, which increases the C-band loss.

The discussion of the effect of SRS on QoT estimation is also an important research issue in the MB field. Several works focus on QoT estimation affected by nonlinear interference (NLI) disturbances jointly with the stimulated Raman scattering (SRS), they prove that the transmission power and SRS play an important role in multi-band optical transmission [22]. In [23], [43], the inter-channel SRS (ISRS) process has been modelled, together with ASE noise and NLI to define SNR. In this way, the SNR can be effectively considered as the unique QoT parameter. Based on SNR, [25] studied multiband power control strategies to maximize and flatten the GSNR over C+L- line systems. [10] aimed to maximize QoT by applying a multiband optimized optical power control.

On the other hand, the resource allocation problem in SDM-EONs has been studied in many papers. Here we only review the research on resource allocation in MB-EON. The main objective of [26] is to minimize node resources at low cost in ultra-wideband wavelength division multiplexed networks. [6] presented the evolution of C+L-band systems from a network design perspective. In [5] an algorithm was proposed for modulation level, band and spectrum assignment to reduce blocking probability in MB transmission. In [27], the authors studied the ISRS-aware RMLSA problem in MB-EONs, and proposed ILP models and heuristic algorithms to solve the problem. [28] presented an approach based on reinforcement learning (RL) techniques to accommodate MB-EON resources. In [29], the blocking performance of a heuristic and a deep reinforcement learning approach for resource provisioning in a dynamic MB-EON is evaluated. In the above studies, most of researches focus on SNR analysis in resource allocation without considering band assignment.

In recent years, most existing studies have been devoted to comparing MB and SDM to highlight the superiority of one over the other. Only a few articles have verified the superior performance derived by the combination of MB and SDM. [30] showed that MCFs over C+L- bands limited to the diameter of SMF can achieve a total decoded throughput of 596.4 Tb/s, per-core throughputs on a par with the highest reported in SMF. In [31], the authors have demonstrated broadband transmission of 359 × 24.5 GBaud 16-QAM channels across C+ L- bands over 2040 km, with strongly coupled, three-core multi-core fiber. [32] proved high capacity transmission in a three-core fiber within C+L- band. 0.61 Pb/s S-, C-, and L-band transmission in a 4-Core fiber has been experimented in [33]. [34] presented high efficiency C+ L-band transmission over a 38-core-3-mode fiber. However, there has been no work considering the resource allocation RSCBA problem in MB-SDM in the above studies.

In terms of network survivability or resource backup, [13] proposes an optimization model that takes into account the probability of failure associated with the workload to derive a primary and backup resource allocation to minimize the maximum expected unavailable time. There are also some researches on link protection in SDM-EON. For example, [35] proposed a distance-adaptive energy-aware resource allocation algorithm using a survival multipath scheme. The authors in [36] proposed a p-cycle algorithm with independent paths to provide protection in case of a link failure in SDM. In addition, [37] formulated RSCA problem as a mixed-integer linear programming (MILP), in which dedicated and shared path protection schemes are supported. Although there have been many works in SDM-EON resource backup, however, no specific survivability study considering multi-band characteristics for MB-SDM has been proposed so far.

## *B. Paper Contributions and Organization*

To the best of our knowledge, so far the survivable RSCBA problem considering SRS effect has not been studied. In this paper, we propose a band partition protection scheme based on multi-band characteristics and the idea of cold backup: working resources are allocated in C-band and protection resources are allocated in L-band, which aims to increase SNR on C-band with no or a low amount of link failures in network. Since the performance of C-band is worse than L-band due to power transfer from one band to another, the band partition protection scheme tries to reduce the use of L-band to reduce the impact on C-band. It should be noted that it is a cold backup strategy, which means the backup spectrum resources in L-band are reserved, they are not used for transmission with working spectrum resources. In simple terms, only when the link fails, the corresponding reserved backup resources are enabled. On the other hand, current commercial optical fibers mainly use C-band for service transmission, and the multi-band is implemented by the upgrading from C- only system to C+L- system. In our study, we put working resources on the C-band to maintain a similar scenario to the original transmission scenario, which tries to reduce the control costs from services adjustments.

In this paper, we develop an integer linear programming (ILP) model for the band partition protection scheme and RSCBA problem, taking both SRS effect and inter-core crosstalk into account. However, since the number of FSs and demands are too large in real MB-SDM, the ILP model can not be solved in polynomial time, thus we propose a heuristic algorithm based on genetic algorithm to serve demands, which supports the band partition protection scheme. In summary, the key contributions of this paper are as follows:

- 1) Propose a band partition protection scheme: working resources in C-band and protection resources in L- band.
- 2) Formulating the band partition protection scheme, one-toone dedicated protection scheme and RSCBA problem as ILP in MB-SDM.
- 3) Formulating spectrum assignment constraints in such a way to consider SRS and XT crosstalk.
- 4) Proposing heuristic algorithm that supports the band partition protection scheme based on genetic algorithm. To evaluate the performance of the algorithm, we conduct a thorough experiment and the results demonstrated that our algorithm performs close to the ILP and is useful for large scale scenarios where ILP is intractable.

The rest of this paper is organized as follows. We have described the network and traffic models, related constraints and interference (e. g. SRS, XT crosstalk) in Section II. The proposed ILP and heuristic algorithm are presented in Sections III and IV, respectively. Section V is devoted to performance evaluation of the proposed methods. Finally, Section VI concludes the paper.

## II. SYSTEM MODEL AND QOT ESTIMATION

## *A. Network and Traffic Model*

Graph G (V, E) represents the network topology, where V = {v1, v2,...,vend} represents the set of nodes and E = {e1, e2,...,eend} represents the set of network links. Each link is composed by a MCF fiber, and at the beginning of each link, the C- and L-bands signals are multiplexed and transmitted on the MCF fiber, where C = {c1, c2,...,cend} is the set of cores of each fiber. The FSs are indexed from low wavelength, F<sup>C</sup> = {f<sup>c</sup>1, f<sup>c</sup>2,...,f<sup>c</sup>\_end} is the set of frequency slots (FSs) over C-band, F<sup>L</sup> = {f<sup>l</sup>1, f<sup>l</sup>2,...,f<sup>l</sup>\_end} is the set of frequency slots (FSs) over L-band. Each FS with bandwidth of Δ = 12.5GHz. The incoming traffic follows a static scenario in which all the demands are known and given in advance. Each demand (r) is denoted by r (sr, dr, br) , where s<sup>r</sup> is the source node, d<sup>r</sup> is the destination node and b<sup>r</sup> is the number of required frequency slots. The demand set is R = {r1, r2,...,rD} , where D is the number of the demands. For each demand, the number of required contiguous FSs are determined based on its crosstalk and SNR. Furthermore, g FSs are considered as guard band after the last assigned FS between demands (set g=1). We assume that signals are transferred all-optically without using any regenerator through the path, with rectangular power spectral density (PSD), where the launch power of each demand is denoted with P.

For each demand, k-shortest disjoint path pairs PP are calculated in advance, for each path pair  $pp(p_{work}, p_{protect}) \in PP$ , one path as primary path (also called working)  $p_{work}$  and the other one as a backup path  $p_{protect}$ . Then, resources are allocated to the demand based on resource assignment strategies. During resource assignment process, three constraints must be satisfied:

- 1) Spectrum Contiguity Constraint: the assigned FSs to each demand should be contiguous;
- Spectrum Continuity Constraint: the assigned contiguous FSs to each demand is the same on all links of the selected path;
- Core Continuity Constraint: the assigned core to each demand is the same on all links of the selected path;

## B. Crosstalk and QoT Estimation

The use of MCF and MB brings non-negligible interference and affects the link transmission efficiency.

For MCF, if the same spectrum of adjacent active cores is occupied, crosstalk will occur. The crosstalk *XT* can be calculated by Equation 1, 2 [38].

$$\tilde{h} = \frac{2k^2r}{\beta w_r} \tag{1}$$

$$XT = \frac{n - n \cdot exp\left[-(n+1) \cdot \tilde{h} \cdot L\right]}{1 + n \cdot exp\left[-(n+1) \cdot \tilde{h} \cdot L\right]}$$
(2)

Where  $\tilde{h}$  denotes the power coupling coefficient, and XT represents the mean crosstalk. In Equation 1, k, r,  $\beta$  and  $w_r$  are the coupling coefficient, bend radius, propagation constant and core pitch, respectively. In Equation 2, n is the number of adjacent cores and L is the path length.

If the crosstalk is too large, the transmission quality will be degraded, or worse, the transmission will be interrupted. Therefore, in the resource allocation process, it should be ensured that the end-to-end crosstalk of all the frequency slots allocated to a demand is less than its threshold  $\Omega$ . Like Equation 3, XT(f) means the crosstalk at frequency f:

$$\max_{f \in F} \left\{ XT\left(f\right) \right\} \le \Omega \tag{3}$$

For MB, after adding other spectrum bands (i.e., O-, E-, S-, and L-band), SRS cannot be ignored, in addition to the ASE noise and NLI induced by Kerr effect. In order to comprehensively consider the effects of noise and interference, we use SNR as the performance metric to estimate the QoT in this work. It should be noted that we consider the fiber as a whole, consider the impact of SRS on the entire fiber, and do not explore the impact of SRS on a single core.

The SNR is calculated as follows [27], [39]–[41]:

$$SNR = \frac{P}{P_{ASE}^d + P_{NLI}^d} \tag{4}$$

Where, P is the launch power,  $P_{ASE}^d$  corresponds to the ASE noise power, and  $P_{NLI}^d$  is the NLI coefficient of demand d.

We use the Equation 5 to calculate the total ASE noise power, which is given by [27], [39]–[41]:

$$P_{ASE}^{d} = \sum_{l \in P^{d}} 2n_{sp} h f_{d} B_{d} \left( e^{\alpha L_{l}} - 1 \right) \tag{5}$$

Where  $P^d$ ,  $f_d$  and  $B_d$ denote the selected path, center frequency and bandwidth of demand d, respectively,  $L_l$  is the length of link l,  $\alpha$  is the fiber attenuation coefficient, h is the Planck's constant,  $n_{sp}$  is the spontaneous emission factor that is assumed equal in C- and L-bands for simplicity.

Equation 8 is used to calculate NLI power of demand *d*. The self-channel interference (SCI) and the cross-channel interference (XCI) can be calculated by Equation 6 and Equation 7 [27], [39]–[41].

$$P_{NLI}^{d} = \sum_{l \in P^{d}} P_{SCI}^{d,l} + P_{XCI}^{d,l}$$
 (8)

Where  $\phi_d=\beta_2+2\pi\beta_3 f_d, \phi_{d,d'}=(\beta_2+\pi\beta_3[f_d+f_{d'}])\times (f_{d'}-f_d), \ \gamma$  is fiber nonlinear coefficient,  $C_r$  is the slope of the linear regression of normalized Raman gain spectrum,  $\beta_2$  is group velocity dispersion (GVD) parameter,  $\beta_3$  is its linear slope,  $D^l$  denotes the number of demands using link l, and  $D^lP$  is the total power at link l.

#### III. ILP FORMULATION

## A. ILP-BP

In this section, we present an ILP formulation of the band partition protection scheme with given static demand set and network status. The ILP model is the mathematical description of the band partition protection scheme and one-to-one dedicated protection scheme. The optimization problem is formulated to achieve optimal resource allocation and higher SNR. The proposed ILP model (ILP-BP) is defined as follows.

#### **Indices**

 $\begin{array}{ll} r \in R \text{:} & \text{Requests.} \\ c \in C \text{:} & \text{Fiber cores.} \\ l \in L \text{:} & \text{Network links.} \end{array}$ 

 $pp \in PP$ : Candidate pairs of link-disjoint paths for each

 $\begin{array}{ccc} & \text{request.} \\ p_{\in}pp: & \text{Primary path.} \\ \tilde{p} \in pp: & \text{Backup path.} \\ f \in F: & \text{Frequency slots.} \\ f_c \in F_c \in F: & \text{C-band slots.} \\ f_l \in F_L \in F: & \text{L-band slots.} \end{array}$ 

#### **Constants**

 $b_r$ : Number of required FSs for request r.

 $\Omega$ : Crosstalk XT threshold.

 $\Xi$ : SNR threshold.

Binary variable which is 1 if the primary (backup) path contains link l.

 $f_{end}$ : The highest frequency in C+L band.

The bandwidth of each FS.  $\Delta$ :

## **Variables**

 $\gamma_r^l(\bar{\gamma}_r^l)$ : Binary variable which is 1 if link l is used to accommodate request r on its primary (backup)

 $\theta_{p}^{r, l}(\bar{\theta}_{\tilde{p}}^{r, l})$ : Binary variable which is 1 if primary (backup) path of request r contains link l.

 $\delta_{p,\tilde{p}}$ : Binary variable which is 1 if p and p' have

common link(s).

Binary variable which is 1 if path p is used  $\tau_r^p(\bar{\tau}_r^{\tilde{p}})$ : to accommodate or reserved as backup for request r.

 $\psi_r^{l,c}(\bar{\psi}_r^{\bar{l},\bar{c}})$ : Binary variable which is 1 if core c on link l is used to accommodate or reserved as backup for request r.

 $x_{r,l,c}^f(\bar{x}_{r,l,c}^f)$ : Binary variable which equals 1 if frequency slot f on core c of link l is used to accommodate (reserved as backup) for request r.

 $f_r^0(\bar{f}_r^0)$ : Integer variable which denotes the index of

starting frequency slot of request r for primary

(backup) path.

 $w_{i,c}^{f}$ : Indicates the crosstalk on FS f of core c on link

 $\xi_r^p(\xi_r^{\tilde{p}})$ : Binary variable which is 1 if primary (backup) path p accommodates request r.

 $SNR^r$ : The SNR of request r.

 $f_{r,i}$ : The center frequency of request r, i is the index of the first selected FSs. It is obtained as  $f_{r,i}$ 

 $f_{end} - (i-1+\frac{b_r+g}{2})\Delta$ .

 $F_{max}$  ( $\bar{F}_{max}$ ): an integer variable which denotes the index of maximum allocated frequency slot for primary (backup) path among all the cores of all the network links.

Objective:

$$minimize F_{max} \left( \bar{F}_{max} \right)$$
 (9)

$$maximize SNR^r$$
 (10)

The proposed ILP formulation has two goals. One is to minimize the maximum index of allocated working FSs and backup FSs which aims to make FSs distribution denser and save more idle FSs for more requests. The other is to maximize the SNR of request r and minimize the impact of SRS.

Subject to:

Constraint for path selection:

$$\sum_{p \in PP} \tau_r^p = 1, \quad \forall r \tag{11}$$

$$\sum_{\tilde{p} \in PP} \bar{\tau}_r^{\tilde{p}} = 1, \quad \forall r \tag{12}$$

$$\sum_{\substack{n \ \tilde{p} \in np}} \theta_p^{r,l} + \bar{\theta}_{\tilde{p}}^{r,l} \le 1, \quad \forall r, l$$
 (13)

Equations 11 and 12 ensure that exactly one primary and one backup path are assigned to request r. Note that PP shows the set of disjoint pairs of paths for request r, Equation 13 guarantees that primary path and backup path are disjoint.

$$\sum_{p \in PP} \tau_r^p \times a_p^l = \gamma_r^l, \quad \forall r, l$$
 (14)

$$\sum_{\tilde{p} \in pp} \bar{\tau}_r^{\tilde{p}} \times a_{\tilde{p}}^l = \bar{\gamma}_r^l, \quad \forall r, l$$
 (15)

Equations 14 and 15 set the value of  $\gamma_r^l$  and  $\bar{\gamma}_r^l$ , which specify the links assigned to request r.

Constraint for core selection:

$$\sum_{c \in C} \psi_r^{l,c} = \gamma_r^l, \quad \forall r, l \tag{16}$$

$$\sum_{c \in C} \bar{\psi}_r^{\bar{l},\bar{c}} = \bar{\gamma}_r^l , \quad \forall r, l$$
 (17)

$$\psi_r^{l,c} = \frac{\sum_l \sum_{c \in C} \psi_r^{l,c}}{\sum_l \gamma_r^l}, \quad \forall r, l$$
 (18)

$$\bar{\psi}_r^{\bar{l},\bar{c}} = \frac{\sum_l \sum_{c \in C} \bar{\psi}_r^{\bar{l},\bar{c}}}{\sum_l \bar{\gamma}_r^l}, \quad \forall r, l$$
 (19)

Equations 16 and 17 assure that exactly one core on each link of the primary and backup paths is assigned to request r. Equations 18 and 19 guarantee that the selected core number on the primary (backup) path is the same for request r.

*Non-overlapping constraint:* 

$$\sum_{r} x_{r,l,c}^{f} \le 1, \quad \forall l, f, c; \tag{20}$$

Equation 20 defines that each FS on each core of each link can only be occupied by one request at a time.

$$\mathbf{P}_{SCI}^{d,l} = \frac{8}{81} \frac{\gamma^2 P^3}{\pi \alpha^2} \frac{1}{\phi_{r,i} B_d^2} \times \left[ \frac{\left(2\alpha - D^l P C_r f_d\right)^2 - \alpha^2}{\alpha} \times asinh\left(\frac{3\pi}{2\alpha} \phi_d B_d^2\right) + \frac{4\alpha^2 - \left(2\alpha - D^l P C_r f_d\right)^2}{2\alpha} \times asinh\left(\frac{3\pi}{4\alpha} \phi_d B_d^2\right) \right]$$

$$(6)$$

$$\mathbf{P}_{XCI}^{d,l} = \frac{16}{81} \frac{\gamma^{2} P^{3}}{\pi^{2} \alpha^{2}} \sum_{d'} \frac{1}{\phi_{d,d'} B_{d'}} \times \left[ \frac{\left(2\alpha - D^{l} P C_{r} f_{d'}\right)^{2} - \alpha^{2}}{\alpha} \times atan\left(\frac{2\pi^{2}}{\alpha} \phi_{d,d'} B_{d}\right) + \frac{4\alpha^{2} - \left(2\alpha - D^{l} P C_{r} f_{d'}\right)^{2}}{2\alpha} \times atan\left(\frac{\pi^{2}}{\alpha} \phi_{d,d'} B_{d}\right) \right]$$

$$(7)$$

Contiguity constraints:

$$\sum_{c} x_{r,l,c}^{f} - 1 \le f - f_r^{0}, \quad \forall r, l, f \in f_{c\_end}$$
 (21)

$$\sum_{c} x_{r,l,c}^{f} - 1 \le f_r^0 + b_r - 1 - f, \quad \forall r, l, f \in f_{c\_end} \quad (22)$$

$$\sum_{r} \bar{x}_{r,l,c}^{f} - 1 \le f - \bar{f}_{r}^{0}, \quad \forall r, l, f \in f_{l\_end}$$
 (23)

$$\sum_{c} \bar{x}_{r,l,c}^{f} - 1 \le \bar{f}_{r}^{0} + b_{r} - 1 - f, \quad \forall r, l, f \in f_{l\_end} \quad (24)$$

$$\sum_{f \in f_{c,end}} \sum_{c} x_{r,l,c}^{f} = b_r \times \theta_p^{r,l} \quad \forall r, l$$
 (25)

$$\sum_{f \in f_{l,end}} \sum_{c} \bar{x}_{r,l,c}^{f} = b_r \times \bar{\theta}_{\tilde{p}}^{r,l} \quad \forall r, l$$
 (26)

When FS f at core c of link l is allocated to request  $\mathbf{r}$  (  $x_{r,l,c}^f=1$ ), the left sides of Equations 21 and 22 equal zero, thus  $\mathbf{f}$  must be within  $[f_r^0, f_r^0 + b_r - 1]$ . Meanwhile, in order to make sure that all the FSs between  $f_r^0$  ( $\bar{f}_r^0$ ) and  $f_r^0 + b_r - 1$ ( $\bar{f}_r^0 + b_r - 1$ ) are occupied by request r for working resources or backup resources and only  $b_r$  FSs are assigned to request r in primary (backup) path, we use Equations 25 and 26 to restrain.

Spectrum Usage Constraints:

$$f_r^0 + b_r - 1 \le F_{max} , \quad \forall r \tag{27}$$

$$\bar{f}_r^0 + b_r - 1 < \bar{F}_{max} , \quad \forall r \tag{28}$$

The highest index of occupied FSs on primary and backup path are computed in Equations 27 and 28, which ensure that the allocated FSs does not exceed the optional FSs.

Constraints for band protection scheme:

$$\sum_{r} \sum_{c} \bar{f}_r^0 = 0, \quad \forall r$$
 (29)

$$\sum_{\tilde{n}} \sum_{r} f_r^0 = 0, \quad \forall r$$
 (30)

Equations 29 and 30 ensure that the working resources are over C-band and backup resources are over L- band for all requests.

Crosstalk constraints:

$$w_{l,c}^f < \Omega, \forall l, c, f \tag{31}$$

The crosstalk value is calculated via from Equations 1 and 2 and used in Equation 31 to make sure that all links meet the crosstalk limit, under the threshold.

ISRS parameters constraints:

$$SNR^r \ge \Xi, \quad \forall r$$
 (32)

The SNR value is calculated by Equations 4–8. Equation 32 keeps it from falling below the threshold to ensure that all requests are compliant and cannot disrupt the assigned requests.

#### B. ILP-MIX

To confirm the validity of the band partition protection scheme, we also apply the ILP formulation to the scenario without the band partition protection scheme, which we call ILP-MIX. Most of the parameter settings and constraints in ILP-MIX are the same as those in ILP-BP, except that there is no band partition protection scheme constraint in ILP-MIX, which allocate the FS form C-band to L-band based on first-fit.

#### IV. HEURISTIC ALGORITHM

## A. GA-S-RSCBA-BP

The ILP model can find the optimal solution of RSCBA problem in MB-SDM-EONs, but it is difficult to get the result in a real large-scale network within an acceptable time. Therefore, we propose an efficient heuristic algorithm based on genetic algorithm to find near optimal solution with a much lower run-time.

GA-S-RSCBA-BP is an efficient heuristic method based on a genetic algorithm (GA) framework that can solve the survivable RSCBA problem from a global perspective. Meanwhile, GA-S-RSCBA-BP adopts a band partition protection scheme within one-to-one protection for each demand, which can provide more stable protection for service requests by sacrificing part of the spectrum. In the future work, we can change the one-to-one protection method to a more efficient protection method, like the SBPP, multi-path protection method.

Initially, we get all demands  $r \in R$ , and sort all demands in descending order of their bandwidth  $b_r$ . In order to improve resource utilization, we give priority to allocate resources for demands that require more bandwidth. For each demand, we calculate K-shortest disjoint primary-protection path pairs. Let  $k_r \in [1,K]$  be the primary - protection path pair assigned to the demand r, and  $c_r \in C$  be the core number assigned to the demand r, then the feasible solution for each demand  $r \in R$ , called gene, can be defined as:

$$G_r = \left\{ k_r, c_r^{primary}, c_r^{protection} \right\}, r = 12, \dots D$$
 (33)

Where,  $c_r^{primary}$  and  $c_r^{protection}$  respectively represent the selected core of the primary path and the protection path. Conversely,  $f_r^{primary}$  and  $f_r^{protection}$  respectively represent the first selected FS of the primary path and the protection path, which are calculated by first-fit method based on  $k_r, c_r^{primary}$  and  $c_r^{protection}$  while considering crosstalk and SNR.

All genes of all demands are grouped into one chromosome  $ch_i$ . One chromosome can represent a candidate solution of the survivable RSCBA problem. The chromosome is given as:

$$ch_i = \{G_1, G_2, \dots, G_D\}, i = 12, \dots, S$$
 (34)

The population *POP* is composed of multiple chromosomes, we set the population size as *S*. Then, the *POP* can be defined

$$POP = \{ch_1, ch_2, \dots, ch_S\}$$
 (35)

In the survivable RSCBA problem, there are some factors that need to be taken into account:

- 1) Successful protection rate: Proportion of demands that find the protection path and protected resources, successfully, which is defined as  $S_p$ .
- 2) The maximum index of the allocated FS: In this paper we use the first-fit method to allocate low frequency FSs in C-band and L-band. The smaller the maximum FS index allocated, the more idle FSs are available for other demands, which means more efficient utilization.

Based on the above factors, the optimization objective of GA-S-RSCBA-BP is to minimize the maximum index of the allocated FS as well as improving their successful protection rate. In GA-S-RSCBA-BP, we use the fitness function to judge the quality of each chromosome (that is, the RSCBA solution). Therefore, the fitness function is defined as follows:

$$fitness = w \times S_p - (1 - w)$$

$$\times avg \left( \sum_{l \in P} avg \left( \sum_{c \in C} \left( \frac{f^{c-max}}{f_{c\_end}} + \frac{f^{l-max}}{f_{l\_end}} \right) \right) \right)$$
(36)

Where, w is the weight parameter,  $f^{c-max}$  and  $f^{l-max}$  are the largest indexes of FS that have been allocated on C-band and L-band, respectively.  $f_{c\_end}$  and  $f_{l\_end}$  are the last index of FS on C-band and L-band, respectively.

The fundamental procedures of GA are chromosome selection, crossover and mutation. The above steps are repeated until the iteration ends or the algorithm converges.

For GA-S-RSCBA-BP, in the selection process, elite selection is used, it retains M outstanding individuals to the new population. Then call the gambling wheel ratio selection algorithm to select the remaining individuals to enter the new population until the number of individuals in the new population reaches the population size. For the crossover operation, the 2-point crossover method is used [42]. It involves the random selection of two individuals from the new population, and generating a random number  $\varsigma_c$  with a uniform distribution of 0–1. If  $\varsigma_c \leq \rho_C$ ( $\rho_C$  is the crossover probability), the two individuals are crossed. Then, the two-point crossover algorithm is called, two crossover points are randomly selected, and the middle part of the two crossover points of the two parents are exchanged to generate two new offspring. In the mutation process, for each individual in the new population, a 0–1 uniformly distributed random number  $\varsigma_m$  is drawn, if  $\varsigma_m \leq \rho_M$  ( $\rho_M$  is the mutation probability), then the mutation operation is performed on this individual. Mutation consists in randomly selecting and changing part of the gene code. The newly generated individual is added to the new population, otherwise the original individual is added to the

In GA, the crossover probability  $\rho_C$  and mutation probability  $\rho_M$  are key factors that influence the behavior and performance of genetic algorithms, and directly influence the convergence of the algorithm. By introducing an adaptive strategy,  $\rho_C$  and  $\rho_M$  can automatically change with the fitness value. When the fitness value of each body of the population tends to be the

## Algorithm 1: GA-S-RSCBA-BP.

- 1: **Initialize** the network G(V, E) and the demand set R;
- 2: Sort all demands in R in descending order based on  $b_r$ ;
- 3: **Initialize** initial population *POP* with random gene coding;
- 4: While algorithm has not converged do:
- 5: For each chromosome  $ch_i \in POP$  do:
- 6: Decode each G<sub>r</sub> ∈ ch<sub>i</sub> to obtain the resource allocation scheme:

Compute fitness by considering SNR and XT constraint;

Select based on elite selection;

Crossover based on 2-point crossover method;

Mutation;

- 7: End while;
- 8: Get the best chromosome;
- 9: **Return** best fitness;

same or tends to the local optimum,  $\rho_C$  and  $\rho_M$  increase, and vice versa. Therefore, the adaptive genetic algorithm can ensure the convergence of the genetic algorithm while maintaining the diversity of the population.

 $\rho_C$  and  $\rho_M$  are adaptively adjusted according to Equation 37 and 38:

$$\rho_C = \begin{cases} k_1 & g' < g_a \\ \frac{k_2 \times (g_{best} - g')}{g_{best} - g_a} & g' \ge g_a \end{cases}$$

$$(37)$$

$$\rho_M = \begin{cases} k_3 & g < g_a \\ \frac{k_4 \times (g_{best} - g)}{g_{best} - g_a} & g \ge g_a \end{cases}$$
 (38)

Where,  $g_{best}$  is the maximum fitness value of the population; g' is the larger fitness value of the two individuals to be crossed; g is the fitness value of the individual to be mutated.  $\mathbf{k}_1,\mathbf{k}_2,\mathbf{k}_3$  and  $\mathbf{k}_4$  are all constants set between (0,1), and must satisfy  $\mathbf{k}_1<\mathbf{k}_2,\mathbf{k}_3<\mathbf{k}_4$ .

In the last generation, GA-S-RSCBA-BP selects the chromosome with the largest fitness value to be the survivable RSCBA solution. The process of GA-S-RSCBA-BP is summarized in Algorithm 1.

## B. Alternative Algorithms

This sub-section is used to introduce simple designed alternative heuristic algorithms and scenarios for comparison to verify the superiority of the proposed band partition protection scheme and GA-MB framework.

We use the Dijkstra algorithm to compare with the efficient heuristic method based on the genetic algorithm framework. In the comparison algorithm scheme, instead of ranking the requests by importance, we assign equal ranks to all requests

TABLE II SIMULATION ALGORITHMS AND SCENARIOS

| ALGORITHM AND SCENARIO                                             | Name          |
|--------------------------------------------------------------------|---------------|
| ILP MODEL BASED ON BAND PARTITION PROTECTION SCHEME                | ILP-BP        |
| ILP MODEL BASED ON MIXED<br>SCENARIO                               | ILP-MIX       |
| BAND PARTITION PROTECTION<br>SCHEME BASED ON GA<br>FRAMEWORK       | GA-S-RSCBA-BP |
| BAND PARTITION PROTECTION<br>SCHEME BASED ON DIJKSTRA<br>FRAMEWORK | D-C+L-BP      |
| SINGLE C-BAND BASED ON GA<br>FRAMEWORK                             | GA-C ONLY     |
| SINGLE C-BAND BASED ON<br>DIJKSTRA FRAMEWORK                       | D-C only      |
| C+L- BAND MIXED SCENARIO<br>BASED ON GA FRAMEWORK                  | GA-C+L-MIX    |

with the same number of demands. The Dijkstra algorithm is used to select the working path and the protection path of the current request (the calculation method of the protection path is the same as that of GA), and the core allocation method adopts the first-fit, which means that, the demand is allocated from the first core of each link. The selected core of the working path and protection path corresponds to  $c_r^{primary}$  and  $c_r^{protection}$  in the GA algorithm, respectively. The spectrum allocation scheme also uses the first-fit.

$$fitness = w \times PS - (1 - w) \times avg \left( \sum_{l \in P} \frac{\sum_{c \in C} f_{max}}{f_{end}} \right)$$
(39)

In order to prove that the combination of MB and SDM can effectively expand the fiber capacity, we will compare the MB-SDM scenario with the single C-band-SDM network scenario, where each link only uses the single C- band without L-band. In addition, we designed another scenario: C+L- band mixed, to prove the performance of the proposed band partition protection scheme. In this scenario, the protection resources and working resources are randomly allocated in the C- and L- bands without applying the band partition protection scheme in the process of resource allocation. Considering comparison parameters, we have the following alternative heuristic algorithms: C+L- band mixed scenario based on GA framework (GA-C+L-mix), single C-band based on GA framework (GA-C only), single C-band based on Dijkstra framework (D-C only) and band partition protection scheme based on Dijkstra framework (D- C+L-BP). For the GA-C+L-mix algorithm and the GA-C only algorithm, it should be noted that their fitness function is calculated as per Equation 39. All the compared algorithms and scenarios are summarized in Table II.

## V. SIMULATION RESULTS AND DISCUSSIONS

In this section, we evaluate and compare the performance of the ILP and the GA-based heuristic algorithm for survivable-

![](_page_7_Picture_9.jpeg)

Fig. 1. Network topologies: (a) 6-node topology. (b) NSFnet topology.

#### TABLE III PARAMETERS SETTING [26], [37]

| Parameters in SNR |                               |  |
|-------------------|-------------------------------|--|
| Parameter         | Value                         |  |
| $f_{end}$         | 196.04 <i>THz</i>             |  |
| α                 | 0.2  dB/km                    |  |
| $\beta_2$         | $-21.6 \ ps^2/km$             |  |
| $\beta_3$         | $0.14 \text{ ps}^3/\text{km}$ |  |
| P                 | $1.0 \times 10^{-3} \text{W}$ |  |
| Ξ                 | 9dB                           |  |
| $n_{sp}$          | 1.5                           |  |
| γ                 | 1.2 1/W/km                    |  |
| $C_r$             | 0.028 1/W/km/THz              |  |

| Parameters in Crosstalk |                          |  |
|-------------------------|--------------------------|--|
| Parameter               | Value                    |  |
| $\epsilon$              | $3.4 \times 10^{-4}$     |  |
| r                       | $5 \times 10^{-2} \ m$   |  |
| β                       | $4.5 \times 10^{-5} \ m$ |  |
| $w_r$                   | $4 \times 10^6 \ ^1/_m$  |  |
| Ω                       | -30dB                    |  |
|                         |                          |  |
| Parameters in GA        |                          |  |

| Parameters in GA |       |  |  |
|------------------|-------|--|--|
| Parameter        | Value |  |  |
| w                | 0.5   |  |  |
| $k_1, k_3$       | 0.1   |  |  |
| $k_2, k_4$       | 0.001 |  |  |

RSCBA problem based on the proposed band partition protection scheme in a static network environment. First, we run the simulations in a small-scale network model by employing the proposed ILP and heuristic algorithm. The results show that the proposed heuristic algorithm performs close to the proposed ILP. Then, as for in large-scale networks, for the reason that ILP formulations are computationally complex and intractable in real large-scale networks, we evaluate only the heuristic algorithm. In order to show that the proposed band partition protection scheme enhances the performance, we compare the proposed heuristic algorithm (GA-S-RSCBA-BP) with the designed alternative heuristic algorithms described in Section IV (GA-C+L-mix, GA-C only, D-C only and D-C+L-BP).

We use the 6-node topology in Fig. 1(a) as a small-scale model and the NSFnet topology with 14 nodes and 21 links in Fig. 1(b) as a large-scale model. We assume that each link has 12 cores for the large scale model and 3 cores for the small scale model. In real transmission scenarios, there is a gap between C- and L band-, which caused C- and L- band to have similar FS numbers. Based on the survey in [28], we set C- band and L- band with 446 FSs each, and 916 FSs on each core. Each FS's bandwidth  $\Delta$  is 12.5 GHz. The modulation format is BPSK. The source and destination nodes of each traffic request are selected randomly with uniform distribution and the number of candidate disjoint pairs of paths (k) for each traffic request is set to 5. The other parameters involved in the simulations can be found in Table III. We employed the academic Gurobi optimizer software package (version 9.1.2) to solve the ILP model and MATLAB (2017) version) to run the alternative heuristic algorithms based on

![](_page_8_Figure_2.jpeg)

Fig. 2. Free space of two scenarios: (a) C+L-MIX; (b) C+L-BP (band-partitioning).

![](_page_8_Figure_4.jpeg)

Fig. 3. The highest index of occupied FSs in the network in the ILP formulation and GA-S-RSCBA-BP.

Dijkstra algorithm. All simulations were run on a 64-bit machine with 3.2 -GHz CPU and 16-GB RAM. All the results reported in the numerical assessment are average results obtained over 20 simulations. The resulted values are reported in the following figures with a confidence interval of 95%.

## A. Comparison of ILP and Heuristic Algorithm

In this sub-section, the performance of ILP model is compared to that of GA-S-RSCBA-BP. Meanwhile, we compare two ILP models to demonstrate the superiority of band-partitioning. We set the *D* of the ILP model to 250, 300 and 350. For each demand, random required FSs are considered from 3 to 10.

Fig. 3 shows the relationship between the maximum index of the allocated FSs and the size of task demands under two scenarios with band-partitioning scheme: ILP-BP and GA-S-RSCBA-BP. The ILP model ILP-BP achieves the minimal FS index assignment. This is because ILP can find the optimal solution for the objective function that minimizes the working resources and protection resources of all demands. The assigned FS index of GA-S-RSCBA-BP is close to the optimal result of ILP, within 8% of the maximum difference with ILP, which means GA-S-RSCBA-BP has superior performance in resource allocation.

Fig. 4 shows the optimal solution of ILP-BP allocates all the primary lightpaths in C-band. This is because ILP-BP implements the band-partitioning constraint, but ILP-MIX does not.

![](_page_8_Figure_11.jpeg)

Fig. 4. The highest index of occupied FSs of primary path in the two ILP scenarios: ILP-MIX and ILP-BP.

![](_page_8_Figure_13.jpeg)

Fig. 5. The SNR Ratio by comparing GA-S-RSCBA-BP and GA-C+L-mix.

## B. Performance of Heuristic Algorithms

In this sub-section, GA-S-RSCBA-BP is compared to other designed alternative heuristic algorithms. For the C+L band scenario, we set the size of demands D from 50 to 750; conversely, we set the size of demands D from 50 to 450 in the single C band scenario. For each demand, random required FSs are considered from 3 to 10.

To prove the performance of the proposed band partition protection scheme, we compare the GA-S-RSCBA-BP and GA-C+L-mix, and use the SNR ratio as the evaluation metric. The SNR ratio is the ratio of the average SNR of GA-S-RSCBA-BP to the average SNR of GA-C+L-mix, which can be calculated as per eq. 40.

$$SNR\ RATIO\ = \frac{\text{average SNR of GA} - \text{S} - \text{RSCBA} - \text{BP}}{\text{average SNR of GA} - \text{C} + \text{L} - \text{mix}} \tag{40}$$

Fig. 5 shows the result of simulations that compare GA-S-RSCBA-BP to GA-C+L-mix. It can be seen from Fig. 3 that the SNR ratio gradually increases as the number of requests increases, which means GA-S-RSCBA-BP has higher SNR. When the size of request set is very small, the C-band is sufficient

![](_page_9_Figure_2.jpeg)

Fig. 6. The highest index of occupied FSs of primary path in the two GA-based scenarios: GA-C+L-MIX and GA-S-RSCBA-BP.

![](_page_9_Figure_4.jpeg)

Fig. 7. The highest index of occupied FSs in the network in the heuristic algorithms.

to undertake all the working resources and protection resources, and the L-band is not used in the GA-C+L-mix. Therefore, in the scenario of a small request set, the GA-C+L-mix and GA-S-RSCBA-BP have similar performance. However, as the size of the request set increases, the C-band of the GA-C+L-mix is insufficient to support all the request. In this way, resources will be gradually occupied on the L-band, which will cause interference to the C-band. In the GA-S-RSCBA-BP, the L-band will not be activated until there is a link failure. There is no interference on the C-band from L-band. Therefore, in the scenario of a large request set, the GA-S-RSCBA-BP will have a higher SNR and its performance will be better, which indicates that our proposed band partition protection scheme performs better.

Fig. 6 demonstrates that GA-S-RSCBA-BP achieves working-protection resource separation constraint, and GA-C+L-mix can not be able to converge to the band-partitioning solution, if bands are assigned randomly. In GA-S-RSCBA-BP, the allocated FSs for primary paths are only on C-band, but the allocated FSs for primary paths can be on L-band in GA-C+L-MIX.

![](_page_9_Figure_8.jpeg)

Fig. 8. The protection ratio in the network in the heuristic algorithms.

![](_page_9_Figure_10.jpeg)

Fig. 9. The fitness value in the network in the heuristic algorithms based on GA framework.

Figs. 7–9 are used to compare the performance of the GAbased heuristic algorithm to that of the Dijkstra-based heuristic algorithm. Also, we can see the results of C+L scenario compared with the C only scenario from the figures. In these simulations, the maximum assigned FSs index in C- and Lband and protection rate are the key optimization and evaluation indicators for this work. The maximum allocated FSs can implicitly represent the resource utilization, which is an important factor worth considering in the resource allocation problem. The protection rate represents the ratio of requests looking for protected resources to all requests. Survivability is the focus of this paper, and the protection rate reflects the impact of the proposed algorithms on network survivability. As a representative, we only compare the simulation results of GA-S-RSCBA-BP, GA-C only, D-C only and D- C+L-BP.

Fig. 7 shows the simulation results of the four algorithms in terms of the maximum allocation FS index. Compared to the algorithms based on the Dijkstra algorithm, the algorithms based on the GA framework have lower assigned FS indexes. This situation arises from two reasons. On the one hand, we give priority to service demands that require more FSs in the GA-based algorithm; on the other hand, the GA-based algorithm is a global optimization algorithm that traverses and searches for as many individuals as possible, and evaluates the strengths and weaknesses of individuals based on the fitness value. After multiple rounds of iterations, it chooses the optimal solution according to the fitness value. We noticed that as the number of requests increases, the assigned FS index gradually increases. This is because in the process of spectrum allocation, we allocate FSs from left to right no matter it is C-band or L-band. Since the allocation, start from low frequencies, when the low-frequency FSs are occupied by the demands, the index of the FSs available for allocation will gradually become larger.

The simulation results of protection ratio are shown in Fig. 8. Because of the superiority of the GA framework compared to the Dijkstra algorithm, the GA-based algorithms perform relatively better than the algorithms based on the Dijkstra algorithm. In the all scenarios, D-C only and GA-C only have the worst performance. This is because that D-C only and GA-C only have single C- band without L-band in the core. As a result, they have less resource for demands than the C+L band scenario. Meanwhile, GA-S-RSCBA-BP and D-C+L-BP have the highest protection rate in comparison to the other heuristic algorithms. What GA-S-RSCBA-BP and D- C+L-BP have in common is that they both use the proposed band partition protection scheme. In the proposed band partition protection scheme, the working resources and the protection resources are separated and placed in the C-band and L-band respectively. This method can reduce the SRS caused by the influence of high frequency on low frequency, thereby improving the SNR of links, which makes more FS on the link available for selection and allocation. From Fig. 8, we can see that as the number of demands increases, the protection rates of the four algorithms are gradually decreasing. This phenomenon is normal. As the number of demands increases, the link is affected by inter-channel SRS and inter-core crosstalk, and the resources available on the link are limited and gradually decreasing. When a new demand arrives, the number of available FSs for selection may be not enough. This causes protection resources reserved to fail, and consequently, the corresponding protection rate decreases.

Fig. 9 shows the relationship between fitness value and demand size for the GA-based algorithms. The GA-based algorithms judge the pros and cons of the solution according to the s fitness value. GA-S-RSCBA-BP has the highest fitness value, indicating that GA-S-RSCBA-BP has the best performance, which benefits from the use of the proposed band partition protection scheme. Since only single C- band is used in GA-C only, it has the lowest protection rate.

To further confirm the superiority of band-partitioning, we compared the size of the free space of MIX and BP in the GAbased and ILP scenarios, respectively. The experimental results are shown in Figs. 10 and 11.

The superiority of the band-partitioning strategy is that sacrifices a small part of FSs to improve the network SNR while achieving the compactness in the distribution of allocated resources.Whether it is band-partitioning strategy or mix scenario, the allocation of FS is from low frequency to high frequency, so the free space is mainly concentrated at the end of the frequency band. Fig. 2 shows the free space of two scenarios: C+L-MIX and C+L-BP (band-partitioning). In C+L-BP, there

![](_page_10_Figure_7.jpeg)

Fig. 10. Free space of two ILP scenarios: (a) C+L-MIX; (b) C+L-BP (bandpartitioning).

![](_page_10_Figure_9.jpeg)

Fig. 11. Free space of two GA-based scenarios: (a) C+L-MIX; (b) C+L-BP (band-partitioning).

are two free spaces. Because, we set up a working-protection resource separation constraint in the band-partitioning strategy, which leads to a free space at the end of the C-band in the band-partitioning strategy. If the free space is too small, it can be called fragmentation. However, the mix scenario has no such constraint, so it has only one free space at the end of L-band. Fig. 5 demonstrates the superiority of band-partitioning strategy in terms of SNR. Figs. 10 and 11 demonstrate the tightness of the allocated FSs in the band-partitioning strategy, the size of the free space of band-partitioning strategy is very close to that of mix scenario. The reason that the free space of band-partitioning strategy is slightly smaller than that of mix scenario is due to the fragmentation at the end of the C-band caused by workprotection resource separation constraint.

Because the GA-based algorithm makes decisions based on the fitness value, the decision result of the GA-based algorithm will be affected when the fitness value calculation function is modified. The fitness function in this article is designed by considering two efficiency indicators: resource utilization and protection rate. The weight*w*is used to set the proportion of resource utilization and protection ratio in a single simulation. With different weights, the focus of algorithmic decision-making will be different. Figs. 12, 13 and 14 show the impact of the weight

![](_page_11_Figure_2.jpeg)

Fig. 12. The fitness value in the network with the weight change.

![](_page_11_Figure_4.jpeg)

Fig. 13. The protection rate in the network with the weight change.

![](_page_11_Figure_6.jpeg)

Fig. 14. The highest index of occupied FSs in the network with the weight change.

*w* change on the fitness value, maximum assigned FS index and protection rate. As the number of requests increases, the Fmax and protection rate of the overall network will deteriorate due to limited resources, which will lead to a decrease in fitness and show a downward trend as shown in Fig. 12. According to Equations 36 and 39, the weight of the protection rate is *w* and the weight of maximum allocated FSs index (or resource utilization) is *1-w*. As the value of *w* increases, the influence of the protection rate on decision-making will gradually increase. Otherwise, it will gradually decrease. As shown in Fig. 13, in the case of the same number of requests, the higher the weight *w*, the higher the corresponding protection rate. Meanwhile, in the case of the same number of requests, the higher the weight *w*, the lower the corresponding protection maximum allocated FS index as shown in Fig. 14.

# VI. CONCLUSION

In this paper, we studied the survivability-RSCBA problem in the C+L band SDM-EONs. In our system, besides inter-core crosstalk, we also proposed a band partition protection scheme which considers the characteristics of multi bands, the idea of cold backup strategy and the impact of SRS. Based on the proposed band partition protection scheme, we formulated an ILP model to find out the best solution to the survivability-RSCBA problem. In the proposed ILP, in addition to the band partition protection, SNR and inter-core crosstalk are strictly modelled. Since the proposed ILP cannot solve large-scale network problems in polynomial time, we propose an effective heuristic algorithm based on genetic algorithm that implements the proposed band partition protection, called GA-S-RSCBA-BP. In GA-S-RSCBA-BP, all given requirements are sorted in a queue and services are provided in order. Moreover, we designed several alternative algorithms based on simple strategies and different band environments for comparison. The results indicated that the performance of GA-S-RSCBA-BP is very close to that of the ILP formulation. In addition, GA-S-RSCBA-BP and alternative algorithms are evaluated and compared in large scale scenarios. The results indicated that GA-S-RSCBA-BP shows better performance than the alternative algorithms, the proposed band partition protection effectively increases the SNR of the network and good compactness of allocated FSs. We also see that, the combined use of MB and SDM can greatly increase the network capacity to serve more demands than the single C-band scenario. Referring to [10], [21], it is clear that L-band has better SNR than C-band at full load. Based on this, we will consider scenario where work resources are placed in the L-band in the future. Meanwhile, since the SRS is not the focus of this paper, we do not discuss whether SRS also occurs among cores. This can be explored in the future work.

# REFERENCES

- [1] K. Kim *et al.*, "High speed and low latency passive optical network for 5G wireless systems," *J. Lightw. Technol.*, vol. 37, no. 12, pp. 2873–2882, Jun. 15, 2019.
- [2] A. Singh *et al.*, "Jupiter rising: A decade of CLOS topologies and centralized control in Google's datacenter network," *ACM SIGCOMM Comput. Commun. Rev.*, vol. 45, pp. 183–197, Aug. 2015.
- [3] Cisco, "Cisco visual networking index: Forecast and methodology, 2017- 2022," Jul. 2019.
- [4] A. D. Ellis, N. M. Suibhne, D. Saad, and D. N. Payne, "Communication networks beyond the capacity crunch," *Philos. Trans. Roy. Soc. A: Math., Phys. Eng. Sci.*, vol. 374, 2016, Art. no. 2062.
- [5] N. Sambo *et al.*, "Provisioning in multi-band optical networks: A C+L+Sband use case," in *Proc. 45th Eur. Conf. Opt. Commun.*, 2019, pp. 1–4.

- [6] V. Lopez *et al.*, "Optimized design and challenges for C&L band optical line systems," *J. Lightw. Technol.*, vol. 38, no. 5, pp. 1080–1091,Mar. 2020.
- [7] A. Ferrari *et al.*, "Assessment on the achievable throughput of Multi-band ITU-T G.652.D fiber transmission systems," *J. Lightw. Technol.*, vol. 38, no. 16, pp. 4279–4291, Aug. 2020.
- [8] A. Ferrari, E. Virgillito, and V. Curri, "Band-division vs. Space-division multiplexing: A network performance statistical assessment," *J. Lightw. Technol.*, vol. 38, no. 5, pp. 1041–1049, Mar. 2020.
- [9] M. Mehrabi, H. Beyranvand, and M. J. Emadi, "Multi-band elastic optical networks: Inter-channel stimulated raman scattering-aware routing, modulation level and spectrum assignment," *J. Lightw. Technol.*, vol. 39, no. 11, pp. 3360–3370, Jun. 2021.
- [10] B. A. Correia, R. S. Yamchi, E. Virgillito, A. Napoli, and V. Curri, "Power control strategies and network performance assessment for C+L+S multiband optical transport," *J. Opt. Commun. Netw.*, vol. 13, no. 7, pp. 147–157, Jul. 2021.
- [11] M. Mehrabi, H. Beyranvand, and M. J. Emadi, "Multi-band elastic optical networks: Inter-channel stimulated Raman scattering-aware routing, modulation level and spectrum assignment," *J. Lightw. Technol.*, vol. 39, no. 11, pp. 3360–3370, Jun. 2021.
- [12] M. Ghobadi and R. Mahajan, "Optical layer failures in a large backbone," in *Proc. Internet Meas. Conf.*, 2016, pp. 461–467.
- [13] M. Zhu, F. He, and E./ Oki, "Optimal primary and backup resource allocation with workload-dependent failure probability," in *Proc. Int. Conf. Inf. Commun. Technol. Convergence*, 2020, pp. 606–611.
- [14] A. Napoli *et al.*, "Perspectives of multi-band optical communication systems," in *Proc. Opto-Electron. Commun. Conf.*, Jul. 2018, pp. 1–2.
- [15] A. Napoli *et al.*, "Towards multiband optical systems," in *Proc. Adv. Photon. 2018 (BGPP, IPR, NP, NOMA, Sensors, Netw., SPPCom, SOF)*, WA, DC, 2018, Art. no. NeTu3E.1.
- [16] S. Okamoto, K. Horikoshi, F. Hamaoka, K. Minoguchi, and A. Hirano, "5-band (O, e, s, c, and L) WDM transmission with wavelength adaptive modulation format allocation," in *Proc. Eur. Conf. Opt. Commun.*, 2016, pp. 20–22.
- [17] F. Hamaoka *et al.*, "150.3-Tb/s ultra-wideband (s, c, and l bands) singlemode fibre transmission over 40-km using *>*519Gb/s/A PDM-128QAM signals," in *Proc. Eur. Conf. Opt. Commun.*, 2018.
- [18] J. Renaudier and A. Ghazisaeidi, "Scaling capacity growth of fiberoptic transmission systems using 100+ nm ultra-wideband semiconductor optical amplifiers," *J. Lightw. Technol.*, vol. 37, no. 8, pp. 1831–1838, Apr. 2019.
- [19] A. Ferrari *et al.*, "Upgrade capacity scenarios enabled by multi-band optical systems," in *Proc. 21st Int. Conf. Transp. Opt. Netw.*, 2019, pp. 1–4.
- [20] H. Yang, K. R. H. Bottrill, N. Taengnoi, N. K. Thipparapu, and P. Petropoulos, "Experimental demonstration of dual O+C-Band WDM transmission over 50-km SSMF with direct detection," *J. Lightw. Technol.*, vol. 38, no. 8, pp. 2278–2284, Apr. 2020.
- [21] M. Cantono, R. Schmogrow, M. Newland, V. Vusirikala, and T. Hofmeister, "Opportunities and challenges of C+L transmission systems," *J. Lightw. Technol.*, vol. 38, no. 5, pp. 1050–1060, Mar. 2020.
- [22] E. Virgillito, R. Sadeghi, A. Ferrari, A. Napoli, and V. Curri, "Network performance assessment with uniform and non-uniform nodes distribution in C+L upgrades vs. Fiber doubling SDM solutions," in *Proc. Int. Conf. Opt. Netw. Des. Model.*, 2020, pp. 1–6.
- [23] D. Semrau, R. I.Killey, and P. Bayvel, "A closed-form approximation of the gaussian noise model in the presence of inter-channel stimulated raman scattering," *J. Lightw. Technol.*, vol. 37, no. 9, pp. 1924–1936, May 2019.
- [24] M. Filer, M. Cantono, A. Ferrari, G. Grammel, G. Galimberti, and V. Curri, "Multi-vendor experimental validation of an open source QOT estimator for optical networks," *J. Lightw. Technol.*, vol. 36, no. 15, pp. 3073–3082, Aug. 2018.
- [25] A. Ferrari, D. Pilori, E. Virgillito, and V. Curri, "Power control strategies in C+L optical line systems," in *Proc. Opt. Fiber Commun. Conf. Exhibit.*, 2019, Art. no. W2A.48.
- [26] F. Hamaoka *et al.*, "Ultra-wideband WDM transmission in S-, C-, and L-bands using signal power optimization scheme," *J. Lightw. Technol.*, vol. 37, no. 8, pp. 1764–1771, Apr. 2019.
- [27] M. Mehrabi, H. Beyranvand, and M. J. Emadi, "Multi-band elastic optical networks: Inter-channel stimulated Raman Scattering-aware routing, modulation level and spectrum assignment," *J. Lightw. Technol.*, vol. 39, no. 11, pp. 3360–3370, Jun. 2021.
- [28] P. Morales *et al.*, "Multi-band environments for optical reinforcement learning gym for resource allocation in elastic optical network," in *Proc. Int. Conf. Opt. Netw. Des. Model.*, 2021, pp. 1–6.

- [29] N. El Din El Sheikh, E. Paz, J. Pinto, and A. Beghelli, "Multi-band provisioning in dynamic elastic optical networks: A comparative study of a heuristic and a deep reinforcement learning approach," in *Proc. Int. Conf. Opt. Netw. Des. Model.*, 2021, pp. 1–3.
- [30] B. J. Puttnam *et al.*, "0.596 Pb/s s, c, L-band transmission in a 125µm diameter 4-core fiber using a single wideband comb source," in *Proc. Opt. Fiber Commun. Conf.*, 2020, pp. 1–3.
- [31] G. Rademacher *et al.*, "172 Tb/s C+L band transmission over 2040 km strongly coupled 3-Core fiber," in *Proc. Opt. Fiber Commun. Conf. Postdeadline Papers*, 2020, pp. 1–3.
- [32] G. Rademacher *et al.*, "High capacity transmission in a coupled-core threecore multi-core fiber," *J. Lightw. Technol.*, vol. 39, no. 3, pp. 757–762, Feb. 2021.
- [33] B. J. Puttnam *et al.*, "0.61 Pb/s s, c, and L-band transmission in a 125µm diameter 4-Core fiber using a single wideband comb source," *J. Lightw. Technol.*, vol. 39, no. 4, pp. 1027–1032, Feb. 2021.
- [34] G. Rademacher, B. Puttnam, R. S. Luis, J. Sakaguchi, and N. Wada, "Highly spectral efficient c + L-band transmission over a 38-core-3-mode fiber," *J. Lightw. Technol.*, vol. 39, no. 4, pp. 1048–1055, Feb. 2021.
- [35] R. Zhu *et al.*, "Survival multipath energy-aware resource allocation in SDM-EONs during fluctuating traffic," *J. Lightw. Technol.*, vol. 39, no. 7, pp. 1900–1912, Apr. 2021.
- [36] H. M. N. S. Oliveira and N. L. S. da Fonseca, "The minimum interference P-cycle algorithm for protection of space division multiplexing elastic optical networks," *IEEE Latin Amer. Trans.*, vol. 15, no. 7, pp. 1342–1348, 2017.
- [37] E. E. Moghaddam, H. Beyranvand, and J. A. Salehi, "Crosstalk-aware resource allocation in survivable space-division-multiplexed elastic optical networks supporting hybrid dedicated and shared path protection," *J. Lightw. Technol.*, vol. 38, no. 6, pp. 1095–1102, Mar. 2020.
- [38] Q. Yao, H. Yang, H. Xiao, Y. Zhao, R. Zhu, and J. Zhang, "Crosstalkaware routing, spectrum, and core assignment in space-division multiplexing optical networks with multicore fibers," *Opt. Eng.*, vol. 56, 2017, Art. no. 066104.
- [39] A. Mitra, D. Semrau, N. Gahlawat, A. Srivastava, P. Bayvel, and A. Lord, "Effect of channel launch power on fill margin in C+ L band elastic optical networks," *J. Lightw. Technol.*, vol. 38, no. 5, pp. 1032–1040, Mar. 2019.
- [40] A. Ferrari *et al.*, "GNPy: An open source application for physical layer aware open optical networks," *J. Opt. Commun. Netw.*, vol. 12, no. 6, pp. C31–C40, Jun. 2020.
- [41] M. Mehrabi, H. Beyranvand, and M. J. Emadi, "Multi-Band elastic optical networks: Inter-channel stimulated Raman scattering-aware routing, modulation level and spectrum assignment," *J. Lightw. Technol.*, vol. 39, no. 11, pp. 3360–3370, Jun. 2021.
- [42] D. Whitley, "A genetic algorithm tutorial," *Statist. Comput.*, vol. 4, no. 2, pp. 65–85, Jun. 1994.

**Zhihuan Luo** is currently working toward the master's degree with the Beijing University of Posts and Telecommunications, Beijing, China. Her research interests include SDM-EON, multi band, and survivability of optical network.

**Shan Yin** received the B.S. and Ph.D. degrees in communication engineering from the Beijing University of Posts and Telecommunications (BUPT), Beijing, China, in 2009 and 2014, respectively. She is currently an Associate Professor with the State Key Laboratory of Information Photonics and Optical Communications, BUPT. Her research interests include intelligent resource optimization and survivalbility in optical networks. Her current research interests include the use of machine learning and optimization methodogloy.

**Ligang Zhao** is currently working toward the master's degree with the Beijing University of Post and Telecommunications, Beijing, China. He is also a Software Engineer. His research interests include machine learning, optical network, and resource assignment.

**ZhenhaoWang** is currently working toward the master's degree with the Beijing University of Posts and Telecommunications, Beijing, China. His research interests include node architecture, margin, and multiband optical networks.

**Wenchao Zhang** received the bachelor's degree in engineering in 2021 from the Beijing University of Posts and Telecommunications, Beijing, China, where he is currently working toward the master's degree. His research interests include node architecture and multiband optical networks.

**Liyou Jiang** is currently working toward the master's degree with the Beijing University of Posts and Telecommunications, Beijing, China. His research interests include survivability of optical networks, optical network virtualization, and network slicing.

**Shanguo Huang** (Member, IEEE) received the Ph.D. degree from the Beijing University of Posts and Telecommunications (BUPT), Beijing, China, in 2006. He is currently a Professor with the State Key Laboratory of Information Photonics and Optical Communications, and the Deputy Dean with the School of Science, BUPT. He has been actively undertaking several national projects, has authored or coauthored three books and more than journal articles and refereed conferences, and authorized 18 patents. His research interests include microwave photonic system, network designing, planning, multiaccess edge computing, and resource allocations. He was the recipient of the Beijing Higher Education Young Elite Teacher, Beijing Nova Program, Program for New Century Excellent Talents in University from 11 the Ministry of Education in 2011 and 2013, National Science Fund for Excellent Young Scholars in 2016 and awarded the National Outstanding Youth Science Fund in 2021. He was a ACP2020 conference, WorkshopTPC Chairman, CECnet2021 conference Chairman, and the branch Chairman or Co-Chairman of many well-known international academic conferences, and invited more than ten international conference reports.
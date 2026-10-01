---
title: "Deep recurrent neural network for optical fronthaul dimensioning and proactive vBBU placement in CF‑RAN"
tema_principal: fl_ran
temas_relacionados: []
ano: 2021
autores: []
veiculo: null
pdf: ../pdf/deep_recurrent_neural_network_for_optical_fronthaul_dimensioning_and_proactive_vbbu_placement_in_cf-ran.pdf
---

#### **ORIGINAL PAPER**

![](_page_0_Picture_2.jpeg)

# **Deep recurrent neural network for optical fronthaul dimensioning and proactive vBBU placement in CF‑RAN**

**Matias R. P. dos Santos<sup>1</sup>  [·](http://orcid.org/0000-0002-8356-157X) Rodrigo I. Tinini2 · Tiago O. Januario1,2 · Gustavo B. Figueiredo1,2**

Received: 14 August 2021 / Accepted: 9 November 2021 / Published online: 9 February 2022 © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2022

#### **Abstract**

In this paper, we solve virtualized passive optical network (VPON) assignment and virtualized baseband unit (vBBU) placement using an integer linear programming formulation, an approximated heuristic using linear relaxation, and a proactive heuristic based on a specifc kind of recurrent neural network. We also studied the application of multi-step forecasting in Cloud-Fog Radio Access Network (CF-RAN) trafc demands for joint use with integer linear programming once it allows the solver more time to generate solutions. Also, we examine if the error in batch prediction impacts the fnal solution in terms of blocking and correctness.

**Keywords** CF-RAN · Integer linear programming · Network functions virtualization

# **1 Introduction**

The Cloud Radio Access Network (CRAN) is a Radio Access Network (RAN) architecture envisioned to be adopted in 5G networks to reduce Capital Expenditure (CapEx) and Operational Expenditure (OpEx). In this architecture, a Baseband Unit(BBU) pool, located in a cloud facility, performs centralized baseband processing, whereas low-power Remote Radio Heads (RRHs) located at cell sites perform user equipment (UE) association and reception functions. Those elements are then connected by an optical

The research has been partially developed at UFBA and was funded by the Fundação de Amparo à Pesquisa do Estado da Bahia (FAPESB) and by CNPq 313057/2020-6. Research Funds for the Federal University of Bahia.

\* Matias R. P. dos Santos matiasrps@ufba.br

> Rodrigo I. Tinini tinini@fei.edu.br

Tiago O. Januario januario@dcc.ufba.br

Gustavo B. Figueiredo gustavobf@dcc.ufba.br

- <sup>1</sup> Universidade Federal da Bahia, Ondina, Salvador, BA, Brazil
- <sup>2</sup> Centro Universitário FEI, SBernardo do Campo, SP, Brazil

access transport interface called fronthaul. The CRANs have a great potential to reduce power consumption. However, this centralized approach may lead to heavy workload burdens in the fronthaul and in the cloud, which impacts the network performance in terms of coverage, capacity, and latency [\[1](#page-12-0)].

For instance, the Common Public Radio Interface (CPRI) protocol provides line rates that range from 614.4 Mbps to 24.3 Gbps for each RRH, which poses a challenge to the design of the fronthaul and requires the use of optical networks in the fronthaul. Active optical networks, such as Dense Wavelength Division Multiplexing (DWDM), can provide transmission rates up to 400Gbps per wavelength. Therefore, the trafc from several RRHs could be groomed into a single DWDM channel. However, the deployment of such networks is cost-prohibitive, especially in high-granularity scenarios. Alternatively, the Time-and-Wavelength Division Multiplexing Passive Optical Network (TWDM-PON) may be equipped with one to eighth optical channels whose nominal line rate classes have values such as 1.25 *Gbit*/*s*, 2.5 *Gbit*/*s* and 10 *Gbit*/*s*, depending on the standard. Hence, they can provide high bandwidth in a low cost and latency operation, although it has lower transmission capacity than active networks. In this work, we assume that a TWDM-PON implements the optical fronthaul [[2\]](#page-12-1).

To address CRAN's limitations, a hybrid architecture called Cloud-Fog RAN (CF-RAN) has been recently proposed [[3\]](#page-12-2). CF-RAN increases network capacity by deploying

![](_page_0_Picture_21.jpeg)

fog nodes closer to cell sites to ofoad the network workload when the fronthaul links connecting to the cloud facility get overloaded. However, as fog node activation increases network capacity, it proportionally increments power consumption. Hence, the CF-RAN operation establishes a clear trade-of between energy consumption and network capacity. Another essential aspect that RANs, in general, must consider is the high fuctuation of mobile network trafc. Such a pattern is due to the number of activated resources that must closely follow the network demand to avoid resource wastage when more elements than necessary are activated. Hence, strategies that optimally decide on activation of fog nodes and placing vBBUs are of paramount importance.

Many promising solutions to solve placement problems use integer linear programming (ILP) formulations for static and dynamic trafc scenarios. Those formulations have been adopted to provide dynamic vBBU placement under temporal and spatial network trafc fuctuations in a powerefcient way [[4](#page-12-3), [5\]](#page-12-4). However, they are time-consuming and suitable only for small-sized networks (Fig. [1](#page-1-0)), not scaling well for large network instances [[6–](#page-12-5)[8\]](#page-12-6). Not rarely, the execution time is too long to use factual trafc information. It means that the fronthaul dimensioning might be done with outdated input data. It is, therefore, imperative that solutions operate at the same timescale as the trafc changes. Thus, an alternative solution to decrease the execution time and mitigate the scalability problem is to apply constraint relaxations to the ILP [\[8](#page-12-6)[–11](#page-13-0)]. However, linear relaxation (LP) solutions may violate the constraints in the formulation, making the solution infeasible.

A possible third way is to decouple the trafc and execution timescales if the former is known in advance. In this case, if the network operator knows a particular network

![](_page_1_Figure_5.jpeg)

<span id="page-1-0"></span>**Fig. 1** How diferent solution approaches are suited for mobile network's tidal trafc

1 3

state (trafc demands, processing node's utilization) by Δ time units earlier, it can use an allocation method that takes no longer than Δ to decide on the network placement and sizing, and the current network state would still be valid. Hence, time-consuming methods can be triggered in advance such that when the processing fnishes, it corresponds to the current network state (see Fig [1](#page-1-0) - ILP + Prediction and ML-based).

Machine learning (ML)-based techniques are suitable for solving scalability and placement problems. Moreover, they may address the problems without the infeasibility of LP solutions and the scalability of ILP formulations. They provide efcient solutions to solve placement problems in network scenarios of high trafc fuctuation, as they may take advantage of increased accurate trafc forecasting capabilities, enabling proactive solutions that can project the allocation of processing resources before the trafc pattern changes [\[12–](#page-13-1)[15](#page-13-2)]. Thus, in this paper, we present an algorithm based on deep recurrent neural networks (DRNNs) to solve the energy-efcient vBBU placement and bandwidth assignment (VB-PWA) problem, which we formally defne later in this paper. Our approach decouples the incoming trafc timescale from the operational timescale in which the algorithms solve the VB-PWA problem, by predicting future trafc variations. Moreover, as we will demonstrate later in this paper, there is a trade-of between the prediction timescale and the prediction error, which limits the use of ILPs in large-scale scenarios. To solve this problem, we also propose a polynomial-time heuristic to resize the network.

The proposed algorithm uses multi-step forecasting to predict trafc fuctuations, proactively place vBBUs, and assign bandwidth to VPONs in CF-RAN. We also present an analysis of the advantages and drawbacks of the immediate resource allocation provided by LP and ILP against our proactive ML-based approach. We also perform an analysis of the trade-of between execution time and prediction error for multi-step forecasting. We highlight the contributions of our study as follows: (1) **ML-based proactive resizing**, we present a DRNN architecture to predict the network trafc, and we also formulate a heuristic to resize the network. (2) **LP relaxation and rounding**, we show a scalable solution to vBBU and vPON assignment using linear relaxation with a rounding approach. (3) **Trade-of between multi-step prediction error and ILP**, we assess the average error of the network multi-step trafc forecasting for joint use with ILP math formulation.

We organize the rest of this work as follows: Sect. [2](#page-2-0) shows related works on network processing migration, network elements activation or deactivation, and optimally virtual BBU placement; Sect. [3](#page-2-1) presents the CF-RAN architecture organization and its functionalities; Sect. [4](#page-4-0) introduces the problem statement and the policy for network elements activation or deactivation; Sect. [5](#page-7-0) presents the ML algorithm architecture and the proactive solution proposed; Sect. [6](#page-8-0) presents the evaluation of the metrics and shows the results obtained in computational experiments; and Sect. [7](#page-12-7) presents conclusions obtained before all test were performed for all approaches and we also present future directions.

# <span id="page-2-0"></span>**2 Related work**

Some recent works investigate the use of ILP and ML in the resource allocation problems in a C-RAN architecture under dynamic trafc load [[16](#page-13-3), [17](#page-13-4)]. They investigated the optimal resource management to achieve the best provisioning in the BBU pool to maximize coverage while minimizing the optical fronthaul restrictions. However, these works neither consider hybrid architectures nor investigate the benefts of ML-based algorithms. Authors in [\[3,](#page-12-2) [18\]](#page-13-5) make use of fog-based architecture for resource allocation targeting the latency and bandwidth demand redirection. Some of these works proposed an ILP formulation to guarantee an optimal solution. However, the presented ILP use is restricted to networks with few processing nodes. Furthermore, the placement problem in virtualized networks continues with special attention, as in [[19,](#page-13-6) [20\]](#page-13-7).

Others works propose techniques to reduce the ILP execution time in large-scale networks through LP relaxation. The proposed solutions apply diferent relaxation approaches to obtain near-optimum results with a reduction in running time [\[8](#page-12-6), [21,](#page-13-8) [22](#page-13-9)]. In the context of relaxation of an ILP formulation in C-RAN, the authors in [\[23](#page-13-10)] investigate the joint caching placement and sub-carrier allocation for two slices use cases with attention to delay and data rate in a Fog-RAN architecture. Due to the scalability and non-convexity of ILP, the authors proposed an interactive method to solve it. The authors use ILP relaxation and convexifcation to generate near-optimal results. Also, the simulation shows results that converge with a fast speed.

Regarding the use of heuristics and ILP formulations, authors in [[24\]](#page-13-11) present a deep reinforcement learning (DRL) policy for routing and BBU placement in a C-RAN architecture to increase resource utilization. Authors in [[25\]](#page-13-12) implemented a long short-term memory (LSTM) network to forecast network trafc demands of BBU pools in C-RAN ROADM networks. The paper focuses on resource reallocation in advance to predict future network resource requirements. Finally, authors in [[26](#page-13-13)] introduced concepts of network resource desegregation in centralized virtualized RAN. They proposed an individual allocation of processing functions to several servers according to the network trafc load.

Unlike the previous works, we formulate and compare three approaches in CF-RAN architecture to evaluate its benefts and drawbacks in vBBU placement and VPON assignment in an energy-efcient way. We present a proactive solution that uses the network trafc prediction to scale the fronthaul. Finally, we investigate the error impact using multi-step forecasting jointly to the ILP formulation with increased analysis in the hour range. We present a brief overview of the related works comparing the solution applied and the architecture covered in Table [1](#page-2-2).

# <span id="page-2-1"></span>**3 CF‑RAN operation and system architecture**

The CF-RAN architecture and its main building blocks are depicted in Fig. [2.](#page-3-0) As one can see, there are two processing layers, an optical fronthaul and an orchestration layer, which we discuss in more detail in the following subsections.

### **3.1 Cloud and fog processing layers**

The CF-RAN architecture relies upon the network functions virtualization (NFV) paradigm to implement virtualized BBUs (vBBUs). Such vBBUs are dynamically deployed to meet trafc fuctuations, thus increasing the overall network capacity. The CF-RAN has two processing layers. The frst one is the cloud processing layer, and it is responsible for keeping the centralization benefts of CRAN when the network is under light trafc loads.

A virtualized BBU (vBBU) pool is deployed in the cloud. This pool comprises a set of Virtual Digital Units (VDUs) deployed in dedicated servers that act as containers of Virtualized Processing Functions (VPFs). The VPFs implement the vBBUs, thus forming the vBBU pool that

<span id="page-2-2"></span>**Table 1** Related works

| References                | ILP | ILP<br>Relaxa<br>tion | Machine<br>Learn<br>ing | Placement | Architecture |  |
|---------------------------|-----|-----------------------|-------------------------|-----------|--------------|--|
| Pelekanou et. al,<br>[16] | ✓   | ×                     | ✓                       | ✓         | C-RAN        |  |
| Mikaeil [17]              | ✓   | ×                     | ✓                       | ✓         | C-RAN        |  |
| Nassar [18]               | ×   | ×                     | ✓                       | ✓         | F-RAN        |  |
| Narumi et al.<br>[19]     | ✓   | ×                     | ×                       | ✓         | –            |  |
| Sebastian et.al.<br>[20]  | ✓   | ×                     | ×                       | ✓         | C-RAN        |  |
| Karzy et al. [21]         | ✓   | ✓                     | ×                       | ×         | –            |  |
| Baruah [22]               | ✓   | ✓                     | ×                       | ×         | –            |  |
| Tang et. al. [23]         | ✓   | ✓                     | ×                       | ✓         | F-RAN        |  |
| Gao et.al. [24]           | ✓   | ×                     | ✓                       | ✓         | C-RAN        |  |
| Mo et al. [25]            | ×   | ×                     | ✓                       | ✓         | C-RAN        |  |
| Gkatzios et al.<br>[26]   | ×   | ×                     | ✓                       | ✓         | C-RAN        |  |
| This work                 | ✓   | ✓                     | ✓                       | ✓         | CF-RAN       |  |

![](_page_2_Picture_16.jpeg)

<span id="page-3-0"></span>**Fig. 2** CF-RAN architecture

![](_page_3_Figure_3.jpeg)

performs virtualized baseband processing. Each vBBU of diferent VDUs may communicate with each other through an internal backplane switch that interconnects all the VDUs of the cloud. For instance, if the trafc forwarded to a vBBU exceeds its capacity, the backplane switch is activated to switch the exceeding trafc to a vBBU in another VDU if it has enough capacity.

The second layer is the fog processing layer, and it is composed of several fog processing nodes connected to the RRHs and the cloud via the optical fronthaul. Analogous to the cloud processing layer, the fog nodes also deploy a vBBU pool. However, each fog node has less processing capacity than the cloud. Moreover, a subset of RRHs is connected to the closest fog node, which may serve their trafc when the cloud node is overloaded. Finally, vBBUs in both cloud and fog nodes need to be dynamically activated to receive RRHs' trafc according to the network demand. In this sense, we assume that the servers that host the vBBU are only activated when used.

The deployment of fog processing nodes at the edge of the network considers optical network virtualization (ONV) and SDN as a proposition. It can be done by integrating the fog nodes and switches into a common Leaf-Spine L2/L3 POD-based fabric infrastructure as proposed in [[27](#page-13-14)].

### **3.2 The optical fronthaul**

The CF-RAN implements the fronthaul over a Time-and-Wavelength Division Multiplexing Passive Optical Network (TWDM-PON). It deploys virtual PON channels (VPON) to support RRH-vBBUs transmissions in an energy, latency, and bandwidth-efcient manner. The ONUs connect the RRH to its corresponding processing node, which in turn deploys the OLT.

The TWDM-PON has three multiplexing levels to interconnect Optical Network Units (ONUs) and Optical Line Terminals (OLT). Each ONU is connected to a local optical splitter (S1) (internal to a fog node) in the frst multiplexing level. For that, it uses dedicated optical fbers. The optical splitter S1 connects the VDUs of a fog node to a level 2 optical splitter (S2) through distribution fbers. The S2 optical splitter, in turn, is connected to several fog nodes and forwards trafc to a level 3 optical splitter (S3), which in

![](_page_3_Picture_11.jpeg)

turn forwards trafc to the cloud-based OLT. Moreover, S3 also receives connections from several S2 splitters through a feeder fber.

In the CF-RAN network, each ONU can be connected to either a single RRH, all RRHs in a cell site, or even subgroup of them. Except when operating in the frst confguration, the ONU aggregates the trafc of the entire cell (or the trafc coming from the group connected to it) and transmits it through a single distribution fber. Regardless of whether it is a shared or a dedicated ONU, it can transmit to any VPONs reachable by the distribution fber. Note that ONUs connected to diferent S1 splitters can tune their transmissions to the same wavelength, characterizing a VPON. We also assume virtualized PON channels (VPON) in the fronthaul, as each ONU can tune in any of the available wavelengths. In this sense, several ONUs can share the same optical channel (a VPON) in a Time Division Multiplexing (TDM) manner to transmit to a common processing node. VPONs can also be dynamically activated/created to support specifc network demands due to trafc fuctuation.

### **3.3 The workload orchestrator**

The workload orchestrator is a piece of software that provides intelligence to the CF-RAN. It is implemented in a centralized manner in a dedicated VPF in the cloud, and its goal is to promote an energy-efcient network operation. Moreover, it is responsible for gathering information about network availability and demands, besides executing the re-optimization procedures. It continuously keeps track of the number of active RRHs in the network, which vary along the day due to the UE demands. Also, it monitors the fronthaul's available capacity and the utilization of the processing nodes.

For power efciency, at the beginning of CF-RAN operation, the orchestrator activates vBBUs and set VPONs to the VDUs located in the cloud. If the cloud becomes overloaded, the orchestrator activates fog nodes to place new vBBUs and VPON on them.

Hence, for each new active RRH in the network, the orchestrator checks whether there are enough resources to instantiate a new vBBU in the cloud for this RRH or if it is necessary to activate a new VDU and create a VPON to support the baseband processing for this RRH in a fog node. This process takes place through the exchange of control messages between the RRHs and the orchestrator. Furthermore, whenever an RRH is deactivated, the orchestrator will verify if it is necessary to turn of VDUs and VPONs, or even fog nodes, to achieve more power efciency.

In summary, the CF-RAN operation is as follows: *i*) It chooses a processing node (cloud or fog) and deploys a vBBU to process the baseband signal for each active RRH; *ii*) then it allocates resources in a VPON to transmit the RRH's baseband signals to its corresponding processing node.

To properly decide whether a new processing node should be activated, where to place a vBBU, or should a new VPON be allocated, the workload orchestrator must solve the VB-PWA problem. In the next section, we formally introduce the (VB-PWA) problem and give an ILP formulation to solve it.

# <span id="page-4-0"></span>**4 Problem statement and mathematical formulations for the VB‑PWA problem**

This section presents the vBBU placement and wavelength assignment (VB-PWA) problem and optimal and near-optimal formulations to solve it. The VB-PWA problem must be properly solved because it will directly impact the power efciency of the network. Moreover, processing and network resources must be properly dimensioned, so all vBBUs can be instantiated in CF-RAN; otherwise, even blocking of transmission may occur.

### **4.1 Problem statement**

The VB-PWA problem is defned as follows: Given a set *R* of RRHs generating CPRI trafc, a set *N* of processing nodes, a set *W* of VPON channels, and a set of VDUs with the same cardinality as the set *W* on each node *n*, allocate one vBBU for each demand in *R* minimizing the number of activated processing nodes, VDUs and VPONs, and also allocate wavelengths in the fronthaul for the associated transmissions (see Table [2\)](#page-5-0).

We assume that the VDUs in the cloud are activated beforehand to receive vBBUs for initial RRHs transmissions. Hence, to save energy consumption, the fog nodes remain deactivated until the cloud capacity is attained. Fog nodes are gradually activated according to the network traffc demand, while the cloud processing capacity remains exhausted. In order to minimize the power consumption, the solution must put all trafc demands from RRHs into the least amount of processing nodes and VPONs. A bin-packing problem can model this operation as the trafc generated by each RRH needs to be put into a processing node and VPON. It is worth mentioning that if power consumption saving is not the primary goal, the activation of fog nodes may begin before the cloud is stressed to minimize the overall latency experienced by each RRH.

# **4.2 ILP formulation**

We now present an ILP formulation to optimally solve the VB-PWA problem. The main goal is to minimize power

![](_page_4_Picture_18.jpeg)

<span id="page-5-0"></span>**Table 2** Notation used for the CF-RAN virtual BBU placement optimization model.

| Symbol             | Definitions                                                                                           |  |  |  |
|--------------------|-------------------------------------------------------------------------------------------------------|--|--|--|
| Sets               |                                                                                                       |  |  |  |
| $i \in R$          | Set of RRH traffic demands                                                                            |  |  |  |
| $n \in N$          | Set of processing nodes                                                                               |  |  |  |
| $w \in W$          | Set of available wavelengths                                                                          |  |  |  |
| Input Parameters   |                                                                                                       |  |  |  |
| $B_i$              | Bandwidth demand of RRH i                                                                             |  |  |  |
| $B_w$              | Capacity of wavelength w                                                                              |  |  |  |
| $B_{en}$           | Bandwidth of the backplane switch $e$ at node $n$                                                     |  |  |  |
| $P_i$              | Processing demand of RRH i                                                                            |  |  |  |
| $P_n$              | Processing capacity of node n                                                                         |  |  |  |
| $I_w$              | Processing capacity of VDU w                                                                          |  |  |  |
| M                  | A Very big number                                                                                     |  |  |  |
| $C_n$              | Power cost of node <i>n</i>                                                                           |  |  |  |
| $C_{lc}$           | Power cost of a LC                                                                                    |  |  |  |
| $C_{vdu}$          | Power cost of VDUs in each node n                                                                     |  |  |  |
| $C_e$              | Power cost of the backplane switch e                                                                  |  |  |  |
| Decision Variables |                                                                                                       |  |  |  |
| $\chi^i_{wn}$      | 1 if the traffic demand $i$ is processed at node $n$ being transmitted at the VPON $w$ , 0 otherwise. |  |  |  |
| $u_{wn}^i$         | 1 if RRH i is processed at the VDU w at node n, 0 otherwise.                                          |  |  |  |
| $z_{wn}$           | 1 if wavelength $w$ is allocated to node $n$ , 0 otherwise.                                           |  |  |  |
| $t_n$              | 1 if processing functions and elements of node $n$ is activated, 0 otherwise.                         |  |  |  |
| $y_{in}$           | 1 if demand of $i$ was allocated to node $n$ , 0 otherwise.                                           |  |  |  |
| k <sub>in</sub>    | 1 if traffic from RRH $i$ was redirected to VDU $w$ at node $n$ , 0 otherwise.                        |  |  |  |
| $r_{wn}$           | 1 if VDU w was activated to receive a redirected RRH at node n, 0 otherwise.                          |  |  |  |
| $S_{wn}$           | 1 if VDU w is active at node n, 0 otherwise.                                                          |  |  |  |
| $e_n$              | 1 if the backplane switch $e$ is active at node $n$ , 0 otherwise.                                    |  |  |  |

consumption by activating the minimum network resources possible for the incoming demands. The sets, input parameters, and decision variables of the ILP are presented in Table 2.

(1)

#### **Objective Function**

$$\operatorname{Min} \sum_{n=1}^{N} x_n \times C_n + C_{lc} \times \sum_{n=1}^{W} \sum_{n=1}^{N} z_{wn} +$$

$$C_{VDUs} \times \sum_{w=1}^{W} \sum_{n=1}^{N} s_{wn} + C_{\text{switch}} \times \sum_{n=1}^{N} e_n$$

#### **Constraints**

$$\sum_{w=1}^{W} \sum_{n=1}^{N} x_{wn}^{i} = 1, \forall i \in R$$

$$\sum_{w=1}^{W}\sum_{n=1}^{N}u_{wn}^{i}=1, \forall i \in R$$

$$\sum_{i=1}^{R} u_{wn}^{i} \ge 0 \forall w \in W, \forall n \in N$$
 (4)

<span id="page-5-2"></span>
$$\sum_{n=1}^{N} y_{in} = 1, \forall i \in R$$
 (5)

$$y_{in} \le k_{in}, \forall i \in R, \forall n \in N$$
 (6)

<span id="page-5-4"></span><span id="page-5-3"></span>
$$\sum_{m=1}^{N} z_{wn} \le 1, \forall w \in W \tag{7}$$

<span id="page-5-6"></span><span id="page-5-5"></span><span id="page-5-1"></span>
$$z_{wn} \le s_{wn}, \forall w \in W, \forall n \in N$$
(8)

(3) 
$$\sum_{i=1}^{R} \sum_{n=1}^{N} (x_{wn}^{i} \times B_{i}) \le B_{w}, \forall w \in W$$
 (9)

![](_page_5_Picture_17.jpeg)

$$\sum_{i=1}^{R} \sum_{w=1}^{W} (x_{wn}^{i} \times P_{i}) \le P_{n}, \forall n \in \mathbb{N}$$

$$M \times t_n \ge \sum_{i=1}^R \sum_{w=1}^W x_{wn}^i, \forall n \in \mathbb{N}$$

$$t_n \le \sum_{i=1}^{R} \sum_{w=1}^{W} x_{wn}^i, \forall n \in \mathbb{N}$$

$$M \times z_{wn} \ge \sum_{i=1}^{R} x_{wn}^{i}, \forall w \in W, \forall n \in N$$

$$z_{wn} \le \sum_{i=1}^{R} x_{wn}^{i}, \forall n \in N, \forall w \in W$$

$$M \times e_n \ge \sum_{i=1}^R k_{in}, \forall n \in N$$

$$\sum_{i=1}^{R} \sum_{n=1}^{N} u_{wn}^{i} \ge I_{w}, \forall w \in W$$

$$M \times y_{in} \ge \sum_{w=1}^{W} x_{wn}^{i}, \forall n \in \mathbb{N}, \forall i \in \mathbb{R}$$

$$y_{in} \le \sum_{w=1}^{W} x_{wn}^{i}, \forall n \in \mathbb{N}, \forall i \in \mathbb{R}$$

$$M \times y_{in} \ge \sum_{w=1}^{W} u_{wn}^{i}, \forall n \in \mathbb{N}, \forall i \in \mathbb{R}$$

$$y_{in} \leq \sum_{w=1}^{W} u_{wn}^{i}, \forall n \in N, \forall i \in R$$

$$M \times s_{wn} \ge \sum_{i=1}^{R} u_{wn}^{i}, \forall w \in W, \forall n \in N$$

$$s_{wn} \le \sum_{i=1}^{R} u_{wn}^{i}, \forall w \in W, \forall n \in N$$

$$\sum_{i=1}^{R} k_{in} \times B_i \ge B_{en}, \forall n \in \mathbb{N}$$

$$(10) e_n \le \sum_{i=1}^K k_{in}, \forall n \in N$$

Constraints (2)-(5) ensure that each demand from RRH *i* is allocated to only one VDU, one processing node, and one VPON. Constraint (6) indicates the set of processing nodes in which a VPON can be assigned. Constraint (7) ensures that a VPON transmits to at most one processing node (fog or cloud). Constraint (8) guarantees that each RRH *i* is allocated only to the processing node assigned to it. Constraints (9) - (1516) ensure that processing nodes, VPONs, and the backplane switches have enough processing capacity to handle RRHs requests. The other constraints enforce the activation of the backplane switch on each processing node and the activation of additional VDUs in case of traffic forwarding by the backplane switch.

#### 4.3 LP relaxation

(11)

(12)

(13)

(14)

- <span id="page-6-1"></span><span id="page-6-0"></span>(15) To speed up the execution of the ILP model in large networks instances, we devised a linear relaxation to this formulation. Linear relaxation is an approximation technique for complex linear problems with promising use in highly complex integer problems. This technique produces optimum or near to optimal solutions when compared to the ILP by relaxing the integrality of some integer variables.
- ables [28]. For that, we solve the linear program in polynomial approximation time and then "round" the relaxed solution to an integer solution to the original ILP (see Fig. 3). We relaxed the following variables of the proposed [18]
- $0 \le u_{nm}^{i} \le 1, \forall i \in R, \forall n \in N, \forall w \in W$  (25)

$$(19) 0 \le y_{in} \le 1, \forall i \in R, \forall n \in N$$
 (26)

$$0 \le k_{in} \le 1, \forall i \in R, \forall n \in N \tag{27}$$

$$(20) t_n \in \{0\} \cup [1, \infty], \forall n \in \mathbb{N}$$
 (28)

$$(21) s_{wn} \in \{0\} \cup [1, \infty], \forall n \in \mathbb{N}, \forall w \in \mathbb{W}$$

$$z_{wn} \in \{0\} \cup [1, \infty], \forall n \in \mathbb{N}, \forall w \in \mathbb{W}$$
 (30)

region, the optimum value of the former is no worse than

- We have changed the t<sub>n</sub>, s<sub>wn</sub> and z<sub>wn</sub> variables from binary to semi-continuous, and y<sub>in</sub>, k<sub>in</sub> and u<sup>i</sup><sub>wn</sub> from binary to continuous. Note that the ideal solution for LP relaxation is not necessarily an integer solution. We make it integral using a rounding function after getting the relaxed solution. However, since the viable LP region is larger than the viable ILP

![](_page_7_Figure_2.jpeg)

<span id="page-7-1"></span>Fig. 3 LP rounding process

the optimum value of the latter. In this way, we can obtain optimum values or close to optimum through this technique with improved computing performance.

#### <span id="page-7-0"></span>5 ML-based formulation

As we mentioned before, providing timely and accurate network sizing requires precise knowledge or a realistic estimate of the traffic demands. However, networks, in general, have non-stationary behavior and are highly dynamic. As a result, fluctuations in traffic and processing demands become hard to predict because past behaviors influence the current ones.

To capture such a relationship, we modeled our problem with a DRNN. DRRNs maintain connections between hidden state layers, allowing memories of previous actions to be saved, making them applicable to problems arranged in series [29]. Specifically, we consider the LSTM, which is a particular kind of RNN. LSTM is well known for its application in several areas like speech recognition and time series prediction [30, 31]. Its extensive use is due to its ability to learn from past historical values to forecasting future occurrences. The memory cells in the hidden

layer of LSTM (see Fig. 4) can filter, store, and forget information associated with the previous network state. This aspect of the LSTM makes it suitable for processing time series-based problems, as the cell output depends on the assigned sequence of past states. For general purposes, LSTM algorithm has commonly in its composition a cell  $(c_i)$ , an output gate  $(o_i)$ , an input gate  $(i_i)$ , and a forget gate  $(f_i)$  that receives data from an input vector  $x_i$  to the LSTM unit. In short, the cell contains values, and the gates manage the information in the cells [32].

We implemented an LSTM multivariate to forecasting network state by analyzing metrics collected in CF-RAN dynamic network scenarios. The loss function uses mean absolute error (MAE); the optimizer uses Adam; and the adopted activation function is the ReLU to minimize the expected loss value after training and improve forecasting capacity. More specifically, our LSTM forecasts the network load for the next hour interval considering previous results. Also, we generated training scenarios with different traffic distributions and different network requirements so that LSTM can learn the pattern data through the variations identified in the execution.

![](_page_7_Picture_10.jpeg)

Fig. 4 LSTM representation

<span id="page-7-2"></span>![](_page_7_Picture_12.jpeg)

We consider the following performance metrics to the ML model: 1) MAE  $\sum_{i=1}^{n} \frac{\hat{y}_i - y_i}{n}$ ; 2)  $R^2$  score or coefficient of determination  $\sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2$ .

We performed online training and validation to reach the best performance and accurate prediction model for operating with data input in CF-RAN scenarios. MAE forecast results (see Fig. 5) computed with 100 epochs attests that prediction accuracy reached a low error value in predicting network state. The result is an indication that the ML algorithm reached a suitable model for testing scenarios. Furthermore, it shows a good fit due to the training, and validation loss has a decedent point of stability with minimum fluctuation in its values. We also evaluated accuracy prediction using other regression metrics, which shows the forecast output of the neural network and the coincidence with the ILP results target. The coefficient of determination, with  $R^2$  value reaching 0.95, corresponds to 95% of adjustment of the ML model. To avoid overfitting, we use a dropout rate of 15%.

#### 5.1 Proactive ML network resizing

We now present a DRNN-based heuristic to solve the VB-PWA problem. The general idea is to enable VPONs and vBBUs using next-hop traffic prediction as input to network resizing.

As we will demonstrate later in Sect. 6 (see Fig. 6), the traffic prediction alone cannot guarantee the proper sizing of the network. Even when combined with optimum methods like the proposed ILP, it is hard to manage the prediction error if the prediction period is too long (which would be the best-fit solution if the ILP takes too long to solve the VB-PWA problem). The prediction error increment, in turn, corresponds to having outdated data and leads to resource

![](_page_8_Figure_7.jpeg)

<span id="page-8-1"></span>Fig. 5 MAE loss acquired

wastage. Therefore, the use of fast methods to solve the VP-PWA problem is imperative.

In this section, we propose a polynomial-time heuristic algorithm to solve the VB-PWA problem under traffic fluctuation. Our algorithm ensures that the network resizing to support the actual network load will follow the traffic forecast.

#### **Algorithm 1** Proactive network resizing

```
1: Input: Network traffic predicted; W; N
2: Output: Network resizing
3: t \leftarrow \text{traffic prediction by ML};
 4: while t > 0 do
                                  ▶ Update network state
       if CloudCapacity \geq t then
5:
          allocates t to the Cloud node n and wavelengths
   w and updates the network status.
7:
       else if CloudCapacity < t then
8.
          t' \leftarrow t - CloudCapacity
9:
          allocates t' to fog nodes n and wavelengths w and
   updates the network status.
10:
       else
           block t'
11:
```

The algorithm takes a variable t with the predicted network load (line 3). All incoming demands will be allocated into the cloud node to guarantee energy efficiency (lines 4-6). However, if the fronthaul gets congested and the cloud facility experiences a shortage of processing capacity, fog nodes receive the exceeding demands (lines 7-9). Fog nodes are activated only on demand. If there is not enough network capacity or resources, demands will be blocked (lines 10-11).

### <span id="page-8-0"></span>6 Illustrative numerical results

We evaluated the proposed approach in two different scenarios. In the first scenario, we investigate the scalability of solutions through the incremental growth of demand. In the second scenario, we assess the solutions under network traffic in a business area [33, 34]. We also investigate the impact of using multi-step time series forecasting to evaluate the use of multiple hops in hour range in prediction to give the ILP solver more time to generate optimal results. For the evaluation, we used the 5GPy simulator to execute our simulations [35]. The simulation parameters used in the simulations are presented in Table 3.

To assess the performance of the evaluated approaches, we analyze the following performance metrics: the CPU intensity and the overall network power consumption.

The CPU intensity accounts for the amount of CPU consumption per second. We calculate this CPU intensity by subtracting the total CPU available with the idle CPU at the second t, and then, we divide the total CPU by the total execution time (T)

![](_page_8_Picture_18.jpeg)

<span id="page-9-1"></span>**Table 3** Simulation parameters

| Parameter              | Value            |  |  |
|------------------------|------------------|--|--|
| RRH Confguration       | 10 MHz, 1x1 MIMO |  |  |
| RRH-vBBU Communication | CPRI line 1      |  |  |
| Cloud cost             | 600 watts        |  |  |
| Fog node cost          | 300 watts        |  |  |
| Line Card cost         | 20 watts         |  |  |
| OLT cost               | 100 watts        |  |  |
| Switch cost            | 15 watts         |  |  |
| Cloud VDU cost         | 100 watts        |  |  |
| Fog VDU cost           | 50 watts         |  |  |
|                        |                  |  |  |

![](_page_9_Figure_4.jpeg)

<span id="page-9-0"></span>**Fig. 6** Multi-step time series forecasting

$$CPU = \sum_{t=1}^{T} (CPU_{(t)} - idle_{(t)}) \Longrightarrow CPU/T.$$

The power consumption is the prime metric evaluated once it corresponds to the objective function of our ILP. This metric relates to the number of active network resources. We present its parameters in Table [3.](#page-9-1)

### **6.1 Multi‑step time series forecasting evaluation**

As we mentioned before, ILP-based solutions, in general, are non-scalable due to the data entry size. Thus, their execution time is usually long, and the longer it is, the earlier the prediction must be made. However, it is also well known that the prediction error increases proportionally to the prediction period (Fig. [1](#page-1-0)). Hence, the ILP can be applied only if the prediction error is not impactful. Therefore, we evaluated this trade-of by implementing an LSTM for multi-step time series forecasting problems and assessed the average error

![](_page_9_Picture_10.jpeg)

Figure [6](#page-9-0) presents the impact of predicting the network trafc with a prediction period longer than one hour. Results show that when predicting one hour in advance, the MAE is 1.19 *Gbps*, which does not represent the degeneration of trafc demand allocation. However, as we increase the prediction interval, the average error rate grows, and the total amount of non-allocated demands increases to a level of lack of optimality. The most signifcant benefts of the ILP model, such as optimal results, are impaired for this high error rate in predictions.

# **6.2 Scalability analysis**

The scalability test is to analyze if the system can handling the increasing trafc and maintaining the CF-RAN operation without any impact on performance. Also, we study if the CF-RAN management guarantees the correct resizing of the network in all solutions investigated in terms of response time and correctness. To evaluate the scalability of the proposed approach, we consider a CF-RAN with a TWDM-PON fronthaul with 24 wavelengths (*w* = {1, 2, …, 24}) of 10 *Gbps* and composed of 1 cloud and 9 fog nodes (*n* = {1, 2, 3, 10}). The ILP and LP relaxation models were implemented using DOCPLEX Python API using a CPLEX 12.10 as the solver. The limitations for wavelength channels were not considered in their simulation scenarios.

The DRNN received the trafc generated by the simulator as input. This simulation shows how the solutions respond in terms of the execution time, memory consumption, and CPU intensity as the load grows evenly.

Figure [7](#page-10-0)a shows that as the network size grows, the solver time increases in such a way that the ILP becomes impractical to decide the network dimensioning in real time. High peak values for a 200 *Gbps* input show that it takes more than one hour to solve the optimal allocation. Also, Fig. [7a](#page-10-0) shows linear time complexity behavior when comparing the ILP with the other solutions. However, Fig. [7](#page-10-0)b shows that the LP solver presents an upward trend behavior, but with solver peaks time much lower than the ILP. On the other hand, the ML-based heuristic execution time showed a linear behavior that was much lower than both solutions. The maximum LP time represented ≈ 4.1% of the ILP time in peak comparison. On the other hand, the ML-based solution presented gains in execution time higher than 99.99% compared to the ILP.

Figure [8](#page-10-1) shows the computational resource consumption as a function of the network growth. Figure [8a](#page-10-1) shows that CPU intensity produced by the ILP is higher than the other approaches and presents an upward behavior as the network size grows. The LP also shows upward behavior, unlike MLbased, which shows an almost linear behavior trend.

![](_page_9_Picture_17.jpeg)

![](_page_10_Figure_2.jpeg)

<span id="page-10-0"></span>Fig. 7 Results comparison of runtime for all proposed solutions

We also investigated memory consumption. The memory usage produced by solvers is closely related to information like the number of threads used and the type of problem. Figure 8b shows the memory consumption with upward behavior in both LP and ILP. The growth in memory consumption is observed as the size of the network increases. On the other hand, memory consumption in the ML-based solution is stable ( $\approx 44\%$ ). These results show the much lower computational resource needed by the ML-based heuristic.

#### 6.2.1 One-day traffic forecasting

We now evaluate the studied approaches using traffic forecasting. Table 4 shows the comparison of the solver time and the percentage gap, given as

<span id="page-10-1"></span>Fig. 8 Results comparison of CPU intensity and memory for all proposed solutions

$$\frac{\max(ILP, LP) - \min(ILP, LP)}{\max(ILP, LP)} \times 100.$$

The percentage gap of the final solution stayed close to zero, implying that, in terms of optimality, the LP relaxation is a viable alternative to ILP once it presented optimal or very close to optimal solutions. The ML-based heuristic also presented close to optimal solutions and, comparing the gap, presented also low disparity from the ILP.

Moreover, the integrality gap, given by  $(IG = \frac{ILP}{LR})$ , remains most of the execution time close to 1, which means that the LP relaxation provides optimal integer solutions. The ML-based heuristic maintained close results to the ILP with lower time and computational resource consumption.

![](_page_10_Picture_11.jpeg)

### 6.3 Dynamic traffic scenarios

We use the 5GPy simulator [35] for dynamic traffic analysis. The maximum traffic load of each hourly operation is  $(\epsilon/60)$ , where  $\epsilon$  is the maximum Erlang for a given hour [35]. At the beginning of the simulation, the RRHs are inactive. The network demands arrive according to a Poisson distribution and hold during a time interval that follows the negative

exponential distribution. We used the independent replication method with 50 executions to generate a confidence interval of 95%. This traffic behavior follows a business access network area following patterns detailed in [33, 34]. For this set of simulations, we consider a CF-RAN architecture with 7 wavelengths ( $w = \{1, 2, ..., 7\}$ ) of 10 *Gbps*, composed of 1 cloud and 3 fog nodes ( $n = \{1, 2, 3, 4\}$ ).

<span id="page-11-0"></span>**Table 4** Comparison of objective function value, CPU intensity, and gap

| Traffic (Mbps) | Objective Function Value |         |          | CPU Intensity (%) |         |          | Gap        |            |
|----------------|--------------------------|---------|----------|-------------------|---------|----------|------------|------------|
|                | Exact                    | Relaxed | ML-based | Exact             | Relaxed | ML-based | ILP-LP (%) | ILP-ML (%) |
| 6144.0         | 620.0                    | 620.0   | 620.0    | 41.1              | 23.1    | 10.6     | 0.0        | 0.0        |
| 30720.0        | 680.0                    | 680.0   | 680.0    | 42.4              | 30.6    | 17.3     | 0.0        | 0.0        |
| 61440.0        | 740.0                    | 740.0   | 740.0    | 55.1              | 32.4    | 16.9     | 0.0        | 0.0        |
| 92160.0        | 800.0                    | 800.0   | 800.0    | 48.8              | 43.0    | 16.5     | 0.0        | 0.0        |
| 122880.0       | 1160.0                   | 1160.0  | 1160.0   | 66.9              | 31.6    | 14.8     | 0.0        | 0.0        |
| 153600.0       | 2440.0                   | 2440.0  | 2480.0   | 79.5              | 44.1    | 10.7     | 0.0        | 0.82       |
| 168960.0       | 2860.0                   | 3020.0  | 2880.0   | 82.5              | 49.1    | 10.1     | 5.28       | 0.69       |
| 178176.0       | 2920.0                   | 3020.0  | 2980.0   | 79.5              | 44.1    | 10.7     | 3.31       | 2.01       |

Results acquired in the static evaluation of the network. The data entry corresponds to the traffic generated. The gap tests were performed in comparison with the result presented by the ILP

![](_page_11_Figure_8.jpeg)

![](_page_11_Figure_9.jpeg)

![](_page_11_Figure_10.jpeg)

<span id="page-11-1"></span>Fig. 9 Network traffic load and avg. solver time

![](_page_11_Figure_12.jpeg)

![](_page_11_Figure_13.jpeg)

![](_page_11_Figure_14.jpeg)

<span id="page-11-2"></span>Fig. 10 ML, LP, and ILP comparisons in dynamic scenario

![](_page_11_Picture_16.jpeg)

Figures [9](#page-11-1) and [10](#page-11-2) show the average of network resources activation and energy consumption, respectively, using traffc loads predicted one hour in advance. The results obtained in the forecast demonstrate precise results concerning the energy consumption and network trafc load expected. The maximum prediction error observed in the power consumption was 35 *Watts* (see Fig. [9](#page-11-1)a), while the forecasting error in network trafc load was ≈ 1.2 *Gbps* (see Fig. [9b](#page-11-1)). Figure [9c](#page-11-1) shows that the behavior related to CPU intensity in the ILP solution presents a high CPU intensity consumption value. On the other hand, the ML-based heuristic continues as the solution that consumes less computational resources.

Figure [10](#page-11-2)a, b and c shows the average result of the CF-RAN network related to all three approaches. The results of ML-based forecasting show statistical approximation values to those obtained using the ILP formulation. Figure [10](#page-11-2)a shows the energy consumption of the approaches. It is possible to see that the results generated by ML are statistically equal to the ILP. Moreover, the ML-based behaves like the ILP and LP relaxation, which is also consistent with the results in Fig. [10](#page-11-2)b and c, related to the avg. nodes activation and VPON wastage. Nevertheless, when we compared the CPU intensity in all three solutions, we observed that the lowest value remains in the ML-based solution.

The results in simulation support that the ILP scalability problem can be circumvented using other approaches like linear relaxation and ML-based heuristics. But, although the LP relaxation reaches large-scale networks, there is an internal issue related to the solution's unfeasibility. Therefore, an ML-based heuristic proved to be a promising alternative to solve the VB-PWA problem. The results acquired show that ML-based heuristic maintains near-optimal results and could maintaining the CF-RAN operation

# <span id="page-12-7"></span>**7 Conclusion**

In this work, we approach a hybrid architecture presented by the literature that allows us to mitigate some problems arising from the centralization of the CRAN through fog and VNF nodes. We address the problem related to the placement of virtual BBUs to expand the fronthaul capacity and, at the same time, reduce costs with energy consumption. We compare an optimal solution performed by ILP with two heuristics related to LP relaxation and ML-based. Our results demonstrate that LP relaxation can achieve optimal or near-optimal results while signifcantly reducing CPU Intensity, memory consumption, and execution time. Also, we compare it to another heuristic based on predictions by time series that show expressive results in reducing the execution time and memory consumption. The execution time, memory consumption, CPU intensity and also present near-optimal results. In future work, we will propose alternative heuristics using other ML algorithms to improve results. One of the alternatives considered will be the use of deep reinforcement learning.

**Data Availability Statement** The data generated during and/or analyzed during the current study were generated in a simulator available at: https://github.com/rodrigo-tinini/5GPy. The dataset used in the research can be made available on reasonable request to the author.

### **Declarations**

**Conflict of interest** The authors declare that they have no confict of interest.

# **References**

- <span id="page-12-0"></span>1. Wu, J., Zhang, Z., Hong, Y., Wen, Y.: Cloud radio access network (C-RAN): a primer. IEEE Network **29**(1), 35–41 (2015). <https://doi.org/10.1109/MNET.2015.7018201>
- <span id="page-12-1"></span>2. ITU-T, Recommendation G. "989.3," 40-Gigabit-capable passive optical networks (NG-PON2): Transmission convergence layer specifcation,"." International Telecommunication Union (2021)
- <span id="page-12-2"></span>3. Tinini, R.I., Batista, D.M., Figueiredo, G.B., Tornatore, M., Mukherjee, B.: Low-latency and energy-efcient BBU placement and VPON formation in virtualized cloud-fog RAN. IEEE/ OSA J Opt Commun Netw **11**(4), B37–B48 (2019). [https://doi.](https://doi.org/10.1364/JOCN.11.000B37) [org/10.1364/JOCN.11.000B37](https://doi.org/10.1364/JOCN.11.000B37)
- <span id="page-12-3"></span>4. Colman-Meixner C, Figueiredo GB, Fiorani M, Tornatore M, Mukherjee B (2016)"Resilient cloud network mapping with virtualized BBU placement for cloud-RAN," 2016 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS), Bangalore, India, pp. 1-3, [https://](https://doi.org/10.1109/ANTS.2016.7947790) [doi.org/10.1109/ANTS.2016.7947790](https://doi.org/10.1109/ANTS.2016.7947790)
- <span id="page-12-4"></span>5. Marotta, A., Correia, L.M.: Cost-efective joint optimisation of BBU placement and fronthaul deployment in brown-feld scenarios. J Wireless Com Netw **2020**, 242 (2020). [https://doi.](https://doi.org/10.1186/s13638-020-01844-9) [org/10.1186/s13638-020-01844-9](https://doi.org/10.1186/s13638-020-01844-9)
- <span id="page-12-5"></span>6. Krasimira G, Vassil G (2011) Linear integer programming methods and approaches-a survey. Cybernetics and Information Technologies. 11
- 7. Chen, H., Li, L., Jing, R., Wang, Y., Zhao, Y., Wang, X., Wang, S., Xu, S.: "A scheme to optimize fow routing and polling switch selection of software defned networks. PloS one **10**, e0145437 (2015). [https://doi.org/10.1371/journal.pone.01454](https://doi.org/10.1371/journal.pone.0145437) [37](https://doi.org/10.1371/journal.pone.0145437)
- <span id="page-12-6"></span>8. Noor-E-Alam, M.D., Doucette, J.: Relax-and-fx decomposition technique for solving large scale grid-based location problems. Comput Indus Eng **63**(4), 1062–1073 (2012). [https://doi.org/10.](https://doi.org/10.1016/j.cie.2012.07.006) [1016/j.cie.2012.07.006](https://doi.org/10.1016/j.cie.2012.07.006)
- 9. Benson, H.P.: An all-linear programming relaxation algorithm for optimizing over the efcient set. J Glob Optim **1**, 83–104 (1991).<https://doi.org/10.1007/BF00120667>
- 10. Lee, S.S.W., Chen, A., Yuang, M.C.: A Lagrangean relaxation based near-optimal algorithm for advance lightpath reservation in WDM networks. Photon Netw Commun **19**, 103–109 (2010). <https://doi.org/10.1007/s11107-009-0215-9>

![](_page_12_Picture_22.jpeg)

- <span id="page-13-0"></span>11. Rodrigues de Sousa, V.J., Anjos, M.F., Le Digabel, S.: Improving the linear relaxation of maximum k-cut with semidefnitebased constraints. EURO J Comput Optim **7**, 123–151 (2019). <https://doi.org/10.1007/s13675-019-00110-y>
- <span id="page-13-1"></span>12. Zhang, C., Zhang, H., Yuan, D., Zhang, M.: Citywide cellular trafc prediction based on densely connected convolutional neural networks. IEEE Commun Lett **22**(8), 1656–1659 (2018). <https://doi.org/10.1109/LCOMM.2018.2841832>
- 13. Huang, Y., Qian, L., Feng, A., Yu, N., Wu, Y.: Short-term trafc prediction by two-level data driven model in 5G-enabled edge computing networks. IEEE Access **7**, 123981–123991 (2019). <https://doi.org/10.1109/ACCESS.2019.2938236>
- 14. Mejia, J., Ochoa-Zezzati, A., Cruz-Mejía, O.: Trafc forecasting on mobile networks using 3D convolutional layers. Mobile Netw Appl **25**, 2134–2140 (2020). [https://doi.org/10.1007/](https://doi.org/10.1007/s11036-020-01554-y) [s11036-020-01554-y](https://doi.org/10.1007/s11036-020-01554-y)
- <span id="page-13-2"></span>15. Rahman, S., Ahmed, T., Ferdousi, S., et al.: Virtualized controller placement for multi-domain optical transport networks using machine learning. Photon Netw Commun **40**, 126–136 (2020). <https://doi.org/10.1007/s11107-020-00895-8>
- <span id="page-13-3"></span>16. Pelekanou A, Anastasopoulos M, Tzanakaki A, Simeonidou D (2018)"Provisioning of 5G services employing machine learning techniques," (2018) International Conference on Optical Network Design and Modeling (ONDM), Dublin, pp. 200-205, <https://doi.org/10.23919/ONDM.2018.8396131>
- <span id="page-13-4"></span>17. Mohammed Mikaeil, A., Hu, W., Li, L.: Joint allocation of radio and fronthaul resources in multi-wavelength-enabled C-RAN based on reinforcement learning. J Lightwave Technol **37**(23), 5780–5789 (2019). <https://doi.org/10.1109/JLT.2019.2939169>
- <span id="page-13-5"></span>18. Nassar, A., Yilmaz, Y.: Reinforcement learning for adaptive resource allocation in fog RAN for IoT with heterogeneous latency requirements. IEEE Access **7**, 128014–128025 (2019). [https://doi.](https://doi.org/10.1109/ACCESS.2019.2939735) [org/10.1109/ACCESS.2019.2939735](https://doi.org/10.1109/ACCESS.2019.2939735)
- <span id="page-13-6"></span>19. Kiji, N., Sato, T., Shinkuma, R., Oki, E.: Virtual network function placement and routing for multicast service chaining using merged paths. Opt Switch Netw **36**, 100554 (2020)
- <span id="page-13-7"></span>20. Troia, S., Cibari, A., Alvizu, R., Maier, G.: Dynamic programming of network slices in software-defned metro-core optical networks. Opt Switch Network **36**, 100551 (2020)
- <span id="page-13-8"></span>21. Noor-E-Alam, M.D., Zaky Kasem, A., Doucette, J.: ILP model and relaxation-based decomposition approach for incremental topology optimization in p-Cycle networks. J Comput Network Commun (2012).<https://doi.org/10.1155/2012/546301>
- <span id="page-13-9"></span>22. Baruah, S.K., Bonifaci, V., Bruni, R., et al.: ILP models for the allocation of recurrent workloads upon heterogeneous multiprocessors. J Sched **22**, 195–209 (2019). [https://doi.org/10.1007/](https://doi.org/10.1007/s10951-018-0593-x) [s10951-018-0593-x](https://doi.org/10.1007/s10951-018-0593-x)
- <span id="page-13-10"></span>23. Tang L, Zhang X, Xiang H, Sun Y, Peng M (2017)"Joint resource allocation and caching placement for network slicing in fog radio access networks," (2017) IEEE 18th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC), pp. 1-6,<https://doi.org/10.1109/SPAWC.2017.8227791>
- <span id="page-13-11"></span>24. Gao Z, Zhang J, Yan S, Xiao Y, Simeonidou D, Ji Y (2019)"Deep reinforcement learning for BBU placement and routing in C-RAN," Optical Fiber Communications Conference and Exhibition (OFC). San Diego, CA, USA **2019**, 1–3
- <span id="page-13-12"></span>25. Mo W, Gutterman CL, Li Y, Zussman G, Kilper DC (2018)"Deep Neural Network Based Dynamic Resource Reallocation of BBU Pools in 5G C-RAN ROADM Networks," in Optical Fiber Communication Conference, OSA Technical Digest (online) (Optical Society of America, 2018), paper Th1B.4
- <span id="page-13-13"></span>26. Gkatzios, N., Anastasopoulos, M., Tzanakaki, A., et al.: Efciency gains in 5G softwarised radio access networks. J

- Wireless Com Network **2019**, 183 (2019). [https://doi.org/10.1186/](https://doi.org/10.1186/s13638-019-1488-z) [s13638-019-1488-z](https://doi.org/10.1186/s13638-019-1488-z)
- <span id="page-13-14"></span>27. Yang B, Zhang Z, Zhang K, Weisheng H (2016)"Integration of micro data center with optical line terminal in passive optical network," 2016 21st OptoElectronics and Communications Conference (OECC) held jointly with. International Conference on Photonics in Switching (PS) (2016), 1–3
- <span id="page-13-15"></span>28. Matoušek J. Gärtner B (2007) Integer programming and LP relaxation. In: Understanding and Using Linear Programming. Universitext. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/](https://doi.org/10.1007/978-3-540-30717-4_3) [978-3-540-30717-4\\_3](https://doi.org/10.1007/978-3-540-30717-4_3)
- <span id="page-13-16"></span>29. Cao, J., Li, Z., Li, J.: Financial time series forecasting model based on CEEMDAN and LSTM. Physica A: Statist Mech Appl **519**, 127–139 (2019). <https://doi.org/10.1016/j.physa.2018.11.061>. (**ISSN 0378-4371**)
- <span id="page-13-17"></span>30. Lipton CZ (2015) "A critical review of recurrent neural networks for sequence learning." ArXiv abs/1506.00019
- <span id="page-13-18"></span>31. Smagulova, K., James, A.P.: A survey on LSTM memristive neural network architectures and applications. Eur Phys J Spec Top **228**, 2313–2324 (2019).<https://doi.org/10.1140/epjst/e2019-900046-x>
- <span id="page-13-19"></span>32. Ketkar N (2017) Deep learning with python a hands-on introduction, Apress, Berkeley, CA. [https://doi.org/10.1007/](https://doi.org/10.1007/978-1-4842-2766-4) [978-1-4842-2766-4](https://doi.org/10.1007/978-1-4842-2766-4)
- <span id="page-13-20"></span>33. Peng C, Lee SB, Lu S, Luo H, Li H (2011) Trafc-driven power saving in operational 3G cellular networks. In Proceedings of the 17th annual international conference on Mobile computing and networking (MobiCom '11). Association for Computing Machinery, New York, NY, USA, 121-132.<https://doi.org/10.1145/2030613.2030628>
- <span id="page-13-21"></span>34. Wang, X., et al.: Energy-efcient virtual base station formation in optical-access-enabled cloud-RAN. IEEE J Select Areas Commun **34**(5), 1130–1139 (2016).<https://doi.org/10.1109/JSAC.2016.2520247>
- <span id="page-13-22"></span>35. Tinini, R.I., Santos, M.R.P., Figueiredo, G.B., Batista, D.M.: A SimPy-based simulator for performance evaluations in 5G hybrid Cloud-Fog RAN architectures. Simul Model Pract Theory **101**, 102030 (2020). <https://doi.org/10.1016/j.simpat.2019.102030>. (**ISSN 1569-190X**)

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afliations.

![](_page_13_Picture_29.jpeg)

**Matias R.P.dos Santos** holds a bachelor's degree in Computer Science fromEstácio de Teresina (2015), a master's degree in Computer Science from the FederalUniversity of Ceará (2018), and currently is a Computer Science Ph.D. student at FederalUniversity of Bahia. I am currently part of the ION (Intelligent Optical Network) researchgroup at the Federal University of Bahia.

![](_page_13_Picture_31.jpeg)

**Rodrigo I.Tinini** holds a degree in Computer Science from Municipal University of São-Caetano do Sul (2011), a master's degree in Computer Science from Federal University of ABC(2014), and a Ph.D. in Computer Science from the University of São Paulo (2019), where he iscurrently a research fellow. His current research interests are: Optical Networks, 5G Networks,Internet of Things, and Artifcial Intelligence applied to

optical and mobile networks.

![](_page_13_Picture_34.jpeg)

![](_page_14_Picture_2.jpeg)

**Tiago O.Januario** holds a Ph.D. from the Federal University of Minas Gerais and is anAdjunct Professor at the Department of Computer Science at the Federal University of Bahia -UFBA.

![](_page_14_Picture_4.jpeg)

**Gustavo B.Figueiredo** received his B.Sc. degree in Computer Science from SalvadorUniversity (2001), and the M.Sc. (2003) and Ph.D. (2009) degrees in Computer Science from theUniversity of Campinas. Since 2010, he has been afliated with the Department of ComputerScience of the Federal University of Bahia, Bahia - Brazil, where is currently an AssociateProfessor. His main research interest includes problems involving Optical and Mobile Networks.

![](_page_14_Picture_6.jpeg)
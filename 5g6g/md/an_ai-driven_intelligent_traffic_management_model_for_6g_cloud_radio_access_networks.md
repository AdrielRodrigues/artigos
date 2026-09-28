# An AI-Driven Intelligent Traffic Management Model for 6G Cloud Radio Access Networks

Smruti Rekha Swain<sup>®</sup>, Deepika Saxena<sup>®</sup>, Jatinder Kumar, Ashutosh Kumar Singh<sup>®</sup>, *Senior Member IEEE*, and Chung-Nan Lee, *Member, IEEE* 

Abstract—This letter proposes a novel Cloud Radio Access Network (C-RAN) traffic analysis and management model that estimates probable RAN traffic congestion and mitigate its effect by adopting a suitable handling mechanism. A computation approach is introduced to classify heterogeneous RAN traffic into distinct traffic states based on bandwidth consumption and execution time of various job requests. Further, a cloud-based traffic management is employed to schedule and allocate resources among user job requests according to the associated traffic states to minimize latency and maximize bandwidth utilization. The experimental evaluation and comparison of the proposed model with state-of-the-art methods reveal that it is effective in minimizing the worse effect of traffic congestion and improves bandwidth utilization and reduces job execution latency up to 17.07% and 18%, respectively.

Index Terms—C-RAN, congestion, stragglers, network hogs.

## <span id="page-0-1"></span>I. INTRODUCTION

**B** OOMING C-RAN traffic (i.e., RAN traffic based on a centralized cloud computing used in the deployment of 5G networks to provide improved cellular coverage, capacity, and reliability) has become inevitable with the emerging technologies, including 6G wireless communication networks, Internet of Things (IoT), and unmanned aerial vehicle (UAV) assisted networks, etc [1]. According to a recent report, the C-RAN market size is projected to grow from USD 5.5 billion in 2022 to USD 43.2 billion by 2032, at a Compound Annual Growth Rate (CAGR) of 22.9% during the forecast period. C-RAN allows virtualization of networks and customize them to cater the specific needs of applications, services, devices, and customers [2]. However, the diversity and complexity of 6G C-RAN environment impose a critical and challenging issue of wireless traffic management because of conflicting perspectives of customers and service provider where, the former aspires for highest service quality

Manuscript received 16 January 2023; revised 9 March 2023; accepted 16 March 2023. Date of publication 21 March 2023; date of current version 9 June 2023. This work was supported in part by the National Institute of Technology Kurukshetra, India, and in part by the National Sun Yat-sen University, Kaohsiung, Taiwan. The associate editor coordinating the review of this article and approving it for publication was H. Lee. (Corresponding author: Deepika Saxena.)

Smruti Rekha Swain, Jatinder Kumar, and Ashutosh Kumar Singh are with the Department of Computer Applications, National Institute of Technology, Kurukshetra 136119, India (e-mail: smruti.sai90@gmail.com; jatinderkumar2851@gmail.com; ashutosh@nitkkr.ac.in).

Deepika Saxena is with the Department of Computer Science, Goethe University Frankfurt, Frankfurt 60323, Germany (e-mail: 13deepikasaxena@gmail.com).

Chung-Nan Lee is with the Department of Computer Science and Engineering, National Sun Yat-sen University, Kaohsiung 804, Taiwan (e-mail: cnlee@cse.nsysu.edu.tw).

Digital Object Identifier 10.1109/LWC.2023.3259942

with least latency and the latter intends minimize operational cost by maximizing bandwidth utilization. In this context, a novel Traffic Management model for 6G Cloud Radio Access Network (TM-CRN) is proposed that examines the heterogeneous RAN traffic for probable network congestion and filters the contention-suspected traffic from the normal traffic to facilitate appropriate management. Firstly, the RAN traffic is estimated and analysed proactively for classification of live job requests into distinct traffic states. Thereafter, cloud-based traffic management is employed which triggers the allocation of job requests confined to various traffic states according to their criticality and resource requirement such that job execution latency is minimized and resource (viz., CPU, memory, and bandwidth) is maximized. The key contributions are: (i) A RAN traffic analyser is introduced that estimates the respective traffic proactively to detect and mitigate the probable congestion while reserving sufficient capacity of physical resources. (ii) A novel approach of RAN traffic states classification, is determined for resource allocation, scheduling, and mapping accordingly. (iii) TM-CRN model is implemented and the results are verified against QoS metrics, and compared with state-of-the-art approaches.

# <span id="page-0-3"></span>II. TM-CRN MODEL

<span id="page-0-2"></span>Consider a wireless telecommunications environment such as Open-RAN, GSM-RAN or C-RAN [3] composed of antennas, radios, and baseband units (BBU)s:  $\{RAN_1, RAN_2, \dots, RAN_n\} \in \mathbb{RAN}$  producing heterogeneous network traffic  $\{Nt_1, Nt_2, \dots, Nt_M\} \in \mathbb{NT}$  as illustrated in Fig. 1. In C-RAN, BBU devices convert digital signals into radio transmissions and vice-versa, are acting as a centralized control and processing station which are connected to remotely located Radio Frequency Units (RFU, the broadcasting antenna of a base station) via high speed optical fiber. The traffic includes job requests varying over execution time and resource demands such as bandwidth (BW), CPU (C), and memory (Mem), are transferred to cloud platform or BBU for different purposes including computation, storage, data sharing, etc., via RAN-Cloud Interface Layer. The cloud platform consists of three co-operative operational units, including RAN Traffic Analyser Unit (RTAU), Traffic Management Unit (TMU), and Cloud Services Unit (CSU). The radio network traffic  $(\mathbb{NT})$  is passed to RTAU for probable traffic congestion identification and estimation using the knowledge generated by AI-driven RAN Traffic Predictor, i.e.,  $\{Pt_1, Pt_2, \dots, Pt_M\}$  and pre-estimated threshold of traffic deviation. Accordingly, the estimated traffic outcome is transferred to RAN Traffic Congestion Handling Mechanism

<span id="page-0-0"></span><sup>&</sup>lt;sup>1</sup>https://www.factmr.com/report/cloud-radio-access-network-market

![](_page_1_Figure_2.jpeg)

<span id="page-1-0"></span>Fig. 1. TM-CRN Architectural Design.

which triggers the essential operations to manage it as depicted in TMU block. Within TMU, NT is segregated into distinct traffic states such as Fast jobs, Stragglers, Network Hogs, and Heavy jobs, etc., depending up on the amount of execution time and bandwidth consumption. The most appropriate single or multiple scheduling and mapping strategies for the live job requests are decided among the Z resource allocation strategies, and applied as per the fulfilment of essential resource availability and latency criteria. Further, TMU explores the selected resource allocation strategies for parallel execution to minimize the resource wastage, execution time and reduce CPU idle time. Correspondingly, the job requests are executed by CSU comprising of *Storage*, *Computing*, and Networking services. The cloud service execution information like, resource (C, BW, Mem) usage, number and type of job requests per time-interval is utilized to generate training data samples for the learning process of RAN traffic predictor. The operational description of RTAU and TMU with CSU is given in Sections III and IV, respectively.

## III. RAN TRAFFIC ANALYSIS

<span id="page-1-1"></span>As illustrated in Fig. 1, RTAU analyses approaching traffic using RAN traffic predictor (RTP) which is based on the AI-driven Extreme-Gradient Boosting (XGB) algorithm. This predictor is capable of learning and developing the intuitive and precise correlations among extracted samples or patterns. Let the RTP is composed of  $\ell$  base learners, i.e., decision trees  $\mathcal{BL}^* = \{\mathcal{BL}_1^*, \mathcal{BL}_2^*, \dots, \mathcal{BL}_\ell^*\}$  which estimate  $\ell$  respective outcomes  $\mathcal{O}^* = \{\mathcal{O}_1^*, \mathcal{O}_2^*, \dots, \mathcal{O}_\ell^*\}$  using Eq. (1);

<span id="page-1-2"></span>
$$O^* = \sum_{z=1}^{l} \mathcal{B} \mathcal{L}_z^*(\mathcal{F}_i) \quad \forall i \in \{1, 2, \dots, s\}$$
 (1)

where  $\mathcal{F}$  represents the input vector of size s, representing s training attributes (such as bandwidth, memory, processing usage samples) for traffic prediction. During each iteration, decision trees are trained incrementally to reduce prediction errors and the amount of error reduction is computed as gain or  $loss\ term\ (L(\mathcal{O}^*,\mathcal{O}^{**}_{t-1}+\mathcal{BL}^*_t(\mathcal{F}_i)))$ . Concurrently, a  $regularisation\ term\ (\Psi(\mathcal{BL}^*_t))$  is computed at each iteration to measure the complexity of decision trees and control their pruning in optimized way while preventing overfitting. Accordingly, the objective function L composed of loss term and regularisation term is minimized using Eq. (2).

<span id="page-1-3"></span>
$$L_{t} = \sum_{i=1}^{s} L(\mathcal{O}^{*}, \mathcal{O}_{t-1}^{**} + \mathcal{B}\mathcal{L}_{t}^{*}(\mathcal{F}_{i})) + \sum_{z=1}^{l} \Psi(\mathcal{B}\mathcal{L}_{z}^{*})$$
(2)

The term  $\Psi(\mathcal{BL}_t^*)$  is calculated using Eq. (3), where  $\gamma$  and  $\lambda$  are  $L_1$  and  $L_2$  regularisation coefficients, respectively, w is internal split tree weight and K is number of leaves in tree.

<span id="page-1-4"></span>
$$\Psi(\mathcal{B}\mathcal{L}_t^*) = \gamma K + \frac{1}{2}\lambda||w||^2 \tag{3}$$

Thereafter, adaptive boosting or optimization is applied using Taylor expansion which calculates exact loss for each decision tree by transforming Eq. (2) into Eq. (4);

<span id="page-1-5"></span>
$$L_t = \sum_{i=1}^{s^*} \left[ g_i \mathcal{B} \mathcal{L}_t^* (\mathcal{F}_i) + \frac{1}{2} h_i \mathcal{B} \mathcal{L}_t^{*2} (\mathcal{F}_i) \right] + \Psi(\mathcal{B} \mathcal{L}_t^*) \tag{4}$$

where  $g_i = \partial_{\mathcal{O}_{t-1}^{**}} L(\mathcal{O}^*, \mathcal{O}_{t-1}^{**})$ , and  $h_i = \partial_{\mathcal{O}_{t-1}^{**}}^2 L(\mathcal{O}^*, \mathcal{O}_{t-1}^{**})$  are the first and second order derivatives of loss function in the gradient, respectively (more details about XGBoost can be found in [4]). During each time-interval  $\{t_a, t_b\} \in t$ , a < b, live traffic values are provided as input to RTP for traffic prediction in the next time interval  $\{t_{a+1}, t_{b+1}\} \in t$ , a < b.

<span id="page-1-8"></span>Let  $\mathcal{T}r_{\sigma}$  be the deviation of network traffic from the predicted traffic (Pt) over duration  $\Delta t \in \{t_a, t_b\}$ ,  $\mathcal{T}r_{\sigma}^{thr}$  and  $\Delta t^{thr}$  are traffic deviation and time-period thresholds respectively. Eq. (5) investigates traffic status  $(\Xi^{status})$  for duration  $(\Delta t)$  based on the comparison between expected traffic deviation  $(\mathcal{T}r_{\sigma})$  and threshold  $(\mathcal{T}r_{\sigma}^{thr})$ .

<span id="page-1-6"></span>
$$\Xi^{status} \times \Delta t = \begin{cases} 1, & \text{If} (\mathcal{T}_{r\sigma} \times \Delta t > \mathcal{T}_{r\sigma}^{thr} \times \Delta t^{thr}) \\ -1, & \text{If} (\mathcal{T}_{r\sigma} \times \Delta t < 0) \\ 0, & \text{Otherwise} \end{cases}$$
(5)

Accordingly, the traffic status  $\Xi^{status}$  value '1' indicates 'network congestion', '-1' specifies 'sub-normal traffic', and 'normal traffic', otherwise. Further, the critical and sufficient condition for the congestion is formulated and defined in Eq. (6) subject to four constraints  $(C_1-C_4)$  over time  $(\Delta t)$ ;

<span id="page-1-7"></span>
$$\int_{t_{a}}^{t_{b}} \left( \sum_{i=1}^{M} Pt_{i} + \sum_{i=1}^{M} \mathcal{T}r_{\sigma i} \right) dt \leq \int_{t_{a}}^{t_{b}} \sum_{i=1}^{M} \left( Nt_{i} \right) dt$$

$$s.t. \quad \forall C_{1} \bigvee \exists \{C_{2}, C_{3}, C_{4}\} \\
C_{1} : \quad t_{b} - t_{a} = \Delta t > \mathcal{T}r_{\sigma} \times \Delta t^{thr} )$$

$$C_{2} : \quad \sum_{i=1}^{M} Nt_{i}^{BW} \geq \sum_{k=1}^{P} PM_{k}^{BW} \\
C_{3} : \quad \sum_{i=1}^{M} Nt_{i}^{C} \geq \sum_{k=1}^{P} PM_{k}^{C} \\
C_{4} : \quad \sum_{i=1}^{M} Nt_{i}^{Mem} \geq \sum_{k=1}^{P} PM_{k}^{Mem}$$

$$(6)$$

where  $Nt_i^{BW}$ ,  $Nt_i^C$ , and  $Nt_i^{Mem}$  specify capacity demand of bandwidth, CPU, and memory, respectively, of the live traffic (Nt). If the aggregated demand of the entire traffic  $(\sum_{i=1}^{M} Nt_i)$  is greater than estimated resource requirement  $(\sum_{i=1}^{M} Pt_i + \sum_{i=1}^{M} Tr_{\sigma i})$ , then congestion is detected.  $C_1$  states traffic overflow  $(T_{\sigma})$  for longer than threshold timeperiod  $(\Delta t^{thr})$ ;  $C_2 - C_4$  state excess demand of resources viz., BW, C, Mem of the live traffic than the available aggregated capacity of resources on P physical machines (PM). If congestion is anticipated, the network traffic is diverted across multiple pathways and assigned to physical machines reserved for handling the network hogs and heavy workloads. Likewise, if the approaching traffic is sub-normal ( $\Xi^{status}$ = -1), the respective job requests are executed on least number of physical machines subject to resource availability constraints; otherwise, the traffic is normal which is handled by TMU. The traffic handling and management by TMU is discussed in the following Section IV.

## IV. CLOUD-BASED TRAFFIC MANAGEMENT

<span id="page-2-0"></span>The RAN traffic analysis and computation information is transferred to TMU to allow estimation of the distinguished traffic states, including Light jobs  $(\mathcal{T}r^{Lit})$ , Stragglers  $(\mathcal{T}r^{Stg})$ , Network Hogs  $(\mathcal{T}r^{Hog})$ , Heavy jobs  $(\mathcal{T}r^{Hvy})$ , and Average jobs  $(\mathcal{T}r^{Avg})$  etc. Eq. (7) determines various states of live RAN traffic  $\{Nt_1, Nt_2, \ldots, Nt_M\}$  at  $t^{th}$  instance by considering different circumstances of the bandwidth demand  $(Nt_i^{BW}: i \in \{1, M\})$  and execution time  $(Nt_i^{Et})$ .

<span id="page-2-1"></span>
$$Nt_{i}^{State} = \begin{cases} \mathcal{T}^{Lit}(1), & \text{If}(Nt_{i}^{BW} < BW_{i}^{thr} & \&\& & Nt_{i}^{Et} < Et_{i}^{thr}) \\ \mathcal{T}^{Stg}(2), & \text{If}(Nt_{i}^{BW} \leq BW_{i}^{thr} & \&\& & Nt_{i}^{Et} \geq Et_{i}^{thr}) \\ \mathcal{T}^{Hog}(3), & \text{If}(Nt_{i}^{BW} \geq BW_{i}^{thr} & \&\& & Nt_{i}^{Et} \leq Et_{i}^{thr}) \\ \mathcal{T}^{Hvy}(4), & \text{If}(Nt_{i}^{BW} \geq BW_{i}^{thr} & \&\& & Nt_{i}^{Et} \geq Et_{i}^{thr}) \\ \mathcal{T}^{Avg}(5) & \text{Otherwise} \end{cases}$$

TMU schedules job requests (Jr) belonging to distinct traffic states exclusively in the most admissible way to minimize latency of execution and maximize the resource (BW, C, Mem) utilization as stated in Eqs. (8)-(12) subject to constraints  $\{C_1 - C_6\}$  specified in Eq. (13). The expression  $\omega_{kii}$  represents mapping among  $k^{th}$  job  $(Jr_k : k \in M)$ ,  $j^{th}$  virtual node  $(VN_j : j \in Q)$ , and  $i^{th}$  physical machine  $(PM_i : i \in P)$ ; R and  $R^*$  are resource capacity of virtual node and physical machine, respectively. The constraint  $C_1$  specifies  $k^{th}$  job can be assigned to only one  $VN_i$  hosted on one  $PM_i$  at an instance;  $\{C_2 - C_4\}$  state resource capacity of  $VN_i$  must be lesser or equal to available resource capacity of  $PM_i$ ; and  $C_5$  &  $C_6$  specify resource requirement of  $k^{th}$  job  $(Jr_k)$  for processing must be satisfied by the available resources on the respective  $VN_i$  hosted on  $PM_i$ . The job requests confined to light traffic state  $(\mathcal{T}^{Lit})$  are allocated to virtual nodes (VN)hosted on physical machines with required resource capacity using first-come first-serve (FCFS) scheduling (Eq. (8)).

<span id="page-2-2"></span>
$$\omega_{kji}^{q_rLit} = Jr_k^{q_rLit} \times VN_j^R \times List_{(FCFS)}PM_i^{R^*}$$
 (8)

$$\omega_{kji}^{T_{i}^{Stg}} = Jr_{k}^{T_{i}^{Stg}} \times VN_{j}^{R} \times MAX(ListPM_{i}^{R^{*}})$$
(9)

$$\omega_{kji}^{q_T Hog} = Jr_k^{q_T Hog} \times VN_j^R \times MAX(List_{BW} PM_i^{R^*})$$
 (10)

$$\omega_{kji}^{T^{Hvy}} = Jr_k^{T^{Hvy}} \times \sum_{i=1}^{Z} VN_j^R \times \sum_{i=1}^{Z^*} PM_i^{R^*}$$
(11)

# <span id="page-2-3"></span>**Algorithm 1:** TM-CRN: Operational Summary

- 1 **Input** Number of: PMs (P), VNs (Q), RANs (M);
- 2 Initialize:  $List_{Jr}$ ,  $List_{VN}$ ,  $List_{PM}$ ;
- 3 Distribute initial RAN traffic:  $\{Nt_1, Nt_2, \dots, Nt_M\}$  on VNs hosted at P PMs;
- 4 for each time-interval  $\{t_a, t_b\}$  do
- 5 Estimate traffic load:  $Pt_{t+1}$ = RAN Traffic Predictor( $NT_{t_a}$ );
- Receive heterogeneous RAN traffic  $(NT_{t_a+1})$  and compute traffic deviation  $(T_{\sigma})$ ;
- Analyse the status of the traffic  $(\Xi)$  using Eq. (5);
- 8 Investigate the exact occurrence of a RAN traffic congestion by applying Eq. (6);
- 9 Determine and distinguish among different traffic states using Eq. (7);
- Apply Eqs. (8)-(12) to decide allocation of job requests in the most appropriate manner;

11 end

$$\omega_{kji}^{T^{Avg}} = Jr_k^{T^{Avg}} \times VN_j^R \times MAX(List_C PM_i^{R^*})$$
(12) subject to  $\{C_1 - C_6\}$ 

$$C_1: \forall_{k \in M} \forall_{j \in Q} \forall_{i \in P} \omega_{kji} = 1$$

$$C_2: \forall_{k \in M} \forall_{j \in Q} \forall_{i \in P} VN_j^C \times \omega_{kji} \leq PM_i^{C^*}$$

$$C_3: \forall_{k \in M} \forall_{j \in Q} \forall_{i \in P} VN_j^M \times \omega_{kji} \leq PM_i^{M^*}$$

$$C_4: \forall_{k \in BW} \forall_{j \in Q} \forall_{i \in P} VN_j^{BW} \times \omega_{kji} \leq PM_i^{BW^*}$$

$$C_5: \sum_{k \in M} R_k \leq \sum_{i \in P} PM_i^{R^*} \quad R^* \in \{C^*, M^*, BW^*\}$$

$$C_6: r_k \times R_k \leq VN_j^{R^*} \quad \forall_k \in [1, M], j \in [1, Q]$$

$$(13)$$

Likewise, the stragglers  $(\mathcal{T}r^{Stg})$  requiring higher computational capacity are assigned to virtual nodes hosted on a physical machine with larger CPU, bandwidth, and memory capacity to allow needed I/O operations (Eq. (9)). Further, a hybrid scheduling is introduced to allow parallel execution of stragglers with network hogs  $(Tr^{Hog})$  such that the bandwidth hogs can be processed by the computing and network devices having sufficient resource capacity that can serve the requirement during idle time when the stragglers are performing I/O operations (Eq. (10)). The 'Heavy jobs'  $(\mathcal{T}r^{Hvy})$  demanding resource capacity larger than the threshold are bound to execute on multiple physical machines with highest resource capacity which can altogether serve resource demand of the respective traffic (Eq. (11)). All the remaining job requests are considered as 'average' and 'delay-sensitive' to be scheduled on the remaining physical nodes to allow faster execution. Specifically, the average jobs  $(\mathcal{T}r^{Avg})$  based requests are sorted as per the basis of their deadlines and priorities, and the physical nodes are assorted in decreasing order of their processing speed in the list (Eq. (12)). Such an allocation of virtual nodes executes lowest deadline requests on highest processing speed servers to minimize the time of execution.

#### V. OPERATIONAL DESIGN AND COMPLEXITY

Algorithm 1 imparts the operational summary of TM-CRN for effective traffic management for cloud-based RAN.

Step 1 allows to read the number of PMs, VNs, and RANs' job requests from users, consumes  $\mathcal{O}(1)$  complexity while

step 2 initializes lists of jobs, VNs, and PMs, has  $\mathcal{O}(1)$  complexity. Step 3 schedules M network requests onto P PMs, with  $\mathcal{O}(P \times M)$  complexity. Assuming steps 4-11 repeat for t time intervals, wherein step 5 calls RAN traffic predictor  $T \mapsto \mathcal{O}(thzlogn)$  where t is the number of trees, h is the height of the trees, z is the number of non-missing entries in the training, and n is the number of examples. The prediction for a new sample consumes time  $\mathcal{O}(th)$ . Steps 6-10 compute Eqs. (7)-(12) consume  $\mathcal{O}(1)$  complexity. Hence, the total complexity comes out to be  $\mathcal{O}(PMT)$ .

#### VI. PERFORMANCE EVALUATION AND DISCUSSION

## A. Experimental Set-Up and Dataset

The simulation experiments are executed on a server machine assembled with two Intel Xeon Silver 4114 CPU with 40 core processor and 2.20 GHz clock speed, deployed with 64-bit Ubuntu 16.04 LTS having main memory of 128 GB in Python 3.1. The CDC environment is set up with CoS [5] having IBM servers' CPU (MIPS), RAM (GB) and bandwidth (bps) configurations: {1060, 2, 2000}; {2660, 4, 2000}; {3067, 8, 4000}; {4076, 64, 8000}. Four types of VMs inspired from Amazon VM instances with CPU, RAM, and bandwidth: {500, 1, 500}; {1000, 2, 1000}; {2000, 3, 1000}; {2500, 4, 2000} are used. We experimented with a wireless traffic data sets of call detail records [6] and a C-RAN traffic gathered from Youtube dataset on Mobile streaming [7] containing records of 80 RAN scenarios having 171 bandwidth settings, measured in 1,939 runs with emulated 3G/4G traces.

<span id="page-3-4"></span>TM-CRN is compared with Federated Meta-Learning Approach (FMLA) based wireless traffic prediction [8], Joint UE and Fog Optimization (JUFO) scheme [2], and Online Secure Communication Model Cloud (OSC-MC) [9] for different performance metrics. A wireless traffic prediction approach, FMLA is proposed in [8] to manage the highly dynamic and low latency wireless communication networks by learning a sensitive global model with knowledge gathered from diverse regions. A minimized energy computation derived tasks offloading and C-RAN traffic management scheme is presented in [2], wherein cloud tasks priority is investigated to allow the task execution within the determined delay bound. OSC-MC model [9] prevents network traffic congestion and minimize occurrence of network hogs by computing the traffic deviation proactively while maintaining secure workload execution.

#### B. Numerical Results

Table I reports resultant values obtained for the key performance metrics for TM-CRN with varying bandwidth  $(BW^{thr})$  and execution-time  $(Et^{thr})$  threshold values (including 25%, 50%, 75%, and 90% of the respective quantitative values) for 500 C-RAN jobs over progressive time-period. By applying Eq. (7), traffic is filtered into different traffic states such that for  $BW^{thr}$ =25% and  $\mathcal{T}^{Lit}$  (%) and  $\mathcal{T}^{Hog}$ (%) increase, while  $\mathcal{T}^{Stg}$ (%) and  $\mathcal{T}^{Hvy}$ (%) decrease with increasing execution time consumption  $(Et^{thr})$  and the similar trend is followed for rest of the  $BW^{thr}$  values. Furthermore, with growing  $BW^{thr}$ , the traffic states  $\mathcal{T}^{Lit}$  (%) and  $\mathcal{T}^{Hvy}$ (%) show reduction, and  $\mathcal{T}^{Hog}$ (%) and  $\mathcal{T}^{Stg}$ (%)

TABLE I
KEY PERFORMANCE INDICATORS FOR TM-CRN

<span id="page-3-0"></span>

| $BW^{thr}$ | $Et^{thr}$ | $Tr^{Lit}$ | $Tr^{Stg}$ | $Tr^{Hog}$ | $Tr^{Hvy}$ | $BW^{Util}$ | $Et^{Cons} \times 10^4$ | $\mathcal{L}t^{Redc}$ |
|------------|------------|------------|------------|------------|------------|-------------|-------------------------|-----------------------|
| (%)        | (%)        | (%)        | (%)        | (%)        | (%)        | (%)         | (sec)                   | (%)                   |
| 25         | 25         | 11.4       | 24.12      | 11.41      | 53.07      | 19.51       | 18.72                   | 23.80                 |
| 25         | 50         | 41.67      | 05.70      | 29.82      | 22.81      | 17.85       | 22.02                   | 10.43                 |
| 25         | 75         | 56.58      | 01.32      | 34.21      | 07.90      | 20.75       | 23.06                   | 6.17                  |
| 25         | 90         | 64.48      | 0.00       | 35.52      | 0.00       | 22.46       | 24.58                   | 0.00                  |
| 50         | 25         | 7.89       | 44.29      | 14.91      | 32.89      | 25.03       | 14.22                   | 42.10                 |
| 50         | 50         | 24.12      | 11.84      | 47.37      | 16.67      | 26.16       | 20.06                   | 18.37                 |
| 50         | 75         | 33.77      | 02.19      | 57.02      | 07.02      | 26.11       | 22.41                   | 8.80                  |
| 50         | 90         | 33.77      | 01.75      | 57.46      | 07.01      | 26.11       | 22.59                   | 8.08                  |
| 75         | 25         | 5.70       | 57.46      | 17.10      | 19.74      | 28.54       | 09.30                   | 62.12                 |
| 75         | 50         | 14.03      | 17.54      | 57.46      | 10.97      | 27.82       | 16.47                   | 32.97                 |
| 75         | 75         | 20.61      | 04.83      | 70.18      | 04.38      | 29.07       | 19.48                   | 20.73                 |
| 75         | 90         | 25.00      | 0.00       | 75.00      | 0.00       | 28.82       | 24.58                   | -0.02                 |
| 90         | 25         | 01.75      | 67.11      | 21.05      | 10.08      | 18.26       | 06.02                   | 75.52                 |
| 90         | 50         | 06.14      | 22.80      | 65.35      | 05.70      | 25.89       | 13.90                   | 43.42                 |
| 90         | 75         | 09.21      | 06.58      | 81.57      | 02.63      | 24.64       | 17.73                   | 27.84                 |
| 90         | 90         | 09.21      | 06.14      | 82.01      | 02.63      | 24.57       | 17.91                   | 27.12                 |

TABLE II XGBOOST-BASED PREDICTION PERFORMANCE METRICS

<span id="page-3-1"></span>

| PWS (                | min) MSE    | MAE        | HE     |         |        |
|----------------------|-------------|------------|--------|---------|--------|
| 5                    | 0.0038      | 0.0547     | 28.89  |         |        |
| 10                   | 0.0047      | 0.0857     | 24.09  |         |        |
| 30                   | 0.0056      | 0.0860.2   | 21.64  |         |        |
| 60                   | 30.0078     | 0.1055     | 19.95  |         |        |
| PWS: Prediction wind | ow size, TT | E: trainin | g time | elapsed | (msec) |

<span id="page-3-5"></span><span id="page-3-3"></span>![](_page_3_Figure_13.jpeg)

<span id="page-3-7"></span><span id="page-3-6"></span><span id="page-3-2"></span>Fig. 2. Traffic estimation error.

upgrade. The bandwidth utilization  $(BW^{Util} \%)$  is achieved in the range [16% - 30%] and the jobs' execution time (Et) varies with their size and processing speed of cloud servers. However, the significant reduction in overall job execution latency  $(\mathcal{L}t^{Redc})$  is observed for TM-CRN as compared to the default traffic execution (using first-come first-serve (FCFS) scheduling). The reason is that TM-CRN efficiently exploits the possible parallelism between jobs confined to  $\mathcal{T}r^{Hog}$  and  $\mathcal{T}r^{Stg}$ .

Table II reports the performance of the XGBoost-based prediction model, where the achieved mean squared error (MSE) and mean absolute error (MAE) vary in the ranges: [0.0033-0.0080] and [0.05-0.11], respectively (Appendix provides more prediction results using Google Cluster Dataset to further validate the XGBoost's performance). The prediction error increases and training time elapsed (TTE) decreases with the size of the prediction interval because of decreased number of data samples. Further, the achieved traffic estimation errors: MSE and MAE are compared against different versions of FMLA [8] including standard network (FMLA-s), wide network (FMLA-w), deep network (FMLA-d), and Optimal case (prediction error is zero) as depicted in Fig. 2. MAE and MSE obtained for Milan (viz.,  $Mi^{MAE}$  and  $Mi^{MSE}$ ) are lesser for both the proposed and FMLA, however, significant reduction in error of 90.8% is observed for Trentino in case of

![](_page_4_Figure_2.jpeg)

<span id="page-4-9"></span>Fig. 3. Traffic congestion.

![](_page_4_Figure_4.jpeg)

<span id="page-4-10"></span>Fig. 4. Network bandwidth utilization.

TM-CRN over FMLA-d because of intuitive pattern learning and optimization of extreme gradient boosting approach.

Fig. 3 compares TM-CRN with OSC-MC [9] and Optimal case for occurrence of C-RAN traffic congestion using Youtube mobile streaming dataset. TM-CRN reduces the congestion up to 10.15% over OSC-MC due to engagement of improved prediction capability and effective distribution and management of the live traffic into distinct traffic states. TM-CRN is closer to Optimal for  $Tr_{25\%}^{25\%}$ ,  $Tr_{50\%}^{50\%}$  and show 2%-9% more congestion as compared with remaining cases of traffic thresholds.

Fig. 4 compares the network bandwidth utilization percent of TM-CRN with Optimal case, JUFO [2] and baseline methods: random-fit and first-fit over varying thresholds for both  $BW^{thr}$  and  $Et^{thr}$  viz., 5%, 25%, 75%, and 90% during experiments. The bandwidth utilization has improved by 17.07%, 17.31%, and 18% over JUFO, random-fit, and first-fit, respectively and reduced by 2.7% over Optimal case for  $BW^{thr} = Et^{thr} = 75\%$  because of the division of the jobs according to their bandwidth and execution time requirement into distinct traffic states followed by the privileged management accordingly that accelerates the optimization of C-RAN jobs allocation and execution.

The comparison of execution time consumed is shown in Fig. 5, the proposed approach of C-RAN traffic management consumes 19.33%, 26.90%, and 27.12% lesser time over JUFO, random-fit, and first-fit, respectively. Accordingly, the job execution latency for TM-CRN management is reduced by 23.80%, 18.37%, 20.73%, and 27.12% for the  $BW^{thr}$  and  $Et^{thr}$  values: 25%, 50%, 75%, and 90%, respectively over default FCFS scheduling-based traffic management. On the other hand, the job latency has been reduced up to 1.22%, 10.68%, and 2.74% for JUFO. However, the time elapsed for

![](_page_4_Figure_10.jpeg)

<span id="page-4-11"></span>Fig. 5. Service execution time.

TM-CRN over Optimal case is higher up to 33.5%-51.27% because of the intended traffic prediction and analysis in case of TM-CRN which is avoided for Optimal case. The significant time reduction is achieved for the proposed approach due to the traffic classification into distinct states, and incorporation and exploitation of parallelism by executing hogs having higher bandwidth and lesser execution time requirement in-between stragglers (slow executing jobs).

## VII. CONCLUSION

A novel TM-CRN model is proposed to facilitate effective RAN traffic management with minimum latency period and maximum bandwidth utilization. The probable resource demand and traffic congestion is detected using XGBoost predictor. Traffic management unit classifies that traffic into distinct states to utilize available bandwidth productively for parallel execution of RAN traffic confined to stragglers and network hogs. The performance evaluation and comparison confirmed that TM-CRN model is more admissible as compared with state-of-the-art approaches.

# REFERENCES

- <span id="page-4-0"></span> Z. Zhao, C. Feng, H. H. Yang, and X. Luo, "Federated-learning-enabled intelligent fog radio access networks: Fundamental theory, key techniques, and future trends," *IEEE Wireless Commun.*, vol. 27, no. 2, pp. 22–28, Apr. 2020.
- <span id="page-4-1"></span>[2] J. Kim, T. Ha, W. Yoo, and J.-M. Chung, "Task popularity-based energy minimized computation offloading for fog computing wireless networks," *IEEE Wireless Commun. Lett.*, vol. 8, no. 4, pp. 1200–1203, Aug. 2019.
- <span id="page-4-2"></span>[3] M. A. Habibi, M. Nasimi, B. Han, and H. D. Schotten, "A comprehensive survey of RAN architectures toward 5G mobile communication system," *IEEE Access*, vol. 7, pp. 70371–70421, 2019.
- <span id="page-4-3"></span>[4] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Mining, 2016, pp. 785–794.
- <span id="page-4-4"></span>[5] D. Saxena, I. Gupta, A. K. Singh, and C.-N. Lee, "A fault tolerant elastic resource management framework toward high availability of cloud services," *IEEE Trans. Netw. Service Manag.*, vol. 19, no. 3, pp. 3048–3061, Sep. 2022.
- <span id="page-4-5"></span>[6] G. Barlacchi et al., "A multi-source dataset of urban life in the city of milan and the province of Trentino," Sci. Data, vol. 2, no. 1, pp. 1–15, 2015.
- <span id="page-4-6"></span>[7] F. Loh, F. Wamser, F. Poignée, S. Geißler, and T. Hoßfeld. "YouTube dataset on mobile streaming for Internet traffic modeling, network management, and streaming analysis, figshare, dataset." 2022. [Online]. Available: https://doi.org/10.6084/m9.figshare.19096823.v2
- <span id="page-4-7"></span>[8] L. Zhang, C. Zhang, and B. Shihada, "Efficient wireless traffic prediction at the edge: A federated meta-learning approach," *IEEE Commun. Lett.*, vol. 26, no. 7, pp. 1573–1577, Jul. 2022.
- <span id="page-4-8"></span>[9] D. Saxena and A. K. Singh, "OSC-MC: Online secure communication model for cloud environment," *IEEE Commun. Lett.*, vol. 25, no. 9, pp. 2844–2848, Sep. 2021.
# Client Selection and Cost-Efficient Joint Optimization for NOMA-Enabled Hierarchical Federated Learning

Bibo Wu [,](https://orcid.org/0009-0002-3918-2510) *Graduate Student Member, IEEE*, Fang Fang [,](https://orcid.org/0000-0002-6582-6570) *Senior Member, IEEE*, Xianbin Wang [,](https://orcid.org/0000-0003-4890-0748) *Fellow, IEEE*, Donghong Cai [,](https://orcid.org/0000-0001-5350-135X) *Member, IEEE*, Shu F[u](https://orcid.org/0000-0002-7988-9724) , *Member, IEEE*, and Zhiguo Ding [,](https://orcid.org/0000-0001-5280-384X) *Fellow, IEEE*

*Abstract*— Hierarchical federated learning (HFL) shows great advantages over conventional two-layer federated learning (FL) in reducing network overhead and interaction latency while still retaining the data privacy of distributed FL clients. However, the communication and energy overhead still pose a bottleneck for HFL performance, especially as the number of clients raises dramatically. To tackle this issue, we propose a non-orthogonal multiple access (NOMA) enabled HFL system under semi-synchronous cloud model aggregation in this paper, aiming to minimize the total cost of time and energy at each HFL global round. Specifically, we first propose a novel fuzzy logic based client selection policy considering client heterogeneity in multiple aspects, including channel quality, data quantity and model staleness. Subsequently, given the fuzzy based clientedge association, a joint edge server scheduling and resource allocation problem is formulated. Utilizing problem decomposition, we firstly derive the closed-form solution for the edge server scheduling subproblem via the penalty dual decomposition (PDD) method. Next, a deep deterministic policy gradient (DDPG) based algorithm is proposed to tackle the resource allocation subproblem considering time-varying environments. Finally, extensive simulations demonstrate that the proposed scheme outperforms the considered benchmarks regarding HFL performance improvement and total cost reduction.

*Index Terms*— Client selection, deep reinforcement learning, hierarchical federated learning, NOMA, resource allocation.

Manuscript received 24 October 2023; revised 15 April 2024; accepted 30 May 2024. Date of publication 18 June 2024; date of current version 11 October 2024. The work of Donghong Cai was supported in part by the Science and Technology Major Project of Tibetan Autonomous Region of China under Grant XZ202201ZD0006G02 and in part by the Basic and Applied Basic Research Foundation of Guangdong Province under Grant 2024A1515012398. The work of Shu Fu was supported by the Natural Science Foundation of Chongqing, China, under Grant CSTB2023NSCQ-LZX0108. The associate editor coordinating the review of this article and approving it for publication was X. Cao. *(Corresponding author: Donghong Cai.)*

Bibo Wu and Xianbin Wang are with the Department of Electrical and Computer Engineering, Western University, London, ON N6A 3K7, Canada (e-mail: bwu293@uwo.ca; xianbin.wang@uwo.ca).

Fang Fang is with the Department of Electrical and Computer Engineering and the Department of Computer Science, Western University, London, ON N6A 3K7, Canada (e-mail: fang.fang@uwo.ca).

Donghong Cai is with the College of Cyber Security, Jinan University, Guangzhou 510632, China (e-mail: dhcai@jnu.edu.cn).

Shu Fu is with the Department of Microelectronics and Communication Engineering, Chongqing University, Chongqing 400044, China (e-mail: shufu@cqu.edu.cn).

Zhiguo Ding is with the Department of Computer and Information Engineering, Khalifa University, Abu Dhabi, United Arab Emirates (e-mail: zhiguo.ding@ieee.org).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TWC.2024.3411479.

Digital Object Identifier 10.1109/TWC.2024.3411479

#### I. INTRODUCTION

<span id="page-0-1"></span><span id="page-0-0"></span>T HE burgeoning Internet of Things (IoT) has greatly increased the number of intelligent devices and applications, which leads to the humongous amount of data traffic. To this end, machine learning (ML) becomes necessary due to its great potential in dealing with the extensive amount of data [\[1\]. In](#page-13-0) general, the traditional ML models are trained using a centralized way, which requires a central server to assemble the distributed raw data of users for model training [\[2\]. T](#page-13-1)his centralized paradigm inevitably raises the data privacy concern for users. In response, a decentralized ML framework called federated learning (FL) was proposed by Google and has been investigated extensively for the past few years [\[3\]. Un](#page-13-2)der the framework of FL, the edge entities, termed clients, are allowed to train a global model collaboratively with local trained model parameters rather than their local private data. As a direct benefit, the global FL model can be well trained while preserving the data privacy.

<span id="page-0-5"></span><span id="page-0-4"></span><span id="page-0-3"></span><span id="page-0-2"></span>The implementation of conventional FL normally based on the two-layer framework, which can be divided into two classes, including the client-cloud FL [\[4\]](#page-13-3) and the client-edge FL [\[5\]. H](#page-13-4)owever, the heavy communication overhead and the inferior FL performance are the two major drawbacks for these two types of FL, respectively. For the former, the local models are trained at clients, and a remote cloud server conducts the model aggregation. Considering the wide service coverage of the cloud server, this architecture can engage numerous clients in model training. Nevertheless, the unbearable high transmitting delay and the limited FL performance due to heavy burden of the cloud server become two critical challenges and needed to be addressed. Assisted by mobile edge computing (MEC), the client-edge FL was proposed, where the edge servers are responsible for model aggregation. This framework achieves a significant reduction in transmission delay and the corresponding energy overhead. However, the number of selected clients is limited due to the reduced service coverage of the edge server, which inevitably degrades FL performance owing to insufficient training data. In response, the hierarchical federated learning (HFL) has been proposed recently, which exploits the client-edge-cloud three-layer structure to realize better performance [\[6\]. In](#page-13-5) HFL, each edge server plays the role of intermediate node which performs the edge model aggregation for local models uploaded by the clients in vicinity. Next, the aggregated edge models are transmitted by edge servers

1536-1276 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

to the cloud server for global model aggregation when the accuracy threshold for edge model training is satisfied. As a result, HFL significantly reduces the transmission latency and energy overhead between clients and the remote cloud server. Besides, the training performance can be guaranteed by the cloud server which is able to select sufficient clients via edge servers.

Nevertheless, the communication latency and energy overhead become the bottleneck for the further improvement of HFL performance as the number of clients raises. Given that the densely distributed clients normally can communicate with more than one edge server, the client selection, i.e., the association between clients and edge servers, plays a vital role in HFL systems. Through effective design of clientedge association, more efficient resource allocation among clients can be achieved, leading to improved client-edge communication and further reduction of HFL training time and energy overhead. Moreover, using non-orthogonal resourceefficient channel access is also helpful in enhancing HFL outcome by reducing access latency and increasing network throughput when communication resources become scarce. In particular, non-orthogonal multiple access (NOMA) [\[7\]](#page-13-6) allows multiple clients to transmit their local model parameters simultaneously on the same channel, which has been regarded as a significant enabler to enhance communication efficiency in HFL systems. Therefore, the investigation towards client selection and efficient resource allocation in HFL over NOMA networks deserves to be conducted.

#### *A. Related Literature*

In recent years, abundant of research has been conducted to improve the performance of two-layer FL and HFL.

<span id="page-1-12"></span><span id="page-1-11"></span><span id="page-1-10"></span><span id="page-1-9"></span><span id="page-1-8"></span><span id="page-1-5"></span><span id="page-1-4"></span><span id="page-1-3"></span><span id="page-1-2"></span>*1) Two-Layer FL Performance Improvement:* Considering the resource bottleneck in the two-layer FL systems, a variety of mechanisms have been proposed to improve FL performance in existing works, including model compression [\[8\],](#page-13-7) [\[9\], cl](#page-13-8)ient scheduling [\[10\],](#page-13-9) [\[11\],](#page-13-10) [\[12\],](#page-13-11) [\[13\],](#page-13-12) [\[14\]](#page-13-13) and resource allocation [\[15\],](#page-13-14) [\[16\],](#page-13-15) [\[17\],](#page-13-16) [\[18\],](#page-13-17) [\[19\]. S](#page-13-18)pecifically, the authors in [\[8\]](#page-13-7) applied network pruning to maximize the FL convergence rate, while the gradient compression method was utilized in [\[9\]](#page-13-8) to realize the tradeoff between FL convergence rate and latency. With the consideration of resource scarceness, client selection is crucial to improve FL performance. In [\[10\],](#page-13-9) a client selection policy based on probability was designed by minimizing the total communication time. The authors in [\[11\]](#page-13-10) considered an emerging criterion, i.e., model staleness, for client scheduling in FL systems, and proposed an age-based selecting policy to achieve better FL performance. The devicespecific participation rate was investigated in [\[12\]](#page-13-11) to achieve the minimization of training delay. In [\[13\], t](#page-13-12)he authors aimed to minimize the total energy cost while considering client heterogeneity of communication conditions, computing capabilities, and available data sets. Differently, [\[14\]](#page-13-13) proposed two client clustering approaches based on sample size and model similarity respectively. Resource allocation is also vital for the implementation of communication-efficient FL. To minimize the convergence time of FL, the joint resource allocation and client selection problem was formulated to optimize transmitting power [\[15\], c](#page-13-14)omputing frequency [\[16\]](#page-13-15) and uplink resource block [\[17\]. S](#page-13-16)ome other works paid attention to the minimization of global FL loss with efficient resource allocation [\[18\],](#page-13-17) [\[19\]. H](#page-13-18)owever, the aforementioned client selection and resource allocation strategies in the two-layer FL frameworks are not always effective in HFL systems since each client can be selected by multiple edge servers simultaneously. Besides, due to the long training latency and heavy energy overhead, conventional two-layer FL systems cannot meet the need from large-scale systems.

<span id="page-1-17"></span><span id="page-1-16"></span><span id="page-1-15"></span><span id="page-1-14"></span><span id="page-1-13"></span>*2) HFL Design and Analysis:* By taking advantage of the conventional two-layer FL, the HFL with the client-edge-cloud structure was proposed and studied extensively [\[20\],](#page-13-19) [\[21\],](#page-13-20) [\[22\],](#page-13-21) [\[23\],](#page-13-22) [\[24\]. S](#page-13-23)pecifically, considering the edge aggregation interval control, [\[20\]](#page-13-19) investigated the multi-objective optimization problem of global loss and training latency in a HFL system. Differently, the convergence bound for one HFL round was analyzed in [\[21\], a](#page-13-20)nd the joint resource allocation and edge server scheduling problem was investigated. In [\[22\]](#page-13-21) and [\[23\],](#page-13-22) the client-edge association scheme was carefully designed to achieve efficient resource allocation, while [\[23\]](#page-13-22) considered the heterogeneous data distribution among clients. The authors in [\[24\]](#page-13-23) took model quantization into account to analyze the HFL convergence bound, which was then applied to the design of edge and cloud model aggregation interval.

<span id="page-1-21"></span><span id="page-1-20"></span><span id="page-1-19"></span><span id="page-1-18"></span><span id="page-1-7"></span><span id="page-1-6"></span><span id="page-1-1"></span><span id="page-1-0"></span>To achieve a further improvement of training performance and communication efficiency, several promising technologies have been considered in HFL systems, including NOMA [\[25\],](#page-13-24) blockchain [\[26\]](#page-13-25) and deep reinforcement learning (DRL) [\[27\],](#page-13-26) [\[28\]. M](#page-13-27)ore specifically, [\[25\]](#page-13-24) applied NOMA in HFL systems and formulated a joint problem regarding client selection and resource allocation. Considering the willingness of clients to transmit their local models during HFL training, [\[26\]](#page-13-25) proposed a blockchain-based incentive scheme to achieve better performance. The rapid development of DRL makes the integration of DRL with HFL more prevalent. A twolayer deep Q-leaning based incentive mechanism was proposed in [\[27\]](#page-13-26) to motivate clients for aggregation, which contributes to the high-quality HFL model training. The authors in [\[28\]](#page-13-27) proposed a multi-agent deep deterministic policy gradient (DDPG) based algorithm to minimize the HFL global loss. Nevertheless, the aforementioned HFL works designed the client-edge association schemes only based on one single criterion, hence failing to balance the client heterogeneity in multiple aspects, which makes them unpractical in application. Besides, none of them considered the joint design of client selection, edge server scheduling and resource allocation, which is crucial to improve HFL performance.

## *B. Motivations and Contributions*

From above observations, HFL shows great superiority than traditional two-layer FL in reducing training latency and energy cost. Nevertheless, there is still a bottleneck of communication and energy overhead for the further improvement of HFL performance when deploying in large-scale systems. Intelligent client selection is one of the solutions to address this issue. However, the client-edge association schemes in the HFL literature only depend on a single criterion and fail to consider the client heterogeneity in multiple aspects, e.g., data, model and communication quality, which makes them unsuitable in practical wireless networks. Hence, it is essential to design multi-criteria based client-edge association schemes for realizing communication-efficient HFL systems. Besides, NOMA shows great potential in addressing the resource scarceness issue via improved access and communication efficiency, which is beneficial to facilitate HFL convergence. Although [25] has conducted the research on NOMA-enabled HFL system, the impact of NOMA on HFL performance was not analyzed.

Motivated by above analysis, we propose a novel NOMA enabled HFL system in this paper, and design a multi-criteria client selection policy based on fuzzy logic. We investigate the joint optimization problem of edge server scheduling and resource allocation to minimize the total time and energy cost. The closed-form solution of edge server scheduling is obtained through the penalty dual decomposition (PDD) approach, and a DDPG-based algorithm is introduced to allocate resources efficiently. The main contributions of this paper are summarized as follows:

- We propose a NOMA enabled HFL system for reduced communication and energy overhead, where the semi-synchronous cloud aggregation is considered. The implementation of HFL training is divided into the client-edge phase and the edge-cloud phase. The corresponding time consumption and energy cost are formulated at each phase.
- 2) We devise a multi-criteria client-edge association policy according to fuzzy logic in light of client heterogeneity, including wireless channel quality, data quantity as well as model staleness. The membership functions for fuzzy inputs and fuzzy outputs, and the fuzzy rules are devised carefully. The final defuzzied output of each client implies its competency level to associate with the edge server, which is utilized to guide the client selection.
- 3) Aiming to minimize the total cost at one HFL round, a joint edge server scheduling and resource allocation problem is formulated, which is a non-convex mixed-integer non-linear programming (MINLP) problem. In order to solve it effectively, the original problem is decomposed into two subproblems for edge server scheduling and resource allocation, respectively. A PDD based algorithm with the double-loop structure is proposed to derive the closed-form solution for edge server scheduling. We resort the DRL method for resource allocation with the consideration of time-varying channels, and develop a DDPG-based algorithm to address the continuous resource allocation subproblem.

#### C. Organization

We organize the remainder of this paper as follows. Section II presents the NOMA enabled HFL system model. In Section III, the fuzzy based client selection scheme is designed. In Section IV, we propose the edge scheduling and resource allocation algorithms to achieve total cost

<span id="page-2-1"></span>![](_page_2_Picture_9.jpeg)

Fig. 1. NOMA enabled HFL system.

minimization. Extensive simulation results are shown in Section V, and we conclude this paper in Section VI.

#### II. SYSTEM MODEL

<span id="page-2-0"></span>Fig. 1 illustrates the proposed HFL system, where a remote cloud server coordinates M edge servers denoting by  $\mathcal{M} \in \{1,2,\ldots,M\}$  and each edge server m associates with a set of clients  $\mathcal{N}_m \in \{1,2,\ldots,N_m\}$ . We assume all the nodes are equipped with single-antenna in the system.\(^1\) Let  $\mathcal{N} \in \{1,2,\ldots,N\}$  denotes the client set, and we assume  $N \gg M$ . For client n, it owns a local training data set denoted by  $\mathcal{D}_n = \{(\mathbf{x}_i,y_i)\}_{i=1}^{D_n}$ , in which  $D_n$  denotes the total number of data samples,  $\mathbf{x}_i$  and  $y_i$  are the i-th data sample and the corresponding label, respectively. We divide the HFL implementation into two phases, including the client-edge phase as well as the edge-cloud phase, and the details are presented as follows.

## A. Client-Edge Phase

1) Local Model Training: At this stage, client n trains the local model utilizing its local data samples. Denote client n's local loss function by  $l_n(\mathbf{w}_n, \mathbf{x}_i, y_i)$ , where  $\mathbf{w}_n$  is the model parameter which characterizes the output label  $y_i$  with the input data sample  $\mathbf{x}_i$ . Based on this, we define the local loss of client n as

$$L_n\left(\mathbf{w}_n\right) = \frac{1}{D_n} \sum_{i=1}^{D_n} l_n\left(\mathbf{w}_n, \mathbf{x}_i, y_i\right). \tag{1}$$

At the t-th local iteration, client n updates its local FL model in the following gradient descent manner:

<span id="page-2-3"></span>
$$\mathbf{w}_{n}^{t} = \mathbf{w}_{n}^{t-1} - \eta \nabla L_{n} \left( \mathbf{w}_{n}^{t-1} \right), \tag{2}$$

in which  $\eta$  denotes the learning rate.

We adopt the concept of local training accuracy  $\theta \in (0,1)$  in this paper, and assume it is the same for all clients. In essence,  $\theta$  indicates the defined threshold for the change of loss function between local iterations for clients' local model training [29]. In order to attain the local accuracy  $\theta$ , client n is expected to execute multiple rounds of local model updates until  $\|\nabla L_n(\mathbf{w}_n^t)\| \le \theta \|\nabla L_n(\mathbf{w}_n^{t-1})\|$  is satisfied. Particularly,  $\theta = 0$  indicates the local optimization problem

<span id="page-2-2"></span><sup>1</sup>Note that the single-antenna setting is widely adopted in existing HFL works, e.g., [21], [22]. However, the analysis framework in this paper can be extended to multi-antenna scenarios with careful beamforming design.

<span id="page-3-0"></span>of client n is required to be solved optimally and hence more local iterations are required; otherwise,  $\theta=1$  indicates no progress for local optimization problem. According to [29], [30], to achieve the local accuracy  $\theta$  for general smooth and convex leaning tasks, the required local iteration number is given by

$$\tau_1 = \mu \log \left(\frac{1}{\theta}\right),\tag{3}$$

where  $\mu$  represents the constant related to learning tasks.

For any client n, it utilizes the equipped CPU resources to complete the local model training task. Define  $f_n$  as the CPU frequency of client n. We can calculate its local training time with  $\tau_1$  local iterations by

$$t_n^{cmp} = \frac{\tau_1 c_n D_n}{f_n},\tag{4}$$

where  $c_n$  represents the required number of CPU cycles to deal with one data sample for client n. The corresponding energy consumption during the entire local model training process can be given as [31]

<span id="page-3-1"></span>
$$e_n^{cmp} = \tau_1 \frac{\beta_n}{2} f_n^2 c_n D_n, \tag{5}$$

wherein  $\frac{\beta_n}{2}$  is the computing chipsets' effective capacitance coefficient at client n.

2) Client-Edge Transmission: In this paper, we propose the utilization of NOMA transmission between clients and the associated edge server. NOMA enables multiple clients to multiplex on the same channel to simultaneously upload their local models, hence improving the communication access and efficiency. Nevertheless, the interference among clients is introduced due to simultaneous transmission over the same channel. To tackle this issue, the successive interference cancellation (SIC) approach has been commonly adopted in NOMA-enabled systems [32]. Note that the increased number of clients for NOMA transmission will increase the burden of SIC at the receiver side, which can be properly addressed via user clustering in NOMA systems. However, it is beyond the scope of this paper and we assume the edge serve is powerful enough to perform SIC for NOMA transmission of multiple clients. For the sake of simplicity, we omit the iteration index in the following content. Denote  $s_n$  by the encapsulated signal of client n's local model parameter, and we normalize  $s_n$  as  $\mathbb{E}(|s_n|^2) = 1$  [33]. We define  $p_n$  as the client n's transmitting power. Let  $h_{n,m}$  be the gain of wireless channel between client n and its associated edge server m. Note that the association between clients and edge servers is a vital issue to be carefully considered in HFL, as a client has the access to associate with more than one edge server but only associates with one specific edge server at each round. With NOMA transmission, the received signal at edge server m is the superposition form of its selected clients' signals, which is expressed as

<span id="page-3-3"></span>
$$y_m = \sum_{n=1}^{N_m} (\sqrt{p_n} h_{n,m} s_n) + \hat{n}_m,$$
 (6)

wherein  $\hat{n}_m \sim \mathcal{CN}\left(0, \sigma_m^2\right)$  denotes the additive white Gaussian noise (AWGN) whose mean is 0 and variance is  $\sigma_m^2$ .

To perform SIC in the uplink NOMA transmission, by regarding other signals as interference, the receiver decodes the most powerful signal first. After subtracting the decoded signal from the superpositioned signal, the receiver subsequently performs decoding to the second strongest signal in the same manner. This approach proceeds until decoding all signals successfully. Note that the design of an optimal SIC decoding order is beyond the scope of this paper. Thus, for simplicity of analysis, we make assumption that the decoding order is decided based on the received power, i.e.,  $p_1|h_{1,m}|^2 > p_2|h_{2,m}|^2 > \cdots > p_{N_m}|h_{N_m,m}|^2$ , which indicates that for the edge server m, the client 1's signal is the first decoded signal, while the client  $N_m$ 's signal is the last decoded one. In this case, the signal-to-interference-to-noise ratio (SINR) of client n at the edge server m can be presented as

$$SINR_{n,m} = \frac{p_n |h_{n,m}|^2}{\sum_{j=n+1}^{N_m} p_j |h_{j,m}|^2 + \sigma_m^2},$$
 (7)

where  $\sum_{j=n+1}^{N_m} p_j |h_{j,m}|^2$  denotes the interference caused by the clients which are decoded after client n. In particular, the SINR for client  $N_m$  is calculated by  $\text{SINR}_{N_m,m} = \frac{p_{N_m} |h_{N_m,m}|^2}{\sigma_m^2}$ . Based on the derived SINR, client n's achievable data rate at the edge server m is expressed as

$$R_{n,m} = B\log_2\left(1 + SINR_{n,m}\right),\tag{8}$$

wherein B denotes the channel bandwidth.

Given the client *n*'s achievable data rate, its NOMA transmission time at one edge iteration is given by

$$t_{n,m}^{com} = \frac{d_n}{R_{n,m}},\tag{9}$$

<span id="page-3-2"></span>where  $d_n$  denotes the size of client n's local model parameter, which is considered to be the same among all clients because of the similar numbers of elements in local models [17]. The corresponding energy consumption can be calculated as

$$e_{n,m}^{com} = p_n t_{n,m}^{com}. (10)$$

3) Edge Model Aggregation: At this stage, for edge server m, it would aggregate the local FL model parameters sent by its selected clients set  $\mathcal{N}_m$  in an averaging manner, which is defined as

$$\mathbf{w}_m = \frac{\sum_{n \in \mathcal{N}_m} D_n \mathbf{w}_n}{D_{\mathcal{N}_m}},\tag{11}$$

where  $D_{\mathcal{N}_m} = \cup_{n \in \mathcal{N}_m} D_n$  denotes the size of aggregated dataset at edge server m. Then, each edge server broadcasts the aggregated edge model parameter to its selected clients to perform the local model training of the next iteration. This process is conducted iteratively by the edge server until meeting the edge accuracy requirement  $\xi$  which is the same for all edge servers. Note that the edge training process in HFL is consistent with the global training in conventional FL with weaker edge accuracy. Hence, as revealed in [34], the number of edge iteration can be calculated by

<span id="page-3-4"></span>
$$\tau_2 = \frac{\delta\left(\log\left(\frac{1}{\xi}\right)\right)}{1-\theta},\tag{12}$$

wherein δ denotes the constant regarding learning tasks. It is also a common result adopted in existing HFL-related works considering edge accuracy [\[22\],](#page-13-21) [\[25\].](#page-13-24)

Given there are abundant resources for edge servers to conduct the edge model aggregation and broadcasting, the corresponding time and energy consumption are reasonably ignored in this paper. Hence, after τ<sup>2</sup> edge iterations, the total time and energy consumption for client set N<sup>m</sup> selected by the edge server m can respectively be expressed as

$$T_{\mathcal{N}_m}^{edge} = \max_{n \in \mathcal{N}_m} \left\{ \tau_2 \left( t_n^{cmp} + t_{n,m}^{com} \right) \right\}, \tag{13}$$

$$E_{\mathcal{N}_m}^{edge} = \sum_{n \in \mathcal{N}_m} \tau_2 \left( e_n^{cmp} + e_{n,m}^{com} \right). \tag{14}$$

Note that the Max in [\(13\)](#page-4-1) implies the edge model aggregation is synchronous, i.e., the last client to complete the model parameter uploading determines the total time consumption. The synchronous manner for the edge model aggregation is reasonable as each edge server's coverage is limited, leading to the moderate time consumption for each client. In this case, the straggler problem will not degrade HFL performance severely.

#### *B. Edge-Cloud Phase*

*1) Edge-Cloud Transmission:* After reaching the edge accuracy, the aggregated edge model parameter is uploaded by each edge server to the cloud for global model aggregation. Given that the number of edge servers is much less than that of clients in our proposed HFL system, the communication burden for edge-cloud transmission is much less severe than that for the client-edge phase. Hence, both the wired and wireless transmission are suitable candidates for edge-cloud communication [\[23\].](#page-13-22) We adopt the common wireless transmission technique, i.e., orthogonal frequency division multiple access (OFDMA), for edge-cloud communication in this paper. Note that the edge servers have relatively abundant resources for computing and communicating compared with clients. Thus, the corresponding resource allocation issue is not the focus of this paper. For ease of analysis, we omit the calculation of achievable data rate for edge servers. Define p<sup>m</sup> and R<sup>m</sup> as the uplink transmitting power and data rate of edge server m, respectively. As a result, its time and energy consumption for model parameter transmission can be presented by

$$T_m^{cloud} = \frac{d_m}{R_m},\tag{15}$$

$$E_m^{cloud} = p_m T_m^{cloud}, (16)$$

where d<sup>m</sup> is the size of aggregated edge model parameter.

*2) Cloud Model Aggregation:* We consider a semisynchronous cloud model aggregation mechanism in this paper, due to the following two aspects. On the one hand, if we adopt the absolute synchronous cloud aggregation, the long transmission delay may cause severe straggler problem, which will degrade the HFL performance. On the other hand, if the absolute asynchronous cloud aggregation manner is adopted, the cloud server would frequently communicate with the edge servers with better computing capability and communicating conditions, which may not only lead to heavy communication overhead but also lead to the overfitting risk for the global HFL model. The semi-synchronous cloud aggregation offers a

<span id="page-4-2"></span>![](_page_4_Picture_13.jpeg)

Fig. 2. Illustration of semi-synchronous cloud aggregation.

<span id="page-4-1"></span>balanced tradeoff to address these issues. As shown in Fig. [2,](#page-4-2) in our proposed semi-synchronous cloud aggregation, the first M<sup>c</sup> edge servers are selected by the cloud server according to their total time consumption, while the rest of edge servers will proceed their edge training and await the next cloud aggregation when they have finished the edge model uploading. Note that the blank space in Fig. [2](#page-4-2) indicates the idle time for the edge server which has better capability to conduct edge training. Compared with the absolute synchronous scheme, it will not be too long under the proposed semi-synchronous aggregation mechanism, hence guaranteeing better HFL performance. The selected edge servers set is denoted by M<sup>c</sup> ∈ {1, 2, . . . , Mc}. Denote z<sup>m</sup> as the scheduling indicator for edge server m, i.e., if the edge server m is selected for global model aggregation, z<sup>m</sup> = 1; otherwise z<sup>m</sup> = 0. The semisynchronous aggregation at the cloud server is given by

$$\mathbf{w} = \frac{\sum_{m \in \mathcal{M}} z_m D_{\mathcal{N}_m} \mathbf{w}_m}{\bigcup_{m \in \mathcal{M}} z_m D_{\mathcal{N}_m}}.$$
 (17)

Note that we ignore the time and energy cost of the cloud server for cloud model aggregation and broadcasting in this paper, as it is supposed to be powerful enough in computing and communicating. Therefore, we can derive the system-wise total time and energy consumption for the proposed HFL system in one global iteration, which are given by

$$T = \max_{m \in \mathcal{M}} z_m \left\{ T_m^{cloud} + T_{\mathcal{N}_m}^{edge} \right\}, \tag{18}$$

$$E = \sum_{m \in \mathcal{M}} z_m \left( E_m^{cloud} + E_{\mathcal{N}_m}^{edge} \right). \tag{19}$$

#### <span id="page-4-0"></span>III. FUZZY LOGIC BASED CLIENT-EDGE ASSOCIATION

The association between clients and edge servers is designed in this section, which is vital in enhancing the HFL performance, especially in large-scale systems. Note that the number of clients far exceeds that of edge servers in our proposed HFL system. In this case, only a subset of clients can associate with the edge server because of the limited communication resources. Besides, we consider that each client can be selected by different edge servers, but it can only associate with one edge server during one global iteration. Therefore, it requires us to carefully design the client-edge association to achieve better HFL performance. Previous client-edge association schemes mainly depend on a single factor or criterion, such as the distance between the edge server and clients,

<span id="page-5-0"></span>![](_page_5_Picture_2.jpeg)

Fig. 3. Fuzzy logic based client-edge association.

the data distribution of clients and so forth. However, such single-criterion based client-edge association schemes fail to simultaneously balance the client heterogeneity in the system, which inevitably degrades the HFL performance. Differently, in this paper, a multi-criteria based client-edge association scheme according to the fuzzy logic [35] is proposed, as shown in Fig. 3, by simultaneously considering the client-edge channel quality, the data quantity of client and the local model staleness. The details of the fuzzy logic based client-edge association scheme are presented as follows.

#### A. Fuzzy Input

- 1) Channel Quality (CQ): This input variable indicates the client-edge communication environment. In our proposed HFL system, the client with poor CQ is not supposed to transmit its local model for edge aggregation, because it will cause long transmission delay under the synchronous model aggregation manner, which could degrade the HFL performance. Thus, CQ is one of the key factors needed to be considered when designing the client-edge association scheme. Note that in wireless communications, the CQ is affected by various factors. In this case, the CQ of a client in HFL cannot be determined merely by the distance from the client to the edge server. In other words, even if the client is located closely to the edge server, the CQ between them may still be unsatisfied due to the fading effect. In this case, we are supposed to choose CQ rather than the distance as a factor for the client-edge association design.
- 2) Data Quantity (DQ): To improve HFL training performance, it is essential to select as many clients as possible, especially considering heterogeneous data distribution among clients. In this case, sufficient data samples can be utilized to train the global HFL model. Nevertheless, we consider that the number of clients far exceeds that of edge servers in the proposed system, leading to few selected clients at each global round. Thus, to achieve better HFL performance, we need to consider how to select clients with more data samples. Hence, DQ is another essential factor needed to be considered when designing the association scheme between the clients and the edge servers.
- <span id="page-5-5"></span>3) Model Staleness (MS): The MS describes the elapsed time from the client's latest selection by the associated edge server. Specifically, if a client has not been selected by the edge server for a long time, its local model will be more stale, which is not beneficial for the global model training and convergence [36]. To realize better HFL performance, the edge servers tend to obtain local models updated timely. We define the client n's MS value at the i-th global round as  $A_n^i$ , which

<span id="page-5-1"></span>![](_page_5_Figure_9.jpeg)

<span id="page-5-4"></span>Fig. 4. Membership functions of fuzzy logic.

can be calculated by

<span id="page-5-3"></span>
$$A_n^i = \begin{cases} A_n^{i-1} + 1, & a_{n,m}^{i-1} = 0, \\ 1, & a_{n,m}^{i-1} = 1, \end{cases}$$
 (20)

where  $a_{n,m}^{i-1}$  denotes the association indicator at the (i-1)-th global HFL iteration, i.e., if client n is selected by the edge server m,  $a_{n,m}^{i-1}=1$ ; otherwise  $a_{n,m}^{i-1}=0$ . The clients with higher MS have a higher probability to be associated with the edge server, as their data samples are more informative to update the global model. Therefore, the average MS of the entire HFL system can be guaranteed to be relatively low, which benefits the fast convergence of HFL.

It is worthwhile to point out that, for the unity of expression, we normalize the above three input variables in a same manner as:

<span id="page-5-2"></span>
$$NV = \frac{V}{MV} \times 100\%,\tag{21}$$

where V denotes the input variable, MV indicates the maximum value of the input variables, and NV is the normalized value of the input variable. Note that for different inputs, V and MV need to be replaced with corresponding values.

#### B. Fuzzy Output

With fuzzy logic, the above three numerical inputs are transformed into fuzzy formats by a fuzzifier via the defined fuzzy membership functions in Fig. 4. The transformed fuzzy input sets for these three criteria are given as

$$CQ \in \{weak, medium, strong\},$$
  
 $DQ \in \{shortage, average, sufficient\},$   
 $MS \in \{fresh, medium, stale\}.$ 

Based on the three types of fuzzy inputs, we can obtain 27 fuzzy rules in Table. I to build a map between the fuzzy inputs and the fuzzy output. Define the fuzzy output set as:

$$Output \in \{poor, fair, average, good, excellent\}.$$

The membership function of the fuzzy output for defuzzification is also defined in Fig. 4. Note that in this paper,

TABLE I FUZZY LOGICAL RULES

<span id="page-6-1"></span>

| Rule | Channel quality | Data quantity | Model staleness | Output    |
|------|-----------------|---------------|-----------------|-----------|
| 1    | Strong          | Shortage      | Fresh           | Fair      |
| 2    | Strong          | Shortage      | Medium          | Average   |
| 3    | Strong          | Shortage      | Stale           | Good      |
| 4    | Strong          | Average       | Fresh           | Average   |
| 5    | Strong          | Average       | Medium          | Good      |
| 6    | Strong          | Average       | Stale           | Excellent |
| 7    | Strong          | Sufficient    | Fresh           | Good      |
| 8    | Strong          | Sufficient    | Medium          | Excellent |
| 9    | Strong          | Sufficient    | Stale           | Excellent |
| 10   | Medium          | Shortage      | Fresh           | Poor      |
| 11   | Medium          | Shortage      | Medium          | Fair      |
| 12   | Medium          | Shortage      | Stale           | Average   |
| 13   | Medium          | Average       | Fresh           | Fair      |
| 14   | Medium          | Average       | Medium          | Average   |
| 15   | Medium          | Average       | Stale           | Good      |
| 16   | Medium          | Sufficient    | Fresh           | Average   |
| 17   | Medium          | Sufficient    | Medium          | Good      |
| 18   | Medium          | Sufficient    | Stale           | Excellent |
| 19   | Weak            | Shortage      | Fresh           | Poor      |
| 20   | Weak            | Shortage      | Medium          | Poor      |
| 21   | Weak            | Shortage      | Stale           | Fair      |
| 22   | Weak            | Average       | Fresh           | Poor      |
| 23   | Weak            | Average       | Medium          | Fair      |
| 24   | Weak            | Average       | Stale           | Average   |
| 25   | Weak            | Sufficient    | Fresh           | Fair      |
| 26   | Weak            | Sufficient    | Medium          | Average   |
| 27   | Weak            | Sufficient    | Stale           | Good      |

we utilize the Max-Min method [37] to derive one rule from multi-criteria and combine multiple rules. To be specific, we choose the minimum value of the three membership functions as the degree of the fuzzy rule. When multiple rules correspond to the same output, we choose the rule with maximum degree.

After utilizing the Max-Min method described above, we can obtain multiple fuzzy outputs related to different fuzzy rules. Now, we need to defuzzify these fuzzy outputs into numerical formats based on the center of gravity (COG) method [38], which is expressed as

<span id="page-6-10"></span>
$$NO^* = \frac{\sum NO \times f(NO)}{\sum f(NO)},$$
(22)

where NO denotes the normalized output, f(NO) represents the corresponding membership function according to Fig. 4 and  $NO^*$  is the final normalized output which indicates the clients' competency level to associate with the edge server.

Then, each edge server sorts the clients located in its service coverage in a descending order according to their  $NO^*$ , and selects the first  $N_m$  clients to participate in edge model aggregation. Note that a client may be selected by more than one edge server. In this case, the client chooses the nearest edge server for association, and other edge servers will select a client to substitute in their queues.

## <span id="page-6-0"></span>IV. JOINT EDGE SERVER SCHEDULING AND OPTIMAL RESOURCE ALLOCATION

## A. Problem Formulation

In this part, given the fuzzy-based client-edge association scheme, our objective is to achieve the total cost minimization in one global iteration of our proposed HFL system, while jointly optimizing edge server scheduling and resource

<span id="page-6-6"></span>![](_page_6_Figure_12.jpeg)

Fig. 5. The procedure of proposed solutions.

allocation. Denote  $\lambda_t, \lambda_e \in [0,1]$  satisfying  $\lambda_t + \lambda_e = 1$  by the importance weighting indicators related to the time consumption and energy consumption, respectively. Then, we can formulate the total cost minimization problem in the HFL system as

<span id="page-6-5"></span>
$$\min_{\mathbf{p}, \mathbf{f}, \mathbf{z}} \lambda_t T + \lambda_e E \tag{23a}$$

s.t. 
$$p_n^{min} \le p_n \le p_n^{max}, \quad \forall n \in \mathcal{N}_m,$$
 (23b)

<span id="page-6-2"></span>
$$f_n^{min} \le f_n \le f_n^{\max}, \quad \forall n \in \mathcal{N}_m,$$
 (23c)

<span id="page-6-4"></span><span id="page-6-3"></span>
$$z_m \in \{0, 1\}, \quad \forall m \in \mathcal{M},$$
 (23d)

<span id="page-6-9"></span>where constraints (23b) and (23c) limit the range of transmitting power and computing frequency of client n, respectively. Constraint (23d) indicates that  $z_m$  is a binary variable.

<span id="page-6-8"></span>Apparently, problem (23) is a non-convex MINLP problem, which is intractable to derive the optimal solutions directly. To efficiently address problem (23), in this section, we propose to decompose it into two subproblems for edge server scheduling and resource allocation, and design the corresponding optimization algorithms to obtain the solutions iteratively. The key procedure of our proposed scheme which combines the fuzzy based client-edge association and joint edge server scheduling and resource allocation is illustrated in Fig. 5.

#### B. Edge Server Scheduling

Given the resource allocation variables  $\mathbf{p}$  and  $\mathbf{f}$ , problem (23) is reduced to schedule edge servers to minimize the total cost. Nevertheless, it is still intractable due to the existence of binary variable  $\mathbf{z}$ . To address this problem effectively, an auxiliary variable  $\tilde{z}_m$  is introduced which is subject to the constraints of  $\tilde{z}_m = z_m$ ,  $z_m (1 - \tilde{z}_m) = 0$ , as well as  $0 \leq \tilde{z}_m \leq 1, \forall m \in \mathcal{M}$ . Note that these constraints guarantee  $z_m$  equals to  $\tilde{z}_m$  only at 0 or 1. Besides, to deal with the Max expression in T, we define  $U = \max_{n \in \mathcal{N}_m} \left\{ \tau_2 \left( t_n^{cmp} + t_{n,m}^{com} \right) \right\}$  and  $W = \max_{m \in \mathcal{M}} \left\{ z_m \left( T_m^{cloud} + U \right) \right\}$ . Then, the edge server scheduling subproblem can be transformed into a more tractable form, which is written as

<span id="page-6-7"></span>
$$\min_{\mathbf{z}, \tilde{\mathbf{z}}, U, W} \lambda_t W + \lambda_e \sum_{m \in \mathcal{M}} z_m \left( E_m^{cloud} + E_{\mathcal{N}_m}^{edge} \right)$$
 (24a)

s.t. 
$$t_n^{cmp} + t_{n,m}^{com} \le U, \quad \forall n \in \mathcal{N}_m, \ \forall m \in \mathcal{M},$$
 (24b)

$$z_m \left( T_m^{cloud} + U \right) \le W, \quad \forall m \in \mathcal{M},$$
 (24c)

$$z_m - \tilde{z}_m = 0, \quad \forall m \in \mathcal{M},$$
 (24d)

$$z_m (1 - \tilde{z}_m) = 0, \quad \forall m \in \mathcal{M},$$
 (24e)

$$0 \le \tilde{z}_m \le 1, \quad \forall m \in \mathcal{M}.$$
 (24f)

In the following, a double-loop PDD-based algorithm [39] is proposed to solve the problem (24). Specifically, the PDDbased algorithm's inner loop solves the augmented Lagrangian (AL) problem, while the dual or penalty variables related to the constraints are updated at the outer loop. The AL form of problem (24), which is utilized to dualize and penalize the equality constraints (24d) and (24e), can be

<span id="page-7-16"></span><span id="page-7-2"></span>
$$\min_{\mathbf{z}, \tilde{\mathbf{z}}, U, W} \lambda_t W + \lambda_e \sum_{m \in \mathcal{M}} z_m \left( E_m^{cloud} + E_{\mathcal{N}_m}^{edge} \right) 
+ \frac{1}{2v} \sum_{m=1}^{M} \left[ z_m \left( 1 - \tilde{z}_m \right) + v q_m \right]^2 
+ \frac{1}{2v} \sum_{m=1}^{M} \left( z_m - \tilde{z}_m + v \tilde{q}_m \right)^2$$
(25a)

s.t. 
$$t_n^{cmp} + t_{n,m}^{com} \le U$$
,  $\forall n \in \mathcal{N}_m$ ,  $\forall m \in \mathcal{M}$ , (25b)  
 $z_m \left(T_m^{cloud} + U\right) \le W$ ,  $\forall m \in \mathcal{M}$ , (25c)

$$z_m \left( T_m^{cloud} + U \right) < W, \quad \forall m \in \mathcal{M},$$
 (25c)

$$0 < \tilde{z}_m < 1, \quad \forall m \in \mathcal{M}, \tag{25d}$$

in which v represents the non-negative penalty parameter,  $q_m$  and  $\tilde{q}_m$  denote the dual variables related to the equality constraints (24d) and (24e), respectively. The AL problem (25) is solved in the inner loop via problem decomposition, and the details are shown as follows.

1) Solution of  $\tilde{z}_m$ : By fixing other variables, the unconstrained solution for  $\tilde{z}_m$  can be derived directly by taking the first-order derivative towards the unconstrained function (25a) and enforcing the first-order optimality condition, which can be expressed as

$$\tilde{z}_{m}^{u} = \frac{z_{m}^{2} + q_{m}z_{m}v + z_{m} + \tilde{q}_{m}v}{z_{m}^{2} + 1}.$$
 (26)

Recalling that  $0 \le \tilde{z}_m \le 1$ , we can obtain the optimal solution of  $\tilde{z}_m$  as

$$\tilde{z}_{m}^{*} = \begin{cases} 0, & \tilde{z}_{m}^{u} \leq 0, \\ \tilde{z}_{m}^{u}, & 0 < \tilde{z}_{m}^{u} < 1, \\ 1, & \tilde{z}_{m}^{u} \geq 1. \end{cases}$$
 (27)

2) Solution of  $z_m$ : To derive the optimal solution of  $z_m$ , we shall solve the subproblem with respect to  $z_m$  by fixing other variables. The transformed problem is formulated as

$$\min_{\mathbf{z}} \lambda_e \sum_{m \in \mathcal{M}} z_m \left( E_m^{cloud} + E_{\mathcal{N}_m}^{edge} \right) \\
+ \frac{1}{2v} \sum_{m=1}^M \left[ z_m \left( 1 - \tilde{z}_m \right) + v q_m \right]^2 \\
+ \frac{1}{2v} \sum_{m=1}^M \left( z_m - \tilde{z}_m + v \tilde{q}_m \right)^2 \qquad (28a)$$
s.t.  $z_m \left( T_m^{cloud} + U \right) \leq W, \quad \forall m \in \mathcal{M}. \qquad (28b)$ 

The following Lemma 1 provides the optimal solution of  $z_m$ .

<span id="page-7-4"></span>Lemma 1: The optimal solution  $z_m^*$  can be given by

<span id="page-7-8"></span>
$$z_m^* = \frac{I_m v}{1 + (1 - \tilde{z}_m)^2},\tag{29}$$

<span id="page-7-1"></span><span id="page-7-0"></span>where  $I_m = \frac{\tilde{z}_m}{v} - \tilde{q}_m - q_m (1 - \tilde{z}_m) - \lambda_e \left( E_m^{cloud} + E_{\mathcal{N}_m}^{edge} \right) - \gamma_m \left( T_m^{cloud} + U \right)$ , and  $\gamma_m$  is the Lagrange multiplier corresponding to the constraint (28b).

<span id="page-7-15"></span>*Proof:* It is easy to prove that the second-order derivative of (28a) is always larger than zero, suggesting it is a convex function. Besides, considering the convex constraint (28b), the optimization problem (28) belongs to a convex problem. Hence, we can utilize the Lagrange dual method to obtain the optimal solution. The Lagrange function of problem (28) is formulated as

$$\mathcal{L}(\mathbf{z}, \gamma_m) = \lambda_e \sum_{m \in \mathcal{M}} z_m \left( E_m^{cloud} + E_{\mathcal{N}_m}^{edge} \right)$$

$$+ \frac{1}{2v} \sum_{m=1}^M \left[ z_m \left( 1 - \tilde{z}_m \right) + v q_m \right]^2$$

$$+ \frac{1}{2v} \sum_{m=1}^M \left( z_m - \tilde{z}_m + v \tilde{q}_m \right)^2$$

$$+ \gamma_m \left[ z_m \left( T_m^{cloud} + U \right) - W \right]. \tag{30}$$

<span id="page-7-3"></span>By using the first-order derivative of  $\mathcal{L}(\mathbf{z}, \gamma_m)$  with respect to  $z_m$ , we can derive

$$\frac{\partial \mathcal{L}\left(\mathbf{z}, \gamma_{m}\right)}{\partial z_{m}} = \lambda_{e} \left(E_{m}^{cloud} + E_{N_{m}}^{edge}\right) 
+ \frac{1}{v} \left[z_{m} \left(1 - \tilde{z}_{m}\right) + vq_{m}\right] \left(1 - \tilde{z}_{m}\right) 
+ \frac{1}{v} \left(z_{m} - \tilde{z}_{m} + v\tilde{q}_{m}\right) + \gamma_{m} \left(T_{m}^{cloud} + U\right).$$
(31)

By setting  $\frac{\partial \mathcal{L}(\mathbf{z}, \gamma_m)}{\partial z_m} = 0$ , the optimal solution of  $z_m$  can be derived, which is shown in (29). This completes the proof.

<span id="page-7-9"></span>3) Solutions of U and W: According to the definition of U and W, the optimal solutions can be calculated as follows:

<span id="page-7-12"></span><span id="page-7-11"></span>
$$U^* = \max_{n \in \mathcal{N}_m} \left\{ \frac{\tau_1 c_n D_n}{f_n} + \frac{d_n}{R_{n,m}} \right\},\tag{32}$$

$$W^* = \max_{m \in \mathcal{M}} \left\{ z_m^* \left( \frac{d_m}{R_m} + \tau_2 U^* \right) \right\}. \tag{33}$$

<span id="page-7-10"></span><span id="page-7-7"></span>4) Update of  $q_m$  and  $\tilde{q}_m$ : After obtaining the optimal solutions for the AL problem (25) in the inner loop of the proposed PDD-based algorithm, we update the dual variables  $q_m$  and  $\tilde{q}_m$  in the outer loop as follows:

<span id="page-7-13"></span>
$$q_m^{l+1} = q_m^l + \frac{1}{n^l} \left[ z_m^* \left( 1 - \tilde{z}_m^* \right) \right], \forall m \in \mathcal{M},$$
 (34)

<span id="page-7-14"></span>
$$\tilde{q}_{m}^{l+1} = \tilde{q}_{m}^{l} + \frac{1}{v^{l}} [z_{m}^{*} - \tilde{z}_{m}^{*}], \forall m \in \mathcal{M},$$
 (35)

in which l is the iteration index of the outer loop.

<span id="page-7-6"></span><span id="page-7-5"></span>In Algorithm 1, the PDD-based edge server scheduling algorithm is presented. The double-loop Algorithm 1 solves the AL problem and updates the dual variables in its inner loop and outer loop, respectively. It is revealed in [39] that the PDD-based algorithm can converge to the stationary solutions of problem (24).

#### Algorithm 1 PDD-Based Edge Server Scheduling Algorithm

```
1: Initialize auxiliary and dual variables \tilde{\mathbf{z}}, \mathbf{q} and \tilde{\mathbf{q}};
2: Set parameter \varepsilon = 10^{-4} and set the maximum iteration number as L^{max}.
 3: for outer loop index l=1 to L^{max} do
            while F^{l} - F^{l-1} \geq \varepsilon do
 4.
 5:
                   Obtain \tilde{z}_m^* according to (26) and (27);
 6:
                   Calculate the optimal edge server scheduling z_m^* based on (29);
 7:
                   Obtain U^* and W^* from (32) and (33);
           \begin{array}{ll} \mbox{end while} \\ \mbox{Update } q_m^{l+1} \mbox{ and } \tilde{q}_m^{l+1} \mbox{ based on (34) and (35);} \end{array}
 8:
 9:
10:
            Set l = l + 1.
11: end for
```

#### C. Resource Allocation

Given the scheduled edge servers, we then consider the resource allocation subproblem. Now, we can convert the original problem (23) to a total cost minimization problem with the variables of resource allocation, which is formulated as

<span id="page-8-2"></span>
$$\min_{\mathbf{p},\mathbf{f}} \lambda_t T + \lambda_e E \tag{36a}$$

s.t. 
$$p_n^{min} \le p_n \le p_n^{\max}, \quad \forall n \in \mathcal{N}_m,$$
 (36b)  
 $f_n^{min} \le f_n \le f_n^{\max}, \quad \forall n \in \mathcal{N}_m.$  (36c)

$$f_n^{min} \le f_n \le f_n^{\max}, \quad \forall n \in \mathcal{N}_m.$$
 (36c)

Owing to the coupled optimization variables in (36a), it is still challenging to obtain the optimal solutions utilizing traditional optimization methods. Moreover, when considering the dynamic channel environment in our proposed system, it is too challenging for the traditional methods to obtain the solutions. In this case, the DRL method is an idea candidate, which has a low optimization complexity and can interact with the dynamic environment to achieve better performance. Since problem (36) can be formulated as a Markov decision process (MDP) with the continuous action and state spaces, we adopt the DDPG-based approach to achieve optimal resource allocation in this paper. Note that in DDPG, all the associated clients are treated as one agent, as they all have the same optimization goal.

Next, to have a better understanding towards DPPG, we first introduce the concept of MDP briefly. According to the theory of Markov process, MDP can be regarded as an optimal decision process with respect to a stochastic dynamic system. More specifically, given the observed state, a new decision can be made by the agent in MDP to transfer the state and calculate the probability of state transition. Then, the new decisions are made by the decision maker according to the new observed state. The process of MDP can be described mathematically as  $\{S, A, R, P\}$ , in which S is the state of the agent, A denotes the available action for the agent under S, R denotes the achievable reward for transferring into the next state and P represents the probability of state transition when the agent takes action A under state S [41], [42]. The objective problem (36) now can be transformed into the MDP problem, and the detailed process for modeling is presented as follows.

1) State Space: We consider that both the dynamic channel information of the network as well as the agent state are included in the state space. Denote  $S_j$  by the agent's state space at time slot j, which is described as  $S_j = \{h_{n,m}^j, D_n, \forall n \in \mathcal{N}_m, \forall m \in \mathcal{M}\}$ . The  $h_{n,m}^j$  denotes the

<span id="page-8-3"></span>![](_page_8_Figure_12.jpeg)

Fig. 6. The framework of DDPG training model.

<span id="page-8-1"></span>channel gain from client n to edge server m at j-th time slot, and  $D_n$  represents the data size of client n.

- 2) Action Space: Based on the observed state information, reasonable decisions are made by the agent for power and computational resource allocation. At time slot j, the agent's action space can be described as  $A_j = \{p_n^j, f_n^j, \forall n \in \mathcal{N}_m\}.$
- 3) Reward: By interacting with the environment with action  $A_i$ , the new state  $S_{i+1}$  and the reward  $R_i$  can be obtained. We adopt the straightforward principle that setting the negative total cost as the instantaneous reward, which is given by

$$R_i = -(\lambda_t T + \lambda_e E). \tag{37}$$

The reason is that DDPG training aims to realize the reward maximization, while our formulated objective is to minimize the total cost.

In DDPG training model, there is an actor-critic framework, which is illustrated in Fig. 6. Specifically, based on the current state, the actor network  $\nu\left(S|\theta^{\nu}\right)$  serves for action selection, while the critic network  $Q(S, A|\theta^Q)$  evaluates the action-state value. The  $\theta^{\nu}$  and  $\theta^{Q}$  are the corresponding weights related to neural networks. It is worthwhile to point out that each of the actor and critic networks has an online and a target network, so that the learning stability can be guaranteed and the overestimated issue in large-scale problems can be avoided. There is a similar structure between the target actor and critic network with the corresponding online networks, and they are defined as  $\nu'\left(S|\theta^{\nu'}\right)$  and  $Q'\left(S,A|\theta^{Q'}\right)$ , respectively, in which  $\theta^{\nu'}$  and  $\theta^{Q'}$  are the related weights. Note that the experience replay is adopted during DDPG training. Particularly, at j-th time slot, the tuple  $(S_i, A_i, R_i, S_{i+1})$  is stored in the experience replay buffer. When reaching the maximum buffering threshold, the training of DDPG starts to update networks by sampling the mini-batch data from the experience replay buffer randomly.

<span id="page-8-6"></span><span id="page-8-5"></span>By minimizing the following loss function, the online critic network can be updated [43]:

<span id="page-8-7"></span><span id="page-8-4"></span>
$$L\left(\theta^{Q}\right) = \frac{1}{M'} \sum_{j} \left(y_{j} - Q\left(S_{j}, A_{j} | \theta^{Q}\right)\right)^{2}, \quad (38)$$

14:

15:

16: 17: end for

#### Algorithm 2 DDPG-Based Resource Allocation Algorithm

```
1: Randomly initialize the online actor network \nu\left(S|\theta^{\nu}\right) and critic network
    Q(S, A|\theta^Q) with weights \theta^{\nu} and \theta^Q, respectively;
 2: Initialize the target actor network \nu' and critic network Q' with weights
    \theta^{\nu'} \leftarrow \theta^{\nu}, \theta^{Q'} \leftarrow \theta^{Q};
 3: Initialize the experience relay buffer and other network hyperparameters.
 4: for each episode do
         Initialize a random noise n_i for action exploration;
 5:
         Receive the initial observed state S_1;
 6:
         for time slot j=1 to J do
 7:
 8:
               Select action A_j = \nu \left( S_j | \theta^{\nu} \right) + n_j based on the online actor
               network and the random exploration noise;
 9:
               Execute action A_j, obtain the reward R_j and the next state
10:
               Store the tuple (S_i, A_i, R_i, S_{i+1}) into the replay buffer;
11:
               if reaching the maximum buffering threshold then
12:
                     Randomly sample M' mini-batch data from the replay
13:
                     Update the online critic and actor network according to
                     (38) and (39), respectively;
                     Update the target actor network and critic network based
```

where  $y_j = R_j + \psi Q' \left( S_{j+1}, \nu' \left( S_{j+1} | \theta^{\nu'} \right) | \theta^{Q'} \right)$ , denotes the mini-batch size and  $\psi$  is the discount factor. Then, the online actor network is optimized by applying the sampled policy gradient  $\nabla_{\theta^{\nu}} Y$ , which is given by

$$\nabla_{\theta^{\nu}} Y = \mathbb{E}_{\theta^{\nu}} \left[ Q \left( S_j, \nu \left( S_j | \theta^{\nu} \right) | \theta^Q \right) \right], \tag{39}$$

where  $\mathbb{E}\left(\cdot\right)$  presents the expectation operator. The target actor and critic networks are updated softly through following manner:

$$\theta^{\nu'} \leftarrow \zeta \theta^{\nu} + (1 - \zeta) \theta^{\nu'}, \theta^{Q'} \leftarrow \zeta \theta^{Q} + (1 - \zeta) \theta^{Q'}, \quad (40)$$

where  $\zeta$  controls the speed for updating.

on (40).

end if end for

Algorithm 2 summarizes the implementation of the DDPG-based resource allocation algorithm. The computation complexity of the DDPG-based algorithm mainly comes from two aspects, including the training and inference of the neural networks as well as the experience replay operation. We assume the input and output dimension of the actor network are  $X_{in}$  and  $X_{out}$ , respectively, and that of the actor network are  $X_{in} + X_{out}$  and 1, respectively. Denote the total number of neurons in the hidden layer by  $X_h$ . Hence, the time complexity of the actor network and critic network are  $\mathcal{O}(I \times X_{in} \times X_h + X_h \times X_{out})$  and  $\mathcal{O}(I \times (X_{in} + X_{out}) \times X_h + X_{out})$  $X_h$ ), respectively, where I denotes the number of iterations for gradient descent optimization. Besides, we can derive the computation complexity of the experience replay and sampling as  $\mathcal{O}(M \times (X_{in} + X_{out} + 1))$  and  $\mathcal{O}(M' \times (X_{in} + X_{out} + 1))$ , respectively [44], where  $\hat{M}$  is the total size of the replay buffer and M' is the mini-batch size of samples.

#### <span id="page-9-6"></span>V. SIMULATIONS AND ANALYSIS

<span id="page-9-0"></span>In this part, abundant of simulations are conducted to verify the superior performance of our proposed schemes. A square area with side length of 500 meters is considered in our simulation, and the cloud server is located at its center. We considered 4 edge servers which are deployed at the midpoints of the

TABLE II SIMULATION PARAMETERS

<span id="page-9-4"></span>

| Parameter                                              | Value         |  |
|--------------------------------------------------------|---------------|--|
| Bandwidth, B                                           | 1 MHz         |  |
| Carrier frequency                                      | 1 GHz         |  |
| AWGN spectral density                                  | −174 dBm/Hz   |  |
| Path loss exponent                                     | 3.76          |  |
| Transmit power limit, $p_n^{min}$ , $p_n^{max}$        | [0.01, 0.1] W |  |
| CPU cycles for each sample, $\mu$                      | $10^{7}$      |  |
| Local capacitance coefficient, $\beta_n$               | $10^{-28}$    |  |
| Computation frequency limit, $f_n^{min}$ , $f_n^{max}$ | [1, 10] GHz   |  |
| Local model size, $d_n$                                | 1 Mbit        |  |
| Learning rate, $\eta$                                  | 0.01          |  |
| Weighting parameters, $\lambda_t$ , $\lambda_e$        | 0.5           |  |

<span id="page-9-5"></span>![](_page_9_Figure_14.jpeg)

![](_page_9_Figure_15.jpeg)

Fig. 7. Examples of HFL system with fuzzy based client-edge association.

<span id="page-9-2"></span><span id="page-9-1"></span>lines connecting the four corners of the square to the cloud server, serving 64 randomly distributed clients. We set the number of associated clients for each edge server  $N_m$  as 4 considering the design complexity of the NOMA receiver. The HFL algorithm is used for the classification task using both the MNIST and CIFAR-10 datasets. We consider two data distribution scenarios for each dataset in our simulation, including the independent and identically distributed (IID) data distribution and the non-IID data distribution. For the former, the data distribution is the same among all clients, while for the latter, different clients have different amount of data with limited label types [45]. Particularly, each client has one type of labels in MNIST dataset and five types of labels in CIFAR-10 dataset [46]. We present other simulation parameters in Table II.

#### <span id="page-9-8"></span><span id="page-9-7"></span>A. Fuzzy Logic Based Client-Edge Association

In Fig. 7(a), we show an example of our proposed HFL system where the fuzzy logic is utilized to determine the clientedge association. The pentagram and triangles represent the cloud server and edge servers, respectively. Note that the red triangles in Fig. 7(a) denote the selected edge servers for cloud aggregation at this global round, while the black triangles are the unselected ones. It can be found that some clients which are not very close to the scheduled edge servers are still selected due to their sufficient training data and their stale local models. This implies that our proposed scheme designs the client-edge association based on the comprehensive ability of clients rather than a single factor. Hence, the client heterogeneity in the HFL system can be balanced effectively.

In Fig. 7(b), an example of the fuzzy output with a simple input (0.2, 0.5, 0.8) is presented. Note that the fuzzy input

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

Fig. 8. Performance of HFL on IID data.

variables are normalized according to [\(21\)](#page-5-2) for ease of analysis. Based on Fig. [4,](#page-5-1) we find that the normalized fuzzy input of the client (0.2, 0.5, 0.8) indicates that the channel quality is 'weak', the data quantity is 'average' and the local model is 'stale'. Hence, according to rule 24 in Table [I,](#page-6-1) the corresponding fuzzy output is 'average', and then the normalized output can be obtained from the x-axis value in Fig. [7\(b\).](#page-9-5) For other more complicated cases with multiple fuzzy rules, the final normalized output is obtained through the COG method shown in [\(22\).](#page-6-8)

### *B. Performance of HFL*

To demonstrate the effectiveness of our proposed fuzzy based client-edge association (FCEA) scheme in improving HFL performance, we consider the following three benchmarking schemes, including the random client-edge association (RCEA) scheme, the greedy client-edge association (GCEA) scheme and the OMA scheme. Specifically, in RCEA, the association between clients and edge servers is designed in a random manner, while in GCEA, the client with the strongest channel gain builds association with the edge server, which reflects the single-criterion association. For the OMA scheme, the OMA transmission is considered between clients and the associated edge server, where the fuzzy based association is performed.

Fig. [8](#page-10-0) illustrates the HFL performance on both IID MNIST dataset and CIFAR-10 dataset. As global round increases, there is a surge trend for the learning accuracy of all schemes before reaching the training convergence. The proposed FCEA scheme always achieves superior learning accuracy in comparison with other three benchmarks over both two datasets. This is because our scheme balances the client heterogeneity for client-edge association by accounting for three properties of clients. Besides, it can also be observed that our proposed FCEA scheme can realize the lowest global HFL loss among the considered schemes. It is interesting to find that in such IID data setting, the OMA scheme can achieve comparative performance with other two benchmarks, although the participating clients are not sufficient enough in this scheme. The reason is that it adopts the same design for client selection and resource allocation as our proposed FCEA scheme, which validates the effectiveness of the proposed FCEA scheme in improving HFL performance. Obviously, both the HFL performance and robustness decrease for the CIFAR-10 dataset, due to it is more complex than the MNIST dataset.

Fig. [9](#page-11-0) shows the HFL performance on both non-IID MNIST dataset and CIFAR-10 dataset. Note that for the non-IID CIFAR-10 dataset, we display the HFL performance using the maximum accuracy and minimum global loss to avoid overcrowding among different algorithms, which follows the same operation in [\[46\]. F](#page-13-45)rom Fig. [9\(a\)](#page-11-0) and Fig. [9\(b\),](#page-11-0) we observe that both the HFL performance and robustness drop a lot comparing with the figures in IID data distribution owing to the property of non-IID data. The proposed FCEA scheme is also able to realize better HFL performance regarding learning accuracy and global loss in comparison with other three schemes. This is because the client-edge association with multiple criteria is considered in our scheme, which is more beneficial for the improvement of HFL performance.

<span id="page-11-0"></span>![](_page_11_Figure_2.jpeg)

Fig. 9. Performance of HFL on non-IID data.

Nevertheless, in such non-IID data setting, the OMA scheme owns the worst HFL convergence performance, which shows the importance of sufficient training data in non-IID settings. Thus, the superiority of NOMA-enabled HFL system can be demonstrated.

#### *C. Performance of Average MS*

Fig. [10](#page-11-1) illustrates the performance of average MS value which is defined in [\(20\)](#page-5-3) versus global rounds over the above four schemes. It is obvious to find out that as HFL training round rises, the average MS figures of all schemes increase, while our proposed FCEA scheme achieves the lowest MS value in comparison with other schemes. This is because in our proposed FCEA scheme, the MS is regarded as one of the factors for client-edge association. Under this circumstance, the system average MS value can be guaranteed at a relatively low level, which is beneficial for the HFL convergence. Specifically, the low level average MS in HFL systems guarantees the local models to be fresh enough for model aggregation and more types of data can be utilized for HFL training especially in the scenarios with non-IID data distribution. In Fig. [10,](#page-11-1) we can also observe that the RCEA and GCEA schemes realize almost the same average MS value as HFL training. This is because in these two schemes, the MS is not considered in the design of client-edge association. Nevertheless, the average MS value of the OMA scheme increases more quickly in comparison with other three schemes because of the much less selected clients at each HFL round. Under this circumstance, the average MS cannot be guaranteed even considering this factor in the design of client-edge association.

<span id="page-11-1"></span>![](_page_11_Figure_7.jpeg)

<span id="page-11-2"></span>Fig. 10. Average MS of HFL system.

![](_page_11_Figure_9.jpeg)

Fig. 11. Convergence of DDPG training.

## *D. DDPG-Based Resource Allocation*

In this subsection, the performance of the DDPG-based resource allocation (DDPG-RA) algorithm is demonstrated given the FCEA scheme. For comparison, we consider four

<span id="page-12-1"></span>![](_page_12_Figure_2.jpeg)

![](_page_12_Figure_3.jpeg)

![](_page_12_Figure_4.jpeg)

Fig. 12. Performance of total cost.

benchmarks which are also under the FCEA scheme, including the random resource allocation (RRA) scheme, the fixed power allocation (FPA) scheme [\[20\], t](#page-13-19)he fixed computation allocation (FCA) scheme [\[21\]](#page-13-20) and the deep Q-learning network (DQN) based resource allocation (DQN-RA) scheme. More specifically, in the RRA scheme, the power and computation resource are allocated randomly for clients, while the power and computation frequency are fixed in the FPA scheme and the FCA scheme, respectively. In DQN-RA scheme, the resource allocation is achieved via DQN-based algorithm with the exploration of discrete action space. Note that the other variables in the benchmarks are optimized in the same way as the DDPG-RA algorithm to ensure the comparison fairness.

Fig. [11](#page-11-2) illustrates the convergence process of training our proposed DDPG-RA algorithm. It can be found that the convergence can be realized before 500 episodes. Note that we set the reward as a negative value during DDPG training because our objective is minimizing the total cost of our proposed HFL system while the training of DDPG aims to achieve the reward maximization.

In Fig. [12\(a\),](#page-12-1) the performance of average cost over five schemes is presented. As the training episode increases, the figures for all schemes except the RRA scheme have the gradual decreasing trend, which verifies the effectiveness of efficient resource allocation to the total cost reduction. Particularly, for the RRA scheme, both power and computation resource are allocated randomly without considering optimization, hence leading to the fluctuation of its figure. In the comparison with the FPA and FCA schemes, the proposed DDPG-RA scheme realizes better performance of total cost, which validates the superiority of the joint optimization of the power and computational resource allocation. Besides, the proposed DDPG-RA scheme still outperforms the DQN-RA scheme, this is because the DQN-RA scheme cannot accurately find the optimal resource allocation strategy due to the discrete action exploration. Nevertheless, the DDPG-RA scheme explores a continuous action space and takes a precise action, which finally obtains the optimal strategy and significantly reduces the total cost.

The performance of total cost versus different associated client numbers is shown in Fig. [12\(b\).](#page-12-1) Apparently, the increasing N<sup>m</sup> results in the growth of total cost, which can be explained from following two aspects. On the one hand, with the growth of Nm, the total energy consumption of the HFL system increases definitely. On the other hand, increasing N<sup>m</sup> causes severe straggler issue for the synchronous edge model aggregation, which also increases the total time consumption in the HFL system. Thus, combining these two aspects, the total system cost increases with the growth of Nm. In Fig. [12\(b\),](#page-12-1) we also find that our proposed DDPG-RA scheme always outperforms other schemes regarding the total cost minimization, which verifies the effectiveness of jointly optimizing transmit power and computational resources in the HFL system.

The performance of total cost versus the client n's local model size d<sup>n</sup> is illustrated in Fig. [12\(c\).](#page-12-1) The figure clearly shows that there is a rising trend for the total cost as d<sup>n</sup> increases. This is because the increasing d<sup>n</sup> results in the growth of wireless transmission time for the edge model aggregation, so that the corresponding energy consumption also increases. Compared with the benchmarks, our proposed algorithm always achieves the least total cost. Moreover, it is interesting to find that as d<sup>n</sup> increases, the increase in total cost for the proposed DDPG-RA scheme is much less than the increase for the other four schemes. It indicates that the DDPG-RA scheme is potential in dealing with large local models.

## VI. CONCLUSION

<span id="page-12-0"></span>In this paper, we studied the multi-criteria client selection and joint optimization of edge server scheduling and resource allocation in a NOMA enabled HFL system under semi-synchronous cloud model aggregation. The application of NOMA in HFL systems ensures the enhanced communication efficiency. We divided the system implementation into two phases, i.e., the client-edge phase and the edge-cloud phase, and formulated the corresponding time and energy cost, respectively. A fuzzy logic based client-edge association policy was first proposed to balance the client heterogeneity in multiple aspects. Then, we formulated the total cost minimization problem and decomposed it into edge scheduling and resource allocation two subproblems. The former subproblem was solved effectively through the PDD-based algorithm, and a closed-form solution of edge server scheduling was obtained. Considering the time-varying communication environment, we developed a DDPG-based algorithm to achieve efficient resource allocation among selected clients at each edge server. Through extensive simulation results, we demonstrated that the proposed schemes own superior performance in improving HFL performance and reducing total cost.

## REFERENCES

- <span id="page-13-0"></span>[\[1\] V](#page-0-0). C. Gogineni, S. Werner, F. Gauthier, Y. Huang, and A. Kuh, "Personalized online federated learning for IoT/CPS: Challenges and future directions," *IEEE Internet Things Mag.*, vol. 5, no. 4, pp. 78–84, Dec. 2022.
- <span id="page-13-1"></span>[\[2\] S](#page-0-1). Savazzi, M. Nicoli, M. Bennis, S. Kianoush, and L. Barbieri, "Opportunities of federated learning in connected, cooperative, and automated industrial systems," *IEEE Commun. Mag.*, vol. 59, no. 2, pp. 16–21, Feb. 2021.
- <span id="page-13-2"></span>[\[3\] K](#page-0-2). Bonawitz et al., "Towards federated learning at scale: System design," in *Proc. Mach. Learn. Syst.*, vol. 1, 2019, pp. 374–388.
- <span id="page-13-3"></span>[\[4\] M](#page-0-3). Chen et al., "Distributed learning in wireless networks: Recent progress and future challenges," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3579–3605, Dec. 2021.
- <span id="page-13-4"></span>[\[5\] S](#page-0-4). Wang et al., "Adaptive federated learning in resource constrained edge computing systems," *IEEE J. Sel. Areas Commun.*, vol. 37, no. 6, pp. 1205–1221, Jun. 2019.
- <span id="page-13-5"></span>[\[6\] L](#page-0-5). Liu, J. Zhang, S. H. Song, and K. B. Letaief, "Client-edge-cloud hierarchical federated learning," in *Proc. IEEE Int. Conf. Commun. (ICC)*, Jun. 2020, pp. 1–6.
- <span id="page-13-6"></span>[\[7\] Z](#page-1-0). Ding, X. Lei, G. K. Karagiannidis, R. Schober, J. Yuan, and V. K. Bhargava, "A survey on non-orthogonal multiple access for 5G networks: Research challenges and future trends," *IEEE J. Sel. Areas Commun.*, vol. 35, no. 10, pp. 2181–2195, Oct. 2017.
- <span id="page-13-7"></span>[\[8\] S](#page-1-1). Liu, G. Yu, R. Yin, and J. Yuan, "Adaptive network pruning for wireless federated learning," *IEEE Wireless Commun. Lett.*, vol. 10, no. 7, pp. 1572–1576, Jul. 2021.
- <span id="page-13-8"></span>[\[9\] H](#page-1-2). Sun, X. Ma, and R. Q. Hu, "Adaptive federated learning with gradient compression in uplink NOMA," *IEEE Trans. Veh. Technol.*, vol. 69, no. 12, pp. 16325–16329, Dec. 2020.
- <span id="page-13-9"></span>[\[10\]](#page-1-3) M. Zhang et al., "Communication-efficient federated edge learning via optimal probabilistic device scheduling," *IEEE Trans. Wireless Commun.*, vol. 21, no. 10, pp. 8536–8551, Oct. 2022.
- <span id="page-13-10"></span>[\[11\]](#page-1-4) B. Wu, F. Fang, and X. Wang, "Joint age-based client selection and resource allocation for communication-efficient federated learning over NOMA networks," *IEEE Trans. Commun.*, vol. 72, no. 1, pp. 179–192, Jan. 2024.
- <span id="page-13-11"></span>[\[12\]](#page-1-5) X. Deng et al., "Low-latency federated learning with DNN partition in distributed industrial IoT networks," *IEEE J. Sel. Areas Commun.*, vol. 41, no. 3, pp. 755–775, Mar. 2023.
- <span id="page-13-12"></span>[\[13\]](#page-1-6) C. Peng, Q. Hu, Z. Wang, R. W. Liu, and Z. Xiong, "Online-learningbased fast-convergent and energy-efficient device selection in federated edge learning," *IEEE Internet Things J.*, vol. 10, no. 6, pp. 5571–5582, Mar. 2023.
- <span id="page-13-13"></span>[\[14\]](#page-1-7) Y. Fraboni, R. Vidal, L. Kameni, and M. Lorenzi, "Clustered sampling: Low-variance and improved representativity for clients selection in federated learning," in *Proc. Int. Conf. Mach. Learn.*, vol. 139, M. Meila and T. Zhang, Eds. 2021, pp. 3407–3416.
- <span id="page-13-14"></span>[\[15\]](#page-1-8) T. T. Vu, D. T. Ngo, H. Q. Ngo, M. N. Dao, N. H. Tran, and R. H. Middleton, "Joint resource allocation to minimize execution time of federated learning in cell-free massive MIMO," *IEEE Internet Things J.*, vol. 9, no. 21, pp. 21736–21750, Nov. 2022.
- <span id="page-13-15"></span>[\[16\]](#page-1-9) R. Chen, D. Shi, X. Qin, D. Liu, M. Pan, and S. Cui, "Service delay minimization for federated learning over mobile devices," *IEEE J. Sel. Areas Commun.*, vol. 41, no. 4, pp. 990–1006, Apr. 2023.
- <span id="page-13-16"></span>[\[17\]](#page-1-10) M. Chen, H. V. Poor, W. Saad, and S. Cui, "Convergence time optimization for federated learning over wireless networks," *IEEE Trans. Wireless Commun.*, vol. 20, no. 4, pp. 2457–2471, Apr. 2021.
- <span id="page-13-17"></span>[\[18\]](#page-1-11) X. Zhou, Y. Deng, H. Xia, S. Wu, and M. Bennis, "Time-triggered federated learning over wireless networks," *IEEE Trans. Wireless Commun.*, vol. 21, no. 12, pp. 11066–11079, Dec. 2022.
- <span id="page-13-18"></span>[\[19\]](#page-1-12) M. Chen, Z. Yang, W. Saad, C. Yin, H. V. Poor, and S. Cui, "A joint learning and communications framework for federated learning over wireless networks," *IEEE Trans. Wireless Commun.*, vol. 20, no. 1, pp. 269–283, Jan. 2021.
- <span id="page-13-19"></span>[\[20\]](#page-1-13) B. Xu, W. Xia, W. Wen, P. Liu, H. Zhao, and H. Zhu, "Adaptive hierarchical federated learning over wireless networks," *IEEE Trans. Veh. Technol.*, vol. 71, no. 2, pp. 2070–2083, Feb. 2022.
- <span id="page-13-20"></span>[\[21\]](#page-1-14) W. Wen, Z. Chen, H. H. Yang, W. Xia, and T. Q. Quek, "Joint scheduling and resource allocation for hierarchical federated edge learning," *IEEE Trans. Wireless Commun.*, vol. 21, no. 8, pp. 5857–5872, Aug. 2022.
- <span id="page-13-21"></span>[\[22\]](#page-1-15) S. Luo, X. Chen, Q. Wu, Z. Zhou, and S. Yu, "HFEL: Joint edge association and resource allocation for cost-efficient hierarchical federated edge learning," *IEEE Trans. Wireless Commun.*, vol. 19, no. 10, pp. 6535–6548, Oct. 2020.

- <span id="page-13-22"></span>[\[23\]](#page-1-16) S. Liu, G. Yu, X. Chen, and M. Bennis, "Joint user association and resource allocation for wireless hierarchical federated learning with IID and non-IID data," *IEEE Trans. Wireless Commun.*, vol. 21, no. 10, pp. 7852–7866, Oct. 2022.
- <span id="page-13-23"></span>[\[24\]](#page-1-17) L. Liu, J. Zhang, S. Song, and K. B. Letaief, "Hierarchical federated learning with quantization: Convergence analysis and system design," *IEEE Trans. Wireless Commun.*, vol. 22, no. 1, pp. 2–18, Jan. 2022.
- <span id="page-13-24"></span>[\[25\]](#page-1-18) T. Zhao, F. Li, and L. He, "DRL-based joint resource allocation and device orchestration for hierarchical federated learning in NOMAenabled industrial IoT," *IEEE Trans. Ind. Informat.*, vol. 19, no. 6, pp. 7468–7479, Jun. 2023.
- <span id="page-13-25"></span>[\[26\]](#page-1-19) X. Wang, Y. Zhao, C. Qiu, Z. Liu, J. Nie, and V. C. M. Leung, "InFEDge: A blockchain-based incentive mechanism in hierarchical federated learning for end-edge-cloud communications," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 12, pp. 3325–3342, Dec. 2022.
- <span id="page-13-26"></span>[\[27\]](#page-1-20) Z. Su et al., "Secure and efficient federated learning for smart grid with edge-cloud collaboration," *IEEE Trans. Ind. Informat.*, vol. 18, no. 2, pp. 1333–1344, Feb. 2022.
- <span id="page-13-27"></span>[\[28\]](#page-1-21) W. Zhang et al., "Optimizing federated learning in distributed industrial IoT: A multi-agent approach," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3688–3703, Dec. 2021.
- <span id="page-13-28"></span>[\[29\]](#page-2-3) Z. Yang, M. Chen, W. Saad, C. S. Hong, and M. Shikh-Bahaei, "Energy efficient federated learning over wireless communication networks," *IEEE Trans. Wireless Commun.*, vol. 20, no. 3, pp. 1935–1949, Mar. 2020.
- <span id="page-13-29"></span>[\[30\]](#page-3-0) Y. Arjevani and O. Shamir, "Communication complexity of distributed convex learning and optimization," in *Proc. Adv. Neural Inf. Process. Syst.*, vol. 28, 2015, pp. 1–9.
- <span id="page-13-30"></span>[\[31\]](#page-3-1) T. D. Burd and R. W. Brodersen, "Processor design for portable systems," *J. VLSI Signal Process. Syst. Signal, Image Video Technol.*, vol. 13, nos. 2–3, pp. 203–221, 1996.
- <span id="page-13-31"></span>[\[32\]](#page-3-2) F. Fang, B. Wu, S. Fu, Z. Ding, and X. Wang, "Energy-efficient design of STAR-RIS aided MIMO-NOMA networks," *IEEE Trans. Commun.*, vol. 71, no. 1, pp. 498–511, Jan. 2023.
- <span id="page-13-32"></span>[\[33\]](#page-3-3) W. Ni, Y. Liu, Z. Yang, H. Tian, and X. Shen, "Integrating overthe-air federated learning and non-orthogonal multiple access: What role can RIS play?" *IEEE Trans. Wireless Commun.*, vol. 21, no. 12, pp. 10083–10099, Dec. 2022.
- <span id="page-13-33"></span>[\[34\]](#page-3-4) C. Ma et al., "Distributed optimization with arbitrary local solvers," *Optim. Methods Softw.*, vol. 32, no. 4, pp. 813–848, 2017.
- <span id="page-13-34"></span>[\[35\]](#page-5-4) T. J. Ross, *Fuzzy Logic With Engineering Applications*. Hoboken, NJ, USA: Wiley, 2009.
- <span id="page-13-35"></span>[\[36\]](#page-5-5) W. Dai, Y. Zhou, N. Dong, H. Zhang, and E. P. Xing, "Toward understanding the impact of staleness in distributed machine learning," 2018, *arXiv:1810.03264*.
- <span id="page-13-36"></span>[\[37\]](#page-6-9) C. Wu, S. Ohzahata, and T. Kato, "VANET broadcast protocol based on fuzzy logic and lightweight retransmission mechanism," *IEICE Trans. Commun.*, vol. 95, no. 2, pp. 415–425, Feb. 2012.
- <span id="page-13-37"></span>[\[38\]](#page-6-10) N. Cha et al., "Fuzzy logic based client selection for federated learning in vehicular networks," *IEEE Open J. Comput. Soc.*, vol. 3, pp. 39–50, 2022.
- <span id="page-13-38"></span>[\[39\]](#page-7-15) Q. Shi and M. Hong, "Penalty dual decomposition method for nonsmooth nonconvex optimization—Part I: Algorithms and convergence analysis," *IEEE Trans. Signal Process.*, vol. 68, pp. 4108–4122, 2020.
- <span id="page-13-39"></span>[\[40\]](#page-7-16) R. Guo, Y. Cai, M. Zhao, Q. Shi, B. Champagne, and L. Hanzo, "Joint design of beam selection and precoding matrices for mmWave MU-MIMO systems relying on lens antenna arrays," *IEEE J. Sel. Topics Signal Process.*, vol. 12, no. 2, pp. 313–325, May 2018.
- <span id="page-13-40"></span>[\[41\]](#page-8-5) Y. Guo, F. Fang, D. Cai, and Z. Ding, "Energy-efficient design for a NOMA assisted STAR-RIS network with deep reinforcement learning," *IEEE Trans. Veh. Technol.*, vol. 72, no. 4, pp. 5424–5428, Apr. 2023.
- <span id="page-13-41"></span>[\[42\]](#page-8-6) S. Fu, X. Feng, A. Sultana, and L. Zhao, "Joint power allocation and 3D deployment for UAV-BSs: A game theory based deep reinforcement learning approach," *IEEE Trans. Wireless Commun.*, vol. 23, no. 1, pp. 736–748, Jan. 2024.
- <span id="page-13-42"></span>[\[43\]](#page-8-7) T. P. Lillicrap et al., "Continuous control with deep reinforcement learning," 2015, *arXiv:1509.02971*.
- <span id="page-13-43"></span>[\[44\]](#page-9-6) Y. He, M. Yang, Z. He, and M. Guizani, "Computation offloading and resource allocation based on DT-MEC-assisted federated learning framework," *IEEE Trans. Cognit. Commun. Netw.*, vol. 9, no. 6, pp. 1707–1720, Dec. 2023.
- <span id="page-13-44"></span>[\[45\]](#page-9-7) Y. Zhao, M. Li, L. Lai, N. Suda, D. Civin, and V. Chandra, "Federated learning with non-IID data," 2018, *arXiv:1806.00582*.
- <span id="page-13-45"></span>[\[46\]](#page-9-8) K. Wang, Z. Ding, D. K. C. So, and Z. Ding, "Age-of-information minimization in federated learning based networks with non-IID dataset," *IEEE Trans. Wireless Commun*, pp. 1–15, Jan. 2024, doi: [10.1109/TWC.2024.3357208.](http://dx.doi.org/10.1109/TWC.2024.3357208)

![](_page_14_Picture_2.jpeg)

Bibo Wu (Graduate Student Member, IEEE) received the B.E. degree in electronic information engineering and the M.E. degree in information and communication engineering from Chongqing University, Chongqing, China, in 2019 and 2022, respectively. He is currently pursuing the Ph.D. degree with the Department of Electrical and Computer Engineering, Western University, Canada. His current research interests include federated learning, non-orthogonal multiple access (NOMA), and machine learning for intelligent wireless communications.

![](_page_14_Picture_4.jpeg)

Donghong Cai (Member, IEEE) received the Ph.D. degree from Southwest Jiaotong University in 2020. From October 2017 to October 2018, he was a Visiting Ph.D. Student with Lancaster University and The University of Manchester, U.K. He is currently a Lecturer with the College of Information Science and Technology/College of Cyber Security, Jinan University, Guangzhou, China. His current research interests include signal detection, security coding, the distributed Internet of Things, privacy preservation, semantic communication, and non-orthogonal

multiple access. He is the General Chair of the 12th EAI International Conference on Game Theory for Networks (GameNets 2023). He serves as the Guest Editor for *Physical Communication* and *Electronics*.

![](_page_14_Picture_7.jpeg)

Fang Fang (Senior Member, IEEE) received the Ph.D. degree in electrical engineering from The University of British Columbia (UBC), Canada. She is currently an Assistant Professor with the Department of Electrical and Computer Engineering and the Department of Computer Science, Western University, Canada. Her current research interests include machine learning for intelligent wireless communications, non-orthogonal multiple access (NOMA), reconfigurable intelligent surface (RIS), multi-access edge computing (MEC), semantic communications,

and edge AI. She received the Exemplary Reviewer Certificates from IEEE TRANSACTIONS ON COMMUNICATIONS in 2017 and 2021 as well as the Exemplary Editor Certificates from IEEE OPEN JOURNAL OF THE COMMU-NICATIONS SOCIETY in 2021 and 2023. She received the IEEE SPCC Early Achievement Award in 2023. She has been serving as the General Chair for EAI GameNets 2022, the Publications Chair for IEEE VTC 2023 Fall, and the Symposium Chair for IEEE GLOBECOM 2023, IEEE VTC 2024 Spring, and IEEE ICC 2025. She serves as an Editor for IEEE COMMUNICATION LETTERS and IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY.

![](_page_14_Picture_10.jpeg)

Shu Fu (Member, IEEE) received the Ph.D. degree in communication and information systems from the University of Electronic Science and Technology of China, Chengdu, China, in June 2016, with a focus on resource allocation in wireless networks and wavelength division multiplexing (WDM)-based optical networks. He is currently a Professor with the School of Microelectronics and Communication Engineering, Chongqing University, Chongqing, China. His research interests include the next generation of wireless networks, integrated networks, and artificial intelligence.

![](_page_14_Picture_12.jpeg)

Xianbin Wang (Fellow, IEEE) received the Ph.D. degree in electrical and computer engineering from the National University of Singapore in 2001.

He is currently a Professor and a Tier-1 Canada Research Chair in 5G and Wireless IoT Communications with Western University, Canada. Before joining Western University, he was with the Communications Research Centre Canada as a Research Scientist/Senior Research Scientist from 2002 to 2007. From 2001 to 2002, he was a System Designer with STMicroelectronics. He has over 600 highly

cited journals and conference papers, in addition to over 30 granted and pending patents and several standard contributions. His current research interests include 5G/6G technologies, the Internet of Things, machine learning, communications security, and intelligent communications.

Dr. Wang is a fellow of the Canadian Academy of Engineering and a fellow of the Engineering Institute of Canada. He has received many prestigious awards and recognitions, including the IEEE Canada R. A. Fessenden Award, Canada Research Chair, the Engineering Research Excellence Award from Western University, the Canadian Federal Government Public Service Award, Ontario Early Researcher Award, and nine best paper awards. He was involved in many IEEE conferences, including GLOBECOM, ICC, VTC, PIMRC, WCNC, CCECE, and CWIT, in different roles, such as the general chair, the TPC chair, the symposium chair, a tutorial instructor, the track chair, the session chair, and a keynote speaker. He was the Chair of the IEEE ComSoc Signal Processing and Computing for Communications (SPCC) Technical Committee. He is serving as the Central Area Chair of IEEE Canada. He serves/has served as the Editor-in-Chief, the Associate Editorin-Chief, and an editor/associate editor for over ten journals.

![](_page_14_Picture_17.jpeg)

Zhiguo Ding (Fellow, IEEE) received the B.Eng. degree from Beijing University of Posts and Telecommunications in 2000 and the Ph.D. degree from Imperial College London in 2005.

He has also been affiliated with The University of Manchester and Princeton University. He is currently a Professor of communications with Khalifa University. His research interests include 6G networks, multiple access, energy harvesting networks, and statistical signal processing. He recently received the EU Marie Curie Fellowship 2012–2014, the

Top IEEE TVT Editor 2017, the IEEE Heinrich Hertz Award in 2018, the IEEE Jack Neubauer Memorial Award in 2018, the IEEE Best Signal Processing Letter Award in 2018, the Friedrich Wilhelm Bessel Research Award in 2020, and the IEEE SPCC Technical Recognition Award in 2021. From 2013 to 2016, he was an Editor of IEEE WIRELESS COM-MUNICATION LETTERS, IEEE TRANSACTIONS ON COMMUNICATIONS, and IEEE COMMUNICATION LETTERS. He is serving as an Area Editor for IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS and IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY and an Editor for IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY. He is a Distinguished Lecturer of IEEE ComSoc. He was a Web of Science Highly Cited Researcher in two categories in 2022.
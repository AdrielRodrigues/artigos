# <span id="page-0-0"></span>Hybrid Hierarchical Federated Learning Over 5G/NextG Wireless Networking

Haiyun Liu<sup>®</sup>, Student Member, IEEE, Jiahao Xue<sup>®</sup>, Student Member, IEEE, Jie Xu<sup>®</sup>, Yao Liu, Senior Member, IEEE, and Zhuo Lu<sup>®</sup>, Senior Member, IEEE

Abstract—Today's 5G and NextG wireless networks are moving toward using the coordinated multi-point (CoMP) transmission and reception technique, where a client can be simultaneously served by multiple base stations (BSs) for better communication performance. However, traditional hierarchical federated learning (HFL) architectures impose the constraint that each client can be associated with only one edge server (ES) at a time. If we keep using the traditional HFL architectures in modern hierarchical networks for model training, the benefits of the CoMP technique would remain unexploited and leave room for further improvements in training efficiency. To address this issue, we propose hybrid hierarchical federated learning (HHFL), which allows clients in overlapping regions to simultaneously communicate with multiple edge servers (ESs) for model aggregation. HHFL is able to enhance inter-ES knowledge sharing, thereby mitigating model divergence and improving training efficiency. We provide a rigorous theoretical convergence analysis with a convergence upper bound to validate its effectiveness. Experimental results show that HHFL outperforms traditional HFL, particularly when the data across different ESs is not independent and identically distributed (non-IID). For example, when each ES is dominated by only two of the ten classes and 15 out of the 57 clients can connect to multiple ESs, HHFL achieves up to  $2\times$  faster convergence under the same configuration. These results demonstrate that HHFL provides a scalable and efficient solution for FL model training in today's and NextG wireless networks.

*Index Terms*—Federated learning (FL), hierarchical federated learning (HFL), multi-server, training efficiency.

#### I. INTRODUCTION

EDERATED learning (FL) in wireless networking is able to effectively utilize data locally stored by wireless users for machine learning tasks with data privacy [1], [2], [3]. In real-world applications, the design of the FL architecture, which

Received 4 September 2025; revised 3 March 2026; accepted 2 April 2026. Date of publication 7 April 2026; date of current version 2 September 2026. The work was supported in part by NSF through USF under Grant 2321270, Grant 2319781, and Grant 2433888 and in part by UF under Grant 2433886 Grant 2505381, and Grant 2515982. Recommended for acceptance by S. Abadal. (corresponding author: Zhuo Lu.)

Haiyun Liu and Yao Liu are with the Department of Computer Science and Engineering, University of South Florida, Tampa, FL 33620 USA (e-mail: haiyunliu@usf.edu; yliu21@usf.edu).

Jie Xu is with the Department of Electrical and Computer Engineering, University of Florida, Gainesville, FL 32611 USA (e-mail: jie.xu@ufl.edu).

Jiahao Xue and Zhuo Lu are with the Department of Electrical Engineering, University of South Florida, Tampa, FL 33620 USA (e-mail: jiahao@usf.edu; zhuolu@usf.edu).

This article has supplementary downloadable material available at https://doi.org/10.1109/TMC.2026.3681750, provided by the authors.

Digital Object Identifier 10.1109/TMC.2026.3681750

![](_page_0_Figure_14.jpeg)

Fig. 1. The traditional HFL architecture and our proposed architecture.

defines how clients and servers communicate and collaborate during the learning process, must account for the network topology, which describes how devices are physically or logically connected within the wireless system, as their alignment directly impacts training effectiveness and efficiency.

In small-scale wireless networks, the star network topology is widely adopted, where a centralized server device directly connects to multiple distributed client devices to finish a training task [4], [5], [6], [7], [8]. As networks continue to expand and become increasingly complex, as exemplified by the Internet of Things (IoT), large-scale vehicular networks (V2X), and edgecloud computing frameworks, the escalating demands for communication and computation often exceed the capacity of a single server device. To address these challenges, the hierarchical network topology is employed, where intermediate-layer servers are designed to reduce the load on the previously centralized server [9], [10], [11]. To fit this common topology, hierarchical federated learning (HFL) has been proposed, as illustrated in Fig. 1(a). In this architecture, training proceeds periodically. The cloud server (CS) disseminates the global model to all edge servers (ESs), which broadcast it to their clients for initialization. Clients perform local updates and upload their models to the connectable ES(s) for aggregation; the aggregated ES model is then broadcast back to clients. After several client–ES rounds, ESs upload their models to the CS for aggregation to update the global model.

As user demands for high data rates, low latency, and strong reliability continue to grow, the multi-point connection mode, i.e., coordinated multi-point (CoMP), has been proposed as a more advanced alternative to the traditional single-point approach in hierarchical network architectures [12], [13]. In this mode, clients can concurrently connect to multiple intermediate-layer base stations (BSs, which correspond to ESs in FL), which better utilizes network resources and enhances

1536-1233 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

communication performance. This connection mode has already seen widespread adoption in 5G networks and is expected to play an even more critical role in the development of 6G [14], [15], [16], [17], [18], [19]. Theoretically, we could continue using the traditional HFL architecture in today's and future hierarchical networks that support CoMP. In this case, each client is assigned to communicate with a single BS, either randomly or based on specific communication parameters such as received signal strength (RSS). However, this design does not fully harness the advantages of multi-point mode to benefit FL training. In particular, under the HFL framework, the models of different ESs perform updates in isolation for extended periods between two consecutive aggregations at the CS; their updated models tend to accumulate biases from heterogeneous local gradients and drift toward localized optima. This inconsistency hinders global convergence, especially when the data distribution across ESs is not independent and identically distributed (non-IID).

To address this issue, we propose a novel hybrid hierarchical federated learning (HHFL) architecture, illustrated in Fig. 1(b). In HHFL, each client obtains the model parameters from its connected ESs and aggregates them via simple arithmetic averaging (i.e., summing the received models and dividing by the number of connected ESs). The client then performs local updates and periodically uploads the updated models back to the connected ESs for further aggregation. After a fixed number of aggregations, the ESs transmit their aggregated models to the CS for further aggregation, resulting in an updated global model. Then, this global model is sent back to the ESs. Compared to traditional HFL, a distinct advantage of HHFL is that each client in overlapping areas functions as a knowledge bridge between neighboring ESs. Specifically, by aggregating models from multiple neighboring ESs and subsequently uploading the updated model to all associated servers, the client effectively fuses knowledge derived from distinct ESs and propagates this fused knowledge across cell boundaries. As a result, clients under a given ES can indirectly benefit from knowledge carried by clients covered by other ESs, which mitigates overly localized model updates at the ES level, makes the aggregated updates more consistent with the global optimization objective, and ultimately accelerates convergence.

Through the rigorous analysis presented in Section IV-A, we demonstrate that HHFL achieves effective convergence as training progresses, with its convergence upper bound formally established therein. The experimental results in Section V show that when the data distribution across ESs is non-IID and some clients are located in overlapping regions covered by multiple ESs, HHFL exhibits a faster convergence speed compared to traditional HFL. Specifically, in a representative case where the data held by each ES is dominated by only two out of the ten classes, and 15 out of the 57 clients are located in overlapping regions, HHFL achieves approximately a 100% improvement in convergence efficiency over traditional HFL. Our contributions are as follows.

 We propose the novel HHFL architecture based on the CoMP technology. This architecture enables clients located in overlapping areas to act as bridges and facilitates knowledge sharing across ESs.

- We provide a rigorous theoretical convergence analysis of HHFL, and discuss its practical deployment considerations to confirm its feasibility in modern 5G/NextG networks.
- 3) We conduct extensive experiments to demonstrate the superior efficiency of HHFL over traditional HFL.

The rest of this paper is organized as follows: Section II introduces the preliminaries of FL. Section III introduces the HHFL architecture in detail, along with a well-designed algorithm. Section IV analyzes the performance of our HHFL architecture. Section V conducts experimental simulations to validate the high efficiency of HHFL. Section VI summarizes related works, followed by the conclusion in Section VII.

### II. PRELIMINARIES AND MODELS

In this section, we briefly introduce the classical FL architectures and their corresponding algorithms.

#### A. Basic FL Architecture

A basic FL architecture includes K participating clients that directly communicate with a CS that enables collaborative model training by aggregating locally computed updates from all clients [20], [21], [22], [23], [24]. Specifically, in each communication round, the CS broadcasts the current global model to clients. Each client then performs local training based on its private data for E steps to get the model update. Finally, each client returns its update to the CS, which aggregates these model updates to refine the global model and send them in the next round.

One of the most representative algorithms for this basic architecture is *FedAvg* [20], in which the CS updates the global model by computing a weighted average of the client models.

Formally, let t denote the index of local update steps, and  $t_0$  be the starting step of a communication round. Then, the FedAvg algorithm proceeds iteratively as follows:

- 1) The CS broadcasts the current global model  $w^{t_0}$  to all K clients, and each client i initializes its local model as  $w_i^{t_0} = w^{t_0}$ .
- 2) Each client i performs E steps of local updates as:

$$w_i^{t_0+e+1} = w_i^{t_0+e} - \eta_{t_0+e} \nabla F_i(w_i^{t_0+e}), \qquad (1)$$

where  $e=0,\ldots,E-1,$   $\eta_{t_0+e}$  is the learning rate at step  $t_0+e,$  and  $F_i(w_i^{t_0+e})$  is the average loss of client i with respect to its local model  $w_i^{t_0+e}.$  After E local updates, the model of client i becomes  $w_i^{t_0+E}.$ 

3) The CS aggregates all the client models to get an updated global model as:

$$w^{t_0+E} = \sum_{i=1}^{K} p_i w_i^{t_0+E}.$$
 (2)

where  $p_i$  denotes the proportion of data held by client i relative to the total amount of data across all clients.

These three procedures are repeated until either a predefined number of communication rounds is reached or the model meets a specified convergence criterion.

#### <span id="page-2-0"></span>B. The HFL Architecture

As communication networks scale and user demands continue to grow, the basic architecture of FL increasingly falls short of meeting practical requirements. To address these issues, the HFL architecture has been introduced [25]. Unlike the basic client-server setup, HFL places ESs between clients and the CS, forming a multi-layer structure of client-ES-CS, as shown in Fig. 1(a). In each global communication round, the global model is first transmitted from the CS to all ESs, which then forward it to their respective clients. Upon receiving the model, each client performs E steps of local updates and sends the updated model to its associated ES for *edge aggregation*. Each ES performs E rounds of edge aggregation with its connected clients. Finally, the updated models from all ESs are sent back to the CS, which performs *cloud aggregation* to update the global model.

A representative HFL algorithm is Hier-FedAvg, which extends the classical FedAvg algorithm to the multilayer setting [25]. Suppose there are N ESs, denoted by  $ES_1, ES_2, \ldots, ES_N$ . For each  $ES_n$ , let  $C_n$  denote the set of indices of all clients that it covers. Similarly, for each client i with  $i \in \{1, \ldots, K\}$ , let  $S_i$  denote the indices of ES to which client i can connect to. Then, the Hier-FedAvg algorithm proceeds iteratively as follows:

- 1) CS broadcasts its global model  $w^{t_0}$  to all ESs, and each  $ES_n$  sets its current model  $w_{(n)}^{t_0}$  to  $w^{t_0}$ .
- 2) Each client *i* initializes its model as:

$$w_i^{t_0} = w_{(S_i)}^{t_0}. (3)$$

3) Each client i performs E steps of local updates as:

$$w_i^{t_0+e+1} = w_i^{t_0+e} - \eta_{t_0+e} \nabla F_i(w_i^{t_0+e}). \tag{4}$$

After E local updates, the model of client i is  $w_i^{t_0+E}$ .

4) Each client i sends its model  $w_i^{t_0+E}$  to the connected ES for edge aggregation. For each  $ES_n$ , its aggregated model is as:

$$w_{(n)}^{t_0+E} = \sum_{i \in C_n} \frac{N_i}{N_n} w_i^{t_0+E}, \tag{5}$$

where  $N_i$  is the number of local data held by client i, and  $N_n = \sum_{i \in C_n} N_i$  is the number of data covered by  $ES_n$ .

5) After repeating 2), 3), and 4) for G rounds, each  $ES_n$  sends its model to CS for cloud aggregation. Then, the updated global model is as:

$$w^{t_0 + GE} = \sum_{i=1}^{N} \frac{N_n}{N_{total}} w_{(n)}^{t_0 + GE}.$$
 (6)

where  $N_{total} = \sum_{n=1}^{N} N_n$  is the number of data covered by all ESs

These procedures are repeated until either a specified number of training steps is reached or the model meets a specified convergence criterion.

![](_page_2_Picture_18.jpeg)

Fig. 2. Coordinated multi-point technique.

#### III. ARCHITECTURE DESIGN

In this section, we first present the motivation behind our HHFL architecture and describe the overall design. Then, we design the algorithm for this architecture.

#### A. Motivation and Architecture Design

With the increasing densification of wireless infrastructures and the growing demand for seamless coverage in 5G and NextG communication systems, overlapping regions among BSs have become increasingly common [26], [27], [28], [29]. The coordinated multi-point (CoMP) transmission and reception technique has been proposed [30] as an enhanced technique over traditional signal-point model (i.e., a client can communicate with only one BS). As shown in Fig. 2, compared to the traditional single-point mode, CoMP allows a client to simultaneously transmit to and receive data from multiple BSs, thereby enhancing system performance by improving spectral efficiency, reducing inter-cell interference, and significantly boosting the quality of service for users [30], [31], [32], [33]. CoMP has been widely adopted in the 5G era and is expected to play an even more significant role in NextG networks [32], [33], [34], [35].

Although some existing studies on HFL have considered making use of the overlapping regions and allow clients to be associated with multiple ESs, such as enabling dynamic edge association [36], leveraging statistical similarities across clients [37], optimizing staleness-aware aggregation schedules [38], analyzing security implications of multi-edge connectivity [39], or modeling asynchronous communication and dynamic client–ES interactions [40], they essentially still follow the conventional HFL paradigm, where multi-connectivity in a CoMP-capable network is not utilized.

To address this under-utilization, we propose the new HHFL to effectively leverage the CoMP technique to benefit the FL training. Specifically, the FL training runs in a hybrid mode: for those clients located in overlapping regions, they are able to simultaneously communicate with multiple ESs through CoMP techniques. In contrast, clients that fall within the coverage of only a single ES still communicate with the ES alone. In each global communication round, the CS first disseminates the global model to all ESs. Then, each ES transmits its current model to the clients within its coverage to initialize their local

<span id="page-3-0"></span>models. For clients in any overlapping area, CoMP-coordinated scheduling (CoMP-CS) allocates frequency-orthogonal physical resource blocks (PRBs) to their accessible ESs via the Xn interface (a standard interface for inter-BS/ES communication) for downlink transmission. This mechanism prevents inter-cell interference, enabling the simultaneous reception of multiple models. Upon receiving these models, the clients in overlapping areas perform client aggregation to initialize their local models. Next, each client conducts local training for E steps and uploads its updated model to all associated ESs for edge aggregation. For each client in the overlapping area, a single uplink transmission of its local model can be received and processed in parallel by multiple ESs via CoMP-capable uplink multi-point reception. Meanwhile, different clients in the same area are scheduled on frequency-orthogonal PRBs to avoid mutual interference. After G rounds of edge aggregation, each ES sends its current model to the CS for cloud aggregation, which updates the global model.

It is worth noting that employing CoMP inevitably introduces additional synchronization requirements, which increase implementation complexity. Nevertheless, our proposed HHFL architecture mitigates these costs through a lightweight and practical CoMP design. Specifically, rather than relying on traditional CoMP joint reception, multiple ESs independently receive and process the uplink data transmitted by the same client. This bypasses the need for complex inter-BS cooperation, such as coherent joint decoding or soft combining, which typically necessitates stringent sub-symbol phase synchronization and heavy backhaul data exchange. Moreover, other fundamental synchronization requirements, such as basic frame and slot timing alignment to absorb marginal propagation delays, strictly align with standard network operations. These macro-level synchronization mechanisms are inherently mandated in all modern cellular systems to maintain basic connectivity and prevent cross-link interference, meaning our architecture successfully accommodates multi-point reception without imposing the prohibitive physical-layer synchronization overheads typically associated with traditional CoMP. Finally, to avoid the latency of per-round dynamic negotiation among ESs for allocating PRBs to the clients in overlapping areas, HHFL exploits the inherently predictable and periodic traffic patterns of FL. Because the model payload size remains constant and uploads occur at regular intervals (i.e., exactly after E local updates), the network can leverage 5G configured grants (CG) [41] to pre-allocate periodic uplink resources, effectively bypassing dynamic resource requests.

Building upon this practical multi-connectivity communication foundation, from an algorithmic perspective, HHFL differs from traditional HFL in that it involves two levels of aggregation: client aggregation and edge aggregation. Together, these mechanisms allow clients located in overlapping areas to act as knowledge bridges between neighboring ESs. Specifically, by aggregating models from multiple ESs, these clients fuse knowledge derived from distinct ESs; subsequently, by uploading their locally trained updates back to all associated ESs, they propagate this fused knowledge across cell boundaries. This mechanism enables clients under a given ES to indirectly benefit from data distributions predominantly located in neighboring

ES coverage areas, thereby mitigating overly localized model updates at the ES level. When ES-level non-IID is pronounced, this extra inter-ES sharing makes their aggregated updates more consistent with the global optimization direction, thereby accelerating convergence.

### B. HHFL Algorithm Design

Let  $S_i$  denote the set of indices of all ESs that client i can connect to, rather than a single ES as previously defined. Similar to the Hier-FedAvg algorithm for HFL described in Section II-B, our HHFL algorithm operates iteratively:

- 1) CS broadcasts the global model  $w^{t_0}$  to all ESs, and each  $ES_n$  sets its current model parameter  $w_{(n)}^{t_0}$  to  $w^{t_0}$ .
- 2) Each client *i* executes client aggregation to initialize its client model as:

$$w_i^{t_0} = \frac{1}{|S_i|} \sum_{n \in S_i} w_{(n)}^{t_0}, \tag{7}$$

where  $|S_i|$  is the number of elements in set  $S_i$ .

3) Each client i performs E steps of local updates as:

$$w_i^{t_0+e+1} = w_i^{t_0+e} - \eta_{t_0+e} \nabla F_i(w_i^{t_0+e}).$$
 (8)

After E local updates, the model of client i is  $\boldsymbol{w}_i^{t_0+E}$ .

4) Each client i sends its model  $w_i^{t_0+E}$  to the ESs it can connect to for edge aggregation. For each  $ES_n$ , its aggregated model is as:

$$w_{(n)}^{t_0+E} = \sum_{i \in C} \frac{1}{\langle n_i} \frac{p_i}{|S_i|} w_i^{t_0+E}, \tag{9}$$

where  $\Diamond_n$  is determined by

$$\Diamond_n = \sum_{i \in C} \frac{p_i}{|S_i|}.$$
 (10)

5) After repeating procedures 2), 3), and 4) for G rounds, each  $ES_n$  sends its model to CS for cloud aggregation. Then, the updated global model is as:

$$w^{t+GE} = \sum_{n=1}^{N} \Diamond_n w_{(n)}^{t+GE}.$$
 (11)

These procedures will be repeated until either the specified overall training steps are reached or the model meets a specified convergence criterion. The pseudo-code of the algorithm is shown in Algorithm 1.

## IV. PERFORMANCE ANALYSIS

In this section, we analyze the convergence properties of the HHFL architecture and derive an upper bound on its convergence to demonstrate its effectiveness. Then, we compare the proposed architecture with the traditional HFL architecture to demonstrate its efficiency advantages.

## A. Convergence Analysis

1) Evolution Path of Client Models: In the HHFL architecture, the global model is closely related to the local models

## <span id="page-4-0"></span>Algorithm 1: The Proposed HHFL Algorithm.

```
1: Input: Initialized parameter w^0 and total training steps
 2: Output: Final global parameter w^T
 3: Set w_i^0 = w^0 for all clients i = 1, ..., K
 4: for t = 0, 1, \dots, T - 1 do
       for all client i = 1, ..., K in parallel do
          v_i^{t+1} = w_i^t - \eta_t \nabla F_i(w_i^t) // Model after one local
 7:
       end for
       if E \nmid t+1 then
 9:
          for all client i = 1, ..., K in parallel do
             w_i^{t+1} = v_i^{t+1}
10:
11:
          end for
12:
       end if
13:
       if E \mid t+1 then
          for all edge server ES_n, n=1,...,N in parallel do
14:
            w_{(n)}^{t+1} = \sum_{i \in C_n} \frac{1}{\lozenge_n} \frac{p_i}{|S_i|} v_i^{t+1} // Edge aggregation
15:
16:
          if GE \mid t+1 then
17:
            w^{t+1} = \sum_{n=1}^{N} \lozenge_n w_{(n)}^{t+1} // Cloud aggregation for all edge server ES_n with n=1,\ldots,N in
18:
19:
               w_{(n)}^{t+1} = w^{t+1} // CS broadcasts its parameter to
20:
21:
            end for
22:
          end if
          for all client i=1,...,K in parallel do w_i^{t+1}=\frac{1}{|S_i|}\sum_{n\in S_i}w_{(n)}^{t+1} // Client aggregation
23:
24:
25:
26: end if
27: end for
28: w^T = \sum_{n=1}^N (\lozenge_n \sum_{i \in C_n} \frac{1}{\lozenge_n} \frac{p_i}{|S_i|} w_i^T) // Final global
     parameter obtained through edge aggregations and cloud
     aggregation for all client models at step T.
```

maintained by individual clients. To investigate whether and how the global model converges as training progresses, we first need to understand how client models evolve after every local update. We use the state vectors  $\mathbf{w}^t = [w_1^t, \dots, w_K^t]^\top$  and  $\mathbf{w}^{t+1} = [w_1^{t+1}, \dots, w_K^{t+1}]^\top$  to represent the collection of local models of all clients at step t and step t+1, respectively. Next, we analyze the evolution path from  $\mathbf{w}^t$  to  $\mathbf{w}^{t+1}$ , denoted by  $\mathbf{w}^t \to \mathbf{w}^{t+1}$ .

We first introduce an intermediate state vector  $\mathbf{v}^{t+1} = [v_1^{t+1}, \dots, v_K^{t+1}]^{\top}$ . This vector represents the collection of all clients' local updates at step t, obtained immediately after local training and before aggregation (if any). Then, we can decompose the evolution path  $\mathbf{w}^t \to \mathbf{w}^{t+1}$  into two successive transitions:  $\mathbf{w}^t \to \mathbf{v}^{t+1}$  (local training) and  $\mathbf{v}^{t+1} \to \mathbf{w}^{t+1}$  (aggregation, if performed). This decomposition enables us to examine the effects of computation and aggregation separately, providing a clearer view of how model evolves during training. In other words, understanding the evolution  $\mathbf{w}^t \to \mathbf{w}^{t+1}$  requires analyzing both  $\mathbf{w}^t \to \mathbf{v}^{t+1}$  and  $\mathbf{v}^{t+1} \to \mathbf{w}^{t+1}$ .

Since  $v_i^{t+1}$  is obtained by client i after one local update based on the model  $w_i^t$ , we have:

$$v_i^{t+1} = w_i^t - \eta_t \nabla F_i(w_i^t), \tag{12}$$

which characterizes the first transition  $\mathbf{w}^t \to \mathbf{v}^{t+1}$ . For the transition  $\mathbf{v}^{t+1} \to \mathbf{w}^{t+1}$ , we analyze the process under three distinct cases based on the value of step t+1:

Case 1:  $E \nmid t+1$ . At this step, there is no any aggregation, and we have

$$w_i^{t+1} = v_i^{t+1}. (13)$$

Case 2:  $EG \mid t+1$ . At this step, edge aggregation, cloud aggregation, and client aggregation perform sequentially. Then, we have

$$w_{i}^{t+1} \stackrel{(a)}{=} \frac{1}{|S_{i}|} \sum_{n \in S_{i}} w_{(n)}^{t+1} \stackrel{(b)}{=} \frac{1}{|S_{i}|} \sum_{n \in S_{i}} w^{t+1} = w^{t+1}$$

$$\stackrel{(c)}{=} \sum_{n=1}^{N} \lozenge_{n} w_{(n)}^{t+1} \stackrel{(d)}{=} \sum_{n=1}^{N} \left( \lozenge_{n} \sum_{i \in C_{n}} \frac{1}{\lozenge_{n}} \frac{p_{i}}{|S_{i}|} v_{i}^{t+1} \right)$$

$$= \sum_{n=1}^{N} \sum_{i \in C_{n}} \frac{p_{i}}{|S_{i}|} v_{i}^{t+1}$$

$$= \sum_{i \in C_{1}} \frac{p_{i}}{|S_{i}|} v_{i}^{t+1} + \dots + \sum_{i \in C_{N}} \frac{p_{i}}{|S_{i}|} v_{i}^{t+1}, \qquad (14)$$

where  $\stackrel{(a)}{=}$  comes from the client aggregation,  $\stackrel{(b)}{=}$  comes from the CS broadcasting,  $\stackrel{(c)}{=}$  comes from the cloud aggregation, and  $\stackrel{(d)}{=}$  comes from the edge aggregation. For all  $i \in \{1,\ldots,K\}$ , the term  $\frac{p_i}{|S_i|}v_i^{t+1}$  would appear  $|S_i|$  times in  $\sum_{i \in C_1} \frac{p_i}{|S_i|}v_i^{t+1} + \cdots + \sum_{i \in C_N} \frac{p_i}{|S_i|}v_i^{t+1}$ , and thus we have

$$\sum_{i \in C_1} \frac{p_i}{|S_i|} v_i^{t+1} + \dots + \sum_{i \in C_N} \frac{p_i}{|S_i|} v_i^{t+1}$$

$$= \sum_{i=1}^K \frac{1}{|S_i|} p_i v_i^{t+1} |S_i| = \sum_{i=1}^K p_i v_i^{t+1}. \tag{15}$$

By combining (14) with (15), we can conclude

$$w_i^{t+1} = \sum_{i=1}^{K} p_i v_i^{t+1}.$$
 (16)

Case 3:  $E \mid t+1$  and  $EG \nmid t+1$ . At this step, edge aggregation and client aggregation are performed sequentially, whereas cloud aggregation does not occur. Since  $w_i^{t+1} = \frac{1}{|S_i|} \sum_{n \in S_i} w_{(n)}^{t+1}$  and  $w_{(n)}^{t+1} = \sum_{i \in C_n} \frac{1}{|S_i|} \frac{p_i}{|S_i|} v_i^{t+1}$ , we have

$$w_i^{t+1} = \frac{1}{|S_i|} \sum_{n \in S_i} \sum_{i \in C_n} \frac{1}{\lozenge_n} \frac{p_i}{|S_i|} v_i^{t+1}.$$
 (17)

In summary, the model of client i at step t+1 is represented as follows:

$$w_i^{t+1} = \begin{cases} v_i^{t+1}, & \text{if } E \nmid t+1 \\ \sum_{i=1}^K p_i v_i^{t+1}, & \text{if } EG \mid t+1 \text{(18)} \\ \frac{1}{|S_i|} \sum_{n \in S_i} \sum_{i \in C_n} \frac{1}{\langle o_n} \frac{p_i}{|S_i|} v_i^{t+1}, & \text{otherwise} \end{cases}$$

which characterizes the second transition  $\mathbf{v}^{t+1} \to \mathbf{w}^{t+1}$ . Now, the evolution path  $\mathbf{w}^t \to \mathbf{w}^{t+1}$  can be clearly obtained.

2) Virtual Global Model and Client Contributions: Since the global model is updated only once every EG local training steps,  $\mathbf{w}^t$  cannot reflect the training performance at step t in real time. To address this issue, we define a virtual global model  $\overline{w}^t$ , which is obtained by hypothetically performing edge aggregation followed by cloud aggregation over all client models. This virtual global model can be expressed as:

$$\overline{w^t} = \sum_{n=1}^{N} \left( \Diamond_n \sum_{i \in C_n} \frac{1}{\Diamond_n} \frac{p_i}{|S_i|} w_i^t \right). \tag{19}$$

Furthermore, based on (14) and (15), the above  $\overline{w^t}$  can be rewritten as follows:

$$\overline{w^t} = \sum_{i=1}^K p_i w_i^t. \tag{20}$$

Similar to  $\overline{w^t}$ , we define model  $\overline{v^t}$  corresponding to  $\mathbf{v}^t$  as:

$$\overline{v^t} = \sum_{i=1}^K p_i v_i^t. \tag{21}$$

It can be seen that each client has the same overall contribution weight in the global model, which is crucial for maintaining client-level fairness and stable training performance. In particular, clients in overlapping areas are not made more influential in the global optimization simply because they participate in multiple edge aggregations. This prevents their updates from being overweighted and helps avoid amplifying any adverse impact caused by potential data bias on those clients.

- 3) Upper Bound for the Convergence: We first introduce four assumptions commonly used in FL [42], [43], [44], [45], [46], [47], [48], [49] and distributed optimization [50], [51]:
  - Assumption 1: For all  $i \in \{1, ..., K\}$ ,  $F_i(\mathbf{w})$  is a L-smooth function, i.e., for any  $\mathbf{w}$  and  $\mathbf{w}'$ ,  $F_i(\mathbf{w}) \leq F_i(\mathbf{w}') + (\mathbf{w} \mathbf{w}')\nabla F_i(\mathbf{w}') + \frac{L}{2}\|\mathbf{w} \mathbf{w}'\|^2$ .
  - Assumption 2: For all  $i \in \{1, ..., K\}$ ,  $F_i(w)$  is a  $\mu$ -strongly convex function, i.e., for any  $\mathbf{w}$  and  $\mathbf{w}'$ ,  $F_i(\mathbf{w}) \geq F_i(\mathbf{w}') + (\mathbf{w} \mathbf{w}')\nabla F_i(\mathbf{w}') + \frac{\mu}{2}\|\mathbf{w} \mathbf{w}'\|^2$ .
  - Assumption 3: For all  $i \in \{1, ..., K\}$ , the variance of stochastic gradients in each client is bounded, i.e., for any  $\xi_i^t \sim \mathbf{D}_i$ ,  $\mathbb{E} \|\nabla F_i(\mathbf{w}_i^t, \xi_i^t) \nabla F_i(\mathbf{w}_i^t, \mathbf{D}_i)\|^2 \leq \sigma_i^2$ .
  - Assumption 4: For all  $i \in \{1, ..., K\}$ , the expected squared norm of stochastic gradients is uniformly bounded, i.e., for any  $\xi_i^t \sim \mathbf{D}_i$  and  $\mathbf{w}_i^t, \mathbb{E} \|\nabla F_i(\mathbf{w}_i^t, \xi_i^t)\|^2 \leq H^2$ .

With these 4 assumptions and 2 definitions in place, we now proceed to present the following conclusions:

Lemma 1 (Lemma 1 in [44]): Let Assumptions 1 and 2 hold, and L,  $\mu$  be defined therein. If  $\eta_t \leq \frac{1}{4L}$ , we have

$$\mathbb{E} \left\| \overline{v^{t+1}} - w^{\star} \right\|^{2} \leq (1 - \eta_{t} \mu) \mathbb{E} \left\| \overline{w^{t}} - w^{\star} \right\|^{2} + \eta_{t}^{2} \mathbb{E} \left\| g_{t} - \overline{g^{t}} \right\|^{2} + 6L\eta_{t}^{2} \Gamma + 2\mathbb{E} \sum_{i=1}^{K} p_{i} \left\| \overline{w^{t}} - w_{i}^{t} \right\|^{2}, \quad (22)$$

where  $w^\star$  denotes the optimal global model corresponding to the objective function  $F(w) = \sum_{i=1}^K p_i F_i(w)$ ,  $\overline{g^t} = \sum_{i=1}^K p_i \nabla F_i(w_i^t, D_i)$  is the full-batch gradient,  $g^t = \sum_{i=1}^K p_i \nabla F_i(w_i^t, \xi_i)$  is the stochastic gradient, and  $\Gamma = F^\star - \sum_{k=1}^N p_k F_k^\star \geq 0$  is the optimality gap with  $F^\star$  is the minimum value of function F and  $F_k^\star$  is the minimum value of function  $F_k$  [44].

Lemma 2: In our proposed algorithm, for any  $t \in \{1, \dots, T\}$ , we have  $\overline{v^t} = \overline{w^t}$ .

*Proof:* See Appendix A in the supplementary material. Corollary 1: Let Assumptions 1 and 2 hold, and L,  $\mu$  be defined therein. Let  $\Delta_t$  be defined by  $\mathbb{E}\|\overline{w^t} - w^\star\|^2$ . If  $\eta_t \leq \frac{1}{4L}$ , we have

$$\Delta_{t+1} \le (1 - \eta_t \mu) \Delta_t + \eta_t^2 \mathbb{E} \left\| g_t - \overline{g^t} \right\|^2$$

$$+ 6L \eta_t^2 \Gamma + 2 \mathbb{E} \sum_{i=1}^K p_i \left\| \overline{w^t} - w_i^t \right\|^2, \qquad (23)$$

*Proof*: Based on Lemma 2, we have  $\overline{v^t} = \overline{w^t}$ , and thus  $\mathbb{E}\|\overline{v^{t+1}} - w^\star\|^2 = \mathbb{E}\|\overline{w^{t+1}} - w^\star\|^2 = \Delta_{t+1}$ . According to (22) in Lemma 1, it is clear that  $\Delta_{t+1} \leq (1 - \eta_t \mu) \Delta_t + \eta_t^2 \mathbb{E}\|g_t - \overline{g^t}\|^2 + 6L\eta_t^2 \Gamma + 2\mathbb{E}\sum_{i=1}^K p_i \|\overline{w^t} - w_i^t\|^2$ .

Remark 1: For  $\Delta_{t+1}$ , it is bounded by four terms:  $\Delta_t$ ,  $\mathbb{E}\|g_t - \overline{g^t}\|^2$ ,  $\Gamma$ , and  $\mathbb{E}\sum_{i=1}^K p_i \|\overline{w^t} - w_i^t\|^2$ . The first term,  $\Delta_t$ , represents the overall training outcome at the previous step. The second term,  $\mathbb{E}\|g_t - \overline{g^t}\|^2$ , indicates the data heterogeneity within each client. The third term,  $\Gamma$ , reflects the data heterogeneity across different clients, which is associated with the non-IID property. The final term,  $\mathbb{E}\sum_{i=1}^K p_i \|\overline{w^t} - w_i^t\|^2$ , is determined by the specific topology and parameters of the training model.

Lemma 3: Let Assumption 4 holds and H be defined therein. Assume  $\eta_t$  is non-increasing and  $\eta_t \leq 2\eta_{t+E}$ , we have

$$\mathbb{E} \sum_{i=1}^{K} p_{i} \left\| \overline{w^{t}} - w_{i}^{t} \right\|^{2}$$

$$\leq \eta_{t}^{2} 4^{G} H^{2} (GE + G - 2) \left[ (GE - 1) + E^{2} (G - 1) \right],$$
(24)

*Proof:* See Appendix B in the supplementary material. *Remark 2:* For the term  $\mathbb{E}\sum_{i=1}^K p_i \|\overline{w^t} - w_i^t\|^2$ , its upper bound is mainly determined by three factors: the topology of the model, the data distribution across different clients, and the current step t.

Lemma 4: Assume Assumption 3 holds. It follows that

$$\mathbb{E}\left\|g_t - \overline{g^t}\right\|^2 \le \sum_{i=1}^K p_i^2 \sigma_i^2. \tag{25}$$

*Proof:* The proof is given in [44].

<span id="page-6-0"></span>Corollary 2: Let Assumptions 1 to 4 hold, and L,  $\mu$ ,  $\sigma_i^2$  and H be defined therein. Assume  $\eta_t$  is non-increasing,  $\eta_t \leq \frac{1}{4L}$ , and  $\eta_t \leq 2\eta_{t+E}$ . Let  $\Delta_t$  be defined by  $\mathbb{E}\|\overline{w^t} - w^\star\|^2$ , then we have

$$\Delta_{t+1} \le (1 - \eta_t \mu) \Delta_t + \eta_t^2 X,\tag{26}$$

where  $X = \sum_{i=1}^K p_i^2 \sigma_i^2 + 6L(F^\star - \sum_{k=1}^N p_k F_k^\star) + 2^{2G+1}H^2$   $(GE+G-2)[(GE-1)+E^2(G-1)].$ 

*Proof:* See Appendix C in the supplementary material. Theorem 1: Let Assumptions 1 to 4 hold, and  $L, \mu, \sigma_i^2$  and H be defined therein. Set the learning rate  $\eta_t = \frac{\beta}{t+\alpha}$ , where  $\beta > \frac{1}{\mu}$ ,  $\alpha \geq E > 0$ , and  $\eta_0 \leq \min\{\frac{1}{\mu}, \frac{1}{4L}\}$ . Then, we have

$$\mathbb{E}[F(\overline{w^t})] - F^* \le \frac{L}{2} \frac{Z}{t+\alpha},\tag{27}$$

where  $Z = \max\{\frac{\beta^2 X}{\beta \mu + 1}, \Delta_0 \alpha\}$  with  $X = \sum_{i=1}^K p_i^2 \sigma_i^2 + 6L(F^\star - \sum_{k=1}^N p_k F_k^\star) + 2^{2G+1} H^2 (GE + G - 2)[(GE - 1) + E^2 (G - 1)]$  and  $\Delta_0 = \|w^0 - w^\star\|^2$ .

*Proof:* See Appendix D in the supplementary material. *Remark 3:* As t increases,  $\mathbb{E}[F(\overline{w}^t)] - F^\star$  gradually approaches zero. From an expectation perspective,  $\overline{w}^t$  converges to the optimum, and the system performance improves accordingly.

Remark 4: From the upper bound in Theorem 1, the driftrelated term  $2^{2G+1}H^2(GE+G-2)[(GE-1)+E^2(G-1)]$ 1)] in X generally increases with larger E and G, suggesting that when edge aggregation (controlled by E) and cloud aggregation (controlled by G) are less frequent, local-update drift becomes more pronounced, thereby slowing down early-stage convergence. Therefore, using smaller E and G at the beginning of training to enable more frequent edge/cloud aggregation can help mitigate drift and accelerate performance improvement. As training proceeds, the model typically approaches a stationary point and the learning rate decays, so the marginal performance gain per communication round diminishes; in this regime, maintaining very frequent aggregation often yields limited additional benefit but incurs substantial communication time overhead, thus reducing the end-to-end training efficiency. Accordingly, gradually increasing E and G in later stages to lower the aggregation and communication frequency is an efficient practical strategy.

Remark 5: For HFL, when the four assumptions and the system parameters are set to be the same as those of HHFL, its convergence bound takes a similar form to (27), i.e.,  $\mathbb{E}[F(\overline{w^t})] - F^* \leq \frac{L}{2} \frac{Z'}{t+\alpha}$ . The only difference lies in the constant term (see Appendix E for the proof in the supplementary material for the proof). Specifically, when the data distribution across ESs is non-IID, we show that Z' > Z, and the gap Z' - Z increases as E and G grow. In other words, under non-IID ES-level data distribution, conventional HFL converges more slowly than HHFL, and the advantage of HHFL becomes more pronounced for larger E and G. This conclusion is also consistent with the experimental results reported later (e.g., Figs. 12–13).

It is worth noting that, while the four assumptions are commonly adopted in the literature, they may not cover all practical scenarios, since different learning models can exhibit different properties. For example, *Assumption 2* does not apply to neural

networks with non-convex loss functions. Nevertheless, the insights obtained from our analysis remain valuable for more general settings. In Section V, we further validate this point through experiments on a variety of learning models.

#### B. Comparison Between HFL and HHFL

We compare the performance of HHFL and HFL in terms of the number of steps and the time required to reach convergence.

1) Steps to Achieve Convergence: We assume that the algorithmic parameters E and G are identical for both HFL and HHFL. In HFL, each client connects to a single ES, and its updates remain confined within isolated ES domains for EG local updates before cloud aggregation is performed. When the data distributions across ESs are non-IID, this isolation exacerbates model divergence and inconsistency across ES models as training progresses. As a result, local models initialized from different ESs become increasingly divergent over time, leading to higher variance in local gradient updates and slower convergence.

In contrast, HHFL effectively mitigates this issue. Each ES in HHFL receives updates from a larger and more diverse set of clients, making its model more representative of the global data distribution and reducing divergence among ES models. In addition, the client aggregation mechanism in HHFL enables clients located in overlapping regions to initialize their models using multiple ES models. Together, these two mechanisms reduce the variance in client initializations. As a result, the local updates computed as  $v_i^{t+1} = w_i^t - \eta_t \nabla F_i(w_i^t)$  are based on betterinformed starting points. Since  $w_i^t$  incorporates more global data, the corresponding gradient  $\nabla F_i(w_i^t)$  is more aligned with the global direction  $\nabla F(w^t)$ , which reduces the variance of local gradients, represented as  $\sigma^2 = \mathbb{E}_i[\|\nabla F_i(w_i^t) - \nabla F(w^t)\|^2].$ This observation is consistent with Remark 4, and more theoretical details are provided in Appendix E of the supplementary material.

According to [51], standard stochastic optimization bounds suggest that  $\mathbb{E}[F(\overline{w^T})] - F(w^\star) \leq \mathcal{O}(\frac{1+\sigma^2}{\sqrt{T}})$ , indicating that a smaller gradient variance  $\sigma^2$  leads to faster convergence. Consistently, the tighter bound in (27) further supports this effect. Therefore, compared with HFL, HHFL typically requires fewer training steps to reach a target convergence level.

2) Time to Achieve Convergence: The overall time (i.e., the total wall-clock time) mainly involves the computing time and the wireless transmission time. We assume that the two types of time do not overlap. This assumption is widely adopted in FL, as it helps reduce scheduling and synchronization complexity, especially on resource-constrained devices [21], [23], [24], [25], [46], [52], [53], [54]. Therefore, the overall time is the sum of the computing time and the transmission time. For the computing time, it is primarily used for local updates and model aggregations. Since model aggregation only involves computing a weighted average, its computational cost is significantly lower than that of a local update. Moreover, aggregation occurs much less frequently than local updates. Therefore, it is reasonable to ignore the aggregation time and approximate the computing time using only the time spent on local updates. Let c denote the number of CPU cycles required to compute one bit, f the CPU <span id="page-7-0"></span>frequency, and  $b_0$  the number of computed bits required for one step of a local update. Then, the local update computation time for executing T updates is given by

$$T_{\rm comp} = \frac{cb_0}{f}T. (28)$$

For the transmission time, the total time for T local update steps can be expressed as

$$T_{\text{trans}} = \left\lceil \frac{T}{E} \right\rceil T_{\text{CES}} + \left\lceil \frac{T}{EG} \right\rceil T_{\text{ECS}},$$
 (29)

where  $\lceil \cdot \rceil$  denotes the ceiling function.  $T_{\text{CES}}$  denotes the end-to-end wall-clock duration (e.g., airtime and protocol overhead) of one ES-client round-trip model exchange, including the ES-to-client downlink model dissemination and the client-to-ES uplink upload of updated models.  $T_{\text{ECS}}$  denotes the end-to-end wall-clock duration of one CS-ES round-trip model exchange, including the CS-to-ES global-model dissemination and the ES-to-CS uplink upload of ES models. Moreover,  $\left\lceil \frac{T}{E} \right\rceil$  and  $\left\lceil \frac{T}{EG} \right\rceil$  represent the numbers of ES-client and CS-ES round-trip exchanges required to complete T training steps, respectively. Then, the overall time for both architectures to complete T local update steps are represented as

$$T_{\text{overall}} = \frac{cb_0}{f}T + \left[\frac{T}{E}\right]T_{\text{CES}} + \left[\frac{T}{EG}\right]T_{\text{ECS}}.$$
 (30)

In practical deployments, model dissemination from ESs to clients can be carried out in parallel over orthogonal PRBs, and a client's model upload can be received and decoded by multiple associated ESs via CoMP-capable uplink multipoint reception. Moreover, contemporary 5G/NextG systems are engineered with substantial parallel receive-side basebandprocessing capability at both BSs and user devices to decode multiple PRB allocations within the same carrier, and BSs are typically provisioned with sufficient transmit-side basebandprocessing resources to map and process multiple PRB allocations in parallel within a carrier, thereby serving multiple users concurrently on orthogonal PRBs [55]. While such parallel processing capabilities effectively eliminate transmission bottlenecks, enabling these multi-point connections does introduce extra synchronization overhead, as ESs must coordinate PRB allocations via the Xn interface. However, this coordination cost has a negligible impact on  $T_{CES}$ . First, because ESs operate independently without data-level cooperation, the Xn interface exchanges only lightweight scheduling signals, thereby bypassing heavy backhaul data transfers. Second, leveraging 5G CG for PRB pre-allocation amortizes the one-time negotiation latency across the entire training process, effectively eliminating per-round dynamic scheduling delays. Consequently, under our latency model, the additional ES-client links do not necessarily increase  $T_{CES}$ , and since the network infrastructure remains static,  $T_{ECS}$  is also unaffected. As a result, with the same client hardware capabilities and the same E and G, HHFL and HFL have equivalent overall training-time expressions in terms of the total number of local update steps, as shown in (30). As discussed in Section IV-B1, HHFL requires fewer steps to reach convergence compared to HFL. Therefore, HHFL requires a

shorter overall time to converge, making it a more efficient choice than HFL.

3) Resource Consumption: Given the negligible computational cost of model parameter aggregation, the primary resource-related drawback of HHFL compared to standard HFL is the greater per-round resource consumption such as higher PRB occupancy and energy costs during model transmission between ESs and clients. This is because clients situated in overlapping areas can simultaneously connect to multiple ESs for data exchange. This creates more ES-client communication links, thereby increasing the volume of data transmitted per round and requiring more resources for transceiving and signal processing. However, as HHFL typically requires fewer training steps to reach convergence due to the knowledge-sharing benefits provided by multi-connectivity links, it yields three primary advantages: i) reduced total computational overhead for local client training; ii) fewer communication rounds between the CS and ESs; and iii) a lower total number of communication rounds between ESs and clients. While the first two advantages provide direct resource savings for the entire system including clients, ESs, and the CS, the third involves a tradeoff between the reduction in communication rounds and the increased per-round transmission overhead between ESs and clients. Notably, when the data distribution across ESs is sufficiently non-IID, the gain from the reduction in total communication rounds dominates this tradeoff, and HHFL achieves lower overall resource consumption on both the ES and client sides for the data transmission between them. For the sake of brevity, the detailed analysis of this tradeoff is relegated to Appendix F in the supplementary material, which derives the theoretical upper bound on the increase factor in resource consumption for per-round ES-client model transmissions under HHFL and uses our experimental results as a concrete case study to demonstrate that the reduction in communication rounds outweighs the increase in per-round resource consumption. Collectively, HHFL is demonstrated to be more resource efficient for every participating entity including clients, ESs, and the CS throughout the entire training process in this sufficiently non-IID case.

It is noteworthy that the increase in per-round ES-client resource consumption is connectivity-dependent and remains decoupled from the ES-level non-IID degree. Consequently, when the degree of non-IID is insufficient, the marginal gain from knowledge sharing between ESs facilitated by multiconnectivity links diminishes, and the aforementioned advantages of HHFL may fail to offset the higher per-round overhead, leading to greater total resource consumption than HFL. While HHFL is primarily designed to improve time efficiency, resource constraints can sometimes become a critical factor to consider in certain deployment scenarios. To optimize practical resource efficiency in such cases, some active multi-connectivity links can be strategically deactivated to reduce the additional per-round communication overhead for ES-client data transmissions, at the cost of some potential knowledge-sharing gains. Optimizing the number and selection of multi-connectivity links to disable (e.g., by disabling a subset of links for a single client or across multiple clients and ESs) is a highly complex problem. Addressing this optimization problem requires jointly considering data

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

Fig. 3. The actual distribution of clients and the number of clients assigned to each ES under the HFL architecture. The coverage area of  $ES_1$  is represented by a blue circle,  $ES_2$  by a red circle, and  $ES_3$  by an orange circle. The values in this figure represent the number of clients.

distribution, network topology, time efficiency, and resource constraints, which exceeds the scope of this study. We defer a detailed investigation of resource-aware link activation/deactivation designs for HHFL to future work.

#### V. EXPERIMENTAL EVALUATION

In this section, we evaluate the effectiveness of HHFL and demonstrate its advantage in convergence efficiency.

### A. Basic Experimental Setup

FL Architecture Configuration: Without loss of generality, we consider a network scenario consisting of one CS, three ESs labeled as  $ES_1$ ,  $ES_2$ , and  $ES_3$ , and 57 clients. The ESs are symmetrically placed at the vertices of an equilateral triangle, each serving 25 clients: 14 connect exclusively to a single ES, 8 connect to two ESs, and 3 connect to all three ESs, as illustrated in Fig. 3(a). This topology can be directly adopted for the HHFL architecture. For the HFL architecture, clients located in each overlapping region are randomly and evenly assigned to one of the ESs covering that region, ensuring that each client connects to only one ES. Specifically, the distributions of clients allocated to  $ES_1$ ,  $ES_2$ , and  $ES_3$  in the HFL architecture are shown in Fig. 3(b), 3(c), and 3(d), respectively.

FLAlgorithm Configuration: We employ the HHFL algorithm for our proposed architecture. For the HFL architecture, we implement the efficient and widely adopted Hier-FAVG algorithm, as introduced in [25]. We set E=5 and G=5.

Training Model Configuration: To validate that our HHFL method converges effectively regardless of whether the training loss function is convex or nonconvex and does so with higher efficiency than HFL, we selected two models: a logistic regression model and a convolutional neural network (CNN). These models correspond to convex and nonconvex loss functions respectively. Both models are trained on the MNIST dataset using mini-batch SGD with a batch size of 20. The logistic regression model's initial learning rate is 0.1, with an exponential decay of 0.992 per epoch. For the CNN model, to obtain a clearer convergence curve, we adopt a smaller initial learning rate of 0.02. Here, we intentionally adopt the simple MNIST dataset and lightweight models. This setup avoids unnecessary complexity introduced by deep models or large-scale datasets, while still providing generalizable insights into architectural performance.

Data Distribution Configuration: We consider three basic data distribution scenarios: i) client IID, ES IID scenario, where the data distribution among clients within each ES is IID while the data distribution across ESs is also IID; ii) client non-IID, ES IID scenario, where the data distribution among clients within each ES is non-IID while the data distribution across ESs is IID; iii) client non-IID, ES non-IID scenario, where both the data distributions among clients within each ES are non-IID while the data distribution across ESs is also non-IID. Since the non-IID setting in this work requires considering IID conditions at the ES level, the conventional Dirichlet-based distribution is not well-suited to meet this requirement. Therefore, we adopt the pathological non-IID setting [20] following the setup in [42].

Computation and Communication Configuration: We set the ratio  $T_{\rm CES}/T_{\rm SGD}=10$  to reflect the communication bottleneck, where  $T_{\rm SGD}$  denotes the local training time for E local updates, following the experimental setup in [42], [49]. In 5G/NextG networks, the connection between base stations and the cloud server station is wired and significantly faster than wireless transmission [56]. Real-world measurements show that the wireless latency between clients and ESs typically ranges from 5 to 20 ms [57], whereas the wired fiber latency between ESs and the CS is typically between 0.2 and 1 ms [58]. Based on these observations, it is reasonable to set the ratio  $T_{\rm CES}/T_{\rm ECS}=10$  without loss of generality.

## B. Experimental Results and Analysis

1) Impact of intra-ES non-IID Data Distribution on Convergence Under ES IID Scenario: We compare the convergence performance of the HFL and HHFL architectures under different degrees of non-IID data distribution among clients within each ES, while keeping the data distribution across ESs IID. To this end, we design three cases: the (IID, IID) case, the (non-IID-1, IID) case, and the (non-IID-2, IID) case. In the first case, each client uniformly contains samples from all 10 classes. In the second case, each client uniformly contains samples from 6 classes, and in the third case, each client uniformly contains samples from only 2 classes. For all three cases, the data distribution across ESs remains IID. The convergence curves over training steps are shown in Fig. 4. It is clear that the two convergence curves corresponding to HFL and HHFL in the same case almost show no difference. One intuitive explanation for this

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

Fig. 4. Convergence curves under different degrees of non-IID data distribution among clients within each ES (*ES IID* scenario).

![](_page_9_Figure_4.jpeg)

Fig. 5. Convergence curves under different degrees of non-IID data distribution across ESs (*ES non-IID scenario*).

is that when the data distribution across ESs is IID, no cross-ES knowledge sharing is needed, and clients in overlapping regions would offer no incremental utility. Another side observation is that the convergence speed in the *(non-IID-2, IID)* case is significantly slower than in the other two cases. This is because the local gradient variance across clients becomes much larger in this case, as each client only contains samples from two classes.

*2) Impact of ES non-IID Data Distribution on Convergence Under* ES non-IID *Scenario:* We compare the convergence performance of the HFL and HHFL architectures under different degrees of non-IID data distribution across ESs. Here, two cases are designed: the *(non-IID, IID-1) case* and the *(non-IID, IID-2) case*. In the first case, each ES is missing 3 data classes, whereas in the second case, each ES is missing 4 classes. The data across ESs is more non-IID in the second case than in the first. The convergence curves over training steps are shown in Fig. 5. It can be observed that HHFL consistently outperforms HFL in terms of convergence performance. Moreover, as the degree of non-IID data distribution across ESs increases, the performance of HHFL remains largely unaffected, whereas the convergence performance of HFL degrades significantly. This results in a larger performance gap between the two architectures. We attribute the advantages of HHFL to the presence of clients located in overlapping regions. These clients enable knowledge sharing between neighboring ESs, which helps mitigate the performance degradation caused by the limited class diversity within individual ESs.

*3) Impact of Proportion of Clients Located in Overlapping Regions on Convergence:* We compare the convergence performance of the HFL and HHFL architectures with varying proportion of clients located in overlapping regions. Here, we adjust this proportion by simulating user mobility. Starting from our original deployment, we increase this proportion by relocating some single-coverage clients into overlapping areas; conversely, we decrease it by relocating some overlapping-area clients into single-coverage areas. To ensure that the overlap proportion is the primary change across configurations and to avoid unintended effects caused by ES reassignment (which may alter the ES-level non-IIDness in HFL), we keep the client–ES association in the HFL baseline unchanged when generating different overlap settings. Specifically: (i) when a client is moved from a single-coverage area to an overlapping area, it remains associated with its pre-relocation ES in HFL; and (ii) when a client is moved from an overlapping area to a single-coverage area, it is placed within the single-coverage region of its originally assigned ES in HFL.

To visualize the impact of changing the overlapping proportion on convergence curves, we first construct an illustrative case based on the *(non-IID, non-IID-2)* case. Specifically, we relocate 6 single-coverage clients into the overlapping areas to get an additional case, called *(non-IID, non-IID-*2 *)* case. The resulting client distribution and the corresponding ES associations are illustrated in Fig. [6.](#page-10-0) The convergence curves over training steps are shown in Fig. [7.](#page-10-0) We observe that HHFL converges faster than HFL under the same case. Moreover, increasing the number of clients in overlapping regions improves the convergence speed of HHFL, although this acceleration is modest due to the small number of relocated clients in our setup, whereas HFL's convergence speed remains largely unaffected. We believe this result comes from the fact that, in the HHFL architecture, a greater number of overlapping clients can enhance indirect knowledge sharing among neighboring ESs, whereas in the HFL architecture, the client assignments at each ES remain unchanged despite the relocation of clients.

While the above comparison provides an intuitive understanding, we next conduct a systematic sweep over the overlap proportion. Specifically, we vary the overlap proportion by relocating additional clients into or out of the overlapping areas, and for each proportion value we run both HFL and HHFL under five basic cases. We then quantify HHFL's advantage using an efficiency-gain metric in terms of the required training steps. To determine the convergence point, we adopt a generalizable approach based on the sliding average of the slope. A threshold of 0.1% is used, such that when the average rate of improvement in accuracy falls below this value at a particular step, the model is regarded as having reached convergence. The resulting Efficiency Gain VS. Proportion curve is shown in Fig. [8.](#page-10-0) We observe that when the data distributions across ESs are IID, namely cases 1–3, the efficiency gain remains close to 1 regardless of the overlap proportion, indicating that HHFL's multi-connectivity offers almost no speedup over HFL. This is because, under ES-level IID data, HFL does not need the overlapping-area clients to facilitate inter-ES knowledge sharing. In contrast, when the data distributions across ESs are non-IID, namely

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

Fig. 6. Client actual distribution and the number of clients assigned to each ES for the *(non-IID, IID-*2 *)* case. The coverage area of *ES*<sup>1</sup> is represented by a blue circle, *ES*<sup>2</sup> by a red circle, and *ES*<sup>3</sup> by an orange circle. The values in this figure represent the number of clients.

![](_page_10_Figure_4.jpeg)

Fig. 8. Efficiency gain of HHFL over HFL versus the overlapping proportion for Cases 1–5: *(IID, IID)* , *(non-IID-1, IID)* , *(non-IID-2, IID)* , *(non-IID, non-IID-1)* , and *(non-IID, non-IID-2)*.

cases 4–5, HHFL's efficiency gain over HFL increases with the overlap proportion. The improvement is pronounced when the overlap proportion is small, and then gradually saturates as the proportion becomes larger. We believe this behavior arises because a small number of overlapping clients can already provide much-needed bridging for inter-ES knowledge sharing; once this bridging effect becomes sufficiently strong, additional overlapping clients yield diminishing marginal gains, leading to a saturation trend.

*4) Convergence Curves Over Wall-Clock Time and Total Data Transmitted:* We further provide a holistic efficiency evaluation by plotting the convergence performance (i.e., test accuracy) of HFL and HHFL against (i) wall-clock time and (ii) the total data transmitted, under different data-distribution cases.

By setting the time required for a client to complete E local updates as one unit time, the experimental results are presented

Fig. 9. Test accuracy versus wall-clock time across six cases (time is normalized such that one unit corresponds to the time for a client to complete *E* local updates).

in Fig. 9. As observed in Fig. 9(a) and 9(b), when the data distribution across ESs is IID, HHFL does not exhibit a noticeable advantage in terms of wall-clock time. However, when the data distribution across ESs is non-IID, HHFL outperforms HFL, as shown in Fig. 9(c) and 9(d). This is because HHFL requires significantly fewer total training steps, which directly cuts down the time clients spend on local training. It also reduces the number of communication rounds between all participants (i.e., Client-to-ES and ES-to-CS), thereby cutting down the time each party spends on communication. Since these phases are the main components of the total time, HHFL ends up being much more efficient overall.

By setting the number of bits required to transmit a single model as one unit of data volume, the experimental results are presented in Fig. [10.](#page-11-0) Note that the transmitted data volume accounts specifically for the communication between the BS/ES and the clients. As observed in Figs. [10\(a\)](#page-11-0) and [10\(b\),](#page-11-0) when the data distribution across ESs is IID, HHFL converges slower than HFL. This is because HHFL establishes more communication

<span id="page-11-0"></span>![](_page_11_Figure_2.jpeg)

Fig. 10. Test accuracy versus total data transmitted across six cases (data volume is normalized such that one unit corresponds to the number of bits required to transmit one model).

![](_page_11_Figure_4.jpeg)

Fig. 11. Efficiency gain of HHFL over HFL across Cases 1-6: (IID, IID), (non-IID-1, IID), (non-IID-2, IID), (non-IID, non-IID-1), (non-IID, non-IID-2), and (non-IID, non-IID-2').

links, which involves more data transmission without providing the compensating benefit of effective knowledge sharing in an IID setting. Conversely, as shown in Fig. 10(c) and 10(d), under the cases where the data distribution across ESs is non-IID, HHFL reaches convergence with significantly less total data transmission. This is because the benefits of knowledge sharing facilitated by the additional links effectively outweigh the additional data-transmission cost introduced by the extra links.

5) Efficiency Gain of HHFL Over HFL in Terms of Training Steps and Wall-Clock Time Across All Cases: Based on the obtained convergence curves, we calculate the number of training steps and the wall-clock time required for each architecture to reach convergence in each case using the same convergence criterion. We then compute the efficiency gain of HHFL over HFL across all cases, in terms of both training steps and wall-clock time. The results of the efficiency gain comparison are shown in Fig. 11. It is evident that both the training steps and the overall time bars are almost equal in height in each case. This is because the overall time scales nearly linearly with training

![](_page_11_Figure_8.jpeg)

Fig. 12. Efficiency gain of HHFL over HFL with varying *E* across Cases 4-6: (non-IID, non-IID-1), (non-IID, non-IID-2), and (non-IID, non-IID-2').

![](_page_11_Figure_10.jpeg)

Fig. 13. Efficiency gain of HHFL over HFL with varying *G* across Cases 4-6: (non-IID, non-IID-1), (non-IID, non-IID-2), and (non-IID, non-IID-2').

steps, as shown in (30), then the time ratio between HFL and HHFL closely matches the ratio of their training steps. Besides that, the efficiency ratios for the first three cases under the *ES IID* scenario are all close to 1, which indicates that there is little to no efficiency improvement for the use of HHFL. Moreover, for the last three cases, the efficiency ratios are significantly greater than 1, even reaching 2 in case 6, indicating that the use of HHFL results in substantial efficiency improvements.

6) Impact of Parameters E and G on the Efficiency Gain of HHFL Over HFL: We evaluate how the efficiency gain of HHFL over HFL changes with different values of parameters Eand G across three cases under ES non-IID scenario: (non-IID, non-IID-1), (non-IID, non-IID-2), and (non-IID, non-IID-2'). The default values are set to E=5 and G=5. When varying one of the parameters, the other is kept fixed at its default value. Since the efficiency gains in terms of training steps and the overall time are nearly identical across all cases regardless of the model used, we use the efficiency gain with respect to training steps as a representative metric. The changes in efficiency gain with respect to E and G are shown in Figs. 12 and 13, respectively. It can be observed that the efficiency gain increases in all three cases as either E or G becomes larger. The underlying reason is that increasing E or G weakens the frequency of global alignment: a larger E means more local steps are taken between edge aggregations, and a larger G means cloud aggregation is invoked less often. Under non-IID data, both effects aggravate inter-ES model drift and make the ES models diverge more easily in conventional HFL, where ESs mainly evolve in isolation between cloud aggregations. In contrast, HHFL introduces an additional cross-ES knowledge bridge via overlapping clients, which repeatedly receive models from multiple ESs and feed

<span id="page-12-0"></span>![](_page_12_Figure_2.jpeg)

Fig. 14. Convergence curves across six experimental cases on the CIFAR-10 dataset.

![](_page_12_Figure_4.jpeg)

Fig. 15. Test accuracy versus wall-clock time across six cases on the CIFAR-10 dataset (time is normalized such that one unit corresponds to the time for a client to complete *E* local updates).

back updates. This inter-ES coupling partially compensates for the reduced global alignment, mitigates model drift, and helps maintain consistency across ESs. Therefore, when E or G increases, the relative advantage of HHFL over HFL becomes more pronounced.

## *C. Additional Experiments on CIFAR-10 Dataset*

*1) Setup:* To validate the robustness of HHFL under complex data heterogeneity, we extended our evaluation to the more challenging CIFAR-10 dataset. The model architecture follows a VGG-11 style backbone, which comprises a feature extractor with three convolutional blocks (64, 128, and 256 channels) interspersed with max-pooling layers. To stabilize training under non-IID data and avoid overfitting, we applied group normalization and dropout. The feature extractor is followed by a streamlined two-layer fully connected classifier (4096 → 1024 → 10). Local training is performed using SGD with a momentum of 0.9 and a weight decay of 5 × 10<sup>−</sup><sup>4</sup>. The initial learning rate is 0.07, with an exponential decay of 0.9 per epoch. For other parameters and configurations, unless otherwise specified, we follow the same experimental settings as in our basic experiments on MNIST.

*2) Results Analysis:* The results are shown in Figs. 14 –16. We observe that the experimental trends on CIFAR-10 are highly consistent with those observed on the MNIST dataset. Specifically, as illustrated in Figs. 14(a) and 15(a) , when the data distribution across ESs is IID, HHFL exhibits negligible advantages over HFL in terms of both total training steps and wall-clock time. However, under non-IID data distributions across ESs, HHFL consistently exhibits significantly better convergence efficiency than HFL, as shown in Figs. 14(b) and 15(b).

![](_page_12_Figure_10.jpeg)

Fig. 16. Test accuracy versus total data transmitted across six cases on the CIFAR-10 dataset (data volume is normalized such that one unit corresponds to the number of bits required to transmit one model).

The fundamental reason is the effect of multi-connectivityenabled knowledge sharing, which makes the update directions of different ES models more aligned with the global optimization direction, thereby reducing the total number of updates required for convergence. Based on our convergence criterion, HHFL consistently achieves efficiency gains greater than <sup>1</sup>.5<sup>×</sup> over HFL across all these non-IID scenarios, in terms of both training steps and wall-clock time. Fig. 16(a) shows that when the data distributions across ESs are IID, HHFL requires more total data transmission than HFL to reach the same test accuracy, as shown in Fig. 16(b). This is because, in this case, the additional data transmitted over the multi-connectivity links is largely redundant in terms of knowledge content. In contrast, when the data distributions across ESs are non-IID, HHFL transmits less total data than HFL to achieve convergence. This is because the data exchanged through multi-connectivity links is no longer redundant; instead, it conveys useful knowledge from different ESs. Moreover, the resulting benefit of accelerating training convergence outweighs the additional data-transmission cost introduced by the extra links.

## VI. RELATED WORK

In this section, we discuss the research related to this work. *HFL Designs:* HFL has been extensively studied to address various real-world challenges faced by FL in large-scale wireless networks [\[10\],](#page-13-0) [\[25\],](#page-13-0) [\[36\],](#page-14-0) [\[37\],](#page-14-0) [\[38\],](#page-14-0) [\[39\],](#page-14-0) [\[40\],](#page-14-0) [\[59\],](#page-14-0) [\[60\],](#page-14-0) [\[61\],](#page-14-0) [\[62\],](#page-14-0) [\[63\],](#page-14-0) [\[64\],](#page-14-0) [\[65\],](#page-14-0) [\[66\],](#page-14-0) [\[67\],](#page-14-0) [\[68\],](#page-14-0) [\[69\],](#page-14-0) [\[70\],](#page-14-0) [\[71\],](#page-14-0) [\[72\],](#page-14-0) [\[73\],](#page-14-0) [\[74\],](#page-14-0) [\[75\],](#page-14-0) [\[76\],](#page-14-0) [\[77\],](#page-14-0) [\[78\],](#page-15-0) [\[79\],](#page-15-0) [\[80\],](#page-15-0) [\[81\],](#page-15-0) [\[82\],](#page-15-0) [\[83\].](#page-15-0) For example, several studies have explored cluster-based hierarchical aggregation, where clients are first grouped into clusters based on geographical proximity, data similarity, or mobility patterns to improve communication efficiency and training accuracy [\[65\],](#page-14-0) [\[66\],](#page-14-0) [\[70\],](#page-14-0) [\[77\].](#page-14-0) Other works have investigated personalized hierarchical FL frameworks, where clients and ESs collaboratively adapt models to individual data distributions to tackle non-IID challenges [\[37\],](#page-14-0) [\[60\],](#page-14-0) [\[76\].](#page-14-0) In addition, some studies focus on optimizing resource allocation and edge association to dynamically improve training efficiency under varying network conditions [\[36\],](#page-14-0) [\[78\],](#page-15-0) [\[83\].](#page-15-0) Although these studies have introduced valuable improvements across various aspects, they fundamentally preserve the traditional HFL architecture, where each client connects to a single ES, and the ESs periodically upload aggregated models to the CS. This communication structure <span id="page-13-0"></span>inherently limits cross-ES information sharing and constrains the potential benefits of modern multi-connectivity wireless infrastructures. In contrast, our proposed HHFL architecture fully leverages the CoMP capabilities of modern wireless networks, allowing clients located in overlapping regions to simultaneously communicate with multiple ESs. By enabling such multi-ES connections, HHFL facilitates broader model sharing across different ESs, effectively mitigates statistical heterogeneity, and significantly accelerates convergence under practical non-IID distributions.

*Multi-ES architecture:* This FL architecture is technically regarded as a client-ES structure with multiple parallel aggregation ESs. Numerous research efforts have been devoted to this type of architecture, generally aiming to explore how inter-ES collaboration can improve overall learning performance, enhance convergence under non-IID data, and optimize communication and resource allocation efficiency in distributed systems [16], [\[42\],](#page-14-0) [\[84\],](#page-15-0) [\[85\],](#page-15-0) [\[86\],](#page-15-0) [\[87\],](#page-15-0) [\[88\],](#page-15-0) [\[89\],](#page-15-0) [\[90\],](#page-15-0) [\[91\].](#page-15-0) Among these, several studies have investigated the overlapping-region scenario, where a client may connect to multiple ESs simultaneously. This setting closely reflects the characteristics of 5G and beyond communication systems and is particularly relevant to our work. For example, [\[42\]](#page-14-0) proposed a multi-ES architecture and introduced the FedMes algorithm, in which clients located in overlapping regions aggregate the models from their connected ESs to initialize local training. Based on that, [\[86\]](#page-15-0) designed the MS-FedAvg algorithm, which further improved model aggregation and achieved higher efficiency. These existing works allow only indirect and localized data sharing between ESs through clients in overlapping regions. However, our proposed HHFL supports direct and global cross-ES data sharing via the CS during training. Under practical 5G and beyond network environments, the wired connections between base stations and the cloud server are stable and high-speed, and it is common to see the data distributions across ESs are non-IID. In such situations, our HHFL can achieve higher efficiency by mitigating statistical heterogeneity while incurring only a small communication cost between the CS and ESs.

# VII. CONCLUSION

This paper presents a novel FL architecture named HHFL, which can be regarded as a hybrid extension of HFL. In this architecture, each client is capable of communicating with one or more ESs simultaneously, making HHFL inherently aligned with current and future wireless infrastructures that support CoMP. Through both theoretical analysis and experimental evaluation, we demonstrate the effectiveness and efficiency of HHFL, underscoring its strong potential as a scalable and efficient solution for practical FL model training in today's and future wireless networks.

# REFERENCES

- [1] B. Brik, A. Ksentini, and M. Bouaziz, "Federated learning for UAVsenabled wireless networks: Use cases, challenges, and open problems," in*IEEE Access*, vol. 8, pp. 53841–53849, 2020.
- [2] D. C. Nguyen, M. Ding, P. N. Pathirana, A. Seneviratne, J. Li, and H. V. Poor, "Federated learning for Internet of Things: A comprehensive survey," *IEEE Commun. Surv. Tut.*, vol. 23, no. 3, pp. 1622–1658, thirdquarter 2021.

- [3] F. Yin et al., "FedLoc: Federated learning framework for data-driven cooperative localization and location data processing," *IEEE Open J. Signal Process.*, vol. 1, pp. 187–215, 2020.
- [4] M. K. Mehmet-Ali, J. F. Hayes, and A. K. Elhakeem, "Traffic analysis of a local area network with a star topology," *IEEE Trans. Commun.*, vol. 36, no. 6, pp. 703–712, Jun. 1988.
- [5] J. Petrek and V. Sledt, "A large hierarchical network star—Star topology design algorithm," *Eur. Trans. Telecommun.*, vol. 12, pp. 511–522, 2001.
- [6] L. Goratti, T. Baykas, T. Rasheed, and S. Kato, "NACRP: A connectivity protocol for star topology wireless sensor networks," *IEEE Wirel. Commun. Lett.*, vol. 5, no. 2, pp. 120–123, Apr. 2016.
- [7] M. Barranco, J. Proenza, G. Rodrı ´guez-Navas, and L. Almeida, "An active star topology for improving fault confinement in CAN networks," *IEEE Trans Ind. Informat.*, vol. 2, no. 2, pp. 78–85, May 2006.
- [8] K. Day and A. Tripathi, "A comparative study of topological properties of hypercubes and star graphs," *IEEE Trans. Parallel Distrib. Syst.*, vol. 5, no. 1, pp. 31–38, Jan. 1994.
- [9] J. Lessmann and A. Krishnamurthy, "Parameterized hierarchical layer topology construction for wireless networks," in *Proc. IEEE ICSNC*, 2007, pp. 15–15.
- [10] B. Xu,W. Xia,W.Wen, P. Liu, H. Zhao, and H. Zhu, "Adaptive hierarchical federated learning over wireless networks," *IEEE Trans. Veh. Technol.*, vol. 71, no. 2, pp. 2070–2083, Feb. 2022.
- [11] E. Ravasz and A.-L. Barabási, "Hierarchical organization in complex networks," *APS Phys. Rev. E*, vol. 67, 2003, Art. no. 026112.
- [12] L. Jiao, J. Zhao, Y. Xu, T. Zhang, H. Zhou, and D. Zhao, "Performance analysis for downlink transmission in multiconnectivity cellular V2X networks," *IEEE Internet Things J.*, vol. 11, no. 7, pp. 11812–11824, Apr. 2024.
- [13] N. Ye, X. Cao, X. Ding, J. Li, D. Zhao, and Q. Ouyang, "Multi-connection to the sky: Energy-efficient beamforming for multi-satellite uplink transmission with lens antenna array," *IEEE Trans. Green Commun. Netw.*, vol. 7, no. 4, pp. 1836–1848, Dec. 2023.
- [14] Y. Xiao et al., "Space-air-ground integrated wireless networks for 6G: Basics, key technologies and future trends," *IEEE J. Sel. Areas Commun.*, vol. 42, no. 12, pp. 3327–3354, Dec. 2024.
- [15] G. Xu, "Research on 6G mobile communication system," in *Proc. J. Phys.: Conf. Ser.*, vol. 1693, 2020, Art. no. 012101.
- [16] Z. Yang, M. Chen, K.-K. Wong, H. V. Poor, and S. Cui, "Federated Learning for 6G: Applications, challenges, and opportunities," *Elsevier Engineering*, vol. 8, pp. 33–41, 2022.
- [17] M. Z. Chowdhury, M. Shahjalal, S. Ahmed, and Y. M. Jang, "6G wireless communication systems: Applications, requirements, technologies, challenges, and research directions," *IEEE Open J. Commun. Soc.*, vol. 1, pp. 957–975, 2020.
- [18] I. F. Akyildiz, A. Kak, and S. Nie, "6G and beyond: The future of wireless communications systems," in*IEEE Access*, vol. 8, pp. 133995–13430, 2020.
- [19] P. Yang, Y. Xiao,M. Xiao, and S. Li, "6GWireless Communications: vision and potential techniques," in*IEEE Network*, vol. 33, no. 4, pp. 70–75, 2019.
- [20] B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. Y Arcas, "Communication-efficient learning of deep networks from decentralized data," in *Proc. PMLR AISTATS*, pp. 1273–1282, 2017.
- [21] P. Kairouz et al., "Adv. and Open Problems in Federated Learn.," Found. *Trends Mach. Learn.*, Emerald Publishing Limited, vol. 14, no. 1-2, pp. 1– 210, 2021.
- [22] K. Bonawitz et al., "Practical secure aggregation for privacy-preserving machine learning," in *Proc. ACM SIGSAC Conf. Comput. Commun. Secur.*, pp. 1175–1191, 2017.
- [23] T. Li, A. K. Sahu, M. Zaheer, M. Sanjabi, A. Talwalkar, and V. Smith, "Federated optimization in heterogeneous networks," in *Proc. MLSys*, pp. 429–450, 2020.
- [24] V. Smith, C.-K. Chiang, M. Sanjabi, and A. S. Talwalkar, "Federated multitask learning," in *Proc. Adv. Neural Inf. Process. Syst.*, pp. 4424–4434, 2017.
- [25] L. Liu, J. Zhang, S. Song, and K. B. Letaief, "Client-edge-cloud hierarchical federated learning," in *Proc. IEEE Int. Conf. Commun.*, pp. 1–6, 2020.
- [26] N. Bhushan et al., "Network densification: The dominant theme for wireless evolution into 5G," *IEEE Commun. Mag.*, vol. 52, no. 2, pp. 82–89, Feb. 2014.
- [27] R. Borralho, A. Mohamed, A. U. Quddus, P. Vieira, and R. Tafazolli, "A survey on coverage enhancement in cellular networks: Challenges and solutions for future deployments," *IEEE Commun. Surv. Tut.*, vol. 23, no. 2, pp. 1302–1341, Secondquarter 2021.

- <span id="page-14-0"></span>[28] Y. Ullah, M. B. Roslee, S. M. Mitani, S. A. Khan, and M. H. Jusoh, "A survey on handover and mobility management in 5G hetnets: Current state, challenges, and future directions," *Sensors*, vol. 23, 2023, Art. no. 5081.
- [29] A. U. Rehman, M. B. Roslee, and T. J. Jiat, "A survey of handover management in mobile hetnets: Current challenges and future directions," *Appl. Sci.*, vol. 13, 2023, Art. no. 13.
- [30] S. Shamai and B. M. Zaidel, "Enhancing the cellular downlink capacity via co-processing at the transmitting end," in *Proc. IEEE VTC Spring*, 2001, pp. 1745–1749.
- [31] F. Qamar, K. B. Dimyati, M. N. Hindia, K. A. B. Noordin, and A. M. Al-Samman, "A comprehensive review on coordinated multi-point operation for lte-a," in*Comput. Netw.*, vol. 123, pp. 19–37, 2017.
- [32] F. Irram, M. Ali, Z. Maqbool, F. Qamar, and J. J. Rodrigues, "Coordinated multi-point transmission in 5G and beyond heterogeneous networks," in *Proc. IEEE Int. Multitopic Confe.*, 2020, pp. 1–6.
- [33] L.-H. Shen, C.-Y. Su, and K.-T. Feng, "CoMP enhanced subcarrier and power allocation for multi-numerology based 5g-NR networks," *IEEE Trans. Veh. Technol.*, vol. 71, no. 5, pp. 5460–5476, May 2022.
- [34] M. S. J. Solaija, H. Salman, A. B. Kihero, M. ˙I. Sa ˘glam, and H. Arslan, "Generalized coordinated multipoint framework for 5G and beyond," IEEE Access, vol. 9, pp. 72499–72515, 2021.
- [35] W. Jiang, B. Han, M. A. Habibi, and H. D. Schotten, "The road towards 6G: A comprehensive survey," *IEEE Open J. Commun. Soc.*, vol. 2, pp. 334–366, 2021.
- [36] S. Luo, X. Chen, Q. Wu, Z. Zhou, and S. Yu, "HFEL: Joint edge association and resource allocation for cost-efficient hierarchical federated edge learning," *IEEE Trans. Wireless Commun.*, vol. 19, no. 10, pp. 6535–6548, Oct. 2020.
- [37] C. Ma, X. Li, B. Huang, G. Li, and F. Li, "Personalized client-edge-cloud hierarchical federated learning in mobile edge computing," in *J. Cloud Comput.*, vol. 13, 2024, Art. no. 161.
- [38] Q. Wu et al., "Hiflash: Communication-efficient hierarchical federated learning with adaptive staleness control and heterogeneity-aware clientedge association," *IEEE Trans. Parallel Distrib. Syst.*, vol. 34, no. 5, pp. 1560–1579, May 2023.
- [39] D. S. Alqattan et al., "Security assessment of hierarchical federated deep learning," in *Proc. ICANN*, 2024, pp. 202–217.
- [40] P. Mitra and S. Ulukus, "Timely asynchronous hierarchical federated learning: Age of convergence," in *Proc. IEEE WiOpt*, 2023, pp. 509–515.
- [41] Y. Liu, Y. Deng, M. Elkashlan, A. Nallanathan, and G. K. Karagiannidis, "Analyzing grant-free access for URLLC service," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 3, pp. 741–755, Mar. 2021.
- [42] D.-J. Han, M. Choi, J. Park, and J. Moon, "FEDMES: Speeding up federated learning with multiple edge servers," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3870–3885, Dec. 2021.
- [43] W. Fang, D.-J. Han, and C. G. Brinton, "Submodel partitioning in hierarchical federated learning: Algorithm design and convergence analysis," in *Proc. IEEE ICC*, 2024, pp. 268–273.
- [44] X. Li, K. Huang, W. Yang, S. Wang, and Z. Zhang, "On the convergence of fedavg on non-IID data," *Proc. ICLR*, 2019. [Online]. Available: [https:](https://openreview.net/forum{?}id$=$HJxNAnVtDS) [//openreview.net/forum?id=HJxNAnVtDS](https://openreview.net/forum{?}id$=$HJxNAnVtDS)
- [45] W. Fang, Z. Yu, Y. Jiang, Y. Shi, C. N. Jones, and Y. Zhou, "Communication-efficient stochastic zeroth-order optimization for federated learning," *IEEE Trans. Signal Process.*, vol. 70, pp. 5058–5073, 2022.
- [46] S. Wang et al., "Adaptive federated learning in resource constrained edge computing systems," *IEEE J. Sel. Areas Commun.*, vol. 37, no. 6, pp. 1205–1221, Jun. 2019.
- [47] H. T. Nguyen, V. Sehwag, S. Hosseinalipour, C. G. Brinton, M. Chiang, and H. V. Poor, "Fast-convergent federated learning," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 1, pp. 201–218, Jan. 2021.
- [48] M. M. Amiri, D. Gündüz, S. R. Kulkarni, and H. V. Poor, "Convergence of update aware device scheduling for federated learning at the wireless edge," *IEEE Trans. Wireless Commun.*, vol. 20, no. 6, pp. 3643–3658, Jun. 2021.
- [49] A. Reisizadeh, A. Mokhtari, H. Hassani, A. Jadbabaie, and R. Pedarsani, "FEDPAQ: A communication-efficient federated learning method with periodic averaging and quantization," in *Proc. PMLR AISTATS*, pp. 2021– 2031, 2020.
- [50] Y. Zhang, M. J. Wainwright, and J. C. Duchi, "Communication-efficient algorithms for statistical optimization," in *Proc. Adv. Neural Inf. Process. Syst.*, 2012.
- [51] S. U. Stich, "Local SGD converges fast and communicates little," in *Proc. ICLR* , pp. 1511–1519, 2018. [Online]. Available: [https://openreview.net/](https://openreview.net/forum{?}id$=$S1g2JnRcFX) [forum?id=S1g2JnRcFX](https://openreview.net/forum{?}id$=$S1g2JnRcFX)

- [52] K. Bonawitz, "Towards federated learning at scale: System design," in *Proc. Mach. Learn. Syst.*, vol. 1, pp. 374–388, 2019.
- [53] Y. Zhao, M. Li, L. Lai, N. Suda, D. Civin, and V. Chandra, "Federated learning with non-IID data," 2018, doi: [10.48550/arXiv.1806.00582.](https://dx.doi.org/10.48550/arXiv.1806.00582)
- [54] L. Lyu, H. Yu, and Q. Yang, "Threats to federated learning: A survey," 2020, doi: [10.48550/arXiv.2003.02133.](https://dx.doi.org/10.48550/arXiv.2003.02133)
- [55] E. STANDARD, "Final draft etsi es 203 228 v1. 2.0 (2017-02)," 2017. [Online]. Available: [https://www.etsi.org/deliver/etsi\\_es/203200\\_](https://www.etsi.org/deliver/etsi_es/203200_203299/203228/01.02.00_50/es_203228v010200m.pdf) [203299/203228/01.02.00\\_50/es\\_203228v010200m.pdf](https://www.etsi.org/deliver/etsi_es/203200_203299/203228/01.02.00_50/es_203228v010200m.pdf)
- [56] H. Qi et al., "Bridge the present and future: A cross-layer matching game in dynamic cloud-aided mobile edge networks," *IEEE Trans. Mobile Comput.*, vol. 23, no. 12, pp. 12522–12539, Dec. 2024.
- [57] R. Fezeu, A. Brunstrom, M. Flores, and M. Fiore, "An in-depth measurement analysis of 5G Mmwave PHY latency and its impact on end-to-end delay," in *Proc. PAM*, 2023, pp. 284–312.
- [58] M. Agiwal, A. Roy, and N. Saxena, "Next generation 5G wireless networks: A comprehensive survey," *IEEE Commun. Surv. Tut.*, vol. 18, no. 3, pp. 1617–1655, thirdquarter 2016.
- [59] M. S. H. Abad, E. Ozfatura, D. Gunduz, and O. Ercetin, "Hierarchical federated learning ACROSS heterogeneous cellular networks," in *Proc. IEEE Int. Conf. Acoust., Speech Signal Process.*, 2020, pp. 8866–8870.
- [60] J. Wu et al., "Hierarchical personalized federated learning for user modeling," in *Proc. ACM Web Conf.*, 2021, pp. 957–968.
- [61] D. Gao, C. Ju, X. Wei, Y. Liu, T. Chen, and Q. Yang, "Hhhfl: Hierarchical heterogeneous horizontal federated learning for electroencephalography," 2019, *arXiv:1909.05784*.
- [62] J. Feng, L. Liu, Q. Pei, and K. Li, "Min-Max cost optimization for efficient hierarchical federated learning in wireless edge networks," *IEEE Trans. Parallel Distrib. Syst.*, vol. 33, no. 11, pp. 2687–2700, Nov. 2022.
- [63] A. Wainakh, A. S. Guinea, T. Grube, and M. Mühlhäuser, "Enhancing privacy via hierarchical federated learning," in *Proc. IEEE EuroS&PW*, 2020, pp. 344–347.
- [64] H. Zhou, Y. Zheng, H. Huang, J. Shu, and X. Jia, "Toward robust hierarchical federated learning in Internet of Vehicles," *IEEE Trans. Intell. Transp. Syst.*, vol. 24, no. 5, pp. 5600–5614, May 2023.
- [65] C. Feng, H. H. Yang, D. Hu, Z. Zhao, T. Q. Quek, and G. Min, "Mobilityaware cluster federated learning in hierarchical wireless networks," *IEEE Trans. Wireless Commun.*, vol. 21, no. 10, pp. 8441–8458, Oct. 2022.
- [66] X. Zhou et al., "Hierarchical federated learning with social context clustering-based participant selection for internet of medical things applications," *IEEE Trans. Comput. Soc. Syst.*, vol. 10, no. 4, pp. 1742–1751, Aug. 2023.
- [67] N. Mhaisen, A. A. Abdellatif, A. Mohamed, A. Erbad, and M. Guizani, "Optimal user-edge assignment in hierarchical federated learning based on statistical properties and network topology constraints," *IEEE Trans. Netw. Sci. Eng.*, vol. 9, no. 1, pp. 55–66, Jan./Feb. 2022.
- [68] Y. Guo, F. Liu, T. Zhou, Z. Cai, and N. Xiao, "Privacy vs. efficiency: Achieving both through adaptive hierarchical federated learning," *IEEE Trans. Parallel Distrib. Syst.*, vol. 34, no. 4, pp. 1331–1342, Apr. 2023.
- [69] Z. Qu, R. Duan, L. Chen, J. Xu, Z. Lu, and Y. Liu, "Context-aware online client selection for hierarchical federated learning," *IEEE Trans. Parallel Distrib. Syst.*, vol. 33, no. 12, pp. 4353–4367, Dec. 2022.
- [70] Z. Wang, H. Xu, J. Liu, Y. Xu, H. Huang, and Y. Zhao, "Accelerating federated learning with cluster construction and hierarchical aggregation," *IEEE Trans. Mobile Comput.*, vol. 22, no. 7, pp. 3805–3822, Jul. 2023.
- [71] L. Li, H. Xiong, Z. Guo, J. Wang, and C.-Z. Xu, "SmartPC: Hierarchical pace control in real-time federated learning system," in *Proc. IEEE RTSS*, 2019, pp. 406–418.
- [72] F. D. Rango, A. Guerrieri, P. Raimondo, and G. Spezzano, "HED-FL: A hierarchical, energy efficient, and dynamic approach for edge federated learning," *Pervasive Mobile Comput.*, vol. 92, 2023, Art. no. 101804.
- [73] C. Liu, T. J. Chua, and J. Zhao, "Time minimization in hierarchical federated learning," in *Proc. IEEE/ACM SEC*, 2022, pp. 96–106.
- [74] W. Fang, D.-J. Han, E. Chen, S. Wang, and C. Brinton, "Hierarchical federated learning with multi-timescale gradient correction," in *Proc. Adv. Neural Inf. Process. Syst.*, pp. 78863–78904, 2024.
- [75] S. M. Azimi-Abarghouyi and V. Fodor, "Quantized hierarchical federated learning: A robust approach to statistical heterogeneity," vol. 13, no. 7, pp. 12655–12672, 2024.
- [76] M.-F. Pervej and A. F. Molisch, "Personalized hierarchical split federated learning in wireless networks," in *Proc. IEEE ICC*, pp. 6118–6124, 2024, *arXiv:2411.06042*.
- [77] C. Briggs, Z. Fan, and P. Andras, "Federated learning with hierarchical clustering of local updates to improve training on non-IID data," in *Proc. IEEE Int. Joint Conf. Neural Netw.*, 2020, pp. 1–9.

- <span id="page-15-0"></span>[78] W. Y. B. Lim, J. S. Ng, Z. Xiong, D. Niyato, C. Miao, and D. I. Kim, "Dynamic edge association and resource allocation in self-organizing hierarchical federated learning networks," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3640–3653, Dec. 2021.
- [79] Y. Su, W. Fan, Q. Meng, P. Chen, and Y. Liu, "Joint adaptive aggregation and resource allocation for hierarchical federated learning systems based on edge-cloud collaboration," in*IEEE Trans. Cloud Comput.*, vol. 13, no. 1, pp. 369–382, Jan.–Mar. 2025.
- [80] Y. Liu, Z. Qu, and J. Wang, "Compressed hierarchical federated learning for edge-level imbalanced wireless networks," *IEEE Trans. Comput. Soc. Syst.*, vol. 12, no. 5, pp. 3131–3142, Oct. 2025.
- [81] Y. Jiang, D. Wang, B. Song, and S. Luo, "HDHRFL: A hierarchical robust federated learning framework for dual-heterogeneous and noisy clients," *Future Gener. Comput. Syst.*, vol. 160, 2024, pp. 185–196.
- [82] W. Y. B. Lim et al., "Decentralized edge intelligence: A dynamic resource allocation framework for hierarchical federated learning," *IEEE Trans. Parallel Distrib. Syst.*, vol. 33, no. 3, pp. 536–550, Mar. 2022.
- [83] Z. Wang, H. Xu, J. Liu, H. Huang, C. Qiao, and Y. Zhao, "Resource-Efficient federated learning with hierarchical aggregation in Edge computing," in *Proc. IEEE INFOCOM*, 2021, pp. 1–10.
- [84] A. Kawnine, H. Cao, A. N. Mih, and M. Wachowicz, "Evaluating multiglobal server architecture for federated learning," in *Proc. IEEE ICCE*, 2024, pp. 1–6.
- [85] B. Ganguly et al., "Multi-edge server-assisted dynamic federated learning with an optimized floating aggregation point," *IEEE/ACM Trans. Netw.*, vol. 31, no. 6, pp. 2682–2697, Dec. 2023.
- [86] Z. Qu, X. Li, J. Xu, B. Tang, Z. Lu, and Y. Liu, "On the convergence of multi-server federated learning with overlapping area," *IEEE Trans. Mobile Comput.*, vol. 22, no. 11, pp. 6647–6662, Nov. 2023.
- [87] D. C. Nguyen, S. Hosseinalipour, D. J. Love, P. N. Pathirana, and C. G. Brinton, "Latency optimization for blockchain-empowered federated learning in multi-server edge computing," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 12, pp. 3373–3390, Dec. 2022.
- [88] H. Guo, W. Huang, J. Liu, and Y. Wang, "Inter-server collaborative federated learning for ultra-dense edge computing," *IEEE Trans. Wireless Commun.*, vol. 21, no. 7, pp. 5191–5203, Jul. 2022.
- [89] M. Diamanti, A. B. Rahman, P. Charatsaris, E. E. Tsiropoulou, and S. Papavassiliou, "Resource allocation and pricing for multi-server multimodel federated learning based on market equilibrium," *Future Gener. Comput. Syst.*, vol. 175, 2025, Art. no. 10805.
- [90] T. S. Nguyen, T. Lepoint, and N. Trieu, "Mario: Multi-round multipleaggregator secure aggregation with robustness against malicious actors," in *Proc. IEEE EuroS&P*, 2025, pp. 1140–1164.
- [91] C. Thapa, M. A. P. Chamikara, and S. A. Camtepe, "Advancements of federated learning towards privacy preservation: From federated learning to split learning," in *Federated Learn. Systems: Towards Next-Generation AI.* Cham, Switzerland: Springer, 2021, pp. 79–109.

![](_page_15_Picture_16.jpeg)

**Haiyun Liu** (Student Member, IEEE) received the BS degree in electrical engineering and automation from Shanghai University, Shanghai, China, in 2019, and the MS degree in signal and information processing from Sichuan University, Chengdu, China, in 2023. He is currently working toward the PhD degree with the Department of Computer Science and Engineering, University of South Florida, Tampa, FL, USA. His research interests include security and privacy in wireless communications, and federated learning for networks.

![](_page_15_Picture_18.jpeg)

**Jiahao Xue** (Student Member, IEEE) received the BS degree from the Huazhong University of Science and Technology, Wuhan, China, in 2018, and the MS degree from the University of California Santa Cruz, Santa Cruz, CA, USA, in 2021. He is currently working toward the PhD degree in systems and security with the Department of Electrical Engineering, University of South Florida, Tampa, FL, USA. His primary research interests include network and mobile system security, and machine learning for networks.

![](_page_15_Picture_20.jpeg)

**Jie Xu** received the BS and MS degrees in electronic engineering from Tsinghua University, Beijing, China, in 2008 and 2010, respectively, and the PhD degree in electrical engineering from UCLA, in 2015. He is currently an associate professor with the Department of Electrical and Computer Engineering, University of Florida. His research interests include mobile edge computing/intelligence, machine learning for networks, and network security. He was the recipient of the NSF CAREER Award, in 2021.

![](_page_15_Picture_22.jpeg)

**Yao Liu** (Senior Member, IEEE) received the PhD degree in computer science from North Carolina State University, USA, in 2012. She is currently a professor with the Department of Computer Science and Engineering, University of South Florida. Her research interests include in the security applications for cyberphysical systems, Internet of Things, and machine learning. She was an NSF CAREER Award recipient in 2016. She also received the ACM CCS Test-of-Time Award by ACM SIGSAC in 2019.

![](_page_15_Picture_24.jpeg)

**Zhuo Lu** (Senior Member, IEEE) received the PhD degree from North Carolina State University, in 2013. He is currently an associate professor with the Department of Electrical Engineering, University of South Florida. His research interests include both theoretical and system perspectives on communication, network, and security. He was the recipient of the NSF CISE CRII award in 2016, the Best Paper Award from IEEE GlobalSIP in 2019, and the NSF CAREER award in 2021.
---
title: "Vertical Federated Learning Over Cloud-RAN: Convergence Analysis and System Optimization"
tema_principal: fl_ran
temas_relacionados: []
ano: 2023
autores: []
veiculo: null
pdf: ../pdf/vertical_federated_learning_over_cloud-ran_convergence_analysis_and_system_optimization.pdf
---

# Vertical Federated Learning Over Cloud-RAN: Convergence Analysis and System Optimization

Yuanming Shi [,](https://orcid.org/0000-0002-1418-7465) *Senior Member, IEEE*, Shuhao Xi[a](https://orcid.org/0000-0002-7887-2453) , *Graduate Student Member, IEEE*, Yong Zhou [,](https://orcid.org/0000-0002-7499-6256) *Senior Member, IEEE*, Yijie Ma[o](https://orcid.org/0000-0001-5077-2998) , *Member, IEEE*, Chunxiao Jiang [,](https://orcid.org/0000-0002-3703-121X) *Senior Member, IEEE*, and Meixia Tao [,](https://orcid.org/0000-0002-0799-0954) *Fellow, IEEE*

*Abstract*— Vertical federated learning (FL) is a collaborative machine learning framework that enables devices to learn a global model from the feature-partition datasets without sharing local raw data. However, as the number of the local intermediate outputs is proportional to the training samples, it is critical to develop communication-efficient techniques for wireless vertical FL to support high-dimensional model aggregation with full device participation. In this paper, we propose a novel cloud radio access network (Cloud-RAN) based vertical FL system to enable fast and accurate model aggregation by leveraging over-the-air computation (AirComp) and alleviating communication straggler issue with cooperative model aggregation among geographically distributed edge servers. However, the model aggregation error caused by AirComp and quantization errors caused by the limited fronthaul capacity degrade the learning performance for vertical FL. To address these issues, we characterize the convergence behavior of the vertical FL algorithm considering both uplink and downlink transmissions. To improve the learning performance, we establish a system optimization framework by joint transceiver and fronthaul quantization design, for which successive convex approximation and alternate convex search based system optimization algorithms are developed. We conduct extensive simulations to demonstrate the effectiveness of the proposed system architecture and optimization framework for vertical FL.

*Index Terms*— Vertical federated learning, cloud radio access network, over-the-air computation.

Manuscript received 22 November 2022; revised 27 April 2023; accepted 15 June 2023. Date of publication 27 June 2023; date of current version 13 February 2024. The work of Yuanming Shi was supported in part by the National Natural Science Foundation of China under Grant 62271318, in part by the Natural Science Foundation of Shanghai under Grant 21ZR1442700, and in part by the Shanghai Rising-Star Program under Grant 22QA1406100. The work of Yong Zhou was supported in part by the National Natural Science Foundation of China under Grant 62001294 and Grant 61971286 and in part by the Natural Science Foundation of Shanghai under Grant 23ZR1442800. The work of Meixia Tao was supported in part by the National Natural Science Foundation of China under Grant 62125108. The associate editor coordinating the review of this article and approving it for publication was Y. Shu. *(Corresponding author: Yong Zhou.)*

Yuanming Shi, Shuhao Xia, Yong Zhou, and Yijie Mao are with the School of Information Science and Technology, ShanghaiTech University, Shanghai 201210, China (e-mail: shiym@shanghaitech.edu.cn; xiashh@shanghaitech.edu.cn; zhouyong@shanghaitech.edu.cn; maoyj@ shanghaitech.edu.cn).

Chunxiao Jiang is with the Tsinghua Space Center and the Beijing National Research Center for Information Science and Technology, Tsinghua University, Beijing 100084, China (e-mail: jchx@tsinghua.edu.cn).

Meixia Tao is with the Department of Electronic Engineering, Shanghai Jiao Tong University, Shanghai 201210, China (e-mail: mxtao@sjtu.edu.cn).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TWC.2023.3288122.

Digital Object Identifier 10.1109/TWC.2023.3288122

## <span id="page-0-3"></span><span id="page-0-2"></span><span id="page-0-1"></span><span id="page-0-0"></span>I. INTRODUCTION

F EDERATED learning (FL), as an emerging distributed learning paradigm, has recently attracted lots of attention by enabling devices to collaboratively learn a global machine learning (ML) model without local data exchanging to protect data privacy [\[1\]. B](#page-13-0)ased on the partition of datasets, FL is typically categorized into horizontal FL and vertical FL [\[2\].](#page-13-1) Specifically, horizontal FL is adopted in the sample-partition scenario where different devices share the same feature space but have different samples [\[3\], as](#page-13-2) shown in Fig. [1\(a\).](#page-1-0) Vertical FL, on the other hand, enables devices to collaboratively learn a global model from the feature-partition datasets that share the same sample space but different feature spaces [\[4\],](#page-13-3) as shown in Fig. [1\(b\).](#page-1-0) Vertical FL has wide applications across e-commerce, smart healthcare, and Internet of Things (IoT). For example, in IoT networks, data collected by different types of sensors (e.g., video cameras, GPS, and inertial measurement units) need to be smartly fused for planning and decisionmaking [\[5\], \[](#page-13-4)[6\]. A](#page-13-5)s each participant owns partial model in vertical FL, the messages exchanged between participants are based on the intermediate outputs of the sub-model and its local data, rather than local updates as in horizontal FL. The number of intermediate outputs is proportional to the number of training samples. This leads to high-dimensional data transmission with a large volume of training samples [\[7\].](#page-14-0) In addition, since vertical FL needs to aggregate all local intermediate outputs to obtain the final prediction, it requires all devices to participate in the training process in vertical FL. Therefore, the high-dimensional data transmission with full device participation in vertical FL brings a unique challenge for communication-efficient system design. Existing works on device selections in horizontal FL cannot address this issue in wireless vertical FL.

<span id="page-0-8"></span><span id="page-0-7"></span><span id="page-0-6"></span><span id="page-0-5"></span><span id="page-0-4"></span>To design communication-efficient wireless vertical FL, it is critical to develop novel wireless techniques to transmit intermediate outputs over shared wireless medium with limited radio resources [\[8\]. C](#page-14-1)onventional orthogonal multiple access schemes aim to decode individual information, which however ignores the communication task for data transmission. Instead, over-the-air computation (AirComp) serves as a promising approach to enable efficient aggregation for FL [\[9\], \[](#page-14-2)[10\],](#page-14-3) [\[11\],](#page-14-4) [\[12\].](#page-14-5) By exploiting waveform superposition of multiple access channel, AirComp can directly aggregate the local updates via concurrent uncoded transmission [\[13\]. A](#page-14-6)s a

1536-1276 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

<span id="page-1-0"></span>![](_page_1_Figure_2.jpeg)

Fig. 1. Sample and feature spaces of horizontal and vertical FL.

<span id="page-1-4"></span><span id="page-1-2"></span><span id="page-1-1"></span>result, AirComp can reduce the required radio resources and the access latency compared with orthogonal multiple access schemes [\[14\].](#page-14-7) To further improve the communication and learning efficiency of wireless FL with AirComp, the intrinsic properties of the local updates are exploited, e.g., gradient sparsity [\[15\], t](#page-14-8)emporal correlation [\[16\],](#page-14-9) spatial correlation [\[17\],](#page-14-10) and gradient statistics [\[18\].](#page-14-11) However, due to the heterogeneity of channel conditions across different devices, AirComp based FL inevitably suffers from the communication stragglers, i.e., the devices with the weak channel conditions [\[19\],](#page-14-12) [\[20\].](#page-14-13) Specifically, the communication straggler devices enforcing the magnitude alignment for AirComp may result in high model aggregation error, which degrades the learning performance. Although it can be alleviated by excluding the stragglers from the model aggregation process [\[21\],](#page-14-14) [\[22\],](#page-14-15) partial device participation reduces the size of the FL training datasets, which deteriorates the performance for FL models. Besides, these works mainly focus on horizontal FL with partial device selection and are inapplicable in the vertical FL scenario. The reason is that vertical FL requires all the devices to participate the training process since each device owns one sub-model of the global model. It is thus critical to design a novel AirComp-based transmission scheme for wireless vertical FL with full device participation.

To enable all devices including the straggler devices to participate in the training process, one approach is to improve the wireless channel quality through advanced communication technologies such as unmanned aerial vehicles [\[23\] a](#page-14-16)nd reconfigurable intelligent surface [\[24\],](#page-14-17) [\[25\],](#page-14-18) [\[26\].](#page-14-19) However, these wireless techniques may become inapplicable in the IoT scenarios with massive geographically distributed devices. An alternative approach is to effectively extend the wireless transmission coverage by deploying multiple edge servers, thereby cooperatively assisting data exchanges between the devices and the edge servers [\[27\],](#page-14-20) [\[28\],](#page-14-21) [\[29\].](#page-14-22) This can shorten the communication distances between the devices and the edge servers, which enhances the transmission reliability and reduces the latency for the straggler devices. A growing body of recent work has demonstrated the effectiveness of deploying multiple edge servers for FL, including semi-decentralized FL [\[30\] a](#page-14-23)nd hierarchical FL [\[31\],](#page-14-24) [\[32\].](#page-14-25) To mitigate inter-cluster interference, the authors in [\[30\] a](#page-14-23)nd [\[31\] p](#page-14-24)roposed to allocate orthogonal radio resource blocks for each device for model aggregation in FL. However, this orthogonal transmission scheme is inefficient due to the limited spectrum resources. In addition, many studies have considered distributed edge computing systems based on Cloud-RAN architecture with various communication metrics, such as energy consumption [\[33\] an](#page-14-26)d latency [\[34\], f](#page-14-27)or resource management.

<span id="page-1-15"></span><span id="page-1-14"></span><span id="page-1-13"></span>In this paper, we propose to leverage cloud radio access network (Cloud-RAN) to enable cooperative model aggregation across densely deployed multiple edge servers over large geographic areas. This is achieved by moving baseband processing from remote radio heads (RRHs) (i.e., edge servers) to a baseband unit (BBU) pool (i.e., central server), where digital fronthaul links connect the central server and the edge servers [\[35\]. T](#page-14-28)herefore, the learning performance and communication efficiency can be significantly improved through cooperative model aggregation and centralized signal processing for large-scale wireless vertical FL system. Besides, since the baseband signal processing and model aggregation are moved to the central server in the BBU pool, edge servers only need to support basic signal transmission functionality, which further reduces their energy consumption and deployment cost [\[35\], \[](#page-14-28)[36\].](#page-14-29)

<span id="page-1-17"></span><span id="page-1-16"></span><span id="page-1-7"></span><span id="page-1-6"></span><span id="page-1-5"></span><span id="page-1-3"></span>In addition, we propose a fast and reliable transmission scheme to support vertical FL with geographically distributed devices over wireless networks. Different from the existing works on vertical FL over wireless networks [\[37\], w](#page-14-30)e shall implement AirComp-based vertical FL over Cloud-RAN to support heterogeneous devices. However, the fronthaul links between the edge servers and the central server have limited capacity, which causes additional quantization error. Furthermore, the quantization error along with AirComp model aggregation error severely degrade the learning performance of vertical FL. The main purpose of this paper is to reveal the impact of limited fronthaul capacity and AirComp aggregation error on the learning performance and then optimize the Cloud-RAN enabled vertical FL system by jointly considering the learning performance and communication efficiency. The main contributions are summarized as follows:

- <span id="page-1-9"></span><span id="page-1-8"></span>• We propose a Cloud-RAN based network architecture for communication-efficient vertical FL to alleviate the communication straggler issue by leveraging the distributed edge servers with shortened communication distance between devices and edge servers. This is achieved by transmitting the intermediate outputs at each device to multiple edge servers (i.e., RRHs) via AirComp. The edge servers then compress the received aggregation signals and forward the quantized signals to the central server via digital fronthaul links for centralized global model aggregation in vertical FL.
- <span id="page-1-12"></span><span id="page-1-11"></span><span id="page-1-10"></span>• We characterize the convergence behaviors of the gradient-based vertical FL algorithm under AirComp model aggregation error and limited fronthaul capacity in both uplink and downlink transmission processes. We further propose a system optimization framework with joint transceiver and quantization design to minimize the learning optimality gap. The resulting system optimization problem is solved based on the

successive convex approximation and alternate convex search approaches with convergence guarantees.

We conduct extensive simulations to demonstrate the\neffectiveness of the proposed system optimization framework and system architecture. We demonstrate that the
proposed framework can effectively combat the effects of
communication limitations on the learning performance
of vertical FL in terms of the optimality gap. The superiority of the distributed antenna system in Cloud-RAN
for vertical FL is also demonstrated.

The remainder of this paper is constructed as follows. Section II introduces the learning framework of vertical FL and the communication model. Section III provides the convergence analysis of the vertical FL algorithm, and Section IV formulates the system optimization problem for resource allocation. Extensive numerical results of the proposed scheme are presented in Section V, followed by the conclusion in Section VI.

Throughout this paper, we denote the complex number set and the real number set by  $\mathbb{C}$  and  $\mathbb{R}$ . We denote scalars, vectors, and matrices by regular letters, bold small letters, and bold capital letters, respectively. The operations of transpose and conjugate transpose are respectively denoted by the superscripts  $(\cdot)^T$  and  $(\cdot)^H$ .  $\mathbb{E}[\cdot]$  denotes the expectation operator.  $\mathcal{N}(x; \mu, \Sigma)$  and  $\mathcal{C}\mathcal{N}(x; \mu, \Sigma)$  denote that the random variable x follows Gaussian distribution and complex Gaussian distribution with mean  $\mu$  and covariance  $\Sigma$ , respectively. We use I and  $\operatorname{diag}\{x\}$  to respectively denote the identity matrix and the diagonal matrix with diagonal entries specified by x. We denote real and imaginary components of x by  $\Re(x)$  and  $\Im(x)$ , respectively.

## II. SYSTEM MODEL

### <span id="page-2-0"></span>A. Vertical Federated Learning

Consider a vertical FL system consisting of K IoT devices and one central server, as shown in Fig. 2. Let  $\mathcal{D}$  $\{(\boldsymbol{x}_{i,1},\ldots,\boldsymbol{x}_{i,k}),y_i\}_{i=1}^L$  denote the whole training dataset of L samples, where  $x_{i,k} \in \mathbb{R}^{d_k}$  denotes the partial nonoverlapped features with dimension  $d_k$  of sample i located at device k, and  $y_i$  denotes the corresponding label only available at the central server [37]. We use the concatenated vector  $\bm{x}_i = [(\bm{x}_{i,1})^\mathsf{T}, \dots, (\bm{x}_{i,k})^\mathsf{T}]^\mathsf{T} \in \mathbb{R}^d$  to denote the whole feature vector of sample i with dimension  $d = \sum_{k=1}^{K} d_k$ . The goal of vertical FL is to collaboratively learn a global model w that maps an input  $x_i$  to the corresponding prediction through a continuously differentiable function  $h(w, x_i)$ . We assume that device k maps the local feature  $x_{i,k}$  to the local prediction result  $g_k(\boldsymbol{w}_k, \boldsymbol{x}_{i,k})$  using sub-model  $\boldsymbol{w}_k$ , where  $g_k(\cdot)$ is defined as the local prediction function. The dimension of each local prediction result is the same, which is determined by the number of classes for the classification task. For example, for a binary classification task, the local prediction result  $g_k(\boldsymbol{w}_k, \boldsymbol{x}_{i,k})$  is a scalar.

The input of the final prediction function  $h(\boldsymbol{w}, \boldsymbol{x}_i)$  is based on the aggregation of the local prediction results  $\{g_k(\boldsymbol{w}_k, \boldsymbol{x}_{i,k})\}$ . We assume the final prediction is obtained

by aggregating the local prediction results,<sup>1</sup> followed by a non-linear transformation  $\sigma(\cdot)$  (e.g., a softmax function) as follows:

<span id="page-2-2"></span>
$$h(\boldsymbol{w}, \boldsymbol{x}_i) = \sigma \left( \sum_{k=1}^K g_k(\boldsymbol{w}_k, \boldsymbol{x}_{i,k}) \right), \tag{1}$$

where w is the global model concatenated by the sub-models  $\{w_k\}$ , i.e.,  $w = \left[(w_1^\mathsf{T}, \cdots, w_K^\mathsf{T})\right]^\mathsf{T}$ . Based on (1), the central server can aggregate local prediction results without directly accessing local features and local model.

To learn the global model w, we focus on the following empirical risk minimization problem:

<span id="page-2-3"></span>
$$\min_{\boldsymbol{w} \in \mathbb{R}^d} F(\boldsymbol{w}) = \frac{1}{L} \sum_{i=1}^L f_i(\boldsymbol{w}) + \lambda \sum_{k=1}^K r_k(\boldsymbol{w}),$$
 (2)

where  $f_i(\cdot)$  is the sample-wise loss function indicating the loss between the prediction  $h(\boldsymbol{w}, \boldsymbol{x}_i)$  and the true label  $y_i$  for sample  $i, r_k(\cdot)$  is the regularization for the sub-model  $\boldsymbol{w}_k$  on device k, and  $\lambda$  is a hyperparameter.

In this paper, we consider using the full-batch gradient descent (GD) algorithm to solve (2). Let  $\nabla F(w)$  denote the gradient of  $F(\cdot)$  with respect to w, then we obtain

$$\nabla F(\boldsymbol{w}) = \frac{1}{L} \sum_{i=1}^{L} \begin{bmatrix} \nabla_1 f_i(\boldsymbol{w}) \\ \vdots \\ \nabla_K f_i(\boldsymbol{w}) \end{bmatrix} + \lambda \begin{bmatrix} \nabla r_1(\boldsymbol{w}) \\ \vdots \\ \nabla r_K(\boldsymbol{w}) \end{bmatrix}, \quad (3)$$

where  $\nabla_k f_i(\boldsymbol{w}) = \frac{\partial f_i(\boldsymbol{w})}{\partial \boldsymbol{w}_k}$  is the partial gradient of the loss function  $f_i(\cdot)$  with respect to the sub-model  $\boldsymbol{w}_k$ . Based on the chain rule in calculus, the partial gradient of  $\nabla_k f_i(\boldsymbol{w})$  can be rewritten as

<span id="page-2-4"></span>
$$\nabla_{k} f_{i}(\boldsymbol{w}) = f'_{i} \left( \sigma \left( \sum_{k=1}^{K} g_{k}(\boldsymbol{w}_{k}, \boldsymbol{x}_{i,k}) \right) \right)$$

$$\times \sigma' \left( \sum_{k=1}^{K} g_{k}(\boldsymbol{w}_{k}, \boldsymbol{x}_{i,k}) \right) \nabla g_{k,i}(\boldsymbol{w}_{k})$$

$$= G_{i} \left( \sum_{k=1}^{K} g_{k}(\boldsymbol{w}_{k}, \boldsymbol{x}_{i,k}) \right) \nabla g_{k,i}(\boldsymbol{w}_{k}), \quad (4)$$

where  $f_i'(\cdot)$  and  $\sigma'(\cdot)$  are the derivatives of  $f_i(\cdot)$  and  $\sigma(\cdot)$ ,  $\nabla g_{k,i}(\boldsymbol{w}_k) = \frac{\partial g_k(\boldsymbol{w}_k, \boldsymbol{x}_{i,k})}{\partial \boldsymbol{w}_k}$  is the partial gradient of the local prediction function  $g_k(\cdot)$  with respect to  $\boldsymbol{w}_k$ , and  $G_i(\cdot)$  is an auxiliary function with respect to the aggregation of local prediction results for sample i.

In vertical FL, the features are distributed at local devices and the labels are known by the central server, so the partial gradients can be calculated separately. Specifically, device k computes and uploads the local prediction result  $g_k(\boldsymbol{w}_k, \boldsymbol{x}_{i,k})$  to the central server. Then, the central server aggregates the local prediction results to obtain  $\sum_{k=1}^K g_k(\boldsymbol{w}_k, \boldsymbol{x}_{i,k})$  and broadcast  $G_i\left(\sum_{k=1}^K g_k(\boldsymbol{w}_k, \boldsymbol{x}_{i,k})\right)$  back to the devices. Consequently, the devices obtain the partial gradient  $\nabla_k f_i(\boldsymbol{w})$ 

<span id="page-2-1"></span><sup>1</sup>For a wide range of models such as logistic classification and support vector machines the intermediate outputs of these models are additive, i.e., the final inner product can be split into the sum of multiple inner products.

<span id="page-3-0"></span>![](_page_3_Figure_2.jpeg)

Fig. 2. Aggregation of local prediction results for the *i*-th training sample in vertical FL.

through Eq. (4) since  $\nabla g_{k,i}(\boldsymbol{w}_k)$  can be calculated locally. Each device then updates its local model by taking one step of gradient decent with learning rate  $\mu$ , i.e.,

<span id="page-3-2"></span>
$$\boldsymbol{w}_{k}^{(t+1)} = \boldsymbol{w}_{k}^{(t)} - \mu \left( \frac{1}{L} \sum_{i=1}^{L} \nabla_{k} f_{i}(\boldsymbol{w}^{(t)}) + \lambda \nabla r_{k}(\boldsymbol{w}^{(t)}) \right). \quad (5)$$

Algorithm 1 summarizes the above procedure. Since the central server only receives the aggregation of local prediction results, i.e., neither local features nor local models are uploaded to the central server, the privacy of local data can be guaranteed. Nevertheless, the number of local prediction results at each device is proportional to the number of training samples, which leads to high-dimensional data transmission. In addition, all devices are required to participate the training process in vertical FL since each device owns a sub-model  $w_k$ . Hence, it is essential to design communication efficient technologies for vertical FL in wireless networks to tame the challenge brought by the high-dimensional data transmission with full device participation.

## B. Over-the-Air Computation Based Cloud Radio Access Network

To enable fast aggregation with full device participation in vertical FL, we shall propose an AirComp based Cloud-RAN to support vertical FL over ultra dense wireless networks, where multiple RRHs serving as edge servers are coordinated by a centralized BBU pool serving as a central server, as shown in Fig. 3. In particular, the central server coordinates N edge servers with limited-capacity digital fronthaul links to serve K single-antenna devices. Each edge server is equipped with M antennas. Let  $C_n$  denote the fronthaul capacity of the link between edge server n and the central server. The fronthaul capacities need to satisfy an overall capacity constraint,

```
Algorithm 1 Error-Free Gradient-Based Algorithm for Vertical FL
```

```
Require: learning rate \mu, maximum communication
                     rounds T, initialization \{\boldsymbol{w}_k^{(0)}\}.
    Output: \boldsymbol{w}^{(T)} = \left[ (\boldsymbol{w}_1^{(T)})^\mathsf{T}, \dots, (\boldsymbol{w}_K^{(T)})^\mathsf{T} \right]^\mathsf{T}.
 1 for t = 0, 1, ..., T do
            each device k \in [K] do in parallel
 2
                 if t = 0 then
 3
                       Send the local prediction results
 4
                          \left\{g_k(\boldsymbol{w}_k^{(0)}, \boldsymbol{x}_{i,k})\right\}_{i=1}^L to the central server;
                 end
 5
 6
                       Compute \{\nabla_k f(\boldsymbol{w}^{(t)})\}_{i=1}^L via (4), and update the local model \boldsymbol{w}_k^{(t+1)} via (5);
                        Send the local prediction results
                          \left\{g_k(\boldsymbol{w}_k^{(t+1)}, \boldsymbol{x}_{i,k})\right\}_{i=1}^L to the central
                 end
10
           end
            the central server do
11
                 Receive and aggregate the local prediction
12
                   results \left\{\sum_{k=1}^K g_k(\boldsymbol{w}_k^{(t)}, \boldsymbol{x}_{i,k})\right\}_{i=1}^L;
                 Compute \left\{G_i\left(\sum_{k=1}^K g_k(\boldsymbol{w}_k^{(t)}, \boldsymbol{x}_{i,k})\right)\right\}_{i=1}^L
13
                   and broadcast it back to all the devices;
          end
14
15 end
```

i.e.,  $\sum_{n=1}^{N} C_n \leq C$ . We assume perfect synchronization<sup>2</sup> between among devices and perfect channel state information (CSI) between the edge servers to the devices is available to the central server and the devices.<sup>3</sup> The notations and parameters used in the system model are summarized in Table I. In the following, we introduce the communication models for the uplink and downlink transmission to vertically train the FL model, respectively.

1) Uplink Transmission Model: In the uplink transmission, we assume the devices communicate with the edge servers over a shared wireless multiple access channel via AirComp. In this case, the edge servers first receive the AirComp results of the local prediction results transmitted by the devices, and then forward the aggregated results to the central server. By exploiting the signal superposition property of a wireless multiple access channel, the central server directly processes the aggregated version of analog modulated local information simultaneously transmitted by the devices, which significantly reduces transmission latency.

<span id="page-3-5"></span><span id="page-3-3"></span><sup>2</sup>For the AirComp-based system, we can implement synchronization by sharing a reference-clock among the devices [38], or using the timing advance technique commonly adopted in 4G Long Term Evolution and 5G New Radio [39].

<span id="page-3-7"></span><span id="page-3-6"></span><span id="page-3-4"></span><sup>3</sup>The RRHs estimates the channel state information (CSI) by receiving pilot signals sent from devices [40].

TABLE I Important Notations

<span id="page-4-0"></span>

| Notation                                                                                                                                             | Definition                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| $\overline{K}$                                                                                                                                       | Number of edge devices                                       |
| N                                                                                                                                                    | Number of edge servers                                       |
| M                                                                                                                                                    | Number of antennas for each edge server                      |
| $C_n$                                                                                                                                                | Fronthaul capacity of edge server $n$                        |
| $L_{\perp}$                                                                                                                                          | Number of time slots (samples)                               |
| $\boldsymbol{h}_{\mathrm{UL},k,n}^{(t)}$                                                                                                             | Uplink channel between device $k$ and server $n$             |
| $\bm{h}_{{\rm UL},k,n}^{(t)} \ b_{{\rm UL},k}^{(t)} \ s_k^{(t)}(i) \ z_{{\rm UL},n}^{(t)}(i)$                                                        | Uplink transmit scalar for device $k$ in the $t$ -th round   |
| $s_k^{(t)}(i)$                                                                                                                                       | Uplink transmit signal for device $k$ in the $t$ -th round   |
| $z_{\mathrm{UL},n}^{(t)}(i)$                                                                                                                         | Uplink channel noise for RRH $n$ in the $t$ -th round        |
| $P_{\rm UL}$                                                                                                                                         | Maximum uplink transmit power                                |
| $\boldsymbol{q}_{\mathrm{UL},n}^{(t)}(i)$                                                                                                            | Uplink quantization noise for RRH $n$ in the $t$ -th round   |
| $P_{\mathrm{UL},n}^{(t)}(i)$ $Q_{\mathrm{UL},n}^{(t)}(i)$ $Q_{\mathrm{UL},n}^{(t)}(i)$ $h_{\mathrm{DL},k,n}^{(t)}(i)$ $p_{\mathrm{DL},k,n}^{(t)}(i)$ | Covariance matrix of $q_{\mathrm{UL},n}^{(t)}(i)$            |
| $n_{\mathrm{UL}}^{(t)}(i)$                                                                                                                           | Effective uplink noise in the t-th round                     |
| $\bm{h}_{\mathrm{DL},k,n}^{(t)}$                                                                                                                     | Downlink channel between device $k$ and server $n$           |
| $z_{\mathrm{DL},n}^{(t)}(i)$                                                                                                                         | Downlink channel noise for RRH $n$ in the $t$ -th round      |
| $P_{\rm DL}$                                                                                                                                         | Maximum downlink transmit power                              |
| $\boldsymbol{q}_{{\rm DL},n}^{(t)}(i)$                                                                                                               | Downlink quantization noise for RRH $n$ in the $t$ -th round |
| $\boldsymbol{q}_{\text{DL},n}^{(t)}(i) \ \boldsymbol{Q}_{\text{DL},n}^{(t)}$                                                                         | Covariance matrix of $q_{\mathrm{DL},n}^{(t)}(i)$            |
| $\frac{n_{\mathrm{DL}}^{(t)}(i)}{}$                                                                                                                  | Effective downlink noise in the t-th round                   |

The channels between the devices and the edge servers are assumed to be quasi-static flat-fading [41], [42], where the channel coefficients remain the same during one communication block. Each block is assumed to contain L time slots, so that each device is able to transmit an L-dimensional signal vector encoding local prediction results of L samples within one block.<sup>4</sup> We assume the devices complete the t-th communication round for model training in the t-th transmission block. Then, the received signal at edge server n during the i-th uplink transmission time slot in the t-th communication round is given by

$$\boldsymbol{y}_{\mathrm{UL},n}^{(t)}(i) = \sum_{k=1}^{K} \boldsymbol{h}_{\mathrm{UL},k,n}^{(t)} b_{\mathrm{UL},k}^{(t)} s_k^{(t)}(i) + \boldsymbol{z}_{\mathrm{UL},n}^{(t)}(i), \qquad (6)$$

where  $\boldsymbol{h}_{\mathrm{UL},k,n}^{(t)} \in \mathbb{C}^{M}$  is the uplink channel between device k and edge server n in the t-th communication round,  $b_{\mathrm{UL},k}^{(t)}$  denotes the transmit scalar,  $s_{k}^{(t)}(i) = g_{k}(\boldsymbol{w}_{k}^{(t)}, \boldsymbol{x}_{i,k})$  denotes the transmit signal, and  $\boldsymbol{z}_{\mathrm{UL},n}^{(t)}(i) \sim \mathcal{CN}(0,\sigma_{z}^{2})$  denotes the additive white Gaussian noise (AWGN) for edge server n. Without loss of generality, we assume that the transmit signals  $\{s_{k}^{(t)}(i)\}$  follow the standard Gaussian distribution,  $s_{k}^{(t)}(i) \sim \mathcal{N}(0,1)$ . Hence, the transmit power constraint of

each device k is written as

<span id="page-4-6"></span><span id="page-4-5"></span>
$$\mathbb{E}\left[|b_{\mathrm{UL},k}^{(t)}s_k^{(t)}(i)|^2\right] = |b_{\mathrm{UL},k}^{(t)}|^2 \mathbb{E}[(s_k^{(t)}(i))^2] \le \left|b_{\mathrm{UL},k}^{(t)}\right|^2 \le P_{\mathrm{UL}},\tag{7}$$

where  $P_{\mathrm{UL}}$  is the maximum transmit power for each device

To forward the received signals to the central server through the limited fronthaul links, edge server n quantizes the received signal  $\boldsymbol{y}_{\mathrm{UL},n}^{(t)}(i)$  and then sends the quantized signals to the central server. In this paper, we use compression-based strategies to transmit the information between the central server and edge servers via fronthaul links. By adopting Gaussian quantization test channel,  $^6$  the quantized signal  $\tilde{\boldsymbol{y}}_{\mathrm{UL},n}^{(t)}(i)$  received at the central server from edge server n can be modeled as [43]

<span id="page-4-4"></span>
$$\tilde{\boldsymbol{y}}_{\mathrm{UL},n}^{(t)}(i) = \boldsymbol{y}_{\mathrm{UL},n}^{(t)}(i) + \boldsymbol{q}_{\mathrm{UL},n}^{(t)}(i), \tag{8}$$

where  $q_{\mathrm{UL},n}^{(t)}(i) \in \mathbb{C}^M \sim \mathcal{CN}\left(\mathbf{0}, Q_{\mathrm{UL},n}^{(t)}\right)$  denotes the quantization noise and  $Q_{\mathrm{UL},n}^{(t)}$  is the diagonal covariance matrix of the quantization noise for edge server n. The quantization noise level directly provides an indication of the accuracy of  $\tilde{y}_{\mathrm{UL},n}^{(t)}(i)$ . On the other hand, the level of the quantization noise indicates the amount of fronthaul capacity required for compression. In general, higher fronthaul capacity results in better compression resolution and less quantization noise.

<span id="page-4-7"></span><span id="page-4-3"></span> $^6$ To model the cost for transmitting high fidelity version of  $\boldsymbol{y}_{\mathrm{UL},n}^{(t)}(i)$ , we study a theoretical quantization model by viewing Eq. (8) as a test channel based on the rate-distortion [43]. The results can be extended to the other quantization schemes, i.e., uniform scalar quantization schemes.

<span id="page-4-1"></span><sup>&</sup>lt;sup>4</sup>For large data sample size, the local prediction results can be transmitted within multiple consecutive coherence blocks, which will be left in the future work.

<span id="page-4-2"></span><sup>&</sup>lt;sup>5</sup>Each neuron in a neural network receives multiple input signals that vary randomly during both forward and backward propagation. Due to the central limit theorem, the sum of these random variables tends to be Gaussian distributed.

<span id="page-5-0"></span>![](_page_5_Picture_2.jpeg)

Fig. 3. AirComp-based Cloud-RAN network for vertical FL.

Based on the rate-distortion theory, the fronthaul rates of Nedge servers at the i-th time slot in the t-th communication round should satisfy [44, Ch. 3]

<span id="page-5-3"></span>
$$\begin{split} &\sum_{n=1}^{N} C_{\mathrm{UL},n}^{(t)} \\ &= \sum_{n=1}^{N} I\left(\boldsymbol{y}_{\mathrm{UL},n}^{(t)}(i); \tilde{\boldsymbol{y}}_{\mathrm{UL},n}^{(t)}(i)\right) \\ &= \sum_{n=1}^{N} \log \frac{\left|\sum_{k=1}^{K} |b_{\mathrm{UL},k}^{(t)}|^{2} \boldsymbol{h}_{\mathrm{UL},k,n}^{(t)}(\boldsymbol{h}_{\mathrm{UL},k,n}^{(t)})^{\mathsf{H}} + \sigma_{z}^{2} \boldsymbol{I} + \boldsymbol{Q}_{\mathrm{UL},n}^{(t)}\right|}{\left|\boldsymbol{Q}_{\mathrm{UL},n}^{(t)}\right|} \\ &\leq \log \frac{\left|P_{\mathrm{UL}} \sum_{k=1}^{K} \boldsymbol{h}_{\mathrm{UL},k}^{(t)}(\boldsymbol{h}_{\mathrm{UL},k}^{(t)})^{\mathsf{H}} + \sigma_{z}^{2} \boldsymbol{I} + \boldsymbol{Q}_{\mathrm{UL}}^{(t)}\right|}{\left|\boldsymbol{Q}_{\mathrm{UL}}^{(t)}\right|} \\ &\leq C, \end{split} \tag{9}$$

where I(X;Y) denotes the mutual information between input X and output Y,  $\boldsymbol{h}_{\mathrm{UL},k}^{(t)}$  is the concatenated channel vector of  $\{\bm{h}_{\mathrm{UL},k,1}^{(t)}\}$ , and  $\bm{Q}_{\mathrm{UL}}^{(t)}$  is the uplink covariance matrix defined by  $\boldsymbol{Q}_{\mathrm{UL}}^{(t)} = \mathrm{diag}\left\{\boldsymbol{Q}_{\mathrm{UL},1}^{(t)}, \ldots, \boldsymbol{Q}_{\mathrm{UL},N}^{(t)}\right\}$ . Stacking the quantized signals  $\{\tilde{\boldsymbol{y}}_{\mathrm{UL}}^{(t)}(i)\}$  transmitted from

all edge servers yields

$$\tilde{\pmb{y}}_{\text{UL}}^{(t)}(i) = \sum_{k=1}^{K} \pmb{h}_{\text{UL},k}^{(t)} b_{\text{UL},k}^{(t)} s_k^{(t)}(i) + \pmb{z}_{\text{UL}}^{(t)}(i) + \pmb{q}_{\text{UL}}^{(t)}(i),$$

where

$$\begin{aligned} \boldsymbol{z}_{\text{UL}}^{(t)}(i) &= \left[ \left( \boldsymbol{z}_{\text{UL},1}^{(t)}(i) \right)^{\text{H}}, \ldots, \left( \boldsymbol{z}_{\text{UL},N}^{(t)}(i) \right)^{\text{H}} \right]^{\text{H}}, \ \boldsymbol{q}_{\text{UL}}^{(t)}(i) &= \left[ \left( \boldsymbol{q}_{\text{UL},1}^{(t)}(i) \right)^{\text{H}}, \ldots, \left( \boldsymbol{q}_{\text{UL},N}^{(t)}(i) \right)^{\text{H}} \right]^{\text{H}}. \end{aligned}$$

We design receive beamforming vectors at the central server for  $\tilde{\boldsymbol{y}}_{\mathrm{UL}}^{(t)}(i)$ , and take the real part to estimate the aggregation of local predictions  $s^{(t)}(i) = \sum_{k=1}^{K} g_k(\boldsymbol{x}_{i,k}; \boldsymbol{w}_k^{(t)})$ , through the following procedure

<span id="page-5-4"></span><span id="page-5-1"></span>
$$\hat{s}^{(t)}(i) = \frac{1}{\sqrt{\eta^{(t)}}} \Re((\boldsymbol{m}^{(t)})^{\mathsf{H}} \tilde{\boldsymbol{y}}_{\mathrm{UL}}^{(t)}(i))$$

$$= \frac{1}{\sqrt{\eta^{(t)}}} \Re\left((\boldsymbol{m}^{(t)})^{\mathsf{H}} \sum_{k=1}^{K} \boldsymbol{h}_{\mathrm{UL},k}^{(t)} b_{\mathrm{UL},k}^{(t)} s_{k}^{(t)}(i)\right) + n_{\mathrm{UL}}^{(t)}(i),$$
(10)

where  $n_{\text{UL}}^{(t)}(i) = \frac{1}{\sqrt{n^{(t)}}} \Re \left( (\boldsymbol{m}^{(t)})^{\mathsf{H}} \left( \boldsymbol{z}_{\text{UL}}^{(t)}(i) + \boldsymbol{q}_{\text{UL}}^{(t)} \right) \right)$  is the effective uplink noise, and  $\boldsymbol{m}^{(t)} = [(\boldsymbol{m}_1^{(t)})^{\mathsf{H}}, \dots, (\boldsymbol{m}_N^{(t)})^{\mathsf{H}}]^{\mathsf{H}} \in \mathbb{C}^{NM}$  is the receive beamforming vector and  $\boldsymbol{\eta}^{(t)}$  is the power control factor. Given  $\boldsymbol{m}^{(t)}$  and  $\boldsymbol{\eta}^{(t)}$ , the effective uplink noise is distributed as  $n_{\text{III}}^{(t)}(i) \sim \mathcal{N}(0, \sigma_{\text{III}}^2(t))$  with the variance

<span id="page-5-2"></span>
$$\sigma_{\mathrm{UL}}^{2}(t) = \frac{1}{2\eta^{(t)}} (\boldsymbol{m}^{(t)})^{\mathsf{H}} \left( \sigma_{z}^{2} \boldsymbol{I} + \boldsymbol{Q}_{\mathrm{UL}}^{(t)} \right) \left( \boldsymbol{m}^{(t)} \right). \tag{11}$$

2) Downlink Transmission Model: After obtaining the estimate  $\hat{s}^{(t)}(i)$ , the central server computes  $G_i\left(\hat{s}^{(t)}(i)\right)$  based on the noisy aggregation  $\hat{s}^{(t)}(i)$  and then broadcasts the result back to the devices. The central server first computes the beamformed signals to encode  $G_i(\hat{s}^{(t)}(i))$ , and then send them to the edge servers over the limited fronthaul links in the t-th communication round. The edge servers directly broadcast the beamformed signals to the devices over the wireless fading channels. The resulting transmit signal at the central server for edge server n is given as  $\tilde{\pmb{r}}_{\mathrm{DL},n}^{(t)}(i) = \pmb{u}_n^{(t)}G_i\left(\hat{s}^{(t)}(i)\right)$ , where  $\boldsymbol{u}_n^{(t)} \in \mathbb{C}^M$  is the transmit beamforming vector at edge server

Similar to the uplink transmission, these signals are then compressed and sent to the edge servers over the finite-capacity fronthaul link. The compression noise is mod-

$$\mathbf{r}_{{\rm DL},n}^{(t)}(i) = \tilde{\mathbf{r}}_{{\rm DL},n}^{(t)}(i) + \mathbf{q}_{{\rm DL},n}^{(t)}(i), \quad \forall i \in [L],$$
 (12)

where  $r_{\mathrm{DL},n}^{(t)}(i)$  is the reconstructed signal that edge server n actually broadcasts to the devices, and  $q_{\mathrm{DL},n}^{(t)}(i) \in \mathbb{C}^{M} \sim$  $\mathcal{CN}(\mathbf{0}, \mathbf{Q}_{\mathrm{DL},n}^{(t)})$  denotes the downlink quantization noise with the covariance matrix  $Q_{\mathrm{DL}}^{(t)}$ 

Without loss of generality, we assume that the transmit signal follows the standard Gaussian distribution, i.e.,  $G_i\left(\hat{s}^{(t)}(i)\right) \sim \mathcal{N}(0,1)$ , the transmit power for all edge servers should satisfy

<span id="page-6-4"></span>
$$\sum_{n=1}^{N} \mathbb{E}\left[\|\boldsymbol{r}_{\mathrm{DL},n}^{(t)}(i)\|^{2}\right]$$

$$= \sum_{n=1}^{N} \mathbb{E}\left[\|\boldsymbol{u}_{n}^{(t)}G_{i}\left(\hat{s}^{(t)}(i)\right)\|^{2}\right] + \sum_{n=1}^{N} \mathrm{Tr}(\boldsymbol{Q}_{\mathrm{DL},n}^{(t)})$$

$$= \|\boldsymbol{u}^{(t)}\|^{2} + \mathrm{Tr}(\boldsymbol{Q}_{\mathrm{DL}}^{(t)}) \leq P_{\mathrm{DL}}, \tag{13}$$

where  $P_{\mathrm{DL}}$  is the maximum total transmit power for all edge servers,  $\boldsymbol{u}^{(t)} = [(\boldsymbol{u}_1^{(t)})^{\mathrm{H}}, \dots, (\boldsymbol{u}_N^{(t)})^{\mathrm{H}}]^{\mathrm{H}}$  is the concatenated transmit beamforming vector, and  $\boldsymbol{Q}_{\mathrm{DL}}^{(t)}$  is the downlink covariance matrix defined by  $\boldsymbol{Q}_{\mathrm{DL}}^{(t)} = \mathrm{diag}\{\boldsymbol{Q}_{\mathrm{DL},1}^{(t)}, \dots, \boldsymbol{Q}_{\mathrm{DL},N}^{(t)}\}$ . Similarly, the fronthaul capacity required for independent compression should satisfy

<span id="page-6-5"></span>
$$\sum_{n=1}^{N} C_{\text{DL},n}^{(t)} = \sum_{n=1}^{N} I(\mathbf{r}_{\text{DL},n}^{(t)}(i); \tilde{\mathbf{r}}_{\text{DL},n}^{(t)}(i))$$

$$= \log \frac{\left| \mathbf{u}^{(t)} (\mathbf{u}^{(t)})^{\mathsf{H}} + \mathbf{Q}_{\text{DL}}^{(t)} \right|}{\left| \mathbf{Q}_{\text{DL}}^{(t)} \right|} \le C. \quad (14)$$

The received signal at device k under the compression strategy can be expressed as

<span id="page-6-1"></span>
$$\begin{aligned} y_{\mathrm{DL},k}^{(t)}(i) &= \sum_{n=1}^{N} \left(\boldsymbol{h}_{\mathrm{DL},k,n}^{(t)}\right)^{\mathsf{H}} \boldsymbol{r}_{\mathrm{DL},n}^{(t)}(i) + z_{\mathrm{DL},k}^{(t)}(i) \\ &= G_{i}\left(\hat{s}^{(t)}(i)\right) (\boldsymbol{h}_{\mathrm{DL},k}^{(t)})^{\mathsf{H}} \boldsymbol{u}^{(t)} + (\boldsymbol{h}_{\mathrm{DL},k}^{(t)})^{\mathsf{H}} \boldsymbol{q}_{\mathrm{DL}}^{(t)} \\ &+ z_{\mathrm{DL},k}^{(t)}(i), \end{aligned}$$

where

$$\boldsymbol{Q}_{\text{DL}}^{(t)} = \left[ (\boldsymbol{q}_{\text{DL},1}^{(t)})^{\mathsf{H}}, \ldots, (\boldsymbol{q}_{\text{DL},N}^{(t)})^{\mathsf{H}} \right]^{\mathsf{H}}, \ \boldsymbol{h}_{\text{DL},k}^{(t)} = \left[ (\boldsymbol{h}_{\text{DL},k,1}^{(t)})^{\mathsf{H}}, \ldots, (\boldsymbol{h}_{\text{DL},k,N}^{(t)})^{\mathsf{H}} \right]^{\mathsf{H}}.$$

After receiving signals, device k estimates  $G_i\left(\hat{s}^{(t)}(i)\right)$  by scaling the received signals with the receive scalar  $b_{\mathrm{DL},k}^{(t)}$  and taking the real part, i.e.,

$$\hat{G}_{i,k}\left(\hat{s}^{(t)}(i)\right) 
= \Re\left(b_{\mathrm{DL},k}^{(t)}y_{\mathrm{DL},k}^{(t)}(i)\right) 
= \Re\left(b_{\mathrm{DL},k}^{(t)}G_{i}\left(\hat{s}^{(t)}(i)\right)\left(\boldsymbol{h}_{\mathrm{DL},k}^{(t)}\right)^{\mathsf{H}}\boldsymbol{u}^{(t)}\right) + n_{\mathrm{DL},k}^{(t)}(i), \quad (15)$$

where  $\hat{G}_{i,k}\left(\hat{s}^{(t)}(i)\right)$  is the estimate of  $G_i\left(\hat{s}^{(t)}(i)\right)$  at device k, and

$$n_{\text{DL},k}^{(t)}(i) = \Re\left(b_{\text{DL},k}^{(t)}((\boldsymbol{h}_{\text{DL},k}^{(t)})^{\mathsf{H}}\boldsymbol{q}_{\text{DL}}^{(t)} + z_{\text{DL},k}^{(t)}(i))\right) \quad (16)$$

denotes the effective downlink noise for device k distributed as  $n_{\mathrm{DL},k}^{(t)}(i) \sim \mathcal{N}(0,\sigma_{\mathrm{DL},k}^2(t))$ . The variance is given by

<span id="page-6-3"></span>
$$\sigma_{\mathrm{DL},k}^{2}(t) = \frac{|b_{\mathrm{DL},k}^{(t)}|^{2}}{2} \left( \sigma_{z}^{2} + (\boldsymbol{h}_{\mathrm{DL},k}^{(t)})^{\mathsf{H}} \boldsymbol{Q}_{\mathrm{DL}}^{(t)} \boldsymbol{h}_{\mathrm{DL},k}^{(t)} \right). \quad (17)$$

The proposed framework performs centralized signal processing via AirComp by exploiting the cooperation among edge servers, thereby achieving reliable and low-latency model aggregation. Note that we assume all the RRHs are active during FL training, since vertical FL require all the devices to participate in FL training. A key challenge of the Cloud-RAN system is that the quantization errors caused by the limited fronthaul capacity and the aggregation errors caused by AirComp will severely degrade the learning performance of vertical FL. In this paper, our goal is to understand the impact of limited fronthaul capacity and AirComp aggregation error on the learning performance for vertical FL, followed by designing efficient Cloud-RAN system optimization framework to improve the vertical FL performance. To this end, we analyze the convergence of Algorithm 1 under the AirComp based Cloud-RAN, and characterize the convergence with respect to the transmission parameters (e.g., transmit/receive beamforming vectors and quantization covariance matrices) in the next section.

### III. CONVERGENCE ANALYSIS

<span id="page-6-0"></span>In this section, we characterize the convergence behavior of Algorithm 1 under the AirComp based Cloud-RAN with limited fronthaul capacity. Specifically, we first derive the closed-form expression of the vertical FL convergence in terms of optimality gap between objective values and the optimal value  $F(\boldsymbol{w}^*)$ , i.e.,  $\mathbb{E}[F(\boldsymbol{w}^{(T)})] - F(\boldsymbol{w}^*)$ , where the expectation is taken over the communication noise.

## A. Zero-Forcing Precoding

In this subsection, we first design the transmit and receiver scalars of devices to compensate the channel fading based on perfect CSI. To achieve channel inversion, the transmit scalar  $b_{\mathrm{III}..k}^{(t)}$  at device k is designed as

$$b_{\mathrm{UL},k}^{(t)} = \frac{\sqrt{\eta^{(t)}}((\boldsymbol{m}^{(t)})^{\mathsf{H}}\boldsymbol{h}_{\mathrm{UL},k}^{(t)})^{\mathsf{H}}}{|(\boldsymbol{m}^{(t)})^{\mathsf{H}}\boldsymbol{h}_{\mathrm{UL},k}^{(t)}|^{2}}, \quad \forall k \in [K].$$
 (18)

Here, we assume that  $m^{(t)}$  and  $\eta^{(t)}$  are known at devices through the feedback process before transmission. As a result, the received signal at the central server becomes the desired aggregation of the local prediction results with noises. Recall (10), the estimate  $\hat{s}^{(t)}(i)$  at the central server can be written as

<span id="page-6-2"></span>
$$\hat{s}^{(t)}(i) = \sum_{k=1}^{K} g_k(\boldsymbol{w}_k^{(t)}, \boldsymbol{x}_{i,k}) + n_{\mathrm{UL}}^{(t)}(i) = s^{(t)}(i) + n_{\mathrm{UL}}^{(t)}(i),$$
(19)

for all  $i \in [L]$ . Since the uplink noise  $n_{\mathrm{UL}}^{(t)}(i)$  is zero-mean and independent to  $s^{(t)}(i)$ , the estimate  $\hat{s}^{(t)}(i)$  is an unbiased estimation of  $s^{(t)}(i)$ , i.e.,  $\mathbb{E}[\hat{s}^{(t)}(i)] = s^{(t)}(i)$ , with the expectation taken over the uplink noise. Considering the transmit power constraint of each device, i.e.,  $\|b_{\mathrm{UL},k}^{(t)}\|^2 \leq P_{\mathrm{UL}}$ , the power control factor is given by  $\eta^{(t)} = P_{\mathrm{UL}} \min_k \left| (\boldsymbol{m}^{(t)})^{\mathrm{H}} \boldsymbol{h}_{\mathrm{UL},k}^{(t)} \right|^2$ .

Similarly, to perfectly compensate the channel fading of downlink transmission, the receive scalar at device k can be designed as

$$b_{\mathrm{DL},k}^{(t)} = \frac{((\boldsymbol{h}_{\mathrm{DL},k}^{(t)})^{\mathsf{H}} \boldsymbol{u}^{(t)})^{\mathsf{H}}}{\left| (\boldsymbol{h}_{\mathrm{DL},k}^{(t)})^{\mathsf{H}} \boldsymbol{u}^{(t)} \right|^{2}}, \quad \forall k \in [K].$$
 (20)

According to (15), the estimate  $\hat{G}_{i,k}\left(\hat{s}^{(t)}(i)\right)$  at device k can be rewritten as

<span id="page-7-2"></span>
$$\hat{G}_{i,k}\left(\hat{s}^{(t)}(i)\right) = G_i\left(\hat{s}^{(t)}(i)\right) + n_{\mathrm{DL},k}^{(t)}(i)$$

$$= G_i\left(s^{(t)}(i) + n_{\mathrm{UL}}^{(t)}(i)\right) + n_{\mathrm{DL},k}^{(t)}(i). \quad (21)$$

Different from (19), the uplink noise is embedded in function  $G(\cdot)$ . In order to characterize the impact of the effective noise of uplink and downlink, we have the following lemma:

<span id="page-7-0"></span>Lemma 1: Suppose that the amplitude of uplink noise is small enough, the estimate  $\hat{G}_i\left(\hat{s}^{(t)}(i)\right)$  becomes an unbiased estimation of  $G_i\left(s^{(t)}(i)\right)$ .

To verify Lemma 1, we can write the estimate  $\hat{G}_{i,k}\left(\hat{s}^{(t)}(i)\right)$  as its first-order Taylor expansion as follows

<span id="page-7-1"></span>
$$\hat{G}_{i,k}(\hat{s}^{(t)}(i)) = G_i(s^{(t)}(i) + n_{\mathrm{UL}}^{(t)}) + n_{\mathrm{DL},k}^{(t)}(i) 
= G_i(s^{(t)}(i)) + G_i'(s^{(t)}(i))n_{\mathrm{UL}}^{(t)}(i) 
+ \mathcal{O}(|n_{\mathrm{UL}}^{(t)}(i)|^2) + n_{\mathrm{DL},k}^{(t)}(i) 
\approx G_i(s^{(t)}(i)) + G_i'(s^{(t)}(i))n_{\mathrm{UL}}^{(t)}(i) + n_{\mathrm{DL},k}^{(t)}(i),$$
(22)

<span id="page-7-7"></span>where  $G_i'(\cdot)$  is the first derivative of  $G_i(\cdot)$ . Assuming that the amplitude of uplink noise is small, the term  $\mathcal{O}(|n_{\mathrm{UL}}^{(t)}(i)|^2)$  is neglected, which implies the last approximated equality in (22) [45]. Actually, we can perform beamforming design and capacity allocation to control the amplitude of the effective noise of uplink and downlink, which is introduced in Section IV.

Remark 1: Through zero-forcing precoding, we can perfectly compensate the channel fading and thus minimize the impact caused by the channel distortion, which gives the closed-form solution with respect to  $\eta^{(t)}$ . As a sequence, the communication noises  $n_{\mathrm{UL}}^{(t)}(i)$  and  $n_{\mathrm{DL}}^{'(t)}(i)$  can equivalently represent the impact caused by uplink and downlink communications, i.e., (19) and (21), respectively. As discussed later in this section, the communication noises significantly degrade the convergence performance of the vertical FL algorithm in terms of the optimality gap over the AirComp-based Cloud-RAN. It is noteworthy that a similar type of aggregation noise was also considered in [46]. However, they addressed the aggregation noise from the algorithmic perspective, while this paper aims to reduce the noise impact through the design of the communication system. In addition, the effect of aggregation noise on vertical FL algorithms is different from that on horizontal FL algorithms.

### B. Convergence Result

In the following, we first provide the convergence analysis of Algorithm 1 under AirComp based Cloud-RAN with a

non-zero optimality gap from the optimal solution. We first present some assumptions which are widely adopted in FL literature [47] and [48].

<span id="page-7-9"></span><span id="page-7-3"></span>Assumption 1 ( $\alpha$ -Strongly Convexity): The function  $F(\cdot)$  is assumed to be  $\alpha$ -strongly convex on  $\mathbb{R}^d$  with constant  $\alpha$ , namely, satisfying the following inequality

<span id="page-7-10"></span><span id="page-7-6"></span>
$$F(\boldsymbol{y}) \ge F(\boldsymbol{x}) + \nabla F(\boldsymbol{x})^{\mathsf{T}} (\boldsymbol{y} - \boldsymbol{x}) + \frac{\alpha}{2} \|\boldsymbol{y} - \boldsymbol{x}\|^2, \quad (23)$$

for all  $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^d$ .

<span id="page-7-4"></span>Assumption 2 ( $\beta$ -Smoothness): The function  $F(\cdot)$  is assumed to be  $\beta$ -smooth on  $\mathbb{R}^d$  with constant  $\beta$ , namely, satisfying the following inequality

$$F(\boldsymbol{y}) \le F(\boldsymbol{x}) + \nabla F(\boldsymbol{x})^{\mathsf{T}} (\boldsymbol{y} - \boldsymbol{x}) + \frac{\beta}{2} \|\boldsymbol{y} - \boldsymbol{x}\|^2,$$
 (24)

for all  $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^d$ .

Based on Assumptions 1-2, we analyze the performance of Algorithm 1 under the AirComp based Cloud-RAN communication system proposed in the previous section. Specifically, the optimality gap from the optimal objective value  $F(\boldsymbol{w}^*)$  with respect to the system parameters  $\{\boldsymbol{m}^{(t)}, \boldsymbol{u}^{(t)}, \boldsymbol{Q}_{\mathrm{UL}}^{(t)}, \boldsymbol{Q}_{\mathrm{DL}}^{(t)}\}$  is established. The details are summarized in the following theorem.

<span id="page-7-5"></span>Theorem 1 (Convergence of Algorithm 1 Under AirComp Based Cloud-RAN): Consider Assumptions 1-2 with constant learning rate  $\mu^{(t)} = 1/\beta$ , and also assuming that estimate  $\hat{G}_i\left(\hat{s}^{(t)}(i)\right)$  is an unbiased estimation of  $G_i\left(s^{(t)}(i)\right)$  according to Lemma 1. The expected optimality gap for Algorithm 1 under AirComp based Cloud-RAN is upper bounded as

$$\mathbb{E}\left[F(\boldsymbol{w}^{(T)}) - F(\boldsymbol{w}^*)\right]$$

$$\leq \rho^T \mathbb{E}\left[F(\boldsymbol{w}^{(0)}) - F(\boldsymbol{w}^*)\right] + \frac{3}{2L^2\beta}B(T), \quad (25)$$

where  $\rho=1-\frac{\alpha}{\beta}$  is the contraction rate and the optimality gap B(T) in the T-th communication round is given by

$$B(T) = \sum_{t=0}^{T-1} \rho^{T-t-1} \sum_{k=1}^{K} (\Phi_{1,k} \sigma_{\mathrm{UL}}^{2}(t) + \Phi_{2,k} \sigma_{\mathrm{DL},k}^{2}(t)), \quad (26)$$

where

$$\Phi_{1,k}(t) = \sum_{i=1}^{L} G_i' \left( s^{(t)}(i) \right)^2 \| \boldsymbol{x}_{i,k} \|^2, \Phi_{2,k}(t) = \sum_{i=1}^{L} \| \boldsymbol{x}_{i,k} \|^2.$$
(27a)

<span id="page-7-11"></span>

*Proof:* Please refer to Appendix.

<span id="page-7-8"></span>Remark 2: Comparing Theorem 1 to the convergence results of the vanilla GD algorithm [49] with error-free communication, we observe that Algorithm 1 under Air-Comp based Cloud-RAN achieves the same convergence rate, but with a non-zero optimality gap B(T) depending on the communication noise variances  $\{\sigma_{\mathrm{UL}}^2(t)\}_{t=0}^T$  and  $\{\sigma_{\mathrm{DL},t}^2\}_{t=0}^T$ . Hence, the non-zero gap B(T) reveals the impact of the communication noises on the convergence performance. In particular, a smaller B(T) leads to a smaller gap between  $F(\mathbf{w}^{(T)})$  and  $F(\mathbf{w}^*)$ , which motivates us to treat the optimality gap B(T) as the metric of vertical FL performance over the Cloud-RAN. Based on (11) and (17), we can control the noise variances by jointly designing the Cloud-RAN system parameters  $\{\mathbf{m}^{(t)}, \mathbf{u}^{(t)}, \mathbf{Q}_{\mathrm{DL}}^{(t)}\}$ .

#### IV. SYSTEM OPTIMIZATION

<span id="page-8-0"></span>This section presents the system optimization for vertical FL over the AirComp-based Cloud-RAN. We first formulate the resource allocation problem by minimizing the optimality gap under the system constraints including the limited fronthaul capacity and the transmit power constraints. Then, we decompose the resulting optimization problem into two sub-problems, i.e., uplink and downlink optimization problems which are solved by the successive convex approximation (SCA) and alternate convex search (ACS) approaches.

### A. Problem Formulation

In this section, we optimize the Cloud-RAN assisted vertical FL system by minimizing the global loss F(w) based on the convergence results in the previous section. Specifically, we minimize the optimality gap in terms of B(T) in Theorem 1 while satisfying the communication constraints (e.g., (7), (9), (13), (14)). Then, the corresponding optimization problem can be formulated as

<span id="page-8-1"></span>
$$\min_{\Omega} \sum_{t=0}^{T-1} \rho^{T-t-1} \sum_{k=1}^{K} (\Phi_{1,k} \sigma_{\mathrm{UL}}^{2}(t) + \Phi_{2,k} \sigma_{\mathrm{DL},k}^{2}(t))$$
s.t. 
$$\sum_{n=1}^{N} C_{\mathrm{UL},n}^{(t)} \leq C, \quad \sum_{n=1}^{N} C_{\mathrm{DL},n}^{(t)} \leq C, \quad \forall t \in [T]$$

$$\mathbf{Q}_{\mathrm{UL}}^{(t)}(i,i) > 0, \quad \mathbf{Q}_{\mathrm{UL}}^{(t)}(i,j) = 0, \quad \forall i \neq j, \quad \forall t \in [T]$$

$$\mathbf{Q}_{\mathrm{DL}}^{(t)}(i,i) > 0, \quad \mathbf{Q}_{\mathrm{DL}}^{(t)}(i,j) = 0, \quad \forall i \neq j, \quad \forall t \in [T]$$

$$\|\mathbf{u}^{(t)}\|^{2} + \operatorname{Tr}(\mathbf{Q}_{\mathrm{DL}}^{(t)}) \leq P_{\mathrm{DL}}, \quad \forall t \in [T], \quad (28)$$

where  $\Omega = \{\boldsymbol{m}^{(t)}, \boldsymbol{u}^{(t)}, \boldsymbol{Q}_{\mathrm{UL}}^{(t)}, \boldsymbol{Q}_{\mathrm{DL}}^{(t)}\}.$ 

Since the communication constraints are independent during T rounds, we can decompose the above problem into T independent sub-problems. Additionally, note that both the objective function and the constraints can be divided into uplink and downlink transmissions, which are independent of each other. As a consequence, we solve problem (28) by solving the following two sub-problems in parallel at each communication round,

<span id="page-8-2"></span>
$$\min_{\boldsymbol{m}^{(t)}, \boldsymbol{Q}_{\text{UL}}^{(t)}} \sum_{k=1}^{K} \Phi_{1,k}(t) \sigma_{\text{UL}}^{2}(t)$$
s.t. 
$$\sum_{n=1}^{N} C_{\text{UL},n}^{(t)} \leq C,$$

$$\boldsymbol{Q}_{\text{UL}}^{(t)}(i,i) > 0, \quad \boldsymbol{Q}_{\text{UL}}^{(t)}(i,j) = 0, \quad \forall i \neq j, \quad (29)$$

and

<span id="page-8-7"></span>
$$\min_{\boldsymbol{u}^{(t)}, \boldsymbol{Q}_{\text{DL}}^{(t)}} \sum_{k=1}^{K} \Phi_{2,k}(t) \sigma_{\text{DL},k}^{2}(t)$$
s.t. 
$$\sum_{n=1}^{N} C_{\text{DL},n}^{(t)} \leq C,$$

$$\boldsymbol{Q}_{\text{DL}}^{(t)}(i,i) > 0, \quad \boldsymbol{Q}_{\text{DL}}^{(t)}(i,j) = 0, \quad \forall i \neq j,$$

$$\|\boldsymbol{u}^{(t)}\|^{2} + \text{Tr}(\boldsymbol{Q}_{\text{DL}}^{(t)}) \leq P_{\text{DL}}.$$
(30)

#### B. Optimization Framework

In the following, we specify the optimization framework for solving the uplink and downlink optimization problems, respectively. To simplify the notations, we omit the time index of the optimized variables in the following as we focus on the system optimization problem at one communication round.

1) Uplink Optimization: By substituting (9) and (11) into problem (29), we then obtain the following optimization problem in the uplink transmission:

<span id="page-8-3"></span>
$$\begin{split} \min_{\boldsymbol{m},\boldsymbol{Q}_{\mathrm{UL}}} & \frac{1}{2\eta} \boldsymbol{m}^{\mathsf{H}} \left( \sigma_{z}^{2} \boldsymbol{I} + \boldsymbol{Q}_{\mathrm{UL}} \right) \boldsymbol{m} \\ \text{s.t. } \log \frac{\left| P_{\mathrm{UL}} \sum_{k=1}^{K} \boldsymbol{h}_{\mathrm{UL},k} (\boldsymbol{h}_{\mathrm{UL},k})^{\mathsf{H}} + \sigma_{z}^{2} \boldsymbol{I} + \boldsymbol{Q}_{\mathrm{UL}} \right|}{\left| \boldsymbol{Q}_{\mathrm{UL}} \right|} & \leq C, \\ & \boldsymbol{Q}_{\mathrm{UL}}(i,i) > 0, \quad \boldsymbol{Q}_{\mathrm{UL}}(i,j) = 0, \quad \forall i \neq j, \end{split} \tag{31}$$

where  $\eta = P_{\text{UL}} \min_k |(\boldsymbol{m})^{\mathsf{H}} \boldsymbol{h}_{\text{UL},k}|^2$ .

We propose to adopt the alternating optimization technique to solve the uplink optimization problem (31). Specifically, we first fix the covariance matrix  $Q_{\rm UL}$  in problem (31) and optimize the receive beamforming vector m by solving the following min-max problem:

$$\min_{\boldsymbol{m}} \max_{k} \frac{\boldsymbol{m}^{\mathsf{H}} \tilde{\boldsymbol{Q}} \boldsymbol{m}}{|\boldsymbol{m}^{\mathsf{H}} \boldsymbol{h}_{\mathrm{ul,k}}|^{2}}, \quad \text{s.t. } \tilde{\boldsymbol{Q}} = \sigma_{z}^{2} \boldsymbol{I} + \boldsymbol{Q}_{\mathrm{UL}}, \quad (32)$$

which is equivalent to

<span id="page-8-4"></span>
$$\min_{\boldsymbol{m}} \max_{k} - |\boldsymbol{m}^{\mathsf{H}} \boldsymbol{h}_{\mathrm{ul,k}}|^{2}, \quad \text{s.t. } \boldsymbol{m}^{\mathsf{H}} \tilde{\boldsymbol{Q}} \boldsymbol{m} = 1.$$
 (33)

Problem (33) is a quadratically constrained quadratic programming (QCQP) problem with a non-convex constraint. To tackle the non-convex constraint in problem (33), we relax the equality constraint to an inequality constraint, i.e.,  $m^H \tilde{Q} m \leq 1$ , which yields the following relaxed problem:

<span id="page-8-5"></span>
$$\min_{\boldsymbol{m}} \max_{k} - |\boldsymbol{m}^{\mathsf{H}} \boldsymbol{h}_{\mathrm{ul,k}}|^{2}, \quad \text{s.t. } \boldsymbol{m}^{\mathsf{H}} \tilde{\boldsymbol{Q}} \boldsymbol{m} \leq 1.$$
 (34)

We adopt the successive convex approximation (SCA) technique to solve problem (34) with good performance and low computational complexity.

To develop the SCA approach, we convert problem (34) from the complex domain to the real domain with the following variables:

$$\tilde{\boldsymbol{m}} = \begin{bmatrix} \Re(\boldsymbol{m})^\mathsf{T} & \Im(\boldsymbol{m})^\mathsf{T} \end{bmatrix}^\mathsf{T},$$
 (35a)

$$\tilde{\boldsymbol{H}}_{k} = -\begin{bmatrix} \Re(\boldsymbol{h}) & \Im(\boldsymbol{h}) \end{bmatrix}, \qquad (33a)$$

$$\tilde{\boldsymbol{H}}_{k} = -\begin{bmatrix} \Re(\boldsymbol{h}_{\mathrm{UL},k}\boldsymbol{h}_{\mathrm{UL},k}^{\mathsf{H}}) & -\Im(\boldsymbol{h}_{\mathrm{UL},k}\boldsymbol{h}_{\mathrm{UL},k}^{\mathsf{H}}) \\ \Im(\boldsymbol{h}_{\mathrm{UL},k}\boldsymbol{h}_{\mathrm{UL},k}^{\mathsf{H}}) & \Re(\boldsymbol{h}_{\mathrm{UL},k}\boldsymbol{h}_{\mathrm{UL},k}^{\mathsf{H}}) \end{bmatrix}, \quad \forall k \in [K],$$
(35b)

 $\tilde{\mathbf{Q}}' = \begin{bmatrix} \Re(\tilde{\mathbf{Q}}) & -\Im(\tilde{\mathbf{Q}}) \\ \Im(\tilde{\mathbf{Q}}) & \Re(\tilde{\mathbf{Q}}) \end{bmatrix}. \tag{35c}$ 

Then, problem (34) can be reformulated as follows:

<span id="page-8-6"></span>
$$\min_{\tilde{\boldsymbol{m}}} \max_{k} \ \tilde{\boldsymbol{m}}^{\mathsf{T}} \tilde{\boldsymbol{H}}_{k} \tilde{\boldsymbol{m}}, \quad \text{s.t. } \tilde{\boldsymbol{m}}^{\mathsf{T}} \tilde{\boldsymbol{Q}}' \tilde{\boldsymbol{m}} \leq 1. \tag{36}$$

For simplicity, we define  $u_k(\tilde{\boldsymbol{m}}) = \tilde{\boldsymbol{m}}^\mathsf{T} \tilde{\boldsymbol{H}}_k \tilde{\boldsymbol{m}}$ . Since  $u_k(\tilde{\boldsymbol{m}})$  is a concave function, we can upper bound  $u_k(\tilde{\boldsymbol{m}})$  by the tangent of the l-th point  $\boldsymbol{m}_{(l)}$  as follows:

$$u_k(\tilde{\boldsymbol{m}}) \leq \nabla u_k(\tilde{\boldsymbol{m}}_{(l)})^{\mathsf{T}}(\tilde{\boldsymbol{m}} - \tilde{\boldsymbol{m}}_{(l)}) + u_k(\tilde{\boldsymbol{m}}_{(l)})$$

## **Algorithm 2** Proposed Algorithm for Uplink Optimization (31)

<span id="page-9-2"></span> $\begin{array}{c|c} \textbf{Input} : \text{Initial points } \tilde{\boldsymbol{m}}_{(0)}^{(0)}, \boldsymbol{Q}_{\text{UL}}^{(0)} \text{ and threshold } \epsilon; \\ \textbf{1 Set } i = 0; \\ \textbf{2 repeat} \\ \textbf{3} & \text{Set } l = 0; \\ \textbf{4} & \text{repeat} \\ \textbf{5} & \text{Update } \tilde{\boldsymbol{m}}_{(l+1)}^{(i)} \text{ by solving problem (37);} \\ \textbf{6} & l \leftarrow l+1; \\ \textbf{7} & \textbf{until } \left\| \tilde{\boldsymbol{m}}_{(l+1)}^{(i)} - \tilde{\boldsymbol{m}}_{(l)}^{(i)} \right\| < \epsilon; \\ \textbf{8} & \text{Set } \tilde{\boldsymbol{m}}_{(0)}^{(i+1)} \leftarrow \tilde{\boldsymbol{m}}_{(l)}^{(i)}; \\ \textbf{9} & \text{Update } \boldsymbol{Q}_{\text{UL}}^{(i+1)} \text{ by solving problem (38);} \\ \textbf{10} & \text{Set } i \leftarrow i+1; \\ \textbf{11 until } \left\| \tilde{\boldsymbol{m}}_{(0)}^{(i+1)} - \tilde{\boldsymbol{m}}_{(0)}^{(i)} \right\| + \left\| \boldsymbol{Q}_{\text{UL}}^{(i+1)} - \boldsymbol{Q}_{\text{UL}}^{(i)} \right\| < \epsilon; \\ \end{array}$ 

$$= \left(2\tilde{\boldsymbol{H}}_k \tilde{\boldsymbol{m}}_{(l)}\right)^\mathsf{T} \tilde{\boldsymbol{m}} - (\tilde{\boldsymbol{m}}_{(l)})^\mathsf{T} \tilde{\boldsymbol{H}}_k \tilde{\boldsymbol{m}}_{(l)}.$$

The sub-problem for each SCA iteration can be reformulated as follows:

<span id="page-9-0"></span>
$$\min_{\tilde{\boldsymbol{m}}} \max_{k} \left( 2\tilde{\boldsymbol{H}}_{k} \tilde{\boldsymbol{m}}_{(l)} \right)^{\mathsf{T}} \tilde{\boldsymbol{m}} - (\tilde{\boldsymbol{m}}_{(l)})^{\mathsf{T}} \tilde{\boldsymbol{H}}_{k} \tilde{\boldsymbol{m}}_{(l)} 
\text{s.t. } \tilde{\boldsymbol{m}}^{\mathsf{T}} \tilde{\boldsymbol{Q}}' \tilde{\boldsymbol{m}} \leq 1.$$
(37)

Starting from an initial point  $\tilde{m}_{(0)}$ , a sequence of solutions  $\{\tilde{m}_{(l)}\}$  is generated by solving a series of the above subproblems.

When fixing the receive beamforming vector m, problem (31) is reduced to the following problem:

<span id="page-9-1"></span>
$$\begin{aligned} & \min_{\boldsymbol{Q}_{\text{UL}}} \ \boldsymbol{m}^{\text{H}} \left( \sigma_{z}^{2} \boldsymbol{I} + \boldsymbol{Q}_{\text{UL}} \right) \boldsymbol{m} \\ & \text{s.t. } \log \frac{\left| P_{\text{UL}} \sum_{k=1}^{K} \boldsymbol{h}_{\text{UL},k} (\boldsymbol{h}_{\text{UL},k})^{\text{H}} + \sigma_{z}^{2} \boldsymbol{I} + \boldsymbol{Q}_{\text{UL}} \right|}{\left| \boldsymbol{Q}_{\text{UL}} \right|} \leq C, \\ & \boldsymbol{Q}_{\text{UL}}(i,i) > 0, \quad \boldsymbol{Q}_{\text{UL}}(i,j) = 0, \quad \forall i \neq j. \end{aligned} \tag{38}$$

It is easy to verify that problem (38) is convex with respect to  $Q_{\rm UL}$ , which can be solved efficiently with polynomial complexity by using CVX, a package for specifying and solving convex programs [50].

<span id="page-9-8"></span>The proposed algorithm for uplink optimization is summarized in Algorithm 2. The convergence results are summarized as follows:

- In the inner loop (Steps 4-7), the values of objective function in problem (36) achieved by sequence  $\{\tilde{\boldsymbol{m}}_{(l)}^{(i)}\}_{l=0}^{\infty}$  converge monotonically.
- In the outer loop (Steps 2-11), the values of objective function in problem (33) achieved by sequence  $\{\tilde{\boldsymbol{m}}_{(0)}^{(i)}, \boldsymbol{Q}_{(1)}^{(i)}\}_{i=0}^{\infty}$  converge monotonically.

Problem (37) can be equivalently formulated as a convex QCQP problem and then be solved by using the interior-point method, and the computational complexity is  $\mathcal{O}((MN+K)^{3.5})$ . Similarly, the complexity of solving problem (38) is  $\mathcal{O}((MN)^{3.5})$ .

2) *Downlink Optimization:* By substituting (17) into problem (30), we solve the following problem:

<span id="page-9-3"></span>
$$\begin{split} & \min_{\boldsymbol{u}, \boldsymbol{Q}_{\mathrm{DL}}} \sum_{k=1}^{K} \frac{\boldsymbol{\Phi}_{2,k}}{|(\boldsymbol{h}_{\mathrm{DL},k}^{(t)})^{\mathsf{H}} \boldsymbol{u}|^{2}} \left( \sigma_{z}^{2} + (\boldsymbol{h}_{\mathrm{DL},k})^{\mathsf{H}} \boldsymbol{Q}_{\mathrm{DL}} \boldsymbol{h}_{\mathrm{DL},k} \right) \\ & \text{s.t. } \log \frac{\left| \boldsymbol{u} \boldsymbol{u}^{\mathsf{H}} + \boldsymbol{Q}_{\mathrm{DL}} \right|}{|\boldsymbol{Q}_{\mathrm{DL}}|} \leq C, \\ & \boldsymbol{Q}_{\mathrm{DL}}(i,i) > 0, \quad \boldsymbol{Q}_{\mathrm{DL}}(i,j) = 0, \quad \forall i \neq j, \\ & \|\boldsymbol{u}\|^{2} + \mathrm{Tr}(\boldsymbol{Q}_{\mathrm{DL}}) \leq P_{\mathrm{DL}}. \end{split} \tag{39}$$

Although the objective function in problem (39) is convex with respect to each optimization variable when other optimization variables are fixed, the capacity constraint is non-convex with respect to  $\boldsymbol{u}^{(t)}$ . Hence, we approximate problem (39) to a convex optimization by linearizing the limited fronthaul capacity constraint. By solving the approximated optimization problem, we successively approximate the optimal solution of the original problem.

Before reformulating the downlink optimization problem, we first present the following lemma for convex approximation, which is also adopted in [51].

Lemma 2: For positive definite Hermitian matrices  $\Omega, \Sigma \in \mathbb{C}^{N \times N}$ , we have

<span id="page-9-9"></span>
$$\log |\Omega| \le \log |\Sigma| + \operatorname{Tr}(\Sigma^{-1}\Omega) - N, \tag{40}$$

with equality if and only if  $\Omega = \Sigma$ .

By applying Lemma 1 to the capacity constraint in problem (39) and setting  $\Omega = uu^{\rm H} + Q_{\rm DL}$ , we can approximate the capacity constraint in problem (39) with the following convex constraint:

<span id="page-9-4"></span>
$$\log |\mathbf{\Sigma}| + \operatorname{Tr} \left(\mathbf{\Sigma}^{-1} \left( u u^{\mathsf{H}} + \mathbf{Q}_{\mathrm{DL}} \right) \right) - \log |\mathbf{Q}_{\mathrm{DL}}| \le C + MN. \tag{41}$$

Note that the capacity constraint in problem (39) is always feasible when the convex constraint (41) is feasible. The two constraints are equivalent when

<span id="page-9-6"></span>
$$\Sigma^* = uu^{\mathsf{H}} + Q_{\mathsf{DL}}.\tag{42}$$

By using the convex constraint (41) to replace the capacity constraint in (39), we reformulate the downlink optimization problem to the following equivalent problem:

<span id="page-9-5"></span>
$$\min_{\boldsymbol{u}, \boldsymbol{Q}_{\mathrm{DL}}, \boldsymbol{\Sigma}} \operatorname{Tr} \left( \boldsymbol{Q}_{\mathrm{DL}} \sum_{k=1}^{K} \frac{\Phi_{2,k}}{\boldsymbol{u}^{\mathsf{H}} \boldsymbol{H}_{\mathrm{DL},k} \boldsymbol{u}} \boldsymbol{H}_{\mathrm{DL},k} \right) 
\text{s.t. } \log |\boldsymbol{\Sigma}| + \operatorname{Tr} \left( \boldsymbol{\Sigma}^{-1} \boldsymbol{\Omega} \right) - \log |\boldsymbol{Q}_{\mathrm{DL}}| \leq C + MN, 
\boldsymbol{Q}_{\mathrm{DL}}(i, i) > 0, \quad \boldsymbol{Q}_{\mathrm{DL}}(i, j) = 0, \quad \forall i \neq j, 
\|\boldsymbol{u}\|^{2} + \operatorname{Tr}(\boldsymbol{Q}_{\mathrm{DL}}) \leq P_{\mathrm{DL}},$$
(43)

where  $\bm{\Omega} = \bm{u}\bm{u}^{\sf H} + \bm{Q}_{\rm DL}$  and  $\bm{H}_{\rm DL,k} = \bm{h}_{\rm DL,k}\bm{h}_{\rm DL,k}^{\sf H}$ .

In this paper, we propose to alternatively optimize problem (43). When  $\{u, Q_{\rm DL}\}$  are fixed, the optimal value of  $\Sigma$  is given by (42). When  $\Sigma$  is fixed, the solutions of  $\{u, Q_{\rm DL}\}$  are given by solving the following problem:

<span id="page-9-7"></span>
$$\min_{\boldsymbol{u},\boldsymbol{Q}_{\mathrm{DL}}} \ \mathrm{Tr}\left(\boldsymbol{Q}_{\mathrm{DL}} \sum_{k=1}^{K} \frac{\Phi_{2,k}}{\boldsymbol{u}^{\mathsf{H}} \boldsymbol{H}_{\mathrm{DL},k} \boldsymbol{u}} \boldsymbol{H}_{\mathrm{DL},k}\right)$$

## **Algorithm 3** Proposed Algorithm for Downlink Optimization (39)

<span id="page-10-3"></span>Input: Initial points  $\Sigma^{(0)}$  and threshold  $\epsilon$ ;

1 Set i=0;

2 repeat

3 | Update  $Q_{\mathrm{DL}}^{(i+1)}$  by solving problem (45);

4 | Update  $u^{(i+1)}$  by solving problem (46);

5 | Update  $\Sigma^{(i+1)}$  by using (42);

6 | Set  $i \leftarrow i+1$ ;

7 until  $\|u^{(i+1)} - u^{(i)}\| + \|Q_{\mathrm{DL}}^{(i+1)} - Q_{\mathrm{DL}}^{(i)}\| + \|\Sigma^{(i+1)} - \Sigma^{(i)}\| < \epsilon$ ;

s.t. 
$$\operatorname{Tr}\left(\mathbf{\Sigma}^{-1}\mathbf{\Omega}\right) - \log |\mathbf{Q}_{\mathrm{DL}}| \le C + MN - \log |\mathbf{\Sigma}|,$$

$$\mathbf{Q}_{\mathrm{DL}}(i, i) > 0, \quad \mathbf{Q}_{\mathrm{DL}}(i, j) = 0, \quad \forall i \ne j,$$

$$\|\mathbf{u}\|^{2} + \operatorname{Tr}(\mathbf{Q}_{\mathrm{DL}}) \le P_{\mathrm{DL}}.$$
(44)

The objective function in problem (44) is a bi-convex problem for  $\{u, Q_{\rm DL}\}$ , e.g., by fixing u the function is convex for  $Q_{\rm DL}$ , and by fixing  $Q_{\rm DL}$  the function is convex for u. By exploiting the bi-convex structure of the problem, we adopt the ACS approach to solve problem (44). Specifically, problem (44) is transformed into the following two sub-problems:

<span id="page-10-1"></span>
$$\min_{\boldsymbol{Q}_{\mathrm{DL}}} \operatorname{Tr} \left( \boldsymbol{Q}_{\mathrm{DL}} \sum_{k=1}^{K} \frac{\Phi_{2,k}}{\boldsymbol{u}^{\mathsf{H}} \boldsymbol{H}_{\mathrm{DL},k} \boldsymbol{u}} \boldsymbol{H}_{\mathrm{DL},k} \right) 
s.t. \operatorname{Tr} \left( \boldsymbol{\Sigma}^{-1} \boldsymbol{\Omega} \right) - \log |\boldsymbol{Q}_{\mathrm{DL}}| \leq C + MN - \log |\boldsymbol{\Sigma}|, 
\boldsymbol{Q}_{\mathrm{DL}}(i,i) > 0, \quad \boldsymbol{Q}_{\mathrm{DL}}(i,j) = 0, \quad \forall i \neq j, 
\|\boldsymbol{u}\|^{2} + \operatorname{Tr}(\boldsymbol{Q}_{\mathrm{DL}}) \leq P_{\mathrm{DL}},$$
(45)

and

<span id="page-10-2"></span>
$$\min_{\boldsymbol{u}} \operatorname{Tr} \left( \boldsymbol{Q}_{\mathrm{DL}} \sum_{k=1}^{K} \frac{\Phi_{2,k}}{\boldsymbol{u}^{\mathsf{H}} \boldsymbol{H}_{\mathrm{DL},k} \boldsymbol{u}} \boldsymbol{H}_{\mathrm{DL},k} \right) \\
\text{s.t. } \|\boldsymbol{u}\|^{2} + \operatorname{Tr}(\boldsymbol{Q}_{\mathrm{DL}}) \leq P_{\mathrm{DL}}. \tag{46}$$

The overall algorithm for downlink optimization is summarized in Algorithm 3. The sub-problems (45) and (46) are convex and can be solved by using the interior-point method within  $\mathcal{O}((MN)^{3.5})$  iterations. The convergence of ACS has already been intensively studied in [52].

### <span id="page-10-5"></span>V. NUMERICAL RESULTS

<span id="page-10-0"></span>In this section, we conduct extensive numerical experiments to evaluate the performance of the proposed system optimization algorithm for the AirComp based Cloud-RAN for wireless vertical FL.

### A. Simulation Settings

1) Vertical FL Setting: We consider a vertical FL setting where K=49 devices cooperatively train a regularized logistic regression model. We simulate the image classification task on Fashion-MNIST dataset. The local training data are independent and identically distributed (i.i.d.) drawn from L=50,000 images, and the test dataset contains 10,000 different

<span id="page-10-4"></span>![](_page_10_Figure_14.jpeg)

Fig. 4. Optimality gap versus communication round for different downlink power constraints.

images. For each training image of 784 features, each device is assigned with 784/49=16 non-overlapped features. The learning rate  $\mu^{(t)}$  is set to 0.01. We use the optimality gap to characterize the convergence of the proposed algorithm. Furthermore, the learning performance of wireless vertical FL is evaluated by the training loss for training and the test accuracy for testing.

<span id="page-10-6"></span>2) Communication Setting: We consider a Cloud-RAN assisted vertical FL system with N edge servers and K =49 devices randomly located in a circle area of radius 500 m. The edge servers are randomly distributed in the circular area. Each edge server is equipped with M antennas, and each device is equipped with single antenna. The channel coefficients are given by the small-scale fading coefficients multiplied by the square root of the path loss, i.e., 30.6 + $36.7 \log_{10}(d)$  dB [53], where d (in meter) is the distance between the device and the edge server. The small-scale fading coefficients follow the standard i.i.d. Gaussian distribution. The transmit power constraint for all device is set to  $P_{\rm UL} =$ 23 dBm, the power spectral density of the background noise at each edge server is assumed to be -169 dBm/Hz [42], and the noise figure is 7 dB. All numerical results are averaged over 50 trials.

### B. Convergence of the Proposed Algorithm

In this subsection, we examine the convergence performance of the proposed algorithm for image classification task. We consider Algorithm 1 as **Performance Upper Bound**, where the channels are noiseless (i.e.,  $\sigma_z^2 = 0$ ) and the fronthaul capacity is infinite (i.e.,  $C = +\infty$ ), which characterizes the best possible learning performance for vertical FL.

In Fig. 4, we plot the optimality gap in 1000 communication rounds for different downlink power constraints with the capacity constraint C=200 Mbps. The number of edge servers and the number of antennas at each edge server are set to N=8 and M=10, respectively. It is observed that the proposed algorithms under two considered downlink power constraints are both able to linearly converge. This implies that the proposed algorithm can effectively compensate for the distortion of channels and noises, thereby speeding up the convergence and reducing optimality gap. Furthermore, the case with higher downlink power constraint achieves better performance gains (smaller optimality gap), since the signal-to-noise ratio (SNR) in this case is higher.

### C. Impact of Key System Parameters

In this subsection, we show the performance gain of joint optimization for wireless and fronthaul resource allocation, and investigate the impact of various key system parameters. For clarity, we refer the proposed algorithm to jointly optimize beamforming vectors and covariance matrices as **Joint Optimization**. We also consider different schemes for designing beamforming vectors and covariance matrices as baselines:

- Baseline 1: Uniform quantization with uniform beamforming. The transmit beamforming  $u^{(t)}$  and the receive beamforming  $m^{(t)}$  are uniformly designed, i.e.,  $u^{(t)} = \kappa \mathbf{1}$  and  $m^{(t)} = \sqrt{1/MN} \mathbf{1}$ , where the scalar  $\kappa$  is chosen to satisfy the maximum power constraint (13). The central server performs uniform quantization noise levels across the antennas for all edge servers, i.e., setting  $Q_{\mathrm{UL}}^{(t)} = \lambda_{\mathrm{UL}}\mathbf{I}$  and  $Q_{\mathrm{DL}}^{(t)} = \lambda_{\mathrm{DL}}\mathbf{I}$ , where the scalars  $\lambda_{\mathrm{UL}}$  and  $\lambda_{\mathrm{DL}}$  are chosen to satisfy the fronthaul capacity constraints (9) and (14).
- Baseline 2: Uniform quantization with optimized beamforming. This baseline is similar to Baseline 1 except that the receive beamforming vector  $\{\boldsymbol{n}^{(t)}\}$  and the transmit beamforming vector  $\{\boldsymbol{u}^{(t)}\}$  are optimized by Algorithms 2 and 3 with the uniformly designed covariance matrices  $\boldsymbol{Q}_{\mathrm{UL}}^{(t)} = \lambda_{\mathrm{UL}}\mathbf{I}$  and  $\boldsymbol{Q}_{\mathrm{DL}}^{(t)} = \lambda_{\mathrm{DL}}\mathbf{I}$ .
- Baseline 3: Optimized quantization with uniform beamforming. This baseline is similar to Baseline 1 except that the covariance matrices  $\{Q_{\mathrm{UL}}^{(t)},Q_{\mathrm{DL}}^{(t)}\}$  are optimized by Algorithms 2 and 3 with the uniformly designed beamforming vectors  $\boldsymbol{u}^{(t)} = \kappa \boldsymbol{1}$  and  $\boldsymbol{m}^{(t)} = \sqrt{1/MN} \boldsymbol{1}$ .

In order to record the performance of each scheme, each numerical experiment runs 500 communication rounds, and the performance of the last round is recorded. Unless specified otherwise, the number of edge servers is set to 8, i.e., N=8, the number of antennas at each edge server is set to 2, i.e., M=2, and the downlink power constraint is set to  $P_{\rm DL}=100~{\rm dBm}$ .

Fig. 5 shows the training loss and test accuracy achieved by different schemes versus the fronthaul capacity C. It is observed that the proposed joint optimization for wireless and fronthaul resource allocation achieves higher test accuracy and less training loss over Baselines 1-3, and approaches the performance upper bound when the fronthaul capacity is greater than or equal to 180 Mbps. Furthermore, Fig. 5 shows that in the region of small the fronthaul capacity (C < 200 Mbps), Baseline 3 performs closer to the proposed joint optimization algorithm compared with Baselines 1 and 2 using uniform quantization. We can therefore conclude that the performance gain of joint optimization is mainly obtained from the quantization optimization at edge servers. On the other hand, as the fronthaul capacity increases, it is observed that Baseline 2 outperforms Baseline 3. This is due to the impact of quantization error on the performance of vertical FL becomes negligible, and thus the scheme with optimized beamforming can achieve better performance.

Next, we investigate the impact of the antennas at each edge server on the performance of vertical FL, where the fronthaul

<span id="page-11-0"></span>![](_page_11_Figure_10.jpeg)

Fig. 5. Training loss and test accuracy versus fronthaul capacity C with N=8 and M=2.

capacity is set to C=200 Mbps. Fig. 6 shows that the joint optimization for beamforming and quantization allocation still outperforms Baselines 1-3, and achieves the performance upper bound with a few antennas (i.e., M=10). In addition, we note that when M is small (i.e.,  $M\leq 10$ ), Baseline 2 has better performance compared with Baseline 3, which is due to the performance gain of beamforming optimization dominates in this stage. However, as the number of antennas M increases, the performance gap between Baseline 2 and Baseline 3 vanishes. The uniform quantization scheme used in Baseline 2 leads to severe quantization error since the capacity allocated to each antenna is very limited, which counteracts the performance gain of optimized beamforming.

## D. Cloud-RAN Versus Massive MIMO

In this subsection, we compare two promising techniques among the antenna configuration proposed for 5G wireless networks, i.e., Cloud-RAN and Massive MIMO. The former is a distributed antenna system, while the latter is a centralized antenna system. For comparison fairness, we assume that there are a total of M antennas to serve K devices. In particular, for the massive MIMO network, we assume that there is only one BS equipped with all  $\tilde{M}$  antennas, while for the Cloud-RAN network, we assume that there are N edge servers each equipped with M/N antennas. In order to compare the two configurations, we eliminate the limited fronthaul constraint in the Cloud-RAN network by setting  $C = +\infty$ , which leads to zero quantization errors when aggregating. The specific simulation settings are as follows: K = 20 devices are randomly located in a circular area of 800 m. There are a total number of antennas M = 40. For the massive MIMO network, the BS is located in the center of the circular

<span id="page-12-1"></span>![](_page_12_Figure_2.jpeg)

<span id="page-12-2"></span>Fig. 6. Training loss and test accuracy versus number of antennas of at each edge server M with N = 8 and C = 200 Mbps.

![](_page_12_Figure_4.jpeg)

Fig. 7. Training loss and test accuracy versus number of RRHs N.

area; while for the Cloud-RAN network, the edge servers are randomly located in the circular area. Furthermore, the beamforming vectors {m(t) ,u (t)} for the considered networks are obtained by Algorithm [2](#page-9-2) and Algorithm [3](#page-10-3) with C = +∞. In order to record the performance of each network, each numerical experiment runs 500 communication rounds, and the performance of the last round is recorded.

Fig. [7](#page-12-2) shows the learning performance comparison between Cloud-RAN and massive MIMO with different number of edge servers. It is observed that when there is only one edge server, the performance of the Cloud-RAN network is slightly worse than that of the massive MIMO network. However, when the number of edge servers N ≥ 2, the performance over the Cloud-RAN network outperforms that over the massive MIMO network, which is due to that the gain of distributed antenna system dominates the performance of Cloud-RAN network. Specifically, by deploying more edge servers in the network, each device can be served by the nearest edge server with strong channel conditions, which significantly mitigates communication straggler issues. A larger number of RRHs results in better channel condition due to dense deployment of RRHs. However, the capacity allocated on each server will be small, resulting in a large quantization error on the learning performance, vice versa. This leads to a trade-off between the channel conditions and quantization error in multi-antenna Cloud-RAN, which allows an optimization of the number of RRHs for maximizing the learning performance. As the total capacity increases, we should allocate more edge servers to exploit better channels for devices to improve performance.

## VI. CONCLUSION

<span id="page-12-0"></span>In this paper, we proposed a novel framework based on AirComp and Cloud-RAN to support communication-efficient vertical FL over wireless networks. To reveal the impact of limited fronthaul capacity and AirComp aggregation error on the learning performance, we characterized the convergence behavior in terms of resource allocation. Based on the derived optimization gap for the wireless vertical FL algorithm, we further established a system optimization framework to minimize optimization gap for the wireless vertical FL algorithm under various system constraints. To solve this problem, we proposed to decompose the original system optimization problem into two sub-problems, i.e., uplink and downlink optimization problems, which can be efficiently solved by successive convex approximation and alternate convex search approaches. Extensive numerical results have shown that the proposed system optimization schemes can achieve high learning performance and the effectiveness of the proposed Cloud-RAN network architecture for vertical FL was also verified.

## APPENDIX PROOF OF THEOREM [1](#page-7-5)

According to [\(4\)](#page-2-4) and Lemma [1,](#page-7-0) the partial gradient estimate ∇ˆ <sup>k</sup>F(w(t) ) is given by

<span id="page-12-3"></span>
$$\hat{\nabla}_{k}F(\boldsymbol{w}^{(t)}) = \frac{1}{L} \sum_{i=1}^{L} \hat{G}_{i} \left( \hat{s}^{(t)}(i) \right) \nabla g_{k,i}(\boldsymbol{w}_{k}) + \lambda \nabla r_{k}(\boldsymbol{w})$$

$$= \frac{1}{L} \sum_{i=1}^{L} \left( G_{i} \left( s^{(t)}(i) \right) + G'_{i} \left( s^{(t)}(i) \right) n_{\text{UL}}^{(t)}(i) + n_{\text{DL},k}^{(t)}(i) \right) \nabla g_{k,i}(\boldsymbol{w}_{k}) + \lambda \nabla r_{k}(\boldsymbol{w})$$

$$= \nabla_{k}F(\boldsymbol{w}^{(t)}) + \boldsymbol{e}_{k}^{(t)}, \tag{47}$$

where  $e_k^{(t)}$  denotes the effective communication noise for device k in the t-th communication round that is given by

$$\boldsymbol{e}_{k}^{(t)} = \frac{1}{L} \sum_{i=1}^{L} \left( G_{i}' \left( s^{(t)}(i) \right) n_{\mathrm{UL}}^{(t)}(i) + n_{\mathrm{DL},k}^{(t)}(i) \right) \nabla g_{k,i}(\boldsymbol{w}_{k}).$$
(48)

In addition, the expected norm of  $e^{(t)}$  over the noises  $n_{\mathrm{UL}}^{(t)}(i)$  and  $n_{\mathrm{DL},k}^{(t)}(i)$  can be bounded as follows

$$\mathbb{E}[\|\boldsymbol{e}_{k}^{(t)}\|^{2}] \\
= \frac{1}{L^{2}} \mathbb{E} \left\| \sum_{i=1}^{L} \left( G_{i}' \left( s^{(t)}(i) \right) n_{\mathrm{UL}}^{(t)}(i) + n_{\mathrm{DL},k}^{(t)}(i) \right) \nabla g_{k,i}(\boldsymbol{w}_{k}) \right\|^{2} \\
\stackrel{\text{(i)}}{=} \frac{1}{L^{2}} \sum_{i=1}^{L} \mathbb{E} \left[ \left( G_{i}' \left( s^{(t)}(i) \right) n_{\mathrm{UL}}^{(t)}(i) + n_{\mathrm{DL},k}^{(t)}(i) \right)^{2} \right] \|\nabla g_{k,i}(\boldsymbol{w}_{k})\|^{2} \\
+ n_{\mathrm{DL},k}^{(t)}(i)^{2} \right] \|\nabla g_{k,i}(\boldsymbol{w}_{k})\|^{2} \\
= \frac{1}{L^{2}} (\Phi_{1,k} \sigma_{\mathrm{UL}}^{2}(t) + \Phi_{2,k} \sigma_{\mathrm{DL},k}^{2}(t)), \tag{49}$$

where

$$\Phi_{1,k} = \sum_{i=1}^{L} G_i' \left( s^{(t)}(i) \right)^2 \|\nabla g_{k,i}(\boldsymbol{w}_k)\|^2, \qquad (50)$$

$$\Phi_{2,k} = \sum_{i=1}^{L} \|\nabla g_{k,i}(\mathbf{w}_k)\|^2.$$
 (51)

Let  $\boldsymbol{w}^{(t+1)} = [(\boldsymbol{w}_1^{(t+1)})^\mathsf{T}, \dots, (\boldsymbol{w}_K^{(t+1)})^\mathsf{T}]^\mathsf{T}$ , and use the definition of  $\boldsymbol{w}_k^{(t+1)}$  to obtain

$$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \mu^{(t)} \hat{\nabla} F(\mathbf{w}^{(t)}),$$
 (52)

where

$$\hat{\nabla}F(\boldsymbol{w}^{(t)}) = \underbrace{\left[\left(\nabla_{1}F(\boldsymbol{w}^{(t)})\right)^{\mathsf{T}}, \dots, \left(\nabla_{K}F(\boldsymbol{w}^{(t)})\right)^{\mathsf{T}}\right]^{\mathsf{T}}}_{=\nabla F(\boldsymbol{w}^{(t)})} + \underbrace{\left[\left(\boldsymbol{e}_{1}^{(t)}\right)^{\mathsf{T}}, \dots, \left(\boldsymbol{e}_{K}^{(t)}\right)^{\mathsf{T}}\right]^{\mathsf{T}}}_{-\boldsymbol{e}^{(t)}}.$$
 (53)

Here, the equality (i) comes from (47). Under Assumption 2, we have

<span id="page-13-7"></span>
$$F(\boldsymbol{w}^{(t+1)}) \leq F(\boldsymbol{w}^{(t)}) + \nabla F(\boldsymbol{w}^{(t)})^{\mathsf{T}}(\boldsymbol{w}^{(t+1)} - \boldsymbol{w}^{(t)}) + \frac{\beta}{2} \|\boldsymbol{w}^{(t+1)} - \boldsymbol{w}^{(t)}\|^{2}$$

$$= F(\boldsymbol{w}^{(t)}) - \mu^{(t)} \nabla F(\boldsymbol{w}^{(t)})^{\mathsf{T}} \hat{\nabla} F(\boldsymbol{w}^{(t)}) + \frac{(\mu^{(t)})^{2} \beta}{2} \|\hat{\nabla} F(\boldsymbol{w}^{(t)})\|^{2}$$

$$= F(\boldsymbol{w}^{(t)}) - \frac{1}{2\beta} \|\nabla F(\boldsymbol{w}^{(t)})\|^{2} + \frac{1}{2\beta} \|\boldsymbol{e}^{(t)}\|^{2}, \quad (54)$$

where the learning rate  $\mu^{(t)} = 1/\beta$  implies the last equality.

In order to derive a lower bound for  $\|\nabla F(\boldsymbol{w}^{(t)})\|^2$ , we use Assumption 1 and minimize both sides of (23) to obtain

$$F(\boldsymbol{w}^*) \ge F(\boldsymbol{w}) - \frac{1}{\alpha} \nabla F(\boldsymbol{w})^\mathsf{T} \nabla F(\boldsymbol{w}) + \frac{1}{2\alpha} \nabla F(\boldsymbol{w})^\mathsf{T} \nabla F(\boldsymbol{w})$$
$$= F(\boldsymbol{w}) - \frac{1}{2\alpha} \|\nabla F(\boldsymbol{w})\|^2. \tag{55}$$

Rearranging the terms, we have

<span id="page-13-6"></span>
$$\left\|\nabla F(\boldsymbol{w}^{(t)})\right\|^2 \ge 2\alpha \left(F(\boldsymbol{w}^{(t)}) - F(\boldsymbol{w}^*)\right).$$
 (56)

Subtract  $F(w^*)$  from both sides and substitute (56) into (54) to get

$$F(\boldsymbol{w}^{(t+1)}) - F(\boldsymbol{w}^*)$$

$$\leq F(\boldsymbol{w}^{(t)}) - F(\boldsymbol{w}^*) - \frac{\alpha}{\beta} \left( F(\boldsymbol{w}^{(t)}) - F(\boldsymbol{w}^*) \right) + \frac{1}{2\beta} \|\boldsymbol{e}^{(t)}\|^2$$

$$= \left( 1 - \frac{\alpha}{\beta} \right) \left( F(\boldsymbol{w}^{(t)}) - F(\boldsymbol{w}^*) \right) + \frac{1}{2\beta} \|\boldsymbol{e}^{(t)}\|^2$$
(57)

Applying this recursively, we obtain

<span id="page-13-8"></span>
$$F(\boldsymbol{w}^{T}) - F(\boldsymbol{w}^{*}) \leq \rho^{T} \left( F(\boldsymbol{w}^{0}) - F(\boldsymbol{w}^{*}) \right) + \frac{1}{2\beta} \sum_{t=0}^{T-1} \rho^{T-t-1} \|\boldsymbol{e}^{(t)}\|^{2}, \quad (58)$$

where  $\rho = 1 - \alpha/\beta$  is the contraction rate.

Taking expectations of (58) over the noises  $n_{\mathrm{UL}}^{(t)}(i)$  and  $\{n_{\mathrm{DL},k}^{(t)}(i)\}_{k=1}^K$ , we obtain

$$\mathbb{E}\left[F(\boldsymbol{w}^{T}) - F(\boldsymbol{w}^{*})\right]$$

$$\leq \rho^{T} \mathbb{E}\left[F(\boldsymbol{w}^{0}) - F(\boldsymbol{w}^{*})\right] + \frac{1}{2\beta} \sum_{t=0}^{T-1} \rho^{T-t-1} \mathbb{E}[\|\boldsymbol{e}^{(t)}\|^{2}]$$

$$\leq \rho^{T} \mathbb{E}\left[F(\boldsymbol{w}^{0}) - F(\boldsymbol{w}^{*})\right] + \frac{1}{2L^{2\beta}} B(T), \tag{59}$$

where the optimality gap B(T) is given by

$$B(T) = \sum_{t=0}^{T-1} \rho^{T-t-1} \sum_{k=1}^{K} (\Phi_{1,k} \sigma_{\mathrm{UL}}^{2}(t) + \Phi_{2,k} \sigma_{\mathrm{DL},k}^{2}(t)), \quad (60)$$

which completes the proof of Theorem 1.

#### REFERENCES

- <span id="page-13-0"></span>[1] K. B. Letaief, Y. Shi, J. Lu, and J. Lu, "Edge artificial intelligence for 6G: Vision, enabling technologies, and applications," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 1, pp. 5–36, Jan. 2022.
- <span id="page-13-1"></span>[2] Q. Yang, Y. Liu, T. Chen, and Y. Tong, "Federated machine learning: Concept and applications," ACM Trans. Intell. Syst. Technol., vol. 10, no. 2, pp. 12:1–12:19, 2019.
- <span id="page-13-2"></span>[3] W. Y. B. Lim et al., "Federated learning in mobile edge networks: A comprehensive survey," *IEEE Commun. Surveys Tuts.*, vol. 22, no. 3, pp. 2031–2063, 3rd Quart., 2020.
- <span id="page-13-3"></span>[4] K. Yang, T. Fan, T. Chen, Y. Shi, and Q. Yang, "A Quasi-Newton method based vertical federated learning framework for logistic regression," in *Proc. Neural Inf. Process. Syst. (NeurIPS)*, Dec. 2019, pp. 1–12.
- <span id="page-13-4"></span>[5] L. Liang, H. Ye, and G. Y. Li, "Toward intelligent vehicular networks: A machine learning framework," *IEEE Internet Things J.*, vol. 6, no. 1, pp. 124–135, Feb. 2019.
- <span id="page-13-5"></span>[6] P. Liu, G. Zhu, W. Jiang, W. Luo, J. Xu, and S. Cui, "Vertical federated edge learning with distributed integrated sensing and communication," *IEEE Commun. Lett.*, vol. 26, no. 9, pp. 2091–2095, Sep. 2022.

- <span id="page-14-0"></span>[\[7\]](#page-0-5) K. Wei et al., "Vertical federated learning: Challenges, methodologies and experiments," 2022, *arXiv:2202.04309*.
- <span id="page-14-1"></span>[\[8\]](#page-0-6) M. Chen et al., "Distributed learning in wireless networks: Recent progress and future challenges," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3579–3605, Dec. 2021.
- <span id="page-14-2"></span>[\[9\]](#page-0-7) K. B. Letaief, W. Chen, Y. Shi, J. Zhang, and Y. A. Zhang, "The roadmap to 6G: AI empowered wireless networks," *IEEE Commun. Mag.*, vol. 57, no. 8, pp. 84–90, Aug. 2019.
- <span id="page-14-3"></span>[\[10\]](#page-0-7) K. Yang, T. Jiang, Y. Shi, and Z. Ding, "Federated learning via overthe-air computation," *IEEE Trans. Wireless Commun.*, vol. 19, no. 3, pp. 2022–2035, Mar. 2020.
- <span id="page-14-4"></span>[\[11\]](#page-0-7) Y. Zou, Z. Wang, X. Chen, H. Zhou, and Y. Zhou, "Knowledge-guided learning for transceiver design in over-the-air federated learning," *IEEE Trans. Wireless Commun.*, vol. 22, no. 1, pp. 270–285, Jan. 2023.
- <span id="page-14-5"></span>[\[12\]](#page-0-7) Y. Shi, Y. Zhou, D. Wen, Y. Wu, C. Jiang, and K. Letaief, "Task-oriented communications for 6G: Vision, principles, and technologies," 2023, *arXiv:2303.10920*.
- <span id="page-14-6"></span>[\[13\]](#page-0-8) G. Zhu, J. Xu, K. Huang, and S. Cui, "Over-the-air computing for wireless data aggregation in massive IoT," *IEEE Wireless Commun.*, vol. 28, no. 4, pp. 57–65, Aug. 2021.
- <span id="page-14-7"></span>[\[14\]](#page-1-1) Y. Shi, K. Yang, T. Jiang, J. Zhang, and K. B. Letaief, "Communicationefficient edge AI: Algorithms and systems," *IEEE Commun. Surveys Tuts.*, vol. 22, no. 4, pp. 2167–2191, 4th Quart., 2020.
- <span id="page-14-8"></span>[\[15\]](#page-1-2) M. M. Amiri and D. Gündüz, "Machine learning at the wireless edge: Distributed stochastic gradient descent over-the-air," *IEEE Trans. Signal Process.*, vol. 68, pp. 2155–2169, 2020.
- <span id="page-14-9"></span>[\[16\]](#page-1-3) D. Fan, X. Yuan, and Y. A. Zhang, "Temporal-Structure-Assisted gradient aggregation for over-the-air federated edge learning," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3757–3771, Dec. 2021.
- <span id="page-14-10"></span>[\[17\]](#page-1-4) C. Zhong, H. Yang, and X. Yuan, "Over-the-air multi-task federated learning over MIMO interference channel," *IEEE Trans. Wireless Commun.*, vol. 22, no. 6, pp. 3853–3868, Apr. 2023.
- <span id="page-14-11"></span>[\[18\]](#page-1-5) N. Zhang and M. Tao, "Gradient statistics aware power control for overthe-air federated learning," *IEEE Trans. Wireless Commun.*, vol. 20, no. 8, pp. 5115–5128, Aug. 2021.
- <span id="page-14-12"></span>[\[19\]](#page-1-6) H. Guo, A. Liu, and V. K. N. Lau, "Analog gradient aggregation for federated learning over wireless networks: Customized design and convergence analysis," *IEEE Internet Things J.*, vol. 8, no. 1, pp. 197–210, Jan. 2021.
- <span id="page-14-13"></span>[\[20\]](#page-1-6) S. Xia, J. Zhu, Y. Yang, Y. Zhou, Y. Shi, and W. Chen, "Fast convergence algorithm for analog federated learning," in *Proc. IEEE Int. Conf. Commun. (ICC)*, Jun. 2021, pp. 1–6.
- <span id="page-14-14"></span>[\[21\]](#page-1-7) G. Zhu, Y. Wang, and K. Huang, "Broadband analog aggregation for low-latency federated edge learning," *IEEE Trans. Wireless Commun.*, vol. 19, no. 1, pp. 491–506, Jan. 2020.
- <span id="page-14-15"></span>[\[22\]](#page-1-7) H. Liu, X. Yuan, and Y. A. Zhang, "Reconfigurable intelligent surface enabled federated learning: A unified communication-learning design approach," *IEEE Trans. Wireless Commun.*, vol. 20, no. 11, pp. 7595–7609, Nov. 2021.
- <span id="page-14-16"></span>[\[23\]](#page-1-8) H. Yang, J. Zhao, Z. Xiong, K. Lam, S. Sun, and L. Xiao, "Privacypreserving federated learning for UAV-enabled networks: learning-based joint scheduling and resource management," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 10, pp. 3144–3159, Oct. 2021.
- <span id="page-14-17"></span>[\[24\]](#page-1-9) Z. Wang et al., "Federated learning via intelligent reflecting surface," *IEEE Trans. Wireless Commun.*, vol. 21, no. 2, pp. 808–822, Feb. 2022.
- <span id="page-14-18"></span>[\[25\]](#page-1-9) H. Liu, Z. Lin, X. Yuan, and Y. A. Zhang, "Reconfigurable intelligent surface empowered over-the-air federated edge learning," *IEEE Wireless Commun.*, early access, Sep. 22, 2022, doi: [10.1109/MWC.007.2200101.](http://dx.doi.org/10.1109/MWC.007.2200101)
- <span id="page-14-19"></span>[\[26\]](#page-1-9) K. Yang, Y. Shi, Y. Zhou, Z. Yang, L. Fu, and W. Chen, "Federated machine learning for intelligent IoT via reconfigurable intelligent surface," *IEEE Netw.*, vol. 34, no. 5, pp. 16–22, Sep. 2020.
- <span id="page-14-20"></span>[\[27\]](#page-1-10) T. T. Vu, D. T. Ngo, N. H. Tran, H. Q. Ngo, M. N. Dao, and R. H. Middleton, "Cell-free massive MIMO for wireless federated learning," *IEEE Trans. Wireless Commun.*, vol. 19, no. 10, pp. 6377–6392, Oct. 2020.
- <span id="page-14-21"></span>[\[28\]](#page-1-10) Z. Lin, H. Liu, and Y. A. Zhang, "Relay-assisted cooperative federated learning," *IEEE Trans. Wireless Commun.*, vol. 21, no. 9, pp. 7148–7164, Sep. 2022.
- <span id="page-14-22"></span>[\[29\]](#page-1-10) Z. Wang, Y. Zhou, Y. Shi, and W. Zhuang, "Interference management for over-the-air federated learning in multi-cell wireless networks," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 8, pp. 2361–2377, Aug. 2022.
- <span id="page-14-23"></span>[\[30\]](#page-1-11) F. P. Lin, S. Hosseinalipour, S. S. Azam, C. G. Brinton, and N. Michelusi, "Semi-decentralized federated learning with cooperative D2D local model aggregations," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3851–3869, Dec. 2021.

- <span id="page-14-24"></span>[\[31\]](#page-1-12) W. Y. B. Lim, J. S. Ng, Z. Xiong, D. Niyato, C. Miao, and D. I. Kim, "Dynamic edge association and resource allocation in self-organizing hierarchical federated learning networks," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3640–3653, Dec. 2021.
- <span id="page-14-25"></span>[\[32\]](#page-1-12) W. Zhang et al., "Optimizing federated learning in distributed industrial IoT: A multi-agent approach," *IEEE J. Sel. Areas Commun.*, vol. 39, no. 12, pp. 3688–3703, Dec. 2021.
- <span id="page-14-26"></span>[\[33\]](#page-1-13) J. Chen, Z. Chang, X. Guo, R. Li, Z. Han, and T. Hämäläinen, "Resource allocation and computation offloading for multi-access edge computing with fronthaul and backhaul constraints," *IEEE Trans. Veh. Technol.*, vol. 70, no. 8, pp. 8037–8049, Aug. 2021.
- <span id="page-14-27"></span>[\[34\]](#page-1-14) S. Park, S. Jeong, J. Na, O. Simeone, and S. Shamai (Shitz), "Collaborative cloud and edge mobile computing in C-RAN systems with minimal end-to-end latency," *IEEE Trans. Signal Inf. Process. Netw.*, vol. 7, pp. 259–274, 2021.
- <span id="page-14-28"></span>[\[35\]](#page-1-15) Y. Shi, J. Zhang, K. B. Letaief, B. Bai, and W. Chen, "Large-scale convex optimization for ultra-dense cloud-RAN," *IEEE Wireless Commun.*, vol. 22, no. 3, pp. 84–91, Jun. 2015.
- <span id="page-14-29"></span>[\[36\]](#page-1-16) M. Tao, E. Chen, H. Zhou, and W. Yu, "Content-centric sparse multicast beamforming for cache-enabled cloud RAN," *IEEE Trans. Wireless Commun.*, vol. 15, no. 9, pp. 6118–6131, Sep. 2016.
- <span id="page-14-30"></span>[\[37\]](#page-1-17) L. Su and V. K. N. Lau, "Hierarchical federated learning for hybrid data partitioning across multitype sensors," *IEEE Internet Things J.*, vol. 8, no. 13, pp. 10922–10939, Jul. 2021.
- <span id="page-14-31"></span>[\[38\]](#page-3-5) O. Abari, H. Rahul, D. Katabi, and M. Pant, "AirShare: Distributed coherent transmission made seamless," in *Proc. IEEE Conf. Comput. Commun. (INFOCOM)*, Apr. 2015, pp. 1742–1750.
- <span id="page-14-32"></span>[\[39\]](#page-3-6) A. Mahmood, M. I. Ashraf, M. Gidlund, J. Torsner, and J. Sachs, "Time synchronization in 5G wireless edge: Requirements and solutions for critical-MTC," *IEEE Commun. Mag.*, vol. 57, no. 12, pp. 45–51, Dec. 2019.
- <span id="page-14-33"></span>[\[40\]](#page-3-7) R. G. Stephen and R. Zhang, "Uplink channel estimation and data transmission in millimeter-wave CRAN with lens antenna arrays," *IEEE Trans. Commun.*, vol. 66, no. 12, pp. 6542–6555, Dec. 2018.
- <span id="page-14-34"></span>[\[41\]](#page-4-6) Y. Zhou and W. Yu, "Fronthaul compression and transmit beamforming optimization for multi-antenna uplink C-RAN," *IEEE Trans. Signal Process.*, vol. 64, no. 16, pp. 4138–4151, Aug. 2016.
- <span id="page-14-35"></span>[\[42\]](#page-4-6) L. Liu and R. Zhang, "Optimized uplink transmission in multi-antenna C-RAN with spatial compression and forward," *IEEE Trans. Signal Process.*, vol. 63, no. 19, pp. 5083–5095, Oct. 2015.
- <span id="page-14-36"></span>[\[43\]](#page-4-7) S. Park, O. Simeone, O. Sahin, and S. Shamai (Shitz), "Fronthaul compression for cloud radio access networks: Signal processing advances inspired by network information theory," *IEEE Signal Process. Mag.*, vol. 31, no. 6, pp. 69–79, Nov. 2014.
- <span id="page-14-37"></span>[\[44\]](#page-5-4) A. E. Gamal and Y. Kim, *Network Information Theory*. Cambridge, U.K.: Cambridge Univ. Press, 2011.
- <span id="page-14-38"></span>[\[45\]](#page-7-7) C. M. Bishop, "Training with noise is equivalent to Tikhonov regularization," *Neural Comput.*, vol. 7, no. 1, pp. 108–116, Jan. 1995.
- <span id="page-14-39"></span>[\[46\]](#page-7-8) F. Ang, L. Chen, N. Zhao, Y. Chen, W. Wang, and F. R. Yu, "Robust federated learning with noisy communication," *IEEE Trans. Commun.*, vol. 68, no. 6, pp. 3452–3464, Jun. 2020.
- <span id="page-14-40"></span>[\[47\]](#page-7-9) X. Li, K. Huang, W. Yang, S. Wang, and Z. Zhang, "On the convergence of FedAvg on non-IID data," in *Proc. Int. Conf. Learn. Represent. (ICLR)*, 2020, pp. 1–12.
- <span id="page-14-41"></span>[\[48\]](#page-7-10) M. Chen, Z. Yang, W. Saad, C. Yin, H. V. Poor, and S. Cui, "A joint learning and communications framework for federated learning over wireless networks," *IEEE Trans. Wireless Commun.*, vol. 20, no. 1, pp. 269–283, Jan. 2021.
- <span id="page-14-42"></span>[\[49\]](#page-7-11) M. P. Friedlander and M. Schmidt, "Hybrid deterministic-stochastic methods for data fitting," *SIAM J. Sci. Comput.*, vol. 34, no. 3, pp. A1380–A1405, Jan. 2012.
- <span id="page-14-43"></span>[\[50\]](#page-9-8) M. Grant and S. Boyd. (Mar. 2014). *CVX: MATLAB Software for Disciplined Convex Programming, Version 2.1*. [Online]. Available: http://cvxr.com/cvx
- <span id="page-14-44"></span>[\[51\]](#page-9-9) Y. Zhou and W. Yu, "Optimized backhaul compression for uplink cloud radio access network," *IEEE J. Sel. Areas Commun.*, vol. 32, no. 6, pp. 1295–1307, Jun. 2014.
- <span id="page-14-45"></span>[\[52\]](#page-10-5) J. Gorski, F. Pfeuffer, and K. Klamroth, "Biconvex sets and optimization with biconvex functions: A survey and extensions," *Math. Methods Oper. Res.*, vol. 66, no. 3, pp. 373–407, Nov. 2007.
- <span id="page-14-46"></span>[\[53\]](#page-10-6) *Further Advancements for E-Utra Physical Layer Aspects*, 3GPP, document TR 36, 2010.

![](_page_15_Picture_2.jpeg)

Yuanming Shi (Senior Member, IEEE) received the B.S. degree in electronic engineering from Tsinghua University, Beijing, China, in 2011, and the Ph.D. degree in electronic and computer engineering from The Hong Kong University of Science and Technology (HKUST) in 2015. Since September 2015, he has been with the School of Information Science and Technology, ShanghaiTech University, where he is currently a tenured Associate Professor. He visited the University of California, Berkeley, CA, USA, from October 2016 to February 2017. His research

interests include optimization, machine learning, wireless communications and their applications to 6G, the IoT, and edge AI. He was a recipient of the 2016 IEEE Marconi Prize Paper Award in Wireless Communications, the 2016 Young Author Best Paper Award by the IEEE Signal Processing Society, and the 2021 IEEE ComSoc Asia–Pacific Outstanding Young Researcher Award. He is an Editor of IEEE TRANSACTIONS ON WIRELESS COMMU-NICATIONS, IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, and *Journal of Communications and Information Networks*.

![](_page_15_Picture_5.jpeg)

Shuhao Xia (Graduate Student Member, IEEE) received the B.S. degree in computer science from ShanghaiTech University, Shanghai, China, in 2017, where he is currently pursuing the Ph.D. degree with the School of Information Science and Technology. His research interests include machine learning, optimization, signal processing, reconfigurable intelligent surface, and their applications to 6G.

![](_page_15_Picture_7.jpeg)

Yong Zhou (Senior Member, IEEE) received the B.Sc. and M.Eng. degrees from Shandong University, Jinan, China, in 2008 and 2011, respectively, and the Ph.D. degree from the University of Waterloo, Waterloo, ON, Canada, in 2015. From November 2015 to January 2018, he was a Post-Doctoral Research Fellow with the Department of Electrical and Computer Engineering, The University of British Columbia, Vancouver, Canada. He is currently an Assistant Professor with the School of Information Science and Technology,

ShanghaiTech University, Shanghai, China. His research interests include the Internet of Things, edge artificial intelligence, and reconfigurable intelligent surface.

![](_page_15_Picture_10.jpeg)

Yijie Mao (Member, IEEE) received the first B.Eng. degree from the Beijing University of Posts and Telecommunications, the second B.Eng. degree (Hons.) from the Queen Mary University of London, London, U.K., in 2014, and the Ph.D. degree from the Electrical and Electronic Engineering Department, The University of Hong Kong, Hong Kong, China, in 2018. She was a Post-Doctoral Research Fellow with The University of Hong Kong, from 2018 to 2019; and a Post-Doctoral Research Associate with the Communications and Signal Pro-

cessing Group (CSP), Department of Electrical and Electronic Engineering, Imperial College London, London, from 2019 to 2021. Since 2021, she has been an Assistant Professor with the School of Information Science and Technology, ShanghaiTech University, Shanghai, China. Her research interests include the design of future wireless communications and artificial intelligence-empowered wireless networks. She received the Best Paper Award of *EURASIP Journal on Wireless Communications and Networking* in 2022 and the Exemplary Reviewer for IEEE TRANSACTIONS ON COMMU-NICATIONS in 2021 and IEEE COMMUNICATIONS LETTERS in 2022. She was a technical program committee (TPC) member of many symposia on wireless communication for several leading international IEEE conferences. She was a Workshop Co-Chair of 2020–2022 IEEE ICC, 2021–2023 IEEE WCNC, and 2020–2022 IEEE PIMRC. She is serving as an Associate Editor for IEEE COMMUNICATIONS SURVEYS AND TUTORIALS and IEEE COMMUNICATIONS LETTERS, a Guest Editor for two special issues of IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS and IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY.

![](_page_15_Picture_14.jpeg)

Chunxiao Jiang (Senior Member, IEEE) received the B.S. degree (Hons.) in information engineering from Beihang University, Beijing, in 2008, and the Ph.D. degree (Hons.) in electronic engineering from Tsinghua University, Beijing, in 2013. He is an Associate Professor with the School of Information Science and Technology, Tsinghua University. He was a Joint Ph.D. Student (2011–2012) and a Post-Doctoral Researcher (2013–2016) with the Department of Electrical and Computer Engineering, University of Maryland, College Park, under the

supervision of Prof. K. J. Ray Liu. His research interests include application of game theory, optimization, and statistical theories to communication, networking, and resource allocation problems, in particular space networks and heterogeneous networks. He is a fellow of IET. He was a recipient of the Best Paper Award from IEEE GLOBECOM in 2013, the IEEE Communications Society Young Author Best Paper Award in 2017, the Best Paper Award from ICC 2019, the IEEE VTS Early Career Award in 2020, the IEEE ComSoc Asia–Pacific Best Young Researcher Award in 2020, the IEEE VTS Distinguished Lecturer in 2021, and the IEEE ComSoc Best Young Professional Award in 2021. He received the Chinese National Second Prize in Technical Inventions Award in 2018 and the Natural Science Foundation of China Excellent Young Scientists Fund Award in 2019. He has served as a member for the technical program committee and the symposium chair for a number of international conferences. He has served as an Editor for IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE INTERNET OF THINGS JOURNAL, IEEE WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON NETWORK SCIENCE AND ENGINEERING, IEEE NETWORK, and IEEE COMMUNICATIONS LETTERS; and a Guest Editor for *IEEE Communications Magazine*, IEEE TRANSACTIONS ON NETWORK SCIENCE AND ENGINEERING, and IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING.

![](_page_15_Picture_17.jpeg)

Meixia Tao (Fellow, IEEE) received the B.S. degree in electronic engineering from Fudan University, Shanghai, China, in 1999, and the Ph.D. degree in electrical and electronic engineering from The Hong Kong University of Science and Technology in 2003.

She is a Professor with the Department of Electronic Engineering, Shanghai Jiao Tong University, China. Her current research interests include wireless edge learning, coded caching, reconfigurable intelligence surfaces, and semantic communications.

Dr. Tao received the 2019 IEEE Marconi Prize Paper Award, the 2013 IEEE Heinrich Hertz Award for Best Communications Letters, the IEEE/CIC International Conference on Communications in China (ICCC) 2015 Best Paper Award, and the International Conference on Wireless Communications and Signal Processing (WCSP) 2012 and 2022 Best Paper Awards. She also received the 2009 IEEE ComSoc Asia–Pacific Outstanding Young Researcher Award. She served as the TPC Co-Chair for IEEE ICC 2023. She is an Associate Editor of the IEEE TRANSACTIONS ON INFORMATION THEORY and the Editor-at-Large of the IEEE OPEN JOURNAL OF THE COMMUNI-CATIONS SOCIETY. She served as a member for the Executive Editorial Committee of the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, from 2015 to 2019. She was also on the Editorial Board of several other journals as an Editor or a Guest Editor, including the IEEE TRANSACTIONS ON COMMUNICATIONS and IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS.
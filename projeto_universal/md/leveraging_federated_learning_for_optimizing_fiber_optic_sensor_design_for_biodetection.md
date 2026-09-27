---
title: "Leveraging Federated Learning For Optimizing Fiber Optic Sensor Design For Biodetection"
tema_principal: projeto_universal
temas_relacionados: []
ano: 2024
autores: []
veiculo: null
pdf: ../pdf/leveraging_federated_learning_for_optimizing_fiber_optic_sensor_design_for_biodetection.pdf
---

#### **RESEARCH ARTICLE**

![](_page_0_Picture_2.jpeg)

# **Leveraging Federated Learning For Optimizing Fiber Optic Sensor Design For Biodetection**

**Yogendra Swaroop Dwivedi1 · Rishav Singh2 · Anuj K. Sharma1  [·](http://orcid.org/0000-0002-3382-3084) Ajay Kumar Sharma3**

Received: 5 August 2024 / Accepted: 2 January 2025 / Published online: 18 January 2025 © The Author(s), under exclusive licence to The Optical Society of India 2025

#### **Abstract**

This paper explores integrating federated learning methodologies to optimize and generalize sensor design for plasmonic-based fiber optic sensors (FOS) applicable in biosensing, removing reliance on specific experimental datasets. By employing machine learning (ML) models, the enhancement of FOS design's figure of merit (FOM) becomes achievable through training on localized data. However, to establish a more universally applicable ML model tailored to distinct applications, amalgamating data and training from diverse sources becomes imperative. FOS finds extensive utility in medical contexts where data privacy stands as a paramount concern, necessitating stringent consent and regulatory adherence for data sharing. Given the challenges posed by decentralized datasets and the criticality of data privacy, federated learning emerges as an indispensable framework, enabling the refinement of generalized ML models while upholding the sanctity of individual data privacy. Through the utilization of the Gaussian Process Regressor (GPR) model for localized training within discrete datasets, federated learning facilitates collaborative model refinement without compromising data privacy. This collaborative approach harnesses collective insights to bolster sensor performance, preserving data privacy boundaries and demonstrating potential enhancements without centralizing data aggregation. The research underscores the potential of federated learning in optimizing sensor design, accentuating its pivotal role in elevating sensing proficiency while safeguarding individual data privacy constraints, thereby paving the way for forthcoming practical implementations in biosensing applications.

**Keywords** Federated learning · Sensor · Figure of merit · Machine learning · Gaussian process regression

Based on a presentation at (PPICEFP-2024) organized by the Department of Physics and Material Science, (MMMUT) Gorakhpur, during March 1–2, 2024.

- Anuj K. Sharma anujsharma@nitdelhi.ac.in
- <sup>1</sup> Physics Division, Department of Applied Sciences, National Institute of Technology Delhi, GT Karnal Road, Delhi 110036, India
- <sup>2</sup> Department of Computer Science and Engineering, Indian Institute of Technology Patna, Bihta, Patna 801106, India
- <sup>3</sup> Department of Computer Science and Engineering, National Institute of Technology Delhi, GT Karnal Road, Delhi 110036, India

## **Introduction**

In recent times, the advancement of high-performance optical biosensors has brought about significant changes across multiple domains, such as drug discovery [[1\]](#page-6-0), biomedical devices [\[2](#page-6-1)], clinical diagnostics [[3\]](#page-6-2), food processing control [[4\]](#page-6-3), and environmental monitoring [\[5](#page-6-4)]. These biosensors are essential for delivering precise, sensitive, and specific measurements of target analytes, with critical parameters like sensitivity, accuracy, specificity, selectivity, response time, and reusability defining their effectiveness and usefulness [[6\]](#page-6-5).

Surface plasmon resonance (SPR) has become a widely adopted technique for developing high-performance sensors and biosensors in various applications [[7\]](#page-6-6). Among these, fiber optic SPR sensors have attracted considerable interest owing to their distinctive advantages, including flexibility, robustness, and remote-sensing capabilities [[8\]](#page-6-7). Over time, advancements in SPR-based sensors have been driven by

![](_page_0_Picture_17.jpeg)

exploring different phenomena, such as integrating twodimensional (2D) materials like graphene and molybdenum disulfide (MoS2) [\[9](#page-6-8)], into sensor designs.

MoS2, with its favorable characteristics such as a large band gap, high absorption efficiency, and hydrophobic nature, has demonstrated superior sensitivity in biosensing applications compared to other 2D materials [\[10](#page-6-9)]. Combining thin layers of MoS2 with fiber optic SPR sensors has shown promise in enhancing sensor performance, particularly through the optimization of radiation damping [[11](#page-6-10)]—a phenomenon that influences the absorption of light by the plasmonic structure.

The optimization of radiation damping, achieved by appropriately selecting parameters such as incident light wavelength (λ) and metal layer thickness (dm), is critical for maximizing the FOM of fiber optic SPR sensors. FOM, defined as the product of sensitivity and accuracy, serves as a comprehensive metric for evaluating sensor performance. Pre-experimental simulations play a crucial role in optimizing sensor design parameters, including λ, dm, and the choice of optical fiber and 2D material.

However, performing simulations for multilayer plasmonic sensor designs often requires careful consideration of parameter ranges and step sizes to ensure accuracy. Conventional simulation approaches with small step sizes and wide parameter ranges often demand significant computational resources, leading to practical challenges in achieving optimal designs.

To address these challenges, exploring techniques such as ML and artificial intelligence (AI) could be considered viable solutions. The advancements in AI since 2011, particularly in deep learning, have significantly contributed to research and development activities in this field [[12](#page-6-11)].

<span id="page-1-0"></span>![](_page_1_Figure_7.jpeg)

**Fig. 1** Pattern similarty between predicted and actual FOM

![](_page_1_Picture_9.jpeg)

In our previous work, we have explored the application of ML [\[13](#page-6-12)] techniques in optimizing sensor design parameters, drawing inspiration from the advancements in AI-driven approaches to address key challenges in optical biosensing. As highlighted in recent literature, AI and ML have played instrumental roles in overcoming various issues encountered in photonics and optical fiber-based devices, such as low data processing speed, signal-to-noise ratio (SNR) degradation over fiber length, management of large data volumes, and cross-sensitivity.

Our work was built by leveraging the core essence of ML—predicting outcomes on unseen data—to enhance the FOM of fiber optic SPR sensors. By training ML models on existing sensor data obtained from varying parameter ranges (λ and dm), we aim to predict optimal combinations of λ and dm that maximize FOM. This approach not only streamlined the sensor design process but also accelerates the discovery of high-performance configurations, highlighting the transformative potential of AI and ML in advancing optical sensing technologies. Figure [1](#page-1-0) shows that the trend of predicted FOM is almost completely matched with that of the actual FOM, which indicates towards good training and high accuracy of GPR [\[14](#page-6-13)] model implemented for this particular result.

Moreover, the fusion of ML techniques with sensor design optimization presents compelling prospects for future research avenues. By leveraging AI-driven insights, researchers can explore innovative methodologies aimed at augmenting sensor sensitivity, precision, and specificity, thereby catalyzing advancements in the development of next-generation optical biosensors for a wide array of applications spanning biomedical, environmental, and industrial domains. Specifically, SPR sensors excel in biomedical sensing applications, such as detecting hemoglobin levels in blood. However, due to the sensitive nature of this data, individuals and agencies are often reluctant to share it. To develop a more generalized model capable of accommodating diverse data from various geographical locations. federated learning emerges as a pivotal approach. This technique allows for the refinement of models without the need to share raw data, instead focusing on sharing the trained model parameters.

To address these challenges, this work explores the potential of federated learning—a decentralized machine learning paradigm—in optimizing fiber optic SPR sensor designs. Federated learning [\[15](#page-6-14)] enables model training across distributed datasets without the need to centralize sensitive data, thus preserving privacy and scalability. By leveraging federated learning techniques, ML models can be trained collaboratively across multiple sensor nodes, each contributing its local data while keeping it secure and private. This approach not only enhances privacy but also enables more efficient model training by leveraging distributed computational resources. In this context, federated learning emerges as a pivotal approach. This technique allows for the refinement of models without the need to share raw data, instead focusing on sharing the trained model parameters. By adopting federated learning, researchers can develop generalized sensor models capable of accommodating diverse datasets from different locations without compromising data privacy, thus advancing the development of next-generation optical biosensors for various applications in biomedical, environmental, and industrial settings.

By integrating federated learning into the optimization process of fiber optic SPR sensor designs, this study aims to overcome computational constraints and privacy concerns, ultimately leading to enhanced sensor performance and utility in biosensing applications.

#### **Literature review**

The optimization of SPR sensors for biosensing applications has been the subject of extensive research in recent years. These sensors hold immense potential in various fields, including drug discovery, biomedical devices, clinical diagnostics, food processing control, and environmental monitoring. Achieving high-performance sensors requires meticulous attention to parameters such as sensitivity, accuracy, specificity, selectivity, response time, and reusability. Researchers have explored numerous strategies to enhance the capabilities of fiber optic SPR sensors, among which optimization techniques and the integration of two-dimensional (2D) materials have been particularly prominent.

Traditional optimization approaches have typically relied on simulation-based methodologies to fine-tune sensor design parameters. These methodologies involve the systematic exploration of factors such as incident light wavelength (λ), metal layer thickness (dm), and the selection of appropriate 2D materials to maximize sensor performance. While effective, these simulation methods often face challenges in computational efficiency, especially when dealing with complex multilayered sensor designs. Moreover, concerns about data privacy arise when utilizing centralized data aggregation, particularly in scenarios involving sensitive biomedical data.

In response to these challenges, researchers have turned to ML techniques as a promising avenue for sensor optimization. ML algorithms, particularly supervised learning models, have shown promise in predicting sensor performance based on input parameters. These models analyze datasets generated from simulations or experimental measurements to identify patterns and correlations, thereby facilitating the optimization of sensor designs. To further contextualize the utilization of machine learning in optimizing fiber optic SPR (FOS) sensor designs, several noteworthy research studies have demonstrated the efficacy of ML in enhancing sensor performance. For instance, researchers have applied ML techniques to process data from tilted fiber Bragg grating (TFBG)-assisted SPR sensors, streamlining the analysis and interpretation of sensor outputs. Additionally, optimization methodologies such as Taguchi approach, machine learning, and genetic algorithms have been employed to refine the design parameters of photonic crystal fiber (PCF) based SPR sensors, showcasing the synergy between traditional optimization techniques and ML-driven approaches. Moreover, the development of "SmartSPR" sensors [[16\]](#page-6-15) has exemplified how ML algorithms can be harnessed to create intelligent surface plasmon resonance sensors capable of adaptive and responsive sensing. Notably, recent work has also explored the application of ML with localized surface plasmon resonance (LSPR) sensors for detecting specific analytes such as SARS-CoV-2 particles [[17\]](#page-6-16), highlighting the potential of ML-driven sensor technologies in addressing pressing healthcare challenges. These pioneering studies underscore the versatility and transformative impact of ML in advancing the capabilities of FOS sensors for diverse applications in biomedical diagnostics, environmental monitoring, and beyond.

However, traditional ML approaches require centralized data aggregation, raising concerns about data privacy and scalability in distributed sensor networks.

To overcome these limitations, federated learning has emerged as a compelling solution for optimizing sensor designs while preserving data privacy in distributed environments. Federated learning decentralizes the model training process by allowing individual sensor nodes to train ML models locally using their respective datasets. These local models are then aggregated to generate a global model, enabling collaborative optimization without exposing sensitive data to centralized servers. By leveraging federated learning, researchers can harness the collective intelligence of distributed sensor networks while ensuring privacy and scalability.

In our earliear work, we leveraged GPR as a machine learning model to optimize fiber optic SPR sensor designs. Our study resulted in a remarkable 11% improvement in the FOM, achieving a peak FOM of 6526.23 RIU−1 compared to the existing peak FOM of 5897.08 RIU−1 . The GPR model accurately predicted the peak FOM at λ=1099.343 nm, highlighting the crucial role of light wavelength step size (0.001 nm) in enhancing FOM through the manipulation of Optical Path Difference (ORD). The high accuracy of our machine learning model was evidenced by the close match between predicted and actual FOM trends, with an R² value near 1 and a Mean Absolute Error (MAE) of 78.32 RIU−1 .

![](_page_2_Picture_12.jpeg)

Subsequent analysis with a larger dataset of 714 data points further validated our approach, achieving a predicted FOM of 6356.98 RIU−1 at λ=1099.345 nm and dm = 29.8 nm, representing an 8% improvement over the actual FOM. The improved accuracy with the larger dataset, reflected by an MAE of 65.69 RIU−1 and an R² value near 0.9, underscores the efficacy and potential of our machine learning model in optimizing sensor performance. Figure [2](#page-3-0) exibits the Gaussian pattern shown by SPR sensor dataset.

Moving forward, additional research efforts are essential to refine and develop robust federated learning frameworks specifically tailored to the challenges inherent in sensor optimization. Overcoming obstacles such as communication overhead, effective model aggregation [[18\]](#page-6-17), and privacy-preserving mechanisms will be pivotal in ensuring the broader applicability and adoption of federated learning within sensor networks. Furthermore, the integration of federated learning with advanced optimization techniques, including evolutionary algorithms and reinforcement learning, presents exciting opportunities for achieving optimal sensor designs that exhibit enhanced performance and utility in biosensing applications. By fostering interdisciplinary collaborations and exploring novel algorithmic approaches, researchers can unlock new frontiers in sensor technology, paving the way for transformative advancements in biosensing and related domains.

#### **Methodology**

In the realm of biosensing technology, optimizing the design of photonic sensors is critical for achieving high performance and reliability across diverse applications. Leveraging simulation-based optimization and ML techniques

<span id="page-3-0"></span>![](_page_3_Figure_6.jpeg)

**Fig. 2** Gaussian pattern exhibited by FOS dataset

![](_page_3_Picture_8.jpeg)

presents a powerful approach to enhancing sensor performance. Specifically, the integration of federated learning within this framework offers a promising avenue to address privacy concerns and facilitate collaborative model refinement without centralized data aggregation.

The following methodology outlines a systematic approach that integrates simulation-based insights with ML capabilities, including federated learning, to optimize the design of photonic sensors for biosensing applications.

Integration of Simulation-Based Optimization and ML Techniques: The methodology integrates simulation-based optimization techniques with machine learning approaches, including federated learning. This integration is crucial for optimizing photonic sensor design, as it allows for a comprehensive exploration of sensor parameters and their impact on biosensing performance.

**Parameter optimization for Photonic sensors** The methodology begins with parameter optimization, focusing on key design parameters relevant to photonic sensors used in biosensing applications. By systematically varying parameters like incident light wavelength and material choices, the methodology aims to enhance sensor performance metrics such as sensitivity and accuracy.

**Simulation-based modeling for Sensor Behavior** Simulation-based modeling is employed to predict the behavior of photonic sensors under different conditions, including variations in environmental factors and analyte concentrations. This step is essential for understanding how sensor design choices influence biosensing performance.

**Machine learning integration for performance prediction** Machine learning techniques, particularly supervised learning algorithms, are utilized to analyze simulation data and predict sensor performance based on input parameters. This integration enables the development of predictive models that can guide sensor design optimization.

**Federated Learning for privacy-preserving collaboration** The adoption of federated learning addresses privacy concerns associated with centralized data aggregation. By enabling collaborative model training across distributed sensor nodes while preserving data privacy, federated learning facilitates the optimization of photonic sensor design for biosensing applications in a secure and scalable manner.

Overall, the described methodology provides a systematic and innovative approach to leveraging federated learning for optimizing photonic sensor design in biosensing. It combines simulation-based insights with machine learning capabilities, including federated learning, to enhance sensor

<span id="page-4-1"></span>**Fig. 3** Federated learning architecuture

![](_page_4_Figure_3.jpeg)

<span id="page-4-2"></span>**Table 1** Few instances of the used dataset

| Metal layer Thickness | Wavelength | FOM         |
|-----------------------|------------|-------------|
| (nm)                  | (nm)       | (RIU−1<br>) |
| 29.74                 | 1099       | 524.9882    |
| 29.78                 | 1099.29    | 941.0315    |
| 29.80                 | 1099.33    | 3050.223    |
| 29.82                 | 1099.47    | 907.2284    |
| 29.87                 | 1099.5     | 506.9020    |

performance while ensuring data privacy and scalability a topic that is highly relevant and impactful for advancing biosensing technologies. By incorporating federated learning, the methodology emphasizes privacy-preserving collaboration and the development of generalized models across distributed sensor networks, facilitating transformative progress in biosensing technology.

## **Federated learning for sensor design optimization**

To apply federated learning for optimizing sensor design and making it more generalized, the workflow can be structured as follows:

- 1. **Data Partitioning**: Initially, the sensor data from different sources or data collected on different enviournment condtions are partitioned into decentralized datasets while ensuring data privacy and regulatory compliance. As shown in Fig. [3](#page-4-1) these dataset are shosn as FOS dataset1, FOS dataset2 etc. A sample dataset from our previous work is shown Table [1](#page-4-2), the complete dataset can be considered as FOS dataset 1.
- 2. **Local Model Training**: Each FOS data source locally trains a GPR model using its respective dataset. The

<span id="page-4-0"></span>**Table 2** Summary of procedure and results

| Input Parameters              |                   |
|-------------------------------|-------------------|
| dm range                      | 29.76 to 29.84 nm |
| λ range                       | 1099 to 1099.5 nm |
| Step size of λ variation      | 0.001 nm          |
| Total data points             | 459               |
| Train dataset size            | 367               |
| Test dataset size             | 92                |
| Evaluation Parameters         |                   |
| R2                            | 0.927211439       |
| Adjusted R2                   | 0.926811501       |
| MSE                           | 34418.53653       |
| RMSE                          | 185.5223343       |
| Mean absolute error (MAE)     | 78.32097826 RIU−1 |
| Results Summary               |                   |
| Existing FOM                  | 5897.082119 RIU−1 |
| Predicted FOM                 | 6526.226903 RIU−1 |
| Existing peak FOM wavelength  | 1099.35 nm        |
| Predicted peak FOM wavelength | 1099.343 nm       |
| ∆ (FOM)                       | 629.144784 RIU-1  |
| % change                      | 10.66874721       |

GPR model learns from the local data to optimize sensor performance based on specified metrics (e.g., figure of merit, sensitivity).The trained model should be evaludated for critical parameters like *R*<sup>2</sup> and RMSE. If accuracy is low for a particular site hyper parameter tunning should be done before moving to next step else this may cause overall degradation of accuracy.The evaluation parameter from our earlier work are shown in Table [2.](#page-4-0) The outcome of this step is trained GPR model at a particular site as shown in blue square in Fig. [3.](#page-4-1)

3. **Collaborative Model Aggregation**: Collaborative model aggregation in the context of federated learning plays a crucial role in optimizing sensor design

![](_page_4_Picture_15.jpeg)

for fiber FOS in biosensing applications. This process involves aggregating locally trained GPR models from distributed data sources without centralizing raw data. By leveraging techniques such as secure multiparty computation or differential privacy, sensitive model parameters are securely combined to create a refined global model. During aggregation, model parameters are updated through weighted averaging or other aggregation schemes, where weights can reflect the reliability or quality of local models. Asynchronous updates are accommodated, allowing data sources to contribute to model refinement at different intervals. Collaborative model aggregation ensures that insights from diverse datasets contribute collectively to enhancing sensor performance, while preserving individual data privacy and complying with regulatory constraints in medical contexts. This iterative process of aggregation and parameter updates iteratively refines the sensor design, leveraging collective knowledge from decentralized sources to optimize sensor performance.

Personalized federated learning (PFL) [[19\]](#page-6-18) can be used to extend the capabilities of collaborative model aggregation in federated learning for optimizing sensor design in biosensing applications. PFL allows for the training of personalized models tailored to the specific characteristics and data distributions of individual clients or nodes within the federated network. This approach accommodates data heterogeneity between clients by focusing on learning personalized models that reflect unique client attributes, enhancing the overall performance and adaptability of the federated learning system. The aggresated model is shown in blue circle in Fig. [3.](#page-4-1)

- 4. **Parameter Updates**: During the aggregation process, model parameters are updated based on weighted averaging or other aggregation techniques. This collaborative approach ensures that insights from diverse data sources contribute to refining the sensor design.
- 5. **Global Model Refinement**: The aggregated model parameters are used to update a global GPR model. This refined global model captures collective knowledge while adapting to heterogeneous data characteristics across different sources.

#### **Implications and challenges**

The integration of federated learning methodologies to optimize sensor design for FOS in biosensing carries significant implications and opens up promising avenues for future research and applications. Firstly, the use of federated learning addresses critical concerns related to data privacy and regulatory compliance, particularly in sensitive medical contexts where stringent data protection measures are essential. By allowing model training on decentralized data sources without data leaving individual devices, federated learning ensures data privacy while still enabling model refinement and generalization.

Looking ahead, future research can explore several important directions. One key area is the development of advanced federated learning algorithms tailored specifically for optimizing sensor designs. Innovations in privacy-preserving techniques, such as secure aggregation and differential privacy, will be pivotal in enhancing the scalability and security of federated learning approaches.

Furthermore, efforts should focus on addressing challenges related to heterogeneous data sources and model convergence. Federated learning models need to adapt to variations in data distributions and quality across different devices, necessitating robust strategies for managing data heterogeneity and ensuring convergence of collaborative models.

Another important future direction involves the application of federated learning to real-world biosensing applications beyond theoretical frameworks. Practical implementations and validations of federated learning in diverse sensor design scenarios will provide valuable insights into its effectiveness and feasibility in real-world settings.

The integration of federated learning into sensor design optimization represents a promising frontier in biosensing research. Addressing privacy concerns, advancing algorithmic innovations, and validating practical applications will be instrumental in realizing the full potential of federated learning for enhancing sensor performance while safeguarding data privacy.

#### **Conclusion**

In this study, we have proposed an innovative approach leveraging federated learning in conjunction with the GPR model to optimize FOS for biosensing applications. By adopting federated learning, we aimed to address key challenges associated with data privacy and scalability in sensor design optimization. Our work demonstrates the potential of federated learning to facilitate collaborative model training across distributed sensor nodes, allowing for the refinement of ML models without compromising individual data privacy.

The integration of federated learning with the GPR model represents a significant step towards achieving more

![](_page_5_Picture_16.jpeg)

generalized sensor designs capable of accommodating diverse datasets from different geographical locations. By decentralizing the model training process and focusing on sharing trained model parameters rather than raw data, federated learning ensures data privacy while harnessing collective insights to enhance sensor performance.

Looking ahead, future research directions should focus on refining federated learning frameworks tailored specifically to sensor optimization challenges. Addressing issues such as communication overhead, effective model aggregation, and privacy-preserving mechanisms will be crucial for the widespread adoption of federated learning in sensor networks. Additionally, integrating federated learning with advanced optimization techniques, such as evolutionary algorithms and reinforcement learning, holds promise for achieving optimal sensor designs with enhanced performance and utility in biosensing applications.

### **References**

- <span id="page-6-0"></span>1. Y. Tao, L. Chen, M. Pan, F. Zhu, D. Zhu, ACS Sens. **6**, 3146–3162 (2021). <https://doi.org/10.1021/acssensors.1c01600>
- <span id="page-6-1"></span>2. A. Haleem, M. Javaid, R.P. Singh, R. Suman, S. Rab, Sens. Int. **2**, 100100 (2021). <https://doi.org/10.1016/j.sintl.2021.100100>
- <span id="page-6-2"></span>3. S. Panesar, X. Weng, S. Neethirajan, IEEE Sens. Lett. **1**, 1–4 (2017). <https://doi.org/10.1109/LSENS.2017.2727983>
- <span id="page-6-3"></span>4. V. Mythili, in International Conference on Advanced Communication Control and Computing Technologies (IEEE, 2016), pp. 333–336.<https://doi.org/10.1109/ICACCCT.2016.7831657>
- <span id="page-6-4"></span>5. J. Newman, A. Turner, A. Rickman, A. Harpin, M. Shaw, J. McKen-, zie, in IEE Colloquium on Optical Techniques for Environmental Monitoring (IET, 1995), p. 3/1–3/6. [https://doi.org/10.](https://doi.org/10.1049/ic:19951117) [1049/ic:19951117](https://doi.org/10.1049/ic:19951117)
- <span id="page-6-5"></span>6. W.J. Peveler, M. Yazdani, V.M. Rotello, ACS Sens. **1**, 1282–1285 (2016). <https://doi.org/10.1021/acssensors.6b00564>
- <span id="page-6-6"></span>7. A.K. Sharma, A. Dominic, IEEE Sens. J. **18**, 4053–4058 (2018). <https://doi.org/10.1109/JSEN.2018.2818197>

- <span id="page-6-7"></span>8. D. Michel, F. Xiao, K. Alameh, Sens. Actuators B Chem. **246**, 258–261 (2017). <https://doi.org/10.1016/j.snb.2017.02.064>
- <span id="page-6-8"></span>9. W. Choi, N. Choudhary, G.H. Han, J. Park, D. Akinwande, Y.H. Lee, Mater. Today. **20**, 116–130 (2017). [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.mattod.2016.10.002) [mattod.2016.10.002](https://doi.org/10.1016/j.mattod.2016.10.002)
- <span id="page-6-9"></span>10. M. Kukkar, A. Sharma, P. Kumar, K.H. Kim, A. Deep, Anal. Chim. Acta. **939**, 101–107 (2016). [https://doi.org/10.1016/j.aca.](https://doi.org/10.1016/j.aca.2016.08.010) [2016.08.010](https://doi.org/10.1016/j.aca.2016.08.010)
- <span id="page-6-10"></span>11. A.K. Sharma, B. Kaur, IEEE Photon Technol. Lett. **30**, 2021– 2024 (2018).<https://doi.org/10.1109/LPT.2018.2874700>
- <span id="page-6-11"></span>12. I.H. Sarker, SN Comput. Sci. **2**, 1–20 (2021). [https://doi.org/10.1](https://doi.org/10.1007/s42979-021-00815-1) [007/s42979-021-00815-1](https://doi.org/10.1007/s42979-021-00815-1)
- <span id="page-6-12"></span>13. Y.S. Dwivedi, R. Singh, A.K. Sharma, A.K. Sharma, IEEE Sens. J. **23**, 2320–2327 (2023). [https://doi.org/10.1109/JSEN.2022.322](https://doi.org/10.1109/JSEN.2022.3225858) [5858](https://doi.org/10.1109/JSEN.2022.3225858)
- <span id="page-6-13"></span>14. Jie, Wang, Comput. Sci. Eng. **25**, 4–11 (2023). [https://doi.org/10.](https://doi.org/10.1109/MCSE.2023.3342149) [1109/MCSE.2023.3342149](https://doi.org/10.1109/MCSE.2023.3342149)
- <span id="page-6-14"></span>15. J. Wen, Z. Zhang, Y. Lan, I.J. Mach, Learn. Cyber. **14**, 513–535 (2023).<https://doi.org/10.1007/s13042-022-01647-y>
- <span id="page-6-15"></span>16. J. Qu, A. Dillen, W. Saeys, Anal. Chim. Acta. **1104**, 10–27 (2020). <https://doi.org/10.1016/j.aca.2019.12.067>
- <span id="page-6-16"></span>17. J. Liang, W. Zhang, Y. Qin, Y. Li, G.L. Liu, W. Hu, Biosensors. **12**, 173 (2022). <https://doi.org/10.3390/bios12030173>
- <span id="page-6-17"></span>18. P. Qi, D. Chiaro, A. Guzzo, M. Ianni, G. Fortino, F. Piccialli, Future Gener Comput. Syst. **150**, 272–293 (2024). [https://doi.org](https://doi.org/10.1016/j.future.2023.09.008) [/10.1016/j.future.2023.09.008](https://doi.org/10.1016/j.future.2023.09.008)
- <span id="page-6-18"></span>19. I. Achituve, A. Shamsian, A. Navon, G. Chechik, E. Fetaya, in International conference on Neural Information Processing Systems (NeurIPS, 2021), pp. 8392–8406. [https://proceedings.neurip](https://proceedings.neurips.cc/paper_files/paper/2021/file/46d0671dd4117ea366031f87f3aa0093-Paper.pdf) [s.cc/paper\\_files/paper/2021/file/46d0671dd4117ea366031f87f3a](https://proceedings.neurips.cc/paper_files/paper/2021/file/46d0671dd4117ea366031f87f3aa0093-Paper.pdf) [a0093-Paper.pdf](https://proceedings.neurips.cc/paper_files/paper/2021/file/46d0671dd4117ea366031f87f3aa0093-Paper.pdf)

**Publisher's note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

![](_page_6_Picture_26.jpeg)
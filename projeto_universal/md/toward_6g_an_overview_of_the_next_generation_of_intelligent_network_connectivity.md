---
title: "Toward 6G: An Overview of the Next Generation of Intelligent Network Connectivity"
tema_principal: projeto_universal
temas_relacionados: []
ano: 2024
autores: []
veiculo: null
pdf: ../pdf/toward_6g_an_overview_of_the_next_generation_of_intelligent_network_connectivity.pdf
---

![](_page_0_Picture_0.jpeg)

<span id="page-0-1"></span>Received 6 October 2024, accepted 19 December 2024, date of publication 26 December 2024, date of current version 2 January 2025.

Digital Object Identifier 10.1109/ACCESS.2024.3523327

![](_page_0_Picture_3.jpeg)

# **Toward 6G: An Overview of the Next Generation** of Intelligent Network Connectivity

SIVARAMA PRASAD TERA<sup>10</sup>1, RAVIKUMAR CHINTHAGINJALA<sup>10</sup>2, GIOVANNI PAU<sup>103</sup>, (Senior Member, IEEE), AND TAE HOON KIM<sup>4</sup>
<sup>1</sup>Department of Electronics and Electrical Engineering, Indian Institute of Technology at Guwahati, Guwahati, Assam 781039, India

Corresponding authors: Giovanni Pau (giovanni.pau@unikore.it) and Ravikumar Chinthaginjala (cvrkvit@gmail.com)

This work was supported in part by Zhejiang Provincial Natural Science Foundation Youth Fund Project under Grant LQ23F010004, and in part by the National Natural Science Youth Science Foundation Project under Grant 62201508.

**ABSTRACT** The development of 6G networks represents a groundbreaking leap in mobile communication, targeting the creation of an Intelligent Network of Everything that seamlessly integrates advanced technologies such as Artificial Intelligence (AI), Machine Learning (ML), and the Internet of Everything (IoE). This next-generation network is projected to begin standardization in 2025, with commercial deployment anticipated by 2030. Building on the foundation of its predecessors, 6G aims to deliver ultrareliable, low-latency, and high-speed communication essential for applications like autonomous systems, immersive virtual environments, and smart cities. This article provides a comprehensive overview of 6G, articulating its vision and identifying the core technologies that will enable its transformative capabilities. The key contributions of this work include a detailed exploration of prospective 6G applications and use cases, such as autonomous systems and integrated communication-sensing scenarios. Additionally, it identifies major challenges—such as advanced coding schemes, energy management, and security and presents a roadmap for future research in these critical areas. The study also reviews potential coding and modulation techniques, such as non-binary codes and lattice codes, assessing their suitability for 6G's stringent performance requirements. Security and privacy considerations are also covered, proposing a robust architecture across all network layers to address emerging threats. Furthermore, the article compiles a literature review on 6G visions and surveys, providing valuable insights into the current state of research, highlighting gaps, and guiding future studies. Through the exploration of spectrum advancements, antenna technologies, network intelligence, and AI/ML integration, this work establishes a clear vision for how 6G can reshape global communication infrastructure and drive innovation in a hyper-connected world.

**INDEX TERMS** Sixth-generation (6G), potential technologies, Internet of Everything (IoE), intelligent network of everything, artificial intelligence (AI), machine learning (ML).

#### <span id="page-0-0"></span>I. INTRODUCTION

The emergence of 6G networks marks the next evolutionary step in mobile communication, building upon the foundation laid by its predecessors to offer unprecedented levels of connectivity and intelligence. As global efforts unite towards the development and standardization of 6G, projected to commence in 2025 with commercial deployment around

The associate editor coordinating the review of this manuscript and approving it for publication was Yeon-Ho Chung.

2030, the vision for 6G extends beyond mere communication improvements. It aims to create an Intelligent Network of Everything, integrating advanced technologies.

The concept of the Intelligent Network of Everything represents the next evolution in the interconnected digital landscape, merging the principles of the Internet of Everything (IoE) with advanced artificial intelligence (AI) to create a truly intelligent and adaptive network environment. This vision goes beyond merely connecting people, devices, data, and processes; it aims to infuse the network with cognitive

<sup>&</sup>lt;sup>2</sup>School of Electronics Engineering, Vellore Institute of Technology, Vellore, Tamil Nadu 632014, India

<sup>&</sup>lt;sup>3</sup>Faculty of Engineering and Architecture, Kore University of Enna, 94100 Enna, Italy

<sup>&</sup>lt;sup>4</sup>School of Information and Electronic Engineering, Zhejiang University of Science and Technology, Zhejiang 310023, China

![](_page_1_Picture_1.jpeg)

capabilities, enabling it to learn, adapt, and make real-time decisions autonomously.

In this paradigm, the network itself becomes an intelligent entity, capable of understanding the context of interactions and optimizing performance dynamically. For instance, in a smart city, the intelligent network could predict traffic patterns and adjust traffic signals accordingly, manage energy distribution based on real-time demand, or provide personalized services to residents by analyzing their behavior and preferences. Similarly, in industrial settings, it could monitor machinery, predict maintenance needs, and adjust production processes to minimize downtime and maximize efficiency.

The Intelligent Network of Everything leverages 6G connectivity to offer ultra-high-speed, low-latency, and highly reliable communication, which is crucial for supporting the real-time data exchange required for such intelligent systems. The integration of AI enables the network to process vast amounts of data from billions of connected devices, extract actionable insights, and make autonomous decisions. This results in a more responsive and resilient network infrastructure, capable of supporting complex, data-intensive applications such as autonomous vehicles, smart healthcare, and immersive virtual experiences.

Ultimately, the Intelligent Network of Everything envisions a future where digital and physical worlds seamlessly converge, creating a smart and responsive environment that enhances human life, optimizes business operations, and enables new levels of innovation and efficiency. This network will be the backbone of future societies, providing the foundation for a truly intelligent and interconnected world.

Central to the 6G vision is the concept of mobile intelligence, a transformative approach that seeks to embed intelligence at all layers of the network—from core and edge to the air interface—through the pervasive use of AI and ML. This paradigm shift will empower devices, systems, and applications to operate with heightened awareness and adaptability, effectively revolutionizing the way they interact with humans and the environment. The integration of the Internet of Everything (IoE) further extends this vision, facilitating seamless connectivity between sensors, devices, vehicles, and various automated systems, thus driving the evolution of smart environments and autonomous operations.

# A. THE EVOLUTIONARY MILESTONES OF MOBILE NETWORKS: 1G TO 6G

The evolution of mobile networks from 1G to 6G in Figure [1](#page-2-0) showcases a remarkable journey of technological advancements, each generation building upon the innovations of the previous one to address the increasing demands for connectivity, speed, and intelligence.

The journey began in the 1980s with the introduction of the first generation (1G) of mobile networks, characterized by analog technology and basic mobile telephony. Systems like Nordic Mobile Telephone (NMT) and Advanced Mobile Phone System (AMPS) enabled users to make voice calls <span id="page-1-2"></span><span id="page-1-1"></span><span id="page-1-0"></span>wirelessly, though with limited coverage, low capacity, and susceptibility to interference [\[1\],](#page-31-0) [\[2\],](#page-31-1) [\[3\].](#page-31-2)

The second generation (2G) indicated a major transition from analog to digital communication in the 1990s. As the industry standard, the Global System for Mobile Communications (GSM) brought text messaging (SMS) and enhanced voice quality. While the major goal was still to improve mobile telephony, this era set the groundwork for later mobile data services [\[4\],](#page-31-3) [\[5\].](#page-31-4)

<span id="page-1-4"></span><span id="page-1-3"></span>The 2000s witnessed the emergence of the third generation (3G), which revolutionized mobile communications by introducing mobile internet access. With the Universal Mobile Telecommunications System (UMTS) at its core, 3G networks enabled faster data transmission, allowing for multimedia messaging, mobile web browsing, and video calling. This generation set the stage for the data-driven applications that have become integral to modern life [\[6\],](#page-31-5) [\[7\].](#page-31-6)

<span id="page-1-6"></span><span id="page-1-5"></span>The 2010s brought the fourth generation (4G) of mobile networks, which further accelerated mobile data speeds and transformed user experiences. Long-Term Evolution (LTE) technology provided the backbone for high-speed internet access on mobile devices, supporting services like HD video streaming, real-time gaming, and seamless connectivity for apps. 4G's enhanced capacity and reduced latency were pivotal in meeting the growing demands for mobile broadband [\[8\],](#page-31-7) [\[9\],](#page-32-0) [\[10\],](#page-32-1) [\[11\],](#page-32-2) [\[12\].](#page-32-3)

<span id="page-1-12"></span><span id="page-1-11"></span><span id="page-1-10"></span><span id="page-1-9"></span><span id="page-1-8"></span><span id="page-1-7"></span>Entering the 2020s, the fifth generation (5G) introduced a new paradigm of mobile intelligence. 5G networks, which make use of New Radio (NR) technology [\[13\],](#page-32-4) offer extremely high data rates, low latency, and the capacity to link billions of devices at once. Smart cities, industrial automation, driver less vehicles, and the Internet of Things (IoT) are just a few of the applications that this generation is intended to assist. The emphasis on mobile intelligence has enabled 5G to drive innovation across multiple sectors, pushing the boundaries of what mobile networks can achieve [\[14\],](#page-32-5) [\[15\],](#page-32-6) [\[16\],](#page-32-7) [\[17\].](#page-32-8)

<span id="page-1-16"></span><span id="page-1-15"></span><span id="page-1-14"></span><span id="page-1-13"></span>Looking ahead, the 2030s are expected to usher in the sixth generation (6G) of mobile networks, which aims to further enhance mobile intelligence and connectivity. While the specific technologies and standards for 6G are still under development, it is anticipated that 6G will offer unprecedented data rates, advanced AI integration, and support for emerging applications that are currently beyond our imagination. The focus on sustainability, security, and global connectivity will be paramount as 6G seeks to address the challenges and opportunities of a hyper-connected world.

In summary, the evolution from 1G to 6G reflects the relentless pursuit of innovation in mobile communications. Each generation has not only improved upon the capabilities of its predecessor but has also introduced new possibilities, fundamentally transforming the way we live, work, and interact in an increasingly connected world.

This article presents a holistic overview and in-depth guide to 6G, providing a comprehensive survey of current research, technological developments, and future prospects.

![](_page_2_Picture_1.jpeg)

<span id="page-2-0"></span>![](_page_2_Figure_2.jpeg)

**FIGURE 1.** The evolutionary milestones of mobile networks: 1G to 6G.

It covers fundamental elements of 6G, including key use cases, performance requirements, and potential challenges, while also exploring emerging technologies through a tutorial approach, drawing inspiration from [\[18\]](#page-32-9) and [\[19\]. T](#page-32-10)he aim is to offer readers a thorough understanding of 6G, from its conceptual framework to practical implementation strategies, and to highlight its potential impact on society and industry.

Our Contributions include:

- Articulation of 6G Vision and Key Enablers: It defines the vision for 6G, including its core features like ultrahigh capacity, low latency, and AI/ML integration, and identifies the critical technologies that will enable these features.
- Survey of 6G Applications and Use Cases: The document explores potential 6G applications, including autonomous systems, immersive experiences, and integrated communication-sensing scenarios.
- Identification of Challenges and Research Directions: It outlines major challenges such as advanced coding schemes, energy management, and security, and provides a road-map for future research in these areas.
- Analysis of Channel Coding and Modulation Techniques: The study reviews potential coding and modulation techniques like non-binary codes and lattice codes, assessing their suitability for 6G's stringent requirements.
- Literature Review: The article compiles a review of current 6G research, providing a valuable resource for identifying gaps and advancing future studies.

This paper is organized into several key sections that systematically explore the evolution and future of 6G technologies. Section [I](#page-0-0) begins by providing an overview of the evolutionary milestones of mobile networks, tracing the advancements from 1G to the anticipated 6G. Following this, Section [II](#page-2-1) outlines the critical stages and milestones <span id="page-2-3"></span><span id="page-2-2"></span>in 6G development, offering a global perspective on current research and a detailed literature review on 6G visions and surveys. Section [III](#page-5-0) explains how the content is organized, guiding readers through the logical flow of the paper. Section [IV](#page-7-0) delves into the transformative advancements expected to shape 6G, setting the stage for the next generation of mobile technology. Section [V](#page-8-0) outlines the key performance metrics, including extreme data rates, low latency, and enhanced reliability. The integration of AI and ML is examined in Section [VI,](#page-9-0) which highlights how these technologies will enhance network capabilities and efficiencies. Section [VII](#page-13-0) explores a range of cutting-edge technologies crucial for the development of 6G, covering topics such as spectrum-level innovations, advanced antenna systems, transmission schemes, network intelligence, energyaware approaches, security enhancements, and potential channel coding schemes. Section [VIII](#page-30-0) focuses on the unique attributes that will distinguish 6G from previous generations, emphasizing extreme performance, ultra-flexibility, advanced intelligence, and a commitment to sustainability. Finally, Section [IX](#page-31-8) summarizes the insights and findings presented throughout the paper, reinforcing the significance of 6G in shaping the future of global communications and the continued evolution of mobile networks.

## <span id="page-2-1"></span>**II. ROAD MAP TO 6G**

# A. THE DEVELOPMENT AND STANDARDIZATION PROCESS OF 6G

Similar to 5G, the development of 6G is characterized by a structured and collaborative procedure, involving the mobile network industry, academia, standardization bodies, and regulatory organizations. The process encompasses phases from research and development through to testing, implementation, and commercialization, with various stakeholders playing pivotal roles at each stage.

![](_page_3_Picture_1.jpeg)

The International Telecommunication Union Radiocommunication Sector (ITU-R) is instrumental in shaping the vision for 6G, defining the framework under the IMT-2030 initiative. This includes setting performance and service requirements, evaluation criteria, and selecting suitable technologies for standardization. The ITU-R's initial reports on IMT-2030 outline future technological trends, emerging services, and applications, as well as potential advancements in radio interface and network technologies.

A critical milestone in the 6G development timeline occurred in November 2023, when the ITU-R published the document. This document lays the groundwork by detailing trends, usage scenarios, capabilities, and the ongoing evolution of the IMT-2030 standards. The next phase, slated between 2024 and 2026, will focus on defining and refining the performance and service requirements, with the final phase targeting the evaluation and selection of compliant Radio Interface Technologies (RITs) by 2027-2030.

In addition to ITU-R, the 3rd Generation Partnership Project (3GPP) plays a key role in the standardization of 6G, particularly as 5G standards reach maturity. The standardization efforts for 6G are expected to begin with 3GPP Release 20 (2025-2026), which will be the first to study 6G, followed by Release 21 (2027-2028), marking the first official 6G standard. This process will also involve frequency band allocations, facilitated by the World Radio Conferences (WRCs), which occur every three to four years to coordinate spectrum management globally.

The global commercialization of 6G networks is projected to commence around 2030, aligning with the completion of these standardization activities. This timeline reflects the iterative and collaborative nature of mobile communication development, ensuring that 6G networks are not only technologically advanced but also meet the diverse needs of industries, governments, and society at large.

## B. 6G RESEARCH MILESTONES: A GLOBAL OVERVIEW

As shown in Figure [2,](#page-4-0) the global research journey into 6G began in 2018, with numerous initiatives and projects aimed at exploring the possibilities and challenges of this next-generation technology. Key activities during the early stages included foundational research, collaborations among academia, industry, and governments, as well as significant investments aimed at defining the vision and technical requirements of 6G.

## 1) EARLY RESEARCH INITIATIVES (2018-2019)

The initial years saw the launch of the Finnish 6G Flagship Program, a major research initiative designed to develop and test enabling technologies for 6G. This program, along with other early studies, highlighted critical aspects such as wireless communications, AI integration, and the Internet of Everything (IoE). Key publications during this phase, including the first 6G vision articles and white papers, outlined the conceptual framework of 6G and posed questions about the future needs and capabilities of mobile networks.

# 2) EXPANDING RESEARCH SCOPE (2020-2021)

As 6G research expanded globally, countries like South Korea, Japan, the United States, and members of the European Union began investing heavily in 6G-related projects. Collaborations such as the Hexa-X initiative in the EU focused on developing fundamental enablers for 6G, including THz communications, advanced MIMO, and intelligent surface technologies. Major corporations and academic institutions worldwide hosted conferences, workshops, and collaborative research events to discuss emerging trends.

## 3) KEY DEVELOPMENTS AND COLLABORATIONS (2022-2023)

During this period, significant progress was made in both theoretical and applied aspects of 6G. Governments and private organizations across the globe funded extensive research into AI-driven network optimization, secure communication protocols, and advanced spectrum management techniques. Collaborative efforts, such as those between leading technology firms and research institutions, aimed to address challenges in areas like network architecture, device connectivity, and seamless integration of non-terrestrial networks (NTNs). The ITU-R's ongoing work on the IMT-2030 framework further shaped the direction of 6G standardization, laying the groundwork for upcoming deployment phases.

# 4) EMERGING TRENDS AND FUTURE DIRECTIONS (2024 AND BEYOND)

Looking ahead, the focus of 6G research will increasingly shift toward real-world trials and the refinement of standards. Future research activities are expected to delve deeper into the integration of AI across all layers of the 6G stack, the deployment of ultra-dense networks, and the exploration of new spectrum bands such as THz frequencies. The ITU-R and 3GPP are set to continue their pivotal roles in coordinating global efforts, ensuring that 6G technologies meet diverse performance, security, and sustainability goals.

Overall, the development of 6G is characterized by a highly collaborative, multi-disciplinary approach that brings together the best of global research and innovation. This comprehensive effort seeks not only to push the boundaries of what is technically possible but also to address the societal, economic, and environmental impacts of deploying such transformative technologies.

#### C. LITERATURE REVIEW ON 6G VISIONS AND SURVEYS

From Table [1,](#page-6-0) the literature on 6G has rapidly evolved since the first vision articles were published in 2018. These early works speculated on the necessity of 6G by evaluating the strengths and limitations of preceding generations and introduced the foundational concepts that would guide subsequent research and development efforts.

![](_page_4_Picture_1.jpeg)

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

**FIGURE 2.** 6G research milestones.

<span id="page-4-1"></span>![](_page_4_Figure_4.jpeg)

**FIGURE 3.** Literature review on 6G visions and surveys.

# 1) 6G VISION ARTICLES

The initial 6G vision articles emerged in 2018, setting the stage for future research. Key publications include the Finnish 6G Flagship Program's introductory articles, which emphasized interdisciplinary research. By 2019, the scope of 6G vision articles expanded to cover diverse aspects, such as usage scenarios, target requirements, AI-driven network design, and the integration of space-air-ground-underwater networks.

In 2020, the volume of 6G vision articles peaked, with numerous papers exploring potential applications, challenges, and key features of 6G, such as the convergence of AI and communication technologies. These works addressed the evolution from mobile edge computing to more sophisticated, AI-enabled architectures that could support diverse and demanding use cases. Visions for 6G as a global ''intelligent network'' also began to take shape, incorporating concepts like pervasive AI, THz communications, and the Internet of Senses.

Between 2021 and 2024, new vision articles continued to refine the 6G landscape. These articles explored comprehensive ecosystem models, emphasizing security, spectrum efficiency, and AI-empowered mobile networks. They provided a top-down view of the 6G ecosystem,

![](_page_5_Picture_1.jpeg)

discussing societal impacts, technical requirements, and the necessary advancements in network architecture to achieve the envisioned capabilities.

#### 2) 6G SURVEY ARTICLES

Survey articles have been instrumental in consolidating 6G research findings, providing comprehensive overviews of the technological and application landscapes. The first major surveys, published in 2020, reviewed the architectural frameworks, core technologies, and potential applications of 6G. Subsequent surveys delved deeper into the network requirements, application scenarios, and future challenges, offering insights into the evolution from 5G to 6G.

Key surveys highlighted the need for high data rates, energy efficiency, and robust security measures within 6G networks. They examined enabling technologies, such as intelligent communication systems, advanced spectrum management techniques, and AI-driven network optimization. By mapping the research frontiers, these surveys have guided ongoing efforts to address open challenges and explore new avenues for technological innovation in 6G.

Overall, the literature on 6G vision and survey articles in Figure [3](#page-4-1) paints a dynamic picture of an evolving technological paradigm, with a strong focus on integrating advanced AI, expanding connectivity through new frequency bands, and meeting the increasing demands of a hyperconnected, intelligent world.

# <span id="page-5-0"></span>**III. STRUCTURE OF THE ARTICLE**

This article provides a comprehensive overview of the vision, development, and future directions of 6G technology. As shown in Table [2,](#page-6-1) the structure of the article is systematically organized to guide the reader through the evolution of mobile communication technologies, the defining elements, and applications of 6G. The main sections of the article are outlined as follows:

- 1) Section: Introduction:
  - Subsection: The Evolutionary Milestones of Mobile Networks: 1G to 6G: This part of the paper sets the stage by tracing the historical development of mobile networks. It begins with 1G, the first generation of analog cellular networks, progressing through each subsequent generation– 2G with digital transmission, 3G with mobile internet access, 4G with broadband capabilities, and 5G with enhanced connectivity and speed. The section culminates with a discussion on the anticipated advancements in 6G, highlighting how each generation has built upon the last and set the groundwork for the future.
- 2) Section: Road Map to 6G:
  - Subsection: The Development and Standardization Process of 6G: This subsection outlines the sequential development stages that the 6G network is expected to undergo. It identifies key milestones,

- such as initial research, standardization processes, trials, and expected deployment timelines, giving a clear road map for the evolution of 6G.
- Subsection: 6G Research Milestones: A Global Overview: Provides a comprehensive overview of the global efforts in 6G research. This includes insights into major research projects, collaborations among leading technology companies, universities, and international bodies, as well as the contributions of different countries in the race toward 6G development.
- Subsection: Literature Review on 6G Visions and Surveys: Reviews existing literature on the visions and expectations for 6G. It summarizes various surveys and research papers, discussing common themes, projected capabilities, and the challenges highlighted by researchers in achieving the 6G vision.
- 3) Section: Structure of the Article: This section serves as a guide for the reader, explaining the overall organization of the paper. It details how each section builds upon the previous one to create a cohesive narrative, making it easier for the reader to follow the flow of the paper.
- 4) Section: The Vision and Performance Benchmarks for 6G Networks: This section delves into the high-level vision for 6G. It describes the transformative advancements that 6G aims to bring, such as unprecedented data speeds, ultra-low latency, global coverage including remote and underserved areas, and the integration of satellite networks. It also explores the societal impacts of 6G, including potential new use cases like advanced healthcare delivery, immersive experiences through virtual and augmented reality, and the expansion of the Internet of Things (IoT) on a massive scale.
- 5) Section: Main Performance Requirements for 6G: This section identifies the critical performance metrics that 6G networks aim to achieve. Key requirements include: Extreme Data Rates, Ultra-Low Latency, Enhanced Reliability and Availability, High Energy Efficiency etc.
- 6) AI/ML for 6G: This section explores the crucial role of AI and ML in 6G networks. It discusses how AI/ML will be integrated to optimize network performance, manage complex network architectures, enable selforganization, enhance security, and drive efficiencies in data processing and management. It also examines the potential of AI-driven predictive maintenance and automated network management.
- 7) Section: Prospective Technologies for 6G Evolution: This comprehensive section explores a wide range of cutting-edge technologies that will be instrumental in the evolution of 6G. It includes:
  - Subsection: Spectrum Advancements in 6G: Discusses new spectrum bands, including terahertz

![](_page_6_Picture_1.jpeg)

<span id="page-6-0"></span>**TABLE 1.** Summary of key 6G vision and survey articles.

| Year | Key Contributions                 | Main Topics                                               | References             |
|------|-----------------------------------|-----------------------------------------------------------|------------------------|
| 2018 | Early 6G vision, Finnish 6G Flag- | Strengths of past generations, interdisci-                | [20], [21]             |
|      | ship Program                      | plinary research                                          |                        |
| 2019 | Expanded visions on AI and net-   | AI-driven design, space-air-ground net-                   | [22], [23]             |
|      | work design                       | works                                                     |                        |
| 2020 | Peak in 6G vision publications    | AI/ML, potential applications, global intel-              | [24], [25], [26], [27] |
|      |                                   | ligent networks                                           |                        |
| 2021 | Development of EU's Hexa-X ini-   | Ecosystem models, spectrum, AI in mobile [28], [29], [30] |                        |
|      | tiative                           | networks                                                  |                        |
| 2022 | Survey on 6G evolution and chal-  | 5G to 6G evolution, enabling technologies,                | [31], [32], [19]       |
|      | lenges                            | societal impacts                                          |                        |
| 2023 | Recent trends and enablers        | Technological enablers, performance indica-               | [33], [34]             |
|      |                                   | tors, applications                                        |                        |
| 2024 | Focus on upcoming 6G challenges   | AI integration, spectrum management, ad-                  | [35], [36]             |
|      |                                   | vanced connectivity                                       |                        |

#### <span id="page-6-1"></span>**TABLE 2.** Article overview.

| Section                                           | Sub section                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I. Introduction                                   | The Evolutionary Milestones of Mobile Networks: 1G to 6G                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| II. Road map to 6G                                | <ul> <li>The Development and Standardization Process of 6G</li> <li>6G Research Milestones: A Global Overview</li> <li>Literature Review on 6G Visions and Surveys</li> </ul>                                                                                                                                                                                                                                                                                                                          |
| III. Structure of the article                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| IV. The Vision and Performance Bench-             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| marks for 6G                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| V. Main Performance Requirements for              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 6G                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VI. AI/ML for 6G                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VII. Prospective Technologies for 6G<br>Evolution | <ul> <li>Spectrum Advancements in 6G</li> <li>Transformative Antenna Systems for the 6G</li> <li>Pioneering Transmission Schemes for 6G</li> <li>Advancing Connectivity Through 6G Network Architectures</li> <li>Enabling Intelligent 6G Networks with AI</li> <li>Sustainable and Energy-Efficient 6G Networks</li> <li>Device-Centric Communication Innovations in 6G Networks</li> <li>Designing Resilient and Trustworthy 6G Networks</li> <li>Potential Channel Coding Schemes for 6G</li> </ul> |
| VIII. Defining Features for 6G                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| IX. Conclusion                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

frequencies, and techniques to efficiently use and manage these bands.

- Subsection: Transformative Antenna Systems for the 6G: Explores advanced antenna technologies such as massive MIMO and beamforming to support higher data rates and more reliable connections.
- Subsection: Pioneering Transmission Schemes for 6G: Covers innovative transmission schemes like orbital angular momentum multiplexing and NOMA to enhance spectral efficiency.
- Subsection: Advancing Connectivity Through 6G Network Architectures: Discusses architectural innovations such as cell-free networks and network

![](_page_7_Picture_1.jpeg)

- slicing, which allow for more flexible and efficient use of network resources.
- Subsection: Enabling Intelligent 6G Networks with AI: Focuses on the application of network intelligence through AI to enable autonomous network operations and real-time decision-making.
- Subsection: Sustainable and Energy-Efficient 6G Networks: Highlights energy-efficient technologies aimed at reducing the environmental impact of 6G, including green communication methods and energy harvesting.
- Subsection: Device-Centric Communication Innovations in 6G Networks: Looks at technologies that enhance communication at the device level, such as ultra-compact and efficient antennas, advanced battery technologies, and AI-enabled end-user devices.
- Subsection: Designing Resilient and Trustworthy 6G Networks: Addresses the need for advanced security measures in 6G, including quantumresistant encryption, enhanced privacy protocols, and AI-based threat detection.
- Subsection: Potential Channel Coding Schemes for 6G: Discusses new channel coding techniques designed to improve data transmission efficiency and error correction in 6G networks.
- 8) Section: Defining Features for 6G: This section emphasizes the unique characteristics that will set 6G apart from its predecessors. Key features include: Extreme Performance, Ultra-Flexibility, Advanced Intelligence, Sustainability etc.
- 9) Section: Conclusion: The paper concludes by summarizing the insights and findings from the previous sections, reinforcing the significance of 6G in the future of global communications. It emphasizes the transformative potential of 6G and its role in continuing the evolution of mobile networks, setting the stage for future innovations.

## <span id="page-7-0"></span>**IV. THE VISION AND PERFORMANCE BENCHMARKS FOR 6G NETWORKS**

The vision for 6G in Figure [4](#page-8-1) encompasses the next evolution in mobile communication, aiming to establish a ubiquitous, intelligent, and ultra-connected network ecosystem. It seeks to integrate advanced wireless technologies, AI, and IoE to create an ''Intelligent Network of Everything'' enabling seamless interactions between humans, devices, and environments. This vision is broader and more far-reaching than previous generations, targeting not just communication enhancements but also transformative impacts on various industries and daily life, creating new opportunities for societal benefit, enhanced quality of life, and economic growth.

# A. FUNDAMENTAL ELEMENTS OF 6G

To realize this vision, 6G is built upon three fundamental elements:

- Wireless Connectivity: Essential for providing the backbone of 6G, it includes advanced forms of communication, computation, and sensing. This layer supports ultra-reliable and high-speed connections necessary for next-generation applications.
- Artificial Intelligence (AI): AI is a core enabler across the entire 6G network architecture, enhancing network management, service delivery, and user experience. It operates from the core network to the edge, optimizing performance, predicting needs, and automating decision-making processes.
- Internet of Everything (IoE): Encompassing the vast network of connected devices, sensors, and systems, IoE aims to expand connectivity beyond traditional devices, including vehicles, drones, and smart infrastructure, creating a deeply interconnected digital environment.

#### B. DISRUPTIVE APPLICATIONS OF 6G

6G is expected to drive a wide array of disruptive applications, categorized into three primary areas:

- <span id="page-7-3"></span><span id="page-7-2"></span><span id="page-7-1"></span>• Human-Machine Interactions: This includes innovations such as the metaverse [\[37\],](#page-32-11) [\[38\],](#page-32-12) augmented and virtual reality (AR/VR) [\[39\], a](#page-32-13)nd digital twins, which demand ultra-high data rates and low latency to support immersive and interactive experiences [\[40\].](#page-32-14)
- <span id="page-7-15"></span><span id="page-7-14"></span><span id="page-7-13"></span><span id="page-7-12"></span><span id="page-7-11"></span><span id="page-7-10"></span><span id="page-7-9"></span><span id="page-7-8"></span><span id="page-7-7"></span><span id="page-7-6"></span><span id="page-7-5"></span><span id="page-7-4"></span>• Smart Environments: 6G will enhance smart cities [\[41\],](#page-32-15) [\[42\],](#page-32-16) [\[43\], f](#page-32-17)actories [\[44\],](#page-32-18) [\[45\],](#page-32-19) [\[46\], h](#page-32-20)omes [\[47\],](#page-32-21) [\[48\],](#page-32-22) [\[49\],](#page-32-23) and other environments [\[50\],](#page-32-24) [\[51\]](#page-32-25) by leveraging AI and IoE for better resource management, security, and user customization. This entails providing beyond-communication capabilities like sensing and intelligent data processing.
- <span id="page-7-21"></span><span id="page-7-20"></span><span id="page-7-19"></span><span id="page-7-18"></span><span id="page-7-17"></span><span id="page-7-16"></span>• Connected Autonomous Systems: Autonomous vehicles [\[52\],](#page-32-26) [\[53\],](#page-33-0) [\[54\], d](#page-33-1)rones, and robotic systems [\[55\],](#page-33-2) [\[56\],](#page-33-3) [\[57\]](#page-33-4) will benefit from 6G's reliable and fast connectivity, enabling independent operation across various settings. This includes stringent performance requirements in terms of reliability, availability, and mobility, particularly in safety-critical applications.

# C. KEY USE CASES

6G is anticipated to expand the capabilities of mobile networks significantly, introducing use cases that go beyond communication to include:

- Communication-Oriented Use Cases: These focus on enhancing core communication dimensions such as capacity, latency, reliability, and mobility, supporting applications like ultra-broadband multimedia communications and mission-critical networks.
- Beyond-Communication Use Cases: 6G aims to support network intelligence, energy efficiency, and extensive network sensing, which are crucial for enabling a wide range of intelligent applications and services.

![](_page_8_Picture_1.jpeg)

<span id="page-8-1"></span>![](_page_8_Figure_2.jpeg)

**FIGURE 4.** Overview of 6G vision.

#### D. PERFORMANCE REQUIREMENTS

To support its ambitious vision, 6G targets extreme performance metrics, including:

- Data Rates: Peak data rates up to 200 Gbit/s and user-experienced rates up to 500 Mbit/s.
- Latency and Reliability: Latency as low as 0.1 ms with high reliability, critical for applications requiring realtime responsiveness.
- Connection Density and Mobility: Supporting up to 10<sup>8</sup> devices per square kilometer and mobility up to 1000 km/h, accommodating high-density environments and high-speed vehicular communications.
- Spectral Efficiency and Positioning Accuracy: Enhanced spectral efficiency (up to 3x of current standards) and precise positioning accuracy (down to 1 cm).

## E. POTENTIAL TECHNOLOGIES FOR 6G

A broad spectrum of advanced technologies is necessary to fulfill 6G's requirements:

- THz Communications: To achieve extremely high data rates and bandwidth, essential for data-intensive applications.
- Ultra-Massive MIMO and Reconfigurable Intelligent Surfaces (RIS): To improve spectral efficiency and extend coverage, adapting the signal environment dynamically.
- AI/ML Integration: AI plays a crucial role in every facet of the network, from optimizing resource allocation to enhancing security and managing complex, dynamic environments.
- Non-Terrestrial Networks (NTNs): Extending network reach via satellite and airborne platforms to provide global coverage, especially in remote areas.

#### F. DEFINING FEATURES OF 6G

The essence of 6G is defined by the following key features:

- Extreme Capacity and Performance: Meeting the growing demand for data and connectivity in various contexts.
- Ultra-Flexibility and Agility: Adapting quickly to diverse environments and use cases, driven by AIenabled adaptability.
- Pervasive Intelligence and Awareness: Embedded intelligence across the network, enhancing situational awareness and decision-making.
- Sustainability and Green Networks: Focused on reducing the environmental impact of communication networks, integrating energy-efficient technologies.
- Security and Trustworthiness: Ensuring robust security frameworks to protect against emerging cyber threats, with a strong emphasis on privacy and data integrity.

These features aim to make 6G not only a technological upgrade but a pivotal societal infrastructure, enabling new possibilities for connectivity and interaction.

#### <span id="page-8-0"></span>**V. MAIN PERFORMANCE REQUIREMENTS FOR 6G**

As we look towards the development of 6G, the key performance metrics in Figure [5](#page-9-1) outlined by various standardization bodies and within the academic literature serve as a critical benchmark for understanding the capabilities and potential of the next generation of mobile networks.

As shown in Table [3,](#page-10-0) the key performance requirements for 6G, as compared to those of IMT-2020 targets, are detailed below. These requirements include both numerical values for critical parameters and qualitative capabilities that are expected to define 6G networks.

<span id="page-9-1"></span>![](_page_9_Figure_2.jpeg)

**FIGURE 5.** Key metrics of 6G.

- 1) Maximum Data Rate: For IMT-2020, this target was set at 20 Gbit/s. In the 6G literature, researchers commonly propose a target peak data rate of 1 Tbit/s, reflecting the need for ultra-high bandwidth to support data-intensive applications such as holographic communications and ultra-HD video streaming.
- 2) User Data Rate: This metric refers to the data rate that can be reliably experienced by 95% of users within a coverage area. The IMT-2020 framework set this at 100 Mbit/s. In contrast, the 6G literature suggests even higher targets, with proposed values ranging from 1 to 10 Gbit/s, to accommodate applications like real-time AI-driven services and immersive experiences that require consistent, high-speed connectivity.
- 3) Spectral Efficiency (Peak): In the 6G context, spectral efficiency may need to be doubled or tripled again to meet the demands of dense urban environments and high-frequency bands such as THz communications.
- 4) Traffic Capacity per Area: IMT-2020 set a target of 10 Mbit/s/m<sup>2</sup> . The 6G literature, however, anticipates even more demanding requirements, with values suggested in the range of 1 to 10 Gbit/s/m<sup>2</sup> . This increase is necessary to support the massive influx of connected devices in smart cities and IoT networks.
- 5) Latency: Latency is a critical factor, particularly for applications requiring real-time responsiveness. The IMT-2020 target was set at 1 ms, but 6G aims to push this further, with typical targets in the literature set at 0.1 ms, essential for enabling URLLC in autonomous systems, industrial automation, and telemedicine.
- 6) System Reliability: The IMT-2020 reliability target was 1- 10<sup>5</sup> . For IMT-2030, this has been tightened to a

- range between 1- 10<sup>5</sup> and 1- 10<sup>7</sup> . In the context of 6G, proposed reliability targets are even more stringent, with values ranging from 1- 10<sup>7</sup> to 1- 10<sup>9</sup> , which are critical for mission-critical applications.
- 7) Connection Density: IMT-2020 targeted 10<sup>6</sup> devices per km<sup>2</sup> . The 6G literature suggests that this density could be pushed even further, particularly in urban areas with dense IoT deployments, with proposed densities ranging up to 10<sup>7</sup> - 10<sup>8</sup> devices per km<sup>2</sup> . In some scenarios, a volumetric density measure of 100 devices/m<sup>3</sup> has also been considered, addressing the three-dimensional deployment of IoT devices in buildings and urban environments.
- 8) Mobility: Mobility measures the maximum speed at which devices can maintain reliable communication with the network. IMT-2020 set the maximum mobility at 500 km/h, suitable for high-speed trains. The 6G vision suggests maintaining or even exceeding this target, with the most common target value set at 1000 km/h, ensuring seamless connectivity for future high-speed transportation systems.
- 9) Accuracy of Positioning: Positioning accuracy is the precision with which the network can determine the location of a device. The 6G literature proposes even more refined targets, potentially down to millimeterlevel accuracy.

#### <span id="page-9-0"></span>**VI. AI/ML FOR 6G**

The integration of AI/ML into 6G aims to enhance the intelligence of the network, providing unprecedented levels of automation, optimization, and personalization. This section explores the role of AI/ML in 6G, introduces key AI/ML

![](_page_10_Picture_1.jpeg)

| Performance Metrics           | IMT-2020 (5G)                    | 6G                                                  |
|-------------------------------|----------------------------------|-----------------------------------------------------|
| Maximum Data Rate             | 20 Gbps                          | 1 Tbps                                              |
| User Data Rate                | 100 Mbps                         | 1/10 Gbps                                           |
| Spectral Efficiency (Peak)    | 1X                               | 2X/3X                                               |
| Traffic Capacity per Area     | 10 Mbps/m <sup>2</sup>           | 1/10 Gbps/m <sup>2</sup>                            |
| Latency                       | 1 ms                             | 0.1 ms                                              |
| System Reliability            | 1-10-5                           | 1-10 <sup>-7</sup> to 1-10 <sup>-9</sup>            |
| <b>Density of Connections</b> | 10 <sup>6</sup> /km <sup>2</sup> | 10 <sup>7</sup> to 10 <sup>8</sup> /km <sup>2</sup> |
| Maximum Mobility              | 500 km/h                         | 1000 km/h                                           |
| Accuracy of Positioning       | Not Specified                    | 0.1-10 cm                                           |

<span id="page-10-0"></span>**TABLE 3.** Comparison of key performance metrics for 6G with IMT-2020 Standards.

concepts, and discusses promising ML methods for the next generation of mobile networks. The Table [4](#page-11-0) summarizes the key AI/ML methods relevant for 6G, highlighting their vision, description, opportunities, and challenges.

<span id="page-10-1"></span>![](_page_10_Figure_5.jpeg)

**FIGURE 6.** AI/ML methods for 6G.

In the context of 6G, AI aims to infuse intelligence into the network at every level, from the core infrastructure to user-facing applications. This includes optimizing network performance, automating resource management, and enhancing user experiences across diverse applications. ML algorithms, particularly those based on data-driven approaches, are highly effective for complex tasks where traditional algorithmic solutions are insufficient. ML is crucial for realizing AI functions in 6G, supporting applications like network optimization, predictive maintenance, and adaptive resource allocation. ML's evolution from simple algorithms in the 1960s to advanced techniques like deep learning (DL) and reinforcement learning (RL) today highlights its expanding role in modern technology ecosystems.

#### *Main Types of ML Methods:*

- <span id="page-10-2"></span>• Supervised Learning: This approach is widely used in 6G for tasks like network traffic prediction, anomaly detection, and classification of communication patterns. Supervised learning [\[58\]](#page-33-5) is particularly valuable for enhancing the accuracy of network predictions and ensuring reliable service delivery.
- Unsupervised Learning: Unlike supervised learning, unsupervised learning [\[58\]](#page-33-5) deals with unlabeled data, focusing on uncovering hidden patterns or structures. This method is essential for clustering similar network behaviors, detecting outliers, and performing dimensionality reduction, which helps in compressing large datasets for more efficient processing.
- Reinforcement Learning: In 6G, RL [\[58\]](#page-33-5) is instrumental in dynamic resource allocation, power control, and routing, where the environment is continuously changing, and decisions must be made in real-time.

## <span id="page-10-3"></span>*Main Types of Training in ML:*

- Offline Learning: Offline learning [\[59\]](#page-33-6) involves training ML models on large datasets in a batch mode before deployment. This approach is effective when high computational resources are available and when the models do not need to adapt rapidly to new data. However, offline learning can be less efficient for applications requiring frequent updates, as re-training is resource-intensive.
- Online Learning: Online learning [\[59\]](#page-33-6) is an incremental process where the model is updated continuously as new data arrives. This approach is highly suitable for 6G scenarios where the network environment evolves quickly, and immediate adjustments are necessary. Online learning supports adaptive AI/ML models that can maintain high performance in dynamic conditions.

In the context of 6G, three key ML methods in Figure [6](#page-10-1) stand out due to their potential to address the unique challenges and requirements of future networks:

*Deep Learning (DL):* DL, a subfield of ML, utilizes multi-layer neural networks to extract high-level features from raw data. Its capacity to model complex patterns makes

![](_page_11_Picture_1.jpeg)

<span id="page-11-0"></span>

|  | TABLE 4. Summary of AI/ML methods for 6G. |  |  |  |
|--|-------------------------------------------|--|--|--|
|--|-------------------------------------------|--|--|--|

| ML Method | Opportunities and Challenges                                       |  |  |
|-----------|--------------------------------------------------------------------|--|--|
| DL        | Opportunities: Excellent in complex tasks. Challenges: High compu- |  |  |
|           | tational and data requirements.                                    |  |  |
| FL        | Opportunities: Enhances privacy, reduces latency. Challenges: Com- |  |  |
|           | munication overhead, scalability, asynchronous updates.            |  |  |
| TL        | Opportunities: Reduces training data and computation needs. Chal-  |  |  |
|           | lenges: Risk of negative transfer, source-target domain relevance. |  |  |

DL suitable for tasks such as network traffic prediction, signal classification, and intelligent routing in 6G. DL is particularly powerful in handling large datasets and high-dimensional data, which are common in 6G applications [\[60\],](#page-33-7) [\[61\],](#page-33-8) [\[62\],](#page-33-9) [\[63\],](#page-33-10) [\[64\],](#page-33-11) [\[65\],](#page-33-12) [\[66\],](#page-33-13) [\[67\],](#page-33-14) [\[68\]. H](#page-33-15)owever, DL's reliance on large volumes of data and intensive computation presents challenges in terms of scalability and energy efficiency.

<span id="page-11-12"></span><span id="page-11-11"></span><span id="page-11-10"></span><span id="page-11-9"></span><span id="page-11-8"></span><span id="page-11-7"></span><span id="page-11-6"></span><span id="page-11-5"></span><span id="page-11-4"></span>*Federated Learning (FL):* FL is a distributed ML approach where learning occurs across multiple decentralized devices, each contributing to the global model without sharing raw data [\[69\],](#page-33-16) [\[70\],](#page-33-17) [\[71\]. T](#page-33-18)his method enhances privacy and reduces latency, as data processing is localized. FL is promising for 6G due to its potential to enable real-time, personalized services while preserving user privacy [\[72\],](#page-33-19) [\[73\],](#page-33-20) [\[74\]. D](#page-33-21)espite its benefits, FL faces challenges such as communication overhead, asynchronous updates, and ensuring model consistency across diverse devices.

<span id="page-11-18"></span><span id="page-11-17"></span><span id="page-11-16"></span><span id="page-11-15"></span><span id="page-11-14"></span>*Transfer Learning (TL):* TL is improving learning performance on a related task by utilizing knowledge learned from one task [\[75\],](#page-33-22) [\[76\],](#page-33-23) [\[77\]. W](#page-33-24)ith 6G, TL can drastically cut down on processing resources and huge training datasets, allowing for more efficient and rapid model deployment. It comes in handy when getting new data is a hassle or costs a lot of money. Negative transfer, in which knowledge is transferred for no benefit, is still a possibility, and the efficacy of TL is conditional on the source and target domains' relevance.

The integration of AI/ML into 6G networks offers numerous opportunities:

- Enhanced Network Performance: AI/ML can optimize resource allocation, reduce latency, and improve overall network efficiency, supporting a wide range of applications from autonomous driving to smart healthcare.
- Personalization and Adaptability: AI/ML enables the network to learn user preferences and adapt services accordingly, enhancing user satisfaction and engagement.
- Automation and Self-Optimization: AI/ML facilitates automated network management, reducing the need for human intervention and enabling self-healing capabilities that enhance reliability and uptime.

However, the integration of AI/ML also presents significant challenges:

- Data Privacy and Security: The extensive use of data in AI/ML models raises concerns about privacy and security, especially as networks become more interconnected and data-driven.
- <span id="page-11-3"></span><span id="page-11-2"></span><span id="page-11-1"></span>• Scalability and Efficiency: AI/ML models, particularly those that are data-intensive like DL, require substantial computational resources, which may limit their scalability in resource-constrained environments.
- Interoperability and Standardization: Ensuring that AI/ML models work seamlessly across different network components and devices requires robust standardization and interoperability frameworks.

<span id="page-11-13"></span>AI/ML will be at the forefront of 6G, driving innovations that transform how networks operate and how users interact with technology. By leveraging the strengths of methods like DL, FL, and TL, 6G can achieve its vision of an intelligent, adaptive, and highly efficient network ecosystem.

# A. EDGE ARTIFICIAL INTELLIGENCE

The rise of AI-driven applications—such as machine learning (ML), deep learning (DL), and big data analytics—presents both opportunities and challenges. These AI systems often require significant computational resources, posing problems in terms of latency, energy consumption, network congestion, and privacy risks when centralized cloud computing models are used. This is where Edge AI emerges as a critical solution.

Edge AI decentralizes AI processes, pushing computational tasks such as AI model training and inference to the edge of the network, closer to where data is generated. This approach minimizes the need for long-distance data transmission to central servers, reducing latency and ensuring faster, more efficient network operations. The core vision of Edge AI in 6G is to enable a new type of network that seamlessly integrates sensing, communication, computation, and intelligence. Edge AI decentralizes the AI training and inference processes, allowing them to occur at the edge of the network where data is generated. This is crucial for supporting real-time applications that demand immediate responses, such as autonomous vehicles, smart cities, and industrial automation.

In the traditional AI model, data from edge devices is sent to a central server (e.g., in a cloud) for processing, which can lead to delays due to the extensive communication required. The large-scale AI models used in tasks such as image

![](_page_12_Picture_1.jpeg)

recognition or autonomous driving are resource-intensive, making centralized processing costly in terms of bandwidth and energy. Furthermore, sending sensitive data to central servers introduces privacy risks. By deploying AI capabilities directly at the edge, Edge AI reduces the amount of data that needs to be sent to central servers, lowering both latency and bandwidth requirements. This also enhances privacy, as data can be processed locally without ever leaving the device.

#### 1) EDGE LEARNING MODELS

<span id="page-12-0"></span>In the domain of Edge Artificial Intelligence (AI) for 6G networks [\[78\], e](#page-33-25)dge learning models are key enablers that ensure AI functionalities are executed efficiently and securely across distributed devices. As depicted in the figures provided, the training process at the edge involves a variety of methods, such as Federated Learning (FL), Decentralized Learning, Model Split Learning, Distributed Reinforcement Learning (RL), and Trustworthy Learning. Each of these methods serves distinct purposes, optimizing how AI models are trained and deployed at the edge, especially in resourceconstrained environments.

## *a: FEDERATED LEARNING (FL): PRIVACY-PRESERVING DISTRIBUTED TRAINING*

Federated Learning (FL) is one of the most prominent architectures in edge AI, providing a privacy-preserving framework for distributed machine learning. In this system, each device performs local training on its private data, and only model updates (e.g., gradients) are shared with a central server for aggregation. FL is ideal for applications where privacy and data security are paramount—examples include medical data analysis, financial fraud detection, and AI-powered keyboards like Google's Gboard. In Federated Learning, the flow of local model updates is aggregated into a global model by a central server. This minimizes the privacy risks associated with transmitting raw data but introduces challenges such as communication overhead and statistical heterogeneity (i.e., non-identical data across devices).

# *b: DECENTRALIZED LEARNING: PEER-TO-PEER AI*

Decentralized Learning is an environment where model updates are exchanged between devices in a peer-to-peer (P2P) fashion, without the need for a central server. Decentralized Learning is well-suited for systems where robustness, data locality, and resilience against node failures are critical, such as in autonomous driving networks or collaborative robotics. In the consensus model aggregation, devices exchange model updates and reach a global consensus without a central coordinator. This decentralized structure reduces the communication bottleneck, but it is sensitive to network topology changes and communication delays. Nevertheless, it improves system robustness against stragglers (i.e., slow devices) and poisoning attacks.

## *c: MODEL SPLIT LEARNING: COLLABORATIVE MODEL TRAINING ACROSS DEVICES*

Model Split Learning provides a way to distribute the training of large deep neural networks (DNNs) across both edge devices and edge servers. In this model, the neural network is divided into different segments, with simple segments trained on edge devices and more complex ones on edge servers. This is particularly useful for applications where computational resources are limited at the edge. The process is described by devices uploading model parameter blocks to a server, which aggregates the model parameters into a global model. The benefit of this approach is a balance between privacy and efficiency—raw data never leaves the device, while complex computations are handled by more capable servers.

# *d: DISTRIBUTED REINFORCEMENT LEARNING (RL): LEARNING IN DYNAMIC ENVIRONMENTS*

Distributed Reinforcement Learning shows an architecture designed to handle dynamic environments, where agents must make decisions based on constantly changing conditions. Distributed RL is essential in applications like autonomous vehicles, smart cities, or real-time robotics, where decisions need to be made quickly and collaboratively across multiple devices. In agents exchanging model information, learning from both their local observations and the shared knowledge of other agents. By distributing the RL process, the system becomes more resilient to changing environments and can optimize decisions through peer communication.

# *e: TRUSTWORTHY LEARNING: ENSURING SECURITY AND FAIRNESS*

As edge learning systems become more prevalent in critical applications, ensuring their trustworthiness—in terms of privacy, security, interpretability, robustness, and fairness is paramount. Trustworthy Learning describes how secure model aggregation can be achieved in federated learning, where encoded model updates are aggregated in a way that prevents adversarial attacks and data breaches. Techniques such as Byzantine-resilient secure aggregation are used to ensure that malicious devices cannot corrupt the global model by sending manipulated updates. Blockchain technology, combined with swarm learning (a fully decentralized method without a central authority), is another method to ensure that the entire system is secure from attacks.

#### 2) COMPARISON TABLE

A comparison table in Table [5](#page-13-1) outlining the key characteristics, strengths, and challenges of each training process at the edge. Federated Learning allows for the privacy-preserving training of AI models by keeping data local, while Decentralized Learning removes the need for a central authority, ensuring better data locality and network resilience. Model Split Learning enables the collaborative training of large

![](_page_13_Picture_1.jpeg)

**TABLE 5.** Comparison of Edge Learning Methods.

<span id="page-13-1"></span>

| Training Method        | Key Characteristics                 | Strengths                          | Challenges                           |
|------------------------|-------------------------------------|------------------------------------|--------------------------------------|
| Federated Learning     | - Distributed learning where local  | - Ensures privacy by keeping data  | - High communication overhead        |
|                        | models are trained on devices and   | on devices.                        | for model updates.                   |
|                        | only model updates are sent to a    | - Reduces the risk of data         | - Statistical heterogeneity of local |
|                        | central server.                     | breaches.                          | datasets affects model               |
|                        | - No raw data sharing.              | - Can scale to many devices.       | performance.                         |
|                        |                                     |                                    | - Handling system heterogeneity.     |
| Decentralized Learning | - Peer-to-peer communication        | - No reliance on a central server, | - Sensitive to network topology      |
|                        | among devices without the need      | improving robustness and           | changes.                             |
|                        | for a central server.               | resilience.                        | - Requires effective mechanisms      |
|                        | - Model updates are exchanged       | - Supports data locality.          | for consensus aggregation.           |
|                        | directly between devices.           |                                    | - Risk of slower convergence.        |
| Model Split Learning   | - Collaborative learning process    | - Reduces computation load on      | - Communication costs for            |
|                        | where a model is split between      | edge devices.                      | transferring intermediate values.    |
|                        | edge devices and servers.           | - Preserves privacy by not sharing | - Requires coordination between      |
|                        | - Different segments are trained    | raw data.                          | devices and servers for              |
|                        | across nodes.                       | - Supports large models.           | synchronization.                     |
| Distributed            | - Agents make decisions based on    | - Suitable for real-time decision  | - Requires efficient peer-to-peer    |
| Reinforcement Learning | local observations and shared       | making in dynamic environments.    | communication.                       |
|                        | knowledge.                          | - Can handle multiple agents in    | - Can suffer from non-stationary     |
|                        | - Involves learning in dynamic      | parallel tasks.                    | environments and changing agent      |
|                        | environments.                       |                                    | behaviors.                           |
| Trustworthy Learning   | - Focuses on ensuring security,     | - Protects against adversarial     | - Managing complex security          |
|                        | privacy, fairness, and robustness   | attacks.                           | protocols increases computational    |
|                        | of edge learning systems.           | - Maintains privacy through        | overhead.                            |
|                        | - Uses techniques like differential | secure aggregation.                | - Balancing privacy while            |
|                        | privacy, blockchain, and            | - Ensures fair AI models.          | maintaining learning performance     |
|                        | Byzantine-resilient aggregation.    |                                    | is challenging.                      |

AI models by distributing computation across devices and servers. Lastly, Distributed RL and Trustworthy Learning ensure that the system remains adaptive to dynamic environments and secure from malicious actors. Each of these architectures represents a different solution to the challenges faced in edge AI, providing a solid foundation for the efficient, scalable, and secure deployment of AI in the next generation of wireless networks.

#### <span id="page-13-0"></span>**VII. PROSPECTIVE TECHNOLOGIES FOR 6G EVOLUTION**

The evolution towards 6G networks demands a sophisticated and diverse set of technologies to meet the extensive and varied requirements of future communication systems. As depicted in Figure [7,](#page-14-0) the potential technologies are identified and categorized into nine technological domains that are crucial for the realization of 6G. This section will explore these technologies in detail, examining their vision, current state, opportunities, challenges, and future directions.

Table [6](#page-14-1) summarizes nine categories of potential technologies for 6G, describing key technologies within each category and their expected contributions to the 6G vision. The primary vision for 6G technologies revolves around achieving ubiquitous connectivity that is intelligent, flexible, and efficient. This entails not only higher data rates and lower latency but also the integration of advanced capabilities like sensing, AI-driven decision-making, and energy efficiency. Each technology within the 6G ecosystem is expected to contribute to these goals by addressing specific challenges and enabling new applications. The technologies identified are grouped into several categories in Figure [8,](#page-15-0) each focusing on a critical aspect of the network:

*Spectrum:* As shown in Figure [9,](#page-16-0) spectrum includes Terahertz (THz) communication and Optical Wireless Communication (OWC). THz communication promises ultra-high data rates by utilizing the high-frequency spectrum, while OWC offers an alternative for short-range, high-bandwidth communication in indoor environments.

*Antenna:* Technologies like Massive MIMO (mMIMO), Reconfigurable Intelligent Surfaces (RIS), and Holographic MIMO (HMIMO) are explored. These technologies are designed to enhance signal quality, coverage, and spectral efficiency through advanced beamforming and spatial multiplexing techniques.

*Transmission:* Covers advanced transmission techniques such as Multi-Wave, Modulation and Coding (MODCOD), Non-Orthogonal Multiple Access (NOMA), and Generalized Frequency Division Multiplexing Access (GFMA), all aimed

![](_page_14_Picture_1.jpeg)

<span id="page-14-0"></span>![](_page_14_Picture_2.jpeg)

**FIGURE 7.** Prospective technologies for 6G.

<span id="page-14-1"></span>**TABLE 6.** Summary of potential 6G technologies.

| Category       | Key Technologies and Description                                |
|----------------|-----------------------------------------------------------------|
| Chastura       | THz and OWC for ultra-high data rates and short-range commu-    |
| Spectrum       | nication.                                                       |
| Antenna        | mMIMO, RIS, and HMIMO enhance signal quality, coverage, and     |
| Antenna        | efficiency.                                                     |
| Transmission   | Multi-Wave, MODCOD, NOMA, GFMA improve spectral effi-           |
| 11 ausinission | ciency and user capacity.                                       |
| Architecture   | INTNs, UDNs, IAB, CF-mMIMO increase network capacity and        |
| Arcintecture   | reduce latency.                                                 |
| Intelligence   | AI-driven solutions at core, edge, and air layers for optimized |
| intenigence    | network operations.                                             |
| Energy-Aware   | Green Networks, RF-EH, Backscatter reduce energy consumption    |
| Energy-Aware   | and enhance sustainability.                                     |
| End-Device     | D2D, V2X, C-UAVs improve connectivity and mobility in dy-       |
| Enu-Device     | namic environments.                                             |
| Security       | Holistic security measures with AI-driven threat detection and  |
| Security       | privacy protection.                                             |
| Channel Coding | Advanced coding like Non-Binary, Fountain, Lattice Codes,       |
| Chamier County | SPARCs for improved error resilience.                           |

at improving spectral efficiency and accommodating more users within the same bandwidth.

*Architecture:* Explores novel network architectures including Integrated Terrestrial Networks (INTNs), Ultra-Dense Networks (UDNs), Integrated Access and Backhaul (IAB), and Cloud-Federated Multi-MIMO (CF-mMIMO). These architectures aim to enhance network capacity, reduce latency, and ensure seamless connectivity across heterogeneous environments.

*Intelligence:* Encompasses AI-driven network intelligence at various layers: Core, Edge, and Air Interface. These technologies are expected to automate network operations, optimize resource management, and enable real-time decision making.

*Energy-Aware:* Includes Green Networks (Green Nets), Radio Frequency Energy Harvesting (RF-EH), and Backscatter Communication, all aiming to reduce the energy consumption of 6G networks and support sustainable operations.

<span id="page-15-0"></span>![](_page_15_Figure_2.jpeg)

**FIGURE 8.** Potential technologies for 6G.

*End-Device:* Addresses the role of devices such as Deviceto-Device (D2D) communication, Vehicle-to-Everything (V2X), and Cellular Unmanned Aerial Vehicles (C-UAVs) in expanding the capabilities of 6G networks, especially in terms of mobility and connectivity in dynamic environments.

*Security:* Holistic security approaches are crucial for 6G, integrating advanced encryption, AI-driven threat detection, and privacy-preserving technologies to protect against increasingly sophisticated cyber threats.

*Channel Coding:* 6G networks are poised to deliver data rates of up to 1 Tb/s, which is a substantial leap from the capabilities of 5G, necessitating the development of advanced channel codes that not only maximize spectral efficiency but also adhere to stringent energy and latency constraints.

The future of 6G will likely involve a hybrid approach that combines multiple technologies to meet the diverse needs of different applications and environments. Research is ongoing into developing more efficient algorithms, improving the energy efficiency of communication systems, and enhancing the robustness of networks against cyber threats. Moreover, future research will focus on overcoming the current limitations of these technologies, such as the high cost and complexity of implementing THz communication, the integration of RIS into existing infrastructure, and the development of AI models that can operate effectively in real-time without compromising security or privacy. The path to 6G is paved with a wide array of innovative technologies, each contributing to the vision of a fully connected, intelligent, and sustainable communication network.

#### A. SPECTRUM ADVANCEMENTS IN 6G

To meet the rigorous performance, service, and application requirements of 6G, a wide frequency range from sub-6 GHz to THz bands will be necessary as shown in Table [7.](#page-16-1) The three primary bands considered for 6G are cmWave, mmWave, and THz. These bands are selected based on their bandwidth capacity and propagation characteristics:

#### 1) THz COMMUNICATIONS

<span id="page-15-3"></span><span id="page-15-2"></span><span id="page-15-1"></span>THz communication is anticipated to be a cornerstone for 6G networks, enabling the extreme data capacities required, with potential data rates reaching up to 1 Tb/s [\[79\],](#page-33-26) [\[80\],](#page-33-27) [\[81\].](#page-33-28) Beyond its role in traditional communication, THz technology is expected to contribute significantly to advanced applications like high-precision sensing and localization, thus broadening its utility within the 6G landscape. Operating in the 0.1 to 10 THz range, this technology leverages the abundant spectrum available to achieve extremely high data rates. However, the high propagation losses at these frequencies limit communication to shorter distances, making it ideal for data-heavy, proximity-based scenarios.

Research on THz communication gained momentum in the mid-2010s, initially overshadowed by mmWave technologies prominent in 5G development. With the shift towards 6G, THz has seen increased focus, with companies like Samsung, LG, and Nokia leading advancements in transceiver design and conducting field trials, demonstrating its practical viability. The potential of THz communication lies in its

![](_page_16_Picture_1.jpeg)

<span id="page-16-1"></span>**TABLE 7.** Summary of spectrum advancements in 6G.

| Spectrum-Level<br>Technologies | Description                                        | Opportunities               | Challenges                            |
|--------------------------------|----------------------------------------------------|-----------------------------|---------------------------------------|
| THz-C                          | Operation at 0.1-10 THz band                       | Massive spectrum            | Propagation losses,<br>HW impairments |
| OWC                            | IR 0.3-400 THz, VLC 400-750<br>THz, UV 0.75-30 PHz | Enormous spectrum, low-cost | Blocked easily, reliability issues    |

<span id="page-16-0"></span>

**FIGURE 9.** Spectrum advancements in 6G.

ability to deliver ultra-high data rates, essential for the future of connectivity. However, significant challenges persist, including high propagation losses and complex hardware impairments such as phase noise and RF non-linearity. Additionally, implementing efficient beam-forming at these frequencies remains technically demanding.

Current literature emphasizes the wide-ranging applications of THz communication, from nanoscale to space-scale environments, indicating its versatile potential. Ongoing research is directed at addressing the propagation and hardware challenges associated with this spectrum, with a focus on developing innovative solutions that can fully exploit the capabilities of THz communication for 6G and beyond [\[82\],](#page-33-29) [\[83\],](#page-33-30) [\[84\],](#page-33-31) [\[85\].](#page-33-32)

## <span id="page-16-5"></span><span id="page-16-4"></span><span id="page-16-3"></span><span id="page-16-2"></span>2) OPTICAL WIRELESS COMMUNICATIONS (OWC)

<span id="page-16-11"></span><span id="page-16-10"></span><span id="page-16-9"></span>Optical Wireless Communications (OWC) [\[86\],](#page-33-33) [\[87\],](#page-33-34) [\[88\]](#page-33-35) is envisioned as a complementary technology for 6G networks [\[89\],](#page-33-36) [\[90\],](#page-33-37) [\[91\], p](#page-33-38)articularly suited for providing access and backhaul in environments where traditional RF communication may be impractical or inefficient. OWC operates across a wide spectrum, including infrared (IR) from 0.3 to 400 THz, visible light from 400 to 750 THz, and ultraviolet (UV) from 0.75 to 30 PHz. The development of OWC dates back to the earliest experiments with visible light communication in the late 19th century. Modern iterations, particularly FSO, have shown the ability to achieve high data rates; however, their performance is often constrained by challenges like atmospheric turbulence and environmental sensitivity. OWC offers substantial bandwidth and costefficiency, making it highly suitable for high-capacity indoor applications and extensive outdoor backhaul links. Despite these advantages, the technology faces obstacles such as susceptibility to blockage, reliability concerns, and varying performance due to environmental factors.

Recent research has concentrated on enhancing the reliability of OWC systems and integrating AI and machine learning to create adaptive communication layers that respond to changing conditions. Future research directions are likely to focus on refining channel modeling, advancing device technologies, and developing hybrid OWC-RF systems to better meet the unique requirements of 6G networks [\[92\],](#page-33-39) [\[93\], e](#page-33-40)nsuring robust and versatile communication solutions.

#### <span id="page-16-14"></span><span id="page-16-13"></span><span id="page-16-12"></span>B. TRANSFORMATIVE ANTENNA SYSTEMS FOR THE 6G

As 6G technology evolves, there is a growing demand for advanced antenna systems capable of handling unprecedented data rates, connectivity, and efficiency [\[94\]. A](#page-33-41)s shown in Figure [10,](#page-17-0) technologies like Ultra-Massive MIMO, Reconfigurable Intelligent Surfaces (RIS), and Holographic MIMO (HMIMO) are poised to overcome the limitations of current wireless communication systems, enabling higher frequencies, greater bandwidths, and more efficient use of the electromagnetic spectrum.

#### <span id="page-16-8"></span><span id="page-16-7"></span><span id="page-16-6"></span>1) ULTRA-MASSIVE MIMO

<span id="page-16-17"></span><span id="page-16-16"></span><span id="page-16-15"></span>Ultra-Massive MIMO is expected to be a foundational technology for 6G, providing the framework for ultra-high data rates and extensive coverage at THz frequencies [\[95\],](#page-34-0) [\[96\],](#page-34-1) [\[97\]. B](#page-34-2)y vastly increasing the number of antennas compared to conventional MIMO systems, Ultra-Massive MIMO enhances beamforming precision, enabling highly directional and narrow beams that mitigate severe path losses typical at THz frequencies. This technology extends the concept of massive MIMO by incorporating hundreds to thousands of antennas, boosting beamforming capabilities and supporting simultaneous connections to numerous devices. This scalability makes Ultra-Massive MIMO ideal for 6G applications that require high capacity and low latency, such as smart cities and industrial IoT networks. Since its conceptualization in the early 2010s and initial deployments in 5G, research has focused on optimizing Ultra-Massive MIMO for THz communication, with recent

![](_page_17_Picture_1.jpeg)

<span id="page-17-1"></span>

|  |  |  |  | TABLE 8. Summary of antenna system technologies for 6G. |  |
|--|--|--|--|---------------------------------------------------------|--|
|--|--|--|--|---------------------------------------------------------|--|

<span id="page-17-0"></span>

| Technology    | Opportunities                                  | Challenges                                    |
|---------------|------------------------------------------------|-----------------------------------------------|
| Ultra-Massive | High beamforming gains, increased spectral     | Cost-effective design, complex beamforming,   |
| MIMO          | efficiency, supports dense environments        | beam misalignment, scalability.               |
| RIS           | Enhances signal quality, reduces interference, | Real-time control, scalability, integration   |
| KIS           | extends coverage with energy efficiency.       | with existing networks, optimal tuning        |
| HMIMO         | Near-ideal MIMO performance, high spatial      | Developing suitable channel models, efficient |
| THVIIIVIO     | multiplexing, efficient beamforming            | beam focusing, alignment, mobility support.   |

![](_page_17_Figure_4.jpeg)

<span id="page-17-2"></span>**FIGURE 10.** Antenna system technologies for 6G.

studies exploring advanced beamforming techniques to address propagation challenges [\[98\].](#page-34-3)

Ultra-Massive MIMO offers significant opportunities, including enhanced spectral efficiency, substantial gains in beamforming, and extensive spatial multiplexing. However, it also faces challenges, such as designing cost-effective and energy-efficient antenna arrays, managing the increased computational complexity of beamforming, and addressing issues like beam misalignment and mobility support. Integrating AI-driven algorithms for adaptive beam management is expected to play a crucial role in optimizing Ultra-Massive MIMO performance. Future research will focus on refining beamforming architectures and exploring their trade-offs in cost, complexity, and performance, with an emphasis on scalability for diverse 6G applications, such as UAV communications and integrated terrestrial and non-terrestrial networks.

#### 2) RECONFIGURABLE INTELLIGENT SURFACES (RIS)

RIS technology aims to revolutionize wireless communication by actively controlling the propagation environment through programmable meta surfaces [\[99\],](#page-34-4) [\[100\],](#page-34-5) [\[101\].](#page-34-6) RIS enables the manipulation of electromagnetic waves, dynamically adjusting their properties to enhance signal strength, reduce interference, and extend coverage. This is particularly valuable in environments with high blockage or interference, such as urban canyons and indoor scenarios where traditional communication methods struggle.

Since gaining traction in the late 2010s, RIS technology has evolved from passive reflect arrays to include active and hybrid RIS, which incorporate minimal active components for greater flexibility and control. Despite its potential, RIS faces challenges in real-time control, scalability, and integration with existing network protocols. Ongoing research focuses on developing advanced control algorithms, including AI and machine learning, to autonomously adapt surface parameters in real-time. Future work will explore the use of RIS in conjunction with other technologies, such as Ultra-Massive MIMO and HMIMO, to create adaptable and resilient communication networks, with particular interest in scaling RIS for larger surfaces and high-mobility scenarios like vehicular communications.

# 3) HOLOGRAPHIC MIMO (HMIMO)

<span id="page-17-9"></span><span id="page-17-8"></span><span id="page-17-7"></span><span id="page-17-6"></span><span id="page-17-5"></span><span id="page-17-4"></span><span id="page-17-3"></span>HMIMO pushes beyond conventional and even Ultra-Massive MIMO by using electromagnetically active surfaces that can transmit, receive, or reflect communication signals with extreme precision [\[102\],](#page-34-7) [\[103\],](#page-34-8) [\[104\],](#page-34-9) [\[105\].](#page-34-10) HMIMO

<span id="page-18-0"></span>![](_page_18_Picture_1.jpeg)

aims to achieve very high spatial multiplexing gains by employing surfaces that function as an infinite array of antennas, offering unprecedented control over the communication environment. Unlike traditional antenna arrays, HMIMO surfaces consist of dense, contiguous arrays of sub-wavelength elements that manipulate electromagnetic fields with high fidelity, treating the entire surface as a single continuous aperture capable of complex wave manipulations. This allows HMIMO to realize beamforming, beamsteering, and multiplexing with unparalleled efficiency, making it suitable for highly dynamic and dense 6G networks.

Since its inception in the late 2010s, HMIMO has evolved rapidly from theoretical models and small-scale prototypes to potential applications that offer comparable performance to large antenna arrays but with reduced size and power requirements. However, challenges remain in developing suitable channel models for the unique properties of HMIMO, such as near-field propagation and managing contiguous active surfaces. Efficient algorithms for beam focusing, alignment, and mobility support are essential to unlock HMIMO's full potential in practical scenarios. Future research will focus on overcoming these challenges, exploring hybrid active-passive surface configurations, and integrating HMIMO into the broader 6G ecosystem, potentially as part of a multi-tiered approach combining Ultra-Massive MIMO, RIS, and other advanced antenna technologies.

Overall, these advanced antenna technologies hold transformative potential for the future of 6G networks, offering unique contributions, addressing ongoing challenges, and opening new avenues for research as shown in Table [8.](#page-17-1) They are set to play a pivotal role in the 6G landscape, shaping the evolution of wireless communication systems.

# C. PIONEERING TRANSMISSION SCHEMES FOR 6G

As 6G technology evolves, the development of advanced transmission schemes as shown in Figure [11](#page-19-0) is vital for optimizing spectral resource utilization and accommodating the diverse requirements of future communication scenarios. These innovative technologies are crucial in transforming the extensive spectrum range into high-performance communication systems capable of meeting stringent demands and supporting a wide array of use cases.

#### 1) MULTI-WAVEFORM SCHEME

Multi-waveform schemes are envisioned to provide a highly adaptable air interface for 6G, enabling efficient operation across a broad spectrum from sub-6 GHz to THz frequencies. These schemes allow for the simultaneous use of different waveforms, each tailored to specific transmission environments, which enables 6G networks to dynamically adjust to changing channel conditions and application demands. This adaptability optimizes performance across diverse scenarios and is supported by multi-numerology, a key component that uses multiple sets of waveform parameters to cater to different transmission settings, thereby enhancing the network's flexibility.

The concept of multi-waveform schemes originated in 4G, which used different waveforms for downlink (CP-OFDM) and uplink (DFT-s-OFDM). In 5G, this approach evolved with the introduction of flexible CP-OFDM variants that improved resilience against hardware impairments and reduced latency at higher frequencies [\[106\].](#page-34-11) As 6G aims to expand beyond traditional communication functions, ongoing research is exploring enhanced OFDM-based schemes and other complementary waveforms to address the broader spectrum and diverse application needs of the next generation [\[107\].](#page-34-12)

<span id="page-18-1"></span>The main advantage of multi-waveform schemes lies in their ability to provide a customizable framework that maximizes the spectral capabilities of 6G. However, selecting the appropriate waveforms and configuring their parameters for specific scenarios remains a complex challenge. Current research efforts are focused on developing adaptive algorithms and hybrid waveform strategies to strike an optimal balance between performance and system complexity. Looking ahead, future research is expected to continue exploring waveform designs that integrate communication and sensing functions, with a strong emphasis on scalability and adaptability across various 6G scenarios. Additionally, there is growing interest in leveraging machine learning to automate the selection and configuration of waveforms, which could significantly enhance the operational efficiency of 6G networks.

#### 2) ADVANCED MODULATION AND CODING METHODS

<span id="page-18-2"></span>These methods are critical in achieving the high performance required by the 6G physical layer, particularly in maximizing throughput and ensuring reliability. These fundamental processes convert digital bits into transmission symbols and maintain data integrity across wireless links. For 6G, modulation and coding methods need to evolve to support ultra-high data rates for applications involving URLLC [\[108\].](#page-34-13) Each generation of mobile communication has introduced new or enhanced modulation and coding schemes; for instance, 5G utilized higher-order QAM and LDPC codes to improve spectral efficiency and error correction [\[109\].](#page-34-14) As 6G aims for even higher data rates and reliability, further advancements in modulation complexity and error-correcting capabilities are anticipated.

<span id="page-18-3"></span>The primary opportunity lies in achieving a balance between modulation order, coding rate, and performance metrics such as data rate and error resilience. However, as modulation orders increase, challenges like power amplifier efficiency and hardware limitations become more significant. Addressing these challenges will require innovative solutions, such as coded modulation with probabilistic shaping and novel channel coding schemes tailored to the 6G environment. Future research is expected to focus on optimizing modulation schemes for the expansive frequency ranges of 6G, including THz communications. Additionally, developing new coding techniques that effectively manage

![](_page_19_Picture_1.jpeg)

| Technology                     | Opportunities                             | Challenge                                             |  |
|--------------------------------|-------------------------------------------|-------------------------------------------------------|--|
| Multi-Waveform Scheme          | Supports a wide spectrum range and        | Requires selecting suitable waveforms and             |  |
| Wuiti-waverorm Scheme          | adapts to diverse conditions              | managing configuration complexity                     |  |
| Advanced Modulation and Coding | Offers high throughput, reliability, and  | Challenges include managing high-order modulation and |  |
| Advanced Modulation and Coding | adaptability to various channels          | coding under latency constraints                      |  |
| NOMA                           | Enhances spectral efficiency and is ideal | Complexity in receiver design and effective           |  |
| NOMA                           | for massive IoT communications            | interference management are key issues                |  |
|                                | Provides fast efficient access with       | Handling preamble collisions and adapting             |  |

<span id="page-19-1"></span>**TABLE 9.** Summary of transmission scheme technologies for 6G.

<span id="page-19-0"></span>![](_page_19_Figure_4.jpeg)

**FIGURE 11.** Transmission scheme technologies for 6G.

high error rates and latency demands will be essential, with potential advancements involving AI-driven error correction strategies to further enhance the performance of 6G networks.

#### 3) NON-ORTHOGONAL MULTIPLE ACCESS (NOMA)

It is seen as a promising solution for enhancing spectral efficiency and system capacity in 6G, especially in scenarios involving massive IoT connectivity [\[110\],](#page-34-15) [\[111\],](#page-34-16) [\[112\].](#page-34-17) NOMA enables multiple users to share the same frequency resources by separating them in the power or code domain, which improves overall system throughput and fairness compared to traditional orthogonal access methods. This approach is particularly beneficial for managing the dense connectivity demands expected in 6G networks. Although NOMA was explored as a potential technology for 5G, its full potential is anticipated to be realized in 6G, where it can be integrated with advanced access techniques like grant-free communication. Despite its promise, NOMA faces significant challenges, including interference management and the complexity of receiver design.

The main advantage of NOMA lies in its ability to efficiently serve multiple devices simultaneously, making it well-suited for the diverse connectivity requirements of 6G. However, scaling NOMA requires overcoming challenges related to receiver complexity and developing effective interference cancellation algorithms. Current research is focused on refining NOMA methods to strike a balance between performance and system complexity in various 6G scenarios. Future studies are expected to explore hybrid NOMA schemes and their integration with other 6G technologies, such as Reconfigurable Intelligent Surfaces (RIS) and AI-enhanced control systems, to further improve system performance in highly dynamic and dense network environments.

# <span id="page-19-4"></span><span id="page-19-3"></span><span id="page-19-2"></span>4) GRANT-FREE MEDIUM ACCESS

<span id="page-19-5"></span>Grant-free access is expected to be a key component for efficient network operation in 6G, especially for ultra-massive IoT applications. Unlike conventional access methods that require permission from the base station, grant-free access allows devices to transmit data immediately, thereby reducing latency and signaling overhead [\[113\].](#page-34-18) This approach is particularly suited for scenarios involving sporadic, lowvolume transmissions, which are common in IoT applications. The concept of grant-free access gained traction with the emergence of massive machine-type communications (mMTC) in 4G and 5G. As 6G aims to further reduce access latency and enhance connectivity, there is a need to

<span id="page-20-2"></span>![](_page_20_Picture_1.jpeg)

improve grant-free protocols to support the increased scale and diversity of connected devices [\[114\].](#page-34-19)

Grant-free access offers significant benefits, such as reduced latency and improved energy efficiency. However, it also presents challenges, including preamble collisions and the complexities of managing massive connectivity in 6G environments. Addressing these challenges requires advanced collision avoidance strategies and the use of AI/ML techniques for dynamic traffic prediction. Future research is likely to focus on integrating grant-free access with other advanced 6G technologies, such as NOMA, cell-free massive MIMO, and AI-enhanced network control. These integrations could lead to highly efficient access mechanisms that meet the stringent demands of 6G networks, providing robust solutions for managing the anticipated growth in connected devices and diverse communication scenarios.

This comprehensive examination of transmission scheme technologies as shown in Table [9](#page-19-1) underscores their pivotal role in shaping 6G capabilities, highlighting their potential to address the evolving demands of next-generation communication networks.

## D. ADVANCING CONNECTIVITY THROUGH 6G NETWORK ARCHITECTURES

As 6G networks continue to evolve, they are set to introduce complex and innovative architectures as shown in Figure [12](#page-20-0) that will significantly enhance connectivity, capacity, and quality of service. Below, advanced architectures stand out as key enablers of 6G's potential.

<span id="page-20-0"></span>![](_page_20_Figure_7.jpeg)

**FIGURE 12.** Network architectural technologies for 6G.

## 1) INTEGRATED NON TERRESTRIAL AND TERRESTRIAL NETWORKS (INTNs)

INTNs are expected to play a crucial role in 6G by providing seamless global connectivity across terrestrial, airborne, and <span id="page-20-1"></span>space layers, supporting applications. INTNs utilize a layered approach, integrating ground-based networks with airborne platforms like drones and airships, and spaceborne satellites positioned in various orbits to ensure extensive global coverage. This architecture, collectively known as space air ground integrated networks (SAGIN) [\[115\],](#page-34-20) builds on the evolution of satellite communications, which have been in use since the 1960s, and more recent advancements involving UAVs and High Altitude Platform Stations (HAPS). In 5G, initial steps were taken to integrate non-terrestrial networks, particularly satellites, with terrestrial mobile networks, and 6G will further enhance this integration to offer more robust and scalable connectivity solutions.

INTNs provide significant opportunities for extending coverage and supporting new applications across diverse environments. However, they also pose challenges, such as the complexity of integrating different network layers, managing regulatory issues for global operations, and developing realistic channel models for accurate performance evaluation. Current research on INTNs focuses on expanding their capabilities through technologies like multi-access edge computing, AI/ML for resource management, and advanced network slicing techniques. Future efforts will aim to refine the synergy between terrestrial and non-terrestrial layers, addressing integration challenges to fully meet the specific requirements of 6G networks [\[116\],](#page-34-21) [\[117\],](#page-34-22) [\[118\],](#page-34-23) [\[119\],](#page-34-24) [\[120\].](#page-34-25)

# <span id="page-20-7"></span><span id="page-20-6"></span><span id="page-20-5"></span><span id="page-20-4"></span><span id="page-20-3"></span>2) ULTRA-DENSE NETWORKS (UDNs)

<span id="page-20-11"></span><span id="page-20-10"></span><span id="page-20-9"></span><span id="page-20-8"></span>UDNs are envisioned to meet the extreme capacity demands of 6G by deploying a highly dense network of small cells, access points, and IoT sensors, particularly utilizing the THz frequency spectrum for enhanced performance [\[121\],](#page-34-26) [\[122\],](#page-34-27) [\[123\],](#page-34-28) [\[124\].](#page-34-29) This approach represents a significant shift towards densely packed deployments, where network nodes are brought closer to end-users, effectively increasing network capacity, reducing latency, and improving overall efficiency. The evolution of network densification has been a steady trend from 1G to 5G, moving from primarily macro cells to a combination of macro and small cells in 5G. In 6G, UDNs will further this trend by supporting high-frequency THz communications and integrating various access technologies, including IoT and vehicular networks.

The primary advantage of UDNs lies in their ability to deliver ultra-high data rates and low latency in densely populated areas. However, this density also introduces challenges such as managing interference among closely spaced nodes, optimizing resource allocation, and handling the increased complexity of mobility management. Current research focuses on developing interference mitigation strategies, AI-driven resource management, and dynamic user clustering to improve the efficiency of dense deployments. Future research directions include exploring the integration of UDNs with other 6G technologies, such as Integrated Access and Backhaul (IAB) and cell-free architectures, to further

![](_page_21_Picture_1.jpeg)

<span id="page-21-0"></span>

|  |  | TABLE 10. Architectural advancements in 6G networks. |  |  |
|--|--|------------------------------------------------------|--|--|
|--|--|------------------------------------------------------|--|--|

| Technology | Opportunities                                         | Challenges                                           |  |  |
|------------|-------------------------------------------------------|------------------------------------------------------|--|--|
| INTNs      | Provides global coverage, supporting diverse appli-   | Faces cost efficiency issues, regulatory challenges, |  |  |
|            | cations.                                              | and performance evaluation difficulties.             |  |  |
| UDNs       | Offers extreme capacity, enhanced connectivity, and   | Challenges include interference management, mobil-   |  |  |
|            | reduced latency.                                      | ity support, and resource management.                |  |  |
| IAB        | Enables faster, cost-effective deployment with flexi- | Interference between access and backhaul and re-     |  |  |
|            | ble network design.                                   | source allocation are key challenges.                |  |  |
| CM MIMO    | Delivers stable QoS, improved signal quality, and     | Synchronization, interference management, and        |  |  |
|            | scalability.                                          | practical implementation are challenging.            |  |  |

enhance network performance and address the challenges associated with ultra-dense deployments.

#### 3) INTEGRATED ACCESS AND BACKHAUL (IAB)

IAB aims to simplify the deployment of ultra-dense networks in 6G by utilizing the same spectrum resources for both access and backhaul, providing a cost-effective and flexible alternative to traditional fiber links [\[125\],](#page-34-30) [\[126\],](#page-34-31) [\[127\].](#page-34-32) IAB leverages existing wireless infrastructure to handle backhaul connectivity, significantly reducing the need for dedicated wired backhaul. This makes IAB especially advantageous for rapid deployment in dense urban environments, where traditional backhaul solutions can be prohibitively expensive and time-consuming. Originally introduced in 4G as part of the LTE relay concept, IAB gained prominence in 5G with its standardization as a solution for mmWave networks. For 6G, the focus will shift towards enhancing IAB to operate efficiently at THz frequencies, supporting even denser network configurations [\[128\].](#page-34-33)

IAB offers several key benefits, including reduced deployment costs and increased flexibility in network design. However, it also presents challenges, such as managing interference between access and backhaul links and optimizing resource allocation to ensure smooth network performance. To address these challenges, current research is exploring AI/ML-based solutions for dynamic resource allocation and effective interference management in IAB networks. Future research will likely focus on integrating IAB with other advanced 6G technologies, such as Reconfigurable Intelligent Surfaces (RIS) and optical wireless communication, to further improve overall network efficiency and performance in ultra-dense deployments.

## 4) CELL-FREE MASSIVE MIMO

It is envisioned as a transformative technology for 6G, designed to provide uniform service quality across the entire network by eliminating the boundaries of traditional cell-based architectures. This approach involves deploying numerous distributed access points that work cooperatively to serve users, rather than relying on a small number of centralized base stations. By doing so, cell-free massive MIMO reduces interference, enhances signal quality, and ensures a consistent user experience throughout the coverage <span id="page-21-7"></span><span id="page-21-6"></span><span id="page-21-5"></span>area [\[129\],](#page-34-34) [\[130\],](#page-34-35) [\[131\].](#page-34-36) The concept was first proposed in 2015 as a solution to the limitations of conventional massive MIMO systems, and research has since expanded to address dynamic user-centric clustering, synchronization strategies, and scalability improvements.

<span id="page-21-9"></span><span id="page-21-8"></span><span id="page-21-3"></span><span id="page-21-2"></span><span id="page-21-1"></span>Cell-free massive MIMO offers significant potential for enhancing network performance, including improved capacity and energy efficiency [\[132\],](#page-34-37) [\[133\].](#page-34-38) However, it also faces challenges such as synchronization, scalable network management, and the integration of distributed processing across a large number of access points. Ongoing research is focused on practical implementations, with an emphasis on validating and optimizing the technology in real-world scenarios. Future studies are expected to explore the integration of cell-free massive MIMO with other 6G technologies, such as AI/ML for real-time network optimization, and to investigate its role in emerging applications like industrial IoT and ultra-reliable low-latency communications [\[134\],](#page-34-39) [\[135\],](#page-34-40) [\[136\].](#page-35-0)

<span id="page-21-12"></span><span id="page-21-11"></span><span id="page-21-10"></span><span id="page-21-4"></span>The Table [10](#page-21-0) outlines the key network architectural technologies anticipated for 6G networks, detailing their core features, benefits, and potential applications.

#### E. ENABLING INTELLIGENT 6G NETWORKS WITH AI

Network intelligence technologies are expected to transform 6G networks by integrating AI and ML at multiple layers, including the core, edge, and air interface as shown in Figure [13,](#page-22-0) thereby enhancing the design, operation, and management of these networks. AI/ML will make 6G networks more intelligent, efficient, scalable, and secure, pushing them beyond the capabilities of current 5G systems [\[137\],](#page-35-1) [\[138\],](#page-35-2) [\[139\].](#page-35-3)

## <span id="page-21-15"></span><span id="page-21-14"></span><span id="page-21-13"></span>1) THE INTELLIGENT CORE

<span id="page-21-17"></span><span id="page-21-16"></span>In 6G, the core network is set to evolve beyond the software-defined and cloud-native architecture of 5G by incorporating pervasive AI/ML, marking a shift from traditional cloud intelligence to a more advanced AI-empowered core [\[140\],](#page-35-4) [\[141\].](#page-35-5) This enhancement aims to elevate network capabilities by making the core network more adaptive and resilient to fluctuating demands and conditions. The core network in mobile communications plays a crucial role in overall network operation, management, and security, acting as the coordinator between the Radio Access Network

![](_page_22_Picture_1.jpeg)

<span id="page-22-1"></span>**TABLE 11.** Intelligent networks for 6G.

| Network Intelligence<br>Technologies | Description    | Opportunities      | Challenges               |
|--------------------------------------|----------------|--------------------|--------------------------|
| Intelligent Core                     | AI-enhanced    | Enhanced network   | End-to-end optimization, |
| Intelligent Core                     | core network   | management         | cloud-edge cooperation   |
|                                      | AI-enhanced    | Enhanced edge      | Infrastructure,          |
| Intelligent Edge                     |                |                    | AI algorithms,           |
|                                      | edge computing | management         | data acquisition         |
| Intelligent Air                      | AI-enhanced    | Enhanced PHY/MAC   | Fast-changing            |
| Interface                            | air interface  | Ellianced FH 17WAC | channel conditions       |

<span id="page-22-0"></span>![](_page_22_Picture_4.jpeg)

**FIGURE 13.** Network intelligence technologies for 6G.

(RAN) and mobile devices. In 6G, the intelligent core will extensively leverage AI/ML to optimize various network functions, including resource allocation, traffic management, and security. By utilizing large datasets, AI/ML can significantly improve the core network's performance, enabling it to adapt swiftly to changes in demand and network conditions.

The evolution of core networks has progressed steadily through generations, from the circuit-switched systems of 2G to the service-based, cloud-native core of 5G. The 5G core introduced key advancements such as Service-Based Architecture (SBA), Software-Defined Networking (SDN), and Network Function Virtualization (NFV), laying the groundwork for the intelligent core of 6G. The integration of AI/ML into the 6G core is expected to address the growing complexity and demands of future networks. This integration offers numerous opportunities, including enhanced operational efficiency, improved network security, and optimized resource management. However, it also poses challenges, such as the need for robust data acquisition and processing frameworks and the development of effective AI/ML algorithms that can seamlessly operate across the core-to-edge continuum. Ensuring effective collaboration between AI-enhanced core networks and other network layers remains a critical area of ongoing research.

Current literature highlights the increasing role of AI/ML in core networks, with a focus on optimization strategies, resource management, and security enhancements. Future research is anticipated to delve deeper into the integration of AI/ML across all network layers, prioritizing the development of standardized frameworks for implementing AI-driven solutions that can adapt in real-time to evolving network conditions.

#### 2) THE INTELLIGENT EDGE

<span id="page-22-3"></span><span id="page-22-2"></span>The intelligent edge, which combines edge computing with AI, is expected to play a crucial role in 6G by providing lowlatency, high-efficiency processing closer to end users [\[78\],](#page-33-25) [\[142\],](#page-35-6) [\[143\].](#page-35-7) This approach aims to reduce the computational burden on the core network while supporting a wide range

![](_page_23_Picture_1.jpeg)

of applications, from IoT devices to real-time analytics. By shifting computation closer to data sources like IoT devices and edge servers, edge computing reduces latency and communication overhead, thereby enhancing the user experience. Integrating AI/ML at the edge enables local optimization of processing tasks, from basic data filtering to complex decision making, facilitating faster responses and more adaptive services. This decentralized approach is essential for managing the diverse and dynamic demands of 6G services.

Although the integration of edge computing and AI is a relatively recent development, it has rapidly gained momentum since its emergence in the 2010s, fueled by advancements in cloud computing and AI technologies. Edge intelligence has evolved into a critical enabler in 5G and is anticipated to be a foundational element of 6G architectures. The combination of edge computing with AI/ML offers substantial benefits, including reduced latency, enhanced data privacy, and improved energy efficiency. However, challenges persist in integrating these technologies across heterogeneous devices, managing data privacy and security concerns, and ensuring efficient resource allocation. AI/ML models designed for edge environments must be highly optimized to function within the constraints of limited computational power and storage capacity typical of edge devices.

Research in intelligent edge computing is expanding, with significant focus on developing AI/ML algorithms specifically tailored for edge devices, improving interactions between the edge and cloud, and establishing standards for AI-enabled edge processing. Future research directions include the deployment of federated learning and other collaborative AI strategies that distribute learning processes across multiple edge nodes, thereby enhancing the resilience, scalability, and overall performance of edge intelligence in 6G networks.

#### 3) THE INTELLIGENT AIR INTERFACE

<span id="page-23-2"></span><span id="page-23-1"></span><span id="page-23-0"></span>AI/ML-enhanced air interfaces are poised to revolutionize the PHY and MAC layers of 6G networks by enabling adaptive, context-aware communication strategies that can dynamically respond to environmental conditions and user demands [\[144\],](#page-35-8) [\[145\],](#page-35-9) [\[146\].](#page-35-10) The air interface plays a crucial role in managing radio communications between devices and the network, handling processes such as channel estimation, symbol demapping, and interference management. Integrating AI/ML into these processes allows for the development of adaptive, learning-based solutions that can replace traditional, inflexible algorithms. This represents a significant paradigm shift, where AI not only designs but also optimizes the entire air interface, potentially simplifying standardization while enhancing overall performance.

Since the mid-2010s, AI/ML has been incrementally integrated into the air interface, initially focusing on optimizing the PHY layer in 5G. As we move towards 6G, this integration is expected to deepen, with AI/ML playing a more central role in the design of both PHY and MAC layers. The application of AI/ML extends from enhancing individual processing blocks to fully automating the air interface's operations, marking a transformative step in network design.

The primary opportunities of AI/ML-enhanced air interfaces include improvements in efficiency, reduced latency, and enhanced spectral and energy performance. However, implementing AI/ML at this level presents several challenges, such as managing the wide variability of wireless environments, handling real-time data collection and model training, and meeting the complex QoS requirements specific to 6G. Effective integration requires robust and flexible AI models capable of adapting to rapidly changing network conditions.

Current literature shows increasing interest in leveraging AI/ML for air interface design, with many studies focusing on deep learning techniques for PHY layer tasks and reinforcement learning for addressing MAC layer challenges. Future research will likely delve into developing AI-native air interfaces that fully exploit AI/ML capabilities for optimized communication protocols, adaptive resource management, and seamless integration with other AI-enhanced components of 6G networks.

As shown in the Table [11,](#page-22-1) overall, AI/ML integration across these network layers promises to make 6G networks smarter and more responsive, but also requires significant research and development to address the technical challenges associated with pervasive AI/ML deployment. The future of 6G networks will depend on the successful implementation of AI/ML across the core, edge, and air interface, leading to a more intelligent, flexible, and capable communication system that meets the needs of next-generation applications.

# F. SUSTAINABLE AND ENERGY-EFFICIENT 6G NETWORKS

As global data consumption and the number of connected devices continue to rise, the energy demands of mobile networks are also increasing, making energy efficiency a critical consideration for the development of 6G networks. To address these challenges, 6G is expected to incorporate advanced energy-aware technologies, including green networks, energy harvesting (EH), and backscatter communications, as shown in Figure [14.](#page-24-0)

# 1) GREEN NETWORKS

These networks aim to minimize the energy overhead of mobile communications by implementing energy-efficient design principles across all components, including network infrastructure, communication protocols, and devices. The primary objective is to alleviate the negative environmental impact associated with the increasing energy demands of mobile networks. This goal is achieved through strategies such as powering down underutilized network elements, enabling virtual resource sharing among operators, and optimizing network management to conserve energy. Green networks present significant opportunities to reduce operational costs and environmental impact. However, the main

<span id="page-24-8"></span><span id="page-24-7"></span><span id="page-24-6"></span>![](_page_24_Picture_1.jpeg)

<span id="page-24-1"></span>**TABLE 12.** Summary of energy-aware technologies for 6G.

| Technology                        | Opportunities                             | Challenges & Future Directions                      |  |
|-----------------------------------|-------------------------------------------|-----------------------------------------------------|--|
| Green Networks                    | Reduces operational costs and environmen- | Balancing energy savings with performance; integra- |  |
|                                   | tal impact.                               | tion with 6G using AI for optimization.             |  |
| Energy Harvesting (EH)            | Powers IoT devices using renewable energy | Efficient energy conversion and storage; developing |  |
|                                   | sources.                                  | advanced EH systems and integrating with 6G.        |  |
| <b>Backscatter Communications</b> | Supports ultra-low-power communication    | Limited range and data rates; integration with      |  |
|                                   | for IoT devices.                          | MIMO, AI, and advanced modulation techniques.       |  |

<span id="page-24-0"></span>![](_page_24_Picture_4.jpeg)

**FIGURE 14.** Energy-aware technologies for 6G.

challenge lies in substantially cutting the overall energy consumption of mobile networks while maintaining high performance and reliability. The complexity of modern mobile networks, which must support a wide variety of services and devices, complicates the implementation of energy-efficient solutions on a large scale. Moreover, designing and managing green networks necessitates advanced AI/ML techniques for real-time optimization of resource allocation and network operations to ensure energy savings without compromising service quality. Recent studies have investigated various approaches to green communication, including AI-based models for network optimization, energy-efficient PHY layer designs, and sustainable 6G network architectures. Future research will likely focus on integrating green networks with other 6G technologies, such as massive MIMO, ultralean carrier design, and intelligent resource management, to develop comprehensive energy-aware communication systems [\[147\],](#page-35-11) [\[148\],](#page-35-12) [\[149\],](#page-35-13) [\[150\].](#page-35-14)

# <span id="page-24-4"></span><span id="page-24-3"></span><span id="page-24-2"></span>2) ENERGY HARVESTING

Energy harvesting is envisioned as a crucial technology for fostering sustainable, low-power, and autonomous IoT networks in 6G, enabling devices to operate without depen<span id="page-24-9"></span>dence on conventional power sources [\[151\],](#page-35-15) [\[152\],](#page-35-16) [\[153\],](#page-35-17) [\[154\].](#page-35-18) Energy harvesting offers significant opportunities for enhancing the sustainability of mobile networks by facilitating the deployment of lightweight, low-power IoT devices that do not rely on traditional energy sources. However, it also presents challenges, such as the efficient conversion and storage of harvested energy, the variability of available energy sources, and the limited power that can be extracted from ambient conditions. Overcoming these challenges necessitates advancements in antenna and circuit design, as well as the development of more effective energy conversion technologies.

Current research on RF energy harvesting has primarily focused on its application within IoT networks, with recent studies exploring the use of metasurfaces and advanced materials to boost energy collection efficiency. Looking ahead, future research directions include the development of both centralized and decentralized energy harvesting architectures, optimizing the placement of energy sources, and integrating energy harvesting with other 6G technologies to create self-sustaining networks that are capable of supporting the diverse needs of next-generation communication systems.

## 3) BACKSCATTER COMMUNICATION

This technology works by reflecting and modulating incoming RF signals to transmit data, thereby eliminating the need for a dedicated power source. This approach allows low-complexity transmitters to communicate with minimal power consumption, making it ideal for battery-free IoT applications. Backscatter communication systems are typically categorized into three main types: monostatic, bistatic, and ambient backscatter, each offering distinct advantages and facing specific challenges [\[155\],](#page-35-19) [\[156\],](#page-35-20) [\[157\].](#page-35-21)

<span id="page-24-12"></span><span id="page-24-11"></span><span id="page-24-10"></span><span id="page-24-5"></span>The key opportunities presented by backscatter communication include significantly reducing the energy requirements of IoT networks and supporting the deployment of ultra-lowpower devices in energy-constrained environments. However, this technology also faces challenges, such as limited communication range, low data rates, and the lack of quality of service (QoS) guarantees due to dependence on ambient RF sources. Addressing these issues will require advancements in modulation techniques, channel modeling, and the development of robust security measures to ensure reliable and secure communication.

![](_page_25_Picture_1.jpeg)

Recent research has focused on improving the performance of backscatter systems by integrating them with emerging technologies like MIMO, NOMA, and AI/ML. Future studies are expected to explore the application of backscatter communication in a variety of scenarios, including smart homes, healthcare, environmental monitoring, and logistics [\[158\].](#page-35-22) Moreover, the development of advanced signal processing techniques and hybrid systems that combine backscatter with other wireless communication methods will be essential to fully harness the potential of this technology in 6G networks.

Table [12](#page-24-1) provides a comprehensive summary of the key energy-aware technologies for 6G networks.

## G. DEVICE-CENTRIC COMMUNICATION INNOVATIONS IN 6G NETWORKS

The evolution of 6G networks is poised to accommodate a vast number of wireless devices, vehicles, and drones, necessitating diverse communication requirements and introducing new paradigms in mobile connectivity. Among these emerging technologies, Device-to-Device (D2D) communication, Vehicle-to-Everything (V2X) communication, and cellular-connected Unmanned Aerial Vehicle (UAV) communications, as shown in Figure [15,](#page-26-0) will play pivotal roles in the 6G landscape.

## 1) D2D COMMUNICATIONS

D2D communications in 6G are anticipated to provide comprehensive support across various environments, including cellular, industrial, vehicular, and aerial settings, by enabling direct communication between nearby devices without relying on a base station (BS) [\[159\],](#page-35-23) [\[160\],](#page-35-24) [\[161\].](#page-35-25) This direct communication can occur in two primary modes: in-band, where the same spectrum as the cellular network is utilized (either in underlay or overlay configurations), and outband, where separate spectra are used, allowing for either autonomous or BS-controlled operations. By offloading data traffic, improving spectral efficiency, reducing latency, and ensuring reliable communication links, D2D communications significantly enhance network performance, which is particularly important for applications such as mobile traffic offloading, public safety, and proximity-based services.

D2D communications offer significant opportunities for enhancing network efficiency, extending coverage, and providing critical support in scenarios such as emergency communications. The integration of D2D within cellular networks adds layers of complexity, necessitating sophisticated strategies for managing interference and strong security protocols to address the potential risks associated with direct communication.

Current literature on D2D communication delves into various topics, including device discovery, interference management, resource allocation, and security issues [\[162\].](#page-35-26) As 6G continues to develop, future research is expected to focus on improving D2D capabilities through AI/ML-based solutions for dynamic resource management and expanding D2D applications to include advanced use cases such as THz and VLC D2D, V2X scenarios, and UAV networks. Integrating D2D with emerging 6G technologies like RIS, AI/ML, and edge computing will be essential to fully realize its potential [\[163\].](#page-35-27)

## <span id="page-25-5"></span><span id="page-25-0"></span>2) V2X COMMUNICATION

<span id="page-25-7"></span><span id="page-25-6"></span>V2X communication is poised to become a fundamental component of future intelligent vehicular systems, facilitating various types of connectivity including vehicle-tovehicle (V2V), vehicle-to-infrastructure (V2I), vehicle-tonetwork (V2N), and vehicle-to-pedestrian (V2P) communications [\[164\],](#page-35-28) [\[165\].](#page-35-29) These connectivity types are essential for developing safe and efficient transportation systems. V2X extends the connectivity of vehicles beyond just other vehicles to include infrastructure, networks, and pedestrians, aiming to enhance road safety, optimize traffic management, enable autonomous driving, and support a broad spectrum of transportation-related applications. The integration of V2X into 6G will leverage advanced communication technologies to address the stringent demands of high mobility and safetycritical scenarios [\[166\],](#page-35-30) [\[167\].](#page-35-31)

<span id="page-25-9"></span><span id="page-25-8"></span>V2X communication holds significant potential to advance vehicular connectivity, fostering intelligent, automated, and cooperative driving experiences. However, several challenges must be addressed, including ensuring reliable connectivity across diverse environments, managing the variability in mobility patterns, and dealing with the complexities of interference and signal fading, particularly in urban settings. Additionally, the integration of non-terrestrial networks (NTNs) and the implementation of AI/ML for predictive and adaptive network management are crucial for overcoming these challenges.

<span id="page-25-3"></span><span id="page-25-2"></span><span id="page-25-1"></span>Research on V2X has been extensive, focusing on areas such as safety, traffic efficiency, and autonomous driving. Future research is likely to explore the integration of AI/ML for resource optimization, the utilization of THz frequencies for ultra-high-speed communication, and the deployment of UAVs as mobile relay nodes to enhance V2X coverage and capacity. The synergy between V2X and other 6G technologies, including NTNs and edge computing, will be critical in creating a fully interconnected and intelligent transportation ecosystem.

## 3) CELLULAR-CONNECTED UAV COMMUNICATION

<span id="page-25-12"></span><span id="page-25-11"></span><span id="page-25-10"></span><span id="page-25-4"></span>Unmanned Aerial Vehicle (UAV) communication is anticipated to unlock new aerial applications by providing seamless, high-quality mobile connectivity for UAVs, thereby broadening their use across various sectors such as logistics, surveillance, agriculture, and emergency response [\[168\],](#page-35-32) [\[169\],](#page-35-33) [\[170\].](#page-35-34) This technology involves integrating UAVs into existing mobile networks, allowing them to utilize cellular infrastructure for data transmission and control, supporting a wide range of applications from remote sensing and monitoring to delivery services and beyond. The advancement of 6G

![](_page_26_Picture_1.jpeg)

<span id="page-26-1"></span>

| Technology                               | Vision                                                                      | Opportunities                                                          | Challenges                                                                   |
|------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------|
| D2D Communications                       | Direct communication between devices without base stations.                 | Improves spectral efficiency, reduces latency, supports public safety. | Interference management, device discovery, security, and privacy issues.     |
| V2X Communications                       | Key for intelligent vehicu-<br>lar systems enabling vari-<br>ous V2X types. | Enhances safety, traffic management, supports cooperative driving.     | Connectivity, mobility variability, interference, and integration with NTNs. |
| Cellular-Connected UAV<br>Communications | Connectivity for UAVs in logistics, surveillance, and more.                 | Improved coverage, real-time control, useful in urban areas.           | High-altitude communication, interference, 3D network planning.              |

<span id="page-26-0"></span>![](_page_26_Picture_4.jpeg)

**FIGURE 15.** End-Device-Oriented communication technologies for 6G.

is expected to further enhance UAV capabilities by providing reliable, low-latency connections and enabling operations in challenging environments like urban areas with dense obstructions [\[171\],](#page-35-35) [\[172\].](#page-35-36)

<span id="page-26-3"></span><span id="page-26-2"></span>Leveraging cellular networks for UAV communication offers numerous opportunities, including improved coverage, enhanced reliability, and the potential for real-time control and data exchange. However, challenges remain, such as the unique propagation characteristics of high-altitude communication, air-ground interference, and the need for comprehensive 3D network planning and management. Solutions being explored to address these challenges include advanced beamforming techniques, 3D massive MIMO, and AI-driven network optimization.

Interest in cellular-connected UAVs has grown significantly within both academic and industrial sectors, with research focusing on the development of communication protocols, interference management, and adaptations to network architecture. Additionally, collaborative UAV operations and the integration of UAVs into broader IoT ecosystems will be critical areas of exploration, aiming to maximize the potential of UAV technology in various applications.

Table [13](#page-26-1) presents a comprehensive summary of enddevice-oriented communication technologies for 6G networks, detailing their key aspects under the categories of Technology, Vision, Opportunities, and Challenges.

## H. DESIGNING RESILIENT AND TRUSTWORTHY 6G NETWORKS

<span id="page-26-6"></span><span id="page-26-5"></span><span id="page-26-4"></span>As 6G networks are poised to become integral to future societies, ensuring their security, trustworthiness, and privacy is paramount. With an increasing dependency on 6G for critical services and the massive amount of data it will handle, a robust security architecture is essential. This section discusses the key aspects of 6G security, focusing on the holistic architecture needed, the evolving threat landscape, and the technology solutions that will safeguard these nextgeneration networks [\[173\],](#page-35-37) [\[174\],](#page-35-38) [\[175\].](#page-36-0)

![](_page_27_Picture_1.jpeg)

*Network Security Architecture:* Mobile network security traditionally focuses on protecting against external threats and attacks, ensuring that networks remain safe and reliable. For 6G, this will involve a holistic security architecture that spans all layers of the network, from the physical and medium access control (PHY and MAC) layers to the application layer. As 6G networks are expected to support a wide array of applications, including those in healthcare, transportation, and industrial automation, securing these layers becomes increasingly critical [\[176\],](#page-36-1) [\[177\],](#page-36-2) [\[178\].](#page-36-3) The challenge is compounded by the growing use of AI/ML, which, while enhancing network capabilities, also introduces new vulnerabilities due to the increasing volume and sensitivity of data [\[179\].](#page-36-4)

<span id="page-27-3"></span><span id="page-27-0"></span>With each generation of mobile networks, new security threats emerge alongside the introduction of novel technologies, services, and applications. Earlier generations faced threats such as unauthorized access, data interception, and physical attacks. For 5G, security architectures were enhanced with advanced authentication mechanisms, access-agnostic solutions, and user privacy protections as specified in 3GPP's Release 15. However, with the extended capabilities expected in 6G, including pervasive AI/ML and integrated non-terrestrial networks (NTNs), new security paradigms must be established to address these emerging threats. Key to this effort will be a thorough understanding of the 6G threat landscape, which includes identifying new vulnerabilities and developing technological solutions to mitigate them. This will require ongoing updates to the security framework as technologies evolve, ensuring that security measures are always aligned with the latest developments.

Recent surveys have highlighted the growing concern over 6G security, emphasizing the need for new strategies to address privacy violations and the protection of vast data flows. Key areas of research include AI/ML-driven security solutions, quantum-safe encryption, and privacy-preserving technologies. Future research will likely continue to explore the integration of AI/ML in security frameworks, while also addressing the dual role of AI/ML as both a tool for enhancing security and a potential vulnerability. Developing secure AI/ML models, robust physical layer security techniques, and zero-trust architectures will be essential to building a resilient 6G security landscape. Additionally, as 6G security will be integral to smart healthcare and digital twins, interdisciplinary efforts will be required to create tailored solutions that address the unique security needs of these domains [\[180\],](#page-36-5) [\[181\].](#page-36-6)

#### <span id="page-27-5"></span><span id="page-27-4"></span>1) DL-BASED PHY SECURITY STUDIES

The integration of deep learning (DL) into Physical Layer (PHY) security is a growing area of research aimed at mitigating various types of attacks, such as spoofing, jamming, and eavesdropping [\[68\]. P](#page-33-15)HY security deals with the vulnerabilities arising from the open nature of wireless communications, particularly when adversaries can easily eavesdrop or tamper with transmissions at the physical layer. Traditionally, PHY security has relied on cryptographic approaches that function at upper layers. However, with the advent of 5G and IoT networks, these methods prove inadequate in terms of scalability and real-time application. DL-based methods offer promising solutions by leveraging neural networks for real-time detection and counteraction of malicious activities at the physical layer.

The most common types of attacks on PHY security are:

- <span id="page-27-2"></span><span id="page-27-1"></span>• **Spoofing:** An attacker (Eve) impersonates a legitimate transmitter (Alice) to deceive the receiver (Bob).
- **Jamming:** Eve disrupts legitimate communication by transmitting signals that interfere with the communication channel.
- **Eavesdropping:** Eve intercepts the communication between Alice and Bob, aiming to gain unauthorized access to transmitted information.

By implementing DL models, researchers are able to provide anti-spoofing, anti-jamming, and anti-eavesdropping solutions. These methods have demonstrated improvements in detection accuracy, efficiency, and adaptability compared to traditional rule-based methods. Table [14](#page-28-0) summarizes key studies across each of these attack types.

#### 2) ANTI-SPOOFING SOLUTIONS

DL-based methods for spoofing detection utilize channel state information (CSI) and channel estimation matrices. These models classify the transmission as legitimate or spoofed by evaluating discrepancies in CSI. CNN and DNN models offer high accuracy but require training within the coherence time, which limits their practical applications. Research such as Liao et al. [\[182\],](#page-36-7) Qiu et al. [\[183\],](#page-36-8) and Liao et al. [\[184\]](#page-36-9) have shown significant progress in overcoming these challenges.

#### 3) ANTI-JAMMING SOLUTIONS

Traditional anti-jamming techniques like frequency hopping or spread spectrum methods are enhanced through DL, particularly with reinforcement learning-based approaches such as deep Q-networks (DQN). These methods improve detection accuracy and system robustness but often lack real-world data validation, as seen in the studies of Han et al. [\[185\],](#page-36-10) Liu et al. [\[186\],](#page-36-11) and Bi et al. [\[187\].](#page-36-12)

#### 4) ANTI-EAVESDROPPING SOLUTIONS

Encryption-based approaches are extended through DL with the use of autoencoders (AE), enabling the encoding and decoding of transmissions while ensuring secrecy. Studies like Fritschek et al. [\[188\]](#page-36-13) and Sun et al. [\[189\]](#page-36-14) show that DL can balance secrecy and bit error rate (BER) but lack realworld testing, which limits their applicability.

# I. POTENTIAL CHANNEL CODING SCHEMES FOR 6G

6G networks are poised to deliver data rates of up to 1 Tb/s, which is a substantial leap from the capabilities of 5G,

![](_page_28_Picture_1.jpeg)

<span id="page-28-0"></span>**TABLE 14.** Overview of important DL-based security studies.

| Attack Type   | Paper Citation | DL Structure   | Model Input             | Key Advantages               | Key Drawbacks               |
|---------------|----------------|----------------|-------------------------|------------------------------|-----------------------------|
| Spoofing      | [182]          | CNN            | CSI Vector              | Comprehensive analysis,      | Requires training after co- |
|               |                |                |                         | works with small datasets    | herence time                |
|               | [183]          | CNN            | Channel Estimation Ma-  | Efficient feature extraction | CSI requirement             |
|               |                |                | trix                    |                              |                             |
|               | [184]          | DNN CNN        | CSI Matrix              | Comprehensive, multi-        | CSI requirement             |
|               |                | PCNN           |                         | user results                 |                             |
| Jamming       | [185]          | CNN-based      | State Matrix            | Applicable to any channel    | No real-world data          |
|               |                | DQN            |                         | model                        |                             |
|               | [186]          | Recursive CNN- | Spectrum Sensing Matrix | Incorporates raw data,       | More training time          |
|               |                | based DQN      |                         | cost of frequency hops       | needed, no real-world       |
|               |                |                |                         |                              | data                        |
|               | [187]          | CNN and LSTM-  | User ID, Position       | More stable than DQN         | No real-world data          |
|               |                | based Double   |                         |                              |                             |
|               |                | DQN            |                         |                              |                             |
| Eavesdropping | [188]          | AE             | One-hot-encoded message | DL capability, balance be-   | Bob has a better channel,   |
|               |                |                | vector                  | tween BER and secrecy        | no real-world data          |
|               | [189]          | CNN-based AE   | One-hot-encoded message | Includes authentication      | Limited analysis, no real-  |
|               |                |                | vector                  | model                        | world data                  |
|               | [190]          | AE             | Message Vector          | Extensive theoretical anal-  | No real-world data          |
|               |                |                |                         | ysis                         |                             |

<span id="page-28-1"></span>**TABLE 15.** Potential channel coding schemes for 6G.

| Coding Scheme           | Key Features                                                                      | Challenges and Applications                 |  |
|-------------------------|-----------------------------------------------------------------------------------|---------------------------------------------|--|
| Non-Binary Codes        | Utilizes higher-dimensional alphabets Increased decoding complexity.              |                                             |  |
|                         | for improved efficiency and resilience.                                           | quires advanced decoders.                   |  |
|                         | Suitable for high data rate scenarios.                                            |                                             |  |
| Fountain Codes          | Generates infinite encoded symbols, High adaptability but needs efficie           |                                             |  |
|                         | flexible and robust against packet loss. decoding. Ideal for multicast/broadcast. |                                             |  |
| Lattice Codes           | Uses multidimensional spaces for ef- High complexity in design/decode             |                                             |  |
|                         | ficient packing and correction. Suited                                            | Effective in massive MIMO.                  |  |
|                         | for multi-user and interference manage-                                           |                                             |  |
|                         | ment.                                                                             |                                             |  |
| Sparse Regression Codes | Structured codebooks for capacity-                                                | acity- Challenges in power optimization and |  |
|                         | approaching performance with low complexity management.                           |                                             |  |
|                         | complexity.                                                                       |                                             |  |
| Application Layer Cod-  | Operates at higher layers, flexible for                                           | Issues with synchronization and la-         |  |
| ing                     | diverse data formats. Good for multi-                                             | tency. Balances simplicity and perfor-      |  |
|                         | media and IoT.                                                                    | mance.                                      |  |

necessitating the development of advanced channel codes that not only maximize spectral efficiency but also adhere to stringent energy and latency constraints. The challenge lies in creating codes that maintain low processing delays and high performance under these conditions, as current codes like LDPC and polar codes, optimized for 5G, may not efficiently scale to meet the heightened demands of 6G. Ultralow latency communication is a cornerstone of 6G, critical for applications such as autonomous driving, industrial automation, and real-time augmented reality, but achieving this requires short block length codes that, while reducing

transmission delays, also increase the likelihood of errors due to fewer redundancy bits. This trade-off necessitates new short block length codes with improved error correction capabilities and lower computational complexity, ensuring that optimal decoders minimize latency without sacrificing reliability.

Additionally, 6G's vision of integrating communication with sensing technologies for applications like smart cities, precision environmental monitoring, and advanced vehicular networks introduces unique challenges, as codes optimized for communication may not perform well in sensing-centric

<span id="page-29-0"></span>![](_page_29_Figure_2.jpeg)

**FIGURE 16.** Channel coding schemes for 6G.

tasks where signal fidelity and accuracy are crucial. This dual functionality often leads to increased noise and interference, complicating signal decoding and requiring versatile coding schemes that can dynamically adapt to the demands of joint sensing and communication environments. Moreover, the dynamic and heterogeneous nature of 6G networks with variable channel conditions influenced by mobility, non-terrestrial components, and dense urban environments demands adaptive coding techniques that adjust in real-time to changing channel states to maintain optimal performance. These codes must also be robust against high noise levels and interference typical in such settings, ensuring reliable data transmission across the diverse and complex scenarios that characterize 6G communication. As depicted in Figure [16,](#page-29-0) a variety of channel coding schemes are proposed for 6G networks.

# 1) NON-BINARY CODES

Non-binary codes extend traditional binary coding schemes by utilizing symbol sets from higher-dimensional alphabets, such as Galois fields, to enhance coding efficiency and resilience against errors. These codes can achieve higher spectral efficiencies, which are critical for supporting the massive data demands of 6G. Non-binary LDPC and polar codes are promising candidates, as they offer improved performance over their binary counterparts in terms of error correction and adaptability to short block length requirements. However, the increased complexity associated with decoding non-binary codes remains a significant challenge, necessitating innovations in decoder design to make them viable for real-time applications in 6G networks.

# 2) FOUNTAIN CODES AND RATE-LESS CODING

Fountain codes, including LT and raptor codes, represent a class of rate-less coding schemes that are particularly suitable for 6G's diverse and dynamic environments [\[191\].](#page-36-15) These codes generate an essentially infinite stream of encoded symbols, allowing receivers to collect as many as needed to reconstruct the original data. This adaptability makes fountain codes ideal for scenarios with varying channel conditions, as they inherently provide robustness against packet loss and fluctuating link quality. Additionally, their erasure-resilience properties ensure reliable data transmission even in the presence of high interference, making them well-suited for multicast and broadcast applications in 6G.

## 3) LATTICE CODES

<span id="page-29-3"></span><span id="page-29-2"></span>Lattice codes, which are built upon geometric lattice structures, offer a promising approach for high-dimensional modulation and coding in 6G [\[192\],](#page-36-16) [\[193\].](#page-36-17) These codes excel in exploiting the spatial structure of multidimensional signal spaces, enabling efficient packing and error correction. Lattice codes are particularly effective in scenarios involving multi-user communication and interference management, as they can leverage the inherent structure of the communication medium to enhance performance. The application of lattice codes extends to advanced 6G use cases, including massive MIMO systems and integrated communication and sensing, where they can provide significant gains in data rate and error resilience.

#### 4) SPARSE REGRESSION CODES (SPARCS)

<span id="page-29-6"></span><span id="page-29-5"></span><span id="page-29-4"></span>SPARCs, or sparse regression codes, utilize structured code books and sparse message representations to achieve capacity-approaching performance with low complexity [\[194\],](#page-36-18) [\[195\],](#page-36-19) [\[196\].](#page-36-20) These codes are designed to handle the high-dimensional signal spaces characteristic of 6G communication environments, making them well-suited for use in channels with stringent performance requirements. By optimizing power allocation and incorporating advanced modulation techniques, SPARCs can deliver exceptional performance.

<span id="page-29-9"></span><span id="page-29-8"></span><span id="page-29-7"></span>Application Layer Channel Coding: Application layer channel coding, including schemes like fountain codes and Reed-Solomon codes, operates at a higher level of the communication stack, offering flexibility in handling diverse data formats and error conditions [\[197\],](#page-36-21) [\[198\],](#page-36-22) [\[199\].](#page-36-23) This approach allows for tailored coding strategies that align closely with application-specific requirements, such as those in multimedia streaming, IoT, and deep space communications [\[200\].](#page-36-24) While application layer coding can simplify implementation and enhance adaptability, it introduces challenges in maintaining synchronization and managing latency, particularly when interfacing with lower-layer coding mechanisms.

<span id="page-29-10"></span><span id="page-29-1"></span>As the development of 6G progresses, channel coding will play a pivotal role in realizing the full potential of nextgeneration networks. The challenges outlined necessitate a comprehensive approach to coding design, incorporating advances in non-binary coding, rate-less coding, and other innovative schemes as shown in Table [15.](#page-28-1) By addressing

![](_page_30_Picture_1.jpeg)

the unique demands of 6G, including high data rates, low latency, and integrated sensing and communication, future coding techniques will enable robust, efficient, and adaptable communication systems that can meet the diverse needs of a hyper-connected world.

#### <span id="page-30-0"></span>**VIII. DEFINING FEATURES FOR 6G**

The advent of 6G is expected to bring transformative changes across global communication landscapes, defined by a set of features that aim to push the boundaries of what current and previous generations of mobile technology can achieve. The defining features of 6G as shown in Figure [17](#page-30-1) include extreme capacity and performance, ultraflexibility and agility, high intelligence and awareness, ubiquitous availability and reliability, true sustainability, and comprehensive security and trustworthiness. These features form the core pillars of 6G, supporting an extensive range of advanced services and applications that will cater to the evolving demands of society, industries, and technology ecosystems [\[18\].](#page-32-9)

<span id="page-30-1"></span>![](_page_30_Figure_5.jpeg)

**FIGURE 17.** Core attributes of the 6G Era.

## A. EXTREME CAPACITY AND PERFORMANCE

One of the cornerstones of 6G will be its extreme capacity and performance, targeting enhancements across several key dimensions. 6G aims to push performance to its limits, supporting a vast array of demanding applications and services by achieving peak data rates of up to 1 Tbps, ultra-low latencies, and superior spectral efficiency. This high performance will be critical for applications requiring real-time data processing, such as autonomous driving. Additionally, 6G is expected to deliver energy-efficient communication solutions, reducing the overall power consumption of networks while maintaining high performance levels.

## B. ULTRA-FLEXIBLE AND AGILE

6G networks will be designed to be ultra-flexible and agile, adapting seamlessly to diverse and dynamic wireless environments and application scenarios. This flexibility is essential for optimizing performance at all levels of the network, from the physical layer to the service layer. It will enable 6G to support a wide variety of use cases with differing requirements, including high-mobility scenarios, dense urban environments, and rural connectivity.

### C. HIGHLY INTELLIGENT AND AWARE

A revolutionary feature of 6G will be its high level of intelligence, driven by pervasive AI and machine learning (ML) technologies. The extensive use of AI/ML will make 6G networks highly intelligent, enhancing their ability to design, operate, and manage themselves autonomously. AI/ML enable capabilities such as predictive maintenance, real-time analytics, dynamic resource allocation, and anomaly detection. Additionally, 6G is expected to incorporate network sensing capabilities, making it aware of its environment and opening up new service opportunities that go beyond traditional communication.

#### D. RELIABILITY AND UBIQUITOUS AVAILABILITY

6G networks will be built to support a wide range of robust services by integrating terrestrial and non-terrestrial networks, such as satellite and high-altitude platform systems, to provide broad coverage even in underserved areas. Various network-level reliability measures, including physical layer enhancements, network-level redundancy, and fault tolerance mechanisms, will be employed to maximize reliability. 6G will enable mission-critical applications, like connected healthcare, industrial automation, and emergency services, by guaranteeing continuous and reliable connectivity.

#### E. TRULY GREEN AND SUSTAINABLE

As global data traffic continues to grow, the energy consumption of mobile networks is a growing concern. 6G will prioritize green and sustainable design principles, enhancing energy efficiency across all levels of the network, from core operations to the air interface. Technologies such as energy harvesting, energy-aware routing, and intelligent power management will play a critical role in reducing the carbon footprint of 6G networks. By promoting sustainability, 6G aims to provide ecological and economic benefits, aligning with global efforts to reduce environmental impact.

#### F. THOROUGHLY SECURE AND TRUSTWORTHY

Given the critical role 6G is expected to play in future society, ensuring security and trustworthiness will be of utmost importance. 6G will require a holistic security architecture that addresses threats across all network layers, protecting data integrity, confidentiality, and availability. This

<span id="page-31-9"></span>![](_page_31_Picture_1.jpeg)

**TABLE 16.** Defining features for 6G.

| Feature                  | Vision                 | Description                                                               |
|--------------------------|------------------------|---------------------------------------------------------------------------|
| Extreme Capacity and     | High performance       | Supports data rates up to 1 Tbps, ultra-low latency, and high spectral    |
| Performance              |                        | efficiency, enhancing real-time data processing and energy efficiency.    |
| Ultra-Flexible and Agile | Adaptability           | Adapts to diverse environments and use cases through technologies         |
|                          |                        | like software-defined networking and dynamic spectrum management.         |
| Highly Intelligent and   | AI-driven intelligence | Integrates AI/ML for autonomous network operation, predictive main-       |
| Aware                    |                        | tenance, and environment sensing.                                         |
| Ubiquitously Available   | Broad coverage         | Combines terrestrial and non-terrestrial networks for continuous, reli-   |
| and Reliable             |                        | able connectivity in all areas.                                           |
| Truly Green and Sus-     | Energy efficiency      | Focuses on reducing energy consumption through green technologies         |
| tainable                 |                        | like energy harvesting and intelligent power management.                  |
| Thoroughly Secure and    | Comprehensive security | Implements holistic security to protect data integrity and privacy across |
| Trustworthy              |                        | all network layers.                                                       |

architecture will need to evolve continuously to address new and emerging threats associated with pervasive AI/ML, increased data abundance, and diverse applications ranging from smart healthcare to autonomous vehicles. Ensuring robust security and trust in 6G will be crucial for the safe and reliable operation of the network, especially as it becomes more deeply integrated into everyday life and critical infrastructure.

This comprehensive overview of 6G's defining features as shown in Table [16](#page-31-9) underscores the transformative potential of next-generation communication networks, highlighting their capacity to support advanced applications, promote sustainability, and ensure secure and reliable connectivity across diverse environments. These features set the foundation for a future where 6G enables a fully connected, intelligent, and efficient world.

# <span id="page-31-8"></span>**IX. CONCLUSION**

The evolution from 1G to 5G has paved the way for the ambitious development of 6G, which aims to redefine mobile communications by integrating a broad array of cutting-edge technologies and addressing the limitations of current networks. This document has provided a comprehensive overview of the anticipated capabilities, challenges, and opportunities associated with 6G, underscoring its potential to fundamentally transform the digital landscape. Central to the 6G vision is the pursuit of ultra-high data rates up to 1 Tb/s, ultra-low latency, and extreme reliability, which will enable groundbreaking applications across diverse sectors, including autonomous driving, remote healthcare, and smart cities. The technological advancements that underpin 6G will not only improve traditional communication parameters but also introduce new paradigms of connectivity that seamlessly blend the physical and digital worlds. The document has highlighted the critical role of AI/ML in enabling adaptive, self-optimizing networks that can respond dynamically to real-time demands and environmental changes, thus pushing the boundaries of what mobile networks can achieve. Security, privacy, and energy efficiency also emerge as crucial considerations, necessitating holistic architectural solutions that address the multi-faceted needs of next-generation networks. The document has emphasized the importance of a collaborative approach, involving academia, industry, and regulatory bodies, to develop standardized frameworks that ensure interoperability, scalability, and sustainability of 6G systems. Looking forward, the success of 6G will hinge on continued innovation and rigorous research to overcome the identified challenges and unlock new possibilities. The potential of 6G extends far beyond incremental improvements; it represents a transformative leap that could enable ubiquitous, intelligent connectivity for an increasingly digital and interconnected world. By building on the foundational technologies discussed, 6G is poised to catalyze a new era of hyper-connectivity, driving advancements in automation, immersive experiences, and global digital inclusion. As we stand on the brink of this technological frontier, the road map to 6G will require bold visions, strategic investments, and a commitment to addressing the complex socio-technical dynamics that will shape the future of communication.

#### **REFERENCES**

- <span id="page-31-0"></span>[\[1\] W](#page-1-0). R. Young, ''Advanced mobile phone service: Introduction, background, and objectives,'' *Bell Syst. Tech. J.*, vol. 58, no. 1, pp. 1–14, Jan. 1979.
- <span id="page-31-1"></span>[\[2\] V](#page-1-1). H. M. Donald, ''Advanced mobile phone service: The cellular concept,'' *Bell Syst. Tech. J.*, vol. 58, no. 1, pp. 15–41, Jan. 1979.
- <span id="page-31-2"></span>[\[3\] R](#page-1-2). Frenkiel and M. Schwartz, ''Creating cellular: A history of the AMPS project (1971–1983) [history of communications],'' *IEEE Commun. Mag.*, vol. 48, no. 9, pp. 14–24, Sep. 2010.
- <span id="page-31-3"></span>[\[4\] A](#page-1-3). Furuskar, S. Mazur, F. Müller, and H. Olofsson, ''EDGE: Enhanced data rates for GSM and TDMA/136 evolution,'' *IEEE Pers. Commun.*, vol. 6, no. 3, pp. 56–66, Jun. 1999.
- <span id="page-31-4"></span>[\[5\] Y](#page-1-4).-B. Lin, H. C.-H. Rao, and I. Chlamtac, ''General packet radio service (GPRS): Architecture, interfaces, and deployment,'' *Wireless Commun. Mobile Comput.*, vol. 1, no. 1, pp. 77–92, Jan. 2001.
- <span id="page-31-5"></span>[\[6\] R](#page-1-5). Attar, D. Ghosh, C. Lott, M. Fan, P. Black, R. Rezaiifar, and P. Agashe, ''Evolution of cdma2000 cellular networks: Multicarrier EV-DO,'' *IEEE Commun. Mag.*, vol. 44, no. 3, pp. 46–53, Mar. 2006.
- <span id="page-31-6"></span>[\[7\] P](#page-1-6). Chaudhury, W. Mohr, and S. Onoe, ''The 3GPP proposal for IMT-2000,'' *IEEE Commun. Mag.*, vol. 37, no. 12, pp. 72–81, Dec. 1999.
- <span id="page-31-7"></span>[\[8\] E](#page-1-7). Dahlman, S. Parkvall, and J. Skold, *4G: LTE/LTE-Advanced for Mobile Broadband*. New York, NY, USA: Academic, 2013.

![](_page_32_Picture_1.jpeg)

- <span id="page-32-0"></span>[\[9\] H](#page-1-8). Holma and A. Toskala, *WCDMA for UMTS: Radio Access for Third Generation Mobile Communications*. Hoboken, NJ, USA: Wiley, 2005.
- <span id="page-32-1"></span>[\[10\]](#page-1-9) H. Holma and A. Toskala, *WCDMA for Umts: Hspa Evolution and LTE*. Hoboken, NJ, USA: Wiley, 2010.
- <span id="page-32-2"></span>[\[11\]](#page-1-10) A. M. Rao, A. Weber, S. Gollamudi, and R. Soni, ''LTE and HSPA+: Revolutionary and evolutionary solutions for global mobile broadband,'' *Bell Labs Tech. J.*, vol. 13, no. 4, pp. 7–34, Winter. 2009.
- <span id="page-32-3"></span>[\[12\]](#page-1-11) J.-P. Rissen and R. Soni, ''The evolution to 4G systems,'' *Bell Labs Tech. J.*, vol. 13, no. 4, pp. 1–5, Winter. 2009.
- <span id="page-32-4"></span>[\[13\]](#page-1-12) S. Parkvall, E. Dahlman, A. Furuskar, and M. Frenne, ''NR: The new 5G radio access technology,'' *IEEE Commun. Standards Mag.*, vol. 1, no. 4, pp. 24–30, Dec. 2017.
- <span id="page-32-5"></span>[\[14\]](#page-1-13) *Service Requirements for the 5G System*, document TS 22.261, 3GPP, 2019.
- <span id="page-32-6"></span>[\[15\]](#page-1-14) S. Baek, D. Kim, M. Tesanovic, and A. Agiwal, ''3GPP new radio release 16: Evolution of 5G for industrial Internet of Things,'' *IEEE Commun. Mag.*, vol. 59, no. 1, pp. 41–47, Jan. 2021.
- <span id="page-32-7"></span>[\[16\]](#page-1-15) W. Chen, J. Montojo, J. Lee, M. Shafi, and Y. Kim, ''The standardization of 5G-advanced in 3GPP,'' *IEEE Commun. Mag.*, vol. 60, no. 11, pp. 98–104, Nov. 2022.
- <span id="page-32-8"></span>[\[17\]](#page-1-16) *Detailed Specifications of the Terrestrial Radio Interfaces of International Mobile Telecommunications-2020 (IMT-2020)*, document ITU 2150, 2021.
- <span id="page-32-9"></span>[\[18\]](#page-2-2) H. Pennanen, T. Hänninen, O. Tervo, A. Tölli, and M. Latva-aho, ''6G: The intelligent network of everything—A comprehensive vision, survey, and tutorial,'' 2024, *arXiv:2407.09398*.
- <span id="page-32-10"></span>[\[19\]](#page-2-3) M. Alsabah, M. A. Naser, B. M. Mahmmod, S. H. Abdulhussain, M. R. Eissa, A. Al-Baidhani, N. K. Noordin, S. M. Sait, K. A. Al-Utaibi, and F. Hashim, ''6G wireless communications networks: A comprehensive survey,'' *IEEE Access*, vol. 9, pp. 148191–148243, 2021.
- [\[20\]](#page-0-1) K. David and H. Berndt, ''6G vision and requirements: Is there any need for beyond 5G?'' *IEEE Veh. Technol. Mag.*, vol. 13, no. 3, pp. 72–80, Sep. 2018.
- [\[21\]](#page-0-1) M. Katz, M. Matinmikko-Blue, and M. Latva-Aho, ''6Genesis flagship program: Building the bridges towards 6G-enabled wireless smart society and ecosystem,'' in *Proc. IEEE 10th Latin-Amer. Conf. Commun. (LATINCOM)*, Nov. 2018, pp. 1–9.
- [\[22\]](#page-0-1) K. B. Letaief, W. Chen, Y. Shi, J. Zhang, and Y. A. Zhang, ''The roadmap to 6G: AI empowered wireless networks,'' *IEEE Commun. Mag.*, vol. 57, no. 8, pp. 84–90, Aug. 2019.
- [\[23\]](#page-0-1) L. Zhang, Y.-C. Liang, and D. Niyato, ''6G visions: Mobile ultrabroadband, super Internet-of-Things, and artificial intelligence,'' *China Commun.*, vol. 16, no. 8, pp. 1–14, Aug. 2019.
- [\[24\]](#page-0-1) I. Tomkos, D. Klonidis, E. Pikasis, and S. Theodoridis, ''Toward the 6G network era: Opportunities and challenges,'' *IT Prof.*, vol. 22, no. 1, pp. 34–38, Jan. 2020.
- [\[25\]](#page-0-1) M. Z. Chowdhury, M. Shahjalal, S. Ahmed, and Y. M. Jang, ''6G wireless communication systems: Applications, requirements, technologies, challenges, and research directions,'' *IEEE Open J. Commun. Soc.*, vol. 1, pp. 957–975, 2020.
- [\[26\]](#page-0-1) G. Gui, M. Liu, F. Tang, N. Kato, and F. Adachi, ''6G: Opening new horizons for integration of comfort, security, and intelligence,'' *IEEE Wireless Commun.*, vol. 27, no. 5, pp. 126–132, Oct. 2020.
- [\[27\]](#page-0-1) H. Yang, A. Alphones, Z. Xiong, D. Niyato, J. Zhao, and K. Wu, ''Artificial-Intelligence-Enabled intelligent 6G networks,'' *IEEE Netw.*, vol. 34, no. 6, pp. 272–280, Nov. 2020.
- [\[28\]](#page-0-1) H. Tataria, M. Shafi, A. F. Molisch, M. Dohler, H. Sjöland, and F. Tufvesson, ''6G wireless systems: Vision, requirements, challenges, insights, and opportunities,'' *Proc. IEEE*, vol. 109, no. 7, pp. 1166–1199, Jul. 2021.
- [\[29\]](#page-0-1) M. A. Uusitalo, P. Rugeland, M. R. Boldi, E. C. Strinati, P. Demestichas, M. Ericson, G. P. Fettweis, M. C. Filippou, A. Gati, M.-H. Hamon, M. Hoffmann, M. Latva-Aho, A. Pärssinen, B. Richerzhagen, H. Schotten, T. Svensson, G. Wikström, H. Wymeersch, V. Ziegler, and Y. Zou, ''6G vision, value, use cases and technologies from European 6G flagship project Hexa-X,'' *IEEE Access*, vol. 9, pp. 160004–160020, 2021.
- [\[30\]](#page-0-1) S. A. A. Hakeem, H. H. Hussein, and H. W. Kim, ''Vision and research directions of 6G technologies and applications,'' *J. King Saud Univ.- Comput. Inf. Sci.*, vol. 34, no. 6, pp. 2419–2442, 2022.
- [\[31\]](#page-0-1) Y. Lu and X. Zheng, ''6G: A survey on technologies, scenarios, challenges, and the related issues,'' *J. Ind. Inf. Integr.*, vol. 19, Sep. 2020, Art. no. 100158.

- [\[32\]](#page-0-1) H. H. H. Mahmoud, A. A. Amer, and T. Ismail, ''6G: A comprehensive survey on technologies, applications, challenges, and research problems,'' *Trans. Emerg. Telecommun. Technol.*, vol. 32, no. 4, p. e4233, Apr. 2021.
- [\[33\]](#page-0-1) S. Alraih, I. Shayea, M. Behjati, R. Nordin, N. F. Abdullah, A. Abu-Samah, and D. Nandi, ''Revolution or evolution? Technical requirements and considerations towards 6G mobile communications,'' *Sensors*, vol. 22, no. 3, p. 762, Jan. 2022.
- [\[34\]](#page-0-1) M. Banafaa, I. Shayea, J. Din, M. H. Azmi, A. Alashbi, Y. I. Daradkeh, and A. Alhammadi, ''6G mobile communication technology: Requirements, targets, applications, challenges, advantages, and opportunities,'' *Alexandria Eng. J.*, vol. 64, pp. 245–274, Feb. 2023.
- [\[35\]](#page-0-1) I. Ishteyaq, K. Muzaffar, N. Shafi, and M. A. Alathbah, ''Unleashing the power of tomorrow: Exploration of next frontier with 6G networks and cutting edge technologies,'' *IEEE Access*, vol. 12, pp. 29445–29463, 2024.
- [\[36\]](#page-0-1) S. Kerboeuf et al., ''Design methodology for 6G end-to-end system: Hexa-X-II perspective,'' *IEEE Open J. Commun. Soc.*, vol. 5, pp. 3368–3394, 2024.
- <span id="page-32-11"></span>[\[37\]](#page-7-1) Y. Wang, Z. Su, N. Zhang, R. Xing, D. Liu, T. H. Luan, and X. Shen, ''A survey on metaverse: Fundamentals, security, and privacy,'' *IEEE Commun. Surveys Tuts.*, vol. 25, no. 1, pp. 319–352, 1st Quart., 2023.
- <span id="page-32-12"></span>[\[38\]](#page-7-2) Z. Huang, C. Xiong, H. Ni, D. Wang, Y. Tao, and T. Sun, ''Standard evolution of 5G-advanced and future mobile network for extended reality and metaverse,'' *IEEE Internet Things Mag.*, vol. 6, no. 1, pp. 20–25, Mar. 2023.
- <span id="page-32-13"></span>[\[39\]](#page-7-3) I. F. Akyildiz and H. Guo, ''Wireless communication research challenges for extended reality (XR),'' *ITU J. Future Evolving Technol.*, vol. 3, no. 2, pp. 273–287, Apr. 2022.
- <span id="page-32-14"></span>[\[40\]](#page-7-4) M. Gapeyenko, V. Petrov, S. Paris, A. Marcano, and K. I. Pedersen, ''Standardization of extended reality (XR) over 5G and 5G-advanced 3GPP new radio,'' *IEEE Netw.*, vol. 37, no. 4, pp. 22–28, Jul. 2023.
- <span id="page-32-15"></span>[\[41\]](#page-7-5) A. Kirimtat, O. Krejcar, A. Kertesz, and M. F. Tasgetiren, ''Future trends and current state of smart city concepts: A survey,'' *IEEE Access*, vol. 8, pp. 86448–86467, 2020.
- <span id="page-32-16"></span>[\[42\]](#page-7-6) M. Murroni, M. Anedda, M. Fadda, P. Ruiu, V. Popescu, C. Zaharia, and D. Giusto, ''6G—Enabling the new smart city: A survey,'' *Sensors*, vol. 23, no. 17, p. 7528, Aug. 2023.
- <span id="page-32-17"></span>[\[43\]](#page-7-7) I. Yaqoob, K. Salah, R. Jayaraman, and M. Omar, ''Metaverse applications in smart cities: Enabling technologies, opportunities, challenges, and future directions,'' *Internet Things*, vol. 23, Oct. 2023, Art. no. 100884.
- <span id="page-32-18"></span>[\[44\]](#page-7-8) B. Chen, J. Wan, L. Shu, P. Li, M. Mukherjee, and B. Yin, ''Smart factory of industry 4.0: key technologies, application case, and challenges,'' *IEEE Access*, vol. 6, pp. 6505–6519, 2018.
- <span id="page-32-19"></span>[\[45\]](#page-7-9) M. Soori, B. Arezoo, and R. Dastres, ''Internet of Things for smart factories in industry 4.0, a review,'' *Internet Things Cyber-Phys. Syst.*, vol. 3, pp. 192–204, May 2023.
- <span id="page-32-20"></span>[\[46\]](#page-7-10) A. Khang, K. C. Rath, S. K. Satapathy, A. Kumar, S. R. Das, and M. R. Panda, ''Enabling the future of manufacturing: Integration of robotics and IoT to smart factory infrastructure in industry 4.0,'' in *Handbook of Research on AI-Based Technologies and Applications in the Era of the Metaverse*. Hershey, PA, USA: IGI Global, 2023, pp. 25–50.
- <span id="page-32-21"></span>[\[47\]](#page-7-11) B. L. R. Stojkoska and K. V. Trivodaliev, ''A review of Internet of Things for smart home: Challenges and solutions,'' *J. Cleaner Prod.*, vol. 140, pp. 1454–1464, Jan. 2017.
- <span id="page-32-22"></span>[\[48\]](#page-7-12) D. Marikyan, S. Papagiannidis, and E. Alamanos, ''A systematic review of the smart home literature: A user perspective,'' *Technological Forecasting Social Change*, vol. 138, pp. 139–154, Jan. 2019.
- <span id="page-32-23"></span>[\[49\]](#page-7-13) B. K. Sovacool and D. D. F. D. Rio, ''Smart home technologies in Europe: A critical review of concepts, benefits, risks and policies,'' *Renew. Sustain. Energy Rev.*, vol. 120, Mar. 2020, Art. no. 109663.
- <span id="page-32-24"></span>[\[50\]](#page-7-14) P. Rodriguez-Garcia, Y. Li, D. Lopez-Lopez, and A. A. Juan, ''Strategic decision making in smart home ecosystems: A review on the use of artificial intelligence and Internet of Things,'' *Internet Things*, vol. 22, Jul. 2023, Art. no. 100772.
- <span id="page-32-25"></span>[\[51\]](#page-7-15) T. Magara and Y. Zhou, ''Internet of Things (IoT) of smart homes: Privacy and security,'' *J. Electr. Comput. Eng.*, vol. 2024, no. 1, 2024, Art. no. 7716956.
- <span id="page-32-26"></span>[\[52\]](#page-7-16) A. Qayyum, M. Usama, J. Qadir, and A. Al-Fuqaha, ''Securing connected & autonomous vehicles: Challenges posed by adversarial machine learning and the way forward,'' *IEEE Commun. Surveys Tuts.*, vol. 22, no. 2, pp. 998–1026, 2nd Quart., 2020.

![](_page_33_Picture_1.jpeg)

- <span id="page-33-0"></span>[\[53\]](#page-7-17) J. He, K. Yang, and H.-H. Chen, ''6G cellular networks and connected autonomous vehicles,'' *IEEE Netw.*, vol. 35, no. 4, pp. 255–261, Jul. 2021.
- <span id="page-33-1"></span>[\[54\]](#page-7-18) V.-L. Nguyen, R.-H. Hwang, P.-C. Lin, A. Vyas, and V.-T. Nguyen, ''Towards the age of intelligent vehicular networks for connected and autonomous vehicles in 6G,'' *IEEE Netw.*, vol. 37, no. 3, pp. 44–51, Mar. 2022.
- <span id="page-33-2"></span>[\[55\]](#page-7-19) S. H. Alsamhi, O. Ma, and M. S. Ansari, ''Survey on artificial intelligence based techniques for emerging robotic communication,'' *Telecommun. Syst.*, vol. 72, no. 3, pp. 483–503, Nov. 2019.
- <span id="page-33-3"></span>[\[56\]](#page-7-20) M. Groshev, G. Baldoni, L. Cominardi, A. D. L. Oliva, and R. Gazda, ''Edge robotics: Are we ready? An experimental evaluation of current vision and future directions,'' *Digit. Commun. Netw.*, vol. 9, no. 1, pp. 166–174, Feb. 2023.
- <span id="page-33-4"></span>[\[57\]](#page-7-21) M. Soori, B. Arezoo, and R. Dastres, ''Artificial intelligence, machine learning and deep learning in advanced robotics, a review,'' *Cognit. Robot.*, vol. 3, pp. 54–70, Apr. 2023.
- <span id="page-33-5"></span>[\[58\]](#page-10-2) O. Simeone, ''A very brief introduction to machine learning with applications to communication systems,'' *IEEE Trans. Cognit. Commun. Netw.*, vol. 4, no. 4, pp. 648–664, Dec. 2018.
- <span id="page-33-6"></span>[\[59\]](#page-10-3) S. C. H. Hoi, D. Sahoo, J. Lu, and P. Zhao, ''Online learning: A comprehensive survey,'' *Neurocomputing*, vol. 459, pp. 249–289, Oct. 2021.
- <span id="page-33-7"></span>[\[60\]](#page-11-1) C. Zhang, P. Patras, and H. Haddadi, ''Deep learning in mobile and wireless networking: A survey,'' *IEEE Commun. Surveys Tuts.*, vol. 21, no. 3, pp. 2224–2287, 3rd Quart., 2019.
- <span id="page-33-8"></span>[\[61\]](#page-11-2) Q. Mao, F. Hu, and Q. Hao, ''Deep learning for intelligent wireless networks: A comprehensive survey,'' *IEEE Commun. Surveys Tuts.*, vol. 20, no. 4, pp. 2595–2621, 4th Quart., 2018.
- <span id="page-33-9"></span>[\[62\]](#page-11-3) L. Dai, R. Jiao, F. Adachi, H. V. Poor, and L. Hanzo, ''Deep learning for wireless communications: An emerging interdisciplinary paradigm,'' *IEEE Wireless Commun.*, vol. 27, no. 4, pp. 133–139, Aug. 2020.
- <span id="page-33-10"></span>[\[63\]](#page-11-4) Y. Cheng, B. Yin, and S. Zhang, ''Deep learning for wireless networking: The next frontier,'' *IEEE Wireless Commun.*, vol. 28, no. 6, pp. 176–183, Dec. 2021.
- <span id="page-33-11"></span>[\[64\]](#page-11-5) P. Joshi, M. Hasanuzzaman, C. Thapa, H. Afli, and T. Scully, ''Enabling all in-edge deep learning: A literature review,'' *IEEE Access*, vol. 11, pp. 3431–3460, 2023.
- <span id="page-33-12"></span>[\[65\]](#page-11-6) S. Zhang, J. Liu, T. K. Rodrigues, and N. Kato, ''Deep learning techniques for advancing 6G communications in the physical layer,'' *IEEE Wireless Commun.*, vol. 28, no. 5, pp. 141–147, Oct. 2021.
- <span id="page-33-13"></span>[\[66\]](#page-11-7) Z. Zheng, L. Wang, F. Zhu, and L. Liu, ''Potential technologies and applications based on deep learning in the 6G networks,'' *Comput. Electr. Eng.*, vol. 95, Oct. 2021, Art. no. 107373.
- <span id="page-33-14"></span>[\[67\]](#page-11-8) A. Jagannath, J. Jagannath, and T. Melodia, ''Redefining wireless communication for 6G: Signal processing meets deep learning with deep unfolding,'' *IEEE Trans. Artif. Intell.*, vol. 2, no. 6, pp. 528–536, Dec. 2021.
- <span id="page-33-15"></span>[\[68\]](#page-11-9) B. Ozpoyraz, A. T. Dogukan, Y. Gevez, U. Altun, and E. Basar, ''Deep learning-aided 6G wireless networks: A comprehensive survey of revolutionary PHY architectures,'' *IEEE Open J. Commun. Soc.*, vol. 3, pp. 1749–1809, 2022.
- <span id="page-33-16"></span>[\[69\]](#page-11-10) S. Niknam, H. S. Dhillon, and J. H. Reed, ''Federated learning for wireless communications: Motivation, opportunities, and challenges,'' *IEEE Commun. Mag.*, vol. 58, no. 6, pp. 46–51, Jun. 2020.
- <span id="page-33-17"></span>[\[70\]](#page-11-11) Y. Liu, X. Yuan, Z. Xiong, J. Kang, X. Wang, and D. Niyato, ''Federated learning for 6G communications: Challenges, methods, and future directions,'' *China Commun.*, vol. 17, no. 9, pp. 105–118, Sep. 2020.
- <span id="page-33-18"></span>[\[71\]](#page-11-12) Z. Yang, M. Chen, K.-K. Wong, H. V. Poor, and S. Cui, ''Federated learning for 6G: Applications, challenges, and opportunities,'' *Engineering*, vol. 8, pp. 33–41, Jan. 2022.
- <span id="page-33-19"></span>[\[72\]](#page-11-13) M. Al-Quraan, L. Mohjazi, L. Bariah, A. Centeno, A. Zoha, K. Arshad, K. Assaleh, S. Muhaidat, M. Debbah, and M. A. Imran, ''Edge-native intelligence for 6G communications driven by federated learning: A survey of trends and challenges,'' *IEEE Trans. Emerg. Topics Comput. Intell.*, vol. 7, no. 3, pp. 957–979, Mar. 2023.
- <span id="page-33-20"></span>[\[73\]](#page-11-14) Q. Duan, J. Huang, S. Hu, R. Deng, Z. Lu, and S. Yu, ''Combining federated learning and edge computing toward ubiquitous intelligence in 6G network: Challenges, recent advances, and future directions,'' *IEEE Commun. Surveys Tuts.*, vol. 25, pp. 2892–2950, 4th Quart., 2023.
- <span id="page-33-21"></span>[\[74\]](#page-11-15) H. Hafi, B. Brik, P. A. Frangoudis, A. Ksentini, and M. Bagaa, ''Split federated learning for 6G enabled-networks: Requirements, challenges, and future directions,'' *IEEE Access*, vol. 12, pp. 9890–9930, 2024.

- <span id="page-33-22"></span>[\[75\]](#page-11-16) F. Zhuang, Z. Qi, K. Duan, D. Xi, Y. Zhu, H. Zhu, H. Xiong, and Q. He, ''A comprehensive survey on transfer learning,'' *Proc. IEEE*, vol. 109, no. 1, pp. 43–76, Jan. 2021.
- <span id="page-33-23"></span>[\[76\]](#page-11-17) C. T. Nguyen, N. Van Huynh, N. H. Chu, Y. M. Saputra, D. T. Hoang, D. N. Nguyen, Q.-V. Pham, D. Niyato, E. Dutkiewicz, and W.-J. Hwang, ''Transfer learning for wireless networks: A comprehensive survey,'' *Proc. IEEE*, vol. 110, no. 8, pp. 1073–1115, Aug. 2022.
- <span id="page-33-24"></span>[\[77\]](#page-11-18) M. Wang, Y. Lin, Q. Tian, and G. Si, ''Transfer learning promotes 6G wireless communications: Recent advances and future challenges,'' *IEEE Trans. Rel.*, vol. 70, no. 2, pp. 790–807, Jun. 2021.
- <span id="page-33-25"></span>[\[78\]](#page-12-0) K. B. Letaief, Y. Shi, J. Lu, and J. Lu, ''Edge artificial intelligence for 6G: Vision, enabling technologies, and applications,'' *IEEE J. Sel. Areas Commun.*, vol. 40, no. 1, pp. 5–36, Jan. 2022.
- <span id="page-33-26"></span>[\[79\]](#page-15-1) I. F. Akyildiz, C. Han, Z. Hu, S. Nie, and J. M. Jornet, ''Terahertz band communication: An old problem revisited and research directions for the next decade,'' *IEEE Trans. Commun.*, vol. 70, no. 6, pp. 4250–4285, Jun. 2022.
- <span id="page-33-27"></span>[\[80\]](#page-15-2) A. Faisal, H. Sarieddeen, H. Dahrouj, T. Y. Al-Naffouri, and M.-S. Alouini, ''Ultramassive MIMO systems at terahertz bands: Prospects and challenges,'' *IEEE Veh. Technol. Mag.*, vol. 15, no. 4, pp. 33–42, Dec. 2020.
- <span id="page-33-28"></span>[\[81\]](#page-15-3) T. Kürner and A. Hirata, ''On the impact of the results of WRC 2019 on THz communications,'' in *Proc. 3rd Int. Workshop Mobile THz Syst. (IWMTS)*, Jul. 2020, pp. 1–3.
- <span id="page-33-29"></span>[\[82\]](#page-16-2) V. Petrov, T. Kurner, and I. Hosako, ''IEEE 802.15.3d: First standardization efforts for sub-terahertz band communications toward 6G,'' *IEEE Commun. Mag.*, vol. 58, no. 11, pp. 28–33, Nov. 2020.
- <span id="page-33-30"></span>[\[83\]](#page-16-3) Z. Chen, B. Ning, C. Han, Z. Tian, and S. Li, ''Intelligent reflecting surface assisted terahertz communications toward 6G,'' *IEEE Wireless Commun.*, vol. 28, no. 6, pp. 110–117, Dec. 2021.
- <span id="page-33-31"></span>[\[84\]](#page-16-4) C.-X. Wang, J. Wang, S. Hu, Z. H. Jiang, J. Tao, and F. Yan, ''Key technologies in 6G terahertz wireless communication systems: A survey,'' *IEEE Veh. Technol. Mag.*, vol. 16, no. 4, pp. 27–37, Dec. 2021.
- <span id="page-33-32"></span>[\[85\]](#page-16-5) W. Jiang, Q. Zhou, J. He, M. A. Habibi, S. Melnyk, M. El-Absi, B. Han, M. D. Renzo, H. D. Schotten, F.-L. Luo, T. S. El-Bawab, M. Juntti, M. Debbah, and V. C. M. Leung, ''Terahertz communications and sensing for 6G and beyond: A comprehensive review,'' *IEEE Commun. Surveys Tuts.*, vol. 26, pp. 2326–2381, 4th Quart., 2024.
- <span id="page-33-33"></span>[\[86\]](#page-16-6) M. Z. Chowdhury, Md. T. Hossan, A. Islam, and Y. M. Jang, ''A comparative survey of optical wireless technologies: Architectures and applications,'' *IEEE Access*, vol. 6, pp. 9819–9840, 2018.
- <span id="page-33-34"></span>[\[87\]](#page-16-7) A. S. Hamza, J. S. Deogun, and D. R. Alexander, ''Classification framework for free space optical communication links and systems,'' *IEEE Commun. Surveys Tuts.*, vol. 21, no. 2, pp. 1346–1382, 2nd Quart., 2019.
- <span id="page-33-35"></span>[\[88\]](#page-16-8) S. A. Al-Gailani, M. F. Mohd Salleh, A. A. Salem, R. Q. Shaddad, U. U. Sheikh, N. A. Algeelani, and T. A. Almohamad, ''A survey of free space optics (FSO) communication systems, links, and networks,'' *IEEE Access*, vol. 9, pp. 7353–7373, 2021.
- <span id="page-33-36"></span>[\[89\]](#page-16-9) N. Chi, Y. Zhou, Y. Wei, and F. Hu, ''Visible light communication in 6G: Advances, challenges, and prospects,'' *IEEE Veh. Technol. Mag.*, vol. 15, no. 4, pp. 93–102, Dec. 2020.
- <span id="page-33-37"></span>[\[90\]](#page-16-10) M. Z. Chowdhury, M. Shahjalal, M. K. Hasan, and Y. M. Jang, ''The role of optical wireless communication technologies in 5G/6G and IoT solutions: Prospects, directions, and challenges,'' *Appl. Sci.*, vol. 9, no. 20, p. 4367, Oct. 2019.
- <span id="page-33-38"></span>[\[91\]](#page-16-11) Z. Wei, Z. Wang, J. Zhang, Q. Li, J. Zhang, and H. Y. Fu, ''Evolution of optical wireless communication for B5G/6G,'' *Prog. Quantum Electron.*, vol. 83, May 2022, Art. no. 100398.
- <span id="page-33-39"></span>[\[92\]](#page-16-12) S. Naser, L. Bariah, S. Muhaidat, P. C. Sofotasios, M. Al-Qutayri, E. Damiani, and M. Debbah, ''Toward federated-learning-enabled visible light communication in 6G systems,'' *IEEE Wireless Commun.*, vol. 29, no. 1, pp. 48–56, Feb. 2022.
- <span id="page-33-40"></span>[\[93\]](#page-16-13) H.-B. Jeon, S.-M. Kim, H.-J. Moon, D.-H. Kwon, J.-W. Lee, J.- M. Chung, S.-K. Han, C.-B. Chae, and M.-S. Alouini, ''Free-space optical communications for 6G wireless networks: Challenges, opportunities, and prototype validation,'' *IEEE Commun. Mag.*, vol. 61, no. 4, pp. 116–121, Apr. 2023.
- <span id="page-33-41"></span>[\[94\]](#page-16-14) E. Björnson, L. Sanguinetti, H. Wymeersch, J. Hoydis, and T. L. Marzetta, ''Massive MIMO is a reality-what is next? Five promising research directions for antenna arrays,'' *Digit. Signal Process.*, vol. 94, pp. 3–20, Jul. 2019.

![](_page_34_Picture_1.jpeg)

- <span id="page-34-0"></span>[\[95\]](#page-16-15) I. F. Akyildiz and J. M. Jornet, ''Realizing ultra-massive MIMO(1024×1024)communication in the (0.06–10) terahertz band,'' *Nano Commun. Netw.*, vol. 8, pp. 46–54, Jun. 2016.
- <span id="page-34-1"></span>[\[96\]](#page-16-16) N. Shlezinger, G. C. Alexandropoulos, M. F. Imani, Y. C. Eldar, and D. R. Smith, ''Dynamic metasurface antennas for 6G extreme massive MIMO communications,'' *IEEE Wireless Commun.*, vol. 28, no. 2, pp. 106–113, Apr. 2021.
- <span id="page-34-2"></span>[\[97\]](#page-16-17) M. Cui, Z. Wu, Y. Lu, X. Wei, and L. Dai, ''Near-field MIMO communications for 6G: Fundamentals, challenges, potentials, and future directions,'' *IEEE Commun. Mag.*, vol. 61, no. 1, pp. 40–46, Jan. 2023.
- <span id="page-34-3"></span>[\[98\]](#page-17-2) H. Lu, Y. Zeng, C. You, Y. Han, J. Zhang, Z. Wang, Z. Dong, S. Jin, C.-X. Wang, T. Jiang, X. You, and R. Zhang, ''A tutorial on near-field XL-MIMO communications toward 6G,'' *IEEE Commun. Surveys Tuts.*, vol. 26, pp. 2213–2257, 4th Quart., 2024.
- <span id="page-34-4"></span>[\[99\]](#page-17-3) E. Basar, M. D. Renzo, J. D. Rosny, M. Debbah, M.-S. Alouini, and R. Zhang, ''Wireless communications through reconfigurable intelligent surfaces,'' *IEEE Access*, vol. 7, pp. 116753–116773, 2019.
- <span id="page-34-5"></span>[\[100\]](#page-17-4) C. Pan, H. Ren, K. Wang, J. F. Kolb, M. Elkashlan, M. Chen, M. D. Renzo, Y. Hao, J. Wang, A. L. Swindlehurst, X. You, and L. Hanzo, ''Reconfigurable intelligent surfaces for 6G systems: Principles, applications, and research directions,'' *IEEE Commun. Mag.*, vol. 59, no. 6, pp. 14–20, Jun. 2021.
- <span id="page-34-6"></span>[\[101\]](#page-17-5) E. Basar and H. V. Poor, ''Present and future of reconfigurable intelligent surface-empowered communications [perspectives],'' *IEEE Signal Process. Mag.*, vol. 38, no. 6, pp. 146–152, Nov. 2021.
- <span id="page-34-7"></span>[\[102\]](#page-17-6) C. Huang, S. Hu, G. C. Alexandropoulos, A. Zappone, C. Yuen, R. Zhang, M. D. Renzo, and M. Debbah, ''Holographic MIMO surfaces for 6G wireless networks: Opportunities, challenges, and trends,'' *IEEE Wireless Commun.*, vol. 27, no. 5, pp. 118–125, Oct. 2020.
- <span id="page-34-8"></span>[\[103\]](#page-17-7) T. Gong, P. Gavriilidis, R. Ji, C. Huang, G. C. Alexandropoulos, L. Wei, Z. Zhang, M. Debbah, H. V. Poor, and C. Yuen, ''Holographic MIMO communications: Theoretical foundations, enabling technologies, and future directions,'' *IEEE Commun. Surveys Tuts.*, vol. 26, no. 1, pp. 196–257, 1st Quart., 2024.
- <span id="page-34-9"></span>[\[104\]](#page-17-8) J. An, C. Yuen, C. Huang, M. Debbah, H. Vincent Poor, and L. Hanzo, ''A tutorial on holographic MIMO communications—Part I: Channel modeling and channel estimation,'' *IEEE Commun. Lett.*, vol. 27, no. 7, pp. 1664–1668, Jul. 2023.
- <span id="page-34-10"></span>[\[105\]](#page-17-9) J. An, C. Yuen, C. Huang, M. Debbah, H. V. Poor, and L. Hanzo, ''A tutorial on holographic MIMO communications—Part II: Performance analysis and holographic beamforming,'' *IEEE Commun. Lett.*, vol. 27, no. 7, pp. 1669–1673, Jul. 2023.
- <span id="page-34-11"></span>[\[106\]](#page-18-0) P. Guan, D. Wu, T. Tian, J. Zhou, X. Zhang, L. Gu, A. Benjebbour, M. Iwabuchi, and Y. Kishiyama, ''5G field trials: OFDM-based waveforms and mixed numerologies,'' *IEEE J. Sel. Areas Commun.*, vol. 35, no. 6, pp. 1234–1243, Jun. 2017.
- <span id="page-34-12"></span>[\[107\]](#page-18-1) M. Sarajlić, N. Tervo, A. Pärssinen, L. H. Nguyen, H. Halbauer, K. Roth, V. Kumar, T. Svensson, A. Nimr, S. Zeitz, M. Dörpinghaus, and G. Fettweis, ''Waveforms for sub-THz 6G: Design guidelines,'' in *Proc. Joint Eur. Conf. Netw. Commun. 6G Summit (EuCNC/6G Summit)*, Jun. 2023, pp. 168–173.
- <span id="page-34-13"></span>[\[108\]](#page-18-2) C. Yue, V. Miloslavskaya, M. Shirvanimoghaddam, B. Vucetic, and Y. Li, ''Efficient decoders for short block length codes in 6G URLLC,'' *IEEE Commun. Mag.*, vol. 61, no. 4, pp. 84–90, Apr. 2023.
- <span id="page-34-14"></span>[\[109\]](#page-18-3) P. K. Singya, P. Shaik, N. Kumar, V. Bhatia, and M.-S. Alouini, ''A survey on higher-order QAM constellations: Technical challenges, recent advances, and future trends,'' *IEEE Open J. Commun. Soc.*, vol. 2, pp. 617–655, 2021.
- <span id="page-34-15"></span>[\[110\]](#page-19-2) B. Makki, K. Chitti, A. Behravan, and M.-S. Alouini, ''A survey of NOMA: Current status and open research challenges,'' *IEEE Open J. Commun. Soc.*, vol. 1, pp. 179–189, 2020.
- <span id="page-34-16"></span>[\[111\]](#page-19-3) M. B. Shahab, R. Abbas, M. Shirvanimoghaddam, and S. J. Johnson, ''Grant-free non-orthogonal multiple access for IoT: A survey,'' *IEEE Commun. Surveys Tuts.*, vol. 22, no. 3, pp. 1805–1838, 3rd Quart., 2020.
- <span id="page-34-17"></span>[\[112\]](#page-19-4) I. Budhiraja, N. Kumar, S. Tyagi, S. Tanwar, Z. Han, M. J. Piran, and D. Y. Suh, ''A systematic review on NOMA variants for 5G and beyond,'' *IEEE Access*, vol. 9, pp. 85573–85644, 2021.
- <span id="page-34-18"></span>[\[113\]](#page-19-5) J. Choi, J. Ding, N.-P. Le, and Z. Ding, ''Grant-free random access in machine-type communication: Approaches and challenges,'' *IEEE Wireless Commun.*, vol. 29, no. 1, pp. 151–158, Feb. 2022.

- <span id="page-34-19"></span>[\[114\]](#page-20-1) Z. Gao, M. Ke, Y. Mei, L. Qiao, S. Chen, D. W. K. Ng, and H. V. Poor, ''Compressive-Sensing-Based grant-free massive access for 6G massive communication,'' *IEEE Internet Things J.*, vol. 11, no. 5, pp. 7411–7435, Mar. 2024.
- <span id="page-34-20"></span>[\[115\]](#page-20-2) J. Liu, Y. Shi, Z. Md. Fadlullah, and N. Kato, ''Space-air-ground integrated network: A survey,'' *IEEE Commun. Surveys Tuts.*, vol. 20, no. 4, pp. 2714–2741, 4th Quart., 2018.
- <span id="page-34-21"></span>[\[116\]](#page-20-3) M. M. Azari, S. Solanki, S. Chatzinotas, O. Kodheli, H. Sallouha, A. Colpaert, J. F. Mendoza Montoya, S. Pollin, A. Haqiqatnejad, A. Mostaani, E. Lagunas, and B. Ottersten, ''Evolution of non-terrestrial networks from 5G to 6G: A survey,'' *IEEE Commun. Surveys Tuts.*, vol. 24, no. 4, pp. 2633–2672, 4th Quart., 2022.
- <span id="page-34-22"></span>[\[117\]](#page-20-4) G. Araniti, A. Iera, S. Pizzi, and F. Rinaldi, ''Toward 6G non-terrestrial networks,'' *IEEE Netw.*, vol. 36, no. 1, pp. 113–120, Jan. 2022.
- <span id="page-34-23"></span>[\[118\]](#page-20-5) M. Giordani and M. Zorzi, ''Non-terrestrial networks in the 6G era: Challenges and opportunities,'' *IEEE Netw.*, vol. 35, no. 2, pp. 244–251, Mar. 2021.
- <span id="page-34-24"></span>[\[119\]](#page-20-6) A. Iqbal, M.-L. Tham, Y. J. Wong, A. Al-Habashna, G. Wainer, Y. X. Zhu, and T. Dagiuklas, ''Empowering non-terrestrial networks with artificial intelligence: A survey,'' *IEEE Access*, vol. 11, pp. 100986–101006, 2023.
- <span id="page-34-25"></span>[\[120\]](#page-20-7) S. Mahboob and L. Liu, ''Revolutionizing future connectivity: A contemporary survey on AI-empowered satellite-based non-terrestrial networks in 6G,'' *IEEE Commun. Surveys Tuts.*, vol. 26, no. 2, pp. 1279–1321, 2nd Quart., 2024.
- <span id="page-34-26"></span>[\[121\]](#page-20-8) V. Stoynov, V. Poulkov, Z. Valkova-Jarvis, G. Iliev, and P. Koleva, ''Ultradense networks: Taxonomy and key performance indicators,'' *Symmetry*, vol. 15, no. 1, p. 2, Dec. 2022.
- <span id="page-34-27"></span>[\[122\]](#page-20-9) A. Mughees, M. Tahir, M. A. Sheikh, and A. Ahad, ''Energy-efficient ultra-dense 5G networks: Recent advances, taxonomy and future research directions,'' *IEEE Access*, vol. 9, pp. 147692–147716, 2021.
- <span id="page-34-28"></span>[\[123\]](#page-20-10) M. A. Adedoyin and O. E. Falowo, ''Combination of ultra-dense networks and other 5G enabling technologies: A survey,'' *IEEE Access*, vol. 8, pp. 22893–22932, 2020.
- <span id="page-34-29"></span>[\[124\]](#page-20-11) B. T. Tinh, L. D. Nguyen, H. H. Kha, and T. Q. Duong, ''Practical optimization and game theory for 6G ultra-dense networks: Overview and research challenges,'' *IEEE Access*, vol. 10, pp. 13311–13328, 2022.
- <span id="page-34-30"></span>[\[125\]](#page-21-1) Y. Zhang, M. A. Kishk, and M.-S. Alouini, ''A survey on integrated access and backhaul networks,'' *Frontiers Commun. Netw.*, vol. 2, Jun. 2021, Art. no. 647284.
- <span id="page-34-31"></span>[\[126\]](#page-21-2) C. Madapatha, B. Makki, C. Fang, O. Teyeb, E. Dahlman, M.-S. Alouini, and T. Svensson, ''On integrated access and backhaul networks: Current status and potentials,'' *IEEE Open J. Commun. Soc.*, vol. 1, pp. 1374–1389, 2020.
- <span id="page-34-32"></span>[\[127\]](#page-21-3) M. Polese, M. Giordani, T. Zugno, A. Roy, S. Goyal, D. Castor, and M. Zorzi, ''Integrated access and backhaul in 5G mmWave networks: Potential and challenges,'' *IEEE Commun. Mag.*, vol. 58, no. 3, pp. 62–68, Mar. 2020.
- <span id="page-34-33"></span>[\[128\]](#page-21-4) W. Lei, Y. Ye, and M. Xiao, ''Deep reinforcement learning-based spectrum allocation in integrated access and backhaul networks,'' *IEEE Trans. Cognit. Commun. Netw.*, vol. 6, no. 3, pp. 970–979, Sep. 2020.
- <span id="page-34-34"></span>[\[129\]](#page-21-5) Ö. T. Demir, E. Björnson, and L. Sanguinetti, ''Foundations of usercentric cell-free massive MIMO,'' *Found. Trends Signal Process.*, vol. 14, nos. 3–4, pp. 162–472, 2021.
- <span id="page-34-35"></span>[\[130\]](#page-21-6) E. Björnson and L. Sanguinetti, ''Scalable cell-free massive MIMO systems,'' *IEEE Trans. Commun.*, vol. 68, no. 7, pp. 4247–4261, Jul. 2020.
- <span id="page-34-36"></span>[\[131\]](#page-21-7) H. Q. Ngo, A. Ashikhmin, H. Yang, E. G. Larsson, and T. L. Marzetta, ''Cell-free massive MIMO versus small cells,'' *IEEE Trans. Wireless Commun.*, vol. 16, no. 3, pp. 1834–1850, Mar. 2017.
- <span id="page-34-37"></span>[\[132\]](#page-21-8) S. Elhoushy, M. Ibrahim, and W. Hamouda, ''Cell-free massive MIMO: A survey,'' *IEEE Commun. Surveys Tuts.*, vol. 24, no. 1, pp. 492–523, 1st Quart., 2022.
- <span id="page-34-38"></span>[\[133\]](#page-21-9) H. A. Ammar, R. Adve, S. Shahbazpanahi, G. Boudreau, and K. V. Srinivas, ''User-centric cell-free massive MIMO networks: A survey of opportunities, challenges and solutions,'' *IEEE Commun. Surveys Tuts.*, vol. 24, no. 1, pp. 611–652, 1st Quart., 2022.
- <span id="page-34-39"></span>[\[134\]](#page-21-10) H. He, X. Yu, J. Zhang, S. Song, and K. B. Letaief, ''Cell-free massive MIMO for 6G wireless communication networks,'' *J. Commun. Inf. Netw.*, vol. 6, no. 4, pp. 321–335, Dec. 2021.
- <span id="page-34-40"></span>[\[135\]](#page-21-11) F. Tang, B. Mao, Y. Kawamoto, and N. Kato, ''Survey on machine learning for intelligent end-to-end communication toward 6G: From network access, routing to traffic control and streaming adaption,'' *IEEE Commun. Surveys Tuts.*, vol. 23, no. 3, pp. 1578–1598, 3rd Quart., 2021.

![](_page_35_Picture_1.jpeg)

- <span id="page-35-0"></span>[\[136\]](#page-21-12) H. M. F. Noman, E. Hanafi, K. A. Noordin, K. Dimyati, M. N. Hindia, A. Abdrabou, and F. Qamar, ''Machine learning empowered emerging wireless networks in 6G: Recent advancements, challenges and future trends,'' *IEEE Access*, vol. 11, pp. 83017–83051, 2023.
- <span id="page-35-1"></span>[\[137\]](#page-21-13) J. Xie, F. R. Yu, T. Huang, R. Xie, J. Liu, C. Wang, and Y. Liu, ''A survey of machine learning techniques applied to software defined networking (SDN): Research issues and challenges,'' *IEEE Commun. Surveys Tuts.*, vol. 21, no. 1, pp. 393–430, 1st Quart., 2019.
- <span id="page-35-2"></span>[\[138\]](#page-21-14) M. Chen, U. Challita, W. Saad, C. Yin, and M. Debbah, ''Artificial neural networks-based machine learning for wireless networks: A tutorial,'' *IEEE Commun. Surveys Tuts.*, vol. 21, no. 4, pp. 3039–3071, 4th Quart., 2019.
- <span id="page-35-3"></span>[\[139\]](#page-21-15) W. Wu, C. Zhou, M. Li, H. Wu, H. Zhou, N. Zhang, X. S. Shen, and W. Zhuang, ''AI-native network slicing for 6G networks,'' *IEEE Wireless Commun.*, vol. 29, no. 1, pp. 96–103, Feb. 2022.
- <span id="page-35-4"></span>[\[140\]](#page-21-16) F. Zhou, W. Li, Y. Yang, L. Feng, P. Yu, M. Zhao, X. Yan, and J. Wu, ''Intelligence-endogenous networks: Innovative network paradigm for 6G,'' *IEEE Wireless Commun.*, vol. 29, no. 1, pp. 40–47, Feb. 2022.
- <span id="page-35-5"></span>[\[141\]](#page-21-17) A. Alhammadi, I. Shayea, A. A. El-Saleh, M. H. Azmi, Z. H. Ismail, L. Kouhalvandi, and S. A. Saad, ''Artificial intelligence in 6G wireless networks: Opportunities, applications, and challenges,'' *Int. J. Intell. Syst.*, vol. 2024, Mar. 2024, Art. no. 8845070.
- <span id="page-35-6"></span>[\[142\]](#page-22-2) S. Deng, H. Zhao, W. Fang, J. Yin, S. Dustdar, and A. Y. Zomaya, ''Edge intelligence: The confluence of edge computing and artificial intelligence,'' *IEEE Internet Things J.*, vol. 7, no. 8, pp. 7457–7469, Aug. 2020.
- <span id="page-35-7"></span>[\[143\]](#page-22-3) Y. Xiao, G. Shi, Y. Li, W. Saad, and H. V. Poor, ''Toward selflearning edge intelligence in 6G,'' *IEEE Commun. Mag.*, vol. 58, no. 12, pp. 34–40, Dec. 2020.
- <span id="page-35-8"></span>[\[144\]](#page-23-0) J. Hoydis, F. A. Aoudia, A. Valcarce, and H. Viswanathan, ''Toward a 6G AI-native air interface,'' *IEEE Commun. Mag.*, vol. 59, no. 5, pp. 76–81, May 2021.
- <span id="page-35-9"></span>[\[145\]](#page-23-1) S. Han, T. Xie, I. Chih-Lin, L. Chai, Z. Liu, Y. Yuan, and C. Cui, ''Artificial-intelligence-enabled air interface for 6G: Solutions, challenges, and standardization impacts,'' *IEEE Commun. Mag.*, vol. 58, no. 10, pp. 73–79, Oct. 2020.
- <span id="page-35-10"></span>[\[146\]](#page-23-2) F. Restuccia and T. Melodia, ''Deep learning at the physical layer: System challenges and applications to 5G and beyond,'' *IEEE Commun. Mag.*, vol. 58, no. 10, pp. 58–64, Oct. 2020.
- <span id="page-35-11"></span>[\[147\]](#page-24-2) B. Mao, F. Tang, Y. Kawamoto, and N. Kato, ''AI models for green communications towards 6G,'' *IEEE Commun. Surveys Tuts.*, vol. 24, no. 1, pp. 210–247, 1st Quart., 2022.
- <span id="page-35-12"></span>[\[148\]](#page-24-3) S. Han, T. Xie, and I. Chih-Lin, ''Greener physical layer technologies for 6G mobile communications,'' *IEEE Commun. Mag.*, vol. 59, no. 4, pp. 68–74, Apr. 2021.
- <span id="page-35-13"></span>[\[149\]](#page-24-4) L. M. P. Larsen, H. L. Christiansen, S. Ruepp, and M. S. Berger, ''Toward greener 5G and beyond radio access Networks—A survey,'' *IEEE Open J. Commun. Soc.*, vol. 4, pp. 768–797, 2023.
- <span id="page-35-14"></span>[\[150\]](#page-24-5) T. Huang, W. Yang, J. Wu, J. Ma, X. Zhang, and D. Zhang, ''A survey on green 6G network: Architecture and technologies,'' *IEEE Access*, vol. 7, pp. 175758–175768, 2019.
- <span id="page-35-15"></span>[\[151\]](#page-24-6) A. A. G. Amer, S. Z. Sapuan, N. Nasimuddin, A. Alphones, and N. B. Zinal, ''A comprehensive review of metasurface structures suitable for RF energy harvesting,'' *IEEE Access*, vol. 8, pp. 76433–76452, 2020.
- <span id="page-35-16"></span>[\[152\]](#page-24-7) H. Rahmani, D. Shetty, M. Wagih, Y. Ghasempour, V. Palazzi, N. B. Carvalho, R. Correia, A. Costanzo, D. Vital, F. Alimenti, J. Kettle, D. Masotti, P. Mezzanotte, L. Roselli, and J. Grosinger, ''Next-generation IoT devices: Sustainable eco-friendly manufacturing, energy harvesting, and wireless connectivity,'' *IEEE J. Microw.*, vol. 3, no. 1, pp. 237–255, Jan. 2023.
- <span id="page-35-17"></span>[\[153\]](#page-24-8) A. J. Williams, M. F. Torquato, I. M. Cameron, A. A. Fahmy, and J. Sienz, ''Survey of energy harvesting technologies for wireless sensor networks,'' *IEEE Access*, vol. 9, pp. 77493–77510, 2021.
- <span id="page-35-18"></span>[\[154\]](#page-24-9) T. Sanislav, G. D. Mois, S. Zeadally, and S. C. Folea, ''Energy harvesting techniques for Internet of Things (IoT),'' *IEEE Access*, vol. 9, pp. 39530–39549, 2021.
- <span id="page-35-19"></span>[\[155\]](#page-24-10) R. Duan, X. Wang, H. Yigitler, M. U. Sheikh, R. Jantti, and Z. Han, ''Ambient backscatter communications for future ultra-low-power machine type communications: Challenges, solutions, opportunities, and future research trends,'' *IEEE Commun. Mag.*, vol. 58, no. 2, pp. 42–47, Feb. 2020.

- <span id="page-35-20"></span>[\[156\]](#page-24-11) S. J. Nawaz, S. K. Sharma, B. Mansoor, M. N. Patwary, and N. M. Khan, ''Non-coherent and backscatter communications: Enabling ultra-massive connectivity in 6G wireless networks,'' *IEEE Access*, vol. 9, pp. 38144–38186, 2021.
- <span id="page-35-21"></span>[\[157\]](#page-24-12) C. Xu, L. Yang, and P. Zhang, ''Practical backscatter communication systems for battery-free Internet of Things: A tutorial and survey of recent research,'' *IEEE Signal Process. Mag.*, vol. 35, no. 5, pp. 16–27, Sep. 2018.
- <span id="page-35-22"></span>[\[158\]](#page-25-0) M. Ahmed, M. Shahwar, F. Khan, W. U. Khan, A. Ihsan, U. S. Khan, F. Xu, and S. Chatzinotas, ''NOMA-based backscatter communications: Fundamentals, applications, and advancements,'' *IEEE Internet Things J.*, vol. 11, no. 11, pp. 19303–19327, Jun. 2024.
- <span id="page-35-23"></span>[\[159\]](#page-25-1) F. Jameel, Z. Hamid, F. Jabeen, S. Zeadally, and M. A. Javed, ''A survey of device-to-device communications: Research issues and challenges,'' *IEEE Commun. Surveys Tuts.*, vol. 20, no. 3, pp. 2133–2168, 3rd Quart., 2018.
- <span id="page-35-24"></span>[\[160\]](#page-25-2) M. S. M. Gismalla, A. I. Azmi, M. R. B. Salim, M. F. L. Abdullah, F. Iqbal, W. A. Mabrouk, M. B. Othman, A. Y. I. Ashyap, and A. S. M. Supa'at, ''Survey on device to device (D2D) communication for 5GB/6G networks: Concept, applications, challenges, and future directions,'' *IEEE Access*, vol. 10, pp. 30792–30821, 2022.
- <span id="page-35-25"></span>[\[161\]](#page-25-3) P. Mach and Z. Becvar, ''Device-to-device relaying: Optimization, performance perspectives, and open challenges towards 6G networks,'' *IEEE Commun. Surveys Tuts.*, vol. 24, no. 3, pp. 1336–1393, 3rd Quart., 2022.
- <span id="page-35-26"></span>[\[162\]](#page-25-4) M. A. Areqi, A. T. Zahary, and M. N. Ali, ''State-of-the-art device-to-device communication solutions,'' *IEEE Access*, vol. 11, pp. 46734–46764, 2023.
- <span id="page-35-27"></span>[\[163\]](#page-25-5) T. Rathod and S. Tanwar, ''AI-based resource allocation techniques in D2D communication: Open issues and future directions,'' *Phys. Commun.*, vol. 66, Oct. 2024, Art. no. 102423.
- <span id="page-35-28"></span>[\[164\]](#page-25-6) H. Bagheri, M. Noor-A-Rahim, Z. Liu, H. Lee, D. Pesch, K. Moessner, and P. Xiao, ''5G NR-V2X: Toward connected and cooperative autonomous driving,'' *IEEE Commun. Standards Mag.*, vol. 5, no. 1, pp. 48–54, Mar. 2021.
- <span id="page-35-29"></span>[\[165\]](#page-25-7) M. H. C. Garcia, A. Molina-Galan, M. Boban, J. Gozalvez, B. Coll-Perales, T. Sahin, and A. Kousaridas, ''A tutorial on 5G NR V2X communications,'' *IEEE Commun. Surveys Tuts.*, vol. 23, no. 3, pp. 1972–2026, 3rd Quart., 2021.
- <span id="page-35-30"></span>[\[166\]](#page-25-8) Annu and P. Rajalakshmi, ''Towards 6G V2X sidelink: Survey of resource allocation—Mathematical formulations, challenges, and proposed solutions,'' *IEEE Open J. Veh. Technol.*, vol. 5, pp. 344–383, 2024.
- <span id="page-35-31"></span>[\[167\]](#page-25-9) S. Roger, C. Botella-Mascarell, D. Martín-Sacristán, D. García-Roger, J. F. Monserrat, and T. Svensson, ''Sustainable mobility in B5G/6G: V2X technology trends and use cases,'' *IEEE Open J. Veh. Technol.*, vol. 5, pp. 459–472, 2024.
- <span id="page-35-32"></span>[\[168\]](#page-25-10) S. Zhang, H. Zhang, and L. Song, ''Beyond D2D: Full dimension UAV-toeverything communications in 6G,'' *IEEE Trans. Veh. Technol.*, vol. 69, no. 6, pp. 6592–6602, Jun. 2020.
- <span id="page-35-33"></span>[\[169\]](#page-25-11) Y. Zeng, J. Lyu, and R. Zhang, ''Cellular-connected UAV: Potential, challenges, and promising technologies,'' *IEEE Wireless Commun.*, vol. 26, no. 1, pp. 120–127, Feb. 2019.
- <span id="page-35-34"></span>[\[170\]](#page-25-12) A. Fotouhi, H. Qiang, M. Ding, M. Hassan, L. G. Giordano, A. Garcia-Rodriguez, and J. Yuan, ''Survey on UAV cellular communications: Practical aspects, standardization advancements, regulation, and security challenges,'' *IEEE Commun. Surveys Tuts.*, vol. 21, no. 4, pp. 3417–3442, 4th Quart., 2019.
- <span id="page-35-35"></span>[\[171\]](#page-26-2) G. Geraci, A. Garcia-Rodriguez, M. M. Azari, A. Lozano, M. Mezzavilla, S. Chatzinotas, Y. Chen, S. Rangan, and M. D. Renzo, ''What will the future of UAV cellular communications be? A flight from 5G to 6G,'' *IEEE Commun. Surveys Tuts.*, vol. 24, no. 3, pp. 1304–1335, 3rd Quart., 2022.
- <span id="page-35-36"></span>[\[172\]](#page-26-3) B. P. S. Sahoo, D. Puthal, and P. K. Sharma, ''Toward advanced UAV communications: Properties, research challenges, and future potential,'' *IEEE Internet Things Mag.*, vol. 5, no. 1, pp. 154–159, Mar. 2022.
- <span id="page-35-37"></span>[\[173\]](#page-26-4) M. Wen, Q. Li, K. J. Kim, D. López-Pérez, O. A. Dobre, H. V. Poor, P. Popovski, and T. A. Tsiftsis, ''Private 5G networks: Concepts, architectures, and research landscape,'' *IEEE J. Sel. Topics Signal Process.*, vol. 16, no. 1, pp. 7–25, Jan. 2022.
- <span id="page-35-38"></span>[\[174\]](#page-26-5) S. Guo, B. Lu, M. Wen, S. Dang, and N. Saeed, ''Customized 5G and beyond private networks with integrated URLLC, eMBB, mMTC, and positioning for industrial verticals,'' *IEEE Commun. Standards Mag.*, vol. 6, no. 1, pp. 52–57, Mar. 2022.

![](_page_36_Picture_1.jpeg)

- <span id="page-36-0"></span>[\[175\]](#page-26-6) S. Eswaran and P. Honnavalli, ''Private 5G networks: A survey on enabling technologies, deployment models, use cases and research directions,'' *Telecommun. Syst.*, vol. 82, no. 1, pp. 3–26, Jan. 2023.
- <span id="page-36-1"></span>[\[176\]](#page-27-0) P. Porambage, G. Gür, D. P. M. Osorio, M. Liyanage, A. Gurtov, and M. Ylianttila, ''The roadmap to 6G security and privacy,'' *IEEE Open J. Commun. Soc.*, vol. 2, pp. 1094–1122, 2021.
- <span id="page-36-2"></span>[\[177\]](#page-27-1) V. Ziegler, P. Schneider, H. Viswanathan, M. Montag, S. Kanugovi, and A. Rezaki, ''Security and trust in the 6G era,'' *IEEE Access*, vol. 9, pp. 142314–142327, 2021.
- <span id="page-36-3"></span>[\[178\]](#page-27-2) V.-L. Nguyen, P.-C. Lin, B.-C. Cheng, R.-H. Hwang, and Y.-D. Lin, ''Security and privacy for 6G: A survey on prospective technologies and challenges,'' *IEEE Commun. Surveys Tuts.*, vol. 23, no. 4, pp. 2384–2428, 4th Quart., 2021.
- <span id="page-36-4"></span>[\[179\]](#page-27-3) Y. Sun, J. Liu, J. Wang, Y. Cao, and N. Kato, ''When machine learning meets privacy in 6G: A survey,'' *IEEE Commun. Surveys Tuts.*, vol. 22, no. 4, pp. 2694–2724, 4th Quart., 2020.
- <span id="page-36-5"></span>[\[180\]](#page-27-4) H. Sedjelmaci, K. Tourki, and N. Ansari, ''Enabling 6G security: The synergy of zero trust architecture and artificial intelligence,'' *IEEE Netw.*, vol. 38, no. 3, pp. 171–177, May 2024.
- <span id="page-36-6"></span>[\[181\]](#page-27-5) S. Zhang, D. Zhu, and Y. Liu, ''Artificial intelligence empowered physical layer security for 6G: State-of-the-art, challenges, and opportunities,'' *Comput. Netw.*, vol. 242, Apr. 2024, Art. no. 110255.
- <span id="page-36-7"></span>[\[182\]](#page-0-1) R.-F. Liao, H. Wen, J. Wu, F. Pan, A. Xu, H. Song, F. Xie, Y. Jiang, and M. Cao, ''Security enhancement for mobile edge computing through physical layer authentication,'' *IEEE Access*, vol. 7, pp. 116390–116401, 2019.
- <span id="page-36-8"></span>[\[183\]](#page-0-1) X. Qiu, Z. Du, and X. Sun, ''Artificial intelligence-based security authentication: Applications in wireless multimedia networks,'' *IEEE Access*, vol. 7, pp. 172004–172011, 2019.
- <span id="page-36-9"></span>[\[184\]](#page-0-1) R.-F. Liao, H. Wen, J. Wu, F. Pan, A. Xu, Y. Jiang, F. Xie, and M. Cao, ''Deep-Learning-Based physical layer authentication for industrial wireless sensor networks,'' *Sensors*, vol. 19, no. 11, p. 2440, May 2019.
- <span id="page-36-10"></span>[\[185\]](#page-0-1) G. Han, L. Xiao, and H. V. Poor, ''Two-dimensional anti-jamming communication based on deep reinforcement learning,'' in *Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP)*, Mar. 2017, pp. 2087–2091.
- <span id="page-36-11"></span>[\[186\]](#page-0-1) X. Liu, Y. Xu, L. Jia, Q. Wu, and A. Anpalagan, ''Anti-jamming communications using spectrum waterfall: A deep reinforcement learning approach,'' *IEEE Commun. Lett.*, vol. 22, no. 5, pp. 998–1001, May 2018.
- <span id="page-36-12"></span>[\[187\]](#page-0-1) Y. Bi, Y. Wu, and C. Hua, ''Deep reinforcement learning based multiuser anti-jamming strategy,'' in *Proc. IEEE Int. Conf. Commun. (ICC)*, May 2019, pp. 1–6.
- <span id="page-36-13"></span>[\[188\]](#page-0-1) R. Fritschek, R. F. Schaefer, and G. Wunder, ''Deep learning for the Gaussian wiretap channel,'' in *Proc. IEEE Int. Conf. Commun. (ICC)*, May 2019, pp. 1–6.
- <span id="page-36-14"></span>[\[189\]](#page-0-1) Z. Sun, H. Wu, C. Zhao, and G. Yue, ''End-to-end learning of secure wireless communications: Confidential transmission and authentication,'' *IEEE Wireless Commun.*, vol. 27, no. 5, pp. 88–95, Oct. 2020.
- [\[190\]](#page-0-1) K.-L. Besser, P.-H. Lin, C. R. Janda, and E. A. Jorswieck, ''Wiretap code design by neural network autoencoders,'' *IEEE Trans. Inf. Forensics Security*, vol. 15, pp. 3374–3386, 2020.
- <span id="page-36-15"></span>[\[191\]](#page-29-1) A. Shokrollahi, ''Raptor codes,'' *IEEE Trans. Inf. Theory*, vol. 52, no. 6, pp. 2551–2567, Jun. 2006.
- <span id="page-36-16"></span>[\[192\]](#page-29-2) R. Zamir, *Lattice Coding for Signals and Networks: A Structured Coding Approach To Quantization, Modulation, and Multiuser Information Theory*. Cambridge, U.K.: Cambridge Univ. Press, 2014.
- <span id="page-36-17"></span>[\[193\]](#page-29-3) E. Agrell, T. Eriksson, A. Vardy, and K. Zeger, ''Closest point search in lattices,'' *IEEE Trans. Inf. Theory*, vol. 48, no. 8, pp. 2201–2214, Aug. 2002.
- <span id="page-36-18"></span>[\[194\]](#page-29-4) A. Joseph and A. R. Barron, ''Least squares superposition codes of moderate dictionary size are reliable at rates up to capacity,'' *IEEE Trans. Inf. Theory*, vol. 58, no. 5, pp. 2541–2557, May 2012.
- <span id="page-36-19"></span>[\[195\]](#page-29-5) C. Rush, K. Hsieh, and R. Venkataramanan, ''Capacity-achieving spatially coupled sparse superposition codes with AMP decoding,'' *IEEE Trans. Inf. Theory*, vol. 67, no. 7, pp. 4446–4484, Jul. 2021.
- <span id="page-36-20"></span>[\[196\]](#page-29-6) A. Fengler, P. Jung, and G. Caire, ''SPARCs for unsourced random access,'' *IEEE Trans. Inf. Theory*, vol. 67, no. 10, pp. 6894–6915, Oct. 2021.

- <span id="page-36-21"></span>[\[197\]](#page-29-7) T. Stockhammer, A. Shokrollahi, M. Watson, M. Luby, and T. Gasiba, ''Application layer forward error correction for mobile multimedia broadcasting,'' in *Handbook of Mobile Broadcasting*. New York, NY, USA: Auerbach Publications, 2008, pp. 239–278.
- <span id="page-36-22"></span>[\[198\]](#page-29-8) D. Gomez-Barquero, D. Gozalvez, and N. Cardona, ''Application layer FEC for mobile TV delivery in IP datacast over DVB-H systems,'' *IEEE Trans. Broadcast.*, vol. 55, no. 2, pp. 396–406, Jun. 2009.
- <span id="page-36-23"></span>[\[199\]](#page-29-9) M. Sandell and U. Raza, ''Application layer coding for IoT: Benefits, limitations, and implementation aspects,'' *IEEE Syst. J.*, vol. 13, no. 1, pp. 554–561, Mar. 2019.
- <span id="page-36-24"></span>[\[200\]](#page-29-10) D. Hou, K. Zhao, and W. Li, ''Application layer channel coding for space DTN,'' in *Proc. Int. Conf. Mach. Learn. Intell. Commun.* Cham, Switzerland: Springer, 2017, pp. 347–354.

![](_page_36_Picture_28.jpeg)

SIVARAMA PRASAD TERA received the B.Tech. degree in electronics and communication engineering from Jawaharlal Nehru Technological University, Kakinada, India, and the M.Tech. degree in digital systems from NIT Allahabad, India. He was an Assistant Professor at KLU University, Vijayawada, India. He is currently a Research Scholar with the Department of Electronics and Electrical Engineering, IIT Guwahati, India. His research interests include machine

learning, deep learning, communication systems, and VLSI.

![](_page_36_Picture_31.jpeg)

RAVIKUMAR CHINTHAGINJALA received the M.Tech. degree in digital electronics and communication systems from Jawaharlal Nehru Technology University, Anantapur, and the Ph.D. degree in communication networks from Vellore Institute of Technology, India, in 2018. He is currently an Associate Professor at the School of Electronics Engineering, Department of Embedded Technology, Vellore Institute of Technology. His current research interests include communication

networks, machine learning, deep learning, wireless sensor networks, and information security.

![](_page_36_Picture_34.jpeg)

GIOVANNI PAU (Senior Member, IEEE) received the bachelor's degree in telematic engineering from the University of Catania, Italy, and the master's degree (cum laude) in telematic engineering and the Ph.D. degree from the Kore University of Enna, Italy. He is currently an Associate Professor with the Faculty of Engineering and Architecture, Kore University of Enna. He is the author/co-author of more than 80 refereed articles published in journals and conference proceedings.

His research interests include wireless sensor networks, fuzzy logic controllers, and intelligent transportation systems. He is a member of the IEEE (Italy Section) and has been involved in several international conferences as the session co-chair and technical program committee member. He serves/served as a leading guest editor in special issues for several international journals. He is an Editorial Board Member and an Associate Editor of several journals, such as IEEE ACCESS, *Wireless Networks* (Springer), *EURASIP Journal on Wireless Communications and Networking* (Springer), *Wireless Communications and Mobile Computing* (Hindawi), *Sensors* (MDPI), and *Future Internet* (MDPI).

TAE HOON KIM, photograph and biography not available at the time of publication.

Open Access funding provided by 'Università degli Studi di Enna "KORE"' within the CRUI CARE Agreement
# Routing, Modulation Level and Spectrum Allocation in EONs via Genetic Algorithm Under Different Assignment Criteria

Rafael Marques, Lisandro Lovisolo, Marcelo G. Rubinstein *Postgraduate Program in Electronic Engineering (PEL) Rio de Janeiro State University (UERJ)* Rio de Janeiro, Brazil rafael.amc97@outlook.com, lisandro@uerj.br, rubi@uerj.br

*Abstract*—This work investigates the impact of ordering the demands using different criteria when a Genetic Algorithm (GA) is used to solve the Routing, Modulation Level, and Spectrum Assignment (RMLSA) problem in Elastic Optical Networks (EONs). The algorithm is configured to minimize blocking and spectral fragmentation ratios. The individuals encode the routes for the demands and the resources are allocated over the routes (and the network) depending on their rates, the number of spectral slices required, or randomly. We propose to analyze the performance statistically. The results demonstrate that the three assignment schemes present similar performances. The 90th percentiles for all measured parameters are very similar, indicating that ordering the input demands for assigning the resources does not significantly affect the performance of the proposed GA, highlighting the effectiveness of the proposed GA. Nevertheless, depending on the trade-offs to fulfill, one may be more advisable than the others in certain cases.

*Index Terms*—Elastic Optical Networks, RMLSA, DWDM, Genetic Algorithm.

#### I. INTRODUCTION

Managing the demands of Data traffic requires advances in network infrastructure to provide adequate communications services. The increasing number of persons using various datahungry services (for example, video conferencing and streaming, cloud processing, and online games), besides machine-tomachine communications and Internet of Things applications, among others, demand large capacity. Wavelength Division Multiplexing (WDM) optical networks are an alternative to accommodate the resulting demands on the network core. They evolved to Elastic Optical Networks (EONs) to provide more flexible spectral allocation [1] and enhance the ability to handle the variety of data rates demanded from core networks.

Allocating routes and spectral resources to satisfy the connection and data rate demands in EONs involves selecting appropriate modulation levels and spectral ranges (subcarriers). This problem, known as Routing, Modulation, and Spectrum Assignment (RMLSA), entails determining the optimal route between the pair of source and destination nodes, choosing suitable modulation levels, and assigning the necessary spectrum range to achieve the data rate for each demand. The objective is to maximize the number of demands addressed, among other performance indicators, thereby efficiently using the network resources [1]. This work explores a Genetic Algorithm (GA) to solve the RMLSA problem, aiming at multi-objective solutions by minimizing the demand-blocking ratio and reducing spectrum fragmentation. The population is formed by individuals or chromosomes that code possible routes for the demands the network has to answer to, each gene codes the route for one demand.

GAs have previously been employed for the RMLSA in EONs. For example, [4] uses a GA to reduce the demandblocking (or simply blocking) ratio when under high traffic demand and to minimize the number of spectral slices allocated for the demands when traffic is low. [5] aims at minimizing the number of occupied slices per link using two populations evolving in parallel with different selection criteria (of the individuals to generate the offspring) and mutation rates, and individuals migrating between the populations. More recently, [6] proposes GAs for RMLSA by encoding the route and allocation of demands on the chromosome (one gene for each) using a series of network performance indicators (among them spectral fragmentation) to evaluate the performance of the solution. In [3], routes are also encoded in the genes, aiming at minimizing route sharing and the number of occupied spectral slices, both separately and jointly.

This work proposes an evaluation function that optimizes the blocking and spectral fragmentation ratios jointly. Unlike [3]–[5], we consider minimizing the spectral fragmentation as an objective. [6] already considers that spectral fragmentation is a relevant performance indicator, but not as an optimization criterion – it is used as a control performance indicator to evaluate the solutions. By employing a mixed evaluation function for the performance of the solution, we find solutions that jointly minimize the blocking and spectral fragmentation ratios [7]. Furthermore, we evaluate the algorithm performance statistically using multiple rounds under different EON operating conditions. Differently from [7], We also investigate if ordering the demands using different criteria for resource allocation impacts the results, and include the number of hops per demand and the index of the last occupied subcarrier as performance indicators.

The proposed GA is tested under three different demand assignment schemes: Random Order (RO), Decreasing Data Rate (DDR), and Most Subcarriers First (MSF). In particular, in the first scheme, the demands are attended (the resources are allocated) randomly without prioritizing any demand. In the second scheme, the demands are ordered according to the transmission rate in Gbps, prioritizing the demands in descending order. Lastly, in the MSF scheme, the demands are ordered by the number of subcarriers required (which depends on the route), and the resources are allocated in that order. The mathematical model of the RMLSA problem has been omitted due to space constraints and can be found in [4]–[6].

Following, Section II describes the EONs and the RMLSA Problem. Section III presents the proposed GA. Section IV brings implementation and test scenario details together with the results and their analyses. Section V concludes this work.

## II. ELASTIC OPTICAL NETWORKS AND THE RMLSA PROBLEM

In EONs [1], the SLICE (Spectrum-Sliced Elastic Optical Path Network) or "flexible grid" technique divides the optical spectrum into small slices (or slots) of fixed width, as established by the ITU-T (International Telecommunication Union-Telecommunication Standardization Sector) G.694.1 recommendation, with a granularity of 12.5 or 6.25 GHz [11]. For an optical fiber bandwidth equal to 4.475 THz [10] and a granularity of 12.5 GHz per slice – 358 slices are available on each link. A set of slices totaling a bandwidth capable of closely providing the demanded transmission bitrate is assigned to create an optical path across the network links among the origin and destination of the demand.

The optical link/path configuration requires the assignment of the center frequency and bandwidth (the spectrum range/slice). This encompasses the Routing and Spectrum Allocation (RSA) problem. The use of the OFDM (Orthogonal Frequency Division Multiplexing) technology and the development of better optical transmitters brought the possibility to use different modulation levels per optical path, which results in an additional assignment of the modulation level on each subcarrier [1], and the RMLSA problem stems. Its solution must use network resources efficiently and reduce the ratio of blocked demands. A blockage occurs if network resources (typically spectrum resources) fail to meet a demand.

In EONs, it is important to store the routes and spectra information throughout the network to provide adaptability; so, modified Link State (LS) algorithms are more suitable for routing, wherein each node stores information about available resources across the entire network. In particular, the OSPF-TE (Open Shortest Path First - Traffic Engineering) and the IS-IS-TE (Intermediate System to Intermediate System - Traffic Engineering) LS protocols are suitable for EONs [8] since they provide traffic engineering information. OSPF protocol uses the Dijkstra algorithm to determine the least cost route between two network nodes based on knowledge of the entire network topology. More routes can be obtained using Yen's algorithm (based on Dijkstra) to find the k-shortest paths between two points on the network [12].

The OFDM subcarriers can convey symbols using different modulation levels; the higher the modulation level, the more bits each OFDM subcarrier supports but the lower the robustness to noise, i.e., the higher the bit error rate under the same operating conditions. Consequently, the shorter the link length under the same OSNR (Optical Signal to Noise Ratio), the higher the modulation level, for the same target BER (Bit Error Rate) or target Quality of Transmission (QoT) [9]. On a subcarrier, the transmission rate C is

$$C = B \log_2 M, \tag{1}$$

where, B represents the spectrum (bandwidth) allocated in GHz, and M is the modulation level adopted. In an optical path, the transmission rate depends on the bandwidth (number of slices) and the modulation level. The adaptive modulation technique can adapt the modulation level according to the path length, the longer the route, the lower the modulation level. Thus, for a demand with a given target transmission bitrate, the longer the optical path, the larger the bandwidth (the number of slices) needed to meet the desired bitrate.

In EONs, the RMLSA consists in finding routes, modulation levels, and subcarriers for the demands. One can employ different selection criteria for the demands for which resources are allocated and various resource allocation policies to serve the selected demand. Given a route for the demand, the First-Fit [2] allocation policy accommodates demands in the free slices (through the whole path) closest to the beginning of the spectrum whenever possible. We use it in this work.

#### III. PROPOSED GENETIC ALGORITHM

Genetic algorithms (GA) are inspired by Charles Darwin's theory of natural selection of species. They are used to find solutions to problems using populations. Each individual represents a possible solution. The performance of individuals as solutions for the problem is evaluated using an evaluation function assigning scores to the individuals. The individuals are ranked and selected for crossover operation to generate offspring. This strategy explores solutions to the problem searching for one leading to good performance.

Each chromosome defines an individual in the population. A chromosome contains n = 1 . . . D genes, i.e., the number of genes equals the number of demands presented to the network. The d-th gene encodes a route to the corresponding d-th demand, and the d-th gene indexes one of the k-shortest paths from Yen's algorithm for the demand d. This coding scheme is illustrated in Fig. 1.

Note that the individual codes the routes, which requires assigning the subcarriers composing the optical path defined by the route to achieve the corresponding transmission ratio of the demand. The resources for the demands are allocated using random, descending, or MSF ordering and the First-Fit policy, as described in Subsection III-B.

For selection, individuals are concatenated on a line where the length of the line section for an individual is proportional to its evaluation score. The algorithm moves along the line in steps of equal size. At each step, the correspondent individual from the section reached by the step is selected, the first step being a uniform random number smaller than the step size. We also employ elitism such that the individual presenting the best aptitude in one generation is replicated in the next generation. The individuals are selected for the crossover operator. During

![](_page_2_Figure_0.jpeg)

Fig. 1. Chromosome coding using an auxiliary table.

the crossover step, the individuals are randomly organized in pairs to form parents, then the crossover generates children (individuals for the next generation - offspring) by making the crossover point in the half of each parent in a manner that one child is formed by the first part of the father and the second part of the mother.

After the formation of the offspring, the mutation operator selects a gene to change the route it encodes to another among the available K-paths. This changes the optical path and may change the length and, consequently, the modulation level and the number of slices required to meet the demand. The mutation probability was set at 0.2% and all the K paths have equal probabilities. The GA stopping criterion is the number of generations.

The blocking ratio is the proportion between the number of blocked demands (a demand is blocked if network there are not resources in sufficient numbers to fully serve it) and the number of demands requested from the network

$$Blocking\_ratio = \frac{num\_blocked\_demands}{total\_num\_demands} \times 100.$$
 (2)

The fragmentation ratio per link is the number of gap slices (free slices between any two groups of slices allocated on a link) divided by the total number of link slices (358). The network fragmentation ratio is the average of the fragmentation ratios of used links between nodes in the network

$$Fragmentation\_ratio = \frac{\sum\limits_{i=1}^{\text{num\_links}} \text{num\_gap\_slices}_i}{\text{num\_links} \times \text{total num slices}} \times 100. \quad (3)$$

The sum of the transmission rates for the attended demands divided by the total transmission rates for requested demands provides the percentage of the total transmission rate met

$$\label{eq:transmission_rate_met} \begin{aligned} \text{Transmission\_rate\_met} &= \frac{\sum\limits_{i=1}^{D} \text{num\_rates\_met}_i}{\sum\limits_{i=1}^{D} \text{num\_input\_rates}_i} \times 100. \end{aligned} \tag{4}$$

The blocked demands have a transmission rate equal to zero. The spectral occupancy

Occupancy = 
$$\frac{\sum_{i=1}^{\text{num\_links}} \text{num\_slices\_used}_i}{\text{num\_links} \times \text{total\_num\_slices}} \times 100,$$
 (5)

averages the spectral occupations over used links between core network nodes – the ratio between the number of slices occupied in the link and the total number of slices of the link.

The number of hops per demand counts the number of nodes along the route serving the demand. Lastly, the index of the last subcarrier used per link brings another perspective of link occupancy; it is the index of the last occupied slice in a network link, the largest index slice in the link; when subtracted from the total number of slices (358), it gives a proxy for the number of remaining slices for serving future demands. This indicator is zero when the link is not used for any requested demand.

#### A. Fitness Function

The fitness evaluation measures the goodness of the solution (the chromosomes). The smaller the fitness, the better the solution, and the individuals with the smallest fitness are selected for crossover. We evaluate performance using the blocking ratio, which should be, ideally zero – the largest possible number of requested demands is met. It is weighted with the fragmentation ratio, since demands must be as contiguous as possible, with fewer free slices between the slices that serve the demands – bandwidth fragmentation can make it difficult to allocate future demands, wasting resources and leading to low spectrum efficiency [2].

Thus, the fitness function assigns a lower score to individuals presenting simultaneously lower fragmentation and blocking ratios, intending to minimize two important performance aspects of an EON. To this end, the evaluation function considers a trade-off between blocking and fragmentation ratios. Experimentally, we determined the weights for the blocking and the fragmentation ratios, leading to the fitness attributed to the solution encoded by a chromosome given by

$$f_1(\text{Blocking, Fragmentation}) = \begin{cases} 0, & \text{if Blocking} = 0 \text{ and Fragmentation} = 0 \\ 0.5, & \text{if Blocking} = 0 \text{ and Fragmentation} \neq 0 \\ 5 \times \text{Blocking} + 3 \times \text{Fragmentation}, & \text{otherwise} \end{cases}$$
 (6)

Above, the terms "Blocking" and "Fragmentation" refer to the blocking and the fragmentation ratios, respectively. The three conditions of the fitness function represent three scenarios: the best case occurs when both blocking and fragmentation ratios are zero; the intermediate case refers to blocking being zero (excellent) but fragmentation is nonzero and still needs to be minimized; and the general case when a trade-off between blocking and fragmentation ratios must be looked for.

## B. Demand Ordering for Resource Allocation

In this work, we test the hypothesis that the results provided by the GA would vary depending on the order the demands (and their routes) are encoded in the chromosome. In other words, we test the proposed GA in scenarios where the demands are allocated in specific orders (determined by heuristics) or not, to validate the algorithm. More specifically, we evaluate the performance of the solutions provided by the GA for three different ordering schemes for the requested demands: Decreasing Data Rate (DDR), Most Subcarriers First (MSF), and Random Order (RO).

In the DDR scheme, the demands are ordered decreasingly upon the requested transmission bitrate. The largest transmission rate is allocated first, one defines its modulation level and slices, and so on; note that for the subsequent demands, the slices in a given link must be allocated to not overlap with already occupied slices. In the MSF, the demands are again ordered in a decreasing manner, however, now according to the number of slices required to fulfill the bitrate of the demand. It is noted that the number of slices (subcarriers) varies due to the modulation level which in turn depends on the optical link distance between the nodes defining the demand. Note that this requires evaluating the number of slices employed for all demands for the routes encoded in the corresponding genes in the chromosomes previously to allocate the resources. At last, in the RO scheme, the resources for the demands are allocated randomly drawing the demand with uniform probability, i.e., no particular demand ranking exists.

#### IV. ALGORITHM PERFORMANCE EVALUATION

#### *A. Parameters of the Genetic Algorithm*

GA performance was assessed through simulation. The initial population is randomly defined. However, we force all the K possible routes for every demand to be present at the initial population, in at least one chromosome, unlike [3]. Empirically, we observed that, when routes are ignored, reducing the population diversity, the GA can take longer to find a solution presenting good performance or even not find one. One can force the K routes for a demand to be coded in the same gene position in K different chromosomes randomly selecting the remaining D − 1 demands. Doing that for every demand one obtains a number of individuals equal to K times the number of demands D. To increase the genetic variety, we add to the previous design other D individuals randomly selected for a total of (K + 1) × D individuals in the population. The Yen's algorithm provides the K possible routes for each demand, we set K = 3.

The selection operation was the roulette. The chromosomes (individuals) were arranged in a roulette wheel and their areas in the roulette are proportional to their fitness score. The better evaluated the chromosome, the greater its area and the larger its chances for mating and crossover. The mutation rate is set at 0.2. The stopping criterion is reaching 50 generations.

#### *B. Network Topology*

We test the proposed algorithm in a realistic network. We consider the NSFNET network, an American backbone example shown in Fig. 2. NSFNET has 16 nodes and the distances between nodes correspond to the distances between the cities where the nodes are placed.

## *C. Requested Demands*

The proposed GA finds solutions for the RMLSA. We evaluate its capacity to find good solutions for sets composed of 75, 100, and 150 demands. The solution is the best individual after 50 generations of the GA. However, finding solutions for specific cases of input demands may misguide the evaluation of the GA in finding good solutions in general. Therefore, we evaluate the GA performances (considering the different assignment criteria) using multiple rounds (see

![](_page_3_Figure_9.jpeg)

Fig. 2. NSFNET American Network [17]

Subsection IV-D). The origin, destination, and transmission rate for all the demands are randomly drawn from uniform distributions in each round. The origin and destination can be any different points but not the same and the transmission rates lie between 10 Gbps, and 1 Tbps, drawn from a list of 10 possible predefined transmission rates (1, 10, 30, 40, 50, 100, 200, 400, 800, 1000 GHz).

#### *D. Number of Rounds*

.

Using multiple rounds, we obtaining the Cumulative Distribution Function (CDF) of the performance indicators. The number of rounds was set using the Wilcoxon test (Mann-Whitney U) [15] to evaluate if the values of the indicator up to the round present the same distribution observed for the same indicators a few rounds before or not [16]; if yes, then there is no reason for executing more rounds, else, new rounds take place. This determines the number of executions such that the values of the performance indicator are drawn from the same distribution with great probability. Applying the Wilcoxon test with p = 0.05 to all the performance indicators, and number of demands (75, 100 and 150), we arrived at 132 rounds.

## *E. Results*

The GA was executed with the three demand ordering presented in Subsection III-B and evaluated with the four network performance parameters (metrics): blocking ratio, fragmentation ratio, percentage of the total transmission rate achieved, and network spectral occupancy ratio; the first two compose the fitness function for the GA, while the two last can be seen as control performance indicators to evaluate the solutions over other relevant parameters of the network.

Fig. 3 presents the CDF of performance indicators considering 75 demands for the three assignment criteria. The black horizontal line corresponds to the 90th percentile. It crosses the blocking ratio at 0% and the transmission rate met at 100% for all criteria. But, it crosses the fragmentation ratio at 44.35% for the RO, 43.45% for DDR, and 41.48% for MSF, and the occupancy at 44.87, 48.31, and 48.75%, respectively. We also calculated the variance of these performance indicators to evaluate their dispersion around their means. The variance of the blocking ratio was equal to 0.22, 0.18, and 0.01%<sup>2</sup> for RO, DDR, and MSF, respectively. For the fragmentation ratio, it was 6.96, 18.42, and 11.98%<sup>2</sup> . For the transmission rate, it was 0.0008, 1.04, and 0.08%<sup>2</sup> . Lastly, for occupancy, it was 23.66, 33.41, 27.60%<sup>2</sup> .

![](_page_4_Figure_1.jpeg)

Fig. 3. CDF of the blocking ratio, the fragmentation ratio, the achieved transmission rate, and spectral occupancy ratio when the GA solves the RMSLA for 75 demands in the NSFNET with the three demand ordering.

Fig. 4 depicts the results for 100 input demands. The 90th percentiles of the blocking ratio are 4% for the RO, 3% for the DDR, and 1.80% for the MSF, while for the transmission rate, it is 100% for all demand ordering schemes. For the fragmentation ratio, it values 46.48% for the RO, 41.74% for the DDR, and 41.76% for the MSF, while for the occupancy ratio, it is 52.82, 56.58, and 56.56%, respectively. The variance of the blocking ratio equals 3.05, 2.65, and 0.81%<sup>2</sup> for the RO, the DDR, and the MSF, respectively. For the fragmentation ratio, it is 8.05, 9.25, and 7.83%<sup>2</sup> , for the transmission rate, it is 0.16, 11.27, and 3.98%<sup>2</sup> , and, lastly, for the occupancy ratio, it was 12.02, 12.08, 13.32%<sup>2</sup> , respectively.

![](_page_4_Figure_4.jpeg)

Fig. 4. CDF of the blocking ratio, the fragmentation ratio, the achieved transmission rate, and spectral occupancy ratio when the GA solves the RMSLA for 100 demands in the NSFNET with the three demand ordering

Figure 5 presents the CDFs for 150 demands. The blocking ratio has a 90th percentile equal to 9.33% for the RO, 13.33% for the DDR, and 13.20% for the MSF, while the achieved transmission rate meets the 90th percentile line at 99.66, 94.30, and 96.49%, the fragmentation ratio at 43.41, 39.14, and 39.89%, and the occupancy ratio at 60.27, 66.35, and 66.17%, respectively. The variance of the blocking ratio equals 6.11, 16.79, and 19.74%<sup>2</sup> for RO, DDR, and MSF, and 5, 10.66, and 9.82 %<sup>2</sup> for the fragmentation ratio, transmission rate, it is 0.83, 35.31, and 44.72%<sup>2</sup> , and for the occupancy ratio, it is 5.99, 8.96, 9.63%<sup>2</sup> , respectively.

The three criteria present very similar 90th percentiles in all indicator. Thus, one may conclude that using RO, DDR, or MSF assignment criteria does not significantly impact the performance of the solutions provided by the proposed GA for the RMSLA. But a more careful analysis is necessary.

![](_page_4_Figure_8.jpeg)

Fig. 5. CDF of the blocking ratio, the fragmentation ratio, the achieved transmission rate, and spectral occupancy ratio when the GA solves the RMSLA for 150 demands in the NSFNET with the three demand ordering.

The variances of the performance indicators, in general, present closer values for the MSF and DDR, while for the RO solutions, they are less close. Moreover, in most of the parameters, the RO lead to a smaller variance than MSF and DDR, meaning that the performance of the RO solutions vary less than the ones provided by MSF and DDR.

From the CDFs in Figs. 3-5, it is noted that the performance of the proposed GA is close when the demands are assigned using MSF or DDR criteria, meanwhile the RO departs from those for all the indicators. RO presents a slightly better performance than MSF and DDR for all indicators, except for the fragmentation. It may indicate that ordering the demands (MSF or DDR) for resource allocation is more indicated when it is intended to reduce fragmentation, and using RO is more indicated to reduce the blocking ratio or occupancy and increase the transmission rate achieved. At first glance, this could be because the RO criterion allows to explore solutions that would otherwise be restricted by the MSF or DDR, since the prioritization of demands in function of their rate or spectral width makes the population to converge more quickly but reducing its variability. This hypothesis is to be investigated in future works.

## *F. Analysis of the Number of Hops per Demand and the Index of Last Subcarrier Occupied per Link*

The number of hops per demand is a proxy to the occupancy of the network, indicating the more or fewer links used in the correspondent route, and may be correlated with the blocking and fragmentation ratios and the transmission rate of the solution. The index of the last subcarrier occupied per link parameter is another perspective on the occupancy of the network, and provides the bandwidth for easy allocation of future demands.

Fig. 6 shows the CDFs of the number of hops per demand for 75, 100, and 150 input demands, respectively, with the three ordering criteria. It is noted that the 90th percentile of the number of hops per demand is 6 for all simulated scenarios, except for DDR and MSF when the network has to serve 150 demands when it drops to 5. The mode of the number of hops is always 4, and the median is 4 in almost all cases, except for 150 input demands under DDR or MSF criteria when it drops to 3 (possibly the fitness functions favors solutions with fewer hops to reduce the blocking ratio).

The results of the number of hops per demand are substantially similar across all simulation scenarios. This probably occurs because the Yen's algorithm (used for settling the possible routes) is unaware of the fitness function.

![](_page_5_Figure_1.jpeg)

Fig. 6. CDF of the number of hops per demand satisfactorily served for 75, 100, and 150 demands with the three demand ordering.

Fig. 7 shows the CDFs of the index of the last subcarrier used per link for 75, 100, and 150 input demands, respectively, with the three demand ordering. Unused links are present in said CDFs and are computed as 0 subcarriers used. For 75 demands, this parameter was equal to 348, 353, and 350 for RO, DDR, and MSF, respectively. For 100 demands, it was 354, 357, and 354. Lastly, for 150 demands, it was 357, 354, and 358. The mode for this parameter was 352, 348, and 330 for 75 demands, 358, 358, and 350 for 100 demands. For 150 demands, this parameter was equal to 358, 353, and 358 (RO, DDR, and MSF). The median was equal to 269, 317, and 314 for 75 demands, 323, 343, and 336 for 100 demands, and 341, 340, and 349 for 150 demands (RO, DDR, and MSF).

The closer the curve reaches the bottom-right extreme, the more occupied the network links are. Consequently, although the 90th percentiles of the last subcarrier approach the largest subcarriers index (358), the concavity (nozzle) of the CDFs in Fig. 7 show that the scenario with 75 demands presents more less-occupied links than the scenario with 150 demands. Moreover, it is noted that the CDFs resulting from using the RO are a bit above the MSF and DDR curves, which show more similar performances also for the other performance indicators, as previously stated.

![](_page_5_Figure_5.jpeg)

Fig. 7. CDF of the index of the last subcarrier used per link for 75, 100, and 150 demands with the three demand ordering.

### V. CONCLUSION

This work presented a genetic algorithm to attack the RMLSA problem while minimizing the blocking rate and spectral fragmentation. The results are quite promising. We use a stochastic approach to evaluate the proposal, under three different resource assignment ordering criteria. The results showed that no significant performance difference is noticeable. However, using no ordering (randomly choosing the demands to save resources for) lead to slightly better blocking ratio, transmission rate, and occupancy, while ordering demands showed smaller fragmentation ratio. In future works, we intend to investigate new fitness functions, considering, for example, the index of the last subcarrier assigned to improve link balancing and equip the network with capacity for allocating future demands.

### ACKNOWLEDGMENT

This work was partially funded by CNPq (processes 312743/2023- 8 and 405940/2022-0), by CAPES (88887.954253/2024-00 and 001) and by FAPERJ.

#### REFERENCES

- [1] Jinno, M., Takara, H., Kozicki, B., Tsukishima, Y., Sone, Y. and Matsuoka, S. (2009). Spectrum-efficient and scalable elastic optical path network: architecture, benefits, and enabling technologies, *IEEE Communications Magazine* 47(11): 66–73.
- [2] Chatterjee, B. C., Sarma, N. and Oki, E., *Routing and spectrum allocation in elastic optical networks: a tutorial*. *IEEE Communications Surveys & Tutorials*, v. 17, n. 3, p. 1776-1800, 2015.
- [3] Fontes, M. F. et al., *Roteamento e alocac¸ao de espectro em redes ˜ opticas ´ elasticas via algoritmo gen ´ etico ´* , *Congresso Brasileiro de Inteligencia ˆ Computacional* (CBIC), 2019.
- [4] Zhou, Xiang et al. Dynamic RMSA in elastic optical networks with an adaptive genetic algorithm. In: *2012 IEEE GLOBECOM*, 2012. p. 2912-2917.
- [5] Gong, Long et al. A two-population based evolutionary approach for optimizing routing, modulation and spectrum assignments (RMSA) in O-OFDM networks. *IEEE Communications Letters*, v. 16, n. 9, p. 1520- 1523, 2012.
- [6] Villamayor-Paredes, Melisa M. Rosa et al. Routing, modulation level, and spectrum assignment in elastic optical networks. A routepermutation based genetic algorithm. *Optical Switching and Networking*, v. 47, p. 100710, 2023.
- [7] Costa, R. A. M. et al., *Roteamento, n´ıvel de modulac¸ao e alocac¸ ˜ ao˜ de espectro em redes opticas el ´ asticas via algoritmo gen ´ etico ´* , *Simposio ´ Brasileiro de Telecomunicac¸oes e Processamento de Sinais (SBrT) ˜* , 2024.
- [8] Casellas, Ramon et al. Design and experimental validation of a GM-PLS/PCE control plane for elastic CO-OFDM optical networks. *IEEE Journeal on Selected Areas in Communications*, v. 31, n. 1, p. 49-61, 2012.
- [9] Bocoi, Adriana et al. Reach-dependent capacity in optical networks enabled by OFDM, *IEEE Conf. on Optical Fiber Communication*, 2009.
- [10] Lu, W, et al., Dynamic Service Provisioning of Advance Reservation Requests in Elastic Optical Networks, *IEEE Journal of Lightwave Technology*, Vol 31:10, March 26, 2013; p. 1621 - 1627.
- [11] ITU-T. ITU-T G.694.1: Spectral grids for WDM applications: DWDM frequency grid. October 29, 2020. Available in: https://handle.itu.int/11. 1002/1000/14498. Accessed: June 6, 2024.
- [12] Yen, Jin Y., Finding the k shortest loopless paths in a network, *Management Science*, vol. 17, no. 11, pp. 712–716, 1971.
- [13] Zhang, Fatai et al., GMPLS OSPF-TE extensions in support of flexiblegrid in DWDM networks, *RFC 8363*, 2012. https://doi.org/10.1007/ BF01386390.
- [14] Talebi, Sahar et al. Spectrum management techniques for elastic optical networks: A survey. *Optical Switching and Networking*, v. 13, p. 34-48, 2014.
- [15] Wilcoxon, Frank et al. *Critical values and probability levels for the Wilcoxon rank sum test and the Wilcoxon signed rank test*. Selected tables in mathematical statistics, v. 1, p. 171-259, 1970.
- [16] Rodrigues, C. F. F., Lovisolo, L., and Mello, L. S., Alocac¸ao de Recursos ˜ da Interface Aerea 5G a partir de um Crit ´ erio de Utilidade, in ´ *XL Simposio Brasileiro de Telecomunicac¸ ´ oes e Processamento de Sinais ˜ (SBrT)*, Sep. 2022, doi: 10.14209/sbrt.2022.1570814168.
- [17] Bibi, Hafsa et al. Dynamic wavelength grouping for quality of service in optical packet switching. *IEEE Access*, v. 9, p. 60946-60959, 2021.
Contents lists available at [ScienceDirect](www.sciencedirect.com/science/journal/10685200)

# Optical Fiber Technology

journal homepage: [www.elsevier.com/locate/yofte](https://www.elsevier.com/locate/yofte) 

![](_page_0_Picture_5.jpeg)

![](_page_0_Picture_6.jpeg)

# Fragmentation-Aware with core classification algorithms for spectrum allocation in Elastic Optical Networks-Space Division Multiplexing (SDM-EON)

Mahdiyeh Hafezi , Akbar Ghaffarpour Rahbar \*

*Computer Networks Research Lab, Faculty of Electrical Engineering, Sahand University of Technology, Tabriz, Iran* 

ARTICLE INFO

*Keywords:* 

Routing and spectrum assignment in SDM-EON Fragmentation Multipath assignment

#### ABSTRACT

The new technology to improve the capacity of transmission in optical networks is Elastic Optical Networking with Space Division Multiplexing (SDM-EON). However, fragmentation is one of the critical issues in EON that is created by dynamically establishing and releasing lightpaths over the time, thus increasing connection blocking probability. In this research, two new algorithms are proposed in SDM-EON to improve the fragmentation problem and improve blocking probability, called Priority Select Frequency (P-S-F) and Priority Select Core (P-S-CO). We assume that connection demands have three priorities as high-priority, mid-priority, and low-priority. Here, the requested bandwidth of a connection demand is divided into smaller sizes to be setup in multiple cores. By providing this opportunity in spectrum allocation and assignment, connection blocking probability is reduced as our performance evaluation results prove. For instance, P-S-CO and P-S-F reduce bandwidth blocking probability, respectively, at least by 6.8% and 4.5% compared to existing methods. In the best case, P-S-CO and P-S-F can improve bandwidth blocking probability, respectively, by 25% and 17.8% compared to existing methods.

### **1. Introduction**

Connection demands can be allocated in a flexible manner in Elastic Optical Network (EON) [\[1,2\]](#page-8-0). EON has some problems as Routing and Spectrum Assignment (RSA), fragmentation, grooming, survivability issues and energy consumption. The RSA is responsible for determining the possible route between a given source/destination pair of a given connection demand. After selecting a route, RSA tries to allocate required spectrum to the connection demand. During the connection setup, two constraints must be considered: the continuity of spectrum ensures that the required frequency slots (FSs) for the connection are allocated with the same FS number over all the links of the path, and the contiguity constraint that focuses on the FSs to be in back to back in the links of the route between the source and destination pair.

Space Division Multiplexing (SDM) increases the capacity of optical transmission systems. Multi-core fibers (MCF) are common SDM that are used in EON. Nowadays, the developments of multi-core fiber amplifiers are suitable for amplifying space division multiplexed signals.

Fragmentation in bandwidth is the problem made by dynamically establishing and releasing of connections. Clearly, fragmentation causes to bandwidth wastage. There are some techniques to control the

fragmentation without any checking about spectra or path situation, e.g. [\[3\].](#page-8-0) In other algorithms like [\[4](#page-8-0)–7], the route and spectra situations are controlled to improve fragmentation in the network.

The multipath mechanism is commonly used in EON to reduce connection blocking, where a connection demand is split into multiple routes between its source and destination in different sizes of FSs until it is completely allocated. Splitting and multipath routing can provide various benefits such as avoiding spectrum fragmentation that causes inefficiency, significantly improving the possibility of connection blocking, and thus bringing fault tolerance, increasing bandwidth, and improving security. However, there are some disadvantages for splitting and multipath routing. One of the disadvantages of splitting multipath routing techniques is that different sub-light paths experience different end-to-end delays. Another disadvantage of this method is that it can increase the number of guard bands.

Overall, based on our study, there is not enough work to consider both fragmentation and splitting of lightpaths to improve the blocking probability for class-based traffic under SDM-EON. This motivates us to reduce blocking probability (BP) by considering these two techniques in order to reduce fragmentation in spectra.

Our objective in this paper is to solve fragmentation which results in

*E-mail address:* [ghaffarpour@sut.ac.ir](mailto:ghaffarpour@sut.ac.ir) (A. Ghaffarpour Rahbar).

<sup>\*</sup> Corresponding author.

![](_page_1_Figure_2.jpeg)

**Fig. 1.** An example for spectrum utilization in Classification and Non-Classification states.

improving blocking probability. We propose spectrum and coreclassification methods in SDM-EON through MCF. By considering the concept of connection splitting, we propose two heuristic fragmentation-aware algorithms called Priority Select Frequency Slot (P-S-F) and Priority Select Core (P-S-CO) for resource allocation of classbased traffic in SDM-EON, both based on the multipath mechanism.

Our contribution in this paper is to propose two heuristic fragmentation-aware algorithms that consider fragmentation with splitting required FSs of a connection in classified cores to reduce blocking probability in SDM-EON.

The organization of this article is as follows. Section 2 reviews recent works on fragmentation. In [Section 3](#page-3-0), our suggested algorithms are explained. In [Section 4](#page-5-0), performance evaluation results are presented. [Section 5](#page-8-0) concludes the paper.

### **2. Related work**

To improve the fragmentation problem in SDM-EON, a number of algorithms have been proposed in the time, space, spectra domains; for example, the fragmentation-aware and alignment-aware algorithms in [\[8\],](#page-9-0) SCVPS[\[9\]](#page-9-0), fragmentation-aware with routing and spectrum assignment algorithm (FA-RSA) [\[10\],](#page-9-0) and fragmentation-aware with routing and spectrum assignment plus congestion avoidance (FA-RSA-CA) in spatial and spectral dimensions [\[10\].](#page-9-0)

On the other hand, space, spectral, temporal are considered in some other algorithms in SDM-EON such as fragmentation-aware with routing and spectrum; spatial plus modulation assignment (FA-RSSMA); and fragmentation-aware with routing and spectrum and spatial plus modulation with congestion avoidance (FA-RSSMA-CA) [\[9,11,12\].](#page-9-0)

In [\[3\],](#page-8-0) Fragmentation-Aware with Routing and Spectrum Assignment (FA-RSA) has been proposed based on the external fragmentation measurement in spectra. In [\[2,13\]](#page-8-0), the multipath mechanism has been studied in optical networks. In addition, in [\[14\],](#page-9-0) the multipath mechanism has been studied under considering software defined network (SDN) architecture in SDM-EON.

A strong candidate to realize practical SDM transmission system is Multi-core fiber (MCF) which provides high capacity transmission [\[15,16\].](#page-9-0) The SDM-EON has been studied in [\[17\].](#page-9-0) A survey of resource allocation schemes and algorithmic approaches researched for SDM optical networks have been investigated in [\[18\]](#page-9-0).

In [\[19\]](#page-9-0), multi-flow virtual concatenation (MFVC) in Flexi-Grid optical networks has been researched. The MFVC could utilize spectral fragments and decrease blocking probability without influencing existing active services or wasting additional spectrum resources. In [\[20\]](#page-9-0), SLA-aware differentiated QoS (SADQ), has been researched at the level of routing, spectrum allocation, and connection survivability. In [\[21\]](#page-9-0), the research challenges and open issues on fragmentation problem in EONs have been addressed.

In [\[22\]](#page-9-0) and [\[23\]](#page-9-0), fragmentation in MCF has been researched, and Core-Classification and core-region methods have been suggested to improve the fragmentation problem. The work in [\[24](#page-9-0)–26] classifies each core according to the number of required frequency slots in a static manner. Fig. 1 presents an example of spectrum utilization in EON with MCFs. Fig. 1(b) shows spectrum utilization without considering core classification and Fig. 1(a) presents the one based on pre-defined core classification. In Fig. 1 (a), each core is used for accommodating the demands with a specific required number of frequency slots. For instance, Core 1 is used to accommodate all the demands that need 6 frequency slots. By this way, there will be no spectrum fragmentation in cores. We consider prioritizing in connections by classifying them in three group besides considering fragmentation controlling and multipath mechanism on MCF network. In MCF, multi cores are used between each source and destination. The common way to allocate a connection on cores is First-Core-Fit (i.e., cores are allocated in sequence) and the other method is first fit core (i.e., FSs are allocated in sequence on each core.

The objective of [\[2\]](#page-8-0) is to resolve fragmentation in MCF, and proposes core-classification and core-region methods. In [\[13,27,28\]](#page-9-0), fragmentation in SDM-EON has been studied. In [\[29\],](#page-9-0) crosstalk besides fragmentation has been considered in SDM-EON. In [\[30\]](#page-9-0), based on QoS-aware

```
Inputs:
   Route: A given path between source and destination 
 Req_FS: Number of FSs required by new connection
   Core: the core number on which the connection must be setup
Output: 
   First free gap for a given connection request is found.
      1. counter = 0
      2. h= number of hops for Route
      3. For i = 1 to n // scan all n FSs on links of Route
      4. FS_Status = 0 // assume FS status is empty at the beginning
      5. For index_of_link = 1 to h // search each link of Route
      6. If ( Route [index_of_link][Core] [i] ≠ 0 ) // situation of FSs in the given Route on core # Core 
      7. FS_Status = 1 // 1 means occupied frequency slot 
      8. break // goto line 11
      9. End If
      10. End For
      11. If (FS_Status = 0) // if the i-th FS is empty on all links of Route
      12. If (counter = 0) // counter of back to back blank FSs in a gap
      13. First_FS_Starter = i
      14. counter = counter + 1
      15. Else 
      16. counter = counter + 1
      17. If (counter = Req_FS) // the gap size is enough for the connection request
      18. Return First_FS_Starter // return the pointer to the beginning of found gap
      19. End If
      20. End If
      21. Else // if the i-th FS is occupied on at least one of the links of 
         Route
      22. counter = 0 // there is no gap so reset counter
      23. First_FS_Starter = 0
      24. End If
      25. End For
      26. Return 0 // no gap found
```

**Fig. 2.** The FindFirstFreeGap (Route, Req\_FS, Core) function [\[2\]](#page-8-0).

classification, the data traffic is divided into high-quality (HQ) and lowquality (LQ) traffic. In [\[31\]](#page-9-0), a crosstalk-aware algorithm in MCF is studied by considering priority-based connections.

The work in [\[22\]](#page-9-0) has proposed a model of multi-service system, where its goal is to improve parameters like blocking probability and average number of waiting calls. For improving blocking probability in EON, in [\[23\]](#page-9-0), the effects of different routing methodology parameters have been studied. The study in [\[32\]](#page-9-0) has proposed an advanced variant of RSA as Routing and Multiple Spectrum Assignments (RMSA) in dynamic traffic grooming for EON by considering spectrum fragmentation problem. In [\[33\]](#page-9-0), by considering the virtual topology spectrum assignment besides higher modulation levels in multiple hops, spectrum assignment has been optimized in network. In [\[34\]](#page-9-0), unicast (one-to-one) and anycast (one-to-one-of-many) traffic demand have been studied by formulating the RMSA problem. First-Fit (FF) [\[34,35\]](#page-9-0) is the simplest and common spectrum allocation policy mechanism in EON that tries to find the first free gaps along the path that is found by a routing algorithm like the *K*-Shortest path routing. In [\[36\]](#page-9-0) and [\[37\]](#page-9-0), fragmentation in SDM-EON and multicore fiber network has been studied.

In [\[38\],](#page-9-0) a spectrum assignment mechanism for an EON node architecture with slicers has been proposed in which a modified RSA scheme for a mixed-integer linear programming (MILP) model and a heuristic algorithm is formulated. In [\[39\]](#page-9-0), a new multi constrained defragmentation algorithm (MCDFA) has been presented in EON, where MCDFA has two key subjects: spectrum assignment for new connections and then reconfiguring the existing connections in a non-fault situation. In [\[40\]](#page-9-0),

<span id="page-3-0"></span>![](_page_3_Figure_2.jpeg)

**Fig. 3.** An example for the P-S-F algorithm.

defragmentation mechanisms in EON by considering connection blocking rate reduction has been studied. The work in [\[41\]](#page-9-0) has researched a new impairment-conscious spectrum assignment mechanism for EON to reduce the connection request blockings in the network.

One of the challenges of EON is fragmentation. One of the methods used to manage or eliminate fragmentation is core classification or demand slot classification. In these types of algorithms, the number of allocated slots in each core is limited. In other words, the performance of these types of algorithms is close to static methods (for example, connections with 11 to 15 slots in core 2, connections with 16 to 20 slots in core 3, …). One of the core classification methods presented in [\[44\]](#page-9-0) is that the algorithm provides a connection level that classifies the frequency slots into several prioritized areas, which is called coreclassification [\[44\]](#page-9-0).

In [\[2\]](#page-8-0), three different algorithms for managing fragmentation are presented. In the first algorithm (called MFPC-RSCA), the external fragmentation criterion is calculated for each core, and then the cores are sorted based on the criterion in ascending order. In the second algorithm (called FMMA-RSCA), the fragmentation measurement criterion is calculated for each clustered core, and then the cores are sorted in ascending order based on the criterion. In the third algorithm, which is named spectrum block multipathing per core (SBMC-RSCA), based on the number of prime numbers related to each core and the number of requested slots in each request, the requested bandwidth is allocated in different cores. For example, if there are 4 cores in a fiber, cores 1 to 4 respond to blocks of size 1, 2, 3, and 5, respectively. Core 1 only responds to the blocks of length 1 slot, Core 2 only responds to the blocks of length 2 slots, Core 3 only responds to the blocks of length 3 slots, and Core 4 only responds to the blocks of length 5 slots. When the number of cores is small, scalability is one of the main problems of this algorithm. Multiple spectrum block paths per core is an algorithm that tries to eliminate or reduce fragmentation by reducing the spectrum allocation dynamics. In this type of routing and spectrum allocation algorithm, two issues should be considered: (1) scalability and (2) maximizing the number of generated requests. An important issue that is less discussed in this article is the number of senders and their related costs. The management of cores when the number of cores is high, as well as the efficiency of the algorithm when the required slot range is wide, are among the important things that should be investigated in this algorithm and similar algorithms. Due to the high impact of transmitters on the final cost of an optical network, the number of required transmitters has not been considered in the SBMC-RSCA algorithm and no comparison has been made with similar methods based on the number of transmitters.

In [\[45\]](#page-9-0), three different algorithms for core classification and fragmentation reduction have been presented. In the first algorithm, which is called smart-fit, in the first step, all gaps with a size greater than or equal to the requested slots are considered, and the start index of each gap is stored in an array called FB (free block). In the next step, it is necessary to calculate the members of an array called Y1, which shows how many gaps remain free if an input request is allocated in each of the gaps. Now, if set Y1 is empty, the connection is blocked. In the second algorithm of this paper, the performance of SBMC-RSCA is greatly improved, which is named OPT-SBMC-RSCA. To improve the scalability of SBMC-RSCA, the authors have proposed an algorithm that calculates the length of the blocks that each core responds to. In OPT-SBMC-RSCA, instead of using prime numbers as used in SBMC-RSCA, it is used powers of 2, that is, the specified length of the block size for each core is 2*<sup>i</sup>* , where *i* =[0,1,2,…*C*-1] for *C* cores on a fiber; the performance of some cores are similar in SBMC-RSCA, which is solved in OPT-SBMC-RSCA by using powers of 2.

### **3. Proposed algorithms**

In this section, our Priority Select Frequency slot (P-S-F) and Priority Select Core (P-S-CO) are presented in detail for SDM-EON. We assume that there are *C* cores on each link in each direction. We assume that connection demands are prioritized. The priority is divided into three groups: (1) high-priority (presented by priority 1), (2) mid-priority (presented by priority 2), and (3) low-priority (presented by priority 3). This priority is randomly given for each arriving connection in the network. Then, based on the connection priority, the connection will be setup on its core (in P-S-CO) or segment (in P-S-F). In our algorithms, we use some common methods such as find first free gap for connection setup, so we decide to explain it in a separate algorithm displayed in [Fig. 2.](#page-2-0)

We propose two new algorithms based on the multipath mechanism, where besides fragmentation controlling in network, we consider priority for connections. In real, we divide connections in 3 priorities to setup them successfully.

We first need to detail the *Find\_First\_Free\_Gap* function which is used in all of our proposed algorithms. [Fig. 2](#page-2-0) presents the *Find\_First\_Free\_Gap*  (*Route, Req\_FS, Core*) function based on [\[2\]](#page-8-0). In this algorithm, *n* is the number of FSs per link. To find the first free gap (i.e., back to back or

```
Inputs:
 Requested_FS : number of required FSs by the new connection. 
 C : number of cores on a link
 p: connection priority 
Output: Connection setup
1- Remain_FSs = Requested_FS // keep the number of unallocated FSs in Remain_FSs
2- For j = 1 to K //scan K shortest paths
3- Path = get the j-th path
4- For c = 1 to C // search all C cores
5- If (p = 1) //evaluate segment 1
6- If (Remain_FSs ≤ m1)
7- Al_FS = Remain_FSs
8- Else
9- Al_FS =m1
10- End if
11- Gap = FindFirstFreeGap (Path, Al_FS, c, 1, m1)
12- If (Gap ≠ 0) // part of the connection can be allocated successfully
13- Assign the found spectrum starting from Gap on core c to the connection
14- Remain_FSs = Remain_FSs – Al_FS // update remaining unallocated frequency slots
15- If (Remain_FSs = 0)
16- break // The connection can now be allocated successfully. Go to line 52
17- End if
18- End if
19- End if
20- If (p = 2) // evaluate segment 2
21- If (Remain_FSs ≤ m2 – m1 )
22- Al_FS = Remain_FSs
23- Else
24- Al_FS =m2-m1
25- End if
26- Gap = FindFirstFreeGap (Path, Al_FS, c, m1+1, m2)
27- If (Gap ≠ 0) // part of the connection can be allocated successfully
28- Assign the found spectrum starting from Gap on core c to the connection
29- Remain_FSs = Remain_FSs – Al_FS // update remaining unallocated frequency slots
30- If (Remain_FSs = 0)
31- break // the connection can now be allocated successfully. Go to line 52 
32- End if
33- End if
34- End if
35- If (p = 3) // evaluate segment 3
36- If (Remain_FSs ≤ ( n - m2 )
37- Al_FS = Remain_FSs
38- Else
39- Al_FS =n-m2
40- End if
41- Gap = FindFirstFreeGap (Path, Al_FS, c, m2+1, n)
42- If (Gap ≠ 0) // part of the connection can be allocated successfully
43- Assign the found spectrum starting from Gap on core c to the connection
44- Remain_FSs = Remain_FSs – Al_FS // update remaining unallocated frequency slots
45- If (Remain_FSs = 0)
46- break // the connection can now be allocated successfully. Go to line 52 
47- End if
48- End if
49- End if
50- End for
51- End for
52- If (Remain_FSs = 0)
53- Setup the whole connection successfully
54- Else
55- Block the connection
56- End If
57-END // of algorithm
```

**Fig. 4.** The P-S-F algorithm.

consecutive empty FSs), we require to find the first index of gaps in the given *Path* and *Core*. The first index of gap is shown by *First\_FS\_Starter*. The *counter* variable is the number of FSs in each one of the gaps, where *counter* must be smaller than the number of requested FSs. The first free gap for a connection may be found in Lines 12–19; otherwise, it is

considered as not found in Lines 22–23. The complexity degree for *Find\_First\_Free\_Gap*(*Route, Req\_FS*, *Core*) is O(*D* × *n*), where *D* is the network diameter.

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

**Fig. 5.** An example for the P-S-CO algorithm.

### *3.1. Priority select frequency (P-S-F)*

The Priority Select Frequency (P-S-F) algorithm is suggested to reduce BP and improve fragmentation in SDM-EON with MCF. Each connection demand has its own priority to allocate special identified FSs and cores in MCF. When a new connection demand arrives, its priority is checked. Then, based on the priority, cores and FSs are allocated to it when they are free; otherwise, the connection demand is blocked.

In [Fig. 3,](#page-3-0) we show how P-S-F works. Assume links are MCF with *C* = 7 cores, and each core has *n* = 300 FSs. Here, we can provide three segments such as: the first segment FSs 1 to 150 (appropriate for accommodating high-priority connections), the second segment FSs with index 151 to 250 (suitable for accommodating mid-priority connections), and the third segment with FSs index 251 to 300 (used for accommodating low-priority connections). Consider that a new high-priority connection arrives that needs 20 FSs (i.e., *Requested\_FS* = 20). Then, in the first segment on Core 1, since we only have 15 free FSs (shown with cyan color), these free slots are allocated for the new connection. To allocate the remaining 5 FSs, since Core 2 has no empty room, Core 3 is checked and 5 free FSs from Core 3 (displayed with cyan color) are allocated to the new connection. If there is no empty FSs on the 7 cores with FSs within index 1–150, the connection will be blocked.

In [Fig. 4](#page-4-0), the P-S-F algorithm is detailed step-by-step. On each core, let FSs 1 to *m*1 be dedicated for allocating high-priority traffic, FSs *m*1 + 1 to *m*2 for mid-priority traffic, and FSs *m*2 + 1 to *n* for low-priority traffic. Until reaching *Remain\_FSs* to zero, cores are searched one by one to setup the FSs required for a new connection request. The allocation is tried for *K* shortest path routes, and on all cores on each path. In Line 3, *path* is obtained. In Lines 5, 20, and 35, connection priority is checked in order to start the allocation in the appropriate segment. In Lines 5–20 if connection priority is high, FS allocation is checked in each core. At the end, if *Remain\_FSs* = 0, we can setup the whole connection on the assigned spectrums on different cores. Otherwise, the connection will be blocked. The degree of complexity for P-S-F is O(*K* × *C* × *D* × *n*), where O(*D* × *n*) denotes the degree of complexity for running *Find\_-First\_Free\_Gap*().

## *3.2. Priority Select core (P-S-CO)*

Let Spectrum Block (SB) be the set of back-to-back FSs in spectra. The P-S-CO algorithm is based on the multipath concept. Multipath is a mechanism to make a connection request in multi-part spectrum blocks in multiple routes between source and destination through cores. In our research, the spectrum and core assignment solution in MCF is considered. We use the Spectrum and Core Assignment mechanism based on Core Partitioning considering the required bandwidth of connection requests. In Core Partitioning, cores are prioritized. For instance, as

shown in Fig. 5, cores with index 1 to 3 are solely used for accommodating high-priority connections. Cores with index 4 to 6 are only used to accommodate mid-priority connections. Core 7 is used for the allocation of low-priority connections. Here, on the arrival of a new highpriority connection, Cores 1 to 3 are checked. Since Core 1 has free FSs, it is chosen to allocate the connection.

In [Fig. 6](#page-6-0), the P-S-CO algorithm is depicted step by step in order to set up a new connection request in one of the *K* shortest paths. Until reaching *remain\_FS* to zero, specified cores are searched to setup the FSs to the new arriving connection request. Here, Cores 1 to *priority*1*\_core*  are for high-priority connections. Cores *priority*1*\_core* + 1 to *priority*2*\_core* are used for mid-priority connections, and Cores *priority*2*\_core*  + 1 to *C* are used for low-priority connections. In Line 2, *path* is defined. Then, in Lines 3, 15, and 27, connection priority is checked in order to start the allocation in an appropriate core.

At the end, if we have *Remain\_FSs* = 0, we can setup the whole connection on the assigned spectrums on different cores. Otherwise, the connection will be blocked. The degree of complexity for P-S-CO is O(*K*  × *C* × *D* × *n*), where O(*D* × *n*) denotes the degree of complexity for running *Find\_First\_Free\_Gap*().

### **4. Performance evaluation**

We evaluate the performance of the P-S-F, P-S-CO, SBMC [\[2\]](#page-8-0), and Classified-Core [\[42,43\]](#page-9-0) algorithms in the NSFNET topology with 14 nodes and 21 links with *C* = 7 cores, where each EON node can be designed based on the architectures stated in [\[46\].](#page-9-0)

In this evaluation, we consider that there are *n* = 300 FSs per core. The number of FSs for an arriving connection request is distributed uniformly between 10 and 20 FSs. The routing for all evaluated algorithms are the *K*-shortest path through physical distance between a given source and destination pair at *K* = 2. Holding time *h* is distributed exponentially with mean 10 ms and network load is assumed to be 200–700 Erlangs, where network load (in Erlang) follows *E*= *µ* × *h* in which *µ* is connection arrival rate and *h* is the mean connection holding time. We have simulated the network in OPNET14 in Windows 8 with 8 GB ram. We consider the NSFNET network topology with 14 nodes used in [\[29\].](#page-9-0)

In simulation, it is assumed that 30 % of arriving connections have low-priority, 30 % of arriving connections have mid-priority, and 40 % of arriving connections have high-priority. In the P-S-F algorithm, we allocate connections with different priorities on each core. In this way, slots with indexes from 1 to *m*1 = 150 are used for high-priority connections and slots 151 to *m*2 = 250 are allocated for mid-priority connections. Then, slots 251 to *n* = 300 are allocated for low-priority traffic. On the other hand, in the P-S-CO algorithm, Cores 1 to *priority*1*\_core* = 3) are only used for high-priority connections, Cores 4 to *priority*2*\_core* = 6)

**Fig. 6.** The P-S-CO algorithm.

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

**Fig. 7.** Blocking probability in P-S-F, P-S-CO, SBMC, and Core-Classification Algorithms.

![](_page_7_Figure_4.jpeg)

**Fig. 8.** Bandwidth blocking probability simulation results on P-S-F, P-S-CO, SBMC, and Core Classification.

are dedicated for mid-priority connections, and core *C* = 7 is allocated to low-priority connections. Note that in SBMC and Core-Classification, all connections are considered to have the same priority.

Each point of a diagram in the following diagrams is averaged for 1,000,000 connection requests and from 15 simulation replications. The simulation results are displayed with 95 % confidence interval within 2 % of their real mean values. Performance parameters used in our implementation are defined as:

- Blocking probability (BP) [\[2\]](#page-8-0) is calculated by the proportion of the number of blocking connections to all coming connections in the network.
- Bandwidth Blocking Probability (*BBP*) [\[2\]](#page-8-0) is calculated by the proportion of the blocked requested bandwidth to the bandwidth requirements of all coming connections computed by Eq. (2). Here, *B*  shows the set of blocked connections, *ARV* shows the set of all coming connections, and *bi* is the amount of bandwidth requirement in frequency slots for connection *i.*

$$BBP = \frac{\sum_{i \in B} b_i}{\sum_{i \in ARV} b_i} \tag{2}$$

• Spectrum Utilization (*SU*) [\[2\]](#page-8-0) is the metric of spectrum efficiency calculated by Eq.(3). Here, *SC* is the set of setup connections and *HTi*  is the holding time of connection *i*. Parameter *TotalSpectrum* is the number of FSs on each core and *SimulationTime* is the simulation time carried out for 1,000,0000 connection arrivals.

![](_page_7_Figure_12.jpeg)

**Fig. 9.** Spectrum utilization simulation results on P-S-F, P-S-CO, SBMC, and Core-Classification.

![](_page_7_Figure_14.jpeg)

**Fig. 10.** Blocking probability for low, mid and high priority connections in P-S-F and P-S-CO.

$$SU = \frac{\sum_{i \in SC} b_i \times HT_i}{Total Spectrum \times Simulation time}$$
 (3)

In Fig. 7, P-S-F and P-S-CO are simulated and their results are compared with the Core-Classification and SBMC algorithms. Here, BP for SBMC and Core–classification is bigger than P-S-F. The P-S-F improves BP because it tries to control fragmentation in cores. However, the results of Core-Classification and SBM are similar in reducing BP. As it can be observed, P-S-CO has the lowest blocking probability in bandwidth. Thus, we can control fragmentation when cores are classified and spectrum can be allocated effectively. The P-S-CO improves BP because it tries to control fragmentation in cores.

In Fig. 8, Bandwidth Blocking Probability (BBP) under P-S-F, P-S-CO, Core-Classification and SBMC are shown. The BBP in P-S-CO is lower than other algorithms, and therefore, P-S-CO is the best proposed algorithm among them. In addition, P-S-F has good performance in BBP in comparison with SBMC and core-classification. In Fig. 8, BBP in P-S-F has better performance than both Core–Classification and SBMC because P-S-F tries to setup connections by considering spectrum blocks through the multipath mechanism and classified cores technique. As it can be observed, P-S-CO has good results in blocking bandwidth probability. The BBP in P-S-CO is lower than both Core–Classification and SBMC because P-S-CO tries to make spectrum blocks based on the multipath mechanism with considering the classified cores technique.

Fig. 9 illustrates overall spectrum utilization (SU) blocking under P-S-F, P-S-CO, Core-Classification and SBMC. We can observe that P-S-F has better performance than Core-Classification and SBMC. By increasing SU in bandwidth, this algorithm presents better performance than the others in controlling of fragmentation. The P-S-CO algorithm has better performance than other three algorithms (P-S-F, Core-Classification and SBMC) in comparison. By increasing SU in

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

**Fig. 11.** Bandwidth blocking probability for low, mid and high priority traffic in P-S-F and P-S-CO.

![](_page_8_Figure_4.jpeg)

**Fig. 12.** Spectrum Utilization for low, mid and high priority connections in P-S-F and P-S-CO.

**Table 1**  The minimum and maximum percentage of performance improvements of P\_S\_Co and P\_S\_F compared to SBMC and core-classifications.

| Improvement<br>of | Compared to         | BP (min,<br>max)<br>percentage | BBP(min,<br>max)<br>percentage | SU (min,<br>max)<br>percentage |
|-------------------|---------------------|--------------------------------|--------------------------------|--------------------------------|
| P_S_Co            | SBMC                | (3.8, 11.3)                    | (6.8, 10.5)                    | (2.5, 5)                       |
| P_S_Co            | core_classification | (7.4, 15.2)                    | (7.2, 25)                      | (1.3, 5)                       |
| P_S_F             | SBMC                | (0, 9.1)                       | (4.5, 14.8)                    | (0, 3. 7)                      |
| P_S_F             | core_classification | (7.2, 9.1)                     | (5.4, 17.8)                    | (0, 3. 7)                      |

bandwidth, this algorithm presents better performance than the others in controlling of fragmentation. Spectrum utilization in P-S-CO is better than other algorithms, and therefore, P-S-CO is the best proposed algorithm. In addition, P-S-F has good performance in spectrum utilization in comparison with SBMC and core-classification.

In [Figs. 10, 11, and 12,](#page-7-0) blocking probability, bandwidth blocking probability and spectrum utilization are respectively illustrated for three low, mid, high priority connections under P-S-F and P-S-CO algorithms. In [Fig. 10](#page-7-0), in P-S-F, BP rate of low-priority connections is more than both high and mid-priority connections, because we have specified less number of FSs for low-priority connections. Besides, the situation under P-S-CO is the same as for P-S-F.

In Fig. 11, under P-S-F, BBP for low-priority connections is more than high and mid-priority connections, because the number of FSs used for low-priority connections is lower than both mid and high-priority connections. This situation is the same for both P-S-CO and P-S-F.

In Fig. 12, under the P-S-F, the SU rate of low-priority connections is lower than high and mid-priority connections because the number of FSs used for low-priority connections is lower than both high and midpriority connections.

Based on our analysis, the P-S-CO algorithm can provide better performance result in controlling fragmentation in MCF. By controlling fragmentation, spectra can be utilized in a better way so that the chance of establishing new connections is increased. This is because partitions under P-S-CO are made on cores, and each connection is accommodated in a specific core so that any FS in the whole spectrum of the core can be allocated to a given connection. However, under P-S-F, there is restriction on the FSs on a core to be given to a connection.

In summary, Table 1 depicts the obtained improvements of both P\_S\_Co and P\_S\_F compared to the SBMC and core-classifications methods under the evaluated traffic loads (200 to 700 Erlang) in terms of three performance parameters (BP, BBP and SU). For each performance parameter, two minimum and maximum improvements have been illustrated. For instance, the BP value of P\_S\_Co is improved by at least 3.8 % and at most 11.3 % under different traffic loads compared to the SBMC method.

### **5. Conclusion**

In this research, we have proposed two fragmentation-aware mechanisms for dynamic traffic in class-based EON networks. The P-S-F algorithm uses multipath and core classification mechanism together and FS segments are specified in each core for three priority connections. In the P-S-CO algorithm, similar to P-S-F, multipath and core classification are used on each core. However, each core can be completely used for a specific class of traffic. We improve connection blocking and spectrum utilization in the network by both the P-S-F and P-S-CO algorithms. However, the P-S-CO can provide the best results among other algorithms in BP reduction and spectrum utilization increase because it is based on multipath mechanism and classified cores. In future work, we will consider crosstalk as a limitation on establishing connection demands under links with MCF.

### **CRediT authorship contribution statement**

**Mahdiyeh Hafezi:** Conceptualization, Methodology, Software, Writing – original draft. **Akbar Ghaffarpour Rahbar:** Supervision, Writing – review & editing.

### **Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### **Data availability**

No data was used for the research described in the article.

### **References**

- [1] [Y.T.M. Jinno, Y. Sone, Sh. Matsuoka, Spectrum-efficient and scalable elastic optical](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0005)  [path network: architecture, benefits, and enabling technologies, IEEE](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0005) [Communications Magazine 47 \(11\) \(2009\)](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0005).
- [2] [F. Yousefi, A. Ghaffarpour-Rahbar, Novel fragmentation-aware algorithms for](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0010)  [multipath routing and spectrum assignment in elastic optical networks-space](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0010) [division multiplexing \(EON-SDM\), Optical Fiber Technology 46 \(2018\) 287](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0010)–296.
- [3] [P. Sayyad Khodashenas, S. Spadaro, J. Perello,](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0015) ´ G. Junyent, Using spectrum [fragmentation to better allocate time-varying connections in elastic optical](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0015) [networks, Opt. Commun. Netw. 5 \(6\) \(2014\) 4433](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0015)–4440.
- [4] J.Socrates-Dantas, ´ D.Careglio, J.Roberto Amazonas, J.Sol`e-Pareta, and W.Vicente Ruggiero. "A Study in Current Dynamic Fragmentation-Aware RSA Algorithms". in ICTON. 2014. Sao Paulo, Brazil.. Universitat Polit`ecnica da Catalunya, Barcelona, Espana. ˜
- [5] [X. Yu, J.Z., V. Yu, J. Zhang, X. Lin, Fragments-minimum spectrum allocation](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0025) [algorithm in flexible bandwidth multi-fiber optical network, Proc.OFC](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0025)'12 (2012) [1](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0025)–3.
- [6] [W. Lu, Z. Zhu, Dynamic service provisioning of advance reservation requests in](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0030)  [elastic optical networks, Journal of Lightwave Technology 31 \(10\) \(2013\)](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0030) 1621–[1627.](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0030)

- <span id="page-9-0"></span>[7] P.M. Moura, N.L. S. da Fonseca, and R.A. Scaraficci "Fragmentation Aware Routing and Spectrum Assignment Algorithm", in IEEE International Conference on Communications (ICC), 2014, Sydney, NSW, Australia.
- [8] A.Pag`es, J.Perello, ´ and S.Spadaro, "Lightpath Fragmentation for Efficient Spectrum Utilization in Dynamic Elastic Optical Networks", 2012, 16th International Conference on Optical Network Design and Modelling (ONDM), Colchester, UK, 2014.
- [9] [Y. Yin, M. Zhang, M. Xia, Z. Zhu, S. Dahlfort, S.J.B. Yoo, Spectral and spatial 2D](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0045)  [fragmentation aware routing and spectrum assignment algorithms in elastic optical](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0045)  [networks \[invited\]. A100, J. Opt. Commun. Netw. 5 \(10\) \(2013\)](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0045).
- [10] Yawei Yin, M.Z., Zuqing Zhu, and S. J. B. Yoo, "Fragmentation-Aware Routing, Modulation and Spectrum Assignment Algorithms in Elastic Optical Networks", in OFC/NFOEC Technical Digest. 2013, University of Science and Technology of China, Hefei: Univ. of California, Davis.
- [11] L. Liu, Z. Zhu , and S.J. Ben Yoo, "3D Elastic Optical Networks in Temporal, Spectral, and Spatial Domains with Fragmentation-Aware RSSMA Algorithms", in Department of Electrical & Computer Engineering, University of California , University of Science and Technology of China, Hefei, 2014.
- [12] [R. Proietti, L. Liu, B. Guan, R.P. Scott, B. Guan, C. Qin, T. Su, F. Giannone, S.J.](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0060)  [B. Yoo, 3D elastic optical networking in the temporal, spectral, and spatial](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0060)  [domains, IEEE Communications Magazine 53 \(2\) \(2015\) 79](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0060)–87.
- [13] [F. Yousefi, A. Ghaffarpour Rahbar, M. Yaghubi-Namaad, Fragmentation-aware](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0065)  [algorithms for multipath routing and spectrum assignment in elastic optical](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0065) [networks \(EON\), Optical Fiber Technology \(2019\) 53](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0065).
- [14] [F. Yousefi, A. Ghaffarpour Rahbar, A. Ghadesi, Fragmentation and time aware](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0070)  [algorithms in spectrum and spatial assignment for space division multiplexed](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0070)  [elastic optical networks \(SDM-EON\), Computer Networks 174 \(2020\) 19.](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0070)
- [15] [S.B.Y. AwajiJun, J. PuttnamRuben, S. LuísJose, M. Delgado, High-capacity](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0075)  [transmission over multi-core fibers, Optical Fiber Technology 35 \(2016\) 100](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0075)–107.
- [16] [T. Mizuno, Y. Miyamoto, High-capacity dense space division multiplexing](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0080)  [transmission, Optical Fiber Technology 37 \(2017\) 108](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0080)–117.
- [17] [G.M. Saridis, D. Alexandropoulos, G. Zervas, D. Simeonidou, Survey and evaluation](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0085)  [of space division multiplexing: from technologies to optical networks, IEEE](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0085)  Communications Surveys & [Tutorials 17 \(4\) \(2013\) 2136](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0085)–2156.
- [18] [M. Klinkowski, P. Lechowicz, K. Walkowiak, Survey of resource allocation schemes](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0090)  [and algorithms in spectrally-spatially flexible optical networking, Optical](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0090)  [Switching and Netowrking 27 \(2018\) 58](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0090)–78.
- [19] [H. Yang, J. Zhang, Y. Zhao, S. Wang, W. Gu, J. Han, Y. Lin, Y. Lee, Multi-flow](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0095)  [virtual concatenation triggered by path cascading degree in Flexi-Grid optical](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0095) [networks, Optical Fiber Technology 19 \(2013\) 604](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0095)–613.
- [20] [A. Agrawal, U. Vyas, V. Bhatia, S. Prakash, SLA-aware differentiated QoS in elastic](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0100)  [optical networks, Optical Fiber Technology 36 \(2017\) 41](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0100)–50.
- [21] [B. Chand Chatterjee, S. Ba, E. Oki, Fragmentation problems and management](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0105) [approaches in elastic optical networks: a survey, IEEE Communications Surveys](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0105) & [Tutorials 20 \(1\) \(2018\) 183](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0105)–210.31. First quarter.
- [22] [S. Hanczewski, M. Stasiak, J. Weissenberg, Non-full-available queueing model of](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0110) [an EON node, Optical Switching and Netowrking 33 \(2019\) 131](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0110)–142.
- [23] [M.A. Cavalcante, H.A. Pereira, D.A.R. Chaves, R.C. Almeida Jr., Optimizing the](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0115)  [cost function of power series routing algorithm for transparent elastic optical](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0115)  [networks, Optical Switching and Netowrking 29 \(2018\) 57](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0115)–64.
- [24] [A. Muhammad, G. Zervas, R. Forchheimer, Resource allocation for space division](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0120) [multiplexing: optical white box vs. optical black box networking, Journal of](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0120)  [Lightwave Technology 33 \(23\) \(2015\) 4228](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0120)–4941.
- [25] Y.Hirota, Y.Hatada, T.Watanabe, and H. Tode "Dynamic Spectrum Allocation Based on Connection Alignment for Elastic Optical Networks". Symposium on Information and Telecommunication Technologies, 2015, Colombo, Sri Lanka.
- [26] H. Tode and Y. Hirota, "Routing, Spectrum and Core Assignment for Space Division Multiplexing Elastic Optical Networks". 2014, 16th International Telecommunications Network Strategy and Planning Symposium Networks, Funchal, Portugal, 2014.
- [27] [Y. Khorasani, A. Ghaffarpour Rahbar, M. Jafari-Beyrami, A novel two-dimensional](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0135)  [metric for fragmentation evaluation in elastic optical networks, Computer](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0135) [Networks 216 \(2022\)](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0135).

- [28] L.H. Bonani, M. Forghani-elahabad, M.L.F. Abbade, "Network Fragmentation Measure in Elastic Optical Networks", 2019, SBFoton International Optics and Photonics Conference (SBFoton IOPC), Sao Paulo, Brazil.
- [29] [F. Yousefi, A. Ghaffarpour-Rahbar, Fragmentation-aware algorithms in space](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0145) [division multiplexed- elastic optical networks \(SDM-EON\) with considering](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0145)  [physical layer security, Optical Switching and Networking 37 \(2020\).](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0145)
- [30] [F. Shirin Abkenar, A. Ghaffarpour Rahbar, A. Ebrahimzadeh, Providing quality of](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0150)  [service \(QoS\) for data traffic in elastic optical networks \(EONs\), Arabian Journal](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0150) [for Science and Engineering \(2015\)](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0150).
- [31] A. Agrawal, V. Bhatia, S. Prakash, Low-Crosstalk-Margin Routing for Spectrally-Spatially Flexible Optical Networks, IEEE Communications Letters 24. (4), 835- 839.
- [32] P. Majumdara and T. De, "De-multiplexing the required spectrum in a traffic demand into multiple non-adjacent granular spectrums for dynamic traffic grooming in EON", Optical Switching and Netowrking, 2018. In Press, Accepted Manuscript.
- [33] [R. Costa, N. Ramos, C. Drummond, Leveraging adaptive modulation with multi](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0165)[hop routing in elastic optical networks, Computer Networks 105 \(2016\) 124](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0165)–137.
- [34] [R. Gos, K. Walkowiak, M. Klinkowski, Tabu search algorithm for routing,](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0170) [modulation and spectrum allocation in elastic optical network with anycast and](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0170) [unicast 5 Q1 traffic, Computer Networks 79 \(C\) \(2015\) 148](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0170)–165.
- [35] R.Zhu, J.P.Jue, A.Yousefpour, Y.Zhao, H.Yang, J.Zhang, X.Yu , N.Wang "Multipath Fragmentationaware Advance Reservation Provisioning in Elastic Optical Networks", in 2016 IEEE Global Communications Conference (GLOBECOM). 2016: Washington, DC, USA.
- [36] Vasundhara , A.Mandloic , and M.Patel, "Fragmentation Coefficient (FC) conscious Routing, Core and Spectrum Allocation in SDM-EON based on MultiCore Fiber", 2023 2nd International Conference on Paradigm Shifts in Communications Embedded Systems, Machine Learning and Signal Processing (PCEMS), Nagpur, India, 2023.
- [37] Anjali Sharma, B.Singh Heera, V.Lohani , and Y.Nath Singh, "Fragmentation-Aware Routing, Core and Spectrum Assignment in Multi-Core Fiber based SDM-EON", 2022 Workshop on Recent Advances in Photonics (WRAP), Mumbai, India, 2022.
- [38] [N. Kitsuwan, P. Pavarangkoon, A. Nag, Elastic optical network with spectrum](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0190)  [slicing for fragmented bandwidth allocation, Optical Switching and Networking 38](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0190)  [\(2020\), 100583.](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0190)
- [39] [S. Selvakumar, S.S. Manivannan, A spectrum defragmentation algorithm using](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0195)  [jellyfsh optimization technique in elastic optical network \(EON\), Wireless Personal](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0195)  [Communications 127 \(2022\) 1187](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0195)–1205.
- [40] [S. Selva Kumar, J. Kamalakannan, R. Seetha, N. Asha, K.T. Raja, S. Sree Dharinya,](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0200)  [M. Sucharitha, S. Kalaivani, The effectual spectrum defragmentation algorithm](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0200) [with holdingtime sensitivity in elastic optical network \(EON\), International](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0200)  [Journal of Optics \(2022\).](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0200)
- [41] [B.C. Chatterjee, N. Stol, E. Oki, Impairment-aware spectrum allocation in elastic](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0205) [optical networks: a dispersion-sensitive approach, Optical Fiber Technology 61](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0205) [\(2021\), 102431.](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0205)
- [42] [X. Yu, Y.Z., J. Zhang, V. Yu, J. Zhang, X. Lin, Fragments-minimum spectrum](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0210)  [allocation algorithm in flexible bandwidth multi-fiber optical network, Proc. OFC](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0210)' [12 \(2012\) 1](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0210)–3.
- [43] S. Fujii, Y. Hirota, T. Watanabe, and H. Tode "Dynamic Spectrum and Core Allocation with Spectrum Region Reducing Costs of Building Modules in AoD Nodes", 2014, 16th International Telecommunications Network Strategy and Planning Symposium (Networks) in Department of Information Networking. 2014: Japan.
- [44] Y.Hirota, Y.Hatada, T.Watanabe, and H. Tode, "Dynamic spectrum allocation based on connection alignment for elastic optical networks," In: 2015 10th Asia-Pacific Symposium on Information and Telecommunication Technologies (APSITT), 2015: IEEE, pp. 1–3.
- [45] [Y. Khorasani, A. Ghaffarpour Rahbar, M. Jafari-Beyrami, Fragmentation](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0225) [management to reduce bandwidth wastage in SDM-EON network, Photonic](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0225)  [Networks Communication \(2023\)](http://refhub.elsevier.com/S1068-5200(23)00403-0/h0225).
- [46] N. Amaya, G.S. Zervas, D. Simeonidou, "Optical node architectures for elastic networks: From static to architecture on demand," 2012, 14th International Conference on Transparent Optical Networks (ICTON), Coventry, UK.
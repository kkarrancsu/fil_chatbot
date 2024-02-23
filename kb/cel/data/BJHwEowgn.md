---
tags: Gas, Research proposals, Almanac
---

# Gas consumption pre and post-FEVM launch. One week in


We compare gas consumption in Filecoin pre and post-FEVM launch. All data was obtained from either Sentinel or starboard. 


### TL;DR:

Following up on our network monitoring efforts, we analyzed gas consumption and user behavior one week after FEVM launch. Our key observations can be summarized as follows:
- The average base fee increased post-FEVM, mostly oscillating around 0.2-0.6 nanoFIL/gas unit. Historically, this puts the current base fee above the 75% quantile. This range is about 1.5 orders of magnitude below the critical limit estimated before of 10nanoFIl gas per gas unit. We also did not detect any trend, hourly seasonality, or evidence it will keep increasing (or decreasing). 
- The statistical distribution of gas usage per block has remained relatively stable after the upgrade. However, we observe a slight shift in the proportion of full or almost full blocks, which helps explain the increase in the base fee. 
- Observing the tips to the miner associated with each kind of message, we observed that while a few FEVM messages had significantly larger miner tips, the majority did not tip substantially more than other methods.
-  It is still too early to draw meaningful conclusions. However, there are no strong indicators of gentrification (or sprawl).






### Base fee.


One of the quantities we are most interested in monitoring is the base fee (the minimum cost of sending a message in terms of FIL per gas unit), as a scenario that we would like to avoid is having base fees that are so high that they interfer with the "normal" network maintenance messages. In order to investigate this quantity, we plot below the time series of the base fee (top left), its statistical properties (top right), and a box-and-whiskers plot of its distribution, both in nanoFIL/gas unit (bottom left) and in logarithmic scale (bottom right).



| ![](https://hackmd.io/_uploads/BkunUKjg2.png) | ![](https://hackmd.io/_uploads/SJGpvYse2.png) |
|---|---|
|  ![](https://hackmd.io/_uploads/HyXDDFjen.png) | ![](https://hackmd.io/_uploads/ByimPtoeh.png)  |

We observe the following: 
- The **average base fee has increased after FEVM**. This increase could be due to various reasons. One of them is that it is often the case that the base fee increases after a network upgrade due to, e.g., recoveries, etc.   In any case this warrants monitoring.
- We note that the standard deviation of the base fee has slightly increased after FEVM. Since base fees can rapidly vary among scales, this more significant standard deviation is a byproduct of having a base fee oscillating around larger values.
- It is worth noting that the data used to compute the pre-FEVM statistics includes periods of very low network usage, which will naturally skew the mean towards smaller values. Indeed, there have been periods pre-FEVM where the base fee has been comparable (or larger) than what it currently is. 
- During this week of data, the base fee has oscillated around 0.4 nanoFIL/ gas unit and reached a **maximum of 2.34 nanoFIL/gas unit.** This is still lower than the all-time high of 4.08 nanoFIL/gas unit.
- Historically, the base fee has had a 75% quantile of roughly 0.3 nanoFIL per gas unit, which means that the base fee has been oscillating at or above such a quantile. 
- We also note that, for the time considered, the base fee has concentrated around the same scale, with about 50% of the epochs having a base fee between 0.25 and 0.5 nano FIL/gas unit. This is the opposite of the pre-FEVM gas consumption, where gas fee had oscillated around several orders of magnitude. In any case, this suggests that, even though the base fee is slightly high, the network is *stable* in the amount of gas that it has been using.
- The base fee oscillates around a relatively high value, but there is no immediately apparent trend (in either direction)  as shown below. This suggests that we are not at immediate risk of either *gentrification* or *sprawl*; however, it is still too close to make any meaningful conclusions. 
-  We detected a mild seasonality with respect to the hour of the day, morning and afternoon (UTC). However, we deem this to not be particularly significant (about ±0.05 nanoFIL per gas unit).



![](https://hackmd.io/_uploads/BkSAohie2.png)



### Gas usage



We plot a histogram of the gas used. Notice that such data is presented relative to the maximum block size; thus, a value of gas used= 0.5 implies that such a block uses 50% of the maximum block size (i.e., the target block size). We observe the following.

- The distribution of gas usage pre and post-FEVM are similar to one another, as can be seen from the histogram below. The most salient feature among these distributions, however, is that pre-FEVM, there's a more significant mass around 0.5 (i.e., the target). At the same time, for post-FEVM, there's a more prominent peak around 1, which indicates that the proportion of very full blocks increased post launch.


![](https://hackmd.io/_uploads/Byb3iYjg3.png)

We now investigate the gas usage per method pre-and post-FEVM. Here,  we are denoting as FEVM messages those from the `evm`, `eam`, `placeholder`, and `ethaccount` actor families. Messages classified as "Other" *do not* belong to these families. 







- We can see that, while at launch, there were some FVM-specific messages (such as `InvokeContract,` for example), **the total gas usage has remained relatively stable and comparable to pre-launch**. 

- The total amount of daily gas used post-launch has remained under 50 Trillion, at roughly 45 Trillion daily gas units. **This averages out to about  3.125 Billion gas units per block**, which is **below** the target gas utilization of 5 Billion gas units. 
- We observe an increase in the daily gas used by `proveCommitAggregate .`In particular, this value has been osciallting around 4-6T gas units per day. This is slightly larger than the amount of gas consumed by such a method in the past 180 days. However, it's still below historical maximums of about 9.5T daily gas units. Presumably, this is due to (1) network QAP growing (even if slowly) and (2) the current relatively high base fees.

![](https://hackmd.io/_uploads/rkAegcoe2.png)




![](https://i.imgur.com/zVPtSJO.png)




### User behavior



We now investigate user behaviour based on the amount of tips paid to the miner. Our goal here is to understand whether FEVM-related messages are outpricing the others. We show a box plot of the miner tips (in FIL) per method below. Given that miner tips can span several orders of magnitude, we plot them on a logarithmic scale. We also show the summary statistics below. 

![](https://hackmd.io/_uploads/Hkn-TAYgn.png)


| names                |       count |        mean |        std |          25% |         50% |         75% |       max |
|:---------------------|------------:|------------:|-----------:|------------:|------------:|------------:|----------:|
| FEVM                 | 58479  | **0.0255**   | **0.121066**   |  1.05895e-06 | 1.63993e-05 | 0.00024 | **12.6949**   |
| Other                | 237580  | 0.00168  | 0.029709   |  3.09626e-06 | 1.93454e-05 | 0.00012 |  9.18568  |
| PreCommitSector      | 933520 | 0.00025 | 0.00107357 |  1.4035e-05  | 5.09439e-05 | 0.00017 |  0.38268 |
| PreCommitSectorBatch | 42365 | 0.00063 | 0.0133425  |  2.08374e-05 | 9.8493e-05  | 0.00034 |  1.87019 |
| ProveCommitAggregate | 17556  | 0.01012  | 0.0444294  |  **0.00054797**  | **0.00218079**  | **0.00793**  |  1.84301  |
| ProveCommitSector    | 987350 | 0.00057 | 0.0134091  |  2.67058e-05 | 9.66649e-05 | 0.0003241 |  1.93945  |
| PublishStorageDeals  | 206830 | 0.00290  | 0.0141231  |  0.000145503 | 0.000555826 | 0.002141   |  2.43892  |
| SubmitWindowedPost   | **1006723** | 0.00033 | 0.00272601 | 1.00329e-05 | 4.3305e-05  | 0.000151 |  1.41609  |


We can observe a few interesting features from the figures above:
- At first glance  there does not seem to be a very significant difference among the distributions of miners tips among these methods, particularly when looking at their spread, however;
- The **average** miner tip for FEVM methods is much larger than the ones for the others. It is around the same order of magnitude as that of `ProveCommitAggregate`. Its **standard deviation** (a measure of how *spread out* this data is) is also the largest, which suggests there is a wide variation in this category.
-  It is also shown that the **medians** across all categories are around the same order of magnitude, which suggests that this increase in the average tip on FEVM messages is skewed to the higher values due to a relatively small number of messages. Indeed, while **batching methods** (i.e., `ProveCommitAggregate` and `PreCommitSectorBatch`), as well as `PublishStorageDeals` tend to have the largest 50% and 70% quantiles** (meaning that, in terms of frequency, they tend to be the ones with the largest miner tips), the maximum tip due to **FEVM or Other** categories is about an order of magnitude larger than the others, with the largest miner tip examined having a value of **12 FIL in a single message** (with `cid=bafy2bzacebzkveaurmnyuzqk2xwuilvcnmp65us43wed3a3r4euumiv4olmzy`). 
- It is also worth noting that FEVM is also the group of tips with the **smallest** 25% and 50% quantile. Furthermore, its 75% quantile is of a comparable magnitude as the others.  
- In a sense, while there are a few FEVM-message-sending users that are willing to tip the miners unusually large amounts to include their messages, the **majority** of these messages do not tip a substantially larger amount. For the moment, this shows **no evidence** of a large-scale *gas gentrification*, where the **majority** of FEVM messages are tipping a substantially larger amount (and hence, potentially outbidding network maintenance messages). 


Motivated by the discussion above, we examine miner tips' top 10% (above 0.0008 FIL). Our results are shown in the figures below. Our observations confirm what is discussed above, indeed;

- Indeed, **for the top 10% of messages by miner tip,** there is a significant difference between the distribution of miner tips from FEVM compared to the others; in particular, the **median** in this setting is about **an order of magnitude larger than the others**. 
- Furthermore,  we can see that all distributions have a long right tail.




![](https://hackmd.io/_uploads/HkNaTDsx2.png)


|                      | count      | mean       | std        | min         | 25%        | 50%        | 75%        | max      |
|----------------------|------------|------------|------------|-------------|------------|------------|------------|----------|
|                 FEVM |  8256 |   **0.180393** |   **0.275496** | 0.000853012 | 0.00166402 |  0.0309144 |    0.33736 |  12.6949 |
|                Other |  19130 |  0.0198311 |   0.102973 | 0.000852791 | 0.00118616 | 0.00171984 | 0.00500126 |  9.18568 |
|      PreCommitSector | **51126** | 0.00269551 | 0.00378625 | 0.000852824 | 0.00151333 | 0.00207061 | 0.00272152 | 0.382681 |
| PreCommitSectorBatch |  4616 | 0.00452468 |  0.0402104 | 0.000853264 | 0.00128536 | 0.00182995 | 0.00255935 |  1.87019 |
| ProveCommitAggregate | 11388 |  0.0154825 |  0.0544342 | 0.000852808 | 0.00230434 |  0.0056797 |  0.0147409 |  1.84301 |
|    ProveCommitSector | 92921 | 0.00454204 |  0.0435069 | 0.000852766 | 0.00111852 | 0.00213472 | 0.00403029 |  1.93945 |
|  PublishStorageDeals | 87161 | 0.00652469 |  0.0212273 | 0.000852767 | 0.00145519 | 0.00266964 |  0.0054028 |  2.43892 |
|   SubmitWindowedPost |  7445 | 0.00338688 | 0.00949791 | 0.000852781 | 0.00116437 | 0.00187022 | 0.00328532 |  1.41609 |

These figures help us *paint a picture* of the users' demand profile and price elasticity. Indeed, the data above suggest that there **are a few** FEVM messages that are more price-inelastic than for the other methods; however, for the majority of the messages, this inelasticity does not hold true. 


### Conclusions 




The average base fee increased after the FEVM launch, but there's no clear trend that suggests immediate risks of gentrification or sprawl. The network seems stable, but monitoring is required to draw more meaningful conclusions.

Gas usage distribution remained relatively stable and comparable to pre-launch levels, with no significant impact on network capacity or utilization.

While a few FEVM messages had more significant miner tips, most were in line with other methods. There's no evidence of large-scale gas gentrification, but ongoing monitoring is necessary.

Users' demand profile and price elasticity indicate that a small number of FEVM messages are more price-inelastic than other methods. Still, the majority of messages do not display this behavior. Further observation is needed to understand the long-term effects on the network.
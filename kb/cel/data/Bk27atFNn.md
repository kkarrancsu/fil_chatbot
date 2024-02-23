# Recent trends in network costs. 

Some storage Providers have flagged that they noticed an increased spending on FIL spent for messages to the chain starting in March of this year. In this short report, we investigate recent trends in base fee, gas usage, and FIL spent by (a) the network and (b) two specific SPs who were kind enough to provide us with their miner ids. Our findings are summarized below.

- *Base fees*: Analysis shows that the base fee has been more volatile in 2023 than in 2022, with a notable increase in volatility since around mid-February 2023. The report suggests that this is not solely due to the Filecoin-Ethereum Virtual Machine (FEVM) introduction but also due to other factors, such as network growth. 
- *FIL Spent:* There is an increased volatility in FIL spent during 2023 starting from around mid-February, stemming from the pattern seen in base fees. Despite the increased volatility, the average spending has remained comparable to other periods of high network activity.
- *Gas Usage*: Overall, we found a slight decreasing trend in the amount of gas used by the `PreCommitSector,` `ProveCommitSector,` and `SubmitWindowedPost` methods. However, there has been a significant increase in the gas used by `PublishStorageDeals` since December 2022, likely due to the implementation of FIP0045.
- *Case studies*: The report finally investigates two specific SPs that we will denote as SP A and SP B. Both SPs have seen an increase in FIL spent, partly due to the above reasons; however, SP-specific factors, such as increased data onboarding, have also contributed to their specific cost increase.


We now describe each of these findings in more detail.

### Base fees.

We begin by examining the base fees. Bellow, We show a plot of the *daily average base fee* (FIL/gas unit) in the Filecoin network together with its summary statistics. We observe the following:

- Base fee has been more volatile and, on average, 30% larger in 2023 than in 2022. While it is tempting to attribute this increase in base fee to the introduction of the Filecoin-Ethereum Virtual Machine (FEVM), it is worth noting that the volatility for such a base fee has been increasing since around one month before FEVM launched. Furthermore, as described [here](https://hackmd.io/@cryptoecon/HyED5m4f2), the gas usage due to FEVM has been significantly smaller than for non-FEVM-related messages. This suggests that increased volatility in base fees can be attributed --at least partly-- to other factors, such as higher network activity and growth. 
- the 25% and 50% quantiles have been smaller in 2023 than in 2022. This roughly means that the bottom 50% of epochs (in terms of base fee) in 2023 have had a smaller base fee than the bottom 50% of epochs in 2022.
- However, there have been more significant spikes and faster fluctuations of the base fee in 2023; that is to say that it has become more volatile than in 2022. This claim is also evidenced in the higher standard deviation for the base fee during 2023. 





| ![](https://hackmd.io/_uploads/rJt6I9KVn.png)| ![](https://hackmd.io/_uploads/Hk_8B09En.png)|
| -------- | -------- | 
| *Daily average base fee (FIL/gas unit)*   | *Epoch-to-epoch base fee (FIL/gas unit)*    | 



| Statistic | 2022  (nanoFIL/gas unit)      | 2023    (nanoFIL/gas unit)   |
|-----------|-------------|-------------|
| mean      |  0.166      | **0.217**       |
| std       |  0.142      | **0.239**       |
| min       | 100 attoFIL | 100 attoFIL |
| 25%       | **0.014**       | 0.006       |
| 50%       |  **0.164**      | 0.139       |
| 75%       | 0.262       |**0.386**       |
| max       | 3.170        | **4.081**       |


### FIL spent. 

We now follow up on SPs' concern about the amount of FIL spent on their operations. To that end, we investigate (i) the daily amount of FIL spent across all methods and by all miners, (ii) the total daily amount of gas used by some of the most commonly-used methods, and (iii) the amount of FIL spent by these methods. 


#### In aggregate

Given that the amount of FIL spent is a function of the base fee, the figure below will naturally resemble that of the daily average base fee presented above. Once again, we observe there is an increased volatility of FIL spent during 2023, starting from roughly mid-February. However, on average, such spending has stayed around the same order of magnitude as other periods of relatively high network activity, such as the period between mid-July through October 2022.


![](https://hackmd.io/_uploads/BJar39F4n.png)


#### Per method


We now break down the daily gas usage and daily FIL spent per method. 

- There has been a downward trend in the amount of gas used by `PreCommitSector,` `ProveCommitSector,` and `SubmitWindowedPost.` This downward trend likely corresponds to a [decreasing trend](https://dashboard.starboard.ventures/capacity-services#network-storage-capacity) in network Raw-byte Power (RBP). As for the `ProveCommitAggregate` and `PreCommitBatch`, their usage is more common whenever the base fee is large, as expected. Taking  their cyclical nature into account (batching is only reasonable whenever base fee is sufficiently high), there does seem to be some sligh upwards trend in their gas usage.
- There has been, however, a significant increase in the amount of gas used by `PublishStorageDeals.` Since the daily number of `PublishStorageDeals` has remained fairly constant, this increase is likely due to [FIP0045](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0045.md#publish-storage-deals), which discussed an increase in such a method. [FIP0045 was implemented on November 30, 2022.](https://github.com/filecoin-project/core-devs/tree/master/Network%20Upgrades) 
- It is worth mentioning that this increase in the gas units spent by `PublishStorageDeals` was likely not *felt* by the whole network until early 2023 due, at least in part, to the low base fees experienced towards the end of 2022-very early 2023. 
-It is also important to mention that while `PublishStorageDeals` is not the most frequently-sent method, it does account for a substantial part of the gas used daily. Lastly, notice that there has been an increase in the amount of daily `PublishStorageDeals` messages since around November 2022. 


![](https://hackmd.io/_uploads/rkTolZoE3.png)

![](https://hackmd.io/_uploads/Sy05xbsV3.png)





### Checking on Specific SPs.


We now investigate the gas usage trends of two specific SPs. To that end, we perform a similar analysis to one above. As we will see, these two SPs increased FIL spending in the last few months. In general, this increase can be  either:

- *Network-driven*, such as more volatile base fees and increased gas usage for `PublishStorageDeals,` as discussed above, or they can also be 
- *SP-driven*, which reflects changes in a specific SPs consumption due to, e.g., increased data onboarding. 

In what follows, we focus on the specific gas consumption of these two SPs, intending to improve our understanding of these SP-driven factors. 


**SP A**

- There has been a significant increase in FIL spending since March and April 2023, especially if compared to January and February of the same year. 
- While more significant and more volatile base fees are a factor here, it is worth noting that a significant portion of this expenditure is driven by the `PublishStorageDeals` and by the `ProveReplicaUpdates` method, due mostly, to snaps. Indeed, there has been a significant increase in the number of these types of messages being sent by SP A. This, in turn, is reflected by their increasing QAP. 


![](https://hackmd.io/_uploads/S1a0TyiEn.png)



| ![](https://hackmd.io/_uploads/rytiUGsEn.png)| ![](https://hackmd.io/_uploads/BkAPkeiE2.png)| 
| -------- | -------- | 
| *Daily message count, SP A.*    | *Daily QAP, SP A*





**SP B**

SP B has also seen a significant increase in their on-chain expenses during 2023. In their particular case, such an increase seems to be driven by `PublishStorageDeals` as well as the onboarding messages `PreCommitSector` and `ProveCommitSector.` Indeed, notice that despite the current higher base fees, `SubmitWindowedPost` has remained comparable to previous years. 





![](https://hackmd.io/_uploads/rJY6KbjEn.png)
![](https://hackmd.io/_uploads/HJ1AY-s4h.png)

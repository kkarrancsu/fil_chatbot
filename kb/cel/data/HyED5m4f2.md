# Understanding the Recent Base Fee Trends in the Filecoin Network

#### Is the recent upwards trend on base fees caused by FEVM?

---
 ## TL;DR.

**There is no evidence to clim that the recent increase in Filecoin network base fees directly related to the Filecoin Ethereum Virtual Machine (FEVM) gas usage.** Factors such as macroeconomic conditions, increased gas consumption, and potential decrease in blocks produced have likely contributed to the rise in base fees.


## Introduction


In this report, we explore recent trends in the Filecoin network's base fee and discuss possible reasons for the increase in this quantity since mid-February. The Filecoin Ethereum Virtual Machine (FEVM) is not solely (or significantly) responsible for the base fee spike. Instead, other factors have played a role, such as favorable macroeconomic conditions, increased gas consumption,  and network growth. In addition, we also investigate a recent decrease in the number of blocks produced. All data is sourced via Sentinel.

## Key Findings


### Weekly base fee

We plot the distribution of base fees every week below. From that plot, we can observe that the lower tail of the distribution of the base fee became shorter for the two weeks after the FEVM launch. This means the base fee for those two weeks was more concentrated around the 0.1-1 nano FIL/gas unit values. We can also observe, however, that for the last two weeks, such a lower tail has been expanding. Effectively, this means that during the previous two weeks, there was a significant portion of time where the base fee was lower, signaling a potential deceleration (or decline) from the spike. 

Furthermore, notice that the base fee in the weeks of 04/03 and 04/10 concentrated around smaller values than the week before the FEVM launch. In addition, there was a drop in the base fee on the day of FEVM, followed by an increase in this quantity. Such an increase could be due to, e.g., recoveries. 

This data suggests that while there was an increase in base fees after the FEVM launch, the trend driving this increase started about a month before the FEVM launch. Furthermore, given that such an increase in base fee has been decreasing, or at least stabilizing in the last couple of weeks, **it would not be accurate to claim that such a spike in base fee is due to FEVM.**.  



![](https://hackmd.io/_uploads/Bys8hhEGh.png)



### FEVM-Related Gas Usage and Correlation with Base Fee
We now examine the amount of gas used by FEVM-related messages Vs. Base fee, on an epoch-to-epoch basis. For clarity, we say that a message is a *FEVM-related message* if its `family` is either one of {`eam`, `evm`, `ethaccount`, `placeholder`} *or* if its sent from or received by an `F4` address. 

![](https://hackmd.io/_uploads/r1lsc7NMn.png)


While base fee and gas usage (among all messages) are connected via the EIP1559 mechanism, we can see that **there is no apparent correlation between base fee and FEVM gas usage**. This is because the proportion of gas consumed by FEVM-related messages in the average block is relatively small compared to other messages. 

Indeed, in most epochs, FEVM gas usage has remained relatively small, with a few moments as an exception where such gas usage exceeded 2B gas units. It is worth mentioning that the first spike in FEVM gas used likely corresponds to the FEVM launch, where many contracts were deployed.


![](https://hackmd.io/_uploads/HkT-4WvGh.png)



In any case, the daily gas usage by FEVM-related messages has remained quite small since the launch, as evidenced by the figures below.

![](https://hackmd.io/_uploads/ryqEx-wM2.png)

![](https://hackmd.io/_uploads/HJ_rl-wz3.png)






### Gentrification

As a reminder, we refer to *gentrification* as the event where FEVM-related users "outbid" storage providers on their messages. Two possible indicators of this are large `gas_fee_caps` and large `miner tips` associated with FEVM-related messages. We plot the total daily `miner_tip` per method, the average daily `gas_fee_cap`, and the average daily `gas_premium` below.


We can see that, for the most part, the largest source of miner tips is due to `PublishSectorDeals`. Notably, right after FEVM launched, FEVM-related messages dominated the total daily tip amount, however this quantity rapidly decayed. 

![](https://hackmd.io/_uploads/ryNYgZDzn.png)

Looking at the Daily average `gas_premium`, we see that FEVM-related messages include a larger premia per gas. While this *might* suggest gentrification, it is important to remember that (i) at the time of writing, FEVM-releated messages only make up a rather small proportion of all messages, and that (ii) this is a tip per gas unit. Once again, we see that this amount decayed rapidly after launch. 


![](https://hackmd.io/_uploads/BkOwxWwf3.png)


Interestingly enough, the largest gas fee cap has been almost always associated with `SubmitWindowedPost` messages; this is not too surprising since, intuitively, miners are more motivated to submit these messages as soon as they can. It is also notable that FEVM-related messages tend to have some of the smallest `gas_fee_caps`. 

![](https://hackmd.io/_uploads/ryfsl-vM2.png)

Lastly, An interesting feature arises when looking at overestimated units of gas to burn (a portion of the difference between `gas_limit` and `gas_used`) for each method. As we can see, there has been a spike in the overestimated amount of gas used by `ProveCommitSector` that started in mid-February and corresponded to a non-negligible amount compared to the gas used (over 10%). Given that in Filecoin, the base fee is adjusted based on `gas_limit`(due to the deferred execution of messages), this can also contribute to the recent base fee spike. The cause of this increase in overestimation is not, however, apparent.


![](https://hackmd.io/_uploads/BJMhx-Dzh.png)


### Power

The network's Quality Adjusted Power (QAP) has been increasing to the point that QAP is at one of its historical highest at the time of writing. QAP has been growing since mid-February 2023 at roughly 0.016 EiB per day. Notice that this steady increase in QAP coincides with the period of (a) token growth and (b) base fee spike. **Given that onboarding makes up about 25-30% of the gas usage, this is likely a more substantial contributor to the increase in base fee than, say, FEVM messages.**


![](https://hackmd.io/_uploads/rJM2leSz3.png)

We also analyze the *Gini index* for the network power. For the unfamiliar reader, the Gini index is an econometric measure of concentration, typically applied to wealth inequality. The Gini index ranges from 0 to 1. A Gini index of 0 means equal distribution of resources, and a Gini index of 1 means that all resources are held by precisely one agent (i.e., extreme concentration). In this scenario, a Gini index of 0 would imply that all storage power is equally distributed among all miners.
In contrast, a Gini index of 1 would imply that exactly one miner holds all power. We can see that while the Gini index for RBP has stayed mostly stable, such a value for QAP has been slowly decreasing, suggesting that newer miners are joining the network or that some of the smaller miners are onboarding more data. Notice that, in principle, it could also mean that larger SPs are quitting the network. However, this would contradict the fact that QAP has been growing almost steadily.  Alternatively, this decrease could also be casued by miners are splitting their operations into more miner ids, but also seems unlikely. 

![](https://hackmd.io/_uploads/rJCYxeBGn.png)



### Block Production.


Lastly, in light of recent events, we look at the current amount of blocks added to the network. As we can see, while the amount of blocks produced has stayed relatively constant for most of the year, there was a noticeable decrease in the number of blocks produced after April sixth, 2023. While this is not a helpful metric to understand the trends in base fees we have seen since mid-February, reducing the average number of produced blocks to 4 would represent a significant decrease in block space in the network. Indeed, while currently, the network should be able to accommodate an average of 72000 Billion gas units per day (at an average rate of 5 blocks per epoch), this change would reduce that block space by 20%, i.e., 57600 Billion gas units. There are better scenarios than this regarding gas gentrification since it would effectively mean that we have 20% less wiggle room to accommodate the demand for block space the network expects to bring. 

![](https://hackmd.io/_uploads/ryVxsmNGh.png)


### A Finalising Remark: Spike in Base Fee and Increase in Price

Below we plot the mean daily base fee and average token price since January first, 2023. As shown below, the base fee started increasing around mid-February, **coinciding** with a rise in FIL's price. This increase in token price can be attributed mainly to favorable macroeconomic conditions, as stocks and other cryptocurrencies also experienced a rally during this period. While a higher token price might signal growing popularity in the network, it would be shortsighted to attribute the base fee spike to the price increase solely. While there is not enough supporting evidence to claim that token price influences base fee, perhaps a more sensible hypothesis is that the underlying macroeconomic conditions do contribute to these quantities. 


![](https://hackmd.io/_uploads/HJgj9m4fh.png)




### Conclusion

The recent spike in the base fee in the Filecoin network can be traced back to mid-February but does not appear to be directly related to or caused uniquely by the release of the FEVM. Instead, it is likely influenced by macroeconomic conditions, increased overall gas consumption, network growth, and a potential decrease in blocks produced. 
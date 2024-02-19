---
tags: Gas, Research proposals, Almanac
---

# Analysis of FIP-0057
CEL. 

---



### TL;DR
FIP--057 proposes some changes to the gas usage of several methods (c.f. [here](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0057.md)). We analyze whether these adjustments would harm the Filecoin network.

Overall, for the current choice of parameters, **we did not detect any significant economic concerns or risks.** However, As with all FIPs that could have any economic impact, it is worth actively monitoring gas usage after implementation, especially given the broader context of this FIP (namely FVM).

Our findings can be summarized as follows: 
1. **Slight increase in overall gas usage.** We estimated an average increase of up to 3% in gas units.
1. **No significant impact on base fee**. Given that the chain is currently working below capacity (i.e., at about 30% capacity), such a slight increase in gas usage is unlikely to cause any harmful increase (if any) in base fee$^*$. In particular, this additional requirement for gas can easily be absorbed by some of those blocks that are less than 3% below the target block size without any issue. 
2. **Slight increase in tokens burn.** The additional gas usage will, in turn, increase the number of tickets burnt, on average.
3. **FVM considerations**. It is worth mentioning that while the increase in overall gas usage is estimated to be small, this increase can "take away" some space that could have otherwise been devoted to FVM. 

$^*$ *Given that the base fee is adjusted on epoch-to-epoch bases, a more precise statement would be among the lines of "We do not expect  such a small increase in demand to significantly affect the statistical properties of the base fee."*


### Introduction

With the introduction of user-programmable smart contracts, we need to ensure that the gas model accurately reflects the cost of on-chain computation. Currently, users can only trigger course-grained behaviors by submitting messages to built-in actors. However, once the FEVM is deployed, users will be able to deploy new smart contracts with fine-grained control over FVM execution. FIP--057 proposes a few adjustments to the gas charging schedule based on code optimization, gas accounting, and cost repricing of the computational cost of some syscalls (like writing and reading from storage, hashing) in order to bring them in line with their real compute cost. 

**Goal.** The goal of this analysis is then to understand whether the proposed gas adjustments (c.f.Appendix 1) would have a negative impact on the health of the network.

## Methodology.



We focus our analysis on understanding the following hypothetical scenario: 

*"what the gas usage be if the same messages that were included on-chain on a given collection of blocks were included with the proposed adjusted gas fees?"*

To answer that question, we collected on-chain data for over one million messages that were included on the chain between epochs 2520000 and 2525770. Each of these data points had the following entries associated with it

- `height`: the height at which the message was sent, 
- `gas_limit`: the gas limit of the message,
-  `method`: the method the message invoked (c.f. reference table).
-   `count`: the number of messages in the tipset
-   `base fee`: the base fee at that epoch (with no adjustment).

These data points were obtained from the following Sentinel tables `messages`, `message_gas_economy`, `actors`, `block_headers`. 

From these values, together with the proposed adjustments in the Appendix, we can estimate what we `gas_used` would have been at every epoch, using `gas_limit` as a proxy (i.e., an upper limit) for the gas used. Naturally, this approximation provides an upper bound on the usage. Given this data, we proceed as follows. 

1. For each message $m$, compute the `adjusted_gas_limit` by multiplying the `gas_limit` of that message by its corresponding adjustment factor according to the Table. Notice that, due to technical and time constraints, we used `gas_limit` as opposed to `gas_used,` which results in an upper bound on our estimates.

2. Group messages by epoch. For each epoch, add the `adjusted_gas_limit` of all the messages in that epoch. This number then gets divided by the total number of blocks on that epoch, yielding an estimate of the total gas usage per epoch. 

Remark: The values for adjusted gas limit were restricted to the interval $[0,10^{10}]$ gas units in order to account for block-size restrictions. 


## Results 



**Average change in usage.** Averaging over all epochs in the procedure above yields the following results: 

| Statistic 	| Current gas units (Billions)        	| Adjusted gas usage  	   Gas units (Billions)       	|
|------	|--------	|--------	|
| mean 	| 5.052  	| 5.207  	|
| std  	| 2.066  	|2.173  	|
| min  	| 0.000  	|0.000  	|
| 25%  	| 3.542  	| 3.619  	|
| 50%  	| 4.766  	| 4.904  	|
| 75%  	| 6.215  	| 6.422  	|
| max  	| 10.000 	| 10.000 	|

This represents, on average, **an increase of roughly 3% in gas consumption**. 



![](https://hackmd.io/_uploads/rks0ax7ao.png)


**Impact on base fee.**

We begin by estimating the current network utilization.

**Daily used.** Notice that currently, there are about $U=4.5\times 10^{13}$ gas units used, at any given day.

![](https://hackmd.io/_uploads/Bk9hBLmpo.png)


**Daily availability**. Each block has a maximum block space of $10^{10}$ gas units. On any given day there are, on average $N_s=14400$ different blocks: 

$$N_\text{blocks}=\underbrace{2880}_{\text{epochs in a day}}\times \underbrace{5}_\text{avg. No of blocks per epoch}=14400.$$

Thus, the average daily available block space is then $$A=10^{10}\times N_\text{blocks}= 1.44\times 10^{14}.$$

Taking the ratio between $U$ and $A$ then implies that the network is running at roughly 32% capacity. In particular, this means that the network could, in theory, accommodate an additional 18% of capacity (on average) without surprising the target block utilization. Thus, **we do not expect this FIP to cause any significant congestion** (due to block space). In particular, **we do not expect that such a small increase in gas usage would cause any harmful change (if any at all) in the statistical properties of the base fee**. By these we mean drift, volatility, etc. 

**Remark**
It is worth mentioning, though, that while the increase in overall gas usage is estimated to be small, this increase can "take away" some space that could have otherwise been devoted to FVM. 


**Additional revenue.** Lastly, it is worth remarking that increasing the amount of gas used would increase the number of tokens burnt. *Ceterus paribus,* under FIP--0057 the network would burn 3% more tokens. This additional amount of tokens burnt is in no way sufficient to close the inflation gap (due to minting too much in comparison to what is being locked and burnt) so this FIP is not expected to significantly alleviate (or worsen) current token inflation.


## Conclusions.
In this short report, we presented a methodology to estimate the average gas consumption under the adjustments proposed in FIP--0057. Such a FIP proposes several code optimizations as well as technical changes that ultimately affect how gas is accounted for. While gas accounting and usage would, in general, pose economic risks or blockers, 
**we did not detect any major economic concerns or risks** associated with this FIP with its current choice of parameters.

As with all FIPs that could have any economic impact, however, we believe it is worth it actively monitor gas usage after implementation, especially given the wider context of this FIP (namely FVM).

**A finalizing remark.**
*Potential economic issues should not hinder progress. This document presented an analysis of the possible economic impacts of the changes proposed by FIP-0057. These changes are about more accurately accounting for gas usage, which, in our opinion, is a pure engineering task; indeed, we believe it is in the network's best interest to have the most accurate accounting of gas we can estimate. If optimizing a network parameter would bring undesirable economic consequences, then the underlying economic mechanism would need to be revised. This should not, however, be a blocker for network improvement on the engineering side.*
## Appendix.


### Appendix 1. Proposed changes
**Remark:** *This table was taken from [here](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0057.md), and presented in this document for convenience. Please refer to the original document for the most up-to-date data.*

| Code | Method | Event Count | Existing gas usage | Gas usage with FIP-0057 | % Change |
| --- | --- | --- | --- | --- | --- |
| fil/9/account | 0 | 1223 | 291660.72 | 645124.08 | 121.18 |
| fil/9/multisig | 2 | 40 | 5938757.07 | 8710765.85 | 46.67 |
| fil/9/multisig | 3 | 2 | 24906502.50 | 29119872.00 | 16.91 |
| fil/9/reward | 2 | 5547 | 40317641.00 | 43873338.19 | 8.81 |
| fil/9/storagemarket | 2 | 1650 | 24982007.47 | 23173395.18 | -7.23 |
| fil/9/storagemarket | 4 | 11953 | 606009920.31 | 541451416.73 | -10.65 |
| fil/9/storageminer | 0 | 7 | 216405.00 | 481000.00 | 122.26 |
| fil/9/storageminer | 3 | 1 | 3146882.00 | 6040850.00 | 91.96 |
| fil/9/storageminer | 4 | 10 | 2601772.10 | 4474645.00 | 71.98 |
| fil/9/storageminer | 5 | 46986 | 52907581.11 | 49981422.43 | -5.53 |
| fil/9/storageminer | 6 | 49513 | 46352972.94 | 48949895.13 | 5.60 |
| fil/9/storageminer | 7 | 55086 | 63102326.38 | 75481067.70 | 19.61 |
| fil/9/storageminer | 8 | 646 | 523704602.86 | 514605025.93 | -1.73 |
| fil/9/storageminer | 11 | 406 | 429599995.23 | 232335284.18 | -45.91 |
| fil/9/storageminer | 16 | 140 | 27477805.81 | 32683070.28 | 18.94 |
| fil/9/storageminer | 18 | 5 | 2571314.40 | 4440263.80 | 72.68 |
| fil/9/storageminer | 23 | 6 | 2593594.83 | 4469491.16 | 72.32 |
| fil/9/storageminer | 24 | 1 | 4096410066.00 | 2142130910.00 | -47.70 |
| fil/9/storageminer | 25 | 1517 | 260234684.68 | 278624611.67 | 7.06 |
| fil/9/storageminer | 26 | 510 | 2255779780.47 | 2582969572.70 | 14.50 |
| fil/9/storageminer | 27 | 967 | 270460447.84 | 318397920.82 | 17.72 |









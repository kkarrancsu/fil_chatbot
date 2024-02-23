---
title: CEL Analysis of FIP-32
tags: FIPs
---

# CEL Analysis of FIP-32

## Introduction

[FIP-24](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0024.md) adjusted the *BatchBalancer* and *BatchDiscount* paramaters to match observed network growth post-HyperDrive and presented the following "Crossover Base-Fee" - the point at which a miner is indifferent between choosing to submit proofs via *SingleProofProveCommit* or *BatchProveCommit*. 

$$ CrossoverNetworkBaseFee = \frac{BatchBalancer \cdot BatchDiscount \cdot SingleProofGasUsage}{SingleProofGasUsage - \frac{BatchProveCommitGasUsage}{NumProofsBatched}}$$

The network parameter values of *BatchBalancer* and *BatchDiscount* currently sit at $5$ nanoFIL and $\frac{1}{20}$ respectively. These parameters are set considering storage onboarding expectations, equilibrium network $BaseFee$, storage provider ROI, cost of *PublishStorageDeals*, and protocol revenue. This applies to both `PreCommitBatch` and `ProveCommitAggregate` messages. 

## FIP-32 

### Summary

FIP-32 introduces changes that adjust the gas accounting model of the Filecoin Blockchain in preparation for User Programmability (UP). These changes are expected to cause a global increase of 1.95x in gas utilization (assuming current chain activity remains unchanged). As a result of this potential change in gas dynamics, CEL is investigating the current Balancer parameters in the event they may need to be adjusted to align with network expectations following FIP-32's rollout.

### EDA on Gas Multipliers

FIP-32 is expected to create a global increase in gas usage, but per the below figure, there is dispersion in this increase across methods. (See [FIP-32](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0032.md) Annex A for greater detail). 
![](https://i.imgur.com/oJGb0Lq.png)

We expect the gasUsage increase for `PreCommitSector` and `PreCommitBatch` method calls to be significantly greater than the increase in gasUsage for `ProveCommitSector` and `ProveCommitAggregate`. This change in gasUsuage affects the relationship between the $CrossoverNetworkBaseFee$ and $NumProofsBatched$, and, therefore, the breakeven curve for which miners should be indifferent between submitting $n$ single proofs or batching $n$ proofs at a given *BaseFee*.   

To account for the uncertainty surrounding gas increase associated with a given proving opersation, we calculate the breakeven curves over sampled FVM gas increase multipliers (with current network *BatchBalancer* and *BatchDiscount* parameters) and compare this to the current network breakeven curve

![](https://i.imgur.com/gU7WUmG.png)

The takeaway is that **given current network conditions** miners will likely have to **aggregate more proofs at any given network *BaseFee* in order for batching to be preferable to submitting single proofs**. 

### Batch Balancer Parameter Analysis

We expect FIP-32 to result in upwards pressure on the *BaseFee* due to
- higher chain bandwith utilization 
- message executions surpassing the base fee target. 

#### Base Fee Derivation 
We derive network *BaseFee* utilizing the following principle: 

$$ UnitAnnual32GiBSectorReward_{t+1} = DerivedNetworkBaseFee * \\(PreCommitSectorGasUsage_{t} + ProveCommitSectorGasUsage_{t})$$ 

That is, one year's worth of mining rewards for a single 32 GiB sector this time next year should be a fair value for network revenue to commit a sector (given by *currentBaseFee* * *SectorGasUsage*). 

Therefore assuming a network *DailyPowerGrowth* of 50 PiB and current chain state **we estimate a *FairNetworkBaseFee* of 0.65 nanoFil**

#### Breakeven Proof Aggregation 
Now we find the equilibrium number of proofs that correspond to *BaseFee* = 0.65 nanoFIL in the post FIP-32 world. Drawing from our sampled FVM gas increase multipliers we show the distribution of break-even proofs below: 
![](https://i.imgur.com/5c8S1d9.png)

The break-even number of proofs to aggregate at our derived network *BaseFee is $\approx 5.3$ proofs.

#### Estimating the fair *BatchBalancer*

We estimate the fair batch balancer (derivedBalancer) utilizing the following principle:

$$ B_\text{derived}  G_\text{todayProveCommitGasUsage} = \beta d \cdot (G_\text{todayProveCommitSectorGasUsage} + \\G_\text{todayPreCommitSectorGasUsage}) + B_\text{derived} \frac{gasBatchUsage[N_\text{derivedProofs}]}{N_\text{derivedProofs}} $$

where $\beta$ is the derivedBalancer, $d$ is the batch discount $B_\text{derived}$ is the *derivedNetworkBaseFee* (*FairNetworkBaseFee*) above. 

The idea is that network revenue at the *derivedBaseFee* should be equivalent to network fee estiamted using the batch balancer. 

Note that: 
- $N_\text{derivedProofs}$ is the breakeven number of proofs that corresponds to the derivedNetworkBaseFee at the batching crossover level. 
- $gasBatchUsage[N_\text{derivedProofs}]$ is a linear function that maps the number of proofs to batchGasUsage 

We can rearrange to arrive at an equation for the derivedBalancer $\beta$

$$ \beta = \frac{B_\text{derived} G_\text{todayProveCommitGasUsage} - B_\text{derived}  \frac{gasBatchUsage[N_\text{derivedProofs}]}{N_\text{derivedProofs}}}{d\cdot (G_\text{todayProveCommitSectorGasUsage} + G_\text{todayPreCommitSectorGasUsage}) } $$


So, from our distribution of equilibrium proofs above, we arrive at a distribution of derivedBatchBalancers shown below: 
![](https://i.imgur.com/RlTHrfG.png)

**with a median $\beta = 6.07$**

The interpretation is, given our expectation for changing gas dynamics, the fair batch balancer parameter lies at about 6.07. 

$$ \\ \\ \\ $$

// TODO: Change to working link
*NoteBook [here](http://localhost:8888/notebooks/CEL_notes/notebooks/FIP-0032/FIP-0032-backtest-cel-v1.1.ipynb) - If curious to look at the analysis in greater detail 


 






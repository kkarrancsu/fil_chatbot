# Report on self preserving SP's
# Introduction

We have previously discussed the potential scenario of "gas gentrification" related to the introduction of FVM. In this scenario demand for gas usage from FVM could become so high that it would hurt essential SP storage operations. 

In principle, SP's as a collective are in control of base fees, given that they can decide how many messages to include on chain. SP's could collude to include fewer messages in the blocks, lowering the base fee, and their operational costs. 

A group of SP's that intentionally excludes general FVM messages, in order to lower base fees is what we call here **self-preserving SP's**.

Here we present a brief report on the possibility of SP's organizing themselves in a self preservation effort, and discuss agent-based simulation results on the viability of this SP approach to lower their own operational costs.

The main difficulty in SP's organizing a self-preserving strategy is that the effort can be "ruined" by a small group of non-collaborating SP's who would rather take in short term gains in the form of excess miner tips. 

## EIP-1559 stability

Here we discuss general stability properties of the EIP-1559 base fee mechanism that are equally applicable to Filecoin or Ethereum. From the next section onward we discuss Filecoin-specific questions.

Gas fees on Filecoin are determined by the EIP-1559 mechanism. Gas fee are composed of a base fee component, which is burnt, and a miner tip. The base fee, $r_t$ at time (epoch) $t$ is given by,
$$ r_t=\left(1+\frac{1}{8}\frac{G_{t-1}-G^T}{G^T}\right)r_{t-1},$$
where $r_{t-1}$ is the previous value of base fee, $G^T$ is the target block size parameter (in units of gas), and $G_{t-1}$ is the amount of gas consumed in the previous block. The base fee adjusts itself according to demand for gas usage, relative to the target block size, where if the block size is larger than the target, the base is increased, and if the block size is smaller than the target, the base fee is decreased.

Given that the base fee portion of transaction fees is burnt, **there could exist an incentive for collusion amongst miners to lower the base fee, by restricting the amount of messages they pack into blocks, to be below the target block size**. This would increase the competition levels of users to get their messages into the block, reverting partially to a first price auction mechanism, where miner tips would become a larger portion of the total transaction fee.

EIP-1559 has an inherent stability preserving mechanism: if a small group of miners tries to manipulate the base fee by restricting the number of messages they accept on chain, this results in higher potential miner tips for the next miner that gets to write a block, who would then be incentiviced to overpack the block, to earn higher miner tips. 

## Filecoin's built in base fee manipulation incentive

The main difference in Filecoin gas dynamics is that SP's are required to consume large amounts of gas, in the form of sector proofs, particularly for onboarding new sectors.

Lower base fees means lower operational costs for Filecoin SP's, and higher profitability. This works as an incentive for SP's to try to lower base fees, something that is in principle possible, if enough SP's collude and underpack blocks.

We will next explore an agent-based simulation of SP behavior, which allows us to explore questions such as, how much collusion is required to effectively lower the base fee? How comitted do all SP's need to be to the cause of lowering base fees, before the incentive to take in additional miner tips ruins the strategy?



## Agent based modeling of SP self-preservation

We created a simple agent-based model to test the levels of collusion required to effectively carry out the "self-preservation" strategy.

The full details of the simulation can be found on [this notebook](https://github.com/protocol/CryptoEconLab/blob/main/notebooks/Self%20preserving%20SP's%20simulation.ipynb), as well as instructions of how the user could change parameters, levels of demand for gas, and SP strategy profiles to test different scenarios.

There are several assumptions made in this model, including (but not limited to):
* We have to assume distributions for how much SP's and general FVM users are willing to pay for gas usage, which will guide how transaction fees rise as a function of demand.
* We model the self-preservation behavior by assuming that every SP has a "temptation theshold". When an SP has to write a block, they are willing to underpack the block, by including only SP storage-related messaages, unless the profit they can make in the form of miner tips from including general FVM messages exceeds their temptation threshold. We draw the temptation threshold for each SP from some statistical distribution, that can be modified, to model different levels of collusion. 

By modifying the distribution for the temptation threshold, we can get an idea of what levels of collusion are needed for SP's to effectively stop gas gentrification.

The output of the simulation is a graph of base fee over time, given different levels of demand for gas (from SP's and from general FVM usage) and given some temptation threshold distribution. If SP self-preservation is successful (high collusion), we see that base fee stabilizes to a fair price for the level of SP demand. If SP self-preservation is not successful (low levels of collusion), SP's are not able to lower the base fee. There are intermediate levels of collusion, which show different levels of fluctuations between high and low base fees.

We present some results in the next section, using some particular demand scenarios and SP strategy profiles.

## Current gas demand trends and breaking points

## Are gas lanes needed?

Gas lanes, as proposed in [this FIP discussion](https://github.com/filecoin-project/FIPs/discussions/679) are a mechanism for the network to explicitly intervene and protect SP's against gas gentrification. If SP's were able to successfully collude to protect themselves from gentrification, gas lanes would be redundant.


[At this point](https://observablehq.com/@starboard/chart-daily-gas-usage) (as of May 2023), gas usage from SP messages are still the majority of gas used in Filecoin. There is yet no significant statistical evidence that gas gentrification has occured in Filecoin. This, however, doesn't mean this will always be the case, as it depends on the demand for gas usage that FVM ends up attracting over time.  

One important argument for the use of Gas lanes is that **the SP self-preservation strategy requires inefficient use of blocks**. For SP's to be able to self-preserve, they need to consistently underpack blocks, wasting potential capacity of the Filecoin block. Having gas lanes would mean that SP's are able to have reasonable base fees, while still optimally filling blocks.










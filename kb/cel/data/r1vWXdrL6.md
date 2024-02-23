---
title: Cryptoeconomic impacts of Direct Data Onboarding
tags: Econ monitor
---

**Authors**: CryptoEconLab

## Summary
* [FIP-0076](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0076.md) (Direct Data Onboarding/DDO) introduces technical upgrades to the Filecoin network that offer alternative messaging pathways for onboarding deal power that reduce gas. 
* In this note, we assess the cryptoeconomic impacts of DDO, namely the supply statistics. Since DDO frees block space, we identify three relevant cases:
    * Case 1 - There is no increase in onboarding or chain activity to fill emptied block space.
    * Case 2 - There is an increase in onboarding, but not enough to fill block space to the target of 5B gas units.
    * Case 3 - There is an increase in onboarding and chain activity to fill block space to the target.
* **Findings**:
    * Gas burn from $\mathtt{basefee}$ is a small percentage of the $\mathtt{net_outflow}$ of circulating supply. This implies that DDO has a small impact on overall circulating supply (CS) and Locked/CS.
    * However, because burned tokens exit the supply permanently while locked tokens exit temporarily, burning provides permanent protocol revenue and thus remains an essential aspect of the network’s cryptoeconomic health.
    * Increasing onboarding rates will decrease CS and increase L/CS, even if no protocol revenue is generated from burning $\mathtt{basefee}$. This is because the outflow due to locking pledge is significantly higher than the outflow due to burn of PSD messages, when onboarding deal power.
    * DDO frees up block space, enabling a higher throughput for onboarding power onto the network. With current estimates of gas savings and onboarding rates, the chain will be able to support ~300 PiB/day of deal power. This would require ~350M FIL of investment into the network.

## Introduction
In this note, we examine the cryptoeconomic effects of Direct Data Onboarding (DDO) on the supply statistics of Filecoin. Direct Data Onboarding is a FIP that introduces technical upgrades which enable a cheaper pathway to onboard deal power onto the Filecoin network. Many expenses are associated with onboarding FIL+ data, but DDO addresses gas-related expenses.

### Gas & Base-Fee Background

Gas is a measure of the computational resources that a message will impose on the blockchain.  Therefore, different messages require different amounts of gas. The Gas Fee (or transaction fee) used to charge for those computational resources contains two components, the amount of Gas used to submit a message (in units of Gas) and the $\mathtt{basefee}$ (fee per unit of gas). Since transactions are settled in units of FIL, the cost of submitting a particular message at epoch=t is given by:

$$ \mathtt{cost} = (\mathtt{basefee_t} + \mathtt{minertip}) * \mathtt{gasrequired_t} $$

$\mathtt{gasrequired_t}$ depends both on the type of message being sent as well as when the message is sent to be included in the blockchain.  $\mathtt{basefee_t}$ is a time-varying value in units of (FIL/gas) that sets an economic cost for submitting messages to the blockchain. In Filecoin, this cost amount of tokens is burned, indirectly compensating blockchain validators and token holders due to a permanent reduction in supply. This is denoted as the $\mathtt{basefee}$ component of protocol revenue; the other components of protocol revenue are from penalties, estimation fees, and fees for batching messages. 

$\mathtt{basefee_t}$ varies according to the following relation:

$$ b[i+1] = b[i] \left( 1 + \frac{s[i] - s^*}{8 s^*} \right)$$
where $s^*$ is the target block size (5B Gas units in Filecoin), and $s[i]$ is the block size at epoch=i, b[i] is the $\mathtt{basefee}$ at epoch=i and b[i+1] is the next epoch’s $\mathtt{basefee}$. $\mathtt{basefee}$ increases from its previous value if the block size at the previous epoch exceeds the target block size, and vice-versa. If block space usage is consistently below the target block space, then $\mathtt{basefee}$ goes to it's minimal value. Similarly, as $\mathtt{basefee}$ starts to increase, the cost to submit messages to the blockchain increases and becomes increasingly uneconomical, incentivizing users to wait to submit new messages until the $\mathtt{basefee}$ is reduced.

### DDO Relevance to Gas

To onboard deal-power onto Filecoin, two specific messages need to be submitted to the network, the PSD message and the ProveCommit message. DDO reduces the amount of gas needed when onboarding a deal sector by offering an alternative messaging pathway to PSD and reducing the gas needed for ProveCommit messages. 

The reduction in gas usage changes the $\mathtt{basefee_t}$ trajectory which then results in a change to the protocol revenue.  There are three relevant cases to consider:
* Case 1 - There is no increase in onboarding or chain activity to fill emptied block space.
* Case 2 - There is an increase in onboarding, but not enough of an increase to fill up excess block space.
* Case 3 - There is an increase in onboarding and chain activity to fill up block space to the target of 5B gas units.

The case where block space exceeds the target is irrelevant because the economic disincentive for miners to exceed the target block space is strong and grows stronger the longer this behavior is sustained. This is a result of the $\mathtt{basefee_t}$ update given in Eq. 2.

We now consider what happens to the supply characteristics in each case outlined.

## Case 1 - No change in onboarding & no increase in chain activity due to other sources

Case 1 simulates the belief that current macroeconomic forces (high interest rates, etc.) are the primary driver for onboarding and renewals in Filecoin. This belief translates to no increased onboarding of deal power onto Filecoin because the most significant cost for onboarding power is the initial pledge. The lack of additional onboarding, combined with the gas reduction of the PSD and ProveCommit messages results in overall reduced gas usage. 

From Eq. 2, this will result in $\mathtt{basefee}$ remaining near zero because the increase in available chain capacity is not utilised with increased onboarding or chain activity.

To simulate Case 1’s impact on the circulating supply, we first estimate the change in the cumulative amount of gas burned over the simulation window if $\mathtt{basefee}$ is zero. In this case, protocol revenue comes from $\mathtt{penalty}$, $\mathtt{batchfee}$, and $\mathtt{overestimationfee}$ and excludes $\mathtt{basefee}$. 

The simulation framework, mechaFIL, simulates gas burned by taking the mean of daily burn over a historical window and linearly extending that to forecast the future. Following this approach, we compute over the same window the percentage of gas burn attributed to base_fee.  The median value is 54%, meaning that 46% of gas burn is attributed to the other sources previously mentioned.

Using this forecasted burn and extending onboarding, renewals, and FIL+ rate at current levels, we can compute the difference in supply statistics between the case where DDO is implemented and where it is not.  Fig. 1 shows the relevant supply metrics.

![case1](https://hackmd.io/_uploads/HJfEA9SIT.png)

*Fig 1: The difference in circulating supply and L/CS trajectories with DDO.*

We observe that there are minimal changes to the supply statistics.  That is because burn is a small percentage of $\mathtt{net_outflow}$. Outflow from the circulating supply has two components:

$$ \mathtt{net_outflow = locking + burning} $$

Fig. 2 shows various perspectives of gas burn on supply statistics. Fig 2A shows the percentage of FIL burned as a percentage of the total circulating supply. Fig 2B shows the percentage of daily outflow attributed to burn, while 2C shows the daily outflow attributed only to the base_fee component of burn. 

![attrib_basefee_burn](https://hackmd.io/_uploads/SyR0f5SUT.png)

*Fig 2: A) Daily burn as a function of total circulating supply  B) Daily outflow attributed to protocol burn over the past 6 months  C) Daily outflow attributed to $\mathtt{basefee}$ burn over the past 6 months.*

We observe that the mean values of daily outflow attributed to burn and $\mathtt{basefee}$ burn are small compared to the outflow attributed to locking. However, an important point to note is that while burn is a smaller component, it has a different effect on the network. Burn permanently removes tokens from the circulating supply, while the effect of locking is temporary.

We can model the impact of locking and burn on circulating supply by applying a discount factor to locking. The discount factor expresses the idea that removing items from the circulating supply is more beneficial now than in the future; akin to the time value of money, where money is more valuable in the present than the future. We leave it to future research to select appropriate discount factors that align with network goals.

## Case 2 - Increased onboarding, but not enough to fill emptied block space.

We now analyze Case 2 - the scenario where block space is not filled to the target, even though onboarding increases.  

To show the effect of this on supply, let us define the base case to be the same level of onboarding as before DDO was implemented.  Then, define the FIL conserved case as the onboarding level increased by the percentage of gas-cost savings afforded by DDO.  Using SP cost information, we find that on average, the percentage of costs attributable to gas for onboarding sectors is 0.026% (Fig 3) of the total onboarding costs across a range of exchange rates considered under assumptions detailed [here](https://hackmd.io/gzftJx5eQDKhv4-UEubSgg?view=#When-Filecoin-Plus-works-and-when-it-doesn%E2%80%99t).


![gas_cost_pct](https://hackmd.io/_uploads/r1G-m9SIa.png)

*Fig 3: Gas cost percentage of total cost needed to onboard a sector, swept across multiple FIL exchange rates*

We then compute multipliers of increased onboarding amounts from that level to see how those situations affect network supply statistics. We keep the gas burn due to $\mathtt{basefee}$ zero, as in Case 1 - this is a consequence of the assumptions of Case 2. Fig 4 shows the effect on supply for the FIL conserved case defined, 1.1x, and 1.2x the FIL conserved case.  The increased rates are in units of RBP; at the current FIL+ rate of ~92%, this translates to a 9.2x increase in deal onboarding rate.

![case2](https://hackmd.io/_uploads/BJn-75B86.png)

*Fig 4: Changes to the supply statistics in Case 2. Even though $\mathtt{basefee}$ is 0 in Case 2, increases in onboarding result in noticeable changes to circulating supply, locked, and L/CS.*

The changes in supply are significant because:
1. The change in RBP is maginified for deal power due to the 10x QA multiplier
2. As onboarding is scaled up, circulating supply decreases while network locked increases.  These are compounding effects that result in a large change to the L/CS trajectory.

In the FIL conserved regime, the small increase in onboarding that results from decreased gas costs does not result in any meaningful changes to the supply statistics (blue line) from the status-quo. This makes sense because gas costs are a small percentage of the total cost for onboarding sectors.


## Case 3 - Increased onboarding and chain activity for gas to reach target block space.

We now analyze Case 3 - the scenario where block space is filled to the capacity through increased onboarding and other chain activities. 

We use the same simulation methodology as above, but implement gas burn due to $\mathtt{basefee}$, and scale RBP onboarding as before. Fig 5 shows the changes from status quo for the supply statistics when the same scaling is considered. The trends are almost identical to Case 2, where there is no gas burn due to $\mathtt{basefee}$. From a supply perspective, this makes sense b/c burn due to $\mathtt{basefee}$ is a small percentage of circulating supply.

![case3a](https://hackmd.io/_uploads/HJ1Xm9HUp.png)

*Fig 5: Changes to the supply statistics in Case 3.*

## Monetary Considerations of DDO
In this section, we estimate the additional investment needed to fully utilize the chain through power onboarding. More precisely, we aim to answer the question: what does the power onboarding rate need to be, such that the same amount of gas is used for onboarding as it was previously?

We examine the PSD case in isolation since it is the most significant contributor to gas usage when onboarding deal sectors. To do so, we build a Generalized Linear Model (GLM) that forecasts the amount of PSD gas used based on the amount of onboarded deal power.  This should be a strong relationship because mechanistically, onboarding power causes PSD messages to be generated. The model is trained using historical data from the network. Fig 6 shows the trained model’s fit to the historical data. 


![glm_case2_historical](https://hackmd.io/_uploads/Sk3Q75rUp.png)

*Fig 6: GLM trained on historical paired data of onboarded deal power to PSD gas used.  The blue dots are historical data, and the dotted red line represents the GLM forecast.*

Next, we use estimates from the DDO engineering team that DDO will reduce gas usage by 85% if the new pathway for onboarding is used, rather than the PSD pathway.  To model this, we scale the GLM model In Fig 6 by 85%. More precisely, if gas usage for PSD is reduced by 85%, then power will need to scale up by 85% to match the same gas usage as before.  The DDO model compared to the status quo is shown in Fig 7.

![glm_case2_extrapolate](https://hackmd.io/_uploads/HJ6N7qHIp.png)

*Fig 7: Hypothetical model for forecasting the gas used when onboarding deal power with DDO implemented.*

Current onboarding levels are roughly 4.76 PiB RBP/day at 92.6% FIL+ Rate, which translates to 44 PiB/day of deal power being onboarded. If DDO reduces gas usage by 85%, this increases the capacity of the chain to onboard upto ~293 PiB/day of deal power (under the linear scaling assumption).

Next, we compute the necessary investment to flow into the Filecoin network to support the increased QA power. We simulate this via MechaFIL, which takes into account the fact that pledge decreases as network QAP increases (below):

$$ ConsensusPledge = 0.3 \times CS \times \frac{SectorQA}{max\{b(t), NetworkQA\}}$$

The simulation results are shown below in Fig 8 - they indicate that even though the pledge per sector decreases as onboarding increases, the overall investment increases.  

![onboarding_vs_investment](https://hackmd.io/_uploads/SyFL7cBLT.png)


*Fig 8: Dynamics of pledge per sector and total investment needed to onboard various multipliers of the current onboarding rate (in black).  The figure shows that while pledge per sector decreases as the onboarding rate increases, the total investment is still greater.*

A related perspective is to compute the total investment needed to increase onboarding over the simulation timeframe as a function of increasing the onboarding rate, normalized to the status quo level. Fig 9 shows this perspective and indicates that the additional investment needed for the pledge to increase onboarding is significant, even though the growth rate is sublinear. 


![onboarding_vs_investment_cumulative](https://hackmd.io/_uploads/S1ND7cSLp.png)

*Fig 9: Total investment needed to onboard greater amounts of RBP than status quo.*

## Conclusion
The cryptoeconomic impacts of DDO have been explored in this report. We find that it is unlikely to have a significant impact on supply. This is due primarily to the fact that gas_burn is a minor contributor to overall $\mathtt{net_outflow}$. The reduced gas burn has two potentially negative consequences:

* Reduced cost to spam the blockchain with irrelevant messages
* Reducing the permanent outflow effect of burn 


Finally, while the cryptoeconomic impacts are reduced, the technical upgrades enable more data onboarding throughput, and consquently enable more investment to flow into the network. While the amount of investment needed is large, the technical upgrade enables it to be possible.

## References
1. [MechaFIL](https://github.com/protocol/filecoin-mecha-twin)
2. [Simulation Notebooks](https://github.com/protocol/CryptoEconLab/tree/mechafil-jax-notebooks/notebooks/mechafil_jax/direct_filp_v2)

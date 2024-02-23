---
title: Thing 1 and Thing 2 A Macroeconomic Summary of Network Shortfall
tags: Econ monitor
---

# Thing 1 and Thing 2: A Macroeconomic Summary of Network Shortfall
{Kiran, Tom, Vik}

![](https://hackmd.io/_uploads/ryHTiNzSh.png)
## Introduction
The introductory FIP discussion post raised by Alex North isolated two problems that currently face the Filecoin network and economy: 
1. The difficulty of Storage Providers (SPs) to source the collateral required for committing storage deals and capacity 
2. The growth rate of Filecoin’s circulating supply, as inflows outstrip outflows which may add some uncertainty to SP returns 

The CryptoNet and CryptoEconLab teams at PL have continued to explore the design space in FIP discussion post [#666](https://github.com/filecoin-project/FIPs/discussions/666) - “Storage & Data On-boarding With Reduced Pledge Collateral (“Pledge Shortfall”). While further design and analysis is ongoing, there are two versions of a “pledge shortfall” policy (known as "Thing 1" and "Thing 2" that are concrete enough for wider public feedback. The following document provides a summary of both proposals, as well as a discussion of some key cryptoeconomic considerations and tradeoffs between the two shortfall proposal variants. CEL will continue to provide supporting analysis as public community discussion relevant to shortfall policy progresses.

### Policy Summary
Both policies look to have the following properties: 
1. Enable SPs to onboard or extend power with less pledge than the full initial pledge required, subject to the constraint that an SP will be required to put up atleast $2/3$ of a sector’s pledge. Said differently, an SP can choose to pledge up to $1/3$ less than the sector's initial pledge; we define   this amount to be the shortfall.
2. Regardless of shortfall taken, all sectors will have the same full QAP an will earn rewards commensurate with sector power 
3. A fraction of rewards earned and/or vested will be taken to either lock as pledge or burn as a fee; this fraction reduces as the shortfall is closed. 

The result is an SP can onboard more power for a given amount of pledge tokens. This could raise FIL-on-FIL returns, however, the mechanisms are designed such that if an SP is not pledge constrained, they would prefer to commit sectors with the full initial pledge amount (i.e. take no shortfall).

A successful outcome for either policy would be their ability to: 
1. Induce a greater rate of deal and capacity onboarding than current levels (~5-6 PiB/Day)
2. A similar or increased rate of tokens locked relative to the current trajectory
3. Reduced inflows to circulating supply due to reward locking and fees paid

Given that it is possible to achieve the stated goals above in a multitude of ways. CNL and CEL have provided the following specs of two variants of a potential network shortfall policy: (Known as Thing 1 and Thing 2).

### Impact on Storage Onboarding Potential 

A potential benefit of a shortfall policy is to reduce onboarding frictions for Storage Provider's who are collateral constrained. A simple model for quantifying the impact of a network shortfall policy is estimated as: 

$$ 
\begin{align*}
DealOnboarding &= NoShortfallDealOnboarding * \\ &(1 + ShortfallEffectiveness * NetworkShortfall) 
\end{align*}
$$

Here, the amount of storage onboarding in a post shortfall policy regime is the amount of onboarding that would have occurred without shortfall availability, scaled by the "effectiveness" of the shortfall policy and the maximum amount of shortfall able to be taken. The effectiveness of the shortfall policy — in terms of increasing onboarding — depends on the hypothesis that there is substantial unmet demand for storage onboarding constrained by collateral availability. Roughly speaking, if true, the shortfall policy will increase onboarding in proportion to the network-level shortfall uptake. A summary of the impact on deal onboarding by end of year is shown below: 


**Table 1: Impact on Storage Onboarding by 1-Jan-2024.**
| Max Network Shortfall Allowed | Shortfall  Effectiveness | Storage Onboarding Strength | Deal Onboarding | Key |
| ---------- | ---------- | ---------- |---------- |---------|
| 33%        | Low - 0% (no shortfall policy)    | Low     | 3 PiB/Day   |OB_low_SE_low  |
| 33%        | Low - 0% (no shortfall policy)    | Med     | 7 PiB/Day   |OB_med_SE_low  |
| 33%        | Low - 0% (no shortfall policy)    | High    | 10 PiB/Day  |OB_high_SE_low |
| 33%        | Med - 50%                         | Low     | 3.5 PiB/Day |OB_low_SE_med  |
| 33%        | Med - 50%                         | Med     | 8.1 PiB/Day |OB_med_SE_med  |
| 33%        | Med - 50%                         | High    | 11.7 PiB/Day|OB_high_SE_med |
| 33%        | High - 100%                       | Low     | 4 PiB/Day   |OB_low_SE_low  |
| 33%        | High - 100%                       | Med     | 9.3 PiB/Day |OB_med_SE_med  |
| 33%        | High - 100%                       | High    | 13.3 PiB/Day|OB_high_SE_high|

Per Table 1, we seperate the Filecoin economy in to 3 different base scenarios for storage onboarding regimes (3, 7, and 10 PiB/Day, marked as Low, Middle, and High respectively). Reasonable bounds on the onboarding rate were derived via [MCMC forecasting](https://github.com/kkarrancsu/shortfall/blob/add_burn_with_fees/notebooks/mcmc_forecast_onboarding.ipynb) of historical rates of storage power onboarding. Allowing a maximum network shortfall of 33%, we can then calculate estimated storage onboarding per the initial model specified above. 

Beyond this simple characterisation, other more extreme outcomes are possible:
- More pessimistic — there is no unmet demand, in which case shortfall policy could weaken the ecosystem by weakening token demand by damaging external lending markets. 
- More optimistic — successful policy increases onboarding, and helps balance supply through lowering net inflation, which supports external lending markets, improving market efficiency further driving lending costs down, and priming the ecosystem for increased rate of onboarding.

#### Specification Summary for Policy 1
- At any point where an SP needs to lock new initial pledge, they can lock less than the notionally required amount: an incremental shortfall.
- The maximum shortfall is determined by a pessimistic estimate of the expected rewards to an SP’s power associated over the commitment’s term (or the shortest term they have committed).
- When rewards are earned (vested), a fraction are taken for repayments, and some burnt as fees. This reward fraction locked is constant or increasing until the entire shortfall is repaid.
- The fee rate is dynamic. If shortfall is heavily utilised the fee for additional shortfall increases over time, pushing parties back towards sourcing tokens externally.


#### Specification Summary for Policy 2
- At any point where an SP needs to lock new Initial Pledge, they can opt to lock less than the notionally required amount, up to a maximum shortfall fraction of ⅓ of the initial pledge. 
- In exchange for taking a shortfall in the upfront amount of collateral, the SP agrees to gradually ‘repay the protocol’ by burning a proportion of future rewards.
- A proportion of rewards is burned until the obligation is paid off.
- The fraction not burned is distributed the ordinary way between immediate and vested release rewards.

## Modeling Summary 
We look to quantify the impact that implementing each variant of the shortfall proposal could have on the Filecoin token economy. While understanding the impact of a shortfall on an individual Storage Provider’s incentives and decision space is important, we can model the Filecoin economy within various shortfall proposal regimes at the population-level via adaptations to the open-sourced [mechaFIL]('https://github.com/protocol/filecoin-mecha-twin/tree/network_shortfall') model of the Filecoin Economy published by CEL. We then look to examine the impact on token circulating supply, and in particular, minting, burning, and locking under different storage onboarding environments and levels of shortfall adoption. 

### Modeling Methodology 
A robust rate of storage onboarding and growth is a strong indicator of economic activity and health on the Filecoin network. It means that parties are committing raw resources (both capital and hardware) to the network, as well as storage capabilities. We look to simulate and examine a range of potential network behaviors that might arise as a result of the shortfall policy. In particular, we simulate the impact on Filecoin circulating supply dynamics potential changes in storage onboarding behavior. 

As introduced in the "[Impact on Storage Onboarding Potential](https://hackmd.io/xElv2TQXRjuiSmFnY7HLJQ?both#Impact-on-Storage-Onboarding-Potential)" section, we sweep across low, medium, and high base scenarios for storage power onboarding as well as adoption (or "effectiveness") of the shortfall policy for each variant of the shortfall policy (Thing 1 and Thing 2).

The onboarding rate is the amount of storage capacity onboarded per day in PiBs, and shortfall effectivness is the proportion of power per day that is onboarded with the maximum allowable shortfall (33%). The amount of network pledge shortfall increases as a higher amount of power with a larger shortfall adoption rate is onboarded relative to the total size of the network. The reason this design choice was chosen was because only sectors onboarded following the shortfall policy’s implementation are able to take on any shortfall. Assuming any steady state rate of shortfall at the network level immediately upon a shortfall policy’s implementation would therefore be an unrealistic approximation of network population dynamics. 

We sweep across three different onboarding regimes and three network shortfall effectiveness regimes, in which levels of onboarding and shortfall adoption are low, medium, and high. This results in simulations for nine distinct macroeconomic environments, which are summarized in Table 1 above. 

For example, per Table 1 a simulation denoted as “OB_med_SA_med” means simulating the scenario in which the rate of daily onboarding is 8.1 PiBs per day, and for each day of onboarding, `50%` of the power onboarded is taking a `33%` shortfall. Said differently, if the amount of pledge required to onboard 8.1 PiBs on day $d$ is $P_{d}$, the amount actually put up by storage providers on the network on day $d$ is $(1-0.165) \cdot P_{d}$.


## Results and Discussion
<!-- Per the onboarding and network shortfall adoption regimes described above, we examine the effect of the shortfall policy variants on Filecoin's token economy and circulating supply.  -->
Figure 1 shows the circulating supply dynamics given each configuration in Table 1. 

![](https://hackmd.io/_uploads/By65eDGr3.png)
*Figure 1: Circulating Supply dynamics across onboarding and network level shortfall adoption regimes*.

We observe that in the short-medium term (1-2 years following the policy's inception) higher power onboarding rates will initially result in net lower circulating supply relative to lower rates regardless of shortfall effectiveness. This is mainly due to the additional FIL locked to sustain higher storage onboarding rates. This lends credence to the argument that if a network shortfall policy were to help remove some onboarding frictions (namely collateral resourcing), a potentially beneficial short-term macroeconomic effect could be a substantial amount of FIL locked and removed from token supply. However, over the longer-term horizon (3+ years) we note the increasing trend in circulating supply. This is a result that holds true irrespective of either shortfall policy's effectiveness or the strength of storage onboarding. Therefore, either shortfall policy could potentially help stimulate a healthy rate of token inflow in the near-term, but neither shortfall policy can fully reverse the longer-term trend of net token inflow. Figure 2 shows the Percent change in circulating supply for each simulation relative to a "base case" scenario of medium strength onboarding (7 PiBs/Day) with no network shortfall policy in effect. 
![](https://hackmd.io/_uploads/SJWIQNfB3.png)
*Figure 2: Percent Change in Circulating Supply relative to a "base case" scenario of 7 PiBs/Day of Storage Onboarding with no shortfall policy. The top image shows this for "Thing 1" across onboarding regimes and shortfall uptake, and the lower image show the same for the "Thing 2" variant*.

Figure 2 above suggests an interesting results regarding the "permanence" of each shortfall policy's potential impact on token dynamics. We observe that in the initial term,  Thing 1 will yield lower circulating supply relative to the base case, especially in high shortfall effectiveness regimes, relative to Thing 2. This is largely due to the difference in how the Thing 1 and Thing 2 variants handle shortfall repayment. In the Thing 1 iteration, a large portion of block rewards will be diverted in to a Storage Provider's locked balance over the sector's lifetime in order to cover shortfall, whilst a small fraction is burnt as a "protocol fee"; in the Thing 2 iteration, a portion of rewards are simply burnt until shortfall is repaid. However, over time, the FIL locked to cover repayments in the Thing 1 policy variant is eventually "unlocked" and reenters supply, resulting in the corresponding increase in supply relative to the base case shown above. The Thing 2 policy will yield the opposite result; since burnt tokens are permanently removed from supply, over the longer-term time horizon, high shortfall effectiveness regimes will put more persistent downwards pressure on circulating supply. Figure 3 below directly compares the burn **due to shortfall** (i.e. excluding network transaction fees and penalties) across the policy variants, and shows burn due to shortfall as a percentage of circulating supply (shown above in Figure 1).
![](https://hackmd.io/_uploads/rk2jYvMHh.png)
*Figure 3: Burn due to shortfall protocol fees (as in Thing 1) or due to shortfall repayment (as in Thing 2) across onboarding and shortfall effectiveness regimes as a percentage of circulating supply*.

In the high shortfall effectivness regimes, we can expect burn due to shortfall uptake be about 5x higher in the Thing 2 policy variant compared to Thing 1. However, this amount burned is still a relatively small percentage of circulating supply, indicating that locking and burning from transaction fees would likely have a larger effect on longer term supply dynamics.  


## Conclusion
A significant portion of Storage Providers on the Filecoin network may currently face elevated frictions to onboarding storage power due to collateral resourcing and relatively higher initial pledges. The discussion post raised by @anorth isolated collateral resourcing, as well as the growth rate of Filecoin's circulating suppply as sources of uncertainty that may inhibit storage onboarding and longer-term investment in the Filecoin economy. 

The FIP discussion post raised presents two flavors of "network shortfall" policies (known as Thing 1 and Thing 2), in which the Filecoin protocol could enable Storage Providers to onboard power at *less pledge than the full initial pledge amount required*, and use their *future stream of block rewards* to repay some or all of the "pledge shortfall" they incurred. 

Both policies could help stimulate onboarding particularly for collateral constrained Storage Providers and have favorable impacts on the Filecoin economy, via renewed resource commitment to the network. Sweeping across pessimistic, median, and optimistic scenario for storage onboarding at various levels of shortfall updake, we find that both shortfall policies could result in higher rates of onboarding and net lower circulating supply. The Thing 2 variant would likely create more permanent deflationary pressure due to burning a greater share of block rewards to pay back shortfall, but over the long-term, token locking and decreasing initial pledges will largely directionally determine circulating supply dynamics. 

CryptoEconLab will look to provide the community with further analysis and insight on the incentive spaces relevant to the shortfall policies as the public discussion on shortfall policy continues to evolve, and further points are raised by the community. 


## Appendix
- [mechaFIL simulations](https://github.com/protocol/CryptoEconLab/tree/network_shortfall/notebooks/shortfall/macro_sim)
- A [Python simulation](https://github.com/anorth/shortfall/tree/main) of the mechanisms’ function for a single SP. Models the cash flows associated with both leasing and using a shortfall under assumptions of bounded pledge availability or hardware/data and a preprogrammed minting rate. Notebooks include some graphs.
- [An interactive notebook](https://github.com/kkarrancsu/shortfall/blob/add_burn_with_fees/notebooks/shortfall.ipynb) comparing the cash flows for a single SP under Thing-1 and Thing-2, using forecasted minting rates under three different onboarding scenarios using default parametrization.
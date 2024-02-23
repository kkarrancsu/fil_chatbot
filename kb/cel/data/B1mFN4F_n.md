---
title: Resilience of the Filecoin Network
tags: Econ monitor
---

**Authors**: {Kiran, Tom} @ CryptoEconLab

## Summary
- The Filecoin Network contains a mechanism to recover from significant shock to the network power (such as large-scale terminations or network forks). The mechanism works as follows: if a shock event occurs, the network creates strong economic incentives for Storage Providers (SPs) to join the network.
- While the network creates the conditions to enable recovery, the actual recovery depends on the behavior of external actors, namely SPs. 
- While network power has a path to recovery, the ratio of locked tokens to the circulating supply drops proportional to the amount of power that leaves the network. Exponentially increasing onboarding is needed for the locked-to-circulating supply ratio to recover, and the reduction in locked tokens could present a consensus risk to the network and exchange rate instability.
- This analysis does not consider other external factors that could lead to alternative (potentially more negative) outcomes. These include overall network sentiment, which could influence SPs’ decision-making beyond the rational approach outlined.
- Recommended Action Items:
    - Implement procedures allowing SPs to profit from the economically advantageous situation following a network shock before they are necessary. Examples include Network Shortfall to allow onboarding to grow faster than otherwise. 
    - Share this knowledge with SPs about the potential upside in a shock scenario to mitigate the impact of negative sentiment following a shock situation.
    - Research updates to pledge functions that alleviate economic pressure on SPs while maintaining network security to reduce the likelihood of shock scenarios. 

## 1. Introduction
In this document, we attempt to answer the following question: 

How will the Filecoin Network respond to the power-loss scenario where a significant portion of SPs either: 
1. leave gracefully expiring power off the network
2. terminate, causing a shock and a sudden loss of power to the network

We explore several variants of this scenario where different types of SPs (CC miners, Deal SPs, and Mixed SPs) leave or terminate the network at different proportions. Our initial findings indicate that there is a mechanism of the network that can enable it to recover from a network shock, provided that: a) FIL lending options such as Network Shortfall are in place for the recovery mechanism to be utilized, and b) that SPs recognize the economic incentives that manifest and take advantage of them.

Supply dynamics and rewards distribution explain the network recovery mechanism. Let us examine the supply dynamics first. 

If a large proportion of SPs leave or terminate the network, this causes the minting rate to decrease due to decreased RB power. Simultaneously, tokens become unlocked because of pledge release from terminations, lack of renewals, and no new onboarding, causing the circulating supply to increase. However, the drop in QA power also results in network QAP crossing the baseline function. The increase in circulating supply is balanced by the QAP baseline crossing, causing the pledge to increase initially but then drop (due to an exponentially growing baseline). 

Rewards are distributed proportionally to an SP’s share of the total network QAP. As SPs terminate or leave the network, the remaining SPs’ share of the total network QAP increases, creating a strong economic incentive for remaining SPs to maintain or increase storage commitments to the network. 

The mining equilibrium cycle shown in Fig. 1 represents how rational SPs interact with power and reward concentration dynamics.

![](https://hackmd.io/_uploads/r1ziszntn.png)
*Fig 1: The Mining Equilibrium cycle. In generality, the tendency of the Filecoin network to establish an equilibrium state is affected by multiple factors, including exchange rates, cost of production, and initial pledge dynamics, among other factors.*

In this cycle, block rewards get diluted as SPs onboard more power, causing returns to decrease. This results in offboarding power, which then increases reward concentration and induces more onboarding. 

The network shock scenario examined here is a case of this cycle, with the primary difference being that the changes to the network happen instantaneously rather than gradually.

However, despite this mechanism, an unmitigated risk is that many tokens become unlocked, which could cause exchange rate instability. Token unlocking could also reveal other risk factors not explored in these simulations.


## 2. Methods and Experiments
We utilize an Agent-Based Model (ABM) of the Filecoin network to simulate shock scenarios. For a detailed description of the ABM, please view our [research report](https://arxiv.org/pdf/2307.15200.pdf) on using ABMs to model utility based cryptoeconomies, published at the Chainscience 2023 conference.

To model the shock scenario, we simulate a population of three types of SPs: FIL+ SPs, CC SPs, and Mixed SPs.  FIL+ SPs only have FIL+ sectors, CC SPs only have CC sectors, and mixed SPs have both CC and FIL+ sectors with a configured split. A percentage of each type of SP then leaves the network by not onboarding any new power or renewing any expiring sectors. The proportion of SP types and the percentage of SPs which leave the network is configurable. 

We use three agent types to accomplish the behaviors described, the `ROIAgentDynamicOnboard`, the `DCAAgentLeaveNetwork`, and the `DCAAgentTerminate`. The `ROIAgentDynamicOnboard` is a rational agent which forecasts a FoFR and onboards and renews power proportional to the difference between the minimum ROI for which the agent will onboard power and the estimated ROI for onboarding power onto the network up to a maximum. The equation governing how much power the `ROIAgentDynamicOnboard` onboards and renews is given by:

```
m1 = (max_onboard - min_onboard) / (max_roi - min_roi)
rb_onboard = m1 * estimated_roi + offset1
m2 = (max_renew - min_renew) / (max_roi - min_roi)
renew_pct = m2 * estimated_roi + offset2
```
`offset1` and `offset2` are configured appropriately to respect the minimum onboarding configuration of the agents.

The `DCAAgentLeaveNetwork` is an agent which onboards and renews a configured amount but stops onboarding and renewing after a configured date.


The `DCAAgentTerminate` onboards and renews a configured amount of power before the termination date. It terminates all existing power on the termination date and stops onboarding and renewing power after termination. The main difference between the leave and terminate variants is that `DCAAgentLeaveNetwork` lets sectors expire while `DCAAgentTerminate` actively terminates existing sectors.

Because the `DCAAgentLeaveNetwork` agents leave the network gracefully, it does not incur termination fees. The `DCAAgentTerminate` sustains termination fees. Both agent types are configurable to be FIL+ SPs, CC SPs, or Mixed. 

## 3. Experiments

We test the following distributions of SP populations distributed by QAP:
1. 33% FIL+ SPs, 33% CC SPs, and 34% Mixed SPs
2. 49.5% FIL+ SPs, 49.5% CC SPs, and 1% Mixed SPs
3. 69.5% FIL+ SPs, 29.5% CC SPs, and 1% Mixed SPs (FIL+ Skewed)
4. 29.5% FIL+ SPs, 69.5% CC SPs, and 1% Mixed SPs (CC Skewed)

Each SP population consists of two subpopulations, one which does not leave/terminate, and one which does. We test two cases of the amount of the subpopulation which either leaves or terminates: 30% and 70%.

The ROIAgentDynamicOnboard agents are set up with three possible RB onboarding ranges (1-3 PiB/day, 1-6 PiB/day, and 1-15 PiB/day) cases to simulate pessimistic, status-quo, and optimistic onboarding scenarios for the SPs which decide to remain in the network. Correspondingly, the agents can also modulate their renewal rates of existing sectors between 20% and 80%. 80% of Mixed SPs modeled sectors are FIL+ with the same onboarding and renewal bounds. 
Fig 1, 2, and 3 show the optimistic, status quo, and pessimistic scenarios when agents leave the network gradually. Fig 4, 5, and 6 show the same onboarding scenarios when agents suddenly leave/terminate from the network.  


### General Trends
We observe several features across all scenarios:


- Pledge
    - The drop in Network RBP causes minting to decrease substantially. 
    - However, the circulating supply still increases because of unlocking the pledge, causing an initial increase in the pledge. 
     - Network QAP crosses the baseline function, causing the pledge to decrease exponentially because inverse baseline corresponds to pledge scaling down with 1Y half-life (at constant circulating supply). 
- Rewards
    - The Filecoin network distributes rewards to SPs based on their share of the overall Network QAP. The result of overall Network QAP dropping is that the ratio of SPs QA to network QA increases for SPs who remain on the network. Thus, their rewards are more concentrated.
    - This is observed in the Rewards/Sector plot.
- Fil-on-FIL Returns (FoFR)
    <!--     - In terms of FoFR, two effects are distinguished.  -->
    - Since the pledge is paid once, but rewards accrue over time, sectors that remain after power loss can benefit from reward concentration, while the pledge paid remains unchanged, thus boosting the FoFR of remaining power. 
        <!-- 2) Since post-QAP baseline crossing, the consensus component of Initial Pledge decreases roughly exponentially with 1y half-life (at a rate inverse to the baseline doubling time). Since simple minting decreases exponentially with a 6-year half-life, FoFR will scale approximately exponentially with a 1.2-year (6/5) doubling time, conditional on constant circulating supply and onboarding trends. -->
    - In essence, rewards/sector increase faster than the pledge/sector, so FoFR increases. This induces rational agents to onboard more power onto the network, causing the network power to rebound.

The network recovery mechanism is robust under the assumption of rational actors across simulated status quo and optimistic scenarios.

Under the pessimistic onboarding condition, the network RBP hovers dangerously close to 0 EiB. Although the same trends seem to hold for network recovery, we flag the severe drop in RBP as a potential risk for further destabilization - that is not captured by the simulation framework. External risks in this scenario can include public sentiment towards the network after such a severe drop. Understanding whether larger or smaller SP operations are more likely to leave the network will be prudent. Suppose smaller operations are more likely to leave/terminate. In that case, we can expect the larger SPs to be able to onboard more data due to potentially better access to lending markets and larger capital reserves, thereby tending towards the optimistic scenarios presented. Conversely, if larger operations leave, we may be closer to the pessimistic scenario, which is a cause for greater concern.

Across the different scenarios, reward concentration is inversely proportional to the power onboarded by the remaining SPs. More concretely, rewards are more concentrated if the remaining SPs onboard less power. This is shown across the scenarios and within each scenario, where the percentage of SPs that terminate is modulated. Less reward concentration results from fewer SPs leaving the network. However, the economic incentives for onboarding are still powerful. The network recovers to its previous state faster when it terminates less power.


### Differences between Gradually Leaving and Suddenly Leaving

- Power
    - In the termination case, power drops instantaneously from the network, whereas in the “leave” case, power gradually diminishes as sectors expire. The minting rate curves follow these same trends.
    - In the termination case, power continues to drop after the termination date. This is due to the logic of the implemented ROI agents, which dynamically onboards and renews power between the configured bounds as ROI is modulated. Consequently, the ROI estimation algorithm that the agents use significantly affects the output power trajectory.
- Pledge
    - In the termination case, the days immediately following the termination result in the ROI agent’s FoFR estimate toggling above and below the configured minimum threshold. This causes a toggling of the pledge since the only remaining agents do not onboard power when the ROI estimate is below the threshold.
    - Pledge increases more in the termination case than in the leave case. This is because the sudden drop in power results in a large increase in the circulating supply rather than a gradual increase, as in the leave case. Even though the baseline crossing of QAP occurs, its effect is not as significant because less time has elapsed, resulting in the CS contributing a more extensive effect to increasing pledge.
- Reward Concentration
    - In both the leave and terminate cases, reward concentration hits its highest point when network QAP is at its lowest point. 
    - However, in the terminate case, reward concentration jumps immediately at the termination date due to an initial sharp drop in QAP. It effectively stays elevated until the lowest QAP point, after it begins to decrease. Conversely, in the leave case, reward concentration builds as sectors expire from the network. After peaking, it subsequently decreases. 
    - Note that the absolute value of reward concentration is greater in the leave scenario than in the terminate scenario. Appendix - A1 discusses this in further detail.
- FoFR follows directly from the other aspects discussed above.


## 4. Conclusions
Filecoin’s economy is designed to protect the network against adverse shocks. The primary mechanism for this is the interaction between how rewards are distributed and the pledge needed to participate in the network. If participants leave or terminate the network, then rewards for the remaining participants become more concentrated. If reward concentration increases, the total expected rewards per sector exceed the pledge, and FoFR increases, creating strong economic incentives to join and participate in the network.  

While the network creates this as an enabling factor, the actual network recovery still depends on SPs. The SPs must: 1) recognize the incentives and 2) take advantage of them by onboarding power, which requires them to have pledge collateral. The simulations above show a possible outcome when the economic incentives, post-shock, are taken advantage of.

However, this is not a guarantee. Additional external factors are not considered, such as 1) network sentiment due to network shock and 2) price instability due to a significant increase in circulating supply. 


## 5. References
* [ABM Codebase](https://github.com/protocol/filecoin-agent-twin)
* [SP Gradually Leaving Experiments](https://github.com/protocol/filecoin-agent-twin/blob/main/agentfil/cfg/exp_roi_leave.py)
* [SP Terminating Experiments](https://github.com/protocol/filecoin-agent-twin/blob/main/agentfil/cfg/exp_roi_terminate.py)
* [Plot generation code](https://github.com/protocol/CryptoEconLab-private/tree/kiran/notebooks/kiran/abm)

## 6. Figures

### Gradually Leaving
Each of the figures below shows Network metrics for different scenarios of onboarding rates on the date when power starts leaving the network. In each figure, the dashed vertical line denotes the start of simulation, and the dotted vertical line denotes the date at which power starts leaving the network. A baseline case using a `DCAAgent` to simulate constant onboarding is also simulated to provide a basis of comparison (black dotted line). 

![](https://hackmd.io/_uploads/HJ-88veo3.png)
*Fig 1: Filecoin Network KPI’s in the optimistic onboarding case under several conditions of SP’s leaving the network. *

![](https://hackmd.io/_uploads/S1RU8vxo2.png)
*Fig 2: Filecoin Network KPI’s in the status-quo onboarding case under several conditions of SPs leaving the network*

![](https://hackmd.io/_uploads/B1IvIwein.png)
*Fig 3: Filecoin Network KPI’s in the pessimistic onboarding case under several conditions of SPs leaving the network*

### Suddenly Leaving
Each of the figures below shows Network metrics for different scenarios of onboarding rates on the date when power terminates from the network. In each figure, the dashed vertical line denotes the start of simulation, and the dotted vertical line denotes the date at which power starts leaving the network. A baseline case using a `DCAAgent` to simulate constant onboarding is also simulated to provide a basis of comparison (black dotted line). 

An interesting feature to observe here is that reward concentration jumps immediately at the termination date. This is due to an sharp drop in QAP. It effectively stays elevated until the lowest QAP point, after it begins to decrease. Conversely, in the leave case (Fig 1,2,3), reward concentration builds as sectors expire from the network. After peaking, it subsequently decreases.

![](https://hackmd.io/_uploads/r1BdLPgo2.png)
*Fig 4: Filecoin Network KPI’s in the optimistic onboarding case under several conditions of SP’s terminating from the network*

![](https://hackmd.io/_uploads/ry3OUwlsn.png)
*Fig 5: Filecoin Network KPI’s in the status-quo onboarding case under several conditions of SPs terminating from the network*

![](https://hackmd.io/_uploads/rkZFLvxo3.png)
*Fig 6: Filecoin Network KPI’s in the pessimistic onboarding case under several conditions of SPs terminating from the network*

## Appendix A1 - Detailed information on differences in the absolute value of rewards concentration between Leave and Terminate

Fig. 7 illustrates the reason for the difference in the rewards concentration amounts between the leave and terminate cases. We observe that:
Slight differences in the minting rate and total QA power at the lowest points contribute to the absolute value of differences between terminations and leaving the network.
This is due to differences in how the ROI agents behave in the two cases. In the termination case, the agent’s ROI estimate toggles above and below the threshold (likely due to estimation algorithm implementation). The toggling is reflected in the pledge/32GiB plot, which shows in the terminate cases that pledge toggles - this is due to the agents toggling between onboarding and not onboarding due to their ROI estimates. In the leave case, the agents do not toggle.

Fig. 8 shows a detailed plot of the agent decisions, and also helps to explain why there are two peaks of reward concentration in the termination case.  Two peaks in reward concentration occur because of the behavior of the ROI agents who remain on the network. After termination, these agents onboard and renew small amounts of power (due to their configuration), leading to power continuing to drop further until it hits its lowest point (where rewards concentration peaks). At that point, the ROI agents consistently pick up their onboarding and renewals.


![](https://hackmd.io/_uploads/BJdKYDeo3.png)
*Fig 7 - Comparison of Network KPI's for the gradually leave and suddenly leave scenarios.*

![](https://hackmd.io/_uploads/rkaQcEKdh.png)
*Fig 8 - An illustration of agent decisions in the gradually leave and suddenly leave scenarios*

## Appendix A2 - Protectiveness of Termination Fees
Here, we quantify the effect of termination fees on the overall circulating supply. We approach this from an upper-bound perspective since the simulations above terminate fractions of the overall power. 

The maximum possible burn due to terminations is 36,711,768 FIL, about 6% of the circulating supply if all network power is terminated. This presents some friction to termination but is low in the context of the entire circulating supply.

Refer to [this notebook](https://github.com/protocol/filecoin-agent-twin/blob/main/notebooks/terminations/dca_terminate_oneagent.ipynb) for further details.
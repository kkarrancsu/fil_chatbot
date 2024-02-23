---
title: Fil+ Multiplier Scenarios
tags: Econ monitor
---

**Authors**: {Kiran, Tom} @ CryptoEconLab

## Summary
* We evaluate several options discussed in the [*Motivation for a Scheduled Reduction in the Quality Multiplier of Fil+ Deals and Example Timelines* GitHub discussion](https://github.com/filecoin-project/FIPs/discussions/774) for sunsetting the Fil+ multiplier. We examine the cryptoeconomic impacts of each option, from the perspective of Network Power, Locked collateral, and FoFR returns.
* Of the proposed variants to update the Fil+ multiplier, the option where all sectors (regardless of whether they are Deal or CC) are given a 10x QA multiplier offers the most positive benefits to network security and new entrants into the system:
    * From a network perspective, this better supports locked collateral, which is the primary source of consensus security for the network. 
    * This policy is also better for new SPs, who would otherwise have no multiplier to dilute costs, compared to current network power which would create minimal incentive for new SPs to join the network. 
* The primary change that any reduction to the FIL+ multiplier would bring, however, is removing the cryptoeconomic structure the network uses to incentivize data storage over disk usage. Utility might grow spontaneously without this, but there is no guarantee, and it may be unlikely at this early stage of the network without the help the Fil+ program gives. 

## Simulations and Analysis
In this analysis, we examine several options for varying the Fil+ mulitplier suggested by participants in [GitHub discussion 774](https://github.com/filecoin-project/FIPs/discussions/774):
* **Option 1** - All new power after policy implementation becomes 1x.
* **Option 2** - All new power after policy implementation gets a multiplier depending on when it is onboarded. The multiplier is halved every six months until it reaches 1.0 in two years.
* **Option 3** - All new power after policy implementation becomes 10x.
* **Option 4** - All new power after policy implementation gets a multiplier depending on when it is onboarded. The multiplier is reduced linearly from 10.0 to 1.0 over the course of 24 months to be direclty comparable to **Option 2**.

Fig. 1 shows the various scenarios of Fil+ multiplier changes considered.

![](https://hackmd.io/_uploads/SJ79IDW32.png)

*Fig 1: The Fil+ multiplier applied to all new QA power added after a policy introduction date in the scenarios considered.*

In each scenario, we use MCMC to forecast the RBP onboarding until the policy change date, which is configured to be 2024-01-01. At the policy change date, we test three onboarding levels of RBP, at 5 PiB/day, 10 PiB/day, and 15 PiB/day, and set the renewal rate to 50%. Since the renewal rate fluctuates, this is a middle ground that captures the “average” case of the network. We set the FIL+ rate to 100% to observe the effect of the various multiplier schedules and note that this is very close to current onboarding trends where the FIL+ rate is greater than 90%. 

### Alternative future scenarios for Fil+ Multiplier
Option 1, 2, 3, and 4 are simulated using the digital twin, [mechaFIL](https://github.com/kkarrancsu/mechafil-jax.git). We compare the network KPIs of these options to the policy of no change. Relevant metrics are shown in Fig. 2.

In **Option 1**, all new power after policy update becomes 1x. This is a more radical change that sees:
* QAP drop significantly compared to no change.
* Locked collateral is much lower than no change. This is an issue because out of the two main contributions to network security — hardware and consensus pledge collateral — the collateral component is estimated to be an order of magnitude greater by fiat value. So if locked collateral decreases this makes it easier to take control of the network.
* In the immediate term of 1-3 years, FIL-on-FIL returns (FoFR) with costs included drops from around 25% to -25%. The drop is because new power cannot benefit from the cost dilution offered by the Fil+ multiplier, whereas existing power can.
    * Note that the exact values will depend on factors such as the FIL exchange rate, individual SP cost models, as well as future network power trajectory.

In **Option 2**, we implement a policy where the Fil+ multiplier is halved every six months and reaches 1x, two years after the policy change is implemented. The Fil+ multiplier change is shown in Fig 1b. Here, we observe that:
* NetworkQAP exhibits a declining trend across all onboarding scenarios, due to the reduced QA multiplier. However, QAP is higher than the 1x scenario (**Option 1**).
* Network locked follows a similar trend, and this follows from the reduced collateral requirements from decreasing Network QAP.
* The FoFR with costs decline is more drawn out but exhibits sharp drops which accompany the Fil+ multiplier changes. This follows from the reduced cost dilution each time the QA multiplier is reduced. The intensity and dynamics of the FoFR with costs decline is sensitive to SP costs and network power dynamics.

In **Option 3**, all new power after policy implementation becomes 10x. This counterfactual is similar to having no change in policy because:
* QAP is slightly higher than no change.
* Locked collateral is slightly higher than no change.
* FoFR with costs is slightly lower than with no change.
The primary change is network utility which explicitly incentivizes data storage.

In **Option 4**, we implement a variant of **Option 2**, where we linearly ramp down the Fil+ multiplier such that it reaches a value of 1.0 by Year 2. Fig. 1d shows the evolution of the Fil+ multiplier in this scenario.
* NetworkQAP exhibits a declining trend across all onboarding scenarios, due to the reduced QA multiplier schedule, but QAP is higher than in the 1x scenario (**Option 1**). Compared to the cliff ramp-down schedule (**Option 2**), QAP has a smoother trajectory but still trends downward.
* Network locked follows a similar trend, and this follows from the reduced collateral requirements from decreasing NetworkQAP. The change is smoother than **Option 2**, due to the smoothness of the Fil+ multiplier schedule.
* The FoFR with costs gradually declines due to the linear rampdown of the Fil+ multiplier, but then increases. This follows from the reduced cost dilution each time the QA multiplier is reduced.
    * The exact dynamics depend on several factors including: (i) the cross-correlation of the rewards with the linear ramp, (ii) how quickly future storage costs decrease, and (iii) initial pledge dynamics.

![](https://hackmd.io/_uploads/r1BhMcMhh.png)

*Fig 2: Each column represents a different counterfactual scenario. The column title indicates the scenario being investigated. The blue, orange, and green lines correspond to 5, 10, and 15PiB/day raw-byte power onboarding at the policy update date. The cost model for the ‘FoFR with Costs’ rows is described in the appendix. In the FoFR with Costs panels, before the policy change, the lines correspond to the typical 10x miner, and after the event they correspond to the specific scenario (10x, 1x, or ramp-down versions).*

## Conclusion
In this report, we explored the cryptoeconomic impacts of several approaches to sunsetting the Fil+ program through QA multiplier modifications. We find that all variants which propose reducing the multiplier to 1x, either immediately (**Option 1**) or through a defined schedule (**Option 2**, **Option 4**) threaten network consensus security. Additionally, we find that due to the reduction in cost dilution, incentives for new SPs to join the ecosystem are reduced in these options. An alternative approach to sunsetting the Fil+ program, whereby all new power is given the 10x multiplier has two advantages: 1) to maintain the locked collateral thereby contributing to the security of the network, and 2) to maintain incentives for new SPs to join the network. 

*Disclaimer: Do your own reasearch, this is not financial advice.*

## Appendix
#### Cost Modeling
We model cost with two components: a) costs that scale with the multiplier (i.e. pledge borrowing costs), and b) costs that are fixed (hardware costs). These are computed per sector as follows:

* Borrowing costs are defined as a percentage of the pledge, set to 5% in the simulations. The percentage is a constant that should be viewed as a way to scale the borrowing costs with changing pledge requirements.  The 5% value can be changed, but the trends in the FoFR with costs row in Fig 2 would remain, regardless of the absolute value chosen.
* A reference fixed cost per sector is selected. This is set to be equal to the borrowing cost at the beginning of the simulation. Fixed costs are then decayed over the course of the simulation to simulate hardware and sealing costs becoming cheaper over time. In the simulations above, we decay the fixed costs such that costs are halved every 3 years.  
    * We note that this is likely a pessimistic fixed cost model because it does not take into account step-level changes such as Sealing-as-a-Service or the introduction of new technologies.

Total costs are subtracted from the returns and then scaled by pledge in order to compute FIL-on-FIL returns (FoFR) with costs. More precisely, this is given by:

$CostFoFR = \frac{(\frac{returns}{sector}*multiplier - \frac{totalcost}{sector})}{(\frac{pledge}{sector}*multiplier)}$

#### Modeling SP Transition Behavior 
We extend the rampdown options (**Option 2** and **Option 4**) to include the counterfactual scenario where onboarding is increased before the policy update date. This is a potential rational action, due to the sudden drop in FoFR after the policy is implemented, as shown in Fig 2. above. To simulate this, we simulate onboarding trajectories where the raw-byte power onboarded per day is linearly increased from its starting value to a certain percentage of the steady-state value until the policy update date. This is indicated by the RampUp percentage value in Fig 3. Note that a RampUp=0.00% is not equivalent to the main set of simulations, which use MCMC forecasting for the RBP trajectory until the policy update date. We then exponentially decrease the onboarding rate from the policy update date to a steady-state value in 90 days, simulating a return back to steady-state. 

The RBP trajectories simulated are shown in Fig 3. Fig 4
shows the network KPIs to compare the effect of the transition period.  We observe that both the power and locking trajectories are concordant with the RampUp value; that is, as RampUp is increased, power and locking trajectories also increase. The inverse is true for the FoFR with Costs. This is because increased QAP results in more reward dilution, thereby reducing the FoFR with costs.

![](https://hackmd.io/_uploads/S1Yx1G33h.png)
*Fig 3: RBP Trajectories considered to model the transition dynamics whereby SPs increase their onboarding before policy update to optimize FoFR trajectories.*


![](https://hackmd.io/_uploads/Hk0ekMh33.png)
*Fig 4: Each column represents transition variants of counterfactual scenarios discussed. The column title indicates the scenario being investigated. The blue, orange, and green lines correspond to 5, 10, and 15 PiB/day raw-byte power onboarding at the policy update date.  The brightness of the line corresponds to the increase in onboarding before policy update, with brighter lines corresponding to larger increases. The cost model for the ‘FoFR with Costs’ rows is described in the appendix. In the FoFR with Costs panels, before the policy change, the lines correspond to the typical 10x miner, and after the event they correspond to the specific scenario.*

## References
* [Simulations](https://github.com/protocol/CryptoEconLab/blob/mechafil-jax-notebooks/notebooks/mechafil_jax/filp_experiments/filp_scenarios.ipynb)
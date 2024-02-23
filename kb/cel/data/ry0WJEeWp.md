---
title: Universal Multipliers
tags: Econ monitor
---

**Authors**: CryptoEconLab

## Summary
* The CE impacts of providing QA multipliers to all sector types, termed universal multipliers and discussed in [FIP 833 - Reasons and Suggestions for Increasing the Quality Multiplier of Filecoin Networks](https://github.com/filecoin-project/FIPs/discussions/833), are evaluated from various perspectives.
* Deviations in network KPIs from the status quo are driven by opposing forces: a) increase in Network QAP due to increased multipliers, and b) potential decrease in Network QAP due to increased percentage of CC sectors onboarded. In terms of the multiplier options considered, 5/5/20 has the greatest and most uniform effect, since the increase in multipliers is large enough to dominate plausible changes in onboarding behavior (that were simulated). The 5/5/10 and 2.5/2.5/10 options are more nuanced due to the competing forces.
* Power and Minting
    * Minting Rates will not change unless [FIP 833](https://github.com/filecoin-project/FIPs/discussions/833) spurns additional raw-byte power onboarding to the network.
    * Overall Network QAP changes as a result of the multipliers update. In the 5/5/20 case, QAP BLC is pushed out for all considered cases of Fil+ onboarding rate after network upgrade. For the 5/5/10 and 2.5/2.5/10 options, if the Fil+ rate stays at current levels or drops slightly, QAP BLC is still pushed out.  However, if Fil+ rates drop significantly, this brings forward the QAP BLC. 
* Circulating Supply
    * Larger multipliers result in increased locking, but the effect is less transitory if there is an associated increase in onboarding.
* Fiat ROI
    * The 5/5/10 option reduces the relative gap between CC and Fil+ sectors the most, and consequently, this option has the biggest boost in Fiat ROI for CC and RD miners. 
    * The 5/5/20 option increases absolute Fiat ROI for all sector types the most. 
    * Any sensitivity of the token price to changes in locking will result in proportional changes to Fiat ROI.
* Fil+ Considerations
    * Closing the gap between FIL+ and CC multipliers reduces relative incentives to onboarding Fil+ deals and the incentive to cheat.


## Simulation and Analysis

In this analysis, we consider the cryptoeconomic impacts of updating [FIP 833 - QA multipliers to sectors discussed in Reasons and Suggestions for Increasing the Quality Multiplier of Filecoin Networks](https://github.com/filecoin-project/FIPs/discussions/833). This FIP proposes increasing the QA multiplier for CC and RD sectors from 1x to 5x and FIL+ sectors from 10x to 20x. 

Our approach is to simulate the effect of this change on the Filecoin economy using [mechaFIL](https://github.com/protocol/filecoin-mecha-twin/tree/policy_update).  The policy change is simulated for all sectors, meaning that new sectors onboarded and renewed after the policy introduction date will receive the new QA multipliers. 

To explore the design space further, we explore several variations of QA multiplier schedules from the FIP 833 proposal. Table 1 outlines the QA multiplier schedules that were simulated.


*Table 1: Multiplier schedules considered*
| Option | CC QA Multiplier | RD QA Multiplier | FIL+ QA Multiplier
| -------- | -------- | -------- | -------- |
| StatusQuo     | 1     | 1     | 10     |
| 2.5/2.5/10     | 2.5     | 2.5     | 10     |
| 5/5/10     | 5     | 5     | 10     |
| 5/5/20     | 5     | 5     | 20     |

To simulate a hypothetical increase in onboarding that results from passing FIP 833, we scale the RBP onboarding rate by 1x, 1.5x, and 2x. Specifically, this increases the onboarding rate by the 1, 1.5 and 2 PiB/Yr, respectively. Additionally, since this FIP aims to make CC onboarding more attractive by decreasing the ratio of QA multiplier for Fil+ and CC sectors, we simulate onboarding scenarios from the current status-quo that have decreased Fil+ sectors onboarded. This is modeled with a percentage decrease in Fil+ onboarding rate, computed for 0% decrease, 20% decrease, and 50% decrease to understand the directionality of the effect.

We show the 20% decrease scenario in all subsections below, to model the intended effect of the FIP. The scenarios where FIL+ rate decreases by either 0% or 50% are shown in the Appendix. Furthermore, note that the expected decrease in FIL+ rate (and consequently increase in CC sectors onboarded, due to total RBP being held constant) is a hypothetical that depends on individual SP cost profiles that determine their business direction. It is important to note that the 20% is not an expectation or a benchmark, but rather a modeling scenario. 

#### Power and Minting
Fig. 1 shows the Network RBP, QAP, and minting trajectories resulting from the policies outlined, for a 20% reduction in Fil+ onboarding rate.  The other scenarios (0% reduction, and 50% reduction) are shown in the appendix. The colors indicated by the legend in the plot show the specific multiplier scenario considered, and the color intensity indicates the scaling factor.

![](https://hackmd.io/_uploads/rkVXbExbp.png)
*Fig 1: Network RBP, QAP, Minting and Minting Percentage Increase from Status-Quo for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 20% reduction from the status-quo of 92%.*

Fig 1 indicates that:
* Increase in minting rate is proportional to the increase in onboarding that can potentially result from the passage of FIP 833. A sustained 2x increase in onboarding in response to the FIP passing can result in an increase of up to 10% in total minting from the status-quo.
* Network QAP increases proportionally to the multiplier option considered; larger multipliers result in larger overall Network QAP. 
* The 5/5/20 option extends the timing of the QAP baseline crossing event. In the 20% Fil+ rate reduction scenario, QAP BLC remains about the same for the 2.5/2.5/10 and 5/5/10 options. However, if Fil+ rate decreases less than 20%, QAP BLC is still pushed out in these options. Conversely, if Fil+ rate decreases more than 20%, QAP BLC would be pulled further in. See the Appendix for further details.
    * Note that Fig 1 is not a forecast of QAP BLC with Monte-Carlo simulations but a projection of the directionality of QAP BLC if QA multipliers are increased with FIP 883

#### Circulating Supply
Fig 2 shows the impact of the multipliers on circulating supply. Larger multipliers increase locking and consequently decrease circulating supply in the immediate term. Because no changes are proposed to the Target-Lock parameter, the Locked/Supply tends towards its target of 30% in the longer term. 

![](https://hackmd.io/_uploads/ByF_bVlbT.png)

*Fig 2: Circulating supply and related metrics for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 20% reduction from the status-quo of 92%.*

The forecasts shown in Fig 2 are under the assumption that Fil+ sectors are onboarded 20% less than the status-quo. Here, 
* The 5/5/20 variant results in the largest decrease in circulating supply. 
* 5/5/10 and 2.5/2.5/10 can also decrease the circulating supply, but only if the FIP is compouned with an increase in onboarding. The effect also takes longer to manifest. 
    * If there is no associated increase in onboarding, the increased multiplier from the FIP competes with any hypothetical decrease in Fil+ rate onboarding to set the overall Network QAP, which affects circulating supply. This is observed in the light red and blue lines in the Pct. Decrease CS subplot in Fig 2.

#### Incentives
Fig 3 explores the impact of the multipliers on pledge and Fil-on-Fil returns.  Consenusus pledge is directly proportional to circulating supply, and inversely proportional to Network QAP. Increasing multipliers increases Network QAP, and decreases circulating supply, meaning that pledge is decreased. 

Fig 3A shows the pledge for the proposals, where the Fil+ onboarding rate is reduced by 20% as a result of the FIP. We observe that the 5/5/20 option (green) uniformly decreases pledge, regardless of potential changes in RBP. The 5/5/10 and 2.5/2.5/10 options see pledge remain about the same as the status quo. Note that this depends on the Fil+ onboarding response. If Fil+ onboarding rate is reduced further than 20%, pledge increases from the status-quo. Conversely, if Fil+ onboarding rate is reduced less than 20%, the pledge converges further to the status-quo.

The associated FoFR plot is shown in Fig 3B. We see that FoFR follows the status-quo trajectory in the 5/5/10 and 2.5/2.5/10 cases. This happens until about 2025-07, but then turns upward due to the QAP BLC. Since the QAP BLC is pushed out further in the 5/5/20 option (green), the FoFR upward turn is not seen in the FoFR observation window in Fig 3B.

![](https://hackmd.io/_uploads/r1p2W4lZ6.png)

*Fig 3: Pledge and ROI for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 20% reduction from the status-quo of 92%.*

#### Fiat ROI
Next, we examine the Fiat ROI for different SPs under the cost model assumptions detailed [here](https://hackmd.io/gzftJx5eQDKhv4-UEubSgg?view=#Misconception-3-Fil-decreases-network-capacity). Fig 4 shows this projection. Here, we assume that deal income for FIL+ SPs is $16/TiB/Yr and compute the Fiat ROI at an exchange rate of $4. To simulate a potential increase in the exchange rate as a result of increased locking, we do the following:
Compute a ratio of of the network locked between the multiplier scenario considered and the status-quo.
Define an additional hyperparameter, sensitivity, to be a user-definable parameter that represents how sensitive the FIL token price is to the associated increase in locking.
We then modulate the exchange rate according to the rule: `StartingPrice * (1+LockedRatio*Sensitivity)`. Note that this is a simple model to understand the directionality of the effect of potential changes in token price as a result of the FIP, but not intended to be a reference or a prediction of how the token price may change as a result of the FIP.

Fig 4 shows the ROI projections for two different sensitivities for each multiplier proposal. All multiplier increases result in increased absolute Fiat ROI from the status quo. Closing the multiplier gap between FIL+ and CC/RD makes CC/RD more competitive.  The effect is more pronounced with the 5/5/10 option than the 2.5/2.5/10 option since the delta between CC and FIL+ is less in the former (2x vs 4x). The absolute value of the multipliers matters, which is why the FIL+ SP sees the biggest boost with the 5/5/20 proposal. 

This effect additionally manifests in the relative ordering of the multiplier proposals. We observe that CC and RD benefit most from the 5/5/10 proposal, whereas FIL+ benefits most from the 5/5/20 proposal. 

![](https://hackmd.io/_uploads/S1mbzNe-p.png)

*Fig 4: Fiat ROI projections for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 20% reduction from the status-quo of 92%.*

#### Fil+ Considerations
In this section, we discuss how the change in multipliers affects variants of FIL+ profiles in the Filecoin ecosystem. The FIL+ variants we consider are a regular FIL+ SP, and three versions of FIL+ SPs who cheat the FIL+ system in various ways.  The specifics of each business profile are defined in [this article](https://hackmd.io/gzftJx5eQDKhv4-UEubSgg?view=#Business-Profiles).

For each profile, we compute the difference in FiatROI between choosing to be that particular variant of a FIL+ SP and choosing to be a CC SP. Since it is assumed that cheating FIL+ SPs do not actually store valuable data (and also don’t have storage revenues), this difference in FiatROI’s is a numerical proxy for the incentive to onboard Fil+ vs. CC.  A greater difference means that there is a greater incentive to onboard Fil+ sectors, and vice-versa. 

This difference is computed for the different multipliers considered in Table 1 for different sensitivities.  Fig 5 and 6 show the change in FiatROI for sensitivities of 0.25 and 0.75, respectively. We observe a reduced (but still positive) incentive to cheat for the 5/5/10 proposal when compared to others in Table 1. This matches intuition because 5/5/10 maximizes closing the gap between FIL+ and CC. If slashing is introduced into the FIL+ program for cheating (V3-ExploitFIL+), all proposals except for 5/5/20 make cheating irrational. 

![](https://hackmd.io/_uploads/B18emVeWa.png)
*Fig 5: Change in FiatROI for each business profile and different multiplier configurations for a sensitivity of 0.25 and a 20% decrease in Fil+ rate onboarding.*


![](https://hackmd.io/_uploads/Hk5xXEl-6.png)
*Fig 6: Change in FiatROI for each business profile and different multiplier configurations for a sensitivity of 0.75 and a 20% decrease in Fil+ rate onboarding.*

We invite the user to explore how the relative incentives for CC and variants of Fil+ mining change as the cost assumptions change, with this interactive [calculator](https://fil-universal-multipliers.streamlit.app).

#### Conclusion
The CE impacts of increasing multipliers can be summarized as follows:
* Network RBP and Minting are unaffected unless the increasing multipliers policy results in significantly increased onboarding.
* The choice of multiplier determines many of the network KPIs. Smaller relative increases to status-quo mean that two competing forces, namely, the increase in multiplier vs the potential decrease in Fil+ onboarding due to increased incentive for CC, will determine the network KPIs. 
* Closing the gap between CC and FIL+ reduces the relative incentive to onboard Fil+ sectors and reduces the incentive to cheat. 

### References
* mechaFIL [branch](https://github.com/protocol/filecoin-mecha-twin/tree/policy_update) used for simulation
* [Analysis notebook](https://github.com/protocol/CryptoEconLab/blob/mechafil-jax-notebooks/notebooks/universal_multipliers/all_sectors.ipynb)
* [Interactive calculator](https://fil-universal-multipliers.streamlit.app)

### Appendix

#### Power & Minting

![](https://hackmd.io/_uploads/SkaKN4eZa.png)

*Fig 7: Network RBP, QAP, Minting and Minting Percentage Increase from Status-Quo for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 0% reduction from the status-quo of 92%.
*


![](https://hackmd.io/_uploads/SkdYVEg-T.png)

*Fig 8: Network RBP, QAP, Minting and Minting Percentage Increase from Status-Quo for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 50% reduction from the status-quo of 92%.
*

#### Circulating Supply

![](https://hackmd.io/_uploads/r1yd4Ngb6.png)

*Fig 9: Circulating supply and related metrics for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 0% reduction from the status-quo of 92%.*

![](https://hackmd.io/_uploads/SkN_44lW6.png)

*Fig 10: Circulating supply and related metrics for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 50% reduction from the status-quo of 92%.*


#### Incentives

![](https://hackmd.io/_uploads/H1MUVNeZa.png)

*Fig 11: Pledge and ROI for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 0% reduction from the status-quo of 92%.*

![](https://hackmd.io/_uploads/SJ8UNNeb6.png)

*Fig 12: Pledge and ROI for different multiplier schedules and RBP scaling factors, and Fil+ rate at a 50% reduction from the status-quo of 92%.*
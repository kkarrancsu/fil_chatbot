---
title: SDM Policy - Scenario Analysis
tags: Econ monitor
---

# Duration Multiplier Policy --- Extreme Scenario Analysis 

**Authors**: {Vik, Kiran, Tom} @ CryptoEconLab

---

## Summary
This document is a summary of analysis that explored different sector duration multiplier (SDM) policies, across storage provider (SP) responses to the policies, and investment and onboarding environments. 

The key takeaways are:

- Filecoin's economy has massive potential for growing utility this year and SDM can enhance this substantially. It is also acknowledged that in extreme scenarios, introducing a duration multiplier with the wrong parameters could lead to lower data onboarding and lower raw byte power (RBP), depending on what type of constraint dominates growth in the short term.
- On the basis of considering more extreme scenarios, in the current iteration of the FIP-0056 draft we advocate for a precautionary approach. We suggest a maximum duration multipler of 2x at 5Y commitment, which corresponds to a SDM slope of 0.285.
- Furthermore, we raise awareness that in order to protect rational incentives to maintain commitments across a wider range of scenarios, the community should consider revising termination fees upwards. The need for a policy upgrade is highlighted by and interacts with SDM, but also exists in a world without duration incentives.
<!-- - We suggest a maximum multiplier of up to 2x at 5y.  -->


## Introduction 
In the Filecoin network, sector quality is a function of the amount of sector space-time that is allocated to verified deals. The precise relationship governing sector quality is given by:

$$ SectorQualityMultiplier = \frac{\sum_{deals} DealWeight * DealQualityMultiplier}{SectorSpaceTime} $$

$SectorQualityMultiplier$ captures the amount of useful data that a sector is serving and is used when computing a storage provider's (SPs) quality adjusted power (QAP).  In the current implementation, $DealQualityMultiplier = 10$. This equates to deal bytes from verified clients receiving a 10x multipler when computing sector QAP, while regular deal and CC sectors receive 1x QA multiplier.

In this report, we consider the implications of adding an additional multiplier applied to all sector types that provides an additional incentive for longer sector durations, and consequently helping fulfill Filecoin's mission: to be a long-term and robust foundation for humanity's information.

## Data Onboarding Conservation vs. Investment Conservation Regimes
To understand the effect of a sector duration multiplier (SDM) on the larger economy, we consider two endpoint states in which the Filecoin economy can be operating in at any given time. The states are the **Data Onboarding Conservation** regime and the **Investment Conservation** regime. 

The **Data Onboarding Conservation** regime is the scenario where data onboarding follows the current trend. If average duration increases, network QAP and locking also increase.

In the **Investment Conservation** regime, the amount of investment flowing into the economy is fixed. In this case, if average duration increases, onboarding and renewal rate must decrease. This is because pledge increases proportional to network QAP and a duration multiplier increases network QAP.

The exact state in which the economy lies is driven both by internal and external considerations, including macroeconomic conditions. We emphasize that neither of these scenarios are expected to be the most likely. They are considered only to frame the conversation through considering extreme outcomes.

<!-- ### Likelihood onboarding dips following SDM -->
#### Current state of Filecoin Economy

Although investment and data onboarding are both constraints, the former (investment) has recently received more attention in the community. Therefore in the near term, **it is possible Filecoin can lean more toward the Investment Conservation regime**. 

This is highlighted by current challenges, framed by SPs as "inability to scale" and by Ecosystem Growth as the "liquidity challenge", resulting from a lack of FIL being engaged to lend in order to support onboarding. **This is not due to lack of FIL in circulation, but rather, from a nascent and developing finance ecosystem that is operating on a challenging global macro-economic environment**, with specific factors including: 
- **Understandable SPs caution to take on currency exchange risk** directly, and FIL variance through issuance (estimated to account for around 50% of observed exchange rate variation).
- An ecosystem in the early stages of building up diversity in financing options to spread risk between different entities and instruments. 
- External factors such as central bank rates and industry volatility. 

**If we assume financing is the primary constraint limiting ecosystem growth**, it is important to consider potential side-effects duration incentives may have such as reducing data onboarding or hardware backing consensus. This is not expected, but it is necessary to consider. 

Discussion of the factors and potential impacts are set out below, with accompanying simulations, alongside a modification of the current FIP. 

## Impact of SDM in each regime

Concretely, what is the impact of being in the Investment Conservation regime where a duration multiplier reduces data onboarding compared to the Data Conservation regime?

### Methodology

We forecast network power, minting, pledge, and SP ROI (before fees) using [mechaFIL](https://github.com/protocol/filecoin-mecha-twin), sweeping across a variety of SDM multipliers under both the data onboarding conservation and investment conservation regimes. 

Data onboarding conservation is simulated with a constant onboarding and renewal rate at their current levels, respectively. 

Investment conservation is approximated by scaling onboarding and renewal rates by the sector duration multiplier.

### Results

Fig. 1 below shows the forecasts of various network econometrics, and Fig. 2 shows the inputs used to simulate the various scenarios. 

![](https://hackmd.io/_uploads/HkElxmBAs.png)

*Fig 1. In the Investment Conservation scenario (solid lines), RB onboarding and renewal rate are extended by their historical values in the 1Y case, and scaled by the corresponding sector duration multiplier in the 3Y and 5Y cases (see Fig 2). In the Data Conservation scenario (dashed lines), data onboarding is maintained and duration multipliers act on top of this assumption. In each FIL+ rate is kept at 60% to reflect current network trends, and SDM slopes of 0.285x and 1x are simulated. ROI is pre-costs.*

![](https://hackmd.io/_uploads/H1j80fSAs.png)

*Fig 2. Input configuration to mechaFIL that is used for various scans when testing the investment conserved regime when both RBP and RR are scaled by the SDM multiplier. D) shows the various SDM slopes that are considered.*

Under current trends of raw-byte onboarding rate, renewal rate, and FIL+ rate, we observe that in the data onboarding conserved scenarios, network RBP (Fig. 1A) is maintained at current levels; variations are due to differences in sector durations that are simulated. Because RBP is maintained, minting stays the same across all data onboarding conserved scenarios (Fig. 1C). Under the investment conserved scenarios, represented by the solid lines, we observe a dip in network RBP. This necessarily follows from the investment conservation thesis, and results in reduced minting as a direct consequence of reduced network RBP.

Network QAP (Fig. 1B) in the data conserved regime increases at a fast rate due to SDM multiplier. In the investment conserved regime, network QAP also increases but at a slower rate due to reduced onboarding and renewals.

Pledge (Fig. 1C and 1E) in the data onboarding conservation regime decreases with the introduction of SDM due to the increase in network QAP. Conversely, in the investment conservation regime, pledge shows a decreasing trend and eventually reaches the same levels as in the data conservation regime. The initial jump in pledge can be explained by focusing on the dashed and dotted black lines. The dashed line is the start of the simulation and the dotted line is when SDM is enabled. Between those time-periods network QAP decreases. This follows from the investment conservation hypothesis since RBP is dropping but SDM has not yet been enabled. Once SDM is enabled, the QAP recovers. These two regions are shown in the pledge trajectories, where the pledge initially increases due to the drop in network QAP but changes direction as soon as SDM is enabled. 

Finally, the network ROI trajectories (Fig. 1F) show that in the FIL conservation regime, SDM has a higher expected ROI over longer time horizons, and this is inversely proportional to the amount of locked FIL. Stated differently, lower SDM values produce higher ROI but lower network locking, while higher SDM values produce lower ROI but higher network locking. Effectively, the choice of SDM slope enables a fine-tuning of the balance between immediate rewards and network stability and security. 

## Termination Incentives Across Regimes
We also examine the incentive for individual SPs to terminate sectors, and, consider the extreme case in which an individual SP with $M$ sectors terminates $M\cdot(1 - \frac{1}{max(SDM)})$ of her sectors and reonboards $\frac{M}{max(SDM)}$ sectors for the maximum duration, maintaining her effective power consolidated across a smaller number of sectors. For the remaining hardware that she does not recommit to the network, we assume the SP resells them and earns a rebate equivalent to the “salvage value” of the previously committed hardware. The alternative is for the SP to not terminate the $M$ sectors.

The incentive to terminate is then defined as the ratio of the ROI if the SP decides to terminate to the ROI if the SP decides to not terminate. 

This is considered in the context of two group-level behaviors: a) the population of SPs decides to terminate and b) the population of SPs decides to not terminate. 

An ROI ratio greater than one implies a rational incentive to terminate to consolidate via a duration multiplier. Estimated incentives to terminate are conditional on model assumptions --- see notebooks in References. The models necessarily give a highly simplified perspective that does not account for the full complexity of implementing such a strategy. Nonetheless idealised rational incentives serve as a guide that any policy should aim to satisfy.


Fig. 3 and 4 below show the ROI ratios between terminating and selling hardware upon the introduction of an SDM at varying decision dates, and not terminating while maintaining hardware commitment and power prior to the SDMs introduction to the network, shown for the investment conservation and data onboarding conservation regimes, respectively.

<!-- Note that this is shown for SDMs with slopes 1 and 0.285, in both the investment conservation and data onboarding conservation regimes.  -->

<!-- ![](https://hackmd.io/_uploads/SkmjckrAj.png) -->
![](https://hackmd.io/_uploads/S12XEMSAj.png)
*Fig 3. In the investment conservation regime, A) Incentives for individual SPs to terminate sectors sealed 1 year prior to selected decision dates if the larger population of SPs decides to terminate. B) Incentives for individual SPs to terminate sectors sealed 1 year prior to selected decision dates if the larger population of SPs decides to **not** terminate.* 
*SDM slopes of 0.285 and 1 are shown in blue and orange lines, respectively. Termination fees are capped at 90 days of Expected Block Rewards.*  

<!-- ![](https://hackmd.io/_uploads/B1ajqJSRj.png) -->
![](https://hackmd.io/_uploads/BkJ8VMS0i.png)
*Fig 4. In the data onboarding conservation regime, A) Incentives for individual SPs to terminate sectors sealed 1 year prior to selected decision dates if the larger population of SPs decides to terminate. B) Incentives for individual SPs to terminate sectors sealed 1 year prior to selected decision dates if the larger population of SPs decides to **not** terminate.* 
*SDM slopes of 0.285 and 1 are shown in blue and orange lines, respectively. Termination fees are capped at 90 days of Expected Block Rewards.*  

We observe incentives to terminate and consolidate power are higher in the data conservation regime than the FIL conserved regime, and markedly higher when the SDM slope increases from 0.285 to 1. It is important to note that raising the termination fee cap from 90 days of Expected Block Reward (as is currently specified in the protocol), to 180 days or 270 days of Expected Block Reward, could likely significantly lowers incentives to terminate and consolidate power. Fig 5 and 6 below that repeats the termination analysis above, but triples the termination fee cap to 270 days of Expected Block Reward. 

<!-- ![](https://hackmd.io/_uploads/HkvxikH0o.png) -->
![](https://hackmd.io/_uploads/r1xvEfBRs.png)
*Fig 5. In the investment conservation regime, A) Incentives for individual SPs to terminate sectors sealed 1 year prior to selected decision dates if the larger population of SPs decides to terminate. B) Incentives for individual SPs to terminate sectors sealed 1 year prior to selected decision dates if the larger population of SPs decides to **not** terminate.* 
*SDM slopes of 0.285 and 1 are shown in blue and orange lines, respectively. Termination fees are capped at 270 days of Expected Block Rewards.*

<!-- ![](https://hackmd.io/_uploads/ryqliyrRs.png) -->
![](https://hackmd.io/_uploads/Sk6vEMH0o.png)
*Fig 6. In the data onboarding conservation regime, A) Incentives for individual SPs to terminate sectors sealed 1 year prior to selected decision dates if the larger population of SPs decides to terminate. B) Incentives for individual SPs to terminate sectors sealed 1 year prior to selected decision dates if the larger population of SPs decides to **not** terminate.* 
*SDM slopes of 0.285 and 1 are shown in blue and orange lines, respectively. Termination fees are capped at 270 days of Expected Block Rewards.* 

## Suggested Modifications to FIP-0056

On the basis of considering more extreme scenarios, we suggest a maximum multiplier of 2x for 5Y sectors, which corresponds to an SDM slope of 0.285. The softer SDM slope creates less incentives to terminate (Fig 3) as well as a smaller potential network RBP drop (Fig 1) when compared with a stronger slope, while still incentivizing longer term sectors, supporting supply dynamics, and helping to fulfill Filecoin's mission of being a long-term and robust foundation for humanity's data. 


## References
The models used for this report are open-source and available on `protocol/CryptoEconLab` and `protocol/filecoin-mecha-twin` repositories on GitHub. The specific notebooks which were used are:
1. [Network Econometrics Simulation under Investment Conservation and Data Onboarding Conservation](https://github.com/protocol/CryptoEconLab/blob/fil_conservation/notebooks/fil_conserved/sweep_sdm_multiplier.ipynb)
2. [Incentives To Terminate Analysis](https://github.com/protocol/CryptoEconLab/blob/fil_conservation/notebooks/sector_duration_multiplier/SP_Termination_SDMv2_Regimes.ipynb)
3. [mechaFIL](https://github.com/protocol/filecoin-mecha-twin)

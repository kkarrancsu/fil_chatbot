---
title: Sector duration multiplier all sectors vs new sectors analysis
tags: Econ monitor
---

# Sector duration multiplier ‘all sectors’ vs ‘new sectors’ analysis

Authors: {Vik, Kiran, Tom} @ CryptoEconLab


## Summary

In the sector duration multiplier (SDM) proposal, an important design choice is to decide whether all sectors (renewals and new onboards) or only new sectors will receive SDM. The choice will impact: 



* Initial pledge per sector onboarded
* A storage provider’s FIL-denominated ROI
* Accessibility for deal power compared to committed-capacity power
* Potential for induced termination incentives
* Potential for induced macro and micro-economic shocks
* Medium-term macroeconomic trajectories for circulating and locked supply.

To better understand these impacts, we simulate Filecoin’s economy across different scenarios. The analysis indicates that:


* ‘New sectors only’ has the weakest effect on macro and lowest scope for shocks. 
* The ‘all sectors’ choice has stronger supply effects and more scope for QAP to grow faster. The flipside is increased potential to incentivise early termination to re-onboard in specific scenarios.
* In general a rush of terminations to re-onboard, which could happen in the ‘new sectors only’ case, should be mitigated by a number of factors. But in supply terms, because this would drop QAP and increase circulating supply, pushing up Initial Pledge for future re-onboarding.
* Incentives to terminate can occur for individual sector choices  under specific network conditions in both ‘all sectors’ or ‘new sectors’ cases. In scenarios with high QAP growth, there is more potential for short duration sectors to terminate-to-re-onboard. However sectors with typical commitment durations — similar to the network average — don’t experience incentives to terminate and re-onboard in general.
* Any SDM implementation is better for improving stability than no SDM. But between the two choices, ‘all sectors’ is likely better, based on its scope for a stronger response, balanced against other considerations discussed here.

In a broader context, SDM provides another dimension for the network to incentivise what it values. The policy is expected to enable QAP growth and bias the network towards long-term stability. However, any SDM policy is ultimately an enabling factor and can only complement the network’s fundamentals, which are growth in client demand and investment interests supported by storage providers alongside technical developments to boost the network’s utility.

## Analysis

A [mechanistic model](https://github.com/protocol/filecoin-mecha-twin/tree/sdm_take2_analysis) of Filecoin’s economy is used to compare four scenario types which capture the bounds of expected behaviour from a SDM policy:



* **All sectors:** all sectors may gain SDM, but there’s no instantaneous extension of CC sectors to do so. 
* **All sectors CC-jump:** all sectors may gain SDM and CC power extends instantaeously to gain the SDM multiplier at policy introduction date.
* **New sectors:** only newly onboarded sectors are allowed to gain SDM.
* **New sectors CC-jump:** only newly onboarded sectors gain SDM, and CC sectors terminate early in order to re-onboard to gain the SDM multiplier. 

For each scenario, SP incentives and supply economics are computed for average durations, and therefore average SDMs, of 1, 2, 3, 4 and 5 years.



![](https://hackmd.io/_uploads/HyvJKbXci.png)
Figure 1. A) The Circulating Supply defined as _Minted + Vested - Locked - Burned_. B) The aggregate number Locked Filecoin from different pledges and rewards. C) The ratio of Locked to Circulating Supply. D) FIL minted per day, E) Network quality adjusted power (QAP) trajectories. F) Network Raw Byte Power (RBP) trajectories. G) Initial Pledge per 32 GiB sector onboarded. H) The 1 year ROI, before gas and capex/opex. The dotted line (15-Jan-2023) indicates when SDM is introduced. The average new duration is 3y, with 3x SDM. Other durations are shown in Appendix/Notebooks. In the New sectors CC-jump scenarios,  committed capacity (CC) power is terminated and re-onboarded on the same day the SDM is introduced. 

**Locked and circulating supply**

The ‘new sectors’ only scenario has the weakest effect in terms of locked and circulating supply, with slowest growth in QAP. This is shown by the green line in Figures 1A-F.

The ‘all sectors’ scenario enables more of current network power to take up the SDM, and can lead to faster QAP growth and changes to supply than ‘new sectors’. Although the extent to which ‘all sectors’ scenario can prevent a decline in the raw byte size of the network is not quantified, directionally, this expectation will in turn support a higher minting rate through baseline minting.

In the scenario of ‘all sectors CC-jump’, in which CC power scheduled to renew opts to extend earlier, this leads to faster growth in QAP, with minimal difference to locked circulating supply, compared to if CC power is extending gradually at the scheduled renewal time.

The scenario that leads to the largest change to locked and circulating supply is when SDM is restricted to new sectors only, but CC terminates in order to re-onboard with a SDM.  This is because the wave of terminations drops QAP and increases supply. In turn, Initial Pledge spikes, and upon re-onboarding locked supply increases substantially. Such an extreme scenario as this is considered unlikely as a rational choice due to the disincentive the spike in Initial Pledge creates for re-onboarding. On the other hand, the ‘new sectors’ scenario does create more uncertainty for the network, since if termination did occur it opens the possibility of terminated sectors not returning to the network.  

**Initial Pledges and FIL-denominated ROI**

Across all scenarios Initial Pledges decrease in the medium-term following the introduction of SDM, see Figure 1G. 

This happens because the main contribution to the Initial Pledge is the Consensus Pledge, which decreases proportionally to circulating supply and inversely with QAP. Note, an important assumption is that QAP grows, through the network seeing an increase in average sector durations while maintaining renewal, expiration, FIL+ rate and raw byte onboarding trends similar to today. These assumptions are discussed further in the Assumption and Limitations section, and further scenarios are given in the Appendix and Notebooks.

In general the declines observed in Initial Pledges are more pronounced when QAP growth is faster and larger. This results in the ‘all sectors CC-jump’ and ‘new sectors CC-jump’ scenarios seeing the largest and fastest decreases.

The decrease in pledge could contribute to an incentive to delay onboarding. Based on estimates of ROI — see Figure 1H — this appears unlikely.

Across each simulated scenario FIL-denominated ROI is broadly stable and not substantially different to the no-SDM scenario in the short to medium term. Longer term predictions have limited value and should be viewed with scepticism. 

It is emphasised that future ROI trends are conditional on FIL+, renewal rate and raw byte onboarding trends. How ROI can change across these was explored in more detail in the [baseline crossing report](https://hackmd.io/Ny_e0UkXRGCTDA0oT3me2A).

**Potential for shocks**

We assess the impact of shocks to the macro supply and individual sector economics. In the ‘all sectors’ scenario, if a large proportion of SPs providing CC power extend on the same day, this could lead to future jumps in power and locked supply. A schematic illustrating synchronisation of power that can potentially lead to future jumps is shown in Figure 2. A similar shock can occur in the ‘new sectors’ scenario if SPs terminate and re-onboard CC power in a coordinated fashion.  The macro effects to Filecoin’s economy in these cases are illustrated in the jump scenarios in Figure 1 (red and purple).

The jump scenarios are not expected to be detrimental to the network for the following reasons:



* The jump scenarios are unlikely because they rely on a concentration of commitments around a single value, for example 3 years, when in reality there will be a variation in times to expiration.
* Any remaining power and supply shocks from expiring sectors falling into lockstep may be smoothed out by early terminations, variation in renewal rate, and the assumption of continued growth in future deal onboarding.
* The instantaneous extension shock scenario modelled, which is extreme in how it is executed, leads to moderate changes in sector economics, see Figure 1. The coordinated early termination-to-re-onboard scenario generates a stronger response, however, this appears to be self limiting through its effects on Initial Pledge and ROI.

![](https://hackmd.io/_uploads/HyMUYWX5i.png)

Figure 2. Schematic illustrating how waves of expiration and renewal could become synchronised through coordinated early extension. The extent to which this could occur is reduced by several factors.



Another important consideration around shocks is the termination fee. Enabling a power multiplier has the potential in the medium term to lead to less stability through lesser relative cost of intentional termination. On this point the current termination fee was set early in the design of the network in the context of 6 month sectors. Its reassessment is overdue, and is part of a broader theme of the cryptoeconomic network parameters needing to change as the network evolves to ensure alignment with network goals. Aligning termination fee incentives should be expected to land in a subsequent proposal if the SDM policy is adopted. 

**Accessibility**

The ‘all sectors’ and ‘new sectors’ scenarios mean differences in SDM accessibility for current CC and deal power, since currently, deals cannot be extended.

In terms of the impact of the difference in accessibility, from the perspective of current network power, ‘all sectors’ enables CC extension, which can lower FIL-denominated ROI for current power. This is illustrated in Figure 1H. 

From the perspective of future onboarded power, growth in QAP scales both pledges and rewards, so while future Initial Pledges can decrease, FIL-denominated ROI is broadly unaffected.

From the network’s perspective, its goal is to build capacity then translate this to usefully stored data. The ‘all sectors’ choice distinguishes accessibility but may better support the raw byte network than ‘new sectors’ choice. The importance of this is encoded in the baseline storage target function. Its maintenance should be viewed in cooperative rather than zero-sum competition terms. This is expressed through increases in baseline minting that can occur with increases in raw byte power. 

**Incentives to terminate early**

If power increases through introduction of SDM this can change Initial Pledges and potentially create incentives to terminate and re-onboard compared to maintaining a sector.

This can arise across each of the 4 simulated macro scenarios under certain specific conditions.  For example, it can occur for an individual sector with a 1 year commitment if the average network duration quickly increases due QAP growth leading to decreased Initial Pledge. See Figure 3 for an example.


<!-- ![](https://hackmd.io/_uploads/Bymqt-Q9j.png) -->
![](https://hackmd.io/_uploads/H1G3oXm5o.png)

Figure 3. Incentives to terminate early and re-onboard when the average network duration is 3 years, and SDM policy is implemented in mid January 2023. Green (>0) means no incentive to terminate early to re-onboard.

This effect is more pronounced the greater the difference between typical sector duration and the short commitment, but the impact is mitigated by it requiring substantial deviation from what is the typical network duration. 

Furthermore, SDM acts to reduce the marginal costs contribution to ROI leading to incentives for longer commitments. The proportion of sectors committing for the shortest durations for this mechanism to be relevant is therefore expected to be low. 

Incentives to terminate also increase with termination decision date. This can be considered partially addressed by the assumption that a proposal in the near future will adapt termination fees if the SDM policy is implemented.

Finally, while termination to re-onboard is wasteful and misaligned, its impact is likely to be limited, as illustrated by the extreme termination scenarios shown in Figure 1.

A more extensive range of scenarios across examining different sector termination dates, sector SDMs, average network SDM, and sealing dates from different perspectives across each of the 4 macro scenarios is given in this [Notebook](https://github.com/protocol/CryptoEconLab-private/blob/qm-expansion/notebooks/quality_multiplier_expansion/all_vs_new_sectors/SP_Micro_Termination_Model.ipynb).


## Assumptions and Limitations

Forecast trajectories and estimates are not predictions of what will happen. They are based on idealised scenarios, and the exploration should be treated as a tool to show relative differences and build design-space understanding. All interpretations of the analysis must be conditioned on the assumptions given below. All absolute value predictions should be interpreted with caution, especially far into the future. None of the analysis comes with any guarantees but the underlying model is open-source and available to be reviewed and improved.

**Termination incentives model assumptions**



* **Assumption 1:** There’s no time-discounting of future risk or rewards in the termination incentives model.
* **Assumption 2:** Operational costs associated with resealing are excluded, overweighting the potential for resealing. This assumption can be adapted in the termination incentives notebook.
* **Assumption 3:** The gas cost to reseal a 32 GiB sector corresponds to values on [filscout](https://www.filscout.com/us) on the dates the analysis was done (28-Dec-2022 to 3-Jan-2023). This value, 0.0485 FIL/32 GiB sector, is likely a lower bound on gas usage in event of substantial termination-to-re-onboard. As with Assumption 2, this assumption therefore leads to the analysis overweighting the potential for termination-to-re-onboard occurring.

**Supply model and derived quantities assumptions**



* **Assumption 1:** the concept of sector duration and how it may change with a SDM enters the model as a single parameter referred to as average duration. In reality a distribution of sector durations exists now and a different distribution will exist in a post SDM future.
* **Assumption 2:** future protocol changes are out of scope. Example: termination fees may increase in the future but this not accounted for in this analysis.
* **Assumption 3:** Introducing a SDM is modelled through a change in average sector duration across the network, and this change happens on top of the forecasted FIL+ rate, raw byte power growth and renewal rate. This means we are assuming the size of Filecoin’s economy is not conserved, it has the potential to increase through longer average durations increasing network QAP.
* **Assumption 4:** The mechanistic model is dependent on three unstructured input parameters: FIL+ Rate, Renewal Rate and Raw Byte Onboarding Power. These parameters are forecast using traditional Bayesian time-series methods. In effect this is an assumption that the historical trend will continue — that the FIL+ Rate will continue to increase, Renewal Rate will remain around 60%, and Raw Byte Onboarding will oscillate around a low value of 2.5TiB/day.
* **Assumption 5:** Supply simulations and derived quantities such as Initial Pledge and ROI are based on the median time-varying trajectories of the underlying parameters. 
* **Assumption 6:** Gas differs substantially across batching. Consequently ROI in Figure 1 is simply displayed pre-gas for the purposes of relative scenario comparison.
* **Assumption 7:** Power is aggregated with daily granularity. 
* **Assumption 8:** Sector duration distributions are approximated with a single fixed duration in power and locking models.
* **Assumption 9:** The jump scenarios are extreme limits: extension occurs on the same date the SDM is introduced. Termination occurs the same day, and re-onboarding gradually over a period of 60 days. Such sharp changes are implausible but useful to understand and to provide bounds on what could happen.


## Methods

**Macro supply models and derived quantities**

![](https://hackmd.io/_uploads/SkevvEXco.png)

Figure 4. Unstructured input parameters of FIL+ rate of newly onboarded power, renewal rate, and raw byte onboarding are forecast using a Bayesian time series model. 

In the ‘All sectors CC-jump’ and ‘New sectors CC-jump’ models, eligible CC power immediately extends or terminates then extends the next day respectively. Eligible means CC power within a 1 year window following the SDM introduction date. 

The jump scenarios are extreme limits: extension occurs on the same date the SDM is introduced. Termination occurs the same day, and re-onboards gradually over the next 60 days. Such sharp changes are implausible but useful in their simplicity to provide bounds. 

For more details see referenced notebooks.


## References



* [Notebook for macro model and derived quantities](https://github.com/protocol/CryptoEconLab/blob/baseline-crossing-updated/notebooks/sector_duration_multiplier/sdm_analysis.ipynb)
* [Notebook for incentives to terminate](https://github.com/protocol/CryptoEconLab-private/blob/qm-expansion/notebooks/quality_multiplier_expansion/all_vs_new_sectors/SP_Micro_Termination_Model.ipynb)
* [FIP Discussion 554](https://github.com/filecoin-project/FIPs/discussions/554)
* [FIP draft (WIP)](https://github.com/filecoin-project/FIPs/pull/571)
* [Baseline crossing report: timing and impact of crossing the baseline storage target from above](https://hackmd.io/Ny_e0UkXRGCTDA0oT3me2A)


## Appendix

Panels across a range of macro supply scenarios for average duration between 1 and 5 years:


## 

![](https://hackmd.io/_uploads/HJRDUQmqj.png)

Figure 5. A) The Circulating Supply defined as Minted + Vested - Locked - Burned. B) The aggregate number Locked Filecoin from different pledges and rewards. C) The ratio of Locked to Circulating Supply. D) FIL minted per day, E) Network quality adjusted power (QAP) trajectories. F) Network Raw Byte Power (RBP) trajectories. G) Initial Pledge per 32 GiB sector onboarded. H) The 1 year ROI, before gas and capex/opex. TheIn each panel the dotted line (15-Jan-2023) indicates when SDM is introduced on 15-Jan-2023. The average new duration is 1y, with 1x SDM. Other durations are shown in Appendix/Notebooks. In the New sectors CC-jump scenarios, where CC committed capacity (CC) power is terminated and re-onboarded, this happens on the same day the SDM is introduced.



![](https://hackmd.io/_uploads/BJD_IQX9i.png)

Figure 6. A) The Circulating Supply defined as Minted + Vested - Locked - Burned. B) The aggregate number Locked Filecoin from different pledges and rewards. C) The ratio of Locked to Circulating Supply. D) FIL minted per day, E) Network quality adjusted power (QAP) trajectories. F) Network Raw Byte Power (RBP) trajectories. G) Initial Pledge per 32 GiB sector onboarded. H) The 1 year ROI, before gas and capex/opex. TheIn each panel the dotted line (15-Jan-2023) indicates when SDM is introduced on 15-Jan-2023. The average new duration is 2y, with 2x SDM. Other durations are shown in Appendix/Notebooks. In the New sectors CC-jump scenarios, where CC committed capacity (CC) power is terminated and re-onboarded, this happens on the same day the SDM is introduced.


![](https://hackmd.io/_uploads/BypO8QX5s.png)

Figure 7. A) The Circulating Supply defined as Minted + Vested - Locked - Burned. B) The aggregate number Locked Filecoin from different pledges and rewards. C) The ratio of Locked to Circulating Supply. D) FIL minted per day, E) Network quality adjusted power (QAP) trajectories. F) Network Raw Byte Power (RBP) trajectories. G) Initial Pledge per 32 GiB sector onboarded. H) The 1 year ROI, before gas and capex/opex. TheIn each panel the dotted line (15-Jan-2023) indicates when SDM is introduced on 15-Jan-2023. The average new duration is 4y, with 4x SDM. Other durations are shown in Appendix/Notebooks. In the New sectors CC-jump scenarios, where CC committed capacity (CC) power is terminated and re-onboarded, this happens on the same day the SDM is introduced.


![](https://hackmd.io/_uploads/r1fFU779j.png)

Figure 8. A) The Circulating Supply defined as Minted + Vested - Locked - Burned. B) The aggregate number Locked Filecoin from different pledges and rewards. C) The ratio of Locked to Circulating Supply. D) FIL minted per day, E) Network quality adjusted power (QAP) trajectories. F) Network Raw Byte Power (RBP) trajectories. G) Initial Pledge per 32 GiB sector onboarded. H) The 1 year ROI, before gas and capex/opex. TheIn each panel the dotted line (15-Jan-2023) indicates when SDM is introduced on 15-Jan-2023. The average new duration is 5y, with 5x SDM. Other durations are shown in Appendix/Notebooks. In the New sectors CC-jump scenarios, where CC committed capacity (CC) power is terminated and re-onboarded, this happens on the same day the SDM is introduced.
---
title: Filecoin Minting
tags: Econ monitor
---

**Authors**: {Kiran, Vik, Tom} @ CryptoEconLab

## Summary
- Using Monte-Carlo methods for forecasting, if current trends in onboarding and renewal rate continue, we expect total minting to approach simple minting on 2026-03-18 (median forecast), with a 90% credible interval between 2024-12-01 and 2028-02-20.
- This is an expected consequence of Filecoin’s minting design, due to raw-byte power being less than the baseline, and due to exponential decay of simple minting. 
- Using counterfactual scenarios for Raw Byte Onboarding and Renewal Rate trajectories, we observe that as these scale up, the date on which total minting approaches simple minting is extended further into the future. For example:
    - For Raw Byte Onboarding at 35 PiB/day and renewal rates of 55%, total minting approaches simple minting around January of 2027. For onboarding and renewal rates higher than this, total minting remains sufficiently greater than simple minting.
    - For Raw Byte Onboarding at 3PiB/day and Renewal Rates at 5%, total minting approaching simple minting around August of 2024.



## 1. Introduction
In this report, we recap the details of Filecoin’s minting and address the following questions: 
1. What is Filecoin’s forecasted minting rate?
2. Will total minting reach simple minting? 

We use Monte-Carlo methods to forecast minting rates for the next five years. Using the forecasts, we show that if current trends in onboarding and renewal rates continue, the median estimate when total minting reaches simple minting is on 2026-03-18, with quantiles Q5 and Q95 falling on 2024-12-10 and 2028-02-20, respectively. We additionally run ten counterfactual scenarios to gain further insight into how total and simple minting are related. We observe that as raw-byte power and renewal rates are scaled up, the date when total minting will approach simple minting is extended further into the future.


## 2. Filecoin's Minting Model
Filecoin uses a [hybrid minting model]((https://spec.filecoin.io/systems/filecoin_token/minting_model/)) to encourage consistent storage onboarding and investment in long-term storage. 
The hybrid minting model is a combination of simple and baseline minting that aligns block reward emissions with baseline storage targets. This enables the Filecoin network to reward storage providers proportional to the utility (i.e. storage power) they offer to the network. A visual explanation of those incentives are described in [this post](https://medium.com/block-science/a-cadcad-interactive-calculator-to-explore-minting-scenarios-in-filecoin-284009a2e941) by BlockScience on Minting Scenarios.

___

| ![](https://hackmd.io/_uploads/ByMFo5mPs.png) | ![](https://hackmd.io/_uploads/H1wtscmvs.png) |
| -------- | -------- |
| *Network Power* | *FIL on FIL profitability vs benchmark* |


*Fig 1. A counter-factual comparison on Storage Mining Rewards according to distinct scenarios (red: what if baseline was not activated, green: what if RBP is always equal to baseline). The Higher the Mining Utility, the more FIL-on-FIL profitable it is to participate on the network. Baseline Minting essentialy creates a Macro "savings account" for the future without reducing the individual rewards. [Source](https://medium.com/block-science/a-cadcad-interactive-calculator-to-explore-minting-scenarios-in-filecoin-284009a2e941)*

___

In the hybrid minting model, a portion of minting rewards come from simple exponential decay (simple minting) and the remainder from network baseline minting. The network disburses maximum rewards when network RBP exceeds the baseline storage target, a key performance indicator (KPI). The baseline storage capacity is currently targeted to double network storage capacity annually.


![](https://hackmd.io/_uploads/ry4X2xYu3.png)
*Fig 2. Network’s total raw byte capacity in relation to the network’s baseline power KPI target since network launch. Source*

## 3. Forecasting Minting Rates

To forecast the range of possible minting rate trajectories, we use a Monte-Carlo approach to forecasting the range of inputs that affect minting, namely the raw byte onboarding rate and the renewal rate. Raw Byte onboarding power and sector renewal rate are modeled as a Bayesian time series using a [Seasonal with Global trend model](https://cran.r-project.org/web/packages/Rlgt/vignettes/GT_models.html) trained on historical data to create forecasts of these inputs over the simulation window. The forecasting uses the previous six months of onboarding and renewal trends to train the model. Daily forecasts of Raw Byte power and renewal rate are computed using 4 MCMC chains, with 5000 samples from each chain and a warmup of 5000 samples. Further details of this modeling approach are detailed [here](https://hackmd.io/@cryptoecon/BkytBgbIs?type=view#Method-1-Markov-Chain-Monte-Carlo-Simulations-for-Baseline-Crossing).

Fig. 3A, 3B, and 3C show the forecasted onboarding, renewal rates, and computed network RBP forecast, respectively. The dark line indicates the median prediction, and the shaded bounds show the respective quantiles.

![](https://hackmd.io/_uploads/BJ6FS-jKn.png)
*Fig 3: A) Forecasted raw byte onboarding, B) and renewal rates, and C) corresponding network RBP forecast.*

These forecasts are conditional on current trends in Raw Byte Onboarding and Renewal Rate continuing. However, this is not guaranteed and depends on many factors, such as the external macroeconomic environment, future cost reductions, and the actions and entry of the current and new network participants. 

Using the Network RBP, we apply the [network equations](https://spec.filecoin.io/#section-systems.filecoin_token.block_reward_minting.baseline-minting) to compute the minting rate. Fig. 4A shows the forecasted trajectories for total and simple minting trajectories. For each realization, we calculate the first date when the total block reward is within 2% of the block rewards due to simple minting. Fig. 4B shows a histogram of the crossing dates. These simulations show that if current onboarding and renewal rate trends continue, the median estimate when total minting approaches simple minting is on 2026-03-18, with quantiles Q5 and Q95 falling on 2024-12-01 and 2028-02-20, respectively.

![](https://hackmd.io/_uploads/r1OG8ZiFh.png)

*Fig 4: A) Minting forecasts and deterministic simple minting projection. B)  Distribution of the hitting time, when total minting crosses the threshold of being with 2% of simple minting.*

Beyond probabilistic trend-following forecasts, it is also possible to see a regime shift in onboarding, for example, lifting raw byte power above the baseline and increasing baseline minting rate. A range of possible optimistic and pessimistic scenarios are set out in the following section. 

## 4. Counterfactual Scenarios
We examined ten counterfactual scenarios that capture potential future SP behavior in the Filecoin network to gain further insight into the minting rate. Each scenario contains a different combination of exponential growth or decay of raw-byte power and renewal rate to a defined percentage of their historical maximum (ranging from 5% to 95%) 180 days after the simulation start. 

Fig. 5A and B show the considered raw-byte onboarding power and renewal rates. Fig. 5C and D show the corresponding minting rate changes. As onboardings and renewals are scaled up, the date when total minting approaches simple minting extends to the future.

![](https://hackmd.io/_uploads/SJXmYe8s2.png)
*Fig 5: A) Input trajectories for raw-byte power, B) input trajectories for renewal rate, C) Block Reward forecasts for counterfactual scenarios, and D) Expected date when total minting will approach simple minting to within 2% as a function of the inputs.* 


## 5. Conclusion
Our analysis indicates that Filecoin’s overall minting will be well above simple minting in the near future. If current onboarding and renewal rate trends continue, we expect total minting to approach simple minting on 2026-03-18 (median forecast), with a 90% credible interval between 2024-12-01 and 2028-02-20. In the most pessimistic counterfactual scenario, the earliest date when total minting may approach simple minting is late 2024. Positive changes in the macroeconomic between now and late 2024 can occur, leading to that date being pushed further into the future.  For example, if Raw Byte onboarding and Renewal Rate approach 55% of their historical maximum (35 PiB/day and 55%, respectively), total minting approaches within 2% of simple minting around January of 2027.


## 6. References
* [Baseline Crossing Analysis](https://hackmd.io/@cryptoecon/BkytBgbIs?type=view)
* [MCMC Forecasting Notebook](https://github.com/protocol/CryptoEconLab/blob/pledge_base_analysis/notebooks/simple_mint/minting_forecast_mcmc.ipynb)
* [Counterfactuals Notebook](https://github.com/protocol/CryptoEconLab/blob/pledge_base_analysis/notebooks/simple_mint/minting_forecast_counterfactuals.ipynb)
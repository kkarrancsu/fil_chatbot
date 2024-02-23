---
title: Jan 2024 - Filecoin SitRep
tags: Econ monitor
---

**Authors**: CryptoEconLab

## Summary
- Network Quality Adjusted Power (QAP) dropped below the baseline on Dec 17th, 2023.
- For QAP to catch back up to the baseline in 1Y, it will require a minimum of $800M of investment into the network, assuming a 5-USD/FIL exchange rate.
- In the regime where QAP is less than the baseline, the consensus pledge required to onboard power is on a decreasing trajectory, which increases Fil-on-Fil returns (FoFR) and incentivizes storage providers to increase data onboarding.
- However, if decreasing pledge is combined with low onboarding, this will result in lower locked FIL, which is critical for consensus security. This should be carefully monitored in the upcoming months, and any bottlenecks to onboarding should be removed to enable the network to maximize investment flow that can be driven by the higher Fil-on-Fil returns.


## Introduction
The network’s QAP (Quality Adjusted Power) crossed the network baseline on Dec 17th, 2023. Considering this milestone, we provide a situational report of the Filecoin network in this report. Given the current state, we begin by forecasting what the network state will be in one year. This is done using two methods:
1. Using forecast trends
2. Developing some possible scenarios of SP onboarding behavior.

We find that using both approaches, the network will trend toward shrinkage.

Next, we examine the onboarding necessary for the network to catch up to the baseline in one year and compute the investment needed to achieve that level of onboarding. We additionally examine whether there are incentives to delay onboarding. Action items for network maintainers are then discussed in the closing remarks. 



## Simulations

### MCMC

In this section, we describe Markov Chain Monte Carlo (MCMC) techniques to forecast the state of the network, given the current state of the network.  Using 120 days of historical data, we first create forecasts of possible onboarding, renewal rate, and Fil+ rate trajectories.  This is shown in Fig. 1, below.

We observe that the median forecasted onboarding rate and Fil+ rate is on a decreasing trend, while the median renewal rate is on a slightly increasing trend. The 25th and 75th quantiles are shown in lighter shades, while the black trajectory represents the historical data.

For each of these trajectories, we then simulate the future state of the network using [MechaFIL](https://github.com/celtd/mechafil-jax), a digital twin of the Filecoin network. Fig 2-4 show the forecasted power, supply, and onboarding metrics.

If current trends continue, we observe from Fig 2 that QAP will diverge from the baseline. Additionally, the L/CS trajectory, an important quantity when assessing the consensus security of the network, is also on a downward trend. These decreases in TVL and power also result in the pledge decreasing, which results in an increased projected Fil-on-Fil returns (FoFR).  This is a resilient property of the network that is automatically activated to encourage more investment into the network.

![mcmc_inputs](https://hackmd.io/_uploads/Sk5VoOEF6.png)
*Fig 1: Possible trajectories for Onboarding, Renewal, and Fil+, given 120 days of historical data.*

![mcmc_power](https://hackmd.io/_uploads/rJsTc_4ta.png)
*Fig 2: Forecasted network power.  The median forecast is shown in dark blue, while the 25th-75th quantile forecast is shown in light blue.*

![mcmc_supply](https://hackmd.io/_uploads/By3W30IYa.png)
*Fig 3: Forecasted supply metrics. The median forecast is shown in dark blue, while the 25th-75th quantile forecast is shown in light blue.*

![mcmc_onboarding](https://hackmd.io/_uploads/BJHRquVtT.png)
*Fig 4: Forecasted Fil-on-Fil returns. The median forecast is shown in dark blue, while the 25th-75th quantile forecast is shown in light blue.*

### Scenario Exploration
In this section, we explore several possible scenarios for onboarding, renewal rate, and Fil+ rate. We examine what the network state would look like if each of those were scaled by 80%, 100%, or 120% of their historical medians using 120 days of history. This is an alternative way to explore future network state to MCMC. 

Fig 5-7 show the relevant power, supply, and onboarding metrics. The status-quo scenario, where the historical median is continued as is, is shown in dark black, while scaled versions of RBP, RR, and FPR are shown and indicated in their respective legends. In Fig 5, we observe that Network RBP and Minting Rate only depend on RBP and RR, but not FPR. Fig 5B shows the QAP trajectory. A 20% increase in FIL+ rate, Renewal Rate, and onboarding rate than the historical median over the past 120 days results in an upward trajectory for QAP, locked, and a stable L/CS (for 1Y into the future). However, this 20% increase in all onboarding engagement (RBP, RR, FPR) still results in QAP being below the baseline. Thus, all scenarios result in decreased pledge and increased FoFR.

Overall, these scenarios mimic the network state forecast using MCMC.

![scenarios_power](https://hackmd.io/_uploads/SJDYsO4Fa.png)
*Fig 5: Trajectories for RBP, QAP, and Minting rate for different scaling factors of RBP, RR, and FPR, as identified in the legend.*

![scenarios_supply](https://hackmd.io/_uploads/S10Ksu4Yp.png)
*Fig 6: Trajectories for Locked, Circulating Supply, and L/CS for different scaling factors of RBP, RR, and FPR, as identified in the legend.*

![scenarios_onboarding](https://hackmd.io/_uploads/H1bcjdNKa.png)
*Fig 7: Trajectories for Pledge and FoFR for different scaling factors of RBP, RR, and FPR as identified in the legend.*

## Discussion

### Onboarding & Investment Needed to Catch up to Baseline
In the previous section, we observed that a 20% increase in onboarding, renewals, and Fil+ rate would not be sufficient for QAP to catch up to the baseline. Here, we explore scenarios that will result in QAP reaching baseline by the end of 2024. 

We simulate multiple scenarios of RBP, with multiplicative factor increases for renewal rate and Fil+ rate. For each scenario, we compare the QAP trajectories to the baseline and the pledge.  Additionally, under the assumption of 5 USD/FIL, we compute the investment needed to onboard the defined amount of power.  These trajectories are shown below in Fig 8. Fig 9 shows the total investment needed to sustain the onboarding, renewal rate factor, and Fil+ rate factor shown.  An X in the heatmap indicates that that particular configuration reaches or exceeds the baseline in 1Y.

Fig 8 and 9 indicate that if the historical renewal rates and Fil+ rates are continued, then 12 PiB/day of onboarding is needed to catch up to baseline.  If Fil+ rate is increased but renewals stay roughly the same, then 10 PiB/day is sufficient.  Fig 9 shows the total amount of investment needed to achieve this onboarding trajectory.  The minimum value is close to 800M of USD, while other trajectories are more expensive. The current TVL of Filecoin at an exchange rate of 5USD/FIL is ~880M USD. Since the baseline doubles every year, it seems reasonable that an additional 800M USD of investment is needed to achieve the exponential growth that is necessary for QAP to catch back up to the baseline.

![investment](https://hackmd.io/_uploads/HJE0s_VYp.png)
*Fig 8: Required Onboarding for network power to cross baseline growth target from below. Daily USD Investment assumes a FIL/USD exchange rate of 1FIL/5USD. Fil Plus Rate and Renewal Rate are our median estimate based on a 120 day lookback period (95.44% and 58.47%, respectively).*

![investment_total](https://hackmd.io/_uploads/ryXUh0IKa.png)
*Fig 9: Required USD investment for network power to cross baseline growth target from below/. Daily USD Investment assumes a FIL/USD exchange rate of 1FIL/5USD.*


## Conclusions
In this document, we explored the current state of the Filecoin network.  We find that the current trajectory of the network is towards shrinkage. For Network QAP to grow and catch back up to the baseline target, ~800M of investment will need to flow into the network. Investment flow into the network is the current primary bottleneck.  However, Filecoin was designed to be robust to downturns, and its anti-fragile mechanism of increasing FoFR to attract further investment is starting to be activated. However, to properly take advantage of this, bottlenecks to QAP growth should be addressed.

Additionally, the Locked and Locked/Circulating Supply trajectories should be monitored, since if the network continues to shrink these will reach levels that may threaten network consensus security. 

To attract more investment, the network should continue to build on its recent engineering advances, such as Direct Data Onboarding (DDO) which reduces costs to onboard power onto the network and enables it to onboard data at a higher throughput. Filecoin can also consider removing the minting cap on DataCap allocation. Although DataCap is not strictly a bottleneck to growth, it can become one if DataCap requests ramp up due to changing macroeconomic conditions. Relatedly, while DataCap allocation can become an issue, the network should devise new solutions to Fil+ abuse in a more scalable manner, to achieve the vision of Filecoin.

Additionally, the network should invest in new technologies that can reduce barriers to entry into the network. These can range from UX upgrades to more economic factors, such as innovations that reduce the capital needed to participate in the network. 

## References
- [RBP Baseline Crossing](https://hackmd.io/@cryptoecon/BkytBgbIs?type=view)
- [QAP Baseline Crossing](https://hackmd.io/@cryptoecon/SkICuaJK2?type=view)
- Simulation notebook

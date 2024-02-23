# Baseline Crossing - Power Forecasting Scenarios

#### Maria Silva, June 2022

###### tags: `Econ monitor`

In this document, we describe the scenarios built to forecast network power for the [Baseline Crossing project](/96OArWoLQvu1HtSnfwgrnQ). In particular, we designed 4 specific scenarios:

* **Base**: a scenario that uses current network stats (as of the end of May 2022) to set all user-defined parameters. The idea is to simulate a case where the network continues to operate as it is doing now. In particular, we assume an amount of new onboardings, FIL+ rates, and renewals equal to the current amounts observed. We also give some sensible estimates for the average sector durations.
* **Fil+ all-in**: a scenario almost equal to the base scenario, but where we assume an increase of Fil+ deals up to a daily total of 5PiB. Note that currently, we are seeing almost 1PiB. The goal is to simulated a case where Fil+ really picks up and leads to more onboardings.
* **Optimistic**: scenario that provides an optimist view of the base scenario. All the user-defined parameters increase when compared with the base scenario, and the Fil+ rate assumes the 5PiB of the Fil+ all-in scenario.
* **Pessimistic**: scenario that provides a pessimistic view of the base scenario. Here, all user-defined parameters decrease. Renewals and onboardings are lower, and sector lengths are the minimum allowed. The Fil+ rate assumes a level of Fil+ onboarding equal to the one we are seeing right now.

In all scenarios, we forecast 4 years (or 1460 days) into the future. We also use the following network state values taken as of May 30st:

* $\textrm{rb_power_zero}$: 16.7 EiB
* $\textrm{qa_power_zero}$: 17.4 EiB
* $\textrm{rb_known_scheduled_expire_vec}$: Extracted from the [Starboard API](https://observable-api-test.starboard.ventures/getdata/sectors_schedule_expiration_full?start=2020-01-01&end=2022-06-30)
* $\textrm{qa_known_scheduled_expire_vec}$: Extracted from the [Starboard API](https://observable-api-test.starboard.ventures/getdata/sectors_schedule_expiration_full?start=2020-01-01&end=2022-06-30)

**Main conclusion:** Looking at the results, crossing the baseline does not seem an immediate concern for the network, which gives us time to study and analyze any potential change to the baseline function. In the base scenario, the network only goes below the baseline after September 2024. Even in the pessimistic scenario, the network only crosses the baseline during July 2023. In other words, the rapid growth Filecoin experienced in 2021 made a nice cushion, which gives us some time to address a baseline crossing event. 


## Base scenario

Network parameters have values equal to the ones observed at the end of May:
* $\textrm{renewal_rate}$: 50%
* $\textrm{rb_onboard_power}$: 27 PiB
* $\textrm{fil_plus_rate}$: 2.9% (800 TiB / $\textrm{rb_onboard_power}$ in TiB)
* $\textrm{duration}$: 1 year (360 days)

![](https://hackmd.io/_uploads/rJNzpNgEo.png)

In this scenario, the baseline crossing event occurs in 2024-09-06.

## Fil+ all-in scenario

Network paramaters assume the base scenario with a daily onboarding of 5PiB FIL+:
* $\textrm{renewal_rate}$: 50% (same as base)
* $\textrm{rb_onboard_power}$: 31 PiB (current power plus a 4 PiB increase in FIL+)
* $\textrm{fil_plus_rate}$: 16.1% (5 PiB / $\textrm{rb_onboard_power}$)
* $\textrm{duration}$: 1 year (360 days)

![](https://hackmd.io/_uploads/rJv5pNeEi.png)

In this scenario, the baseline crossing event occurs in 2024-11-08.


## Optimistic scenario

Network paramaters are higher than the observed:
* $\textrm{renewal_rate}$: 80%
* $\textrm{rb_onboard_power}$: 35 PiB (30% increase)
* $\textrm{fil_plus_rate}$: 14.2% (still maintaining the Fil+ goal -> 5 PiB / $\textrm{rb_onboard_power}$)
* $\textrm{duration}$: 18 months (540 days)

![](https://hackmd.io/_uploads/S1XnT4gNs.png)


In this scenario, the baseline crossing event does not occur within the simulation window.

## Pessimistic scenario

Growth paramaters are lower than the observed:
* $\textrm{renewal_rate}$: 30%
* $\textrm{rb_onboard_power}$: 24 PiB (10% decrease in onboardings)
* $\textrm{fil_plus_rate}$: 3.2% (same value as base -> $800 TiB / $\textrm{rb_onboard_power}$ in TiB$)
* $\textrm{duration}$: 6 months (180 days)


 ![](https://hackmd.io/_uploads/SJiRTEe4s.png)


In this scenario, the baseline crossing event occurs in 2023-07-11.


## References

* [Model code](https://github.com/protocol/CryptoEconLab/blob/main/notebooks/baseline_crossing/power_model_v2.py)
* [Scenario implementation](https://github.com/protocol/CryptoEconLab/blob/main/notebooks/baseline_crossing/power_forecast_v2.ipynb)
* [Model spec](/O6HmAb--SgmxkjLWSpbN_A)



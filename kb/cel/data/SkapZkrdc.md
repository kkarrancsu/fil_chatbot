---
title: Model spec - Network power forecasting v2
tags: Econ models
---

# Model spec - Network power forecasting v2

#### Maria Silva, June 2022

In this document, we describe the methodology and the main assumptions used to create the network power model used in the [Baseline Crossing project](/96OArWoLQvu1HtSnfwgrnQ) and in the duration multiplier proposal ([FIP-0036](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0036.md)).

## Model assumptions

When designing this model, we focus on daily aggregate network dynamics. In order words,  we avoid complex simulations that capture individual miner behavior and, instead, model aggregate network metrics and mechanisms using sensible approximations.

With this in mind, the model has the following assumptions:

* Forecasting is done daily. This means that each forecasting step corresponds to a day and the forecasted power metrics correspond to the value we expect to see at the end of that day.
* We use the current sector states (i.e. known schedule expirations) and we estimate future onboardings and future renewals.
* The daily power onboarded is a constant provided as a tunable parameter. This is a BIG assumption and we will probably want to make the new onboarding a function of time (e.g. have a linear function or a capped liner function). However, for this first deterministic model, having a constant is the easiest approach.
* The sector renewal rate is a constant provided as a tunable parameter.
* Sector duration is a constant provided as a tunable parameter.
* Filecoin Plus sectors have the same renewal rates and sector durations as other sectors. This is something we may want to relax after we do a deeper analysis of renewal rates and sector durations split by sector type.

The model receives the following inputs as parameters:
* $\textrm{renewal_rate}$ (%): sector renewal rate (out of scheduled expiration)
* $\textrm{rb_onboard_power}$ (PiB): raw-byte storage amount to be onboarded on a daily basis
* $\textrm{fil_plus_rate}$ (%): percentage of $\textrm{rb_onboard_power}$ that contains Filcoin Plus deals
* $\textrm{duration}$ (days): duration of thd sectors onboarded/renewed
* $\textrm{forecast_lenght}$ (days): number of days in which to run the simulation

In other words, these are the "nobs" that the user can tweak to create different scenarios of Storage Providers (SPs) behavior.

Besides these parameters, the model receives some inputs from the current state of the network:
* $\textrm{rb_power_zero}$ (PiB): total raw-byte power of the network
* $\textrm{qa_power_zero}$ (PiB): total quality-adjusted power of the network
* $\textrm{rb_known_scheduled_expire_vec}$ (vector of PiB): raw-byte storage power from active sectors expected to expire at each day
* $\textrm{qa_known_scheduled_expire_vec}$ (vector of PiB): raw-byte storage power from active sectors expected to expire at each day

From these inputs, the model derives the raw-byte (RB) power and quality-adjusted (QA) power for each day.


## Notation

Before we detail how the model computes RB and QA power, we need to define the following notation:

* $t$: forecasting step (e.g. $t=0$ is day 0 and $t=1$ is day 1)
* $P_t^{RB}$: total RB power at step $t$
* $O_t^{RB}$: new RB power onboarded in step $t$
* $SE_t^{RB}$: RB power scheduled to expired in step $t$
* $R_t^{RB}$: RB power that renewed in step $t$
* $r_t$: renewal rate at step $t$. This is the percentage of power that will renew at $t$ out of all the power scheduled to expire at $t$
* $d$: duration of a sector after onboarding or renewal

Note that all RB notations have an equivalent notation in QA. As an example, the $P_t^{QA}$ is defined to be the total QA power at step $t$.


## Raw-byte power

We define the RB power at a given step as the previously observed RB adjusted for the inflows and outflows expected at the current step. The inflows are the new onboards and the renewals, while the outflows are the scheduled expirations:

$$
\begin{equation}
\left\{ \begin{aligned} 
  P_0^{RB} &= \textrm{rb_power_zero}\\
  P_t^{RB} &= P_{t-1}^{RB} + O_{t}^{RB} - SE_{t}^{RB} + R_{t}^{RB} 
\end{aligned} \right.
\end{equation}
$$

From the model assumptions, the new onboarded power is simply a constant provided by the user:

$$O_{t}^{RB} = \textrm{rb_onboard_power}$$

The next component is the scheduled expirations. The scheduled power to expire is defined as the sum of the scheduled power to expire coming from two groups of sectors - known active sectors and modeled sectors (i.e., the new onboards and renewals).

$$SE_{t}^{RB} = knownSE_{t}^{RB} + modelSE_{t}^{RB}$$

We can take the scheduled expirations coming from known active sectors  ($knownSE_{t}^{RB}$) directly from the network. This is the $\textrm{rb_known_scheduled_expire_vec}$ provided as input.  

As for the scheduled expirations coming from the modeled onboards and renewals, we can compute it using the estimated power onboarded, the estimated power renewed, and the sector duration:

$$modelSE_{t}^{RB} = O_{t-d}^{RB} + R_{t-d}^{RB}$$

Note that if $t-d < 0$, then by default $modelSE_{t}^{RB} = 0$. 


The final component of the RB power equation is the power renewed at step $t$. At the time sectors are expected to expire, a percentage of these sectors will renew. Thus, we estimate renewals simply as the product between the renewal rate and the scheduled expirations:

$$R_{t}^{RB} = r_t \cdot SE_{t}^{RB} $$

The renewal rate is user-defined paramater and is a constant ($r_t = \textrm{renewal_rate}$).


## Quality-adjusted power

The equations for QA power are almost the same as the the ones for RB power, where one can simply exchange the $RB$ by $QA$. There are however two differences.

Firstly, the new onboarded power needs to be adapted to take into account the Fil+ multiplier and the rate of Fil+ deals (where $\gamma = \textrm{fil_plus_rate}$):

$$
\begin{equation}
\begin{aligned} 
  O_{t}^{QA} &= (1-\gamma) \cdot O_{t}^{RB} + 10 \cdot \gamma \cdot O_{t}^{RB}\\
  &= (1 + 9 * \gamma) \cdot O_{t}^{RB}\\
  &= (1 + 9 * \textrm{fil_plus_rate}) \cdot \textrm{rb_onboard_power}
\end{aligned}
\end{equation}
$$

Secondly, the scheduled expirations coming from known sectors are taken directly from the network. This is the $\textrm{qa_known_scheduled_expire_vec}$ provided as input.  

$$knownSE_{t}^{QA} = \textrm{qa_known_scheduled_expire_vec}$$


## Tunable quality-adjusted power

The equations for QA power described in the previous section assume that Filcoin Plus deals get a fixed quality multiplier of 10x. To assess the proposal to adapt the quality multipliers, we need a more flexible model that allows the user to change the multiplier and incorporate an additional multiplier based on sector duration. 


To design the new equations, we had to make the following assumptions:

* We are not changing the quality multiplier of currently active deals.
* The quality multiplier for a known active sector will change after renewal based on the user-provided sector duration and $\textrm{fil_plus_rate}$. This means that when a known active sector renews, we assume that its percentage of Fil+ will also change to match these two parameters.
* The quality multiplier for new onboards will depend on the rate of Fil+ deals ($\textrm{fil_plus_rate}$), the sector duration ($d$), the multiplier for Fil+ deals ($m_{Fil+}$), and the duration multiplier function ($m_{dur}(d)$), which depends on the sector duration $d$.
* The duration multiplier function is a user input and will be one of the parameters to tune during our simulations


Under these assumptions, the equations for the raw-byte power remain unchanged. We only need to update the daily QA power onboarded (as expected!) and QA renewals (since renewed sectors will have a different multiplier based on the sector duration and Fil+ rates). 

We should also note that scheduled expirations coming from known active sectors ($knownSE_{t}^{QA}$) have the same equation as the "original" QA power section because we assume that active sectors do not change their quality multipliers unless they renew.

The daily quality-adjusted onboarded power is defined as (where $\gamma = \textrm{fil_plus_rate}$):

$$
\begin{equation}
\begin{aligned} 
  O_{t}^{QA} &= m_{dur}(d) \cdot  (1-\gamma) \cdot O_{t}^{RB} + m_{dur}(d) \cdot m_{Fil+} \cdot \gamma \cdot O_{t}^{RB}\\
  &= m_{dur}(d) \cdot (1 + (m_{Fil+}-1) * \gamma) \cdot O_{t}^{RB}\\
  &= m_{dur}(d) \cdot (1 + (m_{Fil+}-1) * \textrm{fil_plus_rate}) \cdot \textrm{rb_onboard_power}
\end{aligned}
\end{equation}
$$

Similarly, we need to adapt the renewals equation to take into account the new multiplier after renewal. To do this, it is simpler to start from the scheduled renewals in RB power and apply the new multiplier:

$$R_{t}^{QA} = m_{dur}(d) \cdot (1 + (m_{Fil+}-1) * \textrm{fil_plus_rate}) \cdot r_t \cdot SE_{t}^{RB} $$

This is in line with the assumption that renewed sectors will have the same Fil+ rate and duration as the new onboarded sectors.
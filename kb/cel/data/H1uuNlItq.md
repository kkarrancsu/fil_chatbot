---
title: Model spec - Network power forecasting v1
tags: Econ models
---

# Model spec - Network power forecasting v1

#### Maria Silva, June 2022

In this document, we describe the methodology and the main assumptions used to create the network power model used in the [Baseline Crossing project](/96OArWoLQvu1HtSnfwgrnQ) and in the quality multipliers expansion proposal.

## Model assumptions

When designing this model, we focus on daily aggregate network dynamics. In order words,  we avoid complex simulations that capture individual miner behavior and, instead, model aggregate network metrics and mechanisms using sensible approximations.

With this in mind, the model has the following assumptions:

* Forecasting is done daily. This means that each forecasting step corresponds to a day and the forecasted power metrics correspond to the value we expect to see at the end of that day.
* We use the current sector states (i.e. known schedule expirations) and we estimate future onboardings and future renewals.
* The daily power onboarded is a constant provided as a tunable parameter. This is a BIG assumption and we will probably want to make the new onboarding a function of time (e.g. have a linear function or a capped liner function). However, for this first deterministic model, having a constant is the easiest approach.
* The sector renewal rate is a constant provided as a tunable parameter.
* Sector durations are constants provided as a tunable parameter.
* We use a single sector cycle. In other words, for each sector currently active or onboarded, at the expiration date, we consider that it may be renewed only once. If it is renewed, we move the expiration date forward and we don't consider further renewals. This assumption is needed so that we can model the process in a single go.
* Filecoin Plus sectors have the same renewal rates and sector lengths as other sectors. This is something we may want to relax after we do a deeper analysis of renewal rates and sector lengths split by sector type.
* Since we currently don't have the known scheduled expirations measured in quality-adjusted power, we approximate it using a provided rate of Fil+ power. This is another assumption we want to remove when we can extract the real data.

The model receives the following inputs as parameters:
* $\textrm{renewal_rate}$ (%): sector renewal rate (out of scheduled expiration)
* $\textrm{rb_onboard_power}$ (PiB): raw-byte storage amount to be onboarded on a daily basis
* $\textrm{fil_plus_rate}$ (%): percentage of $\textrm{rb_onboard_power}$ that contains Filcoin Plus deals
* $\textrm{onboard_length}$ (days): duration of the sectors onboarded
* $\textrm{renewal_length}$ (days): duration of the sectors renewed
* $\textrm{forecast_lenght}$ (days): number of days in which to run the simulation

In other words, these are the "nobs" that the user can tweak to create different scenarios of Storage Providers (SPs) behavior.

Besides these parameters, the model receives some inputs from the current state of the network:
* $\textrm{rb_power_zero}$ (PiB): total raw-byte power of the network
* $\textrm{qa_power_zero}$ (PiB): total quality-adjusted power of the network
* $\textrm{rb_known_scheduled_expire_vec}$ (vector of PiB): raw-byte storage power from active sectors expected to expire at each day

From these inputs, the model derives the raw-byte (RB) power and quality-adjusted (QA) power for each day.


## Notation

Before we detail how the model computes RB and QA power, we need to define the following notation:

* $t$: forecasting step (e.g. $t=0$ is day 0 and $t=1$ is day 1)
* $P_t^{RB}$: total RB power at step $t$ (cumulative)
* $O_t^{RB}$: new RB power onboarded in step $t$
* $SE_t^{RB}$: RB power scheduled to expired in step $t$
* $R_t^{RB}$: RB power that renewed in step $t$
* $r_t$: renewal rate at step $t$. This is the percentage of power that will renew at $t$ out of all the power scheduled to expire at $t$
* $lo$: average duration of the sectors after onboarding
* $lr$: average duration of the sectors after renewal

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

The next component is the scheduled expirations. The scheduled power to expire is defined as the sum of the scheduled power to expire coming from three groups of sectors - currently active, new onboards, and renewals:

$$SE_{t}^{RB} = activeSE_{t}^{RB} + oboardSE_{t}^{RB} + renewSE_{t}^{RB}$$

We can take the scheduled expirations coming from active sectors  ($activeSE_{t}^{RB}$) directly from the network. This is the $\textrm{rb_known_scheduled_expire_vec}$ provided as input.  

As for the scheduled expirations coming from new onboards, we can compute it using the estimated power onboarded and the duration of onboards:

$$oboardSE_{t}^{RB} = O_{t-lo}^{RB}$$

Note that if $t-lo < 0$, then by default $oboardSE_{t}^{RB} = 0$. 

Thirdly, the scheduled expirations coming from renewals depend on the renewed power (which will be defined at the end) and the duration of renewals:

$$renewSE_{t}^{RB} = R_{t-lr}^{RB}$$

Once again, if the time index $t-lr$ is less than zero, then the scheduled power to expire will be zero as well.


The final component of the RB power equation is the power renewed at step $t$. Renewals may come from two different sets of sectors - active sectors and onboarded sectors. Thus, we define $R_{t}^{RB}$ as:

$$R_{t}^{RB} = activeR_{t}^{RB} + onboardR_{t}^{RB}$$

In both sets of sectors, at the time they are expected to expire, a percentage of these sectors will renew. Thus, both components are simply the product between the renewal rate and the scheduled expirations for its groups of sectors:

$$activeR_{t}^{RB} = r_t \cdot activeSE_{t}^{RB} $$

$$onboardR_{t}^{RB} = r_t \cdot onboardSE_{t}^{RB} $$

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

Secondly, the scheduled expirations coming from active sectors are estimated using the RB expirations and the $\textrm{fil_plus_rate}$. Recall that the reason we do this is that we don't have an easy way of getting the real data from the network at the moment. This will be something to improve on later models.

$$activeSE_{t}^{QA} = (1 + 9 * \textrm{fil_plus_rate}) \cdot activeSE_{t}^{RB}$$


## Tunable quality-adjusted power

The equations for QA power described in the previous section assume that Filcoin Plus deals get a higher quality multiplier of 10x. To assess the proposal to adapt the quality multipliers, we need a more flexible model that allows the user to change the multiplier and incorporate an additional multiplier based on sector duration. 


To design the new equations, we had to make the following assumptions:

* The quality multiplier for a sector can change after renewal based on the renewal length. However, before they renew, the multiplier is the original 10x multiplier on Fil+ deals.
* We are not changing the multiplier of currently active deals.
* The quality multiplier for new onboards will depend on the rate of Fil+ deals ($\textrm{fil_plus_rate}$), the expected sector duration ($lo$), the multiplier for Fil+ deals ($m_{Fil+}$), and the duration multiplier function ($m_{dur}(t)$), which depends on the sector duration $t$.
* The duration multiplier function is a user input and will be one of the focus to tune during our simulations


Under these assumptions, the equations for the raw-byte power remain unchanged. We only need to update the daily QA power onboarded (as expected!) and QA renewals (since renewed sectors may have a different multiplier based on the renewal length). 

We should also note that scheduled expirations coming from active sectors ($activeSE_{t}^{QA}$) have the same equation as the "original" QA power section because we assume that active sectors do not change their quality multipliers unless they renew.

The daily quality-adjusted onboarded power is defined as (where $\gamma = \textrm{fil_plus_rate}$):

$$
\begin{equation}
\begin{aligned} 
  O_{t}^{QA} &= m_{dur}(lo) \cdot  (1-\gamma) \cdot O_{t}^{RB} + m_{dur}(lo) \cdot m_{Fil+} \cdot \gamma \cdot O_{t}^{RB}\\
  &= m_{dur}(lo) \cdot (1 + (m_{Fil+}-1) * \gamma) \cdot O_{t}^{RB}\\
  &= m_{dur}(lo) \cdot (1 + (m_{Fil+}-1) * \textrm{fil_plus_rate}) \cdot \textrm{rb_onboard_power}
\end{aligned}
\end{equation}
$$

Now, looking at the renewals, we start from the original formula:

$$R_{t}^{QA} = activeR_{t}^{QA} + onboardR_{t}^{QA}$$

Here, we need to change the $activeR_{t}^{QA}$ and $onboardR_{t}^{QA}$ equations to take into account the new multiplier after renewal. To do this, it is simpler to start from the RB power variables and apply the new multiplier:

$$activeR_{t}^{QA} = m_{dur}(lr) \cdot (1 + (m_{Fil+}-1) * \textrm{fil_plus_rate}) \cdot r_t \cdot activeSE_{t}^{RB} $$

$$onboardR_{t}^{QA} = m_{dur}(lr) \cdot (1 + (m_{Fil+}-1) * \textrm{fil_plus_rate}) \cdot r_t \cdot onboardSE_{t}^{RB} $$
# Network power model with Nicola's longevity multipliers

#### Maria Silva, June 2022

###### tags: `FIPs`

In this document, we describe the methodology and the main assumptions used to create the network power model that assumes the introduction of a new type of duration multiplier as proposed by Nicola.

The idea is to have a duration multiplier base on the longevity of a sector. As an example, a 1-year sector that is renewing for an additional year would get a 2-year duration multiplier after renewal.

This new approach is expected to have two main benefits:

1. We can maintain the current upper limit of 1.5 years for the sector duration. This was a security concern raised by Nicola.
2. We expect this mechanism to smooth out the amount of circulating supply being locked and the drop in SPs profitability.

An important note here is that we will cap the multiplier after 5 years. In other words, a sector with more than five years will continue to receive the same duration multiplier as the 5-year sector. This limit may change in the tuning phase.

## Model assumptions

When designing this model, we focus on daily aggregate network dynamics. In order words,  we avoid complex simulations that capture individual miner behavior and, instead, model aggregate network metrics and mechanisms using sensible approximations.

With this in mind, the model has the following assumptions:

* Forecasting is done daily. This means that each forecasting step corresponds to a day and the forecasted power metrics correspond to the value we expect to see at the end of that day.
* We use the current sector states (i.e. known schedule expirations) and we estimate future onboardings and future renewals.
* The daily power onboarded is a constant provided as a tunable parameter. This is a BIG assumption and we will probably want to make the new onboarding a function of time (e.g. have a linear function or a capped liner function). However, for this first deterministic model, having a constant is the easiest approach.
* The sector renewal rate is a constant provided as a tunable parameter.
* Sector duration is constant and hardcoded to year (for both new onboards and renewed sectors).
* Filecoin Plus sectors have the same renewal rates and sector durations as other sectors. This is something we may want to relax after we do a deeper analysis of renewal rates and sector durations split by sector type.
* Since we currently don't have the known scheduled expirations measured in quality-adjusted power, we approximate it using a provided rate of Fil+ power. This is another assumption we want to remove when we can extract the real data.
* We are not changing the quality multiplier of currently active deals.
* The quality multiplier for a known active sector will change after renewal based on the new sector duration multiplier and $\textrm{fil_plus_rate}$. This means that when a known active sector renews, we assume that its percentage of Fil+ will also change to match the model assumptions.
* The duration multiplier is given by a linear function of the sector's longevity. The slope of the linear function will be provided by the user.
* Because we don't have data on the longevity of currently active sectors, we will assume all active sectors will be 1-year old at their termination date.

The model receives the following inputs as parameters:
* $\textrm{renewal_rate}$ (%): sector renewal rate (out of scheduled expiration)
* $\textrm{rb_onboard_power}$ (PiB): raw-byte storage amount to be onboarded on a daily basis
* $\textrm{fil_plus_rate}$ (%): percentage of $\textrm{rb_onboard_power}$ that contains Filcoin Plus deals
* $\textrm{forecast_lenght}$ (days): number of days in which to run the simulation
* $m_{dur}$: slope of the duration multiplier. This corresponds to the multiplier of a 1-year-old sector.

In other words, these are the "nobs" that the user can tweak to create different scenarios of Storage Providers (SPs) behavior.

Besides these parameters, the model receives some inputs from the current state of the network:
* $\textrm{rb_power_zero}$ (PiB): total raw-byte power of the network
* $\textrm{qa_power_zero}$ (PiB): total quality-adjusted power of the network
* $\textrm{rb_known_scheduled_expire_vec}$ (vector of PiB): raw-byte storage power from active sectors expected to expire at each day

From these inputs, the model derives the raw-byte (RB) power and quality-adjusted (QA) power for each day.


## Notation

Before we detail how the model computes RB and QA power, we need to define the following notation:

* $t$: forecasting step (e.g. $t=0$ is day 0 and $t=1$ is day 1)
* $P^{RB}(t)$: total RB power at step $t$
* $O^{RB}(t)$: new RB power onboarded in step $t$
* $SE^{RB}(t)$: RB power scheduled to expired in step $t$
* $R^{RB}(t)$: RB power that renewed in step $t$
* $r$: renewal rate. This is the percentage of power that will renew at any given day out of all the power scheduled to expire at that day
* $d$: duration of a sector after onboarding or renewal

Note that all RB notations have an equivalent notation in QA. As an example, the $P^{QA}(t)$ is defined to be the total QA power at step $t$.


## Raw-byte power

We define the RB power at a given step as the previously observed RB adjusted for the inflows and outflows expected at the current step. The inflows are the new onboards and the renewals, while the outflows are the scheduled expirations:

$$
\begin{equation}
\left\{ \begin{aligned} 
  P^{RB}(0) &= \textrm{rb_power_zero}\\
  P^{RB}(t) &= P^{RB}(t-1) + O^{RB}(t) - SE^{RB}(t) + R^{RB}(t) 
\end{aligned} \right.
\end{equation}
$$

From the model assumptions, the new onboarded power is simply a constant provided by the user:

$$O^{RB}(t) = \textrm{rb_onboard_power}$$

The next component is the scheduled expirations. Because we need to keep track of sector longevity to model QA power, we have to split the scheduled expirations into 4 groups:

* $SE^{RB}_0(t)$: RB power scheduled to expire at step $t$ coming from new onboards.
* $SE^{RB}_1(t)$: RB power scheduled to expire at step $t$ coming from 1st-time renewals.
* $SE^{RB}_2(t)$: RB power scheduled to expire at step $t$ coming from 2nd-time renewals.
* $SE^{RB}_+(t)$: RB power scheduled to expire at step $t$ coming from sectors that have renewed 3 or more times already.

After we model each component, we can set the total RB power scheduled to expire as: 

$$SE^{RB}(t) = SE^{RB}_0(t) + SE^{RB}_1(t) + SE^{RB}_2(t) + SE^{RB}_+(t)$$

Before we define the equations for the scheduled expirations, we need to introduce a similar notation for renewed power. In particular, we define the total renewed power $R^{RB}(t)$ as the sum of renewed power coming from the following four groups of sectors:

* $R^{RB}_1(t)$: 1st-time renewals
* $R^{RB}_2(t)$: 2nd-time renewals
* $R^{RB}_3(t)$: 3rd-time renewals
* $R^{RB}_+(t)$: sector renewing for the 4th time or more (aka the *oldy renewals*)

Now we have everything in place to define the equations for the scheduled expirations. Here we just need to use the estimated power onboarded, the estimated power renewed, and the sector duration ($d:=$ 1 year):

* $SE^{RB}_0(t) = O^{RB}(t-d)$
* $SE^{RB}_1(t) = R^{RB}_1(t-d)$
* $SE^{RB}_2(t) = R^{RB}_2(t-d)$
* $SE^{RB}_+(t) = R^{RB}_3(t-d) + R^{RB}_+(t-d)$

Note that if $t-d < 0$, then the corresponding renewed power at $(t-d)$ is set to zero.

The final component of the RB power equation is the power renewed at step $t$. We already introduced the notion of the 4 different renewals groups based on longevity. For each group, the equation is very similar - we just need to multiply the scheduled power to expire coming from the correct sector group by the renewal rate $r$. Recall that the renewal rate is user-defined parameter and is a constant ($r := \textrm{renewal_rate}$). The equations are the following:


* $R^{RB}_1(t) = r \cdot (knownSE^{RB}(t) + SE^{RB}_0(t))$
* $R^{RB}_2(t) = r \cdot SE^{RB}_1(t)$
* $R^{RB}_3(t) = r \cdot SE^{RB}_2(t)$
* $R^{RB}_+(t) = r \cdot SE^{RB}_+(t)$


We should highlight that $R^{RB}_1(t)$ is slightly different because it needs to take into account the new onboards ($SE^{RB}_0(t)$) and the known active sectors ($knownSE^{RB}(t)$). We can take the scheduled expirations coming from known active sectors directly from the network. This is the $\textrm{rb_known_scheduled_expire_vec}$ provided as input.  


## Quality-adjusted power

The equations for QA power are almost the same as the ones for RB power, where one can simply exchange the $RB$ by $QA$. There are however three differences.

Firstly, the new onboarded power needs to be adapted to take into account the duration multiplier for 1-year sectors and the rate of FIL+ deals (where $\gamma = \textrm{fil_plus_rate}$):

$$
\begin{equation}
\begin{aligned} 
  O^{QA}(t) &= m_{dur} \cdot (1-\gamma) \cdot O^{RB}(t) + m_{dur} \cdot 10 \cdot \gamma \cdot O^{RB}(t)\\
  &= m_{dur} \cdot (1 + 9 * \gamma) \cdot O^{RB}(t)\\
  &= m_{dur} \cdot (1 + 9 * \textrm{fil_plus_rate}) \cdot \textrm{rb_onboard_power}
\end{aligned}
\end{equation}
$$

Secondly, the scheduled expirations coming from known sectors are estimated using the RB expirations and the $\textrm{fil_plus_rate}$. Recall that the reason we do this is that we don't have an easy way of getting the real data from the network at the moment. This will be something to improve on later models.

$$knownSE^{QA}(t) = (1 + 9 * \textrm{fil_plus_rate}) \cdot knownSE^{RB}(t)$$

The third and final variable we need to change is the renewals. Because we need to adapt the duration multiplier based on the longevity of the sectors, we use the RB power renewed at $t$ and apply the correct multiplier, considering both the rate of FIL+ deals ($\gamma$) and the duration multiplier slope ($m_{dur}$):


|    Sector group   | Sector longevity |                                Renewed QAP                                |
|:-----------------:|:----------------:|:-------------------------------------------------------------------------:|
| 1st-time renewals |      2 years     | $R^{QA}_1(t) = R^{RB}_1(t) \cdot (1 + 9 * \gamma) \cdot 2 \cdot m_ {dur}$ |
| 2nd-time renewals |      3 years     | $R^{QA}_2(t) = R^{RB}_2(t) \cdot (1 + 9 * \gamma) \cdot 3 \cdot m_ {dur}$ |
| 3rd-time renewals |      4 years     | $R^{QA}_3(t) = R^{RB}_3(t) \cdot (1 + 9 * \gamma) \cdot 4 \cdot m_ {dur}$ |
| "oldy" renewals   |      5+ years    | $R^{QA}_+(t) = R^{RB}_+(t) \cdot (1 + 9 * \gamma) \cdot 5 \cdot m_ {dur}$ |


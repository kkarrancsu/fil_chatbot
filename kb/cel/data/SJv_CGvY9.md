---
title: Model spec - Locked FIL forecasting
tags: Econ models
---

# Model spec - Locked FIL forecasting

#### Maria Silva & Tom Mellan, June 2022

In this document, we describe the methodology and the main assumptions used to create a model of the total number of FIL tokens locked in any given time. This is one of the most important components of the circulating supply as it depends both the Storage Providers' (SPs) behavior and the network state.


## Model assumptions

When designing this model, we focus on daily aggregate network dynamics. In order words,  we avoid complex simulations that capture individual SP behavior and, instead, model aggregate network metrics and mechanisms using sensible approximations.

We should note that this model depends on other models, namely, the [power model](https://hackmd.io/@msilvaPL/SkapZkrdc), the mining model, and the circulating supply model. As such, it will automatically inherit all the assumptions being made in those models. It also inherits the "nobs" defined in the power model to model SPs behavior. In later sections, we detail how each model is used to forecast locked FIL.

In addition to the inherited assumptions, we need to highlight the following assumptions:

* Forecasting is done daily. This means that each forecasting step corresponds to a day and the forecasted metrics correspond to the value we expect to see at the end of that day.
* We use the current pledge metrics (i.e. known scheduled expiration in pledge) to model known active sectors and we estimate pledge metrics coming from future onboardings and renewals using the same assumptions as ones used in the network power model.
* Sector duration is a constant provided as a tunable parameter.
* We ignore storage deal collateral when computing the total locked FIL.

Besides the inputs from the other models, this model receives some inputs from the current state of the network:

* $\textrm{known_scheduled_pledge_release_vec}$ (vector of FIL): total FIL locked as initial pledge collateral that is scheduled to be released each day


## Notation

Before we detail how the model computes the total locked FIL, we need to define some notation that will be used throughout the document:

* $t$: forecasting step (e.g. $t=0$ is day 0 and $t=1$ is day 1).
* $L(t)$: total locked FIL at step $t$.
* $\Delta L(t)$: variation in locked FIL at step $t$. This is essentially the difference between the new FIL being locked and the FIL being released at step $t$
* $pledgeL(t)$: total locked FIL at step $t$ due to the initial pledge collateral.
* $\Delta pledgeL(t)$: variation in locked FIL at step $t$ due to the initial pledge collateral.
* $rewardL(t)$: total locked FIL at step $t$ due to the block reward collateral.
* $\Delta rewardL(t)$: variation in locked FIL at step $t$ due to the block reward collateral.
* $C_t$: total circulating supply at step $t$
* $b(t)$: baseline function, which is designed as an exponential $\rightarrow b(t):= b_0 \cdot e^{gt}$
* $P_t^{QA}$: total quality-adjusted power at step $t$
* $O_t^{QA}$: quality-adjusted power onboarded in step $t$
* $R_t^{QA}$: quality-adjusted power that renewed in step $t$
* $dayRe_t$: total network rewards mined in step $t$
* $r_t$: renewal rate at step $t$. This is the percentage of power that will renew at $t$ out of all the power scheduled to expire at $t$
* $SP_t$: total intitial pledge scheduled to expired in step $t$
* $d$: duration of a sector after onboarding or renewal


## Locked FIL

The total locked FIL in the network changes everyday with the inflows and outflos of locked FIL. The inflows correspond to the new collateral being added to the network while the outflows are the collateral released. In other words, we model the total amount of locked FIL at step $t$ as:

$$L(t) = L(t-1) + \Delta L(t)$$


In the Filecoin network, we have three different collateral mechanisms that contribute to locking FIL tokens:

1. **Initial pledge collateral** is an initial commitment of FIL that an SP must provide with each sector. The pledge size is meant to adequately incentivize the fulfillment of a sectorʼs promised lifetime and provide sufficient consensus security.
2. **Block reward collateral** corresponds to the number of future block rewards that get locked at the time each block is mined. Block rewards earned by a sector are subject to slashing if a sector is terminated before its expiration. The goal here is to avoid having an initial pledge too high for SPs while still maintaining good storage security.
3. **Storage deal collateral** is an additional pledge provided by the SP to collateralize deals. This is an agreement between the storage user and the SP and it is not imposed by the protocol. In line with our assumptions, this will be assumed to be zero.

Thus, we can further split that initial equation, based on the type of collateral being changed:

$$L(t) = L(t-1) + \Delta pledgeL(t) + \Delta rewardL(t)$$

### Initial pledge collateral

Now let's start with the initial pledge collateral, $\Delta pledgeL(t)$. This delta is simple terms the total inflows at step $t$ (i.e. the new locked pledge) minus the total outflows at step $t$ (i.e. the pledge release):

$$\Delta pledgeL(t) = Pl_t - releasePl_t$$


Before going into detail about the inflows and outflows, we need to clarify how pledge works for two different types of sectors, namely, newly onboarded sectors and renewed sectors.

When a sector is onboarded, its pledge is computed and locked until the time when the sector is expected to expire (assuming there is no early termination). At that time, the sector may have two outcomes - expiration or extension.

In the case of extension, what happens to the sector pledge may vary. If the new pledge at the time of the expiration is lower than the original pledge, the sector's pledge will not be released. However, if the new pledge is higher than the original, then the sector's pledge is released and the new higher pledge will get locked.

This means that for renewed sectors, the new pledge will always be greater or equal to the original pledge, which makes the equations for $\Delta pledgeL(t)$ different depending on whether they are coming from onboards or renewals:

$$\Delta PledgeL(t) = \Delta oPledgeL(t) + \Delta rPledgeL(t)$$

$$\Delta oPledgeL(t) = oPl_t$$

$$\Delta rePledgeL(t) = rePl_t - releasePl_t$$


Note that the delta pledge for new oboards doesn't have releases. Pledge is only locked from storage collateral and consensus collateral during onboarding. The formulas are:

$$oPl_t = oStoragePl_t + oConsensusPl_t$$

$$oStoragePl_t = 20 \cdot dayRe_t \cdot \frac{O_t^{QA}}{P_t^{QA}}$$

$$oConsensusPl_t = 0.3 \cdot C_{t-1} \cdot \frac{O_t^{QA}}{\max(b(t), P_t^{QA})}$$

Note that the power statistics $O_t^{QA}$ and $P_t^{QA}$ come directly from the power model described [here](https://hackmd.io/@msilvaPL/SkapZkrdc). The daily network reward $dayRe_t$ comes from the minting model, *which we still need to document*. The circulating supply $C_t$ comes from the circulating supply model, *which we also haven't yet documented*. And finally, the baseline function, $b(t)$, is deterministic so there is no need to estimate it.

What about the renewals? The delta pledge for renewals depends mostly on the scheduled pledge to expire $SP_t$, the renewal rate $r_t$, and the difference between the pledges of the sectors scheduled to expire computed at steps $t$ and $t-d$ (recall that $d$ is the sector duration). The folllowing diagram summarises the idea:

<div style="text-align:center">
<img src="https://i.imgur.com/BNfQPkO.png" />
<br>
<br>
</div>

From the diagram, the only formula which is not fully defined is $\Delta Pl_{t, t-d}$:

$$\Delta Pl_{t, t-d} = newPledge - originalPledge$$

$$newPledge = 20 \cdot dayRe_t \cdot \frac{R_t^{QA}}{P_t^{QA}} +  0.3 \cdot C_{t-1} \cdot \frac{R_t^{QA}}{\max(b(t), P_t^{QA})}$$


$$originalPledge = r_t \cdot SR_t$$

Before we continue with the remaining equations, it is important to point out that miners may decide to let a sector expire and automatically re-seal it to get a better deal in terms of collateral. If we wanted to simulate this phenomenon, the ony chnage we needed to do is to drop the $\max$ function from the $\Delta rePledgeL(t)$ equation:

$$\Delta rePledgeL(t)^* = \Delta Pl_{t, t-d}$$

Now, the final component of our equations is the scheduled pledge to be released $SR_t$. Similarly to the power model, scheduled releases may come from two types of sectors - known active sector and modeled sectors (i.e. newly onboarded and renewed):

$$SR_t = knownSR_t + modelSR_t$$

We can take the scheduled releases coming from known active sectors  ($knownSR_t$) directly from the network. This is the $\textrm{known_scheduled_pledge_release_vec}$ provided as input.  

As for the pledge releases coming from the modeled onboards and renewals, we can compute it using the previous locked pledge and the sector duration parameter ($d$):

$$modelSR_t = Pl_{t-d}$$

Note that if $t-d$ is lower than the current day of the forecast, then we define $modelReleasePl_t := 0$. In other words, if we are looking back to past data, then the known scheduled releases already contains the total pledge scheduled to be released. 


### Block reward collateral

At each tipset, 75% of all minting rewards are locked as collateral. This is the block reward collateral we discussed before. This locked collateral is then released linearly over 180 days. Thus, the equations for the locked FIL corresponding to block reward collateral are the following:

$$\Delta rewardL(t) = newRewardLocked_t - releaseReward_t$$

$$newRewardLocked_t = 0.75 \cdot dayRe_t$$

$$releaseReward_t = rewardL(t-1)/180$$


## References

* [Model spec](https://hackmd.io/@msilvaPL/SkapZkrdc) for network power
* [Filecoin documentation](https://spec.filecoin.io/#section-systems.filecoin_mining.miner_collaterals) on miner collaterals
* [Code](https://github.com/filecoin-project/specs-actors/blob/d56b240af24517443ce1f8abfbdab7cb22d331f1/actors/builtin/miner/monies.go#L162-L182) for the initial pledge collateral

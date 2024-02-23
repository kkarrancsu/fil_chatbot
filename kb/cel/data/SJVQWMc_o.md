---
title: FIP-036 revisions
tags: FIPs
---

# FIP-036 revisions

#### [CryptoEconLab](https://www.notion.so/CryptoEconLab-2bd339628c95447b8a9f7df3e8cf8798) authors: Axel Cortes Cubero, Dave Costenaro, Maria Silva, Tom Mellan, and Vikram Kalghatgi  

:::warning
:warning: Please note, this analysis is based on simulations of plausible scenarios conditional on the model assumptions listed in the appendix here. The analysis is not a precise forecast of what will happen in the future. As always, a plurality of voices is valuable (people should do their own research).
:::

This document is a response to the points that have been raised in FIP discussion [#386](https://github.com/filecoin-project/FIPs/discussions/386) and [#421](https://github.com/filecoin-project/FIPs/discussions/421), and in-person discussions with EMEA, NA, Asian storage provider (SP) working groups this week. It builds on the previous modeling summary. To keep it light, information and arguments that remain unchanged will not be duplicated. Please refer to the [previous summary document.](https://www.notion.so/Duration-Changes-FIP-discussion-Analysis-Summary-735ce6685b7946f0a03fc13c3fe271fa)

### Topics addressed

- Clarification on the problem and the proposed solution
- Revised details on the duration multiplier slope and the InitialPledgeLockTarget parameter
- Important and/or recurring questions:
    - What will the new ROI be?
    - What will the initial pledge be?
    - What will the % of available supply that’s locked be?
    - What does the QAP projection look like?
    - What will the effect on small SPs be?
    - Does rolling-out too quickly create an unfair preference for CC?
    - Why the short lead time and concurrent rollout?
    - *There is not enough FIL circulating to fulfill the changes this FIP potentially entails.*
    - *Extension of early testnet sectors.*
    - *I’m a FIL+ SP, will my block rewards decrease?*
    - *The proposal unfairly favors CC over FIL+.*
    - Should there be a ramp in InitialPledgeTargetLock?

### Problem and Solution

The motivation and solution are set out in the [FIP draft discussion](https://github.com/filecoin-project/FIPs/discussions/421). To make them clearer, following requests, the motivation is reiterated.

**Problem**

- Current incentive structures and network parameters, such as 180d minimum, 540d maximums, and ROI dynamics, encourage short-term behavior. They should be updated to better incentivize long-term storage so storage providers who are long-term committed are more fairly rewarded.
- This is intended to support client demand for longer storage durations and the long-term network health.
- Part of the package is an intention to stabilize the % of available supply that is locked. This has been decreasing since approximately Sept 2021. Stabilizing locking dynamics is intended to benefit all network participants who are long-term aligned
- The proposal is judged high-priority by the [FIP](https://www.notion.so/Duration-FIP-revisions-7426f344685940409ac513a0ffcccc86) authors and time sensitive.  In part this is due to the capacity of smaller SPs to weather the winter cycle in our industry and wider global macroeconomic downturn. Time sensitive because we believe the proposal will be positive for the network and not implementing quickly unnecessarily delays receiving the beneficial effects.

**Proposed solution**

- Allow committed SPs to express a longer-term view on the network and be rewarded more for their commitment.
- This is achieved with a power multiplier based on sector duration. Longer durations receive a higher rate of rewards, and longer durations also lock more collateral.
- Adapt the InitialPledgeLockTarget parameter so the total value locked tracks on a higher long-term trajectory. This increases stability which is necessary for successful SP businesses and long-term storage goals.
- Collectively these actions incentivize long-term storage and improve the long-term outlook of the network.

### Revised parameters

After consulting Storage Providers and the broader community we suggest adapting the [previous proposal](https://www.notion.so/Duration-Changes-FIP-discussion-Analysis-Summary-735ce6685b7946f0a03fc13c3fe271fa) in two ways.

**The first change** is to decrease slope from **2x** to **1x.** 

This is to address concerns voiced by some SPs that a change from no slope to a slope of 2x is too large to happen at once, that it may disturb the balance of CC and FIL+, and that it may dissuade some SPs who wish to participate in maximum commitments. 

While we don’t believe 2x is likely to cause these potential issues, CEL agrees with the principle of making the smallest change possible that can achieve most of the proposal's goals. However the desire for implementing small changes must be balanced against the policy’s sufficiency. In this, an important factor to recognize is that core economic changes cannot occur frequently. SP’s should have a stable environment for business planning. 

In summary, when combined with other changes (discussed next), we believe a 1x slope can be sufficient to achieve most of the proposal’s goals. 

The new proposed 1x sector duration multiplier looks like:

<div style="text-align:center">
<img width="500" src="https://hackmd.io/_uploads/ryMDfGqds.png">
<br>
<br>
</div>

Additional point on slope: it is worth considering a *non-linear* slope. If we want to ensure sufficient uptake of longer duration sectors, while not having a large endpoint multiplier, this may be a good option. Decreasing the slope from 2x to 1x lowers the incentive to store for longer. This decreases the potential to realize the positive effects to long-term stability and to client demand. This could be mitigated by making the slope gently increase with duration, which would encourage longer durations more. 

**The second change** we propose is to the InitialPledgeLockTarget parameter. [Previously](https://www.notion.so/Duration-Changes-FIP-discussion-Analysis-Summary-735ce6685b7946f0a03fc13c3fe271fa) this was suggested to take a new value in the range 40-50%. Now we explicitly recommend 50%. This is needed to maintain the target in % available supply locked with lower slope duration multiplier.

### What will the new ROI be?

The proposed changes intend to spread-out storage providers’ return on investment to make it more sustainable, rather than high at the start then rapidly decreasing in the future. This is about making being an SP work long-term, and making sure the protocol is fair to those who are most long-term aligned.

In concrete terms, the modelled FIL-on-FIL annualized ROI for a 1 year sector with FIL+ sealed within the 1 year is expected to be around 50% with slope 1x and target multiplier 50%. This corresponds to the brown candle here:

<div style="text-align:center">
<img width="300" src="https://hackmd.io/_uploads/Hketfz5_j.png">
<br>
<br>
</div>

The spread in each example reflects uncertainty in the future level of raw byte onboarding, renewal rate and FIL+ rate, as well as variation arising from choosing to seal at different times within the next 12 months. 

In the above image, the returns are for a FIL+ sector. For CC sectors, FIL-on-FIL % ROI is consistently around a tenth lower than the % ROI for FIL+ sectors. 

The values discussed here depend on model assumptions outllined in the [previous summary document](https://www.notion.so/Duration-Changes-FIP-discussion-Analysis-Summary-735ce6685b7946f0a03fc13c3fe271fa). SPs should do their own research and draw their own conclusions. 

### What will the initial pledge be?

The minted rewards SP can receive are based on the QAP. Therefore the relevant quantity to consider is Initial Pledge per QAP. 

The Initial Pledge per QAP is expected to be similar to current (slightly higher) to start with. Then within a few months it will become lower than the current pledge. How quickly it becomes lower depends on how quickly the average duration changes, which depends on how quickly storage providers adopt longer durations and the new distribution of sector durations that we see. The trajectories for a range of scenarios are shown here:

<div style="text-align:center">
<img width="300" src="https://hackmd.io/_uploads/rJVeQzq_i.png">
<br>
<br>
</div>

Note, despite pledge decreasing with time, we do not expect any incentive misalignment. The protocol structure is intended to mean ROI will work for storage providers sealing sectors immediately, and for new storage providers joining in the future.

### What will the % of available locked supply be?

Simulations indicate the percentage of available supply that is locked will increase if the FIP is accepted. 

The current situation is that the percentage has been decreasing since around Sept 2021. With no changes it is expected to decrease further. How much further depends on levels of inflow-outflows from storage onboarding and storage sector renewals. But it is judged to be a priority to stabilize this to produce a more predictable business environment.

With the longer durations induced by the sector duration multiplier incentive, and with InitialPledgeLockTarget = 50%, simulations indicate a shift from 30% toward a higher and more sustained level of around 50%:

<div style="text-align:center">
<img width="300" src="https://hackmd.io/_uploads/B1hXmM9do.png">
<br>
<br>
</div>

Some points to note about the above image:

- It has slope 1x. If the slope was made higher, % locked would be higher.
- InitialPledgeLockTarget is 50%. If this was higher, % locked would be higher.
- The above image corresponds to a new average duration of 3y. Longer durations lead to higher % locked.

### What does the QAP projection look like?

QAP projections are based on assumptions about raw byte power, renewal rate and FIL+ rate. The modeled relationship between these and QAP is documented [here](https://hackmd.io/@msilvaPL/SkapZkrdc). 

In the supply simulations, the assumptions have variation +/-50% to reflect our future uncertainty. This leads to the following QAP trajectories for i) the ‘no change scenario and ii) a central scenario of slope 1x, average duration 3y, and 50% InitialPledgeLockTarget:

<div style="text-align:center">
<img width="300" src="https://hackmd.io/_uploads/BJRSQfcdi.png">
<br>
<br>
</div>

### What will the effect on small SPs be?

Everyone can benefit from this change. The multiplier does not depend on size of storage provider or quantity of raw byte.

A concern raised is that capital availability may unfairly advantage larger SPs. We don’t necessarily agree with this, because complexity of operations increases quickly with size. The cost of acquiring collateral increases approximately sublinearly. This should benefit small SPs.

Note that the ROI calculations above show rewards relative to gas and initial pledges. When also factoring in CapEx and OpEx costs, there should be minimal disadvantage to SP’s based on size. Conservatively, CapEx and OpEx, costs scale roughly linearly, so, at worst, smaller miners remain on the same playing field as larger players. At best, however, they are able to take advantage of existing FIL+ incentives, the relative ease of obtaining collateral, coupled with more efficient/cheaper operations, in order to quickly boost their return profiles.

<div style="text-align:center">
<img width="500" src="https://hackmd.io/_uploads/BkavXz9dj.png">
<br>
<br>
</div>

If anything, smaller miners, who have more of their QAP deriving from FIL+ deals should benefit from the DurationMultiplier changes. They are able to multiplicatively scale their returns *without* additional CapEx or OpEx costs extremely efficiently, since the duration multiplier proposed is multiplicative on top of existing FIL+ incentives.

### Concern rolling-out too quickly may create a preference for CC

A concern was raised about the difference in speed for CC to gain duration multipliers compared to FIL+. In general, it is preferable to seal sooner rather than later. However the advantage is small. This is because multiple factors tradeoff to ensure stability. If SPs seal early they gain a larger multiplier and benefit from higher minting rate and time value of money. But those who seal later benefit from lower initial pledge per QAP. The overall effect is a balance that is designed to provide good outcomes for all scenarios. With specific reference to CC vs FIL+, as noted above, FIL+ is the more profitable. This is expected to remain the case after duration multiplier implementation. 

### Why the short lead time and concurrent rollout?

- Individual researchers recognized scope for improvement quite a few months ago. Discussions began happening initially between single individuals, and within multiple small groups independently. This gradually filtered up to a wider agreement a problem existed that should be prioritized. This was raised as a FIP discussion around 1.5 months ago, a short time after preliminary investigations.
- Multiple research groups have dedicated effort to the proposal because it’s considered important. This has allowed it to progress quickly.
- Other projects may move slower. This is not necessarily a good thing.
- Because the effects of the changes are coupled it’s necessary to consider and implement them together.

### *There is not enough FIL circulating to fulfill the changes this FIP potentially entails.*

It is understandable how this view can arise by multiplying the current locked collateral by the max 5x, but this isn’t the right way to think about it.

To understand how much FIL will be locked, one must account for the relationship between pledge locking and circulating supply in Filecoin’s protocol design. At each epoch, the initial consensus pledge is calculated, and this depends on the circulating supply and quality adjusted power (QAP) — see [monies actor](https://github.com/filecoin-project/specs-actors/blob/d56b240af24517443ce1f8abfbdab7cb22d331f1/actors/builtin/miner/monies.go#L170). With increased locking, the circulating supply numerator decreases and QAP denominator increases — this means the pledge decreases. This relationship in turn means the locked pledge **cannot** exceed the circulating supply. 

To see how much is likely to be locked in typical scenarios please see the percentage available supply locked figure above.

### *There is not enough FIL available to borrow/lend*

Around 30% of available supply **is currently locked. This percentage may increase over time to around 50% if the FIP is implemented (based on simulations which are conditional on growth assumptions). This leaves around 50% still not locked up and therefore potentially available to borrow/lend. Unlocked FIL will be distributed among different stakeholders, such as retail investors, SPs, and lenders. If there is demand for borrowing, this will be satisfied by the free market, the efficiency of which is expected only to increase over time, especially as FVM comes online.

### Should there be a ramp on InitialPledgeTargetLock?

The design space of various ramps has been considered. In particular, before, we suggested 40%→ 50% ramp for InitialPledgeTargetLock.

This is likely not advantageous because it has some counteracting effects. On one hand changes to ROI and supply are smoothed, but it is also true a lower initial pledge per QAP likely induces a speeding-up of SPs changing their duration profile, which has the opposite effect. Therefore 50% only and no ramp is now recommended.

### *The proposal unfairly advantages early testnet sectors*

I don’t think this should be the case given v1 sectors can’t be extended, and this was more than 540d ago.

### *I’m a FIL+ SP, will my block rewards decrease?*

- It may increase or decrease depending on i) the duration you choose for new deals, ii) if you extend your FIL+ deals to longer durations (#313 dependent), and iii) the collective behavior of other CC sectors and FIL+ deals.
- A relevant point is that a rising tide lifts all boats — we believe longer sectors are good for network health, and this can benefit all.

### *The proposal unfairly favors CC over FIL+*

Two comments:

- The multipliers retain the current relative subsidy that gives FIL+ an advantage compared to CC.
- FIL+ deals currently tend to be longer than CC sectors, so demand for long FIL+ deals is likely not a limiting factor for SPs who primarily work with verified data.  Facilitating deal extension via #313 should be prioritized if possible.

Function:

<div style="text-align:center">
<img width="600" src="https://hackmd.io/_uploads/ryc3QGq_i.png">
<br>
<br>
</div>
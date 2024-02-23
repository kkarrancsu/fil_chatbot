---
title: Duration FIP simulations — Summary Analysis
tags: FIPs
---

# Duration FIP simulations — Summary Analysis

#### Tom Mellan, June 2022

<div style="text-align:center">
<img width="400" src="https://hackmd.io/_uploads/S1xE2bcOi.png">
<br>
</div>

**Figure 1:** Three-year ahead projections for the ratio of (locked + burned) FIL to circulating supply, defined as (Minted + Vested) - (Locked + Burned). This is shown for the scenario of a duration multiplier function that’s linear with a 3x slope, with a new average sector duration of 4 years (tan bands). For reference, this potential scenario is compared to ‘no change’ supply dynamics (blue bands).

### Summary

**A [FIP discussion was recently opened](https://github.com/filecoin-project/FIPs/discussions/386)** on better aligning storage provider rewards with the long-term storage of useful client data. The changes proposed are in essence twofold: i) increasing possible sector durations from 180-540 days to 1-5 years, and ii) introducing a quality multiplier function that rewards longer-term sector commitments. To explore the effects on the economics of the Filecoin ecosystem and mitigate potential risks, CEL analyzed the proposed changes from the perspective of circulating supply dynamics and storage providers’ return on investment.

**Scenarios** 

Scenarios are tested across linear duration multipliers with slopes of {0,1,2,3,4,5}, and new average sector durations of {1,2,3,4,5} years. 

Both duration multipliers and longer average durations separately lead to locking more FIL and lowering circulating supply, however in simulation, the latter produces more gradual and persistent effects. From the perspective of stability, the principle of minimum multiplier change that incentivizes longer sector durations should be adopted.

In the *outermost* scenario tested — where new sectors have an average duration of 5 years and the linear multiplier has a 5x slope — the locked FIL at +3 years is estimate to be 3.5x higher, and the circulating supply is 30% lower than a no-change reference (ie in the case this FIP is rejected).

However, a new average sector of 4 years with a multiplier slope of 3x may be a more likely outcome of potential changes under discussion. This is treated as the central scenario which is given more attention next.

**Central scenario**

The central scenario is a linear duration multiplier with a slope of 3x, which is modeled as inducing a new average sector duration of 4 years. In response to this change, the locked pledge is expected to increase by x2 within 1 year, and the circulating supply reduce by 20%. 

In Figure 1 (top), projections +3 years ahead show the future trend for (locked+burned)/supply, both for the central scenario, and in the case of no change. The central scenario restores the (locked+burned)/supply ratio to values close to the circulating supply dynamics observed in early 2021. 

**FIL-on-FIL return**

If we introduce a linear duration multiplier function, SPs still experience the right incentives in terms of FIL-on-FIL return. In other words, if SPs behave rationally and if we disregard the additional operational costs and cash availability, SPs are incentivized to continue to lock more FIL+ deals and to do it within longer sectors.

Adding the duration multiplier will lead to a lower FFoR in the short term (i.e. during the first 6 months). However, in the long run, SPs will get a better return with the introduction of the duration multipliers than they would have with no duration multipliers.
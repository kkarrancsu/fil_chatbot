---
title: Duration Changes FIP discussion
tags: FIPs
---

# Duration Changes FIP discussion — Analysis Summary


#### [CryptoEconLab](https://www.notion.so/CryptoEconLab-2bd339628c95447b8a9f7df3e8cf8798) authors: Axel Cortes Cubero, Dave Costenaro, Maria Silva, Tom Mellan, and Vikram Kalghatgi  

:::warning
:warning: Please note, this analysis is based on simulations of plausible scenarios conditional on the model assumptions listed in the appendix. The analysis is not a precise forecast of what will happen in the future. As always, a plurality of voices is valuable (people should do their own research).
:::

[FIP Discussion 386](https://github.com/filecoin-project/FIPs/discussions/386) suggests three changes to better align the network with the principles of long-term commitment:

1. Introducing a Sector Duration Multiplier function. Suggested function: linear with slope 2. This acts as an incentive for long-term storage by assigning higher quality-adjusted power (QAP) and therefore rewards to storage providers (SPs) who commit to longer sector durations.
2. Updating the current sector duration limits, from 180-540 days to 1-5 years. This primarily supports the aforementioned longer durations being incentivized.
3. Adjusting the [Initial Consensus Pledge target multiplier](https://spec.filecoin.io/systems/filecoin_mining/miner_collaterals/), from 30% to a higher value of 40 or 50%. This intends to create long-term-aligned total value locked (TVL) dynamics to support stable and predictable conditions for SP returns.

To explore the effects on the economics of the Filecoin ecosystem and mitigate potential risks, CryptoEconLab (CEL) analyzed the circulating supply dynamics and SPs’ returns across a range of plausible scenarios. Here CEL sets out a summary of the economic benefits and drawbacks of the proposed changes, focusing on a central scenario of linear duration multiplier with slope 2 and Initial Consensus Pledge target multiplier of 40%.

## Multiplier Form

<div style="text-align:center">
<img width="400" src="https://lh3.googleusercontent.com/IB_Xn5JBcFPQvc_eu-bwcnA3pDdY6mcRER68ThWkI2cGxK3K3c1wyjVF6zf7tQbQn-HqGGn8u7Ct2jX_wp1gzv0TxLuvGqN4gMV21-q4wU2cygemqrVEhTAneVwtPoePgZjK9X_dT3L26Ycsabk">
<br>
</div>

*☝ Figure 1: Proposed linear Sector Duration Multiplier function.*


In broad terms, theoretical analysis supports a Sector Duration Multiplier that increases with duration. This backs the principle that SPs who undertake a larger commitment should be rewarded commensurately. Detailed arguments on the shape of the multiplier function concern how much the network values long-term commitments in light of options to renew, potential cost to the network of expiration, and the locked collateral’s equivalent risk free rate of return. These are set out in [1](https://hackmd.io/fDMYQ-4LQDiZ2KwKA7dn1w).  As the theoretical forms partially depend on difficult to determine parameters, a linear multiplier function is selected. This is a compromise but does have the advantage of being a choice that minimizes complexity.

Within this framework, the rationale to select the slope (slope 2 is suggested) is based on a principle that can be summarized as follows. The selected parameters should maximize the effectiveness of the duration incentive, subject to SP’s collateral availability constraints, while taking into account micro and macroeconomic consequences. Specifically accounting for SP returns and changes to supply dynamics, which are set out below.

## Duration Limits

<div style="text-align:center">
<img width="400" src="https://lh6.googleusercontent.com/vcdnXctKxF115qdc7k4aOhkjB5IOYlWfaIj2fpXMqpiMD5XCsITc3e4ljAoV10BXW20Kj1MSVDJUBKPZMyP0cKi6fc-42QQ32qEpW9AJ2wxh8ke_UtX0zkANyMRC4e4Mru9-T-Os5XlmcpNsgrQ">
<br>
</div>

*☝ Figure 2: Average sector durations. Data extracted between 1/1/2022 - 6/30/2022.*

The proposal increases the minimum and maximum sector durations. The new lower limit approximately doubles from 180 days to 1 year. This guards the network against negative short-term behaviors, aims to decrease turnover and improve stability. Since most SPs already store for longer durations (Figure 2), this isn’t expected to be an overly burdensome change. The new maximum limit of 5 years gives SPs the option to express a long-term commitment to the network which was previously not possible with the maximum sector duration length of 540 days.

## Linear Multiplier Slope and Initial Consensus Pledge Target Multiplier

### Impact on percentage locked value

<div style="text-align:center">
<img width="800" src="https://lh3.googleusercontent.com/71FA1awAoiJ-rxMZbiVyKfvNQDzBOQUMrPEVNAR4trdnfQNN08wEwTQ76LCJUOqa0Bynu_NuHtnHtl9XHOKMNWQnVc7As4QGkAxPO82cIAnGENn8QU0lflDtXfEgink8Ok2pXZq1Gp1H2kGoXHU">
<br>
</div>

*☝ Figure 3. Projections of the percentage value locked, defined here as Locked / (Minted + Vested - Burned), are shown for the next year. 
Note the denominator is *available supply* not *circulating supply,* which we define as (Minted + Vested - Burned - Locked). The scenarios include ‘no change’ (meaning no change to slope, average duration or target), and the central scenario which has Initial Consensus Pledge target multiplier of 40% and linear Sector Duration Multiplier slope 2 and average sector duration 3 years. In A) the central scenario is shown with the average sector duration is independently varied between 1-5years, in B) the central scenario is shown with the slope of the linear multiplier is independently varied between 1-3, and in C) the central scenario is shown with the Initial Consensus Pledge Target % independently varied between 30-50%. The uncertainty displayed reflects scenarios of +/-50% variation in current rates of onboarding, the relative uptake of Filecoin Plus deals and in future sector renewals.*


The incentives to seal for longer durations create an important secondary economic effect. In addition to the primary outcomes of rewarding long-term commitment and supporting client demand, longer sectors lock collateral for longer. This means more total locked collateral at any given time. How this gradually plays out as an increase in percentage locked value dynamics is shown in Figure 3A. The simulated scenarios show that as incentives induce longer average durations, the percentage locked value increases to around 50% over time (conditional on the model assumptions listed in the appendix). This is a more sustainable level to support long-term storage.

A similar positive effect on percentage locked value happens also via the duration incentive, but by a different mechanism: the magnitude of the linear multiplier slope. This affects a sector’s quality-adjusted power, which in turn, impacts the initial pledge, leading to faster growth in percentage locked value (Figure 3B). The tradeoff is that while higher slope means the duration incentives are more effective, and give more favorable locked supply dynamics, this is constrained by collateral availability, and SP returns (section below).

An important additional point is that higher percentage locked value can be selected for directly. Without relying on duration changes, increasing the Initial Consensus Pledge target multiplier will increase the percentage value locked, as in Figure 3C. This gives an additional independent path to achieve more sustainable supply dynamics and encourage long-term data storage.

Finally note, whichever the route, the outcome on locked supply is vital. Consider the scenario of ‘no change’ in Figures 3A-C. With ‘no change’ the percentage value locked is likely to decline unless the network takes specific measures to target a higher locking.

### Impact on SP’s profitability

<div style="text-align:center">
<img width="800" src="https://hackmd.io/_uploads/r1zGlf9di.png">
<br>
</div>

*☝ Figure 4. In A) the annualized percentage return on pledge invested is shown for a one year Filecoin Plus sector sealed within the next year, for scenarios of no change, and changing the Initial Pledge Target to 30%, 40% or 50%, with a linear multiplier with slope 2. The quartiles reflect uncertainty in future onboarding, renewals and the Filecoin Plus rate, in addition to variation arising from sealing dates within the next 12 months. In B) the annualized percentage return over three years is shown under behaviors of i) 3x1yr_reseal: sealing, expiring, resealing, expiring, then resealing, compared to, ii) 3x1yr_extend: sealing, extend, extend, compared to iii) 1x3yr: making a single 3 year commitment, which leads to a higher locked-in return. In C), the Initial Pledge in FIL/GiB (of quality-adjusted power) is shown, for the no change scenario, and scenarios where average sector duration of 1, 3 or 5 years is combined with a 40% Initial Consensus Pledge target multiplier.*


From an economic perspective, incentivizing longer durations is positive for percentage value locked. But, this is only useful if individual SPs retain a strong FIL-denominated profit margin. Both parts are needed to achieve the network’s long-termist storage goals.

So the question arises, what is the impact on profitability? Simulations indicate SPs retain a strong profit margin. And furthermore we find this conclusion is robust to 50% joint variation in onboarding, FIL+ rate, and renewal levels. An example is set out in Figure 4A, which shows the percentage rate of return from sealing a 1 year sector within the next 12 months. While the annualized percentage return is lower in the short term following the slope 2 proposal compared to ‘no change’, the main effect is to accelerates the network reaching the more sustainable behavior.

Within the central scenario of slope 2, there’s a tradeoff around the Initial Consensus Pledge target multiplier that’s important to note. Larger values (increased from 30% currently) can  impact  immediate returns. This must be balanced against a positive change to percentage value locked. We therefore suggest 40 or 50% are attractive Initial Consensus Pledge targets that the community should consider.

With the introduction of a duration multiplier, SPs experience a change in incentives. In annualized percentage return terms, the new incentives are better aligned with the long-term useful data network goals. For example, sectors with FIL+ deals continue to generate better returns than Committed Capacity sectors, and longer sectors generate higher returns than shorter sectors (Fig. 4B).

Another positive effect of increasing the total locked FIL is its impact on network efficiency. In particular, the proposal presented here leads to a decrease in the Initial Pledge per GiB of quality-adjusted power added to the network (Fig 4C). Thus, with the same hardware, SPs can get a bigger share of rewards by committing to the network for longer.  In addition, the longer the network’s average sector duration, the more pronounced this reduction of initial pledge per GiB is.

## Appendix

### Model design

In order to evaluate how this proposal would impact the network and Storage Providers (SPs), we designed a model that simulates the protocol’s circulating supply contributions under changes to SP sealing behavior, duration multiplier mechanism, and altered Initial Pledge Target. For now we provide a short description of the model assumptions, aiming to provide a complete model specification and accompanying code in the following days:

The main assumptions to take into account are the following

- The daily raw-byte power onboarded is constant on average through time. We use the value currently achieved by the network and take into account a level of variability around this central value.
- The sector renewal rate is also constant on average over time. Similarly, we use the value currently achieved by the network with a level of variability around the central value.
- We also consider that all new sectors being onboarded or renewed have the same duration. This is a fixed parameter that we vary between 1 and 5 years. Throughout the report, we refer to this parameter as the “average sector duration”.
- The percentage of newly onboarded power that contains FIL+ deals is another parameter we model. To simulate an increase in FIL+ deals, we assume that the rate of FIL+ deals increases linearly at a rate of 50% per year. The initial value at the start of the simulation is the currently observed rate.
- Variability is generated by sampling the onboarding, FIL+ rate, and renewal rate parameters with +/-50% uniform variation about their current values. Uncertainty bands in images correspond to 90% coverage intervals unless stated otherwise.

From these assumptions, the model samples trajectories for the supply contributions and metrics for the next 12 months:

1. Total Minted FIL
2. Total Vested FIL
3. Total Burned FIL
4. Total Locked FIL
5. Circulating Supply = Minted + Vested - Burned - Locked
6. Percent Value Locked = Locked / (Minted + Vested - Burned)

In addition to these macro-level metrics, we were interested in the impacts on SPs’ profitability, which we characterize in terms of the percentage return that pledge collateral generates in a year. This is calculated as the percentage annualized FIL-on-FIL return, which is given by ((Minted - Gas + Pledge) / Pledge) ** (duration/1year)) - 1. It is estimated using the circulating supply and network power projections from the macro model. The percentage return considers the gas fees, the rewards and the initial pledge expected for a 32GiB sector using different network scenarios and different sector compositions and durations. It doesn’t account for deal payments, running costs, or token valuation at a later date.
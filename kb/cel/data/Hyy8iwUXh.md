# Token Supply Dynamics in Qredo

#### Maria Silva and Juan P.M. Cianci, CryptoEconLab, July 2023

In this report, we analyze the current token allocation for QRDO and its current circulating supply dynamics.

In addition, we specify the allocation the 1B QRDO not yet allocated and explore how the new tokenomic mechanisms being introduced (i.e. the Staking Models and the new Fee Models) will impact the dynamics of the QRDO supply.

## QRDO allocation

### Current allocation

When the QRDO token was launched, its total token supply was set at 2 billion. At the time, 1 billion was allocated, while the remaining 1 billion was set apart for future allocations. Since the second billion is not yet allocated, the "available" total supply of QRDO does not include these tokens. The next plots shows the token allocation over this "available" total supply.

<div style="text-align:center">
<img width="420" src="https://hackmd.io/_uploads/Hkjo24yw2.png">
<br/>
<br/>
</div>

Then, [in March 2022](https://www.qredo.com/blog/qredo-tokenomics-update), the team used the the Qredo allocation and the Validators fund to burn 140 million tokens. which reduced the circulating supply at the time. Since then, the various allocations have been vesting at their own schedules. The plot below sows the current otken allocation over the current circulating supply.  


<div style="text-align:center">
<img width="420" src="https://hackmd.io/_uploads/HyPEpVkw2.png">
<br/>
<br/>
</div>

In the following section, we will discuss in more detail the current supply dynamics, however, we should note that the main differences between the two allocation plots are due to the vesting schedules of the various funds.

The Team, Seed Round and Option Holders are the groups that vested the slowest and thus they see the largest decrease in allocation when comparing the total supply with the circulating supply. On the other hand, the token sales vested the fastest and thus have the largest increase in the allocation.

The "slow vesting" groups are the most important in our analysis since they will have a larger impact on supply dynamics going forward.

### New allocation

One of the key outcomes of this tokenomics update is to define the allocation of the second billion QRDO tokens. The new allocation needs to cover the following uses:

1. Create a new fund named **Public Goods**. This fund will be used to cover incentive programs for network participants, with a focus on user adoption.
2. Increase the size of **Ecosystem fund**. This fund will have a key role in the Qredo Protocol going forward and, as such, needs to have a larger allocation. This fund will serve two key roles: firstly it will cover the protocol fees of the protocol-funded transactions; secondly, it will be the repository of the service fees being tipped to the network and will control how these funds are released to fund the rewards of the Staking Model. These rewards will depend on the performance and growth of Qredo, thus aligning the participants of the Staking Model with the long-term goals of the network.
3. Create a new fund to support the Staking Model for federated Proof-of-Stake, named **Staking Program Support fund**. This fund is aimed at supporting the rewards of the Staking Model by providing a predictable source of rewards.
4. Increase the **Treasury**, which is the fund dedicated to the development and growth of the Qredo ecosystem. The scope includes funding partner programs, grants, private sales, and allocations to market makers and exchanges.
5. Do an **additional token burn** to soften the shock in the circulating supply introduced by the new allocation.

In order to achieve all the goals above, the following table shows how the new tokens will be allocated and the final overall allocations:

|  | **Current Allocation** | **New tokens** | **Final Allocation** | **Final Allocation (%)** |
|---|:---:|:---:|:---:|:---:|
| Burned | 140 | 160 | 300 | 15% |
| Team + Advisors | 251 | 0 | 251 | 13% |
| Other token holders | 457 | 0 | 457 | 23% |
| Ecosystem | 110 | 390 | 500 | 25% |
| Staking Program Support | 0 | 150 | 150 | 7% |
| Treasury | 42 | 250 | 292 | 15% |
| Public goods | 0 | 50 | 50 | 2% |

*Note: the category 'Other token holders' includes the Seed rounds, Option Holders, and token sales.*

## QRDO circulating supply

### Current supply dynamics

Currently, QRDO has a single source of variations in its circulating supply - vesting. In particular, the network does not have any staking/locking mechanics, there are no algorithm-controlled burns and the token is not minted. 

From the total available supply (the 860M tokens), there are approximately 339M tokens that have already vested as of June 2023 and thus constitute the current circulating supply. The figure below shows the vesting schedules from January 2023 to the middle of 2026.

<div style="text-align:center">
<img width="600" src="https://hackmd.io/_uploads/ryMZrphSh.png">
<br/>
<br/>
</div>

All the allocation groups still vesting are expected to be fully vested by 2026, with a linear vesting.

Since there are no sources of supply outflow (burning or locking) and a steady source of supply inflow (vesting), Qredo is currently experiencing an inflationary token supply. The following plot shows the supply inflation rates expected from the current vesting schedules and the current token allocation (i.e. supply inflation $=$ tokens vesting at time $t$ divided by the circulating supply at time $t$).

<div style="text-align:center">
<img width="600" src="https://hackmd.io/_uploads/rkhMlxBL2.png">
<br/>
<br/>
</div>


### Supply dynamics after tokenomics update

After the tokenomics update, there will be new token mechanisms that will complicate slightly the circulating supply dynamics. Concretely, the introduction of the Staking Model will add locking and release dynamics that will depend on the sentiment of Stakers and Validators and network growth. 

In addition, the two new Fee Models will introduce token burning that will depend on protocol fees (and thus protocol usage) and will introduce more locking and release dynamics that will be controlled by the payment of service fees into the Ecosystem Fund by Clients and the rewards released by the protocol to pay Validators and Stakers.

Of course, vesting will continue both from the current allocation and the new allocation. We should also note that the Ecosystem fund will have an accelerated vesting when the new tokenomics are introduced. The goal is to have the Ecosystem fund fully available on day zero.

In summary, we will have the following source of changes in circulating supply:

**Supply Inflows:** *(i.e. increases in circulating supply)*

- Vesting:
    - Linear vesting from the previous allocations to the team, advisors, investors, seed rounds, and the treasury.
    - Exponential decay vesting from the Staking Program Support fund.
- Locking releases:
    - Stakers participating in the Federated Proof-of-Stake consensus model (Staking Model). When they unstake their tokens, they stop participating and receiving rewards.
    - Service fees distribution from the Ecosystem Fund

**Supply Outflows:** *(i.e. decreases in circulating supply)*

- Burning from protocol fees
- Locking:
    - Stakers participating in the Federated Proof-of-Stake consensus (Staking Model). When they stake their tokens, they begin participating and receiving rewards.
    - Service fees tipped into the Ecosystem Fund


### Supply dynamics forecast

In this subsection, we show the results obtained from a simulation of the circulating supply for Qredo under the new tokenomics design. The simulation uses a simplified model (MechaQredo) coupled with a set of scenarios that encode user behavior and sentiment. 

Concretely, we design scenarios across the following axis:

- Token Price: This axis models varying scenarios for the token price.
- Network Usage: This dimension refers to different levels of network usage in terms of number of transactions and service fees generated in USD.
- Staking sentiment: This axis represents varying levels of token locking and releasing due to participants’ decisions within the Staking Mechanism.

For each axis, we define 3 scenarios - pessimistic, base, and optimistic. Then, we simulate MechaQredo's inputs under each scenario and axis independently and we run the MechaQredo simulation for each scenario combination. For more information on MechaQredo and the scenarios design, you can check the [dedicated report](/5EBNVwwLRBuhXy9wW4oTiw).

We should note that the results showcased here were obtained with the final parameters we proposed for the design. These parameters were obtained after running a full sweep of various possible parameter values. The full analysis can be consulted in its [report](/CBD_V8E5RzOf7oTSF-MnCQ).

When we look at the circulating supply for QRDO, there will be two separate phases for the proposed tokenomics update, namely, at the start of day zero (i.e. when the new tokenomics are introduced), and after day zero.

At the start of day zero, there will be a large shift in the circulating supply. Assuming that the circulating supply before day zero was at the current level (as of June 2023), we expect the circulating supply to grow from 339M to an average of 639M. The increase in 300M tokens is the result of the following token flows:

- Accelerated vesting from Ecosystem Fund: +55M tokens
- New allocation to funds without vesting (i.e. all except the Staking Program Support): +850M tokens
- Locking of the entire Ecosystem fund: -445M tokens
- Discretionary token burn from new allocation: -160M tokens

After this significant change, the circulating supply stabilizes and we can observe how the different mechanisms respond to the different scenarios. We can observe this in the figures below, which show the circulating supply trajectories over a 3-year period, under the designed scenarios. The combined scenario corresponds to the case when all three axis (token price, network usage and staking sentiment) have the same scenario. Note that each plot shows the average and standard deviation for each scenario.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/rJqC5nqYh.png"><img width="50%" src="https://hackmd.io/_uploads/H1-Jjh5Yh.png">
<img width="50%" src="https://hackmd.io/_uploads/SJPkih9th.png"><img width="50%" src="https://hackmd.io/_uploads/rJrBCt5F3.png">

**Figure 2:** Circulating Supply Forecast by Scenario - estimated with MechaQredo
<br/>
<br/>
</div>


Main takeways:

- Token price has a balancing effect on circulating supply. Low token prices lead to lower circulating supply, which should provide a balancing effect on price. This is mostly due to the service fees tipping mechanism - with lower token prices, the same USD amount of service fees results in more QRDO tokens being bought and locked into the Ecosystem Fund.
- Network usage is aligned with supply dynamics. Concretely, higher usage means more transactions being executed and more service fees collected. More transactions mean more tokens being burned from protocol fees while more service fees mean more tokens being bought and locked into the Ecosystem Fund. Both these impacts lead to lower circulating supplies.
- Staking sentiment also aligns with supply dynamics. When participants stake more (and unstake less), the total tokens locked within the Staking mechanism increases, which leads to lower a circulating supply.

Now let's look at supply inflation. In the plots below, we show the daily and yearly supply inflation rates for the combined scenarios.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/BksDk5cKn.png"><img width="50%" src="https://hackmd.io/_uploads/SJqfy9qtn.png">

**Figure 2:** Inflation rates by combined scenario - estimated with MechaQredo
<br/>
<br/>
</div>

Main takeaways:

- After the shock experienced at the start of day zero,  supply inflation rates are in line with the rates expected without the tokenomics update. This occurs because the "legacy" vesting schedules (e.g. Team, Seed rounds, etc.) are the most significant component impacting daily changes in circulating supply.
- Daily inflation rates decrease significantly once the legacy vesting schedules stop (end of 2025). After this date, inflation rates become mostly driven by network growth (usage and staking sentiment) and token price.
- The supply inflation rates decrease with time. The pessimistic scenario is the one that experiences the steeper fall due to the fall in token price and the consequent increase in tokens locked in the Ecosystem fund. In this scenario, the network becomes deflationary after 3 years. In the other scenarios, inflation rates are close to zero.
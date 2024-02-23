# Qredo tokenomics redesign - Final report

#### Maria Silva and Juan P.M. Cianci, CryptoEconLab, July 2023

The Qredo Network is a decentralized custody platform designed to offer businesses and investors a secure and efficient way to manage digital assets. 

Qredo is currently going through a transaction phase. In 2021, they launched their token (QRDO), and, since then, they have been working on a set of features to improve its usability and increase decentralization. Concretely, the network aims to evolve across three main axes:

- **A1**. Increased decentralization through a Federated Proof-of-Stake consensus system (and, later on, Delegated Proof-of-Stake). 
- **A2**. Enhanced the role of QRDO as Qredo's utility token.
- **A3**. More transparency and community engagement through open governance.

Ultimately, their goal is to execute the vision of a truly decentralized custody network and to put the QRDO token at the center of Qredo's product. However, to achieve this vision, Qredo's underlying tokenomics and its native token need to adapt, which is the reason why the Qredo Team partnered with CryptoEconLab to revamp the tokenomics of the Qredo network.

This collaboration was designed to encompass two main phases - the draft phase and the tuning and validation phase. The idea was to provide the general framework for the new tokenomics earlier and collect feedback before delving into the details of tunning and validating its key parameters.

This report provides an overview of the results obtained in the second phase and puts forward a proposal for the key tokenomic parameters that were left undefined after the first phase. For an overview of the first phase of the project, you can read the [intermediate report](/7hrz1PFOTyqr6Bohk0roFg).

We start by presenting the changes to the token allocations and vesting schedules in [Section 1](#1-New-token-allocation). Then, in [Section 2](#2-Setting-key-tokenomic-paramaters), we explain the methodology we used to set the main tokenomic parameters and discuss key findings. Lastly, in [Section 3](#3-Qredo-economics-after-the-tokenomics-update), we examine how the new design is expected to Qredo's economy under various conditions and discuss whether the new design meets the high-level goals of sustainability and token utility.

As we did in the intermediate report, this final report serves as a summary of a set of longer reports that go deeper into the technical aspects and the analysis. As such, whenever relevant, we will link to the related full reports.  Alternatively, all reports can be found in the menu located on the left.


## 1. New token allocation

This section is based on [this dedicated report](/3Xwe-CZ8TPiC80Fg2r5qtQ).

When the QRDO token was launched, its total token supply was set at 2 billion. At the time, 1 billion was allocated, while the remaining 1 billion was set apart for future allocations. A key outcome of this second phase of the project was to define how the second billion should be allocated and their vesting schedules. Based on the current design proposed, the new allocation has to support the following uses:

- Create a new fund named **Public Goods**. This fund will be used to cover incentive programs for network participants, with a focus on user adoption.
- Increase the size of the **Ecosystem fund**. This fund will have a key role in the Qredo Protocol going forward and, as such, needs to have a larger allocation. More precisely, this fund will serve two key roles: firstly it will cover the protocol fees of the protocol-funded transactions; secondly, it will be the repository of the service fees being tipped to the network and will control how these funds are released to pay the rewards of the Staking Model (for both Validators and Stakers). These rewards will depend on the performance and growth of Qredo, thus aligning the participants of the Staking Model with the long-term goals of the network.
- Create a new fund to support the Staking Model for federated Proof-of-Stake, named the **Staking Program Support fund**. This fund is aimed at supporting the rewards of the Staking Model by providing a predictable source of rewards.
- Increase the **Treasury**, which is the fund dedicated to the development and growth of the Qredo ecosystem. The scope includes funding partner programs, grants, private sales, and allocations to market makers and exchanges.
- Do an **additional token burn** to soften the shock in the circulating supply introduced by the new allocation.

The following table summarises the new token allocations and how they impact the overall allocations of the 2 billion tokens. The units of the table below are millions of QRDO tokens:

|  | **Current Allocation** | **New tokens** | **Final Allocation** | **Final Allocation (%)** |
|---|:---:|:---:|:---:|:---:|
| Burned | 140 | 160 | 300 | 15% |
| Team & Advisors | 251 | 0 | 251 | 13% |
| Other token holders | 457 | 0 | 457 | 23% |
| Ecosystem | 110 | 390 | 500 | 25% |
| Staking Program Support | 0 | 150 | 150 | 7% |
| Treasury | 42 | 250 | 292 | 15% |
| Public goods | 0 | 50 | 50 | 2% |

*Note: the category 'Other token holders' includes the Seed rounds, Option Holders, and token sales.*

## 2. Setting key tokenomic paramaters

During the first phase of this project, we proposed a set of new tokenomic mechanisms, including two new [Fee Models](/v5r6y8a_TE6NtouVHmPnmA) aimed at increasing token utility and a [Staking Model](/Xh_biTXNS8mpG5M_rMfKbg) to support Qredo's introduction of a federated Proof-of-Stake consensus. 

There, we defined the broad strokes of how the mechanisms would work and left some specific parameters undefined. Our strategy to determine these tokenomics parameters was to build a simplified model of the Qredo economy (MechaQredo) and run two separate analyses:

- A sensitivity analysis, where we analyzed how small adjustments in each tokenomic parameter affected a set of economic metrics and the rate at which such changes occur.  Here we used a statistical approach to estimate the marginal dependences and the sensitivity of each individual parameter on the economic metrics.
- A Monte Carlo simulation analysis, where we ran various Monte Carlo simulations based on the MechaQredo model for different combinations of parameters and scenarios, and we analyzed the tradeoffs of each parameter when considering key economic metrics such as circulating supply, supply inflation, and profitability of the Staking Model. 

In the next subsections, we will detail the results of each analysis. However, before doing that, we need to provide an overview of the MechaQredo model and the scenarios we used in both analyses.


### 2.1 MechaQredo and scenarios

This subsection is based on [this dedicated report](/5EBNVwwLRBuhXy9wW4oTiw).

**MechaQredo**

MechaQredo is a mechanistic model that estimates a set of metrics about the Qredo economy. The model receives two types of inputs, the tokenomic parameters and the "market" inputs that encode user behavior, adoption, and the current status of the network.

Given a **fixed** set of inputs, MechaQredo always outputs the same estimates. In other words, MechaQredo does not introduce any source of randomness or uncertainty, leaving us with the flexibility to encode it in the "market" inputs.

MechaQredo implements a simplified version of the new Qredo economy assuming the proposed Fee Models, the Staking Model, and the new token allocations are introduced at the same time. Concretely, it estimates the daily trajectories of the four components that contribute to the circulating supply of QRDO (tokens vested, burned, locked, and released) and the daily profitability of the Staking Model (for both Validators and Stakers))

The model uses the follwoing simplifying assumptions:

- Metrics are computed daily, with staking rewards and decisions made once per day.
- The Ecosystem Fund at step t+1 depends only on the token flows from step t.
- The analysis only considers the  Federated Proof-of-Stake model, as the transition towards the fully delegated system will take a few years.
- Service fees are paid in USD and we apply a fixed slippage when exchanging USD to QRDO.
- Circulating supply and token price are modeled independently.
- Staking inflows and outflows are not impacted by circulating supply or token price.

**Scenarios**

Since MechaQredo is fully deterministic, we need to encode the uncertainty of market conditions and adoption through market inputs. As we explained before, the analysis uses a [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation approach, which involves evaluating the deterministic model multiple times using sets of random numbers within a range of its inputs. Since allowing the full range of inputs would be untractable, we designed scenarios to cover possible trajectories of the market inputs.

Concretely, we built scenarios across three independent dimensions:

- Token Price: This dimension models varying scenarios for the token price.
- Network Usage: This dimension refers to different levels of network usage in terms of the number of transactions and service fees generated in USD.
- Staking sentiment: This dimension represents varying levels of token locking and releasing due to participants’ decisions within the Staking Mechanism.

For each dimension, we created 3 scenarios - pessimistic, base, and optimistic. For context, the base scenario represents a situation where adoption and usage evolves acording to current trends and token price remains at the current values (i.e. token price with a constant trend at its current price, network usage consistent with the current status plus some mild growth assumptions, and a stable TVL). Then, the pessimistic and optimistic scenarios create worse and better versions of the base scenario, respectively.

Since each dimension is assumed to be independent, we consider all possible scenario combinations across the 3 dimensions, which leads to 27 possible scenarios.

Figure 2.1 shows the market inputs and how they vary based on the scenarios of their corrrespondent dimension. Note that each plot encodes the average of each metric by day in a solid line and the standard deviation as a transparent band around the line. This is done since we are using a Monte Carlo method, which means that we sample multiple trajectories for each market input, run MechaQredo on each of these trajectories, and then estimate the average output response, as well as its standard deviation.


<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/SkIFiYCqh.png"><img width="50%" src="https://hackmd.io/_uploads/rJUtjzaFn.png">
<img width="50%" src="https://hackmd.io/_uploads/rJ8_jfaKh.png"><img width="50%" src="https://hackmd.io/_uploads/rkhuoGaF2.png">
<img width="50%" src="https://hackmd.io/_uploads/r1gyafat2.png">
    
**Figure 2.1:** Market inputs by scenario. *Note: validator counts does not depent on the scenarios!*
<br/>
<br/>
</div>

:::info
:information_source: All scenarios were designed to test the tokenomics mechanisms. Therefore, they do not represent actual predictions of future events nor do they reflect the views of our team or any associated parties. 
:::

### 2.2 Sensitivity analysis

This subsection is based on [this dedicated report](/4k7Eg5vaRoun78RnIT6sLA).

**Methodology**

This analysis focuses on understanding how certain input tokenomic parameters affect some given output quantities. In particular, we will focus on the effects that the tipping rate, the protocol fee rate, the validator reward share, the staking rewards vesting decay, and the three paramaters of the release function ($a$, $b$, and $r_\text{max}$) have on critical output quantities, such as circulating supply, yearly inflation, validator rewards, Ecosystem fund balance, staking rewards, and APR.

For each combination of input-output, we examined two key measures, namely:

- *Q1 - Marginal Dependence:* This measure investigates how output changes as a function of a specific input parameter while other parameters are averaged. This measure indicates what happens to an output when you tweak a specific input while keeping everything else constant.
- *Q2 - Sensitivity:* This measure identifies the rate of change of the output parameter concerning a specific input parameter. It shows how swiftly an output is changing relative to a specific input.

To estimate both measures, we ran multiples iterations of MechaQredo using the randomness provided by the base combined scenario. In other words, we assumed that token prices, staking sentiment and network usage followed their base scenarios.

**Summary of findings**

Our results are concisely represented in the table below. The terms Positive (High), Positive (Small), Negative (High), Negative (Small) represent the direction (positive or negative) and the degree (high or small) of the influence an input parameter has on an output quantity.

| Input | Circulating Supply | Yearly Inflation | Validator Rewards |  Staking Rewards |  Ecosystem Fund |  Staker APY |
|---|---|---|---|---|---|---|
| Tipping rate | Negative (Small) | Negative (Small) | -- | -- | Negative (Small) | Negative (Small) |
| Protocol fee rate | Negative (Small) | Negative (Small) | -- | -- | -- | -- |
| Validator reward share | -- | -- | Positive (High) | Negative (High) | -- | -- |
| Max rate | Positive (High) | Positive (High) | Positive (High) | Positive (High) | Positive (High) | Positive (High) |
| Release rate 'a' | Negative (High) | Negative (High) | Negative (High) | Negative (High) | Positive (High) | Negative (High) |
| Parameter 'b' | Positive (Small) | Positive (Small) | Positive (High) | Positive (High) | Positive (High) | Positive (Small) |
| Staking rewards vesting decay | Positive (High for small values, then negligible) | Positive (High for small values, then negligible) | Positive (High for small values, then negligible) | Positive (High for small values, then negligible) | -- | -- |


### 2.3 Monte Carlo simulation analysis

This subsection is based on [this dedicated report](/CBD_V8E5RzOf7oTSF-MnCQ).

**Methodology**

In this analysis, we ran MechaQredo with all the scenario combinations and with a set of combinations of tokenomic parameters. Concretely, we used the following values of tokenomic parameters: 

* Fee models:
    * Tipping rate: 0.2, 0.3, or 0.4
    * Protocol fee rate: 1 QRDO
* Staking model:
    * Minimum stake amount: 2500 QRDO
    * Minimum stake duration: 4 weeks (or 7 x 4 days)
    * Validator reward share: 0.7, 0.8, or 0.9
    * Vesting decay rate:  6, 4, or 2 years half-life
    * Release rate function:
        * $a$: 0.8 or 1
        * $b$: 0.5
        * $r_\text{max}$: 0.0006 or 0.0008
* New token allocation:
    * Discretionary burning: 160M QRDO
    * Ecosystem fund: 390M QRDO
    * Staking Program Support fund: 150M QRDO
    * Treasury: 250M QRDO
    * Public goods fund: 50M QRDO

Some parameters were already fixed, such as the new token allocations. However, for the rest, we were left with $3\times3\times3\times2\times2 = 108$ unique parameter combinations. Recall that we run each combination with the $27$ scenarios, leading to $2916$ Monte Carlo simulations, each with a given number of samples.

**Summary of findings**

- The scenarios have a significant impact on circulating supply:
    - Lower token prices lead to lower circulating supply, as more tokens are bought and locked into the Ecosystem Fund due to the service fees tipping mechanism.
    - Higher network usage and staking sentiment both lead to lower circulating supply, as more transactions are executed, more service fees are collected, and more tokens are staked, resulting in more tokens being burned and locked.
- The scenarios also impact inflation rates:
    - Inflation rates decrease with time in all scenarios, with staking sentiment having the highest impact on lowering inflation rates.
    - Token price has an inverse relationship with inflation rates, as lower token prices lead to more tokens being locked in the Ecosystem Fund.
- Looking at profitability of the Staking Model:
    - Staking sentiment has a significant impact on Staker's profitability, with higher TVL leading to lower APR and weekly rewards.
    - Token price and network usage do not have a significant impact on Staker's QRDO-denominated profitability.
    - Validator profitability is influenced by staking sentiment, with higher TVL's leading to higher profits.
    - Validator's QRDO-denominated rewards decrease with time due to the assumption of a steady growth of validators and the fact that the total available rewards do not grow proportionally to the number to number of validators.
    - Token price has a significant impact on validator profit, with higher prices leading to higher profits. Recall that, for validators, we consider the USD profits and thus the metric is expected to be influenced by the token price scenarios.
- As for the Ecosystem fund:
    - The long-term balance of the Ecosystem fund is influenced by token price, usage, and staking sentiment.
    - Lower token prices and higher network usage lead to more tokens being locked in the Ecosystem Fund, while higher TVL leads to higher release rates and lower fund balances.
    - The burning of protocol fees is a small component of the net flows in the Ecosystem Fund. Tipped service fee and released rewards for Stakers and Validators are the components that most impact the net flows in the Ecosystem Fund.
- Now, if we focus on each individual parameter:
    - The tipping rate does not significantly affect Staker and Validator profitability but impacts the long-term balance of the Ecosystem Fund. Increasing the tipping rate by 10 percentage points locks an additional 10 million tokens in the Ecosystem Fund, reducing supply inflation by 1 percentage point.
    - The validator reward share mainly affects Staker and Validator profitability, with higher shares benefiting Validators at the expense of Stakers.
    - The vesting decay rate influences supply inflation rates and profitability, with shorter half-lives leading to higher inflation and increased profitability.
    - Release rate function parameters impact the distribution of rewards, with higher rates increasing profitability but also inflation and reducing the Ecosystem fund balance.


Based on the findings, we made the following recomentations:

- Set the tipping rate to 30%. This value is low enough to support the operation of Qredo LLC, while maintaining an appropriate flow of funds locked in the Ecosystem Fund.
- Set the validator reward share to 70% to maintain strong APRs for Stakers while ensuring sufficient profits for Validators.
- Set the vesting decay rate to a 2-year half-life: $\frac{\ln{2}}{2 \times 365}.$ This rate is not too aggressive to supply inflation rates while allowing for a good complement to staking rewards.
- Use a release rate function with a maximum rate $r_\text{max}$ of 0.0006 and an exponent $a$ of 0.8 to provide sustainable rewards for Stakers and Validators while maintaining the balance of the Ecosystem Fund.


## 3. Qredo economics after the tokenomics update

This section is based on a [subsection](/CBD_V8E5RzOf7oTSF-MnCQ#Simulations-with-final-paramaters) of the Monte Carlo analysis report.


**Methodology**

In this final analysis, we ran a new set of Monte Carlo simulations using the same scenarios, but now we use the proposed parameters that resulted from our previous analysis. Here, we focused on key metrics that allowed us to assess how the new design would impact the sustainability of the network and the utility of the token.

We conducted a simulation for 3 years, using the same scenarios as before (token price, network usage, and staking sentiment). The tokenomic parameters we employed are as follows:

* Fee models:
    * Tipping rate: 0.3
    * Protocol fee rate: 1 QRDO
* Staking model:
    * Minimum stake amount: 2500 QRDO
    * Minimum stake duration: 4 weeks (or 7 x 4 days)
    * Validator reward share: 0.7
    * Vesting decay rate: 2-years half-life (i.e. rate $=\frac{\ln{2}}{2 \times 365}$)
    * Release rate function:
        * $a$: 0.8
        * $b$: 0.5
        * $r_\text{max}$: 0.0006
* New token allocation:
    * Discretionary burning: 160M QRDO
    * Ecosystem fund: 390M QRDO
    * Staking Program Support fund: 150M QRDO
    * Treasury: 250M QRDO
    * Public goods fund: 50M QRDO


The plots in this section display the average and standard deviations of each metric. Note that the variations observed are due to the uncertainty of each scenario.


**Summary of findings**

- We expect a large shift in the circulating supply right after the new tokenomics are introduced. Concretly, we expect the circulating supply to grow from 339M to 639M, depending on the scenario. This is the result of the accelerated vesting from Ecosystem Fund and the new token allocations that vest immediatly. 
- From here, circulating supply stabilizes and continues to grow for the following 2 years. Supply growth rates decelerate significantly in all scenarios at the start of 2026. This is the time when legacy vesting schedules finish.
- In all scenarios, daily inflation rates are lower than 0.9%, which is below the 1.5% currently experienced by the network.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/rJrBCt5F3.png"><img width="50%" src="https://hackmd.io/_uploads/BksDk5cKn.png">

**Figure 3.1:** Circulating supply and inflation rate by combined scenario
<br/>
<br/>
</div>

- To align token supply with network growth, the tokenomics redesign introduced three mechanisms:
    - **Service fee model**. A percentage of service fees collected by Qredo is converted from USD to QRDO and locked in the Ecosystem fund. This increases tokens locked, reducing circulating supply and providing more tokens for Validators and Stakers.
    - **Protocol fee model**. Transactions in the Qredo network incur a fixed fee that is burned, reducing circulating supply. This mechanism has a minor impact compared to others.
    - **Release function for the Ecosystem fund**. The rate at which tokens are released from the fund to pay Validators and Stakers depends on TVL and the number of validators. This ensures more tokens can be released as the network grows.
- Looking again at circulating supply and inflation, we see how these mechanisms work to soften the scenarios, creating a balancing effect on the economics of the network.
    - In the pessimistic combined scenario, the daily inflation rates are slightly lower, and the circulating supply grows slower than in the other scenarios. After the legacy vesting schedules finish, the trend in circulating supply inverts, and its drops are sharper than the drops observed in the other two scenarios.
    - We also see this effect in the inflows and outflows of the Ecosystem fund, with the pessimistic scenario leading at the same time with more tokens locked and fewer tokens released.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/rkVPXWit2.png"><img width="50%" src="https://hackmd.io/_uploads/SyALXZit2.png">

**Figure 3.2:** Inflows and outflows of the Ecosystem fund by combined scenario
<br/>
<br/>
</div>

- Higher network usage and lower token prices increase APR for Stakers and QRDO-denominated rewards for Validators, creating a balancing effect on network economics.
- In all scenarios, the Stakers receive weekly QRDO rewards exceeding the protocol fees required to claim them.
- The average APR starts relatively high, ranging from 35% to 58%. Then, depending on the scenario, it follows separate trajectories (which mostly depend on the TVL).
- Staker average APR decreases as TVL grows but stays between 5% and 15% when the TVL rate is higher than 30%. Note that TVL rate is the TVL divided by circulating supply.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/Sy2WMNTt2.png"><img width="50%" src="https://hackmd.io/_uploads/HyXVNpctn.png">

**Figure 3.3:** Staker APR - by combined scenario and relationship with TVL
<br/>
<br/>
</div>

- Daily Validator profits vary significantly across scenarios (with token price impacting the most), with the optimistic scenario showing consistent average daily profits of around $1900.
- In the base token scenario, the majority of simulation trajectories allow the average validator to generate a profit. When staking sentiment is at its lowest, the average profit drops to \$9 per day, while the other two staking scenarios generate profits of around \$300 per day.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/SJrc66qKn.png"><img width="50%" src="https://hackmd.io/_uploads/SyHLaaqKn.png">

**Figure 3.4:** Validator daily profit for different scenarios
<br/>
<br/>
</div>
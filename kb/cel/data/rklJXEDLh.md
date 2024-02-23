# Model specifications

#### Maria Silva and Juan P.M. Cianci, CryptoEconLab, July 2023

In this document, we detail the technical specifications of the model we used to tune and test Qredo's tokenomic redesign. The document has two main parts. 

First, we describe a mechanistic model, MechaQredo, that estimates a set of tokenomic metrics for the Qredo economy (e.g. circulating supply, Validator profit, Staker APR, etc.). The model receives two types of inputs, the tokenomic parameters we wish to tune and "market" inputs that encode user behavior, adoption and the current status of the network.

The second part is focused on the inputs to the mechanistic model. Particularly, we describe how we model and/or estimate the probabilistic inputs that encode user behavior and adoption and we detail the different scenarios that we will consider in the simulation. We also describe the parameters we are tuning and any constraints they may be subjected to.

This model will then be used in the context of Monte-Carlo simulations to (a) investigate the effects of the input parameters on the output quantities of interest (i.e., circulating supply, APR, etc) and (b) choose a set of tokenomic parameters that are aligned with Qredo's mision and best interest. 

Before going into the detail, it is important to highlight that the model utilises some assumptions to make the analysis feasible.

#### Model assumptions:

- Forecasting is done daily. This means that each forecasting step corresponds to a day and the forecasted metrics correspond to the value we expect to see at the end of that day. We also assume that staking rewards and the decisions to stake or unstake occur once per day.
- To avoid circular dependencies and simplify calculation, we assume that the Ecosystem Fund at step $t+1$ depends only on the tokens flows from step $t$. This is the same as saying that, in any given simulation step, tokens in the Ecosystem Fund are released before new tokens being locked. 
- All the new mechanisms and changes proposed in the tokenomics update are applied at the same time at the start of the simulation (day zero). This includes accelerated vesting, additional burning, the new fee models and the staking model.
- We only consider the network in the Federated Proof-of-Stake. In other words, even though we expect the network to transition to Delegated Proof-of-Stake in the medium term, we focus the analysis on the Federated Proof-of-Stake.
- We assume that circulating supply does not impact token price, as both variables are modeled independently.
- - We assume that the staking inflows and outflows are not impacted by either circulating supply or the token price, as the variables are modeled independently
- The service fees are paid in Dollars. Furthermore, the conversion between USD and QRDO occurs with some fixed slippage $\gamma\in[0,1)$. That means that, given a QRDO price $P(t)$, each dollar converted to QRDO  results in $(1-\gamma)P(t)^{-1}$ QRDO tokens. 
- We also assume service fees and number of transactions are independent of all other metrics, such as token price, staking flows and circulating supply.
- To simplify the simulation, we are ignoring the bonding mechanism for Stakers. This means that if a participant wants to unlock their staked tokens, the tokens will be immediately released into the circulating supply. We should note that, in other protocols, the unlocking mechanism ranges from 0 to 90 days.

## 1. MechaQredo

MechaQredo contains three main groups variables:

1. [Circulating supply variables](#Circulating-supply-variables)
2. [Fee model variables](#Fee-model-variables)
3. [Staking model variables](#Staking-model-variables)

We will cover each of these variables and how they are computed in the following subsections. But before, we will to list the assumptions underlying MechaQredo and the notation used throughout this section.

### Notation

- $t$: forecasting step (e.g. $t=0$ is day 0 and $t=1$ is day 1).
- $C(t)$: circulating supply at step $t$.
- $L(t)$: total locked tokens at step $t$.
- $L^\text{in}(t)$: number of new tokens that were locked during step $t$.
- $L^\text{out}(t)$: number of tokens that were released from locking during step $t$.
- $V(t)$: number of tokens that vested during step $t$.
- $B(t)$: number of tokens that were burned during step $t$
- $N_\text{trx}(t)$: number of transactions executed in the network during step $t$. 
- $A_\text{fees}(t)$: the amount of USD generated in service fees during step $t$.
- $f$: protocol fee per transaction. This is a tokenomic parameter.
- $\sigma$: percentage of protocol-funded transactions (i.e. transaction where the protocol fees are not paid by the user directly).
- $\gamma$: slippage when converting USD(C/T) to QRDO.
-  $\mathsf{StakingProgramSupportFund}$: number of tokens allocated to the Staking Model supporting Qredo's federated Proof-of-Stake syste. This is a tokenomic parameter.
- $\alpha(t)$: vesting function for tokens allocated to the $\mathsf{StakingProgramSupportFund}$. This function contains one tokenomic parameter, which we will discuss afterwards.
- $\mathsf{EcosystemFund}(t)$: number of tokens locked in the Ecosystem Fund at step $t$.
- $r(t)$: release function rate for the tokens locked in the Ecosystem Fund. This function contains three tokenomic parameters, which we will discuss afterwards.
- $\theta$: the tipping rate, which is the percentage of service fees that Qredo LLC gives back to the network. This is a tokenomic parameter.
- $P(t)$: price of QRDO at step $t$.
- $N_\text{val}(t)$: Number of validators active at step $t$.


### Circulating supply variables

One of the key areas of our analysis is to understand how the tokenomics update will impact the token's circulation supply (and its key components). 

The circulating supply of QRDO at any step $t\geq 1$ is the circulating supply from step $t-1$ plus the token inflows (vesting and locking releases) minus the token outflows (locking and burning). Concretely:

$$
C(t) = 
    C(t-1) 
    + V(t) 
    + L^\text{out}(t) 
    - L^\text{in}(t) 
    - B(t)
$$

Now, let's look at each of the components of the circulating supply.

#### Tokens burned

In Qredo, tokens are burned to cover protocol fees, which are defined as a fixed fee per transaction. In addition, we are considering the option of burning a discretionary amount of tokens to fix a potential supply imbalance. Thus, the number of tokens burned at step $t$ is given by:

$$
B(t) 
    = B_\text{fee}(t) + B_\text{extra}(t) 
    = f \cdot N_\text{trx}(t) + B_\text{extra}(t) 
$$

We should recall that part of the tokens in $B_\text{fee}(t)$ come from users (in self-funded transactions) and another part comes from the Ecosystem Fund (in protocol-funded transactions). 

As for the $B_\text{extra}(t)$, it is a tokenomic parameter that we will set during the simulation. However, we expect this function to be mostly zero, with all the additional burning hapenning at step $t=0$.

#### Tokens vested

When modeling tokens vested, $V(t)$, we need to consider two separate sources of vesting:
- Current vesting schedules, resulting in a vesting function $V_\text{curr}(t)$. These are the schedules of the first 1B tokens allocated back in 2021 and which we cannot change. In particular, this group includes the allocations to the team, treasury fund, advisors, option holders, seed round investors, and private sales.
- New Vesting Schedules, resulting in a vesting function $V_\text{new}(t)$. These are the schedules that will be defined in this tokenomics update. Concretely, this includes the entire second billion tokens not yet allocated and the updated schedules from the Ecosystem fund (which is in scope of being reviewed).


$V_\text{curr}(t)$ is fully defined and does not depend on any other variables. Thus, we will take this variable as a fixed input. On the other hand, $V_\text{new}(t)$ depends on vesting schedules that we need to tune during this analysis. Therefore, this variable will be the sum of the following components:

- $V_\text{stake}(t)$: Vesting coming from the token allocation to kickstart the Staking Model in the Federated PoS consensus. This component is defined as $V_\text{stake}(t) = \alpha(t) \cdot \mathsf{StakingProgramSupportFund}$, with both factors being tokenomic parameters to be tuned during the simulation.
- $V_\text{ecosystem}$: accelerated vesting from the already established Ecosystem fund that will be applied at $t=0$. This is an input we will extract from the current known vesting schedules.
- $V_\text{treasuryRefresh}$: vesting from the refresh allocation assigned to the Treasure. The refresh will be fully vested at $t=0$. The size of the refresh is a tokenomic parameters to be tuned during the simulation.
- $V_\text{publicGoods}$: vesting from the new allocation assigned to the Public goods fund. The new allocation will be fully vested at $t=0$. The size of the new allocation is a tokenomic parameters to be tuned during the simulation.


#### Tokens locked

In Qredo, locking occurs in three situations:

- When service fees tipped to the network are sent to the Ecosystem Fund. We will refer to these locked tokens as $L_\text{fee}^\text{in}(t)$.
- When users stake tokens to participate in a federated Proof-of-Stake consensus system. We will refer to these locked tokens as $L_\text{stake}^\text{in}(t)$.
- At the start of the simulation, when the entirety of the tokens in Ecosystem Fund are locked. e will refer to these locked tokens as $L_\text{ecosystem}$.

Thefore, we can define the number of new tokens locked during step $t$ as:

$$
L^\text{in}(0) = 
    L_\text{fee}^\text{in}(0) 
    + L_\text{stake}^\text{in}(0)
    +L_\text{ecosystem}
$$

$$
L^\text{in}(t) = 
    L_\text{fee}^\text{in}(t) 
    + L_\text{stake}^\text{in}(t), \  t>0
$$

$L_\text{fee}^\text{in}(t)$ depends on the amount of USD generated in service fees ($A_\text{fees}(t)$), the tipping rate ($\theta$), which is the percentage of service fees that Qredo LLC gives back to the network, and the Dollar price of QRDO ($P(t)$). Thus, the number of tokens locked due to service fees during step $t$ is defined as:

$$
L_\text{fee}^\text{in}(t) = 
    \frac{\theta \cdot A_\text{fees}(t)}{P(t)}(1-\gamma)
$$

$\theta$ is a tokenomic parameter which will be tuned during the analysis. $A_\text{fees}(t)$, $\gamma$ and $P(t)$ are all inputs to the model and they will be further discussed in [Section 2](#2-Model-inputs-parameters-and-possible-scenarios).

$L_\text{stake}^\text{in}(t)$ encodes the new tokens being locked for staking and, as such, depends solely on the decisions of users to stake their tokens and participate in the consensus mechanism. Thus, this variable will be an input of this model. We will discuss how we will model this variable in [Section 2](#2-Model-inputs-parameters-and-possible-scenarios).

Finaly, $L_\text{ecosystem}$ can be taken from the token allocation.

#### Tokens released

In Qredo, tokens are released from locking in three cases:

- Tokens from the Ecosystem Fund are released to cover the protocol fees from protocol-funded transactions. Recall that these tokens will be immediately burned. We will refer to these tokens as $L_\text{burn}^\text{out}(t)$.
- Tokens from the Ecosystem Fund are released to pay Validators and Stakers for their role in the federated PoS consensus mechanism. We will refer to these tokens as $L_\text{fee}^\text{out}(t)$.
- Stakers release their locked tokens to stop participating in the federated PoS consensus mechanism. We will refer to these tokens as $L_\text{stake}^\text{out}(t)$.


Therefore, we can define the number of tokens released from locking during step $t$ as:

$$
L^\text{out}(t) = 
    L_\text{burn}^\text{out}(t)
    + L_\text{fee}^\text{out}(t)
    + L_\text{stake}^\text{out}(t)
$$

Since $L_\text{burn}^\text{out}(t)$ are only unlocked to cover the protocol fees that are not paid by protocol users, we can define it as:

$$
L_\text{burn}^\text{out}(t) = 
    \sigma \cdot B(t) = 
    \sigma \cdot f \cdot T(t)
$$

where $\sigma$ is percentage of protocol-funded transactions. This variable is an input of the model and thus will be further discussed in [Section 2](#2-Model-inputs-parameters-and-possible-scenarios).

On the other hand, the tokens used to pay Validators and Stakers are released according to the release rate function $r_\text{max}(t)$, which is a tokenomic parameter we will test during the simulation. Thus,

$$
L_\text{fee}^\text{out}(t) =
    r(t)\mathsf{EcosystemFund}(t)
$$

Note that the Ecosystem Fund has its own dynamics. Service fees tipped to the network are added to the fund while tokens released to cover staking rewards and protocol fees are removed from the fund. 

To avoid circular dependencies, we assume that the Ecosystem Fund at step $t+1$ depends only on the tokens flows from step $t$. This is the same as saying that, in any given simulation step, tokens in the Ecosystem Fund are released before new tokens being locked. Therefore:

$$
\mathsf{EcosystemFund}(t+1) = 
    \mathsf{EcosystemFund}(t)
    + L_\text{fee}^\text{in}(t)
    - L_\text{burn}^\text{out}(t)
    - L_\text{fee}^\text{out}(t)
$$

Finally, $L_\text{stake}^\text{out}(t)$ depends solely on the decisions of users to decrease their stake in the consensus mechanism. Thus, this variable will be an input of this model. We will discuss how we will model this variable in [Section 2](#2-Model-inputs-parameters-and-possible-scenarios).

#### Extra variables

Now that we have the full equation for QRDO circulating supply we can define two additional variables that are helpful to gauge the state of the token:

- **Daily supply inflation rate**: measures the rate of token supply increase each day. It is defined as $i(t) = \frac{C(t)-C(t-1)}{C(t-1)}$.
- **Yearly supply inflation rate**: measures the rate of token supply increase each year. It is defined as $I(t) = \frac{C(t)-C(t-365)}{C(t-365)}$.


### Fee model variables

To extract more information from the Fee Models Design, the simulation will need to track two additional variables. These variables can be easily derived from the equations we defined in the previous section:

- The number of tokens burned from protocol fees: $B_\text{fee}(t) = f \cdot N_\text{trx}(t)$
- The total amount of QRDO tipped to the network from service fees: $L_\text{fee}^\text{in}(t) = \theta(1-\gamma) \cdot A_\text{fees}(t)  P(t)^{-1}$

### Staking model variables

Besides the variables already defined in the circulating supply subsection, there are four more metrics related to the staking model we wish to compute during the simulation:

- Validators rewards
- Validator profit
- Stakers rewards
- Staker returns

#### Validators rewards

The total amount of QRDO tokens paid to Validators in step $t$ is defined as:

$$
R_{v}(t) = 
    \psi \cdot \mathsf{Tokens_{available}} =
    \psi \cdot \left(L_\text{fee}^\text{out}(t) + V_\text{stake}(t)\right)
$$

In other words, Validator received their share (which is encoded in the tokenomic parameter $\psi$) of all available tokens for distribution. The available tokens are the sum of the released tokens from the Ecosystem fund and the vested tokens from the Staking Program Support  Fund. 

#### Validator profit

For this metric, we will compute an average daily profit per validator. This means that we will take the total rewards allocated to validators ($R_{v}(t)$), divide it by the number of validators ($N_\text{val}(t)$) and subtract an estimate of the (per validator) daily operating costs ($\text{OpEx}_\text{val}$):

$$
\text{Profit}(t) = 
    \frac{R_{v}(t)}{N_\text{val}(t)}
    - \text{OpEx}_\text{val}
$$

The previous estimator assumes a fixed OpEx cost for all validators. This quantity is a model input and, as such, we will further defined in [Section 2](#2-Model-inputs-parameters-and-possible-scenarios). 

Note that here we are not considering traditional profitability metrics such as APY. The reason for this is that Validators in the fPoS system will not be required to stake tokens. Instead, they are bringing their expertise and trust while covering the operational costs of running the protocol. Thus, the profit after OpEx is the most meaningful metric for this case.

#### Stakers rewards

Similarly to Validators rewards, the total amount of QRDO tokens paid to Stakers in step $t$ is defined as:

$$
R_{s}(t) = 
    (1-\psi) \cdot \mathsf{Tokens_{available}} =
    (1-\psi) \cdot \left(L_\text{fee}^\text{out}(t) + V_\text{stake}(t)\right)
$$

#### Staker returns

For the Staker return, we will track the APR (i.e. anual percent return). For this, we use average rates based on the daily rate of return experienced at each simulation step $t$:

* Total value locked in staking: $L_\text{stake}(t) = \sum_{i=0}^t L_\text{stake}^\text{in}(i) - L_\text{stake}^\text{out}(i)$
* Daily rewards: $R_{s}(t)$
* Daily interest rate (simple): $r(t) = R_{s}(t) / L_\text{stake}(t)$
* Projected APR: $\text{APR} = 365 \cdot r(t)$

We should note that the APR is subject to change over a year as every day the interest rate changes based on changes in TVL and total rewards available.

Notice that the equation $r(t) = R_{s}(t) / L_\text{stake}(t)$ already gives some guidelines on the construction of the daily rewards function, $R_s(t)$. In particular, notice that if one were to fix such a quantity, while at the same time increasing $L_\text{stake}(t)$, this would result in a lower APY for the returns (as the interest rate becomes smaller). Thus, as the TVL (in staking) increase, so should $R_s(t)$. Furthermore, making $R_s(t)$ increase faster than $L_\text{stake}$ would create a sort of *positive sum game*, as in this case, everyone would benefit more from staking as TVL increases.


## 2. Model inputs, parameters, and possible scenarios


### Market inputs

We begin by describing the market inputs. Depending on the complexity of the chosen experiment, these inputs can be a constant, a deterministic function, or a stochastic process. There is a computational trade-off between these choices; while functions and stochastic processes are more flexible and able to represent a wider variety of scenarios, they are also more computationally expensive to simulate.


#### Circulating supply at $t=0$, $C(0)$

In the context of our dynamic system models, we'll need to establish initial conditions to facilitate proper simulations. One critical initial condition is the circulating supply at the onset of a simulation, denoted as circulating supply at time 0, $C(0)$. This value can be sourced from the current vesting schedule corresponding to any specific date.

#### QRDO Price in USD

We will rely upon the following assumption.

**A1**. *We assume that the price process $P(t)$ follows a so-called [Geometric Brownian Bronian Motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion) (GBM)*

A GBM is a continuous stochastic (i.e., random) process widely used to model the price of an asset. It relies upon a few mild assumptions, but perhaps the most notorious one is that of *path continuity.* In simpler terms, this means that, although price will go through random alterations, as it does in reality, we eliminate the possibility of abrupt, drastic changes in price, often referred to as "black-swan events".

 In this model, the price process $\left\{P(t)\right\}_{t\geq 0}$ satisfies the following Stochastic Differential Equation (SDE):
 
 m_\text{fee}
 
\begin{aligned}
\frac{\mathrm{d}P(t)}{P(t)}=\underbrace{\mu_\text{token}\mathrm{d}t}_\text{deterministic drift}+\underbrace{\sigma_\text{token}\mathrm{d}W(t)}_\text{random, volatile term}.
\end{aligned}

Here, $\mu_\text{token}\in\mathbb{R}$ represents a deterministic drift term that determines the price process's trend, $\sigma_\text{token}>0$ signifies its volatility, and $W(t)$ signifies the Wiener process, responsible for the process's inherent randomness. Given an initial price at time 0, $P(0)$, the solution to the aforementioned SDE can be demonstrated to be as follows:

\begin{aligned}
P(t)=P(0)\exp\left(\left(\mu_\text{token}-\frac{\sigma_\text{token}^2}{2}\right)t +\sigma_\text{token} W(t)\right).
\end{aligned}

However, it's noteworthy that this price model is based on the assumption of price continuity, implying it may not accurately simulate sudden, extremely sharp price movements. For simulations necessitating such scenarios, a more versatile price model, such as the [Levy process](https://en.wikipedia.org/wiki/Lévy_process), could be more suitable. 


#### Daily service fees collected


For the amount of service fees collected by the network (in USD), we took Qredo's projected service fee revenue as a guideline together with some random noise to capture some of the possible uncertainties that can arise in their forecast. We also added a multiplier to allow us to test diferent scenarios. More precisely, denoting by $A_\text{Qredo}(t)$ the service fees expected by Qredo, we model the service fees vector in MechaQredo as 

\begin{aligned}
A_\text{fees}(t)= m_\text{fee} \cdot A_\text{Qredo}(t)+\sigma_\text{fee} W(t),
\end{aligned}

with $m_\text{fee}\in\mathbb{R}$ the multiplier, $\sigma_\text{fee}>0$ the volatility of the service fees and $W(t)$ a Wiener process (independent of the Wiener process of the price). By doing this, we provide a model that, on the one hand, aligns with Qredo's prior work on forecasting their future service fees, while at the same time capturing some of the uncertainty associated with said forecast. 

We remark that, while not used in our simulations, our code is able to include different models for service fees, such as a GBM. 


#### Number of transactions executed, $N_\text{trx}$

This parameter encompasses both self-funded transactions and protocol-funded transactions. Here we use a simple linear model:

\begin{aligned}
N_\text{trx}(t) = \max(c_\text{tx} + m_\text{tx} \cdot t, 0)
\end{aligned}

Here $c_\text{tx} > 0$ and  $m_\text{tx}\in\mathbb{R}$.


#### Number of validators, $N_\text{val}$

Our approach will be based on the following assumption:

**A2**. *The number of validators is non-decreasing*.


We generate the number of validators in the network $N_\text{val}$ as a  [Poisson counting process](https://www.uni-muenster.de/Stochastik/lehre/WS1314/BachelorWT/Daten/StPro_Ross1.pdf). In this framework, a new validator is assumed to join the network after a certain time period, $T_\text{val}$. Here, $T_\text{val}$ is an independent random variable with an exponential distribution parameterized by $\lambda_\text{val}$, representing the expected number of days between two validators joining the network (i,e, $\lambda_\text{val} =1$ implies that, on average, there's a new validator joining the network every day, while $\lambda_\text{val}=30$ means that there's a new validator joining the network every month). This rate can be made to depend on factors such as, e.g., token price, to reflect scenarios such as having validators joining the network at a faster rate whenever the price is high. Such models are extensively utilized in the analysis of queuing systems. 

Regardless of the chosen approach, it's essential to determine $N_\text{val}(0)$. Based on our previous discussions with the Qredo team, we understand that the network plans to transition to FPoS with a total of 6 external validators.

<figure> <img             src="https://hackmd.io/_uploads/B1CUOmnUh.png" alt="my alt text"/>
  <figcaption> Figure. An example of a Poisson counting process for different interarrival rates. N(0)=18.
    </figcaption>
</figure>
![]()


#### Validator operating expenses

The operating expenses (OpEx) of different validators will vary, as these costs depend on factors such as hardware requirements, bandwidth costs, electricity, and technical expertise. Additionally, the network's consensus mechanism, whether it's FPoS or DPoS, will also influence these costs. For example, DPoS requires validators to stake tokens. If validators choose to borrow the amount to be staked, this could be included in their OpEx due to the associated interest rate.

At an initial level, we can ascertain a fixed daily cost for these elements and treat it as a constant provided by the Qredo team of 200 USD/day. This figure includes both infrastructure and *human capital* expenses. However, a more sophisticated approach would be to collect a sample of different validators' monthly costs, estimate a distribution for this metric, and then sample from it on either a daily or monthly basis. This will yield a more robust and realistic portrayal of the validators' operating costs.



#### Staking flows

Staking flows encompasses two key inputs to MechaQredo, namely, the number of tokens locked and released by Stakers at each step $t$. Since the decisions to lock and release depend on many factors, we encode the possible actions of Stakers in a simplified framework that depends on the key tokenomic parameters that impact the Staking Model, and define some sensible scenarios for expressing the various decisions Stakers can make.

When FPoS is first introduced (at $t=0$), Qredo will have a set of wallets that hold various amounts of QRDO. Each wallet will have the decision of whether to lock those tokens to participate in FPoS or not. This decision will depend on two factors:

- The first factor is the minimum staking amount $\bar{s}^\min$, which is a tokenomic parameter. The way this parameter impacts the decision of whether to stake tokens is quite straightforward. If the wallet has a balance greater or equal to the minimum staking amount, it will be "eligible" to stake. If not, that wallet (and its balance) will be excluded. We refer to the total amount of QRDO elligible for staking as $\tilde{S}^\text{in}$. This input can be estimated with the wallet balances data shared by the Qredo Team.
- The second factor corresponds to how much each wallet holder is willing to stake initially. This is harder to model. For simplicity, we aggregate all the eligible wallets ($\tilde{S}^\text{in}$) and assume a given percentage of their token balances will be staked. We refer to this percentage as the initial staking conversion rate, or $\delta^\text{init}\in (0,1)$. This rate is one of the variables we use to design the Stakers' decision scenarios.

We should note that, at this point, we are making a very strong assumption. Concretly, we are assuming that $\delta^\text{init} \cdot \tilde{S}^\text{in}$ will be 
instantaneously staked at day zero. We know that, most likely, wallet holders will take some time deciding they want to stake and then actually putting the request to stake. However, for simplicity, we will ignore this.

After this first wave of staking, the simulation will enter a new phase in terms of Staker behavior. At the start of a given step $t>0$, all Stakers will have a certain amount of QRDO staked, $L_\text{stake}(t-1)$. From this stake, they will be entitled to receive rewards, $R_{s}(t)$. After receiving rewards, they have to make two decisions:

1. Whether to decrease their current stake. This choice is encoded by the variable $\eta \in [0,1]$, which represents how much of the tokens available for release remained staked.
2. Whether to lock the reward they received. This choice is encoded by the variable $\delta \in [0,1]$, which represents the percentage of rewards received by stakers that are locked to increase their stake.

With the two parameters $\eta$ and $\delta$, we can already design some interesting scenarios, such as:

- $\eta = 1$ and $\delta = 1$: this is an "all-in" scenario where participants never decrease their stake and they lock all rewards to increase their stake.
- $\eta = 1$ and $\delta = 0$: this is a "stake and wait" scenario where participants maintain their stake without adding any extra tokens from the rewards they receive.
- $\eta = 0$ and $\delta = 0$: this is a "pessimistic" scenario where participants exit the network as soon as possible (i.e., right after the minimum locking duration) and don't lock any of the rewards they received.

Finally, we need to consider new Stakers joining the network after day zero. Let's call this variable $L^\text{in}_\text{stakeNew}(t)$ There are a few ways we can model this:

- Assume that, at each step, a **fixed percentage of the circulating supply** will be staked. This rate would become the main way to encode how bullish new participants are. However, this assumption has a problem, as we know that tokens locked in a staking mechanism are not perfectly correlated with the circulating supply.
- Similarly, one can assume that at each step, a given percentage $\delta^\text{new}$ of the circulating supply is staked. Contrary as the case above, however, in this setting we are assuming that $\delta^\text{new}$ is a random variable with some known distribution $M$, and that at each step, $\delta^\text{new}$ is independently sampled from $M$. This model relies upon a weaker assumption than the previous one, and has the advantage of capturing a wide array of behaviours, which can help us propagate and quantify this avenue of parameter uncertainty in the model.
- Assume that, at each step, a **fixed amount of tokens** will be staked. This fixed token amount would become the main way to encode how bullish new participants are. This assumption is better since it breaks the perfect correlation with the circulating supply. However, we do know that this fixed influx of locked tokens is also not realistic as circulating supply does have some impact on token availability for prospective Stakers. 
- Similarly, one can assume that at each step, a given amount of tokens will be staked. Contrary as the case above, however, in this setting we are assuming that this amount is a random variable with some known distribution $M$, and that at each step, the amount is independently sampled from $M$.

With this in mind, the final equations for token flows are defined in the following way:

- $L^\text{in}_\text{stake}(0) = \delta^\text{init} \cdot \tilde{S}^\text{in}$
- $L^\text{in}_\text{stake}(t) = \delta \cdot R_{s}(t-1) + L^\text{in}_\text{stakeNew}(t)$, for $t > 0$
- $L^\text{out}_\text{stake}(t) = 0$, for $t \leq \tau^\min$ 
- $L^\text{out}_\text{stake}(t) = (1-\eta) \cdot \text{Release}_\text{avail}(t)$, for $t > \tau^\min$
- $\text{Release}_\text{avail}(t) = \sum_{i<t-\tau^\min} L_\text{stake}^\text{in}(i) - \sum_{i<t} L_\text{stake}^\text{out}(i)$

Recall that $\tau^\min$ is the minimum locking period.


#### Current vesting schedules

This is a deterministic function that encodes the vesting schedule. While there is a fixed vesting schedule for the first 1B QRDO tokens, different vesting schedules and allocations can be determined for the unallocated remaining 1B.


### Market inputs scenarios

As we have seen in the previous subsections, there are a few market inputs that involve forecasting future trajectories of metrics that depend on adoption and market conditions. For our analysis, we wanted to explore how the various mechanisms responded to different conditions and forecasting regimes.

Therefore, we designed a set of scenarios to cover possible trajectories of these market inputs. Concretely, we built scenarios across three independent dimensions:

- Token Price: This dimension models varying scenarios for the token price.
- Network Usage: This dimension refers to different levels of network usage in terms of the number of transactions and service fees generated in USD.
- Staking sentiment: This dimension represents varying levels of token locking and releasing due to participants’ decisions within the Staking Mechanism.

For each dimension, we created 3 scenarios - pessimistic, base, and optimistic. The base scenario represents a situation where adoption and usage evolve according to current trends, while the token price remains at the current values. Then, the pessimistic and optimistic scenarios create worse and better versions of the base scenario, respectively.

Since each dimension is assumed to be independent, we consider all possible scenario combinations across the 3 dimensions, which leads to 27 possible scenarios.

The follwoing table summarises the values of each paramater by scenario and dimension:

|  | Pessimistic | Base | Optimistic |
|:---:|:---:|:---:|:---:|
| **Token price:** |  |  |  |
| $\sigma_\text{token}$ | 0.4 | 0.4 | 0.4 |
| $\mu_\text{token}$ | -0.5 | 0 | -0.5 |
| **Network usage:** |  |  |  |
| $\sigma_\text{fee}$ | 1000 | 2000 | 4000 |
| $m_\text{fee}$ | 0.5 | 1 | 2 |
| $c_\text{tx}$ | 1000 | 1000 | 1000 |
| $m_\text{tx}$ | -2.1 | 0 | 2.5 |
| $\sigma$ (protocol funded rate) | 0.6 | 0.4 | 0.2 |
| **Staking Sentiment:** |  |  |  |
| $L^\text{in}_\text{stakeNew}(t)$ (new Staker inflow) | 0 | 0 | 205500 |
| $\delta^\text{init}$ (initial conversion rate) | 0.4 | 0.6 | 0.8 |
|  $\delta$ (rewards reinvest rate) | 0 | 0.5 | 1 |
| $\eta$ (staking_renewal_rate) | 0.998 | 1 | 1 |
| **Others:** |  |  |  |
| $\lambda_\text{val}$ | 0.0164 | 0.0164 | 0.0164 |
| $N_\text{val}(0)$ | 6 | 6 | 6 |
| $\gamma$ (slippage) | 0.005 | 0.005 | 0.005 |
| Validator OpEx | \$200 | \$200 | \$200 |


:::info
:information_source: We should note that all scenarios were designed to test the mechanics of our design. Therefore, all predictions, projections, and forecasts included in this technical cryptoeconomics report are hypothetical and should not be interpreted as actual predictions or guarantees of future results. The analyses contained herein are based solely on the assumptions and models used for testing, not on any foreknowledge or speculation about future events or conditions.

Furthermore, the views and opinions expressed in this report do not necessarily reflect those of the research team or any associated individuals or entities. It is intended for informational and educational purposes only and should not be construed as financial or investment advice.
:::

### Tokenomic paramaters

In this section, we describe the tokenomics parameters. Thye are an important part of the simulations since they can change significantly the mechanics of token supply, the Staking Model and the Fee models.

#### Allocation and vesting

In terms of allocation, we have the following inputs:

- New allocation to the Treasury
- New allocation to the Ecosystem fund
- Allocation to the newly formed Public Goods fund
- Allocation to the newly formed Staking Program Support fund
- Allocation to the discretionary token burns

In terms of vesting, we assume all the new allocation will vest imediatly, with the exception of the Staking Program Support fund, which will have its own vesting function. We discuss it in more detail below.

#### Fee Models

The Fee Models have two main paramaters:

- **Transaction Protocol Fee, $f$:** This is the fixed amount of QRDO tokens burned by transaction. Recall that a part if this is covered by users while the rest if covered by the Ecosystem fund.
- **Tipping Rate, $\theta$:** This refers to the proportion of service fees that Qredo LLC converts to QRDO and lock in the Ecosystem Fund.


#### Staking Model

Finally, the Staking model has the following paramaters:

- **Vesting Rate Function, $\alpha(t)$:** This function defines the portion of the $\mathsf{StakingProgramSupportFund}$ that will be vested and distributed to Validators and Stakers. Inspired by the traditional minting functions, we propose to have $\alpha$ follow an exponential decay controled by a decay rate. We will test different decay rates to balance both the inflation rate and the staking model feasibility (for both validators and stakers). In particular, $\alpha$ is defined as:

\begin{aligned}
\alpha(t)=\left(1-e^{-d\cdot t}\right),\quad d>0
\end{aligned}
 
Here, the rate parameter $d$ is a tokenomic parameter to be tuned. 

- **Release Rate Function, $r(t)$:** Similar to the vesting rate function, this function allows a share of the $\mathsf{EcosystemFund}$ for distribution. In particular, we define $r(t)$ as 

\begin{aligned}
r(t) = 
r_\text{max}\left((1-b)\cdot\min\left(1,\frac{\mathsf{TVL}}{\mathsf{TVL}_\text{target}}\right)^a+b\cdot\min\left(1,\frac{N^\text{val}}{N^\text{val}_\text{target}}\right)^a\right)
\end{aligned}


Here, the maximum release rate,  $r_\text{max}$, the split between TVL and number of validators, $b$, the shape parameter $a$ and the target number of validators and target TVL, denoted by $N^\text{val}_\text{target}$ and $\mathsf{TVL}_\text{target}$ respectively, are tokenomic parameters. Notice that this is a function that takes values between 0 and $r_\text{max}$, and increases as either the TVL or the number of validators increases. The parameter $b\in(0,1)$ gives more weight to number of validators vs TVL, and the parameter $a$ determines how fast this increase is. 


- **Validator reward share, $\psi$**: This parameter determines the proportion of total rewards distributed to Validators. A value of $\psi=1$ implies that all the rewards sourced for the Staking Model are distributed to validators, while $\psi=0$ indicates that all rewards are directed to stakers.

- **Minimum stake amount, $\bar{s}^\min$:** This paramater encodes the minimum amount of QRDO tokens required for Staking. Different protocols currently impose different minimum staking amounts; for instance, Cardano requires a minimum of 8 ADA, while Ethereum sets a minimum of 32 ETH. 

- **Minimum stake duration, $\tau^\min$**: This is the minimum number of days that tokens must be locked in order to be considered "staked" and receive rewards. The staking duration in other protocols ranges between 0 to 180 days, with longer durations enhancing both network security and circulating supply.

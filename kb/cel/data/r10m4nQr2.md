# Staking Model in the Qredo Network

#### Maria Silva and Juan P.M. Cianci, CryptoEconLab, May 2023

This report provides a comprehensive overview of two staking mechanism designs for the Qredo network, in line with their strategy for decentralization. 

Initially, we examine 'synthetic staking', which is currently employed by the network, and subsequently delve into two increasingly decentralized consensus mechanisms that Qredo aims to integrate in the future: a  Federated consensus mechanism (which we will call Federated Proof-of-Stake (FPoS)), and Delegated Proof-of-Stake (DPoS) mechanisms.

Subsequently, we introduce the key components of a staking mechanism design, which include the source of staking rewards, the method of their distribution, and the enforcement of locking and slashing mechanisms.

Following this, we engage with the more intricate details of these components, including an exploration of the numerous parameters that make up the complex design framework of a staking mechanism.

Concluding our report, we summarize the comprehensive design possibilities of the staking mechanism and offer general suggestions on the selection of these parameters. A future publication will provide a detailed specification of these parameters as part of the project's second phase.


## Introduction


Loosely speaking, staking is the process of locking up tokens to participate in the validation of new blocks on a blockchain network. In return for staking their tokens, participants earn rewards, typically in the form of additional tokens. 

Currently, the Qredo network does not have a protocol-governed staking mechanism *per se*. Instead, Qredo offers a weekly staking event with a **5.05% APY reward for holding QRDO tokens within the Qredo Network.** This *synthetic staking* (i.e., without decentralized validators and with no need to lock tokens into a pool) is automatic, and rewards are distributed every Monday. It occurs on a per-wallet basis and users can withdraw QRDO at any time; however, they would forfeit any accrued rewards for the amount withdrawn. See [here](https://qredo.zendesk.com/hc/en-us/articles/5806237485585-Ongoing-Weekly-Staking-Events) for more details. 


There are two main challenges associated with the mechanism above: 

- *Token dilution*. Continually releasing new tokens to reward holders without strongly incentivizing users to *lock* tokens (and effectively removing them from the circulating supply) can lead to *token dilution*. This means the total supply of tokens increases beyond its demand, which could decrease the value of individual tokens if demand does not rise proportionally. 
- *Centralized consensus*. Having a fully centralized consensus poses trust, security, and censorship-resistance risks, which are antithetical to Qredo's mission.  

Furthermore, the QRDO token has a finite supply, which makes it difficult to sustain a fixed APY based solely on vesting throughout a long period of time. 


To overcome these challenges, the Qredo network is on a path to decentralization, that it intends to achieve by first moving to a federated consensus mechanism and, over time, moving to a wholly Delegated Proof-of-Stake. By doing this, the network intends to generate greater demand for the token (due to the more complex staking mechanisms) at hand while increasing the network's economic security (and, potentially, trust). 




![](https://hackmd.io/_uploads/HkkXCyqOh.png)

<figcaption> Figure 1. Qredo's path to decentralisation. Notice that the timeline needs to be fixed. </figcaption>





## Overview of staking mechanisms

Staking-related consensus mechanisms, such as Proof-of-Stake (PoS), Federated Proof-of-Stake (FPoS, a PoS combined with a federated consensus), and Delegated Proof-of-Stake (DPoS), aim to secure a blockchain network through token ownership rather than computational power, as seen in Proof-of-Work (PoW) systems. 

In PoS, individuals can validate blocks and participate in network governance proportionally to the number of tokens they hold and are willing to "stake" or lock up as collateral. DPoS further democratizes this process by allowing token holders to vote for a select group of validators (delegates), who then carry out the network validation tasks. The FPoS consensus mechanism works similarly; however, in that setting, the (potentially third-party) "delegates" are "voted in" by a centralized authority, such as the network itself. In other words, validators in the FPoS must go through a vetting process before they are approved as validators.

These three mechanisms create economic incentives for good behavior and disincentives for malicious actions, as staked tokens can be forfeited or "slashed" if a validator acts dishonestly. They align network security with the vested interests of token holders while being more energy-efficient than PoW systems. To reiterate, in the case of Qredo, the goal is to first move to a *partially-centralized* FPoS and eventually move to a fully decentralized DPoS mechanism. We now discuss FPoS and DPoS in more detail. 

### Federated Proof-of-Stake

*Federated Proof-of-Stake*  is a type of consensus mechanism used in blockchain networks. In this setting, a group of ***pre-selected, possibly third-party nodes***, called the Federated Nodes, participate in the consensus process. This system operates on the principle of trust and reputation; the network designates nodes as Federated Nodes based on their reputation or trustworthiness within the network. At the time of writing, one of the best-known Web3 projects with a Federated consensus mechanism is Ripple.

#### How does it work?


The network carefully chooses a set of third-party validators based on criteria such as *trustworthiness,* experience as validators, etc. In this setting, the *nodes* are not required to stake funds, since they can be removed at any time by the network in case of misbehaviour, however, *token holders* interested in participating in the staking rewards mechanism will have to lock some tokens for some time. When a transaction or an operation is proposed in the network, Federated Nodes run an agreement protocol amongst themselves. This could involve a voting system where most votes determine whether a proposed operation is validated. If the proposal secures a sufficient number of votes (often more than 50%), it's accepted and included in the ledger. Rewards are then distributed among these nodes and, potentially, the token holders. 


### Delegated Proof-of-Stake

Delegated Proof-of-Stake (DPoS) is a consensus mechanism that aims to maintain security, speed, and decentralization. It was first implemented by Dan Larimer, and it is the consensus mechanism in platforms such as *BitShares, Steem,* and *EOS.*

DPoS seeks to streamline the decision-making process within a blockchain by minimizing the number of nodes involved in such a process. Instead of every network participant being involved in the process, DPoS elects a fixed number of *delegates (or witnesses)* to create blocks and confirm transactions, with the rest of the network participating in a democratic voting process to select these delegates.

#### How does it work?

The delegates are chosen through a **continuous** approval voting system by the holders of the native cryptocurrency. In this system, every token holder can vote for one or multiple candidate nodes, with the number of votes each candidate receives being proportional to the number of tokens the voters hold. The candidates with the most votes are selected as delegates. The number of delegates is predetermined and can vary depending on the blockchain network.

The selected delegates are responsible for creating new blocks and adding them to the blockchain. The block creation process follows a deterministic order, typically a round-robin schedule, **to avoid the competition seen in Proof-of-Work systems (in terms of power) or Proof-of-Stake (in terms of validator wealth)**. That block space is lost if a delegate does not create a block in its turn. Once a block is created, other delegates validate it. If the block is valid, it gets added to the blockchain, and the block creator, and potentially their electors, get a reward, often in the form of the native cryptocurrency.


In a DPoS system, bad behavior or malicious intent is managed by the threat of being voted out by the community. If a delegate does not properly validate transactions or attempts a malicious act, they risk losing their delegate status. This holds delegates accountable and encourages honest behavior. Moreover, since delegates are the representatives of the network, they often have additional governance responsibilities. This can include deciding on blockchain parameter updates or even proposing and voting on network operation changes. However, **having an active voting system effectively requires high community participation, which in turn needs to be properly incentivized**.

A simple pseudocode implementation of the DPoS algorithm is shown below. 

![](https://hackmd.io/_uploads/Hy3-3b2Bh.png)


#### Security

DPoS relies on the economic stake that delegates have in the network. The more a delegate has to lose, the more likely they are to validate transactions correctly. To enhance security, some DPoS systems require delegates to lock up a certain amount of the native cryptocurrency as collateral, known as *staking* or *bonding*. This collateral can be slashed (partially or fully) if they act maliciously.

#### Scalability and Efficiency

By reducing the number of nodes participating in the consensus, DPoS can increase the speed and scalability of the blockchain. Blocks can be created and validated faster, allowing the network to handle a higher transaction throughput.

Overall, Delegated Proof-of-Stake presents a unique approach to consensus that combines elements of democracy, accountability, and scalability. However, it's important to note that it does have potential drawbacks, such as the risk of centralization if a small number of large token holders control the voting process. As with all consensus mechanisms, the effectiveness of DPoS ultimately depends on the specific implementation and the surrounding ecosystem.


### Differences between PoS, DPoS and fPoS


|                            | Proof-of-Stake (PoS) | Delegated Proof-of-Stake (DPoS) | Federated Proof-of-Stake (fPoS) |
|----------------------------|:---------------------:|:--------------------------------:|:--------------------------------:|
| **Selection of Validators**    | Chosen based on the amount of cryptocurrency staked | Token holders vote for a fixed number of delegates | Validators are chosen by the network |
| **Token Holder Involvement**   | More tokens staked leads to higher chances of selection as validator | Tokens used to vote for delegates. Holders can also stake to participate in rewards | No direct involvement of token holders in validator selection, but token holders can stake to participate in rewrds |
| **Distribution of Rewards**    | Rewards go directly to chosen validators | Rewards are distributed among elected delegates; a portion may be shared with voters, potentially proportional to No. of tokens held | Rewards distributed to nodes and stakers  |
| **Decentralization**           | Promotes decentralization but may lead to power concentration if few validators have most tokens | Potentially less decentralized due to concentration of power in the hands of elected delegates | Potentially less decentralized than DPoS, depends on the selection process of the network stakeholders |
| **Efficiency**                 | Tends to be less efficient than DPoS | Generally faster and more efficient due to fixed number of validators | Efficiency may vary, can be high if validators are well-chosen |
| **Token Lockup**               | Staking might require tokens to be locked up, which reduces circ. supply  | Tokens locked by validators and stakers | Tokens locked by stakers |


## An overview of staking mechanism design




We need to consider several essential components when designing a staking mechanism's incentive and economic aspects—whether it be FPoS or DPoS.

- **Source of rewards:** This pertains to the origin of the tokens that serve as rewards.
- **Reward distribution:** This entails the rules and methods for allocating these reward tokens.
- **Locking and slashing*  Mechanism:** This relates to the mechanisms for locking/removing tokens eith the goal of ensuring network security.

**Note**: *We will focus our efforts on the FPoS, where there is no slashing.*


A diagram depicting the staking mechanism is shown below. 

![](https://hackmd.io/_uploads/HyxNyl5d2.png)


One also needs to decide on the number of nodes (for FPoS) or delegates (for DPoS) in the system. Each of these critical elements has multiple associated parameters and potential variations. In this section, we discuss these terms in *plain terms.* We will present a more rigorous treatment of them in the next section. 

For simplicity, and with a slight misuse of terminology, we use the term 'validator' in this section to refer to either a federated node in an FPoS or a delegate in a DPoS mechanism. Similarly, we will use the term 'Staker' to refer to a staking token holder.



### Source of rewards

Here we discuss how the rewards that will be distributed to the staking participants (i.e., stakes and validators) are collected and how they're made available for later distribution. 

For Qredo, we will consider two specific token sources:

1. **Staking program support fund.** A fraction of the staking rewards will come from a portion of the vested tokens, initially allocated from the 1 Billion. The specific amount of tokens to be allocated to this specific fund will be determined in phase 2. 
2. **Ecosystem fund.** The rest of the tokens destined for staking rewards will come from an ecosystem fund created from *service fees.* In particular, a proportion of the service fees will be distributed to the validators. This proportion will also be determined in phase 2 of the project. 

While in principle (and perhaps naively), one could make the totality of those funds available for distribution, there is more flexibility in creating *token inflow mechanisms* that would restrict the number of available tokens available for distribution at any given time in favor of making them available for distribution later. This is done with the intention of incentivizing network growth and other Key Performance Indicators (KPIs) aligned with Qredo's strategy by effectively producing larger rewards as the network achieves some predefined growth milestones. To that end, we propose to implement the following two token inflow mechanisms:

1. **Vesting rate function**, which controls the number of vested tokens in thestking program support fund available for distribution. In particular, for a given total fund size $\mathsf{fundSize}$, the amount of available tokens form this contributor at a time $t$ is given by 
\begin{align}
\mathsf{Available}(t)=\mathsf{fundSize}\left(1-e^{-\mathsf{rate}\times t}\right),
\end{align}
for some given rate $\mathsf{rate}$.

2. **Release rate function**, $r$ which controls the number of tokens available for distribution from the ecosystem fund. This rate takes into account two of Qredo's KPI for network growth: TVL and number of validators. In particular, for some given maximum rate $r_\text{max}$, such a function is chosen of the form:\begin{aligned}
r(N^\text{val},\mathsf{TVL})=r_\text{max}\left(b\cdot \min\left(1,\frac{\mathsf{TVL}}{\mathsf{TVL}_\text{target}}\right)^a+(1-b)\min\left(1,\frac{N^\text{val}}{N^\text{val}_\text{target}}\right)^a\right), \quad a\in\mathbb{R}_{>0},\ b\in(0,1).
\end{aligned}
In words, this means that as either the TVL or the number of validators approach their target, the release rate approaches the maximum possible rate $r\max$. In the equation above, $a$ is a parameter that controls the growth towards that parameter, and $b$ is understood as a lever that gives prefference to either TVL or number of validators. 
![](https://hackmd.io/_uploads/H1VwbgqO3.png)



### Reward distribution

Every day (or more generally, at the end of each pre-specified epoch), a set of rewards is made available for distribution (i.e., vested tokens from the Validator Reward Fund and the released tokens from the Ecosystem Fund), according to the *token inflow mechanisms* mentioned above. These available tokens will be split into ***validator rewards*** and ***staker rewards***.

The *validator rewards* are split among all validators, according to some ***validator score*** function that gives each validator a piece of the validator rewards. This score function, in turn, should depend on whether a FPoS or DPoS mechanism is in place, the amount staked by a specific validator, reputation, etc. For example, in the initial stages where an FPoS system is in place, this score function could split these rewards equally among the number of Nodes (since there is no need for them to stake capital). For a DPoS system, this function should give a more significant *portion of the pie* to those validators with larger stakes and higher reputation scores. 

Similarly, the *staker rewards* will be split among all stakes, according to a **stakes score function**. This function will assign a larger piece of the pie to a staker according to some measurable conditions, such as assigning a larger portion to stakes with a larger balance, those who actively participate in the election process, the delegate they voted for (in DPoS), as well as those who have held the token for a longer time.

 The proportion of this split (e.g., whether it is 50-50, 40-60, etc.), together with the specific functional form and parameters of the *validator and staker score functions*, will be decided in phase 2.

![](https://hackmd.io/_uploads/Hkd7Nec_2.png)


### Locking.

Locking is an essential part of any consensus mechanism derived from proof-of-stake. In particular, it enhances network security while simultaneously impacting token demand and circulating supply. 


As for its effects on the economy, locking tokens will remove them from circulation for a given amount of time, reducing the overall circulating supply. Furthermore, this mechanism could increase the demand for the tokens.

The *Locking* mechanism will depend on the stage where the Qredo network is concerning decentralisation. In particular, for the FPoS model, only *stakers* will be required to lock a number of QRDO in exchange of participating in the staking rewards program, while there is no need for validators to lock tokens. For the DPoS model, however, both *stakers and validators* will be required to lock tokens.


## Technical details and initial recommendations


### Technical details

We now present some technical details on the components of the staking mechanism.

#### Source of rewards

As previously discussed, there are two sources of tokens that will later be distributed as rewards: those allocated from a fraction of the vesting tokens (the *valdiator reward fund*), and those allocated as a fraction of the *service fees* (the *ecosystem rewards fund*). Thus, at any given time $t$, the total number of available tokens, $\mathsf{Tokens_{available}}$, can be represented as:

\begin{aligned}
&\mathsf{Tokens_{available}}(t) = \mathsf{StakingProgramSupportFund}\left(1-e^{-\mathsf{rate}\times t}\right) \\
&+ r_\text{max}\left(b\cdot \min\left(1,\frac{\mathsf{TVL}}{\mathsf{TVL}_\text{target}}\right)^a+(1-b)\min\left(1,\frac{N^\text{val}}{N^\text{val}_\text{target}}\right)^a\right)\mathsf{EcosystemFund}(t), 
\end{aligned}


This leaves us with a few levers; the size of the Staking program suport fund, the release rate ($\mathsf{rate}$), the maximum rate for the ecosystem rewards fund ($r_\text{max}$), the shape and preference parameters $a,b$ and the target TVL and number of validators ($\mathsf{TVL}_\text{target}$, $N^\text{val}_\text{target}$, respectively).   




#### Reward distribution

Recall that tokens are distributed among *validators* and *stakers*. Thus, at any time $t$, we have that: 

\begin{aligned}
\mathsf{Tokens_{available}}(t)&=\mathsf{RewardValidators}(t)+\mathsf{RewardStakers}(t).
\end{aligned}
In what follows we will drop the explicit dependence on time, for notational simplicity.

Recall that we give a  proportion $\psi\in[0,1]$ of the available rewards $\mathsf{Tokens_{available}}$  to the validators (either delegates or nodes) and the rest to the stakers. This in turn results in the following equations:

\begin{aligned}
\mathsf{RewardValidators}&=\psi \mathsf{Tokens_{available}}=\sum_{v\in V}\mathsf{RewardValidator}_v\\
\mathsf{RewardStakers}&=(1-\psi)\mathsf{Tokens_{available}}=\sum_{i\in I}\mathsf{RewardStaker}_i.
\end{aligned}

Here, $V$ denotes the set of all validators (nodes or deletes) and $I$ represents the set of all  stakers (that are not validators).   We then have that in this setting, **$\psi$ corresponds to another lever that one can adjust, controlling how much to give to validators vs stakers.** 

The *crux* fo the design is then to define  suitable values for $\psi$, $\mathsf{RewardValidator}_v$ and $\mathsf{RewardStaker}_i$.

In a general setting, the reward for each validator $v$, denoted by $\mathsf{RewardValidator}_{v}$, is given by:

\begin{equation}
\mathsf{RewardValidator}_{v} = \psi\cdot f_v\cdot \mathsf{Tokens_{available}},
\end{equation}
where $f_v,$ with $\sum_{v\in V} f_v= 1$, is the **validator rewards function.** Such a function assigns a given proportion of the validator rewards to validator $v$ according to, e.g., their relative stake, the number of votes (if any) obtained by such a validator, their reputation, etc.

Similarly, in the general setting of the stakers' rewards, we have that for each staker $i$, their rewards $\mathsf{RewardStaker}_{i}$ are given by 

\begin{aligned}
\mathsf{RewardStaker}_{i} = (1-\psi) \cdot s_{i}\cdot \mathsf{Tokens_{available}},
\end{aligned}

where $s_i$, with $\sum_{i\in I}s_i=1$ denotes the **staker rewards function,** which allocates the *piece of the rewards pie* to staker $i$ according several observable metrics and mechanisms, such as staker $i$'s token balance over some given period of time, their governance participation (in DPoS), number of locked tokens (if decided to use the optional locking for stakers), among others.  


The conversation above leaves us with **3 levers** - the validator rewards function $f_v$, the staker rewards function $s_i$, and the distribution proportion, $\psi$. 


#### Locking

For any given validator $v$ and Staker $i$, we denote the minimum amount of locked tokens as $S_v^\min\geq0, \bar{S}_i^{\min}> 0$, respectively. Notice then that the amount of tokens locked for staking is strictly positive for stakers, and we allow it to be zero for validators, to account for the FPoS case.  Similarly, we denote the minimum holding time for both validators and Stakers by $\tau_v^\min>0,\bar{\tau}_i^\min> 0$, respectively. Lastly, we define functions $u_v(S_v,t)>0,\bar{u}_i(\bar{S}_i,t)> 0$ which control the unlocking of the staked tokens. In particular, for a given amount of locked tokens $S$, $u(S,t)$ releases these $S$ tokens over time. This can be done by e.g., releasing all tokens all at once after some given time, by continuosly releasing some small amount over time, or by releasing the staked amount in *chunks*.




### Parameter overview

The table below summarises the different choices of parameters, their implications, and a recommended value.

| Parameter                            | Name                               | Meaning                                                                                                                                                 | Type                                           | Design Element     | Implication                                                                                                                                                    |
|--------------------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $N$                                  | Number of validators               | Total number of valdiators (nodes or delegates)                                                                                                         | integer                                        | general            | - Larger implies more security but higher transaction costs. Typical DPoS has between 31-101.                                                                  |
| $\mathsf{StakingProgramSupportFund}$ | Staking program support fund       | Amount of tokens allocated to the staking program support fund                                                                                          | Constant>0                                     | Source of tokens   | This is part of the vesting schedule                                                                                                                           |
| $\mathsf{EcosystemRewardFund}(t)$    | Ecosystem rewards fund             | Amount of tokens that can be allocated for rewards coming from service fees                                                                             | Environment variable                           | Source of tokens   | Will depend total trx. volume                                                                                                                                  |
| $\mathsf{rate}$                      | Decay rate function                | Determines how much of the staking program support fund is to be made available  for distribution.                                                      | Constant >0                                    | Source of tokens   | Determines how fast the vested tokens are distributed                                                                                                          |
| $r_\text{max}$                       | Release are function               | Determines the maximum amount of the ecosystem rewards to be made available for distribution                                                            | Constant >0                                    | Source of tokens   | Determines how fast the ecosystem rewards are distributed                                                                                                      |
| $a$                                  | Shape parameter                    | Determines how does the release function increases as it reaches the target                                                                             | Constant >0                                    | Source of tokens   | important to decide weather to incentivise early adoption                                                                                                      |
| $b$                                  | proportion parameter               | determines the relative influence of TVL Vs number of validators                                                                                        | Constant in (0,1)                              | Source of tokens   | Important when deciding which KPI to prioritise                                                                                                                |
| $\mathsf{TVL}_\text{target}$         | Target TVL                         | How much TVL we want to achieve?                                                                                                                        | Constant >0                                    | Source of tokens   | KPI                                                                                                                                                            |
| $N^\text{val}_\text{target}$         | Target number of validators        | How many validators do we want to have?                                                                                                                 | Constant >0                                    | Source of tokens   | KPI                                                                                                                                                            |
| $\psi$                               | Distribution proportion parameter  | The distribution proportion function. Determines the proprtion of rewards that goes to validators                                                       | parameter between (0,1)                        | Token distribution | -lower $\psi$, favors staker engagement, creates demand. Higher $\psi$ favor validator engagement generates security                                           |
| $f_v$                                | Validator rewards function         | Function that weights each validator's rewards amount. Weight can be given regarding votes (DPoS), stake, time, etc.                                    | function $\leq 1$ that sums to 1 over $v\in V$ | Token Distribution | - Connected to stake and how votes are counted, but can also be chosen to favor e.g., reputability                                                             |
| $s_{i}$                              | Stake rewards function             | Function that allocates stake $i$'s piece of the rewards pie. This allocation can be given due to QRDO balance, participation in delegate process, etc. | function $\leq 1$ that sums to 1 over $I\in I$ | Token Distribution | - Connected to $\bar{S}_\min$ and $\bar{\tau}_i^\min$   - should be chosen  so that it increases with staked amount or amount of time tokens have been locked. |
| $\bar{S}_i^\min$                     | minimum amount to stake by stakers | minimum number of tokens to start earning rewards  as a staker.                                                                                         | Positive constant                              | Locking            | - higher values favor security and deflationary pressure, however, less attractive due to liquidity                                                            |
| $\bar{\tau}_i^\min$                  | minimum locking period for stakers | minimum locking period start earning rewards. Optional                                                                                                  | non-negative constant                          | Locking            | - higher values favor security and deflationary pressure, however, raises the bar to entry                                                                     |
| $u_v(S_v,t)$                         | Unlocking function for validators  | A function that unlocks staked tokens for validators over time (in DPoS)                                                                                | function                                       | Locking            | More delay in locking good for security, but less attractive                                                                                                   |
| $\bar{u}_i(\bar{S}_i,t)$             | Unlocking function for stakers     | A function that unlocks staked tokens for stakes                                                                                                        | function                                       | Locking            | More delay in locking good for security, but less attractive                                                                                                   |                                                                                               |

A recommendation of the choice of these parameters will be presented in the final report. 

## Finalizing remarks

The Qredo network is on a trajectory towards decentralization, with an aim to transition from a fully centralized system to a Federated Proof of Stake (FPoS) consensus mechanism and ultimately to a more decentralized Delegated Proof of Stake (DPoS) mechanism. These mechanisms offer economic incentives for beneficial behavior and deter malicious actions, thereby aligning network security with the vested interests of token holders and promoting energy efficiency. This report provides a concise overview of these mechanisms and their tokenomics, introducing a general framework for designing such staking mechanisms.

When formulating a staking mechanism like those mentioned above, various factors such as token inflow, token distribution, locking and slashing conditions, and the number of nodes/delegates should be thoughtfully considered. Furthermore, constructing and identifying suitable reputation and  voting mechanism (for DPoS) requires careful attention. These parameters should be meticulously selected to optimize incentives, boost participation, and guarantee network security.

In this study, we detailed a general structure for these factors and  offered some parameters selection guidelines that we believe align with Qredo's future plans. We plan to delve deeper into analyzing and testing specific parameter choices in future studies. Our forthcoming report will also include an extensive investigation of the voting and reputation mechanisms.







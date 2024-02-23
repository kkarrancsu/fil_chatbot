---
tags: Gas, Research proposals, Almanac
---

# FVM and block space gentrification.


**TL;DR.** While the Filecoin Virtual Machine (FVM) is widely regarded as an excellent addition to the Filecoin network, a potentially harmful, purely hypothetical  (yet possible) scenario stemming from its release is that an increase in block space demand due to the FVM results in some valuable block space taken away from the core functioning of the network, in such a way that it could negatively affect it, by making more expensive for storage providers to onboard data and submit proofs of storage.   We refer to this scenario as *block space gentrification*. 

In these notes, we properly pose this problem and discuss some potential solutions. A detailed, more technical analysis of (i) the characterisation of demand, (ii) the quantities that will be most affected by this change in demand,  and (iii) some proposed methodologies are discussed in the Appendix. 


## Problem statement. 

The [core mission](https://filecoin.io) of  Filecoin is to store humanity's most valuable information. Currently (late November 2022), most ==all?== of the messages and transactions occurring in any given block in this network are related to this data-storage goal.

The introduction of the Filecoin Virtual Machine (FVM) is expected to attract a potentially large whole new set of consistent users to the network. Indeed,  [some stakeholders](https://filecoinproject.slack.com/archives/C0370V3JTPB/p1669234547841079) are aiming to have over 100 unique, value-generating dApps from day one. However, the purpose of these dApps is beyond data storage, as it could be related to, e.g., computing over data, data retrievals, interaction with the Ethereum network, or even DeFi. 

While the FVM will be an immense improvement to the network's current capabilities, the enlarged user base resulting from the FVM will likely increase demand for block space.  *A priori*  such an increase in demand is neither good nor bad. However, it is possible that the stream of new, FVM-related messages might take away valuable block space from those messages that are critical to the correct functioning of the network (so-called *control plane messages*), such as those related to data onboarding (`PreCommitDeposit`) and proof of storage over time (`SubmitWindowedPoSt`). This scenario could happen, for example, if FVM users consistently submit their messages with a substially larger bid that that associated with the control-plane messages$^1$. Given that storage providers might incurr a penalty for not submitting `SubmitWindowedPoSt` messages on time, they will likely still try to submit their messages, even if the price (in terms of base fee and miner tip) is too high, as long as the cost of doing so is smaller than the cost of getting penalised. We refer to this problem as *block space gentrification*.

**[1]**. *We remark that this could still happen today, however, there is little to no incentive for any actor to do it.* 



To better understand this problem, it is worth investigating the following questions. 

1. What is the maximum level of demand, understood either in terms of the percentage of the block size used or as the amount of gas required by messages in the Mpool, that the network can withstand without negatively impacting storage providers? Here we mean impact in the broadest sense; increase in price, average number of epochs to get a message included, average increase in price, probability of commiting a fault due to excessively high base fees, to name a few. 
2. How could we quantify the impact of such an increase in demand? 
3. How would the demand for block space compare between FVM and non-FVM users? i.e., how sensitive are these users' consumptions to a change in the base fee?
4. What are the most susceptible quantities to this change in demand?
5. How does Mpool size and congestion affect block space?
6. How will the block composition change as a function of the base fee?





## Potential solutions to the block space gentrification problem


We present potential solutions discussed in several places by the broader community. We remark, however, that these are ***a Priori* solutions** and that they have yet to be tested extensively in a robust simulation environment. Once we have a running simulation environment, we can fine-tune these proposed solutions and envision other possible solutions. 

### Short term

#### Gas lanes. 

A first approach would be to consider so-called gas lanes. In this setting, one assigns a fixed proportion of the block space to several classes of messages. We describe the main idea behind this setting below. 

The first step is to classify the types of messages in $N_c$ different categories based on, e.g., their perceived importance or purpose. As discussed in  Appendix A1, these categories could be, for example: 

* i. Proofs of space-time (`submitWindowPoSt`).
* ii. Onboarding/PoRep proofs (e.g., `PreCommitSector` and `ProveCommitSector`) 
* iii. F(E)VM messages.

Once these categories are defined,  the network allocates an initial proportion of the available block space to each class. That is, defining by $B_i$ the amount of block space allocated to class $i$, $i=1,2,\dots,N_c$,  one should have that $B_1+B_2+\dots+B_{N_c}=B$, with $B$ the current block size. These block space allocations are called * gas lanes*, and we will refer to the size of $B_i$ (in terms of gas units) as its width. 

Each gas lane is, in turn, endowed with its own Transaction Fee Mechanism (TFM). Such a TFM can be, e.g., $N_c$ different EIP1559-like TFMs, each having a separate base fee, or one could consider the same base fee for all lanes.

At the end of each epoch, the protocol updated all base fees according to some pre-defined scheme. Furthermore,  in a general setting, one could consider updating the widths relative to their use. That is, if the block space used by messages of class $i$ is minimal compared to that of messages of class $j$, $j\neq i$, the method would, algorithmically, re-allocate some of the (unused) spaced in category $i$ to category $j$. This width adjustment resembles the vault balancing process commonly found in (constant sum) Automated Market Makers (c.f. [here](https://blog.chain.link/automated-market-maker-amm/#:~:text=Constant%20Sum%20Market%20Maker%20(CSMM)&text=CSMMs%20follow%20the%20formula%20x,tokens%20is%20not%201%3A1)).


**How could this alleviate the problem posed by block space gentrification?**


One could use this methodology to allocate a given, potentially fixed proportion of the block space to those messages deemed critical to the network. This will immediately avoid the problem of having potentially valuable space poached by FVM-related messages. However, one would need to be more careful when defining the lane-specific base fee.

**Remark 1.** At the time of writing, `SubmitWindowPoSt `messages take, on average, around 20-25% of the used block space at any given block; see [here](https://dashboard.starboard.ventures/transactions-usage#gas-usage-by-methods).

**Remark 2.**  The idea of having multiple Mpools was also mentioned in some discussions. We believe, however, that such an approach can be framed as a particular case of the gas lanes approach.


### Long term
#### IPC. 

An ideal, long-term solution would be using the InterPlanetary Consensus (IPC). In this setting, one could, e.g., dedicate a subnet to all FVM-related transactions and keep the parent network for all storage-related messages. Unfortunately, however, the timelines for these projects do not overlap. Should the gas lane solution be implemented, an interesting crypto-economic question would be to investigate the potential effects induced by this migration. 


# Appendix A1. Characterising demand

There are two possible approaches to characterising demand in our setting. We begin by introducing some necessary notations and then describe these two characterisations. We will assume that there are $N_c$ different classes of messages, each with its own demand function. In the Filecoin network, one such classification could be, e.g., 
* i. Proofs of space-time (`submitWindowPoSt`).
* ii. Onboarding/PoRep proofs (e.g., `PreCommitSector` and `ProveCommitSector`) 
* iii. F(E)VM messages.

Intuitively, one could expect messages of class $i$ to have a more inelastic demand than the others, meaning that storage providers would send these proofs without caring as much for the price (base fee) as the other groups. 


We say that a *message* $m$ is defined by the following tuple: 

\begin{aligned}
m:=(c,v,\ell,g,t),
\end{aligned}

where $c\in\{1,2,\dots,N_c\}$ represents the *class* of the message, $v\in\mathbb{R}_+$ represents the *valuation* of the message (understood as the gasFeeCap), $\ell\in\mathbb{R}_+$ is the user-defined gas limit, $g\in\mathbb{R}_+$ its gas consumption (gassed) and $t\in\mathbb{R}_+$ the time when that message was created. We will use the notation $c(m)$ to denote the class of a message $m$, $v(m)$ to denote its valuation, and so on.

We define the Mpool $M_t$ at time $t$ as a collection of messages $m$ created at a time $t'\leq t$. Messages arrive at the Mpool at random times (as opposed to, e.g., having exactly X messages coming at the Mpool every Y seconds). Notice that at the end of every epoch, some messages leave the Mpool as miners include them in blocks.

 We now proceed to describe our characterisations of demand.



### Mpool-induced demand.

Given some class $i$, an Mpool $M_t$, and some price $p\in\mathbb{R}_+$, we define the *Mpool-induced demand*  $\text{MID}_{i,t}(p)$ as 

\begin{aligned}
\text{MID}_{i,t}(p):= \sum_{\underset{c(m)=i, v(m)\geq p}{m\in M_t:}} g(m).
\end{aligned}

In words, we define $\text{MID}_{i,t}(p)$  as the sum of the gas required by all the messages in the Mpool that have class $i$ and a valuation of at least  $p$. 


### Implicit demand

Another ppossible caharacterization is defined implicitly. Given some class $i$ and a price $p$, and denoting by $G^i$ the amount of block space utilised by messages of class $i$, the Implicit Demand (ID) is defined by the following mapping


\begin{aligned}
p\overset{\text{ID}_i}{\mapsto} G^i(p)
\end{aligned}


i.e., this demands takes a price $p$, a class $i$, and assigns it a proportion of the block space, $G^i(p)$. 

# Appendix A2. Quantities that are likely to be affected. 




We begin by identifying the network quantities that are affected, either directly or indirectly, by these changes in demand.  


### A2.1. Quantities. 

**Gas consumption.** 

Perhaps the most directly-affected network quantity after the introduction of the FVM will be the gas consumption (`gasUsed`) $G_t$. An increase (resp. decrease) in demand for block space will increase (resp. decrease) gas consumption.  *Apriori*, it seems reasonable to assume that the FVM will increase demand for block space.

1. How will this demand affect $G_t$?
2. Not all messages have the same type of demand (elastic vs inelastic). Can we settle on a classification of messages? An example of this could be:

    * i. Proofs of space-time (`submitWindowPoSt`) --very inelastic demand
    * ii. Onboarding/PoRep proofs (`PreCommitSector` and `ProveCommitSector`) 
    * iii. F(E)VM messages -- more elastic demand



![](https://hackmd.io/_uploads/HJ_04HtLo.png)

**Base fee.**

Other than gas consumption $G_t$,  perhaps the most obvious place where this new type of message will affect is the base fee  (`baseFee`).  Recall that for an epoch $t$, the base fee $b_t$ is adjusted dynamically at the next epoch, according to the following formula:

\begin{aligned}
b_{t+1}=b_t\left(1+\frac{1}{8}\frac{G_t-G^*}{G^*}\right),
\end{aligned}
 where $G^*$ is the target amount of gas set by the protocol (currently fixed to be half of the maximum block size), and $G_t$ is the total amount of gas used at epoch $t$. Notice that, clearly, $G_t\in[0,2G^*]$. From here, it can be seen that $b_{t+1}$ increases linearly with $G_t$. It is not difficult to show that increasing (resp. decreasing) the amount of gas consumed by 1 unit of gas, will increase (resp. decrease) the `baseFee` at the next epoch $b_{t+1}$ by $\delta b_{t}:=\frac{b_t}{8G^*}$, tokens per gas unit.  


1. A priori, we would expect the average base fee to behave as follows:

![](https://hackmd.io/_uploads/rJcJ-fYUs.png)

indeed, higher demand will likely cause an increase on the average base fee, however, after some point, given that not all user will have the same *demand profile*, such a function will tend to stabilize.     

i.e., with the launch of the FVM, the average base fee (currently taking values around [0.1, 1] nano FIL/gas unit) will suffer an initial *shock*, increasing (at a non-necessarilly constant rate) for a period of $\Delta t$ epoch, after which it will stabilize. If such a scenario were to occur, two natural quantities to estimate would be 
* (i) $\Delta t$ (i.e., the shock duration), and 
* (ii) $\Delta\mathbb{E}[b_t]$, i.e., the increase on average base fee. 

This would not be a simple task, and will depend on some assumptions, but probably worth exploring.
 
**Miner tip**

Recall that any time a user sends a message $m$ to the Mpool, it is accompanied by a so-called *bid*, given by $$\text{bid}_{m,t}=\underbrace{\left(b_t+\text{gasPremium}_{m,t}\right)}_{\text{:=gasFeeCap}_{m,t}}\times \text{gasLimit},$$

where $\text{gasLimit}$ is a limit on the upper bound on the amount of gas (i.e., computational resources) that a message is allowed to consume, and $\text{gasPremium}$ can be understood as a tip to the miner. During periods of relatively low demand, i.e., when a message would take a relatively short time to be included on-chain, the rational strategy for a user is to submit messages with a $\text{gasFeeCap}_{m,t}$ that barely covers the `baseFee`, i.e., to tip very little. In periods of **sustained** high demand, however, where it will take a long time to get some messages included on chain, some users *might* then need to submit a larger tip to get their messages included. This presents two questions:

1. Which users will need to do this?
2. What will the increase in average gasPremium be?
3. Do we expect a profile as in the previous figure, or something different?


**Protocol revenue**

Here, we define [protocol revenue](https://dashboard.starboard.ventures/transactions-usage) as the number of tokens burnt at every epoch, i.e.,
\begin{aligned}
\text{Rev}_t:=b_tG_t=b_t\sum_{j\in \text{Block}_t}g_{j,t},
\end{aligned}
with $g_{j,t}$ the gas consumed by the $j^\text{th}$ message on the blocks included on epoch $t$. A priori, it is clear that an increase in base fee will in turn present an increase in protocol revenue. 




**Circulating supply.**

Because of the EIP1559-like transaction fee mechanism utilized by the Filecoin network, an amount equal to `gasUsed` $\times$`baseFee` is burnt at every epoch. Circulating supply is also affected by the minted amount $\text{Mint}_t$ at such an epoch, as well as the amounts of tokens that are locked, $L_t$ (due to, e.g., onboarding) and unlocked (due to, e.g., sector expirations and completed vesting periods), $U_t$ at the epoch $t$. 

**Remark.** In practice, the burnt amount is a little bit higher and it is given by $$b_t\times\tilde{G}_t:=b_t\times \left[G_t+ \alpha\left(\left(\sum_{j\in\text{blocks}_t}\text{gasLimit}_{j,t}\right)-G_t\right)\right], $$ 

for some $\alpha\in[0,1]$. The additional term is called the *overestimation fee*. For simplicity, however, we will limit ourselves to considering a burn term of the form $b_t\times G_t$.

Thus,  denoting by $\mathcal{S}_t$ the circulating supply at an epoch $t$, one has that, **all else being equal** one has that

$$\mathcal{S}_{t+1}=\mathcal{S}_{t}-\underbrace{G_t\times b_t}_\text{gets burnt}+\text{Mint}_t-L_t+U_t$$

Things start getting a bit tricky here, as there might be multi-scale and non-linear effects. Indeed, while the effect in burnt tokens is small, immediate (i.e., one epoch), and relatively simpler to quantify, the long-term effects of increased demand for block space in quantities such as minting, locking, and unlocking are far more difficult to quantify. Recall from [the Filecoin specification](https://spec.filecoin.io/systems/filecoin_token/block_reward_minting/) that the amount of minted tokens at any given epoch depends, under certain conditions, on the Raw-Byte Power (RBP) of the network. Given this, one could then ask the question: 

*Could a sustained increase in demand for block space, affect the long-term RBP of the network?* Similarly, *could this expected increase in demand affect $L_t$ and $U_t$, by changing, e.g., the rate at which users join, leave, or renew?* And if so, *at what scale?* *How could we quantify such effects*? 


**Network, miner, and user utility.**

Let us begin with **miner utility**. It can be argued (see, e.g.,[Roughgarden, (2020)](https://timroughgarden.org/papers/eip1559exchanges.pdf), as well as  [these notes](https://hackmd.io/37c7UTGbQq6MuprD23k0jw?both)) that the expected utility of miner $m$  at an epoch $t$ is given by  
\begin{aligned} u_{m,t}&=\underbrace{\mathbb{E}\left[\text{Rewards}_{m,t}\right]}_\text{I}\\
&+\underbrace{\mathbb{E}\left[\sum_{j\in \text{Block}_t}(p_{j,t}-b_t-\mu)\cdot g_{j,t}\right]}_\text{II}\\
&+\underbrace{W_m\left(\frac{\mathcal{S}}{\mathcal{S}-b_tG_t}-1\right)}_\text{III}\\
&-\underbrace{\min\{b_t\cdot B_m,\text{faultFees}_{m,t}\}}_\text{IV}\\
&+\underbrace{\text{Deals}_t}_\text{V}
\end{aligned}


Here, $\mathbb{E}\left[\text{Rewards}_{m,t}\right]$ is the expected block rewards of miner $m$ at epoch $t$, $p_{j,t}$ is message bid  (`gasFeeCap`) associated with the $j^\text{th}$ message in the block at epoch $t$ (denoted by $\text{Block}_t$), $\mu$ is a minimal operational cost that miners would have to incur to process said messages, $g_{j,t}$ represents the gas units consumed by message $m$ at epoch $t$, $W_m$ is the wealth of the miner $m,$ $B_m$ is the proportion of gas used dedicated to miner-related messages (such as submitting proofs of storage), and $\text{Deals}_t$ is the token inflow of a miner due to storage deals.  Let us explain the four components of the miner utility function as defined above. 

* Component $\text{I}$ represents the expected block rewards to miner $m$. According to the [Filecoin specification](https://spec.filecoin.io/systems/filecoin_token/block_reward_minting/), this term can be computed to be 

    $$\mathbb{E}\left[\text{Rewards}_{m,t}\right]=\text{Mint}_t\times \frac{\text{QAP}_{m,t}}{\text{NetworkQAP}_t}, $$
    where $\text{QAP}_{m,t}$ is the Quality Adjusted Power (QAP) of miner $m$ at epoch $t$. Paraphrasing the Filecoin specification, this means that *miners receive block rewards in direct proportion to their quality-adjusted power; a miner who contributes 1% of the network’s overall quality-adjusted power can expect to receive roughly 1% of block rewards over time.*

* Component $\text{II}$  represents the expected utility obtained from including blocks in a message, i.e., 


$$\mathbb{E}\left[\sum_{j\in \text{Block}_t}(p_{j,t}-b_t-\mu)\cdot g_{j,t}\right]:=\frac{\text{QAP}_{m,t}}{\text{NetworkQAP}_t}\sum_{j\in \text{Block}_t}(p_{j,t}-b_t-\mu)\cdot g_{j,t}$$


Here, the term $p_{j,t}-b_t$ can be associated with the so-called "miner tip" (`gasPremium`), which is usually --albeit not necessarily -- a small amount that users send to "tip" the miners (see, e.g.,[Roughgarden, (2020)](https://timroughgarden.org/papers/eip1559exchanges.pdf)). 


* Component $\text{III}$ corresponds to the increase in miner wealth due to burnt tokens. Indeed, since at each epoch a given amount of tokens are burnt, *ceterus paribus*, the circulating supply between any two epochs would decrease, thus making all other remaining tokens (slightly) more valuable.  The term in the parenthesis represents the amount by which the wealth has increased from token burning.


* Component $\text{IV}$ represents the amount of token that it costs a miner to be in the network at epoch $t$. This is defined to be the minimum between $b_t\cdot B_m$, which is to be understood as the number of tokens the miner needs to submit, on average, to keep providing storage (e.g., `submitWindowedPoST`) and $\text{FaultFees}_{m,t}$, which is the amount of token that a user would get slashed by if they failed to submit storage proofs on time. 


* Lastly, Component $\text{V}$ is related to the miner utility associated to deals. 


Let us now focus on user utility, for some given actor $a$ that **is not** a storage provider. This could be thought of, e.g., as the typical user that would be attracted to the Filecoin network because of the FVM. Suppose that at any given epoch $t$, a given user $a$ sends $N_t$ messages to the network, where each message $j$, $j=1,\dots, N_t$ has ($i$) an expected amount of profit per unit of gas, denoted by $w_{j,t}$, ($ii$) a user-defined bid $p_{j,t}$, satisfying $p_{j,t}>b_t$, and ($iii$) an amount of gas consumed $g_{j,t}$. The user utility in this case is si simply

\begin{aligned}
u_{a,t}=\sum_{j\in\text{Block}_t}(w_{j,t}-p_{j,t})\cdot g_{j,t}.
\end{aligned}

Notice that a rational user would only include messages such that $w_{j,t}\geq p_{j,t}$, which would also require that $w_{j,t}\geq b_t$ for any epoch. 


**onboarding     costs**

* **Initial Consensus Pledge (ICP).** Recall that the IPC (per sector) determined  at a given  epoch $t$ is defined as 

$$\text{ICP}_t:=\frac{0.30\cdot \mathcal{S}_t\cdot \text{SectorSize}_{t}}{\max\{\text{NetworkQAP}_t,\text{BaseLine}_t \} }$$


* **Sector Initial Pledge (SIP).** For a given miner $m$ this quantity is defined as 20 days of expected block rewards for miner $m$, i.e., 
$$\text{SIP}_{m,t}=20\cdot\mathbb{E}\left[\text{Rewards}_{m,t}\right]=20\cdot\text{Mint}_t\times \frac{\text{QAP}_{m,t}}{\text{NetworkQAP}_t}.$$



### ==To discuss.==

Notice that the terms $\text{QAP}_{m,t}$ and $\text{NetworkQAP}_t$ show up in various places. While they **do not** explicitly depend on the base fee, **it could happen** that a sustained increase in base fee might have a non-obvious effect on these terms.


Furthermore, other variables affect these quantities, such as renewal rate, scheduled expirations, etc.  As of now, my intuition is that whatever model we impose on the functional relation between $b_t$ and $\text{QAP}_t$ may or may not reflect reality with some acceptable level of accuracy. 

Lastly, my intuition, is that the effects that the FVM will have on these quantities might only be observable on a large time scale, as QAP is unlikely to dramatically change on an epoch-to-epoch (or even day-to-day) basis. 

Is it safe/worth it to ignore these effects, for now?



### A2.2 Observables.

Let $Q_t$ denote any of the quantities described in the previous subsection.  In these notes, we define an *observable* $O$ as a function $f$ of those quantities, i.e., $O_t=f(Q_t)$. As an example, one could consider an observable $\tilde{O}_t$ to be the 

1. Change in average base fee  due to FVM (currently `baseFee` has been around [0.1,1] nanoFIL).
2. onboarding rate.
3. change in batching. 

### A2.3 What if and Catastrophic scenarios.


1. FVM with gas labes and without gas lanes. Monitor QoIs.
1. Slashing rate increases due to base fee: Base fee is so high some miners start getting in trouble to submit their messages.
2. base fee  becomes too high. Probably people slow donw/stop onboarding. network power starts decreasing. rewards fall off and there is more circulating supply (as there will be, eventually, no locking nor renewals), price blows up. 


    


# Appendix 3. Steps, methods and models.

1. Classify types of messages/actors ✅. 
1. Understanding demand, and types of demand ✅. 
3. Define a "set of actions" for each class.
2. Simulate and observe. Available models:
    * Deterministic; compute changes in quantity, due to changes in demand (or `baseFee`), estimate sensitivities via derivaties. 
            * Derivative estimation, graphs, etc. 
    * Scenario-based: Assume base fee increases x%,how does this impact quantity Q?  
    * Stochastic: Multiple possible models, all of them depending on a set of initial assumptions. Suited for UQ. Most informative, but most computationally expensive.











 
 
 


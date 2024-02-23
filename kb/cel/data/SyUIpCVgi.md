---
title: Model for FIP-047
tags: FIPs
---

**Deprecated --- see https://hackmd.io/R_5EoCfUTPG5UAGK5dy2Cg?both**

# Model for FIP-047

#####  Juan P. Madrigal Cianci, Shyam Sridhar, Tom Mellan
##### GitHub: https://github.com/protocol/CryptoEconLab-private/tree/main/notebooks/FIP-047



##### Related documents: 
- [Notion documen on PoRep bug Policy](https://www.notion.so/pl-strflt/Proof-Expiration-PoRep-Bug-Policy-FIP-XXXX-9c661735caa449d28df98e948b244ab0) 
- [Discussion on Slack](https://protocollabs.slack.com/archives/C03U8PC03CM/p1661976025028949?thread_ts=1661939946.939619&cid=C03U8PC03CM )
- [Tom & Shyam's notes, 08.31](https://docs.google.com/document/d/1tyitlaNpQ8I29-1RQMI-ALClb3DKp42kUsVAGibXlb8/edit#)
- [Shyam's initial model](https://hackmd.io/@1dR0N2W7SQyZWg7DGB8Vfw/SkfqY1zxo)


###### tags: FIPs

----


## Setup and preliminary model
Consider The following parameters:

- $y\in \mathbb{R}_+:$`MaxProofDuration`: the maximum period from last commitment or refresh for which a PoRep is valid, set to 1.5y to match current behavior, 
- $x\in \mathbb{R}_+:$ `ProofRefreshWindow`: a window of time before the `ProofExpiration` epoch when the proof can be extended,
- $t\in\mathbb{R}_+$: which represents time,
- $t_0\in\mathbb{R}_+$: the time at which the bug was discovered,
- $\theta\in\Theta$:  the set of all other possible parameters $\theta$ in an abstract space $\Theta$ that could be used in our setting,

Given this, denote by $\mathsf{M}:=\mathbb{R}_+\times\mathbb{R}_+\times\mathbb{R}_+\times\Theta$ the *parameter space*, i.e., the set where our parameters live. The goal of these notes is to the first model and then optimize with respect $\mathsf{M}\ni m:=(x,y,t,\theta)$ a given utility function $u:\mathsf{M}\to \mathbb{\mathbb{R}_+}$, which assigns a positive number associated to the utility (or profitability, or gain) associated with a given choice of parameters $m\in\mathsf{M}$. 

In particular, we propose the utility function:


\begin{aligned} 
u(m)&= \underbrace{\mathbb{E}\left[ \text{R}(m) - r(m)-\omega(m) \right]\mathbf{1}(t\leq y)}_\text{I}\\
&-\underbrace{(\mathbb{E}\left[ \text{R}(m)-P_f\right]\mathbf{1}(t\leq \min\{x-t_0,y\})}_\text{II}\\
&-\underbrace{\left(\lambda_1 C_e(m)+\lambda_2 C_G(m)\right)}_\text{III}.
\end{aligned}
Here,
- $R:\mathsf{M}\to\mathbb{R}_+$ represents the aggregate rewards obtained from the chain,
- $r:\mathsf{M}\to\mathbb{R}_+$ is the resealing cost,
- $\mathbf{1}(x\in S)$ is the indicator function which is equal to 1 whenever $x\in S$, for some arbitrary set $S$, and it's 0 otherwise,
-  $\omega:\mathsf{M}\to\mathbb{R}_+$ is the renewal cost,
-  $P_f$ is the penalization fee,
-  $\lambda_1,\lambda_2\in\mathbb{R}$ are Lagrange multipliers, and 
-   $C_e(m)$, $C_G(m)$ are the equipment and block-size constraints, respectively.

The proposed form for $u$ has the following three components:
- Component $\text{I}$ corresponds to the profit associated with resealing,
- Component $\text{II}$ corresponds to the profits associated with choosing **not** to reseal and letting the sector get terminated, and lastly,
-  Component $\text{III}$ corresponds to the hardware and block-size constraints. 

Given this, one can define the feasibility region $B$ as a function of $m$ as  

$$ B:=\left\{(x,y,t,\theta)=m \in\mathsf{M} \text{ such that } u(m) \geq 0 \right\},$$

i.e., the subset $B$ of $\mathsf{M}$ for which it is more profitable to reseal. We will assume that in the limit case where the costs of resealing or not resealing are the same (i.e., $\{m\in\mathsf{M}: u(m)=0\}$), the storage provider would choose to reseal. 

It is also of interest to find $m^*$ that solves Problem 1:


$$m^*=\text{arg }\underset{m\in B}{\max} u(m) \tag{Problem 1},$$

which can roughly be interpreted as *find $(x^*,y^*,t^*,\theta^*)$ over all possible parameter combinations in the feasibility set $B$ such that $u(m)\geq 0$ is maximized*. Notice that since we are optimizing over the set $B$, it is implied that resealing is the more profitable option. 


Perhaps a simpler and more realistic approach would be to solve Problem 2, given by 


$$x^*=\text{arg }\underset{x\in\mathbb{R}_+\cap B }{\max} u(x,y',t,\theta') \tag{Problem 2},$$
for some fixed values $(y',\theta')\in\mathbb{R}_+\times\Theta$, understood as finding $x$, i.e., the `MaxProofDuration`, which maximises $u(x,y',t,\theta')\geq 0$. Once again, notice that we are optimizing over the set $B$ (or more precisely, over $\mathbb{R}_+\cap B$), which implies that resealing was the more profitable option. 


## Next steps and questions to discuss

- Given the discussion above, we need to provide models for $R, C_e, C_G$, as well as values for $r,\omega, P_f$. 
- Notice that many of the quantities in our formulation are random variables, as they might depend on random quantities such as gas, base fee, etc. This means that we are tackling an Optimization Under Uncertainty (OUU) problem, which can be tricky/computationally expensive to solve. 
- This formulation is given for a particular sector. In general, however,  different sectors will have different (random) parameters that will in turn affect their profitability and/or our formulation, as in this case, the solution $x^*_i$ to Problem 2 for sector $i$, would be itself a random variable. In this case, one would then need to do a Monte Carlo on $x^*_i$. 







## Potentially relevant datasets

The following datasets might be relevant:

- [`chain powers`](https://lilium.sh/data/models/#chainpowers)  Power summaries from the Power actor.
- [`market deal proposals`](https://lilium.sh/data/models/#market_deal_proposals) All storage deal states with the latest values applied to `end_epoch` when updates are detected on- chain.
- [`miner locked funds`](https://lilium.sh/data/models/#miner_locked_funds) Details of Miner funds locked and unavailable for use.
- [`Miner sector info`](https://lilium.sh/data/models/#miner_sector_infos)Latest state of sectors by Miner.

-----
##  Model I: Rewards by storage provider


We begin by focusing on solving $\text{(Problem 2)}$ from the perspective of a Storage Provider (SP). We begin by [recalling the current rewards model for SPs](https://spec.filecoin.io/systems/filecoin_token/block_reward_minting/). 

Let $n\in\mathbb{N}$ denote an arbitrary epoch (of duration $\tau=30$s), and consider an universe of $N_{sp}\in\mathbb{N}$ SPs, where the $i^\text{th}$ SP, provides a proportion $p_i\in[0,1]$, of the total storage in the Filecoin network. Here, it is understood that $\sum_{i=1}^{N_{sp}}p_i=1$. 

[It is known](https://spec.filecoin.io/systems/filecoin_token/block_reward_minting/) that the newly-obtained rewards of the $i^\text{th}$ SP at the  $n^\text{th}$ epoch are given by

$$\tilde{r}_i(n)=s_i(n)+P_i(n,\theta),$$

where $s_i:\mathbb{N}:\to\mathbb{R}_+$ are the newly obtained rewards from storage deals, and $P_i:\mathbb{N}\times\Theta\to\mathbb{R}_+$ are the freshly-minted block rewards assigned to the $i^\text{th}$ SP at epoch $n$. Here, $s_i(n)$ is a known constant for each SP, as it is decided since $n=0$ the block rewards $P_i(n,\theta)$ are a random variable obtained from the following process: 

1. For a given epoch $n$, set $P_i(n,\theta)=0$, and sample a number of blocks $W(n)\overset{\text{iid}}{\sim}\text{Poisson}(\lambda=5)$. 
2. If $W(n)\neq 0$, then,
    
    for $j=0,\dots,W(n)$, with probabiilty $p_i$, set 
    $$ P_i(n,\theta)=P_i(n,\theta)+\text{win}_i(n,\theta), $$
where 
$$\text{win}_i(n,\theta):=\frac{\max\left\{\overline{\text{Mint}}(n,\theta)-\overline{\text{Mint}}(n-1,\theta),0\right\}}{5},$$

with $\overline{\text{Mint}}(n,\theta)$ the [cummulative minting function](https://spec.filecoin.io/systems/filecoin_token/block_reward_minting/). It is known that such a minting function depends on a variety of paremters that we are here characterizing by $\theta\in\Theta$. 


From this, we can define the cummulative rewards function $R_i:\mathbb{N}\times\Theta\to\mathbb{R}_+$ by 

$$ R_i(n,\theta)=\sum_{k=0}^n \tilde{r}_i(k,\theta),$$

understood as the total rewards (i.e., storage fees plus block rewards) obtained by the $i^\text{th}$ SP, from epoch $0$ through epoch $n$. 









For simplicity, we will assume the following:

1. A bug in the PoRep algorithm is discovered at time $t_0=0$.
2. Throughout the times considered, there are no sector faults, and as such, the SP does not incur into a `Sector Fault` fee or a `Sector Fault Detection`


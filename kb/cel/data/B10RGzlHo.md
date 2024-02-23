---
tags: Gas, Research WIP
---

# Adjustable Target Block Size for EIP 1559

## Abstract
We present a possible modification to the EIP 1559 transaction fee mechanism where the target block size becomes an adjustable dynamic parameter. We argue that the current EIP 1559 formulation works as intended when block space is in very high demand, however in low demand periods the block usage dynamics would deviate from what rational miners would do in a first price auction mechanism. Our proposal addresses this issue by adjusting the target block size by maximizing a target function that can be chosen to maximize miner utility.
## Introduction

In this document we provide motivation and possible mechanisms for introducing a variable target block size for the EIP 1559 mechanism, which is currently used to set the base fee in Filecoin.

Let $r_t$ denote the base fee at a given time $t$. Time $t$ here is to be understood as a discrete variable, synonymous with block epoch. 

The base fee at the next epoch is given by the current base fee, as well as the current block size, which we denote as $B_t$, and target block size, which we denote as $B^T$. The base fee then evolves according to the  EIP 1559 rule:
$$r_{t+1}=\left(1+c\frac{B_t-B^T}{B^T}\right)r_t,$$
where $c=1/8$. Furthermore, the block size is restricted to $B_t\in[0,2B^T]$

The rationale is that base fee should adjust according to network usage demand. If the current block size is larger than the target block size, then base fee should increase to relieve congestion, and if current block size is smaller than the target block size, then the network is being underutilized and base fee should be lowered.

Currently the value for the target block size, $B^T$, and maximum block size, $2B^T$, in gas units, are set by engineering constraints. The question to fix $B^T$ is *what is the maximum block size that the network can process consistently?* The maximum block size $2B^T$, is fixed by answering the question *what is the maximum block size that the network can process if  ocassionally needed, but not in a sustained manner?*

Here we question whether fixing the value of $B^T$ should only be an engineering constraint, and whether economic incentives should play a role in fixing the target block size, as well as whether a dynamic, adjustable target block size is needed.

## Motivation, hyperdrive and batch balancer

To understand why we should have a variable target block size, we must ask what is it we want the EIP 1559 mechanism to do. The original motivation for EIP 1559 is not to manipulate or alter transaction fees, but to make the transaction fee process more predictable and user friendly.



Here we want to show that despite the original motivation, EIP 1559 does manipulate transaction fees, in a way that is different to what miners (or storage providers) would freely choose to do in the first price auction mechanism, in the case where demand is low, relative to the capacity of the blockchain.


An illuminating case study is what happened in the Filecoin network with the introduction of Hyperdrive [cite]. Hyperdrive introduced a new much more efficient method to process proofs for sectors, in which proofs can be aggregated as a batch of proofs. This technological advance promised to increase the capacity of the Filecoin blockchain by 10X to 25X. 

This resulted in a sudden increase in blockchain capacity, without a corresponding change in demand. A clear consequence can be seen in the change in behavior of total network revenue upon the release of hyperdrive. The sudden increase in capacity lead to a steep decrease of the base fee, which meant the total amount of token burn to process transactions decreased after hyperdrive in June 2021.
![](https://i.imgur.com/koAXQLw.jpg)

In a world without 1559, miners may see this decrease in total network revenue as a "bad deal", **they may choose instead not to use all the new capacity provided by the new technological advance, but instead restrict the capacity, and release it only according to existing demand, in a way that would maximize their revenue**. EIP 1559 therefore requires miners to fill a block size that has too much capacity, relative to current demand, or else base fee starts to drop.

This for instance has not been a noticeable problem in Ethereum, where the EIP 1559 was introduced, since demand for that blockchain greatly exceeds its capacity at the moment, so the logical choice for miners would be to use all the block space they have available.

We mention that a mechanism, the **batch balancer** was introduced on top of Hyperdrive in Filecoin to address this problem of controlling the release of capacity. This mechanism works by artificially increasing the cost of aggregate batched proofs when network demand is low. This makes it irrational to batch proofs for your sectors at low demand. Once network demand crosses a given threshold, the cost of batch proofs becomes lower than that for single proofs, and it becomes rational to batch. Therefore the batch balancer releases the batching technology only when there is enough network demand to make this desirable. 

Here we seek to establish a more general mechanism that does a job similar to the batch balancer, but is more agnostic to whatever  type of future technological improvement, and generally releases block capacity in a way that corresponds with network demand. 

## Utility functions in first price auction vs EIP 1559

In this section we introduce some game theory concepts which are necessary to understand the difference in incentives of EIP 1559 vs. a first price auction (Bitcoin-like) mechanism. 

We base our analysis on the utility functions for myopic miners, as were presented in [Roughgarden (2020)](https://timroughgarden.org/papers/eip1559.pdf). We, however greatly simplify the notation and presentation, sacrificing some rigor for the sake of clarity and brevity.

Myopic miners are defined as those whose utility they want to maximize equals their net revenue from the current block (not accounting on what they could earn on future blocks). Block rewards and data deals also provide them positive utility, but are left out of this analysis, since they don't change under first price auction or EIP 1559 mechanisms. 

In contrast to [Roughgarden (2020)](https://timroughgarden.org/papers/eip1559.pdf), we will assume there are no *fake* transactions that are submitted by the miner. It was shown under both first price auction and EIP 1559, these transactions would provide negative utility to the miner, so we will assume miners will not include them.

**First price auction utility function for myopic miners:** Let $M$ represent the mempool of all transactions that want to be included in the current block. Let $B\in M$ represent the subset of real transactions that are actually included in the current block. 

If $j\in B$ is one transaction that was included in the block, then we define $g_j$ as the amount of gas that was used by that transaction, and $p_j$ as the price that was paid by the user per unit of gas for that transaction. We define $\mu$ as the operational cost per unit of gas to the miner for including a given transaction, *i.e.* how much it costs them to include a transaction with a certain amount of gas on the block, vs not including it.

The utility function for myopic miners under a first price auction mechanism is then,
$$u_m=\sum_{j\in B\in M}(p_j-\mu)\cdot g_j$$

It is then clear that **the miner's utility is maximized by maximizing the total network revenue: $TNR=\sum_{j\in B\in M}\,p_j\cdot g_j$**, and it can be assumed that a rational miner will only include transactions for which $p_j\ge \mu$.

**First price auction utility function for users:**
Each transaction sent by a user has a given value, $v_j$ that the user assigns to it per unit of gas. This describes how much the user would actually be willing to pay to have their message included (even if they ended up paying less than that).

The utility for the user who submitted the transaction $j$ is then given by,
$$u_j=(v_j-p_j)*g_j$$
Note that for rational users and miners, a transaction will only take place if $u_j\ge 0$ and $u_m\ge 0$.

The value that  users assign to their transactions depends on their personal preferences, but we could roughly model these values as being drawn from some *value distribution*,
$$f(v_j),\,\,\,\,{\rm with}\,\,\,\,\int_{0}^\infty f(v_j)\,df_j=1,$$
where $f(v_j)$ is a monotonically decreasing function. This distribution should capture the fact that there are many users who would be willing to pay to include their messages if the gas costs are low, and decreasingly fewer users willing to pay as the gas costs become higher. For later convenience we also define the cumulative value distribution as
$$F(v)=\int_0^v f(v^\prime)dv^\prime.$$

**EIP 1559 utility function for myopic miners (the ETH case)**

The main difference in utility functions between the first price auction and EIP 1559 formalisms is the introduction of a *base fee*, $r$, which is set algorithmically, and which a minimum payment per unit of gas that all transactions must paid to be included on chain. This base fee payment does not go directly to the miner, but instead it is burned. As argued in [Roughgarden (2020)](https://timroughgarden.org/papers/eip1559.pdf), the miner utility is then,
$$ u_m=\sum_{j\in B\in M}(p_j-r-\mu)\cdot g_j$$
whie the user utility remains the same
$$u_j=(v_j-p_j)\cdot g_j$$

As was argued in [Roughgarden (2020)](https://timroughgarden.org/papers/eip1559.pdf), the optimal strategy for a user that wants to guarantee their transaction is included in the block, is to make a payment that only barely covers the base fee and the operational costs, that is, their optimal strategy is to pay,
$$ p_j=r+\mu+\epsilon_j$$,
where $\epsilon_j$ can be vanishingly small and their transaction would still be guaranteed to be included.

In this case, according to the miner utility defined above, under EIP 1559, with rational users, miners have very small utility, that only barely hovers above zero, $u_m=\sum_{j\in B\in M} \epsilon_j*g_j$.


**Burning reward term:** We belive the miner utility function for EIP 1559 as defined in [Roughgarden (2020)](https://timroughgarden.org/papers/eip1559.pdf) is actually not complete, as it fails to account for the fact that miners actually benefit from other users burning their base fees, even if in a less direct way than if they were being paid those fees. Fee burning is meant to reward every user in the network, by reducing the circulating supply, therefore providing a deflationary pressure and making other tokens more valuable.  The benefit that fee burning provides to a given miner depends on what is the circulating supply, and how many tokens does the miner hold. 

Let $S$ be the circulating supply, and $W_m$ be the amount of tokens held by miner $m$, (including their wealth of previously held tokens and their income for the current block via block reward and miner tips).

We assume the value added to the miner from other users burning their base fees is given by how much this burning increases the fraction of the total circulating supply that they own.  *The underlying assumption here is that the total market cap remains roughly constant after burning* so now the miner owns a larger share of the market cap.

We therefore modify the miner utility function by adding a term that captures how much more valuable the miner's wealth becomes after other users burn their tokens.
$$ u_m=\sum_{j\in B\in M}(p_j-r-\mu)\cdot g_j+W_m\left(\frac{S}{S-\sum_{j\in B\in M}r\cdot g_j}-1\right)$$

$$ =\sum_{j\in B\in M}(p_j-r-\mu)\cdot g_j+W_m\left(\frac{S}{S-\sum_{j\in B\in M}(p_j-\mu-\epsilon_j)\cdot g_j}-1\right)$$

We note that similarly to the first price auction case, *miner utility is maximized by maximizing total network revenue*, $\sum_{j\in B\in M}p_j\cdot g_j$.



 

## The infinite blockchain problem

We will present an extreme scenario in this section which showcases the main diferences between first price auctions and EIP 1559, and the miner's ability to maximize their utility.

We propose a simple thought experiment of considering a blockchain with infinite block size. This means in practice a blockchain where the entire mempool, $M$ fits entirely in the block every time. 

Let us first examine how a rational first price auction miner would behave in the infinite blockchain scenario, where they are seeking to maximize their utility, by maximizing the total network revenue, $\sum_{j\in B\in M}p_j\cdot g_j$.



The main problem with the infinite blockchain is that if every transaction fit in the block without any competition, this would drive down the gas costs all the way to $p_j=\mu$, resulting in zero utility to the miner. 

### First price auction and effective block size

Miners in first price auctions **are however free to not include all of the transactions in the block, if they don't want**. A rational miner would realize that they can increase their utility by introducing an artificial **effective block size**, $B^*$, a finite amount of gas that they will admit into the block. We denote $B_M$ as the total amount of gas of every transaction in the Mempool.

To understand how an effective block size would affect the total network revenue, we invoke the user's value distribution as defined above. Using the value distribution we could find out what would be the gas cost $p^*$ users would have to pay to include their message on chain, if the miners have imposed an effective block size, $B^*$. The gas cost is given by the relation,
$$1-\frac{B^*}{B_M}=F(p^*)$$, or
$$p^*=F^{(-1)}\left(1-\frac{B^*}{B_M}\right)$$
where $F^{(-1)}$ is the inverse of the cumulative value distribution.

The total network revenue at this point is given by 
$$ TNR^*=B^*\cdot F^{(-1)}\left(1-\frac{B^*}{B_M}\right)$$

Recall that first price auction miners are seeking to maximize the total network revenue, so thery will choose the effective block size, $B^*$, which maximizes this revenue,
$$B^*={\rm ArgMax}(TNR)$$

Notice that this issue of miners artificially restricting the effective block size is only an issue when the effective block size is smaller than the target block size that the blockchain can handle. If the blockchain can only process a block size $B^T$, but the optimal effective block size is larger, $B^*>B^T$, then miners would still use the full capacity of the blockchain. This is why the issues we are discussing here have not been relevant to Bitcoin or Ethereum, since there is typically much more demand to use the block space than they can handle.

### EIP 1559 induced deviation from free-market behavior

We now arrive at the problem of the infinite blockchain with EIP 1559. The target $B^T$ in EIP 1559 is set by engineering constraints, by what is the maximum block size that can be consistently processed. In this case, even if that is not infinite, but still much larger than the optimal  effective block size, $B^T\gg B^*$, then the EIP 1559 mechanism will quickly decrease the base fee until it is close to zero.

Since the target block size is hardwired into the EIP 1559 mechanism, the miners are not able to change this if it is too high, compared to current network demand, and it is far from the optimal block size for maximizing their utility. 

If EIP 1559 is meant to emulate and improve upon first price auction dynamics, then it must have a mechanism to adjust the target block size, according to demand, specially when the demand is consistently lower than the block capacity. 


















## Adjusting EIP 1559 target







We present a possible solution to this problem, which is an EIP 1559 mechanism, with an adjustable target block size.


The base fee is evolved with the following two-step formula,
$$r_{t+1}=\left(1+c\frac{B_t-B^T_t}{B^T_t}\right)r_t$$
$$ B^T_{t+1}=H(T_{t},T_{t-1},B_t,B_{t-1})\cdot B^T_{t}$$
where the target block size now is also dynamic.

We introduce the concept of a target function, $T_t$, which is the quantity that we seek to maximize by adjusting the target block size.

In the examples we have discussed above, if we want this  EIP 1559 mechanism to emulate first price auction dynamics, the target function would correspond to the total network revenue, $T_t=TNR_t$. 

We will keep the target function, however, more generic, and we could choose to maximize something other than total network revenue if we wanted. For instance we will later see some issues that are specific to Filecoin miner utility, that mean that the target used for Filecoin should be different.

Defining the quantities, $\Delta T_t=T_t-T_{t-1}$, and $\Delta B_t=B_t-B_{t-1}$, then our updating rule should satisfy the following properties in order to maximize the target,

$$H(T_{t},T_{t-1},B_t,B_{t-1})=H(\Delta T_t, \Delta B_t)$$
and:

If $\Delta T_t> 0$ and $\Delta B_t> 0$, then $H(\Delta T_t,\Delta B_t)>1$.

If $\Delta T_t> 0$ and $\Delta B_t< 0$, then $H(\Delta T_t,\Delta B_t)<1$.

If $\Delta T_t< 0$ and $\Delta B_t> 0$, then $H(\Delta T_t,\Delta B_t)<1$.

If $\Delta T_t< 0$ and $\Delta B_t< 0$, then $H(\Delta T_t,\Delta B_t)>1$.

The idea being that if gas usage increased, and this was a good outcome for the target function, then the target block size should be increased to incentivize even more gas usage, and so on for the other scenarios.

There are different possible formulas that can acheive the same result, but one simple example for instance is a linear function, as
$$H(\Delta T_t,\Delta B_t)=1+g\Delta T_t\Delta B_t,$$
with some parameter $g$ to be specified. 

### Refining the linear evolution rule
Let us first examine the function,
$$H(\Delta T_t,\Delta B_t)=1+g\Delta T_t\Delta B_t,$$
While the simplicity of this linear rule is appealing, there is a problem here that is not present for the standard EIP 1559 rule. The quantities $\Delta T_t\Delta B_t$ are not necessarily bound (depending on the definition of the target function). They could be arbitrarily large,



One way to work around this issue of unbounded $\Delta T\Delta B$ is to use a Sigmoid function which has an asymptotic bound, for instance,
$$H(\Delta T,\Delta B)=1+g_1\tanh\left(g_2\Delta T\Delta B\right)$$. 







While this solves the problem of arbitrarily high values, it may be computationally difficult to implement a $\tanh$ function on chain in real time.

There is another problem present in the new time evolution rule, which is that the target block size is not bounded, while in reality it needs to be a value between $0$ and $B^T$.

The bound for the target block size to be above zero, is actually enforced by the linear rule, as long as $H(\Delta T,\Delta B)>0$, which is guaranteed by the Sigmoid rule presented here, if we choose $0<g_1<1$. We can understand this by examining what happens when $B_t^T$ is close to (but above) zero, yet still the evolution rule requires it to keep decreasing, as $\Delta T_t\Delta B_t<0$. In this case we would have $0<H(\Delta T_t\Delta B_t)<1$, which means $B_{t+1}^T$ will get closer to zero than $B_t^T$, but will never go below zero.


While we allow the target block size to be dynamic now, we shouldn't allow it to go above the current target block size, $B^T$, as this is chosen to be the largest target block size we can consistently process. Therefore we need an evolution rule that prevents the dynamic target block size from going above $B^T$. There are two possible solutions to this:

#### Conditional statement evolution

One straight forward solution to keeping the dynamic target block size within bounds, is to follow the perscribed time evolution, only if that won't mean violating the bounds. The rule would look as follows:
$$ \begin{array}{cc}
{\rm if}& H(\Delta T_t\Delta B_t)\cdot B_{t}^T<B^T\\
& B_{t+1}^T=H(\Delta T_t\Delta B_t)\cdot B_{t}^T\\
{\rm else}&\\
&B_{t+1}^T=B_{t}^T
\end{array}$$
This rule has the advantage of being simple enough to implement and understand, while having the disadvantage of being less symmetric relative to both bounds at 0 and $B^T$, as well as throwing away arbitrary amounts of information once the target block size is close enough to $B^T$. 

#### Symmetric evolution rule

Another approach is to come up with an evolution rule that displays similar behavior when $B_t^T$ is close to 0 and when it is close to $B^T$. 

As we discussed, if $\Delta T_t\Delta B_t<0$, then $B_{t+1}^T$ will keep getting closer to zero, but never going negative. We can design a rule that will replicate a similar behavior for the upper bound.

We will introduce some shorthand notation, $H_t\equiv H(\Delta T_t\Delta B_t)$.

We need an evolution rule that satisfies,
$$B_{t+1}^T\approx H_t B_t^T,$$
for $B_t^T\approx 0$, and similarly only gets closer but doesnt surpass $B^T$, so it satisfies,
$$B^T-B_{t+1}^T\approx (1-H_t)\cdot(B^T-B_t^T),$$
for $B_t^T\approx B^T$.

There is more than one way to design a function with such limits, but one possible solution is a general rule of the form:
$$B_{t+1}^T=\left(\frac{B_{t}^T}{B^T}\right)^2\left[(1-H_t)B_t^T+H_tB^T\right]+\frac{(B^T-B_t^T)^2}{(B^T-B_t^T)^2+(B_t^T)^2}H_tB_t^T.$$






## Target function to maximize, ETH vs FIL

As previously discussed, in Ethereum, miners would benefit from maximizing the total network revenue, such that this could be an appropriate target to use as $T_t$ in the proposed target block size updating formula.

The situation is a bit more subtle in Filecoin, as the Storage Provider (SP) utility function is different.

The main difference between miner utility in Ethereum vs Filecoin is that the majority of gas usage in Filecoin is done by the miners themselves. 

This is because Proving storage in Filecoin consumes large amounts of gas, much more than any other current usages in Filecoin.

This balance may shift upon the introduction of FVM, which may drive other ways to use Filecoin gas.

Since SP's themselves are the largest users of gas, it is not clear that they would want to maximize total network revenue, since this would increae their own costs

### Utility function for Filecoin SPs

The main new ingredient for Filecoin is that miners are large consumers of gas. Let us define $B_m$ as miner $m$'s average gas consumption rate, the amount of gas they are expected to use on a given block.

We can see the breakdown of gas usage in filecoin below, where all of the gas usage methods except "Others" correspond to SP activity. We see that SP activity makes up the vast majority of gas usage.
![](https://i.imgur.com/NzfMaks.png)


The SP utility is then,
$$ u_m=\sum_{j\in B\in M}(p_j-r-\mu)\cdot g_j+W_m\left(\frac{S}{S-r\left(\sum_{j\in B\in M} g_j+ B_m\right)}-1\right)-r\cdot B_m$$

The introduction of the new negative term, $-r\cdot B_m$ means this utility function is no longer maximized

**The main complication is that what quantity needs to be optimized varies from 
SP to SP, one cannot come up with one target to optimize that will make all SPs happy at once**.

Let's simplify by assuming the first term is roughly zero, since rational users should use miner tips to barely cover operational costs,
$$u_m\approx W_m\left(\frac{S}{S-r\left(\sum_{j\in B\in M} g_j+ B_m\right)}-1\right)-r\cdot B_m$$

### A universal target for Filecoin

The utility function to be maximized varies from SP to SP. However with some simple, (yet perhaps unrealistic) assumptions.

Let us define the qualtiy adjusted power for SP $m$ as $p_m$, and $P$ is the total network QAP. The SP therefore controls a fraction $f_m\equiv p_m/P$ of the network power.

As a **simplifying assumption** that may or may not be very well justified, let us sa the a miner's wealth and burn rate scales with the same power fraction,
$$W_m=f_m W$$,
$$B_m=f_m B$$,
where $W$ is the total wealth held by all SP's, and $B$ is the total burn rate from all SPs.

We assume also that for most SP's, $f_m$ is small, since no one should control a large enough fraction of the network. We can therefore perform an expansion of the utility function in powers of $f_m$,
$$u_m\approx f_m\left[ W\left(\frac{S}{S-\sum_{j\in B\in M}rg_j}-1\right)+B\left(-r+f_m\frac{W S}{(S-\sum_{j\in B\in M}rg_j)^2}\right)\right]+\mathcal{O}\left(f_m^3\right)$$

Keeping only up to first order in $f_m$, we arrive at

$$u_m=f_m\left[ W\left(\frac{S}{S-\sum_{j\in B\in M}rg_j}-1\right)-r\cdot B\right]$$
Note that importantly, at this order in the expansion, all the SPs would benefit by maximizing the same target function! so  for our adjustable EIP 1559 formalism, we could use the target function,
$$T_t= W\left(\frac{S}{S-\sum_{j\in B\in M}rg_j}-1\right)-r\cdot B,$$
where it would be necessary to keep track of the total wealth held by all SP's, the circulating supply, the total burn rate from all SP's as well as the total network revenue. 

## Incentivizing something else?

So far we have focused on creating the conditions such that this modified EIP 1559 mechanism is able to emulate what miners would freely do in a first price auction setting. 

At this point, however, we are free to wonder if this is what we want our EIP 1559 to do, or if we could use the opportunity to incentivize some other desirable behavior.

For instance we have been discussing the target function $T_t$, which is the quantity that this mechanism tries to maximize. We have chosen such that it provides the maximum utility to the miners. We have made this choice becasue this is what miners would do in a first price auction setting, choose to maximize their own utility.

The target function $T_t$ however, also presents an opportunity to incentivize something else that miners wouldnt do on their own with first price auctions. One could think for instance of adding a term that favors network Power growth, with some weight, $a$, such as
$$T_t =W\left(\frac{S}{S-\sum_{j\in B\in M}rg_j}-1\right)-r\cdot B+aP.$$



## Appendix: Equilibrium base fee values. 

It is easy to calculate what would be the appropriate equilibium base fee which corresponds to a constant level of demand.

Suppose there is a constant level of demand, here represented as Mempools having a a constant size $B_M$. EIP 1559 is designed to, in such a constant demand case, find the equilibrium base fee, defined as a base fee that would remain constant under EIP 1559, if the demand remains constant. 

In reality there will always be many random fluctuations  around a constant level of demand, and value distributions from users may vary with time, however we still think there is value in understanding this theoretical concept of equilibrium base fee.

In EIP 1559, the equilibrium base fee would be one that given a mempool $B_M$, would lead to a block size $B^T$. With the previously defined value distributions, the equilibrium base fee is given by
$$r^{\rm eq}=F^{(-1)}\left(1-\frac{B^T}{B_M}\right)$$


We now find the equilibrium base fee with our proposed mechanism, in the simple case where we assume the target being maximized is total network revenue, or $T_t= \sum_{j\in B\in M}rg_j$

This calculation is done in two steps, first we calculate what would be the equilibrium target block size, which is the one that maximizes $T_i$ for a given constant demand, and then calculate the equilibrium base fee for that target block size.

As discussed before, the target block size would be given by 
$$B^{\rm eq}={\rm Min}\left\{B^T, {\rm ArgMax}\left[B^*\cdot F^{(-1)}\left(1-\frac{B^*}{B_M}\right)\right]\right\}$$

The equilibrium base fee is then given by
$$\rho^{\rm eq}=F^{(-1)}\left(1-\frac{B^{\rm eq}}{B_M}\right).$$

Since $B^{\rm eq}\ge B^T$, and the fact that $F(v)$ is a cumulative distribution, this implies that 
$$\rho^{\rm eq}\ge r^{\rm eq}.$$
---
title: FVM and base fee - analysis
tags: Econ monitor, Gas
---

# FVM and base fee. Part I:  Analysis.

**This document is for private use only.**


### Summary
* This is the first of an ongoing series of short reports analyzing the impact that the Filecoin Virtual Machine (FVM) will have on chain-usage patterns across several scenarios and outlooks. 
* While the FVM is a *net positive* to the network, it is essential to understand some *worst-case* or *pathological scenarios* that could arise from the (expected) increase in network usage.
* We begin by defining a concept of miner utility and then proceed to investigate the question: *given our definition of miner utility, what is a base fee that, if held on average, could start hurting the network by, e.g., discouraging miners to prove storage or onboard data*?
* Under our definition of miner utility (see Section 1), we estimate two  *magic numbers* that are worth monitoring:
    * 🟠  20 nanoFIL/gas unit as the base fee as an upper limit for miner profitability (in terms of our definition of utility), and 
    * 🔴  70 nanoFIL/gas unit as a base fee that could potentially hinder the miner's ability to submit storage proofs.
    * For context, a quick, conservative, *back-of-the-envelope* calculation suggests that at the current daily gas usage of 50 000 Billion gas units, sustaining a base fee around those values would imply that the network is burning 1M FIL/day and 3.5M FIL/day. The current circulating supply is roughly 405 M FIL, and it is increasing at a rate of about 0.5M FIL/day (from starboard).
* It is worth mentioning, however, that these values are only harmful if the base fee consistently oscillates around them for an extended period (e.g., more than a day). Having a brief (several epochs) spike in some of these values is not necessarily concerning. 
* A key observation is that miners have some control over this increase in the base fee; at the current state of the chain, most of their revenue comes from block rewards (as opposed to the so-called tip and storage deals), while most of their epoch-to-epoch expenses (excluding any potential locking or penalties) are due to sending messages. It is in their interest to keep the base fee from reaching these levels. 


### 1. Introduction and setup.

#### Understanding miner utility

We begin with a definition. We denote the *expected miner utility* of the $j^\text{th}$ miner at an epoch $t$, by
\begin{aligned}
\mathsf{Utility}_{t,j}=\textsf{Expected tokens in}_{t,j}-\textsf{Expected tokens out}_{t,j}.
\end{aligned}
Here, $\textsf{Expected tokens in}_{t,j}$ are the total amount of tokens that the $j^\text{th}$   miner is expecting to receive at epoch $t$ and similarly $\textsf{Expected tokens out}_{t,j}$ are the expected number of tokens that they are going to spend at such an epoch due to messages sent. In this setting, we say that a miner is *profitable* (under our definition of utility) if their expected miner utility is positive. 


***Remark.** Strictly speaking, utility functions are a measure of preference, and as such, one can define utility in several different ways (e.g., over a time interval, above a certain threshold, or adding an inflation-dependent term, to name a few). We chose the definition of utility in the equation above since, on the one hand, it presents an intuitive measure of preference (i.e., a miner would instead perform actions that would keep their utility positive), and on the other, it can be used to derive some upper bounds on profitability (understood as having positive utility)*

In particular, for any given Storage Provider (SP)

\begin{aligned}
\textsf{Expected tokens in}_{t,j}&=:\mathbb{E}[\textsf{Tokens in}_{j,t}]=\underbrace{\mathbb{E}[\textsf{Block Rewards}_j]}_{\text{(I)}}+\underbrace{\mathbb{E}[\textsf{miner tips}_{j,t}]}_{\text{(II)}}+\underbrace{\mathbb{E}[\textsf{Deals}_{j,t}]}_{\text{(III)}},\\
\textsf{Expected tokens out}_{t,j}&=:\mathbb{E}[\textsf{Tokens out}_{j,t}]=\underbrace{\mathbb{E}[\textsf{Gas Expenses}_{j,t}]}_{\text{(IV)}},
\end{aligned}

where for notational simplicity,  we used the symbol $\mathbb{E}[X]$ to denote the expectation of some given quantity $X$. 



Naturally, miners would want a positive utility, i.e., they want to receive, on average, more tokens than what they spend. Currently, the most significant source of income for miners is the expected block rewards, and typically, their primary source of token outflow **on an epoch-to-epoch basis** is due to storage-related messages. We investigate terms **(I)** and **(IV)**  in more detail.


**Block rewards**

**Term (I)** corresponds to the  rewards that the $j^\text{th}$ Storage Provider (SP)  gets, on average, at any given epoch. Recall that in any given epoch, there are $N_t\overset{\text{iid}}{\sim}\text{Poisson}(\lambda=5)$ blocks and that the $j^\text{th}$ SP is randomly chosen (with replacement from the list of all valid miners) to "mine" any of these blocks with probability equal to their relative power in the network, $\rho_j$. The chosen miner gets to include messages and receives a reward for some value $R$ (currently around 20FIL). Thus, we have that, per epoch, the $j^\text{th}$ miner expects to obtain
\begin{aligned}
\mathbb{E}[\textsf{Block Rewards}_j]=\rho_j\lambda R \quad \text{tokens.}
\end{aligned}


**Gas consumption**



**Term (IV)** corresponds to the average amount of tokens an SP needs to spend at any given epoch, e.g., proving storage (`SubmitWindowedPosts`), onboarding data, recovering sectors, etc. For our analysis, we will lower-bound this term, i.e., we will try to determine the minimum, on average, an SP should spend per epoch. To do this, we will first estimate the minimum amount that an SP needs to spend in a day (to provide storage and avoid getting penalized), then divide this number by 2880; the number of epochs in a day. 

Let $\Pi$ and $\Pi_j:=\rho_j\Pi$ denote the total power of the network (in bytes) and the power of SP $j$ (also in bytes), respectively. Furthermore, define a *sector* by $s= 32 \times 10^9$ (Bytes) and a *partition* as $p=2349 s$. Given this, SP $j$ has 

$$N_{p,j}:=\left\lceil \frac{\rho_j \Pi}{p}\right\rceil$$

partitions (where here ''$\left\lceil \cdot \right\rceil$'' denotes the ceiling operator). 

**At a minimum**, each SP needs to submit $N_{p,j}$ proofs of storage (`SubmitWindowedPosts`) every 24 hours. Given that there are 2880 epochs in a day, this averages out to $M_{p,j}=N_{p,j}/2880$ proofs per epoch. Denoting by $g_w$ the average gas usage of these messages,  term  **(IV)** can be **roughly** approximated as 

\begin{aligned}
\mathbb{E}[\textsf{Gas Expenses}_{j,t}]\approx b_t M_{p,j}g_w.
\end{aligned}

We reiterate that the last equation **does not consider other non-`SubmitWindowedPosts` messages**. We choose to do this because we want to lower bound this expenditure term, as it will be discussed in the next section. Naturally, the term $\mathbb{E}[\textsf{Gas Expenses}_{j,t}]$ will increase whenever an SP sends other messages such as `PreCommitSector,` `PublishStorageDeals,` etc. 

***Remark (on notation).** The base fee changes from epoch to epoch as a function of gas consumption. Strictly speaking, the expectation in the previous equation is conditioned on a fixed value of base fee $b_t$, and should be treated as such. Symbolically, we are, with a slight abuse of notation and for the sake of readability, writing $\mathbb{E}[\textsf{Gas Expenses}_{j,t}]$ to denote $\mathbb{E}[\textsf{Gas Expenses}_{j,t}|b_t=x]$.*




## 2. Results and analysis

We present some results that hold for the following reference values:


| Symbol                   | Meaning                                        | Value             | Units     |
|--------------------------|------------------------------------------------|-------------------|-----------|
| $\lambda$                | Average number of blocks per epoch             | 5                 | -         |
| $R$                      | Rewards from winning a block                   | 20                | FIL       |
| $g_w$                    | Average `gasUsed` for a `SubmitWindowedPost`   | 50 000 000        | gas units |
| $\Pi$                    | Network QAP                                    | 19.015            | EiB       |
| $g_\text{pro}$           | Average `gasUsed` for a `PoveCommitSector`     | 67 000 000        | gas units |
| $g_\text{pre}$           | Average `gasUsed` for a `PreCommitSector`      | 45 000 000        | gas units |
| $g_\text{batch}$         | Average `gasUsed` for a `PreCommitSectorBatch` | 100 000 000       | gas units |
| $g_\text{Agg}$                | Average `gasUsed` for a `PoveCommitAggregate`  | 600 000 000       | gas units |
| $\mathsf{BatchBalancer}$ | Batch balancer                                 | $5\times 10^{-9}$ | FIL       |
| $\mathsf{Discount}=1/20$ | Discount Factor                                | 1/20              | -         |
#### 2.1 First result: A threshold for miner profitability.

*** Summary**: miners stop being profitable for base fees of around 20 nanoFIL.*

From the discussion above, it is not difficult to see that the miner utility is positive whenever  the following inequality holds
\begin{aligned}
\frac{\rho_j \lambda R + \mathbb{E}[\textsf{miner tips}_{t,j}]+\mathbb{E}[\textsf{Deals}_{t,j}]}{g_w M_{p,j}}\geq b_t \quad \text{(Condition I)}
\end{aligned}

Conversely, when Condition I does not hold true anymore can roughly be understood as having a base fee so high that it causes *low or no profitability to the miner*.

Interestingly enough, since $M_{p,j}\approx\frac{\rho_j \Pi}{2880 p}$, and since at this current stage block rewards are much larger than miner tips and deals, one then has that the previous equation becomes

\begin{aligned}
&\frac{2880 p\left(\rho_j \lambda R +\mathbb{E}[\textsf{miner tips}_{t,j}]+ \mathbb{E}[\textsf{Deals}_{t,j}]\right)}{g_w \rho_j \Pi}\\
\approx & \frac{2880 p\left(\rho_j \lambda R \right)}{g_w \rho_j \Pi}=\frac{2880 p\left( \lambda R \right)}{g_w\Pi}=\hat{b}_t\underset{\sim}{\geq}   b_t
\end{aligned}

**That is, under this formulation and these assumptions, the threshold for non-profitability is (roughly) the same for all miners!** (indeed, rewards and expenses are relative to the miner power). 

Computing the previous bound with the values described at the beginning of this section yields a limiting base fee $\widehat{b}_t\approx1.97\times 10^{-8}$ FIL/Gas unit, which is equivalent to 19.7 nanoFIL/ Gas unit. 



For reference, during the last year, the base fee has been oscillating between $10^{-16}$ and $10^{-9}$ FIL/gas unit, with a running mean of around $10^{-10}$ FIL/gas unit. Thus, the base fee would need to increase by 10X over the 1-year maximum and 100X over the 1-year average to achieve this boundary. 
 
 Historical base fee over a year           |  base fee last month
:-------------------------:|:-------------------------:
![](https://hackmd.io/_uploads/SkJ3SzE_j.png)  |  ![](https://hackmd.io/_uploads/BkfXh6POi.png)










**Implications.**

* This derivation was made assuming that miners are **only** sending `SubmitWindowedPost'messages. When miners need to submit other types of messages, they will incur additional expenses, hence decreasing the threshold for $\hat{b}_t$. 
* **From the previous bullet point, this value of 20 nanoFIL/gas units can be understood as a threshold for when it is not profitable for the miner to submit messages other than PoSt, including onboarding.**
* It is important to note that this utility is given on an epoch-to-epoch basis. Having a handful of epochs in a day for which Condition I is not satisfied (and hence, the base fee is so high that it makes things unprofitable for the miner) is not catastrophic; however, having demand so high that this situation becomes the norm is concerning.





  
**Critique.** Base fee $b_t$ will, understandably, change through the day. This means that, strictly speaking, the previous equations need to be better defined. One could, perhaps naively, lower bound $b_t$ by $b^*_t$ understood as the minimum base fee in a given day, but this will likely yield a rough bound.


**How long can a miner afford this?**  The utility function considered herein is effectively a "cash flow." A miner $j$ with some wealth (available FIL?) $W_j$ can afford to do this as long as their net balance$W_j-u(B,b_t)$ stays positive (this is, of course, assuming that they are not topping off their account)




#### 2.2 Second result: Onboarding

*** Summary**: an optimistic range on the limiting base fee when including onboarding is between 7 nanoFIL and  18 nanoFIL per gas unit. More realistically, such a number will depend on how much data a particular miner is willing to onboard. Smaller miners are likely to be affected the most. Unsurprisingly, the limiting base fee decreases as a function of onboarding.*

Let us now consider the case where in addition to *just* sending `submitWindowedPoSts` messages; miners are also interested in onboarding a daily amount of data $\mathcal{O}$. For the sake of exposition, we will first derive some results under the assumption below and then present some results that do not rely upon it. 

**Assumptions (on onboarding)**

1. *Each miner onboards an amount of data proportional to their relative power, i.e., for any given amount of data $\mathcal{O}$ to be onboarded by the whole network, the $j^\text{th}$ miner onboards an amount equal to $\mathcal{O}_j:=\rho_j\mathcal{O}$.*
2. *Miners will choose to batch proofs whenever it is cheaper for them to do so.*

While the second assumption is reasonable, we know that the first assumption is much stronger. Nevertheless, we hope that the simplification obtained from such an assumption can bring some meaningful information and hope to study the effects that FVM might have in onboarding in more depth in the future. 


Let $\mathcal{S}_j=\left\lceil \frac{\rho_j\mathcal{O}}{32\times 10^9}\right\rceil$ denote the number of sectors to onboard by the $j^\text{th}$ miner. Under the previous assumptions, and once again assuming that the expected block rewards represent the majority of a miner's income, one has that miner utility as a function of  the  base fee $b_t$ can be approximated as

\begin{aligned}
\textsf{Utility}_{j,t}(b_t)\approx2880\rho_j\lambda R-N_{p,t}g_w b_t-\textsf{OnboardingCosts}(b_t,\mathcal{S}_j)
\end{aligned}

Where $$\textsf{OnboardingCosts}(b_t,\mathcal{S}_j):=\min\left\{b_tg_\text{single}\mathcal{S}_j, b_tg_\text{batched}(\mathcal{S_j}) + \mathsf{BatchGasCharge}(b_t,\mathcal{S}_j) \right\}$$ represents the costs (in tokens) of onboarding $\mathcal{S}_j$ sectors, and where with $\mathsf{BatchGasCharge}$ the batch charge from the [batch balancer](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0024.md).   

Our goal is then to estimate $b^\dagger_t$ such that $\textsf{Utility}_{j,t}(b^\dagger_t)=0$.  Taking as default the values in the table at the beginning of this section and setting $\mathcal{O}=6$ PiB/day (slightly above the current onboarding) yields values between 7 nanoFIL and 18 nanoFIL per gas unit, as shown in the figure below (left). The batch balancer likely causes this difference in the limit base fee. We also plot $b^\dagger_t$ as a function of onboarded data in the figure below (right). The black vertical line represents current onboarding. Smaller miners seem to be the most affected by this. 



 limiting base fee with onboarding  Vs $\rho$         |  limiting base fee with onboarding vs $\mathcal{O}$
:-------------------------:|:-------------------------:
![](https://hackmd.io/_uploads/SyCpt0wdj.png)  |  ![](https://hackmd.io/_uploads/r1yM20Puj.png)







**Relaxing Assumption 1.**

Here we relax the assumption that onboarding is proportional to the relative power but still rely upon the assumption that miners will batch their proofs whenever doing it is more profitable. A similar procedure as before produces the plot below. As we can see, in this setting, smaller miners reach the limiting value faster. 



![](https://hackmd.io/_uploads/BJKs_oLOi.png)




#### 2.3 third result: A Threshold for intentional faults.
 


*** Summary**: If the base fee is around 70 nanoFIL per gas unit for over a day, it is cheaper for a miner to get penalized*



A hypothetical scenario that could hurt the network is when the base fee becomes so large that an SP would rather get penalized than send a PoSt. Given a partition $p$, this happens whenever the cost of getting penalized, together with a later recovery of the partition, is smaller than the cost of sending the PoSt. More precisely, at a given epoch $t$,

\begin{aligned}
\text{Penalisation}_j(p) + b_{s}g_r<b_tg_w, \quad s>  t,
\end{aligned}

With $g_r$, the gas units are required to run a `recovery` message. Notice that, in practice, the decision implied by the previous equation is difficult to make, as it depends on the (clearly unknown) base fee $b_s$ at a later recover epoch $s$. In light of this, we choose to monitor $b_t$ such that.  

\begin{aligned}
\text{Penalisation}_j(p) <b_tg_w.
\end{aligned}

While having a $b_t$ for which the previous bound holds does not necessarily mean that a (rational) miner would instead get penalized, it is likely valuable to understand this threshold.

Here, we define penalization as 3.5 days of expected block rewards. Thus, given that there are, on average, $\lambda=5$ blocks per epoch, and there are 2880 epochs in one day, this becomes 

$$\text{Penalisation}_j(p):=3.5\times2880\times\rho_j\times\lambda\times R\times \underbrace{\left(\frac{\text{partition}}{\text{all partitions miner J}}\right)}_\text{:=$1/N_{p,j}$}.$$

Since $N_{p,j}\approx \rho_j\Pi/p,$ this becomes 

$$\text{Penalisation}_j(p)\approx3.5\times2880\times\rho\times\lambda\times R\times\frac{p}{\Pi}.$$






Given this, we define the **boundary base fee** of the J-th SP as

$$ b'_{j,t}:=\frac{\text{Penalisation}_j}{g_w}\approx \frac{3.5\times2880\times\rho\times\lambda\times R\times p}{g_w\Pi}=3.5 \hat{b}_t, $$

with $\hat{b}_t\approx 1.97\times 10^{-8}$ defined as in the previous section. 


**Implications.**

* In practice, miners will only get penalized if they do not submit a recovery in 24 hours. Thus, base fees should consistently be above 70 nanoFIL per gas unit for over a day. 



## 3. Conclusions and future steps. 



We have presented two bounds on the base fee that is worth monitoring. 

On the one hand, we have shown that, for current values of block rewards, etc., it is not profitable for miners to submit any messages of their own once the base fee is above 20 nano FIL per gas unit. On the other hand, we have shown that it is more profitable for miners to get penalized for a sustained base fee of 70 nanoFIL per gas unit. 

While concerning, we reiterate that such scenarios require that the base fee oscillates around these values for a considerable time. Whether the base fee blows up to such a considerable value depends (at least to some extent) on the miners. *Apriori*, given that (i) miners decide which messages --if any-- to include in a block and (ii) since at this current stage they make the majority of their profits from block rewards (and not tips), they can choose to send *empty (or almost empty) blocks* to reduce the base fee if they decide, as a group,  that such a value is currently too high. This poses an interesting game-theoretic question about the behavior of the miners (are they cooperative?) which should be analyzed further. 

While the 20 nanoFIL/gas unit is a valid threshold for when data onboarding stops, we also aim to understand the effects of base fee on onboarding (and hence, locking) in more depth. This will be the focus of upcoming work. 




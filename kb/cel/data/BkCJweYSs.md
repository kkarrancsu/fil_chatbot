---
title: Saturn reward pool
tags: Saturn aliens, Retrievals
description: Description of how the growth reward pool works
breaks: false
---


# Saturn Reward Pool

#### Maria Silva, November 2022


## Introduction

Within Saturn Treasury, the reward pool is the mechanism that defines how much FIL is available in each payout window. This available FIL is then distributed among the operators based on their relative performance.

Therefore, the reward pool is a key design choice as it ultimately controls how much is being paid to operators and how investment into Saturn is distributed over time.

During the design of the reward distribution component, we ran a [simulation](https://hackmd.io/@cryptoecon/SJIJEUJbs/%2FMqxcRhVdSi2txAKW7pCh5Q#Reward-pool1) to test two possible implementation for the reward pool. In the end, we proposed to use the *growth reward pool* design as it had some advantages over the *constant reward pool*.

In this document, we detail how the *growth reward pool* is defined and how we reached the final parameters.

Note that, on February 2023, Saturn’s growth based payouts model was pause. We discuss the details of this change in the last section.

## Growth Reward Pool

The *growth reward pool* aims to distribute rewards based on the network's growth. The idea is to have a baseline of network growth at each point in time (in this case, the total bandwidth delivered) and to increase the available pool of rewards as the network achieves the defined baseline.

More concretely, given the following variables:

* $B_t$: the actual cumulative bandwidth provided by the network from launch to the payout time $t$
* $\tilde{B}_t$: the cumulative bandwidth baseline set as the goal for the network to deliver between launch and the payout time $t$
* $R$: total reward pool in FIL
* $n$: total number of payouts for the reward pool $R$

we define the available reward pool for payout time $t$ as the difference between the cumulative rewards at payout $t$ and payout $t-1$:

$r_t = R_t - R_{t-1}$

and we define the cumulative rewards at payout $t$ based on the share of bandwidth delivered by the network:

$R_t = R \cdot \frac{\min(B_t, \tilde{B}_t) }{\tilde{B}_n}$

Note that the baseline function $\tilde{B}_t$ can have any formula desired. The shape of the final formula is defined in the next section.



## Deriving the Baseline function

The exact definition of the cumulative bandwidth baseline depends heavily on our assumptions how how much traffic is expected at each point in time. To derive this, we make the following assumptions:

1. Payouts are computed every 30 minutes.
2. The initial reward pool is set to last for the first 12 months of the network.
3. By the end of those 12 months, the network will experience a traffic of 300 TB per day (6.25 TB every 30 minutes).
4. Daily traffic will grow linearly during the first 12 months of the the network, from an initial starting point of 0.5 TB every 30 minutes.

If we define $b(t)$ to be the bandwidth baseline served during the payout perios $t$, because it will growth linearly from 0.5 to 6.25 during 12 months (i.e. $365 \times 24 \times 2 = 17520$ payout periods), we can find its equation by solving the following system:


$$
\begin{cases}
    b(0) = 0.5 \\ 
    b(17520) = 6.25 
\end{cases}
\Longleftrightarrow
\begin{cases}
    0m + b_0 = 0.5 \\ 
    17520m + b_0 = 6.25
\end{cases}\Longleftrightarrow
\begin{cases}
    b_0 = 0.5 \\ 
    m = \frac{6.20}{17520}
\end{cases}
$$

Thus, $b(t) = \frac{6.20t}{17520} + 0.5$. But we don't want to know $b(t)$! What we need is the cumulative bandwidth baseline $\tilde{B}_t$, which is defined as:

$$
\begin{align*}
\tilde{B}_t & =\sum_{n=1}^{t} b(n) =\\
    &=\sum_{n=1}^{t} \left( \frac{6.20n}{17520} + 0.5 \right)=\\
    &=0.5t + \frac{6.20}{17520} \sum_{n=1}^{t} n=\\
    &= 0.5t + \frac{6.20}{17520} \frac{t(t+1)}{2}=\\
    &=0.5t + \frac{6.20t(t+1)}{35040}
\end{align*}  
$$

## Design update - Feb 2023

Since its launch, the Saturn network has experienced massive growth in operator adoption. The original design of a growth pool assumed a linear adoption during a year, while, in reality, operators joined at a significantly faster rate.

Therefore, Saturn now is at a stage where the network has good enough distribution and performance to increase the number of clients it can serve and it should shift focus from increasing supply to increasing demand.

In addition, the overall macro environment and the state of crypto markets make this refocus ever more relevant for the long-term sustainability of the project.

With this in mind, the team was led team to consider pausing the *growth reward pool* design. Having a fixed reward base has two advantages:

1. It is simpler and makes it easier for operators to model their expected earnings.
2. While the growth design is paused, future growth in earnings can only come from increasing Saturn's pool of clients, which is a key priority for the project now. This makes operators more aligned with the task of onboarding more clients.

Now, computing the monthly rewards available for distribution is much simpler. We consider the entire pool of FIL Saturn has collected for the following year and divide it by 12 months. With the current pool, we arrive at a monthly reward of around 30k FIL.
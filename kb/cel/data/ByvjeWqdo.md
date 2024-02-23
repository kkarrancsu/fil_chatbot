---
title: Snapping FIL+ and effective QAP
tags: FIPs
---

# Snapping FIL+ and effective QAP

#### Axel Cortes Cubero, February 2022

## Introduction

Currently the rewards corresponding to FIL+ deals are implemented in such that the extra reward associated with the verified data is spread out over the lifetime of the sector.

Specifically, let's say a sector has lifetime $L$, and total storage space $\mathcal{X}$. Say the sector is sealed with a FIL+ deal, using $\chi_1$ amount of space, for a duration $l_1$. We assume the deal starts at the beginning of the sector lifetime.

As currently implemented, the sector has a constant quality multiplier, $q$, which is assigned for the whole duration of the sector lifetime, even after the deal has expired. This multiplier is computed as

$$q=\frac{m\chi_1l_1+(\mathcal{X}-\chi_1)l_1+(L-l_1)\mathcal{X}}{\mathcal{X}L},$$
where $m=10$ is the quality boost associated with FIL+ deals.

This quality multiplier is used to compute the expected reward and for the given sector. At a given point in time, $t$, the total new block rewards minted are given by $R(t)$, the total raw network power is $P(t)$, and average quality multiplier for all sectors in the network is $Q(t)$, then the instantaneous expected reward rate for the given sector is
$$r(t)=\frac{R(t)q}{P(t)Q(t)}.$$

We introduce the *hat* notation $\hat{y}(t_0;t)$, to mean a prediction of a quantity $y(t)$, at a future time, $t$, using only information known at time $t_0$. Here we will consider $t_0$ to be the time at which the sector was sealed.

The storage pledge for the given sector is then given by
$$SP(t_0)=\int_{t_0}^{t_0+20d}\hat{r}(t_0;t)dt=\int_{t_0}^{t_0+20d}\frac{\hat{R}(t_0;t)q}{\hat{P}(t_0;t)\hat{Q}(t_0;t)}dt$$

The consensus pledge is given by
$$CP(t_0)=0.3\frac{S(t_0)q}{{\rm max}(B(t_0),P(t_0)Q(t_0))},$$
where $S(t)$ is the circulating supply of FIL, and $B(t_0)$ is the baseline function.

## The problem

As can be seen in the previous definitions, $q$ is constant for the lifetime of the sector, If we are to allow for new FIL+ deals to be incorporated later on in the lifetime of the sector, we need to define a mechanism that allows $q$ to change.

More specifially, we examine here the scenario where at some time $t^\prime>t_0+l_1$, another FIL+ deal is added, of space $\chi_2$ and duration $l_2$, such that $t^\prime+l_2-t_0\le L$, that is both deals fit inside the sector lifetime $L$.

## Solution 1: Localized quality multiplier

One solution is proposed, and argued for [here](https://docs.google.com/presentation/d/1eDYXeZAoGrvqsE7jTp3Ln9IIbVDXKbf6SXpn9jpjPrk/edit#slide=id.p4), which consists on changing the timing of the FIL+ extra rewards.

The proposal is to make $q(t)$ dynamic, by making the FIL+ reward concentrate only in the period of time where the deal is active, and drop back to 1 when there is no active FIL+ deal.

In the scenario described before, then the dynamic quality multiplier becomes,

$$q(t)=\left\{\begin{array}{cc}\frac{m\chi_1}{\mathcal{X}},&t_0<t<t_0+l_1\\
1,&t_0+l_1<t<t^\prime\\
\frac{m\chi_2}{\mathcal{X}},&t^\prime<t<t^\prime+l_2\\
1,&t^\prime+l_2<t<t_0+L\end{array}\right.$$

In this case it is simple to add arbitrarily more deals as time goes on, updating the quality multiplier accordingly.

One possible objection to this proposal is that, if say the sector only contains the initial deal, then after time $t_0+l_1$, the reward rate sharply drops, which may weaken the motivation to keep maintaining the sector and not terminating, since sufficient profit to cover termination fee may have been gained in the initial period.

## Solution 2: Spread out, additive qualitive multiplier

A different possible solution is to keep the spread-over-sector-lifetime nature of the quality  multiplier, and simply upgrade the *effective* quality multiplier when a new deal is added.

This approach has a disadvantage of being mathematically more complicated, and of introducing effective quality multipliers which may be larger than $m$.

Considering the two-deal scenario described ago, we first compute what would be the quality multiplier *had both deals been incorporated since the beginning of the sector lifetime*, which we define as,
$$q_{1+2}=\frac{m\chi_1l_1+(\mathcal{X}-\chi_1)l_1+m\chi_2l_2+(\mathcal{X}-\chi_2)l_2+(L-l_1-l_2)\mathcal{X}}{\mathcal{X}L}.$$
The total reward given out in all the lifetime for this sector will be
$$Total\, sector\, reward=q_{1+2}\int_{t_0}^{t_0+L}\frac{R(t)}{P(t)Q(t)}dt$$

Now suppose instead that only the first deal had been incorporated at time $t_0$, and the second deal was only added at time $t^\prime$. We introduce the *effective quality multiplier*, $q^\prime$, which is defined such that the reward given throughout *the remainder* of the sector lifetime is such that the total reward given out through *all* of the sector lifetime is the same as the total sector reward computed above. In this case we have
$$ Total\,sector\,reward=q\int_{t_0}^{t^\prime}\frac{R(t)}{P(t)Q(t)}dt+q^\prime\int_{t^\prime}^{t_0^L}\frac{R(t)}{P(t)Q(t)}dt$$

We note that this calculation is done at time $t^\prime$, such that it involves predicted quantities for what will happen between $t^\prime$ and $t_0+L$. As such the second integral should actualy read,
$$\int_{t^\prime}^{t_0^L}\frac{\hat{R}(t^\prime;t)}{\hat{P}(t^\prime;t)\hat{Q}(t^\prime,t)}dt.$$

We can thus find the effective quality multiplier by requiring equivalence between the two expressions for total sector reward,
$$q^\prime=\frac{(q_{1+2}-q)\int_{t_0}^{t^\prime}\frac{R(t)}{P(t)Q(t)}dt+q_{1+2}\int_{t^\prime}^{t_0+L}\frac{\hat{R}(t^\prime;t)}{\hat{P}(t^\prime;t)\hat{Q}(t^\prime,t)}dt}{\int_{t^\prime}^{t_0+L}\frac{\hat{R}(t^\prime;t)}{\hat{P}(t^\prime;t)\hat{Q}(t^\prime,t)}dt}$$

The time-dependent quality multiplier can then be defined as
$$q(t)=\left\{\begin{array}{cc}q,&t_0<t<t^\prime\\q^\prime,&t^\prime<t<t_0+L\end{array}\right.$$

This approach has the advantage that $q^\prime>q$, such that there is never a drop in incentive, which can only increase.

## Comments on collateral and total reward given

Since both forms of collateral depend on the value of $q(t_0)$, the amount of collateral paid will be different. In the case of solution 1, there will be a higher initial collateral, since $q(t_0)$ is higher in that approach.

As new FIL+ deals are snapped throughout the sector lifetime, it is reasonable to incorporate an additional collateral at the time of incorporating the deal, since the reward gained after that point will not match the previous collateral that was paid. We leave a further analysis of that additional collateral for later.

A last point of difference is that the total amount of reward given through all the sector lifetime will be different with Solution 1 and solution 2

For instance, take the simple case where there is only the first deal, from time $t_0$ to $t_0+l_1$. With Solution 1, all the extra quality power will act at the beginning of the sector lifetime, where the reward per sector is generally higher, if we assume that total new rewards decrease over time, and total network QAP increases over time. The amount of reward a FIL+ deal will earn depends on when along the sector lifetime it is located. In Contrast with Solution 2, one effectively obtains the time average reward, for placing the anywhere in the sector lifetime.
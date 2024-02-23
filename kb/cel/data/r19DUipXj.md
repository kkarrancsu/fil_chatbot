---
title: Saturn earnings calculator
tags: Saturn aliens, Retrievals
description: Proposal for a simple earnings estimation calculator to be added to Saturn's website
breaks: false
---

# Saturn expected earnings - a simple calculator

#### Maria Silva and Amean Asad, October 2022

## Introduction

Saturn's main website contains a page that aims to inform interested users of how much they could earn if they committed their resources to Saturn's CDN as L1 node operators.

![](https://hackmd.io/_uploads/HyeBFkkNj.png)

However, because the final earnings will depend on a lot of factors, we need to make some assumptions and approximations to try and give a reasonable value.

The calculator receives two inputs from users, namely:
1. Upload speed in Gbps (which we will call uplink). This is provided as a slider ranging from 10 Gbps to 50 Gbps.
2. Storage capacity in Terabytes. This is provided as a slider ranging from 10TB to 50TB.

From the inputs, the calculator computes an estimation of the monthly earnings in FIL and USD. The second assumes the current price of FIL (i.e. 5 USD)


## Saturn's intrinsic value for bandwidth

Before explaining how the calculator is defined, we need to recall how the reward pool for the first launch will work. This is important because it allows us to estimate how the network values each new TB of bandwidth entering the network (what we called the network's intrinsic value for bandwidth).

In this case, we use a *growth reward pool* mechanism, which aims to distribute rewards based on the network’s growth. The idea is to have a baseline of network growth at each point in time (i.e., the total bandwidth delivered) and to increase the available pool of rewards as the network achieves the defined baseline. More details on this mechanism can be found [here](https://hackmd.io/@cryptoecon/SJIJEUJbs/%2FMqxcRhVdSi2txAKW7pCh5Q#Full-simulation-setting-the-final-parameters).

In the calculator, we are **assuming that the network is not yet meeting the baseline** and, therefore, adding more bandwidth will increase the total rewards to be distributed proportionally. Now, to get the *exact value of each new TB of bandwidth*, we only need two values:

1. **The total cumulative bandwidth set by the baseline as the goal for the network**. To get this value, we assume that, 12 months after launch, the network aims to collectively serve 300TB per day. We also aim to have a linear growth in the total bandwidth being served each day. Thus, the total cumulative bandwidth after 12 months is $\sum_{t=1}^{360} \frac{300t}{360} = 54150\text{ TB}$.
2. **Total reward pool**. Protocol Labs will put forward an initial pot of FIL to quickstart Saturn. This initial pot is meant to last 12 months, time when the network is expected to develop and start getting paying customers. The exact value is not yet confirmed. However, for the sake of the calculator, we are assuming a total pool of 800k FIL.

With this, we define the intrinsic value of one additional TB of bandwidth as $1\text{ TB} \times \frac{800000\text{ FIL}}{54150\text{ TB}} \approx 14.77 \text{ FIL} \approx 73.85 \text{ USD}$.

## Calculator V1

The simplest version of an earning calculator is to take the intrinsic value of bandwidth we derived before and multiply it by the total amount of bandwidth the operator is expected to serve in a month. In this case, we are ignoring the sorage slider and only taking int account the uplink slider.

We should note, however, that with such derivation we are making big assumptions, namely:

1. The network is below the baseline function and the new bandwidth being added will not reach the baseline.
2. The bandwidth been added is not significantly superior to the average bandwidth per operator. This assumption is needed because reward growth sublinearly with bandwidth. This means that if the an operator serves more bandiwdth than the network's average, they will not receive proportionally more rewards.
3. The performance of the L1 node operator in terms of download speed and uptime is exactly the same as the network average.

With this in mind, we only need to estimate the final bandwidth served by the node operator in a month. The final bandwidth will depend on two main factors, namely:

* The uplink multiplied by the total number of seconds in a month gives the maximum available capacity in TB;
* The traffic demand ratio. This ratio is defined so that the maximum uplink of 100 Gbps leads to a total bandwidth of 45 TB per month, which is the cap we are assuming nodes will experience in the long run.

Thus, the final formula for the FIL earning is the following:

$$I \times R \times C$$

where:

* $I = \frac{800000}{54150}$: intrinsic value of 1 TB of bandwidth
* $C = \frac{\text{uplink} \cdot 60 \cdot 60 \cdot 24 \cdot 30}{8 \cdot 1000}$: maximum available capacity in TB. Note that we are dividing it by 8 to convert Gigabits into Gibabytes and we are dividing it further by 1000 to convert GB into TB. Note that we are diving it by 1000 to convert GB into TB.
* $R = 0.00136$: traffic demand ratio derived above.


To make the formula more concrete, we implemented the calculator in python and generated the following plots:

![](https://hackmd.io/_uploads/HkxXMDVEs.png)

The python calculator can be accessed [here](https://colab.research.google.com/drive/1efJQQzPkJ9IPPVFm4CF09kZdJa0AOlRK?usp=sharing)

Finally,  next table, provides the results of the calculator:

| Uplink | Bandwidth served (TB) | FIL earnings | USD earnings |
|:------:|:---------------------:|:------------:|:------------:|
|   10.0 |                   4.4 |           65 |          325 |
|     25 |                  11.0 |          163 |          814 |
|     50 |                  22.0 |          325 |        1,627 |
|     75 |                  33.0 |          488 |        2,441 |
|    100 |                  44.1 |          651 |        3,255 |


## Calculator V2

In this second version of the calculator, weke two main chnages:

1. We incorporate the storage slider and adapt the estimated earnings to take into account the speed performance.
2. We add a base bandwidth that all nodes serve, irrespective of the uplink value inputed.


The big assumption we are making for the storage slider is that:
1. Storage has a direct relationship with the rate of requests that hit the cache, and
2. Hitting the cache is equivalent to exceeding the speed performance threshold.

Note that we assume that the relationship between storage and the cache-hit rate is logarithmic. We also assume that the max. storage in the slider (50TB) leads to an almost perfect cache-hit rate (90%). Concretely the formula is:

$$\text{cache_hit} = \frac{5 + \ln(\text{storage})}{10}$$

The following plot illustrates the relationship:

![](https://hackmd.io/_uploads/HyADaJINj.png)


Another important assumption is that the network on average achieves a cache-hit rate equivalent to providing storage of 4 TB (which is the default value for the slider). In other words, the speed performance obtained with a storage of 4 TB should result in the reward table of the V1 calculator since the node would performe as the network's average.

On the other hand, if the storage is higher or lower, the rewards need to be adjusted. Since the speed performance scoring function is quadratic, a variation in speed performance of $d$ leads to a variation in rewards of approximately $d^2$.

Finnaly, to incorporate the base badwidth that all node serve by default, we consider this baseline to be 25% of the monthyl cap of 45 TB. On top of the base bandwidth, we assume a traffic demand ratio that a node of 100 Gbps would get after applying the 45 TB cap.

Thus, the final formula is the following:

$$I \times (11.25 + R \times C) \times (\Delta S)^2$$

where:

* $I = \frac{800000}{54150}$: intrinsic value of 1 TB of bandwidth
* $C = \frac{\text{uplink} \cdot 60 \cdot 60 \cdot 24 \cdot 30}{8 \cdot 1000}$: maximum available capacity in TB. Note that we are dividing it by 8 to convert Gigabits into Gibabytes and we are dividing it further by 1000 to convert GB into TB.
* $R = 0.00104$: traffic demand ratio adjustment.
* $\Delta S = \frac{\text{cache_hit}}{\text{cache_hit_med}} = \frac{\frac{5 + \ln(\text{storage})}{10}}{\frac{5 + \ln(4)}{10}} = \frac{5 + \ln(\text{storage})}{5+\ln(4)}$

To make the formula more concrete, we implemented the calculator in python and generated the following plot:

![](https://hackmd.io/_uploads/BJVeklU4i.png)

The python calculator can be accessed [here](https://colab.research.google.com/drive/1efJQQzPkJ9IPPVFm4CF09kZdJa0AOlRK?usp=sharing)

Finally,  next table, provides the results of the calculator:

| Storage (TB) | Uplink | Bandwidth served (TB) | FIL earnings | USD earnings |
|:------------:|:------:|:---------------------:|:------------:|:------------:|
|            1 |  10.00 |                 14.62 |       132.39 |       661.97 |
|            1 |  20.00 |                 17.99 |       162.91 |       814.55 |
|            1 |  30.00 |                 21.36 |       193.42 |       967.12 |
|            1 |  40.00 |                 24.73 |       223.94 |      1119.69 |
|            1 |  50.00 |                 28.10 |       254.45 |      1272.27 |
|            4 |  10.00 |                 14.62 |       215.99 |      1079.93 |
|            4 |  20.00 |                 17.99 |       265.77 |      1328.84 |
|            4 |  30.00 |                 21.36 |       315.55 |      1577.75 |
|            4 |  40.00 |                 24.73 |       365.33 |      1826.66 |
|            4 |  50.00 |                 28.10 |       415.11 |      2075.57 |
|           20 |  10.00 |                 14.62 |       338.57 |      1692.84 |
|           20 |  20.00 |                 17.99 |       416.60 |      2083.01 |
|           20 |  30.00 |                 21.36 |       494.64 |      2473.19 |
|           20 |  40.00 |                 24.73 |       572.67 |      2863.36 |
|           20 |  50.00 |                 28.10 |       650.71 |      3253.54 |
|           35 |  10.00 |                 14.62 |       387.62 |      1938.09 |
|           35 |  20.00 |                 17.99 |       476.96 |      2384.79 |
|           35 |  30.00 |                 21.36 |       566.30 |       2831.5 |
|           35 |  40.00 |                 24.73 |       655.64 |       3278.2 |
|           35 |  50.00 |                 28.10 |       744.98 |       3724.9 |
|           50 |  10.00 |                 14.62 |       420.61 |      2103.06 |
|           50 |  20.00 |                 17.99 |       517.56 |      2587.78 |
|           50 |     30 |                 21.36 |        614.5 |      3072.51 |
|           50 |     40 |                 24.73 |       711.45 |      3557.23 |
|           50 |     50 |                  28.1 |       808.39 |      4041.96 |      


## Calculator V3

**List of improvements:**

- [ ] Take into account the fraud detection system and its false positive rate .
- [ ] Remove the linear bandiwdth assumption and apply the sublinear bandwith exponent.
- [ ] Introduce uptime performance - we will need to have the updatime as another user input and extract the network's uptime performance in real time.
- [ ] Drop assumption that network is always below  - need to extract the current network's daily bandwidth and cummulative bandwidth.
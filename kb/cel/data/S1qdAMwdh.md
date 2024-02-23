# Sensitivity analysis results

#### Juan P.M. Cianci & Maria Silva, CryptoEconLab, June 2023

## Introduction

Our `mechaQredo` package simulates the state of Qredo's economy given a set of (economic) parameters and market conditions (i.e., QRDO price, number of transactions in the network, etc). These input and output quantities are shown below. 


**Input quantities:** Tipping rate, protocol fee rate, validator reward share, staking rewards vesting decay, release rate $a$, proportion rate $b$ and max rate.  



**Output quantities:** We will be focusing on monitoring *circulating supply, yearly inflation, validator rewards, Ecosystem fund balance, staking rewards, and APY*


In this study, we aim to examine the impact of input parameters on an output quantity. To achieve this, we will analyze two primary amounts for each combination of input-output:

- **Q1**: The first quantity, referred to as the "marginal dependence," investigates how, on average, an output varies as a function of a specific input parameter while averaging the other parameters.
- **Q2**: The second quantity, known as the "sensitivity," measures the average rate of change of the output parameter in response to a specific input parameter.

These measures provide two critical pieces of information: Q1 describes what happens to the output when there are changes on a specific input (holding everything else constant), and 
Q2 describes how quickly that output is changing with respect to the specific input.

Let's consider a simplified scenario where the input parameters are just two: the "protocol funded rate" and "staking renewal rate", and the output is "circulating supply". In this setting; the previous two qantities would be interpreted as follows.

- **Q1 (Marginal Dependence):** To understand this concept, let's imagine you want to know how the circulating supply varies when you change the protocol funded rate. You would adjust this parameter while keeping the staking renewal rate constant and look at the resulting changes in circulating supply. For example, if increasing the protocol funded rate from 10% to 20% results in a decrease of the circulating supply from 1000 tokens to 900 tokens, then the marginal dependence of circulating supply on protocol funded rate is negative in this case.
- **Q2 (Sensitivity):** Now, imagine you want to measure how fast circulating supply is changing with respect to the protocol funded rate while other parameters are fixed. This is sensitivity. For example, if you incrementally increase the protocol funded rate by 1%, and each time you see a corresponding decrease of 10 tokens in the circulating supply, you could say that the sensitivity of circulating supply to the protocol funded rate is -10 tokens per percent increase in the protocol funded rate.




To formalize the discussion above, let $\vec{\mathsf{i}}=(\mathsf{i}_1,\dots,\mathsf{i}_N)$ denote the vector of input tokenomic parameters. Let $\Omega$ represent the abstract set of input parameters that inherently possess several sources of randomness, such as token price or service fees, and let $\mu_\omega$ denote the probability distribution of these random input parameters $\omega\in\Omega$. Additionally, let $\vec{\mathsf{O}}=(\mathsf{O}_1,\dots,\mathsf{O}_K)$ be the vector of output quantities, and let $f:\mathbb{R}^N\times\Omega\to\mathbb{R}^K$ denote the function that maps both tokenomic and external inputs to outputs (i.e., the `MechaQredo` model).

Given this setup, investigating the first quantity Q1 involves examining the following expression:

\begin{aligned}
\underbrace{\mathbb{E}_{\mu_\omega}[f(\vec{i},\omega)]}_\mathsf{Marginal}\quad\text{Vs.}\quad \mathsf{i}_j, \quad\quad \ j=1,\dots,N,
\end{aligned}
where $\mathbb{E}_{\mu_\omega}[\cdot]$ denotes expectation with respect to $\mu_\omega$. 
On the other hand, investigating the second quantity, Q2, entails studying the following expression:

\begin{aligned}
\underbrace{\mathbb{E}_{\mu_\omega}\left[ \frac{\partial_\ell f(\vec{i},\omega)}{\partial \mathsf{i}_j}\right]}_\mathsf{Sensitivity}\quad\text{Vs.}\quad \mathsf{i}_j, \quad \quad\ j=1,\dots,N, \ \ell=1,\dots, K.
\end{aligned}


It is important to note that the expectation is necessary due to multiple sources of randomness in our `MechaQredo` model. Notice that the sensitivity equation above is a partial derivative; it tells us how the $\ell$-th output is changing, on average, with respect to the $j$-th input parameter, assuming that the other $N-1$ input parameters are fixed. As a reminder, a positive (resp. negative) sensitivity implies that the function is increasing (resp. decreasing) with respect to the input parameter' the further the value deviates from zero in either direction, the stronger the rate of change will be. 

Considering that all the observed quantities evolve over time, we've represented the sensitivity of a particular amount with respect to time and the corresponding parameter graphically.


Our sources of randomness are determined by the *base scenario*, which, broadly speaking, implies that the realizations of random quantities such as token price, service fee volume, number of transactions, and number of validators lie within the blue shaded regions in approximately 70% of cases in the figure below:


![](https://hackmd.io/_uploads/rJw-d-lo3.png)



## Results 
We begin this section with a table summarising our main results, and then present them in more detail.

| Input | Circulating Supply | Yearly Inflation | Validator Rewards |  Staking Rewards |  Ecosystem Fund |  Staker APY |
|---|---|---|---|---|---|---|
| Tipping rate | Negative (Small) | Negative (Small) | -- | -- | Negative (Small) | Negative (Small) |
| Protocol fee rate | Negative (Small) | Negative (Small) | -- | -- | -- | -- |
| Validator reward share | -- | -- | Positive (High) | Negative (High) | -- | -- |
| Max rate | Positive (High) | Positive (High) | Positive (High) | Positive (High) | Positive (High) | Positive (High) |
| Release rate 'a' | Negative (High) | Negative (High) | Negative (High) | Negative (High) | Positive (High) | Negative (High) |
| Parameter 'b' | Positive (Small) | Positive (Small) | Positive (High) | Positive (High) | Positive (High) | Positive (Small) |
| Staking rewards vesting decay | Positive (High for small values, then negligible) | Positive (High for small values, then negligible) | Positive (High for small values, then negligible) | Positive (High for small values, then negligible) | -- | -- |


Below, we present the aforementioned results     in more detail. Our experimental results consist of four figures for each combination of input/output. On the top left figure, we plot the *marginal*, on the top right, we plot the sensitivity, on the bottom left we plot the average change on a given output quantity that a 1% change in the input quantity produces, and on the bottom right figure we plot the standard deviation of this change.



### Circulating supply

We begin by analysing the circulating supply. Our analysis reveals that  *validator's reward share* has minimal influence.



As for  the protocol fee rate, we notice that there is a slight tendency of decreasing circulating supply as this parameter increases. As we can see by the the figure on the left, the rate of this change is fairly constant and mild for different values of the protocol fee rate.


![](https://hackmd.io/_uploads/Hy3CFOZFn.png)




Regarding the sensitivity with respect to the release parameter $a$, we see that as $a$ increases, the circulating supply decreases. Furthermore, from the figure on the right, we can see that the rate of change on which circulating supply decreases with respect to $a$ is rather pronounced for smaller values of this parameter and becomes milder as $a$ increases. This is indeed an intuitive result since the release rate function decreases as a function of $a$ for the specific choice of rate function considered, i.e., 

\begin{aligned}
r(\mathsf{TVL},N^\text{val}):=r_\text{max}\left((1-b)\cdot\min\left(1,\frac{\mathsf{TVL}}{\mathsf{TVL}_\text{target}}\right)^a+b\cdot\min\left(1,\frac{N^\text{val}}{N^\text{val}_\text{target}}\right)^a\right),
\end{aligned}

with  $\mathsf{TVL}$ the total value locked and $N^\text{val}$ the number of validators, indeed, making $a$ larger will, in turn, make the terms inside the minimum operator smaller (closer to 0), which will, in turn, decrease the release rate for the ecosystem fund, and hence, the circulating supply.



![](https://hackmd.io/_uploads/Sy5Sqt1Yn.png)



Similarly, investigating the Circulating supply with respect to the proportion parameter $b$, we can see that there is a rather mild dependency in this parameter, with the circ. supply increasing with $b$ at a mostly constant (and small) rate.



![](https://hackmd.io/_uploads/ryJwct1F3.png)


Investigating the circulating supply with respect to the max rate in the aforementioned equation yields the result below. As we can see, as this parameter increases, so does the circulating supply. Furthermore, we can that the rate at which this increase occurs is more pronounced for smaller values of $r_\text{max}$.

![](https://hackmd.io/_uploads/BJ3J9d-Yh.png)


As for the staking rewards vesting decay rate, we can see that such a quantity significantly affects the circulating supply whenever it is small, in the sense that increasing such a quantity will, in turn, increase the circulating supply. These effects are, however, *short-lived* in the sense that once this value is above a certain threshold (about 0.05), its effects become negligible, as evidenced in the figure below. 
![](https://hackmd.io/_uploads/rkor_EjO2.png)
A zoomed-in version of the previous figure is shown below.
![](https://hackmd.io/_uploads/B1OZqu-K3.png)


Lastly, examining the effects of tipping rate on circulating supply, we see that they are relatively mild and only become more pronounced over time (see figure on the left). As we can see, increasing the tipping rate will, in turn, decrease the circulating supply over time. However, the rate of this change is relatively constant. 

![](https://hackmd.io/_uploads/ByKGitkKn.png)

From the figures above (magnitude of the figures on the right), we can deduce that the release rate $a$ and the max rate $r_\max$ are perhaps the most consistently impactful input parameters on circulating supply, followed by the tipping rate and $b$, as these quantities are about an order of magnitude larger than the others. It is worth mentioning, however, that a notable exception is the vesting decay rate, which has a short-lived significant impact on circulating supply. 


### Yearly inflation 


There is a rather insiginificant impact of protocol fee rate on yearly inflation. with such a parameter creating slightly decreasing effect on the yearly inflation

![](https://hackmd.io/_uploads/B1EQcuZth.png)


Similarly, as for circulating supply, increasing $a$ will cause a decreasing effect on the yearly inflation due to our choice of release rate function. In this setting, the change rate is more pronounced for smaller values of $a$ and more minor time scales. 

![](https://hackmd.io/_uploads/Hybqitkt3.png)



Just as for circ. supply. we observe a rather mild dependency on the allocation parameter $b$, with larger $b$ leading to slightly larger inflations.

![](https://hackmd.io/_uploads/rkzijYyK3.png)





Furthermore, as in circulating supply,  increasing the max rate $r_\max$ will increase the yearly inflation, however, this rate of change becomes less agressive as $r_\max$ increases.

![](https://hackmd.io/_uploads/rk1r9OZYn.png)


In the case of the staking rewards vesting rate, the effect is more pronounced for smaller values of the parameter. Indeed, we can see a spike in the inflation rate when this parameter is around 0.05. Once again, this goes in hand with the results obtained for circulating supply. 


![](https://hackmd.io/_uploads/Hk7nBGod2.png)
A zoomed-in version is shown below.
![](https://hackmd.io/_uploads/HkKD9d-Kh.png)

Lastly, observing the tipping rate, there is a rather small effect of this quantity on the yearly inflation rate. Specifically,  increasing the tipping rate, in turn, slightly decreases the yearl
y inflation rate. Furthermore, the effect of this decrease diminishes over time. 

![](https://hackmd.io/_uploads/H1rO5ObYh.png)

From the above, we see that the most prominent input parameters, in this case, are the release, parameter, max, and tipping rates, as well the vesting decay rate for smaller values of such a parameter. 

### Validator rewards

Our results show that this quantity is mostly affected by *the release rate $a$, the proportion parameter $b$, the max rate $r_\text{max}$, vesting decay rate, and validators rewards rate*. 

As we can see from the figure below, increasing the release rate has a decreasing effect on the validator's rewards. Intuitively this makes sense since a larger $a$ will cause a smaller contribution from the ecosystem fund. Similarly, as before, the effects of $a$ in this decrease are more pronounced when $a$ is small; this is also due to the specific choice of (fractional) function for the release rate. 

![](https://hackmd.io/_uploads/HJwkaY1K2.png)


As we can see for the proportionality parameter $b$, we can see that, as this parameter increases, the rewards of the validators increase as well. Furthermore,  this increase is faily linear,  as it can be seen from the sensititivty plot (i.e., constant rate of change acroos $b$ for a fixed time.)

![](https://hackmd.io/_uploads/BkbxTtyKh.png)



Examining the max rewards $r_\text{max}$, we can observe the rather intuitive result that increasing such a parameter will in turn increase the amount of validator rewards. This is normal, as this parameter, again, controls how much of the ecosystem fund is given  to validators. 

![](https://hackmd.io/_uploads/ryZccdZK2.png)


Similarly, as before, the vesting decay rate significantly impacts the validator rewards for small values of the parameter at hand' and has no impact for larger values. 
![](https://hackmd.io/_uploads/SkR6azs_n.png)

A zoomed-in version is shown below. As we can see, the effect is far more significant at smaller scales.

![](https://hackmd.io/_uploads/H1kjq_WY3.png)



Naturally, the validator rewards share plays an important contribution to the validator's reward. This is an extremely unsurprising result as this parameter controls the number of rewards given to the validators from those rewards made available for distribution. The effects of this parameter in the validator rewards slightly decrease as the parameter increases. 

![](https://hackmd.io/_uploads/BJkHptJKn.png)

From the above discussion, *the release rate parameter $a$*, the max rate $r_\max$, and the *validator reward share* have, consistently, the most impact on validator rewards. However, the staking renewal rate and the vesting decay rate do produce significant effects on the validator's share whenever these quantities are pretty large and small, respectively. 


### Staking rewards

One can observe similar effects as before when considering the total staking rewards (as they are derived from the same source), albeit with the obvious difference that the validator's rewards share negatively impacts the amount of staking rewards. 

![](https://hackmd.io/_uploads/SJqC5u-K3.png)
![](https://hackmd.io/_uploads/rJc05dWKh.png)
![](https://hackmd.io/_uploads/S1s0qdZth.png)
![](https://hackmd.io/_uploads/rkj0quZKh.png)
![](https://hackmd.io/_uploads/S1jCqOZYn.png)
![](https://hackmd.io/_uploads/BJsAqdWYh.png)
![](https://hackmd.io/_uploads/BkjA5OZF3.png)


### Ecosystem Fund

Our results show that the *ecosystem fund* is only affected by the release rate parameter $a$, the max rate $r_\text{max}$, and the tipping rate. Intuitively, this makes sense, as many of the other parameters do not directly interact with the ecosystem fund. 

Investigating the effects of the *release rate parameter $a$*, we observe that increasing such a parameter also increases the size of the ecosystem fund. Furthermore, the rate of change of this increase decreases as $a$ grows. Once again, this makes sense due to the choice of rate function. 

![](https://hackmd.io/_uploads/ryKq6KkY3.png)


We observe a tather mild effect caused by $b$:
![](https://hackmd.io/_uploads/HJejTtyth.png)


Perhaps unsurprisingly, the size of the ecosystem fund decreases with the max rate, and this rate of change becomes more pronounced as the max rate increases.

![](https://hackmd.io/_uploads/ByYIid-tn.png)


As for the tipping rate, larger values of this parameter will result, over time, in a larger ecosystem fund. The rate of change of this stays fairly constant with respect to the tipping rate but becomes more significant over time. 
![](https://hackmd.io/_uploads/SkolCF1Y2.png)





### Staker APR
Lastly, we investigate Staker's APY. Examining the release rate factor $a$, we observe that such a quantity is negatively correlated to the APY.
![](https://hackmd.io/_uploads/ryZXCKJKh.png)



In addition, the APR increases with $b$, albeit slightly.
![](https://hackmd.io/_uploads/SkWVCKkt2.png)



As for the max rate $r_\text{max}$, the APR clearly increases with such a quantity, however, the rate of change dimishes as $r_\text{max}$ increases.


![](https://hackmd.io/_uploads/BJXusdZF3.png)


Rather unsurprisingly, increasing the validator's rewards rate will, naturally, decrease the APR for stakers (since this would, in turn, mean that they receive fewer rewards)
![](https://hackmd.io/_uploads/SkS71ckF2.png)


Lastly, investigating the effects of tipping rate, we can see, that rather unsurprisingly, such a quantity increases the APR
![](https://hackmd.io/_uploads/rJaC0KJt2.png)


## Conclusions and Finalising remarks.


The mechaQredo package simulates the Qredo economy to understand how various economic parameters and market conditions influence it. Our analysis focused on certain input parameters and their effect on key output quantities such as circulating supply, yearly inflation, validator rewards, Ecosystem fund balance, staking rewards, and APY.

Two primary measures were used: Q1 (marginal dependence), showing how output changes as a particular input parameter varies, and Q2 (sensitivity), indicating the rate of change of the output concerning a specific input parameter.

Some of our key findings are

- Release rate $a$: An increase leads to a decrease in circulating supply, yearly inflation, validator rewards, and staking rewards, with the effect more pronounced for smaller $a$ values.
- Parameter $b$: An increase mildly raises circulating supply and yearly inflation, with a significant positive impact on validator rewards.
- Max rate: Increasing this rate leads to a rise in circulating supply, yearly inflation, validator rewards, and staking rewards, especially for smaller max rate values.
- Tipping rate: While the influence on circulating supply and yearly inflation is slightly negative, it positively impacts the Ecosystem Fund.
- Staking rewards vesting decay: Affects circulating supply and yearly inflation significantly for small values but diminishes for values beyond 0.05.
- Protocol fee rate: Its impact on circulating supply and yearly inflation is minor and negative.

These findings provide valuable insights into Qredo's future economic model and can help us guide our final recommendation of parameters. 

## Appendix

A folder containing the plots of all sensitivities can be found [here](https://drive.google.com/drive/folders/12EqtEA3mGukDEiHRSlZxHbgYYdtN1Orv?usp=sharing)


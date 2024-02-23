# Baseline Crossing - Impact on minting & rewards

#### Maria Silva, June 2022

###### tags: `Econ monitor`




## 1. Theoretical analysis

### 1.1 Notation

Throughout the document, we use the same notation as the [Filecoin spec website](https://spec.filecoin.io/#section-systems.filecoin_token.block_reward_minting). Most of the equations are also from that documentation.

* $M_{\infty}$ : total asymptotic number of tokens to be emitted as storage-mining block rewards
* $M_{\infty S}$: total asymptotic number of tokens to be emitted via simple minting ($M_{\infty S} = 0.3 M_{\infty}$)
* $M_{\infty B}$: total asymptotic number of tokens to be emitted via simple minting ($M_{\infty S} = 0.7 M_{\infty}$)
* $b(t)$: baseline function, which was designed as an exponential $\rightarrow b(t):= b_0 \cdot e^{gt}$
* $b_0$: initial baseline power
* $\lambda$: exponential decay rate for simple minting $\rightarrow \lambda := \frac{\ln(2)}{6yrs}$
* $g$: instantaneous baseline growth rate $\rightarrow g := \frac{ln(2)}{1yr}$
* $R(t)$: instantaneous network raw-byte power at time $t$
* $R_{\Sigma}(t)$: cummulative network raw-byte power at time $t$


### 1.2 Minting

Filecoin uses a hybrid model for mining that incorporates two minting mechanisms - simple minting and baseline minting. As such, the total number of tokens minted at time $t$ is the sum of these two minting mechanisms:

$$M(t) = M_S(t) + M_B(t)$$

Simple minting, $M_S(t)$, is the most common minting we see in other blockchains, where newly minted tokens follow a simple exponential decay model. In Filecoin, simple minting decays at a rate of $\lambda = \frac{\ln(2)}{6yrs}$, which corresponds to a 6-year half-life.

Thus, the total number of tokens emitted via baseline minting at time $t$ is independent of network power and follows the equation below:

$$M_S(t)=M_{\infty S}\cdot(1−e^{−\lambda t})$$


On the other hand, baseline minting, $M_B(t)$, depends on network power and aims to align incentives with the growth of the network’s utility. The minting function still follows an exponential decay, however, it now decays based on the *effective network time*, $\theta(t)$. The equations are as follows:


$$
\begin{equation}
\left\{ \begin{aligned} 
  M_B(t) &= M_{\infty B}\cdot(1−e^{−\lambda \theta(t)})\\
 \theta(t)  &= \frac{1}{g}\ln\left(\frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right)\\
 \overline{R}_{\Sigma}(t)  &= \int_0^t \min\{b(x), R(x)\} dx
\end{aligned} \right.
\end{equation}
$$

We can rework these equations to define the cummulative baseline minting at time $t$ from the cummulative capped RB power of the network:

$$
\begin{equation}
\begin{aligned}
  M_B(t) &= M_{\infty B} \cdot \left(1 - e^{\frac{-\lambda}{g}\ln(\frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1)}\right) = \\
   &= M_{\infty B} \cdot \left(1 - \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-\lambda}{g}}\right)
\end{aligned}
\end{equation}
$$

#### What is the impact of being below the baseline?

When the network power is above the baseline, then:

$$
\begin{equation}
\begin{aligned}
  & \min\{b(t), R(t)\} = b(t)  \\
  \implies & \int_0^{\theta(t)} b(x) dx =  \int_0^t b(x) dx\\
  \implies & \theta(t) = t
\end{aligned}
\end{equation}
$$

In other words, the network will be a full minting power with$M_B(t) = M_{\infty B}\cdot(1−e^{−\lambda t})$.

We can further define $I(t)$ as the impact on baseline minting at time $t$ of the current network power when compared with a situation the network is minting above the baseline:

$$
\begin{equation}
\begin{aligned}
  I_m(t) &= M_{\infty B}\cdot(1−e^{−\lambda t}) - M_{\infty B}(t) \cdot \left(1 - \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-\lambda}{g}}\right) = \\
  &= M_{\infty B}\cdot \left(\left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-\lambda}{g}} - e^{−\lambda t}\right) = \\
  &= M_{\infty B}\cdot \left(\left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-1}{6}} - e^{−\lambda t}\right)
\end{aligned}
\end{equation}
$$


### 1.3 Block rewards

In Filecoin, block rewards are given to miners at every tipset based on the total tokens that were expected to be minted at the time of the tipset. In other words, at a given tipset $t^*$, block rewards are assigned based on the difference between the total tokens expected to be minted at $t^*$ ($M(t^*)$) and the total expected to be minted in the previous tipset ($M(t^*_{-1})$).

However, for simplicity's sake, let's ignore the fact that minting occurs incrementally and in discrete increments and instead consider an *instantaneous* minting at time $t$. This is an approximation, but, for our analysis, the conclusions should be close enough.

In this setting, the instanteneous issuance of new Filecoin tokens is defined as the derivative of the total number of tokens minted at time $t$:

$$
\begin{equation}
\begin{aligned}
  R(t) &:= \frac{dM}{dt} \\
  &= \frac{dM_S}{dt} + \frac{dM_B}{dt}\\
  &= \lambda \cdot 0.3 \cdot M_{\infty} \cdot e^{-\lambda t} + \frac{dM_B}{dt}
\end{aligned}
\end{equation}
$$

The first part of the equation (which relates to the simple minting) is independent of whether the network is above or bellow the baseline. However, the second component does depend on the network status reguarding the baseline and, as such, will be impacted if the network goes below.

We can use the formulas derived in the previous subsection to get the instanteneous issuance of new tokens from baseline minting:

$$
\begin{equation}
\begin{aligned}
  \frac{dM_B}{dt} &= \frac{d \left[ M_{\infty B} \cdot \left(1 - \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-\lambda}{g}}\right) \right]}{dt} \\
  &= M_{\infty B} \cdot \frac{d \left[ - \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-\lambda}{g}} \right]}{dt}\\
  &= M_{\infty B} \cdot \frac{\lambda}{g} \cdot \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-\lambda}{g}-1} \cdot \frac{d \left[ \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1 \right]}{dt}\\
  &= M_{\infty B} \cdot \frac{1}{6} \cdot \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-7}{6}} \cdot \frac{g}{b_0} \cdot \frac{d\overline{R}_{\Sigma}}{dt}\\
  &= \frac{0.7 \cdot g \cdot M_{\infty}}{6 \cdot b_0} \cdot \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-7}{6}} \cdot \frac{d\overline{R}_{\Sigma}}{dt}
\end{aligned}
\end{equation}
$$

We can further simplify the term $\frac{d\overline{R}_{\Sigma}}{dt}$ using the Leibniz integral rule, since $\overline{R}_{\Sigma}(t)$ is the intergal of $\min\{b(t), R(t)\}$ and the $\min$ function is continuous:

$$ \frac{dM_B}{dt} = \frac{0.7 \cdot g \cdot M_{\infty}}{6 \cdot b_0} \cdot \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-7}{6}} \cdot  \min\{b(t), R(t)\}$$


#### What is the impact of being below the baseline?

When the network is above the baseline, the instanteneous issuance of new tokens from baseline minting would have a sinpler equation:


$$\frac{dM_B}{dt} = \frac{dM_{\infty B}\cdot(1−e^{−\lambda t})}{dt} = \lambda \cdot 0.7 \cdot M_{\infty} \cdot e^{-\lambda t}$$

So, bringing everything together, the impact on the block rewards of going bellow the baseline can be described as:


$$I_r(t) = 0.7 \cdot M_{\infty} \left( \lambda \cdot e^{-\lambda t} - \frac{g}{6 \cdot b_0} \cdot \left( \frac{g\overline{R}_{\Sigma}(t)}{b_0} + 1\right) ^{\frac{-7}{6}} \cdot  R(t)\right)$$


Note that here we are assuming $b(t) > R(t)$!




## 2. Empirical analysis

TBD


## 3. References

* [Filecoin token spec](https://spec.filecoin.io/#section-systems.filecoin_token)



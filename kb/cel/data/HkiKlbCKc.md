# Quality multipliers, lock target & FIL-on-FIL return

#### Maria Silva, June 2022

###### tags: `FIPs`

**Main conclusions:**

* Introducing a duration multiplier and/or increasing the lock target leads to an **immediate decrease in SPs’ return**. This effect is worse the larger the multiplier's slope and/or the average network duration.
* During the first few months after any change is introduced, SPs are expected to experience a **lopsided incentive to wait before sealing new sectors**. This happens because the initial pledge for the same sector will decrease rapidly during the first months because of the expected decrease in circulating supply. This is something we need to address before finishing any concrete proposal.
* If we introduce a duration multiplier, SPs still experience the **right incentives** in terms of FIL-on-FIL return **in the long run**. Sectors with FIl+ deals continue to generate better returns than CC sectors. In terms of total return, longer sectors generate higher returns than shorter sectors. However, in annualized return, shorter sectors will be preferable during the first few years, which may cause **some SPs to continue to seal shorter sectors in the beginning**.
* **Smaller slopes** in the duration multiplier funtion are **preferable**. Larger slopes introduce more time-volitility without a gain in SPs' long-term profitability.

## Notation

* $R_{\Sigma}$: total rewards received for the sector
* $R_t$: total FIL tokens minted by network on epoch $t$ (aka the total network reward for the epoch)
* $G_{\Sigma}$: total gas fees paid for the sector's proofs
* $Pl_{\Sigma}$: Initial pledge collateral for the sector
* $d$: duration of the sector in days
* $d_e$: duration of the sector in epochs
* $s$: sector's size in raw-power
* $P_t^{RB}$: total raw-byte power at epoch $t$
* $P_t^{QA}$: total quality-adjusted power at epoch $t$
* $b(t)$: baseline function, which is designed as an exponential $\rightarrow b(t):= b_0 \cdot e^{gt}$
* $m$: sector's average quality multiplier $\rightarrow sectorQAP = m \cdot s$
* $\mathcal{M}_t$: the network's average quality multiplier at epoch $t$ $\rightarrow P_t^{QA} = \mathcal{M}_t \cdot P_t^{RB}$
* $q$: lock target for the consensus pledge. It is currently set at 30%. 


## Total FIL-on-FIL return

The FIL-on-FIL return (FoFR) is based on a common metric used to assess investments - the Return on Investment (ROI). The ROI of a certain investment is defined as the investment's net gain divided by the initial investment.

In Filecoin, Storage Providers (SPs) seal sectors for a certain amount of time and get rewards from the network by maintaining the sector active and providing the corresponding proofs.

For the FoFR, we ignore the price of Filecoin in USD (i.e., we are computing all costs and rewards in FIL tokens) and we also ignore all the operational costs such as the price of the hardware and the electricity to maintain the hardware running. So, we can say the FoFR is an optimistic approximation of the real return of SPs.

Thus, ignoring operational costs, the initial investment for a sector is the initial pledge collateral the SP needs to provide for the sector and any additional deal collateral. Since the deal collateral is an agreement between the storage user and the SP and does not depend on the quality multipliers, we will ignore it for now.

As for the net gain, it is the total rewards paid to the sector minus the gas fees paid to send the sector's proofs to the network.

Therefore, the formula to the FoFR of a given sector is:

$$FoFR = \frac{R_{\Sigma} - G_{\Sigma}}{Pl_0}$$

Since we are interested in computing how the quality multiplier impact FoFR, we will not go into more detail about the gas fees $G_{\Sigma}$ since they do not depend on the sector's quality-adjusted power (QAP). We will, however, detail how the rewards $R_{\Sigma}$ and the collateral $Pl_{\Sigma}$ are impacted by the multipliers in the next two subsections.


#### Sector rewards

During the lifetime of a sector, the SP will receive a ratio of the total network rewards (once every epoch). That ratio is based on the quality-adjusted power of the sector and the network's total quality-adjusted power:

$$R_{\Sigma} = \sum_{t = 1}^{d_e} R_t \cdot \frac{sectorQAP}{P_t^{QA}} = m \cdot s \cdot \sum_{t = 1}^{d_e} \frac{R_t }{\mathcal{M}_t \cdot P_t^{RB}} $$

We can see that the total rewards are influenced by the proportion of QA power secured by the network at the time of sealing and the subsequence QA power of the network. If the network's Qa power increases (which is expected), the rewards will decrease at each new epoch.

#### Sector initial pledge

The initial pledge of a sector is the composed of a storage collateral and a consensus collateral. Both collaterals are computed when sector is selead (i.e., $t=0$):

$$Pl_0 = StoragePl_0 + ConsensusPl_0$$

The storage collateral is an approximation of the expected rewards of the sector for 20 days and depends on the network total rewards and the share of QA power for the sector:

$$
\begin{equation}
\begin{aligned}
  StoragePl_0  &= 20 \cdot R_0 \cdot \frac{sectorQAP}{P_0^{QA}}\\
  &\\
  &= 20 \cdot R_0 \cdot \frac{m \cdot s}{\mathcal{M}_0 \cdot P_0^{RB}}
\end{aligned}
\end{equation}
$$

The consensus collateral aims to capture a fraction of circulating suply. This fraction is defined by the lock target $q$, which is currently at 30%. As such, the consensus collateral depends on the ciruclating supply, the lock target and a *normalized* share QA power for the sector:

$$
\begin{equation}
\begin{aligned}
  ConsensusPl_0 &= q \cdot C_0 \cdot \frac{sectorQAP}{\max(b(0), P_0^{QA})}\\
  &\\
  &= q \cdot C_0 \cdot \frac{m \cdot s}{\mathcal{M}_0 \cdot P_0^{RB}}
\end{aligned}
\end{equation}
$$

Note that, in the previous equation, we are assuming that the network QA power is above the baseline and thus $\max(b(0), P_0^{QA}) = P_0^{QA}$.

We can further simplify these two componenets to get the following equation for the initial pledge:

$$
\begin{equation}
\begin{aligned}
  Pl_0 &= 20 \cdot R_0 \cdot \frac{m \cdot s}{\mathcal{M}_0 \cdot P_0^{RB}} + q \cdot C_0 \cdot \frac{m \cdot s}{\mathcal{M}_0 \cdot P_0^{RB}}\\
  &\\
  &= (20 \cdot R_0 + q \cdot C_0) \cdot \frac{m \cdot s}{\mathcal{M}_0 \cdot P_0^{RB}}
\end{aligned}
\end{equation}
$$


#### Final formula

Now, we can bring all components together to derive the final formula for FoFR:

$$
\begin{equation}
\begin{aligned}
  FoFR &= \frac{ m \cdot s \cdot \sum_{t = 1}^{d_e} \frac{R_t }{\mathcal{M}_t \cdot P_t^{RB}} - G_{\Sigma}}{(20 \cdot R_0 + q \cdot C_0) \cdot \frac{m \cdot s}{\mathcal{M}_0 \cdot P_0^{RB}}}\\
  &\\
  &= \frac{\mathcal{M}_0 \cdot P_0^{RB}}{m \cdot s} \cdot \frac{m \cdot s \cdot \sum_{t = 1}^{d_e} \frac{R_t }{\mathcal{M}_t \cdot P_t^{RB}} - G_{\Sigma}}{20 \cdot R_0 + q \cdot C_0}
\end{aligned}
\end{equation}
$$

Note that we get and equivalent formula by replacing $\mathcal{M}_t \cdot P_t^{RB}$ with $P_t^{QA}$. this will be usefull later for when we compute the FoFR based on the circulating supply simulations:

$$FoFR  = \frac{P_0^{QA}}{m \cdot s} \cdot \frac{m \cdot s \cdot \sum_{t = 1}^{d_e} \frac{R_t }{P_t^{QA}} - G_{\Sigma}}{20 \cdot R_0 + q \cdot C_0}$$


## Annualized FIL-on-FIL return

From the total FoFR formula, we can derive the annualized return as follows:


$$\overline{FoFR} = (FoFR+1)^{1/d}-1$$

Note that here $d$ is the sector duration measured in years and not epochs!

## Impact of lock target on total FoFR

The lock target only appears in the denominator of FoFR and has a simple relationship - if we increase the lock target, the denominator will increase and the FoFR will decrease.

To get sense by the scale of the decrease, let's return to the original formula. To simplify the derivation, let's set $K_1 := \frac{\mathcal{M}_0 \cdot P_0^{RB}}{m \cdot s}$ and $K_2 := m \cdot s \cdot \sum_{t = 1}^{d_e} \frac{R_t }{\mathcal{M}_t \cdot P_t^{RB}} - G_{\Sigma}$. with this assumption, the formula for FoFR get's simplified to:

$$FoFR = K_1 \cdot \frac{K_2}{20 \cdot R_0 + q \cdot C_0}$$


Now, the percentage difference in FoFR experienced by changing the lock target from 0.3 to $q^*$ is the following:

$$
\begin{equation}
\begin{aligned}
  \frac{FoFR^* - FoFR}{FoFR} &= \frac{K_1 \cdot \frac{K_2}{20 \cdot R_0 + q^* \cdot C_0} - K_1 \cdot \frac{K_2}{20 \cdot R_0 + 0.3 \cdot C_0}}{K_1 \cdot \frac{K_2}{20 \cdot R_0 + 0.3 \cdot C_0}}\\
  &\\
  &= \frac{\frac{1}{20 \cdot R_0 + q^* \cdot C_0} - \frac{1}{20 \cdot R_0 + 0.3 \cdot C_0}}{ \frac{1}{20 \cdot R_0 + 0.3 \cdot C_0}}\\
  &\\
  &= \frac{20 \cdot R_0 + 0.3 \cdot C_0}{20 \cdot R_0 + q^* \cdot C_0}-1
\end{aligned}
\end{equation}
$$

Now, we can use this formula to see the impact on FFoR of changing the lock target to different values. The following table contains the impact assuming that $R_0 = 0.29$ and three different values of $C_0$, namely, the currently observed value (311M), a double from the current value (622M) and a half of the current value (155M):

<center>

| **$q*$** | **$C_0 =$ 311M** | **$C_0 =$ 622M** | **$C_0 =$ 155M** |
|:--------:|:----------------:|:----------------:|:----------------:|
|    0.4   |      -26.22%     |      -25.60%     |      -27.58%     |
|    0.5   |      -41.55%     |      -40.76%     |      -43.24%     |
|    0.6   |      -51.60%     |      -50.79%     |      -53.33%     |
|    0.7   |      -58.71%     |      -57.91%     |      -60.37%     |

</center>

In conclusion, as expected, increasing the lock target will decrease the FFoR of SPs. However, the impact is not proportional. The marginal effect gets smaller as $q$ increases.

In addition, increasing the circulating supply will soften the impact on FFoR while decreasing the circulating supply will worsen the impact. But it is interesting to note that circulating supply does not have a significant effect on the % change in FFoR, with decreasing the circulating supply to half only leading to a marginal effect of close to 2%.

Note that in all the scenarios, we are not changing the daily rewards. This is because rewards have been pretty consistent. The trend is a very slow decrease with time and the impact is not significant.


## Impact of quality multiplier on FoFR

Because the interaction between the quality multiplier is somewhat complex, we used the results obtained in the circulating supply simulations to compute the FFoR of different sectors and how they vary the different duration multiplier settings.

Note that we used the data generated by a [simulation](https://github.com/protocol/CryptoEconLab-private/blob/f6da594591e0ba325070d858dc6838ef5083560e/notebooks/quality_multiplier_expansion/multiplier_simulations/6.1-scenarios-5yr_10samples.ipynb) of 5 years, with an uncertainty sampling of 10 samples. It is important to note that to estimate the total gas costs for a sector, we used the current anual average cost of pre-commit, prove-commit and spacetime proofs messages taken from [Starboard's dashboard](https://dashboard.starboard.ventures).

#### Impact of the central scenario

We started the analysis by using the simulation's central scenario. This is the scenario where the average duration of sectors in the network is 3 years and the duration multiplier is a linear function with a slope of 1x for 1-year sectors. With this scenario, we then modeled the total FoFR and the annualized FoFR for 4 different sectors:


1. 1-year sector with a 1 year Fil+ deal $\rightarrow m=10\times1=10$
2. 3-year sector with a 1 year Fil+ deal $\rightarrow m= \frac{10}{3} \times 1 \times 3 = 10$
3. 1-year CC sector $\rightarrow m=1\times1=1$
4. 3-year CC sector $\rightarrow m=1 \times 1 \times 3 = 3$

Note that we computed the FoFR assuming that all sectors have a size of 32GiB. The results are illustrated in the figure below. The x-axis represents the day where the sector was sealed, i.e., we are computing the FoFR for a sector starting in each simulation day. The reason why the 3-year sectors don't have a FoFR after the middle of 2024 is due to the simulation length. We had to guarantee the existence of simulated data for the entire lifetime of the sector.

![](https://i.imgur.com/U3QFO8G.png)


In the right plot, we see an interesting effect. All sectors experience a drop of around 50% in annualized FoFR at the start of the simulation when compared with the baseline scenario (which is the scenario with no duration multipliers and an average sector duration of 1 year).

For the 1-year sectors, the initial pledge is the same. Thus, the drop happens because the entire network is growing at a faster rate, the sector's share of QAP drops faster than the baseline, and the total rewards get smaller. For the 3-year sectors, this effect is compounded by the larger initial pledge required for the additional duration. 


After this first shock, the annualized return rapidly improves (with the exception of the 1-year CC sector), both in the actual return and when compared to the baseline scenario. This is most likely the effect of the decrease in the initial pledge required for the same sector caused by the decrease in circulating supply. This may be a **worrisome dynamic since SPs are incentivized to wait before sealing new sectors during the first months**. This is definately something we need to address.

When compared with the baseline scenario, SPs only recover the same level of returns after more or less 2 years. We can argue that this will not be as big a problem as the waiting incentives issue. The lower FoFR should be compensated by the expected increase in the price of Filecoin caused by decreasing the circulating supply.


We also observe that, as intended, sectors with FIL+ deals are more advantageous from a FoFR point-of-view. In addition, 3-year sectors have higher total returns than 1-year sectors. This is the exact behavior we were hoping for with the introduction of the duration multipliers.

However, if we look at the annualized return, 1-year sectors seem more advantageous during the first 2 years.  Nevertheless, rate at which annualized return is decreasing in time is much slower in the 3-year sectors and on the 1-year sectors, meaning at, in the long run, longer sectors will become more advantageous.

Thus, in conclusion, in the long run, if SPs behave rationally and if we disregard the additional operational costs and cash availability, SPs are incentivized to continue to lock more FIL+ deals and to do it in longer sectors.


#### Impact of different scenarios on FoFR

Now that we have a sense of how different sectors will react to the central scenario, we wonder if we get different mechanics when we change the duration multipliers, the lock targets, and the average sector duration on the network.

In the next figure, we plot the annualized FoFR as a percentage change when compared with the baseline. Note that now we are plotting the FoFR for the 1-year sector with a FIL+ deal for all the simulation scenarios. Note that the *dur=1, slope=1* scenario corresponds to the baseline setting with varying targets.

![](https://i.imgur.com/sH7BFZU.png)


The first observation is that, as expected, increasing the lock target, leads to an almost constant drop in return throughout time.

Secondly, that initial shock in SPs return we discussed previously is worsened by an increase in the multiplier slope and/or an increase in the average network duration. The reason for this is twofold. On one hand, larger slopes mean a larger initial pledge. On the other hand, larger slopes and/or average network durations mean that the share of rewards gets smaller faster because the entire network QAP is growing faster.

However, as the sealing date moves forward, the annualized FoFR recovers to a more or less stable trajectory. This long-term value seems to be impacted by the lock target and by the network's average duration. Interestingly, if we introduce a duration multiplier, the actual slope does not seem to have an impact on SPs' returns in the long run. The only impact they have is to introduce volatility, with higher slopes leading to larger initial drops in FoFR and shaper recoveries to the long-term trend. Because of this, smaller slopes seem to be preferable.


## Annex - additional plots

#### 1-year CC sector

![](https://i.imgur.com/DqhUnG6.png)


#### 3-year Fil+ sector

![](https://i.imgur.com/0cflxT4.png)


#### 3-year CC sector

![](https://i.imgur.com/DqcDaSO.png)



## References

* [Simulation notebook](https://github.com/protocol/CryptoEconLab-private/blob/f1bb557b97700e4835d115ab15ce44299a0cd0b8/notebooks/quality_multiplier_expansion/multiplier_simulations/5.1-fil_on_fill_return_annualized.ipynb)










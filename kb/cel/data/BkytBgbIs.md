---
title: Baseline Crossing - full analysis
tags: Econ monitor
---

# Baseline Crossing
## Timing and Impact of Crossing the Baseline Storage Target from Above

**Authors**: {Kiran, Vik, JP, Shyam, Dave, AX, Maria, Tom} @ CryptoEconLab & Danilo @ BlockScience

---

## Summary

-  The network's Raw Byte Power is estimated to fall below the exponential baseline target in mid February 2023 triggering a decrease in the rate of baseline minting.
-  This report investigates the impact of a baseline crossing on storage providers' ROI. Our models predict that while minting rate will decrease, storage providers ROI is expected to remain stable following the baseline crossing from above.
- The regulation of supply in response to changes in rawbyte storage growth is a unique adaptive feature of Filecoin's minting. The predicted crossing shows the mechanism is working as originally designed and ensures alignment between the network's growth targets and storage providers' block reward incentives.
 

## 1. Introduction 

#### Filecoin's Minting Model 
Filecoin uses a [hybrid minting model]((https://spec.filecoin.io/systems/filecoin_token/minting_model/)) to encourage consistent storage onboarding and investment in long-term storage. 
The hybrid minting model is a combination of simple and baseline minting that aligns block reward emissions with baseline storage targets. This enables the Filecoin network to reward storage providers proportional to the utility (i.e. storage power) they offer to the network. A visual explanation of those incentives are described in [this post](https://medium.com/block-science/a-cadcad-interactive-calculator-to-explore-minting-scenarios-in-filecoin-284009a2e941) by BlockScience on Minting Scenarios.

[comment]: <> (This combination of simple and baseline minting aligns block reward emissions with baseline storage targets. The overall result is that Filecoin rewards to storage providers more closely reflect the utility the network provides. A visual explanation of those incentives are described in [this post]https://medium.com/block-science/a-cadcad-interactive-calculator-to-explore-minting-scenarios-in-filecoin-284009a2e941 by BlockScience on Minting Scenarios.)

___

| ![](https://hackmd.io/_uploads/ByMFo5mPs.png) | ![](https://hackmd.io/_uploads/H1wtscmvs.png) |
| -------- | -------- |
| *Network Power* | *FIL on FIL profitability vs benchmark* |


*Fig 1. A counter-factual comparison on Storage Mining Rewards according to distinct scenarios (red: what if baseline was not activated, green: what if RBP is always equal to baseline). The Higher the Mining Utility, the more FIL-on-FIL profitable it is to participate on the network. Baseline Minting essentialy creates a Macro "savings account" for the future without reducing the individual rewards. [Source](https://medium.com/block-science/a-cadcad-interactive-calculator-to-explore-minting-scenarios-in-filecoin-284009a2e941)*

___


In the hybrid minting model, a portion of minting rewards come from simple exponential decay (simple minting) and the remainder from network baseline minting. The network disburses maximum rewards when network RBP exceeds the baseline storage target, a key performance indicator (KPI). The baseline storage capacity is currently targeted to double network storage capacity annually, but this growth rate can be modified through approved [Filecoin Improvement Proposals](https://github.com/filecoin-project/FIPs) (FIPs).

[comment]: <> (Each epoch, the Network Baseline Storage Target is a Key Performance Indicator <KPI> that the network must meet in terms of Raw Byte Storage Capacity in order for maximum rewards to be disbursed, and is a governance-set parameter. This KPI increases the required baseline network storage capacity by two-fold every year. The growth amount is a governance set parameter that can be modified through approved FIPs.)
![](https://hackmd.io/_uploads/Bktt-bAIj.png)
*Fig 2. Network's total raw byte capacity in relation to the network's baseline power KPI target since network launch. [Source](https://observablehq.com/@starboard/chart-network-storage-capacity-with-baseline)*


#### What is Baseline Crossing?
[comment]: <> ([From early Q2-2021]https://filecoin.io/blog/posts/filecoin-network-crosses-baseline-sustainability-target-for-first-time/, the network has been releasing the maximum possible block-reward per epoch because the network's raw-byte capacity has been exceeding the baseline storage capacity targets. This is shown in Fig. 2 above, where we observe the first Baseline Crossing in April 2021 when "Total RB Capacity" overtakes the "Baseline Power".) 

Baseline Crossing is when the network's storage capacity either exceeds or falls below the network's baseline storage target. The first baseline crossing, shown in Fig. 2, occured in [April 2021](https://filecoin.io/blog/posts/filecoin-network-crosses-baseline-sustainability-target-for-first-time/) when the network's RBP exceeded the baseline storage target. This resulted in the network releasing maximum possible block-rewards per epoch.

This report examines a potential second baseline crossing event in Q1 2023, when the network's raw byte power capacity is projected to fall below the baseline power. The implications for Storage Providers as well as the broader token economy are discussed below.

## 2. Inferred Baseline Crossing and Impact

To examine the timing and impact of baseline crossing, we first use an inference approach based on historical data. This provides an estimate of what we think is most likely to occur. However past trends may not continue into the future. To account for this we also consider a wide range of possible counterfactual scenarios in the following section.

#### Timing of Baseline Crossing

To estimate the date of baseline crossing we explored two Monte Carlo-based methods to infer the date of crossing from empirical data. Technical details of each method are given in the Appendix and code for each is linked in the References. Both produce similar estimates of the baseline crossing date. 

![](https://hackmd.io/_uploads/BJeY-ZSOj.png)

*Fig. 3. Future trajectories based on Markov Chain Monte Carlo simulations, showing A) the network's raw byte power and the baseline target function, B)  the distribution and median estimate for the date of crossing*

Figure 3 A-B show the crossing (median estimate) is predicted to be February 14, 2023, with quantiles Q5 and Q95 falling on February 8, 2023 and March 27, 2023 respectively.

#### Baseline Crossing and the Macro Token-Economy 

Baseline Crossing will affect key macroeconomic metrics in Filecoin's circulating supply, including rate of issuance and aggregate locked supply.


![](https://hackmd.io/_uploads/rJQ9ZZS_s.png)
*Fig. 4. Future trajectories based on Markov Chain Monte Carlo simulations, A) future minting trajectories, B) proportion of supply locked*

For each supply component, the future trajectory depends on future onboarding and sector extension. In the case of minting and locking, Markov Chain Monte Carlo (MCMC) projections of before and after baseline crossing are shown in Fig. 4, with the confidence bands shown corresponding to modeled uncertainty in onboarding and sector extension. 

Initially, following baseline crossing the minting rate decreases approximately 5x faster than if the network was at the maximum minting rate (no baseline crossing), but this immediately tapers to the more gradual decrease in minting rate shown in Fig. 4A. 

The expected trend in locking as a proportion of circulating supply is shown in Fig. 4B. This trend is conditional on the underlying parameters for raw byte onboarding, FIL+ rate and renewal rate continuing on their current trajectories, which is an assumption, not guaranteed.

#### Baseline Crossing and Storage Provider ROI 
Protocol adjustments to the minting schedule can change the expected FIL-denominated ROI Storage Providers (SPs) receive. If baseline crossing occurs, the new block rewards shared between all SPs will be lower. However the effect for individual SPs is more nuanced. 

It is likely that baseline crossing is also accompanied by a reduction in Initial Pledge --- see Figure 5A. In part this is because the decrease in minting rate affects circulating supply, which is a multiplicative factor in  the definition of consensus pledge, which is the largest component of Initial Pledge.


![](https://hackmd.io/_uploads/BJWjb-S_o.png)
*Fig. 5. Future trajectories based on Markov Chain Monte Carlo simulations showing, A) initial pledge per 32GiB sector, B) 1y-sector ROI before gas and other costs.*

In turn a reduction in Initial Pledge can potentially increase an individual SP's ROI. This is illustrated in Fig. 5B. The extent to which an increase may happen depends on the minting rate unit economics, which depend on future onboarding and sector extension. 

A key takeaway is that the reduction in supply and minting rate should not be equated with a reduction in ROI: Filecoin's micro and macroeconomics are designed to be resilient and adapative across a range of scenarios. 

Again it should be emphasised that the simulated Initial Pledge and ROI trajectories are sensitive to network power: if FIL+ rate, raw byte onboard, or sector extension rate change substantially the forecast trajectories will change. This is partially captured by the wide range of projection bands in Fig. 5A-B, for which the uncertainty is parameterised in terms of historical variation. However, historical variation does not fully describe future uncertainty: events beyond the scope of the model can always occur.  

In the next section a wider range of individual scenarios is explored.

## 3. Baseline Crossing and Impact Scenarios

#### Scenario Exploration

To build intuition about the outcome from different scenarios, we examined [54 scenarios](https://github.com/protocol/CryptoEconLab/blob/baseline-crossing-updated/notebooks/baseline_crossing/baseline_crossing_scenarios_v2.ipynb) which capture a range of future storage provider behavior in the Filecoin network. 

Scenarios are constructed by specifying storage provider behavior metrics across the simulation time frame. Different signatures of metrics correspond to different storage provider engagement with Filecoin. The inputs that we focus on are Raw-Byte (RB) onboarding power, sector renewal rate and Filecoin Plus growth rate. 

Fig. 6 shows the case where RB onboarding power, sector renewal rate, and FIL+ rate exponentially grow or decay to a defined percentage of their historical maximum (ranging from 10% to 90%) 180 days after simulation start. 

![](https://hackmd.io/_uploads/rJ73A-Sus.png)

*Fig 6. Counterfactual scenario where raw byte onboarding power, sector renewal rate, and FIL+ reach target values in 180 days. Future trajectories for Filecoin macro and SP econometrics depend on raw byte onboarding and renewal rates. These are treated as assumptions, chosen to span 0% (purple) to 100% (green) of the historical maximums. The power assumptions used to drive the simulation (bottom two panels), have color coding that matches the top 4 panels for Network Raw Byte Power, Initial Pledge, Minting Rate and 1y ROI (pre gas and other costs).*

Fig. 7 shows the case where sector renewal rate exponentially grows or decays to a defined percentage of their historical maximum (ranging from 10% to 90%) 180 days after simulation start. FIL+ rate and onboarding power reach a target value equal to their historical median in 180 days. 

![](https://hackmd.io/_uploads/H1-TAWrdi.png)

*Fig 7. Counterfactual scenario where renewal rate reaches the defined target value in 180 days, and raw byte onboarding power and FIL+ rate reach their historical medians in 180 days*

Finally, Fig. 8 shows the case where RB onboarding power exponentially grows or decays to a defined percentage of their historical maximum (ranging from 10% to 90%) 180 days after simulation start. FIL+ rate and renewal rate reach a target value equal to their historical median in 180 days. 

![](https://hackmd.io/_uploads/rJipR-Sds.png)

*Fig 8. Counterfactual scenario where raw byte onboarding power reaches the defined target value in 180 days, and renewal rate and FIL+ rate reach their historical medians in 180 days*

In these plots, lines shaded green represent the scenario where the network reaches a target from its current value to greater than 50% of the historical max. Purple lines represent the scenario where the network reaches a target from its current value to less than 50% of the historical max. 

We make the following observations from these counterfactual scenarios:
* In network growth scenarios where both renewal rate and raw byte onboard power target values exceeding 50% of their historical maximums, the baseline crossing date is pushed slightly into the future. 
    * A faster rate of growth (e.g. reaching target in 30 or 90 days) will push the baseline crossing date further.
* The effect on storage provider ROI can be summarized as follows: 
    * In cases where the network raw byte onboarding power and renewal rate decrease (represented by the dark purple lines), storage provider 1y-sector ROI is higher than the network growth scenario and in some cases is projected to increase sharply. 
    * In cases where the network raw byte onboarding power and renewal rate exceed their historical maximum, storage provider 1y-sector ROI stablizes to a value slightly lower than the current value. The marginal increase in individual storage provider QAP balances the effect of total decreased minting.
* Storage provider 1y-sector ROI is more sensitive to renewal rate than raw byte onboarding power. This is evidenced by both the absolute values in ROI being higher and the future ROI trending upwards in the scenario where we sweep the renewal rate and hold RB power constant (Fig. 7) versus the case where we hold renewal rate constant and sweep the raw byte power (Fig. 8).

## 4. Conclusions 
[comment]: <> (The Network Baseline function and hybrid minting model is an intended feature of the Filecoin Network that has existed since network launch, in order to align the economic incentives of the protocol with the mission statement for Filecoin to be a long-term and robust foundation for humanity's information.)
The Network Baseline function and hybrid minting model is a feature of the Filecoin Network to align the economic incentives of the protocol with the mission statement for Filecoin: To be a long-term and robust foundation for humanity's information.

The network initially crossed the baseline from below in April of 2021, unlocking the maximum minting possible via the combination of simple and baseline minting. This report examined the expected date and consequences of "crossing the baseline from above", both for a central MCMC-model scenario and range of other potential scenarios. Our models predict that while minting rate will decrease soon after baseline crossing, storage provider ROI is expected to remain stable.

The compensating effect of supply reduction is built into the Filecoin network design to protect against disproportionately disbursing rewards during downturns, deferring potential minting rewards to the future, and incentivizing continued and long-term network investment.
<!-- , in which, as a network, we fall below the Network Baseline KPI, and the natural economic corrections that occur as a result.  -->
<!-- Baseline Crossing protects against the network disproportionately disbursing rewards during downturns, deferring potential minting rewards to the future, and incentivizing continued and long-term network investment.
 -->
[comment]: <> (CryptoEconLab will continue to monitor the baseline crossing event, and will look to provide additional analyses and insights as needed as the situation develops.)

CryptoEconLab will continue to monitor the baseline crossing event and provide additional analyses and insights as needed.  

## 5. References

The models used for this Report are open-source and available on the `protocol/CryptoEconLab` and `protocol/filecoin-mecha-twin` repositories on GitHub. The specific notebooks which were used are as follows:
* [Model 1: Simple Uncertainty Quantification via Monte Carlo simulation](https://github.com/protocol/CryptoEconLab/blob/baseline-crossing-updated/notebooks/baseline_crossing/sampleUQ.ipynb) 
* [Model 2: Mechanistic model with MCMC inferred parameter distributions](https://github.com/protocol/CryptoEconLab/blob/baseline-crossing-updated/notebooks/baseline_crossing/baseline_crossing.ipynb)
* [Scenario Exploration](https://github.com/protocol/CryptoEconLab/blob/baseline-crossing-updated/notebooks/baseline_crossing/baseline_crossing_scenarios_v2.ipynb)

## 6. Appendix

### Method 1: Markov Chain Monte Carlo Simulations for Baseline Crossing 

[comment]: <> (Future predictive posterior distributions for rates of onboardng, FIL+, and sector extensions are estimated from historical data. Samples from these distributions are used to propagate uncertainty to power forecasts. These are in turn used to generate trajectories of the minting rate, initial pledge and ROI.)

With this method, which is used to generate the results and analysis in the main text, we use a mechanistic statistical model ([github](https://github.com/protocol/filecoin-mecha-twin), [PyPI](https://pypi.org/project/mechaFIL/)) to forecast economic metrics of the Filecoin economy. 

The mechanistic model relates inferences or counterfactual assumptions about future onboarding and extension rates to the total rawbyte power, circulating supply components, and derived microeconomic quantities. 

The inputs to the model are a) rawbyte onboarding power, b) FIL+ rate, and c) sector renewal rate. In the inference-based approach these modeled as a Bayesian time series using a [Seasonal with Global trend model](https://cran.r-project.org/web/packages/Rlgt/vignettes/GT_models.html) trained on historical data to create forecasts of these inputs over the simulation window. Otherwise they are specified as counterfactural forecast test functions.

In either case the forecasts are inputs to the mechanistic model's power module, which are used to produce estimates of rawbyte and quality adjusted power. These are in turn used to generate trajectories of the minting rate and initial pledge and their evolutions which are coupled through the circulating supply components as specified in Filecoin's protocol. Finally derived quantities such as ROI as estimated.

As in the first model, the baseline crossing distribution is estimated from the rawbyte power forecasts for each simulation crossing the deterministic baseline storage function. 

See the References section above for code examples and more details.

### Method 2: Simple Uncertainty Quantification via Monte Carlo simulation

This method simulates multiple paths of *Raw Byte Power (RBP)* in time. Here, we call the $i^\text{th}$ path $R_{i}(t)$ for $i=1,2,\dots,N=2000$. 

We model RBP in the following form 
\begin{aligned}
R_i(t) &= R_0e^{X_{i}(t)},\\
X_{i}(t)&= X_{i}(t-1) + \xi, \quad \xi\overset{\text{iid}}{\sim} \pi,\\
X_i(t_0) &= 0,
\end{aligned}
where $\pi$ is assumed to be a stationary distribution of the difference of logs in the RBP function, starting st some `CUTOFF` date.

In particular, we construct $\pi$ by fitting a Kernel Density Estimator (KDE) to the dataset

$$L_{i}=\left\{\log\left(\frac{R(t+1)}{R(t)}\right)\right\}_{t=t_\text{cutoff}}^{t_0},$$

with $t_\text{cutoff}$ taken to be September $1^\text{st}$, 2022 and $t_0$ taken to be the day these simuilations were run (Nov. $10^\text{th}$, 2022). It is worth mentioning that, for the values observed, the assumption of stationary seems to hold, as shown in the figure below. Indeed, it is difficult to identify a trend in the time-series of $L(t)$ (figure on the left) for the dates considered, which suggest that the distribution $\pi$ of these samples is stationary (i.e., does not change with time). The histogram and the KDE associated with the distribution $\pi$ are shown in the right. 

![](https://hackmd.io/_uploads/HkUsXaQIi.png)


Over a large number of runs of this simple Monte Carlo Simulation, we arrive at the following estimator for Baseline Crossing and relevant uncertainty: 
![](https://hackmd.io/_uploads/rJOyk-bUi.png)

This model predicts a crossing date of February 19, 2023, $\pm$ about two weeks. Our simulation also estimates the following quantities:

| Quantity (percentile)	| Time        	|
|----------	|-------------	|
| min   (earliest predicted crossing date)   	| 2023-01-12  	|
| 25%      	| 2023-02-10  	|
| 50%      	| 2023-02-18  	|
| 75%      	| 2023-02-27  	|
| max   (latest predicted crossing date)   	| 2023-04-17  	|

Thus, according to our model, with 25\% probability, crossing will occur on or before February 10th, with 50% probability, it will occur on February 18th, and so on.  



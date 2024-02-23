# Monte-Carlo Simulation results

#### Maria Silva and Juan P.M. Cianci, CryptoEconLab, July 2023


In previous reports, we have proposed a set of new tokenomic mechanisms to be introduced to Qredo, including two new [Fee Models](/v5r6y8a_TE6NtouVHmPnmA) aimed at increasing token utility, a [Staking Model](/Xh_biTXNS8mpG5M_rMfKbg) to support Qredo's introduction of a federated Proof-of-Stake consensus, and the [allocation and vesting](/3Xwe-CZ8TPiC80Fg2r5qtQ#New-allocation) of 1 billion tokens set aside originally when QRDO first launched.

All of these new mechanisms had a set of parameters that needed to be defined in such a way as to accomplish the following three high-level goals:

1. The Staking Model should be sustainable for both Stakers and Validators.
2. The supply inflation rates must be less or equal to the current levels experienced by the network.
3. Token usage should be tied more closely to the growth and usage of the Qredo network.

Our strategy to set these tokenomics parameters was to build a simplified model of the Qredo economy and run Monte-Carlo simulations across different parameter combinations and scenarios. In this report, we describe the main results of this analysis and put forward a proposal of parameters that meet the goals previously described.

We start by showing how each scenario (independently of any specific combination of parameters) impacted key economic metrics, such as circulating supply, inflation rates, Stakers and Validators profitability, and Ecosystem Fund balance.

Then, we focus on each parameter. Concretely, we describe how they impact the QRDO economy, discuss tradeoffs and make proposals for the final values of each parameter.

We finish this report with the results obtained from another Monte-Carlo simulation we ran with the final parameters and demonstrate how this design works to achieve our 3 initial goals.

For more information on the technical specification of the model and the scenarios, refer to [this report](/5EBNVwwLRBuhXy9wW4oTiw).


## Parameter sweep by scenario

In this section, we will show the results obtained in five main metrics (each in its own subsection). To make the report easier to read, we will detail the main takeaways at the top of each subsection and display the corresponding plots afterward.

Note that each plot encodes the average of each metric by day in a solid line and the standard deviation as a transparent band around the line. These standard deviation lines occur due to two main sources of variation:
- The uncertainty around each scenario (recall that we take multiple samples for each scenario to measure the uncertainty of input variables such as the number of transactions, services fees, or token prices.
- The variation caused by different combinations of tokenomic parameters.

We should note that the last plot (i.e. the combined scenario) corresponds to a subset of simulations where all scenario dimensions have the same scenario. In other words, the combined base scenario corresponds to a case where the input variables for token, usage and staking sentiment are set to the "base" scenario.

The tokenomic parameters used in the parameter sweep analysis were the following:

* Fee models:
    * Tipping rate: 0.2, 0.3, or 0.4
    * Protocol fee rate: 1 QRDO
* Staking model:
    * Minimum stake amount: 2500 QRDO
    * Minimum stake duration: 4 weeks (or 7 x 4 days)
    * Validator reward share: 0.7, 0.8, or 0.9
    * Vesting decay rate:  6, 4, or 2 years half-life
    * Release rate function:
        * $a$: 0.8 or 1
        * $b$: 0.5
        * $r_\text{max}$: 0.0006 or 0.0008
        * $N^\text{val}_\text{target}$: 50
        * $\mathsf{TVL}_\text{target}$: 70% of total unburned supply
* New token allocation:
    * Discretionary burning: 160M QRDO
    * Ecosystem fund: 390M QRDO
    * Staking Program Support fund: 150M QRDO
    * Treasury: 250M QRDO
    * Public goods fund: 50M QRDO

### Circulating supply

**Takeaways:**

- On day zero, circulating supply jumps from 339M to a value betwen 600M and 700M, depending on the scenario. This is a signifcant change! However, this shock needs to occur in order to allocate the second billion tokens.
- Notice that the uncertainty increases (i.e., the bands widen) as time evolves. This captures how changes in the long-term are more difficult to accurately predict that those in the short-term.
- Token price has a balancing effect on circulating supply. Low token prices lead to lower circulating supply, which should provide a balancing effect on price. This is mostly caused by the service fees tipping mechanism - with lower token prices, the same USD amount of service fees results in more QRDO tokens being bought and locked into the Ecosystem Fund.
- Network usage is aligned with supply dynamics. Concretely, higher usage means more transactions being executed and more service fees collected. More transactions mean more tokens being burned from protocol fees while more service fees mean more tokens being bought and locked into the Ecosystem Fund. Both these impacts lead to lower circulating supplies.
- Staking sentiment also aligns with supply dynamics. When participants stake more (and unstake less), the total tokens locked within the Staking mechanism increases, which leads to lower a circulating supply.

**Plots:**

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/By7f1xXY2.png"><img width="50%" src="https://hackmd.io/_uploads/r1czJgXF3.png">
<img width="50%" src="https://hackmd.io/_uploads/B1Im1gQFh.png"><img width="50%" src="https://hackmd.io/_uploads/Sk3QJxQK2.png">
    
**Figure 1.1:** Circulating Supply by scenario
<br/>
<br/>
</div>



### Supply inflation

Here we focus on the yearly supply inflation, which corresponds to the percent variation of circulating supply over 365 days.

**Takeaways:**

- In all scenarios, inflation rates decrease with time, which is a positive trend.
- Staking sentiment seems to have the highest impact on inflation rates, with the optimistic scenario showing significantly lower rates than the other scenarios. This shows that the decisions of Stakers to lock more or fewer tokens will have a significant impact on inflation rates and circulating supply.
- Higher network usage also leads to lower inflation rates, although the impact is less pronounced. This occurs both from the additional token burn from protocol fees and the increase in tokens locked in the Ecosystem Fund caused by higher service fees collected.
- Token price also has an impact on inflation rates. However, here the relationship is inversed. As with circulating supply, lower token prices lead to more tokens locked in the Ecosystem Fund.

**Plots:**

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/HJDxfemK2.png"><img width="50%" src="https://hackmd.io/_uploads/ByyZGgXKn.png">
<img width="50%" src="https://hackmd.io/_uploads/HkUWzxXKh.png"><img width="50%" src="https://hackmd.io/_uploads/B1pbfxmF2.png">
    
**Figure 1.2:** Yearly inflation by scenario
<br/>
<br/>
</div>

### Staker profitability

When we discuss Staker's profitability, we will focus on two main metrics:

- **APR**: this is a simple QRDO-denominated return rate over a year, taking into account the total value locked and the rewards in a given day. We should note that these APRs are not the real rates a Staker would experience over a year as every day the interest rate changes based on changes in TVL and the total rewards available. It simply encodes a "synthetic" annual rate experienced on a particular day. We should also note that this APR does not take into account protocol fees.
- **Weekly rewards**: This is the amount of rewards in QRDO a staker would receive in a week, assuming they had staked the minimum amount (i.e. 2500 QRDO). This value is computed in a daily rolling window of 7 days.

**Takeaways:**

- Token price and network usage don't have a significant impact on Staker profitability, with both metrics (APR and weekly rewards) showing similar trajectories in all scenarios. Note that the impact of price on APR is insignificant because we considering QRDO-denominated returns!
- Staking sentiment has a visible impact on Staker's profitability. In general, higher TVL (total value locked) leads to lower APR and weekly rewards, which creates an incentive early joiners. This occurs because the total available rewards do not vary proportionally to TVL. Recall that the Staking Program Support Fund provides a steady source of rewards that are independent of network performance as it follows a simple exponential decay. Thus, as more tokens are staked, even though more rewards are unlocked, the increase in rewards is smaller than the increase in TVL - which leads to lower APR and lower weekly rewards for a minimum Staker. We can see this effect in Figure 1.3.1.
- On average, Staker’s APR starts at between 20% and 30%, depending on the scenario. In the pessimistic scenario, APR grows to an average of 59%. In the other two scenarios, APR decreases to an average of 16%, for the base, and 5%, for the optimistic. Again, these variations are caused by the changes in TVL, as we discussed previously.
- In all scenarios, the minimum staking amount of 2500 QRDO results in enough weekly rewards to cover the protocol fee of  1 QRDO.

**Plots:**

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/By2FdgmYh.png"><img width="50%" src="https://hackmd.io/_uploads/B139dx7th.png">
<img width="50%" src="https://hackmd.io/_uploads/rJrsOxXK3.png"><img width="50%" src="https://hackmd.io/_uploads/BkpidlXK3.png">
    
**Figure 1.3.1:** Staker APR by scenario
<br/>
<br/>
</div>

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/r1rI5lQth.png"><img width="50%" src="https://hackmd.io/_uploads/Byc8cxQYh.png">
<img width="50%" src="https://hackmd.io/_uploads/BkOB3gXKn.png"><img width="50%" src="https://hackmd.io/_uploads/S1gLne7K3.png">
    
**Figure 1.3.2:** Weekly rewards for min. stake by scenario
<br/>
<br/>
</div>

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/r15QzyVF2.png"><img width="50%" src="https://hackmd.io/_uploads/ryEZNkVtn.png">
    
**Figure 1.3.3:** Daily rewards for Stakers and Validators for the staking sentiment scenarios
<br/>
<br/>
</div>



### Validator profitability

When we discuss Validator's profitability, we will focus on two main metrics:

- **Average rewards in QRDO**: this is the average daily rewards per Validator. Here, we simply take the amount of QRDO distributed to validators each day and divide it by the number of validators.
- **Validator profit**: this metric corresponds to the USD profit an average validator would get each day, assuming an OpEx expense of $200.


**Takeaways:**

- Average validator rewards (in QRDO) depend mostly on staking sentiment. The better the scenario, the more tokens are staked, which increases the release rate of the Ecosystem Fund.
- Independently of the scenario, validator rewards decrease with time. This occurs because the total available rewards do not grow proportionally to the number to number of validators (check Figure 1.3.1) and we are assuming a steady increase of validators during the first 2 years.
- Token price has a significant impact on validator profit, which is expected since we are converting QRDO rewards into USD. Staking sentiment impacts validator profit in the same way as the impact seen in the average validator rewards.
- Looking at the combined scenarios, at day zero, the validator's daily profit varies between \$1.7k and \$2.5k. After two years, the optimistic scenario leads to steady profits (1.9k at the end of 2 years), while the daily profits for the base and pessimistic scenarios decrease to $460 and -$56, respectively.

**Plots:**

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/Bk12S-4K3.png"><img width="50%" src="https://hackmd.io/_uploads/SkLhB-4tn.png">
<img width="50%" src="https://hackmd.io/_uploads/S1T3rbEFh.png"><img width="50%" src="https://hackmd.io/_uploads/By46S-4Y2.png">
    
**Figure 1.4.1:** Average Validator rewards by scenario
<br/>
<br/>
</div>


<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/ryblU-VFh.png"><img width="50%" src="https://hackmd.io/_uploads/rk_e8ZVKh.png">
<img width="50%" src="https://hackmd.io/_uploads/H10xUb4F3.png"><img width="50%" src="https://hackmd.io/_uploads/Hyj-I-4tn.png">
    
**Figure 1.4.2:** Validator average daily profit by scenario
<br/>
<br/>
</div>


### Ecosystem fund balance

**Takeaways:**

- Token price has a significant impact on the long-term balance of the ecosystem fund. The lower the token price, the more tokens will be locked from service fees. This balancing mechanism is super important! As the economy experiences hard conditions due to low token prices, the mechanism reduces circulating supply while, at the same time, increasing the long-term pool of tokens available for the Staking Model.
- Usage also has an impact on the fund balance, with more service fees leading to more tokens being locked. This effect is slightly offset by the tokens burned to cover protocol fees, where more transactions lead to more tokens burned.
- Staking sentiment has an inverse impact: higher TVL leads to higher release rates, which leads to lower fund balances.
- In all scenarios, the burning of protocol fees is a small component of the net flows in the Ecosystem Fund (check Figure 1.5.2). The main difference in balances between the various scenarios come from the net results of tokens being locked by the service fee tipping anf tokens being released to cover staking rewards for Stakers and Validators.


**Plots:**

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/ByeetWEY3.png"><img width="50%" src="https://hackmd.io/_uploads/SyIxYW4Fn.png">
<img width="50%" src="https://hackmd.io/_uploads/BJ2eF-VY2.png"><img width="50%" src="https://hackmd.io/_uploads/Sy-bKbNF2.png">
    
**Figure 1.5.1:** Daily balances in the Ecosystem Fund by scenario
<br/>
<br/>
</div>


<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/SJAHAEVY3.png"><img width="50%" src="https://hackmd.io/_uploads/rJl2oWEK3.png">
<img width="60%" src="https://hackmd.io/_uploads/By82sZNY2.png">
    
**Figure 1.5.2:** Daily flows of the Ecosystem Fund for the combined scenarios
<br/>
<br/>
</div>


## Parameter sweep by parameter

In this section, we focus the analysis on the tokenomic parameters exposed to the parameter sweep. For each parameter, we plot the metrics that are most impacted by the parameter. Once again, to make the report easier to read, we will detail the main takeaways at the top of each subsection and display the corresponding plots afterward.  

The plots in this section continue to show the average and standard deviations of each metric. The difference now is the source of variations. Now, we will fix a single tokenomic parameter and aggregate it across the other parameters and the various scenarios.


### Tipping rate

The tipping rate corresponds to the percentage of service fees collected in USD that is converted to QRDO and locked in the ecosystem fund. For the parameter sweep, we used 3 possible values - 0.2, 0.3, and 0.4.

:::info
:information_source: We propose setting the tipping rate to 30%. This value is low enough to support the operation of Qredo LLC, while maintaining an appropriate flow of funds locked in the Ecosystem Fund.
:::


**Takeaways:**

- The tipping rate does not impact in a significant way the profitability metrics for Stakers and Validators. The main reason is that the amount of service fees generated is small when compared with the initial balance of the Ecosystem Fund and the fact that the rewards are also complemented by the Staking Program Support fund. We should note that this does not mean that the tipping rate will not be important in the long term! This is simply the expected behavior during the first few years after the tokenomics update.
- The tipping rate impacts the long-term balance of the Ecosystem fund. The higher the tipping rate, the higher the balance. This increase comes at the cost of lower USD amounts remaining untipped. In other words, there are fewer funds to maintain the operations of Qredo LLC. 
- On average, increasing the tipping rate by 10 percentage points leads to an additional 10 million tokens locked in the Ecosystem Fund after 2 years. This additional 10 million tokens removed from circulating supply corresponds to a reduction in yearly supply inflation of 1 percentual point. This result is consistent with our [Sensitivity Analysis](/4k7Eg5vaRoun78RnIT6sLA).
- On average, increasing the tipping rate by 10 percentage points results in less 980 thousand USD untipped over the course of 2 years.
- In the combined base scenario, a tipping rate of 30% allows the network to reach an equilibrium in the flow of the Ecosystem fun after 2 years. This equilibrium will occur when the QRDO-denominated service fees locked in the Ecosystem fund cover the rewards released on a given day. Since rewards are always capped at the `max_rate`, if the QRDO-denominated service fees keep growing,  this equilibrium will eventually be reached.


**Plots:**

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/BkWDrBEt2.png"><img width="50%" src="https://hackmd.io/_uploads/BJ2PBBEF3.png">
<img width="64%" src="https://hackmd.io/_uploads/rkcCrSNt2.png">
    
**Figure 2.1:** Impact of the tipping rate for the Ecosystem fund and untipped amounts
<br/>
<br/>
</div>


### Validator reward share

The validator reward share defines the percentage of total rewards allocated to Validators. Note that by "total rewards" we mean the tokens vested from the Staking Program Support fund plus the tokens released from the Ecosystem fund. For the parameter sweep, we used 3 possible values - 0.7, 0.8, and 0.9.

:::info
:information_source: We propose setting the validator reward share to 70%. This value allows strong APRs for Stakers while maintaining high enough profits for Validators.
:::

**Takeaways:**

- The validator reward share impacts mostly the profitability of Stakers and Validators, with higher shares leading to higher profitability for validators at the cost of Stakers.
- On average, increasing the validator reward share by 10 percentual points leads to:
    - an increase in validator profit of around \$150.
    - a decrease in Staker APR of 11 percentual points.
- When TVL is at its highest and APRs are at their lowest (i.e. in the optimistic staking scenario), a validator reward share of 70% still allows for APRs higher than 10%. 
- If we consider only the base token scenario, a validator reward share of 70% results in an average validator profit of $1022 per day. This value drops to $583 if we consider the pessimistic token scenario.


**Plots:**

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/BJcAvLEY3.png"><img width="50%" src="https://hackmd.io/_uploads/Sy1BTLNF3.png">
<img width="50%" src="https://hackmd.io/_uploads/rJ7S58VF3.png">
    
**Figure 2.2:** Impact of the validator reward share for the profitability of Stakers and Validators
<br/>
<br/>
</div>



### Vesting decay rate

The Staking Program Support fund has a different vesting schedule from the other funds - instead of a linear vesting, we are implementing an exponential decay vesting (similar to the minting schedules of many traditional blockchains such as Bitcoin).

This parameter controls how fast the fund vest. It is common to think of a decay rate in terms of half-years. For instance, a decay rate of 1-year half-life means that the daily rewards vesting after a year are half of what they are now.  In this example, the decay rate would be $\frac{\ln{2}}{1 \times 365}$.

For the parameter sweep, we used 3 possible values for the half-life - 6, 4, and 2 years.

:::info
:information_source: We propose setting the vesting decay rate to a 2-years half-life: $\frac{\ln{2}}{2 \times 365}.$ This rate is not too aggressive to supply inflation rates while allowing for a good complement to staking rewards.
:::

**Takeaways:**

- The decay rate impacts two main parts of the QRDO economy. On one hand, higher half-lives mean slower vesting, which reduces supply inflation. However, on the other hand,  higher half-lives lead to fewer tokens available for the Staking Model, which reduces the profitability of Validators and Stakers. Thus, there is a trade-off here.
- Going from 6yrs half-life to 4yrs half-life leads to an increase in supply inflation of 1 percentual point (on average) while increasing APR by 3 p.p. and Validator profit by $150 (on average).
- Going from 4yrs half-life to 2yrs half-life leads to an increase in supply inflation of 2 percentual points (on average) while increasing APR by 7p.p. and Validator profit by $367 (on average).


**Plots:**

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/SyIlfwEY3.png"><img width="50%" src="https://hackmd.io/_uploads/S1HZMwEKn.png">
<img width="54%" src="https://hackmd.io/_uploads/SyGCUMSKn.png">
    
**Figure 2.3:** Impact of the vesting decay rate for the profitability of Stakers and Validators and for supply inflation rates.
<br/>
<br/>
</div>


### Release rate function parameters

The release rate function defines how many tokens are released from the Ecosystem Fund to cover staking rewards. Given a specific TVL and validator count, this function returns a rate. This rate is multiplied by the current balance in the Ecosystem fund to arrive at the total rewards available for distribution among Stakers and Validators. 

The idea is to let staking rewards growth as the network growths in terms of TVL and validators. We initially proposed the following function:


\begin{aligned}
r(\mathsf{TVL},N^\text{val}):=r_\text{max}\left(0.5\cdot\min\left(1,\frac{\mathsf{TVL}}{\mathsf{TVL}_\text{target}}\right)^a+0.5\cdot\min\left(1,\frac{N^\text{val}}{N^\text{val}_\text{target}}\right)^a\right)
\end{aligned}


The function has two main parameters - the maximum rate $r_\text{max}$ and the exponent $a$. The maximum rate sets the upper bound to the release rate. In the parameter sweep, we tested 2 values for this parameter - 0.0006 and 0.0008. The exponent $a$ controls the marginal variation of the rate as both TVL and the number of validators change. Here we tested $a=1$ (or making the function linear) and $a=0.8$ (or making the function supralinear). 

:::info
:information_source: We propose setting the following parameters for the release rate function:
- $r_\text{max} = 0.0006$: Even though this slightly reduces profitability, a smaller rate makes the Ecosystem Fund more sustainable for the long term.
- $a=0.8$: This value allows us to have slightly higher staking rewards to incentive the network early on.

:::

**Takeaways:**

- Maximum rate $r_\text{max}$ overview:
    - Controls how fast the ecosystem is drained
    - When set at 0.0006, the Ecosystem Fund will be at most halved in 3 years. If the rate is 0.0008, the fund will be halved at most in 2 years.
    - Higher rates mean more rewards are distributed to Stakers and Validators (thus increasing their profitability). However, this comes at the cost of a faster reduction in the balance of the Ecosystem Fund.
- Exponent $a$ overview:
    - Controls how much to reward early adopters - the closer to 0 the more we reward early adopters at the cost of late adopters.
    - When $a=1$, the release rate increases proportionally to the no. of validators and TVL.
    - At lower values of TVL or validator count, lower $a$ increases the release rates and, as a consequence, there will be more rewards available early on.
- Similarly to the vesting decay rate, the release rate has a trade-off. Higher release rates lead to more rewards available for the Staking Model, which increases profitability for both Satkers and Validators. However, this comes at the cost of higher inflation rates and lower balances of the Ecosystem fund.
- The maximum rate $r_\text{max}$ has an higher impact on these metrics than the Exponent $a$


**Plots:**

<div style="text-align:center">
<img width="100%" src="https://hackmd.io/_uploads/rkcUyONKn.png">
<img width="70%" src="https://hackmd.io/_uploads/SJ3OJO4Fh.png">
    
**Figure 2.4.1:** How the release rate function parameters impact the shape of the release function for different inputs of TVL and no. of validators
<br/>
<br/>
</div>

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/HkOB7zrF3.png"><img width="50%" src="https://hackmd.io/_uploads/SkLc7MBY2.png">
    
**Figure 2.4.2:** Impact of the release rate function parameters for the profitability for Stakers and Validators and for supply inflation rates.
<br/>
<br/>
</div>

<div style="text-align:center">
<img width="48%" src="https://hackmd.io/_uploads/SJ1_wzSY3.png"><img width="51%" src="https://hackmd.io/_uploads/rkYEwfHF2.png">
    
**Figure 2.4.3:** Impact of the release rate function parameters for Ecosystem balances and supply inflation rates.
<br/>
<br/>
</div>


## Simulations with final parameters

In this section, we discuss the results obtained by running the MechaQredo model with the tokenomic parameters proposed from the parameter sweep.  Here we focus on key metrics for Qredo's economy and discuss how the design and proposed parameters meet our goals of sustainability and token utility.

We ran a simulation with the same scenarios (token price, network usage, and staking sentiment), but now we forecasted the economic metrics for 3 years instead of 2 years. In addition, we used the following tokenomic parameters:

* Fee models:
    * Tipping rate: 0.3
    * Protocol fee rate: 1 QRDO
* Staking model:
    * Minimum stake amount: 2500 QRDO
    * Minimum stake duration: 4 weeks (or 7 x 4 days)
    * Validator reward share: 0.7
    * Vesting decay rate: 2-years half-life (i.e. rate $=\frac{\ln{2}}{2 \times 365}$)
    * Release rate function:
        * $a$: 0.8
        * $b$: 0.5
        * $r_\text{max}$: 0.0006
        * $N^\text{val}_\text{target}$: 50
        * $\mathsf{TVL}_\text{target}$: 70% of total unburned supply
* New token allocation:
    * Discretionary burning: 160M QRDO
    * Ecosystem fund: 390M QRDO
    * Staking Program Support fund: 150M QRDO
    * Treasury: 250M QRDO
    * Public goods fund: 50M QRDO

The plots in this section continue to show the average and standard deviations of each metric. However, the variations are the sole result of the uncertainty around each scenario.


### Supply and inflation

One of the goals of this design was to maintain supply inflation lower or equal to the current inflation experienced by the network. We wanted to increase token utility and support the new Staking Model, however, those goals could not come at the expense of higher inflation rates.

Figure 3.1.1 shows the circulating supply and inflation rates with our final design and parameters.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/BksDk5cKn.png"><img width="50%" src="https://hackmd.io/_uploads/SJqfy9qtn.png">
<img width="50%" src="https://hackmd.io/_uploads/rJrBCt5F3.png">

**Figure 3.1.1:** Supply inflation rates and circulating supply by combined scenario
<br/>
<br/>
</div>

As we can see, circulating supply starts between 590M and 690M, depending on the scenario. From here, it continues to grow for the following 2 years. Supply growth rates decelerate significantly in all scenarios at the start of 2026. This is the time when legacy vesting schedules finish.

In all scenarios, daily inflation rates are lower than 0.9%, which is below the 1.5% currently experienced by the network. 

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/BksjM9qt2.png"><img width="50%" src="https://hackmd.io/_uploads/BJb2f59Y2.png">
<img width="65%" src="https://hackmd.io/_uploads/H1xOhz55K3.png">

**Figure 3.1.2:** Components of circulating supply by combined scenario - average across runs
<br/>
<br/>
</div>

Looking at the 4 components that contribute to circulating supply (i.e. locking, burning, vesting, and releasing), we can see that vesting and locking at the largest components (check Figure 3.1.2). Vesting doesn't depend on the scenario while locking is highly influenced by the scenario. This is expected as the number of tokens locked depends on both staking sentiment and network usage. This is a reason why the optimistic scenario leads to a lower circulating supply and lower yearly inflation rates.


### Staking Model

The second goal was to have a tokenomic design capable of supporting a sustainable Staking Model. This means that we need to ensure that both Stakers and Validators are properly incentivized to participate and that the model can be sustained in the long term.

Recall that we measure profitability for Stakers and Validators in a slightly different way. For Stakers, we focus on the APR and the weekly QRDO rewards received by a participant with the minimum stake amount. For Validators, we focus on the USD daily profit assuming a fixed OpEx of \$200.

Let's start with Stakers. In all scenarios, the weekly QRDO rewards obtained by the minimum Staker are higher than the protocol fee required to distribute the reward. In other words, all Stakers will receive enough rewards to cover the protocol fees to claim them.

In the combined scenarios, the average APR starts relatively high, ranging from 35% to 58%, depending on the scenario. Then, in the base and optimistic scenarios, as the TVL growths, the APR decreases steadily. After 3 years, the average APR is at 24% in the base scenario and 5% in the optimistic scenario. On the other hand, in the pessimistic scenario, the APR grows to 174% due to the low TVL of this scenario.

<div style="text-align:center">
<img width="49%" src="https://hackmd.io/_uploads/BkCg6q9Kn.png"><img width="51%" src="https://hackmd.io/_uploads/Sykk6cqKn.png">

**Figure 3.2.1:** Staker profitability by combined scenario
<br/>
<br/>
</div>

We know that the TVL is an important factor affecting the APR of Stakers. The larger the TVL, the lower the APR, as we have more participants sharing the fixed rewards vesting from the Staking Program Support fund. This is a common design that allows the participants to reach a consensus around the optimal APR for the value they bring to the network.  However, we want to make sure that the APR does not drop too much before the network reaches the ideal TVL rate. 

To observe this, Figure 3.2.2 shows the APR for the scenario that has the highest levels of TVL - the optimistic staking scenario. Here, the network achieves TVL rates between 10% and 60%, which we plot against the corresponding Staker APR. We also color each pair of TVL and APR with the corresponding token or scenario.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/HyXVNpctn.png"><img width="50%" src="https://hackmd.io/_uploads/SyIHV65Kn.png">

**Figure 3.2.2:** Staker APR vs. TVL - optimistic scenarios of staking sentiment
<br/>
<br/>
</div>


As expected, as the TVL rate increases the APR decreases. However, when the TVL rate is higher than 30%, we see that most simulation runs lead to APRs ranging between 5% and 15%. This is in line with the rewards offered by the [top cryptocurrencies](https://www.stakingrewards.com/). 

We should note that the final APR depends on other factors besides TVL. For instance, higher network usage and lower token prices will lead to higher APR for the same TVL rate. We will come back to this feature in the next subsection.

Now, looking that daily validator profits, we see a big difference between the various scenarios. This was expected as we are using the token price to convert the average validator rewards into USD. The optimistic combined scenario results in a consistent daily average profit of around \$1900. On the other hand, the base combined scenario starts with an average profit of \$2344 per day and, after 3 years, decreases to an average of \$236 per day. Finally, the pessimistic scenario starts with a daily profit of \$2070 and finishes with a loss of \$152 per day.

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/SJrc66qKn.png"><img width="50%" src="https://hackmd.io/_uploads/SyHLaaqKn.png">

**Figure 3.2.3:** Validator daily profit for different scenarios
<br/>
<br/>
</div>

Figure 3.2.3 also shows the average Validator profits under the base token scenario. In other words, assuming the token price stays stable on average throughout the simulation. Here, the factors that most impact profits are the staking sentiment (with higher TVL leading to higher total rewards and thus higher profits for the average validator) and the number of validators in the network (with more validators leading to lower profits per validator).

In the base token scenario, the majority of runs allow the average validator to generate a profit. When staking sentiment is at its lowest, the average profit drops to \$9 per day, while the other two staking scenarios generate profits of around \$300 per day.

<div style="text-align:center">
<img width="65%" src="https://hackmd.io/_uploads/r11bpest3.png">

**Figure 3.2.4:** Ecosystem fund balance by combined scenario
<br/>
<br/>
</div>

Finally, we need to look at the balance of the Ecosystem fund. Even though we will discuss it in more detail in the next subsection, we should highlight here that in all the combined scenarios, after 3 years, the balance of the Ecosystem Fund changes its trend from a decreasing balance to an increasing balance. This shift in trend is more pronounced for the pessimistic scenario, followed by the base scenario.


### Token utility alignment

The final goal of this tokenomics redesign was to tie more closely the token supply and the network's economics with the growth and usage of the Qredo network. To achieve this, we introduced three main mechanisms:

- **Service fee model**. Under this model, a percentage of the service fees collected by Qredo LLC is tipped to the network. This means that part of service fees is converted from USD to QRDO and locked in the Ecosystem fund. This mechanism has a double effect on the network's economics. Firstly, lower token prices lead to higher exchange rates, which in turn leads to more tokens locked in the Ecosystem.  Secondly, more network usage leads to more service fees collected, which also leads to more tokens locked in the Ecosystem fund. So, more usage and lower token prices lead to more tokens being locked. And why is this a good design? Well, more tokens locked in the Ecosystem Fund have two main effects, namely reducing circulating supply and increasing the tokens available to pay Validators and Stakers.
- **Protocol fee model**. All transactions executed in the Qredo network incur a fixed protocol fee. This protocol fee is burned, which reduces the circulating supply. Thus, as network usage grows, more tokens are burned and more supply is taken from the Qredo Economy. However, we should note that this mechanism has a fairly small impact when compared with the other two.
- **Release function for the Ecosystem fund**. The release rate that controls how much of the current balance in the Ecosystem Fund is released to pay Validators and Stakers depends on both TVL and the number of validators. This allows the network to release a higher percentage of tokens from the Ecosystem fund with the growth of these two metrics. 


Going back to the circulating supply plots in Figure 3.1.1, we observe how these mechanisms work to soften the scenarios, creating a balancing effect on the economics of the network. In the pessimistic combined scenario, the daily inflation rates are slightly lower, and the circulating supply grows slower than in the other scenarios. After the legacy vesting schedules finish, the circulating supply inverts, and its drops are sharper than the drops observed in the other two scenarios.

We can observe this effect in the inflows and outflows of the Ecosystem fund in Figure 3.3.1, with the pessimistic scenario leading at the same time with more tokens locked and fewer tokens released. This is caused by the combined effect of the Service Fee Model and the release function design.


<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/rkVPXWit2.png"><img width="50%" src="https://hackmd.io/_uploads/SyALXZit2.png">

**Figure 3.3.1:** Inflows and outflows of the Ecosystem fund by combined scenario
<br/>
<br/>
</div>


As we discussed in Figure 3.2.2, the Stakers APR is also impacted by token price and network usage. Concretly, higher network usage and lower token prices will lead to higher APRs for the same TVL rate, which is exactly as intended! By converting part of the services fees collected to QRDO and locking them in the Ecosystem fund, we create this balancing effect where:

- More usage leads to more service fees, which leads to more tokens locked in the Ecosystem Fund.
- Lower token prices lead to higher conversion rates, which also leads to more tokens locked in the Ecosystem fund.

In turn, more tokens locked in the Ecosystem fund have a double effect on the TVL rate and APR:

- On APR, we have more rewards available to distribute.
- On the TVL rate, we have a lower circulating supply, which increases the TVL rate. Recall that TVL rate = TVL divided by circulating supply.

This effect can be in part observed in part in the Validator rewards. As we can see in Figure 3.3.2, lower token values and more usage lead to more tokens locked in the Ecosystem fund, which increases the rewards distributed to Validators in the long run. 

<div style="text-align:center">
<img width="50%" src="https://hackmd.io/_uploads/Skb3IZjF3.png"><img width="50%" src="https://hackmd.io/_uploads/BJdnLbjK3.png">

**Figure 3.3.2:** Average rewards per Validator - token and usage scenarios
<br/>
<br/>
</div>

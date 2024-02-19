# FVM as a risk to the Filecoin gas economy

## TL;DR
* Filecoin SP's currently consume the majority of gas in network-essential tasks, like proving their sectors.
* Unregulated FVM demand for gas can pose a problem for network operations, where SP's can be priced out of the gas economy.
* The risk is not immediate, as Filecoin gas is currently underutilized, the network can accommodate approximately 40% increase in current gas usage before base fee starts steadily increasing. Once base fee has risen to around X, this can severely affect maintenance of sectors, pricing out SP's from submitting sector proofs.
* While not immediate, the risk is not impossibly small, and will be significant in the middle term future. 
* Total network revenue (through gas fee burn) could be maximized in many cases by reducing the target block size. Since FVM also has potential to absorb demand for gas (through scaling solutions), "gas sprawl" scenarios are also possible, where the target block size is too large, for the level of demand. 
* **The most direct solution CryptoEconLab is working on is to  directly controlling the amount of gas available for SP usage and for general FVM usage, by separating into different gas lanes with their own target block size.** 

## Quantifying risks of gas gentrification and sprawl

We present here a simple summary of the [study conducted by CryptoEconLab on the quantification of FVM gas risk](https://hackmd.io/LQ8Um2zURFeoGtjoGpiVyA?both).

Filecoin uses a fee market that adjusts the “base fee” based on demand for block space. With the upcoming deployment of the Filecoin Virtual Machine (FVM), there could be increased demand for gas, which could be absorbed by scalability solutions. While the amount of base fee that SP's are willing to pay for gas is constrained by the profitability of onboarding and maintaining sectors on Filecoin, what FVM users will be willing to pay for gas depends on the particular application and the subjective value of these transactions. If enough FVM users want to conduct high value transactions the market dictated base fee can become higher than what SP's can afford, impacting basic Filecoin operations.

In this article, we’ll explore the demand for gas in the Filecoin Virtual Machine (FVM) and how it affects the composition of a block. We’ll also look at the preferences of different stakeholders in the network, like token holders and miners, and how they impact the base fee and network performance. This information is important for designing and operating a decentralized storage network like Filecoin.

## Modeling Filecoin gas demand

**Remark.** *This is a heavily condensed version of the mathematical model presented in [in the extended version of this document](https://hackmd.io/LQ8Um2zURFeoGtjoGpiVyA?both). For the sake of simplicity, we will focus on describing the model in a broad sense, and refer the interested reader to the full version above.*

We model demand as being driven by two main groups: SP's  and FVM users (other non storage-providing users). Naturally, both FVM users and SP's need to pay for sending messages on the network. In our model, each individual user assigns a personal valuation to their messages, and submits these messages to the Mempool with high probability whenever their valuation is high. Conversely, under our formulation, users submit less messages whenever ther valuation is low. This valuation is given in terms of 
\begin{aligned}
\mathsf{valuation}=\mathsf{expected\ tokens\ gain}-\mathsf{gas \ expenses}-\mathsf{operational \  expenses}.
\end{aligned}
Here, $\mathsf{gas \ expenses}$ are a function of the base fee (they increase as the base fee increases) and $\mathsf{operational \  expenses}$ such as, electricity, floor space that SP's need to pay, etc. This is a very subjective measure, and will vary greatly from miner to miner. 

In order take this subjectivity into account, our models use [advanced statistical techniques](https://en.wikipedia.org/wiki/Uncertainty_quantification) to model demand for both SPs and FVM users. By using these techniques, we can take into account how different SPs and FVM users react to changes in price. An example demand curve (as a function of price) obtained using this methodology is shown below. The gray lines correspond to one of many, many possible versions of the demand functions. As we can see, our demand profiles decay very slowly for low values of base fee, but then decrease rapidly as this base fee approaches a threshold value; which corresponds to a base fee that can be roughly understood as *being universally too large*.



![](https://hackmd.io/_uploads/rkZuq2IAj.png)

## When could FVM pose a problem?

One important aspect of this study was to try to understand the composition of messages in a block; i.e., for a given level of demand for gas, what fraction of the total block will be used by FVM vs SP sector onboarding and maintenance? In the lack of real FVM gas usage data, we use a set of  [ assumptions](https://hackmd.io/LQ8Um2zURFeoGtjoGpiVyA?both), and investigate over a wide range of possible future FVM gas demand scenarios, as well as assumptions on SP block preparation preference, that we believe are suitable for a first order understanding of the problem. We  also plan to continue building more sophisticated Agent-Based models that will let us explore wider ranges of SP strategies, as they adjust to the new levels of FVM demand.


We divided messages into two general categories: FVM and Sector maintenance-type messages, each with unique gas fee valuation profiles.  At the moment, about 70% of a block's gas usage is due to SP-maintenance messages, which averages out to about 3.5 billion gas units per block.  As we increase FVM demand for gas, base fee is driven upwards, and we estimate the proportion of gas used in the block as a function of base fee and on the amount of gas brought in by FVM as a fucntion of current gas usage.

We simulated a range of FVM gas demand scenarios, where FVM brings in demand that is: one tenth, one half, about the same and twice as much as the current demand for SP maintenance (*this is labeled as the parameter $\alpha$ in the plots below*). 

Assuming that miners do not discriminate amongst messages, and simply accept those messages that are able to cover the base fee and offer the higher tips, we would see a block composition as shown in the figures below. Here, the faint-colored lines represent a several possible block compositions, while the solid, colored one represent the average composition. Under our assumptions, we can see that in this case the proportion of block usage depends heavily on the initial FVM demand, and that this proportion decreases as as the base fee increases. This is because as base fee increases, the valuation of each message decreases, which causes users to submit less and less messages. 

![](https://hackmd.io/_uploads/r1GPZozyh.png)



We also investigated the case where SPs give preference to their own messages by only including FVM-related messages if there is sufficient space. In this scenario we get a curve that looks like the one below. Once again, we observe the proportion of block usage decreases as as the base fee increases, however, the maximum amount of FVM demand gets capped at around 1.5 Billion gas units, per block. This strategy, however requires SPs to work collaborately, and in unison reject messages that would give them much larger tips. It is then unclear how viable it is for SP's to self-regulate the gas market.

![](https://hackmd.io/_uploads/rkv5piGk2.png)

~~## Understanding utility for different stakeholders.~~

~~We also proposed several utility functions as a way of quantifying the benefit that various stakeholders in the network would have with respect to changes in the base fee and demand.~~

~~Our definitions of utility function showed that **stakeholders who are mostly concerned with high gas usage, those who benefit from onboarding data, and SPs are negatively affected by a significant increase in gas usage**. Conversely, our utility functions show that stakeholders such as **token holders, who benefit from burning more tokens, are positively impacted by an increase in the base fee.** While these results are intuitive, we believe it is worth quantifying and isolating these effects for the stakeholders mentioned above.~~

## Total network revenue, and suboptimal target block size

*Is EIP 1559 optimal?* The EIP 1559 base fee mechanism adjusts the base fee with the goal of keeping all blocks close to the fixed target block size. This increases pressure to send *suboptimally* priced blocks, even if there is not sufficient demand to fill the entire block. If demand for gas usage is lower than dictated by this target block size, base fee will drop, in a way that can harm total network revenue. This is particularly a risk given tht FVM opens the door to numerous L2 scaling solutions, which could end up absorbing too much demand for gas usage.

**If we had the goal of maximizing total network revenue**, from our previous results, it is possible to infer what should be the optimal  block size to fill, for a given level of demand. 

We re-interpret our previous results by assuming that the reason the fraction "prop Empty" is empty is because the  block size has been reduced to $(1-{\rm prop\,Empty})*B_T$, where $B_T$ is the current target block size. We then find the optimal  block size, such that the corresponding total network revenue (base fee* target block size) is maximized. We find that in many cases, network revenue could be maximized by reducing the size of the block.
## What can be done?

The most direct tool that will be explored to protect against FVM gas demand risks, is to have separate lanes for SP and for FVM gas usage. 


Individual gas lanes can help protect 
Currently the base fee is dictated by demand for gas and the chosen target block size, through the EIP 1559 mechanism. Limiting the overall target block size could enable several desirable outcomes, such as: optimizing network revenue to be made from FVM messages, upgrading the batch balancer mechanism in favor charging explcit onboarding fees to SP's, regulate supply of gas in a way that accurately matches demand for gas.

As well as the total target block size, second important lever is the introduction of "gas lanes", where in our case, a fraction of the total block gas can be reserved exclusively for network-essential SP messages, excempting them from FVM driven base fee hikes. 


## Next steps from CryptoEconLab
* In the next week we will publish a FIP discussion introducing separate gas lanes for SP messages and general FVM messages, as a tool to hedge FVM-related gas risks
* We will continue building more sophisticaded agent based simulations, which will enable us to simulate the efficacy of the proposed solutions, as well as the efficacy of letting SP's self regulate without any protocol changes.
* We will start collecting and reviewing real FVM data after launch on 14/03/2023, and use this to improve our models through better informed priors.
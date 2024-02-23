---
title: Is Filecoin Plus essential for Filecoin
tags: Econ monitor
---

**Authors**: {Tom, Vik, Shyam, Kiran} @ CryptoEconLab

## Summary
* Filecoin's value proposition derives from its mission to create a decentralized, efficient, and robust foundation for humanity's information.
* Filecoin Plus is one of two incentive mechanisms that have been part of the network since lift-off to achieve this.
* Filecoin Plus is not about locking, Proof of Stake, or reducing the absolute power of committed capacity. It was designed and operates as a pragmatic solution to the network's inability to otherwise prove useful storage in a verifiable, trustless, and incentive compatible way.
* A version of **Filecoin Plus is needed** because without it, **storing data in deals is not the rational choice over committing capacity**. In essense, the program ensures self-interest aligns with storing data.
* **Misuse of the datacap program is a critical problem.** It undercuts data storage businesses by becoming the primary rational strategy, so it is **essential to improve Filecoin Plus for the network to achieve its mission.** Potential approaches include:
    * Use an escalating challenger-iteration framework for datacap dispute resolution, similar to optimistic rollups or Truebit. This type of approach would remain aligned with a network that supports a decentralized, efficient, and robust foundation for humanity's information. 
    * Increase the friction associated with misuse by making the distribution of datacap conditional upon retrieval tests.
* Alternatives such as **removing Filecoin Plus are not likely to achieve the mission, since CC would then become the dominant strategy, not Regular Deals for storing data.**
* Another possible point for improvement is having a mechanism that can better achieve the networks data storage goals than a single, fixed multiplier. If the network agrees to target a certain fraction of Deal power to CC power, a mechanism can be designed and implemented to more adeptly achieve this.
* Our call to the community is to improve, criticize, and think of better solutions than these. This will help bring the Filecoin Plus program up to date and ensure that data storage is the rational choice.

## Preface
The purpose of this note is to give a perspective on the Past, Present and Future of Filecoin Plus. The perspective is our own - that is, of an ecosystem participant, engaged, motivated, closely familiar with the economic mechanisms of Filecoin, and a vested interest in the long term success of the network. 

As with any perspective, it is one view. Others’ views will differ. Ecosystems are by definition complex and diverse and Filecoin’s is not an exception, so we don’t expect the nuanced questions that arise, relying on deep knowledge, specialized experience or the like, to have singular answers. Still, our capacity to make meaningful steps forward consistently, depends on us jointly on having high-value information and this being widely available and understood, which motivates us to present our perspective as one input. 

Where possible, we prefer to show data rather than present an opinion. Data points exist in the form of artifacts of historical record of development, numerical figures about the current state of the network, and concrete explanations of how Filecoin’s economic constructions mechanistically interact. Based on this, a chain of logic follows that often leads to clear conclusions. At other times, data is more sparse, and evidence to draw strong conclusions is insufficient and the range of plausible possibilities wider. As clearly as we can, we’ll delineate data, from inference, from opinion, so the reader is clear what we think we know and why we think we know it.

As always, do your own research, this is not financial advice in any way, shape or form. 

## Filecoin Incentives in a Nutshell
Filecoin’s mission, shaped between 2017-2020 and set out in fips.filecoin.io/mission/ prior to the network launch, is: *to create a decentralised, efficient, and robust foundation for humanity's information.*

Since this, Filecoin’s cryptoeconomics have supported an explosion of data storage, from the Web3 and enterprise datasets, to storing vast amounts of high-value research data, with respected scientific projects such as SETI and CERN using the network to [safeguard their data](https://filecoin-explorer.com).

The incentive mechanism powering growth in storage is minting and receiving Filecoin tokens in exchange for committing capacity or storing data to the Filecoin network. The tokens have exchange value outside of the network, based on the limited supply, and their demand as needed to support network services as network utility grows. Because the tokens have value, their distribution provides an incentive to grow capacity and onboard data storage, thereby bootstrapping the network’s mission.

## Incentives to store data and Filecoin Plus
The cryptoeconomic incentives Filecoin uses to ensure the network is storing humanities information are twofold:
1. Block rewards are minted at 30 second intervals and distributed based on the proportion of quality-adjusted storage power that a storage provider gives to the network. 
2. Filecoin Plus provides a relative advantage to deals, producing an incentive force-field that favors the storage of data storage over Committed Capacity. 

The Filecoin Plus preference is designed to work by diluting costs, by making hardware costs per unit FIL earned, lower than otherwise via a ‘10x power multiplier’. 

This design intends to make it rational to onboard Verified Deals instead of Committed Capacity, when client demand is readily available. 

The incentive has been effective, at the level of growing Verified Deals. The proportion of Verified Deal onboarding has grown from less than 1% of rawbyte power one year ago to around 90% today (20th August 2023):

![](https://hackmd.io/_uploads/BJ24JhdAh.png)
*Figure 1: 1) Growth in the data storage through Filecoin Plus, as a proportion of raw-byte power onboarding. 2) The expected terminal value of the Filecoin Plus proportion based on current trends is 92% median with [84, 97]% Q10 and Q90 quantiles.*

## Dispelling common myths: what Filecoin Plus is not
In questioning the role of Filecoin Plus, it is useful to provide perspective on what it is not.

### Misconception 1: Filecoin Plus is about locking tokens
Locked tokens *are* valuable to the Filecoin network, both to consensus security and for guaranteeing storage reliability, but locking tokens is not the intention or actual result of Filecoin Plus, at a macro level.

To see why, examine the formula for the consensus pledge (which makes up for atleast 95% of Initial Pledge):

$$ ConsensusPledge = 30\% \times CirculatingSupply \times\frac{QAP_{added}}{NetworkQAP} $$ 

Since the multipliers scale both QAPadded and TotalNetworkQAP, **at equilibrium there is no effect on the amount of consensus pledge locked with or without Filecoin Plus.**

In this context, we define equilibrium as the state when the percentage of onboarded deal sectors matches the total amount of deal sectors on the network. In non-equilibrium states, it is possible for locking to increase or decrease if the FIL+ rate quickly changes, but over time this effect evens out to no net change.

### Misconception 2: Filecoin Plus is about making Filecoin Proof of Stake
A common misinterpretation is that Filecoin Plus is designed to make the network a Proof of Stake network.

At network level, Filecoin has always targeted locking 30% of circulating supply to secure consensus in the network. This target is *unchanged* if Filecoin Plus multiplier exists or not. So the Filecoin Plus incentive is neither designed nor directly affects collateral supporting the Proof of Stake elements of Filecoin’s consensus security. 

### Misconception 3: Fil+ decreases network capacity
As the network evolves several outcomes are possible for QAP and RBP:
* Growth in QAP, Growth in RBP
* Growth in QAP, Constant RBP
* Growth in QAP, Decline in RBP
* Constant QAP Decline in RBP
* Decline in QAP, Decline in RBP

Filecoin Plus does not guarantee any of these. As an incentive it operates on the ratio of committed capacity to deal power. Whether QAP and RBP grow depends on new and current business providers growing their businesses and demand flowing to the network. 

## When Filecoin Plus works and when it doesn't
To question when Filecoin Plus works, and to understand its limitations, and how its failure modes might be overcome, the following discussion is anchored with a set of example SP business profiles. 

### Business Profiles
We examine costs and revenues for six different SP strategies for participating in Filecoin:
1. **CC** - This models a CC SP. When compared to FIL+ SPs, CC SPs have lower bandwidth costs (due to not needing retrieval of data), lower costs associated with borrowing pledge per TiB of capacity onboarded, no business development and data preparation costs. However, CC miners also receive a smaller share of block rewards.
2. **FIL+** - This models an SP trying to grow a data storage business, utilizing the FIL+ program. When compared to CC SPs, FIL+ SPs have higher bandwidth costs (due to retrievals), higher storage costs (due to needing to store redundant copies of the data), a non-zero business development cost, and higher pledge collateral costs. However, FIL+ SPs receive more block rewards than CC SPs, and can potentially also receive deal income from storing clients data.
3. **Regular Deal (RD)** - This models an SP trying to grow a data storage business without using the FIL+ program. When compared to FIL+ SPs, RD SPs have lower pledge borrowing costs, and potentially lower business development and bandwidth costs. However, they also receive a smaller share of the block rewards.
4. **V1-ExploitFIL+** - This models an SP actively exploiting the FIL+ program and not growing a storage business. Compared to the FIL+ SP, the V1-ExploitFIL+ SP does not incur business development costs, does not store an extra copy of the data, has reduced bandwidth costs, and are not subject to any penalties for exploiting FIL+.
5. **V2-ExploitFIL+** - This is similar to the V1-ExploitFIL+, except that this SP tries to project an image of being faithful to the FIL+ program. As such, this SP incurs the cost of storing an extra copy of data and has increased bandwidth costs in order to pass any sort of retrieval test that may be conducted.
6. **V3-ExploitFIL+** - This is similar to V2-ExploitFIL+, but in this case, we add a hypothetical slashing fee for abusing the FIL+ program.

These profiles are used to identify optimal strategies, dependence on cost and income profiles, and the level of multiplier needed for data storage to be preferred.

![](https://hackmd.io/_uploads/B1sIQn_C3.png)
*Table 1: Example profiles for different types of operations. An interactive website to create customized cost profiles and vary model assumptions is given [here](https://filspcostexplorer.streamlit.app/).* 

![](https://hackmd.io/_uploads/HyOULhdA3.png)
![](https://hackmd.io/_uploads/HJjU8n_03.png)
Figure 2: A) Ordering of operation strategies by most rational strategy according to Net Income. B) Breakdown of cost and revenue. All values in USD/TiB/year. The profiles correspond to Table 1. 

### Rational Strategy
Rational incentives for each type of storage operation, set out in Table 1 and shown in Figure 2, imply the following:
* A storage provider with Regular Deals is not competitive with CC. This illustrates the necessity of the multiplier for data storage. 
* A storage provider with Filecoin Plus deals is more competitive than CC or RD, but exploiting Filecoin Plus is the best strategy, if there is minimal cost associated with cheating (V1-exploit profile). 
* If exploiting Filecoin Plus is made more costly, through retrieval tests, or through levying a penalty conditional on the outcome of Filecoin Plus disputes, then FIL+ storage providing will become the rational choice. 

These conclusions depend on the cost and income assumptions made in Table 1, as well as network state and token exchange rate. We invite the reader to explore how profits and losses change, depending on these assumptions, using [this interactive calculator](https://filspcostexplorer.streamlit.app/).

A difficulty discussing Filecoin Plus’s microeconomics is the scope for edge cases, due to the complexity of the cost and income profiles, as well as network and other factors. This leads to a lot of back and forth discussion on possible exceptions — what if client fee income were larger, what if staff costs were lower, and so forth.

To ameliorate this we can summarize possibilities by sampling from plausible prior distributions for each cost and income variable. These distributional assumptions are shown in Figure 3, and lead to the ranking of strategies shown in Figure 4. 

The takeaways are: 
* For 80% of simulated cost and income scenarios, adopting V1-Exploit FIL+ is the best strategy. For the other 20%, FIL+ storage providing is the best. 
* These conclusions are broadly robust across a range of assumptions of token exchange rate, cost and income distributions, and multipliers, all of which can be varied using the interactive calculator.


![](https://hackmd.io/_uploads/rJU-rndRn.png)
*Figure 3. Distributional assumptions for cost and income variables. *

![](https://hackmd.io/_uploads/ryFxI2u03.png)
*Figure 4. Percentage outcomes for each strategy — CC, FIL+, Regular Deal, V1-ExploitFIL+, V2-ExploitFIL+ or V2-ExploitFIL+ — in terms of nth-position ranking.*

## A minimum bar for data storage
Since a typical storage provider with Regular Deals isn’t competitive with CC, the network’s data storage mission needs an additional incentive to store data.

One source of incentive is Deal Income. But usually this isn’t enough to cover the extra costs being a storage provider incurs, such as BizDev, data prep, duplication, serving data and more, as well as to make up for the potential sporadic returns of starting a storage provider business dependent on Deal Income.  

Within the current framework, this leaves the Quality Multiplier to make up the difference and lower the bar to make storing data rational.

![](https://hackmd.io/_uploads/r1J6S2dC2.png)
*Figure 5. Minimum Quality Multiplier needed to make data onboarding more profitable than committing capacity across token exchange rates. In this plot, Fil+ sectors are 4x more expensive than CC sectors, CC sectors are fixed to cost $30/TiB/Yr, and deal income is set at $16/TiB/Yr. These values can be modified in the interactive app to explore other scenarios and how they affect the minimum multiplier.*

Figure 5 shows the minimum Quality Multiplier to make data storage the preferred strategy, compared to committing capacity. The takeaways are threefold:
* If the token price is high, a lower multiplier than 10x is sufficient. 
* High costs mean a higher multiplier is needed, and as does lower revenue, all else equal. 
* The minimum value sufficient to incentivize data storage, under the typical scenarios considered, ranges from 3x to 30x. Due to heterogeneity in costs, the ability of SPs to generate deal income, and token price variance, there is no single minimum multiplier. 

These data points suggest having a multiplier of at least 10x, and likely higher, closer to 30x, is needed to ensure data storage with a single multiplier across the whole range of plausible network operating conditions. Conversely, from historical data we know 10x is already a sufficiently high-powered incentive — this is evident from the growth and saturation of the FIL+ daily onboarding rate to ~90%, shown in Figure 1.

Irrespective, the variability of the multiplier across different network conditions and SP businesses is clear. To achieve the network’s goals more adeptly requires a better mechanism. An alternative approach could be to set the goal the network has for the ratio of capacity vs deals front and center. For example, target a 25% CC to 75% deal ratio. From this it is easy to work backwards using a simple control mechanism to set a dynamic multiplier to ensure the network hits such an agreed upon target. 

The call to action for the community is to build on this, and think of different and better ways to incentivize data storage that are less blunt than a fixed 10x multiplier.

## Would data storage have grown without Filecoin Plus
Although history’s thread is singular, we can establish some points of reference and test our intuition on what would have happened had the Filecoin Plus program not existed by considering counterfactual scenarios from different perspectives.

A first data point is the amount of data stored in Regular Deals outside of the Filecoin Plus program. At most, 0.3% of the network’s raw-byte power had been standard non-Filecoin Plus Regular Deals. This happened in the early days of the network, when CC made up the majority of network QAP and before any substantial Verified Deal growth. 

![](https://hackmd.io/_uploads/S1RLw3_A3.png)

*Figure 6. A) Percentage of raw-byte power attributable to Regular (non-Filecoin Plus) deals since the inception of network (orange line). B) High-growth rate counterfactual for regular deals.*

The growth in Verified Deals has dominated the deal landscape since 2022, so a natural question to ask is what level of Regular Deals would have been observed had they continued at their 1st-year level of growth before the predominance of Filecoin Plus was established. The counterfactual in this instance is shown in Figure 3. This shows Regular Deals would be around 1.5% of total current raw-byte power had their growth continued. This suggests even had the high initial growth rate of Regular Deals been maintained, it would be much less than the current Verified Deal level of data storage at around 12%. 

Here though the model is only a simple one. Using a more sophisticated approach we can mimic how SPs would have behaved if Fil+ was never implemented. To simulate this, we use historical data to learn the behavior of SPs in the current network where Fil+ exists. Specifically, we learn a mapping from the network's Fil-on-Fil Returns (FoFR) to the total amount of power onboarded onto the network. We then rewind the network to 2022-01-01, approximately when deal sectors started to be onboarded onto the network and simulate the scenario where Fil+ was not implemented.

Two types of SPs are considered in this counterfactual, CC SPs and RD (Regular Deal) SPs. The CC SPs behave the same as they did when Fil+ existed. As for RD SPs, we test two behaviors: 1) they behave the same as CC SPs, and 2) they behave the same as Fil+ SPs.  Behavior is defined as the amount of power the SP will onboard for a given network FoFR value. 

While the above gives us some idea of what may have happened, we probe it further to simulate a case where SPs would have onboarded more power, had Fil+ never been implemented. This is implemented with a boost, a multiplier applied to the amount of onboarded power, for a given FoFR value.  For example, if historically, a CC SP onboarded 5 PiBs/day, if the NetworkFoFR was 30%, the 2x boost behavior means that same SP now onboards 10 PiB/day. We simulate boost values of 2x, and 3x. Relevant network KPIs are shown in Fig 7.

![](https://hackmd.io/_uploads/Sy1YP2ORn.png)
*Figure 7. Various scenarios explored to forecast the network state in the counterfactual scenario that Fil+ subsidy was never put forth.*

The takeaway from this experiment is even in the counterfactual scenario where Fil+ did not exist and agents onboarded 3x as much raw-byte power for a given FoFR, network would most likely have less overall raw-byte power, less minting and less locking than its current state.

This aligns with the intuition that had the network economic incentive for data storage not existed, less data would have been stored. 

<!-- ## What makes Filecoin Filecoin
### Other storage Networks
In this section, we differentiate Filecoin from other decentralized storage networks, Chia, Arweave, and Storj. 

Chia is a decentralized “green” proof of work network. Chia’s purpose is not to store data, but rather to use data to create signatures (plots) that can be used for consensus. Thus, while it uses storage, it is not made for storage. This comparison is therefore not directly relevant to Filecoin under its stated mission.

ARWeave is a decentralized storage network that aims to store data permanently. It differs from Filecoin in this regard, because in Filecoin, data is stored for sector durations. In ARWeave, a user pays a relatively large amount (compared to Filecoin or AWS) to onboard data into the “weave.” The data is then served and replicated by clients, who are incentivized by CryptoEconomic mechanisms to continue to store that data for perpetuity. Data is considered “useful” if it is onboarded, since a client has to pay to onboard it. Currently, ARWeave has 129.03 TiB of data stored.

Storj is another decentralized network that enables storage of data. Storj nodes share underutilized hard drive capacity and bandwidth with the Storj network and are paid when users store and retrieve data. They pay node operators for the following:
The use of storage space by users ($1.50 USD per TB per Month) and egress bandwidth used when users retrieve data from the the network ($2.50 USD per TB per Month). Node operators get paid only for the storage and retrieval of data which the clients wish to store on the network. The storage of any other data, or just committed storage capacity is not rewarded by the network. 

The examples of ARWeave and Storj show us that Filecoin is not the only network that values storage of data, other networks also do. What differentiates Filecoin from these other networks is that Filecoin enables a variety of use cases. It supports both 1) SPs that store data on the network (FIL+ SPs) and 2) SPs that provide consensus security and storage capacity to the network (CC SPs). This flexiblity enables Filecoin to fulfill its mission of “storing humanity’s most important data.” FIL+ SPs utilize the 10x multiplier subsidy to help pay for additional associated costs, while enabling important data to be onboarded (examples include SETI, CERN, etc ...). Conversely, CC SPs help to secure the network and simultaneously create capacity that can be utilized to store data in the future (whether through RDs or through FIL+), rather than provide consensus for the sake of consensus. This flexibility and co-existence of CC and FIL+ mining has led to the massive amount of data stored on Filecoin. When compared with ARWeave, Filecoin has, with conservative estimates accounting for FIL+ disputes, 3X the amount of “useful” data. This data will then induce demand for value-add services to be built. Thus, amassing useful data storage on the network is a critical step in Filecoin’s development. While imperfect, Fil+ has contributed significantly to onboard a significant amount of useful data. Improvements will only accelerate this trend and enable Filecoin to fulfill its mission.

### What makes the Filecoin Network valuable?
The value of a token or currency in any economy is fundamentally derived from its utility and demand for transactions. A token is only as valuable as the applications and services that it enables. Bitcoin (BTC) is a unique case because it is not just a digital asset, but also a neutral sovereign money that was designed to be inflation-proof and free from government influence.  Given its wide adoption since its inception, which was shortly after the 2008 financial crisis, network effects made it exceedingly difficult for another PoW cryptocurrency to replicate its success. The key reason might be that there's room for only one dominant economy for such a neutral sovereign money. The positive feedback loop of BTC’s value increasing with its mass adoption very early on allowed it to be that dominant economy. To date, BTC continues to be one of the most successful crypto projects, and it is considered to be one of the most valuable digital currencies. 

Ethereum, on the other hand, distinguishes itself with a diverse network of interconnected decentralized applications (dApps). Additionally, Non-Fungible Tokens (NFTs) have proven to be compelling use cases unique to Ethereum. DeFi (Decentralized Finance) further amplifies Ethereum's demand, as it allows for the creation of new tokens, their collateralization for borrowing, and the purchase of assets using stablecoins, all within the Ethereum ecosystem.

For Filecoin to achieve success, it must carve its own path, through a variation of Proof of Useful Work. In order for the project to achieve its vision of storing humanity's most important information, it needs to incentivize the storage and sharing of valuable data on its decentralized network. While there may be various implementation methods, trustless Filecoin Plus stands as a promising strategy, despite its imperfections. This strategy ensures that incentives flow to genuinely valuable data, safeguarding the integrity of the network. In the quest for a sustainable decentralized storage economy, incentive structures such as Filecoin Plus seem to be a pragmatic approach. -->

## A Pathway for improving Filecoin Plus
Currently, at least 1 of the 3 tools say that nearly 45% of the datacap allocated today has open disputes with no resolution. In an ideal case, datacap abuse would be kept to a minimum. We believe that by improving the incentive structures in place, we can address this problem and make significant steps towards achieving the goal of no datacap abuse.

For instance, escalating penalties for bad notaries and SPs, similar to the verification game used by [Truebit](https://people.cs.uchicago.edu/~teutsch/papers/truebit.pdf) and the solver challenger framework used in optimistic rollup, is a way in which datacap abuse can be addressed. In such a framework, the process would unfold in several rounds, each refining the focus of the dispute and narrowing down the problematic behavior. An example of what this may look like is given below:

* **Initialization**: The process could commence with a challenge originating from a concerned party, the "Challenger." The Challenger might encourage the entity facing scrutiny, the "Solver", to verify the validity of a specified fraction of datacap allocation.
* **Challenges and Iteration**: In subsequent iterations, the Challenger could gradually present challenges to subsets of the Solver's datacap allocation within the stipulated time frame. As the iterations progress, the challenges could evolve to become more precise, delving deeper into the intricate aspects of datacap utilization. The iterative nature of this process could enhance the accuracy of identifying potentially abusive practices.
* **Final Determination**: The verification game could culminate when the challenges reach a stage where the trusted entities within the network, the “Judged” are in a position to render a conclusive judgment regarding the justification of the challenges. This would include an evaluation of both the validity of the challenges presented by the Challenger and an assessment of the Solver's adherence to the established regulations.
* **Punishment and Incentives**: In the event that the challenges are validated, and abusive behavior is substantiated, penalties might be imposed upon the offending party. These penalties could include fines or temporary suspension of datacap privileges. Conversely, if the challenges prove unfounded and the Solver's practices are indeed legitimate, the Challenger could be responsible for covering the expenses linked with the verification process, thereby ensuring that this privilege is not abused. 

Our call to action for the community is to improve this, criticize it, think of different, better solutions, and bring the Filecoin Plus program up to date to ensure data storage is the rational choice. 

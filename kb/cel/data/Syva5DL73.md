# Token Utility in Qredo

#### Maria Silva and Juan P.M. Cianci, CryptoEconLab, May 2023

This report focuses on the QRDO token. We start by discussing how the token is being used today. Then we do an exploratory analysis of the monetary value being generated by the Qredo Network and discuss some proposals to increase token.


## QRDO usage today

There are currently two main use cases for the QRDO token; one as a *form of payment* for *service fees*, and the other as a *synthetic staking* token, where users receive rewards for accumulating QRDO in their Qredo wallets, without the need for such a token to be locked in a staking pool. We discuss these two use cases in more detail bellow. 


### Form of payment

The Qredo network relies on *service fees* from transactions to capture revenue. These fees are only applicable to certain outgoing transactions, namely
-  *Withdrawals*, which are external transfers to any other address not part of the Qredo Ecosystem, and 
- *Smart contract/API calls*, which are invoked when Deploying assets from a Qredo web3 Wallet into a Decentralized Application (dApp).

We discussed each of these use-case and the fee system in the previous [report](/4M4kpUI6QGGsyP_kpbcACw).

All other transfers within the Qredo ecosystem are not considered billable events. Qredo users do not pay service fees for assets under custody, depositing tokens, setup fees or maintenace fees. 

Service fees can be paid in either QRDO, USDC or USDT. The network incentivises the use of the QRDO token by providing a 15% discount on these service fees if paid with the QRDO token. However, there are still a big majority of fees being denominated in USD.


### Synthetic staking

Currently, there is no formal staking mechanism *per se* in the Qredo network. Instead, Qredo offers a weekly staking event with a 5.05% APY reward for holding QRDO tokens within the Qredo Network. This *synthetic staking* (i.e., no need to lock tokens into a pool) is automatic and rewards are distributed every Monday. 

Furthermore, this staking occurs on a per-wallet basis, not per account, and users are allowed to  withdraw QRDO at any time. However, this means that they would forfeit any accrued rewards for the amount withdrawn. Similarly, transferring QRDO between wallets within the same account resets the staking and results in reduced rewards. See [here](https://qredo.zendesk.com/hc/en-us/articles/5806237485585-Ongoing-Weekly-Staking-Events) for more details. 


## Qredo's production value
<!---
:::warning
:warning: This analysis is based on incomplete transaction data (due to data availability issues). We will revised it in phase 2 of the project.
-->


While a big part of Qredo's value stems from it's *intrinsic value,* such as the value stemming from the innovation it proposes, in this section we will we focus on the *monetary value* of the Qredo network. This corresponds to the fees captured by the network, its transaction volume, and the price and transaction volume of the `QRDO` token. We now present a quick analysis of these quantities. 


### Billable volumes

This section focuses on the billable transactions within the Qredo network. We present a histogram of these transactions alongside their summary statistics below. The figures distinguish between MetaMask Institutional (MMI) and others (QL2). Note that the histogram uses a logarithmic scale.

As depicted, MMI transactions, on average, move six times the volume of QL2. However, there is a substantial variation in this amount, evidenced by a considerable standard deviation. A glance at the quantiles indicates that the volume handled by MMI transactions consistently surpasses that managed by QL2.


![](https://hackmd.io/_uploads/S1OgFPjO2.png)



|       | Amount MMI (USD/Trx) | Amount QL2 (USD/Trx) |
|-------|------------------|:----------------:|
| count | **25577**            |       4483       |
| mean  | **662459**           | 24138.3          |
| std   | **4.2788e+06**       | 162773           |
| min   | 1.49562e-16          | **1.21912e-06**  |
| 25%   |**274.37**            | 68.3859          |
| 50%   | **4496.62**          | 437.27           |
| 75%   | **60000**            | 4177.04          |
| max   | **2.46947e+08**      | 5.6e+06          |

In addition, we provide the summary statistics for the service fees collected from these transactions. On average, an MMI transaction collects \$40 in fees (about 4x more than QL2). However, there is a significant right skew, indicating that there are some exceptionally large MMI transactions, resulting in correspondingly substantial service fees. The quantiles up until the 75\% mark seem fairly comparable between MMI and QL2.

|       | MMI fees (USD/Trx) | QL2 Fees (USD/Trx) |
|-------|--------------|-------------:|
| count | 25577        |         4483 |
| mean  | 40.8994      |      13.3957 |
| std   | 215.875      |      41.0204 |
| min   | 1            |            1 |
| 25%   | 1            |            1 |
| 50%   | 1.4992       |      2.39203 |
| 75%   | 11.6608      |      10.6269 |
| max   | 12347.3      |      1070.84 |

Next, we look at the time series of billable volume and collected fees, both in MMI and QL2. While these time series seem rather stationary (meaning that the distribution of these quantities has remained fairly constant over time), there is a slight sip on the daile volume since may 2023. 

![](https://hackmd.io/_uploads/SyEEhDsun.png)

![](https://hackmd.io/_uploads/r1V-RPsuh.png)

|      | Daily amount (Million USD) | Daily Fee (Thousand USD) |
|------|----------------------------|--------------------------|
| mean | 72.5614                    |                  4.70696 |
| std  | 199.456                    |                  11.6657 |
| min  | 0.116151                   |                0.0543835 |
| 25%  | 8.26597                    |                  1.16686 |
| 50%  | 26.0073                    |                   2.2883 |
| 75%  | 72.7197                    |                  4.71732 |
| max  | 2743.57                    |                  148.363 |


Computing the monthly amounts of service fees yields the following table:

| Date       | Fees (1000 USD) |
|------------|-----------------|
| 2022-10-31 | 109.685437      |
| 2022-11-31 | 242.520284      |
| 2022-12-31 | 47.250013       |
| 2023-01-31 | 68.158496       |
| 2023-02-28 | 127.146698      |
| 2023-03-31 | 208.948746      |
| 2023-04-30 | 166.746076      |
| 2023-05-31 | 117.807864      |


### Number of transactions


The focus now shifts to the analysis of the number of transactions, assessed on both daily and monthly bases. Here we observe that the MMI transaction volume has increased slighty in the end of 2022 and, since then, has decreased slighty. We also notice a considerable variance in the number of QL2 transactions. The internal transaction remain steady throughout the interval.


We should note that the recurring peaks observed in QL2 transactions are due to the vesting related to the synthetic staking mechanism, a non-surprising fact given the automatic nature of this mechanism under relatively mild conditions.

![](https://hackmd.io/_uploads/H18GN1mcn.png)


Similar conclusions can be drawn from this data on a monthly basis, which we show below, for completeness.

![](https://hackmd.io/_uploads/B1_KQ1Qqn.png)

Finally, we investigate the daily and monthly transaction counts alongside their summary statistics. The figure on the right implies a decrease in the average number of transactions since 2023, especially compared to the period between May 2022 and late 2022.

On average, the network handles approximately 235 (daily) and 6900 (monthly) transactions. It's worth noting that the daily transaction count has a more pronounced right tail, as indicated by the small 75% quantile compared to the mean. This trend is not as pronounced in the monthly data, suggesting occasional spikes in daily transactions but less variation in the monthly totals.

<div style="text-align:center">
<img width="49%" src="https://hackmd.io/_uploads/ByKESJQc2.png"><img width="51%" src="https://hackmd.io/_uploads/ry4SH1mc3.png">
<br/>
<br/>
</div>


|      | Daily No. Trx | Monthly No. Trx |
|:----:|--------------:|----------------:|
| mean | 235.41        |         6902.34 |
| std  | 929.66        |        13744.19 |
| min  | 1             |               9 |
| 25%  | 17            |             592 |
| 50%  | 37            |            1225 |
| 75%  | 70            |            2076 |
| max  | 14303         |           53962 |


### Synthetic staking

One of the most salient features of the Qredo network is its current synthetic staking mechanism. Below, we plot the historical volume of staking as well as its summary statistics. From there, we can see that such events represent an average volume of ~150K USD/week (since events occur on a weekly basis). Furthermore, this volume is well concentrated around its median, suggesting that the volume due to staking events is less volatile than the total transaction volume. We will discuss future staking mechanisms in a future writeup, however, it is worth mentioning that the network's plans to move towards a Delegated Proof-of-Stake consensus algorithm could, potentially, generate additional value-capturing opportunities.



| ![](https://hackmd.io/_uploads/S1NcdS242.png)| ![](https://hackmd.io/_uploads/HJOkFH24n.png)|
| -------- | -------- | 
| *Historical volume*     | *Summary statistics*     |




### L1 Transactions (Ethereum)



We now investigate the transaction volume of the QRDO token in the Ethereum network. From the figures below, the daily average volume of the QRDO token is about 3.4M USD, with a 50% quantile of roughly 656000 USD. Notice that this implies that there's, on average, a larger volume of QRDO traded in L1 than all other tokens traded in the Qredo L2.


![](https://hackmd.io/_uploads/BycnEpsV3.png)


|      |      Daily volume (QRDO) |   Daily volume (USD) |
|------|------------:|------------:|
| mean | 2.83758e+06 | 3.39956e+06 |
| std  | 5.87171e+06 |  1.0009e+07 |
| min  |        5918 |     7655.35 |
| 25%  |      610631 |      202886 |
| 50%  | 1.26878e+06 |      656620 |
| 75%  | 2.50944e+06 | 3.40805e+06 |
| max  | 6.44095e+07 | 1.82456e+08 |

Examining [market data](https://etherscan.io/dex?q=0x4123a133ae3c521fd134d7b13a2dec35b56c2463#transactions) also reveals that there were about 100 DEX-related transactions for the QRDO token on the last month, which is a much smaller number compared to all other transactions. This could be used as an opportunity to generate additional value by e.g., incentivising and promoting the creation of a decentralised QRDO liquidity provider.

It is worth mentioning that while the value generated by L1 transaction fees is not captured by Qredo (but rather by the Ethereum network), these volumes are also evidence of (i) the value that the company is created, even if indirectly and (ii) a potential market that can be partly captured, by, e.g., further incentivizing P2P trading inside the L2 Qredo network. 


## Token features

Now that we have a clear picture of the value being generated by the Qredo Network, the next question is how to capture that value best and fairly distribute it among participants. 

Tokens can have multiple features, depending on how they are designed. Each feature is not exclusive, meaning that different features can be combined in the same token. For the context of this repot, we will, we will consider the following features:

1. **Membership Feature.** Membership tokens offer holders access to a specific network, platform, or service. They essentially function as "access tickets" and can be compared to a subscription or a software license. Their value often lies in the exclusivity of the service they grant access to. For example, a token might offer access to a unique data set or a specialized blockchain-based service. As an example, Basic Attention Token (BAT) uses this model. Users hold BAT tokens to access premium services in the Brave ecosystem.
2. **Staking Feature.** Staking is used as a form of collateral or 'stake' in a network. Users lock up their tokens in the network to participate in the network and receive rewards from newly minted tokens. The value of these tokens often comes from the potential earnings from staking. Ethereum 2.0 is the most known example of this model, where ETH holders can stake their tokens to secure the network and earn rewards.
3. **Work Feature.** Work tokens give the holder the right to contribute work to a network and earn the fees collected from users. The value of these tokens is tied to the demand for the network's services and the holder's ability to provide these services efficiently. For example, Storage Providers in Filecoin must use FIL to onboard storage into the network, which allows them to collect fees from any clients' deals using that storage.
4. **Governance Feature.** Governance tokens provide holders with voting rights in the network. They enable decentralized decision-making and control over the network's parameters or direction. The value of these tokens often stems from the influence they confer over a network's development and the potential future value of those decisions. MakerDAO (MKR) and Compound (COMP) are examples of this model. Token holders can vote on various aspects of the platform's operation and rules.
5. **Revenue Sharing Feature.** Revenue-sharing tokens entitle holders to a share of the network's profits or revenues. This model is a form of digital cooperative, where token holders are also the network's stakeholders. The value of these tokens is directly tied to the financial performance of the network. For example, KuCoin Shares (KCS) operate on this model, sharing a portion of exchange trading fee revenue with token holders.
6. **Payment Feature.** Payment tokens are used as a medium of exchange within a specific network or platform. They can be used to purchase goods and services or even to pay transaction fees. Their value lies in the utility they provide within the specific ecosystem they operate in, and they often play a critical role in facilitating transactions and interactions within the network. Bitcoin (BTC) is a prominent example of this, where users pay transaction fees with BTC.
7. **Reward/Penalty Feature.** Tokens can also be given to users as incentives for participation in a network or for performing certain actions, like content creation, curating, or community participation. They can also be used as deterrents for undesirable behavior, where certain unwanted actions are penalized by having their tokens slashed. The value of these tokens can be tied to the overall value of the platform, as they can often be redeemed for goods, services, or even cash within the platform. An example would be social media platforms that reward active users with tokens. Steem (STEEM) operates in the form of this model, rewarding users for creating and curating content.
8. **Funding feature.** Tokens can also be used to fund the operations that build the protocol itself. This includes a mixture of paying for the human capital building the tech behind the economy, and/or paying early investors in the project. This feature does not necessarily correlate with the value of the token, although it is oftentimes needed to kick-start and maintain the project.

### QRDO token features

What about Qredo? Which features fit the Qredo network? The following table summarises how the main features of QRDO.

| Feature         | Usage in Qredo                                                                                                                   | Right/Benefit                                              | Stakeholders        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|---------------------|
| Staking         | Tokens are locked to secure the protocol and enable the federated PoS consensus model. In turn, rewards are distributed. | Receive a share of rewards and fees                        | Stakers, Validators |
| Work            | Validators are elected by the community to run the protocol and receive rewards                                          | Receive a share of rewards and fees & execute requests     | Validators          |
| Governance      | Tokens are used to vote on protocol proposals (QPIPs).<br>More tokens = more voting power                                        | Participate in the decision-making process of the protocol | Token holders       |
| Payment         | Tokens are used to pay protocol fees and/or service fees                                                                         | Use Qredo services and make protocol requests              | Clients             |
| Reward/Penalty  | Airdrops and quests from a dedicated fund are used to incentivize participation and adoption of product features                 | Access Qredo services at a discount                        | All                 |
| Funding         | Tokens are awarded to key contributors (either for building the protocol and service and/or providing early funding)             | Share the success/value of the network                     | Developers          |


The *staking* and *work* features will function together within Qredo's Staking Model. The long-term vision is to implement a Delegated Proof-of-Stake model. However, as a transition phase, the network will start with a federated Proof-of-Stake model. The main difference between the two models is that the Stakers contribute to a single staking pool which is distributed among the Validators. Thus, all Validators have the same consensus power and Stakers do not vote on which Validator will produce a given block. These two models are further explored in a dedicated [report](/HbRt4hkHQqK-ykDXr10Y-Q).

*Governance* is another key feature for QRDO as it has the potential to increase community engagement and transparency in the decision-making process. When establishing a new governance process, several aspects need to be considered:

1. **The governance model:** What governance structure should be used? Some common systems include voting-based governance, soft consensus with a Foundation, and a Decentralized Autonomous Organization (DAO). It's essential to consider the platform's goals, values, and community expectations while deciding on a model that balances decentralization, security, and ease of use.
2. **Scope:** What types of decisions can be made by the community? what stakeholders need to be involved? And what level of authority is granted to each participant? Does the community have the power to change all the protocol features? Or are decisions limited to specific components or parameters?
3. **Decision-making mechanism:** What is the exact process to go from a proposal to approval and implementation? Do we have different rounds of voting to reach a consensus? How many votes are required? Do we require community discussions before a more formal proposal?
4. **Resources:** Does the community have access to a treasury? If yes, how is the treasure funded? What is the scope? And what mechanisms should be followed before allowing the deployment of funds?

This is an area that the team is actively working on. But, for the purpose of this project, we will not explore it further as we expect that, in the short term, its impact on token supply and demand will be small when compared with other token features.

The next feature we considered is *payment*. Here, we have multiple fee models we could use. Particularly, Qredo will implement two types of fees:

* Protocol fees - fees that need to be paid when submitting requests to the Qredo network. The goal is to avoid spamming attacks to the network and to support Validator operations.
* Service fees - these are the fees already being paid by Qredo costumers in a pay-as-you-go model based the total volume transacted in billable operations. The question here is how to tie value of these service fees (which currenlty are mostly paid in fiat-denominated currencies) to the QRDO token.

Theses questions and the proposed design for Qredo's fee models will be further explored in another [report](/v5r6y8a_TE6NtouVHmPnmA).

For the last two features, we have *reward/penalty* and *funding*. Both features involve dedicating a part of the token supply for these two uses. We will look into this breakdown and how it will impact token supply in a specific [report](/3Xwe-CZ8TPiC80Fg2r5qtQ).

Finally, we should note that, currently, we are not considering a *membership* feature for QRDO. Qredo could implement this feature by requiring a certain amount of Staking for Clients to access particular services or features within the Qredo platform. However, this strategy is risky as it limits client adoption. Instead, the same value could be collected by charging directly for the service provided, thus increasing the value being produced and shared among network participants.




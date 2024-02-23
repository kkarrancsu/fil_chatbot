# The Qredo Network's Economy


#### Maria Silva and Juan P.M. Cianci, CryptoEconLab, May 2023

In this report, we analyse Qredo through the lens of an island economy. We provide an overview of the current functioning of Qredo's economy and discuss the vision for the next phase in Qredo and its economy.

But before disucssing Qredo in particular, we need to strat by giving an overview of what we maen by "island economies"


## Island Economies

Island economies refer to economic systems that are relatively isolated and highly depend on foreign trading. While the term "island economy" is often used in a literal sense to refer to the economies of actual islands, it can be more broadly applied to economies that share some key features present in physical islands, such as:

* **Limited resources.** Island economies usually have limited resources and thus need to rely on imports to supplement local production and acquire resources needed for their own internal production.
* **Limited demand.** Island economies also tend to have small populations, meaning the internal market for island production is limited. Thus, these economies depend heavily on exports and foreign investment for sustainability and growth.
* **Currency risk.** Many islands have their native currency. These native currencies can be exchanged with other currencies or fiat money. The exchange rate plays a crucial role in determining the purchasing power of the native currency, and strong exchange rates are essential for acquiring resources from external economies. This currency risk is enhanced by the economy's reliance on foreign trading.

Island economies and blockchain networks share several striking similarities. Both systems encompass the production and exchange of goods and services facilitated by their native currencies (the native token). Both highly depend on "foreign trading" and can suffer currency risks. Both rely on humans to optimally organize the economy's limited resources to produce goods and services that can be traded with the outside.

In this context, blockchain networks implement algorithmic protocols that enable their workers (the "miners") to organize resources and participate in the production of a specific good/service. These protocols include rules for token issuance and allocation to network participants and regulations for token outflow (i.e., when tokens are removed from circulation permanently or temporarily). This management of circulating supply dynamics is a crucial aspect of blockchain economies, similar to how island economies manage their resources.

Sound blockchain economies thus require handling two key factors:

1. **Currency risk management.** The price of the native token needs to be high enough so that network participants can pay for their production costs and access external resources (e.g., hardware and energy) while maintaining a sustainable operation. At the same time, the price must be reasonable to make the goods or services produced unaffordable. One lever to achieve this balance is to adapt the token supply (on both inflows and outflows) to meet the demand for the token. Connected to this is the idea of tying token usage with the good or service produced by the economy, making it easier to assess demand. For instance, on Ethereum, users must pay gas fees in Ether to run computations on the Ethereum blockchain. This means that demand for Ether is strongly connected with the usage of the Ethereum EVM. At the same time, the total token supply is infinite. The protocol implements an algorithm to control minting rates so that there is a slow increase in token supply, thus meeting the expected growth in token demand.
3. **Fair value redistribution.** Network participants are central to the functioning of a blockchain economy. If they don't dedicate resources to develop the economy's exports, the entire economy collapses. Therefore, the protocol must be aware of the value its economy is generating and make sure that a fair share is being distributed among the participants based on their contributions. There are two sides to this - the first is to measure the actual value being generated (and this may be value being transacted in native tokens and/or other currencies), and the second is to calculate the contribution of each participant correctly so that rewards can be fairly distributed. A common question here is what should the reward split be between validators and Stakers in a Proof-of-Stake consensus?

There are no universal answers to these problems as they are highly dependent on the particulars of the economy and blockchain network. So, let's start by analyzing Qredo through the lens of an island economy and then discuss options to address each of these factors more concretely for Qredo.

## Qredo's Economy

The Qredo Network is a decentralized custody platform designed for businesses and investors to manage their digital assets. It focuses on reducing risks associated with transactions, counterparty interactions, and asset theft, while also allowing for independent control without relying on external parties.

At its heart, Qredo is a custodian of crypto assets. It offers a new model where the crypto wallet is not controlled by a central entity (as with centralized exchanges such as Coinbase) while making it easier to sign transactions and interact with Web3 apps than cold wallet providers such as Ledger.

To achieve this new model, Qredo built a decentralised asset custody protocol that relies on a set of validators for maintaining consensus and executing the requests submitted to the network. A request may be executing a transaction within Qredo's Layer 2 network (e.g., token swaps between users, creating a wallet, etc.), executing a "bridge transaction" (i.e., depositing or withdrawing assets from Qredo to other blockchains), or signing/approving a transaction in another blockchain (e.g., remote calls to Ethereum contracts).

Instead of using traditional private keys, Qredo's protocol employs a Multi-Party Computation (MPC) architecture. This method signs and validates transactions collectively, providing a higher level of security for users' assets.

In addition, Qredo's network works as a Layer-2 blockchain that can connect with other Layer-1 blockchains such as Ethereum or Bitcoin. The L2 network operates on top of existing blockchains and provides a separate infrastructure to manage transactions and interactions among users.

With this in mind, let's define the following features of Qredo's economy: (1) goods and services produced, (2) stakeholders, (3) production costs and (4) native currency.

### Goods and services produced

The primary product of the Qredo Network is the Qredo Wallet, a web application that provides secure storage for cryptocurrencies and enables quick transfers and exchanges between different blockchain networks. It is designed to accommodate the needs of businesses, allowing them to set up access controls and governance rules for managing their digital assets.

 As such, Qredo supports two main use cases as of May 2023, which we will detail next.

**1. External transactions**

The first use-case is to allow clients to interact with Web3 dApps built on the L1 networks supported by Qredo. This means that clients can use Qredo as their custodian for initiating transactions with other Web3 services. Qredo achieves this by being the only MPC-based custodian that integrates with [MetaMask Institutional (MMI)](https://metamask.io/institutions/).

After setting up the integration, if a user wants to submit a transaction to a DeFi protocol, they only need to initiate it using the MMI browser extension and then Qredo manages the transaction signing and approval.

The image below illustrates an example with AAVE, the largest DeFi Lending Protocol.

<div style="text-align:center">
<img width="700" src="https://hackmd.io/_uploads/S1LXCMt4h.png">

*Source: [MetaMask Institutional](https://metamask.io/institutions/)*
<br/>
<br/>
</div>

This feature is particularly useful for cases where the transaction signing process requires different parties to approve. This can be easily done through the Qredo interface.

Currently, Web3 dApps interaction is the largest use case within the Qredo network. Currently, users of this service are primarily corporate and institutional clients.

All external transactions incur a service fee, making this one of the key income generation verticals for Qredo. 

The network utilises a *Pay-as-you-go* fee model, in which users only pay for the (billable) transactions that they make. The service fee for each user is computed using a pricing curve which reduces the price as the total total amount of traded volume over the last 30 days, increases. The minimum fee per trasaction starts at $1 (or its token equivalent), and caps out at 1% per transaction. The figure below shows the cost curve based on the monthly billable volume.

<div style="text-align:center">
<img width="500" src="https://hackmd.io/_uploads/By_rTkgV2.png">

*Source: [Qredo Website](https://www.qredo.com/fees)*
<br/>
<br/>
</div>

**2. Qredo Layer 2 transactions (QL2)**

The second use case is token swaps within Qredo's L2 network. Users can deposit any of the [supported cryptoassets](https://qredo.zendesk.com/hc/en-us/articles/4407177502097-Supported-Assets) and trade them with other Qredo users. Thus, Qredo Swaps enable cross-chain transactions, meaning users can swap digital assets between different blockchains, such as Ethereum and Bitcoin.

To use Qredo Swaps, users must first deposit their cryptoassets in the Qredo Network. When an asset is deposited, a synthetic version of that asset is created in the Qredo network - a qAsset. Users can swap qAssets freely inside the network. 

Then, after all swaps are completed, the user can withdraw their qAssets. Withdrawing from Qredo means that the L1 assets associated with the qAsset are unlocked and sent to the user's L1 wallet, while the qAsset is destroyed.

It is important to note that Qredo is not an exchange, meaning that there is no mechanism (centralized nor decentralized) to match sell and buy orders. Instead, users must find willing peers to trade with. To support this, the team is planning to launch the Liquidity Hub, which will function as public marketplace that contains a list of Qredo Swaps shared by users. Anyone can browse, select, and take swap quotes that suit their needs.

Currently, users of this service are primarily corporate and institutional clients. While Qredo does not charge service fees for Qredo Swapps, they charge for withdrawals. Withdrawals use the same fee model as external transactions. In fact, the entire trading activity is combined to derive the total 30-day billable volume.


### Stakeholders

There are 5 main stakeholder groups within Qredo's economy, which we will detail next.

<div style="text-align:center">
<img width="450" src="https://hackmd.io/_uploads/Sy9HrfzHh.png">
<br/>
<br/>
</div>

* **Validators** are the "workers" of the economy. They are responsible for running the decentralized custody network and executing transaction requests. For this, they are compensated. This compensation may be a mixture of newly minted tokens (QRDO) and a cut of fees collected by the network. Note that this group includes the Multi-Party Computation nodes (responsible for the generation, storage, and usage of wallet keys) and the Validator nodes (responsible for verifying and validating transactions within the Qredo network)
* **Stakers** are the "external" investors of the economy. They bring capital from the outside to buy the native token (QRDO) and use that token to support validator operations and increase security and confidence in the protocol. For this, they are also compensated, which usually takes the form of minted tokens. Validators and Clients can be Stakers, which is fairly common in other blockchain economies. Staker behavior is super important to understand token flows as they directly impact both inflows and outflows - when they stake, they remove tokens from circulation, thus increasing demand, and when they un-stake, they add tokens to circulation, thus increasing supply.
* **Clients** are the "outside buyers" of the economy. They bring capital and spend it in the economy by buying the services offered by Qredo. Some clients may also be internal to the economy, meaning they are Validatiors or Stakers spending tokens they received from minting. Clients are another key group influencing token flows as they are the driver of adoption and a powerful influence to token demand.
* **Developers** are the "civil servants" and "builders" of the economy. They are responsible for maintaining the core systems and implementing new features to improve the services provided by the economy. For this, they are also compensated. As with Validators, this compensation may be a mixture of newly minted tokens (QRDO) and a cut of fees collected by the network. As Qredo is in active development, Developers are still an important group to maintain and engage.
* **Token holders** are akin to the "voters" in the economy. They hold a piece of the economy by buying and holding their native token. Holding the token will give them specific access to discussions and/or decision-making power, depending on the governance model. Token holders are not directly compensated by the economy. Their incentive should be to access the governance process. In reality, we know that speculation also plays a part in the incentives for token holders. However, in the long run, this is unsustainable for the economy. Holding tokens without actively participating in the economy (as Stakers and/or Clients) should be the exception, not the rule. As with Stakers, token holders can impact token demand as they are a key group in the secondary market for native tokens.

### Production costs/resources

* **Hardware**, which is usually an initial expense on the part of Validators.
* **Operational costs**, which include all the ongoing costs of running a Validator node, including energy, human labor, and physical space (i.e., rent)
* **Capital** is used to cover the staking requirements of Validators and is usually supported by Stakers.


### QRDO Token 

[QRDO](https://coinmarketcap.com/currencies/qredo/) is an ERC-20 token deployed on Ethereum. QRDO has a maximum supply of 2B tokens. However, when it was first launched, only the first 1B tokens were allocated. From these 1B tokens, the total supply is now 860M, after the team decided to burn 140m tokens [in March 2022](https://www.qredo.com/blog/qredo-tokenomics-update).

If we exclude tokens locked and investor/team allocations, the current circulating supply is roughly 300M QRDO tokens and the market cap is hovering around 37M USD ([source](https://coinmarketcap.com/currencies/qredo/)).

In what follows we examine some aspects of the QRDO token and derive some insights about its supply and market dynamics. 

- **Updated vesting schedule.** In March 2022, the team flattened the token release curve, which almost double the previous vesting periods for the team and investors. The plot below shows the two vesting trajectories. 


<div style="text-align:center">
<img width="650" src="https://hackmd.io/_uploads/rJlXsBzNn.png">

*Source: [Qredo Token Update blog post](https://www.qredo.com/blog/qredo-tokenomics-update)*
<br/>
<br/>
</div>


<!---
- **Holders.** According to [Etherscan](https://etherscan.io/token/tokenholderchart/0x4123a133ae3c521fd134d7b13a2dec35b56c2463), there are over 12873 QRDO token holders controlling roughly 860M tokens, or about 43% of the maximum supply. Furthermore, the top 100 wallets control about 760M QRDO tokens. This level of concentration is expected given that most token holders use centralized exchanges such as KuCoin or Crypto.com to hold their assets.

:::warning
:warning: Circulating supply is only 300M. Etherscan also consider tokens not yet vested not allocated.
:::

as it can be seen from the figure below, just 100 addresses control about 760M QRDO tokens, which signals a large concentration of said tokens. This large concentration is confirmed by examining the Gini index $G$, which we estimate to be ==COME BACK==. Presumably, many of these holders are institutional investors; indeed, [it can be seen](https://etherscan.io/token/tokenholderchart/0x4123a133ae3c521fd134d7b13a2dec35b56c2463) that *KuCoin* controls, at least, 30M QRDO. While this concentration might seem extreme, such a concentration of wealth is not uncommon in Web3, as it is easily seen with other ERC20 tokens (c.f. the case of [WETH](https://etherscan.io/token/tokenholderchart/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2) and [WBTC](https://etherscan.io/token/tokenholderchart/0x2260fac5e5542a773aa44fbcfedf7c193bc2c599), for example). 
<div style="text-align:left">
<img width="500" src="https://hackmd.io/_uploads/S1DQN1GNn.png">
</div>
*Source: [Add source!!!]()*
-->

- **Qredo L2 wallets.** [According to the Qredo block explorer](https://explorer.qredo.network), there are over 90K wallets in Qredo's L2 network. The evolution in time of the number of wallets is shown below. Notice how the rate of new wallets increased after November (2022), coinciding with (and presumably due to) the collapse of FTX. This may have been caused by an increase in token holders looking for safer custodians for their assets. 

<div style="text-align:center">
<img width="650" src="https://hackmd.io/_uploads/rk5jOJz42.png">

*Source: [Qredo Block explorer](https://explorer.qredo.network/)*
<br/>
<br/>
</div>


- **Availability.** [According to CoinMarketCap](https://coinmarketcap.com/currencies/qredo/), the QRDO token can be found in several centralized exchanges, namely Bitget, BingX, DigiFinex, BitMart, and KuCoin. It can also be traded in several Decentralized Exchanges (DEXs), such as *Uniswap* or *Kyber*, however, at the time of writing, [there does not seem to be a lot of liquidity](https://info.uniswap.org/#/tokens/0x4123a133ae3c521fd134d7b13a2dec35b56c2463) in these exchanges.

- **Token price and market dynamics.** Next, we plot the time series for the price of QRDO, as well as its day-to-day returns, and benchmark these quantities to those of BTC (a market indicator for crypto currencies).  As we can see from the time series of the token price (first plot), while there was a clear correlation between both tokens until June, 2022, this price correlation has noticeably dimished since. Notice, for example, that QRDO did not benefit as much from the market rally from the begining of 2023. Examining the time series of returns (second plot), reveals that the QRDO token is significantly more volatile than BTC. Lastly, we compute the [*beta*](https://en.wikipedia.org/wiki/Beta_(finance)) of QRDO with respect to BTC. Loosely speaking, *beta* can be understood as a measure of how sensitive the price of an asset is with respect to a reference market. Our computation yields a *beta* of $0.08$, which suggests that large changes in the price of BTC are not likely to signal significant changes in the price of QRDO. 

<div style="text-align:center">
<img width="600" src="https://hackmd.io/_uploads/By5p8xzV2.png">

*Source: [Yahoo finance](https://finance.yahoo.com/quote/QRDO-USD/)*
<br/>
<br/>
</div>

<div style="text-align:center">
<img width="600" src="https://hackmd.io/_uploads/Sy6EIlfN2.png">

*Source: [Yahoo finance](https://finance.yahoo.com/quote/QRDO-USD/)*
<br/>
<br/>
</div>


## Long-term vision

Looking forward, the Qredo Network will evolve across three axes:
1. Increased decentralization through Delegated Proof-of-Stake.
2. Enhanced the role of QRDO as Qredo's utility token.
3. More transparency and community engagement through open governance.

The end goal is to execute the vision of a truly decentralized custody network and to put the QRDO token at the center of Qredo's product. It is worth noting that, *currently*, the Qredo network is fully centralized (i.e., the validator nodes are run by the team).

In the next reports, we will add more details about these initiatives, with a particular focus on the [Staking Model](/HbRt4hkHQqK-ykDXr10Y-Q) and [Token Utility](/-W9X42cMRiiBxzROdfflWw).


## References

* [Qredo Product Guides](https://qredo.zendesk.com/hc/en-us)
* [Qredo Fee's page](https://www.qredo.com/fees)
* [Tokenomics Dashboard from Dune](https://dune.com/0x8868/Qredo(QRDO)-Token-Analytics)
* [Qredo Block explorer](https://explorer.qredo.network/)
* [QRDO's page on CoinMarketCap](https://coinmarketcap.com/currencies/qredo/) 
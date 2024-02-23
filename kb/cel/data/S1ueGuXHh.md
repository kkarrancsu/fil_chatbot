# Qredo tokenomics redesign - Intermediate report

#### Maria Silva and Juan P.M. Cianci, CryptoEconLab, June 2023

The Qredo Network is a decentralized custody platform designed to offer businesses and investors a secure and efficient way to manage digital assets. 

Qredo is currently going through a transaction phase. In 2021, they launched their token (QRDO), and, since then, they have been working on a set of features to improve usability and increase decentralization. Concretely, the network aims to evolve across three main axes:

- **A1**. Increased decentralization through a Federated Proof-of-Stake consensus system (and, later on, Delegated Proof-of-Stake). 
- **A2**. Enhanced the role of QRDO as Qredo's utility token.
- **A3**. More transparency and community engagement through open governance.

Ultimately, their goal is to execute the vision of a truly decentralized custody network and to put the QRDO token at the center of Qredo's product. However, to achieve this vision, the tokenomics underlying the network and its native token need to adapt, which is the reason why the Qredo Team partnered with CryptoEconLab to revamp the tokenomics of QRDO.

This collaboration was designed to encompass two main phases - the draft phase and the tuning and validation phase. The idea was to provide the general framework for the new tokenomics earlier and collect feedback before delving into the details of tunning and validating its key parameters.

This report is the main by-product of the first phase. Here, we provide an analysis of how the network functions now and detail some of the changes related to tokenomics that are expected to occur in the medium to short term.

We start by providing an overview of Qredo's economic landscape in [Section 1](#1-Qredo’s-Economy), delving into key stakeholders' roles, and a brief overview of its product offerings. Then, in [Section 2](#2-QRDO-Token-and-its-utility), we present a concise review of the current utilities of the QRDO token, alongside an outline of its future features and utility. [Section 3](#3-Fee-Models) and [Section 4](#4-Staking-Model) focus on two new economic mechanisms for Qredo, namely the Fee Models and the Staking Model (respectively). In both these sections, we provide an overview of the mechanism and highlight what components will be defined in phase 2. We finalize the report in [Section 5](#5-Final-remarks), where we outline the next steps in the development and analysis of Qredo's tokenomics update.

Each of the first 4 sections is based on a standalone report related to that topic. To provide an efficient review of these key aspects, each section consists of an  *executive summary* of its respective report together with a link to the full version of such a document for a more in-depth analysis. Alternatively, all reports can be found in the menu located on the left.

## 1. Qredo's Economy

This section is based on [dedicated report](/4M4kpUI6QGGsyP_kpbcACw).

### Qredo at a glance

The Qredo Network is a cutting-edge decentralized custody platform meticulously engineered to meet the demanding needs of businesses and investors seeking enhanced control and security over their digital assets. By mitigating risks associated with transactions, counterparty interactions, and asset theft, Qredo empowers users with independent control, eliminating reliance on external parties.

Qredo serves as a custodian for crypto assets, providing a novel approach that distinguishes itself from centralized custodians (e.g., Coinbase), in that Qredo does not exert central control over (the private keys of) the  crypto wallet. In addition, it distinguishes itself from other self-costody solutions by offering enhanced convenience for signing transactions and interacting with Web3 applications compared to cold wallet providers like Ledger.

To achieve this, rather than relying on traditional private keys, Qredo adopts a *Multi-Party Computation* (MPC) architecture, which enables collective signing and validation of transactions, elevating the security measures for users' assets. The  Qredo network operates as a Layer-2 blockchain that can seamlessly connect with Layer-1 blockchains like Ethereum or Bitcoin, providing an independent infrastructure to manage transactions and facilitate interactions among users.

Currently, Qredo is serving primarily corporate and institutional clients. However, with the new product features being introduced in 2023, the team hopes to gain market share in the retail space.

### Qredo Services

The primary *service* offered by the Qredo Network is the *Qredo Wallet*, a secure web application designed to store cryptocurrencies and facilitate swift transfers and exchanges across various blockchain networks. Specifically catering to the needs of businesses, the wallet allows for the establishment of access controls and governance rules to effectively manage digital assets.

As of May 2023, Qredo focuses on two primary use cases: *external transactions* and *Qredo Layer 2 (QL2) transactions*. 

*External transactions* allow clients to engage with Web3 decentralized applications (dApps) built on the supported Layer 1 (L1) networks. This offering is enabled by Qredo's integration with [MetaMask Institutional (MMI)](https://metamask.io/institutions/), making Qredo the only MPC-based custodian offering this integration. 

*QL2 transactions* are token swaps within Qredo's Layer 2 network. Users can deposit any of the [supported cryptoassets](https://qredo.zendesk.com/hc/en-us/articles/4407177502097-Supported-Assets) and trade them with other Qredo users, facilitating cross-chain transactions between different blockchains like Ethereum and Bitcoin.

In both use-cases, Qredo follows a Pay-as-you-go fee model where clients are billed based on the USD volume they transacted. We should note that not all transactions are billable. Only the transactions where monetary value is "leaving" the Qredo network (e.g. withdrawals or smart contract calls).

The fees are determined using a pricing curve that adjusts the price based on the total traded volume over the past 30 days. The minimum fee per transaction begins at $1 (or its equivalent in tokens), with a maximum cap of 1% per transaction.

In either case, it's important to emphasize that Qredo is not an exchange and does not provide a mechanism, centralized or decentralized, to match sell and buy orders. Instead, users are responsible for finding willing peers to engage in trades. To support this process, the team is developing the *Liquidity Hub*, a public marketplace housing a list of Qredo Swaps shared by users. This platform will enable anyone to browse, select, and execute swap quotes that align with their requirements.


### Qredo Stakeholders

There are 5 main stakeholder groups within Qredo's economy:

- *Validators*, who are responsible for running the decentralized custody network and executing transaction requests.
- *Stakers*, that buy and stake the QRDO token to support validator operations and increase security and confidence in the protocol while at the same time obtaining staking rewards.
- *Clients*, who use the protocol in exchange of fees (in both QRDO and other tokens).
- *Developers*, who maintain the protocol and introduce new feature.
- *Token holders*, who can participate in the governance process of the economy.


<div style="text-align:center">
<img width="450" src="https://hackmd.io/_uploads/Sy9HrfzHh.png">
<br/>
<br/>
</div>

All these stakeholders collaborate to support Qredo's economy and derive value from it. This collaboration is only possible because of the protocol encoding the rules of the economy and the the native token (QRDO), that guides the incentives of these network participants. In the next section, we will discuss the QRDO token and its role in more detail.

## 2. QRDO Token and its utility

This section is based on [dedicated report](/-W9X42cMRiiBxzROdfflWw).

### QRDO today

QRDO is an ERC-20 token that operates on the Ethereum blockchain. The token has a maximum supply of 2 billion tokens. From there, only the first 1 billion tokens were allocated, with the remaining tokens to be allocated and distributed at a later date.

In [March 2022](https://www.qredo.com/blog/qredo-tokenomics-update), the Qredo team decided to burn 140 million tokens, resulting in the current total supply of 860 million tokens. Excluding tokens that are locked and those allocated to investors and the Qredo team, the current circulating supply of QRDO tokens is estimated to be approximately 300 million (as of June 1st, 2023). According to [CoinMarketCap,](https://coinmarketcap.com/currencies/qredo/),  the market capitalization of QRDO at the time of writing was around 32 million USD. 

The QRDO token has two main uses within its ecosystem:

- **Form of payment**. As we previously discussed, Qredo charges service fees to its clients for using its custody products. Service fees can be paid in either QRDO, USDC, or USDT. The network incentivizes the use of the QRDO token by providing a 15% discount on these service fees if paid with the QRDO token. However, there are still a big majority of fees being denominated in USD.
- **Synthetic staking**. Qredo offers a weekly staking event with a 5.05% APY reward for holding QRDO tokens within the Qredo Network. This *synthetic staking* (i.e., no need to lock tokens into a pool) is automatic and rewards are distributed every Monday. 

One of the key outcomes of the tokenomics update currently underway is to increase QRDO utility and align it more closely with the value being produced by the Qredo economy. In the next subsection, we will discuss the new token features being introduced to QRDO.

### QRDO token features

There are two main changes being introduced to Qredo that will transform how QRDO will be used by the different Stakeholders:

- Two revamped Fee Models to align token usage with value creation within Qredo's platform. In particular, Qredo will introduce protocol fees and will create a fairer mechanism for transferring value between service fees to QRDO. 
- The launch of the Federated Proof-of-Stake to move to a more decentralized consensus and to allow the community to participate more in the process of running the protocol.

We will discuss both of these changes in [Section 3](#3-Fee-Models)
 and [Section 4](#4-Staking-Model). However, before delving into the details, the following table summarises the different features of the QRDO token once these changes come into effect:
 

| Feature         | Usage in Qredo                                                                                                                   | Right/Benefit                                              | Stakeholders        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|---------------------|
| Staking         | Tokens are locked to secure the protocol and enable the federated PoS consensus model. In turn, rewards are distributed. | Receive a share of rewards and fees                        | Stakers, Validators |
| Work            | Validators are elected by the community to run the protocol and receive rewards                                          | Receive a share of rewards and fees & execute requests     | Validators          |
| Governance      | Tokens are used to vote on protocol proposals (QPIPs).<br>More tokens = more voting power                                        | Participate in the decision-making process of the protocol | Token holders       |
| Payment         | Tokens are used to pay protocol fees and/or service fees                                                                         | Use Qredo services and make protocol requests              | Clients             |
| Reward/Penalty  | Airdrops and quests from a dedicated fund are used to incentivize participation and adoption of product features                 | Access Qredo services at a discount                        | All                 |
| Funding         | Tokens are awarded to key contributors (either for building the protocol and service and/or providing early funding)             | Share the success/value of the network                     | Developers          |

## 3. Fee Models

This section is based on [dedicated report](/v5r6y8a_TE6NtouVHmPnmA).

Qredo is implementing two fees:

- Protocol fees - fees that need to be paid when submitting requests to the Qredo network. The goal is to avoid spamming attacks on the network and to support Validator operations.
- Service fees - fees computed in a pay-as-you-go model based on the total volume transacted in billable operations. The goal is to have a fairer distribution of network costs by requiring clients moving a higher volumes through Qredo to pay more.

Both fee will leverage and the QRDO token in different ways, which will be detail next.

### Protocol Fees

To collect protocol fees, Qredo has three main classes of transactions:

- Self-funded transactions - Transactions initiated by protocol users with a Qredo Layer 2 (QL2) wallet (i.e., the protocol is capable of charging the protocol fees). 
- Protocol-funded transactions - Transactions initiated by protocol users without a QL2 wallet (i.e., the protocol is not capable of charging the protocol fees).
- Control transactions - Internal transactions that the Qredo network must execute to maintain operations. These transactions are not generated by protocol users. Instead, they are initiated by the protocol itself or by the development team when deploying protocol changes. Examples include fee collection, messaging, network upgrades, etc.

The fee collection mechanism for self-funded transactions is very simple - protocol users must have QRDO in their QL2 wallet before making a transaction request. When the transaction is executed, the protocol takes the protocol fees from the user’s wallet and burns them.

On the other hand, protocol-funded transactions and control transactions cannot be directly charged to a user’s wallet. Instead, the protocol fees for these transactions need to be covered by an Ecosystem Fund that is fully controlled by the protocol. 

Everytime a transactions is executed within Qredo, a **fixed protocol fee is collected and burned by the protocol**. This burning model garantees that Validators also pay fees for submitting their own transactions while creating a token supply pressure that benefits all network participants that hold QRDO.

The fixed fee value by transaction will be defined in the second phase of this project by trying to balance the following two goals:

- Have a sufficiently high fee to avoid protect against spamming attacks
- Have a sufficiently low fee to avoid over-burning and make transactions unaffordable for most users.

### Service Fees

Service fees are already collected by Qredo, based on the total USD volume of billable transactions (the pay-as-you-go model). Fees can be paid in either QRDO or USD. However, a large majority of these fees is currently paid in USD. In addition, in both cases, the total fee is aways denominated in USD. 

Service Fees are a singificant portion of the vlaue being generated in Qredo's economy and, thus, we need to introduce a mechanism to transter this value into the native token, QRDO.

However, having the possibility to pay service fees in USD is an important product feature since it increases the platform’s usability. This is especially important for institutional clients as it simplifies their internal accounting and paperwork.

Another key feature of Qredo’s business is that some institutional clients do not pay directly with the decentralized protocol. Instead, They sign a traditional B2B agreement with Qredo’s LLC and the Qredo team is responsible for billing and collecting the fees. In this situation, fees are not collected algorithmically by the protocol and thus Qredo LLC must do an extra step to transfer the value being generated there into the Qredo network.

Therefore, Qredo clients will have two options when paying service fees - they either pay service fees in QRDO or fiat. If they pay in QRDO, these fees are directly pooled into the Ecosystem Fund, which will be later distributed among network participants (i.e. Validators, Stakers, Developers, etc.). If they pay in fiat, these fees will be used to buy QRDO, and only then will they be deposited in the Ecosystem Fund.

Since QRDO payments involve less work to the protocol, fees paid in QRDO are entitled to a discount. The discount will depend on the estimated costs of fiat-to-QRDO conversion and will be a key parameter of the service fee model.

Finally, for the clients billed by the LLC, we need to consider another key model parameter - the tipping rate. The tipping rate is the percentage of fees paid by these clients to the LCC that will be “tipped” to the network. As Qredo’s LLC is responsible for business development, client relations, and payment collection for these clients, they cannot pay the entirety of the fees back to the network. On the other hand, the clients are using the decentralized protocol and thus some value must be transferred. This split is encoded by the tipping rate.

**The tipping rate and the QRDO discount rate will be defined in the second phase of this project.**

## 4. Staking Model

This section is based on [dedicated report](/Xh_biTXNS8mpG5M_rMfKbg).

The Qredo network is on a trajectory towards decentralization, with an aim to transition from a fully centralized system to a **Federated Proof-of-Stake** (FPoS) consensus mechanism and ultimately to the even more decentralized **Delegated Proof-of-Stake** (DPoS) mechanism. These mechanisms offer economic incentives for beneficial behavior and deter malicious actions, thereby aligning network security with the vested interests of token holders and promoting energy efficiency.

The first step is to move into a FPoS mechanism. In this setting, a group of **pre-selected, possibly third-party nodes**, called the Federated Nodes, participate in the consensus process. The system operates on the **principle of trust and reputation**. The network designates nodes as Federated Nodes based on their reputation or trustworthiness within the network. These nodes do not need to lock or *stake* tokens to participate in the block creation process, but interested token holders can stake some QRDO tokens to be part of the *staking rewards.*

Over time, the Qredo network aims to move to Delegated Proof-of-Stake, which is a consensus mechanism that seeks to streamline the decision-making process within a blockchain by minimizing the number of nodes involved in such a process. Instead of every network participant being involved in the process, **DPoS elects a fixed number of delegates** (or witnesses) to create blocks and confirm transactions, with the rest of the **network participating in a democratic voting process to select these delegates**. Effectively, this would mean opening the network so that anyone can become a Validator and making it a much more decentralised environment.

Independently of the consensus system used, the design of the Staking Mechanism involves defined three crucial components:

- **Source of rewards:** The origin of the tokens that serve as rewards.
- **Reward distribution:** The rules and methods for distributing rewards among the different participants.
- **Locking and Slashing Mechanism:** The mechanisms for ensuring network security and penalizing malicious or misbehaving actors in the system.

The next diagram provides an overview of how these components come together within Qredo's Staking.


<div style="text-align:center">
<img width="550" src="https://hackmd.io/_uploads/ry9iBK4Uh.png">
<br/>
<br/>
</div>

In Qredo, rewards come from two sources: 

- The **Validator Rewards Fund** will receive an initial allocation of QRDO and is aimed at kickstarting the Staking and Validation function in Qredo.
- The **Ecosystem Fund** will be made of the service fees collected by Qredo's protocol (as discussed in the previous section). In the long run, this component will be the main source of Validator rewards.


All tokens stored in these two funds will be locked (and thus not part of the circulating supply). The protocol will manage the number of tokens available for distribution through two key functions that will be designed in the second phase of this project:

- The **vesting rate function**, which controls the number of vested tokens in the Validator Reward Fund available for distribution
- The **release rate function**, which controls the number of tokens available for distribution from the Ecosystem Fund.


<div style="text-align:center">
<img width="500" src="https://hackmd.io/_uploads/S1EnVyI83.png">
<br/>
<br/>
</div>

Both functions will use metrics such as network growth and Total Value Locked to gauge network status and unlock enough rewards to support Validator operations while controlling token supply. They will also guarantee that all participants are aligned with the long-term success of the network by, for instance, unlocking bigger shares of rewards a the number of Validators and Stakers in the network increases.

In each epoch, the tokens vested from the Validator Reward Fund and unlocked from the Ecosystem Fund will need to be divided among the parties that participated in the consensus system. First, this pool of tokens is split between Validators and Stakers. Then, for each group, the tokens are further split among individual contributors based on factors such as total staked amount, reputation, active participation, etc. The exact distribution is controlled by two score functions, namely the **validator score function** and the **stakes score function**, which will be defined in phase 2 of this project.

<div style="text-align:center">
<img width="350" src="https://hackmd.io/_uploads/S1uLNyLIn.png">
<br/>
<br/>
</div>


Finally, we have the locking and slashing mechanisms. **Locking** is required by stakers in FPoS and by validators and stakers in DPoS. In the latter, validators stake tokens as collateral against dishonest behaviors, which, when detected, results in **slashing**—a penalty in the form of collateral loss. The amount slashed is a proportion of the validator's total staked amount. In both cases, stakers stake these tokens in exchange of being part of the staking rewards program.  The specifics of these mechanisms, such as minimum staking amount, duration, and token unlocking mechanisms, will also be decided in the project's second phase.

We summarize the design space for the parameters under consideration in [this table](/Xh_biTXNS8mpG5M_rMfKbg#Parameter-overview), and discuss general guidelines on the choice of parameters  [in this section](/Xh_biTXNS8mpG5M_rMfKbg#Towards-a-choice-of-parameters) of the original report. 


## 5. Final remarks

Qredo offers a highly technical product with a rather complex economic model. In this intermediate report we investigated each of the main components of the Qredo economy. It serves the purpose of contextualising the current state of the network and its future plans, as well as laying the foundations for what will be the focus of the seocnd phase of the collaboration. . Furthermore, we identified several potential mechanisms (for e.g., fee collecting and staking) with several possible parameters r variations. 

In the second phase of this project, we will present data-driven, fine-tuned specific recomendations on these mechanisms and their respective parameters. Ultimately, these specifications will result in an updated economic model for Qredo which adapts to the network's specific needs, state, and KPIs. 
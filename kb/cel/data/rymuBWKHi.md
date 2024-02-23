---
title: Project Bacalhau review
tags: CoD
---

# Project Bacalhau: Compute over Data Idea Review

#### Alex Terrazas, February 2022

## Problem Statement

This analysis is related to our meeting with David Aronchick.  David announced a high-priority initiative to use data stored on the Filecoin network in a compute pipeline.  The project is known as Project Bacalhau.  [https://github.com/filecoin-project/bacalhau/](https://github.com/filecoin-project/bacalhau/). Bacalhau is the Portuguese word for cod.  Compute over data is often called CoD.  This initiative is an important part of the CryptoEconLab’s 2022 plan.  

The initial target for Project Bacalhau is existing storage providers with data on nodes.   Existing storage providers will take the least amount of effort to ramp up.  The vision is for the storage provider to simply attach a Bacalhau wallet to their node and begin accepting compute contracts. 

Bacalhau cannot launch to the public without a well-thought out economic model. A key question surrounds the minting of CoD tokens or coins.  Other economic considerations includes value flow through the proposed network, validation, collateral, slashing policy, and liquidity.  

### Native tokens

When creating a new cryptocurrency, one can choose to make a coin or a token.  Coins have their own native blockchain and typically have a specific utility over the whole network, like paying for transaction fees, staking or taking part in governance.  Tokens are built on pre-existing blockchains and have many similarities to coins; however, tokens mainly have utility in their own projects.  Unlike **coins,** which are generally accepted for various services on the Blockchain, **tokens** are much more restrictive in their uses and specific tokens are only accepted for specific services.  For example, ERC-20 tokens issued on the Ethereum blockchain are each part of a specific project with their own use cases.  

Bridging tokens between Filecoin and CoD tokens is one option for providing liquidity to the CoD network.  In this scenario, the client deposits Fil on the Filecoin network and then transfers FIL to CoD tokens at an exchange rate.  The client then offers a compute contract (along with CIDs) to the network.  A Thread Provider agrees to the contact and runs the threads.  After the threads are completed, the results are delivered to the client according to the contact and the Thread Provider is paid.  A gas fee is charged for the compute and the transactions back and forth.      

An alternative is using FIL as the token.  This makes sense because the initial target is Storage Providers who are already accustomed to FIL.  No bridging is necessary.  Because the Thread Providers are already Storage Providers, it is possible to use their existing pledge as collateral against slashing.  Alternatively, an additional pledge can be required.     

Some tokens like Tether — a stablecoin backed by commercial paper, which is the promise to repay short term debt by companies — make use of [more than one](https://tether.to/tether-usdt-integration-live-on-omg-network/)
 blockchain to gain speed and reduce user costs. So, unlike coins, tokens can choose to not be ‘bound’ to a single blockchain, gaining flexibility and becoming easier to trade.

**Example Bacalhau Usecase: Big Geospatial Data**  

Landsat 9 makes a complete image of Earth every 16 days.  These data are already stored on the Filecoin network.  The number of storage providers and the number of copies of the data would be interesting to know.   Earth imagery requires a number of standard processing steps (e.g., calculating vegetation index, cloud removal, image stitching, image timepoint deltas) before it is useful for most applications.  Bacalhau could make these computations right where the data sit; thus requiring no data ingress.  This fact is a serious competitive edge for Bacalhau over other data set providers and traditional map/reduce-style platforms.  The other ecosystem players are not clear about how raw data enter the network.  

The geospatial example above is a deterministic example.  Most machine learning use cases are probabilistic and, therefore, challenging to validate.  The ultimate vision of Bacalhau is to support both deterministic and probabilistic applications.   The technical challenge of how to validate probabilistic use cases remains.  Project Bacalhau proposes a unique approach (see below under **Trace-based Validation**)

**Actors**

There are typically four actors in CoD systems: (1) Clients who wish to have compute on a public or private dataset (2) Compute Providers who receive a fee to process data; (3) Storage Providers who have public or private data on their storage devices.  Note: this is largely confined to Bacalhau except for TrueBit, which accesses data through Ethereum Storm; although, Ethereum Storm does not have nearly the storage assets of Filecoin; and (4) Validators, who confirm the computations for the system.  

## Overview of Ecosystem

As a starting point, the CryptoEconLab surveyed the existing CoD ecosystem with respect to their economic models.  The following companies are considered: (1) Golem, (2) Truebit, (3) DFinity, and (4) Fluence.  Some information is provided about Iagon, near the end of this document.  This report explores those companies in terms of security, tokenomics, and actors.  Fluency, while a web3 p2p player does not have tokens or an crypto economic layer.  Before presenting the specifics of these companies, some general observations are presented. 

### 1. CoD appears to work mainly on smart contracts

The four ecosystem companies reviewed here all work on smart contracts between a Client and the Compute Provider.  A relevant security question is whether Bacalhau will use Turing-Complete contacts or Non-Turing-Complete contacts.  Turing-Complete smart contracts support various codebases and allow building complex structures with any set of computable functions; however, they are more vulnerable to attack.  Non-Turing-Complete programming languages are more specialized but they do not support vulnerabilities such looping, recursion, or other processes that are not guaranteed to terminate on their own.  

### 2. Validation Layer

A key challenge is designing a financial incentive system where participants report honestly about their computations and financial commitments.  Detection of cheating is one approach; however, that can be difficult with machine learning algorithms that are not deterministic.  If suspect transactions are relatively rare, Validators will not be rewarded often.  

Another approach in use is a reputation layer. TrueBit developed an interesting approach they call game-based verification. In fact Golem uses TrueBit game-based verification and reputation. Bacalhau’s proposal optionally includes a unique verification method (described below). 

**Trace based reputation layer** - 

Project Bacalhau is proposing a unique reputation layer that utilizes traces of the compute to make inferences about cheating. Because machine learning is often probabilistic, verification can be difficult.  Any compute task will have a profile for its memory and CPU utilization that can be compared against the trace of the provider’s run.  To enable this capability, a method for inspecting a running process (VM, container or WASM) is needed along with a way to determine if a provider’s process matches the signature.  

Determining a fingerprint would be extremely hard to synthesize without actually running the process.  The initial execution trace Bacalhau will use CPU and memory usage over time, however many other trace variables can be used, such as the entropy profile of the output.  It may also be possible to monitor compute at the thread level; however, running a smaller number of threads may enable a malicious compute provider to generate fake threads.  

## [Golem](https://www.golem.network/)

[https://www.golem.network/](https://www.golem.network/)

Golem is a network for peer-to-peer transactions for renting idle digital resources including spare computing power. It works by connecting Requestors (buyers) and Providers (sellers).  Golem splits the request into smaller parts of the initial task and rents the computing power from multiple users on the network.  The company does not provide detail about how the splitting of the task occurs.  It appears that the requestors fill out a template. Golem also places the control over the P2P market into users’ hands, connecting Requestors and Providers based on the task template. Providers get paid directly for their services.  

**Context**

The whitepaper came out in [Nov 2016](https://assets.website-files.com/60005e3965a10f31d245af87/60352707e6dd742743c75764_Golemwhitepaper.pdf). Reportedly a major overhaul in 2020, but no follow-up whitepaper. The Golem network has an ERC-20 utility token, [GLM](https://coinmarketcap.com/currencies/golem-network-tokens/), which is currently #[116 by market cap](https://coinmarketcap.com/currencies/golem-network-tokens/). While the Golem network is [relatively small](https://stats.golem.network/) with around 12k cores (about the size of a large university cluster) and 37 providers, the [repos](https://github.com/ThinkR-open/golem/issues) and [kanban](https://trello.com/b/YL1qZ2pZ/brass-golem-progress-board) are quite active. A notable point is that individuals can participate as compute providers with a low barrier to entry — it is possible to sell compute using a laptop (although not necessarily economically feasible). 

**Applications**

Golem supports the message passing interface (MPI) protocol for parallel communication and is therefore strongly positioned for use cases in scientific computing that rely on **massive parallelizability with shared memory,** e.g. computational chemistry with gromacs. The projects also highlights GPU-heavy computation. Examples applications include **graphical rendering** with Blender and **deep learning**. An important selling point is the claim of **no specific size or time limits on computation**.

**Economics**

GLM is the utility token for the Golem economy that allows providers to earn GLM for providing compute paid for by users.  Golem uses Polygon MATIC for gas computations.  The requestor agent and compute provider interaction is via a market in the GLM token.  The market relies on reputation.  Compute cost is currently 0.025GLM/cpuhr or $0.01/cpuhr.

**Additional reading**

- [Verification by redundancy scheme on gWASM](https://blog.golemproject.net/gwasm-verification/)
- [Pay as You Use](https://blog.golemproject.net/pay-as-you-use-golem-a-brief-but-effective-primer/)
- [Golem Payments](https://handbook.golem.network/payments/payments-explained)

### TrueBit

[https://people.cs.uchicago.edu/~teutsch/papers/truebit.pdf](https://people.cs.uchicago.edu/~teutsch/papers/truebit.pdf)

TrueBit consists of a **financial incentive layer** and a **dispute resolution layer.**  The dispute resolution layer implements a “verification game.”  In addition to secure outsourced computation, (1) immediate applications include decentralized mining pools in an Ethereum smart contract, (2) a native cryptocurrency with scalable transaction throughput, and (3) a trustless means for transferring currency between disjoint cryptocurrency systems.

TrueBit uses trustless smart contracts to securely perform the computation task.  Presently every Ethereum miner has to independently replicate each smart contract action in its entirety, whereas TrueBit outsources most computation work to a handful of entities. TrueBit reduces the number of redundant network node computations used in traditional Ethereum smart contracts. 

TrueBit takes a market approach to compute—anyone can post a computational task and anyone else can receive a reward for completing it.  The system’s incentive structure guarantees correctness of returned solutions.  

TrueBit enables trustless smart contracts, in theory, to securely perform any computational task. Moreover, TrueBit vastly reduces the number of redundant network node computations used in traditional Ethereum smart contracts.  Presently every Ethereum miner has to independently replicate each smart contract action in its entirety, whereas TrueBit outsources most computation work to a handful of entities. 

**Scalable “on-chain” storage.**

TrueBit makes data accessible to Ethereum smart contracts with Ethereum Swarm, a platform for incentivized, peer-to-peer storage.  TrueBit itself is an Ethereum smart contract which allows users to call TrueBit contracts for trusted, computationally-intensive applications.  

**Verification**

At the heart of TrueBit’s protocol is a verification game, which decides whether or not a contested computational task was performed correctly.  The verification game is a bug bounty that increases the likelihood bug detection.  Compute providers are randomly selected *and paid* for submiting incorrect solutions.  These deliberate errors are termed *forced errors*.  The provider is paid for making forced errors.  

TrueBit avoids deep probabilistically checkable proofs (PCPs), succinct non-interactive arguments of knowedge (SNARKs), and exotic cryptographic assumptions (e.g. those used in zkSNARKs).  Instead, hash functions and digital signatures that are already part of the underlying blockchain are used.w

### Dfinity

[https://dfinity.org](https://dfinity.org/)

Dfinity is a blockchain with a unique, highly scalable architecture.  As a blockchain, it has a shared global consensus across the whole network.  The computation in Dfinity occurs on chain.  The protocol is called the Internet Computer Protocol (ICP).   

Dfinity uses a variation of PoS called Threshold Relay Nodes produce a random number that is used to select the next group of nodes that participate in consensus.  An important part of DFINITY’s ICP is it’s ChainKey technology (described below), which allows transactions to be finalized quickly.

The ICP enables Wasm containers—called canisters—to run under Bitcoin smart contracts.  The Chain Key cryptography gives each canister its own Bitcoin public key, thus directly integating the blockchain with the Bitcoin network. Canisters are able to hold, send and receive their own Bitcoin but can only be changed with messages on the main blockchain.  The execution of canister code is deterministic, therefore, the canister’s state can be audited.  The canister is a full smart contract.  Unlike a smart contract, canisters have processing capabilities that enable them to run applications at Internet scale.  

**Consensus Mechanism**

The DFINITY consensus mechanism consists of four layers: (1) **Identity Layer.**  All participants are registered clients with permanent pseudonymous identities.  Registration requires a stake deposit with a lock-up period. Collateral can slashed; (2) **Random Beacon Layer.**  The overall purpose of the Random Beacon Layer is to provide the source of randomness for the consensus layer.  (3) **Blockchain Layer.**  This layer builds a blockchain from the verified transactions;  and, (4) **Notary Layer,** provides fast finality guarantees to clients in the network.

DFINITY uses consensus to agree on the order of processing of the messages across all the nodes because the nodes aren’t guaranteed to receive messages in the same order.  Messages are placed in blocks and then grouped together on the blockchain.  The messages are validated before they are transferred to the subnet.  

**ChainKey Technology**

DFINITY’s chainkey technology is a 48-byte public chain key that allows DFINITY’s Internet Computer to finalize transactions. The mechanism renders old blocks unnecessary and enables the ICP to operate quickly by finalizing the transactions needed to update smart contract states.  These transactions are finalized within 1 to 2 seconds. Chain key technology is also responsible for the communication between the subnets, canisters, and the Network Nervous System (NNS)) and the network's consensus mechanism.

Chain key technology operates by splitting up the execution of smart contract functions into query calls and update calls — a “divide and conquer” approach that enhances the overall efficiency and speed of the ICP network.

**Canisters**

A canister has the following properties: (1) it has private state that can only be modified by the canister itself, (2) it has single thread execution so it does not need lock-based synchronization.  The canister can communicate with other canisters in a asynchronous fashion; (3) it can spawn new canisters and (4) canisters have bidirectional communications—so they can send requests and receive responses.

Each canister is replicated over all nodes in the subnet.  Browsers and API calls can operate directly on canisters.  A canister cannot modify its balance of tokens.  Canisters can reference secure randomness through the Random Beacon Layer.  DApp users can interact with canisters without holding tokens.  

Canisters do not crash—instead they roll back to the state before the crash.  A canister controlling another canister is a key capability of the ICP.  

**Cycles**

All canisters consume resources (e.g., CPU cycles for execution, bandwidth for routing messages, and storage for persisted data). These resources are paid for using a unit of cost called **cycles**. Cycles are obtained by converting ICP tokens and are stored by each canister in a local balance.

By setting limits on how many cycles a canister can consume, the platform can prevent malicious code from completely taking over resources.  Cycles are intended to reflect the real cost of operations in a stable or deflationary way. The cost of program execution remains the same or decreases with operational efficiency. The conversion rate of ICP to cycles is adjusted based on the current ICP market value.

**Tokens**

Tokens in Dfinity reflect the value of the blockchain and can fluctuate. To prevent the token value from affecting the number of messages a canister can process, tokens are not used to pay for resources directly.  Instead, tokens are used to reward node providers for providing compute capacity—whether it is used or not.  

Tokens can be exchanged between token holders or locked up to secure voting rights as part of the governance system.

Node providers receive compensation for both active and spare nodes so that the Internet Computer blockchain has capacity to handle both normal traffic and workload spikes.  The nodes run the ICP an advanced cryptographic fault-tolerant protocol which ensures that smart contracts running on the blockchain cannot be tampered with or stopped.

**Subnets**

The Internet Computer is composed of individual subnet blockchains running in parallel and connected using chain key cryptography. This means that canisters running on a subnet can seamlessly call canisters hosted in any other subnet of the Internet Computer blockchain.

**Governance**

Another feature of the Internet Computer is that it runs under the control of a decentralized permissionless governance system, (Network Nervous System**;** NNS), which runs completely on-chain. The NNS can make decisions on (1) creating new subnet blockchains, (2) updating the node machines, and (3) configuring parameters used in the Internet Computer protocol. 

Anyone can participate in the governance and submit new proposals to the NNS or vote on open proposals. To do so, users have to stake ICP, the Internet Computer utility tokens, and create a **neuron** with the NNS.

**Example Applications**

DFINITY unveiled an open professional profile network dubbed LinkedUp and CanCan, a video sharing social networking service, to demonstrate how popular social media applications could be rebuilt to be decentralized and ownerless. Though DFINITY does not plan to continue developing these applications, it open-sourced the projects’ code for developers who wish to build on them.

## [Fluence](https://doc.fluence.dev/faq/)

[https://doc.fluence.dev/faq/](https://doc.fluence.dev/faq/)

**Status**

Fluence is a newer entry in the compute ecosystem.  It recently [raised](https://twitter.com/fluence_project) $9M Round A funding in February 2022.  Development recently has been moderatively active on their [github repos](https://github.com/fluencelabs/fluence/graphs/contributors) — current drive to attract dev talent may increase progress in the near future.

**Fluence model**

Fluence is a P2P compute layer. It provides an open Web3 protocol, framework and tooling to develop and host applications, interfaces and backends on permissionless peer-to-peer networks. The Web3 stack enables 

(1) programmable network requests 

(2) distributed applications from composition without centralization

(3) extensibility through adapter/wrapper services

(4) efficiencies and improved time to market arising from the reuse of deployed services and significantly reduced devops requirements.

**Tech**

Fluence is a P2P compute layer, **not a blockchain/incentive layer**.  It aims to provide P2P compute nodes, targeting applications in web3, storage, and blockchain domains. In this it supports IPFS. 

The types of computation and environment it uses are announceable/discoverable. 

Fluence uses the term [Particle](https://doc.fluence.dev/docs/concepts) to refer to it secure distributed state medium.  The distributed state medium includes replication data structures containing (1) application data, (2) workflow scripts and (3) some metadata that traverse programmatically specified routes in a highly secure manner. The particles can be thought to hop from distributed compute service to distributed compute service across the peer-to-peer network as specified by the application workflow updating along the way.  

The Services on Fluence behave like microservices: they are created on nodes and served by the VM and can *only* be called by the VM.  Services are logical constructs instantiated from Wasm modules that contain some business logic and configuration data.  Services can accept incoming calls but can't initiate an outgoing request without being called.   

**Applications** 

The applications envisaged are non-specific blockchain infrastructure. This includes computation on decentralized data related to exchange, DAO tooling, and wallets.  

**Economics**

Fluence is substantially different from the other projects and the Bacalhau model. Fluence has **no token**. The project economic strategy relies on web3 microservice compute payments becoming increasing wide-spread, but there is no clear revenue model now. It appears to be a case of build now, capture market, figure out revenue streams later. To quote from their documentation: “Earn from usage — coming in phase 3”.

## **Iagon**

[https://www.iagon.com/Features](https://www.iagon.com/Features) 

Iagon’s goal is a Global Supercomputer, powered by AI & Blockchain Technology. This is accomplished by integration across all smart devices. The AI connects users to services and decentralized applications. The company aims to generate revenue by sharing individual’s processing power and storage.  Clients create smart contracts with tools that not require coding.  

**Native Token**

IAG is the native token. It is a capped-supply token with a circulating supply of 1 billion IAG. 1 billion IAG tokens were already minted as ERC-20 tokens on Ethereum. Later, an equal supply will be minted on Cardano and locked in the bridge smart contract.  The smart contract will allow users to move IAG tokens between Ethereum and Cardano. 

**Cross Chain Bridging**

See the [Cross-Chain Bridge](https://whitepaper.iagon.com/detailed-architecture/cross-chain-bridge) section for more details about how the bridge will work.

When storage providers commit their resources, the commitment is handled by Adagio.  The rewards are locked for at least 1 month.  During the lock-up period, Adagio generates yield. This yield is distributed among storage providers, IAG stakers, and Iagon.

IAG serves the following key functions in the Iagon protocol (1) IAG holders can stake their tokens in the company's ADA staking pool to earn additional rewards; (2)  The IAG token represents a 'share' in the Iagon ecosystem, providing holders with a portion of the revenue generated through the storage marketplace. The amount earned will be determined by the number of IAG tokens staked and the trading volume in the storage exchange. (3)  A portion of the company's IAG tokens is paid to well-performing storage providers; and (4) A portion of both the transaction fees and the yield provided by the locked rewards go back to ”the house”  in order to fund further development of the network, to cover operational costs, and buy back IAG tokens in order to refill he Adagio reward pool for stakers and resource providers.

### Vast

[https://vast.ai/](https://vast.ai/) 

GPU rental

### Raven

[https://www.ravenprotocol.com/about](https://www.ravenprotocol.com/about)

## Economic Story

To understand CoD economics, we can think about the roles of the different actors involved — clients, miners, developers, token holders, and ecosystem partners — and map out how value flows between each player. Some of these actors have strong overlap with the current Filecoin ecosystem, others don’t necessarily. The details on this depend on how we design the system, and a fundamental question that needs to be addressed is whether the project has its own utility token. 

Issuing a CoD token has benefits and disadvantages which are set out below.

**Reasoning to support** new utility token issuance include:

- Provides a focal point for interest on the project. If people believe the project will grow, the token aquires investment as well as utility status. This *is* secondary to central goal of the project, but can raise the profile, which feedbacks into supporting utility growth of the project.
- Insulates established FIL ecosystem from new-project risk.
- Compute and storage are distinct modular entities, in computing in general. Unless there’s a good reason otherwise this seems like a plausible economic default.
- In terms of the economic actors involved, the clients storage are likely often different compute ones, as are the miners.
- New token gives greater flexibility for compute-specific incentives that may be different to the ones for storage mining. Discussion needed.

**Reasons against** include:

- From user perspective:
    - *Cognitive load* on users of having to manage additional tokens.
    - More tokens, means more interactions, means more exchange fees.
    - New system with low volume, potential for liquidity issues e.g. slippage, compared to FIL.
    - Probably further exposure to counterparty risk — *more failure points* for users.
- Difficult tokenomic balance. A new token might be perfectly functional in utility terms, but if pools are paying 10%, people will be adverse to holding the token for any length of time (and by extension interacting with the system), unless supply is sufficiently deflationary, through either speculative demand, which isn’t what we want to rely on, or mechanistically through burning or otherwise.

 **Summary of Findings**

1. **Issuing of a new token.**  The initial goals of Bacalhau could be achieved without launching a new coin because the target Compute Providers are already on the Filecoin network as Storage Providers.  It may make sense to launch a token in future version; however, the least amount of friction will result from using Filecoin.
2. **Choice of Smart Contract.**  Turing-complete smart contracts allow for flexibility but introduce some security risks; however, non-Turing-complete smart contracts are not likely to enable the type of compute required.  
3. **Validation Layer.**  The TrueBit approach may be a useful model for validation.  It is possible to contract directly with TrueBit to use the model (as Golem has done) or to create a similar approach.  If Bacalhau’s Trace Validation approach can be developed quickly, it may be able to run in parallel or in place of the game-based verification model.
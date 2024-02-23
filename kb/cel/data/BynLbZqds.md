---
title: Chain Rollup Models
tags: Econ models
---

# Review of Chain Rollup Models

#### Alex Terrazas, March 2022

The CEL was asked to examine the economic systems for Optimism, Arbitrum, zkSync, and Polygon.   Additional solutions described here include Plian (formerly PChain), Boba, StarkNet, and Dfinty.

***Note:** Polygon [https://polygon.technology/solutions/polygon-edge](https://polygon.technology/solutions/polygon-edge) is a whole family of solutions including Miden (a STARK-based zk rollup), Edge (a framework for building private and public Etherium-compatible blockchain networks), Zero (a scalable Ethereum-compatible zk rollup), Nightfall (optimistic roll ups combined with zk rollups), Avail (a scalable data availability-focused blockchain for standalone chains and off-chain scaling solutions) and Hermez (an open source zk rollup for token transfers on Etherium).  Avail, Miden, and Zero are still under development.*

## General

### **Side chains vs Layer 2 Solutions**

A side chain is a blockchain with its **own consensus mechanism** (usually compatible with Ethereum). In contrast, a Layer 2 solution does not have its own consensus mechanism but instead relies on Ethereum security.   Roll ups are an example of a Layer 2 solution.  Polygon (MATIC) and DFinity are examples of true side chains. 

Side chains have two main advantages. (1) they are permanent. Once a side chain is built, it is maintained and can be used by anyone off the main chain and (2) they allow interaction between different cryptocurrencies. However, miners are needed to ensure the safety of the side chains. This makes the formation of new sidechains costly. Sizable investments have to be made before any new sidechain can be created. Another downside to side chains is the requirement of a federation. The extra layer formed by the federation could prove to be a weak point for attackers.

The two-way pegs enable assets to be interchanged between the parent Blockchain and the side chain; for instance, using Bitcoin as the underlying asset for a separate Blockchain.
The rate at which these assets are exchanged between the main Blockchain and the childchain is usually predetermined.  Side chains require their own miners. Miners can be given incentives through merged mining, where two different cryptocurrencies with the same algorithm are mined at the same time.

### Typical Costs of Scaling Solutions

Scaling solutions typically have three types of costs: L1 data publication fee, L2 cost of operations,  and L2 congestion costs. 

A system receives revenue in two forms: transaction value and issuance.

- **User fee** = L1 data publication fee + L2 operator fee + L2 congestion fee
- **Operator cost** = L2 operator cost + L1 data publication cost
- **Operator revenue =** User fees + MEV
- **Operator profit = Operator revenue - Operator cost** = L2 congestion fee + MEV

No matter how the side chain itself is secured, **when it’s used as a scaling solution, security of the assets always depends on the goodwill of the majority of the bridge validators**. If the majority is compromised, they can irreversibly steal all of the assets. And since most bridges operate in a **delegated PoS** model with low-latency consensus requirement, the majority of the stake is usually controlled by only a handful of validator servers physically located in the same data center. 

## Permissionless Protocol Experimentation

Although not widely discussed, the ability to create side chains allows developers to experiment with protocol changes without permissions; thereby, spawning innovation on the base chain.  New features can be tested on side chains and moved onto the main chain only when proven to work in practice.

## Fragmentation and chain interoperability

Scaling solutions are rarely interoperable—they provide scaling within the boundaries of their own platform but they do not allow subchain-to-subchain transactions.  This fragmentation can result in scarce liquidity because the capital of users is divided between the subchains.  Scaling solutions benefit the main chain, but liquidity off-ramping from the mainnet might counter these benefits.

Cross-chain token transfer involves several challenges such as (i) how to issue tokens on the chains and ways to disable tokens when they are leaving the blockchain, (ii) rebalancing of tokens across blockchain to maintain liquidity, 

As previously noted, both Arbitrum and Optimism use bridges to interact with other blockchains. However, where Arbitrum employs a universal and permissionless bridge for all tokens, Optimism deploys dedicated bridges when the market demands are ripe.

DFinity’s Internet Computer is a blockchain built by the Dfinity Foundation to help facilitate a decentralized layer of web infrastructure. DFinity uses a cross-blockchain bridge to connect the Ethereum network with Dfinity’s Internet Computer.  The bridge allows ERC-20 to exist natively on Dfinity’s network.  The bridge (Terabithia) enables cross-chain contract communication, asset mirroring and transfers across different blockchains. It is built on Starkware, a forked version of Ethereum scaling tool and will enable contracts on both blockchains to communicate.  Anyone can mirror and use any Ethereum asset on the Internet Computer and vice versa.

Polygon PoS is a layer 2 scaling solution that achieves high transaction speeds and cost savings by utilizing side-chains for transaction processing. At the same time, POS ensures asset security using the robust Plasma bridging framework and a decentralized network of Proof-of-Stake (PoS) validators.  Plasma is a framework of secondary chains that will communicate and interact as sparingly as possible with the main chain.

## Optimistic vs. ZK Rollups

There are two fundamental forms of rollups: optimistic and zero knowledge (ZK).  The primary difference between these two approaches is that optimistic rollups depend on fraud proofs during a period of time called a  “challenge window” while zk Rollups depend on validation proofs and are immediate.  Validation proofs are cryptographic proofs while fraud proofs are submitted by human watchers who stake a claim on the fraud proof and risk losing their stake if the fraud proof doesn’t hold up.  During the challenge window (usually about seven days) of optimistic rollups, transactions sit in a pending state; offending transactions can be corrected in the event a fraud proof occurs. If the challenge window expires without a fraud proof, the main chain is updated.  Validation proofs for ZK rollups run on every batch of L2 transactions but optimistic rollup fraud proofs run only if a transaction or chain state is disputed during the challenge window.  Optimistic rollups provide near-instant transactions and they do not require gas (except for aggregator fees).

### Optimistic Rollup Details

***Optimism vs. Arbitrum***

While Optimism and Arbitrum use optimistic rollups, they differ in the details of those how those rollups work.  ***Note:** Optimism is undergoing substantial changes to its rollup approach.*  

The major difference between Optimism and Arbitrum rollups is that Optimism uses **single-round fraud proofs** running on L1 while Arbitrum uses **interactive multi-round fraud proofs** that run almost entirely on L2.  Arbitrum’s interactive fraud proof winnows disagreements about chain state to a singular point of disagreement using a back-and-forth, recursive splitting method that runs on L2.  

Optimism's single-round fraud proof relies on L1 to execute the entire (disputed) L2 batch of transactions.  This approach results in greater costs because on-chain L1 execution costs more gas.  The L2 fee is itself limited by the L1 gas block,  Moreover, large L2 data (e.g., NFTs) cannot use Optimism because L1 is limited by the size of the blocks that can be validated.  In contrast, a transaction requiring so much gas that it couldn't even fit into an Ethereum block is still possible on Arbitrum.   

***Boba Network***
The Boba network uses Optimism’s (non-interactive) rollup but shrinks the waiting period from seven days to only a few minutes by giving liquidity providers incentivized yield farming opportunities.  Boba uses a swap-based onramp, fast exit, cross-chain bridging and other features to enable this speed; however, note that liquidity providers may not be willing to cover large transactions.  

Boba is not technically a side chain because it does not have its own chain.  Instead, the Boba Network lives *inside* of Ethereum as a series of smart contracts that are capable of executing Ethereum transactions. Whereas side chains rely on their own consensus mechanisms for security, Boba relies on the security of Ethereum itself.

***Polygon Nightfall***

Nightfall (currently running in testate) is designed to lower the transaction cost of ERC20, ERC721 and ERC1155 token private transfers. Interestingly, Nightfall uses an optimistic rollup for lowering the costs and the privacy is attained by leveraging zero knowledge proofs.  Validators will roll up transactions into blocks and submit them to the Optimistic contracts. Challengers will submit fraud proofs for any invalid block to the same contracts.  Like Boba, liquidity providers enable instant withdrawal of fungible tokens.

### ZK Rollup Details

zk rollup architecture provides the following guarantees: (1) Validators can never corrupt the state or steal funds; (2) users can always retrieve the funds from the zk rollup smart contract even if validator(s) stop cooperating, because the data is available; and, (3) neither users nor a single trusted third party needs to be online to monitor zk rollup blocks in order to prevent fraud (unlike fraud-proof systems, such as payment channels or optimistic rollups).

***Advantages of ZK Rollups***

ZK rollups offer a number of advantages over optimistic rollups.  Many industry leaders consider ZK rollups to be the preferred solution. Some advantages of ZK rollups include (1) improved security by eliminating reliance on watchers.  ZK rollups replace the game-theoretic economic security with mathematic-based cryptographic security; (2) elimination of the challenge window.  While the waiting period (typically 7 days) can be mitigated by liquidity providers (for a fee), liquidity providers may not be willing to back large transactions.  With ZK rollups, withdrawals are finalized between 15 minutes and 3 hours; and (3) reducing the amount of data to be posted on-chain (no signatures and no transaction parameters).  Specifically, ZK rollups only need to post the final changes to state.

Accounts and balances are represented by separate Merkle trees.  The roots of these two trees ensure no one can fake the data.  The roots are stored in a smart contract on Ethereum which provides a succinct representation of the state of the side chain. All other data is stored off-chain.

***SNARKS and STARKS***

The main players in the ZK rollups (zkSync, Starkness, Polygon Hermez, and Polygon Miden [under development]) utilize different ZK algorithms.  zkSync and Hermez uses Succinct Non-interactive Arguments of Knowledge (SNARKs) while StarkWare and Miden utilize STARKs.  STARKS add transparency validation occurs without the need for generated trust settings.  StarkNet and Miden preserve the security of L1 Ethereum by producing STARK proofs off-chain, and then verifying those proofs on-chain.  STARK validations are 10 times faster to generate than SNARK validations.  

zkSync uses PLONK; see [https://vitalik.ca/general/2019/09/22/plonk.html](https://vitalik.ca/general/2019/09/22/plonk.html)). Therefore, the entire security of the system relies on trust settings (ZK proofs rely on a set of *public parameters* which allow users to construct and verify private transactions. These parameters must be generated in a setup phase called a multiparty computation ceremony). All of the participants would have to be compromised in order to compromise the batch of transactions.

Polygon Hermez is a SNARK rollup that stores the proof and the compressed data from the batch of transfers.  The data availability is on the Ethereum Mainnet.  The zk rollup is open source and has permissionless coordinators.  Hermez has a decentralized auction model with validation rewards.  

### Actors in L2 Solutions

***Optimism***  

The actors in the Optimism chain include (a) the Sequencer that bundles transactions into batches, (b) the Bond Manager which handles ERC20 token deposits from **bonded** Proposers. The bond manager accounts for **gas costs spent by a Verifier** in case of a challenge; (c) a Bridge Contract that implements  L1→L2 and L2→L1 transactions, (d) a standard bridge for "transferring" either ERC-20 tokens or ETH between L1 and Optimism. **To deposit tokens into Optimism, the bridge locks them on L1 and mints equivalent tokens in Optimism.** To withdraw tokens, the bridge burns the Optimism tokens and releases the locked L1 tokens; and (e) predeploys, a set of essential L2 contracts which are deployed and available in the genesis state of the system. These contracts are similar to Ethereum's precompiles.

***Arbitrum***

The primary components of Arbitrum are Aggregators, Validators, Compiler, and the EthBridge. 

In Arbitrum, transactions go through an Aggregator that makes calls to the EthBridge and produces transaction results to the client.  To improve efficiency, Aggregators will usually package together multiple client transactions into a single message to be submitted to the Arbitrum chain.  There is no requirement for the client to use an Aggregator.   There is also no limit on how many Aggregators can exist ****nor on who can be an Aggregator**.**  

Although transaction data is posted on the Ethereum blockchain, transaction execution is moved off-chain and performed by Validators.  Being a Validator is permissionless.  Validators post a stake, which they lose if they’re caught trying to cheat.  Anyone can watch the Arbitrum chain and ensure that it executes correctly.  Even if everyone else is dishonest, one honest person can force the Arbitrum chain to execute correctly and profit from taking the deposits of attempted cheaters.  The chain continues to execute and make progress even while assertions are awaiting confirmation.

EthBridge is a decentralized application deployed on the Ethereum main network. It serves as a connection between the Ethereum main network and Arbitrum.  Validators report back their off-chain processing results in the form of a “roll up block” (assertion), which is posted on the Ethereum chain (optimistically without proof).  Validators check the assertion and prove fraud if it's wrong.  Validators that successfully prove fraud will receive a large reward. A Validator who is caught cheating will lose a large deposit. 

### Launching Sub-chains

Dfinty’s Internet Computer **subnet blockchains** provide physical hardware and resources—like CPU and memory—for performing software operations. Each subnet is a blockchain that consists of some number of decentralized, independently owned and controlled machines—connected peer computers called **nodes**—that run the software components of the Internet Computer protocol.

Key components are: (1) a P2P networking layer that collects and advertises messages from users, from other nodes in its subnet blockchain, and from other subnet blockchains. Messages received by the P2P layer are replicated to all of the nodes in the subnet to ensure the security, reliability, and resiliency; (2) A **consensus** layer that selects and sequences messages received from users and from different subnets to create blockchain blocks that can be notarized and finalized by BFT Consensus forming the evolving blockchain. These finalized blocks are delivered to the message routing layer; (3) A **message routing** layer that routes user- and system-generated messages between subnets, manages the input and output queues for dapps, and schedules messages for execution; and, (4) an **execution environment** that calculates the deterministic computation involved in executing a smart contract that process the messages it receives from the message routing layer.

*In the case of L2 solutions, there is no sub chain.  Instead, the L2 solutions launch new instances of their solution.  There is no consensus mechanism for an L2 solution.*  

***Optimism***

Currently, Optimism runs the sole Sequencer on Optimism.  While this approach is centralized, Optimism aims to decentralize the Sequencer over time, eliminating its role entirely so that anyone can participate in the network as a block producer.  Optimism intends to support multiple concurrent sequencers by adopting a standard BFT consensus protocol, as used by other L1 protocols and side chains like Polygon and Cosmos.

### Native tokens

When creating a new cryptocurrency, one can choose to make a coin or a token.  Coins have their own native blockchain and typically have a specific utility over the whole network, like paying for transaction fees, staking or taking part in governance.  Tokens are built on pre-existing blockchains and have many similarities to coins; however, tokens mainly have utility in their own projects.  For example, ERC-20 tokens issued on the Ethereum blockchain are each part of a specific project with different use cases.

Optimism uses Wrapped ETH (WETH), pegged to ETH in a 1:1 ratio.  WETH allows for cross-chain ERC-20 token compatibility.  Arbitrum has native ETH support; all transaction fees for Arbitrum are paid in ETH.   Polygon Nightfall enables token transfers of ERC20, ERC721 and ERC1155 tokens.  Arbitrum does allow for minting of tokens on L2.

Among the ZK rollup offerings, StarkEx currently supports ETH, ERC-20, ERC-721 tokens, and synthetic assets. Also, it can readily support tokens on other EVM-compatible blockchains.zkSync and Polygon have their own native currencies on the subchain.  

### Gas model and base fee for subchains

***Optimism***

If the Optimism network is not congested, a Uniswap swap transaction is **10x cheaper** on L2 compared to L1.  During network congestion, gas fees increase commensurate with demand according to a strategy similar to EIP-1559. The Sequencer charges a single, small gas fee that covers two costs: (1) a gas fee to pay for the L1 rollup transaction (also called L1 security fee or publishing fee; the fee is split among the L2 transactions) and (2) an L2 Sequencer gas fee for the work performed to execute the transaction.  Another small fee is charged for a swap or liquidity deposit.  Typically the L1 security fee is much higher than the L2 execution fee so it can make sense to wait for low congestion to complete the L1 transaction.  

The L1 fee is based on three factors: (1) the gas price for L1 transactions (when the transaction was processed), (2) the gas used on L1 to publish the transaction. This is based on the transaction length, as well as the byte type (whether it is zero or a different value) for each byte; and (3) the L1 fee scalar, which is at writing 1.5. This value covers the change in L1 gas price between the time the transaction is submitted and when it is published with some profit taken to fund the network.  

Additional fees on Optimism include: (1) **Deposit Gas Fees.** The user must first execute an L1 transaction to [deposit](https://help.uniswap.org/en/articles/5392809-how-to-deposit-tokens-to-optimism) assets to the L2 bridge. The gas fee will be similar to other L1 deposit transactions and (2) **Withdraw Gas Fees.**  Two transactions are required move funds back to L1 (a) an L2 transaction to trigger the withdrawal. This will initiate the fraud proof period.  After 7 days, the funds will be available on; and, (b) wallet fee, an L1 transaction fee (cost ~500k gas) to transfer funds to an L1 wallet.

The OVM does not have blocks, it just maintains an ordered list of transactions. Because of this, there is no notion of a block gas limit; instead, the overall gas consumption is rate limited based on time segments, called epochs. There is a separate gas limit per epoch for sequencer submitted transactions and L1 to L2 transactions. Transactions exceeding the gas limit for an epoch return early.  An operator can post several transactions with varying timestamps in one on-chain batch.

### Arbitrum

Arbitrum uses ArbGas along with L1 fixed cost and calldata cost to compensate the chain’s Validators for their expenses.  Arbitrum fees include (1) L1/L2 bridge fee (costs much more than L1 transfer), (2) L1/L2 fixed cost (inclusion to Layer 1 inbox) (3) calldata (transactions are written on Ethereum) and (4) L2 computation costs,  The ETH data inbox and calldata cost the majority of the fee.

In an Arbitrum Rollup, clients submit transactions by posting messages to the Ethereum chain, either directly or through an aggregator, or on a Sequencer chain. These messages are put into the chain's *inbox.  Note:* Rollups are still susceptible to miners/sequencers being able to choose the order of transactions within blocks they produce.

A single Ethereum block could include within it multiple Arbitrum blocks (if, say, the Arbitrum chain is getting heavy activity); however, an Arbitrum block cannot span across multiple Ethereum blocks. Thus, any given Arbitrum transaction is associated with exactly one Ethereum block and one Arbitrum block.

### zkSync and zkPorter

In **zkSync** the cost of every transaction has two components: (1) the **Off-chain part (storage + prover costs)**: the cost of the state storage and the SNARK (zero-knowledge proof) generation. This part depends on the use of hardware resources and is therefore invariable. Our benchmarks give estimates of ~0.001 USD per transfer.

- **On-chain part (gas costs)**: for every **zkSync** block, the validator must pay Ethereum gas to verify the SNARK, plus additionally ~0.4k gas per transaction to publish the state ∆. The on-chain part is a variable that depends on the current gas price in the Ethereum network. However, this part is orders of magnitude cheaper than the cost of normal ETH/ERC20 transfers.

Transfers in **zkSync** support "gasless meta-transactions": users pay transaction fees in the tokens being transferred—there is no need to convert to ETH.  

1. Users sign transactions and submit them to Validators.
2. Validators accumulate thousands of transactions together into a single block and submit a cryptographic commitment (the root hash) of the new state to the smart contract on mainnet.  The Validator also sends a cryptographic proof (a SNARK) confirming the new state is reflects correct transactions applied to the old state.  In addition to the proof, the state ∆ (a small amount of data for every transaction) is published over the mainchain network as cheap (but limited) call data. This enables anyone to reconstruct the state at any moment.
3. The proof and the state ∆ are verified by the smart contract, thus verifying both the validity of all the transactions included in the block and the block data availability.

**zkPorter**

zkSync 2.0 has an extension called zkPorter that offers constant 1-3 cent transaction fees by putting data offchain. Optimistic rollups fundamentally cannot utilize off-chain data availability because there is no way to verify the validity of every single transaction without public data.  zkPorter puts data availability — essential the transaction data needed to reconstruct state — offchain rather than on Ethereum. Instead of using the main chain for public data, data availability is secured using proof of stake (PoS) by zkSync token stakers. This enables much higher scalability (tens of thousands TPS).  zkPorter uses Ethereum for transaction validity and zkSync token stakers for data availability.

In the worst case, a malicious actor who controls both the sequencer and over ⅔ of the total stake can sign a *valid* state transition but still withhold the data. This would freeze the state and users would not be able to withdraw, but the attacker’s stake would also be frozen.  This is still a much stronger guarantee than sidechains, because no hack can be directly exploited and there is no economic benefit from being compromised. Moreover, guardian nodes can run on consumer hardware, so they don’t require delegated PoS. This means much higher decentralization and hence digital security.  A hacker would need to break thousands of guardian nodes to control the majority of the stake.

### Polygon

Polygon paid $400M to buy Mir, a startup building ZK tech.  MIR developed plonky2, a fast recursive proof system that is Ethereum friendly.  

The throughput of every blockchain (including every scaling solution) is limited by the capacity of the weakest node in the network, because every node has to process every transaction. With horizontal scaling, the throughput can be proportional to the total computing power available in the network. This can fundamentally improve scaling properties, because the throughput increases with every node that gets added to the network.

‘Plasma’ is a native protocol of Ethereum which is used by Polygon’s MATIC network. ‘Plasma chains’ are essentially sub-chains which have work hierarchically delegated to them by the main chain.  Polygon is secured by its own Proof of Stake consensus mechanism, where stakers lock up the MATIC token to get a reward for validating transactions.Polygon is secured by MATIC staking, which is a smaller pool of capital versus the miners who are securing Ethereum.

### Plian

Plian is a small player with only a $6MM market cap.  However, the company does explicitly support multiple chains running off the main P-Chain.  Plian rebranded from P-Chain recently and announced 5 division.
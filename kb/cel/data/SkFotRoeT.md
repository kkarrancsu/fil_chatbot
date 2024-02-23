# Deep Dive on MEV prevention

## Context 
Drand plans to offer a service to aleviate the externalities caused by MEV by building an L2 network that uses timelock encryption to hide the contents of the transactions that are sent to its mempool, thereby preventing them from being susceptible to frontrun and sandwich attacks. In this report, we provide an introduction to the problem and solutions space, discuss the competitor landscape, and go deeper into the mechanisms they use and how they can be improved upon. 

:::warning
:question: **Open questions:**
- What stage of development is the L2 architecture at currently? Would it follow a process flow as charted out in the doc (validation)
- Would the TLE for the L2 be provided by the same nodes that generate randomness for the VRF network? If so, how would the coordination (specifically for maintaining synchrony for both applications simultaneously) work?
- What mechanism would we need to focus on? (Rollup vs Drand node operator incentives)
:::

## Intro

[Maximal Extractable Value (MEV)](https://ethereum.org/en/developers/docs/mev/) refers to the maximum value that can be obtained from block production through inclusion, omission, or reordering of transactions within a block. 

Encrypted mempools are a class of solutions that aim to prevent MEV extraction by using cryptography to look for primitives to limit disclosure of information about pending transactions to block producers. The generalised order flow for such solutions are:
1. Users encrypt their transactions and send it to the mempool for execution
2. Block producers commit to a particular flow and make this commitment public 
3. The transactions are then decrypted and executed in the order that the block builder committed to 


[Rondelet and Kilbourn](https://browse.arxiv.org/pdf/2307.10878v2.pdf) give us a primer on some of the cryptographic primitives that warrent further investigation as methods to implement encrypted mempools: 
 - *Threshold Encryption* - $(t, n)$ threshold cryptography is a way to distribute confidential data among a group of $n$ people (called a committee) so that anyone can use the secret key, but only if more than the threshold $t$ people, in the committee work together. This aims to solve the problem of a single point of failure by allowing any group of more than $t$ committee members to collectively decrypt ciphertext, while keeping the original plaintext secret, even if an attacker can compromise up to $t − 1$ participants. Today, most encryption based MEV resistence solutions implement a threshold encryption scheme to offer MEV resistence. 
 - *Trusted Execution Environments* - A Truested Execution Environment (TEE) is a secure area within a computer's processor where sensitive applications can be run, and critical data can be stored. It helps code and data loaded inside it to be protected with respect to confidentiality and integrity. TEEs can be used to encrypt mempools by moving block production logic into a TEE.  Transactions can be decrypted using a decryption key that is stored in the TEE before they are executed and bundled into a block. This is appealing because it doesn't require changes to the underlying blockchain protocol, doesn't compromise composability on smart-contract chains, and doesn't incur any settlement delay. However, TEEs also have drawbacks, such as the security model, which requires trust in entities like Intel. Additionally, there is a lack of control at a protocol level in case of breaches in the TEE. Such cases would warrent hardware manufactures to rollout a patch for their firmware.  
 - *Timelock Encryption* - This is the approach that drand plans to take. Timelock encrypted mempools operate on the principle of revealing complete transaction data only after a pre-defined period of time, thus allowing users to conceal their transactions without using centralised relays and private mempools. A key consideration for this approach is to design a complementary mechanism of 1-block finality to avoid the possibility of [time-bandit attacks](https://www.mev.wiki/attack-examples/time-bandit-attack) and other malicious reorgs that seek to extract MEV by orphaning blocks. Osmosis mitigates this challenge by opting for a safety-favouring proof of stake consensus mehchanism where  all the validators vote on a block and if two-thirds of validators approve it, then the block is considered final. 

## Competitor Landscape - L2's with Encrypted Mepools 

### Optimism + Shutter - [Shutterised Optimism](https://gov.optimism.io/t/shutterized-optimism-an-encrypted-mempool-for-the-op-stack/6387)
In the shutterized version of Optimism, the main addition to the existing stack is a set of keypers who generate keys to encrypt and decrypt transactions. Users can send encrypted transactions to protect them from frontrunning and censorship. To do this, users first create a payload and encrypt it with an encryption key that the keyper generates. They then submit the encrypted payload to a smart contract, the Shutter Inbox Contract. Whenever the sequencer seals a block, the keypers generate the decryption key for it and broadcast it on a P2P network. The sequencer picks up the key and puts it at the front of the block. Executing this transaction will result in all encrypted transactions being read from the Shutter Inbox Contract, decrypted, and executed. The state transition function ensures that the sequencer plays by the rules and that blocks fulfill the structure outlined above. In particular, blocks without a decryption key at the top (or an incorrect one) are deemed invalid.

![](https://hackmd.io/_uploads/ByxXtAmS-T.png)
<p style="text-align: center;">Fig1: Internal structure of blocks: Time increases from left to right, with decryption processes between the blocks. Inside of the block structure, transactions are executed in a left to right order.</p>


### Arbitrum + Chainlink - [Arbitrum with Fair Sequencing](https://blog.chain.link/arbitrum-and-chainlink-fair-sequencing-services/)
Offchain Labs and Chainlink Labs are working together to minimize MEV on Arbitrum using Fair Sequencing Services (FSS), a decentralized transaction ordering solution. FSS uses decentralized oracle networks to collect user transactions off-chain, generate decentralized consensus for transaction ordering, and submit the ordered transactions using the Arbitrum protocol. In the first phase of FSS, user transactions are encrypted to hide transaction details, ordered by a decentralized oracle network, and then decrypted for execution by the Arbitrum protocol. This will remove the ability to front-run transactions based on early visibility. In the second phase of FSS, Aequitas ordering (consensus) protocols will be implemented to order transactions based on supermajority receive time. This will help enforce a first-in, first-out (FIFO) ordering policy, and will be combined with transaction encryption mechanism from phase one, to provide a more defense-in-depth solution for the fair ordering of user transactions.

![](https://hackmd.io/_uploads/B129xVB-T.png)
<p style="text-align: center;">Fig2: The Arbitrum protocol with FSS.</p>



## Mechanisms 

### Transaction Supply Chain
In order to get a better understanding of the mechanisms involved, we need to dive deeper into the transaction supply chain, and the economic flow models. 

![](https://hackmd.io/_uploads/S1LAXAQWa.png)
<p style="text-align: center;">Fig3: Transaction Supply Chain in a drand powered L2 system with an encrypted mempool</p>

### Economic Flow Models
Based on the above process flow diagram, we understand that the main actors in the system include:
- **Users** 
    - They submit transactions for inclusion in the mempool
- **Drand node operators**:
    - They provide value by generating both the encryption and decryption key
    - The encryption key is used by the user to conceal the contents of their transaction
    - The decryption key is revealed once the transaction sequence is confirmed and it is used by the rollup operator to decrypt the transaction before execution
- **Rollup operators**:
    - They sequence transactions, execute them and post the proof of execution to the layer-1

Based on this understanding of the actors involved and the role that they play in the system, we can now dive deeper into the economic flows within the system. 

![](https://hackmd.io/_uploads/S18cJUSbp.png)
<p style="text-align: center;">Fig4: Rollup economic flows in a drand powered L2</p>

Therefore, in essence, there are two main mechanisms that are at play. The first one being incentives to rollup operators, and the second one being incentives to drand node operators. In both cases, the value flows to the user. 

### Rollup Mechanisms 
In order to design the mechanisms of the rollup, we need to further break down the economic flows into costs and revenues. We consider the entire rollup to be a system, and assess the costs as outflows and revenues as inflows in a framework similar to [the one introduced by Barnabe Monnot](https://barnabe.substack.com/p/understanding-rollup-economics-from). What we are breaking down below is the entire left fork from the previous diagram on the economic flow model. 

Rollup systems have a complex cost structure, which can be divided into three categories:

- **L2 operator costs**: The cost of running the rollup infrastructure, such as maintaining a transaction pool, sequencing batches, and computing state roots/state diffs/validity proofs.
- **L1 data publication costs**: The cost of publishing compressed rollup data to the base layer. This cost is incurred by the base layer and is currently governed by EIP-1559.
- **L2 congestion costs**: The cost of allocating scarce rollup blockspace to users. This cost is typically made explicit through the use of fee markets.

Rollup systems receive revenue in two forms:

- **Transaction value**: The value that users obtain from transacting on a rollup rather than elsewhere. This can include the convenience of lower fees and faster transaction times, as well as access to new features and applications.
- **Issuance (Optional)**: The ability to issue new tokens, which can be used to cover operator costs or to generate revenue for the rollup system as a whole.

It is essential for the system (in this case, the rollup) to maintain budget balance, meaning that they must receive a revenue equal to or greater than their costs. Generally, the mechanisms that dictate issuance in rollup systems are made dynamic in a way that can be used to ensure budget balancs. Operators can issue new tokens to cover their obligations if they are unprofitable.

### Drand Mechanisms
If we were to do a similar breakdown of the right fork in our economic flow model, we can break down the flows to the "drand" system into a single inflow, and a single outflow. 

Here the cost is:
- **drand node operator costs**: The cost of running the rollup drand node, such as generating the encryption and decryption key, and releasing them to the user/sequencer in a timely manner.

The revenue in this case is:
- **drand encryption value**: The value that users obtain from using drand's services in hiding the content of their transaction. This can include the value that is captured by them not being front-run or sandwiched by an arbitrager.

Similar to the case with the rollup mechanisms, it is critical to ensure that the renvenue to the drand system is greater than or equal to the costs, in order to make the service a sustainable one for node operators. 

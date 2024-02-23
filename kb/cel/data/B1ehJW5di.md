---
title: HC incentives discussion
tags: IPC
---

# Hierachical Consensus Incentives discussion

#### ZX, December 2022

### Resources

- [https://www.youtube.com/watch?v=G7d5KNRZdp0](https://www.youtube.com/watch?v=G7d5KNRZdp0)
- [https://github.com/protocol/ConsensusLab/blob/main/docs/b1.pdf](https://github.com/protocol/ConsensusLab/blob/main/docs/b1.pdf)

### 2/10/2022 CEL Response

**Some differences from the last iteration**

- There is a greater decoupling between consensus within subnet and consensus on the main chain.
- There is also no notion of “power” or “delegation of power” on subnet relative to mainnet.

**Clarification needed**

- There is some mention of circulating supply on subnet and it is mostly mentioned in the following two ways.
    - Security impact is limited to the circulating supply of subnet.
    - SCA needs to keep track of circulating supply of subnet.
    - ZX: the mainnet may not actually need to care about circulating supply of subnet since users can issue any tokens they like on subnet. The question really is how much collateral does that subnet need to provide to spawn.
    - There are two aspects of “circulating supply” within a subnet: initial deposit, and the balance of crossnet in and out transactions. Only the initial deposit seems to be locked, while the balance of transactions is liquid.  It is unclear how to use these for:
        - “Mining rewards are proportionately distributed among all subnets” Does proportionately mean with the locked balance? the transaction circulating supply? Does this proportion also come with consensus power towards their parent chain?
- Can we confirm that only transactions that involve SCA will impact the network bandwidth (BaseFee) of the main chain?
    - aka what the interfaces with gas are?
    - It seems like only cross net transactions (which actually take place in the parent net) are the only ones that would touch gas fees of that parent net. So the FIL gas fees would only be touched by cross-net transactions amongst “first layer” subnets?
    
- Checkpointing
    - Despite not explicitly mentioned, there might be some CryptoEcon questions around checkpoiting. Do we have some sense of constraints / desirability around checkpointing?
        - the more frequent the better?
        - how does it impact gas?
    - Checkpointing must invoke some consensus power? How much information can a subnet write to the parent net at checkpointing? should it be proportional to their locked deposit?
- Initial Deposit
    - The amount of tokens locked by the subnet, determine the influence that subnet will have on its parent chain? This translates to consensus power on the parent chain+ block rewards from the parent chain.
    - This effectively transforms FIL into a PoS chain? Could this deposit also be made instead in storage capacity? Or to implement a lending program where these staked FIL are to be used to subsidize storage providers.
    - The initial deposit, must it always be in FIL? or can it be in the token of the parent chain? This means that only “first layer” subnets would need FIL deposits.
- Role of FIL
    - Each subnet may implement their own native token, which can be used for in-net transactions. These tokens cannot be sent to a different subnet, instead the native token must be translated to The parent-level token, and some of that parent token be transferred to a different subnet
    - There could be a stabilizing effect for the in-subnet tokens, if they can be used to redeem parent tokens that were locked. Suppose there is a total amount $D$ of deposit in parent-chain token, and the subnet as a circulating supply $S$ of native token. A native token holder with $s$ in native token, could be allowed to redeem parent token, by burning their native token, and obtaining an amount $d=D\frac{s}{S}$ of the parent-level token. This way All Subnet coins are “stable coins” relative to FIL.

**Key CryptoEcon Questions**

- Assuming an EIP1559-type model on the main chain, the network circulating supply is tied to the usage of the network.
    - BaseFee is a result of relative supply and demand for using the network and BaseFee directly affects Network Transaction Fee.
    - Hierachical Consensus is a way for a Network to scale horizontally (meaning increasing its network TPS on demand). As such, the following two statements may be at odds.
        - Any one can spawn a subnet (unlimited network TPS) and hence further crushing network protocol revenue through BaseFee mechanism (unlimited chain bandwidth supply).
        - Bringing value to the parent chain as there is value created with horizontal scaling.
        - Balancing the two goals will be the key tradeoff for the policy that governs spawning of new subnet.
            - We can call this the collateral function but it does not have to be in that form. For example, we can take inspiration from Polkadot’s parachain auction, trying to price the subnet to the groups/operators/teams that can derive the most value from it (bidding) and give the access to them.
            - Similarly, we may not need to enable sub subnet from the get go.
- Given that there is a policy for spawning a chain, who gets to decide when to sunset one? It is unclear who should have that power and under what conditions. We should go back to first principles.
    - A possible way out is the “stable coin” model above, where subnet members can cash out a piece of the parent token supply, by burning their subnet token . A subnet naturally dies out, or more accurately stops interacting with the parent net, when all of its parent-net tokens are removed.
    
### TODO
    
- Specify power to write blocks in subnet?
    
- Validate transactions between nets?
    
- Compare the power of two different subnets?
    
    1) horizontally scaling bandwidth of mother chain—unlimited supply of chain —how to compensate the mother chain.
    
    2) Policy for starting and stopping a subnet
    
    3) How much of the coupling notion of power on the main net?
    
- Present this to Consensus Lab for discussion.  Decide to open new issue or move to Backlog after discussion.  Share document.
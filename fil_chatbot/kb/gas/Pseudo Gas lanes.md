# Pseudo Gas lanes

## Summary

Gas lanes have been proposed as a mechanism to separate SP storage-related gas usage from general FVM gas demand, which can have undesireable effects on SP operations and the network as a whole.

While the proposal has gathered positive feedback, and seems to be welcomed by the community, There are questions as to how feasible explicit separate gas lanes are to engineer.

Here we discuss an alternative "pseudo gas lanes" solutions, where a number of different but more feasible tools, such as **SP gas refunds, explicit proof fees, Batch balancer modification** and **adjustable target block size** can be combined together to produce an outcome that is equivalent to the implementation of "real" gas lanes

## Gas lanes, gentrification and sprawl
We have started a [FIP discussion](https://github.com/filecoin-project/FIPs/discussions/679), proposing "gas lanes" as a solution to the potential problem of "gas gentrification", where new FVM applications could end up pricing out essential SP operations. Gas lanes can also be a [viable solution towards the "opposite" of gas sprawl](https://hackmd.io/@7JfXCEujQwWCaFm8acpJ7A/SJIqR1Gl3), where there is excessive supply of gas, in a way that negatively affects network revenue.

In its simplest form of a gas lanes mechanism, Filecoin gas is separated into two general categories: SP "storage related" messages, and all other FVM messages. 

We define $B_T$ to be the "target block size" parameter that is used in the EIP-1559 mechanism. An explicit "gas lanes" solution would split storage related and other FVM messages, where storage messages would be allocated a target block size of $aB_T$ for some $0<a<1$, and other FVM messages have allocated a $(1-a)B_T$ target block size. 

The allocation parameter, $a$, could be dynamic, and it is a separate problem, choosing the "best" $a$ that brings most utility to the network at a given time. 

Each gas lane would have its own base fee, which follow individual EIP-1559 pricing formulas, with target block sizes $aB_T$ and $(1-a)B_T$.

## Difficulty  of creating gas lanes

Allowing "storage related" messages to consume a different type of gas than other general FVM messages, requires the ability to identify and individually charge base fee for such messages.

The main difficulty of this approach is tha storage related messages may not be easily separable, in cases where the messages are sent by a smart contract, within a mix of other general messages.

Presently, storage related messages are sent directly by the SP. When the SP wants to prove a sector, they send their PreCommit and ProveCommit messages, estimating and paying for their gas usage. If this was the only way storage related messages will be sent, then it can be feasible to identify and separately price such messages.

In the near future, SPs may be doing such storage related operations via smart contracts. The user would send and pay for  a message that triggers a smart contract, which then sends a number of messages, which may include storage related messages. Since the payment for gas usage happens at the initial user-sent message, it is hard to separate and estimate what fraction of the messageis attributable to each different gas lane.

## Feasible tools to effectively recreate gas lanes

Given the problem of identifyng different types of messages, and assigning them to different gas lanes, is there a way to acheive the same effect by combining different tools that are more feasible?

We explore here a possible alternative mechanism to gas lanes that could end up acheiving similar results of defending against gas gentrification and sprawl, by combining a number of mechanisms that are more feasible to implement.

We also summarize the key points of all the mechanisms discussed in the table at the end of the document

### Discounting/refunding gas usage 

An approach that has been proposed in an earlier FIP discussion was to [excempt storage related messages from paying base fee](https://github.com/filecoin-project/FIPs/discussions/430). The discussion quickly pointed out that there may be incentive alignment difficulties by implementing such an extreme solution to the gentrification problem. 

Apart form this, isolating storage related messages such that they can be excempted from base fee runs into the same feasibility issues as the full gas lanes solution.

**An alternate version** of this proposal could be instead to *charge regular gas usage to storage related messages, but later refund some percentage of the gas fees to SPs.*

A simple mechanism to implement such refunds is to track the gas usage of all storage related message in a given period (let's say for one day as an example), then that corresponding amount of gas fee burn can be re-introduced the next day as additional block reward. The principle here being that both block reward and gas usage should be roughly proportional to relative power of each SP.

One weakness of this approach is that gas usage is related more directly to *raw byte* power, while block reward is proportional to quality adjusted power. Therefore SP's with higher quality multiplier sectors would  dispproportionately benefit from such a mechanism, receiving more refund than they spent originally. This issue could in principle be addressed by introducing explicit proof fees, as will be discussed in the next section.

If the refund given was more direct, in the sense that each SP gets refunded exactly the amount of gas that they used, this could incentivize SP's to set arbitrarily large gas fee caps, to ensure their message is included, knowing they will be refunded afterwards. The fact that the gas fees are combined and then redistributed amongst SP's eliminates this incentive on an individual basis, if one SP sets a high fee cap, then they will not individually get back a full refund.

The percentage of the gas fees that is burned vs refunded can also be set dynamically. If there is a coordinated attack, where most SPs set high fee caps knowing the group of SPs as a whole will get their fees refunded, the burn percentage could be increased, disincentivizing the attack.

### Explicit proof fees

Once there is a mechanism for refunding gas fees to SPs, one could consider placing explicit proof fees, that are more appropiately priced for storage related messages. This idea is based (up to some modification) on [this FIP discussion](https://github.com/filecoin-project/FIPs/discussions/557).Explicit fees here mean that the network charges explicitly for the act of submitting proofs, independently of demand for gas usage (though the fees can also be dynamic, and can be made to vary with demand).

A way to effectively acheive a siilar effect of having gas lanes, is to decouple Storage related messages completely from regular usage by 
1) Refunding all (or X percentage) of gas usage of storag messages via refunds through additional block rewards.
2) Charging explicit fees for proofs, with their own pricing mechanism, that is independent of demand for gas usage. 

Explicit proof fees can also be used to fixed some of the imbalances created by simple gas fee refunds. As we previously discussed, the refund mechanism would disproportionately benefit sectors with higher multipliers, which earn a higher proportion of block reward, while not consuming an equally higher amount of gas. Proof fees for sectors with multipliers could be set higher, for instance to compensate for this disproportionate benefit.

### Opening gas supply by enabling batching

Implementing explicit proof fees, as argued in the [original FIP discussion](https://github.com/filecoin-project/FIPs/discussions/557), would enable us to eliminate the batch balancer mechanism entirely, which would result in lower gas costs for general FVM messages as well.

The batch balancer mechanism makes batching proofs irrational when base fee/demand for gas usage is low, artificially forcing sectors to consume more gas than is necessary, which keeps base fees and network revenue from plumetting. 

Since explicit proof fees decouple storage proofs from gas fees, the proof fees can be designed in a way that replicate the batch balancer's effect, of regulating the low demand scenarios, ensuring a base level of network revenue, while encouraging batching as the optimal strategy at all times. 

Having SP batching proofs at all times would end up opening large amounts of gas supply that could be used for general FVM messages, generally lowering base fees.

### Adjustable target block size

Note that replacing the batch balancer mechanism with explicit proof fees, which would result in generally lower gas base fees, could turn into a scenario where the majority of network revenue is coming from SPs providing proof fees, which subsidizes cheap FVM gas usage. 

If it is desirable to balance the network revenue coming from FVM and SP's, base fees could also be artificially increased by adjusting the parameter $B_T$, that is lowering the target block size from the EIP-1559 mechanism, as proposed in [this FIP discussion](https://github.com/filecoin-project/FIPs/discussions/515).

Note that if storage proofs are decoupled from gas fees via the mechanism described above, adjusting the target block size would have no effect on storage-related messages, while it could increase costs, if that is desirable, for other general FVM messages.


| Mechanism                  | What does it acheive?                                                                                         | Pitfalls of mechanism                                                                                                         |
|----------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Gas Lanes.**  Classify messages into $N$ different groups and allocate a proportion $a_i$ of the block to a class $C_i$, of messages, where $i=1,2,\dots,N.$ | - Defends against gas gentrification and sprawl                                              | - Difficulty in identifying and charging storage-related messages sent by smart contracts                    |
|                            | - Separates storage-related messages and general FVM messages                                | - Separation of messages is challenging and might only work in a few cases                                                    |
|                            | - Well-received idea by SP community  and probably better studied than other alternatives      | - No consensus on technical feasibility                                                         |
|                            | - Flexible design  |                                                       |
| | |
| | |
| | |
| | |
| | |
| | |
| **Discounting/Refunding.** Remove, reduce or return via additional block rewards the cost of specific, storage-related messages. | - Refunds a portion of gas fees to SPs, effectively reducing their costs                                                       | - Might disproportionately benefit SPs with higher quality multiplier sectors                                |
|                            | - Gas fee refunds can be set dynamically to disincentivize abuse                                    | - Incentivizes SPs to set arbitrarily large gas fee caps if the refund mechanism is not well designed        |
|                            |                                 | - There might  be a missalignment on the amount paid and amount refunded       |
| **Explicit Proof Fees.** (TBD)   | - More appropriately priced fees for storage-related messages that are independent of demand for gas                               | - Could end up with SP's subsidizing FVM gas usage if fees not set correctly
| | -Could perform a similar role as the Batch Balancer mechanism, thus making that redundant, increasing gas usage efficiency | 
| |-Could be used to compensate for imbalance created by the gas refunds, higher multiplier sectors could pay higher fees, so they do not disproportionately benefit from gas refunds.
| **Batch Balancer modification**               | - Potentially increases gas supply by enabling more efficient processing of multiple messages | - Requires an alternate solution for low-demand periods, which could be provided by explicit proof fees.                                                 |
| |-Would simplify SP operational logic, no inefficient batching vs. no batching rationality test required. | 
|       | -Opportunity to improve current batching mechanisms and their unpopular revenue-capturing systems | -                                             |
| **Adjustable Target Block Size**| - Can help balance network revenue between SP's and general FVM, prevent SP's from subsidizing all FVM gas usage. |-Requires implementing the gas refund solution, such that it doesn't negatively affect SP operations.
| | | -Adds complexity to EIP-1559 formalism

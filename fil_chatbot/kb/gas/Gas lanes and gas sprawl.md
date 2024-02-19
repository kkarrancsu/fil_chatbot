# Gas lanes and gas sprawl

## Key points

* **Gas sprawl** is a situation where supply of available gas is too large for the current demand for gas, in a way that negatively affects total network revenue.
* The Batch balancer mechanism is a measure we have already taken against gas sprawl, but it is very limited and not transparent.
* Gas lanes would provide a mechanism to protect against gas sprawl that is compatible with Filecon, where SP's consume large amounts of gas.
* Gas lanes would enable replacing the batch balancer with a more general and future proof mechansim, including possibly setting up explicit proof fees.

## Summary of proposed solution via gas lanes

* We have previously proposed the [Adjustable Target Block Size](https://github.com/filecoin-project/FIPs/discussions/515) as a general and permanent solution to gas sprawl. This however can be problematic in Filecoin, since it could make SP operations too expensive.
* We are proposing introducing separate gas lanes [as specified here](https://hackmd.io/IVCFQYo7T--v-xNxmhfv0w?both), for SP storage related messages vs. other general FVM usage, as a potential solution to the parallel "gas gentrification". This separation allows us to more granularly control the supply of gas to avoid sprawl, without negatively affecting SP's.
* Gas lanes would ensure revenue can be extracted from general FVM messages, while managing the supply of gas for SP-specific messages would make the batch balancer mechanism redundant and unnecessary.

## What is the problem with Gas Sprawl

We define **gas sprawl** as a situation where the available gas in a block is considered *too large* for the corresponding demand for gas usage. Whether this is a problem or not, depends on what is the network objective.

A simple scenario of where gas sprawl could be considered to be a problem is *if the network is interested in maximizing total gas fee burn*, (commonly reffered to as *total network revenue*), as a means of introducing a deflationary pressure. If the available gas in the block is too large for the level of demand, total gas fee burn could be maximized by reducing the block size, which would increae base fees and competition for block space.

We acknowledge that *gas sprawl is not objectively a problem for everyone*, Specially if network revenue could be maximized from other sources (such as deal revenue, and total value lock from FVM smart contract). Total gas fee burn is, however, a significant contribution to total network revenue, and it may be worthwile to consider its optimization.

Gas sprawl could occur as a consequence of FVM-enabled scaling solutions, such as Interplanetary consensus (IPC), which could end up removing "too much" gas demand from the Filecoin rootnet, and driving down network revenue.



## Batch Balancer is a narrow solution to gas sprawl

Filecon already has a mechanism to defend itself against gas sprawl, in the form of the *batch balancer*.


FIP-0008 and FIP-0013 introduced the ability to submit PreCommit and ProveCommit sector proofs more efficiently, as batches of proofs. For a large enough number of proofs, submitting them as a batch consumes significantly less gas than sending the submitting the same number of proofs individually.

These improvements then greatly increased the supply of gas available for sector onboarding. 

What is known as the Batch Balancer mechanism, consists of an additional Gas charge was introduced in FIP-0013 and FIP-0024, to be charged to a batch of proofs, **designed to make it irrational, or more expensive, to batch when base fee is below a certain threshold**. That is, when the ability to batch introduced too much supply of gas, without the demand for gas to justify it, the batch balancer made it irrational to use that extra demand.

The batch balancer mechanism is therefore a very specific approach to protect against gas sprawl, by "turning on" ( technically, it's always on; what changes is whether it is rational or not to use it) or off the ability to batch proofs, depending on demand levels. 

The current batch balancer mechanism also involves parameters that need to be recalibrated manually. For instance in FIP-0024 parameters were adjusted to increase the lower threshold on base fee required to make batching rational, given an observed change in network onboarding rates. FIP-0057 also introduced changes in the expected gas usage of PreCommit and ProveCommit messages, making a manual recalibration of batch balancer parameters necessary.

*Could the batch balancer be replaced with a more general mechanism that regulates overall supply of gas to more accurately match demand levels, instead of specifically targeting only the ability to batch?*



## Filecoin gas sprawl problem is more complicated than Ethereum

Filecoin miners (SPs), at least at least before FVM launch, were the largest consumers of Filecoin gas. This is in contrast to Ethereum where miners don't have particularly significant gas operational costs.

This makes the question of *how should gas supply be optimized?* easier to answer in a network like Ethereum. **Ethereum miners strictly benefit from having higher total network revenue, in the form of gas fee burn**. It is in the best interest of miners to maximize gas supply in a way that the most revenue is generated, from users that are willing to pay or gas.

In contrast **having high gas prices can negatively affect Filecoin SP's**, since gas usage is a large component of an SP operational expenses. In an ideal case, SP's would benefit from extracting maximum network revenue from non-SP's, while keeping as much gas supply as possible available for SP operations. 


## Gas lanes and full control of supply

We are proposing the idea of Gas Lanes, in parallel in [this discussion](https://hackmd.io/IVCFQYo7T--v-xNxmhfv0w?both), as a direct solution to the issue of *gas gentrification*.

On the other hand gas lanes also provide a possible solution to the problem of gas sprawl appropriate for the Filecoin network.


In a network like Ethereum, where miners benefit from having higher total gas fee burn, a solution like the proposed [Adjustable Target Block Size](https://github.com/filecoin-project/FIPs/discussions/515) alone can be effective for protecting the network against gas sprawl. In this scenario the total supply of gas (parametrized by the target block size parameter in EIP 1559), could be adjusted to find an optimal block size, that better matches current demand for gas, and maximizes network revenue. 


Implementing the adjustable target block size on its own is more complicated for filecoin, since it would generally increase SP operational costs as a byproduct of maximizing network revenue. 


The introduction of gas lanes opens a possiblity to reserve an an amount of gas explicitly for SP essential messages (Such as PreCommit, ProveCommit, SubmitWindowedPoST, *etc.*), while being able to maximize network revenue, if desired, on the rest of the non-SP messages. 

## Relationship with batch balancer explicit onboarding fees

While gas lanes serve to protect SP operations from being priced out, one may one to also actively manage the gas supply available to SP's.

**A gas lane with adjustable width for SP messages could eliminate the need for a batch balancer mechanism**. At times of lower demand for gas, the width of the SP gas lane could simply be decreased, more accurately balancing gas supply to gas demand, fulfilling the purpose of the batch balancer, which would become redundant. Regulating SP gas supply by adjusting gas lane width is also more *future proof* than the batch balancer mechanism, as the batch balancer only regulates when SP's are incentivized to batch their proofs, but there may be other technological advances in the future that make SP gas usage more efficient and may lead to gas sprawl, that are unrelated to proof batching.

A related recent proposal is the idea of **[eliminating the batch balancer in favor of adding explicit proof fees](https://github.com/filecoin-project/FIPs/discussions/557)**, where any network revenue from SP messages would be extracted via explicit fees, that are more commesurate to the value derived by the SP from using the Filecoin network. Gas lanes would also be a way to enable this proposal, by reserving as much gas supply as possible for SP operations, reducing SP gas costs, without being affected by non-SP gas demand. Then explicit proof fees can be added on top of the very low gas fees.


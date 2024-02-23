---
title: Blockchain scaling solutions and risk of gas sprawl
tags: Econ monitor, Gas, draft
---



# Blockchain scaling solutions and risk of gas sprawl

## Summary

Scaling solutions have the capacity to absorb some demand from the Filecoin mainnet. For built-in scaling solutions (such as sharding, or the original version of IPC), the Filecoin network would have direct tools available to regulate how much capacity is opened up by the scaling solution, not wanting to open up **too much capacity**, in a way  that would be harmful to Filecoin's best interests.

Currently, IPC is planned to be implemented fully as an L2 solution on FVM. This means there is less control available to regulate the amount of capacity opened up by scaling solutions. If the amount of supply that has been opened up becomes problematic, the only tool Filecoin has is to regulate FVM gas usage as a whole.

Being optimistic, this risk of too much supply could be exactly cancelled by the risk of FVM introducing too much demand for Filecoin gas usage, but this requires strong belief that free markets will self-regulate for the best, and it may be more advisable to regulate possible gas sprawl or gas gentrification more actively. The most direct solution to these problems we are working on is introducing separate gas lanes for FVM and for storage-related messages, as well as an overall [adjustable target block size](https://github.com/filecoin-project/FIPs/discussions/515).


A more detailed research plan (WIP) can be found [here](https://hackmd.io/@cryptoecon/BJGVpWvio). The main outcomes of the planned research project will be a full understanding of the potential gas-related risks of FVM (How too much gas demand, or too much gas supply from FVM could be harmful to Filecoin, and the relation of net FVM gas demand to several Filecoin health indicators.) Having understood the risk, the second outcome of this project is understanding how effective gas lanes plus adjustable target block size can be at combatting these risks (as well as recommending an optimal mechanism and parameter choice), vs the alternative of not doing anything and relying on the free market to self-regulate. We expect to complete the project by the end of Q1 2023.



## FVM changes the gas economy

With FVM planned to be introduced soon to Filecoin, we can expect changes in gas usage and transaction fee economics. Filecoin blocks can accommodate a finite amount of gas, a scarce resource, which has so far been used mostly only for processing storage-related messages.

FVM will open the door to a variety of new uses for precious gas. There is a known risk of "[gas gentrification](https://github.com/protocol/CryptoEconLab/discussions/58)". In that case the high demand from new FVM gas uses can price out storage providers, making storage-related messages too expensive, ultimately harming the foundation of the Filecoin network.

There also lies risk at the other end of the spectrum: could FVM end up absorbing too much precious demand from Filecoin? This issue of gas "Sprawl" was discussed [in  the context of Interplanetary Consensus](https://github.com/protocol/CryptoEconLab/discussions/64) (IPC) as a built in actor, a previously proposed solution to scaling capacity in Filecoin. The current version of IPC is planned to be deployed entirely as an L2 scaling solution using FVM. 

The risks of sprawl previously associated with IPC, are then now to be considered a possible outcome of the introduction of FVM.


## Sprawl is relative

To determine if the network is "sprawling too much" we must define a network target. The target definition encodes the values of the Filecoin network and answers the question "what should the Filecoin gas economy be optimizing for?"

Currently the EIP 1559 mechanism for gas pricing used in Filecoin targets having the lowest possible gas fees (by encouraging usage of as much gas as the network can consistently process). If this is the target, the network could never sprawl too much, as adding more and more capacity would reduce gas fees, which would be a good thing relative to the goal of lowering transaction fees.

On the other end of the spectrum, the network could for instance want the gas mechanism to maximize for the total network revenue (total token burn through gas fees). In this case there would be an [optimal amount of capacity to introduce which would maximize revenue](https://hackmd.io/@cryptoecon/B10RGzlHo), opening any more capacity beyond that would only drive gas fees, reducing network revenue.

Low gas fees and total network revenue are not the only possible targets to choose from. There are a number of quantities that may be valuable for the Filecoin gas economy to optimize for, such as SP utility, total deal revenue, total network storage power, total onboarding rate, just to name a few. 


How much control do we have over how much Filecoin sprawls? That depends on the scaling mechanism.

## Appendix: Regulating sprawl from different scaling solutions
### L1 Horizontal scaling (sharding)

We define L1 scaling here as a scaling solution that increases the amount of gas available on the main blockchain itself. A solution that has been proposed in Ethereum is [sharding](https://www.web3.university/article/ethereum-sharding-an-introduction-to-blockchain-sharding), where essentially the blockchain can be split into $N$ parallel blockchains, or shards (equally distributing the amount of validators and consensus power amongst the $N$ chains), while periodically reporting on their respective states to each other. (Note that the latest version of sharding planned for Ethereum differs from what we have described here, as they would initially include only [data-availability shards](https://ethereum.org/en/upgrades/sharding/) without excecution capabilities. )

The immediate sprawl-related question here would be "How should we set the number $N$, that is the best for our network?" Answering this question depends on the network target. The network could regulate sprawl by finding the optimal $N_{\rm optimal}$ that would maximize the network target.


### Built-in IPC

In its earliest form, [IPC was proposed as a Filecoin-native scaling solution](https://github.com/filecoin-project/FIPs/discussions/419). This version of IPC would be similar to sharding, except for arranging the shards into a hierarchical topology (hence its previous name "Hierarchical Consensus"). In this case there would exist the Filecoin rootnet, which must allocate some of its gas resources to process checkpoints from $N_1$ subnets that operate directly under it. There are in turn $N_2$ subnets that checkpoint onto the first layer of subnets, consuming some of their gas resources, and so on with any possible number of layers. 

In this previous version, the rootnet could also transfer some amount of trust to its first layer of subnets, by requiring a minimum amount of collateral the subnets need to lock to remain in an active state, where the rootnet would have power to slash some collateral when a defined fault is committed. 

What could the rootnet do in this case to avoid over-sprawling? The rootnet has two levers to pull: it can control the amount of gas allocated to subnet checkpointing (making it cheaper or more expensive to checkpoint), and it could increase or decrease minimum collateral (making it a more or less enticing investment to spawn a first-layer subnet). 

This is a lower level of control to the sharding case, where $N$ could be manually fixed. Nevertheless these are two powerful levers that could provide a major influence that propagates through the entire hierarchy. One could be reminded of a central bank raising or lowering interest rates, an effect that propagates to different levels of the national economy. 


### L2 IPC

The current version of IPC is now planned to be launched as an FVM actor, and a fully L2 solution. While the risk of sprawl remains there, a given L2 hierarchy could grow too large, absorbing too much demand from the rootnet. There are fewer direct levers to pull to attempt to control the sprawl. It is no longer possible to directly limit the amount of gas available for checkpointing, or to enforce minimum collaterals for the first level subnets.

The sprawling hierarchy would be effectively indistinguishable amongst all FVM messages. It is now FVM directly which represents a risk of gas sprawl. The only remaining lever available to control FVM-related sprawl, is to control the amount of gas available to FVM as a whole, creating different gas lanes for regular storage-related messages and FVM messages. 

Coincidentally this is the same lever that is available to regulate gas gentrification. Whether FVM ends up leading to gentrification or to sprawl, controlling the amount of gas allocated to FVM, in a way that maximizes a specific network target, could be a way to address both problems.  

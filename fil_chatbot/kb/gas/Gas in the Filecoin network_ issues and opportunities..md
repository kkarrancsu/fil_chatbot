---
tags: Gas, Research proposals, Almanac
---

# Gas in the Filecoin network: issues and opportunities.

##### Juan P. Madrigal Cianci.


**TL;DR:** A visual summary of the  gas-related topics currently being investigated by the CryptoEconLab,  their relation with each other, and their use base is shown below. 

![](https://hackmd.io/_uploads/SkG2U3AUj.png)



A table containing short descriptions of these topics is presented in Section 3. 



==As suggested by ZX, I will likely split this into several documents (one per section). I will do this once we are done discussing here, to avoid having to jump through multiple docs==

## 1. Introduction.
Currently, there are several unresolved questions, potential issues, and research directions related to gas consumption and behavior in the Filecoin network.   In light of this, the CryptoEconLab (CEL) has decided to collect a list describing these *problems*, and detailing how we intend to solve them. The purpose of this document is two-fold. On the one hand, it would serve as a single source of truth for gas-related questions, thus facilitating and streamlining research and research directions for the CEL. On the other hand, we hope that such a document can be helpful for other teams, such that they can plan around the development of these issues, as well as contribute to their unresolved questions regarding gas consumption.

We list these issues and research opportunities in the next Section and present a summarised version of such a list in Section 3.

## 2. Research questions, issues, and potential problems. 

We now present a list of potential issues and research opportunities regarding gas consumption in the network. 

We classify our progress in three categories 🟢,🟡,🔴:

1. 🟢 means are actively working towards the problem discussed therein. 
2. 🟡 implies that we have done some work toward this issue; however, we have temporarily paused working in this direction for various reasons, such as shifts in priorities and diverse blockers.
3.  🔴 means we have not formally started a deep dive on that topic. 


Similarly, we also classify our research directions on three categories:

1. Sections marked with 🚩 represent either a problem or an issue that can become problematic for the network.
2. Sections marked with 💡 represent a potential research opportunity aimed at improving the network.
3. Sections marked with 🛠️ represent a research oportunity to develop a tool, to be used either as a means to help other research directions, or by users.


---
### 2.1. FVM and block space gentrification. 🟢 🚩


==Remark: this section is a condensed version of [these notes](https://hackmd.io/gV9HY4KDQluovuRr3wRKkw).==

**Description.** 
A potentially harmful, purely hypothetical  (yet possible) scenario stemming from the release of the Filecoin Virtual Machine (FVM) is that an increase in block space demand due to the FVM results in some valuable block space taken away from the core functioning of the network. This situation could negatively affect the network, making it more expensive for storage providers to onboard data and submit storage proofs.   We refer to this scenario as *block space gentrification*. 


**Potential solutions.**

A potential, short-term solution is implementing gas lanes (c.f. Section 2.6). The main idea behind this solution is to classify messages in groups according to, e.g., their perceived importance and then to preallocate a given amount of block space to each of these categories. A long-term solution would be to use IPC dedicating one subnet to FVM-related messages. 

**Proposed steps and related questions.**

1. Identify the network-related quantities likely to be affected by the upcoming change in demand.
2. Identify the theoretical, methodological, or computational tools that we would need to investigate the effects of an increase in demand for block space on the quantities identified above. 
3. Identify problems that could arise from this change in demand. 
4. Compare several "what if scenarios" for models using (i) gas lanes and (ii) no gas lanes. Write down a report on this. 
5. Propose and test relevant changes, patches, or solutions that would be needed to solve those problems presented in the previous point.

We remark that we will discuss points 2 and 3 with the FVM team and other network stakeholders.


**Related projects**

1. *InterPlanetary gas usage*, as a potential solution.
2. *Gas Lanes* as a potential solution.
3. *Mpool modeling*, for testing scenarios.


**Related Documents**

At the time of writing, the CEL is actively investigating this issue. Some of our documents on this matter are listed below. 

1. [Work plan for the FVM gas consumption (CEL)](https://hackmd.io/gV9HY4KDQluovuRr3wRKkw). Here we aim to address these previous 5 points. We are actively working on that document at the current time. 
2. [A mathematical model for Mpool dynamics. (CEL) (2022). *In progress*](https://www.overleaf.com/project/636e9b1f3e942e68b85553ae). This document (in progress) presents a mathematical model for how a Mpool will behave under different demand levels. This proposed model can simulate the process under which *(i) users submit messages to the Mpool and (ii) these messages are then included in the blockchain. This process, in turn, also simulates quantities derived from such a process, such as gas usage and base fee, as well as other network quantities that depend on them.

3. [Code base for *A mathematical model for Mpool dynamics*](https://github.com/protocol/CryptoEconLab/tree/blockSim/notebooks/blockSim)


---
### 2.2. InterPlanetary gas usage. 🟡 💡

==TODO: @7JfXCEujQwWCaFm8acpJ7A could you pls review this subsection?==

**Description.** 

IPC proposes a protocol to scale the network horizontally. This scaling, in turn, presents a significant opportunity to realize the Filecoin mission. The crypto-economic implications of these proposed changes require careful analysis to both (1) encourage innovation on the network and (2) protect the main net from unintended consequences.  

**Use case** 

Once a  Crypto economic model for the IPC has been designed and tested, one could use such a protocol to scale the network horizontally. In addition,  IPC could also be a potential long-term solution to the gas gentrification problem; in this setting, one could, e.g., dedicate a subnet to all FVM-related transactions and use the parent network for all storage-related messages. Unfortunately, however, the timelines for these projects are separate.

**Proposed steps.**
1. Agree on the objectives of the economic and gas model for IPC. This task involves agreeing with the Consensus Lab and other stakeholders on a reasonable and measurable objective function that the IPC economic mechanism must work to maximize.  
2. Identify the tunable parameters of the gas economy that can steer the hierarchy towards achieving the goals identified in (1). Establish an efficient algorithm that intakes feedback from the state of the hierarchy and adjusts the control parameters in a defined way to reach the desired target.
3. Simulation and fine-tuning. The tunable parameters identified in (2) will contain arbitrary parameters that may need to be optimized. After this step, there will be a menu of several mechanisms from which to choose a final mechanism.
4. Decide the best mechanisms for IPC economics. The output of (3) will compete for sets of parameters and rules. The final product will be an agreement on the best mechanisms and parameters to incorporate into IPC.


**Related projects**

1. FVM. IPC could be a long-term solution to the gas gentrification problem.
2. Gas Lanes. Conceptually, there is some overlap between these two projects.
3. Mpool modeling.


**Related Documents.**

1. [de la Rocha, Alfonso, et al. "Hierarchical Consensus: A Horizontal Scaling Framework for Blockchains." 5th International Symposium on Foundations and Applications of Blockchain 2022. 2022.](https://research.protocol.ai/publications/hierarchical-consensus-a-horizontal-scaling-framework-for-blockchains/delarocha2022.pdf).

==TODO @ 7JfXCEujQwWCaFm8acpJ7A Please include here a list of relevant documents. I couldn't find them on HackMD. Can also ping me on slack with them==



---

### 2.3. Beyond the EIP1559 TFM. (🟢,🔴) 💡

**Description.** 

The Filecoin network utilizes the EIP1559 transaction fee mechanism to compute the base fee $b_t$ at every epoch $t$. Under the current version of such a model, the protocol updates the base fee  according to the following formula:

$$b_{t+1}=b_t\left(1+c_t\frac{G_t-G^\text{target}_t}{G^\text{target}_t}\right),$$

where, $G_t\in[0,G^\text{max}]$ is the gas consumption at epoch $t$, which can take values between $0$ and the maximum block-size $G_\text{max}$, $G^\text{target}_t$ is the target block-size at the current epoch, currently fixed to be $G^\text{max}/2$ for any $t$, and $c_t$ is the so-called *step-size,* which is currently set to be $c_t=1/8$ for any epoch $t$. Thus, an epoch where the gas usage is above the target gas usage will create a *congestion* on the network and will increase the base fee (up to $12.5\%$ for $c_t=1/8$). This increase in base fee is intended to drive demand down in the next epochs. The opposite effect occurs whenever gas usage at a given epoch is below the target gas consumption $G^\text{target}_t$.

**Adjustable block size**


Although conceptually simple, this base fee-updating mechanism is not necessarily optimal; indeed, [one could argue](https://hackmd.io/37c7UTGbQq6MuprD23k0jw) that in low-demand periods, the block usage dynamics would deviate from what rational miners would do in a first price auction mechanism. [Our proposal](https://hackmd.io/37c7UTGbQq6MuprD23k0jw) addresses this issue by adjusting the target block size by maximizing a target function that can be chosen to maximize the miner utility or any other quantity of interest.  🟢



**Adjustable step size**

==TODO: @1dR0N2W7SQyZWg7DGB8Vfw  Shyam, would you mind reviewing here, as you're listed as a co-author in one of the references?== 
Another point of contention regarding EIP1559 mechanisms is that, while empirical findings suggest that the EIP–1559 mechanism achieves its goals on average (c.f. Empirical results for [Ethereum](https://ieeexplore.ieee.org/abstract/document/9680496?casa_token=l8_ErSrSaUkAAAAA:swwTHffCtYOS2kV5iV_v6wIuwHRrBP2Pyu7OCfSa02jaktNxQva5PPbCdi6kr2Jt6DlORgwjeo9d) and [Filecoin](https://hackmd.io/BrlCWpykSTyQyQ3HNDFqUA) ), short-term behavior is marked by intense, chaotic oscillations in block sizes, and slow adjustments during periods of large bursts in demand. [Monnot et al. (2022)](https://ieeexplore.ieee.org/abstract/document/9680496?casa_token=l8_ErSrSaUkAAAAA:swwTHffCtYOS2kV5iV_v6wIuwHRrBP2Pyu7OCfSa02jaktNxQva5PPbCdi6kr2Jt6DlORgwjeo9d), suggest to alleviate this with a variable step-size $c_t$, allowing it to take the form of an [Additive-Increase, Multiplicative Decrease (AIMD)](https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease) control term, however, there are quite a few research avenues to explore in this regard.  🔴


**Use case** 

Improving upon the current EIP1559-based TFM would simultaneously benefit users and the network, as these improvements aim at having a base fee that more accurately reflects the demand levels on the network.

**Proposed steps.**

1. Formulate the base fee updating mechanism for a variable target block size.
2. Present it to the broader community and discuss its implications and interpretation with them, gathering their feedback and incorporating it into the model. The aim here is to define a "common goal" that such a change should achieve.
3. Define a simulation environment and run several simulations in different scenarios to better understand the effects of such a change. Document observations and iterate with the community until such a common goal has been achieved, or reasonable improvement towards it has been obtained.
4. Formalise discussion, gather comments and results, and presents a Filecoin Improvement Proposal (FIP) on this issue. 
5. Repeats steps 1-4 for the adjustable step size $c_t$. 

Notice that one could, in principle, work simultaneously on tasks 1-4 and 5.  

**Related projects**

1. *Batch balancer*. The adjustable target block size project could replace the batch balancer.
3. *Mpool modeling.*


**Related Documents.**

1. [Adjustable Target Block Size for EIP 1559. A. Cortes-Cubero, CEL, (2022)](https://hackmd.io/37c7UTGbQq6MuprD23k0jw). Motivation and theoretical formulation of the base fee mechanism with adjustable blocksize. [Link to GitHub discussion](https://github.com/filecoin-project/FIPs/discussions/515).
2. [Transaction fees on a honeymoon. B. Monnot et. al, (2022).](https://hackmd.io/BrlCWpykSTyQyQ3HNDFqUA). This paper describes the AIMD control mechanism with a focus on the Ethereum network. 
3. [Transaction Fee Mechanism Design for the Ethereum Blockchain: An Economic Analysis of EIP-1559. T. Roughgarden, (2020).](https://timroughgarden.org/papers/eip1559.pdf) Work describing the game-theoretical foundations and implications of EIP1559-like mechanisms.
4. [Empirical analysis of gas usage in the Filecoin network. JP. Madrigal-Cianci, CEL, (2022).](https://hackmd.io/BrlCWpykSTyQyQ3HNDFqUA)

---




### 2.4. Batch balancer revamp. 🟡 (🚩,💡)

**Description.** 



Hyperdrive ([FIP0013](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0013.md)) introduced a new, much more efficient, method to process proofs for sectors (the *batch balancer*), in which proofs can be aggregated as a batch of proofs. This technological advance promised to increase the capacity of the Filecoin blockchain by 10X to 25X. This resulted in a sudden increase in blockchain capacity, however, without a corresponding change in demand. The sudden increase in capacity lead to a steep decrease in the base fee, which meant the total amount of tokens burnt to process transactions decreased after hyperdrive in June 2021 (c.f. [A. Cortes-Cubero, (2022, in preparation)](https://hackmd.io/37c7UTGbQq6MuprD23k0jw)). This meant that such a mechanism had to be (manually) updated through a FIP ([FIP0024](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0024.md)). This evidences the need of having a self-calibrating batch balancer, or a different mechanism that is sufficiently robust to network growth that could replace it. 


**Proposed steps.**
1. Identify a quantity of interest to be monitored. This could be, e.g., average gas consumption, network revenue, or sector onboarding cost. 
2. Perform a literature review on control systems, and optimal control, as similar issues are likely to occur in various domains. Identify several possible models. 
3. Perform several simulations, taking different scenarios into account. Some private communication with other EngRes members has highlighted the importance of this type of mechanism when the FVM is introduced. Indeed, such an upgrade may increase the frequency at which users batch their sector onboarding proofs.
4. Communicate results and iterate with the network. Gather their input.
5. Present a FIP, if deemed necessary and or beneficial for the overall network. 


**Related Projects**

1. *Adjustable target block size* (Section 2.3). Might provide an alternative solution to the issue the batch balancer is trying to solve.


**Related Documents.**

1. [FIP0013](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0013.md). FIP proposed to add a method for a miner to submit several sectors proveCommitMessage in a single one-- the batch balancer.
2. [FIP0024](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0024.md) FIP that proposed to adjust `BatchBalancer` and `BatchDiscount` to match observed network growth rate post-HyperDrive & apply mechanism consistently to both `ProveCommitAggregate` & `PreCommitBatch`.
2. [Adjustable Target Block Size for EIP 1559. *A. Cortes-Cubero,* (2022, in preparation)](https://hackmd.io/37c7UTGbQq6MuprD23k0jw). Notes on the adjustable target block size project. 
3. [HyperDrive ANOVA](https://github.com/protocol/CryptoEconLab/tree/blockSim/notebooks/batchBalancersimpleanalysis). A very simple statistical analysis investigating the effects of FIP0013 and FIP0024 on network revenue.
---
### 2.5. Gas oracles. 🟡 💡🛠️

**Description.** 
Recall that under the EIP1559 mechanism, users submit messages accompanied by a *bid* given by 

\begin{aligned}
\mathsf{UserBid}=\underbrace{\left(\mathsf{gasPremium + baseFee_t}\right)}_\mathsf{gasFeeCap}\times \mathsf{gasLimit},
\end{aligned}

where $\mathsf{baseFee}_t$ is the base fee at epoch $t$, $\mathsf{gasPremium}$ is the miner tip, $\mathsf{gasLimit}$ is an estimated upper bound on the number of gas units (computational resources) that a given message should be allowed to consume and $\mathsf{gasFeeCap}$ is the sum of $\mathsf{gasPremium}$ and $\mathsf{baseFee}_t.$ Typically, miners will prioritise the messages that have $\mathsf{userBids}$. that would maximise their profits. In periods of low demand for block space (roughly equivalent to having comparatively few messages in the Mpool), the optimal user strategy is to set $\mathsf{gasFeeCap}$ so that it barely covers the $\mathsf{baseFee}_t$, since in this case, it would be quite likely that their message will be included relatively fast. In periods of mid or high demand, however, the sender of a transaction faces a trade-off between timely inclusion and the cost of this transaction, since the higher the miner tip is, the more inclined these actors will be in including such a message. For both the Ethereum and the Filecoin network,  existing recommendation mechanisms aggregate recent gas price data on a per-block basis to suggest a gas price, however, it can be shown that these recommendations are far from optimal, rely upon fairly unsophisticated estimators (c.f. [this medium post](https://trapdoortech.medium.com/filecoin-gas-calculation-4352536e287c)), and could be subject to large variations (c.f. [Werner et. al. (2020)](https://link.springer.com/chapter/10.1007/978-3-030-53356-4_10), [Laurent et. al, (2022)](https://www.sciencedirect.com/science/article/pii/S209672092200015X) for a discussion of this phenomena on the Ethereum network, and [this post](https://filecoinproject.slack.com/archives/CSC2632KB/p1665455856223449) for an equivalent discussion for the Filecoin network).
**Proposed steps.**
1. Review relevant literature, and identify what is the current state of the art of these methods, their strengths, and weaknesses.
2. Implement relevant methodologies a publish it as a `gasToolBox` library of sorts.  Potential methodologies include Exponentially-weighted moving average, Time series forecasting, LSTM, or Bayesian forecasting.
2. Improve upon these methodologies, using cutting-edge techniques from different fields of knowledge, such as time series analysis, deep learning, and uncertainty quantification. 

**Related projects.**

1. *Mpool modeling.* useful to generate a simulation environment.

**Related Documents.**

1. [Slack conversation on this issue](https://filecoinproject.slack.com/archives/CSC2632KB/p1665455856223449).
2. [Transaction fees optimization in the Ethereum blockchain. Laurent et. al, (2022)](https://www.sciencedirect.com/science/article/pii/S209672092200015X) Previous work on gas-recommendation predictions for the Ethereum network. 
3. [Step on the Gas? A Better Approach for Recommending the Ethereum Gas Price. Werner et. al. (2020)](https://link.springer.com/chapter/10.1007/978-3-030-53356-4_10) same as above, but with a *first price auctions* focus. 
---

### 2.6. Gas lanes 🟢 💡

**Description.** 



One issue that has been brought up on several occasions is the need for and viability of so-called "gas lanes". By gas lanes, we refer to the process of (i) grouping messages into several different classes (or *lanes*), and (ii) allocating a given proportion of the block space to each different class of messages. In this setting, each lane could be equipped, at least in theory, with its own base fee updating mechanism, or even more generally, with a different transaction fee mechanism together.  While the current state of the IPC project (c.f. Section 2.2) relies upon very similar ideas, this research direction as a *standalone* feature needs to be understood in more detail, as it is, at the moment, unclear whether such a construction is beneficial or even necessary.



**Proposed steps.**
1. Determine a set of Quantities of Interest, QoI. More precisely, given the question *How would implementing gas lanes affect X?* the goal of this step is to determine meaningful quantities *X* to monitor before and after a potential gas lane implementation. An example here would be setting the QoI *X* to be *demand for block space due to the FVM upgrade*.
1. Determine how many lanes to use.  Because of its relation to other ongoing projects (c.f. Section 2.1, reference 2), one should define how many lanes or groups to consider. As an example, one could consider one lane for FVM-related messages and another gas lane for non-FVM-related messages, or a three-lane system, with one lane for FVM, messages, one for proof-related messages (e.g., `SubmitWindwedPoSt`), and one for everything else. In theory,  one could even consider sub-lanes, i.e., scenarios where each class of messages is subdivided into sub-classes and so on. 
2. Understand, via analysis and simulation the effects of such a change. Identify potentially dangerous scenarios. 
3. Communicate findings to the wider EngRes community, as well as other stakeholders in the network, and gather their feedback.
4. Assuming that introducing a gas-lane mechanic is shown to be in the best interest of the network, write down a FIP. 

**Related Projects.**
1. *FVM*. This project could be a solution to avoid or alleviate the block space gentrification problem.
2. *IPC* This shares some similarities to the IPC.
3. *Mpool model*. Useful as a simulation environment to test issues here.


**Related Documents.**

==TODO: if anyone is aware of other docs, could you pls add them or let me know?== 

1. [FIP0013](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0013.md). In a sense, this FIP added a gas lane by allowing some messages to be aggregated.
2. [FIP Discussion #430](https://github.com/filecoin-project/FIPs/discussions/430). A proposal to exempt consensus-related messages (so-called *control-plane messages*) from base fee burning.





---


### 2.7 Mpool model 🟢 🛠️

**Description.** 
The idea behind this project is to present a probabilistic model for  the dynamics of the  Message/Memory pool (Mpool) dynamics of an arbitrary blockchain. This model can be understood as a formalisation of the process under which messages  arrive at the Mpool, and are later removed from it, by being included in blocks by some miner. 
We argue that under certain reasonable conditions,  messages that arrive to the Mpool follow a non-homogeneous Poisson process, with an intensity parameter directly proportional to the demand for such a type of messages. Furthermore, we argue that, under certain conditions on the bidding behaviour of message-sending users and miners, the Mpool follows an M/G/1 process.

**Proposed steps.**

1. Determine a model for user and miner behaviour.
2. Analyse model.
3. Implement  and present toy examples.

**Related projects.**

This is a model/simulation environment, so it could be of used in most if not all gas-related projects that require some simulation. At time of writing, we are pushing towards this direction to incorporate this modeling in the upcoming FVM-related work.

**Related documents.**

1. [A mathematical model for Mpool dynamics. (CEL) (2022). *In progress*](https://www.overleaf.com/project/636e9b1f3e942e68b85553ae). This document (in progress) presents a mathematical model for how a Mpool will behave under different demand levels. This proposed model can simulate the process under which *(i) users submit messages to the Mpool and (ii) these messages are then included in the blockchain. This process, in turn, also simulates quantities derived from such a process, such as gas usage and base fee, as well as other network quantities that depend on them.

2. [Code base for *A mathematical model for Mpool dynamics*](https://github.com/protocol/CryptoEconLab/tree/blockSim/notebooks/blockSim)




## 3.  Summary


We present a table heavily summarising the discussion above. Here, The priority level $P_i$ is to be understood in decreasing order of $i$, that is, $P_0$ is an extremely high or top priority task, $P_1$ has a high priority, but is not as urgent as $P_0$, $P_2$ is not as urgent as $P_1$, and so on. 

==TODO Update and  this table look nicer==
| Name                                             	| Description                                                                                                                                                                                                 	| Proposed Steps                                                                                                                                                                                                                                                                                                                     	| Use case                                                                                                	| Priority 	| References                                                                                                                                                                                                                                                                                                        	|
|--------------------------------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|---------------------------------------------------------------------------------------------------------	|----------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| FVM and block space gentrification               	| Understand how the (likely) increase in demand for block space stemming from the FVM will affect other network quantities.                                                                                  	| 1. Identify QoIs likely to be affected by FVM.  2. Identify tools needed to investigate the effect of FVM-induced demand in 1.  3. Identify potential problems and problematic scenarios that a sustained increase in demand could present.  4. Propose and test relevant solutions.   Iterate with the community in steps 1,3 and 4.  	| mainly Filecoin, but some methodologies developed here can be extended to other blockchains.            	| $P_0$    	| [FVM1](https://hackmd.io/gV9HY4KDQluovuRr3wRKkw),  [FVM2](https://hackmd.io/GBJoWNyDQrmYo9tTgTRSFg)                                                                                                                                                                                                               	|
| Gas usage and the InterPlanetary Consensus (IPC) 	| Propose gas models for the IPC.                                                                                                                                                                             	| 1. Agree on the objectives and model.   2. Identify the tunable parameters.  3. Simulation and fine-tuning.  4. Decide best mechanisms for IPC economics                                                                                                                                                                           	| Initially only Filecoin, but could in theory be extended to any network with a hierarchical consensus.  	| $P_1$    	| [TBD]()  [TBD]()                                                                                                                                                                                                                                                                                                  	|
| Price-discovery mechanisms.                      	| Improve the way that the base fee is computed so that it optimizes some pre-defined targets. This could mean: 1. Adjusting target block size dynamically. 2. Adjusting the step-size $c_t$ in the base fee formula.  	| 1. Motivate and formulate proposed models  2. Iterate with the wider community.  3. Define a simulation environment and run several tests.  4. Present FIPs as appropiate.  Iterate with community steps 1-3.                                                                                                                          	| Any EIP1559-based blockchain (including Filecoin).                                                      	| $P_2$    	| [PD1](https://hackmd.io/37c7UTGbQq6MuprD23k0jw).  [PD2](https://hackmd.io/BrlCWpykSTyQyQ3HNDFqUA).  [PD3](https://timroughgarden.org/papers/eip1559.pdf)  [PD4](https://hackmd.io/BrlCWpykSTyQyQ3HNDFqUA)                                                                                                         	|
| Batch balancer.                                  	| Improve or replace batch balancer.                                                                                                                                                                          	| 1. Identify QoIs  2. Survey of control systems. Propose models.   3. Simulate these models on several scenarios.  4. Write down the findings. Iterate with the wider community.  5. Present FIPs as appropriate.                                                                                                                           	| Filecoin network.                                                                                       	| $P_1$    	| [BB1](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0013.md)  [BB2](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0024.md)  [BB3](https://hackmd.io/37c7UTGbQq6MuprD23k0jw)  [BB4](https://github.com/protocol/CryptoEconLab/tree/blockSim/notebooks/batchBalancersimpleanalysis) 	|
| Improving Gas Premium predictions.               	| Improve predictions for how much a user should bid in terms of tokens per gas unit.                                                                                                                         	| 1. Literature review of state-of-the-art on this topic. Learn what could be improved.   2. Implement relevant methods, and publish them as a toolbox. (No FIP required)  3. Improve upon relevant methods using cutting-edge tools & methodologies from several scientific fields.                                                     	| Any EIP1559-based blockchain (including Filecoin).                                                      	| $P_3$    	| [GP1](https://filecoinproject.slack.com/archives/CSC2632KB/p1665455856223449)  [GP2](https://www.sciencedirect.com/science/article/pii/S209672092200015X)  [GP3](https://link.springer.com/chapter/10.1007/978-3-030-53356-4_10)                                                                                  	|
| On the implementation of gas lanes               	| investigate the need for and efficiency of gas lanes.                                                                                                                                                       	| 1. Determine QoI.  2. Determine No. of lanes, and TFM on each lane.  3. Simulate the effects of this implementation.  4. Share results with the community. Iterate.  5. Present FIP as appropriate.                                                                                                                                        	| Any EIP1559-based blockchain (including Filecoin).                                                      	| $P_1$    	| [GL1](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0013.md).  [GL2](https://github.com/filecoin-project/FIPs/discussions/430).                                                                                                                                                                   	|
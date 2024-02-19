# FVM and the gas economy Work plan Q1 2023 (WIP)

## Problem definition

The deployment of FVM is imminent, and this is expected to bring large changes to the Filecoin gas economy. The variety of new applications to be deployed on FVM will bring new demand for usage of Filecoin gas. On the other hand, FVM also opens the possibility of implementing scalability solutions, which could end up absorbing demand for Filecoin gas usage.

**This research project has two main goals:**

1) To understand if (and under which circumstances) the FVM-induced changes in gas dynamics could turn out to be harmful to the Filecoin network. Particularly we need to understand the thresholds where the change in gas demand becomes a problem for Filecoin.
2) To find robust solutions to be in place, preventively, before FVM-related gas demand becomes a major problem.



## Part 1.  Understanding FVM gas-related risks

[We have already established](https://hackmd.io/7nJE364rRmeBENhK5qarjQ) that there are some thresholds of FVM-induced gas demand, where base fees become so high that it becomes a problem for Filecoin as a data storage network. Base fees that are too high may affect storage power onboarding and sector maintenance and stability.

In a similar fashion, [we have also exposed](https://hackmd.io/@cryptoecon/ByF9M4Ess) that the introduction of Interplanetary Consensus (IPC) also brings the risk of absorbing too much demand for Filecoin gas usage. Deciding when "too much demand has been absorbed", depends on what metric we use to determine the wellbeing of the Filecoin network.

IPC is now planned to be deployed fully as an FVM application, and not a Filecoin built-in actor. This implies that the risks of gas sprawl previously associated with IPC are now to be associated with FVM itself. 

The risk that FVM poses to the gas economy can be understood in terms of the **net FVM gas demand**, defined as
$$ D_{FVM}\equiv {\rm additional\,FVM\,related\,demand\,for \,Filecoin\,gas\,}$$
$$ \,\,\,\,\,\,\,\,\,\,\,\,\,-{\rm \,amount\,of\,gas\,demand\,absorbed\,by\,IPC\,and\,other\,scaling\,solutions.}$$

This net FVM gas demand can take positive or negative values. 


It is impossible to predict exactly what $D_{FVM}$ will look like in the future upon FVM launch, yet there are two possible options to explore:

1) Performing extensive data analysis and modelling to try to generate a prediction or estimate of what the future effects of FVM will be.

2) Not trying to predict the future of FVM demand, but  understanding the possible risks with all possible hypothetical outcomes. 


#### Deprioritized goal: Making FVM gas usage predictions
Our opinion is that option 2 is the most sensible path forward, and the one that will receive most of our attention during this research project.

We consider Option 1 to be a **low reward, high effort** strategy. The low reward aspect relates to the fact that any prediction we are able to generate on the possible future net FVM gas demand is bound to be highly inaccurate.

The Filecoin network upon the launch of FVM will be an incredibly complex system, with many new teams and applications with different strategies coming onboard. While we could try to do a survey of planned upcoming applications and estimate their future gas usage, each of these estimates will be inaccurate, and there will be high uncertainty, with FVM projects that may launch or fail to launch without us being aware of them. This would be a **high effort option** that would require a large amount of surveying and data analysis. 

We also consider option 1 to be **low reward**, in the sense that even if we manage to produce an accurate prediction of FVM gas usage, this may not be as valuable as spending the same effort in preparing the Filecoin network for **any** possible outcome.

This being said, when real FVM gas usage data becomes available, that will be extremely valuable in informing our models and proposed solutions. Real FVM data will help us narrow down priors and assumptions and lead to more realistic and useful solutions that can be applied adaptively going forward.

#### Primary goal: Understanding all hypothetical gas demand outcomes

We instead will spend most efforts on option 2.  This goal can be more precisely defined in terms of target/net-FVM-demand graphs. 

We need to understand if the effects of a certain level $D_{FVM}$ of net FVM gas demand will be good for Filecoin or bad for Filecoin. To determine what is good and what is bad, we need to measure a given **target function**.

A **target function** in this case is some measurable quantity that Filecoin stakeholders have agreed is a quantity that should be maximized.


Some example of possible target functions to consider are (that have risen from different conversations with different community members):

1) Engineer's target: 1/Base fee

With this target, Filecoin would always be focused on improving gas efficiency of different proofs and messages, and on increasing capacity. If this is the main target, gas Sprawl cannot be a problem, since adding more capacity would always be considered a good thing.

2) HODLer's target: Total Network Revenue

One possible network interest is to increase deflationary forces in Filecoin, by maximizing the amount of token burn. The assumption is that by reducing the amount of circulating supply through burning, each of the remaining tokens in the supply will become more valuable.

3) SP Utility: an approximate definition is derived [here](https://hackmd.io/37c7UTGbQq6MuprD23k0jw)

One could write a target function that captures the best interest of SP's. This includes balancing the occasions when they would favor, or disfavor higher base fees (Storage proofs consume significant amount of gas, so SP's would only want higher base fees if other users, like FVM are consuming more gas). This can also include optimization for other SP sources of revenue, like maximizing data deal revenue.

4) Data Utility: 

A combination of Total Network Storage Power, and Onboarding rate. Filecoin's central mission is to store Humanity's most important data. It could be argued the main target is then that the gas economy should work only towards the goal of maximizing amount data storage (whether verified real data, or storage capacity) in Filecoin.

5) Total Locked Token:

The network could try to maximize the amount of FIL that is locked, both as collateral for storage sectors, and how much is locked by all the different FVM applications.

Futhermore, given that FVM will impact (positively or negatively) the whole network (rather than a few particular groups of stakeholders), it would make sense to consider a utility function that combines all or several of the utility functions described before.  This can be done by taking a linear combination of these utility functions. An example is shown below. 


\begin{align}
\mathsf{Total\ utility}=w_1 \mathsf{HODL's\ utility } +w_2 \mathsf{user\ utility }-w_3 \mathsf{network\ burden }+...
\end{align}
where $w_1,w_2\dots$ are some given weights determined by the agreed relevance of the terms.

##### Target-$D_{FVM}$ graphs

A main outcome of this part of the research project is then to understand the possible positive or negative impacts to Filecoin that FVM launch could have. 

This could be quantified by generating a map between a given level of Net FVM gas demand, and its estimated effect to a given target function, such as those listed above. 

We present a hypothetical generic example of what these graphs will look like. On the $x$ axis we would have the net FVM gas demand, which could be positive or negative. For certain, mapped against its expected effect on the given target function on the $y$ axis. Such a graph can be generated for each of the proposed target functions above. In general for a given target, net FVM gas demand being too large either in a positive or a negative direction, would be harmful to the target, as is illustrated in this hypothetical example. There could be some optimal point in the graph where the target function is maximized. 

Obtaining or estimating such plots will require developing innovative mathematical analysis and complex system simulation techniques. 




![](https://hackmd.io/_uploads/BkcqELOos.png)


## Part 2. Understanding the solution space and making recommendations


This second portion of our research project is about understanding what can Filecoin proactively do, if net FVM gas demand turns out to reach a problematic regime.


### Maintaining status quo
The main possible solution we will investigate is simply **maintaining status quo,** or not making any changes to the gas economic mechanisms. It could be argued that since FVM has the capacity to bring high levels of gas demand, as well as absorbing high levels of gas demand from Filecoin, in the free market these two forces might organically cancel each other. 

The main argument against this free market approach is that there may be too much market inefficiency, inelasticity, and uncoordination.

**Inefficiency**: Even if there is a market induced need, from having excessive gas demand, or excessive gas supply, and thus economic incentives exist for solutions to organically arise, this may not happen efficiently enough, and the network may be stuck indefinitely in a suboptimal state.

**Inelasticity**: If there is an excess of gas demand or gas supply, the free market may not be able to swiftly compensate in the other direction. For example, if too much gas supply has been made available through L2 scaling solutions, the low transaction fees may induce some additional amount of demand, but this may not necessarily happen. Additional gas demand may not simply appear because it is induced.

**Uncoordination**: Maximizing the targets described above, is a matter of **working together for the greater good**. These are targets that may be deemed as positive for the Filecoin network as a whole. These targets, however, may not represent the utility of an individual Filecoin agent, who may maximize their own utility, even if this is contrary to the network target function. Unregulated free markets like this then may be succeptible to falling into *[tragedies of the commons](https://online.hbs.edu/blog/post/tragedy-of-the-commons-impact-on-sustainability-issues#:~:text=The%20tragedy%20of%20the%20commons%20refers%20to%20a%20situation%20in,British%20writer%20William%20Forster%20Lloyd.)*, in the lack of an external force aligning the incentives of individuals with the greater good.

### Block Balancer
The second main alternative we will be investigating is the set of mechanisms we will collectively call the **Block Balancer** (this is named in analogy to the Batch Balancer, a mechanism which the Block Balancer would seek to replace). We define the Block Balancer as a combination of an [adjustable target block size]() plus separate gas lanes for storage-related messages and FVM messages.

The **adjustable target block size** is a proposed mechanism that adjusts the target block size, (which we call $B_T$) used in the EIP 1559 base fee formula, in a way that maximizes a given target function. 

Adding to the adjustable target block size, gas within the block can be explicitly allocated between storage related and general FVM messages. The adjustable target block size is then split by an **allocation parameter,** $a\in[0,1]$, such that storage related messages would have a target block size, $aB_T$, and FVM messages would have a target block size $(1-a)B_T$. The allocation parameter, $a$, could also be adjusted in a way that maximizes the given network target.

The general principle here is that if $D_{FVM}$ enters a harmful regime, where it is too large (in a positive or negative direction), the effects can be countered, and perhaps $D_{FVM}$ could be reduced by increasing the parameter, $a$, and allocating less amount of block space to FVM.

A key aspect of this line of research is then understanding the effectivenes of the Block Balancer mechanism, over the default approach of doing nothing, in regulating the potential negative effects of net FVM gas demand. 


Importantly, to recommend the Block Balancer as a solution, it not only needs to perform better than the free market approach, but has to perform *significantly* better, to overcome the advantage of the simplicity of the 
"status quo" approach.


Within the Block Balancer approach, there is also a large amount of room for mechanism optimization and optimal parameter choice. A final recommendation resulting from this research project would also involve a recommendation on the best possible mechanisms and parameters for a Block Balancer that maximizes the network target.




## Work Plan and Milestones

This project is expected to be completed by the beginning of Q2 2023. It will also be the main project and occupy the majority of the resources of [AX](@7JfXCEujQwWCaFm8acpJ7A)  and [JP]( @-e2UbSEIRjClRu9Dz4XIQw  ) (CryptoEconLab) for this period.

##### Week 1-2 (Jan 23- Feb 3)

* Drive  discussions with FVM and ConsensusLab, spreading awareness of the risks of gas gentrification and sprawl, as well as collecting direct feedback and insights, on expected gas usages and timelines.

* Developing mathematical and simulation techniques needed to understand effects of $D_{FVM}$ on possible target functions.

* Generating target-$D_{FVM}$ graphs for simpler to simulate targets, such as the Engineer's and the HODLer's targets, defined above.

##### Week 3-4 (Feb 6- Feb 17)

* Drive more community discusion about understanding the possible target functions we could choose to maximize. Communicating to different stakeholders the need to align on a given target.

* Generating target-$D_{FVM}$ graphs for more complex targets, such as SP utility (including properly defining SP utility), as well as Data utility (understanding effects of the gas economy on data onboarding).

* Publish a report containing the set of target-$D_{FVM}$ graphs, and explaining the significance relative to FVM launch.

* Publish a general audience Blog/short communication on the subject of FVM related gas risks.

##### Week 5-6 (Feb 20-Mar 3)

* Developing simulations to understand the effectiveness of *maintaining status quo*, in response to FVM gas risks. 

* Publishing report on the *maintaining status quo* approach, elaborating on the existing set of incentives, potential *tragedies of the commons*, and our best estimates of the free market's capability to self-regulate.

##### Week 7-9 (Mar 6-24)

* Continue to gather community feedback on possible important network target functions.

* Exploration of mechanism and parameter space of the Block Balancer approach.

* Classifying different possible mechanisms that could be used to update $B_T$, and $a$, by maximizing a given target function (using the set of target functions that will have been generated through community discussion).

* Running simulations to test which Block Balancer mechanisms perform better at regulating FVM gas demand risk, and finding optimal set of parameters, which may differ with different choices of target functions. 

##### Week 10 (Mar 27-Mar 31)

* Publish final report, including list of official recomendations (either maintaining status quo, or a given Block balancer mechanism), the recommendation may vary with the given target function chosen.

* Publish a general audience Blog/short communication on the outcomes of the research project, and official recommendations.

##### Week 11 and beyond

* Drafting and promoting a FIP for a Block Balancer implementation, if this turns out to be our official recommendation.

* Continue to drive community discussion and alignment. Generating a viable target function through community discussion. 



## Risks

* A large risk of prediction inaccuracy has been eliminated by deprioritizing the approach of trying to predict what will be the net gas demand from FVM after launch. 

* Understanding the effect that a given value of $D_{FVM}$ has on a target function will involve a number of assumptions to be able to run a simulation. There is always the risk of assumptions having been too oversimplified, or inaccurate, leading to a misleading result.

* There is a large risk of community misalignment. Gas fee burning is a sensitive economic issue, where different network stakeholders may have different strong opinions. Trying to align the network to obtain a viable network target to optimize may prove a very difficult task. In any case, we plan all of our reports to include several possible target functions, providing different options, rather than making final choices ourselves.

* There is a risk that this research project may be too late, as FVM is expected to launch before this project is finalized. This is not expected to be a very large risk, since the effects of FVM on gas demand may not be felt immediately upon launch, but may accumulate over a longer period of time. 


## Modeling approach [WIP]



 

Any economic modelling of network behaviors will involve a number of assumptions, which will never be perfectly accurate. Our goal is to maximize the accuracy of our assumptions, while beign constrained by computational complexity and explainability of the models. 

We propose foscusing our modeling efforts into (1) demand, (2) target function reaction, (3) uncertainty, and (4) solution exploration and testing. In order to make our models as useful as possible, we believe it is necessary to regularly (and often) interact with other stakeholders from Product, Engineering and Research. 

**Remark.** From a scientific point of view, the types of models and analysis required here fall into one of the two following paradigms: 

- *Apriori.* These are models/estimates that are obtained before any data has been observed. They typically rely upon expert information. In our case, this information translates into the estimates, pre-launch data, and opinion that our colleagues from product and engineering might have regarding the usage of FVM.  

- *Aposteriori*. These are models/estimates that are obtained once data is available (i.e. after FVM launches). They are data-driven and as such they are in general more accurate, but would require FVM data, which is not available at the time of writing.   




**Demand, $D_\text{FVM}$.** 

We will need to define a concept of total demand, as shown below.

\begin{align}
\mathsf{Total \ demand}=\mathsf{status\ quo\ demand}+\underbrace{\mathsf{FVM \ demand}}_{D_\text{FVM}}
\end{align}

We can accurately model and estimate the $\mathsf{status\ quo\ demand}$ (i.e., pre-FVM demand) in several different forms; indeed a quick back-of-the-envelope calculation estimates this demand to be, on average, about 30% of the total block space. The crux here is to model $\mathsf{FVM \ demand}$. We envision the following approaches:

**Simplified approach (Apriori, lower effort, less explainability)**. A simple approach (that could also be considered as a first step), would be to consider a pre-defined model for demand of the form:

\begin{align}
\mathsf{FVM \ demand}=a_t \times \mathsf{status\ quo\ demand}
\end{align}

with $a_t$ a scaling parameter (either positive or negative) ranging from -1 (so that when $a_t=1,$ $\mathsf{total \ demand}$ is 0) to some positive value $A$. The goal here would be to test different values of $a_t$; either as constants or as a function of time, $t$.

A potential improvement over this model would be to consider several predetermined functional relation $f$ between FVM and status-quo demand.

**Advanced approach (Aposteriori, higher effort than previous, potentially more explainability)**

Once data for FVM usage in mainnet is available, we could leverage our knowledge of Machine Learning (ML) methodologies to approximate a function $\hat{f}$ such that

\begin{align}
\mathsf{FVM \ demand}=\hat{f}\left(\mathsf{status\ quo\ demand}\right).
\end{align}

That is, instead of supposing a predetermined functional relation we try to recover that functional relation (if any). This can also be extended to take other variables into account.  Furthermore, having obtained some historical data, one could try to forecast and simulate, using traditional methods from time-series analysis. 

**Target Function.** As mentioned earlier in this document, there are several possible definitions of target function. 

The main question here is understanding what would be the impact of the different levels of demand on the target functions. Some of these targets are easier and more deterministic than others. 

For instance, for the *engineer's* target, We need a mechanism to predict how different levels of gas demand translate into changes in the base fee. We have previously used a simple mechanism for understanding such relationships [here](https://hackmd.io/@cryptoecon/B10RGzlHo). The key assumption is defining some probabilistic distribution describing the value that users are likely to give to a given transaction, or how much a given user would be willing to pay for gas. Such a distribution may be fitted from existing gas usage data, but would be much improved after considering real FVM gas usage data. With these distributions, modeling different mempool sizes as inputs, it is possible to compute the resulting base fees.

The same tools allow us to examine the total network revenue as a target, once we are able to compute the base fee corresponding to a given level of demand, that can be combined with the amount of gas used to compute total network revenue.

When considering SP utility or Deal revenue as targets, some elements need to be added to the model: understanding total SP revenue, wealth and token burning rates, as well as constructing a data-based probabilistic model of the relationship between gas demand and demand for data deals.




**Uncertainty.** This modeling component comes from the observation that it is impossible to predict gas usage in the future based on current information with absolute certainty. However, while this cannot be accurately predicted, gas usage patterns can be studied. An example of this is shown below, where we investigated gas usage patterns in the Filecoin network  (relative to block space) . From there, we can already see that there are well-defined statistical properties for this usage. A full report with this information can be found [here](https://hackmd.io/BrlCWpykSTyQyQ3HNDFqUA).

![](https://hackmd.io/_uploads/S1J9llyhi.png)


Thus, once demand and targets are modeled, we will aim at estimating gas usage patterns stemming from this demand. Given this, we can quantify how this randomness trickles down into the target utility functions via Monte Carlo simulations. 

**Solution exploration and testing.** Given the first three modeling components mentioned above, one can then develop a set of testing scenarios that would, to some extent, approximate the behaviour of FVM demand, and its expected effect in the target function. Thus, we can start comparing some of the aforementioned proposed solutions, such as gas lanes, demand-driven pricing  (as proposed [here](https://github.com/filecoin-project/FIPs/discussions/587)), etc. 

A useful resource in this setting is the recently-published manuscript [*"Dynamic pricing for non-fungible resources".* By Theo Diamandis, Alex Evans, Tarun Chitra, and Guillermo Angeris. *arXiv preprint arXiv:2208.07919 (2022)*](https://arxiv.org/abs/2208.07919). This work presents a theoretical framework for both gas lanes as demand-driven pricing. The CEL has recently distilled this paper [here](https://www.overleaf.com/read/stycwnqscdtr) and in a mini seminar video [here](https://www.youtube.com/watch?v=kXpf2kGrPgE)

**Maintaining Status Quo.** The first possible solution to explore is simply understanding *maintaining status quo*, that is understanding the free-market's ability to maximize given targets.

To understand this, we must understand the incentives and utility functions that exist for different Filecoin agents: SP's, data clients, FVM developers and application users. The assumption to model the free market is that every agent will be acting in a way that generally maximizes their own utility. 

Once we formulate the different utility functions and expected behaviors, a given level of net FVM gas demand can be used as an initial state for the system, after which different Filecoin agents will act in a way that maximizes their utility. We can then examine what is the final state, or final net FVM gas demand that these expected behaviors lead to. This can then be translated into the given target functions, where we could examine what was the effect of free market dynamics on the target we sought to maximize.

**Block Balancer** Here we would assume that there is a mechanism that has explicit control over the target block size and allocation of block space between storage messages and FVM messages. Using this mechanism, and incorporating the expected behaviors of different Filecoin agents, we can again use a given net FVM gas demand as an initial state input, and examine what would be the final state, determining how effective (and how much more effective than the free market) is the block balancer at maximizing a given target. 
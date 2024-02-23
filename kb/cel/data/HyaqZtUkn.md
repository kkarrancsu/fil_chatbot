---
tags: Gas, Research proposals, Almanac
---


# Gas lanes.


## TL;DR
While we believe that *gas gentrification*  is unlikely to occur at the early stages of FVM launch, we see a lot of value in understanding, proposing and testing possibles mitigation strategies. Motivated by this, we investigate the idea of so-called *gas lanes* as a potential solution to the *gas gentrification issue*. We also discuss possibles extensions to the proposed model, and we also identify some potential drawbacks from the proposed solution.  


## 1. Introduction 

The Filecoin Virtual Machine (FVM) is quickly rising in popularity and it is posed to attract a larger and much welcome user base to the Filecoin network. However, one as-of-now hypothetical, but serious scenario that this larger user base might bring is what we call *gas gentrification.* In short, this refers to the phenomena where demand for FVM-related messages is so high that  either (i) it drives the base fee upwards to a point where it might become difficult for some miners to submit network-critical messages (such as onboarding, sector recovery of proofs of storage)  or (ii) that FVM users are simply willing to pay significantly higher tips to get their messages included, and thus pricing out some storage providers. Either case (which again, are purely hypotethical as of the time of writing) is a scenario that could potentially harm the network. 

In this writeup we investigate the idea of so-called *gas lanes* as a potential solution to the *gas gentrification issue*. *Gas lanes* (also known as *multi-dimensional gas*) refer to the idea of dividing the block space into multiple parallel *lanes*, each with its own target block size, gas limit, and EIP1559-like pricing mechanism.  In this setting, each lane would be intended for a specific type of message, such as, e.g., network-related maintenace messages, data onboarding, or FVM-related messages, and each type of message will be priced according to the resources consumed in each lane.  

We present two examples to illustrate the point. We emphasize that the values taken in those examples are purely chosen for illustration purposes, and are not to be understood as a specific recommendation. 
 
 ---
**Example I.**

Let's say that we introduce two gas lanes:

- FVM lane: 30% of the maximum block size, with a target of 15% of the maximum block size. This includes FVM related messages such as `invokeContract`. 
- Status-Quo lane: 70% of the maximum block, with a target of 35% of the maximum block size. This lane wouls include all other non-FVM messages such as `SubmitWindowdPost`, as well as  the recovery messages. Essentilly, it would correspond to the Filecoin network pre-FVM. 


---

**Example II.**

Let's  now consider a case with three gas lanes:

- SP maintenace lane: 20% of the maximum block size, with a target of 10% of the maximum block size. This would include messages such as `SubmitWindowdPost`, as well as  the recovery messages.
- Data onboarding lane: 50% of the block, with a target of 25% of the maximum block size. This lane would include messages such as `PreCommitSector`, `ProveCommitSector`, `PreCommitBatch` and `ProveCommitAggregate`.
- 'Others' lane: 30% of the max. block size, with a target of 15%. This lane would include all other types of messages, including all FVM-related messages.

---
**Remark.** *It might not always be straightforward to identify the difference among these messages (e.g., an FVM contract that takes care of SP maintenance messages); and as such one needs to be careful with the classification.*



In this setting, the network would identify the lane each message belongs to, and miners will process messages in each lane according to their given preference (e.g., in descinding order of tips). If a lane runs out of gas before all the messages are processed, the remaining messages would be processed in the next block for that lane.


 Once messages are packed, the base fee for each lane would be adjusted dynamically based on the demand for that particular lane. For example, if the 'Others' lane is experiencing high demand, the base fee for that lane would increase, making it more expensive for senders to submit messages to that lane. This would help balance the demand for each lane and ensure that the network operates efficiently. **Intuitively, it will also solve the issue of having FVM users "pricing out" miners from their maintenance messages, as these messages are in two separate and independent lanes**


Overall, a version of the Filecoin 1559 mechanism that utilizes gas lanes intended for specific types of messages would aim to improve the efficiency and throughput of the network by allowing for more granular fee adjustments and better responsiveness to changes in demand for specific types of messages. However, there is no free lunch and this would also require careful design and testing to ensure its safety and reliability. We also remark that is also not immediately clear for us at the CEL how technically challenging the implementaiton of such a mechanism would be. 



The rest of the writeup is organized as follows. We introduce the proposed model in Section 2. In particular, we argue how a simple Transaction Fee Mechnism (TFM) with gas lanes can be constructed as an extension of the EIP1559 TFM. In Section 3 we discuss several extensions and generalizations to the proposed model. We present a critique of the proposed mechanism in Section 4, and mentioned some related works in Section 5. 

## 2. Model.

We begin by stating a perhaps obvious, but important (and not so innocent) assumption.

**Assumption 1.**  *There are $L\in\mathbb{N}$ different classes of messages, and each message belongs to exactly one class $c_\ell$, $\ell=1,2,\dots,L$, i.e., no message can belong to two or more classes.*


**Remark.** The previous assumption requires carefully classifying messages as the line thaty separates different classes of messages can become blurry. An example of an edge case is where we have two classes of meesages: FVM and non-FVM (e.g., network maintenance), and an FVM user invokes a contract that takes care of maintenance-related tasks, such as `submitWindowedPost`. This classification is worth discussing in more deailt with the wider community. 


We present a simplified model for gas lanes, and discuss several possible extensions in the next Section.

Let $t\in\mathbb{N}$ denote the *epoch number*,  $L\in\mathbb{N}$ denote the number of gas lanes, and let $B_\text{max}\in\mathbb{R}_{> 0}$ and $B_\text{target}\in\mathbb{R}_{> 0}$ denote the *maximum* and *target* block sizes, respectively. In our simplified model, we split the block $B$ into $L$ **non-overlapping gas lanes**. Each lane $\ell=1,2,\dots,L$ is defined so that it has a *maximum width,* $w_\ell$, and a *target width*, $B_{\text{target},\ell}$ where


\begin{aligned}
\sum_{\ell=1}^L w_\ell&=B_\text{max}\\
\sum_{\ell=1}^L B_{\text{target},\ell}&=B_\text{target}\\
\ell_i&\leq w_i, \quad \forall \ell=1,2,\dots,L.
\end{aligned}

In addition, to each lane $\ell=1,2,\dots,L$, there corresponds a *gas utilization at epoch $t$ denoted by $G_{\ell,t}\in[0,w_\ell]$* (which clearly implies that  $\sum_{i=1}^N G_{\ell,t}\leq B_\text{max}, \ \forall t$) and a *base fee* $p_{\ell,t}$. 

This version of the EIP1559 mechanism with gas lanes then proceeds as follows.


We propose to equip each lane with its own EIP1559-like transaction fee mechanism. Thus, the base fee at lane $\ell$ is updated on an epoch-to-epoch basis according to:

\begin{align}
p_{\ell,t+1}=\underbrace{\max\left\{p_{\ell,t}\left(1+\frac{1}{8}\frac{G_{\ell,t}-B_{\text{target},\ell}}{B_{\text{target},\ell}}\right)
, p_{\ell}^\text{min}\right\}}_\text{$:=H_p(p_{\ell,t},G_{\ell,t},p_\ell^\text{min},B_{\text{target},\ell})$}, \tag{1}
\end{align}


with $p_{\ell}^\text{min}\in\mathbb{R}_{>0}$ the minimum base fee to be paid per lane. At the time of writing, (i.e., with $L=1$) this minimum is set to $p_{\ell}^\text{min}=100$attoFIL$=10^{-16}$FIL.

Given this, the proposed multi-lane EIP1559 mechanism would proceed as follows:

1. For each class of message $c_\ell=1,2,\dots,L$:
    - Miners select the messages of class $c_\ell$ that they would like to include, according to their strategy $\mathsf{S}$, taking into account the the maximum block size for this class of messages is $w_\ell$ and the target utilization is $B_{\text{target},\ell}$. The total gas limit from each class of message is given by $G_{\ell,t}\leq w_\ell$. 
2. The base fee for each lane gets updated according to the price-update function in Equation (1). 


Under the scenario outlined above, we would need to define $3\times L$ parameters, namely $\{w_\ell,B_{\text{target},\ell},p^\text{min}_\ell\}_{\ell=1}^L$. **These parameters would need to be defined from the begining of the implementation, and might need to get adjusted over time.** 

Intuitively, a properly chosen lane width $w_\ell$ and lane target $B_{\text{target},\ell}$, can help us overcome the potential issue of Storage Providers being priced out; indeed, since gas lanes are non-overlapping and the base fees of each lane is independent of the others, a lane whose target is bigger than the average gas usage for that specific type of lane will almost never result in a gas gentrification issue, however, one needs to be careful to not give too narrow lanes (and hence, overcharge) other users. 

In addition, **preliminary** experimental results, where we used a demand-driven, agent-based system to simulate the version of gas lanes presented in **Example I** above (in a scenario where there's a comparable amount of gas demaded by either actor)  *suggest* that gas lanes do indeed provide a safety net of sorts to the miners. Naturally, we will expand on these models and experiments once input from other stakeholders has been obtained. 

![](https://hackmd.io/_uploads/ryIeY4xx2.png)



## 3. Possible extensions.

### 3.1 Variable lane width. 

Instead of defining a fixed lane width $w_\ell$,  we can alternatively use a mechanism that adjusts the lane widths based on the utilization rate of each lane. For simplicity, let's suppose throughout that $B_{\text{target},\ell,t}=w_{\ell,t}/2$. We present two examples of how to implement this. 


**Example III.** Consider a scenario with only two lanes; one for the network maintenance, (say $\ell=1$) and one for all FVM-related messsages ($\ell=2$). Intuitively, we can expect the number of mainentance messages to grow with the network Quality Adjusted Power (QAP). Thus, one alternative in this case would be to make

\begin{aligned}
w_{1,t+1}&=\max\left\{w_{1,t}\left(1+\alpha \frac{\textsf{QAP}_t-\textsf{QAP}_{t-1}}{\textsf{QAP}_{t-1}}\right), B_\text{max}\right\},\\
w_{2,t+1}&=B_\text{max}-w_{1,t+1}.
\end{aligned}

for some suitable value of $\alpha$. Notice that the time indices in the previous equation can also be taken as moving averages over some given number of epochs $T$.  This approach has the advantage of being quite straightforward, once $\alpha$ has been defined. 

Notice that if the network becomes so large that $w_{2,t+1}\ll w_{1,t+1}$, there's a clear scalability issue (as this would mean that the network maintenance is taking almost all available resources) and as such we would need to resort to layer 2 solutions.

**Example IV.** We now consider a slightly more abstract example. Let $\pi_{\ell} \in(0,1)$ be a *priority factor* for lane $\ell$, where a higher value indicates higher priority for messages in lane $\ell$. Given this, one could update $w_{\ell,t}$ on an epoch-to-epoch basis using the following procedure. 

1. Once mesages have been included in a block, we compute an *adjustment factor* for each lane, $A_{\ell,t}$ defined as 
\begin{align}
A_{\ell,t}:= \pi_\ell \left(\frac{G_{\ell,t}-B_{\text{target},\ell}}{B_{\text{target},\ell}}\right).
\end{align}
 

2. Update widths according to 
\begin{aligned}
w_{\ell,t+1}:=\frac{w_{\ell,t}(1+A_{\ell,t})}{\sum_{\ell'=1}^L w_{\ell',t}(1+A_{\ell',t})}\cdot B_\text{max}.
\end{aligned}

When congestion levels rise in a particular lane (i.e., the ratio $\frac{G_{l,t}}{B_{\text{target},\ell}}$ is greater than 1), the adjustment factor $A_{l,t}$ becomes positive, leading to an increase in the width of that lane. This increased width allows more transactions to be included in that lane, effectively lowering the gas fee for that lane. As a result, storage providers in that lane would have a lower chance of being priced-out due to high gas fees.

On the other hand, if a lane's congestion level drops (i.e., the ratio $\frac{G_{l,t}}{B_{\text{target},\ell}}$ is less than 1), the adjustment factor $A_{l,t}$ becomes negative, leading to a decrease in the width of that lane. This decreased width results in a smaller number of transactions being included in that lane, effectively increasing the gas fee for that lane. However, since the sum of lane widths is kept constant at $B_\text{max}$, the capacity that is removed from this lane will be reallocated to other lanes with higher congestion levels. This reallocation helps maintain a balance between the lanes, ensuring that storage providers have a fair chance of being included in the network without being priced-out by other users. 


### 3.2 Variable target block-size.

Alternatively, one could fix the lane widths at every epoch (effectively setting $w_{\ell,t}=w_\ell$) and change the target lane size $B_{\text{target},\ell}$ so that at eavery epoch the network is optimizing a predefined objective. This mechanism is discussed in detail [here](https://hackmd.io/@cryptoecon/B10RGzlHo?type=view). 



### 3.3 Choice of update rule.

In addition, one could also implement each lane with its own different EIP1559-like update rule. Some alternatives are, e.g.,

**Exponential.**  Defined as

\begin{align}
p_{\ell,t+1}=\max\left\{p_{\ell,t}\exp\left(a\frac{G_{\ell,t}-B_{\text{target},\ell}}{B_{\text{target},\ell}}\right),p^{{\text{min}}}_\ell\right\}
\end{align}

**Geometric average.** as 


\begin{align}
p_{\ell,t+1}=\max\left\{p_{\ell,t}\left(1+\frac{1}{8}\frac{\widehat{G}_{\ell,t}-B_{\text{target},\ell}}{B_{\text{target},\ell}}\right),p^{{\text{min}}}_\ell\right\}
\end{align}

with $\widehat{G}_{\ell,t}$ the  geometric average of the gas consumption. 

In either case, it can be shown that using these update rules, while computationally more expensive, can help securing the network against some  weakly-coordinted potential attacks as discussed in [this potential FIP](https://hackmd.io/@guy-goren/r1RVuou0j).



## 4. Critique and topics to discuss.

Naturally, we are aware that the model presented is not perfect, and there are a few issues to discuss with the community.

**Added complexity.** One potential drawback of the gas lanes model is the added complexity it introduces, as miners and users need to manage lane-specific parameters, such as lane widths, base fees, and target consumptions. This complexity could make it more difficult for users to estimate transaction costs and for miners to efficiently select transactions. Additionally, the gas lanes model might require more frequent monitoring and updates to keep lane parameters in line with the network's current state. This could lead to increased overhead for network operators and a higher chance of suboptimal adjustments if the monitoring and updating processes are not executed effectively.

 **Lane definition.** The number of lanes $L$ in the proposed model needs to be carefully defined. Indeed, one could consider having e.g., 2 lanes, one for FVM messages and one for non-FVM, or 3 lanes, one for onboarding, one for PoSt, and one for everything else (including FVM), or many other choices. Furthermore, the choice of $L$ can have a significant impact on the efficiency and flexibility of the network.
 A larger number of lanes allows for finer granularity in segregating transactions based on factors such as gas prices or priority levels. This in turn could lead to a more efficient allocation of resources and better handling of congestion. However, increasing the number of lanes can also result in added complexity for both miners and users, making it more challenging to determine the optimal lane for a transaction or to adjust lane parameters effectively. Therefore, when choosing the number of lanes, it is essential to strike a balance between granularity and simplicity to maintain efficient network operation.

**Non-identifiability.** This is the scenario where it is not immediately obvious whether a message belongs to a given class or not.  In the 2 lane case, for example (FVM Vs. Maintenace), a contract that takes care of submitting maintenance would be difficult to classify in either group. This distinction would need to be analyzed in detail.

**Multi-dimensional knapsack problem solved by the miners.** Introducing gas lanes results in a "multi-constraint" knapsack problem for the miners when deciding which blocks to pack (in the setting where they want to maximize miner tips). This problem is NP-hard, which means finding an optimal solution can be computationally intensive. However, miners can employ heuristic or approximation algorithms to obtain near-optimal solutions within reasonable time frames. These algorithms can consider factors such as transaction fees, gas prices, and priorities to create a balanced and profitable block, however, it is unclear to us if this would represent a significant techincal challenge. 


## 5. Related work.
1. Resource pricing. Anorth has recently proposed a *similar* (but not quite the same) idea [here](https://github.com/filecoin-project/FIPs/discussions/587). The idea of segregating and pricing messages according to the type fo resources they consume has been studied in the  recent work [Dynamic Pricing for Non-fungible Resources: Designing Multidimensional Blockchain Fee Markets](https://arxiv.org/abs/2208.07919) by Theo Diamandis et. Al. 






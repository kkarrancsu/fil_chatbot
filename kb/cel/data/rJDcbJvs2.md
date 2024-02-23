# Gas Lanes: Exploring the Design Space

**Author**: Juan P. Madrigal-Cianci @CryptoEconLab 

*(Questions or comments? @JP in PL/Filecoin slack)*

This document delves into the critical design choices and parameters for implementing gas lanes in a blockchain system. In particular, we explore three main design aspects: inclusion flexibility, lane-adjusting mechanisms, and the choice between multi-fee and discounted/adjusted gas lanes. 

**Remark:** For the sake of readability, the *math-heavy* parts have a text box explaining, in plain English, the intuition and implication of the equations being discussed. 

<div class="warning" style='background-color:#E9D8FD; color: #69337A; border-left: solid #805AD5 4px; border-radius: 4px; padding:0.7em;'>
<span>
<p style='margin-top:1em; text-align:center'>
<b>Executive summary </b></p>
<p style='margin-left:1em;'>
Our analysis leads to the following recommendations:

- *Inclusion Flexibility*: We recommend adopting a flexible approach, allowing messages to be included based on available block space rather than enforcing rigid lane widths. This enhances message inclusion while necessitating adjustments in the target gas usage mechanism to control fee growth.
- *Lane-Adjusting Mechanism:* A proportional allocation based on Raw Byte Power (RBP) emerges as a suitable choice. This mechanism adjusts lane sizes based on the network's health and prioritizes messages effectively. However, we remain open to alternative proposals that provide more precision.
- *Multi-Fee vs. Discounted/Adjusted Gas Lanes*: We highlight the isomorphism between the two mechanisms under specific adjustment factors. While multi-fee lanes provide fairness and revenue, discounted/adjusted lanes might offer a simpler user experience. The choice depends on whether a pure discount mechanism is desired.
- **Call to Action  for Stakeholders & next steps.**
We invite stakeholders to engage in a collaborative discussion to refine these design choices and parameters. Once there is alignment in the design space, we will start (co) writing the FIP. Parallel to this, we intend to run numerical simulations to verify that the proposed design does not induce any undesirable behavior, such as significantly increasing the variance of the base fee, rendering unsustainably large base fees, etc. 
</p>
</p></span>
</div>
 





## Main setting
Consider a block of maximum block size $B$ and $L\geq 1$ different *gas lanes.* In our setting, we embrace the concept of "one message, multiple lanes," where every message *taps* into gas from several lanes based on its components.


In particular, we treat a message $m$ as a set of $N_m\geq 1$ *instructions* (or OpCodes) $m=\{c_{i_j}\}_{j=1}^{N_m}$. Here, each OpCode $c_{i_j}$ consumes a specific amount of gas $g_\ell(c_{i_j})$ of a unique, specific, lane $\ell$. Thus, any given message consumes $G^m_\ell$ gas units, with $G^m_\ell$ understood as the sum of the gas consumed by the OpCodes that execute on the lane $\ell$. This is illustrated in the figure below. 

![](https://hackmd.io/_uploads/HJdhVJm9h.png)

In our design, a message can only be included in a block if **all** the OpCodes forming the message fit within their designated lanes (i.e., if there's enough gas available on each lane).

However, there are multiple ways of implementing this; one must decide on specific design elements and parameters:



**Design**
- ***Inclusion flexibility.*** Which relates to whether we include and enforce maximum lane widths.
- ***Lane-adjusting mechanism**.* Which describes how the width of each lane changes from epoch to epoch.
- ***Multi-fee vs. discounted/adjusted gas lanes***. Which describes the underlying transaction fee mechanism of each lane. 

Each of these design choices has its own set of parameters; however, regardless of the choice of design, one also needs to decide on the number of lanes and the (initial) lane widths.


In what follows, we delve deeper into these aspects.

 

## Diving Deeper

We now discuss these design choices in more detail. A table summarising that discussion is shown below. 

| Design Choice | Pros | Cons | Additional Parameters | Recommendation |
|---------------|------|------|-----------------------|----------------|
| **Flexibility in Inclusion** | | | | |
| Rigid | - Better control over base fee changes | - Limited opcode inclusion flexibility<br> - Potential missed message inclusions | - Maximum lane width<br> - Target gas usage | Prioritize base fee stability|
| Flexible | - Greater flexibility in message inclusion | - Requires additional parameters to control base fee | - Target gas usage adjustment mechanism |Prioritize message inclusion|
| **Lane Adjustment Mechanisms** | | | | |
| Fixed | - Simple solution | - Requires periodic adjustments | - Initial priority factors | Useful for initial or temporary setups but not long-term due to its static nature. |
| Proportional Allocation (RBP-based) | - Reflects network status<br> - Can prioritize important messages | - Might need frequent recalibrations | - Linear regression coefficients<br> - Min/Max priority widths |  Suitable for networks where certain messages correlate well with network size. |
| Gas-based Dynamic | - Auto-adjusts based on demand | - More unpredictable<br> - Might lead to oscillations | - Look-back period<br> - Max adjustment factor<br> - Min lane width | Useful for highly fluctuating demand dynamics |
| **Multi-fee vs Discounted Gas Lanes** | | | | |
| Multi-fee | - Fair pricing for each lane |  - Potential fee disparity | - Pricing mechanism per lane<br> - Dynamic fee adjustments | Clear breakdown of price |
| Discounted Gas | - Incentivizes specific transactions or users <br> - Can be made pure discount  | - Potential revenue loss (if pure discount) | - Discount rate<br> - Criteria for qualifying transactions/users | More useful if we want a strict, pure discount mechanism |



### Flexibility in Inclusion
This refers to determining if a maximum lane width (besides the maximum block size) is required or if we should aim for a target usage. For simplicity, imagine every lane having an EIP1559-like transaction fee mechanism. As we will see, the former choice offers more control over the growth of the base fee at the cost of potentially excluding some messages, while the latter does not run into this inclusion but necessitates additional parameters in order to control the growth of the base fee. 

- **Rigid.** In this setting, each lane has a *fixed maximum lane width* $B_\ell ≤ B$ (with equality only if `L = 1`) **and** a *target gas usage* $B_\ell^*$. The latter could, for instance, be set at $B_ℓ^* = B_\ell / 2$. Under this setup, opcodes of class $\ell$ can use up to $B_\ell$ gas units (i.e., it holds that $G_{\ell,t}\leq B_\ell$ for any epoch $t$). This ensures better control over base fee changes. However, the downside is limited flexibility in opcode inclusion, which could lead to missed message inclusions. Indeed, notice that setting $B^*_\ell:=\alpha B_\ell$, for some $\alpha$ taking values between 0 and 1, implies that the base fee $b_t$ increases **by at most** $100\times\frac{1-\alpha}{8\alpha}$% on an epoch to epoch basis, and decreases by at most 12.5% at each epoch. Indeed, to see this, notice that since $G_{\ell,t}\leq B_{\ell}$,  one then has that
\begin{aligned}
b_{t+1}&=b_t\left(1+\frac{1}{8}\frac{G_{\ell,t}-\alpha B_\ell}{\alpha B_\ell}\right)\leq b_t\left(1+\frac{1}{8}\frac{B _\ell-\alpha B_\ell}{\alpha B_\ell}\right)\leq b_t\left(1+\frac{1}{8}\frac{1-\alpha}{\alpha}\right),
\end{aligned}
which implies a relative increase of at most $100\times\frac{1-\alpha}{8\alpha}$%. Similarly, 
\begin{aligned}
b_{t+1}&=b_t\left(1+\frac{1}{8}\frac{G_{\ell,t}-\alpha B_\ell}{\alpha B_\ell}\right)\geq b_t\left(1+\frac{1}{8}\frac{0-\alpha B_\ell}{\alpha B_\ell}\right)\geq b_t\left(1-\frac{1}{8}\right).
\end{aligned}
However, since it is enforced that messages on lane $\ell$ can only consume at most $B_\ell$ gas units, this control on the relative change in the base fee comes at the cost of having less flexibility when including opcodes on a given lane, which can result in failing to include messages. 

-    **Flexible.** Here, lanes have **only** a *target gas usage* $B_\ell^*$., and messages can be included as long as there's available block space. This offers greater flexibility in message inclusion. But, if the target gas usage gets adjusted, it could lead to significant jumps in the base fee if no other requirements are enforced. To see this, notice that  
\begin{aligned}
b_{t+1}&=b_t\left(1+\frac{1}{8}\frac{G_{\ell,t}- B^*_\ell}{B_\ell}\right)\leq b_t\left(1+\frac{1}{8}\frac{B- B^*_\ell}{ B^*_\ell}\right)=b_t\left(1+\frac{1}{8}\left(\frac{B}{ B^*_\ell}-1\right)\right),
\end{aligned}
which has the term $B/B^*_\ell$. Thus, if one is, in addition considering a mechanism where $B^*_\ell:=B^*_{\ell,t}$ changes over time, one needs to specify additional parameters on the adjusting mechanism (like enforcing a minimum target, for example), since otherwise,  in the case where the target block size is much smaller than the total block size ($B^*_{\ell,t}\ll B$), the relative change on the base fee can become arbitrarily large. 


<div class="warning" style='background-color:#FFFDD0; border-radius: 20px; padding:0.7em;'>
<span>
    
💡 **Intuition.** The intuition behind the proofs above is to determine upper and lower bounds on the base fee, by presenting upper and lower bounds on the amount of gas used; indeed, the maximum amount of gas that can be used in a block is the total block size (which is present in the first and third equations), and the minimum amount of gas  that can be used is 0 (used in the second line)
</p>
</p></span>
</div>

### Lane Adjustment Mechanisms
The lane adjustment mechanism adjusts each lane's block space based on network designers' or stakeholders' objectives, like prioritizing specific types of messages (onboarding, maintenance, FIL+, etc). The process, generally outlined below, adapts the block space for each lane based on the network's status at time $t$, symbolized as $X_t$. The challenge then lies in designing the updating mechanism, denoted by  $H_\ell(X_t)$.   

<div class="math" style='background-color:#FFFDD0; border-radius: 20px; padding:0.7em;'>
<span>
    
💡 **intuition**. The idea here is to introduce a factor $p_{\ell,t}$ that takes values between 0 and 1 and which gives the proportion of the block space allocated to lane $\ell$ at epoch $t$. Thus, if $p_{\ell,t}=0.5$, for example, it means that lanel $\ell$ has 50% of the target block space; if $p_{\ell,t}=0.25$ it means that lane $\ell$ has 25% of the block space, etc. 
</p>
</p></span>
</div>



We now discuss this in more formal terms. Notice that, depending on the design choice regarding the flexibility discussed above, this can be understood as adjusting $B^*_\ell$ (the target), $B_\ell$ (the maximum lane size), or both, however, for the sake of exposition, we will limit ourselves to the case where $B^*_\ell$ is updated. Define the *relative priority factor* of lane $\ell$ at epoch $t$ as $p_{\ell,t}\in(0,1)$, where $\sum_\ell p_{\ell,t}=1$ for any epoch $t$. At epoch $t+1$, the $\ell$-th lane is assigned a target width $B^*_{\ell,t+1}$ given by

\begin{aligned}
B^*_{\ell,t+1}:=p_{\ell,t+1}B^*, \quad \text{where, currently, $B^*=\frac{B}{2}$}.
\end{aligned}
The relative priority of lane $\ell$ then gets adjusted on an epoch-to-epoch basis according to some updating mechainsm $H_\ell$, i.e., 

\begin{aligned}
p_{\ell,t+1}&:=H_\ell(p_{\ell,t}, X_t).
\end{aligned}


We now discuss several possible choices of $H_\ell$.

**Example mechanism: Fixed**

This corresponds to the simplest mechanism. In this setting, one chooses a set of *initial priority factors* $p_{\ell,0}$ for $\ell=1,2,\dots,L$, satisfying $\sum_{\ell=1}^Lp_{\ell,0}=1$, and keeps them fixed, i.e., $H_\ell(p_{\ell,t},X_t)=p_\ell=p_{\ell,t+1}$. While this offers a simple solution, we do not believe this is a rather valid approach, as it would require to be periodically adjusted to keep up with the gas requirements of the network. 

**Example mechanism: Proportional allocation based on Raw Byte Power (using linear regression)**

A metric that is closely related to the size of the network is *Raw Byte Power (RBP)*. Indeed, as we can see from the figures below, there is a clear dependence between RBP and some of the most widely used messages (e.g., `ProveCommitSector,` `PreCommitSector,` `SubmitWindowedPost,` etc.). 


![](https://hackmd.io/_uploads/ryCT1iton.png)

Taking this into account, we propose an **example implementation** with two lanes ($L=2$). In this setting, one lane $(\ell=1)$ is used exclusively for what we call *Maintenance and Onboarding Messages (M&O)*, namely`provecommit_sector_gas_used`,
       `precommit_sector_gas_used`, `provecommit_aggregate_gas_used`,
       `precommit_sector_batch_gas_used,` and 
       `submit_windowed_post_gas_used`,  and the other lane ($\ell=2$) is used for everything else. Since there is a clear linear relation between the total gas used by M&O messages and network RBP (figure below, on the left), we can use simple linear regression to model
       
\begin{aligned}
\mathsf{Total \ daily \ gas\ used\ M\&O}_t=2632.09\times \mathsf{Network\  RBP}_t-9609,
\end{aligned}
where the equation above is given in terms of Billions of gas units. 

**Remark** *The previus equation was estimated using [linear least squares](https://en.wikipedia.org/wiki/Linear_least_squares#:~:text=In%20statistics%20and%20mathematics%2C%20linear,unknown%20parameters%20of%20the%20model.), using  daily gas usage and power data obtained from Starboard.* 

<div class="warning" style='background-color:#FFFDD0; border-radius: 20px; padding:0.7em;'>
<span>
    
💡 **Intuition.** From our observed data, we can see that there is a roughly linear relationship between total gas used in a day and total RBP. Thus,  we use linear least squares to find out the parameters that make up such a relationship. This doesn't mean that daily gas usage can be predicted from netwrok RBP with 100% accuracy, but as show in the figure below, these quantities are, in fact, related.
</p>
</p></span>
</div>

![](https://hackmd.io/_uploads/S1PFl_W2n.png)
One can use the previous equation to derive the *relative priority factor* of lane $\ell=1$, and from it, use the fact that $p_{\ell=1,t}+p_{\ell=2,t}=1$ for all $t$, to derive the   *relative priority factor* of lane $\ell=2$. To that end, notice that from the previous equation, we have that the average block proportion of gas used by M&O messages on a daily basis is given by 

\begin{aligned}
\mathsf{Prop.\ Target \ block \ used}_t&=\frac{\mathsf{Total \ daily \ gas\ used\ M\&O}_t}{\underbrace{\mathsf{Epochs \ in \ a \ day}}_\text{:=2880}\times \underbrace{B^*}_\text{:=5 billion}\times \underbrace{\mathsf{Avg. \ Blocks \ per \ epoch}}_\text{:=5 Blocks}}\\\\
&=\frac{\mathsf{Total \ daily \ gas\ used\ M\&O}}{2880\times 5\times 5}\\ \\
&=\frac{2632.09\times \mathsf{Network\  RBP}_t-9609}{2880\times 5\times 5}.
\end{aligned}
Notice, however, that while the previous equation induces a proportion, it is not enough to define the relative priority of lane $\ell=1$,   $p_{\ell=1,t}$ since $\mathsf{Prop.\ Target \ block \ used}_t$, as a function, is not necessarily between 0 and 1. Thus, taking some minimum width $p_{\ell=1,\min}\in(0,1)$ and a maximum width $p_{\ell=1,\max}\in(0,1)$, we can then define the update rule for $p_{\ell=1,t}$ as 
\begin{aligned}
p_{\ell=1,t+1}:=\underbrace{\min\left\{p_{\ell=1,\max},\max\left\{ p_{\ell=1,\min},\mathsf{Prop.\ Target \ block \ used}_t\right\}\right\}}_\text{$:=H_{\ell=1}(X_t=\mathsf{Network\  RBP}_t)$},
\end{aligned}
where the $\min$ and $\max$ operators are there to guarantee that *relative priority of lane $\ell=1$* says bounded between 0 and 1. Furthermore, since it holds that $p_{\ell=1,t}+p_{\ell=2,t}=1$ this induces the update rule for lane $\ell=2$, which is given by 
\begin{aligned}
p_{\ell=2,t+1}:=\underbrace{1-p_{\ell=1,t+1}}_\text{:=$H_{\ell=2}(X_t=\mathsf{Network\  RBP}_t)$},
\end{aligned}
which defines $H_{\ell,t}$ for both lanes. This, in turn, implies that the lane width $B_\ell$ of each lane is then given by 
\begin{aligned}
B^*_{\ell=1,t+1}&=\min\left\{p_{\ell=1,\max},\max\left\{ p_{\ell=1,\min},\mathsf{Prop.\ Target \ block \ used}_t\right\}\right\}B^*,\\
B^*_{\ell=2,t+1}&=B^*-B_{\ell=1,t+1}.
\end{aligned}


<div class="math" style='background-color:#FFFDD0; border-radius: 20px; padding:0.7em;'>
<span>
    
💡 **intuition**. Under our considered model (i.e., a linear regression), one can write the (estimated) total gas used by M&O messages as a function of Raw Byte Power (RBP).
    
From this, we obtain the average proportion of gas used in a block, by taking the estimated total gas used by M&O messages and dividing it by the average number of blocks in a day (2880 epochs $\times$ 5 Billion gas units as a target $\times$ 5 blocks per epoch, on average). 

Since this is a proportion, it *should* returna number between 0 and 1. However, since the estimated total daily gas used by M&) messages is a linear function, it is not necessarily bounded between 0 and 1 (as we require for the priority factor); and as sucvh we resort to  using the min and max operators. 
</p>
</p></span>
</div>


Notice that the previous approach can be generalized in a few ways. First, it can easily be extended to the case of more than two lanes. Furthermore, the gas requirements as a function of the state $X_t$ can be made more precise by computing how much gas is needed by `SubmitWindowPost.` Lastly, the choice of a single variable regression model was made due to simplicity. However, one could consider a model with several other predictor variables, such as e.g., *quality-adjusted power, baseline, circulating supply,*etc.   



**Example mechanism: Proportional allocation based on average gas consumption**

In this mechanism, block space is allocated to each lane in proportion to its gas usage, thereby ensuring an equitable distribution of space and preventing the monopolization of resources by any single lane.

We denote the average (whether geometric, arithmetic, or exponentially weighted) gas usage of lane $\ell$ at time $t$ as $G^N_{\ell,t}$, and the cumulative average gas usage of all lanes as $G^N_{t}:=\sum_{\ell=1}^LG^N_{\ell,t}$. The block space allocated to lane $\ell$ at time $t+1$, denoted $B_{\ell,t+1}$, can be calculated as:

\begin{aligned}
B^*_{\ell,t+1}=\underbrace{\frac{G^N_{\ell,t}}{G^N_t}}_\text{:=$p_{\ell,t}$}B^*,
\end{aligned}

In this setting, the adjustment mechanism $H_\ell$ is simply the ratio of average gas usage. 

### Multi-fee vs. adjusted (prev. discounted) gas lanes.

Here we discuss the differences between having a multi-fee mechanism (i.e., having a different EIP1559 mechanism per lane)  vs. utilizing an adjustment (previously referred to as *discount*) per lane. As we will see shortly, there is a specific choice of parameters for which these two approaches are the same.

#### The multi-fee mechanism.

This mechanism equips each lane with its own EIP1559-like transaction fee mechanism; hence, to each lane $\ell$, there corresponds a base fee $b_{\ell,t}$ which gets updated on an epoch-to-epoch basis according to the formula

\begin{aligned}
b_{\ell,t+1}=b_{\ell,t}\left(1+\frac{1}{8}\frac{G_{\ell,t}-B^*_{\ell,t}}{B^*_{\ell,t}}\right),
\end{aligned}
where $G_{\ell,t}\geq 0$ the gas used in lane $\ell$ at time $t$ and $B^*_{\ell,t}$ is the target block-size of lane $\ell$. Notice that, in a general setting, $B^*_{\ell,t}$ can be updated over time.

In this model, including a message $m$ on chain incurs a cost $\text{cost}_\text{mf}(m)$ given by the amount of gas used in lane 1 times its base fee, plus the amount of gas used in lane 2 times the base fee in lane two, and so forth. Mathematically:   

\begin{aligned}
\text{cost}_\text{mf}(m)&=b_{1,t} G_{1,t}+b_{2,t} G_{2,t}+\dots + b_{L,t} G_{L,t}=\sum_{\ell=1}^Lb_{\ell,t} G_{\ell,t},
\end{aligned}

Notice that setting $b_{\ell,t}=\tilde{b}_t$ returns the single-laned cost at some base fee $\tilde{b}_t$.

#### Adjusted multi-lane mechanism.

Contrary to the previous case, where we had $L$ different base fees, this model employs a single base fee $b_t$, adjusted according to consumption in each lane. Specifically, letting $a_{\ell,t}\geq 0$, $\ell=1,2,\dots,L$ denote the adjustment factor on each lane at epoch $t$, the cost  $\text{cost}_\text{aml}(m)$ that a user pays for submitting a message $m$ is given by the base fee multiplied by the adjusted gas usage on each lane, i.e.,:
\begin{aligned}
\text{cost}_\text{aml}(m)&=b_t\left(a_{1,t} G_{1,t}+a_{2,t} G_{2,t}+\dots +a_{L,t} G_{L,t}\right)=b_t\left(\sum_{\ell=1}^La_{\ell,t} G_{\ell,t}\right). 
\end{aligned}

Setting $a_{\ell,t}=1$ returns the single-laned cost at some base fee $b_t$.


Notice that if, in addition, one enforces that $a_{\ell,t}\in[0,1]$, this mechanism clearly becomes a pure discount over the single lane case. Indeed, since that condition implies that $a_{\ell,t}\leq 1$, one has that
\begin{aligned}
\text{cost}_\text{aml}(m)&=b_t\left(\sum_{\ell=1}^La_{\ell,t} G_{\ell,t}\right)\leq b_t\left(\sum_{\ell=1}^LG_{\ell,t}\right)=\text{cost}_\text{single lane}(m).
\end{aligned}
It is relatively easy to see that the previous result becomes a strict inequality (i.e., strictly cheaper) *if at least one*  of the parameters $a_{\ell,t}<1$. 
#### The isomorphism

Observing the similarity in the cost equations in both models raises a question: *Are these two approaches equivalent?* As we shall see, this question can be answered positively under a specific adjustment mechanism $a_{\ell,t}$. 


Indeed, setting $$a_{\ell,t}:=\frac{b_{\ell,t}}{b_t},$$ and replacing on the equation for the cost of the *adjusted multi-lane mechanism* ($\text{cost}_\text{aml}(m)$)  then yields

\begin{aligned}
\text{cost}_\text{aml}(m)&=b_t\left(a_{t,1} G_{t,1}+a_{t,2} G_{t,2}+\dots +a_{t,L} G_{t,L}\right)\\
&=b_t\left(\frac{b_{t,1}}{b_t} G_{t,1}+\frac{b_{t,2}}{b_t} G_{t,2}+\dots +\frac{b_{t,:}}{b_t} G_{t,L}\right)\\
&=b_{t,1} G_{t,1}+b_{t,2} G_{t,2}+\dots +b_{t,L} G_{t,L}\\
&=\text{cost}_\text{mf}(m)
\end{aligned}

<div class="math" style='background-color:#FFFDD0; border-radius: 20px; padding:0.7em;'>
<span>
    
💡 **intuition**. For a specific discount factor, both approaches are the same, in the sense that they result in a cost that is equal under both approaches. By the same token, for any other choice of adjustment factor, these two approaches are different. 
</p>
</p></span>
</div>

A simple simulation illustrating this is shown below. We use a random adjustment factor $a_{\ell,t}$ to illustrate the point. 
![](https://hackmd.io/_uploads/ry5uvY_oh.png)

This is a rather interesting (and somewhat intuitive) result, as it shows that both approaches are the same under a specific choice of adjustment mechanism.  

In more detail, let's look at the term $a_{\ell,t}$. Such a term can be understood as the relative intra-lane cost compared to the overall cost. Given that such a cost is, loosely speaking, a proxy for network demand and congestion, the adjustment terms can be roughly understood as the congestion in lane $ \ell $ relative to the overall network congestion. Thus, an $a_{\ell,t}>1$, can roughly be understood that lane $\ell$ is busier than the overall network (per unit of gas), while $a_{\ell,t}<1$ can roughly be understood as such a lane being comparatively less busy that the rest of the network (per unit of gas).


#### Comments

- Despite their operational differences, both models exhibit an isomorphism under a specific choice of adjustment mechanism, i.e., they are practically equivalent under the right conditions. Setting the adjustment factor to be the ratio of the base fee of each lane to the overall base fee renders the costs in both models identical. This result shows that while the mechanisms differ in their approach, they capture the same principles and behaviors.
- The adjustment factors serve as valuable indicators of the relative congestion in each lane, giving a proxy for network demand and congestion. The factors may help determine if a lane is busier or less busy compared to the rest of the network per unit of gas, which can be a key factor in decision-making.
- One needs to investigate (via game-theoretic arguments and simulation) whether the isomorphic choice of $\{a_{\ell,t}\}_{\ell=1}^L$ is optimal (in some sense) or if there are any clear advantages of one method over the other one for non-isometric adjustment parameters.
- An important factor to consider when defining which mechanism to use is UX/UI. Intuitively, the adjusted approach *may* offer a simpler UX, as there is a single base fee that gets adjusted according to the lane's consumption. From a UI perspective, this could be easier to display and understand. However, it's important that the adjustment factor is communicated clearly to the user, as it still affects the total cost of transactions.


## Proposed model 

Taking the previous discussion into account, we propose the following choice of design space. 


**Number of lanes** It is our view (also supported by discussions with stakeholders) that this should be as small as possible. Initially, we propose to set $L=2$, one lane for M&O (lane 1) and the other for everything else (lane 2). The number of lanes can be reevaluated in a posterior FIP as the conditions of the network change. 

**Initial lane width** For Lane 1, this parameter can be estimated by computing the average gas used by M&O messages and potentially inflating this quantity by some small factor as a way of providing some *wiggle room* and potentially avoiding introducing shocks to the cost, ultimately, the goal is to guarantee that such a *priority* lane is equipped with sufficient gas so that these transactions can get included on-chain without users having to pay unprofitable fees for them.

***Inclusion flexibility.*** We believe it is better to go with the *flexible approach*, as this would reduce the probability of failing to include a message whenever the gas lane for one of its components is full. This, in turn, requires determining a minimum target gas usage $B^*_{\ell,\min}>0$.

***Lane-adjusting mechanism**.* Due to its simplicity, we propose using the *Proportional allocation based on Raw Byte Power* as discussed above; indeed, this is an updated formula that can easily be computed using state data. **However, we are open to suggestions for either a more complex and more precise model.**

***Multi-fee vs. discounted/adjusted gas lanes***. This needs further discussion, and we should align on our ultimate goals. In our views:

- The choice of $a_{\ell,t}$ in the isomorphism *seems*intuitive, however, one might run into the issue of having $b_{\ell,t}\gg b_t$, which can significantly inflate the price in lane $\ell$. 
-  However,  if we want to create a pure discount for the M&O lane, then the (purely discounted) adjusting mechanism is the way to go. This has the UX/UI advantage of knowing an upper bound on the cost of including a message (given by the single-laned cost of doing so), but it is subjected to loss of network revenue.  


## Next steps and call to action. 
- We (CEL) would like to get alignment from the stakeholders in the design space, the proposed model, as well as other clear technical details that we might have missed in this discussion. Points related to feasibility, impact, security concerns, and backward/forward compatibility are especially appreciated. 

- Once we align on the design space, we will start (co)writing the FIP. Parallel to this, we intend to run numerical simulations to verify that the proposed design does not induce any undesirable behavior, such as significantly increasing the variance of the base fee, rendering unsustainably large base fees, etc.





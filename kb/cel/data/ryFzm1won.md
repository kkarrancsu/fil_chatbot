

## Simple Summary


This proposal introduces a structure where block space is divided into (two) different segments, called *gas lanes*, to reserve some block space for maintenance and onboarding messages, hence avoiding potential *gentrification* issues as the demand for FEVM gas grows. manage operations more efficiently. 

## 1. Motivation

As demand for the Filecoin-Ethereum Virtual Machine (FEVM) grows, it is in the Filecoin network's best interest to reserve a minimum amount of block bandwidth for messages that are critical to the functioning of the network, such as sector maintenance (e.g., `SubmitWindowPost`) and data-onboarding messages (e.g., `PreCommitStorage`).  Indeed, as it has been explored in [cite], if the amount of gas demanded by FEVM messages were to grow substantially to the point were FEVM users start submitting large miner tips in order to get their messages included in any given block,  then it is entirely possible that these *network-critical* messages might get *priced-out* and not be included. This is a phenomena that we have termed *gas gentrification*.   

It is worth mentioning that at the time of writing (September, 2023), demand for FEVM-related messages is still quite low (about 1% of gas consumed). Nevertheless, this is aimed to be a *preventive* FIP, which, if passed, can be later be implemented a t the developers' discression. 


## 2. Specification 

This proposal introduces a structure where block space is divided into (two) different segments, called *gas lanes*, to reserve some block space for maintenance and onboarding messages, hence avoiding potential *gentrification* issues as the demand for FEVM gas grows.  





### 2.1 Main setting


We begin by describing the gas lanes mechanism on a general setting, and we will then present the specifics of the model. Consider a block of maximum block size $B$ and $L\geq 1$ different *gas lanes.* In our setting, we embrace the concept of "one message, multiple lanes," where every message *taps* into gas from several lanes based on its components. Here, each of these lanes is equipped with its own EIP1559-like transaction fee mechanism, with a specific target gas usage on each lane. This target gas usage then gets adjusted on an epoch-to-epoch basis according to the relative requirements for each lane. 


In particular, we treat a message $m$ as a set of $N_m\geq 1$ *instructions* (or OpCodes) $m=\{c_{i_j}\}_{j=1}^{N_m}$. Here, each OpCode $c_{i_j}$ consumes a specific amount of gas $g_\ell(c_{i_j})$ of a unique, specific, lane $\ell$. Thus, any given message consumes $G^m_\ell$ gas units of lane $\ell$, with $G^m_\ell$ understood as the sum of the gas consumed by the OpCodes that execute on the lane $\ell$. This is illustrated in the figure below. 

![](https://hackmd.io/_uploads/HJdhVJm9h.png)

It is worth mentioning that our design does not allow for partial inclusion, i.e., a message containing $M$ instructions, will only be included if all M instructions can be executed. Notice that this is **not** different to how messages are included in bocks today.  

With this in mind, what we propose is: 

1. Divide the block into 2 lanes; one for maintenance and onboarding messages (M&O) and one for everything else. 
2. Assign each *Instruction/OpCode* to either one of those lanes
3. Endow each lane with its own transaction fee mechanism and
4. Give the whole system a *lane adjustment mechanism*, which at each epoch assigns an amount of target block size to each epoch according to a well-defined rule.

We now discuss our proposed mechanism in more detail.

## 2.2 Components

### 2.2.1 Choice of lane.

We Propose to allocate the following messages into their own lane (lane $\ell=1$)
`SubmitWindowedPoSt`, `PreCommitSector`, `ProveCommitSector`,`proveCommitAggregate`, `precommitSectorBatch`. We will denote these messages as *Maintenance and Onboarding* (M&O).

All other messages and opcodes will be allocated to lane $\ell=2$. 

Both lanes are endowed with their own EIP1559-like transaction fee mechanism; meaning that there will be 2 base fees, 2 target gas usages, and 2 gas usages.

Notice that setting $b_{\ell,t}=\tilde{b}_t$ returns the single-laned cost at some base fee $\tilde{b}_t$.

####  Rationale 
We believe that the number of lanes should be as small as possible. This is to avoid introducing additional sources of complexity, since a larger number of lanes, would in turn imply that the end user needs to track a larger number of base fees, etc. 

Furthermore, we propose to only include these 5 messages sinc e they can be reasonably well predicted by raaw byte power, as disacussed in section 2.2.3.



### 2.2.2 Inclusion mechanism.

A message can be only be included if all there is enough space for all of its instructions. Rather than setting a maximum lane size on each lane, we  **only** introduce a *target gas usage* $B^*_{\ell,t}$ on each lane, and messages can be included as long as there's available block space. Thus, denoting by $G_{\ell,t}$ the amount of gas used in lane $\ell$ at epoch $t$, the base fee $b_{\ell,t}$ for such a lane evolves according to the rule:


\begin{aligned}
b_{\ell,t+1}&=b_{\ell,t}\left(1+\frac{1}{8}\frac{G_{\ell,t}- B^*_{\ell,t}}{B^*_{\ell,t}}\right),
\end{aligned}
where $G_{\ell,t}$ is allowed to take values between 0 and the maximum block size. We remark that the target block size, $B^*_{\ell^*,t}$ is allowed to cahnge on an epoch-to-epoch basis, and this adjusting mechanism is described in the following section. 

**Remark** Notice that the previous model allows the base fee to change by more that 12.5% per epoch (which is the current maximum the base fee can increase or decrease by in two consecutive epochs). As such, one needs to guarantee that $B^*_{\ell,t}$ does not become arbitrarilly small, as this can in turn cause arbitrarilly large changes in the base fee. 


In this model, including a message $m$ on chain incurs a cost $\text{cost}_\text{mf}(m)$ given by the amount of gas used in lane 1 times its base fee, plus the amount of gas used in lane 2 times the base fee in lane two, and so forth. Mathematically:   

\begin{aligned}
\text{cost}_\text{mf}(m)&=b_{1,t} G_{1,t}+b_{2,t} G_{2,t}+\dots + b_{L,t} G_{L,t}=\sum_{\ell=1}^Lb_{\ell,t} G_{\ell,t},
\end{aligned}

for the *general* case with $L$ lanes, and in the particular case of 2 lanes that we are proposing, one simply has:

\begin{aligned}
\text{cost}_\text{mf}(m)&=\overbrace{b_{1,t}}^\text{base fee lane 1} \times \underbrace{G_{1,t}}_\text{gas in lane 1}+\overbrace{b_{2,t}}^\text{base fee lane 2}\times \underbrace{G_{2,t}}_\text{gas in lane 2}
\end{aligned}

####  Rationale.

This offers greater flexibility in message inclusion (when compared to setting a fixed maximum lane size). It also makes for a more efficient use of the block space. Additonal models, together with their pros and cons, are explored [here](https://hackmd.io/vmi9ROQeTqefuVDDvy1jYg?both) (c.f. Section 3).


### 2.2.3 Lane adjustment mechanism.
To ensure that the proposed system remains adaptive and responsive to the demands of the network, it's essential to devise a method that can automatically allocate the right amount of target block space to Maintenance & Onboarding (M&O) messages. The goal is to have a mechanism that adjusts based on real-time data without necessitating frequent manual recalibrations. In this section, we introduce a "Lane Adjustment Mechanism" designed to fulfill this need. This mechanism employs mathematical formulas derived from observing the relationship between the amount of gas used by M&O messages and the network's Raw Byte Power (RBP). Let's delve into the specifics. 

Let $B^*$ denote the current target block size (5 Billion gas units), let $B^*_{\ell=1,t},B^*_{\ell=2,t}$ denote the target block size of lane 1 and 2, respectively, at epoch t, $p_{\ell=1,\max},p_{\ell=1,\min}$ are two parameters determining the maxmimum and minimum proportion of the target block space allocated to lane 1, respectively. Given this, we propose to adjust the target block size of each lane according to the following formula: 

\begin{aligned}
B^*_{\ell=1,t+1}&=\min\left\{p_{\ell=1,\max},\max\left\{ p_{\ell=1,\min},\mathsf{Y}_t\right\}\right\}B^*,\\
B^*_{\ell=2,t+1}&=B^*-B_{\ell=1,t+1},
\end{aligned}

where $\mathsf{Y}_t$ is an upper bound on the estimated proportion of gas used by M&O messages, given by

\begin{aligned}
\mathsf{Y}_t=\frac{2632.09\times \mathsf{Network\  RBP}_t}{2880\times 5\times 5}.
\end{aligned}
This estimation is obtained from using linear regression on the amount of gas used by these messages, taking raw byte power as a predictor variable. In the following subsection we describe our choice of model and parameters in full detail. 

#### Rationale.

We begin from the observation that there is a clear, linear relation between the amount of gas used by M&O messages and network *Raw Byte Power (RBP),* as shown below.

![](https://hackmd.io/_uploads/ryCT1iton.png)
![](https://hackmd.io/_uploads/S1PFl_W2n.png)

With this in mind, one can use linear regression to estimate the amount of daily gas required by M&O messages as a function of RBP to be of the form:

\begin{aligned}
\mathsf{Total \ daily \ gas\ used\ M\&O}_t=2632.09\times \mathsf{Network\  RBP}_t-9609,
\end{aligned}

where $\mathsf{Network\  RBP}_t$ is given in EiB and $\mathsf{Total \ daily \ gas\ used\ M\&O}_t$ is given in Billions of gas units.  Furthermore, notice that this quantity can be upper bounded by $Z_t:= 2632.09\times \mathsf{Network\  RBP}_t$ (this will become relevant soon). Taking into account that there are 2880 epochs in a day, 5 blocks per epoch (on average), and that the current target block size is 5 Billion gas units, it follows from the previous equation that the *proportion of target block used* by M&O messages at any epoch $t$ can be approximated by 

\begin{aligned}
\mathsf{Prop.\ Target \ block \ used}_t&=\frac{\mathsf{Total \ daily \ gas\ used\ M\&O}_t}{\underbrace{\mathsf{Epochs \ in \ a \ day}}_\text{:=2880}\times \underbrace{B^*}_\text{:=5 billion}\times \underbrace{\mathsf{Avg. \ Blocks \ per \ epoch}}_\text{:=5 Blocks}}\\\\
&=\frac{\mathsf{Total \ daily \ gas\ used\ M\&O}}{2880\times 5\times 5}\\ \\
&=\frac{2632.09\times \mathsf{Network\  RBP}_t-9609}{2880\times 5\times 5}.
\end{aligned}

And it is also easy to see that it can be upper bounded by


\begin{aligned}
Y_t=\frac{Z_t}{2880\times 5\times 5}=\frac{2632.09\times \mathsf{Network\  RBP}_t}{2880\times 5\times 5}>\mathsf{Prop.\ Target \ block \ used}_t.
\end{aligned}

The previous number can be made into a *true proportion* (i.e., a number between 0 and 1) by the following transform:

\begin{aligned}
p_{\ell=1,t+1}:=\underbrace{\min\left\{p_{\ell=1,\max},\max\left\{ p_{\ell=1,\min},\mathsf{Prop.\ Target \ block \ used}_t\right\}\right\}}_\text{$:=H_{\ell=1}(X_t=\mathsf{Network\  RBP}_t)$},
\end{aligned}
where $p_{\ell=1,\min}$ and $p_{\ell=1,\max}$ take a fixed value  between 0 and 1, and represent the *minimum and the maximum proportion of target block space to be allocated to M&O messages*, respectively. 


From this, $p_{\ell=1,t+1}$ can be interpreted as the proportion of the target block size allocated to M&O, and by extension, $p_{\ell=1,t+1} B^*$ can be understood as the amount of block space allocated to such messages. Since there are only two lanes, the rest of the target block space is allocated to lane 2, which finally, gives our proposed formula: 

\begin{aligned}
B^*_{\ell=1,t+1}&=\min\left\{p_{\ell=1,\max},\max\left\{ p_{\ell=1,\min},\mathsf{Y}_t\right\}\right\}B^*,\\
B^*_{\ell=2,t+1}&=B^*-B_{\ell=1,t+1},
\end{aligned}

**Why using an upper bound on the amount of gas *required* by M&O?**

Notice that in the formula above we used an upper bound on the estimated proportion of gas used, rather that the estimated proportion itself. The reason behind this is to err in the side of caution, by giving M&O messages some extra *wiggle room*.

⚠️ It is worth mentioning that this extra *wiggle room* will help including more M&O messages without congesting that lane, at the cost of sacrificing *some* network revenue due to token burning. However, since this FIP is intended to be implemented in a secenario where FEVM-related messages are in such a high demand that they might imply a threat to network critical messages, that increase in use on the other lane should, at least in theory, alleviate thar reduction on protocol revenue. It is also important to mention that this approach is NOT optimal, but is is easy to implement. 



**Why enforcing lower and upper bounds on the target block size *given* to M&O?**

Recall that each lane has its own EIP1559-like transaction fee mechanism of the form 

\begin{aligned}
b_{\ell,t+1}&=b_{\ell,t}\left(1+\frac{1}{8}\frac{G_{\ell,t}- B^*_{\ell,t}}{B^*_{\ell,t}}\right).
\end{aligned}

Thus, if no positive lower bound to $B^*_{\ell,t}$, this quantity can get arbitrarilly close to 0, which will imply that the base fee can grow by an arbitrarily large amount from one epoch to another. By the same token, if no upper bound smaller than one is enforced, a similar situation can happen with the other lane (as it would, effectively, give it an arbitrarilly small target). 



## 3. Alternatives

We now briefly discuss some alternatives to the proposed mechanism. These alternatives are explored in much more detail in this [document](https://hackmd.io/vmi9ROQeTqefuVDDvy1jYg?both). 

### 3.1 Fixed lane size 
In this setting, each lane has a *fixed maximum lane width* $B_\ell ≤ B$ **and** a *target gas usage* $B^*_\ell$. The latter could, for instance, be set at $B_ℓ^* = B^*_\ell / 2$. Under this setup, opcodes of class $\ell$ can use up to $B_\ell$ gas units (i.e., it holds that $G_{\ell,t}\leq B_\ell$ for any epoch $t$). This ensures better control over base fee changes, however, might increase the probability of a message failing to be included whenever one of its opcodes fails to be included, and, intuitively, it makes a less efficient use of the block space.


### 3.2 Multiple base fees vs. adjusting factor

In our discussion, we presented an approach were multiple base fees were introduced. alternatively, one could consider one single base fee, and endow each lane with an *adjustment factor* that increases or decreases the amount of gas used on each lane. As shown [here](https://hackmd.io/vmi9ROQeTqefuVDDvy1jYg?both) it can be shown that, under a specific choice of *adjustment parameter*, this mechanism behaves *exactly* as a mechanism with multiple base fees, however, they are not, in general the same. We believe that using multiple base fees is more direct and easier to understand. 

###  3.3 Lane adjustment mechanism 


Alternatively, one can devise a mechanism where block space is allocated to each lane in proportion to its gas usage, thereby ensuring an equitable distribution of space and preventing the monopolization of resources by any single lane.

We denote the average (whether geometric, arithmetic, or exponentially weighted) gas usage of lane $\ell$ at time $t$ as $G^N_{\ell,t}$, and the cumulative average gas usage of all lanes as $G^N_{t}:=\sum_{\ell=1}^LG^N_{\ell,t}$. The block space allocated to lane $\ell$ at time $t+1$, denoted $B_{\ell,t+1}$, can be calculated as:

\begin{aligned}
B^*_{\ell,t+1}=\underbrace{\frac{G^N_{\ell,t}}{G^N_t}}_\text{:=$p_{\ell,t}$}B^*,
\end{aligned}

Notice that this demand-based adjusting mechanism can also be combined with the proposed RBP-based adjusting mechanism, at the cost of having a more complicated model. 

## 4. Security considerations

Apriori, we do not see any security concerns with the proposed model, provided that the amount of blockspace allocated  for maintenance and onboarding messages is sufficently large to cover for these needs. To do this, we overestimate the amount of gas required by M&O messages. However, this can cause the opposite effect: having too much space for M&O messages will in turn mean that the base fee for such a lane will tend to go down. This is not necesarilly ideal from a token-burning perspective, however, we choose to do it in such a way since:
    
1.  it  errs on the side of caution by giving these network-critical messages (more than) sufficient space. 
2.   The scenario which this aims to avoid, i.e., one where demand for FEVM-related messages is so large it *blocks* M&O messages from being included, would likely "make up" for this lost of tokens burned.
3.   At the time of writing, the largest contributor to the reduction of circulating supply comes from token locking, which is encouraged by having a more "accessible" maintenance and onboarding prices. 

## 5. Incentive Considerations

Erring on the side of miners *might* reduce network revenue, but can be balanced with FEVM demand if demand is high (which is why we propose this anyways). On the other hand, however, having *easy access* to M&O messages might, in turn, promote onboarding. 




## 6. Product Considerations

### 6.1 UX/UI

Introducing gas lanes adds an additional layer of complexity to the user interface, however, reserving enough block space for maintenance and onboarding operations (and hence, introducing some *control* on the base fee for these messages) can, in turn, encourage a larger volume of onboarding.


### 6.2 Multi-dimensional knapsack
 Gas lanes introduce a more complicated optimization problem. Instead of just considering gas fees, nodes or miners need to also evaluate which lane a transaction belongs to, and how it fits into the current distribution of lanes.


## 7. Compatibility

**Backwards compatibility** This change requires a hard fork since the base fee is enforced (for blocks to be considerd valid).  Tools that provide gas estimates will need to be recalibrated to account for the new mechanism.

**Future-proofness** As technical innovations that change the costs associated with M&O messages are introduced, the formula used to compute the target block sizes will need to be revaluated.


**Relation to FIP064** FIP064 proposes to implement an EIP1559-type of Transaction Fee Mechanism (TFM) where the update is taken based on a weighted average of the gas usage over a number of epochs, rather than on the gas usage on the previous epoch. If such a FIP were to pass, then its proposed a TFM would need to be implemented in multiple lanes. See [here](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0064.md) for more details. 


## 8. Test Cases

Too early to say.


## 8. Copyright Waiver 
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).


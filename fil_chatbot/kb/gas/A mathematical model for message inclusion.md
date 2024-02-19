---
tags: Gas, Research WIP
---
# A mathematical model for message inclusion


## Abstract. 
We present a mathematical characterisation of the process  of how messages are included in blockchains. In particular, we argue that, under some reasonable assumptions on the behaviour of said messages, their inclusion can be thought-of as a hierarchical Markov process. 

The relevant codes can be found [here.]('https://github.com/protocol/CryptoEconLab/tree/blockSim')

## Introduction and motivation. 


TODO: expand by a lot. 

We present a probabilistic model for the process in which messages arrive to a Mempool, and are later included on-chain. Such a model can be easily implemented to simulate the process at hand for  an arbitrarily large number of epochs. Our model takes into account possibles changes on demand for blockspace (resulting from, e.g., changing base fee, block-size, etc), as well as broad ecosystem changes (such as, adding user-defined actors, as will be the case for the F(E)VM). 


In this manuscript, we present a theoretical framework, together with the computational tools, required to investigate (via simulation) several questions on the Filecoin netork involving a high degree of complexity, such as:

* How will the F(E)VM affect the amount of block-space, what can we expect to happen if F(E)VM messages  consume, on average, $X$% of the available blockspace, in any given block?
* What is the distribution of transactions per second, for a given level of F(E)VM demand?
* How could one propagate and quantify the uncertainty in block-space used by F(E)VM to other arbitrary quantities of interest? (i.e., how will this affect, e.g., base fee,  onboarding, etc.) 

## Notation and Setup. 

### Some notes on notation

We will use the  symbol $\mathbb{R}_+$ to denote the non-negative real numbers (i.e., $\mathbb{R}_+:=[0,\infty)$).


We will also assume that tokens and gas units are real-valued, i.e., $A,B\in\mathbb{R}_+$ for any given token $A$, and gas units $B$. Notice that this is a slight simplyfying assumption as, in general, these terms are defined to be (large) integers. 




### Setup
Let $c_i, i=1,\dots,N_c, \ c_i\cap c_j=\emptyset\ \forall j\neq i$ be a collection of $N_c$ mutually exclusive abstract sets that we will refer to as  *classes*. The union of all such classes form what we call the *Message Universe* $\mathcal{M}:=\bigcup_{i=1}^{N_c}c_i$. In addition, for a given  time $t\in\mathbb{R}_+$, we define the *Mpool* $M_t\subset \mathcal{M}$, as well as the *block at time* $t$, $B_t\subset M_t$.

The main focus of this work is to model how messages are included on-chain. We  define a *message* $m\in \mathcal{M}$ as the following touple:


$$ m=(g,v,t,c_i), $$


where for each message $m$,  $g\in\mathbb{R}_+$ is the amount of gas required by the message, $v\in\mathbb{R}_+$ denotes the amount of token an user bids to send such a message to the Mpool, $t$ is the time at which such a message was sent to the Mpool, and $c_i$ denotes the class of such a message. With a slight abuse of notation, for a given message $m$, we denote its class by $c(m)$, its associated bid by $v(m)$, and so on. 

In the particular case of the filecoin network, we have $N_c=3$ different classes; namely `ControlPlane` $(i=1)$, `DataPlane` $(i=2)$, or `F(E)VM` $(i=3)$.  In this setting,  the `ControlPlane` class consists of those messages that are vital for the correct functioning of the network (which includes, e.g., `ProveCommitSector`, `SubmitWindwedPoSt`, etc), the  `FVM` class encompases all user-defined methods that will be used in the (Filecoin(-Ethereum) Virtual Machine), and, lastly, the `DataPlane` class consists of all other methods that are in neither of the previous two classes. Furthermore, in this same setting, $g$ and $v$ are equivalent to the so-called `GasUsed` and  `GasFeeCap`$\times$`GasLimit` respectively. See the [filecoin specification]() for more context. 



## Assumptions
We will work under the following underlying assumptions:


###### Assumption 1 [Messages are random] 

Let $\Delta t\in\mathbb{R}_+$ denote the time between any two consecutive messages.

* A1.1.  The time $\Delta t$ between any two messages arriving at $M_t$ is random. 
* A1.2. No two messages can occur at the exact same time.
* A1.3. For a given message, $v(m)$ and $g(m)$ are also random variables. 
* A1.4. The distribution for the time $\Delta t$ between two messages will depend on the class of message, i.e., messages of class $c_i$ might appear more or less frequent than those of class $c_j$, $j\neq i$.
* A1.5. The distribution of $g(m)$ and $v(m)$ for any given message $m$,  will also depend on the class $c_i$. 


Notice that these assumptions are quite mild and should hold for a wide variety of cases. 


We now focus on constructing the distribution (or more general, the random process) that characterises $\Delta t$ and $(g,v)$.


Let $d$ be some *demand parameter* in some abstract space $\mathcal{D}$. For any class $c_i$ let :

1. $\mu_{\Delta t | c_i}(t,d)$ denote the random process that characterises how often messages of class $c_i$ occur, given a time $t$ and a demand paramter $d.$ 

2. $\mu_{g,v | c_i}(t,d)$ denote the random process that characterises both the gas consumed and the amount of gas bid for a message of class $c_i$, given a time $t$ and a demand parameter $d$.


Here $d$ is to be understood as an *intensity* parameter such that, as $d$ increases, $\mathbb{E}[\Delta t]$ decreases and $\mathbb{E}[g]$ increases. 


Furthermore, assume that for any $t\in\mathbb{R}_+$ and $d\in\mathcal{D}$,   $$\mu_{\cdot|c_i}(t,d)\perp \mu_{\cdot|c_j}(t,d)\quad \forall i\neq j,$$

i.e., samples from these distributions are statistically independent.  

## Model and Algorithm.

### Model

Let us focus on how to model $\mu_{(\cdot)|(\cdot)}$ and $d$.  


#### Modeling demand. 

We define demand for class $c_i$ messages $d_i:\mathbb{R}^2_+\to\mathbb{R}_+$ as the total volume of messages included at a time $t$ for a price $v$.  In a First-price auctions, $d_i(t,v)$ can be understood as the amount of messages with a bid larger than or equal to $v$, at some time $t$. Similarly,  in the case of EIP1559-like transaction fee mechanisms, $d_i(t,v)$ can be understood as  the amount of messages with `GasFeeCap`$\times$`GasLimit` larger than or equal to $v$, for some given time $t$. Characterising demand in blockchain networks is a non-trivial aspect and is currently an active area of research (cite). For our purposes, we will require that for any $c_i$,

1. For any $v,t\in\mathbb{R}_+$, $\int_0^t d_i(s,v)\mathrm{d}s$ exists. 
2. For any fixed $t\in\mathbb{R}_+$, the mapping $v\mapsto d_i(t,v)$ is non-increasing in $v$. 
3. The *demand rate* for messages of class $i$, $\lambda_i(t,v):=t^{-1}\int_0^t d_i(s,v)\mathrm{d}s$ is strictly positive and locally integrable, i.e., for any set $B\subset\mathbb{R}_+,$ $\int_{B}\lambda_i(s,v)\mathrm{d}s <+\infty$.

TODO: Comment on why we need these.

TODO: clarify that one could consider different types of rate functions.


#### Modeling $\mu$

There are two random components to a message The first one is the *time component*, which is related to the arrival time between any two messages of the same class $c_i$. The second one is the *value component*, which relates to  (i) the amount of gas used by any given message and (ii) the bid associated to it. We now describe. We now describe these components in more detail. 

##### Time compenent. 

Intuitively, messges arrive at a random time and the frequency at which they arrive depends on (i) the class of messages and (ii) the current demand for such a class of messages. We now present a process that satisfies (i) and (ii). 



Let $N_i(t)$ denote the random number of messages of class $i$ that arrive to the Mpool in the time interval $[0,t)$,  and denote by $t_i^n\in\mathbb{R}_+$ the time at which the $n$-th message of class $i$ arrives to the Mpool. For some small $h\in\mathbb{R}_+$ we will assume that 

B1. $\mathbb{P}(N_i(t+h)-N(t))=1)=\lambda_i(t,v)h + o(h),$

B2. $\mathbb{P}(N_i(t+h)-N(t)\geq 2)=o(h)$.


 It can be shown  under conditions B1 and B2 that the time $\Delta t^n_i:=t^{n+1}_i-t^n_i$ between the $n$-th and the $(n+1)$-th message of class $i$ satisfies 
\begin{aligned}
\mathbb{P}(\Delta t^n_i>\tau)&=\mathbb{P}(N_i(t_i^n+\tau)-N_i(t_i^n)=0) \\
&=\exp\left(-\int_{t^n_i}^{{t^n_i}+\tau}\lambda_i(s,v)\mathrm{d} s\right)
\end{aligned}

TODO: Prove previous claim, this follows from Kolmogorov equations. 

Furthermore,  from the previous equation we can see that $\Delta t_i^n$ has the following Cummulative Distribution Function (CDF): 

\begin{aligned}
\mathbb{P}(\Delta t^n_i\leq\tau)&=1-\exp\left(-\int_{t^n_i}^{{t^n_i}+\tau}\lambda_i(s,v)\mathrm{d} s\right)\\
&=:(\mu_{\Delta t|c_i}(t_i^n,d_i))(\tau).
\end{aligned}

Given this, we will use the  notation $$ \Delta t_i^n\sim \mu_{\Delta t|c_i}(t_i^n,d_i)$$ to denote a sample from a probability measure induced by the previous CDF. This is usually called a *non-homogenous Poisson* process. In the case where $\lambda_i$ itself is a random variable, it is called a *Cox* process. 

let $\Lambda(p):=\sup_{t\in\mathbb{R}_+} \lambda_i(t,v)$. One way of simulating such processes is shown in the algorithm below. A `python` implementation of such a process can be found [here](https://github.com/protocol/CryptoEconLab/blob/blockSim/notebooks/blockSim/NHPP.py). Such a process is illustrated in the figure below Algorithm 1. There, we used $T=0$, $\lambda(t,v)=\sin^2(t)$ and $\Lambda(v)=1$. 


![](https://hackmd.io/_uploads/SyOhhJeUi.png)




![](https://hackmd.io/_uploads/B1zYcJeUi.png)




#### Value component. 

We now model the distribution of the value of each message. For any given $(g_i,v_i)$, we require that 

1. $g_i,v_i$ are positive-valued.
2. As $d_i$ increases, $\mathbb{E}_{\mu_v|c_i}[v_i]$ also increases but $\mathbb{E}_{\mu_g|c_i}[g_i]$ stays constant; i.e., users are willing to submit a larger bid (in the form of a larger `GasPremium`), however, the amount of network resources required to submit such a message stays constant. 

For any $c_i$, $i=1,\dots, N_c$, let $f_i:\mathbb{R}_+\to\mathbb{R}_+$ be some positive and monotonically increasing function, and let $b_t$ denote the base fee at time $t$. One could then generate samples of $(g,v)$ as follows:

1. Sample, independently:
\begin{aligned}
X_g&\sim\mathcal{N}(m_i,\sigma_{i,g}^2),\\
X_v&\sim\mathcal{N}(f_i(d_i),\sigma_{i,v}^2),\\
u&\sim\mathsf{Uniform}(0,1)
\end{aligned}
2. set $g=\exp(X_g)$ and $v=(b_t+\exp(X_v))\times g\times(1+U)$.

Here, $g$ is to be understood as `GasUsed`, $g\times (1+ U)$ as `GasLimit`, $b_t+\exp(X_v)$ as `GasFeeCap` and $v$ as the total amount of tokens a user is willing to bid. Thus, given some class $c_i$, we denote a realisation of the the previous two steps as 

\begin{aligned}
(g,v)\sim\mu_{(v,g)|c_i}.
\end{aligned}




### Algorithm

Let $\mathcal{S}:\mathcal{M}\to\mathcal{M}$ be a *miner strategy*, understood as a function that  takes a set of messages $M\in\mathcal{M}$, assigns to each message $m\in\mathcal{M}$ a "preference" value, sorts the messages contained in $M$ in decreasing order of preference, and returns the sorted set of messages $M^\text{sorted}$. 
Furthermore, let $T\in\mathbb{R}_+$ denote the epoch time, and  $G^*$ denote the maximum block-size.

There are two parts to our proposed simulation framework. The first part, presented in Algorithm 1, simulates the process of messages arriving on the Mpool. Such an algorithm relies upon the assumption of having message frequency and cost $(v,g)$ independent across different classes. Under this assumption, the algorithm  simulates the process of messages arriving to a *restricted Mpool* $M^i_t:=\left\{m \in M_t | c(m)=c_i\right\}$ (i.e., an artificial Mpool where all messages are of class $c_i$), and then combines all restricted Mpools into one by setting $M_t=\bigcup_{i=1}^{N_c}M^i_t$. We remark that since the process of creating each restricted Mpool is independent of the others, one could perform the `for loop` in Algorithm 1 in an *embarassingly parallel* manner.  



 

![](https:/hackmd.io/_uploads/SywsuNnSo.png)
![](https://hackmd.io/_uploads/rJUwxGeLi.png)




The second part of our simulation framework takes the combined Mpool obtained from Algorithm 1, sorts the messages contained there according to the miner preference function $\mathcal{S}$, i.e., sets $M^\text{sorted}_t=\mathcal{S}(M_t)$, and includes the messages in  $M^\text{sorted}_t$ in the new block $B_t$, in decreasing order of preference, until either the maximum amount of gas in the block has been reached or until there are no more messages in $M^\text{Sorted}_t$. Once messages have been included in the block $B_t$, said messages are removed from the Mpool $M_t$. This procedure is shown in Algorithm 2.    
![](https://hackmd.io/_uploads/H1jJKN2Hs.png)
Lastly, running Algorithm 1 and Algorithm 2 in a sequential manner, gives our simulation framework.
![](https://hackmd.io/_uploads/rktwKVnro.png)


## Next steps.



In the Filecoin case we have that messages can be of either one of these classes:

* $c_1:$ Control PLane class, i.e., messages that are required for proof of storage (`SubmitWindowedPoSt`)
* $c_2:$ Data plane messages; all other messages that are not required  for proof of storage (e.g., `send`)
* $c_3:$ F(E)VM messages, which are actor-defined transactions to be executed on-chain. Notice that there are not, at the time of writing, being deployed on mainnet. 


A first question is *How could one anticipate the effect of $c_3$ messages?*

One could, a priori, consider the following scenario. 

Assume that, for any fixed time $t$ and value $v$,   we have $d_3(t,v):=d_3(t,v,a_1,a_2)=a_1d_1(t,v)+a_2 d_2(t,v)$, for some $a_1,a_2\in\mathbb{R}_+$. This means that the demand for $c_3$ messages is a linear combination of the demands for the other two messages. As an example, setting $a_1=2,a_2=0$, would represent a scenario where demand for FEVM messages is twice as high as that of control plane messages. Similarly, setting $a_1=1/2, a_2=0$, would mean that the demand of FEVM messages is about half of that for control-plane messages, and so on. 

Given a time-dependent quantity of interest $Q$ that depends indirectly on the demand function $d_3$ (such as, base fee, pledge, total network revenue, etc), we could estimate the effects of $c_3$ on $Q$ by iterating the following steps for any combination of $a_1,a_2$:




1. For $n=1,\dots, N_\text{sims}$:

* 1.1. Use Algorithm 3 to simulate how blocks evolve on $N_e$ epochs, i.e., obtain $B^n=\{B_e^n\}_{e=1}^n.$

* 1.2. For  each *path of blocks* $B^n$, compute a value of the desierd quantity of interest, $Q^n$. This could be, e.g., the basefee at epochs $e=1,\dots,N_e$, onboarding rate at each epoch, etc.

2. Compute relevant statistical properties of $Q$, such as mean, standard error and histogram. Store them and repeat these two steps for other values of $(a_1,a_2)$


The one issue with this process is that it might be computationally expensive to simulate. 























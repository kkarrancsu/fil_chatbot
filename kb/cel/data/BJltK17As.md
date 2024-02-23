


## Introduction
Filecoin is a decentralized storage network that allows users to *rent* out their unused storage space to others in exchange for FIL. To ensure smooth network operation, Filecoin uses a fee market that includes a "base fee," the minimum fee required to get a transaction included in a block. The base fee changes dynamically based on demand for block space, which can vary widely over time.

The upcoming deployment of the Filecoin Virtual Machine (FVM) is expected to bring new demand for the usage of Filecoin gas, which could be absorbed by scalability solutions. However, different stakeholders in the network have varying *utility functions*  (understood as a mathematical characterization of preference) with respect to the base fee. For instance, users sending small transactions may pay a higher base fee to ensure quick confirmation, while larger transactions may wait for lower fees. Furthermore, other stakeholders in the network will have their own utility fucntions reflecting their own interests; token holders, for example, would in gernal have a utility funcrtion that *prefers* token burning, while miners could have a utility function that aims at striking a balance between maximizing earnings and maintaining network stability.

In this article, we will (1) present mathematical models for demand in FVM, (2) explore the composition of a block and (3) the utility functions of different stakeholders in the Filecoin network as a function of the base fee and demand for gas. By understanding the composition of block as a function of demand can help us understand how will FVM affect the demand for block space. Furthermore, by examining the utility functions of different stakeholders in the Filecoin network, we can gain a deeper understanding of their interactions and their effects on network performance. This knowledge is crucial for designing and operating a decentralized storage network like Filecoin.

This first report is intended to (1) formulate the system at hand and (2) provide a qualitative and "first order" understanding of the effects of the (upcoming increase in) demand in the FIlecoin network.

We begin by formulating the governing equations of demand based on a series of mild assumptions. The reader uninterested with these mathematical details can freely skip the next section.

## Model



We begin with some definitions. For any epoch $t$, let $R_t\in \mathbb{R}_{\geq0}$ denote the block reward at an epoch $t$, let $G_t\in\mathbb{R}_{\geq 0}$ denote the gas usage, and let $b_t\in[b_\text{min},\infty)$ denote the base fee. Furthermore, for any given SP $m$, let $\rho_m$ denote that SP relative power in the network.   

**Definition (expected cashflow)**. For a given value of $b_t$, we define the *expected cashflow* of miner $m$ at epoch $t$ as 

\begin{aligned}
\Phi(m,t,b_t):=\mathbb{E}_m[R_t]-b_t\mathbb{E}_m[G_t]-O_m,
\end{aligned}
where $O_m$ represents the *op-ex* of miner $m$. Here, $\mathbb{E}_m[\cdot]$ represents the expectation over the probability measure induced by the lottery process for which  SP $m$ gets to mine a block.  

Currently in the Filecoin network, SPs (i.e., *miners*) are the same *users*. This means that they need to regularly submit messages to the network and pay gas for those messages that get included in the chain. 

The amount of FIL that each miner is willing to pay per message depends on several factors; how urgent is it for them to send the message (due to recurring proofs of storage, for example), the type of message, their opex, etc. Thus, for each message class $i$ and each miner $m$, there's some associated *value* $v_i$. This value is, of course, imposible to know for each miner and for each message, as it is highly subjective. The goal of this section is to present a model and a framework that can overcome this.

In order to do so, we will make the following simplifying assumptions and observations.


- **Assumption 1.** The value $v_m$ of a message **sent by the miner $m$** is equal to 
\begin{aligned}
v_m&=\max\{\Phi(m,b_t),0\}\\
v_m&=\max\{\mathbb{E}_m[R_t]-b_t\mathbb{E}_m[G_t]-O_m,0\}\\
\end{aligned}

- **Assumption 2.** Any miner $m$ submits a message with probability 1 only if $b_t=b_\text{min}=10^{-16}$ FIL/gas unit. Furthermore, we assume this probability decreases with $b_t$, and becomes *small* whenever $v_m<0$. 

- **Assumption 3.** We consider a suffciently short time horizon so that the changes in $\mathbb{E}[G_t]$ and $\mathbb{E}_m[R_t]$ (with respect to time) are negligible.

- **Assumption 4.** The average gas spenditure of miner $m$ is proportional to its network power. 

- **Observation 1.** The base fee can typically vary through several orders of magnitude. 

Intuitively, Assumption 1 means that the value assigned from each SP to its transaction is determined by their expected "cashflow". Assumption 2 means that miners are more likely to submit messages to the Mempool if their inclusion is profitable for (in expectation). In practice,  Assumption 3 holds relatively well over short periods of time (about a month). Lastly, Assumption 4 is relatively mild, and representative that, larger miners are more likely to spend more gas. 



From Assumptions 1 and 2 it follows that a message will be submited to the Mempool **with probability 1** if the base fee is $b_\text{min}=10^{-16}$ FIL per gas unit. Otherwise it decreases with $v_m$. We consider that messages will be submitted to the Mempool with a *high* probability if $v_m<0$:


\begin{align}
v_m<0 \Longleftrightarrow b_t\leq \frac{\mathbb{E}_m[R_t]-O_m}{\mathbb{E}_m[G_t]}.
\end{align}

In addition, under Assumptions 3 and 4, one can upper bound $b_t$ **independently of the miner** as follows:

\begin{align}
b_t\leq \frac{\mathbb{E}_m[R_t]-O_m}{\mathbb{E}_m[G_t]}\leq \frac{\mathbb{E}_m[R_t]}{\mathbb{E}_m[G_t]}=\frac{\rho_m\lambda N_\text{epochs}R}{\rho_m\mathbb{E}[G]}=\frac{\lambda N_\text{epochs}R}{\mathbb{E}[G]}=:b^*,
\end{align}
with $\mathbb{E}[G]$ the average gas usage over a day, $\lambda=5$ the expected number of blocks in an epoch, and $N_\text{epochs}$ the numer of epochs in a day.  

Thus, under Assumptions 1 and 2, it follows that whenever $b_t>b^*$, there's a significant probability that **any** miner might choose not to submit a message. 

Let's investigate these effects in more depth. In the next subsection we introduce our concept of demand.

### Survival function and demand.



**Definition (Survival Function).** We call a function $S:[b_\text{min},\infty)\to[0,1]$ a *survival function if*

- $S(b_\text{min})=1$.
- $\lim_{p\to\infty}S(p)=0$.
- $S$ is strictly monotonically decreasing.

For any given price $p$, we can interpret $S(p)$ as the proportion of gas that users (miners or FVM users) are willing to include in the Mempool (relative to all possible gas to be included). 

**Remark.** *Notice that $1-S(p)=:F(p)$ is, by definition, a cummulative distribution function when seen as a random variable. Furthermore, it follows from its definition that $S$ is a diffeomorphism; which in turn implies that $F$ has a probability $f$*.


**Modeling SP's demand**


Let $\hat{G}_\text{sp}$ denote the demand (in gas units) for a basefes $b=b_{\text{min}}$, and denote by $S_\text{sp}(p)$ the survival function of SPs.  Then, we can define the **SP-driven demand, $D_\text{sp}(p)$,** as a function of the price as 

\begin{align}
D_\text{sp}(p):=\hat{G}_{sp}S_\text{sp}(p)
\end{align}

Modeling this demand requires two inputs: $\hat{G}_\text{sp}$ and $S_\text{sp}(p)$. **While it is not possible to know this exact values, we can estimate them using statistical techniques and arguments from Uncertainty Quantification (UQ). By doing this, we steer away from trying to predict an exact outcome (an impossible task), and consider, "in one go", several different scenarios.**



**Estimating $\hat{G}_\text{sp}$.** We construct a Kernel Density Estimator (KDE) of the daily gas used, based on the last 90 days worth of data. A histogram based on samples form such a KDE is shown below. Denoting such a KDE by $K_{G}$, We define 

\begin{align}
\hat{G}_\text{sp}\sim K_G.
\end{align}


By considering $\hat{G}_\text{sp}$ to be distributed according to $K_G$, we can consider a wide variaty of possible scenarios.

![](https://hackmd.io/_uploads/Hk8HCFI0o.png)



**Estimating  $S_\text{sp}$.** In a general setting, the survival function can be understood as the proportion of miners that are  willing to submit messages at a given base fee. Mathematically, this can be written as a sigmoid function of the form

\begin{aligned}
S_\text{sp}(p;a,b)&=\left[1-\left(1+e^{-a(p-b)}\right)^{-1}\right]N^{-1}, \quad a,b\in\mathbb{R}_{+},\\
N&=\left[1-\left(1+e^{-a(b_\text{min}-b)}\right)^{-1}\right],
\end{aligned}

with some unknown parameters $a,b$, representing the decay rate of the sigmoid, and the point where half of the miners are not willing to submit messages. Once again, obtaining a "real" version of $S_\text{sp}$ is not possible, as this would require to have an intimate understanding of each SP, their risk preferences, OpEx's, etc. Instead, we construct a *family* of survival functions by parametrising the values $a,b$. 



**Example.** Taking into account that $b$ should be similar in magnitude to $b^*$ and that $a$ should be sufficiently large, we propose the following models:


\begin{aligned}
\log_{10} B&\sim \mathcal{N}\left(\log(b^*),1\right),\\
\log_{10} A&\sim \mathcal{N}\left(8,\frac{1}{4}\right).
\end{aligned}

Notice that by including the logarithmic term, we can consider a wide range of survival functions. 

**Putting it together.** Given this, we can generate what we call **demand profiles** with the following algorithm:

1. Sample $\hat{G}_\text{sp}\sim K_g$
2. Sample $\log(A), \log(B)$, from, e.g.,  the formulas above.
3. Set $D_\text{sp}(p)=\hat{G}_\text{sp}S_\text{sp}(p;A,B)$.

A figure depicting 100 such demand profiles is shown below. 


![](https://hackmd.io/_uploads/rkZuq2IAj.png)

**Modeling FVM's demand**

We  follow a similar procedure in our aim of understanding and quantifying the amount of gas due to FVM. More precisely, let $\hat{G}_\text{fvm}$ denote the FVM demand (in gas units) for a basefee $b=b_{\text{min}}$, and denote by $S_\text{fvm}(p)$ the survival function of the FVM users. Furthermore, we make the asusmption that 

\begin{aligned}
\hat{G}_\text{fvm}&=\alpha\hat{G}_\text{sp},\\
\alpha&\sim \mathcal{U}[0,5].
\end{aligned}
While it is not a strong assumption to model $\hat{G}_\text{fvm}$ as a multiple of $\hat{G}_\text{sp}$, the uniform prior $\mathcal{U}[0,5]$ we are assuming on $\alpha$ is, and might have an impact in some of our results.**Thus, the model should be updated once sufficient FVM has been obtained.** 
Taking advange of the fact that our survival function is a random variable that is sufficeintly general to cover a wide variety of cases, we can define the **FVM-driven demand, $D_\text{fvm}(p)$,** as a function of price as 

\begin{aligned}
D_\text{fvm}=\hat{G}_\text{fvm}S_\text{fvm}(p;A'B'),
\end{aligned}
with $A'$,  and $B'$ random variables with a known distribution. 


**Total demand**

Lastly, we can define the total FVM demand as follows. let $\hat{G}:=\hat{G}_\text{sp}+\hat{G}_\text{fvm}$, $r_\text{sp}:=\hat{G}_\text{sp}/\hat{G}$, and $r_\text{fvm}=\hat{G}_\text{fvm}/\hat{G}$. Then the *total demand,* $D:[b_\text{min},\infty)\to\mathbb{R}_+$ can be written as 

\begin{aligned}
D=\hat{G}(r_\text{sp}S_\text{sp}(p;A,B)+r_\text{fvm}S_\text{fvm}(p;A',B')),
\end{aligned}

with $r_\text{sp},$ $r_\text{fvm},A,A',B',B',\alpha$ random variables, as previously described. 


The rest of this document is devoted to the *Primary goal* of the [work plan](https://hackmd.io/trzLL3qmQpWslKg_oDt9yw): namely, *understanding all hypothetical gas demand outcomes*.

## Estimating block composition
We present a first approximation of the *block composition*; that is, we present a first estimate of the proportion of the gas in a block that are due to FVM messages, versuss the proportion of these messages that are due to maintenace-type of messages. In order to so, we will rely upon several approximations.  While these approximations will not always hold in practice, we use them as a first-step towards understanding the task at hand. In upcoming work, we will investigate this issue through the lens of Agent-Based Models, which can in turn helps broaden our understanding of the tasks at hand, while at the same time relying upon a smaller number of assumptions, that we present next. 


- **Assumption 5** Let $B_\text{sp}(p),B_\text{fvm}(p)$ denote the amount of a block space due to SP messages and FVM messages, respectively at a base fee $p$. Furthermore, assume that, on average, one has that 
\begin{align}
B_\text{sp}(p)+B_\text{fvm}(p)\leq B_\text{target},
\end{align}
where $B_\text{target}:=5\times 10^{9}$ gas units denotes the target block size. Notice that this trivially implies that $B_\text{sp}(p)\leq B_\text{target}$ and $B_\text{fvm}(p)\leq B_\text{target}$.

- **Assumption 6** Furthermore, denote by $r_\text{sp}\in[0,1],r_\text{fvm}\in[0,1]$ the proportion of unsend messages of maintenance and FVM type, respectively. Exploiting the fact that $S_{(\cdot)}$ is a bijection, we interpret 
\begin{align}
S_{(\cdot)}(p;a,b)&:=1-r_{(\cdot)}\\
\implies p&:=S^{-1}_{(\cdot)}\left(1-r_{(\cdot)};a,b\right)
\end{align}

It follows from Assumptions 5 and 6 that we can use the following system of equations to estimate the block composition for any given price $p$:

\begin{align}
S_\text{sp}(p;a,b)&:=1-r_\text{sp}\\
S_\text{fvm}(p;a,b)&:=1-r_\text{fvm}\\
B_\text{target}&\geq B_\text{sp}(p)+B_\text{fvm}(p).
\end{align}

Furthermore, it can be estimated that, on average, $B_\text{sp}\approx 0.7 B_\text{target}$ for any given block; indeed it just suffices to divide the expected gas usage in a day by the number of blocks per day, multiplied by the target block size, i.e., 
\begin{align}
\frac{B_\text{sp}}{B_\text{target}}=\frac{\mathbb{E}[G_\text{sp}]}{N_\text{epochs}\times \lambda\times B_\text{target}}\approx \frac{5\times 10^{13}}{2880\times 5 \times 5\times 10^{9}}\approx0.694.
\end{align}


This means that, on average, the gas used per block due to SP maintenance messages is about $\hat{G}_\text{sp}=3.5\times 10^9$ gas units. As such, we will assume that $B_\text{sp}(p_\text{min}=10^{-16})=\hat{G}_\text{sp}$. In what follows we investigate the composition of a given block, assuming that 

\begin{aligned}
B_\text{sp}(p)&=\hat{G}_\text{sp}S_\text{sp}(p;A,B),\\
B_\text{fvm}(p)&=\hat{G}_\text{fvm}S_\text{fvm}(p;A',B'),\\
\log_{10}(A)&\sim \mathcal{N}(10,1),\\
\log_{10}(A')&\sim \mathcal{N}(10,1),\\ 
\log_{10}(B)&\sim \mathcal{N}(-11,1),\\ 
\log_{10}(B')&\sim \mathcal{N}(-9,1),\\ 
\log(\hat{G}_\text{sp})&\sim \mathcal{N}(\log(\hat{G}_\text{sp}),1/400),\\ 
\hat{G'}_\text{fvm}&=\alpha\hat{G}_\text{sp},\\
\alpha&\in\left\{0.1,0.5,1,2,5,10\right\}.
\end{aligned}
Notice that the choice of distributions presented above allows us to consider a wide variety of cases. We investigate the composition of the block in two scenarios: the "no preference" scenario, where a miner packs a block without discriminating against the type of messages, and the "SP-prioritized" scenario, where a miner first packs all  maintenace-type messages (i.e., those submitted by SPs) and then packs the remainder FVM messages, if any. 

In either scenario, for each value of $\alpha$, we run 1000 experiments for different values of $A,A',B'B',\hat{G}_\text{sp}$, sampled from the distributions above. We display each individual realisation in faint colors, and their mean value as a solid line. We reiterate that by doing this, we take into account several combinations of demand profiles.


Notice that we chose to have a a distribution for $B'$ that concentrates around smaller values that the one of $B$ since intuitively, SPs would tend to have a more inelastic demand function; indeed, they need to consistently submit proofs of storage on time, which allows for less flexibility on whether they can choose to submit a message or not. 

**No preference**

We plot the proportion of the target block space, occupied by each type of message without any given level of preference. As we can see from the figure below, as $\alpha$ increases, the proportion of the messages occupied by FVM messages increases; however, this proportion rapidly decreases as $p$ increases. On average, regardless of the initial value, once the base fee is roughly above $10^{-10}$ tokens per gas unit, the block is dominated by SP maintenance messages.


![](https://hackmd.io/_uploads/rJWYLB61h.png)




**With preference -- prioritizing SPs**

We now repeat the previous experiment, but for a miner who always packs the maintenance messages first. As we can see, the plots looks quite similar for higher values of $\alpha$; this is natural, since, regardless of the proportion of FVM messages, the miner at hand will always pack all the SP messages first, which account for a maximum block space of about $0.7B_\text{target}$, leaving at most $0.3B_\text{target}$ worth of block space available, irrespective of $\alpha$. In a practical setting, this would imply that FVM users will likely need to wait a comparatively longer time to get their messages included.




![](https://hackmd.io/_uploads/HJ7dLra13.png)


**Gas usage**

If we had the goal of maximizing total network revenue, from our previous results, it is possible to infer what should be the optimal block size to fill, for a given level of demand.

We re-interpret our previous results by assuming that the reason the a fraction of the block is empty is because the target block size has been reduced to $(1-\mathsf{prop.\ empty})\times B_\text{target}$. We then find the optimal block size, such that the corresponding total network revenue (base fee* reduced target block size) is maximized. This optimal block size is labeled in the above figures as B* . We find that in many cases, network revenue could be maximized by reducing the size of the block.



## Utility Functions

As mentioned in the work plan, instead of trying to predict or forecast an exact outcome due to FVM demand, we instead aim at understanding various hypothetical gas demand outcomes. In simple terms, our goal is to understand if the effects of a certain level of net gas demand $D$ will be "good" or "bad" for the network, a set of users, etc.  In order to determine what "good" and "bad" is, we need first need to define a metric for this effect. We will refer to this metric as a **utility function**. In what follows. we consider several utility functions of varyiing complexity. 


**Remark.** *Please note that utility functions are a measure of preference and represent the interests of different stakeholders in a subjective way. While we have proposed several utility functions in this report to quantify the benefit that various stakeholders would have with respect to changes in the base fee and demand, it is important to note that these functions are not unique and may differ depending on the assumptions and values used. Additionally, the utility functions presented in this report may not capture all aspects of a stakeholder's interest and may not be applicable in all situations. Therefore, the results and conclusions based on these functions should be interpreted with caution and considered as a starting point for further analysis and discussion.*

**Simple payer's utility**


We begin by defining a utility function for a user in the Filecoin network who is mostly concerned with keeping low base fees. There are several possible choices for this function, but we consider  one of the form:  


\begin{aligned}
U_\text{simple payer}(p) &:= -\log(p)
\end{aligned}
Furthermore, notice that the previous utility function can also be written in terms of demand by observing that $D$ is a *diffeomorphism* (differentiable and bijective) and hence invertible; i.e., for a given demand curve $y$, we can always write $p=D^{-1}(y)$. Below we plot this utility function as a function of price and demand. 


In this utility function, the user's utility is inversely proportional to the base fee $b$. That is, the higher the base fee, the lower the user's utility. The use of the logarithm ensures that the utility function is concave, which is a desirable property for many economic models.

This utility function is a common choice in economic models of congestion pricing and dynamic pricing, where users are charged a fee for using a shared resource such as a road or a network. In these models, the goal is to encourage users to self-regulate their usage of the resource by charging higher fees during periods of high demand, and lower fees during periods of low demand. Users who are sensitive to the fees will adjust their behavior accordingly, leading to a more efficient use of the resource.

In the context of the Filecoin network, this utility function can be used to model the behavior of users who are sensitive to the base fee and prefer to wait for periods of low demand to submit their transactions, in order to minimize their costs. The utility function can be combined with other factors such as the urgency of the transaction and the value of the data being stored to model more complex user behavior.


Below we plot $U_\text{simple payer}(p)$  vs $D(p)$ (left) and $U_\text{simple payer}(p)$ vs $p$ (right). As we can see, for this particular actor, the utility is maximized whenever the base fee is  at its smallest; which in turn is when the demand is also maximized.

![](https://hackmd.io/_uploads/ByfCGALRs.png)



An alternative model is to consider 

\begin{aligned}
\hat U_\text{simple payer}(p) &:= p^{-1}.
\end{aligned}
This utility function is shown below for several realizations of the demand function; in particular, once again, we show $U_\text{simple payer}(p)$  vs $D(p)$ (left) and $U_\text{simple payer}(p)$ vs $p$ (right). The conclusions remain the same as in the previous case. 


![](https://hackmd.io/_uploads/rJawbvHCo.png)


**Naive burner utility**


We now consider the utility of an agent that is mostly concerned about burning tokens. In this case, their utility is maximized whenever tokens are burnt due to the EIP1559 mechsnism. Once again, there are several ways of expresing a utility function of this form, but a possible one could be

$$ U_\text{burn}(D,p;S,W_m) := W_m \left(\frac{S}{S-Dp}\right),$$

with $W_m$ the token wealth of the $m$-th SP and $S$ the circulating supply. Notice that as $D$ or $p$ increase, the amount of token burnt incerases, thus decreasing the circulating supply. Thus, this particular choice of utility function is maximized whenever $D$ and $p$ are maximized. Below, we show $U_\text{burn}(p)$  vs $D(p)$ (left) and $U_\text{burn}(p)$ vs $p$.


![](https://hackmd.io/_uploads/SkdLedrAs.png)

As expected, such a function is maximized at around the maximum level of base fee that still provides some level of demand; i.e., around $10^{-8}$ FIL per gas unit


PLotting $U_\text{burn}(p)$ as a function of $D$ and $p$ yields the figure below. From there it is clear that such a utility increases with either $D$ or $p$ (or both).

![](https://hackmd.io/_uploads/Byr5bDBRj.png)

**Data onboarding utility**

Let's assume that the user's utility function is a function of two variables: the amount of data onboarded, denoted by Q, and the total cost, denoted by C, which includes the cost of using gas and paying fees.

In this setting, the user's utility function is:

$$ U_\text{data}(p,D,q;\alpha,\beta) = \beta Q - \alpha D\cdot p $$

where $Q$ is the amount of data onboarded and $d\cdot p$ is the total cost, which includes the amount of gas used, $D$, and the base fee, $p$. The parameter $\alpha$ reflects the user's sensitivity to the cost of using gas and paying fees relative to the amount of data onboarded, and $\beta$ is a parameter (given in terms of tokens per byte) symbolising the "monetary" value of this data. 

 Below, we show $U_\text{data}(p)$  vs $D(p)$ (left) and $U_\text{data}(p)$ vs $p$. As we can see, such a utility function decreases quite rapidly with either $D$ or $p$; once again this is intuitive, since a user that is mostly concerned with onboarding data will, of course, find it more challenging to do so as $p$ increases.
 
![](https://hackmd.io/_uploads/rkyGdhM12.png)






**SP utility**

\begin{equation}
U_\text{sp}(p,d) = b \cdot \log(d\cdot p) - \rho \cdot d\cdot p 
\end{equation}

where $U$ represents the utility function value, $d$ represents the gas usage, $p$ the base fee, $\rho$ the relative power of a miner in the network and $b$ a scaling factor.

Notice that the logarithmic term in the function $\log(d\cdot p)$ is added to account for the fact that the utility increase from gas burning is diminishing  for this particular agent, as $p$ grows; indeed. Furthermore, notice that the base fee has a negative impact on the utility, since storage providers have to spend gas.

![](https://hackmd.io/_uploads/S1hVK1mJh.png)



## Finalizing remarks



In this report, we presented a mathematical model for demand in the Filecoin network, investigated the composition of a Filecoin block as a function of the base fee, and proposed and investigated several utility functions representing the interests of different stakeholders.

Our proposed demand models are based on several assumptions and observations and are believed to hold well in practice. These mathematical representations of preference consist of a sigmoid function parametrized by a "rate factor" that determines how fast the amount of demanded gas decays as a function of price, and a "threshold factor" that represents the price that a service provider would be "comfortable" to pay on average. Since these values represent a highly subjective measure of choice for each miner, we formulated them as random variables with known distributions. This accounts for the subjectivity of these values and produces better and more robust estimates of subsequent quantities of interest using Monte Carlo methods.

Using these parametrized demand models, we estimated the proportion of gas in a block that is due to Filecoin Virtual Machine (FVM) messages versus the proportion of these messages that are due to maintenance-type messages, i.e., those used by SP on a recurring basis. Under our modeling assumptions, we found that once the base fee is roughly above $10^{-10}$ FIL per gas unit, the block is dominated by SP maintenance messages. We also estimated the decay rate of the proportion of FVM messages, and visualized these proportions as a function of the base fee for several levels of total FVM demand. **An interesting conjecture, is that the block composition will ultimately depend on the strategy of the miner.** 

We also proposed several utility functions as a way of quantifying the benefit that various stakeholders in the network would have with respect to changes in the base fee and demand. Our definitions of utility function showed that **stakeholders who are mostly concerned with high gas usage, those who benefit from onboarding data, and SPs are negatively affected by a significant increase in gas usage**. Conversely, our utility functions show that stakeholders such as **token holders, who benefit from burning more tokens, are positively impacted by an increase in the base fee.** While these results are intuitive, we believe it is worth quantifying and isolating these effects for the stakeholders mentioned above.

In our next report, we will aim at performing a simulation-based exploration of the composition of a block under several conditions, as well as shedding light to the following two questions:

1. *To what extent is it viable to not interfer with the gas usage  in the network ?* and 
2. *how can we mitigate the effects of a high demand for block space in case that it becomes problematic?*

These insights are valuable and will be expanded upon in future work using our latest [Agent-Based Model](https://github.com/protocol/CryptoEconLab/tree/gasABM/notebooks/gasABM) of gas consumption in the network.
---
title: Empirical analysis of gas consumption and model proposal
tags: Gas, Econ models
header-includes:
  - \usepackage[ruled,vlined,linesnumbered]{algorithm2e}
---
# Empirical analysis of gas consumption and model proposal

###### Juan P. Madrigal Cianci

---
## 1. Introduction

This report is the outcome of **task 1** in the [research plan proposal](https://hackmd.io/-SPCa6L7Sm-MK0liGX4Jww). As outlined in such a proposal, here we present a report covering a thorough data analysis of the gas dynamics currently used in the Filecoin network and discuss several modeling techniques for the gas consumption of each method or actor family. 


##  2. Methodology and datasets
In this report, we will focus on two main aspects of gas consumption. We will first investigate gas consumption at an aggregate, per-block level; that is, the sum of gas consumption across all actors for a given block. We will then focus on gas consumption at the actor level, where we will investigate the individual behavior of each of the gas components, per height (tipset). In both cases, we will investigate the statistical properties of gas consumption with the ultimate goal of being able to model such processes. 


Throughout this work, we will work with the following datasets. 
* [`derived_gas_output`](https://lilium.sh/data/models/#derived_gas_outputs), which provides data on derived gas costs resulting from the execution of a message in the VM. Each message is indexed by its `CID`. 
* [`message_gas_economy`](https://lilium.sh/data/models/#message_gas_economy), which gives gas economics for all messages (indexed by their `CID`) in all blocks at each epoch.
*  [`parsed_messages`](https://lilium.sh/data/models/#parsed_messages), which gives Messages parsed to extract useful information.
*  [`chain_consensus`](https://lilium.sh/data/models/#chain_consensus), which gives height and TipSet to Parent TipSet.


## 3. Gas as an aggregate


### 3.1 Basic exploratory analysis

We begin by examining the aggregate gas consumption per block by observing the `base_fee`  from tipset height 2005320 through 2094600, corresponding to block data ranging from July 22nd, 2022 through August 22nd, 2022. This data consisted of 88644 entries. 


Recall that base fee $b_t\in\mathbb{R}_+$ at block $t\geq 0$ is given by $$b_t=b_{t-1}\left(1+\frac{1}{8} \frac{G_{t-1}-G^*}{G^*}  \right),$$ with $G_{t-1}$ the gas consumption at block $t-1$ and $G^*:=5\times 10^9$ the target gas consumption. Defining the *normalised gas consumption at block $t$* as $\tilde{G}_t$, given by  $$\tilde{G}_t:=\frac{G_t-G^*}{G^*}, \quad \tilde{G}_t\in[-1,1],$$ it then follows that 
$$\tilde{G}_t=8\times\left( \frac{b_t-b_{t-1}}{b_{t-1}} \right).$$


Cleaning up the gas data (making sure that gas is obtained by block, and not tipset, removing empty entries, etc) and plotting it, gives the results shown in the figure below.



![](https://i.imgur.com/CyHSh35.png)

 We can see from the plot on the top left that, as expected, $\tilde{G}_t$ stays within its range of $[-1,1]$. Furthermore, it can be seen from such a figure that it is more likely to have a $\tilde{G}_t$ close to 1 than to -1; meaning that gas tends to be over-used, rather than under-used. This is further evidenced in the top right figure, where we plot the histogram for $\tilde{G}_t$. As we can see, the distribution for such a quantity seems to have a heavier right tail, as well as a non-negligible mass at $\tilde{G}_t\geq0.99$; in particular, it can be estimated (at 95\% confidence) that
 
 
 | Quantity 	|  Estimated probability 	| 95% standard error	|
|---	|---	|---	|
| $\mathbb{P}(\tilde{G}_t\geq0.99)$ 	|0.037 	| 0.002 	|
|  $\mathbb{P}(\tilde{G}_t\leq-0.60)$	|0.016  	|  0.002	|
 
 Thus, for the dates considered, about 4% of the time, $\tilde{G}_t$ was above a 99% capacity. The plot on the bottom left shows the AutoCorrelation Function (ACF) of $\tilde{G}_t$. From such a plot one can measure the dependence of $\tilde{G}_t$ (and hence $G_t$, as it is just an affine transformation) on its history, with the rough interpretation that the first zero of the ACF is roughly how long it takes the process $\tilde{G}_t$ to "forget" (i.e., become independent of) its history. In our case, we can see that the ACF plot crosses 0 at around lag-5, meaning that, roughly, two realizations of the gas process become independent of each other every five-or-so blocks. 
 
 


In addition, we plot the empirical cumulative distribution function for $\tilde{G}_t$ on the bottom right figure. As it can be seen,  there is a slight jump around $\tilde{G}_t=1$,  which accounts for the peak on the histogram.  A table with the summary statistics of $\tilde{G}_t$ is shown below:

| mean 	| std 	| min 	| 25% 	| 50% 	| 75% 	| max 	|
|---	|---	|---	|---	|---	|---	|---	|
| 0.010087 	| 0.391897 	| -0.973181 	| -0.280465 	| -0.058001 	| 0.228362 	| 0.999999 	|


There are some interesting takeaways from the previous table. First, the mean is within the standard error (at a 95% confidence level) of 0. As we will discuss later,  having a mean-zero process for $\tilde{G}_t$ is of importance to the overall health of the network. Furthermore, 75% of the time, the normalized gas usage is below 0.228.



### 3.2 Conditional behaviour

We now investigate the statistical behavior of $\tilde{G}_{t+1}$ given that $\tilde{G}_t$. In particular,w e will focus on the case where $\tilde{G}_t>0.99$, i.e., how does the gas consumption move in the next block, given that it is currently at capacity. Here we look at the histogram, the empirical CDF, and the ACF, as shown below.  
 
 
 
![](https://i.imgur.com/1O5Tfwe.png)


We can see that there is a non-negligible mass at $\tilde{G}_t>0.99$ (accounting for about 4.1% of the total mass) and that the ACF decays almost immediately to 0, implying that there is a very weak autocorrelation in this series. Furthermore, we have that:


 | Quantity 	|  Estimated probability 	| 95% standard error	|
|---	|---	|---	|
| $\mathbb{P}(\tilde{G}_{t+1}\geq0.99 \text{ given that } \tilde{G}_t\geq0.99)$ 	|0.041 	| 0.007 	|


The summary statistics of $\tilde{G}_{t+1}|\tilde{G}_{t}>0.99$, are given by:

| mean 	| std 	| min 	| 25% 	| 50% 	| 75% 	| max 	|
|---	|---	|---	|---	|---	|---	|---	|
| 0.127784 	| 0.377492 	| -0.735456 	| -0.144990 	| 0.071521 	| 0.349911 	| 0.999998 	




### 3.3 Time series analysis

We now investigate whether there are some seasonality components to the process $\{\tilde{G}_t\}_{t\geq 0 }$.  To that end, we fit a seasonality model from [Meta's Prophet library](https://facebook.github.io/prophet/docs/quick_start.html#python-api).  We can see that there do not seem to be any significant changes due to seasonality (less than one percent), as shown below. There, the shaded region corresponds to the uncertainty in a 10-day prediction for the trend. It is worth noting that perhaps a dataset with a larger timespan might be able to capture other seasonal components of the model. 


![](https://i.imgur.com/9hnAoe8.png)

### 3.4 Identifying demand peaks

Let's look at high and low-demand peaks. Let $\overline{G}\in[0,1]$ and $\underline{G}\in[-1,0]$ be some given threshold values. We define the high (resp. low) demand process $\{H_t\}$ (resp. $\{L_t\}$) as
\begin{align}
\{H_t\}_{t\geq 0}&:=\{1 \text{ if }G_t\geq \overline{G}, \ 0 \text{ otherwise}\}_{t\geq 0}\\
\{L_t\}_{t\geq 0}&:=\{-1 \text{ if }G_t\leq \underline{G}, \ 0 \text{ otherwise}\}_{t\geq 0}.
\end{align}


We plot these quantities below. In particular, we plot the processes $\{H_t\}_{t\geq 0}, \{L_t\}_{t\geq 0}$, the histogram of the interarrival times (i.e., the time between two consecutive high/low demand peaks), together with a KDE and an exponential fit, and the ACF of the interarrival times. We remark that, for the sake of visibility, we only plot the last 5000 observations for the high-usage process $\{H_t\}_{t\geq 0}$. 
![](https://i.imgur.com/CoSsde1.png)
![](https://i.imgur.com/aE79XTu.png)

As we can see, the process $\{H_t\}_{t\geq 0}$ "peaks" (i.e., takes non-zero values) more frequently than that of $\{L_t\}_{t\geq 0}$,  which signals that high-usage peaks occur more often than the low-usage valleys, as also evidenced by the histogram in Section 3.1. We can also see that the histograms for the interarrival times are well-approximated by an exponential distribution. In particular, for the high-usage case, we can see that such a distribution is characterized by a parameter $\lambda_H\approx0.04$, which means that, on average, there is a high-demand peak every $\lambda_H^{-1}\approx 20$ blocks. Similarly, one can conclude that, on average, there is a low-demand valley every $\lambda_L^{-1}\approx20$ blocks. Lastly, it can be seen from the ACF plot of both functions that the ACF goes to zero almost immediately, which suggests that these interarrival times might be statistically independent of each other. This is a rather interesting fact since the exponential distribution and the statistical independence characterize a Poisson process ([c.f. Kroese et al (2013), p. 172](https://www.wiley.com/en-us/Handbook+of+Monte+Carlo+Methods-p-9780470177938#:~:text=Handbook%20of%20Monte%20Carlo%20Methods%20provides%20the%20theory%2C%20algorithms%2C%20and,random%20numbers%20on%20a%20computer)). We will discuss this in further detail later in this report.

A natural question to ask is whether there exists a continuous mapping $\overline{G}_t\mapsto \lambda_H(\overline{G})$, which induces an exponential distribution, characterized by a rate $\lambda_H(\overline{G})$ of the interarrival times for gas usage above a given threshold value of $\overline{G}$. In order to investigate such a question, we fit $\lambda_H$ for different values of $\overline{G}$ in $[-1,1]$.  In all cases, we were able to see that the distribution of the interarrival times can be approximated with an exponential distribution relatively well (at least to the naked eye) and that the ACF decays to 0 almost immediately. We plot the values of the computed $\lambda_H$  as a function of $\overline{G}$. In the same plot, we perform a least-squares polynomial approximation of such a function, given by $$ \lambda_H(\overline{G})\approx \lambda^P_H(\overline{G}):=-0.6096 \overline{G}^4 + 0.7184 \overline{G}^3 + 0.4776 \overline{G}^2 - 1.001 \overline{G} + 0.4422$$

![](https://i.imgur.com/HiV0U2W.png)


### 3.5 Long-term behavior 


We now investigate the long-term behavior of gas consumption. For some given number of blocks $B\in\mathbb{N}$, we defined the averaged-out gas consumption every $B$ blocks as $$\widehat{G}^B_t:=\frac{1}{B}\sum_{i=0}^{B-1} \tilde{G}_{t-i}, \quad t\geq B.$$

Such a quantity averages the normalized gas consumption $\tilde{G}_t$ over the last $B$ blocks. Plotting this quantity for $B\in\{2, 10, 20, 60, 120\}$ (equivalent to averaging over 1,5,10,30 and 60 minutes, respectively),  yields the following results:


![](https://i.imgur.com/EzQkXER.png)
![](https://i.imgur.com/p25Y8lM.png)
![](https://i.imgur.com/0RXUQLP.png)
![](https://i.imgur.com/HEQqrTC.png)
![](https://i.imgur.com/Nq1l3Gq.png)


There are two important features to notice here. The first one is that, as we increase the number of blocks in the average, the distribution of $\widehat{G}^B_t$ starts becoming increasingly more concentrated around 0. This should not be a surprising fact given that the average value of $\tilde{G}_t$ is close to 0. It is also important to notice here that, as we increase $B$, the distribution of  $\widehat{G}^B_t$ increasingly resembles that of a Gaussian. 



Lastly, we define the $B$-*censored normalized gas consumption* as $$\mathring{G}^B_t:=\tilde{G}_{B\times t},$$
i.e., the process $\{\tilde{G}_t\}_{t\geq0}$ observed every $B$ blocks. Similarly, as before, we plot $\mathring{G}^B_t$ for $B\in\{2, 10, 20, 60, 120\}$, which yields the following results:

![](https://i.imgur.com/gqunuoW.png)
![](https://i.imgur.com/0ZyB4q1.png)
![](https://i.imgur.com/1v5yHy7.png)
![](https://i.imgur.com/LBHHyrD.png)
![](https://i.imgur.com/yrzftPM.png)

As it can be seen, at least for the time scales considered in this experiment, there does not seem to be much difference in the gas behavior from the uncensored case (i.e., $B=1$). This suggests that there might be some sort of *scale-invariance* in the dynamics of $\tilde{G}_t$. 


## 4. Gas by message

### 4.1 Basic analysis

We now move into examining gas usage by actor/method/message. To that end, we compute the total gas usage for each actor at any given height. Furthermore, we  have  separated the messages into two categories: the first category includes the so-called *Control Plane* messages, namely:

`CompactSectorNumbers`,`DeclareFaultsRecovered`,`DisputeWindowedPoSt`,`ExtendSectorExpiration`,`PreCommitSector`,`PreCommitSectorBatch`,`ProveCommitSector`,`ProveCommitAggregate`,`ReportConsensusFault`,`SubmitWindowedPoSt`, and`TerminateSectors`.

The second category includes all other messages. 

![](https://i.imgur.com/O7x5Qu5.png)

and in logarithmic scale (for ease of comparison):

![](https://i.imgur.com/nUOmntl.png)

From the previous two pictures, it is easy to see that most of the gas used is due to the following messages: `PreCommitSector`, `ProveCommitSector`, and `SubmitWindowedPoSt`. It is worth mentioning that all of these messages are Control-plane messages. We now plot the usage proportion of each method below. 

![](https://i.imgur.com/40lZa4p.png)


As it can already be seen from the picture above (left), control-plane messages take up most of the gas usage, as also evidenced by the following table:


| Statistic | Proportion Control plane | Proportion others |
|:---------:|:------------------------:|:-----------------:|
|   mean    |         0.955922         |     0.044078      |
|    std    |         0.055071         |     0.055071      |
|    min    |         0.254468         |     0.000215      |
|    25%    |         0.946541         |     0.012242      |
|    50%    |         0.972345         |     0.027655      |
|    75%    |         0.987758         |     0.053459      |
|    max    |         0.999785         |     0.745532      |



From here we can see that at least the average gas use proportion due to control-plane messages is about 0.955, while non-control plane messages are about 0.044. Furthermore, it can be seen that in 75% of the cases, the contribution to gas usage by non-control plane messages is below 0.053. This is further explored in the picture above (right), where we plot the histogram of the total weight for control-plane messages and the others.



### 4.2 Top methods

We now investigate the most influential messages for gas consumption. We begin by taking the average proportion of gas usage for each message. The top 10 messages by gas usage are shown in the table below. There, the $n^\text{th}$ position of the `Cumulative` column the sum of mean gas proportion from position 1 through $n$. As we can see, the top 8 messages represent over 99% of gas usage. Furthermore, the top 3 messages (all three of which are control-plane messages) account for over 86% of the gas consumption. 


| Position 	| Method 	| mean Proportion 	| Cummulative 	|
|---	|---	|---	|---	|
| 1 	| ProveCommitSector 	| 0.378143 	| 0.378143 	|
| 2 	| PreCommitSector 	| 0.302857 	| 0.681 	|
| 3 	| SubmitWindowedPoSt 	| 0.189821 	| 0.870821 	|
| 4 	| ProveCommitAggregate 	| 0.037305 	| 0.908125 	|
| 5 	| PublishStorageDeals 	| 0.037036 	| 0.945161 	|
| 6 	| ExtendSectorExpiration 	| 0.019451 	| 0.964612 	|
| 7 	| PreCommitSectorBatch 	| 0.018764 	| 0.983376 	|
| 8 	| DeclareFaultsRecovered 	| 0.00931 	| 0.992686 	|
| 9 	| ProveReplicaUpdates 	| 0.003358 	| 0.996043 	|
| 10 	| AddBalance 	| 0.001517 	| 0.99756 	|

We now investigate these messages in further detail. For each of these methods, we plot four quantities. On the top left plot, we plot the distribution of the time (measured in blocks) between non-zero occurrences. This can be understood as a measure of how frequently a given method is used. On the top left, we plot the histogram of its non-zero occurrences, measured in gas units. We also fit a KDE and an exponential distribution to such a distribution. On the bottom left, we plot the ACF of the times between non-zero occurrences, and on the bottom right, we plot the ACF of the gas consumption from that method. 


We begin with `ProveCommitSector`, which on average utilizes about 37% of the gas for any given block. As can be seen from the figure below, this message was included in all examined blocks. Notice that this should not be a surprising fact, given how Filecoin operates (and the same holds true for `PreCommitSector` and `SubmitWindowedPost`). Notice, furthermore,the distribution for the gas it consumes is left-skewed. As it can be seen from the ACF plot in the bottom right, the ACF decays to zero at around lag 10. This can be roughly interpreted as it taking 5 blocks for any two values of gas usage by this method to become statistically independent. 


![](https://i.imgur.com/hRgO3iN.png)

We now shift our attention to `PreCommitSector`. On average, this utilizes about 30% of the gas for any given block. Similarly, as with the `ProveCommitSector` message, this message was included in all examined blocks, and the distribution for the gas it consumes is also left-skewed. As it can be seen from the ACF plot in the bottom right, the ACF decays to zero at around lag 10. This can be roughly interpreted as it taking 10 blocks for any two values of gas usage by this method to become statistically independent. 

![](https://i.imgur.com/FaU2NSL.png)


We now shift our attention to `SubmitWindowedPost`. On average, this utilizes about 19% of the gas for any given block. Similarly, as with the previous two messages, this message was included in all examined blocks, and the distribution for the gas it consumes is also left-skewed. As it can be seen from the ACF plot in the bottom right, the ACF decays to zero at almost lag-1. This can be roughly interpreted as every realization of the gas used by `SubmitWindowedPost` being statistically independent of each other. 

![](https://i.imgur.com/83E71kW.png)

We now focus on `ProveCommitAggregate`. Contrary to the previous three messages, this method is not present in every block, as it can be seen from the histogram between non-zero times. Such a message is included, on average, every 3 blocks. As we can see, the distribution of the gas usage of such a method can be well-approximated by an exponential distribution with parameter $\lambda=2.68\times10^{-9}$.

![](https://i.imgur.com/tsXt8X0.png)

Looking at  `PublishStorageDeals`, we can see that such a message is included on most blocks and that its gas distribution is also well-approximated by an exponential distribution. 

![](https://i.imgur.com/G2pW7W4.png)

Looking at  `ExtendSectorExpiration`, we can see that such a message is sent relatively often. An interesting feature is that the ACF plot does not seem to decay very fast, meaning that there might be some hidden correlation among messages of this kind across blocks.

![](https://i.imgur.com/J4Sgyha.png)


Lastly, `PreCommitSectorBatch` and `DeclareFaultsRecovered` are other types of message that gets sent fairly often. Notice that the range of their gas consumption is about one order of magnitude smaller than the one for the previous messages.
![](https://i.imgur.com/yIyCXPn.png)
![](https://i.imgur.com/FmmaJGX.png)

The following plot shows the correlation matrix for the gas consumption of each of the top-10 messages. As it can be seen, there is not a particularly high correlation between any two variables, however, there is some non-negligible correlation among the top three methods.

![](https://i.imgur.com/g8humhi.png)




## 5 Proposed models

We now propose several models based on the previously described data. While we aim at implementing such models in this report, we postpone their validation and comparison for the next report, which aims at completing task 2 in the [research plan proposal](https://hackmd.io/-SPCa6L7Sm-MK0liGX4Jww).




### 5.1 Modelling gas as a whole.

We begin by presenting several ideas on how to model gas as its own process (i.e., without looking at each component). We remark that this is not an exhaustive list and that several components presented herein can be combined. 

#### 5.1.1 Simulating gas from the kernel density estimator. 

Perhaps the simplest way of simulating the process $\tilde{G}_t$ is by resampling its Kernel Density Estimator (KDE). Recall that given some [kernel function](https://en.wikipedia.org/wiki/Kernel_density_estimation) $K:\mathbb{R}_+\to\mathbb{R}_+$, and a bandwidth parameter $h\in\mathbb{R}_+,$ the KDE of the probability density of a dataset  $\{\tilde{G}_t\}_{t=1}^T$ is given by
$$\text{KDE}(x)=\frac{1}{hT}\sum_{t=1}^T K(x-\tilde{G}_t).$$
 The KDE is a probability density, meaning that it integrates with 1 and that it is always non-negative. It also induces a probability distribution, $F$. A simple, data-driven model for gas consumption is then to sample $\tilde{G}_t\sim F$ for any $t=1,2,\dots$. 
 
 ```{Python, eval=FALSE, FALSE}
#Preallocates
G=zeros(T)
#initialvalue
G[0]=g_0  
For t in 0,..., T:
    G[t]=sample_from_KDE()
```
Simulating $\tilde{G}_t$ from the KDE yields the results presented below. As we can see, the simulated results resemble the measured data fairly well. Here the bandwidth $h$ was chosen according to [Silverman's rule](https://en.wikipedia.org/wiki/Kernel_density_estimation).


![](https://i.imgur.com/inzeMem.png)



One disadvantage of this method is that the simulated samples of $\tilde{G}_t$ are statistically independent of one another, which in practice means that some of the autocorrelation encoded in the process for $\tilde{G}_t$ is lost. The following 


#### 5.1.2 Markovian approximation. 

Assume that $\{\tilde{G}_t\}_{t\geq 0}$ is a Markov process, i.e.,

$$\mathbb{P}(\tilde{G}_{t+1}=g_{t+1} | \tilde{G}_0=g_0, \tilde{G}_1=g_1, \dots, \tilde{G}_{t}=g_{t}, )=\mathbb{P}(\tilde{G}_{t+1}=g_{t+1} | \tilde{G}_{t}=g_{t}).$$

In words, this means that for any given time $t$,  the next value of the process $\tilde{G}_{t+1}$ only depends on the current value $\tilde{G}_t=g_t$. In this setting, if the conditional probability  distribution of $\tilde{G}_{t+1}$ given $\tilde{G}_{t}=g_{t}$ is known for any realization $g_t\in[-1,1]$, one can simply generate the process $\{\tilde{G}_t\}_{t\geq 0}$ by sampling from such a conditional distribution, as  shown in the following pseudo-code: 

```{Python, eval=FALSE, FALSE}
#T: number of steps
#Preallocates
G=zeros(T)
#initialvalue
G[0]=g_0  
For t in range(T):
    G[t+1]=sample_from_conditional(G[t])
```

The name of the game here is then to find such a suitable conditional distribution. This is, in general not an easy task to do without any further assumptions on the dynamics of the process (such as assuming it is an AR(1) process, for example). We propose the following heuristic methodology. First, we discretize the interval $[-1,1]$ in $N_h$ non-overlapping subintervals $I_i$ of length $h=1/N_h$. Then, for each $\tilde{G}_t\in I_i$, we estimate the probability of moving to an interval $I_j$ $j\in[1,\dots,N_h]$, using the recorded data. This induces a Markov transition matrix $P_{ij}$, with the property that $\sum_{j}P_{ij}=1$. The $i^\text{th}$ row of this matrix can then be understood as the probability of moving from interval $i$ to interval $j$ in one step. Given this matrix, one can simulate the gas dynamics as follows

```{Python, eval=FALSE, FALSE}
# chain= chain of tilde{G}
# ProbMatrix= Matrix P_ij
# Nsteps= Number of steps to simulate
# states= list of intervals e.g., states=[-1,-0.5,0,0.5,1]
# Nh Length of the states array

    for i in range(Nsteps):
         current_index=np.argmin(chain[i]>states)
         #samples from P
         new_index=np.random.choice(a=np.arange(Ns),p=ProbMatrix[current_index,:])
         #Gets some random value inside the interval
         if new_index<Nh:
            low=states[new_index]
            high=states[new_index+1]
            chain[i]=low+(high-low)*np.random.uniform()
          else:
            chain[i]=1
```

This process induces a random process approximating the true dynamics of $\tilde{G}_t$, with the understanding that such an approximation converges to the real process as $N_h\to\infty$. We plot 10000 steps of this process below. As we can see, the simulated process closely resembles that of $\tilde{G}_t$. This method has the advantage of being data-driven and easily implementable, however, large values of $N_h$ might yield a computationally expensive algorithm. 


![](https://i.imgur.com/iQdglkp.png)


#### 5.1.3 Gas as a bounded Ornstein-Uhlenbeck process. 


Based on the observations that $\tilde{G}$ is stationary, mean-reverting, and weakly autocorrelated, we propose the following variation of an Ornstein-Uhlenbeck process. Let $\mu,\theta,\sigma\in\mathbb{R}$ be three parameters representing the mean, the reversion rate, and the volatility of the process $Y_t$ given by 

$$\mathrm{d}Y_t=\theta(\mu-Y_t)\mathrm{d}t + \sigma \mathrm{d}W_t,$$

with $W_t$ the Wienner process. Given this, together with the observation that the gas process $\{ \tilde{G}_t\}_{t\geq0}$ is bounded between $[-1,1]$, we propose the following model for $\tilde{G}_t$:


$$
\tilde{G}_t=\begin{cases}
Y_t &\text{ if   }Y_t\in(-1,1)\\
1 &\text{ if   }Y_t>1 \text{ or with probabiliy }P_\text{high}\\
-1 &\text{ if   }Y_t<-1\text{ or with probabiliy }P_\text{low},
\end{cases}
$$
where the choice of probabilities is taken from the estimated probabilities of these events, presented in the previous section. 


We proceed to implement such a model. It is known that the exact solution to Equation for $Y_t$ is given by 
\begin{align}
\tilde{Y}_t=\tilde{Y}_0 e^{-\theta t} +\mu (1-e^{-\theta t})+\sigma\int_0^t e^{-\theta(t-s)}d W_s,
\end{align}
and as such, for any $h>0$, it holds that 
\begin{align}
\tilde{Y}_{t+h}=\tilde{Y}_t e^{-\theta h} +\mu (1-e^{-\theta h})+\sigma\int_t^{t+h} e^{-\theta(h-s)}d W_s.  
\end{align}

[It can be shown](https://arxiv.org/pdf/1811.09312.pdf) that $v:=\sigma\int_t^{t+h} e^{-\theta(h-s)}d W_s$ is a normally distributed random variable with mean 0 and variance $\gamma^2$ given by 
$$\gamma^2:=\frac{\sigma^2}{2\theta}(1-e^{-2\theta h}).$$

Writing $\alpha:=\mu(1-e^{-\theta h})$ and $\phi:=e^{-\theta h}$, one can write  the discrete-time solution for $\tilde{G}_{t+h}$ as an AR(1) process given by 
\begin{align}
\tilde{Y}_{t+1}=\alpha + \phi \tilde{Y}_t  +v, \quad v\overset{iid}{\sim}\mathcal{N}(0,\gamma^2).
\end{align}

Notice that this implies that $[\tilde{Y}_{t+1}-\alpha - \phi \tilde{Y}_t]{\sim}\mathcal{N}(0,\gamma^2).$

Notice, furthermore, that $\alpha,\gamma^2,\phi$ can be estimated with the usual time series techniques.  Once this is done, one can obtain estimates for $\theta,\mu,\sigma$ as 

\begin{align}
\hat{\theta}&=-\frac{1}{h}\log\hat\phi,\\
\hat{\mu}&=\frac{\hat{\alpha}}{1-\hat\phi},\\
\hat{\sigma}^2&=-2\frac{1}{h}\frac{\hat{\gamma}^2}{1-\hat\phi^2}\log\hat\phi,
\end{align}
where $\hat{a}$ represents a given estimator (Least squares, maximum likelihood, etc) of some quantity $a$. Implementing these parameters using the `statsmodels.tsa.arima_model` package, yields the following results for $N_s=10000$ samples.


![](https://i.imgur.com/fJctWdK.png)

which, as it can be seen, also resembles quite well the real distribution of $\tilde{G}_t$, with the caveat that such a process over-samples the low demand valleys (i.e., smaller values of $\tilde{G}_t$). 


### 5.2 On modeling demand 


#### 5.2.1 On modeling demand peaks

Following the discussion in section 3.4,  we can model high (resp. low) demand peaks (resp. valleys) using a Poisson process. Let $\{\tau^H_i\}_{i\in\mathbb{N}}$, $\{ \tau^L_i \}_{i\in\mathbb{N}}$, denote the times between two occurrences of a high demand peak or low demand valley, as defined in section .. One can then model  the times at which  these peaks (resp. valleys) appear by sampling $\tau^H_i\sim\text{Exp}(\lambda^H(\tilde{G}_t))$. This in turn can be combined with the previous two approaches in order to include a value of $\tilde{G}_t>\overline{G}$ every $\tau^H_i\overset{\text{iid}}{\sim}\text{Exp}(\lambda^H(\tilde{G}_t))$ times. 


#### 5.2.2 Demand as a [Hidden Markov Model (HMM)](https://en.wikipedia.org/wiki/Hidden_Markov_model)

In this setting, we model the demand process           $\{D_t\}_{t\geq 0}$ as an unobservable Markov process and $\{\tilde{G}_t\}_{t\geq 0}$ as observable Markov process which depends $\{D_t\}_{t\geq 0}$ as shown in the picture below.  

![](https://i.imgur.com/1b4Dt5P.jpg)

Thus, given measurements from $\{\tilde{G}_t\}_{t\geq 0},$ we aim at inferring the associated process $\{D_t\}_{t\geq 0}$. To that end, we propose the following model. Let us assume that the demand process is a discrete-time, discrete space Markov process taking values in the set of states 

$$\text{States}:=\{ \text{state 1}, \text{ state 2}, \dots, \text{ state $N_m$}   \},\quad N_m\in\mathbb{N},$$


where, clearly, $D_t=\text{Low}$ means that the time $t$ was of low demand for the network, $D_t=\text{Medium low}$ means that at time $t$ the demand on the network was medium-low, and so on. Furthermore, let's assume that  the probability distribution of $\tilde{G}_t$ conditioned on $D_t=s_t$  for any state $s_t\in\text{States}$ is given by 

$$ \underbrace{\tilde{G}_t|D_t=s_t}_\text{$\tilde{G}_t$ conditioned on $D_t=s_t$ } \sim \text{GaussianMixture}(\mathbf{w},\mathbf{m},\mathbf{C};N_m)$$


where $\mathbf{w}=(w_1,\dots,w_{N_M})$, $\mathbf{m}:=(m_1,\dots,m_{N_m})$, $\mathbf{C}:=(C_1,\dots,C_{N_m}),$ $m_i\in\mathbb{R}$, $w_i,C_i\in\mathbb{R}_+,$ $\forall i=1,\dots,N_m$, are $N_m$-dimensional vectors of means, variances, and weights (i.e., $\sum_{i}^{N_m}w_i=1$), respectively, and $$\text{GaussianMixture}(\mathbf{w},\mathbf{m},\mathbf{C})=\sum_{i=1}^{N_m} w_i\mathcal{N}(m_i,C_i)$$ is a mixture of $N_m$ Gaussian distributions, each with weight $w_i$, mean $m_i$ and variance $C_i$. Given this, if one could estimate:
1. The Markov transition matrix $\pi$ for the process $\{D_t\}_{t\geq 0}$, where $\pi_{i,j}$ gives the probability of $D_t$ moving to state $j$ given that it is in state $i$ and
2. the mixture hyper-parameters $\mathbf{w},\mathbf{m},\mathbf{C};N_m$,

Then one could come up with a  model for demand (albeit a discrete-space one), which in turn induces a dynamic for the process $\{\tilde{G}_t\}_{t\geq0}$. 


As an example, we consider a set of $N_m=5$ possible states:

$$\text{States}:=\{ \text{very low demand}, \text{ low demand}, \text{ medium},\text{ high demand}, \text{ very high demand}   \}.$$

We use the [`hmmlearn`](https://hmmlearn.readthedocs.io/en/latest/) python package to train the model and learn the matrix $\pi_{i,j}$ together with the set of hyper-parameters $\mathbf{w},\mathbf{m},\mathbf{C}$. Once such a model has been trained, we use it to classify our data, as shown in the figure below. As we can see on the left, the HMM

![](https://i.imgur.com/qji9rOm.png)

Next, we examine the histograms of $\tilde{G}_t | D_t=s_t$ for each of the 5 considered states. The plots of these histograms are shown below. As we can see, the conditional distribution of $\tilde{G}_t$ given $D_t$ is a mixture of Gaussians

![](https://i.imgur.com/YRD2i9J.png)


Furthermore, simulating the joint process for $\{D_t\}_{t\geq 0}$ and $\{\tilde{G}_t\}_{t\geq 0}$, yields the following results. As we can see from the Figures on the left and in the middle, the time series and the histogram for the normalized gas process resemble the measured data. We plot the last 200 realizations of the demand process $\{D_t\}_{t\geq 0}$  on the figure on the right. 

![](https://i.imgur.com/8NM3FRJ.png)


Lastly, define the following indexation of the states: state 1= high demand, 
state 2=very low demand, state 3=very high demand, state 4=low demand, and state 5=medium demand. We obtain a transition matrix $\pi$ given by 


$$\pi=\begin{pmatrix}
    0.26 &    0.05 &    0.04 &    0.26 &    0.39\\
    0.10 &    0.37 &    0.03 &    0.28 &    0.22\\
    0.28 &    0.04 &    0.04 &    0.25 &    0.39\\
    0.14 &    0.21 &    0.03 &    0.35 &    0.26\\
    0.22 &    0.12 &    0.04 &    0.29 &    0.34
\end{pmatrix},$$

where, to reiterate, $\pi_{i,j}$ represents the probability of $D_{t+1}$ being in state $j$ given that $D_t$ is in state $i$. Lastly, the invariant probability measure $\nu$  of the process $\{D_t\}_{t\geq 0}$ is given by 

$$\nu=\begin{pmatrix}
      0.18 &    0.18 &    0.04 &    0.30 &    0.30
\end{pmatrix}.$$

Here, $\nu_i$ can be interpreted as the probability of finding $\{D_t\}_{t\geq 0}$ in state $i$ at any given time. Notice that this is in agreement with some of our other findings (e.g., about a 4% probability of having very high demand (and hence, usage) in the network).

#### 5.2.3 Other alternatives for modeling demand
Alternatively, one can aim at modeling demand as  a stochastic neural network, that aims at approximating  functions 

$D_\text{drift}:\mathsf{X}_\text{Drift}\to\mathbb{R}_+,$ $D_\text{vol}:\mathsf{X}_\text{vol}\to\mathbb{R}_+,$

$$\mathrm{d}\tilde{G}_t=D_\text{drift}(\text{Parameters}, t)\mathrm{d}t + D_\text{vol}(\text{Parameters}, t) \mathrm{d}W_t.$$

Here, $D_\text{drift}$ and $D_\text{vol}$ are unknown functions representing the change in drift and volatility due to demand. In this setting, one needs to think about what would be  appropriate parameter spaces $\mathsf{X}_\text{drift},\mathsf{X}_\text{vol}$. We remark that this approach would require a significant time commitment and as such, we choose not to pursue it in this particular report. 





### 5.3 Modeling gas by message.

Many of the previously discussed techniques can be directly extended to study each gas component. Here we mention some additional approaches to model gas consumption by the type message.

#### 5.3.1 As an individual, independent process.
We can use the information obtained in Section 4 together with the methods proposed in Section 5.1 to model the individual behavior of each method. More precisely, denote by $\mathcal{M}$ the set of all possible messages, and let $p_{i,t}\in[0,1]$ denote the probability of sending message $i\in\mathcal{M}$ at time $t$. Lastly, denote by $F_i$ the probability distribution of the non-zero realization of gas consumed by message $i$. Then, one could model the gas consumption of the $i^{th}$ by taking the following two steps

1. with probability $p_i$,  sample $\tilde{G}^i_t\sim F_i$.
2. Otherwise set $\tilde{G}^i_t=0.$

 Here, we have used $\tilde{G}^i_t$ to denote the normalized gas consumption of message $i$ at time $t$. We will call this first methodology a frequentist approach. Alternatively, one can use the Poisson process-like interpretation of such a process, where the number of blocks between two non-zero events can be reasonably modeled as a random variable following  an exponential distribution, by iterating the following two steps for each message $i\in\mathcal{M}$:

1. Starting at $\tilde{G}^i_t$, sample $h\sim \text{DistrTimeBetweenNonZeroEvents}_i$
3. Sample $\tilde{G}^i_{t+h}\sim \text{DistrOfNonZeroGas}_i$
 We will refer to this approach as the process approach.  
We implement this methodology for two given messages (`PublishStorageDeals`, and `ProveCommitSector`) and show the results below. As it can be seen, either approach seems to capture the "bulk" of the dynamics quite well, however, they do seem to struggle to capture those exceedingly high values.
 
 
 

![](https://i.imgur.com/R0fSrfK.png)
![](https://i.imgur.com/w0unJkc.png)


Once either model is implemented, can then recover a model for $\tilde{G}_t$ by iterating over all $i\in\mathcal{M}$ and adding all the obtained values of $\tilde{G}^i_t$, i.e., by setting $\tilde{G}_t=\sum_{i\in\mathcal{M}}\tilde{G}^i_t$. A




We remark that this model while being able to capture the frequencies between messages, it is not able able to capture the (admittedly weak) correlation between messages. The following two methods aim at alleviating this issue. 

#### 5.3.2 As a joint process.

As it can be seen from the correlation plot of Section 4.2, only the top 3 messages, namely `ProveCommitSector` `PreCommitSector` and `SubmitWindowedPoSt ` have non-negligible correlation. To capture this, one could fit a 3-dimensional KDE to the normalized gas usage data from these three messages. Denoting the joint probability distribution of these three messages by $F^\text{top}$, one can then repeat the procedure above by sampling $$(\tilde{G}_t^\text{ProveCommitSector},\tilde{G}_t^\text{PreCommitSector},\tilde{G}_t^\text{SubmitWindowedPoSt})\sim F^\text{top},$$ and all the other less impactful variables independently of each other.



We remark that KDE's suffer from the [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality), and as such, their use is often limited to a handful of dimensions (usually less than 4). 



#### 5.3.3 [Using a normalizing flow](https://www.jmlr.org/papers/volume22/19-1028/19-1028.pdf)

Lastly, an additional methodology worth investigating is that of Normalizing Flows (NFs) (or any other generative model) -- a set of emerging machine-learning techniques used to approximate probability distributions. We briefly describe the idea behind such a methodology and then discuss how it could be used in our setting. 

Suppose we have two probability distributions $\mu_\text{target}$ a target probability distribution that we would like to sample from, and a reference probability distribution that is easy to sample from (a multi-variate Gaussian, for example). In the context of  NFs, it is typically the case that sampling from $\mu_\text{target}$ directly is unfeasible. This could happen e.g. because such a probability distribution is not known, it is high-dimensional, etc. Despite this difficulty, it is also often the case that a set of samples from such a distribution is available apriori.  The idea behind  normalizing flows is to use deep neural networks to approximate an invertible map $T$ such that $T_\sharp \mu_\text{target}=\mu_\text{ref}$, i.e., that the pushforward  of $\mu_\text{target}$ through $T$ is the reference measure $\mu_\text{ref}$.  Notice that, in practice,  the measure $\mu_\text{target}$ is approximated by the empirical measure obtained from its samples. Once such an invertible transformation $T$ has been constructed, observing that $\mu_\text{target}=T^{-1}_\sharp(\mu_\text{ref})$ one can then easily generate samples from $$\mu_\text{target}$ by the following algorithm:

1. Sample $Z\sim \mu_\text{ref}$ (easy to do)
2. Transform to a sample from $\mu_\text{target}$ by taking the inverse mapping $T^{-1}$, i.e., $Y=T^{-1}(Z)$.

In our setting, given that we have gas data for all methods,  we can then use this methodology to approximate the joint distribution of the gas consumption across all messages. We aim at investigating this methodology further in a different report.





























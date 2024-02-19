---
tags: research proposals, gas modeling
---

# Research plan proposal: modeling gas consumption in the Filecoin network.
GitHub: https://github.com/protocol/CryptoEconLab-private/tree/main/notebooks/gas_modeling 

###### Juan P. Madrigal Cianci.
------------


## Introduction




**The goal of this project is to develop a probabilistic, data-driven model for gas usage in the Filecoin network**. In particular, we aim at using a mixture of theoretically sound, as well as experimental, state-of-the-art simulation techniques in our implementation. Once such a model has been obtained, it can be implemented in combination with other gas-related models in the Filecoin blockchain, such as the [digital twin model](http://wikipedia.org/en/digital_twin) for the network,  described [here](https://www.overleaf.com/1478878644fqzrjkxszxmx), as well as the gas model for the [Hierarchical Consensus](https://research.protocol.ai/publications/hierarchical-consensus-a-horizontal-scaling-framework-for-blockchains/delarocha2022.pdf) (HC) simulations, being developed in collaboration with the [ConsensusLab](https://research.protocol.ai/groups/consensuslab/). 



## Modeling and possible tools.  

Recall that for an epoch time $h>0$, the base fee $b_{t+h}\in\mathbb{R}_+$ at a time $t+h$ is given by 

$$b_{t+h}=b_t\left(1+\tilde{c}(t)\frac{G_t-G^*}{G^*}\right),$$

where $\tilde{c}(t):=1/8$ is what we will call *control function*, $G_t\in[0,2G^*]$ is the gas usage and $G^*$ is the target gas utilization. For simplicity, we will usually write 

$$\tilde{G}_t:=\frac{G_t-G^*}{G^*}, \quad \tilde{G_t}\in[-1,1].$$


In particular, $\tilde{G}_t$ is a random process that needs to be characterized and which depends on an unknown demand function $D$. Given this formulation (together with the data presented later in the proposal), one could present several modeling and design choices for the gas dynamics on the Filecoin network.


In what follows, we first describe some of the models we have developed in these first three weeks, and then we will describe how to extend them, as well as some research directions.

### Current models.

The ideas described here are based on the notes and experiments presented in the *preliminary results*
section. 
#### Continuous/coarse-grained limit of $b_t$. 
This model is based on the notes [*A continuous-time model for gas in Filecoin*](https://hackmd.io/uPkCaSdHRGOG-5KQ_vwvxg). Intuitively, such a model considers the case where the gas dynamics are simulated for a time $T$ with $h\ll T$ so that, at a heuristic level (as there are some technicalities arising with the differentiability of $b_t$) the dynamic for $b_t$ obeys a Differential Equation (DE). More precisely, redefine the scaling $\tilde{c}(t)=h c(t)$, for some (implicitly small) $h>0$, and some positive function $c:\mathbb{R}_+\to\mathbb{R}_+$. We then have that
\begin{align}
\implies b_{t+h}&=b_t+h b_t{c}(t)\tilde{G}_t \\
b_{t+h}-b_t&=h b_t{c}(t)\tilde{G}_t \\
\implies \frac{b_{t+h}-b_t}{h}&=b_t{c}(t)\tilde{G}_t.
\end{align}
Taking the limit as $h\to 0$ (which again, at a heuristic level can be interpreted as $h$ being extremely small for the time scales considered) yields
\begin{align}
\lim_{h\to 0}\frac{b_{t+h}-b_t}{h}&=\frac{\mathrm{d}b}{\mathrm{d}t}(t)=b(t){c}(t)\tilde{G}_t,
\end{align}
which yields a continuous-time evolution form for $b_t=:b(t)$. Furthermore, notice that, given some known value of $b_t$ at some some point in time $t_0$, denoted by $b_{t_0}=b(t_0)$, as well as some technical conditions on $\tilde{G}$ and $c(t),$ the previous DE can be solved by separation of variables; indeed
\begin{align}
\frac{\mathrm{d}b}{\mathrm{d}t}(t)&=b(t){c}(t)\tilde{G}_t,\\
\implies \int\frac{\mathrm{d}b}{b}(t)&=\int{c}(t)\tilde{G}_t\mathrm{d}t+c'\\
\implies \ln b(t)&=\int{c}(t)\tilde{G}_t\mathrm{d}t+c'\\
\implies  b(t)&=Ke^{\int{c}(t)\tilde{G}_t\mathrm{d}t}, \end{align}
where $K=b(t_0)\exp\left(-F(t_0)\right)$, and $F(t)=\int{c}(t)\tilde{G}_t\mathrm{d}t$.

**Remark 1.** In general, we will not be able to analytically compute the integral in the previous equation. Instead, we will likely have to resort to numerically approximating it using some given quadrature rule.  


**Remark 2.** An interesting remark worth noting is that AX independently arrived at [essentially the same formula for $b_t$](https://hackmd.io/@R02mDHrYQ3C4PFmNaxF5bw/B12vha869) using a [coarse-grained](https://en.wikipedia.org/wiki/Coarse-grained_modeling) interpretation of this process. 
 
#### Random behaviour of $\tilde{G}_t$. 

The notes [*A continuous-time model for gas in Filecoin*](https://hackmd.io/uPkCaSdHRGOG-5KQ_vwvxg) also propose to model $\tilde{G}_t$ as an [Ornstein-Uhlenbeck](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process) (OU) process, i.e., they propose to model $\tilde{G}_t$ as the solution of the following Stochastic Differential Equation (SDE): 

\begin{align}
\mathrm{d} \tilde{G}_t=\theta(\mu-\tilde G_t)\mathrm{d}t +\sigma \mathrm{d}W_t,
\end{align}
where $\theta\in\mathbb{R}_+$ is the mean reversion rate, $\mu\in\mathbb{R}$ is the mean of the OU process, $\sigma\in\mathbb{R}_+$ is its standard deviation, and $W_t$ is the [Wienner process](https://en.wikipedia.org/wiki/Wiener_process). As an example, the picture below presents the plot of $\tilde{G}_t$ for measured data (in blue) and simulated data with a fitted OU process (in orange). As it can be seen from the plot, the overall behaviour  between the measured and simulated data is essentially the same, at least in the [eye norm](https://en.wikipedia.org/wiki/naked_eye).

![](https://i.imgur.com/k58QB66.png)



We remark that the OU process is Markovian, stationary, and mean-reverting. 

It is worth mentioning that since $\tilde{G}_t$ is bounded, perhaps a better alternative is to model the gas consumption as $\tilde{G_t}:=s(G'_t)$, where $G'_t$ follows an OU process and $s:\mathbb{R}\to[-1,1]$ is a [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function).



In a more general setting, such a model can be written as 

\begin{align}
\mathrm{d} \tilde{G}_t=D(t,\tilde{G}_t,\Theta)\mathrm{d}t +\sigma \mathrm{d}W_t, \tag{1}
\end{align}
to include some demand process $D$, which could potentially depend on time, $G_t$ and a set of unknown parameters $\Theta$. Notice that the inclusion of this demand process does not guarantee mean reversion anymore. 

At an even more general level, one could extend this model for gas consumption to:

\begin{align}
\tilde{G}_t=\sum_{m=1}^M \sum_{\ell=1}^\mathcal{L}\tilde{G}^{m,\ell}_t, \tag{2}
\end{align}
where each term $\tilde{G}^{m,\ell}_t$ corresponds to the normalized gas usage of method $m=1,2,\dots,M$ in gas lane $\ell=1,2,\dots,\mathcal{L}$, and has its own governing dynamics.  It is worth mentioning that, as for now, $\mathcal{L}=1$.    

#### High demand peaks as a random process.

Let $\overline{G}\in[0,1]$ and $\underline{G}\in[-1,0]$ be some threshold values. We define the high (resp. low) demand process $\{H_t\}$ (resp. $\{L_t\}$) as
\begin{align}
\{H_t\}_{t\geq 0}&:=\{1 \text{ if }G_t\geq \overline{G}, \ 0 \text{ otherwise}\}_{t\geq 0}\\
\{L_t\}_{t\geq 0}&:=\{1 \text{ if }G_t\leq \underline{G}, \ 0 \text{ otherwise}\}_{t\geq 0}.
\end{align}


Notice that the distribution of interarrival times (e.g., the time between two consecutive high/low usage periods) can be relatively well approximated by an exponential distribution  as shown below:

![](https://i.imgur.com/JCLzpxy.png)

where we have taken $\overline{G}=0.99$ and $\underline{G}=-0.7$. 

We remark that we are implicitly assuming that the (random) time between any two high-usage peaks is continuous. Although this is not the case, it can be thought of as a large-scale (in time) approximation. 

If one furthermore assumes that these interarrival times are independently distributed, it can be shown (c.f. Kroese et al (2013), p. 172) that the process behind a high-demand (resp. low-demand) usage is a [Poisson process](https://en.wikipedia.org/wiki/Poisson_point_process). 





## Key questions to answer

Given that the main focus of our proposed work is to present and validate a model for gas usage in the Filecoin network, we will aim at answering -or at the very least, shedding some light to- the following questions:


1. What are the strengths/weaknesses of our proposed models? How accurate are they? What are some sensible metrics to validate our models?
2. How can one model the underlying, unobservable demand function for the gas process? What should it depend on? Other than having demand proportional to gas usage, what else is a desirable behavior of this function? According to Maria, it is reasonable to assume that network power plays a part, as the number of proofs sent scale with the amount of power in the network. She also suggested that  maybe FIL price would likely play a role in this price, and I agree with this. 
3. How should one model the gas consumption of each method or actor (e.g., `ProveCommitSector`, c.f. [Filecoin specifications](https://spec.filecoin.io/#section-systems.filecoin_vm.sysactors))? 
4. Is the "control term" $c(t)=1/8$ in the base fee formulation optimal in a given sense? Would the network benefit from a different, potentially non-constant control term?
5. Could one predict gas consumption (and consequently, base fee, or other quantities of interest) for a given time scale? if so, could one estimate the uncertainty in this prediction? Furthermore, could one present uncertainty estimates for a given quantity of interest from this process? 
6. Is there any clear functional relation among gas-consuming methods?  How does each method contribute to the overall gas consumption? 
7. Can one provide theoretical estimates on the long-term behavior or the statistical properties of the proposed methods? 
8. How can one use the proposed method to improve the batch balancer (c.f. [FIP0013](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0013.md#incentive-considerations) and [FIP0024](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0024.md))?
9. How can this be extended to the hierarchical consensus case?
10. How would FVM affect this gas consumption?




## Proposed work

We will devide the outcome of this research into (i) short-term goals and (ii) medium-term goals.


### Short-term goals


#### A complete model for network demand. 

So far, we don't have a complete and robust model for network demand. One of our short-term goals is then to expand our current model. We envision three possible approaches. We remark that these approaches are not necessarily mutually exclusive. 

1. One possible model for the demand process is to split its components into a high/low demand usage and a "normal" demand process. While a Poisson process can be used to model high/low-demand peaks, one would need to explore the process for "normal" demand in more detail. 
2. Notice that, although a "demand process" is not directly observable, the gas usage associated with such a process is. Thus, one could potentially model this demand process as some sort of  [Hidden Markov Model](https://en.wikipedia.org/wiki/Hidden_Markov_model). A similar approach has been attempted in [Yu and Sheble (2006)](https://sci-hub.se/10.1016/j.epsr.2005.09.013), to model demand in electricity markets.
3. On a similar note, one could attempt to approximate an arbitrary demand function $D$ given the proposed dynamics for $G_t$ in Equation (1). In this setting, $D$ is a deterministic function of some stochastic input $\tilde{G}_t.$ One way of attempting to do this is with state-of-the-art machine learning techniques, such as Neural SDEs ([c.f. Kidger et al (2021)](https://arxiv.org/abs/2102.03657)).
4. After discussing with AX, another possible model for gas demand can be given by investigating the covariance  structure $K(i,j)$ between any two times  of high-demand $t_i,t_j$, and seeing wheather it can be written as $K(i,j)=\beta|t_i-t_j|^\alpha$, for some given parameters $\alpha$ and $\beta$. According to AX, this convariance structure has some interesting scale-invariant properties.


#### Modeling of gas consumption per method. 

While an aggregate model for gas consumption [seems to work fairly well](https://hackmd.io/5lcDIN23SJOrWrwy8f4Hpg), one could gain a greater degree of granularity in the model (and hence, robustness) by modeling each  $\tilde{G_t}^{m,\ell}$, $m=1,\dots,M$, $\ell=1,\dots,\mathcal{L}$, individually.  Alternatively, one could group each component of the gas usage by an actor. 


#### Gas modeling for hierarchical consensus

The results from the previous two subsections can be combined with the ideas behind hierarchical consensus. A possible way of doing this is to assume that each subnet (child-net) has a similar model as the one we are considering for the non-hierarchical version of the model, albeit with different parameters. This setting fits fairly well in the "gas-lane" model,  however, one should be careful to include interactions across sibiling chains, as well as up-and-down messages. 



### Medium and long-term goals

Here we present some medium to long-term goals (or applications) for the outcome of this research proposal. There is not a clear deadline for these goals at the time of writing, however, this should be discussed and updated. 

1. **FIP proposal to update the batch balancer**. Once a gas model has been proposed and tested, one could potentially move to the longer-term goal of proposing a FIP to improve the batch balancer. 
2. **A go-to model for FIP consideration**. Furthermore, once these models are up and running, they can be used to better justify arguments regarding FIPs. 
3. **Extension into another research project**. Naturally, one could go extremely deep on the models considered here-in. A more dedicated study on aby one of the parts (modeling gas demand, for example) could become a ersearch project in itself, perhaps aimed at some dedicated research fellow (a PL-funded Ph.D, for example). 
4. **Modeling effect of FVM**. Lastly, one could try to predict how the implementation of the FVM would affect the gas consumption on the network. While it is reasonable to assume that such gas consumption would increase, it is crucial to understand how, and by how much. This can be done by, e.g., looking at data from other blockchains. 




### Possible tools and methodologies

 We intend to implement most (if not all) of our analysis and simulations in  Python. For the sake of completeness, we present a non-comprehensive, non-binding, list of possible tools that can be used in this project. 

1. **Random processes and their simulation.** Although there are a handful of packages to implement these processes, it is the opinion of the author that, in most cases, they are simple enough to implement "from scratch". Two widely-used references for these methods are [Kroese et al (2013)](https://books.google.com.co/books?hl=en&lr=&id=Trj9HQ7G8TUC&oi=fnd&pg=PA1&dq=kroese+handbook&ots=1FWbDcXazI&sig=Fouxa7PpNelnslAFwzP3VDlQOYY&redir_esc=y#v=onepage&q=kroese%20handbook&f=false) for a rather hands-on approach,  and [Ross (2014)](https://books.google.com.co/books/about/Introduction_to_Probability_Models.html?id=wGOMDwAAQBAJ&printsec=frontcover&source=kp_read_button&hl=en&redir_esc=y#v=onepage&q&f=false) for a more theoretical discussion.
2. **Parameter estimation and function approximation.** Parameter estimation can be done using either Markov Chain Monte Carlo (MCMC) methods (which will typically also provide uncertainty estimates on such a parameter), which are fairly simple to implement from scratch, or optimization-based methods, such as maximal likelihood estimation, which can be implemented using standard optimization packages. Functional approximation for the tasks at hand is perhaps best done using neural network models, which can be implemented in `TensorFlow` or `PyTorch`.
4. **Time series modeling and analysis.** This could be done using Meta's `Prophet` library or the `statools` time series analysis package if using *traditional* time-series analysis. Alternatively, one could use e.g., `keras`, if using more recent, machine learning-based models. 
5. **(forward) Uncertainty quantification.** Once a model is proposed and backtested, one could do (forward) uncertainty quantification of some given quantity of interest, using Monte Carlo methods. Once again, I believe these methodologies are simpler to implement "by hand", especially if the need arises for an advanced type of Monte Carlo sampler (i.e., with the aims of reducing variance, computational cost, etc.) 







## Datasets
We will mostly use the following datasets obtained from [Sentinel](https://lilium.sh/):

* [`derived_gas_output`](https://lilium.sh/data/models/#derived_gas_outputs), which provides data on derived gas costs resulting from the execution of a message in the VM. Each message is indexed by its `CID`. 
* [`message_gas_economy`](https://lilium.sh/data/models/#message_gas_economy), which gives gas economics for all messages (indexed by their `CID`) in all blocks at each epoch.

We remark that, although there is a wealth of information on the two previous datasets, it is not possible to uniquely identify the type of method being used on each message.  To achieve this, we cross-reference the message `CID` on the previous datasets with those in [`parsed_messages`](https://lilium.sh/data/models/#parsed_messages) which do provide a unique name to each used method. 


To more easily integrate these datasets (stored as as `PostgreSQL` database) with our models (written in `python`), we have developed a data module ([`utils/getData.py`](https://github.com/juanpmcianci/GasModeling/blob/main/utils/getData.py)) which queries such any given Sentinel dataset (given just its name and possibly a minimum block number) and outputs the query as a `pandas` data frame. 


## Work plan, milestones, and deliverables. 



The following plan is an estimation of the weekly workload for the execution of this project. This timeline is based on the onboarding document and assumes that the author will be working on this project, as well as on the hierarchical consensus project simultaneously, with the workload between both projects split equally.  Furthermore, the timeline assumes a familiarity with the inner workings of the Filecoin network, as well as with other existing gas models, which are equivalent to the first three weeks of the [onboarding document](https://docs.google.com/document/d/1egdPibTePh6y_DZ8vjQdmpO7vwtxgayui5ilww_27Uo/edit).

#### **Task 1** - Empirical analysis of gas consumption and model proposal. Due: August 26, 2022. 

This task consists of a report covering (1) a thorough data analysis of the gas dynamics at hand, exploring things such as the statistical properties of such dynamics for each method, the relative contribution of each method and actor, and the correlation among each method, etc, and (2) one or several modeling techniques for the gas consumption of each method or actor family. 


#### **Task 2** - Model validation, simulations, and theoretical analysis. Due: September 2nd, 2022. 

This task consists of validating and back-testing the proposed model(s). Crucial to this task is the proposal and development of suitable validation metrics.  Such a task is crucial for the model, as in the case where the proposed methodologies do not reflect reality, then, an iteration of Task 1 must be performed. This task should end up in a short write-up detailing the models tested and their validation, and it should ideally be approved by the rest of the team. 

#### **Task 3** - Finalized report. Due: September 2, 2022. 

The last task of this project consists of putting together a complete report for the gas model, its findings, use cases, potential limitations, etc. It should also provide a well-documented code base for the methods used, in the hopes that the methodologies developed in this project can be used for future projects.  


In short, we envision the following deliverables as an outcome of this project: 
1. A well-documented and modular repository of codes used to run the model. Ideally, some of the methods implemented therein should be able to be seamlessly combined with other future, related projects.
2. A written report detailing the produced model(s).
3. In addition, such a report could eventually become a talk at a CryptoEcon day, or -perhaps more ambitiously- it could be finalized as a submission to a leading peer-reviewed conference or journal. 



## Risks and difficulties
This project aims to characterize a highly complex, multi-scale, and stochastic dynamical system depending on a wide array of variables, not all of which can be easily modeled or even identifiable. Thus, the model at hand is anything but trivial, and several sources of *risk* (as in falling behind of schedule) may arise. 

Given the high complexity of these processes, coming up with models that correctly capture the dynamics at hand might become a tougher-than-expected task. A potential risk mitigation measure would be to start building up on top of relatively simple models and iterate with the team. 

In addition, validating the models might also prove to be challenging, and as such, appropriate validation measures, as well as discussion with the team when tackling Task 2 is heavily encouraged. 

Although we do not anticipate this to be an issue --at least for now--, it could still happen that the resulting model is computationally expensive to run. A computationally expensive model can quickly become prohibitively expensive to run when using it inside a Monte Carlo simulation. Thus, efficient implementation of the computational techniques used in this project is a must. 

An additional computational difficulty is the size of some of the datasets. As an example, a mixed query of the three previously-mentioned datasets including relevant gas information from blocks 2045000 to 2055500, worth roughly 3.6 days of data (assuming 1 block every 30s) requires storing a dataset of around 500MB. This is not an extremely large dataset, however, it can quickly become  computationally expensive  to operate on, once a larger period is considered. One can mitigate the cost by either averaging information over $m\in\mathbb{N}$ blocks, or by querying the dataset every $k\in\mathbb{N}$ blocks, however, this will likely imply a loss in the granularity of the data. 



## Important links and references

### Housekeeping

1. GitHub Repo: https://github.com/juanpmcianci/GasModeling 
2. Roadmap: https://www.notion.so/pl-strflt/3e7a7e17816341b4ae08a69aca02eff0?v=277c15267e154da185867b93f27cf26d&p=a08d28a79f0441539816625510cb52bc&pm=s

### Preliminary results


1.  [A continuous-time model for gas in Filecoin](https://hackmd.io/uPkCaSdHRGOG-5KQ_vwvxg). In these notes, we present our first mathematical model for gas consumption. In particular, such a model assumes that the network gas usage $G_t$ behaves as an [Ornstein-Uhlenbeck process](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process). It also includes a first work towards modeling the gas usage of each method as the same type of process. 
2.  [Gas usage and base fee](https://hackmd.io/5lcDIN23SJOrWrwy8f4Hpg). This is an exported Jupyter Notebook where we investigate and validate the model presented above. From the data explored there, it is somewhat reasonable to assume that the total gas consumption (i.e., gas usage across all methods) behaves, roughly as an OU process. 
3. [scrips for analyzing gas consumption and base fee behaviour](https://github.com/juanpmcianci/GasModeling/blob/main/scripts/AnalyseGasConsumption.py)
4. [Script to analyze gas consumption by method](https://github.com/juanpmcianci/GasModeling/blob/main/scripts/gasByMethod.py)




### References

1. Kroese, Dirk P., Thomas Taimre, and Zdravko I. Botev. *Handbook of Monte Carlo methods*. John Wiley & Sons, 2013.
2. Kidger, Patrick, et al. *Neural SDEs as infinite-dimensional GANs.* International Conference on Machine Learning. PMLR, 2021.
3. Ross, Sheldon M. *Introduction to probability models*. Academic Press, 2014.
4. Yu, Wang, and Gerald B. Sheblé. *Modeling electricity markets with hidden Markov model.* Electric power systems research 76.6-7 (2006): 445-451.
5. Moore, Ian C., and Jagdeep Sidhu. *Stochastic Properties of EIP-1559 Basefees.* arXiv preprint arXiv:2105.03521 (2021).

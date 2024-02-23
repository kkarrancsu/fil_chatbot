---
title: Rationale behind locked pledge sector expiration models
tags: FIPs
---

# Rationale behind locked pledge sector expiration models

The purpose of this note is two-fold: to put the approximations we've been using in practice on more solid ground, and to develop a general model to deal with more complex pledge expiration behavior.

**Notation**
* $L_{t}$ --- locked pledge at day $t$
* $L_{t}^\text{i}$ --- newly locked pledge at day $t$ (locked pledge inflow).
* $g_{t,\tau}$ --- probability distribution function (pdf) of sector lifetime including subsequent renewals, of duration $\tau$, on day $t$. This can be thought of as a distribution of sealing durations, that's also changing with time itself.
* $G_{t,\tau}$ --- cdf of sector lifetime including subsequent renewals, of duration $\tau$, on day $t$
* $S_{t,\tau}$ --- survival function of sector lifetime subsequent renewals, of duration $\tau$, on day $t$
* $\tilde{g}_{\tau}$ --- pdf of effective single lifetime of duration $\tau$, not including renewals. 'Single effective' in the sense the sealing distribution is stationary. Same distribution now as in a year etc.
* $\tilde{G}_{\tau}$ --- cdf of effective single lifetime of duration $\tau$, not including renewals
* $\tilde{S}_{\tau}$ --- survival function of effective single lifetime of duration $\tau$, not including renewals
* $e_t$ is the probability of expiration
* $r_t$ is the probability of renewal

## Basic proposition

**Claim**

The locked pledge at time $t$ ($L_{t}$), is given by incrementing locked pledge one day before, plus the new locked pledge inflow ($L_{t}^\text{i}$), less the convolution of the pledge inflow history with the pledge lifetime probability distribution function $g$,

\begin{align*}
L_{t} & \mathrel{+}=L_{t}^\text{i}-\left(L^\text{i}*g\right)_{t}\,.\\
\end{align*}
This is intuitive but let's see for sure why this works.

**Proof**

The total locked pledge at time $t$ is given by the sum of new locked pledges at all previous times multiplied by their probability of surviving $\tau$ days:

\begin{align*}
L_t & =\sum_{\tau\le t}\text{NLP}_{t-\tau}\,S_{t,\tau}\\
 & =\sum_{\tau\le t}\text{NLP}_{t-\tau}\,\left(1-G_{t,\tau}\right)
\end{align*}

where the survival function is related to the cumulative distribution function of the sealing lifetime as $S_{t,\tau}=1-G_{t,\tau}$. 

The *daily change* in locked pledge is given by
\begin{align*}
L_t-L_{t-1} & =\sum_{\tau\le t}\text{NLP}_{t-\tau}\,\left(1-G_{t,\tau}\right)-\sum_{\tau\le t-1}\text{NLP}_{t-\tau}\,\left(1-G_{t,\tau}\right)\\
 & =\left(\sum_{\tau\le t}\text{NLP}_{t-\tau}-\sum_{\tau\le t-1}\text{NLP}_{t-\tau}\right)+\left(\sum_{\tau\le t}\text{NLP}_{t-\tau}\left(-G_{t,\tau}\right)-\sum_{\tau\le t-1}\text{NLP}_{t-\tau}\left(-G_{t,\tau}\right)\right)\\
 & =\left(\text{NLP}_{t}\right)+\left(\sum_{\tau\le t}\text{NLP}_{t-\tau}\left(-G_{t,\tau}\right)-\sum_{\tau\le t-1}\text{NLP}_{t-\tau}\left(-G_{t,\tau}\right)\right)\\
 & =\text{NLP}_{t}-\left(\sum_{\tau\le t}\text{NLP}_{t-\tau}G_{t,\tau}-\sum_{\tau\le t-1}\text{NLP}_{t-\tau}G_{t,\tau}\right)\\
 & =\text{NLP}_{t}-\left(\sum_{\tau\le t}\text{NLP}_{t-\tau}\left(G_{t,\tau}-G_{t,\tau-1}\right)\right)\\
 & =\text{NLP}_{t}-\sum_{\tau\le t}\text{NLP}_{t-\tau}g_{t,\tau}
\end{align*}

It therefore follows

\begin{align*}
L_{t} & =L_{t-1}+\text{NLP}_{t}-\sum_{\tau\le t}\text{NLP}_{t-\tau}g_{t,\tau}\\
\end{align*}
and 

\begin{align*}
L_{t} & +=\text{NLP}_{t}-\sum_{\tau\le t}\text{NLP}_{t-\tau}g_{t,\tau}\\
 & +=\text{NLP}_{t}-\left(\text{NLP}*g\right)_{t}\\
\end{align*}
as claimed above. So the sealing dynamics can equivalently be cast in the form of survival model with surivival distribution $S$, or directly in terms of the pdf for the sealing duration $g$. This may seem like a minor point, but it's useful for understanding, and gives us some implementation flexibility. 

## Simple practical approximations

The pdf of sealing lifetime including renewals $g_{t,\tau}$ can worked out from empirical data, but as it's a 2d --- the duration distribution is also changing with time --- it's worth trying to simplify our calculations. We can do this by writing in terms of a stationary effective duration distribution $\tilde{g}_{\tau}$, times the extension rate $e_{t}$ on that day:

\begin{align*}
g_{t,\tau} & :=\left(1-r_{t}\right)\tilde{g}_{\tau}\\
 & =e_{t}\tilde{g}_{\tau}\,.
\end{align*}

Then

\begin{align*}
L_t & +=\text{NLP}_{t}-\sum_{\tau\le t}\text{NLP}_{t-\tau}g_{t,\tau}\\
 & +=\text{NLP}_{t}-e_{t}\sum_{\tau\le t}\text{NLP}_{t-\tau}\tilde{g}_{\tau}\,.
\end{align*}

The average daily expiration rate $e_{t}$ is easily available from empirical data. For the term $\tilde{g}_{\tau}$, from EDA there a few approximations that are likely not terrible:

* $\tilde{g}_{\tau}^{\text{}}=\delta_{\tau-365}$ . A delta distribution to look back what the newly locked pledge was a year ago to subtract as an outflow. 
* $\tilde{g}_{\tau}=\frac{1}{3}\left(\delta_{\tau-180}+\delta_{\tau-365}+\delta_{\tau-540}\right)$. Generalising the above to the three equimodal delta distributions at the three spikes identified in exploratory data analysis. 

The first approximation is the simplest. It gives the dynamics

\begin{align*}
L_t& +=\text{NLP}_{t}-e_{t}\sum_{\tau\le t}\text{NLP}_{t-\tau}\tilde{g}_{\tau}\\
 & +=\text{NLP}_{t}-e_{t}\sum_{\tau\le t}\text{NLP}_{t-\tau}\delta_{\tau-365}\\
 & +=\text{NLP}_{t}-e_{t}\text{NLP}_{t-365}\,.\\
\end{align*}

To put this in words, the locked pledge today, is equal to locked pledge yesterday, plus new pledge today, less the new pledge locked 1 year ago times the probability of sealing extension today.

If the average sealing lifetime increases from 365 days at time $t'$, an average of $d$ days thereafter, then the dynamics including the future counterfactual scenario follow:

\begin{align*}
L_t+ & =\text{NLP}_{t}-e_{t}\begin{cases}
\text{NLP}_{t-365} & t<t'+d\\
\text{NLP}_{t-d} & t\ge t'+d
\end{cases}\\
\end{align*}

The shortcomings of this approximation are that is undersmooths the locked dynamics. 

The second option, which is more realistic, follows the dynamics

\begin{align*}
L_t & +=\text{NLP}_{t}-e_{t}\sum_{\tau\le t}\text{NLP}_{t-\tau}\tilde{g}_{\tau}\\
 & +=\text{NLP}_{t}-\frac{e_{t}}{3}\sum_{\tau\le t}\left(\text{NLP}_{t-\tau}\delta_{\tau-180}+\text{NLP}_{t-\tau}\delta_{\tau-365}+\text{NLP}_{t-\tau}\delta_{\tau-540}\right)\\
 & +=\text{NLP}_{t}-\frac{e_{t}}{3}\left(\text{NLP}_{t-180}+\text{NLP}_{t-365}+\text{NLP}_{t-540}\right)\\
\end{align*}

Again, if the average sealing lifetime increases from 365 days at time $t'$, an average of $d$ days thereafter, then the dynamics including the future counterfactual scenario follow:

\begin{align*}
L_t+ & =\text{NLP}_{t}-\frac{e_{t}}{3}\begin{cases}
\left(\text{NLP}_{t-180}+\text{NLP}_{t-365}+\text{NLP}_{t-540}\right) & t<t'+180\cdot\frac{365}{d}\\
\left(\text{NLP}_{t-d}+\text{NLP}_{t-365}+\text{NLP}_{t-540}\right) & t'+180\cdot\frac{365}{d}\le t<t'+365\cdot\frac{365}{d}\\
\left(\text{NLP}_{t-d}+\text{NLP}_{t-d}+\text{NLP}_{t-540}\right) & t'+365\cdot\frac{365}{d}\le t<t'+540\cdot\frac{365}{d}\\
\left(\text{NLP}_{t-d}+\text{NLP}_{t-d}+\text{NLP}_{t-d}\right) & t'+540\cdot\frac{365}{d}\le t
\end{cases}\\
\end{align*}


## General approach

A statistical inference-based approach is to find an effective survival function $\hat{S}_{\tau}$ from the past data:

\begin{align*}
L_t=\sum_{\tau\le t}L^\text{i}_{t-\tau}\hat{S}_{\tau}\,.
\end{align*}

In the context of predictive modeling, including counterfactual scenarios where the average sealing duration changes to $d$ from $d'$ at time $t'$, this can be handled as

\begin{align*}
L_t=\begin{cases}
\sum_{\tau\le t}L^\text{i}_{t-\tau}\hat{S}_{\tau} & t<t'\\
\hat{S}_{t-t'}\sum_{\tau\le t}L^\text{i}_{t-\tau}\hat{S}_{\tau}+(1-\hat{S}_{t-t'})\frac{d}{d'}\sum_{\tau\le t}L^\text{i}_{t-\tau}\hat{S}_{\tau} & t\ge t'
\end{cases}\,.
\end{align*}
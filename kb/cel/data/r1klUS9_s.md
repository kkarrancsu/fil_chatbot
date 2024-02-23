# Coarse Grained EIP 1559

## EIP 1559 preliminaries.
EIP 1559 is a mechanism for determining the base fee for gas usage. There is a target block size, we call $B^T$, which is the optimal amount of gas the blockchain can consistently process. 

The actual blocksize that gets commited to the chain is actually flexible, and depends on the number of users who can afford the current base fee. There is a maximum block size of $2B^T$.

We call $B_t$ the actual realized block size at time $t$. Also $b_t$ is the base fee at that time. The base fee updating rule is then 
$$b_{t+\varepsilon}=\left(1+c\frac{B_t-B^T}{B^T}\right)b_t$$
with the constant set at $c=1/8$, and $\varepsilon$ is the epoch duration.

*We wish to derive a continuous time version of this base fee evolution, which we could use to make simpler gas models*. The time variable heres, $t$ is defined only in discrete epochs.

### Continuous limit?

The EIP 1559 equation clearly looks like a difference equation, where we could just take the continuous limit: $\varepsilon\to 0$, which would give us a differential equation, as
$$\lim_{\varepsilon\to0}\frac{b_{t+\varepsilon}-b_t}{\varepsilon}=\frac{d b_t}{dt}=\lim_{\varepsilon
\to 0}c\frac{B_t-B^T}{\varepsilon B^T}b_t $$

There are actually two problems here, the first of which is more philosophical. We are free to mathematically *let $\varepsilon$ go to zero*, but in reality $\varepsilon$ doesn't really *go* anywhere, it is a constant set at 30s. So this is not the actual limit that describes reality. In reality what we mean by *continuous* limit, is that we are looking at time scales that are too long, to care about the local epoch to epoch dynamics.


The second problem si that to take the continuous limit of some function defined only at discrete epoch intervals, we would need the $\lim_{\varepsilon\to0}b_{t+\varepsilon}-b_t\sim \varepsilon$. That is, if we want a finite continuous derivative then it should be true that
$$c\frac{B_t-B^T}{B^T}b_t\to \varepsilon$$
for large $\varepsilon$.

We simply don't know if this condition is true, empirically, because we are not actually changing values of $\varepsilon$ in real life to see what would happen. In fact in the current data it seems epoch-to epoch fluctuations are pretty significant, so not necessarily always true that $b_{t+\varepsilon}\approx b_t$.

## Coarse grained limit

Instead we need to consider a coarse grain limit, where *we dont vary the value of $\varepsilon$, instead we only look at longer time scales, where epoch to epoch fluctuations are irrelevant.

This coarse graining procedure is inspired from condensed matter physics, where spatial coarse graining is regularly done, to study the long scale dynamics of some lattice based system (see for example an appication to the [Ising Model](https://link.springer.com/content/pdf/bbm%3A978-1-4614-1487-2%2F1.pdf)).

For convenience, let us redefine the quantity,
$$G_t=c\frac{B_t-B^T}{B^T}\in[-c,c]$$

The first step for coarse grainig is to consider the evolution of base fee after a large "box" of $n$ epochs,
$$b_{t+n\varepsilon}=b_t\prod_{i=1}^n\left(1+G_{t+i\varepsilon}\right)$$

**the main assumptions of the coarse graining procedure are that**
* there are short scale fluctuations that happen within the box that we can ignore
* The actual long-scale dynamics we care about happen on a much larger scale than the box size of $n$ epochs.

These assumptions mean we can parametrize as
$$G_{t+i\varepsilon}=\frac{\mathcal{G}_{t}}{n}+\sigma_{t+i\varepsilon},$$
where $\mathcal{G}_t=\sum_{i=1}^n G_{t+i\varepsilon}$. We assume that $\mathcal{G}_{t+i\varepsilon}/n$ represents the trend we care about, which remains constant throught the whole box, and $\sigma_{t+i\varepsilon}$ are short scale fluctuations that we do not care about, and generally cancel each other out
$$\sum_{i=1}^n\sigma_{t+i\varepsilon}\approx 0$$
as we take large enough $n$.

we then have 
$$b_{t+n\varepsilon}=b_t\left[\left(1+\frac{\mathcal{G}_{t}}{n}\right)^n+\mathcal{O}\left(\frac{1}{n}\right)\right]$$
where the $\mathcal{O}\left(\frac{1}{n}\right)$ corrections come from the non-cancellation of in-box fluctuations, if the box is not large enough.

We can now take the large-box limit. We define the box duration, $\tau=n\epsilon$. In the large $n$ limit we then have
$$b_{t+\tau}=\lim_{n\to\infty}\left(1+\frac{\mathcal{G}_t}{n}\right)^n\,\,b_t=e^{\mathcal{G}_t}b_t.$$


## Longer time scale phenomena

We now consider that we are studying phenomena at a time scale, $\Lambda$ which is much larger than the box size $\tau$

Let's say for instance $\Lambda=N\tau$ with large $N$, then
$$b_{t+\Lambda}=e^{\sum_{j=1}^N \mathcal{G}_{t+j\tau}}b_t$$

Since real phenomena we care about happen at a much longer time scale, we assume box to box fluctuations are small, which means we can take the coninuum limit of this sum.

We define $\Gamma_t=G_t/N$, so
$$b_{t+\Lambda}=e^{\int_t^{t+\Lambda}\Gamma_{t^\prime} \,\,dt^\prime}b_t$$



## Incorporating external demand vs reaction to base fee

We assume there is an external demand $D_t$ signal that drives the base fee, this represents the total amount of gas that exists, that would like to be included on the blockchain. The amount that actually gets included actualy depends on the current base fee, and how much value the users place on that particular transaction.

We model this value distribution with an exponential distribution (see for example [here](https://github.com/AxCortesCubero/HC-gas-simulation/blob/4bcfe359aed86288ef1669dbece0dfc15f9f84ed/HC%20gas%20simulation.ipynb) for more details).

We assume a value distribution, with cumulative distribution $F(v)$ (this could be an exponential distribution for example as we have used before).

For a given amount of demand $D_T$, we the block size that will be realized is 
$$B_t=D_t[1-F(b_t)]$$

We define a  Demand variable rescaled to the appropriate time scales,
$$\mathcal{D}_t=\frac{D_t}{nN}$$.

Then the evolution of the base fee, driven by a given external demand is
$$b_{t+\Lambda}=e^{\int_t^{t+\Lambda}\mathcal{D}_t\left[1-F(b_{t^\prime})\right]\,\,dt^\prime}b_t.$$

We note that it is not really trivial how to solve this integral equation.

### Re-introducing long-range noise

While we are not interested in epoch to epoch fluctuations, we may want to model more long range fluctuations around our deterministic base fee function. This can be done by introducing a stochastic integral (something like):,
$$b_{t+\Lambda}=e^{\int_t^{t+\Lambda}\mathcal{D}_t\left[1-F(b_{t^\prime})\right]\,\,dt^\prime+\sigma \mathrm{d}W_{t^\prime}}b_t.$$

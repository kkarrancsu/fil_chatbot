# Understanding Dilution of value, and maximum supply

## Summary

- We explore the question *"what should maximum supply mean for a cryptocurrency investor"?*
- We quantify the impact on inflation of a programmed increase in token supply.
- We define a **time-weighted diluted price** as a useful metric that quantifies how increases in token supply would affect an investor's decision making.

## Fully diluted value vs constant market cap

Many cryptocurrencies define a maximum amount of tokens that will ever be minted, and a schedule for how these would be released over time. What importance should these parameters have for an investor?

Increasing the token supply leads to inflationary pressure. Minting large amounts of tokens, without there beying demand for it, would lead to each token losing value. Therefore having a large maximum token supply can be seen as an indication that the token's value will decay over time.

But how can we quantify the effect of future token supply on token value and how this would affect an investor?

Let us first define some important quantities. We define $S_t$ to be the **circulating supply** at time $t$, or the number of tokens that are available at a given time. We define $P_t$ to be the **token price**, at a given time $t$, in terms of USD, such that $1{\rm TOKEN}=P_t \,{\rm USD}$. We then define the $C_t$ to be the **market cap**, defined as,
$$ C_t=P_t*S_t,$$
which provides some quantification of the total value of the currency as a whole.

Suppose the currency has a defined maximum supply of tokens, $S_{\rm max}$. An quantity that is sometimes evaluated by investors is the **fully diluted value**, or $FDV_t$, as a hypothetical future market cap the project will have *if token price remains the same*. This is calculated as,
$$FDV_t=P_t*S_{\rm max}.$$
This quantity provides investors with some idea of what the future valuation for a project may look like, but it relies on the **strict assumption that token price would not be affected by increasing the supply**.


In this analysis, we are more interested in isolating what would be the inflationary effects of the maximum token supply. Instead of holding token price as a constant as is done when calculating $FDV$, we consider the alternative that *Market cap is not affected by increasing circulating supply*, and therefore explore, what happens to token price, if market cap remains constant.

As a simple analogy suppose token holders are dividing a slicing a pie and dividing amongst themselves. If in the future the pice will be cut into more slices, without it becoming a larger pie overall, then every holder will end up with a smaller slice of pie.

We define the *Asymptotic diluted price*, $P^A_t$ as the expected token price under the assumptions that 1) All the maximum circulating supply has been minted and 2) Market cap has not changed. At time $t$ this can be computed as,
$$ P^A_t=\frac{C_t}{S_{\rm max}}$$

This Could give some idea to an investor of what would happen to their token investment eventually in the far future, if the project's market cap doesn't grow.


## When thinking about the asymptotic future doesn't make much sense

An interesting counterexample that points to $P^A_t$ not being a good indicator to investors, is Ethereum, a currency that doesn't have a capped maximum supply. 

Ethereum's minting model is inflationary by design, where a fixed percentage of the circulating supply will be minted yearly. The maximum circulating supply in the infinitely far future, tends to infinity. This means that $P^A_t=0$. Yet investors keep holding ETH. Can we design a better metric to explain this?

## Expected Token lifetime dilution


What will happen to token price infinitely far in the future, should not be the main concern of investors. 
A much more important question is what will hapen to token price throughout the entire time that they will hold the token.

Suppose the investor plans on holding the token for $T$ years. We define the *Lifetime Diluted price*, $P^L_t$, as the Average token price throughout the $T$ years, under the assumptions that 1) There is a known schedule $S_t$ for how the circulating supply will increase, and 2) the market cap will remain constant. This is computed as
$$ P^L_t=\frac{1}{T}\int_0^T\frac{C_t}{S_{t+t^\prime}}dt^\prime$$

Note that we are defining this quantity with a Constant market cap, but we could easily modify it to inclute any other prediction we have for market cap.


Also note that if the circulating supply reaches an asymptotic value, this quantity will approach the asymptotic diluted price as we consider larger liftimes, that is,
$$\lim_{T\to \infty} P^L_t=P^A_t.$$


## Time weighting: the next 10 years are more important than the next 20 years

The lifetime diluted price, still does not account for the fact whappens to token price in the far future is less important to an investor than what happens to token price in the near future.

The fact that money is less valuable the further in the future than one can obtain it, is usually modelled with a *discount factor*, $\mu$, where $0<\mu<1$. Compared to an amount of money worth $V_0$ at present, The value of obtaining that same amount $T$ years later is given by 
$$V_T=(1-\mu)^T V_0$$


With this we are ready to present the metric we believe should be most informative to a potential investor, which accounts for the higher importance of the near future. 

We define the **time-weighted diluted price**, $P^W_t$, as the average lifetime token price under the assumptions that 1) There is a known schedule $S_t$ for how the circulating supply will increase,  2) the market cap will remain constant, and 3) Future events are weighted down with a discount factor. This can be computed as
$$P^W_t=\frac{1}{\tau}\int_0^T \frac{C_t(1-\mu)^{t^\prime}}{S_{t+t^\prime}}dt^\prime,$$
with,
$$\tau=\int_0^T(1-\mu)^{t^\prime}dt^\prime$$

We present a simple example of an exponentially increasing circulating supply 


### Example: Exponentially increasing supply

Let's consider a currency whose total circulating supply increases exponentially, such that $S_t=S_0e^{rt}$. **We choose this rate simply to illustrate the concept, because it is easy to compute the necessary integrals.** Nevertheless, note that this is would be applicable to Ethereum's minting model, at least in the absense of burning to reduce the supply. 

We can fix this exponential rate, say by demanding that the supply increases by X% each year, which means,
$$S_{1yr}=S_0(1+X/100)=S_0e^{r*1yr},$$
or,
$$r=\frac{1}{1yr}\log(1+X/100)$$

This currency has an uncapped circulating supply, as there is no finite maximum amount that will ever be minted. For this reason the traditional idea of Fully diluted value, $FDV_t$ is not applicable, since it would be infinite.

We can compute the expected token lifetime dilution, $P_t^L$, defined above, for a period of time $T$, assuming constant market cap:
$$P_t^L=\frac{C_t}{TS_0}\int_0^Te^{-rt^\prime}dt^\prime$$
$$=\frac{C_t}{TS_0r}(1-e^{-rT})$$
Notice that this quantity still goes to zero if we consider very long holding times, $T\to\infty$.

We can now evaluate the proposed time-weighted diluted price, $P_t^W$, as
$$ P_t^W=\frac{C_t}{\tau}\int_0^T\left(\frac{1-\mu}{e^r}\right)^{t^\prime} dt\prime=\frac{C_t}{\mu}\frac{\left(\frac{1-\mu}{e^r}\right)^T-1}{\log\left(\frac{1-\mu}{e^r}\right)},$$
and 
$$\tau=\int_0^T(1-\mu)^{t^\prime}dt^\prime=\frac{(1-\mu)^T-1}{\log(1-\mu)}$$


Now we can take the $T\to\infty$ limit,
$$\lim_{T\to\infty}P_t^W=\frac{C_t}{\mu}\frac{\log(1-\mu)}{\log\left(\frac{1-\mu}{e^r}\right)}$$

**Notice that unlike the fully diluted value or lifetime expected price, this gives a finite amount!**




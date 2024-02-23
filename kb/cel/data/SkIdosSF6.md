# How to define "use it or lose it" baseline minting?

## Summary

* It has been proposed (https://github.com/filecoin-project/FIPs/discussions/887) to burn the amount of baseline minting rewards that were not minted since RBP remained below baseline.
* Here we provide two general definitions for how this could be implemented: 1)Reducing the minting rate, so that the asymptotic total minted value is reduced, or 2) abrubtly stopping baseline minting at some finite time.
* We examine possible unintended negative consequences for both approaches. 
* In case 1) the baseline minting rate is reduced immediately, and there would be immediate economic consequences, particularly we discuss a risk of a downward spiral, where baseline minting rate can quickly diminish.
* In case 2) there is a risk of a large economic shock at the time when baseline minting suddenly stops.

## Baseline minting primer

Filecoin block rewards are given through a combination of simple minting and baseline minting 

Rewards from **Simple minting** decay exponentially, with a maximum of $M_{\infty,S}$ tokens to be minted over time. The amount of tokens that have been minted at a time $t$, via simple minting, is given by,
$$ M_S(t)=M_{\infty,S}(1-e^{-\lambda t}),$$
with the parameter $\lambda=3.663258818×10^{−9}
 Hz$, implying a 6-year half life
 
 
Rewards from **baseline minting** follow a similar formula at first glance, where a maximum of $M_{\infty, B}$ tokens to be minted over time, following an exponential decay law:
$$ M_B(t)=M_{\infty, B}(1-e^{-\lambda \theta(t)}),$$
with the only difference being that an **effective time** $\theta(t)$ is used in place of the real time, $t$.

The effective time is defined such that it passes more slowly than real time, when the network raw byte power is under the baseline power. That is, the more time is spent below baseline power, the more the rewards are postponed towards the future. Baseline power is a pre-defined exponential function,
$$b(t)=b_0e^{gt}.$$
The precise formulation of the effective time can be found in the [spec](https://spec.filecoin.io/systems/filecoin_token/block_reward_minting/), but we omit it here for simplicity. 

Let's consider a particular *pessimistic* example, that the network raw byte power grows linearly, as $R_{\rm linear}(t)=rt$, such that it is lower that the exponential baseline function, $R_{\rm linear}(t)<b(t)$. In this case the the total amount of baseline minting is
$$ M_B^{\rm linear}(t)=M_{\infty,B}\left(1+\frac{1}{(\frac{grt^2}{b_0}+1)^\lambda}\right)$$
That is, in this pessimistic scenario, baseline minting goes from exponential decay, to much softer polynomial decay. This is interpreted as *saving these tokens to use in the future*

![Screenshot 2024-01-12 at 3.25.18 PM](https://hackmd.io/_uploads/HyUBfG1Ya.png)
*Figure 1. Exponentially decaying Maximum baseline minting (red) vs. polynomially decaying pessimistic baseline minting*, against time in the $X$-axis. (Parameters were chosen for qualitative illustration purposes, this is not meant to be a quantitatively accurate plot)


Now we can understand the premise of the FIP discussion: Suppose we find ourselves in the *blue line* of Fig.1, where network power stays below baseline, and we have minted less than the maximum possible amount so far. **FIP discussion 887 proposes, "what if we burn this difference between the blue and the red line, instead of saving it for the future"?**

## Two ways of "using it or losing it"

Even though the blue line (baseline minting) in Fig. 1 is lower than the red line, (maximum baseline minting), by design the blue line will eventually catch up in the far future (the unminted rewards are saved to give more rewards later in time).

We present here to alternatives mechanisms to prevent the blue line from eventually catching up to the red line (burning the unused rewards instead). 

The first approach is to lower the minting rate, such that the blue line approaches a smaller asymptotic value. The second approach is to simply stop baseline minting entirely when we've minted enough.


### Proposal 1: Reduce the minting rate

By design, baseline minting will always reach an asymptotic value, $M_{B,\infty}$ in the very far future, even if in the pessimistic scenario, it does so very slowly.
We see this from the formulation,
$$ M_B(t)=M_{\infty, B}(1-e^{-\lambda \theta(t)}),$$
that as the effective time becomes larger, the exponential term becomes smaller, and eventually we reach the asymptotic value.

We can also think about the **minting rate**, that is, how much baseline minting reward is given at each block, which we can find this by taking the derivative of these cummulative minting rewards,
$$R_{B}(t)\equiv \frac{dM_B}{dt}=M_{\infty,B}\lambda e^{-\lambda\theta(t)}\frac{d\theta(t)}{dt}$$

**The minting rate dictates the eventual asymptotic value, $M_{\infty,B}$. So if we wanted to change this asymptotic value, we can propose to change the value as it appears on the minting rate.** The proposal would then be to have a minting rate:

$$R_B^{\rm proposed}(t)=M_{B,\infty}^{\rm proposed}(t)\lambda e^{-\lambda\theta(t)}\frac{d\theta}{dt}$$
Where the factor $M_{B,\infty}^{\rm proposed}(t)$ is modified such that the asymptotic value is reduced, according to the difference between the blue line and red line.

This new factor could be roughly defined as,
$$ M_{B,\infty}^{\rm proposed}(t)=M_{B,\infty}-{\rm Maximum\,\,recorded\,\,difference\,\,between\,\,red\,\,line\,\,and\,\,blue\,\,line}$$


This version of the proposal contradicts the wording of FIP proposal 887, which states that there would be no immediately measurable change. **The downside of this version of the proposal is that reductions in Minting rate are felt immediately.**

This version of the proposal doesn't affect only the eventual outcomes in the far future, but any loss in baseline minting is felt immediately in a reduction of minting rate.

#### Potential concern: Minting downward spirals

Under this version of the proposal, the minting rate is reduced poportionately depending on the maximum difference between the red and blue line. The subsequent lower minting rate, makes it more likely for this difference between the two lines to increase even more.

This mechanism leads to a worrying negative feedback loop:low baseline minting will lead to a lower minting rate, which again will lead to an even wider gap between the maximum possible baseline minting, and the realized baseline minting. 

There is a risk that this dynamic would lead to a rapidly decreasing minting rate.

### Proposal 2: Abruptly stopping baseline minting when we've had enough


If we do not want to alter the rate at which we mint tokens, the other alternative is to keep minting tokens at the same rate, but stopping the minting at some finite time. 

This would mean modifying the baseline minting function as,
$$ M_B(t)=\rm MAX \,\{M_{\infty, B}(1-e^{-\lambda \theta(t)}),M_{B,\infty}^{\rm proposed}\}.$$
That is, we continue minting at the usual rate, until we mint a decided maximum amount. The maximum $M_{B,\rm max}^{\rm proposed}$ can have the same definition as above, based on the maximum recorded difference between the red and blue lines.

**The main downside of this proposal is that it will cause a large economic shock at the time when all baseline minting abruptly stops, instead of the current smooth decay of baseline minting**







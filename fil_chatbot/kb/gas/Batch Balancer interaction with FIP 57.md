# Batch Balancer interaction with FIP 57

## Summary
FIP 57 was recently accepted, including a recalibration of the gas usage of a number of common messages. Of particular interest to us are **PreCommit, ProveCommit, PreCommitAggregate and ProveCommitAggregate** which all will consume more gas, post FIP 57.

The gas usage of PreCommit and ProveCommit messages appears as a parameter in the Batch Balancer mechanism. In principle **These parameters need to be updated in the Batch Balancer mechanism, following FIP 57 gas usage change**. 

If we do not update the batch balancer parameters, there are two main consequences:
* Batching becomes encouraged at a lower threshold (lower base fee, and/or lower number of proofs in the batch).
* Once the SP has chosen to batch, the **BatchGasCharge** is lower than it should be.

## What is the Batch Balancer supposed to be doing?

The ability to submit sector proofs as a more efficient batch was introduced in [FIP 13](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0013.md). If all else stayed equal, such an improvement would reduce the demand for gas and base fee.

The batch balancer mechanism imposes an additional **BatchGasCharge** to be paid whenever a set of proofs is batched. The consequence of this additional charge is that **when the base fee is low, it becomes irrational to batch proofs, as it would be cheaper to send the proofs individually**. This is a measure that protects against demand for gas lowing to very low levels.

When the conditions are met such that it is rational to batch, the BatchGasCharge serves as a fee to compensate the network, for allowing SP's to use the batching capabilities.

Batching can be done either for PreCommit or ProveCommit messages, both having their own batch balancer mechanisms. For simplicity of presentation for now, we will not distinguish between these two messages in the mathematical notation, since the mechanism works the same way for either message.

Suppose sending a single message, without batching, consumes an amount of gas $g_s$. We denote the base fee as $r$, then if one submits $n$ such messages without batching, the cost of submitting those single messages is given by,
$$C_s^n=g_s\cdot n\cdot r.$$

Suppose now those $n$ proofs are sent as a batch, which consumes an amount of gas, $g_b^n$, the cost of submitting the proofs as a batch is then,
$$C_b^n=g_b^n\cdot r+{\rm BatchGasCharge}.$$
The BatchGasCharge includes three parameters, the Batch balancer, $\gamma=5\,{\rm nanoFIL}$, the batch discount, $\frac{1}{d}=\frac{1}{20}$ , and the single message gas usage, $\bar{g}_s$. We are denoting the *parameter*, single message gas usage as $\bar{g}_s$, to distinguish it from the *actual* single message gas usage, $g_s$, since that will be the central issue we are exploring, a case where the parameter and the actual gas usage may not match. The batch gas charge is then defined as
$${\rm BatchGasCharge}=\frac{{\rm Max}(\gamma,r)}{d}\bar{g}_s\cdot n.$$

Batching is then a rational decision when
$$C_b^n< C_s^n,$$
or,
$$g_b^n\cdot r+\frac{{\rm Max}(\gamma,r)}{d}\bar{g}_s\cdot n<g_s\cdot n\cdot r.$$


## When is batching rational? (Pre FIP 57)

Let us explore further the above inequality, which indicates when batching is rational. In this section we assume the gas charge parameter is properly calibrated so that $\bar{g}_s=g_s$.  It can be instructive to rearrange the inequality as,
$$\frac{g_b^n}{g_s\cdot n}<1-\frac{{\rm Max}(\gamma,r)}{d\cdot r}$$

The left-hand-side describes how efficient batching is relative to not batching. $g_b^n$ grows logarithmically with larger $n$, so this approaches zero as $n$ increases. 

**The left-hand-side will always be a positive number**, so for batching to have any chance at being rational, the righ-hand-side must be positive as well.

We can understand the rationality of batching by dividing the scenario into three different regimes.

#### Regime 1)  $r<\frac{\gamma}{d}$

In this regime, the right-hand side of the above inequality is negative. This means that **batching is always irrational in this regime**, regardless of batch size.

#### Regime 2) $\frac{\gamma}{d}<r<\gamma$

In this regime, the inequality becomes,
$$\frac{g_b^n}{g_s\cdot n}<1-\frac{\gamma}{d\cdot r},$$
which we can re-write in terms of the base fee as,
$$\frac{\gamma}{d\left(1-\frac{g_b^n}{g_s\cdot n}\right)}< r$$

**In this regime, batching can be rational, depending on the number of proofs that are being batched.** For a given number $n$, the above inequality dictates the base fee required to make baching rational

#### Regime 3) $\gamma< r$

In this regime the inequality becomes,
$$\frac{g_b^n}{g_s\cdot n}<1-\frac{1}{d}.$$

**note that the base fee no longer plays a role in the inequality, after crossing the threshold $r>\gamma$.**

In this regime **the rationality of batchign depends only on the number of proofs being submitted*, as long as a large enough $n$ is batched, it is always rational to batch for any base fee above this threshold. 





## When is batching rational? (Post FIP 57, without parameter update)

FIP 57 recalibrated the amount of gas that is consumed, both by the single messages, and the aggregated messages. 

We denote the change in gas usage, as the real gas usage shifting to,
$$g_b^n\rightarrow a\cdot g_b^n,\,\,\,\,\,\,\,g_s\to b\cdot g_s,$$
where $a$ and $b$ are different for pre and prove commit, but in all cases, $a>1$ and $b>1$ as specified in FIP 57.

**In this scenario we assume that the batch balancer mechanism is not updated, such that we keep the wrong parameter**, $\bar{g_s}=g_s$. 

The inequality for the rationality of batching then takes the form,
$$\frac{a\cdot g_b^n}{b\cdot g_s\cdot n}< 1-\frac{{\rm Max}(\gamma, r)}{b\cdot d\cdot r}.$$

Again we notice that there are three distinct regimes,

#### Regime 1) $r<\frac{\gamma}{d\cdot b}$

In this regime, the right-hand-side of the inequality is negative, so batching is always irrational.

**Note that this lower threshold is lower than in the Pre-FIP 57 case**, This means that if the batch balancer is not updated, SP's will be able to start batching at lower base fees than is currently possible.

#### Regime 2) $\frac{\gamma}{d\cdot b}<r<\gamma$

In this regime, again given a number of proofs $n$, batching can only be justified if the base fee is high enoug. The inequality is given by
$$\frac{\gamma}{d\cdot b\left(1-\frac{a\cdot g_b^n}{b\cdot g_s\cdot n}\right)}<r$$

Note here that also because $b>1$, the precense of $b$ in the denominator pushes the base fee required for batching lower than it currently is. The fraction $\frac{a}{b}$ also affects the critical base fee required, but this number is closer to 1, and its effect is smaller than the effect of the single $b$ outside of the parenthesis. 

Note that for PreCommit, $\frac{a}{b}>1$, while for ProveCommit $\frac{a}{b}<1$, according to FIP 57, so the re-calibration in gas usage, affects the two types of message differently.

#### Regime 3) $\gamma<r$

In this regime, again the base fee drops out of the inequality, after crossing this threshold, then batching is justified for large enough, $n$, satisfying,
$$\frac{a\cdot g_b^n}{b\cdot g_s\cdot n}<1-\frac{1}{d\cdot b}.$$
Note again that **the presence of $b$ in the right-hand-side means that a lower $n$ will be necessary to justify batching, as it makes the right-hand-side larger.**

## When is batching rational? (Post FIP 57, with parameter update)

Suppose now, as in the previous case, FIP 57 has recalibrated the gas usages,
$$g_b^n\to a\cdot g_b^n,\,\,\,\,\,\,g_s\to b\cdot g_s,$$

but **now we have also re-calibrated the batch balancer parameter accordingly**, such that,
$$\bar{g}_s\to b\cdot g_s.$$

The inequality governing the rationality of batching is then,

$$\frac{a\cdot g_b^n}{b\cdot g_s\cdot n}< 1-\frac{{\rm Max}(\gamma, r)}{ d\cdot r}.$$

Note the difference here, compared to the previou scenario is that now $b$ does not appear on the right-hand-side, we only have the ratio $\frac{a}{b}$, which is close to 1, and slightly above 1 for PreCommit, and slightly below 1 for ProveCommit.

We again examine the three regimes,

#### Regime 1) $r<\frac{\gamma}{d}$

In this case, the right-hand-side of the inequality is negative, so it is never rational to batch. 

Note that **this lower threshold is now restored to its pre-FIP 57 value, because of the parameter update.**

#### Regime 2) $\frac{\gamma}{d}<r<\gamma$

In this regime, it is only rational to batch if the base fee is high enough, given $n$, as
$$\frac{\gamma}{d\left(1-\frac{a\cdot g_b^n}{b\cdot g_s\cdot n}\right)}<r.$$

Note that the factor of $b$ outside the parenthesis is now absent, compared to the previous scenario. This means that the threshold base fee required to batch is higher, compared to when the parameter is not updated, and closer to the pre-FIP 57 case.

#### Regime 3) $\gamma<r$

In this regime again the base fee disappears from the inequality, so the rationality of batching depends only on $n$,
$$\frac{a\cdot g_b^n}{b\cdot g_s\cdot n}<1-\frac{1}{d}.$$

Note the disappearance of $b$ from the right-hand-side of the inequality, compared to the previous scenario. This means that the righ-hand-side is now larger, and equal to the pre-FIP 57 case, and means that a larger $n$ will be needed to justify batching, than if the gas usage parameter was not updated.


## What are the risks of not updating parameters?

Here we summarize what are the risks of not updating the parameter $\bar{g_s}$ to $bg_s$ after FIP 57.

* For **Regime 1**, the lowest base fee required to make any batching rational is lowered, if batch balancer parameters are not updated after FIP 57.

* For **Regime 2**, Batching will be justified for lower base fees and/or lower number of proofs, if batch balancer parameters are not updated after FIP 57.

* For **Regime 3**, Batching will be justified for lower number of proofs, if batch balancer parameters are not updated after FIP 57.

* Whenever the SP has already decided to batch, the BatchGasCharge will be lowered, so less gas will be burnt, if batch balancer parameters are not updated after FIP 57.

In general **not updating the parameters of the batch balancer after FIP 57, will lead to less gas fee burnt in all regimes**.

All the above problems can be fixed (or alleviated) by simply updating the new single message gas usage in the batch balancer mechanism.
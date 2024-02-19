# Generalized batch balancer

Suppose the cost for a non-batched message which consumes gas $\gamma^p$, and there is a base fee $\phi$, is given by
$$C^p_n(\phi,\gamma)$$

When the same message is part of a batch, the non-batched set of messages will consume an amount of gas $\Gamma=\sum_p \gamma^p$. By batching, the total amount of gas actually used is reduced to $M=\Gamma d$, where we can assume $d(\Gamma)$ is a non-increasing function of $\Gamma$. The individual message gas can take the range $\gamma^p\in(0,\Gamma)$.

The cost for submitting the same message, but as part of a batch, is then
$$C^p_b(\phi,\Gamma,d,\gamma^p).$$
This can be simplified by assuming $d$ is only a function of $\Gamma$, so
$$\tilde{C}^p_b(\phi,\Gamma,\gamma^p)\equiv C^p_b(\phi,\Gamma,d(\Gamma),\gamma^p)$$

We define the discount factor provided by batching as
$$D^p(\phi,\Gamma,\gamma^p)\equiv\frac{\tilde{C}^p_b(\phi,\Gamma,\gamma^p)}{C^p_n(\phi,\gamma)}.$$

With these definitions we can now place our set of constraints on the discount factor.

### Constraints:

1) Batching becomes better with larger batches:
$$\frac{\partial D^p(\phi,\Gamma,\gamma^p)}{\partial \Gamma}\le 0.$$

4) Increase in base fee incentivizes batching (or alternative the U-shape proposed by Jamsheed):
$$\frac{\partial D^p(\phi,\Gamma,\gamma^p)}{\partial \phi}\le 0.$$

2) There is a *unique* crossover base fee $\phi^*$, above which batching becomes profitable,
$$D^p(\phi^*,\Gamma,\gamma^p)=1.$$
We may want to set $\phi^*(\eta)$ as a function of the network growth rate, $\eta.$

3) OPTIONAL. We may want to incentivize smaller messages to join the batch as is done in the split between pre- and prove-commit, where the savings for the smaller pre-commit messages are greater:
$$\frac{\partial D^p(\phi,\Gamma,\gamma^p)}{\partial \gamma^p}\ge 0.$$
This generalizes the idea presented in [fip-0024](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0024.md) to the case where there could be many possible types of messages. Furthermore we could think of sub-batches of messages within a batch, which could have varyng sizes.
Notice that different goals are being acheived, regarding this subject, between [fip-0013](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0013.md#batch-gas-charge) and fip-0024. Batch balancer not being applied to the smaller pre-commit messages, means that these smaller messages had a greater discount, as we have proposed. The adjustment from fip-0024 undoes this property, so it would be good to decide what we actually want.
This specifications do not matter as long as the messages in a batch arise from the same miner, so it doesn't matter how the discount is distributed amongst individual messges. We could however imagine a possible future where miners pool together to make joint batches, then discount attribution to each individual message would be important.

3) Ensure it is still good to batch for the largest messages:
$$\lim_{\gamma^p\to\Gamma}D^p(\phi,\Gamma,\gamma^p)\le 1.$$



## Testing the current formulation.    DON'T READ THIS SECTION YET, WORK IN PROGRESS

We now test under which conditions (if any) the current formulation for the batch balancer satisfies our constraints. The current implementation takes the form
$$C^p_n(\phi,\gamma^p)=\phi\gamma^p,$$
$$C_b^p(\phi,\Gamma,\phi^p,N)={\rm max}(\phi_{\rm bal},\phi)r^b\gamma^p+\frac{\phi\Gamma d(\Gamma)}{N},$$
notice how this depends on the additional variable $N$, which is the number of messages in the batch, which we didn't consider relevant previously. This variable can be rephrased as $N=\Gamma/\bar{\gamma}$, where $\bar\gamma$ is the average un-batched gas consumption for each message in the batch.

We then have the discount factor
$$D_b^p(\phi,\Gamma,\phi^p,\bar\gamma)=\frac{{\rm max}(\phi_{\rm bal},\phi)r^b\gamma^p+\phi\bar\gamma d(\Gamma)}{\phi\gamma^p}.$$

We now test whether our constraints are satisfied,

1) Discount factor decreases with batch size,
$$\frac{\partial D_b^p}{\partial \Gamma}=\frac{\bar\gamma}{\gamma^p}\frac{\partial d(\Gamma)}{d\Gamma}\le 0,$$
where the last inequality is true becasue we assumed $d(\Gamma)$ is a non-increasing function, and $\bar\gamma/\gamma^p$ is a positive number.

Note that increasing the total batch size $\Gamma$ will bring a larger benefit to smaller-than-average messages, where $\bar\gamma/\gamma^p>1$.

2) Incentivize smaller messages to join batch,
$$\frac{\partial D_b^p}{\partial \gamma^p}=-\frac{\bar\gamma d(\Gamma)}{(\gamma^p)^2}\le 0,$$
where all the quantities involved are positive numbers, so the negative sign makes the inequality true.

3) Ensure batching is good for large messages,
$$\lim_{\gamma^p\to\Gamma}D_b^p=\frac{{\rm max}(\phi_{\rm bal},\phi)r^b\Gamma+\phi\bar\gamma d(\Gamma)}{\phi\Gamma},$$
which we require to be smaller or equal to 1. This requires implementing constraints on the batch discount, $r^b$, as follows:

First consider the case $\phi>\phi_{\rm bal}$, then the condition is satisfied if,
$$r^b\le \frac{\Gamma-\bar\gamma d(\Gamma)}{\Gamma}.\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,(*)$$

If $\phi<\phi_{\rm bal}$, then the condition is satisfied if,
$$r^b\le \frac{\phi}{\phi_{\rm bal}}\frac{\Gamma-\bar\gamma d(\Gamma)}{\Gamma}.$$
Since in this case, by assumption already $\frac{\phi}{\phi_{\rm bal}}<1$, then the condition is automatically satisfied if (*) is satisfied.

Therefore in all cases condition 3 is satisfied if the batch discount satisfies (*).

It is convenient here again to re-express (*) in terms of the number of messages in the batch,
$$r^b\le 1-\frac{d(\Gamma)}{N}.\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,(*)$$

4) Increasing base fee incentivizes batching.
$$\frac{\partial D_b^p}{\partial \phi}=\left\{\begin{array}{cc} 0,&{\rm for} \,\,\,\,\,\phi\ge\phi_{\rm bal},\\
-\frac{\phi_{\rm bal}}{\phi^2}r^b,&{\rm for}\,\,\,\,\,\phi<\phi_{\rm bal}\end{array}.\right.$$
The constraint is automatically marginally satisfied for $\phi\ge\phi_{\rm bal}$, and for $\phi<\phi_{\rm bal}$ it is satisfied as all the quantities involved are positive, and the negative sign means the constraint is satisfied.

The case $\phi<\phi_{\rm bal}$ can become more complicated if we introduce a  **dynamic batch balancer**, which we interpret as $\phi_{\rm bal}$ actually being a function $\phi_{\rm bal}(\phi)$.

We then have,
$$\frac{\partial D_b^p}{\partial \phi}=\left\{\begin{array}{cc} 0,&{\rm for} \,\,\,\,\,\phi\ge\phi_{\rm bal},\\
\left(-\frac{\phi_{\rm bal}}{\phi^2}+\frac{\phi_{\rm bal}^\prime}{\phi}\right)r^b,&{\rm for}\,\,\,\,\,\phi<\phi_{\rm bal}\end{array}.\right.$$

Now the constraint is satisfied for $\phi_{\rm bal}>\phi$ only if,
$$\phi_{\rm bal}^\prime-\frac{\phi_{\rm bal}}{\phi}\le 0$$
We can turn this inequality into a differential equation, as the constraint,
$$\phi_{\rm bal}^\prime-\frac{\phi_{\rm bal}}{\phi}+g(\phi)=0,$$
where $g(\phi)$ is some surplus function such that $g(\phi)\ge 0$. The differential equation is linear and first order, and can be easily solved as
$$\phi_{\rm bal}=\frac{C+\int g(\phi)\phi d\phi}{\phi},$$
which gives us the generic form of batch balancer function we are free to choose, while ensuring constraint 4 is satisfied, where $C$ is some constant and $g(\phi)$ is a positive function. 

With this form, constraint 4 becomes,
$$\frac{\partial D_b^p}{\partial \phi}=\left\{\begin{array}{cc} 0,&{\rm for} \,\,\,\,\,\phi\ge\phi_{\rm bal},\\
-g(\phi)r^b,&{\rm for}\,\,\,\,\,\phi<\phi_{\rm bal}\end{array}.\right.$$
which satisfies the constraint.


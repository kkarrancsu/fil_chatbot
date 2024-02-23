# Collateral for HC (No longer applicable to IPC as an L2)

Here we briefly propose a mechanism for pricing collateral in the Hierarchical consensus context.

We will focus on fixing the collateral mechanism only for the rootnet, and allowing freedom or the subnets to set up their own structure.

At a given point in time, $t$, the rootnet has $N_t$ subnets directly under it in the hierarchy. For a subnet to join as a direct child of the rootnet, it needs to pay a certain amount of collateral. This collateral is slashable (or a fraction of the collateral) if subnet commits any defined slashable offense.

Here we propose a possible approach to pricing collateral.



## Key elements of rootnet collateral

1) At any point in time, $t$, the rootnet publishes its current *collateral coefficient*, $C_t$. This coefficient has units of [Token units*/gas units].
2) A given subnet operating under the rootnet, which we label as the $i$-th subnet, checkpoints to the subnet at a rate $B^i$ (in units of gas), which is defined as the amount of gas the $i$-th subnet will consume in the average rootnet block.
3) The *minimum* amount of collateral a subnet needs to commit to remain active is given by 
$$ {\rm minimum\,collateral}=C_t*B^i$$
The subnet is also free to place a higher collateral to express confidence in the subnet.
5) There exist a set of violations a subnet can commit, $V_k$, where $k$ enumerates the set of violations. Each of these has a given weight, $w_k$, porportional to how grave this violation is.
6) At any moment in time, the rootnet can compute a *violation index* measuring violations committed by its subnets within the previous time period $T$. The violation index at time $t$ is defined as
$$\mathcal{V}_t=\int_{t-T}^t\sum_{i\in {\rm subnets}}\sum_{k\in {\rm violations}}w_{k}\delta(t^\prime-t_{V_{k}^i})dt^\prime$$
where $\delta(t^\prime-t_{V_{k}^i})$ is a Dirac delta function (can be replaced with a Kronecker dealta when dealing with Discrete time), which has a peak at time $t_{V_{k}^i}$, which is the time when the $k$th violation was commited by the $i$th subnet.
5) The collateral coefficient may be adjusted every time period $T$, depending on a function of the violation index, and some acceptable *violation threshold* $\mathcal{V}^*$,
$$C_t=f(\mathcal{V}_t,\mathcal{V}^*)*C_{t-T}.$$
6) The function $f(\mathcal{V}_t,\mathcal{V}^*) $targets the threshold $\mathcal{V}^*$, such that
$$f(\mathcal{V}_t,\mathcal{V}^*)>1,\,\,\,\,\,\,{\rm if}\,\,\,\,\,\mathcal{V}_t>\mathcal{V}^*$$
and
$$0<f(\mathcal{V}_t,\mathcal{V}^*)<1,\,\,\,\,\,\,{\rm if}\,\,\,\,\,\mathcal{V}_t<\mathcal{V}^*$$


## Open questions

1) This works on the assumption that the higher we make the penalty, the less likely users are to commit violations. There are obvious limitations to this assumption (unavoidable accidents for instance). So perhaps much higher weight, $w_k$ must be given to violations that are not accidental, but malicious. 
1) Slashing policy: How much of the collateral should be slashed when a violation occurs? (should in principle depend on the violation weight $w_k$).
2) In principle all the collateral can be slashed, doesn't have to be a fraction of it, because the total collateral adjusts to market dynamics. If this is too high an amount to be slashed then people will commit fewer violations, which will bring the slashing amount to a more reasonabe price.
3) Collateral updating: What if a subnet is active and then $C_t$ increases? Do they become inactive until they pay up?
4) Do we need individual miner collateral, separate from Subnet collateral, for all the miners in the subnet? I think this is not necessary as this information is not relevant to the parent, the parent should not mind the inner workings of the subnet, but should only care about its performance as a whole.
5) How often do we update the collateral? Basically setting the period $T$. This doesn't have to be very fast (epoch level). Week by week ? month by month?
6) Interaction with regulation of hierarchy growth: Higher collateral means it can become less likely to spawn new subnets, which may be an undesired consequence. Updating formula could also include information about desired network growth. In other words, could includde information on the value of the updating function for the block-space [allcoation parameter](https://github.com/AxCortesCubero/HC-gas-simulation/blob/4bcfe359aed86288ef1669dbece0dfc15f9f84ed/HC%20gas%20simulation.ipynb) $a_t$. 
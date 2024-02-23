---
title: Crossover Base Fee Unit Economics
tags: FIPs
---

# Crossover Base Fee Unit Economics

Here we derive the unit economics difference in the *SingleProofProveCommit* and *BatchProveCommit* methods. 

## Definitions
1. $g_{s}$ -> SingleProofProveCommit Gas Usage (Gas Unit)
2. $g_{b}$ -> BatchProveCommit Gas Usage (Gas Unit)
3. $B$ -> Network base fee (Fil/Gas Unit)
4. $M$ -> Number of proofs batched (Unitless)
6. $\beta$ -> Batch Balancer (Fil/Gas Unit)
7. $d$ -> Batch Discount (Unitless)

## Unit Economic Analysis

The below equation describes $N_{S}$, the Network Fee for a Unit Sector *SingleProofProveCommit*

$$  N_S = g_sB $$

We now define $N_B$, the Network Fee for a Unit Sector *BatchProveCommit*:
$$ N_B = \frac{max\{B,\beta\} * g_s * M * d}{M} + \frac{g_bB}{M}$$

Which reduces to: 
$$ N_B = g_smax\{B,\beta\} * d  + \frac{g_bB}{M} $$

We analyze economic preferences in various *BaseFee*, *BatchBalancer*, and *BatchDiscount* Regimes. 

### Case 1: $B \le \beta * d$
Here, the network *BaseFee*, $B$ is less than the *BatchBalancer* * *BatchDiscount*. If we refer to Unit Ecnonomics above, under this regime $N_B > N_S$. The per unit cost for batching is strictly greater than the per unit cost for single proofs. 

Under this condition, the *SingleProofProveCommit* method is preferred. 

### Case 2: $B > \beta$

Here, the network *BaseFee*, $B$ is strictly greater than the *BatchBalancer*, $\beta$. We are interested in describing the conditions under which miners would prefer to batch rather than submit single proofs for their sectors:  

$$ N_S - N_B > 0 $$

Substituting the unit economics definitions above, this is when: 

$$ g_sB  - (max\{B,\beta\} * d * g_s + \frac{g_bB}{M}) > 0 $$

Since $B > \beta$:

$$ g_sB  - (g_sB*d + \frac{g_bB}{M}) > 0 $$

which reduces simply to $N_S > N_B$ when:

$$ g_s(1 - d) - \frac{g_b}{M} > 0 $$

The intuition here is under this regime in which $B > \beta$, **miners will generally prefer to batch** since *BatchProveCommit* **reduces the unit sector GasUsage**, and, as more proofs are aggregated $\frac{g_b}{M}$ becomes smaller pushing the above inequality to be positive. In other words, since it is always true by construction that $g_s(1 - d) > 0$, and $\lim_{M\to\infty} \frac{g_B}{M} = 0$, miners should increase batching such that $N_B < N_S$ (per unit cost of batching is less than the per unit cost of submitting single proofs) 


### Case 3: $\beta*d < B < \beta$

Here, the network *BaseFee*, $B$ is less than the *BatchBalancer*, $\beta$ , but greater than the *BatchBalancer* * *BatchDiscount*. We are interested in the crossover event $N_S - N_B > 0$, in which the per unit cost of batching is lower than the per unit cost of single proving. 

We evaluate $N_S - N_B = 0$. Per the definitiosn above, this is when:

$$g_sB - g_smax\{B,\beta\} * d  + \frac{g_bB}{M} = 0$$

Since $B < \beta$, this reduces to: 

$$g_sB - (g_s\beta d  + \frac{g_bB}{M}) = 0$$

And so the crossover event in which miners are indifferent between single proving or batching is when:

$$ B = \frac{\beta dg_s}{g_s - \frac{g_b}{M}} $$

When $B > \frac{\beta dg_s}{g_s - \frac{g_b}{M}}$ miners should prefer to batch, and when  $B < \frac{\beta dg_s}{g_s - \frac{g_b}{M}}$ they should prefer utilizing *SingleProofProveCommit* 

Further, as the number of proofs batched increases: 

$$\lim_{M\to\infty} \frac{\beta dg_s}{g_s - \frac{g_b}{M}} = \beta d$$

so the above crossover event can be approximated to: 

$$ B = \beta d $$









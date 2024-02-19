# Gas lanes vs gas dicounts, equilibrium propoerties

## Summary
Exploring some details of the version of gas lanes where there is only one base fee for all lanes, but a special lane gets a discount factor. How does this relate to the approach where the two lanes have fixed widths and have separate base fees?

## Introduction

Let's assume there is only one base fee given EIP-1559 with a target block size $B^T$. 

Let's model user behavior with a value distribution function $F(v)$, which means that for a base fee $v$, only a fraction $1-F(v)$ of users would be willing to send their messages. 

If there is an external demand for gas usage, $D$, (this means all the amount of gas that would be included at that time if they didn't have to pay base fee), the base fee for that level of demand would be given by the relationship,
$$ \frac{B^T}{D}=1-F(v*)$$,
which can be solved by defining the inverse function, $F^{(-1)}$,
$$v^*=F^{(-1)}\left(1-\frac{B^T}{D}\right)$$

## Two kinds of gas with no gas lanes

Let us now assume there are two different kind of messages, which we will label here as "SP" and "FVM". Each has their own value distribution, $F^{\rm SP}(v),\,F^{\rm FVM}(v)$, and levels of demand $D^{\rm SP},\,D^{\rm FVM}$.

If both of these messages have to share the same blockspace, $B^T$, and there is no explicit gas lanes, organically they will divide the block according to who is able to pay more. The SP messages will occupy an amount of gas, $aB^T$, and the FVM messages occupy $(1-a)B^T$.  

The resulting base fee, $v^*$ and block distribution $a$ for a given level of demand, $D^{\rm SP},\,D^{\rm FVM}$, can be obtained by solving the system of two coupled equations:
$$v^* =F^{(-1 )\rm SP}\left(1-\frac{aB^T}{D^{\rm SP}}\right)$$
$$v^*=F^{(-1)\rm FVM}\left(1-\frac{(1-a)B^T}{D^{\rm FVM}}\right)$$

## Two kinds of gas with explicit gas lanes

Fixing gas lanes explicily amounts to fixing the quantity $a$ explicitly, controlling by hand the width of the gas lanes. Holding this quantity fixed will mean that there will now be two base fees that vary independently.

We denote a constand fixed lane width parameter as $a_c$.  For a given level of demand, and a given fixed lane width, the two resulting base fees can be obtained by solving the two **independent** equations,

$$v^{*\rm SP} =F^{(-1 )\rm SP}\left(1-\frac{a_cB^T}{D^{\rm SP}}\right)$$
$$v^{*\rm FVM}=F^{(-1)\rm FVM}\left(1-\frac{(1-a_c)B^T}{D^{\rm FVM}}\right)$$

## Two kinds of gas with gas discounts

In this case, suppose the lane width, $a$ again is let to freely vary, but a discount, $d$ is given to the SP lane, such that they have to pay only a fraction $d$ per unit of gas.

Intuitively, more of the SP gas will be able to get into the block as a result of the discount, resulting in a larger $a$, and a larger overall base fee. 

For a fixed discount $d$, at a given level of demand, we can obtain the resulting base fee and block distribution by solving the following set of equations:
$$dv_d^* =F^{(-1 )\rm SP}\left(1-\frac{a_dB^T}{D^{\rm SP}}\right)$$
$$v_d^*=F^{(-1)\rm FVM}\left(1-\frac{(1-a_d)B^T}{D^{\rm FVM}}\right)$$

where we denote explicitly $v_d^*$, $a_d^*$ to imply explicitly that these are the resulting quantities in the precense of a discount. 

Note in particular that
$$v_d^*>v^*,\,\,\,\,\,a_d^*>a^*$$
for any $0<d<1$

Question: What discount should we choose to reach a desired distribution $a_d$? (depends on the levels of demand and value distributions)


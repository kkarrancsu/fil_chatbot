# Linear multiplier, what slope?
### Relative risk perspective
--- 

Longer sector durations bring collective benefits to the network through stability and longevity, but from an individual SP's perspective, risk also increases with commitment to longer durations. 

One perspective is that power should scaled in porportion to the increase in risk accepted by commiting for longer. 

Given this, **what should the slope of the duration multiplier to scale the power be?**

### SP participation perspective
Let $p^\text{survive}(n)$ be the probability of surviving $n$ years. 

If the survival probability is independent from year-to-year then

\begin{align*}
p^\text{survive}(n)=p^\text{survive}(1)^n\,.
\end{align*}

The relative risk is the ratio of 1 year compared to $n$ years:

\begin{align*}
\frac{p^\text{survive}(1)}{p^\text{survive}(1)^{n}}=\frac{1}{p^\text{survive}(1)^{n-1}}\,.
\end{align*}

Given a principle to compensate rewards in proportion to relative risk using a multiplier that scales power with $n$ years (linear sector duration multiplier), then the slope should be the per year increase in relative risk:

\begin{align*}
\frac{1}{n\,p^\text{survive}(1)^{n-1}}
\end{align*}

For different survival probabilities and sector commitment durations this looks like:

![](https://hackmd.io/_uploads/rkN6U2rXo.png)

The lower the survival probability, the higher the linear multiplier slope should be to conserve relative risk.

A linear multiplier slope between 0.5-1x is probably reasonable to maintain relative risk. 

Given the value longer sectors bring to the network in terms of stability and locking, erring on the upper side of this range seems appropriate.

### Sector fault perspective

If we consider the increased risk of losing collateral through faults, this scales with duration as

\begin{align*}
\frac{1}{p^\text{fault}(1)^{n-1}}\,.
\end{align*}

The logic and form is the same as above, except scaled by $n$ to account for the increased collateral commitment with longer duration that can be lost upon faulting. 

![](https://hackmd.io/_uploads/rkIQb68Xj.png)

From the perspective of scaling power to compensate increased expected collateral loss through increase probability of incurring a fault, the linear multiplier slope is strictly greater than 1x.

---


#### Assumptions
* The principle of maintaining relative risk across an increase in duration commitment is only one way to anchor our beliefs about what changes in sector durations imply. It doesn't account for network level benefits at all. 
* The concept of the power multiplier being linear in duration. In reality risk the SP takes on is not linear in duration. Nor is the value of the commitment from the network's perspective. 
* That probability of exit or fault  occurance is constant and independent from one year to next. 
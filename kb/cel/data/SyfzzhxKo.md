# All sectors vs new sectors SDM question

### Scenario: 'new sectors' only SDM, CC suddenly terminates to gain SDM

Currently RBP is modeled as
\begin{align*}
P_{t}^{\text{RB}}=P_{t-1}^{\text{RB}}+\underset{\text{onboarded}}{\underbrace{O_{t}^{\text{RB}}}}+\underset{\text{renewals}}{\underbrace{R_{t}^{\text{RB}}}}-\underset{\text{scheduled expiration}}{\underbrace{E_{t}^{\text{RB}}}}
\end{align*}
We want to model 'new sectors'-only SDM where CC terminates in order
to gain an SDM.

Assume a single discrete termination event at $t=\tau$. Then power
should be

\begin{align*}
P_{t}^{\text{RB}}=\begin{cases}
P_{t-1}^{\text{RB}}+O_{t}^{\text{RB}}+R_{t}^{\text{RB}}-E_{t}^{\text{RB}} & 1:t<\tau\\
P_{t-1}^{\text{RB}}+O_{t}^{\text{RB}}+O_{t}^{\text{RB}}+R_{t}^{\text{RB}}-\underset{\text{terminations}}{\underbrace{T_{t}^{\text{RB}}}} & 2:t=\tau\\
P_{t-1}^{\text{RB}}+\underset{\text{terminations re-onboarded}}{\underbrace{O_{t}^{\text{RB}}+T_{t}^{\text{RB}}}}+\underset{\text{vectors adapated by terminations}}{\underbrace{R_{t}^{\text{RB}}-E_{t}^{\text{RB}}}} & 3:t=\tau+1\\
P_{t-1}^{\text{RB}}+O_{t}^{\text{RB}}+\underset{\text{vectors adapated by terminations}}{\underbrace{R_{t}^{\text{RB}}-E_{t}^{\text{RB}}}} & 4:t>\tau+1
\end{cases}
\end{align*}

Here each step is:

* Before the termination: no change (current model).
* Termination occurs. Causes a $T$ sized drop in RBP. Elsewhere this affects CS via burned penalties.
* Terminated RBP is re-onboarded. This one-off onboarding is separated from standard onboarding $O_{t}^{\text{RB}}$. Some notes: this requires paying any difference in pledge, and gaining a SDM in the QAP calculation (later). Practical note: in reality re-onboarding is machine-limited by resealing throughput. In addition to the terminations being re-onboarded, the scheduled expirations and renewals vectors have to change to account for dropped power (what's gone doesn't scheduled expire or renew --- and when reintroduced, these things get pushed to future). 
* Post termination event, onboarding continues as before, renewals and onboards continue with the updated vectors.

Now we can describe each term in the power.

Firstly, for onboarding $O_{t}^{\text{RB}}$, no change.

For the expirations vector, the SDM/termination event requires changing to
the following structure:

\begin{align*}
E_{t}^{\text{RB}}=\begin{cases}
E_{t}^{\text{RB,active}}+O_{t-d}^{\text{RB,onboard}}+R_{t-d}^{\text{RB,onboard}} & 1:t<\tau\\
\gamma\left(E_{t}^{\text{RB,active}}+O_{t-d}^{\text{RB,onboard}}+R_{t-d}^{\text{RB,onboard}}\right) & 2:\tau\le t\le\tau+d\\
E_{t}^{\text{RB,active}}+O_{t-d}^{\text{RB,onboard}}+R_{t-d}^{\text{RB,onboard}} & 3:\tau+d<t\le\tau+\tilde{d}\\
E_{t}^{\text{RB,active}}+O_{t-\tilde{d}}^{\text{RB,onboard}}+R_{t-\tilde{d}}^{\text{RB,onboard}} & 4:t>\tau+\tilde{d}
\end{cases}
\end{align*}

Here each step is:
* Pre termination/intro of SDM: as before.
* The effect of terminations on expirations is modeled as immediately scaling down scheduled contributions by a factor $\gamma$ in an interval of time between the termination event, to a current average sector duration $d$ forward in time. The factor is based on the proporation of power that terminates: $\gamma=1-\frac{T_{t}^{\text{RB}}}{P_{t}^{\text{RB}}}$.
* After some time (average duration $d$) the terminated sectors no longer contribute the downscaling of scheduled expirations. 
* After some further time, scheduled expirations shift to a lag of the new average duration $\tilde{d}$ instead of $d.$ 

For renewals, termination/SDM changes the future renewal vector to

\begin{align*}
R_{t}^{\text{RB}}=\begin{cases}
r_{t}E_{t}^{\text{RB,active}}+r_{t}O_{t-d}^{\text{RB,onboard}} & 1:t<\tau\\
\gamma r_{t}E_{t}^{\text{RB,active}}+\gamma r_{t}O_{t-d}^{\text{RB,onboard}} & 2:\tau\le t\le\tau+d\\
r_{t}E_{t}^{\text{RB,active}}+r_{t}O_{t-d}^{\text{RB,onboard}} & 3:\tau+d<t\le\tau+\tilde{d}\\
r_{t}E_{t}^{\text{RB,active}}+r_{t}O_{t-\tilde{d}}^{\text{RB,onboard}} & 4:t>\tau+\tilde{d}
\end{cases}
\end{align*}

The changes here follow the same logic as above.

QAP is given by 

\begin{align*}
P_{t}^{\text{QA}}=P_{t-1}^{\text{QA}}+\underset{\text{onboarded}}{\underbrace{O_{t}^{\text{QA}}}}+\underset{\text{renewals}}{\underbrace{R_{t}^{\text{QA}}}}-\underset{\text{scheduled expiration}}{\underbrace{E_{t}^{\text{QA}}}}
\end{align*}

The QAP onboarded before, during, after SDM/termination event is

\begin{align*}
O_{t}^{\text{QA}}=\begin{cases}
\left(1+9\cdot\text{fil_plus_rate}\right)O_{t}^{\text{RB}} & 1:t<\tau\\
\tilde{d}\cdot\left(1+9\cdot\text{fil_plus_rate}\right)O_{t}^{\text{RB}} & 2:t=\tau\\
\tilde{d}\cdot\left(1+9\cdot\text{fil_plus_rate}\right)O_{t}^{\text{RB}}+\tilde{d}T_{t}^{\text{RB}} & 3:t=\tau+1\\
\tilde{d}\cdot\left(1+9\cdot\text{fil_plus_rate}\right)O_{t}^{\text{RB}} & 4:t>\tau+1
\end{cases}
\end{align*}

The steps are:
* No change, as before.
* SDM happens. SDM is available to all new onboarded sectors and scales
them by the new duration.
* The terminated power is re-onboarded as new CC and gains a multiplier.
* Same as step 2.

Other QAP contributions are similarly scaled by $\tilde{d}$. 

### Scenario: 'all sectors', CC suddenly gains SDM through extension




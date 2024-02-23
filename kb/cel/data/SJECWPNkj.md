# PCD Analysis 
**Vik K and Maria S**
###### tags: `FIPs`

This is analysis supplemental to the FIP-0036 proposal - specifically analyzing the impact on PreCommitDeposit. 

Here we take a look at Expected Returns for a single sector given a failure rate for proveCommiting messages in time 

Given 
- $r$: FIL-on-FIL Return for a Sector
- $f$: ProveCommit failure Rate
- $PCD$: ProveCommit Deposit
- $g$: gas fees for ProveCommit messages (assuming they are negligble)
- $IP$ - InitialPledge required for a sector 
- $R$ - Total Minted Rewards for a Sector
- $n$ - Years for which the sector receives rewards

Then, the following Expected Return: 
$$ E[r] = f \cdot r_{fail} + (1-f) \cdot r_{success}$$

The annualized expected return can be written as:  
$$ E[r]_{annl} = f \cdot r_{fail_{annl}} + (1-f) \cdot r_{success_{annl}}$$

In the event of failed proveCommit: 

$$ r_{fail} = \frac{-PCD-g}{\max \{IP,PCD\}} $$

Assuming gas is negligible: 
$$ r_{fail} = \frac{-PCD}{\max \{IP,PCD\}} $$

In the case of successful proveCommit:
$$r_{success} = \frac{R}{\max\{IP,PCD\}}$$

Annualized, these are 

$$ 
r_{fail_{annl.}} = (1+r_{fail})^{1/n} - 1 \\
r_{success_{annl.}} = (1 + r_{success})^{1/n} - 1 
$$

Therefore, the annualized Expected Return: 

$$ E[r]_{annl} = f \cdot [(1 + \frac{-PCD}{\max \{IP,PCD\}})^{1/n} - 1] + (1-f) \cdot [(1+\frac{R}{\max\{IP,PCD\}})^{1/n} - 1] $$

### Case 1: $PCD >= IP$
$$ E[r]_{annl} = -f + (1-f) \cdot [(1 + \frac{R}{PCD})^{1/n} - 1] $$

### Case 2: $PCD < IP$

$$ E[r]_{annl} = f \cdot [(1 + \frac{-PCD}{IP})^{1/n} - 1] + (1-f) \cdot [(1 + \frac{R}{IP})^{1/n} - 1] $$









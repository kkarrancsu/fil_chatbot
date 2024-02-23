# A quick, back-of-the-envelope, comparative analysis of gas costs in Filecoin, Ethereum, and Polygon







### Gas usage in a nutshell

*Gas fees* are the costs users pay for executing transactions and smart contracts on blockchains. In general, these fees are meant to compensate network participants (e.g., miners, validators, etc.) for their participation on the network and prevent network spam and abuse by attaching a cost to transactions and smart contract execution. In general, gas fees (**in fiat**) are determined by three main factors:

1. **Gas Used:** This is the amount of computational resources required to process a transaction or execute a smart contract. Gas is measured in *gas units*, and different operations have different gas requirements depending on their complexity. For instance, a simple ETH transfer might require 21,000 gas units. In contrast, more complex operations in smart contracts can require significantly more gas.

2. **Gas Price (Base Fee):** This is the price users are willing to pay per unit of gas. This price is typically given in terms of tokens per gas unit. It is given in the native token of the network (e.g., FIL per gas unit in Filecoin, ETH/per gas unit in Ethereum, etc.). In Filecoin, Ethereum, and Polygon, this *Gas Price* is referred to as *Base Fee* and gets adjusted on an epoch-to-epoch basis to network congestion, according to the well-known *EIP-1559 mechanism*

3. **Token Price:** This is the current market price of the network token (e.g., ETH or MATIC) in dollars. Since the cost of FIL and MATIC are (much) lower than the price of ETH, transactions in Filecoin and Polygon are generally cheaper than transactions in Ethereum.


The total gas fee for a transaction (in native tokens) is calculated as follows:
\begin{aligned}
\mathsf{Total \ Gas\ Fee \ (in \ tokens) = Gas \ Used \ \times \ Base \ Fee},
\end{aligned}
and in fiat is given by
\begin{aligned}
\mathsf{Total \ Gas\ Fee \ (in \ fiat) = Gas Used \  \times \ Base \ Fee\times  \ Token \ Price}.
\end{aligned}

So, for example, while a `transfer` function in Polygon and Ethereum consumes 21000 gas units, the base fee in either network might be different. For the sake of argument, suppose that the base fee in Ethereum is currently $1\times 10^{-9}$ ETH/gas unit and that the base fee on the polygon network is $100\times10^{-9}$ MATIC/gas unit. The cost of that `transfer` in either network amounts to 0.000021 ETH in Ethereum and 0.0021 MATIC in Polygon. In terms of *tokens*, this example clearly shows that the Ethereum transactions have a lower gas cost; however, it is work mentioning that, at the time of writing, 1 ETH $\approx$ 1829 MATIC, and as such the transaction in Polygon would then be the cheaper of the two. For completeness, a `send` transaction in Filecoin, takes about  1,273,063 gas units. While this seems much larger than the other two, it is important to remember that these are units of a different network. A base fee of 0.5 $\times 10^{-9}$ FIL/gas unit would result in about $0.00065$ FIL for that transfer.



### Methodology

We now discuss an **approximate** way of comparing gas usage in the Ethereum, Polygon, and Filecoin networks. The approach presented below relies on several approximations. It will not necessarily be very accurate, but we produce it in the hopes that it can provide a ***Ballpark*** estimate of these gas equivalences. 

#### Ethereum Vs. Polygon
Polygon started as an EVM-powered, PoS-based Layer 2 solution to the Ethereum scalability issue. Thus, given that Ethereum switched to a PoS mechanism since *The Merge* (September 2022) and that Polygon is built on top of the EVM, we will assume, for the sake of simplicity, a 1:1 equivalency in terms of `Gas_used` for transactions in both networks. Notice that this is indeed the case for simple transactions, such as `transfer`. Notice that this is only in terms of gas units used, and the other factors that affect gas fees (i.e., base fee and token price) are generally not the same in both networks.


#### Ethereum Vs. Filecoin
**Remark.** *Notice that since we are taking a 1:1 equivalence between Ethereum and Polygon, the following approximations also hold for the equivalence between gas in Filecoin-Polygon.*

Comparing gas usage between two networks is complex, as such an amount can depend on several factors. However, as a first approximation, we extend the "back-of-the-envelope" computation presented [here](https://github.com/filecoin-project/ref-fvm/issues/1401), in the hopes that it can be helpful. 

We gathered gas usage data from Ethereum and Filecoin networks after the Ethereum merge (15 September 2022). This data was obtained on an epoch-to-epoch basis. We then proceeded to compute the average gas usage in each network over a given period (5 minutes). Then we compared the amount of gas used on each network. More formally, let $G^e_t$ and $G^f_t$ denote the total amount of gas used at epoch $t$ by the Ethereum and Filecoin network, and let $\tilde{G}^e_t$ and $\tilde{G}^f_t$ denote the 5-minute average gas usage of $G^e_t$ and $G^f_t$. Our analysis consists of estimating the 5-minutes ratio of averages defined below. $$\mathsf{ratio}_t:=\frac{\tilde{G}^f_t}{\tilde{G}^e_t}$$
Notice that the procedure above results in a time series for $\mathsf{ratio}_t$ form, which we can obtain several statistics: 



![](https://hackmd.io/_uploads/H1FswHxmh.png)



|       |   ratio of gas usage |
|:------|-----------:|
| mean  |   330.334  |
| std   |    18.4305 |
| min   |   173.043  |
| 25%   |   322.206  |
| 50%   |   330.353  |
| 75%   |   338.842  |
| max   |   638.058  |

In summary, we can then estimate that. 


**average ratio**
1 gas unit in Ethereum $\approx$ 1 gas unit in Polygon $\approx 330$ gas in Filecoin  

**lower bound**
1 gas unit in Ethereum $\approx$ 1 gas unit in Polygon $\approx$ 173 gas in Filecoin


**upper bound**
1 gas unit in Ethereum $\approx$ 1 gas unit in Polygon $\approx 638$ gas in Filecoin 



## Gas consumption of common EVM operations

We can use the numbers above as well as the [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf) to compute the gas equivalence of various common EVM operations


| Operation name                    | GU Ethereum | GU FIlecoin, low | GU FIlecoin, mid | GU FIlecoin, high | Description                                                                                                |
| --------------------------------- | ----------- | ---------------- | ---------------- | ----------------- | ---------------------------------------------------------------------------------------------------------- |
| $G_{\mathrm{zero}}$              | 0           | 0                | 0                | 0                 | Nothing paid for operations of the set $W_{\mathrm{zero}}$.                                               |
| $G_{\mathrm{jumpdest}}$          | 1           | 173              | 330              | 638               | Amount of gas to pay for a JUMPDEST operation.                                                             |
| $G_{\mathrm{base}}$              | 2           | 346              | 660              | 1276              | Amount of gas to pay for operations of the set $W_{\mathrm{base}}$.                                       |
| $G_{\mathrm{verylow}}$           | 3           | 519              | 990              | 1914              | Amount of gas to pay for operations of the set $W_{\mathrm{verylow}}$.                                    |
| $G_{\mathrm{low}}$               | 5           | 865              | 1650             | 3190              | Amount of gas to pay for operations of the set $W_{\mathrm{low}}$.                                        |
| $G_{\mathrm{mid}}$               | 8           | 1384             | 2640             | 5104              | Amount of gas to pay for operations of the set $W_{\mathrm{mid}}$.                                        |
| $G_{\mathrm{high}}$              | 10          | 1730             | 3300             | 6380              | Amount of gas to pay for operations of the set $W_{\mathrm{high}}$.                                       |
| $G_{\mathrm{warmaccess}}$        | 100         | 17300            | 33000            | 63800             | Cost of a warm account or storage access.                                                                  |
| $G_{\mathrm{accesslistaddress}}$ | 2400        | 415200           | 792000           | 1531200           | Cost of warming up an account with the access list.                                                        |
| $G_{\mathrm{accessliststorage}}$ | 1900        | 328700           | 627000           | 1212200           | Cost of warming up storage with the access list.                                                         |
| $G_{\mathrm{coldaccountaccess}}$ | 2600        | 449800           | 858000           | 1658800           | Cost of a cold account access.                                                                             |
| $G_{\mathrm{coldsload}}$         | 2100        | 363300           | 693000           | 1339800           | Cost of a cold storage access.                                                                             |
| $G_{\mathrm{sset}}$              | 20000       | 3460000          | 6600000          | 12760000          | Paid for an SSTORE operation when the storage value is set to non-zero from zero.                          |
| $G_{\mathrm{sreset}}$            | 2900        | 501700           | 957000           | 1850200           | Paid for an {\small SSTORE} operation when the storage value's zeroness remains unchanged or is set to 0  |
| $R_{\mathrm{sclear}}$            | 15000       | 2595000          | 4950000          | 9570000           | Refund given (added into refund counter) when the storage value is set to zero from non-zero               |
| $R_{\mathrm{selfdestruct}}$      | 24000       | 4152000          | 7920000          | 15312000          | Refund given (added into refund counter) for self-destructing an account.                                  |
| $G_{\mathrm{selfdestruct}}$      | 5000        | 865000           | 1650000          | 3190000           | Amount of gas to pay for a SELFDESTRUCT operation.                                                         |
| $G_{\mathrm{create}}$            | 32000       | 5536000          | 10560000         | 20416000          | Paid for a CREATE operation.                                                                               |
| $G_{\mathrm{codedeposit}}$       | 200         | 34600            | 66000            | 127600            | Paid per byte for a CREATE operation to succeed in placing code into state.                                |
| $G_{\mathrm{callvalue}}$         | 9000        | 1557000          | 2970000          | 5742000           | Paid for a non-zero value transfer as part of the CALL operation.                                          |
| $G_{\mathrm{callstipend}}$       | 2300        | 397900           | 759000           | 1467400           | A stipend for the called contract subtracted from $G_{\mathrm{callvalue}}$ for a non-zero value transfer. |
| $G_{\mathrm{newaccount}}$        | 25000       | 4325000          | 8250000          | 15950000          | Paid for a CALL or SELFDESTRUCT operation which creates an account.                                        |
| $G_{\mathrm{exp}}$               | 10          | 1730             | 3300             | 6380              | Partial payment for an EXP operation.                                                                      |
| $G_{\mathrm{expbyte}}$           | 50          | 8650             | 16500            | 31900             | Partial payment when multiplied by the number of bytes in the exponent for the EXP operation.              |
| $G_{\mathrm{memory}}$            | 3           | 519              | 990              | 1914              | Paid for every additional word when expanding memory.                                                      |
| $G \text{txcreate}$              | 32000       | 5536000          | 10560000         | 20416000          | Paid by all contract-creating transactions after the {\textit{Homestead} transition}.                     |
| $G_{\mathrm{txdatazero}}$        | 4           | 692              | 1320             | 2552              | Paid for every zero byte of data or code for a transaction.                                                |
| $G_{\mathrm{txdatanonzero}}$     | 16          | 2768             | 5280             | 10208             | Paid for every non-zero byte of data or code for a transaction.                                            |
| $G_{\mathrm{transaction}}$       | 21000       | 3633000          | 6930000          | 13398000          | Paid for every transaction.                                                                                |
| $G_{\mathrm{log}}$               | 375         | 64875            | 123750           | 239250            | Partial payment for a LOG operation.                                                                       |
| $G_{\mathrm{logdata}}$           | 8           | 1384             | 2640             | 5104              | Paid for each byte in a LOG operation's data.                                                              |
| $G_{\mathrm{logtopic}}$          | 375         | 64875            | 123750           | 239250            | Paid for each topic of a LOG operation.                                                                    |
| $G_{\mathrm{keccak256}}$         | 30          | 5190             | 9900             | 19140             | Paid for each KECCAK256 operation.                                                                         |
| $G_{\mathrm{keccak256word}}$     | 6           | 1038             | 1980             | 3828              | Paid for each word (rounded up) for input data to a KECCAK256 operation.                                   |
| $G_{\mathrm{copy}}$              | 3           | 519              | 990              | 1914              | Partial payment for \*COPY operations, multiplied by words copied, rounded up.                             |
| $G_{\mathrm{blockhash}}$         | 20          | 3460             | 6600             | 12760             | Payment for each BLOCKHASH operation.                                                                      |


## Disclaimer 

*Converting gas units from one network to another is a complex task, which might be approached on a case-by-case basis, given each network's different purposes and underlying mechanisms. The approach presented in this report is intended to be a "back-of-the-envelope" estimation for guidance purposes. It should not be relied upon for making critical decisions or pursuing specific business directions. To fully grasp the equivalence of gas units between networks, a thorough gas profiling and analysis must be conducted by seasoned developers, taking into account the nature of the operations, the gas unit values for specific tasks, and the gas prices and token conversion rates at the time of comparison. Furthermore, by using the information provided in this report, you agree that the authors, Protocol Labs, or the publishers of this report are not responsible for any direct, indirect, consequential, or incidental losses or damages that may result from the use of, or reliance on, the information provided herein. This report is not intended to provide investment advice. Nothing contained herein should be construed as an offer to buy or sell or a solicitation of an offer to buy or sell any token, security, or another financial instrument.*


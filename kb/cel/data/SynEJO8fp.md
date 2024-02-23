# Problem Overview 

## Problem

Nascent ecosystems like Filecoin offer the potential for high yields, but their high volatility can deter investors from holding large amounts of native assets like FIL. This creates a demand for protocols that can facilitate the hedging of relative volatility between assets. The problem can be framed as one of designing a method to allow investors to earn high yields on nascent assets like FIL, while holding other valuable assets with strong downside protection.

An options contract that takes a deposit in a more mature asset like ETH, BTC, or USDC, converts it to Filecoin at market price, and sells the user an option to sell back the FIL at current market price solves this problem to an extent. However, this contract relies on someone taking the other side of the trade and assuming the Filecoin price risk, which may be difficult to find.

## Insights

Smarter synthetic asset-based solutions can solve this problem without relying on someone being on the other end of the trade. To incorporate the key advantages of options, any solution should:

- Limit investor losses to the price of the option by always exchanging FIL back to the amount of ETH that was initially deposited.
- Allow investors to benefit from price increases when the price of FIL relative to ETH increases.
- Enable investors to earn FIL yield throughout the whole process.

A synthetic asset-based solution could look something like this:

- A smart contract takes an ETH deposit, converts it into FIL at the market price, and issues the equivalent amount of "eFIL" tokens. Let the price of FIL = x1 ETH.
- The smart contract tracks the price changes of FIL relative to ETH.
    - If the price of FIL falls relative to ETH, the investor can mint more eFIL tokens to maintain the same collateral ratio with the same ETH deposit. This means that the investor does not risk losing ETH from their initial deposit just because of a FIL price drop. Additionally, the investor always has the option of unwrapping their eFIL tokens for ETH at the market price.
    - If the price of FIL rises, the investor can either increase their ETH deposit or burn the required amount of eFIL tokens to maintain the same collateral ratio. Suppose the price at this point is x2 ETH. A strategy here could be to swap (x2 - x1) eFIL tokens to FIL, trade it for ETH, and add that ETH to the deposit. Therefore the investor would have made a profit of (x2 - x1) ETH.
    - eFIL tokens can be swapped for pFIL tokens to fund storage provider (SP) operations, and investors can earn yield on the FIL rewards.

To provide extra downside protection to the held assets, the collateral can be through multiple assets including stablecoins or even tokenized gold.

### Numerical Example

- At time $t_0$, assume that the price of ETH in terms of FIL is 500. At this point in time, user A deposits 1 ETH into the contract. Assuming overcollaterization of 0% for now, user A consequently receives 500 eFIL in return. 
    - At the contract level, some percentage (assume 70%) of the ETH deposited is converted to FIL and is put to work by SPs. By doing this, users get about 7% Annual Yield on the 500 eFIL that they hold (7% APY because, an SP gets 10% returns on all staked FIL, but only 70% is converted and put to work. The remaining stays in the contract as ETH for immediate wnrapping). Therefore, at day $t_0 + 1$, the balance of eFIL would become 535.
    
- At time $t_1$, assume that the price of ETH in terms of FIL goes up to 600.  With a overcollateralization rate of 0%, this means that the rightful amount of eFIL that user A should get for their deposit is 600 eFIL. The user can thus mint 100 more eFIL now. 
    - The yield that is earnt by the eFIL holder is applied to collateral of 600 now, so therefore at day $t_1 +1$, the interest paid out is 42 eFIL instead of the usual 35. Therefore, the user earns yield on a larger collateral. Therefore, the eFIL total now becomes 535 + 42 + 100 = 677 eFIL. 
    - **Note**: this does mechanism assumes simple interest payouts for now. Based on the daily locked rewards, earned eFIL rewards could also get restaked leading to a higher yield - this parts need figuring out

- At time $t_2$, assume that the price of ETH in terms of FIL goes down to 400. With a overcollateralization rate of 0%, this means that the rightful amount of eFIL that user A should get for their collateral is 400 eFIL. The user has 2 option - (1) Burn 200 eFIL tokens, or (2) Increase the ETH collateral to 1.5 ETH. 
    - One strategy that user A can do is to swap 200 eFIL to 200 FIL tokens, and sell them for 0.5 ETH. 
    - They can then add the 0.5 ETH to their original collateral without having to burn any tokens and compromise on the amount of yield that they earn. 
    - They have thus made a profit of 0.5 ETH due to the price difference 

- At any time, user A can always unlock their ETH collateral by paying the required eFIL to the contract. 
    - Using a mechanism that limits the amount of ETH collateral that is converted to FIL and put to work by SPs, you ensure that there is enough ETH liquidity in the protocol for SPs to unstake at any time. 
## Allocations
- Shyam: 50% (DRI)
- Vik: 30% 
- Mike: 33%
- AX 25%

## ToDo's
- [ ] Research into Synthetic Assets
    - [x] Synthetix
    - [ ] UMA
- [ ] Research into Lending Protocols
    - [ ] AAVE
    - [ ] Compound
- [ ] Research into DeFi Options
    - [ ] Opyn
    - [ ] Lyra 
    - [ ] DoPex
- [ ] Review of paper on Multi-Collateralization
- [ ] Draft design for our own protocol
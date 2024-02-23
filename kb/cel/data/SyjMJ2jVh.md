# Pledge Shortfall Spec: Policy 2

## Summary
- At any point where an SP needs to lock new Initial Pledge, they can opt to lock less than the notionally required amount, up to a maximum shortfall fraction of ⅓ of the initial pledge. 
- In exchange for taking a shortfall in the upfront amount of collateral, future rewards are split: the SP agrees to ‘repay the protocol’ by burning a proportion of future rewards.
- The proportion of rewards burnt is dynamic, decreasing with shortfall. A proportion continues to be burnt until the obligation is gradually paid off. 
- The fraction not burned is distributed the ordinary way between immediate and vested release rewards.
- The mechanism can be generalised, so that on top of repaying the protocol through burning the amount of shortfall taken, an additional fee could be charged. This can be included if further analysis indicates it is a necessary property. 


## Actor State

### Miner Actor State

Miner actor state tracks one new field: `shortfall_fee`: 
```
/// Total rewards and added funds locked in vesting table. 
locked_funds: TokenAmount, // Existing 

/// Absolute value of debt this miner owes from unpaid fess. 
fee_debt: TokenAmount, // Existing

/// Sum of initial pledge requirements of all active sectors. 
initial_pledge: TokenAmount, // Existing

/// Amount of shortfall fee remaining to pay. 
shortfall_fee: TokenAmount, // New!
```

### Power Actor State
No change for the basic construction

## Actor Behavior

### Sector Activation 

Sector activation includes the `ProveCommit` and `ProeCommitAggregate` methods. These methods get an additional parameters for the amount of pledge to lock: 

```
struct ProveCommitSectorParams { 
    sector_number: SectorNumber, 
    proof: Vec<u8>, 
    pledge: TokenAmount // New!
}
```

**Sector Onboarding**
```
/// Maximum shortfall as fraction of notional pledge requirement.
/// Note, the value for this parameter is subject to further consensus 
/// and risk analysis. 
MAX_SHORTFALL_FRACTION = 0.33 // Can be in range 10-50% TBD

/// Calculate Minimum Pledge Required at Sector Activation 
pledge_requirement = initial_pledge_for_power(...)

minimum_pledge_requirement = pledge_requirement * (1 - MAX_SHORTFALL_FRACTION)

/// Update State 
if params.pledge >= minimum_pledge_requirement { 
    miner.initial_pledge += params.pledge 
    miner.shortfall_fee += pledge_requirement - params.pledge
} else {
    abort('Insufficient Pledge')
}
```

### Burn and Receiving Rewards

**Set the SP repayment (burn) rate:** 
```
/// Exponent to the shortfall fraction determining the take rate
/// from earned rewards.
/// Value or generalisation to be developed in subsequent further
parameteristion analysis.
DEFAULT_SHORTFALL_TAKE_RATE_EXPONENT = 0.75

/// Outstanding fee as fraction of pledge plus that obligation
/// Note that as it's repaid, this denominator becomes smaller
/// than the initial nominal pledge requirement.
shortfall_fraction = miner.shortfall_fee / 
(miner.initial_pledge + miner.shortfall_fee)

/// Note, this is subject to refinement both in form and
/// parameterisation.
MIN_BURN_RATE = 0.01 / Avoid Zeno's paradox 
burn_take_rate = min(MIN_BURN_RATE + 
shortfall_fraction ** DEFAULT_SHORTFALL_TAKE_RATE_EXPONENT, 1)
```
The burn take rate formulation presented here can be generalised in a number of ways. Two ways are: (i) by making the exponent dynamic, allowing it to change based on the level of shortfall, and (ii) introducing an additional burn fee that increases with shortfall uptake. 

Both generalisations can in effect make shortfall progressively less attractive with the level of uptake. One indirectly through repayment dynamics without any additional cost (but through less favourable cash flow), and one explicitly through an additional fee rate component. 

While full specification of these generalisations is beyond the scope of this introductory spec, sketches for each are presented at the end.

**Distribute rewards between burning, vesting, and immediate release:**
```
/// Stream proportion of rewards to be burnt
if shortfall_fraction > 0 {
    burn_amount = earned_reward * burn_take_rate burn(burn_amount)
    miner.shortfall_fee -= burn_amount
}

/// After the burnt portion has been taken, recieve
/// the rest, splitting between vest and immediate release
earned_reward = earned_reward * (1 - burn_take_rate)
immediate_reward = 0.25 * earned_reward
vesting_reward = 0.75 * earned_reward
vest(vesting_reward)
```
### Sector Expiration
When a sector expires, the outstanding burn obligation is reduced proportionally to the fraction of power represented by the sector. The sector’s initial pledge amount is returned in full. The remaining ratio of the burn obligation to pledge requirement thus remains constant.
```
/// Reduce any burn obligation proportionally to the power removed.
/// Reduce (forgive) outstanding fee in proportion to the
/// power removed.
remaining_power_frac = (miner.power - sector.power) / self.power
self.shortfall_fee *= remaining_power_frac
miner.pledge -= sector.pledge
miner.power -= sector.power
```

### Sector Termination 
Similar to expiration following termination fee payment

## Generalized Burn Rate Variants
Two variants are set out that can generalise the dynamics to make uptake of the shortfall progressively less attractive. 

Variant 1 increases the shortfall repayment rate by changing the exponent, which makes it less attractive under most network conditions. 
```
/// Dynamic burn rate variant 1

/// Note, this increases the burn rate with shortfall usage
/// and therefore in effect makes high usage less attractive 
shortfall_usage = shortfall_fraction / MAX_SHORTFALL_FRACTION
burn_take_rate = min(MIN_BURN_RATE + 
    shortfall_fraction ** (1 - shortfall_usage), 1)
```
Variant 2 introduces an additive rate penalty.
```
/// Dynamic burn rate variant 2 

/// The form and parameterisation of the penalty function
/// `progressive_uptake_penalty` remain to be determined
shortfall_usage = shortfall_fraction / MAX_SHORTFALL_FRACTION
burn_take_rate = min(MIN_BURN_RATE + shortfall_fraction, 1) +       
    progressive_uptake_penalty(shortfall_usage)
```
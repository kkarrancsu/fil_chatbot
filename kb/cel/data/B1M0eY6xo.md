---
title: Baseline Crossing - Preliminary analysis
tags: Almanac
---

#### December 2022

## Motivation

Filecoin uses a hybrid model for mining that incorporates two minting mechanisms - Simple minting and Baseline minting.
Simple minting is the most common minting we see in other blockchains, where newly minted tokens follow a simple exponential decay model. This type of minting aims to encourage early adoption since the number of new tokens awarded to miners gets exponentially smaller as time goes on.

In order to encourage long-term storage and to align incentives with the growth of the network’s utility, Filecoin introduced Baseline minting. The team defined a baseline function that determines the expected level of growth for the network. The tokens reserved for Baseline minting are only distributed if the network as a whole achieves or goes beyond that predefined growth goal. Thus, if storage providers don’t onboard storage at the expected rate, the network will not mint at full speed and the total rewards distributed will be lowered. When the network achieves the growth goals, tokens are minted at full capacity and follow a “normal” exponential decay.

In April 2021, the network crossed the baseline function and started to grow faster than the initial goal. This was a major milestone for Filecoin (more info here). Since then, the network has been minting tokens at full speed since the network has managed to maintain a high growth rate. However, current market conditions (e.g. China’s crackdown, crypto market crash, etc.) are putting pressure on the Storage Providers (SPs) and their growth capability.

## Goals and Milestones

The goal of this project is to investigate this problem and understand the potential consequences of the network experiencing a downward baseline crossing. In particular, we will estimate the likelihood of observing a baseline crossing assuming current market conditions, we will model the consequences of that event for both SPs and the network as a whole, and we will look into potential mitigation strategies.

The work is divided into 4 main milestones:

1. BlockScience work review *[skipped due to time constraints]*
2. Baseline Crossing prediction *[completed]*:
    - [Power model spec v1](/qN_D4q_aSXK_cWM7KGcasA)
    - [Power model spec v2](/O6HmAb--SgmxkjLWSpbN_A)
    - [Power scenarios analysis](/XmcZLLMHSVyyTqGiBuhOmA)
3. Side effects modeling *[completed]*:
    - [Impact on minting and rewards](/Rba7W4ZtQGe1w25maWZhSA)
    - [Final report](/Ny_e0UkXRGCTDA0oT3me2A)
4. Mitigation mechanisms
    - There are no plans for mitigation mechanisms.

## Main conclusions

* The network’s Raw Byte Power is estimated to fall below the exponential baseline target in mid February 2023 triggering a decrease in the rate of baseline minting.
* This report investigates the impact of a baseline crossing on storage providers’ ROI. Our models predict that while minting rate will decrease, storage providers ROI is expected to remain stable following the baseline crossing from above.
* The regulation of supply in response to changes in rawbyte storage growth is a unique adaptive feature of Filecoin’s minting. The predicted crossing shows the mechanism is working as originally designed and ensures alignment between the network’s growth targets and storage providers’ block reward incentives.

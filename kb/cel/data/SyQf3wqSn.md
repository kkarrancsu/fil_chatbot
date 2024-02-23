# IC3 Project proposal: A Multi-dimensional EIP1559 mechanism

## Project Background
The recent surge in blockchain technology and decentralized applications (dApps) has laid bare the limitations of existing Ethereum transaction systems, thereby triggering a pressing demand for an efficient and predictable gas fee structure. The proposed project aims to address this challenge by integrating the EIP 1559 mechanism with gas lanes, an innovative approach to enhance transaction predictability and network scalability.

Ethereum Improvement Proposal 1559 (EIP 1559) has already marked a significant shift in the way transaction fees operate on the Ethereum network. With its introduction, users can enjoy more predictable gas fees and improved transaction inclusion reliability, while simultaneously mitigating some of the issues related to miner extractable value (MEV). Nonetheless, during periods of high demand, the problem of transaction congestion remains, which calls for a solution that can further optimize the process.

This is where the idea of a multi-dimensional EIP1559 mechanism (AKA 'gas lanes') comes into play. Gas lanes propose the segregation of transactions into different 'lanes' based on several criteria [[2]](https://arxiv.org/abs/2208.07919). This criteria could be, e.g., compute vs storage intensive messages [[3]](https://hackmd.io/IVCFQYo7T--v-xNxmhfv0w). An additional
criteria could be grouping messages by the types of user. 

The intention is to ensure that higher priority transactions can proceed unimpeded, even during network congestion, effectively creating a fast lane for urgent transactions. This strategy is akin to implementing traffic lanes in traditional road networks to handle different traffic needs and improve overall efficiency.
By combining the benefits of EIP 1559 and the gas lanes concept, this project aims to create a next-generation transaction system for Ethereum, capable of enhancing user experience and supporting the growing needs of the Ethereum ecosystem. This amalgamation not only promises to streamline transaction processes but also ensures sustainability and scalability, thereby making Ethereum more accessible and reliable for users worldwide.

## Goals and Deliverables

The main goal of this project is for student to gain a deep understanding of the EIP1559 transaction fee mechanism, and how its multi-dimensional extension (gas lanes) can be used to improve upon it in some specific cases. 

Given the complexity of the proposed project and the 1-week timeframe for a student hackathon, it would be reasonable to break down the project into a series of smaller, manageable deliverables. The goal is to have tangible outcomes that demonstrate the feasibility and potential benefits of the EIP 1559 mechanism combined with gas lanes. Ultimately, a proof of concept of how gas lanes work and how it can be used to mitigate increasing gas costs in some blockchains would be ideal. Here are some suggested deliverables, that we expect to adjust once a team has been created.

1. **Conceptual Design and Documentation:**

    Students will need to thoroughly understand the EIP 1559 mechanism and the concept of gas lanes, and come up with a design that integrates both effectively. This will include creating flowcharts, network diagrams, or pseudocode as required. They should also compile comprehensive documentation that details the proposed system's design and potential impacts on the Ethereum ecosystem.

2. **Simulation Tool:**

    Given the time constraints, developing a real, functional implementation might be too ambitious. Instead, a simulation tool that demonstrates the performance of the proposed system under various network conditions could be a more feasible goal. This tool could simulate the behaviour of transactions under different gas prices and congestion levels, demonstrating how the system prioritizes transactions and reduces congestion.

3. **Smart Contract Templates:**

    Students could develop a set of smart contract templates that demonstrate how transactions might be created and managed under the proposed system. These templates could include features like setting the gas price for different lanes and handling lane assignments.

4. **Presentation and Demonstration:**

    A key deliverable should be a clear, concise, and engaging presentation of the project. This would include a demonstration of the simulation tool and smart contract templates, as well as a walkthrough of the conceptual design. The presentation should effectively communicate the project's goals, the potential benefits of the proposed system, and how the deliverables achieved during the hackathon contribute to the broader vision of the project.

## Challenges
 
The main challenge that we can identify priori is the tight deadline.  The project might be entirely too complex to be finalised in a week, due to both analytical and implementation challenges.  Once a team has been agreed upon, a revised version of the deliverables should be produced, making small consessions taking into account the size of the team, its expertise, etc. 

An additional challenge that has been identified in the implementation of gas lanes is identifying to which lane(s) each message belongs to. This is further discussed in Reference [[3](https://hackmd.io/IVCFQYo7T--v-xNxmhfv0w)]. 

## References

1. https://ethresear.ch/t/multidimensional-eip-1559/11651
2. https://arxiv.org/abs/2208.07919
3. https://hackmd.io/IVCFQYo7T--v-xNxmhfv0w
4. https://arxiv.org/abs/2201.05574
5. https://arxiv.org/abs/2012.00854


**About the DRI**

*Juan Pablo (JP) works as a research scientist at the CryptoEconLab of Protocol Labs (PL). His main research interest lie at the intersection of computational probability, uncertainty quantification, and Web3. JP  has worked in topics such as understanding gas dynamics, mechanism design,  stochastic and data-driven agent-based models, and DeFi-native exotic derivates. Prior to joining PL  JP worked as a quantitative researcher for a DeFi company and as a PostDoc at the EPFL. He  holds a Ph.D in mathematics from the chair of Scientific Computing and Uncertainty Quantification of the same University.*
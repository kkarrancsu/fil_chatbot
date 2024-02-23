# Saturn Aliens Project

[Filecoin Saturn](https://strn.network/#whatissaturn) is a decentralized Content Delivery Network (CDN) that aims to accelerate the retrieval of media files from the Filecoin Network and IPFS. The project is currently ongoing and is a major bet for 2022.

According to [Saturn’s roadmap](http://strn.network/#roadmap), the project will go over different states of maturity. In Q2 2022, we hope to launch a **private network with a few L1 nodes** in order to test the L1-IPFS interactions and see if Saturn can perform better than simply using the IPFS gateway. It is important to note that this first network will be composed of trusted workers and thus we don’t expect it to include any undesirable behavior from the side of retrieval providers (which are called node operators).

In H2 2022, we plan to launch **a more complete network that incorporates both L1 and L2 nodes**. This second network will be public and node operators will be paid in Filecoin for their services. Interestingly, since the network won’t have any crypto-economics design, RPs will be paid in a centralized manner based on the logs we submit. This is where this project will be most needed since we will have to **analyze these logs and determine if node operators are exhibiting any undesired behaviors**.

Finally, in Q1 2023, we hope to complete a **detailed plan for the crypto-economics of retrieval** in Saturn. The idea is to use the learnings taken from the logs collected during H2 2022 to improve the way payments are distributed from content publishers to node operators.

Thus, the CryptoEconLab will play an important role in the last two phases of Saturn. First, we will need to support the project in the analysis of the logs and in defining how node operators will be paid. And second, we will guide the design of the crypto-economics for retrieval scheduled for Q1 2023. **Saturn Aliens aims to focus on the first part, i.e., analyzing Saturn requests’ logs to detect undesirable behavior from node operators (aka Alien operators 😁) and defining how they are paid.**

## Key questions

- What undesirable behaviors (for both clients and node operators) are we trying to avoid in Saturn retrieval networks?
- How can we monitor and detect the undesirable behaviors defined in the first question? More generally, what methods should we have in place to detect unknown anomalous behavior?
- When analyzing logs to pay node operators:
    - How do we distribute rewards amongst the operators in order to incentivize fast and reliable retrievals?
    - Which mechanisms should we have in place to penalize the detected undesirable behaviors?

## Additional resources

- [Saturn website](https://strn.network/)
- [Saturn Roadmap](https://www.notion.so/pl-strflt/Saturn-Roadmap-e049d0c9dbbd4fb6901941bdb8dff076)
- [GitHub repo](https://github.com/protocol/cel-retrieval)
- [Retrieval Markets Working Group](https://retrieval.market/)
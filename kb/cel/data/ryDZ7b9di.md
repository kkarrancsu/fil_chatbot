---
title: Value Flow and KPIs in Bacalhau
tags: CoD
---

# Value Flow and KPIs in Bacalhau

#### Alex Terrazas, March 2022

## Actors

The primary actors in the proposed Bacalhau system include the (1) **users,** notionally data scientist who would like to utilize Filecoin network data to answer a business or social question;  (2) **clients**, the persons or entities paying for the compute; (3) **storage providers,** existing Filecoin storage providers who have valuable data in storage that is needed for a compute process, ****(4) **compute providers**, who provide compute nodes.  Compute providers are, in this MVP, storage providers; (5) **validators**, who earn tokens or FIL for either (a) rewarding correct computations or (b) finding fraudulent or erroneous computing; (6) **schedulers/match makers**, who match compute providers with user compute requests; (8) **data originators**, public entities such as Landsat who original the data to be used, (7) the **Filecoin network**.  

## Costs Involved

### **Users**

Users (primarily data scientists but also computer vision researchers and others) will typically make requests for compute by submitting a computer code that can run on the compute nodes.  Users will typically write code on their local machine, test the code locally, and then submit it to the network.  

Users will only pay costs when they assume the role of clients; otherwise, users will primarily use their time to interact with the network.  The value for users includes access to data that are accessible on the network.  

The work of data science often involves a long periods of exploratory data analysis, changing hyper parameters, and checking the results of the compute.   There can be considerable back-and-forth in the checking of processes.  As an aside, a large percentage (>> 50%) of processes are terminated early or produce unusable results.  This back-and-forth can be improved by running and testing locally before committing to the Bacalhau network.  To improve the UX for clients, tools for examining results and terminating processes.  

Finally, finding interesting data on the Filecoin Network can be a challenge.  Adoption of Bacalhau is strongly dependent on improving the public’s ability to identify data on the network.  Kaggle is an excellent model for identifying available data sets.  Another suggestion is to provide Python accessible data sets.

### **Clients**

A client’s main role is funding the compute of users.  Clients are likely to be diverse including (1) organizations promoting social good, (2) businesses wishing to profit from publicly available datasets, (3) universities as part of the research and education mandates, (4) individual data scientists conducting self-funded research, and (5) even PL and the Filecoin Foundation (see below)

Clients will be required to deposit FIL into an account that will fund the gas and fees required for the expected compute.  Depending on whether clients can be “slashed” for malicious behavior (i.e., submitting compute requests that overwhelm the network or the target compute node), *collateral may also be required.*  If a compute request exceeds the client’s unlocked available balance, the compute request will presumably be denied.  

In many cases, the client will also pay for storage of the results of computations.  Separate storage contracts will be required for storage of results.  Processed raw data may become more valuable than the original data itself and it may sometimes be desirable to overwrite raw data with the processed data through a Snap deal.  

Finally, it is not clear if the storage providers (who also provide compute) will be paid for retrieval or whether that will be subsumed in the compute contract.  

***Filecoin as Client.***  

*Another prominent client could be the Filecoin Network itself.  All data run through cleaning and post processing on their way to their use in building models.  In some cases, it may make sense for Filecoin itself to process data.* 

 *A good example is Landsat 9 satellite data, which are refreshed every 16 days.  These images undergo a number of processing steps before they become useful to the research community.  There is no reason to have each researcher run these processes individually.  By having Filecoin sponsor these processes, the network would better support its mission of with more usable data.*    

### **Compute providers**

Compute providers incur capital costs when purchasing depreciable equipment as well as operating costs of data traffic within their own networks and when transferring data to and from other storage nodes.  There may be a need to temporarily store results during a midway point. Some legitimate compute processes can use considerable memory and disk space while other processes may be lightweight. In many cases, compute will be a one-time event while storage is The scheduler may need to make some estimate; alternatively, the client may be charged after the compute.  Some compute providers charge by the cycle.  The downside of that is that the client may experience sticker shock.

Compute providers (who are also storage providers) also incur opportunity costs because they are diverting resources that the can use for sealing or data storage.  Opportunity costs may be overcome by adding resources to their network but. given limited resources, a choice between compute or storage may be required.  At the same time, offering compute may be a way for some storage providers to diversify their income streams.  

Technical expertise is another factor (and cost) for compute providers to consider.  If additional overhead in the form of specialized software (e.g. CUDA, TensorFlow) is required, that play a part in the provider’s choice to participate as a compute provider.     

## **Value Flow**

Cloud compute is already well established in the marketplace.  One existential questions for Bacalhau is what value can be added above and beyond AWS EC and Google Kubernetes, for example.  One of the biggest advantages of Bacalhau is the number of data sets already on the Filecoin network.  

### **Client**

Value flows to the client from not having to upload data to the network (which can be a substantial benefit) and by being able to store results inexpensively on the network.  *Note: the client may not want to publicly store results that they have written code for and paid compute for.   Furthermore, if clients simply want the results for their computations can they request those from a temporary storage location.  Finally, how does the new storage contract work if the client want to (more or less) permanently store the data. Perhaps a storage contract can be combined with the compute contract.*  

### **Storage Provider**

Value flows to the storage providers in terms of fees for processing the data and from the storage of results.  *Note:  This brings up an interesting question as to what rate storage providers can charge for storing results and whether results must be stored with the same provider.*  

### **Validators**

Typically, validators are seeking a bounty or fee for verification of the results.  It is not clear how this works in the CoD model because only the client knows what the computations are going to be.  Self-validation may be a good model in this case.  Data scientists usually do extensive checking on the results (and often discover their own errors).  In the case of satellite image processing and cloud removal (a use case for Bacalhau), the results are obvious to the client. 

### **Scheduler/match-maker**

The scheduler is part of the Filecoin network presumably and is a necessary part of the workflow.  Some applications may require heavy GPU processing while other applications can be run on CPUs.  It is not yet clear how the match making process will occur.  Value flows to the client and the compute provider if the scheduler does an efficient job at aligning needs with compute resources.

### **Filecoin Netowrk**

The network benefits from Bacalhau by making its large data assets more useful.  CoD has the potential to turn the data into information.  The storage of the results of Bacalhau might result in increased utilization of Filecoin capacity.  There is the potential for a virtuous circle where data assets are enhanced by compute and *vice versa.*  

## Key Performance Indicators

Important metrics for success include (1) increasing the number of bytes of data utilized on the network that are attributable to Bacalhau. The rate of utilization of certain datasets (e.g., Landsat 8) through Bacalhau processes should be easy to determine and directly reflect impact. (2) the number of nodes offering compute including nodes offering GPU compute (3)  new storage based on Bacalhau processes; (4) number of unique wallets executing a job, a measure of how widespread the use of Bacalhau is, (5) number of jobs executed.  Note that this metric may be corrupted if users resubmit jobs because of network failure or Bacalhau-related errors, (6) number of cores on the network, a measure of network power, and (7) number of storage providers participating

## Outstanding Questions

Power.  Will compute providers be able to earn power on the Filecoin network?  The project currently envision a simple marketplace for compute.  Power and the ability to mine new blocks would be a challenge for Bacalhau; however, compute providers may want this power, especially because they are already members of the network.
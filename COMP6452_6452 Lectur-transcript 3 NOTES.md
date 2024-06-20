Summary of chunk 1:
Summary start from 'SPEAKER 0 thing. OK, Good morning, everyone. I was just waiting for the recording to start. So we we' 
### Blockchain Lecture Notes

#### Block Composition and Miner Activity
- **Block**: Sequential set of transactions in a particular order.
- Miners can collect and add transactions to a block but need an ordered chain.
- **Chain Sequence**: Block N, Block N+1, Block N+2, etc.

#### Proof of Work (PoW)
- **Purpose**: Prevent multiple miners from claiming block creation simultaneously.
- **Mechanism**:
  - Transactions form a Merkle Tree.
  - Timestamp and nonce (initially unknown value).
  - Find a nonce that produces a hash with leading zeros using SHA-256.
  - **Significant Bits**: Hash must meet difficulty target.
- **Hash Function**: SHA-256 used to generate hash values.
  
#### Computational Aspects of PoW
- Miners attempt various nonce values.
- **Nonce Range**: 2^32 potential combinations.
- First miner to find valid nonce claims block creation rights.
- High computational power needed; verification of nonce is simple.
- Specialized hardware (ASICs) or GPUs (initial Ethereum) are used.

#### Mining on Ethereum
- **Ethereum v1**: Uses GPUs due to complexity and memory requirements.
- Memory-intensive along with computational demands.

#### Contention in Block Creation
- **Parallel Block Creation**: Multiple miners may solve the problem at nearly the same time.
- **Satoshi Nakamoto’s Solution**:
  - Let competing blocks coexist temporarily.
  - **Longest Chain Rule**: Eventually, one chain grows longer and becomes dominant.
  
#### Network Dynamics
- Miners prefer to work on the longest chain.
- **Orphan Block**: Block not included in the longest chain.
- **Confirmation Blocks**: Subsequent blocks verifying and building on each other.
  
#### Incentives
- Miners have a higher incentive to extend longer chains.
- Shorter chains have less probability of receiving rewards.
  
#### Probabilistic Nature of Blockchain
- **Bitcoin Whitepaper Calculation**: Shows typical waits times for confirmation.
- **Common Practice**: Wait for 6 blocks before considering a transaction finalized.
  - Higher security applications may wait for 12 blocks.
- Longer chains reflect more computational work.

#### Summary of Important Concepts
- Blockchain structure requires ordered and confirmed block submissions.
- PoW prevents simultaneous block claiming and requires substantial computational work.
- Verification is quick compared to the effort of finding a valid nonce.
- Competing chains are resolved over time through the most computationally intensive chain.
- Miner incentives align with maintaining the longest chain.

Summary of chunk 2:
Summary start from 'It's a basic guarantee in the sense that comes from probability. So it's not a typical transaction. ' 
influenced by multiple factors, including the recent improvement proposals being accepted by the network.

### Transaction Commitment in Blockchain

- **Persistence vs. Probabilistic Finality**:
  - In traditional databases, once data is written, it's persistent due to ACID properties (Atomicity, Consistency, Isolation, Durability).
  - In Bitcoin, even after a transaction is included in a block, probabilistic finality requires waiting awhile to ensure it remains part of the longest chain.

- **51% Attack**:
  - Occurs if an entity controls more than half the network's computational power. This entity can outpace the rest of the network and potentially alter the blockchain.
  - Higher chances in new blockchains with fewer nodes.
  - Established blockchains like Bitcoin, with thousands of nodes, are harder to attack.

### Transaction Lifecycle

- **Submission**:
  - Transaction is submitted to the network and placed in the transaction pool (mempool).
  - If valid, it gets included in a block.

- **Confirmation**:
  - After subsequent blocks are added, the transaction is considered committed (e.g., typically 6 blocks in Bitcoin).

- **Dropping and Resubmission**:
  - Transactions may be dropped from the longest chain and returned to the pool if not included.
  - Ether-based systems like Ethereum may drop transactions after a default period (e.g., 3 hours).
  - Transactions can be resubmitted or superseded with higher fees to incentivize miners.

### Miner Incentives

- **Block Rewards**:
  - Bitcoin miners receive block rewards (e.g., 6.25 BTC, halving to 3.125 BTC approximately every four years or 210,000 blocks).
  - Ethereum miners receive block rewards (~2 ETH by default plus transaction fees).

- **Transaction Fees**:
  - Miners also earn transaction fees, which can be substantial.
  - Ethereum burns a portion of transaction fees to control supply and incentivize miners to focus on block creation rather than competing solely for fees.

### Ethereum Specifics

- **Improvements and Protocol Rules**:
  - Ethereum continuously updates via improvement proposals, including changes to transaction fees and rewards.
  - Example of transaction burning to disincentivize fee competition among miners.

### Economic Impact on Supply and Pricing

- **Supply Reduction**:
  - Reduction in block rewards over time can increase currency value due to decreased supply (e.g., Bitcoin halving events).

### Miscellaneous

- **Block Creation Complexity**:
  - Building a block in Ethereum is easier than in Bitcoin due to the different consensus mechanisms and computational requirements.

#### Relevant Ethereum Improvement Proposal (EIP)
- **EIP-1559** (example improvement proposal):
  ```solidity
  // EIP-1559 introduces a base fee mechanism to Ethereum
  function calculateBaseFee() public view returns (uint256) {
      uint256 parentBaseFee = block.header.baseFee;
      if (block.gasUsed == block.gasLimit) {
          return parentBaseFee + parentBaseFee / 8; // Increase fee
      } else if (block.gasUsed < block.gasLimit / 2) {
          return parentBaseFee - parentBaseFee / 8; // Decrease fee
      } else {
          return parentBaseFee; // Keep fee constant
      }
  }
  ```

### Future Considerations

- **Sustainability of Blockchain Networks:**
  - Potential longevity of Bitcoin and Ethereum depends on community support and handling of issues like inflation, security, and miner incentives.
  - Speculated transition events, like zero block reward, balance supply-demand dynamics in the long run.

### FAQs
- **Mining Fee Adjustments:** Burned portion in Ethereum reduces supply and incentivizes network stability.
- **Transaction Replacement Issues:** Default settings can be adjusted by individual miners, affecting transaction lifecycle.
- **System Configuration:** Miners can modify configurations affecting how long transactions are retained in the pool.

Overall, these aspects underscore the complexity and evolving nature of blockchain technology, highlighting significant differences between traditional databases and decentralized networks like Bitcoin and Ethereum.

Summary of chunk 3:
Summary start from 'just suddenly everyone discusses and say, OK, it's time to change our mining fees. And somewhere sin' 
the power of -9 of an ether. It shows how much gas you need to pay per unit if you are, say, willing to wait for more than 30 minutes versus if you want immediate confirmation. So, Ethereum's transaction fee model provides flexibility for users to decide based on urgency.

- **Hardware Requirements for Ethereum 2.0:**
  - Significantly lowered power consumption.
  - Reliable devices preferred, though advanced hardware isn't mandatory.
  - Ethereum 2.0 can theoretically run on a Raspberry Pi.

- **Ethereum's Model:**
  - Uses an account balance model akin to bank accounts.
  - Each address has a balance, unlike Bitcoin's UTXO model.
  
- **Transaction Signing:**
  - Public key: Proves identity.
  - Private key: Used for signing transactions.
  - Transaction ID: Unique hash for each transaction.

- **Nonce in Ethereum:**
  - Used for ordering transactions.
  - Distinct from nonce in mining.

- **Gas:**
  - Gas Limit: Max gas a block can contain.
  - Gas Price: Cost per unit of gas.
  - Gas Used: Gas consumed by a transaction.
  - Determines transaction fee.

- **Ethereum Gas Tracker:**
  - Shows different gas prices based on urgency.
  - Gwei: Fee unit, \(10^{-9}\) Ether.
  - Higher fees for faster confirmations.

- **Sharding and Layer Two:**
  - Sharding: Abandoned approach of partitioning data.
  - Layer Two: Scaling solution discussed in future classes.

- **Proof of Stake (PoS):**
  - Validators: Stake 32 Ether to build blocks.
  - Random selection algorithm.
  - Penalties for failing duties or acting maliciously.
  - Aligns incentives: Maintaining network integrity retains cryptocurrency value.

- **Finalization and Block Confirmation:**
  - Average block time: 12 seconds.
  - Confirmation blocks: Increased to 64 for safety (~7.5 mins).
  - Hyperledger Fabric: Example of faster block finality in private blockchains (fractions of a second).

- **General Concepts:**
  - Higher transaction fees can expedite transaction inclusion.
  - In Ethereum, users decide fees, unlike merchants in traditional payments.
  - Wallet attacks: Risk from stolen private keys.
  - Multi-copy sync becomes more challenging with increasing copies.

Examining these concepts reveals the intricacies and ongoing evolution within blockchain technology, especially in systems like Bitcoin and Ethereum. Different blockchain implementations handle aspects such as transaction fees, finality, and validator motivation uniquely, underscoring the diverse approaches in achieving decentralized consensus.

Summary of chunk 4:
Summary start from 'the power of minus six ether. , even if I look at this morning, I still saw 888. So I didn't update ' 
### Transaction Fees and Timing in Ethereum

- **Impact of Transaction Fees on Speed:** 
  - Higher transaction fees generally result in faster transaction inclusion into blocks.
  - When network is less busy, even lower fees might ensure quick inclusion.
  - Fees correlate with inclusion probability:
    - Higher fees: ~100% probability within ~500 seconds.
    - Moderate fees: ~70% probability within ~500 seconds.
  - Example: For quick transactions in automated market makers or initial coin offerings, higher fees are crucial.

- **Dynamic Nature of Fees:**
  - Busy network -> Higher fees.
  - Cryptocurrency prices affect fee dynamics:
    - Higher prices = Slightly lower transaction fees.
    - Increased activity can negate linear fee predictions.
  - Urgency and application specifics influence fee setting.

- **Gas Limit and Gas Price in Ethereum:**
  - **Gas**: Ethereum’s way of accounting resource usage.
  - **Gas Limit**: Maximum gas user is willing to pay.
  - **Gas Price**: Cost per unit of gas.
  - Example: Fuel efficiency and cost analogy.

- **Gas Limit Importance:**
  - Protects against endless loops and excessive ether loss.
  - Ensures efficient network usage and prevents denial of service attacks.
  - Limits safeguard both the user and the network.

### Key Factors Influencing Transaction Fees

1. **Network Load:**
   - More pending transactions -> Higher fees required for faster inclusion.
   
2. **Cryptocurrency Prices:**
   - Rapid price changes drive user activity, affecting fees.
   
3. **User Application Needs & Urgency:**
   - Critical for automated market traders or fast ICO participants.
   
4. **Security & Error Handling:**
   - Rare cases of excessive fees due to errors or attacks.
   - Attacks can still be valid transactions, impacting miners.

### Practical Considerations

- **Gas and Smart Contracts:**
  - Computational and storage costs factor into gas usage.
  - Optimizing smart contracts reduces gas consumption.

- **Example in Project Work:**
  - Project 1: Activity like looping through friend addresses uses computational resources.
  - Storage or computation-heavy operations incur higher gas costs.

- **Risk Management:**
  - Setting gas limits prevents exhaustive ether loss due to endless loops.
  - Ensures the network remains exposed to diverse transactions rather than stalling.

### Conclusion of Concepts

Understanding the nuances of transaction fees, gas limits, and gas prices is crucial. Ethereum users must balance transaction urgency, network conditions, and fee willingness to optimize their interactions on the blockchain.

Summary of chunk 5:
Summary start from 'to get executed. But if you set the wrong gas limit, it's gonna fail. So any transaction that you do' 
### Gas Limit and Transaction Failures
- Setting an incorrect gas limit leads to transaction failure.
- All Ethereum transactions have a base gas fee of 21,000.
- Minimum gas fee example: transferring ether from Alice to Bob.
- Additional gas costs for:
  - Executing smart contracts (e.g., might take 140,000 gas).
  - Storing data or deploying contracts.
- Smaller contracts incur lower costs; larger contracts incur higher costs.
  
### Gas Price
- Gas price is the market price set according to urgency.
  - Higher gas price for faster inclusion.
  - Lower gas price if willing to wait.
- Multiply gas limit by gas price to get total cost.
- Gas used must be less than or equal to the set gas limit to avoid transaction failure.
  
### Block Gas Limit
- Blocks have a gas limit (e.g., 30 million).
- Miner may use only a fraction of total gas limit.
  - Example: Miner may use only 3 million out of 30 million.
- Gas limit prevents overloading network with too many transactions.
  
### Ethereum vs. Bitcoin Throughput
- Ethereum: 1,428 ether-only transactions every 12 seconds.
- Bitcoin: Max of 1,500 transactions per 10 minutes.
- Ethereum processes more transactions per second compared to Bitcoin.

### Ethereum Block Structure
- More complex than Bitcoin due to smart contracts.
- Uses three Merkle trees for:
  - World state: all data on the blockchain.
  - List of transactions.
  - Transaction traces: detailed information on gas used, address changes, etc.
- Storage needs for Ethereum node: ~7 terabytes.
- Bitcoin node: ~1.5 terabytes.

### Block Propagation and Interblock Time
- Interblock time for Ethereum: 12 seconds.
- Bitcoin interblock time: 10 minutes.
- Propagation time: <1 second.
- Propagation time influenced by latency, primarily constrained by the speed of light.
- Interblock time ensures blocks propagate before the next one starts.
- Bitcoin retains 10-minute interval due to historical and political reasons rather than technical necessity.

### Coding Context Example
If applicable, use the following code to set gas limit and gas price in Ethereum transactions:

```javascript
const tx = {
  from: '0xAliceAddress',
  to: '0xBobAddress',
  value: web3.utils.toWei('1', 'ether'),
  gas: 21000,  // minimum gas limit
  gasPrice: web3.utils.toWei('5', 'gwei')  // example gas price
};
web3.eth.sendTransaction(tx)
  .on('receipt', console.log);
```

### Key Considerations
- Ensure gas limit set correctly to avoid transaction failure.
- Be aware of network conditions and set appropriate gas price.
- Block gas limits and miner behavior impact transaction inclusion rate.
- Processing capabilities differ between blockchains like Ethereum and Bitcoin.

Summary of chunk 6:
Summary start from 'change. Can Bitcoin run? Uh, let's say, run under 12 seconds like Ethereum. Probably. Only thing is,' 
the block itself, so I might run my own transactions to take advantage of this. Instead of taking a regular transaction fee, I could potentially gain more. This leads to MEV (Maximal Extractable Value).

### Bitcoin vs Ethereum
- Bitcoin block time: ~10 minutes.
- Ethereum block time: ~12-15 seconds.
- Technical reasons for Bitcoin's longer block time:
  - Initial constraint to ensure miners have time to propagate blocks.
  - Larger block size (1 MB).

### Ethereum 1.0 vs Ethereum 2.0
- **Ethereum 1.0**: Single node handling both transaction execution and consensus.
- **Ethereum 2.0**: Split into two components:
  - **Execution Client**: Responsible for transaction execution and smart contracts.
  - **Beacon Node**: Responsible for consensus.
- Must operate both for a full Ethereum node.

### Terminology
- **Execution Client / Engine Client / Eth1 Client**: Handles execution of transactions.
- **Consensus Client / Beacon Node / Eth2 Client**: Manages consensus.

### Miners and Network Considerations
- **Altruistic Miners**: Individuals or organizations running nodes for network health rather than reward (e.g., Ethereum Foundation).
- **Transaction Inclusion**:
  - Focus can vary: Some aim for higher MEV rather than transaction fees.
  - Differing motivations lead to unpredictable behaviors.
  - Example: Sandwich attacks where reordering of transactions yields higher profits.

### Mining Dynamics
- Miners prioritize transactions based on:
  - Transaction fees.
  - Potential MEV.
- Larger computational power impacts efficiency but also complexity.

### Proof of Work vs Proof of Stake
- **Proof of Work**:
  - High energy consumption due to intense competition (e.g., Bitcoin).
  - Example: ~10,000 nodes competing globally.

- **Proof of Stake**:
  - Significantly lower power consumption.
  - Fewer nodes needed to build blocks (selection based).
  - Example: Ethereum 2.0 where one node builds the block upon selection.
  - Selection probability can be tied to the stake (32 ETH per node).

### Additional Issues
- **MEV (Maximal Extractable Value)**:
  - Miners can reorder or insert transactions to maximize profits beyond regular fees.
- **Power Consumption**:
  - Bitcoin's power usage criticized for its high levels.
  - PoW vs PoS: PoW involves massive redundancy in computations, while PoS is efficient with selected validators.

### Questions from Discussion
- **Large Computation Power**: Efficiency varies based on individual miner strategies and market demands.
- **Updating Systems**:
  - Moving to PoS significantly reduces the power requirements.
  - PoS mechanisms depend on the selection process and stake distribution.

### Real-World Applications and Issues
- **Competition among nodes**: Visa vs Mastercard as analogies of decentralized networks.
- **Marketplace Dynamics**: Business justifications for multiple nodes and competing platforms to avoid monopolies but at the risk of increased resource usage.

Continue with further questions and discussions when we return.

Summary of chunk 7:
Summary start from 'the block, because all the transactions come to my transaction pool. Now if I see someone is trying ' 
### Real-World Applications and Issues (cont.)

- **Transaction Ordering and Miner Advantage**: 
  - Miners receive all transactions in their pool.
  - If large volume trading affects price, miners can gain by positioning their transactions first.
  - Example: Miner buys an asset at $1.05 before a large purchase drives the price up, then sells for profit.
  - Miners may prioritize these profits over transaction fees.
  - Estimated value extracted by miners: ~$100 million/year.
  
- **Probabilistic Immutability**: 
  - Transactions in a block seem immutable but can be dropped if not in the longest chain.
  - Termed as probabilistic immutability rather than absolute.

### Blockchain Mechanisms

- **Bitcoin vs Ethereum**:
  - Ethereum: Uses account balance model.
  - Bitcoin: Uses UTXO (Unspent Transaction Output) model.

- **Throughput**:
  - Ethereum has a higher transaction throughput compared to Bitcoin.
   
### Hyperledger and Hyperledger Fabric

- **Overview**:
  - **Hyperledger Fabric**: Private, permission blockchain for consortiums or organizations.
  - Originally developed by IBM, now a Linux Foundation project.
  - Varies with versions like Hyperledger Besu (similar to Ethereum for private networks) and Hyperledger Indy (identity management).

- **Key Features**:
  - **Modules and Consensus Protocols**:
    - Modular framework allows different consensus protocols.
    - Early support included multiple consensus protocols.
    - Currently primarily uses Proof of Authority.
    - Plan to incorporate PBFT (Practical Byzantine Fault Tolerance).
  - **Smart Contracts**:
    - Known as chain codes in Hyperledger Fabric.
    - Support multiple languages: Go, Node.js, Java.
  - **Transaction Fees**:
    - No transaction fees as it's a private network.

- **Performance**:
  - Higher transaction performance due to controlled trust environment.
  - Block creation latency: ~2 seconds.
  - Throughput: 1000+ transactions per second, depends on hardware.
  - Private transactions: ~400 transactions per second, higher complexity than public ones.

- **Data Management**:
  - State management using key-value pairs.
  - Visibility of transactions and states ensures transparency for network participants.

### Example Transaction Process in Hyperledger Fabric

- **Transaction Proposal**:
  - Example: Owner Max transfers car ownership to Alice.
  - Proposal created and must be endorsed.
- **Endorsement**:
  - Designated endorsing peers validate the transaction.
  - Check Max’s private key signature.
  - If valid, endorsements are signed and added.
- **Ordering Service**:
  - Ordered and validated by special nodes called "Orderers".
  - Valid transactions added to the block.

*Code Example: State Management (Key-Value Pair)*
```javascript
// Example of a JSON object to represent a car in Hyperledger Fabric
let car = {
    "key": "Car3",
    "value": {
        "owner": "Max",
        "make": "Volkswagen",
        "model": "Passat",
        "color": "yellow"
    }
};

// Proposing a transaction to change ownership
function changeOwnership(car, newOwner) {
    car.value.owner = newOwner;
    return car;
}

// Endorsing transaction
function endorseTransaction(transaction, endorser) {
    // Simulating endorsement with endorser's private key
    transaction.endorsements.push(endorser.sign(transaction));
    return transaction;
}
```

### Validation and Block Creation

- **Validation**:
  - Orderers ensure transaction authenticity and endorsements.
- **Block Formation**:
  - Transactions placed in ordered blocks.
  - Blocks linked consecutively to form the blockchain.

---
These detailed notes capture the key details, mechanisms, and processes of blockchain technology as discussed in the lecture transcript.

Summary of chunk 8:
Summary start from 'second one third one like that and here's a block containing all of them. And then he broadcast that' 
### Block Creation and Broadcasting

- **Transaction Handling**:
  - Transactions get endorsed and execute to ensure sender legitimacy.
  - Example: Car ownership update, voting tally.

- **Read-Write Set**:
  - Read-Write Set equals data's state before and after transaction.
  - Version numbers track changes, e.g., `version 0` to `version 1` after ownership update.

- **Orderer's Role**:
  - Validates transaction signatures and endorsements.
  - Orders transactions sequentially into blocks (e.g., Block N, Block N+1).
  - No proof of work/stake; predefined nodes build blocks (proof of authority).

- **Broadcasting**:
  - Ordered blocks are broadcasted to the network.
  - All nodes validate transactions in received blocks.

### Double Spending Problem

- **Sequential Ordering**:
  - Ensures singular ownership transfers (e.g., car cannot be sold to both Alice and Bob).
  - Only one validated transaction (based on first-seen version) persists.

- **Conflicts and Validation**:
  - If transaction's version number does not match ledger’s current version, it is discarded.
  - Similar to enterprise concurrency control (e.g., airline booking systems managing seat availability).

### Transaction Efficiency and Finality

- **Parallel Processing**:
  - Multiple transactions are endorsed and executed in parallel.
  - Only conflicting transactions (version number changes) are invalidated.

- **High Throughput**:
  - Enables processing a large number of transactions simultaneously, reducing delays.
  
- **Latency**:
  - Transaction finality is typically between 2 to 4 seconds.
  - Faster than Ethereum (12+ seconds) and Bitcoin (requiring multiple block confirmations).

### Comparison to Bitcoin/Ethereum

- **Separate Execution and Persistence**:
  - Execution and endorsement happen before persistence into the ledger.
  - Parallel processing enhances efficiency.

- **Read-Write Set Details**:
  - Ensures data consistency similar to traditional databases.
  - Validations during writing, requires retry if data changes.

### Key Concepts

- **Read-Write Set**: Tracks data state versions pre- and post-transaction.
- **Ordering Service**: Organizes sequential transaction processing.
- **Proof of Authority**: Designated nodes are consistently responsible for block creation. 

---
Additional questions and detailed explanations were offered for better understanding complex topics. The key takeaway is the efficient handling and validation of transactions utilizing the read-write set for high throughput and swift transaction finality.

Summary of chunk 9:
Summary start from 'wrong here. Uh, OK, so going further. So let's say if this is the hyper fabric network. So each circ' 
---

### Hyperledger Fabric Network Architecture

- **Nodes**:  
  Each circle represents a node running the software. Nodes can be part of multiple sub-networks or channels.

- **Channels**:  
  Logical partitions within the network. Ensures segregation of data so that activities in one channel are invisible to another. Example: Separate channels for interactions with suppliers and customers to maintain privacy.

### Membership Service Provider (MSP)

- **Role**:  
  Not an actual service but a file containing public keys.
  
- **Purpose**:  
  Adds public certificates to register nodes into the network, ensuring only authorized nodes join.

### Private Data Collections

- **Function**:  
  Allows selective visibility of data. Example: A customer can see the quantity of beef purchased but not its cost. 

### Network Roles

1. **Clients**:  
   Entities (e.g., Alice, Bob, Max) who want to transact and can be members of multiple channels.
  
2. **Peers**:  
   - Maintain the ledger using a key-value store (LevelDB or CouchDB).
   - Can act as endorsers by executing transactions and digitally signing them.
  
3. **Orderers**:  
   - Responsible for ordering transactions and forming blocks.

### Consensus and Policy

- **Consensus Algorithm**:  
  Hyperledger Fabric primarily uses Proof of Authority.
  
- **Policies**:  
  Define how many endorsements are required for a transaction. Example: Minimum two organizations' signatures needed.

### Data Structure and Finality

- **Maintaining World State**:  
  Uses account balances as key-value pairs. Example: Account number as key, balance as value.
  
- **Transaction Finality**:  
  Immediate (2-4 seconds) after database write, contrasting Bitcoin/Ethereum's need for multiple block confirmations.

### Sample Policy Definition

```json
{
    "policy": {
        "identities": [
            { "role": { "name": "member", "mspId": "Org1MSP" } },
            { "role": { "name": "member", "mspId": "Org2MSP" } }
        ],
        "policy": {
            "2-of": [{
                    "signed-by": 0
                },{
                    "signed-by": 1
                }]
        }
    }
}
```

### Q&A Insights

- **MSP**:  
  Helps register nodes but does not sign transactions.
  
- **Consensus**:  
  Not based on proof of work, mainly Proof of Authority but configurable.
  
- **World State**:  
  Reflects account balances in key-value format.
  
- **Finality**:  
  Immediate upon database write, taking about 2-4 seconds.

---

**Questions?**

Summary of chunk 10:
Summary start from 'on the final Blockchain. What would be your definition of a Blockchain? SPEAKER 2 A chain of blocks.' 
### Blockchain Overview

- **Definition:** 
  - A chain of blocks ordering transactions that everyone in the network agrees upon.
  - Ethereum, Bitcoin, and Hyperledger each have unique ways of implementing blockchain. 
  - PBFT can handle 110,000 transactions per second.

- **Purpose:**
  - Consistent global tracking of ownership.

### Smart Contracts

- **Concept:** 
  - User-defined code executed by the entire network, maintaining the ledger.
  - Similar to stored procedures in databases but user-defined and network-executed.
  - Code is deterministic: same input yields same output.

- **Components:**
  - Functions for predefined actions (e.g., voting, adding restaurants).
  - Storage to keep track of related data (e.g., list of friends, their votes).

- **Access Control:**
  - Functions like `Manager` to restrict actions to specific roles.

- **Implementation:**
  - An object-like contract in Ethereum reflecting real-world ownership and transactions.

### Deterministic Code

- **Determinism:**
  - Smart contracts require deterministic functions. 
  - Example non-deterministic: `random` functions in Python/JavaScript.
  
- **Consensus Issue:**
  - Non-deterministic functions cause inconsistency across nodes executing the contract.

### Best Practices in Smart Contract Programming

- **No Random Functions:** 
  - Ethereum’s Solidity doesn’t support random functions to maintain consistency.

- **Input and Ledger State:**
  - Smart contract execution depends on both the input and the current ledger state.
  - Voting example: Previous votes affect future contract behavior.

### Transactions and Messages

- **Execution:**
  - Smart contracts are triggered via transactions (Ethereum also calls them "messages").

- **Trustworthiness:**
  - Only transactions signed by a private key can deploy contracts, ensuring immutability.

### Smart Contract Lifecycle

- **Deployment:**
  - Smart contracts are deployed as blockchain transactions.
  
- **Execution Monitoring:**
  - Post-deployment, smart contracts can be executed and monitored for integrity and transparency.

### Blockchain Properties Applied to Contracts

- **Immutability:**
  - Once deployed, code cannot be altered.

- **Transparency:**
  - Code and subsequent transactions are visible and verifiable.
  
- **Re-execution:**
  - Contracts can be repeatedly executed till disabled.

### Practical Example: Voting Contract

- **Voting Logic:**
  - Total votes tracked; decisions based on majority.
  - Pre-existing votes affect new transactions.

### Q&A Insights

- **MSP (Membership Service Provider):**
  - Registers nodes but doesn’t sign transactions.

- **Consensus Protocol:**
  - Typically Proof of Authority, configurable.

- **World State:**
  - Reflects current balances in key-value format.

- **Finality:**
  - Immediate upon database write (~2-4 seconds).


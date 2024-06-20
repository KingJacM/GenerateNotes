> Summary of chunk 1:
> Summary start from 'SPEAKER 0 OK, I think we can get started. ,, hi, everyone. I think this is the first time you're see' 
Instructor: Salil (Prof. in Computer Science, specialized in cybersecurity, network, distributed computing, and Blockchain).

### Announcements
- **Project/Lab Deadline:** 
  - First project due by Sunday.
  - Get into groups (preferably 4 per group but 3 or 5 is allowed).
  - Task due by end of this week: Tell what you want to do in your project.
  - Feedback will follow.
- **Importance of the Project:**
  - A chance to create something notable for your resume.
  - Choose a topic you're passionate about.

### Blockchain Integration in Software Architecture

- **Initial Consideration:**
  - Assess if Blockchain is necessary before using it.
  - Avoid using Blockchain just because it’s trendy.
  - Examples where Blockchain makes sense: Decentralized finance, supply chain management.

- **Key Points:**
  - **Past Trend:** Many unnecessary Blockchain applications were created.
  - **Current Industry Stabilization:** Identified suitable applications.

### Design and Requirements in Software Architecture

- **Software Architecture Process:**
  - Start with requirements.
  - Develop multiple designs.
  - Consider nonfunctional requirements (performance, security, usability).
  - Evaluate designs based on performance metrics such as latency and throughput.
  - Assess trade-offs in designs.

- **Decision-Making:**
  - Different designs have different strengths and weaknesses.
  - Choose design based on specific requirements and trade-offs.

### Blockchain’s Role in Software Architecture

- **Four Aspects:**
  - **Storage**
  - **Computation**
  - **Communication**
  - **Asset Management**

### Additional Resource
- **Interesting Article:** Unspecified, but meant to give further insights into the topic.

---

Instructor noted orientation adjustments for better audibility and recording accuracy.

> Summary of chunk 2:
> Summary start from 'author's name, but if you click on that, you'll find the names of the author. So it's very well cite' 
### Decision Process for Implementing Blockchain

- **Initial Steps:**
  - Assess necessity: Do you need to store state?
    - If no: No need for Blockchain.
    - If yes: Proceed to next question.

- **Evaluating Writers:**
  - Single writer: Prefer a centralized database for better performance.
  - Multiple writers: Consider Blockchain based on additional criteria.

- **Trusted Third Party:**
  - Can you use a trusted third-party (TTP)?
  - If yes: TTP can verify state transitions.
    - No Blockchain needed if TTP is sufficient.
    - Consider Blockchain if auditability is needed.

- **Availability of Trusted Third Party:**
  - Always online: Functions like a certificate authority (CA) for verifying.
  - Not always online: Example of PKI (Public Key Infrastructure) for certificates.
    - Trusted entities get authority to write, consider permissioned Blockchain.

- **Trust Level of Writers:**
  - Trusted writers: Centralized or distributed database may suffice.
  - Not trusted: Blockchain becomes more relevant.

- **Public Verifiability:**
  - Required: 
    - Public Permissioned Blockchain: Certified to write, public to read.
  - Not required: 
    - Private Permissioned Blockchain: Certification needed to read (e.g., supply chain data).

- **Unknown Writers:**
  - Use permissionless Blockchain (e.g., Bitcoin).

### Practical Considerations in Projects
- Use these steps for project feasibility.
- Implementing Blockchain should be based on clear, justified necessity.

```python
class BlockchainDecision:
    def __init__(self, needs_state, writers, trusted_ttp, writers_trusted, public_verifiability):
        self.needs_state = needs_state
        self.writers = writers
        self.trusted_ttp = trusted_ttp
        self.writers_trusted = writers_trusted
        self.public_verifiability = public_verifiability

    def should_use_blockchain(self):
        if not self.needs_state:
            return "No Blockchain needed"
        if self.writers == 1:
            return "Use a centralized database"
        if self.trusted_ttp:
            return "Trusted third party can be used"
        if self.writers_trusted:
            return "Use a centralized or distributed database"
        if not self.writers_trusted and self.public_verifiability:
            return "Public Permissioned Blockchain"
        if not self.writers_trusted and not self.public_verifiability:
            return "Private Permissioned Blockchain"
        if self.writers == 'unknown':
            return "Use a permissionless Blockchain"
        return "Consider Blockchain based on specific context"

# Example Usage
decision = BlockchainDecision(needs_state=True, writers=2, trusted_ttp=False, writers_trusted=False, public_verifiability=True)
print(decision.should_use_blockchain())
```

---

References to papers: Check author's name for proper citation. 

Instructor emphasized identifying when Blockchain is logical. Follow the flowchart to assess necessity and proper type. 

For further understanding, study an interesting article linked here [unavailable in transcript].

> Summary of chunk 3:
> Summary start from 'not very strict, but at least it gives you reasonable guidance on whether a Blockchain makes sense i' 
written on the chain. Off-chain data or links to external data must be diligently managed to preserve their integrity alongside the Blockchain's promise. Another notable property is the decentralization. The key idea behind Blockchain is the removal of a single point of failure. Data is replicated across several nodes, making the system resilient to single-node failures.

### Advantages of Blockchain:
1. **Immutability**:
    - Ensures transactions, once committed, remain unchanged.
    - Below is an example of ensuring immutability:
    ```python
    def add_transaction(self, transaction):
        if self.valid_transaction(transaction):
            self.current_transactions.append(transaction)
            return self.last_block['index'] + 1
    ```

2. **Transparency**:
    - All transaction records are visible to everyone.
    - Ideal for auditing purposes.

3. **Integrity**:
    - Guarantees data recorded on the chain is tamper-proof due to consensus protocols.

4. **Decentralization**:
    - Removes single points of failure.
    - Replicates data across multiple nodes.

### Limitations:
1. **Scalability**:
    - Not suitable for storing vast amounts of data.
    - Best for smaller data chunks or metadata.
    
2. **Resource Intensive**:
    - Consensus algorithms, like Proof of Work, require significant computational power.
    
3. **Complexity**:
    - Implementing and maintaining Blockchain solutions are technically complex.
    
4. **Regulatory and Compliance Issues**:
    - Legal recognition and adherence to jurisdictional regulations are a challenge.

### Selecting the Right Blockchain:
- **Public Blockchains**:
  - Example: Bitcoin, Ethereum.
  - Decentralized and trustless environment.
  - Anyone can join and participate.
  
- **Private Blockchains**:
  - Controlled environment with known participants.
  - Examples: Hyperledger, Quorum.
  - Performance efficient and regulatory compliant.
  
- **Consortium Blockchains**:
  - Hybrid of public and private.
  - Multiple organizations govern the network.
  - Used in banking, supply chain, etc.

### Key Management:
- Critical for securing public-private key pairs.
- Outsourcing key management or using third-party services for secure handling.
- Example code snippet for public-private key generation:
```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate public key
public_key = private_key.public_key()

# Serialize private key
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Serialize public key
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
```

### Practical Applications:
- **Financial Services**:
  - Cross-border payments, DeFi platforms.
  
- **Supply Chain**:
  - Track and trace goods, ensuring authenticity.
  
- **Healthcare**:
  - Secure, shareable electronic health records.

### Blockchain Types:
1. **Permissionless**:
    - No central authority.
    - Public participation.
  
2. **Permissioned**:
    - Controlled access.
    - Organizations decide participants.

### Conclusion:
Blockchain technology embodies many advantageous properties that can be utilized across various fields, but it is essential to comprehend its limitations and perform a cost-benefit analysis to determine its suitability for specific use cases.

> Summary of chunk 4:
> Summary start from 'on the chain. Right? If you're using tokens to represent physical assets, that doesn't give you inte' 
### Qualities of Blockchain

1. **Non-repudiation**:
    - Transactions, once created and logged, cannot be denied by the creator.
    - Each transaction is tied to a specific key, which in turn identifies the creator.
    - Exception to non-repudiation: if private keys are compromised.

2. **Availability for Reads**:
    - Blockchain ensures high availability due to data being replicated across multiple nodes.
    - Even if several nodes fail, data remains accessible.

3. **Authenticity for Digital Assets**:
    - Digital assets created on-chain ensure genuine and verifiable tokens (e.g., cryptocurrencies).
    - Protocols followed on-chain validate the authenticity, making it tamper-proof.

### Negatives of Blockchain

1. **Lack of Privacy**:
    - Transparency leads to no inherent privacy.
    - All transactions remain visible to everyone, posing privacy issues.

2. **Latency in Transaction Inclusion**:
    - There is a delay in transaction confirmation.
    - Time varies with Blockchain type (Bitcoin takes longer, Ethereum is quicker but still delayed).
    - More blocks might need to be added to ensure a transaction is confirmed, increasing delay.

3. **Throughput Issues**:
    - Blockchain systems like Bitcoin and Ethereum process fewer transactions per second compared to non-Blockchain systems (e.g., Visa, MasterCard).
    - Limited to 7-8 transactions per second for Bitcoin, slightly higher for Ethereum.

4. **Scalability Concerns**:
    - Performance degrades as the load increases (transaction numbers, data size, etc.).
    - Scalability remains limited compared to non-Blockchain systems.

5. **Write Availability Issues**:
    - Writing data involves a consensus process, making Blockchain less available for writes.
    - Transactions may re-enter the waiting pool if blocks get dropped.
    - Blockchain offers high read availability but comparatively lower write availability.

6. **Authenticity Limitation for Off-Chain Assets**:
    - Cannot ensure integrity of physical assets or off-chain data linked by tokens on the Blockchain.
    - The token’s integrity fails if the physical asset it represents is compromised.

### Interactivity and Questions

- Encourage interaction during the lecture for better understanding.
- Ensure examples are contextually accurate and relatable.
  
### Discussion:
- Examples involving physical money vs. digital representation in banks highlight the differences in asset representation and its integrity on the chain.

Be mindful of these points to understand both the strength and weaknesses of Blockchain technology.

> Summary of chunk 5:
> Summary start from 'by by here. What I mean is a good example. Could be a supply chain ecosystem. Right. So I've created' 
- existing state a month ago or whatever point in time you'd like to check, but it's much more natural, i.e., closer to traditional bookkeeping.

### Elements of Blockchain

#### Storage Aspect
- Blockchain is an up-and-only store.
  - Data keeps expanding; once created, data cannot be deleted.
  - Keeps track of all historical data from the origin of the system.
  - Different types of data stored depending on Blockchain type.

#### Types of Data Stored
1. **Account Balances:**
   - Applies to digital currencies like cryptocurrencies.
   - Tracks balances for accounts (who owns how much).
   
2. **Smart Contract Data:**
   - Code, variables, and the state related to the contract.
   - Can store a significant amount of data.
   
3. **Transaction Data:**
   - Stores various fields within each transaction logged in the ledger.
   
4. **Execution Results:**
   - Logs of transaction execution results.
   - Includes transaction receipts and contract execution logs.

#### Ethereum Data Storage
- Uses a Merkle tree structure.
- Stores different information:
  - **World State:** State of all accounts and addresses.
  - **Transaction Data:** Includes standard fields like gas price, gas limit, to/from addresses.
  - **Transaction Receipts:** Standardized data fields.
  - **Log Entries:** Fixed format data.

#### Ledger State Representation
- Varies based on the Blockchain platform.
1. **Bitcoin (UTXO Model):**
   - Tracks unspent transactions (UTXOs).
   - Limited information; amount of money associated with transactions.
   - No global state; balance derivation requires matching UTXOs to public keys.
   
2. **Ethereum (Account Model):**
   - Tracks account balances of individual addresses.
   - More informative and natural representation, similar to a bank.
   - Global state available within the ledger.
   - Queries easily return account balances.

#### Model Comparison
- **UTXO Model:**
  - No global state easily available.
  - Must derive balance using all public keys and UTXOs.
  - Public keys may change with each transaction.
  
- **Account Model:**
  - Immediate global state available.
  - Transaction updates account balance states.
  - Historical states can be queried (e.g., state from a month ago).

#### Impact on Transactions
- **UTXO Transactions:**
  - Each transaction consumes one or more UTXOs and produces one or more UTXOs.
  
- **Ethereum Transactions:**
  - Each transaction updates the latest state of balance.
  - Old states are not lost and can still be queried.

### Further Considerations
- **Bank Analogy:**
  - Ethereum's account model is intuitive, similar to how banks track account balances.
  
---

> Summary of chunk 6:
> Summary start from 'can say, Show me the state of the account at block number five or block number 10 or at certain time' 
system in an inconsistent state. Isolation means transactions are separated from each other until completion. Durability means once a transaction is committed, it remains so, even in the case of a system failure. 

Blockchain inherently reflects these properties. Transactions are atomic since they either get recorded in a block or not at all. Consistency is ensured by consensus protocols, which dictate the state resulting from the transaction. Transactions are isolated because they are executed sequentially within blocks, ensuring durability as the transaction data is immutably stored on the blocks.

- Blockchain: 
  - **Storage:** Replicated
  - **CRUD Operations:** Create, Read (no Update, Delete)
  - **ACID Properties:** 
    - Atomicity: Yes
    - Consistency: Yes
    - Isolation: Yes
    - Durability: Yes
  
- Centralized Database:
  - **Storage:** Not replicated
  - **CRUD Operations:** Create, Read, Update, Delete
  - **ACID Properties:** 
    - Atomicity: Yes
    - Consistency: Yes
    - Isolation: Yes
    - Durability: Yes
  
- Distributed Database (Master/Slave):
  - **Storage:** Replicated or partially replicated
  - **CRUD Operations:** Create (Master), Read, Update (Master), Delete (Master)
  - **ACID Properties:** 
    - Atomicity: Yes (Managed by Master)
    - Consistency: Yes
    - Isolation: Depends on implementation
    - Durability: Yes

- Distributed Database (Fully Distributed):
  - **Storage:** Fully Replicated
  - **CRUD Operations:** Create, Read, Update, Delete (All Nodes)
  - **ACID Properties:** 
    - Atomicity: Yes (Distributed Transaction Protocol)
    - Consistency: Yes
    - Isolation: Depends on implementation
    - Durability: Yes

### Peer-to-Peer Storage

- Peer-to-peer storage has a distributed nature similar to Blockchain.
- Each peer in peer-to-peer storage contributes part of the total storage.
- It does not provide the same level of immutability and historical tracking as Blockchain.

### Cloud Storage

- Cloud storage refers to data storage on remote servers accessed via the Internet.
- It offers high scalability and flexibility.
- Cloud storage solutions might be centralized or distributed.
- They support full CRUD operations and offer various consistency models.

### Replicated State Machine (RSM)

- RSM ensures all nodes in a distributed system follow the same sequence of operations, maintaining a consistent state among nodes.
- Very similar to how Blockchain nodes replicate the ledger.
  
### Conclusion

- Blockchain is unique in its up-and-only storage nature and its immutability.
- It contrasts against more traditional storage solutions like centralized, distributed databases, P2P storage, and cloud storage in several key aspects such as CRUD operations, storage replication, and ACID properties.
- Blockchain's immutability and sequential processing ensure clear and consistent state across all nodes but posing differences in practical implementations when compared with traditional data stores.

Note ends here.

> Summary of chunk 7:
> Summary start from 'database in a inconsistent state. Uh, isolation basically means if you're trying to execute multiple' 
noted for databases and Blockchain. Cloud services generally offer high performance and scalability. They provide elastic scalability, allowing resources to be increased or decreased based on demand.

### More on Cloud Storage

- **Trust:** Centralized, relies on the cloud provider.
- **Management:** User management limited by service terms; primary control resides with the provider.
- **Data Ownership:** Dependent on provider agreements; subject to regional data sovereignty laws.
- **Data Integrity:** Defined by Service Level Agreements (SLAs) but can be questionable.
- **Performance and Scalability:** High elasticity, robust infrastructure to handle large-scale operations.

### Consensus Protocols

- A critical component ensuring data integrity and accuracy in the Blockchain.
- Common protocols:
  - **Proof of Work (PoW):** 
    - Nodes solve cryptographic puzzles.
    - Resource-intensive.
    - Example: Bitcoin.
  - **Proof of Stake (PoS):** 
    - Nodes validate transactions based on the amount of stake.
    - Energy-efficient.
    - Example: Ethereum post-update.
  - **Delegated Proof of Stake (DPoS):** 
    - Stakeholders elect delegates to validate transactions.
    - High throughput.
    - Example: EOS.

### Governance Models

- Varies between centralized, decentralized, and hybrid models.

#### Centralized Governance

- Typically found in cloud and traditional database environments.
- A single entity or organization has oversight and decision-making power.
- Pros: Quick decision-making, clear accountability.
- Cons: Single point of failure, trust reliance on the central authority.

#### Decentralized Governance

- Found in Blockchain environments.
- Governance executed by community consensus.
- Pros: No single point of failure, democratic decision process.
- Cons: Potential inefficiency in decision-making, susceptible to governance attacks.

### Performance Trade-Offs

- Blockchain vs. Traditional Databases:
  - **Speed:** Traditional databases (centralized) offer faster processing due to no need for consensus.
  - **Security:** Blockchain provides better tamper-evidence and fraud resistance.
  - **Scalability:** Distributed databases/Cloud services often scale better via vertical and horizontal mechanisms compared to Blockchain which may struggle due to its consensus mechanism overhead.

### Using Blockchain in IoT

- Benefits:
  - Enhanced security for data exchange.
  - Transparency and auditability.
  - Decentralized control reducing single points of failure.

- Challenges:
  - Resource constraints on IoT devices may limit participation in Blockchain.
  - Network latency and bandwidth constraints affect real-time data processing.
  - Managing the volume of transactions while maintaining performance.

### Smart Contracts
   
- **Definition:** Self-executing contracts with terms directly written into code.
- **Benefits:**
  - Automated execution without intermediaries.
  - Increased transparency.
  - Reduced costs as it eliminates intermediaries.
  
- **Common Languages/Platforms:**
  - **Solidity:** Ethereum.
  - **Chaincode:** Hyperledger Fabric.

Example Smart Contract in Solidity:
```solidity
pragma solidity ^0.4.24;

contract SimpleContract {
    address public owner;

    constructor() public {
        owner = msg.sender;
    }
  
    function getOwner() public view returns (address) {
        return owner;
    }
}
```

### Security Considerations

- Blockchain technology offers strong security but is not immune to attacks:
  - **51% Attacks:** A group controls 51% of the network hash rate.
  - **Sybil Attacks:** Attackers flood the network with nodes they control.
  - **Smart Contract Vulnerabilities:** Bugs in the contract code can lead to exploits. Example: DAO hack.

### Scalability Solutions

- **Layer 1 Solutions:** Modify the underlying Blockchain protocol (e.g., sharding).
- **Layer 2 Solutions:** Build on top of the existing Blockchain to handle more transactions off-chain (e.g., Lightning Network).

### Interoperability Challenges

- **Existing Solutions:**
  - Cross-chain swaps.
  - Interoperability platforms such as Polkadot and Cosmos.
  
- **Challenges:**
  - Varying consensus algorithms.
  - Different transaction models and contract languages.

### Emerging Trends

- **Decentralized Finance (DeFi):** Financial services leveraging smart contracts on Blockchain.
- **Non-Fungible Tokens (NFTs):** Unique digital assets tokenized on Blockchain.
- **Blockchain in Supply Chain:** Enhancing traceability, transparency from source to consumer.

> Summary of chunk 8:
> Summary start from 'said, with Blockchains, you will always suffer. There is no way around that the performance and scal' 
might have a scenario where you need to ensure data availability across multiple regions with low latency and cost also being a significant factor. In this case, a peer-to-peer (P2P) data store might be suitable as it offers decent performance and cost-effectiveness.

---

### P2P Data Store

- **Examples:**
  - BitTorrent
  - StoreJ
  - IPFS (Interplanetary File System)

- **Characteristics:**
  - Decentralized management: No central entity; participation is open.
  - Trust: Decentralized, more reliable due to multiple participating entities.
  - Data Integrity: Generally high due to multiple entities.
  - Availability: Varies with the popularity of the data.
  - Performance: Generally higher than Blockchain but lower than cloud services.
  - Cost: Typically low to medium.

### Replicated State Machines (RSM)

- **Definition:** Fault-tolerant systems creating replicas of state machines allowing clients to interact with multiple replicated servers.
- **Components:**
  - Starting state and transitions based on inputs.
  - Outputs generated from state transitions.

- **Characteristics:**
  - Fault Tolerant: Ensures data accuracy through replication.
  - Follows Consensus: Voting mechanisms for data addition and ordering.
  - Lock Mechanism: Clients acquire and release locks for writing data.
  - Performance: Generally better than Blockchains, lower overhead.
  - Ordering: Transactions are ordered without the concept of blocks.

### Scenarios for Storage Selection

#### High Volume and High Velocity Data

- **Preference:** Cloud Storage
- **Rationale:** Cloud services handle high data volumes and velocity efficiently.

#### High Velocity but Small Volume Data

- **Preference:** Cloud Storage or Distributed Database
- **Rationale:** Both can handle frequent, small-sized data inputs well.

#### Low Velocity and Low Volume Data with High Integrity

- **Preference:** Blockchain
- **Rationale:** Blockchain ensures high data integrity, suitable for transactions with these characteristics.

#### Data Availability Across Regions

- **Preference:** P2P Data Store
- **Rationale:** Effective for low latency requirements across multiple regions with cost efficiency.

---

Questions were posed to apply understanding:
- For a scenario requiring high data volume and high velocity, Blockchain may not be ideal due to its limitations in data storage capacity and processing speed; Cloud Storage is recommended.
- For high velocity but low volume data, like sensor data, distributed databases are practical alternatives to cloud storage.
- In scenarios requiring low velocity and volume but high integrity (e.g., financial transactions), Blockchain provides maximal integrity.
- Finally, for low-cost, high-availability needs across multiple regions, P2P data stores are an appropriate choice due to their decentralized nature and cost efficiency.

Every scenario emphasizes different strengths and weaknesses of storage solutions, guiding tailored choices suitable for specific data management requirements.

> Summary of chunk 9:
> Summary start from 'might say you have some medium volume data which is not frequently accessed. Right? So it's more lik' 
executed consistently across all nodes in the Blockchain network to ensure the same outcome. 

---

### Computation in Blockchains

#### Smart Contracts

- **Definition:** Programmes stored and executed on the Blockchain.
- **Execution:** Code runs on multiple nodes, ensuring consistency across the network.
- **Flexibility:** 
  - **Ethereum:** High expressiveness for business logic, complex programmable behaviours.
  - **Bitcoin:** Limited flexibility.
- **Transparency:** Contract code is visible to all participants.

#### Considerations for Smart Contracts

- **Overhead:** Code execution involves significant computational resources due to replication across nodes.
- **Use Cases:** Automating tasks, enforcing rules and agreements without intermediaries.
- **Security:** Ensure contracts are error-free to avoid vulnerabilities.

---

### Integration and Co-Existence of Blockchain and Off-Chain Data

- **Hash Storage:** Store a hash of off-chain data on the Blockchain to maintain integrity.
  - Verify off-chain data by re-hashing and comparing with the Blockchain-stored hash.
  - Example: `SHA-256 hash` comparison ensures data has not been tampered with.
- **Efficiency:** Use data structures like Merkle Trees for handling large datasets:
  - Store aggregated hashes rather than individual hashes for better efficiency.

#### Merkle Trees

- **Definition:** Hierarchical hash structure.
- **Efficiency:** Reduces the number of hashes stored on-chain.
- **Integrity:** Any change in data reflects in the Merkle root.

---

### Nodes in Blockchain Network

#### Full Nodes

- **Characteristics:** Maintain the complete Blockchain history.
- **Role:** Actively validate and relay transactions.

#### Light Nodes

- **Characteristics:** Maintain only a subset of the Blockchain.
- **Role:** Rely on full nodes for transaction validation and historical data.

### Data Availability and Concurrency
- Nodes ensure multiple copies of data exist, enhancing availability and fault tolerance.
- Distributed nature allows concurrent access, but involves trade-offs with latency and throughput.

### Costs and Scalability

- **Blockchain:** High costs due to replication and consensus mechanisms.
- **P2P Data Stores:** Cost-effective with higher performance compared to Blockchain but might lack extreme scalability features of cloud solutions.

---

> Summary of chunk 10:
> Summary start from 'deterministic. That's again something very important. Because remember, these contracts again have t' 
that an oracle provides data from real-world sources to the Blockchain in a secure manner.
  - **Oracles:** Act as intermediaries to fetch and verify off-chain data before it's submitted to the Blockchain.
  - **Trust:** Ensuring that the oracle itself is trustworthy and not compromised is crucial.

### Key Limitations and Considerations in Smart Contracts

#### Determinism
- **Consistency:** Smart contracts must produce the same output given the same inputs and state.
- **Restrictions:** Indeterministic operations like floating points and random numbers are not allowed.
  - Floating-point operations can result in slightly different values across different systems.
  - Random number generation cannot guarantee the same sequence across nodes.

#### Performance
- **Slower Execution:** Blockchain execution is inherently slower due to replication and consensus requirements.
- **Gas Limits:** Ethereum imposes gas limits on transactions and blocks to prevent denial of service attacks.
- **Overhead:** High computational and storage costs due to distributed nature.

### Smart Contract Development Decisions

- **On-Chain vs Off-Chain Data:** 
  - Pure on-chain data usage is simpler but limits the range of applications.
  - Off-chain data requires fetching and potentially processing it outside the Blockchain, often through oracles.
- **Efficiency Trade-offs:** Deciding what computations to perform on-chain vs off-chain based on specific requirements.

### Bitcoin Scripting Language

- **Capabilities:** Limited scripting abilities.
- **Scripts:** 
  - **Locking Script:** Specifies conditions for spending a transaction output.
  - **Unlocking Script:** Provides proof (e.g., signature) to unlock a transaction.
- **Operations:** Basic operations like checking hashes and validating signatures.
  - E.g., paying Bitcoins to a public key and checking the signature against the hash.

### Advanced Smart Contract Platforms

- **Ethereum:** Provides a robust and flexible environment with the Solidity programming language.
  - **Types:** Fully Turing complete, allowing sophisticated logic.
  - **Limits:** Imposed gas limits and memory constraints for stability.
- **Other Platforms:**
  - **Hyperledger Fabric:** Uses languages like JavaScript.
  - **Corda:** Utilizes Java.
- **Security:** Avoid indeterministic or extremely complex operations to maintain network performance and security.

### Off-Chain Computation
- **Oracles:** Used to fetch and verify data from off-chain sources.
- **Integrity:** Ensuring the reliability and trustworthiness of the data provided by oracles.
- **Models:** Use models where multiple oracles provide data to increase reliability and reduce the risk of compromised data sources.

These considerations form the foundational aspects to be aware of when designing and implementing smart contracts and Blockchain applications.

> Summary of chunk 11:
> Summary start from 'you have some trusted execution environment. Right? So you might have heard of this intel SGX platfo' 
### Trusted Execution Environments (TEEs) in Off-Chain Computation
- **TEEs (e.g., Intel SGX):** Allow execution of code in a secure environment.
- **Integrity Proof:** Results from TEEs can be logged on the Blockchain with proof of trusted execution.
- **Privacy and Trust:** Using cryptographic techniques (e.g., zero-knowledge proofs, homomorphic encryption) can enhance privacy and integrity in off-chain computations.

### Communication in Blockchain
- **Broadcasting Transactions:**
  - Transactions are broadcast to the entire network and logged on the ledger.
  - Transparency: Anyone can view transactions and state information.
  - Proxy for Communication: Transactions can signal other entities for further actions.
  
- **Supply Chain Example:**
  - Logging raw material creation and transfer on Blockchain to trigger subsequent actions.
  - **Orphaned Block Risk:** Be cautious of transactions ending in orphaned blocks and potential impact on business processes.

- **Ethereum Log Events:**
  - Subscribing to log events to initiate actions based on specific events.
  - Flexibility to implement sophisticated mechanisms.

### Oracles
- **Role of Oracles:**
  - Facilitate interaction between Blockchain and external data/entities.
  - Trust: Ensure reliability of oracles, despite having decentralized oracles.

- **Operation of Oracles:**
  - **Transaction Interface:** Some Blockchains allow oracles to interact only through transactions.
  - **Delays:** Account for delays due to off-chain computations and data fetching.

### Asset Management on Blockchain
- **Cryptocurrencies:** Manage access and ownership using Blockchain.
- **Virtual Assets:**
  - **ERC-20:** For creating fungible tokens.
  - **ERC-721:** For creating non-fungible tokens (NFTs).

### Final Thoughts
Understanding these components and the nuanced interactions between on-chain and off-chain data, as well as the importance of secure computation and communication, is essential in Blockchain applications and smart contract development.

> Summary of chunk 12:
> Summary start from 'hype around NFTS in the recent past, . So it gives you a good platform to manage, these assets, you ' 
parties involved, ensuring everything is consistent and transparent. The final aspect, integration with external systems, like oracles, can be brought in to verify external data, such as land boundaries from a government database.

### Complex Asset Control
- **Multi-signature Transactions:**
  - Require multiple signatures to authorize a transaction.
  - M-out-of-N model: Specify the required number of signatures (M) out of total (N) signatories.
  - Escrow Example: Controlled asset management via smart contracts until conditions are met (e.g., payment conditions).
  - Off-chain Key Management: Keys and signatures managed off-chain, enhancing security.

- **Atomic Swaps:**
  - Enable the exchange of two assets in a single transaction.
  - All-or-nothing principle: Either both assets are exchanged, or none are.

- **Cardano:**
  - Native Tokens: Issue tokens via built-in protocol operations.
  - Flexible Asset Management: Integrated into the blockchain protocol.

### Multi-party Computation
- **Fireblocks Example:**
  - Split key into multiple parts across different parties.
  - M-of-N keys required to generate the final key.
  - Enhanced security and flexibility: Manage keys and signatures off-chain.

### Colored Coins
- **Concept:**
  - Proposed by Vitalik Buterin before Ethereum.
  - Use Bitcoin to represent real-world assets (not currency).
  - Limited data capacity: Only a few bytes (~40 bytes) per transaction script.
  
- **Applications:**
  - Transfer and manage assets digitally.
  - Represent 100 assets with specific bytes assigned to Bitcoin address.
  - Coloured Coins: Label coins to distinguish them from standard Bitcoin.

### Real-world Example: Land Registry
- **Digital Representation:**
  - Use blockchain to manage land ownership.
  - Record and verify ownership: Store ownership records on-chain, approve transfers through smart contracts.
  
- **Processes:**
  - Ownership transfer: Encode transfer conditions in contracts.
  - Payment with Cryptocurrency: Use cryptocurrency for land sale transactions.
  
- **Full Utilization:**
  - All blockchain aspects: Data storage, computation via smart contracts, transaction communication, and integration with external systems (oracles).

### Practical Application
- Integrating Blockchain for both cryptocurrency aspects and asset management allows for complex applications.
- Ensures security, transparency, and efficiency in managing digital and real-world assets.

> Summary of chunk 13:
> Summary start from 'entities, . And the fact that you are creating tokens that allow you to manage? Uh, this, piece of l' 
### Real-world Example: Land Registry (continued)
- **Tokens for Asset Management:**
  - Use tokens to manage land pieces.
  - Represent physical assets with tokens.
  - Use native tokens as Cryptocurrency.
  - Demonstrate all four blockchain aspects: data storage, computation via smart contracts, transaction communication, and integration with oracles.

### Cap Theorem Application in Blockchain
- **Consistency, Availability, Partition Tolerance (CAP):**
  - **Consistency:**
    - High, due to consensus algorithms.
    - All nodes verify transactions ensuring uniform ledger state.
  - **Availability:**
    - High availability achieved through multiple nodes storing data.
  - **Partition Tolerance:**
    - Possible issues if the network partitions; however, designed to handle network splits.
    
### Storage and Database Systems
- **P2P Storage:**
  - **Storj:**
    - Decentralized storage ecosystem.
    - Users can store data and volunteer to host data.
    - Monetary incentives for hosting nodes.
    - P2P storage provides redundancy and prevents data loss.
    - Different from centralized cloud storage as multiple nodes store data.

### Next Week's Topic
- **Blockchain Taxonomy and DApps:**
  - Deep dive into decentralized applications (DApps).
  - Understanding Blockchain taxonomy.

Reminder to form groups and think about project topics. Consider interesting and innovative areas beyond provided examples.


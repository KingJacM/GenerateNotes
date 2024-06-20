Summary of chunk 1:
Summary start from 'SPEAKER 0 OK, I think I better say hello to you first. So my name is Helen. , I couldn't be here las' 
### Lecturers and Schedule Adjustments
- Helen introduces herself.
- Dylan filled in last week.
- From now on, Helen and Professor Salil will deliver lectures.
- Dylan may appear occasionally.
- Dylan’s Monday lecture on smart contract testing incomplete.
- Remaining content to be released as a video this week.
- Next Monday is a public holiday; pre-recorded guest lecture video will be released.

### Today's Topic: Basics of Software Architecture
- Relevant for understanding Blockchain applications in a software architecture context.
- Introduction to the design aspect of software architecture.
- Importance of understanding how Blockchain fits as a component in larger systems.
  
### Software Design Process
- Focus on designing a system from a software architecture point of view.
- Involves thinking beyond single-system views or simple modules.
- Views system architecture as a high-level overview of how different parts work together.

### Key Components
- **Goals and System Scope**:
  - Starting point: Define goals and type of system.
  - Set of goals informs the design process.
- **Requirements**:
  - Functional: What the system should do.
- **Architectural Constraints**:
  - Non-functional requirements (e.g., performance, security, cloud restrictions).
- **Creative Ideas**:
  - Additional features or innovative aspects to include.

### Output of Design Process
- **Architecture Model**:
  - Usually represented through diagrams.
  - Contains boxes, arrows, and annotations explaining the design.
  - May include assumptions and comments.
  
### Example: Designing a House
- Similar to planning the layout of a house.
- Considerations might include number of bedrooms, placement of bathrooms, etc.
- Software design considerations include goals, requirements, and constraints, translating to architecture documentation.

Summary of chunk 2:
Summary start from 'More designing documents. So you will produce those artefacts as part of your design process. And th' 
### Design Process in Software Architecture
- **Production of Design Artifacts**:
  - Multiple designs and alternative designs are produced.
  - Evaluation criteria used to choose the best design.
  - Process involves back-and-forth refinement before finalizing.
  - Paper-based exercises to refine ideas are cost-effective.
  
- **Role of Blockchain in Architectural Solutions**:
  - **Database**:
    - Acts as a data store with unique properties (e.g., immutability, transparency).
    - Not just a relational DB; offers special physical and logical characteristics.
  - **Computational Platform**:
    - Executes smart contracts.
    - Provides verifiable computational operations.
  - **Communication Mechanism**:
    - Facilitates shared data writing/reading.
    - Acts as a common message exchange platform.
  - **Asset Management & Access Control**:
    - Manages asset access through logic, often powered by smart contracts.
  
- **Typical Architecture Diagram**:
  - Layers:
    - Top Layer: Applications communicating via APIs.
    - Backend: Blockchain layer, off-chain data sources, ledger, token management, smart contracts.
  - Blockchain is a component in a larger system.
  - Decision on Blockchain’s role based on system requirements.

### Impact of Architectural Decisions 
- **Trade-offs in Design**:
  - Performance, availability, and security may vary.
  - Architectural decisions influence system performance and privacy protection.
  - You can't optimize for all aspects due to inherent trade-offs (CAP theorem).
  - The CAP theorem states you can only achieve two out of three: Consistency, Availability, and Partition Tolerance.

### Example of Architectural Layers Involving Blockchain:
1. **Application Layer**:
    - User-facing applications or services.
    - Interacts with backend through APIs.
  
2. **Blockchain Layer**:
    - **Ledger Component**:
        - Stores transactional data with immutability.
    - **Smart Contracts**:
        - Define and execute business logic.
    - **Token Management**:
        - Manages tokens and digital assets.
    - **Off-Chain Data Sources**:
        - For extensive data that doesn’t fit on-chain storage limitations.

### Importance of Preliminary Design Process
- Implementation is costly.
- Detailed design and evaluation avoid expensive mistakes.
- Refined ideas through documentation and analysis before commitment.

### Key Takeaway
- Blockchain’s role in a system must be clearly defined.
- Architectural choices influence the entire system's performance and properties.
- Understanding trade-offs is crucial for effective software design.

Summary of chunk 3:
Summary start from 'or something That is kind of, contradictory, . Like transparency and privacy, you might say, using B' 
evaluate and choose the best one? You might look at the cost, reliability, and speed of service. So these are nonfunctional aspects but very critical in determining the best service for your needs.

### Importance of Functional and Nonfunctional Requirements
- Functional requirements: Define what the system should do, specify relationship between input, output, and internal states.
  - Example: Describing debit transactions in technical terms.
- Nonfunctional requirements: Describe how the system should behave in ways apart from functionality.
  - Example: Performance metrics such as processing 250 transactions per second.
  - Include usability, reliability, modifiability, availability, confidentiality, etc.
  
### Software Quality Properties
- **Usability**: How user-friendly the software is.
- **Reliability**: Includes availability, recoverability, maturity, fault tolerance.
- **Modifiability**: How easy it is to change.
- **Availability**: Uptime of the software.
- **Confidentiality**: Protection of data.
- **Performance**: Speed and efficiency, such as transaction rates.
- **Compatibility**: Ability to work with different systems.

### Importance of Describing Nonfunctional Properties
- Offers a complete picture of system performance beyond just the functional aspects.
- Companies often adhere to international standards for software quality.
- Nonfunctional properties also help compare services where functional attributes are identical.

### Metrics and Standards
- International standards define many software quality properties.
- Companies pursue standards to ensure high-quality software and obtain certification.
- Measurement criteria under each quality property.

### Example of Reliability
- **Availability**: Percentage uptime of the system.
- **Recoverability**: How quickly the system recovers from failure.
- **Maturity**: Stability over time.
- **Fault tolerance**: System's ability to operate without failure.

### Relevance to Blockchain
- Focus on nonfunctional properties like performance, security in Blockchain systems.
- Analyze how Blockchain meets these criteria and trade-offs involved.

Understanding these elements and their importance helps design robust systems and make informed architectural decisions. The role of preliminary design and clear documentation in preventing costly mistakes cannot be overstated.

Summary of chunk 4:
Summary start from 'choose which plumber, . The same in software you probably have a look at in terms besides the. Besid' 
### Nonfunctional Properties
- **User Experience**: Functionality isn't enough; consider user interaction aspects.
- **Regulatory Requirements**: Privacy, anti-money laundering, digital currency regulations are key.
  - These are nonfunctional requirements but crucial for system compliance.
- **Trade-offs**: Balancing multiple nonfunctional properties such as security vs. performance
  - Use tools like spider diagrams to evaluate design against these properties.

### Group Project Introduction
- **Release of Specification Pending**: Project details to be shared after the lecture.
- **Project Scope**:
  - From design to implementation.
  - Start with documenting the architecture and requirements.
  - Create your own project idea, no predefined requirements.
  
### Documenting Requirements
- **Importance**:
  - Specific, detailed, complete, clear, and concise requirements.
- **Incorporate Assumptions**:
  - Define operational environments, e.g., which resources are available.
- **Functional vs. Nonfunctional Requirements**:
  - Functional: Clearly defined actions like user permission requests.
  - Nonfunctional: Qualities like confidentiality, defined with context-specific clarity.

### Basic Terminology in Software Architecture
- **Components**: Fundamental units of software architecture.
  - Can be large units like web servers or databases.
  - Functional units performing specific roles.
- **Connectors**: Links between components, necessary for communication.
  - Display how components interact (e.g., load balancer to web server).
  - Usually organized in layers (e.g., web layer, application layer, data layer).

### Blueprint View of Software Architecture
- **Layered Model**:
  - Web Layer: Handles HTTP requests and responses.
  - Application Layer: Implements core business logic.
  - Data Layer: Manages data persistence and retrieval.
- **Component Interaction**: Visual depiction of how each component communicates.
  - E.g., Load balancer directs traffic to the web servers which then interact with application servers and databases.

```plaintext
+----------------+        +--------------+        +--------+
|  Load Balancer |------> |  Web Server  |------> |Database|
+----------------+        +--------------+        +--------+
                                   |
                         +---------V---------+
                         | Application Server|
                         +-------------------+
```

### Importance of Architecture Design
- **Overarching View**: Comprehensive system understanding.
- **Communication**: Essential for the seamless operation within the system.
- **Scalability and Maintenance**: Helps in future scaling and system maintenance planning.

Effectively, having a robust design and clear documentation can significantly impact the success and efficiency of software systems, particularly in blockchain applications where regulatory and performance aspects are pivotal.

Summary of chunk 5:
Summary start from 'what's in it, how they're connected. And how they're placed. Yeah, to to work as a as a single syste' 
useful to follow. These patterns are essentially templates that have been proven to work well in certain situations.

### Key Concepts in Blockchain Architecture Design

- **Components and Connections**: 
   - Components: Different modules or parts of the system.
   - Connections: How they interact with each other.
   - Placement: Deployment in physical hardware/environment.

- **Load Balancers**: 
   - Elastic load balancers for auto-scaling, ensuring high availability and scalability.
   - Redundancy with multiple application servers and web servers.

- **Configuration**:
   - Topology setup: Structure and placement of components.
   - Not just system configuration (like typing port numbers) but rather the overall structure.

- **Design Focus**:
   - The intention behind the design (e.g., scalability, availability).

### Abstraction in Architecture Design

- **Abstraction**:
   - Simplifies complexity to enhance communication.
   - Facilitates discussions with non-technical stakeholders.
   - Model the problem at a high level.
   - Different models serve different purposes based on design goals.

### Non-functional Properties

- **Design Choices**:
   - Impact functional and non-functional properties.
   - Multiple design options can achieve various trade-offs.

- **Examples of Database Designs**:
   - Single Database System:
     - Simple to build and maintain.
     - Higher risk: single point of failure.
   - Distributed System with Multiple Databases:
     - Higher availability and scalability.
     - Challenges: synchronization, complexity.
   - Blockchain-Based Storage:
     - Excellent availability.
     - Scalability remains an issue with current technology.

### Design Patterns

- **Utility of Design Patterns**:
   - Templates for common problems, proven to work.
   - Example: Patterns from object-oriented programming.
   - Using patterns can provide confidence in the robustness and elegance of the design.

- **Advantages**:
   - Avoid starting from scratch.
   - Leverage industry best practices.
   - Potential for innovative solutions, yet validated by common use.

### Workflow for Creating Architecture

1. **Initial Design**:
   - Develop from scratch, evaluate different architectural choices.
   - Understand the problem domain and non-functional requirements.
   
2. **Pattern Utilization**:
   - Adopt established patterns for robustness and reliability.
   - Mix initial designs with recognized patterns to innovate.

3. **Iterative Improvement**:
   - Revise based on functional requirements and performance issues.
   - Optimize for scalability, availability, and specific non-functional requirements.

### Practical Example

- **Three-Layer System with Backend**:
   - Presentation Layer.
   - Application Layer.
   - Database Layer options:
     - Single database (simple but risky).
     - Multiple databases (complex but scalable).
     - Blockchain (high availability but limited scalability).

By melding these architectural principles with design patterns, developers can craft a robust and adaptable blockchain system capable of meeting varied requirements and challenges.

### Next Steps

- **Upcoming Coverage**:
   - In future classes, design patterns will be explored.
   - Application of these patterns in real-world scenarios.

Summary of chunk 6:
Summary start from 'available as a generic solution to lots of problems. So one of the sort of strategy is that identify' 
you have experience with UML? OK, so UML, we use it for these kind of diagrams like logical view and process view.

### Understanding Architectural Styles vs Patterns

- **Architectural Style**:
  - Set of principles and guidelines.
  - Example: Web or Client-Server Architecture.
  - Gives unique identity to the design.
  - Similar to recognizing a famous architect’s work by style.

- **Architectural Pattern**:
  - Specific solutions to common problems.
  - Not unique to any one style—can be applied broadly.
  - Example: 3-tier design or MVC (Model-View-Controller).
  - More practical in solving specific issues within the architecture.

### Understanding Views and Viewpoints

- **Views**: Different perspectives to describe and understand the system.
  - Similar to different anatomical views like skeleton, circulatory system, and muscles in human anatomy.

- **Viewpoints**: Used to generate design based on a particular perspective.

### Four Plus One View Model

1. **Logical View**:
   - Components and their relationships.
   - Represented using class diagrams in UML.
   
2. **Process View**:
   - Dynamic behavior of the system.
   - Focuses on flow and control.
   - Often represented with state diagrams or flow charts.

3. **Physical View**:
   - Describes the deployment of components in the physical environment.
   - Focus on how components are mapped onto hardware.

4. **Development View**:
   - More concrete view of logical view.
   - Software components depicted in a programmer-friendly manner.
   
5. **Use Case View**:
   - Scenarios describing how the design works.
   - Interaction between stakeholders and the system.

### UML (Unified Modeling Language)

- **Usage**:
  - Designing and documenting different views.
  - Important diagrams include:
    - *Class Diagrams*: For logical view.
    - *State Diagrams/Flow Charts*: For process view.
    - *Deployment Diagrams*: For physical view.

### Practical Takeaways

- Patterns are applied to solve particular problems.
- Styles provide a broader guideline.
- Understanding and applying the correct viewpoint is crucial for generating an effective design.
- Utilize UML for visual representation of different views.

Continuing on this path, you’ll gain insights into how to utilize architectural styles and patterns more efficiently in your projects. This approach will be discussed in more depth in the following weeks.

Summary of chunk 7:
Summary start from 'you actually know UML done UML A lot of software engineering students were not that many. what sort ' 
---
### UML Overview

- UML (Unified Modeling Language) is used for modeling, similar to EL (Entity-Relationship) diagrams for databases.
- UML offers diverse notations such as state charts, class diagrams, and use case diagrams.
- State charts describe the work and flow of the system with standardized notation.
- Class diagrams and use case diagrams give different perspectives on system design.
- UML standardizes the way different views and ideas about a system are represented.
- Quick tutorial on UML might be provided later, useful for project modeling.

#### Break Announcement

---

### Software Architecture Elements

#### Basic Terminology

- **Software Architecture Design**:
  - Components: Larger scope in design, fundamental building blocks.
  - Connectors: Links that integrate components.
  - Configuration/Topology: Structure and placement of components and connectors.

- **Software Components**:
  - Architectural entities encapsulating subsets of system functionality.
  - Abstract examples: Web server component, database component.
  - Access is restricted through defined interfaces.
  - Components interact through their interfaces.
  
    ```python
    # Example Interface in Python
    class DatabaseComponent:
        def connect(self):
            pass
        
        def execute_query(self, query):
            pass
    ```

  - Must have a clear execution context (e.g., location of database/server).
  - Components should be modular, self-contained, and reusable.
  - Provide application-specific services (contextualized services like banking database services).

- **Connectors**:
  - Enable integration and communication between components to form a whole system.
  - Serve as 'glue' to ensure functional unit operations.
  - Examples: 
    - File transfer (FTP)
    - Streaming protocols
    - Remote procedure calls (RPC)
    - Shared databases
    - Message buses like Message Queues

    ```python
    # Example of a simple connector - RPC in Python
    import xmlrpc.client

    server = xmlrpc.client.ServerProxy("http://localhost:8000/")
    result = server.example_method("param")
    ```

#### Application in Blockchain

- **Blockchain as a Component**:
  - Provides application-specific services.
  - Plays a role in software architecture depending on its context.

- **Blockchain as a Connector**:
  - Facilitates secure and decentralized communication.
  - Acts as a medium for exchanging information between components.
  
---

### Next Steps

- Deeper exploration of Blockchain's role in architectural design.
- Specific connecting facilities Blockchain can provide, covered in later topics.

---

Summary of chunk 8:
Summary start from 'components right in the system. Like storage component or what was it computational component, thing' 
be included when you're trying to describe your design. 

### Design Considerations in Blockchain Architecture

- **Configuration**:
  - Represents the state structure.
  - Arranges components and connectors.
  - Examples of configurations:
    - **Simple Linear Configuration**:
      - Browser -> Application Server -> Database.
    - **Scaled-Up Configuration**:
      - Browser -> Load Balancer -> Multiple Application Servers -> Multiple Databases.
  - Each configuration has pros and cons:
    - Simple configuration has lower operating costs but higher risk of single points of failure.
    - Scaled-up configuration enhances performance and availability but is more complex and costly to maintain.

- **Fault Tolerance and High Availability**:
  - Geographical distribution (e.g., different regions for application servers and databases) for fault tolerance.
  - Increased redundancy and load balancing to ensure high availability.

### Exercise Example: Lunch Application Architecture on Ethereum

- **Components**:
  - Smartphone
  - Ethereum
  - MetaMask
  - Smart Contracts

- **Design Approach**:
  - Basic Configuration:
    - Remix (browser-based IDE) -> MetaMask -> Ethereum.
  - Alternative Configuration:
    - Mobile App -> MetaMask -> Ethereum.

- **Expressing Mobile App Context**:
  - Replace browser-based interface with a mobile app.
  - Ensure all interactions previously done through the browser are now handled by the app.

### Problem Solving in Design Exercises

- Multiple ways to design:
  - Each design has its pros and cons.
  - No absolute right or wrong; some solutions may be more suitable depending on context.

### Tips for Project Presentations

- Present clear architectural designs.
- Highlight important components and connectors.
- Explain design choices, pros, and cons.
- Practice drawing architecture diagrams to effectively communicate design ideas.

### Tools and Concepts

- **MetaMask**:
  - Component for interacting with Ethereum blockchain.
- **Remix**:
  - Browser-based development environment for smart contracts.
- **Load Balancer**:
  - Distributes requests among multiple servers to optimize resource use and ensure reliability.

### Final Thoughts

- Explicitly discuss and draw your architecture.
- Clear, well-thought-out designs lead to better implementation and understanding.

---

The session continues with specific exercises and drawing architecture diagrams, helping you better understand blockchain architecture and its practical applications.

Summary of chunk 9:
Summary start from 'a box represent? What should an arrow represent? What does a stacking one box over the other actuall' 
process the photo and create an NFT. Yeah. And on the other side, you have a very similar process, mobile phone uploads the photo, it's stored somewhere as well, but then it uses a different sort of, um, process to mint an NFT using the smart contract here. Yeah, so that's that's one difference. Anyway, so go through this analysis thinking about integrity, availability and cost, ticking the boxes. So here's a list of questions that we want to go through to compare these two options. So things like how would a blockchain fit in here? Why should you even use blockchain technology? How does each component contribute to the integrity of the system? How does each component impact the availability of the system, and what does it cost to run each of these options? Consider these points.

### Architectural Stack and Design

- **Layered Architecture**: 
  - Bottom layer: Database/backend.
  - Middle layer: Service interfacing with the database.
  - Top layer: Interface/browsers interacting with services.

- **Importance of Stacking**: 
  - Conveys a structured flow and clear dependencies between layers.
  - Example: Database -> Service -> User interface.

### Modelling and Analysis

- **Purpose**:
  - Provides a clear, abstract representation to evaluate system properties.
  - Helps predict performance metrics like transaction latency without full implementation.

- **Designing Your Architecture**:
  - Models enable you to scrutinize aspects such as availability, fault-tolerance, and scalability.
  - Allows you to identify bottlenecks and other potential issues before they arise.

- **Trade-offs**:
  - Balance different system qualities (performance, cost, availability).
  - Example: Larger servers improve performance but increase cost.
  - Redundant servers offer better availability but might lead to higher latency or cost.

### Comparing Design Options

- **Data Storage**:
  - Options: On-chain vs. off-chain, Private Cloud, Peer-to-Peer systems.
  - Embed data within Bitcoin transaction or a smart contract.

- **Criteria for Comparison**:
  - **Integrity**: Ensuring data correctness and authenticity.
  - **Availability**: System uptime and responsiveness.
  - **Cost**: Operational and infrastructure costs.

- **Analysis Example**:
  - **Design Option A**:
    - Mobile user uploads photo to storage.
    - Service within storage mints NFT.
  - **Design Option B**:
    - Mobile user uploads photo.
    - Different process minting NFT via smart contract.

- **Evaluation Questions**:
  - How does blockchain technology fit into each design?
  - Contribution of each component to system integrity and availability?
  - Cost analysis for running each option?

### Exercises and Evaluation Practice

- **Exercise Setup**:
  - Go through the example systems, apply comparative analysis.
  - Evaluate integrity, availability, cost for each option.
  - Make informed decisions based on analysis, focusing on architecture's strengths and weaknesses.

---

The lecture will involve further hands-on practice with these concepts, ensuring a deeper understanding of blockchain architecture and its application in various scenarios.

Summary of chunk 10:
Summary start from 'generate hash of the photo and put it on Blockchain. Right. So that generates an FT. And the idea is' 
### Lecture on Blockchain

#### NFT Creation and Ownership

- **NFT Creation**:
  - Generate hash of the photo and put it on Blockchain to create an NFT.
  - Ownership proof using well-known cryptographic solutions.
  - Process:
    - Take a photo 
    - Upload it
    - Hash generated
    - Hash put on Blockchain
    - NFT created and ID associated with the owner

#### Interaction with Storage and Blockchain

- **User Interactions**:
  - User uploads photo: interacts with storage and Blockchain.
  - Web component (browser) abstracts these interactions.
  - User-friendly: one interface for user interaction.
    - For the system: increases complexity to provide ease of use.
  - Trade-off between user simplicity and system complexity.

#### Comparison of Design Options

- **Integrity**:
  - Similar in both systems due to Blockchain usage.
  - Blockchain ensures photo integrity via hashing.
  - Possible detection of tampering due to hash comparison.
  
- **Availability**:
  - Direct Blockchain interaction may have higher availability.
  - Potential issues if storage is not available even if Blockchain is.
  
- **Cost**:
  - Depends on perspective (user vs system).
  - **User Cost**:
    - Could be higher due to additional services provided.
    - Minimal cost for direct underlying Blockchain access.
  - **Blockchain Transaction Cost**:
    - Two transactions: upload to storage, hash to Blockchain.
    - One transaction in direct method.
  - Importance of making assumptions clear when analyzing cost and integrity.
  
#### Design Exercise Insights

- **Design Methodology**:
  - Emphasis on understanding and justifying design choices.
  - Systems comparisons using common terminology.
  - Formal methodologies could be applied for thorough analysis (not explored here).
  
#### Project and Group Work

- **Project 2 Details**:
  - Group-based project focusing on design discussions and choices.
  - Importance of group collaboration for effective design and decision-making.
  
- **Group Registration**:
  - Default group type, up to 5 members per group.
  - Option to create/join groups in the system (CM S3).
  - Group wiki page for design entries and feedback.
  
- **Upcoming Instructions**:
  - Instructions for managing group activities and project tasks.
  - Released alongside Project 2.

### End of Lecture

Summary of chunk 11:
Summary start from 'OK. All right. It's nice to see I'm sorry that I missed the big one, but we back so all will be OK a' 
### Blockchain Lecture Notes

#### **Basic Concepts**

- **Definition of Blockchain**:
  - A decentralized ledger that records all transactions across a network of computers.
  - Transactions are grouped into blocks and linked chronologically.
  
- **Key Features**:
  - **Decentralization**: No central authority; data distributed across nodes.
  - **Transparency**: Transactions visible to participants.
  - **Immutability**: Once recorded, data cannot be altered.

#### **Components of Blockchain**

- **Blocks**:
  - Each block contains a batch of transactions.
  - Includes a unique identifier called a hash.
  - Contains the hash of the previous block, forming a chain.

- **Nodes**:
  - Computers that participate in the blockchain network.
  - Verify and record transactions.
  - Maintain a copy of the blockchain.

- **Smart Contracts**:
  - Self-executing contracts with terms directly written into code.
  - Execute automatically when conditions are met.

#### **Consensus Mechanisms**

- **Proof of Work (PoW)**:
  - Miners solve complex mathematical problems to add new blocks.
  - Energy-intensive and slow.

- **Proof of Stake (PoS)**:
  - Participants lock up a certain amount of cryptocurrency as a stake.
  - Validators are chosen to add new blocks based on their stake.
  - More energy-efficient than PoW.

#### **Applications of Blockchain**

- **Cryptocurrencies**:
  - Bitcoin, Ethereum, etc.
  - Digital currencies that use blockchain for transactions.

- **Supply Chain Management**:
  - Tracking products from origin to destination.
  - Increased transparency and traceability.

- **Digital Identity**:
  - Secure and verifiable digital identities.
  - Reduces risk of identity theft.

- **Voting Systems**:
  - Secure and transparent voting.
  - Ensures election integrity.

#### **Challenges and Limitations**

- **Scalability**:
  - Current blockchains struggle with high transaction volumes.
  - Solutions like sharding and layer-2 protocols are being developed.

- **Energy Consumption**:
  - PoW consumes significant energy.
  - Transition to PoS in some networks to mitigate this issue.

- **Regulation**:
  - Legal and regulatory frameworks are still evolving.
  - Need for clear guidelines and policies.

#### **Future Trends**

- **Interoperability**:
  - Developing protocols to allow different blockchains to communicate.
  - Enhances the utility and functionality of blockchain networks.

- **Decentralized Finance (DeFi)**:
  - Financial services on blockchain without intermediaries.
  - Includes lending, borrowing, and trading platforms.

- **Non-Fungible Tokens (NFTs)**:
  - Unique digital assets verified using blockchain.
  - Applications in art, gaming, and collectibles.

### Data Integrity and Security

- **Cryptographic Techniques**:
  - Public and private keys for transaction authentication.
  - Hash functions to secure data.

- **Distributed Consensus**:
  - Ensures all nodes agree on the blockchain state.
  - Reduces the risk of malicious attacks.

- **Sybil Attacks**:
  - Attackers create multiple fake identities.
  - Prevented by requiring resources (PoW, PoS) for participation.

---

Next lecture will cover slides from 36 to 39 for deeper understanding.

### Group Collaboration Tips

- Use group wiki page effectively for design entries and feedback.
- Communicate regularly to ensure everyone is on the same page.
- Divide tasks based on individual strengths and expertise.

---

### Miscellaneous

- Will review the quiz for any potential errors.
- Study the notes as they provide necessary details.
- Contact group members directly for project collaboration. 

### End of Notes


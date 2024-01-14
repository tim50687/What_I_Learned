# Network Architecture

**Challenges in Network Design**:
- **Comprehensive Requirements**: Designing a computer network involves meeting extensive requirements, such as:
   - **General Connectivity**: Ensuring broad and effective connectivity among numerous computers.
   - **Cost-Effectiveness**: Balancing performance with cost-efficiency.
   - **Fairness**: Providing equitable access to network resources.
   - **Robustness**: Maintaining reliable and resilient network operations.
- **Adaptability**: Networks must continuously evolve to keep pace with changes in underlying technologies and the varying demands of applications.
- **Manageability**: They should be manageable by individuals with different skill levels, ensuring ease of operation and maintenance.

**Role of Network Architectures**:
- **Blueprints for Networks**: Network architectures serve as foundational blueprints guiding the design and implementation of networks.
- **Handling Complexity**: These architectures provide structured approaches to address the complexity inherent in network design.
- **Standardization**: Network architectures help in standardizing network functions and communication protocols.

**Key Network Architectures**:
1. **OSI Model (Open Systems Interconnection)**:
   - A theoretical framework that divides network communication into seven layers, each with specific functions and responsibilities.
   - It's a conceptual model used to understand and design complex network interactions.

2. **Internet Architecture**:
   - Also known as the TCP/IP model, this architecture underpins the modern Internet.
   - It's based on a simpler structure compared to the OSI model and focuses on the practical implementation of network protocols.

## Layering 

The concept of abstraction and layering in network design is a crucial strategy for managing complexity. Let's break down these ideas for better understanding:

### Abstraction in System Design
- **Hiding Complexity**: Abstraction is about hiding the complex inner workings of a system behind a simpler interface. This makes the system easier to understand and use.
- **Example**: Consider a channel in network communication. For application developers, a channel is just a means to send and receive data. They don't need to understand the underlying complexities of how data is routed through the network, the management of network traffic, or how data integrity is maintained.

### Defining Abstraction
- **Model and Interface**: An abstraction creates a model capturing essential aspects of the system and provides an interface for interacting with this model.
- **Encapsulation**: The details of how the model works are encapsulated or hidden inside the object, separating the functionality from its implementation.

### Layering in Network Systems
- **Building on Underlying Services**: Layering in networks starts with the services offered by the hardware. Then, a sequence of layers is added, each providing a more abstract level of service.
- **Implementation of Services**: Services at higher layers are built upon the services provided by lower layers.

### Example of Layering
- **Host-to-Host Connectivity Layer**: The first layer above the hardware might provide basic connectivity between two hosts, abstracting the complexity of the network topology.
- **Process-to-Process Channels Layer**: The next layer could build upon this connectivity to provide process-to-process communication, handling issues like message loss.

### Advantages of Layering
1. **Manageable Components**: It breaks down the network design into smaller, more manageable parts. Each layer addresses a specific aspect of the network functionality.
2. **Modularity**: This approach allows for modularity in design. If a `new service` or functionality needs to be added, it might only require changes at a specific layer, without altering the entire system.

> Unfortunately, the OSI model hide information, which will lead to the performance issue.

### Conclusion
Abstraction and layering are fundamental in network design, simplifying complex systems and making them manageable and scalable. By abstracting details and layering functionalities, network systems become easier to develop, maintain, and upgrade. This approach allows network designers to focus on one layer's functionality at a time, leveraging the capabilities provided by the lower layers.

> Each layer provides different services to the layer above it but building on the same low-level services provided by the layer below it.


#### Protocols in Network Architecture

**Protocols as Foundation of Network Layers**:
- **`Definition`**: In network systems, protocols are the `abstract objects that make up the layers`. A protocol provides specific communication services used by higher-level objects (like applications or higher-level protocols) to exchange messages.

**Examples of Protocols**:
- **Request/Reply Protocol**: Facilitates a simple interaction where a request is sent, and a reply is received, akin to a question and answer.
- **Message Stream Protocol**: Supports continuous streams of messages, such as in video streaming or chat applications.

**Two Interfaces of Protocols**:

1. **Service Interface**:
   - **Purpose**: Defines how local objects on the same computer can interact with the protocol to use its communication services.
   - **Operations**: For instance, a request/reply protocol might allow applications to send requests and wait for replies. An HTTP protocol implementation might include operations to fetch web pages.
   - **User Interaction**: An application like a web browser uses these operations to perform tasks like loading new pages when a user clicks a link.

2. **Peer Interface**:
   - **Function**: Specifies the format and semantics of messages exchanged between protocol peers (counterparts on different machines).
   - **Message Structure and Meaning**: Details how messages are structured, arguments used, and how peers should respond. For example, in HTTP, how a GET request is formatted and how servers respond to it.

**Role of Protocols in Communication**:
- **Local Service Exportation**: A protocol defines how it offers communication services locally, allowing applications to interact with it.
- **Rule-Setting for Message Exchange**: It also sets the rules for exchanging messages with its peers, defining how communication is carried out over the network.

**Layered Architecture and Protocol Functionality**:
- **Layered Approach**: Each layer in a network architecture is associated with specific protocols, each building on the services provided by lower layers.
- **Modularity and Flexibility**: This structure allows for modularity in network design, where changes or upgrades can be made to specific layers without altering the entire system.

Let's break down the concept of encapsulation in network communication, as it can be a bit complex.

## Encapsulation in Network Protocols

**1. Basic Concept**:
   - **Encapsulation** is a process in networking where a message or packet gets additional data attached to it (like headers or trailers) as it passes through each layer of a network protocol stack.

**2. Example Process**:
   - Imagine an application (like an email client) sends a message.
   - **At the Application Layer (RRP in your example)**: The application gives its message to the Request/Reply Protocol (RRP). RRP treats this message as just a string of bytes, without interpreting its meaning (like whether it's an email, an image, etc.).
   - RRP then adds its own header to this message. This header contains control information necessary for the receiving RRP to process the message correctly.
   - The message with the RRP header is the new 'body' or 'payload' for the next layer.

**3. Further Encapsulation**:
   - **At the Next Layer (HHP in your example)**: This layer takes the RRP message (original message + RRP header) and adds its own header.
   - Each layer of the protocol stack adds its own header (or trailer) to the message. This header has information specific to that layer's protocol.

**4. Transmission and Receiving Process**:
   - The fully encapsulated message is transmitted over the network.
   - At the receiving end, each layer processes its respective header and removes it, passing the remaining content up to the next layer.
   - Eventually, the original message reaches the corresponding application on the receiving end, stripped of all the additional headers added during transmission.

**5. Purpose of Encapsulation**:
   - It ensures that each layer of the network can communicate control information to its counterpart on the receiving end.
   - It allows the network to handle complex operations like routing, error handling, and data integrity without the application needing to manage these details.

**6. Transformation of Data**:
   - Sometimes, lower-level protocols might compress or encrypt the entire message body, including the original application data and all attached headers. This doesn't mean they interpret the data but rather apply transformations to it.

### Conclusion

Encapsulation is a fundamental concept in network communication, crucial for the layered network architecture. It involves wrapping data with protocol-specific headers (or trailers) at each layer, enabling complex network functions to be performed transparently from the applications that initiate the communication. This process allows for modular, organized, and efficient data transmission across diverse network environments.


## Multiplexing in Packet Switching

1. **Basic Idea**: 
   - **Multiplexing** is the process of combining multiple data flows or messages into one communication channel or medium. In networking, this typically happens when various application data packets are sent over the same physical network link.

2. **Application Level**:
   - In your example with RRP (Request/Reply Protocol), multiplexing occurs when messages from different applications are combined and sent over the same logical channel at the source host.

### Demultiplexing

1. **Reversing Multiplexing**:
   - **Demultiplexing** is the process of separating these combined data flows back into their original, individual messages when they reach their destination.
   - This separation is necessary for delivering each piece of data to the correct recipient application.

2. **Role of Demultiplexing Key**:
   - In the header attached to each message by protocols like RRP, there is a specific identifier known as the "demultiplexing key" or "demux key."
   - This key is used to identify which application or higher-level protocol a particular piece of data belongs to.

### How Multiplexing and Demultiplexing Work Together

- **At the Source (Multiplexing)**:
   - When RRP prepares messages for transmission, it adds a header with a demux key specific to the destination application.
   - These messages from different applications are then sent over the network in a combined form.

- **At the Destination (Demultiplexing)**:
   - Upon arrival, the receiving RRP looks at the demux key in each message's header.
   - It uses this key to determine which application the message should be delivered to.
   - RRP then directs each message to the appropriate application based on the demux key.

### Protocol-Specific Demux Keys

- **Variation Across Protocols**:
   - Different protocols have different ways of defining their demux keys. For example, some might use 8-bit fields (allowing for 256 different identifiers), while others might use 16- or 32-bit fields for more options.
   - Some protocols might use a single demultiplexing field, while others use a pair (one for each communication direction).


## Example of Layering of Protocols on Data

### The Process of Sending an HTTP Request

#### 1. Application Layer (HTTP Request)
- **Web Browser's Role**: The browser creates an HTTP request, which is a plain text message following the HTTP protocol format, like the `GET / HTTP/1.1` request.
- **Data**: The request includes the path (`/`), HTTP version (`HTTP/1.1`), and headers like `Host` and `Connection`.

#### 2. Transport Layer (TCP)
- **OS and TCP**: The operating system takes the HTTP data and uses TCP (Transmission Control Protocol) to ensure reliable delivery. TCP handles the data integrity and order.
- **TCP Header**: The OS adds a TCP header to the HTTP data, including information like the source and destination port numbers (e.g., port 80 for HTTP).

#### 3. Network Layer (IP)
- **IP Routing**: The OS then encapsulates the TCP-HTTP data within an IP (Internet Protocol) packet, adding an IP header. This header includes the source and destination IP addresses.
- **Routing Decision**: The OS determines the next hop for the packet, which could be a local server or an external router, based on its routing table.

#### 4. Data Link Layer (Ethernet)
- **Ethernet Frame**: For communication over the LAN, the OS wraps the IP-TCP-HTTP packet in an Ethernet frame, adding an Ethernet header with MAC addresses.
- **Transmission**: The packet, now Ethernet-IP-TCP-HTTP, is sent over the network. Ethernet handles local network delivery.

#### 5. Receiving and Processing
- **Destination Device**: The receiving device (server or router) reads the Ethernet frame.
- **Layer-by-Layer Processing**: Each layer processes and strips off its respective header, passing the remaining data to the next layer up.
- **Final Delivery**: If the destination is the correct server, the HTTP request reaches the application layer (web server) after all headers are removed.

### Intermediate Routers
- **Routing Function**: If a router is an intermediate stop, it processes the Ethernet and IP headers, determines the next hop based on the IP address, and forwards the packet accordingly.
- **Protocol Flexibility**: The packet might switch from Ethernet to another protocol if it leaves the LAN (e.g., over fiber optic lines).

### Layered Network Model
- **Abstraction and Independence**: Each layer operates independently and handles specific tasks: Ethernet for local delivery, IP for routing, TCP for reliable transmission, and HTTP for application-level communication.
- **Encapsulation**: Each layer adds its own header to the data from the higher layer. This nesting ensures that each layer's protocols and operations are contained and managed distinctly.


## Conceptualize the layered model of network communication

### 1. Application Layer
- **Intent**: The application (e.g., a web browser) wants to send or receive data (like an HTTP request).
- **Action**: It prepares the data in a format understandable at the application level (following HTTP protocol, for instance) and hands it off to the transport layer.
- **Perspective**: "I've formatted this data according to my protocol. Transport layer, it's your turn to handle it."

### 2. Transport Layer
- **Intent**: Needs to transport the application's data reliably to the correct process on the destination machine.
- **Action**: Adds a transport layer header (like TCP), which includes information for managing this transport (like port numbers, sequence numbers for ordering, etc.).
- **Perspective**: "I've ensured this data will reach the right process reliably. Network layer, please route this to the right machine."

### 3. Network Layer
- **Intent**: Responsible for routing the packet to the destination machine across networks.
- **Action**: Adds a network layer header (like IP), containing source and destination IP addresses and other routing information.
- **Perspective**: "I've determined how to route this packet. Data link layer, please deliver this to the next node."

### 4. Data Link Layer
- **Intent**: Handles the local transmission of data (like on a LAN).
- **Action**: Adds a data link layer header (like Ethernet), which includes MAC addresses and other local network information.
- **Perspective**: "I'll handle the local delivery of this packet. Physical layer, please transmit these bits over the hardware."


## The 7-Layer Model


### Physical Layer

- **Service**: Transmits raw bits over a physical link between two systems.
- **Interface**: Defines how a single bit is sent across the physical medium.
- **Protocol**: Specifies the encoding scheme for a bit, including voltage levels, signal timing, etc.
- **Examples**: Coaxial cable, fiber optics, radio frequency transmitters.

### Data Link Layer

- **Service**: Manages data framing (defining packet boundaries), Media Access Control (MAC), and provides per-hop reliability and flow control.
- **Interface**: Handles the transmission of packets between two hosts on the same medium.
- **Protocol**: Involves physical addressing (like MAC addresses).
- **Examples**: Ethernet, WiFi, DOCSIS (Data Over Cable Service Interface Specification).

### Network Layer

- **Service**: Responsible for delivering packets across the entire network, handling tasks like fragmentation/reassembly, packet scheduling, and buffer management.
- **Interface**: Facilitates sending a packet to a specific, globally-defined destination.
- **Protocol**: Involves global addressing schemes (like IP addresses) and maintaining routing tables.
- **Examples**: Internet Protocol (IP), IPv6.

### Transport Layer

- **Service**: Offers services like multiplexing/demultiplexing of data streams, congestion control, and ensures reliable, in-order delivery of messages.
- **Interface**: Allows sending of a complete message to a destination.
- **Protocol**: Includes the use of port numbers, mechanisms for reliability and error correction, and flow control.
- **Examples**: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).

### Session Layer

- **Service**: Manages access and synchronization of data.
- **Interface**: Varies depending on the implementation.
- **Protocol**: Includes token management and insertion of checkpoints.
- **Examples**: Not typically used in modern networking, more abstract.

### Presentation Layer

- **Service**: Converts data between different formats and representations, such as from big endian to little endian, or ASCII to Unicode.
- **Interface**: Varies depending on the implementation.
- **Protocol**: Defines data formats and transformation rules.
- **Examples**: Again, more abstract and not typically used in modern networking.

### Application Layer

- **Service**: Provides a wide range of services depending on the application's requirements. This layer encompasses the high-level applications we interact with.
- **Interface and Protocol**: Both are highly variable and depend on the specific application. This layer follows the protocols and interfaces defined by the application itself.
- **Examples**: Any high-level applications like web browsers, email clients, and mobile apps.

### Conclusion

Each layer of the OSI model has specific roles, protocols, and interfaces. The lower layers (Physical, Data Link, Network) are more concerned with the transport of data, while the upper layers (Transport, Session, Presentation, Application) deal with the formatting and management of that data for various applications. This layered approach allows for modular networking, where each layer can operate independently yet collaboratively to ensure efficient and reliable network communication.


## Hourglass Model of the Internet

### Top of the Hourglass: Application Layer
- **Wide Range of Applications**: The top wide part of the hourglass represents the multitude of applications and high-level protocols (like HTTP for web browsing, SMTP for email, FTP for file transfer, etc.).
- **Diversity**: This layer is diverse and ever-expanding, allowing for a wide range of applications and services to be built.

### Narrow Waist: Internet Protocol (IP) Layer
- **Simplicity and Universality**: The narrow middle of the hourglass represents the Internet Protocol (IP) layer. It's the core of the Internet's architecture, providing a simple set of rules for routing packets of data from source to destination.
- **Uniformity**: All data, regardless of its final application, passes through this layer. This uniformity simplifies the routing process and ensures interoperability across different networks and devices.

### Bottom of the Hourglass: Network Access Layer
- **Diverse Technologies for Data Transmission**: The bottom wide part of the hourglass represents the various network technologies used to transmit data (like Ethernet, Wi-Fi, LTE, Fiber Optics, etc.).
- **Flexibility**: This layer is characterized by a variety of physical and data link technologies that can connect devices to the Internet. Despite their differences, they all support the IP layer above.

### Significance of the Hourglass Model
- **Simplicity at the Core**: By having a simple, standardized IP layer at its core, the Internet can support a wide range of applications and network technologies. This design allows for innovation and expansion at both the application and network layers without changing the core IP layer.
- **Interoperability**: The model ensures that `as long as data can be packaged into IP packets`, it can traverse the Internet regardless of the application or the underlying physical network.
- **Scalability**: This architecture allows the Internet to grow and incorporate new technologies and applications without fundamental changes to its core.

### Conclusion
The hourglass model of the Internet effectively illustrates how a simple and universal protocol at its core (IP) can support a vast and diverse range of applications and network technologies. This design principle is key to the Internet's widespread success and its ability to continuously evolve and accommodate new technologies and services.

> However, it's extremely hard to change the IP protocol, which is why we have IPv4 and IPv6 at the same time. The reason why it's really hard to change is because it's the core of the Internet, and it's really hard to change the core of the Internet.


## Reviews

Sure, let's go through these questions one by one:

### 1. When a router sees an IP address, how does it know where to forward it?
- A router uses a routing table to decide where to forward packets. The routing table contains information about the topology of the network and uses IP addresses to determine the best next hop for a packet. When a router receives a packet, it examines the destination IP address and checks its routing table to find the best route for the packet. If the destination is on the router's local network, it sends the packet directly to that destination. If not, it forwards the packet to another router that is closer to the destination.

### 2. Speculate on why IP is above TCP in the layered model. Why does the TCP header go on before the IP header and not the other way around?

1. **Separation of Responsibilities**:
   - The layered model divides network responsibilities into distinct layers, each handling a specific aspect of data communication.
   - **TCP (Transport Layer)**: Focuses on data transmission between devices, ensuring data is sent reliably and in order.
   - **IP (Network Layer)**: Deals with routing the data across different networks to reach the correct destination.

2. **Why TCP Comes Before IP**:
   - **Order of Operations**: When a message is sent over the Internet, it first goes through the Transport Layer (TCP), where it is broken down into segments, and transport-level considerations like establishing a connection, reliability, and order are applied.
   - **Addition of Headers**: Each layer adds its own header information to the data packet:
     - **TCP Header**: Contains information like `source and destination port numbers`, `sequence numbers`, `acknowledgment numbers`, etc.
     - **IP Header**: Added after the TCP header, containing source and destination IP addresses, among other things.
   - **Conceptual Flow**: Conceptually, the data flows from the application down through the layers. It hits TCP (Transport Layer) first, where it's prepared for transport. Then it moves to IP (Network Layer) where it's prepared for routing.

3. **Why Not the Other Way Around**:
   - **Data Integrity and Order First**: It's essential to establish a reliable connection and segment the data before worrying about how to route it. TCP handles these tasks.
   - **Routing is the Next Step**: Once the data is reliably prepared for transmission, the next step is to figure out how to get it to the destination, which is IP's role.

#### `Simplified Example`

Imagine sending a letter:
- **TCP's Role**: Writing the letter, putting it in an envelope, and ensuring the letter is ready for posting (e.g., adding a return address, checking the content).
- **IP's Role**: Once the envelope is ready, determining the best postal route to get the letter to its destination.

#### Conclusion

In the network stack, TCP (Transport Layer) handles the preparation of data for transmission, ensuring reliability and proper sequencing. After this, IP (Network Layer) takes over to route this prepared data to its final destination. This sequential process explains why the TCP header is added to data packets before the IP header.

### 3. If UDP is unreliable and TCP is reliable, speculate on why one might ever use UDP.
- UDP (User Datagram Protocol) is used in scenarios where `speed` and `efficiency` are more critical than reliability. For example:
  - Streaming services (like live video or audio) where receiving all data in order isn't as important as keeping the stream going without delay.
  - DNS queries, where the overhead of establishing a TCP connection is not justified for small query-response interactions.
  - Situations where the application can handle some level of packet loss or has its own mechanisms for ensuring data integrity.
  - IoT (Internet of Things) devices, where lightweight and fast communication is preferred.

Using UDP reduces the overhead associated with the connection establishment, error checking, and congestion control features of TCP, making it more efficient for certain types of network communication.
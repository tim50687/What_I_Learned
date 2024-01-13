# Foundation 

## Understanding Computer Networks

**Conceptualization of Computer Networks**:
- Traditionally, networks were specialized for specific data types and connected to particular devices. For example:
  - **Serial Lines Network**: Connected terminals to mainframe computers for keystroke data.
  - **Voice Telephone Network**: Facilitated voice communication.
  - **Cable TV Network**: Disseminated video signals.

**Distinctive Features of Computer Networks**:
- **`Generality` and Versatility**: Unlike specialized networks, computer networks are not optimized for a single type of data or application. They are built with general-purpose, programmable hardware.
- **Multi-Functionality**: Capable of handling various types of data, computer networks support a wide range of applications, far beyond the capabilities of single-use networks.

**Evolution and Integration**:
- **Taking Over Single-Use Networks**: Modern computer networks are increasingly subsuming the roles once played by dedicated networks. They are not just for data transfer but also cater to voice communication, video streaming, and more.
- **Application Diversity**: The range of applications supported by computer networks is constantly expanding, making them integral to numerous aspects of daily life and various industries.

**Implications for Network Design**:
- **Network Design Requirements**: Designers of computer networks need to be aware of the diverse requirements of different applications. The network must be flexible, scalable, and capable of handling a variety of data types and communication needs.

### Conclusion
Computer networks represent a shift from single-purpose data communication systems to versatile, general-purpose platforms capable of supporting an ever-growing array of applications. This generality and flexibility distinguish them from traditional networks and pose unique design challenges and opportunities.

## Applications

- World Wide Web: A application that allows users to access and share information over the Internet using web browsers.
- Email: A application that allows users to send and receive messages over the Internet.
- Online social networks: A application that allows users to connect and share information with other users over the Internet.

...

## Requirements

How these three groups might list the requirements for a network:

- Application Programmer -  List the services that his application needs: How much data they need? What are the dealy limitation on it? Reliability? Security? 
    - Email can tolerate some delay, but video streaming cannot.
    
- Network Designer - List the properties of a cost-effective design.

- Network Provider - List the characteristics of a system that is easy to manage. 


## Networking Concepts: Switches, Hosts, Internetworks, Addressing, and Routing

**1. Network Elements - Switches and Hosts**:
   - **Switches (Inside the Network)**: These are devices within a network whose primary function is to store and forward packets. They manage the flow of data within the network, ensuring that packets reach their intended destinations.
   - **Hosts (Outside the Network)**: These are end-user devices like computers and smartphones connected to the network. Hosts support users, run application programs, and initiate communication within the network.

**2. The Network Cloud Icon**:
   - The cloud symbol in network diagrams represents a network. It's a versatile icon that can denote various network types, including point-to-point links, multiple-access links, or switched networks. In essence, a cloud is a placeholder for any network configuration.

**3. Internetworks and Internet**:
   - **Internetworks (Lowercase 'i' internet)**: An internetwork, or internet, is a network of multiple independent networks (clouds) interconnected together. It's a broader concept than a single isolated network.
   - **The Internet (Capital 'I' Internet)**: Specifically refers to the global network using the TCP/IP protocol suite. It's an instance of an internetwork.
   - **Routers and Gateways**: Devices that connect two or more networks in an internetwork. Like switches, they forward messages from one network to another.

**4. Addressing and Routing**:
> Each node must be able to say which of the other nodes on the network it wants to communicate with. 
   - **Node Addressing**: Each device (node) on a network is assigned a unique address, a byte string that identifies it and distinguishes it from other nodes.
   - **Routing**: The process of systematically forwarding messages to a destination node based on its address. If nodes aren't directly connected, switches and routers use addresses to direct messages through the network.

**5. Communication Types - Unicast, Broadcast, and Multicast**:
   - **Unicast**: Sending a message from a source node to a single destination node.
   - **Broadcast**: Sending a message from a source node to all nodes on the network.
   - **Multicast**: Sending a message from a source node to a selected group of nodes, not necessarily all, within the network.

**6. Summary**:
This introduction covers fundamental networking concepts, including the types of devices that make up a network, how networks are represented and interconnected, and the crucial processes of addressing, routing, and types of network communications.


## Note on Packet-Switched Networks and Statistical Multiplexing

**Packet-Switched Networks - Key to Efficiency**:
- **Fundamental Question**: How can numerous hosts share a network, especially simultaneously? The answer lies in the efficient use of network resources through packet switching and multiplexing.

**Multiplexing - Sharing Network Resources** `How all hosts communicate with each other`:
- **Concept**: Multiplexing is akin to time-sharing in computing. Multiple users share the same physical resources (like links), with each believing they have private access.
- **Application in Networks**: Data from multiple sources is multiplexed over physical network links, allowing efficient sharing and transmission.

**Time-Division and Frequency-Division Multiplexing (STDM and FDM)**:
- **STDM**: Divides time into equal slots, allocating each flow a slot to transmit data in a round-robin manner.
- **FDM**: Assigns different frequencies to different data flows, enabling simultaneous transmission over one link.

**Limitations of STDM and FDM**:
- **Inefficiency During Idle Periods**: If a flow has no data to send, its allocated time or frequency remains unused.
- **Fixed Number of Flows**: These methods are not flexible for dynamic addition or removal of flows.

**Statistical Multiplexing - A Superior Approach**:
- **Dynamic Allocation**: Like STDM, it shares the physical link over `time` but differs by transmitting data from each flow `on demand`.
- **Efficiency**: If only one flow has data, it can use the entire link capacity without waiting, minimizing idle time.
- **Packet-Based**: Once the flow begins sending data, we need some way to limit the transmission, so that the other flows can have a turn. This is done by dividing the data into `packets`. The source may need to `fragment` the message into several packets, with the receiver reassembling them into the original message.

**Packet Switching in Networks**:
- **Packet Transmission**: Decisions on which flow's packet to transmit next are made independently by each switch.
- **Fairness and Quality of Service (QoS)**: Ensuring fair bandwidth allocation and managing congestion are key challenges.

**Network Congestion**:
- **Buffering and Packet Drop**: When incoming data exceeds the link's capacity, switches buffer packets. Prolonged congestion can lead to buffer overflow and packet loss.

**Conclusion**:
Statistical multiplexing in packet-switched networks enables fine-grained, efficient sharing of network resources. It addresses the limitations of earlier methods by dynamically allocating network capacity based on demand, with packet scheduling at each switch playing a critical role in managing network traffic and congestion.

## Different Types of Networks: LANs, WANs, MANs, and SANs

**Network Classification by Size**:
- Networks are often categorized based on their geographical scope and size, influencing the technology and architecture used.

**Local Area Networks (LANs)**:
- **Definition**: LANs are networks that typically extend less than 1 kilometer.
- **Usage**: Commonly used in homes, offices, and building complexes.
- **Characteristics**: High data transfer rates, low latency, and limited geographic coverage.

**Wide Area Networks (WANs)**:
- **Definition**: WANs can span large geographical areas, potentially worldwide.
- **Historical Context**: The term WAN emerged as computers proliferated, necessitating networks that connected geographically distant computers.
- **Usage**: Used for broader communication needs, connecting LANs and MANs, often via leased telecommunication lines.

**Metropolitan Area Networks (MANs)**:
- **Definition**: MANs usually span tens of kilometers, covering a city or a metropolitan area.
- **Usage**: They bridge the gap between LANs and WANs, providing regional connectivity.

**Storage Area Networks (SANs)**:
- **Definition**: SANs are high-speed networks that connect storage devices with servers. They are usually confined to a single room or building.
- **Technology Example**: Fibre Channel is a common technology in SANs, connecting computing systems to storage servers and data vaults.
- **Performance Edge**: SANs often lead in performance and are increasingly integrated into LANs and WANs.

**Implications of Network Size**:
- **Data Propagation Time**: The size of a network often affects the data propagation time – the time it takes for data to travel from one end of the network to the other.
- **Technology Choices**: Different sizes and scopes of networks require distinct technological approaches and considerations.

**Conclusion**:
Understanding the different types of networks – LANs, WANs, MANs, and SANs – is crucial for grasping the varied networking technologies and their specific uses. Each type serves distinct purposes and scales, from local area coverage in LANs to global connectivity in WANs, and specialized high-performance connections in SANs.

## Support for Common services

Since many applications need common services, such as file transfer, email, and the web, it makes sense to provide these services once and then make them available to all applications.  

###   Network Channels in Computer Networks

**Network Channels - Facilitating Application Communication**:
- A network channel is a conceptual pathway through which application-level processes on different hosts communicate over a computer network.

**Beyond Simple Connectivity**:
- **Role of Channels**: Channels are not just about delivering packets from one host to another but about `enabling meaningful communication between applications`.
    - Ex. request/ reply or message streams.
        - A request/ reply channel is a channel that supports a request/ reply protocol, it `guarantees` that a request is received and processed by the recipient, which then sends a reply back to the sender.
        - A message stream channel is a channel that supports a message stream protocol, where one application sends a stream of messages to another application, which then receives the messages in the `same order` they were sent. Furthermore, `support multicast`, where one application can send a message to multiple applications.
- **Simplifying Application Development**: Instead of each application handling complex network functionalities, channels provide common services to simplify this process.

**Characteristics of Network Channels**:
1. **Logical Connection**: Channels represent a logical, not necessarily physical, connection between applications.
2. **Abstraction**: They abstract the complexities of the underlying network, offering a simpler interface for application developers.
3. **Application-Specific Services**: Different applications can use different types of channels based on their specific requirements.

**Services Provided by Channels**:
- **Guaranteed Delivery**: Ensuring that messages are reliably delivered to the recipient.
- **Order Preservation**: Maintaining the order in which messages are sent.
- **Security and Privacy**: Providing secure and private communication to prevent eavesdropping.
- **Error Handling and Correction**: Managing and correcting errors in transmission.


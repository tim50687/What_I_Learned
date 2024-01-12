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

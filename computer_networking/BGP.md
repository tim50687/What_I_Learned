# BGP Routers and Their Role

A **BGP (Border Gateway Protocol) router** is a crucial component of the internet's infrastructure, acting as a pivotal point that directs data traffic between different autonomous systems (ASes). An autonomous system is a collection of IP networks and routers under the control of one or more network operators that presents a common routing policy to the internet.

### Configuration and Connection

1. **Physical Connection**: Network administrators physically connect BGP routers to one another using network cables. These connections can be within the same AS (internal connections) or between different ASes (external connections).

2. **Port Configuration**: Each port on the router, to which cables are connected, is configured with an IP address. This address is unique to the port and allows the router to participate in the network. The configuration process involves:
   - Assigning an **IP address** to the port. Each port has a different IP address to identify different segments of the network or connections to different ASes.
   - Defining the **type of BGP relationship** for the port, which could be with a provider, a peer, or a customer:
     - **Provider**: An AS that provides access to the internet or other networks.
     - **Peer**: An AS that exchanges traffic with your AS, often on an equal basis, without charging.
     - **Customer**: An AS that pays for the internet access or network connectivity.
   - Optionally, configuring **specific routes** via each neighbor, which involves setting up predefined paths for data traffic.

### BGP Sessions Establishment

Once the manual configuration is done, the router is turned on. It then initiates contact with its neighbors (other routers it's connected to) to establish BGP sessions. These sessions are used for exchanging routing information.

### Main Functions of BGP Routers

1. **Updating Forwarding Tables**: The router receives BGP protocol messages from its neighbors, which contain routing information. Based on this information, the router updates its forwarding table, which is a database that holds the best paths to various network destinations.

2. **Distributing Routing Information**: The router also sends BGP protocol messages to its neighbors, helping them keep their forwarding tables up-to-date. This mutual exchange of information ensures that each router knows the best paths for directing traffic to any destination in the network.

3. **Forwarding Data Packets**: The router uses its forwarding table to make decisions about where to send incoming data packets. Its goal is to ensure that data packets reach their intended destinations as efficiently as possible. This process involves examining the destination IP address of each packet and using the forwarding table to determine the best next hop (next router) on the path to the destination.

## Example

If a BGP router has 6 ports, each port would still be uniquely configured to handle connections to different networks or autonomous systems (ASes), with each port assigned a distinct IP address. This setup allows the router to manage multiple relationships and route traffic appropriately based on the source and destination of each packet. Let's expand the previous example to include 6 ports on a BGP router, connecting to a variety of networks.

### Router Setup with 6 Ports

- **Ports Configuration:**
  - **Port A** and **Port B**: Connections to **Customers**
  - **Port C** and **Port D**: Connections to **Peer ISPs**
  - **Port E** and **Port F**: Connections to **Providers**

### Configuration Details

1. **Customer Connections (Ports A & B)**
   - **Port A:**
     - **Your IP:** 192.168.10.1
     - **Customer's Router IP:** 192.168.10.2
   - **Port B:**
     - **Your IP:** 192.168.20.1
     - **Customer's Router IP:** 192.168.20.2
   - These ports connect to customers' networks, providing them access to your network and the broader internet.

2. **Peer ISP Connections (Ports C & D)**
   - **Port C:**
     - **Your IP:** 10.20.30.1
     - **Peer ISP's Router IP:** 10.20.30.2
   - **Port D:**
     - **Your IP:** 10.20.40.1
     - **Peer ISP's Router IP:** 10.20.40.2
   - These ports are used for peering agreements with other ISPs, exchanging traffic to mutually benefit both networks' customers.

3. **Provider Connections (Ports E & F)**
   - **Port E:**
     - **Your IP:** 172.16.40.1
     - **Provider's Router IP:** 172.16.40.2
   - **Port F:**
     - **Your IP:** 172.16.50.1
     - **Provider's Router IP:** 172.16.50.2
   - These ports connect to upstream providers, facilitating access to the global internet. You pay the providers for this service.

### BGP Sessions

Each port establishes a BGP session with the router on the other end to exchange routing information. This ensures your router knows the best paths for directing traffic, depending on its destination.

### Traffic Routing

The router uses the BGP routing information to intelligently route traffic:
- Traffic destined for the internet might go through the providers on Ports E or F.
- Incoming traffic for your customers is routed to the appropriate customer port, A or B.
- Traffic to and from peer ISPs, meant for mutual exchange without financial settlement, goes through Ports C and D.

## Why different port has different IP address

Assigning different IP addresses to each port on a router, particularly in complex networking scenarios like those involving BGP, is foundational for several key operational and technical reasons:

1. **Network Segmentation and Identification**: Each port on a router can be connected to different networks or segments, each requiring a unique identity within its respective network. The IP address assigned to a port serves as the identifier for that segment of the network, enabling clear communication and routing decisions both within the router's local network and in the broader internet.

2. **Routing Decisions**: Routers make forwarding decisions based on destination IP addresses. Having a unique IP address for each port allows the router to correctly identify the entry and exit points for data packets. This is crucial for implementing routing policies and ensuring that packets are forwarded along the optimal paths to their destinations.

3. **BGP Peering and Relationships**: In BGP, routers establish peer relationships to exchange routing information. Each peering relationship is uniquely identified by the IP addresses of the ports on the connecting routers. Different ports with different IPs allow a single router to establish multiple peering relationships, each potentially with different routing policies and agreements (such as with providers, peers, or customers).

4. **Security and Policy Enforcement**: Unique IP addresses enable the application of specific security policies or access controls for traffic entering or leaving through each port. This granularity is vital for protecting the network from attacks, managing traffic flows, and enforcing policies based on the type of connection (e.g., customer vs. provider).

5. **Simplification of Network Management**: Different IP addresses on each port simplify network management and troubleshooting. Network administrators can easily configure, monitor, and manage each connection individually, applying specific settings or changes to one port without affecting others.

6. **Scalability and Flexibility**: As networks grow and evolve, new connections may be added, and existing ones may change. Having a unique IP for each port provides the flexibility to adapt to these changes without disrupting the entire network's operation. It allows for easy expansion, reconfiguration, and integration of new services or connections.


## Path vector protocol
# Intra Domain Routing

The organization of the Internet into a two-level hierarchy involves the use of autonomous systems (ASs) and inter-domain routing protocols.

1. **Autonomous Systems (ASs):**
   - An autonomous system (AS) is a region of the Internet under a single administrative domain or authority. Examples of ASs include large Internet Service Providers (ISPs) like Comcast, AT&T, Verizon, T-Mobile, etc.
   - Within an AS, there can be multiple routers and networks managed by the same organization, but they operate under a unified administrative control.

2. **Intra-Domain Routing Protocols:**
   - Within an AS, routing is managed using intra-domain routing protocols. These protocols are used to exchange routing information and compute paths between routers within the same AS.
   - Examples of intra-domain routing protocols include Distance Vector protocols like Routing Information Protocol (RIP) and Link State protocols like Open Shortest Path First (OSPF).

3. **Inter-Domain Routing Protocols:**
   - Inter-domain routing protocols are used to exchange routing information between different ASs, enabling communication between networks operated by different organizations.
   - The primary inter-domain routing protocol used on the Internet is Border Gateway Protocol (BGP). BGP is the de facto standard for inter-domain routing and is widely deployed across the Internet.
   - BGP allows ASs to exchange routing information, including reachability information for IP prefixes (network addresses), and make routing decisions based on policies and network conditions.

4. **Border Gateway Protocol (BGP):**
   - BGP operates on routers at the edges of ASs, known as Border Gateway Routers (BGP routers). These routers establish connections with BGP routers in neighboring ASs and exchange routing information.
   - BGP routers advertise the IP prefixes they can reach and receive advertisements from neighboring ASs, allowing them to build a view of the Internet's topology and make routing decisions accordingly.
   - BGP supports policies that allow ASs to control how traffic is routed, enabling them to implement traffic engineering, traffic shaping, and other network management strategies.

## Why do we need AS

Autonomous Systems (ASes) play a crucial role in the architecture and operation of the Internet for several reasons:

1. **Scalability:** The Internet began as a network of interconnected networks, each managed by different organizations. As the Internet grew, it became impractical to manage routing information for the entire Internet as a single entity. ASes allow for the hierarchical organization of networks, which improves the scalability of routing and network management.

2. **Efficient Routing:** Routing algorithms are not efficient enough to execute on the entire Internet topology due to its size and complexity. By dividing the Internet into ASes, routing algorithms can focus on smaller, more manageable portions of the network, leading to more efficient routing decisions.

3. **Different Routing Policies:** Different organizations may have varying routing policies based on factors such as cost, performance, and security. ASes allow organizations to implement their own routing policies within their networks, including preference for certain routes or traffic engineering strategies.

4. **Network Privacy:** ASes provide a level of privacy by allowing organizations to hide the internal structure of their networks from external entities. By defining boundaries around their AS, organizations can control the flow of traffic into and out of their network, protecting sensitive infrastructure and resources.

5. **Interconnection and Peering:** ASes interconnect with each other through peering agreements to exchange traffic. Border Gateway Protocol (BGP), the primary inter-domain routing protocol, enables ASes to negotiate these peering arrangements and exchange routing information. ASes can choose how to route traffic across each other based on factors such as cost, performance, and business relationships.

## Routing Problem

- How does router learn the shortest path to a destination?

### Link State Routing

#### OSPF (Open Shortest Path First)

[GOOD VIDEO](https://www.youtube.com/watch?v=kfvJ8QVJscc)

- Every router has the same view of the network topology.

1. Get the neighbors and their cost.

- Set the router ID.

- Need 2 way communication to become neighbors.

2. Build the Link State Database.

- Routers collect LSAs from neighboring routers and use this information to build a Link-State Database (LSDB).

3. Run the Dijkstra's algorithm to find the shortest path.

> Route Table: sometimes called Forwarding Database, the routing table defines the network traffic forwarding rules of a given router
> Topology Map: also called Link State Database, this table holds topological information about the working network
> Neighbors Table: sometimes referred to as Adjacency Database, it keeps data and routing details about directly connected neighbors of a given router

### Distance Vector Routing

A distance vector-based router communicates and evaluates paths only between them and their immediate `neighbors`. So, routers share their information about the network with their `neighbors`, enabling them to calculate the distance between them and a particular destination.




## Main differences between Bellman Ford and Dijkstra's algorithm

----
- Bellman Ford’s Algorithm works when there’s `negative weight edge`, it also detects the negative weight cycle. 
- Dijkstra’s Algorithm doesn’t work when there’s negative weight edge.

---

- **Bellman-Ford Algorithm (e.g., used in Distance Vector routing protocols):**
  - Bellman-Ford algorithm performs checks on all vertices iteratively, updating the distance to each vertex until convergence is reached.
  - This approach, although less complex, requires comparing distances to all vertices at each iteration.
  - In distributed environments, such as those found in Distance Vector routing protocols like RIP (Routing Information Protocol) and IGRP (Interior Gateway Routing Protocol), where mostly local information is used, Bellman-Ford's simplicity makes it easier to implement.
  - Distance Vector protocols rely on routers exchanging routing information with their directly connected neighbors, making Bellman-Ford a suitable choice due to its distributed nature and simplicity.

- **Dijkstra's Algorithm (e.g., used in Link State routing protocols):**
  - Dijkstra's algorithm selects the vertex with the best distance calculated so far and updates its neighbors accordingly.
  - While Dijkstra's algorithm provides more efficient routing by focusing only on vertices with the best distance, it requires distributing the entire network topology before calculations can begin.
  - Link State protocols, such as OSPF (Open Shortest Path First) and ISIS (Intermediate System to Intermediate System), distribute the entire network topology to all routers, enabling the use of Dijkstra's algorithm for more accurate and optimized routing decisions.


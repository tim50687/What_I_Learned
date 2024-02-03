# Bridging

> Hub is stupid, it just broadcast all the packets to all the ports. and also expand the collision domain.

1. **Bridging Different LANs**:
   - A Local Area Network (LAN) is a network that covers a relatively small area like a home, office, or building. Traditionally, LANs were isolated from each other.
   - A bridge is a network device used to connect multiple LANs. By doing so, it effectively creates a single, larger network. This is particularly useful in environments where you have multiple LAN segments that need to communicate with each other.

> Bridge should understand MAC address, and only send to destination.

2. **Forwarding Packets to Intended Recipients**:
   - One of the primary functions of a bridge is to decide whether to forward or filter out a packet based on the packet's destination address.
   - A bridge learns the addresses of devices on each LAN segment it connects. When it receives a packet, it checks the destination MAC (Media Access Control) address and only forwards the packet to the LAN segment where the recipient device is located. If the destination device is on the same segment as the sender, it doesn't forward the packet.

3. **Reduction in Broadcasting**:
   - In a typical LAN using a hub (a basic networking device), all packets are broadcasted to every port, regardless of the intended recipient. This can lead to a lot of unnecessary traffic and can reduce the overall efficiency of the network.
   - A bridge, on the other hand, reduces this broadcasting. By only forwarding packets where they need to go, it cuts down on unnecessary network traffic. This is especially beneficial in networks where there's a lot of inter-LAN traffic.

4. **Benefits of Using Bridges**:
   - **Increased Network Efficiency**: By reducing unnecessary traffic, bridges make the network more efficient.
   - **Segmentation**: Bridges can be used to segment large networks into smaller, more manageable sections, reducing overall network congestion.
   - **Connectivity**: They enable devices on different LANs to communicate with each other, enhancing network functionality.

5. **Other Considerations**:
   - While bridges were more common in earlier network designs, in modern networks, switches (advanced bridges) are more commonly used. A switch is essentially a multi-port bridge that performs the same filtering and forwarding functions more efficiently.


## Bridging Limits the Size of Collision Domains:

A collision domain is a network segment where data packets can "collide" with each other if sent simultaneously by devices. In a typical Ethernet network using a hub, the entire network acts as a single collision domain.
Bridges help to `limit the size of collision domains`. By intelligently forwarding frames only to the segment where the recipient device is located, a bridge reduces the chances of collisions. Each port on a bridge essentially creates a separate collision domain.

## Improves Scalability

By reducing the size of collision domains, bridges enhance the scalability of networks. Networks can grow larger without facing the performance degradation associated with too many devices trying to communicate on the same network segment.

## Tradeoff: Complexity of Bridges vs. Hubs:

- Hubs are simple `physical layer devices` (Layer 1 in the OSI model). They merely replicate incoming signals to all ports without any filtering or processing.
- Bridges, however, are `data link layer devices` (Layer 2). They need to examine, process, and selectively forward frames based on MAC addresses. This requires more sophisticated hardware.

## Bridges vs Switches

### Bridges 
- One port facing one LAN and the other port facing the other LAN.
- Bridges learn which hosts are on `each side of the LAN`.

### Switches
- Facilitate communication between multiple devices on the same LAN.
- Multiple Ports.
- Learn which host are on `each port`.

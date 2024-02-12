# Network Layer 

## Router 

- Figure out the most efficient path for data to travel from one network to another.

- Connects imcompatible networks (Dealing with `Heterogeneity`)
    - Every network within the Internet can have different `capacities`, `technologies`, and `protocols`. The Internet's architecture and protocols are designed to bridge these differences, enabling seamless communication across disparate networks.

- Ensure network can scale.
    - Scalable routing protocols, such as `BGP` (Border Gateway Protocol), enable efficient data packet delivery across diverse and changing paths, managing the Internet's complex topology.


- How do you name a host?
    - IP address

> Best-effort (i.e. things may break)

## Possible Addressing Schemes

Addressing Schemes:

1. **Flat:** Uses a unique identifier like a 48-bit MAC address for each host. Challenges include `massive routing tables`, difficult `maintenance` due to `dynamic host availability`, and slow routing processes.

2. **Hierarchy:** Addresses are segmented into levels of specificity, facilitating scalable routing by reducing the need for routers to maintain exhaustive, constantly updated tables. This approach supports `mobility`, such as with cellphones, without overwhelming the routing system.
    - Changes stay local, if NEU changes its IP address, Suffolk county doesn't need to know about it.

## IP Addressing

- Store in big endian format.

### Big Endian vs Little Endian

In computing, MSB stands for "Most Significant Byte." The significance of a byte refers to its weight or position in the sequence of bytes that make up a larger data item, such as a multi-byte integer or a memory address.

- **Big Endian:** In Big Endian format, the MSB is stored first at the lowest memory address, and the remaining bytes follow in decreasing order of significance. For example, if we have a 4-byte (32-bit) integer with a value of 0x12345678, it would be stored in memory as:

  ```
  Address 0: 12 (MSB)
  Address 1: 34
  Address 2: 56
  Address 3: 78 (LSB - Least Significant Byte)
  ```

  Here, the byte with the value 0x12, which is the most significant byte, is stored first.

- **Little Endian:** Conversely, in Little Endian format, the LSB (Least Significant Byte) is stored first at the lowest memory address, and the remaining bytes follow in increasing order of significance. Using the same example value of 0x12345678, it would be stored in memory as:

  ```
  Address 0: 78 (LSB)
  Address 1: 56
  Address 2: 34
  Address 3: 12 (MSB)
  ```

  In this case, the byte with the value 0x78, which is the least significant byte, is stored first.

The choice between Big Endian and Little Endian affects how data is read from and written to memory, as well as how it's transmitted over networks. It's important for systems to agree on an order when sharing data to ensure correct interpretation. The Big Endian format is also referred to as "Network Byte Order" because it's the standard for most network protocols, ensuring consistent data exchange across diverse systems.

## Home router

**Complexity and Density Considerations:**
- Routers typically have fewer ports and are designed to route traffic between different networks, making them more complex and less suited for directly connecting a large number of devices.
- Switches, on the other hand, are designed to connect multiple devices within the same network. They are simpler in operation, focusing on forwarding packets based on MAC addresses, and can support a higher density of connections.

**Home Routers:**
- The common "home router" is actually a combination of a router (for routing traffic to and from the internet) and a switch (the LAN ports used to connect local devices). This setup simplifies connectivity for home users by providing both routing and switching capabilities in a single device.

**Servers and Scalability:**
- In environments with a large number of servers, such as data centers, relying solely on Layer 2 switching (the domain of switches) can lead to scalability issues. This is due to the limitations of protocols like spanning tree, which are used to prevent loops in networks.
- An advanced setup might involve connecting each server to multiple switches using routed interfaces, employing protocols like OSPF for routing, and using technologies like VXLAN for any necessary Layer 2 broadcasts. This approach reduces the reliance on traditional Layer 2 technologies and improves scalability and resilience.

**Summary:**
- Switches are favored for their simplicity and ability to efficiently connect many devices within the same network. They work well for end-users and small to medium-sized networks.
- For larger networks, particularly those with significant server infrastructure, a more complex routed approach using routers and advanced networking techniques is necessary to ensure scalability and performance.
- The choice between using switches and routers (or a combination of both) depends on the specific needs of the network, including the number of devices, the requirement for inter-network routing, and scalability considerations.



## Two ways to name IP

## **Old School Method: Class-Based Hierarchy**
- Uses the first three bits of the IP address as a prefix to denote the network's class, size, and "name" or prefix. This method categorizes networks into classes (A, B, C, etc.) based on their size and the portion of the address allocated for network and host identifiers.

> Have no clue what he is talking about, just remember the concept (A, B and C).
--- 

### Subnetting

This example demonstrates how IP addresses are divided into network, subnet, and host components using network and subnet masks in IP networking.

1. **Network Mask Operation:**
   - The IP address `10110101 11011101 01010100 01110010` is given.
   - A network mask of `11111111 11111111 00000000 00000000` is applied using the bitwise AND operation.
   - This operation isolates the network portion of the IP address, resulting in `10110101 11011101 00000000 00000000`, effectively removing the host part and leaving the network identifier.

> We know where is the network and where is the host.

2. **Subnet Mask Operation:**
   - The same IP address is considered with a more specific subnet mask of `11111111 11111111 11000000 00000000`.
   - Applying this subnet mask with a bitwise AND operation narrows down the address to `10110101 11011101 01000000 00000000`, which identifies a specific subnet within the larger network by also removing the host-specific portion but retaining more detail than just the network portion.

> You `increase the number of available networks` (subnets) that can be created within the original IP address class, allowing for more granular control over network segmentation and addressing.  

> You `decrease the number of hosts` that can be assigned within each subnet, which can actually be beneficial for managing broadcast traffic, enhancing security, and improving overall network performance.

[good video](https://www.youtube.com/watch?v=s_Ntt6eTn94&t=944s)

3. **Extracting the Host Component:**
   - To find the host part of the IP address, the subnet mask is inverted using the bitwise NOT operation (`~`), turning `11111111 11111111 11000000 00000000` into `00000000 00000000 00111111 11111111`.
   - This inverted mask is then ANDed with the original IP address, isolating the host portion: `00000000 00000000 00010100 01110010`.
   - This result shows the host-specific part of the IP address, distinguishing this particular host within its subnet.

The network and subnet masks are tools used to segment an IP address into hierarchical levels, enabling organized network and subnet management. This segmentation facilitates routing by allowing routers to make decisions based on network and subnet identifiers, while the host portion identifies a specific device within these networks.

#### N-Level Subnet Hierarchy by subnetting:

Imagine a university network with a Class B IP address space, which gives it a substantial number of IP addresses to distribute across its campus. The university could organize its network in a hierarchical manner as follows:

- **Level 1 (Campus-wide network):** The university starts with its entire network address space. This level is the most general and covers the entire campus.

- **Level 2 (College networks):** The university divides its network into subnets for each college. For example, the Engineering College, the Business College, and the Liberal Arts College each get a subnet. This division helps in managing the network more efficiently by grouping related departments.

- **Level 3 (Department networks within colleges):** Each college further subdivides its subnet among its departments. For instance, within the Engineering College, there might be separate subnets for the Computer Science Department, the Electrical Engineering Department, and the Mechanical Engineering Department.

- **Level 4 (Specific labs or offices):** Departments can further divide their subnets for individual labs, faculty offices, or student residence halls. Each lab or office might have its subnet, allowing for finely tuned network management and security settings.

At each level, a portion of the IP address space is allocated for defining subnets, borrowing bits from the host portion to create more networks with fewer hosts per network. This hierarchical approach ensures that the university can manage its IP addresses efficiently, providing precise control over access, routing, and network policies at each organizational level. It also simplifies routing by allowing routers to aggregate routes to larger subnets at higher levels of the hierarchy, reducing the size of routing tables.

#### Why use subnetting?

**Note: Benefits of Subnetting**

Subnetting is a network practice that offers several advantages:

1. **Efficient Traffic Routing:** Subnetting divides broadcast domains, leading to more efficient routing of network traffic. This improves network speed and overall performance by reducing unnecessary broadcast traffic.

2. **Enhanced Network Security:** Subnetting contributes to network security by creating distinct subnetworks within a larger network. This allows for better route mapping and identification of potential threats. Devices in one subnet are isolated from others, enabling companies to control access to sensitive data more effectively.

3. **Organizational Control:** Subnetting facilitates sound organization within large businesses. It grants organizations full control over their traffic, data packets, network structure, and routers. This helps in managing complex networks efficiently.

Overall, subnetting is a valuable technique for optimizing network performance, enhancing security, and maintaining control over network resources in both small and large-scale environments.


## **Modern Method: Classless Inter-Domain Routing (CIDR)**
> classless


- Moves away from the rigid class-based system to a more flexible approach that allows for more efficient allocation of IP addresses. CIDR uses variable-length subnet masking (VLSM) to specify network and host portions of an IP address, enabling the creation of differently sized networks and more precise control over IP address assignments.
### Example routing table

[Good tutorial](https://www.youtube.com/watch?v=pbqc6IlFuVc)
[subnetting](https://www.youtube.com/watch?v=ecCuyq-Wprc)

- Slash: means how many bits are used for the network.

- Broadcast address: The last address in the range of IP addresses for a subnet. It is used to send data to all devices on the subnet.

### Example (Solve classful IP address)

**CIDR (Classless Inter-Domain Routing)**

- CIDR is a technique introduced to overcome the limitations of classful IP addressing and efficiently allocate IP addresses.
- It uses a 32-bit IP address representation and allows for flexible allocation of address blocks based on the specific needs of organizations.

**CIDR Block Representation:**

- CIDR blocks are represented as "a.b.c.d/n," where "n" represents the number of bits in the Block ID or Network ID portion.

**Example:**

- 20.10.50.100/20 represents a CIDR block with a 20-bit Block ID and a 12-bit Host ID.

**Rules for Forming CIDR Blocks:**

1. **Contiguous IP Addresses:**
   - All IP addresses within a CIDR block must be contiguous, meaning they follow one another sequentially.

2. **Block Size as a Power of 2 (2^n):**
   - The size of a CIDR block must be a power of 2 (2^n). This ensures that the block can be efficiently divided and that the Block ID can be easily determined.
   - Example: If the block size is 2^5, then the Host ID contains 5 bits, and the Network ID contains 32 - 5 = 27 bits.

3. **First IP Address Divisible by Block Size:**
   - The first IP address within a CIDR block must be evenly divisible by the size of the block.
   - In other words, the least significant bits of the Host ID should start with zeroes.
   - This allows the least significant bits to be used as the Block ID portion.
   - Example: For the block 100.1.2.32 to 100.1.2.47, all three rules are satisfied, making it a valid CIDR block.


### Example (Shorter routing table)
I apologize if my previous explanation was unclear. Let me provide a more detailed example to illustrate how CIDR reduces the size of routing tables.

Suppose you have a router that needs to maintain a routing table for four different IP address blocks, each with a /24 subnet mask:

1. 192.168.1.0/24
2. 192.168.2.0/24
3. 192.168.3.0/24
4. 192.168.4.0/24

Without CIDR, each of these subnets would require a separate entry in the routing table. In this case, the routing table would look like this:

- Destination Network: 192.168.1.0/24
- Destination Network: 192.168.2.0/24
- Destination Network: 192.168.3.0/24
- Destination Network: 192.168.4.0/24

So, there are four separate entries in the routing table to represent these four networks.

Now, let's apply CIDR and route aggregation:

With CIDR, you can combine these four networks into a single entry by finding the longest common prefix that covers all of them. In this case, the common prefix is "192.168.," which includes all the addresses. The subnet mask required to encompass all these networks is /22 because it covers 192.168.1.0 to 192.168.4.0.

So, using CIDR and route aggregation, you would have a single entry in the routing table:

`“Send me anything with addresses beginning 192.168.0.0/22”`

This single entry represents all four of the original networks (192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24, and 192.168.4.0/24) by summarizing them into one larger address block. By doing this, you reduce the number of entries in the routing table from four to just one, which simplifies routing table management and makes the routing process more efficient.


## How do you get IP address?

Obtaining IP addresses involves a hierarchical process that begins with the allocation of IP address ranges by the Internet Assigned Numbers Authority (IANA) and then further distribution to regional authorities and ultimately to organizations that need IP addresses. Here's an explanation of this process:

1. **IANA (Internet Assigned Numbers Authority):**
   - IANA is responsible for the global coordination of IP address allocations, among other Internet-related functions.
   - Its history dates back to 1972 with the establishment of ARPANET at UCLA.
   - Today, IANA is part of the Internet Corporation for Assigned Names and Numbers (ICANN), which oversees various aspects of Internet governance.

2. **Regional Internet Registries (RIRs):**
   - IANA divides the world into several regions, each served by a Regional Internet Registry (RIR).
   - RIRs are responsible for managing IP address allocations within their respective regions.
   - Examples of RIRs include ARIN (American Registry for Internet Numbers), RIPE NCC (Réseaux IP Européens Network Coordination Centre), APNIC (Asia-Pacific Network Information Centre), and others.

3. **Requesting IP Addresses:**
   - Organizations that require IP addresses for their networks or infrastructure submit requests to their respective RIR.
   - These requests typically include information about the organization's size, technical requirements, and justification for the number of IP addresses needed.

4. **RIR Allocation:**
   - The RIR reviews the request and, if approved, assigns a range of IP addresses to the organization based on the organization's needs and the available address space.
   - The allocated IP address range is often in the form of CIDR blocks (Classless Inter-Domain Routing).

5. **Advertisement of Routes:**
   - Once an organization receives an IP address allocation from the RIR, it can advertise these routes to the global Internet via its network infrastructure.
   - This allows other routers on the Internet to know how to reach the organization's IP addresses.

6. **Secondary Markets and Auctions:**
   - In addition to the traditional process of obtaining IP addresses directly from an RIR, there are now secondary markets for IP address blocks.
   - Organizations that have unused or surplus IP address space can sell or transfer it to other organizations in need.
   - These transfers often involve negotiations, legal agreements, and sometimes auctions.

## IP fragmentation 

### Each network jas its own Maximum Transmission Unit (MTU)

MTU: The maximum size of a data packet that can be transmitted over a network.

> The smaller the MTU, the more fragmented the data will be. -> more headers -> more overhead.

- When specifying the MTU for an Ethernet network, you are generally referring to the maximum size of the IP packet's payload, excluding the Ethernet header and trailer.

- `Second bit of flags`: Don't fragment.
    - Might send back an ICMP message to the sender. (Hey, I can't send this packet, it's too big.)
    - We might not want the attacker to insert fragments instead of the original packet.

### Challenges of IP Fragmentation
The challenges mentioned - out-of-order fragments, missing fragments, duplicate fragments, and overlapping fragments - refer to issues that can occur when IP packets are fragmented and reassembled. These challenges can create complexities and difficulties for memory management and proper packet reconstruction in network devices and applications. Here's an explanation of each challenge:

1. **Out-of-Order Fragments:**
   - Out-of-order fragments occur when the fragments of an IP packet arrive at their destination in a different order than they were originally sent.
   - This can happen due to varying network conditions where some fragments may take longer routes or encounter delays, causing them to arrive out of sequence.
   - Managing out-of-order fragments requires buffering and sorting them until all fragments arrive, so they can be properly reassembled in the correct order.

2. **Missing Fragments:**
   - Missing fragments occur when one or more fragments of an IP packet are lost or dropped during transmission.
   - When fragments are missing, it becomes impossible to fully reconstruct the original packet, which can lead to data loss or incomplete information.
   - To handle missing fragments, network devices must have mechanisms to detect missing pieces and request retransmissions or drop the entire packet if necessary.

3. **Duplicate Fragments:**
   - Duplicate fragments can occur when the same fragment of an IP packet is transmitted more than once due to network errors, packet retransmissions, or other issues.
   - Duplicate fragments waste network resources and can lead to unnecessary processing and memory usage.
   - Network devices need to detect and eliminate duplicate fragments to avoid processing redundant data.

4. **Overlapping Fragments:**
   - Overlapping fragments happen when different fragments of an IP packet cover the same portion of the original packet's data.
   - Overlapping fragments can lead to ambiguities during reassembly because it's unclear which data should be retained.
   - Managing overlapping fragments requires careful examination of the offset values in the IP fragmentation headers to determine the correct alignment and eliminate redundancy.

> Endpoints reassemble the fragments, not the routers.
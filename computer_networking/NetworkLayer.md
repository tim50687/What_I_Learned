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
- Moves away from the rigid class-based system to a more flexible approach that allows for more efficient allocation of IP addresses. CIDR uses variable-length subnet masking (VLSM) to specify network and host portions of an IP address, enabling the creation of differently sized networks and more precise control over IP address assignments.
### Example routing table

[Good tutorial](https://www.youtube.com/watch?v=pbqc6IlFuVc)
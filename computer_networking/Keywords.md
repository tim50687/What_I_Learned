# Keywords

## Switching 

### Switching in Telecommunications and Networking

**Switching** is a key process in telecommunications and networking that involves directing data signals or voice calls between different points within a network. It is fundamental to the operation of both telephone and computer networks, enabling efficient communication and data transfer. Switches, the devices that perform this function, determine the best path for data to travel to reach its intended destination.

### Circuit Switching

**Circuit Switching** is a type of network switching where a dedicated communication path or circuit is established between two endpoints for the duration of a call or data transfer session. This method was traditionally used in telephone networks. Key characteristics include:
- **Dedicated Path**: A continuous physical connection is established for the entire duration of the communication.
- **Exclusive Resource Allocation**: Network resources (like bandwidth) along the established path are exclusively reserved for the connected parties.
- **Consistent Quality**: Provides a high and consistent quality of service, ideal for voice calls.
- **Inefficiency in Resource Usage**: Can be inefficient, as the dedicated path remains underutilized when no data is being transmitted. `Scales poorly for large networks.`

### Packet Switching

`The packets actually go one at a time, but they are interleaved so it looks simultaneous.`

**Packet Switching** is the approach used in modern computer networks, including the Internet. In this method, data is broken into smaller units called packets, which are then routed independently through the network to their destination. Key features include:
- **No Dedicated Path**: Unlike circuit switching, packet switching does not require a dedicated path. Packets can take various routes to reach the destination.
- **Efficient Resource Utilization**: This approach allows for more efficient use of network resources through statistical multiplexing, as the network bandwidth is shared among multiple users.
- **Flexibility and Scalability**: Offers greater flexibility and scalability, accommodating more users and data types.
- **Potential for Variable Quality**: Since resources are not reserved, packet-switched networks can experience variable quality, especially during high traffic conditions.

In conclusion, while circuit switching offers consistency and reliability for voice communications, packet switching provides flexibility, efficiency, and scalability, making it suitable for the diverse and high-volume traffic of modern digital networks.


### Networking Key Concepts: An Overview

**Speed/Bandwidth**:
- **Definition**: Bandwidth refers to the maximum rate at which data can be transferred over a network connection in a given amount of time. It is typically measured in bits per second (bps).
- **Importance**: Higher bandwidth means more data can be transferred, leading to faster internet speeds. It is crucial for applications requiring high data transfer rates, like streaming video.

**Latency**:
- **Definition**: Latency is the time it takes for data to travel from its source to its destination across a network. It is usually measured in milliseconds.
- **Relevance**: Lower latency is essential for real-time applications like online gaming or video conferencing, where delays can be noticeable and disruptive.


**Encoding**:
- **Definition**: Encoding in networking refers to the process of converting data into a form that can be easily transmitted and then decoded at the destination.
- **Application**: It includes methods like digital-to-analog conversion and vice versa, necessary for transmitting data over various types of media.

**Cable Management**:
- **Definition**: Cable management involves the organization and arrangement of cables for efficiency and ease of maintenance in a network.
- **Benefits**: Proper cable management is essential for reducing clutter, improving airflow, and making troubleshooting easier in network infrastructures.

**Multiplexing**:

[Good video](https://www.youtube.com/watch?v=7i-72hsmWTQ)
- **Definition**: Multiplexing is a technique where multiple signals or data streams are combined and transmitted over a single communication channel.
- **Types**: Examples include Time-Division Multiplexing (TDM) and Frequency-Division Multiplexing (FDM), which are used to increase the amount of data that can be sent over a network.

**Routing**:
- **Definition**: Routing is the process of selecting paths in a network along which to send network traffic.
- **Functionality**: Routers, the devices that perform routing, use routing tables and algorithms to determine the most efficient path for data packets to reach their destination.

## IP Address

Historically 4 bytes, now 6 bytes. 4 bytes is 32 bits, 6 bytes is 48 bits, uniquely identifying you computer on the network.

## Port

Programs talk through prots, which are numbered 0-65535 and are associated with the TCP or UDP protocol.

Since `multiple programs can be running on a computer at the same time`, ports are used to identify which program a message is for.

## TCP

Transmission Control Protocol, responsible for reliable, in-order data transmission. From a higher-up perspective, makes a packet-switched network look like a circuit-switched network.

TCP uses port numbers to identify senders and receivers of data.

## What is Network Interface?


1. **Physical Hardware Connection**:
   - A network interface is the point of interconnection between a computer and a network. It's a piece of hardware, often a network card (like a wired Ethernet card or a wireless adapter) that enables a computer to connect to a network.

2. **Types of Interfaces**:
   - **Wired Ethernet Interface**: Connects to a network via an Ethernet cable. Common in desktops and laptops for wired network connections.
   - **Wireless Ethernet Interface (Wi-Fi Adapter)**: Allows a device to connect to a wireless network. Present in most modern laptops, smartphones, and many other devices.

### Interfaces in Routers

1. **Router Interfaces**:
   - Routers typically have multiple interfaces to connect to different networks. For example, a home router usually has at least two main interfaces:
     - **LAN (Local Area Network) Interface**: Connects to your home network (like your computers, smartphones, etc.).
     - **WAN (Wide Area Network) Interface**: Connects to the external internet, typically via a connection provided by an ISP (Internet Service Provider).


## MAC Address

1. **Hardware Identifier**: MAC addresses are unique identifiers assigned to network hardware, like `Ethernet cards` and `Wi-Fi adapters`. They are used for identifying devices within a local network.

2. **Format and Length**:
   - MAC addresses are 6 bytes (48 bits) long.
   - Typically represented in hexadecimal format, like `aa:bb:cc:dd:ee:ff`.
   - Each byte is two hexadecimal characters, separated by colons or hyphens.

3. **Assignment and Uniqueness**:
   - MAC addresses are assigned by the manufacturer of the network interface card and are embedded into the hardware.
   - They are designed to be globally unique so that every network device has a distinct address.

4. **Function**:
   - Used for network activities at the data link layer (Layer 2 in the OSI model).
   - Essential for processes like Ethernet frame transmission within a local network.

## Network cards and Adapters

### Network Cards (NICs - Network Interface Cards)

1. **Hardware Device**: A network card, or NIC, is a hardware component that enables a computer to connect to a network.

2. **Types**:
   - **Ethernet Cards**: Used for wired network connections. They have a port where an Ethernet cable can be connected, linking the computer to a network device like a router or switch.
   - **Wireless Adapters**: Used for wireless network connections. These are common in laptops and allow them to connect to Wi-Fi networks.

3. **Connection to Computer**:
   - Can be integrated into the motherboard or added as an expansion card in an available slot (like PCI or PCIe in desktop computers).
   - In laptops, NICs are typically built-in, either as part of the motherboard or as a small internal expansion card.

### Network Adapters

1. **Broader Term**: The term "network adapter" is more encompassing and can refer to any device that allows a computer to connect to a network, including NICs.

2. **Variety of Forms**:
   - Can be internal (like NICs) or external. External adapters can connect via USB or other ports.
   - In laptops, network adapters (especially for Wi-Fi) are often integrated into the system and not visible as separate cards.

### Clarifications

- **Interchangeable Terms**: While the terms "network card" and "network adapter" are often used interchangeably, "network adapter" is a broader term that includes any device enabling network connectivity, whether it's a card, a USB dongle, or an integrated component.
- **Laptops and Tablets**: Modern laptops and tablets usually come with built-in wireless network adapters. Many also have built-in Ethernet adapters, though this is less common in ultra-thin models.


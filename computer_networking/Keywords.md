# Keywords

## Switching 

### Switching in Telecommunications and Networking

**Switching** is a key process in telecommunications and networking that involves directing data signals or voice calls between different points within a network. It is fundamental to the operation of both telephone and computer networks, enabling efficient communication and data transfer. Switches, the devices that perform this function, determine the best path for data to travel to reach its intended destination.

### Circuit Switching

**Circuit Switching** is a type of network switching where a dedicated communication path or circuit is established between two endpoints for the duration of a call or data transfer session. This method was traditionally used in telephone networks. Key characteristics include:
- **Dedicated Path**: A continuous physical connection is established for the entire duration of the communication.
- **Exclusive Resource Allocation**: Network resources (like bandwidth) along the established path are exclusively reserved for the connected parties.
- **Consistent Quality**: Provides a high and consistent quality of service, ideal for voice calls.
- **Inefficiency in Resource Usage**: Can be inefficient, as the dedicated path remains underutilized when no data is being transmitted.

### Packet Switching

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

## Note on Packet-Switched Networks and Statistical Multiplexing

**Packet-Switched Networks - Key to Efficiency**:
- **Fundamental Question**: How can numerous hosts share a network, especially simultaneously? The answer lies in the efficient use of network resources through packet switching and multiplexing.

**Multiplexing - Sharing Network Resources**:
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

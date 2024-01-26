# Ethernet And Wifi

## What is media access control (MAC) protocol?

Ethernet and WiFi are examples of multi-access (or shared medium) network technologies. In such systems, multiple devices (or hosts) use the `same communication medium` (like a cable for Ethernet or a wireless spectrum for WiFi) to send and receive data. Let's break down the key points mentioned in your statement:

1. **Broadcast Medium, Shared by Many Hosts**:
   - In a broadcast or multi-access network, the communication channel is shared among multiple devices.
   - For Ethernet, this traditionally meant that all devices were connected to the same physical cable (`though modern Ethernet networks use switches to avoid this`).
   - For WiFi, devices share the same wireless frequency band.

2. **Simultaneous Transmissions Cause Collisions**:
   - When two or more devices transmit data at the same time on the same channel, their signals interfere with each other. This event is known as a collision.
   - Collisions are particularly problematic in older Ethernet networks and in WiFi networks, where only one device can successfully transmit at a time on the same channel.

3. **Collisions Destroy the Data**:
   - When a collision occurs, the data from the colliding transmissions becomes corrupted or lost, as the signals become mixed up and indistinguishable from each other.
   - This necessitates some mechanism to detect and recover from such events.

4. **Media Access Control (MAC) Protocols are Required**:
   - MAC protocols are a set of rules or methods used to control access to the network medium.
   - They `define how devices in a shared medium network take turns to transmit data and how they detect and respond to collisions`.

## Strategies for Media Access Control

The strategies for media access control (MAC) in shared medium networks can be broadly categorized into three types: channel partitioning, taking turns, and contention. Each of these strategies has a different approach to handling the challenge of multiple devices trying to communicate over a shared communication channel.

### 1. Channel Partitioning:

- **Concept**: This strategy involves dividing the network resource (such as bandwidth or time) into smaller, distinct portions. Each portion is then allocated to a different host, preventing collisions by ensuring that only one host transmits over a given portion at a time.

- **Examples**:
  - **Time Division Multi-Access (TDMA)**: In TDMA systems, such as in some cellular networks, the time is divided into slots, and each slot is assigned to a different user. Only the user who owns the current time slot transmits, effectively eliminating collisions.
  - **Frequency Division Multi-Access (FDMA)**: FDMA divides the frequency band into smaller bands and allocates each band to a different user. Since each user transmits on a different frequency, simultaneous transmissions do not interfere with each other.

### 2. Taking Turns:

- **Concept**: This approach involves coordinating shared access to the medium by taking turns. It reduces the chance of collisions by controlling which device has the right to transmit at a given time.

- **Example**:
  - **Token Ring Networks**: In token ring networks, a special data packet called a "token" circulates around the network. A device can transmit data only when it has the token, ensuring orderly access to the medium. Once a device has finished transmitting, it passes the token to the next device in the ring.

#### Downside of Taking Turns:

1. `single point of failure`: If the token is lost or corrupted, the network stops functioning.

2. `scalability`: As the number of devices increases, the time it takes for a device to receive the token increases, reducing the network's efficiency.

3. `bandwidth utilization`: In a Token Ring network, only one device can transmit at a time, which might lead to underutilization of available bandwidth, especially if many nodes have little or no data to send.

### 3. Contention:

- **Concept**: Contention-based strategies allow collisions to occur but employ methods to detect, recover, and minimize their impact. These methods are typically used in environments where it's impractical or inefficient to strictly coordinate access.

- **Examples**:
  - **Ethernet**: Traditional Ethernet networks use Carrier Sense Multiple Access with Collision Detection (CSMA/CD). Devices listen to the medium before transmitting to avoid collisions and stop transmitting if a collision is detected, followed by a random backoff algorithm before reattempting.
  - **WiFi**: WiFi networks use Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA). Devices sense the medium and attempt to avoid collisions by waiting for a clear channel and employing acknowledgments and retransmissions.


## Contention Protocols Evolution

### ALOHA
- Developed in the 70’s for packet radio networks
### Slotted ALOHA
- Start transmissions only at fixed time slots
- Significantly fewer collisions than ALOHA
### Carrier Sense Multiple Access / Collision Detection (CSMA/CD) 
- Start transmission only if the channel is idle
- Stop ongoing transmission if collision is detected
### Carrier Sense Multiple Access / Collision Avoidance (CSMA/CA)
- Can’t always detect collisions a priori, so try to avoid them

## ALOHA

The ALOHA protocol, particularly in the context of a radio broadcast network with multiple stations, is a simple yet foundational method for managing how multiple devices access a shared communication medium. Here's an explanation of its operation:

### Topology: Radio Broadcast with Multiple Stations

- **Radio Broadcast Network**: In this setup, multiple stations (or devices) communicate over a shared radio frequency. Each station can both transmit and receive data.
- **Shared Medium**: All stations share the same radio channel, meaning that if multiple stations transmit simultaneously, their signals can interfere with each other.

### ALOHA Protocol Operation

1. **Immediate Transmission**:
   - In ALOHA, when a station has data to send, it transmits the data packet immediately, without checking if the channel is currently in use. This is known as a "random access" method.

2. **Acknowledgments (ACKs) from Receivers**:
   - When a receiver correctly receives a packet, it sends an acknowledgment (ACK) back to the sender. The ACK is a signal that the packet was successfully received without collision.
   - The acknowledgment process is crucial because it informs the sender about the success or failure of the transmission.

3. **Collision Handling**:
   - **No ACK Indicates Collision**: If the sender does not receive an ACK within a certain time frame, it assumes that a collision occurred. Collisions happen when two or more stations transmit simultaneously, causing their packets to interfere with each other.
   - **Random Wait and Retransmit**: After detecting a collision (inferred from the absence of an ACK), the station waits for a random period before retransmitting the packet. This randomness helps reduce the chances of repeated collisions.

### Key Characteristics and Limitations

- **Simplicity**: ALOHA's main advantage is its simplicity. There are no complex coordination or scheduling mechanisms.
- **Efficiency Issues**: However, this simplicity comes at the cost of efficiency. The likelihood of collisions is high, especially as the number of active stations increases.
- **Throughput Limitation**: Due to frequent collisions and the need for retransmissions, the effective throughput (the rate at which successful transmissions occur) of the network can be quite low.

## Slot ALOHA

The protocol you're describing is Slotted ALOHA, an adaptation of the original ALOHA protocol that improves network efficiency by structuring the time during which hosts can transmit data. Here's an explanation of how Slotted ALOHA works and its requirements:

### Protocol: Slotted ALOHA

1. **Time Division into Slots**:
   - In Slotted ALOHA, time is divided into equal-sized slots. Each slot is typically long enough to accommodate one frame or packet of data.

2. **Transmission Rules**:
   - Hosts (stations in the network) are only allowed to begin transmitting at the start of a time slot. They cannot start sending data in the middle of a slot.
   - This rule ensures that if a collision occurs (when two or more hosts transmit simultaneously), it will involve the entire frame, as all colliding frames are aligned in time.

3. **Collision and Throughput**:
   - **Complete Collisions**: Since transmissions are aligned with time slots, collisions, if they occur, will be between entire frames. This differs from the original ALOHA, where partial collisions could occur.
   - **Improved Throughput**: Slotted ALOHA roughly doubles the throughput compared to the original ALOHA. Theoretically, Slotted ALOHA achieves about 37% efficiency (i.e., 37% of slots carry successful transmissions) versus 18% for ALOHA. This improvement is due to the reduced likelihood of collisions.

> With complete collisions, a transmission that begins in a time slot either succeeds entirely or fails entirely due to a collision. This makes it easier to detect and manage collisions, as any frame that doesn't receive an acknowledgment can be retransmitted in a subsequent slot.

> In the original ALOHA, a new transmission could collide with any ongoing transmission, whereas in Slotted ALOHA, it can only collide with other transmissions that start in the same time slot.

4. **Requirement for Synchronized Clocks**:
   - For Slotted ALOHA to work effectively, all hosts in the network must have synchronized clocks. This synchronization ensures that all hosts agree on when each time slot begins and ends.
   - Clock synchronization is critical because if hosts are not aligned in their timing, the benefit of having time slots (reduced collision probability) is negated, as hosts might start their transmissions at different times.

## Broadcase Ethernet (Old)

Carrier Sense : `all the nodes can distinguish between an idle and a busy link`

**Ethernet CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**

- **Definition:** Ethernet CSMA/CD, or Carrier Sense Multiple Access with Collision Detection, is a network protocol used in Ethernet networks to manage access to the shared communication medium, typically a coaxial cable or twisted-pair cable.

- **Key Insight:** CSMA/CD is based on the idea that in a wired protocol, it is possible to sense the medium (the communication channel) to determine its availability.

- **Algorithm:**
  1. **Carrier Sensing:** Devices on the network first listen to the communication medium (the cable) to detect the presence of any carrier signals. If a carrier signal (indicating another host is currently transmitting) is detected, the device waits for it to end before attempting to transmit its own data. This is done to avoid collisions.

  2. **Transmission:** If no carrier signal is detected, the device proceeds to send its data frame onto the medium. However, it continues to monitor the medium for the presence of any collision during the transmission.

  3. **Collision Detection:** Simultaneously, the transmitting device checks whether it senses a collision during its transmission. If a collision is detected (e.g., because another host started transmitting at the same time), the device immediately aborts its transmission.

  4. **Collision Resolution:** In the event of a collision, the devices involved perform a process called exponential backoff, where they wait for a random period before reattempting to transmit their data. This randomized backoff reduces the likelihood of repeated collisions.

- **Purpose:** The purpose of CSMA/CD is to manage access to the shared network medium and prevent multiple devices from attempting to transmit simultaneously, which would result in data collisions and degraded network performance.

- **Efficiency:** CSMA/CD helps improve the efficiency of Ethernet networks by ensuring that devices wait for an idle channel before transmitting, reducing the chances of collisions. However, it is less relevant in modern Ethernet networks as most use switched Ethernet (CSMA/CD is mainly associated with Ethernet over a shared medium).

- **Legacy Protocol:** While CSMA/CD was a fundamental part of early Ethernet networks, it is no longer used in modern Ethernet networks, which predominantly rely on switched Ethernet where collisions are less likely.

In summary, Ethernet CSMA/CD is a protocol designed for shared Ethernet networks, allowing devices to sense the medium to determine its availability, avoid collisions, and manage network access efficiently. However, it is largely a legacy protocol, as modern Ethernet networks are primarily switched Ethernet, where collisions are less of a concern.

## Ethernet Header
The structure of an Ethernet frame header, including the preamble and start frame delimiter (SFD), is as follows:

1. **Preamble:** The preamble is 7 bytes long and consists of the bit pattern 10101010. Its purpose is to signal the start of a frame and to help synchronize the receiver's clock with the incoming data. The alternating bit pattern is used to ensure that the receiver's clock can lock onto the incoming data without knowing the data rate in advance.

2. **Start Frame Delimiter (SFD):** The SFD is 1 byte (8 bits) long and has the bit pattern 10101011. It immediately follows the preamble and marks the end of the preamble and the start of the frame's actual data.

3. **Source and Destination MAC Addresses:** The Ethernet frame includes the source MAC address (the sender's MAC address) and the destination MAC address (the intended recipient's MAC address). These addresses are 6 bytes (48 bits) each and uniquely identify network interfaces on Ethernet devices.

4. **Broadcast Address:** The broadcast MAC address, FF:FF:FF:FF:FF:FF, is used to address a frame to all devices on the network segment. Any device with a matching MAC address will accept the frame.

5. **Minimum Packet Length:** Ethernet frames must have a minimum length of 64 bytes (excluding the preamble and SFD). If a frame is shorter than 64 bytes, it is padded with additional bytes to meet this minimum requirement. This padding ensures that the frame is long enough to allow for proper collision detection in shared Ethernet networks (CSMA/CD).

The preamble and SFD are essential for synchronization and framing purposes in Ethernet communication. They help receivers identify the start of a frame and establish synchronization with the incoming data stream. The specific bit patterns used in the preamble and SFD are part of the Ethernet standard and are designed to serve these synchronization and signaling functions.

## CSMA/CD Collisions

Collisions in Ethernet networks can occur when two or more devices attempt to transmit data simultaneously on a shared communication medium. However, in modern Ethernet networks that operate in full-duplex mode, collisions are rare or eliminated because devices can transmit and receive data simultaneously. Nonetheless, let's explain the concept of collisions, how they are detected, and the role of distance, propagation delay, and frame length in collision detection in traditional Ethernet networks that used CSMA/CD (Carrier Sense Multiple Access with Collision Detection).

1. **Collisions Can Occur:**
   - In traditional Ethernet networks (e.g., 10BASE-T, 100BASE-TX), multiple devices share the same communication medium, such as a coaxial cable or a segment of twisted-pair cable.
   - When two or more devices attempt to transmit data at the same time, their signals interfere with each other, resulting in a collision. This interference causes the data on the medium to become garbled.

2. **Collision Detection:**
   - Ethernet networks using CSMA/CD employ collision detection mechanisms to quickly identify and handle collisions.
   - When a device transmits data, it continues to monitor the medium for the presence of a collision while it transmits.
   - If a collision is detected, the transmitting device immediately aborts its transmission to prevent further data corruption.
   - The collision detection mechanism is based on the fact that devices can detect that the signal they are transmitting is different from the signal they are receiving, which indicates a collision.

3. **Role of Distance:**
   - The distance between devices on an Ethernet network segment plays a role in collision detection. Longer segments may introduce a delay in the time it takes for a signal to propagate from one end to the other.
   - Devices need to be able to detect collisions within a certain timeframe to ensure efficient collision resolution. Longer segments may require more time for collision detection to work effectively.

4. **Propagation Delay:**
   - Propagation delay refers to the time it takes for a signal to travel from one end of the network segment to the other.
   - If the propagation delay is too long, it may affect the ability of devices to detect and abort collisions promptly.
   - Ethernet standards specify a maximum round-trip propagation delay that a network segment can have to ensure that collision detection operates effectively.

5. **Frame Length:**
   - The length of the data frames being transmitted can also affect collision detection.
   - Longer frames take more time to transmit, increasing the window of opportunity for collisions to occur.
   - Ethernet standards define a minimum frame length (e.g., 64 bytes) to ensure that devices have adequate time to detect collisions before completing their frame transmissions.

In summary, collisions can occur in Ethernet networks when devices share a communication medium. In traditional Ethernet networks using CSMA/CD, collisions are detected and promptly aborted. The distance between devices, propagation delay, and frame length all play a role in ensuring that collision detection mechanisms operate effectively to maintain network efficiency and reliability. However, in modern Ethernet networks operating in full-duplex mode, collisions are minimized or eliminated, making collision detection mechanisms largely irrelevant.


### Exponential backoff

Certainly! Here's a note summarizing the concept of exponential backoff in networking:

**Exponential Backoff in Networking**

- Exponential backoff is a network protocol or algorithm used to manage and resolve contention or collisions in shared communication networks.
- It is commonly associated with the CSMA/CD (Carrier Sense Multiple Access with Collision Detection) protocol used in Ethernet networks.
- When a sender detects a collision during data transmission, it initiates the exponential backoff process to avoid immediate retransmission and potential repeated collisions.
- Key components of exponential backoff include:
  - **Jam Signal:** After detecting a collision, the sender sends a jam signal to inform all hosts on the network of the collision.
  - **Backoff Value 'k':** The sender selects a random backoff value 'k' from a predefined range based on the number of sequential collisions ('n'). 'k' determines the waiting time before retransmission.
  - **Time Interval:** The backoff time is calculated as 'k' multiplied by a fixed time interval (e.g., 51.2 microseconds per contention slot).
  - **Randomness and Fairness:** Exponential backoff introduces randomness into retransmission attempts, reducing the likelihood of repeated collisions and promoting fair access to the network.
  - **Limit on Retransmissions:** There is often a limit on the number of retransmissions (e.g., capped at 10). After reaching this limit, the frame may be dropped.
  - **Contention Slots:** Backoff time is divided into contention slots, where each slot corresponds to the fixed time interval.
- Exponential backoff helps improve network efficiency and fairness by preventing immediate retransmissions and encouraging devices to wait random intervals before retrying.
- It is particularly useful in shared communication media where multiple devices contend for access to the network.

Exponential backoff is a fundamental component of collision detection and resolution mechanisms in Ethernet networks and plays a crucial role in maintaining effective network performance.


## Long live ethernet

You are correct in your description of modern Ethernet networks:

1. **Switched Ethernet:** Modern Ethernet networks are predominantly switched Ethernet. Ethernet switches are used to create logical segments within a network, allowing devices to communicate without the need for collision detection (CSMA/CD). This results in more efficient and higher-performing networks.

2. **High Speeds:** Ethernet networks commonly operate at speeds of 1 Gigabit per second (1Gbps) and 10 Gigabits per second (10Gbps). Additionally, 100 Gigabit Ethernet (100Gbps) has become more common, and higher-speed Ethernet standards are continually being developed.

3. **Packet Header:** Ethernet still uses the same fundamental packet header structure, which includes source and destination MAC addresses, frame type or length, and other fields. This consistency in packet structure allows for compatibility across different Ethernet standards.

4. **Full Duplex:** Modern Ethernet operates in full-duplex mode, which means that devices can send and receive data simultaneously without the risk of collisions. This greatly improves network performance and efficiency.

5. **Auto-Negotiation:** Ethernet devices often support auto-negotiation, which allows them to automatically determine and configure the best possible connection speed and duplex mode when connecting to a network. This feature ensures compatibility between devices with varying capabilities.

6. **Power over Ethernet (PoE):** Ethernet can also carry electrical power in addition to data. PoE allows devices like IP phones, security cameras, and access points to receive power over the Ethernet cable, simplifying installation and reducing the need for separate power sources.

These features make modern Ethernet networks highly versatile, capable of supporting high data rates, and suitable for a wide range of applications, from home networks to data centers and beyond. The use of switched Ethernet and full-duplex communication has significantly improved network efficiency and reliability, making Ethernet a foundational technology in today's digital world.
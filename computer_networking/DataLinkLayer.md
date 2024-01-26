# Data Link Layer 

In networking, the Data Link Layer plays a crucial role in facilitating communication between network nodes. One of the key components in this layer is the network adapter (often referred to as a network interface card or NIC), which enables nodes to exchange data frames. Here are some key points to note regarding the role of network adapters and the challenge of recognizing frames:

- **Network Adapters:** Network adapters are hardware components or cards installed in network nodes (e.g., computers, servers) that enable them to connect to a network. These adapters handle the physical transmission of data frames over network links.

- **Frame Transmission:** When a node (e.g., Node A) wishes to transmit a data frame to another node (e.g., Node B), it instructs its network adapter to transmit the frame from the node's memory. This action initiates the process of sending a sequence of bits over the network link.

- **Frame Reception:** On the receiving end (Node B), the network adapter collects the incoming sequence of bits arriving on the network link and processes them to identify and extract the corresponding data frame. The frame is then deposited into Node B's memory for further processing.

- **Frame Recognition Challenge:** A fundamental challenge faced by network adapters is recognizing the `boundaries of data frames`. In other words, determining where each frame begins and ends within the continuous stream of bits on the network link is crucial for proper frame reception and data integrity.

## **Note: Framing Approaches in Networking Protocols**

In networking protocols, the framing approach used to delineate the boundaries of data frames is crucial for accurate data transmission and reception. Different protocols employ various framing techniques, and here we discuss three common approaches: Byte-Oriented Protocols (such as BISYNC, PPP, and DDCMP), Sentinel-Based Approaches, and Byte-Counting Approach.

### **Byte-Oriented Protocols (BISYNC, PPP, DDCMP):**
- Byte-oriented protocols `treat each frame as a collection of bytes` (characters) rather than individual bits.
- Examples of such protocols include Binary Synchronous Communication (`BISYNC`), Digital Data Communication Message Protocol (`DDCMP`), and Point-to-Point Protocol (`PPP`).
- Sentinel characters are used to indicate the start and end of frames. For instance, BISYNC uses SYN (synchronization), STX (start of text), and ETX (end of text) characters.
- Character stuffing is employed to handle special characters (e.g., ETX) within the frame's data portion. Escaping characters (e.g., DLE - data-link-escape) ensure they are correctly interpreted.
- Error detection mechanisms like CRC (cyclic redundancy check) are often included in the frame format.

#### **Sentinel-Based Approaches:**
- Sentinel-based framing relies on special characters (sentinels) to mark the start and end of frames.
- For example, BISYNC uses SYN, STX, and ETX characters.
- The challenge with this approach is ensuring that the sentinel characters do not accidentally appear within the data portion of the frame. `Character stuffing` is used to address this issue by inserting extra characters (e.g., DLE) in the data portion.

##### Downside of character stuffing:
> Character stuffing `increases the size of the transmitted data `and can reduce the overall efficiency of the communication channel.

> If there are `errors in the sentinel characters` themselves (e.g., due to noise or corruption)

#### **Byte-Counting Approach:**
- The byte-counting approach includes a field in the frame header that specifies the number of bytes in the frame's body.
- An example of this approach is the DECNET's DDCMP protocol.
- The COUNT field indicates how many bytes are contained in the frame's body.
- A potential issue with this approach is that transmission errors can corrupt the COUNT field, leading to a failure in correctly detecting the frame's end. This is known as a framing error.
- In the case of a framing error, the receiver accumulates bytes according to the corrupted COUNT field until it detects a frame error using an error detection field. The receiver then waits for the next SYN character to start collecting the next frame.


## **Note: Bit-Oriented Protocols and Bit Stuffing in HDLC**

Bit-oriented protocols, unlike byte-oriented ones, consider the frame as a collection of individual bits, without concern for byte boundaries. An example of a bit-oriented protocol is the High-Level Data Link Control (HDLC) protocol, originally developed by IBM as the Synchronous Data Link Control (SDLC) protocol and later standardized by ISO.

**HDLC Frame Format:**
- HDLC uses a bit sequence of 01111110 to denote both the beginning and the end of a frame.
- This sequence is also transmitted during idle times to help keep the sender and receiver clocks synchronized.
- Bit stuffing is employed to handle the potential occurrence of the 01111110 sequence within the frame's body.
- Bit stuffing ensures that the frame's structure is not disrupted, and it plays a role similar to character stuffing used in byte-oriented protocols.

**Bit Stuffing in HDLC:**
- Bit stuffing in HDLC works as follows:
  - On the sending side, whenever five consecutive 1s have been transmitted from the message body (excluding the 01111110 sequence), the sender inserts a 0 before transmitting the next bit.
  - On the receiving side, when five consecutive 1s arrive, the receiver examines the next bit.
    - If the next bit is a 0, it must have been stuffed, so the receiver removes it.
    - If the next bit is a 1, the receiver distinguishes between two cases:
      - End-of-frame marker (if the last 8 bits observed are 01111110).
      - Error in the bit stream (if the last 8 bits observed are 01111111). In this case, the whole frame is discarded, and the receiver waits for the next 01111110 before resuming reception.

**Variable Frame Size:** One notable characteristic of bit stuffing (and character stuffing) is that the size of a frame depends on the data being sent in the payload. Frames can have different sizes based on the content of their payloads, making it impossible to ensure that all frames are of exactly the same size, especially when the payload contains arbitrary data.

While bit stuffing and the use of sentinel sequences help maintain frame synchronization and handle certain framing scenarios, it's important to acknowledge that they introduce complexities related to variable frame sizes and the potential for errors, which must be managed within the protocol's design and implementation.

### Why bit oriented frrame is variable in size?

Why frame size in bit-oriented protocols is variable:

1. **Bit-Oriented Nature:** Bit-oriented protocols do not rely on byte boundaries to delineate frames; they view the frame as a sequence of individual bits. This means that the frame's content can vary based on the specific bits in the payload.

2. **Bit Stuffing:** To ensure proper frame synchronization and handle sentinel sequences, bit-oriented protocols use bit stuffing. Bit stuffing introduces extra bits (0s) into the frame when specific bit patterns (e.g., five consecutive 1s) are encountered. These stuffed bits are added as needed to prevent the sentinel sequence from appearing within the payload. As a result, the size of the frame can change dynamically based on the data content.

3. **Variable Payload Size:** The payload of a frame in a bit-oriented protocol can contain arbitrary data, and the size of the payload depends on the actual data being transmitted. For example, one frame may have a relatively small payload, while another frame may have a larger payload, all depending on the data that needs to be sent.

Due to these characteristics, bit-oriented protocols inherently support variable frame sizes. The frame size is not explicitly negotiated but rather adapts to the payload's content and the need for bit stuffing to maintain proper frame structure and synchronization.

While this flexibility allows bit-oriented protocols to accommodate a wide range of data types and sizes, it also presents challenges in `managing variable frame lengths and ensuring efficient error detection and correction mechanisms`. As such, designers of bit-oriented protocols must carefully consider these factors when defining the protocol's behavior and frame format.

## Error Detection and Correction

In networking, dealing with bit errors is essential to ensure the integrity of data transmission. Errors can occur due to factors like electrical interference or thermal noise. Detecting and, when possible, correcting these errors is crucial to maintain data accuracy and reliability in network communication.

**Error Detection Techniques:**
- Error detection involves identifying the presence of errors in transmitted data frames.
- Common error detection techniques include techniques like parity checking, cyclic redundancy check (CRC), and checksums.
- These techniques use mathematical calculations and patterns to determine whether the received data matches the expected data.

**Handling Errors:**
- When errors are detected, two basic approaches can be taken:
  1. **Retransmission:** The recipient notifies the sender that the message was corrupted, and the sender retransmits a copy of the message. In cases where bit errors are rare, the retransmitted copy is likely error-free.
  2. **Error Correction:** Some error detection algorithms, particularly those using error-correcting codes, enable the recipient to reconstruct the correct message even after corruption. This eliminates the need for retransmission.

### Error Detection 

#### `Naïve Error Detection Approach`

The naïve error detection approach suggests `sending two copies` of each data frame and then comparing them to detect errors. If the two copies do not match, it is assumed that an error has occurred. While this approach may seem intuitive, it has significant drawbacks that make it impractical for error detection in networking.

**Drawbacks of Naïve Error Detection:**

1. **High Overhead:** Sending two copies of each frame results in an extremely high overhead. In fact, the overhead is 50% because for every data frame, an additional identical copy is sent. This means that half of the transmitted data is used solely for error detection, which is highly inefficient.

2. **Inadequate Error Protection:** Despite the high overhead, this approach provides poor protection against errors. It relies solely on a simple comparison of the two copies. If both copies are corrupted in the same way, the error detection mechanism may not detect the error, leading to a false sense of data integrity.

3. **Increased Risk of Bit Errors:** Sending twice the data increases the chance for bit errors. More data on the network means more opportunities for individual bits to be corrupted during transmission. This exacerbates the problem of errors rather than mitigating it.


#### `Two-Demensional Parity Check`

**Note: Two-Dimensional Parity for Error Detection**

Two-dimensional parity is an error detection technique used in data communication. It is an extension of the one-dimensional parity concept, where an extra bit is added to a data byte to ensure a specific number of 1s (either odd or even) in the byte. Two-dimensional parity extends this concept to multiple bytes within a frame, providing enhanced error detection capabilities.

> One-dimensional parity is bad because if `0 1 becomes 1 0`, it will not be detected.

**Key Points about Two-Dimensional Parity:**

1. **One-Dimensional Parity:** In one-dimensional parity, an extra bit is added to a byte of data to achieve either odd or even parity. Odd parity sets the extra bit to 1 if needed to make the total number of 1s in the byte odd, while even parity sets the extra bit to 1 if needed to make the total number of 1s in the byte even.

2. **Two-Dimensional Parity:** Two-dimensional parity extends the concept of parity to multiple bytes within a frame. It calculates parity not only for individual bytes but also for each bit position across all bytes in the frame.

3. **Example:** In a frame containing multiple bytes, each bit position (bit 0, bit 1, bit 2, etc.) is checked for parity across all the bytes. An extra parity byte is added to the entire frame to provide additional error detection. The parity bit for each byte ensures that the number of 1s in that byte is either odd or even, depending on the chosen parity scheme.

4. **Enhanced Error Detection:** Two-dimensional parity is effective at detecting various types of errors, including `1-bit, 2-bit, 3-bit, and most 4-bit errors`. This makes it more robust than simpler error detection techniques like repetition codes.

5. **Redundant Information:** Implementing two-dimensional parity involves adding redundant information to the data. For example, if a 42-bit message is protected using two-dimensional parity, an additional 14 bits of redundant information are added to achieve stronger error detection capabilities.

6. **Protection Against Common Errors:** Two-dimensional parity provides reliable protection against common errors, making it suitable for applications where data integrity is crucial, such as in data transmission over communication channels.

#### Checksum

**Checksums for Error Detection in Networking**

Checksums are a commonly used technique for error detection in networking. The basic idea behind checksums is to add up the values of all the bytes in the data to create a sum, which is then included in the frame. Checksums rely on ones-complement arithmetic and are used in protocols like UDP, TCP, and IP. Here's an explanation of each aspect:

**Idea Behind Checksums:**
- Checksums are used to detect errors in transmitted data frames.
- The concept involves adding up the values (in binary) of all the bytes in the data portion of a frame to calculate a sum.
- This sum is then included in the frame along with the data.

**Ones-Complement Arithmetic:**
- Checksums typically use `ones-complement` arithmetic to calculate the sum.
- In ones-complement arithmetic, negative numbers are represented by inverting all the bits of the positive number.
- For checksum calculation, each byte's value is added to the running sum in ones-complement form.

**Lower Overhead than Parity:**
- Checksums have lower overhead compared to some other error detection techniques like parity.
- Parity, which involves adding an extra bit to each byte for even or odd parity, can result in higher overhead (additional bits) per frame.
- In contrast, a checksum typically involves a fixed number of bits, often 16 bits, per frame, which results in lower overhead.

**Not Resilient to Multi-Bit Errors:**
- Checksums have a limitation—they are not resilient to multi-bit errors.
- If multiple bits in the data or checksum itself are corrupted during transmission, the checksum may not detect the error.
- Checksums are more effective at detecting single-bit errors or small errors in the frame.

**Usage in UDP, TCP, and IP:**
- Checksums are widely used in networking protocols, including UDP (User Datagram Protocol), TCP (Transmission Control Protocol), and IP (Internet Protocol).
- In these protocols, checksums are calculated and included in the headers of data packets to ensure data integrity during transmission.
- Checksums provide a basic level of error detection in these protocols, helping to identify and discard corrupted packets.

> Checksums are used in the data link layer as well

#### Cyclic Redundancy Check (CRC)

#### Hashes

## **Short Note on Error Detection in Network Layers**

Error detection is a critical aspect of network communication, implemented across various layers of the network stack, each serving different roles:

1. **Data Link Layer**: Focuses on detecting errors in the physical transmission of frames over a medium (e.g., Ethernet, wireless). Common methods include Cyclic Redundancy Check (CRC) and checksums, ensuring the integrity of each frame.

2. **Transport Layer**: Ensures end-to-end integrity of messages or data streams. Protocols like TCP use checksums for each segment, verifying the entire data transmission from one end system to another.

3. **Application Layer**: Some applications implement their own error detection to guarantee data integrity, especially where high accuracy is critical. This can involve checksums or hashes for verifying file integrity post-transfer.

4. **Network Layer**: While less common, error detection can occur at this layer too, such as the IP header checksum, which verifies the integrity of the IP header.

Each layer's approach to error detection ensures robust, layered protection, ensuring data integrity from origin to destination. The Data Link Layer addresses single-link errors, while the Transport Layer and beyond focus on broader, end-to-end data integrity.

## From Detection to Correction

1. **Corrupted Frames and Error Detection**: In data communication, frames (units of data) can become corrupted during transit. Error detection codes like Cyclic Redundancy Check (CRC) are used to identify such errors. Some error codes can also correct errors, but often they introduce too much overhead (additional data or processing) to handle the variety of errors that can occur on a network link. Therefore, many corrupt frames are simply discarded.

2. **Reliable Transmission at Different Network Layers**: The passage notes that while reliable transmission can be provided at the link level (the level where data packets are encoded and decoded into physical signals), it's often omitted in modern link technologies. Instead, reliability is frequently achieved at higher levels of the network stack, such as the transport layer (TCP in the Internet protocol suite is an example) and sometimes even at the application layer. The location of reliable delivery in the network stack is debated and depends on various factors.

3. **Achieving Reliability with Acknowledgments and Timeouts**:
    - **Acknowledgments (ACKs)**: These are small control frames sent back to the sender to indicate that a frame has been successfully received. They can be standalone or piggybacked onto data frames traveling in the opposite direction.
    - **Timeouts**: If an acknowledgment for a sent frame is not received within a reasonable time, the sender will assume the frame was lost or corrupted and will retransmit it. This waiting period is known as a timeout.

4. **Automatic Repeat Request (ARQ)**: The general strategy of using acknowledgments and timeouts for reliable data transmission is called `Automatic Repeat Request`. The passage mentions that there are various ARQ algorithms, which are methods to manage how acknowledgments and retransmissions are handled to ensure reliable delivery. These algorithms determine when and how to resend data and acknowledge receipt.


### Basic Concept of Stop-and-Wait ARQ:

> How does the sender know when to send the next frame?


1. **One Frame at a Time**: The sender sends a single frame and then stops to wait for an acknowledgment (ACK) from the receiver.

2. **Waiting for Acknowledgment**:
   - If the ACK is received before a timer (set for a specific time period) expires, the sender proceeds to send the next frame.
   - If the ACK is not received before the timer expires (indicating potential loss or error), the sender retransmits the original frame.

3. **Scenarios Illustrated in Figure 2.17**:
   - **(a)** ACK is received before the timer expires. This is the ideal case.
   - **(b)** The original frame is lost. The sender retransmits after timeout.
   - **(c)** The ACK is lost. The sender retransmits after timeout.
   - **(d)** The timeout period is set too short, leading to premature retransmission.

4. **Timeline Representation**: This process is depicted on a timeline, with the sending side on the left, the receiving side on the right, and time flowing from top to bottom.

### Addressing Duplicates in Stop-and-Wait:

- **Issue of Duplicate Frames**: A problem arises if the sender transmits a frame and the receiver acknowledges it, but the ACK is lost or delayed. The sender, not receiving the ACK, retransmits the original frame. However, the receiver, having already received and acknowledged the first frame, might interpret the retransmission as a new frame, leading to duplicate frame delivery.

- **Solution - 1-bit Sequence Number**:
  - To solve this, each frame's header includes a 1-bit sequence number, which can be either 0 or 1.
  - The sequence numbers alternate for each frame (0, 1, 0, 1, ...).
  - This way, if the sender retransmits frame 0, the receiver can recognize it as a duplicate of frame 0 (not a new frame 1) and ignore it.
  - Despite ignoring the duplicate, the receiver still sends an ACK for it, in case the first ACK was lost.

### Summary:

Stop-and-Wait ARQ is a fundamental method for reliable transmission in data communications. It involves sending one frame at a time and waiting for its acknowledgment before sending the next. If acknowledgments are not received in time, the frame is retransmitted. The inclusion of a 1-bit sequence number in each frame's header helps the receiver distinguish between new frames and retransmissions, thus avoiding the problem of duplicate frame delivery. This method is simple but can be inefficient, especially over networks with high latency or long distances.


### Bandwidth-Delay Product

The Bandwidth Delay Product is a theoretical measure that indicates the maximum amount of data that should be sent to keep the network link fully utilized**Note on Calculating Maximum Sending Rate using Stop-and-Wait ARQ for a 1.5-Mbps Link with 45-ms RTT**

##### Example :
- **Network Link**: 1.5 Megabits per second (Mbps) bandwidth.
- **Round-Trip Time (RTT)**: 45 milliseconds (ms).

##### Bandwidth Delay Product:
- **Calculation**: Bandwidth × RTT = 1.5 Mbps × 45 ms.
- **Result**: 67.5 kilobits (Kb), or approximately 8 Kilobytes (KB).
- **Interpretation**: The link can theoretically have 8 KB of data in transit at any given time.

##### Stop-and-Wait Protocol Limitation:
- **One Frame at a Time**: The sender transmits one frame and then waits for an acknowledgment before sending the next.
- **Frame Size**: Assuming a frame size of 1 KB.

##### Maximum Sending Rate Calculation:
1. **Frame Size in Bits**: 1 KB = 1024 bytes = 1024 × 8 bits.
2. **Time Per Frame**: Equivalent to the RTT, 45 ms or 0.045 seconds.
3. **Formula**: Bits Per Frame ÷ Time Per Frame.
4. **Calculation**: \( \frac{1024 \times 8 \text{ bits}}{0.045 \text{ seconds}} \).
5. **Result**: 182 kilobits per second (kbps).

##### Interpretation:
- **Utilization of Link's Capacity**: The maximum sending rate under Stop-and-Wait for this link is 182 kbps.
- **Comparison with Link's Capacity**: This rate is approximately one-eighth of the link’s total capacity (1.5 Mbps).
- **Inefficiency**: This demonstrates the inefficiency of the Stop-and-Wait protocol in fully utilizing the link’s capacity, particularly for links with high bandwidth and significant RTT.

##### Conclusion:
- The example illustrates that using Stop-and-Wait ARQ on a high-capacity link with notable delay leads to substantial underutilization of the link's potential throughput. The sender spends most of the time waiting for acknowledgments rather than continuously transmitting data, resulting in a throughput much lower than the link's actual capacity.

## Sliding Window Protocol

> is about allowing multiple frames/packets to be sent before an acknowledgment is required

### Concept:
- **Sliding Window Protocol**: This is an advanced method used in network communication to manage and control the flow of data between a sender and receiver. It's particularly significant in the context of Transmission Control Protocol (TCP) and is used to increase the efficiency of network communication.

### Key Features:
1. **Multiple Outstanding Frames**: Unlike Stop-and-Wait ARQ, the Sliding Window Protocol allows the sender to have multiple unacknowledged (un-ACKed) frames in transit simultaneously.
2. **Window Size**: The number of frames that can be sent before receiving an acknowledgment is known as the "window size." This window slides over the sequence of frames as acknowledgments are received and new frames are sent.
3. **Enhanced Utilization**: This mechanism significantly enhances the utilization of network bandwidth and reduces the idle time compared to Stop-and-Wait ARQ.

### Operation:
1. **Sending Window**: The sender maintains a window that represents the range of frame sequence numbers allowed to be sent but not yet acknowledged.
2. **Receiving Window**: The receiver also maintains a window for frames it expects to receive. This ensures proper sequencing and error control.
3. **Window Adjustment**: As the sender receives ACKs for sent frames, it slides the window forward, allowing more frames to be sent.

### TCP and Sliding Window:
- **TCP Implementation**: TCP, a core protocol of the Internet protocol suite, uses the Sliding Window Protocol to manage data transmission.
- **Reliability and Flow Control**: In TCP, the Sliding Window Protocol is crucial for providing reliable transfer by handling retransmissions, sequencing, and flow control.
- **Dynamic Window Sizing**: TCP dynamically adjusts the window size based on network conditions, such as available bandwidth and latency, to optimize data flow.

### Benefits:
1. **Increased Throughput**: By allowing multiple frames to be in transit, the protocol increases network throughput.
2. **Efficient Use of Network Resources**: It leverages the full capacity of the network, reducing the impact of latency and maximizing data transfer efficiency.
3. **Congestion and Flow Control**: The protocol helps in managing network congestion and controlling the flow of data, preventing buffer overflow and packet loss.

### Conclusion:
- The Sliding Window Protocol is a fundamental concept in network communication, especially in protocols like TCP, enhancing data transfer efficiency by allowing multiple frames to be sent before receiving acknowledgments. Its dynamic nature and ability to adjust to network conditions make it essential for reliable and efficient network communication.

## Should we error check in the data link? 

### End-to-End Argument Overview:

- **Principle**: This concept suggests that certain network functions can only be completely and correctly implemented by the end systems (applications) themselves. 
- **Application in Error Checking**: According to this principle, error checking might be more effectively implemented at the application layer rather than at lower levels like the Data Link Layer.

### Cons of Error Checking in the Data Link Layer:

1. **No Guarantee of Error-Free Transmission**:
   - Despite error checking at the Data Link Layer, errors can still occur at other points in the network.
   - Complete error-free transmission can't be guaranteed solely by the Data Link Layer.

2. **Not All Applications Require It**:
   - Different applications have different needs. Some might require stringent error checking, while others (like streaming services) can tolerate some level of errors.

3. **Additional Overhead**:
   - Implementing error checking adds CPU processing load and increases the size of packets due to additional error-checking data (like CRC codes).
   - This overhead can be significant, especially in high-speed networks.

4. **Need for Buffering and RAM**:
   - Error recovery often requires buffering of data for retransmission, which in turn requires significant amounts of RAM.
   - This can be resource-intensive, especially in systems with limited memory.

### Pros of Error Checking in the Data Link Layer:

1. **Improved Performance Over App-Level Checking**:
   - Handling errors closer to where they occur (e.g., on noisy links) can be more efficient.
   - It potentially offers faster detection and correction of errors compared to leaving this task entirely to the application layer.

2. **Practical Usefulness Over Lossy Links**:
   - In environments where errors are more common (like WiFi, cellular, or satellite communications), Data Link Layer error checking can significantly improve data transmission reliability.
   - It is particularly beneficial for correcting transient errors and maintaining a basic level of reliable communication.

### Conclusion:

Deciding whether to implement error checking in the Data Link Layer involves a trade-off between efficiency, resource utilization, and the specific requirements of the network and its applications. While it can offer improved performance and is especially useful over lossy links, it also introduces additional overhead and cannot guarantee complete error-free transmission. The decision should be based on the network architecture, the nature of the communication links, and the requirements of the applications using the network.
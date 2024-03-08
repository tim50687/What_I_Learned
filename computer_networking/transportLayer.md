# UDP

- Provide a way to send error-free data from one computer to another. (That's it)


The following are not goals of UDP:

- Provide data in order
- Provide data without loss
- Provide data without duplicates

## Same port number on TCP and UDP 
Separate Namespace: Since `TCP and UDP are independent`, an application can use the same port number on TCP and a different application can use the same port number on UDP without conflict. 

For example, a TCP application might use port 4040, and a UDP application might also use port 4040 on the same machine.


## No connection 

With UDP sockets, there are some differences from TCP:

- You no longer call listen(), connect(), accept(), send(), or recv() because there’s no `“connection”`.
- You call sendto() to send UDP data.
- You call recvfrom() to receive UDP data.


## Fragmentation

If any fragment is lost, the entire original packet cannot be reassembled, leading to higher packet loss rates. Since UDP does not provide mechanisms for retransmission (unlike TCP), avoiding fragmentation can significantly improve reliability.

Therefore, 

Avoiding Fragmentation with UDP: To minimize the risk of packet loss, it is often recommended to keep UDP packets small enough to avoid fragmentation, adhering to the `minimum MTU standards` of the Internet.


- Two benefits:
    - Prevent from fragmentation loss
    - Fast: don't have to reassemble the packet

## Broadcast and Multicast
Broadcast and Multicast: UDP supports broadcast and multicast, allowing a packet to be sent to multiple recipients at once, which TCP does not support natively.


# TCP

[good website](https://cabulous.medium.com/tcp-3-way-handshake-and-how-it-works-8c5f8d6ea11b)

## Goals of TCP

- Provide reliable communication
- Simulate a `circuit-like` connection on a packet-switched network
- Provide flow control
- Provide congestion control
- Support out-of-band data

## Overview

1. Make the connection 
2. Transmit data
3. Close the connection


### Make the connection

TCP always send `ACKs` to confirm the receipt of data. (`allowing for retranmission if necessary`)

This involves the famous `three-way handshake`.

### Why Random Initial Sequence Numbers?

The sequence number is a counter used to keep track of every byte sent outward by a host.

#### Connection confusion

##### Scenario: Multiple Connections Between Two Hosts

Imagine you have two computers, Computer A and Computer B. Computer A is sending data to Computer B over two separate TCP connections at the same time. Both connections are using the same source and destination IP addresses and the same source and destination ports (this can happen, for example, if connections are made to the same service on a server from the same client application). nnAt a glance, packets from these two connections might look identical in terms of their addressing information.

##### The Problem: Connection Confusion

Without a mechanism to differentiate these packets, Computer B might confuse which packets belong to which connection. This confusion could result in data being sent to the wrong application or session, leading to errors, data corruption, or security issues.

##### The Solution: Random Initial Sequence Numbers

To distinguish between these two connections, TCP uses a unique Initial Sequence Number (ISN) for each connection. The ISN is a random number that starts the count of bytes for the connection. Here's how it helps:

1. **Connection 1:** Computer A starts the first connection to Computer B, using a random ISN, let's say 1000. The first packet of data from this connection will start with sequence number 1000.

2. **Connection 2:** Almost simultaneously, Computer A starts a second connection to Computer B. This time, a different random ISN is chosen, let's say 5000. The first packet of this second connection starts with sequence number 5000.

##### How Random ISNs Prevent Confusion

- **Unique Identifier:** Even though both connections use the same IP addresses and ports, the unique ISNs (1000 and 5000) serve as additional identifiers that allow Computer B to distinguish between packets belonging to the two different connections. 

- **Sequence Continuation:** As data is transmitted over each connection, the sequence numbers continue to increment from their respective ISNs. So, packets from Connection 1 will have sequence numbers like 1001, 1002, etc., and packets from Connection 2 will follow their sequence starting from 5000 (5001, 5002, etc.).

##### Example Outcome

When Computer B receives a packet, it can look at the combination of source IP, destination IP, source port, destination port, **and the sequence number** to determine which connection the packet belongs to. If a packet arrives with a sequence number around 1000, Computer B knows it's part of Connection 1. If another packet arrives with a sequence number around 5000, it knows this packet is part of Connection 2.


#### Spoofing and Session Hijacking: 

If ISNs were predictable, an attacker could easily guess the sequence number of the next packet in an ongoing communication. This vulnerability could be exploited to inject malicious packets into the data stream, leading to spoofing (where the attacker pretends to be another user) or session hijacking (where the attacker takes over an existing session between two parties). Randomizing the ISN makes it significantly more difficult for attackers to predict the sequence numbers, thereby increasing the security of TCP connections.


## UDP Datagram vs TCP Stream

`UDP`

Message oriented, you have an API (send/recv and similar) that provide you with the ability to send one datagram, and receive one datagram. 1 send() call results in 1 datagram sent, and 1 recv() call will recieve exactly 1 datagram.

`TCP`

Stream oriented, you have an API (send/recv and similar) that gives you the ability to send or receive a byte stream. There is no preservation of message boundaries, TCP can bundle up data from many send() calls into one segment, or it could break down data from one send() call into many segments - but that's transparent to applications sitting on top of TCP, and recv() just gives you back data, with no relation to how many send() calls produced the data you get back.
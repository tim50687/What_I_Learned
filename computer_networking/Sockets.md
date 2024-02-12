# Sockets

A good way to think of a socket is as the point where a local application process attaches to the networks. 

> While sockets are most closely associated with the Transport Layer (Layer 4), they also interact with the Network Layer (Layer 3).

A socket itself `is not an API, but rather an endpoint in a network communication`. However, the term "socket" is often used to refer to both the endpoint and the Socket API, which is a set of functions or methods provided by a programming language or environment to enable network communication. Let's clarify these concepts:

> Yes, you can think of sockets as the means by which applications interact with the Transport and Network Layers in the OSI model. Sockets abstract the complexities of these layers, providing a simpler interface for applications to send and receive data over a network. This abstraction allows application developers to focus on the application's logic rather than the details of network communication.

### Socket as an Endpoint
- A socket represents one endpoint of a two-way communication link between two programs running on a network.
- It is `bound to a port number` so that the Transmission Control Protocol (TCP) layer can identify the application that data is destined for.
- An analogy for a socket is a telephone in a landline network, where the telephone is the endpoint through which you communicate.

### Socket API
- The Socket API refers to the set of functions or methods that you use to create and manage sockets in programming.
- It includes operations like creating a socket, connecting to a server, sending and receiving data, and closing the connection.
- These APIs are provided by the operating system and are accessible in various programming languages like Python, Java, C, and others.

### How Sockets Work in Network Communication
1. **Creation**: Your program creates a socket using the Socket API.
2. **Connection**: The socket connects to a server's socket. This is like dialing a phone number.
3. **Communication**: Data is sent/received through this socket.
4. **Closure**: The connection is closed when communication is complete.

## Create a Socket

The `socket()` function is a fundamental operation in network programming, used to create a socket, which serves as an endpoint for sending and receiving data over a network. Let's break down the parameters and the purpose of this function in detail:

### `int socket(int domain, int type, int protocol)`

1. **`int domain`**:
   - **Purpose**: Specifies the protocol family to be used.
   - **Common Values**:
     - `PF_INET`: Stands for "Protocol Family Internet" and is used for IPv4 Internet protocols. This is typically used for TCP/IP or UDP/IP network communication.
     - `PF_INET6`: Similar to `PF_INET` but for IPv6 Internet protocols.
     - `PF_UNIX` (or `PF_LOCAL`): Used for local communication between processes on the same system, employing Unix domain sockets.
     - `PF_PACKET`: Used for low-level packet interface, directly interacting with network devices, bypassing the standard TCP/IP stack.

2. **`int type`**:
   - **Purpose**: Defines the communication semantics (how data is transferred).
   - **Common Values**:
     - `SOCK_STREAM`: Provides a sequenced, reliable, two-way, connection-based byte stream. It's used with TCP (Transmission Control Protocol). Data is read and written as a continuous stream, much like reading and writing to a file.
     - `SOCK_DGRAM`: Supports datagrams (connectionless, unreliable messages of a fixed maximum length). It's used with UDP (User Datagram Protocol). Each `send()` or `recv()` call deals with a discrete message.

3. **`int protocol`**:
   - **Purpose**: Specifies the particular protocol to be used with the socket. Normally, only a single protocol exists to support a particular socket type within a given protocol family.
   - **Common Values**:
     - Typically set to `0` to automatically choose the appropriate protocol for the given `type`. For example, for `PF_INET` and `SOCK_STREAM`, the default protocol is TCP.

4. **Return Value**:
   - The function returns a socket descriptor, an integer value, which is used as a handle to refer to the socket in all subsequent operations (like connect, listen, send, receive).
   - If the function fails, it returns `-1`, indicating an error, and the specific error code can be retrieved using functions like `perror()` or `errno`.

### Example Usage
Here's a basic example of how `socket()` might be used to create a TCP socket for IPv4 communication:

```c
int sockfd = socket(PF_INET, SOCK_STREAM, 0);
if (sockfd == -1) {
    perror("socket failed");
    exit(EXIT_FAILURE);
}
```

### Conclusion
The `socket()` function's parameters—`domain`, `type`, and `protocol`—allow you to specify the exact nature of the communication you intend to perform, including the network protocol family, the socket type (stream or datagram), and the specific protocol (usually defaulted). The returned socket descriptor is then used for further socket operations. Understanding these parameters is crucial for setting up the desired network communication in your application.


## Client Connection Process

1. Ask the OS for a socket. In C, this is just a `file descriptor` (an integer) that will be used from here on to refer to this network connection.

### File Descriptors in Unix-like Systems
- **General Concept**:
   - In Unix-like operating systems, a file descriptor is an abstract indicator used to access a file or other input/output resource, such as a pipe or network socket.
   - It's a low-level representation used by the operating system to keep track of open resources.

- **Everything is a File**:
   - Unix philosophy treats various types of I/O (Input/Output) resources as files. This is part of the "everything is a file" concept, meaning most interactions with the OS are through file-like interfaces.
   - Whether it's reading from or writing to a regular file, communicating over a network, or interacting with a device, Unix uses file descriptors as a common way to handle all these different types of I/O.

2. `Perform a DNS lookup` to convert the human-readable name (like example.com) into an IP address (like 198.51.100.12). DNS is the distributed database that holds this mapping, and we query it to get the IP address.

- C Hint: Use `getaddrinfo()` to perform this lookup.

3. Connect the socket to that IP address on a specific port.

-  A good example port to remember is 80, which is the standard port used for servers that speak the HTTP protocol (unencrypted).

- `There must be a server listening on that port on that remote computer`, or the connection will fail.

4. Send or receive data on that socket.

- Data is send as a sequence of bytes.

5. Close the Connection.

## Server Listening Process

1. Ask the OS for a socket. Just like with the client.

2. `Bind the socket to a port`. This is where you assign a port number to the server that other clients can connect to. “`I’m going to be listening on port 80!`” for instance.

> Caveat: programs that aren’t run as root/administrator can’t bind to ports under 1024–those are reserved. Choose a big, uncommon port number for your servers, like something in the 15,0000-30,000 range. If you try to bind to a port another server is using, you’ll get an “Address already in use” error.

- Ports are per computer. You can have a server listening on port 80 on one computer, and another server listening on port 80 on another computer. The port number is just a way for the OS to know which program to send incoming data to.

3. `Listen for incoming connections`. This is where you tell the OS to start listening for incoming connections from clients on a specific port.

4. `Accept incoming connections.` The server will block (it will sleep) when you try to accept a new connection if none are pending. Then it wakes up when someone tries to connect.

- **How It Works**: The `accept()` function is used by a server to accept incoming connection requests from clients.

- **New Socket for Each Connection**: When a client attempts to connect to the server, the server's original socket (created and bound to a port earlier) listens for these connection requests. Upon a successful connection request, `accept()` returns a *new* socket specifically for that connection.

- **Why a New Socket?**: This design allows the server to continue listening for other incoming connections on the original socket while the new socket with the same port is dedicated to the established client connection. Each client gets its own unique socket for communication.

- **Handling Multiple Clients**: Servers often handle multiple clients simultaneously. The new socket for each connection allows for individual communication channels with each client. To manage multiple clients, `servers might spawn a new thread or process for each new connection.
`
5. `Send data and receive data.` This is typically where the server would receive a request from the client, and the server would send back the response to that request.

6. `Go back and accept another connection.` Servers tend to be long-running processes and handle many requests over their lifetimes.


## Reflect Questions


### 1. What role does `bind()` play on the server side?
- **Function**: The `bind()` function on the server side associates the server's socket with a specific port number and, optionally, an IP address. This is crucial for a server because it defines the address at which the server listens for incoming connections.

- **Usage**: It's used before the `listen()` call and is essential for servers, as clients need to know the specific port to connect to.

### 2. Would a client ever call `bind()`?
- **Typical Scenario**: In most cases, clients do not use `bind()`. Instead, they use `connect()`, which automatically assigns a local ephemeral (temporary) port and the default local IP address for the connection.

- **`Exceptional Use`**: However, there are scenarios where a client might use `bind()`. For example, when a client `needs to use a specific local port (perhaps for firewall rules or protocol requirements)` or when implementing certain types of network software like a `peer-to-peer` application.

### 3. Why does `accept()` return a new socket as opposed to just reusing the one we called `listen()` with?
- **Multiple Connections**: The original socket is used to listen for new connections. When `accept()` is called, it returns a new socket specifically for the accepted connection. This design allows the server to handle multiple connections simultaneously.

- **Dedicated Communication Channel**: Each new socket represents a separate, dedicated communication channel with a specific client. This separation ensures that communication with one client doesn't interfere with another.

### 4. What would happen if the server didn’t loop to another `accept()` call? What would happen when a second client tried to connect?
- **Single Handling**: If the server doesn't loop back to `accept()` after handling a client, it won't be ready to accept new connections.

- **Result for Second Client**: A second client trying to connect while the server is not actively listening (i.e., not in an `accept()` call) would fail to establish a connection. The client might receive an error like "connection refused" depending on the server's configuration and OS.

### 5. If one computer is using TCP port 3490, can another computer use port 3490?
- **Yes**: Ports are specific to each computer's network interfaces. One computer using TCP port 3490 has no effect on another computer's ability to use the same port number. Each device on a network has its own set of ports.

### 6. Speculate about why ports exist. What functionality do they make possible that plain IP addresses do not?
- **`Multiplexing`**: Ports allow multiple network processes or applications on a single device to use network resources (like IP addresses) simultaneously. They act as endpoints within the host.

- **`Identifying Services`**: Ports help in identifying specific services running on a computer. For instance, `web servers generally listen on port 80 for HTTP`.

- **`Enabling Multiple Connections`**: With ports, a single IP address can be used to establish numerous connections for different purposes. For example, you can browse the internet, send emails, and stream videos from the same device concurrently, each using different port numbers.

## Youtube tutorial

### Header Files

- `#include <sys/types.h>`: This header file contains definitions of a number of `data types used in system calls`. 

- `#include <sys/socket.h>`: This header file contains definitions of `structures needed for sockets`. Eg. sockaddr
    - Provides the definitions for socket-related functions like `socket()`, `bind()`, `listen()`, `accept()`, `connect()`, etc.
    - Defines important structures such as `sockaddr`.

- `#include <netinet/in.h>`: This header file contains `constants and structures needed for internet domain addresses`.
    - Defines structures like `struct in_addr` (which represents an IPv4 internet address) and `struct sockaddr_in` (used for IPv4 socket address structure).
    - Provides constants such as `AF_INET (address family for IPv4)` and `INADDR_ANY (used to bind a socket to all available interfaces)`.

#### Structure of sockaddr_in
    
```c
#include <netinet/in.h>

struct sockaddr_in {
    short            sin_family;   // e.g. AF_INET
    unsigned short   sin_port;     // e.g. htons(3490)
    struct in_addr   sin_addr;     // see struct in_addr, below
    char             sin_zero[8];  // included to pad the structure to the length of a struct sockaddr, should be set to all zeros with the funciton `memset()`
};

struct in_addr {
    unsigned long s_addr;  // load with inet_aton()
};
```

- In memory, the `struct sockaddr_in` is the same size as `struct sockaddr`, and you can freely cast the pointer of one type to the other without any harm, except the possible end of the universe.

### Functions

```c
int sockfd = socket(int domain, int type, int protocol);
```

- **Purpose**: Creates a new socket.

- **Parameters**:
   - `domain`: Specifies the protocol family of the created socket.
        - `PF_INET`: Stands for "Protocol Family Internet" and is used for IPv4 Internet protocols. This is typically used for TCP/IP or UDP/IP network communication.
        - `PF_INET6`: Similar to `PF_INET` but for IPv6 Internet protocols.
        - `PF_UNIX` (or `PF_LOCAL`): Used for local communication between processes on the same system, employing Unix domain sockets.
   - `type`: Specifies the communication semantics.
        - `SOCK_STREAM`: Provides a sequenced, reliable, two-way, connection-based byte stream. It's used with `TCP` (Transmission Control Protocol). Data is read and written as a continuous stream, much like reading and writing to a file.
        - `SOCK_DGRAM`: Supports datagrams (connectionless, unreliable messages of a fixed maximum length). It's used with `UDP` (User Datagram Protocol). 
   - `protocol`: Specifies a particular protocol to be used with the socket. Normally, only a single protocol exists to support a particular socket type within a given protocol family.
        - use `0` to automatically choose the appropriate protocol for the given `type`. For example, for `PF_INET` and `SOCK_STREAM`, the `default protocol is TCP`.


```c
int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
```

- **Purpose**: Binds the newly created socket to the specified address.

- **Parameters**:
   - `sockfd`: The socket descriptor returned by `socket()`.
   - `addr`: A pointer to a `sockaddr` structure containing the address to bind to, cast to a `sockaddr *`.
   - `addrlen`: The size in bytes of the address to bind to.


```c
int listen(int sockfd, int backlog);
```

- **Purpose**: Marks the socket as a passive socket, that is, as a socket that will be used to accept incoming connection requests using `accept()`.

- **Parameters**:
   - `sockfd`: The socket descriptor returned by `socket()`.
   - `backlog`: The maximum number of pending connection requests that can be queued up before connections are refused. This is typically set to `5`.


```c
int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
```
- It is the blocking operation that does not return until a remote client has successfully connected to the server. And when it does return, it returns a new socket descriptor that can be used to communicate with the client.

- **Purpose**: Accepts an incoming connection request on a socket.

- **Parameters**:
   - `sockfd`: The socket descriptor returned by `socket()`.
   - `addr`: A pointer to a `sockaddr` structure that will be filled with the address of the client that connects, cast to a `sockaddr *`.
   - `addrlen`: A pointer to a `socklen_t` structure that will be filled with the size in bytes of the address of the client that connects.


```c
int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
```

- **Purpose**: Connects the socket to the specified address.

- **Parameters**:
   - `sockfd`: The socket descriptor returned by `socket()`.
   - `addr`: A pointer to a `sockaddr` structure containing the address to connect to, cast to a `sockaddr *`.
   - `addrlen`: The size in bytes of the address to connect to.


```c
bzero((char *) &serv_addr, sizeof(serv_addr));
```

- **Purpose**: Sets all values in the buffer to zero.

- **Parameters**:
   - `serv_addr`: A pointer to the buffer to be zeroed.
   - `sizeof(serv_addr)`: The size in bytes of the buffer to be zeroed.


### `inet_ntoa` and `ntohs` and `inet_pton` and `inet_ntop`
`inet_ntoa` and `ntohs` are functions used in C programming for handling network-related tasks, specifically for dealing with IP addresses and port numbers in a network context.

1. `inet_ntoa`: (Obsolete)
   - `inet_ntoa` stands for "Internet Network to ASCII."
   - It is a function used to convert an IPv4 address from its binary network byte order representation into a human-readable string in dotted-decimal format.
   - The function takes an `in_addr` structure as an argument and returns a pointer to a static buffer containing the string representation of the IP address.
   - Here's an example of how it's typically used:

   ```c
   #include <stdio.h>
   #include <netinet/in.h>
   #include <arpa/inet.h>

   // ...

   struct sockaddr_in client_addr;
   // Assume client_addr is filled with information
   printf("server: got connection from %s port %d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));
   ```

   In the code snippet above, `inet_ntoa` is used to convert the binary IP address (`client_addr.sin_addr`) to a string.

2. `ntohs`:
   - `ntohs` stands for "Network to Host (Short)."
   - It is a function used to `convert a 16-bit unsigned short integer from network byte order to host byte order` (which might be little-endian or big-endian depending on the system).
   - It's typically used for converting the port number received in network packets to the format used by the host system.
   - Here's an example of how it's used:

   ```c
   #include <stdio.h>
   #include <netinet/in.h>

   // ...

   struct sockaddr_in client_addr;
   // Assume client_addr is filled with information
   printf("server: got connection from %s port %d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));
   ```

   In this code, `ntohs` is used to convert the port number (`client_addr.sin_port`) from network byte order to host byte order before displaying it in the `printf` statement.

3. `inet_pton()`

Converts an IP address in `numbers-and-dots` notation into either a `struct in_addr or a struct in6_addr` depending on whether you specify AF_INET or AF_INET6.

4. `inet_ntop()`

```c
#include <arpa/inet.h>

const char *inet_ntop(int af, const void *src, char *dst, socklen_t size);

```

Converts either a `struct in_addr or a struct in6_addr` into a `textual representation` suitable for presentation. The `dst` parameter points to a buffer to receive the `null-terminated string` containing the text address. The `size` parameter specifies the size of this buffer. The `src` parameter points to the `struct in_addr or struct in6_addr` that you want to convert.


## Blocking and Non-blocking Sockets

### The Scenario with Blocking Sockets

- **Data to Send**: 100,000 bytes
- **Buffer Size**: 1,024 bytes

### Blocking Sockets Explained

In blocking mode, when you send data over a socket, your program will wait (or "block") if the buffer is full and not ready to accept more data. The system will automatically manage the process of emptying the buffer by sending its contents over the network, but your program stops executing further instructions until it can send more data.

### Step-by-Step Process

1. **Initial Send Attempt**: You attempt to send 100,000 bytes of data using a blocking socket. The system copies as much data as it can into the buffer, up to its limit. In this case, the first 1,024 bytes of your data are copied into the buffer.

2. **Buffer is Full**: Since the buffer is now full, the system will attempt to send this data over the network. Your program is "blocked" during this time, meaning it will not proceed to the next line of code until there is more space in the buffer.

3. **Buffer Empties**: As the data is sent over the network, the buffer begins to empty. The speed at which this happens depends on various factors, including network speed and congestion.

4. **Sending More Data**: Once there is space in the buffer (for example, after the first 1,024 bytes are sent and the buffer is empty), the system will automatically attempt to copy the next chunk of data from your program into the buffer. Your program continues to be blocked if the buffer fills up again and will only proceed once there's more space in the buffer.

5. **Repeat Until Complete**: This process of filling the buffer, blocking until it's sent, and then filling it again, continues until all 100,000 bytes of your data have been sent. Your program will be repeatedly paused and resumed during this process, but you don't need to manually manage the buffer or check how much data has been sent.

6. **Completion**: Once all data has been successfully copied into the buffer and sent over the network, your program can continue executing the next instructions. There's no need for manual intervention to handle the buffer or manage the data sending process beyond the initial send command.




### Non-blocking Sockets

For non-blocking sockets, the process differs significantly because your program doesn't wait for the buffer to be ready to accept more data. Using the same scenario where you want to send 100,000 bytes of data and the buffer size is 1,024 bytes, let's see how it works:

### The Scenario with Non-blocking Sockets

- **Data to Send**: 100,000 bytes
- **Buffer Size**: 1,024 bytes

### Non-blocking Sockets Explained

In non-blocking mode, when you attempt to send data, the operation will not block your program's execution. If the buffer can't accept all the data you're trying to send at once, the `send` method returns immediately with the number of bytes successfully copied into the buffer. If the buffer is full, it might return 0 or raise a `socket.error` (depending on the environment and situation).

### Step-by-Step Process

1. **Initial Send Attempt**: You try to send 100,000 bytes. The system attempts to copy as much of this data as it can into the buffer. Let's say it manages to copy 1,024 bytes, filling the buffer.

2. **Immediate Return**: Unlike blocking sockets, the `send` method now immediately returns, indicating how many bytes were sent (or copied to the buffer) — in this case, 1,024 bytes. Your program continues running immediately after this call.

3. **Program Responsibility**: It's now up to your program to handle the fact that not all data was sent. The `send` method's return value tells you how much was sent, so you know that 1,024 bytes of the 100,000 bytes were handled.

4. **Handling Unsent Data**: Your program needs to try sending the remaining data again. But, since the socket is non-blocking, you should do this in a way that doesn't just loop immediately, trying to resend the data, as that could waste CPU resources and potentially lead to a tight loop.

5. **Resend Attempts**: You might use a method like polling with `select`, a delay, or an event-driven approach to wait until the socket is ready to accept more data. Once it is, you try to send the next chunk of data (or the rest of the unsent data).

6. **Repeat Process**: This process of attempting to send data, checking how much was sent, and then waiting before trying to send more continues until all 100,000 bytes have been successfully sent.

7. **Completion**: Your program has to actively manage this process, repeatedly checking and sending, until all data is sent. It requires more complex coding but allows your program to remain responsive and able to perform other tasks while the data is being sent.

### Summary

With non-blocking sockets, your program must actively manage the sending of data, including dealing with partially sent data and retrying sends. This approach provides greater flexibility and can keep your application responsive, but it requires more sophisticated error handling and flow control mechanisms. You're responsible for ensuring all data is eventually sent, which might involve keeping track of unsent data and intelligently deciding when to retry sending.


## Select and Poll

[GOOD Article](https://stackoverflow.com/questions/970979/what-are-the-differences-between-poll-and-select)

## Non-blocking vs Asynchronous

[GOOD Article](https://medium.com/@livajorge7/breaking-down-the-differences-non-blocking-vs-asynchronous-programming-and-when-to-use-each-953f2354b052#:~:text=However%2C%20there%20are%20some%20subtle,concurrently%20without%20blocking%20other%20operations.)
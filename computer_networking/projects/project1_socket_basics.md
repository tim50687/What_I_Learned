# Socket Basics

## What is TLS

[Good website](https://www.codecademy.com/article/transport-layer-security-tls)

[Good video](https://www.youtube.com/watch?v=j9QmMEWmcfo)

**TLS (Transport Layer Security)**

- TLS is a cryptographic protocol that ensures the end-to-end security of data transmitted between applications over the Internet.
- It is commonly associated with secure web browsing, indicated by the padlock icon in web browsers, but it can be used for various applications like email, file transfers, video/audioconferencing, instant messaging, and more.
- TLS evolved from SSL (Secure Socket Layers), which was developed by Netscape in 1994. SSL 3.0 served as the foundation for TLS.

- TLS secures data in transit, preventing eavesdropping and unauthorized alterations.
- It's typically `implemented over TCP` for protocols like HTTP, FTP, SMTP, and IMAP, but can also be used with UDP, DCCP, and SCTP (Datagram Transport Layer Security - DTLS) for specific applications.

### Introduction to TLS

Without `HTTPS`, the data you send and receive over the Internet is transmitted in plaintext, which means it's not encrypted and can be intercepted by attackers (Ex. your `password` or `credit card number`).

HTTPS is designed to solve this problem by encrypting data in transit using TLS. It uses a combination of symmetric and asymmetric encryption to secure data between the client and server.

### How the TLS handshake works

1. TCP handshake: The client and server establish a TCP connection.

> Asymmetric Encryption V
2. Client hello: The client sends a `ClientHello` message to the server, which includes the TLS version, a random number, and a list of supported ciphers and compression methods.

- Tell server `what version of TLS` it can support.

- What cyber suite it can support.

- The server send back the `ServerHello` message back to the client. And send `certificate` to the client.
    - `Certificate` contains a public key that's used to encrypt the data.

- Server send `ServerHelloDone` message to the client.
    -  The cliend and server have `agreed` on the TLS version and the cipher suite to use.

3. Key exchange: The client generates a `session key` and encrypts it with the `server's public key` from the certificate. The client sends the encrypted pre-master secret to the server.

- The server decrypts the session key using its private key.

- Now both side includes the `session key`.

> Symmetric encryption V
4. Data exchange: The client and server exchange encrypted data using the session key.

- If the server is able to successfully decrypt the message, the handshake is complete.

### For example

#### With TLS Handshake (Secured Connection)

The workflow in a TLS-enabled connection includes additional steps for setting up a secure communication channel:

1. **SSL/TLS Context Initialization**:
   Both client and server initialize an SSL context using OpenSSL functions. This context is configured with necessary certificates and keys. For servers, this includes a server certificate and private key. For clients, this may include a CA (Certificate Authority) certificate to verify the server's certificate.

2. **Server and Client Socket Creation**:
   Similar to the non-TLS process, both parties create a socket.

3. **Server Binds, Listens, and Accepts**:
   The server binds to a port, listens for incoming connections, and accepts a connection.

4. **SSL Object Creation and Association**:
   Both server and client create an SSL object from their respective SSL contexts. The server and client associate their respective sockets with their SSL objects using `SSL_set_fd()`.

5. **TLS Handshake**:
   - **Server**: Waits for a client to initiate a TLS handshake. The server uses `SSL_accept()` to negotiate and establish a secure connection.
   - **Client**: Initiates the TLS handshake using `SSL_connect()`. The client verifies the server's certificate against the CA certificate.

6. **Secured Data Transmission**:
   Once the secure channel is established, data transmission occurs over SSL using `SSL_read()` and `SSL_write()`. This ensures that data is encrypted and decrypted automatically.

7. **Close Connection**:
   Both parties close the SSL connection using `SSL_shutdown()` and free the SSL objects. The underlying sockets are then closed as in a non-TLS connection.

8. **Cleanup**:
   SSL contexts are freed, and any OpenSSL-specific cleanup is performed.

### Summary

- **Non-TLS**: Involves direct socket communication. It is simpler but not secure.
- **TLS**: Adds layers of security by initializing SSL contexts, performing an SSL handshake, and then transmitting data over SSL. This ensures data confidentiality and integrity and can also provide authentication.

It's important to note that while the TLS process seems more complex, it provides essential security features, especially for sensitive or private data transmitted over the internet.


## getaddrinfo

**Note on `getaddrinfo` Function**

- `getaddrinfo` is a standard networking function in C used for hostname-to-IP address resolution and obtaining socket address information.

- It performs hostname resolution, associates IP addresses with service ports, and allows specifying preferences using the `hints` struct.

- Parameters:
  - `node`: Hostname or IP address to resolve. Can be `NULL` for local host.
  - `service`: Service name or port number (in string format) associated with the socket address.
  - `hints`: A `struct addrinfo` providing preferences for the address resolution.
  - `res`: Pointer to a pointer to store resulting socket address information.

- The `hints` struct allows specifying:
  - Address family (IPv4, IPv6, both).
  - Socket type (e.g., TCP, UDP).
  - Additional flags and preferences.

- Results are returned as a linked list of `struct addrinfo` objects, which contain IP addresses, ports, and other details.

- Commonly used for setting up network connections, client-server applications, and network services.

- Memory allocated for results should be freed using `freeaddrinfo` when no longer needed to prevent memory leaks.

- `getaddrinfo` enhances code clarity, portability, and maintainability by centralizing preferences for address resolution.

- Include `<netdb.h>` for `getaddrinfo` and `<stdio.h>` for error handling (e.g., `perror`).

>  It abstracts away the complexities of DNS resolution for you


## `sprintf` 

- `sprintf` is a function in C that writes formatted data to a string.

- It is similar to `printf` but writes to a string instead of stdout.

## `strstr`

- `strstr` is a function in C that finds the first occurrence of a substring in a string.

- It returns a pointer to the first occurrence of the substring in the string, or `NULL` if the substring is not found.

## JSON
Use cJson header file from 
https://github.com/DaveGamble/cJSON/blob/master/cJSON.h

## buffer overflow

Using dynamically allocated memory with `malloc` and `realloc` instead of declaring arbitrarily huge arrays is considered good practice for several reasons:

1. **Efficient Memory Usage:** Dynamically allocated memory is only allocated when needed. If you declare a large array, it consumes memory even if you don't use all of it. With dynamic allocation, you allocate memory as needed, which is more memory-efficient.

2. **Avoiding Buffer Overflows:** When you allocate memory dynamically, you can extend the buffer size as necessary to accommodate incoming data. This helps prevent buffer overflows, which can lead to security vulnerabilities or crashes.

3. **Adaptability:** Dynamic allocation allows your program to adapt to varying data sizes. If you allocate memory based on actual data size, your program can handle different input sizes without wasting memory.

4. **Reduced Risk of Stack Overflow:** Declaring large arrays as local variables can lead to stack overflow issues, especially when the array size is huge. Dynamic allocation, which uses the heap memory, avoids this problem.

5. **Error Handling:** When using `malloc` or `realloc`, you can check if the allocation was successful. If not, you can handle the error gracefully, whereas with fixed-size arrays, you might run into undefined behavior or crashes.

6. **Portability:** Dynamic memory allocation is more portable across different systems and platforms because you're not relying on the availability of large stack memory.

In summary, using dynamic memory allocation is a safer and more efficient approach when you don't know the exact size of the buffer you need. It helps in efficient memory usage, prevents buffer overflows, and makes your code more adaptable and robust.

## To clean up pointer to pointer

- check both pointer and pointer to pointer are not NULL


## How to use SSL

```
# Compiler and Compiler Flags
CC = cc
CFLAGS = -Wall -g -I/opt/homebrew/opt/openssl@3/include

# Linker Flags
LDFLAGS = -L/opt/homebrew/opt/openssl@3/lib -lssl -lcrypto

# Target Executable
TARGET = client

# Source File and Object Files
SRCS = client.c cJSON.c client_utils.c client_network.c client_game.c set.c
OBJS = $(SRCS:.c=.o) # Turn every .c file in source to .o

all: $(TARGET)

client: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(TARGET) $(LDFLAGS)

# Remove the Executable and Object Files
clean: 
	rm -f $(TARGET) $(OBJS)
```

- `-lssl` and `-lcrypto` are the libraries you need to link to your program.

- `-I` and `-L` are the path to the header files and libraries.

### Debug

The `openssl s_client -connect` command is a command-line tool that allows you to establish an SSL/TLS connection to a remote server. It is primarily used for testing and debugging SSL/TLS connections to servers, such as web servers, mail servers, or any service that uses SSL/TLS encryption.

Here's what each part of the command does:

- `openssl`: This is the OpenSSL command-line tool.
- `s_client`: This is a subcommand of OpenSSL for acting as an SSL/TLS client.
- `-connect proj1.3700.network:27994`: This part of the command specifies the hostname and port to which you want to connect. In this case, it's connecting to the hostname `proj1.3700.network` on port `27994`.

When you run this command, OpenSSL will attempt to establish an SSL/TLS connection to the specified server and port. It will then display various information about the SSL/TLS handshake and the server's SSL certificate, which can be helpful for diagnosing issues with SSL/TLS connections.

The output typically includes information like the server's certificate details, the SSL/TLS handshake process, and any errors or warnings encountered during the connection attempt. This can be useful for troubleshooting and verifying that a server's SSL/TLS configuration is correct.

For example, if you run `openssl s_client -connect proj1.3700.network:27994`, it will attempt to connect to the server at `proj1.3700.network` on port `27994` and provide information about the SSL/TLS handshake process. This can help you diagnose any issues with your SSL/TLS configuration or connectivity to the server.


### Cipher Suite

Yes, for successful SSL/TLS communication between a client and a server, both the client and the server need to agree on and use the same cipher suite during the SSL/TLS handshake. The SSL/TLS handshake is the process by which the client and server negotiate and establish a secure connection, and it involves the following steps:

1. **Client Hello**: The client sends a "ClientHello" message to the server, indicating its supported cipher suites, TLS version, and other parameters.

2. **Server Hello**: The server responds with a "ServerHello" message, selecting one of the cipher suites offered by the client and indicating its chosen TLS version.

3. **Key Exchange**: If necessary, the server and client exchange key information required for encryption and authentication. This may include Diffie-Hellman parameters or other key exchange methods.

4. **Finished**: Both the client and server exchange "Finished" messages, which confirm that they agree on the selected cipher suite and have derived the necessary encryption keys.

If the client and server do not agree on a common cipher suite during the handshake, the handshake will fail, and secure communication cannot be established. Therefore, it's crucial for both parties to support at least one common cipher suite to ensure compatibility.

In practical terms, administrators and developers need to configure their SSL/TLS settings to ensure that both the client and server support the same cipher suites and TLS versions. This ensures that they can establish a secure and encrypted connection that adheres to the same security protocols and algorithms.


Yes, you're on the right track. The process of establishing a TLS connection in a client application involves creating a regular socket, connecting to the server, and then initializing and using SSL objects to secure the communication. Here's a step-by-step breakdown:

### TLS Connection Process

1. **Create a Regular Socket**:
   - Just like a non-encrypted connection, start by creating a TCP socket using `socket()`.
   - Connect this socket to the server's IP address and port using `connect()`.

2. **Initialize OpenSSL**:
   - Call `SSL_load_error_strings()` and `OpenSSL_add_ssl_algorithms()` to initialize the necessary algorithms and error strings used by OpenSSL.

3. **Create an SSL Context**:
   - Create a new SSL context using `SSL_CTX_new()`. This context will be used to manage the settings and data for the TLS connection.
   - Typically, you'll use `TLS_client_method()` as the method for the SSL context.

4. **Load CA Certificates** (if required):
   - If the server you are connecting to uses a self-signed certificate or a certificate not signed by a CA in your system's default trust store, you'll need to load the CA certificate into the SSL context using `SSL_CTX_load_verify_locations()`.

5. **Create an SSL Object**:
   - Create a new SSL object for the connection using `SSL_new()` and pass it the SSL context.
   - Associate the socket file descriptor with the SSL object using `SSL_set_fd()`.

6. **Initiate SSL Handshake**:
   - Initiate the SSL handshake with the server using `SSL_connect()`.
   - The SSL object will handle the negotiation of SSL version, cipher suites, and other parameters.

7. **Verify Server Certificate** (optional but recommended):
   - After the handshake, you can optionally verify the server's certificate to ensure its authenticity.

8. **Send and Receive Data Over SSL**:
   - Use `SSL_read()` and `SSL_write()` to securely send and receive data over the socket.

9. **Close the SSL Connection**:
   - Once you are done with the communication, use `SSL_shutdown()` to shut down the SSL connection.
   - Free the SSL object using `SSL_free()`.

10. **Clean Up**:
    - Close the socket.
    - Free the SSL context using `SSL_CTX_free()`.
    - Call `EVP_cleanup()` to clean up the OpenSSL state.

### Note on Process

- The process ensures that the data transmitted over the network is encrypted and secure.
- TLS adds an extra layer of protection against eavesdropping and man-in-the-middle attacks.
- Proper error checking and handling are crucial at every step to ensure the reliability and security of the connection.

> `After the TCP connection is established, SSL_connect() is used to start the SSL/TLS handshake` process over this connection. This step is specific to secure communication and sets up the encrypted channel.

This process encapsulates the steps for securing a client connection using TLS, leveraging OpenSSL to handle the complexities of the TLS protocol.
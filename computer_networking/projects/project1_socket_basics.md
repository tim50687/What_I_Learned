# Socket Basics

## What is TLS

**TLS (Transport Layer Security)**

- TLS is a cryptographic protocol that ensures the end-to-end security of data transmitted between applications over the Internet.
- It is commonly associated with secure web browsing, indicated by the padlock icon in web browsers, but it can be used for various applications like email, file transfers, video/audioconferencing, instant messaging, and more.
- TLS evolved from SSL (Secure Socket Layers), which was developed by Netscape in 1994. SSL 3.0 served as the foundation for TLS.

- TLS secures data in transit, preventing eavesdropping and unauthorized alterations.
- It's typically `implemented over TCP` for protocols like HTTP, FTP, SMTP, and IMAP, but can also be used with UDP, DCCP, and SCTP (Datagram Transport Layer Security - DTLS) for specific applications.

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
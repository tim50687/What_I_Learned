# IP Addresses, structs, and Data Munging

## IP Addresses

- ::1 is the loopback address for IPv6

- 127.0.0.1 is the loopback address for IPv4

> Lookback address always means "This machine I'm running on now"

- You can turn IPv4 addresses into IPv6 addresses by prefixing them with ::ffff: (e.g. ::ffff:192.0.2.33)

## Byte order 

Sure, let's provide an example to illustrate the difference between Big-Endian and Little-Endian byte orders, and then we'll add a note related to the provided message.

**Example for Big-Endian and Little-Endian:**

Let's consider a 32-bit hexadecimal number `0x12345678`. In Big-Endian and Little-Endian representations, this number would be stored differently in memory:

1. **Big-Endian**:
   - In Big-Endian byte order, the most significant byte (the "big end") is stored at the lowest memory address, and the least significant byte (the "little end") is stored at the highest memory address.
   - So, `0x12345678` in Big-Endian byte order would be stored as follows in memory:
     ```
     Address:   0x1000  0x1001  0x1002  0x1003
     Data:      12      34      56      78
     ```

2. **Little-Endian**:
   - In Little-Endian byte order, the least significant byte is stored at the lowest memory address, and the most significant byte is stored at the highest memory address.
   - So, `0x12345678` in Little-Endian byte order would be stored as follows in memory:
     ```
     Address:   0x1000  0x1001  0x1002  0x1003
     Data:      78      56      34      12
     ```

In summary, Big-Endian stores the most significant byte first, while Little-Endian stores the least significant byte first.

**Note:**
The provided message discusses the concept of byte order in computer architecture. It explains that different computer systems use either Big-Endian or Little-Endian byte order to store multi-byte data types like integers in memory. The key points from the message are:

- Big-Endian stores the most significant byte first, and it is often referred to as "Network Byte Order" in networking contexts.
    - one of the ways that computers store bytes in memory.
- Little-Endian stores the least significant byte first, and it is commonly used in Intel and Intel-compatible processors.
    - another way that computers store bytes in memory. 
- Host Byte Order depends on the architecture of the computer, and you may need to convert data to Network Byte Order when working with networking protocols to ensure compatibility across different systems.
- Functions like `htons()` and `ntohl()` are used to convert between Host Byte Order and Network Byte Order, making it easier to write portable code that works on machines with different endianness.


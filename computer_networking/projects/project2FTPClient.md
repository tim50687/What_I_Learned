# FTP client 

This is a protocols that are used to transfer files between a client and a server on a computer network.

- FTP is the language that compuer use to transfer files between each other.

- You can use FTP to send the file to the FTP server and then other nodes can download the file from the FTP server.
    - Or you can configure you computer to be an FTP server and other nodes can download the file from your computer.

## Authentication

Depending on the FTP server, you may need to authenticate yourself before you can access the files on the FTP server.

- You can use the `anonymous` username and your email address as the password to access the FTP server.

- You can also use the `username` and `password` that you use to login to the FTP server.

> Not an secure protocol, so you should not use it to transfer sensitive information.

- FTP (File Transfer Protocol) operates at the application layer (Layer 7) of the OSI (Open Systems Interconnection) model.


## Steps

To implement an FTP client in Rust for your project, you'll want to follow a structured approach. Here's a high-level introduction and a step-by-step guide on how to get started:

1. **Project Structure**:

   Create a directory for your project, and within it, you can organize your code into modules and files. Here's a basic project structure:

   ```
   ftp_client/
   ├── src/
   │   ├── main.rs        # Entry point
   │   ├── ftp.rs         # FTP client logic
   │   ├── ftp_command.rs # FTP command handling
   │   └── utils.rs       # Utility functions
   ├── Cargo.toml         # Dependency and project configuration
   └── README.md          # Project documentation
   ```

2. **Dependencies**:

   In your `Cargo.toml` file, you'll specify your project's dependencies. You will need to add dependencies for handling FTP connections and parsing URLs. For instance, you can use libraries like `hyper` for HTTP connections and `url` for URL parsing. You can also use `std::net` for basic socket operations.

   ```toml
   [dependencies]
   hyper = "0.14"
   url = "2.2"
   ```

3. **Parsing Command-Line Arguments**:

   Start by implementing code to parse command-line arguments in your `main.rs` file. You can use the `std::env` module to access command-line arguments. Extract the operation and parameters from the command line.

4. **FTP Client Logic**:

   Create an `ftp.rs` module (or file) to handle the core FTP client logic. Here, you'll implement functions for connecting to the FTP server, sending commands, and processing responses.

   - Implement functions to open a control channel (TCP socket) to the FTP server and handle login using the USER and PASS commands.
   - Implement functions for sending FTP commands like TYPE, MODE, STRU, LIST, DELE, MKD, RMD, STOR, RETR, QUIT, and PASV.
   - Handle FTP response codes and responses from the server. Ensure that the control channel remains open while interacting with the server.

5. **FTP Command Handling**:

   Create an `ftp_command.rs` module (or file) to handle individual FTP command operations. Each command should be implemented as a separate function, and this module can be responsible for constructing the appropriate FTP command strings.

6. **Utilities**:

   In the `utils.rs` module (or file), implement any utility functions that may be needed across your project. This could include functions for parsing FTP response codes, constructing URLs, or handling data transfer.

7. **Testing**:

   As you implement each FTP command and functionality, write unit tests to ensure that individual components are working correctly. Consider using the Rust testing framework (`#[cfg(test)]`) to organize your tests.

8. **Integration Testing**:

   Perform integration testing by running your FTP client against a test FTP server to ensure that the client functions as expected. You can use the provided FTP server (ftp://ftp.4700.network) for testing. Make sure to follow the server's FTP protocol.

9. **Error Handling**:

   Implement error handling throughout your code to handle potential issues gracefully. Rust's `Result` type can be useful for this purpose.

10. **Documentation**:

    Ensure that your code is well-documented. Add comments explaining the purpose and usage of functions, modules, and important data structures. Rust's built-in documentation tool (`cargo doc`) can generate documentation from your code comments.

11. **Final Testing and Debugging**:

    Perform thorough testing and debugging to ensure that your FTP client works as expected and handles various scenarios gracefully.

12. **Cleanup and Optimization**:

    Review your code for any unnecessary redundancy or inefficiencies. Optimize your code as needed.

13. **Readme**:

    Update the `README.md` file to provide clear instructions on how to use your FTP client, including examples of different operations and FTP URLs.

14. **Submission**:

    Finally, compress your project directory (excluding any build artifacts) and submit it via Gradescope as specified in the project guidelines.



## Rust note

- In Rust, `collect` is one function you do often need to annotate because Rust isn’t able to infer the kind of collection you want.

### [[bin]] section in Cargo.toml
The `[[bin]]` section in a `Cargo.toml` file is used to specify the configuration for a binary executable that is part of your Rust project. In this case, it's defining the configuration for the binary named "my_ftp_client."

Here's what each key in the `[[bin]]` section does:

- **name**: This specifies the name of the binary executable. In your example, the binary is named "my_ftp_client." This is the name you would use to run the executable from the command line once you build your Rust project.

- **path**: This specifies the path to the main source file for the binary. In Rust projects, the main source file for a binary is typically named "main.rs." The `path` key tells Cargo where to find this file. In your example, it points to "src/main.rs," indicating that the main source file for the "my_ftp_client" binary is located in the "src" directory and named "main.rs."

By defining this configuration in your `Cargo.toml` file, you are telling Cargo how to build and manage the binary executable when you use the `cargo build` and `cargo run` commands. It ensures that when you run `cargo run`, it will build and execute the "my_ftp_client" binary based on the specified source file and configuration.


## Debug trait

In Rust, `#[derive(Debug)]` is an attribute used to automatically implement the `Debug` trait for a custom data type (struct or enum). The `Debug` trait is part of the Rust standard library and provides a default way to format and print a value for debugging purposes.

When you annotate a struct or enum with `#[derive(Debug)]`, Rust automatically generates the implementation of the `Debug` trait for that type, including a default implementation of the `fmt` method from the `std::fmt::Debug` trait. This generated implementation produces a debug representation of the data in a format that is intended to be human-readable and helpful for debugging.

Here's an example of using `#[derive(Debug)]`:

```rust
#[derive(Debug)]
struct Person {
    name: String,
    age: u32,
}

fn main() {
    let person = Person {
        name: String::from("Alice"),
        age: 30,
    };

    // Printing the person using debug formatting
    println!("{:?}", person);
}
```

In this example:

- The `Person` struct is annotated with `#[derive(Debug)]`.
- Inside the `main` function, we create an instance of the `Person` struct named `person`.
- We use `println!("{:?}", person);` to print the `person` struct using the debug formatting provided by the `Debug` trait.

The output will look something like this:

```
Person { name: "Alice", age: 30 }
```

The debug representation includes the struct's name and its field names along with their values. This is very useful for inspecting the contents of complex data structures during development and debugging.


## TCP connection

The `TcpStream::connect` method in Rust is used to establish a TCP connection to a remote host. Here's an explanation of its behavior:

- `addr` is the parameter that specifies the address of the remote host to which you want to connect. This address should be provided in a form that implements the `ToSocketAddrs` trait.

- The `ToSocketAddrs` trait is a generic trait that allows various types to be used as addresses for network connections. It's used to abstract over different types of addresses like IP addresses and domain names.

- When you call `connect` with an `addr`, Rust will attempt to establish a TCP connection to the remote host specified by that address.

- If the `addr` resolves to multiple IP addresses (for example, a domain name can resolve to multiple IP addresses due to DNS round-robin or other mechanisms), the `connect` method will make connection attempts to each of these addresses in order.

- It will try to connect to the addresses sequentially until one of the connection attempts succeeds.

- If none of the connection attempts are successful (i.e., all addresses fail to establish a connection), the error returned from the last connection attempt (the last address in the list) is returned as the result of the `connect` method call.

This behavior is useful in scenarios where a remote host can be reached using multiple IP addresses, and the `connect` method automatically handles the selection of a working address for the connection. It simplifies network programming by abstracting away the complexities of dealing with multiple addresses and connection failures.

### ?
In the line `let mut stream = TcpStream::connect(server_addr)?;`, the `?` operator is used for error handling. It will automatically handle errors and return an error result (`Result`) if `TcpStream::connect` returns an error. If it returns an `Ok` result, the value is assigned to `stream`.

Here's how it works:

1. If `TcpStream::connect` returns an `Ok` result (i.e., the connection is successful), the value (a `TcpStream`) is assigned to `stream`, and the code continues executing as normal.

2. If `TcpStream::connect` returns an `Err` result (i.e., an error occurs during the connection attempt), the `?` operator will cause the error to be returned from the current function with the `Err` variant. This is essentially a shorthand way of handling errors without writing explicit error-checking code.

So, you don't need to manually check if `stream` is `Ok` or `Err` in this specific line because the `?` operator handles it for you. However, you should make sure to handle potential errors later in your code as needed. Typically, you would use a `match` or `Result` combinators like `map`, `and_then`, etc., to handle errors appropriately in your application logic.


## Read from TCP stream
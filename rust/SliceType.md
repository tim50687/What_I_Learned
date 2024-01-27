# Slice 

## usize

In Rust, `usize` is an integral data type that represents the size of a pointer on the current platform. It is an unsigned integer type, which means it can only store non-negative whole numbers.

The size of `usize` is platform-dependent. On a 32-bit platform, `usize` is typically 32 bits (4 bytes), while on a 64-bit platform, it's typically 64 bits (8 bytes). This makes `usize` a suitable type for indexing into and representing sizes of collections, arrays, and memory regions, as its size adjusts to match the platform's architecture.

Here's how you can use `usize`:

1. **Indexing:** You can use `usize` to index into arrays, slices, and other data structures, ensuring that the index is the correct size for the platform.

2. **Size and Length:** You can use `usize` to represent sizes and lengths of collections, strings, or any data structure that varies in size.

3. **Pointer Arithmetic:** Since `usize` represents the size of a pointer, it is often used in pointer arithmetic, especially when dealing with low-level memory operations or interacting with foreign functions and libraries.

Here's an example of using `usize` to index an array:

```rust
fn main() {
    let array = [1, 2, 3, 4, 5];
    let index: usize = 2;
    let element = array[index];

    println!("Element at index {} is: {}", index, element);
}
```

In this example, `usize` is used to specify the index, ensuring that it is of the correct size for the platform and can be used to access the array element safely.


## :?

The `:?` is a formatting specifier in Rust used within the `println!` or `format!` macros to print or format data using the `Debug` trait. It is often referred to as "pretty-print" because it aims to produce human-readable output for debugging purposes.

When you use `:?`, Rust will automatically format the value using the `Debug` trait implementation for that type. The `Debug` trait provides a way to represent the value in a way that is intended for developers to understand, rather than for end-users.

Here's an example of how `:?` is used:

```rust
fn main() {
    let my_variable = "Hello, Rust!";
    println!("Value of my_variable: {:?}", my_variable);
}
```

In this example, `println!("Value of my_variable: {:?}", my_variable);` will print the value of `my_variable` using its `Debug` trait implementation, which is often a format that allows you to see the content of the variable and its type.

The behavior of `:?` is defined by the `std::fmt::Debug` trait implementation for each specific type, and you can customize how your custom types are formatted by implementing this trait for them. Many standard library types and commonly used types, like numbers, strings, and collections, already have `Debug` trait implementations provided for them.
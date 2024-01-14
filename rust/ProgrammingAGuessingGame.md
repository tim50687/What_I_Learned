# Guessing Game

## Prelude

By default, Rust has a minimal set of features. This is called the *prelude*. It contains essential traits, types, and functions that are available in every Rust program. The prelude is imported by default into every Rust program.

If a type you want to use is not in the prelude, you need to import it explicitly. For example, the `io` module is not in the prelude, so we need to import it to use it.

## let

We use the `let` keyword to create a variable.

- In rust, variables are immutable by default. This means that once you assign a value to a variable, you can't change it later. This is a good thing because it prevents accidental changes to the value of a variable.

- To create a mutable variable, you need to use the `mut` keyword.

### String is a string type provided by the standard library that is a growable, UTF-8 encoded bit of text 

1. **String**: In Rust, "String" is a data type that represents a sequence of characters or text. It is a part of the standard library and is used to work with text data. Unlike string literals (e.g., `"Hello, world!"`), which have a fixed size and are stored in the program's compiled binary, a `String` is dynamic and can grow or shrink in size as needed during runtime.

2. **Provided by the Standard Library**: Rust's standard library includes many data types, including `String`, that are commonly used in Rust programs. This means you don't need to write your own code to work with strings; you can simply use the `String` type provided by the standard library.

3. **Growable**: One of the key features of a `String` in Rust is that it is "growable." This means you can dynamically add or remove characters from a `String` as your program runs. You can concatenate (`push_str`) or append characters (`push`) to a `String`, making it a flexible choice for working with text data.

4. **UTF-8 Encoded**: Rust's `String` type is designed to store text in UTF-8 encoding. UTF-8 is a widely used character encoding that can represent characters from various scripts and languages, making it suitable for handling internationalization and multilingual text.

Certainly, here's a note explaining the concept of associated functions and the `::` syntax in Rust:

## **Associated Function in Rust:**
- An `associated function` in Rust is a function that is associated with a particular type (struct, enum, or trait) rather than with an instance of that type.
- Associated functions are invoked on the type itself, not on an instance of the type, and they are typically used for operations or functionality that are related to the type but do not depend on specific instance data.
- The `::` syntax is used to call associated functions on a type.

**Example with String::new:**
- In the statement `String::new`, `String` is the type, and `new` is an associated function of the `String` type.
- The `new` function is commonly used in many types in Rust, and its purpose is to create a new instance or value of that type with some default or initial characteristics.
- In this specific case, `String::new` creates a new, empty `String` instance. It initializes a `String` object without any initial text content.

**Common Usage:**
- Associated functions like `new` are used to perform tasks related to the type itself, often involving the creation of instances or performing type-specific operations.
- They are especially useful for creating instances of types without the need for a constructor method, which is common in many object-oriented languages.

In summary, associated functions in Rust are functions associated with a specific type, not with instances of that type. The `::` syntax is used to call these associated functions on the type itself. The `new` associated function is a common example used to create new instances of various types, including `String` in this case.


## references

This is useful when you want to allow multiple parts of your code to access the same data without needing to copy that data into memory multiple times.

- Reference is immutable by default. This means that you can't change the value of a reference once you create it.




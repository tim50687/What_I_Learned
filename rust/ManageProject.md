# Managing Growing Porject 

## Package and Crates

### Crates

A crate is the smallest amount of code that the Rust compiler can compile.

A crate can come in one of two forms:

- A binary crate is an executable.
    - Binary crates are programs that you can compile to an executable that you can run.
    - Each must have a function called `main` that serves as the entry point of the program.

- A library crate is a collection of functionality that is intended to be used in other programs.
    - Library crates don't have a `main` function, and they can't be compiled to an executable.
    - Instead, they define functionality intended to be used in other programs.


> Most of the time, when Rustaceans refer to "crates," they're referring to `library` crates. They use crate interchangeably with the concept of `library`.

### Packages

- A **package** in Rust is a project or collection of related code files.

- A package contains one or more **crates**.

> A package can contain as many binary crates as you like, but at most only one library crate.

- A **crate** can be a **library crate**, which provides reusable code, or a **binary crate**, which is an executable program.

- The `Cargo.toml` file defines a package and its dependencies.

- In a package, `src/main.rs` is the entry point for a binary crate with the same name as the package.

- `src/lib.rs` is the crate root for a library crate with the same name as the package.

- You can have multiple binary crates in a package by placing Rust files in `src/bin`.

- Cargo is the Rust package manager and build tool, and it manages packages and their dependencies.

> Cargo passes the crate root files to rustc to build the library or binary.


## Declaring Modules

> we have to make the module part of the crate's module tree in order to call the functions using the `::` syntax.

In Rust, when you declare modules using the `mod` keyword, the compiler looks for the module's code in specific places. Let's break down what each of these places means:

1. **Inline Module**: When you declare a module inline within the crate root file (the main `.rs` file of your project), it means you define the module right there, within curly braces `{}` that replace the semicolon following the `mod` declaration. Here's an example:

    ```rust
    // In your main.rs or lib.rs
    mod garden {
        // Code for the 'garden' module goes here
        // This is an inline module declaration.
    }
    ```

    In this case, the code for the `garden` module is directly written within the crate root file.

2. **Separate File (src/garden.rs)**: If you don't define the module inline, the compiler will look for the module's code in a separate file named after the module, such as `src/garden.rs`. This file should contain the code for the `garden` module.

    ```rust
    // In src/garden.rs
    pub fn plant_tree() {
        // Code for planting a tree in the 'garden' module
    }
    ```

    Here, `src/garden.rs` is the file where the code for the `garden` module is located.

3. **Module Directory (src/garden/mod.rs)**: If you organize your code into submodules within the `garden` module, you can use a special file named `mod.rs` within a directory named after the module (in this case, `src/garden`). The compiler will look for the submodule code in this `mod.rs` file.

    ```rust
    // In src/garden/mod.rs
    pub mod flowers {
        // Code for the 'flowers' submodule within the 'garden' module
    }
    ```

    In this example, the `src/garden/mod.rs` file contains code for submodules of the `garden` module, such as the `flowers` submodule.

By following these conventions, Rust allows you to organize your code into modules and submodules in a structured way. This makes it easier to manage and navigate your codebase as it grows.

## Module tree

We mentioned that `src/main.rs` and `src/lib.rs` are called crate roots. The reason for their name is that the contents of either of these two files `form a module named crate at the root of the crate’s module structure`, known as the module tree.

### Privacy

Items in a `parent module can’t use the private items inside child modules`, but `items in child modules can use the items in their ancestor modules`. This is because child modules wrap and hide their implementation details, but the child modules can see the context in which they’re defined. To continue with our metaphor, think of the privacy rules as being like the back office of a restaurant: what goes on in there is private to restaurant customers, but office managers can see and do everything in the restaurant they operate.

> Sibling can use sibling.
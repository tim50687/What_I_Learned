# Common Programming Concepts

## Variables and Mutability

Variables are immutable by default. This means that once you assign a value to a variable, you can't change it later. This is a good thing because it prevents accidental changes to the value of a variable.

To create a mutable variable, you need to use the `mut` keyword.

## Constants

Certainly, here's a note summarizing the key points about constants in Rust:

**Constants in Rust:**
- Constants are values bound to a name and are not allowed to change.
- Unlike variables, constants are always immutable by default, and you cannot use the `mut` keyword with them.
- Constants are declared using the `const` keyword instead of the `let` keyword.
- You must annotate the type of a constant, even though Rust can often infer types.
- Constants can be declared in any scope, including the global scope, making them accessible throughout your code.
- Constants must be set to a constant expression, not to the result of a value that could only be computed at runtime.

**Example of a Constant Declaration:**
```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```
- In this example, `THREE_HOURS_IN_SECONDS` is the name of the constant, and its value is computed at compile time by multiplying constants together.
- Rust's naming convention for constants is to use all uppercase letters with underscores between words.

**Usage of Constants:**
- Constants are valid for the entire duration of a program within the scope where they were declared.
- They are useful for values that multiple parts of the program need to know about, such as configuration settings, mathematical constants, or domain-specific constants.
- Naming hardcoded values as constants improves code readability and maintainability, as it provides a meaningful name for the value and centralizes its definition.

By using constants in Rust, you can create named, immutable values that are available throughout your code, making it easier to manage and update important values used across your program.


## Shadowing

The concept being explained here is called "shadowing" in Rust. Shadowing occurs when you declare a new variable with the same name as an existing variable in the same scope. This new variable "shadows" or overrides the previous one, effectively taking its place within the scope. There are a few important points to understand about shadowing:

1. **Rebinding with `let`:** When you shadow a variable, you use the `let` keyword followed by the same variable name to create a new variable that shares the same name. This allows you to `change the value or even the type` of the variable.

2. **Immutable by Default:** In Rust, variables are immutable by default. Shadowing allows you to `change the value of a variable while keeping it immutable`. This is different from using the `mut` keyword, which makes a variable mutable, allowing you to reassign values without shadowing.

3. **Changing Types:** With shadowing, you can also change the type of the variable. For example, you can shadow a variable initially defined as a string with a new value of a different type, such as an integer, without encountering type errors.

4. **No `mut` Required:** Unlike mutable variables (those declared with `mut`), which allow you to change their values directly, shadowed variables do not require the `mut` keyword. Instead, you create a new variable in the same scope with the same name.

Here's an example to illustrate shadowing:

```rust
fn main() {
    let x = 5;
    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```

In this example, the variable `x` is initially set to 5, then shadowed to become 6, and later shadowed again within an inner scope to become 12. When the `inner scope ends, the last shadowing is discarded`, and the value of `x` reverts to 6.

The key takeaway is that shadowing allows you to reuse variable names within the same scope, change values, and even change types without the need for mutability (i.e., no `mut` keyword). This can make your code more readable and maintainable by using the same variable name for different purposes in different parts of your code.


## Data Types

**Data Types and Type Annotations in Rust:**
- Every value in Rust has a specific data type that informs Rust how to work with that value.
- Rust is a statically typed language, meaning that it must determine the types of all variables at compile time.
- The Rust compiler can often infer the type of a variable based on its value and usage, eliminating the need for explicit type annotations.
- However, in cases where multiple types are possible (e.g., parsing a String to a numeric type), you must provide a type annotation to specify the desired type explicitly.

**Example of Type Annotation:**
```rust
let guess: u32 = "42".parse().expect("Not a number!");
```
- In this example, the `: u32` type annotation specifies that the `guess` variable should have the type `u32` (unsigned 32-bit integer).
- Type annotations help the compiler understand the intended type and prevent errors when the type is ambiguous.

**Compiler Error without Type Annotation:**
- If you omit the type annotation when it's required, the Rust compiler will display an error message indicating that type annotations are needed.
- Providing an explicit type annotation helps the compiler resolve the ambiguity and compile the code correctly.

By using type annotations when necessary, you ensure that your code is unambiguous and that the Rust compiler can perform type checking effectively, leading to more reliable and safe programs.
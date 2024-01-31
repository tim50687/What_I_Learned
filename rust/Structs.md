# Structs

Like tuples, the pieces of a struct can be `different types`. Unlike with tuples, in a struct you’ll `name` each piece of data so it’s clear what the values mean. 

> you don't have to rely on the order of the data to specify or access the values of an instance.

## mut instance

If the instance is mutable, we can change a value by using the dot notation and assigning into a particular field.

- Rust `doesn’t` allow us to `mark only certain fields as mutable`. 

## Using the Field Init Shorthand

Because the `parameter names` and the `struct field names are exactly the same` , we can use the field init shorthand syntax to rewrite build_user so it behaves exactly the same but doesn’t have the repetition of username and email.

## Create instance from other instances with struct update syntax

```rust
    let user2 = User {
        email: String::from("another@gmail.com"),
        ..user1
    };
```

- The ..user1 `must come last` to specify that any remaining fields should get their values from the corresponding fields in user1

> If you move the data that has not implemented the copy trait, you can not longer use user1 after user2 is created.

## Unit-Like Structs Without Any Fields

You can also define structs that don’t have any fields! These are called unit-like structs because they behave similarly to ().

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

## Print out 

- dbg! macro
    - dbg! macro prints its argument(s) to standard error.
    - Takes ownership of any values passed to it. It will return ownership when it is done with them.

- println! macro
    - println! macro prints its argument(s) to standard output.
    - Does not take ownership of any values passed to it. Instead, it borrows them.

## Implementing a Method

- The &self is actually short for self: &Self

> If we wanted to change the instance that we’ve called the method on as part of what the method does, we’d use `&mut self` as the first parameter.

> Rust has a feature called automatic referencing and dereferencing.

## Associated Functions

- All functions defined within an impl block are called associated functions because they’re associated with the type named after the impl. We can define associated functions that don’t have self as their first parameter (and thus are not methods) because they don’t need an instance of the type to work with. 

### Constructor

- Associated functions are often used for constructors that will return a new instance of the struct.

- To call this associated function, we use the `::` syntax with the struct name
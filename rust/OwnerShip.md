# Ownership

- If someone wants to use my thing, they need to ask me first.

- I can give it away, then they will be the owner.

- Eventually the owner can decide to drop it.

> If a function returns, it will drop or free the ownership, including parameters, local variables, and return value.

## We can use clone to pass it to another function (not recommended)

```rust
fn main() {
    let name = format!("John");
    healper(name.clone()); // Deep copy the string
    healper(name);
}

fn healper(name: String) {
    println!("name: {}", name);
}
```

### We have copy type

- So that we don't need to clone everytime.

- Copy type: integer, boolean, float, char, tuple (if all the elements are copy type) `(i32, String) does not.`

## Three categories of value

- Non-copyable: Move from place to place.

- Clone: Run the custom code to make a copy.

- Copy: They implicitly copies when re referenced.
    - The reason is that types such as integers that have a `known size at compile time` are stored entirely on the stack, so copies of the actual values are `quick to make`.


## Borrow 

We can use `&` to borrow the ownership.

However, it's `immutable` by default. Sometimes you can use api to allow it to be mutable. For example, thread.

- If someone is borrowing my thing, they `cannot modify my original thing by default`.

- If someone is borrowing my thing, I can only modify my original thing `after they return it`. `Many readers, no writer`

## Slice

- &String slice: `&str`. It does noy copy at runtime.
    - We can also pass whole &String to a function, because it is still a subset of the original String.
##  Mutable reference

name: &mut String `no other reader, one writer`

- We can only have one mutable reference at a time.
```rust
pub fn main() {
    let mut name = format!("my friend");
    {
        let r = &mut name;
        greet(r);
        greet(r);
    }
    println!("Hello, {}!", name); // if someone is borrowing name, you can not read it or write it.
}
```



### Example

In Rust, you can have multiple immutable references (`&`) to the same data without any issues because the borrow checker enforces the rules of ownership and borrowing. When you write:

```rust
let r1 = &s;
let r2 = &s;
```

You are creating two immutable references `r1` and `r2` to the `String` data owned by `s`. This is allowed because multiple immutable references to the same data do not introduce data races or conflicts. Rust ensures that these references cannot mutate the data they point to, and they exist simultaneously without any issues.

In the `println!` statement:

```rust
println!("{} and {}", r1, r2);
```

You are using `r1` and `r2` to print the data they reference. After this point, `r1` and `r2` go out of scope, and their references are automatically dropped. Since they were immutable references, there are no issues with ownership or borrowing violations.

Rust's borrow checker is designed to provide safety and prevent data races while allowing multiple immutable references to coexist peacefully. This is a key feature of Rust that helps ensure safe concurrent access to data.
# Enums

Enums give you a way of saying a value is one of a possible set of values.

Enum can only be one of the variants at a time.

## Make variant a constructor function

```rust
enum IpAddr {
    V4(String),
    V6(String),
}
```


## The Option Enum

```rust
enum Option<T> {
    Some(T),
    None,
}
```

- The Option<T> enum is so useful that it’s even included in the prelude; you don’t need to bring it into scope explicitly.

- Its variants are also included in the prelude: you can use Some and None directly without the Option:: prefix.

```rust
let some_number = Some(5);
let some_char = Some('e');

let absent_number: Option<i32> = None;
```

- The type of some_number is Option\<i32>. 
- The type of some_char is Option\<char>.
- For `absent_number`, Rust requires us to annotate the overall Option type: the compiler `can’t infer` the type that the corresponding Some variant will hold `by looking only at a None value.`

> When we have a value of a type like i8 in Rust, the compiler will ensure that we always have a valid value. We can proceed confidently without having to check for null before using that value. 

> Everywhere that a value has a type that isn’t an Option<T>, you can safely assume that the value isn’t null.


## Catch-all Variant

> Note that we have to put the catch-all arm last because the patterns are evaluated in order.

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    other => move_player(other),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn move_player(num_spaces: u8) {}
```

> Rust also has a pattern we can use when we want a catch-all but don’t want to use the value in the catch-all pattern: `_` is a special pattern that matches any value and does not bind to that value. This tells Rust we aren’t going to use the value, so Rust won’t warn us about an unused variable.

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => reroll(),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn reroll() {}
```

## If let 

You can think of if let as syntax sugar for a match that runs code when the value matches `one pattern` and then ignores all other values.
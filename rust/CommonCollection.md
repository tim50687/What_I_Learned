# Common Collection 

Unlike the built-in array and tuple types, the data these collections point to is stored on the `heap`, which means the amount of data does not need to be known at compile time and can grow or shrink as the program runs. 


## Vector 

Vectors can only store values of the same type.

- Using & and [] gives us a reference to the element at the index value.

```rust
    let v = vec![1, 2, 3, 4, 5];

    let does_not_exist = &v[100];
    let does_not_exist = v.get(100);
```

When we run this code, the first `[]` method will cause the program to panic because it references a nonexistent element. This method is best used when you want your program to `crash` if there’s an attempt to access an element past the end of the vector.

When the `get` method is passed an index that is outside the vector, it returns None without panicking. You would use this method if accessing an element beyond the range of the vector `may happen occasionally under normal circumstances`. 

### Iterating over the Values in a Vector

```rust
    let v = vec![100, 32, 57];
    for i in &v {
        println!("{}", i);
    }
```

### Iterating over the Mutable References in a Vector

```rust
    let mut v = vec![100, 32, 57];
    for i in &mut v {
        *i += 50;
    }
```

> Rust needs to know what types will be in the vector at compile time so it knows exactly how much memory on the heap will be needed to store each element.

> Like any other struct, a vector is freed when it goes out of scope

## Vector drop

```rust
    {
        let v = vec![1, 2, 3, 4];
        // do stuff with v
    } // <- v goes out of scope and is freed here
```

> Vector has to store same type, but if you put different type to Enum, you can store different type in the same vector.


## String

- `String literals`, for example, are stored in the program’s binary and are therefore `string slices`.


## Concatenation with the + Operator

```rust
    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2; // note s1 has been moved here and can no longer be used
```

> The + operator uses the add method, whose signature looks something like this:
```rust
fn add(self, s: &str) -> String {
    // implementation goes here
}
```

- Second, we can see in the signature that add takes ownership of `self`, because `self` does not have an `&` This means s1 in will be moved into the add call and will no longer be valid after that.

- Rust `strings` don’t support indexing.


## Hash Map (Hash Maps and Ownership)

For types that implement the `Copy` trait, like `i32`, the values are copied into the hash map. For `owned` values like `String`, the values will be moved and the hash map will be the `owner` of those values
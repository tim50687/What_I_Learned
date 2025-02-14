# Bit Manipulation

## XOR

a | b | a ^ b
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0

- XOR with 0 is always the number itself.
- XOR a number with itself even number of times the result is 0.
- XOR a number with itself odd number of times the result is itself.

## How to count number of 1 bits?

- `& 1` is same as `% 2` : we can decide if the first bit is 0 or 1

- `To shift right by 1` is same as `/ 2`

### Sol1

we can count the first bit and shift right by 1

### Sol2

we can flip the last bit of 1 by minus 1 -> `n - 1`, and if we `&` the original number, the right hand side of last bit of 1 including the last bit of 1 will be 0. 


## 338. Counting Bits

> we can use DP

- If you times 2, that basically means you shift left by 1. So, 10 and 20 will have the same number of 1 bits.
    - What about odd number? say 5, if you shift right 1 bit, it's 2. So, for odd number, you just // 2 and add 1.
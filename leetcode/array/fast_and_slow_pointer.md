# Fast and Slow Pointer

## Algorithm

### Floyd's Cycle Detection Algorithm



## Problems

### 202. Happy Number

Based on our exploration so far, we'd expect continually following links to end in one of three ways.

1. It eventually gets to 1.
2. It eventually gets stuck in a cycle.
3. It keeps going higher and higher, up towards infinity.

#### How do we rule out the 3rd possibility?

Think carefully about what the largest next number we could get for each number of digits is.

| Digits | Largest       | Next  |
|--------|---------------|-------|
| 1      | 9             | 81    |
| 2      | 99            | 162   |
| 3      | 999           | 243   |
| 4      | 9999          | 324   |
| 13     | 9999999999999 | 1053  |

> The number would either go down to 1 or be in a cycle.

#### Time Complexity

- $O(logn)$

#### Space Complexity

For a large enough n, the most space will be taken by n itself.

However, we can optimize to O(1) easily. As we've already shown, for numbers higher than this, it's impossible to return to them anyway.

- $O(1)$
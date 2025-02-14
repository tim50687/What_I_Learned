# Two pointers

## 167. Two Sum II - Input Array Is Sorted

- Use two pointers, because it's sorted, and also gaurantee that there's a solution.
    - If too big, move right pointer to left to make the sum smaller.
    - If too small, move left pointer to right to make the sum bigger.
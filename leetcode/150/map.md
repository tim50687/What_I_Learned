# Hash Map

## 128. Longest Consecutive Sequence *

- Trying to visualize the answer first 
    - say we have array of [100, 4, 200, 1, 3, 2]
    - visualize it as 1 -> 2 -> 3 -> 4 -> 100 -> 200
    - `we notice that the start of the sequence, there's no element before it.`
    - `we notice we only need to check 3 sequences: 1 -> 2 -> 3 -> 4, 100, 200`
- So, we can just find the start of the sequence, then try to find the rest of the sequence.
    - The most traversal is O(n).
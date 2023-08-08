# Python

## QUEUE

- `list.pop(0)` removes the first element. All remaining elements have to be shifted up one step, so that takes $O(n)$ linear time.
    - Instead, use `collections.deque(list)` to get $O(1)$.
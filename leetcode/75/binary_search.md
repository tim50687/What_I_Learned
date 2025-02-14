# Binary Search

## How yo find left most index using binary search?

- If mid >= target, we can set left_most = mid and move right to mid - 1

## How to find right most index using binary search?

- Same as left most, but target is target + 1.

## Find Peak Element

### Modification of Binary Search *

> Can use binary search to find peak element in an array.

- Visualize the array as a graph.

- Find a mid point, if mid is less than mid + 1, then peak is on right side, else peak is on left side.

```python
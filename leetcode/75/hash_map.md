# Hashmap

> Hint:
> 1. Set difference can be found by set1 - set2.

## * Operator

> It's an operation, not a type.

The * Operator (Unpacking):

The * operator is used to unpack the list a into its individual elements when passing them as arguments to the zip() function.

So, when you do zip(*a), it's equivalent to passing a[0], a[1], and a[2] as separate arguments to zip(), like this:

```python
zip([1, 2], [2, 3], [3, 4])
```

> We can get the row of a grid by zip(*grid), which returns an iterable of tuples, where each tuple represents a column.
# Merge Interval

## Sort with Lambda Function



- `intervals`: This is a list where each element is an interval represented by a list or tuple of two numbers, like `[start, end]`. For example, `intervals` could be `[[5, 10], [1, 3], [8, 12]]`.

- `.sort()`: This is a method in Python that sorts a list in place. That means the original list `intervals` is sorted, and no new list is created. The sorting is done in ascending order by default.

- `key=lambda x: x[0]`: This is an argument passed to the `.sort()` method. The `key` argument specifies a function to be called on each element prior to making comparisons for sorting.

  - `lambda x: x[0]` is a lambda function in Python, which is a small anonymous function. Here, `x` is the argument to this function, and `x[0]` is the value it returns. In the context of this line, `x` represents an interval from the `intervals` list, so `x[0]` is the start time of the interval.

  - By setting `key=lambda x: x[0]`, you're telling the `.sort()` method to sort the intervals based on the value of the first element of each interval (i.e., the start time of each interval).


## 56. Merge Intervals

Strategy:

- if next interval's start time is greater than current interval's end time, then it's save to add it to the result. Becuase it will never overlapped with the previous one.

- else: figure out how to merge the two intervals.

## 57. Insert Interval (redo)

Strategy:

There will be three cases when you try to insert a new interval:

1. The new interval is completely to the left of the existing intervals.

2. The new interval is completely to the right of the existing intervals. -> `might need to merge`

3. The new interval overlaps with some intervals. -> `might need to merge`

## 986. Interval List Intersections

I did `n^2` first. 

However, can use `two pointer` to solve this problem to prevent the `revisit`.
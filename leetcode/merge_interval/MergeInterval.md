# Merge Interval

## Sort with Lambda Function



- `intervals`: This is a list where each element is an interval represented by a list or tuple of two numbers, like `[start, end]`. For example, `intervals` could be `[[5, 10], [1, 3], [8, 12]]`.

- `.sort()`: This is a method in Python that sorts a list in place. That means the original list `intervals` is sorted, and no new list is created. The sorting is done in ascending order by default.

- `key=lambda x: x[0]`: This is an argument passed to the `.sort()` method. The `key` argument specifies a function to be called on each element prior to making comparisons for sorting.

  - `lambda x: x[0]` is a lambda function in Python, which is a small anonymous function. Here, `x` is the argument to this function, and `x[0]` is the value it returns. In the context of this line, `x` represents an interval from the `intervals` list, so `x[0]` is the start time of the interval.

  - By setting `key=lambda x: x[0]`, you're telling the `.sort()` method to sort the intervals based on the value of the first element of each interval (i.e., the start time of each interval).

### To merge intervals, we can use the following algorithm:

1. Sort the intervals in ascending order based on the start time.

2. Create a new empty list `merged`.

3. Create a new interval `currInterval` and set it equal to the first interval in the sorted list.

4. Three situations can occur when iterating through the intervals in sorted order:

   - curr.start > interval.end : No overlap, so we can add the interval to the merged list.

   - curr.end < interval.start : No overlap, so we can add the curr to the merged list, and set curr = interval

   - Otherwise, we have an overlap, so we merge the two intervals and set curr = merged interval.

5. At the end, we add the last `curr` to the merged list and return it.

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


## 759. Employee Free Time

1. Flatten the list of intervals into a single list.

2. We merge all the intervals together, and then find the gaps between them.

## 621 Task Scheduler (do it again)

### Greedy

1. It just make sense to do the task with the most frequency first.

2. We do the most frequent task first, and then do the second most frequent task, and so on.

- The answer will look like this:

  - Most frequent task -> second most frequent task -> ... -> least frequent task
  - Put idle in between if necessary

- Once the next most frequent task is available, we want to do that again.

> Heapq, and Queue are useful data structures to solve this problem.

## 253 Meeting Rooms II (do it again)

- We can not merge it is because maybe third meeting can share the room second meeting is using.

- simulate it in the real world situation.

- Let's sort it first, more organized.

- If there are three meeting, and the fourth meeting just need to check if there's any meeting that finished before the fourth meeting starts.
    - if so, then we can use the same room.
    - if not, then we need to add a new room.

- We can use prioiry queue as the meeting room. 

> If you want to know currently who is smallest, first, or largest, you can use `priority queue`.
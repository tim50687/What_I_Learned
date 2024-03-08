# Two Heap

## 295 [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)


- Use two heaps to find the median, one max heap and one min heap
    - Make sure it is sorted.

    - Need to make the length difference less than or equal to 1

    - Need to make sure the max heap's top is less than or equal to the min heap's top

> Don't forget max heap need to insert negative value to make it work.


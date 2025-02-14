# Priority Queue

## How to calculate sum of the subsequences of length k?

- Brute Force: n choose k
- With Library
```python
from itertools import combinations
for subseq in combinations(nums, k):
    sum += sum(subseq)
```
- Without Library
```python
total_sum = 0
arr = [1, 2, 3]
k = 2
def back_tracking_helper(start, path):
    global total_sum  # Declare total_sum as global
    # base case
    if len(path) == k:
        total_sum += sum(path)
        return 

    # find all the subsequence starts from index i
    for i in range(start, len(arr)):
        # add index i
        path.append(arr[i])
        # find the subsequence of len k - 1 from the rest of the array
        back_tracking_helper(i + 1, path)
        # At the base case, you found it, then we can pop from the array and keep explore
        path.pop()

back_tracking_helper(0, [])
```

## 2542. Maximum Subsequence Score *

- Say if we pick the min of the nums2, that means the rest of the k - 1 in nums2 are larger or equal to the min. 

- So, we sort nums2 in descending order, the left hand side k - 1 elements of the picked min will be valid index that we can choose from nums1.

> We know we have to choose min from nums2, so we can start from here. Once we sort the nums2, and pick the min, left hand side index of that min is all valid choice.

> So, with all the valid index choices, we go to nums1 and find the max of the sum of the subsequence in nums1.

> And how do we find the max of the sum of the subsequence in nums1? We can use priority queue to keep track of the max of the subsequence sum. (in order to do it in log(n) time instead of n(calculate the min and remove it))


# 2462. Total Cost to Hire K Workers *
- Just do it again, doing it too slow.

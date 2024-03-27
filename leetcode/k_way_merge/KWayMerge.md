# K way merge


# 86. Merge sorted array

> Whenever you're trying to solve an array problem `in place`, always consider the possibility of `iterating backwards` instead of forwards through the array. It can completely change the problem, and make it a lot easier.


proof:

`curr` pointer will never overwrite the nums1 array

- `nums2` pointer will at most move n steps, and `curr` pointer will move n steps as well.

- whenever `nums1` moves, `curr` will move as well.

Therefore, `curr` pointer will never step on the value of `nums1` array that has not been processed yet.

## 373. Find K Pairs with Smallest Sums

- Remember we might add the same pair to the heap multiple times, so we need a `visited` set to keep track of that.

# 23. Merge k Sorted Lists

- heapq can not compare ListNode, so we put tuple `(val, index, node)` into the heap. Therefore, it will never compare the ListNode, and we can get the ListNode by popping the heap.

# 378. Kth Smallest Element in a Sorted Matrix (do it again for binary search)

we can use `heap` to solve this problem, but we can also use `binary search` to solve this problem.

> Sorted Array - think of using `binary search` 

> mid = start + (end - start) / 2 -> gracefully handle overflow compare to (start + end) // 2
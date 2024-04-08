# Binary search 

## Concepts

Usually, if you want to find the minimum or maximum operation, you can use binary search.

## 33. Search in Rotated Sorted Array 

- in each side, `3 conditions` 

- when you check if lhs is sorted, use `nums[mid] >= nums[left]` instead of `nums[mid] > nums[left]`

### 528. Random Pick with Weight

- Number got picked is proportional to the value of the number

> Instead of expand all the number based on their weight in the array, we can use prefix sum to store the range of each number. This is O(n) time complexity. If you expand the number into the array, say if the weight is 1000, you need to expand 1000 times, which is bad.

> `In other words, if you trying to sample over a range of numbers, you can use prefix sum to store the range of each number.`

> `Moreover, prefix sum is sorted, so that we can use binary search to find the number that we want to pick.`

> `Don't forget the bisect_left function in python. This function is to find the left most undex to insert the number in the sorted array.`


- You can not pick from `r_num = randint(0, self.prefix_sum_ary[-1])`, because the weight start from 1, not 0. So you need to pick from `r_num = randint(1, self.prefix_sum_ary[-1])`


## 658. Find K Closest Elements

- Brute force
    - left and right pointer and move to the middle.

- Better way
    - Window is from 0 to k ~~~ len(arr) - k to arr(len), so we can use binary search to find the start of the window.
    - Binary search 
        - if arr[left] < arr[right + 1], we know that we won't move exceed right hand side `arr[right + 1]`.
        - if arr[left] > arr[right + 1], we know that we won't move exceed left hand side `arr[left]`.

```python
if x > (arr[mid] + arr[mid + k]) / 2:
    left = mid + 1
else:
    right = mid

```
we need to use this math instead of description math, becuase if it will failed at `1,2,3,4,4,4,4,5`, `k = 3`, `x = 3`. If we use description math, the algorithm will go to right, but the correct answer is to go to left.


## 81. Search in Rotated Sorted Array II

```python
if nums[left] == nums[right]:
    left += 1  
```

There's is one case that we need to consider, that is when `nums[left] == nums[right]`, we don't know which side is sorted, so we need to move the left pointer to the right by 1. It doesn't matter because the number is the same, so we can just move the left pointer to the right by 1.
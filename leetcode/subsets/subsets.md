# Subset

- array + array -> can add array together. Or `array += array`, can add array to the array.

## Subsets

### 1. DP O(N * 2^N)
```python
nums = [1,2,3]
_len = len(nums)
dp = [[] for i in range(_len + 1)]
dp[0] = [[]]

for i in range(1, len(nums) + 1):
    candidate_subarray = []
    for element in dp[i - 1]:
        candidate_subarray += [element + [nums[i - 1]]]
    dp[i] += dp[i-1] + candidate_subarray
        
return dp[_len]
```
> Why n * 2^n? 
> Because we ahve total 2^n subset, and each subset has at most n element, and we have to copy the subset to the output array.


## 46. Permutations (so abstract!!!!)

Recursion idea is: 

- Pick a number from the array
- Add the number to the current array
- Do the same thing (find_permutation) to the rest of the array
- Backtrack -> you pop the last element from the array, so that you can try the next number in the array.


## 17. Letter Combinations of a Phone Number

Recursion idea is:

- Pick a number from the array
- Get the possible letter from the number
- Do the same thing (find_combination) to the rest of the array (`But how?`) you can use `index` to indicate the next number in the array.
- Backtrack -> you pop the last element from the array, so that you can try the next number in the array.


## 22. Generate Parentheses

If right parentheses is more than left parentheses, then that means you have to close it.

- Use `array` to pop or append, because if you use `str`, when you try to pop, it will cost O(n) time complexity.

- `If the usage of right parentheses is less then left parentheses, then you can add right parentheses.` -> thus we need counters to keep track of the number of left and right parentheses.


Recursion idea is: 

```
        # add left -> recursion(left, right) then backtrack, if left > 0
"(" +
        # add right -> recursion(left, right) then backtrack, if right > left

It's either one or both, so both condition we use `or` to combine them.
```

- You add the first left parentheses
    - You can then add left parentheses if the number of left parentheses is greater than 0.
        - Then do the backtracking
    - Or you can add right parentheses if the number of right parentheses is greater than left parentheses.
        - Then do the backtracking


## 689. Partition to K equal sum subsets (fking harddddd)

### Instinct

We try to sum the element, we might need to minus it. -> `backtracking`


Recursion idea is:

1. We got the `target_sum`, which is `sum(nums) // k`.

```python
can_get_target_sum(start, in_progress_sum, target_sum) 
=
# mark it used

# start with first element, pick it and call 
can_get_target_sum(start + 1, in_progress_sum + nums[start], target_sum)
# if not used, then mark it as unused and
```

> You can't loop through K time and find if you can fill up k buckets, `say you find a bucket that is valid, good, but maybe that bucket can not gie you the solution, like [1,1,1,1,2,2,2,2], you will get 1,1,1 first in the buckets, however, that is not the solution.`

> Therefore, you need to keep explore in the recursion, in the above example, if you keep recursion, [1,1,1] will return False, so that you will go to next which is [1,2], and following [1,2] you will get the solution.

> So your recursion job is not just find one bucket, it needs to find k buckets.

#### Use Memoization

- Use hash map to store the `used_array`, so that you can avoid the duplicate calculation. `remember list is not hashable`

    - `After you find a bucket`, you will go to find the next bucket -> here you can memoize the result.
    - If you `can't find the bucket`, you can memoize the result as well.

- `We can return False quickly with memoization.`
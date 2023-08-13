# Longest Increasing Subsequence

## Concepts

$C[i]$ = Max # of LIS end at index i.

$C[i] = max(C[i], max(C[j] + 1))$

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        _max = 1
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

            _max = max(_max, dp[i])

        return _max
```

> However, we can use $\textcolor{blue}{\textbf{patience sort}}$ to deal with this problem.  $O(nlgn)$

We can use patience sort to tackle this problem.  

Given the sequence of n numbers. We use patience sort to sort them into piles. Our goal is to form as few piles as possible. 

It has three constraints:
- Stack smaller number on larger number.
- Always choose the leftmost pile whenever possible.
- If there is no possible position for a number, then create a new pile and add the number.

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def patience_sort(nums):
            piles = []

            for i in nums:
                temp = [i]

                index = bisect.bisect_left(piles, i, key = lambda x: x[-1])
                # either 0 or at the end
                if index == len(piles):
                    piles.append(temp)
                else:
                    piles[index].append(i)
            return piles
        
        piles = patience_sort(nums)

        return len(piles)
```


Now we come to the question of why the length of longest increasing sub-sequence is equal to the maximum number of piles?  
To prove this we will argue that the following two invariants hold at each step:  
 1. The top cards in each pile, when read from left to right, are in sorted order.
 2. At any point in time, every card in every pile is part of an `increasing sub-sequence` whose length is given by the pile index.  

For the first invairant, we can see it from greedy strategy. Every element is places as far to the left as possible without violating the rule that smaller numbers must be placed on top of the larger numbers. For example, if you put a number into pile p, we know that it must greater than the number on the top of the pile p-1.

For the second invariant, we prove it by induction. 

**Base case**: We have one number, we know that the length of longest increasing sub-sequence is 1. By performing patience sort, we put it into pile 1. Therefore, it is clear that the number we placed is part of an increasing sub-sequence of length 1 given by the pile index.

**Inductive Hypothesis**: After placing $n_{th}$ numbers, the property holds.

**We want to prove that**: After placing $n+1_{th}$ number on the pile, the property still holds.

When we place $n+1_{th}$ number on the pile p, we know that $n+1_{th}$ number is greater than the number on top of pile $p-1$. By the inductive hypothesis, we know that the number on top of the pile $p-1$ is part of the increasing sub-sequence with length $p - 1$. Moreover, the number we put on top of pile $p-1$ precedes the number we just placed on the pile p in the original order, since we are placing numbers in order. Thus, we can extend the increasing sub-sequence $p-1$ by 1, resulting in a increasing sub-sequence of length p that includes the $n+1_{th}$ number we put on pile p.


Therefore, by the base case and induction, we know that at any point in time, every number in every pile is part of an `increasing sub-sequence` whose length is given by the pile index.


By proving the above two variants holds, we can establish that if the maximum number of piles is $L$, there is no number that is part of an increasing sub-sequence with the length $L + 1$, but there are numbers that are the part of increasing sub-sequence with length $L$. Therefore, the length of longest increasing sub-sequence is $L$, which is equal to the number of piles.
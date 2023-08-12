# Activity Selection

## Concepts

> Max total duration you can schedule up to that activity -> sort by end time.  

$$ C[i] = max(C[i - 1], max(C[i], C[j] + duration[i]))$$

Either to include activity i or to exclude it

1. Find the max duration of activities that include i. $max(C[i], C[j] + duration[i])$

2. Compare it to the duration of activities without i. $C[i-1]$

<p align = "center">
<img src = "../images/activity_selection.jpg" style = "width:400; border:0">
</p>

- Max # of activities can use `Greedy`, proved by $Staying \text{ } Ahead$.
    - Sort by end time.

## Problems

646. Maximum Length of Pair Chain

- Basic version. $O(n^2)$

```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job = list(zip(startTime, endTime, profit))

        job.sort(key = lambda x : x[1])

        
        # init
        dp = [0] * len(job)
        for i in range(len(job)):
            dp[i] = job[i][2]
        for i in range(1, len(job)):

            for j in range(i):
                if job[j][1] <= job[i][0]:
                    dp[i] = max(dp[i], job[i][2] + dp[j])

            dp[i] = max(dp[i], dp[i-1])
        return dp[len(job) - 1]
```

- Using Binary Search (`do again!`) to find which activity should be added before. $O(nlgn)$

```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job = list(zip(startTime, endTime, profit))

        job.sort(key = lambda x : x[1])

        # init
        dp = [0] * len(job)

        for i in range(len(job)):
            # See if there's an activity that can be put before
            # If so, return the 1st item whose end_time is <= my start_time

            # There might be same end time, but since we keep updating the max, 
            # therefore, we find the right most
            j = bisect.bisect_right(job, job[i][0], 0, i, key = lambda x: x[1])
            if j == 0: # no activity can be put before
                dp[i] = job[i][2]
            else:
                dp[i] = job[i][2] + dp[j -1]
            if i != 0: # Update the max 
                dp[i] = max(dp[i], dp[i-1])

        return dp[len(job) - 1]
```
# Prefix Sum

Fast calculation of sum of subarray.

## Problems

### Static Range Sum Quiries

```python
c, q = map(int, input().split(" "))
input_array = list(map(int, input().split(" ")))
# get prefix_sum
prefix_sum = [0]

for i in input_array:
    prefix_sum.append(i + prefix_sum[-1])

for i in range(q):
    left, right = map(int, input().split(" "))
    print(prefix_sum[right] - prefix_sum[left - 1])

```

### Subsequences Summing to Sevens

- Find the max subarray summing to the multiple of 7.

#### Solution

- brute force: O(n^2)

- smart way to do it: O(n)
let's say:
a and c is prefix sum, a < c
a = 7 * k + r
c = 7 * d + r

if you subtract a and c, you will get a subarray summing to 7 * (k - d)

1. Calculate prefix sum

2. Find the remainder start from left most

3. Find the remainder start from right most

4. Compare both array and find the max difference.
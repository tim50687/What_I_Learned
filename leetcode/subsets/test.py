
nums = [1,2,3]
_len = len(nums)
dp = [[]] * (_len + 1)
dp[0] = [[]]
print(dp)
for i in range(1, len(nums) + 1):
    for element in dp[i - 1]:
        
        dp[i] += [element + [nums[i - 1]]]
    print(dp[i])
print(dp[_len])


a = []
b = []
b.append(1)
print(a)
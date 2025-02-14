from itertools import combinations



total_sum = 0
arr = [1,2,3]
arr2 = [3,4,5]
print(zip(arr,arr2))
for i in zip(arr,arr2):
    print(i)
k = 2
def back_tracking_helper(start, path):
    global total_sum
    # base case
    if len(path) == k:
        total_sum += sum(path)
        return 

    # find all the subsequence starts from index i
    for i in range(start, len(arr)): # 1, 2 
        # add index i
        path.append(arr[i])
        # find the subsequence of len k - 1 from the rest of the array
        back_tracking_helper(i + 1, path) 
        # At the base case, you found it, then we can pop from the array and keep explore
        path.pop()

back_tracking_helper(0, [])
print(total_sum)
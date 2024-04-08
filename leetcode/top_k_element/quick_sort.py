import random
def partition(array, left, right):
    # Randomly select a pivot element
    random_index = random.randint(left, right)
    array[random_index], array[right] = array[right], array[random_index]
    pivot = array[right]

    i = left
    for j in range(left , right):
        if pivot >= array[j]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[right] = array[right], array[i]

    return i

def quickSelect(array, left, right, k):
    # base case
    if left == right:
        return array[left] ### study 
    
    # do the randomize partition
    pivot = partition(array, left, right)
    
    # get the index of k th largest element for the subarray
    k_largest_index_subarray = pivot - left + 1

    if k_largest_index_subarray == k:
        print(array)
        return array[pivot] # study
    elif k_largest_index_subarray > k:
        # third parameter is the index supposed to be find in next sub array
        return quickSelect(array, left, pivot - 1, k)
    else:
        # third parameter is the index supposed to be find in next sub array
        return quickSelect(array, pivot + 1, right, k - k_largest_index_subarray)

def quickSort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quickSort(array, left, pivot - 1)
        quickSort(array, pivot + 1, right)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)


# Driver Code 
arr = [ 10, 4, 5, 8, 6, 11, 26 ] 
n = len(arr) 
k = 3
print("K-th smallest element is ", end = "") 
print(quickSelect(arr, 0, n - 1, k)) 

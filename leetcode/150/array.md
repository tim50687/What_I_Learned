# Array

## 80. Remove Duplicates from Sorted Array II

> Since array is sorted, duplicate are adjacent to each other.

- We can use two pointers
    - one to iterate the array
    - one to keep track of the position of where the next valid element should be.

> For each element, there always a place it should be, if it's valid.

## 69. Majority Element *

- We assume the first element is possible majority element.
    - If we find the same element, we increase the count.
    - If we find a different element, we decrease the count.
    - Once it reach zero, then that means before this element, there's no majority element (`we don't care about them anymore, that means we can just find the possible majority for the rest of the array`).
    - And also the majority of 

- By using this approach, we garantee that the possible majority of rest of the array is the majority of the whole array.
    - Say assuming we know where is the point of last 0, the possible majority after that has to be the majority of the whole array.
        - Because by contradiction, there's no majority of the whole array, which contradicts the assumption that the array has a majority.


## 189. Rotate Array *

- We can reverse the entire array -> reverse the first k -> reverse the k - len(nums) - 1

## 122. Best Time to Buy and Sell Stock II


# 6. Zigzag Conversion

> Find the pattern, solve by row by row.

> To go to the next section, you just jump (n - 1) * 2

> But for the middle part, you need to find the second, which you jump (n - 1) * 2 - 2 * ith_row


## 274. H-Index 

- If you want to check if h paper has h citation, you can sort the array descending and check if the ith element is greater than i. we got h = i + 1.

- Also
    - We can have k buckets, and we can put the number of citations in the bucket.
        - If the citation is > n, we put it in the last bucket.
    - Then we can iterate the bucket from the last to the first, and we accumulate the number of papers.
        - Because if citation 6 also means that it has citation 5, 4, 3, 2, 1.


## 380. Insert Delete GetRandom O(1)

> How to remove element in array in O(1)?
You can use hashmap to store the index of the number, so that if you want to remove it, you can swap it with last element and pop it out. (`Don't forget to update the index of the last element`)
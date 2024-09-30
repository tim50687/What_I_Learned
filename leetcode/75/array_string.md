# Array/String

> If trying to reverse something, use 2 pointers
> Because save space complexity, for time complexity, it's O(n)

## 1071. Greatest Common Divisor of Strings

### Brute Force

- Start with the length of the shorter string (for loop)

- Check
    - if the length is divisible by the length of both string

    - if both str1 and str2 are made up of the same substring

> candidate length is important because you can just use candidate times (substring // candidate length) to verify the original string

### Cool trick

1. if there's GCD, then str1 + str2 == str2 + str1

2. GCD length must be the length of the GCD of the two strings

    The question is can the answer be shorter than the GCD of the two strings?

    No, becuase if there's a shorter answer, then that answer must be divisible by GCD, str1, and str2. Therefore, it's not the greatest common divisor.


## 238. Product of Array Except Self

1. we can use prefix product array and suffix product array, becuase each position in the answer array is coming from the product of the prefix and suffix of the original array.

### Trick

We can save some space of prefix product array and suffix product array.

1. We can set current prefix = 1, and current suffix = 1

2. Once you loop through array, you deal with the prefix from the start and suffix from the end.

3. After loopin through the array, each element will be multiplied by the prefix and suffix.


## 334. Increasing Triplet Subsequence

1. We get the first smallest and second smallest number.

2. If we can find the third number that's greater than the second smallest number, then we can return True.

3. We have to update the first smallest number because we might miss the chance to find the third number.

Now the questions is how to update the second smallest number? 

- We know that the previous smallest second number will always be greater than new first smallest number.
    - So we can add the condition, that if third number is greater than the second number, then we can return True. `This is because we know that there exists previous first smallest number is smaller than the second smallest number.`
    - Else, if next number is smaller than previous second smallest number, we can update the second smallest number. `Because we have the better candidates for the first and smaller number.`


## 443. String Compression

Use three pointers 

1. for char position
2. for number position
3. for traverse the string 

> Don't use for loop because we need to keep track of third pointer



## 11. Container With Most Water

- Area is based on the shorter height

- Start from beginning and end


## 1679. Max Number of K-Sum Pairs

- Sort the array

OR

- Use a hash map to keep track of the number of times we have seen the number
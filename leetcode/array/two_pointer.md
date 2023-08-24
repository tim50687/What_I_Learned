# Two pointer


## Problems

### 15. 3Sum

- Two pointer tricks for each index.

- Need to remove duplicate:
    - outer loop: If $nums[i] == nums[i-1]$
    - inner loop: After finding the triplets, check if the next triplet is the same as the previous one while moving the left and right pointers.
# Two pointer


## Problems

### 15. 3Sum

- Two pointer tricks for each index.

- Need to remove duplicate:
    - outer loop: If $nums[i] == nums[i-1]$
    - inner loop: After finding the triplets, check if the next triplet is the same as the previous one while moving the left and right pointers.


### 19. Remove Nth Node From End of List

- Brute force: Loop once to determine the length, and then in the subsequent iteration, identify the node to remove.

- Two pointer (fast and slow): Position the fast pointer n steps ahead of the slow pointer and loop until the fast pointer reaches the end.
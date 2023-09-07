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

### 75. Sort Colors

- Use three pointers.

### 151. Reverse Words in a String

`In Python, strings are immutable, so any operation that modifies a string will inherently require additional space`

- One line solution:

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
```

- Use two pointers:  
Start from the end and keep adding words until the back pointer is less than 0.

### 680. Valid Palindrome II *

**Note on Palindrome Verification:**
- After confirming matching characters at positions \(i\) and \(j\) in string \(s\), focus shifts to the substring between \(i\) and \(j\).
    - If the characters at the two pointers are the same, move the pointers towards the middle.
- If the inner substring is a palindrome, the entire string is too.
- If the inner substring is not a palindrome, the entire string is not either.
    - However, we are allowed to remove one character from the string.
        - If the characters are different, check if the substring without the left pointer is a palindrome. If not, check if the substring without the right pointer is a palindrome.

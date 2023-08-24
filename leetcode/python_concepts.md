# Python

## Class

- `self` refers to the instance of the Solution class on which the method is called.
    - Instance-level attributes are specific to each instance of the class and are typically defined within methods using self.

```python
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDistance = 1e9
        self.prevNode = None
```

## Array

- `isalnum()` - The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

## QUEUE

- `list.pop(0)` removes the first element. All remaining elements have to be shifted up one step, so that takes $O(n)$ linear time.
    - Instead, use `collections.deque(list)` to get $O(1)$. 
    - `queue = deque()`
    - `u = queue.popleft()`


## Binary search

- `bisect_left(list, num, beg, end)`: This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the leftmost position where element has to be inserted is returned. 

This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered. 

```python
li = [1, 3, 4, 4, 4, 6, 7]
print (bisect.bisect_left(li, 4)) # 2
```
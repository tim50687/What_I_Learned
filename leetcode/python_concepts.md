# Python

## %

> Python’s modulo operator (%) always returns a number having the same sign as the denominator. This is `different` from C and languages inspired by it, which return the remainder having the same sign as the numerator.

- -a % b = Add +b to -a until you reach either 0, or positive number

- a % -b = Subtract -b to a until you reach either 0 or negative number

### If you wanna access the specific index in the circular array, use the following:

```python
def get_next(_index):
    temp = _index + nums[_index]
    return (temp % n) 
```


## Scope

 In Python, if you define a function within another function, it becomes a local function to that enclosing function. However, the function must be defined before it is used.

## Function

- `divmod()` - The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).

```python
x = divmod(5, 2)
# x = (2, 1)
```

> Can be used to get each digit of a number. Also, get the remaning number after removing the last digit.

```python
while number > 0:
    number, to_be_add = divmod(number, 10)
```

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

## Tuple unpacking

In the tuple unpacking example, such as `x, y = 10, 20`, you're not actually modifying a tuple. Instead, you're using a tuple-like syntax to perform multiple assignments in a single line. Here's a breakdown:

1. `10, 20` on the RHS creates an implicit tuple `(10, 20)`.
2. The LHS `x, y` is a `pattern that tells Python to expect multiple values for assignment`. It's tuple-like in its structure, but it doesn't represent an actual tuple object in memory.
3. Python unpacks the values from the RHS tuple and assigns them to the variables on the LHS. Specifically, `x` is assigned the value `10`, and `y` is assigned the value `20`.

At a lower level, Python is doing the following:

1. **Tuple Creation**: The expression `10, 20` implicitly creates a tuple `(10, 20)`. This tuple holds the values `10` and `20`.

2. **Tuple Unpacking**: The left-hand side `x, y` indicates to Python that it should unpack the values from the tuple. It does this by iterating over the tuple and assigning each value to the corresponding variable on the left.

3. **Assignment**: As Python iterates over the tuple `(10, 20)`, it assigns the first value (`10`) to `x` and the second value (`20`) to `y`.

## min

### To get the smallest string in a list
```python
Letters = ["This", "is", "b","a", "sentence"]

print(min(Letters, key=len))
```

## Round up

rounded_up = -(-numerator // denominator)

## Reference

In python, array is mutable, se if you do something like this `dp = [[]] * (_len + 1)`, each element in the array will be the same reference. So if you change one element, all the element will be changed.

Instead, if you do this `dp = [[] for _ in range(_len + 1)]`, each element will be different reference.

### Contrast with the * Operator
When you use the * operator, like in `[[]] * 4`, Python doesn't create new objects for each element in the resulting list. Instead, it copies the reference to the `original object` (in this case, the empty list []) multiple times. Thus, all elements in the resulting list refer to the same object.


## Create immutable object in global scope

- If you want to use it in the nested function, you need to use `nonlocal` keyword. Becase it's immutable, when you change the value in the nested function, it will create a new object, so you need to use `nonlocal` to change the value in the global scope.

> Use the `nonlocal` keyword if curr_str is defined in an enclosing function but not in the global scope

> Use the `global` keyword if curr_str is defined in the global scope



## See if the element in the array is visited or not

- Create a array that mark the element is 1 or 0, so that you can see if the element is visited or not.


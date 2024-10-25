# Stack

> Hint: you can use else for while loop.

> Hint: isdigit() is a built-in method that returns True if all the characters are digits, otherwise False.

> Hint: stack.peek() to see the top element. if stack is empty raise an exception.

## Pattern

1. Handle nested relationships where the last element is the first to be processed.

2. If you only care about the most right element, you can use a stack.


## 394. Decode String *

Two situation:

```python
"3[a]2[bc]"
"3[a2[c]]"
```

Add char to the stack until you reach ']'. There will be 2 situations:

1. next char is close bracket ']': pop all the char until you reach open bracket '['. Then pop the number before '[' and repeat the char.

2. next char is digit which represents another pattern.

### Logic 

- Last in first out: we know that when we readh ']', we need to pop all the char until we reach '['. So we can use stack to store the char. `However`, can we put it to the ans? `No`, Because there might be nested pattern. So we need to store the char in the stack and repeat the char when we reach ']'.
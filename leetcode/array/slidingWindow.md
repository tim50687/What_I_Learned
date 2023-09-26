# Sliding Window
- <font color="#3382FF">A subarray can be defined by two indices, the start and end.</font>
- Algorithm:
	- Define a pointer for the left and right bound that represents the current window, usually both of them starting at 0.
	- Iterate over the array with the right bound to add elements to the window.
	- Whenever the constraint is broken, remove the elements from the window by incrementing the left bound until the condition is satisfied again.

> A sliding window guarantees a maximum of `2n` window iterations - the right pointer can move n times and the left pointer can move n times. Sliding windows algorithms run in linear time.



## Problems

### 187. Repeated DNA Sequences

- If you can deal with hash table while moving the window, deal with it.
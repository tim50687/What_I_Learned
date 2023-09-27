# Sliding Window
- <font color="#3382FF">A subarray can be defined by two indices, the start and end.</font>
- Algorithm:
	- Define a pointer for the left and right bound that represents the current window, usually both of them starting at 0.
	- Iterate over the array with the right bound to add elements to the window.
	- Whenever the constraint is broken, remove the elements from the window by incrementing the left bound until the condition is satisfied again.

> A sliding window guarantees a maximum of `2n` window iterations - the right pointer can move n times and the left pointer can move n times. Sliding windows algorithms run in linear time.

## Dynamic Sliding Window

- Let's say we found the valid window index 0 -> 8, then we move the right pointer to 9, and the window is no longer valid.
	- That means, for index 0, this is the best you can do.
		- We then now check if the window is valid by moving the left pointer += 1 (`See what is the next left index we can start`).
		- If the window is invalid, we can keep moving the left, but why?
			- That means, 1 -> 8 cannot grow larger.
			- In addition, Answer of 0 -> 8 is better than 1 -> 8, there's no point to keep focus on index 1.
	- Once we again find the valid left index, we can move the right pointer again, to see what is the best that left index can do.

## Problems

### 187. Repeated DNA Sequences

- If you can deal with hash table while moving the window, deal with it.

### 424. Longest Repeating Character Replacement **

- In the substring, we only want to replace the less frequent letter. 
	- window.length() - mostFreqLetterCount <= k


# Top K Elements

## 703. Kth Largest Element in a Stream

Use a min heap to store the top k elements. The heap size is k

We can focus on only the top k elements in the heap. 

- If the incoming element is larger than the smallest element in the heap
    - incoming element is also larger than k + 1...n elements in the heap
- If the incoming element is smaller than the smallest element in the heap
    - kth largest element is still the smallest element in the heap

> In init, there might be the case that that the length of the heap is less than k. In this case, we don't pop out the elements from the heap.

> In add(), we always push the element into the heap. Before add(), if heap size + 1 == k, we don't need to pop out the smallest element in the heap.



## 767. Reorganize String

Use Max_heap data structure to store the frequency of each character. Then start from the most frequent character, append it to the result string.

### we can use greedy, use hashmap, not heap

> If most frequent character is greater then n/2 (ceil), then `it is impossible to reorganize the string`. Else: it is possible to reorganize the string.

Now we know that most frequent can be placed in the answer string by index 0, 2, 4, 6, 8, ... and so on. (Best arrangement without any two same characters are adjacent)

Next, just finish even ideces if it's not finished yet. Then, finish odd indices. (`don't care about frequency of the rest of the characters`)


#### Proof 

For `If most frequent character is greater then n/2 (ceil), then there must be two character adjacent to each other`, you can use `pigeonhole principle` to prove it.

But for the whole problem, don't know how to prove it, just remember the algorithm.

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




# Depth First Search 


## 430. Flatten a Multilevel Doubly Linked List

### How to recursively traverse the linked list?

> If we just want to print out the value, we can use preoder traversal.

> Or if every node is doing the same thing, we can use preoder traversal.

`But`

Here, for the `next`, we just need to keep going to the right, so we can use while loop to traverse the linked list horizontally.

for the `child`, we need to deal with that if we see that first, so inside the while loop, before you go right, if there's a child, you deal with that first.

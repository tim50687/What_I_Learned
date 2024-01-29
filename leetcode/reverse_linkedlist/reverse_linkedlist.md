# Reverse Linked List 

> A sublist in itself is a linked list. -> use recursion!

## 206. Reverse Linked List

> think about what stops you, then go back and store that 
> visualize it

- we don't have the access to previous node, so we need to store the previous node in a variable

- While we point curr back to the prev, we don't have the next node, so we need to store the next node in a variable

## 25. Reverse Nodes in k-Group (do it again)

Recursion : reverse_k_nodes(head, k).next = reverse_k_group(ptr, k)

1. we have to figure out where is the next 

2. Set the recursive head to record the solution

3. Deal with node_len < k (`use small example to visualize how to deal with it`)
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

Iterative: 

We need four variable

1. I need to where where is the next start of the linked list, or else once we reverse it , we can not get it

2. Save the prev reversed_list tail

3. Current recursive head, and tail

## 143. Reorder List (do it again)

- Reverse the second part of the list and then merge two list together


## 1721. Swapping Nodes in a Linked List

> Cool trick: How to find the kth node from the end of the list?
> Traverse the list until kth node, once we find it, set the end node to the head (Now they have k node between them), and then keep going until the curr is at the end. The head node is the kth node from the end of the list.


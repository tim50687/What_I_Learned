# Binary Search Tree

- At most 2 children

- left child's value less than parent
- right child's value greater than parent

## Insertion

- Search until you find the right parent to insert the node + remember the parent

- Insert based on the value

- O(h), where h == height of the tree == log(n)


## 450. Delete Node in a BST *

- 3 cases
    - No child: We can simply remove the node from the tree.
    - One child: We can just replace the node with its child.
    - Two children: We need to replace node with its successor.
        - Right node: Replace node with right node
        - Right node's `leftmost` node: 
            - 1. Replace `leftmost` node with its right child
            - 2. Replace node with `leftmost` node

> Rememebr to deal with remove node is root (In my algorithm , only 0 or 1 child case)
> 2 children, because we are switching the value, we don't deal with the root case where parent is None

```python
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        parent = None
        # search if the node is in the tree
        while curr and curr.val != key:
            parent = curr
            if curr.val > key:
                curr = curr.left
            elif curr.val < key:
                curr = curr.right
        if not curr:
            return root
        
        # deal with 0 child
        if not curr.left and not curr.right:
            # if root
            if not parent:
                return parent
            if curr == parent.left:
                parent.left = None
            elif curr == parent.right:
                parent.right = None
        
        # deal with 1 child
        elif not curr.left: # has right child
            if not parent:
                return curr.right
            if curr == parent.left:
                parent.left = curr.right
            elif curr == parent.right:
                parent.right = curr.right


        elif not curr.right: # has left child
            if not parent:
                return curr.left
            if curr == parent.left:
                parent.left = curr.left
            elif curr == parent.right:
                parent.right = curr.left

        else:
            p = None
            min_right_sub_tree = curr.right
            
            while min_right_sub_tree.left:
                p = min_right_sub_tree
                min_right_sub_tree = min_right_sub_tree.left
            
            if p:
                p.left = min_right_sub_tree.right
                curr.val = min_right_sub_tree.val
            else:
                curr.right = min_right_sub_tree.right
                curr.val = min_right_sub_tree.val
        
        return root
```
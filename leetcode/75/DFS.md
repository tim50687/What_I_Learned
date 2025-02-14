# DFS

> `nonlocal` is used when you want to modify a variable in an enclosing scope (i.e., in a function that’s outside the current function but not global).

> You can read outer-scope variables freely within an inner function.

> Integers are immutable, if you pass them into a function, you can't change them. You have to use nonlocal `But you can change the value of a list.`

> If you pass an value as an argument to each recursive call, each recursive call get's its own copy of the value. If you pass a list, each recursive call gets a reference to the same list.

> DFS (Depth-First Search) in its general form is often similar to `pre-order` traversal (Root → Left → Right) when applied to binary trees

> You can modify the contents of a hashmap (dictionary) or an array (list) inside an inner function without using nonlocal or global, because they are mutable objects. However, if you try to reassign the entire variable, you will need nonlocal or global.

> `Think of DFS like recursion` (problem can be solved by sub-problems)

> If you try to reassign a variable in an inner function, Python will create a new local variable in the inner function, and the outer variable will remain unchanged.


> n - 1 edges means there's no 

## 437. Path Sum III

> If you see sum -> think about `prefix sum`

Idea: How to find sum of sub path? `prefix sum` is the key.

Ans: We can use a hashmap to store the prefix sum of the path from the root to the current node. Then, we can use this hashmap to find the number of sub-paths that sum up to `target` ending at the current node.

Note: Don't forget add to asnwer if current node == targetSum.

## 1372. Longest ZigZag Path in a Binary Tree *

> This is easier to use sub problem logic to solve the problem. So, sometimes when you see dfs, we can also use sub problem logic to solve the problem.

Problem can be solved by sub problem: `longest path from left child` and `longest path from right child`. You just gotta return the `max` of the two.

For the helper function: 

    - If left child:
        - Go left 
        - Go right

    - If right child:
        - Go right
        - Go left

    return depth 


## 236. Lowest Common Ancestor of a Binary Tree *

Two cases:

- Root is P or Q
- P and Q are in left and right subtree

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find_root_helper(root):
            # base case
            if not root:
                return False

            if root == p or root == q:
                return root

            find_left = find_root_helper(root.left)

            find_right = find_root_helper(root.right)

            if find_left and find_right:
                return root
            elif find_left:
                return find_left
            else:
                return find_right

        ans = find_root_helper(root)

        return ans
```



### Stop searching when you find the node

```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def helper(root):
            if not root:
                return root
            # base case
            if root and root.val == val:
                return root
            # go left
            left_result = helper(root.left)
            if left_result:
                return left_result
            # go right
            right_result = helper(root.right)
            if right_result:
                return right_result


        ans = helper(root)

        return ans if ans else None
```
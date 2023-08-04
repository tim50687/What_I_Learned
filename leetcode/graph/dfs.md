# Depth First Search

## Problem 

### 797. All Paths From Source to Target

- Use DFS to explore if path exists.  

- Here we want to explore `black node` (already finished) to find alternative path.
    - If we find the target by DFS, we will mark it as BLACK.

    - Normal DFS, we will ignore GRAY or BLACK node, but here we don't ignore in order to see if there's another path to go to target.

- Use pop() when:
    - you reach a `dead end` or `finish all the searches for current node`.
    - Since there's no cycle, if you find the target, store the path -> done the work -> pop(). 

#### Time complexity
- Whenever heard DAG, imagine a line.
- There's $O(2^V)$ possible path from source to target.
    - After we find a path, we need to store the path (make a copy) to answer. There may be a N number of nodes to reach that Nth node. $O(V)
- RT = $O(V*2^V)$
# Depth First Search

## Problem 

### 1971. Find if Path Exists in Graph

$\textcolor{red}{\text{Practice again and understand the recursion}}$

```python
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited = [False] * n

        def dfs(source):
            visited[source] = True
            if source == destination:
                return True
            
            for neighbor in adj_list[source]:
                if visited[neighbor] == False:
                    # return True if you found it, otherwise, keep dfs searching
                    if dfs(neighbor):
                        return True
        
            return False
        return dfs(source)
```


### 797. All Paths From Source to Target

- Use DFS to explore if path exists.  

- Here we want to explore `black node` (already finished) to find alternative path.
    - If we find the target by DFS, we will mark it as BLACK.

    - Normal DFS, we will ignore GRAY or BLACK node, but here we don't ignore in order to see if there's another path to go to target.

- Use pop() when:
    - you reach a `dead end` or `finish all the searches for current node`.
    - Since there's no cycle, if you find the target, store the path -> done the work -> pop(). 

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        temp_ans = []
        target = len(graph) - 1

        def dfs(source):
            temp_ans.append(source)
            
            if source == target:
                ans.append(temp_ans.copy())
                temp_ans.pop()
                return 

            for neighbor in graph[source]:
                dfs(neighbor)
            
            # if you can't find any
            temp_ans.pop()

        dfs(0)

        return ans
```

#### Time complexity
- Whenever heard DAG, imagine a line.
- There's $O(2^V)$ possible path from source to target.
    - After we find a path, we need to store the path (make a copy) to answer. There may be a N number of nodes to reach that Nth node. $O(V)
- RT = $O(V*2^V)$
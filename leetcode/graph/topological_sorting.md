# Topological Sorting

## When to use? 

When selecting courses for the next semester in college, you might have noticed that some advanced courses have prerequisites that require you to take some introductory courses first.

## Two ways to implement topological sorting

1. Call DFS on every vertex  
    - The last vertex to finish must have an in-degree of 0.
    - Sort V by decreasing order.  
    (Like the thing that must be done first will always be finished later by DFS)

2. Repeatedly find a vertex of in-degree 0.

    ### Why Removing In-Degree 0 Vertices Works? 
    - **In-Degree 0 Vertices**: A vertex with in-degree 0 has no incoming edges. This means that there are no prerequisites for this vertex, and it can be placed at the beginning of the ordering.

    - **Removing Vertices and Outgoing Edges**: Once a vertex with in-degree 0 is found and added to the ordering, it and its outgoing edges are removed from the graph. This may reduce the in-degree of other vertices to 0, allowing them to be added to the ordering next.

    - **Directed Acyclic Graph (DAG)**: In a DAG, there must be at least one vertex with in-degree 0 (otherwise, there would be a cycle). So, the algorithm can always find a next vertex to add to the ordering.

    - **Ordering Reflects Dependencies**: By always choosing vertices with in-degree 0, the algorithm ensures that all prerequisites for a vertex are placed earlier in the ordering.

## Problem 

### 210. Course Schedule II

- Use deque

- Use an array to store the in-degrees. When you need to remove a vertex that you have visited, you can simply call array[i] -= 1 instead of removing it from a dictionary, which would cost $O(E)$. 

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)

        # make an array to store the in-degree, play with this array instead of remove from dictionary O(E)
        in_degree = [0] * numCourses

        for i in prerequisites:
            adj_list[i[1]].append(i[0])
            in_degree[i[0]] += 1

        ans = list()
        q = collections.deque()
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            done = q.popleft()

            ans.append(done)
            # go through dictionary to remove done node
            for neighbor in adj_list[done]:
                in_degree[neighbor] -= 1   
                # we only care about vertex from positive to 0
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

           


        return [] if len(ans) != numCourses else ans
```


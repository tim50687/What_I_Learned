# Minimum Spanning Tree

## Problem 

### 1584. Min Cost to Connect All Points

- `Prim` is just like `Dijkstra`, the only difference is `DECREASE-KEY`.

- `Prim` proved by cutting property; `Dijkstra` proved by contradiction.

#### Python code

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def cal(u1, u2, v1, v2):
            return abs(u1 - v1) + abs(u2 - v2)

        heap = [(0, tuple(points[0]))]

        tree = set()

        ans = 0
        
        while heap:
            u = heapq.heappop(heap)

            if u[1] in tree:
                continue
            
            tree.add(u[1])
            ans += u[0]

            if len(tree) == len(points):
                return ans
            for i in points:
                if tuple(i) not in tree:
                    dist = cal(u[1][0], u[1][1], i[0], i[1])
                    heapq.heappush(heap, (dist , tuple(i)))
```
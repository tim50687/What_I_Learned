# Bellman Ford

From u to v, edges at most V - 1.

At First round of V - 1, if I relax all the edges, I can make sure that I relax the first edge of all shortest path.
And so on, and then if I relax the edges again, I can make sure that I relax the second edge of all shortest path.

Since the longest path is V - 1, if I relax the edges V - 1 times, I can make sure I will get the shortest path from source to every other vertex by `Path-Relaxation property`.
## Problem 

### 787. Cheapest Flights Within K Stops

#### Review how bellman ford go relaxation in each loop

- During relaxation, we cannot modify the distance array in place, as each edge is independent while relaxing. Therefore, we need a temporary array to store the result after relaxing.

- If the distance array represents relaxing m times, create a temporary array to represent relaxing m + 1 times. Since relaxing m + 1 times will be at least as good as relaxing m times, we can use temp = distance_array.copy() to initialize it.

- During relaxation, we relax the distance array to see if it can be better than temp. It's like saying, "You must be at least this good, but see if you can do better."

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        def relax(u, v, w, distancelist, temp):
            if distancelist[u] + w < temp[v]:
                temp[v] = distancelist[u] + w
            

        distance_list = [float("inf") for i in range(n)]

        distance_list[src] = 0
        

        for i in range(k + 1):
            # store the updated distances for the next iteration without affecting the current iteration
            temp = distance_list.copy()
            for edge in flights:
                relax(edge[0], edge[1], edge[2], distance_list, temp)
            distance_list = temp

        return -1 if distance_list[dst] == float("inf") else distance_list[dst]


```
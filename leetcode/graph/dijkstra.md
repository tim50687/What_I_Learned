# Dijkstra

- There's no DECREASE-KEY(`Relax`) in heapq, we just simply push the updated vertex to the heap. There might be identical vertex in the heap, but heappop() will get the min one -> same effect. `# Note: Need to deal with the next same vertex`

## Problem 

### 743. Network Delay Time

- Last node to be added in dijkstra tree will be the longest path among the shortest path.

#### Python code

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Make adjacency list
        adj_list = defaultdict(list)

        for x,y,w in times:
            adj_list[x].append((y,w))

        # initialize min_heap (For choosing next vertex) 
        # unlike PRIM, the distance here is cumulative
        distance = [(0, k)]
        
        # initialize tree
        d_tree = set()

        # find answer
        ans = 0

        # You will deal with every vertex if a valid G
        while distance:
            sp, node = heapq.heappop(distance)

            # Deal with duplicate
            if node in d_tree:
                continue
            d_tree.add(node)
            
            # last node to be add would be the longest path in shortest path
            if len(d_tree) == n:
                return sp
            
            for neighbor, esp in adj_list[node]:
                if neighbor not in d_tree:
                    # Since there's no DECREASE-KEY in heapq,
                    # we just simply push the updated vertex to the heap.
                    # There might be identical vertex in the heap, but 
                    # heappop() will get the min one -> same effect.

                    # Note: Need to deal with the next same vertex
                    heapq.heappush(distance, (sp + esp, neighbor))


        return -1

```
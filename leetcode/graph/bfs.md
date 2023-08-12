# Breadth First Search

## Concepts

- In BFS(), whenever you add vertex to the queue -> visit.

- If you process things layer by layer, you are still doing the same thing, however, here you're grouping the layer together, so that after the for loop, you know this layer is complete:
    - Use a for loop inside the while loop  
    ```python
    while q:
            # deal with layer by layer
            for i in range(len(q)):
                ...
    ```

## Problem

# 994. Rotting Oranges

- For 2D traversal problems, instead of using:  
if row == 0 do ...  
if row == len(grid) do ...  
**Use this approach**
```ur, uc = q.popleft()            
    for r, c in [(1,0), (-1,0), (0, 1), (0,-1)]:
        nb_r, nb_c = ur+r, uc+c
        
        # check border
        if nb_r < 0 or nb_r == len(grid) or nb_c < 0 or nb_c == len(grid[0]):
        continue
```

> Rather than setting specific rules for certain rows or columns, check the 4-directionally adjacent vertices for every target vertex and simply discard any vertex that is out of bounds.

1. It's more concise.
2. It's easier to modify. If you want to check 8 directions (including diagonals) instead of 4, you can simply update the directions list.
3. It's less prone to errors. By simplifying the logic and removing repeated code, there's a smaller chance of introducing bugs.

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()

        visit_rotted = set()
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visit_rotted.add((i, j))
                if grid[i][j] != 0:
                    count += 1
        # if rotten orange == 0 and count > 0 (impossible to rot)
        if len(q) == 0 and count > 0:
            return -1
        elif len(q) == 0 and count == 0: # nothing to rot
            return 0

        minute= -1
        while q:
            
            # deal with layer by layer
            for i in range(len(q)):
                ur, uc = q.popleft()
                
                for r, c in [(1,0), (-1,0), (0, 1), (0,-1)]:
                    nb_r, nb_c = ur+r, uc+c
                    
                    # check border
                    if nb_r < 0 or nb_r == len(grid) or nb_c < 0 or nb_c == len(grid[0]):
                        continue
                    
                    # check blank
                    if grid[nb_r][nb_c] == 0:
                        continue

                    if (nb_r, nb_c) not in visit_rotted:
                    
                        q.append((nb_r, nb_c))
                        grid[nb_r][nb_c] = 2
                        visit_rotted.add((nb_r, nb_c))
            minute += 1

        

        return minute if len(visit_rotted) == count else -1
```

#### Time complexity

$O(N*M)$, where $N * M$ is the size of the grid. BFS go through every slot in the grid.
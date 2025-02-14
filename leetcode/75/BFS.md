# Breath First Search

> Only need curr_len if you want to do something layer by layer. Or else 

## 1466. Reorder Routes to Make All Paths Lead to the City Zero *

```python
# we gotta make sure every node pointed to 0
# create a neighbors hashmap reps 2 connected nodes
# started from 0 
# do bfs
```


## 1926. Nearest Exit from Entrance in Maze *

> Trick to make adjacency list: `[(1,0), (-1,0), (0,1), (0,-1)]`. Use third loops to iterate through the directions.

> Actually, We don't need to make adj list, we can just use directions to check the neighbors

## 994. Rotting Oranges *

> We can use BFS and start from different sources by putting them into queue at the beginning.
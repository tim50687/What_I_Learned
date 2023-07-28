# Breadth First Search

## Concepts

- In BFS(), there are two situations to check if a node has been visited.
    - `Explore`. Don't explore the nodes that have already been visited.
    -  `Dequeue/ Visit`. Since we might discover the same node several times, once we dequeue/visit the node, we want to avoid duplicate visits.
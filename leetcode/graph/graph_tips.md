# Graph

## Properties

1. Triangle inequality: `d(u, v) + d(v, w) >= d(u, w)`

You can not be better than the best.

2. Path relaxation property:

Given a shortest path from u to v, if we relax the path in the order of the vertices, the path is still the shortest path.

## Tips

- If the range of weights in edges is limited to a small range, we can represent the weight as an index and push the corresponding vertices into that index. (like counting sort). `Rather than using heap`  
    - e.x. Prim algorithm.

- Use `Disjoint Set` to detect if there's a cycle. Use `Bellman Ford` to detect if there's a negative cycle.

## Adjencency matrix vs Adjencency list

- Do the `Adjencency matrix` or `list` first to avoid finding neighbor several times.
    - Time complexity of finding neighbor in `Adjencency matrix` is O(V^2), while in `Adjencency list` is O(E).
    - 0 <= E <= V^2 (`Graph can be not connected`)

## Path

Sequence of connected edges.

## Tree

It's a connected graph without a cycle. (`Connected graph: There's a path between every pair of vertices`)

- Choosing a `root` will `imply a direction` on the edges. 

- Path from u to v in the tree is unique. (Use any edge once)


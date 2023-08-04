# Graph

## Tips

- If the range of weights in edges is limited to a small range, we can represent the weight as an index and push the corresponding vertices into that index. (like counting sort). `Rather than using heap`

- Use `Disjoint Set` to detect if there's a cycle. Use `Bellman Ford` to detect if there's a negative cycle.

- Do the `Adjencency matrix` or `list` first to avoid finding neighbor several times.
# Functions

## ROW_NUMBER()

**MySQL Ranking Functions Note:**

**Introduction**:
- With the advent of MySQL 8.0, four ranking functions were introduced.
- These functions provide various ways to rank the rows returned by a result set.
- They share similar syntax and operate in analogous ways.

**Ranking Functions**:
1. `ROW_NUMBER()`
2. `RANK()`
3. `DENSE_RANK()`
4. `NTILE(integer_expression)`

**Common Syntax**:
```
function_name() OVER ([partition_clause] order_clause)
```

**Key Takeaways**:
- The introduced ranking functions provide a robust way to rank rows in MySQL result sets.
- The `ORDER BY` clause inside the ranking function defines the sequence of rows.
- The optional `PARTITION BY` clause allows for further categorization of rows before they are ranked.
- `ROW_NUMBER()` will always give unique numbers starting from 1 for each partition.
- These functions offer the advantage of clearly segmenting and numbering data, which is invaluable in many analytic operations.

> The issue with the query is in the `ORDER BY` clause inside the `ROW_NUMBER()`. When you use `ROW_NUMBER()` in conjunction with an aggregate function in the same query, you cannot reference the aggregate column by its alias directly within the window function. Instead, you need to use the actual aggregate function.


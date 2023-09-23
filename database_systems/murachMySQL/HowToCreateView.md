# How to create views

SELECT queries can be complicates, particularly if they use multiple joins, subquires, and/or aggregate functions.

Because of that, you may want to save the queries you use regularly. One way to do that is to store the statement in a script. Another way is to create a view.

## How views work

- `view` is a SELECT statement that's stored in the database as a database object. It's similar to a table in that it has columns and rows, but it doesn't store data. Instead, it's a virtual table that's created by a query.

- Views is dynamic. 

    1. **Updatable Views**: Some views are updatable, meaning you can perform `INSERT`, `UPDATE`, or `DELETE` operations on them. When you delete a row from an updatable view, the change is propagated to the underlying base table, and the corresponding row in that table is deleted.

    2. **Non-Updatable Views**: Some views are not updatable due to their complexity. For example, views that involve joins across multiple tables, aggregate functions, or certain types of subqueries might not support deletions. If you attempt to delete a row from such a view, the database system will raise an error.

    3. **Cascading Effects**: If there are any triggers, cascading deletes, or referential integrity constraints associated with the base table, those will also come into play when a row is deleted through the view.


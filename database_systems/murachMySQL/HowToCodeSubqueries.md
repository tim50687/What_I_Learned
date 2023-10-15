# Sub queries

Subquery can be coded in the `SELECT`, `FROM`, `WHERE`, or `HAVING` clause.

1. When a subquery returns a single value, you can use it anywhere you would normally use a single value.

2. Subquery can also return a list of values(a result set that has one column). In this case, you can use the subquery in a comparison operator such as `IN`, `NOT IN`, `ANY`, or `ALL`.

3. Subquery can return a table of alues(a result set that has multiple columns). In this case, you can use the subquery in the `FROM` clause.

4. You can code a subquery within another subquery. However, nested subqueries can be difficult to read. So, you should avoid nesting subqueries more than two or three levels deep.

5. Subquery **cannot** be included in the `ORDER BY` clause.

## In a WHERE clause

```sql
select invoice_number, invoice_date, invoice_total 
from invoices
where invoice_total > (select avg(invoice_total) from invoices)
order by invoice_total
```

- you must enclose the subquery in parentheses.

```sql
SELECT vendor_ id, vendor_name, FROM vendors
WHERE vendor_id NOT IN
(SELECT DISTINCT vendor_id
FROM invoices) ORDER BY vendor_id
```

- When you use the IN operator, the subquery must return a single column of values.

```sql

SELECT invoice_r.t,,rnh~r, invoice_date,
invoice_total - payment_total - credit_total AS halance_due
FROM invoices
WHERE invoice_total - payment_total - credit_total > 0
AND invoice total - payment_total - credit total < 
(
SELECT AVG(invoice_total - payment_total - credit_total)
FROM invoices
WHERE invoice_total - payment_total - credit_total > 0
)
ORDER BY invoice_total DESC
```

- If you code a search condition without the `AND`, `SOME`, `ALL` operator, the subquery must return a single value.

- If you code a search condition with the `AND`, `SOME`, `ALL` operator, the subquery must return a list of values.

### ALL

The condition must be true for all the values returned by a subquery.

### ANY or SOME

The condition must be true for at least one of the values returned by a subquery.

### Correlated subqueries

Correlated subquery executeted once for each row that's processed by the main query.

```sql
select vendor_id, invoice_numner, invoice_total
from invoice i
where invoice_total >
(select avg(invoice_total) from invoices
where vendor_id = i.vendor_id)
order by vendor_id, invoice_total
```
- A correlated subquery refers to a value that's provided by a column in the main query.

- To do the correlated subquery, the WHERE clause of the subquery refers to the vendor_id value of the main query.

- You can use a table alias for the table in the main query if two table are identical.

### How to use the EXISTS operator

1. **The Concept of EXISTS:**  
   The `EXISTS` operator in SQL is used to determine if a subquery returns any results. It doesn't actually return those results or rows, but instead, it simply returns `TRUE` if there are any rows returned by the subquery and `FALSE` otherwise.

2. **Correlated Subquery:**  
   A correlated subquery is a subquery that references columns from the outer query. It relies on the outer query to process each row.

3. **The Example:**  
   The provided example query aims to find all the vendors that don't have any associated invoices. Here's the main query:

   ```sql
   SELECT vendor_id, vendor_name, vendor_state 
   FROM vendors
   WHERE NOT EXISTS (
       SELECT *
       FROM invoices
       WHERE vendor_id = vendors.vendor_id
   );
   ```

4. **Explanation of the Example:**

   - The main query is selecting vendors from the `vendors` table.
   - For each `vendor` in the `vendors` table, the subquery checks if there are any `invoices` associated with that particular vendor. It does this by checking if the `vendor_id` in the `invoices` table matches the `vendor_id` of the current row in the `vendors` table. This is where the subquery is correlated.
   - The `EXISTS` returns `TRUE` if any such invoices are found, otherwise `FALSE`.
   - The `NOT EXISTS` condition in the main query then checks if the result of the subquery was `FALSE` (meaning there are no associated invoices for the vendor). If true, that `vendor` is included in the main query's result set.
   
5. **Why use EXISTS?**  
   One advantage of using `EXISTS` is that the database engine knows it can stop checking further once it finds a single row that meets the subquery criteria because it doesn't need to return all the rows, only a TRUE or FALSE. As a result, `EXISTS` can be more efficient in some scenarios compared to other methods.

6. **The Asterisk in the Subquery:**  
   Since `EXISTS` only checks for the presence of rows and doesn't actually return the rows or use the data in any columns, it doesn't matter what you put in the `SELECT` part of the subquery. Thus, it's customary to just use `*`.

In summary, the provided SQL query is a way to efficiently check which vendors in the `vendors` table don't have associated rows in the `invoices` table.

### How to code subqueries in the SELECT clause
**1. The First Query Using a Subquery in the SELECT clause**

```sql
SELECT vendor_name,
(SELECT MAX(invoice_date) 
 FROM invoices
 WHERE vendor_id = vendors.vendor_id) AS latest_inv 
FROM vendors
ORDER BY latest_inv DESC
```

- **Purpose**: For each vendor in the `vendors` table, the query wants to find the most recent `invoice_date` from the `invoices` table.
  
- **How It Works**: For every row in the `vendors` table, the subquery runs and looks for the maximum `invoice_date` in the `invoices` table for that specific vendor. This is a correlated subquery because the subquery references a column (`vendor_id`) from the outer query.

- **Output**: A list of vendors along with their most recent invoice date.

**Points to Note:**

- **Single Value**: The subquery in the SELECT clause must return a single value. If it were to return multiple values, the database wouldn't know which specific value to show for a given vendor. That's why functions like `MAX()` are used to ensure a single value is returned.

- **Correlated Subquery**: The subquery is correlated because it references a column from the outer query (`vendors.vendor_id`). For every vendor in the `vendors` table, the subquery checks the `invoices` table to find the latest invoice date for that vendor.

**2. The Second Query Using a JOIN**

```sql
SELECT vendor_name, MAX(invoice_date) AS latest_inv 
FROM vendors v
LEFT JOIN invoices i ON v.vendor_id = i.vendor_id 
GROUP BY vendor_name
ORDER BY latest_inv DESC
```

- **Purpose**: Achieves the same result as the first query but uses a different method.
  
- **How It Works**: Instead of using a subquery for each vendor, this query joins the `vendors` table with the `invoices` table on the `vendor_id` column. After joining, it groups the results by `vendor_name` and then calculates the maximum invoice date for each group (i.e., each vendor).

- **Output**: Similarly, a list of vendors with their most recent invoice date.

**Comparison Between the Two Methods**:

- **Performance**: Joins are generally more efficient than subqueries in the SELECT clause because databases are optimized for joining tables. In the first method, the subquery runs for each vendor, whereas, in the join method, the tables are combined just once.

- **Readability**: The JOIN method can be easier to understand at a glance. Seeing tables being joined and data aggregated with GROUP BY can be more intuitive than understanding multiple levels of queries.

- **Flexibility**: While joins are often preferred, subqueries can be more flexible in complex scenarios, especially when the logic doesn't lend itself easily to a straightforward join.

#### Breaking Down the Query

```sql
SELECT vendor_name, MAX(invoice_date) AS latest_inv 
FROM vendors v
LEFT JOIN invoices i ON v.vendor_id = i.vendor_id 
GROUP BY vendor_name
ORDER BY latest_inv DESC
```

1. **Tables Involved**: 
    - `vendors`: This table has details about vendors. 
    - `invoices`: This table has details about invoices, including a field for the date when each invoice was issued (`invoice_date`), and a field (`vendor_id`) indicating which vendor the invoice belongs to.

2. **Alias**:
    - `v`: This is an alias for the `vendors` table. It's a shorthand notation so that in other parts of the query, we can use `v` instead of `vendors`.
    - `i`: This is an alias for the `invoices` table. Similarly, we can use `i` instead of `invoices` in other parts of the query.

3. **LEFT JOIN**: 
    - This joins the `vendors` table with the `invoices` table based on matching `vendor_id`s. The reason for using a "LEFT JOIN" instead of a regular "INNER JOIN" is to make sure we still see vendors in the result even if they have no invoices (i.e., if a vendor doesn't have any associated invoice, they will still appear in the results with a null `latest_inv`).

4. **Grouping**: 
    - `GROUP BY vendor_name`: After joining the two tables, we'll have rows where a single vendor might be associated with multiple invoices. The "GROUP BY" clause groups these rows by the vendor name so that for each vendor, we can apply aggregate functions (in this case, `MAX`) on their associated invoice dates.

5. **Selecting Data**: 
    - `SELECT vendor_name, MAX(invoice_date) AS latest_inv`: For each group (i.e., each vendor), this selects the vendor's name and the maximum invoice date (i.e., the most recent invoice date). The `MAX(invoice_date)` gives the latest invoice date for each vendor. The `AS latest_inv` is an alias for this maximum date, making it easier to reference in the ORDER BY clause or read in the results.

6. **Ordering**: 
    - `ORDER BY latest_inv DESC`: Finally, the result is ordered by the latest invoice date in descending order. So, vendors with the most recent invoices will be at the top of the result.

## In the From clause


**Subqueries in the `FROM` Clause**

- **Inline View**: When a subquery is coded in the `FROM` clause, it can return a result set comprising any number of rows and columns. This type of result set is often called an "inline view."

- **Usage**: Subqueries in the `FROM` clause are commonly used to create inline views that offer summarized data, which can then be further processed or summarized by the outer/main query. An example is provided where the subquery aggregates invoice totals for each vendor and the main query further identifies the largest invoice total for the top vendor in each state.

- **Alias Requirement**:
  - **Table Alias**: Any subquery within the `FROM` clause must have an associated table alias. This alias is essential, even if it's not used in the outer query. In the provided example, the table alias "t" (for "temporary table") is used.
  - **Column Alias**: If you're calculating values within the subquery (like SUM, AVG, etc.), it's good practice to provide a column alias for these calculations. This makes it easier to reference these columns in the main query and also clarifies the purpose of the calculated column.

- **Example Query**:
  ```sql
  SELECT vendor_state, MAX(sum_of_invoices) AS max_sum_of_invoices 
  FROM
  (
    SELECT vendor_state, vendor_name, SUM(invoice_total) AS sum_of_invoices 
    FROM vendors v 
    JOIN invoices i ON v.vendor_id = i.vendor_id 
    GROUP BY vendor_state, vendor_name
  ) t
  GROUP BY vendor_state 
  ORDER BY vendor_state;
  ```

  Here, the inner subquery creates a result set (inline view) of vendor states, vendor names, and their associated total invoice amounts. The outer query then takes this inline view and finds the largest invoice amount for each state.

- **Takeaways**:
  - An inline view acts like a table in the scope of the main query.
  - Always assign a table alias to subqueries in the `FROM` clause.
  - Provide aliases for calculated columns in the subquery to make the main query more readable and to easily refer to those columns.

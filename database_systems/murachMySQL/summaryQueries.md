# Summary queries

## Aggregate functions

`Aggregate functions` perform calculations on a series of values and return a single summary value.

A query that contains one or more aggregate functions is called a *summary query*.

The most common aggregate functions are:

- `COUNT()` - returns the number of rows in a column

    **Note on SQL LEFT JOIN with COUNT:**

    When using a `LEFT JOIN`, if there's no matching entry in the right table, the fields for that table in the result set will contain `NULL` values.

    When applying the `COUNT` function to a field that might contain `NULL` values due to the `LEFT JOIN`:

    1. `COUNT` will only consider non-`NULL` values. 
    2. Any `NULL` values in the counted field will be excluded from the count.

    For instance, if we're counting songs by genre using a `LEFT JOIN`, and a particular genre has no songs associated with it, the `COUNT` for that genre will return 0.

    This behavior ensures that you get an accurate count of actual entries, without inflating the count with non-matching entries from the join.

- `SUM()` - returns the sum of the values in a column

- `AVG()` - returns the average of the values in a column

- `MIN()` - returns the minimum value in a column

- `MAX()` - returns the maximum value in a column


### ALL and DISTINCT

When you use these functions, you can also code the ALL or DISTINCT keyword to specify whether to include all values or only distinct values in the calculation.

- `ALL` - includes all values, including duplicates. But the exceptions are null values, which are excluded from the calculation except when you use the COUNT(*) function.

- `DISTINCT` - includes only distinct values, excluding duplicates and null values.
    - In most case, you will use DISTINCT only with the COUNT function. <- make  sense.

> you can't use ALL or DISTINCT with COUNT(\*), because the COUNT(\*) function always includes null values.

#### Description

- AVG, SUM: numeric values

- MIN, MAX, COUNT: numeric, date, string value.

## Queires that use aggregate functions

With 2 exceptions, a SELECT clause that contains an aggregate function can contain only aggregate functions.

1. If the column specifications results in a literal value.

```sql
SELECT 'After 1/1/2018' AS selection_date,
COUNT(*) AS number_of_ invoices, ROUND{AVG{invoice_total), 2) AS avg_invoice_amt, SUM{invoice_total) AS total_invoice_amt
FROM invoices
WHERE invoice_date > '2018-01-01'
```

In SQL:

- **`SELECT`**: Used to retrieve data.
  
- **“literal string”**: Represents a static string value. The actual value is determined by what's placed inside the quotes. For example, in `SELECT "Hello World"`, the output would be a single row with "Hello World".

2. If the query includes a GROUP BY clause. Then the SELECT clause can include any columns specified in the GROUP BY clause, as well as aggregate functions.

## GROUP BY clause

The GROUP BY clause deteremines how the selected rows are grouped, and the HAVING clause determinces which groups are included in the results.

GROUP BY and HAVING clauses are coded after the WHERE clause and before the ORDER BY clause. **That makes sense because the WHERE clause is applied before the rows are grouped, and the ORDER BY clause is applied after the rows are grouped.**

- In the GROUP BY clause, you list one or more columns or expressions separated by commas.

## Difference between WHERE and HAVING

- The WHERE clause is used to filter rows before they are grouped.
    - Cannot include aggregate functions.
    - Can refer to any columns in the base table.

- The HAVING clause is used to filter groups after they are created.
    - Can include aggregate functions.
    - Can only refer to columns included in the SELECT clause.


## **GROUP_CONCAT() in SQL**

- **Purpose**: The `GROUP_CONCAT()` function is used to concatenate values from multiple rows into a single string. It's particularly useful when working with grouped results.
  
- **Syntax**: 
  ```sql
  GROUP_CONCAT(column_name)
  ```

- **Example**:

  Consider a table named `vendors`:

  | vendor_id | vendor_name       | vendor_city  | vendor_state |
  |-----------|-------------------|--------------|--------------|
  | 1         | Vendor A          | Los Angeles  | CA           |
  | 2         | Vendor B          | San Francisco| CA           |
  | 3         | Vendor C          | San Diego    | CA           |
  | 4         | Vendor D          | Austin       | TX           |
  | 5         | Vendor E          | Dallas       | TX           |
  | 6         | Vendor F          | Phoenix      | AZ           |

  To get a list of cities for each state where vendors are located:

  ```sql
  SELECT vendor_state, GROUP_CONCAT(vendor_city) AS vendor_cities 
  FROM vendors 
  GROUP BY vendor_state 
  ORDER BY vendor_state;
  ```

  Result:

  | vendor_state | vendor_cities                            |
  |--------------|------------------------------------------|
  | AZ           | Phoenix                                  |
  | CA           | Los Angeles,San Francisco,San Diego      |
  | TX           | Austin,Dallas                            |

- **Note**: The result for the state of CA shows cities "Los Angeles", "San Francisco", and "San Diego" concatenated into a single string, indicating all the cities in CA with vendors. This provides a concise way to view grouped data.

## How to code aggregate window functions

Aggregate window functions are similar except that the groups, or partitions, aren't collapsed to a single row. Instead, the aggregate function is applied to each row in the partition.

- You can partition the rows by coding a PARTITION BY clause after the OVER clause.

- If you code an OVER clasuse with a PARTITION BY clause, the aggregate function is applied to each partition.

- If you code an ORDER BY clause on the OVER clause, the rows with each partition are sorted and the values from one row to the next are cumulative.

> The RANK() function, when used with the ORDER BY clause, assigns a rank to rows within each partition based on the specified ordering. In your query, you have used ORDER BY COUNT(incident_number) DESC, which means that rows within each district_name partition will be ranked based on the descending order of COUNT(incident_number)
# Summary queries

You might need to report sales totals by vendor or state.

## Aggregate functions

`Aggregate functions` perform calculations on a series of values and return a single summary value.

A query that contains one or more aggregate functions is called a *summary query*.

The most common aggregate functions are:

- `COUNT()` - returns the number of rows in a column

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

# How to retrieve data from a single table?

## SELECT

The `SELECT` clause is always the first clause in a SELECT statement. These columns are retireved from the based table named in the `FROM` clause.

> You can select a column that is calculated from other columns in the table. 
```sql
SELECT invoice_id, invoice_total,
credit_total + payment_total AS total credits
FROM invoices
WHERE invoice_ id = 17
```
> You can use the `CONCAT` function to combine two or more columns into a single column.
```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name
```

> Using alias. To include a space in the alias for the first column, you must enclose the alias in double quotes.
```sql
SELECT invoice_number AS "Invoice Number", invoice_date AS Date, invoice total AS Total
FROM invoices
```


The `WHERE`, `ORDER BY`, and `LIMIT` clauses are optional. If you don't include them, the database system will return all rows from the table.

- `WHERE` - determines which rows are returned.  

Between different date
```sql
SELECT invoice_n11mher, invoice_date, invoice_total FROM invoices
WHERE invoice_date BETWEEN '2018-06-01' AND '2018-06-30' 
ORDER BY invoice_date
```
Might return empty result
```sql
SELECT invoice_number, invoice_date, invoice_total FROM invoices
WHERE invoice_total > 50000
```
- `ORDER BY` - determines the order in which the rows are returned.
    - `ASC` - ascending order
    - `DESC` - descending order

    ```sql
    SELECT invoice_number, invoice_date, invoice_total 
    FROM invoices
    ORDER BY invoice_total DESC
    ```

- `LIMIT` - determines the number of rows that are returned.

#### Arithmetic operators

You can use arithmetic operators in the SELECT clause to perform calculations on the columns in a table.

- `+` - addition

- `-` - subtraction

- `*` - multiplication

- `/` - division (decimal_quotient)
    - `DIV` - division (integer_quotient)
    - `%` - modulus (remainder)

#### How to use functions

- LEFT() - returns a specified number of characters from the left side of a string.

- DATE_FORMAT() - formats a date value based on a specified format.

- ROUND() - rounds a number to a specified number of decimal places.

#### Without FROM clause

With mySQL, you don't have to code a FROM clause. This makes it easy to test expressions that include arithmetic operators and functions.

```sql
SELECT "Ed" AS first_name, "Williams" AS last_name, 
CONCAT(LEFT("Ed", 1), LEFT("Williams", 1)) AS initials
```

#### How to eliminate duplicate rows
- `DISTINCT` - eliminates duplicate rows from the result set.
```sql
SELECT DISTINCT vendor_city, vendor_state
FROM vendors
ORDER BY vendor_city
```


#### count
To count the number of rows in a table, you can use the COUNT() function in SQL. Here's how you can do it:

```sql
SELECT COUNT(*) FROM table_name;
```

#### Four way to code column specifications
- All columns : `*`

- Column name: `column_name`

- Result of calculation: `Arithmetic expression`

- Result of function: `function_name()`. E.g. `CONCAT(first_name, ' ', last_name)`



## WHERE

The `WHERE` clause is used to filter rows from the result set. It's placed after the `FROM` clause and before the `ORDER BY` clause.

### How to use comparison operators

> MySQL databases are not case-sensitive.

> If you compare a null value using operators, the result is always a null value. To test for null values, use the `IS NULL` clause.

#### Example

Vendors with names from A to L

```sql
WHERE vendor_name < 'M'
```

Invoices on or before a specified date

```sql
WHERE invoice_date <= '2018-06-30'
```

### How to use the IN operator

The `IN` operator is used to test whether a value is equal to any value in a list of values. Here's how you can use it:

```sql
WHERE vendor_state NOT IN ('CA', 'NV')
```

```sql
WHERE vendor_id IN (
    SELECT vendor_id
    FROM invoices
    WHERE invoice_date = '2018-06-30'
)
```

- You can use the IN phrase to test whether an expression is equal to a value in a list of expressions. Each of the expressions in the list is automatically converted to the same type of data as the test expression.
- The list of expressions can be coded in any order without affecting the order of the rows in the result set.
- You can use the NOT operator to test for an expression that's not in the list of expressions.
- You can also compare the test expression to the items in a list returned by a subquery. You'll learn more about coding subqueries in chapter 7.

#### How to use the BETWEEN operator

The `BETWEEN` operator is used to test whether a value is within a range of values. Here's how you can use it:

```sql
WHERE invoice_date BETWEEN '2018-06-01' AND '2018-06-30'
WHERE invoice_total BETWEEN 50000 AND 100000
```


- You can use the `NOT` operator to test whether a value is outside a range of values.
- `Lower limit` must be coded as the first expression, and the `upper limit` must be coded as the second expression.
- `Between` phrase for the range of values are inclusive. That is, the lower and upper limits are included in the range.

You can use `BETWEEN` phrase with the upper and lower limits coded as calculated values:

```sql
WHERE payment_total BETWEEN credit_total AND credit_total + 5000
```

#### How to use REGEXP

The `REGEXP` operator is used to test whether a string matches a pattern. Here's how you can use it:

```sql
WHERE vendor_name REGEXP '^A'
```

- ^ - matches the beginning of a string

- $ - matches the end of a string

- . - matches any single character

- [ ] - matches any single character within the brackets

- [char1 - char2] - matches any single character in the range from char1 to char2

> It will degrade performance if you use the `REGEXP` operator.

### ORDER

To sort by more than one column, list the columns in the order that you want them sorted, separated by commas.



# Retrieve data from two or more table

## JOIN

> Use vein-diagram to think.

A *join* lets you combine columns from two or more tables into a single result set based on the *join condition* you specified.

```sql
SELECT invoice_number, vendor_name
FROM vendors INNER JOIN invoices
    ON vendors.vendor_id = invoices.vendor_id
ORDER BY invoice_number
```
- For an `inner join`, only those rows that satisfy the join condition are included in the result set.

- Tables are typically joined on the relationship between the `primary key` in one table and a `foreign key` in the other table.

- If the two columns in a `join condition` have the same name, you must qualify them with the table name so MySQL can distinguish between them. (table name + "." + column name)

#### Notes on Specifying Tables in SQL Queries:

1. **Uniqueness of Column Names:** If a column name is unique across the tables involved in the query, MySQL will automatically determine the correct table from which to pull the column.
   
2. **Ambiguity Errors:** If the same column name exists in multiple tables involved in the query, and you do not specify the table, MySQL will throw an ambiguity error. 

   - Example:
     ```sql
     SELECT vendor_id
     FROM vendors INNER JOIN invoices
         ON vendors.vendor_id = invoices.vendor_id
     ```
     In this query, the column `vendor_id` exists in both `vendors` and `invoices`, causing an ambiguity error.

3. **Best Practices:**
   - Always specify the table (or use a table alias) when working with columns in JOIN operations or any other scenario involving multiple tables. This makes the query clear and prevents potential ambiguity errors.
   - Using table aliases can shorten the queries and make them more readable.

4. **Explicit is Better:** While MySQL can sometimes infer context, it's more maintainable and less error-prone to be explicit about your intentions in your SQL queries. 

### How to use table aliases

A `table alias` is an alternative table name that's typically just a letter or two.

```sql
SELECT invoices_number, vendor_name, invoice_due_date, 
    invoice_total - payment_total - credit_total AS balance_due
FROM vendors v JOIN invoices i
    ON v.vendor_id = i.vendor_id
WHERE invoice_total - payment_total - credit_total > 0
ORDER BY invoice_due_date DESC
```

- You must use alias in place of the original table name throughout the query.

### How to use compound join condition

```sql
SELECT customer_first_name, customer_last_name
FROM customer c JOIN employee e
    ON c.customer_first_name = e.first_name
    AND c.customer_last_name = e.last_name
```

### How to use self join

Certainly! Let's break down the concept of a self-join and the given query step by step.

### What is a Self-Join?
A self-join is a join in which a table is joined with itself. It's useful when the data related to one row is contained within other rows in the same table. This can be useful to compare rows within the same table.

> must use alias for each table

> used to compare rows within the same table

#### The Query in Question:
```sql
SELECT DISTINCT vl.vendor_name, vl.vendor_city, vl.vendor_state
FROM vendors vl JOIN vendors v2
ON vl.vendor_city = v2.vendor_city AND
vl.vendor_state = v2.vendor_state AND
vl.vendor_name <> v2.vendor_name 
ORDER BY vl.vendor_state, vl.vendor_city;
```

#### Sample `vendors` table:
```
| vendor_id | vendor_name | vendor_city | vendor_state |
|-----------|-------------|-------------|--------------|
| 1         | Vendor A    | New York    | NY           |
| 2         | Vendor B    | Los Angeles | CA           |
| 3         | Vendor C    | New York    | NY           |
| 4         | Vendor D    | Boston      | MA           |
| 5         | Vendor E    | New York    | NY           |
```

#### The Logic:
1. The table `vendors` is joined with itself. This means for every row in the table referenced as `vl`, it tries to find a matching row in the table referenced as `v2` based on the conditions specified in the `ON` clause.
2. The condition `vl.vendor_city = v2.vendor_city` ensures that the join is made based on common cities between two vendors.
3. The condition `vl.vendor_state = v2.vendor_state` ensures vendors are from the same state.
4. The condition `vl.vendor_name <> v2.vendor_name` ensures that we don't join the vendor with itself.
5. We select the `vendor_name`, `vendor_city`, and `vendor_state` from the `vl` reference.
6. `DISTINCT` ensures that there are no duplicate rows in the result.
7. The result is ordered by `vendor_state` and then by `vendor_city`.

#### Expected Output:
```
| vendor_name | vendor_city | vendor_state |
|-------------|-------------|--------------|
| Vendor A    | New York    | NY           |
| Vendor C    | New York    | NY           |
| Vendor E    | New York    | NY           |
```

#### Output without `DISTINCT`:
```sql
| vendor_name | vendor_city | vendor_state |
|-------------|-------------|--------------|
| Vendor A    | New York    | NY           |
| Vendor A    | New York    | NY           |
| Vendor C    | New York    | NY           |
| Vendor C    | New York    | NY           |
| Vendor E    | New York    | NY           |
| Vendor E    | New York    | NY           |
```


### How to work with outer joins

An `outer join` returns all rows that satisfy the join conditionm plus unmatached rows from left or right tables.

Besides matched rows, an outer join returns unmatched rows from one or both tables.

- A left outer join returns unmatched rows from the first (left) table.
- A right outer join returns unmatched rows from the second (right) table.


### How to join tables with the USING keyword

```sql
SELECT invoice_number, vendor_name
FROM vendors
    JOIN invoices USING (vendor_id)
ORDER BY invoice_number
```

When you use the equal operator to join two tables on a common column, the join can be referred to as an `equijoin`. 

For joins like this, you can simplify the query with the USING keyword.

- `vendor_id` column exists in both the Vendor and Invoice tables.

### How to use cross joins 

A `cross join` returns the Cartesian product of the two tables involved in the join.

- use explicit syntax

```sql
SELECT select_list
FROM table1 CROSS JOIN table2
```

> A cross join joins each row from the first table with each row from the second table.

### How to work with unions

```sql
SELECT 'Active' AS source, invoice_number, invoice_date, invoice_total 
FROM active_invoices
WHERE invoice_date >= '2018-06-01'
UNION
SELECT 'Paid' AS source, invoice_numher, invoice_date, invoice total 
FROM paid_ invoices
WHERE invoice_date >= '2018-06-01'
ORDER BY invoice_total DESC
```

- same number of columns.

- data types of the corresponding columns must have the same number of columns.

- In an ORDER BY clause, you must use the columns names that are specified in the first SELECT statement. This is because the column names in the first SELECT statement are used to determine the column names in the result set.

- By default, the UNION operator removes duplicate rows from the result set. If you want to include duplicate rows, use the `UNION ALL` operator instead.

- you will typically assign the same name to corresponding columns so the statement is easier to understand.


### **Sequential JOINs in SQL Queries**

When performing multiple JOIN operations in a query, the results are built upon each other sequentially based on the order of the JOINs. Here's a breakdown using the example:

```sql
SELECT *
FROM songs s
LEFT JOIN albums al ON s.album_id = al.alid
LEFT JOIN artists ar ON al.artist = ar.artist_name
LEFT JOIN user_follows_artist ufa ON ar.aid = ufa.aid;
```

1. **First JOIN (`songs` with `albums`):** This pairs each song with its associated album. If a song doesn't have a corresponding album, the columns related to the album will show `NULL` for that song.

2. **Second JOIN (Result of First JOIN with `artists`):** This is based on the intermediate result from the first JOIN. It attempts to pair each album (from the previous result set) with its associated artist. If the intermediate result has a song with `NULL` album details, this song will continue to have `NULL` details for both album and artist after this JOIN.

3. **Third JOIN (Result of First and Second JOINs with `user_follows_artist`):** The result from the previous two JOINs is then paired with the `user_follows_artist` table. This adds information about which users follow each artist. If an artist doesn't have any followers, this column will display `NULL`.

To summarize, each subsequent JOIN operation processes the result of the previous JOINs. If there's a `NULL` from an earlier JOIN, this `NULL` will persist through the subsequent JOINs unless otherwise addressed in the query.

> If you change one of the LEFT JOINs to a standard (INNER) JOIN, the behavior of the query changes.

Let's break down the new query:

```sql
SELECT *
FROM songs s
LEFT JOIN albums al ON s.album_id = al.alid
JOIN artists ar ON al.artist = ar.artist_name
LEFT JOIN user_follows_artist ufa ON ar.aid = ufa.aid;
```

1. **First JOIN (`songs` with `albums`):** As before, this pairs each song with its associated album. If a song doesn't have a corresponding album, the columns related to the album will show `NULL` for that song.

2. **Second JOIN (Result of First JOIN with `artists`):** Here's where the change is. Since it's an INNER JOIN, only those rows with matching entries in both the intermediate result (from the first JOIN) and the `artists` table will remain in the result set. If there's a song from the intermediate result that has `NULL` as album details (because it doesn't have an associated album), then it won't have a matching artist either. Consequently, such a song will be excluded from the final result set. Essentially, any song without an associated album will be dropped at this stage.

3. **Third JOIN (Result of First and Second JOINs with `user_follows_artist`):** This tries to pair each artist from the previous result set with information from the `user_follows_artist` table. If an artist doesn't have any followers, this column will display `NULL`.

To summarize, by using an INNER JOIN with the `artists` table, any song without a matching album (and hence without a matching artist) will be excluded from the result set. Only songs that have both an associated album and artist will appear in the final result.
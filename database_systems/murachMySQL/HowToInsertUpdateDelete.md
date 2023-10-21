# Insert, Update, and Delete Data


## How to create test table

```sql
CREATE TABLE table_name AS select_statement
```

- When you use the CREATE TABLE AS state1nent to create a table, only the column definitions and data are copied. Definitions of primary keys, foreign keys, indexes, and so on are not included in the new table.

## How to insert new rows

- If you don't include a column list, you must provide a value for every column in the table. `(in the same sequence)`

- The time you don't need to include value:
    - Primary Key: `AUTO_INCREMENT`
    - Allow null value
    - Have default value

**MySQL Column Value Insertion Notes:**

- **Null Values**: 
  - If a column allows null values, you can use the `NULL` keyword in the list of values to insert a null value into that column.

- **Default Values**: 
  - For columns defined with a default value, use the `DEFAULT` keyword in the list of values. This will insert the default value for that column.
  
- **Auto Increment Column**: 
  - If a column is set as an auto increment column, using the `DEFAULT` keyword in the list of values will prompt MySQL to generate and insert the appropriate value for the column.

- **Omitting Columns**:
  - When providing a column list for insertion, columns that allow default values or null values can be omitted. In such cases:
    - Default value columns: Their predefined default value is automatically inserted.
    - Null value columns: A null value is assigned.
    - Auto increment columns: MySQL auto-generates the value.
    
**MySQL INSERT Statement Notes:**

1. **Standard INSERT Statement**:
   ```sql
   INSERT [INTO] table_name [(column_list)]
   VALUES (expression_1[, expression_2, ...]),
          (expression_1[, expression_2, ...]) ... ;
   ```
   - This syntax is used for inserting specific values into specified columns. You can insert multiple rows by separating value sets with commas.

2. **Using Subquery for Insertion**:
   ```sql
   INSERT [INTO] table_name [(column_list)]
   select_statement;
   ```
   - With this syntax, you can use the result set from a subquery to insert one or more rows into a target table.

## How to update existing rows

1. **Purpose**:
   - The `UPDATE` statement is used to modify one or more rows in a table.
   
2. **Basic Syntax**:
   ```sql
   UPDATE table_name
   SET column_name_1 = expression_1[, column_name_2 = expression_2, ...]
   [WHERE search_condition];
   ```
   
3. **Column Update**:
   - In the `SET` clause, specify each column's name and its new value. This value can be a literal or an expression.
   - You can assign any valid expression to a column as long as the outcome is compatible with the column's data type.
   - The `NULL` keyword can be used to assign a null value to a column that allows nulls.
   - The `DEFAULT` keyword can assign the default value to a column that's defined with a default value.

4. **Conditional Update**:
   - The `WHERE` clause determines which rows get updated. If omitted and not in safe update mode, all rows are updated.
   - Before executing an `UPDATE`, you might want to run a `SELECT` statement with the same `WHERE` condition to ensure you're updating the correct rows.

5. **Examples**:
   ```sql
   UPDATE invoices
   SET payment_date = '2018-09-21', payment_total = 19351.18
   WHERE invoice_number = '197/5221'; 
   ```

   ```sql
   UPDATE invoices
   SET terms_id = 1
   WHERE vendor_id = 95; 
   ```

   ```sql
   UPDATE invoices
   SET credit_total = credit_total + 100
   WHERE invoice_number = '97/522'; 
   ```

6. **MySQL Workbench - Safe Update Mode**:
   - By default, MySQL Workbench operates in "safe update" mode. This means you can't update rows if the `WHERE` clause doesn't target a primary key or foreign key column.
   - To disable "safe update" mode: Go to Edit → Preferences → SQL Editor → Uncheck "Safe Updates" and then restart MySQL Workbench.
   - Caution: Without the "safe update" mode and if the `WHERE` clause is omitted, all rows in the table will be updated.

**Warning**: Always back up your data before running `UPDATE` statements, especially when disabling safeguards like the "safe update" mode.

## How to delete existing rows

**Basics:**
- The `DELETE` statement is used to delete one or more rows from a table.
- While the `WHERE` clause in the `DELETE` statement is optional, it's crucial to include it to ensure you're only deleting the intended rows. Omitting the `WHERE` clause results in deleting all rows from the table.
- To verify which rows will be affected, it's a good practice to first use a `SELECT` statement with the same conditions. Once confirmed, this can be converted into a `DELETE` statement.

**Examples:**
1. **Delete a single row**:
   ```sql
   DELETE FROM general_ledger_accounts WHERE account_number = 306;
   ```
   (Affects 1 row)

2. **Delete using compound conditions**:
   ```sql
   DELETE FROM invoice_line_items
   WHERE invoice_id = 78 AND invoice_sequence = 2;
   ```
   (Affects 1 row)

3. **Delete multiple rows**:
   ```sql
   DELETE FROM invoice_line_items WHERE invoice_id = 12;
   ```
   (Affects 4 rows)

4. **Using a subquery in DELETE**:
   ```sql
   DELETE FROM invoice_line_items
   WHERE invoice_id IN (SELECT invoice_id FROM invoices WHERE vendor_id = 115);
   ```
   (Affects 4 rows)

**Key Points:**
- To delete a row that has corresponding entries in another table (due to foreign key relationships), the related rows in the child table need to be deleted first. For instance, before deleting a vendor in the `Vendors` table, all related invoices in the `Invoices` table should be deleted first.
  
- Using subqueries can help in identifying rows for deletion based on complex conditions or relationships with other tables.

- MySQL Workbench, by default, runs in "safe update mode". This prevents accidental mass deletion of rows. If a `DELETE` statement doesn't refer to a primary or foreign key column in the `WHERE` clause, it will not execute. However, it's important to note that turning off "safe update mode" and omitting the `WHERE` clause will result in deleting all rows from the table.

**Warning**: Always exercise caution when working with `DELETE` statements. Ensure that backups are in place and that you're certain about the rows you're targeting for deletion.
# How to create databases, tables, and indexes

## How to work with tables

- Field constraints
  - NOT NULL
  - DEFAULT
    - specify a default value for a column
  - AUTO_INCREMENT
    - can only be specified for one column per table. That column must be defined as either primary key or unique key.
    - can start with value other than 1:
        - AUTO_INCREMENT = 3
  - PRIMARY KEY  
  Two primary key:
  ```sql
  CREATE TABLE example_table (
      column1 INT,
      column2 INT,
      PRIMARY KEY (column1, column2)
  );
  ```
  - UNIQUE
  - INDEX
  - FOREIGN KEY

- Table constraint and Column constraint  
They are the same. The only difference is that table constraint is defined at the end of the CREATE TABLE statement.
> Note: If you need to refer to multiple columns, you must use a table-level constraint.

## INFORMATION_SCHEMA

📌 **Note on `information_schema` in MySQL**

- `information_schema` is a **virtual database** in MySQL that provides metadata about the database system itself. It's not a physical database, meaning it doesn't have associated data files or logs.

- It's a **standardized concept** across many relational database management systems (RDBMSs), making it a valuable tool for those working with multiple systems.

- **Key Tables** within `information_schema`:
  - `COLUMNS`: Details about columns in all tables.
  - `TABLES`: Details about all tables and views.
  - `SCHEMATA`: Details about all databases.
  - `STATISTICS`: Details about table indexes.
  - `USER_PRIVILEGES`, `SCHEMA_PRIVILEGES`, `TABLE_PRIVILEGES`, `COLUMN_PRIVILEGES`: Information on user privileges.

- It's a **read-only** database. You can query it to retrieve metadata, but you cannot modify its structure or data. Any modification attempts will result in errors.

Using `information_schema` offers a powerful means to introspect and understand the structure and metadata of databases, especially useful for dynamic SQL or when working with unfamiliar database structures.

## How to work with indexes?

- Updates take more time, SELECT takes less time.

- DBMS can go directly to a row rather than having to search through all the rows until it finds the one you want.
# mySQL

## information_schema

### List all tables from a specific database

```sql
SELECT COUNT(*) 
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'your_database_name';
```

## INSERT

- List the values to be inserted on the VALUES clause.

- If you don't include a column list, you must provide a value for every column in the table.
    - Those value must be listed in the same order as the columns in the table.
- If you do include a column list, you can omit values for columns that have default values.
    - If you omit a column that doesn't have a default value, the database system will raise an error.
    - If columns `allow NULL values`, you can omit values for those columns. The database system will insert NULL values for them.

## Foreign Key Action

[GOOD WEBSITE](https://stackoverflow.com/questions/6720050/foreign-key-constraints-when-to-use-on-update-and-on-delete)

In MySQL, when defining foreign key relationships, you can specify what action should be taken when a referenced row in the parent table is updated or deleted. Here are the available actions:

1. **CASCADE**: This action will propagate the change when the parent changes. For instance, if you delete a row in the parent table, rows in the child table that reference that row will also be deleted.

   **Example**:
   ```sql
   CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       customer_id INT,
       FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
   );
   ```

   If a customer is deleted from the `customers` table, all their orders will also be deleted from the `orders` table.

2. **SET NULL**: This action sets the column value to `NULL` when a parent row is deleted or updated.

   **Example**:
   ```sql
   CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       customer_id INT,
       FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL
   );
   ```

   If a customer is deleted from the `customers` table, the `customer_id` in the `orders` table for those orders will be set to `NULL`.

3. **RESTRICT**: This action causes the attempted `DELETE` or `UPDATE` of a parent row to fail.

   **Example**:
   ```sql
   CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       customer_id INT,
       FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT
   );
   ```

   If you try to delete a customer from the `customers` table who still has orders in the `orders` table, the delete operation will fail.

4. **SET DEFAULT**: This action is recognized by the MySQL parser, but it's rejected by both the InnoDB and NDB storage engines. Therefore, it can't be used in MySQL.

5. **NO ACTION**: In MySQL, this is equivalent to `RESTRICT`. Some other databases might defer the check, but in MySQL, the check is immediate.

   **Example**:
   ```sql
   CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       customer_id INT,
       FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE NO ACTION
   );
   ```

   This will behave the same way as `RESTRICT` in MySQL.

Lastly, it's important to note that cascading foreign key actions do not activate triggers in MySQL.

## How to represent relationships in a database?

The parent entity refers to the entity that posts a copy of its primary key to the child entity. The child entity refers to the entity that receives a copy of the primary key from the parent entity.

### One to Many

Student can accept one school, but school can accept many students.

1. Create school table with school_id as primary key.
2. Create student table with school_id as foreign key.

### Many to Many

Student can accept many courses, and course can accept many students.

1. Create student table with student_id as primary key.
2. Create course table with course_id as primary key.
3. Create student_course table with student_id and course_id as foreign key.

### One to One

#### Mandatory participation on both sides
1. Put another entity's fields into the other entity.


#### Mandatory participation on one side and optional participation on the other side

Put mandatory participation entity's primary key into the optional participation entity as a foreign key.

#### Optional participation on both sides

1. See which entity is more likely be mandatory participation.

2. Copy the primary key of the mandatory participation entity to the child entity as a foreign key.

#### Recursive relationships

A recursive relationship would usually be expressed as a foreign key relationship back to the same table.

```sql
create table folders (
    folder_id int generated always as identity primary key,
    name varchar(255),
    parent_folder_id int,
    constraint fk_folder_parent foreign key (parent_folder_id) references folders(folder_id)
);
```

### Superclass/Subclass relationship types

Superclass - parent entity  
Subclass - child entity

<p align = "center">
    <img src="../images/superSubclass.png" alt="File-based systems" width="500px">
</p>

### Complex relationships

We post a copy of the pri- mary key attribute(s) of the entities that participate in the complex relationship into the new relation, to act as foreign keys. Any foreign keys that represent a `“many” relationship (for example, 1..*, 0..*) generally will also form the primary key` of this new relation, possibly in combination with some of the attributes of the relationship.

### Multi-valued attributes

Create a new relation to represent the multi-valued attribute, and include the primary key of the entity in the new relation to act as a foreign key.

### weak entity

[good website](https://stackoverflow.com/questions/26448216/sql-create-weak-entity-table)


**Note on Referencing Composite Primary Keys in Relational Databases**

**Context**: In a database, there might be scenarios where one entity (like `Seat` in a `Classroom`) cannot be uniquely identified by its attributes alone. Such an entity is termed a "weak entity." For unique identification, it uses a composite primary key, which includes its own attribute and a foreign key referencing another (strong) entity.

**Example**:
- **Strong Entity**: `Classroom` with primary key `classroom_id`.
- **Weak Entity**: `Seat` with a composite primary key consisting of `classroom_id` (foreign key referencing `Classroom`) and its own attribute `seat_number`. Foreign Key on delete cascade.

**Challenge**: If a third table, say `SeatAssignment`, needs to reference a `Seat`, it must acknowledge the composite nature of the `Seat's` primary key.

**Solution**:
1. The third table must have columns to accommodate every part of the composite key.
2. When setting up foreign key constraints in this third table, both columns (`classroom_id` and `seat_number` in this example) must be used to reference the primary key of the `Seat` table.

**Illustrative Schema**:
```sql
CREATE TABLE SeatAssignment (
    classroom_id INT,
    seat_number INT,
    student_id INT,
    assignment_date DATE,
    PRIMARY KEY (classroom_id, seat_number, student_id),
    FOREIGN KEY (classroom_id, seat_number) REFERENCES Seat(classroom_id, seat_number),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);
```

> Using composite foreign keys helps in preserving the relationships between tables when the primary key of the referenced table is made up of multiple columns
```sql
FOREIGN KEY (classroom_id, seat_number) REFERENCES Seat(classroom_id, seat_number)
```


**Key Takeaway**: When designing tables that reference entities with composite primary keys, it's essential to handle both parts of the key correctly, both for data integrity and for maintaining clear relational mappings.

What you're looking at is a Common Table Expression (CTE), introduced using the `WITH` clause in SQL.

## **Common Table Expression (CTE)**

- **Purpose**: A CTE provides a temporary result set that you can reference within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. CTEs are used for simplifying complex joins and subqueries, and also for breaking up queries into more logical and manageable pieces.

- **Syntax**:
  ```sql
  WITH cte_name (column_name1, column_name2, ...)
  AS (
      -- Your query here
  )
  -- Main query referencing the CTE
  ```

- **Example**:

  Given your snippet:

  ```sql
  WITH vendor_table AS 
  (SELECT vendor_id, AVG(invoice_total) AS vendor_avg 
   FROM invoices
   GROUP BY vendor_id) 
  -- After this, you can use "vendor_table" in your main query as if it's a regular table
  ```

  You can now use `vendor_table` in subsequent queries as if it was a real table, for example:

  ```sql
  SELECT v.vendor_name, vt.vendor_avg 
  FROM vendors v 
  JOIN vendor_table vt ON v.vendor_id = vt.vendor_id;
  ```

  This will give you the average invoice total for each vendor.

- **Benefits**:
  1. **Readability and Maintenance**: By using CTEs, you can break down complex queries into simpler parts, which makes your SQL code more readable and easier to maintain.
  2. **Reusable**: The same CTE can be referenced multiple times in the main query.
  3. **Logical Flow**: CTEs enable top-down logic in which you can first define the CTE and then use it, providing a flow that can be easier to follow.

- **Note**: Remember, CTEs are temporary and only last for the duration of the query in which they're defined. They don't store data beyond the execution of that query.

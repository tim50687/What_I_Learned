# Procedures and Functions

## Procedures

### How to code input and output parameters

#### Input parameters

```sql
CREATE PROCEDURE procedure_name (IN parameter_name data_type)
BEGIN
    -- SQL statements
END;
```

- You cannot change the value of an input parameter in the procedure.

#### Output parameters

```sql
CREATE PROCEDURE procedure_name (OUT parameter_name data_type)
BEGIN
    -- SQL statements
END;
```

- Values must be set by the body of the stored procedure.

#### Input/output parameters

```sql
CREATE PROCEDURE procedure_name (INOUT parameter_name data_type)
BEGIN
    -- SQL statements
END;
```

- You can change the value of an input/output parameter in the procedure.

- Not recommended to use input/output parameters. It is confusing.


### Set default value

```sql
IF credit_total_param IS NULL THEN
    SET credit_total_param = 0;
END IF;
```
> It's a good programming practice to code your create procedure statements so they list parameters that require values first.


### Validate parameters 

```sql
IF credit_total_param < 0 THEN
    SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Credit total cannot be negative',
    MYSQL_ERRNO = 1146;
END IF;
```

> The SIGNAL statement is used to raise an error. When you raise an error you must specify a SQLSTATE code. In addition, you can optionally specify an error message or MySQL error number.


### A stored procedure that inserts a row

- In most cases, a stored procedure like this is called from an application program.


### User variable

- A **user variable** is a special type of MySQL variable that's globally available to the current user.

- It is only available as long as the user remains connected to the database.

- Only available to the current user and cannot be seen or used by other users.


## Funcitons

With MySQL, a function can only return a single value.

### How to code a function

```sql
CREATE FUNCTION function_name (parameter_name data_type)
RETURNS data_type
-- characteristic...
BEGIN
    -- SQL statements
END;
```

### Characteristic

- **DETERMINISTIC**: The function always returns the same result when called with the same parameters.

- **NOT DETERMINISTIC**: The function may return different results when called with the same parameters.

- **READS SQL DATA**: The function reads data from the database but does not change it.

- **MODIFIES SQL DATA**: The function changes data in the database.

- **NO SQL**: The function does not include any SQL statements.

- **CONTAINS SQL**: The function includes SQL statements.

> code at leat one characteristic for each function you create.


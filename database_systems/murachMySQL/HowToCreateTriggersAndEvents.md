# Triggers and Events

## Triggers

Triggers can be executed before or after an INSERT, UPDATE, or DELETE statement is executed. They can be used to enforce business rules, to audit changes to data, or to replicate data to other tables.

```sql
CREATE TRIGGER trigger_name
    BEFORE | AFTER INSERT | UPDATE | DELETE
    ON table_name
    FOR EACH ROW
```

- NEW: A keyword that refers to the new row that is being inserted or updated.

- OLD: A keyword that refers to the old row that is being updated or deleted.
    - However, you can only use the OLD keyword in a DELETE or UPDATE trigger. Because there's no old values for inserted rows.

### After Trigger

Store iformation about a statement after it executes.



## Events

Events can be executed at a specific time or at a specific interval. They can be used to automate tasks such as archiving data or generating reports.

### A create event statement that executes only once

```sql
CREATE EVENT event_name
    ON SCHEDULE AT NOW() + INTERVAL 1 DAY
    DO
            -- SQL statements
```

- INTERVAL: one dar in the future from the current date and time.

### A create event statement that executes every month

```sql
CREATE EVENT event_name
    ON SCHEDULE EVERY 1 MONTH
    Starts 'YYYY-MM-DD HH:MM:SS'
    DO
            -- SQL statements
```
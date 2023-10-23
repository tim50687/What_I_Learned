# Trick

## How to get the top crime for each district.

- Get the count for each (district + crime) pair.

- Use `ROW_NUMBER()` or `RANK()` to get the top crime for each district.

## Use ENUM to sort by a specific order.

**Note on ENUM Data Type in MySQL**

- **Definition**: In MySQL, the `ENUM` type allows you to define a static set of string values that a column can hold, like days of the week.
  
- **Sorting Behavior**: When sorting an `ENUM` column, MySQL does not use the lexical (alphabetical) order of the strings. Instead, it uses the order in which the values are defined within the `ENUM`. 

  For instance, with the column defined as:
  ```sql
  ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
  ```
  Sorting in ascending order will list days from Monday to Sunday, not based on their alphabetical order.

- **Use Cases**: This specific sorting behavior is one of the reasons to use `ENUM` – it allows for intuitive ordering based on the sequence of defined values. 

- **Cautions**: While `ENUM` can be useful, it also has its criticisms:
  - **Flexibility**: It's not easy to change or add new values to an `ENUM` type without altering the table structure.
  - **Portability**: The `ENUM` type is not standard SQL, and its behavior may differ across databases or might not be supported at all in some databases.

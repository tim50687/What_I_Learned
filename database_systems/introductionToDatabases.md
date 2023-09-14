# Introduction to databases

## Limitations of file-based systems

<p align = "center">
    <img src="images/limitationOfFileBaseSystem.png" alt="File-based systems" width="500px">
</p>

All of the limitations of the file-based approach can be attrib- uted to two factors:
Alright, let's break this down into simpler terms:

1. **The definition of the data is embedded in the application programs, rather than being stored separately and independently**:
   - In file-based systems, the structure and format of the data (how it's organized and stored) are defined within the application programs themselves.
   - This means that every time you want to access or manipulate the data in a different way, you might need to modify the program or create a new one.
   - Imagine if every time you wanted to view a photo in a different size or format, you had to use a different photo viewer or modify the existing one. It would be very inefficient!

2. **No control over the access and manipulation of data beyond that imposed by the application programs**:
   - In these systems, the only rules or controls over the data are those that are written into the application programs.
   - There's no central system or authority that oversees who can access the data, how it can be changed, or ensures its consistency and security.
   - Think of it like a library without a librarian. If books (data) are borrowed, damaged, or misplaced, there's no one to check or manage the situation unless specific rules are written into every individual library card (application program).

#### Factors:

(1) **The definition of the data is embedded in the application programs, rather than being stored separately and independently**:
   - This directly relates to **Data Dependence**. Since the data definition is within the application, any change in data structure might require changes in the application.
   - It also leads to **Incompatible File Formats**. Different applications can define and store data differently.
   - **Fixed Queries/Proliferation of Application Programs** arise because the queries are tied to how the application defines and accesses the data.

(2) **No control over the access and manipulation of data beyond that imposed by the application programs**:
   - This results in **Separation and Isolation of Data**. Without a central control, each application manages its own data, leading to isolated data silos.
   - It also causes **Duplication of Data**. Since there's no central control to check and manage data across applications, the same data can be stored multiple times.


## Database Approach

## Key terms

- `Query`: A query is a request for data or information from a database, computer system, or other information repository. In the context of databases, a query is typically formulated using a specialized query language, such as SQL (Structured Query Language), to retrieve specific data from a database.

- `Relation`: Amazingly, "relation" in "relational" databases does not refer to the foreign key relationship of one table to another. "A relation is a data structure which consists of a heading and an unordered `set of tuples` which share the same type," according to Wikipedia on ['Relation (database)'](https://en.wikipedia.org/wiki/Relation_(database)).

### What is a database?

A database is a collection of data. It is a repository of information. It is a place where data is stored and organized to serve a particular purpose. It is a collection of related data that represents some aspect of the real world.

### What is a database management system?

A database management system (DBMS) is a software system that manages and controls access to the database.

### What is a database system?

A database system is a combination of a database, a database management system, and the application programs that interact with the database and DBMS.


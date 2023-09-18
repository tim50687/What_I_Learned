# Database Environment

## The three level ANSI-SPARC Architecture

### **Three Levels of Database Architecture:**

1. **External Level (User View)**:
   - Represents how individual users or user groups view the data (user-specific views).
   - Tailored to meet the needs of various user groups.
   - Shields users from the complexities of the overall database system.

2. **Conceptual Level (Logical Level)**:
   - Represents the entire logical view of the entire database as a whole.
   - Includes all entities, attributes, relationships, constraints, and more.
   - Independent of both the external and internal views, acting as a bridge between the two.

3. **Internal Level (Physical Level)**:
   - Deals with the physical storage of data on the storage medium.
   - Concerned with how data is stored, accessed, and updated (e.g., file organization, indexing).
   - Ensures efficient data storage and access mechanisms.

In summary, these three levels provide a separation of concerns, ensuring that users interact with data at a high level, while the database system efficiently manages the underlying physical storage.


### Data Independence

#### Logical Data Independence

1. **Conceptual Schema**: This is a high-level description of the organizational data, often representing the entire database's logical view. It includes all entities, attributes, and relationships without any details about how they are stored physically.

2. **External Schemas (User Views)**: These are different views or perspectives of the database tailored to various user groups or application needs. Each external schema presents only the data relevant to a particular set of users.

3. **Independence Between Schemas**: The main idea is that changes to the conceptual schema (like adding or removing entities or relationships) should not necessitate changes to the external schemas or the need to rewrite application programs. This principle is known as **logical data independence**.

4. **Impact of Changes**: While users directly affected by changes to the conceptual schema need to be aware of them (for instance, if a new attribute is added that they interact with), other users who aren't concerned with those changes should remain unaffected. Their view of the database and their interactions with applications should continue seamlessly.

The benefits of this separation and independence include:

- **Flexibility**: The database can evolve, with entities, attributes, or relationships being added, modified, or removed without disrupting users or applications that don't interact with those specific elements.

- **Reduced Maintenance Effort**: When changes are made to the conceptual schema, there's no need to rewrite or modify all the application programs that interact with the database. Only the affected parts might need adjustments.

- **Stability**: Users have a consistent experience, even as the underlying database structure evolves. They interact with a stable, unchanging view of the data relevant to them.

- **Efficiency**: Developers and database administrators can optimize or restructure the database without worrying about widespread disruptions or the need for extensive application rewrites.

#### Physical Data Independence

1. **Internal Schema**: This is a low-level description of the physical storage of data in the database. It includes details such as file organization, indexing, and access paths.

2. **Independence Between Schemas**: The main idea is that changes to the internal schema (like changing the file organization or indexing) should not necessitate changes to the conceptual or external schemas or the need to rewrite application programs. This principle is known as **physical data independence**.

> From the users' point of view, the only effect that nay be noticed is a change in performance. For example, if a new index is added, the performance of queries that use that index might improve.

## Database Languages
1. **Data Sublanguage**: 
   - This is a specialized language used specifically for interacting with databases. It's called a "sublanguage" because it doesn't have all the features of a full-fledged programming language. Instead, it focuses on tasks related to data definition and manipulation.

2. **Data Definition Language (DDL)**:
   - Part of the data sublanguage used to define and manage the structure of the database. For example, creating tables, defining relationships, setting up indexes, etc.
   - Common DDL commands include `CREATE`, `ALTER`, and `DROP`.

3. **Data Manipulation Language (DML)**:
   - The other part of the data sublanguage, which deals with the actual data within the database. It's used to retrieve, insert, update, and delete data.
   - Common DML commands include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

4. **Limitations of Data Sublanguages**:
   - Data sublanguages are specialized for database tasks, so they don't have general programming constructs like loops or conditional statements. Those are provided by full programming languages.

5. **Embedding in Host Languages**:
   - Many database systems allow you to embed data sublanguage commands within a regular programming language (like Java, C++, or COBOL). This regular programming language is referred to as the "host language."
   - This embedding allows developers to mix database operations with other programming logic seamlessly.
        - **What it means**: Many database systems allow you to write database-specific commands (like SQL queries) directly within a program written in a general-purpose language such as Java, C++, or COBOL. This general-purpose language in which you're writing your main program is called the "host language."
        - **Why it's useful**: By embedding database commands within a host language, developers can integrate database operations directly into their application logic. This makes it easier to develop applications that need to interact with databases, as you don't need to switch between different tools or languages.

6. **Compilation Process**:
   - When a program with embedded database commands is compiled, the database commands are first extracted and replaced with function calls specific to the database system.
   - After this "preprocessing" step, the program is compiled like any other program. When executed, these function calls interact with the database.
        - **Preprocessing**: Before the main compilation process begins, any embedded database commands in the program are identified and extracted. These commands are then replaced with specific function calls that the database system understands. This process is called "preprocessing."
        - **Compilation**: After preprocessing, the program (which now has database function calls instead of direct database commands) is compiled like any regular program in the host language. This produces an executable file.
        - **Execution**: When you run the compiled program, whenever it reaches one of the database function calls, it will interact with the database system to perform the desired operation (like fetching data, updating a record, etc.).

7. **Interactive Commands**:
   - Apart from embedding in host languages, most data sublanguages also allow direct interaction. This means you can run database commands directly from a terminal or command line without embedding them in another program.
        - **What it means**: In addition to embedding database commands in host languages, most database systems also provide a way for developers to directly interact with the database using a command-line interface or a GUI tool.
        - **Why it's useful**: This direct interaction is beneficial for quick tasks like testing a query, checking the structure of a table, or performing ad-hoc database operations. You don't need to write a full program in a host language for these tasks; you can just run the database command directly.
        - **Example**: Consider SQL databases. Using tools like MySQL's command-line client or Microsoft SQL Server's Management Studio, you can directly run SQL commands without embedding them in another program.

### Data Manipulation Languages (DMLs):

DMLs are languages used to retrieve, insert, update, and delete data in a database. The way they operate can be categorized into two main types: procedural and nonprocedural.

1. **Procedural DMLs**:
   - **Definition**: These languages require the user (or programmer) to specify both what data is needed and exactly how to retrieve that data.
   - **How it Works**: In procedural DMLs, data retrieval is often a step-by-step process. A record is fetched, processed, and based on the results, another record might be fetched and processed in a similar manner. This continues until all the desired data has been retrieved.
   - **Characteristics**:
     - Requires the user to handle the data access operations by calling appropriate procedures.
     - Often embedded in high-level programming languages that can handle loops and navigational logic.
     - Examples of systems using procedural DMLs are network and hierarchical databases.
   - **Usage Scenario**: Imagine navigating a hierarchical database where you start with a parent record and then fetch its child records one by one based on certain conditions.

2. **Nonprocedural DMLs**:
   - **Definition**: These languages allow the user to specify what data is needed without detailing how to retrieve it.
   - **How it Works**: The user simply states the desired data, and the DBMS figures out the best way to fetch it. The user doesn't need to know the internal workings of the database or the specific steps to get the data.
   - **Characteristics**:
     - Also known as declarative languages.
     - The DBMS handles the complexities of data retrieval, offering users a degree of data independence.
     - Commonly used in relational DBMSs with languages like SQL or QBE (Query-By-Example).
     - Generally easier to learn and use than procedural DMLs because the DBMS does most of the heavy lifting.
   - **Usage Scenario**: Imagine querying a relational database with a simple SQL statement like `SELECT * FROM users WHERE age > 25;`. You're stating what you want (users over 25), but not detailing how the DBMS should fetch that data.

#### Summary:

- **Procedural DMLs** are like giving turn-by-turn directions to someone: "Go straight, then turn left, then take the second right."
  
- **Nonprocedural DMLs** are like just stating the destination: "Take me to the library." The driver (or in this case, the DBMS) figures out the best route.

In modern database systems, nonprocedural DMLs like SQL are more prevalent due to their ease of use and the efficiency of modern DBMSs in determining the best way to access data. However, understanding both types is crucial for a comprehensive grasp of database systems.
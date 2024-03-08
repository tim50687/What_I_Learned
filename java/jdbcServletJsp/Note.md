# Course Note

## Server side programming steps

- Capturing the user input

- Communicate with the database

- Process the data

- Produve the response page

- Handing the response page to the client

## Servlet life cycle

- init()
    - Called once when the servlet is loaded into the memory

- service()
    - Called for each request

- destroy()
    - Called once when the servlet is unloaded from the memory

These methods are called by the web `container`.

1. Tomcat will load the servlet into the memory and create an instance of the servlet. (Instantiation)

2. Tomcat will call the init() method to initialize the servlet. `init()` method is called only once.

3. Tomcat will then call the `service()` method for each request.(**All the business logic**)`service()` method is called for each request.

4. Tomcat will call the `destroy()` method to remove the servlet from the memory. `destroy()` method is called only once.

## Web APP folder structure
```
WEBAPP
    - WEB-INF 
        - classes // all class files
        - lib // third party jar files
        - web.xml // configuration file
    - META-INF
    - home.html
    - index.jsp
    - welcome.html
    - welcome.jsp
```

## Servlets and Servlet

- Servlets is a technology in the Java EE-standered that allows us to develop dynamic web applications using
    - API - for developing server side code
    - Specification - developer has to follow the rules and regulation

- Servlet is a program that runs on the server and creates a dynamic web page.
    - captures the request from the client
    - can make a call to the database / read from the file system ... etc
    - take the data from the database
    - send the html response to the client

# JDBC concepts

## JDBC Architecture

- JDBC client
    - CRUD operations
        - delete : we return the number of rows deleted
        - update : we return the number of rows updated
        - read : we return the result set
    

- JDBC API

part of java.sql package

- JDBC Driver

implements the JDBC API

It will go to META-INF/services/java.sql.Driver file and find which driver can use the url.

- JDBC driver manager

used to find the driver and establish the connection

between client and driver

1. We use driver manager(only once) to find the driver and establish the connection between the client and the driver.

2. we directly communicate with the driver to perform the CRUD operations.


## How to perform CRUD

1. Establish the connection

2. Create the statement object

3. submit the sql query to DBMS

4. close the statement object

5. close the connection

### Statement

executeQuery() : read

- if no records, close the result set and return null

executeUpdate() : create, update, delete


### Result set 

This is the object that holds the data returned by the database after executing the sql query.

## Try with resources

The reason the objects are automatically closed for you in the provided `JdbcBasic` class is due to the use of the try-with-resources statement, introduced in Java 7. This feature is a try statement that declares one or more resources. A resource is an object that must be closed after the program is finished with it. The try-with-resources statement ensures that each resource is closed at the end of the statement execution. 

The syntax for try-with-resources is:

```java
try (ResourceType resource = new Resource()) {
    // Use the resource
}
```

In your code snippet, the resources are a `Connection`, `Statement`, and `ResultSet` objects:

```java
try (Connection connection = DriverManager.getConnection("jdbc:postgresql://localhost:5432/postgres", "postgres", "787878");
     Statement statement = connection.createStatement();
     ResultSet rs = statement.executeQuery("select * from account")) {
    // Work with the resources
}
```

Each of these implements the `AutoCloseable` or `Closeable` interface, which defines a single method, `close()`, that will be called automatically when the try block is exited, either normally or as a result of an exception being thrown. This automatic closing includes freeing up the database connections and resources associated with `Connection`, `Statement`, and `ResultSet` objects, thus preventing resource leaks such as unclosed database connections.

This feature simplifies the code and reduces the need for boilerplate finally blocks that were previously necessary to ensure resources were closed properly, making your code cleaner and more readable. It also minimizes the risk of resource leaks, which can happen if the resources are not explicitly closed in a finally block, especially in the presence of exceptions.

The passage you've provided discusses a specific configuration step required when working with JDBC (Java Database Connectivity) in a web application deployed on Apache Tomcat, particularly version 8 or earlier. The step involves manually loading the JDBC driver class before establishing a connection to a database. This step is necessary due to a decision by the Tomcat developers to disable the Service Provider mechanism for automatically loading JDBC drivers based on the database URL. Let's break down the key points for clarity:

### Background: JDBC Service Provider Mechanism
- **Service Provider Mechanism**: Starting with Java 6, JDBC 4.0 introduced a feature where JDBC drivers could be automatically loaded without needing explicit class loading code in the application. This works through the service provider mechanism, where JDBC driver jars contain a file (`META-INF/services/java.sql.Driver`) listing the driver classes. The JVM can then automatically discover and load these drivers when a database connection is requested.
- **Automatic Driver Loading**: This means that, in most environments, you can simply include the JDBC driver jar in your classpath, and the driver will be loaded automatically when you connect to a database using `DriverManager.getConnection(url)`.

### Tomcat's Decision to Disable Automatic Loading
- **Memory Leak Issues**: The passage mentions that Apache Tomcat, at least up to version 8, has disabled this automatic driver loading mechanism due to memory leak issues. Memory leaks in web applications can lead to performance degradation over time and could eventually cause the application or server to crash if the memory is exhausted.
- **Manual Driver Loading Required**: Because of this decision, applications deployed on Tomcat need to manually load the JDBC driver class before attempting to establish database connections. This is done using the `Class.forName("com.mysql.jdbc.Driver")` method call.

### Manual Driver Loading
- **`Class.forName(String className)`**: This method is used to dynamically load a class at runtime. Before JDBC 4.0 and the introduction of the service provider mechanism, this was the standard way to load the JDBC driver class to register it with the `DriverManager`. When you call this method with the name of the driver class, it ensures that the class is loaded and initialized, and any static initialization blocks in the class (including its registration with the `DriverManager`) are executed.
- **Example for MySQL**: The passage provides an example for loading the MySQL JDBC driver: `Class.forName("com.mysql.jdbc.Driver")`. This is the fully qualified name of the MySQL driver class. Note that for newer versions of the MySQL driver, the class name has been changed to `com.mysql.cj.jdbc.Driver`.

### Exception Handling
- **Class Not Found Exception**: The `Class.forName` method can throw a `ClassNotFoundException` if the provided class name cannot be found on the classpath. The passage suggests adding a catch block to handle this exception, which is essential for robust error handling in your application.

In summary, when deploying a web application on Tomcat that uses JDBC for database connectivity, you may need to manually load the JDBC driver class using `Class.forName` to avoid `NullPointerException`s or other connection issues, especially in environments where automatic driver loading is disabled due to memory management decisions by the Tomcat team.
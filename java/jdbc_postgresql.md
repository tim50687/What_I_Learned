# JDBC

JDBC stands for Java Database Connectivity. It is a Java `API` for connecting to and executing queries on a database. It is a part of the Java Standard Edition platform, from Oracle Corporation.

We need a `driver` to connect to a database. The driver is a set of classes that implement the `JDBC API`. The driver is specific to the database we are using. For example, if we are using PostgreSQL, we need a `PostgreSQL JDBC driver`.


## Overview

JDBC consists of two packages:

1. `java.sql` package: It contains the JDBC classes and interfaces for connecting to a database, executing queries, etc.

2. `javax.sql` package: The APIs in the javax.sql package are required when working with database serves.
# Apache Maven

## Overview

Apache Maven is a build automation tool used primarily for Java projects. It is used to manage the project's build, reporting, and documentation from a central piece of information. 

Maven is a `build tool` that helps in project management. The tool helps in building and documenting the project.

### Build tool

- Generates `source code` from `source files`.

- Generagtes documentation from `source code`.

- Compiles `source code`.

- Packages compiled `source code` into `JAR`, `WAR`, `ZIP`, etc.

- Install the `packaged code` into the local repository, server, or central repository.

Maven is based on the concept of a `Project Object Model (POM)`. 

### Project Object Model (POM)

POM is an XML file that has all the information regarding project and configuration details.

When we tend to execute a task, Maven searches for the POM in the current directory. 

## The problem that maven solves

- Getting the right version of the right `jar` file.

- Download dependencies.

- Help create the right project structure.

- Building and deploying the project.



## Jar File

A JAR (Java ARchive) file is a package file format typically used to aggregate many Java class files and associated metadata and resources (text, images, etc.) into one file to distribute application software or libraries on the Java platform.

### Why JAR?

- Used to distribute java code/libraries for use by other developers.



## archetypes

Maven Archetype is a template for the project. It is a Maven project templating toolkit. An archetype is defined as an original pattern or model from which all other things of the same kind are made.

- quickstart: A simple project with a single Java class.

- webapp: A web application project.
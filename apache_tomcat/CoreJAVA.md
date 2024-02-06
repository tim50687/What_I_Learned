
# Tomcat and Java: A Quick Look Behind and Look Ahead

When installing Tomcat, it's common to define `JAVA_HOME` (or `JRE_HOME`) as an environment variable that points to the Java JDK (or JRE) installation directory.

Tomcat is implemented in Java and designed specifically to handle Java web applications.

Output from invoking the 'startup' script (`startup.sh` or `startup.bat`) at the command-line:

```sh
% ./startup.sh
Using CATALINA_BASE:   /home/kalin/tomcat8
Using CATALINA_HOME:   /home/kalin/tomcat8
Using CATALINA_TMPDIR: /home/kalin/tomcat8/temp
Using JRE_HOME:        /usr/local/java8
Using CLASSPATH:       /home/kalin/tomcat8/bin/bootstrap.jar:/home/kalin/tomcat8/bin/tomcat-juli.jar
Tomcat started.
```

To confirm that Tomcat is indeed running, you can open a browser to http://localhost:8080 or use the 'curl' utility (https://curl.haxx.se/) from the command-line:

```sh
% curl localhost:8080
```

For now, CATALINA is Tomcat's main component, often referred to as its 'web container.'

It's common to conflate 'Tomcat' (the web server) and 'Catalina' (the main `component` in tomcat).

## Tomcat Runs as a Java 'Application'

Tomcat runs as a Java 'application,' which means as a single process at the system level.

Tomcat implements the '`one-thread-per-request`' model of handling client requests:

```
TCP or HTTP request        request handed off to a thread from a thread pool
          \   +--------+              /
client request ----->| Tomcat |----->client-handling thread
                   +--------+
```
- tomcat takes the request and handed to the thread from the thread pool.

Tomcat is thus multi-threaded, and multi-threading is the standard Java way to manage 'client concurrency.'

Modern Tomcat uses a mix of multi-threading and non-blocking ('asynchronous') I/O to manage concurrent client requests.

## Managing Tomcat with JMX

Tomcat can be managed, even remotely, through JMX (Java Management Extensions), in particular by exposing the web container (Catalina) as an MBean.

## Tomcat v.s. Catalina

Tomcat is a web server, and Catalina is the main component of Tomcat.

A web container and a web server are both components involved in serving web applications, but they serve different roles and have distinct functionalities in the context of web development. Here's a comparison of a web container and a web server:

**Web Container (Servlet Container or JSP Container):**

1. **Role:**
   - A web container is responsible for executing Java Servlets and JavaServer Pages (JSP) within a web application.
   - It manages the lifecycle of servlets and JSP pages, handling their initialization, request processing, and destruction.
   - Web containers are part of the Java Enterprise Edition (Java EE) or Jakarta EE specifications and are used to run Java web applications.

2. **Functionality:**
   - A web container provides a runtime environment for Java-based web components (servlets and JSP pages) to handle HTTP requests and generate HTTP responses.
   - It manages the threading and concurrency for handling client requests, ensuring that each request is processed in a separate thread.

3. **Examples:**
   - Apache Tomcat, Eclipse Jetty, WildFly, and Apache Geronimo are examples of web containers.

4. **Usage:**
   - Typically, web containers are used as part of a larger Java EE application server or can be used as standalone servlet containers for running Java web applications.

**Web Server:**

1. **Role:**
   - A web server's primary role is to serve static web content (HTML, CSS, JavaScript, images, etc.) and to handle HTTP requests and responses.
   - It can also serve as a reverse proxy, load balancer, and SSL/TLS terminator.
   - Web servers are often used to serve dynamic content through the integration of application server components, such as servlet containers or FastCGI handlers.

2. **Functionality:**
   - A web server handles the low-level HTTP protocol, listens for incoming client requests, and returns static web content or forwards dynamic requests to appropriate backend services (e.g., a web container).
   - It is optimized for efficiently serving files and handling high volumes of incoming HTTP requests.

3. **Examples:**
   - Common web servers include Apache HTTP Server (Apache), Nginx, Microsoft Internet Information Services (IIS), and LiteSpeed.

4. **Usage:**
   - Web servers are often used in conjunction with application servers or servlet containers to serve dynamic web content. They can also serve as standalone servers for hosting static websites or proxying requests to various backend services.

In summary, a web container is a component specifically designed for executing Java Servlets and JSP pages within a web application, while a web server is a more general-purpose server that handles HTTP requests, serves static content, and can also interact with application servers or web containers to serve dynamic content. Many web applications involve both a web server and a web container working together to provide a complete web solution.


## WAR Files

A WAR (Web Application Archive) file is a JAR (Java ARchive) file used to package a web application. It contains the web application's classes, JSPs, HTML, JavaScript, and other resources, along with a deployment descriptor (web.xml) that describes the structure and configuration of the web application.

In /tomcat/webapps, you can deploy a `WAR file` by copying it to the webapps directory. Tomcat will automatically expand the WAR file into a corresponding directory structure and deploy the web application.


## WAR Files and URLs in Tomcat Deployment: Request Mapping ('Dispatching')

```
                +-------------------+
request------->| Request Dispatcher |-----> Requested Resource
                +-------------------+
```

### How does Tomcat map client requests to the appropriate 'resource' within a web app?

Tomcat maps client requests to the appropriate resource within a web app using a two-step operation:

1. **Find the Appropriate WAR File:**
   - Tomcat first identifies the appropriate Web Application Archive (WAR) file associated with the requested web application.

2. **Find the Resource Within the WAR File:**
   - After locating the correct WAR file, Tomcat then searches within that WAR file to find the specific resource (e.g., HTML page, Java code) requested by the client.

   - If the requested WAR file or the resource within it doesn't exist, Tomcat returns the familiar "404 Not Found" response to the client.



## Deployment in Tomcat

The standard way to deploy a web application in Tomcat is to copy a WAR file (a JAR file with a .war extension) to the `TOMCAT_HOME/webapps` directory or its subdirectory. The WAR file's name is arbitrary.

Example with a deployed 'preds.war' file:

- Contents of the 'preds.war' file:
  - `ajax.xhtml` (the identifier is 'ajax.jsf', a proxy for 'ajax.xhtml')
  - `WEB-INF/web.xml` (standard 'deployment descriptor' - optional)
  - `WEB-INF/faces-config.xml` (JSF deployment descriptor)
  - `WEB-INF/classes/beans/Controller.class` (backend JavaBean)
  - `WEB-INF/classes/beans/Organization.class` (backend JavaBean)
  - `WEB-INF/classes/beans/Prediction.class` (backend JavaBean)
  - `WEB-INF/lib/javax.faces.jar` (JSF implementation library)

The client's URL includes the WAR file's name as the first name in the URI part of the URL. For example, with 'preds.war' as the name of the deployed WAR file:

```plaintext
http://localhost:8080/preds/ajax.jsf
```

- In this URL:
  - `http` is the scheme.
  - `localhost:8080` is the port number.
  - `/preds` is the WAR file name without the '.war' extension.
  - `/ajax.jsf` is the resource URI (Uniform Resource Identifier), also known as the 'path.'

- The URI `/preds/ajax.jsf` represents what's being requested by the client.

## Servlet

Simply put, a Servlet is a class that `handles requests, processes them and reply back with a response`.

For example, we can use a Servlet to collect input from a user through an HTML form, query records from a database, and `create web pages dynamically`.

Servlets are `under the control of another Java application called a Servlet Container`. When an application running in a web server receives a request, the Server hands the request to the Servlet Container – which in turn passes it to the target Servlet.

## JSP 

JSP (JavaServer Pages) is a technology used to create dynamic web pages. It allows developers to embed Java code within HTML pages, which is then executed on the server to generate dynamic content.

- Basically you can use java code in HTML.

- It is a type of servlet that is executed on the server to generate dynamic content.

## JSF 

JSF (JavaServer Faces) is a Java-based web application framework that simplifies the development of user interfaces for Java web applications. It provides a component-based architecture and a set of standard UI components that can be used to build web applications.


[jsf, jsp, servlets](https://www.baeldung.com/jsf-servlet-jsp)

[MVC example with servlets and JSP](https://www.baeldung.com/mvc-servlet-jsp)


## Basic Example

Certainly! The interaction between Tomcat, the thread pool, and the request dispatcher can be a bit complex, but I'll explain each component and how they work together when handling client requests in a Java web application.

1. **Tomcat**:
   - Tomcat is a Java-based web server and servlet container. Its primary role is to accept incoming client requests (usually over HTTP or HTTPS), manage the lifecycle of Java Servlets and JavaServer Pages (JSP), and send responses back to clients.
   - Tomcat operates as a server, listening for incoming requests on a specific port (e.g., 8080).

2. **Thread Pool**:
   - Tomcat typically uses a thread pool to manage incoming client requests efficiently. This thread pool consists of a collection of threads that are available to process requests.
   - When a client request arrives, Tomcat takes a thread from the pool to handle that specific request. This allows Tomcat to process multiple requests concurrently without creating a new thread for each request, which can be resource-intensive.

3. **Request Dispatcher**:
   - A request dispatcher in the context of a Java web application (e.g., servlet or JSP) is a mechanism to forward or include a request from one component to another.
   - When a client sends a request to Tomcat, Tomcat decides which servlet or JSP should handle the request based on URL mappings defined in the web application's deployment descriptor (e.g., `web.xml`).
   - The request dispatcher can forward the request to the appropriate servlet or JSP for further processing.
   - Alternatively, the request dispatcher can include the output of another servlet or JSP within the current response.

Here's how it all works together when a client sends a request:

1. A client sends an HTTP request to Tomcat (e.g., `http://localhost:8080/myapp/servlet`).
2. Tomcat listens for incoming requests on port 8080 and receives the client request.
3. Tomcat checks the URL mappings to determine which servlet or JSP should handle the request (e.g., `/myapp/servlet` is mapped to a specific servlet in `web.xml`).
> Step 3, which involves checking the URL mappings to determine which servlet or JSP should handle the request, is typically done by the main Tomcat server thread, not one of the threads from the thread pool.

4. Tomcat takes a thread from the thread pool to process the request.
5. The selected servlet or JSP is invoked to handle the request's logic.
6. If needed, the servlet or JSP may use a request dispatcher to forward or include the request to another servlet or JSP for further processing.
7. The servlet or JSP generates a response, which is sent back to the client.

The use of a thread pool allows Tomcat to efficiently manage concurrent requests, ensuring that multiple clients can be served simultaneously. The request dispatcher enables component-based development and the composition of responses from multiple servlets or JSPs, promoting code reuse and modularity in web applications.
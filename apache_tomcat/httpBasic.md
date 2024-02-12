## HTTP (HyperText Transfer Protocol) Basics

HTTP is a messaging protocol commonly used for communication between web clients (such as browsers) and servers. It operates atop the TCP (Transmission Control Protocol) and facilitates the exchange of hypertext, typically in the form of HTML documents, although it can be used for other types of data as well.

### Key Concepts

- **Two Basic Message Types**: HTTP defines two basic types of messages: requests and responses.

- **`Request Methods`**: Requests can have various methods, including POST (Create), GET (Read), PUT (Update), and DELETE (Delete), often referred to as CRUD operations.

- **URI and HTTP Method**: A request requires a Uniform Resource Identifier (URI), which `specifies the resource being accessed`, and an HTTP method (verb) that indicates the desired action to be performed on the resource.

### Request-Response Interaction

- **Request Message**: Sent from the client to the server, typically consisting of a start line (including the HTTP method and URI), headers (key/value pairs), and an optional body (for methods like POST and PUT).

- **Response Message**: Sent from the server to the client, consisting of a start line (including the HTTP version and status code), headers, and an optional body.

### Statelessness and State Management

- HTTP is often described as stateless, meaning that each request-response cycle is independent of previous ones. However, mechanisms like cookies and headers allow for state management across requests.

- Web applications typically maintain state internally to support multi-message conversations. Tomcat provides mechanisms like the `session map (through Catalina)` to help manage state for web applications.

### Format of Requests and Responses

#### HTTP Request Format:

```
[start line]
[headers]
[newline]
[newline]
[body]
```

```
> GET /mkalin/index.html HTTP/1.1
> User-Agent: curl libcurl OpenSSL zlib libidn librtmp
> Host: condor.depaul.edu
> Accept: */*
> 
```

#### HTTP Response Format:

```
[start line]
[headers]
[newline]
[newline]
[body]
```

### Example Interaction

- **Client Request**: A client sends an HTTP request to the server, specifying the desired method (e.g., GET) and URI (e.g., `/greet/hello.html`).

- **Server Response**: The server processes the request and sends back an HTTP response, typically including the requested resource (e.g., an HTML page).

HTTP provides the foundation for communication in web applications, enabling the exchange of data between clients and servers in a standardized manner. Understanding its basics is crucial for developing and interacting with web-based systems.

- 
- Interactions among HTTP, the web container, and app-specific code

## Given an incoming HTTP request to Tomcat/Catalina


             Catalina in the case of Tomcat
                          /                 +-----> static content (e.g., 'productList.html')? 
      HTTP request  +---------------+       |
     -------------->| web container |-------+-----> app-specific servlet (e.g., 'myProdListServlet')?
                    +---------------+       |
                                            +-----> framework servlet (e.g., the JSF servlet)? 

    ## For app-specific servlets, recall that JSP scripts are translated into servlet instances (in Tomcat,
       Jasper is the 'JSP engine' that does the translating).
Static content - no code processing needed

### Here's how each of these cases is handled:

- Requests for static content

        http://...:8080/acmeProducts/productList.html   ## a static HTML page

      are dispatched to the DefaultServer, which comes with the web container Catalina.

              productList.html  +--------------------+
      request------------------>| request dispatcher |----->DefaultServlet ## loaded when Tomcat starts up
                                +--------------------+

             body of the HTTP response
                     /
                 productList.html
      requester<------------------DefaultServlet

### For dynamic content--the request-handling code in a web app--Catalina 

- parses the request (make sure its well-formed)

- generates a map (key/value pairs) of the request contents (put the request in the `java map`)

- passes the map to the request-handling code(some servlet or others)

- passes a channel reference to the request-handling code so that this code can generate a response    

                                                 HttpServletRequest instance
                                                            /
              productList.jsp   +--------------------+  request map
      request------------------>| request dispatcher |-------------->productListServlet ## compiled JSP script
                                +--------------------+


            body of the HTTP response
                     /
                 productList.html
      requester<------------------productListServlet
                     \
               HttpServletResponse instance

### For various web frameworks (e.g., JSF = JavaServerFaces), the approach is quite similar:

#### There's an 'interceptor' servlet that represents the framework.

#### The interceptor then manages the application-specific code.

Depicition:

                                                 HttpServletRequest instance
                                                            /
              productList.jsf   +--------------------+  request map              
      request------------------>| request dispatcher |-------------->JSF servlet------>app-specific code
                                +--------------------+                  \
                                                                 'interceptor' servlet


### An HTTP(S) request has the start-line/headers/[body] structure examined earlier:

- always a start-line and at least one header element

- body is optional (e.g., PUT and POST have a body, GET and DELETE do not)

### The javax.servlet.http.HttpServlet class encapsulates 'do' methods that are Java counterparts of the underlying HTTP methods ('verbs'): doGet, doPost, doPut, doDelete, etc.

### In general, the servlet API enables and simplifies program interaction with the underlying HTTP request and HTTP response.

### The web container (Catalina in Tomcat) parses the request, and creates a Java map from the key/value pairs that make up the HTTP headers and (optional) body. Info from the HTTP start-line (e.g., the HTTP verb such as GET or POST) also goes into this map. 

### Various 'get' methods are available to extract information from the HTTP start-line, the headers, and the body.

### The API is flexible: an HTTP request can have arbitrarily many header and body elements so the API has, for example, a getParameter(paramName) method.



---

## JSP translation 

This statement means that JSP (JavaServer Pages) scripts, which are essentially HTML pages with embedded Java code, are not directly executed by the web container. Instead, they are translated into Java servlets by a special component called the JSP engine, which is part of the web container (such as Catalina in Tomcat).

When a JSP script is requested by a client, the JSP engine first translates the JSP code into a Java servlet class. This translation process involves converting the HTML markup and embedded Java code in the JSP file into Java code that generates dynamic content. 

Once the translation is complete, the resulting servlet class is compiled into bytecode by the Java compiler. This compiled servlet class is then loaded and executed by the web container to generate the dynamic content that is sent back to the client as an HTTP response.

In summary, the process of translating JSP scripts into servlet instances allows web developers to write dynamic web pages using a combination of HTML and Java code, which are then executed by the web container to produce the desired output for the client.

> While JSP files are typically translated into servlet classes by the JSP engine during development, in a production environment, they are pre-compiled and loaded into memory by the server during startup,

## HTTP is a map 

HTTP can be thought of as essentially a map because it relies heavily on key-value pairs to convey information between clients and servers. Here's why:

1. **Headers**: HTTP requests and responses consist of headers, which are key-value pairs that contain metadata about the message. For example, headers may include information such as the content type, content length, cookies, caching directives, and more. Each header consists of a key (header name) and a corresponding value.

2. **Parameters**: HTTP requests can include parameters, particularly in methods like GET and POST. These parameters are also key-value pairs, where the key represents the parameter name and the value represents the parameter value. Parameters are commonly used to pass data from clients to servers, such as form submissions or query strings in URLs.

3. **Request and Response Bodies**: Although not always present, HTTP messages can also include bodies that contain additional data. For example, in POST requests, the body may contain form data or payloads sent from the client to the server. Similarly, in HTTP responses, the body may contain the content being returned to the client, such as HTML, JSON, or binary data. The body content can be considered as the value in the key-value pair, with the key being implicit (e.g., the body itself).

4. **State Management**: While HTTP itself is stateless, web applications often use mechanisms like cookies or session identifiers to manage state between requests. Cookies, for instance, are key-value pairs stored by the client and sent along with subsequent requests to the same server. They enable the server to maintain some form of state information across multiple requests from the same client.

Overall, the use of key-value pairs in various aspects of HTTP messaging allows for a flexible and extensible communication protocol that can convey a wide range of information between clients and servers. This characteristic makes HTTP akin to a map, where data is organized and accessed based on specific keys.
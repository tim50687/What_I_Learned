# Web Development Fundamental

## How the Web works?

A URL (Uniform Resource Location) is a way to locate resources in the Internet. Resources can be:

* Web pages (HTML documents)
* Images
* Video files
* Fonts
* ...

**Client-Server model**

The web works on a `client-server model`. The client is the browser, and the server is the computer or computers that host our target website. The client requests a service, and the server provides that service.

The message that the client requests is formatted based on a protocol called HTTP. HTTP is a language that clients and servers use to talk to each other. We also have HTTPS, which is HTTP with encryption.

When broswer recieve HTTP response, this HTTP response contains an HTML document, the browser reads that HTML document to construct a document object model and render the page.

**Front end developer**
- HTML  
The building block of our webpages.
- CSS  
Styling webpages and makeing them beautiful.
- JavaScript  
Adding functionality to webpages

**HTML basic**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>My first web page</title>
    <style>
      img {
        width: 200px;
        border-radius: 100px;
        float: left;
        margin-right: 10px;
      }
      .username {
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <img src="./images/boston.jpg" alt="An image of Boston" />
    <p class="username">@Boston</p>
    <p>I love to code!</p>
  </body>
</html>
```

`<!DOCTYPE html>` - Tell browser this is an html5 document  
html element:  
`<html></html>` - Opening tag and Closing tag  
`<head></head>` - head element. Give browser information about this page  
For example:  
    this

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

The message that the client requests is formatted based on a protocol called HTTP. `HTTP is a language that clients and servers use to talk to each other`. We also have HTTPS, which is HTTP with encryption.

When broswer recieve HTTP response, this HTTP response contains an HTML document, the browser reads that HTML document to construct a [document object model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) and render the page (${\color{cyan}\text{After fetching all the resources}}$).

> JavaScript primarily interacts with the Document Object Model (DOM) when it comes to web development.

**Front end developer**
- HTML  
The building block of our webpages.
- CSS  
Styling webpages and makeing them beautiful.
- JavaScript  
Adding functionality to webpages

## URL Basic

URL, which stands for **Uniform Resource Locator**, is a fundamental concept of the Web. It serves as the mechanism browsers use to retrieve resources on the internet. A URL essentially acts as the address of a unique resource online. While each valid URL theoretically points to a distinct resource, there are exceptions, such as URLs pointing to nonexistent or relocated resources. `The management of these resources and URLs falls under the responsibility of the web server owner.`

**Examples of URLs:**
- [https://developer.mozilla.org](https://developer.mozilla.org)
- [https://developer.mozilla.org/en-US/docs/Learn/](https://developer.mozilla.org/en-US/docs/Learn/)
- [https://developer.mozilla.org/en-US/search?q=URL](https://developer.mozilla.org/en-US/search?q=URL)

You can type any of these URLs into your browser's address bar to load the associated web page or resource.

**Parts of a URL:**

A URL consists of various components, some mandatory and others optional. The most crucial parts are highlighted below:

- **Scheme:** Represents the chosen communication protocol, such as "https://" for secure browsing.
- **Domain Name:** Acts as the location (city or town) where the resource resides, like "developer.mozilla.org."
- **Port:** Similar to a zip code, specifying the destination for the resource.
- **Path:** Describes the building or directory where the resource is located.
- **Parameters:** Provide additional information, akin to specifying an apartment number.
- **Anchor:** Represents the specific section or target within the resource.

You can think of a URL like a postal mail address, where the scheme is the postal service, the domain name is the city or town, the port is the zip code, the path is the building, parameters are extra details like an apartment number, and the anchor is the intended recipient.


## **HTML basic**

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

- `<!DOCTYPE html>` - Tell browser this is an html5 document  
html element:  
- `<html></html>` - Opening tag and Closing tag  
- `<head></head>` - head element. Give browser information about this page  
For example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<title></title>` - title element. Specify title of this page  

- `<body></body>` - body element. Elements that will appear on our page  
For example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<img src="" alt="">` - image element. 1. We don't have closing tab because image element cannot have child element. 2. Don't need to add forward slash in html5. Two attributes (supply addition information about an element): `src` - specify the path of image. `alt` - give the browser some text to display in case the image cannot be display. Attributes are coded as part of the opening tag.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<p></p>` - text element.  
`<style></style>` - style element. Place we write CSS code. Type img {} to reference the image element. `border-radius` - half of the width will get round image. `margin-right` - add some space next to the image. 

##### How to seperate two paragraph elements?  
Give an attribute called `class`(classification) - Put this element inside different class or a different category. We can use `p.username` or even `.username` to apply to all elements that hace the username class.

**CSS syntax**  
```css
h1 {color:blue; font-size:12px;}
```
`h1` - selector. The selector points to the HTML element you want to style.  
`{color:blue; font-size:12px;}` - declaration block. The declaration block contains one or more declarations separated by semicolons. Each declaration includes a CSS property name and a value, seperated by a colon.


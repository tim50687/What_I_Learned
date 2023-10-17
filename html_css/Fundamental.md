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

When broswer recieve HTTP response, this HTTP response contains an HTML document, the browser reads that HTML document to construct a `document object model` and render the page (<span style="color: cyan">After fetching all the resources</span>).

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


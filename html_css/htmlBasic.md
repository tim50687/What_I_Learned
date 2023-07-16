# HTML Basic

> Ｔips: `! + tab `- Get a basic HTML boilerplate
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="keywords" content="HYML, CSS" />
    <meta name="description" content="..." />
    <title>Document</title>
    <style>
      em {
        color: red;
        font-style: normal;
      }
    </style>
  </head>
  <body>
    <h1>Heading 1</h1>
    <h2>HTML</h2>
    <p>HTML tutorial</p>
    <h3>Code</h3>
    <h3>Exercise</h3>
    <h2>CSS</h2>
    <p>CSS tutorial</p>

    <p>I love to teach you <em>HTML!</em></p>
    <p>I love to teach you &lt;HTML!&gt; &copy;</p>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Rerum quibusdam
      iusto facilis nulla nam dolore repudiandae iste. Itaque, doloribus natus
      quos earum magnam quidem adipisci molestias dicta at non tempore odit
      quaerat consectetur, eaque vel &nbsp;nesciunt aliquam minima ab placeat
      velit praesentium sunt quam sequi? Error sit mollitia sunt eveniet?
    </p>
  </body>
</html>
```
In head element, we have couple of `meta elements`, giving information about this webpage.  

`<meta name="description" content="">` - description of this page. It will appear on search engine when someone searches for our website.

`<em></em>` - emphasize element. To emphasize content in our HTML. This helps search engines extract important content in our document. By default, browser display emphasize content in italic. But again the purpose of this element is to emphasize element. If you want to style the content, use CSS. `Don't use it just because you want to implement italic.` 
> HTML is not meant for styling, it should only be used for structuring content.

In HTML, we have six heading elements.  
`<h1></h1>` - most important heading. *Don't choose heading based on the size*, size can always be changed with CSS. We should use these headings only for creating hierarchy. We should only have one single h1 element to avoid confusing search engine.

## Entities
Some characters are reserved in HTML, to display them we have to use special notation. Here's the common three entities:  
- `&lt;` - &lt; (less than).
- `&gt;` - &gt; (greater than).
- `&copy;` - &copy; (copy right symbol).
- `&nbsp;` - &nbsp; (non breaking space).
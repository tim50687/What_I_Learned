# HTML Basic

> Tips: `! + tab `- Get a basic HTML boilerplate
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
      img {
        width: 200px;
        height: 200px;
        object-fit: cover;
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
    <img src="images/coffee.jpg" alt="A coffee mug on a table">
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

## Hyperlinks

```html
    <a href="company/about.html"> About me </a>
    <a href="images/boston.jpg" download>Boston pics</a>
    <a href="#section-css">CSS</a>
    <h2 id="section-css">CSS</h2>
    <a href="#">Jump to top</a>
    <a href="https://google.com" target="_blank">GOOGLE</a>
    <a href="mailto:tim506877@gmail.com">Email me</a>
    <h2 id="section-css">CSS</h2>
```
- `a` - anchor element. Links to other pages or website.  

- `href attribute` - hypertext reference. We can use relative or absolute URL **(Also image)** . 
    - `download` - download attribute. Prmopt the user to download it.

- `id` - id atribute. Unique identifier. Can use pound sign to jump to the second heading. 

- `#` - empty fragment. Jump to top.

> Use absolute URL to link to an external website (Start with the protocol `https://`)

### How to open a new tab

- `target` - target attribute. Set it to `_blank`

### How to link to email

`mailto: <your email>`

### Difference between link and hyperlink

A link is just an address, the url, the location of the target page.

A hyperlink is the element that user can click on to navigate to that target page. Hyperlinks are hidden under the graphics, music, text, image, and video and are only visible when the mouse hovers over them.

## img

- `alt` - alt attribute. 
    - 1. Make our page accessible to visually impaired people. They use screen reader to read the web out to them. That means we should write a good meaningful description here.
    - 2. Help search engines read this text and understand what we're providing here.
    - 3. If the image cannot be loaded, the alternative text is shown.

### Sizing image

We have a property in CSS called `object fit`. Most of the time we use `cover`, so the images covers its containing box.

#### Containing box?

Conceptually, there is a box around every element in an HTML document. The browser use that box to figure out how the page should be displayed.

```html
<style>
      img {
        width: 200px;
        height: 200px;
        object-fit: cover;
      }
    </style>
```

Here we have a box with this dimension 200 by 200. And in this box, we're trying to insert this image. 

## Video and Audio

```html
<style>
video {
        width: 400px;
      }
</style>

<!-- Video -->
    <video src="videos/ocean.mp4" controls autoplay loop >
      Your browser does not support videos.
    </video>
    <audio src=""></audio>
```

- `video` - video element. By default, we see the image of the video. We don't have to specify the `height` because the browser will automatically calculate the height based on the aspect ratio of the video.
    - `controls` - control attribute. We call it `boolean attribute`. `controls = "true"` or `controls = "false"` doesn't matter. The present of the boolean attribute represents the true value and its absence represents the false value.
    - `autoplay` - autoplay attribute. The video automatically start when our page is loaded.
    - `loop` - loop attribute. The video will automatically loop.

In case the browser does not support video. We can provide the fallback text "Your browser does not support videos".

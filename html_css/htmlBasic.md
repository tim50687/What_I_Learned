# HTML Basic

## Viewport

The term "viewport" in web development refers to the visible area of a web page within the user's web browser. It represents the portion of the web page that is currently visible to the user without scrolling. The viewport's size can vary depending on the device and the user's settings, and it plays a crucial role in responsive web design and user interface layout.

Here are some key points related to the viewport:

1. **Initial Viewport**:
   - When a user opens a web page, the initial viewport is the portion of the page that is visible without the need for scrolling. It's the first impression of the web page that a user sees.

2. **Viewport Dimensions**:
   - The dimensions of the viewport are measured in pixels, and they represent the width and height of the visible area in the user's browser window.

3. **Responsive Design**:
   - Viewport size can vary widely between different devices, such as desktop computers, laptops, tablets, and smartphones. To create a user-friendly experience on all devices, web designers often use responsive design techniques to adapt the layout and content of a web page to fit within the available viewport.

4. **Viewport Meta Tag**:
   - Web developers can control how a web page is initially displayed on mobile devices using the `<meta>` viewport tag in the HTML `<head>` section. This tag allows developers to set the initial viewport width, scale, and other properties.

   Example of a viewport meta tag:
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```

   - In the above example, `width=device-width` instructs the browser to set the initial viewport width to the device's screen width, and `initial-scale=1.0` sets the initial zoom level to 100%.

5. **Viewport Units**:
   - CSS provides viewport units (`vw`, `vh`, `vmin`, and `vmax`) that allow designers to specify sizes and positions relative to the viewport dimensions. This is especially useful for creating responsive designs that adapt to different viewport sizes.

6. **Scrolling**:
   - When the content of a web page extends beyond the dimensions of the viewport, users can scroll to view the hidden content. Vertical and horizontal scrollbars may appear, depending on the overflow behavior set for the content.

In summary, the viewport is the visible area of a web page within a user's browser, and it plays a vital role in responsive web design. Web designers and developers use various techniques and tools to ensure that web pages are displayed optimally within the available viewport, providing a consistent and user-friendly experience across different devices and screen sizes.

## The Head section 
> Tips: `! + tab `- Get a basic HTML boilerplate

In head element, we have couple of `meta elements`, giving information about this webpage.  

`<meta name="description" content="">` - description of this page. It will appear on search engine when someone searches for our website.

`<p>I love to teach you <em> HTML </em></p>` - emphasize element. To emphasize content in our HTML. This helps search engines extract important content in our document. By default, browser display emphasize content in italic. But again the purpose of this element is to emphasize element. If you want to style the content, use CSS. `Don't use it just because you want to implement italic.` 
> HTML is not meant for styling, it should only be used for structuring content.
### Heading 
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

## Images

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
    - `controls` - control attribute. Add the control buttons. We call it `boolean attribute`. `controls = "true"` or `controls = "false"` doesn't matter. The present of the boolean attribute represents the true value and its absence represents the false value.
    - `autoplay` - autoplay attribute. The video automatically start when our page is loaded.
    - `loop` - loop attribute. The video will automatically loop.

In case the browser does not support video. We can provide the fallback text "Your browser does not support videos".


## List

- `ul` - unordered list. Show a list of item where the order does not matter. Nivigation menus on the website are often represented by unordered list.
  - `li` - list item. 

> `nest list`: We can display unordered list under the list item of the unordered list.

- `ol` - ordered list. 

> Short cut: `ol>li*3` + tab

- `dl` - description list. Implement glossaries or display metadata.
  - `dt` - description term. 
    - `dd` - description detail element. To describe this term.

## Table
The table element should only be used for displaying tabular data.

```html
<style>
table, td , th{
        border: 1px solid grey;
        border-collapse: collapse;
        padding: 5px;
      }
      tfoot {
        text-align: left;
      }
</style>
<!-- table -->
    <table>
      <thead>
        <tr>
          <th colspan = "2">Expenses</th>
        </tr>
        <tr>
          <th>Category</th>
          <th>Amount</th>
        </tr>
        
      </thead>
      <tbody> 
        <tr>
          <td>Marketing</td>
          <td>$100</td>
        </tr>
        <tr>
          <td>Accounting</td>
          <td>$200</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th>Total</th>
          <th>$300</th>
        </tr>
      </tfoot>
    </table>
```

- `tr` - table row. To define a row. 
  - `th` - header cell. 
    - `colspan="2"` - colspan attribute. Determine how many columns this cell should expand to. (Default is 1)
  - `td` - data cell. 

> We want to tell search engine that in this table we have two sections, a header and a body.

To do that we use: `<thead></thead>, <tbody><tbody>, <tfoot></tfoot>`

### CSS

- `border` - 3 values.
  - 1. Thickness
  - 2. Style of the border
  - 3. Color

> Here you can put two element together to apply style to both elements.

- `border-collapse: collapse` - collapse the borders in neighboring cells.

- `padding` - add padding around the data in cell.

- `text-align: left;` - Make text in that element aligned to the left. 



## Container

[What is a container?](https://www.geeksforgeeks.org/container-and-empty-tags-in-html/)


```html
<style>
.product {
  background-color: gold;
  width: 300px;
  }

.highlight {
  background-color: yellow;
}
</style>

<!-- Container -->
    <div class="product">
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis debitis ipsam tempore facere atque praesentium sunt recusandae aperiam beatae deserunt.</p>
      <a href="#">Link</a>
    </div>
    <div class="product">
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis debitis ipsam tempore facere atque praesentium sunt recusandae aperiam beatae deserunt.</p>
      <a href="#">Link</a>
    </div>
    
    <p><span class="highlight">Lorem</span> ipsum dolor sit, amet consectetur adipisicing elit. Modi, rerum.</p>
```

Most common comtainer element:

- `div` - division element. This container will `fill up the width of the page` because it's a `Block-Level Element` - always start on a new line and fillup the entire available space. But we can use CSS to change its width.

-  `span` - span element. In a paragraph we can wrap the text with `span`. It's an `Inline Element`, which mean it's not gonna take up entire width.

  - The <span> HTML element is a generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the class or id attributes), or because they share attribute values, such as lang.

### Semantic elements

Container elements that are more descriptive or meaningful. It helps search engine better understand our pages and what they contain. 

```html
<article class="article">
      <h1>Heading</h1>
      <p>Published <time datetime="2022-08-27 17:00">August 27 2021 05:00pm </time> </p>
      <p><mark>Lorem</mark> ipsum dolor sit amet consectetur adipisicing elit. Optio expedita rem ipsa mollitia impedit quos dicta reprehenderit nam cumque molestiae?</p>
      <figure>
        <img src="images/coffee.jpg" alt="">
        <figcaption>
          My coffee this morning
        </figcaption>
      </figure>
    </article>
```

- `article` - article element. This article doesn't has to be a blog post or a newspaper article. 
  - `It can be any independent, self-contained content.` 
    - Forum Post
    - Comments
    - Reviews
    - Product cards

- `figure` - figure element. We can make img element more meaningful by wrapping it and tell search engine this is a figure.
  - `figcaption` - figure caption. This caption can be above or below the figure.

- `mark` - mark element. If you want to highlight the content.

- `time` - time element. Wrap the time to make it more semantic.
  - `datetime` - date time attribute. This can help search engine better extract the necessary information from this page. Format = `datetime="2022-08-27 17:00"`

> Imagine if instead of these semantic elements, all we had was divs and spans, the HTML markup wouldn't be very descriptive.

## Element we use to structuring webpages

Most webpages have at least three building blocks

- `header` - Represent introductory content, which can belong to the page or a section or an article.
  - `nav` - navigation bar. With a list of menu items `ul`. We can have multiple navigation on the same page.

- `main` - Main content of the page. **`Every page can have only one main element`** Sometimes we may have multiple sections.
  - `section` - group related content. **Every section should have a heading, which is quite often an h2**. We can use article element to represent each product(any independent, self contained piece of content).

```html
<section>
        <h2>Products</h2>
        <article></article>
        <article></article>
        <article></article>
</section>
```

- `aside` - sometimes we can have a side bar for advertising, or other content that is not directly to the main content.


- `footer`
  - `nav` - navigation bar. With a list of menu items `ul`.


> There are several ways to structure pages. Like we can have multiple sections inside an article.

> Also the header and footer don't just represent the header and the footer of the page, we will use them inside the section or an article.

> The semantic elements in HTML5 are: `<header>, <footer>, <nav>, <main>,  <aside>, <article>, <section>, <figure>, <time> and <mark>`.

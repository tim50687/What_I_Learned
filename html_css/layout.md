# Layout

## Box Model

Whenever browser renders an element, it places it inside a invisible box. This box is called the **CSS Box Model**. It consists of:

<p align = "center">
    <img src="images/box model.png" alt="File-based systems" width="500px">
</p>

- **Content**: The content of the box, where text and images appear

- **Padding**: Clears an area around the content. The padding is transparent

- **Border**: A border that goes around the padding and content

- **Margin**: Clears an area outside the border. The margin is transparent


### Margin Collapsing

When two elements are stacked on top of each other, the margin of the element with the largest margin will be used, and the margin of the element with the smallest margin will be ignored. This is called **margin collapsing**.

Their margin get collapsed into a single margin. The margin of the element with the largest margin will be used, and the margin of the element with the smallest margin will be ignored.

> We should use the margin property to separate the elements.

> We should use the padding property to add space betweem the border and the content area.

## Sizing Element

### Width and Height

By default, the width and height property are applied to the content box. So any padding and border will be added to the width and height.

### Margin

The margin property does not impact the size of the visible box. It only impacts the position of the box.

### Box Sizing 

- **content-box**: The width and height properties are applied to the content box. This is default value.

- **border-box**: The width and height properties are applied to the border box. The content box will shrink to fit the specified width and height. 

1. **Box Model and `width`/`height` Properties**:
   - The comment mentions that the `width` and `height` properties primarily apply to block-level elements. In the CSS box model, a block-level element takes up the full width of its parent container by default and can have its dimensions adjusted using `width` and `height`.

2. **Inline Elements and `width`/`height`**:
   - The comment highlights that inline elements don't inherently respond to the `width` and `height` properties. Inline elements typically occupy only as much horizontal space as necessary to contain their content. Therefore, applying `width` and `height` directly to inline elements may not have the expected effect.

3. **Using `display: inline-block;`**:
   - To make inline elements respond to `width` and `height`, the comment suggests using `display: inline-block;`. This CSS property value allows inline elements to be treated as block-level elements regarding the sizing properties (`width` and `height`) while still maintaining their inline behavior, such as sitting next to each other horizontally.

4. **Removing Space Between Inline-Block Elements**:
   - The comment provides a practical tip for preventing unwanted space between inline-block elements. When you have multiple inline-block elements (e.g., `<span>` elements with the class "box"), placing them directly adjacent to each other in the HTML source code (`<span class="box"></span><span class="box"></span>`) ensures there is no space between them, resulting in a seamless layout.

## Overflowing Content

The CSS `overflow` property is used to control how content that exceeds the dimensions of an element is displayed within that element. It is a crucial property for managing the visibility and behavior of overflowed content. Here are the key aspects of the `overflow` property:

1. **`overflow: visible;`**:
   - When set to "visible" (the default), content that overflows the element's boundaries will be fully visible and extend beyond the element's box. This may affect the layout of surrounding elements.

2. **`overflow: hidden;`**:
   - Setting `overflow` to "hidden" clips or hides content that overflows the element. The hidden content will not be visible to the user, and scrollbars will not appear.

3. **`overflow: scroll;`**:
   - With "scroll," both horizontal and vertical scrollbars are added to the element if the content overflows. Users can scroll to view the hidden content.

4. **`overflow: auto;`**:
   - The "auto" value dynamically adds scrollbars only when content exceeds the element's dimensions. If content fits within the element, no scrollbars are displayed.

5. **Both Horizontal and Vertical Overflow**:
   - The `overflow` property applies to both the horizontal (x-axis) and vertical (y-axis) directions by default. It controls overflow behavior in both dimensions unless you specifically target one axis using `overflow-x` or `overflow-y`.

## Measurement Units

### Absolute Units

- **px**: Pixels are fixed-size units that are used in screen media (i.e., for display on a monitor, phone, tablet, etc.). One pixel is equal to one dot on the computer screen (the smallest unit of an image). The more pixels per inch, the greater the resolution. The pixel unit is relative to the resolution of the screen, and thus is not a physical measurement unit. However, for print media (e.g., in a PDF), pixels are not a good unit to use because they have no physical size.

- pt, in, cm, mm: mainly used in print media. 

### Relative Units

- **%**: The percent unit is relative to the size of the container. For example, setting the `width` of an element to 50% will make its content area half of the width of its container. Percentages are often used to set the `width` and `height` of images, videos, and other media types.

- **vm, vh**: Relative to the viewport.

- **em, rem**: Relative to the font size.

> By default the width of the block level element is 100% 

> By default the height of the block level element is 0%, but the height will adjust to the content inside the element.

In CSS, measurement units play a crucial role in defining the sizes and dimensions of elements. The provided code snippet demonstrates the use of various measurement units. Let's break down the key measurement units and their applications:

```css
html {
    /* trick to make font size = 10px */
    font-size: 62.5%;
}
```

- **`font-size: 62.5%;`**: This line sets the font size for the `html` element to 62.5% of the default font size. This is a common trick used to establish a 1:1 ratio between font size and pixels, making it easier to work with font sizes in CSS. It effectively sets 1 rem (root em) equal to 10 pixels (px).

- **`vw` (Viewport Width)**:
   - The `width: 50vw;` commented out line demonstrates the use of viewport width units (`vw`). It sets the width of the element to 50% of the viewport width.

- **`em` (Relative to Font Size)**:
   - The `width: 10em;` commented out line shows the use of `em` units. An `em` is a unit of measurement that is relative to the font size of the current element. In this case, it would be 10 times the font size of the current element.

- **`rem` (Relative to Root Font Size)**:
   - The `width: 15rem;` line uses `rem` units, which are relative to the font size of the root (`html`) element. It's often preferred for maintaining consistent sizing across the entire document, as it's not influenced by nesting.

- **`vh` (Viewport Height)**:
   - The `height: 100vh;` line uses viewport height units (`vh`). It sets the height of the element to 100% of the viewport height.

- **`border-top: 3px solid orange;`**:
   - This line defines a border style using pixel units (`px`) for the border width.

In summary, CSS offers various measurement units to define sizes and dimensions. Understanding the appropriate use of units like `px`, `em`, `rem`, `vw`, and `vh` is essential for creating responsive and well-proportioned web layouts. The choice of unit depends on the specific use case and the desired responsiveness of the design.

## Positioning

Each element can have several classes by separating them with a space.

```html
<div class="box box-one"></div>
```

By default, the position property of an element is set to static. This means that the element will be positioned according to its place in the normal flow of the page.

### Relative Positioning

Setting the top, right, bottom, and left properties of a relatively-positioned element will cause it to be adjusted away from its normal position. Other content will not be adjusted to fit into any gap left by the element.

- position: relative
    - left, right, top, bottom

In CSS, the `position` property plays a crucial role in determining how elements are positioned within a web page. Two commonly used values for this property are `absolute` and `relative`. Let's clarify the concepts:

#### `position: fixed`: 

Elements with position: `fixed`; are removed from the normal document flow and are positioned relative to the viewport itself. 

#### `position: absolute;`

- When you apply `position: absolute;` to an element, it is positioned relative to its nearest positioned ancestor, not the initial containing block (usually the `<html>` element).

- Positioned ancestors are elements with a `position` property set to anything other than the default `static`. These ancestors establish a reference point for the positioning of child elements with `position: absolute;`.

- `position: absolute;` allows you to precisely position an element by using properties like `top`, `right`, `bottom`, and `left`. The element is removed from the normal document flow, which means it won't affect the layout of other elements.

- Overlapping can occur if multiple absolutely positioned elements are not properly managed. To control their positioning within a specific context, it's common to set a parent container to `position: relative;`. This makes the parent the positioned ancestor for its children with `position: absolute;`.

#### `position: relative;`

- When you set a parent element to `position: relative;`, you establish it as a positioned ancestor for its child elements.

- Child elements with `position: absolute;` are positioned relative to the boundaries of their nearest positioned ancestor (the parent container). This allows you to create specific layouts or effects within the context of the parent without affecting the overall page layout.

- Importantly, elements with `position: relative;` remain in the normal document flow, preserving the integrity of the page structure.

In summary, `position: absolute;` positions an element relative to its nearest positioned ancestor, while `position: relative;` establishes a parent container as the positioned ancestor for its child elements. Understanding these concepts is crucial for precise layout control in CSS.

### Three axis

- x-axis: left, right

- y-axis: top, bottom

- z-axis: z-index
    - By default, all elements have a z-index of 0. The z-index property specifies the stack order of an element. An element with greater stack order is always in front of an element with a lower stack order.

    - When multiple HTML elements have the same z-index value (which is the default 0 if not specified), they are considered to be in the same stacking context, and their order in the stacking context is determined by the order in which they appear in the HTML markup.

### Two ways to set the position elements

1. Width and Height

2. Top, Right, Bottom, Left
```html
    left: 2rem;
    right: 2rem;
    width: auto; /* let the browser decide how wide it should be */
```


## Floating Elements

The CSS `float` property is used to specify how an element should float. It is commonly used to float images, but it is also useful for layouts that require smaller elements to be floated next to larger elements. Here are the key aspects of the `float` property:

1. **`float: left;`**:
    - The `float` property is set to "left" to float an element to the left of its container. The floated element will move as far to the left as possible, and other content will wrap around it.

    - How can we make element not wrap around the floated element? We can use the `clear` property to prevent content from wrapping around a floated element. The `clear` property specifies which sides of an element other floating elements are not allowed. The `clear` property can have one of the following values:

        - `none` - Allows floating elements on both sides. This is default

        - `left` - No floating elements allowed on the left side

        - `right` - No floating elements allowed on the right side

        - `both` - No floating elements allowed on either the left or the right side

### By default, parent elements don't see floated elements.

Therefore, the height will not consider the height of the floated elements. 

We can use pseudo element `::after` and `clear:both` to fix this problem.

```css
.clearfix::after {
    content: '';
    display: block;
    clear: both;
}
```
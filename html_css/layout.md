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
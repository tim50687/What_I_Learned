# Writing clean maintainable CSS

## Create logical sections in your stylesheet

```css
/* Basic styles */
* {
    box-sizing: border-box;
}

html {}

/* Typography */
h1, h2, h3 {}

/* Forms */

/* Navigation Bar */
```

> In a large project, you will seperate this section into multiple files.

## Avoid over-specific selectors

- Don't use direct child selectors too often

- Avoid !important

- Take advantage of the inheritence

## Variables

We can use 

```css
:root {
    --main-bg-color: #fff;
    --main-text-color: #333;
}
```

to define global variables.

- Start with `--`

Then we can access the variable using

```css
.one {
    background: var(--main-bg-color);
}
```

## Object Oriented CSS

1. Seperate container from content

2. Seperate structure from skin

## BEM (Block Element Modifier)

- Use `__` to seperate block and element

- block inside the block, we can drop the prefix

- Use `--` to seperate block and modifier

```html
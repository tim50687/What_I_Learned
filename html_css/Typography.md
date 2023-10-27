# Typography 

## Styling Fonts

- font-weight: 100 - 900 
    - boldness of the font

- font-style: normal | italic | oblique
    - italic: slanted version of the font
    - oblique: slanted version of the font, but not as much as italic

- font-size: 1em | 1rem | 1px | 1pt | 1pc | 1cm | 1mm | 1in
    - em: relative to the font-size of the element
    - rem: relative to the font-size of the root element
    - px: pixels
    - pt: points
    - pc: picas
    - cm: centimeters
    - mm: millimeters
    - in: inches

- color: red | #ff0000 | rgb(255, 0, 0) | rgba(255, 0, 0, 0.5)
    - red: color name
    - #ff0000: hex code
    - rgb(255, 0, 0): rgb code
    - rgba(255, 0, 0, 0.5): rgba code, the last number is the opacity

### Three main category of fonts

1. Serif

- small line or small stroke at the end of character

2. Sans-serif

- no small line or small stroke at the end of character

3. Monospace

- each character takes up the same amount of space
    - ideal for displaying code


### Inheritance

- Remove duplicate code:

Put the font-family property on the body element, so that the children elements can inherit the font-family property.


## Embedding Web Fonts

### Font Formats

- .ttf: TrueType font

- .otf: OpenType font

- .woff: Web Open Font Format

- .woff2: Web Open Font Format 2

- .eot: Embedded OpenType font

For web we will use `WOFF`, `WOFF2`, because these two format are more compressed and more efficient for web.

## Flash of Unstyled Text (FOUT)

- While the browser loads the page, it will display the text in the default font first, then when the font is loaded, it will display the text in the font we specified.

- Font-display: auto(default) 
    - But this is diffferent from all browser.

- Font-display: swap 
    - We want to explicitly tell the browser to use the fallback font first, then when the font is loaded, it will display the text in the font we specified. (`better than auto`)
    - This is the most common way to solve the FOUT problem.

- Font-display: fallback (better approach)
 
    - Acts as a compromise between the auto and swap values. The browser will hide the text for about 100ms and, if the font has not yet been downloaded, will use the fallback text. It will swap to the new font after it is downloaded, but only during a short swap period (probably 3 seconds).

- Font-display: optional
    - The browser will hide the text for about 100ms and, if the font has not yet been downloaded, will use the fallback text.
    - Optional had a 100ms block period and no swap period. This means that "invisible" text is displayed very briefly before switching to a fallback font. If the font is not downloaded within 100ms, then the fallback font is used and no swapping occurs.
    - `However`, behind the scene, it will try to download the font in the background and store it in the cache. In subsequent page loads, the font will be loaded from the cache and the text will be displayed in the font we specified.

### Reduce download size

- You can reduce the download size of the font by only including the characters you need.


## Font Services

Some of the fonts need to be licensed, so we need to pay for them. But there are some free fonts that we can use.

- [Google Fonts](https://fonts.google.com/)
    - But we cannot using subset to reduce the download size.
- [Adobe Fonts](https://fonts.adobe.com/)


## System Fonts Stack

With this stack, we can tell the browser to use the default font of the OS on the user's computer.

- Benefits:
    - Can boost performance
    - No FOUT
    - Native look and feel
    - Overall: better experience

- Drawbacks:
    - No control over the font


## Sizing Fonts

- We should `avoid using px` to size fonts, because it is not consistent across devices.

- We should use relative units to size fonts, such as `em`, `rem`, `vw`, `vh`, `vmin`, `vmax`.

## Vertical Spacing

- Law of Proximity: elements that are close to each other are perceived to be more related than elements that are further apart.

### Line Height

We can use `line-height` to control the vertical spacing between lines of text.

- General rule of thumb: `line-height` should be `1.5` times the `font-size`.

- `line-height: 1.5;` (Trick)
    - If we set the `line-height` to `1.5`, then the line height will be `1.5` times the `font-size`.
    - So that when we adjust the font size, we don't need to change the `line-height`.

## Horizontal Spacing

1. letter-spacing

- Usually we use absolute units to size the letter spacing, such as `px`, `pt`, `cm`, `mm`, `in`.

- negative values are allowed

2. word-spacing

3. width

### Ideal Line Length

How many characters should be in a line?

- 50 to 70 characters per line

```css
p {
    width: 50ch;
}
```

- `ch`: width of the `0` character

In this case, that is equivalent to `50 zeros`. But some character like `1` or `i` take less space. Therefore it's roughly `60 - 70` characters per line.


## Formatting Text

1. Text-Align

2. Text-Indent

What if you want to indent the second paragraph?

---
**CSS Selector: `p + p`**

- **Selector Meaning**: The `p + p` selector targets paragraphs (`<p>`) that directly follow another paragraph. It selects the second and subsequent paragraphs in a sequence when they immediately follow a preceding paragraph.

- **Usage**: This selector is commonly used when you want to apply specific styles to paragraphs that are not the first paragraph in a series of consecutive paragraphs. It allows you to differentiate the styling of paragraphs based on their position in the document structure.

- **Example**: Consider the following HTML:

  ```html
  <p>This is the first paragraph.</p>
  <p>This is the second paragraph, styled differently.</p>
  <p>This is the third paragraph, also styled differently.</p>
  ```

  Applying `p + p` CSS rules could be used to style the second and third paragraphs differently from the first paragraph. For example, you could set different margins, font sizes, or text alignments for these paragraphs.

- **Note**: It's important to understand that the `p + p` selector specifically targets paragraphs that immediately follow another paragraph. If there's any other element (e.g., a heading or a list) between the paragraphs, the selector won't match.

- **Use Cases**: This selector can be useful for creating visually distinct styles for paragraphs in situations like article content, where you want to style the initial paragraph differently from subsequent paragraphs for better readability or aesthetics.

---
3. Text-decoration

4. text-transform

5. white-space

6. column-count

- `column-count: 2;`
    - We will have two columns

- `column-gap: 2rem;`
    - We will have a gap of `2rem` between the two columns

- `column-rule: 1px solid #ccc;`
    - We will have a rule of `1px solid #ccc` between the two columns

7. direction

### How to truncate text

1. `width` 

2. `white-space`: nowrap

- We will end up with only one line of text

3. `overflow`: hidden

- Any extra content will be hidden

4. `text-overflow`: ellipsis

- So we get the ellipsis (...) at the end of the text


# Transformation

## 2D Transformation
- rotate()
    - `rotate(45deg)`: 45 degrees clockwise

- scale()
    - `scale(2, 3)`: 2 times wider and 3 times taller

- skew()
    - `skew(30deg, 20deg)`: 30 degrees on the x-axis and 20 degrees on the y-axis

- translate()
    - `translate(100px, 50px)`: 100px to the right and 50px down

> The order of the function matters

```html
.box:hover {
    transform: skew(20deg, 30deg) translate(100px);
}
```

## 3D Transformation

**Applying the Hover Effect with Transform**

```css
.box:hover {
    transform: perspective(200px) translateZ(-50px);
}
```

- `.box:hover`: This is a CSS rule that targets elements with the class `.box` when they are in a hovered state. It uses the `:hover` pseudo-class to specify the hover effect.

- `transform`: The `transform` property is used to apply transformations to an element. In this case, it is used to create a 3D transform effect when the element is hovered.

- `perspective(200px)`: The `perspective()` function defines the perspective from which the element is viewed. It creates a 3D space with depth, and the `200px` value sets the depth of the perspective.
    - We need to add perspective first.

- `translateZ(-50px)`: The `translateZ()` function translates the element along the Z-axis, which creates a depth effect in the 3D space. When the element is hovered, it moves 50 pixels away from the viewer along the Z-axis (towards the background).


**Creating 3D Transformations on Hover**

In the provided CSS code snippet, 3D transformations are applied to elements within a container when the container is hovered. The `perspective` property is used to establish a 3D space, and `transform` is employed to rotate elements. Here's a note explaining this code:

```css
.container {
    perspective: 200px;
}

.container:hover .box {
    transform: rotateY(45deg);
    transform-origin: 0 0;
}

.container:hover .box-sp {
    transform: rotateX(45deg);
}
```

- `.container`: This CSS rule selects elements with the class `.container`. The `perspective` property is applied to create a 3D perspective for child elements within this container.

- `perspective: 200px;`: The `perspective` property sets the depth of the 3D space in which child elements will be transformed. In this case, it's set to `200px`, which determines the depth of the 3D perspective.

- `.container:hover .box`: This CSS rule selects elements with the class `.box` when they are children of a `.container` that is being hovered.

- `transform: rotateY(45deg);`: The `transform` property applies a 3D rotation effect to `.box` elements when the container is hovered. It rotates them by `45deg` around the Y-axis, creating a horizontal (side-to-side) rotation effect.

- `transform-origin: 0 0;`: The `transform-origin` property specifies the point around which the rotation occurs. In this case, it's set to the top-left corner of the `.box` elements (`0 0`), so they rotate around their top-left corner.

- `.container:hover .box-sp`: This CSS rule selects elements with the class `.box-sp` when they are children of a `.container` that is being hovered.

- `transform: rotateX(45deg);`: Similar to the previous rule, this line applies a 3D rotation effect to `.box-sp` elements when the container is hovered. It rotates them by `45deg` around the X-axis, creating a vertical (up-and-down) rotation effect.

**Note:**

- The `perspective` property is used to create a 3D perspective within the `.container`, affecting how child elements are transformed in 3D space.

- The `transform` property is applied to rotate `.box` and `.box-sp` elements when the `.container` is hovered. `rotateY(45deg)` rotates around the Y-axis (horizontal), and `rotateX(45deg)` rotates around the X-axis (vertical).

- `transform-origin` determines the pivot point for the rotation, affecting where the element appears to rotate from.

- These CSS rules create an interactive 3D effect when users hover over the container, providing a visually engaging experience.

## Transitions

```html
.box {
    width :100px;
    height: 100px;
    background: gold;
    transition: transform 0.5s ease-out 1s;
}
```
We can add the transition property to the `.box` element to create a smooth transition effect when the element is transformed. The `transition` property specifies the CSS property to which the transition should be applied, the duration of the transition, and the timing function that controls the transition effect.

## Animation

**Creating a Keyframe Animation - "pop"**

In the provided CSS code snippet, a keyframe animation named "pop" is defined using the `@keyframes` rule. This animation applies a series of transformations and style changes to an element with the class `.box`. Here's a note explaining this code:

```css
@keyframes pop {
    0% {
        transform: scale(1);
    }

    25% {
        transform: scale(1.3);
    }

    50% {
        transform: rotate(45deg);
        background: tomato;
    }

    100% {
        transform: rotate(0);
    }
}

.box {
    width: 100px;
    height: 100px;
    background: gold;
    animation-name: pop;
    animation-duration: 4s;
}
```

**Keyframes Animation:**

- `@keyframes pop`: This rule defines a keyframe animation named "pop." Keyframe animations allow you to specify a series of style changes and transformations that occur at specific percentages of the animation's duration.

- `0%`: At the start of the animation (0% progress), the `transform` property sets the element's scale to its original size (`scale(1)`).

- `25%`: At 25% progress, the `transform` property scales the element to 1.3 times its original size (`scale(1.3)`).

- `50%`: At the midpoint (50% progress), the `transform` property rotates the element by 45 degrees (`rotate(45deg)`) and changes the background color to "tomato."

- `100%`: At the end of the animation (100% progress), the `transform` property resets the rotation to 0 degrees (`rotate(0)`).

**Animation Application:**

- `.box`: This CSS rule selects elements with the class `.box`. These elements will be animated using the "pop" animation.

- `width` and `height`: The `.box` elements are defined with a width and height of 100px, creating square elements.

- `background`: The background color of the `.box` elements is set to "gold."

- `animation-name: pop;`: The `animation-name` property specifies the name of the keyframe animation to apply, which is "pop."

- `animation-duration: 4s;`: The `animation-duration` property sets the duration of the animation to 4 seconds.

**Note:**

- Keyframe animations, defined using `@keyframes`, allow you to create complex animations by specifying styles and transformations at different points in the animation's timeline (percentage values).

- In this example, the "pop" animation scales, rotates, and changes the background color of `.box` elements as it progresses.

- You can customize the animation further by adjusting the properties and keyframe percentages to achieve different visual effects.

## Reusable Animations
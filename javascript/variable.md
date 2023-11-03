# Variable

## Undefined

- The default value of a variable that has not been assigned a value is `undefined`.

## Array

- Array is an object in JavaScript.

**In JavaScript Arrays: Assignment to a Specific Index**

When you write `selectedColors[5] = 'green';` in JavaScript, you are assigning the value 'green' to the element at index 5 in the `selectedColors` array. `If there was already an element at index 5, it would be overwritten with 'green'. If there was no element at index 5, JavaScript would create an element at that index and set its value to 'green'.` This operation modifies the array in place and does not append 'green' to the end of the array. It's essential to be aware of this behavior when working with arrays in JavaScript.

```javascript
let selectedColors = ['red', 'blue'];
selectedColors[5] = 'green';
```

# Control Flow

## Switch...Case
In JavaScript, when a `switch` statement is executed, it starts from the matched case and continues executing code until it encounters a `break` statement or reaches the end of the `switch` block. In your code, when the `role` is 'guest', it enters the first case block and executes the `console.log("guest user");`. However, it doesn't encounter a `break` statement, so it continues to execute the code in the subsequent `case` block, which is 'moderator', leading to the execution of `console.log("Moderator User");`.


```javascript
let role;
role = 'guest';

switch (role) {
    case 'guest':
        console.log("guest user");
        break; // Add a break statement here
    case 'moderator':
        console.log("Moderator User");
        break;
}
```


- default case
    - If none of the cases match, the code in the `default` case will be executed.
    - The `default` case is optional. If you don't have a `default` case, and none of the cases match, the code in the `switch` block will not be executed.


## For in loop

For in loop is used to iterate over the properties of an object or the elements of an array.

- Use for in loop to iterate over the `properties of an object` or `index of an array`.

```javascript
// for in 

const person = {
    name: 'tim',
    age:30
};
// Object
for (let key in person) {
    console.log(key, person[key]); // name age
}

const colors = ['red', 'green', 'blue'];
// Array
for (let index in colors) {
    console.log(index, colors[index]);
}
```

## For of loop

Use for of loop to iterate over the **`elements of an array`**.

```javascript
// For of 
for (let color of colors) {
    console.log(color);
}
```
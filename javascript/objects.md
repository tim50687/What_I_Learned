# Objects

- Every object has constructor property and that references the function that was used to create that object.

## Object Literals

```javascript
const circle = {
  radius: 1,
  location: {
    x: 1,
    y: 2,
  },
  isVisible: true,
  draw: function () { // called method
    console.log("draw");
  },
};

circle.draw();
```

## Create object

### Factory function

- Naming convention: Camel Notation

```javascript
// Factory function

function createCircle(radius) {
  return {
    radius, // if key and value are the same name, we can remove the value

    draw() {
      // another way to define funciton
      console.log("draw");
    },
  };
}

const myCircle = createCircle(1);
```

### Constructor function
- Naming convention: Pascal Notation

```javascript
// Constructor Function
function Circle(radius) {
  this.radius = radius;
  this.draw = function () {
    console.log("draw");
  };
}

const circle = new Circle(1);
```

## Dynamic nature of objects

```javascript
// Constructor Function
function Circle(radius) {
  this.radius = radius;
}

const circle2 = new Circle(1);
// add property or method
circle2.color = "yellow";
circle2.draw = function () {};
// delete property or method
delete circle2.draw;
console.log(circle2);
```

> With `const`, we can not reassigned the circle2 variable to a new object. But we can change the properties and methods of the object.


## Values vs Reference Types

- Value Types: Number, String, Boolean, Symbol, undefined, null
    - Primitives are copied by their value
- Reference Types: Object, Function, Array
    - Objects are copied by their reference

## Cloning an object

```javascript
const circle = {
  radius: 1,
  draw() {
    console.log("draw");
  },
};
// old
// const another = {};

// for (let key in circle) {
//   another[key] = circle[key];
// }

// new
// copies the properties and methods from one or more objects into a target object, you can also add the property
// const another = Object.assign(
//   {
//     color: "yellow",
//   },
//   circle
// );

// elegant way
const another = { ...circle };

console.log(another);
```

## Built-in Objects

- Math
- Date
- String
    
    We have two kind of string: primitive string and string object. Primitive string is not an object, so it does not have any methods. But when we call a method on a primitive string, JavaScript will automatically wrap the string primitive to a string object, then call the method, then convert it back to a primitive string.


- ...

## Template Literals

```javascript
const name = "tim";
// we have place holder (variable, operation, function)
const message = ` 
Hi ${name} ${2 * 18}
This 'is' my 
first message`;
console.log(message);
```

## Date

```javascript
const now = new Date();
const date1 = new Date("May 11 2018 09:00");
const date2 = new Date(2018, 4, 11, 9); // 4 is May, 0 is January
```

- Has a lot of get/ set methods

## Enumerating Properties of an Object

```javascript
for (let key of Object.keys(circle)) {
  console.log(key);
}

for (let entry of Object.entries(circle)) {
  console.log(entry);
}
```
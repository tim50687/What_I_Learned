# Prototypical Inheritence

## Object.create

- The Object.create() static method creates a new object, using an existing object as the prototype of the newly created object.

```javascript
function Shape() {}

Shape.prototype.duplicate = function () {
  // duplicate method
  console.log("duplicate");
};

function Circle(radius) {
  this.radius = radius;
}

Circle.prototype = Object.create(Shape.prototype);

Circle.prototype.draw = function () {
  console.log("draw");
};

const s = new Shape();
const c = new Circle(1);

```


> It creates a new object that has Shape.prototype as its prototype. This new object is then assigned to Circle.prototype.
```
Circle.prototype = Object.create(Shape.prototype);
```

### Resetting the Constructor

```javascript
Circle.prototype = Object.create(Shape.prototype);
```

This will make the constructor of Circle to be Shape. We want it to be Circle.

**So, as a best practice, we should always reset the constructor**

```javascript
Circle.prototype = Object.create(Shape.prototype);
Circle.prototype.constructor = Circle;
```

## Calling the Super Constructor

```javascript
function Shape(color) {
  this.color = color;
}

Shape.prototype.duplicate = function () {
  // duplicate method
  console.log("duplicate");
};

function Circle(radius, color) {
  Shape.call(this, color);
  this.radius = radius;
}
```

- The `call()` method of Function instances calls this function with a given `this` value and arguments provided individually.

1. The `this` refers to the Circle object that is being created.

2. This means that when Shape sets this.color = color;, it is actually setting the `color property on the new Circle object`.

## Intermediate Function Inheritance

If we want to create a Square object that inherits from Shape, we can do this:

```javascript
Square.prototype = Object.create(Shape.prototype);
Square.prototype.constructor = Square;
```

However, we don't want to repeat this code for every object we want to create. So, we can create an intermediate function called extend.

```javascript
function extend(Child, Parent) {
  Child.prototype = Object.create(Parent.prototype);
  Child.prototype.constructor = Child;
}
```

## Mixins

```javascript
const canEat = {
  eat: function () {
    this.hunger--;
    console.log("eating");
  },
};

const canWalk = {
  walk: function () {
    console.log("walking");
  },
};

const canSwim = {
  swim: function () {
    console.log("swimming");
  },
};

function Person() {}
// we can use assign to copy the properties and methods of one object to another
Object.assign(Person.prototype, canEat, canWalk);

const person = new Person();

console.log(person);

function Goldfish() {}

Object.assign(Goldfish.prototype, canEat, canSwim);

const goldfish = new Goldfish();
```

However, we can make the code more readable by creating a mixin function.

```javascript
function mixin(target, ...sources) {
  Object.assign(target, ...sources);
}
```

- `...sources`:  is the rest parameter syntax that captures all additional passed arguments into an array called sources. This means mixin can take one or more source objects.
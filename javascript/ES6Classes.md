# ES6 Classes

## Syntatic sugar over constructor functions

```javascript
class Circle {
  constructor(radius) {
    this.radius = radius;
  }

  // draw will be added to the prototype
  draw() {
    console.log('draw');
  }
}
``` 

## Hoisting

### Function declaration

It will be hoisted to the top of the file.

### Function expression

It will not be hoisted to the top of the file.  

### Class declaration

```javascript
class Circle {
}
``` 

### Class expression

```javascript
const Square = class {
}
```

> Class declarations or Class expression are not hoisted.



## Static Method

```javascript
class Circle {
  constructor(radius) {
    this.radius = radius;
  }

  // Instance method
  draw() {
    console.log('draw');
  }

  // Static method
  static parse(str) {
    const radius = JSON.parse(str).radius;
    return new Circle(radius);
  }
}

const circle = Circle.parse('{ "radius": 1 }');
console.log(circle);
```


- `static method` : a method that is not available on the instance. It's only available on the class itself.
    - Create utility functions that are not tied to a particular object.

- `Strict mode` : It's a feature that was added in ES5. It prevents us from accidentally doing something with the global object. It makes our code more secure.

## Private Members Using Symbols

In ES6, we have a new primitive type called `Symbol`. It's used to generate `unique identifiers`. 

```javascript
const _radius = new Symbol();
const _draw = new Symbol();

class Circle {
  constructor(radius) {
    // this.radius = radius;
    this[_radius] = radius;
  }


    [_draw]() {
        console.log('draw');
    }
}
```

## Private Members Using WeakMaps

- WeakMap is a new type of collection in ES6. It's very similar to a Map with a few differences:
    - The keys of a WeakMap must be objects, not primitive types.
    - The keys of a WeakMap are `weak`. This means that they do not prevent garbage collection in JavaScript. We can't enumerate the keys of a WeakMap. This was done for security reasons. We cannot access private members from the outside.

```javascript
const _radius = new WeakMap();
const _move = new WeakMap();

class Circle {
  constructor(radius) {
    _radius.set(this, radius); // key: this, value: radius

    _move.set(this, () => {
      console.log('move', this);
    });
  }

  draw() {
    _move.get(this)();

    console.log('draw');
  }
}
```

- We can use `get` and `set` methods to get and set the value of a private member.


## Getters and Setters

```javascript
const _radius = new WeakMap();

class Circle {
  constructor(radius) {
    _radius.set(this, radius);
  }

  get radius() {
    return _radius.get(this);
  }

  set radius(value) {
    if (value <= 0) throw new Error('invalid radius');

    _radius.set(this, value);
  }
}
```

## Inheritance

```javascript
class Shape {
  constructor(color) {
    this.color = color;
  }

  move() {
    console.log('move');
  }
}

class Circle extends Shape { // with extends, we don't have to reset the constructor
  constructor(color, radius) {
    super(color);
    this.radius = radius;
  }

  draw() {
    console.log('draw');
  }
}
```

## Method Overriding

```javascript
class Shape {
  move() {
    console.log('move');
  }
}

class Circle extends Shape {
  move() {
    super.move(); // call the base implementation
    console.log('circle move');
  }
}
```

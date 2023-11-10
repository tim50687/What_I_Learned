# Prototypes

- A `prototype` is essentially a parent of an object.

- We can get object prototype by `Object.getPrototypeOf(obj)`.

- Object created by a given constructor will have the same prototype.

## Property descriptors
When we create a JavaScript object, whether using object literal syntax or some other means and add some properties to it, `each property (key) gets a default property descriptor`. A property descriptor is a simple JavaScript object associated with each property of the object that `contains information about that property such as its value and other meta-data.`

```javascript

let person = {name: 'Mosh'};
let ObjectBase = Object.getPrototypeOf(person);
let descriptor = Object.getOwnPropertyDescriptor(ObjectBase, 'toString');
```

- `writable` - whether the value of the property can be changed or not (can overwrite ). Default is `true`.

- `enumerable` - whether the property shows up in a `for...in` loop and `Object.keys()` or not. Default is `true`.

- `configurable` - whether the property can be deleted or not. Default is `true`.

```javascript
Object.defineProperty(person, 'name', {
    writable: false,
    enumerable: false,
    configurable: false
});
```

> The Object.defineProperty method in JavaScript is used to define a new property directly on an object, or modify an existing property on an object. In the snippet you provided, Object.defineProperty is being used to define or modify the property descriptor for the name property on a persion object. 


## Constructor Prototypes

- Every object has a `prototype` property.

- `prototype` is a property that references another object.

- All objects created by a given constructor will have the same prototype.

- Only function objects have the `prototype` property.

- `Circle.prototype` **this property for function**, is an object that will be used as a prototype for all the objects created by the `Circle` constructor.


## Prototype vs Instance Members

```javascript
function Circle(radius) {
    this.radius = radius;
    this.draw = function () {
        console.log('draw');
    }
}

const c1 = new Circle(1);
const c2 = new Circle(1);
```

We will copy the `draw` method to each instance. `This is not ideal`. We want to have only one copy of this method.

```javascript

function Circle(radius) {
    // instance members
    this.radius = radius;
    this.move = function () {
        console.log('move');
    }
}
// solution
// prototype members
Circle.prototype.draw = function () { // because it's dynamic, we can add something later
    console.log('draw');
    this.move(); // we can access instance members from prototype members
}
// We can also overwrite the toString inherited from ObjectBase
Circle.prototype.toString = function () {
    return 'Circle with radius ' + this.radius;
}

const c1 = new Circle(1);
const c2 = new Circle(1);
```

- We can still access `draw` method from `c1` and `c2` because `JavaScript engine` will look for `draw` method in `c1` and `c2` first, if it can't find it, it will look for it in `Circle.prototype`.

---

**JavaScript Prototypal Inheritance and Method Calling**

In JavaScript, objects created by a constructor function can have both instance-specific members and shared members via the prototype.

- **Instance Members**: Defined within the constructor function and are unique to each instance. Each new object has its own copy of these members.

- **Prototype Members**: Defined on the constructor's prototype object (`ConstructorFunction.prototype`) and are shared across all instances of the constructor.

**Method Calling Between Instance and Prototype Members**:

- Instance members can call prototype members because `this` within the context of an instance method refers to the instance itself, which has access to prototype methods.

- Prototype members can call instance members when they are invoked by an instance, since `this` will be bound to the instance that invoked the method, allowing access to instance-specific members.

---

## Iterating Instance and Prototype Members

```javascript
function Circle(radius) {
    // instance members
    this.radius = radius;
    this.move = function () {
        console.log('move');
    }
}

Circle.prototype.draw = function () {
    console.log('draw');
}

const c1 = new Circle(1);

// returns instance members
console.log(Object.keys(c1)); // ['radius', 'move']

// returns all members (instance + prototype)
for (let key in c1) console.log(key); // radius, move, draw
```

- Sometimes we refer to instance as `own`.

## Avoid Extending the Built-in Objects

```javascript
Array.prototype.shuffle = function() {
    // ...
}
const array = [];
array.shuffle();
```

- We should avoid extending the built-in objects because we can run into problems.
    - Because some where else you might be using, there might be a library that is depending on the original implementation of the `Array` object.

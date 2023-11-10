# Object 

## Object literal

- Not a good way to create an object

```javascript
const circle = {
    radius: 1,
    location: {
        x: 1,
        y: 1
    },
    draw: function() {
        console.log('draw');
    }
};
circle.draw();
```

## Factory function

```javascript
function createCircle(radius) {
    return {
        radius, // can remove the value if key == value
        draw: function() {
            console.log('draw');
        }
    };
}
const circle = createCircle(1);

```

## Constructor function

```javascript
function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}
const another = new Circle(1);
```

## Adding or removing properties

```javascript
function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}
const circle = new Circle(10);
circle.location = { x: 1 };
const propertyName = 'center location'; // dynamically access a property
circle[propertyName] = { x: 1 };
delete circle.location;
delete circle[propertyName];
```

- If you have special characters in the property name, you can't use the dot notation. You have to use the `bracket notation`.

- If you want to dynamically access a property, you can't use the dot notation. You have to use the `bracket notation`.

## Enumerating properties

```javascript
function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}
const circle = new Circle(10);
for (let key in circle) {
    if (typeof circle[key] !== 'function')
        console.log(key, circle[key]);
}

// another way to get all the keys
const keys = Object.keys(circle);

// Check if an object has a given property
if ('radius' in circle)
    console.log('Circle has a radius.');
```

## Abstraction

we should hide the details and complexity and show only the essentials.

```javascript
function Circle(radius) {
    this.radius = radius;
    this.defaultLocation = { x: 0, y: 0 };
    this.computeOptimumLocation = function(factor) {
        // ...
    };
    this.draw = function() {
        this.computeOptimumLocation(0.1);
        console.log('draw');
    }
}
```

- We don't want user have access to radius and defaultLocation.

## Private properties and methods

- We can use `let` instead of `this` to make a property private.
    - This is because `let` is a local variable.

```javascript
function Circle(radius) {
    this.radius = radius;
    let defaultLocation = { x: 0, y: 0 };
    let computeOptimumLocation = function(factor) {
        // ...
    };
    this.draw = function() {
        computeOptimumLocation(0.1);
        console.log('draw');
    }
}
```

## Getters and setters

```javascript
function Circle(radius) {
    this.radius = radius;
    let defaultLocation = { x: 0, y: 0 };
    this.draw = function() {
        console.log('draw');
    };
    Object.defineProperty(this, 'defaultLocation', {
        get: function() {
            return defaultLocation;
        },
        set: function(value) {
            if (!value.x || !value.y)
                throw new Error('Invalid location.');
            defaultLocation = value;
        }
    });
}
const circle = new Circle(10);
circle.defaultLocation = 1;
```

- `Object.defineProperty` defines a new property for an object.
    - The first argument is the object.
    - The second argument is the name of the property.
    - The third argument is an object that has a bunch of key/value pairs.
        - `get` is a function that is used to read the property.
        - `set` is a function that is used to set the property.
# Function

## Function Declaration

```javascript
function name(parameter1, parameter2, parameter3) {
  // code to be executed
}
```

## Function Expression

```javascript
let run = function() {
  // code to be executed
};

run();
let move = run;
```

### Difference between Function Declaration and Function Expression

- `Function Declaration` can be called before it is defined.
    - Because java script engine moves all function declarations to the top of the current scope. (`hoisting`)


## Arguments

```javascript
function sum(a, b) {
  return a + b
}

console.log(sum(1)); // 1 + undefined = NaN

// we can pass 5 argument
console.log(sum(1, 2, 3, 4, 5)); // 3
```


### How do we pass varying number of arguments to a function?

```javascript
function sum() {
  let total = 0;
  for (let value of arguments) // can use for any iterator
    total += value;
  return total;
}

console.log(sum(1, 2, 3, 4, 5)); // 15
```

#### Alternative

```javascript
function sum(...args) {
  return args.reduce((a, b) => a + b);
}
```

The rest operator `...` will convert all the arguments to an array.

```javascript
function sum(discount, ...args) {
  const total = args.reduce((a, b) => a + b);
  return total * (1 - discount);
}

console.log(sum(0.1, 1, 2, 3, 4, 5)); // 13.5

```

> rest operator must be the last parameter

## Default Parameters

```javascript
function interest(principal, rate = 3.5, years = 5) {
  return principal * rate / 100 * years;
}
```

> If you put the default value for the first parameter, you have to put the default value for the rest of the parameters.

## Getter and Setter
    
```javascript
const person = {
    fistName: 'Tim',
    lastName: "jack",
    get fullName() {
        return `${person.fistName} ${person.lastName}`;
    },
    set fullName(value) {
        if (typeof value !== 'string')
            throw new Error('Value is not a string.'); // defensive programming
        const parts = value.split(' ');
        if (parts.length !== 2)
            throw new Error('Enter a first and last name.');
        this.fistName = parts[0];
        this.lastName = parts[1];
    }
}

// 1
// console.log(`${person.fistName} ${person.lastName}`);

// 2. getter
console.log(person.fullName);

// 3. setter
try {
person.fullName = 'John Smith';
} catch (e) {
    alert(e); // let end user know what is wrong
}
```

## Let vs Var

```javascript
function start() {
    for (var i = 0; i < 5; i++) {
        console.log(i);
    }

    console.log(i); // 5
}
```

- It's scope is not limited to the block statement.
- It's scope is limited to the function.
- It will attach to the window object.

> Avoid using `var` keyword.

## This

```javascript
const video = {
    title: 'a',
    play() {
        console.log(this);
    }
};

video.stop = function() {
    console.log(this);
};

video.play(); // {title: "a", play: ƒ}
video.stop(); // {title: "a", play: ƒ, stop: ƒ}


// global
function playVideo() {
    console.log(this);
}

playVideo(); // window object

// constructor function

function Video(title) {
    this.title = title;
    console.log(this);
}
```
- When dealing with regular function calls, `this` will point to the global object (window object in the browser).

#### Another example

```javascript
const video = {
    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        this.tags.forEach(function(tag) {
            console.log(this.title, tag); // undefined a, undefined b, undefined c
        }, this); // we can refer to the current object
    }
};
```

- `this` in the callback function is not the same as `this` in the `showTags` function. `It is window object.`

> However not every function has the `this` keyword. 

```javascript
// sol 1
const video = {
    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        const self = this;
        this.tags.forEach(function(tag) {
            console.log(self.title, tag);
        });
    }
};

// sol 2
function playVideo(a, b) {
    console.log(this);
}

playVideo.call({ name: 'Tim' }, 1, 2); // {name: "Tim"}
playVideo.apply({ name: 'Tim' }, [1, 2]); // {name: "Tim"}

// The only difference between call and apply is the way we pass the arguments.

playVideo.bind({ name: 'Tim' })(); // {name: "Tim"}
// bind returns a new function. We can store it in a variable and call it later.

const video = {
    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        this.tags.forEach(function(tag) {
            console.log(this.title, tag);
        }.bind(this));
    }
};

// sol 3
const video = {
    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        this.tags.forEach(tag => {
            console.log(this.title, tag);
        });
    }
};

```

> `Arrow functions` inherit from the containing function.
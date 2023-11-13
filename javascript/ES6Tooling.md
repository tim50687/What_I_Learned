# ES6 Tooling

We separate our code into multiple files (called `module`). 


## CommonJS

- This is the module system used by Node.js.

- We use `require` to load a module.

1. Create a new file 

`circle.js`

```javascript
const _radius = new WeakMap();

class Circle {
  constructor(radius) {
    _radius.set(this, radius);
  }

  draw() {
    console.log("Circle with radius " + _radius.get(this));
  }
}

module.exports = Circle; // module.exports is an object that has a property called Circle, and the value of that property is the Circle class

```

2. Load the module

```javascript
const Circle = require("./circle"); // Circle is a reference to the object that was exported from circle.js
const c = new Circle(1);
c.draw(); // Circle with radius 1
```


## ES6 Modules

- We use `import` and `export` to load and export modules.

1. Create a new file

`circle.js`

```javascript
const _radius = new WeakMap();

export class Circle {
  constructor(radius) {
    _radius.set(this, radius);
  }

  draw() {
    console.log("Circle with radius " + _radius.get(this));
  }
}
```

2. Load the module

```javascript
import { Circle } from "./circle.js"; // Circle is a reference to the object that was exported from circle.js
const c = new Circle(1);
c.draw(); // Circle with radius 1
``` 

## Babel

- Babel is a JavaScript compiler. It converts the code that all browsers can understand.
- It converts the new version of JavaScript (ES6, ES7, ES8) to the old version (ES5).

1. `npm init -y` : create a new package.json file with default settings. 
    - package.json is a file that contains information about our project.

2. `npm i babel-cli babel-core babel-preset-env --save-dev` : install babel-cli and babel-preset-env packages.
    - `babel-cli` is a command line interface for babel.
    - `babel-core` is the core module of babel.
    - `babel-preset-env` is a plugin that tells babel to use the latest features of JavaScript.
    - `--save-dev` means that we want to install these packages as development dependencies. 
        - We don't want to install these packages on the production server.


## Webpack

### Workflow

1. `npm i -g webpack-cli` : install webpack globally.
    - `webpack` is a module bundler. It takes all the JavaScript files and bundles them into one file.
    - `i` is short for `install`.
    - `-g` means that we want to install this package globally. 
        - We want to install this package globally because we want to use it from the command line.

    - It install `babel` as well.

2. `npm init -y` : create a new package.json file with default settings. 
    - package.json is a file that contains information about our project.

3. `npm run build` : run the build script.
    - `npm run` is a command that allows us to run any script that we define in our package.json file.
    - `build` is the name of the script that we want to run.
    - `build` is a convention. We can use any name we want.


> Do `webpack -w` to watch the changes in the file. It will automatically recompile the code when we make changes to the file.
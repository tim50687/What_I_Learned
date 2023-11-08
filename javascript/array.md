# Array

- `const` does not stop us from modifying the content of array.

## Adding elements

- `push` : add to the end of array

```javascript
number.push(5,6);
```

- `unshift` : add to the beginning of array

- `splice` : add to the middle of array

```javascript
numbers.splice(2, 0, 'a', 'b');

// second argument is delete count -> how many element you wanna delete
```

## Finding elements (Primitives)

```javascript
const numbers = [1,2,3,4,1];
numbers.indexOf('a'); // -1
numbers.indexOf(1); // 0

numbers.lastIndexOf(1); // 4
```

- `includes` : return true or false, if the element is in the array

```javascript
numbers.includes(1); // true
```

## Finding elements (Reference Type)

```javascript
const courses = [
    { id: 1, name: 'a'},
    { id: 2, name: 'b'}
];

courses.includes({ id: 1, name: 'a'}); // false
// This is because these are two different objects in memory
```

- Therefore, we use `find` method

```javascript
const course = courses.find(function(course) {
    return course.name === 'a';
});

console.log(course); // { id: 1, name: 'a'}

const course = courses.findIndex(function(course) {
    return course.name === 'a';
});

console.log(course); // 0

```

## Arrow Function

```javascript
const course = courses.find(course => {
    return courses.name === 'a';
});

// if there is only one parameter, we can remove the parenthesis

// if no parameter, we need to have parenthesis
```

## Remove elements

- `pop` : remove the last element

```javascript
const last = numbers.pop();
```

- `shift` : remove the first element

```javascript
const first = numbers.shift();
```

- `splice` : remove elements in the middle

```javascript
const middle = numbers.splice(2, 1);
```

## Emptying an array

Remove all the elements in the array

```javascript
let numbers = [1,2,3,4];
// sol 1
numbers = [];

// sol 2 ** recommended
numbers.length = 0;

// sol 3
numbers.splice(0, numbers.length);

// sol 4
while (numbers.length > 0) {
    numbers.pop();
}

```

## Combining and slicing arrays

- `concat` : combine two arrays

```javascript
const first = [1,2,3];
const second = [4,5,6];

const combined = first.concat(second); // return new array
```

- `slice` : slice the array

```javascript
const slice = combined.slice(2, 4); // return new array
// 3, 4
const slice = combined.slice(2);
// 3, 4, 5, 6
```

> Concat and Slice, if primitive type, it will `copy` the `value`, if reference type, it will `point` the `reference`.

### The spread operator

```javascript
const combined = [...first, ...second];
// [1,2,3,4,5,6]
// we can also add element in the middle
const combined = [...first, 'a', ...second, 'b'];


// if call slice, it will return copy of array
const copy = [...combined];
```

## Iterating an array

```javascript
const numbers = [1,2,3];
for (let number of numbers) {
    console.log(number);
}

numbers.forEach(function(number) {
    console.log(number);
});

// we can also get the index by using second parameter
numbers.forEach(function(number, index) {
    console.log(index, number);
});

```

## Joining arrays

```javascript
const numbers = [1,2,3];
numbers.join(',');
// "1,2,3"
```

## Splitting strings

```javascript
const message = 'This is my first message';
message.split(' ');
// ["This", "is", "my", "first", "message"]
```

## Sorting arrays

```javascript
const numbers = [2,3,1];
numbers.sort(); // no return
// [1,2,3]

numbers.reverse(); // no return
// [3,2,1]
```

### If we want to sort object

```javascript
const courses = [
    { id: 1, name: 'Node.js'},
    { id: 2, name: 'javaScript'}
];

courses.sort(function(a, b) {
    // a < b => -1
    // a > b => 1
    // a === b => 0
    const nameA = a.name.toUpperCase();
    const nameB = b.name.toUpperCase();

    if (nameA < nameB) return -1;
    if (nameA > nameB) return 1;
    return 0;
});

```

## Testing the elements of an array

```javascript
const numbers = [1,2,3];

numbers.every(function(value) {
    return value >= 0;
}); // true



numbers.some(function(value) {
    return value >= 2;
}); // true
```


## Filter an array

```javascript
const numbers = [1,-1,2,3];

numbers.filter(function(value) {
    return value >= 0;
}); // [1,2,3]
```

## Mapping an array

```javascript
const numbers = [1,-1,2,3];

const filtered = numbers.filter(function(value) {
    return value >= 0;
}); // [1,2,3]

const items = filtered.map(function(value) {
    return '<li>' + value + '</li>';
});

// we want to put them in the ul element

const html = '<ul>' + items.join("") + '</ul>';


// we can also map it into object
const items = filtered.map(function(n) {
    return { value: n };
});

// we can also use arrow function, we need to add parenthesis around the object, so that hs engine will not think it is a code block
const items = filtered.map(n => ({ value: n }););
```

### Both filter and map return new array

- They are chainable

```javascript
const numbers = [1,-1,2,3];

const items = numbers
    .filter(n => n >= 0)
    .map(n => ({ value: n }))
    .filter(obj => obj.value > 1)
    .map(obj => obj.value);
```

## Reducing an array

```javascript
const numbers = [1,-1,2,3];

let sum = 0;

for (let n of numbers) {
    sum += n;
}

// we can use reduce method
// reduce method reduces all the elements in the array into one value
// first argument is a callback function
// second argument is the initial value of accumulator

const sum = numbers.reduce((accumulator, currentValue) => {
    return accumulator + currentValue;
}, 0);

// If we don't set second argument, it will be the first element of the array

// we can also use arrow function
const sum = numbers.reduce(
    (accumulator, currentValue) => accumulator + currentValue
);

```
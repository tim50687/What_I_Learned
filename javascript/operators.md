# Operators


## Increment and Decrement

```javascript
let x = 10;
console.log(++x); // console will log 11
console.log(x++); // console will log 11
```

```javascript
let x = 10;
let y = x++;
console.log(y); // 10
console.log(x); // 11
```

## Equality Operators

### Strict Equality (Type + Value)
```javascript
console.log(1 === 1); // console will log true
console.log('1' !== 1); // console will log True
```

### Lose Equality (Value)

- It will convert the type of the right operand to the type of the left operand and then compare the values.
```javascript
console.log(1 == 1); // console will log true
console.log('1' != 1); // console will log false
```

## Ternary Operator

```javascript
let x = 110;
let type = x >= 110 ? "Gold" : "silver";

console.log(type); // Gold
```

## Logical Operators

### Logical AND (&&)

### Logical OR (||)

### Logical NOT (!)

## Logical Operators with Non-booleans

### Falsy (false) // kinda like false
- undefined
- null
- 0
- false
- ''
- NaN

### Truthy (true) // Anything that is not Falsy

- short-circuiting
    - It doesn't matter how many operands you have, it will stop evaluating as soon as it finds the first truthy value.
```javascript
false || 1 || 1 // return 1
```

- Use case

```javascript
let userColor = '';
let defaultColor = 'blue';
let currentColor = userColor || defaultColor;
console.log(currentColor);
```

## Bitwise Operators

- Bitwise operators treat their operands as a sequence of 32 bits (zeroes and ones), rather than as decimal, hexadecimal, or octal numbers. For example, the decimal number nine has a binary representation of 1001. Bitwise operators perform their operations on such binary representations, but they return standard JavaScript numerical values.

### Bitwise AND (&)

```javascript
console.log(1 & 2); // 0001 & 0010 = 0000
```

### Bitwise OR (|)
```javascript
console.log(1 | 2); // 0001 | 0010 = 0011
```

### Read, Write, Execute

```javascript
// 00000100 Read
// 00000010 Write
// 00000001 Execute

const readPermission = 4; // decimal representation
const writePermission = 2;
const executePermission = 1;

let myPermission = 0;
myPermission = myPermission | readPermission | writePermission;
```
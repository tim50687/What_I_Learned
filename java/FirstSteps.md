# First Step

## JShell

JShell is a Read-Eval-Print Loop (REPL) tool introduced in Java 9. It is a command line tool that can be used to execute Java code and get immediate results. It is a great tool for learning Java and prototyping Java code.

- it `reads` the command or code segment we type in.

- it `evaluates` the code we type in.

- it `prints` the result of the evaluation.

- it `loops` back to step 1.

## Expressions

An expression is a combination of values, variables, operators, and method calls that evaluates to a single value. The value can be a number, a string, or a boolean value. For example, `1 + 2` is an expression that evaluates to `3`. `1 + 2` is an expression that evaluates to `3`. `"Hello"` is an expression that evaluates to a string value `"Hello"`. `true` is an expression that evaluates to a boolean value `true`.

## int

In java, by default, any whole number literal without a decimal point is treated as an `int` data type.

## L suffix

Using the `L` suffix to specify a `long` literal, as in `long num = 100L;`, provides a clear and unambiguous way to indicate that the value should be treated as a `long` data type rather than an `int`. There are several benefits to doing this:

1. Avoiding Data Loss: If you assign a large integer value to a `long` variable without the `L` suffix, the compiler might treat it as an `int`, and if the value exceeds the range of `int`, you'll lose data or encounter unexpected results. Using the `L` suffix ensures that large values are correctly assigned to a `long`.

2. Code Clarity: The `L` suffix makes your code more explicit and easier to understand for both yourself and other programmers. It clearly indicates your intention to use a `long` data type, reducing the chances of misunderstandings or bugs.

3. Conformance to Coding Standards: Some coding standards and guidelines recommend always using the `L` suffix when working with `long` literals for consistency and code readability.

Here's an example to illustrate the potential issue without the `L` suffix:

```java
// Without L suffix, might cause an error or unexpected behavior
long largeNum = 10000000000; // Error or unexpected behavior

// With L suffix, explicitly indicates a long literal
long largeNumWithL = 10000000000L; // Correct, explicitly a long
```

In the first line, without the `L` suffix, the value `10000000000` may be treated as an `int`, resulting in a compilation error or unexpected behavior. In the second line, using the `L` suffix makes it clear that you intend to use a `long`, and the code will work as expected.

## Float and Double

- The `double` is default floating-point data type in Java. If you write a floating-point literal without a suffix, it will be treated as a `double` data type.

## Char

A char occupies 16 bits of memory and can store any character from the Unicode character set. Java is using Unicode behind the scenes to represent and handle character.

You can use single quotes and a character literal to assign a value to a char, which is much simpler than looking up the representative number.


## Compound Assignment Operators

x -= y

is really

x = (data type of x) (x - y)

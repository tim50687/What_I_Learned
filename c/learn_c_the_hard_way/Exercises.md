# Exercises note


## Exercise 3

### Escape Sequences

Escape sequences are used to represent certain special characters within string literals and character literals. They are also used to represent certain hard-to-type characters.

| Escape | What it does. |
| ------ | ------------- |
| \\\ | Backslash (\) |
| \\' | Single-quote (') |
| \\" | Double-quote (") |
| \a | ASCII bell (BEL) |
| \b | ASCII backspace (BS) |
| \f | ASCII formfeed (FF) |
| \n | ASCII linefeed (LF) |
| \r | ASCII carriage return (CR) |
| \t | ASCII horizontal tab (TAB) |
| \v | ASCII vertical tab (VT) |
| \ooo | ASCII character with octal value ooo |
| \xhh | ASCII character with hex value hh |

- `\r`: moves the cursor back to the beginning of the current line.

#### Undefined behavior

```c
int age;
int height = 72;

printf("I am %d years old.\n", age);
```

> This leads to undefined behavior, as the value of `age` is indeterminate. The output can be any random number, depending on what data was previously in the memory location used for `age`.


## Exercises 4: debugging

- `-g`: adds debugging information to the executable file.


### Common commands

- `run`: launches the program.

- `target create`: the debugger initializes a new debugging session with ex3 as the target program. This means LLDB loads the program and makes it ready for debugging but does not start executing it yet.

- `b` : sets a breakpoint at the specified line.

- `s`: steps into the next line of code.

- `n`: next line, but step over function calls.

- `bt`: backtrace, shows the stack of function calls that got us to this point in the program. (`read it from the bottom up`).


## Exercise 7: Variables and Types

- `%e`: prints a floating-point number in scientific notation.

- `%%`: prints a literal percent character.

- `\0`: is 0 in integer, but is the null character in character.

You can do `math operation on int and char`, C implicitly converts char to int. `To C, a character is just an integer`. It's a really smaill integer.


## Exercise 10: switch statement

- Variable expressions are not allowed in case labels. `Although macros are allowed.`

- Float value is not allowed as a constant value in case label.

- ONly those expressions are allowed in switch which results in an integral constant value.

## Exercise 11: Array and Strings

- `int numbers[4] = {1};` : if you don't initialize all the elements, the rest of the elements will be initialized to 0.

## Exercise 12: Sizes and Arrays

The size of char is `always` 1 byte in C. 

- `char name[] = "Zed"` : the size of the array is 4, because the string "Zed" has 4 characters, including the null byte.

## Exercise 13: For Loops and Arrays of Strings

You can loop through the string by:

```c
for (int i = 0; argv[1][i] != '\0'; i++) // cool!!!!!
    {
        char letter = argv[1][i];

        switch (letter)
        {
        case 'a':
        case 'A':
            printf("%d: 'A'\n", i);
            break;
        case 'e':
        case 'E':
            printf("%d: 'E'\n", i);
            break;
        case 'i':
        case 'I':
            printf("%d: 'I'\n", i);
            break;
        case 'o':
        case 'O':
            printf("%d: 'O'\n", i);
            break;
        case 'u':
        case 'U':
            printf("%d: 'U'\n", i);
            break;
        default:
            printf("%d: %c is not a vowel\n", i, letter);
        }
    }
```
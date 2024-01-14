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
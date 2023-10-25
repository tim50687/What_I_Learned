# 5008 Review

## Head First C

The C language is designed to create small, fast programs. It's lower level than most other languages; **that means it creates code that's a lot closer to what machines really understand**.

## Main()

The computer will start running your program from the `main()` function. **Why the return type of int?** When the computer runs your program, it needs to have some way of deciding if the program ran successfully or not.
- Returning `0` means that the program was successful.
- Returning any other value indicates that there was a problem.

### Questions:

- **Why do I have to prefix the program with "./" when I run it on Linux and the Mac?**  
On Unix-style operating systems, programs are only run if you specify the directory where they live or if their directory is listed in the PATH environment variable.

- **For C, s = "Tim" is just an array of separate characters: {"T", "i", "m"}**  
This is why you can refer to the individual characters in the string by using an index. Each character in the string is just an element in an array.

- **Does it matter if I use single quotes or double quotes?**  
Yes. Single quotes are for `individual character`s, while `double quotes` are always used for strings.

- **Why does it need a sentinel character?**  
C-style strings are null-terminated, which means they end with a null character. If you're using an array for other purposes, such as storing numerical data, then you may not need a sentinel character.

- **What the heck is a bus error?**  
A bus error means that your program cannot update that piece of memory.

- **Literal String and Character Array**
```c
char *ptr = "string literal";
char b[] = "string2";
```
  - Literal strings are defined by enclosing a sequence of characters in double quotes (" "). They're stored in a read-only memory segment, cannot be modified, are automatically null-terminated, and can be concatenated at compile time.
  - Character arrays are defined by specifying the array type and size, then initializing the array with characters. They can be modified, may or may not be null-terminated, and require functions like `strcat()` to concatenate.

> **Note:** In `char str2[] = "Hello World!";`, `str2` is a character array initialized with the string "Hello World!". Since it's a character array, it's stored in stack memory and can be modified. Meanwhile, `char str[] = "Hello World!";` allocates memory and copies the string "Hello World!" into it, so modifying it is valid. It's also more memory efficient and readable.

- **When you set a pointer to a string literal, you're actually setting it to the address of the string's first character in memory.**

## Boolean

In C, boolean values are represented by numbers. For C, the number `0` is the value for false. Anything not equal to `0` is treated as true.

## Scanf
```c
char str[10];
scanf("%2s", str);
```
Since `str` is a character array, it's equivalent to `&str[0]`, which is the memory address of the array's first element.



## Pointer

<p align = "center">
<img src = "images/pointer_example.jpeg" style = "width:500; border:0">
</p>

In this code where is array stored and where is &array stored?

The pointer variable `array` itself is stored on the stack because it's a local variable of the function. However, it points to a memory location on the heap where the actual `Array` structure is allocated using `malloc()`.

- `&array` is stored on the stack

- `data[0]` refers to the `first` element of the array named `data`.


```c
int numbers[3] = {1,2,3};
printf("%p\n", numbers + 1); // Get the address of second element
```

- `numbers` is an array of integers. When used in an expression, the name `numbers` decays to a pointer to the first element of the array.
- `numbers + 1` increments the pointer by the size of one `int`, effectively pointing to the second element of the array.
- `printf("%p\n", numbers + 1);` will print the address of the second element of the `numbers` array.

### Access Structure Members

1. **Dot Operator (.)**: If you have an instance of a structure (not a pointer), you use the dot operator `.` to access its members.
   ```c
   struct Point {
       int x;
       int y;
   };

   struct Point p;
   p.x = 10;
   p.y = 20;
   ```

2. **Arrow Operator (->)**: If you have a pointer to a structure, you use the arrow operator `->` to access its members.
   ```c
   struct Point {
       int x;
       int y;
   };

   struct Point *ptr = (struct Point *)malloc(sizeof(struct Point));
   ptr->x = 10;
   ptr->y = 20;
   ```

In the above example, `ptr` is a pointer to a `Point` structure. To access the `x` and `y` members of the structure that `ptr` points to, you use the `->` operator.

Essentially, `ptr->x` is a shorthand for `(*ptr).x`. The arrow operator `->` dereferences the pointer and then accesses the member, all in one step.

> Note: It’s a good practice to check if the pointer return by malloc is NULL everytime.

### Structure in C: Direct Usage v.s. Pointer Usage

1. **Using Structures Directly**:
   - Structures can be assigned by value, copying all data from the source to the destination.
   - Efficient for small structures but can be time-consuming for larger ones due to data copying.
   ```c
   struct abc instance1, instance2;
   instance1.field = 42;
   instance2 = instance1;
   ```

2. **Using Pointers to Structures**:
   - Work with addresses, not the data directly, making assignments and function calls more efficient.
   - Allows for dynamic memory allocation and runtime memory adjustments.
   - Changes made through pointers in functions reflect in the original structure.
   ```c
   struct abc instance;
   struct abc *ptr = &instance;
   ```

3. **Advantages of Pointers**:
   - Memory and time-efficient, especially for large structures.
   - Provide flexibility in memory management and function operations.
   - Analogous to the difference between using `int` and `int *`.

### Will OR statement check all criteria in C?

If the first condition is true, the computer won't be bother to check the second condition.


### Execution of C program
 **Execution**:
   - When you run the executable, the operating system loads it into RAM.
   - The program's entry point, usually the `main()` function, starts executing.
   - As the program runs:
     - Local variables of functions are allocated on the `stack`.
     - Dynamic memory allocations (using `malloc()`, `calloc()`, etc.) are made on the `heap`.
     - The program may read/write data, interact with the user, access files, etc.
   - The stack grows and shrinks as functions are called and return. If the stack grows too much (e.g., due to deep recursion), it can lead to a stack overflow.
   - The heap is used for dynamic memory allocation and deallocation. Improper management of heap memory can lead to memory leaks or other issues.

## int main()

### int main(int argc, char *argv[]) {}
The int argc is a parameter that represents the number of arguments passed to the program when it is run from the command line. char *argv[] is an array of character pointers that holds the arguments passed to the program.

For example, if you run a program called "myprogram" with the command ./myprogram arg1 arg2 arg3 then argc will be 4 and argv[0] will be "myprogram", argv[1] will be "arg1", argv[2] will be "arg2" and argv[3] will be "arg3"

## Stream

### What is a stream?

[good website](http://websites.umich.edu/~eecs381/handouts/basicCio.pdf)

A stream is a popular concept for how to do input/output. Basically, a stream is a sequence of characters with functions to take characters out of one end, and put characters into the other end. In the case of input/output streams, one end of the stream is connected to a physical I/O device such as a keyboard or display. If it is a console output stream, your program puts characters into one end of the stream, and the display system takes characters out of the other and puts them on the screen. If it is a console input stream, the 
keyboard puts characters into one end of the stream, and your program takes characters out of the other and stores the results in variables in the program. If no characters are waiting in the input stream, your program must wait until you supply some by typing on the keyboard. File streams follow the same principle, except that the file system is attached to the other end of the stream.
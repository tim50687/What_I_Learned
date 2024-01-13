# Using Make
[good video](https://www.youtube.com/watch?v=GExnnTaBELk)
## What is Make?

How make works is you declare dependencies, and the describe how to build them or rely on the program's internal knowledge of how to build most common software. Make is a tool which controls the generation of executables and other non-source files of a program from the program's source files.

## Exercise 1

When you type `make ex1` in the terminal, you are invoking the `make` command to build a target named `ex1`. The `make` command looks for a file named `Makefile` or `makefile` in the current directory. This file contains rules that tell `make` how to build targets.

If you don't have a `Makefile` (or `makefile`) in your directory, or if the `Makefile` doesn't have a rule for `ex1`, `make` has a set of implicit rules it can use. One of these implicit rules is for building C programs.

Here's what happens step by step:

1. You type `make ex1`.
2. `make` looks for a rule to build `ex1`.
3. If `make` doesn't find a specific rule for `ex1` in the `Makefile`, it uses an implicit rule to compile C programs.
4. The implicit rule for C programs is something like: `cc -o target target.c`. In your case, the target is `ex1`, so `make` runs the command `cc ex1.c -o ex1`.
5. The `cc` command is a common alias for the system's C compiler (often GCC or Clang). The `-o ex1` option tells the compiler to output the compiled program to a file named `ex1`.
6. After this command runs, you should have an executable file named `ex1` in your directory.

In summary, when you typed `make ex1`, you told `make` to compile `ex1.c` into an executable named `ex1` using the system's C compiler. The output `cc ex1.c -o ex1` is just `make` showing you the command it executed to do this.


### Track


**Note on `make` and File Timestamps**

- **Primary Function**: `make` determines whether to rebuild a target based on file timestamps.
  
- **Timestamps Checked**:
  1. **Modification Timestamp**: Indicates the last time a file was changed. This is the primary timestamp `make` relies on.
  2. **Creation Timestamp**: Shows when the file was created. Less relevant for `make`.
  
- **Rebuild Decision**: When comparing a target and its dependencies:
  - If any dependency has a more recent modification timestamp than the target, `make` will rebuild the target.


> If just type make, make will build the first target in the makefile. In this case, it will build ex1. If you want to build a specific target, you can type make ex1. If you want to build all targets, you can type make all.

> `all` is a special target. It is the default target if you just type make. It can build every target you list as a dependency. In this case, it builds ex1 and ex3.


- If I don't have the dependency, try going down the tree and see if you can build it. 

- If you have the dependency, check the timestamp. If the dependency is newer than the target, then rebuild the target. If the target is newer than the dependency, then don't rebuild the target.
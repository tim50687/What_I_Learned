# Key Word 

## `file descriptior`:

In simple words, when you open a file, the operating system creates an entry to represent that file and store the information about that opened file. So if there are 100 files opened in your OS then there will be 100 entries in OS (somewhere in kernel). These entries are represented by integers like (...100, 101, 102....). This entry number is the file descriptor. So it is just an integer number that uniquely represents an opened file for the process. If your process opens 10 files then your Process table will have 10 entries for file descriptors.

Similarly, when you open a network socket, it is also represented by an integer and it is called Socket Descriptor. I hope you understand.

## `$?`
    
The exit status of the last command executed.

```bash
echo $?
```


1. **Exit Status Value Conversion:**
- When a program exits, it can return an exit status value. This value is limited to 8 bits (0-255).
- If you provide an exit status value outside of this range (like 231312), the value wraps around modulo 256. So 231312 modulo 256 is 144, which is why you see 144 as the exit status.

2. **$? Variable:**
- In Unix-like systems, the `$?` variable holds the exit status of the last executed command or program. When you run `echo $?`, it prints the exit status of the previously executed command.
- After you ran `./shell56` and then `exit 231312`, the shell returned an exit status of 144 (as explained in the first point).
- When you subsequently ran `echo $?`, it displayed the exit status of the previous command, which was 144.
- Finally, when you ran `echo $?` again, it displayed the exit status of the `echo` command itself, which was 0 because `echo` successfully printed the value.

## `ls`:

**Understanding the Behavior of the `ls` Command**

The `ls` command in Unix-like operating systems is used to list files and directories. Its output format adjusts based on where its output is being sent:

1. **Direct Terminal Output:** 
   When you run `ls` directly in a terminal, it detects that its output is connected to a terminal screen. In this scenario, `ls` often displays its output in columns, making it user-friendly and easier to read.

2. **Command Substitution or Redirection:** 
   When the output of `ls` is captured by command substitution (e.g., `$(ls)`) or redirected to a file or another command, `ls` defaults to listing filenames one per line.

   For instance, in the command:
   ```bash
   echo $(ls)
   ```
   The `ls` command lists filenames one per line, but then those filenames (including newlines) become arguments to the `echo` command. As a result, the newlines are replaced by spaces, giving a single-line output.

3. **Forcing Single-Line Output:** 
   If you always want `ls` to list one file per line, regardless of the output destination, you can use the `-1` option:
   ```bash
   ls -1
   ```
   This ensures a single file is listed per line.

## `$(...)`:

## Command Substitution: `$(...)`

In this mechanism, the output of a command replaces the command itself.

Command substitution allows us to run a command and use its output in another context, whether in an assignment or as an argument to another command.

### Example 1:
Let's capture the output of `ls -1` (which lists files one per line) and assign it to a variable:
```bash
output=$(ls -1)
```
The variable `$output` now contains the names of the files, with each file name on a separate line.

If we echo this variable *with quotes*, it will respect the newlines:
```bash
echo "$output"
```
This will print each file on its own line.

### Example 2:
However, if we use the command substitution directly as an argument to another command *without quotes*, things change:
```bash
echo $(ls -1)
```
This will print all the files on a single line, separated by spaces. Why? Because the shell, by default, splits arguments on whitespace (spaces, tabs, and newlines). So, each file name becomes a separate argument to `echo`, and `echo` prints them all separated by spaces.

#### The Role of Double Quotes:

**Preserving White Spaces**: Without double quotes, the shell interprets whitespace (spaces, tabs, and newlines) as argument delimiters. By surrounding a string or command substitution with double quotes, we're instructing the shell to treat the content as a single argument, even if it contains whitespace.

   - Without quotes:
     ```bash
     echo $(ls -1)
     ```
     Here, each file/directory returned by `ls -1` is treated as a separate argument to `echo`, and `echo` prints them separated by spaces.

   - With quotes:
     ```bash
     echo "$(ls -1)"
     ```
     In this case, the entire output of `ls -1` (including all newlines) is treated as a single argument. Thus, `echo` prints the files/directories each on a separate line, respecting the newlines.


# Function

## `isatty()`: 
- check if the file descriptor is associated with a terminal device.

Further investigation would lead you to the discovery that file descriptors 0, 1 and 2 (aka STDIN_FILENO, STDOUT_FILENO and STDERR_FILENO) are by convention set up to point to your terminal when your program is running from a terminal.

---

When you run `./shell`, your program reads input from the terminal in an interactive mode, which means it continuously waits for the user to type commands, process them, and then wait again for the next command.
However, when you use `echo ls | strace -f ./shell`, you're piping the output of `echo ls` (which is just the string "ls") into the `./shell` program. This means the standard input (`stdin`) for `./shell` is no longer your keyboard in an interactive session. Instead, its input becomes the output of the `echo` command, which is the string "ls". 

Here's a step-by-step breakdown:

1. `echo ls` sends the string "ls" to its standard output.
2. The `|` (pipe) sends this string "ls" to `./shell` as its standard input.
3. `./shell` reads "ls" as a command, processes it, and then looks for the next input.
4. Since there's no more input (the `echo ls` command only provided "ls" and nothing more), an End-Of-File (EOF) condition is encountered on the standard input of `./shell`.
5. When your shell encounters EOF (which would be equivalent to pressing `CTRL+D` in an interactive session), it terminates as per the logic in the `if (!fgets(line, sizeof(line), fp)) break;` line in your program.

When you're running in interactive mode, you don't encounter EOF until you explicitly signal it (usually with `CTRL+D`), or you close the terminal. But when piping input into your shell, EOF is encountered as soon as the piped input is consumed.

This behavior is typical of Unix-like shells and utilities. It allows for flexibility in using tools both interactively and in a scripted or batch-processing manner.

### stdin

1. **Terminal Session**: When you open a terminal (or command line interface) on your computer, you're starting a new terminal session. This session allows you to interact with the operating system by typing commands and viewing their output.

2. **File Descriptor**: In Unix-like operating systems, everything is treated as a file – devices, sockets, regular files, etc. A file descriptor is a unique identifier (usually a non-negative integer) that the system uses to access and manage these files. When you read from or write to files, you're essentially reading from or writing to file descriptors.

3. **Standard Input (`stdin`)**: This is the primary mechanism through which a program receives input data. By default, `stdin` is connected to the keyboard. So when a program reads from `stdin`, it's reading what you type into the terminal. 

4. **Inheriting the File Descriptor**: When you run a program from the terminal (like `./shell56`), that program becomes a child process of the terminal. The child process (your program) inherits certain attributes from the parent process (the terminal). One of these attributes is where its `stdin` points to. So, when you run your program, its `stdin` is automatically set to the same source as the terminal's `stdin`, which is the keyboard. 

5. **Refers to the Terminal**: Saying that `stdin` "refers to the terminal" means that the input source for the program is the terminal itself. So, when the program wants to read some input, it'll take whatever is typed into the terminal.

So, to tie it all together: When you run your program (`./shell56`) directly from the terminal, the operating system sets up your program's `stdin` to get input from the terminal. This is why, in a typical scenario, you can directly type input into your program right from the terminal. The reason this setup works seamlessly is due to the inherited file descriptor pointing to the terminal session.

## `fflush()`: 
- flush a stream

If stream points to an output stream or an update stream in which the most recent operation was not input, the fflush function causes any unwritten data for that stream to be delivered to the host environment to be written to the file; otherwise, the behavior is undefined.

- The `stdout stream` is line buffered by default, so will only display what's in the buffer after it reaches a newline (or when it's told to).

## `fgets()`:

`fgets()` is designed to read a line of input from a stream until either:

1. A newline character (`\n`) is encountered.
2. The specified size minus one (for the null terminator) characters have been read.
3. The end-of-file (EOF) is reached.

> fgets() reads from the argument stream. If this stream is tied to a device or a pipe, it blocks until input is obtained from the device/pipe or until an end of file is detected.



### 1. User Interaction with Terminal:
Imagine you have an open terminal on your computer. When you type on your keyboard, the terminal application receives those keystrokes.

### 2. Terminal Buffers:
The terminal maintains a buffer of characters. When you type, the characters go into this buffer but aren't immediately sent to the underlying program. This allows for functionalities like backspacing to correct mistakes.

### 3. The Enter Key:
When you press the Enter key (or Return, depending on your keyboard), the terminal sends the content of this buffer as a line of input to the underlying program. This is typically sent to the program's `stdin`.

### 4. The `stdin` Stream:
The `stdin` (standard input) is a stream that provides input to a program. By default, when a program is run from the terminal, its `stdin` is connected to the terminal. This means that when you type something and press Enter, the data you typed becomes available on the program's `stdin` stream.

### 5. `fgets()` Function:
The `fgets()` function is a C library function that reads from a specified stream. When you use `fgets()` to read from `stdin`, it waits (or "blocks") for input to be available on `stdin`.

In the context of our example:

```c
char buffer[256];
fgets(buffer, sizeof(buffer), stdin);
```

The `fgets()` function will block and wait for user input. Once the user types something into the terminal and hits Enter:

- The terminal sends that input to the program's `stdin`.
- `fgets()` reads from `stdin` and stores the input in the `buffer`.
- Execution continues after the `fgets()` call.

### 6. End of File or Error:
If there's an end-of-file condition (for instance, if the input is being redirected from a file and the end of that file is reached) or an error occurs, `fgets()` will return a NULL pointer.

### To Summarize the Process:

1. **User Types**: You type "Hello, World!" in a terminal and hit Enter.
2. **Terminal Buffers**: The terminal takes "Hello, World!" and places it in its buffer.
3. **Terminal Sends to `stdin`**: Upon pressing Enter, the terminal sends "Hello, World!\n" to the `stdin` of the program running in the terminal.
4. **`fgets()` Reads**: If that program is using `fgets(buffer, sizeof(buffer), stdin);`, it will read "Hello, World!\n" from `stdin` into `buffer`.
5. **Program Continues**: Execution continues after the `fgets()` line in the program.

Remember that the behavior of "waiting until you hit Enter" is specific to terminal-based input. If `stdin` is reading from a file or another source, the behavior might differ.

## `sprintf()`:

The `sprintf()` function is a C library function that writes formatted data to a string. It's similar to `printf()`, except that it writes to a string instead of `stdout`.

```c
char buffer[50];
int a = 10, b = 20, c;
c = a + b;
sprintf(buffer, "Sum of %d and %d is %d", a, b, c);
```

## `dup2()`:

The `dup2()` function is a Unix system call that duplicates an existing file descriptor to another file descriptor. It's typically used to redirect `stdin` and `stdout` to files or other devices.

```c
dup2(int oldfd, int newfd)
```
closes newfd if it is already open, and makes a copy of oldfd numbered newfd. 
### Why is this necessary?

Using `dup2()` allows processes to change where their output goes (for writers) or where their input comes from (for readers). 

In the case of `ls | grep`:

- The `ls` command should have its output directed to the pipe instead of the terminal. Hence, we use `dup2()` to replace stdout for `ls` with the write end of the pipe.
  
- The `grep` command should take its input from the pipe instead of the keyboard. Hence, we use `dup2()` to replace stdin for `grep` with the read end of the pipe.

The `close()` calls are essential for two reasons:
1. Free up system resources.
2. Ensure that the pipe behaves correctly. For example, if the read end isn't closed, `grep` might hang waiting for more input because the pipe wouldn't send an EOF (end of file) signal.


## perror():

The `perror()` function in C is used to print a descriptive error message to the standard error output (stderr). It's typically used in conjunction with system calls and library functions that set the global variable `errno` on failure. Here's a detailed explanation:

### Purpose of `perror()`

- **Error Reporting**: When a system call or library function encounters an error, it often returns a specific value (like `-1`) and sets the global variable `errno` to indicate the type of error.
- **Contextual Information**: `perror()` uses the current value of `errno` to fetch a human-readable error message that describes the last error encountered.
- **Custom Prefix**: It takes a string as an argument, which is displayed as a prefix to the error message. This helps provide context about where or why the error occurred.

### How `perror()` is Used

- **Example Usage**:
   ```c
   int fd = open("non_existent_file.txt", O_RDONLY);
   if (fd == -1) {
       perror("Error opening file");
   }
   ```
- **In this Example**:
   - If the `open()` system call fails (for example, the file doesn't exist), it returns `-1` and sets `errno`.
   - `perror("Error opening file")` then outputs a message like "Error opening file: No such file or directory" to stderr.
   - The specific error message after the colon is determined by the value of `errno`.

### Why Use `perror()`

- **User-Friendly Error Messages**: Directly reading `errno` gives a numeric code, which isn't user-friendly. `perror()` translates this code into a message that is easier to understand.
- **Debugging Aid**: It's helpful for debugging, especially for system-level programming where interpreting `errno` values is common.
- **Standard Error Reporting**: It's a standard way in C to report errors that occur during system call or library function execution.

### Conclusion

`perror()` is a simple yet powerful function in C for reporting errors. By providing descriptive, human-readable error messages that are associated with the `errno` value set by system calls and library functions, it plays a crucial role in debugging and error handling in C programs.
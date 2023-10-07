# Key Word 

- `file descriptior`:

    In simple words, when you open a file, the operating system creates an entry to represent that file and store the information about that opened file. So if there are 100 files opened in your OS then there will be 100 entries in OS (somewhere in kernel). These entries are represented by integers like (...100, 101, 102....). This entry number is the file descriptor. So it is just an integer number that uniquely represents an opened file for the process. If your process opens 10 files then your Process table will have 10 entries for file descriptors.

    Similarly, when you open a network socket, it is also represented by an integer and it is called Socket Descriptor. I hope you understand.

- `$?`
    
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




# Function

- `isatty()`: check if the file descriptor is associated with a terminal device.

    Further investigation would lead you to the discovery that file descriptors 0, 1 and 2 (aka STDIN_FILENO, STDOUT_FILENO and STDERR_FILENO) are by convention set up to point to your terminal when your program is running from a terminal.

- `fflush()`: flush a stream

    If stream points to an output stream or an update stream in which the most recent operation was not input, the fflush function causes any unwritten data for that stream to be delivered to the host environment to be written to the file; otherwise, the behavior is undefined.

    - The `stdout stream` is line buffered by default, so will only display what's in the buffer after it reaches a newline (or when it's told to).
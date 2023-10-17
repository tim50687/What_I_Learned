# Understanding Unix Pipes

**1. Basic Concepts**:
- **File Descriptors**: Integer values serving as references or handles to system I/O resources. They're not the resources themselves but pointers to these resources.
  
- **Pipes**: A communication mechanism in Unix-like systems. When a pipe is created using `pipe(fd)`, a buffer (the actual pipe) is set up in the kernel space. 
  - `fd[0]`: File descriptor for the reading end of the pipe.
  - `fd[1]`: File descriptor for the writing end of the pipe.

- **Forking**: The `fork()` system call creates a child process as an almost exact copy of the parent. This includes the child having copies of the parent's file descriptors. But, these descriptors point to the same underlying resources.

**2. Analogy**:
Imagine a room (the pipe) with two doors: an entrance (write side) and an exit (read side). Two people (parent and child processes) each have a set of keys (file descriptors). Both sets of keys can open the same doors. Even though each person has separate keys, the doors they unlock are the same.

**3. Execution Flow**:
- Upon creating a pipe, you have two file descriptors: one for reading and one for writing.
  
- Post `fork()`, both the parent and child have their own sets of these descriptors. However, these descriptors point to the same underlying pipe.
  
- In the example, to facilitate smooth communication:
  - The child only writes to the pipe and closes its reading end.
  - The parent only reads from the pipe and closes its writing end.

**4. Importance of Closing Pipe Ends**:
- **Avoid Data Races**: Prevents unpredictable data intermixing when both processes try to write simultaneously.
  
- **Resource Management**: Every open file descriptor consumes kernel resources.
  
- **Signal End of Data**: Closing the write end signals the read end that no more data will be sent, indicating an end-of-file (EOF) condition.
  
- **Clarity in Code**: Designates clear roles for parent and child, simplifying debugging and maintenance.
  
- **Prevent Accidental Access**: Avoids accidental reads or writes to the wrong end.

## Why close the pipe

### Close Write

When you use a pipe, it creates two file descriptors: one for reading (read-end) and one for writing (write-end). A process reads from the read-end and writes to the write-end. The EOF is "sent" when the write-end is closed.

Consider a simple pipeline: `cmd1 | cmd2`

- `cmd1` writes data to the write-end.
- `cmd2` reads data from the read-end.

The crux is this: as long as the write-end of the pipe is open somewhere (in any process), the read-end won't receive an EOF. That's because the system doesn't know if more data might still be written to the pipe.

Here's where the confusion might arise with `dup2` and `fork`:

1. When you fork a child process, that child inherits all the open file descriptors of the parent. So, both parent and child have the write-end open.
  
2. If you use `dup2` in the child to redirect `stdout` to the write-end of the pipe, you essentially have two file descriptors pointing to the same write-end: the original from the pipe and `stdout` (typically file descriptor 1). This is a "copy" of sorts but both point to the same actual file description in the kernel.

3. Closing the write-end in the child after the `dup2` means you're ensuring that this child has no extra references to the write-end of the pipe. It will still write to this pipe via `stdout` (because of the redirection you did with `dup2`).

4. When `cmd1` completes its execution and exits, it automatically closes its `stdout`, which is the write-end of the pipe. This sends the EOF to `cmd2`.

5. But, if you didn't close the write-end in the child after the `dup2`, then even if `cmd1` finishes execution, that extra open write-end would prevent the EOF from being sent, because from the system's perspective, there's still a possibility that someone might write to the pipe.

So, the sequence is:

- `dup2` to redirect `stdout` of `cmd1` to the write-end.
- Close the original write-end file descriptor in `cmd1` (to avoid the problem explained above).
- When `cmd1` finishes and exits, it automatically closes its `stdout` (which is the redirected write-end of the pipe) -> EOF is sent to `cmd2`.

### Close Read

Consider again the pipeline: `cmd1 | cmd2`

- `cmd1` writes data to the write-end.
- `cmd2` reads data from the read-end.

When you fork to create the child process for `cmd1`, it inherits **both** the read and write ends of the pipe. However, `cmd1` only needs the write-end to send its output to `cmd2`. It has no use for the read-end.

Here are the reasons why you'd close the read-end in the `cmd1` process:

1. **Resource Efficiency**: Keeping file descriptors open unnecessarily can be wasteful. Each open file descriptor consumes a small amount of system resources. By closing the read-end in the `cmd1` process and the write-end in the `cmd2` process, you are ensuring efficient use of resources.

2. **Avoiding Accidental Reads/Writes**: If for some reason there's a bug or unexpected behavior in your code, having the read-end open in the `cmd1` process might lead to accidental reads from the pipe when you intended to read from somewhere else. Closing file descriptors that are not in use can prevent such unintended operations.

3. **Clarity and Conventions**: It's a good programming practice to close file descriptors you don't need. This makes the code's intent clearer to other developers and helps maintain conventions.

For the `cmd2` process:

- You close the write-end because `cmd2` only needs to read the output of `cmd1` from the read-end. It doesn't need to write anything into the pipe, so you close the write-end for similar reasons: efficiency, avoiding accidental writes, and clarity.

In summary, for each command in a pipeline:

- If it's a writing command (like `cmd1`), you close the read-end.
- If it's a reading command (like `cmd2`), you close the write-end.


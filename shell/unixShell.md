# Shell

[reference](https://indradhanush.github.io/blog/writing-a-unix-shell-part-1/)

## Introduction
**Terminal and Shell Behavior**

- **Terminal**: A terminal emulator application allows users to interact with the operating system. Examples include `gnome-terminal` on Linux, `Terminal` on macOS, and Command Prompt on Windows.

- **Shell**: When a terminal is opened, it typically starts a shell session automatically. A shell provides a user interface (either command-line based or graphical) to access the operating system's services.

**Understanding Shell Processes and Memory Management**

- **Shell as a Process**: The $\textcolor{cyan}{\text{shell}}$ itself is an active process. Its primary role is to wait for user input, like commands.

- **Child Process Execution**: When you type a command in the shell:
   - The shell spawns a $\textcolor{cyan}{\text{child process}}$ to handle most commands. This child process is responsible for executing the command and then terminating.
   - For instance, using the `ls` command in a Unix-like system creates a child process to list directory contents.

- **Built-in Commands**: Some commands are $\textcolor{cyan}{\text{built-in}}$ to the shell.
   - Commands like `cd` or `echo` might be executed within the shell's own process. These built-ins don't need a separate process since they're fundamental or lightweight.

- **Isolation and Error Handling**: Running commands as child processes provides $\textcolor{cyan}{\text{isolation}}$. If a command (child process) encounters an error:
   - The error is contained within that process.
   - The parent shell remains unaffected and can continue its operations.

- **Memory Management**:
   - Each process, be it parent or child, gets a $\textcolor{cyan}{\text{separate memory space}}$ allocated by the operating system.
   - Memory space separation ensures system $\textcolor{cyan}{\text{stability}}$ and $\textcolor{cyan}{\text{security}}$ by preventing unintentional or malicious interference.
   - Processes can communicate via $\textcolor{cyan}{\text{Inter-Process Communication (IPC)}}$ mechanisms such as pipes, sockets, and shared memory.
   - During the creation of a child process, especially with `fork()`, the child starts as a near-identical copy of the parent. However, this is a separate memory space (Copy-On-Write semantics), ensuring that changes in one process do not affect the other.

## Fork 

**Design Choice of `fork()` Returning `0` in the Child Process**

1. **Background**: The `fork()` system call in UNIX-based systems creates a new child process by duplicating the current (parent) process. After the `fork()`, both processes continue executing from the next instruction.

2. **Return Values**:
   - $\textcolor{cyan}{\text{Parent}}$: `fork()` returns the PID (Process ID) of the newly created child, a positive integer.
   - $\textcolor{cyan}{\text{Child}}$: `fork()` returns `0`, signaling it's the child process.
   - $\textcolor{cyan}{\text{Error}}$: `fork()` returns `-1` in the parent if there's an error in creating the child.

3. **Reasons for Design**:
   - $\textcolor{cyan}{\text{Clarity}}$: Returning `0` provides a direct and unambiguous indication that the code is running in the child process.
   - $\textcolor{cyan}{\text{Consistency}}$: Keeping the return type as an integer (whether positive, zero, or negative) maintains type consistency.
   - $\textcolor{cyan}{\text{Error Handling}}$: Distinct return values make error handling straightforward.

4. **Origin**: The design choice likely stems from the UNIX creators, Ken Thompson and Dennis Ritchie, reflecting the UNIX philosophy of simplicity and clarity.

**Summary**: The behavior of `fork()` returning `0` in the child is a design choice for clarity, consistency, and efficient error handling in differentiating processes post-fork.

## Sleep

### **`sleep()` System Call and Context Switching**

1. **Definition**: The `sleep()` function is a system call used to pause the execution of the current process for a specified duration.

2. **Role in Context Switching**:
   - When a process invokes $\textcolor{cyan}{\text{sleep()}}$, it signals to the kernel that it doesn't need the CPU for the specified duration.
   - The operating system updates the process's status to $\textcolor{cyan}{\text{blocked}}$ or $\textcolor{cyan}{\text{sleeping}}$, meaning it won't be considered for execution until its sleep duration ends.
   - The OS scheduler, recognizing that the sleeping process isn't utilizing the CPU, performs a $\textcolor{cyan}{\text{context switch}}$ to another "ready" process, ensuring efficient CPU utilization.
   - Post-sleep duration, the process is marked as "ready" and is considered for execution again by the OS scheduler.

3. **Importance**:
   - The `sleep()` function is an example of how a system call can lead to a context switch.
   - It illustrates the OS's ability to allocate CPU time efficiently, allowing other processes to run when one is in a waiting or blocked state.
   - Other system calls, especially I/O-bound calls, can also trigger similar context switches.

**Summary**: The `sleep()` system call pauses a process's execution, prompting the OS to perform a context switch to other ready processes, thereby optimizing CPU usage.


### **`sleep()` as a System Call**

1. **Definition**: The `sleep()` function is a system call used to suspend the execution of the calling process for a specified duration.

2. **Necessity of Kernel Interaction**:
   - **Process State Management**: `sleep()` requires the operating system to update the state of the process in the system's scheduling structures. This involves changing the process's state from "running" or "ready" to "blocked" or "sleeping".
   - **Timer Management**: To ensure the process resumes after the specified sleep duration, the operating system must manage hardware or software timers. This management often requires privileged operations only accessible in kernel mode.

3. **Protection and Isolation**: 
   - Directly managing process states and hardware timers in user space could risk system stability and security. By keeping `sleep()` in kernel mode, the OS ensures user processes can't inadvertently or maliciously disrupt system operations or other processes.

4. **Efficient CPU Utilization**: 
   - When a process invokes `sleep()`, it's indicating it doesn't need CPU resources for a while. This gives the OS scheduler an opportunity to allocate CPU time to other ready-to-run processes, optimizing overall system performance.

**Summary**: The `sleep()` function is a system call because it necessitates interactions with deep system-level structures and resources, specifically around `process scheduling` and `timer management`. Handling this in kernel mode ensures safety, stability, and efficient resource utilization.


### **System Calls and OS Security**

1. **Role of System Calls**: 
   - System calls serve as a gateway between user-space applications and the kernel, allowing access to more privileged operations.
   
2. **Limits on System Calls**:
   - System calls are not a free pass for unchecked actions. Applications looking to misuse system calls will encounter numerous $\textcolor{cyan}{\text{security checks and balances}}$ established by the operating system.

3. **Potential Vulnerabilities**:
   - Despite these safeguards, the implementation of system calls or kernel functions can have vulnerabilities.
   - Malicious actors can potentially exploit these vulnerabilities to gain unauthorized access or privileges.

4. **Importance of Updates**:
   - To counteract potential threats, it's crucial to regularly update and patch the operating system.
   - These updates address known vulnerabilities and continuously enhance the security mechanisms in place.

### **Concerns with Using `sleep()` for Process Control**

1. **Unpredictability**:
   - Relying on `sleep()` assumes a certain task or condition will be met within its duration. Due to factors like system load, I/O delays, or other unpredictable events, there's no guarantee the awaited task will complete within that time.

2. **Inefficiency**:
   - If the condition or task you're waiting for is satisfied earlier than the sleep duration, your process remains idle for the remainder, wasting potential CPU time and system resources.

3. **Potential Race Conditions**:
   - Using `sleep()` to handle synchronization can lead to race conditions, where the behavior of the program is inconsistent and depends on the timing of various events.

## Use waitpid() to wait for a child process

check 
```bash 
man waitpid
```
and ask chatgpt to explain it to you.

**Usage of `WUNTRACED` and `WNOHANG` with `waitpid()`**

1. **WUNTRACED**:
   - **Purpose**: Allows `waitpid()` to return when a child process is stopped, not just when it's terminated.
   - **When to Use**:
     - **Debugging**: Useful in scenarios where you want to monitor if a child process is stopped, often due to signals like `SIGTTIN`, `SIGTTOU`, `SIGTSTP`, or `SIGSTOP`.
     - **Process Monitoring**: If you have an application that needs to be aware of child processes' entire lifecycle, including pause points, `WUNTRACED` helps in capturing such state transitions.
     - **Job Control**: In shell implementations where you want to handle foreground and background jobs and need to be informed when a job is stopped.

2. **WNOHANG**:
   - **Purpose**: Modifies `waitpid()` to be non-blocking. If no child has terminated, it returns `0` immediately instead of blocking.
   - **When to Use**:
     - **Polling Mechanisms**: If you want to periodically check the status of child processes without getting blocked. Useful in event-driven programs or applications with a main loop that checks various conditions.
     - **Responsive Applications**: In scenarios where you don't want the main program or thread to hang waiting for child processes, ensuring the application remains responsive to other events or user input.
     - **Parallel Processing**: When managing multiple child processes and you want to efficiently check which ones have completed without getting stuck on a particular child.

**Summary**: 
- Use `WUNTRACED` when you need to capture both termination and stopping events of child processes.
- Use `WNOHANG` when you want to make non-blocking checks on child process statuses to keep the parent process or application responsive.

### **Interleaving (Jumbling) of Output in Concurrent Programming**

- **What is Interleaving?**
  Interleaving refers to the mixing or alternating of output from multiple concurrent processes or threads when they print to the same output medium, typically a terminal or console. 

- **Causes**:
  1. **Concurrency**: When parent and child processes (or multiple threads) run in parallel, they can produce output to the terminal simultaneously.
  2. **Output Buffering**: Most terminals or shells buffer the output. The flushing of these buffers to the display might not happen in the exact sequence the processes send the output.
  3. **Shell Prompt Timing**: Shells typically display their prompt once the foreground process completes. If background processes produce output after this, it can appear after the prompt, causing a jumbled appearance.

- **Common Scenarios**:
  Seen frequently in:
  - Multi-threaded applications.
  - Parent-child processes where both produce output, especially if child processes have delays (like `sleep`).
  - Event-driven programs where multiple events trigger output responses.

- **Potential Solutions**:
  - **Synchronization**: Use mechanisms like locks or semaphores to coordinate when each process or thread can produce output.
  - **Buffer Management**: Explicitly manage and flush output buffers to control the sequence of displayed output.
  - **Structured Logging**: Instead of direct output, log outputs to a file or system that can handle concurrent entries without jumbling.

**Summary**: Interleaving is a natural occurrence in concurrent programming when multiple entities share a common output medium. While often benign, it can sometimes lead to confusing output sequences, especially in diagnostic or logging scenarios. Awareness and certain mitigation strategies can help manage and understand interleaved outputs.

> Shell Behavior: Most shells are designed to display the prompt once the foreground process completes.  

## Exec in C

**Arrays, Strings, and Null Terminators in C**

- **Strings**:
  - When you define a string literal, the compiler automatically appends a null terminator (`'\0'`).
    ```c
    char str[] = "hello";  // Automatically becomes {'h', 'e', 'l', 'l', 'o', '\0'}
    ```
  - This null terminator indicates the end of the string.

- **Arrays of Pointers**:
  - Arrays of pointers (or strings) don't automatically receive a `NULL` terminator.
    ```c
    char *argv[] = {"ls", "-l", "-h", "-a"};  // No NULL at the end
    ```
  - For certain functions (e.g., the `exec` family), a terminating `NULL` is required to indicate the end of the array.
    ```c
    char *argv[] = {"ls", "-l", "-h", "-a", NULL};  // Explicit NULL at the end
    ```

- **Why Use `NULL` Terminator**:
  - In C, there's no inherent way to determine the length of an array.
  - Functions like those in the `exec` family rely on the `NULL` terminator to know where the array of arguments ends.
  - Not adding the `NULL` terminator can result in `undefined behavior`, as the function might read past the array.


### **`execvp` Function in C**

- **Description**:
  The `execvp` function is a member of the `exec` family of functions in C. It is used to execute a file, replacing the current process image with a new process image. 

- **Signature**:
  ```c
  int execvp(const char *file, char *const argv[]);
  ```


- **Parameters**:
  - `file`: The name of the file to be executed. If the name doesn't contain a slash (`/`), the `PATH` environment variable is used to locate the file.
  - `argv[]`: An array of pointers to strings passed as arguments to the program. The array must be terminated by a `NULL` pointer.

- **Behavior**:
  - Replaces the current process image with a new one.
  - Does not return on success. If the function does return, it indicates an error, and the return value is `-1`.
  - Uses the `PATH` environment variable to locate the file to be executed if the file name doesn't contain a directory path.

- **Example**:
  ```c
  char *argv[] = {"ls", "-l", NULL};
  execvp("ls", argv);
  ```

- **Important Notes**:
  - Always ensure that the `argv[]` array is terminated with a `NULL` pointer.
  - The `execvp` function doesn't create a new process. Instead, it replaces the current process image. To create a new process and then execute a file, you'd typically use `fork()` followed by `execvp`.
  - If `execvp` is successful, the program specified will start running and the code after the `execvp` call won't be executed in the original program. If there's an error (e.g., the specified program can't be found), `execvp` will return `-1`.
  - The process ID (PID) remains the same. 

**Summary**: `execvp` is a powerful function for executing programs from within a C application, replacing the current process image. Proper usage requires an understanding of process management and a careful construction of the `argv` array.

### strtok

**Static Pointer in `strtok()`**

- **Static Keyword in C**:
  - When a variable (or pointer) is declared as `static` in a function, it retains its value between successive calls to that function.
  - Such a variable is initialized only once. Afterward, it retains its last-assigned value across function calls.

- **`strtok()` and its Static Pointer**:
  - `strtok()` utilizes an internal static pointer to track its position in the string being tokenized.
  - On the initial call to `strtok()` with a string, the function locates the first token and returns it. The internal static pointer then sets its position just after this token.
  - For subsequent calls with `NULL` as the first argument, `strtok()` continues from the position of this internal static pointer, allowing it to tokenize the string piece by piece across multiple calls.
  - The static nature of this pointer means it remembers its position even after the function exits.

- **Implications**:
  - **Thread Safety**: The use of a shared static pointer means `strtok()` is not thread-safe. Concurrent calls in different threads can result in unexpected behavior. For thread-safe tokenization, consider using `strtok_r()`.
  - **Tokenizing Multiple Strings**: Interleaved calls to `strtok()` for different strings can disrupt the tokenization process due to the shared static pointer. It's advisable to complete tokenization for one string before starting on another.

**Summary**: The `strtok()` function employs an internal static pointer to maintain its state between calls. This allows the function to continue parsing the same string over multiple calls. While convenient, this approach presents limitations concerning thread safety and handling multiple strings simultaneously.

## Free Memory

**Memory Management in Forked Processes**

1. **Process Image Replacement**: When a child process runs `execvp()` (or similar functions), it replaces its current process image with a new one. This means the entire memory space of the child process, including any memory allocations, is substituted by the memory image of the new program.
 
2. **Memory Isolation**: `fork()` duplicates the parent's memory for the child, providing the child with its own separate memory space. Any modifications in the child's memory do not impact the parent's memory, and vice versa.

3. **Memory Cleanup**:
    - **Child Process**: If `execvp()` is used, memory cleanup in the child process isn't necessary because the process image (and its memory allocations) are discarded.
    - **Parent Process**: It's essential to free any dynamically allocated memory to prevent memory leaks. 

4. **Point to Remember**: Absent an `execvp()` call or similar in the child process, both the parent and child processes must handle their own memory management, meaning each would need to free any allocated memory independently.

## Error Handling

**errno**
- **Description**: `errno` is a global variable set by system calls and some library functions to indicate what went wrong. It's defined in `errno.h`.
- **Usage**: When a system call fails, it usually returns `-1` and sets the `errno` variable to a value representing the error. 
- **Note**: Since it's a global variable, its value can be overwritten by subsequent system calls that don't fail, so it's best to check its value immediately after the failure of a call.

**perror**
- **Description**: `perror` is a library function that prints a description for the last error that occurred.
- **Usage**: It's used to display a string you provide, followed by a colon, a space, and then the textual representation of the current `errno` value.
- **Example**: 
  ```c
  if (some_system_call() == -1) {
      perror("Description of what we were trying to do");
  }
  ```

**exit**
- **Description**: `exit` is a function to terminate a program. It's defined in `stdlib.h`.
- **Usage**: 
  - `exit(0)`: Generally indicates successful termination.
  - `exit(1)`, `exit(2)`, ...: Generally indicates termination due to an error. The specific non-zero value can be used to indicate different error reasons.
- **Note**: On program exit, it ensures that all I/O buffers are flushed, files are closed, and any atexit() registered functions are called.


## **Understanding Libraries in C Programming:**

1. **Standard Libraries**:
   - These are libraries that come bundled with most C compilers and provide the fundamental functionalities required for C programming.
   - Libraries such as `libc` contain implementations of the C Standard Library, which includes functions from headers like `stdio.h` and `stdlib.h`.
   - Because they are part of the standard, they're linked automatically by the compiler. This is why functions from `stdio.h` (e.g., `printf`, `scanf`) don't need any special linking instructions.
  
2. **External (or Non-standard) Libraries**:
   - These libraries provide additional functionalities beyond the standard library but aren't automatically linked by compilers.
   - An example is the `readline` library. Even if you include its header (`readline/readline.h`), you still need to link against it using the `-lreadline` option.
   - The need for explicit linking prevents unnecessary bloat in the final executable. If every library were automatically linked, a simple program could become large due to unneeded code.
  
When compiling C code, it's essential to know whether you're using standard or external libraries. For external libraries, ensure you provide the appropriate linking instructions.

## Use cd

**Changing the Current Working Directory in a Shell-Like Program**

In a shell-like program, you often need to handle changing the current working directory. The most common approach is to use the `chdir` system call directly within a custom `cd` function. Here's a simple implementation:

```c
#include <unistd.h>

int cd(char *path) {
    return chdir(path);
}
```

This function accepts a path as an argument and uses `chdir` to change the current working directory to the specified path. If successful, it returns 0, and if there's an error, it returns -1.

## Signal

**Understanding Signals in Unix-Like Operating Systems**

Signals are a fundamental concept in Unix-like operating systems, serving as a means of asynchronous communication between processes and the operating system. Here are key points to understand about signals:

1. **Purpose of Signals:**
   - Signals are notifications sent to processes to inform them of specific events or conditions, such as user actions or system events.
   - They facilitate inter-process communication, allowing processes to respond to external events.

2. **Signal Identification:**
   - Each signal is identified by an integer number (e.g., 1, 2) and often has a symbolic name (e.g., SIGINT for interrupt) defined in the system's signal header file.

3. **Signal Sources:**
   - Signals can be generated by various sources:
     - **User Actions:** User actions like pressing Ctrl-C can trigger signals (e.g., SIGINT).
     - **Operating System:** The operating system can send signals to processes for various reasons (e.g., termination, termination request).
     - **Other Processes:** One process can send a signal to another process to communicate or request specific actions.

4. **Signal Handling:**
   - Processes can define signal handlers, which are functions that respond to specific signals.
   - When a signal is received, the operating system invokes the corresponding signal handler, allowing the process to respond to the signal's event.

5. **Asynchronous Nature:**
   - Signals are asynchronous, meaning they can interrupt a process's execution at any point in time.
   - This asynchronicity can make signal handling challenging, as processes must be prepared to handle signals while in any state of execution.

6. **Common Signals:**
   - Some common signals include:
     - SIGINT (Ctrl-C): Sent to terminate a process or request interruption.
     - SIGTERM: Sent to request the termination of a process.
     - SIGKILL: Sent to forcefully terminate a process.
     - SIGSTOP and SIGCONT: Used to pause and resume processes, respectively.

7. **Custom Signal Handling:**
   - Processes can customize how they handle signals by defining their signal handlers.
   - Custom signal handlers allow processes to take specific actions in response to signals, such as cleaning up resources or saving state.

8. **Signal Termination:**
   - By default, some signals terminate processes when they are received, while others can be customized to perform different actions.

Understanding signals is essential for designing robust and responsive Unix-like software applications. They enable processes to communicate and adapt to a wide range of events, improving system reliability and user experience.

### Comparing Signals and Interrupts

**Interrupts:**

1. **Communication Medium:** Interrupts can be viewed as a means of communication between the CPU and the OS kernel.

2. **Initiators:** Interrupts can be initiated by multiple sources, including:
   - The CPU itself, for exceptions like divide by zero or page faults.
   - Hardware devices, such as input devices (hardware interrupts).
   - CPU instructions, like traps initiated by syscalls or breakpoints in debugging.

3. **Management:** Interrupts are managed primarily by the CPU. When an interrupt occurs, the CPU interrupts the current task and invokes an OS-kernel-provided Interrupt Service Routine (ISR) or interrupt handler. The ISR is responsible for handling the specific event or condition that triggered the interrupt.

**Signals:**

1. **Communication Medium:** Signals can be viewed as a means of communication between the OS kernel and OS processes.

2. **Initiators:** Signals can be initiated by different sources, including:
   - The OS kernel itself, for specific events or errors (e.g., SIGFPE for a floating-point exception, SIGSEGV for a segmentation fault).
   - Processes, using functions like `kill()` to send signals to other processes.

3. **Management:** Signals are primarily managed by the OS kernel. When a signal is generated, the OS kernel delivers it to the target thread or process. The OS kernel then invokes either a generic action predefined for that signal (e.g., terminate the process) or a process-provided signal handler. The signal handler is a user-defined function that allows processes to respond to signals in a customized way.

In summary, interrupts and signals serve different purposes and involve different communication paths within a computer system:

- Interrupts are used for low-level hardware events and are initiated by the CPU, hardware devices, or specific CPU instructions. They are managed by the CPU and handled by OS-kernel-provided Interrupt Service Routines (ISRs).

- Signals are used for higher-level events and communication between processes and the OS kernel. They can be initiated by the OS kernel or processes and are managed by the OS kernel. Signals can trigger predefined actions or user-defined signal handlers in processes.

Both interrupts and signals are essential mechanisms for managing events and communication in a computer system, but they operate at different levels of abstraction and have distinct use cases.
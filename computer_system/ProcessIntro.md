# Process
## How you run a program?

### Program Execution Process

#### 1. User Executes Program
- **What Happens**: You, the user, initiate the execution of a program by either clicking on its icon or running a command in the terminal.
- **Role**: User interaction
- **Location**: User Interface (UI)

#### 2. Demand Paging
- **What Happens**: Instead of pre-loading the entire program into RAM, the operating system uses demand paging to load only the necessary parts (pages) of the program when they are actually needed during execution.
- **Role**: Memory management technique
- **Location**: Operating System (OS)

> What It Is: Demand paging is a mechanism in modern operating systems where pages (segments of a program) are loaded into RAM on an as-needed basis. When a program tries to access a page not currently in RAM, a page fault occurs, prompting the OS to load the required page from storage, allowing for efficient memory utilization and the ability to run larger programs than would fit into physical RAM.

#### 3. RAM (Random Access Memory)
- **What Happens**: The loader places the program into RAM. This is a type of volatile memory that provides fast read and write access to a processor.
- **Role**: Memory storage
- **Location**: Physical hardware

> Before running anything, the OS clearly must do some work to get the important program bits from disk into memory. This is the job of the loader, which reads the program from disk and places it into RAM.

> Besides stack and heap, the OS will also do some other initialization tasks, particularly as related to I/O. For example, in UNIX systems, each process by default has three open file descriptor, namely `stdin`, `stdout`, and `stderr`. These are the standard input, output, and error streams, respectively.

#### 4. Process Created
- **What Happens**: Once the program is in RAM, the operating system creates a new process for it. A process is essentially a program in execution, and activities such as keeping track of processor status and program counter are the essential roles of process management.
- **Role**: OS task management
- **Location**: Operating System (OS)

   ##### Process state

   - **Running**: The process is currently being executed by the CPU.

   - **Ready**: The process is ready to be executed by the CPU, but it is waiting for the CPU to become available.

   - **Blocked**: The process is waiting for some event to occur (such as an I/O operation) before it can continue. And some other process and use the processor.

#### 5. CPU (Central Processing Unit)
- **What Happens**: The CPU starts executing the process. It fetches, decodes, and executes instructions from RAM.
- **Role**: Computation and logic operations
- **Location**: Physical hardware

> Once the Scheduler decides which process to run next, it sets the CPU's Program Counter to the entry point of that process's next instruction, effectively handing over control to that process.

#### 6. Process Execution
- **What Happens**: The process is now actively being executed. It may perform a variety of tasks such as calculations, data processing, or network communication.
- **Role**: Program functionality
- **Location**: CPU and RAM

#### 7. Process Termination
- **What Happens**: Once the process completes its execution or encounters an error, it is terminated. The OS then reclaims any memory and resources that were allocated to the process.
- **Role**: Ending the program
- **Location**: Operating System (OS)

#### 8. Memory Freed
- **What Happens**: After the process is terminated, the memory it was using is freed up and returned to the system pool.
- **Role**: Resource management
- **Location**: RAM and Operating System (OS)

## **Operating System Data Structures:**
- The OS uses various critical data structures to manage its functions and keep track of relevant information. One of these is the **Process List** (also known as the task list), which maintains records of all running programs in the system.
- Each entry in this list is sometimes called a **Process Control Block (PCB)** or a **process descriptor**. It's essentially a structured way to store information about each process.

**xv6 Kernel – Process Information:**

```c
### xv6 Register Context

```c
// the registers xv6 will save and restore
// to stop and subsequently restart a process
struct context {
  int eip;
  int esp;
  int ebx;
  int ecx;
  int edx;
  int esi;
  int edi;
  int ebp;
};

// the different states a process can be in
enum proc_state { UNUSED, EMBRYO, SLEEPING,
                  RUNNABLE, RUNNING, ZOMBIE };

// the information xv6 tracks about each process
// including its register context and state
struct proc {
    char *mem;                  // Start of process memory
    uint sz;                    // Size of process memory
    char *kstack;               // Bottom of kernel stack for this process
    enum proc_state state;      // Process state
    int pid;                    // Process ID
    struct proc *parent;        // Parent process
    void *chan;                 // If !zero, sleeping on chan
    int killed;                 // If !zero, has been killed
    struct file *ofile[NOFILE]; // Open files
    struct inode *cwd;          // Current directory
    struct context context;     // Switch here to run process
    struct trapframe *tf;       // Trap frame for the current interrupt
};


```

- **context**: This structure holds the register context. It consists of the values for:
  - eip, esp, ebx, ecx, edx, esi, edi, ebp
- When a process is stopped, `its registers' values are saved her`e. By restoring these values, the OS can continue running the process.
  
- **proc_state**: Indicates the various states a process can be in:
  - UNUSED, EMBRYO, SLEEPING, RUNNABLE, RUNNING, ZOMBIE
  
- **proc structure**: Contains details about each process, such as:
  - Memory start (`*mem`)
  - Size of process memory (`sz`)
  - Bottom of kernel stack for the process (`*kstack`)
  - Process state (`state`)
  - Process ID (`pid`)
  - Parent process (`*parent`)
  - Channel for sleeping (`*chan`)
  - Killed status (`killed`)
  - Open files (`*ofile[NOFILE]`)
  - Current directory (`*cwd`)
  - Context (`context`)
  - Trap frame for the current interrupt (`*tf`)

**Process States:**
- **Running**: When the process is currently executing.
- **Ready**: Process is prepared to run, waiting for CPU time.
- **Blocked**: Process is waiting for an I/O event or some other form of signal.
- **Zombie**: Represents a process that has finished execution but has not yet been cleaned up. In UNIX systems, a process in the zombie state has completed its task, but its exit status hasn't been collected by its parent process.
  
**Summary:**
- The process is the most basic and essential abstraction of the OS. It's essentially viewed as a running program.
- The OS uses techniques like **context switch** to stop and resume processes by saving and restoring their register values.
- There are mechanisms to implement processes and policies for scheduling them, which collectively help understand how the OS operates.

> A process list contains information about all running processes in the system. Each entry in this list is found in what is sometimes called a Process Control Block (PCB). It's essentially a structured way to store information about each process.
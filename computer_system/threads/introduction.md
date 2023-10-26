# Threads

## What is User-Level Thread and Kernel-Level Thread?

Certainly, here's a summary of the differences between User-Level Threads and Kernel-Level Threads presented in a table format:

| Parameter                  | User-Level Threads                 | Kernel-Level Threads              |
|----------------------------|-----------------------------------|----------------------------------|
| Implementation             | Managed by user-level software.    | Implemented and managed by the operating system (OS). |
| Recognition by OS          | Not recognized individually; the OS treats the entire process as a single entity. | Recognized and managed individually by the OS. |
| Implementation Complexity  | Relatively easy to implement.     | More complex implementation and requires explicit OS support. |
| Context Switch Time        | Faster context switching because it doesn't involve switching to kernel mode. | Context switching may be slower due to kernel mode involvement. |
| Hardware Support           | No specific hardware support for context switching required. | May require hardware support for efficient context switching. |
| Blocking Operation         | If one user-level thread blocks, it can potentially block the entire process. | If one kernel-level thread blocks, other threads within the same process can continue execution. |
| Multithreading             | May not fully leverage multi-core processors and multiprocessing. | Can fully leverage multi-core processors and multiprocessing. |
| Creation and Management    | Faster creation and management.    | Creating and managing kernel-level threads can be more time-consuming. |
| OS Support                 | Can be used on any OS with thread libraries. | Depends on the specific OS; support varies. |
| Memory Management          | User-level threads share the same address space within a process. | Kernel-level threads have their own separate address spaces, isolating them. |
| Fault Tolerance            | Less fault-tolerant; a crashing thread can affect the entire process. | More fault-tolerant; one thread's crash doesn't necessarily affect others. |
| Resource Utilization       | May not fully utilize system resources like I/O operations. | Fully utilizes system resources, including I/O operations. |
| Portability                | Generally more portable across different operating systems. | May be less portable due to OS-specific threading models. |

### Memory management aspect of User-Level Threads and Kernel-Level Threads:

**User-Level Threads Memory Management:**
- User-Level Threads share the same address space within a process. This means that all threads belonging to a process have access to the same memory and resources.
- Since User-Level Threads within a process share the same address space, they can easily access and modify data stored in the process's memory. This shared memory space simplifies data sharing and communication between threads.
- While sharing memory can simplify communication, it also introduces potential challenges. Threads need to coordinate their access to shared data to prevent data corruption or race conditions. This often requires the use of synchronization mechanisms like mutexes or semaphores to ensure data integrity.
- User-Level Threads can efficiently communicate and share data because they operate within the same memory space. However, this also means that if one thread in a process corrupts memory or crashes, it can affect all other threads within that process.

**Kernel-Level Threads Memory Management:**
- Kernel-Level Threads have their own separate address spaces, isolating them from each other. Each thread operates in its own distinct memory environment.
- Each kernel-level thread is assigned its own memory resources and memory space by the operating system. This isolation ensures that one thread's actions, such as accessing or modifying memory, do not directly impact other threads within the same process.
- Because Kernel-Level Threads have separate memory spaces, they do not share memory resources by default. If they need to share data, they typically use inter-process communication (IPC) mechanisms provided by the operating system. IPC mechanisms allow threads or processes to exchange data in a controlled manner.
- Memory isolation among Kernel-Level Threads provides a higher degree of fault tolerance. If one thread crashes or experiences memory-related issues, it is less likely to affect the stability of other threads within the same process.

## Preemptive and Non-Preemptive Scheduling

**Preemptive vs. Non-preemptive Scheduling for Threads:**

In the context of thread scheduling, the terms "preemptive" and "non-preemptive" refer to how the operating system manages CPU allocation when multiple threads are competing for execution.

**Preemptive Scheduling:**
- Threads can be forcibly interrupted by the operating system at predefined time intervals or based on thread priorities.
- Ensures fairness and responsiveness by preventing threads from monopolizing the CPU.
- Even in preemptive scheduling, threads can voluntarily yield the CPU by calling a yield function.

**Non-preemptive Scheduling:**
- Threads are expected to voluntarily yield the CPU by explicitly calling a yield function or taking cooperative actions.
- If a thread does not yield voluntarily, it can potentially monopolize the CPU, causing other threads to wait indefinitely.
- Relies on the cooperation of threads, and the operating system does not forcibly interrupt them.

Both scheduling approaches have their use cases, with preemptive scheduling being more common in modern operating systems to ensure fair CPU allocation and responsiveness. However, even in preemptive scheduling, threads can still yield voluntarily to manage their execution.

## Properly Handling Threads After Completion

When working with multi-threaded programs, it's essential to ensure that threads are appropriately managed and terminated after they have completed their tasks. Failure to do so can lead to various issues, including resource leakage, uncontrolled execution, and synchronization problems. Here are some key points to consider:

**What to Do After Threads Finish Their Job:**

1. **Thread Exit:** Always use the appropriate thread exit function (e.g., `qthread_exit`) to terminate a thread when it has completed its task.

2. **Thread Joining:** If necessary, use thread joining functions (e.g., `qthread_join`) to wait for a thread to finish before proceeding with other parts of your program. This ensures that you have control over the order of execution.

3. **Resource Cleanup:** If your threads allocate resources (e.g., memory, file handles), make sure to release or close these resources properly within the thread before exiting.

4. **Data Sharing:** If threads share data or resources, implement proper synchronization mechanisms (e.g., mutexes, semaphores) to avoid data races and conflicts.

**Consequences of Not Properly Handling Threads:**

1. **Resource Leakage:** Threads that are not properly exited may not release allocated resources, leading to memory leaks and resource exhaustion.

2. **Uncontrolled Execution:** Unexited threads can continue executing unpredictably, potentially interfering with other threads or the main program.

3. **Stack and Memory Issues:** Memory allocated for thread stacks may not be freed, leading to stack overflow or other memory-related problems.

4. **Race Conditions:** Uncontrolled threads can introduce race conditions and synchronization problems, making the program behavior unpredictable.

5. **Debugging Challenges:** Managing threads that are not properly terminated can make debugging more challenging, as it becomes difficult to track thread states and identify issues.

In summary, proper thread management, including explicit thread termination, is crucial for the stability and reliability of multi-threaded programs. Always ensure that threads are appropriately exited or joined when they have finished their tasks to avoid potential problems and resource leaks.

## Function Pointer

**Function Pointers in C**

Function pointers in C allow you to create pointers that point to functions instead of data. They are a powerful feature that enables you to use functions in a more flexible and dynamic manner.

Let's start with a basic function that we'll use for demonstration:

```c
int addInt(int n, int m) {
    return n + m;
}
```

**Defining a Function Pointer:**

To define a pointer to a function that receives two `int` parameters and returns an `int`, you can use the following syntax:

```c
int (*functionPtr)(int, int);
```

**Assigning a Function to a Pointer:**

You can assign a function to the function pointer as follows:

```c
functionPtr = &addInt;
```

**Using the Function Pointer:**

To use the function pointer, you need to dereference it with the function call operator `()`:

```c
int sum = (*functionPtr)(2, 3); // sum == 5
```

**Passing Function Pointers to Functions:**

You can also pass function pointers to other functions, just like any other data type:

```c
int add2to3(int (*functionPtr)(int, int)) {
    return (*functionPtr)(2, 3);
}
```

**Function Pointers as Return Values:**

Function pointers can be used as return values from functions. Here's an example:

```c
int (*functionFactory(int n))(int, int) {
    printf("Got parameter %d", n);
    int (*functionPtr)(int, int) = &addInt;
    return functionPtr;
}
```

However, using a `typedef` can make this more readable:

```c
typedef int (*myFuncDef)(int, int);

myFuncDef functionFactory(int n) {
    printf("Got parameter %d", n);
    myFuncDef functionPtr = &addInt;
    return functionPtr;
}
```

Function pointers are a versatile feature in C that can be used for various purposes, including creating callback mechanisms, implementing dynamic behavior, and more.

## Resource Management in Thread Libraries

In thread libraries like the one we are implementing, resource management, especially memory management, is a critical aspect to consider. When a thread calls `qthread_exit` to exit, `it removes itself from the active queue but does not immediately free its associated resources, such as stack memory.`

This approach is intentional and serves two main purposes:

1. **Memory Ownership**: Threads are responsible for their own stack memory. If a thread were to immediately free its stack memory within `qthread_exit`, it might cause issues if other parts of the program are still trying to access that memory after the thread has exited. Delaying resource cleanup helps avoid such problems.

2. **Waiting for Join**: Other threads in the program might still be interested in the return value of the exiting thread, and they use `qthread_join` for that purpose. If the exiting thread were to free its resources immediately, the return data might be lost, leading to unexpected behavior. Leaving resource cleanup to be handled when another thread calls `qthread_join` ensures that resources are reclaimed only when they are no longer needed and when it's safe to do so.

Therefore, remember that calling `qthread_exit` marks a thread as finished and removes it from the active queue, but the actual resource cleanup occurs when another thread calls `qthread_join`. Proper usage of thread library functions is essential to ensure that resources are managed correctly and efficiently.

## **Context Switching in qthreads:**

- **Purpose**: Context switching in the `qthreads` library is essential for managing and executing threads concurrently.

- **Creating Threads**: When you create a new thread using `qthread_create`, you initialize its context, including its stack and execution state.

- **Switching Execution**: Context switching is used to transition execution from one thread to another. It involves saving the current thread's context and loading the context of the thread to be executed.

- **Concurrency**: Context switching enables multiple threads to run concurrently, allowing them to share CPU time and make progress independently.

- **Thread Management**: Context switching is crucial for managing thread scheduling and control flow. It ensures that threads can exit (`qthread_exit`), yield (`qthread_yield`), and be managed effectively.

Context switching is a fundamental mechanism that enables multithreading in `qthreads`, facilitating concurrent execution and thread management.

## Why init

- `qthread_init` is a function used to initialize a user-level thread management system within your program.
- When your program starts, it typically runs in the context of the main thread provided by the operating system.
- `qthread_init` sets up data structures and context for user-level threads, creating a "main thread" in the user-level thread management system.
- User-level threads are managed within your program's address space and are separate from the main OS thread.
- `qthread_init` allows you to create and manage user-level threads using functions like `qthread_create`, `qthread_exit`, and more.
- This user-level thread management system operates independently of the main OS thread, providing concurrency within your program.


## `makecontext`, `getcontext`, and `swapcontext` in User-Level Threading

1. **`makecontext` Function:**
   - `makecontext` is used in user-level threading libraries to set up the execution context for a user-level thread.
   - It takes a `ucontext_t` structure and a function pointer as arguments.
   - The function pointer specifies the entry point for the thread's execution.
   - It also takes the number of integer arguments that will be passed to the entry function and allows for additional integer arguments to be passed.
   - `makecontext` prepares a context (ucontext_t) to execute a specific function when that context is activated (usually with swapcontext)

2. **`getcontext` Function:**
   - `getcontext` is used to obtain the current execution context, which includes the program's state at the point of the call.
   - It stores the current context in the provided `ucontext_t` structure.
   - Commonly used in user-level threading libraries to save the context of the currently executing thread before switching to another thread.

3. **`swapcontext` Function:**
   - `swapcontext` is used to perform a context switch between two contexts (e.g., between two user-level threads).
   - It takes two `ucontext_t` structures as arguments, representing the context to switch from and the context to switch to.
   - `swapcontext` saves the current context and loads the new context, effectively switching the execution from one thread to another.
   - Used to implement thread scheduling and context switching in user-level thread libraries.

These functions are essential tools for managing user-level threads without relying on the operating system's thread scheduler. They allow user-level threads to be created, their execution contexts to be set up, and context switches to be performed, all within user space. This enables lightweight and efficient thread management in user-level threading libraries.
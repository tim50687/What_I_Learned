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

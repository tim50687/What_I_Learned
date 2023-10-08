# Concurrency

## **Understanding Threads and Their Benefits**

**1. Parallelism:**
   - **Purpose:** Threads enable $\textcolor{cyan}{\text{efficient utilization of multiple processors}}$ by allowing parts of a program to run concurrently.
   - **Example:** For operations on large arrays (like array addition), it can significantly speed up this process by distributing the workload across multiple CPUs. Each thread can handle a part of the array, allowing operations to be done in parallel.
   - **Terminology:** The process of adapting a single-threaded program for multi-core systems is termed $\textcolor{cyan}{\text{"parallelization"}}$.

**2. Overcoming I/O Blocking:**
   - **Purpose:** Threads can prevent a program from $\textcolor{cyan}{\text{halting due to slow I/O}}$.
   - **Example:** If a program is involved in different I/O activities (e.g., waiting for a message), one thread can handle the I/O while another continues with other tasks.
   - **Outcome:** This overlap ensures that while one thread is blocked, other threads can perform $\textcolor{cyan}{\text{useful tasks}}$. This model is used in applications like web servers and databases.

**Processes vs. Threads:**
   - **Shared Memory:** Threads within a program share the same address space, making $\textcolor{cyan}{\text{data sharing efficient}}$.
   - **Isolation:** Processes run in separate spaces. This can be beneficial when tasks operate independently.
   - **Usage:** Threads are suited for tasks needing shared data, while processes are for $\textcolor{cyan}{\text{logically distinct tasks}}$.

**Takeaway:** Threads offer a way to improve performance through parallelism and to ensure smooth operation despite I/O blocking. They are a go-to in modern software design when tasks need efficient data access.

## Thread Creation

1. **Thread Creation:**
   - Creating a thread can be compared to $\textcolor{cyan}{\text{making a function call}}$. However, there's a distinction: while a function call will execute and then return to the caller, thread creation leads to a new execution path that operates concurrently with the caller.
   - The point at which the new thread begins execution may be immediately after its creation, or it could be delayed, depending on the OS scheduler's decisions.

2. **OS Scheduler's Role:**
   - The Operating System's scheduler determines $\textcolor{cyan}{\text{what runs next}}$. Its decision-making is based on algorithms that aim for efficient task management, but the exact sequence of task execution can be unpredictable.
  
3. **Complexity of Concurrency:**
   - Threads introduce a level of unpredictability. Without concurrency, computer operations follow a predictable sequence. With concurrency, multiple operations can interleave, making it $\textcolor{cyan}{\text{hard to foresee the exact order}}$ of execution.
   - This unpredictable nature escalates the complexity of understanding and managing computer operations. Concurrency not only complicates things, but it can also magnify challenges exponentially.

**Takeaway:** While threads unlock potentials like parallelism, they also bring complexity and unpredictability. It's crucial to approach multi-threading with caution and a deep understanding of its intricacies.

## The heart of the problem: Uncontrolled scheduling


- A `critical section` is a piece of code that accesses a shared resource, usually a variable or data structure.
- A `race condition` (or data race [NM92]) arises if multiple threads of execution enter the critical section at roughly the same time; both attempt to update the shared data structure, leading to a surprising (and perhaps undesirable) outcome.
- An `indeterminate program` consists of one or more race conditions; the output of the program varies from run to run, depending on which threads ran when. The outcome is thus not deterministic, something we usually expect from computer systems.
- To avoid these problems, threads should use some kind of `mutual exclusion primitives`; doing so guarantees that `only a single thread ever enters a critical section,` thus avoiding races, and resulting in deterministic program outputs.
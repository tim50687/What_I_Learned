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

## Thread API

**Note on Multithreading with POSIX:**

1. **Introduction**:
   - Writing a multi-threaded program requires the ability to create new threads. 
   - In POSIX, this is achieved through the `pthread_create()` function.

2. **Thread Creation**:
   ```c
   #include <pthread.h>

   int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine)(void*), void *arg);
   ```
   ```c
   #include <stdio.h>
   #include <pthread.h>

   typedef struct {
      int a;
      int b;
   } myarg_t;

   void *mythread(void *arg) {
      myarg_t *args = (myarg_t *) arg;
      printf("%d %d\n", args->a, args->b);
      return NULL;
   }

   int main(int argc, char *argv[]) {
      pthread_t p;
      myarg_t args = { 10, 20 };
      int rc = pthread_create(&p, NULL, mythread, &args);
      // Rest of your main function...
      return 0;
   }

   ```

3. **Function Arguments**:
   - `thread`: A pointer to a structure of type `pthread_t`. It is used to interact with this thread later.
   - `attr`: Used to specify attributes for the thread (e.g., stack size or scheduling priority). Defaults are typically sufficient, so passing `NULL` is common.
   - `start_routine`: A function pointer. It defines which function the thread should start executing. The function is expected to take a single `void*` argument and return a `void*` value.
   - `arg`: The argument to be passed to the `start_routine`.

4. **Function Pointers**:
   - A function pointer in C represents the address of a function. It allows dynamic invocation of functions.
   - For `pthread_create()`, the `start_routine` is expected to have a specific signature. Depending on the requirements, the argument type and return type can be adjusted.

5. **Passing Multiple Arguments**:
   - Since `start_routine` takes only one argument, if you want to pass multiple arguments to it, you can package them into a single custom type (e.g., `myarg_t`).
   - Within the `start_routine`, you can cast the received `void*` argument back to the expected type and access the packaged arguments.

6. **Execution**:
   - Upon successfully creating a thread with `pthread_create()`, you now have another active execution entity. This new thread has its own call stack but shares the address space with existing threads in the program.

**Highlighted Points**:
- $\textcolor{cyan}{\text{POSIX}}$ offers a function called `pthread_create()` for thread creation.
- Threads can be $\textcolor{cyan}{\text{given specific attributes}}$ through the `attr` argument.
- A thread starts its execution from a function pointed to by start_routine.
- Passing multiple arguments requires packaging them into a $\textcolor{cyan}{\text{single custom type}}$.
- Creating a thread results in another $\textcolor{cyan}{\text{live executing entity}}$ with its own call stack.

### Waiting for thread Completion

```c
#include <stdio.h>
#include <pthread.h>

typedef struct {
    int a;
    int b;
} myarg_t;

typedef struct {
    int x;
    int y;
} myret_t;

void *mythread(void *arg) {
    myarg_t *args = (myarg_t *) arg;
    printf("%d %d\n", args->a, args->b);
    
    myret_t *rvals = malloc(sizeof(myret_t));
    rvals->x = 1;
    rvals->y = 2;
    return (void *) rvals;
}

int main(int argc, char *argv[]) {
    pthread_t p;
    myret_t *rvals;
    myarg_t args = { 10, 20 };
    
    pthread_create(&p, NULL, mythread, &args);
    pthread_join(p, (void **) &rvals);
    
    printf("returned %d %d\n", rvals->x, rvals->y);
    free(rvals);
    return 0;
}

```
#### pthread_join()

- When you create a thread and it's running, your main program doesn't know when the thread finishes. If you want your main program to wait until the thread completes its task, you use `pthread_join()`.
  
- The `pthread_join()` function ensures that the main program waits until the specified thread has finished executing.

#### Arguments to pthread_join():

1. **pthread_t thread**: This argument is the ID of the thread you want to wait for. This ID is given to you when you create the thread using `pthread_create()`.
  
2. **void **value_ptr**: This is a pointer to where the result of the thread's execution will be stored. Since a thread can return any kind of data, this pointer is of type "pointer to void" (`void*`). This means it can point to any type of data. You can think of it as a generic pointer.

#### The Example:

Here's a breakdown of the provided code:

1. **Structures**:
    - Two structures are defined: `myarg_t` (used to pass arguments to the thread) and `myret_t` (used to retrieve results from the thread).
    
2. **Thread Function (mythread)**:
    - This function is what the thread will execute when it runs.
    - It receives a single argument, `arg`, which is a pointer (hence it can point to any data type). Here, it points to `myarg_t` data.
    - The function allocates memory for a `myret_t` structure and sets its values to `x=1` and `y=2`. 
    - It then returns a pointer to this structure. This is the result that the main program will retrieve after the thread finishes.

3. **Main Program**:
    - It first defines the arguments for the thread in a `myarg_t` structure (`args = {10, 20}`), though these arguments aren't used in this example.
    - It then creates the thread using `Pthread_create()`, which will run the `mythread()` function.
    - The main program waits for the thread to complete using `Pthread_join()`. Once the thread finishes, the return value (pointer to `myret_t` structure) is stored in `rvals`.
    - Finally, the program prints the results and then frees the memory allocated inside the thread.

#### Key Points:
- The `pthread_create()` function is used to start a new thread.
  
- The `pthread_join()` function is used to wait for a thread to finish and to retrieve its result.
  
- You have to be careful about memory management when working with threads. Here, the memory is allocated inside the thread, and after its results are used, the memory is freed in the main program.

#### However

1. **Using `pthread_create()` followed by `pthread_join()`**:
    - This segment suggests that if you're simply creating a thread and then immediately waiting for it to finish (`pthread_join()`), it might seem unusual or unnecessary. After all, the main idea behind threads is to allow multiple tasks to run concurrently.

2. **Procedure Calls**:
    - The text mentions that if you're doing the above pattern (create then immediately wait), then you might as well have just made a `regular function` (or procedure) call instead of using a thread. This is because a regular function call also runs a block of code and waits for it to complete before moving on.

3. **Purpose of Threads**:
    - Threads shine when you want to do multiple things at once. For instance, you might want to create multiple threads to process data concurrently and not wait for each one to complete immediately after starting it.

4. **Not All Multi-threaded Code Uses `pthread_join()`**:
    - The text points out that not every situation requires you to wait for a thread to complete.
    - Consider a multi-threaded web server: the main thread could continuously accept client requests and hand them off to worker threads for processing. These worker threads might run indefinitely, processing multiple requests over their lifetimes. In such a scenario, the main thread doesn't always wait for worker threads to finish a task before continuing (it doesn't always "join" them).

5. **When Joining is Essential**:
    - For parallel processing tasks, where you split up a job into smaller tasks and distribute them among several threads, you'd likely want to wait for all threads to finish before continuing. This is because the next step in your computation might depend on the results of all those threads.
    - In these situations, you use `pthread_join()` to ensure that all threads have completed their work before the program moves onto the next phase.

In summary:
- Using threads makes sense when you want concurrent execution. If you're creating a thread just to wait for it immediately, you might as well use a simple function call.
- Not every threaded application requires you to wait for threads to finish. It depends on the specific use case and application design.
- In scenarios where the next step depends on the results of all threads, you'll likely use `pthread_join()` to ensure all threads have finished their tasks.

## Locks

### POSIX Locking and Concurrency

In the POSIX framework, locks can be associated with specific variables, enabling greater flexibility in synchronization strategies. This offers the following benefits:

1. **Increased Concurrency**: Rather than employing a single, overarching lock for every critical section, distinct locks can be allocated for individual data or structures. This fine-grained approach lets multiple threads access locked code concurrently.

2. **Efficiency and Scalability**: By employing variable-specific locks, the system can avoid unnecessary waiting. Threads that need to access different data structures or variables can do so without being blocked by unrelated operations.

3. **Fine-Grained vs. Coarse-Grained**:
   - **Coarse-Grained Locking**: A strategy where one overarching lock protects access to all shared resources. While simple, it can be less efficient in multi-threaded scenarios since only one thread can access any shared resource at a given time.
   - **Fine-Grained Locking**: A strategy where different locks protect different shared resources. This permits multiple threads to access separate resources concurrently, enhancing system throughput.

By using fine-grained locking in the POSIX model, developers can craft synchronization strategies that better fit their specific use cases, optimizing for performance and concurrency.


### **Lock Evaluation Criteria:**

1. **Mutual Exclusion:**
   - Definition: Ensuring that only one thread can enter the critical section at a time, thus preventing concurrent access.
   - Key Question: Does the lock effectively prevent multiple threads from accessing a shared resource simultaneously?

2. **Fairness:**
   - Definition: Ensuring that each thread contending for the lock has an equitable chance to acquire it.
   - Concerns:
     - **Thread Starvation:** It's the scenario where a thread perpetually waits and never gets a chance to acquire the lock, even when it's free. This is an extreme case highlighting the absence of fairness.
   - Key Question: Does any thread contending for the lock get indefinitely postponed or neglected, leading to starvation?

3. **Performance:**
   - Factors to Consider:
     - **No Contention:** Assess the time overhead of acquiring and releasing the lock when there's only one thread in the system.
     - **Single CPU Contention:** Examine the efficiency of the lock when multiple threads compete for it on a single CPU. 
     - **Multi-CPU Contention:** Evaluate the lock's performance when threads from different CPUs contend for it.
   - Key Question: What is the time overhead introduced by the lock in different contention scenarios, and how does it affect the overall system performance?

### Why test and set can solve correctness problem?

If `TestAndSet` were only a C function written like that, it wouldn't be atomic and wouldn't solve the problem. The difference is in how `TestAndSet` is actually implemented and executed.


1. **Atomic in this Context**: "Atomic" here doesn't refer to atoms in the physical sense. In computer science, an "atomic operation" means an operation that runs completely independently of any other operations and is uninterruptible. Once it starts, it runs straight through without being stopped or interfered with.

2. **The Role of Hardware**: While we can represent `TestAndSet` as a function in C or any high-level language, for it to be truly atomic, it must be supported by the hardware. That means the processor itself has a built-in mechanism or instruction to execute `TestAndSet` as a single, uninterruptible operation. When you call `TestAndSet` in a program on a system that supports it, under the hood, the processor uses its built-in atomic `TestAndSet` instruction.

3. **Why Not Just a Function?**: If `TestAndSet` were only a high-level function like in the example, other threads or processors could interfere between the moment we fetch the old value and when we set the new value. This interference would introduce the race condition we're trying to avoid. That's why a simple function isn't sufficient. The hardware-level atomic operation ensures that the entire fetch-and-set sequence happens without any possibility of interruption or interference.

In summary, while we can *represent* operations like `TestAndSet` in high-level programming languages for understanding or illustrative purposes, ensuring their atomicity in real-world scenarios requires hardware support. When we talk about `TestAndSet` in the context of synchronization, we're often referring to the hardware-supported atomic operation, not just the high-level function representation.

#### Evaluating Spin Locks

The crucial element missing in the description is the atomicity of the combined operations. In a real `TestAndSet` hardware instruction, the process of fetching the old value, storing the new value, and returning the old value is done as a single, indivisible (atomic) operation. No other operation on the CPU, and no other CPU (in multi-CPU systems), can see the intermediate state or interrupt in the middle of this operation.

For `TestAndSet` to work correctly as a mutual exclusion primitive, it needs to be a hardware-supported atomic operation. When we say that `TestAndSet` is a hardware instruction, we mean that the CPU provides support to ensure that the entire sequence of fetching, storing, and returning occurs without interruption. If two threads on two different CPUs were to execute the `TestAndSet` instruction at the "same time", the hardware ensures that they are serialized in some order, so only one of them sees the lock as available.

**Spin Locks on a Single-CPU System**

- A spin lock uses atomic hardware instructions (e.g., `test-and-set` or `compare-and-swap`) to check if a lock is available.
- These atomic operations ensure that reading, possibly modifying, and writing a memory value occurs in an uninterruptible step, providing mutual exclusion.
- In a uniprocessor system:
  1. If a thread (Thread A) tries to acquire a spin lock held by another thread (Thread B), Thread A will enter a loop, repeatedly checking if the lock is free.
  2. The OS scheduler can preempt Thread A (i.e., pause its execution) due to its time slice expiring or other scheduling decisions.
  3. If another thread (Thread C) is scheduled and also attempts to acquire the same lock, it will also enter a spin, waiting for the lock to be released.
  4. This becomes inefficient: if Thread B isn't scheduled to run, both Thread A and Thread C are stuck in a non-productive spinning state.
- In summary, on a single-CPU system, spin locks can lead to significant inefficiencies when threads are preempted while holding or waiting for a lock.


**Multiple CPUs**: 

In a multiprocessor system, spin locks can be more efficient. If one thread on CPU 1 holds the lock and another thread on CPU 2 tries to acquire it, the second thread will spin. However, since the critical section (the part of code protected by the lock) is expected to be short, the first thread will quickly release the lock, and the spinning thread can acquire it. In this scenario, the overhead of spinning is relatively small, especially if the number of threads is roughly equal to the number of CPUs.

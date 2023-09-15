# Chapter 2: Program and OS Organization

## Key terms and concepts

### Register

Registers are the smallest data holding elements that are built into the processor itself. These are the memory locations that are directly accessible by the processor. They may hold an instruction, a storage address, or any kind of data such as a bit sequence or individual characters. For example, an instruction may specify that the contents of two defined registers be multiplied together and then placed in a specific register.

**Example**: Accumulator register, Program counter, Instruction register, Address register, etc.

### Memory

Memory is a hardware device used to store computer programs, instructions, and data.  
1. **Primary / Main Memory**: 
   - Directly accessible by the CPU.
   - Comprised of DRAM (Dynamic Random Access Memory).
   - Provides the actual working space for the processor.
   - Holds data and instructions that the processor is currently working on.
   - Examples include RAM, register, cache, etc.

2. **Secondary Memory / Mass Storage**:
   - Not directly accessible by the CPU.
   - Data from secondary memory needs to be transferred to primary memory before the CPU can access it.
   - Examples include hard drives, SSDs, CDs, DVDs, USB drives, etc.

- **Volatile Memory**: Loses its contents when the computer or hardware device loses power. Example: RAM.
- **Non-Volatile Memory**: Retains its contents even if power is lost. Examples: EPROM, Flash memory.

$\textcolor{cyan}{\text{RAM is usually stored outside the CPU in separate chips.}}$  
$\textcolor{cyan}{\text{RAM memory modules are installed into slots on the computer motherboard.}}$

### Disk Storage

#### **Disk Driver:**
   - The disk driver is a software component, typically part of an operating system, that provides an interface between the operating system and the disk controller.
   - It translates high-level operating system commands (like "open this file") into lower-level commands that the disk controller can understand.
   - The driver ensures that the operating system can communicate with the storage device regardless of its brand or model, as long as there's a corresponding driver for that device.
   - In essence, the disk driver "drives" or operates the disk controller, telling it what actions to perform.

#### **Disk Controller:**
   - The disk controller is a hardware component that `manages` the physical operations of a storage device, such as a hard disk drive (HDD) or a solid-state drive (SSD).
   - It is responsible for `converting the logical data requests from the computer (like reading a file) into the actual physical actions on the storage device (like moving the read/write head to the correct track or sector on an HDD).`
   - The disk controller communicates directly with the storage device and typically resides on the device's motherboard or on the storage device itself.
   - In the context you provided, the disk controller is described as "extremely simple," which means it likely performs basic operations to read and write data in 512-byte blocks on the disk.

In a simplified analogy, if you think of the storage device as a car, the disk controller would be like the car's engine and mechanical parts, while the disk driver would be like the car's software or computer system that tells the engine how to operate.

### TRAPS

A trap in an operating system is a software-generated interruption brought on by an error or exception that happens while a programme is being executed. When a trap occurs, the CPU switches from user mode to `kernel mode` and jumps to the trap handler, a predefined point in the operating system. Traps can happen for a number of reasons, including division by zero, accessing erroneous memory addresses, carrying out erroneous instructions, or other unanticipated occurrences that might force the programme to crash or yield inaccurate results.

Traps can also be purposefully created by the software to ask the operating system for a particular service, such reading from a file or allocating memory. The operating system's trap handler is in charge of managing the trap and taking the proper action in accordance with the trap's cause. For instance, if an unlawful instruction set off the trap, the trap handler may terminate the programme and notify the user of the error. The trap handler may carry out the requested service and transfer control back to the programme if the trap is brought on by a request for a particular service.

- **Trap Handler:** This is a specific part of the OS designed to handle traps. Depending on the cause of the trap, the handler decides the appropriate action. It could be terminating a program that performed an illegal operation or fulfilling a service request made by a program.

- **Purposeful Traps:** Not all traps are errors. Programs can intentionally trigger traps to request services from the OS. This is a common mechanism for programs to interact with the OS and utilize its services, like reading a file, writing to a disk, or communicating over a network.

#### Reason to use TRAP

1. `Centralized Control`: By having a specific instruction like TRAP or INT, the CPU provides a standardized way for programs to request `services from the operating system`. This centralizes the control and ensures that system-level operations are invoked in a consistent manner.
2. `Protection`: Directly accessing system-level functions can be risky. By using a trap or interrupt mechanism, the CPU can safely transition from user mode (where regular programs run) to kernel mode (where the OS runs). This ensures that the system remains stable and secure.




## 2.1 Simple Computer

<p align = "center">
<img src = "images/simple_computer.png" style = "width:400; border:0">
</p>

1. **16-bit computer**: The "16-bit" part indicates that the computer's central processing unit (CPU) is designed to handle data in chunks of 16 bits at a time.

2. **8 general-purpose registers, R0-R7**: Registers are small storage areas directly inside the CPU. This computer has 8 of them, labeled R0 through R7. "General-purpose" means they can be used for a variety of tasks, rather than being dedicated to a specific function.

3. **Holding 16 bits each**: Each of these registers can hold 16 bits of data. This aligns with the computer being a 16-bit machine.  

The CPU's ability to handle data in chunks of 16 bits at a time (its `word size`) refers to the amount of data it can process in a single operation, not the total amount of data it can hold across all its registers.  

&nbsp;&nbsp;&nbsp;&nbsp; - `Word Size`: The word size (in this case, 16 bits) refers to the maximum amount of data the CPU can operate on in a single instruction. For example, if the CPU is adding two numbers, it can add two 16-bit numbers in one operation.

&nbsp;&nbsp;&nbsp;&nbsp; - `Total Register Capacity`: While the CPU has 8 registers, each holding 16 bits, it doesn't mean the CPU operates on all of them simultaneously in a single operation. Instead, specific instructions will operate on specific registers or specific pairs of registers. For instance, an instruction might add the contents of R0 to R1 and store the result in R2. This operation still only processes 16 bits from R0 and 16 bits from R1 at a time, even though other registers are available.

&nbsp;&nbsp;&nbsp;&nbsp; - `Parallelism`: Modern CPUs, especially those with multiple cores or those that support vector operations, can indeed process data from multiple registers simultaneously. However, this is a form of parallelism and is different from the basic word size of the CPU. The word size still refers to the amount of data processed per operation per core or execution unit.

4. **Stack pointer (SP)**: The stack is a specific area of memory used for temporary storage of data. The stack pointer is a special register that keeps track of the top of the stack. As data is added to or removed from the stack, the SP is updated to point to the current top.

5. **Program counter (PC)**: The program counter is another special register. It keeps track of where the CPU is in its execution of a program. `Specifically, it holds the address of the next instruction to be executed.` As each instruction is completed, the PC is updated to point to the next one.

6. **Accessed as 8-bit bytes or 16-bit words**: This means that the computer's memory can be read or written in chunks of either 8 bits (called bytes) or 16 bits (called words). This flexibility allows for more efficient processing, depending on the task.

- Memory in a computer is organized in small containers or slots. Each slot can hold a certain amount of data.
- "8-bit bytes" means that each slot in this computer's memory can hold 8 bits of data. This is commonly referred to as a "byte". For example, a single character like "A" or "1" is stored in one byte.
- "16-bit words" means that the computer can also treat two adjacent slots (each of 8 bits) as a single unit, which can hold 16 bits of data. This is called a "word" in this context.

The computer can either take data from one slot at a time (8 bits) or from two slots together (16 bits). 

7. **Zero Flag**: The zero flag is a special register that keeps track of the result of the most recent arithmetic or logical operation. If the result of the operation is zero, the zero flag is set to 1. Otherwise, it is set to 0.

- If the result of the operation is `0` (represented as `00H` in hexadecimal), `the Zero Flag is set`, meaning its value becomes `1`.
- For any other result, ranging from `01H` to `FFH` in hexadecimal,` the Zero Flag is cleared`, meaning its value becomes `0`.

In simpler terms:
- `1` indicates a zero result.
- `0` indicates a non-zero result.

**Example:** 
Consider the following instructions:
```
MVI A, 10H  (Load the value `10H` into register A)
SUB A       (Subtract the value in register A from itself)
```
After executing these instructions, the Zero Flag will be set to `1` because `10H - 10H` equals `00H`.


### Instruction

1. **CALL instruction**:
   - **Purpose**: This instruction is used when you want to execute a subroutine (a separate section of code that performs a specific task). 
   - **How it works**: When the `CALL` instruction is executed, the computer does two main things:
     1. It saves the address of the next instruction (the one that comes after the `CALL` instruction) onto a special memory area called the "stack". This saved address is known as the "return address" because it's where the computer should return to after the subroutine is finished.
     2. It then jumps to the address specified in the `CALL` instruction to start executing the subroutine.
   - **Why use it**: Subroutines are useful because they allow for code reuse. Instead of writing the same code multiple times, you can write it once as a subroutine and then "call" it whenever needed.

2. **RET instruction**:
   - **Purpose**: This instruction is used to return from a subroutine back to the main program.
   - **How it works**: When the `RET` instruction is executed, the computer does the following:
     1. It looks at the top of the stack to find the return address (the address that was saved when the `CALL` instruction was executed).
     2. It pops (removes) this address from the stack.
     3. It then jumps to this return address, resuming execution from where it left off before the subroutine was called.
   - **Why use it**: After a subroutine has finished its task, you need a way to get back to the main program. The `RET` instruction provides this mechanism by using the saved return address.

### Memory-mapped I/O

1. **Memory-mapped input/output devices**: 
   - This means that certain parts of the computer's memory are not just used for storing data like numbers or text. Instead, these specific `memory locations are linked (or "mapped") to certain devices in the computer. When the computer reads from or writes to these memory locations, it's actually communicating with these devices.`

2. **Devices**:
   - **Frame buffer**: 
     - Think of this as the computer's screen memory. It's a specific area in memory that holds what should be displayed on the screen.
     - The frame buffer mentioned here can show 24 lines of text, and each line can have 80 characters. So, the total space needed is 1920 bytes (24 lines x 80 characters = 1920 characters).
     - If you change a byte in this memory area, the corresponding character on the screen will change. For example, if you write the byte for the letter "A" to the first location of this memory, the top-left corner of the screen will show an "A".
   
   - **Keyboard controller**:
     - This is how the computer interacts with the keyboard.
     - There are two special memory locations (or "registers") for this:
       1. One register tells the computer if a key has been pressed.
       2. The other register tells the computer which key was pressed. For example, if you press the "A" key, this register will have the value for "A".


## 2.3 A Simple Operating System Interface

`Library Operating System`:

- The section introduces the concept of a "library operating system." This type of OS consists of a set of functions that are directly linked with an application. The result is a single program that includes both the application and the necessary OS functions.  
- This combined program is often stored in `Read-Only Memory (ROM)`, meaning it's immediately available when the computer is turned on.

### Limitations of a Library Operating System:

While this approach `works well for devices with a single purpose (like a microwave oven)`, it has limitations for general-purpose computers:
Changing or updating the program means changing the entire memory content. This is because the application and OS functions are combined into one program.
In extreme cases, updating the program might require getting a new device. This approach isn't practical for devices like personal computers.

> When this combined program is loaded into memory, it occupies a specific, contiguous block of memory. Any change to a part of this program (whether it's the application portion or the OS library portion) could potentially alter the memory layout or size of the entire program.

**Read-Only Memory (ROM) Considerations:**  

In some devices, the Library Operating System might be stored in read-only memory (ROM). ROM is a type of non-volatile memory that retains its contents even when the device is turned off. If the combined program is stored in ROM, updating any part of it might require reprogramming the ROM, which effectively means changing its entire contents. This is not a practical solution for devices like personal computers.

#### What is ROM?

ROM stands for non-volatile memory in computers., which means the information is permanently stored on the chip. The memory does not depend on an electric current to save data, instead, data is written to individual cells using binary code. Non-volatile memory is used for parts of the computer that do not change, such as the initial boot-up portion of the software, or the firmware instructions that make your printer run. Turning off the computer does not have any effect on ROM. Non-volatile memory cannot be changed by users.

## 2.4 Program Loading

The disk driver doesn't directly read data from the disk. Instead, it facilitates the process by which the operating system can read data from the disk. Here's a step-by-step breakdown:

1. **User or Application Request:** When a user or an application requests to read a file, the operating system receives this request.

2. **Disk Driver's Role:** The operating system communicates this request to the disk driver. The disk driver translates this high-level request into a set of commands that the disk controller can understand.

3. **Disk Controller's Role:** Upon receiving these commands from the disk driver, the disk controller takes charge. It manages the physical operations required to access the data on the storage device. For example, if it's a traditional hard disk drive (HDD), the controller might move the read/write head to the correct track and sector.


#### Example. Writing 512 bytes to a block:

<p align = "center">
<img src = "images/data_controller.png" style = "width:400; border:0">
</p>

      1. **Data Preparation**: 
         - The data you want to write is organized into 256 words, where each word is 16 bytes long.
         - You write these words one at a time to the disk controller's data register. The address of this register is `0xF824`.

      2. **Block Address Specification**:
         - You specify which block you want to write to by writing the block's address (B) to the block address register. The address of this register is `0xF822`.

      3. **Command Execution**:
         - To initiate the write operation, you write a command byte to the cmd/status register. The value `2` represents the WRITE command. The address of this register is `0xF820`.

      4. **Completion Check**:
         - After issuing the write command, you need to check if the operation is complete. You do this by polling (or repeatedly checking) the cmd/status register.
         - Once the operation is complete, the value in the cmd/status register will change from `2` (WRITE) to `0`, indicating that the data transfer to the disk is finished.

      ### Reading from a block:

      1. **Block Address Specification**:
         - Similar to the write operation, you first specify which block you want to read from by writing the block's address (B) to the block address register (`0xF822`).

      2. **Command Execution**:
         - To initiate the read operation, you write a command byte to the cmd/status register. The value `1` represents the READ command. The address of this register is `0xF820`.

      3. **Completion Check**:
         - After issuing the read command, you need to check if the operation is complete. You do this by polling the cmd/status register.
         - Once the operation is complete, the value in the cmd/status register will change from `1` (READ) to `0`, indicating that the data is ready to be read from the disk.

      4. **Data Retrieval**:
         - You then read the data from the disk controller's data register (`0xF824`). The data is organized into 256 words of 16 bytes each.
         - Typically, you would read this data into a buffer in the computer's memory for further processing or use.

In summary, these steps provide a low-level procedure to interact with a disk using a simple disk controller. By following these steps, you can write data to or read data from specific blocks on the disk.

4. **Data Transfer:** Once the disk controller accesses the desired data, it sends this data back through the data bus to the computer's main memory (RAM).

5. **Completion:** The operating system can then access this data from RAM and provide it to the user or application that made the initial request.

### OS example

<p align = "center">
<img src = "images/load_program.png" style = "width:400; border:0">
</p>

- `load` - load from disk

- `load_disk_sectors(_PROGRAM_BASE, blk, count):` This function likely interacts with the disk driver. When this function is called, the disk driver would send commands to the disk controller to read the specified sectors (`blk` and `count`) from the disk. The data read from the disk would then be loaded into memory at the `_PROGRAM_BASE` address.

When you want to load (or execute) a program, the following steps typically occur:

1. **Read from Disk**: The program's data, which is stored on a disk (e.g., hard drive, SSD), is read by the operating system. This involves the disk controller interfacing with the storage device to fetch the required data.

2. **Load into RAM**: The data read from the disk is then loaded into the computer's RAM (Random Access Memory). RAM is a type of volatile memory that provides fast access for the CPU. Loading the program into RAM ensures that the CPU can execute it efficiently.

3. **Execution by CPU**: Once the program is in RAM, the CPU starts executing its instructions. The CPU fetches instructions from RAM, decodes them, and then executes them.

#### Limitation

1. It’s not robust: if it doesn’t find the program you specified, it crashes.
2. If the program crashes, the entire system has to be reset (or power cycled) before another program can be loaded.
>  This operating system lacks isolation between different programs.
3. The program may not run on another machine, or on the same
machine after an OS upgrade.
> This OS are tightly coupled with specific hardware or OS versions.

##### Deal with 1st and 2nd limitation?

In particular, this operating system requires a certain amount of coordination between the OS and the program: 

(a) The OS must know at what address the program expects to begin execution—e.g. the main() function in a C program or its equivalent. This isn’t too much of an issue, as the
OS authors can just tell the application (and compiler) writers what to do. (e.g. in our case execution begins at the very beginning of the program in
memory)

(b) the program, in turn, must have the correct addresses
for any of the OS functions (e.g. getkey in 2.6) which it invokes.

##### 3rd limitation

This is where the problem lies. The location of these entry points may vary from machine to machine due to e.g. different memory sizes, and will almost certainly change across versions of the OS as code is added (or occasionally removed) from some of its functions.

###### Why It's a Problem:
If a program is hard-coded to expect specific memory addresses for its entry point or for OS functions, it becomes very inflexible. If anything changes in the system (like an OS update), the program might try to execute the wrong code or access incorrect memory locations, leading to crashes or unpredictable behavior.

###### Solution:

The issue described is that the location of entry points (i.e., where specific functions or services of the OS begin in memory) can vary based on different factors, such as the machine's memory size or changes in the OS version. If programs are written to directly access these entry points based on their memory addresses, they would break when those addresses change.

Now, let's see how system calls, especially when accessed through a system call table, address this problem:

1. **Fixed Table Location**: The system call table is placed at a fixed, known location in memory, often at the start. This means that even if the actual OS functions move around in memory, the table's location remains consistent.

2. **Indirection**: The system call table acts as an intermediary or a level of indirection. Programs don't call OS functions directly by their memory addresses. Instead, they refer to the system call table's entries. Each entry in the table points to the current location of the corresponding OS function. So, even if an OS function's location changes, its entry in the table is updated to reflect that change.

3. **Abstraction**: By using system calls, programs interact with an abstract interface rather than specific memory addresses. This abstraction ensures that programs remain compatible across different machines and OS versions. They just need to know the system call numbers, not the actual memory addresses of the OS functions.

4. **Flexibility for OS Developers**: With this system, OS developers have the freedom to modify, add, or remove OS functions without worrying about breaking existing programs. They just need to ensure that the system call table is updated accordingly.

In essence, the system call table acts as a stable "middleman" between programs and the OS. Programs rely on this table to access OS services, and the table ensures that it always points to the correct locations of those services, regardless of where they are in memory. This provides a consistent interface for programs and shields them from the underlying changes in the OS.
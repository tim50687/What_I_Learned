# Chapter 2: Program and OS Organization

## Key terms and concepts

## Register

Registers are the smallest data holding elements that are built into the processor itself. These are the memory locations that are directly accessible by the processor. They may hold an instruction, a storage address, or any kind of data such as a bit sequence or individual characters. For example, an instruction may specify that the contents of two defined registers be multiplied together and then placed in a specific register.

**Example**: Accumulator register, Program counter, Instruction register, Address register, etc.

## Memory

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


## Simple Computer

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

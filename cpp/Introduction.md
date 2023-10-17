# Introduction

## Machine Language

- Machine language is the only language a computer is capable of understanding.

Here is a sample machine language instruction: `10110000 01100001`

Some CPUs process instructions that are always 32 bits long, whereas some other CPUs (such as the x86 family, which you are likely using) have instructions that can be a variable length.


1. **Fixed-Length Instruction Set**:
    - CPUs with a fixed-length instruction set expect every instruction to occupy a fixed number of bits, regardless of the actual operation being performed.
    - For instance, in a purely 32-bit fixed-length instruction set, every instruction is 32 bits long, no more and no less. When the CPU fetches an instruction from memory, it always fetches 32 bits at a time, decodes it, and then executes it.
    - The advantage here is simplicity in decoding, as the CPU always knows the size of the instruction ahead of time.

2. **Variable-Length Instruction Set** (like x86):
    - Instructions can vary in length. Some might be as short as 8 bits, while others might be 16, 32, or even longer.
    - The CPU's instruction decoder has to first determine the length of the instruction before fully decoding and executing it. This is typically done by reading certain key bits of the instruction that indicate its format and length.
    - This can provide more code density (more compact code), as simpler operations don't need to use up as much space as more complex ones. But it also adds complexity to the decoding process.

### Portability Issues:
In the early days of computing, a program written and compiled for one CPU architecture couldn't run on another architecture because the binary encodings of the instructions were different.
This lack of compatibility was a barrier to software portability, leading to higher development costs. If developers wanted their software to run on different architectures, they often had to rewrite and recompile it for each one.

## Assembly Language

Much `easier to read and write` than machine language. However, the CPU can not understand assembly language directly. Instead, the assembly program must be translated into machine language before it can be executed by the computer. This is done by using a program called an assembler.

- Assembly language `still isn’t very portable` -- a program written in assembly for one CPU will likely not work on hardware that uses a different instruction set, and would have to be rewritten or extensively modified.

## High-Level Language

To address the $\textcolor{orange}{\text{readability}}$ and $\textcolor{orange}{\text{protability}}$ concerns, new programming languages such as C, C++, Pascal (and later, languages such as Java, Javascript, and Perl) were developed. These languages are known as high-level languages.

- High-level languages are `portable`, meaning that they can run on different types of hardware with little or no modification.

    - Portability is achieved by using a compiler to translate the high-level language program into the machine language of the target computer.

## Why doesn't Python compile directly to machine code if it's faster?:

- `Portability`: Bytecode is platform-independent. You can take the same bytecode and run it on any system with a Python interpreter, be it Windows, Linux, or macOS.
- `Flexibility & Development Ease`: The dynamic features of Python (like dynamic typing, introspection, and eval/exec functionalities) are more naturally suited to an interpreted environment. `Compiling such features to machine code would complicate the compiler and potentially reduce some of the language's flexibility.`
- `Safety`: By interpreting bytecode within a virtual machine (PVM), Python can provide safety features like `bounds checking on lists` and `garbage collection`.
# Introduction

## Key terms and concepts

### Boot Up: Computer Startup Process

**Boot up** refers to the process by which a computer starts up and initializes its system software and hardware components. When you turn on a computer or restart it, the system undergoes a series of steps to load the operating system and prepare it for user interaction. This process includes:

- **Powering on** the hardware components.
- The **BIOS (Basic Input/Output System)** performing initial hardware checks and starting the bootloader.
- The **bootloader** locating and starting the operating system.
- The **operating system** loading drivers and system services.
- **User login** and the start of the user environment.

In simpler terms, "boot up" is the journey your computer takes from being turned off to being ready for use.

### BIOS (Basic Input/Output System)

The **BIOS** (Basic Input/Output System) is a program stored in a ROM (Read-Only Memory) chip on the motherboard. It is the first program that runs when you turn on your computer. The BIOS performs a series of checks, known as the **POST (Power-On Self-Test)**, to ensure that all the hardware components are functioning properly. If everything is in order, the BIOS identifies the boot device, loads the **bootloader** from it into the computer's RAM (Random Access Memory), and then hands over control to the bootloader to continue the boot process.

#### Key Functions Explained

- **POST (Power-On Self-Test)**: This function tests the hardware components of the system before loading the operating system. It ensures that all hardware components are functioning correctly before the boot process continues.

- **Bootstrap Loader**: The bootstrap loader's role is to locate a capable operating system on the storage devices. Once it identifies a valid operating system, the BIOS transfers control to it, allowing the OS to load and run.

- **BIOS Drivers**: These are low-level drivers that provide the system with basic control over its hardware components. They enable fundamental interactions between the system's software and hardware, such as displaying text on the screen during the early boot stages.

- **BIOS Setup**: This is a configuration utility that allows users to modify system hardware settings. Through the BIOS setup, users can adjust settings like the system time, date, boot sequence, and set up passwords for added security.

### Terminal

It's a program called a terminal emulator. This is a program that opens a window and lets you interact with the shell.


**Terminal Behavior with Ctrl+C**

1. **Signal Generation**:
   - When you press `Ctrl+C`, the terminal generates a `SIGINT` (interrupt signal).
   
2. **Signal Delivery**:
   - This signal is delivered to the foreground process group associated with the terminal. In the context of running processes, this means the currently executing command and any child processes it may have spawned.

3. **Default Behavior**:
   - If not otherwise handled, the `SIGINT` signal will terminate processes in the foreground process group.

4. **Input Buffer Clearance**:
   - The terminal's input buffer (where keystrokes are temporarily stored before being sent to the foreground process) is cleared. This means any unsent characters typed before pressing `Ctrl+C` are discarded.

5. **Visual Feedback**:
   - Often, the terminal will move to a new line after detecting `Ctrl+C`, providing visual feedback to the user that the interrupt was recognized.

6. **Return to Ready State**:
   - If a shell was running, it typically displays a new command prompt, indicating it's ready for the next command.


### Shell

Simply put, the shell `(command-line interpreter)` is a program that takes commands from the keyboard and gives them to the operating system to perform. 

#### PATH

The `PATH` variable is a fundamental environment variable in Unix-like operating systems, including Linux. It plays a crucial role in determining where the shell looks for executable files when you type a command in the terminal.

Here's how it works:

1. When you enter a command in the terminal, the shell (e.g., Bash, Zsh) tries to find the corresponding executable file for that command.
2. The shell looks in each directory listed in the PATH variable, in order from left to right, until it finds a matching executable file. It searches these directories one by one until it either finds the executable or exhausts the list of directories.
3. If the shell finds the executable, it executes the command. If it doesn't find the executable in any of the directories listed in PATH, it will display an error message indicating that the command is not found.

> `:$PATH`: This is the crucial part of the command. It appends the current value of the `PATH` variable to the end of the new `PATH` you are setting. The colon (`:`) acts as a separator between the new directory (`/usr/local/mysql/bin/`) and the existing directories in the `PATH`.


## Threads and Processes

[Good video](https://www.youtube.com/watch?v=exbKr6fnoUw)

[Okay video](https://www.youtube.com/watch?v=4rLW7zg21gI&t=117s)

A thread is a unit of execution within a process. In computing, a thread is the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is typically a part of the operating system. Multiple threads within a process share the same data space, which allows them to communicate more easily with each other than if they were separate processes.

### Characteristics of Threads:

1. **Lightweight**: Threads are lighter than processes, meaning they require less overhead to create and destroy.
  
2. **Shared Memory Space**: All threads of a process share the same memory space, including code, data, and files.

3. **Context Switching**: Threads have faster context switching compared to processes.

4. **Communication**: Inter-thread communication is easier and faster than inter-process communication.

## API and ABI


📝 **Note: Definition of API**

An API (Application Programming Interface) serves as a bridge between two different software applications, allowing them to communicate and exchange data or functionalities. It defines the methods and data formats that applications can use to request and exchange information.




$\textcolor{red}{\text{}}$  


## DLL (Dynamic Link Library)

A "DLL" stands for "Dynamic Link Library." It is a feature of the Windows operating system and represents a file that contains code and data that multiple programs can use simultaneously. Here's a detailed breakdown:

1. **Purpose of DLLs**:
   - **Code Reusability**: DLLs allow developers to create modular programs where a module can be a DLL that multiple programs can use.
   - **Efficient Memory Usage**: Since multiple programs can share a single copy of a DLL in memory, it reduces redundancy and saves memory.
   - **Easier Updates**: If a function in a DLL needs to be updated or fixed, it can be done without affecting the programs that use the DLL. Once the DLL is updated, all programs using it will benefit from the update.

2. **Dynamic Linking**:
   - Unlike static linking, where program code is combined with library code into a single executable file, dynamic linking allows a program to call functions from a DLL that is separate from the program itself.
   - The linking occurs at runtime when the program is executed, not at compile time.

3. **Structure**:
   - A DLL can define two kinds of functions: exported and internal. The exported functions are intended to be called by other applications, while internal functions are meant for use only within the DLL itself.

4. **Loading & Unloading**:
   - DLLs are loaded into memory by a program when needed and are unloaded when no longer required. This dynamic loading and unloading provide flexibility but also requires careful management to ensure that resources are properly allocated and freed.

5. **File Extension**:
   - DLL files have the `.dll` file extension.

6. **Potential Issues**:
   - **DLL Hell**: This is a term used to describe complications that arise from using multiple versions of a DLL. If different programs require different versions of a DLL, it can lead to version conflicts and software errors.
   - **Security**: Malicious software can exploit certain vulnerabilities by replacing a legitimate DLL with a malicious one, a technique known as "DLL Hijacking."

In summary, DLLs are a crucial component of the Windows operating system, allowing for modular, efficient, and flexible software design. However, they also come with challenges that developers need to be aware of and manage appropriately.



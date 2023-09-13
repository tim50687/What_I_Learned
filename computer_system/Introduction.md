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

### Shell

Simply put, the shell `(command-line interpreter)` is a program that takes commands from the keyboard and gives them to the operating system to perform. 

#### PATH

The `PATH` variable is a fundamental environment variable in Unix-like operating systems, including Linux. It plays a crucial role in determining where the shell looks for executable files when you type a command in the terminal.

Here's how it works:

1. When you enter a command in the terminal, the shell (e.g., Bash, Zsh) tries to find the corresponding executable file for that command.
2. The shell looks in each directory listed in the PATH variable, in order from left to right, until it finds a matching executable file. It searches these directories one by one until it either finds the executable or exhausts the list of directories.
3. If the shell finds the executable, it executes the command. If it doesn't find the executable in any of the directories listed in PATH, it will display an error message indicating that the command is not found.

> `:$PATH`: This is the crucial part of the command. It appends the current value of the `PATH` variable to the end of the new `PATH` you are setting. The colon (`:`) acts as a separator between the new directory (`/usr/local/mysql/bin/`) and the existing directories in the `PATH`.




$\textcolor{red}{\text{}}$  
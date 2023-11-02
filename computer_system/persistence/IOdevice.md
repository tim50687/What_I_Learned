# I/O device

## System Architecture

- `CPU` attached to the main memory of the system via some kind of memory bus.

- `Some device` connected to the system via a general-purpose I/O bus, which in many modern systems would be PCI.

- Finally, we have `peripheral bus`, such as SCSI, USB, or FireWire. These connect slow devices to the system, including disk drives, mice, keyboards, and so on.
    - a `peripheral bus` is a computer bus designed to support computer peripherals like printers and hard drives.

## Memory Bus

`Bus` = a collection of wires through which data is transmitted.

<p align = "center">
<img src = "../images/bus.png" style = "width:500; border:0">
</p>

## PCI (Peripheral Component Interconnect)

Developed by Intel Corporation, the Peripheral Component Interconnect standard (PCI) is an industry-standard, high-speed bus found in nearly all desktop computers. PCI slots allow you to install a wide variety of expansion cards including:

- Graphics or Video cards
- Sound cards
- Network cards
- SCSI cards
- Many other types of cards

## PCI Express 

[good video](https://www.youtube.com/watch?v=PrXwe21biJo)

Higher spped version of PCI.

### PCI Express Lanes

Data is communicated to and from PCIE cards through lanes. Each lane consists of two pairs of wires, one for receiving and one for transmitting. The number of lanes, or data paths, directly relates to the card's bandwidth. The more lanes there are, the more bandwidth the card will have.


## CPU interact with I/O device

1. We can use `interrupts` to signal the CPU when an I/O device is ready to transfer data.

- Without interrupts, the system simply polls the I/O device to see if it is ready to transfer data. This `polling(Checking the status register, basically just asking it what is going on)` wastes CPU cycles.

- With interrupts, the I/O device signals the CPU when it is ready to transfer data. The CPU can then do other work until the I/O device is ready.

2. DMA

Unfortunately, there is one other aspect of our canonical protocol that requires our attention. In particular, when using programmed I/O (PIO) to transfer a large chunk of data to a device, the CPU is once again over- burdened with a rather trivial task, and thus wastes a lot of time and effort that could better be spent running other processes.

This passage discusses the issue of data transfer between the CPU, memory, and peripheral devices in computer systems and introduces the concept of Direct Memory Access (DMA) as a solution to improve the efficiency of data movement.

- **Problem with Programmed I/O (PIO):** The text begins by highlighting a problem with programmed I/O (PIO). PIO is a method of data transfer where the CPU is responsible for moving data between memory and a device one word at a time. This process is illustrated in the timeline:

- **The Need for DMA:** To address the inefficiency of PIO, the text introduces Direct Memory Access (DMA). DMA is a mechanism that allows data transfer between devices and main memory with minimal CPU intervention. It offloads the task of moving data to a specific DMA engine or controller.

- **How DMA Works:** DMA works by programming the DMA engine with specific instructions. When data needs to be transferred, the operating system instructs the DMA engine by specifying where the data resides in memory, how much data to copy, and which device to send it to. Once programmed, the DMA engine takes over the data transfer, and the CPU is freed up for other tasks. When the transfer is complete, the DMA controller raises an interrupt to notify the OS.


**Key Points:**

- PIO involves the CPU manually moving data between memory and devices, which can be inefficient.

- DMA offloads data transfer tasks from the CPU to a DMA engine, allowing the CPU to focus on other processes.

- DMA is programmed with data transfer instructions and operates independently, raising an interrupt when the transfer is complete.

- DMA improves CPU utilization and system efficiency by minimizing CPU involvement in data movement tasks.

> Instead of the CPU manually performing data transfer tasks like reading from or writing to peripheral devices or memory, the CPU can instruct the DMA (Direct Memory Access) controller to handle these data transfer operations. The DMA controller operates independently of the CPU, and once programmed with the necessary instructions, it can efficiently move data between memory and peripheral devices without direct CPU involvement. This offloading of data transfer tasks to the DMA controller allows the CPU to focus on executing other processes or tasks concurrently. It improves overall system efficiency by reducing CPU overhead and maximizing CPU utilization for processing tasks other than data movement.
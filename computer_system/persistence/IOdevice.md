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
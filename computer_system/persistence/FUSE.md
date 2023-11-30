# FUSE
[Good Intro video](https://www.youtube.com/watch?v=i3YJK3es-iQ)

Filesystem in Userspace (FUSE) is a way to create a file system in a user-space program, rather than in the kernel space.

2. **Kernel Space vs. User Space:**
   - **Kernel Space:** This is where the core of the operating system (OS) runs. It has complete control over everything in the system.
   - **User Space:** This is where user applications run. It's separate from kernel space for security and stability; if something goes wrong in a user-space program, it doesn’t crash the entire OS.

3. **Challenges with Traditional File Systems:**
   - Writing a file system in kernel space is complex and risky. It's difficult to develop and debug because errors can crash the entire system.

4. **FUSE to the Rescue:**
   - FUSE allows creating a file system in user space, which means it's easier to write and debug, and less risky for system stability.
   - With FUSE, a file system is developed as a regular user-level application, not as part of the kernel. This makes it more accessible for developers.

5. **How FUSE Works:**
   - When a program (like `ls` or `mkdir`) makes a call to a file system operation (like opening a file), the request goes to the kernel.
   - If the file is on a FUSE file system, the kernel forwards this request to the FUSE kernel module.
   - The FUSE kernel module then passes the request to the user-space program that implements the FUSE file system.
   - The user-space program processes the request (like reading a file) and returns the result back through the FUSE module to the kernel, which then sends it back to the program that made the initial request.

6. **Benefits of FUSE:**
   - **Simplicity:** FUSE provides a simpler interface for file system operations.
   - **Safety:** Since it runs in user space, it's less likely to cause system crashes.
   - **Flexibility:** It allows for the creation of innovative and non-standard file systems without needing to modify or add code to the kernel.

In essence, FUSE makes it possible to develop and use complex file systems without having to delve into the more risky and intricate kernel space.

## Mount

### file system

 can be understood in two complementary ways in the context of computers, which might be causing the confusion:

1. **File System as Code (Software Component)**: 
   - In one sense, a file system is indeed a set of software or code that manages how data is stored and retrieved on a storage device. This code implements the rules and structures (like directories, inodes, file allocation tables, etc.) that determine how data is organized on the disk.
   - It includes the algorithms for operations like creating and deleting files, reading and writing data, managing space on the disk, and keeping track of where everything is stored.
   - Examples include NTFS (used by Windows), ext4 (used by many Linux distributions), HFS+ (used by macOS), FAT32 (common in USB flash drives), etc.

2. **File System as a Storage Structure (Physical or Logical Component)**:
   - The term file system also refers to the layout of the data on the storage medium (like a hard drive, SSD, or USB stick) managed by the aforementioned software. This includes the organization of files, directories, and the metadata that describes them on the disk.
   - When you format a storage device with a particular file system type, you are essentially organizing that device's storage space according to the rules and structures dictated by that file system's code.

#### Mounting in Context

- When we talk about "mounting" a file system, we're referring to the process of making a particular storage structure (the second definition) accessible through the computer's operating system, using the software component (the first definition) of the file system.
- For instance, when you insert a USB drive into a computer and access its contents, the operating system uses the file system code to interpret the organized data on the drive and integrates it into its own file directory structure, making it accessible for use.

#### Summary

So, in summary, a file system is both a set of code that governs how data is stored and a way of structurally organizing data on a storage device. The process of mounting makes the data on a storage device accessible in a way that is consistent with the rules and structures defined by the file system's code.

### Note on File System Mounting

**Overview of Mounting**: 
- Mounting a file system involves integrating the file system of a storage device (like a disk image) into the host system's directory tree. This process makes the contents of the storage device accessible as part of the host system's file hierarchy.

**File System's Role**: 
- Each file system (e.g., ext4, NTFS, FAT32) has unique rules and structures for organizing data. The file system's software is responsible for understanding these structures.
- When a device with a certain file system is mounted, the operating system utilizes the corresponding file system code to manage and interpret the data on the device.

**Interpreting Disk Structure**: 
- The file system code knows how to navigate its specific layout, including data blocks, inodes, directories, and files.
- Different file systems have different ways of organizing data, and the appropriate file system code is used for each type.

**Mounting Process**: 
- During mounting, the operating system links the file system on the disk to a mount point in the system's directory tree.
- After mounting, files and directories on the disk can be accessed as if they were part of the local file system, via the mount point.

**Example with Disk Image**: 
- When mounting a disk image, the OS uses the file system code relevant to the file system within the image, making its contents accessible at the mount point.

**Responsibility of OS and File System Code**: 
- The operating system's kernel contains the code (drivers) for various file systems, enabling it to read and write data according to the file system's structure.
- For custom or user-space file systems (like FUSE-based systems), a user-space program provides the logic for file system interactions.

**Summary**: 
- Mounting is a crucial process that allows a storage device's file system to be accessed and managed as part of the host's directory structure. The operating system, through its file system drivers or user-space programs, handles the intricacies of different file systems during this process.

### Stackoverflow Answer

Unix systems have a single directory tree. All accessible storage must have an associated location in this single directory tree. This is unlike Windows where (in the most common syntax for file paths) there is one directory tree per storage component (drive).

Mounting is the act of associating a storage device to a particular location in the directory tree. For example, when the system boots, a particular storage device (commonly called the root partition) is associated with the root of the directory tree, i.e., that storage device is mounted on / (the root directory).

It's worth noting that mounting not only associates the device containing the data with a directory, but also with a filesystem driver, which is a piece of code that understands how the data on the device is organized and presents it as files and directories.

Let's say you now want to access files on a CD-ROM. You must mount the CD-ROM on a location in the directory tree (this may be done automatically when you insert the CD). Let's say the CD-ROM device is /dev/cdrom and the chosen mount point is /media/cdrom. The corresponding command is

mount /dev/cdrom /media/cdrom
After that command is run, a file whose location on the CD-ROM is /dir/file is now accessible on your system as /media/cdrom/dir/file. When you've finished using the CD, you run the command umount /dev/cdrom or umount /media/cdrom (both will work; typical desktop environments will do this when you click on the “eject” or ”safely remove” button).

Mounting applies to anything that is made accessible as files, not just actual storage devices. For example, all Linux systems have a special filesystem mounted under /proc. That filesystem (called proc) does not have underlying storage: the files in it give information about running processes and various other system information; the information is provided directly by the kernel from its in-memory data structures.
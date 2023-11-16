# Very Simple File System

The file system is pure software. It is a layer of software that sits on top of the disk hardware and provides a higher-level interface to the user.

## Overview

- Data region: A region of the disk that stores file data.

- Inode region: A region of the disk that stores inodes.

- Allocation bitmap: A bitmap that tracks which blocks are free and which are in use.

- Superblock: A region of the disk that stores metadata about the file system.

### Inodes

Given an i-number, you should directly be able to calculate where on the disk the corresponding inode is located.

- How it refers to where data blocks are located?
    - Direct pointers
        - Each pointer refers to one disk block that belongs to the file.

> However, to support bigger files, we need to use more than one disk block for a file. We can use indirect pointers to support this.

### Understanding the Basic Parameters

- **Block Size:** 4 KB (or 4096 bytes).
- **Pointer Size:** 4 bytes.
- **Number of Pointers per Block:** \( \frac{4096 \text{ bytes}}{4 \text{ bytes/pointer}} = 1024 \text{ pointers/block} \).

### Direct Pointers

- **12 Direct Pointers:** Each pointing to a 4 KB block.
- **Total Size with Direct Pointers:** \( 12 \times 4 \text{ KB} = 48 \text{ KB} \).

### Single Indirect Pointer

- **1 Indirect Pointer:** Points to a block containing 1024 pointers.
- **Each of These Points to a 4 KB Block:** \( 1024 \times 4 \text{ KB} \).
- **Total Size with Single Indirect Pointer:** \( 1024 \times 4 \text{ KB} = 4096 \text{ KB} \) or 4 MB.

### Double Indirect Pointer

- **1 Double Indirect Pointer:** Points to a block containing 1024 pointers.
- **Each of These Points to Another Block of 1024 Pointers:** \( 1024 \times 1024 \) pointers in total.
- **Each of These Points to a 4 KB Block:** \( 1024 \times 1024 \times 4 \text{ KB} \).
- **Total Size with Double Indirect Pointer:** \( 1024 \times 1024 \times 4 \text{ KB} = 4,194,304 \text{ KB} \) or approximately 4 GB.

### Triple Indirect Pointer

Now, let's calculate the size a file can reach with a triple indirect pointer:

- **1 Triple Indirect Pointer:** Points to a block containing 1024 pointers.
- **Each of These Points to a Block of 1024 Double Indirect Pointers:** \( 1024 \times 1024 \) pointers per block.
- **Each Double Indirect Pointer Points to 1024 Blocks of 4 KB:** \( 1024 \times 1024 \times 1024 \times 4 \text{ KB} \).

### Total Calculation

The total size a file can handle with all these pointers is:

- **Direct + Single Indirect + Double Indirect + Triple Indirect:** 
  \( 12 \times 4 \text{ KB} + 1024 \times 4 \text{ KB} + 1024^2 \times 4 \text{ KB} + 1024^3 \times 4 \text{ KB} \).

Let's calculate the total size.

The total file size that can be handled with the addition of a triple indirect pointer is approximately 4,299,165,744 KB, which is about 4100 GB (or 4 TB). This demonstrates the vast capacity for file size that can be achieved through the multi-level index approach in file systems.

## Directory Structure

- Storage of Directories
    - Directories as Files: Directories have inodes and are stored like files, with the type field in the inode marked as “directory.”
    - Data Blocks for Directory Data: The directory's entries are stored in data blocks (and potentially indirect blocks) that the directory's inode points to.

## Read and Write

All traverse begin at the root directory.

Usually the root directory is stored in a fixed location on the disk, so the file system can find it. Must be "well-known" to the file system.

### Read example

#### 1. Open the File (`open("/foo/bar", O_RDONLY)`)

1. **Read Root Inode:**
   - Start at the root of the file system (`/`).
   - Read the inode of the root directory. This is often a well-known inode number (usually 2 in UNIX file systems).
   - This step involves reading the block containing inode number 2.

2. **Read Root Directory Data:**
   - Once the root inode is read, the file system uses pointers within it to find data blocks containing the contents of the root directory.
   - Read these data blocks to locate the directory entry for `foo`.

---
##### How to find inode of /foo?

###### Directory Entries

- **List of (Name, Inode Number) Pairs:** A directory's data blocks contain entries, each consisting of a file or subdirectory name and its associated inode number.

###### Process of Finding `foo`'s Inode

1. **Start at Root (`/`):** The file system always starts at the root directory when you provide an absolute path like `/foo/bar`.

2. **Read Root Inode:** The file system first reads the inode of the root directory. This inode contains pointers to the data blocks of the root directory.

3. **Read Root Directory's Data Blocks:** These data blocks contain entries for each file and subdirectory directly under the root. These entries are essentially a list of names (like `foo`, `bar`, etc.) and their corresponding inode numbers.

4. **Locate `foo` Entry:** The file system scans these entries to find the one for `foo`. This entry will have the name `foo` and its associated inode number.

5. **Access `foo`'s Inode:** Once found, the file system uses the inode number for `foo` to access its inode. This inode will then provide information about where `foo`'s data blocks (or directory entries if `foo` is a directory) are located.

---

3. **Read Inode of `/foo`:**
   - Find the inode number of `foo` from its directory entry.
   - Read the block containing the inode of `foo`.

4. **Read `/foo` Directory Data:**
   - Use pointers in the inode of `foo` to find its directory data blocks.
   - Read these data blocks to find the entry for `bar`.

5. **Read Inode of `/foo/bar`:**
   - Find the inode number of `bar`.
   - Read the block containing the inode of `bar`.

#### 2. Read the File (`read()`)

1. **First Read Operation:**
   - Use the inode of `bar` to find the location of its first data block.
   - Read the first data block of `bar`.

> After this, you need to update the inode of bar, like: `bar` has been read, so the inode of `bar` should be updated to reflect that the file has been accessed. Or time stamps should be updated. Basically the metadata of the file should be updated.

2. **Subsequent Reads:**
   - For reading additional blocks (as `bar` is 12KB, it spans 3 blocks), the file system will consult the inode to locate each block.
   - Read the second and third data blocks of `bar`.

#### 3. Close the File

- **No Read Operation Required:** Closing the file (`close()`) typically does not involve reading from the disk. It mainly involves deallocating the file descriptor in the open-file table of the process.

### Write example

Certainly! Writing a file to disk, especially creating a new file and writing data to it, involves a series of steps that require multiple Input/Output (I/O) operations. Let's break down these steps for the example of creating and writing to a file at `/foo/bar`:

#### 1. Creating the File (`create("/foo/bar")`)

1. **Read Inode Bitmap:**
   - To find a free inode for the new file.
   - This operation identifies an unused inode that can be allocated to `bar`.

2. **Write to Inode Bitmap:**
   - To mark the found inode as allocated.
   - This updates the bitmap to reflect that the inode is no longer available for other files.

3. **Write to New Inode:**
   - To initialize the inode for `bar`.
   - This includes setting up metadata like file size, permissions, and pointers to data blocks (initially empty).

4. **Read Directory Inode:**
   - To access the inode of the parent directory (`foo`).
   - Necessary for updating the directory with the new file entry.

5. **Write to Directory Data:**
   - To add an entry for `bar` in the `foo` directory.
   - This involves writing the name `bar` and its inode number to one of `foo`'s data blocks.

6. **Write to Directory Inode:**
   - To update the inode of the directory `foo`, reflecting the changes in its data blocks.

#### 2. Writing Data to the File (`write()` Operations)

For each block of data written to `bar`:

1. **Read Data Bitmap:**
   - To find a free data block to allocate to `bar`.
   - Necessary for determining where to store the new data on disk.

2. **Write to Data Bitmap:**
   - To mark the selected data block as used.
   - Updates the bitmap to reflect the allocation of this block to `bar`.

3. **Read `bar` Inode:**
   - To access the inode of `bar` for updating its data block pointers.
   - Necessary to associate the newly allocated data block with `bar`.

4. **Write to `bar` Inode:**
   - To update `bar`'s inode with the location of the new data block.
   - This step ensures the inode points to the correct data blocks where `bar`'s content is stored.

5. **Write to Data Block:**
   - To write the actual data to the allocated block.
   - This is where the content of `bar` is physically stored on disk.

#### 3. Closing the File

- **No I/O Operation Required:** Typically, closing the file does not involve disk I/O operations. It mainly involves updating the file system's in-memory structures.



## Caching and Buffering

Most file systems aggresively use DRAM to cache data.

- **Caching:** The process of storing data in a cache.

- **Buffering:** The process of temporarily storing data in a buffer.

## Mounting

### Step-by-Step Example of Mounting a USB Drive

#### 1. Connect the USB Drive

- **Physical Connection:** Plug the USB drive into the computer. The operating system's USB drivers detect the new device.

#### 2. Device Recognition

- **Device Detection:** The operating system detects the new device and assigns it a device identifier, such as `/dev/sdb1`.

#### 3. Choosing a Mount Point

- **Mount Point Selection:** Decide where in the file system hierarchy you want to access the USB drive's contents. For this example, let's say the mount point is `/mnt/usb`.
- **Create Mount Point:** If the directory `/mnt/usb` doesn't already exist, you create it using a command like `mkdir /mnt/usb`.

#### 4. Mount Command

- **Issue Mount Command:** Run the command `mount /dev/sdb1 /mnt/usb`. This tells the operating system to mount the device identified as `/dev/sdb1` at the `/mnt/usb` directory.

   -  When a storage device is mounted, it is assigned a specific location in the file system hierarchy, known as a mount point. This is a directory through which all files on the storage device are accessed.

#### 5. Filesystem Driver Association

- **Driver Involvement:** The operating system uses the appropriate filesystem driver (ext4 in this case) to read the filesystem's metadata from the USB drive. This step is crucial for the OS to understand how to interact with the data structure on the drive.

   - `Filesystem Driver`: This is a crucial component. A filesystem driver is a piece of software that understands how to read and write data on a storage device according to the rules of a specific filesystem format (such as ext4, NTFS, FAT32, etc.).

#### 6. Accessing Files

- **File System Integration:** Once mounted, the files on the USB drive are accessible through the directory `/mnt/usb`. You can navigate, read, and write files as if they were part of the local file system.

#### 7. File Operations

- **Read/Write:** Perform file operations such as reading, writing, or listing files under the mount point `/mnt/usb`.

#### 8. Unmounting (When Done)

- **Unmount Command:** When you're finished using the USB drive, you unmount it with the command `umount /mnt/usb`. This step is important to ensure all file operations are completed and the filesystem is left in a consistent state.
- **Physical Removal:** After unmounting, you can safely remove the USB drive from the computer.

### Additional Notes

- **Automatic Mounting:** In many modern systems, this process can be automatic. When you plug in a USB drive, the system may automatically choose a mount point and mount the filesystem.
- **Filesystem Compatibility:** The operating system must have support for the filesystem used on the USB drive. Most Unix-like systems natively support common filesystems like ext4, NTFS, and FAT32.
- **Permissions and Security:** The mount command may require root privileges, and the system's security settings will determine access permissions for the files on the USB drive.

In this example, the mounting process involves recognizing the USB drive, associating it with a directory (the mount point) in the file system hierarchy, and using the appropriate filesystem driver to interpret and manage the data on the drive.
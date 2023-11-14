# Hard Link

## What is a Hard Link?

The way link() works is that it simply creates another name in the directory you are creating the link to, and associates it with the same inode as the original file. This means that the link and the original file are indistinguishable from each other. If you delete the original file, the link will still work, because the inode still exists. If you delete the link, the original file will still work, because the inode still exists.

### When you create a file...

1. Making a structure(the inode) that will track virtually all relevant information about the file.

2. Linking a human-readable name to that structure. And putting that name in a directory.

### Reference Counting

The inode structure contains a reference count. This is a count of how many links point to this inode. When you create a new link, the reference count is incremented. When you delete a link, the reference count is decremented. When the reference count reaches zero, the inode is deleted, and the space it occupies on disk is freed.

# Symbolic Link (Soft Link)

- Symbolic Link is a special type of file that contains a reference, or a pointer, to another file or directory. It is a third type the file sytem knows about.

- The way symbolic link is formed is by holding the path to the file or directory it points to.


# Inode

## Inode and File Descriptor difference
## Overview
In Unix-like operating systems, files are represented by two key data structures: **inodes** and **file descriptors**.

### Inodes
- **Definition:** Data structures storing information about a file.
- **Contents:** Size, permissions, location on disk, and a unique inode number.
- **Function:** Represent a file in the file system.
- **Lifecycle:** Created with the file for storing metadata; freed for reuse when the file is deleted.
- **Storage:** Persist on disk, not deleted when a file is closed.

### File Descriptors
- **Definition:** Integers referencing open files.
- **Allocation:** Assigned by the kernel when a file is opened.
- **Nature:** Small, non-negative integers.
- **Uses:** Read from, write to, or close the file.
- **Scope:** Each process has its own set of file descriptors.
- **Defaults:** The first three (0, 1, 2) reserved for standard input, output, and error.

### Differences
- **Inode:** Represents a file.
- **File Descriptor:** Represents access to a file, with limited permissions and duration.

### Relationship
1. **Assignment:** Each file has a unique inode number.
2. **Opening Files:** Kernel assigns a file descriptor when a file is opened.
3. **Usage:** File descriptor is used to access the file's inode, which contains file information.

### Additional Data Structures
- Directory entries, indirect blocks, and extents also play roles in file management.


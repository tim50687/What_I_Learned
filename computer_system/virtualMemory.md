# Virtual Memory

## MMU (Memory Management Unit)
- **Definition**: The MMU is a specialized hardware unit within a computer system, often integrated into the CPU or located close to it. Its primary role is to manage and translate virtual addresses into physical addresses.
  
- **Key Components and Registers**:
  - $\textcolor{cyan}{\text{Page Table Base Register (PTBR)}}$: Holds the base address of the page table in memory.
  - $\textcolor{cyan}{\text{Translation Lookaside Buffer (TLB)}}$: A cache that stores recent virtual-to-physical address translations to speed up the translation process.
  - $\textcolor{cyan}{\text{Base and Bound Registers}}$: In systems using base and bounds memory protection, these registers store the base address of a memory segment and its size.

- **Functionality**: While the MMU itself is not a register, it interacts with and uses various registers to perform its address translation and memory management functions.


## **4.1 Base and Bounds Translation**

<p align = "center">
<img src = "images/external_frag.png" style = "width:400; border:0">
</p>


### Traditional Memory Allocation (Base and Bounds):

1. **Variable-sized Blocks**: In the traditional approach, memory is allocated in variable-sized blocks based on the exact amount of memory a program requests. If a program needs 150 units of memory, it gets exactly 150 units.

2. **External Fragmentation**: Over time, as programs start and finish, they release their allocated memory. This can lead to a situation where there are multiple small free blocks scattered throughout memory. If a new program needs a large contiguous block of memory, it might not find a suitable space, even if the total free memory is sufficient. This scattered unusable memory is what's referred to as external fragmentation.

3. **Compaction**: One solution to this fragmentation is to periodically move programs around in memory to group all the free space together. However, this is time-consuming and inefficient.

### Paged Memory Allocation:

1. **Fixed-sized Pages**: Memory is divided into fixed-sized chunks called pages (e.g., 4KB each). When a program needs memory, it's given a number of these pages. If a program needs 150 units and each page is 50 units, it gets three pages.

2. **No Contiguity Requirement**: The key difference is that these pages don't need to be contiguous. One page could be at the start of memory, the second in the middle, and the third at the end. The mapping system in the CPU ensures that these pages appear contiguous to the program.

3. **Elimination of External Fragmentation**: Since each page is the same size, when a program releases memory, the freed pages can be used for any new program, regardless of its size. There's no issue of small gaps of unusable memory because every free page is a standard size and can be used for any new request.


### **Paging and Fragmentation:**

- **External Fragmentation**: Paging effectively addresses the issue of external fragmentation, ensuring that memory can be allocated flexibly without leaving gaps between blocks.

- **Internal Fragmentation**: However, paging introduces a new problem called internal fragmentation. This occurs when the memory allocated using pages doesn't fit perfectly into the page size. For instance:
  - If a program requires 10 KB of memory and the system uses 4KB pages, the system will allocate three pages (12 KB in total). This results in 2KB of wasted space.
  - For larger allocations, this overhead is relatively minor. For example, when hundreds of KB are allocated in 4KB pages, the waste is roughly half a page or 2KB.
  - However, for very small allocations, such as those made by the `new` operator in C++, this overhead can be significant.

- **Huge Pages**: Many modern CPUs support larger page sizes, often referred to as "huge" pages. These can range from multi-megabyte to multi-gigabyte sizes. While they can be more efficient than standard 4KB pages, they are not commonly used due to the increased risk of internal fragmentation.

## 4.3 Paged Address Translation

[good video](https://www.youtube.com/watch?v=6neHHkI0Z0o)

- **32-bit Virtual and Physical Addresses**: In a 32-bit system, the address space is defined by 32 bits. This means that the system can address \(2^{32}\) unique locations, which equates to 4 GB of memory. Each unique location corresponds to a byte in memory.

- **Page Size of 4096 bytes**: The memory is divided into fixed-sized chunks called pages. Each page in this system is \(2^{12}\) bytes, or 4096 bytes (4 KB).

- **Address Division**: The 32-bit address is divided into two parts:
  - **20-bit Page Number**: This identifies which page is being referred to. Since there are \(2^{20}\) possible page numbers (given by \(2^{32}\) total addresses divided by \(2^{12}\) bytes per page), 20 bits are used to represent the page number.
  - **12-bit Offset**: This identifies a specific byte within the chosen page. Since each page is \(2^{12}\) bytes, 12 bits are used to represent the offset within that page.

- **Memory Management Unit (MMU)**: The MMU is responsible for translating virtual addresses (used by programs) to physical addresses (actual locations in memory). When a program wants to access a memory location, it provides a virtual address. The MMU uses the 20-bit page number to find the corresponding physical page in memory and then uses the 12-bit offset to find the exact byte within that page.

- **Page Tables**: Since the MMU needs to map a large number of virtual pages to physical pages, `it uses structures called page tables stored in memory`. These tables contain the mapping information.

**Note**:
$\textcolor{cyan}{\text{32-bit Virtual and Physical Addresses}}$: The system can address \(2^{32}\) unique locations, equating to 4 GB of memory.
$\textcolor{cyan}{\text{Page Size of 4096 bytes}}$: Memory is divided into fixed-sized chunks called pages, each 4 KB in size.
$\textcolor{cyan}{\text{20-bit Page Number and 12-bit Offset}}$: The address is split into a page number and an offset to identify both the page and the specific byte within it.
$\textcolor{cyan}{\text{Memory Management Unit (MMU)}}$: Responsible for translating virtual addresses to physical addresses using page tables in memory.

### Single-level Page Table


- **Page Table Array**:
  - Structure: A simple array with $2^{20}$ entries.
  - Purpose: Each virtual page has an entry, and the value in that entry is the corresponding physical page number.

- **MMU and Page Table Pointer**:
  - The MMU is given a pointer to the page table.
  - This pointer is stored in an MMU register. On Intel-compatible CPUs, this is known as Control Register 3 (CR3).

- **Entry Details**:
  - Each entry contains a P bit to indicate if the entry is "present" or valid.
  - Special null pointers (like in C or Java) cannot be used because 0 is a valid page number.

- **Translation Algorithm**:
  - Pseudo-code representation is provided for the translation algorithm in the MMU using a single-level table.
  - VA (Virtual Address) and PA (Physical Address) are used for address representation.
  - VPN (Virtual Page Number) and PPN (Physical Page Number) represent the page numbers.

- **Memory Operations**:
  - Every memory operation by the CPU requires two physical memory operations:
    1. Translate the virtual address.
    2. Perform the actual memory operation.
  - This process can be inefficient, but the overhead is reduced using the `Translation Lookaside Buffer (TLB)` which caches translations.


**Single-level Page Table and Memory Challenges:**

- The single-level page table is a mechanism used for encoding the virtual-to-physical page map.
- However, it has a drawback: it uses 4 MB of memory for each map.
- In the mid-80s, when Intel introduced CPUs using this paging structure, many computers had only 4 MB of memory or even less. Hence, using such a table was not feasible.
- Fast forward to 2013, a heavily-used machine in the CCIS lab had 4 GB of memory. But with 640 running processes, if each process had a 4 MB page table, it would require 2.5 GB of memory just for these tables. This would consume a significant portion of the machine's total memory.
- An additional challenge is that each of these tables would need a contiguous 4 MB region in memory. This leads to the problem of external fragmentation, which paged address translation was initially designed to solve.

### 2 Level Page Table

**1. Two-Level Page Table:**
Instead of using a single large table to map virtual addresses to physical addresses, a two-level page table uses a hierarchical structure, like a tree. This structure consists of a top-level table (often called the page directory) and multiple second-level tables.

**2. How it Works:**
- The virtual page number (from the virtual address) is divided into two parts: the top ten bits and the bottom ten bits.
- The top ten bits are used to index into the top-level table (page directory). This gives a pointer to one of the second-level tables.
- The bottom ten bits are then used to index into the chosen second-level table. This provides the actual physical address.

**3. Memory Efficiency:**
At first, it might seem that this two-level structure uses just as much memory as a single-level table. However, the advantage comes into play when not all memory is being used:
- If a process only uses a small portion of memory, many entries in the top-level directory will be empty (not used). This means fewer second-level tables are required.
- This design allows processes that use less memory to have smaller page tables, saving space.

**4. Flexibility in Memory Allocation:**
The two-level structure is made up of individual pages. This means:
- You don't need a large contiguous block of memory for the table. Instead, you can use any available 4 KB pages from memory.
- This design avoids the problem of external fragmentation (when large blocks of contiguous memory are wasted).

**5. Page Table Characteristics:**
A key feature of many page table designs is that the page table itself is made up of pages. This means:
- The same pool of free memory pages can be used for both user memory and for the page tables.
- Each sub-table (second-level table) starts at the beginning of a memory page and fits within that page. This design simplifies the process of looking up addresses during translation.

In essence, the two-level page table design provides a more flexible and efficient way to manage memory, especially when not all memory is being used by processes. It allows for better utilization of memory and reduces fragmentation issues.

## 4.4 **Translation Look-aside Buffers (TLBs)**

- **Inefficiency of 2-level Table**: The two-level table address translation is even more inefficient than the single-level table. Despite potential L1 cache hits for MMU memory accesses, the CPU can still experience significant slowdowns.

- **Introduction of TLB**: To combat this inefficiency, a special-purpose cache called the Translation Look-Aside Buffer (TLB) is used. Unlike regular caches that store memory values, the TLB caches mappings from virtual page numbers to physical page numbers.

- **TLB Size**: TLBs are typically small, ranging from 64 mappings on some CPUs to 640 mappings on high-end ones like Core i7 and Xeon E7. This small size is because TLBs need to be extremely fast, given their role in every memory operation.

- **TLB Translation Process**:
  1. Split the virtual address (VA) into a virtual page number (VPN) and offset.
  2. If the VPN is present in the TLB, return the corresponding physical page number (PPN) from the TLB added to the offset.
  3. If not in the TLB, split the VPN into top and bottom parts.
  4. Read the page directory entry (PDE) using the top part.
  5. Read the page table entry (PTE) using the PDE and the bottom part.
  6. Extract the PPN from the PTE.
  7. Add the VPN to PPN mapping to the TLB, potentially evicting another entry.
  8. Return the PPN added to the offset.

- **Performance Implications**: If all actively used code and data fit within the TLB's capacity (e.g., within 2.5MB for a 640-entry TLB), then all translations will be sourced from the TLB, avoiding additional overhead. If the working set exceeds the TLB's capacity, some accesses will miss in the TLB, necessitating in-memory page-table lookups. However, once a mapping is in the TLB, it's likely to be used multiple times before eviction, minimizing the overhead. Additionally, MMU accesses to the page table benefit from caching, speeding up the translation process.

#### **TLB Consistency in Virtual Memory**

- **Overview**: The Translation Look-aside Buffer (TLB) is a specialized cache that holds virtual page number to physical page number mappings. For it to function correctly, it must remain consistent, meaning its entries should accurately reflect the in-memory values (page tables) they cache.

- **Source of Inconsistencies**:
  - **Individual Entry Modifications**: The Operating System (OS) might need to modify a program's address space, such as during demand paging where it maps in new pages and un-maps others. When the OS updates the page table in memory, it must ensure the TLB isn't caching an outdated entry.
  - **Context Switches**: Each process is provided with its own virtual address space by the OS. `The same virtual address can map to different physical memory locations in different processes.` When the OS switches between processes, it updates the CR3 register to point to the new process's address space. It's crucial for security and correctness that the Memory Management Unit (MMU) uses these new mappings and not the old ones.

**Key Takeaway**: Maintaining TLB consistency is vital for ensuring that memory accesses are directed to the correct physical addresses, especially during operations like demand paging and context switches.

##### **Preventing TLB Inconsistencies**

The TLB (Translation Look-aside Buffer) is a cache that stores recent virtual-to-physical address translations to speed up memory access. However, there are situations where the entries in the TLB can become inconsistent or outdated, leading to potential issues.

**1. Issue of Modifications**:
- When the operating system (OS) modifies the page table (which holds the virtual-to-physical address mappings), there's a risk that the TLB might still have old, now-invalid entries.
- **Solution**: The MMU (Memory Management Unit) provides instructions to:
  - Flush (or clear) a specific TLB entry.
  - Flush the entire TLB.
  
  Flushing ensures that outdated entries are removed. However, this can lead to a performance hit since the flushed entries will need to be reloaded from the page table the next time they're accessed. But, as the text mentions, this overhead isn't too significant because the OS doesn't modify the page table very frequently.

**2. Issue with Context Switches**:
- As discussed earlier, each process has its own virtual address space. When the CPU switches from one process to another (a context switch), the TLB entries of the previous process might not be valid for the new process.
- **Solution 1**: Flush the entire TLB every time there's a context switch. This is a straightforward approach and is used by many CPUs. However, it can be inefficient, especially if context switches happen frequently.
  
  The text mentions that with a 500-entry TLB and a 4-level page table, this approach results in discarding the equivalent of 2000 memory accesses worth of work during each context switch.

- **Solution 2**: Use an Address Space ID (ASID). Instead of flushing the TLB, `each TLB entry is tagged with an ASID`, which identifies the process (or context) it belongs to. A special MMU register holds the ASID of the currently running process. TLB entries with a different ASID are ignored, ensuring that entries from one process aren't mistakenly used by another. This approach allows multiple processes' TLB entries to coexist, improving efficiency.

**Key Takeaway**: Ensuring the TLB's consistency is crucial for system correctness. While flushing the TLB is a straightforward solution, it can be inefficient. Using an ASID provides a more efficient way to handle TLB entries across context switches, allowing for better performance.

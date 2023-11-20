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
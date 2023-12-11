# Security

## Protection

Each process has uid and gid, which are used to determine whether the process can access a file or not. 

## Authentication

### Password

The section you've provided discusses the concept of storing passwords in a hashed format and the associated security implications, particularly in the context of dictionary and rainbow table attacks. Here's an explanation:

#### Hashed Password File

1. **Hashing Process**: Instead of storing passwords in plain text, they are put through a cryptographic hash function. This function transforms the password into a fixed-size string (the hash), which is theoretically unique for each password. Importantly, this process is one-way, meaning you can't easily reverse the hash back into the original password.

2. **Verification**: When a user enters their password, the system hashes this input using the same algorithm and compares the result with the stored hash. If the hashes match, the password is deemed correct.

3. **Security Considerations**: Early UNIX systems used this method and considered it secure, especially on slower, non-networked machines. The computational effort required to brute-force (systematically try all possible combinations) a password hash was significant.

#### Dictionary Attacks

1. **Concept**: A dictionary attack is a method to crack passwords by hashing each word in a dictionary and then comparing these hashes against those in the password file. If any user has used a dictionary word as their password, the corresponding hash will match, revealing which account can be accessed with that password.

2. **Efficiency**: This attack is efficient on systems with many users because it increases the likelihood that at least one user has chosen a weak password that appears in the dictionary.

#### Rainbow Tables

1. **Advanced Technique**: Rainbow tables are a more sophisticated tool for cracking hashed passwords. They are precomputed tables that contain a large number of potential plaintext passwords and their corresponding hash values.

2. **Speed**: By using rainbow tables, an attacker can quickly look up the hash of a captured password to find the corresponding plaintext, bypassing the need for real-time computation.

3. **Limitation**: Rainbow tables are effective against basic hash functions but are less effective when additional security measures like salting (adding random data to passwords before hashing) are used.

#### Summary

- **Hashed Passwords**: Storing passwords as hashes is more secure than plain text but not infallible.
- **Dictionary Attacks**: Effective against users with weak, common passwords.
- **Rainbow Tables**: Provide a quick way to reverse-engineer hashes but can be mitigated with techniques like salting.

This discussion highlights the evolution of password storage and cracking techniques, emphasizing the need for robust security practices like using strong, unique passwords and implementing additional measures like hashing with salts.

## Unix Access Control

File and directory have an owner and a group. The owner and group can have read, write, and execute permission. The permission can be set for owner, group, and others.

### Unix File Permissions
In Unix and Unix-like systems, each file and directory has an associated set of permissions that determine who can read, write, or execute them. These permissions are typically divided into three categories:

1. **Owner**: The user who owns the file.
2. **Group**: Users who are part of a group that is assigned to the file.
3. **Others (World)**: All other users on the system.

Each category can have three types of permissions: read (`r`), write (`w`), and execute (`x`). 

### The Provided Scenario
The text describes a situation with an access control list for four entities (`file1`, `file2`, `dir1`, `file3`) and four users (`user1`, `user2`, `user3`, `user4`). The permissions are set differently for each file and user.

#### Problem with `file1`
- **Scenario**: Both `user3` and `user4` need high-level privileges (`rw-`) for `file1`. If they are in the same group, you can set the group permissions to `rw-`. However, this creates a dilemma for setting the "world" permissions.
- **Dilemma**: 
  - If "world" is set to `---`, then `user2` won't have the read access (`r--`) they are supposed to have.
  - If "world" is set to `r--`, then `user1` will have read access, which they shouldn't have according to the access control matrix.

#### Problem with `file3`
- **Scenario**: There are four distinct combinations of permissions required for `file3`, but Unix permissions only allow for three combinations (owner, group, and world).
- **Limitation**: This means it's impossible to accurately represent all four required permission sets within the standard Unix permission model.

### Summary
The limitations highlighted here stem from the fact that Unix permissions are quite basic and not designed for complex access control scenarios. In real-world applications, these limitations can lead to situations where it's not possible to perfectly map an access control matrix to Unix file permissions. This can result in either overly permissive or overly restrictive access to files, depending on how the permissions are set.

To address these limitations, more advanced access control mechanisms like Access Control Lists (ACLs) are used in many systems. ACLs provide a more granular level of control, allowing specific permissions to be set for individual users and groups beyond the basic owner/group/world model.

## Buffer Overflow Attack

good reference: [Buffer Overflow Attack](https://www.youtube.com/watch?v=1S0aBV-Waeo&t=412s)


### Understanding Why Shellcode is Injected Through Buffer Overflow

#### Execution Privileges
- Shellcode often requires high-level privileges for sensitive operations (like accessing `/etc/shadow`).
- Direct execution of such code by a non-privileged user is typically restricted by system security.

#### Exploiting Vulnerabilities
- Buffer overflow attacks exploit vulnerabilities in software that may run with higher privileges.
- The attack overwrites the return address on the stack, redirecting program execution to the shellcode.

#### Bypassing Security Mechanisms
- Modern operating systems have security measures (non-executable stacks, address space layout randomization) that prevent arbitrary code execution.
- Buffer overflow attacks circumvent these protections by hijacking the control flow of a legitimately running program.

#### Context of the Vulnerable Program
- The effectiveness of shellcode can depend on the context in which it's executed.
- Injecting shellcode into a program with higher privileges allows performing actions that are impossible under normal user permissions.

#### Stealth and Avoiding Detection
- Directly running malicious code can be more easily detected by security software.
- Injecting shellcode through a buffer overflow can be more stealthy, appearing as a regular operation of the program until the exploit occurs.

#### Role of SUID in Buffer Overflow Exploits
- SUID (Set User ID) is a special permission that allows a program to run with the privileges of its owner, often root, regardless of the user executing it.
- Buffer overflow vulnerabilities in SUID programs are particularly critical because they can be exploited to run shellcode with root privileges.
- Attackers often target SUID programs for buffer overflow attacks to achieve privilege escalation from a regular user to root.
- Managing SUID permissions and minimizing their use on essential programs is crucial for system security.

In summary, directly running shellcode for privileged operations is typically not possible due to system security restrictions. Buffer overflow attacks exploit vulnerabilities in higher-privileged programs, often those with SUID permissions, to execute shellcode, bypassing normal security mechanisms and gaining unauthorized access or privileges.


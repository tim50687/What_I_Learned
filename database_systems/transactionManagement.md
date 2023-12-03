# Transaction Management

If the transaction is not execute successfully, the transaction is `aborted`. If a transaction is aborted, the database must be restored to the consistent state it was in before the transaction started. This is called `rollback`.

## Consistency (ACID)

### By user and DBMS

- User: Don't do stupid logic

- DBMS: 

#### Example 
DBMS-Enforced Constraints:
- Referential Integrity: Ensures all references within the database are consistent (e.g., no transactions refer to non-existent accounts).
- Domain Constraints: Ensures that data entries fall within specified domains (e.g., account balances are numeric, positive values).
- Check Constraints: Enforces specific rules defined on the columns of tables (e.g., account balance should not go negative).
- Unique Constraints/Primary Keys: Ensures uniqueness where required (e.g., no two accounts have the same account number).



## Concurrency Control Problems

1. `Lost update problem`: An apparently successfully completed updated operation by one user can be overriden by another user's update operation.

2. `Uncommitted dependency problem`: A transaction reads a value that has been updated by another transaction but not yet committed.
    - What is T2 crashes after writing 200 but before committing? T2 has to be rolled back. And what T1 read is not valid anymore.

    - It is also called `dirty read`.

3. `Inconsistent analysis problem`: A transaction reads several values while a second transaction updates some of those values during the execution of the first transaction.

    - T1 and T2 Read X first, but T1 move X to Y, then T2 read Y. The result is not consistent.

4. `Nonrepeatable read problem`: A row is retrieved twice and the values within the row differ between reads.

5. `Phantom problem`: A transaction reads a set of rows that satisfy a search condition. While the transaction is active, a second transaction inserts or `deletes` rows that satisfy the condition. The first transaction then repeats the search, returning a different set of rows.

    - T1 read A, T2 delete A, T1 read A again, the result is different.

## Serializability and Recoverability

> There is no gaurantee that the results of all serial executions of a given set of transaction will be identical.

- `Serial schedule`: A schedule in which the operations of each transaction are executed consecutively `without any interleaved` operations from other transactions.

- `Serializable schedule`: A schedule that is equivalent to a serial schedule.
    - The objective of serializability is to find nonserial schedules that allow transactions to execute concurrently without interfering with each other, and thereby produce a database state that could be produced by some serial schedule.


### Conflicting operations
Two operations are said to be in conflict, if they satisfy all the following conditions:

1. Both the operation should belong to different transactions.

2. Both the operations are working on the same data item.

3. At least one of the operation is a write operation.


> The order of non-conflicting operations has no effect on the final state of the database.

A `conflict serializable schedule` orders any conflicting operations in the same way as some serial schedule.

- A schedule is called `conflict serializable` if it can be converted into a serial schedule by swapping only non-conflicting operations. This is because swapping non-conflicting operations will not change the final state of the database.
- Importantly, `conflicting operations cannot be swapped`. Conflicting operations are those where at least one operation is a write, and both operations involve the same data item but are from different transactions. Swapping conflicting operations would indeed change the final state of the database, violating the integrity of the transactions.


### Why Conflict Serializable Schedules?
Conflict Serializable schedules are sought in database systems primarily for these reasons:

1. **Data Integrity**: They ensure that the final state of the database is the same as if the transactions were executed in a serial order, maintaining consistency and integrity of data.

2. **Optimized Performance**: Conflict Serializable schedules allow for concurrency, letting multiple transactions process simultaneously, which enhances performance and throughput.

3. **Practicality**: They strike a balance between strict serial execution (which can be inefficient) and the need for data consistency, making them a practical choice for real-world applications.

4. **Ease of Implementation**: Determining and managing conflict serializability is relatively simpler and more efficient compared to full serializability, often using common techniques like two-phase locking.

5. **Scalability**: By enabling a controlled level of concurrency, these schedules allow database systems to scale effectively, handling more transactions without compromising data integrity. 

In essence, conflict serializable schedules are crucial for maintaining data correctness in a more efficient and scalable manner than strict serial execution.

> If precedence graph contains a cycle, then the schedule is not conflict serializable.


### Recoverability

A schedule is `recoverable` if for every pair of transactions Ti and Tj such that Tj reads a data item previously written by Ti, the commit operation of Ti appears before the commit operation of Tj in the schedule. 

#### Type of recoverable schedules

- `Strict recoverable schedule`: If in the given schedule, each transaction Tj `neither reads nor writes` any data item ‘x’ until the last transaction Ti that has written ‘X’ is committed or aborted then it is strict.

- `Cascadeless schedule`: A cascadeless schedule is one where, for each pair of transactions Ti and Tj such that Tj `reads` a data item previously written by Ti, the commit operation of Ti appears before the read operation of Tj .

#### What if the the commit does not occur?

We can still recover if the other transactions that read the
uncommitted data have not yet committed, using the `cascading rollback` technique.


## Locking Methods

- Shared lock (S-lock): A lock that allows a transaction to read a data item.

- Exclusive lock (X-lock): A lock that allows a transaction to perform both a read and a write operation on a data item.

Because read operations cannot conflict, it is permissible for several transactions to hold shared locks on the same data item. However, if a transaction holds a shared lock on a data item, no other transaction can obtain an exclusive lock on that data item.

### Two-Phase Locking

A transaction follows the two-phase locking protocol if all locking operations precede all unlocking operations in the transaction.

- `growing phase`: A transaction acquires all the locks it needs without unlocking any data.

- `shrinking phase`: A transaction releases all the locks it holds without requesting any new locks.

There is no requirement that all locks be obtained simultaneously.

> If every transaction in a schedule follows the two-phase locking protocol, then the schedule is guaranteed to be conflict serializable.

#### How 2PL prevents cascading rollback?

1. Release all locks at the end of the transaction.
    - This is called `rigorous 2PL`.

2. Strict 2PL: Holds only the exclusive locks until the end of the transaction. 

### Deadlock

Solution for deadlock:

### 1. Timeout
    - If a transaction waits for a lock for a certain amount of time, it is aborted.

    `Downside`: This approach penalizes long-running transactions and may cause unnecessary aborts.

### 2. Deadlock prevention

#### 1. Wait-Die Algorithm

- **Basic Principle**: In Wait-Die, older transactions are given priority over younger ones.

- **How it Works**:
    - When a transaction (let's call it \( T_x \)) requests a resource (like a lock) that's held by another transaction (\( T_y \)):
        - If \( T_x \) is **older** than \( T_y \) (i.e., \( T_x \)'s timestamp is smaller), \( T_x \) is allowed to wait. The idea is that the older transaction has been in the system longer, so it should be given a chance to complete.
        - If \( T_x \) is **younger** than \( T_y \), \( T_x \) is aborted ("dies") and restarted with the same timestamp. This restart ensures that eventually, \( T_x \) will become the oldest active transaction and will not be aborted in the future due to its age.

- **Advantages**: This method prevents deadlock by ensuring that transactions don't wait indefinitely and that there is a clear hierarchy of transactions based on age.

- **Scenario Example**:
    - Transaction \( T1 \) (older) requests a lock held by Transaction \( T2 \) (younger). \( T1 \) waits.
    - Transaction \( T3 \) (younger) requests a lock held by Transaction \( T1 \) (older). \( T3 \) is aborted and restarted.

#### 2. Wound-Wait Algorithm

- **Basic Principle**: In Wound-Wait, the approach is somewhat reversed compared to Wait-Die. Here, younger transactions are given priority.

- **How it Works**:
    - When a transaction \( T_x \) requests a resource held by another transaction \( T_y \):
        - If \( T_x \) is **older** than \( T_y \), \( T_y \) is aborted ("wounded") to allow \( T_x \) to proceed. The younger transaction \( T_y \) will restart with a larger timestamp.
        - If \( T_x \) is **younger** than \( T_y \), \( T_x \) waits.

- **Advantages**: Like Wait-Die, Wound-Wait prevents indefinite waiting and potential deadlocks, ensuring a system where resource allocation is age-dependent.

- **Scenario Example**:
    - Transaction \( T1 \) (older) requests a lock held by Transaction \( T2 \) (younger). \( T2 \) is aborted and restarted.
    - Transaction \( T3 \) (younger) requests a lock held by Transaction \( T1 \) (older). \( T3 \) waits.

##### Key Differences

- **In Wait-Die**: Older transactions wait for younger ones; younger transactions are aborted and restarted.
- **In Wound-Wait**: Older transactions abort (wound) younger ones to proceed; younger transactions wait for older ones.


### 3. Deadlock Detection

DBMS allows deadlock to occur but recognizes it and breaks it.

Handle by the construction of a `wait-for` graph.

- Create a directed edge from transaction Ti to Tj if Ti is waiting for a data item locked by Tj.

> If the wait-for graph contains a cycle, then a deadlock exists.

## Granularity of Data Items


### Requesting a Lock on a Descendant Node

- **Scenario**: Suppose a transaction requests a lock on a record within a page.
  
- **Process**:
    - The DBMS checks the hierarchy: it looks at the record's parent (the page), the page's parent (the file), and so on up to the database level.
    - If any of these ancestor nodes are already locked by another transaction, the lock request on the record is denied. This is to prevent conflicts, as locking the record while its page or file is locked by another transaction could lead to inconsistencies or deadlocks.

### Requesting a Lock on an Ancestor Node

- **Scenario**: Now imagine a transaction requests a lock on an entire file.

- **Process**:
    - The DBMS must check all the descendants of the file: every page in the file, every record in those pages, and every field in those records.
    - If any of these descendant nodes are already locked by another transaction, the DBMS must decide based on its locking protocol (e.g., wait, deny the lock, abort the transaction holding the lock, etc.) to resolve the conflict. The key is to ensure no current locks on smaller granularities within the file are violated.

## Timestamping Methods

No locks are involved and therefore no deadlocks can occur.


- `Timestamping` : A concurrency control protocol that orders transactions in sucg a way that `older` transactions, transaction with `smaller timestamps`, get priority in the event of conflict.

### Basic timestamp ordering protocol

1. **Transaction Timestamps**:
   - Each transaction \( T \) is assigned a unique timestamp \( ts(T) \) when it starts.
   - Timestamps help order transactions chronologically.

2. **Handling Read Operations**:
   - When \( T \) reads an item \( x \):
     - If \( ts(T) < write\_timestamp(x) \), \( T \) is too late to read the outdated value of \( x \) because a younger transaction has updated \( x \). In this case, \( T \) must be aborted and restarted with a newer timestamp.
     - Otherwise, \( T \) can read \( x \), and \( read\_timestamp(x) \) is updated to the maximum of \( ts(T) \) and the current \( read\_timestamp(x) \).

3. **Handling Write Operations**:
   - When \( T \) writes to an item \( x \):
     - If \( ts(T) < read\_timestamp(x) \), a younger transaction has already read the current value of \( x \), and updating \( x \) now would be incorrect. \( T \) must be rolled back and restarted with a later timestamp.
     - If \( ts(T) < write\_timestamp(x) \), \( T \) is attempting to write an obsolete value to \( x \), as a younger transaction has updated it. \( T \) should be rolled back and restarted with a newer timestamp.
     - Otherwise, \( T \) can write to \( x \), and \( write\_timestamp(x) \) is set to \( ts(T) \).

#### Example for \( ts(T) < write\_timestamp(x) \)

Imagine two transactions, \( T1 \) and \( T2 \), with timestamps 10 and 20, respectively. \( T1 \) (older) wants to write to \( x \) after \( T2 \) (younger) has already updated \( x \):

- \( ts(T1) = 10 \), \( write\_timestamp(x) = 20 \) (set by \( T2 \)).
- \( T1 \)'s attempt to write to \( x \) would be based on the state of \( x \) before \( T2 \)'s update, which \( T1 \) is unaware of.
- Therefore, \( T1 \) is rolled back and restarted with a new timestamp, say 30, to reflect the current state of the database, including \( T2 \)'s updates.


#### Key Characteristics

- **Conflict Serializability**: BTO ensures transactions are executed in a manner equivalent to their chronological order, based on timestamps.
- **Preventing Inconsistencies**: By aborting and restarting transactions that would violate the chronological order of reads and writes, BTO maintains data consistency.
- **Limitations**: BTO does not inherently guarantee recoverable schedules, as it focuses on maintaining conflict serializability.

#### Conclusion

Basic timestamp ordering is a method to control transaction concurrency using timestamps, ensuring that the transactions proceed in a way that avoids conflicts and maintains the consistency of the database. However, it may lead to more transaction restarts and does not automatically ensure recoverable schedules.

### Thomas' Write Rule

- **Basic Principle**: Thomas' Write Rule (TWR) is a timestamp-based concurrency control protocol that uses a simple rule to determine whether a transaction can write to a data item.

- **How it Works**:
    - When a transaction \( T \) wants to write to a data item \( x \):
        - If \( ts(T) < read\_timestamp(x) \), \( T \) is too late to write to \( x \) because a younger transaction has already read the current value of \( x \). \( T \) must be aborted and restarted with a newer timestamp.
        - If \( ts(T) < write\_timestamp(x) \), \( T \) is attempting to write an obsolete value to \( x \), as a younger transaction has already updated it. \( T \) simply ignores the write operation and proceeds without rollback.
        - Otherwise, \( T \) can write to \( x \), and \( write\_timestamp(x) \) is set to \( ts(T) \).


#### What's the Difference Between TWR and BTO?

Thomas's write rule is indeed an extension of the basic timestamp ordering (BTO) protocol, but it introduces a significant modification that enhances concurrency. Let's compare the two to understand the difference:

### Basic Timestamp Ordering (BTO)

In BTO, when a transaction \( T \) attempts to write to a data item \( x \), the following checks are performed:

1. **Read Timestamp Check**:
   - If \( ts(T) < read\_timestamp(x) \), transaction \( T \) is rolled back and restarted with a later timestamp. This check prevents \( T \) from writing a value that could overwrite a more recent read.

2. **Write Timestamp Check**:
   - If \( ts(T) < write\_timestamp(x) \), transaction \( T \) is also rolled back and restarted. This means \( T \) is attempting to write an outdated value to \( x \), as \( x \) has been updated by a younger transaction.

### Thomas's Write Rule

Thomas's write rule modifies the write timestamp check of the BTO:

1. **Read Timestamp Check** (Unchanged):
   - Same as BTO: If \( ts(T) < read\_timestamp(x) \), roll back and restart \( T \) with the later timestamp.

2. **Modified Write Timestamp Check**:
   - If \( ts(T) < write\_timestamp(x) \), instead of rolling back and restarting \( T \), the write operation by \( T \) is simply ignored. This is known as the "`ignore obsolete write rule.`" It's based on the rationale that since a younger transaction has already updated \( x \), the outdated write by \( T \) doesn't need to be applied.

### Key Differences

- **Handling Obsolete Writes**:
  - In BTO, `a transaction is rolled back and restarted if it tries to write an obsolete value.`
  - In Thomas's rule, the `obsolete write operation is ignored`, allowing the transaction to continue without rollback. This enhances concurrency as it reduces the number of transaction restarts.

- **Concurrency and Performance**:
  - Thomas's write rule allows for greater concurrency and potentially better performance by reducing the overhead of transaction rollbacks and restarts.

- **Schedule Types**:
  - While BTO ensures conflict serializability, Thomas's write rule allows for schedules that are view serializable but not necessarily conflict serializable. This means it can validate a broader set of schedules where the order of some non-conflicting operations may be different from their chronological order.

### Conclusion

Thomas's write rule is a modification of the BTO that provides greater concurrency by allowing transactions to proceed even if they attempt to perform obsolete writes. This approach enhances system performance by reducing the frequency of transaction rollbacks.



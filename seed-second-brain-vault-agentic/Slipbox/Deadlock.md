---
creation date: 2024-12-17 18:40
modification date: Tuesday 17th December 2024 18:43:58
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/OS
description:
dg-publish: true
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# What is Deadlock?

A **deadlock** is a situation in multithreading or concurrent programming where **two or more [[Threads]]** are **waiting indefinitely** for resources that are held by each other. None of the [[Threads]] can proceed because they are **blocked** waiting for a resource to be released.

---

## Conditions for Deadlock (Coffman’s Conditions)

Deadlock occurs when all the following conditions hold true:

1. **Mutual Exclusion**:
   - Only one thread can access a resource at a time.

2. **Hold and Wait**:
   - A thread holds at least one resource and is waiting to acquire additional resources held by other [[Threads]].

3. **No Preemption**:
   - Resources cannot be forcibly taken from [[Threads]].

4. **Circular Wait**:
   - A set of [[Threads]] are waiting on each other in a circular chain.

---

## Example of Deadlock

Two [[Threads]] trying to lock two resources in opposite order:

```java
class DeadlockExample {
    static final Object resource1 = new Object();
    static final Object resource2 = new Object();

    public static void main(String[] args) {
        Thread t1 = new Thread(() -> {
            synchronized (resource1) {
                System.out.println("Thread 1: Locked resource 1");
                try { Thread.sleep(50); } catch (InterruptedException e) {}

                synchronized (resource2) {
                    System.out.println("Thread 1: Locked resource 2");
                }
            }
        });

        Thread t2 = new Thread(() -> {
            synchronized (resource2) {
                System.out.println("Thread 2: Locked resource 2");
                try { Thread.sleep(50); } catch (InterruptedException e) {}

                synchronized (resource1) {
                    System.out.println("Thread 2: Locked resource 1");
                }
            }
        });

        t1.start();
        t2.start();
    }
}
```

### Output:
- Both [[Threads]] lock one resource and wait indefinitely for the other resource.

---
## How to Prevent Deadlock?
1.	Avoid Circular Wait:
	- Impose an order on resource acquisition. All [[Threads]] must acquire resources in the same order.

### Example:
```
synchronized (resource1) {
    synchronized (resource2) {
        // Critical section
    }
}
```


2.	Avoid Hold and Wait:
	- Require [[Threads]] to acquire all resources at once.

### Example:
```
synchronized (resource1) {
    synchronized (resource2) {
        // Acquired all resources together
    }
}
```


3.	Use Try-Lock (Timeout Mechanism):
	- Use a timeout when attempting to acquire locks, so [[Threads]] don’t wait indefinitely.

### Example (Java ReentrantLock):

```
Lock lock1 = new ReentrantLock();
Lock lock2 = new ReentrantLock();

if (lock1.tryLock(100, TimeUnit.MILLISECONDS)) {
    try {
        if (lock2.tryLock(100, TimeUnit.MILLISECONDS)) {
            try {
                // Critical section
            } finally { lock2.unlock(); }
        }
    } finally { lock1.unlock(); }
}
```


4.	Resource Allocation Graph:
	- Use resource allocation graphs to detect potential circular waits and avoid deadlock.
5.	Avoid Mutual Exclusion:
	- If possible, design resources so they can be shared without locking (e.g., using immutable data or read-only resources).

# Summary

A deadlock occurs when multiple [[Threads]] are waiting for resources held by each other, causing a circular wait. To prevent deadlock:
- Impose an order on resource acquisition.
- Acquire all resources at once.
- Use timeouts to avoid indefinite waiting.
- Minimize resource locking by using thread-safe designs.

By following these techniques, you can ensure that your multithreaded programs are deadlock-free.


---
# Related Topics
### [[Threads]]
### [[Race Conditions]]



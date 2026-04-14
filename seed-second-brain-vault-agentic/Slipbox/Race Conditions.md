---
creation date: 2024-12-17 18:30
modification date: Tuesday 17th December 2024 18:30:44
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
# What are Race Conditions?

A **race condition** occurs in multithreading or concurrent programming when **two or more [[Threads]] access shared data** and try to modify it **simultaneously**. The outcome depends on the **order of execution**, which can be unpredictable and lead to incorrect results.

---

## Key Characteristics:
1. Occurs when:
   - Multiple [[Threads]] perform **read/write operations** on shared resources.
   - Execution order is not synchronized.
2. Leads to:
   - **Data corruption** or inconsistent results.
   - Hard-to-diagnose bugs.

---

## Example of Race Condition

### Scenario:
Two [[Threads]] increment a shared variable `count`.

```java
class RaceConditionExample implements Runnable {
    int count = 0;

    public void run() {
        for (int i = 0; i < 1000; i++) {
            count++;  // Not synchronized
        }
    }

    public static void main(String[] args) throws InterruptedException {
        RaceConditionExample example = new RaceConditionExample();

        Thread t1 = new Thread(example);
        Thread t2 = new Thread(example);

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println("Final Count: " + example.count);  // Output may vary
    }
}
```

### Issue:
- Both [[Threads]] access count simultaneously.
- count++ (read, increment, write) is not atomic, so values are overwritten.

## How to Prevent Race Conditions?
1.	Synchronization:
	- Use locks or synchronized blocks to control access to shared resources.

### Example:

```
synchronized(this) {
    count++;
}
```

### Example in Python

![[Pasted image 20241224094640.jpg]]


2.	Atomic Variables:
	- Use AtomicInteger or similar classes to ensure thread-safe operations.
3.	Thread Safety Libraries:
	- Use thread-safe collections like ConcurrentHashMap.
4.	Avoid Shared Resources:
	- Minimize sharing of mutable data between [[Threads]].

---
## Real-World Example:

- Multiple [[Threads]] updating a bank account balance without synchronization can result in incorrect totals.

# Summary:

A race condition happens when multiple [[Threads]] access shared resources simultaneously, leading to unpredictable results. It can be prevented using synchronization, atomic operations, or thread-safe mechanisms.


---
# Related Topics
### [[Threads]]
### [[Deadlock]]


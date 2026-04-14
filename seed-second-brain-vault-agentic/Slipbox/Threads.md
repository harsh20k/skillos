---
creation date: 2024-12-17 18:24
modification date: Tuesday 17th December 2024 18:24:54
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/OS
  - slipbox/permaNotes/java
description: 
share_link: https://share.note.sx/3s9vfkj3#ax+i11kc6/dRGkc59Krxrjea1U2e+ZykP7/Gy6wf4m0
share_updated: 2024-12-28T15:42:19+05:30
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
# What are Threads?

A **thread** is the smallest unit of execution within a process. It represents a **lightweight sub-process** that runs independently but shares the same memory and resources as other threads within the same process.

---

## Key Points:

1. **Process vs Thread**:
   - A **process** is a running program with its own memory space.
   - A **thread** is a unit of execution within a process. Threads within a process share:
     - ==Code==
     - ==Data==
     - ==File descriptors==

2. **Multithreading**:
   - Running multiple threads **concurrently** within the same process to achieve parallelism and improved performance.

3. **Benefits**:
   - Efficient use of CPU.
   - Faster context switching compared to processes.
   - Enables tasks like I/O operations and computations to run in parallel.

4. **Disadvantages**:
   - **Thread Safety**: Shared data may lead to [[Race Conditions|race conditions]].
   - Complex debugging and synchronization.

---
### Example (Java):
```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running...");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();  // Start the thread
    }
}

```


## Real-World Use Cases:
- Running background tasks.
- Handling multiple user requests on servers.
- Parallel computation in multi-core processors.

---

# **Threads - Different Ways to Use It in Java**

In Java, threads allow concurrent execution of tasks. There are multiple ways to create and use threads depending on your requirements.

---

## 1. Extending the `Thread` Class

You can create a thread by extending the `Thread` class and overriding its `run()` method.

### Syntax:
```java
class MyThread extends Thread {
public void run() {
System.out.println(“Thread is running…”);
}
}

public class Main {
public static void main(String[] args) {
MyThread thread = new MyThread();
thread.start();  // Starts the thread
}
}
```

### Key Points:
- Simple to implement.
- Not suitable if your class needs to extend another class, as Java supports only single inheritance.

---

## 2. Implementing the `Runnable` Interface

A more flexible way to create a thread is by implementing the `Runnable` interface.

### Syntax:
```java
class MyRunnable implements Runnable {
public void run() {
System.out.println(“Thread is running…”);
}
}

public class Main {
public static void main(String[] args) {
Thread thread = new Thread(new MyRunnable());
thread.start();  // Starts the thread
}
}
```

### Key Points:
- Preferred when you need to extend another class.
- Promotes better design by separating the task logic from the thread logic.

---

## 3. Using Lambda Expressions

For a concise approach, you can use lambda expressions with the `Runnable` interface.

### Syntax:
```java
public class Main {
public static void main(String[] args) {
Thread thread = new Thread(() -> {
System.out.println(“Thread is running…”);
});
thread.start();  // Starts the thread
}
}
```

### Key Points:
- Reduces boilerplate code.
- Useful for simple, one-off thread tasks.

---

## 4. Using the `Callable` Interface with `Future`

The `Callable` interface allows threads to return results and handle exceptions. It works with the `ExecutorService`.

### Syntax:
```java
import java.util.concurrent.*;

public class Main {
public static void main(String[] args) throws Exception {
ExecutorService executor = Executors.newSingleThreadExecutor();
Callable callable = () -> “Thread result”;

    Future<String> future = executor.submit(callable);
    System.out.println(future.get());  // Retrieves the result

    executor.shutdown();
}
}
```

### Key Points:
- Returns a result using `Future`.
- Handles exceptions more effectively than `Runnable`.

---

## 5. Using the `ThreadPool`

Thread pools manage a group of worker threads and are suitable for executing a large number of tasks efficiently.

### Syntax:
```java
import java.util.concurrent.*;

public class Main {
public static void main(String[] args) {
ExecutorService executor = Executors.newFixedThreadPool(3);

    for (int i = 0; i < 5; i++) {
        executor.execute(() -> {
            System.out.println("Thread is running...");
        });
    }

    executor.shutdown();
}
}
```

### Key Points:
- Optimizes thread management for multiple tasks.
- Avoids the overhead of creating and destroying threads repeatedly.

---

## Comparison of Different Approaches

| **Method**                 | **Advantages**                                         | **Disadvantages**                               |
|----------------------------|-------------------------------------------------------|------------------------------------------------|
| **Extending `Thread`**     | Simple to use.                                        | Cannot extend another class.                   |
| **Implementing `Runnable`**| Flexible, allows extending other classes.             | No direct result or exception handling.        |
| **Lambda Expressions**     | Concise and easy for simple tasks.                    | Limited to simple tasks, less readable for complex logic. |
| **`Callable` with `Future`**| Supports returning results and exception handling.    | Slightly more complex to implement.            |
| **ThreadPool**             | Efficient for managing multiple threads.              | Overhead of setting up and managing the pool.  |

---

## Conclusion

Java provides various ways to create and use threads:
1. Extend `Thread` for simple tasks.
2. Implement `Runnable` for flexibility.
3. Use lambdas for concise code.
4. Leverage `Callable` for tasks that require results or exceptions.
5. Employ thread pools for managing a large number of concurrent tasks.

Choose the method based on the requirements of your application.

---
# Related Topics
### [[Type of Threads]]
### [[Race Conditions]]
### [[Deadlock]]

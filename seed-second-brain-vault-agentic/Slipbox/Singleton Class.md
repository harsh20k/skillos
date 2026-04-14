---
creation date: 2024-12-18 15:29
modification date: Wednesday 18th December 2024 15:29:37
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/datastructures
  - slipbox/permaNotes/java
description: 
share_link: https://share.note.sx/ic483uo6#JzJLT8VvF2u4gbUGxa1UEHpZ6BY3aFPIPUYL/Lh5lmA
share_updated: 2024-12-28T14:42:06+05:30
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
# Singleton Class in Java

A **singleton class** is a design pattern in Java where only **one instance** of the class can be created throughout the application's lifecycle. It ensures controlled access to the single instance and provides a global point of access.

---

## Key Features of a Singleton Class

1. **Single Instance**: Ensures that only one object is created.
2. **Global Access**: The single instance can be accessed globally.
3. **Thread Safety**: Proper implementation avoids issues in multithreaded environments.
4. **Lazy or Eager Initialization**: Singleton can be instantiated when required (*lazy*) or at application startup (*eager*).

---

## How to Implement a Singleton Class

To create a singleton class:
1. Make the **constructor private** to restrict instantiation from outside.
2. Create a **static instance** of the class.
3. Provide a **public static method** to return the single instance.

### Example: Lazy Initialization

```java
class Singleton {
    // Static instance of the Singleton class
    private static Singleton instance;

    // Private constructor to prevent external instantiation
    private Singleton() {}

    // Public method to provide global access to the instance
    public static Singleton getInstance() {
        if (instance == null) { // Create instance if not already created
            instance = new Singleton();
        }
        return instance;
    }
}

public class Main {
    public static void main(String[] args) {
        Singleton obj1 = Singleton.getInstance();
        Singleton obj2 = Singleton.getInstance();

        System.out.println(obj1 == obj2); // Output: true (both refer to the same instance)
    }
}
```

### **Example**: Thread-Safe Singleton (Double-Checked Locking)

```
class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) { // First check
            synchronized (Singleton.class) {
                if (instance == null) { // Second check
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

## Advantages of Singleton Class

| **Advantage**              | **Description**                                    |
| -------------------------- | -------------------------------------------------- |
| *Controlled Instantiation* | Ensures only one instance exists at any time.      |
| *Global Access*            | Provides a single point of access to the instance. |
| *Resource Optimization*    | Saves memory by limiting object creation.          |
| *Thread-Safe Design*       | Proper implementation ensures thread safety.       |

## Disadvantages of Singleton Class

|Disadvantage|	Description|
|--|-|
|Global State Management|	Can lead to tightly coupled code if overused.|
|Difficult to Test|	Singleton can complicate unit testing due to global state.|
|Concurrent Access Issues|	Improper implementation may lead to threading problems.|
## Use Cases of Singleton Class
1. **Database Connection Pool**: Manage shared access to the database.
2. **Configuration Manager**: Maintain application configuration in a single instance.
3. **Logging Service**: A global logger for consistent logging across the application.
4. **Cache Management**: Handle a shared in-memory cache.

## Summary

A singleton class ensures that only one instance of the class is created and provides controlled global access. It is widely used in scenarios where a single shared resource or state is required. Proper implementation, especially in multithreaded environments, is crucial for achieving thread safety and avoiding common pitfalls.




---
# Related Topics
##


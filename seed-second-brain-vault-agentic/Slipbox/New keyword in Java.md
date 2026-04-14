---
creation date: 2024-12-18 11:10
modification date: Wednesday 18th December 2024 11:10:49
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - "#slipbox/permaNotes/java"
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
# The `new` Keyword in Java

## What is `new`?

The `new` keyword in Java is used to **create objects** and **allocate memory** for them in the [[Heap Data Structure|heap]]. It initialises the object by invoking its constructor and returns a reference to it.

---

## Syntax

```java
ClassName objectName = new ClassName(parameters);
```

## How It Works
	1.	Memory Allocation: Allocates memory in the heap.
	2.	Constructor Call: Invokes the class constructor to initialize the object.
	3.	Returns Reference: Returns a reference to the newly created object.

---
### Example: Creating Objects
```java
class Example {
    String message;

    Example(String msg) {
        this.message = msg;
    }

    void display() {
        System.out.println(message);
    }
}

public class Main {
    public static void main(String[] args) {
        Example obj = new Example("Hello, Java!");
        obj.display();  // Output: Hello, Java!
    }
}
```

### Example: Creating Arrays

```java
int[] numbers = new int[5];  // Allocates memory for an array of size 5
numbers[0] = 10;
System.out.println(numbers[0]);  // Output: 10
```

---
## Key Points
- **Memory**: Objects are stored in the heap, and references are in the stack.
- **Default Initialisation**: Fields are initialised to default values (e.g., 0 for numbers, null for objects).
- **Garbage Collection**: Objects without references are eligible for garbage collection.

## Uses of new
1.	Creating Objects: Instantiate user-defined or built-in classes.
2.	Creating Arrays: Allocate memory for arrays.
3.	Anonymous Objects: Objects used immediately without a reference.

### Example:
```java
new Example("Anonymous Object").display();
```

---
## Summary

The new keyword in Java:
- Creates objects or arrays.
- Allocates memory dynamically in the heap.
- Invokes constructors to initialize objects.

It is fundamental for object-oriented programming in Java.

---
# Related Topics
### [[Java]]
### [[Protected Keywords in JAVA]]




---
creation date: 2024-12-18 14:13
modification date: Wednesday 18th December 2024 14:13:50
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/java
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
# `final` vs `finally` in Java

## Overview

- **`final`**: A keyword used for defining constants, preventing inheritance, or making methods non-overridable.
- **`finally`**: A block in exception handling that is always executed, regardless of whether an exception is thrown or not.

---

## **`final`**

### Purpose:
#### 1. **Final Variable**:
- Prevents reassignment.
```java
   final int value = 10;  // Cannot be changed later
```

#### 2. **Final Method:**
- Prevents overriding in subclasses.
```java
class Parent {
    final void display() {
        System.out.println("Cannot be overridden");
    }
}
```

#### 3. **Final Class:**
- Prevents inheritance.
```java
final class FinalClass { }
```

## Key Characteristics:
- Used for constants or to enforce immutability.
- Applied to variables, methods, and classes.

## **`finally`**

### Purpose:
- A block in a try-catch statement that contains code executed after the try block, regardless of whether an exception occurs or not.

### Syntax:
```java
try {
    // Code that may throw an exception
} catch (Exception e) {
    // Exception handling
} finally {
    // Cleanup code (e.g., closing resources)
}
```

### Key Characteristics:
- Typically used for cleanup operations, such as closing files or releasing resources.
- Executed even if a return statement is present in the try or catch block.

### Example

#### Using final:
```java
final int CONSTANT = 100;  // Cannot change this value

class Parent {
    final void show() {
        System.out.println("This method cannot be overridden");
    }
}

final class ImmutableClass {
    // This class cannot be extended
}
```

#### Using finally:
```java
try {
    int result = 10 / 0;  // Throws ArithmeticException
} catch (ArithmeticException e) {
    System.out.println("Caught exception: " + e.getMessage());
} finally {
    System.out.println("Finally block executed");
}
```

---
## Key Differences

|Aspect |	final |	finally|
|---|---|---|
|Purpose	|Defines constants, prevents changes.|	Executes cleanup code after try-catch.
|Usage|	Applied to variables, methods, classes.|	Part of exception handling.
|Execution Context|	Compile-time behavior.	|Run-time behavior.
|Modifiers|	Used to enforce immutability.	|Ensures code execution after exceptions.

---
# Summary
•	**final**: For constants, non-overridable methods, or non-inheritable classes.
•	**finally**: For cleanup operations in exception handling, ensuring execution under all circumstances.



---
# Related Topics
### [[Java]]

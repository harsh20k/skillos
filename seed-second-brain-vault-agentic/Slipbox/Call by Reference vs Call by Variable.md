---
creation date: 2024-12-18 20:37
modification date: Wednesday 18th December 2024 20:37:43
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
# Call by Reference vs Call by Value

In programming, **call by reference** and **call by value** are two ways of passing arguments to functions. They determine how changes to the parameters within a function affect the original variables.

---

## 1. **Call by Value**

In **call by value**, a **copy of the actual value** is passed to the function. Changes made to the parameter inside the function do **not affect the original variable**.

### Key Points
- A **copy** of the value is passed.
- The original variable remains unchanged.
- Default behavior in many languages like **Java (for primitives)** and **C**.

### Example (Call by Value in Java)

```java
class Example {
void modify(int x) {
x = 10;  // Changes only the local copy
}
}

public class Main {
public static void main(String[] args) {
int num = 5;
Example obj = new Example();
obj.modify(num);
System.out.println(num);  // Output: 5 (original value remains unchanged)
}
}
```

---

## 2. **Call by Reference**

In **call by reference**, the **reference (memory address)** of the variable is passed to the function. Changes made to the parameter inside the function **affect the original variable**.

### Key Points
- A **reference (address)** of the variable is passed.
- Changes inside the function **directly modify** the original variable.
- Used in languages like **C++** (with pointers) and **Java (for objects)**.

### Example (Call by Reference in Java)

```java
class Example {
void modify(int[] arr) {
arr[0] = 10;  // Modifies the original array
}
}

public class Main {
public static void main(String[] args) {
int[] arr = {5, 20};
Example obj = new Example();
obj.modify(arr);
System.out.println(arr[0]);  // Output: 10 (original array is modified)
}
}
```

---

## Key Differences

| **Aspect**              | **Call by Value**                          | **Call by Reference**                    |
|--------------------------|--------------------------------------------|-------------------------------------------|
| **What is Passed**       | A copy of the value.                      | A reference to the memory address.       |
| **Effect on Original**   | Original variable is not affected.        | Original variable can be modified.       |
| **Use Case**             | For primitives or when modification is not required. | For objects or when modification is needed. |
| **Languages**            | C, Java (primitives), Python (immutable types). | C++ (pointers), Java (objects), Python (mutable types). |

---

## Summary

| **Method**         | **Description**                             | **Impact on Original Variable**        |
|---------------------|---------------------------------------------|----------------------------------------|
| **Call by Value**   | Passes a copy of the value.                 | No changes to the original variable.   |
| **Call by Reference** | Passes the reference (address) of the variable. | Changes affect the original variable. |

### Conclusion
- Use **call by value** when you don’t want a function to modify the original variable.
- Use **call by reference** when the function needs to directly alter the original variable.




---
# Related Topics
### [[Static keyword in Main(Java)]]
### [[New keyword in Java]]
### [[Protected Keywords in JAVA]]
### [[Final vs Finally in Java]]
### [[Safe Lock in java]]
### [[Java]]


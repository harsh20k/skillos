---
creation date: 2024-12-18 15:00
modification date: Wednesday 18th December 2024 15:00:58
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
# Protected Keyword in Java

The **`protected`** keyword in Java is an **access modifier** used to restrict the visibility of a class member (field, method, or constructor). It allows access to members **within the same package** and **subclasses (even in different packages)**.

---

## Key Points About `protected`

1. **Package-Level Access**:
   - Members marked as `protected` can be accessed by **any class in the same package**.

2. **Inheritance Access**:
   - `protected` members can be accessed in **subclasses**, even if they are in different packages.

3. **Cannot Be Applied to Classes**:
   - The `protected` modifier cannot be used for top-level classes or interfaces, only for class members.

4. **Combination of Default and Public**:
   - Acts like `default` within the same package and like `public` for subclasses.

---

## Syntax

```java
protected type memberName;

Example: Protected Access in the Same Package

package package1;

class Parent {
    protected void display() {
        System.out.println("Protected method in Parent");
    }
}

class Child extends Parent {
    public static void main(String[] args) {
        Parent obj = new Parent();
        obj.display();  // Accessible within the same package
    }
}
```

Example: Protected Access in Different Packages

```java
package package1;

public class Parent {
    protected void display() {
        System.out.println("Protected method in Parent");
    }
}

package package2;

import package1.Parent;

class Child extends Parent {
    public static void main(String[] args) {
        Child obj = new Child();
        obj.display();  // Accessible because Child is a subclass
    }
}
```

## Access Levels Comparison

| **Modifier** | **Same Class** | **Same Package** | **Subclass (Different Package)** | **Other Classes** |
| ------------ | -------------- | ---------------- | -------------------------------- | ----------------- |
| *public*     | Yes            | Yes              | Yes                              | Yes               |
| *protected*  | Yes            | Yes              | Yes                              | No                |
| *default*    | Yes            | Yes              | No                               | No                |
| *private*    | Yes            | No               | No                               | No                |

## When to Use protected
1.	Inheritance:
- Use protected for members that subclasses need to access while restricting access to unrelated classes.
2.	Encapsulation:
- Provides controlled visibility, limiting access to trusted subclasses or classes within the same package.

## Limitations of protected
- Does not provide fine-grained control over access like private.
- Accessible to all classes in the same package, which may expose members unnecessarily.

## Summary
- The protected keyword in Java allows access to class members within the same package and in subclasses (even in different packages).
- It is commonly used to enable inheritance while restricting access to unrelated classes.
- Usage: Combine encapsulation and inheritance effectively, especially in object-oriented designs.






---
# Related Topics
### [[Java]]
### [[New keyword in Java]]
### [[Final vs Finally in Java]]



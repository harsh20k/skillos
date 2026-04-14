---
creation date: 2024-12-16 15:54
modification date: Monday 16th December 2024 15:54:07
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
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
# Abstraction

**Abstraction** is an object-oriented programming (OOP) principle that focuses on representing the essential features of an entity while hiding unnecessary implementation details. It allows you to model complex real-world scenarios in a simplified manner, letting you concentrate on *what* an object does rather than *how* it accomplishes it.

## Key Points of Abstraction

1. **Hiding Complexity**:  
   Abstraction lets you interact with an object or system using a clear, simplified interface. The internal workings are kept hidden, reducing cognitive load and making it easier to reason about the overall design.

2. **Focus on Essentials**:  
   By filtering out extraneous details, abstraction highlights the behaviors and attributes that are most important for solving the problem at hand. This makes it easier to understand and maintain code.

3. **Interfaces and Abstract Classes**:  
   Abstract classes and interfaces are common tools for achieving abstraction in many OOP languages.  
   - **Interfaces**: Specify methods without providing their implementations, defining a contract that implementing classes must fulfill.  
   - **Abstract Classes**: Can provide partial implementation while still leaving certain methods abstract, forcing subclasses to provide the specific behavior.

4. **Improved Maintainability and Flexibility**:  
   Because calling code only depends on the abstracted interface, changes to the underlying implementation are less likely to break dependent code. This leads to more maintainable and adaptable software.

## Example (in a Java-like Syntax)

```java
// Abstract class defining a general "Shape"
abstract class Shape {
    abstract void draw();
}

// Concrete class "Circle" only needs to implement the draw method
class Circle extends Shape {
    void draw() {
        System.out.println("Drawing a circle");
    }
}

// Concrete class "Square" implements the draw method differently
class Square extends Shape {
    void draw() {
        System.out.println("Drawing a square");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape s1 = new Circle();
        Shape s2 = new Square();
        
        s1.draw(); // "Drawing a circle"
        s2.draw(); // "Drawing a square"
    }
}
```
# Related Topics
### [[OOPS]]
### [[Encapsulation]]
### [[Inheritance]]
### [[Polymorphism]]


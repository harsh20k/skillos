---
creation date: 2024-12-16 14:55
modification date: Monday 16th December 2024 14:55:57
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

# Classes and Objects
**Classes** and **objects** are fundamental concepts in object-oriented programming (OOP). They provide a blueprint and tangible form for modeling real-world entities within software.
## Class
A **class** is a blueprint or template for creating objects. It defines two main components:
1. **Attributes (Data)**: These are the characteristics or properties of the entities the class represents. For example, a `Car` class might have attributes like `color`, `brand`, and `speed`.
2. **Methods (Behaviour)**: These are functions defined inside the class that describe how the class’s objects behave or what actions they can perform. For example, a `Car` class might have methods like `drive()` or `brake()`.

The class itself is not a concrete entity; it is more like a recipe. Just as a recipe outlines the ingredients and steps without being an actual dish, a class outlines data and methods without representing an actual object in memory.
**Example (in Java-like pseudocode):**
```java
class Car {
    String color;
    int speed;
    void drive() {
        System.out.println("The car is driving.");
    }
    void brake() {
        System.out.println("The car is stopping.");
    }
}
```

## Object
An **object** is an instance of a class. It is a tangible manifestation created from the blueprint defined by the class. Once you use the class to create an object, that object occupies memory and can perform the behaviors defined in the class’s methods. Each object has its own unique state (specific values for its attributes).

**Example:**
	Car myCar = new Car(); _// myCar is an object (instance) of the Car class_
	myCar.color = "Red";
	myCar.speed = 100;
	myCar.drive(); _// Calls the drive method on the myCar object_

In this example, myCar is a specific object that has its own color and speed. It “knows” how to drive() and brake() because it was created from the Car class blueprint.

## **Why Use Classes and Objects?**

• **Modularity**: Classes help organize code into logical units. Objects represent these units in action.
• **Reusability**: Once a class is defined, you can create multiple objects (instances) from it without rewriting the same code.
• **Maintainability**: Changes to a class structure are reflected in all objects, making it easier to manage large codebases.
• **[[Abstraction]]**: Classes provide a level of [[Abstraction]] that allows you to focus on the essential qualities of an entity, rather than its implementation details.
In essence, classes define the structure and capabilities, while objects are the “living” instances that interact with each other to form a working program.

# Related Topics
### [[OOPS]]
### [[Inheritance]]
### [[Abstraction]]
### [[Encapsulation]]
### [[Polymorphism]]



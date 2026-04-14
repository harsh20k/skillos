---
creation date: 2024-12-16 15:56
modification date: Monday 16th December 2024 15:56:21
tags:
  - slipbox/permaNotes/DalhousieInterview
  - "#slipbox/permaNotes/codingConcepts"
description: A fundamental concept of Object-oriented programming.
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
# Inheritance

**Inheritance** is a fundamental concept in object-oriented programming (OOP) that allows a new class to acquire the properties and behaviours of an existing class. It promotes code reusability, establishes a natural hierarchy between classes, and facilitates the creation of more specialised and organised code structures.

## Key Concepts of Inheritance

### 1. **Base Class (Superclass)**
- The **base class** or **superclass** is the class whose properties and behaviours are inherited by another class.
- It defines common attributes and methods that can be shared across multiple derived classes.

### 2. **Derived Class (Subclass)**
- The **derived class** or **subclass** inherits from the base class.
- It can extend or modify the inherited attributes and behaviours to provide specialised functionality.
- A derived class can also introduce new attributes and methods unique to itself.

### 3. **Single Inheritance vs. Multiple Inheritance**
- **Single Inheritance**: A subclass inherits from only one superclass.
  - **Example**: In Java, a class can extend only one superclass.
- **Multiple Inheritance**: A subclass inherits from more than one superclass.
  - **Example**: In C++, a class can inherit from multiple classes. (Note: Languages like Java do not support multiple inheritance directly but achieve similar functionality using interfaces.)

### 4. **Method Overriding**
- **Method Overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.
- This allows the subclass to tailor or enhance behaviours inherited from the superclass.

### 5. **Access Control**
- Inheritance respects access modifiers (`public`, `protected`, `private`), determining how the members of the superclass can be accessed by the subclass.
- Typically, `public` and `protected` members are accessible to subclasses, while `private` members are not directly accessible.

## Benefits of Inheritance

1. **Code Reusability**
   - Inheritance allows subclasses to reuse code from superclasses, reducing redundancy and promoting DRY (Don't Repeat Yourself) principles.
   
2. **Hierarchical Classification**
   - It enables the creation of a natural hierarchy between classes, making the code more organised and easier to understand.
   
3. **Extensibility**
   - New functionalities can be added to existing classes through inheritance without modifying the original class, facilitating easier maintenance and scalability.
   
4. **[[Polymorphism]] Support**
   - Inheritance works hand-in-hand with [[Polymorphism]], allowing objects of different subclasses to be treated uniformly based on their superclass type.

## Example (in Java-like Syntax)

```java
// Superclass
class Animal {
    String name;

    void eat() {
        System.out.println(name + " is eating.");
    }

    void sleep() {
        System.out.println(name + " is sleeping.");
    }
}

// Subclass inheriting from Animal
class Dog extends Animal {
    void bark() {
        System.out.println(name + " is barking.");
    }

    // Overriding the eat method
    @Override
    void eat() {
        System.out.println(name + " is eating dog food.");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.name = "Buddy";
        myDog.eat();    // Outputs: Buddy is eating dog food.
        myDog.sleep();  // Outputs: Buddy is sleeping.
        myDog.bark();   // Outputs: Buddy is barking.
    }
}
````java
```

# Explanation

- **Animal Class**: Serves as the superclass with attributes and methods common to all animals.
- **Dog Class**: Inherits from `Animal` and adds a new method `bark()`. It also overrides the `eat()` method to provide a specialised behaviour for dogs.
- **Main Class**: Creates an instance of `Dog`, sets its name, and calls its methods, demonstrating inheritance and method overriding.

# Types of Inheritance

1. **Single Inheritance**
   - A subclass inherits from one superclass.

2. **Multiple Inheritance**
   - A subclass inherits from more than one superclass. (Supported in some languages like C++, but not directly in Java.)

3. **Multilevel Inheritance**
   - A chain of inheritance where a subclass acts as a superclass for another subclass.
   - **Example**: Class A → Class B inherits from A → Class C inherits from B.

4. **Hierarchical Inheritance**
   - Multiple subclasses inherit from a single superclass.
   - **Example**: Classes B, C, and D all inherit from class A.

5. **Hybrid Inheritance**
   - A combination of two or more types of inheritance.
   - Typically achieved using interfaces or abstract classes to avoid issues like the diamond problem in multiple inheritance.

# Access Modifiers and Inheritance

- **Public Members**: Accessible from any other class.
- **Protected Members**: Accessible within the same package and subclasses.
- **Private Members**: Not accessible outside the class; cannot be inherited directly.
- **Default (Package-Private) Members**: Accessible only within the same package.

# Types of Inheritance


# Conclusion

Inheritance is a powerful OOP concept that promotes code reusability, organisation, and scalability by allowing classes to inherit properties and behaviours from other classes. Proper use of inheritance leads to cleaner, more maintainable code and supports the creation of flexible and extensible software systems.

# Related Topics
### [[OOPS]]
### [[Polymorphism]]
### [[Abstraction]]
### [[Encapsulation]]
### [[Classes and Objects]]


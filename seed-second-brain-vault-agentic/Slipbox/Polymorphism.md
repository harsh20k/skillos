---
creation date: 2024-12-16 16:03
modification date: Monday 16th December 2024 16:03:15
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
# Polymorphism

**Polymorphism** is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types), enhancing flexibility and integration within software systems.

## Key Concepts of Polymorphism

1. **Definition**
   - **Polymorphism** derives from the Greek words "poly" (many) and "morph" (form), meaning "many forms."
   - It allows methods to perform different functions based on the object it is acting upon, even if they share the same name.

2. **Types of Polymorphism**
   - **Compile-Time Polymorphism (Static Polymorphism)**
     - Achieved through **method overloading** and **operator overloading**.
     - The decision about which method to invoke is made at compile time.
   - **Runtime Polymorphism (Dynamic Polymorphism)**
     - Achieved through **method overriding** using [[Inheritance]].
     - The decision about which method to invoke is made at runtime based on the object's actual type.

## Types of Polymorphism

### 1. Method Overloading (Compile-Time Polymorphism)
   - **Definition**: Multiple methods in the same class share the same name but have different parameters (different type or number of parameters).
   - **Purpose**: Increases the readability of the code by allowing the same method name to handle different types of inputs.
   - **Example (in Java-like Syntax)**:
     ```java
     class MathUtils {
         // Method to add two integers
         int add(int a, int b) {
             return a + b;
         }
         
         // Overloaded method to add three integers
         int add(int a, int b, int c) {
             return a + b + c;
         }
         
         // Overloaded method to add two doubles
         double add(double a, double b) {
             return a + b;
         }
     }

     public class Main {
         public static void main(String[] args) {
             MathUtils math = new MathUtils();
             System.out.println(math.add(2, 3));          // Outputs: 5
             System.out.println(math.add(2, 3, 4));       // Outputs: 9
             System.out.println(math.add(2.5, 3.5));      // Outputs: 6.0
         }
     }
     ```

### 2. Method Overriding (Runtime Polymorphism)
   - **Definition**: A subclass provides a specific implementation of a method that is already defined in its superclass.
   - **Purpose**: Allows a subclass to modify or extend the behavior of methods inherited from the superclass.
   - **Example (in Java-like Syntax)**:
     ```java
     // Superclass
     class Animal {
         void makeSound() {
             System.out.println("Some generic animal sound");
         }
     }

     // Subclass
     class Dog extends Animal {
         @Override
         void makeSound() {
             System.out.println("Bark");
         }
     }

     // Another Subclass
     class Cat extends Animal {
         @Override
         void makeSound() {
             System.out.println("Meow");
         }
     }

     public class Main {
         public static void main(String[] args) {
             Animal myAnimal = new Animal();
             Animal myDog = new Dog();
             Animal myCat = new Cat();

             myAnimal.makeSound(); // Outputs: Some generic animal sound
             myDog.makeSound();    // Outputs: Bark
             myCat.makeSound();    // Outputs: Meow
         }
     }
     ```
   - **Explanation**: Even though `myDog` and `myCat` are of type `Animal`, the overridden methods in `Dog` and `Cat` are called at runtime, demonstrating dynamic polymorphism.

### 3. [[Operator overloading]] (Less Common in Some Languages)
   - **Definition**: Allows the same operator to have different meanings based on the context or the operands.
   - **Purpose**: Enhances the readability and usability of user-defined types.
   - **Example (in C++ Syntax)**:
     ```cpp
     class Complex {
     public:
         float real;
         float imag;

         Complex(float r = 0, float i = 0) : real(r), imag(i) {}

         // Overloading the + operator
         Complex operator + (const Complex& obj) {
             Complex res;
             res.real = real + obj.real;
             res.imag = imag + obj.imag;
             return res;
         }
     };

     int main() {
         Complex c1(3.0, 2.5);
         Complex c2(1.5, 4.5);
         Complex c3 = c1 + c2; // Uses overloaded + operator
         std::cout << "Result: " << c3.real << " + " << c3.imag << "i"; // Outputs: 4.5 + 7.0i
         return 0;
     }
     ```

## Benefits of Polymorphism

1. **Flexibility and Extensibility**
   - Polymorphism allows for designing flexible and extensible systems where new classes can be introduced with little or no modification to existing code.

2. **Code Reusability**
   - Enables the reuse of existing code with new functionality, reducing redundancy and enhancing maintainability.

3. **Maintainability**
   - Simplifies code maintenance by allowing changes in the superclass to propagate to subclasses, ensuring consistency across different parts of the application.

4. **Interchangeable Components**
   - Objects can be interchanged based on their shared interfaces or superclass types, facilitating the implementation of design patterns like Strategy, Factory, and Observer.

## Real-World Example

**Scenario**: A graphics application that can render different shapes like circles, squares, and triangles.

**Implementation**:
```java
// Superclass
abstract class Shape {
    abstract void draw();
}

// Subclasses
class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a Circle");
    }
}

class Square extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a Square");
    }
}

class Triangle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a Triangle");
    }
}

// Main Class
public class Main {
    public static void main(String[] args) {
        Shape[] shapes = { new Circle(), new Square(), new Triangle() };

        for (Shape shape : shapes) {
            shape.draw(); // Calls the appropriate draw method based on the actual object type
        }
    }
}
```

**Output**
Drawing a Circle
Drawing a Square
Drawing a Triangle

## **Explanation**:
• The Shape class defines an abstract draw() method.
• Each subclass (Circle, Square, Triangle) provides its own implementation of draw().
• In the Main class, an array of Shape references holds different shape objects.
• When draw() is called on each shape, the appropriate subclass method is invoked, demonstrating polymorphism.
## **Summary**

Polymorphism is a powerful OOP concept that enhances the flexibility, reusability, and maintainability of code. By allowing objects of different classes to be treated uniformly based on a common superclass or interface, polymorphism facilitates the creation of scalable and adaptable software systems.

# Related Topics
### [[OOPS]]
### [[Operator overloading]]
### [[Abstraction]]
### [[Encapsulation]]
### [[Classes and Objects]]
### [[Inheritance]]



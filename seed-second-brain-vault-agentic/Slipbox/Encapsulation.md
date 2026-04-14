---
creation date: 2024-12-16 15:48
modification date: Monday 16th December 2024 15:48:07
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
# Encapsulation

**Encapsulation** is an object-oriented programming principle that combines data (attributes) and the methods (functions) that operate on that data into a single unit called a class. It also protects the internal state of an object by restricting direct access to its attributes, often allowing modifications only through well-defined methods.

## Key Aspects of Encapsulation

1. **Data Hiding**:  
   By marking class attributes as private or protected, you prevent external code from directly altering these attributes. This helps maintain [[Data integrity]], since changes must go through controlled methods that can validate inputs and maintain consistency.

2. **Public Interfaces**:  
   Encapsulation provides a set of **public methods** (getters, setters, or other operations) through which outside code can interact with the object. These methods define how the object’s data can be accessed or modified, ensuring proper validation and preventing the misuse of internal state.

3. **Improved Maintainability**:  
   By localising data handling and logic within the class, encapsulation makes it easier to modify and maintain code. If internal details change, the external code using the object often remains unaffected, as long as the public interface is consistent.

4. **Enhanced Security and Robustness**:  
   Controlling access to the object’s internal state reduces the likelihood of errors or inconsistencies, thereby making the software more stable and secure.

## Example (in a Java-like Syntax)

```java
class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        if (initialBalance > 0) {
            this.balance = initialBalance;
        } else {
            this.balance = 0; // Default to 0 if invalid initial balance
        }
    }

    public void deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
        }
    }

    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= this.balance) {
            this.balance -= amount;
            return true;
        }
        return false;
    }

    public double getBalance() {
        return this.balance;
    }
}
```java
```

In this example, the balance attribute is kept private to prevent direct access from outside the class. Instead, deposit(), withdraw(), and getBalance() methods provide the only means to interact with the balance. This ensures that all operations on balance are carefully managed and validated.

## Summary

Encapsulation ensures that objects control how their internal data is used and modified, leading to cleaner, more maintainable, and safer code. By making classes responsible for their own data and providing a consistent interface, encapsulation lays a foundation for building robust and resilient software systems.

# Related Topics
### [[OOPS]]
### [[Abstraction]]
### [[Inheritance]]
### [[Polymorphism]]


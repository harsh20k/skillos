---
creation date: 2024-12-16 14:41
modification date: Monday 16th December 2024 14:41:02
tags:
  - slipbox/permaNotes/DalhousieInterview
  - "#slipbox/permaNotes/codingConcepts"
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
# Programming Paradigm

A **programming paradigm** is a fundamental style or approach to structuring and writing computer programs. It provides a particular way of thinking about and organizing code, often guided by a set of principles, concepts, and abstractions. Different paradigms influence how developers design solutions, how code is structured and maintained, and how problems are conceptualised.

## Key Points:
- **Conceptual Framework**: A programming paradigm defines how problems are broken down and how solutions are expressed in code.
- **Influence on Code Structure**: Paradigms dictate how data, functions, and logic are organized. For example:
  - **Procedural**: Uses a sequence of instructions and routines.
  - **Object-Oriented**: Structures code around objects and classes.
  - **Functional**: Emphasizes pure functions, immutability, and declarative problem solving.
  - **Logic/Declarative**: Focuses on expressing the desired result rather than the steps to achieve it.
- **Choice of Paradigm**: The paradigm chosen can affect program clarity, maintainability, scalability, and performance. Some languages support multiple paradigms, allowing developers to blend concepts as needed.

# Other Programming Paradigms

Beyond Object-Oriented Programming (OOP), several other programming paradigms offer different approaches to structuring and reasoning about code:

## 1. Procedural Programming
- **Description**:  
  Focuses on a sequence of instructions or procedures that operate on data.  
- **Key Characteristics**:  
  - Uses functions and procedures to break down tasks into smaller, manageable steps.  
  - Emphasises a clear flow of control.  
- **Examples**: C, Pascal

## 2. Functional Programming
- **Description**:  
  Treats computation as the evaluation of mathematical functions and avoids changing state and mutable data.  
- **Key Characteristics**:  
  - Encourages immutability and the use of pure functions (no side effects).  
  - [[Functions as First-Class Citizens|Functions are first-class citizens and can be passed around like data. ]] 
- **Examples**: Haskell, Erlang, Clojure, and functional styles in languages like JavaScript or Python.

## 3. Logic Programming
- **Description**:  
  Uses formal logic to express relationships, facts, and rules. The program queries these rules to derive conclusions.  
- **Key Characteristics**:  
  - Instead of giving step-by-step instructions, you define what you want and let the system figure out how to get it.  
- **Examples**: Prolog

## 4. Declarative Programming
- **Description**:  
  Focuses on **what** the program should accomplish rather than **how** to accomplish it.  
- **Key Characteristics**:  
  - High-level specifications of desired results, leaving the implementation details to the underlying system.  
- **Examples**: [[SQL]] (for database queries), HTML (for web structure), CSS (for styling), SwiftUI(for IOS apps interface design).

## 5. Event-Driven Programming
- **Description**:  
  Organises logic around events (e.g., user actions, sensor outputs, messages) and handlers that respond to those events.  
- **Key Characteristics**:  
  - The flow of the program is determined by events rather than a predefined sequence of instructions.  
- **Examples**: JavaScript in web browsers, Node.js, GUI frameworks.

## 6. Aspect-Oriented Programming (AOP)
- **Description**:  
  Separates cross-cutting concerns (like logging, security, or transaction management) from the main business logic.  
- **Key Characteristics**:  
  - Uses “aspects” to encapsulate concerns that affect multiple parts of a program.  
- **Examples**: AspectJ (an extension of Java)

---

## Conclusion
Each programming paradigm offers a distinct way of thinking about and writing software. While OOP structures code around objects, other paradigms like procedural, functional, logic-based, declarative, event-driven, and aspect-oriented programming present alternative perspectives, each suited to particular types of problems or application domains.

# Related Topics
### [[OOPS]]


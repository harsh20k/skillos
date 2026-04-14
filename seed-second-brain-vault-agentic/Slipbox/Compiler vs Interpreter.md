---
creation date: 2024-12-18 14:11
modification date: Wednesday 18th December 2024 14:11:15
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/algorithms
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
# Compiler vs Interpreter

## Overview

Both **compiler** and **interpreter** are tools used to translate high-level programming languages into machine code, but they operate differently in terms of execution.

---

## What is a Compiler?

A **compiler** translates the entire source code into machine code **before execution**. The machine code is saved as an executable file, which can be run independently.

### Characteristics:
1. **Translation**: Translates the whole code at once.
2. **Execution**: The executable file is run later.
3. **Speed**: Faster execution after compilation because translation is done beforehand.
4. **Error Handling**: Detects and reports all errors during the compilation phase.

### Example:
Languages like **C**, **C++**, and **Java (partially)** use compilers.

---

## What is an Interpreter?

An **interpreter** translates and executes the code **line-by-line** at runtime. It does not produce an intermediate executable file.

### Characteristics:
1. **Translation**: Translates the code line-by-line.
2. **Execution**: Executes immediately after translating each line.
3. **Speed**: Slower execution because translation happens during runtime.
4. **Error Handling**: Stops immediately when an error is encountered.

### Example:
Languages like **Python**, **JavaScript**, and **Ruby** use interpreters.

---

## Key Differences

| **Aspect**          | **Compiler**                          | **Interpreter**                             |
| ------------------- | ------------------------------------- | ------------------------------------------- |
| **Translation**     | Entire code translated at once.       | Translates code line-by-line.               |
| **Output**          | Produces an executable file.          | Does not produce a file; executes directly. |
| **Speed**           | Faster execution (after compilation). | Slower due to runtime translation.          |
| **Error Detection** | All errors are reported at once.      | Errors are reported line-by-line.           |
| **Examples**        | C, C++, Java (compiles to bytecode).  | Python, JavaScript, Ruby.                   |

---

## Example of Execution

### Compiler Workflow:

Source Code → Compiler → Executable File → Run Program

### Interpreter Workflow:

Source Code → Interpreter → Line-by-Line Execution

---

## Summary

- **Compiler**: Translates the entire program into machine code before execution, offering faster runtime but delayed feedback.
- **Interpreter**: Executes the program line-by-line, providing immediate feedback but slower runtime performance.

Each has its strengths and is suited to different use cases.


---
# Related Topics
### [[Programming Paradigm]]
### [[Programmming Languages]]


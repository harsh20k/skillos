---
creation date: 2024-12-28 10:45
modification date: Saturday 28th December 2024 10:45:11
tags:
  - slipbox/permaNotes/codingConcepts
  - codingQuestions
  - slipbox/permaNotes/swift
description: 
source: "#chatgpt"
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
---
# Concept

The concept of **“functions as first-class citizens”** means that in programming languages that support this feature, functions can be treated like any other value. This allows you to:

- Assign functions to variables.
- Pass functions as arguments to other functions.
- Return functions from other functions.
- Store functions in data structures (e.g., arrays, dictionaries).

## Explanation with Examples:

### **1. Assigning Functions to Variables:**
Functions can be assigned to variables and invoked using the variable name.

##### **Example in Python:**

```python
def greet(name):
    return f"Hello, {name}!"
_# Assign the function to a variable_
say_hello = greet
_# Call the function using the new variable_
print(say_hello("Alice"))  _# Output: Hello, Alice!_
```

### **2. Passing Functions as Arguments:**
You can pass functions as arguments to other functions, allowing for higher-order programming.

##### **Example in Python:**

```python
def greet(name):
    return f"Hello, {name}!"
def execute_function(func, value):
    return func(value)
_# Pass the `greet` function as an argument_
print(execute_function(greet, "Bob"))  _# Output: Hello, Bob!_
```

### **3. Returning Functions from Other Functions:**
A function can return another function, enabling the creation of dynamic behavior.

##### **Example in Python:**

```python
def multiplier(factor):
    def multiply_by(n):
        return n * factor
    return multiply_by
_# Get a function that multiplies by 3_
times_three = multiplier(3)
_# Use the returned function_
print(times_three(10))  _# Output: 30_
```

### **4. Storing Functions in Data Structures:**
Functions can be stored in collections like lists or dictionaries.

##### **Example in Python:**

```python
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
operations = {
    "add": add,
    "subtract": subtract
}
_# Access and call functions from the dictionary_
print(operations["add"](5, 3))       _# Output: 8_
print(operations["subtract"](5, 3)) _# Output: 2_
```
---
# Advantages of Functions as First-Class Citizens:

1. **Flexibility:** Enables higher-order functions like map, filter, and reduce.
2. **Dynamic Programming:** Functions can be created and passed dynamically, adapting to runtime requirements.
3. **Code Reusability:** Promotes modularity and composability.
4. **Cleaner Syntax:** Enables concise, readable, and maintainable code.

##### **Example in Real Life:**

**Event Handlers:**
In UI programming, event handlers (functions) are passed to UI components to define their behaviour when events like clicks or keypresses occur.

##### **Example in JavaScript:**

```js
function handleClick() {
    console.log("Button clicked!");
}
_// Passing the function as a callback_
button.addEventListener("click", handleClick);
```


> [!NOTE]
> The concept of functions as first-class citizens is foundational in functional programming and languages that support higher-order functions, such as Python, JavaScript, Swift, and more. It promotes flexibility and power in designing programs.

---
# Related Topics
### [[Programming Paradigm]]
### [[Programmming Languages]]
### [[Swift]]
### [[Python]]

---
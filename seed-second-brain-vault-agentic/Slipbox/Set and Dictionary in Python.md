---
creation date: 2024-12-22 17:38
modification date: Sunday 22nd December 2024 17:38:34
tags:
  - slipbox/permaNotes/DalhousieInterview
  - codingQuestions
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/python
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

# Difference Between Set and Dictionary in Python

| **Aspect**      | **Set**                                                                                                           | **Dictionary**                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| *Definition*    | Unordered collection of unique elements.                                                                          | Unordered collection of key-value pairs.                         |
| *Data Type*     | Stores only values.                                                                                               | Stores keys and their associated values.                         |
| *Syntax*        | Defined using curly braces {} or set().                                                                           | Defined using curly braces {} with key-value pairs.              |
| *Example*       | {1, 2, 3} or set([1, 2, 3])                                                                                       | {"name": "Alice", "age": 25}                                     |
| *Uniqueness*    | Ensures all elements are unique.                                                                                  | Keys must be unique, but values can be duplicated.               |
| *Mutability*    | Mutable (can add/remove elements).                                                                                | Keys are immutable; values are mutable.                          |
| *Access Method* | Iterated over directly.                                                                                           | Accessed using keys (dict[key]).                                 |
| *Use Case*      | Used for membership testing, eliminating duplicates, and mathematical set operations (e.g., union, intersection). | Used for mapping relationships (e.g., storing data with labels). |

## Key Differences

### 1. Storage:
	- Set: Stores unique values.
	- Dictionary: Maps unique keys to values.

### 2. Initialization:

#### Set
```python
my_set = {1, 2, 3}
my_set = set([1, 2, 3])
```
#### Dictionary
```python
my_dict = {"name": "Alice", "age": 25}
```

### 3. Operations:
- Set Operations:

```python
my_set = {1, 2, 3}
my_set.add(4)       # Add an element
my_set.remove(2)    # Remove an element
print(3 in my_set)  # Membership test
print(my_set.union({4, 5}))  # Union of sets
```

- Dictionary Operations:

```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])          # Access value by key
my_dict["city"] = "New York"    # Add key-value pair
del my_dict["age"]              # Remove key-value pair
print("name" in my_dict)        # Membership test (key)
```


### 4. Iteration:
- Set: Iterates over values directly.

```python
my_set = {1, 2, 3}
for val in my_set:
    print(val)
```

- Dictionary: Can iterate over keys, values, or key-value pairs.

```python
my_dict = {"name": "Alice", "age": 25}
for key in my_dict:
    print(key)  # Iterates over keys
for value in my_dict.values():
    print(value)  # Iterates over values
for key, value in my_dict.items():
    print(key, value)  # Iterates over key-value pairs
```


### 5. When to Use:
- Set: When you need a collection of unique items, such as finding unique elements or performing set operations.
- Dictionary: When you need to store data as a mapping between keys and values, such as a phone book or configuration data.

## Summary

A set is ideal for unique value storage and set operations, while a dictionary is used for mapping relationships between keys and values. Both are powerful tools, and the choice depends on the specific use case. 🚀



---
# Related Topics
##


---
creation date: 2024-12-18 10:41
modification date: Wednesday 18th December 2024 10:41:40
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/algorithms
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/datastructures
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
# What is a Hash Function?

A **hash function** is a mathematical function that takes an input (key) and returns a fixed-size value (hash), usually an integer. This hash is used as an **index** in a [[Hash Table]] to store and retrieve values efficiently.

---

## Key Characteristics of a Hash Function

1. **Deterministic**:
   - For the same input, it always produces the same output.

2. **Fast Computation**:
   - The hash function should compute the hash value in constant time, **O(1)**.

3. **Uniform Distribution**:
   - Distributes keys evenly across the [[Hash Table]] to minimize collisions.

4. **Minimizes Collisions**:
   - Reduces the number of keys mapping to the same index.

5. **Fixed Output Size**:
   - The output hash value has a fixed size, regardless of the input size.

---

## How a Hash Function Works in a [[Hash Table]]

1. **Key to Hash Conversion**:
   - The hash function maps a key (e.g., a string) to a hash value.
2. **Index Calculation**:
   - The hash value is used to calculate an index for the key:
     ```
     index = hash_function(key) % table_size
     ```
3. **Storage**:
   - The value is stored at the calculated index.

---

## Properties of a Good Hash Function

1. **Low Collision Probability**:
   - Maps different keys to different hash values as much as possible.

2. **Uniform Distribution**:
   - Ensures keys are spread uniformly across the table.

3. **Efficiency**:
   - Computes hash values quickly.

4. **Deterministic**:
   - Always returns the same hash value for the same input.

---

## Example of a Simple Hash Function

### Hashing Strings
A simple hash function can sum the ASCII values of characters in a string:

```python
def hash_function(key, table_size):
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    return hash_value % table_size

# Example
key = "cat"
table_size = 10
print(hash_function(key, table_size))  # Output: 8
```

## Collisions in Hash Functions

### What Are Collisions?

- When two keys produce the same hash value, they map to the same index in the [[Hash Table]].
- Example:

```
hash("cat") = 8
hash("act") = 8
```

### How to Handle Collisions:
1.	Chaining:
	- Store multiple values in a linked list at the same index.
2.	Open Addressing:
	- Use probing to find the next available slot.

Applications of Hash Functions
1.	Hash Tables:
	- For fast data retrieval in dictionaries or caches.
2.	Cryptography:
	- Secure hash functions (e.g., SHA-256) for encrypting sensitive data.
3.	Checksums:
	- Verifying data integrity in files or network communication.
4.	Data Indexing:
	- Indexing large datasets in databases.

# Summary

A hash function is the backbone of hash tables, enabling fast storage and retrieval of data by mapping keys to indices. A good hash function minimizes collisions, distributes data uniformly, and is computationally efficient. It is widely used in various domains, including databases, caches, and cryptography.



---
# Related Topics
### [[Hash Table]]
### [[Algorithms and Data Structures]]
### [[Data Structures]]


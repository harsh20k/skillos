---
creation date: 2024-12-18 08:54
modification date: Wednesday 18th December 2024 08:54:26
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/datastructures
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
# Hash Table

## What is a Hash Table?

A **Hash Table** is a **data structure** that stores data in an array-like format using a **key-value pair** system. It uses a **[[Hash Function]]** to compute an index (hash) into an array where the desired value is stored.

---

## Key Concepts

1. **[[Hash Function]]**:
   - Maps a key to an index in the array.
   - Example: `index = hash(key) % table_size`

2. **Buckets**:
   - An array slot where data is stored.
   - Multiple values can share the same bucket (due to collisions).

3. **Collisions**:
   - Occur when two keys hash to the same index.
   - Handled using techniques like **chaining** or **open addressing**.

---

## Operations in Hash Table

1. **Insert**:
   - Use the [[Hash Function]] to determine the index and store the key-value pair.
   - Time Complexity: **O(1)** (average), **O(n)** (worst case with collisions).

2. **Search**:
   - Use the [[Hash Function]] to find the index and retrieve the value.
   - Time Complexity: **O(1)** (average), **O(n)** (worst case).

3. **Delete**:
   - Use the [[Hash Function]] to find the index and remove the key-value pair.
   - Time Complexity: **O(1)** (average), **O(n)** (worst case).

---

## Collision Resolution Techniques

1. **Chaining**:
   - Each bucket stores a linked list of elements that hash to the same index.
   - **Advantage**: Handles collisions well, easy to implement.
   - **Disadvantage**: May degrade to O(n) if many collisions occur.

2. **Open Addressing**:
   - All elements are stored in the hash table itself.
   - When a collision occurs, the algorithm searches for the next available slot.
   - Types:
     - **Linear Probing**: Check the next slot sequentially.
     - **Quadratic Probing**: Use a quadratic function to find the next slot.
     - **Double Hashing**: Use a second [[Hash Function]] to resolve collisions.

---

## Advantages of Hash Tables

- **Fast Lookups**: Average time complexity of **O(1)** for insertion, deletion, and search.
- **Efficient**: Ideal for large datasets where quick access is required.
- **Dynamic Size**: Can resize dynamically to reduce collisions.

---

## Disadvantages of Hash Tables

- **Collisions**: Degrade performance in the presence of many collisions.
- **Space Overhead**: May require more memory to handle collisions effectively.
- **Not Ordered**: Does not maintain the order of keys or values.

---

## Applications of Hash Tables

1. **Dictionaries**:
   - `dict` in Python, `HashMap` in Java.
2. **Caching**:
   - Storing frequently accessed data for faster retrieval.
3. **Database Indexing**:
   - Indexing rows for fast search queries.
4. **Symbol Tables**:
   - Compilers use hash tables to manage variables and functions.
5. **Set Implementation**:
   - `set` in Python or Java is implemented using hash tables.

---

## Example of a Hash Table in Python

```python
# Basic Hash Table Implementation
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Chaining
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if key exists
                return
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Not found
    
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False  # Key not found

# Example usage
ht = HashTable(10)
ht.insert("name", "Alice")
ht.insert("age", 25)
print(ht.search("name"))  # Output: Alice
print(ht.search("age"))   # Output: 25
```

# Time and Space Complexity

| **Operation**    | **Average Case** | **Worst Case** |
| ---------------- | ---------------- | -------------- |
| Insert           | O(1)             | O(n)           |
| Search           | O(1)             | O(n)           |
| Delete           | O(1)             | O(n)           |
| Space Complexity | O(n)             | O(n)           |

# Summary

A **Hash Table** is a powerful data structure for fast key-based access. It provides constant-time average performance for operations like insert, search, and delete. While it handles collisions via chaining or open addressing, its performance can degrade in worst-case scenarios. Hash tables are widely used in dictionaries, caches, and real-time applications requiring quick lookups.
## Resources

[Youtube video- Hash table in 4 minutes](https://www.youtube.com/watch?v=knV86FlSXJ8&ab_channel=MichaelSambol)

---
# Related Topics
### [[Data Structures]]
### [[Heap Data Structure]]
### [[Algorithms and Data Structures]]



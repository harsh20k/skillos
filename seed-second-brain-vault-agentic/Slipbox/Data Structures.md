---
creation date: 2024-12-18 08:55
modification date: Wednesday 18th December 2024 08:55:20
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/datastructures
  - slipbox/permaNotes/algorithms
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
# Overview of Data Structures

## What are Data Structures?

A **data structure** is a way of organizing and storing data to enable efficient access and modification. Choosing the right data structure is critical for designing efficient [[Algorithms and Data Structures|algorithms]] and solving computational problems.

---

## Categories of Data Structures

### 1. **Linear Data Structures**
- Data elements are arranged sequentially, and each element is connected to its previous and next element.

#### Examples:
| **Type**           | **Description**                                     | **Examples**                                  |
|--------------------|-----------------------------------------------------|----------------------------------------------|
| **Array**          | Fixed-size collection of elements stored contiguously.| Used for storing and accessing data by index.|
| **Linked List**    | Collection of nodes connected via pointers.         | Singly, doubly, or circular linked lists.    |
| **Stack**          | Follows LIFO (Last In, First Out).                  | Undo operations, recursion.                 |
| **Queue**          | Follows FIFO (First In, First Out).                 | Task scheduling, print queues.              |

---

### 2. **Non-Linear Data Structures**
- Data elements are arranged in a hierarchical or non-sequential manner.

#### Examples:
| **Type**           | **Description**                                     | **Examples**                                  |
|--------------------|-----------------------------------------------------|----------------------------------------------|
| **Tree**           | Hierarchical structure with nodes and edges.        | Binary Tree, Binary Search Tree, AVL Tree.  |
| **Graph**          | Set of nodes (vertices) and edges (connections).    | Directed, Undirected, Weighted Graphs.      |

---

### 3. **Hash-Based Data Structures**
- Use a **[[Hash Function]]** to map keys to values for fast lookups.

#### Examples:
| **Type**           | **Description**                                     | **Examples**          |
| ------------------ | --------------------------------------------------- | --------------------- |
| **[[Hash Table]]** | Stores key-value pairs for constant-time lookups.   | Dictionaries, caches. |
| **Hash Set**       | Stores unique elements with fast insertion/removal. | Sets.                 |

---

### 4. **Dynamic and Specialized Data Structures**
- Designed for specific use cases or performance optimizations.

#### Examples:
| **Type**                      | **Description**                              | **Examples**                           |
| ----------------------------- | -------------------------------------------- | -------------------------------------- |
| **Heap**                      | Specialized binary tree for priority queues. | Min-Heap, Max-Heap.                    |
| **Trie (Prefix Tree)**        | Efficient for searching strings or prefixes. | Autocomplete, dictionary lookups.      |
| **Disjoint Set (Union-Find)** | Efficient for connected component queries.   | Kruskal's Algorithm, network problems. |

---

## Comparison of Key Data Structures

| **Data Structure** | **Access** | **Search** | **Insertion** | **Deletion** | **Use Cases**               |
|---------------------|------------|------------|---------------|--------------|-----------------------------|
| **Array**           | O(1)       | O(n)       | O(n)          | O(n)         | Static data, indexing       |
| **Linked List**     | O(n)       | O(n)       | O(1)          | O(1)         | Dynamic collections         |
| **Stack**           | O(n)       | O(n)       | O(1)          | O(1)         | Undo operations, recursion  |
| **Queue**           | O(n)       | O(n)       | O(1)          | O(1)         | Scheduling tasks            |
| **Binary Search Tree**| O(log n)  | O(log n)   | O(log n)      | O(log n)     | Sorted data, range queries  |
| **[[Hash Table]]**      | O(1)       | O(1)       | O(1)          | O(1)         | Fast lookups and retrievals |

---

## Applications of Data Structures

| **Category**         | **Use Case**                                  | **Examples**                                   |
|-----------------------|-----------------------------------------------|-----------------------------------------------|
| **Linear Structures** | Sequential data processing                   | Arrays, queues for pipelines.                |
| **Trees**             | Hierarchical data                            | File systems, XML/HTML parsing.              |
| **Graphs**            | Network problems                             | Social networks, shortest path algorithms.   |
| **Hash Structures**   | Fast lookups                                 | Databases, caching mechanisms.               |
| **Dynamic Structures**| Real-time prioritization                     | Heaps for priority queues, event scheduling. |

---

## Importance in Technical Interviews

1. **Problem Solving**:
   - Understanding data structures helps you choose the best tool for solving algorithmic problems.

2. **Algorithm Design**:
   - Efficient algorithms are often built on top of the right data structures.

3. **Real-World Applications**:
   - Knowledge of data structures is essential for system design, databases, and real-time applications.

---

## Summary

Data structures are the building blocks of programming, providing organized ways to store, access, and manipulate data. Mastery of linear, non-linear, and specialized structures is crucial for solving technical problems effectively and efficiently.


---
# Related Topics
### [[Sorting Algorithms]]
### [[Search Algorithms]]


---
creation date: 2024-12-18 08:58
modification date: Wednesday 18th December 2024 08:58:15
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/algorithms
  - slipbox/permaNotes/datastructures
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
# Overview of Algorithms and [[Data Structures]]

## What Are [[Data Structures]] and Algorithms?

- **[[Data Structures]]**: Organize and store data efficiently to enable quick access and modification.
- **Algorithms**: Step-by-step procedures or rules designed to solve a problem or perform a task efficiently.

Together, they form the foundation of computer science and are critical for solving computational problems.

---

## Types of [[Data Structures]]

### 1. **Linear [[Data Structures]]**
- **Array**: Fixed-size, contiguous memory storage.  
  Use: Random access, simple data storage.
- **Linked List**: Nodes connected via pointers.  
  Use: Dynamic data insertion/deletion.
- **Stack**: LIFO (Last In, First Out).  
  Use: Undo operations, recursion.
- **Queue**: FIFO (First In, First Out).  
  Use: Task scheduling.

### 2. **Non-Linear [[Data Structures]]**
- **Tree**: Hierarchical structure with parent-child relationships.  
  Use: File systems, decision trees.
- **Graph**: Nodes (vertices) connected by edges.  
  Use: Social networks, shortest path problems.

### 3. **Hash-Based Structures**
- **[[Hash Table]]**: Key-value pairs for fast lookups.  
  Use: Dictionaries, caching.
- **Hash Set**: Stores unique elements.  
  Use: Fast membership testing.

### 4. **Dynamic and Specialized Structures**
- **[[Heap Data Structure|Heap]]**: Priority queue implementation.  
  Use: Scheduling, event handling.
- **Trie**: Prefix tree for string searches.  
  Use: Autocomplete, dictionary lookups.
- **Union-Find**: Connected component queries.  
  Use: Network analysis.

---

## Types of Algorithms

### 1. **[[Search Algorithms]]**
- **Linear Search**: Sequential search, O(n).  
  Use: Small, unsorted datasets.
- **Binary Search**: Divide and conquer on sorted arrays, O(log n).  
  Use: Sorted datasets.

### 2. **[[Sorting Algorithms]]**
- **Bubble Sort**: O(n²), simple but inefficient.  
- **Merge Sort**: O(n log n), stable and divide-and-conquer.  
- **Quick Sort**: O(n log n), efficient but unstable.  
- **Heap Sort**: O(n log n), in-place but unstable.

### 3. **Graph Algorithms**
- **Depth-First Search (DFS)**: Explores as far as possible, O(V + E).  
- **Breadth-First Search (BFS)**: Explores level by level, O(V + E).  
- **Dijkstra’s Algorithm**: Finds shortest paths, O((V + E) log V).  
- **Kruskal’s/Prim’s Algorithm**: Finds minimum spanning trees.

### 4. **Dynamic Programming**
- Solves problems by breaking them into overlapping subproblems.  
  Examples: Fibonacci, Knapsack problem.

### 5. **Greedy Algorithms**
- Makes locally optimal choices at each step.  
  Examples: Huffman Coding, Activity Selection.

---

## Relationship Between Algorithms and [[Data Structures]]

- **[[Data Structures]]**: Provide efficient storage and access mechanisms.
- **Algorithms**: Use [[Data Structures]] to manipulate and solve problems.

**Example**:
- Searching: Binary Search requires a sorted array (data structure).
- Pathfinding: Dijkstra’s Algorithm uses a graph (data structure) for traversal.

---

## Comparison of Common [[Data Structures]] and Algorithms

| **Category**    | **Data Structure** | **Algorithm**           | **Use Case**                              |
|------------------|--------------------|--------------------------|-------------------------------------------|
| **Search**       | Array, Linked List| Binary Search, DFS       | Finding elements in sorted/unsorted data. |
| **Sort**         | Array              | Merge Sort, Quick Sort   | Organizing data efficiently.              |
| **Graph**        | Graph              | BFS, Dijkstra’s Algorithm| Pathfinding, network analysis.            |
| **Priority**     | Heap               | Heap Sort                | Priority queues, event handling.          |
| **Strings**      | Trie               | Pattern Matching         | Autocomplete, searching prefixes.         |

---

## Importance in Technical Interviews

1. **Problem Solving**:
   - Understanding how to pair algorithms with the right [[Data Structures]].

2. **Optimization**:
   - Writing efficient, scalable solutions.

3. **Real-World Applications**:
   - Knowledge of [[Data Structures]] and algorithms is essential for system design, database queries, and software engineering.

---

## Summary

**[[Data Structures]]** provide ways to store and organize data, while **algorithms** provide ways to manipulate and process that data. Together, they are the backbone of efficient problem-solving in computer science, making them critical for both theoretical understanding and practical applications in technical interviews and real-world development.

---
# Related Topics
##


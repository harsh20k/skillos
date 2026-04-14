---
creation date: 2024-12-18 08:41
modification date: Wednesday 18th December 2024 08:41:13
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
# Overview of Searching Algorithms

**Searching algorithms** are used to find the location of a specific element (or elements) in a data structure such as an array, list, or tree. These algorithms are fundamental in computer science and form the basis for many real-world applications.

---

## Categories of Searching Algorithms

### 1. **Linear Search**
- **Description**: Scans each element in the data structure sequentially until the target is found or the end is reached.
- **Best Case**: O(1) (target is the first element).
- **Worst Case**: O(n) (target is the last element or not present).
- **Use Case**: Small, unsorted datasets.

---

### 2. **[[Binary search]]**
- **Description**: Efficiently searches for a target in a sorted array by dividing the search interval in half at each step.
- **Best Case**: O(1) (target is at the middle).
- **Worst Case**: O(log n) (halves the search space at each iteration).
- **Use Case**: Large, sorted datasets.

---

### 3. **Jump Search**
- **Description**: Skips fixed intervals (jumps) in a sorted array to narrow down the search space, then performs a linear search within the reduced space.
- **Time Complexity**: O(√n).
- **Use Case**: Sorted datasets where binary search is less optimal.

---

### 4. **Interpolation Search**
- **Description**: A variant of binary search that calculates the probable position of the target based on the value (useful for uniformly distributed sorted datasets).
- **Best Case**: O(log log n).
- **Worst Case**: O(n) (when data is skewed).
- **Use Case**: Sorted datasets with uniformly distributed values.

---

### 5. **Exponential Search**
- **Description**: Expands the search range exponentially and then applies binary search within the determined range.
- **Best Case**: O(log n).
- **Use Case**: Large sorted datasets where the target is near the beginning.

---

### 6. **Hash-Based Search**
- **Description**: Uses a [[Hash Table]] to map keys to values for constant-time average search.
- **Time Complexity**:
  - Average: O(1).
  - Worst Case: O(n) (hash collisions).
- **Use Case**: Fast lookups in unordered data.

---

### 7. **Depth-First Search (DFS)**:
- **Description**: Traverses a graph or tree by exploring as far down a branch as possible before backtracking.
- **Time Complexity**: O(V + E) (vertices + edges).
- **Use Case**: Pathfinding, puzzle-solving, tree traversal.

---

### 8. **Breadth-First Search (BFS)**:
- **Description**: Traverses a graph or tree level by level, exploring neighbours before children.
- **Time Complexity**: O(V + E).
- **Use Case**: Shortest path in unweighted graphs.

---

## Comparison of Searching Algorithms

| **Algorithm**        | **Best Case** | **Worst Case** | **Sorted Required?** | **Use Case**                       |
| -------------------- | ------------- | -------------- | -------------------- | ---------------------------------- |
| Linear Search        | O(1)          | O(n)           | No                   | Small, unsorted datasets           |
| Binary Search        | O(1)          | O(log n)       | Yes                  | Large, sorted datasets             |
| Jump Search          | O(√n)         | O(√n)          | Yes                  | Sorted datasets                    |
| Interpolation Search | O(log log n)  | O(n)           | Yes                  | Uniformly distributed sorted data  |
| Exponential Search   | O(log n)      | O(log n)       | Yes                  | Large datasets, unknown range size |
| Hash-Based Search    | O(1)          | O(n)           | No                   | Fast lookups in unordered data     |
| DFS                  | O(V + E)      | O(V + E)       | No                   | Tree/graph traversal               |
| BFS                  | O(V + E)      | O(V + E)       | No                   | Shortest path in unweighted graphs |

---

## Real-World Applications

1. **Database Queries**: Searching for records using index structures like binary trees or hash tables.
2. **Pathfinding**: BFS and DFS for shortest paths and navigation systems.
3. **Autocomplete**: Hash-based searching for predictive text.
4. **File Systems**: Searching for files and directories using DFS/BFS.

---

## Summary

The choice of a searching algorithm depends on:
- The size and nature of the data (sorted vs unsorted).
- The need for efficiency (time and space constraints).
- The use case (e.g., traversal, real-time search).

Mastering the key searching algorithms ensures strong problem-solving skills in interviews and real-world scenarios.


---
# Related Topics
### [[Sorting Algorithms]]


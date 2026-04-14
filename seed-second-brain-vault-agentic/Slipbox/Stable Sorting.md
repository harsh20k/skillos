---
creation date: 2024-12-17 16:48
modification date: Tuesday 17th December 2024 16:48:10
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
# What is Stable [[Sorting Algorithms]]?

A **stable [[Sorting Algorithms]] algorithm** preserves the **relative order** of records with equal values. In simpler terms, if two elements are equal and one appears before the other in the input, they will appear in the same order in the sorted output.

---

## Key Idea

For an array with **equal elements**, a stable [[Sorting Algorithms]] algorithm ensures:
- The relative position of equal elements remains **unchanged** after [[Sorting Algorithms]].

---

## Example of Stable [[Sorting Algorithms]]

### Input Array:

[ (A, 1), (B, 3), (C, 3), (D, 2) ]

Here, the tuples `(B, 3)` and `(C, 3)` have the same **key value** `3`. Notice the original order:
- `(B, 3)` appears **before** `(C, 3)`.

### [[Sorting Algorithms]] by Key Value in Ascending Order

#### **Stable [[Sorting Algorithms]]** (Preserves relative order):

[ (A, 1), (D, 2), (B, 3), (C, 3) ]

- `(B, 3)` remains **before** `(C, 3)`.

#### **Unstable [[Sorting Algorithms]]** (May change relative order):

[ (A, 1), (D, 2), (C, 3), (B, 3) ]

- `(C, 3)` appears **before** `(B, 3)`.

---

## Why is Stability Important?

1. **Preservation of Original Order**:
   - Stable [[Sorting Algorithms]] is crucial when [[Sorting Algorithms]] data based on **multiple criteria** (e.g., [[Sorting Algorithms]] by two columns in a database).

2. **Example Use Case**:
   - First, sort a list of students by **age**.
   - Then, sort by **name** while keeping the ages' relative order intact.

---

## Examples of Stable and Unstable [[Sorting Algorithms]] Algorithms

| **Stable [[Sorting Algorithms]] Algorithms** | **Unstable [[Sorting Algorithms]] Algorithms** |
| ----------------------------- | ------------------------------- |
| Bubble Sort                   | [[Quick Sort]]                      |
| Insertion Sort                | [[Heap Sort]]                       |
| Merge Sort                    | Selection Sort                  |
| TimSort                       |                                 |

---

# Conclusion

A **stable [[Sorting Algorithms]] algorithm** ensures that the relative order of equal elements is maintained in the sorted output. This property is especially useful in multi-level [[Sorting Algorithms]] or when the input data contains duplicate keys.

---
# Related Topics
### [[Sorting Algorithms]]


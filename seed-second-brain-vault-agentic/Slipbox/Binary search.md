---
creation date: 2024-12-18 08:33
modification date: Wednesday 18th December 2024 08:33:45
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
# Binary Search

## What is Binary Search?
**Binary Search** is an efficient search algorithm used to find the position of a target element in a **sorted array**. It repeatedly divides the search interval in half, reducing the search space with each iteration.

---

## Key Characteristics:
1. **Divide and Conquer**:
   - Splits the array into two halves and eliminates one half based on comparisons.
2. **Efficient**:
   - Time complexity: O(log n) (faster than linear search).
3. **Requires Sorted Array**:
   - Works only on arrays that are sorted in ascending or descending order.

---

## How Binary Search Works:

1. **Initialization**:
   - Start with two pointers: `low` (beginning of the array) and `high` (end of the array).
2. **Find Middle**:
   - Compute the middle index: `mid = (low + high) // 2`.
3. **Compare**:
   - If `array[mid] == target`, return `mid` (target found).
   - If `array[mid] < target`, search the right half (`low = mid + 1`).
   - If `array[mid] > target`, search the left half (`high = mid - 1`).
4. **Repeat**:
   - Continue until `low > high` (target not found).

---

## Pseudocode

```plaintext
FUNCTION binary_search(array, target):
    low = 0
    high = LENGTH(array) - 1

    WHILE low <= high:
        mid = (low + high) // 2
        IF array[mid] == target:
            RETURN mid
        ELSE IF array[mid] < target:
            low = mid + 1
        ELSE:
            high = mid - 1

    RETURN -1  // Target not found
END FUNCTION
```

**Example**:

**Array**:
```
[2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
```

**Target**:
```
23
```

**Steps**:
1.	low = 0, high = 9, mid = 4 (value = 16) → Target > 16 → Search right half.
2.	low = 5, high = 9, mid = 7 (value = 45) → Target < 45 → Search left half.
3.	low = 5, high = 6, mid = 5 (value = 23) → Target found at index 5.

## Time and Space Complexity:

| **Operation**    | **Complexity**                          |
| ---------------- | --------------------------------------- |
| Best Case        | O(1)                                    |
| Average Case     | O(log n)                                |
| Worst Case       | O(log n)                                |
| Space Complexity | O(1) (iterative) / O(log n) (recursive) |

---
## Advantages:
1.	Efficiency: Significantly faster than linear search for large datasets.
2.	Simplicity: Easy to implement and debug.

## Disadvantages:
1.	Requires Sorted Array: Data must be sorted beforehand.
2.	Not Suitable for Unordered Data: Sorting introduces overhead if the data is not pre-sorted.

## Use Cases:
•	Searching for a value in large, sorted datasets (e.g., phonebooks, sorted arrays).
•	Useful in solving problems like finding square roots or determining the closest match.

# Summary:

Binary Search is a fast and efficient algorithm for finding a target in a sorted array. It reduces the problem size logarithmically, making it an essential tool in programming and technical interviews.




---
# Related Topics
### [[Search Algorithms]]


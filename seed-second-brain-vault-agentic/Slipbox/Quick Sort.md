---
creation date: 2024-12-17 17:18
modification date: Tuesday 17th December 2024 17:18:33
tags:
  - slipbox/permaNotes/DalhousieInterview
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
# Quick Sort

## What is Quick Sort?

**Quick Sort** is a **divide and conquer** sorting algorithm that works by selecting a **pivot element**, partitioning the array into two subarrays (elements smaller than the pivot and elements larger than the pivot), and recursively sorting the subarrays. It is efficient, widely used, and performs well on average with **O(n log n)** time complexity.

---

## Key Characteristics of Quick Sort

1. **Divide and Conquer**:
   - Divides the problem into smaller subproblems, sorts them, and combines the results.

2. **In-Place**:
   - Requires a constant amount of extra memory for sorting.

3. **Unstable**:
   - It does not preserve the relative order of equal elements.

4. **Efficient**:
   - On average, Quick Sort performs better than other sorting algorithms for large datasets.

---

## Steps of Quick Sort

1. **Choose a Pivot**:
   - Select a pivot element from the array.  
   - Common strategies:
     - Last element
     - First element
     - Random element
     - Median-of-three (middle of first, last, and middle element)

2. **Partition the Array**:
   - Rearrange the elements so that:
     - Elements smaller than the pivot are on the left.
     - Elements larger than the pivot are on the right.
   - Place the pivot in its correct position.

3. **Recursively Sort**:
   - Apply Quick Sort on the left and right subarrays.

---

## Pseudocode for Quick Sort

### High-Level Quick Sort

```plaintext
FUNCTION quick_sort(array, low, high):
    IF low < high:
        // Partition the array
        pivot_index = partition(array, low, high)

        // Recursively sort the left subarray
        quick_sort(array, low, pivot_index - 1)

        // Recursively sort the right subarray
        quick_sort(array, pivot_index + 1, high)
END FUNCTION
```

### Partition Function

```
FUNCTION partition(array, low, high):
    pivot = array[high]  // Choose the last element as the pivot
    i = low - 1          // Pointer for the smaller element

    FOR j FROM low TO high - 1:
        IF array[j] <= pivot:
            i = i + 1
            SWAP array[i] AND array[j]  // Swap smaller element with current element
    
    // Place the pivot in its correct position
    SWAP array[i + 1] AND array[high]
    RETURN i + 1  // Return the pivot index
END FUNCTION
```

### Explanation of the Pseudocode

1.**quick_sort** Function:
	•	Divides the array into two partitions based on the partition function.
	•	Recursively sorts the left and right partitions.
2.**partition** Function:
	•	Selects a pivot (commonly the last element).
	•	Rearranges the array so that elements smaller than the pivot are placed before it, and elements larger than the pivot are placed after it.
	•	Places the pivot in its correct sorted position.

### Example of Quick Sort

**Initial Array:**

[10, 7, 8, 9, 1, 5]

#### Step-by-Step Execution:

1.	Choose Pivot: 5 (last element).
2.	Partition Step:
		- Rearrange array so that elements ≤ 5 are on the left and elements > 5 are on the right.
		- After partition: [1, 5, 8, 9, 10, 7].
		- Pivot 5 is now at index 1.
3.	Recursively Sort Left Subarray: [1] → Already sorted.
4.	Recursively Sort Right Subarray: [8, 9, 10, 7].
		- Choose pivot 7, partition → [7, 8, 9, 10].
		- Repeat for subarrays until fully sorted.

**Final Sorted Array:**

[1, 5, 7, 8, 9, 10]

---
## Time and Space Complexity

| **Complexity** | **Type**   | **Time Complexity	Space Complexity** |
| -------------- | ---------- | ------------------------------------ |
| Best Case      | O(n log n) | O(log n)                             |
| Average Case   | O(n log n) | O(log n)                             |
| Worst Case     | O(n²)      | O(log n)                             |

- **Best and Average Case:**
	- Occurs when the pivot divides the array into nearly equal halves.
	- Results in O(n log n) performance.
- **Worst Case:**
	- Occurs when the pivot always results in one empty subarray (e.g., when the array is already sorted or all elements are identical).
	- Leads to O(n²) performance.
- **Space Complexity:**
	- O(log n) due to the recursive call stack.

---
## Advantages of Quick Sort

1.	Fast in Practice:
	•	Performs better than other O(n log n) algorithms, such as merge sort, for large datasets.
2.	In-Place:
	•	Requires no additional memory, saving space.
3.	Efficient for Large Arrays:
	•	Works well with modern cache systems and memory hierarchies.

---
## Disadvantages of Quick Sort
1.	Worst-Case Performance:
	•	Can degrade to O(n²) if the pivot is poorly chosen.
2.	Unstable:
	•	Does not maintain the relative order of equal elements.
3.	Recursive Overhead:
	•	Excessive recursion can lead to stack overflow for very large arrays.

---
## When to Use Quick Sort?
- When an in-place sorting algorithm is required.
- For large datasets where the average-case time complexity O(n log n) is acceptable.
- When stability is not a concern.

# Conclusion

Quick Sort is a highly efficient and widely used sorting algorithm due to its average-case performance of O(n log n) and minimal memory usage. Its divide-and-conquer approach makes it an excellent choice for large datasets, although care must be taken with pivot selection to avoid the worst-case scenario. Despite its instability, Quick Sort remains one of the fastest general-purpose sorting algorithms.




---
# Related Topics
### [[Sorting Algorithms]]
### [[Data Structures]]
### [[Quick Sort Code]]



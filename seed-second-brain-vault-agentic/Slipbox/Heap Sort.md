---
creation date: 2024-12-17 11:25
modification date: Tuesday 17th December 2024 11:25:23
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
# Heapsort

Heapsort is a comparison-based [[Sorting Algorithms]] algorithm that uses a **binary heap** data structure to efficiently organize and sort elements. It is an **in-place** [[Sorting Algorithms]] algorithm that generally performs well and guarantees O(n log n) time complexity in all cases. While it is not stable, it is often used when constant extra memory is desired since it requires only O(1) additional space.

## Key Concepts

1. **[[Heap Data Structure]]**:  
   - A heap is a specialized binary tree that satisfies the heap property:
     - **Max-Heap**: Every parent node is greater than or equal to its children.
     - **Min-Heap**: Every parent node is less than or equal to its children.
   - Heaps are typically represented as arrays for efficient indexing.

2. **Max-Heap for [[Sorting Algorithms]] in Ascending Order**:  
   - Heapsort commonly uses a **max-heap** so that the largest element is always at the root.
   - By removing the root (largest element) and placing it at the end of the array, you effectively "sort" the last element.
   - Re-heapifying (or "heapifying") ensures the next largest element moves to the root, and the process repeats until the entire array is sorted.

3. **In-Place [[Sorting Algorithms]]**:  
   - After building a max-heap, heapsort swaps the root (largest element) with the last element in the array.
   - It then reduces the heap size by one (ignoring the last element, which is now sorted) and heapifies the remaining elements.
   - This procedure continues until the entire array is sorted.

## Time and Space Complexity

- **Time Complexity**:
  - Building the heap from an array: O(n)
  - Extracting the maximum n times: O(n log n)
  - Overall complexity: O(n log n) in the worst, average, and best cases.

- **Space Complexity**:
  - O(1) auxiliary space (in-place [[Sorting Algorithms]]).

## Pseudocode

### High-Level Steps

1. **build_max_heap(array)**: Transform the array into a max-heap.
2. **for i = n-1 down to 1**:
   - Swap `array[0]` (largest element) with `array[i]`.
   - Decrease the heap size by 1.
   - **heapify(array, 0, heap_size)**: Restore the max-heap property starting from the root.

### Detailed Pseudocode

```plaintext
FUNCTION heapsort(array):
    n = LENGTH(array)

    // Step 1: Build a max-heap from the array
    build_max_heap(array, n)

    // Step 2: Repeatedly extract the maximum and heapify
    FOR i FROM n-1 DOWN TO 1:
        SWAP array[0] AND array[i]
        heap_size = i
        heapify(array, 0, heap_size)

END FUNCTION

FUNCTION build_max_heap(array, n):
    // Start from the last internal node down to the root
    FOR i FROM ⌊n/2⌋ - 1 DOWN TO 0:
        heapify(array, i, n)
END FUNCTION

FUNCTION heapify(array, index, heap_size):
    largest = index
    left = 2*index + 1
    right = 2*index + 2

    // Check if left child is larger than the parent
    IF left < heap_size AND array[left] > array[largest]:
        largest = left

    // Check if right child is larger than the current largest
    IF right < heap_size AND array[right] > array[largest]:
        largest = right

    // If largest is not the parent (index), swap and continue heapifying
    IF largest != index:
        SWAP array[index] AND array[largest]
        heapify(array, largest, heap_size)
END FUNCTION
```

## Explanation of the Pseudocode

### 1. **build_max_heap**
- Converts an unordered array into a **max-heap** by calling `heapify` from the bottom-most internal node up to the root.  
- Internal nodes are at indices `[0..⌊n/2⌋-1]`.

### 2. **heapify**
- Given an index in the heap, `heapify` ensures that the subtree rooted at that index satisfies the **max-heap property**.  
- **Steps**:  
   - Compares the node at `index` with its children.  
   - If the node is not larger than both children, it swaps with the largest child.  
   - Recursively heapifies the subtree rooted at the largest child.

### 3. **heapsort**
- **Steps**:  
   - First, build a max-heap.  
   - Then, repeatedly swap the root (max element) with the last element in the current heap and reduce the heap size by one.  
   - Call `heapify` to restore the heap property for the reduced heap.  
   - Continue until all elements are extracted, resulting in a sorted array.

---

# Why Use Heapsort?

- **Guaranteed O(n log n)**:  
  Unlike quicksort, which can degrade to O(n²) in the worst case, heapsort **always runs in O(n log n)**.
  
- **In-Place**:  
  Requires no additional arrays, saving space.

- **Not Stable**:  
  If stability is required, another [[Sorting Algorithms]] algorithm might be preferred.

---

# Conclusion

Heapsort is a reliable, in-place [[Sorting Algorithms]] algorithm that uses a **[[Heap Data Structure]]** to maintain the order of elements efficiently. While **not stable**, it provides consistent **O(n log n)** performance and minimal memory overhead. This makes it suitable for situations where **guaranteed worst-case performance** and **space efficiency** are essential.
# Related Topics
### [[Sorting Algorithms]]
### [[Sorting Algorithms#a. TimSort|Tim Sort]]
### [[Heap Data Structure]]


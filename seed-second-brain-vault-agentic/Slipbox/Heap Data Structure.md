---
creation date: 2024-12-17 11:30
modification date: Tuesday 17th December 2024 11:30:31
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/algorithms
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
# Heap Data Structure

## Definition
A **heap** is a specialized **tree-based data structure** that satisfies the **heap property**. Heaps are primarily used to implement priority queues and efficiently manage dynamic datasets where finding the minimum or maximum element is critical.

A heap is typically implemented as a **binary heap** and stored as an array for ease of access and traversal.

---

## Types of Heaps

### 1. **Max-Heap**
- In a **max-heap**, the **parent node** is always **greater than or equal** to its children.  
- The largest element is at the root of the heap.

#### **Max-Heap Property**:
For any node `i`:

array[i] ≥ array[2i + 1] (left child)
array[i] ≥ array[2i + 2] (right child)

### 2. **Min-Heap**
- In a **min-heap**, the **parent node** is always **smaller than or equal** to its children.  
- The smallest element is at the root of the heap.

#### **Min-Heap Property**:
For any node `i`:

array[i] ≤ array[2i + 1] (left child)
array[i] ≤ array[2i + 2] (right child)

---

## Representation of a Heap

A heap is usually implemented using an **array**. The tree structure is mapped to the array as follows:

### Mapping:
1. **Root Node**: Stored at index `0`.
2. **Parent Node**: At index `i`.
3. **Left Child**: At index `2*i + 1`.
4. **Right Child**: At index `2*i + 2`.

### Example: Max-Heap Representation

For the array ` [40, 20, 30, 10, 15, 25, 5]`, the max-heap tree structure looks like this:

        40
      /    \
    20      30
   /  \    /  \
 10   15  25   5

- Parent `40` is greater than its children `20` and `30`.  
- This property is recursively true for all parent-child relationships in the heap.

---

## Operations on Heap

### 1. **Insertion**
- Insert a new element at the end of the heap (array).  
- "Heapify Up" or "Bubble Up" the element to restore the heap property.  
- Time Complexity: **O(log n)**.

**Steps**:
1. Add the element at the end of the array.
2. Compare it with its parent node.
3. If the heap property is violated, swap the element with its parent.
4. Repeat until the heap property is restored.

### 2. **Deletion (Extract Max/Min)**
- Remove the root element (largest in max-heap or smallest in min-heap).  
- Replace the root with the last element of the heap and "Heapify Down" to restore the heap property.  
- Time Complexity: **O(log n)**.

**Steps**:
1. Replace the root node with the last element in the array.
2. Reduce the size of the heap by 1.
3. "Heapify Down" the new root to maintain the heap property.

### 3. **Heapify**
- **Heapify Up**: Moves an element up the tree to restore the heap property after insertion.
- **Heapify Down**: Moves an element down the tree to restore the heap property after deletion.

### 4. **Build Heap**
- Construct a heap from an unsorted array by applying `heapify` from the bottom-most non-leaf nodes to the root.  
- Time Complexity: **O(n)**.

### 5. **Peek**
- Returns the root element without removing it.  
- Time Complexity: **O(1)**.

---

## Applications of Heap

1. **Priority Queues**:
   - Implemented using heaps to efficiently access the highest (max-heap) or lowest (min-heap) priority element.

2. **Heapsort**:
   - A [[Sorting Algorithms]] algorithm that uses a heap to sort elements in O(n log n) time.

3. **Dijkstra's Algorithm**:
   - Uses a priority queue (min-heap) to find the shortest paths in a graph.

4. **Dynamic Median Finding**:
   - A combination of max-heap and min-heap can be used to maintain the median of a stream of numbers.

5. **Scheduling Algorithms**:
   - Used in CPU scheduling and job prioritization.

6. **Kth Largest/Smallest Element**:
   - Heaps provide an efficient way to find the kth largest or smallest element in a dataset.

---

## Advantages of Heap

- **Efficient Operations**: Insertion, deletion, and access to the largest or smallest element have logarithmic time complexity O(log n).
- **Space-Efficient**: Heap operations are performed in-place using arrays.

---

## Disadvantages of Heap

- **Not Suitable for Search**: Unlike balanced binary search trees, heaps are not efficient for searching arbitrary elements (O(n) time complexity).
- **Unstable Sort**: When used in [[Sorting Algorithms]] (heapsort), the relative order of equal elements is not preserved.

---

## Pseudocode for Max-Heap Operations

### Build Max-Heap

```plaintext
FUNCTION build_max_heap(array, n):
    FOR i FROM ⌊n/2⌋ - 1 DOWN TO 0:
        heapify(array, i, n)
END FUNCTION
```

### Heapify Down

```
FUNCTION heapify(array, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    IF left < heap_size AND array[left] > array[largest]:
        largest = left

    IF right < heap_size AND array[right] > array[largest]:
        largest = right

    IF largest != index:
        SWAP array[index] AND array[largest]
        heapify(array, largest, heap_size)
END FUNCTION
```

### Insert into Heap

```
FUNCTION insert(array, value):
    array.APPEND(value)
    index = LENGTH(array) - 1

    WHILE index > 0 AND array[PARENT(index)] < array[index]:
        SWAP array[PARENT(index)] AND array[index]
        index = PARENT(index)
END FUNCTION
```

### Time and Space Complexity of Heap Operations

| **Operation**        | **Time Complexity** | **Space Complexity** |
|-----------------------|---------------------|----------------------|
| **Insertion**         | O(log n)            | O(1)                |
| **Deletion**          | O(log n)            | O(1)                |
| **Build Heap**        | O(n)                | O(1)                |
| **Heapify**           | O(log n)            | O(1)                |
| **Peek (Get Max/Min)**| O(1)                | O(1)                |

# Conclusion

The heap data structure is a powerful tool for efficiently implementing priority queues and solving problems requiring frequent access to the minimum or maximum element. Heaps are widely used in algorithms like heapsort, Dijkstra’s shortest path, and dynamic median finding. Its logarithmic performance for insertion and deletion makes it an essential tool in competitive programming and real-world applications.


# Related Topics
### [[Data Structures]]



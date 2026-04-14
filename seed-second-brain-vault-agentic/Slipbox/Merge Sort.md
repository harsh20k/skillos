---
creation date: 2024-12-17 14:47
modification date: Tuesday 17th December 2024 14:47:52
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
---
# Merge Sort

## What Is Merge Sort?

**Merge Sort** is a **divide and conquer** [[Sorting Algorithms]] algorithm that splits the input array into smaller subarrays, sorts them, and then merges the sorted subarrays to produce the final sorted array. It is a **stable** and **comparison-based** [[Sorting Algorithms]] algorithm with a guaranteed time complexity of **O(n log n)** in all cases.

---
## Key Characteristics of Merge Sort

1. **Divide and Conquer**:
   - The array is repeatedly divided into two halves until each subarray has only one element.
   - Subarrays are then merged in a sorted manner.

2. **[[Stable Sorting]]**:
   - Maintains the relative order of equal elements.

3. **Not In-Place**:
   - Requires additional memory to store temporary subarrays during the merging process.

---
## Steps of Merge Sort

1. **Divide**:
   - Split the array into two halves recursively until each subarray contains a single element.

2. **Conquer**:
   - Sort and merge the subarrays in a sorted order.

3. **Combine**:
   - Combine the sorted subarrays to form the final sorted array.

---

## Merge Sort Pseudocode

### High-Level Pseudocode

```plaintext
FUNCTION merge_sort(array, left, right):
    IF left < right:
        mid = (left + right) // 2

        // Recursively sort the left half
        merge_sort(array, left, mid)

        // Recursively sort the right half
        merge_sort(array, mid + 1, right)

        // Merge the two sorted halves
        merge(array, left, mid, right)
END FUNCTION
```

### Merge Function Pseudocode

```
FUNCTION merge(array, left, mid, right):
    n1 = mid - left + 1   // Length of left half
    n2 = right - mid      // Length of right half

    // Create temporary arrays
    left_array = array[left...mid]
    right_array = array[mid+1...right]

    i = 0   // Index for left_array
    j = 0   // Index for right_array
    k = left   // Index for the main array

    // Merge left_array and right_array back into array
    WHILE i < n1 AND j < n2:
        IF left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i = i + 1
        ELSE:
            array[k] = right_array[j]
            j = j + 1
        k = k + 1

    // Copy any remaining elements of left_array
    WHILE i < n1:
        array[k] = left_array[i]
        i = i + 1
        k = k + 1

    // Copy any remaining elements of right_array
    WHILE j < n2:
        array[k] = right_array[j]
        j = j + 1
        k = k + 1
END FUNCTION
```
---

### Explanation of Pseudocode

1.	merge_sort Function:
	•	Divides the array into two halves: [left...mid] and [mid+1...right].
	•	Recursively sorts each half.
	•	Merges the two sorted halves using the merge function.
2.	merge Function:
	•	Creates two temporary arrays to store the left and right halves.
	•	Merges the two arrays into the main array while maintaining sorted order.
	•	Copies any remaining elements from the left or right array if one side is exhausted.


### Example of Merge Sort

Initial Array: [38, 27, 43, 3, 9, 82, 10]
		
1.	Divide Step:
	
	[38, 27, 43, 3, 9, 82, 10]
	      /                 \
	[38, 27, 43, 3]       [9, 82, 10]
	   /       \            /       \
	[38, 27] [43, 3]     [9, 82]   [10]
	  /  \      /  \       /  \
	[38] [27] [43] [3]   [9] [82] [10]


2.	Merge Step:
	•	Merge [38] and [27] → [27, 38]
	•	Merge [43] and [3] → [3, 43]
	•	Merge [9] and [82] → [9, 82]
Combining:
	•	Merge [27, 38] and [3, 43] → [3, 27, 38, 43]
	•	Merge [9, 82] and [10] → [9, 10, 82]
Final Merge:
	•	Merge [3, 27, 38, 43] and [9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]

Final Sorted Array: [3, 9, 10, 27, 38, 43, 82]

---

### Time and Space Complexity of Merge Sort

| **Complexity Type**      | **Time Complexity** | **Space Complexity** |
| ------------------------ | ------------------- | -------------------- |
| **Best Case**            | O(n log n)          | O(n)                 |
| **Average Case**         | O(n log n)          | O(n)                 |
| **Worst Case**           | O(n log n)          | O(n)                 |
| **Worst Case for Space** | -                   | O(n)                 |
#### **Time Complexity:**
•	Dividing the array takes O(log n) steps.
•	Merging takes O(n) time for each level of recursion.
•	Total time complexity: O(n log n).
#### **Space Complexity:**
•	Requires O(n) additional space for temporary arrays.

---
## Advantages of Merge Sort
1.	Stable: Maintains the relative order of equal elements.
2.	Predictable Time Complexity: Always runs in O(n log n) time, regardless of the input.
3.	Suitable for Linked Lists: Merge sort is efficient for [[Sorting Algorithms]] linked lists as it does not require random access.

---
## Disadvantages of Merge Sort
1.	Space Requirement: Requires O(n) additional memory, which can be significant for large datasets.
2.	Slower for Small Arrays: Merge Sort has overhead due to recursive calls, making it slower than simpler algorithms like Insertion Sort for small datasets.

---
## When to Use Merge Sort?
•	When stability is required.
•	For [[Sorting Algorithms]] large datasets where worst-case time guarantees are necessary.
•	When [[Sorting Algorithms]] linked lists, as Merge Sort does not rely on random access.

---
# Conclusion

Merge Sort is a powerful, stable, and efficient [[Sorting Algorithms]] algorithm that guarantees O(n log n) time complexity. Its divide-and-conquer approach ensures predictable performance, making it suitable for large datasets and applications where stability is important. While it has higher space requirements, its reliability makes it a preferred choice in many scenarios.


---
# Related Topics
### [[Sorting Algorithms]]
### [[Data Structures]]
### [[Heap Sort]]
### [[Merge Sort Code]]


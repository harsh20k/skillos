---
creation date: 2024-12-19 09:35
modification date: Thursday 19th December 2024 09:35:07
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - codingQuestions
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
# Problem
### You have an array of pencils' size. You need to arrange the array from smallest pencil size to largest pencil size.

## Solution
- Using [[Quick Sort]]

[[quick sorting algo]]
![[quick sorting algo]]


```pseudocode

Function QuickSort(A as Array, low ,high)
	if low < high
		// partition the array
		pivotIndex = partition(A, low, high)
		
		QuickSort(A, low, pivotIndex - 1)
		
		QuickSort(A, pivotIndex + 1, high)
End Function

function partition(a as array, low as int, high as int)
	pivot = a[High]
	leftWall = low -1
	for i from low to high -1 
		if a[i] <= pivot
			leftWall ++
			SWAP a[i] and a[leftWall]
		
	SWAP a[high] and a[leftWall+1]
	return leftWall + 1
			
	
	

```

## Python Code

![[Pasted image 20241219161529.jpg]]
```python
# Partition Function
def partition(A, low, high):
	pivot = A[high] # setting the pivot to the righmost 
	leftWall = low-1 # pointer for the smaller element
	
	for i in range(low, high):
		if A[i] <= pivot:        # element is larger than pivot
			leftWall = leftWall +1 #increment leftwall for swapping      
			A[i], A[leftWall] = A[leftWall], A[i] #swap larger element to the right
			
	A[leftWall+1], A[high] = A[high], A[leftWall+1] #swap pivot at correct pos
	return leftWall+1

# Quick Sort Function
def quickSort(A, low, high):
    if low < high:  # Base case for recursion
        # Partition the array and get the pivot index
        pivotIndex = partition(A, low, high)
        # Recursively sort the left and right subarrays
        quickSort(A, low, pivotIndex - 1)
        quickSort(A, pivotIndex + 1, high)

# D
```output
Original Array: [10, 5, 2, 6, 8, 5]
Sorted Array: [2, 5, 5, 6, 8, 10]
```
river Code
A = [10, 5, 2, 6, 8, 5]
print("Original Array:", A)
quickSort(A, 0, len(A) - 1)
print("Sorted Array:", A)

```
```output
Original Array: [10, 5, 2, 6, 8, 5]
Sorted Array: [2, 5, 5, 6, 8, 10]
```

### My algo 
- Divide
	- select the pivot usually rightmost
	- divide the array into parts left part should have smaller elements and right part should have larger elements than pivot
	- place the pivot in its correct sorted order.
- Conquer
	- recursively call the quicksort algorithm on the left array and the right arrays.
	- When only single values are left then go combine
- combine
	- combine the arrays (combining is implicit since sorting is in place)
- base case
	- if the array has one or no values it is already sorted.

# Related Topics
### [[Sorting Algorithms]]
### [[Quick Sort]]
### [[TimSort]]


---
creation date: 2024-12-19 18:48
modification date: Thursday 19th December 2024 18:48:47
tags:
  - slipbox/permaNotes/DalhousieInterview
  - codingQuestions
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
# Algorithm

![[Drawing 2024-12-19 18.23.07.excalidraw]]

## My Algorithm
- Divide
	- Divide the array into two subarrays from the middle, left and right subarray
	- Recursively call mergesort on the left and right subarrays
- Conquer
	- continue splitting the arrays until we have only one or no elements in the subarrays
- Merge
	- Put the elements in the subarrays in their sorted order 
		- compare elements of each subarrays and put the smaller in the left 
		- continue until all the elements in the subarrays are put in the new array
- base case 
	- when there is only one or no elements in the subarrays it is already sorted

### My Pseudocode

```
#merge sort
function mergesort(arr as array) 
	if lenght of arr > 1
		mid = lenght(arr)/2
		leftarr = mergesort(arr[0,mid])
		rightarr = mergesort(arr[mid+1,0])
		
		//merge the two sorted subarrays
		i = 0
		j= 0
		k = 0 
		while i<length(leftarr) and j<length(rightarr)
			if leftarr[i] <= rightarr[j]
				arr[k] = leftarr[i]
				i++
			else 
				arr[k] = rightarr[j]
				j++
			k++
		//check if both arrays have any leftover elements
		while i<length(leftarr)
			arr[k] = leftarr[i]
			i ++ k++
		while j<length(rightarr)
			arr[k] = rigtharr[j]
			j++ k++
	return arr
```


### My Code

![[Pasted image 20241220114324.jpg]]
  
```python
def mergeArrays(left_half, right_half):  
    # Merging the sorted halves  
    i = j = k = 0  
    merged = [0] * (len(left_half) + len(right_half))  # Initialize with the correct size  
    # Copy data to temp arrays left_half and right_half    while i < len(left_half) and j < len(right_half):  
        if left_half[i] < right_half[j]:  
            merged[k] = left_half[i]  
            i += 1  
        else:  
            merged[k] = right_half[j]  
            j += 1  
        k += 1  
  
    # Checking for any leftover elements in left_half  
    while i < len(left_half):  
        merged[k] = left_half[i]  
        i += 1  
        k += 1  
  
    # Checking for any leftover elements in right_half  
    while j < len(right_half):  
        merged[k] = right_half[j]  
        j += 1  
        k += 1  
    return merged  
  
# Merge Sort Function  
def mergeSort(arr):  
    if len(arr) > 1:  
        # Finding the middle of the array  
        mid = len(arr) // 2  
  
        # Dividing the array elements into two halves  
        left_half = arr[:mid]  
        right_half = arr[mid:]  
  
        # Recursively sorting the two halves  
        left_half = mergeSort(left_half)  
        right_half = mergeSort(right_half)  
  
        return mergeArrays(left_half, right_half)  
    return arr  
  
  
# Driver Code  
arr = [12, 11, 13, 5, 6, 7]  
print("Original Array:", arr)  
arr = mergeSort(arr)  
print("Sorted Array:", arr)
```
```output
```

---
# Related Topics
##


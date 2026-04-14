---
creation date: 2024-12-20 11:59
modification date: Friday 20th December 2024 11:59:11
tags:
  - slipbox/permaNotes/DalhousieInterview
  - codingQuestions
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
# Insertion Sort algo

1. **Iterate Through the Array**:
	- Start with the second element (index 1) as the first element is considered sorted.
	- Let the current element be the **key**.
1. **Compare with Sorted Subarray**:
	- Compare the **key** with the elements of the sorted subarray (elements before the key).
2. **Shift Elements**:
	- If the current element in the sorted subarray is greater than the **key**, shift it one position to the right.
3. **Insert the Key**:
	- Insert the **key** into its correct position within the sorted subarray.
4. **Repeat**:
	- Repeat steps 2–4 for all elements in the array.
5. **Base Case**:
	- If the array has 0 or 1 elements, it is already sorted.

[[Quick sort algo diagram]]
![[Quick sort algo diagram]]

### My Code

![[Pasted image 20241220181916.jpg|center]]

```python
def insertionsort(arr):  
    key = 1  
  
    while key<len(arr):  
        currentValue = arr[key]  
        i  = key-1  
        while i>=0 and arr[i] > currentValue:  
            arr[i+1] = arr[i]  
            i-=1  
        arr[i+1] = currentValue  
        key+=1  
    return arr
    
    
    # Driver Code  
arr = [12, 11, 13, 5, 8, 7]  
print("Original Array:", arr)  
arr = insertionsort(arr)  
print("Sorted Array:", arr)
```
```output
Original Array: [12, 11, 13, 5, 8, 7]
Sorted Array: [5, 7, 8, 11, 12, 13]
```


---
# Related Topics
### [[Insertion Sort Code]]


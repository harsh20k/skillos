---
creation date: 2024-12-28 09:14
modification date: Monday 30th December 2024 10:37:22
tags:
  - "#inbox/fleetingNotes/tempWriting"
description:
dg-publish: true
---
```
function quick_sort(array, low , high):
	if low<high:
		pivot_index = partition(array, low, high)
		quick_sort(array, low, pivot_index)
		quick_sort(array, pivot_index, high)

function partition(array, low, high):
	pivot = array[high]
	leftwall = low-1
	
	for i from low to high-1:
		if array[i] <=pivot:
			leftwall ++
			swap array[leftwall] and array[i]
	
	swap array[leftwall+1] and array[high]
	return leftwall+1
End Function
	
	```
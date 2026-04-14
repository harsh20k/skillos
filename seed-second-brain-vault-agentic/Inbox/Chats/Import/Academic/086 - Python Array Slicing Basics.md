---
title: Python Array Slicing Basics
category: Academic
priority: Medium
starred: None
created: 2024-07-03T05:00:30.889282
updated: 2024-07-03T05:05:51.882206
dg-publish: true
---
# Python Array Slicing Basics

**Priority:** Medium

## Conversation

### Assistant

In the given example, the slice notation `array[-3:]` is used to extract a subset of the array starting from the third last element to the end of the array.

### Explanation

- **Array**: `[0, 1, 2, 3, 4, 5]`
- **Slice Notation**: `array[-3:]`

### Breakdown
1. **Negative Indexing**: In Python, negative indices are used to access elements from the end of the list. For example:
    - `array[-1]` is the last element, which is `5`.
    - `array[-2]` is the second last element, which is `4`.
    - `array[-3]` is the third last element, which is `3`.

2. **Start Index**: `-3` means the slicing starts from the third last element, which is `3`.

3. **Stop Index**: Omitting the stop index means the slice goes until the end of the array.

### Result
- Starting from the third last element (`3`), and going to the end of the array, the elements are `[3, 4, 5]`.

### Visual Representation
- The original array: `[0, 1, 2, 3, 4, 5]`
- Indices: ` [ 0, 1, 2, 3, 4, 5]`
- Negative Indices: `[-6,-5,-4,-3,-2,-1]`

So, `array[-3:]` picks elements starting from index `-3` to the end, resulting in `[3, 4, 5]`.

### Code Example
Here’s how it works in code:
```python
array = [0, 1, 2, 3, 4, 5]
slice = array[-3:]
print(slice)  # Output: [3, 4, 5]
```

This is a convenient way to access the last few elements of a list without needing to know its exact length.

---


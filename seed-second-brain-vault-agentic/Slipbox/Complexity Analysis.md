---
creation date: 2024-12-17 09:05
modification date: Tuesday 17th December 2024 09:05:20
tags:
  - slipbox/permaNotes/DalhousieInterview
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
# Big O Notation and Time/Space Complexity Analysis
## What Is Big O Notation?

**Big O Notation** is a mathematical concept used to describe the **upper bound** of an algorithm's running time or space requirements in terms of the size of the input data, denoted as `n`. It provides a high-level understanding of the algorithm's efficiency and scalability by characterizing its performance relative to input size.

### Key Characteristics
- **Abstract Measurement**: Focuses on the growth rate of an algorithm rather than exact execution time.

- **Worst-Case Scenario**: Typically represents the maximum time or space an algorithm could take.

- **Simplification**: Ignores constant factors and lower-order terms to highlight the most significant factors affecting performance.

### Common Big O Classifications


| Big O Notation | Description                          | Example Algorithms              |
| -------------- | ------------------------------------ | ------------------------------- |
| **O(1)**       | Constant time                        | Accessing an array element      |
| **O(log n)**   | Logarithmic time                     | Binary Search                   |
| **O(n)**       | Linear time                          | Linear Search, Bubble Sort      |
| **O(n log n)** | Log-linear time                      | [[Merge Sort]], [[Quick Sort]]          |
| **O(n²)**      | Quadratic time                       | Selection Sort, Insertion Sort  |
| **O(2ⁿ)**      | Exponential time                     | Recursive Fibonacci             |
| **O(n!)**      | Factorial time                       | Traveling Salesman Problem      |

## Time Complexity Analysis

**Time Complexity** measures the amount of **time an algorithm takes** to complete as a function of the length of the input. It provides insights into how the runtime increases with larger inputs.

### Components
1. **Best-Case**: The minimum time required for an algorithm to complete.
2. **Average-Case**: The expected time over all possible inputs.
3. **Worst-Case**: The maximum time an algorithm could take.

### Examples

#### Constant Time (O(1))

```python
def get_first_element(arr):
	return arr[0]
	```
• **Explanation**: Retrieves the first element regardless of the array size.
#### Linear Time (O(n))

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```
• **Explanation**: Iterates through each element once.

#### Logarithmic Time (O(log n))

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```python
```

• **Explanation**: Divides the search interval in half each step.


## Space Complexity Analysis

**Space Complexity** measures the amount of **memory an algorithm uses** relative to the input size. It accounts for both the auxiliary space (extra space used by the algorithm) and the space used by the inputs.

**Components**
1. **Fixed Part**: Space required for constants, simple variables, fixed-size variable components.
2. **Variable Part**: Space required for dynamically allocated variables based on input size.

#### Examples

#### Constant Space (O(1))
```python
def is_even(n):
	return n % 2 == 0
```
  
• Explanation: Uses a fixed amount of space regardless of input size.
#### Linear Space (O(n))

```python
def create_copy(arr):
	return arr.copy()
```

• Explanation: Creates a copy of the input array, requiring space proportional to n.

#### Quadratic Space (O(n²))

```python
def create_matrix(n):
	return [[0 for _ in range(n)] for _ in range(n)]
```

• Explanation: Creates a 2D matrix with n² elements.

# Why It’s Relevant in Technical Interviews

Understanding Big O Notation and performing time and space complexity analyses are crucial for several reasons:

1. **Algorithm Selection**:
• Choosing the most efficient algorithm based on input size and constraints.
• Demonstrating knowledge of trade-offs between different algorithms.
2. **Optimization**:
• Identifying bottlenecks in existing solutions.
• Improving the performance of code by reducing time or space complexity.
3. **Problem Solving**:
• Structuring solutions that scale well with larger inputs.
• Ensuring that solutions are feasible within given resource limits.
4. **Communication**:
• Clearly articulating the efficiency of your solutions to interviewers.
• Showing an understanding of underlying computational principles.

### Example Interview Question

#### **Problem**: Given an unsorted array of integers, find all pairs that sum up to a specific target.
#### Approach and Analysis:
1. **Brute Force**:
• **Algorithm**: Check all possible pairs.
• **Time Complexity**: O(n²)
• **Space Complexity**: O(1)
2. **Using a Hash Set**:
• **Algorithm**: Iterate through the array, store elements in a hash set, and check for the complement.
• **Time Complexity**: O(n)
• **Space Complexity**: O(n)
3. **[[Sorting Algorithms]] and Two Pointers**:
• **Algorithm**: Sort the array and use two pointers to find pairs.
• **Time Complexity**: O(n log n) (due to [[Sorting Algorithms]])
• **Space Complexity**: O(1) or O(n) depending on the [[Sorting Algorithms]] algorithm used.
**Discussion**:
• The hash set approach offers the best time complexity at O(n) but requires additional space.
• The [[Sorting Algorithms]] approach balances time and space but has a higher time complexity due to [[Sorting Algorithms]].

# Conclusion
Big O Notation and time/space complexity analyses are fundamental tools for evaluating and comparing the efficiency of algorithms. Mastery of these concepts enables you to:
• **Design Optimal Solutions**: Choose the right algorithms and [[Data Structures]] for the problem at hand.
• **Communicate Effectively**: Clearly explain the efficiency and trade-offs of your solutions.
• **Perform Well in Interviews**: Demonstrate a deep understanding of algorithmic efficiency, which is highly valued in technical assessments.
Investing time to thoroughly understand these concepts will significantly enhance your problem-solving skills and improve your performance in technical interviews.

# Related Topics
##


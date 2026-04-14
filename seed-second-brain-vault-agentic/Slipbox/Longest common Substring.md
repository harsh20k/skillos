---
creation date: 2024-12-21 09:29
modification date: Saturday 21st December 2024 09:29:28
tags:
  - slipbox/permaNotes/DalhousieInterview
  - codingQuestions
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

# ChatGpt Code

```python
# Dynamic Programming Approach
def longest_common_substring_dp(strings):
    if not strings:
        return ""

    # Start with the first string
    reference = strings[0]
    longest_substring = ""

    for i in range(len(reference)):
        for j in range(i + 1, len(reference) + 1):
            candidate = reference[i:j]

            # Check if candidate is in all other strings
            if all(candidate in string for string in strings[1:]):
                if len(candidate) > len(longest_substring):
                    longest_substring = candidate

    return longest_substring

# Input strings
input_strings = ["abcdex", "abfdex", "abdexyz"]

# Find LCS using DP
print("Longest Common Substring (DP):", longest_common_substring_dp(input_strings))

```
```output
Longest Common Substring (DP): aLongest Common Substring (DP): ab
Longest Common Substring (DP): dex
Longest Common Substring (DP): dex
b
```

## Concise code 

![[Pasted image 20241222110510.jpg]]

```python
# concise code
def lcs(strings):  
    if len(strings) == 0 :  
        print("NA")  
    else:  
        first = strings[0]  
        substrings = {strings[0][i:j] for i in range(len(strings[0])) for j in range(i+1, len(strings[0])+1) }  
        for string in strings[1:]:  
            substrings &= {string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)}  
        print (max(substrings,key=len,default=""))  
  
# Example usage  
input_strings = ["abcdex", "abfcdex", "abcdexxyz"]  
lcs(input_strings)
```
```output
cdex
```


---
# Related Topics
### [[Suffix Tree]]
### [[Ukkonen's Algorithm]]
### [[Dynamic Programming]]
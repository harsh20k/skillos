---
creation date: 2024-12-20 18:51
modification date: Friday 20th December 2024 20:45:40
tags:
  - slipbox/permaNotes/DalhousieInterview
  - codingQuestions
  - slipbox/permaNotes/datastructures
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/python
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


# Algo 
[[Drawing 2024-12-20 18.51.30.excalidraw]]
![[Drawing 2024-12-20 18.51.30.excalidraw]]
# Code

![[Pasted image 20241220204301.jpg|555|center]]


```python
# code for counting unique characters in an input string  
# for example input = "hello hello" and output should be 4 for four unique characters in the string.  
  
def countcharacters(inString):  
    uniquecharacters = set() #set to store unique values  
  
    for char in inString:  
        if char != " ":  
            uniquecharacters.add(char)  
  
    print (uniquecharacters)  
    return (len(uniquecharacters))  
  
  
inputstring = "hello hellohellohellohello hellohello"  
print (countcharacters(inputstring))
```


---
# Related Topics 
### [[Hash Function]]
### [[Hash Table]]
### [[Data Structures#3. **Hash-Based Data Structures**]]
### [[Set and Dictionary in Python]]
---
creation date: 2024-12-21 09:24
modification date: Saturday 21st December 2024 09:24:39
tags:
  - slipbox/permaNotes/DalhousieInterview
  - codingQuestions
  - slipbox/permaNotes/datastructures
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
# My Code
![[Pasted image 20241221092453.jpg|center]]

![[Pasted image 20241222182648.jpg]]

```python
# code for counting frequency of characters in an array of strings  
def characterFrequency(input):  
    # use dictionary hashmap for storing characters and their frequency  
    charfreq= {}  
  
    for string in input:  
        for char in string:  
            if(char!=" "):  
                charfreq[char] = charfreq.get(char,0) + 1  
    print(charfreq)  
  
inputstring = ["hello", "do you know me", "hi", "how are you"]  
print(inputstring)  
  
characterFrequency(inputstring)
```

```python
# code for counting unique characters in an input string  
# for example input = "hello hello" and output should be 4 for four unique characters in the string.  
  
def count_characters(inString):  
    char_count = {}  
    for char in inString:  
        if char!= " ":  
            char_count[char] = char_count.get(char, 0) + 1  
    return(char_count)  
  
def count_words(inString):  
    word_count = {}  
    words = inString.split()  
    for word in words:  
        word_count[word] = word_count.get(word, 0) + 1  
    print(word_count)  
  
def count_word(inString, searchWord):  
    word_count = 0  
    words = inString.split()  
    for word in words:  
        if word == searchWord:  
            word_count += 1  
    print( word_count)  
  
  
input_string = "hello je hellohellohellohello hello hello how je"  
print ("character frequency:")  
print(count_characters(input_string))  
count_words(input_string)  
count_word(input_string,"hello")
```


---
# Related Topics
### [[Dictionary]]
### [[Hash Table]]


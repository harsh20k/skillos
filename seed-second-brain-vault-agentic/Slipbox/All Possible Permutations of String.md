---
creation date: 2024-12-21 18:59
modification date: Saturday 21st December 2024 18:59:10
tags:
  - slipbox/permaNotes/DalhousieInterview
  - codingQuestions
  - slipbox/permaNotes/codingConcepts
description: "Problem: To enlist all the permutaions of a string in an array."
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
# Code

![[Pasted image 20241222193440.jpg]]

## Algo
![[Pasted image 20241222193551.jpg]]


```python
def permutee(string, fixed= ""):  
    if len(string) == 0:  
        print(fixed)  
        return  
  
    for i in range(len(string)):  
         permutee(string[:i]+ string[i+1:],fixed+string[i])  
  
permutee("abc")  

```
```output
hello
helol
hello
helol
heoll
heoll
hlelo
hleol
hlleo
hlloe
hloel
hlole
hlelo
hleol
hlleo
hlloe
hloel
hlole
hoell
hoell
holel
holle
holel
holle
ehllo
ehlol
ehllo
ehlol
eholl
eholl
elhlo
elhol
ellho
elloh
elohl
elolh
elhlo
elhol
ellho
elloh
elohl
elolh
eohll
eohll
eolhl
eollh
eolhl
eollh
lhelo
lheol
lhleo
lhloe
lhoel
lhole
lehlo
lehol
lelho
leloh
leohl
leolh
llheo
llhoe
lleho
lleoh
llohe
lloeh
lohel
lohle
loehl
loelh
lolhe
loleh
lhelo
lheol
lhleo
lhloe
lhoel
lhole
lehlo
lehol
lelho
leloh
leohl
leolh
llheo
llhoe
lleho
lleoh
llohe
lloeh
lohel
lohle
loehl
loelh
lolhe
loleh
ohell
ohell
ohlel
ohlle
ohlel
ohlle
oehll
oehll
oelhl
oellh
oelhl
oellh
olhel
olhle
olehl
olelh
ollhe
olleh
olhel
olhle
olehl
olelh
ollhe
olleabc
acb
bac
bca
cab
cba
h
```


```
abc  
fix: a   permute: bc  
         b   c             abc  
         c   b             acb  
fix: b   permute: ac  
         a   c             bac  
         c   a             bca  
fix: c   permute: ab  
         a   b             cab  
         b   a             cba
```

---
# Related Topics
##


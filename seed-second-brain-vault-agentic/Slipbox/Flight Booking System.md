---
creation date: 2024-12-21 11:07
modification date: Saturday 21st December 2024 11:07:43
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
# My code
![[Pasted image 20241221185234.jpg|481 center]]

```python
## code for Random Flight booking system  
import random  
def assignTickets(num, persons, flights, seats):  
  
    ## without replacement if we want with replacement we can use random.choice()  
    selectedperson = random.sample(persons,2)  
    print(selectedperson)  
  
    selectedseats = set() # (flight,seat)  
    results = []  
  
    for person in selectedperson:  
        while True:  
            selectflight = random.choice(flights)  
            selectseat = random.choice(seats)  
            ticket = (selectflight,selectseat)  
  
            if ticket not in selectedseats:  
                selectedseats.add(ticket)  
                results.append((person,selectflight,selectseat))  
                break  
    print(results)  
  
## Driver code  
persons = ["Alice", "Bob", "Charlie", "David", "Eve"]  
flights = ["Flight1", "Flight2", "Flight3", "Flight4"]  
seats = ["Seat1", "Seat2", "Seat3"]  
  
assignTickets(2, persons, flights, seats)
```

### random.choice, random.choices, random.sample



---
# Related Topics
### [[Random Function]]


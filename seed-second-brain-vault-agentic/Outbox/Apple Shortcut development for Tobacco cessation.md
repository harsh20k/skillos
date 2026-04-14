---
creation date: 2025-01-08 11:15
modification date: Wednesday 8th January 2025 11:15:36
tags:
  - "#outbox/projectNotes"
  - "#inbox/health/harsh/tobaccoConsumption"
description: A shortcut to create a full fledged workflow for tobacco cessation.
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
# Primary Objective

The objective of creating this shortcut was to somehow help me with Tobacco cessation. I created this after I got my apple watch. 

By documenting and tracking my tobacco consumption I can gradually reduce the timer functionality slowly to completely taper off the tobacco consumption. 

Timer functionality in the shortcut creates a some sort of cue to stop the chewing and spit the tobacco. This might help in slowly tightening the timer to zero. 

---
# Current State _2025-01-08_

Currently the shortcuts does the following.
- It checks the time of the day and calculates a day part that varies from 0 to 4.
- Based on the day-part variable and timer dosage variable the timer value is being calculated whose value varies from min-timer value to maximum of 5 minutes.
- There is also functionality to start DND mode on the devices based on the timer value. 

---
# Improvements Needed

- I need to somehow **document** the number of times the shortcut was run everyday, and if possible to also store the number of seconds for which the chewing session went on.
- **Gradual reduction** of timer over the months, maybe?
- After each session probably notify me with some **positive quote** like "Great Job! One step closer to quitting." for encouraging the user to keep using the timer with the chewing habit.

# Modifications

> [!POINT]
> ## 1. Set the timer so it gradually reduces from max to min values and be controlled by only these two variables. 









---
# Related Topics
###

---
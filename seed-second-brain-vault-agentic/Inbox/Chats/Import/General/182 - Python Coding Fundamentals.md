---
title: Python Coding Fundamentals
category: General
priority: Medium
starred: None
created: 2025-02-18T06:38:00.249801
updated: 2025-03-14T12:55:10.014028
dg-publish: true
---
# Python Coding Fundamentals

**Priority:** Medium

## Conversation

### Assistant

### **Session 3: Lists, Loops & More Problem-Solving**  
**Goal:** Strengthen understanding of lists, loops, and problem-solving by working with real-world scenarios.  

---

### **1. Quick Recap (5 mins)**
- Ask: **"What did you find easy/hard in the last session?"**  
- Review **functions and conditions** with a quick question:  
  - **Q:** "What does this function return?"  
    ```python
    def check(num):
        if num % 2 == 0:
            return "Even"
        return "Odd"
    
    print(check(7))
    ```  

---

### **2. Deep Dive into Lists (15 mins)**
- **Explain List Basics** with examples:
  ```python
  numbers = [10, 20, 30, 40]
  print(numbers[0])  # First element
  print(len(numbers))  # List length
  ```
- **Looping through Lists:**  
  ```python
  for num in numbers:
      print(num)
  ```
- **Practice Task:**  
  Write a function that **takes a list of numbers and returns their sum**.

---

### **3. Common List Operations (15 mins)**
- **Adding & Removing Elements:**
  ```python
  nums = [1, 2, 3]
  nums.append(4)  # [1, 2, 3, 4]
  nums.pop(1)  # Removes 2
  ```
- **Sorting a List:**
  ```python
  nums = [3, 1, 4, 2]
  nums.sort()  # [1, 2, 3, 4]
  ```
- **Practice Task:**  
  Write a function that **finds the largest number in a list**.

---

### **4. Nested Loops & 2D Lists (15 mins)**
- Introduce **nested loops** with a real-world example:  
  - Example: **Matrix (2D List) Traversal**  
    ```python
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    for row in matrix:
        for num in row:
            print(num, end=" ")
    ```
- **Practice Task:**  
  Write a function that prints a **3x3 number grid** using nested loops.

---

### **5. Mini Challenge (10 mins)**
- **Task 1:** Write a function that **counts how many times a number appears** in a list.  
- **Task 2:** Write a function that **reverses a list without using `.reverse()`**.

---

### **6. Recap & Homework (10 mins)**
- **Summarize:** Lists help store multiple values, and loops help process them efficiently.  
- **Homework Task:**  
  - Write a function that finds the **second largest number** in a list.  
  - Try solving **FizzBuzz** again but using a loop from 1 to 50.

---

Would you like to introduce **dictionaries** in the next session, or should we reinforce list manipulation more? 🚀

---


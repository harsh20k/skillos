---
title: Python Control Structures Plan
category: Academic
priority: Medium
starred: None
created: 2025-01-21T11:02:34.553370
updated: 2025-01-23T08:21:34.366643
dg-publish: true
---
# Python Control Structures Plan

**Priority:** Medium

## Conversation

### Assistant

Here are some fun and interesting example questions for kids to find the output of simple Python programs using `if-else`, `for`, and `while` loops. These examples include relatable and engaging themes like games, counting, and fun scenarios.

---

### **1. If-Else Questions**
#### Example 1: Is it a holiday?
```python
day = "Sunday"
if day == "Sunday":
    print("Yay! It's a holiday!")
else:
    print("Time for school!")
```

**Question:** What will be the output of the code?

---

#### Example 2: Detecting a superhero!
```python
name = "Spiderman"
if name == "Spiderman":
    print("Superhero detected!")
else:
    print("Just a normal person.")
```

**Question:** What will the code print if the name is "Spiderman"? What if the name is "John"?

---

#### Example 3: Candy Sharing
```python
candies = 8
if candies % 2 == 0:
    print("You can share candies equally.")
else:
    print("Oops! Someone will get one extra.")
```

**Question:** What will the program output if `candies = 7`?

---

### **2. For Loop Questions**
#### Example 1: Counting stars ⭐
```python
for i in range(1, 6):
    print("⭐" * i)
```

**Question:** What will be the output of this program?

---

#### Example 2: Multiplication table of 3
```python
for i in range(1, 6):
    print(f"3 x {i} = {3 * i}")
```

**Question:** Write the output for the first 5 multiples of 3.

---

#### Example 3: Counting down for a rocket launch 🚀
```python
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```

**Question:** What will the output of the program be?

---

### **3. While Loop Questions**
#### Example 1: Collecting coins in a game
```python
coins = 0
while coins < 5:
    coins += 1
    print(f"Coins collected: {coins}")
```

**Question:** How many times will the loop run? What will the final output be?

---

#### Example 2: Guess the secret number 🔢
```python
secret_number = 7
guess = 5
while guess != secret_number:
    print("Wrong guess, try again!")
    guess += 1
print("You guessed it!")
```

**Question:** If the starting value of `guess` is 5, how many times will the loop run?

---

#### Example 3: Climbing stairs 🪜
```python
step = 1
while step <= 5:
    print(f"Climbing step {step}")
    step += 1
```

**Question:** What will the program output?

---

### **Bonus: Mix of For and If-Else**
#### Example 1: Sorting odd and even numbers
```python
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

**Question:** What will the program print?

---

These questions are simple, engaging, and help kids connect programming to real-life scenarios, making learning enjoyable and intuitive!

---


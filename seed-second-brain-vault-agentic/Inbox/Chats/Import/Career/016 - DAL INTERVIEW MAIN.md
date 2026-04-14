---
title: DAL INTERVIEW MAIN
category: Career
priority: Medium
starred: None
created: 2024-12-15T09:49:10.251233
updated: 2025-01-22T12:06:39.459208
dg-publish: true
---
# DAL INTERVIEW MAIN

**Priority:** Medium

## Conversation

### Assistant

Here’s an example of a Python program that uses `if`, `elif`, and nested `if` statements:

```python
# Program to determine ticket price based on age and time of the day

age = int(input("Enter your age: "))
time = input("Enter the time of day (morning, afternoon, evening): ").lower()

# Outer if-elif to check age groups
if age < 12:
    ticket_price = 5
    if time == "morning":
        ticket_price -= 1  # Discount for morning shows
    elif time == "evening":
        ticket_price += 2  # Extra charge for evening shows
elif 12 <= age < 18:
    ticket_price = 10
    if time == "afternoon":
        ticket_price -= 2  # Discount for afternoon shows
elif age >= 18:
    ticket_price = 15
    if time == "evening":
        if age > 60:  # Nested if for senior citizens in evening
            ticket_price -= 3  # Discount for seniors
        else:
            ticket_price += 2  # Regular extra charge for evening shows
else:
    ticket_price = 0  # Invalid input case

# Output the ticket price
print(f"The ticket price for you is: ${ticket_price}")
```

---

### **Example Outputs**

#### **Input:**
```plaintext
Enter your age: 10
Enter the time of day (morning, afternoon, evening): morning
```

**Output:**
```plaintext
The ticket price for you is: $4
```

---

#### **Input:**
```plaintext
Enter your age: 65
Enter the time of day (morning, afternoon, evening): evening
```

**Output:**
```plaintext
The ticket price for you is: $12
```

---

This example demonstrates a combination of `if`, `elif`, and nested `if` statements to calculate ticket prices based on age and time of the day with discounts or extra charges applied.

---


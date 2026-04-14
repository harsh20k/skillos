---
title: Decorator pattern in Python
category: Academic
priority: Medium
starred: None
created: 2025-08-30T01:48:18.733497
updated: 2025-08-30T01:52:17.392210
dg-publish: true
---
# Decorator pattern in Python

**Priority:** Medium

## Conversation

### Assistant

Here’s the simplest **recursive function** for the **nth Fibonacci number** in Python:  

```python
def fib(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Example: 6th Fibonacci number
print(fib(6))  # Output: 5
```

---

## 🔎 Explanation
- Fibonacci sequence starts as:  
  `0, 1, 1, 2, 3, 5, 8, ...`  
- Defined by the recurrence:  
  \[
  F(n) = F(n-1) + F(n-2)
  \]  
- Base cases:  
  - `F(1) = 0`  
  - `F(2) = 1`  

---

⚠️ **Note:** This naive recursion has **exponential time complexity \(O(2^n)\)** because it recalculates the same values many times.  

👉 If you’d like, I can also show you **optimized versions**:
- Using **memoization** (`functools.lru_cache`)  
- Or **dynamic programming** (bottom-up, \(O(n)\))  

Would you like me to show you those efficient versions too?

---


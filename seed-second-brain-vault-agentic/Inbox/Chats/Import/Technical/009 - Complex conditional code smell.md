---
title: Complex conditional code smell
category: Technical
priority: Medium
starred: None
created: 2025-11-25T15:53:03.888166
updated: 2025-11-25T15:53:18.999628
dg-publish: true
---
# Complex conditional code smell

**Priority:** Medium

## Conversation

### Assistant

A **complex conditional** is a **code smell** that occurs when an `if`, `else if`, or `while` condition becomes too long, too nested, or too hard to understand at a glance.

### What makes a conditional “complex”
A conditional is considered complex when it has things like:

- **Many logical operators** (`&&`, `||`, `!`)
- **Nested conditions** inside other conditions
- **Long boolean expressions** involving multiple variables
- **Comparisons repeated in multiple places**
- **Mixed responsibility** (e.g., doing validation + business logic in the same condition)

Example of a complex conditional:

```python
if (age > 18 and user.is_active and (plan == "premium" or (plan == "basic" and not user.is_suspended)) and not user.has_unpaid_dues):
    allow_access()
```

This is hard to read, debug, and maintain.

---

### Why it’s a code smell
- Hard to understand what the condition is actually checking.
- Easy to introduce bugs.
- Difficult to extend or change without breaking something.
- Makes business rules unclear or inconsistent.

---

### How to fix (refactor)
Common refactoring techniques:

#### 1. **Extract condition into a well-named function**
```python
if user_is_eligible(user):
    allow_access()
```

#### 2. **Break down into intermediate boolean variables**
```python
has_valid_plan = plan == "premium" or (plan == "basic" and not user.is_suspended)
no_dues = not user.has_unpaid_dues

if age > 18 and user.is_active and has_valid_plan and no_dues:
    allow_access()
```

#### 3. **Replace conditionals with polymorphism** (for more complex rules)

#### 4. **Use enums / strategies instead of nested checks**

---

### In short
**A complex conditional code smell means the condition is hard to read, hard to reason about, and should be simplified or decomposed so the intention is clear.**

---


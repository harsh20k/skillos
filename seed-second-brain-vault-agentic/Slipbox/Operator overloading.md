---
creation date: 2024-12-18 21:00
modification date: Wednesday 18th December 2024 21:00:57
tags:
  - slipbox/permaNotes/DalhousieInterview
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
# Operator Overloading

## What is Operator Overloading?

**Operator overloading** is a feature in some programming languages that allows **custom implementation** of standard operators (like `+`, `-`, `*`, etc.) for user-defined types (e.g., classes or structs). It enables operators to be redefined to perform operations on objects in a meaningful way.

---

## Key Features of Operator Overloading

1. **Custom Behavior**:
   - Allows operators to perform operations on objects instead of primitive types.

2. **Improves Readability**:
   - Makes object-oriented code more intuitive by allowing operators to work seamlessly with user-defined types.

3. **Supported in Certain Languages**:
   - Languages like C++, Python, and Kotlin support operator overloading.
   - Not supported in Java (except for string concatenation using `+`).

---

## Example: Operator Overloading in C++

```cpp
#include <iostream>
using namespace std;

class Complex {
public:
    float real, imag;

    Complex(float r, float i) : real(r), imag(i) {}

    // Overloading the '+' operator
    Complex operator+(const Complex& other) {
        return Complex(real + other.real, imag + other.imag);
    }

    void display() {
        cout << real << " + " << imag << "i" << endl;
    }
};

int main() {
    Complex c1(2.5, 3.5), c2(1.5, 2.5);
    Complex c3 = c1 + c2;  // Using overloaded '+' operator
    c3.display();  // Output: 4.0 + 6.0i
    return 0;
}
```

### Explanation:
- The + operator is overloaded to add two Complex objects by summing their real and imag parts.

---
## Operator Overloading in Python

```
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Using overloaded '+' operator
print(v3)  # Output: (4, 6)
```

### Explanation:
- The + operator is overloaded using the __add__ method to add two Vector objects.

---
## Benefits of Operator Overloading
1.	Intuitive Code:
- Allows objects to behave like built-in types with operators.
2.	Improved Readability:
- Reduces the complexity of function calls (e.g., add(a, b) becomes a + b).
3.	Encapsulation:
- Encapsulates behavior inside the class, promoting cleaner design.

---
## Drawbacks of Operator Overloading
1.	Potential Misuse:
- Can lead to confusion if operators are overloaded in a non-intuitive way.
2.	Increased Complexity:
- Adds additional logic to the class, which may complicate debugging.
3.	Not Universal:
- Not all languages support operator overloading (e.g., Java).

## Supported Operators (Examples)

| **Language** | **Operators That Can Be Overloaded**                     |
| ------------ | -------------------------------------------------------- |
| *C++*          | Arithmetic (+, -, *, /), Relational (==, <), etc.        |
| *Python*       | Arithmetic (__add__, __sub__), Comparison (__eq__), etc. |

---
## Summary
- Definition: Operator overloading allows redefining standard operators for user-defined types.
- Use Case: Improves code readability and functionality in object-oriented programming.
- Example: Overloading + to add two objects like Complex or Vector.

## Key Takeaway:

Operator overloading enhances customizability in programming, but it should be used judiciously to maintain code clarity and prevent misuse.




---
# Related Topics
### [[Polymorphism]]



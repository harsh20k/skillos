---
creation date: 2024-12-18 15:16
modification date: Wednesday 18th December 2024 15:16:31
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/codingConcepts
  - slipbox/permaNotes/datastructures
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

# What is a Wrapper Class in Java?

A **wrapper class** in Java is an object representation of a primitive data type. It allows primitive data types like `int`, `char`, `float`, etc., to be treated as objects. Each primitive type has a corresponding wrapper class in the `java.lang` package.

---

## List of Primitive Types and Their Wrapper Classes

| **Primitive Type** | **Wrapper Class** |
| ------------------ | ----------------- |
| `byte`             | `Byte`            |
| `short`            | `Short`           |
| `int`              | `Integer`         |
| `long`             | `Long`            |
| `float`            | `Float`           |
| `double`           | `Double`          |
| `char`             | `Character`       |
| `boolean`          | `Boolean`         |

---

## Key Features of Wrapper Classes

1. **Convert Primitives to Objects**:
   - Enables primitives to be treated as objects.
   - Example: Using collections like `ArrayList` that work with objects, not primitives.

2. **Provide Utility Methods**:
   - Wrapper classes include methods to perform conversions (e.g., `parseInt()`, `valueOf()`).

3. **Immutability**:
   - Wrapper objects are immutable, meaning their values cannot be changed after creation.

4. **Autoboxing and Unboxing**:
   - **Autoboxing**: Automatic conversion of primitives to their corresponding wrapper class.
   - **Unboxing**: Automatic conversion of wrapper objects back to primitives.

---

## Example: Using Wrapper Classes

### 1. **Primitive to Wrapper Object**
```java
int num = 10;
Integer obj = Integer.valueOf(num);  // Explicit boxing
```

2. Wrapper Object to Primitive

```java
Integer obj = 10;
int num = obj.intValue();  // Explicit unboxing
```

3. Autoboxing and Unboxing

```java
int num = 20;
Integer obj = num;  // Autoboxing
int primitiveNum = obj;  // Unboxing
```

Use Cases of Wrapper Classes
1.	Collections:
- Collections like ArrayList and HashMap work only with objects, requiring wrapper classes for primitives.

```java
ArrayList<Integer> numbers = new ArrayList<>();
numbers.add(10);  // Autoboxing
```

2.	Data Conversion:
- Convert between strings and primitive types using utility methods.

```java
String str = "100";
int num = Integer.parseInt(str);  // Converts string to int
```

3.	Default Values in Generics:
- Generics require objects, so wrapper classes are used for primitive types.
4.	Multi-threading:
- Wrappers are used in scenarios requiring immutability or object synchronization.

---
## Advantages of Wrapper Classes
1.	**Object-Oriented:**
- Treats primitive types as objects, enhancing compatibility with Java’s OOP features.
2.	**Utility Methods:**
- Provides useful methods for type conversion and operations.
3.	**Collections Compatibility:**
- Enables storage of primitives in collections.
4.	**Default Null Handling:**
- Wrapper objects can have a null value, unlike primitives.

---
## Disadvantages of Wrapper Classes
1.	**Memory Overhead:**
- Objects consume more memory compared to primitive types.
2.	**Performance:**
- Slower than primitives due to boxing and unboxing.

---
## Summary

A wrapper class in Java bridges the gap between primitive data types and objects. They provide utility methods for type conversion, allow compatibility with collections, and support Java’s object-oriented programming features. While convenient, they come with performance and memory trade-offs.

| **Primitive Type** | **Wrapper Class** | **Key Use**                                |
| ------------------ | ----------------- | ------------------------------------------ |
| *int*                | Integer           | Use in collections, parsing, and utilities |
| *char*               | Character         | Use in text processing                     |
| *boolean*            | Boolean           | Use in conditions, collections             |


---
# Related Topics
### [[Abstraction]]
### [[Encapsulation]]
### [[Data Structures]]


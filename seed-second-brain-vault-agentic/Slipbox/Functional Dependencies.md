---
creation date: 2024-12-16 11:43
modification date: Monday 16th December 2024 11:43:52
tags:
  - slipbox/permaNotes/DalhousieInterview
  - "#slipbox/permaNotes/databaseconcepts"
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
# Definition

A ****functional dependency**** (FD) is a relationship between two sets of attributes in a database. It specifies that the value of one attribute (or group of attributes) determines the value of another attribute (or group of attributes).

In simple terms, if you know the value of one attribute (or a set of attributes), you can uniquely determine the value of another attribute. Functional dependencies are a key concept in ****database normalization****, helping to reduce redundancy and ensure data integrity.

---
## **Notation of Functional Dependencies**

A functional dependency is represented as:
A → B
Where:
- `A` is a **determinant** (the attribute or set of attributes that determines another attribute).
- `B` is the **dependent** attribute, which is determined by `A`.
This means that for each value of `A`, there is exactly one corresponding value of `B`.
---
## **Examples of Functional Dependencies**
### **Example 1:**

Consider a `Student` table:

| StudentID | StudentName | Course  |
| --------- | ----------- | ------- |
| 1         | John        | Math    |
| 2         | Alice       | Science |
A functional dependency in this case could be:
StudentID → StudentName

This means that the `StudentID` uniquely determines the `StudentName`. For each `StudentID`, there will always be one corresponding `StudentName`.
### **Example 2:**
Consider an `Employee` table:

| EmployeeID | Name     | Department | Salary |
| ---------- | -------- | ---------- | ------ |
| E1         | John     | HR         | 50000  |
| E2         | Alice    | IT         | 60000  |
A functional dependency could be:

EmployeeID → Name, Department, Salary
 This means that knowing `EmployeeID` allows us to determine the `Name`, `Department`, and `Salary` associated with that employee.

---
## **Types of Functional Dependencies**
1. **Trivial Functional Dependency**:
   - A functional dependency where the dependent attribute is part of the determinant or is the same as the determinant.
   - Example: `A → A` (A trivially determines itself).
2. **Non-Trivial Functional Dependency**:
   - A functional dependency where the dependent attribute is not part of the determinant and is not the same as the determinant.
   - Example: `StudentID → StudentName`.
3. **Transitive Functional Dependency**:
   - If `A → B` and `B → C`, then `A → C` is a [[Normalisation#Transitive Dependency|transitive functional dependency]].
   - Example: If `EmployeeID → Department` and `Department → Location`, then `EmployeeID → Location` (through transitivity).
---
## **Role of Functional Dependencies in Database Design**
- **[[Normalisation]]**: Functional dependencies play a critical role in the normalization process. By identifying and analyzing functional dependencies, we can determine how to organize data into tables and reduce redundancy.
  - **[[Normalisation#1NF First Normal Form Eliminate Duplicate Columns|First Normal Form]] (1NF)**: Eliminate repeating groups.
  - **[[Normalisation#2NF Second Normal Form Remove Partial Dependencies|Second Normal Form]] (2NF)**: Eliminate partial dependencies.
  - **[[Normalisation#3NF Third Normal Form Remove Transitive Dependencies|Third Normal Form]] (3NF)**: Eliminate transitive dependencies.
- **[[Data integrity]]**: Functional dependencies help maintain the accuracy and consistency of data. They ensure that data is logically structured and can be queried efficiently.
---
## **Conclusion**
Functional dependencies describe how one attribute in a database table is related to another. Understanding and identifying functional dependencies is fundamental for designing efficient databases, reducing redundancy, and ensuring [[Data integrity]] through normalization.
# Related Topics
### [[Database design]]


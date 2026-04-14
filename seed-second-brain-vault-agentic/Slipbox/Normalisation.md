---
creation date: 2024-12-15 19:18
modification date: Sunday 15th December 2024 20:43:16
tags:
  - slipbox/permaNotes/DalhousieInterview
  - "#slipbox/permaNotes/databaseconcepts"
description: Database design process for reducing data redundancy and improving data integrity
source: "#chatgpt"
dg-publish: true
---
```table-of-contents
```
# Normalisation

Normalisation is a [[Database design]] process used to organise data to reduce redundancy and improve [[Data integrity]]. It involves structuring a database according to specific forms (normal forms), each with rules and constraints. The three most common normal forms are **1NF (First Normal Form)**, **2NF (Second Normal Form)**, and **3NF (Third Normal Form)**. Here’s what each form entails:

## 1NF First Normal Form: Eliminate Duplicate Columns
• **Requirements**:
1. Data must be stored in a **tabular format** (rows and columns).
2. Each column contains **atomic values** (no repeating groups or arrays).
3. Each row is uniquely identifiable, typically with a **primary key**.

• **Example** (Non-1NF to 1NF):
**Non-1NF (Unnormalized Table)**:

| **StudentID** | Name  | Subjects         |
| ------------- | ----- | ---------------- |
| 1             | John  | Math, Science    |
| 2             | Alice | English, History |

**1NF (Atomic Values)**:

| **StudentID** | **Name** | **Subject** |
| ------------- | -------- | ----------- |
| 1             | John     | Math        |
| 1             | John     | Science     |
| 2             | Alice    | English     |
| 2             | Alice    | History     |

---
## 2NF Second Normal Form: Remove Partial Dependencies

• **Requirements**:
1. Must meet **1NF**.
2. All non-prime attributes (attributes not part of the primary key) must depend **entirely** on the primary key (no partial dependency).

• **Example** (Breaking Partial Dependency):
**1NF**:

| **OrderID** | **ProductID** | **ProductName** | **OrderDate** |
| ----------- | ------------- | --------------- | ------------- |
| 1           | P1            | Laptop          | 2024-12-01    |
| 2           | P2            | Mouse           | 2024-12-05    |
• Problem: **ProductName** depends only on **ProductID**, not on the composite key (**OrderID, ProductID**).
**2NF**:
Separate into two tables:
**Orders Table**:  

| **OrderID** | **ProductID** | **OrderDate** |
| ----------- | ------------- | ------------- |
| 1           | P1            | 2024-12-01    |
| 2           | P2            | 2024-12-05    |

**Products Table**: 

| **ProductID** | **ProductName** |
| ------------- | --------------- |
| P1            | Laptop          |
| P2            | Mouse           |


---
## 3NF Third Normal Form: Remove Transitive Dependencies

• **Requirements**:
1. Must meet **2NF**.
2. Non-prime attributes must depend **only** on the primary key (no transitive dependency).
• **Example** (Breaking Transitive Dependency):
**2NF**:

| **EmployeeID** | **DeptID** | **DeptName**    |
| -------------- | ---------- | --------------- |
| E1             | D1         | Human Resources |
| E2             | D2         | IT              |
• Problem: **DeptName** depends on **DeptID**, which is not the primary key.
**3NF**:
Separate into two tables:
- **Employee Table**:  

**EmployeeID** | **DeptID**  
------------- | ---------  
E1            | D1  
E2            | D2  

- **Department Table**:  

**DeptID** | **DeptName**  
--------- | ---------------  
D1        | Human Resources  
D2        | IT  

**Summary of Benefits:**
• **1NF**: Ensures atomic data and a structured table format.
• **2NF**: Eliminates redundancy due to partial dependencies.
• **3NF**: Further reduces redundancy by eliminating transitive dependencies.
Proper normalisation improves database efficiency and integrity, making it easier to maintain and query the data.


---

## Partial and Transitive Dependencies

### Partial Dependency
- A **partial dependency** occurs when a **non-prime attribute** (an attribute not part of any candidate key) depends on part of a composite primary key rather than the whole key.
- Relevant in tables where the primary key is **composite** (consists of multiple attributes).

#### **Example of Partial Dependency**
**Table**: StudentCourse  

| StudentID | CourseID | CourseName | StudentName |
|-----------|----------|------------|-------------|
| S1        | C1       | Math       | John        |
| S2        | C2       | Science    | Alice       |

- **Primary Key**: (StudentID, CourseID)  
- **Dependencies**:  
  - **StudentName** depends only on **StudentID** (*partial dependency*).  
  - **CourseName** depends only on **CourseID** (*partial dependency*).

#### **Solution**
Remove partial dependencies by splitting into two tables:

1. **Student Table**:  
   | StudentID | StudentName |
   |-----------|-------------|
   | S1        | John        |
   | S2        | Alice       |

2. **Course Table**:  
   | CourseID | CourseName |
   |----------|------------|
   | C1       | Math       |
   | C2       | Science    |

This satisfies **2NF**.

---

### Transitive Dependency
- A **transitive dependency** occurs when a **non-prime attribute** depends on another non-prime attribute instead of directly on the primary key.

#### **Example of Transitive Dependency**
**Table**: Employee  

| EmployeeID | DeptID | DeptName |
| ---------- | ------ | -------- |
| E1         | D1     | IT       |
| E2         | D2     | HR       |

- **Primary Key**: EmployeeID
- **Dependencies**:  
  - **DeptName** depends on **DeptID** (not the primary key).  
  - **DeptID** depends on **EmployeeID** (primary key).  
  - This creates a transitive dependency: **EmployeeID → DeptID → DeptName**.

#### **Solution**
Remove transitive dependencies by splitting into two tables:

1. **Employee Table**:  

| EmployeeID | DeptID |
|------------|--------|
| E1         | D1     |
| E2         | D2     |

1. **Department Table**:  

| DeptID | DeptName |
| ------ | -------- |
| D1     | IT       |
| D2     | HR       |

This satisfies **3NF**.

---

## **Summary of Differences**
| **Partial Dependency**                                    | **Transitive Dependency**                                     |
| --------------------------------------------------------- | ------------------------------------------------------------- |
| A non-prime attribute depends on part of a composite key. | A non-prime attribute depends on another non-prime attribute. |
| Violates **2NF**.                                         | Violates **3NF**.                                             |
| Relevant in tables with composite keys.                   | Can occur in any table with non-prime attributes.             |

---
# Related Topics

## [[Database design]]
## [[Pillars of Database design]]
## **[[Keys and Constraints]]**
• Primary Key, Foreign Key, Composite Key, Candidate Key
• Integrity constraints (unique, not null, etc.)
## **[[Database Anomalies]]**
• Insertion, Deletion, and Update anomalies
• How normalisation helps prevent these issues.
## **[[Denormalisation]]**
• When and why [[Denormalisation]] is used.
• Trade-offs between normalisation and performance.
## **[[Functional Dependencies]]**
• How they influence normalisation.
• Identifying [[Normalisation#Partial Dependency|partial]] and [[Normalisation#Transitive Dependency|transitive]] dependencies.
## **[[Joins in SQL]]**
• The role of joins in retrieving data from normalised tables.
• Impact of [[Normalisation|normalisation]] on [[Query complexity]].
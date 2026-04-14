---
creation date: 2024-12-16 11:01
modification date: Monday 16th December 2024 11:01:45
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
# Database Anomalies

In database design, anomalies refer to the undesirable behavior or inconsistencies that arise in the database when data is inserted, deleted, or updated. These anomalies can occur in a poorly normalized database and can lead to [[Data integrity]] issues.

The three main types of database anomalies are **Insertion**, **Deletion**, and **Update** anomalies. Each type of anomaly occurs due to the improper organization of data, often caused by redundant or poorly structured data in non-normalized tables.

---

## **1. Insertion Anomaly**
- **Definition**: This occurs when it is difficult to insert data into a database due to missing or redundant information.  
- **Cause**: Insertion anomalies typically happen when there are **null values** or when data needs to be inserted into multiple places, leading to redundancy.  
- **Example**:  
  Suppose you have a table to store information about employees and the departments they belong to:

| EmployeeID | EmployeeName | DepartmentID | DepartmentName |
|------------|--------------|--------------|----------------|
| 1          | John         | D1           | HR             |
| 2          | Alice        | D2           | IT             |
  If you want to insert a new department (e.g., Marketing) but haven't assigned any employees yet, you cannot insert the department without having a corresponding employee row. This is because the `DepartmentID` is tied to the `EmployeeID`, creating an insertion anomaly.

---

## **2. Deletion Anomaly**
- **Definition**: This occurs when deleting data leads to the unintended loss of other important data.  
- **Cause**: Deletion anomalies happen when data is **tightly coupled** and deleting one record causes the loss of other relevant information.
- **Example**:  
  Continuing from the previous example, if you delete **Employee 2** (Alice), the entire department information (`DepartmentName`, `DepartmentID`) for IT will be lost as well, even though the department still exists in the system. This leads to unnecessary data loss and a deletion anomaly.

---

## **3. Update Anomaly**
- **Definition**: This occurs when updating data in one place requires making changes in multiple places, and failing to update all places leads to inconsistencies.  
- **Cause**: Update anomalies occur when data is **repeated** in multiple places, so a change needs to be made in multiple locations to maintain consistency.
- **Example**:  
  Consider the same table with employees and departments:

| EmployeeID | EmployeeName | DepartmentID | DepartmentName |
|------------|--------------|--------------|----------------|
| 1          | John         | D1           | HR             |
| 2          | Alice        | D2           | IT             |
  If the department name for IT changes (e.g., from "IT" to "Information Technology"), it must be updated in every row where the department appears. If one of the rows is missed, it leads to an **inconsistent database**. This is an update anomaly.

---

## **How to Avoid Database Anomalies**
- **Normalization**: Normalize the database to eliminate redundancy and ensure data is stored in related tables. This minimizes the chances of anomalies.
  - **First Normal Form (1NF)** eliminates repeating groups.
  - **Second Normal Form (2NF)** removes [[Normalisation#Partial Dependency|partial dependencies]].
  - **Third Normal Form (3NF)** eliminates [[Normalisation#Transitive Dependency|transitive dependencies]].

---

## **Conclusion**
Database anomalies occur due to poorly structured databases, often as a result of [[Data redundancy]]. By following proper normalization practices, these anomalies can be avoided, ensuring that the database remains consistent, efficient, and easy to maintain.

# Related Topics
### [[ACID]]
### [[Database design]]

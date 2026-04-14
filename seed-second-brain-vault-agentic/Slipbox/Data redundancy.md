---
creation date: 2024-12-16 10:29
modification date: Monday 16th December 2024 10:29:58
tags:
  - slipbox/permaNotes/DalhousieInterview
  - "#slipbox/permaNotes/databaseconcepts"
description:
dg-publish: true
---
# Data Redundancy

## **What is Data Redundancy?**
Data redundancy occurs when the same piece of data is **unnecessarily stored in multiple places** within a database. This can happen in poorly designed databases, leading to duplication and inefficiencies.

### **Example of Data Redundancy**
**Table with Redundancy**:  

| EmployeeID | EmployeeName | DepartmentID | DepartmentName |
|------------|--------------|--------------|----------------|
| 1          | John         | D1           | HR             |
| 2          | Alice        | D2           | IT             |
| 3          | Bob          | D1           | HR             |

- Here, the `DepartmentName` is repeated for each employee in the same department.

---

## **Why Do We Remove Data Redundancy?**

1. **Prevent Data Anomalies**
   - Redundancy can lead to **insertion, deletion, and update anomalies**, making the database inconsistent:
     - **Insertion Anomaly**: Adding new data might require redundant fields (e.g., adding a new department for a single employee).
     - **Update Anomaly**: Updating one instance of data (e.g., changing "HR" to "Human Resources") requires updating all duplicates.
     - **Deletion Anomaly**: Deleting a record might accidentally remove critical information (e.g., deleting the last employee in a department may remove the department name).

2. **Improve Storage Efficiency**
   - Redundant data consumes unnecessary storage, which can be costly, especially for large-scale systems.

3. **Enhance Query Performance**
   - Redundancy can slow down queries as duplicate data increases the size of tables and the complexity of processing.

4. **Ensure Data Integrity**
   - Consistency across the database becomes harder to maintain with redundant data. Eliminating redundancy helps enforce accurate relationships between data.

5. **Simplify Maintenance**
   - A normalized database with minimal redundancy is easier to maintain, update, and modify.

---

## **General Philosophy**
The goal of [[Database design]] is to achieve **a balance between redundancy and performance**:
- Use **[[Normalisation]]** to minimize redundancy and ensure [[Data integrity]].
- Opt for **[[Denormalisation]]** selectively, when performance outweighs the need for strict normalization (e.g., in read-heavy applications).

By structuring data thoughtfully, we ensure that information is stored efficiently, relationships are meaningful, and operations on the database remain consistent and reliable.

# Related Topics

## [[Database design]]

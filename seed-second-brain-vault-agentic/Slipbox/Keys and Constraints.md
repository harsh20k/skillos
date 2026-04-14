---
creation date: 2024-12-16 10:05
modification date: Monday 16th December 2024 10:05:43
tags:
  - slipbox/permaNotes/DalhousieInterview
  - slipbox/permaNotes/databaseconcepts
description: concept of keys and constraints
dg-publish: true
---
```table-of-contents
title: 
style: nestedOrderedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# Keys and Constraints

## **Keys**

1. **Primary Key**  
   - A unique identifier for each record in a table.  
   - Ensures no duplicate or null values.  
   - Example: `StudentID` in a Student table.

2. **Foreign Key**  
   - A field in one table that refers to the primary key in another table.  
   - Establishes relationships between tables.  
   - Example: `DeptID` in Employee table referencing `DeptID` in Department table.

3. **Composite Key**  
   - A primary key made up of two or more attributes.  
   - Used when a single attribute cannot uniquely identify a record.  
   - Example: `(StudentID, CourseID)` in an Enrollment table.

4. **Candidate Key**  
   - A set of attributes that can uniquely identify a record.  
   - One candidate key is chosen as the primary key.  
   - Example: In a Student table, both `StudentID` and `Email` could be candidate keys.

---

## **Integrity Constraints**

1. **Unique Constraint**  
   - Ensures all values in a column are distinct.  
   - Example: Email addresses in a User table.

2. **Not Null Constraint**  
   - Ensures a column cannot have null values.  
   - Example: `EmployeeID` must always have a value.

3. **Check Constraint**  
   - Ensures that values in a column meet a specific condition.  
   - Example: `Age > 18` for a User table.

4. **Default Constraint**  
   - Assigns a default value to a column if no value is provided.  
   - Example: `Status = 'Active'` by default.

5. **Primary Key Constraint**  
   - Combines `Unique` and `Not Null` constraints to uniquely identify records.  

6. **Foreign Key Constraint**  
   - Ensures referential integrity between two related tables.  
   - Example: Prevents deleting a department if employees are assigned to it.

# Why Do We Use Keys and Constraints in Databases?

## **Purpose of Keys**
1. **Ensure Uniqueness**  
   - Keys like **Primary Keys** and **Candidate Keys** ensure that each record in a table is uniquely identifiable.  

2. **Establish Relationships**  
   - **Foreign Keys** create and enforce relationships between tables, enabling structured and connected data storage.  

3. **Enable Efficient Data Retrieval**  
   - Keys facilitate faster searches, indexing, and querying of data within relational databases.  

4. **Prevent Duplicate Data**  
   - Keys prevent duplication of records, maintaining [[Data integrity]].

---

## **Purpose of Constraints**
1. **Maintain [[Data integrity]]**  
   - Constraints (e.g., **Not Null**, **Unique**) ensure that only valid and meaningful data is entered into the database.

2. **Enforce Business Rules**  
   - Constraints like **Check** and **Default** help enforce specific rules and conditions required by the business logic.

3. **Ensure Referential Integrity**  
   - **Foreign Key Constraints** ensure that references between tables are valid and consistent.

4. **Prevent Errors**  
   - Constraints help avoid issues like null values in critical columns or mismatched data across tables.

5. **Streamline Data Validation**  
   - Instead of validating data at the application level, constraints ensure correctness at the database level, reducing [[Data redundancy]].

# **Conclusion**
Keys and constraints are essential for ensuring the reliability, consistency, and efficiency of relational databases, allowing them to handle complex data and relationships effectively.

# Related Topics
### [[Data integrity]]
### [[Data redundancy]]
## [[Database design]]
## [[Pillars of Database design]]

## [[ACID]] transactions

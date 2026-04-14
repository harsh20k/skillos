---
creation date: 2024-12-16 11:52
modification date: Monday 16th December 2024 11:52:29
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
# Denormalisation in Database Design

## When and Why Denormalisation Is Used?

**Denormalisation** is the process of intentionally reintroducing redundancy into a database that has previously been normalized. It is employed when there is a need to improve **query performance**, especially in read-heavy or analytical scenarios.

**Reasons for Using Denormalisation:**
1. **Performance Improvement**:  
   By storing related or derived data together, the number of joins needed to fulfill queries can be reduced, thus speeding up query response times.
   
2. **Simplified Queries**:  
   Complex queries involving multiple joins become simpler when some of the necessary data is stored directly in the same table, making queries more straightforward.

3. **High Volume Reads**:  
   In environments where read operations vastly outnumber write operations (e.g., reporting databases, data warehouses), denormalisation can make common queries more efficient.

---

## Trade-offs Between Normalisation and Performance

**Normalisation** organizes data to minimize redundancy, ensure data integrity, and reduce anomalies. While this is excellent for maintaining a clean and consistent database, it can sometimes lead to slower queries due to the need for multiple joins.

**Pros of Normalisation:**
- **[[Data integrity]]**: Each piece of information is stored once, reducing inconsistencies.
- **Reduced [[Data redundancy|Redundancy]]**: Less duplicated data lowers storage costs and maintenance overhead.
- **Stable Structure**: Changes are made in a single place, reducing update, insertion, and deletion anomalies.

**Cons of Normalisation (Impact on Performance):**
- **Complex Queries**: *More normalized tables mean more joins and potentially slower query execution*.
- **Less Suited for Analytical Workloads**: Queries that need to combine large amounts of data across many tables can degrade performance.

**Denormalisation** relaxes some of these rules to speed up query responses, at the expense of creating redundant data.

**Pros of Denormalisation:**
- **Faster Queries**: Pre-joined or aggregated data reduces the need for multiple table joins.
- **Better for Analytics**: Ideal for dashboards, reporting, and read-heavy applications where performance is critical.

**Cons of Denormalisation:**
- **Redundant Data**: Data must be carefully synchronized; updates become more complex and error-prone.
- **Potential Data Inconsistency**: If one copy of the data is updated and another is not, inconsistencies can occur.
- **Increased Storage**: Storing the same data multiple times can inflate storage requirements.

---

## Conclusion

**Denormalisation** is a strategic choice to improve read performance at the cost of introducing some redundancy and potential data management complexity. It is most beneficial in systems where the priority is fast data retrieval—such as reporting, analytics, and data warehousing—while less critical for transactional systems focused on [[Data integrity]] and minimal redundancy.
# Related Topics
### [[Database design]]


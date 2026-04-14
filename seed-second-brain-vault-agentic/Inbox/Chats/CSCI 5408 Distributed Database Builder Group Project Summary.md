---
creation date: 2025-12-29 12:18
tags:
  - chat
description:
dg-publish: true
---
# CSCI 5408 – Distributed Database Builder Project (Fall 2025)

**Course:** CSCI 5408 – Data Management, Warehousing, and Analytics  
**Instructor:** Prof. Gabriel Spadon, PhD  
**Project Type:** Group Project (4–5 students)

---

## 1. Project Overview

The CSCI 5408 Group Project focuses on the end-to-end design and implementation of a **distributed database system**. The objective is to integrate theoretical and practical concepts from data modeling, database normalization, SQL schema design, and distributed data management.

Each group defines an industry-relevant problem, designs a comprehensive data model, and implements a **working distributed database prototype in Java**. The system is deployed across multiple virtual machines using **VirtualBox**, where each VM simulates an independent database node. Nodes communicate using **Java sockets**, while a **Global Data Catalog (GDC)** coordinates data location and query execution.

The emphasis of the project is on **conceptual correctness, architectural clarity, and understanding of distributed database principles**, rather than production-grade performance.

---

## 2. Project Objectives

- Design a scalable and normalized data model for a real-world problem
- Apply ER modeling principles and resolve common design issues
- Achieve at least **Third Normal Form (3NF)** through systematic normalization
- Implement SQL DDL scripts with proper constraints and relationships
- Build a distributed database using horizontal or vertical fragmentation
- Implement inter-node communication and distributed query handling
- Demonstrate understanding through documentation, reports, and presentation

---

## 3. Team Structure

- Groups consist of **4–5 students**
- Teams are **self-formed** and fixed for the duration of the project
- No reassignment of group members is permitted

---

## 4. Research and Implementation Flow

### 4.1 Background Research

Teams begin by researching their chosen domain to build foundational understanding and identify data sources. This includes:

- Identifying domain-specific entities and attributes
- Evaluating data formats (CSV, JSON, APIs, etc.)
- Assessing data relevance and reliability
- Summarizing findings in a structured table with sources and URLs

---

### 4.2 Initial Conceptual Model (ERD)

- Creation of an **Entity-Relationship Diagram (ERD)** using Chen notation
- Minimum of **20 meaningful entities**
- Clear relationships and cardinalities
- Avoidance of many-to-many relationships at the conceptual stage
- Focus on clarity over optimization

Tools such as **draw.io** are recommended for ERD creation.

---

### 4.3 Design Issue Identification

Teams critically evaluate the initial ERD to identify and resolve common modeling problems:

- **Historical Data Issues:** Missing time-based attributes or logs
- **Fan Traps:** Ambiguous 1:M relationships causing incorrect joins
- **Chasm Traps:** Missing relationships that block entity traversal
- **Redundant Entities:** Overlapping or duplicated structures
- **Complex Relationships:** Overloaded or unclear associations

Findings and corrective actions are documented in a **1-page design issues report**.

---

### 4.4 Final ERD

The refined ERD includes:

- All resolved design issues
- Clearly defined primary keys
- Composite, multivalued, and derived attributes where appropriate
- Clean, normalized structure ready for logical modeling

---

### 4.5 Logical Design and Normalization

In this phase, the conceptual model is transformed into a logical schema:

- Identification of all attributes for each entity
- Resolution of partial and transitive dependencies
- Step-by-step normalization to achieve **at least 3NF**
- Clear definition of primary and foreign keys

The normalization process is fully documented with explanations and diagrams.

---

### 4.6 DDL Implementation

Teams write **SQL DDL scripts** to implement the logical schema:

- `CREATE TABLE` statements for all relations
- Enforcement of constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `CHECK`)
- Index creation where necessary
- Referential integrity enforcement

These scripts form the foundation for the distributed implementation.

---

### 4.7 Distributed Database Implementation

The distributed database is implemented in **Java**, using **VirtualBox** to simulate multiple machines:

- At least **two virtual machines**, each acting as a database node
- Each node stores a **fragment of the data**
- Fragmentation strategies:
  - Horizontal fragmentation (row-based)
  - Vertical fragmentation (column-based)
- Data stored locally using simple file-based or serialized storage
- Nodes communicate via **Java sockets**

#### Global Data Catalog (GDC)

The GDC acts as the coordinator:

- Tracks where each data fragment is stored
- Routes queries to the appropriate node
- Coordinates distributed inserts and retrievals

The focus is on demonstrating distributed interaction, not on advanced query optimization.

---

## 5. Team Workflow Methodology

Teams follow the **Think – Pair – Share** approach:

1. **Think:** Individual research, idea exploration, and documentation
2. **Pair:** Group discussions, consolidation of ideas, and decision-making
3. **Share:** Regular feedback sessions with TAs and iterative refinement

Meeting logs, agendas, decisions, and outcomes are maintained in tabular form.

---

## 6. Project Deliverables

### Intermediate Deliverables

- Domain research summary table
- Initial ERD (Chen notation)
- Design issues report
- Meeting logs and documentation
- Logical schema and normalization report
- SQL DDL scripts
- Distributed database architecture report

---

### Final Report (10-page PDF)

The final report includes:

- Domain research summary
- Initial and final ERDs
- Design issues and resolutions
- Normalization diagrams and explanations
- Complete DDL scripts
- Description of the Global Data Catalog
- Distributed database structure and fragmentation strategy

If ERD images are unclear, separate image files are submitted.

---

## 7. Group Presentation

- **10-minute presentation** per group
- Includes **5-minute Q&A**

Presentation covers:

1. Problem statement
2. Research insights
3. ERD evolution and design decisions
4. Logical and physical implementation
5. Distributed database architecture
6. Challenges and solutions
7. Live demo or recorded demonstration

Slides are submitted as a **PDF via Brightspace**, along with any supplementary material.

---

## 8. Evaluation Criteria

- Content clarity and relevance
- Technical depth and correctness
- Quality of distributed design
- Team collaboration and balance
- Demo functionality and accuracy
- Effectiveness during Q&A

---

## 9. Outcome

By completing this project, students gain hands-on experience in **data modeling, normalization, SQL design, and distributed database systems**, bridging theoretical concepts with practical system implementation in a controlled, educational environment.


---
creation date: 2025-12-29 12:18
tags:
  - chat
description:
dg-publish: true
---
# CSCI 5308 – Advanced Topics in Software Development
## Group Project Detailed Summary

---

## 1. Project Overview

This group project was completed as part of **CSCI 5308 – Advanced Topics in Software Development** at Dalhousie University. The objective was to design, implement, and evaluate a **real‑world, distributed software system** by applying advanced software engineering principles, architectural patterns, and collaborative development practices.

Our team built a **distributed flight‑tracking and airport retail application** tailored to the **Halifax Stanfield International Airport** context. The system integrates flight information with airport shop listings, providing passengers with real‑time flight data and relevant retail options within the airport.

The project emphasized:
- Real‑world problem decomposition
- Clean architecture and modular design
- Testability and maintainability
- Team‑based software development workflows

---

## 2. Problem Statement

Modern airports host a large number of retail outlets, yet passengers often lack timely, contextual information that links their **flight status** with **available airport services and shops**. The problem addressed by this project was:

> How can flight information and airport retail data be combined into a single, scalable, and user‑friendly system that enhances passenger experience?

---

## 3. System Architecture

The system was designed using a **multi‑tier, distributed architecture**, separating concerns across frontend, backend services, and data storage.

### 3.1 High‑Level Architecture

- **Frontend (Mobile Application)**
  - Built using **React Native**
  - Provides cross‑platform support
  - Responsible for user interaction, flight search, and shop browsing

- **Backend (RESTful API Services)**
  - Developed using **Python Flask**
  - Implements business logic and orchestration
  - Exposes REST APIs for frontend consumption

- **Database Layer**
  - Relational database (PostgreSQL / MariaDB)
  - Stores flight data, shop details, and availability

- **External / Simulated Data Sources**
  - Mocked flight feeds
  - Airport retail metadata

---

## 4. Key Functional Features

### 4.1 Flight Information Module
- Search flights by number, destination, or time window
- View flight status (scheduled, delayed, departed)
- Designed for extensibility to real‑time flight APIs

### 4.2 Airport Shops Module
- List airport shops by terminal and category
- Display shop operating hours
- Filter shops based on passenger flight timing

### 4.3 Integrated User Experience
- Contextual shop suggestions based on flight departure time
- Clean, minimal mobile UI focused on usability

---

## 5. Software Engineering Practices

The project strongly emphasized **engineering discipline**, not just feature delivery.

### 5.1 Design Principles
- **Separation of Concerns**
- **Single Responsibility Principle**
- **Loose Coupling & High Cohesion**
- **Layered Architecture**

### 5.2 Design Patterns Applied
- Repository Pattern for data access
- Service Layer for business logic
- DTOs for API communication

---

## 6. Testing Strategy

Testing was treated as a first‑class concern.

- **Unit Tests** for backend services using `pytest`
- **API Testing** using Postman collections
- Validation of edge cases (invalid flight IDs, empty results)

This ensured:
- Reduced regression risk
- Confidence in refactoring
- Clear verification of business rules

---

## 7. DevOps & Tooling

### 7.1 Version Control
- Git with feature‑branch workflow
- Clear commit messages and PR reviews

### 7.2 Collaboration Tools
- GitHub Issues for task tracking
- Structured meeting notes and action items

### 7.3 Development Environment
- Local development using virtual environments
- Consistent setup across team members

---

## 8. Team Collaboration

The project was completed by a multi‑member team with clearly defined responsibilities:

- Backend API development
- Database schema design
- Frontend mobile UI
- Testing and integration
- Documentation and reporting

Regular stand‑ups and milestone reviews ensured alignment and timely delivery.

---

## 9. Challenges Faced

- Designing APIs flexible enough for future data sources
- Coordinating backend‑frontend integration
- Managing merge conflicts in a multi‑branch workflow
- Balancing feature scope with academic timelines

Each challenge was addressed through structured discussions and iterative refinement.

---

## 10. Learning Outcomes

This project significantly strengthened understanding of:

- Distributed system design
- RESTful API development
- Real‑world software architecture
- Collaborative development in a team setting
- Translating requirements into scalable solutions

---

## 11. Relevance to Industry

The project closely mirrors real‑world software systems used in:

- Travel and aviation platforms
- Retail discovery systems
- Mobile‑first SaaS products

Skills demonstrated are directly applicable to roles in:
- Full‑stack development
- Backend engineering
- Cloud‑native application development

---

## 12. Conclusion

The CSCI 5308 group project successfully delivered a **well‑architected, testable, and extensible distributed system**. Beyond the technical implementation, the project reinforced professional software engineering practices, teamwork, and system‑level thinking—making it a strong portfolio‑ready academic project.

---

*End of Document*


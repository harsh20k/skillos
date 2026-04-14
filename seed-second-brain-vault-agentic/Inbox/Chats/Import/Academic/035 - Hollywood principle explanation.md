---
title: Hollywood principle explanation
category: Academic
priority: Medium
starred: None
created: 2025-11-04T15:21:19.489890
updated: 2025-11-04T15:21:29.224419
dg-publish: true
---
# Hollywood principle explanation

**Priority:** Medium

## Conversation

### Assistant

The **Hollywood Principle** in software design means:  
**"Don’t call us, we’ll call you."**

It describes **inversion of control (IoC)** — instead of your code controlling the flow, the framework or higher-level component calls your code at the right time.  

**Example:**  
In a web framework, you don’t manually call functions to handle requests. Instead, you write handler methods, and the framework *calls them* when an HTTP request arrives.

**In short:**  
- Your code defines *what to do*.  
- The framework decides *when and how* to do it.  

Commonly used in:  
- Frameworks like Django, Spring, and React.  
- Design patterns like Template Method and Dependency Injection.

---


---
title: Broken hierarchy explanation
category: Projects
priority: Medium
starred: None
created: 2025-11-25T15:20:10.039893
updated: 2025-11-25T15:20:15.351793
dg-publish: true
---
# Broken hierarchy explanation

**Priority:** Medium

## Conversation

### Assistant

Correct answer: **Broken hierarchy**.

Explanation:  
In the scenario, `Employee` is made a subclass of `Manager`, but this violates the fundamental **IS-A relationship** required for inheritance. An employee is **not** a manager, so forcing that relationship leads to methods that don’t apply (e.g., `getReportees()`, `conductPerformanceEvaluation()`), requiring exception-throwing or NOP overrides. This is exactly what “broken hierarchy” refers to.

---


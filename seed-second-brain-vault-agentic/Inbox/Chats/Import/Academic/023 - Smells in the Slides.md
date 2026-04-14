---
title: Smells in the Slides
category: Academic
priority: Medium
starred: None
created: 2025-11-19T17:10:05.725505
updated: 2025-11-19T22:31:32.388933
dg-publish: true
---
# Smells in the Slides

**Priority:** Medium

## Conversation

### Assistant

- The project contains several implementation smells—like long methods, complex conditionals, magic numbers, and empty catch blocks—which the slides describe as early indicators of deeper design issues.  
- A few methods show higher-than-ideal complexity, matching the slide examples where long method bodies and branching logic hurt readability and maintainability.  
- Some responsibilities are spread across different components (such as scattered sorting logic), which connects directly to the “feature concentration” and “scattered functionality” architecture smells in the lecture.  
- The architecture is otherwise clean: no cyclic dependencies, no god components, and clear interfaces, aligning well with the architectural principles outlined in the slides.  
- Error handling patterns—especially empty catch blocks—stand out because the slides highlight how they hide failures and reduce the system’s overall robustness.

---


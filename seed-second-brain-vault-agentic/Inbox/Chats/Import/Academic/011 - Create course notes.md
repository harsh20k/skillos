---
title: Create course notes
category: Academic
priority: Medium
starred: None
created: 2025-12-21T09:49:32.181074
updated: 2025-12-21T10:08:48.128260
dg-publish: true
---
# Create course notes

**Priority:** Medium

## Conversation

### Assistant

Below is a **clean, production-grade QuickAdd Macro** setup that matches how you already think and work in Obsidian.

No fluff. Follow in order.

---

# Goal

**One button → choose course → new note created**
```
Courses/CSCI-5100/Notes/5100 21-12-2025.md
Courses/CSCI-5308/Notes/5308 21-12-2025.md
Courses/CSCI-5408/Notes/5408 21-12-2025.md
```

With the **right template automatically applied**.

---

## 1. Create the Macro

**QuickAdd → Manage → Add Choice → Macro**

**Name**
```
New Course Note
```

---

## 2. Macro Step 1 — Course selector

Add **Choice → Prompt → Dropdown**

**Variable name**
```
course
```

**Choices (exactly like this)**
```
CSCI-5100
CSCI-5308
CSCI-5408
```

This variable will be used everywhere else.

---

## 3. Macro Step 2 — Capture (dynamic file creation)

Add **Choice → Capture**

### Location

**Capture to** → *File*

**File path / format**
```
Courses/{{VALUE:course}}/Notes/{{VALUE:course:split("-")[1]}} {{DATE:DD-MM-YYYY}}
```

### What this does
- `{{VALUE:course}}` → `CSCI-5100`
- `split("-")[1]` → `5100`
- Final filename → `5100 21-12-2025.md`

No duplication. No hardcoding.

---

### Toggles

- **Create file if it doesn’t exist** → ✅ ON
- **Create file with given template** → ✅ ON

---

### Template path (dynamic)

```
Admin/Assets/Templates/{{VALUE:course}}-note.md
```

So:
- `CSCI-5100` → `CSCI-5100-note.md`
- `CSCI-5308` → `CSCI-5308-note.md`

---

## 4. Templates (one per course)

### Example: `CSCI-5100-note.md`

```md
---
course: CSCI 5100
date: {{DATE:YYYY-MM-DD}}
type: lecture
---

# CSCI 5100 — {{DATE:DD MMM YYYY}}

## Context
Lecture / Reading / Assignment / Idea

## Key Concepts

## Diagrams / Models

## Questions

## Action Items
- [ ]
```

Duplicate this file and change only:
- course name
- title line

---

## 5. Button (single universal button)

```button
name New Course Note 🎓
type command
action QuickAdd: New Course Note
```

---

## 6. Final UX (what you get)

1. Click **New Course Note 🎓**
2. Dropdown appears:
   - CSCI-5100
   - CSCI-5308
   - CSCI-5408
3. Note is created:
   - Correct folder
   - Correct name
   - Correct template
4. Cursor ready at top

This scales to **any number of courses** with zero friction.

---

## Optional next upgrades (tell me when ready)

- Auto-detect **lecture vs assignment vs idea**
- Auto-link to **course MOC**
- Auto-increment lecture numbers (`5100-L12`)
- Daily notes → course notes backlinking
- Dataview dashboard per course

This macro setup is exactly how power users run Obsidian long-term.

---


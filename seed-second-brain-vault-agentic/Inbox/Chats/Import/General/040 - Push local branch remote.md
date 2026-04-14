---
title: Push local branch remote
category: General
priority: Medium
starred: None
created: 2025-11-28T14:54:11.848597
updated: 2025-11-28T15:07:02.402550
dg-publish: true
---
# Push local branch remote

**Priority:** Medium

## Conversation

### Assistant

To create a new branch **from `dev`**, follow these steps:

1. Make sure you are on the `dev` branch:
```
git checkout dev
```

2. Create a new branch from it:
```
git checkout -b feature-branch-name
```

(or any branch name you want)

3. If you want this new branch on the **remote** as well:
```
git push -u origin feature-branch-name
```

That’s it.

---


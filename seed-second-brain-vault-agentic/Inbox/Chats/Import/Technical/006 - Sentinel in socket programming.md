---
title: Sentinel in socket programming
category: Technical
priority: Medium
starred: None
created: 2025-11-30T10:31:57.077437
updated: 2025-11-30T10:43:24.578526
dg-publish: true
---
# Sentinel in socket programming

**Priority:** Medium

## Conversation

### Assistant

To merge `init` into `dev`:

### 1. Switch to the branch you want to update
You want `dev` to receive the changes from `init`:

```bash
git checkout dev
```

### 2. Merge the other branch into it
```bash
git merge init
```

### 3. Resolve any conflicts (if shown), then:
```bash
git add .
git commit
```

### 4. Push updated `dev` to remote
```bash
git push origin dev
```

### Summary
- Checkout **dev**
- Merge **init → dev**
- Resolve conflicts
- Push

If you want the reverse (dev → init), switch the order.

---


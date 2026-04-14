---
title: CI/CD pipeline setup
category: Health
priority: Medium
starred: None
created: 2025-11-18T09:39:27.732541
updated: 2025-11-18T11:43:41.668308
dg-publish: true
---
# CI/CD pipeline setup

**Priority:** Medium

## Conversation

### Assistant

No. It will **never** run on old code.

Here is the important point:

# GitLab Runner *always* receives a fresh copy of the latest commit
Even if your VM itself never runs `git pull`, the **runner still gets the latest code** directly from GitLab.

### Why?
Because every GitLab CI job starts by **checking out the commit** associated with the pipeline.

This happens automatically with:
```
git clone
git fetch
git checkout <commit>
```

So the runner always scans the **exact commit** you just pushed.

---

# Summary

### Does the VM need to keep the repo updated?
**No.**  
The VM does not need to run `git pull` manually.

### Will DPI always run on the latest code?
**Yes.**  
The runner always checks out the specific commit triggered by the pipeline.

### Why?
Because GitLab CI injects the repo for each job before running any script.

---

If you want, I can show you the exact internal steps GitLab runs before your script executes.

---


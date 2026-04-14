---
title: Ls files with sizes
category: General
priority: Medium
starred: None
created: 2025-11-30T17:34:28.394299
updated: 2025-11-30T17:34:33.985229
dg-publish: true
---
# Ls files with sizes

**Priority:** Medium

## Conversation

### Assistant

Use `ls` with the `-l` or `-lh` flags.

### Show files with exact sizes (bytes)
```
ls -l
```

### Show files with human-readable sizes (KB/MB/GB)
```
ls -lh
```

### Only files with sizes, sorted by size
```
ls -lhS
```

### Reverse size sort (smallest first)
```
ls -lhSr
```

### Show hidden files too
```
ls -lha
```

These work on Linux and macOS.

---


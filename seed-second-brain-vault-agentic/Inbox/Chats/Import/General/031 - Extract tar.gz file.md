---
title: Extract tar.gz file
category: General
priority: Medium
starred: None
created: 2025-12-05T13:30:13.766318
updated: 2025-12-05T13:30:18.897085
dg-publish: true
---
# Extract tar.gz file

**Priority:** Medium

## Conversation

### Assistant

Use the `tar` command.

### Basic extraction
```bash
tar -xzf file.tar.gz
```

### Extract to a specific directory
```bash
tar -xzf file.tar.gz -C /path/to/destination/
```

### See contents before extracting (optional)
```bash
tar -tzf file.tar.gz
```

### Common flags explained
- `x` → extract  
- `z` → use gzip  
- `f` → file name follows  
- `t` → list contents  
- `C` → change directory before extracting  

This works on Linux and macOS.

---


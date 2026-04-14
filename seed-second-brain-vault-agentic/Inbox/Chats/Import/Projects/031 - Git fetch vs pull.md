---
title: Git fetch vs pull
category: Projects
priority: Medium
starred: None
created: 2025-11-19T23:06:33.904553
updated: 2025-11-20T00:30:37.155396
dg-publish: true
---
# Git fetch vs pull

**Priority:** Medium

## Conversation

### Assistant

Yes.  
You can redirect the output of any Git command to a file.

### **Simplest way**
```
git log --follow --name-status -- node_modules > log.txt
```

This creates `log.txt` in the current folder.

### **If you want to append instead of overwrite**
```
git log --follow --name-status -- node_modules >> log.txt
```

### **If you want the file in a different path**
```
git log --follow --name-status -- node_modules > /path/to/output/log.txt
```

### **If you want color removed (recommended)**
Git adds ANSI colors sometimes. Remove them using:
```
git -c color.ui=never log --follow --name-status -- node_modules > log.txt
```

Let me know if you want a cleaner summary or need help reading the log.

---

